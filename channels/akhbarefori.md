<div dir="rtl" align="right">

<style>
.tg-channel-box {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
  font-family: system-ui, -apple-system, 'Segoe UI', 'Vazirmatn', Tahoma, sans-serif;
  background: #fafafa;
  border-radius: 20px;
  line-height: 1.7;
}

/* حالت دارک برای کسانی که تم دارک دارن */
@media (prefers-color-scheme: dark) {
  .tg-channel-box {
    background: #1a1a2e;
    color: #eee;
  }
  .tg-post {
    background: #16213e;
    border-color: #0f3460;
  }
  .tg-post-header {
    background: #0f3460;
  }
  .tg-footer {
    color: #aaa;
  }
  .tg-text a {
    color: #7eb6ff;
  }
}

/* کارت پست */
.tg-post {
  background: white;
  border-radius: 20px;
  padding: 18px 22px;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 1px solid #e5e7eb;
  transition: box-shadow 0.2s;
}
.tg-post:hover {
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.tg-post-header {
  background: #f3f4f6;
  margin: -18px -22px 16px -22px;
  padding: 10px 22px;
  border-radius: 20px 20px 0 0;
  font-size: 13px;
  color: #4b5563;
  border-bottom: 1px solid #e5e7eb;
}

/* نقل قول / فوروارد */
.tg-forward {
  background: #eef2ff;
  border-right: 4px solid #3b82f6;
  padding: 8px 14px;
  border-radius: 12px;
  margin: 12px 0;
  font-size: 13px;
  color: #1e40af;
}

/* متن */
.tg-text {
  font-size: 16px;
  margin: 14px 0;
}
.tg-text a {
  color: #2563eb;
  text-decoration: none;
}
.tg-text a:hover {
  text-decoration: underline;
}

/* تصاویر */
.tg-photo {
  margin: 12px 0;
  text-align: center;
}
.tg-photo img {
  max-width: 100%;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* آلبوم */
.tg-album {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
  margin: 12px 0;
}
.tg-album-item {
  overflow: hidden;
  border-radius: 12px;
}
.tg-album-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: transform 0.2s;
}
.tg-album-item img:hover {
  transform: scale(1.02);
}

/* ویدیو */
.tg-video {
  margin: 12px 0;
}
.tg-video video {
  width: 100%;
  border-radius: 16px;
  background: black;
}
.tg-dl-btn {
  display: inline-block;
  background: #3b82f6;
  color: white;
  padding: 6px 14px;
  border-radius: 24px;
  font-size: 13px;
  text-decoration: none;
  margin-top: 6px;
}
.tg-dl-btn:hover {
  background: #2563eb;
}

/* فایل */
.tg-doc {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 12px 16px;
  margin: 12px 0;
  display: flex;
  align-items: center;
  gap: 12px;
}
.tg-doc-icon {
  font-size: 32px;
}
.tg-doc-info {
  flex: 1;
}
.tg-doc-title {
  font-weight: 600;
}
.tg-doc-extra {
  font-size: 12px;
  color: #6b7280;
}
.tg-doc-link {
  background: #3b82f6;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  text-decoration: none;
}

/* نظرسنجی */
.tg-poll {
  background: #fef9e3;
  border: 1px solid #fde047;
  border-radius: 20px;
  padding: 12px 18px;
  margin: 12px 0;
}
.tg-poll h4 {
  margin: 0 0 10px 0;
  color: #854d0e;
}
.tg-poll ul {
  margin: 0;
  padding-right: 20px;
}
.tg-poll li {
  margin: 6px 0;
  color: #a16207;
}

/* فوتر پست (تاریخ و بازدید) */
.tg-footer {
  font-size: 12px;
  color: #9ca3af;
  margin-top: 12px;
  padding-top: 8px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
.tg-footer a {
  color: #6b7280;
  text-decoration: none;
}
.tg-footer a:hover {
  color: #3b82f6;
}

/* هدر کانال */
.tg-channel-header {
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 28px;
  color: white;
  margin-bottom: 24px;
}
.tg-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 4px solid white;
  margin-bottom: 12px;
}
.tg-channel-header h1 {
  margin: 8px 0 4px;
  font-size: 24px;
}
.tg-channel-header p {
  margin: 4px 0;
  opacity: 0.9;
}
.tg-channel-desc {
  background: #f3f4f6;
  padding: 14px 20px;
  border-radius: 20px;
  margin: 16px 0;
  font-size: 14px;
  color: #374151;
}
.tg-last-update {
  text-align: center;
  font-size: 12px;
  color: #9ca3af;
  margin: 16px 0;
}
.tg-telegram-btn {
  display: inline-block;
  background: #1e88e5;
  color: white;
  padding: 8px 18px;
  border-radius: 30px;
  text-decoration: none;
  margin: 12px 0;
  font-weight: 500;
}
.tg-telegram-btn:hover {
  background: #0b5e8a;
}
@media (prefers-color-scheme: dark) {
  .tg-channel-desc {
    background: #1f2937;
    color: #d1d5db;
  }
  .tg-post {
    background: #1e1e2f;
    border-color: #2d2d44;
  }
  .tg-post-header {
    background: #2a2a3b;
    color: #bbb;
    border-color: #3a3a52;
  }
  .tg-doc {
    background: #252535;
    border-color: #3a3a52;
  }
  .tg-forward {
    background: #1f2a3a;
    color: #90cdf4;
  }
}
</style>

<div class="tg-channel-box">

<div class="tg-channel-header">
<img src="https://cdn4.telesco.pe/file/O9LKj1Nmkh2fkDLMfdNxOlU_C0KkNVDgd85j-_4C_s2nLcreJANANuxd_vx-_kEb9vSA0_j4KocvTmmZJnHEB7SCxpycY_CfEFy6dtpgvcXpegT5HdnMSapQDvXVxKxa3jvqVaN0yQsrjOvalTilxbYCBMeHY7vuZLSl6iHlo9Nuo8c9-3mxTZEKetnU2I59psxegz4931VMLAHmMx-MfRy77CUNhmzy_rhmw-RNP_aW19tSVXxd9xMn57uak-uyIcr270EgNFElnIvKZ4UsP7QRdWHFdSjnSUuIX6lNIf77EySW1gJkChw6BxlM9j2_0u7u_hOwK49hIx2jWsoGaA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.31M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-11 21:34:41</div>
<hr>

<div class="tg-post" id="msg-695283">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AzSGQsHmkiZdO_08iw_YtRCeNVl7JY8KgszWQmabZXOHAWAAbdp0zAoSDRcjn0hMZbSCpYEYqodEjVzsnsuUoCu7VFj-i1Bj-NXT95HavxHa3h3_uhOZF9SDtZyuTPVC0f3rVMrwh8YDpp2sbqJCDTFclsk8RVCFYew63likb0kYice5INcW7ibbjqJQxPzQtw1VmaySPBAfpR9oiORJLIErrssveArN2m-PuHfIomrNnF7jPIO4ayW9m3kpyfvEOvC-hT7fMJz8xsDlnD1ldxRVdymubCde-EdhJ_q2dsHpWETi47ITErTBdSA7FS91XiThvn06c8LjJBMON8XzWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WQhJOIXfIwdCO7szi5ShUkjd85qqUYLk0HHwqiO3qtzi26MPGPdUa4z2KKh_nLwVVxBp1oDIQHna1UWbzfW4iqpNHaWdJuhql-yRDhj-ecabz92Tguvl1PNyfTDRRvDCHY-0IZlTnJJVPyjJNVSrn5iWqnee9-LGKarpVGAKPbD_w4NUPLynjG6xIimMtqUXpJFvUsjZDL81rhCfHpsxThdsmp43Iet90T75Yd4zVYC-SKIbeG25kvjXmBrv61Y3byGuvnUTq4ocXaNw7GjnOfS7lvNUNbi7n3DvtDxshRtV85u_fsamhJPkYOwaV5TSz15CagWs8-9be-Gr6ZX2tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WqFEGvNXEH5wFZ81TlvQlNV5fd4Trw0jq30Ed4k2BcG66iI1zp351P0iyioAKH2VudZQzdbZj020aPAa0dL50pVpIMrrp-2YC50xK52cnk2ba-ce4SI82bnk_JL_CK057mYDLUKazE8EXkQJ-Cmyw6nefEjx2zO0rBe-3zjpjdj2S0biAvdZlMJTTvof9t0_Nb2OlkCMjwAxALy3Z-wAuVHrYXb7gPB9WlNIPFRJOA6IWqpD2DzNR4PhqtcxYrKXEmGEKGzUhusBwyCxhPT0cqEZ8-oRcB3XE1hogjNlezFp8FMwLSh93EKQSBnPNajKCWYiSLAJ20QMqoOIvJXjow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nlWPXADIRy3ZyBukUyMzX4NPGVwlb6BuVHhPbWVRFjpYHguEWebawFgDcbcCHkEjHQx6bXaOzvdpRV2FKcI4oOYdySHh46BdHJPmdH1MUKrTIEo2Jcd54wLFqj0IEesRHYEwdn39hU0kHwkhktv34UJnToOEd3ZXOeMPhnBjk-Cy_Q42G0L9TttZ-dpSUuK9f99MTSNgsENdF-hVBFjfzqbSpVGDJ5zdoX4x-wAgCvRDDcsLwWBSKtyuwyiDpvZrPt-6pPGmuE3N9hQHXelBq84_sCl82cxiN_FhC9mT9H1VHZuSGVjtZpqxduKm4flZTi6H1uX_5wvaOLBri96xIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
کدهای مخفی ChatGPT
🤖
#هوش_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/akhbarefori/695283" target="_blank">📅 21:31 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695282">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gy9MsCYTXFNNDw3SuEOkvYoFrBMCHgzjtTPxvSe_wApGVpp6CNP72PvezBOcmVRUzgwWSjiLwaZcJBkbgCxU6midqRt9PrriLgliDYh_Rtd29OVC94AcCpJsgGPbcKwUzArs5-_nrITrsNrDoaXrzifp1uL1xITH6Ml2yTz4S2XcD6SFS7z3Vs2_iLToqJSwqH3LBZunmfFecPE4AjQy4FHy4qK1hC9LCAIbnChkuia_5-AEuw_Fqm7n62Ghmr-F2KSEWabPPOphbv2WEiq9SR2xgd4ZY0kb1QGVm5EgSox7dKhEISlLvtcYhmDJFQmDGgwyUkohR3LnINA_bRYqVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نتیجه‌ای عجیب در لیگ ملت‌های اروپا؛ کرواسی با ۷ گل مقابل انگلیس تحقیر شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/akhbarefori/695282" target="_blank">📅 21:29 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695281">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2882858491.mp4?token=klvx7ebs4l4relihRjLTax2mELrBS4z4u4zfa_RjGv7Fg1Ia6OEQd0kFkTClIZFdAy9qq-gM41g8Rt-LzFQeI4WT3gnvEQfbtQTdQ7LNl5MyzVLkVETSf9J6UMh1seC0J9YzX2MJYnOReCZ42_dbtt6-XesVevuPJWFqjN7EEKI69bwzISptTT9icyMC3PogKymFWfwdv_CFIi0ntOtMs-jktmcjmRlCxTW-W7TLgCSipgnGhki4oMZ6NqXzZZUa-AfF9KsqgYZ_e5Qu13ITbCAXSQKap8Ew5R7d1p1wrXfOGetCnRDalcUDEHxakpbmk3vaXvJdSJz6mAV9a0HH1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2882858491.mp4?token=klvx7ebs4l4relihRjLTax2mELrBS4z4u4zfa_RjGv7Fg1Ia6OEQd0kFkTClIZFdAy9qq-gM41g8Rt-LzFQeI4WT3gnvEQfbtQTdQ7LNl5MyzVLkVETSf9J6UMh1seC0J9YzX2MJYnOReCZ42_dbtt6-XesVevuPJWFqjN7EEKI69bwzISptTT9icyMC3PogKymFWfwdv_CFIi0ntOtMs-jktmcjmRlCxTW-W7TLgCSipgnGhki4oMZ6NqXzZZUa-AfF9KsqgYZ_e5Qu13ITbCAXSQKap8Ew5R7d1p1wrXfOGetCnRDalcUDEHxakpbmk3vaXvJdSJz6mAV9a0HH1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه تخریب برجک زندان گوهرشت⁩⁩
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/akhbarefori/695281" target="_blank">📅 21:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695280">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f50698e369.mp4?token=VYUuYhzD_Yx-ZVoWEJhvaUV2y1EFJsvxCd1DS2lgjBvTVcuUcoqBXq-SNtidwwDk7eECFGbuxIEAeWLvM1A3uZPbUitgt13M6O9XVh6Zj17CyVvnmq4tJHeKIBy46Z5wydxle8hhGixnNhbb06TdEQ98Qoetjwqft501UDgIBj0H-3rlNVwBdlWqEhqCtsb84GgZ7HZF_Zcvo-kwI-daeVqI9eX-4E7LgKG3mTG-4MtCZaky2q1ZzWoi5Jx--N4gDV6ntqT3W121_DmjP63ROZtzleImboJ2pwntsBwsOaRFnPo7gjNaKfQzi2ybkvYsKHHb9M3CH9Zqr9tRvBGOXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f50698e369.mp4?token=VYUuYhzD_Yx-ZVoWEJhvaUV2y1EFJsvxCd1DS2lgjBvTVcuUcoqBXq-SNtidwwDk7eECFGbuxIEAeWLvM1A3uZPbUitgt13M6O9XVh6Zj17CyVvnmq4tJHeKIBy46Z5wydxle8hhGixnNhbb06TdEQ98Qoetjwqft501UDgIBj0H-3rlNVwBdlWqEhqCtsb84GgZ7HZF_Zcvo-kwI-daeVqI9eX-4E7LgKG3mTG-4MtCZaky2q1ZzWoi5Jx--N4gDV6ntqT3W121_DmjP63ROZtzleImboJ2pwntsBwsOaRFnPo7gjNaKfQzi2ybkvYsKHHb9M3CH9Zqr9tRvBGOXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اثری که مکیدن انگشت روی استخوان فک و دندان ها میزاره رو جدی بگیرید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/akhbarefori/695280" target="_blank">📅 21:21 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695279">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
ادعای وزیر دفاع انگلیس: ایران نیات خصمانه دارد و تهدیدی برای ما و متحدانمان است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/akhbarefori/695279" target="_blank">📅 21:19 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695277">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bcc3c3cd9.mp4?token=c-KjVl-Yw1EJrlfYt4UQxIDg-4xmAHj4w-7E2V1Zg7yVDhdwtbmvSXKWoc_VAPVhoQoAWOrUd5wDtIN6V5H6iT-eG3hXZZxdIDsCxSfgxVqqerPaob5j-_yYqaOHnD8eFTtFhNDKRogeSz-NuEhOotjNz2yRZ47WBGZKNMo35JEdUle0Zyn2i02H5F5HLRf1YFbaxoXwNNedzUdKgjwqPxgQRxvvJ0CMW9mk4Tlu1b54fFTfjifvtPJmqWbevESxKNe-I3snwU4oE6ixhRugh6jqc7OMrUf8VD9S3ry3FUllvSpxDv2eZVj-MEPpUlTMGzwpYYm5XmXT0F5EndNRPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bcc3c3cd9.mp4?token=c-KjVl-Yw1EJrlfYt4UQxIDg-4xmAHj4w-7E2V1Zg7yVDhdwtbmvSXKWoc_VAPVhoQoAWOrUd5wDtIN6V5H6iT-eG3hXZZxdIDsCxSfgxVqqerPaob5j-_yYqaOHnD8eFTtFhNDKRogeSz-NuEhOotjNz2yRZ47WBGZKNMo35JEdUle0Zyn2i02H5F5HLRf1YFbaxoXwNNedzUdKgjwqPxgQRxvvJ0CMW9mk4Tlu1b54fFTfjifvtPJmqWbevESxKNe-I3snwU4oE6ixhRugh6jqc7OMrUf8VD9S3ry3FUllvSpxDv2eZVj-MEPpUlTMGzwpYYm5XmXT0F5EndNRPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیل امروز عظیمیه (بام) کرج/ خودروها را آب برد
#اخبار_البرز
در فضای مجازی
👇
@akhbare_Alborz</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/akhbarefori/695277" target="_blank">📅 21:18 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695276">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HcUNWlsvnG_LkQOg1Q9MJZAlzdrOSr6Re3PEDRGr1r4KycGmt9rg2HHoSdmM-UrdhsRbV-KCPvOOHgnynPDgHf2DblAUFohzuS55c_HkQRTF60Iwc8kUWCE0C09NBZ7WZg4ivjJSKzAzJlAaskD8O0-RjhtdTZ2dmV3OS0bYXhh8mRwhnnMF-1mj6OXh_FKKrqhlW5hOVCIXTnmYGwrEe0-5Gz88inA0eSVk9FdgrvHreVeudxO7lYJfH8e6wykYnyuXxPIDt2SlK9gLJJ7k1hXyn8RhmZQHFufaTKDyyrCOTKyyeHueWY86SMg1Z2iYCUTxTJqtunDn0tsn_jD3Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گلشیفته فراهانی در راه بازگشت به ایران | نشانه‌های بازگشت او چیست؟
🔹
انتشار خبرهایی درباره احتمال بازگشت گلشیفته فراهانی به ایران، بار دیگر نام این بازیگر شناخته‌شده سینمای ایران را به یکی از موضوعات بحث‌برانگیز فضای مجازی تبدیل کرده است؛ با این حال، برخلاف برخی روایت‌های منتشرشده، تاکنون خبر معتبری مبنی بر قطعی‌شدن بازگشت او یا تکمیل مراحل اداری این سفر تأیید نشده است.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3249711</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/695276" target="_blank">📅 21:14 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695275">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZlFuYHhmUhBGOSobz3U1FwxB8oh9k4bTD6t6yq9Wk4-e9004DpFS91Jw0XWY68YqQ0n60aPCK955zeNgq4YXl7QXh1DrXlALOeE4U1CHtuQAOjEI_unmZUeCyOLZxO6UXGSW2FtLXGMwFyhvzSewEbiaz56fwoG1bNqpWnU5ejbJ5XxLfcVeF6soKzaETctWAWaX1G1qfTLVAJnz1pkonFOtGUmFlRhTOY25ytQc8zOuAu9R2use5cjde5oc03QoRiEswI71EK4ts0P6W28zD4EISlpWRCvbE4g3x9UfjUkmzBqe8nfQe7sBNJIwJ8t_yMr5Xcv7dh2h7iVTMmipHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قانون ۲ دقیقه‌ای؛ شروع کن، حتی خیلی کوچک!
جیمز کلیر نویسنده کتاب عادت‌های اتمی این‌طور می‌گوید:
🔹
شروع کردن همیشه نیاز به انگیزه‌ زیاد ندارد؛ گاهی فقط باید کار را آن‌قدر کوچک کنیم که ذهنمان دیگر مقاومت نکند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/695275" target="_blank">📅 21:09 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695274">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
منظومه شمسی زودتر از تصور ما نابود می‌شود
🔹
پژوهش جدید: پس از مرگ خورشید، مدار سیارات بیرونی حدود یک میلیارد سال بعد ناپایدار و منظومه فروپاش می‌شود. زمین، عطارد و زهره پیش‌تر در مرحله غول سرخ از بین می‌روند./ دیجیاتو
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/akhbarefori/695274" target="_blank">📅 21:09 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695272">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XqZkpLGzAbypYXfSJl-SDTF_vDlmj89wEGwARz0rtwYXWW_luVdvtcGn4Uv0LcPQWCZ6TgztlvAVcz3cvMFcLB_PYt5H9pgT3cPuvkCrc8qgZ1szwg7zo8uyg4xneoUos-nxThm8XdBV9gsUUqxABFM5rFU9hOq-Bj44M8lTqaUzqFJlfStWKNQ0_TRDymE0fc39fjOW3tm8CSn7qIuEAMaul25gpJqSi14A_buKQlo-gUywiqCh400Kn5AJ1sXRz2g62wl9TGb-CvS9Yx75ZE0gbH1PSNnKsydmc3njH_Y9yPRA6Ye90gzwELtkr8iGTQdrGlP89HRXRgX2wR7PrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd9fe5b7e4.mp4?token=caw-APB030aOXagdNJObeyt9LCrPS3LaKWfe3E2c5IxeXBRgJpJXfYPM-a4fktxKPaYvYadKyjsbpIOV5Z8sS9direbggSNZPO1x8JMRb4Z8Ldt0XqFQ0Mg4GImyM6JEeFB5k_o7PfaQ9F-HfbqrdYWslqnFyJjfhZWD2SUt9lrEXat2VotCxeaEsmZ6dDIq7sIbdpENfk856el2hIYFkg80ZE7Roiz9YjOaiLqF9ydfWlT7GQFIDIE91P7wSEZZYw0GxwmTfxlmK8p-5nc1GsdDjXxoCFlW9gJWqmlChQlfHmwzqR6iiPBsc6iAOTyYQ2Ffbakw6Uanjb1JvcOKoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd9fe5b7e4.mp4?token=caw-APB030aOXagdNJObeyt9LCrPS3LaKWfe3E2c5IxeXBRgJpJXfYPM-a4fktxKPaYvYadKyjsbpIOV5Z8sS9direbggSNZPO1x8JMRb4Z8Ldt0XqFQ0Mg4GImyM6JEeFB5k_o7PfaQ9F-HfbqrdYWslqnFyJjfhZWD2SUt9lrEXat2VotCxeaEsmZ6dDIq7sIbdpENfk856el2hIYFkg80ZE7Roiz9YjOaiLqF9ydfWlT7GQFIDIE91P7wSEZZYw0GxwmTfxlmK8p-5nc1GsdDjXxoCFlW9gJWqmlChQlfHmwzqR6iiPBsc6iAOTyYQ2Ffbakw6Uanjb1JvcOKoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری نزدیک از آتش‌سوزی گسترده در پالایشگاه سعودی آرامکو در ریاض، حومه جنوبی شهر ریاض، در مرکز عربستان سعودی
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/695272" target="_blank">📅 21:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695271">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JsOhGw_zO_PdN1_eCmjZ7BrYnH0OxkOEv3FAyyoHvdOGgJfJ84yC8VPBIzQddG-xASeItbFJ44uLHBVbTsqPvvykWBnsn24H76WC4g5XY4HwtPBMb6uDk6rHRkGMap3o1lXRkd6YzCC_h8oB1vCNpIhg5uvH_I2-6Tqlxde6aP_lvVkISaqEzeZMA8lWq91YoPS5yI7wdIDJfiI4VM8HksKcPxJ-NkkVg7urCN-jVGzY0RbyTh6mTszT81U5SWbwtIh_vtjrMzMaw-DckRZNS8Pox1f-3YR10QM5EseCWRnqVC-RLEpQWueHLJJgFUExBiNZulgCruXV3NMeyr0AMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معاون علمی رئیس جمهور:  قدرت یعنی حق انتخاب؛ هر فناوری باید یک گزینه تازه پیش پای ایران بگذارد
🔹
دکتر افشین معاون علمی و فناوری ریاست جمهوری، در جمع نخبگان و سرآمدان فناوری در
مشهد مقدس
با طرح این پرسش کلیدی که «از تمام دستاوردهای علمی چه میزان قدرت برای ایران ساخته‌ایم؟» تأکید کرد: قدرت معنایی تشریفاتی ندارد؛ قدرت یعنی حق انتخاب.
وقتی زنجیره‌های تأمین مختل می‌شوند یا فناوری‌های راهبردی را به ما نمی‌فروشند، داشتن دانش فرآوری و فناوری داخلی یعنی وابستگی صفر و حق انتخابِ حداکثری.
کشوری که فقط یک گزینه دارد، در لحظه تصمیم‌گیری آسیب‌پذیر است. مسیر پیش‌رو مشخص است: از علم به فناوری، از فناوری به حق انتخاب، و از انتخاب به مرجعیت فناوری.
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/akhbarefori/695271" target="_blank">📅 21:00 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695270">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08eb3b2263.mp4?token=QSXmbZSJ1GHKOtHb2dYzcoMEqv_h1xAH3nRamx6Zv75IchPCtG-eWI0EdATjPL4ltbkhE4-IMcThbAxwT4Pks5-67LAA297tYLULOhxdLWDim-S5oWT33hgUBNiWA4Zp38_utxSNjmcoiUaxWdBSyUIIHnC3GUHBgfpwSrZimsfGcHg4FnTN-ciWKHkwLIMvsED8KXNIXlZYk_CqcrGAUIUFfpnfkp7k_1ebGY0uA_vtA4wr5bW1F1z2qYlNahJPuepAnjlLsQTM_hjND4gTwJ4HY5cHB3p9XHS0nB9wIt7BHxwp6e6eJM_mTWjZZkFLSdvOF6m_dy8DhPB8JJB61g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08eb3b2263.mp4?token=QSXmbZSJ1GHKOtHb2dYzcoMEqv_h1xAH3nRamx6Zv75IchPCtG-eWI0EdATjPL4ltbkhE4-IMcThbAxwT4Pks5-67LAA297tYLULOhxdLWDim-S5oWT33hgUBNiWA4Zp38_utxSNjmcoiUaxWdBSyUIIHnC3GUHBgfpwSrZimsfGcHg4FnTN-ciWKHkwLIMvsED8KXNIXlZYk_CqcrGAUIUFfpnfkp7k_1ebGY0uA_vtA4wr5bW1F1z2qYlNahJPuepAnjlLsQTM_hjND4gTwJ4HY5cHB3p9XHS0nB9wIt7BHxwp6e6eJM_mTWjZZkFLSdvOF6m_dy8DhPB8JJB61g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فعالیت پدافند در آسمان قشم
🔹
پدافند هوایی نوین نیروهای مسلح کشورمان در قشم موفق به رهگیری یک پرنده متخاصم و اجرای آتش در آسمان این جزیره شد./ تسنیم
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/695270" target="_blank">📅 20:53 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695268">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FWAip9C_OKXdJCtdsAON4GBuRAMibKn_osQE3JwIGl3yrX_O3ThPfmyDo7aZyBsgJ7vPFkwLP30jyOY7Bpo--WxIy6lJ1gAoHfMWxBsEGXLxgy4RemPOi-oezUNOLeBssGhAlAL9DmU1rtw9aa2tKePXTJoAt1lkllENUtxsm7J_56sKbXsLQwb5caHAA0ehw9P0dN8b5FxhRo-dipSmZN3C9JgnvurTmM1O1YLvldcngz4cnNGqF63trYlM1eDhK1vxHX12kw3W3iDgTcWJQ3W9ntikXWWRlGL2CRBP2lqdbK0WkWWeViB72S5j191sXZ-bvEs3SL1u05v-HKcqIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FNSeregDENQ7f0ern0i-INqtfug4uKogrQMtiWyS85KqN-xTMm0iRJYDxdOaE7dFdOdkCw7iaIn61hFa1giuQQS_yH81-6Y0abDLcr3eYSBw91Jv4ApCa0wtQVAlh3mswuaJnmmAmwPgDTIRBAFIIg_1RrQ8uDgxmFyOh3LT6ZzAuVYsDc0NsgK6g3BNBETqemq0bSoQtS3msyKYyFPAFj2uo4VHFRNIdZyG6cPv9hMdV6ECIIi9cSyC572rq3ZVGXjIxkuUNGXX7LKaLnzXeZJpIMlijG2hlS9xKGV8AvQUnemkoRNrKYX3haIYV3nrvsrZm6-nwMHiFp5yLLXkmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
موشک‌های پدافند هوایی «صیاد-۳» ایران در جزیره قشم شلیک شدند
🔹
این موشک‌ها بخشی از سامانه توانمند «۱۵ خرداد» هستند و حضور عملیاتی آن‌ها پس از دو جنگ اخیر، نشان‌دهنده اقتدار و بازسازی قدرتمند پدافند هوایی ایران است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/695268" target="_blank">📅 20:51 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695267">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
خرید نفت ایران توسط چین قبل و بعد از جنگ چه تغییر کرده است؟
🔹
پیش از جنگ، چین معمولا روزانه حدود ۱ تا ۵/۱ میلیون بشکه نفت ایران خریداری می‌کرد. این نفت عمدتا با تخفیف و خارج از بازارهای رسمی و در شرایط تحریمی معامله می‌شد. پس از تشدید فشار بر صادرات نفت ایران، اما جریان نفت ایران به چین به‌ شدت کاهش ‌یافته است./ روزنامه اعتماد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/695267" target="_blank">📅 20:49 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695266">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
ادعای برخی رسانه‌ها مبنی بر سفر عراقچی به امارات تکذیب شد/ عراقچی در تهران است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/695266" target="_blank">📅 20:46 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695265">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7379ba0ed1.mp4?token=j5Lzd-s-sJiJX2Zs8isig9w0LBv34y7ZvP3sUSIwpgdmNrP_z8RiPCTNKVKK8RdCqkRncL32hUDV7LyRjP6baXfLjvnfBg3PCyLcHM2OKrcSRwBciLyLpoD664_PaXTpiplajz7zfT6uDVZZHqilGOo-EIQsmCrbTQEs-RxoQBEVR7QnI_XTreNlymHBUhQ02VLR5t8ng0Nd_OZ8URchSh09POEJDqfH90yFiP9JF7rziT_jw-7b1oFjyCpv9ZriZLOYZRO9zQmhl0d9wQzhw-Kj9DuavLKXlxa_vBMMMNFGvCUAYVxVAwdUqQumOT91tJZ9wLpKXl5EfK8GHUzJyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7379ba0ed1.mp4?token=j5Lzd-s-sJiJX2Zs8isig9w0LBv34y7ZvP3sUSIwpgdmNrP_z8RiPCTNKVKK8RdCqkRncL32hUDV7LyRjP6baXfLjvnfBg3PCyLcHM2OKrcSRwBciLyLpoD664_PaXTpiplajz7zfT6uDVZZHqilGOo-EIQsmCrbTQEs-RxoQBEVR7QnI_XTreNlymHBUhQ02VLR5t8ng0Nd_OZ8URchSh09POEJDqfH90yFiP9JF7rziT_jw-7b1oFjyCpv9ZriZLOYZRO9zQmhl0d9wQzhw-Kj9DuavLKXlxa_vBMMMNFGvCUAYVxVAwdUqQumOT91tJZ9wLpKXl5EfK8GHUzJyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کاملا واقعی؛ با یک پیاز، شکر و مایع ظرفشویی کف قابلمه‌هات رو برق بنداز! #ترفند_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/695265" target="_blank">📅 20:42 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695264">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77c92db990.mp4?token=Co8IPFpOfP_cwK4a1mfbfcfTQpn01YjszU-91iz33bHLFb6_uLDIcarLwzUyUmo0Te21MP3TecdBnvlCbvbdNVdAASFm6FQQ3UKKF_xh-I70xQvUe7Iwz79Ne1Q4oBxGvS2IzMjRyc6F3yuQPAX32QBCCUmQI2XvZqNy1hmUsJHFuvJw9qd7Btd6J4r7cqZFHBaoivdH35h7-DsC6Fe8L22DMYZpUYIWeCw7CDaZIdIfAuimOZPuu2l4cZVN2nMzfd3FNSg8iq73os8Fg6u5G3k60pq-gTJuLHFnOvIdi5U_uJ9PpTGC7Qnm8DsGLu_LWcwVKZe2k2ZI_ZDH2je2Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77c92db990.mp4?token=Co8IPFpOfP_cwK4a1mfbfcfTQpn01YjszU-91iz33bHLFb6_uLDIcarLwzUyUmo0Te21MP3TecdBnvlCbvbdNVdAASFm6FQQ3UKKF_xh-I70xQvUe7Iwz79Ne1Q4oBxGvS2IzMjRyc6F3yuQPAX32QBCCUmQI2XvZqNy1hmUsJHFuvJw9qd7Btd6J4r7cqZFHBaoivdH35h7-DsC6Fe8L22DMYZpUYIWeCw7CDaZIdIfAuimOZPuu2l4cZVN2nMzfd3FNSg8iq73os8Fg6u5G3k60pq-gTJuLHFnOvIdi5U_uJ9PpTGC7Qnm8DsGLu_LWcwVKZe2k2ZI_ZDH2je2Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
درگیری آسمان تهران با برج میلاد امروز
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/695264" target="_blank">📅 20:39 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695263">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
معاون علمی رئیس‌جمهور: برای تحلیل دقیق‌تر کنکور به جای ۱۰ نفر اول، باید یک درصد اول بررسی شود/ منابع آموزشی یکسان در اختیار همه دانش‌آموزان نیست
حسین افشین، رئیس بنیاد ملی نخبگان در
#گفتگو
با خبرفوری:
🔹
هفته آینده تصویب دو آیین‌نامه برای حمایت از بازگشت نخبگان و استفاده از ظرفیت ایرانیان خارج از کشور در دستور کار دولت است.
🔹
منابع آموزشی مناسب هنوز به شکل یکسان در اختیار همه دانش‌آموزان نیست و برای تحلیل دقیق‌تر کنکور به جای ۱۰ نفر اول، باید یک درصد اول بررسی شود.
🔹
برنامه‌های جبرانی برای دانش آموزان جنگ‌زده جنوب، در اختیار آموزش و پرورش است و وظیفه بنیاد ملی نخبگان، شناسایی و حمایت از استعدادها است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/695263" target="_blank">📅 20:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695262">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BLBR0YXiCamHN4gixN6zODbI0XJxXZxylGbp46k26HKJN5MeoiPWgjQ0qwbEXGfP564tdjgw0i7qP9HelhXeSQtzdPWkUckRwkcoO4CTcCHQlqApwTHDFHg9LGUlsXTa_2FttIz5ljZ1vG61PzrCAUpnqG8fYg7hr-fI5IqjH2M_w0Xk-VJ4AxL7Pl-WFW2o0ppxD0rhW-1OsphhkBBiRxWW2rv8FJcKl1K_rcO87g1lR6kYF1CH4zWgaip_Y6PXA5pl2wCZfgGsECykCwEoaODm7JJMlMW_txCS98COhqIO3GEupetQ-6dmmVluVOEih6YD4TPOzJuNkrL_nOIEDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پدر و مادر رتبه‌های برتر کنکور چه شغل‌هایی دارند؟
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/695262" target="_blank">📅 20:32 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695261">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
مجوز روزانه ۴۰ پرواز ایران به نجف
🔹
رسانه‌های رسمی عراق از توافق برای انجام روزانه ۴۰ پرواز شرکت‌های هواپیمایی ایرانی از مبدأ و به مقصد فرودگاه بین‌المللی نجف خبر دادند؛ شرکت ماهان از این توافق مستثنی است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/695261" target="_blank">📅 20:29 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695260">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
محسن رضایی، دبیر شورای عالی امنیت ملی: شرایط کنونی از جمله دشوارترین مقاطع کشور است /روند مذاکرات بسیار جدی است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/695260" target="_blank">📅 20:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695259">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-Wkp6RUpWH2ZBGAxwK3R6m3SbvNGlvvfFF2RNx2a_JbQr_J2IKHVeKPdWdQ5DSfDmMhlFLJq6WCYY2QS8BkctWzJQBZfAR9oKchk_QeuabESiS3pqpmOWlFfRfCWEcSo-9Qs7rw1wgVjGnmhrfvrpWR0CHPgQLyLQ7tw1IeE_hLYObMIinFdCvuWiUOKnt2wKucL3j4EL0svS8jOeByATWQKx5JSG6Cj-urnCPa6WSgwtN59OnFAb3U3EkxWI80-lptWeO6uwZlyBcNSltZog8oFrzgIXxRkiksiMluG5yCboxKv1fwL_oxfYnVl1VIn7l7bVTPfp2pg1_tcegL_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
قاب گل متبرک فوق ضریح حرم مطهر امام رضا (ع)
ساخته‌شده از گلبرگِ گل‌هایی که روزی خادمِ حریم پاک رضوی بوده‌اند؛ یادگاری معنوی و ارزشمند از آستان حضرت رضا (ع)، برای نگهداری در خانه یا هدیه به عزیزان.
ویژگی‌های محصول:
✔️
اثری هنری با تکنیک رزین
✔️
قاب از جنس پروفیل
✔️
قابلیت نصب روی دیوار
✔️
دارای شناسنامه اصالت
💰
قیمت اصلی:
۷۹۸,۰۰۰ تومان
🔥
قیمت با تخفیف ویژه:
۶۸۹,۰۰۰ تومان
📩
برای ثبت سفارش و دریافت اطلاعات بیشتر:
@gharar_order
🤍
هر خرید از «قرار»، سهمی در مسیر خیر.
@ghararshop</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/695259" target="_blank">📅 20:22 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695258">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/328f198eff.mp4?token=p8IPswX9ZfhJ5wL8BaZdz55Ko8LH1IXNabtPUL_zkBGCRka4Ky2iQBZ1-WiYTA9rW7VYK5Z2gQ9kRJ0fvYtuZjijqt5mVlkBa_hYa0DQCGyzSQXU9BjxgSJNDO5W5v2cEnrNg66PqOydyo90sBwCuvZzdyJuBcOr7AeSHX3K3Zi4Oen2mN3glUXilt6w8EKNZszShsVTw5tzMmEZk6OxF3ihSss0lD7_s6Ogk4_3vbIbRIJ1PXxF8d53BzMPtLjygjz2vG1Gv1-CtROcA1scejpFR0B82ldHa77iy2WyuSX2e7EV6MBSPH5KkYPZR8IofC1xi5__1p5sBx5uVS776w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/328f198eff.mp4?token=p8IPswX9ZfhJ5wL8BaZdz55Ko8LH1IXNabtPUL_zkBGCRka4Ky2iQBZ1-WiYTA9rW7VYK5Z2gQ9kRJ0fvYtuZjijqt5mVlkBa_hYa0DQCGyzSQXU9BjxgSJNDO5W5v2cEnrNg66PqOydyo90sBwCuvZzdyJuBcOr7AeSHX3K3Zi4Oen2mN3glUXilt6w8EKNZszShsVTw5tzMmEZk6OxF3ihSss0lD7_s6Ogk4_3vbIbRIJ1PXxF8d53BzMPtLjygjz2vG1Gv1-CtROcA1scejpFR0B82ldHa77iy2WyuSX2e7EV6MBSPH5KkYPZR8IofC1xi5__1p5sBx5uVS776w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئوی جدید از سیلاب امشب کرج
#اخبار_البرز
در فضای مجازی
👇
@akhbare_Alborz</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/695258" target="_blank">📅 20:22 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695257">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
این کلمه‌های دو معنایی رو یاد بگیر و با یه تیر، دو نشون بزن! #زبان_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/695257" target="_blank">📅 20:19 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695256">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Frdj7ZY2Yb1WqU6s-UDV2lbyApFeu8ZK2gVdQasBBdBqLw2VRgJh3yu0prb7xLBqHtbG_hXMcGArmTiXRMjXKmZDY8zC_-WGDVun9ejjp_eb6rl9Vf_qXV8BAsVlz3SfyBDuHWiesXeJJsaha1SQ1cU6Sy3nSBQX30BODWaP8jw8yAwASNvRb8PDQWq_Ar_t_iQ7FllxJdvX5YLfjqpEcn3_24odvK5U1fkmRRq9fuJPcrf3r04QxwS9wf_MYQz9rAWKB_xSHODoIU-qtU81GOu4th0194WosX-eRu342UNsMqAt1FtzFDd9_vST7JnOzIYfjWiSsGF6IJCH_aUYfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نحوه استفاده از سهمیه جنگ برای کنکوری‌ها اعلام شد  رئیس سازمان سنجش:
🔹
متقاضیانی که ساختمان محل سکونتشان در جنگ‌های تحمیلی ۱۲ و ۴۰ روزه تخریب شده و قابل‌ سکونت نیست، با تأیید مراجع ذی‌صلاح می‌توانند فرم تسهیلات پر کنند
🔹
ساکنان شهرهای تهران، اصفهان، شیراز،…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/695256" target="_blank">📅 20:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695255">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
دستیار رئیس بانک مرکزی: اگر تورم را کنار بگذاریم نرخ امروز ارز با سال‌های ۹۷ و ۹۹ یکی است/ افزایش کنونی قیمت ارز گذراست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/695255" target="_blank">📅 20:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695254">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CzWbgEHkZMPuTpYQ7z85J9BJ0gSoZSSRSZ0KFTZJ9xYIiOvjRz_cgyqeR4lCPpZMZViwWzmL9tym3dGkiOzbCMfIW67QeB95aRnsQJsqtRgbCmM2g-gKgLsE7z5y9IwzXSUUuog3Ax9iraYkSWIVylMCNbZroSDgse_BpC4P-1UUvUwkDDXNxvTJ9eWeZnVDBg5gqWQ-uxKLgXYeoApGsJ6Ec97tXcb1vo7aOy4ptDAco7fidYI7syc7TBpDHWTX5d5b-wp57mBu_gwGbUrPmDjdBRS4HR9F1Xtgzv2I8KYG4KfhVdxpORluvasvDE-DOCIALH64jJNV5ke3gCoXHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جزئیات جلسه محرمانه کمپ‌دیوید درباره ایران | افزایش پرواز سوخت‌رسان‌ها؛ زمان حمله معلوم شد؟
🔹
گزارش‌ها از برگزاری نشست چندساعته و اعلام‌نشده مقام‌های ارشد امنیت ملی آمریکا در کمپ‌دیوید حکایت دارد؛ جلسه‌ای که در آن، گام‌های بعدی واشنگتن در جنگ با ایران و تحولات مرتبط با درگیری عربستان سعودی و حوثی‌ها در یمن بررسی شده است.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3249675</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/695254" target="_blank">📅 20:12 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695253">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJj4tQrjYC8GImRaxNCfrOlOpQseykvxCNyHfjcGL1pHYWEZxT5dG12KHZnt8tRmbCjZNlwl4iuQxQeGJj7i4EzpIlU1KnzqjLPGCcQvOY4BHjwcQLiXqnTeOhy_jq5PlpvgEHGKV2g1xliMr1impyEmv-AWZGm84zN5uHgU0r1I5nW6J0uKYqdPvpe39uhauroCETcBLOkC0v3XSArVE4q4GR3VzEiMPdvt3021ovrH1IrEyKZu2Eg6V2cy8E_CSJ5OKb-G0tl-SbWPOMePtT-vVUReVpNxD3M5rG_KdgNsctEIBdIr7gERcgtumRhubPXBDS2Zs5EdwcFM-pZHtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی: گام بعدی ایران، اخراج کامل آمریکا از خاورمیانه است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/695253" target="_blank">📅 20:06 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695252">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c30420132b.mp4?token=M4moYPJXYV3Q4TKKc2UILdtisacQi1FsYkt0QtrlRpf1pg7QGdRAcBMMilx5I39AgRhINUITNXr98V9-y2RxXB74YmLJEB0cgCKDKqUW4AiORnA32YVDdtD7HWarZrMr_b7teYC_ObZftE5t5EMqllRUKlShi51lfhFyEbeMTLdCQiKgIy3MUH6HrQL-lX7RETfRvl0GT6VxXUEMZ6rsRQUXh5LDsBB62BnIoZfDkHNVgfeOI3cLA2vnVge6_uEE-esr4ssFXhiKlNXkiBrErXuwriMJyIul_bUeOZDBbnPACRBSBjughWKWypzXN97Hn1GUKUvzjSpkDOXT6xthuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c30420132b.mp4?token=M4moYPJXYV3Q4TKKc2UILdtisacQi1FsYkt0QtrlRpf1pg7QGdRAcBMMilx5I39AgRhINUITNXr98V9-y2RxXB74YmLJEB0cgCKDKqUW4AiORnA32YVDdtD7HWarZrMr_b7teYC_ObZftE5t5EMqllRUKlShi51lfhFyEbeMTLdCQiKgIy3MUH6HrQL-lX7RETfRvl0GT6VxXUEMZ6rsRQUXh5LDsBB62BnIoZfDkHNVgfeOI3cLA2vnVge6_uEE-esr4ssFXhiKlNXkiBrErXuwriMJyIul_bUeOZDBbnPACRBSBjughWKWypzXN97Hn1GUKUvzjSpkDOXT6xthuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای سرهنگ بازنشسته تفنگداران دریایی آمریکا، مایک جرنیگان: ترامپ، در حال آماده شدن برای جنگی دیگر است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/695252" target="_blank">📅 19:53 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695251">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJYoUwHCZVeo6gnXpyC9AQ8zpx4GqmNzuDJaRzqeJCqgBLkQmsW_NjNmruUfUcDnUvjdKkdgLTDMJIK9FVIJSP-InRettgf7PSH0wcXa5XzNHcZ3iLKDLy-EzHTyL8yqtgSlMAnIi4pZDkXXlAOETiRV7Ga0DXodtKBpey5EOKV5Tn7UYZedluFjsKhp4ybB4F-0Tw5JXcl5QO_qZ1AsN8l7xyc5jLOgFSPF2OrFkemCYdxYHyFRVOM_-WFFHYzYRBFI-gtxiFXN-rUkQt_jgcYsm-T36k4tPQUx98s_A8VrX1J5VHvfgIigP5xVsgHDxWLCrphyM_EV2kjc_OCNXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گزافه‌گویی وزیر دولت امارات: امارات خواستار پیگیری اشغال جزایر سه‌گانه تنب بزرگ، تنب کوچک و ابوموسی توسط ایران است!
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/695251" target="_blank">📅 19:50 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695250">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
ادعای الجزیره: فرانسه پیش‌نویس قطعنامه‌ای جدید درباره آزادی دریانوردی در تنگه هرمز توزیع کرد
جزئیات اعلامی:
🔹
آزادی دریانوردی و حق دفاع کشورها از کشتی‌هایشان
🔹
حمایت از راه‌حل دیپلماتیک پایدار برای درگیری‌های منطقه
🔹
تشویق تلاش‌های داوطلبانه برای مین‌روبی و اسکورت دفاعی کشتی‌ها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/695250" target="_blank">📅 19:49 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695249">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/181095730a.mp4?token=dzuC6hffYuabbHLI08i1ljGEN6ReG5q-yAySFOZTMzuRGm0Cd_Kt_GqSrQqlx2yHThkh33vqOKWd6GfxOA3mq-SefU8cpplD57xBAu0CuVcDxcjVJlMeukELb0f4NkR46hLHcD3arayzfdyyL-B7DwFs5NymA2IoHU_OHlK3XSlY7YoRr1tYJE2lZ-GcU9hDu7BM7rPtc1O4dXS70P-1k9l3iV7FvM_whWfBsckfCD46B0wm0fFRsvpdKtC6gfzx4t1w0qzw6P0PJ3ssiwEFGyaITcwP58LnHNhf0ExwPAslOPeSzsZ9tvy3ZQhHSGHKMcULnd-HImzn4MQDGeIhsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/181095730a.mp4?token=dzuC6hffYuabbHLI08i1ljGEN6ReG5q-yAySFOZTMzuRGm0Cd_Kt_GqSrQqlx2yHThkh33vqOKWd6GfxOA3mq-SefU8cpplD57xBAu0CuVcDxcjVJlMeukELb0f4NkR46hLHcD3arayzfdyyL-B7DwFs5NymA2IoHU_OHlK3XSlY7YoRr1tYJE2lZ-GcU9hDu7BM7rPtc1O4dXS70P-1k9l3iV7FvM_whWfBsckfCD46B0wm0fFRsvpdKtC6gfzx4t1w0qzw6P0PJ3ssiwEFGyaITcwP58LnHNhf0ExwPAslOPeSzsZ9tvy3ZQhHSGHKMcULnd-HImzn4MQDGeIhsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری بیشتر از شدت طوفان و گرد و خاک در قم   #اخبار_قم در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/695249" target="_blank">📅 19:49 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695245">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QcpME37wulqdpHF6xusu6NL0xyUScUha6DdhiSVx_vHggKUzcFyCy4MNknmHg8CwLqTa3hRhM35IU5vcsyY9qGmuq6gNBWKT7jna3XRESFV3fsZGLaUWg8gUSHZHVT25YAId1yi9tc6l7D_EnjcR14CuC0hH80IfuwwTeFcP-aV_Uqs3iwHUoJ_HOXf0QaLrqEZEjoCRrmmIP3hIV4BmTKn3PMnDO8Th71e2YjM9S3yqgmxDekbY2X_fhK8ocWWUW7B2G4WaaUaWGjEiLsHut6_JH5qWLk3xdNdzDjkAJL2gDI_ITzCE6q0gmObmz5Wrw2E_KVnoHqMUZEIJ-CQIuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MumsGHTECmlmUMq--4UJq0lgE_AMlG0q91zi8aX6tfbdgQ01EYSfQpzLDwf7DgLhU3DsEsYBvP3Te0HhO-6PSrREGucGSlaQvNJBD6Hoh5WvPNoklZk4V2Vl5WBarTi6Rh_tATBf5mv-TRDZtraX5BhtbOg76HbrFRZk08ad7ssLxCuL1pVKXsOLIw-jGUoouin-QZ_5TuVQHMKNhqcBbfnjIo7pCZWyncNOkZxUBRJ7uNW7kIdQQ_e0XYwed8JT3MADUu6vDgNU6IFVx9B0Il4aWc2QgLkTC7kcUXYGhMMWI0PgxzHu9eiF6fFNlAlUOx20Pxq2KVUpUOnLOTomcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WDTWjk_Qg0RUO5-SQC6UDRzETg0OEFINQO0CwsJ9JBPgQf3NHpKpY1CNPNcTYJjU1nhjuaEQuuBwDgNU1dxkxgUMM5p3vkA9PuOCugTaipY0tUWUPpjZWxEKBbKx6fXjm0g83o_a6xY0nR6Ahp4jsK4Xp_XDHCKurs-4S0FJxKiz-qKs3CxZxmNtxqe_THIHnKaGr3hBE9wzQ-DLTgMd05n41BYsAcsfHz1abOoLhvgLDAMUKHcAl-jHbjlvxiOJppWGmY2kRGdPAnrqbPfeSpd2iOZdjpv5dZlE8zLde2Eu1G4-84Kw5uXIEQHO58WSNk9CjxNfo6EqW_mhKk6T0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YboScde2vF2O8R5qb5E9O3E9jAS5QigeqIcu28VKaSGWpyPfFrsllTtDPvzVyPK24Pt3JajvYqIwn5xCvthnnYCkkwRnYVDgyYCHl0jMt1YXXhJkCbX1nglfocKvBmNarze8leSCPmoKe31B-XaertvevL7NdqoEpP4cx4udJ7nTC1Qb06cxu6Zs-2PwcCnfkaykZ_ioqgnOZYdKtVqyqlqCuQkOdD2V2YeWDkWGeTreRVmDDUyYk9AQaQ_2xxaUGlnVt0t-5c8SDiDKbU7DizsR-ey3nqWz4VrZFOgP3mYKxaNgCz2WTNPBFpMQFr42LOMhxFKWEG9vBjo8hpK-uA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری باکیفیت از خسارت‌های به‌جا مانده از پاسخ ایران در پایگاه شاهزاده سلطان
🔹
پایگاه شاهزاده سلطان عربستان سعودی میزبان هواگردهای آمریکایی که از محل اسکان نیروها، سازه‌ها و آشیانه‌ سی۱۳۰ توسط نیروهای مسلح ایران هدف قرار گرفته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/695245" target="_blank">📅 19:46 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695244">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43cb2e134a.mp4?token=Fz08XNSE4GA2ijfHGarMP9qxPQ_erwFvxErU3oF54IlI8xtt7mMvaXFX96HFohP5cu-DQ5r-kWgCJ3-02FNlTIMFzBWOB-g9crrS0wDnoq-mhvn7WKmZxg_xezHTnJSfDKxwmDQDzWfty6AZsukln2MhPwTfv1diVSWjVDVEmfpU6QK66Ks6e8f_4eMaeO0D7mEV3Iv_3tzeNBa0JDQxYV3OPOYWAPMJGbj_TYadbpdmIN4jZy1LRfIsGSNNG7-eZ__-Zo7-jI-5EbMiPIJChuRSRSLCggvcByE44N4As8VrXDF8G6k4-wJa79lPhV7d6WIyywmTBLDmfEGNG82qyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43cb2e134a.mp4?token=Fz08XNSE4GA2ijfHGarMP9qxPQ_erwFvxErU3oF54IlI8xtt7mMvaXFX96HFohP5cu-DQ5r-kWgCJ3-02FNlTIMFzBWOB-g9crrS0wDnoq-mhvn7WKmZxg_xezHTnJSfDKxwmDQDzWfty6AZsukln2MhPwTfv1diVSWjVDVEmfpU6QK66Ks6e8f_4eMaeO0D7mEV3Iv_3tzeNBa0JDQxYV3OPOYWAPMJGbj_TYadbpdmIN4jZy1LRfIsGSNNG7-eZ__-Zo7-jI-5EbMiPIJChuRSRSLCggvcByE44N4As8VrXDF8G6k4-wJa79lPhV7d6WIyywmTBLDmfEGNG82qyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زنی که دو بار اعدام شد و زنده ماند!
🔹
کریستا پایت، قاتل همکلاسی‌اش در ۱۸ سالگی، ۳۰ سال است که در انتظار اعدام است. دو بار تزریق کشنده، دو بار زنده ماندن. دستیار قاضی: یا روش را عوض کنید یا جوخه تیراندازی.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/695244" target="_blank">📅 19:43 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695243">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32ba9bdbdc.mp4?token=VbtLRCzRqs5v3tpk-grVTUX_VOe-o7y7A8TWJcv9IPf29uYS-99rWOUHHAhK0V7b7UU_16p9kl8P31vvGNHjKky3q0EpO0ia0UimwJacaw2zufWViCmQAthQQwQ3YRXgY44FXIOFTFuJpVAIiEjqBNV9WrCDvu8OXPCJrXYu45MGecumlq5-g-K_-Qj724xNCAQ_oJuAdxeO1S9LZFKHKik-WkHS7_GKaVgoKm5F1FRJo5vNgJqhTqwudcskGz4bE0XTxmH2eWqu2py4GJ5gPnth8z6cPCrVjzoInI8sVnknzMk_LO2iUT0LuZwCMAh2CaTKGuU4EZ7XpQMgwGg9lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32ba9bdbdc.mp4?token=VbtLRCzRqs5v3tpk-grVTUX_VOe-o7y7A8TWJcv9IPf29uYS-99rWOUHHAhK0V7b7UU_16p9kl8P31vvGNHjKky3q0EpO0ia0UimwJacaw2zufWViCmQAthQQwQ3YRXgY44FXIOFTFuJpVAIiEjqBNV9WrCDvu8OXPCJrXYu45MGecumlq5-g-K_-Qj724xNCAQ_oJuAdxeO1S9LZFKHKik-WkHS7_GKaVgoKm5F1FRJo5vNgJqhTqwudcskGz4bE0XTxmH2eWqu2py4GJ5gPnth8z6cPCrVjzoInI8sVnknzMk_LO2iUT0LuZwCMAh2CaTKGuU4EZ7XpQMgwGg9lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ساسان زارع سخنگوی ستاد مردمی جانفدا خبر داد؛ تشکیل ۱۰ هزار یگان مردمی امداد و نجات با مشارکت «جان‌فدایان»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/695243" target="_blank">📅 19:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695242">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
آموزش گام به گام اعزام به خدمت سربازی
🔹
آماده‌کردن مدارک: کارت ملی، شناسنامه، مدارک تحصیلی و مدارک لازم.
🔹
مراجعه به پلیس +۱۰ : درخواست اعزام به خدمت رو ثبت می‌کنید.
🔹
دریافت برگ آماده به خدمت: تاریخ اعزام مشخص می‌شود.
🔹
انجام واکسیناسیون: واکسن‌های مورد نیاز رو می‌زنین.
🔹
دریافت برگ معرفی‌نامه: محل مرکز آموزشی مشخص می‌شود.
🔹
روز اعزام: در تاریخ تعیین‌ شده به مرکز اعلام‌ شده مراجعه می‌‌کنید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/695242" target="_blank">📅 19:36 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695241">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b4c5ac571.mp4?token=ukvVwCsT4OwaPKjGO-jZR3lBeYNC7K7147SI0cRAfRWqK5uUnmxkPeNEnKqg06jXlmAwVDxSI882Twotz4e-RWL3DxJsWap_q19y4gzwNBb20hEe0wEyOzyyYkbop4Zvg2_wwUQ-XBVRAQxnmw3JBCm_0Ey6yj7qohCsyt6s96CPDG3iCPvvGrj9GBq91D06GzPa_LMq3Suzo2c8SWVgpnU4WhZq0PP-I7fajfUMAanjzuLzKN5DJYcjiV9wvVsGuXRnKBeOj8eoIIkGWUE4L67FyyIWmWLdyhZR2Txi1o9IbOLwJP3d6oEEMxK98H_WgQIu994NSzwAvG0l3dL27g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b4c5ac571.mp4?token=ukvVwCsT4OwaPKjGO-jZR3lBeYNC7K7147SI0cRAfRWqK5uUnmxkPeNEnKqg06jXlmAwVDxSI882Twotz4e-RWL3DxJsWap_q19y4gzwNBb20hEe0wEyOzyyYkbop4Zvg2_wwUQ-XBVRAQxnmw3JBCm_0Ey6yj7qohCsyt6s96CPDG3iCPvvGrj9GBq91D06GzPa_LMq3Suzo2c8SWVgpnU4WhZq0PP-I7fajfUMAanjzuLzKN5DJYcjiV9wvVsGuXRnKBeOj8eoIIkGWUE4L67FyyIWmWLdyhZR2Txi1o9IbOLwJP3d6oEEMxK98H_WgQIu994NSzwAvG0l3dL27g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
الهام علی‌اف، رئیس‌جمهور آذربایجان: آمریکا و چین دو ابرقدرت جهان هستند؛ ابرقدرت سومی نیست
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/695241" target="_blank">📅 19:23 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695240">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dd059bda8.mp4?token=gqOp9Kq9Qgh_bPfWpapIS_6f3IiZahmRF-xaLankk6T2QJjmWk_VuuTdSy38ur2TXbPrHsZmfNCX0sCFsSIwju3qwF9pQEPhXrODqJbCK2bB0uPyHFuQTX5jzcc6s9W4X46ySV3iJGHEa3ruVE4wU4CCATqW2CU6nAsjN6VpCiAqaD9gTFCpAqKXcQhhSCRtCQ7RwMM28gOm1fbsKa7KSz2RQir2PAsYhlHt4tksGyGnglCtS1LmoAelzdAXy3PyoDIVkMiQQZ9iPF3bmgzIzcOYiht_UAmtakqTRZH_SpPEZS9WFVaJQ6cShJhV7b3Ps6D04l0C35E8uB91H_MhsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dd059bda8.mp4?token=gqOp9Kq9Qgh_bPfWpapIS_6f3IiZahmRF-xaLankk6T2QJjmWk_VuuTdSy38ur2TXbPrHsZmfNCX0sCFsSIwju3qwF9pQEPhXrODqJbCK2bB0uPyHFuQTX5jzcc6s9W4X46ySV3iJGHEa3ruVE4wU4CCATqW2CU6nAsjN6VpCiAqaD9gTFCpAqKXcQhhSCRtCQ7RwMM28gOm1fbsKa7KSz2RQir2PAsYhlHt4tksGyGnglCtS1LmoAelzdAXy3PyoDIVkMiQQZ9iPF3bmgzIzcOYiht_UAmtakqTRZH_SpPEZS9WFVaJQ6cShJhV7b3Ps6D04l0C35E8uB91H_MhsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیت هگست» وزیر جنگ دولت تروریستی آمریکا مدعی شد: امروز نفت بیشتری از تنگه هرمز عبور می‌کند زیرا خلبانان شگفت‌انگیزی بر حریم هوایی کنترل دارند
🔹
این در حالی است که هر روز چند نفتکش در تنگه هرمز هدف تیر غیب قرار می‌گیرند وآسیب می‌بینند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/695240" target="_blank">📅 19:15 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695239">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hif6KRxOFMCb31odca_ziE8_v-_HnA3mFK991-2G73FuKYG1XmtPFJ3GoXOP9YooqF2OwILuoyBdrbZLg_Dz8p4xDKYu4KGs1k-WlNJ6pM072k3ooGrBdqDul_dzIdv_h4cXfdnj1oDyQzagFLN_GBhozxy2B7g8RN5cgZ4f_VeqQAm-Cpte7lXcVvnn4nOx-hpJCHOIg44O46qwZ7f13wYpA7WGmjZFs2wkT31bsis9M-HI4633jHDdJLQUxU8Drcwm7pTgnwMqmL-_tTA9bfPp-G9Nl7dJgWGSQbwhSAxhIk0Ug7qI6nAhBZW4Z_h3l7LrRDtnsmsN1w9I74cOWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چیزهایی که ایرانی‌ها خیلی قبل‌تر از تصور ما ساختند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/695239" target="_blank">📅 19:03 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695238">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/444bcd3338.mp4?token=s64hZDapL0HHP8doRXEpEaJzPW5kl6QeVp1sICOCEvbp_C17Gy9aNTF7TEsAfyzUchYoQAxbOsyp6TQsylU1-FOrSYy0LlowvPdzGGCFGD2PR1nVdYI7SyM9DRillL_F_nrXMAPq031eo5TVr-m2ywwwsUhFopqkpaeeMccfv7Wc9OtEBk-txLLXsb12aiLLTGyFmzaUowOWzjSauu32zIEHf5yS9W0ect7GziE15MLz5BooTWdn9TQCZsfIoClXndzndQdaZKZvL3COeLpcy5GLQnMqpsSe7h5U6azQhOG80pTGILVCnyCxUCOvWI6_jFpPkeGV5a-KdFthnVe4GXEwTd_yx4sT1uAwNX0lWhJeZRnNBG2uR_5xUS28HmRaM0SzA35_GyqRJD6CcmEg6kQWghdvVa5K_lFuW0A5NeAzSvtLSn6Og1ZJWmQIgdP8_G9UrrlQfT-LAFv4EGXYxZ_sZVge1P-PRr2CigRjRQai8cNIbjLgD4nHDm5y1DqyaPobeDGBarY-TXefYSHzlWzvmRXFoIjVao1JKFuzWNajy3-HMELm_JqmcTl2bWkyrDShIoGW5578_9ok0oLXV6k0mTIh10LFabbjYjl2ZYM9guqMsy0NdQkVFAEl0U9Zd6p6KBHLXsoJnYnstIJVaYKgMhbM93_GoF44hRyeWks" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/444bcd3338.mp4?token=s64hZDapL0HHP8doRXEpEaJzPW5kl6QeVp1sICOCEvbp_C17Gy9aNTF7TEsAfyzUchYoQAxbOsyp6TQsylU1-FOrSYy0LlowvPdzGGCFGD2PR1nVdYI7SyM9DRillL_F_nrXMAPq031eo5TVr-m2ywwwsUhFopqkpaeeMccfv7Wc9OtEBk-txLLXsb12aiLLTGyFmzaUowOWzjSauu32zIEHf5yS9W0ect7GziE15MLz5BooTWdn9TQCZsfIoClXndzndQdaZKZvL3COeLpcy5GLQnMqpsSe7h5U6azQhOG80pTGILVCnyCxUCOvWI6_jFpPkeGV5a-KdFthnVe4GXEwTd_yx4sT1uAwNX0lWhJeZRnNBG2uR_5xUS28HmRaM0SzA35_GyqRJD6CcmEg6kQWghdvVa5K_lFuW0A5NeAzSvtLSn6Og1ZJWmQIgdP8_G9UrrlQfT-LAFv4EGXYxZ_sZVge1P-PRr2CigRjRQai8cNIbjLgD4nHDm5y1DqyaPobeDGBarY-TXefYSHzlWzvmRXFoIjVao1JKFuzWNajy3-HMELm_JqmcTl2bWkyrDShIoGW5578_9ok0oLXV6k0mTIh10LFabbjYjl2ZYM9guqMsy0NdQkVFAEl0U9Zd6p6KBHLXsoJnYnstIJVaYKgMhbM93_GoF44hRyeWks" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
درخواست مردم دیگر کشورها برای پیوستن به جانفدا در جنگ با آمریکا و رژیم صهیونیستی به روایت سخنگوی ستاد مردمی جانفدا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/695238" target="_blank">📅 19:02 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695237">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/162a2a67d5.mp4?token=Wq-awkcF8g3XNs6Ecp2r0kEVDLVR5pBhVv2L-3XJHTOhtsMpWj0v9l4ylglp0YBdCtDNsmFuLikxqFXAtZNpj4diQShIg5wmmuNyIlllhjemcha6KthEvehAWAVJ86IW6sfAXXWRD8w6f7gbU99mxBExQTBJ_FGF14XwDouBiXQuVhk1h2mB6nd1Y48qppGAbJMacDnD0qY_86uiEvc88Al_du2MhZt4sBCEel5cQmO8srRYVDQWrZ81dSJyN2Jh4Jq8UxMCeTuX-kMQU_pc3rFsc3u9HcpsPhl9rvDt6wypkgUWS26Hqd1ILa20sGy3OZfkSbNlDIvtwpwo8__mJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/162a2a67d5.mp4?token=Wq-awkcF8g3XNs6Ecp2r0kEVDLVR5pBhVv2L-3XJHTOhtsMpWj0v9l4ylglp0YBdCtDNsmFuLikxqFXAtZNpj4diQShIg5wmmuNyIlllhjemcha6KthEvehAWAVJ86IW6sfAXXWRD8w6f7gbU99mxBExQTBJ_FGF14XwDouBiXQuVhk1h2mB6nd1Y48qppGAbJMacDnD0qY_86uiEvc88Al_du2MhZt4sBCEel5cQmO8srRYVDQWrZ81dSJyN2Jh4Jq8UxMCeTuX-kMQU_pc3rFsc3u9HcpsPhl9rvDt6wypkgUWS26Hqd1ILa20sGy3OZfkSbNlDIvtwpwo8__mJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای حجم آتش‌سوزی‌های رخ داده در پالایشگاه آرامکو در ریاض را نشان می‌دهند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/695237" target="_blank">📅 18:56 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695236">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cee328bd43.mp4?token=NgU9_t07vpjvsUfAe5nLP7TLa6I-bPE-UKdE0KKaTJU1CvL-sToSpg3OauMrrMWH6JBJKvpBC-rTPsF4KA6cw-kjSDvXMhXNzTDr5Kb6p3fFPyq7ezCQtr_s3nNXoh-um47vYf4jo5uzm49u_K7JPfHfH1BKwBFs0MyztV3dcLXQ7AwFXaC4vBHgq8-hHEWp0f--kjjGYgwr-h_YS_M7Uu8jJzdg-O-8uwlcfb2i5r4s8bZwJYK-Oxsxf3u0DqKB5hQ04ncEXqisoeUJhQCk1aMT6SnfoKQQpH8vPyq1zPA1vzinmv6aZU_ReA176zpKw2u60YJC4gaHLyycl3Xyxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cee328bd43.mp4?token=NgU9_t07vpjvsUfAe5nLP7TLa6I-bPE-UKdE0KKaTJU1CvL-sToSpg3OauMrrMWH6JBJKvpBC-rTPsF4KA6cw-kjSDvXMhXNzTDr5Kb6p3fFPyq7ezCQtr_s3nNXoh-um47vYf4jo5uzm49u_K7JPfHfH1BKwBFs0MyztV3dcLXQ7AwFXaC4vBHgq8-hHEWp0f--kjjGYgwr-h_YS_M7Uu8jJzdg-O-8uwlcfb2i5r4s8bZwJYK-Oxsxf3u0DqKB5hQ04ncEXqisoeUJhQCk1aMT6SnfoKQQpH8vPyq1zPA1vzinmv6aZU_ReA176zpKw2u60YJC4gaHLyycl3Xyxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمک‌گرفتگی پر و بال، معضلی جدی برای پلیکان‌های سفید دریاچه ارومیه
#اخبار_آذربایجان_غربی
در فضای مجازی
👇
@azarbaijan_gharbi</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/695236" target="_blank">📅 18:56 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695235">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/259f28e509.mp4?token=Evu_CWBzimIP9Lhusc__GXO8pq91hKjMJZ5n02M1-IXronffPMlctEaXC9lAQWxC0wXVRXKe6jhdXm9BrlMhhDhuO7tmbkfZAQBoUqEyNLm7nm1qqUCco1K7bBPp4fAAZBRJGkORA0OvAikk5NcNM1O5QXVRedzgv5iTTGaRBwFXPjeIuLq_cuu8YRhqjCWwQKxtCUwomW7RPGZXWjIgAdZKOCMeKK_lDReMMniQC6w6KaR1hMocZGoXd1PV0C7N9y0BMIDzsVhPiSG8jWUoCx29PqH2T5ktyRBE6_5iiZZY5uFvtROdsrlsB0e-FlfszDJXO-ro3HEs1qUm9wXDCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/259f28e509.mp4?token=Evu_CWBzimIP9Lhusc__GXO8pq91hKjMJZ5n02M1-IXronffPMlctEaXC9lAQWxC0wXVRXKe6jhdXm9BrlMhhDhuO7tmbkfZAQBoUqEyNLm7nm1qqUCco1K7bBPp4fAAZBRJGkORA0OvAikk5NcNM1O5QXVRedzgv5iTTGaRBwFXPjeIuLq_cuu8YRhqjCWwQKxtCUwomW7RPGZXWjIgAdZKOCMeKK_lDReMMniQC6w6KaR1hMocZGoXd1PV0C7N9y0BMIDzsVhPiSG8jWUoCx29PqH2T5ktyRBE6_5iiZZY5uFvtROdsrlsB0e-FlfszDJXO-ro3HEs1qUm9wXDCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طوفان و گرد و خاک شدید قم را فرا گرفت  #اخبار_قم در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/695235" target="_blank">📅 18:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695234">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d3228e40c.mp4?token=HHAozP6yf46yqZLvEUx7BMXmTBO-K0eYE_txs84DLVeCg9yBurQRwR08fqJBk4-GdeQep7Msah9dMZvYgvwMXR3H_iLfs5EYjrIhnZft_n4n0xrp27Cp_dfLxnxtGtbkckQHw2v6eFd_dftW8wYUAv986GuVZepdrHi4Ddxpuwtrx4d8RgOLdBZiTL8S47W3-K37bqFbWaGzte3vW_-Bgyn7QBST6N-Zby8azuQol_dK4fU7qd2pVJqkbKJV6VXQLqolY2xH6cfALTouPCB46ijSlFLD8GS5RowSYI_cx5n_zvmxgwqHppO-Oy8sjBvUMnbgZUm4wl0xVfpymRp_Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d3228e40c.mp4?token=HHAozP6yf46yqZLvEUx7BMXmTBO-K0eYE_txs84DLVeCg9yBurQRwR08fqJBk4-GdeQep7Msah9dMZvYgvwMXR3H_iLfs5EYjrIhnZft_n4n0xrp27Cp_dfLxnxtGtbkckQHw2v6eFd_dftW8wYUAv986GuVZepdrHi4Ddxpuwtrx4d8RgOLdBZiTL8S47W3-K37bqFbWaGzte3vW_-Bgyn7QBST6N-Zby8azuQol_dK4fU7qd2pVJqkbKJV6VXQLqolY2xH6cfALTouPCB46ijSlFLD8GS5RowSYI_cx5n_zvmxgwqHppO-Oy8sjBvUMnbgZUm4wl0xVfpymRp_Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مدل جدید Fable 5.5 در ۱۵ ثانیه آثار هنری ۴۰ هزار سال تاریخ را ساخت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/695234" target="_blank">📅 18:45 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695233">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7e6a788a7.mp4?token=cXhbRIeyUZOqhi-hHXDchFBoKfSV2ZvYObUzZvzlp6MkSqqf7gP8jk-4qhGzXL0uGaiV7kRxCeumegOOlVxSYaYtOG3DudGoELB3Oz5PnghMdnyhrRcQwZMV7zcduIM1rAH083DKQMPRfGZ4gL9-4njEZeNvLouQ8LBAGn4NbjfKA_lrWfEbpCiDC09hcfd6M2xHVfdAzVxLijPBFKbBy_vtZmfwpezIAGBUmtY1aDmiVjqtIND17ncxN18ktMXyAJndPfUDN4Nj-J7V-EUBQmlEoG8cP0GjSWwMljR7nb1q8EmpCxkrgNQRCPhUmiGEzIhxTH5nA4yVwG4izeh-LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7e6a788a7.mp4?token=cXhbRIeyUZOqhi-hHXDchFBoKfSV2ZvYObUzZvzlp6MkSqqf7gP8jk-4qhGzXL0uGaiV7kRxCeumegOOlVxSYaYtOG3DudGoELB3Oz5PnghMdnyhrRcQwZMV7zcduIM1rAH083DKQMPRfGZ4gL9-4njEZeNvLouQ8LBAGn4NbjfKA_lrWfEbpCiDC09hcfd6M2xHVfdAzVxLijPBFKbBy_vtZmfwpezIAGBUmtY1aDmiVjqtIND17ncxN18ktMXyAJndPfUDN4Nj-J7V-EUBQmlEoG8cP0GjSWwMljR7nb1q8EmpCxkrgNQRCPhUmiGEzIhxTH5nA4yVwG4izeh-LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ارتش، پای کار جانفدا
🔹
دومین پایگاه آموزش نظامی و امدادی جانفدا با همکاری و محوریت ارتش جمهوری اسلامی ایران افتتاح‌ شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/695233" target="_blank">📅 18:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695232">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
دومین نفتکش امروز در تنگه هرمز منفجر شد؛ در ۵ روز گذشته ۸ نفتکش در مسیر جنوبی تنگه هدف گرفته شده‌اند/ فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/695232" target="_blank">📅 18:41 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695231">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
کانال ۱۲ اسرائیل: آمریکا در حال تقویت گسترده نیروهای خود در خاورمیانه و ارسال سامانه‌های پدافندی به کشورهای عربی برای احتمال ازسرگیری جنگ ایران است
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/695231" target="_blank">📅 18:39 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695230">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d50c947ff.mp4?token=tBGsA9XDH5HX8fh-dbZn1AfO2UxcxX_sbDOucYjPtqbQLcOyPi9qnrBfEUEWtMEnv7qrRRMCO7MfpwtwlcMluKc9A0v3Ex_cxacU5Z5ZxVnNevdbsPuz1mIGTDwlDqY5hifRDcOBrcqTaTqdbn87m4R18NukjUEaBx2upC6pIJVElVc0w2_qny6vGYp5lHMQEcRKwU-oc7dRx6YKE8CIsGzK5rKmFNWAEqeQ8giMJ6KhvF-H0nC27-V-clO6YaaOLmqq5q655qEb_eMkykTgautAzWASm3wTyo3mlnVnkFcLbuMqirTY8GvVQ8WTgynkO_EJOatNCI9VUUzhFIxzXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d50c947ff.mp4?token=tBGsA9XDH5HX8fh-dbZn1AfO2UxcxX_sbDOucYjPtqbQLcOyPi9qnrBfEUEWtMEnv7qrRRMCO7MfpwtwlcMluKc9A0v3Ex_cxacU5Z5ZxVnNevdbsPuz1mIGTDwlDqY5hifRDcOBrcqTaTqdbn87m4R18NukjUEaBx2upC6pIJVElVc0w2_qny6vGYp5lHMQEcRKwU-oc7dRx6YKE8CIsGzK5rKmFNWAEqeQ8giMJ6KhvF-H0nC27-V-clO6YaaOLmqq5q655qEb_eMkykTgautAzWASm3wTyo3mlnVnkFcLbuMqirTY8GvVQ8WTgynkO_EJOatNCI9VUUzhFIxzXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آموزش ساده کشش زمانی نت‌ها؛ از چنگ تا سه‌لاچنگ
🎶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/695230" target="_blank">📅 18:36 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695221">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sn-Zbi-vsAVMh5xO9DWkDhrYA7cVNYzPttARXQn9VMtmw68FHbaEmgkHw_SAP-1P1rAj8k8Xt-zjKp0pivBbzqu2QcKeGy-ZEtmRCmkdeq44MIzAxZ2cPx_8he5BaqsE_8lvG4rVEuOV5MMXSrTf9nAXUubm3Lo1Wp9bf9Y71QujK9Z4KlSRo3jV1aM6PTcw9FljIrRmS2W3t_VoBl-ox9vl68eid8v0hFBqTnqKaleAZ05_lSq3mqdhLqIGb_NhQGjI4-bVzHR-FwlpXMn2zetYZMuQLVGDotTm2aosK_TE6vVP6TT8omJbQOS-LVPfcCJJ5i3hPEHpHKgiayrXlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y_PYwgwcjwxGw2BjBwk65pD2XfguxeO6V7f1rP3lCsaTPCv0fTXHi5qpVv6fNZ1Z3A0N4qUk5VlrJxu4U79va1AzJX_fPNVFEgSRMzBHq3QNRVMUjZHioRaX6cET4M-hff9zryvon1Y40jokJgSAaDGf_lNhQXuI4B06VXxvkPCRgXgmsXTm3FC0SdJup6HRd5z3R6rQAgoc7cbRPhacM9IOHSKIpRYRCzrXrpnRyTBTx5wF2o9zXmXUEfocgKiO8X4nIuhowgVrRPBDazkrI4nYWonCQ5ORCeIwBpyH_rqxQpTrsp-gclaMB4hU4SAxEXMLmaMyrU_vlmA6UYwhpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KitQw4UsKtc-8jlVgmw-HtN_fpVWBGTGVAf38NDnhD4p5rtGZrIGQEt9H7MVjn2s1IHSGXwdVxRfFm4CY3hN5S-BNFG60r5J981vjKlpXIKIthjXsmgJ_cBPS-paekRqXlzBTJsj4N_JZFyjeiIpWCoxba2WnST-gaD9QAeDREOSzt0hH1KPxa_TemBD_-sDWtQoSoBDo2rvQ-88DA3NY-Yl5utLOhqXcBHIo0v0fu8_xH5lzW6YVphUsKCvBU2rTNma0CMWN4PkTzDo4N2hmWfEGGRFQnXZ-bJ-PqIm-lYNBnifeJZ37z5vWb70jh2ZNqXGLECeEPMiHjA-9lGKBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F4aFOb2aHqSmZ2amtSVu4522-tIvRdPMCPfC-uf8osLQEwHo5lrqeGiHGLBCqjvVTckm9adm9nVIc7NwB3E5E3XNlZ6bQ4Rq2EtPP7ThfBcD58PXc-fI6fCN0WSVZ5qoPwqs90l2xHlhIzlpHIt9Z7gFPKTbjtVNpoWiVh08UeGi2N8Hbixzb_ZFlWD7r5vnPFzdE0oh72Uhwbwr_KUDZaiYk9bypRODkYXlKQk0neLLXVAV3kud9k8BriCpD3QHnyClfWeQ110YddZt9ann2rWPiJwnkVafcGoMorCefUcDRaqs66qXQgf81da6Dr__y3ezXWDXRVzc5xodN2EU7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BXV0s1TkhXJMKnszqRkFx7ubBLhtCVrHd2PzDdQfMBqSkuXRoYWhHsPRDZEzXm6UaOKBun91wojl5VmtkmDXRqjK7OxPIWXANupW-Rj66jBwddFOPYq8gmjXwLLRwQiUeEAQPVaVwZkvZakPm1yvUwRuphPJQOKucwWXSkg4GT79EXKbCvqVZE-kQu2T_Mu4is5XqwBZkHnPbNsZyKWUY8Pk84nEnIOuZQ1DTaRYf6xLO3ABplbZf3-zewkvqzrCdgDWRR-cv2Z2Rzf0Sg7Jg38tY0YQrpXaC3z5Nb9V0wRqsDM_SoWiC-PdS0dRmNk1EKFIXTQH04bxME1EOelVow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mqJJuE5mH7srfvvDjz5tOZV3YN89DT7GlsyQjTt11_lv4SUdhqZ4oj2GPPSr2STn6X8YMhNuVQIPhoBbg9D8-hBlcRxsp9po-UVJgCWzOZfKQm_P0EVN-rNQ3FvwsNQxN3Vu8b62MLthWJtXGLuR7zYiXIFbKlSVDoneg950KslUo6DX2trZARsdZYNsQzFP1sZ09zG6zQNwmtYtPpM_33nWLbe1JQBiCstRdZQMEu2F6ZGt5GD138kMwaYIeoqd4OGfpt6PjBs49aRCCRlDHW4coIPp5QONO8yuKNk0YHxBbN_DOWChjpkfRZkyb7AuEJMCYDuVgTXntG-szQJIiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BtrBsVBVVnf-lLcEn_jkn3kcxipea2U3YBB4wcxNaMrvku74Skoawhe3WJpFREDAgWYmeYqbF6e5Jm_915VNuo1EeLdOPX5-wmpToXfJaCMP_Bo5V80OMhuyTGx-TREZYvLshOG-LYFxepCBSQWeAC-aJFBqHNxpmHiz2h9b-3MV7tMTY2PrQqSMAY0zHJtWapKj26emUixnmYarqYDL_yiYELeNpgCmC6dIhCgW2HqNKxpg2IVA7_CiwsUX6cSZzEJN0URBrlGzxMAtmc7-F-eDtUdVs1CRwsVe_fzUoRbOPYpgk8IpufvGLoJb7UKneny4QiLVThrLrBGOeBzt_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qk8RvaRUgC9FauN0jimr5Zms4op3pL1ko5QejUvSdDbz4OBi-3ygf2OWA1V057ZVBEEMZomT3tPJQwzEA2CbmnOYeCpcd2tk_lRei5faUvDa7s0S-1pnus3aWKDMt_4xdBet9eChu0WpOUmj4h47qliTLu9732Vb629vbmyAeRS4eQQr3zdbFC6A9v3Snb15zR5OF8XF5rt7VUDvCzqPyK6oAqKCrZJWRGoctmayCndAjQBC_-TwqZR8FgTwvx6C0EwFk-60qnEDxo-W285zZ8EQFR8bXKHFWmQNa99HPFBtJORAh2MeAsPxaDkqIKQVuTnH3oTVGbUiQuy0PfLirA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ooJbwT06j0-XeZVAySQPpmbSE9vZgU3Ywmaoo-yfd_nlbeR8lwd0YrQWgKeLcpNGvLKKSklWERGMrU0se2NKGMzjSGg7nJwhmy5eUauv9ZycLdeWeq_ub6LWr0tXvhd0p0H0cJLUpvxAuEaq-KfNwTczZ9qPznlU1J5E2X2FcVvFI0abHKAbWRzd-aZvgnKAxcs06_OevnVWth5UXEO9BtgkbXUvTV1KFleSuQqEtCEBQB5ujoOYnkjLyEPYrQCy0k2j6upm6RjtVfRkoHeaFF-5gUjhamCGaTcnz9M-Tvx0qRdTIcKY2Q5FzEuIK4O2xsoZj_Ja8kKvOqSNddkWjQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
در ظاهر خیابان به ما محتاج است در باطن ما به خیابان
مجموعه تولیدات گرافیکی
#پای_ایران_ایستاده‌ایم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/695221" target="_blank">📅 18:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695220">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0faf61c2cf.mp4?token=K-TyvcuEPlf1XPoyZVBepoBLCu9-6hKfOgHjVfRXa5fNBeE9ORFTsWpIP1XzPYD18RcN0a1_cSGF2FLg8wfJXCDt_aCyQV7c7_gPDYVFIFpuS7RJs8W2CAlRcC36tCRvnVII7BEgIFRG_OyDCKzdwB0D20b86tC-iIAwOtfoFglAX0sLX40NMBvf0P8qo-avg0-iFbwh6ZEWrg2hr2ptGXDHFSJ0h8sgIOApHqjaIyUqzOW7RKi2A8Bdd5elZvc-r25lE0nTpoC58WwgD6htK2P-7CLkubsQD-TEtUYmxCiUQBvwaayOm6i1KFTyWex2IOTBQ2dd9rOjBW8ShJO19A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0faf61c2cf.mp4?token=K-TyvcuEPlf1XPoyZVBepoBLCu9-6hKfOgHjVfRXa5fNBeE9ORFTsWpIP1XzPYD18RcN0a1_cSGF2FLg8wfJXCDt_aCyQV7c7_gPDYVFIFpuS7RJs8W2CAlRcC36tCRvnVII7BEgIFRG_OyDCKzdwB0D20b86tC-iIAwOtfoFglAX0sLX40NMBvf0P8qo-avg0-iFbwh6ZEWrg2hr2ptGXDHFSJ0h8sgIOApHqjaIyUqzOW7RKi2A8Bdd5elZvc-r25lE0nTpoC58WwgD6htK2P-7CLkubsQD-TEtUYmxCiUQBvwaayOm6i1KFTyWex2IOTBQ2dd9rOjBW8ShJO19A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ جنایتکار: اگر در انتخابات پیروز شویم به همه مردم ۵۰۰۰ دلار میدهیم ، نه فقط بزرگسالان/ ایران هم مثل ونزوئلا سقوط خواهد کرد #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/695220" target="_blank">📅 18:28 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695218">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0231847ac4.mp4?token=a1oge-99Otfy125lzlHtxafOnBcamd3UHc92Jmz3n1Dtb76-FBjbvNIdUWzbXjKgQO8zKFNvWaj3FephRq1vFy3CkH34xBFEVF9t84LEbPQPZhb06zC2FDIh-OMTsc8oPYekBcspEUKUQKe4-spXShMfogw0TmlvCimCRfAsWvgdGZh6M_Zghj9svie05lUIaxgImZD0qXun5Iid0sO2YzS6Q-jinp8QuJqWslq_XYe72X9G4rbThEk4qjQ2R0MeTuiKfWPkUOb_18OZLo-4EUdVItRdA8RsVdAQSj6TV5pN6-XQP8sGmsP_60hGI0JKZynxjFaLvMoMAuC7V-P33A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0231847ac4.mp4?token=a1oge-99Otfy125lzlHtxafOnBcamd3UHc92Jmz3n1Dtb76-FBjbvNIdUWzbXjKgQO8zKFNvWaj3FephRq1vFy3CkH34xBFEVF9t84LEbPQPZhb06zC2FDIh-OMTsc8oPYekBcspEUKUQKe4-spXShMfogw0TmlvCimCRfAsWvgdGZh6M_Zghj9svie05lUIaxgImZD0qXun5Iid0sO2YzS6Q-jinp8QuJqWslq_XYe72X9G4rbThEk4qjQ2R0MeTuiKfWPkUOb_18OZLo-4EUdVItRdA8RsVdAQSj6TV5pN6-XQP8sGmsP_60hGI0JKZynxjFaLvMoMAuC7V-P33A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پهپاد روسیه به پل مسکوفسکی، از پل‌های اصلی کی‌یف، اصابت کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/695218" target="_blank">📅 18:23 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695217">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84fa4af9be.mp4?token=o5lUtE7nSXLopoS2eLltFn0ZDJ2TiXKvgcd-3eMsMJmZXnAEUwrH7eJrM8ftm_gcqGjzUrQjt85CprYH0oXuq5yneD461sShM-U0yUDxjTOkUacvfnp80DLgeQngNoj2lmm_J347vDdbYVlHeQ4tfTdiv0hrAZ7f5u8OuM6_H38WR8ZzSCZkwYnqX_UuNt9bTZO0x3ookGQoI68APxeQnGJR08HDjvcqA5ZRjfP1S5xemR_QBmGB_llc0Gt8gobs2pt8VFB3Owfu26sH2eSLlOFGq8YpeW9_jj1SsvNKkcBWYdhU-dKCi94mBHF27kXUjWWGv5Ikml4m5l-6PNT9eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84fa4af9be.mp4?token=o5lUtE7nSXLopoS2eLltFn0ZDJ2TiXKvgcd-3eMsMJmZXnAEUwrH7eJrM8ftm_gcqGjzUrQjt85CprYH0oXuq5yneD461sShM-U0yUDxjTOkUacvfnp80DLgeQngNoj2lmm_J347vDdbYVlHeQ4tfTdiv0hrAZ7f5u8OuM6_H38WR8ZzSCZkwYnqX_UuNt9bTZO0x3ookGQoI68APxeQnGJR08HDjvcqA5ZRjfP1S5xemR_QBmGB_llc0Gt8gobs2pt8VFB3Owfu26sH2eSLlOFGq8YpeW9_jj1SsvNKkcBWYdhU-dKCi94mBHF27kXUjWWGv5Ikml4m5l-6PNT9eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بارش شدید تگرگ در دزفول خوزستان
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/695217" target="_blank">📅 18:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695216">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96de173dbc.mp4?token=scl_jPrwa9nh7ceREEkjnZI-eXMsIa54mxghM7jnwpjCcCAFVIsqTva4pApg42HxdW7kiO-IFLg4Pun1NPHaHtSQWwCGTUkDM9fPHV5n1XluvQztEUdE3PFZ4YE0kfy_GUKRdxq6vZ44AVpKUh6VP4GocqUmlVF0VE6ZjeLcZkeIkBztI8rxIlcuZzg7H5INjlyd65SiryPwVIthI_Re_tNkC2bIL1vlLFHxt2AJUgtOelosymOf1a2bHiJcij7rfGxjU2Q2IbMRYRQGA_rgUszbRlkOButgdXcxNggBWJqjCZTAGbs32kySxB1toGoarq2Jfw6Eqs9f2GlW-kuIFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96de173dbc.mp4?token=scl_jPrwa9nh7ceREEkjnZI-eXMsIa54mxghM7jnwpjCcCAFVIsqTva4pApg42HxdW7kiO-IFLg4Pun1NPHaHtSQWwCGTUkDM9fPHV5n1XluvQztEUdE3PFZ4YE0kfy_GUKRdxq6vZ44AVpKUh6VP4GocqUmlVF0VE6ZjeLcZkeIkBztI8rxIlcuZzg7H5INjlyd65SiryPwVIthI_Re_tNkC2bIL1vlLFHxt2AJUgtOelosymOf1a2bHiJcij7rfGxjU2Q2IbMRYRQGA_rgUszbRlkOButgdXcxNggBWJqjCZTAGbs32kySxB1toGoarq2Jfw6Eqs9f2GlW-kuIFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئویی از ترکیدن لاستیک تسلا با سرعت ۲۸۸ کیلومتر!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/695216" target="_blank">📅 18:14 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695215">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
وزیر خزانه‌داری آمریکا: گاهی فکر میکنم مردم امریکا در زیر کامیون تورم له شده اند و من مثل اتش نشان هستم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/695215" target="_blank">📅 18:12 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695214">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc139729d.mp4?token=awbxMnMyHWRuTOu4UVonHMF0DdnW0uNoWp59K2Zp0ackanrL_6u7Q_fJ3LAzHm035bvCrSEFCc7IJ841WJfHvPIcaEIPbFzPeap_nonEZouMz4y1ejfvulC4Nyo4OSAPIGdgeLFO0REPMfdV2FyCD1VXCVn5BP4ylbOdnGoAsWitUjNYN2Te1Ipl_ir5J8lSetwgzYfu9B0MEpg63BFFLEw5uC14hkU2MWhHSGzj2_vGEEbib5z5hwntylwdB3vflB3Y4d3PDQ3O4JXeckVMBE74EP0W0GPG2QtL7epK4Y3yFkQXzb88VKsv13KsqCSanZxfHzf2SZhubYHkJtGeTYt_yUhfQRrs78wQJLkei1oU2f7oKL5jCMUgZ8vOWEErWMfNjPL4lkHMUWnXKHpLMAI1XTfnjIcGiHep3pby8op5NK78QmA3HgDhki9gA-bEYwSItPZqe6jn-e3JwGTxZHWGx9knlkNpCgTYtc-unZzj9yO7mm9qOHHOQcMkKMURGoilsNhJ8AoWSH-588O8OCfq6k4QJM0lyTlq_BWAJcH8I5piegvOpSfj9rjbmnY01QtlIkee3vekBzNPwvz1ZbeAQEBJetZ4nkLrn7ZUfNqfI-fpEUMP_n2MBdjjo05OeL71DaMMTDbLAWemAnFXADJiGCS2zsfPY51KB2eIu54" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc139729d.mp4?token=awbxMnMyHWRuTOu4UVonHMF0DdnW0uNoWp59K2Zp0ackanrL_6u7Q_fJ3LAzHm035bvCrSEFCc7IJ841WJfHvPIcaEIPbFzPeap_nonEZouMz4y1ejfvulC4Nyo4OSAPIGdgeLFO0REPMfdV2FyCD1VXCVn5BP4ylbOdnGoAsWitUjNYN2Te1Ipl_ir5J8lSetwgzYfu9B0MEpg63BFFLEw5uC14hkU2MWhHSGzj2_vGEEbib5z5hwntylwdB3vflB3Y4d3PDQ3O4JXeckVMBE74EP0W0GPG2QtL7epK4Y3yFkQXzb88VKsv13KsqCSanZxfHzf2SZhubYHkJtGeTYt_yUhfQRrs78wQJLkei1oU2f7oKL5jCMUgZ8vOWEErWMfNjPL4lkHMUWnXKHpLMAI1XTfnjIcGiHep3pby8op5NK78QmA3HgDhki9gA-bEYwSItPZqe6jn-e3JwGTxZHWGx9knlkNpCgTYtc-unZzj9yO7mm9qOHHOQcMkKMURGoilsNhJ8AoWSH-588O8OCfq6k4QJM0lyTlq_BWAJcH8I5piegvOpSfj9rjbmnY01QtlIkee3vekBzNPwvz1ZbeAQEBJetZ4nkLrn7ZUfNqfI-fpEUMP_n2MBdjjo05OeL71DaMMTDbLAWemAnFXADJiGCS2zsfPY51KB2eIu54" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آخرین وضعیت کاربران میلی از زبان مجری صداوسیما
🔹
المیرا شریفی مقدم مجری صداوسیما: مشکل میلی حل شده و این پلتفرم توانسته به ذخایر طلایش دسترسی پیدا کند. تسویه کاربران از دو روز پیش آغاز شده است.
🔹
ظاهراً آنچه در روزهای اخیر درباره‌ ورشکستگی یا خالی فروشی مطرح شد، با واقعیت ماجرا فاصله داشته؛ حالا هم فرآیند تسویه کاربران در حال انجام است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/695214" target="_blank">📅 18:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695213">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
برگزاری مراسم عقد در کنار پل B1 کرج
#اخبار_البرز
در فضای مجازی
👇
@akhbare_Alborz</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/695213" target="_blank">📅 18:07 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695212">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edd7a942d5.mp4?token=tgzxZf1sT2E6-6uvySBWS_3CH2PMebLHIUZNmPQEmCAXn_e60qwMRKjN1ZclTr5YketofJ7pLbZC4nRrZFyPnjtxORZfFPGKqcam_5VVOavOH-7xW1VGnsdcSkwH7_P-VAYWzFjbhaCgDQVIr_1E7DbOKgSRFGTEvyTJbbakZdSp067KhBAkFeTKhtwryqQWXEai8qpLqTogLlb96g0ap1_XuFOTy3NTUlh3xUYiHHuXRD3KamhqXp8drNqTluMvBB-fBoCcUMxmVOK3i4cjuV0dpvg8yqOeBhW6szuo8bPF-yjagdJWHFg-ROKpECQCqhYumS9WGZejJfa69_HI0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edd7a942d5.mp4?token=tgzxZf1sT2E6-6uvySBWS_3CH2PMebLHIUZNmPQEmCAXn_e60qwMRKjN1ZclTr5YketofJ7pLbZC4nRrZFyPnjtxORZfFPGKqcam_5VVOavOH-7xW1VGnsdcSkwH7_P-VAYWzFjbhaCgDQVIr_1E7DbOKgSRFGTEvyTJbbakZdSp067KhBAkFeTKhtwryqQWXEai8qpLqTogLlb96g0ap1_XuFOTy3NTUlh3xUYiHHuXRD3KamhqXp8drNqTluMvBB-fBoCcUMxmVOK3i4cjuV0dpvg8yqOeBhW6szuo8bPF-yjagdJWHFg-ROKpECQCqhYumS9WGZejJfa69_HI0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی تماشایی از دماوند زیبا
🗻
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/695212" target="_blank">📅 17:52 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695206">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F3Fi8paFAvdsO1-gew5hvu8A1jTAvDWCizcAghAHcAGlSgYsTZEDZK0CcwxH40OA5EwVWapaFNM3iyxvcXVasSfpYGAm3wUiIVMTID4UF-Wyskb4My_VhK9pp1uKlrdGNhwa20qMZ3ieBkwj0EQDgQd6EBJuX5KyCsnD9kHPPLz1657seTjSDCxLMiEckWXeKcRvsey1IaaE1iDsrEXIanBg7W3FlxGTEseJ3zDBNd3VdG7q98S3ZT7kNftjlUfh8pe1WbKtbCMPq69UV0RScPu6-uNSSBmRmDdopqHApbG_jSbOEPCfI7CpTAHEXtIKhsMAIzw508T3o4_d4PolnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bhZcK86UdwijkyYQp1Z_B9DKScTdvycDDbgo53AU0-muS1rTUP4qwa35YvonQachhTLsNYP5x-_zrLkgHFDyITfcBs9gM223q1oqHtyiHY6tO4ByOaWyEE1UBEEQsHRYX72kWMoOs2mVwFj2hubQBw3Hsm1EximupOaXrX9VS_iZdtVzmgJ3anEsM5zRFgFaUrWvgDNnYUxvjgL8BLx26OJs0eSEuabg06Vs1nfh6KiU-2x4FAyxdLDl19lpaypjx1IA2fjJ_viX18KCWaCUDUx3TdAXrB0c1GrwFSY9O6UsMOWR3nIpcXv2pbbimTbsqThX9Hj4SlVeyuWl5D1Inw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z24DcGz6W8D9FiXKQ4sTRNUVNcb1cN5CU5mSic1sKx5ZT3TQKQB4OdBV1rWVqf6yYsVNXLwNLZ1qlDzIyr3pkDc5x_tIBPIWymvqXUF3ef-cKjiz9hkHak0JTuJgWM2Y7EKoh-tk3JKwrzx-AC5pNzHyFjzOOnECoBKBzE5ySEos8Ez_v5w4sFMAD8uVCOHAMsSXLF2H6R3W5cNIFYXXml-6STWpjuM9ca1hv6laXvNHyzc1sSb-B_AZ9HD4E_6tMZB8gi30TL4HaeFUmsLQtiSuqAbdI5dSsKiH47M1noZlSlwpLyRa17yYKNBy7RUlzzkH3Kd7NEnxfnqVlwZS_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LwamAH_XJSDGIJ65OwG_H7SH5IQdYwAjebclcbLmtaNnFEjilB0av1hgejwHm-rhwTCpoXV2yNMJFl7P50cIyIvVb39U9MjUnc8c-vA93u5ABLBmOvCHjbhLxKSzNuXzcX6jErpT9iWWMZIDLADwK20jp5xNaFcsSATWrNgVoGTs804GBt03VwreT1LmBGl8V8ZAhaszWe-OVGuCqgoMaVuDuwSyXvi0vATA6pDQ6EU5SA0HXdv9emO5h6_gCgzH1lK_01l4QIMJUPf8afNXnHMGmnYoWtooEk8lqJpgsvLw8i6c8PXfkafCZfEbyCUPr_Q2N8tkjyt9k4ZNfcqWqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GdnTlN5_blgqNBvJ8GoK-osli190yeXE-xR4z1KLKwBKw2_AxYtsFC8Tdd2Q1KQZYNgyJPWD_bJMA1zVhsi4ZzF7kC4XqiTXW2KmMiEvEdtrKiNwk2wiZQ9Qjj0suKLYtEgKttH1gTwTNiT1vaqrksx8k_aDbwidtMHhmV5S87ksdSAx7gF5DpR0JLrytreGeZA5C373VqvN94ApQxnKIBNf--LBaUUPBemm6xfdi3BcEZY8GD1BigUAo-RutGje1jwx9zo5k4h7N1aFL4jbl24MwyVZbMXTpoBg6z58oIax5PfvtyvjFsWONfUMmBLMieZIyU-n5UGjCINO5B6S9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/paeLZv1_09a_ET7PgXqRP1KgBorqyI_3iHofSkA6oY_DeuFlv3DN3EAdEH8TaIFjDpUbHwjU-qC6c21anrAXg2LUKrhjdKQezDuXICekP0DT5MAEYbwpdKNdGjt0RZc0PYVJgLHe4HpT1vofKMmPM6u2Nv5cxEc958caahvb2ctg6QqRr85GIZ4vhs489a-AyeqAtq7qOAtDZEu8m_eaqRe8gRzHEWdM1dPIc8i7CKyaICiknsDCUWuVu1F4thHrxHHyebfA5VrM-eLo42T1j251flWFw0Q7y6nlIuT0nDhykv158CBYDWGV18fEzBmvhCqF2HfDKQt-CAYbwWtoZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چطور محتوای هوش مصنوعی را کشف کنیم؟
🔹
فکر می‌کنید اگه واترمارک رو حذف کنین، فایل رو فشرده کنید یا متن خروجی هوش‌مصنوعی رو بازنویسی کنید، واقعا می‌‌تونید تمام ردپاهای هوش مصنوعی رو پاک کنید؟
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/695206" target="_blank">📅 17:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695205">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
حساب صرافی‌های رمزارزی در آستانۀ مسدودی
🔹
بانک مرکزی قصد دارد حساب‌ها و درگاه‌های ریالی برخی صرافی‌های رمزارزی را به‌دلیل سفارش‌گذاری‌های مصنوعی در بازار تتر و ایجاد اختلال در قیمت‌گذاری تتر و بازار ارز مسدود کند.
🔹
پیش از این نیز در دی ۱۴۰۳ درگاه‌های ورودی ریالی صرافی‌های رمزارزی مسدود شده بود.
🔹
شدت برخورد این‌بار بیشتر خواهد بود، اما یک طرف حساب صرافی‌ها برای تسویۀ وجوه کاربران باز می‌ماند./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/695205" target="_blank">📅 17:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695204">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
دومین نفتکش امروز در تنگه هرمز منفجر شد؛ در ۵ روز گذشته ۸ نفتکش در مسیر جنوبی تنگه هدف گرفته شده‌اند/ فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/695204" target="_blank">📅 17:43 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695203">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c86f2a125.mp4?token=sJaXn0w_KSXOnhJwXOiYyx7ZWZKuwTT3MVHTQ4_KLWqn_Opj2ll_MnKvkykjn2lYNpTwK44FFUXn-F04DjlGUOEfhg2RjPjveVMV_d_CmsGCT2nZRzjou7sxnlCzmqm8O7mB5D3KAoU9w_aOaEyu8ac2D7RQKZsrslETkYAO583cL1vnt861_W6A-1lL5qAug83_GJrUmsHUegbb1eLW_9s9nrmSbjLPdnL9SPshZoL-HOqHFCpKoR4fzl1UP91Ob_XaUFzvk86QM9Vu6P5QvDik-TNtJOwwhQoF3RJalZ5aWaDz5TVsQ7TKraW7YdkmHCjkdBfnE1p-U0tycoajkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c86f2a125.mp4?token=sJaXn0w_KSXOnhJwXOiYyx7ZWZKuwTT3MVHTQ4_KLWqn_Opj2ll_MnKvkykjn2lYNpTwK44FFUXn-F04DjlGUOEfhg2RjPjveVMV_d_CmsGCT2nZRzjou7sxnlCzmqm8O7mB5D3KAoU9w_aOaEyu8ac2D7RQKZsrslETkYAO583cL1vnt861_W6A-1lL5qAug83_GJrUmsHUegbb1eLW_9s9nrmSbjLPdnL9SPshZoL-HOqHFCpKoR4fzl1UP91Ob_XaUFzvk86QM9Vu6P5QvDik-TNtJOwwhQoF3RJalZ5aWaDz5TVsQ7TKraW7YdkmHCjkdBfnE1p-U0tycoajkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طوفان و گرد و خاک شدید قم را فرا گرفت
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/695203" target="_blank">📅 17:41 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695202">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33998a3453.mp4?token=JKoA5S28q4fZK5PhA-3kinSu7GgHXWER4xTAwlMkbAOoGBRt_rwHhsOMltGOwVoM5gvXw0LXn78a1PMaz9c1UvTKRBQNqhCYsbHliv9lDE3J54L3OC78byeHN1J3mT8gUz23qJmI-CesNebNq7OsVo5L-IjY2anW_SGVNYUSE3bJkv9MyXfGTTLxPGmD7Nhrv9C7rQFvHY_Ae6GhjPt_Eg0N8FyurbvvmHhqcfxzx_ymuPd0awwCAMeOTdCMouwqlYeLheZDkWtClbgwrLPhS0ycUdbM82YLNf2QqPUmBsgUxmpFKuRchOiNgXkufeNoZKery-V_xJI1-poBCiDOlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33998a3453.mp4?token=JKoA5S28q4fZK5PhA-3kinSu7GgHXWER4xTAwlMkbAOoGBRt_rwHhsOMltGOwVoM5gvXw0LXn78a1PMaz9c1UvTKRBQNqhCYsbHliv9lDE3J54L3OC78byeHN1J3mT8gUz23qJmI-CesNebNq7OsVo5L-IjY2anW_SGVNYUSE3bJkv9MyXfGTTLxPGmD7Nhrv9C7rQFvHY_Ae6GhjPt_Eg0N8FyurbvvmHhqcfxzx_ymuPd0awwCAMeOTdCMouwqlYeLheZDkWtClbgwrLPhS0ycUdbM82YLNf2QqPUmBsgUxmpFKuRchOiNgXkufeNoZKery-V_xJI1-poBCiDOlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
داستان خرگوش و لاک‌پشت در دنیای واقعی هم ثابت شد
🐢
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/695202" target="_blank">📅 17:36 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695201">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
شهرداران کلان‌شهرها از پزشکیان چه خواستند؟
🔹
مومنی وزیر کشور خطاب به رییس جمهور: مولد سازی را به شهرداران بسپارید نتیجه اش بهتر از الان است
🔹
نصرتی معاون عمران وزیر و رییس سازمان شهرداری ها و دهیاری ها: شهرداری ها برنامه عرضه مایحتاج مردم تا ۳۰ درصد پایین تر از بازار را  دارند.
🔹
درخواست صریح یک آتش‌نشان از رییس‌جمهور
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/695201" target="_blank">📅 17:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695200">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WebNIOd3ScNz-OwpUhQsmKnBSvRXkTIoO1hniP9RUdJtHQBfcJkvhkSlC-sB2b3bi5PdVdzu1hguiLqgkZyvxoz29WyvF6m5WifPMYxBGK6oMpE_0-MwbJ4pd-VDdB9UHBuFi_0eI6yhPQB_kBwfA0jWAIoyYIN90LTRo8OADJ9vYpH5SMbzspR7rVZ06lBWD9-Vh57Vac_8PgUouui2icLQHCs1muDR-bqH6X9YFu4pgGBTmxlM2K9woyE8T3b2M1Bfazpxpaxl_-kQvPgV8rzUo_iJly91Jmvp2wBMGqdNU4xoXL7-6E9KHSnWMhtP8_SB9moCfIv4yZx6AhT10g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پست امروز گلشیفته فراهانی در اینستاگرام: سال‌ها پیش تهران
🔹
این پست گمانه‌زنی‌ها در مورد احتمال بازگشت گلشیفته فراهانی به ایران را افزایش داده. پیش از این خبرگزاری تابناک از احتمال سفر فراهانی به ایران خبر داده بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/695200" target="_blank">📅 17:31 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695199">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4d34c7efd.mp4?token=MdDjZHoipvQONmwuXMbBaJmiO21Ty2O6brOCE03GRbbjVjYHkHTl5QAPSJzwW7tPR8Rinz1YCdaFAQ8pgwrkcLplU9DdxArsSnQp1-Zm6b43AFOd977nB_NqqRvyTjuNI5yIg6WsUU3ztKgB7qt57JbF6qGcdfjViqJg1XGOKOCHO623A5NIW0VPT49qY4vrtbooO7JVfbyRHh5kRdFY1d9Gcr7gEHngh9i7Au3WWwG4goIB779bjuG7VRGBa-rRg15BPI_Py7KVJGCbnUYOEy6kGuHN_VxWuILz-PUDqFvo43-JVNgavxGqMiAhnz_UIrOIU6CVlfvVEg48oFfGWIB3PmWMVWYxdXwGrJ1AZJb_gRPAVdn4bRQqScU9Itt1H5MpAyslCoXBp413sp4rt90ZfIt7BfAOwI61lCKBsH61xhs6Uq__ILGAp06dZfVL4is9Ttfb8d6H237jPsYtDOei1_JcKyJcOHY7SbO8cAqxCeaKDOomv16jBkmd8dqFV73Q_0Nhl6reO0BTVMRnTm2H_dONraXaodqvuZT69a18wUGnJLrCjSMWeeU_PvvBV-RwIeJn6VdtQvoQGKsXejKS2xOWzWWam1wVCHwZ0JXOdQh4Yj7kCCcfWB-DXI1pMlBiyAupqFm4WFPA6Ghmtb5Pi-DE3vthZ-LUE99CWNk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4d34c7efd.mp4?token=MdDjZHoipvQONmwuXMbBaJmiO21Ty2O6brOCE03GRbbjVjYHkHTl5QAPSJzwW7tPR8Rinz1YCdaFAQ8pgwrkcLplU9DdxArsSnQp1-Zm6b43AFOd977nB_NqqRvyTjuNI5yIg6WsUU3ztKgB7qt57JbF6qGcdfjViqJg1XGOKOCHO623A5NIW0VPT49qY4vrtbooO7JVfbyRHh5kRdFY1d9Gcr7gEHngh9i7Au3WWwG4goIB779bjuG7VRGBa-rRg15BPI_Py7KVJGCbnUYOEy6kGuHN_VxWuILz-PUDqFvo43-JVNgavxGqMiAhnz_UIrOIU6CVlfvVEg48oFfGWIB3PmWMVWYxdXwGrJ1AZJb_gRPAVdn4bRQqScU9Itt1H5MpAyslCoXBp413sp4rt90ZfIt7BfAOwI61lCKBsH61xhs6Uq__ILGAp06dZfVL4is9Ttfb8d6H237jPsYtDOei1_JcKyJcOHY7SbO8cAqxCeaKDOomv16jBkmd8dqFV73Q_0Nhl6reO0BTVMRnTm2H_dONraXaodqvuZT69a18wUGnJLrCjSMWeeU_PvvBV-RwIeJn6VdtQvoQGKsXejKS2xOWzWWam1wVCHwZ0JXOdQh4Yj7kCCcfWB-DXI1pMlBiyAupqFm4WFPA6Ghmtb5Pi-DE3vthZ-LUE99CWNk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم‌اکنون؛ بارش شدید باران در برخی مناطق تهران
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/695199" target="_blank">📅 17:25 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695198">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f4lq2mx_yU4ydw07Eyqt_NC7mr2T_sToaSedOm4TuyruqBk_-Fk9jJ2NnU7gUSVPVeIJuJJ7y0V6jOrz7NUFmsDQEmku2NELZUBQgBOZvgX9zIgxrSBN8oviqGDasVdvxlzKlHEbp_FQ-VNvQfDtTtODt4AtgugXj4WGqcHlvuTbXH-RJ_CCIsihwUHF1Gk2m82ZEW65I8E2Jck8pywfrPU1frbzW55JzgPoKdNtnbsWsYt-bGwqtkAASscD4AizJsOEDyVx_p1492kGb8ifL6Bt4W4xQxCE4mTIiXyhUdBM6tx8nVNVZaRNCVeg-Qwz56an9yVYPC67bwwN3-rVqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
المیادین: ارتش یمن کنترل رشته‌کوه راهبردی راسن در استان تعز را به دست گرفت
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/695198" target="_blank">📅 17:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695197">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g7WZ45rrHA1RARDXWx2y0_sxWh9uNFsXwY646viLpT_wmQvIOI5TzNMOyE6-h2Hc_gXFDCjr5GPi7AvEY2ayJo4BWyEYKmS3dHvAiD-Sek4S1Ll8hgw3dw51mFdK4ZfpKJP_-Ui0T2x62BfrOk4bQE6vnFS_-7pb2r-V9J64GKWCxsxft-7rWYK9d-DV3ulLw_u8AjaOsEFMZPk6K5t0embGGpet6LjWGm49eIvKyMd0n-5ZUyaK_21CshFC7ca5TytAs9llqPsmhEZYq0IM8EnW8dVpwNlAgOvET5Jq0UcU5DVaSdAzj4BUWlelAR_kjKINu1ugKO7EFD8tluBqJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۶ نشانه در بدنتان که نباید نادیده گرفته‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/695197" target="_blank">📅 17:22 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695196">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EPAW7toiZ3RMa5RSiOtBF-2HFjmao1qmv_GgWCYolyntJCgMudhQ8duHBbVnhFWiwoAbj5RTXcQfF9o9PULLnz11DCuAK1zIcBO3i4moXcmjjTyjueuK9zVow8RNHDo9h3ufslyiL4_k3DpiZCvdAMAjlIPv7iKKesiXSBI-NNgJIxU4WFnv0GDx9GIgL2VLqxW-4bypBoPRZp1q89DcfcS-DMVMEOO0g4rZCmPTCx2LFgkiY3HXUiRxI-ZbwHlZzgj0DUyUVVnNyGvsKcVec7CFoDU_9W7wf4sN1hi0kJmRyP8nIIvsiQAuq_KT__NzRDmzwF6CnTnNZxlPfDXGLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
مدیرعامل بانک کشاورزی تشریح کرد:
ثبت سود عملیاتی ۵.۳ همتی؛ بانک کشاورزی در مسیر تثبیت سودآوری پایدار
🔻
مدیرعامل بانک کشاورزی با تشریح مهم‌ترین دستاوردهای این بانک در سال گذشته، از ثبت ۵.۳ همت سود عملیاتی، کاهش ۴۸ درصدی هزینه‌های مالی، رشد ۳۵ درصدی درآمدها و صفر شدن اضافه‌برداشت بانک خبر داد و تأکید کرد: تداوم این مسیر، مستلزم توجه جدی به جزئیات، توسعه بازار و سودآوری پایدار است.
🔻
وهب متقی‌نیا با قدردانی از تلاش مدیران و کارکنان این بانک در سراسر کشور، دستاوردهای حاصل‌شده را محصول کار تیمی در شعب، مدیریت‌های استانی، ستاد و هیات ‌مدیره بانک دانست و اظهار داشت: ثبت سود ۵.۳ همتی، با وجود تعدیلات  اعمال‌شده در فرآیند بررسی صورت‌های مالی، از محل عملیات بانک محقق شده و این موضوع در شرایط کنونی نظام بانکی، دستاوردی بزرگ و کم‌سابقه است.
🔗
مشروح‌خبر
🔸
🔸
🔸
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/695196" target="_blank">📅 17:22 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695195">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b985326ea.mp4?token=vZp244s4oRp9NmnXdqEUM21GVpxd_TWmAbKIaAV44TV9HZd8QzH43I5kZfl9FzAwwSlIwvO7Yn2YONJNs8BYDCNu4IrTKJ9zlacHJknSR7MADYlgvYjLZJKOjkH36C93zWAj7w2hRUqx9JPvHc7eWoiSDf1WCaagorxhAq5quTmpWkcjcGdi6cjrBruv0mbcLFwkS00mNizbFtZk_7HVBrZJnySnw0gsALJWgCwcH9TErWFKBQq9jxx_gTUeTd-9gVRuREEuuganLi_1QIZ0NycBfqRO9FNtlSFi_tvUpGw3mJj5WjnCKuO3GjV9e1_8EGKY5dAeL9nRw_vtGd2Xnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b985326ea.mp4?token=vZp244s4oRp9NmnXdqEUM21GVpxd_TWmAbKIaAV44TV9HZd8QzH43I5kZfl9FzAwwSlIwvO7Yn2YONJNs8BYDCNu4IrTKJ9zlacHJknSR7MADYlgvYjLZJKOjkH36C93zWAj7w2hRUqx9JPvHc7eWoiSDf1WCaagorxhAq5quTmpWkcjcGdi6cjrBruv0mbcLFwkS00mNizbFtZk_7HVBrZJnySnw0gsALJWgCwcH9TErWFKBQq9jxx_gTUeTd-9gVRuREEuuganLi_1QIZ0NycBfqRO9FNtlSFi_tvUpGw3mJj5WjnCKuO3GjV9e1_8EGKY5dAeL9nRw_vtGd2Xnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
درگیری‌ها در فرانسه همچنان در حال گسترش است؛ از تنش و درگیری با نیروهای پلیس و افراد لباس‌شخصی تا حمله به خودروی پلیس و غارت یک فروشگاه پوشاک
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/695195" target="_blank">📅 17:19 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695194">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
ادعای الجزیره: دمشق و تهران در حال نزدیک شدن به یکدیگر هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/695194" target="_blank">📅 17:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695193">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb250b2e7d.mp4?token=Q7TmHh7vQYt0YAgKZ4fwFLvGU81kcj_0t7LpNiBF_QeMtJB81jA7EZF_rLsoooXK2KCB6bj5B22b15GpzdbqSMUfi2h6WSIU9svpWLCZe6dTgGpN8b95PnzWcetma8DqM8WSYbuq0Sf41xohDnHdvVWlhz0yfzwrtjptXuelpEVfUc_16rRhPfC_w6N0QfsNbXu4_RHwUPAdtHgiv6v1o5IwBh5KIEtcDOc6tcA7eX3wz-CL6v0Aw0ZvhvWpmQ7x-7o8-cEu9dcvTU1EB8KVaurRQ1mlumYRpd95WkqFifw9dJvK51S8Gxh3SxRIvstZ_3vFg5VsDHTC9mgtq2cHYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb250b2e7d.mp4?token=Q7TmHh7vQYt0YAgKZ4fwFLvGU81kcj_0t7LpNiBF_QeMtJB81jA7EZF_rLsoooXK2KCB6bj5B22b15GpzdbqSMUfi2h6WSIU9svpWLCZe6dTgGpN8b95PnzWcetma8DqM8WSYbuq0Sf41xohDnHdvVWlhz0yfzwrtjptXuelpEVfUc_16rRhPfC_w6N0QfsNbXu4_RHwUPAdtHgiv6v1o5IwBh5KIEtcDOc6tcA7eX3wz-CL6v0Aw0ZvhvWpmQ7x-7o8-cEu9dcvTU1EB8KVaurRQ1mlumYRpd95WkqFifw9dJvK51S8Gxh3SxRIvstZ_3vFg5VsDHTC9mgtq2cHYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روش متفاوت و خلاقانه برای الک کردن آرد؛ ساده، سریع و کاربردی
🍞
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/695193" target="_blank">📅 17:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695192">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
عصر شنبه صدای انفجارهایی از جزیره قشم شنیده شد؛ بررسی‌ها نشان می‌دهد هیچ حادثه یا اصابتی در جزیره رخ نداده و صداها احتمالاً مربوط به اقدامات نظامی در پهنه آبی خلیج فارس و تنگه هرمز بوده است./ مهر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/695192" target="_blank">📅 17:12 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695191">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
ترامپ قمارباز: معمولاً در انتخابات میان‌دوره‌ای عملکرد خوبی ندارید و نمی‌دانم چرا #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/695191" target="_blank">📅 17:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695190">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
ترامپ قمارباز: معمولاً در انتخابات میان‌دوره‌ای عملکرد خوبی ندارید و نمی‌دانم چرا
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/695190" target="_blank">📅 17:06 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695189">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OMelyZwT8eliBxBtFcpcTHWlxKESkZ_DwKSSYvkgeUrSzjAeoEkwyLas6F4H0JBAw9rQrlKue0NX92anPym36-RpQYW1Q5qB1rJY78s4mqLMNw91phx-SMAYWOPUoc0CZQEZREzGMJF2omIFWoGgZDmMkhOd43C87hP9gM3WhLOPsRBhiKIBkQas49o_vUHHoj4mwy5j2l3P3jlp5u_XvPwkuZBPBfdSAtrZfmKgbj0logP2MKLI2Dc9-FPYSfv5Y4cjVZ8JZW1rs-QqD0-rUg6awRF5QORS9fBHZiXhQSceXy39JsukAdhKOORN-yvHyCiJnyg7nNkVqDNs0OljJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گزارش‌ها از سرنگونی یک پهپاد متخاصم در نزدیکی سواحل ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/695189" target="_blank">📅 17:04 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695188">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d93aeff917.mp4?token=RGRJ0F_PoFcOSsrLzYABmCNETg4a6y1sAvsoZQ1UmLUDFmtxB584YFAbDrMMeeeUC2QBCg_CVWovn3p8amUDrs4oyZZ_NeOQhKPEa72EczOIOrxFRnTkHgA0PMc1vJpDGojcvprV8YRr_lBoB0VAh9lsESgwJFwY5NQZsbVqaNNrTdO0y1etXY63xKy9if9KLoNACCGIyrplRiyuWRScP34oLhm0a2d0_fMCGnkJ9XWhBlSaXOGc-MbDsIhHpajauaq3UBcrmcKYcJLd0NLmbYa7B6Vr3Crqkh_4oDm4h9zv4rkq2sbejfig0_W5ot49j1WcQ8jLoOOXayO1VZOReT8bbr1VBPE4vkeQ5y-MQ55Mx8j0jHKx3w6sV5SrA9VFzhxoGUZFJCndnEfqZDzPWUIgTCmzKNdciWcszA0WE3qOwTfNm-eVreDTSLkr6fkpGD9E9DSZyoOb6pBTUEidEwZUp0gbrvW_BO8tHgt7-eUUGa02HA9V4qkyxl-lErZ_b3j86unxTeOUtt40LVZA9QNh-ugNSf1wYsb_9WO-XlOUpAbjYOorPrxbnwBvkCr04c9VgsbRf-7mkkINEl8jg-B4Iewh1Nq4j0GfD2SpijuzVItXxCal_rTIPmJ-uBb8PWwXNkMGuBEekmv-8VwZGzGVDpxVW0PoPPRF31N9H0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d93aeff917.mp4?token=RGRJ0F_PoFcOSsrLzYABmCNETg4a6y1sAvsoZQ1UmLUDFmtxB584YFAbDrMMeeeUC2QBCg_CVWovn3p8amUDrs4oyZZ_NeOQhKPEa72EczOIOrxFRnTkHgA0PMc1vJpDGojcvprV8YRr_lBoB0VAh9lsESgwJFwY5NQZsbVqaNNrTdO0y1etXY63xKy9if9KLoNACCGIyrplRiyuWRScP34oLhm0a2d0_fMCGnkJ9XWhBlSaXOGc-MbDsIhHpajauaq3UBcrmcKYcJLd0NLmbYa7B6Vr3Crqkh_4oDm4h9zv4rkq2sbejfig0_W5ot49j1WcQ8jLoOOXayO1VZOReT8bbr1VBPE4vkeQ5y-MQ55Mx8j0jHKx3w6sV5SrA9VFzhxoGUZFJCndnEfqZDzPWUIgTCmzKNdciWcszA0WE3qOwTfNm-eVreDTSLkr6fkpGD9E9DSZyoOb6pBTUEidEwZUp0gbrvW_BO8tHgt7-eUUGa02HA9V4qkyxl-lErZ_b3j86unxTeOUtt40LVZA9QNh-ugNSf1wYsb_9WO-XlOUpAbjYOorPrxbnwBvkCr04c9VgsbRf-7mkkINEl8jg-B4Iewh1Nq4j0GfD2SpijuzVItXxCal_rTIPmJ-uBb8PWwXNkMGuBEekmv-8VwZGzGVDpxVW0PoPPRF31N9H0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برای سرمایه گذاری، طلا بهتره یا نقره؟
🔹
اگر طلا دارید و فکر می‌کنید نقره هم، همون کار رو براتون انجام می‌ده، صبر کنید! یک بررسی 40 ساله، یک تفاوت خیلی مهم بین طلا و نقره رو نشون میده.
🔹
جزئیات را در این گزارش ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/695188" target="_blank">📅 17:01 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695186">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
بلومبرگ: ایران می‌خواهد فشار را تحمل کند تا آمریکا کم بیاورد
بلومبرگ:
🔹
محاسبه در تهران این است که فشار داخلی را تاب بیاورد و منتظر فرسوده‌شدن حضور آمریکا بماند؛ مقام سابق شورای اطلاعات ملی آمریکا نیز می‌گوید ادامه این راهبرد در بلندمدت فشار «واقعی» بر نیروی دریایی آمریکا وارد می‌کند. نفت ۱۰۰ دلاری و انتخابات میان‌دوره‌ای هم ترامپ را تحت فشار گذاشته‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/695186" target="_blank">📅 16:52 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695184">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P36d6z9wEPoZtjgG9ds615Ik1Sr0-A-WQsv-96TBIssYywpHrgOe_NwlDHa4BWgPTKx3lFQFxCEJAJydonw7xMDTSg5toHzUVSyciwRkxKuXONRAgStGL-kymDtQzh2h2Nee-Id6qVzaI2Fja909O7vBogeg7n6v9x6guARkNFsWEq0sEb3qEaUVCPJtxNFzVSrn4xYmlbDAwudqx9w6B4QB7mDYgF2gsnuRxEw5RpLwts2fXWUGqEkbu8WFhcMI3LZtVJHIIUXJhFD5smUFIXyJhEVQZUOftGu0VKzhrT9DWiLRrEbxkgInQyndSBwOzCVgzwMorjf-aOgDZzlIKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این مواد غذایی رو جایگزین کن؛ لاغر شو!
🥗
✨
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/695184" target="_blank">📅 16:42 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695183">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c9ff93120.mp4?token=dlI7tEgBGusvrfOrBghd3a7aP229Y0loPLuk46myAULzZ1JxXA1c2Zuc92TUDnSXFATmpszjuxnbB_27lgw0iiDlkxnxnWVYxfcESLmDiCPrn_BQ8aaT02T6grOuBrT9MhIeEYKuAlx47OpU0ActGZEVBZUFhwcjYfVUU8BCitJun-28mm7CP7tbrIyH4XAYG6YCm82MjL2fbktrWCf6VtIEIMRBu59yk5G3bdqArjN7pcixDD5agNhvEXYlVn7COyO6nT8WxlPCdkCLLDAgs5o07aQcrCH_4GWj_Mig2jX1Pmg_M7EN2ZIPTL-DjPb4uW0Zqty_rx4T7QyJl6hG0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c9ff93120.mp4?token=dlI7tEgBGusvrfOrBghd3a7aP229Y0loPLuk46myAULzZ1JxXA1c2Zuc92TUDnSXFATmpszjuxnbB_27lgw0iiDlkxnxnWVYxfcESLmDiCPrn_BQ8aaT02T6grOuBrT9MhIeEYKuAlx47OpU0ActGZEVBZUFhwcjYfVUU8BCitJun-28mm7CP7tbrIyH4XAYG6YCm82MjL2fbktrWCf6VtIEIMRBu59yk5G3bdqArjN7pcixDD5agNhvEXYlVn7COyO6nT8WxlPCdkCLLDAgs5o07aQcrCH_4GWj_Mig2jX1Pmg_M7EN2ZIPTL-DjPb4uW0Zqty_rx4T7QyJl6hG0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شوخی وحید یامین‌پور با حاج حسین یکتا در منزل شهید لبنانی در روستای عرب صالیم در منطقه نبطیه جنوب لبنان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/695183" target="_blank">📅 16:41 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695180">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58f2ece7cd.mp4?token=TWE7ECamM_bG_eWiFtkZRbyw-_AK7y2q4bSFX1E722SsHRi_xpTrEm70Iefo1rix5k-jc1WCOUsdOvWB2rjKtd_m9cnxg3394NOMMz60Dd-wUcsBgBaOl2q0OxZtU_MsU9Rr69NDRx9oBukXaQULJy8erUCkJtIqfPlx_k19npKJ9iSUf5iX_jp1Q48QJokSmLcay1v0Dh0X_ATeMD9ETa6oZwn6DZ-EBDptAj0utfsfXCBkzHQYr_sBKpPYhn0ROd8BQ13WxoFVfmCyJevK6sXIiwwhK0jNBeppUBlegq_GOvfj_O94DH4p8BtjWqJ2KvgB4TQDgzt4VSishSRa1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58f2ece7cd.mp4?token=TWE7ECamM_bG_eWiFtkZRbyw-_AK7y2q4bSFX1E722SsHRi_xpTrEm70Iefo1rix5k-jc1WCOUsdOvWB2rjKtd_m9cnxg3394NOMMz60Dd-wUcsBgBaOl2q0OxZtU_MsU9Rr69NDRx9oBukXaQULJy8erUCkJtIqfPlx_k19npKJ9iSUf5iX_jp1Q48QJokSmLcay1v0Dh0X_ATeMD9ETa6oZwn6DZ-EBDptAj0utfsfXCBkzHQYr_sBKpPYhn0ROd8BQ13WxoFVfmCyJevK6sXIiwwhK0jNBeppUBlegq_GOvfj_O94DH4p8BtjWqJ2KvgB4TQDgzt4VSishSRa1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خیابان‌های مادریگراس اسپانیا رودخانه شد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/695180" target="_blank">📅 16:34 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695179">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea3782ee87.mp4?token=D7CwjPOXrt-M2_6_3XOCRWm1E8xwVQvhNQI_0a4VyGW6BCC3MvG0ckqRnL9r0cgBKcKtB4yfjEnI160LBihs2DJAqxGwd3RyMpd2lJ9X_09lnvloderdMESuV6oBHaPjaNcwdwHl5WWXMh7AJFJJQpyF1PkQr26VyUVPTL2P0iS1TkCa3qWoW2HqchJypOLvHy5HDg9YRrLwW7hnRwPMfeEL_MiFNTmKBS1YF1r6Qa27dnihzRFb5NWh1mjmWZ39RREbMxoQoZWPoqKAtkZJBUDU5yzHy3oI-miD9BWuLDxWKSpuki0NHgnIWDQEbGjHPMenvrQ4LzaovXuFJqMjlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea3782ee87.mp4?token=D7CwjPOXrt-M2_6_3XOCRWm1E8xwVQvhNQI_0a4VyGW6BCC3MvG0ckqRnL9r0cgBKcKtB4yfjEnI160LBihs2DJAqxGwd3RyMpd2lJ9X_09lnvloderdMESuV6oBHaPjaNcwdwHl5WWXMh7AJFJJQpyF1PkQr26VyUVPTL2P0iS1TkCa3qWoW2HqchJypOLvHy5HDg9YRrLwW7hnRwPMfeEL_MiFNTmKBS1YF1r6Qa27dnihzRFb5NWh1mjmWZ39RREbMxoQoZWPoqKAtkZJBUDU5yzHy3oI-miD9BWuLDxWKSpuki0NHgnIWDQEbGjHPMenvrQ4LzaovXuFJqMjlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هشدار جدی؛ زودپز را با آب سرد خنک نکنید!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/695179" target="_blank">📅 16:31 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695178">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nFnqHTNeKqVIpwdMC_SF1GK4hcRoSMki5yOvWuU9uIrSTHVt_vlbt3EBEHhEhYIbhCHP7oeI30amiDsfr2dD-n42dbXxY8WG0OuHbd0MauiL28W6Q1Se-GV77ExLO-zk5Scjy4tO4ccYoBg6vOej_xlV8YMuxs7dhc_vfKqDlvRfGqC-REB5NV6Oy8s5dGVdrri44MS8rAN7h_d9xVPXxXCqlnV9WVgrhR3kneWgBarsEOYG7ahFJygxtReb3vRSFwXVfXx3U4ZrcVUwofooMIPgduabxrkFUu-7JX4iEnfNHoGO8q7Kp7LPlZD2YNr_N85cnOha3FDWAzauRe9WNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مردم چه رفتارهای اجتماعی را بیشتر می‌پسندند؟
🔸
در این نظرسنجی بیش از ۳۲ هزار نفر شرکت کردند که سهم روبیکا حدود ۵۶، بله حدود ۲۸ و تلگرام ۱۶ درصد بوده است.
🔸
حدود ۴۰ درصد شرکت‌کنندگان رعایت قانون و بیش از ۲۳ درصد رعایت حقوق دیگران را به عنوان یک رفتار اجتماعی که تمایل دارند بیشتر در جامعه دیده شود، معرفی کرده‌اند.
🔸
رعایت قانون و حقوق دیگران می‌تواند به تقویت اعتماد متقابل، کاهش تعارضات روزمره و بهبود کیفیت روابط اجتماعی کمک کند.
@amarfact</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/695178" target="_blank">📅 16:31 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695176">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTSTnwH1W8CT-pc0s7--j7-Gup_9nHq4zfocbc0or1kv8DbHwpByOelIS00qcGvv6pGUjThoLUJxEn-4sCUA6VastLZqHKQyGpDSXwAwPTzjMEg9UcbG8RgRAJi_rbxc8xK-86wAU5YXOvcNEodRXz8eUbqL7T8sXB2K0OGjqYPQy7f9GyzP2nU_UwYCJwp9Ivkn1lLVhQqxyfVu0bx9nfmKo43I642mAnVnlJRY0Uqll92xCDmsBPo-AyiTHATwA_RqvsBkt-kcqBlH1PmW6Z9B0p84LbJaa__H-i6Ykso_l0_hYDYu9MMu2YNwl7zvjxQDdMSBgU4CuHS7Ji1giQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استایل عجیب و جدید مرجانه گلچین بازیگر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/695176" target="_blank">📅 16:22 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695171">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PUO75KmiNdvvXux18gCzpZ65WB1JqPWybvj5UDt2bBi1YtRz_48-e8KZy-6RjoiLdxdWvs30dFyy1IqBg0WejjdfyTMT_WQyFuQtlMXY-QA7oSdtDcoYzIE4A3MWu5yN4FcK8h4rtQmSTJm1FfBe_m_nZzZVUb_zJ3FRDfGQ3gQwVi6HC9WiayP28NKK6zykkieiO8FWrvdGpnGM4KeT4RYBwYCtbaJxExA_D606Ppe5UI35Fu0utwunF83ohXPYvwxm8wvlzOGrY_ubc_AbBHIWKB37rcZVgf7tzasmtXaBpGDtxD7s2BFK9LB0wEDzSsULQirA1jsKPxC0B9K5rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XKRojCoYUexXccg0HdkdsnrYC8qN9tHC0BcRgQ9rZSaiIhwyOkoB63eqpt0gwlu55Pj0wqW8AeUuns8Nb0Z0LD7DqDlS5ADUN121TzGiLFtE5IS7xlQh2AAFIXhzIGRAjf0_0aTeV6oF0nMAI0VpKCKM9gMFg_2QuPuvcfINnyebNNpMXL1F4Bo72UM053vn2VxOPO1NcjpgVoAjJ4CZqZ6br-rcPK02PS9VImEWjxt0bj4PWdsMKwKL-oyI8QocrN8fLy1Wztky2ka75l0VXANg9-yFpPo8Kdil9EjNzOulbA-HPX1KoGudCd9RbHnlOWKD4u5chAGwuuYdMimqug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YlD3bgyuOcWk-6fI_O701klNLNzE_FqIav6GIMufc8HlO4yS7brCE6Z2H3fx-oJbG22REMRRrWD_7hJsPoOafJwxDgH6tdtxtYxoI4pH43y1RqlZm3mLgXTox08Ct2IXoThErgUKNYB-nZN6Ur16o9WCL1KRoVkDpqK6oINcCeyprWB7wd5krfYNQu_zX2fGDB9bCYVH5tFycnWfoFS2WBOa2PX2-yYp036vhoDiznEEW6o1YAYAVMfZaw8RSBDSgglZUMGXSrfEQ7U1srsrXR8FRhCRb3U0Gj44KU7M3yJHJG1CincA1QRl-urLk6V7u8uzfD-1HGmVfVnSUOOs_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BS1_-jIEtWi9JgOQxxWSQlpHQGvsu13kBks5_f1Z-GYxRf2d4sI_s3h63okOBac9LdgRpB3tQqPVFupEXrjpSp8mbI1w96qRi5C1YMMqeU2g76VXNmZqoa13KqRb0HDAeILnGRgrllOfgTkDzQVLrVT2ItL6MekDxPK49lNJFlxOjUWb1eWR14rraEABu0wfNDASxf7vgb_m6Cl_cQPzx8W5OaubHkkR7zl4qouk9DwTq6jM-1dLKEBf5gpYolMVlGopaDHBEUdK0_xW_t7f4NhMwgCC2vKoPxBj2WtKunEv67ncdRCnWjfM0jrfZs0GYUGJ8wu0D6HIj-xHisSpUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uI__oWPrH2oKJroNkCThkfKmaObEao5Gv4B2-2E7Sg9OvQGxjNJlWNrgTUdxTXb2RMaIOGr0nZeyVq2hAWYObL_YgwYTxcScFiKjc09DPQBc8Ju_gSgJk4HHtkSpCEbamCq8D-1CEoUKwX7XenqkfrWmb2xDVrIQoj6xgX_3-s-hYvRsEKLp2kX5UIPXFPh0k0wQUkgkCnZnk5TliVLCZKUGNefzMIAZY0sFJ8sVAJ7kre2W1PfyGyG9Txoo4rd7vn__DvzvHqSOei2UiyYXZLVRl72Zgcknncp65je6FrsWBo_qYJ-Lk491JRWWUmXlRi5SsaZZq3luQHudBMC_IA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
قبل از خرید میوه، این نکات رو ببینید؛ انتخاب بهتر، خرید بهتر!
🍎
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/695171" target="_blank">📅 16:19 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695170">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
افزایش قیمت ۲۰۰ درصدی ترند این روزهای اینستاگرام، ۵ شاخه لیلیوم نزدیک به ۵ میلیون تومان!
اکبر شاهرخی، بازرس هیئت‌مدیره اتحادیه گلفروشان در
#گفتگو
با خبرفوری:
🔹
بازار گل با کاهش ۳۰ تا ۴۰ درصدی مواجه شده و گل از سبد خرید خانوار حذف شده است.
🔹
محاصره دریایی و هوایی موجب افزایش قیمت پیاز گل شده و گل‌های وارداتی نیز تحت تأثیر افزایش قیمت دلار، گران شده‌اند، اما گل‌های داخلی افزایش قیمت چندانی نداشته‌اند.
🔹
قیمت ۵ شاخه لیلیوم از ۵۰۰ هزار تومان به ۴.۵ میلیون تومان رسیده و قیمت لیلیوم و ارکیده حدود ۲۰۰ درصد افزایش یافته است.
🔹
از ابتدای سال، قیمت اسفنج گل‌آرایی حدود ۳ برابر و قیمت کاغذ تزئینی گل و ربان ۱۰۰ درصد افزایش یافته است.
🔹
قیمت هر برگ کاغذ تزئینی از ۷ تا ۸ هزار تومان به ۲۵ هزار تومان و قیمت باکس گل نیز حدود ۱۰۰ تا ۱۵۰ درصد افزایش یافته است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/695170" target="_blank">📅 16:15 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695169">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f512f4a2d.mp4?token=BSQAHrmG2g65bvOyske7JZJQ2OL7GSHsHVeicGSoNdIjiBcfXeUMsI6UW9yleyUX8mqHC-zW99KNcH36SdnxgjEml4i5nz6GNED_lVptsBodj7Q5AAwkrE5ixIRpy6XhMBv8wbGuxT6r_MSnOUfB7_pInsSLrFqUNAh602U4dxKSlvQDOesEOpGZqnhkAe7DLLuguJTlz6DWCo3TmssQliZ9MSHlFKeCE2HRiF8LCbBKW7N21kwamdRZCNmNPuAv-TsmGduMkuzXQWkP3qNRTV9dpss6fByp6aopvoVjj4mWbBfABgEV5Paj4vXyJTnKxI1UeVx7IB0DTTs36RnnAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f512f4a2d.mp4?token=BSQAHrmG2g65bvOyske7JZJQ2OL7GSHsHVeicGSoNdIjiBcfXeUMsI6UW9yleyUX8mqHC-zW99KNcH36SdnxgjEml4i5nz6GNED_lVptsBodj7Q5AAwkrE5ixIRpy6XhMBv8wbGuxT6r_MSnOUfB7_pInsSLrFqUNAh602U4dxKSlvQDOesEOpGZqnhkAe7DLLuguJTlz6DWCo3TmssQliZ9MSHlFKeCE2HRiF8LCbBKW7N21kwamdRZCNmNPuAv-TsmGduMkuzXQWkP3qNRTV9dpss6fByp6aopvoVjj4mWbBfABgEV5Paj4vXyJTnKxI1UeVx7IB0DTTs36RnnAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای وزیر خزانه‌داری آمریکا: ایران این هفته نفتی برای فروش نخواهد داشت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/695169" target="_blank">📅 16:03 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695168">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WYDA_2hEgV92MvVi8c8cZyhTB4vEe1jBGwx-XRU4L8m5Wi9Ys_AVdiNuEJpL4vazgvw5eDPpcxXr7g59RD0boKU9dzrMIn5RMiNoCXOoijPia_Eh-deUd8exOzWkP62_1GOHbuC2wdAOoiXjCLG9gTGtPPpVez_O9RUk5y5hDuWHcrYW12VaOcreLq0QX74NHGrfC4-B5iFfQR9dBnvwi0i4RqLnNVm09RzXiTD8QSESnp_TTq6ydYsY_4x-nMiNY6jFkhQ_poNjV8vfeUEAvUZk0qOQkr9KBOrimLwWW9ERT7V1f8VC7xZaFNuwDiZpdosd1o309-jTPgZvzRoCrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کهن‌ترین درخت گردوی ایران ثبت ملی شد
مدیرکل میراث فرهنگی لرستان:
🔹
کهن‌ترین درخت گردوی کشور با قدمتی حدود هزار سال در منطقه کهمان شهرستان سلسله لرستان، در فهرست میراث طبیعی ملی ثبت شد.
#اخبار_لرستان
در فضای مجازی
👇
@Akhbarlorestan</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/695168" target="_blank">📅 15:56 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695167">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">خبرفوری
pinned «
♦️
فوری/ نتایج کنکور ۱۴۰۵ اعلام شد
🇮🇷
✊
@AkhbareFori | Link
»</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/695167" target="_blank">📅 15:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695166">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GbYor4fV6uEFPMjBs7-To0NYcWvfAbw-Gfsc38C34Jz3BxO5N4uYHKW2kmmhaleBRSfIYFyzPCAwwaH05CCCTuxg9iWSyAq2reD_0lUyy0N8DNBxUMqNhxQvRUjoeSFja3n0AIMhgoPInaecDQS57ysmcuAqxCgg4lKIgu6rMoqoWH_O57s8_27IUV7_MxDzY_MlD9bTxSId1Bip0-eds6EpuSAtjdzJGP-m2NCc8dC2EiPoSE2P_xrEGgVxn-dV19IezRuh7vOwQT5C9kuTKAD5BqBpT2cx9K0sBI-I8wAUfeF1ADF0W8nuYW29WjfVC0pRom1J0oTgvkkGm0puyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر جدید از تداوم آتش سوزی در پالایشگاه «آرامکو» در ریاض
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/695166" target="_blank">📅 15:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695162">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hcLydsBVFWDDZ5RiZhkVKhnmdS2zqyOIXXZvITybpbqoJPO8GE7A1AcsdcFbQYbLmLwID7DMMJYRjfRCRWwacto0NhL6Zls6hQ3Lm13UaOQMdWefOUA2aQMmLrwHRp2uHgRiy20eNVeQpN5fs1b3qHFXtX8z0_I9LhVHrq0A7ytNsa67jIp4lXFvqQfg1W8Jv0_I4gEli1v-P5NVJkvlmiKs_z9CQvt7BLVMVOznASFI4gfZBt1lRvQBsOvkzYwIrhQocGM10UJ-veFaYfx4VZjjRAOCsYiFdIMSL5Tz-i1Lz2mqXOkXO1_fB0iHSg8DGoKhvI7QXVhuMTvCxyIozg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pEQe2eesYxFhTOgbFPPmxeicfWHjpkDEtkB2gTSDq6KBgHrSsf-vQgWOxOuzsI9ZVu3waKXHfAQLIPqLp8Sof-VTyXcS-slWtE2_lqhY78rYtVHt74yDyedPqsgjPYj9EA4aojHrwTcirSlmiXT68pzhH0TZk8XTmafUQwq-l7S1Y-MimKqq5IE6Ac7zzRdCng78wagIIc-ALS11UGhZFMIx4hnmVoTHQBa92UQkuHNBAo_mF4so4mMYlLNpWoPffX26ZvE-FRss8YWyUabtlCg4Em-nuz8JOAQ-voNEaObKzYDJ9g9Ibra61D2_a61uU5Z_05C5jzP71CENe5XeRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/akG1tuyBtK6zpYPSSDsYNB6869s_Fq_vft7R1K3LlvKD-bceQHpDUoYsjN6FZMQ-wVzbE9891O7des6uZ5bIok42-W4t-o0t2o2w1VksPXqWT2kEhBnPoWVAH7i1oLfTjva2uyY_X_ipRwJk9LypE410R3_NKgQSQ5cCPad8TzkN1lDHaJrl8wcjHZ0dyJ_Va__af_FY54a5dfs1zoe2nzejdlYkanlX2uOV8izgmDiTf9OJyc_tS1UtPbzVVF_IXr8sr-930qixefWNDf3iaPgrAEQ1feUTA71_C0FAa2rF8LD0YlQq_vryjbQtLJ46RMfug8KYe5V2LYQ4fVBGvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BFDqE0hAyg7FU1tY0n3dHPj73uP-Y9XZlUdQ7o7H4D5_Y_WHxjAi01XKtoTuvFOab-U2LDMmSyua6pQnw4FRRa-txA3rGLWhMhG8NgD4BNwQlLahiK9e7fDVByPeQoEwEXjsPkkt0h99JtGFaPXuRvAwId8NSymfO5yRV1Xf0nmldg0Q1c1BYZ9NNk5dolS0mX_uGROm3aid_2HWreiJ39buWjaUrYw90yB3DLy7X0FgvnoJRB-XuUjQg3_3ZwMV4S95WTrjQzsncIV15I1ysJYw16qLGN2S6U62uhAKs89aNUDO4Focj4GOp4pH-gXqH8mm8qJjbTKxJRVsTmRdYA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
پایان موفق پروژه «پل چارگون» با ۴۳ تیم
🔹
پروژه پل چارگون با مشارکت ۴۳ تیم و ترکیبی از تخصص‌های مختلف برای بازنگری در محصولات و فرایندهای سازمانی به ایستگاه پایانی مرحله حضوری رسید.
🔹
این رویداد فراتر از هوش مصنوعی، بر تقویت آینده‌نگری سازمانی و هم‌افزایی تخصص‌ها تمرکز داشت و ایده‌ها در قالب‌هایی نظیر مدل کسب‌وکار و نمونه اولیه (PoC) ارائه شدند.
🔹
شاهین طبری، رئیس هیئت‌مدیره گفت هدفشان صرفا پیدا کردن یک ایده طلایی نبوده و به دنبال تمرین کردن توان دیدن آینده و همکاری در سراسر سازمان بوده‌اند.
🔹
‌این پروژه همچنان ادامه دارد؛ تیم‌های منتخب ۶۰ تا ۷۰ روز فرصت دارند تا دستاوردهای خود را تکمیل و در روز نمایش پل عرضه کنند.
مشروح خبر در لینک زیر
👇
khabarfoori.com/fa/tiny/news-3249563
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/695162" target="_blank">📅 15:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695161">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b29b502f2.mp4?token=T4AFYJJvcHgPjxFLCA1A2yj3B1PsqlQd56R7HuoiqQlofemjyEdp1lnCe4QU85vxEDHZguWpysSBmizqwKX568TVniWaILh2l0F2kcQNENzJGcEvyTlDs_fwqbIE6F4Wc0CSAiJkmjfK52ll4E8DKzN8DSRgtzcLpLlFaAOisBVQ2FQFOvn8zJ3F9yPcsdJWEfAtjnNXZZ1vraDaI8oswYHK7mCGQmwZ6ywtQHijJObcjny873RyjsBnZjNAdn9IuQtIixc9-8wmjyGTSTCpWK9PG_ATVqBs-i5jrGjGy8aWp5ZiDugAWiVSPQOyVK8BU7rkfwXGt3b-kYtnY-wVlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b29b502f2.mp4?token=T4AFYJJvcHgPjxFLCA1A2yj3B1PsqlQd56R7HuoiqQlofemjyEdp1lnCe4QU85vxEDHZguWpysSBmizqwKX568TVniWaILh2l0F2kcQNENzJGcEvyTlDs_fwqbIE6F4Wc0CSAiJkmjfK52ll4E8DKzN8DSRgtzcLpLlFaAOisBVQ2FQFOvn8zJ3F9yPcsdJWEfAtjnNXZZ1vraDaI8oswYHK7mCGQmwZ6ywtQHijJObcjny873RyjsBnZjNAdn9IuQtIixc9-8wmjyGTSTCpWK9PG_ATVqBs-i5jrGjGy8aWp5ZiDugAWiVSPQOyVK8BU7rkfwXGt3b-kYtnY-wVlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر جالبی از شباهت شگفت‌انگیز طبیعت با اجزای بدن انسان؛ گویی طبیعت آینه‌ ماست
🌿
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/695161" target="_blank">📅 15:45 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695156">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
فوری/ نتایج کنکور ۱۴۰۵ اعلام شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/695156" target="_blank">📅 15:41 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695152">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JobJ8z1NR3gKtTlx4-A6rCWR_6EhKrispB0v7WhRobuJEjyu5jBlnNHk5THo_ODzl0mJZ14lTOLIjJlBelEcZ1p_T8Z_1Q6SrOALJHH0hro4O5yK6VgK1Ai9vg2vOKLK9CgY6j7UUSeZyI0az9xuOaSWyJmVkCZtsXDpXUcbIGiUya5wujJoA2G0iphu9eBpebZ3DbkH9lX1-sYNMeHHAEz38aPN9IqRgw7IUjlvi0CgRi518EKmvvtJTvIA2Bo77OmEmkYk2X65toWBe_mgCRnLWyfg8N6cgPmu7jPO8WDuMmNePpmeCFzfEM-8y3ejP8UoHHl94oul0QEtWgFMiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dWkC3PGr34j0WCP-YqooE7NEFlSDl0xKBRkMOsvshUdwPe6LGuYzSXOLqNxjNNKTh9XZ7ycXJagt9nksEbZqIT7LmAX-7khQSVqS-mp_HyiAJuEhUN7GpyjF0Ul1xFAjtmtErhmDNEz0E7C2K0PCtgmmkyoO1BEZ8JlLr1cPmE-mQDbGokJcjEoo3BzOl0a9QH25PtrZYT3MjIrVhnGHXuFpV4hIUp0arrSB8z0LEJ-gRXeODaQl8-xY_g8PcbisVSV7nJgh2i-JGB4kMSzc3XW5CACNEU7D77BCEFvneX_WRQ1AiKqdBDl0jESvZgglyO1xnkK8kqaCHv934-5EMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bo2hoRzYn04gYIhdCLf5XiqIIGDyQ-i5AqPip8NH1BqQqmKmU5y7jX7g1L2uzcGplTZ4qwcftVGD1-OuIr_yKEuqJeJ_DzwZ2KopNDolWEKWLAIRdNH9lts2AVozeAXc41TdGt2VUKCSoP6IfXmzeNOzBj7kICFKUSt3xP6hBYQk3rZOQ4f5Fbq_KHdTZu-RDVdidd8y8nlDbgRBszvVyYUpXbo0djusnHD0TnVP2-p7idljf9E5nPZiEgpUH4lzg9Q9jwjsnolkDEPyIIXKK_t7LK5c06ke7ELzvK9DknO8_aXXL-v5jH_94dGWuJebTH7OSrq1LVjnQ2ECh5Wupg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QpYxlidK0DjAAMAc8KATiSLBiikutKOX0WfXNwei-MJOkrZweNQR_7P3YQApn5Gb1qF5dvL_faUGXS8s-REDQjDlR1PtXqV1I2V16yPn1a8MNgd2iAOZrrqWITEXzfzXMvw06qkYx9pUSVBbvc6NguBs-DLFrt4b7Bfkk572_hZAwa-bSstSohq8Fx4D3pifn3qiIlb-KkXIsvovbV9qCy3Qr8phsqHs9xmPli1NVYt_FAzR_ccS_VmaIONdTFpr5bMvbcQFEExy3QzX-f7McC9gheqkY__g0dKX2wVqPchHzsASmdX39W0hoglFbOt_CL_uRh5UdZCOYf1J1Fc4Xw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نرخ کارمزدهای بانکی در سال ۱۴۰۵
🔹
از انتقال وجه و خدمات کارت تا پیامک تراکنش و اعلام مانده کارت؛ نرخ هر کارمزد چقدر است؟
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/695152" target="_blank">📅 15:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695150">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V7ArkEB9RadcQ3n27rdarP8Sh2Mn-Ti_-j6wOdJBrNccwTCNB5i2iolnVMIpg0qomVueUGibWQxryWfdaGI3Y6PAVSrZE-NNMmB7kfgCojcmlVUHddeU0sBNefjSHkUSDWhrVkxvgTwdgmxTNpafIYVsa_CmtUdMJRX9h8j4-4DJvVKmnBBmoXWQZmYlH_8_FB7v1_Sx9g0oSouMgT0QaU6CWpve38-U65pHdBA_rJryLElq-QBtKAQETr6EAwngHmIEdD9TSQ67NtpkhRYanM3C-i-TKC9AoxRb8Ltaqg8zOgOxJe7NihNVV_Qs8QNwcOmK42nDy72pasHf7n6Sgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/smXYFoavvw_xYM64S-wjDGpFqG8Ew-wmVRmxgHJ2_ezoLbIab3jq46YNNV8z02SO21Y84uAhYSIufMSgcnSU683MlAMeH21WlnOe6ABiSMq0_XZLvNxi0764Bu2crjfdhdv9JEh0mhrFkcgmWfyP7tjX1PthK2x8LnK3Oyek4kIw6f42EVJBoh6UhbCKZ-vG8UggPkhySTx0kvj0Og6CFSUaJX-FZGqYdmF9qA56JASoJ2x_p_9wVDURFUo1tDn9_iKUi8POMt9K7g07qh2LiLZHJQ0rcvn0LdDoqrx8UXTR-yWJr6w4KOfg2HDra87UP68h7P0RExhzJg1fIUi0kw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
مکلمور، خواننده آمریکایی و برنده گرمی، پس از کنار گذاشته‌شدن از تور اد شیرن به دلیل حمایت از فلسطین، تور اروپایی خود با عنوان «موسیقی مقاومت» را برگزار کرد؛ تمامی بلیت‌ها در ساعات اولیه به فروش رفت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/695150" target="_blank">📅 15:32 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695149">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FQsS8ftDogb0zxwDvm7BIogrnhAKux4l_B54wocSL7-o0FrSgnn_pZsmJlOC0HAZtc3CxlLExgYnpnRAfcBnUuYtxmQYOB8JhKiigY8yDJMfSHMM8CAW_UFXmqDXmwrRCczsBJ86xaU6cmICYYxOEin_xy8vTz_sqRscshXTBqwXaryQXAH2WxO3sFFBiyBSR28cxD4kXLbHmkD8KOGwZ0O9klPpZE_0kk2bMVvDYBfGY_P7KUEsQw7uwAp6jwCMnp_EM_fgFa-c-h48bGGTpY4MOz3VTu1D2O6CbmptEvalJ2XRnf-jAEA89-DfcCHxtVzLKo49NvrU3VkIlo8WSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اشکان کریمی، رتبه یک کنکور ریاضی ۱۴۰۵؛ مادر و پدرش، هر دو پزشک هستند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/695149" target="_blank">📅 15:28 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695147">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/di_SRZSKlY3-iuxI4xXibyT8654w2dVU63akbTIyXID9PakjGS4yZ-nK_yRwInLmOlUUsgncDz8mnLE09IWye1MZIsAKiwUTWfGvvBGmx-4VZ41QiVgLXKNXSzKuzL1HOQU-Ag1Wr3jXdxPPCVVoohtDjAXzJlacXvDrWSqsr5vab_5l9OqpQW0CJJiaAXIPK8VZgAQjdB4pTowR1kjgwNpcwNi-TMaCf9iqoGjWGZX27XFg2lmQVrL9k51sLOD6BvZQUc0c8kPGYRjfk8RJxeH9mgO3QPQE9dddz79M_LPCdHDI_JvIj1_DVTLpnKrFMygi5oSBwSebPtddVXU3uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WOLzdOHkqVDJLcx_HE-GGxE9yypJQZPDERJ4BG6l31ndHLa1ECbKzOarufpKBHmd27YhoGGcGvkctOeDo-hePkHz-MeFafTSBpNKBGgslh5ZawDDexve-xv3inilCQ2bSyNcegC4QDvesm56B-wO9I4i8za8jVkA87285IyghefiPJA7jQ1OaGxnqfmuBTt238lyvPQxr0mceT1ZNBwxKu6NqjK3gqEZrHdzKh2BO8YOu8VgY4VH7rVGwBzFnDYIIxP16vvk2h00VdmbPVFCQnWiMpjcZ4e6KscMKsLPhCseZpmDrWiciB4tKJw5uXCt27p9qXyQcy5POhg7BmF3_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نامه مدیران عامل شرکت‌های هواپیمایی به رئیس‌جمهور
🔹
در این نامه، مدیران عامل برخی از ایرلاین‌ها ازجمله زاگرس، چابهار، کیش‌ایر، ایران ایرتور و آتا، ضمن اظهار گلایه درباره اقدام اخیر سازمان هواپیمایی کشوری در ممنوعیت پرواز برخی از هواپیماهای MD، نسبت به پیامدهای این تصمیم برای صنعت هوانوردی هشدار داده‌اند.
🔹
کاهش پروازها، افزایش قیمت بلیط، فشار مضاعف بر ایرلاین‌ها و تهدید اشتغال و معیشت خانوارهای مشاغل وابسته به صنعت هوانوردی ازجمله مواردی‌است که در این نامه به آن اشاره شده است.
🔹
طبق آمار غیررسمی بر اثر پیامدهای ناشی از این تصمیم، موقعیت شغلی بیش از ۶ هزار نفر بصورت مستقیم تحت‌الشعاع قرار گرفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/695147" target="_blank">📅 15:28 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695144">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99155c9708.mp4?token=Gsdc0_YPB8YsQ2ZrA5XnVj6gUNjRZs5oRmzVvoMlGzYHhtEFcyhf5BnG8rceEoHbAb3tO4bs5XCHr6Wh7bbU8d35ekiEN9-PhpOfr2g5tURBpJgyJCR3IkG86QhLgs0mZaQ6zvLdMPuOC51cS0xSrTrOC8jkALkivHAb7T8xSYG1krnTXYXFVs8jIG106txwoPszEHOvG5gYGZhB3C9FfVXUHX4uIZVwclFp9njKVp54KqS3nmlZYzSoWuro2hyyBCtzXgU5_r9Q9TLjVF8u4TK3leZASAJHQqts4tB2g1Ah9YKFdCl5-Z0o_1U8pvxNNitBDKYVjH4TKbQpW1vLZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99155c9708.mp4?token=Gsdc0_YPB8YsQ2ZrA5XnVj6gUNjRZs5oRmzVvoMlGzYHhtEFcyhf5BnG8rceEoHbAb3tO4bs5XCHr6Wh7bbU8d35ekiEN9-PhpOfr2g5tURBpJgyJCR3IkG86QhLgs0mZaQ6zvLdMPuOC51cS0xSrTrOC8jkALkivHAb7T8xSYG1krnTXYXFVs8jIG106txwoPszEHOvG5gYGZhB3C9FfVXUHX4uIZVwclFp9njKVp54KqS3nmlZYzSoWuro2hyyBCtzXgU5_r9Q9TLjVF8u4TK3leZASAJHQqts4tB2g1Ah9YKFdCl5-Z0o_1U8pvxNNitBDKYVjH4TKbQpW1vLZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم‌اکنون، سیلاب شدید در اوز ؛جنوب استان فارس
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/695144" target="_blank">📅 15:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695143">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
ادعای جدید ترامپ: به نظر می‌رسد ایران در حادثه فرفورد دخیل بوده است
🔹
ترامپ: ممکن است از اروپایی‌ها بخواهم ذخایر اضطراری گازوئیل خود را آزاد کنند #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/695143" target="_blank">📅 15:15 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695139">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LisVHhjHey6HQLflLl92B-gnMN7JMud9NBNItc-Zcv7X-_zlUUrK7pazhY2CN5SF8PP8mnReD59JcaT_g7WzEfMzfTp1XWqF0ltJY_1B5LeLKWwPXIcBpldHdJesQ0twC_Je13xwYWuWe3f_UdUT0eZDx7A-yO6KVOC4bUEC-1BESTP5Ky6NCIWZX9-bdLA_fvVtbI74Oi6u_-aIrCa6hbcCY1oTFTveJdRhCkBA52L5CgK2LAQm-nBx-QCgu7W3RMrSWysiS7JM6eIxe0Ue-4PnbDbqw6WaCWYP3VrTWfwNhe0a-fglA66vzgGAXWMSSTuq5mXSa6hHdLHR9gZJNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/go_0ROyFpEf5iBervbKm9T-EWV3MH5V5qpuyGk08G0vtt_473-pWWnfXWDGPJYTS3ufzRRs_EblrK_kNeanhDDP3ZTbBNN83k_JgimABhdFmmXkxxiD9e4eVkOph76hhfiI01dHlNmCGfX5M2UFtDuZL3e-OE-dtftRLz_qhJoCvN66_yQNm-D5thtZ5pzuV01XMWGVp7sSKywCBHlNmPxBkTP_gILoNOD3QWI-7gk-EXaybhZEkhXoUkgOjhiHrhVlsyhLPNwfbK76eV6cSwqz6Lkr0SNzlItYPSfgQcRZGDffRZq6zICWivKXh3xzE7QXCRSqC1E9myzPjqv7XXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wdk32eSZ7IkUWZ8C7kXDn-fg0BUuepxZy9T_rWaz7E9-1dmGjcjZZ9Z-ltHahIbic0-o_VVf44BD_YrOdXpK1uPFDuad89HrATODTt0f5bgfZg2K7NX89DiODkmVtOngbKgvi9BN4fuYPO6C8Bp0D5N677GhnxF-mmaRgiKIrPJ40SPWos2buomGqHeFX6iQIRmf6cySgxDx2eN2aZRHUgNGpeMCJcJ69cR4FijGoM75P5gPGlVYMCWa8xMu8qxXPPhvf4_0cqOUNAUmIfkCxtP2G0lni0k-KbGX2dg14jp08aWokX0AJavZFtR97kuwvro0CcpgR364HWvABWuS_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tBK2qFGUyzo1cQfkmK_DDtnb0pj5D_uZVDZQTMJNMLDaZU2Q8XVkCS7AtJmwen1G0YPV2BP3zZuH-J1V65FJy3I8UiIQl0fHch2Jem6aQUiCF8kh2q7T2ogtjWhye7Vth1n0lEtF7bikxqeBZ8pRs69mj27Bzn2ZOHsKPXApMiXXYHY8Y9y8LHnNCypkazBCaPEoJpcHVxDV_b_T1B8r35yaaVAdazAF01Flnc-uzfntcpnpY0OXcCZs36kbO56lKf-ViWDj17qTEkjdul-adKM6SuriojhEWwl3utWSBSRr7xyQK_Ie7NSPFme-52k2WAQC5neXavB3SeC1Sovahg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بهترین‌های عکاسی طنز از حیات‌وحش
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/695139" target="_blank">📅 15:14 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695138">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
وزرای کار و جهاد کشاورزی در صف اول استیضاح
مهرداد بائوج لاهوتی، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
در حال‌حاضر شرایط استیضاح وزیر کار و وزیر جهاد کشاورزی مهیاست و یکی از  علت‌های استیضاح این دو وزیر، عملکرد ضعیف آن‌ها در ایام جنگ است.
🔹
خبر استیضاح وزیر ورزش نیز مطرح شده، اما فعلاً اقبال بیشتری برای استیضاح وزیر کار و وزیر جهاد کشاورزی وجود دارد.
🔹
استیضاح وزیر نیرو از سال گذشته مطرح بود، اما هیئت رئیسه هنوز آن را اعلام وصول نکرده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/695138" target="_blank">📅 15:10 · 11 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
