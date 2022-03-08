from email.mime import audio
import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.asr.v20190614 import asr_client, models

def s_r_post(audio_):
    try:
        cred = credential.Credential("AKIDEI6evwoPDm58uPdaGfneEXYJn0wb07xW", "JL5YlhMjqgFXYIlxsXu0pNedLmwpxoQl")
        httpProfile = HttpProfile()
        httpProfile.endpoint = "asr.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = asr_client.AsrClient(cred, "", clientProfile)

        req = models.CreateRecTaskRequest()
        params = {
            "EngineModelType": "16k_en",
            "ChannelNum": 1,
            "ResTextFormat": 0,
            "SourceType": 0,
            "Url": audio_
            #"Data": audio_
        }
        req.from_json_string(json.dumps(params))

        resp = client.CreateRecTask(req)
        #print(resp.to_json_string())
        Task_ID = json.loads(resp.to_json_string())["Data"]["TaskId"]
        return Task_ID
    except TencentCloudSDKException as err:
        print(err)

if __name__ == "__main__":
    audio_ = "https://www.recaptcha.net/recaptcha/api2/payload/audio.mp3?p=06AGdBq25uB24yhUeoKc80gS50ivsr2ooPKeQj97_4IzC6wR2ZUwC4f8WkuXkcL_XGI_u5ioYQbYOmYWw9sa2k8NZySZlxptg0_6usN4wP3AV2u1d4JpPGrbNuB47RZvX7TYadNb0kAWoxqdlFTgpQS9JHnEXSTnrAXphiUrb7ddPC37lEeigCpnJL47iCirChbL8xROCxNDHs&k=6LdZ3_YZAAAAALyzLQjyjE6RPFdcG9A-TLr6AxF0"
    print(s_r_post(audio_))