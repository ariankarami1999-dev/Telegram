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
<img src="https://cdn4.telesco.pe/file/uhDvF0Gd3UEBtEBFl4Yp7Sh3i_muUp38zvdlXLEKhGwsCO4Ia8JfvG34n7f23tFfktpfRgkygpIhV9EDe_JocDXI037w3kc47LmuKryf5dRDQh6pRb7vApZMvyt9YWo7sTaQ3B4Le138NoBtqwFFM04DJ0-y_wx8KK71UMidxZ38dfLtUAVygO2-GAfzrMxg-IJEWKMp4Bv-o03ShPmVM3v-U9REKx8EBRwDZJcHkXLRwoDflmxT852VRvjgKHrAONAnk_15mMLOvMtILUjhDlz8jxqEL_2-er1RINOdbdc8KpLlMrtAjQEgKg0kCvB4lUzADkKyMbtWlCgTZyXukQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.3M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-27 10:24:21</div>
<hr>

<div class="tg-post" id="msg-672458">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bEB0F2Mv74IrE2bbXJLX9KZEJa1dGtH0Ulev_A8jGKclLb3iV_AkAlFKiifQhDqJ8o_QX4yE2EgsNZgFQMD6fR06VG4qvLaku7YoYWOZlkfr2tDdkBxoTqPNgGmgEvIW8w21zIPot4vjHs4WRoIg2yQNXw_sNPch8MDDAylITpofqR2-yndRelCPGFCf_GCf-0Uii6dI1F6G6xiDP2GKyaBEuRyUn4f2n_hyiPSgdhczGiUTE0d4YzICNtUNmGfjcNtLBHPugYV42YGKKO8fBbAsR1MzAjEk65uvsBDZEP3aIC9Upk_2YsZFNF99ymdXmYGQBtzTT72n9JWUdSfXrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیژن مرتضوی، خواننده و آهنگساز ایرانی مقیم آمریکا با تصمیم فیفا در بین دو نیمه فینال جام جهانی ۲۰۲۶ به اجرای زنده ۱۱ دقیقه‌ای خواهد پرداخت
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/akhbarefori/672458" target="_blank">📅 10:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672457">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sTZdCae-ql7McKY8ls4XfgTN1_WY_NSQhcGPU-AFbrCjCvuCV5Dsj5q-azJ92xVupYKF5v-67aO5LM1dn1pyu1pnyb60CHUuYGMcEhvlCqjIqDd3ZHr8MP9R3MoOoaeZGk_nSAooYT6VeLoVThClxWvDp7u46GJkoLrqwgYJwKbiacLH2KjEhG1f3_8cCxOvghQ-7VARUu1TZ2T8fwx-DzA-XHi3ESp1BWLz-Lc9TE5bUXqEFHIQMmeD6wuROpdTrpJnahcyeAYarVZby3s5w7ks8e5eBpogHhM7gYB9NLPEvwQtzHg_PhwYtAGcWtHoCwkgGynlh_fEJs-gEYJNVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گوگل در اقدامی هماهنگ با ارتش تروریستی آمریکا، تصاویر ماهواره‌ای مراکز حساس کویت را محو کرد!
🔹
گوگل تصاویر ماهواره‌ای با وضوح بالای نیروگاه برق الشعیبه، تأسیسات آب‌شیرین‌کن الشعیبه، چند پالایشگاه و مجتمع پتروشیمی و همچنین بندر الشعیبه در کویت را محو کرده است.
🔹
این تأسیسات در هفته‌های گذشته هدف حملات ایران قرار گرفته بودند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/akhbarefori/672457" target="_blank">📅 10:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672456">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d419140269.mp4?token=SU65-liw0weIsDKu9I6BaLRMZRM3_LZq0VDtMFIe9ACaO9Hrjj5eC9tC5a6VnjhkSdXlQrcIi7RxrJNR2_JHwcFMdOkYd92toOhtFtwysX93dsHrdOK6VOarABoTceIENCIqz0yJn4y2jSE_HZL81vuAXbmF16Tmwe_BSlKtMYXSZ_mnylJ5a0kOrvZB-tndr9tWU3mjpYX_K18eNsijXsUD9SK5LVlBWJvD6sinKjW0ANtDD-pdb5bU1MaMTW_30mE0rTNjVpBbhNEGsqsiYOgfUHwhtroa6rOC_0gkyXVzrmCMEFfnZqItXWuacArKE4cktkWarnUI5MR9LTdEC7PElmLabLvfnPBncVnMazp6YrZu57N_4y2n_hH1xPDlX1d5HoxvuifTnqht5kiEggGYkEdgacxDMQJBWBKQV2UmhVoKFPnfjvcJX6vLQuzMB43BULcr4plr8jJhGrd_bZG56kfOuM0GmqtEkQI7xrRj0TDLTS-7p4v_T4Uj6I5HHbetxKin5k5Ht0GC0FFfao7ChaJlr9RdfZiEigsrtFfhKMDX5ZDW34cRV-Ur4ftaul0nns-6atZn3cU0RxTcLlSIQhzt0ZagStafhKX_yccM2i73utjIFeLbxNKox7hwgwzS13xVq9HIwQa0MkerZyQcT7cIv8XDnjqZe5aXKjs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d419140269.mp4?token=SU65-liw0weIsDKu9I6BaLRMZRM3_LZq0VDtMFIe9ACaO9Hrjj5eC9tC5a6VnjhkSdXlQrcIi7RxrJNR2_JHwcFMdOkYd92toOhtFtwysX93dsHrdOK6VOarABoTceIENCIqz0yJn4y2jSE_HZL81vuAXbmF16Tmwe_BSlKtMYXSZ_mnylJ5a0kOrvZB-tndr9tWU3mjpYX_K18eNsijXsUD9SK5LVlBWJvD6sinKjW0ANtDD-pdb5bU1MaMTW_30mE0rTNjVpBbhNEGsqsiYOgfUHwhtroa6rOC_0gkyXVzrmCMEFfnZqItXWuacArKE4cktkWarnUI5MR9LTdEC7PElmLabLvfnPBncVnMazp6YrZu57N_4y2n_hH1xPDlX1d5HoxvuifTnqht5kiEggGYkEdgacxDMQJBWBKQV2UmhVoKFPnfjvcJX6vLQuzMB43BULcr4plr8jJhGrd_bZG56kfOuM0GmqtEkQI7xrRj0TDLTS-7p4v_T4Uj6I5HHbetxKin5k5Ht0GC0FFfao7ChaJlr9RdfZiEigsrtFfhKMDX5ZDW34cRV-Ur4ftaul0nns-6atZn3cU0RxTcLlSIQhzt0ZagStafhKX_yccM2i73utjIFeLbxNKox7hwgwzS13xVq9HIwQa0MkerZyQcT7cIv8XDnjqZe5aXKjs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از پل‌های غرب استان هرمزگان که مورد حمله ارتش آمریکا قرار گرفت
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/akhbarefori/672456" target="_blank">📅 10:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672455">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BxQdGkrHF5uThoqEPyTlJ-Ov8Lr_hEG4zSjKvDGrjzgWDmFlNxmdAZJ0heJPJP3gDr9qKT3HImD2XV_QWghCSf_8HUKNqJpY8eWe_FPERMpXMWoQAX-lulFwpi3bwm1n0aKEpLqn618LQ8uO3i7tOKW3m9PrDBifQeeTz_taXrXYyALVpmmny7wIu9qfEy-wET54bbuGMC1IjXrC8wlQDM-4o92xXE4W2fCzlKJA7eR1gehcx6jYYE2RKujbeog8QGDF5hRKsW0rZT1hoWBZBNWuKC7_20bvW4v6_mMdHnhIMvzPZtcP8EEC0low2aP75jF0QGO36FUn06Mi4POxAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این‌بار پاستا رو به سبک انیمیشن باد برمی‌خیزد درست کن
🍝
مواد لازم:
🔹
اسپاگتی ۲۰۰گرم
🔹
گوجه‌فرنگی ۴عدد
🔹
سیر ۲حبه
🔹
روغن زیتون ۲قاشق غذاخوری
🔹
ریحان تازه
🔹
نمک و فلفل به مقدار لازم
🔹
پنیر پارمزان اختیاری
#آشپزی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/672455" target="_blank">📅 10:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672454">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
سی‌بی‌اس: مقامات آمریکایی اعلام کردند که ایران در این هفته دست‌کم ۲ پایگاه در اردن را هدف قرار داده و چندین نفر از نیروهای نظامی آمریکا مجروح شده‌اند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/672454" target="_blank">📅 09:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672453">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
ادعای کویت درباره حمله ایران به نیروگاه و تأسیسات آب شیرین‌کن
🔹
کویت مدعی شد در جریان حملات موشکی ایران، یک  نیروگاه و تأسیسات آب شیرین‌کُن این کشور به شدت آسیب دیده است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/672453" target="_blank">📅 09:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672449">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bYH8ElMt-L4XzSFoBDxWUfaciyyL8_nNTyvoCQe21XkZ-F6_tlibE1haVMhB5Don8Axc7aY1RjdGuEBAwJ2DBaz-gXSNdGbVERKCSZYAEDI1eKKl0i1BaFZ1CsLl_IdtDXOhRNgjd2F-BS12IACdZ0Us84yQdxUCRuMLsD5o-HAdybIyordQnLVE9grbLR7PSszSYK_ysUo6RzRjEOtWBNGo0drynkg1uEwnCU6iI4O9XE1EadhB5y51gXxXFmtauAehb99s4pJl69k7yH6exqu1Rb9qG1DngrqfTY9nwCXEqJjylTcLig_D2PJkpzSu9FVz7-GjiGKQx-da8m3xvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pqe8wEzIfJDXmYuJjGzrf5PRZ4J5GzjwyYPuo9GctDoLH4L_6j55uM8uYUexpvpKScSLC1Zzf1-howf5rPljJO8kifEI9vt9n41Hi4VmGVQrHR1dZZ6N3hOM5r96SCJDtUS1WXE6e8GMHygfTbfI20R3z5GR0OPvrYbMKkJV9OBK0ksFKO8JwWe1K9kTcOi8IL6fScxpvxWb9JXkNZ7Gce_AbFSBYn3uszNvPBiy7BASw9B9E-46SQynO6oL-j_RPiQyD5tQh80NglqwcyFMmM51Y0Owag7XqYzHrrTG4FAsmeCLDW4IdLrohSOAt09fLbzYqJ6ST3oywQNAid5FBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iL_Eucv_U36snKhhaK-9UsN9c0xLV0NhyE61ffaP8da_7kH8TqTQLHNrUqE0rT9iUHM473HnVLheL4gdO3gvIp5ku8EXI5bRQY4O8gubd6XjT7AUl2UNeCqIPoZ6-iPNYhDupndjmGwOlP7c3yH58cnH1JOLW2L68ZdZ2mRjcC9nkdK6QuVBmq9LCwEhcWgiGr-hxbFDbqlwrb4zODzQYKeipSW8bPkbtwUZYIkeJftksghcuSUbMW6SmrqtmBe4wU7E0vjnDIeJBO7vwxhyR5gqwDthnQHV-9DUJx23VQA_vFoUlNAKRe6jWFnnM9P-r2BAJTqgWTckPu-QaoB_8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XR-azpkJQxqz_FEbridrWfNuQ6S95fdaacRDn9xjSHxAii36kW3XqIMkOzc_RGP30ZrK5_mtIZMgfMyE45qiDLsZOSnKIbhmvO9klZ8eNVG9FEvfsM5ly7F1MAYFnb4iaCq7r4XTOY12ArdTItyKksJb2wdIVhQTL7OYbniKMVjo6z2TqHOMi2bFvnh8bpsHnPXKQsVvmoTPs_P32IX13-UhmGlN10vNH4h5CCIiCCbZwX-XbNjQJmFZR6EKEKc9ApVp1gYYVtL4xUxnHxp_l6QDmgiQcecokwdBXitFXIt1q1SOjKcns_SgtbBmnCW7EhbLWaI6W1MQ4LOYL1x4Pg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حمله جنایتکارانه آمریکا به آب‌شیرین‌کن بونجی جاسک/ ۲۰ روستای ۱۰ هزار نفری بی‌آب شد  مدیرعامل شرکت آب و فاضلاب هرمزگان:
🔹
آمریکا در حمله تروریستی به آب‌شیرین‌کن بونجی در غرب جاسک، ایستگاه پمپاژ و ترانس برق آن را تخریب کرد. این تأسیسات روزانه ۳۱۵۰ مترمکعب آب…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/672449" target="_blank">📅 09:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672448">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
وزارت دفاع بحرین از حملهٔ موشکی به این کشور خبر داد و طبق معمول مدعی «رهگیری حملات هوایی ایران» شد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/672448" target="_blank">📅 09:55 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672446">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51f6728ec8.mp4?token=tcxEx9fohAFbTIQ1iJyZJfouTMrhTH_ncxyG5Pa5zpoALBN1FtAGews_eJgVtV4ej0ZCWaJGTz0knyxbDK-9hyFXX4OTmSTfnokZmUxL4V2Ol8JDJ5D6aCq-mXls6VNPfWkM7yfhMlBfSRWUX6Wpw6Rp_Q4d6lHnlPiNPtvoRzEp2XeH2x2poWK_Hwith4tIXhjTkzz4bbAwrR55i4d8QG-IMSV_BxrVgJe1T1F8wA8uLgJCu04XOQCqZY9L7PdW8hvcUuroKklVxldPdDx7XdD6wWqpyU0zF4rr1FQBO-A-SASVzClkiQVbmvR_S9n3NAGSizVV-VDM81Eg9XfHqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51f6728ec8.mp4?token=tcxEx9fohAFbTIQ1iJyZJfouTMrhTH_ncxyG5Pa5zpoALBN1FtAGews_eJgVtV4ej0ZCWaJGTz0knyxbDK-9hyFXX4OTmSTfnokZmUxL4V2Ol8JDJ5D6aCq-mXls6VNPfWkM7yfhMlBfSRWUX6Wpw6Rp_Q4d6lHnlPiNPtvoRzEp2XeH2x2poWK_Hwith4tIXhjTkzz4bbAwrR55i4d8QG-IMSV_BxrVgJe1T1F8wA8uLgJCu04XOQCqZY9L7PdW8hvcUuroKklVxldPdDx7XdD6wWqpyU0zF4rr1FQBO-A-SASVzClkiQVbmvR_S9n3NAGSizVV-VDM81Eg9XfHqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیل مرگبار و ناگهانی در ویتنام
آژانس مدیریت بحران ویتنام:
🔹
از روز چهارشنبه هفته گذشته، رانش زمین و سیل ناگهانی، به جاده‌ها، شبکه‌های برق و صدها منزل مسکونی آسیب زده و همچنین ۲۳۸ هکتار از محصولات کشاورزی در منطقه را زیر آب برده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/672446" target="_blank">📅 09:55 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672445">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2139743d15.mp4?token=RuJq0WJlElAvb5NLKqSZCYyVRZ8sDZss5VelnQ2xliUNnd9N2QqJHa-s_RQulzkqYW7vGdBa2ijKceN8hnUfO-92FpGaqA6dxn0yThxR8KPucwop1QJYdn6MKYpwL5hjijRW6Q7hHgcgzUT_ZyIPLuyRx_ue7_3-oRnYCwLt08Dymiz6dTIE17end7mxhuXs7SM2tkWfgd8rJqHsfjHjLY5vWVE1wFeweua6wNMjg21vAniVBrYgHEQbURqwo7EtdAhwWNBNeP-qJzYBc4DXkN666aeEpVeh0fTQqxxk8rIw4zHfN6LrF_3nFXfqJtk2it5TEZeufWBagJgyHdko6TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2139743d15.mp4?token=RuJq0WJlElAvb5NLKqSZCYyVRZ8sDZss5VelnQ2xliUNnd9N2QqJHa-s_RQulzkqYW7vGdBa2ijKceN8hnUfO-92FpGaqA6dxn0yThxR8KPucwop1QJYdn6MKYpwL5hjijRW6Q7hHgcgzUT_ZyIPLuyRx_ue7_3-oRnYCwLt08Dymiz6dTIE17end7mxhuXs7SM2tkWfgd8rJqHsfjHjLY5vWVE1wFeweua6wNMjg21vAniVBrYgHEQbURqwo7EtdAhwWNBNeP-qJzYBc4DXkN666aeEpVeh0fTQqxxk8rIw4zHfN6LrF_3nFXfqJtk2it5TEZeufWBagJgyHdko6TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تقابل تاریخی در فینال؛ مسی و یامال: از قاب سال ۲۰۰۷ تا رویارویی در جام جهانی ۲۰۲۶
🔹
سال ۲۰۰۷، خانواده لامین یامال در یک قرعه‌کشی خیریه یونیسف برنده شدند تا نوزاد ۵ ماهه‌شان برای یک تقویم خیریه با مسیِ ۲۰ ساله عکس بگیرد.
🔹
۱۹ سال بعد، آن نوزاد و مسی، حالا به…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/672445" target="_blank">📅 09:46 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672444">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
دود بسیار غلیظ از کویت به دلیل اصابت موشک‌های ایرانی
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/672444" target="_blank">📅 09:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672443">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6bc485f4a.mp4?token=NjFOS_7Nj25NILn9jtmp6U0fvFq8fqqWUpqM6JGdvbzeT3vGb27kQ7nzixRP5zctyJIPpzGSMR3Os3vRRDYS7nqf3rwdsxV6_YH2KNgkB3DRU5XoCfttvD-THdvdbMvaAvUkZd_f37U2syEcXH-gYvEuTwKgi7xw7Bk_sko5jVQVI2oCXcabvu1VGsklu1y3aW9OlqH7hN3EMSqlFniNT__UP2OeZiaDel72bFy1YPI5oGv8v8Hac0q3pDwFu1aKFmVdZe8Gk55RDGNXBk73_FNEV0hZZ9BGkHVMY27UOryHUkzzWJ5AbajmIkhq1fZweq4KvCSo7DIqjvtP6pF9AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6bc485f4a.mp4?token=NjFOS_7Nj25NILn9jtmp6U0fvFq8fqqWUpqM6JGdvbzeT3vGb27kQ7nzixRP5zctyJIPpzGSMR3Os3vRRDYS7nqf3rwdsxV6_YH2KNgkB3DRU5XoCfttvD-THdvdbMvaAvUkZd_f37U2syEcXH-gYvEuTwKgi7xw7Bk_sko5jVQVI2oCXcabvu1VGsklu1y3aW9OlqH7hN3EMSqlFniNT__UP2OeZiaDel72bFy1YPI5oGv8v8Hac0q3pDwFu1aKFmVdZe8Gk55RDGNXBk73_FNEV0hZZ9BGkHVMY27UOryHUkzzWJ5AbajmIkhq1fZweq4KvCSo7DIqjvtP6pF9AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قاب‌های جدید از مزار نورانی ابرمرد شهید تاریخ در رواق دارالذکر حرم مطهر رضوی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/672443" target="_blank">📅 09:36 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672442">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
سپاه پاسداران انقلاب اسلامی: کشورهای میزبان نظامیان متجاوز آمریکا آماده دریافت پاسخ متناظر باشند
🔹
آمریکا با شکست نظامی، به جنایت جنگی (حمله به بیمارستان، پل، فرودگاه و غیره) روی آورد. در نبود نهاد بین‌المللی، ایران مقابله‌به‌مثل می‌کند. از کشورهای میزبان نظامیان آمریکا خواستیم شهروندان خود را از اهداف احتمالی دور کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/672442" target="_blank">📅 09:34 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672441">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b204f4e610.mp4?token=ufdBDeuF15nqp79nk8Km5hkb3guIcG2ia1qN1fimMqFDK10C9sLepC4PrUpHGAWd8gMeVOfgBC7bdNEyPnOJETQImeuMRZs2dDYXCZex3SUg82Nksm4NyFhEv8Hcfcja23rrKmCVCV3yNnRHcpb8gm_85nI86w9PYnMkR3tgZmIUDWmfX72e7rRbMvKlYIS0_8HeyIEMqIsNrPMd8MrKyZj70Qc6kQFKpfaSjcreQgAYxFAy_LX3ohkBcjohBJ_EMZw39CaIMiFmo_Gq5HWPYCLykrfWMr7EmpmClcWAL8JxRIk_1UN0W13PRkDHv1GJSFpqoEb1UvWdHWmLFDbU3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b204f4e610.mp4?token=ufdBDeuF15nqp79nk8Km5hkb3guIcG2ia1qN1fimMqFDK10C9sLepC4PrUpHGAWd8gMeVOfgBC7bdNEyPnOJETQImeuMRZs2dDYXCZex3SUg82Nksm4NyFhEv8Hcfcja23rrKmCVCV3yNnRHcpb8gm_85nI86w9PYnMkR3tgZmIUDWmfX72e7rRbMvKlYIS0_8HeyIEMqIsNrPMd8MrKyZj70Qc6kQFKpfaSjcreQgAYxFAy_LX3ohkBcjohBJ_EMZw39CaIMiFmo_Gq5HWPYCLykrfWMr7EmpmClcWAL8JxRIk_1UN0W13PRkDHv1GJSFpqoEb1UvWdHWmLFDbU3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دود بسیار غلیظ از کویت به دلیل اصابت موشک‌های ایرانی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/672441" target="_blank">📅 09:32 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672440">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
وزارت آموزش و پرورش: آزمون‌های نهایی یکشنبه و دوشنبه در هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان لغو شد و به زمان بعدی موکول شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/672440" target="_blank">📅 09:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672439">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O0jIT_EjVGOO7V1J4wv7sBADKhf4IKhSpKCN0B5vZbGr_3hF118QlxA3rLi-FKkfwCYzcJhEhYlEXG6KsAzJCj1HLLPsBH5KR07TdAFZ1BlV1VwJp9JyLijD_CBSfnsdLFtdJ_8eey9ULTwp5y-KAN8oE1clD8xyRNAPZ49Uq-Jr8FUoFVepGDGRqTpnb4-Mv7iud_vMNfnB4dLewpfqM2U9q6xQDUbNgbGuDj12qUTBli21xrLkvFTeDdfo6YqrmFK-PMQBkfAuZCawrwPOjhXT32kdCbPJgZk1QqpUgoH-ka2RTBmMap1uTIJdP99W8sJG0_UX7n6JL532xLlLvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افت ۱۰۷ هزار واحدی شاخص بورس در شروع معاملات امروز
🔹
شاخص بورس تهران ۱۰۷ هزار واحد سقوط کرد و وارد کانال ۴.۷ میلیون واحد شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/672439" target="_blank">📅 09:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672438">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/257aca5779.mp4?token=cj2bD-hW9fetgJrCuCRxqqU-RA6mhxjLeC0j-ZynGuDGnWgK01vqqAqq9gH6O-0J37L5K374RoqNQutmVD0aAzPsBpnhuGIEAWGoISjKOfQ-IXoB-bYdN79rTMWpthAzy2g3yzEb_t4oXUGjmDQ9XWNUsXntbzmLta6mOI0GtfTLH6_R2RshCYfxK2T3V5nbVF_agDau_3QTTD532-Dkelcfo5cSgvK3J7uZIWE7J2eK3oXHQ5K5GKkifFQZ-kYZGo-yHlk1QM39jekC16A6gCw1JXYZde3G0i5B_s5vtjhApq5NVhSA8PcrVL5I8vVst6yBnYl5SZhLgV8mcQB93g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/257aca5779.mp4?token=cj2bD-hW9fetgJrCuCRxqqU-RA6mhxjLeC0j-ZynGuDGnWgK01vqqAqq9gH6O-0J37L5K374RoqNQutmVD0aAzPsBpnhuGIEAWGoISjKOfQ-IXoB-bYdN79rTMWpthAzy2g3yzEb_t4oXUGjmDQ9XWNUsXntbzmLta6mOI0GtfTLH6_R2RshCYfxK2T3V5nbVF_agDau_3QTTD532-Dkelcfo5cSgvK3J7uZIWE7J2eK3oXHQ5K5GKkifFQZ-kYZGo-yHlk1QM39jekC16A6gCw1JXYZde3G0i5B_s5vtjhApq5NVhSA8PcrVL5I8vVst6yBnYl5SZhLgV8mcQB93g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیو ادعایی سنتکام از برخی حملات متجاوزانه بامداد امروز خود به ایران
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/672438" target="_blank">📅 09:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672437">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
تعلیق فعالیت فرودگاه کویت
🔹
هواپیماها به دلیل تداوم حملات از ورود به حریم هوایی کویت اجتناب می کنند.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/672437" target="_blank">📅 09:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672436">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gM-A4p06iTZpmGNchPvRBsK7BCFOlVJ27CzpPf7YO4BZuPk7Xo190Xff4FEZK95QQ4aCjJZCYX5IfHLofMwGKASxcTbiEnBbZk1c4kR1Dh1YYWIWkDkWgd5LRtVPyl26jADe7K9yaSE9CWXs_b-b_7w8A8nf6cAPD8rAHWKepmRSuDiEEOTCr_PSOKGtj52WzNjSFW8gK8jrWxdk0Srpx8KZudwT7eEqVqxJKnf9w8s86ureu-lKYCt9CFZCxTv9YBYl1wDWcT43ESQsVvHlgaXzG6A4Lfx7mEAlR5lRLLTZmci1cKyJkYctvuyPnF73uSOwmQPZemD6TVro40WSyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تعلیق فعالیت فرودگاه کویت
🔹
هواپیماها به دلیل تداوم حملات از ورود به حریم هوایی کویت اجتناب می کنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/672436" target="_blank">📅 09:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672435">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
ایروانی: هدف قرار دادن زیرساخت‌های ایران جنایت جنگی است
🔹
ثبت اعلام آمادگی دارندگان قبوض ودیعه‌گذاری حج تا ۳۰ مهر ۸۶ از امروز.
🔹
نتایج آزمون سمپاد به‌زودی اعلام می‌شود.
🔹
زلزله‌ای ۵ ریشتری شماری از استان‌های جنوب شرق ترکیه را لرزاند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/672435" target="_blank">📅 09:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672434">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
معاون سیاسی، امنیتی و اجتماعی استاندار هرمزگان: جنایت جنگی دیگر آمریکا این بار در جاسک  تأسیسات برق و پمپ‌های آب‌شیرین‌کن اسکله روستای بونجی هدف حملات موشکی قرار گرفت
🔹
بر اثر حمله به این تاسیسات آب شرب چندین روستا در غرب شهرستان جاسک قطع شده است  #اخبار_هرمزگان…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/672434" target="_blank">📅 09:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672432">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26cfd2b190.mp4?token=g1RRGzUfMn2tFbyW0CGJJNoawao8cVqhSN00tx13DoFd6rKEnefqXW41bm3v-AtgGx9syypZeBYJaiG7mFbwYeGGyK3xmzaZaG43F-XEQH6rdAstU0TcTdHqcMfIsURqcAVEgC9UDXT6fHo_06F2v3UJPj-BDyrF0rdVWXUUpAbnnVm3Oflqvph3tM_E86B01a10zppkedcAMbbCR82iMKiijYvZkH2MSPOC252doZAbaYjIjS14ZUX2fhYVWjm8_cPFADj-2bUkf_odlFh-wKKMDwPB7WGLnyL5O1iZKDAoHclHQfQJ2caiG_7rbksPthDHxeo8kJ9o_RoDxe9teg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26cfd2b190.mp4?token=g1RRGzUfMn2tFbyW0CGJJNoawao8cVqhSN00tx13DoFd6rKEnefqXW41bm3v-AtgGx9syypZeBYJaiG7mFbwYeGGyK3xmzaZaG43F-XEQH6rdAstU0TcTdHqcMfIsURqcAVEgC9UDXT6fHo_06F2v3UJPj-BDyrF0rdVWXUUpAbnnVm3Oflqvph3tM_E86B01a10zppkedcAMbbCR82iMKiijYvZkH2MSPOC252doZAbaYjIjS14ZUX2fhYVWjm8_cPFADj-2bUkf_odlFh-wKKMDwPB7WGLnyL5O1iZKDAoHclHQfQJ2caiG_7rbksPthDHxeo8kJ9o_RoDxe9teg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
♦️
حمله پهپادهای اوکراینی به انبارهای نفت در مسکو
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/672432" target="_blank">📅 09:06 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672429">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DWTPF3_4J2VdD6Y2oEwQrLV6kdOcD6gHzYMLG8_DQIYrJ2ehwRiSAg6AV_dMjaRtCxribnKyRKAhznK0P4o4EO_B__7IwwDnVmO3P2X3IsP3VfPhfbwfmjPXMWwxz4knwMDeicbayNJR8wVXosSYWBP3p1pySknYK6d7xOb8PgKIpLKLAPN0P_GUGXvPghvTbhp2bgsgJgBYFz_GZFG8-1tz8ZfL4ACi2DrXNrCHOc7hCeDPRfNH83KYUrgJkysIH6QJAnNRlYukz3mefwvfcGPFUGhuQSJHiIei1BZ73HGlxGvtAovAvoNwwRgvbWLld0gtqk7lwjS2i4McXxrNCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CcbSyeZY3ynu00DzgzlqgSumVymIzb7l-dWrMcaG2RW-LjEyhh12Q6D2rWTlm9eZt_vapiA7MX-gSJhyGJrB492hel8CLWknbQkpXIseL7uzczgJKGNArf1-Voc6x_Xd1XjJBAQhcNwljga5AqGvVEBnoernovUvpdnWpm1u_cq6bWpFTQJV4A_on_Prqt4n3rpyjDMp2hC1OMXcYlEq3R0n5HsoxsuuCrWYl-w7xWTMnUe9VPaRqSXFv1FMQxt3EpTXxmaHmeXnTm2SVBhx2jmEAVXq0YUmWWMF0wMWU5K8LConK5a_wq8LGlRSljFi6xrfTNEnbJCxnb-yyI08_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gCZn6HC4DCknprlAfYz-sZCQt4nEw-4BwWlSAaoGFWrAD8pJXFCsoP_ZQFgG6sKv_OhTKG6wNd0Y-Vb2xCDIxEwPHjNoKx4Kmtam_zgGGbazs350W9FKxsNsOVRhLi0ggBwCKmRWCmRys4985ZzyGRCwtL7qfUSgS1FAmEC0UhgzcO86e-kX5bLARW-nLjQ6dhmSRoh6Cx4hHsEF04eMnkdvjH-WMc28S6wLqoHNccVg72zIBU3msSueFrBhDdN0SWB83pEyLorRz-ANNPrG-wvcmc40z54XMeL0FWm4ssROJ-wt2FyK7eOQYwwyODJdO2wB1fCL9IDGgwV4Uv4vdQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از برخاستن ستون‌های دود در کویت؛ صبح امروز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/672429" target="_blank">📅 09:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672428">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98cab861f1.mp4?token=Xfa6ZK17wQ6q1WHBEINSp7VbVi_Swxc4dKNRAYoiwEQ825ody73S-bF780zbokUKLUtq2PS-Fp9Nltdw3mD6kOhxuwLmgG1Lt_7ccusq3VzUikWaXGCCU8Yj1NC5fthfqgN8YU-0t-95IRWbsdMFmf-zn5HjSe4fELjDBG2RN81C6QIgciIqH8wyuwiogY3zBCAoknr4zU5Ce0tJW7XbV5qnyQzVo4nSFqZBWFjr4FrEYgNLo0ECDgWahZzvk1OvQ11-aaytFeKTMs4pFOAaBx0BAJOY-yZlYfren5zfTp330xyIHYG17adXAQcvTNn57hz8_Jx635wJrv0HvZC6Mw9DtT7a0CKi2KxH87vm-3RBuyW_GQ_SUp2aYvRYmWL2yJweemAnQyGsNR8gESaYxF9bR-BAJRuUMybl3stHWZrwqhWR7axmoUdwmBF2pWVegXMEPeGh-6gTlqyqj_K32XPgMs3FKnumSrJfXj5NsKyf4b2nGODC58HpFM_Ua40wZFsAPQfaaBlEamGPG6_lQDSeuzfhb_6759qHNPSJ8i3QteMAQlzobRUs5dsjftYRvAwOa7-gRcOeFu8c2OEtqSYMkksWVgqM76oprtu7V_BXxUFGtmaIQpf9VOFYQAdiz0RCqfGSTcG_AIYcccv2cHOR9g-4g6pRsVswHmr1RWo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98cab861f1.mp4?token=Xfa6ZK17wQ6q1WHBEINSp7VbVi_Swxc4dKNRAYoiwEQ825ody73S-bF780zbokUKLUtq2PS-Fp9Nltdw3mD6kOhxuwLmgG1Lt_7ccusq3VzUikWaXGCCU8Yj1NC5fthfqgN8YU-0t-95IRWbsdMFmf-zn5HjSe4fELjDBG2RN81C6QIgciIqH8wyuwiogY3zBCAoknr4zU5Ce0tJW7XbV5qnyQzVo4nSFqZBWFjr4FrEYgNLo0ECDgWahZzvk1OvQ11-aaytFeKTMs4pFOAaBx0BAJOY-yZlYfren5zfTp330xyIHYG17adXAQcvTNn57hz8_Jx635wJrv0HvZC6Mw9DtT7a0CKi2KxH87vm-3RBuyW_GQ_SUp2aYvRYmWL2yJweemAnQyGsNR8gESaYxF9bR-BAJRuUMybl3stHWZrwqhWR7axmoUdwmBF2pWVegXMEPeGh-6gTlqyqj_K32XPgMs3FKnumSrJfXj5NsKyf4b2nGODC58HpFM_Ua40wZFsAPQfaaBlEamGPG6_lQDSeuzfhb_6759qHNPSJ8i3QteMAQlzobRUs5dsjftYRvAwOa7-gRcOeFu8c2OEtqSYMkksWVgqM76oprtu7V_BXxUFGtmaIQpf9VOFYQAdiz0RCqfGSTcG_AIYcccv2cHOR9g-4g6pRsVswHmr1RWo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل به طریقه گلاب ادامه دارد
🔹
فیلم دیده‌نشده‌ای از زیر قبه‌ی حرم مطهر حضرت عباس علیه‌السلام هنگام طواف و گلباران پیکر رهبر مسلمانان جهان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/672428" target="_blank">📅 08:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672427">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
انفجارهای جدید کویت را لرزاند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/672427" target="_blank">📅 08:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672425">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Eo7LYL-DUC_eYX4JjLqdBx_cPNn86pstImCQ6eIMhdvVl2SHl-Ez4KJlwUewRZMNYU2F1IkXsiVAY0CSWbbnOY8wC_VtigtagFSS5XjXsr69ogyVCIP86t68Qucs4CFF5cuXqdKTmpjakqGBFDhnQSoU7NxSi8zsgRhAaFMBoROq1RtiI54el8X9ygtU9wvsGoebJ9zt0iZE_i2DdWWsJNJ8rdX8Ioesms7H2Ijm6JvONQ21hNqWeWSVZvWxVCzBYroKOSw_4Bl4SNY3kPX5Vz9XvLrw78EOB6ZJwt0lgqoEVxehjSG5etu6ixK4r8A-La_bcN8vGpwJ0pPh76vvpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W9PBaRhSeb8V3YyfivLdzROnBd6lVn3ptRcjw5DBsMojejJZm-2lq1Z8XD-t5UIss9ufuWP_zoEAZiyL67S4AExFM6XXtpv2asPlw7xzwxp0Vr5EkHqRa3Y4zHgm_LdqQouNP4Wo1VkHhxNYF12D4QxfHwe8A6psf8IWttygiQY1X0fuuLJnHO8fPtfUq9cZ9rLqvljF3tKIEEpBbpo4Uu4GvoOJ8fdmiC2UiOJBAzJUDGk1E9lJOi7LVufGmklBoqKXH0JNgxNxscA-DJ3VlVYDE815ewwT2X-NVaw-lVMH98cZtAbCHBEUpvQie_-eOv-VPOD75SI9ocpPwYGdtg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصویر ۳ تن از شهدای حمله آمریکا به پل بندر خمیر
🔹
این ۳ شهید اهل روستای نیمه‌کار بودند که درحال رفتن به منزل خویش روی پل به شهادت رسیدند.
🔹
در جریان این حملات ۸ نفر شهید و ۱۹ نفر مجروح شدند. #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/672425" target="_blank">📅 08:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672424">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
اطلاعیه شماره ۲۷/روابط عمومی سپاه پاسداران انقلاب اسلامی: کشورهای میزبان نظامیان متجاوز آمریکا آماده دریافت پاسخ متناظر باشند
🔹
محل استقرار تجمع نیروهای متجاوز در مرکز پشتیبانی نیروهای زمینی در عریفجان و رادار پایگاه علی السالم آمریکا در کویت منهدم شدند…</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/672424" target="_blank">📅 08:34 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672423">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LkQ6TaQ-Ya99Ovcr-j9jHWHDIRY6ipRp7rjjdkSGTgwcRO3Yghf6lV4FW5JkZorHzZERTOBRU4MRxlTYVzWkJvxinaO0fWMODBe-kHIq_AY_kw9E8fwLRJZlQ5z_jOzN5QFSnZu3khSgmWOaXjw6ScHMYClTAEazwIfvVRs-B-8hnLNS7zwcwyNLfp5AEler7Ca1BAf5wE5ITWlz4M1iWKEKmxY1r16Q4pzpRrZ9jQ5eoYxMyLQzMmCiwef6-iBoYvKkvnaFAPVKfhxW6qORBg54Lp47m6JYBSG5qmcI98kB8Ae6VOjmgWBOuMLLBhFt3bYxTorB3mLnRbSLR07ojQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معرفی ۸ سایت هوش مصنوعی؛ ابزار هایی که کارتو راحت‌تر می‌کنند
⌨️
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/672423" target="_blank">📅 08:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672422">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
انفجارهای جدید کویت را لرزاند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/672422" target="_blank">📅 08:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672421">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
مهاجرانی، سخنگوی دولت: سهمیه مناطق جنگی برای داوطلبان کنکور ارشد استان‌های جنوبی در نظر گرفته شد./ ایسنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/672421" target="_blank">📅 08:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672420">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
منابع رسانه‌ای از وقوع انفجارهایی در شهر الخرج عربستان سعودی گزارش می‌دهند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/672420" target="_blank">📅 08:12 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672419">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TJ8lcpMsasV0OZj7FKOfTUovlYzBXvod9pvTY8O7UgGZv9UcP2EGzkP0XEH9wh9aczjUJaolfp9dNwM9YdBMjlbRDpnCyQwfXLW1yZZIid5zNol8805YoEc6NHIX3S1je1KJTJjPzF5TD1DZDPxQ3ZCyPP72M-uMKAjT5E93fYE4TEETgJ2YfhSDzVYpEHvMBDjWLJe2mxjGJrbv8xLZlghj2c29bJaDrkttUQW6XAAJxyt-v62vFRIvyNG4bAyvO3xorqD2oHBkYjBW1-ytfZvO4zzj-WTRWICCs4othK5BiLHHarNFHcTve9Dmc5hKpqaojQnp-HWCv7T5ZpKpvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
پوستر فیفا برای فینال جام جهانی ۲۰۲۶
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/672419" target="_blank">📅 08:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672415">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fANLbCzYD8oJKkd_c0fMH5RNw-6wDkrbSHGxqlbsXwCR5sQe4D0nNV4FVynLn8-T5Z4VuvDce3pcFH2_s7PUtGBsYB9YwD7pc9Jhq8Ny_EovsOmBnuGPWJcHHMHhq4I1gAokVUHm8HnDtaEl58eH3ojYg8dvh-_bvMv3VejYKiYUyOnRhaljhfBhULfLm9Tb38E5X8m2fLC2GeFDY5gzpU54SGtVbRuyHAnolmbSi9FMbL91Xh66k_0wbPl4kA3W2h2-GNx0c2Vwb74g3Ps0KfqLksmcdBtUPbi1hBh3lYaIb_4x8WEBI44gdevT6ljd9t4o5szv_u2lrCggHz4HgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EzgWd8fR87P6dxGGex1G2AfIwh28zRw7KfvjEB6N55uV5hBy_QmtKk9pNbZWfeaDvJHFqjIKYCOpw79qKYO4rUARfIZMpB2t0gfFiYNdQzAKOKx6bHIH48JcaBt4LyXTPXsB9GNa5kxYx5HdujQ-8cBvsTkCRqDX210HNTK95C2Nc4XWon3n0zjtJ9XOLEnAxXWwiBFok8S_6A5Y8CPIfGY4W4oBgsuC-akZqotvy5oQiaq2vxML3lr2qeXSgDQfs9bs11fsNRZspGT0vJ9mRFS2ZgdjjY7TbwH0B3vuod2jx1cWv9F6uj5tv1z2HIBzJqLwot4HLWrNFAsumzZWwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jnk_d4U-VBw8yBgabeNrp8tm_tVLbAfi-YLRnp7UX2UJHs-Jm5xYb60y3E-0E1SOEfxUaBbac_yT5SGekFOKc1TKPU8tpecks36k0-03JVNv_SUd6v5-nG3gwylUEwEoaRr_wznomurZdBY1V_m7SZoret64hs9hhJzgf7tGR6j37IrZ6xPTB0687fd06KuGx35vnPjkFBSMrz-ec5y5lm8lmROj4al6rMx42Lr4AX5BSLnTVV434ULZk3hHaWss06GjmU5ORMRu7FgTL7QAZ6rB7P8CfmvWlyKikI0R__1y39gQsSAndZ9BS9sWYFnZRXGgjgQZU5W7dl7wzjYg_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a69e676ae.mp4?token=URt1GuT0izhNq1iKrXlPAeCh1hLsWeGmeHFuSPhvT8YhXwIxwKfqmaWqcIvOMqIPBmfkYmMlyPu6v-xqwqVtS_-Zx8t7SKZh9sDUUEvsEibdjxhH1MdrcSAVnyNLvgakxIyhZg6Zo6Pg55RLIJfNnZGVppCS7FAsYCSWYYdi3_smXHo4Tf8s8EGat3oQVHQZORknNsVh_np299TnnNQRlTmnPChrR4GeKE5Qz4KOcTWfaqT613660SS7v8TV5EZ5xdpLzL4DGn8ORlFjDJMKgVbsNfLb67JSVwqZOSggxCWxm0Iy_qwVvi6aqf4lj_QB7Fa4ISceanu0poqNCdM-Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a69e676ae.mp4?token=URt1GuT0izhNq1iKrXlPAeCh1hLsWeGmeHFuSPhvT8YhXwIxwKfqmaWqcIvOMqIPBmfkYmMlyPu6v-xqwqVtS_-Zx8t7SKZh9sDUUEvsEibdjxhH1MdrcSAVnyNLvgakxIyhZg6Zo6Pg55RLIJfNnZGVppCS7FAsYCSWYYdi3_smXHo4Tf8s8EGat3oQVHQZORknNsVh_np299TnnNQRlTmnPChrR4GeKE5Qz4KOcTWfaqT613660SS7v8TV5EZ5xdpLzL4DGn8ORlFjDJMKgVbsNfLb67JSVwqZOSggxCWxm0Iy_qwVvi6aqf4lj_QB7Fa4ISceanu0poqNCdM-Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر دیگری از آتش در مقرهای احزاب کرد مخالف ایران در اربیل و سلیمانیه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/672415" target="_blank">📅 08:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672414">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d5c6c882c.mp4?token=KRrYMUv0vgTKooA5mno08SzScqcqn1ihSBdWXfYzIEEMRsvTmJouqtBj1zCt39Df9x253xipVP8LdGFwtaWHdUYqOLGX97YOhg94fQTQSChAiOtqbYxkCiebIoK8ojngt5EkbHj-n1oxq1DmSAAvg6NTNHmfwJJvFDKOFq7nPBKnykegyD9DkcR5kYPPqwlT1vk6esP8TPxZO0tRVCLCgVstAybGcZWZQIwPgvHxtnSDJ6--NqI87tSz4kbS9HKu3eCIvdxUkBSeg98JrY7tFwVTxkO4Hr4qCAGM0jQ9_n7WpI-IQ_eAfZWlfaHQUNVk2G078LyHty2dOXsuTKI6-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d5c6c882c.mp4?token=KRrYMUv0vgTKooA5mno08SzScqcqn1ihSBdWXfYzIEEMRsvTmJouqtBj1zCt39Df9x253xipVP8LdGFwtaWHdUYqOLGX97YOhg94fQTQSChAiOtqbYxkCiebIoK8ojngt5EkbHj-n1oxq1DmSAAvg6NTNHmfwJJvFDKOFq7nPBKnykegyD9DkcR5kYPPqwlT1vk6esP8TPxZO0tRVCLCgVstAybGcZWZQIwPgvHxtnSDJ6--NqI87tSz4kbS9HKu3eCIvdxUkBSeg98JrY7tFwVTxkO4Hr4qCAGM0jQ9_n7WpI-IQ_eAfZWlfaHQUNVk2G078LyHty2dOXsuTKI6-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برنامه یک روزه فول بادی بدون نیاز به باشگاه و تجهیزات
💪🏻
#ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/672414" target="_blank">📅 08:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672413">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
منابع رسانه‌ای از وقوع انفجارهایی در شهر الخرج عربستان سعودی گزارش می‌دهند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/672413" target="_blank">📅 07:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672412">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
اطلاعیه شماره ۲۷/روابط عمومی سپاه پاسداران انقلاب اسلامی: کشورهای میزبان نظامیان متجاوز آمریکا آماده دریافت پاسخ متناظر باشند
🔹
محل استقرار تجمع نیروهای متجاوز در مرکز پشتیبانی نیروهای زمینی در عریفجان و رادار پایگاه علی السالم آمریکا در کویت منهدم شدند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/672412" target="_blank">📅 07:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672411">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
زمین‌لرزه‌ای به بزرگی ۳.۵ ریشتر، صبح شنبه حوالی شهرستان بندر خمیر را لرزاند.
🔹
احتمال شنیده‌شدن صدای انفجار در محدودۀ جنوب اصفهان/ مردم نگران نباشند.
🔹
خبرگزاری کویت: آژیرهای خطر برای چهارمین بار در این کشور به صدا درآمدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/672411" target="_blank">📅 07:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672410">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b822dcfe2.mp4?token=ppPxUvAJlJe4HYdY5HGbBJIM31q0FbtBDxzdG9A7f0pkFN_vXrbLwqrJwxJsVSr7aCy7wZ5fPqiXFVXwhPVyjqy8iyDTEbBsbzfSuIJGpIQP7bNx86ecejZgKdlaEvL-Gc8zXq7FoDwAGk8MJg4NfJrq20ltsF7nPy7z6w06r4PtSZnPo3gKNFa9rOOr812VQ2x29R8mCyhY5J6F8rvAKJVVBovUha0zmHqsTWjdHvLweTlR0HrNUE55XH0dQcSnTVdKZEuzVqnL4c9Tx-o3xpUweDjAVhbwV6m7CihXdsYYjW4GrFS-xaQfXvRtEztYkFv77oQC3nUa7f7we6YivQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b822dcfe2.mp4?token=ppPxUvAJlJe4HYdY5HGbBJIM31q0FbtBDxzdG9A7f0pkFN_vXrbLwqrJwxJsVSr7aCy7wZ5fPqiXFVXwhPVyjqy8iyDTEbBsbzfSuIJGpIQP7bNx86ecejZgKdlaEvL-Gc8zXq7FoDwAGk8MJg4NfJrq20ltsF7nPy7z6w06r4PtSZnPo3gKNFa9rOOr812VQ2x29R8mCyhY5J6F8rvAKJVVBovUha0zmHqsTWjdHvLweTlR0HrNUE55XH0dQcSnTVdKZEuzVqnL4c9Tx-o3xpUweDjAVhbwV6m7CihXdsYYjW4GrFS-xaQfXvRtEztYkFv77oQC3nUa7f7we6YivQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پس از ادعای خوک زرد درمورد گرسنگی مردم ایران، یک ایرانی در خیابان‌های لس‌آنجلس با پخش رایگان پیتزا، پاسخ خود را نه با سخن، بلکه با عمل داد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/672410" target="_blank">📅 07:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672409">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
سران کشورهای عربی که به دشمن پایگاه داده‌اند، قاتل رهبر ما هستند و باید قصاص شوند
🔹
جنگنده‌های آمریکا و رژیم صهیونیستی برای ترور و به شهادت رساندن رهبر و دانشمندان و فرماندهان نظامی کشورمان از پایگاه‌های این دو در کشورهای عربی پرواز کرده بودند.
🔹
بنابراین سران این کشورهای عربی که پایگاه داده‌اند نیز در شهادت بزرگان ما شریک هستند و به عنوان قاتل باید قصاص شوند. پس چرا به قصرها و کاخ‌هایشان حمله نمی‌کنیم و آنها را به جهنم نمی‌فرستیم؟/ روزنامه کیهان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/672409" target="_blank">📅 07:36 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672408">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DTXGlnSxOtfom2XidjoaMWa1Tj96_sxNP1FZOxjt-Ls1izPKGSmN1nlOXyBtExObG0H-w2PZGwhhy4-CpxMdOV172cBhWe9CcTAU5T0xqExytNC_URIdjOkd4Ktf3Ed9mBbk8mh1dM3IbngfTH2mgDEXgAimFnXaBMoENGgi5gVqsobnBL8CVlZH8RIxIUCUjvBVkchkn7_eYExREX60xNERQP5-pCg8Rx9HHEkrXp970tCnXD6rw1sbbql8bxnqEOTUH3H9Auv-Gtz_SoCJUNVcMlLSwAllVmT0YPYE7htcSeJR229I6vHPjBNXtjDeYnYLKYeoiRemJrKxBoLclA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز شنبه
۲۷ تیر ماه
۳ صفر ‌۱۴۴۸
۱۸ جولای ۲۰۲۶
شنبه‌ها
#دعای_عهد
بخوانیم
⬅️
متن و صوت دعای عهد
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/672408" target="_blank">📅 07:32 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672407">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ex5yEYOdO6PE32UU3kFxaOTf7fX3CGgOEo5cuZhuzq6RpDnHapE98VE3CoOzd3OK8GGXHyoxzXLmhXBCz7p2uCylpzRL-NFxB0EPMppR4RFLCdZ7xttHM4YwhEQ5QE-luUK3lfNCGo2ggND_8g5Qz_v3MP3kZ9k5GRq9bdYNUckw2JtVLwBA7emnhVZZiEuJMEtKqHI9ZliOrUhm0YT3-A4rA735w1Q1Sm1l_WSA50qMk46T8Zlv3aFD0ejrHmT9jyydmBShjYyy4v35ZLVx4I0ilxa0cdmhQ3vsQ3ye0-IvTmoMJPnrWHLhJzVwsGhjT3k-HUVqK4PPhkAniPTr8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
منابع عربی: انفجارهایی دوباره، پایگاه‌های نظامی آمریکا در بحرین و کویت را به لرزه درآورد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/672407" target="_blank">📅 07:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672406">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
منابع محلی از حملۀ مستقیم موشک‌های ایرانی به تأسیسات آمریکایی در بحرین، و انفجارهای مداوم در آن محل‌ها خبر دادند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/672406" target="_blank">📅 07:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672405">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d479df485.mp4?token=j_0W1YJKET2cZCZtxiYUF8Kx7HFPp5-5CsfJfexdIsynqbtmEsPSQEGYslFsgFWx_il9Lc8kStR4jcn2Q1NOGlEVACg9omY6DMuWVbaWHAAPKMZ1C2Miiw5lmyleYlTkbWZ4Q8XvWzeyEdIHsICq9wuRGI5k8czAG52voGNAjuPVs9rp1ZptyxptqHjQLknDKK7KErJ0WcPdBtLuPuWvKkiGdf5w_x_0BUlCEiuicCncqN6u7yVR85hKZ5mncYY109Vzzgt-xTGB58AglLt6GvORkUBCDqD402QpbecXetbZ1UFhbbGnmyVjlEGKu-x2RY_meyVO4ptVg7Jl6Cv6Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d479df485.mp4?token=j_0W1YJKET2cZCZtxiYUF8Kx7HFPp5-5CsfJfexdIsynqbtmEsPSQEGYslFsgFWx_il9Lc8kStR4jcn2Q1NOGlEVACg9omY6DMuWVbaWHAAPKMZ1C2Miiw5lmyleYlTkbWZ4Q8XvWzeyEdIHsICq9wuRGI5k8czAG52voGNAjuPVs9rp1ZptyxptqHjQLknDKK7KErJ0WcPdBtLuPuWvKkiGdf5w_x_0BUlCEiuicCncqN6u7yVR85hKZ5mncYY109Vzzgt-xTGB58AglLt6GvORkUBCDqD402QpbecXetbZ1UFhbbGnmyVjlEGKu-x2RY_meyVO4ptVg7Jl6Cv6Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منابع عربی: ناوگان پنجم نیروی دریایی ایالات متحده در بحرین، مورد حمله هوایی شدید قرار گرفته است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/672405" target="_blank">📅 06:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672404">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
منابع عربی: ناوگان پنجم نیروی دریایی ایالات متحده در بحرین، مورد حمله هوایی شدید قرار گرفته است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/672404" target="_blank">📅 06:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672403">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
۶ صدای انفجار در بحرین شنیده شد.
🔹
وزیر امور خارجه عراق: مخالف جنگ، گسترش و ادامه آن هستیم
🔹
رسانه رژیم صهیونیستی: اسرائیل تولید بمب‌های هدایت‌شونده را آغاز می‌کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/672403" target="_blank">📅 06:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672402">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
صدای چند انفجار در اردن
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/672402" target="_blank">📅 06:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672401">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
معاون سیاسی، امنیتی و اجتماعی استاندار هرمزگان: جنایت جنگی دیگر آمریکا این بار در جاسک
تأسیسات برق و پمپ‌های آب‌شیرین‌کن اسکله روستای بونجی هدف حملات موشکی قرار گرفت
🔹
بر اثر حمله به این تاسیسات آب شرب چندین روستا در غرب شهرستان جاسک قطع شده است
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/672401" target="_blank">📅 06:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672400">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
منابع عربی: انفجارهایی دوباره، پایگاه‌های نظامی آمریکا در بحرین و کویت را به لرزه درآورد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/672400" target="_blank">📅 05:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672399">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bce0a3dfc.mp4?token=MBZBWHwL06DoeG82MggT6flZPiaaAREXA6dDSzsBEyoUlzvIqb9d8hpygPIsRIX5e624DR8r6aZN5hw_k3ow-kytYwXp9ELEs3Ue1sSaX_Kmie-bU-OmG5VJaUfe9eZ5cKaPHtUOGAN8F89xL2FiBXpN4Du_PTpAm7kJakpnP7NP-sA7gpQxDaVsrD9pI0Q7lc1iAbSmtGaq6RoFEeCpiXJ2ewrjWgnvwPb3mPziNJbJkUpgxAoYiP5lrRNwgcGlVj-NH5hPm263hu3LN1OwzMkOnLfkBClvGlrnkbGEScgC8mrH5Y0roJkW_8QZa_PaEpftATh16orJNbxSQqqSTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bce0a3dfc.mp4?token=MBZBWHwL06DoeG82MggT6flZPiaaAREXA6dDSzsBEyoUlzvIqb9d8hpygPIsRIX5e624DR8r6aZN5hw_k3ow-kytYwXp9ELEs3Ue1sSaX_Kmie-bU-OmG5VJaUfe9eZ5cKaPHtUOGAN8F89xL2FiBXpN4Du_PTpAm7kJakpnP7NP-sA7gpQxDaVsrD9pI0Q7lc1iAbSmtGaq6RoFEeCpiXJ2ewrjWgnvwPb3mPziNJbJkUpgxAoYiP5lrRNwgcGlVj-NH5hPm263hu3LN1OwzMkOnLfkBClvGlrnkbGEScgC8mrH5Y0roJkW_8QZa_PaEpftATh16orJNbxSQqqSTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
♦️
پهپاد ایرانی در آسمان بی دفاع بحرین در جدیدترین موج حملات پیاپی ایران به پایگاه‌های آمریکایی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/672399" target="_blank">📅 05:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672398">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
کویت، بحرین و اردن به دلیل ناتوانی سامانه‌های آمریکایی در برابر ایران، در حال مذاکره برای جایگزینی پیمان‌های دفاعی با پاکستان به جای واشنگتن هستند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/672398" target="_blank">📅 05:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672397">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
حملۀ هوایی دشمن آمریکایی به جزیرۀ هرمز
استانداری هرمزگان:
🔹
در ساعت ۵ بامداد، نقطه‌ای در جزیرۀ هرمز هدف حملۀ دشمن آمریکایی قرار گرفت.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/672397" target="_blank">📅 05:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672396">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
حمله موشکی ایران به پایگاه موفق سلطی در اردن
🔹
این پایگاه میزبان نیروها و هواپیماهای آمریکایی است. پایگاه در حال حاضر در آتش است.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/672396" target="_blank">📅 05:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672395">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
انفجارهای شدیدی همچنان در کویت ادامه دارد
🔹
موشک‌های ایرانی به کویت رسیدند و انفجارهایی پایگاه هوایی علی‌السالم را لرزاند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/672395" target="_blank">📅 05:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672394">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMqm17c1RKKjTGcmCnUdgUPuLNM5lznyiG5x5HVoa33UMn4lCXv1sAHiEdVFHiTRTp1_mJuPiL02MpL4aebTvk61PSAtcquC697vDXfIEOdAHvACRtm1dzhiXrnZIRaONUMCHChVWEsQC7bL3Z2Z8MkncGS8UNBcFDCxnXZPi-5SV0jarVOhdaKZyFk0HjZWMQ3jVn-K152E1s3Ct-K_dCn04fB_eIy2qUAvwsKoxdnHBCBRBe47AQd-M1LY8hlAi7WMGL7MOVb9Pw7svClY1z6nxq_6ddGZYSddGpqhn5jCaZ1Igps_qvnxNudUZvvIJGiUab9ufywrNzxuhv29WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمله موشکی ایران به پایگاه موفق سلطی در اردن
🔹
این پایگاه میزبان نیروها و هواپیماهای آمریکایی است. پایگاه در حال حاضر در آتش است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/672394" target="_blank">📅 05:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672393">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mD2k5PRF8_LAjFFaTXWb97FCJvTulyLUxJlkZTmKzFaVXX9G1PFqw1k2HZoyvP2nd8QYnaKgRZCb-vC_sDNE5WqbflkWWck6dAC3n480jZvwrye4IZJgcIyg6ym_zJRB52WU79I7OOCA5Txs1QL3a_Bd9F4U4ilQntGq6NJ-DL-9Q3vp2MaPo9vN8-bc9grAojLnBKNc9qXMA_LA-3vlhZ7QtlZiRIXjs16YrMdVK8FWQSK1x3654pAac2WcndoYWLWeio11SyKu-U3LFf_NFdiE5UrnAqQEJCjd67uS8WauTlYsrlQsesmbhUKQUfj1cOFCWhvb-UIjHRc4txaOqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیروهای آمریکایی به دلیل ترس از قرار گرفتن در معرض حملات ایران به تخلیه دارایی های خود از خاورمیانه ادامه می دهند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/672393" target="_blank">📅 05:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672392">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
حوالی ساعت ۵ صدای دو یا سه انفجار در خرم آباد شنیده شد
./ ایرنا
#اخبار_لرستان
در فضای مجازی
👇
@Akhbarlorestan</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/672392" target="_blank">📅 05:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672391">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
سازمان تروریستی سنتکام: هفتمین شب متوالی از حملات علیه ایران را به پایان رساندیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/672391" target="_blank">📅 05:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672390">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aee131af51.mp4?token=kEfpDXgalg6tx978mlvMs3MnzlggPcHrQqWSqNDUB41nykbZYdOvbxBOjoBc3Kx_i0YFIes8icz5SRjIIHoA8G9PuK-tKWNwj143FC3C0bq4cOghHSso0OK2cAi3DEpmOlZBjWvPZy1mCJGkMpKoUTttxLWoTCpgGbcA3zsCQ2XU4H0blkNs2qBMryu28ECVorppCdFy1Fa5f20OVfFU-BtxVmD4kkMFcG-A6K1_dUEJikSfTkKUNTg8blD-R6lUiaZbdqq0_jtEEwgdXYWftftx0jW9RX70UP-uHDDKaiRPWMTFGvx1HMSxLphzxBS99iyGxP4t9hDb8S4rasH6Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aee131af51.mp4?token=kEfpDXgalg6tx978mlvMs3MnzlggPcHrQqWSqNDUB41nykbZYdOvbxBOjoBc3Kx_i0YFIes8icz5SRjIIHoA8G9PuK-tKWNwj143FC3C0bq4cOghHSso0OK2cAi3DEpmOlZBjWvPZy1mCJGkMpKoUTttxLWoTCpgGbcA3zsCQ2XU4H0blkNs2qBMryu28ECVorppCdFy1Fa5f20OVfFU-BtxVmD4kkMFcG-A6K1_dUEJikSfTkKUNTg8blD-R6lUiaZbdqq0_jtEEwgdXYWftftx0jW9RX70UP-uHDDKaiRPWMTFGvx1HMSxLphzxBS99iyGxP4t9hDb8S4rasH6Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شلیک موشک از خاک کویت به سمت ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/672390" target="_blank">📅 05:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672389">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
ارتش کویت از مقابله با حملات پهپادی خبر داد
🔹
همزمان با شنیده شدن صدای انفجارهای شدید در کویت، ارتش این کشور در اطلاعیه‌ای اعلام کرد که در حال مقابله با حملات پهپادی است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/672389" target="_blank">📅 04:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672388">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
منابع عربی از انفجارهای شدیدی و صدای آژیرها در بحرین خبر دادند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/672388" target="_blank">📅 04:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672387">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
سازمان تروریستی پنتاگون اعلام کرد که تعداد تلفات آمریکایی‌ها در جنگ علیه ایران به ۴۲۷ نفر رسیده است/ ایسنا
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/672387" target="_blank">📅 04:55 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672386">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
حمله نظامی دشمن آمریکایی به حوالی جاسک
🔹
در ساعت ۰۴:۴۴، نقطه‌ای در حوالی جاسک هدف حمله نظامی دشمن آمریکایی قرار گرفت.
🔹
جزئیات این حادثه پس از انجام ارزیابی‌های اولیه و جمع‌بندی اطلاعات، متعاقباً اعلام خواهد شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/672386" target="_blank">📅 04:51 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672385">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7a40b49b4.mp4?token=Lgihpy2jeKNNI0ndPTjSR8sbs3GMZmnlD4a8wAzLsQarRHL3pzlAE-zaAgyGJxoGhQ_re2rx6glJgB1jOwBVdAjuz1jUOWpLsQ6IV4Wlr3Mem2nxLOy1BE4F_ZeJBACGiMpOAoE1JENbihcXZPPmxNt9WJGpjCOSdiEN7SIDgFTEXicsOduQkDlZhgPdMkO12cXzkqZ1AqAqGu4Yu367Dt76NlY9ZEe2jA-oDpJVJT6pnHpTLtvDgQjkqEBOActdDw87WXLQP6u4drcU76DJwnvqospSmUEYDkftV0gfIir0wyriIXjjppg2Jssi7ydZlFVIaFZraMVVbo-V5ddujg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7a40b49b4.mp4?token=Lgihpy2jeKNNI0ndPTjSR8sbs3GMZmnlD4a8wAzLsQarRHL3pzlAE-zaAgyGJxoGhQ_re2rx6glJgB1jOwBVdAjuz1jUOWpLsQ6IV4Wlr3Mem2nxLOy1BE4F_ZeJBACGiMpOAoE1JENbihcXZPPmxNt9WJGpjCOSdiEN7SIDgFTEXicsOduQkDlZhgPdMkO12cXzkqZ1AqAqGu4Yu367Dt76NlY9ZEe2jA-oDpJVJT6pnHpTLtvDgQjkqEBOActdDw87WXLQP6u4drcU76DJwnvqospSmUEYDkftV0gfIir0wyriIXjjppg2Jssi7ydZlFVIaFZraMVVbo-V5ddujg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله به زیرساخت‌های ایران
روایتی از محل حمله آمریکا به جاده بندرعباس رودان
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/672385" target="_blank">📅 04:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672384">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
اطلاعیه شماره ۲۶/دو فروند کشتی نفتکش با عبور از مسیر مین گذاری شده جنوب تنگه هرمز منفجر و دچار حریق گسترده شدند  سپاه پاسداران:
🔹
ملت قهرمان و بصیر ایران اسلامی؛ حضور شما در صحنه و حماسه آفرینی خیابانی شما، همانگونه که قائد شهید امت فرمودند سوخت موشک‌های…</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/672384" target="_blank">📅 04:34 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672382">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uD37--ZB1To11aYVlq4TxFvwcmKGXz8-TFJhdLffj-lYp34E6QcFTAuP0xtjBr8sR_kjSjwu3k1Qhz3vfZw8UGAAuoKY2i_jVvtSEVPymarmsZjHowR_xazz5fXpaMmbFmYUNv7kEprLE5WJJ0drQ5mkW5T-Pa1DBoAOqBHjs11oP_c7HlnXYHBm1Fyy_w0rXJWRHzwuW5v9xQNlkF9DFtwGLeFiX2JQvaOdDOlu00tSswcY-VShTGxWcpYpcIPejRNSTppNbbsIug_-5_NxXrwlxIrxyKYTadqOtKa4K-QvUaLUZ7wd6vdjRzkihRkbt_D3_kqA0tCehK_S0hq0Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xpc9MFbcIMI8CSk3y5GBQHzscML1MsElwQJva7czT_5kvov44lZ2veh-szQcuXBBg_oFQWWTcoGkEWgaA_3Ni0ewGumqLVQEMCb_F198s0t47lhNJ_ncqISznHJs7STJMX8oKDd40myYvecYYK54v2IECefWGQWnvrnDe7BL070ADByl5H_cl2hBfQkY4GXUuFa-V_CX-kOArExF9vesBJmFnLiojWMQ_nh9_1sjFS1jDY4caUA66TiN9WfRaOL6wDoVDknLvviym5zs6dojsbclyP60jmUJ93POrsyLjqbe3xdPTHqMCB0_qb947aCmGG5gnHmprcT6rKA6WtPnzw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
منابع عراقی: شدت آتش‌سوزی مقر گروهک‌های تجزیه‌طلب در سلیمانیه به‌حدی است که آتش‌نشانان کنترل آتش را از دست داده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/672382" target="_blank">📅 04:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672381">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
سازمان تروریستی پنتاگون اعلام کرد که تعداد تلفات آمریکایی‌ها در جنگ علیه ایران به ۴۲۷ نفر رسیده است/ ایسنا
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/672381" target="_blank">📅 04:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672380">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
انسداد محورهای مواصلاتی هرمزگان در پی حملات دشمن
🔹
در پی حملات به زیرساخت‌های جاده‌ای هرمزگان، تونل «شهید میرزایی» (محور بندرعباس-حاجی‌آباد) به طور کامل مسدود شد.
🔹
همچنین پل «شور» و پل محور سه‌راهی میناب به رودان نیز مورد حمله قرار گرفتند. از شهروندان خواسته…</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/672380" target="_blank">📅 04:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672379">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
حمله نظامی دشمن آمریکایی به حوالی بندرعباس
🔹
در ساعت ۰۳:۵۰ نقطه ای در حوالی بندرعباس مورد حمله نظامی دشمن آمریکایی قرار گرفت که گزارش تکمیلی پس از ارزیابی‌های اولیه متعاقبا اعلام خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/672379" target="_blank">📅 04:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672378">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WW0oF2bxZYg10T6cBcLstQulRZkHmzn1UIFHV__HmVrpXdSBPHH1AQnA3pZrawdt-EddpdxP3D_ICai_a_8KhX41oUVFI9YehYJ148fk_vxlVTRX_0dshnqnyi--4KJzjYcqAur8cjL-VfXfIk_2smfVyvF8DzENxcSXPyR0tZGkvoZEZ0I_UNKIF4J7LoPTTHnMfttn-lFtFXrHrE-mho18KlZCod2ihu7V4FgOfcfUIfC8fKqODPSwz8vgpO3dYiiYX9EhgTma_PODLg5E3k3EYUTRkDfrW3hSvQvkdgHOST0mokWbtGkJoU53yjdYGGHMdK9KVp8VIvLtuPa50A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شیرجه سهمگین موشک ایرانی بر روی پایگاه موفق السلطی در اردن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/672378" target="_blank">📅 04:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672377">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
ارتش کویت: پدافند هوایی کویت در حال حاضر در حال مقابله با حملات پهپادی است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/672377" target="_blank">📅 03:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672376">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/192eb09786.mp4?token=TavLgv1CgVJ8gVb9RIQ5ZsU6w-dED6aI8K8qj61iyvy79606tnpXBh6ILR8DUJHgjAOiZwHl1SMpPF_zO5-uDhEuHQplBZ39-2eNVHStmpXjm8TJeKWRqiTJmjQ5aBs4pm3dYgqkQnNhPZ4kj3WjqFFLPqXbr_kBcaTeunObJsCXZ6ZHpzD7HT1c5XIXiuQOcv3B_loT6xQnyfCDenzDV59RUl5TUIlF8asweLcL3GTF0DPbSeQgBOARZtJmt56pP0RIZL5CEQy-_9LkFU_D23C15uJ0r_cqLYPN8PdCjZOyEK5fkLWOdmb3zd8GPl6CgOAVZ3Oe4KjgbI4hMFxjJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/192eb09786.mp4?token=TavLgv1CgVJ8gVb9RIQ5ZsU6w-dED6aI8K8qj61iyvy79606tnpXBh6ILR8DUJHgjAOiZwHl1SMpPF_zO5-uDhEuHQplBZ39-2eNVHStmpXjm8TJeKWRqiTJmjQ5aBs4pm3dYgqkQnNhPZ4kj3WjqFFLPqXbr_kBcaTeunObJsCXZ6ZHpzD7HT1c5XIXiuQOcv3B_loT6xQnyfCDenzDV59RUl5TUIlF8asweLcL3GTF0DPbSeQgBOARZtJmt56pP0RIZL5CEQy-_9LkFU_D23C15uJ0r_cqLYPN8PdCjZOyEK5fkLWOdmb3zd8GPl6CgOAVZ3Oe4KjgbI4hMFxjJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برخی منابع خبری: سامانه‌های دفاعی آمریکا و اردن نتوانسته‌اند هیچ یک از موشک‌های شلیک شده به پایگاه موفق السلطی را رهگیری و منهدم کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/672376" target="_blank">📅 03:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672375">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
وقوع چند انفجار در بحرین
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/672375" target="_blank">📅 03:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672374">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
اصابت موشک‌های ایرانی به پایگاه موفق السلطی اردن، محل استقرار ارتش تروریستی آمریکا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/672374" target="_blank">📅 03:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672373">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80c3e5dae0.mp4?token=SI5kb92Zg8NXVauk8Q66uSO5RXY4W6eC3cUDSrnydhpj6TczK1qx_sHuUMz4410hoV8IiqoAEIIvxG00KZdOiFlRDaBmlYqun-4yMkoWC4wrQUkzup7bNRdp9Ju35I9dcNRAKNnlqSh-ig5SEtoxLhTY8Xun4W0ZeLpojUvDKnpNr56BMYUzmuclj6pxFOMkDfXPDEwwHN5qv_Ng9YsbGmH6QMWQhp8I5H2RvC6Ux6XbPSdYTE14E8Br0_EjfTlNX-f4iSOgQRUVkhaC5PappB_iKxOSC0MkRxSwSk5XViXgY0ZCU4wLlL4ZlWM8-y1SRj6iGCDowj3u6pdhA4piPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80c3e5dae0.mp4?token=SI5kb92Zg8NXVauk8Q66uSO5RXY4W6eC3cUDSrnydhpj6TczK1qx_sHuUMz4410hoV8IiqoAEIIvxG00KZdOiFlRDaBmlYqun-4yMkoWC4wrQUkzup7bNRdp9Ju35I9dcNRAKNnlqSh-ig5SEtoxLhTY8Xun4W0ZeLpojUvDKnpNr56BMYUzmuclj6pxFOMkDfXPDEwwHN5qv_Ng9YsbGmH6QMWQhp8I5H2RvC6Ux6XbPSdYTE14E8Br0_EjfTlNX-f4iSOgQRUVkhaC5PappB_iKxOSC0MkRxSwSk5XViXgY0ZCU4wLlL4ZlWM8-y1SRj6iGCDowj3u6pdhA4piPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله پهپادی ارتش به پایگاه‌های آمریکا در کویت و اردن
روابط عمومی ارتش جمهوری اسلامی ایران:
🔹
در مرحله چهاردهم «عملیات صاعقه»، پهپادهای ایرانی انبار مهمات و مراکز پشتیبانی در «اردوگاه العدیری» و پایگاه «علی‌السالم» کویت، و همچنین مخازن سوخت پایگاه «الازرق» اردن را هدف قرار دادند.
🔹
ارتش جمهوری اسلامی ایران با تاکید بر اینکه وارث غیرت و ایثار ملت بزرگ ایران است، هشدار می‌دهد: هر قدرتی که سودای آزمودن اراده ملت ایران را در سر بپروراند، با عزم راسخ و آمادگی نیروهای مسلح  و مردم قهرمان و نستوه این سرزمین کهن روبه‌رو خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/672373" target="_blank">📅 03:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672372">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
جزیره
لارک مورد هدف قرار گرفت
🔹
گزارش‌های محلی از اصابت موشک به دکل مرکز کنترل ترافیک دریایی در جزیره حکایت دارد./ تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/672372" target="_blank">📅 03:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672371">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
وقوع چند انفجار در بحرین
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/672371" target="_blank">📅 03:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672370">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8c5a8ae3b.mp4?token=rO_ZU6xJ0U1gtpq41Tk4Sx_zUKd8YqIq4qEBzyIBttHCoBxiwZdDUkgNbnrpGL9-DTUANri3zhrt-ASGqoWq_xESagUj0vVizNZ0rwB2X2X0ke-7yPNoS-C4XZuZSj7yiJUFdQtEP5j046SKwp16Wqc17vpY4cnuzPruhod1tcegXIYR7_WM4RsaDt8oLFYu1MgaWgGFmSqW-ZnDJDwYoiVd5oyA5NlW6SzE0mCXh_dxsJ8FLc91pobhU2RYTaTdju-W8g2XyaoSwlYIbI0dUnT5N_XY-5LSZ6y9QPKiwyQYXaT_amxe_SnsAo6TkCVvl4MOLzOAvvK368WLPaxywn-8mkdftc1K7-DxdbM29MaYE_fRvt8REzE4U8DdipgFMlgxY1hl9WEJ0fusPdNujkLEX7zEg2NpAV2lqlNRYaXIoNYbGx3nHKjd4xhNPIXDNiYRH3cYOteDmWD8CrOUIXWrCHOrUGVsIfYu9V1HCTCAQxqV6FG96OShJyEfBtvVPJBHj7jGEudxuD66-SE2U0xDkMpJ5J_4Ak0S91WiWm5bGq1umdTmLHNHA9pU2S7FpTaOtljsFm2KD3CysGLstHM229SL1q04LAuwZdT75fZ6X31fcJvxmZyATbSjJOaLc98K9IpD_WMIWGzoPoBaifDIfHOVqRTmXymKDSf7ieY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8c5a8ae3b.mp4?token=rO_ZU6xJ0U1gtpq41Tk4Sx_zUKd8YqIq4qEBzyIBttHCoBxiwZdDUkgNbnrpGL9-DTUANri3zhrt-ASGqoWq_xESagUj0vVizNZ0rwB2X2X0ke-7yPNoS-C4XZuZSj7yiJUFdQtEP5j046SKwp16Wqc17vpY4cnuzPruhod1tcegXIYR7_WM4RsaDt8oLFYu1MgaWgGFmSqW-ZnDJDwYoiVd5oyA5NlW6SzE0mCXh_dxsJ8FLc91pobhU2RYTaTdju-W8g2XyaoSwlYIbI0dUnT5N_XY-5LSZ6y9QPKiwyQYXaT_amxe_SnsAo6TkCVvl4MOLzOAvvK368WLPaxywn-8mkdftc1K7-DxdbM29MaYE_fRvt8REzE4U8DdipgFMlgxY1hl9WEJ0fusPdNujkLEX7zEg2NpAV2lqlNRYaXIoNYbGx3nHKjd4xhNPIXDNiYRH3cYOteDmWD8CrOUIXWrCHOrUGVsIfYu9V1HCTCAQxqV6FG96OShJyEfBtvVPJBHj7jGEudxuD66-SE2U0xDkMpJ5J_4Ak0S91WiWm5bGq1umdTmLHNHA9pU2S7FpTaOtljsFm2KD3CysGLstHM229SL1q04LAuwZdT75fZ6X31fcJvxmZyATbSjJOaLc98K9IpD_WMIWGzoPoBaifDIfHOVqRTmXymKDSf7ieY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
موشک‌های ایرانی بر فراز پایگاه موفق السلطی اردن محل استقرار ارتش تروریست آمریکا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/672370" target="_blank">📅 03:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672369">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/049b5524e5.mp4?token=jj41LPdDCAr8ZdjxxHux1F18DiDZKjz4bXvbnc9B4nohiPGnlpv61jzJZQTaiyE5B4rhBqhrZifmtkAJREk4bEcCecijy7Ni6GlJKIMDqDlz8dM-0UbpjDTcsZjK_LVtuN5lK9QHQrhVHBzotYxf6P1WMGb73YQlET0X-0qmKUF_dcBiyJmLOM4XEHeFGxwIh3qECCbJ0XmWOmZ8UIAn_drIu6h0aEFIkBOiF69xjqYe5_wBeTv08kFi1drXes2seD1F4j_uaMCpRyVl3cLlnIlIrSghAEgpFulmtPt7h9hRZy449Q2PRrrHT2NW-h9z91W-7GWAcBh29qF0qsQgdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/049b5524e5.mp4?token=jj41LPdDCAr8ZdjxxHux1F18DiDZKjz4bXvbnc9B4nohiPGnlpv61jzJZQTaiyE5B4rhBqhrZifmtkAJREk4bEcCecijy7Ni6GlJKIMDqDlz8dM-0UbpjDTcsZjK_LVtuN5lK9QHQrhVHBzotYxf6P1WMGb73YQlET0X-0qmKUF_dcBiyJmLOM4XEHeFGxwIh3qECCbJ0XmWOmZ8UIAn_drIu6h0aEFIkBOiF69xjqYe5_wBeTv08kFi1drXes2seD1F4j_uaMCpRyVl3cLlnIlIrSghAEgpFulmtPt7h9hRZy449Q2PRrrHT2NW-h9z91W-7GWAcBh29qF0qsQgdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آسمان الزرقاء، اردن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/672369" target="_blank">📅 03:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672368">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
انفجار در کویت
🔹
منابع عربی از چند انفجار شدید در پی اصابت پرتابه‌هایی از سمت ایران خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/672368" target="_blank">📅 02:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672367">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a67fed2838.mp4?token=Akrs0FTVt7MmRELHbvxLoY1f0N4JAqeuDq5xW8w4jO2cAYuPLCbkLJUCA3rHbJZ8etWAssZRCfVb3Cd1rCfuL1_80Wg5ata0dBNem_8A3KM_E8dw8bTs3kOXfTRdx_qdVhygA2vflF3Ryi4JfWIvjoYbx_ulz6jStj17BD6dPLMzDWwO6YyStMFfiKPjiMYDe2KeHgADO_d9_uyNOCfOlm42llfpkeWcvRKCuEAfJsFhuFjfA2IDi6jcnx1hCuSlY_LwJuBB3k7W6SRNMJLqhJgBQwjCFUPDraPHE72To1uYJt2I4cJVljY2OdBYp2hfRQ-g6HQwK5Q01ouxdjUyQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a67fed2838.mp4?token=Akrs0FTVt7MmRELHbvxLoY1f0N4JAqeuDq5xW8w4jO2cAYuPLCbkLJUCA3rHbJZ8etWAssZRCfVb3Cd1rCfuL1_80Wg5ata0dBNem_8A3KM_E8dw8bTs3kOXfTRdx_qdVhygA2vflF3Ryi4JfWIvjoYbx_ulz6jStj17BD6dPLMzDWwO6YyStMFfiKPjiMYDe2KeHgADO_d9_uyNOCfOlm42llfpkeWcvRKCuEAfJsFhuFjfA2IDi6jcnx1hCuSlY_LwJuBB3k7W6SRNMJLqhJgBQwjCFUPDraPHE72To1uYJt2I4cJVljY2OdBYp2hfRQ-g6HQwK5Q01ouxdjUyQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رسانه‌های عربی: صدای انفجارها در پایگاه‌های آمریکایی اردن به حدی بود که در مناطق اشغالی شنیده شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/672367" target="_blank">📅 02:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672366">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AxFE3iMV16qo3smsgSpliPICwnf3DHgzFaxhpL6aA4lHtvU87XzgkTaV8mbsQbSRQSmCTKO4ZBNVydOSDW87SAf691Zzc96Uz1G45XQ0QWt1_HGd5ikeAKcKjipC6SfZROC7ZaH8hJZE72n5halfOWKlXBVfKev8v5wbkq4P4Xw-zfkYDJeA36NPhG4l4DRy2je2fSHqKCRTP-FAlrDNdNM9_2fH-gMXKEMrWHuzHZNcO5T5iQh8tRevv8CqxmQT1nR9nVWxfOvY4Kgd9kQ5fsrw1sdkoz1_T9fxJisivsmGpMxRqxQ4PqJpyaFy8iU26VxCLCT6K-85h-ZhScxD2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای اکسیوس به نقل از مقام آمریکایی: ایران یک موشک بالستیک به سوی یک پایگاه آمریکایی در عربستان سعودی شلیک کرد
🔹
این نخستین حمله ایران به عربستان است پس از ۴ ماه.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/672366" target="_blank">📅 02:51 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672365">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
بر اساس گزارش‌ها، آژیرهای هشدار در شهرهای الخرج و ینبع پس از رصد شلیک موشک از ایران به صدا درآمده‌اند/ تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/672365" target="_blank">📅 02:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672364">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
رسانه‌های عراقی: صدای انفجار در اردن به گوش می‌رسد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/672364" target="_blank">📅 02:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672363">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
فرماندار بوشهر: لحظاتی قبل یک نقطه اطراف شهر چغادک از توابع این شهرستان مورد اصابت تهاجم دشمن آمریکایی قرار گرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/672363" target="_blank">📅 02:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672362">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
انفجار در کویت
🔹
منابع عربی از چند انفجار شدید در پی اصابت پرتابه‌هایی از سمت ایران خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/672362" target="_blank">📅 02:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672361">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
معاون استاندار هرمزگان: در پی حملات دشمن به برخی نقاط استان هرمزگان سه نفر شهید و ۸ نفر مصدوم شدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/672361" target="_blank">📅 02:39 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672360">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
صداهای شنیده شده در لرستان مربوط به شلیک موشک های رزمندگان اسلام است
🔹
مردم عزیزمان نگران نباشند./ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/672360" target="_blank">📅 02:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672359">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">‌‌
♦️
منابع عربی: پایگاه‌های نظامی آمریکا در عربستان سعودی، هدف حملۀ موشکی قرار گرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/672359" target="_blank">📅 02:36 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672358">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
فارس: دقایقی پیش اهالی امیدیه خوزستان از شنیده‌شدن صدای انفجار خبر دادند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/672358" target="_blank">📅 02:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672357">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
رسانه‌های عربی از وقوع چندین انفجار در عربستان سعودی خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/672357" target="_blank">📅 02:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672356">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
رسانه‌های عربی از وقوع چندین انفجار در عربستان سعودی خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/672356" target="_blank">📅 02:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672355">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
ایروانی: آمریکا مسئول کامل تلفات و خسارات حملات علیه ایران است
🔹
سفیر و نماینده دائم ایران در سازمان ملل متحد در نامه‌ای به دبیرکل سازمان ملل و شورای امنیت، آمریکا را مسئول کامل تلفات جانی و خسارات ناشی از حملات اخیر علیه ایران دانست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/akhbarefori/672355" target="_blank">📅 02:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672354">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
رسانه‌های عراقی: صدای انفجار در اردن به گوش می‌رسد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/672354" target="_blank">📅 02:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672353">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPuovJgSDNyP5FFRZA9jx1lNplBv69UR8ODmDBRLlr9KzS9n3eFG0J2WEa1fQNq4sziGgMttsbi1RCz8RFYBuzcpzi6-cbEB4tOIDQ4QUM1y_uzQWICXtZLsicn5rLWfWHmfRdi_rWlb0AoocJfm00CFPhpJ1bUsWlf1CwmCxuLeoITqtM-dtEkT0C3XmyHwq1ZtmzSsAetN6uRozwtX7HvBn8OmbZd4YBR0nkHA0U_Ord3d4sk014RDiNplQIyIKeFZWAxLP1e-cxL2iaOJuD_XRyQ4pk_aWmOg7Geyqne-b2eKO2Hy-pGslVUcubkpn86SOQdZNBiBtfXUWB3diQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیروی دریایی سپاه: در ساعات گذشته ۴ کشتی متخلف متوقف شدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/akhbarefori/672353" target="_blank">📅 02:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672352">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
حمله پهپادی مجدد به اربیل و انفجارها در پایگاه‌های اشغالگران و تروریست‌های تجزیه طلب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/672352" target="_blank">📅 02:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672351">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
تایید مسئولیت آمریکا در کشتار مدرسه میناب
🔹
تحقیقات مشترک «اسکای‌نیوز» و آژانس «معماری قانونی» با استناد به تحلیل‌های فنی، بررسی‌های منبع‌باز و شهادت بازماندگان، مسئولیت مستقیم ارتش آمریکا در حمله به یک مدرسه در شهر میناب را تایید کرد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/akhbarefori/672351" target="_blank">📅 02:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672350">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
سی‌بی‌اس نیوز به نقل از مقامات آمریکایی: در جریان حملات هفته جاری به دو پایگاه در اردن، شماری از نظامیان آمریکایی مجروح شده‌اند/ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/akhbarefori/672350" target="_blank">📅 02:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672349">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
انسداد محورهای مواصلاتی هرمزگان در پی حملات دشمن
🔹
در پی حملات به زیرساخت‌های جاده‌ای هرمزگان، تونل «شهید میرزایی» (محور بندرعباس-حاجی‌آباد) به طور کامل مسدود شد.
🔹
همچنین پل «شور» و پل محور سه‌راهی میناب به رودان نیز مورد حمله قرار گرفتند. از شهروندان خواسته شده است تا اطلاع ثانوی از ترددهای غیرضروری در این مسیرها خودداری کنند./ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/akhbarefori/672349" target="_blank">📅 01:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672348">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
افزایش سطح آماده‌باش سنتکام در پایگاه‌های منطقه
🔹
فرماندهی مرکزی آمریکا (سنتکام) با استناد به ارزیابی‌های اطلاعاتی درباره احتمال حملات تلافی‌جویانه، سطح آماده‌باش نظامی در تمامی پایگاه‌های ایالات متحده در منطقه را افزایش داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/akhbarefori/672348" target="_blank">📅 01:55 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672347">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
حملات دشمن آمریکایی به اهواز، لار، یزد و چند شهر ایران
🔹
ارتش تروریستی آمریکا در ادامه حملات نامشروع امشب به خاک وطن، برای چند بار متعدد مناطقی در شهرهای اهواز، بندرعباس، قشم، لار، داراب و یزد را هدف موشک‌های خود قرار داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/akhbarefori/672347" target="_blank">📅 01:45 · 27 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
