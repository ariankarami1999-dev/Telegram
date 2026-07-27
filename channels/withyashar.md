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
<img src="https://cdn4.telesco.pe/file/XE2AfZ8KAxP7vqgjTayhmFRWqLjdWD9nRNgRLwBLTBoIedyZgpvCkusoZrXF4kqInZCHa7QRI_a6nmWpwxWN8HcPti74WFRmr4BWnNzWlRsADHruuJB0DyMcpxGEukTzdODVErV88f6f9bmmeRpEJ76qru0EmsEtdyus7Ferz6LIufagy7M-wFIrAyaC7dgcP0tRM41Sauv-dTxp51XnR9v89-NxH_Bqw3Vm2lut0YY1jWYfhwjclvaCzEIU-av2UXv2WEZd8udyMSIRKR74OvNp08K6iir7DEHo9mWFWXhcQwDcDl6TbxZFtYcGTnVdPVP0I_OJQEZhFEAvvwh1Rw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 428K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-05 18:50:44</div>
<hr>

<div class="tg-post" id="msg-19823">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ترامپ به شبکه ۱۲ اسرائیل گفت: به درخواست واسطه‌ها پاسخ دادم تا فرصتی برای مذاکره با ايران فراهم شود.
"من زمان زیادی را برای مذاکرات اختصاص نخواهم داد."
@WarRoom</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/withyashar/19823" target="_blank">📅 18:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19822">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ترامپ به شبکه ۱۲ اسرائیل گفت: ما در حال انجام مذاکرات عمیقی با ايران هستیم و اگر این مذاکرات موفقیت‌آمیز نباشند، به یک عملیات نظامی گسترده باز خواهیم گشت.
@WarRoom</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/withyashar/19822" target="_blank">📅 18:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19821">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">کاظم دست کج : در اسلام‌آباد طرف آمریکایی ۲ درخواست افراطی داشت و اصرار داشت که مسیر جنوبی تنگۀ هرمز فعال باشد و گفت اگر آن‌ها را نپذیرید مذاکرات شکست می‌خورد و ما برمی‌گردیم؛ ما درخواست‌ها را رد کردیم و گفتیم برگردید.
@WarRoom</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/withyashar/19821" target="_blank">📅 18:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19819">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fU7Rv_XYlLcqq9QO_z_VyL5iNf2g7v9_4kT8UiMBsbOcJ_4h_A93Lt2PrWdXbt8pPlYlpIQFVo-DV_hUyxFrYntz6tWAMAKp22AclPnslQEUmA-w-TvWCLe8z9vBdUOCg4ady2WLDDIq2D_cmi5phwqAnYsPXze9jmb2EqPSiVvmvqC7evd4zbrkkF50q2hqRFZdFv2wt4AjRH8FDXgfOkP2SDuXt0DruIkOvZoSMR-DjLLqjvT0Enl8ZeBlA8-n2myZscuvxLWdXQWVgV5ulCeDWLBBhfollo5ao5r5Kr0In3UwJQYggXZpCPsGD3PB9zyWiA-ik-DBdjgf9-roDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک فروند پهپاد MQ-4C آمریکا پس از فعالیت در خلیج فارس، نزدیکی ایران، در آسمان عربستان سیگنال اضطراری ۷۶۰۰ ( از کار افتادن ارتباط رادیویی ) صادر کرد و به مقر خود برمیگردد ، همچنین ادامه پل هوایی ترابری سنگین نظامی آمریکا را شاهد هستیم
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/withyashar/19819" target="_blank">📅 17:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19818">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">وزارت امور خارجه عربستان : ما پهپادهایی که قصد هدف قرار دادن تاسیسات نفتی در مناطق شرقی و ریاض را داشتند از بین بردیم همچنین این حملات را که توسط شبه‌نظامیان تحت کنترل ایران در عراق انجام شده است محکوم می‌کنیم و تأکید می‌کنیم که پادشاهی عربستان سعودی مصمم است جلوی متجاوزان را بگیرد.
@WarRoom</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/withyashar/19818" target="_blank">📅 16:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19817">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">همشهری: سران قوا با بنزین ۱۰ هزار تومانی برای سهمیه سوم موافقت کرده اند.
@WarRoom</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/withyashar/19817" target="_blank">📅 15:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19816">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">جی دی ونس در انتقاد از اسرائیل برای جلوگیری از مذاکرات:
من قطعاً فکر میکنم شاهد یک کارزار بسیار پنهان و با بودجه بسیار بالا بودیم که تلاش میکنه مذاکرات رو منحرف کنه و مانع رسیدن به توافق بشه.
@WarRoom</div>
<div class="tg-footer">👁️ 93.1K · <a href="https://t.me/withyashar/19816" target="_blank">📅 15:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19815">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbef676e41.mp4?token=Xgul2ZIcIhO0PHUSPzlQLWgNvw0Y3Z15Cox6a2aF8U0UWrW_eyXT07y7yIo54afwqrOFjJKOHOaeltFy7mwMOQJrADKaOhW_agGhAO3zE-apOt_cjGRxJ2jGCQjB8v5_8EtkDsobAkm7TukgRcPfBJZ4WdfUaBZ9_vKrjXAjd4_xPIf2FMWxCvlAEsZB_vYP-ifNvqGOeFDXrGOan7dFWoHw4TCw-DJlCt4Z7NULQmQJitOSeN6g4BDYihZnj86G3TzjQ_LBketPktyjq3m1C2K_XXc9y8HmoYQ9fSC3sVsbhfLArjIx2Ib59dR4canBSJveNk1k86pIR0mPgRhYHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbef676e41.mp4?token=Xgul2ZIcIhO0PHUSPzlQLWgNvw0Y3Z15Cox6a2aF8U0UWrW_eyXT07y7yIo54afwqrOFjJKOHOaeltFy7mwMOQJrADKaOhW_agGhAO3zE-apOt_cjGRxJ2jGCQjB8v5_8EtkDsobAkm7TukgRcPfBJZ4WdfUaBZ9_vKrjXAjd4_xPIf2FMWxCvlAEsZB_vYP-ifNvqGOeFDXrGOan7dFWoHw4TCw-DJlCt4Z7NULQmQJitOSeN6g4BDYihZnj86G3TzjQ_LBketPktyjq3m1C2K_XXc9y8HmoYQ9fSC3sVsbhfLArjIx2Ib59dR4canBSJveNk1k86pIR0mPgRhYHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: من با رئیس جمهور ترامپ در مورد مسائل مختلف گفتگو خواهم کرد، و در صدر این مسائل، ايران قرار دارد.هدف از سفر من به واشنگتن، تضمین امنیت، قدرت و آینده اسرائیل و همچنین گسترش دامنه صلح در منطقه است.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/19815" target="_blank">📅 15:06 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19814">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wyr-RRt-PiXNdSbF7KI5mIZmJxUsqe5VnRA4S97N5t8zOo-J_55BW29IocGadC9UXJGlooj4LmXs_vH_cWkGmSa_lOzkBLPhj81ImZh-8dq79HwQxlZA2xlD7ws5PU_J3As_msA0XDEBueGeL3GiWND--lBnAfyePCYCc3DN6HGx7bQ9WpXJk-YjRG3NSrAKFuabesS2LhW8Z88wiI3QGRqWbbAZy2WEih2RFxfIFE26F7A_9F0tyXBRA5E3EqL_Y5kcun2WN-47wEO-iJ0UmQRWFBv2q4knfxDM3XITqgBzhwWDc5gNFZ4Tppqs_UV7Vv-Faz0jn69kzZxqEAh5jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون کرج سمت فرودگاه پیام
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/19814" target="_blank">📅 14:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19813">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">صداوسیما: تلاش آتش نشانی برای نجات ۳ نفر که در طبقه سوم ساختمان مجاور هتل استقلال محبوس شده اند @WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/19813" target="_blank">📅 14:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19812">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tI38umdr4LCmYvF2p60GCkdhuMtDEFuViK8xEh1xYQrkSWYTpzTJfO5QMWJrTbPfotaWt39m9RlEU4rInU1Kwx7aKRJfRBjRq7QHedmYplC39EYQTeRRGsctZQb_OCNIgLBvwxqKiqCURzZ_uEqiEtinsSghqHMhwbP83sTydbS6SfozTi3Gxd4811OlERPBZIe1Z-NFwDcFpXv-o2pymn06Ro-PL-MZmlbWycfdvHwB3Od1biiVHvVeY1jZjWUUdfQ1Qzxq5myAFOEL8SVkQd1DthTSjg0rl_X7YEMi6_f2iJtByJT9uva5YR9qJnk9R14UQBOLVq6Q6YRZHwabhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در دهه هفتاد میلادی، در زمانی که در منطقه کسی نمیدانست سوخترستان حتی چیست. عکس بسیار زیبا از سوختگیری دو فروند بویینگ 747 شاهنشاهی بر فراز دماوند.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/19812" target="_blank">📅 14:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19811">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">هواپیمای استاد بزرگ شطرنج بی بی نتانیاهو  تیک آف کرد و پرید ! تا کور شود رسانه هایی که خبر تاخییر رو کنسلی انتشار میدهند @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/19811" target="_blank">📅 14:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19810">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4f9ca588d.mp4?token=ruMP7pWuvgRwFYGs-r9zyJDfW-y-JRRFLipTLFM1RqI-IckhimE6-Tm4E1mr6zRE0ZgPiL9oyd7qEAtDtWkkx1lB10UXW7Il9GT_aOjwbcC9Sx_bvdNkUvPNRcnOoeRToWo7uQxufBvRALxcIe4OP8xKfFFRIaNpzf-Wjy6sYzUfUo9vmbKMWRHbyM3GQquPiN1wEZnwd6x-4gNbLjdMigiXeJLUi6q2llnxnmgr3Rfwg5sbut9ghUT0a7YMVOeX4o7-L1d4YDuxw8ebHOWEgABAX8VvqhwrbpYW-v-w5oYihm4TvHZE6wA0l61uPvSsB7l8y07a9FhywB5ijFTWGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4f9ca588d.mp4?token=ruMP7pWuvgRwFYGs-r9zyJDfW-y-JRRFLipTLFM1RqI-IckhimE6-Tm4E1mr6zRE0ZgPiL9oyd7qEAtDtWkkx1lB10UXW7Il9GT_aOjwbcC9Sx_bvdNkUvPNRcnOoeRToWo7uQxufBvRALxcIe4OP8xKfFFRIaNpzf-Wjy6sYzUfUo9vmbKMWRHbyM3GQquPiN1wEZnwd6x-4gNbLjdMigiXeJLUi6q2llnxnmgr3Rfwg5sbut9ghUT0a7YMVOeX4o7-L1d4YDuxw8ebHOWEgABAX8VvqhwrbpYW-v-w5oYihm4TvHZE6wA0l61uPvSsB7l8y07a9FhywB5ijFTWGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یاشار : نگران نباشید یک سری مدارک رو و آلبوم رو حتما موساد دیر حاضر کرده  تکمیل کنه میپره
😁
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/19810" target="_blank">📅 13:48 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19809">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bc-ksY_7LKG_n30z6bh7Wq5d7AnYWldORkBpZHugiWIoKIiFsVh-5SokqjrGOMhWr5eHLF2qXfCTnWWKNZmiXmgywS8mrjKO3_mh0OlMewbDTOaDgF9LeYPuBYt3W6uk5GHWFla4ij7MY96OwohMuGB4rBkMw37cs4kDYvGd-CfVpzPuBA2g8ZyxXEsjoA7PQMmE0AaH525nROzdxxVr0rWV_-aZTmkg8zYCfOKolcnCsmslPJVFEa6zzX7s2WwWT9EGJw9D6c8mzOWyxXR2039K_AwlxcAeNuN_lo4h4lt2hlKCp5F-VNsljr_ih_Umlir79eaYLiCNJDGPciYc7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیمای استاد بزرگ شطرنج بی بی نتانیاهو  تیک آف کرد و پرید ! تا کور شود رسانه هایی که خبر تاخییر رو کنسلی انتشار میدهند
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/19809" target="_blank">📅 13:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19808">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/19808" target="_blank">📅 13:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19807">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ایتامار بن گویر، وزیر امنیت ملی اسرائیل گفت: «باید کارهای بیشتری انجام شود. من امیدوارم که دونالد ترامپ، رئیس جمهور آمریکا، متقاعد شود که ساده‌لوحی خود را متوقف کند. او یک تاجر است و در مورد مسئله ایران بسیار ساده‌لوح است. هیچ دیپلماسی با این افراد وجود ندارد، هیچ چیزی برای صحبت با آنها وجود ندارد. باید با ایرانی‌ها از طریق دوربین صحبت کرد.»
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/19807" target="_blank">📅 13:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19806">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">دفتر نخست‌وزیر اسراییل از به تعویق افتادن پرواز ۱۱ صبح وی به واشنگتن خبر داد، اما بدون ارائه توضیحی درباره علت این تصمیم، زمان جدیدی برای انجام این سفر اعلام نکرد @WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/19806" target="_blank">📅 13:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19805">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">دفتر نخست‌وزیر اسراییل از به تعویق افتادن پرواز ۱۱ صبح وی به واشنگتن خبر داد، اما بدون ارائه توضیحی درباره علت این تصمیم، زمان جدیدی برای انجام این سفر اعلام نکرد
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/19805" target="_blank">📅 13:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19804">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jimHdjDWThb19yJ_bRI99jI4dkJFdeRImt9e3GIMIfbCVLj5eovaLzKCn-gZCR0LTpCYyLoJi1xGaBrJF_AD1fq5L5b6hqvoVRj-gUy0WdLKu_XCSBzLpZxxHqgEBoc9A5qyBWNAM4jaKpdODTzF2fNXjtC4MeXifiX9bWsbbu3yP4e7Vvuv8HQbHU2jQcL1VfMilUnawGBvWMgs0c30lFLn7gTUyhnBNCleWNggqoNR-l031K36Ns-FLxFnSWmi4ULm_T13LaUU7ZaPzmXkEkBx0DQQcO9L2x-oRKKlaY0puZIEUIM4grBr4w8-8dtXSEgXHGOn9shfifiWR3nrYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه اطلاعات ۴ مرداد ۱۳۵۶. دقیقا سال پنجاه و شش هم همین موقع ها، هتل هیلتون آتش گرفته بود.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/19804" target="_blank">📅 13:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19803">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">صداوسیما: تلاش آتش نشانی برای نجات ۳ نفر که در طبقه سوم ساختمان مجاور هتل استقلال محبوس شده اند
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/19803" target="_blank">📅 13:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19802">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4db435b3a7.mp4?token=Lae0n2FVqwuKwCFjzp1tQL3Tg2rEXpaNqgj78ftg3pFIr3tWgaXbS1g6tUQ-90t0dDnpHFkOGxg6E_cJ_oCHPMxa0UJ1IA5cOPansZYk5pCESFgQTRBsZqjpm0b8BRSfX7zTsegqMsasAN4sJG0w3hy2u3iW3BoY5UKoypdL2Bwz65pplZ7bhYbPEsJn8oEQrnKILjHKOxUXxXVyKuekNUYw_IP_FoET7NBuiJf1LfYYvRDP_8VFyr4KrnzfS8rZP-TdUfLbwaeM9T92vR9-2KoiuRUNktXWDXBkoqHD6ucZkNm5XCQkXJR-YUs1dIRLZf60ODbfIseaRKQqcb65Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4db435b3a7.mp4?token=Lae0n2FVqwuKwCFjzp1tQL3Tg2rEXpaNqgj78ftg3pFIr3tWgaXbS1g6tUQ-90t0dDnpHFkOGxg6E_cJ_oCHPMxa0UJ1IA5cOPansZYk5pCESFgQTRBsZqjpm0b8BRSfX7zTsegqMsasAN4sJG0w3hy2u3iW3BoY5UKoypdL2Bwz65pplZ7bhYbPEsJn8oEQrnKILjHKOxUXxXVyKuekNUYw_IP_FoET7NBuiJf1LfYYvRDP_8VFyr4KrnzfS8rZP-TdUfLbwaeM9T92vR9-2KoiuRUNktXWDXBkoqHD6ucZkNm5XCQkXJR-YUs1dIRLZf60ODbfIseaRKQqcb65Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هتل در حال تخلیه است
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/19802" target="_blank">📅 13:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19801">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c5G9RPyINcBo75svDWC3cbI5Wco7uOq2qA0s_Cnd40mZNgLlIV6Rnr5ckMId_VR_MQVlZTs3etVSgcp0B1MpHBEMNvAIZ0gyOH5kac3U9VVec-R9zJlpTgj05_p4k8eGPMhwc4amTzAaqBR0h_fY6Ks5SS1pyhdZRgssDrzt-F2lZoP2ZXOK9H4Q8Vl31WdCO_E1n29JtYkiKLaUwtHQVge7Oln56kM6_r1RItyhDsvBskJU-wZHyPaY4S3pd73c_7s2ucUjGu3mfF5MPIGZ7HIe_6PNScnMmI-OwR4L2uVhgh9OvPNigC4MYiY1bBu89nU9jHr6T5EF0A0vr9lBdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتش سوزی ساختمان هتل هیلتون
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/19801" target="_blank">📅 12:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19800">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">جمهوری اسلامی  : تنگه بسته است
سخنگوی وزارت امور خارجه ایران گفت تهران به واشنگتن اجازه نخواهد داد شرایط پایان جنگ را دیکته کند و هشدار داد که تنگه هرمز همچنان بسته است. او همچنین اوکراین را به دلیل حمله ادعایی به یک کشتی ایرانی تهدید به تلافی کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/19800" target="_blank">📅 12:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19799">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b0896ed8.mp4?token=PLP411kNbgyyNIlllCLgbfyc7DWm2waQe0-KjFeZVwtZsEzGJuZq6QjmwJPCesk7GcfP8TDkoCbKTBCsl_N4LM7eU9rrxWdHFSngbD8B87tdNw8lcc-yS2U8yjeDWxr01Jxv8jCrUxhS4ub8XO3IYvVgi_a1UFL5WphmFonYHLPlLRe5jkjs8m-F90iE1jZbxk_RH2I_h-vdJ3UBpd7SvmO9Worcg5QcEgCtCok5b666nNfly7u4gDke63mR4I7Pe_wv09HqVtPM5XAPjF4krFT6TmIU2A7gP6f-ur3ymNDe2EmylrRcDIttb_QnJqQypx2A1yl4M3RZuCVjAOW5nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b0896ed8.mp4?token=PLP411kNbgyyNIlllCLgbfyc7DWm2waQe0-KjFeZVwtZsEzGJuZq6QjmwJPCesk7GcfP8TDkoCbKTBCsl_N4LM7eU9rrxWdHFSngbD8B87tdNw8lcc-yS2U8yjeDWxr01Jxv8jCrUxhS4ub8XO3IYvVgi_a1UFL5WphmFonYHLPlLRe5jkjs8m-F90iE1jZbxk_RH2I_h-vdJ3UBpd7SvmO9Worcg5QcEgCtCok5b666nNfly7u4gDke63mR4I7Pe_wv09HqVtPM5XAPjF4krFT6TmIU2A7gP6f-ur3ymNDe2EmylrRcDIttb_QnJqQypx2A1yl4M3RZuCVjAOW5nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در
۲۰ و ۲۱ بهمن ۱۳۵۷
در پادگان‌هایی مانند
دوشان‌تپه، عشرت‌آباد، حشمتیه، لویزان و مراکز دیگر
مردم برای تصرف اسلحه وارد پادگان‌ها شدند و تعدادی افسر، درجه‌دار و سرباز را کشتند !
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/19799" target="_blank">📅 12:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19798">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">دیدار نتانیاهو و زلنسکی با ترامپ
گزارش ها از سفر قریب‌الوقوع و ناگهانی زلنسکی، رئیس جمهور اوکراین به آمریکا همزمان با سفر نتانیاهو به آمریکا
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/19798" target="_blank">📅 12:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19797">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">سخنگوی وزارت خارجه: درخواست مذاکره کردن اصلا با ژن ما همخوانی ندارد بقایی:ادعای درخواست مذاکره از سمت ایران، صرفا یک خبرسازی است. البته ما درب دیپلماسی را نبسته‌ایم، اما در حال حاضر هیچ مذاکره‌ای با آمریکا در جریان نیست. @WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/19797" target="_blank">📅 11:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19796">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">سخنگوی وزارت خارجه: درخواست مذاکره کردن اصلا با ژن ما همخوانی ندارد
بقایی:ادعای درخواست مذاکره از سمت ایران، صرفا یک خبرسازی است. البته ما درب دیپلماسی را نبسته‌ایم، اما در حال حاضر هیچ مذاکره‌ای با آمریکا در جریان نیست.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/19796" target="_blank">📅 11:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19795">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nkMa2tjEuVtwXScgeMEcsccMbonOibuaTJR_9xALs0BubIzCdhrEseWLgUgOsvjAXRqSK8TLgtV-xSup-MU4bTexlvg80vTZPHL12tjZ6yckcXFr88aHm-7II1PuJEQ8pHcUxah7UWmg6X5m8081heViEyKrpzO6712PSDWn8BP8yJ2Yj9-lHDLPpTL60M2lSadqGrdP631X0MRyKb9fAj5MQwvVZDbArlKIt77XKrPk2G7NiOqsZ4fCPBh3HPhXbYp_pFM5-dZuAYOOAUzaYREi15tgnHiM5X1Wlhi2_53QdCMJQHRAj957_nhtaF-R_INLQ_N-Y08PK54PXFL89w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویری از «نیما مرادی» که در حمله اوکراین به کشتی ایرانی کشته شد. کشتی آنا از بندر آستاراخان عازم بندر انزلی بود.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/19795" target="_blank">📅 11:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19794">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">پوتین: شناورهای تندروی ایران در درگیری با آمریکا عملکردی موثر داشتند
رئیس‌جمهور روسیه در دیدار با فرماندهان و نظامیان ناوگان دریایی این کشور اعلام کرد که ایران در جریان درگیری نظامی با آمریکا با موفقیت از به‌اصطلاح «ناوگان پشه‌ای» (شناورهای کوچک و تندرو) استفاده کرده و این نیروها عملکردی کاملاً مؤثر از خود نشان داده‌اند
، توسعه چنین نیروهایی برای ناوگان دریایی روسیه نیز ضروری است.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/19794" target="_blank">📅 11:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19793">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">هواپیماهای تهاجمی A-10 Warthog برای عملیات احتمالی علیه ایران در خاورمیانه اعزام شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/19793" target="_blank">📅 10:56 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19792">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccbe6758e6.mp4?token=MCSmpeO_1qFq395tQgZwQykrFwYO9CCaB0kdv8RFItuW-YzoY-JDGcJB-aniVhFjO24UJgb_LvNtplXwVS0ZCSscCR9Ufj_coxatFmCa06Hq4drVdt3qmfuiQji7PTOR4JxJmmxIrJcPhVOmrssw4Vyd45-GNNOq6h1v3lJ_G7Td2mCmnlD0WkFMo2ccfKirHiGCHbdsjO3KCtNsP2svBij0yZfXNmBW4jcRhgQJP5JLmI9VQh6doVEvNWEvH_UBKmOr_fmDYTsFeEKK-aoITORK3JwKyFNIpbna_C3Y9TUCc3tM5bRHRoTMs_ztvp8AQUerGaizfFHeXmv8ZhltUTqmnbCKjkEXeGIZT8OAwmR5cgZtRUoU2ZL4m7jJ7GMmCb6g6DAH78P4Nk2cCZDiSDNgSkXkNSm25GJRxaamFQAUWfBo06TOYyLfHtx_gulXUsDXhYvHbKXzhUfiLkKmnVhbtObvL3clmsmGnxYarghS2V08UzfJeqI7VXeb-NKZm1qW4LhUtE5OEuIeIoUbemtZgrS8uElDsTy55ghTRpFwwGdgX5p0smHU8NYKvs2gcy8wF6AR6uG33UmdWKK7gkedhTNv-NSStbLb_p3QnJoGGZdf5a-gijjkujxyqT8DHEvoJ3RiQ41RVxVCheRSlugZXqlFiO0stEOq7jMMUZ0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccbe6758e6.mp4?token=MCSmpeO_1qFq395tQgZwQykrFwYO9CCaB0kdv8RFItuW-YzoY-JDGcJB-aniVhFjO24UJgb_LvNtplXwVS0ZCSscCR9Ufj_coxatFmCa06Hq4drVdt3qmfuiQji7PTOR4JxJmmxIrJcPhVOmrssw4Vyd45-GNNOq6h1v3lJ_G7Td2mCmnlD0WkFMo2ccfKirHiGCHbdsjO3KCtNsP2svBij0yZfXNmBW4jcRhgQJP5JLmI9VQh6doVEvNWEvH_UBKmOr_fmDYTsFeEKK-aoITORK3JwKyFNIpbna_C3Y9TUCc3tM5bRHRoTMs_ztvp8AQUerGaizfFHeXmv8ZhltUTqmnbCKjkEXeGIZT8OAwmR5cgZtRUoU2ZL4m7jJ7GMmCb6g6DAH78P4Nk2cCZDiSDNgSkXkNSm25GJRxaamFQAUWfBo06TOYyLfHtx_gulXUsDXhYvHbKXzhUfiLkKmnVhbtObvL3clmsmGnxYarghS2V08UzfJeqI7VXeb-NKZm1qW4LhUtE5OEuIeIoUbemtZgrS8uElDsTy55ghTRpFwwGdgX5p0smHU8NYKvs2gcy8wF6AR6uG33UmdWKK7gkedhTNv-NSStbLb_p3QnJoGGZdf5a-gijjkujxyqT8DHEvoJ3RiQ41RVxVCheRSlugZXqlFiO0stEOq7jMMUZ0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبتهای زیبای ریچارد نیکسون در مورد شاه و اتفاقات آن روز.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/19792" target="_blank">📅 10:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19791">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f90eed59a.mp4?token=Eyk09zfifDhN3auzk4ss0LYsfS4nNv5ER8uzRVSd6QdH3VAyq4v9IiUEZbsIJQd4Z0FAw1YPFo7CkH5tmm8lQs_JFv8IOPbKLVmhasVL9NJmRejSuButAeDczEKWUD-zBKvVgvw8MBFdSxBQSqrno5N-ye6ErperQHrkfGXuNgv-JwEV1N_Ork9NTQOMyUKycqWn1SxomKdvL5IAiCEXsoa4EKyuN9Z1iLtzRA6hyvUBhiP9VCHyJf6oIOD56Ld2WNo0zVjGyCwXPJnUP4PD5guUdccziCHJVfYP1-zOb8aGQj1zzmfNA6zFvAmU7nyb9Lq23-EbNUjr23lpvk7d8ZUvCCzittQthSFD9HLtvoRpBsUrfOomFa23r6AqwvKNIUN6CDXvI4Ul3yeWuuewOsCjvvtXJtMq_UbiAY-KaIHCCwPwb74uS9bBRzETpltM-0HsLLkIMRlExLRXrWrwjKo_p7wZDfAubF1VAdEjwyVy7Y9YCge3l5SSi_GDdxOntLgCMZKQJl6_hRlhOfe0_QILWPPYLxqysGCRFfmALfuMEh0HIAOLn8s4SDzNxED5qKkJSQoz8hXYHhJTjt4CYE_QVjbMxlDfKsvN78803HE-H4tvXJGqzKoOOw9OEd5aeDAUpoaAdtZ3AI_TAWAAu3a84YUPff8YN8ys1tJjU9E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f90eed59a.mp4?token=Eyk09zfifDhN3auzk4ss0LYsfS4nNv5ER8uzRVSd6QdH3VAyq4v9IiUEZbsIJQd4Z0FAw1YPFo7CkH5tmm8lQs_JFv8IOPbKLVmhasVL9NJmRejSuButAeDczEKWUD-zBKvVgvw8MBFdSxBQSqrno5N-ye6ErperQHrkfGXuNgv-JwEV1N_Ork9NTQOMyUKycqWn1SxomKdvL5IAiCEXsoa4EKyuN9Z1iLtzRA6hyvUBhiP9VCHyJf6oIOD56Ld2WNo0zVjGyCwXPJnUP4PD5guUdccziCHJVfYP1-zOb8aGQj1zzmfNA6zFvAmU7nyb9Lq23-EbNUjr23lpvk7d8ZUvCCzittQthSFD9HLtvoRpBsUrfOomFa23r6AqwvKNIUN6CDXvI4Ul3yeWuuewOsCjvvtXJtMq_UbiAY-KaIHCCwPwb74uS9bBRzETpltM-0HsLLkIMRlExLRXrWrwjKo_p7wZDfAubF1VAdEjwyVy7Y9YCge3l5SSi_GDdxOntLgCMZKQJl6_hRlhOfe0_QILWPPYLxqysGCRFfmALfuMEh0HIAOLn8s4SDzNxED5qKkJSQoz8hXYHhJTjt4CYE_QVjbMxlDfKsvN78803HE-H4tvXJGqzKoOOw9OEd5aeDAUpoaAdtZ3AI_TAWAAu3a84YUPff8YN8ys1tJjU9E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو دیده نشده از مراسم محمدرضا شاه
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/19791" target="_blank">📅 10:38 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19790">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‏ساعت ۲۵ ایران ‏ساعت ۹:۱۷ صبح روزِ ۵ مرداد سال ۱۳۵۹ بود كه اين خبر به دنيا مخابره شد: «پادشاه ايران درگذشت.» ‏انورسادات با لباس نظامى آمد،  ‏مستقيم به اتاق شاه رفت. ‏دستش را روى قلب شاه گذاشت،  ‏به انگليسی گفت: ‏«تو ساعت ٩:١٧ دقيقه مردى، ايران در ساعت ۲۵»…</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/19790" target="_blank">📅 10:16 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19789">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">صداوسیما: در ساعات اولیه بامداد امروز، ۶ فروند کشتی متخلف با خاموش نمودن موقعیت‌یاب خود قصد عبور از مسیر جنوب تنگه هرمز را داشتند که یکی از آنها دچار حادثه شده و بقیه تحت مدیریت ایران به خلیج فارس برگردانده شدند
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/19789" target="_blank">📅 10:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19788">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">خبرنگار الجزیره: نیروهاى ارتش اسرائیل، به همراه بولدوزرهاى نظامی، وارد شهر عرابه، واقع در نزدیکی جنین، در کرانه باختری شدند
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/19788" target="_blank">📅 09:52 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19787">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">پنتاگن : از زمان شروع درگیری‌ها در ۹ اسفند، ۱۸ نظامی ایالات متحده کشته و ۶۲۴ تن زخمی شده‌اند
سی‌ان‌ان ‌: بر اساس اعلام پنتاگون، بیش از ۱۴۰ نظامی آمریکایی جدید به مجروحان جنگ علیه ایران، اضافه شدند
نام چهار سرباز آمریکایی کشته‌ شده در حملات ایران که از پایگاه داده‌های پنتاگون حذف شده بود نیز بازگردانده شد
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/19787" target="_blank">📅 09:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19786">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">‏
ساعت ۲۵ ایران
‏ساعت ۹:۱۷ صبح روزِ ۵ مرداد سال ۱۳۵۹ بود كه اين خبر به دنيا مخابره شد: «پادشاه ايران درگذشت.»
‏انورسادات با لباس نظامى آمد،
‏مستقيم به اتاق شاه رفت.
‏دستش را روى قلب شاه گذاشت،
‏به انگليسی گفت:
‏«تو ساعت ٩:١٧ دقيقه مردى، ايران در ساعت ۲۵»
اما ‏آن روز كسی نفهميد معنی ساعت ۲۵ چيست؟
‏او در يک مصاحبه با خبرنگاران خارجى و داخلى ‏گفت: جهان عزادار شد.
‏امروز مردى از ميان ما رفت كه خواهان صلح بود، ‏بعد از او خاورميانه رنگ آرامش و آسايش به خود نخواهد ديد.
‏او فقط پادشاه ايران نبود.
‏پدرِ بزرگى براى منطقه خاورميانه بود و ‏روزهاى سختی را پشت سر گذاشت،
‏او براى دفاع از كشورش در مقابل دنيا ايستاد ، ‏او امروز صبح مُرد اما ايران در ساعت ۲۵ از حركت ايستاد.
‏اين خبر به ايران رسيد، روزنامه كيهان و اطلاعات با خط درشت نوشتند: «شاه مُرد.»‏
‏فرانسوى‌ها ضرب‌المثلى دارند كه حركت روز و شب ۲۴ ساعت است و ساعت ۲۵، ‏ساعت مرگ است.
‏به واقع ساعتِ مرگ محمد رضا شاه پهلوی ساعت ۲۵ ایران بود.
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/19786" target="_blank">📅 09:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19785">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">گزارش صدای انفجار‌بندر عباس ، ممکنه خنثی سازی باشه
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/19785" target="_blank">📅 09:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19784">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">https://t.me/boost/withyashar</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/19784" target="_blank">📅 02:41 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19783">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">پیغام های زیاد گزارش انفجار در‌ اهواز
🚨
🚨
🚨
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/19783" target="_blank">📅 02:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19782">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab6daf7646.mp4?token=WLW1LzjNYmUxkoT-19L3aQgxPjA9xe1wxL-9n5o-WtN0DlW-CKKlwZTQrCbSq9gRUfh2sJxKNy9c79BF1YVCsGQEny4w4peI2hwqwzwopRszDyuOX1fS_jDYe6_zE78nDhhzEbnVTZVHF0mt_QA7PNRNTOosSAz2YoFeknfwa2lzBvSMmodfwzX-hw-zRNi8LvPmyaIO1-Njqfuc7RUsFp6YIFgV1tU559fx2HaJ31H75fIGv7AzTSTYRzaDdPD3WnEl8QrIFHGTLmwl0C44lUXTzFWFhmfC6c-26xWSYetZG40Hh9V_C7_n24DiltUNR7AIQ0chV9R6mMAb_2coiqhP-pdFjIon1a5517AHwTIrlFkZ3Jc_zwImvCZO8EKin2fI_6DFrFzYkuD37ZAsW-JwVO3oWC5UADO6sbXO70XrWdez1zAtREr1XkNRkuAWsC8j-BTI0DBIdn1_OtydKMc9oFDb2Z1Rq0kC_AFnLhpifG9_iQRTvweohtpDL5M4x1k5Dj3-gXrQlhxP6Cb8t3OWOqdU92Q4OID9ouMI0O9uN2fzgtyTWHbIdYS3UE2H-cAGJsI1MpxyE_K3J_bpqyCPPKRmvppkEUrTcWw1z_dhDq2e7APnd0B_R9vEo4_vO7pYSWyw4poj1_BJ-32c4wbzOGlK9aKxNHjmPvVijY0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab6daf7646.mp4?token=WLW1LzjNYmUxkoT-19L3aQgxPjA9xe1wxL-9n5o-WtN0DlW-CKKlwZTQrCbSq9gRUfh2sJxKNy9c79BF1YVCsGQEny4w4peI2hwqwzwopRszDyuOX1fS_jDYe6_zE78nDhhzEbnVTZVHF0mt_QA7PNRNTOosSAz2YoFeknfwa2lzBvSMmodfwzX-hw-zRNi8LvPmyaIO1-Njqfuc7RUsFp6YIFgV1tU559fx2HaJ31H75fIGv7AzTSTYRzaDdPD3WnEl8QrIFHGTLmwl0C44lUXTzFWFhmfC6c-26xWSYetZG40Hh9V_C7_n24DiltUNR7AIQ0chV9R6mMAb_2coiqhP-pdFjIon1a5517AHwTIrlFkZ3Jc_zwImvCZO8EKin2fI_6DFrFzYkuD37ZAsW-JwVO3oWC5UADO6sbXO70XrWdez1zAtREr1XkNRkuAWsC8j-BTI0DBIdn1_OtydKMc9oFDb2Z1Rq0kC_AFnLhpifG9_iQRTvweohtpDL5M4x1k5Dj3-gXrQlhxP6Cb8t3OWOqdU92Q4OID9ouMI0O9uN2fzgtyTWHbIdYS3UE2H-cAGJsI1MpxyE_K3J_bpqyCPPKRmvppkEUrTcWw1z_dhDq2e7APnd0B_R9vEo4_vO7pYSWyw4poj1_BJ-32c4wbzOGlK9aKxNHjmPvVijY0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رویترز : در ۲۹ دسامبر ۲۰۲۵، خودروی آنتونی جاشوا در نیجریه با یک کامیون تصادف کرد. در این سانحه، سینا غمی، مربی آمادگی جسمانی و دوست نزدیک او، جان باخت. جاشوا پس از ۲۰۸ روز دوری از رینگ، با آهنگ «نقاب» از سیاوش قمیشی به یاد دوست از دست‌رفته‌اش بازگشت و در یک کامبک احساسی دوباره وارد رینگ شد.
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/19782" target="_blank">📅 01:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19781">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LXmvxI0ZJ8t_au-Sd7JAhZpAw1x-D2t6Fd5-GSHvKzQmF73ScU35DFDcKi7JCxNbEq6knhw2f3ESG_tnDthoGMMJrEcBY1KK7Y45pTlRGipqVdnv9erhplMnsxVfA9fs_lD25K8Be7Vo6Twm9qx5LZQ0zYTCg6tWfvKoFYNs1K_RReEmNLO8vNJMluFzVUxWp4cfCEzrcr-0DlqDrMolQ30JIywJr7MYcMoN-4UlTwIbccLK66vSESDT1tFAQpIaeho97Tt3rC6Rr6jVvTNPIq-G79GPe6IMpxLZHKTOgc6Foh_4MTIykIu4-YpoequrjeE0UFnrqUcegeVcnii21A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افشاگری یک سایت خبری روسی مبنی بر کنترل مافیای لوازم آرایشی توسط حسن روحانی
رسانه‌های روسی در چند ساعت گذشته با انتشار خبری جنجالی از یکی از بزرگ‌ترین پرونده های قاچاق سازمان‌یافته آرایشی-بهداشتی در غرب آسیا پرده برداشتند.  طبق ادعای این سایت، حلقه اصلی این مافیا حسن روحانی؛ دیپلمات‌ سفارت فرانسه و فردی به نام مهدی‌زاده بوده‌ است.   طبق گفته این سایت اخیرا و در طول جنگ ایران و آمریکا دو کشتی محصولات قاچاق آرایشی تولید کره جنوبی، متعلق به وی توسط دستگاه های امنیتی ایران کشف شده است. این در حالی است که چند کشتی تجاری نیز در سال گذشته توسط دستگاه های امنیتی جمهوری اسلامی کشف شده که با دخالت سفارت کره جنوبی و پیگیری وزیرخارجه کره، این موضوع رها شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/19781" target="_blank">📅 01:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19780">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">رسانه های نظامی اوکراینی ادعا کردند: در صورت پاسخ نظامی ایران به اوکراین،ارتش اوکراین حملات پهپادی دور برد به شهر های ایران انجام خواهد داد.
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/19780" target="_blank">📅 01:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19779">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/19779" target="_blank">📅 00:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19778">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">جولانی: حزب‌الله به مدت 14 سال، رژیم سرکوبگر سابق را در جنگ وحشیانه‌اش علیه مردم سوریه همراهی کرد و باعث آوارگی و کشته شدن تعداد زیادی از افراد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/19778" target="_blank">📅 00:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19777">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">پوتین : شرق اوکراین برای ماست و غرب آن برای لهستان، مجارستان و رومانی است و به زودی به آن ها برگردانده خواهد شد
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19777" target="_blank">📅 00:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19776">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">فاکس نیوز:حمله گسترده به ایران هر لحظه ممکن است رخ دهد
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19776" target="_blank">📅 00:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19775">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7Gp3WJitAib3tS3GvtJkLvgwafHLCFJPVWbhaBWbGGE5oaTMSjv8KFmtO37obqIUoKwiykDakaYUBEuHoqNqnWpEF9qwKm5SKmf3HTp80gZ7PnyetB28AHrwP5_WknAxCRWtDRrF1F1Lg1a6UHn6h5k6OyL6Qkj2NduKuYekeqpoBjknWQiaslVQlXI8EaQ23GceXqnLhyfrrskEtRwdDRI43Mvomf3PEg8MbmdnJSp0LS_nkuic0EJWBjdhaHhy_d7yjIrCDTMc8AqqmnYKlusaygWf5zG3RbzsZYpKYIe-VyxqDu22d-pcEw20speVcuNedMbGxSSzMH-xH8uXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : نگهبان جهان
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/19775" target="_blank">📅 00:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19774">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TjFetXFiMva1Glbf6tN_2vsiJf10aSqg_0pdB05kuAq6OqXtOtnM72JmFXxEnZX7E5mmmgZt_QFsdIve5AwO1Q-92ivSPJhRiglNNuhwsHw2qhlFRAlReHS0NpZn9a-ajqtj_dEXz5xlgJWScA3z1LhYrIToqcu0OAMd2V8eGqxkM3UsLzeJeDtlxUp7SviLFDG2gsDjO2xm4yuPxR52c4Z_0IXH_v8NIGB_zLDrMWsZC0xqeI20AQGo1qZsqL2SPAd14GbI-Jnwd2W26QYIUAApLd4mcjqPkpryQNHedIBCYhV8j9WHKnF5EBuBSzTgdwQJqgbP5bprvfylwgfGIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : خداحافظ موتورخانه
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/19774" target="_blank">📅 00:28 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19773">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fUhJMgY3cvAdEH2tYtv9QwT-xal1ESnhA2Bf24jSXBFBXUkBzBZB0_bx9JuDUznjI_iRbfabPgUQe5I9DBPZHah21CYHQYIKliLnBcmpB9jjClRLhxpLQHUMYpt6kxbOoRUKXpIDkr2ejUo-vUZxtQHbxadPp_KwicDFVnjZ0MOvUyNAppVZS6drE0KEiHBvYMaEMtnHNMxUukHECbsTlVwPc2hLhviad1HbcHcVpwfbT2z_1EQrS280zTql5YxWRoHCVXcvcHRKPAKJUhWxUFZsCZ8VAEfUF_5gtQ4ZFEKG8i2v1s9xFcjfRfFzdNy1jEm81PBO2pygscCxDqQBrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : فرشتگان نگهبان جهان
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/19773" target="_blank">📅 00:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19772">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9e1f8494c.mp4?token=fplC2v2gjhbS4Aob_OSDyluRHkpMEZBhZDgzXHz9JQobIRmJaZUyoLl8voOX_-McsaNFqqRzArZLoByiMQRu3POizua_NMhcwdCAqGCZKHgFN_VMSuwEGuO2wHv5ZF6_0FkF6GRNUM1e6-HRisepbBzB3EeGBI4M2UnqP1WIznP25z5jlLSzW1VPjCppm5nK2lswA_qh8459jUfnGncL3O-2FdwJIROB09HMXqCM69VAhjAj0lCsOaoxZKRowhQnI2cPwyoKCYytfg8XP3VNLrA6ZdAIBQmeTJkQaRi1UjkoqLlSrQIfW4777dXD3X0IE8AB7JhzuHSe1kR9mJ9WJC92an_IADkEv4SPNCpcIvsf8demEii97mm2BEmX7Nd50pBrK3oB1N4Ug-JHx27wgIlV-P81WxkPevJkI24zcv4lBlLiYdqJJy1GXEgTfvzrKEfBixB_GSjg7tMEWHdMpRvYP0fXghrHs8LliUIT4jQMS-EGH4cTRo64EKTQ0UlmKofCaCfTbYOB58o2lqBlrcMntkw0GVsPYGIIchMlZrxiqfWB5qusKmjqTt94cAIsq4Y4t5F6HPsE9g4im2EfGw8XB8wszPaMfeMjZXOXh46zoZFW1rQcAVFknwtaJEgdjacmle-9AKUBqXxC6_U3EInfZCrzXH4u7VYIgvxaJBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9e1f8494c.mp4?token=fplC2v2gjhbS4Aob_OSDyluRHkpMEZBhZDgzXHz9JQobIRmJaZUyoLl8voOX_-McsaNFqqRzArZLoByiMQRu3POizua_NMhcwdCAqGCZKHgFN_VMSuwEGuO2wHv5ZF6_0FkF6GRNUM1e6-HRisepbBzB3EeGBI4M2UnqP1WIznP25z5jlLSzW1VPjCppm5nK2lswA_qh8459jUfnGncL3O-2FdwJIROB09HMXqCM69VAhjAj0lCsOaoxZKRowhQnI2cPwyoKCYytfg8XP3VNLrA6ZdAIBQmeTJkQaRi1UjkoqLlSrQIfW4777dXD3X0IE8AB7JhzuHSe1kR9mJ9WJC92an_IADkEv4SPNCpcIvsf8demEii97mm2BEmX7Nd50pBrK3oB1N4Ug-JHx27wgIlV-P81WxkPevJkI24zcv4lBlLiYdqJJy1GXEgTfvzrKEfBixB_GSjg7tMEWHdMpRvYP0fXghrHs8LliUIT4jQMS-EGH4cTRo64EKTQ0UlmKofCaCfTbYOB58o2lqBlrcMntkw0GVsPYGIIchMlZrxiqfWB5qusKmjqTt94cAIsq4Y4t5F6HPsE9g4im2EfGw8XB8wszPaMfeMjZXOXh46zoZFW1rQcAVFknwtaJEgdjacmle-9AKUBqXxC6_U3EInfZCrzXH4u7VYIgvxaJBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در بخش دیگری از‌مستند او قصد داشته در اوایل ماه مارس به فلوریدا سفر کند تا از دونالد ترامپ، رئیس جمهور آمریکا، بخواهد در بمباران حزب الله لبنان به اسرائیل بپیوندد.با این حال، بنیامین نتانیاهو، نخست وزیر اسرائیل، قبل از این سفر، توصیه کرد که درگیری گسترش نیابد و گفت که اسرائیل باید بر ایران متمرکز بماند و هشدار داد که حمله به حزب الله می‌تواند باعث یک جنگ منطقه‌ای گسترده‌تر شود.
نتانیاهو در این تماس تلفنی به گراهام گفت: «ما در حال حاضر بر ایران تمرکز داریم.» گراهام موافقت کرد و پاسخ داد: «این واقعاً توصیه خوبی است.»
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/19772" target="_blank">📅 23:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19771">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1de7526ff5.mp4?token=c8qyYtw5LKyX8Z0hVwoE4w7fFaO-4zmrO-xcu060EGiWusGTjW1ELOof3Lqvr_aMbKpirooDbhXSf07VhLk3jMdHKybbAsmIG9C6X3soRsiuaG6zr7gPUsGd59SRISd4vduTMfyoql8WyIQE6UeCsbWS4zveFa9Ks18-mlzV4XBUbQCTYnQYpxea7k9UIsAGtzZInwbcDZ-zQqG0CTEZzvBzz9Jje2P_KlNqaK3Ikwko4s5nBIumOe64tsSvcYiGI0CBdfI5s-hfu1PzE_aZBYsd5ZXkvEzsQ7QQ4DuHR0i7q23B9r6XYcX9DZqIoE1-dCejNo2Qhx6fYhfn1pMQmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1de7526ff5.mp4?token=c8qyYtw5LKyX8Z0hVwoE4w7fFaO-4zmrO-xcu060EGiWusGTjW1ELOof3Lqvr_aMbKpirooDbhXSf07VhLk3jMdHKybbAsmIG9C6X3soRsiuaG6zr7gPUsGd59SRISd4vduTMfyoql8WyIQE6UeCsbWS4zveFa9Ks18-mlzV4XBUbQCTYnQYpxea7k9UIsAGtzZInwbcDZ-zQqG0CTEZzvBzz9Jje2P_KlNqaK3Ikwko4s5nBIumOe64tsSvcYiGI0CBdfI5s-hfu1PzE_aZBYsd5ZXkvEzsQ7QQ4DuHR0i7q23B9r6XYcX9DZqIoE1-dCejNo2Qhx6fYhfn1pMQmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر مستند منتشر نشده نشان می‌دهد که سناتور فقید لیندسی گراهام در اوایل ماه مارس پیش‌بینی کرده بود که دولت ایران ظرف «سه تا چهار هفته» کنترل شهرها را از دست خواهد داد و مشارکت بیشتر اعراب «حرکتی تقریباً برگشت‌ناپذیر» ایجاد خواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/19771" target="_blank">📅 23:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19770">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">وال استریت ژورنال
: ارتش آمریکا یک طرح نظامی تمام عیار برای مدت 2 هفته جنگ همه جانبه با ایران آماده کرده است که هر لحظه پس از دستور ترامپ آغاز خواهد شد.
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/19770" target="_blank">📅 23:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19769">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">کامنت جدید زیر پست بی بی  : فقط همین کامنت رو لایک کنید و کارهای اداریش رو انجام بدید.
https://www.instagram.com/reel/DbRKUnvs_mq/?comment_id=18097108343207051
ترجمه : بی‌بی، مردم ایران بسیار دلتنگ شما هستند. لطفاً به هر روشی که صلاح می‌دانید، این بار پس از وحیدی، کاری کنید که روحانیون تندرو نیز یکی‌یکی از این دنیا بروند و ریشه کن شوند . هدف قرار دادن زیرساخت‌ها و سربازان وظیفهٔ عادی، که خودشان نیز قربانی این حکومت هستند، فقط رنج و درد مردم ایران را بیشتر می‌کند.
ما شما را بسیار دوست داریم و از همه تلاش‌ها و زحمات شما صمیمانه سپاسگزاریم.
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/19769" target="_blank">📅 23:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19768">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">کامنت جدید زیر پست ترامپ : فقط همین کامنت رو لایک کنید و کارهای اداریش رو انجام بدید.
https://www.instagram.com/reel/DbRJwPPBPaP/?comment_id=18108319289002859
ترجمه : لطفاً به‌جای هدف قرار دادن زیرساخت‌ها، که تخریب آن‌ها تنها موجب رنج و سختی بیشتر مردم عادی می‌شود، و همچنین به‌جای سربازان وظیفه که بسیاری از آن‌ها خود قربانی این شرایط هستند، تمرکز خود را بر سران حکومت، به‌ویژه رهبران مذهبی تندرو، قرار دهید.
از تلاش‌های خستگی‌ناپذیر و شبانه‌روزی شما صمیمانه سپاسگزارم.
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/19768" target="_blank">📅 23:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19767">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tAfYILTtRjbA5tml5OEIrIlXJMHGRrCX7JL6Pl78qBsKonjpuAB7fLkM23spBApD3LzwTYpTW6_iw82u3vKtM-gCa58Bn153xQCfYYUO9LminHreFLqR31B__chlkDh2kWxCrbVlNvMIcA2kdkyDnCAKnrCAvHsGlpLPoVAskq1X1m_8N9pdZ_uPvMpDEJC615ef1OwMo1wHx7eVgQMMBfkwClHaWRwLqWbRvoBDh7dQizx__0IEsmM8MuzOOTsulbpekMbkB6XdtuZ2qHNLOec6SgB0Bh21JuDqfbLas6HhgxdSAFaBRYVSDBJcdYpLEqGDyKM50Mti-PP9J-iqZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : الان دیگه نفتکش ماست.
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/19767" target="_blank">📅 23:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19766">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QIwIOOnjp-kCx4RuI6XSX-A8GEjvWyG2BtpLc0khECTGF1qQBEUARmZr4f1BoR7aaMKXoNa7jEPDMy5MV_0xmPvXqf7rxSiknmlNpDpsyvO3mKAC6PUuEBUjQolxlm3FbORyCceNH6AuTPirOb9jLPK2EkUUV7eVAnA12j1GeS4a-uQntn8Ntav5ttzK2vEmlHDkCZKWNZ_0kt2Gtz_wAK-6aVbvijxm-_JjeHTBd2OSocqkcDwkqC1qoV6fP4TLBKE_BFHB69_xLUrgQKneEgY2HTnPnu9IIKp7lgAlCVasZBV-Xi-i1Yt4Pb011mns_NqWr9I3akIuioDzCs7Z3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : حمله هوایی به جزیره خارک
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/19766" target="_blank">📅 23:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19765">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ced9d7006c.mp4?token=u_RVRahRaMRRpX2-iego4VXHX8j5WOqMKPKkj18qxn3Nmvpq0QedE5nsN70njlT-Ucy4tiQFH70G06druev7str5D7ciBMcEH2W5fFN7n_nWv0FvJ0zjVEworRF_IoX1r-gIja1BxAZRpQBJguhES6jAbR3KAy_BS17vWyWo6MNNAmnvahIJ2cm_RH8Sh3mUkbZAEU-EwpD_vOEI_y4h1mRyIJeEwMgkclUeWgwjCEn-KewLGJ1UHqIiaotkS6lf0LrHHrnWJzdtgzTdA09GaXMXfpC2mhVoCCpv6mceonmtWgjjhKi3PxzyYL3-xmO5BB34bPnxOwQlzxr6ZUvgKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ced9d7006c.mp4?token=u_RVRahRaMRRpX2-iego4VXHX8j5WOqMKPKkj18qxn3Nmvpq0QedE5nsN70njlT-Ucy4tiQFH70G06druev7str5D7ciBMcEH2W5fFN7n_nWv0FvJ0zjVEworRF_IoX1r-gIja1BxAZRpQBJguhES6jAbR3KAy_BS17vWyWo6MNNAmnvahIJ2cm_RH8Sh3mUkbZAEU-EwpD_vOEI_y4h1mRyIJeEwMgkclUeWgwjCEn-KewLGJ1UHqIiaotkS6lf0LrHHrnWJzdtgzTdA09GaXMXfpC2mhVoCCpv6mceonmtWgjjhKi3PxzyYL3-xmO5BB34bPnxOwQlzxr6ZUvgKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏واکنش من به تحلیل‌های احساسی مردم:
💥
«ترامپ از رژیم ترسیده.»
‏
💥
«ترامپ با رژیم ساخته.»
‏
💥
«مهماتشون تموم شده.»
‏
💥
«ترامپ ارباب نتانیاهوعه.»
‏
💥
«همه‌چی از قبل هماهنگ شده بود.»
‏
💥
«اینم یه جنگ نمایشی بود.»
‏
💥
«فلانی با یه مقام امنیتی در ارتباطه.»
‏
💥
«چین آخرش همه رو غافلگیر می‌کنه.»….
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/19765" target="_blank">📅 23:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19764">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07f4990448.mp4?token=lH32zCqnEzDmtgbR3009kVRLEspNefag0nZRvv-U3Tj2LrDuBshJv2Oh8fTsccIraPKPRKQwlzkkL76Co2cSUzFMICr0BITY53NiZFzfyrL_OnffITpfZt_6ZK-APvN6eW1EIg1CjXjvHIwXWVcCj1p9khCKsWrnxQBA4bHoBF4us1kZe6ttd6-Qy7RWAYCMDY3UMm9Znw92b9dia-IBQMQRY-Dg1PUTvltQ0ho359NE4W0oufGq0QsQYFbLeVCXkwH9lHtbLiDxvgAKqAvuiectqowoL1XOa2x4lTzkx90AYHB1p8SzOMh649Tto7ikbDAbKfarBqmP2XnwBHM9sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07f4990448.mp4?token=lH32zCqnEzDmtgbR3009kVRLEspNefag0nZRvv-U3Tj2LrDuBshJv2Oh8fTsccIraPKPRKQwlzkkL76Co2cSUzFMICr0BITY53NiZFzfyrL_OnffITpfZt_6ZK-APvN6eW1EIg1CjXjvHIwXWVcCj1p9khCKsWrnxQBA4bHoBF4us1kZe6ttd6-Qy7RWAYCMDY3UMm9Znw92b9dia-IBQMQRY-Dg1PUTvltQ0ho359NE4W0oufGq0QsQYFbLeVCXkwH9lHtbLiDxvgAKqAvuiectqowoL1XOa2x4lTzkx90AYHB1p8SzOMh649Tto7ikbDAbKfarBqmP2XnwBHM9sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار: آقای رئیس جمهور، امشب کجا را بزنیم؟
ترامپ:
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/19764" target="_blank">📅 22:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19763">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQjEsnT8UBpmkSNrq8WGFr9lqBNHuLkKcgTGo-sRhUzhoi1Zh4iFlZib1epj2fldMw3f_QojcOaR6zqJdjuSFhOoO0gknqWCFZh8rc2Y58eA3w4xZ1GiQOEQhmWhVPIQabM7yLLCijtjrL8vPCegqW-K1tH2zOj-QP6sRSv15EtMFD1hLtl7byYkjXonohWhBeswUmyIaZomDvBOtlSEj1389fGQzSsXpJmf6Jb9cP6h9lzXG8sHn4jSQWcBTxRAeldl-cIDEr3he7raU-l75YE-RGKZcvbEMJRDmGysY3la59EaQw9IPRM9-W-Bh5x96NRT1jAeef6qli10pkWZhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه آگاه : اوکراین را ادب میکنیم
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/19763" target="_blank">📅 22:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19761">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uvHX9_oUBQExOrFkTHqXqv1-EqY1FMMn8yDHUS4OR11jBLw5RrqKLbg8IcW28RMGXMDgcZPgqFGAJvl5DLm-716l2s900CLVzMdeT9BhB340exvIKz2qxdfbSa-dAe4CsfPeVx5huA8zdHowmiICrTNTif8rc7e5Bj5r-2LPoLsgRzge3Dj0Mmajgp2OWxN0q-N3wi0DBuxwCGynr4m-cV3suLD2m_fFlR6N7hlGbvnHy46LoTYlg3PSPhBuc80_S0tVIE_GVi5D-soixHqf-lr_9N_kIzw8hkJXNTElDb3Fe3pmmWlj6s6CD0RF8CkAuM89V7ZhdCu8XQi0gRjqkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فضای به شدت شلوغ و عرفانی حاکم بر منطقه و یک دسته حوری جدید که از اسرائیل به سمت خلیج فارس میآیند.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/19761" target="_blank">📅 22:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19760">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">عراقچی: تو عراق به من میگن عباس قهرمان
@WarRoom
🤡</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/19760" target="_blank">📅 21:45 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19759">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">مجتبی خامنه ای: ایران حفظ تمامیّت ارضی لبنان و رفع کامل و بدون قید و شرط تجاوز اسرائیل را به‌عنوان شرط اوّل تفاهم‌نامه‌ی پایان جنگ تحمیلی با امریکا قرار داده
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/19759" target="_blank">📅 20:56 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19758">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">اکسیوس : ژنرال برد کوپر فرمانده سنتکام، پیشنهاد داد که عملیات بمباران در اطراف تنگه هرمز متوقف شود، با این استدلال که این عملیات به حداکثر کارایی خود رسیده و بیشتر اهداف تکراری شده است
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/19758" target="_blank">📅 20:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19757">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">سی‌بی‌اس
:
بسیاری از آمریکایی ها احساس می کنند که جنگ با ایران به خوبی پیش میره
این احساسات به طول جنگ، ارتباط در مورد آن و تأثیر آن بر اقتصاد مربوط میشه
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/19757" target="_blank">📅 20:09 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19756">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">العربیه:ایران با تمام پیشنهادات عمان برای ایجاد گذرگاه جدید در تنگه هرمز مخالفت کرده است،
هیئت دیپلماتیک عمانی پس از مخالفت های ایران، تهران را ترک کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/19756" target="_blank">📅 20:07 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19755">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">گزارش CNN: عمان پیشنهاد ایجاد یک ائتلاف منطقه‌ای برای ارائه خدمات در تنگه هرمز را داده است، مشابه مدلی که در تنگه مالاکا استفاده می‌شود.
پیشنهاد عمان شامل یک مکانیسم پرداخت داوطلبانه برای خدمات ارائه شده در تنگه هرمز است.
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/19755" target="_blank">📅 20:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19754">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">سی‌بی‌اس:حملات آمریکا به ایران به دلیل سفر مقامات عمانی به تهران در روز جمعه برای انجام مذاکرات، متوقف شد
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/19754" target="_blank">📅 19:30 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19753">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">در ابتکاری خوب برای کاستن حاشیه‌ها، شاهزاده رضا پهلوی تمام فالوینگهای اینستاگرام خود را آنفالو و فقط خانواده و پیجهای رسمی را نگهداشت.
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/19753" target="_blank">📅 19:21 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19752">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">سفیر ایالات متحده در سازمان ملل متحد به شبکه ان‌بی‌سی گفت: مذاکرات با ایران در سطوح مختلف ادامه دارد، با وجود اختلافات موجود در داخل رژیم ایران
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/19752" target="_blank">📅 19:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19751">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b90613bbec.mp4?token=ijlzISW2uSTZ6z7JeAkC2tKIqJYLADmy9alYXIMRyMwFlwQ882W0GOZUzBkOzf07d64a1T8Bw2d7xjoFEK1u1Ccjnn_2_VxvwTAQcF0xoMTjI7_KsClOtlSQv47X5snfeTm40P2we6uvuuc_fXd0FVpFQ8FLxFcEo5OAqPse2APRWoskxF4bIhHTcgGHi__wj4d6PyBi0OQuPJVhHKzGy7_knf8RDnr_53a33RsZ4tCH6XmKTBkb2Nvq3zOB2bF2TIoRu4CiZfd7ihR1kTrYfsNM9OnMPoCFf-brapap0V8vA7XYHSpeVA9bmSuYUKtCvfyNeR6MYWJ9h9dEFPfNtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b90613bbec.mp4?token=ijlzISW2uSTZ6z7JeAkC2tKIqJYLADmy9alYXIMRyMwFlwQ882W0GOZUzBkOzf07d64a1T8Bw2d7xjoFEK1u1Ccjnn_2_VxvwTAQcF0xoMTjI7_KsClOtlSQv47X5snfeTm40P2we6uvuuc_fXd0FVpFQ8FLxFcEo5OAqPse2APRWoskxF4bIhHTcgGHi__wj4d6PyBi0OQuPJVhHKzGy7_knf8RDnr_53a33RsZ4tCH6XmKTBkb2Nvq3zOB2bF2TIoRu4CiZfd7ihR1kTrYfsNM9OnMPoCFf-brapap0V8vA7XYHSpeVA9bmSuYUKtCvfyNeR6MYWJ9h9dEFPfNtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست وزیر اسرائیل:
اگر ایران به اسرائیل حمله کند، چه مستقیم و چه از طریق نیروهای نیابتی، چه با موشک‌های بالستیک یا پهپادها یا هواپیماهای بدون سرنشین قاتل، اشتباه وحشتناکی مرتکب خواهد شد.
زیرا پاسخ ما، پاسخ اسرائیل بسیار بسیار قاطع خواهد بود.
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/19751" target="_blank">📅 18:09 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19750">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">مجری فاکس: در مورد هرگونه اطلاعات جدیدی که ممکن است در مورد برنامه هسته‌ای داشته باشید و قرار است به ترامپ ارائه دهید، چه می‌توانید به ما بگویید؟
نتانیاهو: قرار نیست من اطلاعات جدیدی ارائه دهم؛ فکر می‌کنم خوب است که فرصتی برای نشستن با دوست خوبمان، رئیس جمهور ترامپ، و شنیدن آنچه در ذهن دارد، داشته باشیم، زیرا فکر می‌کنم از بسیاری جهات، این تصمیم اوست.
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/19750" target="_blank">📅 18:07 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19749">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">بنیامین نتانیاهو در گفت‌وگو با فاکس نیوز: برنامه هسته‌ای ایران باید به هر شکل ممکن پایان یابد؛ چه از طریق توافق و چه بدون توافق.
این جنگ زمانی پایان خواهد یافت که یا نظام ایران سقوط کند، یا آن‌قدر تضعیف شود که به این نتیجه برسد که باید برنامه هسته‌ای خود را متوقف کند.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/19749" target="_blank">📅 18:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19748">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">مطابق گزارش رویترز، به نقل از یک مقام ارشد ایرانی، در تهران، میزان تردید و بدبینی نسبت به تصمیم ایالات متحده برای توقف عملیات نظامی، بیشتر از خوش‌بینی است.
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/19748" target="_blank">📅 17:30 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19747">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">وزارت دفاع اسرائیل اعلام کرده سامانه لیزری پرتو آهنین پس از آزمایش‌های گسترده، در مرحله تحویل/ادغام عملیاتی با ارتش قرار گرفته و به‌عنوان لایه مکمل در کنار گنبد آهنین استفاده می‌شود. این سامانه توانسته در آزمایش‌ها راکت، خمپاره و پهپاد را رهگیری کند و هدفش کاهش شدید هزینه دفاع در برابر تهدیدات ارزان‌قیمت است.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/19747" target="_blank">📅 17:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19746">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">کانال ۱۴ اسرائیل:داماد خامنه‌ای سکوت خود را در مورد انزوای مجتبی شکست
رئیس سابق مجلس ایران فاش کرد که مجتبی خامنه‌ای «به دلایل خاصی» تمام تماس‌های خود را قطع کرده و در بحبوحه سوالات مربوط به غیبت طولانی مدت رهبر جدید از انظار عمومی، تنها با احتیاط گفته است «امیدوارم سالم باشد».
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/19746" target="_blank">📅 17:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19745">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">العربیه:  ایران آمادگی خود را به پاکستان برای ادامه مذاکرات در ژنو یا دوحه یا اسلام آباد اعلام کرد
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/19745" target="_blank">📅 17:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19744">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">یک منبع بلندپایه به الحدث:
ایران به مسئولان پاکستانی اعلام کرده است که از مذاکرات خارج نشده، بلکه
«آن را به تعلیق درآورده است»
ایران به پاکستان تأکید کرده است که ادامهٔ مذاکرات بر اساس یادداشت تفاهم ضرورت دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/19744" target="_blank">📅 16:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19743">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">الکساندر دوبریندت، وزیر کشور آلمان، در بیانیه‌ای در محل حمله به رژه همجنسگرایان برلین گفت: «همه چیز نشان می‌دهد که ما با یک حمله تروریستی اسلامی روبرو هستیم.» این وزیر افزود که مهاجم مظنون به استفاده از قمه است.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/19743" target="_blank">📅 16:25 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19742">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">شبکه سی‌بی‌اس نیوز به نقل از منابع: مذاکرات بین سلطنت عمان و ایران درباره بازگشایی تنگه هرمز، پیشرفت‌هایی داشته است.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/19742" target="_blank">📅 16:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19741">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">خبرگزاری الحدث: واشنگتن و تهران، پیشنهاد پاکستان و قطر مبنی بر از سرگیری مذاکرات را رد کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/19741" target="_blank">📅 16:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19740">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">صدا و سیما
:
جمهوری اسلامی بارها هشدار داده است که هرگونه عواقبی که ناشی از انحراف کشتی‌ها از مسیر اعلام‌شده توسط ایران باشد، مسئولیت آن بر عهده‌ی آن کشتی‌ها خواهد بود.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/19740" target="_blank">📅 15:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19739">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">خبرگزاری وابسته به رژیم :
سخن از هدف قرار گرفتن سه فروند کشتی تجاری و نفت‌کش در میان است؛ دو فروند در باب‌المندب و یک فروند در تنگه هرمز. ایران در حال بازی با اعصاب ترامپ است و احتمال دارد قیمت نفت در زمان بازگشایی بازار به ۱۱۰ دلار برسد.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/19739" target="_blank">📅 15:25 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19738">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">یک منبع آگاه وابسته به رژیم : کمی پیش یک نفتکش متخلف در تنگه هرمز که از مسیر مشخص شده توسط جمهوری اسلامی خارج شده بود، بعد از برخورد با مین دریایی منفجر شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/19738" target="_blank">📅 15:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19737">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">تنگه دعوا شد
🚨
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/19737" target="_blank">📅 15:21 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19736">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ادعای منبعی عربی به نقل از مقامات آمریکایی و اسرائیلی: نشست ترامپ و نتانیاهو، زمان عملیات مشترک علیه ایران را تعیین خواهد کرد.
مرحله اول این عملیات، بر تاسیسات هسته‌ای متمرکز نخواهد بود و تا 10 روز ادامه خواهد داشت.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/19736" target="_blank">📅 15:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19735">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">کریم خان دادستان کل دیوان کیفری بین‌المللی ، که حکم بازداشت نتانیاهو، نخست‌وزیر اسرائیل، و گالانت، وزیر دفاع سابق، را صادر کرده بود، پس از اتهامات سوء رفتار جنسی از سوی یکی از کارمندان سابق، توسط کشورهای عضو با رأی قاطع برکنار شد.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/19735" target="_blank">📅 14:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19734">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">سوأل شما : ترامپ رئیس قوه مجریه است، اما همه چیز را نمی‌تواند شخصاً جابه‌جا کند. معاون رئیس‌جمهور یک جایگاه انتخابی در قانون‌اساسی است که برای تغییر ونس ، پای کنگره و مقررات صریح قانون اساسی وسط می‌آید ؛ تنها راه‌های عملی برای رفتن او، استعفا، مرگ، یا در موارد خاص فرآیندهای قانون اساسی و رأی کنگره است
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/19734" target="_blank">📅 14:51 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19733">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">نیکزاد، نایب‌رئیس مجلس :اقدام نابخردانه دولت اوکراین درهدف قراردادن کشتی ما بی‌جواب نمی‌مونه
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/19733" target="_blank">📅 14:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19732">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">سازمان دریایی بریتانیا یک گزارش جدید در جنوب دریای سرخ دریافت کرده است.
گزارش شده که یک نفتکش در نزدیکی خود، برخورد/اصابت موج آب ناشی از یک پرتابه ناشناس را مشاهده کرده است. گزارش‌ها تأیید می‌کنند که کشتی و خدمه در سلامت هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/19732" target="_blank">📅 14:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19731">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">کانال ۱۴ : منابع تأیید شده گزارش می‌دهند که جی دی ونس شایعات و نگرانی‌ها در مورد ذخایر مهمات ایالات متحده را دامن زده است. در صورتی که اگر مشکلی بود وزیر جنگ باید این را عنوان کند
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/19731" target="_blank">📅 14:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19730">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">گرندپری فرمول یک بحرین به کشور مالزی منتقل شد : دلیل جنگ ایران و آمریکا
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/19730" target="_blank">📅 14:21 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19729">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">شورای اتحادیه اروپا پنج قاضی دادگاه‌های انقلاب و یک هکر ایرانی را که می‌گوید در «نقض جدی حقوق بشر» دست داشته‌‌اند در فهرست تحریم‌های خود قرار داد.
«مصطفی نریمانی»، رییس شعبه سوم دادگاه انقلاب کرج؛ «ابوالفضل عامری شهرابی»، قاضی شعبه ۱۱۹۱دادگاه تجدیدنظر کیفری تهران و معاون پیشین دادستان اراک، «مهدی راسخی»، قاضی شعبه سوم دادگاه انقلاب رشت، «محمدرضا عموزاد»، رییس شعبه ۲۸ دادگاه انقلاب تهران و قاضی مشاور شعبه ۱۵، «محمدرضا توکلی»، رییس شعبه اول دادگاه انقلاب اصفهان پنج نامی هستند که به‌دلیل محاکمه اقلیت‌های مذهبی و مخالفان سیاسی توسط شورای اتحادیه اروپا در فهرست تحریم‌ها قرار گرفته‌اند.
اتحادیه اروپا همچنین «نیما صالحی» را به دلیل همکاری گروه هکری «آشیانه» با پلیس فتا و سپاه پاسداران و نقش این گروه در حملات سایبری علیه مخالفان داخلی و نهادهای خارجی و کمک به سرکوب جریان آزاد اطلاعات، تحریم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/19729" target="_blank">📅 14:16 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19728">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">العربیه: منابع آگاه گزارش دادند که واشنگتن و تهران پاسخ‌های خود را به پیشنهاد پاکستان و قطر برای از سرگیری مذاکرات ارائه کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/19728" target="_blank">📅 14:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19727">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from❤🦁💚</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hG76RQrxGgayISfBQCHbCk-E-qiZzebkJvGbw04XfDR2RV1MUfa4F4nZr8Gcj7U8Zl6jGRbQPNrJ0tLLKlqd9xcEPvB8BKDu5U5PPPmOuPo6NEVLZh622Z3Xv8U5gejNedH2Ws1Wanwabfgw_SgngIYzcK5iYht4GzD_WY8kqln-JuS7QunecybjdQh_ZIvC5de1jPPcWbTs9UukamhyvdOHxQyJmhnCSSxv-1YI8zHHaidUkZgii_O9hlsqO5gj3wnILiVxWFNnVqwQkDcdTyZrgsk0hBtSkWytOcxVGBsjojgei5k0siQA-GKpyZM46zVRw4S_kAXwJNMCT1DWnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یاشار داداش دیشب سنگ قبر رفیقم طاها نادری رو جاوید نام شهرضا رو شکستن حروم زاده ها دارن سنگ قبر جاوید نام ها رو تو این شهر میشکنن حروم لقمه ها از قبر هم هراس دارن ولی روز انتقام نزدیگه</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/19727" target="_blank">📅 14:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19726">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">کاخ سفید: در مورد ایران هنوز همه گزینه‌ها روی میز است
در پی گزارش رسانه‌های آمریکا که دونالد ترامپ فعلا از تشدید عملیات نظامی علیه ایران منصرف شده است، کاخ سفید تاکید کرد که همچنان «همه گزینه‌ها» در مورد ایران روی میز است.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/19726" target="_blank">📅 14:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19725">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BHQFMJolYmpFWdAikNa6HGwdaI2FcJBqKB-rVgPcHdfqx6vv6Ay0HxKojKz2OJdJaJ9D4HPMDUvhvXM99i39z7YwuMYfEJmgiooUwFeOWmv9yZGmfGV0td_X0EwTjRCG4kAgpH1ugw6ELakA5_prPcm_Qt7jIjAJk-ZgHBQdR1i7ZqgTHyN1F32MOYfVHznJwiKJ73MySwky1plW9vK8F4PzBhPmLHaQSERbm0cruvCbsdSxfYVe-s4dyRWcQPLtKn0SeT2G5qs_-qtRytYVrXv6_S57OYCm7EwVIT6Gk1ubi1AX--my58uUlVDp-xtmyn8Vu6asitSgJuPg7meOIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو:این هفته با ترامپ ملاقات خواهم کرد تا درباره تمام موضوعات، از جمله ایران، گفتگو کنیم. @WarRoom
🚨
🚨
🚨
🚨
یاشار : آلبوم جدید داره میبره رو کنه
😁</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/19725" target="_blank">📅 13:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19724">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">نتانیاهو:این هفته با ترامپ ملاقات خواهم کرد تا درباره تمام موضوعات، از جمله ایران، گفتگو کنیم.
@WarRoom
🚨
🚨
🚨
🚨
یاشار : آلبوم جدید داره میبره رو کنه
😁</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/19724" target="_blank">📅 13:45 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19723">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KemqibaLjvPHislN7x1GSUvfdkXllzAfqpvHn2BdDC8GkcvGDv8xeJ6_xPJFXDYg1uVHx0fV4hMiSmUlFGcHBD3ilP0c2xCMGlTjAol9KUwMDcISatEQk7YLF3-SFX3V1D7bOC6JbY-PT2DyegZdOXvm2zijc1BsT2KBum48v3HEku570WJCMIl0Mm66L6tvQTFvdTfhSdCiq76vwhKyKtH3I2P3JlgLDTXXDgkpB9XG1FsG7KplAnvDoHsU0nLPOU-WIWqdX5GgmLIDfIfDPldFAV5tp9NsqVthy0W33UF38g4seF_M4rqLXJvgMNiopz-COGSSOwVnd2NErHIRkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن شرتی و غول برره که به مرده ها هم  رحم نمی‌کنند و پریدن توی‌ کادر زیر تابوت اکبر عبدی و بلند میگویند الله اکبر.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/19723" target="_blank">📅 13:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19722">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BRuwhsMRkqijp2fFZO6c5N4qWnDs0dIzx6BX8rIMIt6p4xhyaIyaTGaK3AXmrzyiaA2Dl9Syj2HJR5RaRSKimqPA0_F21c_EHAKnuFeafgWQf7lR4rX_BLfB2zA-9hSELrGu2gLlFQVUkhD2PXIWX_gdYzsGM1AUtZbFj-zdyoqeZWwbjujJ1B8aw2DWgeIUGjQpUZZMmqC1CtijK5t4nafkw1U5vTVmZkbEx8-GL6opJ9JyPOy8sJvf8Md3BuMAdabhQHI_jU6083JJwIezFdWiJljYpj_ET_ke5sqySvb_C1bSYRI5W54WtX40GE8AaivjkB46g2zhMNBgTwkC-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان حمل و نقل دریایی بریتانیا (UKMTO) گزارشی از وقوع حادثه‌ای در جنوب دریای سرخ دریافت کرده است. به UKMTO گزارش شده است که یک نفتکش شاهد پرتاب یک پرتابه ناشناخته در نزدیکی کشتی بوده است. گزارش‌ها تأیید می‌کنند که کشتی و خدمه در سلامت هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/19722" target="_blank">📅 13:04 · 04 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
