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
<img src="https://cdn4.telesco.pe/file/sUmA3nd-B89jWW6HDwhHZo0ihHyuxftv5_fAebwwIAJvMmSCMjgr3nm42K229HPhRQX9QImlxeBf8fIW3OPmhm9bmcnpuw3sunaf7ewvfBLo19oonOvDpMyHuidhRw0CywTbwZ0xgO-cIjeOjJCfGnRVNev_k1AJWm2GE2teaiAEXDpsf9IKvGIZgNiVrSvFqBgfrn5G1B99mi-u6ZoImfT-vcrof1t-k1yslbapWGHkQA1WR3enu9II8tyP7T4rNL3cBlVDwLu6ytZ_anZmWTjqqM7QFhD5xJ8YF2d689jcaU8P_Uin06lMm-Mt87FzwvyrJYeK5TYY6M9ZoL3R-Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.08M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-01 22:38:16</div>
<hr>

<div class="tg-post" id="msg-692468">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
همتی، رئیس بانک مرکزی: در حد توان تورم را کنترل می‌کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/akhbarefori/692468" target="_blank">📅 22:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692458">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BldFAAEoWv6PAoxU7OSXgkbWKS8Ky4d2ajkDXlmzYWDlyEn2_X69j9jnhpZOrqxcWHNfzvPSQ0oLUOslH5yacf3Ozvirndda1dfVo3n6iO0qJWwuIPF_TwxwjEXnkAxrnnzLVdca4bMoRxJFFz-DslcFkIzm5b7EusUYegs42NlxYccrCgtzLafvhVyDsGAp0WosPFbrane_SI9MMCfRnSmjMZdjSF63VHN6TbwsVYSRvBhKWA9ZE7bPNJlEoUcnE08tKldTMT251kKyBjhv9vBgVRJegX5G5N1qIumrHKxrS85g5HL9cdRQGSRUDVhljsu9nJYW0H4k6n-NFJVYNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T49DCXlWR9Jv4ChQW6yzB2rBObMTegUxpVDeZxIhkXYmBNDhgZjGbdoS6cfpnTnKNQCYdbi7mrudNvmbz05HONnJ7yFkslK6PubjGcQ3w-LGpaZIMAtnJcwgPi4MORjNyjPr4X6AabsNVkTt_4nwNrvN89gQDQGwlK9WhceI9HIIcwj_JfomDjxYOWujav2qv2kW3jL8kl1PDQkVDx92fMUOt6zjXPsk-OIxvCHiZ4ncxNaZxNnWoAy0OrhFDyMtipXqX3pvt2POfucjntI1udalb-Kr6-8oMXwDRWTDpeStI5zSMyj2h1Sgi4JCjia6wxEEvspnVQ5Ll-Z9tVpgPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R3iAbkeIuBilV_otH1u23g70Rf5E8f30z7HIiWIBerbFmLQWsYBshMFewby3LZEO70H-G2dAYPbjCY2KDTKY5ej2T8Xv4KpNozWIz4Me6QRUUSyjy8ZvqMyTNtMljOx-290l5BnYY8PkOyN6BoJRI_YRwk_RmOvQRcn28j2D2BmvE3dxqX0Ff-XSTHVufAMJ_AHZrF2f5A_IHouq15DKcY5yotdWBx6ybcPaskOEpKPnK0h4dYdLX96hrKy--4QYX27sKiTElnTbjEtExnWYuPtT6ODE0k0rythWxwneRtnobcWEnT5C_VKJ919AQmrjKqfrua2IKyzyJuuShD9Jdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eZs1WkZ4KwOvpydYAMGOFGzt6Q0Y-dBb7fg2SKrqqaPezm1jnNRG1LKplfUEC7rvegPnQXCIVTj8dFVoNZSnUI18mtRT-pSO_rCsYMFPSxcxrjwVa0A6ARfeg6vEafa3Bihnf6-GVBpi618aARt0zMPiRf8H2F__HciBrAELJa_JLyIjOgTLj42TLdjgCsVXIo3MwyOLMUlwV7DGBC1s78L2zajNYRnUpM4Jpq8Ea17ihjCvewHedn0G_XtYeMv8_zoS7z7-pWsPn4Bymvn3-ruZxM82k2btt8WKK1_JPoi4Z5BUUFeQ891RVDptkSCoEFCfziq3NzOwKMJjc0JqbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UFMdBgoWPIjF-PGz3vp-SLNea2G09C2cFhLidiJjnKR1SVWwoO1PErStxv8y3SwxKloQsCxstkuiRuro4fJyHaIHlmbP-i9jMknJUTs93X8VK_n-8qhoLcIFeY_LgFfx1pRcXjkcuEIqjKtEAXBoAB0jlxa7STFaLoq2JC9LuzfDkNiIHErAd81f2taQVGr9FVZuUZvsDyJhz-nz8pRrOxDSmj6Kjd0__StgftMDjLZT9k4gQJ0qE_nDXtmX_uLWSjs-W9SVrzlkYW5bPXtBAtkiV75kNcN_mCAbUP0o7FqquuZSqmzGzUcGUXHVguwrEKYwl1OMxHhcydeQ4hf6gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HxmCfqYtOsCGZgOWI_XzB-FFCukYWfh5zTVuMLqcwVAM1AoOCltXaeWGpKz-2f1LMdJ2EYDUM0sps8zcOuXSTxW1ae7GrCu_fVD4BZHWuo8iB6Dwu24oKM3AXbCuRVTNUsn-2upNkx4dmptXcu8KW0g482JGqi7CzaUow9ujPCmr0amS5CJblVQGFfP8RW4h9ljrt43NdlXafJKXAcuc-itwGUBEOWINJ_b_KwFEWD3cy-aC3fvYNu6_-7DEEWBbqW1YYhX2P6f5e_7uKv4htdVejNasEskjGXfIYVT_etLACwug8jfsy5C2iRuXRv4s6jbcDevVFWfPkwWtLnd1KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rRdb1La8_QgpVwPf7EF3HD86KtkhiM2PssZpRj3PJj0Ug3R5wxuOgGSKkRuAE6v4IuD5xIIgnaqDko2Md6nI07ou8UCOn9jru_4uSkQsDj-GoKja92yIs3MEjSNPs99i3SDH1NNv-CSjXgek5ETboSP_LdEqoU0EmAia0u3S3b4ReBtEzPmwFWxVJB_b9SlC98oaWyCf1WjKex73nER70uupb27Ee2Iu1zvs1Pv_EArTin8Olqhw0_WoKa-GC_c_PTgkrf3xnGnkDKZ6LZcX-x9rQiE1ELcl3kmoBv0dhDrWPen9GfppjrxIRmLbgxyw8uGtValEcPEvk_lpmqJ0gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WpHlwxCWwnl8u8HXvZhlmXzq5FJoOgMXsK6Rr87qLbf3IB8OPWYpUrFA0vx01fV0X-D7-EtNyjoyJOoIH_uBs1DZpZdvOBtXfncoLudzNRVveAFRUv2FN9EJ4Pj-AA5KUODm_5qM_yIPr10dCT2UC7tIYx89d1cRGQcNBZ6c7jvwRiFyu9pQTkSYJmGF2Gyh56cm3uHMnO0x1dciTMr7Mb8hx8gn_Z9OWg0N9YJ_O8tgJ6o7ghrbfJcKVFbJHmeiczzziGY3ZyGwSpSMCiiaMuIMQg3ARHcAyhx7O3FssKK5gNs_LvGh0C4IiZkBnvW7ydKtX-GuQNcRPcDPLDiUag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RqDkyZE9IHLmZTMHVzzbKu_aW-I6B8FPFuUgYmF4fUhCkVcxyKkFgkyusgPtLKVx15P3IPkBtDWdvwQHw5RexWyuAzQWyrPvowPKts6R8IwR8Ud0alJag1iF12gHKleLpRA4WnAFi5QvMxN1n8DLSm1KYo2E2Dgv_P5YRyP6nJ98rT-kE83GeARK8eWwGPMMerdtYYPjYpNOn-mfPsVo0lKZviVg-RTYfmqnJYqcOYmKElc5RzJ_UxE5dbImO-GK-4t3kzRELxIjDrnVGxGOiPJjWktt2_UYhYXefVzFRKQzV0yrwTgLchllPO8nIiMQB_mAi3_jClaBdInYj3dMBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oPRRfq9SzW9zhBoj9Lvvl9xWwxEF92cfXX3EBSqI0rDxoBTW1ULiBzpWW91lEYOHJhnSaxULImMaqB7G-lwCveEHCrDzYJJqRn9Yjx7NvDaWWzOIysJjTh571H6-nBvg_bmYZ8Ng9cc49H9uglriYnv8Fdo3C6cipUmzgdg8K992mQX4WQokXEbGjW4JxljkjEpY73BdxjX8mvId29H58lYEVfzCLmnNIg7dbb8q-_5T6_nerVAfhCd0edUmruwOi0-nQia1OgLStmxUSqEGvINT32Byva8ruAHmBzoAqXOV7mkCXDWdjMspKAUVLmPLeeEc5mMeX019LJnv9DaVtg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
درد دارو
🔹
روایت مخاطبین الوفوری  از موانع پیش‌رو برای دسترسی آسان به اقلام دارویی ضروری.
🔸
در چند خط  روایت خود را همراه با نام، شهر و نام دارو برای ما ارسال کنید
👇
#درد_دارو
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/akhbarefori/692458" target="_blank">📅 22:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692457">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2a682239e.mp4?token=N9TbIPnOZugGxqdeS1xfoAu_g6Cb4FWuPQrqfJHbH6F0wIq6JVEN1FJVXgoAcVMXuFpHegC0ZFHW8UDqFSr5uJlFmoiKHpo4VxFWXFbreYKqFwo_Syw_lueTbyGIZ8bLHWVla4hZXE5MAbuF_ty9QiaudG4S8ECVM4PxHGtELqACV-9n1BZV3Ikge95Bod4k80xJ7OI11JISb6EshuKNS8MjTZ7u6jjn0SNTai_dCesCwLKBtLrLfTf_VULAY2Ia2Gx-GCr483SFADkdobWgblHJWAduixsEHkztya4rRexEZEnZgCuugJwLiJ41O0sSK7nF5Ef_ycABYvQMqJgn9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2a682239e.mp4?token=N9TbIPnOZugGxqdeS1xfoAu_g6Cb4FWuPQrqfJHbH6F0wIq6JVEN1FJVXgoAcVMXuFpHegC0ZFHW8UDqFSr5uJlFmoiKHpo4VxFWXFbreYKqFwo_Syw_lueTbyGIZ8bLHWVla4hZXE5MAbuF_ty9QiaudG4S8ECVM4PxHGtELqACV-9n1BZV3Ikge95Bod4k80xJ7OI11JISb6EshuKNS8MjTZ7u6jjn0SNTai_dCesCwLKBtLrLfTf_VULAY2Ia2Gx-GCr483SFADkdobWgblHJWAduixsEHkztya4rRexEZEnZgCuugJwLiJ41O0sSK7nF5Ef_ycABYvQMqJgn9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روح کودکان میناب همراه رئیس‌جمهور بود
🔹
انیمیشن لگویی از سخنرانی پزشکیان در مجمع عمومی سازمان ملل و یادکردن از کودکان شهید میناب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/akhbarefori/692457" target="_blank">📅 22:31 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692456">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pzdCNEKDyHLZtQBbQzNPKG_xpK4vv6JgzWNry64AMy9V3K3SQYSDRoTgGuJN-mrHOOuoE63ixfaelyyhPnHLY3LkBtUUZ_89o8kjN-L1QwtvdafcjW52JORDoTAWE-_U7M6nJcqhW-0ELsA9isZGsCkf3HuIW7MsEZqkHEZoGwXd7S2gF5yOYL8hxAYmFl8zrRJwF6oftIqIPqRFegIR1pM-rsD9Gt5sRdMteSQimq9-3_Ypt5CGM9eK1ZEyuuCHNmfLc2iC5j3Pxx7uy6SGCK6YcUXZH0DN8h8i56lW_QnfKnU1MISanKe5pSm9XSbQdK0iTxro9oMUyxuJyuf5tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
همان درخت، اما در چهار فصل
🍂
🍃
🌸
❄️
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/akhbarefori/692456" target="_blank">📅 22:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692445">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">خبرفوری
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/692445" target="_blank">📅 22:23 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692444">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X_wlBDD4EQISbKjLUMYZnaJA9F8YAVQvB7uvANCa29WgIP6Xq15BNjP4QutPgc32PNY-ACVtliyhMeMiUUkn6S83FR5OPckOHcmnLFH-onPGWxV4jMqb9MxZgmmGhixPVNea9cbe3p2Qy2qCzRmqesrc9aduW80bhOIFb8Hn5BHp6R-ucUtXwLl3htC-Z3dZMB3PWleqgVlggPbtaMMHbZRj5KlOPoi9yS5CYGPujbZa5faCfm8QYiMraOVMd3tKW4_0bJIeyECBo-8uv5V5dH_2wbc9T5s6ZgGU8lm8wC-mKPDigaQJOLSpVOCwDjFH7yuEWao1wyxa58drFxnufw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افزایش دستمزد کارگران بیش از نرخ تورم، از دستاوردهای میدری است
🔹
اکبر شوکت، عضو هیئت‌مدیره کانون کارگران ساختمانی کشور، با دفاع از عملکرد احمد میدری، وزیر تعاون، کار و رفاه اجتماعی، گفت: در دوره حضور میدری، افزایش دستمزد کارگران بالاتر از نرخ تورم انجام شد و انجمن‌های صنفی کارگران ساختمانی که در دولت قبل متروک شده بودند، احیا شدند.
🔹
او همچنین از احیای بیمه‌های قطع‌شده کارگران ساختمانی، سرعت گرفتن روند برقراری سهمیه بیمه و توقف پرونده‌سازی برای انجمن‌های صنفی خبر داد.
🔹
شوکت با اشاره به طرح استیضاح وزیر کار نیز گفت: بهتر بود پیش از طرح استیضاح، نظر نمایندگان مجامع کارگری و کانون‌های بازنشستگی در استان‌ها دریافت می‌شد.
🔹
وی همچنین حمایت وزارت کار از اجرای کالابرگ و اصلاح ساختار یارانه‌ها و دهک‌بندی‌ها را از دیگر اقدامات این وزارتخانه عنوان کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/akhbarefori/692444" target="_blank">📅 22:22 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692443">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FKe_4Fe1_zLvfOY1BFPzB0npJ76EZJwC_4MN8m8cU6n9bYGOnKZVJZD3VdSEi3EUpn3dDUYFW8TM_jFRpQasbBwoypoMKMr-0zZsS4guE6il52iHC7uqxQrwwM9Ftk7iubfhCJavb_2FwJ-mCRLqgsRj6kGFoUTeEMf4LJ-owrkd64hX4JXhRAYjwg3GShtUkANCEXNsIddlI05l_x7kflMCqvYGplSbNklT9-DtY5UOoU6DPyMAbKEQKAY9OoY6ttJ82mC3N55gEnxZQb6hC-pPrCZ65Va5Orp84ZBuqGrKs1jiNggk3i4OlW4SpSEW19NeFQbl99IfaNhqw6jovw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نفت برنت ۱۰۰ دلاری شد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/akhbarefori/692443" target="_blank">📅 22:21 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692442">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2c75dd6a1.mp4?token=hWOJIOMw4NawvwSMxQ8__vWnxyKX1-ephhRxI2sRRX7jjNspT92JbQf7DMlO-oT1UNw0udoYbEhn4zWneUhp5PVSwyxHJnTQmBMYFerbuT3ArxoYTuc0PfaTZQNzunyb1fhjNTd0zpX1jzh12rKGZeQl7f_jRpUcbperlTkf8rZvIntDUm1zBgeKnXYqeGhfOVQjRK5h35hm-hq4cK9JzLwOfgMzqGeD2hpWj9QoziA_rTgwz107RbU9Io_nMIFeZZeJi9AbF4gl420c0X7ulAyzxZI24OzAhzJOuyJopX_ZmI991wo00NbVmioHZQWAZlXV_3QOiNc2N7PEWLkjCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2c75dd6a1.mp4?token=hWOJIOMw4NawvwSMxQ8__vWnxyKX1-ephhRxI2sRRX7jjNspT92JbQf7DMlO-oT1UNw0udoYbEhn4zWneUhp5PVSwyxHJnTQmBMYFerbuT3ArxoYTuc0PfaTZQNzunyb1fhjNTd0zpX1jzh12rKGZeQl7f_jRpUcbperlTkf8rZvIntDUm1zBgeKnXYqeGhfOVQjRK5h35hm-hq4cK9JzLwOfgMzqGeD2hpWj9QoziA_rTgwz107RbU9Io_nMIFeZZeJi9AbF4gl420c0X7ulAyzxZI24OzAhzJOuyJopX_ZmI991wo00NbVmioHZQWAZlXV_3QOiNc2N7PEWLkjCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صادقانه‌ترین مصاحبه تاریخ!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/akhbarefori/692442" target="_blank">📅 22:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692441">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38cac377e0.mp4?token=ngRp4twjAJCe7YSmCvEN8HnFnI-NF1A_jkNIAR3FhthuRkt3ug54JYHfwxjSRgedtBFuRmRdMZf4S5Kaju2EH-PENTZMTSeqRZdhp4lYT-uCS5d6lJ0wJ1oOG53noCi6zxBizER7RrbBh8fNvQqJeE326Dow5dupJ2WkRQ8rpyWJlmG6BIVC8eRliBKhS7MUS_APO8Z0BErkNomEhca338LqNeGudOvkZ7n1hEj860iCr72HVN7LVOsunmJoWqj6VERPYuPagQsHts1lmPsVsb0RgaYLXfGJ-4Z9JTTI1SQsc2txSMIl4uFMPrUKclRtOHwOXKPDQBKLPQDagbhcoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38cac377e0.mp4?token=ngRp4twjAJCe7YSmCvEN8HnFnI-NF1A_jkNIAR3FhthuRkt3ug54JYHfwxjSRgedtBFuRmRdMZf4S5Kaju2EH-PENTZMTSeqRZdhp4lYT-uCS5d6lJ0wJ1oOG53noCi6zxBizER7RrbBh8fNvQqJeE326Dow5dupJ2WkRQ8rpyWJlmG6BIVC8eRliBKhS7MUS_APO8Z0BErkNomEhca338LqNeGudOvkZ7n1hEj860iCr72HVN7LVOsunmJoWqj6VERPYuPagQsHts1lmPsVsb0RgaYLXfGJ-4Z9JTTI1SQsc2txSMIl4uFMPrUKclRtOHwOXKPDQBKLPQDagbhcoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان کتاب «کمک‌های آمریکا به مردم ایران» را به رئیس‌جمهور سوئیس هدیه داد
🔹
در این کتاب جنایات آمریکا علیه مردم ایران، تحریم‌ها، حملات نظامی و ترور دانشمندان و فرماندهان ایرانی تشریح شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/692441" target="_blank">📅 22:03 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692440">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
انجام
انفجار کنترل شده مهمات جنگی در جاسک، فردا از ساعت ۸ صبح تا ۱۲ ظهر در محدوده شهر
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/692440" target="_blank">📅 22:02 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692439">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GtTfSI_T4gvdnRLKzUuSBV0O0jUsNs8x_NRPsdH_8rkk0-0Ux3bdKuIgWREl0x29kcQAJ6IJIcWU2T-h1zDMpW9mH05X3MD9UBYCSZiUk5rJKY9WEY16qHGtAD8i0uYAMhY2NfYuElydVOBJ2qI6TBTT2_4eKeMyc9xCAg8a96QbEGT6Jgv-z_xxnHMljHGnXzzOlDX5KaQwNb0-rOtaJygWMw9gnjssN5VhfdvTwQqnkTEZuQdUv_CrVKdrXazuZza11Qm2MHHmEPDA0JJxVBzTgpAES0WwK5mnb5wkpaA3u5hRyvMtTqpPC-3U0xPgluoCbaOd8SGAM6tY7Xlm3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وقتی طراحی لویی ویتون، حال‌وهوای «شب‌های برره» را تداعی می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/692439" target="_blank">📅 22:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692438">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96795c03d9.mp4?token=gvLbVTFp2dTU0auI8qxddv5PLaLWFGKiwFoDfpv3PhqdHfUtgB95nvjGB1GnyP01dJW0QBZHz9uakF-o_0ryrPlevp5UyKMuRh8gcc7UqvbN6XCdVopteWtPWe-jGbTu2zTc-ZZsNZkQk8P_ovp1nwQ5OlS6HXiqMed-OGa5ZBbfdzbVF-BtxwXijmv_NGklhTuIHTFlrLOHswaZZFoJJiingNbBFNvjO25obr9LxmfmZuKqaULGjZcoQ4NEZDZpF_1N5VPwr9jpu5LrAbbr7MxeS_BTwVHxlxqCQKULRWAB9ACi-xe47ltSKL-K5tsPN01y5ezOzpPACpPbj1etXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96795c03d9.mp4?token=gvLbVTFp2dTU0auI8qxddv5PLaLWFGKiwFoDfpv3PhqdHfUtgB95nvjGB1GnyP01dJW0QBZHz9uakF-o_0ryrPlevp5UyKMuRh8gcc7UqvbN6XCdVopteWtPWe-jGbTu2zTc-ZZsNZkQk8P_ovp1nwQ5OlS6HXiqMed-OGa5ZBbfdzbVF-BtxwXijmv_NGklhTuIHTFlrLOHswaZZFoJJiingNbBFNvjO25obr9LxmfmZuKqaULGjZcoQ4NEZDZpF_1N5VPwr9jpu5LrAbbr7MxeS_BTwVHxlxqCQKULRWAB9ACi-xe47ltSKL-K5tsPN01y5ezOzpPACpPbj1etXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه افتتاح اولین پایگاه آموزش نظامی یگان‌های مردمی جانفدا با شلیک حجت الاسلام طائب؛ فرمانده بسیج
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/692438" target="_blank">📅 21:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692437">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e39ffd5743.mp4?token=d3jkmakshT2R6KCGw97t_cy7NDctiCmD0hfvwJu93M0D10vgn8K-Tb26_X8EHjnqeShEBQMI9wfBUfrNII2-8-nCKtO119rofIQVlcGAXoSv5Zjeiai3mpBU8AgYAaKD6BNTb64ybKS8NrXJgB1fb2eFn16KOOrqstZzFj8mTc3FakSduy78YvW-y9U-K-OB32z9jnENVL6m7NMd9UmNM94kuwR00sgpGrFTb4nt5VoVxWe4-4TWxPz8gN8wxxbmz-qbaanGjVAtJNWkg9FBJAXh2fkZXJJBtnpWE-whSNTEAHPqCdZoaX8FFN9XQi6fZoYn1I-QwzunCXbby2b9HZn_gSVYSrl6lHJ_mXOCPDvhZYfVsppQv2Blg3A4QyMYil5AUPd42crWAUBAvRMfb0lyI2OHVcHHfQHp_NpbwOz4jeDfZLW4mXPL8iSVmlhQMdfTbqkPOH4ntzS-S-5XZlI787azV9JiL4IMvcHxpXRDjK8z1JHSKHGV0yyWxDOQZUUK-pri7OcBHMVEXmxrfPiIF-625zYAMCkxhA01ufuIWFGTasejE54yJtfo712D_AonppMYrrySBrVvNQ_2HslCsWa3JBCIJj3htT2N6jSohC6txQPQcjJuB60iYmKlxt5FK_h1I5S37du46FR8ShBuIfEahHxVhT1NVMzEa_E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e39ffd5743.mp4?token=d3jkmakshT2R6KCGw97t_cy7NDctiCmD0hfvwJu93M0D10vgn8K-Tb26_X8EHjnqeShEBQMI9wfBUfrNII2-8-nCKtO119rofIQVlcGAXoSv5Zjeiai3mpBU8AgYAaKD6BNTb64ybKS8NrXJgB1fb2eFn16KOOrqstZzFj8mTc3FakSduy78YvW-y9U-K-OB32z9jnENVL6m7NMd9UmNM94kuwR00sgpGrFTb4nt5VoVxWe4-4TWxPz8gN8wxxbmz-qbaanGjVAtJNWkg9FBJAXh2fkZXJJBtnpWE-whSNTEAHPqCdZoaX8FFN9XQi6fZoYn1I-QwzunCXbby2b9HZn_gSVYSrl6lHJ_mXOCPDvhZYfVsppQv2Blg3A4QyMYil5AUPd42crWAUBAvRMfb0lyI2OHVcHHfQHp_NpbwOz4jeDfZLW4mXPL8iSVmlhQMdfTbqkPOH4ntzS-S-5XZlI787azV9JiL4IMvcHxpXRDjK8z1JHSKHGV0yyWxDOQZUUK-pri7OcBHMVEXmxrfPiIF-625zYAMCkxhA01ufuIWFGTasejE54yJtfo712D_AonppMYrrySBrVvNQ_2HslCsWa3JBCIJj3htT2N6jSohC6txQPQcjJuB60iYmKlxt5FK_h1I5S37du46FR8ShBuIfEahHxVhT1NVMzEa_E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرز بین کانادا و آمریکا
🔹
یک نفر می‌تواند همزمان یک پایش را در آمریکا بگذارد، یک پایش را در کانادا.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/692437" target="_blank">📅 21:53 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692436">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
دو سیگنال مثبت از اقتصاد ایران
🔹
ارزش حقیقی تراکنش‌های شاپرک در مردادماه، با حذف اثر تورم، ۳۰۷ درصد نسبت به تیرماه و ۲.۵ درصد نسبت به مرداد پارسال افزایش یافته است.
شامخ صنعت هم با ثبت ۴۹.۸ به مرز رونق نزدیک شده است.
🔹
نکته قابل تامل اینجاست که شامخ کل اقتصاد با عدد ۴۶.۹ برای پانزدهمین ماه متوالی زیر مرز ۵۰ مانده و صنعت نیز دهمین ماه انقباض را پشت سر گذاشته است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/692436" target="_blank">📅 21:52 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692435">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
اظهارات وقیحانه زلنسکی: روسیه با تکنولوژی ایرانی نمی‌تواند ما را تسلیم کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/692435" target="_blank">📅 21:39 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692434">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3162143bf.mp4?token=LmgplDj5VV0XWqmiSSq_hBzRvWkukHa8yp_6ZwetzLljLkFlk0Wja_YVEabmsA7qVcy9im0Q7LChHk0upcuX_vIMmAEC4m3JTQX1JyxNcChoxNDy-B7Ox-ZXWoegYxWuqn_ubzog4MWbk8aDwPhn_r821CsEVuZL18BFT-RRosajOVE4IWfpySW7IvvJQ1I-ejv4GaXtKQVtAeCPG4IVf_o9D-W3hZ_XjNxDkDotxoCmBt4yT8fiGm2vDMovJsj1gVTWstIvCc7nuqEgL_OuTm__ULsOQuGRjqKX9TgoveX1OZc3IupZhN-b6v6afhBXkO8Naa8gC4mIL6O1lmET9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3162143bf.mp4?token=LmgplDj5VV0XWqmiSSq_hBzRvWkukHa8yp_6ZwetzLljLkFlk0Wja_YVEabmsA7qVcy9im0Q7LChHk0upcuX_vIMmAEC4m3JTQX1JyxNcChoxNDy-B7Ox-ZXWoegYxWuqn_ubzog4MWbk8aDwPhn_r821CsEVuZL18BFT-RRosajOVE4IWfpySW7IvvJQ1I-ejv4GaXtKQVtAeCPG4IVf_o9D-W3hZ_XjNxDkDotxoCmBt4yT8fiGm2vDMovJsj1gVTWstIvCc7nuqEgL_OuTm__ULsOQuGRjqKX9TgoveX1OZc3IupZhN-b6v6afhBXkO8Naa8gC4mIL6O1lmET9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سهراب احمری، ستون‌نویس سابق وال استریت ژورنال: در آینده، دیگر هیچ دولتی در آمریکا، نه جمهوریخواه نه دموکرات، به جنگ ایران نخواهد آمد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/692434" target="_blank">📅 21:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692433">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e40853421.mp4?token=fdUYtAhNMPipVUcINGeIfhlw5C80Za8yAFhDPCJDm--ErEBLvPh1aoWFBpJeJtlQuwbSfRZKjqdPLBHR11kMOXzZ-VmRG0iz3LmnZzAh7F_w9KQuHkN_m6Z09GqmXRaPP1KsvsNr8kQCU_vZ21hGJMbSvQLu2BMpUD4t-Rfk2ioNnCaX7MQTVYb0xCvVeLwi0ogeuMlxw1I3BAt-hFZj5lGQMn9iQmDD0zKo1oiFHYjq-XsA7o_jUUg4EtQBD4u19fPHbG3puSMUNxMu6Uhspl_kvJitPoHLAsxik77g75u29wyYp-PK6CL1YA531KZLu-1RPVB8w1jP7QtsoWutvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e40853421.mp4?token=fdUYtAhNMPipVUcINGeIfhlw5C80Za8yAFhDPCJDm--ErEBLvPh1aoWFBpJeJtlQuwbSfRZKjqdPLBHR11kMOXzZ-VmRG0iz3LmnZzAh7F_w9KQuHkN_m6Z09GqmXRaPP1KsvsNr8kQCU_vZ21hGJMbSvQLu2BMpUD4t-Rfk2ioNnCaX7MQTVYb0xCvVeLwi0ogeuMlxw1I3BAt-hFZj5lGQMn9iQmDD0zKo1oiFHYjq-XsA7o_jUUg4EtQBD4u19fPHbG3puSMUNxMu6Uhspl_kvJitPoHLAsxik77g75u29wyYp-PK6CL1YA531KZLu-1RPVB8w1jP7QtsoWutvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خداداد عزیزی پس از حواشی او در پی فحاشی به امید عالیشاه، با حضور در یک مدرسه در مشهد، زنگ آغاز سال تحصیلی را به صدا درآورد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/692433" target="_blank">📅 21:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692432">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
انعقاد یک توافقِ مطلوب ایران با دولت فعلی آمریکا، یک رویا بیشتر نیست
حسین مهدی‌تبار، پژوهشگر روابط بین‌الملل در برنامه سیاست خارجی شبکه سه:
🔹
در حالی آمریکا و ایران گفت‌وگو کردند که ترامپ کشور ما را به نابودی تهدید ‌کرد. این تنها یک رویاست که توافقی مطلوب ایران، با دولت فعلی آمریکا صورت بگیرد. ترامپ در هیچ دوره‌ای نتوانسته یک توافق پایدار با سایر کشورها داشته باشد. اگر امکان پذیر بود، کانادا می‌توانست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/692432" target="_blank">📅 21:24 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692430">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d2e663a6e.mp4?token=pPWuCS14IcHoMtM32ZfQ52vRoaInu52ScGsis6DmhwsjyzTvL2TOxv0lwgoPBNlVPEIMoCKqLkvpC66t6aUnKO8hU42EBSUexpGQz_vKiXD-bHPaNBH_ZVDL9eLyN-g2oUxxYsad2kxdavsnfVP0FZXv2gTCBvHVTSNiCmuY6HPzS_rXE9_Re1MhrMP-2a_Csuthf5NmKD3C7RmcZFCgOei6m5n5mihIo0negrgIiCEqTJQnYbsXuYJ5BzBw6u1Haa-4FG9MDUJIHIO6YdSPeW5e7FNs6zHNTTC0dWpiJPA6PUb_hG8qHf1DTvkN2CvTzrhDnuzsAdosHdo_FxmyCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d2e663a6e.mp4?token=pPWuCS14IcHoMtM32ZfQ52vRoaInu52ScGsis6DmhwsjyzTvL2TOxv0lwgoPBNlVPEIMoCKqLkvpC66t6aUnKO8hU42EBSUexpGQz_vKiXD-bHPaNBH_ZVDL9eLyN-g2oUxxYsad2kxdavsnfVP0FZXv2gTCBvHVTSNiCmuY6HPzS_rXE9_Re1MhrMP-2a_Csuthf5NmKD3C7RmcZFCgOei6m5n5mihIo0negrgIiCEqTJQnYbsXuYJ5BzBw6u1Haa-4FG9MDUJIHIO6YdSPeW5e7FNs6zHNTTC0dWpiJPA6PUb_hG8qHf1DTvkN2CvTzrhDnuzsAdosHdo_FxmyCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صورتحساب مجمع عمومی سازمان ملل در نیویورک
🔹
در هشتاد و یکمین مجمع عمومی سازمان ملل چه تعداد نفر حضور داشتند؟ هزینه این همه رفت‌وآمد، امنیت و برگزاری را چه کسی پرداخت می‌کند؟
🔹
جزئیات را در این گزارش ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/692430" target="_blank">📅 21:22 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692429">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
سهمیه دو جنگ اخیر برای کنکوری‌ها تصویب شد
دبیر شورای معین شورای‌عالی‌انقلاب فرهنگی:
🔹
سهمیه ۵ درصدی ایثارگران برای کنکوری‌های آسیب‌دیده از جنگ‌های ۱۲ و ۴۰ روزه به مدت دو سال تصویب شد؛ این سهمیه جدید نیست و در چارچوب ظرفیت‌های قانونی موجود اجرا می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/692429" target="_blank">📅 21:19 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692428">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fc1c26416.mp4?token=jID-V_yx0PnJha0_uCANqGvvQ7C43BVlXPlRwkCXZ6MwwWn16RIJcDF4xuq1ACsOrqwuhe7bRJXOUoCJkk6E4vyPKy5kT4WjqPOZ1-zly5S-ZdF5uhhH2qXAu-rO0k-381xN4fuJZmzhkKv1eJJbxxr7U52FlYCW-U28Qf55lGW3e0MVWAeZsEky0f8YWIvHeYWavhS-58VbgJ7VP2FtjUBSDpXFZWRmqfefhVHevBrOFIYJ8QlBjv4mEskUnmsDc3iNg_OCokO0WEKle8RUvLLWgs-M7ltew-3_kqS7O-X6A1_CFJ2njbKEGMoWNoKirI3i1M8J16nWt-6XouP-TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fc1c26416.mp4?token=jID-V_yx0PnJha0_uCANqGvvQ7C43BVlXPlRwkCXZ6MwwWn16RIJcDF4xuq1ACsOrqwuhe7bRJXOUoCJkk6E4vyPKy5kT4WjqPOZ1-zly5S-ZdF5uhhH2qXAu-rO0k-381xN4fuJZmzhkKv1eJJbxxr7U52FlYCW-U28Qf55lGW3e0MVWAeZsEky0f8YWIvHeYWavhS-58VbgJ7VP2FtjUBSDpXFZWRmqfefhVHevBrOFIYJ8QlBjv4mEskUnmsDc3iNg_OCokO0WEKle8RUvLLWgs-M7ltew-3_kqS7O-X6A1_CFJ2njbKEGMoWNoKirI3i1M8J16nWt-6XouP-TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز درباره ایران در سخنرانی سالانه مجمع عمومی ملل متحد: آن‌ها قلدرِ خاورمیانه بودند، اما دیگر قلدر نیستند
🔹
از همان روز نخستِ ورودم به عرصه سیاست، موضعی تزلزل‌ناپذیر داشته‌ام: هرگز اجازه نخواهم داد ایران به سلاح هسته‌ای دست یابد. #Devil…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/692428" target="_blank">📅 21:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692426">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90fbdf5753.mp4?token=LuoESw_ix7UCnCOQ7-CNVQnr1IhPahrTyXnPvQPFf5100cI2e9RspDTos2fJxxGaGgo81Bw7ORbjqv-15x3afLz3B75-Up_wFFsMMQU0R0ORYx3N7AJRbLvwHu2FLI_lw9MtFwkr3WzfcTPG7rjRveBQxR5VpG9evM-FgsqcGrH-QLdyKnYPbk-zaTwTiaUwJarqdT5CaqUaXuqtkmuaMKKXSO3oTnB0iwuh5MKcNmTzeeks5ijcS8GIrXspSz6qP_PqCh8fEu56qGJP59u63jBhHg8l2GfrIKfRXzgPMG4mY2FVT2JhYih0LFSR0O_FB_1rnpAse7sqYMfUNEZCnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90fbdf5753.mp4?token=LuoESw_ix7UCnCOQ7-CNVQnr1IhPahrTyXnPvQPFf5100cI2e9RspDTos2fJxxGaGgo81Bw7ORbjqv-15x3afLz3B75-Up_wFFsMMQU0R0ORYx3N7AJRbLvwHu2FLI_lw9MtFwkr3WzfcTPG7rjRveBQxR5VpG9evM-FgsqcGrH-QLdyKnYPbk-zaTwTiaUwJarqdT5CaqUaXuqtkmuaMKKXSO3oTnB0iwuh5MKcNmTzeeks5ijcS8GIrXspSz6qP_PqCh8fEu56qGJP59u63jBhHg8l2GfrIKfRXzgPMG4mY2FVT2JhYih0LFSR0O_FB_1rnpAse7sqYMfUNEZCnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اظهارات بی‌اساس روبیو: تصمیم‌گیری نهایی در ایران در دست جریان‌هایی است که به صادر کردن ایدئولوژی انقلاب خود باور دارند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/692426" target="_blank">📅 21:13 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692425">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h68PqXXBXwCTR8hEKceF1GW-1ElgtHo4ROJ9pEpnY-uA5c2AQ7cCvlUmdC2GrekQE7e0kd_VYVq6Eswk5f1UISpCod6C8Ajvr3bBTuzxd81fPJUyixMAKaQJLCGfyqM8yr-pmRnz_T5P8eHb7ZR7DFjEiFfBMBz2JeOo_zUyhRp6jh8x254uwOGpG3xrLCJQ6R_cdFcUi71ucfqaD1AuJiKzEBgaz6Hs4kxecv11CYJdoQ2Vl8FNy1aFREt-5u3eW9IaBm8jF7ELwx6Mlqsds8ZsB9_N2RZ5YClmAK9XakRt9E9N6Wl8T-iA9YTafX3tG4xoliuGYC0CQpU13ZYSAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پس از صبحت های دبیر شورای عالی امنیت ملی نفت مجدد صعودی شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/692425" target="_blank">📅 21:12 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692424">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VKxZ1k15EeV_7KDVlejouPFFiw8Lcj9vp14XbqUk7TxV1mdqe8g4NvJHzec-7xzmwaYjlOOXH1IOBPzD6qV-gWaBt9HZ3wEHElGoKzhBG4Z2bSN1l1WqYLld2J-mFmap5xzlmKtxkUUFql8LDHs-94cBlzCzLX8OQhL7twK9hfJEavah55O6wxFpq0qiAo3wUQ6s8E_iP_ciEJ9tZTwk_0PQ1JDV2zOTcfp7_ZC5vMyH-OzCOx4IYHU7EK8s5idOJp6cCjwSsx8e2ayVkHK7pw1bSoU4ygJLWp_vHYYsjHN0sPSIaFxhYiBskvWKzd2CwcoNrnvmH5kLirR0zTwHWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در آپدیت جدید تلگرام، میانگین زمان پاسخ‌گویی کاربران به پیام‌ها در پروفایل آن‌ها نمایش داده می‌شود؛ از چند دقیقه تا چند روز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/692424" target="_blank">📅 21:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692423">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
الجولانی: به ترامپ گفتم چرا نیوجرسی را به اسرائیل نمی‌دهید؟   رئیس‌جمهور سوریه:
🔹
در دیدار با ترامپ در کاخ سفید، پس از اظهارات او درباره تعلق بلندی‌های جولان به اسرائیل، به شوخی گفتم: شما مالک جولان نیستید که آن را ببخشید، اما مالک نیوجرسی که هستید.
🇮🇷
✊
…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/692423" target="_blank">📅 21:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692422">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
خوب نفت می‌فروشیم؟  وزیر نفت:
🔹
خداروشکر. وصولی فروش‌ها درحال انجام است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/692422" target="_blank">📅 21:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692421">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jeZxyd3KE6BTUKF4bSblRHxHbs1pukQKWqwCEyZeh7zVtUs_DF3plIccQBcC_I0wDcA0EE6anij54DIDG7OA7ldbVHoXIApV2PaJSDoeFY7YIvaECQSm-tpCPJv4WRSl8XlCmFrsItqpvIs3320Z3Y8ctjouhTxRWBRe-pZCEZFANa-mNkb_xnMcKKIlXpslqLxbwJ3YvUIV51FLHeomnEfJuKUbgi7eJQKTNfqpGSudz2GNFyDRG6db3GO6Ust10aZq05Ui4lKm6skm6B2Oe2PE13zaJVXgOMqYbtjIFztf47iqvCmbKytWDTb9HP0dB2iyTqSfdgjQKWK1v8WyLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اختصاص یکی از ساختمان‌های آبفای میناب برای استقرار و فعالیت مدرسه «شجره طیبه»
🔹
مدیرعامل شرکت مهندسی آب و فاضلاب کشور از اختصاص یکی از ساختمان‌های آب و فاضلاب شهرستان میناب برای استقرار و تداوم فعالیت مدرسه شجره طیبه در چارچوب مسئولیت اجتماعی این شرکت خبر داد.
🔹
هاشم امینی: با توجه به ضرورت آغاز فعالیت آموزشی مدرسه از ابتدای مهرماه، یکی از ساختمان‌های آب و فاضلاب شهرستان میناب برای استقرار موقت دانش‌آموزان این مدرسه در اختیار اداره آموزش و پرورش قرار گرفته است.
🔹
این اقدام در چارچوب مسئولیت اجتماعی شرکت مهندسی آب و فاضلاب کشور و با هدف کمک به تداوم فرآیند آموزشی و فراهم‌کردن محیطی مناسب و ایمن برای حضور دانش‌آموزان انجام شده است.
🔹
شرکت مهندسی آب و فاضلاب کشور توجه به مسئولیت‌های اجتماعی را از وظایف خود می‌داند و تلاش می‌کند ظرفیت‌ها و امکانات موجود را در جهت رفع نیازهای ضروری جامعه، به‌ویژه در حوزه آموزش و دانش‌آموزان به کار گیرد.
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/692421" target="_blank">📅 21:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692420">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
برقراری پروازهای ایرانی به امارات، ترکیه، چین، آذربایجان و افغانستان؛ بغداد پیشرو در تحریم پروازی ایران
🔹
داده‌های فلایت رادار نشان از آن دارد که پروازهای ایرانی به رغم تحریم‌های امریکایی به کشورهای امارات متحده عربی، ترکیه، چین، آذربایجان و افغانستان…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/692420" target="_blank">📅 20:58 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692419">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
پزشکیان در نیویورک در هتل مستقر نشده است
🔹
پزشکیان در سفر به نیویورک به‌جای هتل، در محل اقامت نماینده ایران در سازمان ملل (رزیدانس) مستقر شده است.
🔹
این اقدام با هدف کاهش هزینه‌های سفر، برای اولین‌بار توسط یکی از رؤسای‌جمهور ایران انجام شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/692419" target="_blank">📅 20:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692417">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7fbd948ad.mp4?token=bSednMXXaSUIL6kZZcE2k9xvE4dsWeuW1kgES6OlpzyUzfUCKMUY9ks4NTsl5v0H_QHNnUza2A3mOO_Flli8SUkfES5hV9jehk6jGjOhgB10Z60TsGtOWIIDwOVasOH1_GW429vVklDFUXtnXsaOocdlktd179Zi31IxYV92yHC2glwn1vuNjkY1ug9Xi-6-B7iuxPCiGaaQPZuZKIcqy5UpHdcprUyMh_OWJU2MHVH7VbmyYF0An9_WJTVXusW8Syy2y-wQbvj4jBnJhub-0S3yhHJj10eLQ7FFZxTe_RgW7_1RraaLW_hs6GT4NizUiXUsLBVgt7-8qzNXOUjchw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7fbd948ad.mp4?token=bSednMXXaSUIL6kZZcE2k9xvE4dsWeuW1kgES6OlpzyUzfUCKMUY9ks4NTsl5v0H_QHNnUza2A3mOO_Flli8SUkfES5hV9jehk6jGjOhgB10Z60TsGtOWIIDwOVasOH1_GW429vVklDFUXtnXsaOocdlktd179Zi31IxYV92yHC2glwn1vuNjkY1ug9Xi-6-B7iuxPCiGaaQPZuZKIcqy5UpHdcprUyMh_OWJU2MHVH7VbmyYF0An9_WJTVXusW8Syy2y-wQbvj4jBnJhub-0S3yhHJj10eLQ7FFZxTe_RgW7_1RraaLW_hs6GT4NizUiXUsLBVgt7-8qzNXOUjchw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرزند سفیر اسرائیل در عملیات ضدصهیونیستی مجروح شد
🔹
رسانه‌های اسرائیلی گزارش دادند فرزند سفیر اسرائیل در واشنگتن، در عملیات اخیر نزدیک رام‌الله مجروح شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/692417" target="_blank">📅 20:51 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692416">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/617c3cf0e4.mp4?token=Nv7Af1kX4HqxPcvQ-K55Zvwx9ZmpYg9DNziwZVhQApluCdXz-CKDEOjUV9oJIOPuYHy9UampQfT7oMbWwkTmWIL5zdbrm0m-0Yoi645KU_uK2GSV9XNUKBI7WDyN0RZUCNeqz2a_Xes9hI11Tjx20swE_s2Mcp7Mmsh3Kr1u42qXFZlHaA92ZR14f52OunsmaXP2vKkAWlzMuMJfvRKILekR7kkij3QWx8rSpggTeFk2gnuC4wzCtlvUl6NHDQ-31ByrJ7lH_6dgOUwIsV0QWwvsvK6oUkntR1pc9KLp3GxW7ZvNzxnin2vltxUk7KtsYGjdhuGoqjlcZx2cPeBIyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/617c3cf0e4.mp4?token=Nv7Af1kX4HqxPcvQ-K55Zvwx9ZmpYg9DNziwZVhQApluCdXz-CKDEOjUV9oJIOPuYHy9UampQfT7oMbWwkTmWIL5zdbrm0m-0Yoi645KU_uK2GSV9XNUKBI7WDyN0RZUCNeqz2a_Xes9hI11Tjx20swE_s2Mcp7Mmsh3Kr1u42qXFZlHaA92ZR14f52OunsmaXP2vKkAWlzMuMJfvRKILekR7kkij3QWx8rSpggTeFk2gnuC4wzCtlvUl6NHDQ-31ByrJ7lH_6dgOUwIsV0QWwvsvK6oUkntR1pc9KLp3GxW7ZvNzxnin2vltxUk7KtsYGjdhuGoqjlcZx2cPeBIyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور فرزند رهبر شهید انقلاب در مراسم بزرگداشت آیت‌الله شبیری زنجانی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/692416" target="_blank">📅 20:49 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692415">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vi1omo2SqTtPQmulStXdNjHwuXrUWC7ML-q5WEH9Uh8bHFAX4h1dnR8xvEs5-MblcX3VbHRC17iBb01otLwNO2oz2pyDOFRvRm69zB9cBWGrMBud6dA-Ef2_eotCi70V1s7J_RRB8NV1CuPzZ_34UlWi6wNvOWPfqGaBbh3jvJvC7Ag_JdHp5jLuwO5LD_CtlNMuc0u6GERiuc-H9w7Gt-r-RBw8RZd_AS9EjOUAeH7FrH3FSlfr2ntr87pvu5eZCye0xhzeOxMNfOcFwUdVZN_-sSRYNNEnvmiCN4bfff8PbJow5sv2VfoWdTeAprQlO_pOPUkw_BOEA2M2U9huRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هلاکت سه تروریست در سراوان
🔹
معاون امنیتی و انتظامی استاندار سیستان‌ و بلوچستان از درگیری و هلاکت سه نفر از اعضای تیم تروریستی در درگیری آنها با نیروهای امنیتی و نظامی در شهرستان سراوان خبر داد.  #اخبار_سیستان_و_بلوچستان در فضای مجازی
👇
@akhbar_sob</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/692415" target="_blank">📅 20:44 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692414">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ga_bGDJZanptcVLUCVc-deivpP70hzJq9rtfD9km5iiBQoHC1xGDkaWSauZ1OMSbN8G5adLWECjvdKt1B2baC2-f2_MEO9VuGx_nYf40Yd0aIpuCL5XFPkK9BZBdhaIdy-szs9QYLdYuK8zufoVrAGDMIh4U8WbwpgbvXP6fhzacB6NvVfgiP-_v-gGmSeopsrJ7iyS0oZ6Us-lId1t6JPrglcQlMVH_Pl5NeSQ4vhlz4LyQWiE_F7ME4BxEW6wO-gb6gpn1amV9dZYlaa9kiJp0FHjRQFzKXcZn1KTcrJ72aPl1pTZY3xusqCgCG78TOqUkbwkMF4V0YL0S9gjubw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری | جشن فرشتگان
🔹
همراهان گرامی خبرفوری، شما می‌توانید با ضبط یک ویدیوی کوتاه از دانش‌آموزان خود با لباس فرم مدرسه، در این پویش شرکت کنید .
🔸
از کودکان خود بخواهید این جمله را بیان کنند: «کودکان شهید میناب؛ ما راهتان را ادامه می‌دهیم.»
🔸
ویدئو های خود را به آیدی زیر ارسال کنید
👇
#جشن_فرشتگان
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/akhbarefori/692414" target="_blank">📅 20:42 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692412">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0orxN9TgdmzDSFtRsNupzaJh1wWPpN0_lqRTD9EKeclLwumuNXW90zkHosUEzxpcVGOk_9gmpqkgX4oN4pCkMA7K7RJYLpC2OpSrD8oNUe-JBoX5_M1QQRcf2LP_eUFL7yrDOkBgkkErjoTS6ym8LVLgQABx5JfJ-_5iNHUx2EaksZjyYe2-eZ0YH4S9PmrPI5IYo7sKZw0rOekZs4V0YfHLSTkpeh0lLiquG0zfFUGSbAFQrYsgrFwAFGurSpzwX7FLLNPW7iqw1lqzUgjiLO7d4Ui5--mPlMynQfTo0lXNZIq_vh8k2EYY2wpThn-61yNWWOURBl01ffw4ItAQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حضور دختر و داماد پزشکیان در مجمع سازمان ملل در نیویورک
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/692412" target="_blank">📅 20:40 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692411">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
پولیتیکو: آمریکا در حال آماده‌سازی طرحی برای ممنوعیت صادرات گازوئیل به مدت ۹۰ روز است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/692411" target="_blank">📅 20:37 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692410">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/418cebf273.mp4?token=uqHR9-ZZOQC_sRuwzRjfitoAe7JECoMkMYaN6qs1vZHTib2wIQ7pxZJN1gASSNUlPtnBCmS1dV25ZfhPFFq_L7XKB4WLJ7t_5M8uw3y_d5fk1xG9l6_P6mVosjTn2MT58soimshrnv8rxSekT45-SV1RkMXqCRuJXyFEeM02zPdvqM6uD0LtZavfz-qypiKTgq8NHOpf2hpkzdFjO0wXvwsg2wHC08gNfuAPLu1CC8Z-He7rWhyXDIDa7dJc4KmM6yknMkwZfI4i91uDPClmA0pWTPL2I3oD9QLMGf1cvMjoMX5dFgQRhHZBJZMuUfHENUqfi5w_2VOnJP8_BZsA0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/418cebf273.mp4?token=uqHR9-ZZOQC_sRuwzRjfitoAe7JECoMkMYaN6qs1vZHTib2wIQ7pxZJN1gASSNUlPtnBCmS1dV25ZfhPFFq_L7XKB4WLJ7t_5M8uw3y_d5fk1xG9l6_P6mVosjTn2MT58soimshrnv8rxSekT45-SV1RkMXqCRuJXyFEeM02zPdvqM6uD0LtZavfz-qypiKTgq8NHOpf2hpkzdFjO0wXvwsg2wHC08gNfuAPLu1CC8Z-He7rWhyXDIDa7dJc4KmM6yknMkwZfI4i91uDPClmA0pWTPL2I3oD9QLMGf1cvMjoMX5dFgQRhHZBJZMuUfHENUqfi5w_2VOnJP8_BZsA0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روبیو مدعی شد: عربستان شریک راهبردی آمریکاست و به تعهدات دفاعی خود پایبند می‌مانیم!
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/692410" target="_blank">📅 20:37 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692409">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
ادعای بی اساس روبیو: نتیجه انتخابات میان دوره ای آمریکا بر خلاف تصور ایرانی ها تغییری در اختیارات ترامپ ندارد!
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/692409" target="_blank">📅 20:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692408">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58f3a12635.mp4?token=io5xLV4SzfJSIzMJDpHyW9Y1eVQY-noLJ80U3GCBjPHDpsW8p0rZrx7TEGcAoqvlDrYv812Y1qqEi3qkV4EiIPYV7P2iFSM_ctz961dB7LSGR6N_dExG1-tMmBPwdv7jE4-XhnPVVGm7Vd0hBHNgqWbQdv2cgFb7YftC739LQwlerUJAVUNGpxzYQcSnDhyGOd3QeEXj6oUB-HRPNcEydcwUurebcZZM3hXSAAtA8h6ZPoXx8pRHq_iC2avwNnC9JKm87D99KP_yNzRf5oZLdcfYU7jks6Z51JrF-3v8vow3Zg18dqAN2oRLpGcm4Lh_cyFufzBkW2TjypR6IpN_MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58f3a12635.mp4?token=io5xLV4SzfJSIzMJDpHyW9Y1eVQY-noLJ80U3GCBjPHDpsW8p0rZrx7TEGcAoqvlDrYv812Y1qqEi3qkV4EiIPYV7P2iFSM_ctz961dB7LSGR6N_dExG1-tMmBPwdv7jE4-XhnPVVGm7Vd0hBHNgqWbQdv2cgFb7YftC739LQwlerUJAVUNGpxzYQcSnDhyGOd3QeEXj6oUB-HRPNcEydcwUurebcZZM3hXSAAtA8h6ZPoXx8pRHq_iC2avwNnC9JKm87D99KP_yNzRf5oZLdcfYU7jks6Z51JrF-3v8vow3Zg18dqAN2oRLpGcm4Lh_cyFufzBkW2TjypR6IpN_MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راهکار جالب و ساده برای اینکه هوش مصنوعی چهره تو تغییر نده
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/692408" target="_blank">📅 20:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692407">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
کانادا ۵ مقام و نهاد ایرانی را تحریم کرد
🔹
وزارت امورخارجه کانادا بدون ارائه جزئیات مشخص، اعلام کرد تحریم‌های جدیدی علیه ۵ مقام ارشد امنیتی و ۵ نهاد دولتی ایران اعمال کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/692407" target="_blank">📅 20:29 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692406">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
ادعای نتانیاهو جنایتکار: امشب راهی نیویورک می‌شوم تا با دروغ های وحشتناکی که علیه ما گفته شده مقابله کنم/ضمن اینکه چند سوپرایز هم در راه است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/692406" target="_blank">📅 20:26 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692405">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2d4fa3068.mp4?token=fbZuQZEoa_YMJdr7pQq0atUEkPvKA1UqZsrNe7413T5qRXHt42bKRaT1ia_G5T7onpsLGgHWeWPGXflUTQRUrFb4fe2cwGkKuL8HDsbLJouHkivYxXw3zBcrICcBfql-6ttsSEG1nUjig0_mSyolDc6edcA76jy4f8wDHtPPrjH-oIUzbKRhXzZ_rGdm4v4zE-cYVhFxC-Y6PTiPm3GlTnZEOQP09OEK5TvrlY3WItKC76G2b6zopHhmOaGPsLQqhgt1ZXAiE6axn8q_KXzdqNhC8b_clh7V4smCwzRZhbTbJkJZLeB5Tm3Tj1QeNcO_5W-SFIp3-ZZCWDHOXl1VPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2d4fa3068.mp4?token=fbZuQZEoa_YMJdr7pQq0atUEkPvKA1UqZsrNe7413T5qRXHt42bKRaT1ia_G5T7onpsLGgHWeWPGXflUTQRUrFb4fe2cwGkKuL8HDsbLJouHkivYxXw3zBcrICcBfql-6ttsSEG1nUjig0_mSyolDc6edcA76jy4f8wDHtPPrjH-oIUzbKRhXzZ_rGdm4v4zE-cYVhFxC-Y6PTiPm3GlTnZEOQP09OEK5TvrlY3WItKC76G2b6zopHhmOaGPsLQqhgt1ZXAiE6axn8q_KXzdqNhC8b_clh7V4smCwzRZhbTbJkJZLeB5Tm3Tj1QeNcO_5W-SFIp3-ZZCWDHOXl1VPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای
نتانیاهو جنایتکار: امشب راهی نیویورک می‌شوم تا با دروغ های وحشتناکی که علیه ما گفته شده مقابله کنم/ضمن اینکه چند سوپرایز هم در راه است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/692405" target="_blank">📅 20:21 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692404">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2389f63da.mp4?token=o7WVd6tXx6kmh9o0xfE3glHgZY3694SPirEcJj8fyZGMMASQQIO-F9STpx0CjlgpSU3HVDgqzICjeRXHvqPR9XHJxEsMtS_dIVaIGJQTSax-uTwHvaJXa86jaVkpQALu6WmP68t4HdculwWXzTVhc1p3X01gKLAZF61TUgdZRK1uZmXeiqnVPV7rLRM2nW8QOmVHGH6uxjJYbcA2NSegT9X10_qPDBx-Nwn--7-xKptVBZxR4waRxGintCYHc4UQzkqBLGDS5TNxvaXcsfJ_BUHmDcB1nHBcJ9-t3ZOFf5tD8Ow0b9reD4BapSN6awu-Hnj-d4jiHtXJfTwy5_cb9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2389f63da.mp4?token=o7WVd6tXx6kmh9o0xfE3glHgZY3694SPirEcJj8fyZGMMASQQIO-F9STpx0CjlgpSU3HVDgqzICjeRXHvqPR9XHJxEsMtS_dIVaIGJQTSax-uTwHvaJXa86jaVkpQALu6WmP68t4HdculwWXzTVhc1p3X01gKLAZF61TUgdZRK1uZmXeiqnVPV7rLRM2nW8QOmVHGH6uxjJYbcA2NSegT9X10_qPDBx-Nwn--7-xKptVBZxR4waRxGintCYHc4UQzkqBLGDS5TNxvaXcsfJ_BUHmDcB1nHBcJ9-t3ZOFf5tD8Ow0b9reD4BapSN6awu-Hnj-d4jiHtXJfTwy5_cb9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوب نفت می‌فروشیم؟
وزیر نفت:
🔹
خداروشکر. وصولی فروش‌ها درحال انجام است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/692404" target="_blank">📅 20:21 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692403">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/847dcb1767.mp4?token=EIkbERsoWsGUB4-OCvKy8Tch9h5teDvtpQ6AvCBqIMEBqGzxz_6E5Q8A8lqHaUGJG3TBMauZG1iEtviPcncouVgRu6eqkyhAhudZoyo3eXyHhR45qB3fSaYy0ph1-02rHDa1FAbCw18EUWdFMgRkGZtzpDnw2FxEjoVkZYTiITkOERL-68ipuN2WjfjwRzySJl-v-TFBuocI2u8No3qMk7k6kCximR06Mm-2dZGrr2Z2DtvlXyedVfunyJSuGJfOb918pAhZM6us2lwOZmUt_GX9iitbT3EHJ68XXJNXqSk85wBkYP3cPHDv27JWpnUTvghdqcQn9_eDuB8f_HeWXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/847dcb1767.mp4?token=EIkbERsoWsGUB4-OCvKy8Tch9h5teDvtpQ6AvCBqIMEBqGzxz_6E5Q8A8lqHaUGJG3TBMauZG1iEtviPcncouVgRu6eqkyhAhudZoyo3eXyHhR45qB3fSaYy0ph1-02rHDa1FAbCw18EUWdFMgRkGZtzpDnw2FxEjoVkZYTiITkOERL-68ipuN2WjfjwRzySJl-v-TFBuocI2u8No3qMk7k6kCximR06Mm-2dZGrr2Z2DtvlXyedVfunyJSuGJfOb918pAhZM6us2lwOZmUt_GX9iitbT3EHJ68XXJNXqSk85wBkYP3cPHDv27JWpnUTvghdqcQn9_eDuB8f_HeWXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مارکو روبیو: از ولادیمیر پوتین برای حضور در اجلاس G20 در میامی دعوت کرده‌ایم و امیدواریم این دعوت را بپذیرد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/692403" target="_blank">📅 20:20 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692402">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
معاون اول رئیس‌جمهور: امیدواریم در روزها یا هفته‌های آینده در زمینه افزایش مبلغ کالابرگ به تکلیف خود عمل کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/692402" target="_blank">📅 20:19 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692401">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
ادعای
ناتو: بدون اروپا جنگ آمریکا علیه ایران غیرممکن بود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/692401" target="_blank">📅 20:18 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692400">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
رئیس‌جمهور جایزه بگیر آرژانتین: برای جلب رضایت نتانیاهو ایران را محکوم می‌کنم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/692400" target="_blank">📅 20:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692399">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HUMRLpCqwwUUAwo8f5aMi-kOWim-tkeCwFmcf2aVlHV2140GELN-QqizKaducJBrE-m478iSohgesA1fjSXzeH7qjq5RDGqVuPsAwbaxoHb5Jqx5b2C2JZjCIUfnCRzs_IBos6GTGNAc6uhtY6qzE6TuJRz-nZ5GqSCxJ6myxFHtZSkszFVDKDpDjd30ODX7JH4Xf2t8qFA-QOdVG_J4c32XbR6F0Kh7z3vtCQBIl35ziej2AeiHo_dUFjNdxhdT40iCND6KyNIE3EsWUCMucRL1u-D403QA3k1DBzG5L788Y5ptdHoDtlBeJ92GyFK3eksvnoObQr1w65r0pu712g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دیدار احمد الشرع در نیویورک با ولودیمیر زلنسکی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/692399" target="_blank">📅 20:15 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692398">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
مارکو روبیو: از ولادیمیر پوتین برای حضور در اجلاس G20 در میامی دعوت کرده‌ایم و امیدواریم این دعوت را بپذیرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/692398" target="_blank">📅 20:12 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692397">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78297f7d8b.mp4?token=Xyz0736ngLgyJuK7b3D4q2eR1Hh1y-jh7lBWm0etf6AZXfLvSqspKhwm3dYcFypioNgVEimWPRP-usjtBNUhQ_EOsShRIScXeS6EFK8oosPWAGD7TCkxyISNRaWsVEgIJp8-TGBAy6LYcK1lZzSWBvxoXCXijIFiyeKXqa0oBletQ6tMZiT_MxrnqjpXpDJB8DU_iNifvUJLMl4m52ENlzJ4gj8sgMMUK52grwHyYJ1wueEsCqObfQGCOiyZye7Rq-i42wcZqYTqZg-USwgJ5a5S76uNe_kUhVQ3Q0Kt05UmpknYt9GcL-LGX2UjwkEF3mIr8LGituv8ts6WgN0ZFLXBBwPrjymxW7X9cqARmWSlrNVsbncQQ1NffDkXVV7e6oZzEiqPV8YIcCyFvENeuRShonPoVZK2qKSWCjT5oru6Na4xvrwuGFssRshOHhfTeDhmb2Q9czK7uRXzOLZBO1in2qidJJKV9GnZrLVGhjQdJbbxUpMHA_VPj-wlZa4cBZXm6_WUkxppnPkxsK8EBznTZUhS5nq5Hl70JeXxNsoPfwIjATwtjQAEPtLecYOM5roSPcknsICkqzcD5H4lcMGgRa8Mo-cIDLeR4lqsIBFN2vVOn-kYgOyjMw3aY1QGmBebtn8yMJfiNcd-z-gZGS9_EgTvhMoqIi_A2b3CtJE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78297f7d8b.mp4?token=Xyz0736ngLgyJuK7b3D4q2eR1Hh1y-jh7lBWm0etf6AZXfLvSqspKhwm3dYcFypioNgVEimWPRP-usjtBNUhQ_EOsShRIScXeS6EFK8oosPWAGD7TCkxyISNRaWsVEgIJp8-TGBAy6LYcK1lZzSWBvxoXCXijIFiyeKXqa0oBletQ6tMZiT_MxrnqjpXpDJB8DU_iNifvUJLMl4m52ENlzJ4gj8sgMMUK52grwHyYJ1wueEsCqObfQGCOiyZye7Rq-i42wcZqYTqZg-USwgJ5a5S76uNe_kUhVQ3Q0Kt05UmpknYt9GcL-LGX2UjwkEF3mIr8LGituv8ts6WgN0ZFLXBBwPrjymxW7X9cqARmWSlrNVsbncQQ1NffDkXVV7e6oZzEiqPV8YIcCyFvENeuRShonPoVZK2qKSWCjT5oru6Na4xvrwuGFssRshOHhfTeDhmb2Q9czK7uRXzOLZBO1in2qidJJKV9GnZrLVGhjQdJbbxUpMHA_VPj-wlZa4cBZXm6_WUkxppnPkxsK8EBznTZUhS5nq5Hl70JeXxNsoPfwIjATwtjQAEPtLecYOM5roSPcknsICkqzcD5H4lcMGgRa8Mo-cIDLeR4lqsIBFN2vVOn-kYgOyjMw3aY1QGmBebtn8yMJfiNcd-z-gZGS9_EgTvhMoqIi_A2b3CtJE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رهبر شهید انقلاب: قدرت مادی آمریکا بر آنچه انقلاب اسلامی دارد، کارگر نیست
۱۳۷۴/۱۱/۲۰
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/692397" target="_blank">📅 20:12 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692395">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1b9BlfN8vEc2VvHsr7Eqsr9B8cbverCoxOBi42F5FdClqWCY6KJ2AUArmxBYbiDDL4188wZrqeu-gH4zDK3zUo9PrEQHkgaLArrRKp9tcfWdlueCwUiNNsON3uv5k2s_v-p81ZQj90laOqjnjAAijIK2yGMj-vr6R7OnAX5N0VBmtLtvXinv1vuXUQumyK552VZ4EBgtOwcH7jEJU-8SKfl4tDYO-E9jDog7bn957nFxtaKeougyrKocjqGpPph3f5IvR5ZgElC54569w-67SXjgylFk9tuACYfZvR0jENIVx2jpfqAB6OLArkWHr1Etw4lGcNFWie-Z-sDoSbKgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عکس‌هایی که پزشکیان به دنیا نشان داد چه بود؟
🔹
رئیس‌جمهور کشورمان طی ایراد سخنرانی خود در هشتاد و یکمین مجمع عمومی سازمان ملل، عکس‌هایی از رهبر شهید انقلاب، مدرسه دخترانه شجره طیبه میناب و ورزشگاه لامرد را به عنوان سند جنایت مدعیان حقوق بشر به دنیا نشان…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/692395" target="_blank">📅 20:08 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692394">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
ایراد شورای نگهبان به طرح مهریه
🔹
صرف نظارت الکترونیکی بر بدهکاران کافی نیست و ممکن است فرد توان پرداخت داشته باشد اما از پرداخت خودداری کند.
🔹
سقف ۱۴ سکه برای ضمانت اجرای وصول مهریه ایراد شرعی دارد و باید توان واقعی پرداخت بدهکار ملاک باشد.
🔹
ضوابط نظارت…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/692394" target="_blank">📅 20:07 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692393">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fL0Hr8YvhIZmJftxAtJKVYyBP8_q1AeGGV1L5OzcuT-SSHyYl7ZuMX-sHZSKD_nDZLmpW71yhw-Dc8e0zH3uAZalkRDLfw4W9lyrvVWYl45SxpydzUmY3RCEM2eVhTQbzLU5LvdAtLQczBJpeSYIl3lEgIHVtOlMI_8fuWHs7vxddW5lfh1fBoPza83CNsfxuBHkJCGUhPJnnBkf0taOR5mEUIWHhZ3fzQd-Sgc5lfF_fsR97VPR4GyeqBkFLM-NIOwcnLMX3sFy7cGwKlM0Iy-KGbBb_1BU64LZImY2W4AVb4vfd7RFRJqpCDzIDbHsRcyWYjmm2wxYmwhZ806KlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سرلشکر رضایی: تا قبل از بازشدن تنگه هرمز هفت شرط ایران باید عملی شود
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/692393" target="_blank">📅 20:06 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692392">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ad434211e.mp4?token=Wruhk6Mtr5TGdnHrAMohb5vl7in4bTwAPCwm_1Qo3BpfFXOiiR6DIzkniM3WxVxMrB9q1i16NKrjKajj1NERAlWIPhWwyqXhf1e9nLzWzSfuktgTtKiGrUSFcYE_0CQauMHHgQgOjeoR0xoSf10zk-cM_gUW_inhEnHvNc6o9zn7u8Tbm7Ac6P8wCpm2lfrBnHVOqFXbH-m9bPCLHplQv_XEBJkEXyHwTCJSkAo9PmeUo7M9eHqxEP3Gsduuy9aVd_9f1DpHzvhdoxXhaWYjl7Bpepi2Ouzv88yqc51bbpQdKgntIpFF3cv1gxkAKX8sneHDnS5DjQVAcTc3L9dn2TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ad434211e.mp4?token=Wruhk6Mtr5TGdnHrAMohb5vl7in4bTwAPCwm_1Qo3BpfFXOiiR6DIzkniM3WxVxMrB9q1i16NKrjKajj1NERAlWIPhWwyqXhf1e9nLzWzSfuktgTtKiGrUSFcYE_0CQauMHHgQgOjeoR0xoSf10zk-cM_gUW_inhEnHvNc6o9zn7u8Tbm7Ac6P8wCpm2lfrBnHVOqFXbH-m9bPCLHplQv_XEBJkEXyHwTCJSkAo9PmeUo7M9eHqxEP3Gsduuy9aVd_9f1DpHzvhdoxXhaWYjl7Bpepi2Ouzv88yqc51bbpQdKgntIpFF3cv1gxkAKX8sneHDnS5DjQVAcTc3L9dn2TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این اشتباه‌های کوچیک باعث میشن مواد غذایی‌ات زودتر خراب بشن! #ترفند_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/692392" target="_blank">📅 20:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692391">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m8elSwHKV6CQsC4rIG8OFHQwFzlZ3Kf9fTxsIa44xQopwF4ea2MQUTiDWCQz9D4k0QGIkJne-if5AQAXpxujDKlUXh0FvucXHo-aGLpzybrxerJgYpLVExNiCAVImp2Aj5_MvugJeHLU_4pK8no4EwbxkP48xy1qA9mMYIO9XTghtFGTwHDBM5EgwWcNGqLFF8rOwJGwKr_0VC4JXO70ENVGCp5se_5HgirUlMm-KtZ3_oV6Erxc0DisfTG6rKnG4aGXtM6EDbdE3bH-txajYOiNhX9dnsXkwobCt7vcBMyxeDbMblCtiTyi0LvowWRygsrxPLYlmIxpBAyqAG6OTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">THEIR STYLE, THEIR STORY.
هر نسلی، استایل خودش را دارد ...
40% OFF
GERAD Kids & Juniors
تخفیف طلایی | روزهای پایانی
Instagram.com/geradofficial</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/692391" target="_blank">📅 20:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692390">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‼️
اوکراین: با آتش‌بس فوری و بدون قید و شرط موافقت کردیم
🔹
رسانه‌های اوکراینی به نقل از وزیر امور خارجه این کشور اعلام کردند که کی‌یف با برقراری آتش‌بس کامل، فوری و بدون قید و شرط موافقت کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/692390" target="_blank">📅 19:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692389">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
چین پردازش هوش مصنوعی را به مدار زمین برد
🔹
چین با ماهواره Supercomputing-1، برای نخستین‌بار پردازش هوش مصنوعی را در مدار زمین آزمایش کرده است؛ این ماهواره می‌تواند تصاویر رصدی را مستقیماً در فضا تحلیل کند و زمان پردازش داده‌ها را از چند ساعت به چند دقیقه کاهش دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/692389" target="_blank">📅 19:45 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692388">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb348fe895.mp4?token=th_Obmipx85pfML0hbJpDy1lcuhwFjBvAGlHcZpKZe2lnY852Kc7qVG8HZsQiNjrD-IGSyjdElvyaFn2t7FBVUrblXSHVtUarixIoUrrxdWK5K1UwMkN_CXxKa4AfVYSeOh7P9k4gGA4P6ECe5QyU5oWlmPbM6YUd6PZ-6cqXk40Bc7q3Ikz3rzoM-9WhyKkQVGQDwP51W1gs3JeR2USVxoBh1cLYBKOMMW2bjSDokhSMqb_VF7m3EgVFV7k9sMzRD0ZSPcpY-K7VIDaOD8G3zk6YrrhKg4twiWtwiYpuwKvXd-mGG1mj6JodTY7v_3Urt-DHrPnlcLTxnldlAiFLx_4cnNAvwkCqS6PsESYv0-F50Q70bOCcAtAJ_IAVCpdTA3cxjw2QooE8ZNKlxUk_H8gLy4c13zWMorBme7KbsG0DCJsnOQuPz6gWkjsWypnxc-mqvn81VVLVVZnOTTkoA85QQG1Hl0lFnkH5a5zFEYYipevNdbE2LpQOqmJSKGTxyCOZSt_fE81IZ8pBiCoBNo8mcKaNjoElPH1WHD97Dd9oWcHAOrX7Kj72Jhf0NBij4PJdASAuNOWoRAB6WGlsQdaGGyuJ5CIO_g2SYtDD4TZ4Gq_melSttQpC8gWbnDzwOREm3hFyzbU0u5BBZfqW0wMMaFUkTHaV9D22cWPfRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb348fe895.mp4?token=th_Obmipx85pfML0hbJpDy1lcuhwFjBvAGlHcZpKZe2lnY852Kc7qVG8HZsQiNjrD-IGSyjdElvyaFn2t7FBVUrblXSHVtUarixIoUrrxdWK5K1UwMkN_CXxKa4AfVYSeOh7P9k4gGA4P6ECe5QyU5oWlmPbM6YUd6PZ-6cqXk40Bc7q3Ikz3rzoM-9WhyKkQVGQDwP51W1gs3JeR2USVxoBh1cLYBKOMMW2bjSDokhSMqb_VF7m3EgVFV7k9sMzRD0ZSPcpY-K7VIDaOD8G3zk6YrrhKg4twiWtwiYpuwKvXd-mGG1mj6JodTY7v_3Urt-DHrPnlcLTxnldlAiFLx_4cnNAvwkCqS6PsESYv0-F50Q70bOCcAtAJ_IAVCpdTA3cxjw2QooE8ZNKlxUk_H8gLy4c13zWMorBme7KbsG0DCJsnOQuPz6gWkjsWypnxc-mqvn81VVLVVZnOTTkoA85QQG1Hl0lFnkH5a5zFEYYipevNdbE2LpQOqmJSKGTxyCOZSt_fE81IZ8pBiCoBNo8mcKaNjoElPH1WHD97Dd9oWcHAOrX7Kj72Jhf0NBij4PJdASAuNOWoRAB6WGlsQdaGGyuJ5CIO_g2SYtDD4TZ4Gq_melSttQpC8gWbnDzwOREm3hFyzbU0u5BBZfqW0wMMaFUkTHaV9D22cWPfRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رشیدی‌کوچی، نماینده سابق مجلس: ۱۷ میلیارد دلار ارز برای تولید خودرو هزینه شد/ با همین پول می‌شد حدود یک میلیون خودرو وارد کرد
جلال رشیدی کوچی، نماینده سابق مجلس:
🔹
انحصار خودروی ما اقتصادی است.
🔹
به جرأت میگویم یک چهارم و حتی یک سوم بودجه مملکت را صنعت خودرو دارد از بین می برد.
🔹
ادعای درستی مطرح شد مبنی بر اینکه دوسال گذشته چند نفر از مونتاژکارها حدود ۱۷ میلیارد دلار از دولت گرفتند تا ۲۵۰ هزار ماشین تولید کنند.
🔹
اگر دولت این مبلغ را ماشین ۱۷ هزار دلاری وارد میکرد، تعداد آن یک میلیون ماشین می‌شد که مصرف سوخت آنها نصف خودرویی بود که اینها در داخل تولید می‌کردند.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/692388" target="_blank">📅 19:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692387">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SD9ev61qdI7xciyf4tFHRBvlHmBbW7qHhgOBImebLlwWlERKM6f7pvDLhRo_hJDLKv0buH_wL0-_b-64dOMZC0JqkIe1c8-CH5LttnU4I5QBOHmItgIH-Y_u6AlrnRZqkIzrEDaS1MGMFLLCGnZhT-hyREXZR1FPDg9EkIu-hKIdYkqKirzqFnoNZgx_0qii8ZzsyTGI6mP6BHpNm8moTJhx0I1ms9UIxrxYveiIZRkOeMWHD2XrzFh6yofv77u5K4_q3weQbCeQUtRmJGGzA3dFod5uB_mAysTQO5jtDhcOZ65HXzFNv0SFw8hZNkeVqJqT6sE48bwwAtZoyFsh7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آیفون ۱۸ تنها دقایقی بعد از موجود شدن در فروشگاه‌های اینترنتی، ناموجود شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/692387" target="_blank">📅 19:29 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692386">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bab1625dec.mp4?token=pynr1roasMhXvTMEHw1WTxXyciuLQwRUGAZNi5O2WFZjT8rMCghofN7gDfmsWk-HIYHCGFhDgmRXRAp91ymXLNJsZCvjGBQ0HNg8YARfuRrTbUMtsfkfXMdRdajOkYjHooBAiI8yNo1WHESBRDYo1sGtBYnpqOKAyGxaSRW9X_A_uJHY8UJd3PL_c2-Wadby3utxtVnfKIg482D6e3Y0vGpNSm_TBZWsZhWgBoYF-KMhHesdLhrT5JACFUO2-xG6fjWitM1ye9rez9rRNvyUUHDA6467vc60zfHGnNUy4HcGSLzC_p1JTnGhIVrbFN-sEMf1Sp0tPZp92_0L2OQ-Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bab1625dec.mp4?token=pynr1roasMhXvTMEHw1WTxXyciuLQwRUGAZNi5O2WFZjT8rMCghofN7gDfmsWk-HIYHCGFhDgmRXRAp91ymXLNJsZCvjGBQ0HNg8YARfuRrTbUMtsfkfXMdRdajOkYjHooBAiI8yNo1WHESBRDYo1sGtBYnpqOKAyGxaSRW9X_A_uJHY8UJd3PL_c2-Wadby3utxtVnfKIg482D6e3Y0vGpNSm_TBZWsZhWgBoYF-KMhHesdLhrT5JACFUO2-xG6fjWitM1ye9rez9rRNvyUUHDA6467vc60zfHGnNUy4HcGSLzC_p1JTnGhIVrbFN-sEMf1Sp0tPZp92_0L2OQ-Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افتتاح اولین پایگاه آموزش نظامی یگان‌های مردمی جانفدا با شلیک فرمانده بسیج
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/692386" target="_blank">📅 19:24 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692385">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VgYRRKW6JX8oBafWEJHg3bFelod5K4GgubRxkOnD9jNrpmZWVjx-GdYWH_O1amNyG_1KeFuVQ4CRqPuvxCtlflma3QpNTTMD78K_g_YY93Czl_Ih_6JpUPSfGd9y898pYrhCE7FI7SLTt-uoSE8cuvmX8ucECmEh9B3iZ5RaFmMgLJwRB4jGvrntvSDtU5wObiLKJeMdInYFqS1GswDxORdw4zuGbrztor_HN7JMfM7NrWWe2j8Zw5PNsddo0fb2-n43AxbHjOE8XWPQV8M9g9EVbey8Cy4tZ_Zw5xb4Na9jOcyQikLhbqPKJPRu0fE5SgmJ4r7kYmmf53gmyh2QSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تقدیر زاکانی از پزشکیان
🔹
آقای پزشکیان سربلند باشی که یاد امام شهید و شهدای مظلوم مان را در سازمان ملل زنده کردی @AkhbareFori</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/692385" target="_blank">📅 19:20 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692384">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
وزیر اقتصاد: ارائه کالابرگ با مبالغ جدید از ۱۵ مهر آغاز میشود
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/692384" target="_blank">📅 19:15 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692383">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/avutQmBmTgXQ1bqemhYFlNeFIRL4j0PrP7PUnCMkMF06O7I4jt-RU1_jMWPxj6-oiMcisDyaKGypluOI-xBLdrrlCRMUqfiw4ACrdgQ2ia1nOW5p1uAzehzANiMnVTH6qihYRa-EXp9ccCts6eCL-2C2NF9kY_R_wtMHM0oa0zCyexk0v-P2PZZHS2A9bO2V2EA9dlRw3wt-3CPYlr_i9OE7ll7d2AfP0LU20hPYplvnAxRRlRYOFgY9X09qsaksdNiX6LwH-j2wBBV4k_c9FakO9ZgukuDhwXuzRlRsbvsZo_lD9VmdUOXhYIxaVU4tNWYdy2_D-2QEJ8S2zfcjxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اقدام عراقچی در تعامل با ویتکاف بدون هماهنگی با نهادهای ذیربط صورت گرفته است
🔹
تعامل غلط آقای عراقچی با ویتکاف (از نمایندگان ترامپ در مذاکرات) بدون هماهنگی و کسب مجوز از نهادهای سیاستگذار و مسول در این زمینه (از جمله شورای عالی امنیت ملی) صورت گرفته و برخی…</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/692383" target="_blank">📅 19:15 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692382">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
ادعای پنتاگون: تعداد کشته‌های مرتبط با جنگ ایران به ۱۹ نظامی آمریکایی رسید
🔹
پنتاگون شمار فوتی‌های اعلام‌شده را ۱۹ نفر اعلام کرده؛ مقام‌های آمریکایی می‌گویند آمار واقعی تلفات ممکن است به ۲۲ تا ۲۳ نفر رسیده باشد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/692382" target="_blank">📅 19:13 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692381">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
سقوط جنگنده «هاوک» نیروی هوایی انگلیس در ولز
🔹
یک فروند جنگنده هاوک نیروی هوایی انگلیس در نزدیکی پایگاه RAF Valley در ولز سقوط کرد؛ دو خلبان هواپیما با خروج اضطراری نجات یافتند و علت حادثه در دست بررسی است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/692381" target="_blank">📅 19:08 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692380">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
نگرانی هند از تحریم‌های آمریکا علیه روسیه و ایران
🔹
وزیر خارجه هند، در دیدار با «مارکو روبیو» بار دیگر نگرانی دهلی‌نو درباره تحریم‌های آمریکا علیه روسیه و ایران را مطرح کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/692380" target="_blank">📅 19:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692379">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
وزیر‌خارجه دولت تروریستی آمریکا درمورد ایران: نمی‌خواهم مذاکرات دیروز را به‌عنوان یک پیشرفت بزرگ جلوه بدهم، اما در عین حال فکر می‌کنم همین که دست‌کم گفت‌وگویی انجام شد، اتفاق مهمی بود
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/692379" target="_blank">📅 19:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692378">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b71fa33aec.mp4?token=pJt6eLZPz0nbakZ2eIjq6h-ONwuSq_CRk0RLf40JQQij3JNSCP-vuUSlrnuHplJCv9BHVac6pfvuq2YNT9ufpJwJD8gGBWZ3P_nAMBitqcLvPlgGaDaGaHehKpTp0y5GtwB_3Jku0tY6hLg9O4F_lQ9vDscBljKrtXMdcISiZL2shz43zRWIBjsmo5eW6aw6D6fyArIEqtJ5yqYLpBr--khXVUQs3PzN6UhLnxdj02edkUe1D9WzqfVWeG6hAz7lJ_uTHOYOGEkDjWzNBZ_QIOG8pSp1Xk-pIfyeaRfocBTXY82bOIZ_1CFYEB77Vsvjlj6XC2vB2w3_wZETBCKWSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b71fa33aec.mp4?token=pJt6eLZPz0nbakZ2eIjq6h-ONwuSq_CRk0RLf40JQQij3JNSCP-vuUSlrnuHplJCv9BHVac6pfvuq2YNT9ufpJwJD8gGBWZ3P_nAMBitqcLvPlgGaDaGaHehKpTp0y5GtwB_3Jku0tY6hLg9O4F_lQ9vDscBljKrtXMdcISiZL2shz43zRWIBjsmo5eW6aw6D6fyArIEqtJ5yqYLpBr--khXVUQs3PzN6UhLnxdj02edkUe1D9WzqfVWeG6hAz7lJ_uTHOYOGEkDjWzNBZ_QIOG8pSp1Xk-pIfyeaRfocBTXY82bOIZ_1CFYEB77Vsvjlj6XC2vB2w3_wZETBCKWSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور‌ حجت‌الاسلام طائب؛ رئیس سازمان بسیج مستضعفین در اولین دوره آموزش نظامی یگان های مردمی جانفدا در میدان امام حسین (ع) تهران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/692378" target="_blank">📅 19:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692377">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
ادامه اقدامات خصمانه امارات علیه ایران
🔹
بانک مرکزی امارات متحده عربی در اقدامی همسو با منافع آمریکا بانک ملی ایران را از فعالیت در این کشور منع کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/692377" target="_blank">📅 18:56 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692376">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MOe0PHqu_4Gfvoq_WBrgvRe24jPkWtTBoP0EyMEj19bb33-SOVotREAl69PUH5IUK7qguf9Dg0qzuamlolu-izjRlWFuWRmDKYR1u91Fql7MCaTF9-UZGzFbE9K-C8aY9rogCHqAs_bKkIzLBhnYa93YsuTmOgWRsDb0LcwYr8tgDP1Mi9ioXdolMK9scqQDrmjw29xE3I09jIH_cXJmNIB5TXB_AcWC7MC5OO7NK8wJ2dXX4q_xLU8tjhrAlZg6romHkMpBL2kjzbkGlXJd31mTH9ia6h_N9qTh3mA4fVie8XddQ4jASTlDIVtF9dviR19MnJGuq7NgDKrGyQxEqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نشان دادن تصویر رهبر شهید انقلاب توسط رئیس جمهور
🇮🇷
✊
@AkhbareFori |</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/692376" target="_blank">📅 18:53 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692375">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fmRQvhPAeOKZ2mNlmUw3GomJ7xt7umDeMtlJXVRMrpGBLwPGm5cQ3FnX8kZP4vKTmNgmYW_XCCv1vgw4_6e_CMVe8zOxIfnq4NoYoD2Dx2xQ9NiwH2poDhl6gs6N3Dk3fyhTXWBO56WYl7qNARDhu698eaFrgJfcxJQtHp07B8mlcPwsuxhL0652zp1Sgi_pjFUHhKtrQfO-bjkCMlk8T_oUn3Cc0M2QNZqNrWgoQvsU-ZG0A4WX1KIWwe2WyTkZrGwbOYHWx4togLLLgOt4askueUL0Ql_d4Q_eB1d8PBDtwfg-9avu85UiMrLs2MTf_jiunJpF0t-yB_Yfr4CbFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تقدیر زاکانی از پزشکیان
🔹
آقای پزشکیان سربلند باشی که یاد امام شهید و شهدای مظلوم مان را در سازمان ملل زنده کردی
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/692375" target="_blank">📅 18:50 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692374">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
روبیو در ادامه گزافه‌گویی‌هایش: احتمال استفاده از گزینه نظامی وجود دارد و مدعی شد بخش جنوب تنگه هرمز باز است
🔹
وزیر خارجه آمریکا بدون اشاره به کمک برخی کشورهای منطقه در حمله علیه مردم ایران گفت نیروهای نیابتی ایران در منطقه، امنیت و حاکمیت کشورها را تهدید…</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/692374" target="_blank">📅 18:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692373">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
روبیو، وزیرخارجه امریکا: توافق با ایران نیاز به بازه زمانی طولانی دارد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/692373" target="_blank">📅 18:44 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692372">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a7e36c97f.mp4?token=Z3J82g5LrGUQdvvxhMIMwyhnPum6M_rv9O7zqYq6O4PQGzTud2JOAQT14vgZYLe9G0Up9GdWyQRYIjDGKJVs1cIZbupR3-LduqA3O25qVQZkmP4a9Ir7RfNTEny0yGI8bfS9BhYHNqRHI0TWi-7312h6lCSPfA-z9TFtKzpUsyTfEtWo-AV0wEjhm_nZncZ_2tTl2VrGrXG6CVoRMmAVmHHLriTk_Y6YNnKzv0nxQh4uXGgnqf-8iUHgCzOq1GG4-hxwMK97z-GkvyfTOgjrobcxZz7-uJ0uW4q7Mp6P42QvT8cVl5hW8RyHXqfRVnc8kpFT6BML76EGayvqRaZh_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a7e36c97f.mp4?token=Z3J82g5LrGUQdvvxhMIMwyhnPum6M_rv9O7zqYq6O4PQGzTud2JOAQT14vgZYLe9G0Up9GdWyQRYIjDGKJVs1cIZbupR3-LduqA3O25qVQZkmP4a9Ir7RfNTEny0yGI8bfS9BhYHNqRHI0TWi-7312h6lCSPfA-z9TFtKzpUsyTfEtWo-AV0wEjhm_nZncZ_2tTl2VrGrXG6CVoRMmAVmHHLriTk_Y6YNnKzv0nxQh4uXGgnqf-8iUHgCzOq1GG4-hxwMK97z-GkvyfTOgjrobcxZz7-uJ0uW4q7Mp6P42QvT8cVl5hW8RyHXqfRVnc8kpFT6BML76EGayvqRaZh_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سازمان عملیات تجارت دریایی بریتانیا: یک کشتی تجاری در تنگه هرمز هدف یک پرتابه ناشناس قرار گرفته است
🔹
دو نفر از سرنشینان کشتی تجاری هدف‌قرارگرفته در تنگه هرمز زخمی شده‌اند و تمامی اعضای خدمه از کشتی تخلیه شده‌اند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/692372" target="_blank">📅 18:40 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692371">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a449a8b51f.mp4?token=ttw2aYz9uP5qWlHoBo5tcKM724oLyChRPYhWbRiAvkl_KuwfaRMjkS-W9D9Ut6Be9BwyiASsTAOAdz12frpU4FnI-4WikhP3mfbRkU_pEcapT5IvU4ZbjdX5X15qaMyFMJ4Kxen5WFySRYi73IhJcDTwTHtrXid6dru6uVTYrkWgdFhBpk6G3J6dmrudzyPXRsv4tMCCFLuFljRt2J_3nUw6pyKvQs6qzEzT_Wi9MLgaeNbjQ5NgRdObfIsmr8TnG-7xDYzWGh4CoYi3WvfiJ9i11IhH3pmEgublLP0pHgk_1WoAW2Z1iTP1YXdYsg49ndDuhmqFN9pZZ7NL_d5Q6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a449a8b51f.mp4?token=ttw2aYz9uP5qWlHoBo5tcKM724oLyChRPYhWbRiAvkl_KuwfaRMjkS-W9D9Ut6Be9BwyiASsTAOAdz12frpU4FnI-4WikhP3mfbRkU_pEcapT5IvU4ZbjdX5X15qaMyFMJ4Kxen5WFySRYi73IhJcDTwTHtrXid6dru6uVTYrkWgdFhBpk6G3J6dmrudzyPXRsv4tMCCFLuFljRt2J_3nUw6pyKvQs6qzEzT_Wi9MLgaeNbjQ5NgRdObfIsmr8TnG-7xDYzWGh4CoYi3WvfiJ9i11IhH3pmEgublLP0pHgk_1WoAW2Z1iTP1YXdYsg49ndDuhmqFN9pZZ7NL_d5Q6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور سردار حسن‌زاده؛ فرمانده سپاه حضرت رسول (ص) تهران بزرگ، دکتر زارع؛ سخنگوی ستاد مردمی جانفدا و سرهنگ کوثری؛ معاون آموزش سازمان بسیج مستضعفین در اولین دوره آموزش نظامی جانفدا در تهران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/692371" target="_blank">📅 18:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692370">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
رویترز به نقل از یک مقام ایرانی: تهران در حال بررسی پاسخ آمریکا به پیشنهادش برای پایان دادن به خصومت‌ها است
🔹
هنوز اختلافات زیادی بین مواضع ایران و آمریکا وجود دارد، اما دیپلماسی ادامه دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/692370" target="_blank">📅 18:31 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692369">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
مجتبی زارعی، عضو کمیسیون امنیت ملی مجلس: عراقچی مجوز مذاکره با ویتکاف را دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/692369" target="_blank">📅 18:30 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692368">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
وزیر امور خارجه آمریکا: به تعهدات خود در مورد توافق دفاعی با عربستان سعودی عمل خواهیم کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/692368" target="_blank">📅 18:28 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692364">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T6cRQuqETp6QLM6KX5pcW6s-QuZuY6lR3qmX-VvZJf6Kbmo6pa-ZffEfq_ZZL3HrzVWyJUCTOw1WkJYHsLR9bntSs6dmBE6ztXcUediYHIzP9t0dNx7cQ9Zr6sFcf7WD3x1eA57NtTbLIqmjNrT3hl4BLDp-0NVbUY5gKNlAv6UfwnV-_BOOgDlzUCVJa8518IGXLskKOoX7K1aVxyDwSxQgExxzdRrbR3uh3YkmDypsiPE0H__2In_c9m3mjlkDerhdt-h-FohklmsxFeShrJKIZ1-3ojLhafAnVWwP16j_0gB_RJZvsUAtYM2vD7zK0zyZ6YOFidqAp420W_c84g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یکی از مهم‌ترین اصطلاحات ضروری، اصطلاحات مربوط به زمان هست که به‌طور کامل این پست بهمون یاد میده #زبان_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/692364" target="_blank">📅 18:26 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692363">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/swHrxn8A--0MjI85jlb5VVeK65-HjWGEDQhQpT6J3-V_XVOvPPNOH9rFLo_3kdzCHbj0v0AF4a30lO3lAg63R_dZ8hUAp0GC330svdBLls4hwGj2GhebQFqa8ZNKv1vmrEc8dw5Wrc5gpUH-9cnClVv-plFiIH3SQktxHkytZdr08tVLET_avRJDeV5XVV-LJiXuuQmzWocpN02TrfCy8x2vloDiFZxiPGb1r9p3nw4udyeWWbFTZh55qoQJBgbd9ZdnwDYQ16dLvAvZVz5JBJ9EdSWDZbEPXNH1rIdK6Qd5qDZcmkniZyVwCpTRQ-JeNzQXdgItInnXejEbBXWIgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TEeqyi2-8E7wvBt77sv0-BPXqrnSIcXbonGKU21MuoZNS4M9Te2VJ83MzVlgs9ztzt9zIoZQLBPRlxa5l5dNiGOmK5z4kkfJcWvQS7jW-y8NIcIiVjFSbl_rFWWEykA7szlrnOS86JPHoVEW9MClMPWFbnAj5-YmHNpQ6yMoJqQdUco_OKp_sLij-UZ3mu5aU0785XTusA4_Ufqw5anoO3f1Q1QDDVcjkhB2gqgcsDKMah2cTWy0wJCxUHQdorIg53-deiug82k_5Q2zREVoZK-RxQpuMfNka2Raz0XcvqsQLjyF8WMAPciiiJ7ghtQAkRb8e-hIGQqgXHvLsjbN8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XCGBoMCwuLYm81R5gTrwY5ZDV8NaToHcXw1ZXhNMvA0zA3h5c40l3xwJvtMRQU1fJmukhqAaKPgUVcfSjIurPGieRK1e0tOo5CQYNSizTLN-ymwwq8oqVbD7Eguwta9ErlnuPmT4ttOuRtWdO-dZtXbO6utX6UQBlWSjX3XfN7Q1sonxTFwT7oHEyjWaG0rrbWhz_uGZakuxVrxQqehF6WXGlnx0LT5uhPoJnxmHgdBNvL-HHGVgOiqgo0VxRpIL0rhrKvP_CXYr38vIsNG5ArdyJkmTzRuVTOq2UuX2mRy6Myq6QjISxDBZ6SriiCvtojIC6KCayTem07L8neb94w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NnXKZTWub-Xl1ZTrsOHcIoVi5C1MPq6ANoGSRbucGFFHLQV8Uv-GEYiUHUXEun1G2HBuuFtQYOT2G7y5VHFn8-virJJuGBEjpmohVkDL6KY7Zht_4Zu6WXkBK5fOIKZgLam0vTfWvShxiSsjO8eGW6hN-IPl4jhmD-shP8v333bBH2ZV2GdH7hz13omNUsXfRxp2FpLepA7-e4jwrz_zzXj6tyAFb8FVAIzE4XF8YzkUCoSDr6oTUVC3-Qu4UbNFjZpYFdz5v-OA8ive5oUY8rIDccgv2XuiS4m9LcR8vFX_4yNR7DQdfRT6Fm9Z0YaqsdZ0LTvaltagS536RP8TzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصویر شهدای مدرسه میناب در دستان پزشکیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/692363" target="_blank">📅 18:26 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692361">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/478c35574b.mp4?token=h_AVsutiWdWReNS08ugwb81mkMXpRqwlZCcHPnRDfx0M28o2_BU91Qm7BwTrO4BekFmZxT2WAinWrfwhs240scpS5QXBG3-6M57UfvDItM649OHSXHi6lX3OOD_Js_n4q-tCLgosVJAcHBnTHKZJ2f4Wt8_lfRodUo5aSSYKW1fforNg4eFoMfbR05NUuQrHUXipsIRuWLDe3HSndEV3M1a8YCdFwFV-vSiVnuRH2gc2WauuWDB58U1ZIrTwt2FiRCMjugk9MriDTwsy50Ut8Vrk08CmNmRxDDDdGY-Xhpy1VYIyL5-Rt-nf-b7jseNY4fmq_l-rAYzNtG-MYfxZJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/478c35574b.mp4?token=h_AVsutiWdWReNS08ugwb81mkMXpRqwlZCcHPnRDfx0M28o2_BU91Qm7BwTrO4BekFmZxT2WAinWrfwhs240scpS5QXBG3-6M57UfvDItM649OHSXHi6lX3OOD_Js_n4q-tCLgosVJAcHBnTHKZJ2f4Wt8_lfRodUo5aSSYKW1fforNg4eFoMfbR05NUuQrHUXipsIRuWLDe3HSndEV3M1a8YCdFwFV-vSiVnuRH2gc2WauuWDB58U1ZIrTwt2FiRCMjugk9MriDTwsy50Ut8Vrk08CmNmRxDDDdGY-Xhpy1VYIyL5-Rt-nf-b7jseNY4fmq_l-rAYzNtG-MYfxZJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اولین دوره آموزشی نظامی یگان‌های مردمی جانفدا آغاز شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/692361" target="_blank">📅 18:20 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692360">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
بازار سیاه فروش کد ملی برای ثبت نام خودرو / قیمت ۲۵ میلیون تومان ناقابل!
🔹
انتشار آگهی‌های فروش کد ملی برای ثبت‌نام خودرو در فضای مجازی خبرساز شده و برخی افراد برای واگذاری کد ملی خود تا ۲۵ میلیون تومان مطالبه می‌کنند؛ پدیده‌ای که پیش‌تر در ثبت‌نام خودروهای وارداتی نیز گزارش شده بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/692360" target="_blank">📅 18:18 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692359">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
پزشکیان: صلحی که برای همه نباشد صلح نیست؛ سخنان دیروز رئیس‌جمهور آمریکا نشانۀ بارز خوی قُلدری است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/692359" target="_blank">📅 18:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692358">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a83689d89.mp4?token=MjMA6CoKfxuMKCx4JSnksY9ZMz83zX3-F6wSljPbj6ZMzDWnX-kSMauw_JW9hKPlCIO7BLruYYvTkkyLiIzWUJGC8cDZlU9kEq_RaDeWFZRGuscs81FPpAjttgnfQLnNyC1VIfbVk6s-ljWXJN5iTh5tfVQ0jWoWQbmbSwWZmE_5beJvqfCQ0myRHQsEfdi8Nys-C9weOmGnED0za2zIl-fqBrQHD66dwOZdDbHbhcG4aYXnbTxB9F9PPvhNNG6vf0dsiX1yTtrXNBq5tK9sFILt_QEFUxVGOLocsUpS4-jOf4Uog457K8_lB9pwz7N-Ob90IvIXysJrA3uhq2PmOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a83689d89.mp4?token=MjMA6CoKfxuMKCx4JSnksY9ZMz83zX3-F6wSljPbj6ZMzDWnX-kSMauw_JW9hKPlCIO7BLruYYvTkkyLiIzWUJGC8cDZlU9kEq_RaDeWFZRGuscs81FPpAjttgnfQLnNyC1VIfbVk6s-ljWXJN5iTh5tfVQ0jWoWQbmbSwWZmE_5beJvqfCQ0myRHQsEfdi8Nys-C9weOmGnED0za2zIl-fqBrQHD66dwOZdDbHbhcG4aYXnbTxB9F9PPvhNNG6vf0dsiX1yTtrXNBq5tK9sFILt_QEFUxVGOLocsUpS4-jOf4Uog457K8_lB9pwz7N-Ob90IvIXysJrA3uhq2PmOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: ترامپ باید بداند که مقاومت مردم ایران در برابر تحریم‌ها، فشارهای بیشتر و رفتارهای زورگویانه، تنها افزایش خواهد یافت
🔹
ما هرگز سر خم نخواهیم کرد و تسلیم نخواهیم شد.
🔹
ایران باید توسط آقای ترامپ و کسانی که به دنبال تحمیل خواسته‌های خود به ما هستند،…</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/692358" target="_blank">📅 18:13 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692357">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
پزشکیان: ایران خواهان تعامل، همکاری و مشارکت با جهان است و این رویکرد را نه از موضع ضعف، بلکه بر پایه اعتماد به توانایی‌های خود می‌داند. که امنیت منطقه تنها از طریق همکاری مشترک میان کشورها امکان‌پذیر است و ناامنی نیز می‌تواند همه را تحت تأثیر قرار دهد.…</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/692357" target="_blank">📅 18:08 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692356">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f1e98216e.mp4?token=DnzkPFQ81ibZpdYY42M6MPod3LEX9bwF-tW8FrojB9J3b6lH9RfLJKBw7fxJ2eePlTzq5FqfSHpVM7zEXYa-y-1WYbCRQZ6I8yaoqILtbvejDg3NpEjZz1vxrhCkjRwjO_UvHGSt0Vs_hO_Rwn1P8pqRrT4F9sPHLsxDbfhggV7siodrLTt57gouSx0o9Kbg03S8upNkcXx0LzO7rua-lMKlyE4wY0GOVbQv5SSH4jDFAoFxqOUnE73-GQ38VlWSUrI5e6SnnHoyMlb63vvFkchkFkjB9ksy6vLH1lixoe4Ek5GZgverDgNpXtrPJZySozWmIYtzPv-_lJBR3WC0n4qfARdmWJdUz_5xVmouEJiL4FRr2sY_dooMLIn2yH9cYdBr4H-LAGcdaBBQg69bNR0sLwbC7_10WlnaXHWjJF6PouBuLcIjQVoqSYjgdcVXjcDX_Rkfl5QrCOBkvpxCFKDQo1NrZNonT9yS-mtnAv-LAsaARqF2yMyOJK54o69wtns6q0CIZ1pY-jDkH5U7o79NdS_v99h19PGCZa-wgwtrd3_OIHyvp4iR5Ymy_q6u6iPBVJ6PlWWxQM-P5V4umDOi4wzzYrjp1ndSwTGEkrJrgFrmdH2h6p6JK3rVcBm3wE7yuq5cUplupsiSFbdeHto-JQwjBh8SP5szQ-1rWTM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f1e98216e.mp4?token=DnzkPFQ81ibZpdYY42M6MPod3LEX9bwF-tW8FrojB9J3b6lH9RfLJKBw7fxJ2eePlTzq5FqfSHpVM7zEXYa-y-1WYbCRQZ6I8yaoqILtbvejDg3NpEjZz1vxrhCkjRwjO_UvHGSt0Vs_hO_Rwn1P8pqRrT4F9sPHLsxDbfhggV7siodrLTt57gouSx0o9Kbg03S8upNkcXx0LzO7rua-lMKlyE4wY0GOVbQv5SSH4jDFAoFxqOUnE73-GQ38VlWSUrI5e6SnnHoyMlb63vvFkchkFkjB9ksy6vLH1lixoe4Ek5GZgverDgNpXtrPJZySozWmIYtzPv-_lJBR3WC0n4qfARdmWJdUz_5xVmouEJiL4FRr2sY_dooMLIn2yH9cYdBr4H-LAGcdaBBQg69bNR0sLwbC7_10WlnaXHWjJF6PouBuLcIjQVoqSYjgdcVXjcDX_Rkfl5QrCOBkvpxCFKDQo1NrZNonT9yS-mtnAv-LAsaARqF2yMyOJK54o69wtns6q0CIZ1pY-jDkH5U7o79NdS_v99h19PGCZa-wgwtrd3_OIHyvp4iR5Ymy_q6u6iPBVJ6PlWWxQM-P5V4umDOi4wzzYrjp1ndSwTGEkrJrgFrmdH2h6p6JK3rVcBm3wE7yuq5cUplupsiSFbdeHto-JQwjBh8SP5szQ-1rWTM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: ایران خواهان تعامل، همکاری و مشارکت با جهان است و این رویکرد را نه از موضع ضعف، بلکه بر پایه اعتماد به توانایی‌های خود می‌داند. که امنیت منطقه تنها از طریق همکاری مشترک میان کشورها امکان‌پذیر است و ناامنی نیز می‌تواند همه را تحت تأثیر قرار دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/692356" target="_blank">📅 18:08 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692355">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
روبیو، وزیرخارجه امریکا: توافق با ایران نیاز به بازه زمانی طولانی دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/692355" target="_blank">📅 18:06 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692354">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
تصویری از هیئت ایرانی حاضر در سالن سخنرانی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/692354" target="_blank">📅 18:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692353">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tGI3AzyS6lA5XdFl0uzpzAJMhGZtYnp32y6xavCA8R76I9BsYc97Vr4_Xcr6PHUNXvYtiwqYwy7_-6z4kbWQ65htEavueNO4ZQCN5l0QOo8mg7_1OWnE2DwsgtCem9PwZ1iQT57XqtuKGyZZ4FFwUl2UdYCo4Yz0PyJmIltQSjreVdIRjSz0qJnjkjYNLJFP6ic-vIidNfZ8Z2p761KLw4jkFaPsNlpRNRCSXe55bqoCTKPxkkeSEjg2jKrtrLq8y_ZsMwfXlh-uVpVbjMIk3HFZqqv24w9a4gVqaxmKv1c7qQHH8rdaAgKgYiNg-XQ9XZw9xmry2UYhqTOsLDrfAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان: ایران هرگز، مطلقاً هرگز، آغازگر جنگ نبوده است، هرگز جنگی را شروع نکرده و همواره تعهد خود را به میز مذاکره نشان داده است
🔹
آنها جنگ را به ما تحمیل کردند، اما ما ثابت کردیم که از جنگیدن نمی‌ترسیم – جنگی که ماهیتی دفاعی دارد – و ما تا آخرین نفس در…</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/692353" target="_blank">📅 18:04 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692352">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
پزشکیان: دهه هاست قطع نامه ها صادر می شود اما اشغال و خشونت ادامه دارد
🔹
اگر انسانی را با بمب و ویرانی از خانه کاشانه اش بیرون کنند حتما مقاومت خواهد کرد
🔹
مسایل منطقه ما در خود منطقه و توسط کشورهای منطقه باید حل و فصل شود
🔹
اکنون سخنی با همه کسانی که مسوول…</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/692352" target="_blank">📅 18:02 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692351">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9788505185.mp4?token=PmIF5R7yiUX8fZ-H1eNH9Mx4QOZNd0UxumOYYHpz4qG6WB_Bh4WB6P-JA3unj60y3WM2OhmAD6OvsMgpt5WtgxggHYRCKRbqUuY__vxz41bZ-LgTrKp9tVDgjqJxgElupp2zv5gdlW0W-QD8_l6B1ofCGRpismTQOefNDzi_6L7za4IE9_TZZ3ifZVbhCS2GMnGvDRCNRak5yqfs-e9Onwx-igN_8p_23GpsWM5gvjC1oyz_pVxnL_gwHjmcBA0nPo65lqz6WL0hN_J2tyGFI4UaeRgMmctrxfKf-mwCTZvp9zBS3bMeQJuFu2VsTfWlsJIZcIjjHunat-QAD2uRrQSWTjJT3A5E6PMEI3Xgg1DZretLMZBRsTVq1LpzHYwJL5coWsfB9PE3vue2_nsEpV5tz9wXaFZ_b2aHttshDEVD7nmqafK0pDK_I3UY3WIjtTR53MUXj9duefOXzRdd6LSd4SdxhncvhgEHiD9kiUrlDbA253PdtNYULakvAwf2uWVQaPOhchVecLWXFiUqCtbeguZvnHqUvaN1NZnHnlAku_Ksx_HAglTIrAlDBugptirT6I25b4IVT1pfdZNBhwkCN_AFAGaEyhbuZKeA5VTPtlH3x42tQt7XDPmlStHPyz7lo8O_xi0-kHZOnBMmkoxHa1XTm5VXzB3466zPMlY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9788505185.mp4?token=PmIF5R7yiUX8fZ-H1eNH9Mx4QOZNd0UxumOYYHpz4qG6WB_Bh4WB6P-JA3unj60y3WM2OhmAD6OvsMgpt5WtgxggHYRCKRbqUuY__vxz41bZ-LgTrKp9tVDgjqJxgElupp2zv5gdlW0W-QD8_l6B1ofCGRpismTQOefNDzi_6L7za4IE9_TZZ3ifZVbhCS2GMnGvDRCNRak5yqfs-e9Onwx-igN_8p_23GpsWM5gvjC1oyz_pVxnL_gwHjmcBA0nPo65lqz6WL0hN_J2tyGFI4UaeRgMmctrxfKf-mwCTZvp9zBS3bMeQJuFu2VsTfWlsJIZcIjjHunat-QAD2uRrQSWTjJT3A5E6PMEI3Xgg1DZretLMZBRsTVq1LpzHYwJL5coWsfB9PE3vue2_nsEpV5tz9wXaFZ_b2aHttshDEVD7nmqafK0pDK_I3UY3WIjtTR53MUXj9duefOXzRdd6LSd4SdxhncvhgEHiD9kiUrlDbA253PdtNYULakvAwf2uWVQaPOhchVecLWXFiUqCtbeguZvnHqUvaN1NZnHnlAku_Ksx_HAglTIrAlDBugptirT6I25b4IVT1pfdZNBhwkCN_AFAGaEyhbuZKeA5VTPtlH3x42tQt7XDPmlStHPyz7lo8O_xi0-kHZOnBMmkoxHa1XTm5VXzB3466zPMlY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رئیس جمهور ایران: ایران، کشورهای همسایه را به عنوان رقبای امنیتی نمی‌بیند. ما خواهان داشتن همسایگان قدرتمند هستیم.
🔹
در آب‌های تنگه هرمز، ما نمی‌خواهیم ناامنی ایجاد کنیم. ما نمی‌توانیم اجازه دهیم که برخی افراد به طور آزادانه به این آبراه دسترسی داشته باشند…</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/692351" target="_blank">📅 18:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692350">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‼️
رئیس جمهور ایران: ایران، کشورهای همسایه را به عنوان رقبای امنیتی نمی‌بیند. ما خواهان داشتن همسایگان قدرتمند هستیم.
🔹
در آب‌های تنگه هرمز، ما نمی‌خواهیم ناامنی ایجاد کنیم. ما نمی‌توانیم اجازه دهیم که برخی افراد به طور آزادانه به این آبراه دسترسی داشته باشند…</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/692350" target="_blank">📅 18:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692349">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
پزشکیان: ایران را نمی توان با جنگ وادار به تسلیم کرد  ما ثابت کردیم که برای دفاع از خود از جنگ نمی ترسیم تا پای جان برای دفاع از ایران عزیز ایستاده ایم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/692349" target="_blank">📅 17:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692348">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
پزشکیان: ایران را نمی توان با جنگ وادار به تسلیم کرد  ما ثابت کردیم که برای دفاع از خود از جنگ نمی ترسیم تا پای جان برای دفاع از ایران عزیز ایستاده ایم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/692348" target="_blank">📅 17:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692347">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
پزشکیان: ما نمی‌توانیم بگذاریم همه از تنگۀ هرمز بهره ببرند اما ایران از آن محروم باشد
🔹
راه را بر ایران می‌بندند و سپس از تنگه اسلحه و مهمات و موشک برای نابودی کشورها از تنگه منتقل می‌کنند؛ این امکان‌پذیر نیست و ما اجازه‌اش را نخواهیم داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/692347" target="_blank">📅 17:58 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692346">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
پزشکیان: اسرائیل می‌کشد، ایران تحریم می‌شود، به هرکس بگویید خنده‌اش می‌گیرد
🔹
صلح در غرب آسیا بدون توجه به صلح در فلسطین اتفاق نمی افتد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/692346" target="_blank">📅 17:57 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692345">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
پزشکیان: از جنگ نمی‌ترسیم و برای صلح از مذاکره نمی‌گریزیم
🔹
کنایه رئیس جمهور به آژانس بین اللمللی انرژی اتمی: بمب اتم در اسرائیل است و بازرسان در ایران!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/692345" target="_blank">📅 17:56 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692344">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
پزشکیان: اسرائیل به هر کشوری که دلش می‌خواهد حمله می‌کند
🔹
عاملان ناآرامی اسرائیل و آمریکا هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/692344" target="_blank">📅 17:56 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692343">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
رئیس جمهور: نه سلاح هسته ای، نه صرف نظر از دانش هسته‌ای
🔹
پزشکیان: تسلیم نمی‌شویم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/692343" target="_blank">📅 17:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692342">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3573a2cefc.mp4?token=kXgRnfkWB9duo7U7jv4EPHOcp3_w1tkruTeOAXi94gWIiQ9CofCX09_C0REmfZ7EUDTYHdtnrqvOGNOksR8UTVdKm7szbwbmPRT1k-ryn0bOuVueJshQ-ApEMeJC6X_3vzRCN-4PFCzMpR0D8tfczyIXHaW_89BJM7Lv8lXDJ-GS0yxt0d9Z4lccqy7V2Qq_Nldjr-oQ-J-83t84soAFqWkiybHc3-5jUkt7uBYCh9CduXgxV68ZRmgCArnYNwHTNOxr9sYj-Of3sKBDB29hopfyl4uc52iikV-TGy29VNRlxw3ec-zaF6LdTTC-q72qr58p41mtJzzGM3xIEMt-UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3573a2cefc.mp4?token=kXgRnfkWB9duo7U7jv4EPHOcp3_w1tkruTeOAXi94gWIiQ9CofCX09_C0REmfZ7EUDTYHdtnrqvOGNOksR8UTVdKm7szbwbmPRT1k-ryn0bOuVueJshQ-ApEMeJC6X_3vzRCN-4PFCzMpR0D8tfczyIXHaW_89BJM7Lv8lXDJ-GS0yxt0d9Z4lccqy7V2Qq_Nldjr-oQ-J-83t84soAFqWkiybHc3-5jUkt7uBYCh9CduXgxV68ZRmgCArnYNwHTNOxr9sYj-Of3sKBDB29hopfyl4uc52iikV-TGy29VNRlxw3ec-zaF6LdTTC-q72qr58p41mtJzzGM3xIEMt-UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: برای کشور ما انرژی هسته ای برای بیماران ما درمان و برای کشاورزان ما اهمیت دارد و برای آینده برقی پایدار است
🔹
در منطقه ای زندگی میکنیم که جنگ مرز نمیشناسد/ ما همسایگان خود را قوی میخواهیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/692342" target="_blank">📅 17:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692341">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb9890865e.mp4?token=DOnn9CBbWXCsbuSaaDV33lNrjfX8OBIv5gdsYfkjtck3XdDm3A4l1QwIZoTqbUr59Sdzg4T-SkKPiGmRxtrFb_udwW1_RrOIrvvVSR5Rq1M3perbNlI9xQYKLW3HoGq9w-iJhrktyAMRBhjE7mtEo2f324e8ZKzC5sigFkcBdE4Xal3Ozpe58NjJyZyVdqcy0K9GuFKdQV5vDOKHBLtJWctDJCMIiGF1ePYJuEpa0IHpCidsBYgQLyaMKcvyJLQh1VVriCC-mBKnENXTV7SXx2rGu9KXHkwk7MEEicjYWHNXVNK7oEQULL2y_f7nASMgtyZCpnaeIyxpZJxhFcqEWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb9890865e.mp4?token=DOnn9CBbWXCsbuSaaDV33lNrjfX8OBIv5gdsYfkjtck3XdDm3A4l1QwIZoTqbUr59Sdzg4T-SkKPiGmRxtrFb_udwW1_RrOIrvvVSR5Rq1M3perbNlI9xQYKLW3HoGq9w-iJhrktyAMRBhjE7mtEo2f324e8ZKzC5sigFkcBdE4Xal3Ozpe58NjJyZyVdqcy0K9GuFKdQV5vDOKHBLtJWctDJCMIiGF1ePYJuEpa0IHpCidsBYgQLyaMKcvyJLQh1VVriCC-mBKnENXTV7SXx2rGu9KXHkwk7MEEicjYWHNXVNK7oEQULL2y_f7nASMgtyZCpnaeIyxpZJxhFcqEWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: ما سامانه دفاعی‌مان را برای آن ساختیم که هیچ کس تصور نکند بمباران شهرهای ایران بی پاسخ خواهد ماند
🔹
ما برای دفاع از کشورمان از کسی اجازه نمی گیریم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/692341" target="_blank">📅 17:51 · 01 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
