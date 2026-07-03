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
<img src="https://cdn4.telesco.pe/file/IRDVUkCaJDt0UYV0t7c3Y8uwpyKn5kRb3y6DZTvGS5efGeRiT1ubf5AaP3O7eAIPiIJHzDk7yb2_FOsk0ORny-A5-gACrczqL8Tu_Z2VfGSt6sNh368VilbCSq5NM5T-2HBXZkc8pmpVBsZqsb4teUlLRiudV8X7y8JB_6s7xNyhSh0__YgovOpcRlBOMFs_YK5Rbflg1U4-7yJI-PJmjPwhLN-uqGWiEKGJmCeG3QWsopCRf0Rj3RkS0XQ1mvfxIoX6Zu8CBYQ7iCGkd3lDUaS5Dv1Szk1fJNfymfXwc04PiDSPxNUDortkpFrFnl-FfWXoEJHm7N3aT_XI6OOdvQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.69K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐https://www.youtube.com/@ArchiveTelll</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-12 19:49:21</div>
<hr>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZlhOp7ux2IpCTKNFnKUATepaAFMXoPi-2oBKz-dqtayaOhZyx6jCKYWnc8XvNguPwm72bRg2bZ5iF98t3u5J3NQXCnJbecI7r3rOD0p1CmjF1YBlC0SUV5DF3Ls22oAlnOgt-FOrJqeeeRTZEXQldN96UTkm49aOuGo9pylm7Sf6Pdkr3rba3BXJWwLdhrzunv2Csu2HSBAJVsv8kdY1MG0VvbGpAeYx9utPBjAol9J5jawaKXmeico1CiGDH13HNZqGMLnqPY13smBahVihscKnng7VLVHJd3e4DeA5Enun_zWbTQBYHyc5aE7d9JDfeoJ_XefeDhTjdpfA_hdxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادا پولاتو چیکار می کنی؟
پولام:
به زودی ۱ میلیارد*
😊
@ArchiveTell</div>
<div class="tg-footer">👁️ 717 · <a href="https://t.me/ArchiveTell/6702" target="_blank">📅 17:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZFKwXLENRj12DiLR61bKvMqaM8AGOlhHBszX_hvdx981RTNWFl1nZud5IQlHYJozu01QKexhh7oJH_6kayrKY9Rw5yhb0gfXSBOkOrrctbCCJj9WMxlYviA9oiYrQIK3VpT8gssnEqG1ikTqPUcx0qAhCaR_QmyNoNmoAZyu-BziTrdm6bx4RrHJBCP7O0FQ-Pxmi0UZYzD9qv8uUlnA05Y9M1Jo41qq87AURI10DAbwM4U_i0lPgoNVQN0mjRzZeOz6TtLgv7Sv_mq3iA8wFV1bBcXk77uvNZNGYrOBCTC2eSh1I1Khrc9I3gz53uidjlbfUjyddpykq6xGe1PfSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V3OYkczeCKgwhymlPbeUrq7-iHr3LNVRmpmlZFRsoB_oVp-RltkDmiQvqv1IxWqmjkREwToTm2C_PZjvuAPR_i9ELRIkt3mz5ImJa_HbSZxTjeW-FlVZpGyeGZnigxc8ABlcTsqPOa573LFlyNXKoOkky93CTEl6Xf1WLvOjT9YV88Peap2YrQT16Y859vFV0bUSrbrYGl_zE1Q00lmVrdO2rWN9TI2Z6SDjS8PYo_5ng4E5CvNZtDX42PWyM2YOGYyxLs7GoCCpTM252qVG-5lkMUYcRPHRI3w_nyzlj7ywXttd-oZadz3xiCfciDbI1YqSTdjAeD1UZzmxCKvDAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XI1VHF3d4mfYEz_PxrOo-3-035lvI7y2ry7ebpJrDLhm9Myfgge4RTQeLMuW0tHzf9iSU88MtXjNSsSeXrve0fjD4jp9-z4xPTUcDbbxgG1hO1R0kHb4NOkp9RdIZF74xPQH3wXYMAQYxVY4MqFMz2TzNsIQyy_hoFeVDH1clD3784LgvjvttsWR9BkL_NdKfz85BjfkqQi79LSFG23vgCMSAGlyb4HXShX0PrOrIx3Bdw9ScLa8hmhFvdvtcYUQSxPdT-FlBlYemPEk6abGJeRNvJHdBc_1rWCipcWnuN_mQ7wwJDGKzdCefQeizW-jDs6Qlfd7Ql7GH4OsfrJzNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NIiESgcg5YoWHynUjOxr14Xybhg8yzK171WZOgr7Yb_jivtixSPSvswrIbRig0mWtE8PUSc9YjskYwqjxJ958KRFatAm7MNl_3FrB71wX9rcQSkMCDQRB6IPM4dtTP4wT_HG7v1UNaLAfc01tAnaylXhkLMpnl561bkRHbwnfp6BWKzZ3NbdiAMQU8GtrFHmWxDcth_pHDQvH7XE1HMgoMV0KKm7JzFWyyqDdkPBfmwFlua1JQG-bgkVL5SiQYhS-iZBY94Hlgif6IZYr1BkQBZ66YJzD5w1E_DfYUQfWVX51mTwAjr0cW67i4x9NN8jMhU-PvgaqpEcKsCfMIsGVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iLA5SVcFTxKkvYvnyW4-nMjgygaB6xLF4eLnUaKXgtj6e5h-sucFoVFMA3wWxMlQYxbyUjJylrWkOFP8Sv5uzhB094hChblN4nyRtWj3CQSdsTuhMvdtyQogofaCc8pd8hVVu1oefS3DTCDK3j6K9xF2SSI0wYUJYX5v5wlI8vxZ4Ve0vxE64V6m7IGFWU2Qdc0Ubdig0Y4YjhSVh2t543rWz8uW5C0ioPd_oQV5rAK7ytjauubsVddwQSxFPL2QSfeD04qlD0TTRl5ts3GCM_wu7TBA2Ahlg-i6Knm6sgQAYSTLwA5fGAB1sLdIR9Gp8S6R1P0bvaZJ7uN846EArg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b6rKOTa5VGTFRx7juQ6aEcqBBn6qso5MlAbcltBUnrsYddoZb4fFwoMae7bvDdq6Z0E-0zQpbd2q29tiqoPiKR8i3r26jc0MXdnYnIbcVcuNLD-G2JfmUyUTvuVC3FAbuHxOpmq2kwo75SB-tnI9nCr_0CKABYrGebevROzrb6tv0WLMCz8EmxLJMYMHXVMhIEGLJGamxE-Zbpm-D1rHceFJFc_0XCZPFmWgJiQpCidg87ZhL4P1qJRJ_y3-cXK_5Oe8DcSTYpceH3rdVgau_UQhpf092QYxQeTtWkz93RBp0bvJNFN5cNoP87fdNIrp1fugvMmWK6iCCHYRsfaqmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bmW2phAl7yZsm3TXn3ggsXdiHj37JQNn_626MI4Y66B6whzle58hh-a4SVZxOvH-7uhupnTkaugk6lRFX-qNPK0wFrv3mG_gIu9rzX6hGrk1CoOu1ULms4iedGRVwph0hO4gjwnElclqv3FNS0IAMMrTftfrr6fvt06KGHujT8qpdgkuwSidg4ATOm9HXnuBDocp70-nmuTO48EZUmxV5W6JTS7l3LNV5pXnQ2O6wYMWY0dDAu0CkwLD_29FQdl-1fOSbTUiBouNUh4P7Q3V30r9qEMY4AwAiX0D27NQyl3SlYnW9rLWD0EQG1tnu0JRpfxnAgQrMCvZNsE7D_V48A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نتایج
جایزه عکاسی با آیفون اعلام شد.
در این مسابقه سالانه عکاسان از سراسر جهان بهترین عکس‌های خود را که با آیفون گرفته اند، ارسال می‌کنند.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 856 · <a href="https://t.me/ArchiveTell/6695" target="_blank">📅 17:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXt1nzhDZxj3b1zda50QGkkIZ9dpWy8YT7aDRTWHD-WC2RLKkQJbgrTIruXidLGZfl_zmj2MAnHl5d-CZyk-xyBSffLLqVCkznU3hzLE_RQQA-HS8z1ayLcD3WWG-Uc8SIXaYNiRSdahCU_xruC_jFCQshIddZhGw3CIezno-J-sVmUNAnPFDTDnbMTrAdsBWp4F0eX9X30FTtc-zTiWHjnN3ymRmYqMc93U3lxfN0GJjqz6xoNbRCLZpcYtNhrGh9aaMjl7iLK8RZgLtIqxDkeL8t01fK6eiG9Q-rI9TXm1EeHwmiCGa2-b0R5NvQDmT3aoM8sVrkU8uT8bpoz-xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">AITwitter Generator
یک افزونه برای تولید توییت است.
این افزونه که بر اساس فناوری پیشرفته هوش مصنوعی ساخته شده، خلاقیت و سرگرمی بی‌حد و حصر را به حساب کاربری توییتر شما اضافه میکند.
https://tweethunter.io/generate-tweets
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/ArchiveTell/6694" target="_blank">📅 15:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WMfjh1o5z5Isj3q8zuVP-uHhhWfsaMEty9GXVRzT7P_U7D_peJskgjNbwD3-getBZN6xUXVQzwF9DsL6oWIXIaRPj7KkoNABMOL7CGakGvatTa0DZ40_L9UvppZ3n8Ryys5aqeh41XqahV12qq_xgC69n3deqgsPFvu9tJbeP2DFK4Zm1LIRAdSYqyDE_eIesLWNCnIIzkh0ermWBpf8UTno_3wbc4fWlXsc7Lqb11l-6O_2PVioSUy7lwXDq6kB8oytPgGpy5DT_8ML-btdhrdgQm642wuJ8IVnKFBv0HaHxjgRd4yLaos4A8Y0Njfb6KVi84v5Wqxc2D2dgInFkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنتروپیک مجموعه‌ای رایگان از پرامپت ها برای Claude ارائه می‌دهد
🤩
این مجموعه شامل ده‌ها راهکار آماده برای بررسی امنیت، رفع اشکال و بازبینی کد، خودکارسازی وظایف و موارد دیگر است. برای هر پرامپت، توضیحات مربوط به نحوه عملکرد آن ارائه شده است.
https://code.claude.com/docs/en/prompt-library
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 996 · <a href="https://t.me/ArchiveTell/6693" target="_blank">📅 15:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ul269Skwk82NdaxBX5V1sZfJKGvk0Tz3ECxWJ8BxbORrBHnfYMUzwxpFu0a7AYo0_NiTDZqUof1kzvy_PMXn2yZx3pUBg6xjgemCx-Qc5CdngFlhVwWThNwCkYhIRKzpgddvTZthSPZZR-Axvmx77iTPfX78oN7LTQK5xUjKX91W4xJdaydWK3Fi4gLFYDzGP-UhoPEBu-sCGPdqtBPepbIpgoOGSTKFH1qKHTdRRQLaKfaMgs6GyiX_Z4Lfg0HPyzdloqoYTVSrBMjGpFgb3KSc7RcMgyJIyxIQ8mnU7B619hsO4hMK1hfj6FIvGibr7JCpzCejL4c-9G15MHJWxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فتوشاپ را فراموش کنید
🤯
یک ابزار مبتنی بر هوش مصنوعی می‌تواند تمام وظایف را با دستورات متنی انجام دهد و برای این کار نیازی به مهارت‌های طراحی یا دانش فنی نیست.
🎨
✨
🔹
همه چیز بسیار ساده است: یک عکس یا تصویر را آپلود می‌کنید، پس‌زمینه را تغییر می‌دهید، اشیاء اضافی را حذف می‌کنید، رتوش انجام می‌دهید، کیفیت را بهبود می‌بخشید و از ده ها امکان دیگر استفاده می‌کنید.
🖼️
🛠️
🔹
بدون ثبت‌نام و مستقیماً در مرورگر
🌐
🔹
کاملاً رایگان
🆓
https://ezmaker.ai/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/ArchiveTell/6692" target="_blank">📅 14:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‏
🎁
500 کریدیت رایگان ‌Opus 4.8⁩ و Fable 5 هدیه بگیرید!
‏دنبال دسترسی رایگان به قدرتمندترین مدل‌های هوش مصنوعی می‌گردید؟ با این روش ساده، ماهانه ۵۰۰ کریدیت رایگان دریافت کنید.
🚀
‏
1⃣
وارد سایت زیر شوید:
🔗
‌www.relay.app
⁩
2⃣
‏ ثبت‌نام کنید:
‏با اکانت
گوگل
یا
مایکروسافت
خود وارد شوید.
3⃣
انتخاب مدل:
اگر روی آیکون پروفایل خود کلیک کنید و وارد تنظیمات شوید
در بخش اکانت ، اولین گزینه را بزنید و select model را انتخاب کنید و مدل مورد نظر خود را انتخاب کنید
4⃣
لذت ببرید:
‏از امکانات پیشرفته و کریدیت‌های رایگان ماهانه استفاده کنید.
✨
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/6691" target="_blank">📅 23:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🧠
یک سرویس جدید که قادر است مدل‌های سه بعدی را به کتاب‌های آموزشی تعاملی تبدیل کند!
📚
✨
هر مدل سه بعدی را بارگذاری کنید، سیستم به طور دقیق ساختار آن را تجزیه و تحلیل می‌کند: عملکرد هر قطعه را توضیح می‌دهد و نحوه کارکرد آن را نشان می‌دهد. در پایان، یک آزمون کوتاه برای ارزیابی دانش شما ارائه می‌شود.
🧪
🔧
برای آشنایی اولیه با قابلیت‌های این سرویس، مدل‌های آماده‌ای در زمینه‌های پزشکی، مهندسی و علوم طبیعی در دسترس هستند.
🏥
🏗
🌿
https://atlas3d.space/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/6690" target="_blank">📅 23:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6689">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0677cd71ec.mp4?token=su-MiunMJ7XQ4u_FbljGsl3JCtFGXYg2c3mQUyHRGf-XoiEfPv1Z37qdi2XpgExOuKNI3dmzrbqlS_tVgIcP04m64Os2U4Kdpz8i4F7YwmcOTRO0h7UGFozgsrp2g4mNqZpLZLoIXFgLSYj8dfd6L_SpxQhqRbnmfgthhEbLk4bYPgpLOYjCc69IzUd-y3T-UzIa4EQ-x2cX57ym7WW9g2ETmJ1JqNCleWvgpQT4rtRSOB-dszRCzxmXJAKnFpNk1uTmWoxUpYE9uFwOsro2pmglsoUReACyBBI6EB4Q10Ql5S0ajw_ElRHIKXSh_2_WLWSGkeoV-7Yqb4MLYYBXHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0677cd71ec.mp4?token=su-MiunMJ7XQ4u_FbljGsl3JCtFGXYg2c3mQUyHRGf-XoiEfPv1Z37qdi2XpgExOuKNI3dmzrbqlS_tVgIcP04m64Os2U4Kdpz8i4F7YwmcOTRO0h7UGFozgsrp2g4mNqZpLZLoIXFgLSYj8dfd6L_SpxQhqRbnmfgthhEbLk4bYPgpLOYjCc69IzUd-y3T-UzIa4EQ-x2cX57ym7WW9g2ETmJ1JqNCleWvgpQT4rtRSOB-dszRCzxmXJAKnFpNk1uTmWoxUpYE9uFwOsro2pmglsoUReACyBBI6EB4Q10Ql5S0ajw_ElRHIKXSh_2_WLWSGkeoV-7Yqb4MLYYBXHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
😂
سووو رونالدو با رینگتون های مختلف
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/6689" target="_blank">📅 23:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">آموزش‌ گرفتن Fable 5 به صورت رایگان تا 1 ماه هر هفته 70 دلار
💰
برید توی
Aerolink
و ثبت نام کنید
📝
لینک ثبت نام
🔗
نحوه ثبت نامش دقیقا مثل
freemodel
هست طبق این
پست
📄
نحوه اجراش روی
claude code
هم همونه فقط این تنظیمات رو بزنید جای اون
⚙️
{
"env": {
"ANTHROPIC_API_KEY": "کلیدت",
"ANTHROPIC_BASE_URL": "https://capi.aerolink.lat/",
"CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1"
},
"permissions": {
"allow": [],
"deny": []
},
"apiKeyHelper": "echo 'کلیدت'"
}
هر ورژنی از claude code هم بزنید قبوله
✅
لیمیتش هم دقیقا مثل
freemodel
هست
🔒
موقع اجرای claude code بجای دستور claude این دستور رو بزنید
👇
claude --model claude-fable-5[1m]
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/6688" target="_blank">📅 22:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚀
معرفی Qwen Gate؛ دسترسی رایگان به API مدل قدرتمند Qwen 3.7-Max!
🤖
✨
مدل Qwen 3.7-Max در حال حاضر یکی از بهترین مدل‌های هوش مصنوعی است، اما استفاده از API رسمی آن هزینه دارد. ابزار متن‌باز Qwen Gate نسخه وب (
chat.qwen.ai
) را به یک API کاملاً سازگار با استاندارد OpenAI تبدیل می‌کند تا بتوانید به صورت کاملاً رایگان و لوکال از آن در پروژه‌هایتان استفاده کنید!
🔥
ویژگی‌ها و قابلیت‌های این ابزار:
1️⃣
سازگاری گسترده:
قابلیت اتصال بی‌دردسر به دستیارهای برنامه‌نویسی مثل Cursor, Claude Code, Continue و سایر کلاینت‌های مبتنی بر OpenAI.
2️⃣
چرخش اکانت (Multi-account rotation):
پشتیبانی از مدیریت و چرخش بیش از ۳ حساب کاربری برای جلوگیری از محدودیت‌ها.
3️⃣
امکانات کامل:
پشتیبانی از فراخوانی ابزارها (Tool calling)، استریمینگ سریع و دارای یک داشبورد حرفه‌ای برای گزارش‌گیری.
4️⃣
پشتیبانی از مدل‌های مختلف:
دسترسی به Qwen 3.7-Max, 3-Max, 3-Plus و سایر نسخه‌ها.
💻
نصب و راه‌اندازی سریع:
برای نصب کافیست دستور زیر را در ترمینال اجرا کنید:
Bash
curl -sSL https://raw.githubusercontent.com/youssefvdel/opengate/main/install.sh | bash cd opengate && qg
پس از اجرا، آدرس
http://localhost:26405/dashboard
را در مرورگر باز کرده و اکانت Qwen خود را اضافه کنید. حالا می‌توانید از آدرس http://localhost:26405/v1 به عنوان Endpoint (درگاه API) در نرم‌افزارهای خود استفاده کنید.
⚠️
توجه بسیار مهم:
از آنجا که این ابزار بر پایه اتوماسیونِ رابط کاربری وب کار می‌کند، احتمال مسدود شدن اکانت توسط سیستم‌های امنیتی وجود دارد.
حتماً از اکانت‌های فرعی و تستی استفاده کنید
و به هیچ وجه حساب اصلی خود را متصل نکنید.
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/6687" target="_blank">📅 21:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚀
ساخت بی‌نهایت اکانت معتبر با یک Gmail!
📧
✨
سایت‌های حساس (مثل صرافی‌ها، ChatGPT یا AWS) ایمیل‌های فیک را مسدود می‌کنند. اما با ترفند پنهان «پلاس» (+) می‌توانید بدون نیاز به شماره موبایل، بی‌نهایت ایمیل معتبر (برای دریافت اکانت‌های تریال) بسازید!
🔥
این ترفند چطور کار می‌کند؟
قانون جیمیل این است: هر عبارتی که بعد از علامت + (و قبل از @) بیاید، نادیده گرفته می‌شود.
مثلاً اگر ایمیل اصلی شما ArchiveTell@gmail.com باشد، می‌توانید با این آدرس‌ها در سایت‌های مختلف ثبت‌نام کنید:
ArchiveTell+twitter@gmail.com
ArchiveTell+vpn123@gmail.com
از نظر سایت‌ها، این‌ها ایمیل‌هایی کاملاً متفاوت هستند، اما تمام کدهای تایید مستقیماً به
اینباکس همان ایمیل اصلی شما
ارسال می‌شوند!
🛠
ابزار کمکی:
برای ساخت خودکار هزاران آدرس مشابه، می‌توانید از ابزارهای آنلاین
Gmail Generator
استفاده کنید.
🔵
@ArchiveTell
| Bachelor
⚡️
#آموزش
#ترفند_جیمیل</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/6686" target="_blank">📅 20:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65311253ad.mp4?token=VUT1q1HFjUf57O_hz2xn4ksNjr8V08zQwAZd7h898UsHG_Aa2j9imNooi3N87p9OkNUDrVvWwg48ssJ-KM049SQQW0ZyXjflxZ7MXrgl6pYsh9cOKn-8jA2cQgUhbuTClr34uXDF4VTuMYo7Z1zgcW4xFqNwwuD9_pRU9coSf6r9OZJ71-j19eSH74bIY3P1kMhp5x4L0abxFgD-fcnvLuTUlsDSQBc0uTaixCuXDpEgO1XhkzVYRdLV1ANudS0EKj6IwyTTzgaWRJVsY0IXGAKAfFBhRWpL7Ho0qdVHCJ1AyV-Uv-eS_2ceGJNvXujG5_hDHkKeMFRUbYDUoV8SWIGOo2Qej4z4SQWoUwDjFooPqMZ92_2P0qlsS7DjX1ikBOcH2RF9pGpSn_6M1c6BV34u7j4iLIi6g10j5vywq_rdRmkg92IskjdcqBKF9JHZ7AUIOucwTout4aXNhWZ75onYg-ReP7tYiLQGlKkurdOQiAKxncWPNx-KbkRgtjQ9NGyLeGhJpiXndDMtWZ6pFHylSlULBcWinwKxQXmtCNjeb4rQ5cAQkN3k-znshKOYPszA27kSE6PJhwAbFHo4-Dkufu5EeQSQ4rTLwjQ39QWOW_R-bhUhdFWY3P36jXCoPY986QnwrFNxHDS_lJftPhwU6z0RGoBiinwv-wmmejY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65311253ad.mp4?token=VUT1q1HFjUf57O_hz2xn4ksNjr8V08zQwAZd7h898UsHG_Aa2j9imNooi3N87p9OkNUDrVvWwg48ssJ-KM049SQQW0ZyXjflxZ7MXrgl6pYsh9cOKn-8jA2cQgUhbuTClr34uXDF4VTuMYo7Z1zgcW4xFqNwwuD9_pRU9coSf6r9OZJ71-j19eSH74bIY3P1kMhp5x4L0abxFgD-fcnvLuTUlsDSQBc0uTaixCuXDpEgO1XhkzVYRdLV1ANudS0EKj6IwyTTzgaWRJVsY0IXGAKAfFBhRWpL7Ho0qdVHCJ1AyV-Uv-eS_2ceGJNvXujG5_hDHkKeMFRUbYDUoV8SWIGOo2Qej4z4SQWoUwDjFooPqMZ92_2P0qlsS7DjX1ikBOcH2RF9pGpSn_6M1c6BV34u7j4iLIi6g10j5vywq_rdRmkg92IskjdcqBKF9JHZ7AUIOucwTout4aXNhWZ75onYg-ReP7tYiLQGlKkurdOQiAKxncWPNx-KbkRgtjQ9NGyLeGhJpiXndDMtWZ6pFHylSlULBcWinwKxQXmtCNjeb4rQ5cAQkN3k-znshKOYPszA27kSE6PJhwAbFHo4-Dkufu5EeQSQ4rTLwjQ39QWOW_R-bhUhdFWY3P36jXCoPY986QnwrFNxHDS_lJftPhwU6z0RGoBiinwv-wmmejY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شبیه‌ساز هاگوارتز ( مدرسه جادوگری سری داستان‌های هری پاتر ) از ‌Fable 5⁩
در این قلعه افسانه‌ای می‌توانید درس بخوانید و با جارو پرواز کنید.
🧙‍♂️
‏این شبیه‌ساز مستقیماً در مرورگر اجرا می‌شود.
https://hogwarts-production.up.railway.app/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/6685" target="_blank">📅 20:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ظاهرا کلودفلر اعصابش از ایرانیا **ری شده و از این به بعد دیگه ایمیل فیک قبول نمیکنه اگرم بکنه تایید نمیتونین کنین اگرم بتونین تایید کنین بنتون میکنه
😍
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/6684" target="_blank">📅 18:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ArchiveTel
pinned «
دریافت 2 دامنه رایگان بدون احراز هویت و شماره و ...  https://youtu.be/1yzxi-U_vVo
🔵
@ArchiveTell
»</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/6683" target="_blank">📅 18:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🛡
آیا وای‌فایِ شما واقعاً امن است؟ (یک تستِ ساده و حیاتی)
خیلیا فکر می‌کنن چون روی وای‌فای‌شون پسورد گذاشتن، امنیتشون کامله. اما حقیقت اینه که اگر پسورد شما ضعیف باشه، نفوذ به شبکه و شنودِ ترافیکِ شما برای یک فردِ آشنا به تکنیک‌های ساده، کمتر از ۱۰ دقیقه زمان می‌بره.
⚠️
چطور تست کنیم؟
در دنیای امنیت، ما از روشی به اسم «Capture Handshake» استفاده می‌کنیم. وقتی یک دستگاه به مودم وصل می‌شه، یک تبادلِ اطلاعات (Handshake) بین اون دستگاه و مودم انجام می‌شه. اگر کسی این تبادل رو ضبط کنه، می‌تونه آفلاین و بدونِ اتصال به مودمِ شما، اونقدر رمز عبور رو حدس بزنه تا بالاخره یکی درست دربیاد!
💡
چطور نفوذناپذیر شویم؟ (اقدامات فوری)
۱.
پسوردِ قوی انتخاب کنید:
رمز عبور باید حداقل ۱۶ کاراکتر شاملِ (ترکیبِ حروفِ بزرگ/کوچک، اعداد و کاراکترهای خاص) باشه. رمزهای ساده مثل شماره تلفن یا کلماتِ دیکشنری، در لیست‌هایِ هکِ «آفلاین» در عرض چند ثانیه شکسته می‌شن.
۲.
غیرفعال‌سازی WPS:
این قابلیت که اجازه می‌ده با فشار دادنِ یک دکمه روی مودم وصل بشید، یک درِ پشتی (Backdoor) خطرناکه. حتماً وارد تنظیماتِ مودم بشید و
WPS رو کاملاً Disable کنید.
۳.
ارتقا به پروتکل WPA3:
اگر مودمِ شما از WPA3 پشتیبانی می‌کنه، حتماً تنظیماتِ امنیتِ وای‌فای رو روی این گزینه بذارید. WPA3 به شکلی طراحی شده که اصلاً Handshake به روشِ قدیمی تولید نمی‌کنه و عملاً در برابر این حملات ایمنه.
۴.
تغییرِ دوره‌ایِ رمز عبور:
حتی اگر رمزِ پیچیده‌ای دارید، هر چند وقت یک‌بار اون رو تغییر بدید تا اگر کسی قبلاً در حالِ شنودِ ترافیکِ شما بوده، دسترسی‌اش قطع بشه.
این پست رو برای کسانی که هنوز رمزِ وای‌فای‌شون ضعیفه، فوروارد کنید!
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/6682" target="_blank">📅 13:39 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AbKvhWmgMYzHe_jyKKKZU3uv6l1uPoqEhEDMnffeU5hslRjWiZjDtgMKPxAPgXpPrps1h_l5JI1yjo2B4e8rFt6CT5Pe1_LjtJ5ipRYBN-cle8gb1GK-bNNp038lqF4SzeW4V0O6arNi0nSwZ65FWTU301dHNvcm4V2b-Wk1aD4v3zbFCoKW9jgOc7TQN-6BwAPl0aasi5uFBH_UTX0DhYaQoACYO1KxPO_3I119s77av4wcnIeQf8GpsS4FLGEApPqguiTpiPzhct0ejOrCuvd2DBKuRuyj9Hk_MvY_WYUPTkifp0oNwK8CfipuoCLAjx7Iq2ft9eiMXwLeg5Ll7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/6680" target="_blank">📅 09:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚀
دسترسی رایگان به Claude Fable 5 از طریق GitLab!
💻
✨
اگر می‌خواهید به صورت کاملاً رایگان از قدرت مدل هوش مصنوعی Claude برای برنامه‌نویسی، ساخت سیستم‌ها و توسعه پروژه‌های بلندمدت استفاده کنید، گیت‌لب (GitLab) یک فرصت بی‌نظیر ۳۰ روزه برای شما فراهم کرده است. با اجرای این ترفند، می‌توانید نسخه گران‌قیمت Ultimate را به راحتی فعال کنید!
🔥
آموزش قدم‌به‌قدم فعال‌سازی:
1️⃣
ثبت‌نام:
به سایت
gitlab.com
مراجعه کنید و با یک حساب گوگل جدید یا یک ایمیل معمولی اکانت بسازید.
2️⃣
تعیین نقش (مرحله حیاتی):
در بخش تنظیمات و شخصی‌سازی پروفایل، نقش خود را حتماً به عنوان
مدیر سیستم (System Administrator)
انتخاب کنید.
3️⃣
انتخاب نوع کاربری:
زمانی که پرسیده شد چه کسی از این فضا استفاده خواهد کرد، به جای گزینه «فقط من»، حتماً
«تیم من» (My team)
را انتخاب کنید.
4️⃣
تکمیل مشخصات:
کادرهای مربوط به نام شرکت، پروژه و گروه را پر کنید. (اگر با خطای «مسیر گرفته شده است / Path taken» مواجه شدید، کافیست چند عدد تصادفی به انتهای نام گروه خود اضافه کنید).
5️⃣
فعال‌سازی نهایی:
روی گزینه «ادامه به GitLab» کلیک کنید تا لایسنس آزمایشی ۳۰ روزه Ultimate شما فوراً فعال شود.
⚠️
نکته بسیار مهم برای جلوگیری از خطای دسترسی (Permissions):
وقتی وارد داشبورد شدید، به هیچ وجه چت هوش مصنوعی را مستقیماً از صفحه اصلی (عمومی) باز
نکنید
. ابتدا وارد داشبورد خود شوید، روی صفحه گروه یا پروژه‌ای که ایجاد کرده‌اید کلیک کنید و سپس از آنجا روی آیکون چت
GitLab Duo
ضربه بزنید.
در نهایت، از منوی کشویی انتخاب مدل،
Claude Fable 5
را انتخاب کنید و از دستیار برنامه‌نویسی حرفه‌ای خود لذت ببرید!
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/ArchiveTell/6679" target="_blank">📅 09:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">دریافت 2 دامنه رایگان بدون احراز هویت و شماره و ...
https://youtu.be/1yzxi-U_vVo
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/6678" target="_blank">📅 02:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rx2_oikSsU0ju1xmHoaMbChRwcxI3mTR16qf-Eurn0q1DcRWbhLL2h7mJQ26cGWFAARPE9peSlHOtCj44fQReWs97rO5O6k_R_w7XzVmVGNwEpwygNHQ7l-PSWW26X5oocDnhWjA87z4m78z6YOGM9ucE8s1QftuKZL7vHiN5AC9kIsveQUU_LpSoLWeruv0JMIF6K7D4Y5ujPekZiqokHN2saokM6CgzmqX-_gjhXGzMjbaJtbkng1OJLwc0MXWDVk7pbbWRywJNYjjUTViO4b2OJQCzr_v_o3slIdYr9JV1IlY4L8KSl8FyaFda1cLJnM1S87wpka_eVlOLwUBxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توسعه‌دهندگان چینی GLM ابزار قدرتمند ZCode 3.0 را معرفی کردند
😮
این یک ابزار همه‌کاره برای نوشتن کد و تعامل با عوامل هوش مصنوعی است: همه چیز در یک پنجره جمع شده با امکان کنترل از راه دور از طریق تلگرام.
این سرویس به صورت رایگان در دسترس است.
http://zcode.z.ai/en
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/6677" target="_blank">📅 01:29 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RXo27GswaE4Ob-tPip7LcvP1KBAekqE8MUMTckR7WLAlMtWRKiKAeAoGh8WMWMtvZwVlA4UKDvkRyfz5TQtWbkL1VVzjjIYzs_55MdEAekb2UfzXvOMu_ZCvXXDMpSPYqkvhf0EimhzpEF1IHSHqLlAFZqXVoLyDN_88GWJSDbIiLtrJjPKJinaaFYisiZM6PyAaYYSMb0smoXaXuYahkmiz1rDZau8dH3iEzBTj8IaX6PVElQJRVdKlZWc4V3oZiIzE8mn9GcvM3VZdropUiCdp2-lNi_Db54_GgcvNVxHhaZjMGP6s4M1F3xfu21Wmvmhv9n4YUXK_KqTedrqbSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازگشت Fable 5
🔥
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/6676" target="_blank">📅 23:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4eb8383feb.mp4?token=H1lm6Xv08a_pKMaLXuYds_46DUqfU9Igc0LV197h11vIAQsyKbBhrJpBmal0Jp7wIbA_6xuP2H0_zmIqdwK5zobh_LKAEV4-ZKWrDDtyafz9Q6nqA2qWMVLS2ph5hWim5fhd8vdINJCQVHkuSUF7RyECaGWiOFdoqhJLfsPIM_OPqDIStNniGBQZKhJdboUMQhkU1m9KdXH7w5thXA9_0i_eL4zmS8VODzw5T4lYkaZxPhHCDUKZQoPLJCB3tTs7ESZbcaUnfn7-mzNxKjOE_0omQ7fPsWOEHFSN83KXT5cQtpWbNU8-sTe_LQgTkxtp8lWopOq1QnYu8wcsBxp780Q6fsLFu7L1N02F55fatbG86qvQQwuh4vIFrwNrpv0I2mOYvBNTCXqPA-x9_jLIWYY5DePro3nsuWrZzyVx8OlMibL46baxn65a8ulFSY18onI-sdcod991HT3ifVl0dETs9pObOwZxdN4G2RNA4s8uRxGAfxJxaPXkqpmzXvB8EdApvOe1DqKK2cszXAcgmEfu_JsiNgTFDMVhCuzzNGF2ZnJa0XZfiXOxDG0rzsPE8I96dglNf5TRYWxKKZ6FyjBjFUrDjKOOxi2n0wjt_f_3tBQVrK-_zA8pU62E6IjUDFUhcs3CvN1Wlgls4IcdasBvt9_97USTITnXT5IGPxY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4eb8383feb.mp4?token=H1lm6Xv08a_pKMaLXuYds_46DUqfU9Igc0LV197h11vIAQsyKbBhrJpBmal0Jp7wIbA_6xuP2H0_zmIqdwK5zobh_LKAEV4-ZKWrDDtyafz9Q6nqA2qWMVLS2ph5hWim5fhd8vdINJCQVHkuSUF7RyECaGWiOFdoqhJLfsPIM_OPqDIStNniGBQZKhJdboUMQhkU1m9KdXH7w5thXA9_0i_eL4zmS8VODzw5T4lYkaZxPhHCDUKZQoPLJCB3tTs7ESZbcaUnfn7-mzNxKjOE_0omQ7fPsWOEHFSN83KXT5cQtpWbNU8-sTe_LQgTkxtp8lWopOq1QnYu8wcsBxp780Q6fsLFu7L1N02F55fatbG86qvQQwuh4vIFrwNrpv0I2mOYvBNTCXqPA-x9_jLIWYY5DePro3nsuWrZzyVx8OlMibL46baxn65a8ulFSY18onI-sdcod991HT3ifVl0dETs9pObOwZxdN4G2RNA4s8uRxGAfxJxaPXkqpmzXvB8EdApvOe1DqKK2cszXAcgmEfu_JsiNgTFDMVhCuzzNGF2ZnJa0XZfiXOxDG0rzsPE8I96dglNf5TRYWxKKZ6FyjBjFUrDjKOOxi2n0wjt_f_3tBQVrK-_zA8pU62E6IjUDFUhcs3CvN1Wlgls4IcdasBvt9_97USTITnXT5IGPxY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎮
واقع‌گرایی GTA 6 شگفت‌انگیز است: یک علاقه‌مند صحنه‌هایی از تریلر رسمی بازی را در دنیای واقعی بازسازی کرد.
بعضی از صحنه‌ها عملاً از نسخه‌های اصلی بازی قابل تشخیص نیستند
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/6674" target="_blank">📅 20:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EoFIkOIKcLatQSZnPuWZQ4nC4gV9V_7d-Doxot8IR32jYC5yiDxFJ6Yw66kWrp27QRupJ32j04yMsJbktb8oOIMKmmRviMfxn5Z73q5qJEN3y2QxrmvKsfvc20vFgfIISRUKs6_LB4IPw44HZqBi-ZQbG8ZHLLwm-EywZg9EYqU_i6YBDnKXusFBMj13LIhl5bhNXjzfYXkRgwPlMUpZOFCga3t4yJEw3VVS1dZLRLmuWMj4CavVOiWZ_tKoYD_0N9nAFOAK-yJiKcuUrScuuKDuAqEcLVIRgxCuKpQHUnqANyezDURekUVJ9l3e1TMnip6lP4bX1wDa2JDacmhu6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکنون هوش مصنوعی مهارت خودآموزی (self-learning) را به دست می‌آورد — عامل یک راه‌حل پیدا شده را به خاطر می‌سپارد تا در هر جلسه جدید دوباره آن را جستجو نکند.
🧠
وقتی هوش مصنوعی با یک مسئله مواجه می‌شود، این روش را ثبت می‌کند و علامت می‌زند که دقیقاً چه چیزی کار کرده است. دفعه بعد سیستم مسیر اثبات شده را دنبال می‌کند، به جای اینکه دوباره گزینه‌های ناکارآمد را بررسی کند.
https://github.com/Kulaxyz/self-learning-skills
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/6673" target="_blank">📅 18:54 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6672">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJnt0z5SYZrOJLnxaPTTMaMfb2F2-kbF5CCGwY0-kk-WJBcLX_AeK6NE2KaU7R6Rj3LIrT925Z52kYJvurM0tnnzY469jtnnXjWKfPIx3l9l0ZjkBfy-1jil8vESRC0CWyzxHqAzn8uMsyqe3Ic1x9FJsMxi76gZWu_omnO2bwWkMjh2wMB73st7tQF9uMzHpnaS83oQ3amb09BwXwM7wZOA_zVZT5QtqQ8SSVK4K8LRSoeTVF09Wq4qnn6-V_pBVoMsPaXPH3Ko7s27CKQcfcKYGwja10ZcMZ7UZybOD_q46fNzR4TisnKX1BJcDKnH1P9-LjVOKfI7IV6ksrRvlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">RevPDF
ویرایشگر PDF سریع، بومی و متمرکز بر حفظ حریم خصوصی به صورت آفلاین است.
این برنامه امکان ویرایش متن و تصاویر را مستقیماً در سند PDF فراهم می‌کند و همچنین عملیات‌هایی مانند ادغام، تقسیم، فشرده‌سازی و تبدیل فایل‌ها را انجام می‌دهد.
تمامی عملکردها به صورت محلی روی دستگاه اجرا می‌شوند و حریم خصوصی کامل داده‌ها را بدون نیاز به اتصال به اینترنت تضمین می‌کنند.
https://github.com/Pawandeep-prog/revpdf-release
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/6672" target="_blank">📅 18:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6671">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc1d8b6548.mp4?token=GUrS4jO8Wg9IJKhUTKAw4KrEVY4kAYrMHAzG71uDvjpiLTE0YWA9Qzn2MEu1XsGiSLFqXMvVWPkkCugTN8XP1Kt72KDJpC6xaVLrYatlxujdkDhyALd7exLuWv1iV85w6bOgn7ZyiEXI-1hCn7TaUl-XPcsAHUnZYF6Ef78PJYLCQfPaBAtvODNLBa3vSORfjBhWZsSzSbamccyOOPuh_8Ms6yC2EneaRZgSCLPkP3_imGXdfklMVj93xo_LFwwKZmw2xL037bI7Yk5MYhH5q4rc1emRkLKRyuSOoEWhfrAPjjrYMXscjgRiq8_tbxso06zjNXtUjvZBtLyU7PAsHYGLoPk6MnB7urMB4OnowcX7Jyvnwg64VNg9C21WalJgLDefosnno7ISfKW5eO6TXnDGLBemOQlVYIPjOAOrZZDhO0Ly8mja7tsCQSKbnTzrCqIgwtTXc-xN45Cw8gHl1LCl6n3WiUb3eGbxp0AZoPSfOh1O-YVyuQJqk7t-NUVjcXW54dsdqrhVMp_QXWuUUBL8-f6ErrSnylfeG2OmjKeU7Djcek2pkaicMMtQZ335mlh_OPDojkC8EQ-_wPtIaxxK-XgRAu1KgMUbMsTggO-QghvHMPuXiAmLVwFrFzVa_cAZ9Y2vUAdNd7OtsbNMGTMji6NvYHNGU38cUu7iJ3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc1d8b6548.mp4?token=GUrS4jO8Wg9IJKhUTKAw4KrEVY4kAYrMHAzG71uDvjpiLTE0YWA9Qzn2MEu1XsGiSLFqXMvVWPkkCugTN8XP1Kt72KDJpC6xaVLrYatlxujdkDhyALd7exLuWv1iV85w6bOgn7ZyiEXI-1hCn7TaUl-XPcsAHUnZYF6Ef78PJYLCQfPaBAtvODNLBa3vSORfjBhWZsSzSbamccyOOPuh_8Ms6yC2EneaRZgSCLPkP3_imGXdfklMVj93xo_LFwwKZmw2xL037bI7Yk5MYhH5q4rc1emRkLKRyuSOoEWhfrAPjjrYMXscjgRiq8_tbxso06zjNXtUjvZBtLyU7PAsHYGLoPk6MnB7urMB4OnowcX7Jyvnwg64VNg9C21WalJgLDefosnno7ISfKW5eO6TXnDGLBemOQlVYIPjOAOrZZDhO0Ly8mja7tsCQSKbnTzrCqIgwtTXc-xN45Cw8gHl1LCl6n3WiUb3eGbxp0AZoPSfOh1O-YVyuQJqk7t-NUVjcXW54dsdqrhVMp_QXWuUUBL8-f6ErrSnylfeG2OmjKeU7Djcek2pkaicMMtQZ335mlh_OPDojkC8EQ-_wPtIaxxK-XgRAu1KgMUbMsTggO-QghvHMPuXiAmLVwFrFzVa_cAZ9Y2vUAdNd7OtsbNMGTMji6NvYHNGU38cUu7iJ3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚡️
«اودیسه» نولان - تریلر نهایی. این فیلم یکی از بزرگترین آثار چند سال اخیر خواهد بود.
با بازی ستارگان: مت دیمون، تام هالند، ان هتاوی، رابرت پتینسون، لوپیتا نیونگو، زندایا و شارلیز ترون.
اکران: 17 جولای.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/6671" target="_blank">📅 18:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TFgdi_dsmTUzF7-zeM2SVBsyiDqCSHJhpT9tNQ4pPm3DTAdXVjK9KYBJIYuMefNmNUAFkx5H89P3qHArYmI765c2WGhQBunVDhPE6R6X1YWeKZeQyl-4c2YjrIj4sZzjGpfFU6JPjk5hwRG3Q3iKW-YL5ApfVKIwicA-Jb-8tg2LD5XZQ3ZCJ5AzCxyKyIvBrpULIF6Qe9Zq7IyEiK5N4xkqaEaMJWaL4H5NGJS979WsTRrg0JaeuEccevnia1EV-zICJAQl4yr_l1qM9kiOmXQTOSq6mM8T4qNgFivcPWgO_fTbN3xEdpzg9igslJvj8FF1OMjtZYjWlClz4OSBIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در عرض چند ثانیه هر نوع کپچا را در سایت‌ها و منابع دیگر رد می‌کنیم
• به سرعت بیش از ۳۰ نوع کپچا را حل می‌کند، رفتار انسان را تقلید می‌کند تا هر محدودیتی را دور بزند.
• با چند کلیک روی کامپیوتر نصب می‌شود، نیازی به ثبت‌نام و نصب نرم‌افزار اضافی نیست.
• فوری و به صورت محلی کار می‌کند.
https://github.com/clawdbrunner/captcha-solver
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/6670" target="_blank">📅 18:08 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6669">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/268d269709.mp4?token=ku_81w4q27rqYR3xJK_ElHUmVK9iKBa9X36ESe8YVo13GJ0tzoklxFC5eGdtZa7K7Gl5_0PIGONPQr9pDaAd8QmuM3vHH5AXQAUsmZTSbE0Hopw9jVYPaM44cvmDAj67JfdY937kfl4TAHrOv6FzaOxhyNy5a4pXoXjN7g5WD-1V29YgAKFelQjnkXYsQWFlHPI_kcq6JYNfw-4oMXRluWG0YesZawZB2A2LDYoLXjOSgk_hfbRBK9jmf9YEmTGPed5pAFOZvqPdRaQwTQ9pINM6Stq2ccPDmVc6DiN_FT3AJvI9TTNLRhjbwvtU2hU0Ptuy4pQTP43TY71TpKaU2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/268d269709.mp4?token=ku_81w4q27rqYR3xJK_ElHUmVK9iKBa9X36ESe8YVo13GJ0tzoklxFC5eGdtZa7K7Gl5_0PIGONPQr9pDaAd8QmuM3vHH5AXQAUsmZTSbE0Hopw9jVYPaM44cvmDAj67JfdY937kfl4TAHrOv6FzaOxhyNy5a4pXoXjN7g5WD-1V29YgAKFelQjnkXYsQWFlHPI_kcq6JYNfw-4oMXRluWG0YesZawZB2A2LDYoLXjOSgk_hfbRBK9jmf9YEmTGPed5pAFOZvqPdRaQwTQ9pINM6Stq2ccPDmVc6DiN_FT3AJvI9TTNLRhjbwvtU2hU0Ptuy4pQTP43TY71TpKaU2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
شبکه عصبی Gamma به ChatGPT اضافه شد — حالا می‌توانید پرزنتیشن‌های زیبا را مستقیماً در چت بسازید.
ابزار هوش مصنوعی محبوبی که صدها هزار نفر در سراسر جهان از آن استفاده می‌کنند، در ChatGPT ادغام شده است. حالا کافی است ایده خود را توصیف کنید یا متن را وارد کنید، شبکه عصبی آن را به یک پرزنتیشن آماده با اسلایدهای طراحی شده تبدیل می‌کند.
می‌توانید تا ۱۰ اسلاید را به صورت رایگان تولید کنید.
🔗
لینک
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/6669" target="_blank">📅 17:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6667">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rpnbB7wnBcHI6Osv0dygqlfkOgVgu5D8HrVGrBRI00mMWoybnjT79Z3DyahxCiVJVpqUEHVI6RXCIdPzt72fGVmfvPqUYGnLkm56K8BUJiK0epfz4nHExO_6TtHLfXoSKTEEu1hUlrlpTZbrHZb2zmzEjG0wR6egUt1heBL0RrfTGgV-QKTkmey7dJouNGiT7nQ822N2FSFYD4g1p7s5zNA2LcrCjPmf6v0jL2kEm2ilYd9NMTaCnw85fqdj0BYbAAPEwryQGbKJjntPJtf8U9hxv8FGDRAkkTAXEAdVwVc6T7S0OUGmLfcGX6MX2GaKNUP7ItS46WVvMA6IY-J-2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دیسک‌های بازی پلی‌استیشن سال ۲۰۲۸ ناپدید خواهند شد
بازی‌های جدید فقط به صورت دیجیتال منتشر خواهند شد. همچنین سونی فروشگاه PS Store برای PS3 و PS Vita را خواهد بست.
یک عصر به پایان رسید.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/6667" target="_blank">📅 17:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6665">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚀
معرفی Superfile؛ فایل منیجر مدرن و فوق‌سریع برای محیط ترمینال!
📁
✨
اگر از طرفداران محیط خط فرمان (ترمینال) هستید و به یک مدیر فایل قدرتمند، زیبا و سریع نیاز دارید، ابزار
Superfile
دقیقاً برای شما ساخته شده است. این ابزار با رابط کاربری بصری (Intuitive) و کنترل آسان از طریق کلیدهای میانبر، تجربه مدیریت فایل‌ها در ترمینال را به سطح کاملاً جدیدی می‌برد.
🔥
ویژگی‌ها و امکانات برجسته این ابزار:
1️⃣
پشتیبانی کراس‌پلتفرم (Cross-platform):
اجرای بی‌نقص روی تمامی سیستم‌عامل‌های دسکتاپ از جمله لینوکس، ویندوز و macOS.
2️⃣
شخصی‌سازی بی‌نهایت:
دارای سیستم پیشرفته برای نصب پلاگین‌ها و تم‌های متنوع جهت تغییر ظاهر و افزودن قابلیت‌های جدید به محیط برنامه.
3️⃣
نصب سریع و بی‌دردسر:
قابلیت نصب تنها با یک دستور ساده از طریق پکیج‌منیجرهای معروف مانند curl، winget، scoop یا Homebrew.
4️⃣
محبوبیت و پایداری بالا:
توسعه‌یافته با زبان قدرتمند
Go
که توانسته بیش از ۱۷.۷ هزار ستاره (Star) در گیت‌هاب به دست آورد و نشان‌دهنده استقبال بی‌نظیر توسعه‌دهندگان از آن است.
https://github.com/yorukot/superfile</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/6665" target="_blank">📅 16:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6664">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ao-ACipPcii40HItkYIoNvpbbTlxbxMaU-VSdDCxVbLr-DNqdROTPge8ATI2p1OIXtcFAZ0CePl4lz3bvIxPVxh5K9-K6bb3z0wqr26y_wzeY16hl-lrDjFkx-YHk7P2UeeZ7eKeyApVk1aQ7BLIgMfePmv_7NL1Py_GpG0lSGNgZ417BMXX8-67phaZAldcF_2Vy1R-5bMp29Nkr48SBIbw_n3B6Mor8qq5Ag_hTXKQboYorHWV_3owyQixLvE_9an-613FrROpeKAaW2X05YAh9NuFiJ8uiqdkNABG9cEc5ETBIUrmplJ7RxoKpPBLJ1C6cnc3Q-Ud0dW28i1egg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر اروین یالوم خودکشی کرده ظاهرا
😐
اروین یالوم نویسنده و تئوریسین روان درمانی اگزیستانسیال</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/6664" target="_blank">📅 15:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6663">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hrmQvKuJ284t6efZ52KXxCWaXvI__1G3oGhSjToE3NkjOYdrsgLatFdeqRmUrSki8YAAcuxlB84Danr-YIX6y7Zm6T3985rInQFYGyzf6xfn30Po2nixBtVAhFnvkGZvCx5sgRJ51UlfQXT0-DNsj7NtySBd9GObgHBCsWP1kxfNGtZ3L-HqroePCp3Beu1hGaAhYTt5i960Q5aZUPER_tIMVyLtNMJvN-1Zwf4utXDd6EmK6DO-kygAQSRbSS_dD5qFyYxeSO3mMAxYW_OSxor1_I0UumclDSq1jKf9TRSE-xM35JJM7iNGd3gZjHaqzIrwFYhg-wjwJAm2fV00Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر سرویسی راه‌اندازی کرده است که پروژه را از نظر سئو، جستجوی هوش مصنوعی، احراز هویت ربات وب، MCP و پارامترهای دیگر بررسی می‌کند.
سپس به سایت امتیازی از ۰ تا ۱۰۰ داده می‌شود و یک پرامپت با اصلاحات ارائه می‌شود که می‌توان آن را به شبکه عصبی داد و سایت را بهبود داد تا امتیاز خود را افزایش دهد.
https://isitagentready.com/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/6663" target="_blank">📅 13:27 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R9HOhz0-37cAvFwU5jrhidN-Tdgpz5z9HnrKBnM6MECgh9U1IpNEQ7gqW-IJ61peYijyFPPSTj3FVWxJv-6vM295OO2cfpLFt7-NzxO9b18BqMHtq3Y1sGvsAurbDczQZkLMBo7WiuZtO-KifhCTY2N_PVOCkFuoxr6xiCDyrLemh2QaTEIMc9KEz1LvPavDQPc4aevex3_ahpoP4Gg9y0wqTteoX0d02NZbnim0Gyqy-V8BmPSK7rQYHIWp_07y4l6PckMjlpvg20k2wOUdgqocOHD4-aZMw6u131I75ngR4OlbRDFh9ZMeJqVOGYx5P8HWRL5qTEDSlRNKN1xMRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منبع مفید برای توسعه‌دهندگان: در گیت‌هاب یک فهرست عظیم از APIهای رایگان برای همه موارد زندگی جمع‌آوری شده است.
🌐
بیش از ۵۰ دسته‌بندی موجود است: از آب و هوا، ارزهای دیجیتال و مالی گرفته تا یادگیری ماشین، نقشه‌ها، موسیقی، اخبار، انیمه و میم‌های بامزه با حیوانات.
🐱
💻
https://github.com/public-apis/public-apis
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/6662" target="_blank">📅 13:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MwfHf4ek5ftTrME4JNQiMS6r06xMB6ZSdgsg6-vUplhS6hPmzfeS_js-di4s241yuPb7TDTbG6ihNHk3r-dEmd-sNwiIHJipTLyhvA81hZA_9qvmHYEkDBLFibKPGX8p9ccxweFCnUux-UhodJ0DZVnC89fcFzlOP10OtoET6TE-5jNyWspMOcDzM1aSB_uIGY4GL7BFX7UUQhJd92cSdMR7X-JqupjOnfsPNN8Ys9RTPCzRiw-2ITrNHqo0n2C7gDd3h0-PSiKM16de43FVOKpzcCbcIqiE2l5TP-RTwu9aARkoA2wQBQqvpfgs8AQC5vwZjpy6gOxDH4__wz_9xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RLV1Elu6hLrZQv_LRS8_RetHbAWux9ZS9u0Hn1JBI4CCwfkIGdAZH_IKChDKdoqpXHu6jDGM4XADrgDGZYOK-IZ51RyGqFZ9FcPobiL8059MbaS-ZQGOh-pVXhRHtT6LDrgQVGr0x5hSwzl0ZdTeNCjft0ztjGuW_XBdRAPejZGRQ-zYClIU7_lZ5AMNczZhuM6GOwi3w2wyFg2ocI3cKpRsGtJp7hGF37VTbkeBrzOag7uNJvyKxAhni1v_ej4ensTzNY_466xxCsXLYnUl9H87G318qogWa0B-FnLpepeOK9Z4q5h_9yQT5QBFVTc8qoXeX-O1vdZXNMXCHVDa2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nR1CRbqVaVvz_MPKXqhTqchwVB28cC88Sj7MNbPCuu4ldGpvsfRmy86DtnA1UAWpbyB2wbb9LT-Ug1TV37ANbIVsGycwh7NmYo0mWXv6no63D3sui1IPKhp7yrCYYBDoA4HeuyfKo5ZFMIGCKKe_v6OnNKH6y3Gsfl9UkQP5NPjLCQituwjSZULlZWLpb7WMaP-SuVw7zEFSgezwLHdTaMHkLVmsTIUahtxjG37G9z7fUjNKFHvQTUHJQg6uZyrNwa-di6odEsVWsEliMbD54G0bg5m5Njd_Qs0bWJfVzS9ArQ05L7LJ1A4BY4oL7zmrbf_x3fo1gjFiNT4hO0jdtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BLg5D2lD7w-M2UfmLEDHwnHE2ccH_SI9-ysloEK4ty_Iv3gJylv7hLzS4oyj_83qoHfHL3cxHQKoQ_wPHjx-xp2ubVHxyGRAQNR8RRIrjTTzYVOKs7XgXz0JwxO6HiUIKwN7t-JgRdFhGw2QcLTLX6aziXi_VV8ugIyrol2xVkkpebvZcdMse6LmS5R0ZdY_h17TNSc5NQT45-OrEcAfc-5zY7GDvtT_z-eIwI8mq_m4WyIiZ9vmZ0Fwn3wgrEwwNBsu4gsRLHbjGsFmct7BWiJTz-IAzRHGpN57prm-sQOWG4SLhIQblIHV19uGM_-jYVrfOpaCRncFeUngD-g_VQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">PlayTorrio
مگاتورنتی که همه چیز را دانلود می‌کند:  بازی‌ها، موسیقی، فیلم‌ها، کتاب‌ها و هر نوع فایل.
https://playtorrio.pages.dev/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/6658" target="_blank">📅 09:35 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWlL_pnOncaJ9Lr3FcvzA5LoyuhR9efYgSk-YsB16dSgRFG1HPrbpmb4GRnP1q9xeAUVs7DO_8wM7_Llu0_g_4vOxa1mhNbL0O8wI43mKLYNfASVqz-YQ4ZRwk5K7gp7jb4Ip8hmW2U55cNKYXXNmEtOsXl-mbA70fUASmgCHdGl75ECbe7dbsYqO-e65_wPkfLMoRMoSGjwcyMvV2NiKVc9hxeO9ISBqg5HMcW6DE8FUyZqYlVRxhO_u6bkyHkP9Un10HTf7EFZqtSw4gJWB-p4EB-mHQ06jptlDmB8sl7MvvV1GXXGmnvyhbXOxCZt9hzwaQLWs_WWDnLjwQBRCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
کلود Mythos و Fable 5 برگشته‌اند! دولت ایالات متحده این دو مدل‌ رو از حالت مسدود خارج کرده است.
امروز Fable 5 برای همه کاربران در دسترس قرار می‌گیرد و تا ۷ جولای می‌توانید تا ۵۰٪ از محدودیت‌های هفتگی خود را روی این مدل استفاده کنید.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/6657" target="_blank">📅 09:10 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/heU5aokX40OO1dhwQBbobi8OoidH_YWBalpmtOBOztHgzU7-26JY-uRzyMIhX8oo3qhVuQHAMLLxlhElq6prwBn8CWumttZWIu6a51LLJ4tY1sszo7sllBrgny8ZYWmynZkSbm7YwIJCJNpht9IkwZUGJSv2lZ3imgx6BhG9pB9qEMJYiyqAacNTeobsTGFPz-zdIcyPBODL_ZJP-RCEYTc6RH02PS5F6vpNPYVEQaj_s8N9zWxLt-NpWNidvQturaQIjUssKGL3g6rmxnK9xb09q8AUsrzX60-qBSZHisKum6T6DMxuaYBBtORJNfNIY5O8GeFDWAbMeBC7l1aLjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلود اوپوس بدون سانسور منتشر شد!
توسعه‌دهندگان Qwen 3.5 را با داده‌ها و استدلال‌های Opus 4.6 آموزش دادند و یک نابغه شرور واقعی ساختند.
• محدودیت سوالات فقط تخیل شماست.
• می‌توانید هر چیزی، حتی ترسناک‌ترین‌ها را درخواست کنید، اما مسئولیت آن با خودتان است!
• به صورت محلی اجرا می‌شود و بسیار سبک است.
https://huggingface.co/DavidAU/Qwen3.5-9B-Claude-4.6-HighIQ-THINKING-HERETIC-UNCENSORED
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/6656" target="_blank">📅 08:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6655">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ArchiveTel
pinned «
🔥
آموزش ساخت سیستم ایمیل موقت نامحدود و اختصاصی (روی کلودفلر - بدون نیاز به سرور)
🔥
رفقا سلام! تا حالا شده بخواید تو سایت‌های مختلف ثبت‌نام کنید ولی نخواید ایمیل اصلی‌تون پر از اسپم بشه؟ سایت‌های ایمیل موقت (مثل Temp-Mail) هم که دیگه تو اکثر سرویس‌ها بلاک…
»</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/6655" target="_blank">📅 08:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6654">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">درود دوستان AssA هستم
بابت خرابی ربات
@REN_WZA_BOT
دیروز معذرت می‌خوام
حقیقتا به خاطر شرایط نتونستم سرور تهیه کنم و ربات روی کلودفلر ران شده
فکرش رو نمی‌کردم که قراره انقدر استقبال بشه که سقفش به نصف روز نکشیده پر شه
😄
خبر خوب اینه که یه ربات بک اپ گذاشتم برای وقتی که سقف اولی پر شد بتونید کار هاتون رو راحت روی ربات دوم انجام بدین
جای نگرانی هم نیست تمام اطلاعات دیپلوی ها و کاربر ها انتقال داده میشن پس عملا هیچ فرقی برای شما نداره
مورد دیگه این هستش که خیلی از دوستان بدون اینکه پنل قبلی شون از کار افتاده باشه یا مشکلی پیش اومده باشه ده تا ده تا میسازن که واقعا عجیبه
🤔
خلاصه که دیگه قرار نیست به همچین مشکلی بر بخورید
و نکته سوم هم اینکه ربات دوم کمی با عجله ساخته شد اما از تست های خودم سالم بیرون اومد
اگر باگی یا مشکلی دیدین با تگ کردن آیدی ام توی چت بهم بگین
@Assa_7788
(بابت مشغله های کاری و پی وی شلوغ به احتمال زیاد پاسخ ندم بهتون پس ممنون میشم پیامتون رو با تگ کردن آیدی ام توی گروه بنویسین)
و عذر بنده رو برای طولانی شدن پیام بپذیرید
🌚
❤️</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/6654" target="_blank">📅 05:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6653">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">الیوم اکملت لکم دینکم
🚶‍♂️‍➡️
😂
(حس تکمیل پروژه خوبه)</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/6653" target="_blank">📅 23:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6652">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/6652" target="_blank">📅 23:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUPt9k5zu-fhaiXl7hcvIUigrS4CRW5ILa9VFXvC__8MyvsaJBU3fm6QMs5abVbRzMMzWDLYVAPwsIhVSk1z0YGEOEK9dwHKARfGImxp-XogosvE4xQkLWm4-MW9lf3Gn3PbyS3ZoADJPZc3PUxPWx-oOdHNbVxRr9iYAuwcp4K__86sPqZwv_kz2a3iynV_4hUJcT1zch2OyLoossepyBYOv7h38Sjz5mbrwBXzBV90vY7kUxqmjqu5Ia188Tr8vTKqEqtCkhtIuCr3Snf03sIW6w7vINuh-MWUI0pxC9qm3FLWTNrxqL8u8260dEg6Ji5DR7VbQ6FjAJV9eBAryw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://www.youtube.com/watch?v=JnpHyg-Vc40</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/6651" target="_blank">📅 23:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">CFMail@ArchiveTell.zip</div>
  <div class="tg-doc-extra">471.7 KB</div>
