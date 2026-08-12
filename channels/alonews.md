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
<img src="https://cdn4.telesco.pe/file/TF5VU5EXClRNOWjcIzWzl57iqYxUzwjq_8beCc6MU455pTd7H9xnNvSAP1AJWQIz_H-jrEzaUp525VoHVKoFf5jpa9VxSV7Yq99avX8acNk5q4CFG7k9NsTZzSZSeS3LpVubPU00PJwBNWcfEW-7ULPudr4fWCTzkFPZtw8Ttapi5jS2_5rcvVvBhy_9ov6035OM9gW-z3gOuG14cO4NMEWaRvQdEnC6wfE_vi8xyRjUQWl6ljjcCTCoFoAU0oqMxiOSiPXZ5irapoGKLtJhlEZ9B_XGOU9iInnSgWK5pxoie1O7aK3krUu72y7PIePwTRZ6wfV92TVKwTKAozgC2g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 967K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-21 08:54:13</div>
<hr>

<div class="tg-post" id="msg-141256">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0dffaedf3.mp4?token=VAkvltPBCB4bK4QytC_595JlewpN3IRJmKBNTn1CCxLGaeDzysSr02lm0Xdrhl_jySDus8Eusw4zyf_2gGIrHXScVFN9tTMBnjU8mVheRtsWLXQY2VThLV4XI9X3Sa0m56n2Iv-zsIGrUWxAqL_JkFfzEA0GzrixK_smJYEiVFb6Gddt3PzqvxpBEoqh8T_-Zzc-hw8cgytCwsH0ClWwHpm3ynO1gSw1jQ83G0KRr1PI6spKwQ2WLhfLsUvAvBHwyUguI_m-iGGbbGpgDGgOPtdEC_jbLFqP8Oyw4Yop96U8Yva3CKxM2da8NHdYQZvzgWw3DoqX7zMOqEwLJjRdag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0dffaedf3.mp4?token=VAkvltPBCB4bK4QytC_595JlewpN3IRJmKBNTn1CCxLGaeDzysSr02lm0Xdrhl_jySDus8Eusw4zyf_2gGIrHXScVFN9tTMBnjU8mVheRtsWLXQY2VThLV4XI9X3Sa0m56n2Iv-zsIGrUWxAqL_JkFfzEA0GzrixK_smJYEiVFb6Gddt3PzqvxpBEoqh8T_-Zzc-hw8cgytCwsH0ClWwHpm3ynO1gSw1jQ83G0KRr1PI6spKwQ2WLhfLsUvAvBHwyUguI_m-iGGbbGpgDGgOPtdEC_jbLFqP8Oyw4Yop96U8Yva3CKxM2da8NHdYQZvzgWw3DoqX7zMOqEwLJjRdag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
من به ایران اعتماد ندارم، چرا؟ مگه فکر می‌کنید به ایران اعتماد دارم؟
🔴
من آخرین کسی‌ام که به ایران اعتماد می‌کنه مدام به من دروغ گفتن، الان ما کاملاً کنترل تنگه رو در دست داریم
🔴
اونا کنترلش رو ندارند، ما کامل کنترلش می‌کنیم، مال ماست، شاید یه زمانی کاری بکنن و اون‌وقت کارشون تمومه
✅
@AloNews</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/alonews/141256" target="_blank">📅 08:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141255">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95e1e30aad.mp4?token=aSBLSiXa_CHOeKmP4Q-yV8S8XZKaT0d-Ms4KFTw3KA2kFACou9YFDW_6b89eganKSaDOAZiA2DuynPxUyLIu-28Y6JrfOs_qfirVuRckAEXfqjxPTda8KRhqvrjynJY5_2f6Vb9Cql1Joe-j4gyPeyIcDPIe3nYHfFgYA0flBZ4xYeflXdQdcy2STNOxpKnD-LGYy8vADnc5jRrb8p0WTcQthnv8sMkkCTjDut4kOidZSHmxccYgM0iJh_9411Vm_OPtdpyQ4T58HskyfzyhaiXfF5HcPDZIOfk6pSvC_jlyZzsbkDXjrqYiAFNXxIACPpwiCjDxbdhtS5jBn_O-VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95e1e30aad.mp4?token=aSBLSiXa_CHOeKmP4Q-yV8S8XZKaT0d-Ms4KFTw3KA2kFACou9YFDW_6b89eganKSaDOAZiA2DuynPxUyLIu-28Y6JrfOs_qfirVuRckAEXfqjxPTda8KRhqvrjynJY5_2f6Vb9Cql1Joe-j4gyPeyIcDPIe3nYHfFgYA0flBZ4xYeflXdQdcy2STNOxpKnD-LGYy8vADnc5jRrb8p0WTcQthnv8sMkkCTjDut4kOidZSHmxccYgM0iJh_9411Vm_OPtdpyQ4T58HskyfzyhaiXfF5HcPDZIOfk6pSvC_jlyZzsbkDXjrqYiAFNXxIACPpwiCjDxbdhtS5jBn_O-VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
تهدیدهای زیادی علیه من هست که شما ازشون خبر ندارید
🔴
هر رئیس‌جمهور تأثیرگذاری تهدیدهای زیادی دریافت می‌کنه، رئیس‌جمهورهای بی‌اهمیت تهدید نمی‌شند
🔴
فکر می‌کنم شاید من تأثیرگذارترین رئیس‌جمهور باشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/alonews/141255" target="_blank">📅 08:48 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141254">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
ترامپ درباره اینکه چرا خودش با ایر فورس وان پرواز نکرد ولی خبرنگارا پرواز کردن : نمی‌دونم، اتفاقاً فکر می‌کنم هواپیمایی که من سوار شدم بیشتر در معرض خطر بود
🔴
خبرنگار : چرا؟ ترامپ : چون فکر می‌کنم همون هواپیمایی بود که احتمال بیشتری داشت هدف قرار بگیره
✅
@AloNews</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/alonews/141254" target="_blank">📅 08:46 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141253">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d65563b805.mp4?token=uPbpRFcMui5nHZKMK6kZ5iwbg0omozFqhckEn75AHd-mRdSKuXk4NDxEU6rl9SWXtYI-3dRXSRZckHL2tF6LBncdlnQx3b8fIJ_Av73h1Qog2kpygft4eLxJmCQ3Qp4rdejFnN4pa06BdxuwwQyXQMRotn1emEMyya-WIIN_eW0iwv9gIvPfXZXyWRaBwEvSDWdMEm_7aTiGmaPqFzbej0yrLCajwh5nrb7sX_o-5HCdUNp5nhdysvpfl2ymEhRoWEw2pt-iVYcV_gDNnVEW5SjhZuEYC0ClIYpzUjF-4QCRkg__i__uM643ZUv2B2UmPtRwIhn-wYFGZh7ugCxxNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d65563b805.mp4?token=uPbpRFcMui5nHZKMK6kZ5iwbg0omozFqhckEn75AHd-mRdSKuXk4NDxEU6rl9SWXtYI-3dRXSRZckHL2tF6LBncdlnQx3b8fIJ_Av73h1Qog2kpygft4eLxJmCQ3Qp4rdejFnN4pa06BdxuwwQyXQMRotn1emEMyya-WIIN_eW0iwv9gIvPfXZXyWRaBwEvSDWdMEm_7aTiGmaPqFzbej0yrLCajwh5nrb7sX_o-5HCdUNp5nhdysvpfl2ymEhRoWEw2pt-iVYcV_gDNnVEW5SjhZuEYC0ClIYpzUjF-4QCRkg__i__uM643ZUv2B2UmPtRwIhn-wYFGZh7ugCxxNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
،
درباره نامزدیش :  دوست دارم دوباره تو سال ۲۰۲۸ نامزد بشم، ولی قانون اجازه نمی‌ده
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/alonews/141253" target="_blank">📅 08:43 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141252">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64ee228998.mp4?token=Rim9OcFO3USdbw4n1Mw9hDBhxf5bmxolTzRucCr5leygc0uwW-ixeGzVnb3s7Mv-UWRs27qs3E-j2Jpjy45g2a7HGRv7G2jRH2yt-5NBoKNVVjViSZvFAHcoLR77tr6jLzGSF87yeNTOeT4KSqmcblvP9hQ-EhXwxSzEDkZzTy293LWATHJhkghpmzmfXD9ViJJACQSzaLoe9XzsuyOS1-iVyPGD2LorXAmHhmr22AtLB3ZaDuDeDqzUGY4vMquvx0jxJHw1uQIrQ397acMuyY8KelYF71xDSBRxV81prWsk-oLQSTxm4NhtP-QmUgS2XenwJ5PKqAwL1hArzGtvdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64ee228998.mp4?token=Rim9OcFO3USdbw4n1Mw9hDBhxf5bmxolTzRucCr5leygc0uwW-ixeGzVnb3s7Mv-UWRs27qs3E-j2Jpjy45g2a7HGRv7G2jRH2yt-5NBoKNVVjViSZvFAHcoLR77tr6jLzGSF87yeNTOeT4KSqmcblvP9hQ-EhXwxSzEDkZzTy293LWATHJhkghpmzmfXD9ViJJACQSzaLoe9XzsuyOS1-iVyPGD2LorXAmHhmr22AtLB3ZaDuDeDqzUGY4vMquvx0jxJHw1uQIrQ397acMuyY8KelYF71xDSBRxV81prWsk-oLQSTxm4NhtP-QmUgS2XenwJ5PKqAwL1hArzGtvdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
اوضاع ایران داره عالی پیش میره ما کاملاً کنترل تنگه هرمز رو در دست داریم و نیروی دریایی‌مون فوق‌العاده‌ست
✅
@AloNews</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/alonews/141252" target="_blank">📅 08:41 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141251">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e66e57720.mp4?token=rPktAjh2L5p4AiywyCJ9-TYd9gAvFDMBEPO_vuov0N-LHRXrQwfx4NvoXaT9QdMrOELlLP2_WanYdbDPVbkpXVWb--MbWKoML5im37-rhUy-8OR3newr34BTcbwaQhAj1Hb9omlD7jsO1GlT6oTbMa6TtlL0NYfDlGoMtkyaMrIGPna8vmnCzwpWjD2F3RiqetKvagYrnoF92j1Ocr61T7wVSusFDT2fYr6n-yTg6nsfJk2wAV85TvpgSl7Wohc3A5R7iVFdOC9szg80n-JYJsM2-Sln0Fxf5szDMHEPQd9T9e3BB4Nq8LXpSjz5qi7z9UI5OQ4jodgDQY5VK9I3hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e66e57720.mp4?token=rPktAjh2L5p4AiywyCJ9-TYd9gAvFDMBEPO_vuov0N-LHRXrQwfx4NvoXaT9QdMrOELlLP2_WanYdbDPVbkpXVWb--MbWKoML5im37-rhUy-8OR3newr34BTcbwaQhAj1Hb9omlD7jsO1GlT6oTbMa6TtlL0NYfDlGoMtkyaMrIGPna8vmnCzwpWjD2F3RiqetKvagYrnoF92j1Ocr61T7wVSusFDT2fYr6n-yTg6nsfJk2wAV85TvpgSl7Wohc3A5R7iVFdOC9szg80n-JYJsM2-Sln0Fxf5szDMHEPQd9T9e3BB4Nq8LXpSjz5qi7z9UI5OQ4jodgDQY5VK9I3hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شیوه جدید کلاهبرداری: گوشت بوفالو به جای گوساله و گوسفند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/alonews/141251" target="_blank">📅 08:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141250">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m0bRDGgJ1_6-1a4caEaDfnJgOsWld-cjchpsaz_Qh64K1vXw7YKotFe0o9m9iYYWhbDe5l9oyHqeDHy5FMUnx-Jx5WyOYjDPW60sqk0tJKxyJtq_hgv8FACMbrcb8jzLacFtkzYWk7CB9OEjpCCYtkQOV-t9LXXCPFJt4X-JOSacwwqp1T2eH4PZCTlOH2tXWqyMOxLtzHMZ6WWWU3Q8kr8DlTgSqmABloDs3jRVqZ_asrvCGxIXowZK-tU65-2_bxv2Yr9CYR92q_F6J9usIQIH_1FhUnyah52MFq6dx2smIt767UZHOSGlsAftjZ9aUasij9mAL3K8QxgZJ98OaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سردار نقدی:
پیروز شدیم و به پیروزی ادامه میدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/alonews/141250" target="_blank">📅 02:49 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141249">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LPVaj4QcNdWFXPM0SgyyacVKRTnbRTIsYjcLPlEXklqbryQ8-eBP9MiLmokuVFucg7ICQLb35TAHFyEKtkBO8CwDc3eoC-V5MQLSr8-YU1EhevYvUp9rpNc78H1xuola8y001Lm18NAc0SixuehoUAhA_NdErqoV8OP6lfLgstDX-A_4ucJOsK2FzSR2l9FSkAAH-YnW64zGgyvdUoyOkeUDAExGzYQc8X_QUK-mhVirYbOhSJP9JU6YyXEmy9PIhLE3bGAb0QejjcbVUwgQtk48CB2x1aVUMBwlr7LJHNL_YmFgycDLAxm_XBuYjSpwqqCSxmAkTCAq2R4oQ6KiHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خسارت شرکت ترامپ مدیا در سه ماهه دوم سال به 238 میلیون دلار رسید - در حالی که سال گذشته این رقم 20 میلیون دلار بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/141249" target="_blank">📅 02:44 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141248">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
سی ان ان: ترامپ دیگر جنگ نمیخواهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/141248" target="_blank">📅 02:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141246">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
دوستان تهرانی صدا رعدوبرق بود نگران نباشید
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/alonews/141246" target="_blank">📅 02:23 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141245">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
ان‌بی‌سی: ایران نفوذ چهره‌های تندرو را در مراکز تصمیم‌گیری، به‌ویژه در حوزه امنیت و دفاع، تقویت می‌کند.
🔴
این اقدام نشان می‌دهد تهران به جای امتیازدهی سریع، خود را برای احتمال تداوم تشدید تنش و رویارویی آماده می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/alonews/141245" target="_blank">📅 01:41 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141244">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
صدای جنگنده تو تهران شنیده میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/141244" target="_blank">📅 01:24 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141243">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kOhAaEEcxp23D99e40K6xfOVKlB8h1sXWufz3Z4H5mQUoUOKiLjCGx02iYtwWV8_VcOEU6ez7EIbU8s8xQQsYHaFlLzZ87eSxhVtE3K0FePgvMMTA-gHxKCmHlkyhj8UaDkqf4O_fXtpkUFDQVdmA9_uN_VapNEBU1cB9iPGHeF97B06QPhVGYLaUo_zitCtb_gKKvJbgB95IZK702RTAcwwkbJAH8XYxK6VQya3yEhs3_5BNQPkDcMA3K6corBMatpzz5b4eQhgNe_LtSWz0iqRNI6kqFJCxyNOBi30GXKRZCWNKkExvTCj1HmH7QujJWmkD7gsCEv9drVObgfdiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: آرزوی شهادت دارم
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/141243" target="_blank">📅 01:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141242">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zum36wI-E7VVNO8nzJJTFeYrzRpEUetW1xQtkotBJx60nnNR588n4KDQ5PewxWvCvqdCEiumDo5b9LOW13J5wiVT9x761XMrx3TN_tt41UBS8wmEJc-QF0qR9UXYctUV_Eg0tkaSsviIW4YXSmvutF8_Wn1QdfxNLdgtoHBk10S-Ns-VDvTJBOVtCUBkF4jo_BHBS0h8awMVxb5DQ5m9MCYw0FjITg5iDjON9gv9eo4SD5b61HhfjnYCXqvDZ9t-ZEPtPsCJII_5eUSL1-7OS04LjteW40_3cmqDdICQE4vnT5eD1g5DYSVxsamrkFJuHjdqJZ36eecD3th8N02g6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیویورک تایمز: نیروهای آمریکایی در طول حملات ایران به پایگاه‌های مستقر در اردن حدود 50 موشک پاتریوت را شلیک کردند. این میزان معادل حدود 200 میلیون دلار در یک روز بود، با توجه به اینکه هر موشک پاتریوت حدود 4 میلیون دلار قیمت دارد.
🔴
ایران از موشک‌هایی با قابلیت تغییر مسیر استفاده کرد تا هزینه‌های سنگینی را تحمیل کند و ذخایر محدود موشک‌های پاتریوت را کاهش دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/alonews/141242" target="_blank">📅 00:41 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141241">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gbUpgixL5Y3XSk7jIOKvRgj1yicaZQWh2UmyH8SXMiPFAqVAk7kOkO4BEBKkKhIPfPesC3oh5QQ8OLhgtP7-9k8JfORiETrZK39tLKXzC4crntH035p1fD8cFdamQqhKSJQtqns5G8RqI54yL4wOgsNiHeA907POXajdshnBmJd97wWv1M489zRoPUXOVNGnuHbSVVxPoK8K9vIHUwux-LB21OS_62DG7o7AvvdpV6UlCJTuBo0JcEdhiMqTFTE3Jp1TXwVvDTnXgDYfHiqmd8G6DIB617v5_8_FCix6nBcD5DCaOeUWKpMzXEKPE2oHCJUVuXNKpFeGShaHOH46ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هیمتی:
گرونیا بخاطر جنگه دیگه! طبیعیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/141241" target="_blank">📅 00:27 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141240">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLElwHeWTJpD0VEk95kiCS9Pqva_IrncgtEoZ0WWpLl3Z16eD7YW9ZCT04NJ4OIoLPQvPouiwYFl1lKW5QvGvzTXXPx5wfmxuXC8IbtB2VNkBRVjhD37q7Gvm3n9_p867tVRpOr9feasO0ulpc9MG1Z3291wcGqlY5VzDz_MHOHcYeAen5ONuh_xsHxZYwP3JlEs8D-v908hWUiMIXEMUSoTfhhWd-mDQza___snVMQdayv8f3RsdKxEnSt3tBXO65ZwWeVJwCyjLukZGfgOAQuOdGnHYfX7JPsYu76BIV4t606g1yqxI0cXtE4M3tzPkq1CfCKNYT7irz0yfLFFGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نفت برنت به ۸۹ دلار رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/alonews/141240" target="_blank">📅 00:25 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141239">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tf2v9bR6LlwdjCvLnpDD4fs_O2ja4wRMOqyE1xPUtFrVyHeKGt_KiUCaVTsXAstJjrMCa6bYl1eveOgIlqWUhZL3Qb3id87EE7PYsLQqyp13ZtMqP1XHBI6lqyc2ozAgwXykb_tUa2xbA26i1IXqvnHLmlaekpf73TrLgYE8pm1lZ0lzMvtQSWbxSC7RLRmq1RRSs8Dt64WwUPam7IcI-5tfUVIk-odrCNHUo_RCNYTmgFQ6TZi98Uv29Ojupq4ERgxWLFbXTUomgkNtyKPDmYTrjj3Owl-mtaT-of6uY2FrFqqBSRjj8zOB3YOYNMC5FrWZ2ZwiDnWkHbNKSLs4-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایلان ماسک :
پایگاه ماه آلفا شگفت انگیز خواهد بود. ما این پایگاه را طوری خواهیم ساخت تا هرکی بخواد بتونه به ماه بره.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/alonews/141239" target="_blank">📅 00:19 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141238">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c913fe1394.mp4?token=UqCYtqBvLmpH0bgIiKhL5yLAxiYrgcK3IL-S9_wqJQ9QjeUEpgih1lKpxan0gmb94dtBwlV8H-4uhrcZj2wReT8O38k4HubK07vnaMu3JKQqs72uZdWd-TXJscPqyhrvC801lTdk2v7mc7gVZ5shrTIuaX6k_hcw0i78GNEwqYhQM_RJi-FIh2deoUmbUop4PwQYNeN6WbuI4jlIb1q7Z0Lrs4n9ujaJJcPAvQ41lVrfNbkgfccuRtK9bdIy8GrDGLvwMtuNogWGmO63FArjezoq25CRpMpfaOx0qsUIYnpiiweILmcQIT1bbH3Z33eGR3nxdE7Wsjaki5Pi5agq_A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c913fe1394.mp4?token=UqCYtqBvLmpH0bgIiKhL5yLAxiYrgcK3IL-S9_wqJQ9QjeUEpgih1lKpxan0gmb94dtBwlV8H-4uhrcZj2wReT8O38k4HubK07vnaMu3JKQqs72uZdWd-TXJscPqyhrvC801lTdk2v7mc7gVZ5shrTIuaX6k_hcw0i78GNEwqYhQM_RJi-FIh2deoUmbUop4PwQYNeN6WbuI4jlIb1q7Z0Lrs4n9ujaJJcPAvQ41lVrfNbkgfccuRtK9bdIy8GrDGLvwMtuNogWGmO63FArjezoq25CRpMpfaOx0qsUIYnpiiweILmcQIT1bbH3Z33eGR3nxdE7Wsjaki5Pi5agq_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلمی که به تازگی از دی ماه منتشر شده، یکی از هموطنان که تیر خورده با درد فریاد میزنه...
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/141238" target="_blank">📅 00:13 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141237">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">⭕️
هشدار درباره کلاهبرداری‌های اینترنتی
🔴
کلاهبرداران اینترنتی معمولاً با ایجاد هیجان، ترس، اعتماد یا عجله تلاش می‌کنند شما را وادار به واریز پول، نصب برنامه، بازکردن فایل یا ارائه اطلاعات بانکی کنند. با رعایت نکات زیر می‌توانید از خود و خانواده‌تان محافظت…</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/alonews/141237" target="_blank">📅 00:12 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141234">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
تسنیم در یک خبر اختصاصی مدعی شد عربستان سعودی درخواستی محرمانه به حوثی ها داده تا جنگ را متوقف کنند که با رد درخواست از طرف انصارالله رو‌به‌رو شده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/alonews/141234" target="_blank">📅 00:06 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141233">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
نیروهای مسلح یمن: حملۀ امروز ما به مواضع نیروهای وابسته به سعودی با دقت بالایی انجام شد و ده‌ها کشته و زخمی به‌جا گذاشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/alonews/141233" target="_blank">📅 23:52 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141232">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
جروزالم‌پست گزارش داده سه هفته پس از آغاز طرح آزمایشی خلع سلاح حزب‌الله، ارتش لبنان وارد برخی مناطق شده و چند انبار سلاح و مهمات را کشف کرده است.
🔴
با این حال، یک مقام مسئول گفته اقدامات انجام‌شده «هنوز کافی نیست»؛ ارزیابی‌ای که نشان می‌دهد اجرای این طرح با موانع جدی و سرعتی کمتر از انتظار روبه‌روست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/141232" target="_blank">📅 23:43 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141231">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
الجزیره: ایران و آمریکا در حال تعیین «هزینه ورود احتمالی به مذاکرات» هستند/ این رسانه می‌گوید: هیچ‌یک از طرفین خواهان جنگ تمام‌عیار نیستند، اما دستیابی به صلح دشوارتر از پیروزی در جنگ است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/141231" target="_blank">📅 23:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141230">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/frar6TydaKE_zFVvi311Z4-7QusTQVDpW3Nbu0PpzaeKrmyscXoMAPR_8LaEGEbc1kdURRO3S2rWFRefZJ14EFgeCWkuLWrlBTy7fu92HDP16k-6dKrSYHEJe5i7fC6oTPIz6ABfnunZ6CNTpAuHGdrD2Fgj5Uy6RzHu5BXYCmL3OtjOfzNCUmLWNPBhgruZEF1WcYIxnt43qgP1aNmiac26PWF9EwPDRsZ-B4ZhnpxhHO6SAsdpQ4zx7XmQUIq-4TnkOcXmkkcLJroXLGe_JS8DhS6U-dk6WVPKE7muzee-SWCa52ibyTTexV4rSt1ekNEQmvqqEvENfdp2kHEYYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اوکراین تعدادی پهپاد رو به سمت روسیه فرستاده، طبق ادعای منابع روسی، تخمین زده میشه حدود ۴۰۰ پهپاد بوده
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/141230" target="_blank">📅 23:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141228">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
وزیر کشور پاکستان در جریان سفر به تهران پس از دیدار با همتای ایرانی خود اعلام کرد: پیام نخست‌وزیر و فرمانده ارتش پاکستان به رئیس جمهور ایران منتقل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/141228" target="_blank">📅 23:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141227">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MfI804gtsWoLF-0k5Vgg8t3e1R4RDWLcv2FlKWYavANilfy1yibVSJvNngnrSj4sZfHRZctOsj4wygcqWcUisE3O7hRJjgHt1awtcA-OMEYgF-98C5Dtgyd-nBteJCwdmwPBPYZgG2L7NZ3LIovhAXesNyInqXGm3rU9EDL85ond6syXw7YKHMO2695wEwD2-QlNIMr9MXXp6PnAuv-SDm9HpwW2THNzzeklFoGTmyo1guCprqjgeEZzVWt_7noYBvtrQBSnieD40nyf0SJHb0cyNexW7t0PVlkfETVS1nAiPREGo7KdVWkCvuMmV9uGCEhBzbttKD6xIAvE2sQjRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کانال ۱۴ اسرائیل: مجتبی شش تندرو جدید را برای رهبری جنگ بعدی ایران منصوب می‌کند
با وجود شایعات فزاینده درباره سلامت رهبر عالی‌رتبه مجتبی خامنه‌ای، تهران ادعا می‌کند که او شش تندرو از رژیم را برای رهبری جنگ بعدی ایران منصوب کرده است؛ پیامی نگران‌کننده برای اسرائیل و ایالات متحده مبنی بر اینکه رژیم در حال تشدید تنش‌هاست، نه عقب‌نشینی.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/141227" target="_blank">📅 23:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141226">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d7021b6ac.mp4?token=fkMzkvE-USg9eQ4J6aOd0W27RLZaJrXTWVtIycDKO2_AhXJxrxC_e27i99O7yYcAtYK6dsPCw17BjTWwOGMLizvb-vZUZX7r-SmS_ur4Zrd925Px1lviekCACQY5tDnbQslThEvnvXaegVBgbJzm6M0il9C0DHcWp3DgmnZrrihBU21MSDihDDnCYpS3vDBOa1gDyktm2JQjxvsx4Tq7R7F331IuDkAHmNQo_-EXZCXICzn0PBrFqorgjnVQXYZYoMaTZ27rLza9dC1qVlnUx2OpdBLc4zY_2_8_p_7AlnSSR5gSEsXWCoAeshcAl8S4wYwp4Ntj9JhTnfbnSJmgAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d7021b6ac.mp4?token=fkMzkvE-USg9eQ4J6aOd0W27RLZaJrXTWVtIycDKO2_AhXJxrxC_e27i99O7yYcAtYK6dsPCw17BjTWwOGMLizvb-vZUZX7r-SmS_ur4Zrd925Px1lviekCACQY5tDnbQslThEvnvXaegVBgbJzm6M0il9C0DHcWp3DgmnZrrihBU21MSDihDDnCYpS3vDBOa1gDyktm2JQjxvsx4Tq7R7F331IuDkAHmNQo_-EXZCXICzn0PBrFqorgjnVQXYZYoMaTZ27rLza9dC1qVlnUx2OpdBLc4zY_2_8_p_7AlnSSR5gSEsXWCoAeshcAl8S4wYwp4Ntj9JhTnfbnSJmgAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سردار نقدی: بعد از جنگ، جمهوری اسلامی طرفداران زیادی در دنیا پیدا کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/141226" target="_blank">📅 23:22 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141225">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UE-RzpMPTt_81eacMaOfXJEpUX_Y8MG4eXorCH2v-im6DkMCdtEfCMp7azi06EU2UBt1t6MdbXR2bVfkqMjAEYEfISpgz6pJOcUPBxqpdVNR9KweJP3yGbZqAF9Ysg22gqMLsNySHHrK1HlbGW-WIWtwEhh6ItSiFxBwPmfSf6wumR4ZMJ0Hu61yy0kfB764Xia0LFqIKoanM3u3W7oTGXEfHTAHuFniYa2UCe8yyroazKpgIUBXZg431UWFGML9UKgL-sqdzNkSEhcj6tvux-_5EVbMfDV3rt_a2lJQDp2x_9Kd0iALxAmMOt0klJmnQzWGRUKNker3MQzGY-bDsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
این وسط فیلم مسیح علینژاد و دوس پسر سیاه پوستش منتشر شده که.........
💢
مشاهده ویدیو</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/141225" target="_blank">📅 23:16 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141224">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ایشالا بعدی آقا مجتبی</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/alonews/141224" target="_blank">📅 23:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141223">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dOSnIi3zyvD2VaRxHOmzhuCJIYlyS8e1fvHnJ2-r0OuZW-pZ_RC20v57R6XsaBrBc3v4CiQeVS29JiFpLrbAT6DZNQ1MPtOxo6sazpwwI9g8mJcSSc4h11qwj_AuRBO5-UfJr_DcFCOaL9Bcq6sUDqD0Je6BVURE-NiwWqIYoXTeyyAn5RwZEsm4zgrvG_Dy1NyHlUTYzPyBhOSTBxSkSTqsTpfApLUpNC2gaJ7myM66w54AQfdPbvh06X3f8oodInzWzG05syjV0geGwKZDDShtJIETPpgeJT9N7QGeIOVxuH0a-V7Dr_E7Rso91POof5Q21mNIJOyckb6WflM5QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
کریس رونالدو با انتشار یک پست اینستاگرامی مشترک، خبر از ازدواج رسمی خود با جورجینا رودریگز داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/alonews/141223" target="_blank">📅 23:12 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141222">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eac7e6c261.mp4?token=Z5PaYM3eloKxshfAZZZ34TgUDnDv82CP5ALf0gc0rmmzRhhBN_VmIGtbrVBBdapFARd5UttOBm5n-BpI-ArX2erWMIZ8IPouW-bi3SevrEhh-7KSE76pCsYpKymuQV-8qMuiJKOVsVF8tgvPjcYaaPnamhIFUWao0cjiabStE57bFap8sKIZv8HPBlwojl2ARAtJnvMeoggxPFwLyn_USCu4EgncUTCDSNX0KDQyU1aWkXoJmxSyBCWHQiYiwMI7_K6toivKngQ_95UGH7PFsP3PoMLmIQcn2UVkETdb9VDC6EKouFOa3e5VPuCmxdhTq7t_iz58uUofz7zZIF3vsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eac7e6c261.mp4?token=Z5PaYM3eloKxshfAZZZ34TgUDnDv82CP5ALf0gc0rmmzRhhBN_VmIGtbrVBBdapFARd5UttOBm5n-BpI-ArX2erWMIZ8IPouW-bi3SevrEhh-7KSE76pCsYpKymuQV-8qMuiJKOVsVF8tgvPjcYaaPnamhIFUWao0cjiabStE57bFap8sKIZv8HPBlwojl2ARAtJnvMeoggxPFwLyn_USCu4EgncUTCDSNX0KDQyU1aWkXoJmxSyBCWHQiYiwMI7_K6toivKngQ_95UGH7PFsP3PoMLmIQcn2UVkETdb9VDC6EKouFOa3e5VPuCmxdhTq7t_iz58uUofz7zZIF3vsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
۵تا زن یه مرد همزمان تولدش رو تبریک گفتن
#حرمسرا
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/alonews/141222" target="_blank">📅 23:06 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141221">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
فاکس‌نیوز: پنتاگون خرید رهگیرهای پاتریوت و THAAD را ۱۰ برابر افزایش خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/141221" target="_blank">📅 22:58 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141220">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/le4CB0meUCOo8kkzZwO2_x00vNBeRASzic7IVRKGEVq0BUWeFBv11hzapprDJohy0nM1X-5CU3ZBHg7m5q7Hj_dvyHhYPqndgwWVrQyxqqGF4UvMJShxSj73-o_5c5PuEWvjgZQzlpAZMiUmmSmpmmIl-cUXSqwWEhVZIEhCTjCpD77ZlsqXcz3t8CCziRUkEWWZnNo70UoU3uH4rYfPoNcG3blZXfP_HjTRP9G6Rz5dzNFYb0WvN0aXOEizMC3YcS04xntbzPYxv82DerjbImbYeSOyFxN8fdsU2YiprwNsbF82-zYQbgMDsQauIyHfwZubj7sIZm9ugertI2Rj3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام مدعی شد امروز سامانه هدایت کشتی تجاری (M/V Vela Nova) با پرچم پاناما را با شلیک موشک از کار انداخته است
🔴
این کشتی قصد داشت محاصره دریایی علیه ایران را بشکند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/141220" target="_blank">📅 22:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141219">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
باراک راوید/آکسیوس: امید به توافق میان ایران و آمریکا در حال محو شدن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/141219" target="_blank">📅 22:46 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141218">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W7qgiEHQhwGMI-dBCL2LrodnzaxwQ3EXlpVcORf_kEcsi6IE8jh_0yL3OCqWq9qU5eo9qmYigbdX8-Hh7GbsclpqqV3agjzUVuX3--cfiXX4RPpxSDkE4YDYczN0BTYpL4sjB2h-j1xVczqbhWG6tOqp-MMm1wCsC_T58SBYLpKin6Xu672yEkFT-tqYxOA-Ri5Y7QRUs-_EcpbV-kqhK-y1s3P7Qrz2G3Ro81GwxSUUn8ZGrmVtALBXHqle6UBFB7COykDc7lw_IcWfcx_DCPC-CMBXONVvAP7FlzBElazB9n00EtYF2rRFkBtUDalZXgPF1iDeCpspDNP2-49cHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ادعای عجیب رحیم‌پور ازغدی: موشک‌هایی داریم که می‌توانند کره زمین را دور بزنند و هر نقطه ای از جهان را که بخواهیم بزنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/141218" target="_blank">📅 22:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141217">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
سنتکام: از زمان تشدید محاصره بنادر ایران، ۵۵ کشتی تجاری تغییر مسیر داده شده، ۳ فروند از کار افتاده و ۲ فروند بازرسی شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/alonews/141217" target="_blank">📅 22:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141216">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
اروپا با کمبود موشک‌های رهگیر پاتریوت مواجه است، زیرا اوکراین پیش از حمله زمستانی مورد انتظار روسیه، به دنبال صدها موشک است.
🔴
ذخایر ایالات متحده به دلیل جنگ ایران محدود شده است، در حالی که تولید جدید به موقع نخواهد رسید و کشورهایی مانند آلمان، لهستان، اسپانیا و یونان تمایلی به کاهش توان دفاعی خود ندارند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/141216" target="_blank">📅 22:29 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141215">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
عملیات تجارت دریایی بریتانیا:
ارتش آمریکا در ۴۸ ساعت گذشته ۴۲ ترانزیت از تنگه هرمز را تسهیل کرده است
🔴
فعالیت‌های سپاه پاسداران در تنگه هرمز طی ۴۸ ساعت گذشته ادامه داشته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/alonews/141215" target="_blank">📅 22:20 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141214">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">فرهنگ لغت جدید
دزد = تراستی
رابطه نامشروع = امر به معروف
موشک / بمب سنگرشکن = پرتابه
کمبود = ناترازی
تبعیض و پارتی‌بازی = برخورد مؤمنانه
اعتراض = اغتشاش
انتقاد = تبلیغ علیه نظام
روشنفکر = غربگرا
رفراندوم = تجمع خودی‌ها
طرفدار صلح = باسن‌لیس ترامپ
شلیک به هواپیمای مسافربری = خطای انسانی
قتل‌های زنجیره‌ای = نیروهای خودسر
اصلاح قیمت = گران‌کردن خارج از برنامه
مجازات نکردن خودی‌ها = برخورد مؤمنانه
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/alonews/141214" target="_blank">📅 22:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141213">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">⭕️
⭕️
بخاطر افزایش قیمت دلار تا 200 هزار تومان  هدیه ما به شما عزیزان به مدت 15 دقیقه کانال vip  دلار و ارز را رایگان کردیم. بعد از 15 دقیقه اگه عضو نشدید باید با پرداخت 10 میلیون تومان اشتراک بگیرید.
👇
👇
👇
https://t.me/+t2df2MwRSAIyMWM8
https://t.me/+t2df2MwRSAIyMWM8
شانس کسایی ک انلاینن
☝️</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/alonews/141213" target="_blank">📅 22:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141212">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
شبکه ۱۳ اسرائیل در خبری اعلام کرد که مشاور حقوقی کابینه اسرائیل قصد دارد علیه مشاوران نزدیک بنیامین نتانیاهو در پرونده جنجالی «قطر گیت» اعلام جرم کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/141212" target="_blank">📅 22:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141211">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WTaTvO_Aw3XRoKPCKS5KeMMCXGTkMqJp8eZ3wnu9ZLfcrSzkxnl2w8b4MygzjAoBw3mTS3FgX2JkyHmZ2JUDYouPg9YnTcQ1KdwDqg4FhkLrqn_bbn4K9QwMu14JFipiH7RKBgliAc4UdV_PmY2BRqg5vTl68XsYiKfifoIafQuTP1Tx4Xy9jqcB1_VyZ5Iz5EiQ01jY7YPsSNwrIiMlcDoUs2yo8NyGaRJFRtVcALZw0kM7ypmhMs_Bjr6pd78a5ViWX3sceqRsLogJTJihDdt5qA8wv3RheX8rwZhMjAiSDnfCdkKDMe4xnLAgYOxUBPdNKShBZ5kYnb0TA45ARg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عکس انفجار در بنی حیان، جنوب لبنان تحت کنترل ارتش اسرائیل (IDF)، که احتمالاً ناشی از عملیات تخریبی ارتش اسرائیل است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/alonews/141211" target="_blank">📅 21:53 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141210">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
شبکه ۱۲ خبری اسرائیل: گزارش‌هایی مبنی بر وقوع انفجار در منطقه سیریک، در جنوب ایران، منتشر شده است؛ احتمالاً موشک‌هایی به سمت تنگه هرمز شلیک شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/alonews/141210" target="_blank">📅 21:41 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141209">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
سخنگوی سپاه: درصورت وقوع مجدد تهدید علیه ایران، صدها هزار مایل خطوط انتقال انرژی، هزاران نیروگاه، همه سامانه‌های آمریکایی و غیر آمریکایی و حتی زیرساخت‌های جهانی متصل به اینترنت در معرض تهدید قرار دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/141209" target="_blank">📅 21:37 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141208">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
صرافی نوبیتکس دقایقی هست کلا قطعه
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/141208" target="_blank">📅 21:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141207">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qhh4sBM-o7N50WX7x9k7hds8wOa1Gq22B7hug_otFZLEi4t0iKgtQJBXWuMUL0wHyYHCm7ODDMUKAIdkLcgf74elUhH83QKcFfqVvcOveMgWfPtq8YvrE_BtoeTUKv3PV45gNIh7q9X3i3UueTiGdCkTqFrH2R1gUE_33iIAmVNh2QJecuHdjneaPKv_gCKBf2BWb_uitDb39Nwqe5UCOaLj_EKIAaFtf84XGW0M-VvWicy4NENrD3oTngcx_VWumph5MuTS2u0Lu6xrEmvPqNagPioxo0s0kZ_z-Lmn-hT0HYYMg0ra2wCFaZllL-cHpYiKsjpvL1ernkAcqUz8sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
احتمال بازگشت تردد دریایی در تنگه هرمز به حالت نرمال تا پایان سال میلادی از نگاه پلی مارکت دقیقا ۵۰ درصد است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/141207" target="_blank">📅 21:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141206">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
فوری / یمن اعلام کرد یک کشتی حامل تجهیزات نظامی عربستان سعودی را در باب المندب هدف قرار داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/141206" target="_blank">📅 21:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141205">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
باراک بتش خبرنگار i24news: گزارش‌هایی مبنی بر وقوع انفجارهایی در جنوب ایران منتشر شده است. به گفته منابعی که با سپاه پاسداران مرتبط هستند، این انفجارها ناشی از شلیک موشک‌ها به سمت تنگه هرمز بوده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/141205" target="_blank">📅 21:24 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141204">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
هم اکنون حملات سنگین به جنوب لبنان در جریان است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/141204" target="_blank">📅 21:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141203">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57ef63b346.mp4?token=fwGj9Ul1Qos-JJHUZR_znVb4Npogz4tVAoWOZ8KwqHSgxdDaPNyF6BJLxhIH9FjooLoxWKg73ylUm1DmlOZWSk7bk-U4fn-Nz11obPsM9xAkn03H3buGIDWNR-LDtxXDwzxLPlBUy8wkb7z2l4sMugx_0Ytp03YdUjJYyoSx47yKqn0AJm4vHEPHf_dD7kHXRtO94uEem_jj9B0JW-YdhhScGceCOEreYPTp-rcjcWsafdVd13x0L2OZAh9w8LgTxRpUi98GYzYUwdqBHGK22tRK7KuGK7Uuwhm5hGb7CRLx25iFMEccJK__e4ewhPDCuHAmU8zBL4PXo-gekOryGmcmCXgmsKDp1aXxMx4XHJ7SxFOIrEeLO0q53t7vb9UwHKC50eufxI2vVetYkfKTQCQzwSg_9giofryt8kfRdKSYj-H8J0EdngK8IX_tmXBP-gQdds4hDUZACrMB9ECYgAXsJTSjqACCrK2tbQ-drCu1dkL8tgGapx6Kop0CK9V0S6Z8-ne4Y5M0RCgal8PNVXoea7FG0ZQLv9lgKBeFaQGizyycfGzoIkiVVKHG2xqMmrkkpRefSNRQP6rLLaP46hTggmSTbvJqSym6GSKhwvm6vHTtxLG7kBWS26p7fQ4encl6dII-_43QfC-YDi_BUCRDSAIN-lg1pMTBUT1b_QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57ef63b346.mp4?token=fwGj9Ul1Qos-JJHUZR_znVb4Npogz4tVAoWOZ8KwqHSgxdDaPNyF6BJLxhIH9FjooLoxWKg73ylUm1DmlOZWSk7bk-U4fn-Nz11obPsM9xAkn03H3buGIDWNR-LDtxXDwzxLPlBUy8wkb7z2l4sMugx_0Ytp03YdUjJYyoSx47yKqn0AJm4vHEPHf_dD7kHXRtO94uEem_jj9B0JW-YdhhScGceCOEreYPTp-rcjcWsafdVd13x0L2OZAh9w8LgTxRpUi98GYzYUwdqBHGK22tRK7KuGK7Uuwhm5hGb7CRLx25iFMEccJK__e4ewhPDCuHAmU8zBL4PXo-gekOryGmcmCXgmsKDp1aXxMx4XHJ7SxFOIrEeLO0q53t7vb9UwHKC50eufxI2vVetYkfKTQCQzwSg_9giofryt8kfRdKSYj-H8J0EdngK8IX_tmXBP-gQdds4hDUZACrMB9ECYgAXsJTSjqACCrK2tbQ-drCu1dkL8tgGapx6Kop0CK9V0S6Z8-ne4Y5M0RCgal8PNVXoea7FG0ZQLv9lgKBeFaQGizyycfGzoIkiVVKHG2xqMmrkkpRefSNRQP6rLLaP46hTggmSTbvJqSym6GSKhwvm6vHTtxLG7kBWS26p7fQ4encl6dII-_43QfC-YDi_BUCRDSAIN-lg1pMTBUT1b_QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سردار محبی
:
سرعت افول آمریکا بسیار زیاد است
🔴
آمریکا در همه اهداف خود، از جابجایی نظام تا چپاول ثروت‌ها شکست خورد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/141203" target="_blank">📅 21:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141202">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
پرواز های فرودگاه هانوفر آلمان به علت مشاهده پهپاد های ناشناس بر فراز این فرودگاه به طور موقت لغو شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/alonews/141202" target="_blank">📅 21:11 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141201">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IbPKNbwbm-FOo8z4EApTWI9aOl_OWNcN8ZtB6-ESZsOjxfwPylNq4isnayY8H07OQ_JkMqDvHjWX3HmvF4nIAX25GPIvmg7OH4phIqSWwB6-w9D_lip2Qq_XeqaYTqeL4Fo4MuInMRo9tJ65vOnuwLrkZ15zl8fpTrqGzghwCrr9xde3icdHxJuStV_sEkiik2X5tpbDvydwtunxj1dxKp9B3sSNpd_d3hpWdEsKkTZJWow7x2NMyw5GbDHmV7bu5aDVAbAQ4s2uuLBsEnXpr7MchBY15iW4tbjK6utFqP1avbtLc3nMW4MzIS1qPVXJKjq-wlpAn5IW5t3F0xnLGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / خبرنگار الجزیره: یک موشک ضد کشتی از شهر سیریک ایران شلیک شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/141201" target="_blank">📅 21:02 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141200">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de77474c70.mp4?token=LBhYYmE17lEfp5vGkc5czudU6kUO_wubS4g8uVCXBpkrOreHyGp0NLwBg495GvwhhKv1MMxYrMYVBVBlfen1vlPi94ucoWxhvDhytwauKPNsC3zKATMuhFlOXLrEOwV_cjJB9CxiowaDLQ2S_FB8mI1DcjTdqKpKKmEID15g7ow3b5JQKWDiZ481cKXsJFK_HL95hZovNncHslE4bZLkEa6J7dlpJ7DAlz8aGthzFnVcp9O1UwaaFwCiNAA2puIwlg8mL0jTKhLpXJZT1BDtZB0uBz4A73SyvQ69IPUL-ZXl9hJqoCU-2S8PwyzokqxAOSsf1Z6XgMXA5qUhCxfkkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de77474c70.mp4?token=LBhYYmE17lEfp5vGkc5czudU6kUO_wubS4g8uVCXBpkrOreHyGp0NLwBg495GvwhhKv1MMxYrMYVBVBlfen1vlPi94ucoWxhvDhytwauKPNsC3zKATMuhFlOXLrEOwV_cjJB9CxiowaDLQ2S_FB8mI1DcjTdqKpKKmEID15g7ow3b5JQKWDiZ481cKXsJFK_HL95hZovNncHslE4bZLkEa6J7dlpJ7DAlz8aGthzFnVcp9O1UwaaFwCiNAA2puIwlg8mL0jTKhLpXJZT1BDtZB0uBz4A73SyvQ69IPUL-ZXl9hJqoCU-2S8PwyzokqxAOSsf1Z6XgMXA5qUhCxfkkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش‌سوزی گسترده در درپالایشگاه نفت الزاویه در پی حمله پهپادی ناشناس!
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/141200" target="_blank">📅 21:02 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141199">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
هم اکنون/ دیدار وزیر کشور پاکستان با پزشکیان
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/alonews/141199" target="_blank">📅 21:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141198">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea51341f01.mp4?token=Fdt5-HPBsB8cg9D1WzTDeyaX1uP89SJ5OsrpiTt5zC8mq6SLrVo2KEziLufOCvgeRQNoVwq-KQV7L53fyZDixx7j4p8z-ySbfIKJw3ejO_GeVChX_4pGaJ4vS98FFI5aNlxxthqzax8FcjHEgdvAZy-X73G-xu1UczWeGCILggUAFOtd2KWLqOW7pOFLeADD3rmb-dYMyBPrOzlrslqvlarG17YtyCDCb0pG-O9A19JJAwhHpgkNFIGhpKUcaWg5-NcjHw0eRhX8tMJrl1tz6uO44D_3OYPMGqTjgnTCUb--w5HI2z-DPoSIWgLSYb9R3cMoJJUp5sUCW6xDREjp9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea51341f01.mp4?token=Fdt5-HPBsB8cg9D1WzTDeyaX1uP89SJ5OsrpiTt5zC8mq6SLrVo2KEziLufOCvgeRQNoVwq-KQV7L53fyZDixx7j4p8z-ySbfIKJw3ejO_GeVChX_4pGaJ4vS98FFI5aNlxxthqzax8FcjHEgdvAZy-X73G-xu1UczWeGCILggUAFOtd2KWLqOW7pOFLeADD3rmb-dYMyBPrOzlrslqvlarG17YtyCDCb0pG-O9A19JJAwhHpgkNFIGhpKUcaWg5-NcjHw0eRhX8tMJrl1tz6uO44D_3OYPMGqTjgnTCUb--w5HI2z-DPoSIWgLSYb9R3cMoJJUp5sUCW6xDREjp9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه خلع سلاح گروگانیگر خیابان ولیعصر توسط پلیس نوپو
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/141198" target="_blank">📅 20:59 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141197">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHF28Kmjs6RcL0ynuNiFToB-65R2rxFbDKZOtmBGOGAxTuMoumW972W7ldZxNz_6gbkXRCrMW9RiSEtLd_Aq1Lm4KN0xyvsVUlCjAB8I3YQ1Nkg-H2bcgmvettfm4Yr7X3BD1dAL7aB4QXyhxiid1CpKkFHJ1G8qWYHtv6fwuxDpJO_cuOpljqyZUVoixSrSUw9FFvBxvDB_eo61oEfEepdEViGlT9QjE8t67Fyw34Vh_9JDQcvMAUWAOtChx5XhxbeYt67QOPCqiYtu5FuSM1_hfhXHRCF0yoyI1k2blj-UwpCTrzem8xJe4VdtpBB8H5Wok16t5yrGaYukcFB4tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
میا خلیفه بازیگر محبوب هالیوود: تا آخر پشتیبان فلسطین هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/alonews/141197" target="_blank">📅 20:57 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141196">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">بچه‌ها این گردونه صراف رو چک کنید، من الان شانسی زدم ۵ دلار بهم داد
😐
😂
انگار اصلاً پوچ نداره و به همه یه چیزی میده.
برید بچرخونید ببینید شانس شما چیه
👇
https://r.saraf.app/s/agrd248</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/141196" target="_blank">📅 20:52 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141195">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
فوری / وقوع دو انفجار پیاپی در مأرب یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/141195" target="_blank">📅 20:50 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141194">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
محسن رضایی: تا وقتی تو غزه و لبنان آتش بس نشه ، تنگه تنگ میمونه
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/alonews/141194" target="_blank">📅 20:50 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141193">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
کوهن، رئیس سابق موساد : مأمورهای موساد برای اینکه بهتر بفهمن تأسیسات هسته‌ای فردو چطوریه
🔴
چندین بار از این سایت بازدید یا اونو بررسی کرده بودند
🔴
اینکه آمریکا فردو رو بمباران کرد، تحقق همه آرزوهای من بود
🔴
اورانیوم ۶۰ درصد غنی‌شده ایران هم هنوز با ساخت بمب هسته‌ای فاصله داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/alonews/141193" target="_blank">📅 20:42 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141192">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
ترامپ: سلاح و جنگنده به اروپا می‌فروشیم و آن‌ها در ارسال به اوکراین آزادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/141192" target="_blank">📅 20:38 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141191">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
ترامپ: ما بر پول ایران کنترل داریم و کنترل کاملی بر آن اعمال می کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/alonews/141191" target="_blank">📅 20:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141190">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
میدل ایست آی: ترکیه معتقد است که گزارش اطلاعاتی اسرائیل در مورد طرح ترور ترامپ توسط ایران، یک عملیات فریب برای نابودی مذاکرات بوده
🔴
تل‌آویو گفته بود تهران با دوش پرتاب می‌خواسته هواپیمای ترامپ را در ترکیه هدف قرار دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/141190" target="_blank">📅 20:20 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141189">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
رسایی: چونکه نمیدانیم اسرائیل کِی حمله میکند مجبوریم جلسات مجلس را مجازی کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/141189" target="_blank">📅 20:12 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141188">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13f811c57f.mp4?token=toZhuSC2dOPUhvIZUTXhdtMq9J6zgz30oBcJHWRQwgZ5bc5A-J3N4rACYvwXg_bEsWECfPDL1Jg1x7P11lWxW4iQYfO5EmB5fzF_faeuoQKTHp4T6neIYhmYUzn8oyQ3oxa7ZeuF2SPYBXliv4p-b-Sr89Xm_0NzRgVPkEJxNgoeO7gtDzbeY70nAYjuaoNEdABh_SMqY-cYM6UAFojYzLjxxxU7AlftLacWiI7Uub3pf2hLvJ_ejzEXhw9Hc-9tsQrguhLDbVl3ZOwTW6D4Jf3AfvT_cNYjaiakAb1nQO2M0tC6Uona0rEWaWRZfjWOCFvRma8JSnVOVMrGiycX9qqkSKhFxfiqrpvFSKlfTw8rQ-F49cSArx8PSScMCytVpfo-jQ6Gm1IH3VL_CGu3DjwNnOUMWgIYLet6KPmyk2fnYZ4c65ODU0D7PntQg-c8WdnDrEvigWci-o7ggPkvJV3LkOVAFQfd2bZw2_bSNpS98wbAQgSaDaLkunA9-aUUk1mG96oU5gDjmfKHqQ6KsPykgFFrcsEgWio3AG7fLesuDDiAPq8nLK5Ju2phnEe_w5Ak6r1IznG1NKMzTWlCzIlJn_XCcw_KJdUv7pNJbOOzaj2PwO9N14rJCZyZEjGUAaBqCZZ1EYv_LIsUZESS87GdzPfKwzaiGtIESLw42xI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13f811c57f.mp4?token=toZhuSC2dOPUhvIZUTXhdtMq9J6zgz30oBcJHWRQwgZ5bc5A-J3N4rACYvwXg_bEsWECfPDL1Jg1x7P11lWxW4iQYfO5EmB5fzF_faeuoQKTHp4T6neIYhmYUzn8oyQ3oxa7ZeuF2SPYBXliv4p-b-Sr89Xm_0NzRgVPkEJxNgoeO7gtDzbeY70nAYjuaoNEdABh_SMqY-cYM6UAFojYzLjxxxU7AlftLacWiI7Uub3pf2hLvJ_ejzEXhw9Hc-9tsQrguhLDbVl3ZOwTW6D4Jf3AfvT_cNYjaiakAb1nQO2M0tC6Uona0rEWaWRZfjWOCFvRma8JSnVOVMrGiycX9qqkSKhFxfiqrpvFSKlfTw8rQ-F49cSArx8PSScMCytVpfo-jQ6Gm1IH3VL_CGu3DjwNnOUMWgIYLet6KPmyk2fnYZ4c65ODU0D7PntQg-c8WdnDrEvigWci-o7ggPkvJV3LkOVAFQfd2bZw2_bSNpS98wbAQgSaDaLkunA9-aUUk1mG96oU5gDjmfKHqQ6KsPykgFFrcsEgWio3AG7fLesuDDiAPq8nLK5Ju2phnEe_w5Ak6r1IznG1NKMzTWlCzIlJn_XCcw_KJdUv7pNJbOOzaj2PwO9N14rJCZyZEjGUAaBqCZZ1EYv_LIsUZESS87GdzPfKwzaiGtIESLw42xI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرواز بالگرد آپاچی ۶۴ آمریکایی در نزدیکی قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/141188" target="_blank">📅 20:07 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141187">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
وزیر انرژی آمریکا: روز یکشنبه ۲۰ میلیون بشکه نفت از خلیج فارس خارج شد که بالاتر از میانگین قبل از شروع درگیری است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/141187" target="_blank">📅 20:03 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141186">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0160411b7b.mp4?token=S20LLkf527VZvISJWcq0D5JGoWcDlB_1J8vRxeeYsDcGv7erMwScPe3aQhrK3zEDVEIBWXWOkDkbBS7eLX5c3QmySHYtC4IyrNzFU7sLuopHVjj3ur1yrxCE6vAFsvgYpkG2syihYkzPR_F9TvwLEr6nVJEVU5oLJ3wtCYQHpROaKMT67QW-ub6Ia4WKXZFAOCHsJKPN5SpXYY8U5StNaRYPcWFdu94zVdQUXesfpRYM8Ssdx1mghUBH1_PAhscHHpo4BG5l8134qDUS6Ib61XCthDKEbZoD7MdT4tOIDD91J1C_Px2MmNCy3J1Y_b6sJ4jo-EOy8onXtIVIw_8mbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0160411b7b.mp4?token=S20LLkf527VZvISJWcq0D5JGoWcDlB_1J8vRxeeYsDcGv7erMwScPe3aQhrK3zEDVEIBWXWOkDkbBS7eLX5c3QmySHYtC4IyrNzFU7sLuopHVjj3ur1yrxCE6vAFsvgYpkG2syihYkzPR_F9TvwLEr6nVJEVU5oLJ3wtCYQHpROaKMT67QW-ub6Ia4WKXZFAOCHsJKPN5SpXYY8U5StNaRYPcWFdu94zVdQUXesfpRYM8Ssdx1mghUBH1_PAhscHHpo4BG5l8134qDUS6Ib61XCthDKEbZoD7MdT4tOIDD91J1C_Px2MmNCy3J1Y_b6sJ4jo-EOy8onXtIVIw_8mbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بعد اعتراض مردم فوجیساوا ژاپن به ساخت مسجد تو این شهر،دولت ژاپن اعلام کرد اسلام تو ژاپن جایی نداره
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/141186" target="_blank">📅 19:59 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141185">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
سی‌ان‌ان: کاهش ذخایر موشک‌های رهگیر آمریکا، نگرانی تازه کشورهای عربی خلیج فارس شده است؛ آنها نگران‌اند در صورت تشدید جنگ با ایران، توان پدافندی آمریکا برای مقابله با حملات احتمالی کاهش یابد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/alonews/141185" target="_blank">📅 19:55 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141184">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
اسرائیل و ونزوئلا روابط کنسولی خود را از سر گرفتند
🔴
اسرائیل و ونزوئلا در سال ۲۰۰۹ میلادی روابط دیپلماتیک خود را قطع کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/141184" target="_blank">📅 19:51 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141183">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
وزارت دفاع اوکراین تأیید کرد بیش از یک میلیارد دلار مطالبات معوق مربوط به تسلیحات و تجهیزاتی دارد که برخلاف برنامه، در موعد مقرر به خطوط مقدم تحویل داده نشده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/141183" target="_blank">📅 19:47 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141182">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
سفارت ایران در ترکیه: هیچ نگرانی بابت توافق مکه که علیه ایران باشد، نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/alonews/141182" target="_blank">📅 19:43 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141181">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rkTYJHkWsq6H2bFxkOvVhwbp8MWvA4rWYS_5nBC_3C0Zse12Yynia9vLNlYhku66t25EQ6ZKVSpPT9b0YqGvrhthfbq_pmjfN599uISiIvkrYs1I2wpRu33Mq2lEidswnrhm4sd-0wF6l6Xk_GcXOGdC1Qvr3FhzhwpE0m6j5UI7PqopIxHIxBUkf87IztSWnFydw4WmNoPOIBGEFrBGPgMMT_eJnjBD6fyuIPog9Cekq-nUIyGO_il1iismh7gWrZF-8UieKfRyQgiI6K2I7DhJq0pRV_Yd4_08xEOpBOM402z-8DFamApvQ2n8DWq0NZ8rgxczn0cAtgQsvLJ6YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اوکراین گزارش حملات موشکی خود را متوقف می کند زیرا حملات روسیه بر دفاع ها غلبه کرده است
🔴
اوکراین انتشار داده‌های موشک‌های وارده روسیه را متوقف کرده است زیرا پدافند هوایی این کشور تحت حملات تشدید شده در میان ذخایر رهگیر خالی شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/141181" target="_blank">📅 19:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141180">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I25fzE8_l2K_SPAIJ5E0ug472kklrmL1GVmo4Pgfm1B5MIJYqV--z6gZNrrGyvPxilm3mo7e08UHdqIdZX2AMpeGPA8GE_GE1QrwEnxu415fh5VNLQPfshRSP7t7BPdLcsnvsNjWgd8HY4Q5XmpOJtCFhkvQlRCku2zGstxWxCF2pUkCsL-dpDtmOhz3U3IjuJWCPhl5_mCHpuzOBIXrdihObVNDFefct8p--yD-7yQEDYeNPDJ8D87YHQ8himO1DKTpzh0uXACgIy9Goh1OCC1c3DVyhReWgNSCCNcm0NJpjfoYEvWBjvAEjiLv453Vm5onipD0tGTL1wxd7kSGzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مخبر: تنگه هرمز باز نخواهد شد تا شرایط ایران محقق شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/141180" target="_blank">📅 19:32 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141179">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
محسن رضایی دبیر شورای امنیت ملی:
شرط بازگشایی تنگه هرمز، پایان جنگ و آزادسازی پول‌های ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/141179" target="_blank">📅 19:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141178">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IJI7LI-sBid1vnYe5v4T2z81TweFeMlB90YmgGiUXc_LGSEynpLonat4pVa_VaObg4mJ9NurZ9AnsAdbZI3Kg8k0_n-mINKDX77yVqBSYNkb71_b6X5joDOhrydsEcryfWVrgyNP-9Fe7PG8VzEFm9UTpQeTDHA2RX9ei2eJmXDRz7I4GJxv-s1hLCD9Lpb3_zwLliGmMp5TVZkga6QmtnesgPc7172-HuQvo-n80RqTQO5RAUeMY264ECsObQ3N-6Gpez4JFijPDevpST3-8WSxIoG61fn_NU3ugUuC7lxi7Bg9txdXf_0u2gxEDVLTU-tZwpWIvCbS3WxsmP29Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مجری: شما از آینده هوش مصنوعی نمی ترسید؟
🔴
پوتین: من تا حالا تو زندگیم از چیزی نترسیدم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/141178" target="_blank">📅 19:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141177">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e386169ba.mp4?token=OmwX6l5TyoFL_rhP1nc5VKWxnSA3xhZv19E3CzhVXUaKGOu8vp8n2d0fGMkuAVj9NfbHzZDAuHD16Cy6T-j9N5-5BLrGYfgJYUIYc5NLPfIe6dW2T0HbKq8Mh5UxoihnyNcH6fdkof2_zZcmUPvP8WJucEYtVqZ8b9Nj5Ad8XMeuV6vUy6jaELreu9uJnxUUaCZe3qcplg94Ku91CqFH-6wDbW3WooJpE17Fd_8bLLjhsCDH6pYwpS9LX__OWSEhIhCDnH77s8wWK-22LoM3WX5ZRee93P8Xpz3lrgoWcygzHvKNm0dCeHWayzCOIJ99D2tqZuqgwOQNA9SfZYCLWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e386169ba.mp4?token=OmwX6l5TyoFL_rhP1nc5VKWxnSA3xhZv19E3CzhVXUaKGOu8vp8n2d0fGMkuAVj9NfbHzZDAuHD16Cy6T-j9N5-5BLrGYfgJYUIYc5NLPfIe6dW2T0HbKq8Mh5UxoihnyNcH6fdkof2_zZcmUPvP8WJucEYtVqZ8b9Nj5Ad8XMeuV6vUy6jaELreu9uJnxUUaCZe3qcplg94Ku91CqFH-6wDbW3WooJpE17Fd_8bLLjhsCDH6pYwpS9LX__OWSEhIhCDnH77s8wWK-22LoM3WX5ZRee93P8Xpz3lrgoWcygzHvKNm0dCeHWayzCOIJ99D2tqZuqgwOQNA9SfZYCLWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو : این منطقه جولانه پرچم اسرائیل اینجا به اهتزاز دراومده و همین‌جا هم باقی می‌مونه، چون این سرزمین ماست
🔴
امروز این سرزمین متعلق به ماست، دوباره به ما برگشته و همیشه متعلق به ما خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/141177" target="_blank">📅 19:03 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141176">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a895c6e9a3.mp4?token=mSVi3vaaTeATJajSUuD6eYw14MYC0JDB8-GZFKxlydNgbVaggFl4e0WRty7IyCxOrdA7juQihr55gfgfThT866RqM0qMTsoimhqnEC4-80WhrDaUj9PJM7YuNIIo5HbfaW2z63W9cBk6n_Lj5unr2efwG-C1zuaswPkEyb2Zr1gu_XgYvfbXR7CntADrisA8KXdeOuhnT9eI8C67-sVF9l2FO5x1s-VcsNe8GJ46mjUFFPE5oy7wfkWY9xq5CvUJYDrtlJXH6nn9WR9XP0GChYMQ1fY5jRPMgrVyGmKrz5iZYSQ3MOTvvu6mehvfq_IXfaBa-YFjPMLIRHjEd9U0Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a895c6e9a3.mp4?token=mSVi3vaaTeATJajSUuD6eYw14MYC0JDB8-GZFKxlydNgbVaggFl4e0WRty7IyCxOrdA7juQihr55gfgfThT866RqM0qMTsoimhqnEC4-80WhrDaUj9PJM7YuNIIo5HbfaW2z63W9cBk6n_Lj5unr2efwG-C1zuaswPkEyb2Zr1gu_XgYvfbXR7CntADrisA8KXdeOuhnT9eI8C67-sVF9l2FO5x1s-VcsNe8GJ46mjUFFPE5oy7wfkWY9xq5CvUJYDrtlJXH6nn9WR9XP0GChYMQ1fY5jRPMgrVyGmKrz5iZYSQ3MOTvvu6mehvfq_IXfaBa-YFjPMLIRHjEd9U0Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت مردم پاکستان بعد از توافق مکه با عربستان و ترکیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/alonews/141176" target="_blank">📅 18:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141175">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
سوریه اعلام کرد آژانس بین‌المللی انرژی اتمی به‌زودی از دستیابی به «پیشرفت قابل توجه» در پرونده هسته‌ای این کشور خبر خواهد داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/141175" target="_blank">📅 18:38 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141174">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
شورشیان نیروهای سریع‌العملیات (RSF) که از امارات متحده عربی حمایت می‌شوند، در کنار جناح «مجلس ملی سودان» (SPLM-N) به رهبری عبدالعزیز الحلو، شهر مرزی قیسان در منطقه نیل آبی سودان، نزدیک مرز اتیوپی را تصرف کردند.
🔴
نیروهای RSF و SPLM از خاک اتیوپی به عنوان پایگاهی برای عملیات استفاده کردند که به آن‌ها اجازه داد به صورت غافلگیرانه از مرز عبور کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/alonews/141174" target="_blank">📅 18:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141173">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
تسنیم: درگیری خونین در ناو «آبراهام لینکلن» ۷ کشته برجا گذاشت؛ این درگیری پس از اعتراض خدمه به شرایط نامناسب خدمت، کمبود غذا و مشکلات بهداشتی ناو رخ داده است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/alonews/141173" target="_blank">📅 18:29 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141172">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
فوری/ترامپ: ایالات متحده می‌تواند به زودی با قدرت بسیار زیاد به ایران حمله کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/141172" target="_blank">📅 18:23 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141171">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P69WvPG7KK30U828--krUSm2YCkXMD1Ac8jREYslmIZROZcgvKiQOXXJjX6q-0nSneaH19nzpTMKwWHeRTmf7npMmZWX26sgLLvaQ5U6xJg5zkQaw8gjC2Uwr0Mwb27yx2C5nUj4lNsKJ9gLxg6Eb6t0unCQpcQmvHFH3bqSPYVAXinYQyAMpt30RKJNOgG-DLeQHRTWOC_HxZ6OpJfZZHUOQLV-c7viAQdeZKm6QZfaPDWlIo64XdBQ7QUR3tBRkSTstTgok1ecWmXCYb0t5yAwckC0QGfSb0riumb5Ho4fisA0WxpVn6SszLrTFeHyZ41J0jUbEMrMsIyagRiqdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس جمهور لهستان: صبح بخیر ایران عزیز!
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/alonews/141171" target="_blank">📅 18:22 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141170">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
فوری/ترامپ:
ایالات متحده می‌تواند به زودی با قدرت بسیار زیاد به ایران حمله کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/141170" target="_blank">📅 18:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141169">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
وزیر کشور پاکستان با عراقچی دیدار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/alonews/141169" target="_blank">📅 18:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141168">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cn7GANRcmWSOfkoTZkvs_Drm9bvLWD5Ap4fJ2hLNWtVQCURTWHswyd9RVHssX4hnWHrUUmIxu4yRP1M-0yxxYfB8XEtSgtWtTtxGylXsQxQFgPCp6ERDrrFbsQmpS6NhzMM91iTKathO0zbx4wvnprZWu9l4rJhHXiD4uYDyFypJD0PYOj75bRiwjjCGCtu9nwkIhESRgKdOZpTSCDUXOmPjlOCynH7G4l7nQO5LynwqOBzj2vnUKaKieDaBy6QjyH2jrivLwmrsfwd7woGixE0LTq_HI-LnYW2Uexdne8jvvsoZW0TmpM0KTvAWAZeU5DX1SKlMvghSlO7ptlybrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
می‌دونی طلا و دلارتو کی بفروشی، کی بخری؟
می‌دونی چطور ۱ میلیون نفر پارسال ۲ برابر تورم سود کردن؟
📈
با اکوتراست
✅
همین الان ثبت‌نام کن، تست شخصیت مالی رایگان بده، تا دقیق بهت بگیم توی چه بازاری، چه زمانی باید ورود کنی که بیشترین سود رو بگیری
💰
⚠️
فقط ۵۰۰ نفر ظرفیت داریم!
👇
سریع کلیک کن و تست شخصی رو بده تا بهت بگم چی بخری و کی بخری
👇
https://storage.ecotrust.ir/marketing/landing/index.html?utm_source=ArshiaYar&utm_medium=Telegram&utm_campaign=sinaps-marketinglanding-0505&utm_content=Telegram
Alo</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/alonews/141168" target="_blank">📅 18:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141167">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: می‌گویند «آقا بروید صحبت کنید»، اما طرف مقابل با شمشیر آخته آمده؛ نیامده که بگوید صلح کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/alonews/141167" target="_blank">📅 18:01 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141166">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
ترامپ:
ما از رویکرد ایران در مذاکرات راضی نیستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/alonews/141166" target="_blank">📅 17:57 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141165">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
دلار 187000
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/141165" target="_blank">📅 17:46 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141164">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bon_6RgYSQlViHoGZse9KQO7PTq1ML9LIE0MOaFkTRZZT4IJ1mxbfRJU3ybNGGkyvUTkbyzD_iHJV4tgYovGtqrMdufNvhj7sCciLhN919UjMpWduXchysBz2_sDwMld4h_j9ZnuiKh7Img2YOdITUefNyZP25b_CzuNoakRi60TucI7EJF3vkUJFI5Oc-g3cXRYPo1CyGaWWLL_cW2vb9jUyM7ijK5uWkOClnFrtv_WuIZ3Hbi0bzsMJrLyAVebVz-FynWYv959AFb1E5sakXgwnyHhJ_gqlTlSlL6WDnBNSIC3CiDrqWY1Bwrpwe9BIxASe6aaChYcX2nTkQifGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زاکانی: وقتی بیت رو زدن، خودم رو با موتور رسوندم اونجا ببینم آقا چیشده
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/141164" target="_blank">📅 17:32 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141163">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9676b05e8a.mp4?token=qMhbn2Y3hGUsiHug6EwIocbvyyfjI2mFP-lBy7OEIHWLtRT-ECbOAMppUkqMHZXXpQHQe-uB_2OZBTze_TWYjEqEpasZHlTeRMgQcToNTTgmMGFze9zsvTt7CwOc8nQtNVeG8RmNol_EkUpd834RkdQfORtcPRTzYr_LNpP0vwc9Pvimf7ycrcOE9A45osdIMj-xO4tZsrgQIA9IE_RxAUKOlC9wHIY-QvfJvOJGws-eMmR4o1g_UfUtApRNkgKFz8nrUYYvgK_HAfeypjVHV_kZ2qw3TPHYJ8nY116gV5SQymjg1pjTkp7-L9GeXl78qCXpvHWoPieGRXUap0qSpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9676b05e8a.mp4?token=qMhbn2Y3hGUsiHug6EwIocbvyyfjI2mFP-lBy7OEIHWLtRT-ECbOAMppUkqMHZXXpQHQe-uB_2OZBTze_TWYjEqEpasZHlTeRMgQcToNTTgmMGFze9zsvTt7CwOc8nQtNVeG8RmNol_EkUpd834RkdQfORtcPRTzYr_LNpP0vwc9Pvimf7ycrcOE9A45osdIMj-xO4tZsrgQIA9IE_RxAUKOlC9wHIY-QvfJvOJGws-eMmR4o1g_UfUtApRNkgKFz8nrUYYvgK_HAfeypjVHV_kZ2qw3TPHYJ8nY116gV5SQymjg1pjTkp7-L9GeXl78qCXpvHWoPieGRXUap0qSpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قیمت خونه و برج توی فرشته تهران بعد از جنگ، متری 2 میلیارد تومن!!!!
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/alonews/141163" target="_blank">📅 17:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141162">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18584c6055.mp4?token=JrioQ81WuOOdlFalWYOUc94XlHWDpjAE85Jf80cpA8D1ahgB2_mH3sOvCa2FGYMqddRNysd7ZmBm2b0gQ3bR0EEiRbjfvC4JhXDI_1F5WTRvXglH2jVcT-T9TcwShYjia7yWF-udmB2H2Awj4PR9HoEerpoJgvByVvbEI3QpNQ0CE-FItfqKwfpbH59bpQrWlionQesZbuud0xwWuCn9AIWSy_kANfzJbNvfy1960jfHqt8c8Ms9x1o8kStVFwdCkCeF_M9vPcs4eV6tEOKEVyP1SqwKZ4WsjfE1IlEsHLxI8JqLa9-tJuUmIYbjZj_k4-nh16ydzZDiBSP6VGHkhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18584c6055.mp4?token=JrioQ81WuOOdlFalWYOUc94XlHWDpjAE85Jf80cpA8D1ahgB2_mH3sOvCa2FGYMqddRNysd7ZmBm2b0gQ3bR0EEiRbjfvC4JhXDI_1F5WTRvXglH2jVcT-T9TcwShYjia7yWF-udmB2H2Awj4PR9HoEerpoJgvByVvbEI3QpNQ0CE-FItfqKwfpbH59bpQrWlionQesZbuud0xwWuCn9AIWSy_kANfzJbNvfy1960jfHqt8c8Ms9x1o8kStVFwdCkCeF_M9vPcs4eV6tEOKEVyP1SqwKZ4WsjfE1IlEsHLxI8JqLa9-tJuUmIYbjZj_k4-nh16ydzZDiBSP6VGHkhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
محمد دادکان: چند دهه حکومت کردید و نتونستید کاری کنید خب برید دیگه مگه ارث ننه باباتونه
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/alonews/141162" target="_blank">📅 17:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141161">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
ارتش اسرائیل (IDF):
کمی پیش، نیروهای IDF یک تک‌تیرانداز از سازمان تروریستی حماس که در منطقه خط زرد، جایی که نیروهای IDF در نوار غزه شمالی عملیات انجام می‌دهند، تهدیدی فوری ایجاد کرده بود، شناسایی کردند. بلافاصله پس از شناسایی، نیروهای IDF برای حذف این تهدید به سمت تروریست شلیک کردند. اصابت شناسایی شد. نیروهای IDF تحت فرماندهی جنوبی طبق توافق در منطقه مستقر هستند و برای حذف هرگونه تهدید فوری به عملیات خود ادامه خواهند داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/alonews/141161" target="_blank">📅 16:55 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141160">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCDbw4movXObn6jUubtXP0cdgg-PguyPofPiKbcIaPXoEIMPveWKxX3Cfa78FN3tg-HtNA4-A0OSpmsKUjJ5ZK8ArsnX2EvJ-XfGXDpSyWP6p9-H6LYSRYxTeNkF-5glSsmh_Jny0kdieXErWOOpssyQ2-AlWyVCaxNWCDALUPeWHkiJh1kAR_kexzYIpI-6rZIlMJ0bpt2oEHmgEWu3vGY0nfgjlwqReKrKte1xN2w2uSJsqcq3ljiZLJ8alN_ZBY7J904ZnWbCQKJLnp7KZP_FPk_H3aS0KVfAw4As2PfZUGuZzc1ID8Z_5MazAnrauG-s_0fJRJiB2tldd5tUPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علم الهدی: افرادی که می‌گویند جنگ را تمام کنید، منافق و عوضی و بی عقل هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/alonews/141160" target="_blank">📅 16:43 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141159">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی: تمام توانم را برای افزایش قدرت ایران به کار خواهم گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/141159" target="_blank">📅 16:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141158">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vo1hkFLEGTdqY1cRZKRZJh2xEMoRWiwoHjUoagGpIdbBit65EOwlkOu4QyJsUIIfETfMf18G2QZqnT-27p_bfGaH-93_uCiHYn5XnWRXKY8i0obQ3Iq8xdgPAr-CQEsOjQrWvWcE_TxDY9fijK6kGvxc2nQyy21chNAXwtimmiF4MlEjvxyRAQrTy76-Q48d4gXVPf-jeIgw1Mz1G9ImFpPaEoTLwgRAGv1PfEtanmd24WbwvLfxNdS_2lDSDQufMV_-8MRNypvgLiBO3DLhKE86HJXQIyxo-SMbo9tnnz1IIPIzkbODi8xAKdbKaE7wCOxJLTu-NMAPCbXYEkWfyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی: تمام توانم را برای افزایش قدرت ایران به کار خواهم گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/141158" target="_blank">📅 16:27 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141157">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ha7kF2OniQ-h1YBGa7szElZXoiJNcJgTmQF78xSK7hhXUaMtI1hOER_BAiUg1uhD069y0c4rEANFSrvWfmQ9XnVns2pcMLl1lXyKil60O2EGj0mWNqhdRjabrNNXQzzaTXsuY-0DEgVbUFy-LBj-qznB18OakzJ8Yam5grM_Az-xgIgkOfRNrmvmX1C-GENOaXR_o43cXSBUjuxRui_t5DOvOXQSLY26cJjBkg5FIbTPaaw9T6C2zS3AAfOJdYTieer0xWR2xKmWFCORO1yOAC7S8NuqTbLPvTcILnbcxPCQadO5HnVzmJZQ9eE_4RieqLV1NZbUkx_NS96Fs8TZkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مهدی مطهرنیا:
اقتصاد و ارزش پول ملی درحال نابود شدنه اما برخی آقایان در توهم هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/alonews/141157" target="_blank">📅 16:11 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141156">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
وال استریت ژورنال خبر داده که نیروهای آمریکایی امروز به سمت یه کشتی که با پرچم پاناما حرکت می‌کرده، شلیک کردن. ظاهراً این کشتی قصد داشته محاصره بنادر ایران توسط آمریکا رو نقض کنه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/141156" target="_blank">📅 16:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141155">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h4eeL26SOlTGYv4Lva2K3PZc4RpzXqPvanfnRiSHCd0J_wS6cSyJBgkXxlicZ0uiKMv7lWmzIBMif_j9ninclZ0uq8yGaGViq6SNmpEja3XyezF5J9ASI7jktJN64A2b95qmV00fjGXo_oJpwCgDGXGdmTz0_r1nK5Xz1HIdvDF5egxIatpgpCleK-C4Ci9i_e868IvVntQD9LTP3x0ZuKKbElyp8ldDQmBW_RITei_KSFXCPa_F-7qdhSkPdcs_i2AFVH3UhvOm9J3F-Q0Kda_vNxVuK8Lgni5nJg7oe_0ti2rO6iVDTKAyX9Tx8Xcu199yJoxZPgrbqhMSUhmKKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فایننشال‌تایمز: پول و نزدیکی به اسرائیل، نفوذ امارات در واشنگتن را افزایش داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/alonews/141155" target="_blank">📅 15:58 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141153">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
بلومبرگ: پاکستان می‌گوید ایالات متحده و ایران به توافق در مورد صلح نزدیک می‌شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/alonews/141153" target="_blank">📅 15:51 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141152">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZkZIV6kr1sa0eVso3JbdzBwdDd0o_YtRmRyBx5BaIBDsc3-ezLikNb4zyACNfGmqf1BgSPWYbuHmKCR5mIs5557DMz1oRIp2ykPjxnYmSCFrYA5sYkCjcPaY4taONBQQ90RIH9Oxr9F0lzBwlXRWnF6TRR602aRp1-1CBvm72VC1i0I3bPlLsbbaOBSSVP2iTNr2cN41KFjI9vlV9rZG6WZzIko-atNG55BrCZQQy9pZwPjU-bLy-OKxD1O3fvdmC5GHkG_xEfFS2Koi5pmU5IhbkQ3DVtCuQHaBVsCYMsQ3xO9mmFX4RAP2aOO7S5mehPHmVXdpy8O9G5-L66R4RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آتش‌سوزی در کارخانه نخ اطراف بیدگنه «ملارد»
🔴
دود مشاهده شده از آتش‌سوزی در محدوده بیدگنه «ملارد» مربوط به آتش‌سوزی در کارخانه نخ است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/alonews/141152" target="_blank">📅 15:41 · 20 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
