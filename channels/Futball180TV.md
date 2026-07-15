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
<img src="https://cdn5.telesco.pe/file/Ti1O9aqglQnYjMQoZM_BoWTSryUcqq8TSN88pvfwLLu2wLv3XBC4qBZEsHSbVMbR_t6X-oJx9wg2t7hsPg87y4iHgmcqoNi0gKeJQRLDAdGzHL_1WrVTlrMTWsrnnXmz6XtNjm6eSNYjO0UQ8U2CW1wvzMy0cJtHYpidDiLuvq3oL197Zb-Uc2FBW53nU2Tc3zb3NFslsdKz65ThtoJpwxS0Uk7oKKGktdBXard5v8DOdsxk6Dn8kZOR3bM_ewciWjcwTWimJWjgnUgeFyCsUP7WMproGMjfWX_LffX7MLdOR6vnBxyJ7XCKWLoPbp6FPLS2bxWoCMYDsDdYoyYOVA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 573K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-25 00:57:43</div>
<hr>

<div class="tg-post" id="msg-100415">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hKlJDYYhNDQZL6ZlXgAd_hFw8zqQGM_fDsjldww_TX8DHRUzd8zQLik8JH1Iz3QgZLVRtZjIav8jmPk5kJaqFkS9WUvTBlWblrMEeIwUzETsHQoVkoTWdJ4VXkq-BpDVuLK6yHBRj9tqvD7rKKvQ_NonqeO0NT6aw4T3OCye-NbgQir8niXUt07qqkdQkTb-R4SbWbu1x3sxdQKfVHAtESfCRtv2TdzWUGRMkXpSCJL7Xsnh-4GZ2uSYIB4DN4DmGiT4lWUD324N09x1C4Nln6GyRFMLax9MbO3uwgUqyisRFpw7ig5L2ysTtnc3lxj1GkJxrArwf-mImHzRll7hXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکتیک توخل بعد از اینکه انگلیس گل اولو زد:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15 · <a href="https://t.me/Futball180TV/100415" target="_blank">📅 00:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100414">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/msif32d1FL4z4MmE072ZLKfJAYLzMu6Iax0q_dQ4opkGsJUkVKWevyCMsrmLz8RSfz-J8qkX-8xK6YesUH5ZKfhST7BktMEcxdf9xiqEn3sawiHZGmqKDH0W4rvWxckCQNfc5LGoAF6rlV8Br_YtrqulUyOkokUiVsdlUVWPKwzP8K_gD9ZKI1zY1CQPj7P6RkOWCU9vUfUpJJUfHrQG4R-lvRENk6ne7S1l4RD82EdkwG8xAB-pBx7NO_UfaavWlvA7Ym4l3hJGXw-14917Au4WUGQ6gIeD6xyVtxlbqVujGv-GzQHhNAVFRd8Hu-N6ZDMESR3Tj4voz4edc0XMmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
ویلیام سالیبا مدافع تیم‌ملی فرانسه بدلیل مصدومیت از ناحیه کمر ۴ ماه غایب خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/Futball180TV/100414" target="_blank">📅 00:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100413">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/Futball180TV/100413" target="_blank">📅 00:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100412">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uuGSsuqfNqsGg6B-lRp4mRYHXU6G7bKPRVdUdPDcgfdZ-O_G5O7SCcnmqtSN1e_W-QgGTmfQ4DQxHjkNJpuhoC8QyFfZGXxyImnOe5Ua2TiizL-cYqwQl8uRLm0YryEStRVn06JaM3Wc3dChG4vhHCfoUkEJ4dlH1vJGdZhBMS8R-etoPkin3uCenNa1oiXLWLea1XmrkobeodBNWQmPT60e3bGUgkhflt8l6beFkufC8f8Y6nLWzVGP8P818c9fMXZGv4VIv5wvWJo4rKJpEBCoKrxMZbOd_Y-4Stlds6ekoO8XJ-EA1XTmMjePslhu4vY_7vZZ5WSMXZM3QaRcsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/Futball180TV/100412" target="_blank">📅 00:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100411">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
از الان بگم دوستان رئالی - بایرنی - منچستری - آرسنالی - پاریسی - بازم رئالی - وغیرررره
بازی فینال هیچ ربطی به شما نداره بهتره نبینین و‌خوابتونو حروم نکنین
مرسی از توجه تون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/Futball180TV/100411" target="_blank">📅 00:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100410">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/thivMXX_PytjF0JdFwsO-gKdcFUSwCe90qXP7V3V5kvIhWiLEqv0MCHHSnfZuo5mfn_Am0Fj64Mf0rTfjlj4Z0Zi1f6waug0WN2UiHYTI-MnFGZ1PCiOg_LxoUPclcmRW_rMNr_9VKLFrmGBmp560aS8LxH90G9vgbOqfVdPdFIgYtKquqz02Afufm2pBmNi1tPiNUq9JNjE_wCxIYmC0uY42h9757LK6RSSrurO1KbNNOEJcKZlpDWIYFmA8Snma7TOLuHPDtfEnO9N_rxwh1g_XgdLnpJI7ZFEZpK6Eb5PkJchJUJfpQqmPPKsnc8D-tMfZXAU-s0lPJLnLy2ogw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روباه مکار گریه کن پدرسگگگگگ
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/Futball180TV/100410" target="_blank">📅 00:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100409">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
🚨
هری‌کین: من بسیار ناراحت هستم بری بازیکنان. من بسیار ناراحت هستم برای هواداران. من بسیار ناراحت هستم برای کادر فنی.
🇬🇧
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/Futball180TV/100409" target="_blank">📅 00:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100407">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Iu-iWZie00IlCH_auiNB6qqUgK0IX7Lnt2PaqWjscNCSjq9T-U_ghG-4l9x3AZ7EFRhqbYLiNEeUde6gL_Lrbc2RpQQA8m4KatXRik_8g21RwsjGb4tygsx6PATXMTerjfyK0zcpx67jG0AGUyhNmOoaHKIWAmKbl_K7AfCSjBsl4R89mAxC6l9dPctsHs8nzJPcIPYdISZpRcvcOxFLz9j2oth8WP6jyfs-xw7gJBc__-lau23MBxOgcdYscAiX_Gwc-QVU7eGWQHn5gRAyyzYON19nZEvXTQt3i0MTOs5Ca7lFbQNT0wWQZb1PmkqaH8K5fGgDkm1JQp14ev4Knw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TNhrnxxL1eSHQu0W2YXzvxhjVS3n_tVc7GyKPikdGqRBiUMBnB17Yg4cbaPb2OLla2XDLRzziTn4qpMuVoAKWizDLNsBxP1qjzk2fJRsVifI9RzEhkyeoQowJAP0CJ8qjX5JsD91ajQIjFQ0RatQN5aJVSh7mr6kDlmogHGVXrBEM05JRXwexNvp4sMmdXTtQqhmsfOyg02KJPL4MPTh7F6a-fbre_bN4rl8UQNaPh3X8eYrFHc3erFikLjBR_qRMHGDH0McRGlfoyAjTq9t-AOWPkdHUJFkTPNnXnlUo9mzy4XcqAhowqFoD11iz6S7tPgDNCg5uIpvDnAvfUtu_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حالا بقیه هیچی، چطوری دلت اومد یه کاری کنی دوا لیپا ناراحت بشه توخل احمق؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/Futball180TV/100407" target="_blank">📅 00:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100406">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z81Zglbdx8MonZIpk9VJ8sLp1nkyJKoPEW4QLJRjW6CdVycjUbf21KlHZusA9hJcrc3qHd3RWQrCeZWSapyAHlp5uziZDnynOZiiINX_ia6yWOt0rVV-DiS8Ld__EXT_FfVY-Zsl-nN1Hj5W1lkLBzPsb-uExmWFdEAFDDdbT1gPuGMTmEP918z2CiiTmJTMdcdw_qcA05C39WVqVnEgu_babyRsX9LUxz5jHLjswKxpPy-z9bjwIt-M4i356_nQTH2Kta2i_zBBRk67dUtZejy4TB3mUZo9mS0fQJu3Ysu0zQWdP0aq9CmxZnb_D3thuJKtou2-PCxSToTR8rbkdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇦🇷
🏆
🇪🇸
#
فوووووری
؛ علیرضا فغانی شانس اول قضاوت فینال جام‌جهانی شد. با توجه به اینکه فغانی حداقل یک بازی برای فرانسه و انگلیس در این تورنمنت سوت زده، فیفا قصد داره رقابت حساس فینال رو به این داور بسپاره. جمع‌بندی نهایی تا حداکثر روز شنبه صورت میگیره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/Futball180TV/100406" target="_blank">📅 00:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100405">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YVvPzovC8vw7WuHJ6FN8UU3QahcFlAg5A2t0NpiDcHi-VRtbY3WSE5LSvdARAcc6pcYHwtmuA_JxLPcan8nonpzSeLwbltSDesdIap_8SmPx8OtnlBsQWN6hDBZZgLWj67JrjU6-ZSAsqOv3ymqMu5vaZ3i2rub9iJwta29a677e4Z7RHmHpnINg3sxVAFJ4c8uhvDk7RfEcDK6hNQ6aPNmCsGfHicbRHdq4DLlvkeqlZPLZPqPxu60RAXifUNwrCHe2bJx82_LmB143Tz2hASagXfikapzaHN5mJCH5r6PBAKQrI7jY62-8reBopKL76vn6-I7csnBwX4jfJyATGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعویضای توخل بعد از گل اول انگلیس رو باید تدریس کنن تو کلاس‌های مربیگری تحت عنوان «چگونه تیم خود را از هم بپاشیم»
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/Futball180TV/100405" target="_blank">📅 00:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100404">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇵🇹
➡️
🇫🇷
➡️
🇬🇧
➡️
🖕
چیزی نیست دوستان مهاجرت ۳۰ روزه دوستانمونو بهتون نشون دادم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/100404" target="_blank">📅 00:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100403">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VmlXBzp1pY0VHTgtBwoGscXwmKpwKGvI1PGItj_HXgmbJ8BBUmTfWxucGssvf72mwRmAkr6-OxoJW1Bnda2vDIq0OR01FJ4g1cahHYpulDwihHA4jlbSqkTHcu6PSooo_7WipoiFcmeiVG8Renq4xmkzTD841f2-y5Lyf3KvO4EF9fsPSl8ERzvxSqdylo0GFHYGUyybWKBq4i8VTNxPDo1RCLoviRNhxryD-CgsKA2ALSXcXBXgwFJ25r2Gecmnuc3REYCLL86qLbffslhc2x6XATf9jILkjlxGt5s4_txWKFCJu_k014jxGofhKzovGcOyN1dzn2V4x1cdvgNxHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
|| بیشترین حضور در فینال در تاریخ جام‌جهانی:
🇩🇪
• آلمان — ۸ بار
🇦🇷
• آرژانتین — ۷ بار
🆕
🇧🇷
• برزیل — ۶ بار
🇮🇹
• ایتالیا — ۶ بار
🇫🇷
• فرانسه — ۴ بار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/100403" target="_blank">📅 00:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100402">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6480a164be.mp4?token=l5tG3ET8oMeUJY0H-D_eDQal9Dl2lQDLWiW11vp_BWPLMnJYtPboLbxR7e5lENNSZmqG9LELMoHPtyuQjt5GICzn565lasFqNhcZsGFxt2HYBPCm8v1PyaCxl605mEoZx8tg6Iq2pSC2EcdyNHZxpaKmV28Ht__fSvDQP6k7F55HaQb97AJr8-xFL1zXTvBVXq6OcdvlxMKg35jKPjaVLy9zoohyARvxhyR4XuaQNMWbzPji5SoyRgeST-c6r3em0o1M1VKL6AoAayR9Mra2TYWYbGajZwbverrC2YEJJNvU-UFotAdYLegefAQHhh22hi4beqec25qRY3xyaG-qew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6480a164be.mp4?token=l5tG3ET8oMeUJY0H-D_eDQal9Dl2lQDLWiW11vp_BWPLMnJYtPboLbxR7e5lENNSZmqG9LELMoHPtyuQjt5GICzn565lasFqNhcZsGFxt2HYBPCm8v1PyaCxl605mEoZx8tg6Iq2pSC2EcdyNHZxpaKmV28Ht__fSvDQP6k7F55HaQb97AJr8-xFL1zXTvBVXq6OcdvlxMKg35jKPjaVLy9zoohyARvxhyR4XuaQNMWbzPji5SoyRgeST-c6r3em0o1M1VKL6AoAayR9Mra2TYWYbGajZwbverrC2YEJJNvU-UFotAdYLegefAQHhh22hi4beqec25qRY3xyaG-qew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
👍
اسطوره لیونل‌مسی بعد صعود به فینال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/100402" target="_blank">📅 00:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100401">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rbeJKrozH3nez2pP9zWquQKjlagJ37WxNwHARH6e5goigz8UJBKT8jgrTrsbOZZyynOUy2nXxTBhK5oL2t75dmRX7Q3TYouC9478HSXKft3nyVqHrHwgtev4sVIcoi-2evTw4UIZApLRZImLAk7I75n0Vu1AZ_qtL4STu5_fbUhhmWSBgpVlU3bQcObw2rRqwqpc6XDgAArZs-LOTRqcDdUMxhK1SY01ZgtF3MMJas0it7U_CNty66PwQlgKUc3iqaJL9e0tDPg2KhQ7_xXJ4KLYmFSEXD0L3uigEnB7JDcMqJwXfoFdWTCTd6XSmvKRp_ZCQOJkaxzbelA8YDhiEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👋🏻
👋🏻
👋🏻
👋🏻
👋🏻
👋🏻
👋🏻
👋🏻
👋🏻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/100401" target="_blank">📅 00:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100400">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S8A-hyhejfmuof125hA7QcXjxP7TrTJRNXUE_lxn21UZ_VlwiYT09NEmJRNtvxk-yXaVQMYW9wVFTLjwqOIMTibltPEvx1_v9ChqQno5lhUQ9_TxM-cGSp4hxKYVlKJ1vqj1v-zvlEfgLrA6NSKTQpton-NzyrrNxIk9VfB6sg4-ij3hTTLkHcKFKtvxY2AGKcq1J3kdP91FyilDHX-DPe-E-33uhLC_i4rxz3dmiBs_ue3jB6xYHdF3KDlCcdZpLjo27ue5iMUOMA8j6LtyWiSOZJdlW0qHQDM9ifh0Xf0TFf-tungpYU93SoOa_eOLA98u29Zo2mUuTfKx1O5YRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👋🏻
👋🏻
👋🏻
👋🏻
👋🏻
👋🏻
👋🏻
👋🏻
👋🏻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/100400" target="_blank">📅 00:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100399">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CCh1NBKqTCzeAwn6nxz25UbuD2fWIjNeSsVvfLXmZrOzTMEZwcU6JrmNtBrNUBsB69GpANK-AGgHTiF0oO3Wp0o3Py0ZsbOj-OMW7pPmBGR0Jsj4lnCdJ9va1bK4Y2l1awjGIMeUE7VztF4dXMOYIhe8dUelJTLYrbhZ2hls8L5az4YxOBcW2RnQnTuTnDSXICWLJMHCEKfHN_Pb7LFbK79TlaeNRsAZnmgIXd3Y6Qewp5iglXjJg7l3qCzoadsid9rxPpiDLTEj3Dvp7L8_G9Nn9p2ccmU2RESseZ2cRdvqqd7SwcLGRgSUMG0ys6qt2ABY8P5Ahn8Plo-1KNRAyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی، اسطوره فوتبال، با ۱۱ پاس گل، رکورددار بیشترین پاس گل در تاریخ جام جهانی شد.
🇦🇷
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/100399" target="_blank">📅 00:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100398">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">اسطوره
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/100398" target="_blank">📅 00:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100397">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YWiwCABTmsQUmto6ISG23NLuyp9P9DLxCFdV65zLyY60zRpqA1xDPX1IdRbpA2wCo9ZDAhz3tjOlGURoWryGD3vovj3ZZOtMgeyFetupr2whP7_uinSdga6SixgDJamaDPrf2BFLjPXw5JZGbPWS5uDojzc3AlQTKRpzFPjDO7bZNz2sLdKkAqAA5keyTxKATjSx5tpzgbrJ-hDsft2I28WA15QK8oAoR6eyZZa_k5b6IVOb1HizshNgnCIZiW2IvWWbI8xax-QUXcQKxH7E9gDRI_m1Nj6CqC9vt5EKIWWnJZ7ThK8sCHF4H1aDNURVZXwHfaqhASScYtysWlqDmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔥
🏆
#فوووووری
از ESPN: توپ‌طلا جام‌جهانی فوتبال به یامال یا لیونل‌مسی اهدا خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/100397" target="_blank">📅 00:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100396">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P3tgygK7MCq4ON2zZgiB1CMlkxjaZVewkdfSZpzoyv_R6B_8wEoYG3VXF6PkmI_XCM2hx1YxkqtosMMcP89mCJiBioVbjkN114QyySEPLQP4xB2i5a2HMe5HIB61al3c9pO7_f3hVjDcbsU8OEohnGOGTRBLlfoB4Cy28xs1wLLboKA9Gppij2y2u--FYv3xrq__NfLRvyKSvZMD2zJBJqg3rlXTD-HPLpFItC7rPrkVppZSzpL0nkw4sf6Ca1s8xZ97nVjgSJExQA755mJ0nu5qvK6LEOfRNX05GG8v3JIN1aE3tU0KQkx6UTo1w1F0Ws-2uRppyLuslrdogZdo0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
آغوش هری‌کین و لیونل‌مسی بعد بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/100396" target="_blank">📅 00:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100395">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d66FAB11EFP50DmMHcHXx1tLs7fqxRXRLNZT9qUKGQ0wx4XoSSMbFJ13l55XK20P9cbbUhKIRLUcGHZi1wgUnmK_UFwg9rShB9IrvYHiWoB2Ms8gME_eftuZoXNI6CaZmcAiQmpbg20awGmpVjtDR_nJO7kPaFk8raUgH4YvJ7-3DXCaqQX2KeTpEQmdOWmjeQ9B2zk2PX4pEF-crbVZvGGUN5598OyKk6uxQ3Sm6h-KrANMZZCJiEmK7jDoLGKRa39aOCqe8WZ9IXFxjLPj5S97xLULGK6qT090jP3C09fiucsAvoJS5XacvYmHlvYo6uuLFvsL5H3cZz177pAMAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسطوره
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/100395" target="_blank">📅 00:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100394">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/nbephOCelUgaCmKRMX3KPiSWo2oTXOLtKklNJeyX2hWRk_3L10CZ1UTZinxTkf1FJqOiIt4iQh15IxQVkNKUb3m2miRCDfKGf16i2VxNa0OCDFf1zY2SoSsyTZKn4xy7v3FVA7KhqvVLlMjsDdh9WH0iQrKrHfcLiyDOpbwtgKkeRmCmBd2kmTbnJ73ktEqSUWoeFNATwafFT1S7U6x2y4nETEwxE_JM5sGu-WQD00enadhtEjTlWBJlh9YdI4lwswkhdKJH1iQVf33iIgT2S_rz8z2iIHvJw6JUBQvmGEf7id5jdzKGuDN5wSvdnPlNLwvh_eQfH93sdbVwTwAz1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضربه سر عالی فیفا به انگلیس
😍
😍
تیم ملی فیفا ۲ -- تموم دنیا ۱
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/100394" target="_blank">📅 00:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100393">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVVpWIYyzIW1qNUHUkQPyU7IxE-TzTbTzSNe9Ohx_KI0PUI1hxO2-1wlZ1nqa965TQHiJfrakyvE61QJxE8G9n3b9Fbp5WMi3GxBHWuW5W2VL8tQMCutVSwbJoIGexgVOIy7A_zY62kZHM18J6eYpvJu241yP6IZ9kiRWd5THekT5kXmhY9KkW1lyOYT4VKnXRaWQi2vz31ZoVXuXDJ7RIC553CadmXJNIW_IgulgKJpmpvFBc1i8zwED8Yyg35HUSvVuKGVGY5LhN3SKxR-e-vd5mlTJJiFK9KI8XF7uVcShXmmx27KPGGIoa1O3QV2Df8aQkW1rW4z_VLimke3Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
اسطوره لیونل‌مسی بهترین بازیکن زمین شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/100393" target="_blank">📅 00:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100391">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔥
خلیل البلوشی:
- فینال بین آرژانتین و اسپانیا، چه کابوسی برای برخی از افراد.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/100391" target="_blank">📅 00:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100390">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rmtZnb1et2WRT60N7CiKw_QsTFzrtY0TzFRZeLkHrAelrg9k1sBMWUowhTHsdDIdtwMsTMuhQCGr_itC-P9ZkYw5VX3Rq06811FGqC4h-OAYscoalaNbGngZpefZNORF_GSd4lI0NhP9qd4D_rPkc2FpF9qX5IwIZERrUSLBabVrzYHbI-mxVagVbGNd9uT736hoJdXeYnKpfBJKW0sjL_ADiWk9pc_nMs3HRUlchlRI5gsnlregm97cmnb0SKQO84UQ4Nlz4GdeX_oLcMiMwJNEv0LdI2sXNT7HOePpmEJj7_wzVs-gvXHr_azuznj9lvon4JUUaMGlUeR93H4lnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی|ادای احترام جهان به اسطوره مسی و آرژانتین؛ نمایش درخشان مقابل تیم انگلیس؛ اسکالونی و تیمش برای دومین بار پیاپی راهی فینال جام‌جهانی شد
🇦🇷
آرژانتین
😀
😃
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/100390" target="_blank">📅 00:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100389">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">زندگییییییییی به کامممممه اقایووووون</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/100389" target="_blank">📅 00:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100388">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DSCwsBME4SnMZLbDxaPfVmSZmn07NMrneCUjjZBdyTQAs551OqlfOzfw1ngFO2Ew98Csf6oK-iqqJNoK3QehFlEhMKqqYiCml87M9XmMVGdOfXLeM2Fu4n7z_eD11-jAVzBoar66jDcgGZSVpE-eJPfVO2tVotxQIqKBs1O8O8_l3ljXTGQI__71J5vcQyJ06WVBjE405F0TZZh0wtLuGzmVQEdebpa1Jqms726agZQpFEmp8gOSAhkRocagesX2chWymj_i91r7X4LvvJtTyO5LN-EihUWsdsFQJUOp8tNDeM9Vk4AAxliIOM32DPZKUk9lk7_HqbOXIL7DFNZbQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی|ادای احترام جهان به اسطوره مسی و آرژانتین؛ نمایش درخشان مقابل تیم انگلیس؛ اسکالونی و تیمش برای دومین بار پیاپی راهی فینال جام‌جهانی شد
🇦🇷
آرژانتین
😀
😃
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/100388" target="_blank">📅 00:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100387">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KBx_uj4QJWquAeU8VYIjew2JkNSaVR8Xi6uvfkEP-APcccaWDwLYf63Ygr5pVuR7XznuhqeUKhGUlbRh0ZgA9A_H4K3vo_E0ge3JebdpF0szgmaDjmMiRi5Qrm67hIYtbXfD711gHj27J_jBrOH2FFNrbCdmfTc7aeuNpatmC58_v7VRv3jfOdanVpjxHJDA1sydgJqfb77SGDklGQPo3MLPDQ21xUar-22LiLbLi7RDjG1OjlqObmhK7q7GxK352QBqmjzclLuBYyzG3oYKG-4qqsy8HLw2dkeqyxUsHqWCmodC92MpAVM_jM1Vbfqotba4S2LxdNxG2o0pNjK-DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت مسی از دقیقه 80:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/100387" target="_blank">📅 00:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100385">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">توخل حالا میتونه پرویز مظلومی استایل ده دوازده تا دفاع دیگه بیاره داخل</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/100385" target="_blank">📅 00:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100384">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">کسخار انگلیسی جماعت</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/100384" target="_blank">📅 00:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100383">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">حاله وقتشه امیرعلی ۹ ساله از کرج بیاد هشتگ پسرفیفا بزنه
🤡
🤡
🤡</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/100383" target="_blank">📅 00:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100382">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">میگما ؟
تا الان که ناداوری چیزی نبوده ؟</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/100382" target="_blank">📅 00:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100381">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
🔥
گل‌دوم آرژانتین توسط لائوتارو مارتینز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/100381" target="_blank">📅 00:25 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100380">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">اسپید کیت انگلیس پوشیده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/100380" target="_blank">📅 00:25 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100379">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">مسی: من به اینا نمیبازم.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/100379" target="_blank">📅 00:25 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100377">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/591054bccf.mp4?token=Y9YLbaNODwWqw_Oe-gA_IISmzJz9nzfQ3lfap-d6UjtUll2vBbq8cdFgsJkoSd2j-ukusUtln_9CdfVTeUaYOk_5Gvu-Gr7L8gj-nUMLCtNhOnrPULmnfWk9HU3mkFPYFm3pZZ7h32D4wn25am3E3HJj_DbgDB5bYaM0aKU2LwreiTUZg5bAiPU5aSwQZRX0x-FVZyHCx08jagHyImJuEFqBoe5ZtvggH8Yoj8IiZchmSctQz3A_wsz4AVjuC0V-_Zj3NW0qPWt3hWGok78WmU2y-oy1eHkSN6b4sk9QfDAoLRpmo6nZITUrH7L3TERVuLLVgV9u_uzSzhXDv-4vY0jxaQafF2q3W7K0KAHXV29YC0jya_LqyOLYK13OpYlPAhML7KzWac74gx-MPTXNHKcwX3DIt7CpOmRBf9LZyTiaBysKAraZ_trFY406TY1dzsdXOElofzBWQkSx0C9gXKcj7AQNZ05X3hguNjxZqstfGqqAXNNjJ5KuRaVpzssWONw6PuJghhLcF4v0Ishsfhei62CpPwBwpvUzRGYxOJvpDntvlFATGgdTSdagxIlZ2y-vAwwhvvEEfjP2gy-2h2yoRjNJkzVFF-QlIKpmULtk8GFRZIP1PYCw7vPputAOF6VcpL0DNzgV2uKRR4kGE8IZjpvzDh8UqY8XgjL16rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/591054bccf.mp4?token=Y9YLbaNODwWqw_Oe-gA_IISmzJz9nzfQ3lfap-d6UjtUll2vBbq8cdFgsJkoSd2j-ukusUtln_9CdfVTeUaYOk_5Gvu-Gr7L8gj-nUMLCtNhOnrPULmnfWk9HU3mkFPYFm3pZZ7h32D4wn25am3E3HJj_DbgDB5bYaM0aKU2LwreiTUZg5bAiPU5aSwQZRX0x-FVZyHCx08jagHyImJuEFqBoe5ZtvggH8Yoj8IiZchmSctQz3A_wsz4AVjuC0V-_Zj3NW0qPWt3hWGok78WmU2y-oy1eHkSN6b4sk9QfDAoLRpmo6nZITUrH7L3TERVuLLVgV9u_uzSzhXDv-4vY0jxaQafF2q3W7K0KAHXV29YC0jya_LqyOLYK13OpYlPAhML7KzWac74gx-MPTXNHKcwX3DIt7CpOmRBf9LZyTiaBysKAraZ_trFY406TY1dzsdXOElofzBWQkSx0C9gXKcj7AQNZ05X3hguNjxZqstfGqqAXNNjJ5KuRaVpzssWONw6PuJghhLcF4v0Ishsfhei62CpPwBwpvUzRGYxOJvpDntvlFATGgdTSdagxIlZ2y-vAwwhvvEEfjP2gy-2h2yoRjNJkzVFF-QlIKpmULtk8GFRZIP1PYCw7vPputAOF6VcpL0DNzgV2uKRR4kGE8IZjpvzDh8UqY8XgjL16rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🔥
گل‌دوم آرژانتین توسط لائوتارو مارتینز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/100377" target="_blank">📅 00:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100376">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">لایوتارووووووووون</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/100376" target="_blank">📅 00:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100375">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/100375" target="_blank">📅 00:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100374">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">چه فوتبالییییییی</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/100374" target="_blank">📅 00:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100373">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">یاااااااااا خدااااا</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/100373" target="_blank">📅 00:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100372">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ایننننن مسییییییییه اییییننننته مسیییییییی</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/100372" target="_blank">📅 00:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100371">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">یاااا خداااااا</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/100371" target="_blank">📅 00:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100370">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">یا پیغمبرررررر</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/100370" target="_blank">📅 00:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100369">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">خدایاااااا</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/100369" target="_blank">📅 00:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100368">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">چه کامبکییییی</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/100368" target="_blank">📅 00:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100367">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">آرژانتینینیننینینینینین</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/100367" target="_blank">📅 00:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100366">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">گلللللللللللل دومممم</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/100366" target="_blank">📅 00:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100365">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUlvV9Tmwdn2Fgl4HHMoAv_8-RFlEaXKETykmTy7OdZHBnJfj2MvzKl_G3I2OtEmWY6EhW6DWvkkgoLuyEY1phGldXXZGDE-Ml3ob_nG-ve8R5mX7hL7iv2O5vcl5Pe1fGY5BU3LKT0qvxpJIF5ndQ1eFc6Gu7uP1-xJzFd7F0btb1QWTS3vRGZkokrmgUnvqlBKxRvgfh-SxCXtZeXqjch3gJ6nKDt3tKyIXzuBFhfoKarnScU2BUB0OkoK5yixEYXn3UqBOptzga4njqX4nExHet1TUjSznqM3gEiLPKPB_JcO3z9QY2OMWb1bqc5PZky0m2n-LTBFyk8OEA0vYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منم همینطور بانو
منم همینطور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/100365" target="_blank">📅 00:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100364">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">۹ دقیقه وقت اضافه گرفت</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/100364" target="_blank">📅 00:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100363">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58d3c31b26.mp4?token=oc_XYv3HgupClDEo4pkBkRXBBkH9AjmBW_uyfwpm7q1PO9hCwn5ANTUC--Ld569R28bSLiR2IBg7j2u2Y7VT69cEWHnpaU5gW0XQWpFDD34nIqS-K7DdFW4qlO_1aJs8LSX3lH_m-PGYCUrltcw-eo_k4Cuxy0yFE8sl-kNgS6fjFZp64ZRXP38SEcvQymJZlenc5V1edry-WyI4xMza24CsPsWpDQHJvH62EcDh1qO_VWB1P_ce5kuEl5c4I2F8WHnQ974kyNGhsDLcwavmT2VXKnPgGeXWrmgLbFZcJxeN_MebphlCbunVRtSZka8WHS2xuGuj1DVRFtuDieAiiIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58d3c31b26.mp4?token=oc_XYv3HgupClDEo4pkBkRXBBkH9AjmBW_uyfwpm7q1PO9hCwn5ANTUC--Ld569R28bSLiR2IBg7j2u2Y7VT69cEWHnpaU5gW0XQWpFDD34nIqS-K7DdFW4qlO_1aJs8LSX3lH_m-PGYCUrltcw-eo_k4Cuxy0yFE8sl-kNgS6fjFZp64ZRXP38SEcvQymJZlenc5V1edry-WyI4xMza24CsPsWpDQHJvH62EcDh1qO_VWB1P_ce5kuEl5c4I2F8WHnQ974kyNGhsDLcwavmT2VXKnPgGeXWrmgLbFZcJxeN_MebphlCbunVRtSZka8WHS2xuGuj1DVRFtuDieAiiIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
گل‌زیبای انزو با گزارش عادل فردوسی‌پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/100363" target="_blank">📅 00:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100362">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">داور خارکسده ضد آرژانتینه</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/100362" target="_blank">📅 00:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100361">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇦🇷
گل مساوی آرژانتین به انگلیس توسط انزو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/100361" target="_blank">📅 00:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100360">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">گل تایییده</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/100360" target="_blank">📅 00:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100359">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">کمترین حق آرژانتین گل زدن بوددد</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/100359" target="_blank">📅 00:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100358">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">پاس گل مسیییییی</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/100358" target="_blank">📅 00:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100357">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">این ارژانتییییییییننننننننه حروم زاده هاااااااا</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/100357" target="_blank">📅 00:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100356">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">چه گلیییییییی زد انزووووو</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/100356" target="_blank">📅 00:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100355">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ارژانتیننننن</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/100355" target="_blank">📅 00:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100354">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">گلللللللللللل</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/100354" target="_blank">📅 00:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100353">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">چه شوووووتی گرفت پیکفورد</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/100353" target="_blank">📅 00:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100352">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">چه پاسییی داد مسی ولی افساید بود</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/100352" target="_blank">📅 00:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100351">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">انگلیس شدیدا تحت فشاره</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/100351" target="_blank">📅 00:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100350">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">پیکفورد لاشییی گل بخور دیگه</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/100350" target="_blank">📅 00:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100349">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">پیکفورد چییییی گرفت</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/100349" target="_blank">📅 23:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100348">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">وااااااای</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/100348" target="_blank">📅 23:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100347">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">چه تکلیییییی زد اسپنس</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/100347" target="_blank">📅 23:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100346">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل اول انگلیس به آرژانتین توسط گوردون.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/100346" target="_blank">📅 23:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100345">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">گوردووووون</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/100345" target="_blank">📅 23:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100344">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">انگلیییس</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/100344" target="_blank">📅 23:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100343">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">گلللللللللللل</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/100343" target="_blank">📅 23:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100342">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">رومرو هم زرد گرفت</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/100342" target="_blank">📅 23:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100341">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">بلینگهام و مسی کشتی گرفتن
😂
😐</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/100341" target="_blank">📅 23:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100340">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">انگلیس کووووون آوذدددد</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/100340" target="_blank">📅 23:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100339">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">وااااای</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/100339" target="_blank">📅 23:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100338">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">مسسییییی داشت میزدددددد</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/100338" target="_blank">📅 23:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100337">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">پااااای</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/100337" target="_blank">📅 23:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100336">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
🚨
🚨
آغاز‌ نیمه‌دوم بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/100336" target="_blank">📅 23:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100335">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pExEFbhEq38omtCaEQmw4kMulFzU5jtCpvICLhB6Mr9mfxX0evOPK2PkHiG1w51zsrVO26RJa8CjnKM6-BwL4eJUi81WtQlwVg9XhZ6kSYlkL7SYUsAdWTMpvOeSxG08VS0vijN8wi_mARwNWhM7zM9DiJBznl1YWR63oNTGUaCfcldRilzrdek3KeAkhwJDn3Ok8oDqlxGYRYl7eEIYnTXObIbkVY67AfwcOEULhYGkO7ECnIBT-vhyi2SM3Gpl1gcHrH5MX_om99LQ0YJ9AIiMTCniisokk797Irb2Q536SfZL8YvvpELNPJ9TREdJshBGaLwAON-s8RE7iaTHeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
توییت جدید رسانه آرشیو وار:
🤐
🤐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/100335" target="_blank">📅 23:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100334">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kIlCfbmuOa56fU4YtV5FrI6L-F3LuRiE8OruVvN8UWO_eh8XIbov3dmhadQkqiGfUyknCo2Sb8l6rPFPbVIkCeV_m9Jqk3BgbU9iRvXpiHOzOZhFpc6RKcz7IoC2TQZCqDVzZGZGWR5cTj52grEgKDkJBc3Hrvfanywg73YLZzNjU7E9cbAiQ0VZPJN_dQfXvYXw1CHFP5eRrFe2hVYR0Jiog8r4rwEtA5bwHEejCJOn7ytJvEU44SSHZZlF2OC252P_a_tGQvnul_nQH-L2xyttzmxTS3W08o-2ebwBdYzUSs4R0QAaAeI69ER1bR7hzcHBFTYeedUvAXdh4q4MWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
🏆
روی‌کین: داور آمریکایی رفیق ترامپ و عاشق آرژانتینه. چطور ممکنه با اینهمه خطا فقط یه کارت زرد به آرژانتین‌ها نشون بده؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/100334" target="_blank">📅 23:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100333">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G_W7dNU1ZPNjzGAyi5knN8dGskoNqZ7r7DSql7NqhdJk-c5tRIavXSgAMEODE_qQRTZIfIhuVkGhHRjUfq1GQnlbZx06Ksbt0D7E8ARrhaMo3Jq5w7Po2B81yykwxKVwpaQ5RLkfGEpP5pcijQjv9sDI9vRZI8CkFN7ethdDDuLjuSpcsPsFr3bE5KYFt5cf3KB0L8AT8y96RSK4uqdWzv8x8V5-_tWDo8MYqaEc-KoJVtoLhx0FefxRXJsP1mhq7THFhgYBbddKnP0sH3hR-s5qvUkolKynslXq2qNuEVIYczx_yDU15XjlvnIdGbp4UX60DwnSYMrUJP_yWcWAoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
👀
شباهت دو قاب از تقابل شماره 10 آرژانتین با انگلیسی
‌
ها
؛ از 1986 تا 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/100333" target="_blank">📅 23:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100332">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/100332" target="_blank">📅 23:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100331">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EyQ-PRyDZHOsUDNfuMIZTXsPN2JQLc2pHl-dU0LZYQlNDYw567h7kEuCbIqKb6pDsp08icknw3O6t4_Tpf-yV7dIWhsi1i6tlmre1BdhlxyocK2BUyduKf7qNadbdQeJEd7txohONbymcYCeujSYcV4TYQv7CPgLrfz-LfycLPdiYI6oE_1z85Fmu4U7YRITL7THbAkOBnwBLhNUqDDFsC_vAMSZoFy4i2JZUkefSbHL-_zVKGnTB87YctPtGwnatvRFu0b8-HvXt3IcvTIDarUwK8O6GlQJHN0Kn7mATu9A8H_peNjh5hV0-z0niMBcPeQSJpXZ8K6rJRKul7pvmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/100331" target="_blank">📅 23:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100330">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QKuT_gZinPJynnFFYkExfMRpf2GgVbNBUMyqz7sFzamg0F8a2Yz_s1Jg3SsgFd-1Ufe5lYFCf7uDML18iFBQa4rVFc4IqJEiAxKrQv-SoR0wNxSgdEz92V-zDYGkCn0h5ssc4hOkwpMVAOOknaz8Tc0Io8B8LDaA1zNFLpVMO_ss5107PWRJD1t14eZj8H2NKcpJKkrFFslCnZ2rlTVWTpzY6CxkEVRAGu_Y2vfSApKaiazPsn1-sfqE5tHPgR3-fz6EGm8ujoeh8MhO1m_mBBi-D7MSHIFjeYKO6YxHiHyii3wAWR_OlUwDythpBipEseEamFkid2D6F9D7hFXDsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمار نیمه اول بازی:
0 شوت در چارچوب و 19 تا خطا
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/100330" target="_blank">📅 23:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100329">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jo5tMSqMUsvsIUT5UBoUnXTc2WFV9-xBze7ZW2hbyLuwsiksW5Nmur7OGlK80izIL_jUcFyW3xExPva8M-I40JOgc_CIFv4GUP6hs9sySb8PLmLEHVgnPDCCehipLYI4quyNX5itayJ90hC0ud9qi_zirkiCbKSZk4UmUHsZfM0KFCtFYKOcfvqKPfS7B6_y4iaIlfAb_MI9i7t5Tvmipimk61yqTOiJj6YSXAEf_KsuVIzQzFc3V1pTmZvw0UD-u2D2MaJBsiclpOlm_ZLCadM4kx0fjT7SkYiOVXYfoqct0fSFOXwrEpQkgbVxw13ikhpp2oNKRY4O25vKmN8cgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‏
🇦🇷
اسطوره، لیونل مسی، در نیمه اول بازی مقابل انگلیس، بیشترین تعداد دریبل‌های موفق را داشته است: 4 دریبل موفق از 5 تلاش.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/100329" target="_blank">📅 23:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100327">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
پایان نیمه اول؛ آرژانتین 0 انگلیس 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/100327" target="_blank">📅 23:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100326">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">۳ دقیقه وقت اضافه</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/100326" target="_blank">📅 23:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100325">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">زرد واسه مارتینز</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/100325" target="_blank">📅 23:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100324">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">آرژانتین داشتتتتت میزددددد</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/100324" target="_blank">📅 23:08 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100323">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">وااااااای</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/100323" target="_blank">📅 23:08 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100322">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">وااااای</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/100322" target="_blank">📅 23:08 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100321">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">کارت زرد برای بازیکن انگلیس الیوت اندرسون</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/100321" target="_blank">📅 23:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100320">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">وحشتناک بازی فیزیکیه</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/100320" target="_blank">📅 23:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100319">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">انگلیس بدشااااانس</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/100319" target="_blank">📅 23:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100318">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ووااااای</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/100318" target="_blank">📅 23:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100317">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">استونزززز داشت میزدددددد</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/100317" target="_blank">📅 23:03 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100316">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">وااااای</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/100316" target="_blank">📅 23:03 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100315">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
چند انفجار در اهواز رخ داده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/100315" target="_blank">📅 22:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100314">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
چند انفجار در اهواز رخ داده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/100314" target="_blank">📅 22:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100313">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">فغانی امشب داور بود کون دو تا تیم میذاشت.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/100313" target="_blank">📅 22:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100312">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">تو 12 دقیقه 9 تا خطا کردن</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/100312" target="_blank">📅 22:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100311">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">کشتی کجه به جای فوتبال</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/100311" target="_blank">📅 22:42 · 24 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