</div>
<a href="https://t.me/ArchiveTell/6650" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
آموزش ساخت سیستم ایمیل موقت نامحدود و اختصاصی (روی کلودفلر - بدون نیاز به سرور)
🔥
رفقا سلام! تا حالا شده بخواید تو سایت‌های مختلف ثبت‌نام کنید ولی نخواید ایمیل اصلی‌تون پر از اسپم بشه؟ سایت‌های ایمیل موقت (مثل Temp-Mail) هم که دیگه تو اکثر سرویس‌ها بلاک…</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/6650" target="_blank">📅 23:22 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔥
آموزش ساخت سیستم ایمیل موقت نامحدود و اختصاصی (روی کلودفلر - بدون نیاز به سرور)
🔥
رفقا سلام! تا حالا شده بخواید تو سایت‌های مختلف ثبت‌نام کنید ولی نخواید ایمیل اصلی‌تون پر از اسپم بشه؟ سایت‌های ایمیل موقت (مثل Temp-Mail) هم که دیگه تو اکثر سرویس‌ها بلاک…</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/6649" target="_blank">📅 23:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔥
آموزش ساخت سیستم ایمیل موقت نامحدود و اختصاصی (روی کلودفلر - بدون نیاز به سرور)
🔥
رفقا سلام!
تا حالا شده بخواید تو سایت‌های مختلف ثبت‌نام کنید ولی نخواید ایمیل اصلی‌تون پر از اسپم بشه؟ سایت‌های ایمیل موقت (مثل Temp-Mail) هم که دیگه تو اکثر سرویس‌ها بلاک شدن.
تو این آموزش یک ترفند فوق‌العاده رو پیاده کردیم: ساخت یک سرویس ایمیل موقت اختصاصی روی دامنه شخصی خودتون با استفاده از زیرساخت رایگان کلودفلر!
🚀
این سیستم کاملاً ضدِ بلاک هست و می‌تونید تا بی‌نهایت آدرس ایمیل فیک بسازید و همون لحظه پیام‌هاش رو دریافت کنید.
🎥
آموزش ویدیویی و قدم‌به‌قدم (از صفر تا صد) رو تو یوتیوب آپلود کردم. حتماً ببینید:
🔗
[لینک ویدیوی یوتیوب ]
👇
خلاصه مراحل و کدهای مورد نیاز برای رفقایی که ویدیو رو دیدن:
۱. مخزن اصلی گیت‌هاب (برای فورک کردن فرانت‌اند)
۲. ساخت دیتابیس (D1) و کش (KV):
یک دیتابیس به اسم
mail_db
و یک فضای KV به اسم
mail_kv
تو کلودفلر بسازید. فایل
schema.sql
(موجود در مخزن بالا) رو تو تب Console دیتابیس اجرا کنید.
۳. متغیرهای طلایی (Environment Variables):
موقع ساخت Worker برای بک‌اند، این متغیرها رو دقیقاً با همین نوع و مقادیر اضافه کنید (راحت کپی کنید):
DOMAINS
(نوع JSON)
👈
["yourdomain.com"]
DEFAULT_DOMAINS
(نوع JSON)
👈
[]
DISABLE_ANONYMOUS_USER_CREATE_EMAIL
(نوع Text)
👈
true
JWT_SECRET
(نوع Text)
👈
یک_رمز_طولانی_و_رندوم_انگلیسی
ADMIN_PASSWORDS
(نوع JSON)
👈
["رمز_ورود_شما"]
ENABLE_USER_CREATE_EMAIL
(نوع Text)
👈
true
USER_ROLES
(نوع JSON)
👈
کد زیر رو کپی کنید:
JSON
[
{
"domains": ["yourdomain.com"],
"prefix": "",
"role": "vip"
},
{
"domains": ["yourdomain.com"],
"prefix": "",
"role": "admin"
}
]
🚀
مرحله ۵: آپلود کد بک‌اند و هدایت ایمیل‌ها
۱. در منوی
Runtime
ورکر، تو بخش Compatibility flags، کلمه
nodejs_compat
رو اضافه کنید.
۲. روی
Edit code
کلیک کنید و کدهای فایل
worker.js
پروژه رو کپی و پیست کنید. Deploy رو بزنید.
۳. تو تب
Triggers
، یه ساب‌دامین اختصاصی (Custom Domain) برای بک‌اند اضافه کنید (مثلاً
apimail.yourdomain.com
).
۴. حالا به بخش
Email Routing > Routing rules
تو دامنه‌تون برگردید. اون پایین قسمت
Catch-all address
رو ویرایش کنید، Action رو روی
Send to a Worker
بذارید و ورکر پروژه‌تون رو انتخاب کنید.
6. اتصال ظاهر سایت (فرانت‌اند):
مخزن پروژه را در گیت‌هاب شخصی خود
Fork
کنید.
در کلودفلر به
Workers & Pages > Create > Pages > Connect to Git
بروید و مخزن خود را متصل کنید.
تنظیمات Build (دقیقاً این مقادیر را وارد کنید):
Framework preset:
None
Build command:
npm run build:pages
Build output directory:
dist
Root directory:
frontend
تنظیمات محیطی:
یک Environment Variable به نام
VITE_API_BASE
بسازید و آدرس ورکری که در مرحله اول ساختید را در آن قرار دهید (بدون اسلش آخر).
تنظیم SPA:
در مسیر
Settings > General
، مقدار
Not Found behavior
را روی
single-page-application
تنظیم کنید.
روی
Save and Deploy
کلیک کنید.
ارادت، Bachedev
✌️
🆔
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/6648" target="_blank">📅 23:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6647">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">سورپرایز امشب
اختصاصی
🗿
❤️
از یوتیوب
تقدیم به بچه های گل کانال</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/6647" target="_blank">📅 22:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LqihCdkZ3QlKEqYNYQe4sBafcdEbf3qVbFg2dW5PCTNLu5UwmG81rQcJNTvu7AmmQG7yybo7ARjdudbPrUW1po_FhhlydS03lbsx4_qvFk3EAWnyNtGM6g_eeHp6Pm9JXUYn0pkkaME18MpwC2ustuqPaxJZQz5ufvcQaHKtx2kHpbabeS69iw0tHU9Sz1i7Kw7Zbxe-uBpHcpGY6gVNODUf4oAuTCR6xurgVbBZD89sS4a45Ma1lWLnaaUCHVl1-8Dg2li5we4dz1EMfPL_NfZndRgKU937N3z96JIspSeilc3vtOpKUe_U7XVrpJi8EeU9hSyCzgUpU1Yhoq5iwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Claude Sonnet 5
منتشر شد!
مدل قدرتمندی برای کارهای روزمره اکنون برای تمام کاربران، حتی کاربران رایگان، در دسترس است.
• از نظر عملکرد بسیار به مدل Opus 4.8 نزدیک شده است.
• به مناسبت انتشار، Anthropic همچنین تمام محدودیت‌های مدل‌ها را حذف کرده است.
https://www.anthropic.com/claude/sonnet
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/6646" target="_blank">📅 22:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6642">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O4dyxqi8rlf4X7JL0Zy3qwq8WJpR6_LvA6szXDsRZw1Ju4T8g_IuBoli6mKI9mcWH2g6OIGdTj3qw5KFx7qWUgvamn6JukZ152RbteDpA14F6ajDytv00aeoXCPoAOdQH9YDN2iQrlhD04TBat-fH-Wi0b1iyMyh6qacdfKMxcv4aRl2jFoQM6Ju0Z8u0hEVd3fgvwjKXEje7PJngyjaRpjFIxEwUrxT2FaVrY58kTDij1Q9jhiCzOuVrpNTNJMgVtQyqVXblgAwwCNpR-PJ8BzKgnfezwIV2uxwIwJEEv69RLYB3BjaTH7ZiBFFojYASd69C70oKslheDyYfIeDOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/clcDcWQbyxZlhofAHzBOYCbGGuRnK0ZrM14zdRPoJeb54JPaMQW4Es0dGVVPMR7N4jNhn68NM6oJLjDEUkfXdP5dX1xEI5WEOXsIVkWYXGjbmfYqKLb0kwgwmCqwgmnhwM-pr7fgyA-ddsyoNRLB16seygop0fbHayAbIiHQzks8HCfwxuNkTevnHO2RgEweKImMdkfyckTcli0r3Fn3cX_zr6b-VKBJabNth76Vf8SFJG0FfdGY-DgZf2I4KR4H7QCLHZHuljeZNYwHlSjuQKxCM50K8XLr3Qw6cLkAasgDRlWamYdAUbdpu8O69dqpSAEQdgF2oyt9H2rpVsCKhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p1YBQ5wbekBt_l0Z_Aj9rCWrmfQ5N5d52ig85bVTaran2MPvQPTlC9OUkAXfquahARArzdyEUzONJTEDWOzXIAhGRNIKJBliJyBoACIFjGvF9PnuvZjxf5X7glg8_JS3be-fZDGwpyN6Zhrrp2RS71WminKR7sa8pxktkczBjtOg1I-K7PMO7fx3vfwdrDN1e2pgeJZ4dQ4kUMUxIAl47NFzxebwJ6p-e3em-kUp9a0Nil9AbchR8IRYyxl3mGRM99sUXVxjdDsHwlOc8C9sfmiDKqdo7TR8Mqzg3fv9VUuOjBwLXcx6fyLeqa0vADBQrOOuwKQXCY2ubopuHC8MLg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9de073ef68.mp4?token=kURmehWAvPij8EJIdYLJCu99MYfGV_bgoYIxvN5fyE28URUL1FZkUa_AzWwZoEUcr0x9dMAY-KBAdqmBXcQsSRt5lNhc6esgq3VlXVqtN4pz8IO-uE37sw9CScZYFtZHU1LxdCyc3S4Z1e5uNAD1js65cwxg2sNsZWKRM3JGyjMBg3EIE_M8HF9kyZC8jl2C2LUVtTiNFC6ADx2Fu12mxyceqn6LncdkP6EZyeslPc16CpQRJ90ioZqAX-MSHXjVbP2CUxh80yTN8QQVwz8haoV94YK90GlTG5cvCVHbYw_POO_anT18E-Q3-GKlbXp8fpfhhIQJTh8C8wPmQ0P9cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9de073ef68.mp4?token=kURmehWAvPij8EJIdYLJCu99MYfGV_bgoYIxvN5fyE28URUL1FZkUa_AzWwZoEUcr0x9dMAY-KBAdqmBXcQsSRt5lNhc6esgq3VlXVqtN4pz8IO-uE37sw9CScZYFtZHU1LxdCyc3S4Z1e5uNAD1js65cwxg2sNsZWKRM3JGyjMBg3EIE_M8HF9kyZC8jl2C2LUVtTiNFC6ADx2Fu12mxyceqn6LncdkP6EZyeslPc16CpQRJ90ioZqAX-MSHXjVbP2CUxh80yTN8QQVwz8haoV94YK90GlTG5cvCVHbYw_POO_anT18E-Q3-GKlbXp8fpfhhIQJTh8C8wPmQ0P9cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💰
تولید محتوا ارزان‌تر می‌شود — گوگل مدل‌های Nano Banana 2 Lite و Omni Flash را معرفی کرد، نسخه‌های سبک‌تر از مدل‌های محبوب خود.
نکات مهم:
؛Nano Banana 2 Lite تصاویر را تقریباً در ۴ ثانیه ایجاد می‌کند و هزینه آن حدود ۰.۰۳۴ دلار برای هر ۱۰۰۰ توکن است.
با وجود قیمت پایین‌تر، مدل کارایی خوبی در زمینه متن دارد، متن را به درستی پردازش می‌کند و نتیجه‌ای با کیفیت و بدون آثار قابل توجه ارائه می‌دهد.
؛Omni Flash مسئول ایجاد و ویرایش ویدئو است. هزینه تولید هر ثانیه حدود ۰.۱۰ دلار است.
از نظر هزینه، Omni Flash در سطح Veo 3.1 Fast قرار دارد، اما کیفیت بصری بسیار قابل قبول است.
ویژگی اصلی — می‌توان مدل‌ها را با هم استفاده کرد: ابتدا تصویر را سریع با Nano Banana 2 Lite ایجاد می‌کنیم و سپس آن را به ویدئو با Omni Flash تبدیل می‌کنیم.
https://deepmind.google/models/gemini-image/flash-lite/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/6642" target="_blank">📅 21:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6641">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RraO1eWzv2zuNWT84l5bw1dFsHxVY6TtGeqUW6yqzD2DjYF6tjlMdSWtpb6QzyVrvH7bVh-7GalI_vDpJnCWsc1KAnA7yUzdBvb4csSxhtgMTWDj2ldK-FSh8AO8PDQ2iG_HrCriNiVlhswt8LqsWIlHKqRibU12whSiTXerEHACaLgGNmkqiINO-tW5VLoK9N7Q3c_phAAYlfeYB817byzaOOsSRpSOmH020JnaIBCIBEyrVQ9opZxZeLwBmHoGhfMpVJVfGpm2LFCHy1EUfDmzSCV6_OMMCmT0fcdJdiIrCfF-7GonJyHfuSRilaTQ6KoNzPpLMiBpIm0etmx7BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API هوش مصنوعی Opus 4.7
سازگار با همه پلتفرم‌ها:
ربات تلگرام ، وب‌سایت ، Codex و Claude Code
http://zyloo.io
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/6641" target="_blank">📅 20:41 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6640">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d39bc32d0.mp4?token=Q_drp0iiQjEGH0onyuL6FvRUxJsGB-uSU22zU8Maha9q-x8_Ems63W-4zragN-N0n9UeZBvs8RzU6j7kmcOxvzfaRy2vh3WHEmX6FVl57lLwWgLfCoi6uUNHJS0Pcp5nnMNZ-I2T8xI6cxi46AHmxBbDvWsyOYeXV7P7l46w8vQ1J62qTVGD123mIQ-EHQY3A_IYdO9O9mrOyyoq5DjffonNbb2OrVqIb8iEz0T8aoLENmT7L453zGHNoeu2xWcK9ijGrucgM5Am8BKZwKdGi6s_EsCd4nHIryXelqwg6bDvvAtzP3kCeqe8HIr9o2pBOwmWEVmRd2exMjFGQSr3_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d39bc32d0.mp4?token=Q_drp0iiQjEGH0onyuL6FvRUxJsGB-uSU22zU8Maha9q-x8_Ems63W-4zragN-N0n9UeZBvs8RzU6j7kmcOxvzfaRy2vh3WHEmX6FVl57lLwWgLfCoi6uUNHJS0Pcp5nnMNZ-I2T8xI6cxi46AHmxBbDvWsyOYeXV7P7l46w8vQ1J62qTVGD123mIQ-EHQY3A_IYdO9O9mrOyyoq5DjffonNbb2OrVqIb8iEz0T8aoLENmT7L453zGHNoeu2xWcK9ijGrucgM5Am8BKZwKdGi6s_EsCd4nHIryXelqwg6bDvvAtzP3kCeqe8HIr9o2pBOwmWEVmRd2exMjFGQSr3_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دقیقا همین‌طور در سال ۲۰۲۷ رم (RAM) خواهیم خرید — یک پروژه با جاسوسان هوش مصنوعی پیدا کردیم که برای شما اینترنت را زیر نظر خواهند داشت
😋
ایده به این صورت است: شما سایت‌ها یا جستجوهای مورد نظر در گوگل را مشخص می‌کنید و «جاسوس‌ها» در فواصل زمانی مشخص اطلاعات را رصد کرده و گزارش را به ایمیل شما ارسال می‌کنند.
https://github.com/firecrawl/open-scouts
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/6640" target="_blank">📅 20:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6639">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2MBlObRCA1Uhzyvh0Gf3vW2XqrgOVj3daJMU_PohLUFkwIUsbbNWQ5henmtyywYBRpzGMsYdYuYVEuUbkWKGbT7X5c2Vt06FHHpX_UUP8V8cXHNA5tNB8ZCFDjwCFreoOSO85wH5ukfnPwEB8aAbX-fnq_TUuEYqYcMLzIvhwdQgdy9QXIBoZD4dhXh5zGAxTW-pK6vK3R5OPhrYwltbhBdVY0p1Rv05y4BNrhJtpVnuD0LZfZ2-LzsUFIkaKEfdpKcpIok6e-7Y_QqO5-K7BXqEe8oUDhWdJKZ08TOK-ArZGgyTBiv8aixpoqdCIwUqqurpX6RaeuMubIdTHv7fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">DocumindAI
راهکاری برای تحلیل اسناد PDF است.
این ابزار قادر است حجم زیادی از اطلاعات در فایل‌های PDF را تحلیل کند، داده‌های کلیدی را استخراج کرده و رابط کاربری منحصر به فردی برای تعامل با خود سند ارائه دهد. این امکان را فراهم می‌کند تا به صورت تعاملی و مؤثر در سند حرکت کرده، اطلاعات موجود در PDF را درک و استفاده کنید.
https://www.documind.chat/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/ArchiveTell/6639" target="_blank">📅 20:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6638">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t9ZqjpJHfEWhN5QkNoTYqmWe2JZISvdWVphHMuqQaE4ri7ONeErMuT1_2OcnjprVal5NRGn3H5lQDvqWuU9stq8943zL1Av83YGVEe-Fao7KNj7dD2kJUfbDct1dkBw3S8gbM1uwT0ATcpszSmeamVnz7vu25mpaEttSy3A9FZoTHwaaSzC0YxxVtrTNvEhWQuVGeEK_QgputOam1Ohb-rf59nPred3HDSe2RUBgmzWS7T3LOr0tHnzwOZJtkbgbh_2bnef7zzqEcgjzEkJ3eijaUz0ceqSy7p6n6EG8CEYK61MQDKUcZeRWeJWL1jI1vYYAHRxOY22WvmhzT87Ktw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧠
نورون‌ها بالاخره دیگر هیچ چیز را فراموش نمی‌کنند — OpenHuman حالت Super Context را دریافت کرده است که بین جلسات، زمینه را حفظ می‌کند و کار را از جایی که متوقف کرده‌اید ادامه می‌دهد.
🔹
در هر بار باز کردن چت، زمینه را به خاطر می‌سپارد.
🔹
مستندات را مطالعه می‌کند، لاگ‌ها را تحلیل می‌کند، ایمیل‌ها را بررسی می‌کند و می‌تواند آنچه روی صفحه نمایش اتفاق می‌افتد را ببیند.
🔹
به طور مستقل اهداف را تعیین می‌کند.
🔹
به ۱۱۸ برنامه متصل می‌شود.
🔹
با سبک کاری شما سازگار می‌شود و به صرفه‌جویی در توکن‌ها کمک می‌کند.
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/6638" target="_blank">📅 20:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6637">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hM0MoTNclbK5XbhI6bnFuEOiuTEjXGlWO39L3L9kt4QiW_dZw8duyGlKNxUff5Vzke_F0QvmWicpiOi4nkFDyndD01uhGnMRidKGIA5KaXPnTi_mQ8S9McdHc9CacgGYdSVuMnzxK9xC-4HHu0Ffd80b-PnL4tgfmmXXBnGtvXc5W8-FfO59pL0CjMwzCA0HCipa6Owmtn8cClWZPYpkTyLgd4pcul9j5PWFSE57EEf7B_gqbThGHoHSm3PSoKBrAVv1HrUa6iwUwMIxgu1AtbdffEn_8funnErzIFFufWuG6JdX2ieTJ76HP5wkubvTwZ8Ye8A8KZPvLyauG7BHvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاک کردن واترمارک، افراد، اشیاء مزاحم، متن، برچسب و غیره از تصاویر، با تکمیل خودکار پس‌زمینه توسط AI رایگان
لینک:
https://magicremover.org
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/6637" target="_blank">📅 17:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6636">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lG7kybr2X4FDnXOhNGFNPj_2xpPUfTOlMiGN9h9CqXV7Svx6-pU3k902dpgJ7QYixZS5IKW-lRGdilnNP7ybz3hmO9f8NQib4MiGjDsGbokGBZ5heP_jbh1EisyBtbd4MIB5K43m71AsZr-6t-2pTzcKGMbj-f7mJLJJaWmw1vC_5k-bPGkkkd0bLUeGwXUUrQsKv8yhPne2nZ0-LjFCquBtDq37OWIaC5y1LqDGwC39PQs06Xuv0m2x1wjcF21SiLuOzzipaqzTeeMpHh52vbcNpRkUrImDiC5SU_SKslwnmmlcjJ7kSiylrc04rzQUMyz0gWbDYfrwWiIicFctzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🤯
گوگل را دور بزنید! ‌NotebookLM⁩ رایگان و لوکال شد
🚫
☁️
‏نسخه متن‌باز و محلی ‌NotebookLM⁩ منتشر شد؛ دقیقاً همان تجربه قدرتمند گوگل، اما روی سخت‌افزار خودتان و بدون ارسال داده به سرورهای خارجی.
💻
🔒
🔹
چت هوشمند: تحلیل عمیق، خلاصه‌سازی و یافتن تناقضات در اسناد
🧠
‏
🔹
ارجاع دقیق: لینک مستقیم به پاراگراف‌های خاص، بدون جستجوی دستی
🔗
‏
🔹
تولید چندرسانه‌ای: ساخت پادکست، نقشه ذهنی و دوره‌های آموزشی از روی ‌PDF⁩ و ویدیو
🎙️
🗺️
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/6636" target="_blank">📅 16:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6635">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mVL1rWd0I6HjyJirSz--9m7euaZXZ9pS3q2wBrdbnSt_3ArSq9wt4UVPUbalI3FaJF3Mdnmx0HHLgIbVYmSygqa8tpGU2403UoKNvoBMdZdyxh00yfIawPzoN2UxHA9Vxrh8VW5oFvhlIv76-ACg2nbRIQr2fmJcI4LG3FSPXCtoomqAif1BRyf2TY59jKyxbvhKR2MyGaVyR26bvLI0nvqIeuR_h4kxFWC-j_42JgoWXYTRQsB1EybqXdI8P-CLfjTYe16QMeGZSyA_K14sILj0txJMBWRU2cyPKxIvONyf1Jj6jVmPzrMQQwA57CVj6Uo1K6_pngLgMu2hR0uYFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دانلود فایل از اینترنت با ‌Torlink⁩، سریع‌تر از همیشه
🤯
‏این ابزار خط‌فرمانی، جستجوی فایل را برایت خودکار می‌کند تا بدون دردسر به منابع معتبر دسترسی داشته باشی.
‏
✨
قابلیت‌ها:
‏•
🔹
بررسی هوشمند منابع و یافتن فایل‌های سالم
‏•
⚡
نمایش دقیق حجم و تعداد سیدها
‏•
🛠️
دانلود مستقیم از محیط ترمینال
‏•
📦
متن‌باز و بدون نیاز به ثبت‌نام
‏
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/6635" target="_blank">📅 14:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6634">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b49cca50b.mp4?token=dteJR1_zDA70-Jg4LdAwwN2PUsem8kXpUWvr4j07W16pzarN1UXWNCasfoiN7wo98Xq1-G6hg-hQLK-3tro8mvsS3UTw43fw2TPoNiaQpUiGJnJO3teKba5MjwLEEut0PxaG8OonFCV1lgxiWskPzVU7LBDYp7ysQJIXeWf8lMZ8xeYr-jX6kddv3KiuvkmJrOgcJldrD9pM33r31vcyrE6L7GqNh4EXIEYDVRrQaqDvlGC2SoGoAsJWCjnVkc6iXiGX455t4K9q8pJ-8OOFT7eRFJ0V-4fFeZ_jKbjj1C7CnGNTKqd1P6qDrwMt1onth4shnmBE9TsIcNESEESMpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b49cca50b.mp4?token=dteJR1_zDA70-Jg4LdAwwN2PUsem8kXpUWvr4j07W16pzarN1UXWNCasfoiN7wo98Xq1-G6hg-hQLK-3tro8mvsS3UTw43fw2TPoNiaQpUiGJnJO3teKba5MjwLEEut0PxaG8OonFCV1lgxiWskPzVU7LBDYp7ysQJIXeWf8lMZ8xeYr-jX6kddv3KiuvkmJrOgcJldrD9pM33r31vcyrE6L7GqNh4EXIEYDVRrQaqDvlGC2SoGoAsJWCjnVkc6iXiGX455t4K9q8pJ-8OOFT7eRFJ0V-4fFeZ_jKbjj1C7CnGNTKqd1P6qDrwMt1onth4shnmBE9TsIcNESEESMpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوگل تصمیم گرفته که پشتیبانی از API پلتفرم Tenor، بزرگ‌ترین مخزن انیمیشن‌های GIF در جهان را متوقف کند.
دسترسی مستقیم به کتابخانه عظیم Tenor از تلگرام، دیسکورد، توییتر و سایر شبکه‌های اجتماعی غیرقابل دسترس خواهد بود.
اگر بخواهید یک گیف انتخاب کنید، باید خودتان تصویر را جستجو کنید.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/6634" target="_blank">📅 13:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B5157C9YJI5WvTc_ck8BaNeb898LYFH2Rh0sI6Rxr-3zw1eoQHX-6Qk0kKdq-SQVH9mzFob6MCJhebq1Q4ABP82emqwULE2WtO4hg2KhoieQpOCqHPiYovjm8vzP1nXibeNUGe1DLHkavtsxXdIewoWqmXb_-sZNgIoJ1KyRn-ylQKkibLnxqeFiJLgRi1kNKaM2IhHXEsDAoCRadkaG_IecZ6oGZyoK7nip-l-HZ2xqk-AIzm21Dkwycfl0vSjAXbLGsV_vYB6dXUnrymkvU3DOE6h_h8TpSpfaTbo5TQlk7KCmmri4CFxeKIVhqGNn6gvmgTvoK9Q1fl8ipawiBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚫
غیرفعال کردن ردیابی در مرورگر — راه‌حل ایده‌آل برای کسانی که از جمع‌آوری گسترده داده‌ها خسته شده‌اند و به دنبال حفظ حریم خصوصی واقعی هستند.
افزونه
Fingerprint Detector
در سه حالت کلیدی کار می‌کند:
🔹
شناسایی — نشان می‌دهد که سایت دقیقاً چه اطلاعاتی را از کاربر استخراج می‌کند.
🔹
شبح — داده‌های واقعی را مخفی می‌کند و آن‌ها را با مقادیر «میانگین» جایگزین می‌کند و دسترسی به canvas، audio و WebGL را مسدود می‌کند.
🔹
جعل — رد دیجیتال شما را به طور کامل با یک رد جعلی تولید شده جایگزین می‌کند.
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/6633" target="_blank">📅 11:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fMXVIbAgkr5dijHolVNsTXdXMMZaH8MBsVVnNK21IX4cUdoU0prPbQilbNhI721r-pANapC_m4GNWp7S_MERjDTTXeNvbXqQ6bwXDZWllx33dlKvatE3LHoRhXNJ87GniTcEij282XoppFv7uMV-mALdnAcvhaDc54wir1uHfo5f0g1t_5VpSFTZG0yf-Az_BTZ5YcCFq9Mf50sEYwGAlwoQJbadfrBwgNFfTvuY770v985zWETlZ4R_QHsPOqrv7HwMHvXuvBitMxD6Dw9BvCAR9NJtxjpOgGwzE47PtD3iEJixA0GC7PGAwQwWI7ws7p5xhqs5B2sxTe6iFJ0Geg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🤯
هوش مصنوعی بساز، پول دربیار!
‏فکر می‌کنی ساختن هوش مصنوعی فقط مخصوص نوابغ سیلیکون‌ولی است؟
🤔
اشتباه بزرگی است!
‏تصور کن یک جعبه‌ابزار جادویی داری که از صفر مطلق شروع می‌کنی و تا جایی پیش می‌روی که محصولت را به شرکت‌ها می‌فروشی. این دوره دقیقاً همین مسیر را بدون پیچیدگی‌های خشک دانشگاهی به تو نشان می‌دهد.
🛠️
‏
✨
چرا این دوره خاص است؟
🐍
مبانی:
پایتون و ریاضیات را مثل آب خوردن یاد می‌گیری.
‏
🧠
دانشمند:
مدل‌ها را آموزش می‌دهی و بهینه‌سازی (کوانتیزاسیون) را مسلط می‌شوی.
‏
💼
مهندس:
سرویس‌های واقعی می‌سازی و مشتری پیدا می‌کنی.
🌐
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/6632" target="_blank">📅 11:09 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6631">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">این هم آموزش راه اندازی</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/6631" target="_blank">📅 05:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6630">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚀
آپدیت جدید بات تلگرام ما منتشر شد!
✨
بخش جدید
Hugging Face
اضافه شد!
از این به بعد می‌تونید خیلی راحت پروژه‌های خودتون رو از طریق تلگرام دیپلوی کنید:
🔹
فقط کافیه در سایت
huggingface.co
ثبت‌نام کنید
🔹
از طریق بات، توکن خودتون رو دریافت کنید
🔹
پروژه به‌صورت خودکار دیپلوی میشه
🚀
⚡
برخلاف خیلی از گزینه‌های دیگه، این بخش فقط از
سرورهای آمریکا
استفاده می‌کنه.
درسته که سرعتش به پای سرویس‌هایی مثل Render نمی‌رسه، اما در عوض:
✅
حجم بسیار بالا
همچنین در بخش
IP تمیز
می‌تونید این IPها رو اضافه کنید:
🇮🇷
Irancel:
52.214.248.106
32.195.122.200
108.133.38.41
🌐
All net:
amazonaws.com
108.133.38.41
34.196.7.222
3.162.112.2
18.185.80.10
23.162.112.25
2.92.189.25
115.185.114.108
18.138.171.15
135.160.210.199
🔥
تجربه دیپلوی راحت‌تر با
@REN_WZA_BOT
💻
توسعه داده شده توسط
AssA
📌
سورس پروژه
⭐
برای حمایت از پروژه، می‌تونید وارد گیت‌هاب بشید و با دادن Star از ادامه توسعه حمایت کنید.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/6630" target="_blank">📅 05:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">سورپرایز تو راهه...
Ren panel</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/6629" target="_blank">📅 04:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6628">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nxye0FRrZ7NAg9mpgoYWSsdXmKid7aoZsfTquJs4-v4t0f7YkH_UQvRYOmrE_wEJ2JUbUZeka43np4lNrvlDzuWTP-cb4JXT1KwDd82rcjDOggYA44sWBOeZ0lMfsn3B9rbRbG-_r_6TQHXGyzMieOmPl9HiVXklFhV2KWEmSW0gDcHpFqxsB5dD5js7qVqgvg3F0v_qS_kPf1jUuf3yF0KS_s3SgaFHUoRZaVt_L1K4BGIIw1Amp1mezkYrKnllxkcLrMsJLGSx-udXOt0_p45A07-MaFgKE9FiaqaAL0GASgnVp8xwzmFj4O8GAYphdtKX2FzqEPucCV6-snKiJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واتس‌اپ پس از تقریباً ۱۷ سال از وجود خود، نام‌های کاربری را معرفی کرد — می‌توان بدون شماره تلفن با کاربر شروع به گفتگو کرد.
تلگرام به انقلاب سال واکنش نشان داده است
😁
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/6628" target="_blank">📅 22:53 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6627">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d53c28976b.mp4?token=mhANIYjXs-mjkKkbtJNZdNQRfnTV8TIxCyAmyoBZWZUWrmQn0iqrv7jFbUeWSnRl-6FMLMS21TMmRELSfI6mLwJc0upLMuqVNpZ3yMMDwox3S5c-YalJ8iG-bPe6mKIiU0GFQ2FW41Ro-j1KbmqoOPixYAEB-J_6eCDCNMEzNqMiyVyf8iUI1Eiqab96cgtKC2TlNLFhd7BmMPx025fAi0FjHzYykhIGF2kno0craxXpHWyrCqwdSADlxMeWOv8tAcig6MVekUuc4hlQQuDOTbp5OQsCKUg30cZwVbKs4e7NdKDy8sNq3pQL97Ax9fsLgel3g_jZlDjDJIZsn-FHQR0Lf0yiw8MdW2Ni5LQaSJdxXRqryg0UiPOsi-PDXUDAo5TfU_P3emJiwCz2NbtYpmgHYZIASt47XDaLNwnTsMe6OeF1DLQyWQ_GH6KzPliCdxcwFbBTUeatP46N-uZWzeHcZRFX0PkWW6tRSwtTDGEpi1sZ5iWRyprNyzYIF7m86-QNboZrf5t7GUPdFsuUlDM5zmglPxrRALxMqOs1CTmtjRSGkBRFwQbLM1l36pCz_zPn3EIpn0-7vgBUP09di9vH3V5yLfk8RSxzVm5gY4ElknNSDUfE9CS-K0w2CuekChAGvrmaJIfMT507TckMx85DxKKkwTjxR1dGyP_QH3o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53c28976b.mp4?token=mhANIYjXs-mjkKkbtJNZdNQRfnTV8TIxCyAmyoBZWZUWrmQn0iqrv7jFbUeWSnRl-6FMLMS21TMmRELSfI6mLwJc0upLMuqVNpZ3yMMDwox3S5c-YalJ8iG-bPe6mKIiU0GFQ2FW41Ro-j1KbmqoOPixYAEB-J_6eCDCNMEzNqMiyVyf8iUI1Eiqab96cgtKC2TlNLFhd7BmMPx025fAi0FjHzYykhIGF2kno0craxXpHWyrCqwdSADlxMeWOv8tAcig6MVekUuc4hlQQuDOTbp5OQsCKUg30cZwVbKs4e7NdKDy8sNq3pQL97Ax9fsLgel3g_jZlDjDJIZsn-FHQR0Lf0yiw8MdW2Ni5LQaSJdxXRqryg0UiPOsi-PDXUDAo5TfU_P3emJiwCz2NbtYpmgHYZIASt47XDaLNwnTsMe6OeF1DLQyWQ_GH6KzPliCdxcwFbBTUeatP46N-uZWzeHcZRFX0PkWW6tRSwtTDGEpi1sZ5iWRyprNyzYIF7m86-QNboZrf5t7GUPdFsuUlDM5zmglPxrRALxMqOs1CTmtjRSGkBRFwQbLM1l36pCz_zPn3EIpn0-7vgBUP09di9vH3V5yLfk8RSxzVm5gY4ElknNSDUfE9CS-K0w2CuekChAGvrmaJIfMT507TckMx85DxKKkwTjxR1dGyP_QH3o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خداحافظی با چشم‌درد دیجیتال!
👋
👀
تا حالا شده بعد از چند ساعت کار با لپ‌تاپ، چشمانت بسوزد و احساس کنی  به یک لامپ ۱۰۰۰ وات خیره شدی؟
💡
😫
بیایید روراست باشیم: صفحه نمایش‌های امروزی مثل آینه‌های صیقلی هستند که نور را مستقیم به چشم‌هایت پرتاب می‌کنند. اما تصور کن اگر بتوانی یک لایه نامرئی از «کاغذ واقعی» یا «شیشه مات» روی مانیتورت بکشی. جادوی
Paperman
دقیقاً همین است! این ابزار با تغییر بافت پیکسل‌ها، صفحه نمایش را از حالت آزاردهنده به یک سطح نرم و خوانا تبدیل می‌کند، درست مثل ورق زدن یک کتاب قدیمی و دلنشین.
📖
☕
✅
چرا باید همین الان نصبش کنی؟
•
🧊
حذف بازتاب نور:
صفحه مات می‌شود و دیگر نور چراغ سقف روی مانیتورت نمی‌افتد.
•
🎨
تنوع بافت:
از کاغذ کاهی تا E-Ink (مثل کیندل)، هر سلیقه‌ای را پوشش می‌دهد.
•
🎯
هوشمند و انتخابی:
می‌توانی افکت را فقط برای مرورگر فعال کنی و در فتوشاپ یا بازی‌ها خاموشش کنی.
•
🖥️
همه‌کاره:
هم روی ویندوز و هم مک‌او‌اس به زیبایی کار می‌کند.
به نظرت کدام بافت برای کارهای روزمره‌ات مناسب‌تر است؟ کاغذ کاهی یا شیشه مات؟
👇
💬
🔗
دانلود:
Windows
macOS
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/6627" target="_blank">📅 20:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6626">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">اولین تریلر Cyberpunk  Edgerunners 2 منتشر شد!
🔥
انتظار داشته باشید که هر ۱۰ قسمت این فصل جدید،
پاییز امسال
پخش شوند.
آماده‌اید برای بازگشت به نایت‌سیتی؟
🏙️
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/6626" target="_blank">📅 20:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">حدود 900 تا کانفیگ مختلف
📶
https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Germany.txt
💬
@Archivetell</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/6625" target="_blank">📅 20:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">#اختصاصی
🎧
استودیوی کامل AI: از ایده تا مسترینگ
۱۱ ابزار برای ساخت حرفه‌ای موسیقی:
🎤
تولید: Suno, Udio
🗣️
کلون صدا: Kits AI, Synthesizer V
🎹
سمپل/لوپ: Stable Audio, Splice Create
✂️
جداسازی/ویرایش: LALAL, RipX
🎚️
میکس/مستر: Sonible, iZotope Ozone 11
🔊
پاکسازی: Adobe Enhance
💡
نکته: ترکیب این ابزارها فرآیند تولید را از هفته‌ها به چند ساعت کاهش می‌دهد.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/6624" target="_blank">📅 17:22 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IwLtPH6u1XK0WSzF-O-T4cU3JsuPYzRlhgCcZ0FfcUyOe12cS-O_-hqZp6WWUE7BhkpeVeJJlDCuu96lWBkogoiSiw20q9Xchpc9LAt2VOPMBRe_UU0RmoeOm1_VCStoj0q2gFHDf27RwmPQlkEYbYIA-0gk1DISc6NbiDA7mwld43PbdyGI42cdKZSMcxY-eVG8iqGfYMT7Roq3w7fqvPSyhqMDrIH4E3mO44SPZR7-WPyRu2pO3TyGARSpoa7HSaoQ0wxMUOGCYnOyb9aNgWDh4YVVoolysevxrGonHTW93krWYy0Nk_3KvT0GzqXrs_QoI3wGaGOLMuVImlezCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی GTweak؛ جعبه‌ابزار همه‌کاره برای شخصی‌سازی و بهینه‌سازی حرفه‌ای ویندوز!
💻
✨
اگر به دنبال یک ابزار پرتابل (بدون نیاز به نصب) هستید که کنترل کامل سیستم‌عامل ویندوز را به شما بدهد، GTweak یکی از قدرتمندترین گزینه‌هاست. این برنامه با رابط کاربری نوشته…</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/6623" target="_blank">📅 15:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">نحوه اکتیو ویندوز با اسکریپت Microsoft activation
💻
اول تو منو استارت Powershell رو سرچ کنین و باز کنین   بعد از اجرا شدن پاورشل فقط کافیه کد زیر رو وارد کنین و اینتر بزنین .   irm https://get.activated.win | iex   اگر کد به مشکل خورد و اجرا نشد دستور زیر…</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/6622" target="_blank">📅 15:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">نحوه اکتیو ویندوز با اسکریپت Microsoft activation
💻
اول تو منو استارت Powershell رو سرچ کنین و باز کنین
بعد از اجرا شدن پاورشل فقط کافیه کد زیر رو وارد کنین و اینتر بزنین .
irm https://get.activated.win | iex
اگر کد به مشکل خورد و اجرا نشد دستور زیر رو بزنین ( نیاز به ویندوز ۱۰ یا ۱۱ به روز داره )‌
iex (curl.exe -s --doh-url https://1.1.1.1/dns-query https://get.activated.win | Out-String)
Github
😀
📱
@Archivetell</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/6621" target="_blank">📅 14:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">حجم : نامحدود
زمان : تا ۱۲ شب
vless://63b43d54-3bdc-4d9e-b3f3-10163c892936@64.90.7.102:8443?type=ws&path=%2Fws&host=play.google.com&security=none#%D9%86%D8%A7%D9%85%D8%AD%D8%AF%D9%88%D8%AF
وصل شدید بگید</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/6620" target="_blank">📅 12:12 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uPLfXh4YW2xps9iKseEztnaG3SvdYRu2H0yYJFCTVQxn1cCsJoV-1PLhnEWX_sBPGfXPS1VaRLSgXnDPfe6vv_lXOzNm1_isjTs8qka7kRzNxAu30uDUtj5KDHqeapq42NJ_Cc-6rPdTEPCBhMJvNGJKTODxvxYM9BGdYD8kp-d8XfaDOmEAodlYUopYfdLcpiwtlBH1s89ZBTjJsLFwgLVcboeKf-iWLy2SHfjo8HvcCLLPl4uFAkwSiMfO-zAQsbyKidNXh4dQbNAL7iyfMuUppyOKL-VGDRK4Nv-TVDbhBh3Y46f1Qb4J_z_ozeTu0kJLui51esiryM3OLLgt6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقشه راه جامع علوم کامپیوتر: ۸۰۰+ منبع از دانشگاه‌های برتر جهان
🎓
اگر می‌خواهی به یک توسعه‌دهنده حرفه‌ای تبدیل شوی، این مخزن گنجینه‌ای از دوره‌های دانشگاه‌های هاروارد، استنفورد، MIT و شیکاگو است.
✨
چرا این لیست؟
•
🏛
منابع معتبر:
دسترسی به دوره‌های دانشگاه‌های تاپ جهان.
•
🤖
پوشش کامل:
از الگوریتم‌ها و زبان‌های برنامه‌نویسی تا هوش مصنوعی و رباتیک.
•
📚
دسته‌بندی هوشمند:
گم نمی‌شوی؛ دقیقاً همان چیزی را که نیاز داری پیدا می‌کنی.
•
🔄
همیشه به‌روز:
نویسندگان مخزن را مداوم آپدیت می‌کنند.
مسیر یادگیری‌ات را از اینجا شروع کن!
👇
🌐
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/6619" target="_blank">📅 11:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G3hyf3yWgyPl-MDtuTTtagtKTUsju3kxd3UkSoIm67fX2WCs3Df-tgVrqUra4M_RP7pScaF3h4qVje5UkhQZ1YuNqtu6zk3cWdmqBsx66ZEpqJ9qnUnvmB7aeKfmhbIYr3SDgPgC2SP90l4Q4tGukEQ8Z2IsfetbNM1ldX8-nwcvz_kbjVzrpd1dHERYZYPYA9k79fgOWTgfcp-MKLml7i1i90SH-7yF9bcDQl0PAs3GH_ZIMOAiSPMAVGR8P3Hr9qJmvwJSVi3FbP3tYgEdzqGUJPEPKT9brr8IYb435J8CT5kWOKH_82-6dULohi-WrONjXXk2_xZ0HyrNSWj5xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت Anthropic بسیاری از دوره‌های هوش مصنوعی خود را رایگان کرده است.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/6618" target="_blank">📅 09:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gumDoq1ubpW-rW_8QYKmkmJltogP1A4MEBTBrG0GS5R3keiZ8CkXAM7WrMqbWgkDIPGaSzDvRmR5xXUy567oxWIDhF4a5Y5U9iPSGpbjmvXOam6e8lw-4VVYkHRUJcZFB3Suzl3gZmPgtwXs9dE_DVy_pIo9CHxiXvmZJFpaiDPbB7_9TVRckiajtufKcd4hfsRsp-t1okfVxRlxHmTHmVxqMahXejWwmszKSpZYn3B_ky4zvoMqmXbLVIDubNu5DVQoTNdZXTqEgXPZL6dLlcp_gUJrsfUfrY_6mKn5fa6oCx861EDBd_4trY971_8w3jonxa60Rdfs2GBJouQu0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">OmniRoute
۱۶۰+ هوش مصنوعی رایگان در یک API!
🤯
دیگر نگران تمام شدن توکن‌ها نباشید. OmniRoute با ارائه
توکن‌های نامحدود رایگان
، تمام مدل‌های برتر جهان را در یک نقطه جمع کرده است.
✨
چرا OmniRoute؟
•
🔄
تغییر خودکار مدل:
اگر توکن یک مدل تمام شد، بلافاصله به مدل بعدی سوئیچ می‌کند.
•
📉
فشرده‌سازی هوشمند:
تا ۹۵٪ کاهش حجم متن برای صرفه‌جویی بیشتر.
•
🌐
دسترسی جامع:
GLM، Grok، Mistral، DeepSeek، Qwen و... همه در دسترس.
•
🛠
پشتیبانی کامل:
سازگار با MCP و مهارت‌های پیشرفته.
یک API، تمام هوش‌های مصنوعی دنیا. رایگان و بی‌نهایت!
🚀
🌐
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/6617" target="_blank">📅 09:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">10 میلیون توکن رایگان هوش مصنوعی Mercury 2
🎁
وقتشه ربات تلگرامیت رو با هوش مصنوعی ارتقا بدی!
✨
✅
مناسب برای ساخت چت‌ بات
✅
دسترسی فوری و رایگان
⚡️
همین الان فعال کن:
🔗
platform.inceptionlabs.ai
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/6616" target="_blank">📅 02:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6615">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9a7cbc953.mp4?token=lEziWagRcHlWiXlOv6dqpQQlhT2S9GGOKnu0Gbvhoyd7GYbjBIfpBFM5oNFONs2IDKMi4_5OaXL2ca_UB_D6l5-dABtqb3GiQYOkGtFhwcZCoq_KND8C5CeBNUFKWL8fiavXUwFKZB3abxy1EtQde1FW5irRJ83lMSWb_Fg_6zVFcSmrg8dCMBuoSvcQVVFW9cuRbrcH1EtHqo9bP-YfgGfrRLYyFWLmj-DtttHMyKzBUrDwLr7qzKw2DPnDJoL2e3R3ydTW_u3ebWT_QJPgynGUGG0g6UvEZgqLcBeMnZ8W2Ats-CbQFE49dGWc_wVjWjK3CVKRYNMvkFVSyCQfkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9a7cbc953.mp4?token=lEziWagRcHlWiXlOv6dqpQQlhT2S9GGOKnu0Gbvhoyd7GYbjBIfpBFM5oNFONs2IDKMi4_5OaXL2ca_UB_D6l5-dABtqb3GiQYOkGtFhwcZCoq_KND8C5CeBNUFKWL8fiavXUwFKZB3abxy1EtQde1FW5irRJ83lMSWb_Fg_6zVFcSmrg8dCMBuoSvcQVVFW9cuRbrcH1EtHqo9bP-YfgGfrRLYyFWLmj-DtttHMyKzBUrDwLr7qzKw2DPnDJoL2e3R3ydTW_u3ebWT_QJPgynGUGG0g6UvEZgqLcBeMnZ8W2Ats-CbQFE49dGWc_wVjWjK3CVKRYNMvkFVSyCQfkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#اختصاصی
🚀
معرفی PokieTicker؛ کشف دلیل واقعی پشت هر نوسان قیمت در بازار بورس!
📈
✨
اگر شما هم از دیدن نمودارهای شلوغ و کندل‌استیک‌ها (Candlesticks) خسته شده‌اید و همیشه این سوال برایتان پیش می‌آید که *«چرا قیمت این سهم امروز بالا/پایین رفت؟»*، اپلیکیشن فوق‌العاده…</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/6615" target="_blank">📅 00:42 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">#اختصاصی
🚀
معرفی PokieTicker؛ کشف دلیل واقعی پشت هر نوسان قیمت در بازار بورس!
📈
✨
اگر شما هم از دیدن نمودارهای شلوغ و کندل‌استیک‌ها (Candlesticks) خسته شده‌اید و همیشه این سوال برایتان پیش می‌آید که *«چرا قیمت این سهم امروز بالا/پایین رفت؟»*، اپلیکیشن فوق‌العاده و متن‌باز
PokieTicker
دقیقاً برای شما ساخته شده است!
🔥
این ابزار چگونه کار می‌کند و چه امکاناتی دارد؟
1️⃣
تلفیق اخبار و نمودار:
نقاطی روی نمودار کندل‌استیک ظاهر می‌شوند که نشان‌دهنده اخبار منتشر شده در آن روز هستند. با کلیک روی هر نقطه، متوجه می‌شوید چه خبری باعث آن نوسان شده است.
2️⃣
فیلتر هوشمند اخبار:
دسته‌بندی اخبار بر اساس تأثیرات مختلف (گزارش درآمد، تغییرات مدیریتی، محصولات جدید، سیاست‌گذاری و...).
3️⃣
تحلیل و پیش‌بینی با هوش مصنوعی:
با استفاده از مدل‌های قدرتمند
XGBoost
و
Claude
، سنتیمنت (احساسات) اخبار را تحلیل کرده و روند قیمتی سهم را برای روزهای آینده (T+1, T+3, T+5) پیش‌بینی می‌کند!
4️⃣
کشف الگوهای مشابه:
روزهای گذشته که اخبار و شرایط مشابهی داشتند را پیدا می‌کند تا ببینید در آن زمان بازار چه واکنشی نشان داده بود.
5️⃣
رایگان و آماده استفاده:
دیتابیس لوکال (SQLite) از قبل در مخزن گیت‌هاب قرار دارد و برای اجرای اولیه نیازی به خرید API کلیدهای پولی ندارید.
﻿
⚡️
مشخصات فنی:
*
بک‌اند:
Python (FastAPI) + SQLite
*
فرانت‌اند:
React + TypeScript + D3.js
*
مدل‌های AI/ML مورد استفاده:
XGBoost, Claude Haiku / Sonnet
﻿
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️
──────────────────────────────</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/6614" target="_blank">📅 00:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6613">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8393e8cd0f.mp4?token=oWkzBWYx7kMRfquOvd4cnnj4UQiVNGIHzwWZL_-exHnEFhsdsr8OV9IAxb-Tb06xdO7yftWnOxMni2Fphh9a3uHZpzknxX7aJwHofBNcLwd5xsOhxDDm5plqsKEu0pcHtBpkrNxEqThTH7LJqfUQLXJCDhptOl2qJFLnkEGdVNO2jwQoDR5MzcOTO0xHGr9LDA-lhiexRsFdzm6AvI6NWPATDU1mptI6N35RhNw14HcintxGC8SWQK47kQxWqLg9y7EBsQWNIEVyz2Ev130x-1WAuUn3pvtBNU6-wjI6FnNxHR3eo0pwUI3s2YidYpGCbEy5tCrwbe4ossAM1zvaAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8393e8cd0f.mp4?token=oWkzBWYx7kMRfquOvd4cnnj4UQiVNGIHzwWZL_-exHnEFhsdsr8OV9IAxb-Tb06xdO7yftWnOxMni2Fphh9a3uHZpzknxX7aJwHofBNcLwd5xsOhxDDm5plqsKEu0pcHtBpkrNxEqThTH7LJqfUQLXJCDhptOl2qJFLnkEGdVNO2jwQoDR5MzcOTO0xHGr9LDA-lhiexRsFdzm6AvI6NWPATDU1mptI6N35RhNw14HcintxGC8SWQK47kQxWqLg9y7EBsQWNIEVyz2Ev130x-1WAuUn3pvtBNU6-wjI6FnNxHR3eo0pwUI3s2YidYpGCbEy5tCrwbe4ossAM1zvaAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">DewatermarkAI
حذف واترمارک با هوش مصنوعی در مرورگر
این سرویس رایگان واترمارک‌ها را از عکس‌ها حذف می‌کند و فایل آماده را می‌توان با وضوح اصلی دانلود کرد.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/6613" target="_blank">📅 00:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YhHhrShpBVWH6_leB_Q2WsOB6bwUm1RNXWqDhsr5vOZr3oM0GtpGGIKovTNj9LR9gNRUfoWuRlmW8oz4ln_l9qAuQhz_5UBdkt5uk-wYydwbyGTWzW5T_42Esx2vaO_pPz7Q0_md-hE3ucyTUfz8DrWWin6irMyqREpaUML6jiNnC32NrQ46O3tb-D0HcalumHMv6A5SASP0QGO3UV5Na4Lbwn-kVeCRK5AaRW5-iAHrimnXahKghOMQNZnrFHNj_WmtTC5rtO-MzTxXfVZh2zNNp42jnMlN_ZuX98P1FJkW_0PgS7SWz3oA8jJYaoNPGyFX8tAU0mDkA3NbJeUBEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از به‌هم‌ریختگی اسکرین‌شات‌ها خسته شده‌اید؟ Trickle دستیار جدید هوش مصنوعی است که همه اسکرین‌شات‌های شما را به‌طور منظم سازماندهی و خلاصه می‌کند
فقط یک اسکرین‌شات بگیرید و آن را به Trickle ارسال کنید. هوش مصنوعی پیشرفته Trickle یک خلاصه دقیق تولید می‌کند که اطلاعات کلیدی مانند متن، نمودارها و یادداشت‌های دست‌نویس را استخراج می‌کند و سپس می‌توانید این داده‌ها را جستجو و درخواست کنید.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/6612" target="_blank">📅 23:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ORmNAFKt-mhKK6olikOp27jdD511sTK_wDkUSgiAMCG20iocY38ddHym4UOs9uZolwUctXvImckWq4Jql__8zXK5by2nEXIuxG_Lsn9rNuYv6MZ7gTnUn44cZCph1xs_L6k_CxPcey2gwmjGabxiXXt18-ZKDJmLX-vW9h8w12TC3jxuEa9-JllTsd1nK6l7CPuIfTbnDmCQWtwywCp6A8NjVXy5jk-rpFdWMSsNV7NWUa4vDgKGQt-8DNjy_SQvN6-LkgDb4vEulvftab2uDtMDMSRxTGaeiA5pvaxIkWM0HtlhopuUvikED1BJQP12AQcda54f0H3iMSqtVLcMow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧠
شورای خردمندان هوش مصنوعی: تصمیم‌گیری با قدرت ۱۸ متخصص
آیا از پاسخ‌های ساده و تکراری هوش مصنوعی خسته شده‌اید؟ با این ابزار، مسئله خود را به شورای مجازی فیلسوفان، دانشمندان و مهندسان بسپارید و تحلیلی عمیق و چندجانبه دریافت کنید.
➖
مناظره کامل بین ۱۸ کارشناس مجازی (سقراط، ارسطو، سون‌تزو، آندری کارپاتی و...)
➖
بررسی مسئله از زوایای مختلف فکری و تخصصی
➖
ارائه راه‌حل‌ها همراه با نقد و رد استدلال‌های رقیب
➖
دریافت نتیجه‌گیری نهایی بر اساس جمع‌بندی بحث‌ها
➖
تحلیل واقعی به جای پاسخ‌های کلیشه‌ای
این ابزار برای تصمیم‌گیری‌های پیچیده و نیاز به دیدگاه‌های متنوع، گزینه‌ای بی‌نظیر است.
🌐
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/6611" target="_blank">📅 21:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uEYICdrnrFTd_xZdGz1FG7WHSOF18VPqPjL5i3obPmu9OvWjoMWY_oXGa1B3RZe1roH0UgnLcYn-tL85mhQ4476YdlDUfRqW5Yb6lWPVpjQZqiGrcgeimGD_n_-sA4q2gOXWwG5Xf9DT6CXlyaxdKpuz-QqOkFzcDjbECWdDBT0gxt7jXzqb_bZ7O1y24EMhgnGAtdRIY0agSHigsYXUVk2LUFRCnyyKOjKqB8tlVs5wpE3Dd--pVETiAzx6TD_g3df9vGsGYjyhSF8-KI_wQEdYkHkC91AGIZuuWtobSHwYYxZSMcPJhJsfyy6V1xQfq627TRRBPcy0IINup570DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎵
OFPlayer: پخش‌کننده موسیقی محلی و حرفه‌ای
➖
پشتیبانی کامل از فرمت‌های FLAC و MP3
➖
مدیریت آسان کتابخانه و لیست‌های پخش
➖
نمایش متن ترانه (Lyrics) و کاور آلبوم
➖
تحلیل دقیق فراداده‌های صوتی
➖
اتصال به سرویس‌های WebDAV، Subsonic و Navidrome
➖
رابط کاربری ساده، رایگان و بدون نیاز به ثبت‌نام
این پخش‌کننده برای کاربران NAS و کسانی که مجموعه موسیقی شخصی دارند، بسیار مناسب است.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/6610" target="_blank">📅 21:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6609">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aG0ozci1GnCp61fZUYe2IFUXNqsNKrj4TNglWYYv59UmP4dNGA3_C2SIFRHsVo6irpAgok74EjR-R9lets7WDqEbj680CIu35hykhlr-FH4p8bKa4vHxDKWFINUAB0wAndzHJofZKTasMQVVn3oowQ2lVwqTWQG6wTBBV-2aCgjVsEf-ci-2R8BUrE5zp7MSzO1h3a-pATpRSzJBnRhFxsHefyPk-PmmwFqdRJDaD3qvkQrlRy_4ce4IsDg1XgGWP032hWG6wvPqWB8xZpQ38cy3fXN9braiecIQE-CH37FWjy4-4R2Pe9O5006NI9YoZicahVUSq3aTxyAT4mZF7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏋️‍♂️
مخزن کد با ۱۳۲۴ تمرین برای اپلیکیشن فیتنس!
اگه میخوای اپلیکیشن فیتنس خودت رو بسازی، این گنجینه رو از دست نده:
• ۱۳۲۴ تمرین کامل
• انیمیشن‌ها و تصاویر باکیفیت
• جزئیات عضلات درگیر و تجهیزات مورد نیاز
• دستورالعمل‌های گام‌به‌گام حرفه‌ای‌
پروژه خودت رو با این داده‌های غنی شروع کن!
🌐
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/6609" target="_blank">📅 19:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6608">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">خب Claude Fable هم استفادش برای مردم عادی کنسل شد
چینیا هم دارن مدرک جعلی میسازن تا بتونن ازش استفاده کنن
😂</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/6608" target="_blank">📅 19:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6607">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚀
تبدیل جادویی اسناد پیچیده به Markdown خالص با MinerU!
📄
✨
اگر برای استخراج متن، جداول و فرمول‌ها از فایل‌های درهم‌ریخته و پیچیده مشکل دارید، ابزار متن‌باز
MinerU
دقیقاً همان چیزی است که نیاز دارید! این پروژه فوق‌العاده که با استقبال بی‌نظیری روبرو شده و بیش از ۷۰ هزار ستاره در گیت‌هاب دریافت کرده است، اسناد شما را به راحتی و با بالاترین دقت به فرمت تمیز Markdown تبدیل می‌کند.
🔥
ویژگی‌های برجسته این ابزار:
1️⃣
پشتیبانی از فرمت‌های متنوع:
توانایی پردازش و تبدیل فایل‌های PDF، DOCX، PPTX، XLSX، تصاویر و حتی صفحات وب.
2️⃣
استخراج دقیق جزئیات:
بیرون کشیدن بی‌نقص متن‌ها، جداول و فرمول‌های پیچیده (ریاضی و علمی) از دل اسناد.
3️⃣
پشتیبانی از ۱۰۹ زبان:
قابلیت تشخیص و پردازش بی‌نظیر اسناد در اکثر زبان‌های دنیا.
4️⃣
کاملاً رایگان و متن‌باز:
یک پروژه Open Source قدرتمند و بدون هیچ‌گونه محدودیت پرداخت یا نیاز به سرویس‌های ابری پولی.
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️
─────────────────────────────</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/6607" target="_blank">📅 18:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PeN_uv8897iRiyX6SP8CImRZFE6kds-j1PSIyDPA7RPzZYcOpk9yHgu9-bq8hw4f1WHVkNTTjQ4zBWCTs66ya1gE-RzZDyGcxWAQcDN3DFOUecyzXbogpNe6QU-O-HESlhXJaYtjjgQAFt_DCNkFRb6hjFSXd_CQoVf5yKwR24t6dL9nabJagzdTRdfTbSL5hNBYhVILi6ck0LioOryyy3DkBCOdogNRNp1MQAGBCl1VUMT0vGUM-JjA1YvFKLm_ZYdsRJdv-XEpTrZaAr48QOYnCjIHypLO2nyf1CErDn_ppbtTSkrxR30d1ygMd_IXcpdFPGvXRo6uDgVTqp4pUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چینی‌ها ElevenLabs را کشتند!
💀
توسعه‌دهندگان ByteDance نسخه SeedAudio 1.0 را عرضه کردند که هر نوع گفتار و افکت صوتی را کلون و تولید می‌کند.
1⃣
ایجاد گفتگو با چندین شخصیت: هر شخصیت متمایز است، دارای احساسات، سرعت، تمبر و حتی لهجه منحصر به فرد؛
2⃣
دریافت تا سه منبع برای کپی کامل صدا، احساسات و سبک؛
3⃣
تولید صداها بر اساس پرامپت، مرجع صوتی یا حتی تصویر.
آیا این پایان دوران انحصار ElevenLabs است؟
🤔
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/6606" target="_blank">📅 16:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hh1lALAXXZ-0rRy19D9BzQE1-qFhAqCQ_gHtk-p4cB8UeRIq-kxhXM8mdwEUzHAt2DMMbvncqfKcdBwkScRZ75_lU99Pa519iSoqaFi4yQgS6rptDH0noesD8H3LUlvNIx_YLXIvLv9wmu6xOyc5chYP5oZMOSux7JvGIgSFevu5eWmhXGRBCZYpNUsWe94DQvGk0ceGxjdjSTlTNzPTHMBD8pFXGchqf4_bQI7rnQV9qSts1P0Cgi2Fn8ln0Aw13iskDrRLCdedT56bGPb5ibzCW97QBbfU4W052OCEAhxc0PR5d0UJrrlZdA4X0gMUzvHI_JZBb7eRy17Tl0ZExg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
تولید رابط‌های کاربری زیبا با پرامپت‌های آماده
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/6605" target="_blank">📅 14:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6604">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚀
معرفی IstanPdf؛ ابزار قدرتمند و آفلاین برای مدیریت فایل‌های PDF و DOCX!
📄
✨
اگر از سایت‌های پولی، تبلیغات آزاردهنده و محدودیت‌های سرویس‌های آنلاین تبدیل فرمت خسته شده‌اید، اپلیکیشن
IstanPdf
دقیقاً همان چیزی است که نیاز دارید. این ابزار کاملاً آفلاین توسعه یافته تا جایگزینی بی‌نقص و رایگان برای سرویس‌های پولی (Freemium) باشد. در این اپلیکیشن حریم خصوصی شما در بالاترین سطح قرار دارد و هیچ فایلی از گوشی شما خارج نمی‌شود!
🔥
امکانات فوق‌العاده IstanPdf (نسخه v1.0):
1️⃣
ابزارهای حرفه‌ای PDF:
*
Merge:
ترکیب و چسباندن چندین فایل PDF به یکدیگر.
*
Split:
استخراج صفحات دلخواه با تعیین محدوده صفحات.
*
Remove & Reorder:
حذف صفحات اضافی و تغییر ترتیب صفحات یک فایل.
2️⃣
تبدیل فرمت (Conversions):
* تبدیل یک یا چند تصویر به یک فایل PDF یکپارچه.
* استخراج صفحات PDF و ذخیره آن‌ها به عنوان عکس.
3️⃣
ابزارهای کاربردی DOCX:
امکان حذف صفحات خاص و تغییر چیدمان و ترتیب صفحات در اسناد ورد.
4️⃣
حریم خصوصی و امنیت مطلق:
کاملاً آفلاین، بدون نیاز به ساخت حساب کاربری، بدون محدودیت حجم و آپلود، و فاقد هرگونه تبلیغات و پرداخت درون‌برنامه‌ای.
🔗
دانلود
🔵
@ArchiveTell
| Bachelor
⚡️
──────────────────────────────</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/6604" target="_blank">📅 13:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6603">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hDBCTpVKG-WloaanFqwMKiIgcDJsop6l_s74Jl8qIfpy8RazTp9otBr4I5_TU4UtCprDqE6PYm0_baP8z_bs78-XRuSWzuPjrdYvrqAkK7WyfKGeTe1T-McDSVi9sHR8pDQb9dkHdlOzZjtLmJhMeDy9C3uj4i14bQ-QZ81-g7ufVj68I75gReVaBiQ_5M3nNL3mHoUSQo1F408x7eBjFRxr3sauV-Amx1BbuTwd5knsotJpyIW-vTocGICmG9XAwq7LWdtqm1kYbMvHJQK83hI5mW1GvNX1nXFI2e9-5ESTraUyBgUEj8J2QqNXAWSJDwzP132INAJ_5l6VlcT_3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
جایگزین رایگان و متن‌باز برای Claude، Cursor، Codex و سایر نمونه‌های مشابه.
✨
ویژگی‌ها:
•
💻
تولید کد برای وب‌سایت، اپلیکیشن و بازی در چند ثانیه
•
🆓
کاملاً رایگان؛ بدون اشتراک یا محدودیت پنهان
•
🌐
اجرای مستقیم در مرورگر؛ بدون نیاز به نصب
•
📝
فقط پرامپت بنویسید و کد آماده دریافت کنید
🌐
Site
#AI
#Coding
#OpenSource
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/6603" target="_blank">📅 11:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6600">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be7baa23f6.mp4?token=XKo0KmCVARM9XR3CT7KT_zxRyW-V80b170Vu2X9u6GCLWPZNHgK8xwJJ1TpWGEdWNmLMQRFivCMGMALtBxO918A9g-Pzc-reZCCKcBL9LUfLVdLkxzvUJA0EjKPIxRovb9avIkNZzqcvesm5_CTiKBTtMGhDxKk_J-65hY5qZyOxJaPr8sX6ZsXMoDHor7wSQ9mSef2rA7ITy3mZd5bUbL9sbIPqZUxBt5tRYjqDxeAp7WRaxd_umn5MWR3es11MSrTFog2l-M3IvCoabDp4vzfjNvTlHMo1xaPIPvi6mNDzFV0vco3zPrA-7kN0nEfsydlg7nqv5EKxbWpf72Ylug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be7baa23f6.mp4?token=XKo0KmCVARM9XR3CT7KT_zxRyW-V80b170Vu2X9u6GCLWPZNHgK8xwJJ1TpWGEdWNmLMQRFivCMGMALtBxO918A9g-Pzc-reZCCKcBL9LUfLVdLkxzvUJA0EjKPIxRovb9avIkNZzqcvesm5_CTiKBTtMGhDxKk_J-65hY5qZyOxJaPr8sX6ZsXMoDHor7wSQ9mSef2rA7ITy3mZd5bUbL9sbIPqZUxBt5tRYjqDxeAp7WRaxd_umn5MWR3es11MSrTFog2l-M3IvCoabDp4vzfjNvTlHMo1xaPIPvi6mNDzFV0vco3zPrA-7kN0nEfsydlg7nqv5EKxbWpf72Ylug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#اختصاصی
🔥
🔥
هر نوع رسانه‌ای را از تلگرام و حتی چت‌های خصوصی دانلود کنید
🤯
• دانلود صوت، پیام‌های صوتی، ویدئو، GIF از چت‌ها، استوری‌ها و حتی چت‌های خصوصی که دانلود در آن‌ها ممنوع است.
• پشتیبانی از دانلودهای چندگانه بدون کاهش سرعت.
• قوانین تلگرام را نقض نمی‌کند، می‌توانید با خیال راحت استفاده کنید.
🌐
GitHub
#Telegram
#Tools
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/6600" target="_blank">📅 08:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6599">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">دریافت 7 میلیون توکن روزانه AI به صورت رایگان!
🎁
🤖
مدل‌های موجود:
• Mimo 2.5 Pro
• Mimo 2.5
• Mistral Large
• Mistral Medium 3.5
💻
کاربرد:
• ساخت وب‌ سایت
🌐
• ساخت ربات تلگرامی
🤖
• کدنویسی در ترمینال
⚙️
🔗
NaraRouter
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/6599" target="_blank">📅 01:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6598">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">#اختصاصی
🔥
🚀
معرفی Metapi؛ هاب هوشمند و همه‌کاره برای مدیریت APIهای هوش مصنوعی!
🤖
✨
اگر برای دسترسی به مدل‌های هوش مصنوعی در سایت‌های مختلفی ثبت‌نام کرده‌اید، حتماً می‌دانید مدیریت ده‌ها API Key، چک کردن مداوم موجودی و تغییر دستی تنظیمات هنگام قطعی یک سرور چقدر کلافه‌کننده است. پروژه متن‌باز
Metapi
توسعه یافته تا به عنوان «پروکسیِ پروکسی‌ها» تمام این مشکلات را حل کند!
🔥
امکانات و ویژگی‌های شگفت‌انگیز این ابزار:
1️⃣
تجمیع تمام APIها (Aggregation):
شما ده‌ها کلید مختلف را به Metapi می‌دهید و این ابزار به شما
فقط یک API Key و یک Base URL واحد
می‌دهد. حالا می‌توانید این کلید واحد را در تمام برنامه‌های خود (مثل Open WebUI، Claude Code یا Cherry Studio) قرار دهید.
2️⃣
مسیریابی هوشمند (Smart Routing):
اگر سرور یکی از ارائه‌دهنده‌ها قطع شود یا مدل خاصی در آن گران باشد، به صورت خودکار درخواست شما را به یک سرور جایگزین، سالم‌تر و ارزان‌تر می‌فرستد (بدون اینکه شما متوجه قطعی شوید!).
3️⃣
دریافت اعتبار خودکار (Auto Check-in):
به صورت زمان‌بندی‌شده در سایت‌هایی که سهمیه رایگان روزانه می‌دهند لاگین کرده و اعتبار شما را به‌طور خودکار جمع‌آوری می‌کند.
4️⃣
حریم خصوصی ۱۰۰٪ و نصب آسان:
به راحتی با داکر (Docker) روی سرور یا سیستم شخصی شما نصب می‌شود و تمام داده‌ها فقط در دیتابیس محلی (SQLite) خودتان ذخیره می‌مانند.
5️⃣
سیستم هشدار پیشرفته:
در صورت بروز قطعی یا اتمام موجودی، از طریق تلگرام و ایمیل (SMTP) به شما نوتیفیکیشن می‌دهد.
⚡️
برخلاف پروژه‌های مشابه که برای تیم‌ها و فروش API طراحی شده‌اند، Metapi کاملاً برای
استفاده شخصی
بهینه‌سازی شده و رابط کاربری بسیار سبک و تمیزی دارد.
🔗
لینک مخزن گیت‌هاب:
🔵
@ArchiveTell
| Bachelor
⚡️
#AI
#API
#Metapi
#OpenSource
#Github
#SelfHosted
#Docker
#Tools
#OpenWebUI
#LLM
──────────────────────────────</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/6598" target="_blank">📅 01:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6597">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">#اختصاصی
🔥
🚀
معرفی Awesome Android Root؛ گنجینه‌ای بی‌نظیر برای روت و شخصی‌سازی اندروید!
📱
✨
اگر به دنیای روت، کاستوم رام‌ها و دستکاری عمیق سیستم‌عامل اندروید علاقه‌مند هستید، مخزن
Awesome Android Root
یک دایرکتوری جامع و بی‌نظیر است که بیش از ۴۰۰ ابزار، اپلیکیشن و ماژول مخصوص دستگاه‌های روت‌شده را به همراه آموزش‌های دقیق در یک‌جا جمع‌آوری کرده است.
🔥
امکانات و ویژگی‌های کلیدی این لیست:
1️⃣
آموزش‌های قدم‌به‌قدم:
راهنماهای کامل و دقیق برای آنلاک کردن بوت‌لودر (Bootloader Unlocking) و نصب کاستوم ریکاوری‌ها (Custom Recovery).
2️⃣
پشتیبانی از جدیدترین متدهای روت:
پوشش کامل و معرفی ابزارها برای روش‌های مدرن روت سیستم از جمله
Magisk
،
KernelSU
و
APatch
.
3️⃣
کالکشن گلچین‌شده ماژول‌ها:
مجموعه‌ای از بهترین و کاربردی‌ترین ابزارها برای مسدودسازی تبلیغات (Ad-blocking) در سطح سیستم، اتوماسیون وظایف و شخصی‌سازی عمیق رابط کاربری اندروید.
⚡️
مشخصات فنی:
*
زبان:
Python (برای مدیریت و استخراج داده‌های لیست)
*
پلتفرم:
Android
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️
#Android
#Root
──────────────────────────────</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/6597" target="_blank">📅 20:36 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6596">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">سلام
دوستان اگر به وایب کدینگ علاقه دارید یه نگاهی به این سایت بندازید:
https://risman.pro
برای ساخت محصولات فنی میتونه خیلی کمکتون کنه. (بدون نیاز به هیچ دانش نرم‌افزاری و برنامه‌نویسی)
امکان انتشار در دامنه خودتون هم بهتون میده.
با اولین لاگین حدود ۱۰۰ هزار تومان توکن هدیه میگیرید و اگر خواستید توکن بیشتری مصرف کنید میتونید از کد تخفیف welcome برای ۵۰% تخفیف تا سقف ۱ میلیون تومان استفاده کنید.</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/6596" target="_blank">📅 19:12 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6593">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/akpCkWZGTl3xmY_5a2M1mdinpZbUlx7Si_DEU05BByUWmTOG5r7EJzHBdofQT_blYN3OHSvcKQj7k-T_9ORYE26iDmj17Xh-aAK47GxQuG8pEg04sOk2uHHmKgUhLjJMzH3v8hpYVBsy3v628Vy_fUwQdpnWy0aHxmduzs24T3u0RASneDUtZrLGl20kb2M2u0A1kJLz9C3Jgxe6TmJxGYB7AX-Thi560qMBCTPwBnJljqqIOipDLw4ia30Ho4wXmvLqXJyjEewb-gHbVfuTVlwm-mXWTditCf22f3T8xhl88pQdpEYlxj3IzWE9fKiUEWLmZ15mQQCmdPO1IYAZMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابلیت ست کردن پراکسی لوکال
خیلیم ساده
مرورگر باحالیه
🔥</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/6593" target="_blank">📅 15:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6591">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jhHX-5aytaOuBX0pdMCIXDCjx7wMeVdKIzF1N4UVCQZXmBJDdnpau_K94QTlm16w8N_CwOQTKeg992IBo5PC4p9dmzESd09L8mDvz-tLdxO39QJhyB9dbtZzqoLYxwIySVWrGgoIoH_qebTMSW-qdHBhKr7PBJ2tpirqL9644r0uJYpy4hfi7g8orOiJBpVoi8QevO7Y8MH_NhUtoENqU6RbUneLtMW7hDsIbBOPXFu4fB9VUBXgw3BDbY4kpx3LfAbmTC191jCAnZHZAS7DsPHmoejsNF23ND6T2dnbecME6I66rGBAwtrXdT7lgk5TjriOrxedOQB8bpruCfQEFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی مرورگر Solipsism؛ وب‌گردی با طراحی منحصربه‌فرد و متمرکز بر حریم خصوصی!
📱
✨
اگر از ظاهر تکراری مرورگرهای موبایل خسته شده‌اید و به دنبال مرورگری خاص، قابل شخصی‌سازی و امن می‌گردید، اپلیکیشن Solipsism یک شاهکار در طراحی رابط کاربری است. این مرورگر اندرویدی…</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/6591" target="_blank">📅 15:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6590">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚀
معرفی مرورگر Solipsism؛ وب‌گردی با طراحی منحصربه‌فرد و متمرکز بر حریم خصوصی!
📱
✨
اگر از ظاهر تکراری مرورگرهای موبایل خسته شده‌اید و به دنبال مرورگری خاص، قابل شخصی‌سازی و امن می‌گردید، اپلیکیشن
Solipsism
یک شاهکار در طراحی رابط کاربری است. این مرورگر اندرویدی با ایده خلاقانه "Rail-first" تمام کنترل‌ها و نوار آدرس را به جای بالا یا پایین، در یک نوار کناری (سمت چپ یا راست) قرار می‌دهد تا کار با گوشی‌های بزرگ با یک دست بسیار راحت‌تر شود.
🔥
ویژگی‌های شگفت‌انگیز این مرورگر:
1️⃣
طراحی نوآورانه (Rail-first):
قرارگیری منوها در نوار کناری با قابلیت تنظیم اندازه (از کوچک تا Super Compact) متناسب با اندازه دست و صفحه نمایش شما.
2️⃣
زبان طراحی Material 3:
رابط کاربری بسیار زیبا با گوشه‌های گرد، انیمیشن‌های روان، سایه‌ها و قابلیت هماهنگ‌سازی رنگ‌ها با تم سیستم‌عامل اندروید.
3️⃣
ابزارهای قدرتمند حریم خصوصی:
دارای مسدودکننده تبلیغات (Ad Blocker)، وب‌گردی ناشناس، کنترل کوکی‌ها و WebRTC، پاک کردن خودکار داده‌ها هنگام خروج، و یک قابلیت بی‌نظیر به نام
Decoy Mode
(تولید تاریخچه وب‌گردی جعلی برای محافظت از حریم خصوصی!).
4️⃣
امکانات کاربردی و سریع:
دارای اسکنر QR داخلی، قابلیت نصب مستقیم وب‌سایت‌ها به عنوان اپلیکیشن (PWA)، پخش تمام‌صفحه و بدون مزاحمت ویدیوها و ابزار دانلود حرفه‌ای.
5️⃣
صفحه خانگی شخصی‌سازی‌شده:
امکان تغییر والپیپر هوم‌پیج یا تنظیم آن روی حالت کاملاً تاریک و بی‌صدا.
﻿
⚡️
این مرورگر سبک که بر پایه WebView اندروید ساخته شده، تجربه‌ای کاملاً متفاوت، سریع و مدرن از وب‌گردی را به شما ارائه می‌دهد.
🔵
@ArchiveTell
| Bachelor
⚡️
#Solipsism
#Android
#Browser
#Privacy
#Material3
#AdBlocker
#WebDevelopment
#MobileApp
#TechTools
──────────────────────────────</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/6590" target="_blank">📅 15:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6589">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚀
هوش مصنوعی دیگر کدهای شما را فراموش نمی‌کند؛ دستیار حافظه دائمی برای ایجنت‌های برنامه‌نویسی!
🧠
✨
اگر از پریدن کانتکست (Context) در چت با هوش مصنوعی و توضیح دادن‌های تکراری خسته شده‌اید، این ابزار جدید مشکل شما را حل می‌کند! به تازگی یک دستیار هوشمند برای مدل‌هایی مثل Claude، Codex و Cursor منتشر شده که دانش و اطلاعات پروژه شما را بین سشن‌های (Sessions) کاری مختلف حفظ می‌کند.
🔥
این دستیار چه کارهایی انجام می‌دهد؟
1️⃣
حفظ همیشگی کانتکست:
اطلاعات جلسات کاری شما را ذخیره می‌کند تا با بستن پنجره، کدهای شما فراموش نشوند.
2️⃣
یادگیری ساختار پروژه:
معماری، دایرکتوری‌ها و ویژگی‌های خاص کدبیس (Codebase) شما را کاملاً به خاطر می‌سپارد.
3️⃣
بسته‌بندی خودکار دانش:
اطلاعات جمع‌آوری‌شده را به صورت خودکار و هوشمند بایگانی و بهینه‌سازی می‌کند.
4️⃣
بازخوانی در کسری از ثانیه:
هر زمان که ایجنت به اطلاعات قدیمی نیاز داشته باشد، در کمتر از یک ثانیه آن را فراخوانی می‌کند.
5️⃣
پشتیبانی بسیار گسترده:
سازگاری کامل با
Claude Code
،
Cursor
،
Codex
،
LangGraph
،
CrewAI
و سایر ایجنت‌های هوش مصنوعی.
🔗
لینک دریافت و راه‌اندازی پروژه
🔵
@ArchiveTell
| Bachelor
⚡️
#AI
#CodingAgents
#Claude
#Cursor
#Codex
#LLM
#Memory
#ProgrammingTools
#DevTools</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/6589" target="_blank">📅 12:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6588">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lki64p03sMdf2LUP6LoufDFDpAjABUIztXExddem-4jfAtF6HyJz3MC6hH1mgMFymzopiRvYgo3auNM8cCF9ReQkD5Nd914igj90v0kc-bXAR6nZyOcFVw4tynZBrQqyM56yreW1Mx6JV3uFPqFbCp-gcOYMe3EaBQs52MBIF4eSYJ39oIRokg0cYpXKg_8u85f9quzmRcqW_FmopeOmMAUujvuiIgiglRz7gIdEtYu-A5aGFNwc_nYHoxqaXDIAT6d1GpWjsNEVWz6eNmm2lduasla32P57BTE_oO9uqJyGcLK_I2eE746hR_psy9IKAC84UDtqbzd97pT_fZitmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت 1T کانفیگ شخصی
🔑
🟢
از لینک زیر میتونین شروع به ساخت اکانت کنید :
➡️
sign up
بعد از ثبت نام وارد اکانت بشید و روی
Quick Subscription
کلیک کنید و داخل اپ هایی مثل :
Nekobox,hiddify,singbox و ...
اکسپورت کنین .
به دلیل نوع پروتکل یعنی AnyTls بودن فقط داخل اپ های ذکر شده میتونین اکسپورت کنین و داخل اپ هایی مثل V2ray کار نمیکنن
😬
خط های تست شده :
🛜
🛜
💬
@Archivetell</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/6588" target="_blank">📅 12:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6585">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JUhGUx6BLdcgCAuL2-7qggK7fTni-F0Twlkv3m7Rn20VcZ1bBUTEaX9_Pam9xTB7rO3D_X34mAmotCt1rC4K5T7vM8EkxD8fDLA5KE5MjOpkwZ3dnSK6yXce5GUlboT_8rUEcJCGYgouILJD143TZuIFIpIz2qdF1Xlay310aIhxWuXGgaL-u9BReZT2wE9IPYGLH6pWdDhAuWiJtiP53hyLltLTyHlRWlrz5r5iQhc4EFfowo5zAOjSBxnHuJq8Iy8JGXzo2ZuH1AllHyD9fgq2p3nfGZYL92DxBOwRbn26zh5ap3_DL82PaYiutZCNrcqrhL6NEfLCGNmHGtX1ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GsJc4iUMbQMvuquuvlmPKey1acmeyO1VC1RIoSpgGFVWVpxbVZp-w72VW0eoni-px_OpCzb0Ld_EKU2X-ni16Rzmb6Gk0s9stG4-nJx-cXCNEImnpYtgdWNODiuZFMeagMH1ftE4dqw3G-fc4EfGpy3I5RuNhKejSN27Jtaw1ahxaSrGdcC4A4VEXBtL8nfwkgYOEH6vQxftBLzFDrVNFxxCLZzre5U8AyIPwJzh4H2_ykuDcA0iQScTy6-z9KtynCQjXlHXp12_PMUN8KOMT05j9ZclZBxqO53gf_7QDt1kktq7TpYatk0jrP0oflzj8TKrcWQRxa-Z1HKfcWKxxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nRNuERT9xJtyJGgY_ISvvMkn1Q_U6S98sFnTAKUlbOW64br8PvP5ztU7Lj3y8aXLH6IwDUH_C_RM6bjWFWk6mjpDFXPVeJUBR5hfmoTEibEZLHLBkrO16RMpgY7pXU8NQq3_FceguN-hvy6ji9toPk9rsMOjLyuV_K5g9wr_oqW6EV5Xl5H72FptOfk0HJEI7XsM7SDkjsvfTxY1o9vsexY_SaPv0mip4cMbI0KWdGHaYYPyArtTzfnYEoMc15jC91-WicdE6ygMrIazPErkuocCi4mTLsQ4QiTl-IU0SwBfq0MjXsHxttSH8kCN1NAcNGtIGxyuEEXAGX8Ccxv59Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تبدیل عکس‌های معمولی به شاهکارهای هنری با هوش مصنوعی
🔥
✨
قابلیت‌ها:
•
🎨
انتقال سبک هنری (مثل ون‌گوگ) به تصاویر شما
•
🪄
انتقال سبک بصری یک عکس به عکس دیگر
•
⚡
مبتنی بر شبکه‌های عصبی کانولوشنی و الگوریتم‌های پیشرفته
•
🛠️
رابط کاربری ساده و سریع برای ویرایش آنلاین
•
📦
بدون نیاز به نصب نرم‌افزار سنگین
🌐
Site
#AI
#Art
#Tech
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/6585" target="_blank">📅 11:00 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6584">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6YgcfdsoEVjT0faH9WvNKR_tR2B_o0RNLdDKf5RLHxXBA5KaMaGH_0vos0oTyGmmIEqmi0oNq6yVv1yOCTrCoIKiPG4Ae1YlQ8iVa6vDttfjDydx8KSnMmBXsmmJ4v6dwBqJeDVeIkhMCuqK4Qek8Yp1G_VKh-U6_-g0gD8k6zuLASQsCD6oxTk-2sasXMtUVc998drsdZTOoZDECc3g2iBqWqcwvCBMKu8Tei2MOYg-FZbo3j11VyazUBdAGsHQcxHn17kmqm6k9XIfDZjWA6IPcHyqFO7_0zVMUeJzUxqCzY3oTmj0s2UvtV28dUCXw6qwTrdtJ-exgYvNmIHjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویژه
🔥
🚀
معرفی Orcafile؛ ابزار جستجو و دسته‌بندی سریع فایل‌ها بر اساس پسوند!
📁
✨
اگر از گشتن در میان پوشه‌های درهم‌وبرهم برای پیدا کردن یک فایل خاص خسته شده‌اید، پروژه Orcafile دقیقاً برای شماست. این اپلیکیشن دسکتاپ و متن‌باز (Open-Source) به جای اینکه شما…</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/6584" target="_blank">📅 09:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6583">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ویژه
🔥
🚀
معرفی Orcafile؛ ابزار جستجو و دسته‌بندی سریع فایل‌ها بر اساس پسوند!
📁
✨
اگر از گشتن در میان پوشه‌های درهم‌وبرهم برای پیدا کردن یک فایل خاص خسته شده‌اید، پروژه
Orcafile
دقیقاً برای شماست. این اپلیکیشن دسکتاپ و متن‌باز (Open-Source) به جای اینکه شما را مجبور کند پوشه به پوشه بگردید، کل یک دایرکتوری (یا حتی یک درایو کامل) را اسکن کرده و تمام فایل‌ها را بر اساس پسوندشان (Extension) گروه‌بندی می‌کند.
🔥
ویژگی‌های کلیدی Orcafile:
1️⃣
اسکن فوق‌سریع:
قابلیت اسکن بیش از ۱۰۰ هزار فایل در پس‌زمینه بدون افت عملکرد سیستم.
2️⃣
مشاهده لحظه‌ای پیشرفت (Real-time):
نمایش لحظه به لحظه وضعیت اسکن فایل‌ها.
3️⃣
جستجو و فیلترینگ هوشمند:
جستجوی آنی نام فایل‌ها و فیلتر کردن دقیق بر اساس فرمت و پسوند.
4️⃣
دسترسی سریع:
امکان باز کردن مستقیم فایل‌های پیدا شده در فایل اکسپلورر ویندوز.
⚡️
مشخصات فنی و
پلتفرم:
توسعه‌یافته با ترکیب قدرتمند
Python
و
PyQt6
.
نسخه اجرایی (App) در حال حاضر فقط برای
ویندوز
منتشر شده است، اما از آنجا که پروژه متن‌باز است، با استفاده از سورس‌کد و دستورالعمل‌ها می‌توانید آن را در هر سیستم‌عاملی (مثل لینوکس و مک) اجرا کنید.
🔗
سایت پروژه
🔗
لینک مخزن گیت‌هاب:
🔵
@ArchiveTell
| Bachelor
⚡️
#Orcafile
#Python
#PyQt6
#OpenSource
#FileManagement
#WindowsApp
#Github
#Tools
#Productivity
──────────────────────────────</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/6583" target="_blank">📅 09:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6582">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f93c42b223.mp4?token=g7dUOkI6UgX9k5MmdO48515YQY4vhY2xAosxtw5rQnOb6jChKoOxpGBG3-nN9Ynl2VnqwACNlHzzVd1G02mQOm4wIv-Pga3IWlxqLf3RyyiaNdCxNrJLeC9o47MCCSeODlO3gsimnnRMM8uyN_mmNjkyZYzhRUef5D7Q4GLVFSj_9zW42R_Sp2QaQ_ANTL0VemsH9Dwv679D109woCCWVrgZurraMzstxOKlLZPugRDAy2jIXiGCyQhDxTSynWCc-4fB0NCD7I0-6tkTJR1UjDDCH7UP-oSUqKZCimguRf0xeSp8YwYWw5mIVPjKStOcNcyWYDFeNpMvs5y3PHlxUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f93c42b223.mp4?token=g7dUOkI6UgX9k5MmdO48515YQY4vhY2xAosxtw5rQnOb6jChKoOxpGBG3-nN9Ynl2VnqwACNlHzzVd1G02mQOm4wIv-Pga3IWlxqLf3RyyiaNdCxNrJLeC9o47MCCSeODlO3gsimnnRMM8uyN_mmNjkyZYzhRUef5D7Q4GLVFSj_9zW42R_Sp2QaQ_ANTL0VemsH9Dwv679D109woCCWVrgZurraMzstxOKlLZPugRDAy2jIXiGCyQhDxTSynWCc-4fB0NCD7I0-6tkTJR1UjDDCH7UP-oSUqKZCimguRf0xeSp8YwYWw5mIVPjKStOcNcyWYDFeNpMvs5y3PHlxUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💻
JanAi
جایگزین محلی ChatGPT
این برنامه مستقیماً روی کامپیوتر اجرا می‌شود و نیازی به اتصال به اینترنت ندارد. می‌توان از مدل‌های زبانی مختلف برای متون، برنامه‌نویسی و سایر وظایف استفاده کرد.
🌐
Site
#AI
#OpenSource
#LocalLLM
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/6582" target="_blank">📅 09:16 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6580">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j1tTkM5UMWJVMZi-gPul4JRPtMX2OPbmNgqRJWEALX02MwSFFxBsBLRSVVi_jTk7L-qjVDNchSjoZIBT6GmhTY_vay3If8_JV2NnYouA30KkWL-RgIwEo_t5dJHsfv_wiOCXpxa-wmt9_0DJzrrPikFghL8u0BnT2e6ifQ3yva8ohA5JffJgbBrUp_xoJOkXosRt9Cbz5vgEmi7XSt8BEVUlrECZvSpJCcZxO_oqOQmtddmfUic5u2xLvHJmHr-OpAZFCFdcULEVH2G7Pe5i8Iv3Igw7IY6ou11u_wYLqZL3ZJFBTm3lssoW4OOl0N239zqf5xHdyON7nP1ng7U0Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fA4fRhsLrxlKBhXPCdeJo6F0z4nGwYrs2hZHb9x8CvZymAMK2Snv8rkpy85mBsdcDnW1YglU19qK4CPQWHighEEDMZ-kb6j3-4tOb7naGCXj6CaPinbhrW3_45aw5qnxzetv6MHfy3HxJ3yuTCaYkuAAi-qvzYJxhePtbEDcoilx7qoO8didRWkUHcbHV0O_LSNcLev7BqDSMkZGt6xrrEoXSj6GkGF1Z6uyhktdU7cvXW5OSrt0gOoCyhcDGQJ5wjkUMFyPvZKS7nO5JAeV5ZWsGZg299NRGPFRN8HA2rw3lgIpkS_Ms1yBQNHRTIGmwTyzoibWhhO0ToPiDMXWFQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
«انجمن‌ها» به تلگرام اضافه می‌شوند — در نسخه آزمایشی برنامه چند ویژگی جدید پیدا شده که عملاً پیام‌رسان را به دیسکورد تبدیل می‌کند.
• در انجمن‌ها می‌توان چند گروه را در یک فضا ادغام کرد، چت‌های عمومی و خصوصی اضافه کرد و همچنین دعوت‌نامه‌ها را به آنجا ارسال کرد.
• همچنین می‌توان کانال‌ها را به انجمن‌ها اضافه کرد، اما این ویژگی هنوز فعال نشده است.
تاریخ انتشار به‌روزرسانی بعدی هنوز اعلام نشده است.
#Telegram
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/6580" target="_blank">📅 08:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6579">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">طراحی وب و اپلیکیشن در یک ثانیه با ابزار جدید GenSpark
🚀
✨
قابلیت‌ها:
•
🔹
تحلیل مستقیم فایل‌های Figma، عکس و کد
•
⚡
تولید طرح نهایی بدون نیاز به کدنویسی دستی
•
🛠️
دسترسی به قالب‌های آماده برای وب و موبایل
•
📦
ساخت رایگان نمونه‌کار برای فریلنسرها
🌐
Site
#AI
#WebDesign
#GenSpark
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/6579" target="_blank">📅 00:06 · 06 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
