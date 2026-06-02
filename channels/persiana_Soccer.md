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
<img src="https://cdn4.telesco.pe/file/iWqKpB7m6HaYvoUmd9Z4IhqLKmsoNTnvELS6hLArbZiaRZfT737DKmiBh2FaLlpXisDPkLBfSJQ_9iZLOgx1vF-bAOnD-UEDKU8lVe3jUugp3laC6qg3yepVJSG9iW-9M2d6wZLdGC6cLb4l7AymtOxMpQI4eYfGvV1UidbJm4JF0Fg-_E-FYr8Iqsl2CYx7_pgN49xRbgEKxBcVTTU9XnQe0HZE1uIplHQjKwW6-62Ou_SfRg6rwI-NdBW-V21AUzOYpEAHxWEJF6ccU6DpQKTG_7Zz3ylRVy_Q78QWMQHLMpcPju85ZqnZ2kkpGo3JLRHCA0KUk8iycD5GQKlfSQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 176K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-12 17:23:10</div>
<hr>

<div class="tg-post" id="msg-22669">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXQmvB8rRGTa70FiWUhARawdIOYdfQdD2TFBkeDtQrnCqGFClDxw7Nxw3aP-D1045efENBYVcj2nDHNWM-cOqQLX6Yu7bjulIHo637TGdQ0JDF7-Tk5OFkxLjEYFhThO0a9i5zIQyXXZK08yAjBEuG7iGJ0r_dLblep0WwezxDooA-YnGQ878L3GFPQhEBWjd0hklxrnE-QDJdoJN_GxmTfgrls7IZQyYmmXIDY2Dn4AweIqjzukIeZZZagn1j7li9ktovPVIuDBCr-GMgeHRoVsQJDh4wbW4WzUwTFCx-lhK6XkfywfgI31_6bI2OrUpx-fVT0I5FxS2AqFSF5Wqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سلام و احوالپرسی‌رسمی بین‌بچه‌های کره شمالی وتیم ملی ژاپن، در مراسم پیش از شروع بازی مرحله یک هشتم نهایی جام جهانی زیر ۱۷ سال.
😳
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/persiana_Soccer/22669" target="_blank">📅 16:52 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22668">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bbM46susScVz9xwfdHfStpPR1pP9MMbUWc7ExfqP1doE5auc6JsLtZxAH6PbO9Mg_SvR_jzL5R5n9jhSvYVYJjrAMGvc_rs3kAMd4bYLBJ7fGgknnQUiypf1WcZA8Ycuzx3O5KLQtfiSmD1Y5ccdmVO4F913vaJWlWk6XH3yEIDgEKXaqqhcG2JSq4XBwuPxWXEBizdpDF8A_RENuPb0XQ8HgmCjzLKWGBYGmnrcLstAQPsPRxyA3TxObaqct7Eyh346NROMP66zHrBeKH41rxJKo9_bU0_fBt1NTXFVMAeOJGmRCIBAmpSm7W-ceaLItWReOOyNqRhRvsHcOLz5Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی؛ علی رغم تلاش علی تاجرنیا برای گرفتن مجوز رسمی فعالیت فرهاد مجیدی در لیگ برتر؛ اسطوره باشگاه استقلال به مدیریت این تیم‌اعلام‌کرده علاقه ای به بازگشت به ایران ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22668" target="_blank">📅 16:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22667">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/avG1S1TCyKQ1qwhwtMntvd8riVbZPOGh3D7gOXdN69hICvYevv0ShmGTHS8r3RgcHW64fl2IZmW9eiTVX9yrMpSOOPLmozBa6U6kAIvI6zuJSm8w6i6F6BRwNetacUOcULejX8s9_Xd3Mobb0MPaUusastScIMohEKCJ-BhXxAXGg9U4ms7l0KrdmRKH9irU1sV2A3ziprQWsmX0y_lW2lRTXonIwbwjuDXe9msmKbv5LMDgtvQMzCbGRUfrV-9yMUHzWNqlhxKqRCNNWKHLgehGVML_iXXe4k8FjzEG7AcTDjiH25arnFzaHTaQGuRQkqSkkljjXbC44GU7X-etMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇨🇲
دراقدامی‌عجیب؛ کادر فنی کامرون؛ وینسنت ابوباکار و آندره‌ اونانا دو بازیکن با تجربه کامرونی ها رو از لیست این تیم برای جام ملت‌های افریقا 2025 کنار گذاشت. ابوباکار و اونانا در این فصل در تیم‌های نفتچی و ترابزون اسپور عملکرد درخشانی داشتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22667" target="_blank">📅 16:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22666">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kqxOSyQe5-HgezMYo9hXtEa6Ip3-UI1YFyqOewnHL3Q3oJrElqWlxxIIJ3mPAJf4KsAWWAtrdhfbMtdN8sUwM9VxRRUwpAhgWm6h1cMrGfM6OqE61F-bmfms2vZg2jQYvjXG47b5Lo5J30Dyo1ojZhcONZNc78VWnnILge24KEhvPTr3eERp23pqSYqzRDSkhVmyQZTfFJqmuP3eIdKnQrkUywcOhubaSZga3NvfBkN4QYHXtUqIt0ujQtxYtwmQE4tORNkncmx5GKww1zCWg6JY2xKtfosY2wkgUyLns5R7FCzsOfw_SjRu-3r8XD_kfAJnr9BAMr4mgC933b41XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#نقل‌وانتقالات|انزو فرناندز ستاره آرژانتینی باشگاه چلسی درپایان‌بازی امروز آبی‌ها با هواداران این تیم خداحافظی کرد و از جمع آبی ها جداشد. فرناندز از رئال مادرید و منچسترسیتی آفردریافت‌کرده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/persiana_Soccer/22666" target="_blank">📅 16:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22665">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pzd1ZgESS86X9P6xtO9lUHWZyGSjhWM4Nz9esB1bAZ3lXLotrvJOhAQbBJVTaT9A2FGa2E2zebwhdscY6kFMLvvkA9HvXPglpI4fHBXJOoTOy_YtS-XU2UTVS8W_2wJwT7jk-25eNtEq0xLAt_MsgubuMMEgqIIAGgtrPU0gqa88WDIPViNKnjQsAFBUhPcyBWc5ioEs4P8k-hd0NNpEcoaFWzWzxWUNgtk2qS9V2B474inpADyis-V_x6DwBKxoph-m1dbi89BH61v3NwNGPfLTz4-hAUjLVzR6gClkLU0x-Iis8zdukgxMmDqf-SeY_wn7yYb_K9tpPVmvlvrRdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#اختصاصی_پرشیانا
#فوری
؛
سران کایسری اسپور درتماس‌بامدیربرنامه سید مجید حسینی اعلام اند قصد دارند این‌بازیکن رو در تابستان بفروشن. رقم تعیین شده برای فروش او 500 هزار دلار میباشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/persiana_Soccer/22665" target="_blank">📅 15:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22664">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQ-HBQH4QB2Ts9dMQplU7E3JEORB0ROxMfXMgpRch0TZ1QVRF98v9ur6kbwyJROc5CVajyPsiDA7vg-k7fDwRXg0cOe23oinkUawGXGFOSfklASc8tGRTwkatxKBFPAHSGXakvk2VDl5Ra-gtJ5Xlne3cjkpt2mYm60sZAwwhTzC7WIZ-u-eWkbrdAmykgq4uU2cgmzmJhVnzLLUhns70nZbByGOYvsydHnitDeVA2X31PmZV30umI-rvRD5ivgrUZu26CDo-9eN0D_fMEvj3p83NdPc3QKujgMrhRreE-alYWyhw_g3pbZyyou5P_d2wUI-aWW9y2nPKxRz9PTANA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
شبکه الچرینگیتو در خبری #فوری؛ ابراهیم کوناته مدافع 27 ساله فرانسوی سابق لییورپول برای عقد قرارداد 4 با باشگاه رئال مادرید با پرز به توافق کامل رسیده و بزودی قرارداد منعقد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/persiana_Soccer/22664" target="_blank">📅 15:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22663">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sjxeh6VTeHe6rwfSVON6dOj1w8vfGRAlVFnYRbrmyWmwuyHWTIivaZjrPU_iTf_SpoGEgG7lWfLW8pba2N7Rg1n0-U4fH_TFSG8QySiGD6upVID_KP84NuYIGSigFKR-udGwtgO-Pe3JaNPbnrrC-s9x7rOi_mIHcoOfkmWsoic4Sk6_FDwlS-viXrnxYPP6mDLi8XAIz1w32igo7bwvqHMVwlnZl5xgPNAnSgqvaX6LArNHIHOSYPbFdBXlNGnVB36WOATYZ28D_7zG2E85do9hyoJR4tV9ipTMNa0HHANyavHljyUpaRHaOB9tp871tlxSOfbSvDCBVPH0FIETYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری
؛ باشگاه بارسلونا به‌ زودی با پرداخت رقمی بین 8 الی 15 میلیون‌یورو به الهلال عربستان؛ قرارداد ژائو کانسلو مدافع راست پرتغالی خود را از قرضی‌به‌قطعی تبدیل خواهد کرد و قراردادی جدید به مدت سه فصل با این بازیکن امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/persiana_Soccer/22663" target="_blank">📅 15:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22662">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBbHIIn4AlwDo4Cm27bUmDUZMdpm3RSHaTeSgsQqcCEkhwKAbybk2vrSnEoRoNCktILYfvGtbmO4Bi3yDiDGE9kpF_7Ap5H-_g-QtQQJwOXpDrkbFKn9F5vysfJwFAPqRlJR5gWJd_pejMmhF9eZrBa6nV6sqA9-Tlg38zh-K5_Y-qncXKin5b7Wc95F-tYepxCa-GvEXOfuLm_pJIF3lRNSRvDEZ2D4QzNpy9MRfEpvJJqPsWOAHBqK4NX7jWi_u9rkPt3QG0nVL5i-meEq4lxPWWszvcr-u-pB6vC-__rhYAMcIXmer_ZXgTg-qQ-zYXfiBy8mql39DWTHIeGZUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا
#فوری
؛طبق شنیده‌های رسانه پرشیانا؛ محمد جواد حسین نژاد ستاره ایرانی ماخاچ قلعه بزودی از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/persiana_Soccer/22662" target="_blank">📅 14:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22661">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bYvGi7YBgdqYGn36c2Kzez4TbS19facgEs8b8v0wsh7L832_bdlXtY4c5Q_LfCYCoQ3myFiaRHJY9BmGLkPhGpIxWIyfEOZctJ2SENtCuA9maarWPhMsHZncOHGNa7a8p8Rqq_Y9GC8AQ3TyPD8D1MqZbR7PHAMgc8jntrFWuM4YTK4V3AJnJaZwGjtqHpsZn6DyNUMZD3qfXh11L9UH5qx2Y0KWV5-h6dBGRfsnrfKuAKtD5uHNSyQR71kEwHIUZ839jnKVmwgcuzNcd3cyJipbLW5cSgqtz81pxIfV26W2eXDbwxTD0ti-C3Wgv80m1e3kUd8J-rZ6kjVePucyeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فوری؛ درحالی باشگاه پرسپولیس در تلاش بود که رضایت دو باشگاه گل گهر و چادرملو رو برای رفتن به آسیا جلب کنه اما دقایقی قبل زارعی رئیس کمیته صدور مجوز حرفه‌ای خبر داد: تیم پرسپولیس قطعا نماینده ایران در فصل آینده آسیا نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/persiana_Soccer/22661" target="_blank">📅 14:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22660">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5314c21b9f.mp4?token=Cnoh3dw8PmNW4LT6OQvu5d1dlcVEgcffXpvx5MYxLAY_qRNfr44g6_NUsHAq87J-FTOdFITPKaFk04gwSEwzcVEeRW6S9ZPhrkup8m54tuUEauAFtUF6YzMEeaO-ugE1fgp5D8fr74u5uURaWZZ1NmUhatilSqE1pj58b7B9rWdy-Qeu6YNbRIt-mIW7BpFXdi-3JrLhmWTNiFcZfbdaIWj_AHHZA9SND6qsd7_GILs198n6TEq1KqP88_bkmD1pWcjrtJYVG40GOlzNpfp-MXF7-x3eitO0YeddRcLVlSuBEA9g8JwFZvXk3XUSZbUJ2fatGuwf37Mr_ndlO3q6Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5314c21b9f.mp4?token=Cnoh3dw8PmNW4LT6OQvu5d1dlcVEgcffXpvx5MYxLAY_qRNfr44g6_NUsHAq87J-FTOdFITPKaFk04gwSEwzcVEeRW6S9ZPhrkup8m54tuUEauAFtUF6YzMEeaO-ugE1fgp5D8fr74u5uURaWZZ1NmUhatilSqE1pj58b7B9rWdy-Qeu6YNbRIt-mIW7BpFXdi-3JrLhmWTNiFcZfbdaIWj_AHHZA9SND6qsd7_GILs198n6TEq1KqP88_bkmD1pWcjrtJYVG40GOlzNpfp-MXF7-x3eitO0YeddRcLVlSuBEA9g8JwFZvXk3XUSZbUJ2fatGuwf37Mr_ndlO3q6Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های ایرائولا بعد از پیوستن به لیورپول:
خوشحالم‌که اینجاهستم. به هوادارانمان قول میدهم در فصل جدید یک لیورپول جدید و جنگنده خواهند دید و از دیدن بازی‌هایمان‌بی‌نهایت‌لذت خواهند برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/persiana_Soccer/22660" target="_blank">📅 13:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22659">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mnEwhAVnVZuc6lbcDzZF9672pp29CGWbfyEipEKX1TCGt8X3MWgjRQ0eCQ4IOdPbIz4LvWpVElVtx71gKG6N_FOHQvSRQPax-rttDOTo2QQWh8zKvaZVmgyZ3FgIAoBIrlg2HsAz-4TOgjaRxXYK2o5xPqN3mO3DS16lwbvP7lz6riG7Fqhc4Po1sKHVz3yc9nNR6WxGg7lU5lN_YfBvyCrK8_ZBwm3cLfxsHTmg73oWBj90reSqxpURfIc0C_0PAN-8mLrAvAxyE5zqbVQfnsTJGrxbEZ0oAHzH0l8pROmQX0UAVi1TvuGLN5qrY8ImBb_JEW0B92jjSH0uWEOhGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
علی تاجرنیا مدیرعامل استقلال: برای فصل بعد هم یاسر آسانی درجمع.ما باقی خواهد ماند هم مونیر الحدادی؛ یک وکیل خوب ایتالیایی استخدام کرده‌ایم و قول داده که پنجره باشگاه رو بزودی باز کنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/22659" target="_blank">📅 12:59 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22658">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LD1v5OZnQS4kd0T9q9bFj56j61LWjSCpZ1dEl69NzYtMc2Czc83yt8D0Qt7k2-PuRSpR92JivXwWTmWRrdUUVz4WlnsIKhJ49jn6jl0fZn-3Zvzysm_S_xQLXwLI9cPk0BD_vs4spNxHm3c7YfD5FMD6hKpSFedOtg9uTKIU3aBBZze9Yb8qsoCfoBKYTIpH-8FnZX_o9CYadaqRJjW_IC1vkXeaUJOUWlcxlSt59F4NmtoM622DeMO4m3Ut-I9UPAn9eGxKUMGzL_SpXbCORzzG7coABeaIlmbZWkwVqsA0O4qGHjkmJW3sD1OZsfxa1AfwDonwPcCwV1WpjHFwdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعد از یک فصل اسفناک؛ آرن اسلات هلندی از هدایت باشگاه لیورپول اخراج شد. اسلات سال اولش فوق العاده بود و قهرمانی لیگ جزیره رو هم از مشت پپ گواردیولا دراورد اما فصل دوم ناکام مطلق بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/22658" target="_blank">📅 12:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22657">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d8d6fd380.mp4?token=TX25mho3aJW0abS340mcc1g9YCvrkxZxVm249OlpZwf_JXNtIYZRCRTJss2vquO7BifRtkixzhwVnZ1lTvTAZh-I5KCJkkX-AaU1Nn1zSIA5EeYXzYAV0Jqe2eI9x8vzr-hjUzv4nAJj5wPjLC2L16jnuLmgcR4AECbHPYcFeTpSQVn0aWr9PBITjfygkac8_ixnYAzriOEWtc9LHmeOxGlu4ucXws3HTkQuIplzt2UkVgsuoA4807ROSC269fOJtJM8cBzL0h0uXCgCzSj7sTH88WfDOEbis4LasYS6seqagRFxMWu550dVacwhKh_hb_WBxDnPJnnJKo3QOXCFRmQjjKFaN6dE2YIthxLxioz3IXK1d4olZshAffEXksL_rwCkU3TLMxpDVv00VbP9gUNbyaIvcqS4OuisDHZZHjoeIb4CltckaNfXK3j4bquMt54aYPjv2I6pzWCcehJZnHJ1LMZwaQW0NE_kM8aeLObycz-jxSyPcRkQYN7ELE5E8KHtIUFZNYRnCP24JHZFnEWoPH6yByO0JRJ2xDJSr1kBvj_maPuJqFTIEYqpmu_1JYo2HTkSJI9f651w7CQt1xbU3puLHAZlgk81hUFg_R0Wo0_4xbjCxsqlGvnX46GiteJ0_sxJ6TFTA7uIuPfuyX9tODjU_0mKTnSzUvQk-lo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d8d6fd380.mp4?token=TX25mho3aJW0abS340mcc1g9YCvrkxZxVm249OlpZwf_JXNtIYZRCRTJss2vquO7BifRtkixzhwVnZ1lTvTAZh-I5KCJkkX-AaU1Nn1zSIA5EeYXzYAV0Jqe2eI9x8vzr-hjUzv4nAJj5wPjLC2L16jnuLmgcR4AECbHPYcFeTpSQVn0aWr9PBITjfygkac8_ixnYAzriOEWtc9LHmeOxGlu4ucXws3HTkQuIplzt2UkVgsuoA4807ROSC269fOJtJM8cBzL0h0uXCgCzSj7sTH88WfDOEbis4LasYS6seqagRFxMWu550dVacwhKh_hb_WBxDnPJnnJKo3QOXCFRmQjjKFaN6dE2YIthxLxioz3IXK1d4olZshAffEXksL_rwCkU3TLMxpDVv00VbP9gUNbyaIvcqS4OuisDHZZHjoeIb4CltckaNfXK3j4bquMt54aYPjv2I6pzWCcehJZnHJ1LMZwaQW0NE_kM8aeLObycz-jxSyPcRkQYN7ELE5E8KHtIUFZNYRnCP24JHZFnEWoPH6yByO0JRJ2xDJSr1kBvj_maPuJqFTIEYqpmu_1JYo2HTkSJI9f651w7CQt1xbU3puLHAZlgk81hUFg_R0Wo0_4xbjCxsqlGvnX46GiteJ0_sxJ6TFTA7uIuPfuyX9tODjU_0mKTnSzUvQk-lo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تمام‌برندگان‌جایزه بهترین بازیکن فینال چمپیونز لیگ از2020مصدوم‌شدن؛ ویتینیا طلسمو میشکنه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/persiana_Soccer/22657" target="_blank">📅 12:11 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22656">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kq_fRMdu25rW_DnO_kMF9a_nFTxHv6HqXnybki7gl07gfmbRHGnnb8Zytv9WPvfolWtquQByOg_i8amAez4Fs3y2Wfnc3AY_y9xOr-LoFEMDXDC0oaJC9dzpTrTUo51MGDXwEDEojTqCFVDRDcs3FX1RIbTiil0zesfxT6YAHGP7nTFOz3iWu872o3Vgl6HBzJpZ9EQgKpt4pqGk7sWLlPn-RdLxounOjU-IMnEFI-TNrSplgUF1SQenXqOLXY3SIeCsoPIbcdJiTLnoiTmD50fWkI0FfJBYD22sQGZvtwB-izmHkIUQLZpjUu2rqIGzGyqVb_wvA2mXi2yy7dfzlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
شبکه الچرینگیتو در خبری #فوری؛ ابراهیم کوناته مدافع 27 ساله فرانسوی سابق لییورپول برای عقد قرارداد 4 با باشگاه رئال مادرید با پرز به توافق کامل رسیده و بزودی قرارداد منعقد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/persiana_Soccer/22656" target="_blank">📅 11:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22655">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c58775c3a.mp4?token=h0rfxb0r_VbpOdUebbRrwZlT4JvLf6weAif6ofzkHzPWCjudQZc1Zg9ojzgmfRoRLv8foJBPr-rprN1C24bnAUKiQk47UqvFyJbBji7mamrdcQcQM9rU3Ck8AW7ia2zdXg9Ocoo_3Hi74B_A9J62fsr2znU8Qkhptn0mvqI6Td6ljT0ki1bVB0mgAdrNjCcvAPhFSA-9S2jDCOEVuOQvbISAoAutYsnDppaZFRKXM46p9PK1867_yIVtn6rYIDr28fWHUATZsclGfhiHjQ5wI45-_2muv99FjsAiR6Ybleo7CqMBsn0SbQM8K9sDeLD7_E6sXdId6RJvtmsmFKyY7g-P3coZFJ20UOT7N1O06xKi3gcIfJp8OBnKRzl3NELf2ZwFcpI8WGe9zh8_zeFXKUpIIwSwcSlUJEmG9Qk09qj8uKpEyuhyE7hfiFEi9EOxEgiwndIk-tqE0H7aea8FSbCgOYgQ1oKnqk3FiGydSm-QKlz0jveZUXbTo0G7_7uFu84JutRi_icVyWl2P0amdx5JZ6pIDCizt1tWnxGW0wuBQ4t5G1yMtzH6yT36t7aCKkKPottdeI87Pl0CWuFCMjnB4YC-vF1ZCrT2QRl8i3nqcHW_i1odWU37R3F9YDuTJLvvx_k6LpfTdRVSgaEzagZ2NZuM7wCkh9QwhM_vNlU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c58775c3a.mp4?token=h0rfxb0r_VbpOdUebbRrwZlT4JvLf6weAif6ofzkHzPWCjudQZc1Zg9ojzgmfRoRLv8foJBPr-rprN1C24bnAUKiQk47UqvFyJbBji7mamrdcQcQM9rU3Ck8AW7ia2zdXg9Ocoo_3Hi74B_A9J62fsr2znU8Qkhptn0mvqI6Td6ljT0ki1bVB0mgAdrNjCcvAPhFSA-9S2jDCOEVuOQvbISAoAutYsnDppaZFRKXM46p9PK1867_yIVtn6rYIDr28fWHUATZsclGfhiHjQ5wI45-_2muv99FjsAiR6Ybleo7CqMBsn0SbQM8K9sDeLD7_E6sXdId6RJvtmsmFKyY7g-P3coZFJ20UOT7N1O06xKi3gcIfJp8OBnKRzl3NELf2ZwFcpI8WGe9zh8_zeFXKUpIIwSwcSlUJEmG9Qk09qj8uKpEyuhyE7hfiFEi9EOxEgiwndIk-tqE0H7aea8FSbCgOYgQ1oKnqk3FiGydSm-QKlz0jveZUXbTo0G7_7uFu84JutRi_icVyWl2P0amdx5JZ6pIDCizt1tWnxGW0wuBQ4t5G1yMtzH6yT36t7aCKkKPottdeI87Pl0CWuFCMjnB4YC-vF1ZCrT2QRl8i3nqcHW_i1odWU37R3F9YDuTJLvvx_k6LpfTdRVSgaEzagZ2NZuM7wCkh9QwhM_vNlU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
بزرگترین و خفن ترین کامبک در تاریخ فوتبال؛
بنظرتون عثمان امسال هم توپ‌طلا رو میگیره یا نه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/persiana_Soccer/22655" target="_blank">📅 11:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22653">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65ddfd9ec7.mp4?token=aTyesFYz3k60hBI0PR-36W9okcCiFiNI9_9tAa12eU_aQHv4TZX98aVk4gP7WhgvZyWZIxvt-4p8QBN6x8huVDmNBcUmdgQq7mUlCvhJ-UrAIzh7ODmsOMFCEwK_JkvZF_YfDJpd5ctW1xsypX-dMn7JGNF1ZUUCezZs4WwZ4Oanz7ybaTP72UbG3mH5fco4bXalTavHeek63C_cQyqzkEHUQJrFWjpMUbla5uLCA7ntFCVM4iw_K-FvvOdRwS2OG6NzuPdttwvNFbqKQksl_eb2uWaRq-vUvZoYpv4dXVWdvDn-Oby5fyqQV0vpMUexGO8nB01u5YQhqq6E7RyQXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65ddfd9ec7.mp4?token=aTyesFYz3k60hBI0PR-36W9okcCiFiNI9_9tAa12eU_aQHv4TZX98aVk4gP7WhgvZyWZIxvt-4p8QBN6x8huVDmNBcUmdgQq7mUlCvhJ-UrAIzh7ODmsOMFCEwK_JkvZF_YfDJpd5ctW1xsypX-dMn7JGNF1ZUUCezZs4WwZ4Oanz7ybaTP72UbG3mH5fco4bXalTavHeek63C_cQyqzkEHUQJrFWjpMUbla5uLCA7ntFCVM4iw_K-FvvOdRwS2OG6NzuPdttwvNFbqKQksl_eb2uWaRq-vUvZoYpv4dXVWdvDn-Oby5fyqQV0vpMUexGO8nB01u5YQhqq6E7RyQXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
هواداران خودِ بارسا از خریدهای خفن لاپورتا تو این پنجره‌بعدازمدت‌ها تعجب کردند. لاپورتا به فلیک قول داده 6 بازیکن تو این پنجره براش جذب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/persiana_Soccer/22653" target="_blank">📅 11:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22652">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xs1EnwjQRiPUhlGOBA_7KFfxDRJz_j5PZvwJzY39qgXhV83swW2DdtdL4tZlfntwFOt1uPGC2vqRCmVaBQEatPrzIzs0Lx2Oarx8rzcXbdtKzvr40u9rEdIwb0WYelelvRPkI8YrGm8u2i9j5RLWP7TbrfarWr1idji2QoQPAeJNdcqCCDEUGvT2UWcJj0faizQ8k_gmzz-56OWEr6t5DwtgA16jppvs48hbkIe4qkdfsmMK7Z45MGXUVFQSaRXbyUPqArd-2fNaMXRD-E2-jB7N8_loYH7aIwAP6LFDmPiJwRQS4An4IR7-0qjZ81IV-TFIMhLrJshbjwiHepp4Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
آرتتا سرمربی‌آرسنال درفصل‌آینده پرمیرلیگ تنها سرمربی‌ای خواهدبودکه‌قهرمان این رقابت شده. همه سرمربیان موفق از لیگ برتر انگلیس رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/22652" target="_blank">📅 11:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22651">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">⚠️
خیلیا نمیدونن که اگه ثبت‌نامشون رو با لینک زیر انجام بدن...
⁉️
💥
بونوس خوش‌آمد گویی تا %220 بیشتر میگیرن!
فقط کافیه به لینک زیر مراجعه کنید و وارد ملبت بشید و به راحتی ثبتنام کنید!
👌
🌐
لینک بدون فیلتر سایت معتبر ملبت
👇
🌐
www.MelBet1.com
🎁
بعد از ثبتنام، وارد حسابت شو و توی بخش "بونوس‌ها" فعالش کن
🎚️
نکته:
فقط این هفته فعاله، پس از دستش نده
🙂
🎁
کد هدیه 100 دلاری فراموش نشه:
Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💯
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/persiana_Soccer/22651" target="_blank">📅 11:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22650">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TAn8vhCyXwnFuIuXaU3zcI2XlqBQQ4F01-koPHWciDC4WqjwzMFl_Kuu45DDMy7jsfppB2qS5ETJxZ4aAMsVeinb-cAHOrqXoQ2LVkOuCeZQOXni5SMtEDNHHxyNrW1EPAJlu-ypdLQO7fY0jRo8AGmnmTZ1QC5EO6PjiKcnefsc56KxQdlyFgtWwA4rgpgtB0Y9VIBMdeLtaQ0maGZjvRwsLfv6GycEdCXBFKepDg2-JqS_Wxt5Xtko-k7GtBu-3xYpab1QCmGeGKDKhlKwFs-0o7xzYWn6B3R5iSom0BeVH0avekZlogatBZf9MaY_8fP8-_0b45N-T6rKbYNq8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
ویدیویی‌ازسوپرسیوهای‌داوید دخیا در مستطیل سبز در آستانه تولد ۳۵ سالگی این گلر اسپانیایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/persiana_Soccer/22650" target="_blank">📅 10:52 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22649">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZaOHNvDT-Y-0KJhjWsgphlRduDHKEYxFqfEuz8dW4OmRGknGovcTmreZ6qwTwo9k3MJheS1TFNpUOGRTftYG1_IzCFvB9VKgjWBZgEaTOx0U2_fqZFHlNutEox7oeVudCcz-UC_Ay_c4J2fYROLZFKQvU5qSO7RnX6pliPrwWy4o63SIwqMW1F7J5_x3JN9OJxqe4n9LavKPZs8fBZC5Urv9Z3tD7VpU0CJhn9wDIKUJcYzLQyWoDFSGW5io3_wPdIZgIvnftXVRyZvidu0KIOqgPSCGnf3dBhyYRqJmwk2hhONp2CniW3Q9LirreKYzb2LzKSO903EB8PgP4_ADoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#نقل‌وانتقالات|ادعای رسانه‌های آلمانی: هری کین یکی از سه گزینه‌اصلی‌ونهایی‌سران باشگاه بارسلونا برای جانشینی رابرت لواندوفسکی لهستانی در خط آتش آبی‌اناری‌ها برای فصل اینده رقابت‌هاست.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/22649" target="_blank">📅 10:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22648">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ab78a2ef5.mp4?token=aZcj0E829EIQ4QtQZ5EIt3XdrGrYj4vtpUtfgb67Bh30BNXigXhlYicQQjRprHsUi39XYnbyAKK30IhEUBD_TzRsPtrhJBUtmIMWfQ0ENZPUBJclq-AD81TawxCVrV2vIiB5Ou3h_DGSHW0g0K5DrugP01rTBgkleZX__zwWDWo5y_v15P49gwFaR-0OproDQJ_GtMTPw9ciqJ2oUyI3SdlGBzAxk9CAKDmMcgHpyUHCKsmByXSln1AFj5FDQ9ZKXo2Y6H8P8tZgnlq1mmrRU4ORCzK5DYWfQrW4J14x53WweRPE7IIp4tWGyMxdmuVPVP5REcLyo57QshE_5pW-Sy0aUb5AOeNjeOPgfXTBK4fgR1NKJQBbi0aXd9JE0SjOLbXZzuTHo4DTVhymM6H-1pKirY7UQiAY6ncjLQn6JiiuDFVOUYIw_jWjMqzKlpJhp0lFaSB3oTumecRDaffjHbrmIVC2uvBgoRF7iqo2-mv7yzvOJT-fwVKDYue1LKTioKJBNALQSTZ8nS-JJtgi1RqQGqoMof_BG9VTI_z7hwIEc2o1Hq45u23vTwhgrDS-8Dq5qKg-oC1E5qlmLwbYVifsZxNhLBuovAWlqA3noMkm0j2vrLhxFT8g1pcu2PHMZSgtbc27oSNSNCpgsQTl2jWx9brPiNKwgDk1w3QwB1U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ab78a2ef5.mp4?token=aZcj0E829EIQ4QtQZ5EIt3XdrGrYj4vtpUtfgb67Bh30BNXigXhlYicQQjRprHsUi39XYnbyAKK30IhEUBD_TzRsPtrhJBUtmIMWfQ0ENZPUBJclq-AD81TawxCVrV2vIiB5Ou3h_DGSHW0g0K5DrugP01rTBgkleZX__zwWDWo5y_v15P49gwFaR-0OproDQJ_GtMTPw9ciqJ2oUyI3SdlGBzAxk9CAKDmMcgHpyUHCKsmByXSln1AFj5FDQ9ZKXo2Y6H8P8tZgnlq1mmrRU4ORCzK5DYWfQrW4J14x53WweRPE7IIp4tWGyMxdmuVPVP5REcLyo57QshE_5pW-Sy0aUb5AOeNjeOPgfXTBK4fgR1NKJQBbi0aXd9JE0SjOLbXZzuTHo4DTVhymM6H-1pKirY7UQiAY6ncjLQn6JiiuDFVOUYIw_jWjMqzKlpJhp0lFaSB3oTumecRDaffjHbrmIVC2uvBgoRF7iqo2-mv7yzvOJT-fwVKDYue1LKTioKJBNALQSTZ8nS-JJtgi1RqQGqoMof_BG9VTI_z7hwIEc2o1Hq45u23vTwhgrDS-8Dq5qKg-oC1E5qlmLwbYVifsZxNhLBuovAWlqA3noMkm0j2vrLhxFT8g1pcu2PHMZSgtbc27oSNSNCpgsQTl2jWx9brPiNKwgDk1w3QwB1U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روزیکه لوئیز فیگو پرتغالی به ورزشگاه نیوکمپ برگشت اما این بار با پیراهن باشگاه رئال مادرید که هواداران بارسا به این شکل از او استقبال کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/22648" target="_blank">📅 10:09 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22647">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jj2nx5i8PsC3_ZgmSW_PNF0jVGwL-TdsfV106GOsTCATCQnPRW0xwG-WzgyIuXOFJ1sIqEojMfVYZyivc6iercVci-waX123GdPDw--xqZvYsAhWMLvOZVNnLU2aKbJh0RMdviN7uLVbeGyvU1rg-jbj3Dy-U5YuRoBYQGmoLWfqZmAgzEw9tkIO5apyw4XNt31JH7QUqYfuZO2WUtOhkh5ygyRbhz06Od93hM8dbPMPDtUkqirxZ0BIwU1zseQCTmsFZ4ZWesZLSHo7I_tEmPb4dQOWvbMoKHqYHpN8zjmnYtskDLb1uSEDaPQbKqxltx0sla6X4p4rGloCOU1eow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
از پیرفلک تا شاه کرمی؛ اسامی لایسنس نشده‌ی بازیکنان تیم‌ملی ایران در آپدیت جام جهانی EAFC 26 با نام‌های جاویدهای کشور جایگزین شد. حرکت غیر قابل انتظاری که EA آن را انجام داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/persiana_Soccer/22647" target="_blank">📅 09:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22646">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6Yd24U5AtNm6TlRnH94QcELxZoOQV_QU-XHUW0LWDk_zA6GharphGYBh8wT4lowysyT19M2oL9ey1kOTqh6lMF0yYz-frCcRPpOBvUk3eSdtsCns9et2IXr-3jesS2KaokRPeBV11LKJ4iWafO5oQ-FICT6U64ngmieV5O-8KjyvKvCeCJObabTrjbFhDd7j4RZFLI-ebZHI56eX2sct-Rx5vlkqnE-IEcqT-zFhsYt4Oyfnv4LFM8EkenkUxtLjDCU2Bhme_E8a6xVkduVZcoW4iCZW8hJfNL8UsxwwvhKV2SYG36qvHv066n9Nk_yaONYClaL-KL71vaL_jwthA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ ابراهیم کوناته مدافع تیم ملی فرانسه که‌هم اکنون بازیکن آزاد هست اولویتش پیوستن به باشگاه رئال‌مادریده و درصورتیکه آفری‌از سران این باشگاه دریافت کنه سریعا پاسخ مثبت خواهد داد.  کوناته از پاری‌سن ژرمن و الاتحاد عربستان افر مالی بسیار سنگینی رو دریافت…</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/22646" target="_blank">📅 03:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22645">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lzinCT8NRko_Z6FY5TpJwJXNU-Gy5pcwqrcDKFohTK3ASdOJmxBD8WZezGhCS3SDtZYRUcr0pbSSYswYV1X1_yoEDcrZNaZEBzg2K72hwHMuv791s6dxlIuk6jKgUrfIzONF8zfwhMbL0eD8O2pusatqCEB-cSb_GcasWv6BYv73E2r-8qn94eGL8z6wnIjL46RsKHRfrSRSo3XoHXPCXlU8TMXXRqPc7LxClV3pjzvpURo5303rU6tPzpit-Qa6_CxRZNylQr9el5JBlbs8RRi08Rw-K-jCLbNlh1uaupRFhOXS7Ru3wrO8l-AQPXKRnwJ_02h6xaqCSqeikcOJNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
دیمارتزیو خبرنگار اسکای اسپورت:
بعد از جدایی دنی‌کارواخال؛ سران رئال‌مادرید بشدت دنبال جذب دنزل دامفریس مدافع‌راست تیم اینترمیلانن و میخوان تو همین پنجره این بازیکن رو جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/22645" target="_blank">📅 03:14 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22643">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T2fMSPi1P08woO1Enu5q7UVXmljTJifOAc7sVPKfzUOOoyXwKM01AdiRKLImT7UBVtSpCCOssudwDdP6EUIjWqi8O3HHxFTMUu-A4coXOWR3Zn98BTfZBXMZbhYyfgRhMZmRXAsoqghTd00T7nCavBmu2H_sQXcPSjaZyUaIE5D-XZlCXrI2KQTuxHjxDZkdX3i2Kmo6LFhg6eDWV9yaT1bprlFEbXKbU5IZaPts0zeYDZxvbjspQGLq9fjGesfd_JPk4zSenncH1BDXWLWEUp5Ml-XZICG-zFsiR_HxYMcTH8T0G98o4jc7z63c-Ruobr81oaut2vfKXlmUsyjBrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FPVmY8Gv_Co7GCNwCirycuYaMYMHyAtWEK_s1yUxfrhktsn6AiW6k37t-2ihKDgkoRl8JAJtuTAtRd-AdKRPKDgjr60cw-gdm7pkIAcjlWjtbgswWHU8IMSjscm8B9R-B_1zMC-i5Im7zQ5Wuc6qENccd4TDuPKTFQ8KMsCJknOPsIGrrE__N3SMBctk5O8NuYG5Aw9Jyiu0QYRfbVwNjyZArW8cP6jaTqkaN0DYE1IVrKV2FDObff34MBIoJC3lx0UXVU_WxqpfPmY-pSI3stZYDcVyOpokk9-jxhKSCvUZdPlfENE9NNAiRTHb-I4pM1SRvbUw7dI8gOdsNNRjRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
🔵
تاییدشد؛ مدیربرنامه‌های فابیو آبرئو ستاره آنگولایی‌تیم‌بیجینگ‌گوان: در ژانویه مذاکراتی با یک باشگاه ایرانی‌انجام‌دادیم‌اما بسته شدن پنجره نقل و انتقالاتی این باشگاه مانع انجام شدن این انتقال شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/22643" target="_blank">📅 01:59 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22642">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/282d7b4a2e.mp4?token=CDYdGDR5uHwUZEkJE3MtO2TTPB1TSyZJ6GAi6RvI7VHk3D-3uLJJUsXjxLsPL37ahUDEuPl5OJhPHXjV6ZDMlIqcTWcJhSzjOHhBrcLyGCX0uyt_Ogatl8Og2HorJZF4v7ns86-l5K_MzbMU98AhL47iYl8orC30fZPGUOOawfyMIkhDExRVh57cnMtXxaPZkVgDAYJfmy15hIR3HgJTR8pckrbndiXXRD8ABO9kZw-EwAKmuRp066jxTdeQh_P0qqpd3jJNHZE0xLhFgmjBPbI_3z2olWEJfent-EFiqfrnDlXS1kpWAF6aQpJGnigCEJFshaZPmV_TmasEHoZJxIFrwUil_Wkufekk8VLfwJKalgVkbWB-6ikEHRDL761EZvKVBVoJ_vPoiiCTTB2ujmEaF2EfB7F84d3kAmPaoPfDXNdDapM9_xg74GWQY1OdbINaQ0BUMiWtL0IeSdzJhCNg-IyT0SjEKOECvuXocR1MCWWjs53ci85pHVwmvQG8TfqXc3nXGqZcsuTjGN0ZNvYKuBuITMuuumtkdNqfXC4n0fNMjFd1PvxXoI6v8ybf1CwESaduu5BcRpll0fLdtPu8KlJIMgXVnC6e5j_Qu1V9rl1tQHN-4wQnfWOPmNxuN8X4xkOT9VR9Zl5PBoYnpdPW5wBo7fk6AykVBnZ2Mbs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/282d7b4a2e.mp4?token=CDYdGDR5uHwUZEkJE3MtO2TTPB1TSyZJ6GAi6RvI7VHk3D-3uLJJUsXjxLsPL37ahUDEuPl5OJhPHXjV6ZDMlIqcTWcJhSzjOHhBrcLyGCX0uyt_Ogatl8Og2HorJZF4v7ns86-l5K_MzbMU98AhL47iYl8orC30fZPGUOOawfyMIkhDExRVh57cnMtXxaPZkVgDAYJfmy15hIR3HgJTR8pckrbndiXXRD8ABO9kZw-EwAKmuRp066jxTdeQh_P0qqpd3jJNHZE0xLhFgmjBPbI_3z2olWEJfent-EFiqfrnDlXS1kpWAF6aQpJGnigCEJFshaZPmV_TmasEHoZJxIFrwUil_Wkufekk8VLfwJKalgVkbWB-6ikEHRDL761EZvKVBVoJ_vPoiiCTTB2ujmEaF2EfB7F84d3kAmPaoPfDXNdDapM9_xg74GWQY1OdbINaQ0BUMiWtL0IeSdzJhCNg-IyT0SjEKOECvuXocR1MCWWjs53ci85pHVwmvQG8TfqXc3nXGqZcsuTjGN0ZNvYKuBuITMuuumtkdNqfXC4n0fNMjFd1PvxXoI6v8ybf1CwESaduu5BcRpll0fLdtPu8KlJIMgXVnC6e5j_Qu1V9rl1tQHN-4wQnfWOPmNxuN8X4xkOT9VR9Zl5PBoYnpdPW5wBo7fk6AykVBnZ2Mbs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
#فوری
؛ درحالی باشگاه پرسپولیس در تلاش بود که رضایت دو باشگاه گل گهر و چادرملو رو برای رفتن به آسیا جلب کنه اما دقایقی قبل زارعی رئیس کمیته صدور مجوز حرفه‌ای خبر داد: تیم پرسپولیس قطعا نماینده ایران در فصل آینده آسیا نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/22642" target="_blank">📅 01:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22641">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SazvkCDFlb422mdvvuD9_0S7MnMwPfM7R8ggwpkTA-1iBRYxYhxb3fVb21xZZC8rSquxXpTsG5GkAAW1_OKD2fK4e1pjyrvNM5kNzx1rOc564nwg6uBrc9HAKQxwwq9H2bSAv30-ipyGvwql0sxI9Ki-RPg3Ugn5L6P4-_yjz3r6rqX1KdLkmJAICoEDjB1g5R6lGQiTO509xn3ghAWaeG-71_Bt9qkaFVkhZROhRFfqLZTl-6xjJnaMkvrCpG85e1LLhbLCYDyfwbTkwBLLcUX-V5TQaHYEjy6mknKnZQu_W_acxK3BFgF8iI5TH0JvZOSdH2-0J6GFHaEKtAFyng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ آخرین خبری که درباره وضعیت پنجره نقل‌وانتقالات تابستونی باشگاه استقلال گرفتیم وکیل ایتالیایی به باشگاه گفته کارهای اداری رضایت منتظر محمد انجام بشه پنجره قطعا باز خواهد شد. هر خبر درستی از هر باشگاهی بگیریم میزاریم براتون حتما.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/22641" target="_blank">📅 01:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22640">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df595076a3.mp4?token=Oj361Ppog8MB0JOd7YixPPloTuyqLEC--DMNbMkjyhQws8CEpgiFgBXSzVuEDQ5LrKtC6n-yZv2c1dHuLSKdzL4i7AIvpPzqP7JpVxIVkDrK-if66YnxMKgpYAGQ5bNxiOeYMGUEeP4SAe4vB_bxqJUakZPF3n1Jf6G2UUTnptI74Lomjv3l6_cawjt79dYLdRgrWLWP7HfbJBEZhUIPFm4Mv5gIC6qFmsfUnZ6w8iAwmtkXlnnxBvQzqQf8nQcgj4ssttnSf5jBg1v4x_a6nEoNwtMIYWqEajYuiTdAOWD62snBx9baIiO-PtZ5gEaum1ATdUq3AoyV_gAHUra21CsazUsMN2qSjHzlIP1VHicdn7mrCoYHeR5eY4Yq0jYtvSKpYluCqK_GIUJewzXahc3Da01mKDRiDF7x9hQRK9cVsNUrZN66-qDYS3YCnAqUn3FkL2GpskPvhRPIA3dhfneiT7Dtu26mV-IYJe60LvgSz9NErpRkzMHfbX1fYBC9eBIRUzgcAvYatURv0VkVzeznwClZCMOGVGeIw3EuQ8DrF-wA-pqPTffeiWKO-V2a7bI1ehNJ_oCdd-N_JvSkecacU3E7Fxh-6tRCenk6aJFZwCYeU3RywX_emtE3l8Ciz62jQdpImSxoMemcLwABNRlOxWRmeIpKipBPi8Rz1Yo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df595076a3.mp4?token=Oj361Ppog8MB0JOd7YixPPloTuyqLEC--DMNbMkjyhQws8CEpgiFgBXSzVuEDQ5LrKtC6n-yZv2c1dHuLSKdzL4i7AIvpPzqP7JpVxIVkDrK-if66YnxMKgpYAGQ5bNxiOeYMGUEeP4SAe4vB_bxqJUakZPF3n1Jf6G2UUTnptI74Lomjv3l6_cawjt79dYLdRgrWLWP7HfbJBEZhUIPFm4Mv5gIC6qFmsfUnZ6w8iAwmtkXlnnxBvQzqQf8nQcgj4ssttnSf5jBg1v4x_a6nEoNwtMIYWqEajYuiTdAOWD62snBx9baIiO-PtZ5gEaum1ATdUq3AoyV_gAHUra21CsazUsMN2qSjHzlIP1VHicdn7mrCoYHeR5eY4Yq0jYtvSKpYluCqK_GIUJewzXahc3Da01mKDRiDF7x9hQRK9cVsNUrZN66-qDYS3YCnAqUn3FkL2GpskPvhRPIA3dhfneiT7Dtu26mV-IYJe60LvgSz9NErpRkzMHfbX1fYBC9eBIRUzgcAvYatURv0VkVzeznwClZCMOGVGeIw3EuQ8DrF-wA-pqPTffeiWKO-V2a7bI1ehNJ_oCdd-N_JvSkecacU3E7Fxh-6tRCenk6aJFZwCYeU3RywX_emtE3l8Ciz62jQdpImSxoMemcLwABNRlOxWRmeIpKipBPi8Rz1Yo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
وقتی درواز‌ه‌‌بان‌ ها حوصله‌شون سر میره؛
فقط ادرسون که‌گزارشگرم گفت بی‌دلیل نیست پپ کچله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/22640" target="_blank">📅 01:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22637">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0yjSFZe0PrRXSLISl1lkJ3mpfvfo2claqztvDejI62gVKRdBSLgX_NCJJxGyxsZov2SmPbRNszv4sYwSvX-xnF9u1jrRqnJxmPCosfUKxyAzY1N-fXunkeDK1GQWjbXmk2y0MBebuR_IeCimju1-hzFWSVfxN0Qv6gzeDYIFGm-ibjdYdFjOo972ev_mBYz-8GSmuoH-DrocQzpJ6QEIo7PrF08WFvrWr2PJHR2OXhCKrFWvQRiDrIECNy710n3eIwZb6nUs2z1vvorIHrzre4wv-_U_E7UZhC1UIF9hlTMLi7_JE23Fq1lSjwjVugN-zdN1H6vzabJRe8Owhh6Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ مهم ترین دیدار های‌ امروز؛
نبرد دوستانه دوتیم کرواسی و بلژیک برای آمادگی در جام‌جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/22637" target="_blank">📅 01:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22636">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MI9J9bO3NERpBLCJVOM5In8zE-PtE3RBOfZT-KgPtuFpm-BRlSoH5BtOY7WNyicdMTfP5Dl_E7S_Iqca8BDmUCGzUpayXuljN_47K1E_fVnvU42TXjc5aIhI5NcQ-9PdEaI-liKF5VA7cTbwRPqIfR5o7oRWrdgg9ciJ2Nnxm3XXe49wLgJ5mAQC42shbNNoBKXzoX4jGDmLO1E1kp8XQ9EhxHyLJ13lCqPcAzTrJMrOusF5Ddfuoc41AxjrVrY_mc8Kt0F-kJTORrGE78rGFYNGkfFg76IJXSVKoT7LPXQ6rOIwMkk0OzqaE-txqXKQUQexeAVJKrDJgg3kV3kfMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
از برد پرگل و مهم سلسائو تا برتری وایکینگ‌ها در غیاب اودگارد و ارلینگ هالند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/22636" target="_blank">📅 01:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22635">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31b893cce4.mp4?token=HBd_R1qfzMgBGWlI1Rcz1pSkRX90GnVB5QZLpTCqGQ286zag-9zxKvsTHAacKIA8xXx7yD80Ou97asVAe_jlqqTenhUYDRdJPfYKTMDj8_z4ZQ_fAe0jUDTn1AFYxeMectYxuCgJvZq9rJWAcXzj1ptQ3q9EqPIZrgOoJhwWtIlQ17S3byiLJz40I6K02dRtE-gONgI3Y2klJ4I_g4Cztqkk7485yXSo5TRp-e6sBeWOO9XYbAbjsfEbh1cL3F1iERvDvKX0MA2iPwz1H9HZI469IaxCbYPSYaxPaIDFSRVTdxfiFokHJiEndQ_KomvDliXYU4RottK8xFDPRY8-RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31b893cce4.mp4?token=HBd_R1qfzMgBGWlI1Rcz1pSkRX90GnVB5QZLpTCqGQ286zag-9zxKvsTHAacKIA8xXx7yD80Ou97asVAe_jlqqTenhUYDRdJPfYKTMDj8_z4ZQ_fAe0jUDTn1AFYxeMectYxuCgJvZq9rJWAcXzj1ptQ3q9EqPIZrgOoJhwWtIlQ17S3byiLJz40I6K02dRtE-gONgI3Y2klJ4I_g4Cztqkk7485yXSo5TRp-e6sBeWOO9XYbAbjsfEbh1cL3F1iERvDvKX0MA2iPwz1H9HZI469IaxCbYPSYaxPaIDFSRVTdxfiFokHJiEndQ_KomvDliXYU4RottK8xFDPRY8-RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دربازی‌ایسلند و ژاپن قانون‌جدید ۱۰ ثانیه تعویض اجراشد و بازیکن‌ایسلندبیشتر از ده ثانیه صبر کرد تا از زمین بازی‌خارج‌شودوطبق قانون داور اجازه ورود بازیکن تعویضی رانداد. به این ترتیب ایسلند بیش از یک‌دقیقه تازمان وقفه بازی ده نفره بازی کرد و ژاپن درهمان زمان گل پیروزی را به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/22635" target="_blank">📅 00:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22634">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J42U-wwt85xhWShxBh8V56oJybXYCzZ-9HrPgggp2aIbyDdLQ7ZNTvj10A61Pb3sufIxwY0VlJxUb1oygB7-2xoIXnO0E0quxfKiAmikmi3mFY4NiaM0iEfVZgQc9yy1ZhthV-ri9JxkD0yl2WEVIK0HfXyJrJfmy7ly6AT3oXOz8cENJL797NrRC4THtor64ISUyy0ZazhrCKsVWUkeSVUm8bYWFo1fYCxwGoidhS-b5ov2dZePL4UUgqOBqkjadwOM2HKwJL8JZ5Lmt7Dz1oEzbFxRJgk64_gswCYKRBtSm1AxGrbocxbKYgX3Z-R-9ZaF8RMT5k9dkgI_rsrf1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ظرف 72 ساعت آینده از لیست اولیه اوسمار ویرا برای‌فصل‌بعد پرسپولیس رونمایی خواهیم کرد. منتظر جوان گرایی و عوض شدن شاکله سرخپوشان باشید‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/22634" target="_blank">📅 00:31 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22632">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRbBnZZNHFTGa--ZizF57MKWYw1ZnFcmQR51mvuMe_QavcrOTWJ0zbppTDYwuAewoJ-94GH31uQ35J4I_CVVB4UbHBnjZhpfO5JKVYkeKocxSCGw2XICJshqugKbjuVVbgJg_yX53hpy7UXvz2yngVND9mKXN3WPz25QPk6Jnzt-EnSVUdfAZcvJSYKUFeKafQmbYGXphSaM1eBK3fxBZdPqBRXCXRNkTBMoSnRDD1WrDIOLmkg6ZtCgPyZEyfRLoLhz80S1X_fGt9xIb6LpEAgZU9U-DKWwdMYWo5AACdnPDFP1oRHpHCxERP4wiVXEslTz09CUzR28MvT5ZsnHVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d165d6a89.mp4?token=oweQ4XkjEQyqGEEarJorKd9hIQCFP-BKGvXaauqGBTFZIt6rXTzzFkm2k6u8CN5cassoW-esTg_nM94bSdXxFoAgQtb0eSAJarbbNIdyD-PmkS4XnmjdUQoRnal4lUPr8mJ1M-j2oPlAUqaEBjfutpupCQ3hfJ9k3gLDuJ1KyzdufefVtPRQcXuqWkA1FCCNgpJsmtMmdQfZfQrHpj3X2tkL20DPOK3uYyfisCS4QQSJOS1l63wvk6GQ8onK0VtTWnFHh2IBv8-fCDSGVZGx46OXduQ16sQUAjiux_LtSnfWwb4JdphkQYCG53WbSECzPwHjVvTNDJH3Jq4Vy9d58Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d165d6a89.mp4?token=oweQ4XkjEQyqGEEarJorKd9hIQCFP-BKGvXaauqGBTFZIt6rXTzzFkm2k6u8CN5cassoW-esTg_nM94bSdXxFoAgQtb0eSAJarbbNIdyD-PmkS4XnmjdUQoRnal4lUPr8mJ1M-j2oPlAUqaEBjfutpupCQ3hfJ9k3gLDuJ1KyzdufefVtPRQcXuqWkA1FCCNgpJsmtMmdQfZfQrHpj3X2tkL20DPOK3uYyfisCS4QQSJOS1l63wvk6GQ8onK0VtTWnFHh2IBv8-fCDSGVZGx46OXduQ16sQUAjiux_LtSnfWwb4JdphkQYCG53WbSECzPwHjVvTNDJH3Jq4Vy9d58Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اول‌برام‌سوال شد که چرا بازیکنان پاریس همسر مکرون رو اینجوری نگاه میکنند، گفتم حتما خیلی خوشگله و رفتم گوگل عکسشو واستون بذارم که با این رو به رو شدم
🥸
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/22632" target="_blank">📅 23:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22631">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QqGXmlqUwWfd654xmoPmTBsrHHzbJs8kKgVWmcRCI-rNmRBwRvzkjvIFYBe7iZi_X5xjDJOJ-fVsnZ-QgpDpMUp9NSrTKUEqBEG8zGtujOngMGeiEX3bP8la2NMBLzXcJa36CSsq6oPBTUJ-wzOMTZoWkWp9N3VuqOo4M1E0mykK6JWy5zdtKeOEz3YqPsIix_DxZ031gFytubOA1IkRpX_at3FLh2P6WBU6ajIPJFh7_kRGx9fdtHqMkkeWYtzxTSiBxGAzmmDK5DnJIPvlnlfbPFgMOSgjZIQ2B_9MchiIZwH18HTLlIQtavGq8KWeWKoEevnNkGqYxXK6u4QTOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇸🇦
#تکمیلی؛رسانه‌های‌عربستانی: باشگاه الاتحاد عربستان اگه بخواد سرجیو کونسیسائو رو اخراج کنه باید 25 میلیون یورو غرامت به او پرداخت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/22631" target="_blank">📅 22:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22630">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQb9P_zggrCBAOBBWeMmNGD2ZKRI8XzFcj4rRFIiUAOA0mUhz7-I7CUfPg-leeTAqDQWAjLoWf7VPZ19KUgOYk80cPkR2way8IW0Yz9jMwE0qI3xSWeHFUgzby8KZG_Ai5aXUWFJtIclxRz_Zk4Gipnqigtwge-WlWmGMJ7q8D_Co9WKKbN0jrJ-xyar4lVFB0juRc6U7lotvfFGDSn1bntR4IeV_phirzrvMeieZloAPbF_rGKXDHHmq4gvQgP6EURZnEKkeBsmqmzzmTMgQ4IAZg63wuKUyiY_clVJLPR9mAgexOYeP1N_oPItGVeBflyycR9nvcUNDTwYMIzaGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درخصوص نحو سرچ فرکانس شبکه‌های رایگان ماهواره یاهست‌سوال‌زیاد پرسیدین. روپست ریپلای شده کامل ویدیونحو سرچ فرکانس شبکه مدنظر رو توضیح‌دادیم. الان‌این ماهواره‌خودمه شبکه‌ها سرچ‌ کردم مرتب پشت سر هم قرار دادم که هرکدوم رو خواستم سریع پیدا بشه. تموم این شبکه‌ها…</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/22630" target="_blank">📅 22:25 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22629">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4344a08e8.mp4?token=P4xwAiCZVwhTpkhYGQCUZutb6gWcp2FIMf2McDmgsM7gNO4ur944zM9XivtlQmgFblUsdhjtx-FOL326pkDSsPphiFvRBMki2NZmZJmq9j5UsWU1RUkK2Y_KiIkv70gLBw54CTUl8Utbvc3tmBoLqr7utH-ald8rZHKtKbrFVfXfesuAOeB68CRRcgf2eO_vrMMDPEwas1buAGYlDpR5BrYTBE12A-SytrC1P4mvq3s_lIwaERIjNTj4s958wS2ld_zY4N6N0uvhhsFGooEhofbfRtVUE80aAovI4k8AX5_LXrUqmjNOVRnJpKvOVWjjEmCxCCZs2sIWtU3UjenGSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4344a08e8.mp4?token=P4xwAiCZVwhTpkhYGQCUZutb6gWcp2FIMf2McDmgsM7gNO4ur944zM9XivtlQmgFblUsdhjtx-FOL326pkDSsPphiFvRBMki2NZmZJmq9j5UsWU1RUkK2Y_KiIkv70gLBw54CTUl8Utbvc3tmBoLqr7utH-ald8rZHKtKbrFVfXfesuAOeB68CRRcgf2eO_vrMMDPEwas1buAGYlDpR5BrYTBE12A-SytrC1P4mvq3s_lIwaERIjNTj4s958wS2ld_zY4N6N0uvhhsFGooEhofbfRtVUE80aAovI4k8AX5_LXrUqmjNOVRnJpKvOVWjjEmCxCCZs2sIWtU3UjenGSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
پرس‌ سنگین برزیلِ کارلتو در بازی با پاناما؛ حتی وینی هم داره زیر نظر کارلتو وظیفه‌شو انجام میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22629" target="_blank">📅 22:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22628">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ca84e9f76.mp4?token=vKFWy0JJ6SuyaCW_ycIrthWkMo65oeTOhf76iphxSj3PlnlTm16RXBrE94lx-BSBO-QiMPOQLY_jsWRmUVyGxyA3Ecav19-KGHC9H_6zTFOdgYpfeGtpTQlNehzfjmVSi3-kmWVoM3kusDCk6kFlIx6w_MTaX3Y3KisC4-K_u68ZFmSu9oVEVBOaQMZTm1J-zcmzw9y-vBBBV25HX7aUssjPTfE4-9He_WxqP7q58m2aK_o8qO7JvXahJ01zMJ6wEpsM9azt1zOq-HFo5uwHAz2oWw60LCswTFmNLogFnNRER0q5P6tOEd2X8KQWpoCfNVJa-vmFsk-4StO4pUc6xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ca84e9f76.mp4?token=vKFWy0JJ6SuyaCW_ycIrthWkMo65oeTOhf76iphxSj3PlnlTm16RXBrE94lx-BSBO-QiMPOQLY_jsWRmUVyGxyA3Ecav19-KGHC9H_6zTFOdgYpfeGtpTQlNehzfjmVSi3-kmWVoM3kusDCk6kFlIx6w_MTaX3Y3KisC4-K_u68ZFmSu9oVEVBOaQMZTm1J-zcmzw9y-vBBBV25HX7aUssjPTfE4-9He_WxqP7q58m2aK_o8qO7JvXahJ01zMJ6wEpsM9azt1zOq-HFo5uwHAz2oWw60LCswTFmNLogFnNRER0q5P6tOEd2X8KQWpoCfNVJa-vmFsk-4StO4pUc6xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
هواداران خودِ بارسا از خریدهای خفن لاپورتا تو این پنجره‌بعدازمدت‌ها تعجب کردند. لاپورتا به فلیک قول داده 6 بازیکن تو این پنجره براش جذب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/22628" target="_blank">📅 22:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22627">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🔑V2RAY-VPN🗝️ADMIN️</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QiJlXQ2Nqtu7We7c3aexc6Ls10_FG6N5xDiiDb36liAS-huOBGuLCrQq1Q5SLlxrhV8_jUqujovEf6nQM_E_7H2y-6rHLK6ruejCwaMhOM9xT6NKBbBSli3XGMb84NCvgPbhA9YD5NGBnXOmSn5SCETNn7HQ8sWHIfkkw0RaRlByjIi9hrii9aM-lBJ87BF1RTCXvXyMMCqjSOvMcTXvzNaSKYA3eZVGTKEqtwrMmYaQ8HAQX-dcKUUgN3yR9nOY3Nb-jSC1PodQvobQ1hYtL_3PaWUpqEa5IAb-iEgq4YOZMb5MaEPYqsUifHf4WUyE4iD6xEx72XfDCd_pn4oRwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐
سرویس استارلینک واقعی
🎖️
💥
🔝
موقع جنگ بعدی،بلافاصله تموم سرورهای موجود در بازار قطع میشن پس جای معتبر خرید کنید
✅
✅
🥇
آی پی ثابت و واقعی استارلینک
🥈
پایداری تضمینی حتی در زمان جنگ
🥉
لینک ساب جهت
استعلام سرویس
✅
بدون ضریب با ضمانت عودت
➕
سرویس
تانل و استار موجود
✅
✅
معتبر هستن ما ازشون خرید میکنیم.بگین از طرف کانال پرشیانا هستین اولین خرید رو تخفیف میدن
·• ━━━━༺
🔗
༻━━━━ •·
🛫
Channel:
@vpn_artel
🕹️
🛡
admin:
@Make_server
·• ━━━━༺
🔗
༻━━━━ •·</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/22627" target="_blank">📅 22:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22625">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bNgvLrATOO1uCxb5L8KxGySGQgPJZdpPK3gdfcXt-kA01YSKOsI2u1jbOLi-pt9UAJqglGXoye4iqFz0oMqHzmYJXh4fjQjdQuDcRNlRb6Yt-XTQcYVUDNKYFklP74EQdcmQsNVaYHXwAt1K2MEQTCEqMJlyaJ1Bfg5cJrBxuLDcVmlQZLspnws_JWlVNO-3LWHZaM3Q0jHnj53iebZQhb82-rnFRbj6yWfGtsNPqcSaO4Ml8VPmeX17SItVPAITje-vyUJHEhLhUg-wEJ8cfF_EG9F4IaewOZiKem-dF1XUwXnuj6sTPlEMO-706Xm3SUDqsJBuuXZHu3ZVX4MFwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AyjUsp7wk1g9M8ZLYu7eZpunauPUufSMRjsHkX2Z-u6R0-Q4nTucLkQn76H-ZmxdjqYlVGXVP_GspG9UPTKzAlRU7lOsFYAj43r7MscyAzqXG1pnPdgxl0HkHkh92dJ1wa9WHqYm8mwNelNE7WByySriRfxr0MeTsZcMRhke4_p6Toqj3Ph4cSbrUswcemGEd3uPeflRzvre-EsTqbr7OkAWHV4OQCr4FOC-9A2r2b2Hd63JbtYaNxFZTSzLw41gDdSFQWGGcUd6zATYEHfO_f_2NVJNcDSIZw_8ldh_00HLHZnlK_4ISkX3z4817YAbraRku2OaGFGJBlbAh5b1kA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
لیست نهایی‌وقطعی تیم فوتبال جمهوری اسلامی برای جام جهانی؛ قلعه نویی همه جوانان رو خط زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/22625" target="_blank">📅 21:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22624">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bceaf8ef4.mp4?token=Nc53V6J_Xo3VqRm_Z7ijs_r7GbXaHxxkK8FRP6ESnoQLcTmyRBB6vkND-4ezzI7d5Lawj6I7W4Gc0O0AMSZt_GfuJ7suj4yxq6OEiZS4KLiSFVH8tcKV64qSOWT5Xfxc99b72cgqxgHbO_rkAG1CyYAJMEjV2L1ZpOVxWDNReMgWYWDihJTLPuCahUihs3bX2USeOR_h9RliqvoqV5MbV7_LWglsP3GONvjh0Rrz-eKC1WWtOgXd56I1XqzdwsFm8Qm2ee7Cv7LY3ivkEoxQdMeqsNvntONkU-BxpzfZVv4QLd7y9hg6Sq1OH9k6rHggDV6hyFyTB5rxGgo2IQUl8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bceaf8ef4.mp4?token=Nc53V6J_Xo3VqRm_Z7ijs_r7GbXaHxxkK8FRP6ESnoQLcTmyRBB6vkND-4ezzI7d5Lawj6I7W4Gc0O0AMSZt_GfuJ7suj4yxq6OEiZS4KLiSFVH8tcKV64qSOWT5Xfxc99b72cgqxgHbO_rkAG1CyYAJMEjV2L1ZpOVxWDNReMgWYWDihJTLPuCahUihs3bX2USeOR_h9RliqvoqV5MbV7_LWglsP3GONvjh0Rrz-eKC1WWtOgXd56I1XqzdwsFm8Qm2ee7Cv7LY3ivkEoxQdMeqsNvntONkU-BxpzfZVv4QLd7y9hg6Sq1OH9k6rHggDV6hyFyTB5rxGgo2IQUl8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
همسر ایرانی سرمربی‌سابق سپاهان خواننده شد؛ همسر ایرانی خوزه مورایس که یه مدت با تیم بانوان سپاهان قرارداد بست با انتشار این ویدیو اعلام کرد بزودی اهنگ جدیدش منتشر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/22624" target="_blank">📅 21:44 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22623">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c62242613a.mp4?token=C3mMwcufulVSEJvYORfR4MuveZMKQpFR71Zo2b7-zP5qA6qETAWY6xQa4AzT4imBzR3-KwPqcCo0NbJt7NhMUxYms7VpLUETQY6Q19IPwc2L_4roFAhHWv_2vt0B-QmIHejJopBFWWEWHhBlHnbh9-wYGhpps3vf2oCuhd0TZcZeEPUk8_mEDgvY65sS7gv4E5xg2q0gC8SJvMV7qpeAvFVraWN0nUmMdTu3KI5G3fzrCp0u1lZUeyc3OgQbCwjBcfpneUiKbkrI5qEW_dVej23dlcLC8I8yCxWXoo3cM0BGXa6zxPb8fvwVgHZRGbO49T8-0ZQE8nZJzhR79mrL5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c62242613a.mp4?token=C3mMwcufulVSEJvYORfR4MuveZMKQpFR71Zo2b7-zP5qA6qETAWY6xQa4AzT4imBzR3-KwPqcCo0NbJt7NhMUxYms7VpLUETQY6Q19IPwc2L_4roFAhHWv_2vt0B-QmIHejJopBFWWEWHhBlHnbh9-wYGhpps3vf2oCuhd0TZcZeEPUk8_mEDgvY65sS7gv4E5xg2q0gC8SJvMV7qpeAvFVraWN0nUmMdTu3KI5G3fzrCp0u1lZUeyc3OgQbCwjBcfpneUiKbkrI5qEW_dVej23dlcLC8I8yCxWXoo3cM0BGXa6zxPb8fvwVgHZRGbO49T8-0ZQE8nZJzhR79mrL5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
بازم‌ این‌یارو با هوش مصنوعی‌ش اومد و اینبار فینال چمپیونزلیگ رو برای آرسنالیا اصلاح کرد. اونایی که روی قهرمانی آرسنالیا شرط سنگین بسته بودند دقیقا یه همچین حسی به این بازی داشتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/22623" target="_blank">📅 21:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22622">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i37N06mdoQSO753fQjRdER8PVtNr-win-j2qK3ZS61unZ0j0dQfeyH-fLgWlyIl1trQHvG_cWTNWQgSTNECHXIZp17XyX1Dg0WFa985CHs5RuAwUrl2xIRnwbGi7Jvv-OZduPKKIBQOti7E3tOCDobYqKlVpS5QiRvXLD6VrlCBqOEPxQKxpUZJC9xELfsk1TVs450fy5qvhvvBKG6VTxo5c7XyUztCCyblSu_iJ-6u0gA0yXYEvSi_bEsdxkRPDXdiq0Yp7wDRxLmaFHGhd42cVMj3-O2yn_hYKyWqNUIXKfO7xEWhHoLvcS2ep-tcb15VqnTs_-9DgE94eHEyI8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
طبق اخبار دریافتی پرشیانا؛ چهار باشگاه فولاد، استقلال،ملوان و خیبر باارسال‌نامه‌ای‌به سازمان لیگ خواستار برگزاری رقابت‌های جام حذفی بعد از اتمام جام‌جهانی‌بصورت‌فشرده در دو هفته اعلام کرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/22622" target="_blank">📅 21:25 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22621">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dqWQyY0BvmuLHUhMoQ0KBoMWf6ZwwFEOh3dzh0mCVCqzwo8rRYlpE5IcT0TquOG2_2tWt70zBtvBpf-hXisCfLg_nu6HPn_qjacJBtrazmUZ-53_o2zTd7pYcyrVTCFE8cHQkrZnkV7mTd2_p42wLvB7uNKw5y-eVMzGkSBILMUzxtc1Ps9EfZvnSL2zUgyx0RQ5952erXo88iEVRBwRrXpBqNLVLs783Rgt_bVvogp452JrVBFESIzmMfPxUP6uM4leo1DotsBEJ7LrjvlkA4Iuu4GCKt2vKJNRIjvp4u5ctflMKYu42KptSpbBCIAQ3SdK5D5hvvp9hqFknbWlzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🩵
‏پاول دروف مالک‌تلگرام: حکومت ایران تلگرام رو به بدترین‌شکل‌فیلترکرده صد تا پیام رسان ساخته ولی ایرانیان هنوز دارن از تلگرام استفاده میکنن و محبوب ترین پیام رسان بینشون تلگرامه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22621" target="_blank">📅 20:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22620">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T2c-NEz4Gx2jB9txUwGvVd5W90nTiBjeEs-FvQ9xIyqhh_kJE6p6H9gCr9OADVLNSfGxlPFSyZzbWhpnldxVYBwOgPYoH-2E03Pjnqpsc6uakJr9Ekop8E5_3j2e7zDD9u2Im6ZRLSQUAf2Au7EcwDAax6HYsNWrrh7NXFXSjsTJyzxC7KosAUUnEbaFQt_aLt5aRqB6Qcyx2N55RQyu9t9G_nZeqmw_RZ-20bD7mbyCUFRPtzje-DLikNabKyK-87EfstU1QqOHIqY0UhkXVbIKRAQqwXvbvp7CI64CfPyVdH1b6yHgLNZ1aSZ7fDZrHhd1p0b4cwsBn_SC0jQbOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ با اعلام خبرنگاران نزدیک به لاپورتا رئیس باشگاه‌بارسلونا؛ خولیان آلوارز ستاره آرژانتینی ظرف 48 ساعت آینده قرار داد 5 ساله خود را با آبی اناری ها امضا خواهد کرد و رونمایی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/22620" target="_blank">📅 20:22 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22619">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VuZVfBqwDLkbtqfpnIX8ZjcYtowZ2aS-kiRASQmvgs7UV_CCaTnHwI9DDPmKTdQua_JImjLps6uo9jABvVj8x0qXLFkDc060xyna6Z5FBBspidOkA4t_zW7er05tXB0G3UKzoirLPjw_byOgV0DYWSplz2uLY700DJEKRlFKM5srXqXciA68PAKEsMXSHs5TPjFWgkY07qWLHtpH_ElFpOObOtd6W8sjIyoLCV32_NlqlUiWDBMjyg45uVHU3NsyULbyEouGsiQ2LUcWWe4jYTN5WFbrIJIFfQp-sw2nwmhD0PYswUvypkp-0ppkqih6joeJa4n9PXKEgi7Y_MNxqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#فوری؛ بااعلام‌رومانو؛ باشگاه PSG بزودی قرار داد لوئیز انریکه رو بلند مدت همون دائم العمر تمدید خواهدکرد. حالاخداروشکرکریک با یونایتد جا افتاده ولی بنظرم تنهامربی که میتونست یونایتد رو بدوران خوب خودش برگردونده همین آقای انریکه بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/22619" target="_blank">📅 19:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22618">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UKlvBdLR9_eATFeefDT0Xpn44VzUdNCR1rX0oJ_nX73jl7X5LajiSdkhZiNfO3ldhoU-dIcxi4CUm9ef3BgbP-7rOvJ2xJEAKW3849iGnaFanpZfjeZ8ujCFYS0zz1P5kGntB0AF4hBe1B8nm6VGH5XQ1yn6dArtoN_Z7Ilem0_KE6NigcsGVKHiERXRQq5LKaZuTwX61aVVyF0auTQFSB-7dZ8l4D6f2eK5rWUewPgTFf6AXg-APgqD3Ql7JcnlZ6deU6JTrQJnqOfnb_3WO11eWR0MDyFvKqvW-G3a7XD2uGYY7uZhkyNmIlJWMdvriMAKQV89cGQxHT5yl6OjyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#نقل‌وانتقالات|مدیریت باشگاه پاری‌سن ژرمن آمادگی خود را برای تمدید قرارداد دائم العمر لوئیز انریکه سرمربی این تیم اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/22618" target="_blank">📅 19:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22617">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/514074c458.mp4?token=pRKQMKsLgZWbSJsVGliTHcHjtKWPD3WLYpCSwdlZtKOX61vOGlYX9-DyEBZwqStWyrde2zOs0JRuU1s-qTKe66nZ-Ag3VmfzLxcs9QAcWIDuIftxCTOXfZD9G6CtLDW23kthqKNMIXF8ujP5_2-sRsZ4eK7XamiyAuiTCLbFIsDj80pmfB5xmNJDzIuv2exVbwxrtE16rfs1Lgqs1n0KBAoP7H1Uo9k9US8PNnHuzXm_umVahP8d6nXR0sKsF_0ar7G08cQccd1sa9eu2h9alHXd9BmgCe8_T_psx6E805tNyecWQocgrogU8mL1nQ931e-5tom_PhZySsMKhvFxlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/514074c458.mp4?token=pRKQMKsLgZWbSJsVGliTHcHjtKWPD3WLYpCSwdlZtKOX61vOGlYX9-DyEBZwqStWyrde2zOs0JRuU1s-qTKe66nZ-Ag3VmfzLxcs9QAcWIDuIftxCTOXfZD9G6CtLDW23kthqKNMIXF8ujP5_2-sRsZ4eK7XamiyAuiTCLbFIsDj80pmfB5xmNJDzIuv2exVbwxrtE16rfs1Lgqs1n0KBAoP7H1Uo9k9US8PNnHuzXm_umVahP8d6nXR0sKsF_0ar7G08cQccd1sa9eu2h9alHXd9BmgCe8_T_psx6E805tNyecWQocgrogU8mL1nQ931e-5tom_PhZySsMKhvFxlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇺
5 گل از بهترین گل‌های فینال لیگ قهرمانان اروپا به انتخاب پیج رسمی این رقابت‌ها؛ نظرتون کدومه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/22617" target="_blank">📅 19:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22615">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Da0cRUi_XLzr5cjvPWZeASE0ONrRJcRoZ2e8hBqF0Wmo7t3-XTsDHVO27aej7Yu3rt_NY5aCYY7H7GhyGRp653jsRM2zhH9rT23qSsIf5ZFLR_k37jPsEI5coLQtXb9OySL-xp8JFU9ise-Z3rjCq5_0wgdbBceniPwUa3lpjKGds_8wx-Q9Ao03GFVpnoyFoJEe0L2M1F8sY3mV93i4or_42hHENYUkGwGtiJaSoGYR9xsTztY_l-qAoKgEtgiO_n_k2pGI1wzVs2yM-RCyehJZRyJYSVC5G-QI-BEjY3Lmwao4KjZ1H72a-Uj7K0mbEXRjuzRrAbJqXPqO6Wc35A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیدمهدی رحمتی سرمربی شمس آذر: من با باشگاه شمس آذر قرارداد دارم و همچنان روی حرفم هستم که فعلا در حد و قواره سرمربی استقلال نیستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/22615" target="_blank">📅 18:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22614">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d191ac7bce.mp4?token=Gk-ZbtA4F1NgYnjDAe2raKVcB-l8W8v8WsVInWiu85s6kjWOUkazMNoHeleg2r6YkzYLEEi1RodYn4ckrUFSr42OeS--u0iuVc85pUg-AQ-zBB0Auek8pVtED-bJB2M_5Nt7skpbqfrg3wjwb3rBhnVo50R88MBsZqBUeNT29GAec4DWZ9KFXiJzeqVpLGYY-YYxCMUMG4NwB8l7toE3OGQRUseBcN8W80WrxDhn6P13y_S8cSXPaYRhA9Lzkd5N9xKTC1a18E0GOQOWwKE4F_3OLsy4UXNSD71GUqM2SObblPqaWzrBxVuy1SgKHpXBYvaLZnFlGar3bNDqi3qqVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d191ac7bce.mp4?token=Gk-ZbtA4F1NgYnjDAe2raKVcB-l8W8v8WsVInWiu85s6kjWOUkazMNoHeleg2r6YkzYLEEi1RodYn4ckrUFSr42OeS--u0iuVc85pUg-AQ-zBB0Auek8pVtED-bJB2M_5Nt7skpbqfrg3wjwb3rBhnVo50R88MBsZqBUeNT29GAec4DWZ9KFXiJzeqVpLGYY-YYxCMUMG4NwB8l7toE3OGQRUseBcN8W80WrxDhn6P13y_S8cSXPaYRhA9Lzkd5N9xKTC1a18E0GOQOWwKE4F_3OLsy4UXNSD71GUqM2SObblPqaWzrBxVuy1SgKHpXBYvaLZnFlGar3bNDqi3qqVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدئوباشگاه‌گلف‌یونایتدحاضر دردسته ۲ امارات برای رونمایی از«آندرس‌اینیستا»سرمربی جدید تیم؛ اسطوره اسپانیایی وارد دوران سرمربیگری شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/22614" target="_blank">📅 18:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22612">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gqhyyFVqtiQcTw-wfloKLw1cTX1mtPQ86tnM4mbyhQxhNr0wjOU69QlXGXz3By2aeY1eLmwEMkQt8AF5FRbcTTPHBK8Xa9VYfokqyX6Ap3zcb0x3J6E1IJcvgp2vBqOwiWa1lqHEz7RZBrr42q7JiR6TyA3r5ukfL4Pocp9HDjz_KrtoVrBM-TzbBxLuhQ3Db9Q-vh-pw2Swbv2qvcZk2Qhka0Y7wn_D2mFn58pFCQXvDeD0tlGBBKTM9MnbBR7zJQY49zZ38tHm0eoy9SOyVOxbJWw8UywGw0Jj5xrCm6qhOBd0P1Z-56gfxYaaHeBJ_NPpgdLegAVL2Er058z1eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فکت
؛ ویلیام پاچو مدافع‌پاریسن‌ژرمن این‌فصل در اروپا هر ۱۷ تامسابقه‌روکامل‌و بدون تعویض شدن بازی کرده که‌یک‌رکورد خارق‌العاده‌حساب میشه.
🤯
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/22612" target="_blank">📅 17:27 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22609">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f31679a7dc.mp4?token=brCD8BfK-NAWP8suIjP2DHKbdTeUAUbJZyGRZghPhQPXI_shZsO5vswI-15ubzKwxQYOdWkt_0Lw9JMdz6fJ6q2YY4r8PMK2vHB45uNqEHMH8RMXwmbg7rBh6p-nEqjA92w9c5u36Dv8MzQ1TLrpv_6ejQb42Tf474RfxAgMsyO-oCaefsfEbMjaIu0CeNvxS8aueBc89TTjChjAdRXNuCYn8_mchjpUO8Whub5t9DLJs4Of64MKby-1oUl5HGcWyTcfALGz2TUK_eMN1K4ZD1TMTjCtAfqvCDaAv8-bZjU65AhJtkiKGs1kx9e2oTn01PfKnbipnwGDwazLvzPCVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f31679a7dc.mp4?token=brCD8BfK-NAWP8suIjP2DHKbdTeUAUbJZyGRZghPhQPXI_shZsO5vswI-15ubzKwxQYOdWkt_0Lw9JMdz6fJ6q2YY4r8PMK2vHB45uNqEHMH8RMXwmbg7rBh6p-nEqjA92w9c5u36Dv8MzQ1TLrpv_6ejQb42Tf474RfxAgMsyO-oCaefsfEbMjaIu0CeNvxS8aueBc89TTjChjAdRXNuCYn8_mchjpUO8Whub5t9DLJs4Of64MKby-1oUl5HGcWyTcfALGz2TUK_eMN1K4ZD1TMTjCtAfqvCDaAv8-bZjU65AhJtkiKGs1kx9e2oTn01PfKnbipnwGDwazLvzPCVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
لیست‌ ابتدایی تیم‌ ملی برزیل برای رقابت های جام‌جهانی با حضور نیمار فوق ستاره این‌کشور؛ ای دمتگرم پیرمرد ایتالیایی‌که نیمار رو دعوت‌کردی
😍
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22609" target="_blank">📅 17:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22608">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nA1bvpi-lr1IZKelvj7wZCpGKh6xkiDqQxrKaA4Pfezd096SU1qgXpdOzXQdoRlx3OCrxcKqao3-AE7AB8z7gg5Hnq727oBmwzkzOx6M4RzzdEub_aw2863Kt3rChg9a09M5YVBpGgRoQVBC2uihmNkFZ5NdPcsCdcFtl-pzfQrxWge31fituveQ3R8Ig77aC1ztGPeiAKM30SNwuH_RO6CsKI7tdzlhgkXyPRUXXHJSGW8Qx-vApeYMB8ueZ8n7tUp51bU3EJG4cQDLGo_v5BvCHCLvp1XFe8eq4rgql4qd8sOGtZzJ5q59o3SzD79Fbwby1RMAcm_R7aprBM1PnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌مدیرعامل‌باشگاه‌پرسپولیس؛ اوسمار ویرا قطعا فصل اینده در این تیم خواهد ماند و لیست نقل و انتقالاتی خود را بزودی تحویل باشگاه خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/22608" target="_blank">📅 16:42 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22607">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y6qMnnVjXzZrc1knpc609mNZ4nSC4Iz8N1oRtPhRrFVzWmfZCadPXIEEphs8n6HBP9-1uOMs7mgiLhFr93opo4H5lugtVTiDNkHnpVk34_ihqy6X1XRuZQXUe_kuh9lh889LwtIj1Eny3vDwZK2vryLkK9Ji5m9mnUoPECA-aayds6s-Z4xnvRI2uGGmpZ6MUdmDpxDsxm0fiurH0SrQbLX6tkOosao0X9vzOSOj3AcBLKxBAH2fLiVXWw1cbWAKPow8At2we7mCysMMI-fggSSQXATrlGf2tCSv7m8B_r_Vpbb11h6aBBbtQ_ZKYIweJE-yOeqc7UsUaDfQmJiltg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست نهایی‌وقطعی تیم فوتبال جمهوری اسلامی برای جام جهانی؛ قلعه نویی همه جوانان رو خط زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/22607" target="_blank">📅 16:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22606">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bf_wVtfZN8eVNU06nmBZ1vX89fxMFT-G6tRuulOsFs9VlJZoOBnOK57huNlbz4aC63bl4ZK1hRj8nIbWT9CIdquJ6oR3fZmYpU7B0PBuKQ597i8O8hS_ZhKJO38m23O9zaj6Z8HyWhhrpXgOCv3fsrjnNix8B03nAAX5mNnWvjJjaoUBDsk8sP1bAPZn1NaFd01NeX8KnSJqWkkcLqg5cDI7LDAnrWNpE-QLln6D3hrVrArkyNOQNR9Ij9HjGnjzwjrRb6wt34-bMHO5wyJZZBGJ4vml4U_ft8lXMEXitMG5QL2JIuOTg2BPYu-t_dLihIddmYXSezLxH22r4u9v7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست نهایی‌وقطعی تیم فوتبال جمهوری اسلامی برای جام جهانی؛ قلعه نویی همه جوانان رو خط زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/22606" target="_blank">📅 15:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22605">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YMSqg1vd_OdFiORLX9joCVayFDYmZptPluNuzneRa9tePByTC6BR--NdYCumyhNS0I8O2d7BA0QtS9WUM9MGwEST5ha-_22aUesRWlbR8cTeLDT1BrgtKG3YOS04er41KXuY_kivW51N6oIAxyCfki0Ou508VmcC9WWC4wJwG9QGsg-EJ02iQI2P4AY7hP7wB_arrz9kUUk8pHPO_4wcv-pwykRgU067FETQ3SBegBXtYgjF6hONdWX8ngSWoWq7zOtg72X6Qo2H7-FSdwf0RJTrp2xxt7RS2vDvQP_rt11D8viDxbWB96lSD2Q6xuptfxFdgh9IwL-DQCekbSuHJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مارکینیوش کاپیتانPSG با عبور از دنی‌آلوز حالا تبدیل به دومین بازیکن پرافتخار تاریخ فوتبال شده و‌ فقط لیونل‌مسی از این بازیکن جلوتر هست
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/22605" target="_blank">📅 15:29 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22604">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMT_Me8L6jB83o2f-mYCf6IcuaIi99vm8OCf70eBcjSrj44mFODnQWR_dn0vJ-JvbWmUCJOqgqFwmUiDWLBaT6DAtGAhDOa5Rmn14epLVlptEovMi8u_UGpmeyDZEjJZdDSTJjwynExZxnre64n09dueiBQ2Y14MjOG_fKQ9D74M_y_0oznIo5sgl4aukxbmQwiREwZS1ZCgGgZHfnWpUCmDoli3jqd7HI0KYeJv7wUhKhW9QkNKtLqjaYdTOZUTprxG-b6vtF9rfsEiAHKasGA7YANLx0dLgMyyYs0828TjLRDQuqM5bBzU_SJ9_ioXbwKcmhU1gI7r9rnexmpg_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
آنسو فاتی ستاره22ساله‌موناکو تاقبل‌از شروع هشتم؛ با 5 گل در صدر بهترین گلزنان لوشامپیونه قرار داره. فاتی در پایان فصل به بارسا برمیگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/22604" target="_blank">📅 15:05 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22603">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I_8y_OwApdfpRnOUn7yWU28LpzSqmNiwglIhMOKH1iqq5G2hTbQM5_x-pX0tPQhOFhvVXHwiLFxQmXB5F35GnPMdhIdah5wX4kDRhUbrAvKtN5hZhLGBECKensSsMEmgVsZzHrJN4BN_cM6hGCBgMO_80DHNSXI_MzF-rD_2F191mpahk-2x3Ys0Bq1jZu7fWm0KrEBR2y3oKyWyFdVBO-IEUXDtNxrGqXnx98dbS3WKIDXoBTycSZSmTTA1N0gtY_81J64BDDW_8USt76Re-fkmU8jJ44-HZ8-sCUww3TFw6HRl6pKmxo4Yms7IwUvcXT-pGMjC1IalrVCdhW_ifA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
کوارتسخلیا: بازیکنان‌تیم‌آرسنال بویی از رقابت جوانمردانه نبرده بودن. اونا خیلی سعی کردن منو به بد ترین شکل مصدوم کنن هرچند تا حدودی موفق بودن ولی درس خیلی خوبی بهشون دادیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/22603" target="_blank">📅 14:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22602">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kGZ9w4gtXKfXy9lUMc5HEPKkarfWOUdJtBjNvd58hxNvGOGn3WKLwuPpA6ORfXTf9_p5fwmiNxzBgBlUFbzDkPRpIlG5OyNv4zdURTEJjm1CnWAKQbMtv7ylyVHBdNyUF1tEfvDDn1V0TAWp4AJAO2O6xX-IUtU3qYlOhErwP7-0KEpGVhJh6842l7pscMshpP0ULxTolrXKFSoom2vMzvVEY5eEMm3RR8iOtWfVxy8LkIpSWiVuezs8DW5GVqmrVEmg0hPbu_-Cbuo4_2iWcoARO_i1cwM7_Z1a_cIiqQDCPR0Gy91f1Qv0ILe8VkZLvUJDbq4fL419ejKa52szfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
هرکی‌بهتون گفت که چرا اینقدر به فوتبال علاقه داری؟ چیش به تومیرسه این ویدیو رو براش بفرس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/22602" target="_blank">📅 14:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22601">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SlCIlWgqQti2Kxye3j0jXgYP9qVWjHmpcMHfqV7ld87Ug207bW81VDQHJI_RYtDAIVvEB-8qKSFrGOhSs-byLMjNpZQ7YXhIdse-2uzwU9L9H0kL_T3avqFchmzN_j4QtAZnpLCcSM6BaB-1I-QOWnvsGYS2_UymYWgYytdFkHQGNitxfZniipe2QoBrXsIaVdBl1usoMIxED7JpkItx3aWrA1u6c8rc3-TP9qtS76H3VaR4lGkpIB1uifvw6cWmq21H3tY9SsEuyN2gmmectavMJpjSoETxSqkAHJP9IGMqDD0vkVUKq5iFZhPmQRx0nQabdCPIjWhO_T36J4r8UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
کوارتسخلیا
: بازیکنان‌تیم‌آرسنال بویی از رقابت جوانمردانه نبرده بودن. اونا خیلی سعی کردن منو به بد ترین شکل مصدوم کنن هرچند تا حدودی موفق بودن ولی درس خیلی خوبی بهشون دادیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/22601" target="_blank">📅 13:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22600">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05ff67e8c4.mp4?token=Q-Rt9ocz3ZWi_LU4urJ0E4fJ66ecDz2hwkE7fxd7RtUrt0__0UALpmq7VaGCGiQIn1YBto2HcRUmoeDm50kEWwtn0Kz4izUoCv3UaRj0rje_4a5952lcpxNsWahKPDsirt6fC6hx1VLAMfho0BpzX1D_MgOlh4I2cMO4ZF_dCamLVRr1B-1fcaLm-BZDoIxiulyGUDdVBr7sD36JkhZY05DpOhimk1Oqo0i4uVyZYUcLcM-90AmqgIurEXl0LqciyxujBB7jNhNjCAy7pXwhrud3LWc49ZhDa3YClBTRl5yGYLvTYhS96HcB8pymSUtxHuwX7b7JUUgloW1vu2uRUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05ff67e8c4.mp4?token=Q-Rt9ocz3ZWi_LU4urJ0E4fJ66ecDz2hwkE7fxd7RtUrt0__0UALpmq7VaGCGiQIn1YBto2HcRUmoeDm50kEWwtn0Kz4izUoCv3UaRj0rje_4a5952lcpxNsWahKPDsirt6fC6hx1VLAMfho0BpzX1D_MgOlh4I2cMO4ZF_dCamLVRr1B-1fcaLm-BZDoIxiulyGUDdVBr7sD36JkhZY05DpOhimk1Oqo0i4uVyZYUcLcM-90AmqgIurEXl0LqciyxujBB7jNhNjCAy7pXwhrud3LWc49ZhDa3YClBTRl5yGYLvTYhS96HcB8pymSUtxHuwX7b7JUUgloW1vu2uRUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇫🇷
اکسپوزیتو زید جدیدکیلیان‌امباپه ستاره تیم رئال درحال قر دادن در کنسرت روز گذشته بدبانی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22600" target="_blank">📅 13:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22599">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59ab989954.mp4?token=NW_0pzBOk360Wan5Oe41f5b5kcroi2AGDRReDsYxnFTIGc_-eN3vX90cmth4Q1xpQxd-gghPB8RYs1iKWrotE2b3ztPV7Hpx6gDbPo1otyrDEt_liZHM-iIz_YDqzZWKe5AveON7m9J3WapzxJFSR1D9eOBVPCEOrX7f5b9oHtJhOP3Bb5oRwnPRvpLzznDDYl5_3QQZDcb8OXaZGWRhL1-eG1pZsjqy-2JtLxO_khOs_p6x3MpVbYKCyFnQ2cMGS0iTxQAOimXpXVn-oWJW1ogJg9j0bFg2JxGqCPUF57xT8BEOi_swSk6mInOLjGH_-qTjCjwxw93JRFyU0Pmd2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59ab989954.mp4?token=NW_0pzBOk360Wan5Oe41f5b5kcroi2AGDRReDsYxnFTIGc_-eN3vX90cmth4Q1xpQxd-gghPB8RYs1iKWrotE2b3ztPV7Hpx6gDbPo1otyrDEt_liZHM-iIz_YDqzZWKe5AveON7m9J3WapzxJFSR1D9eOBVPCEOrX7f5b9oHtJhOP3Bb5oRwnPRvpLzznDDYl5_3QQZDcb8OXaZGWRhL1-eG1pZsjqy-2JtLxO_khOs_p6x3MpVbYKCyFnQ2cMGS0iTxQAOimXpXVn-oWJW1ogJg9j0bFg2JxGqCPUF57xT8BEOi_swSk6mInOLjGH_-qTjCjwxw93JRFyU0Pmd2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
قشنگ ترین توضیح درخصوص بازی تخته و این زندگی؛ واقعا هم همینطوره. عالی بود حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/22599" target="_blank">📅 13:07 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22598">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gN4U5UXd4zbgNJOJpmJ1UD-OGzDjSiHjpzsU3jyBa8dkkMsEua_WWz6P2mTZ3cJggfYPR3qnt4Br4qGeXitOKF_Fc0NRDMS-ovhKtuvK9x5e24bdTvL6WIoLMnjOGNqBYZ-QeH_peBJNuh7yzWB6rgKP42kFo15pvPFcSnr3VAEBPt8nTmaU2NF7WM3D0JaQr45d7JjuEQ7SWSQ9ZBsQW-ChlD9ert4Fk_MXWrsdnqH8xaI1_i8yMrlwt-vt22wKX8_in_vxeLuECIFRMajRgTD0uZME9YMf0NzcApFCraxbqgcqyaKh_d_jZH15UnxgXdARCTuWaSrj69BEBvQfvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات|گاتزتا:سران‌باشگاه منچستر یونایتد مذاکرات‌رسمی‌خود رابرای جذب رافائل لیائو ستاره پرتغالی‌آث‌میلان‌آغاز کرده‌اند و قصد دارند این بازیکن روبعداز جام جهانی 2026 به خدمت بگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/22598" target="_blank">📅 12:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22597">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a3a620208.mp4?token=eDuR4c6s24PrOzIPi3ZW5-b2PXj9y2zcvthSkTWagvjKgSPRUlrNXlyR23DPGNRYcLkZUCOmevSVn-pitvXOBBEdovLZrs-1GPtL68qqqbcF4yIQ5GiG8gqduUJ8JgJhecZ_bDuMtly07xv32kz9pHK-d1_Q5aJ70Y0nh0RBCoJXoEql4j4Cn0r8hZFISg52VNJ2SstxOiOFJJxSRt7-ShtqGjaZfaX8WWUReYogl_NRZKd53ItnOTm5vR6YbsrU7v_fVzQDFjIwvxnJK4mYWdQv1S33XzDJmfb8uM3S98KbPqUvpXemxRLLt4qaQXvP78dzpBspwfR0Xo4A9GNfkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a3a620208.mp4?token=eDuR4c6s24PrOzIPi3ZW5-b2PXj9y2zcvthSkTWagvjKgSPRUlrNXlyR23DPGNRYcLkZUCOmevSVn-pitvXOBBEdovLZrs-1GPtL68qqqbcF4yIQ5GiG8gqduUJ8JgJhecZ_bDuMtly07xv32kz9pHK-d1_Q5aJ70Y0nh0RBCoJXoEql4j4Cn0r8hZFISg52VNJ2SstxOiOFJJxSRt7-ShtqGjaZfaX8WWUReYogl_NRZKd53ItnOTm5vR6YbsrU7v_fVzQDFjIwvxnJK4mYWdQv1S33XzDJmfb8uM3S98KbPqUvpXemxRLLt4qaQXvP78dzpBspwfR0Xo4A9GNfkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
کیلیان امباپه وقتی‌میبینه که با خوب بازی کردن در جام‌جهانی و قهرمانی‌فرانسه به عثمان دمبله توی گرفتن دومین‌توپ‌طلا قطعی‌اش کمک میکنه
😒
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/22597" target="_blank">📅 12:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22596">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TAWNA264TlPvFzupH2Z6VsiBUO7fpJTduao24Z3dpgZAl4459LTnkwEgC9dNedvommoefDbBKOzF9y36bn7RW3d1q4hywmxmt-rBRqvI3fkGsco8PsHFyAB3TxIrqj2d2le3up2OiWYJAT85hnw7j1mR7FI152TdmVTZccAvSW1-ut_59GqY6YB9bblT7CDmmxj8ZvgKMNYYI3GGWNA38tEgxgQSjqzgcL0khTGm-4m3IRgYhtp5hImEYs_QKw7mUIEjWGUtYG4Q8GZ_QEyb55IFo1jAOnZyyDLbUDAftAvyo7HSZf3HqYoE1B0Psb-CuNYktHFe787wGCZQgBfpuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
لحظه حک شدن نام باشگاه پاری‌ سن‌ ژرمن روی جام قهرمانی فصل 26-2025 لیگ قهرمانان اروپا؛ این دومین قهرمانی UCL در تاریخ PSG بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/22596" target="_blank">📅 12:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22595">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eter0tnZ_-_s_D6sIFGLuHYQqxN6N5ZU3IlNIyhMXRGS_Cwm7FaIi7mSb7_Ia4fOv4DSd-8-MbtBaJX5l51Noo4Cgr3vLcM5jmTzKEj8EO8Rys5rrgSgqIPEYuJBUSBRduUFKt1WjVbz6kdHyAICwEQf9kA6QwfA9M0WW61ptjHDf4HPKOKxJeKCpAc2IGyopLdwDpFR8A99899UodAn1S9J2IiCVI-cPDtV5rPylj-jvMSoU4PPKsZpDE0_L8IV6-W-jnRSpOo8QEpAObnsqYFnDf0f_GivKKaCVhGF9P4EaRskHE2XCXQnhCYhSIDu9scqXNXQzCSNfdT67nshjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جرارد رومرو: یوشکو گواردیول مدافع سیتی نیز همچون خولیان آلوارز در خواست جدایی از منچستر سیتی کرده. فلیک عملا با تماس هاش داره راه انتقال ستاره‌های مدنظر خود به نیوکمپ رو هموار میکنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/22595" target="_blank">📅 11:56 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22594">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3238aa793a.mp4?token=SxsNJ2CbU7lbrpVaA8OD8rj_lFt2x7BwaxzReoQ6hmUOudye5sQJu7U8EJ9MA07oCsU_Qd2pZWzuyG196QLvqIGC5Sjk8x1hfVQjwCaPNaRaPv-DF_iXp-_NI8rYjcN-uVz4yRoOrFtaGXK_DYU6njiTX71v1vLGq7ce3dZY2tle9ZNpUnf9ZHISMrf7lRX7kHSMd9BGpyo5AX-Ub3LF8qY3AcW37LVg16xWEdraYkD3OtpyEAqb8Dwqd3zNIaE2CXWhHmO52cmAnojPTOqJ15DDzIjkSBbjlCirQful1eReDvgtPfM9qMFiEgLsmq60zkQxBhdjNPwlmkLKVWydOXi2qJ4LIgefxxf_NzVCOhZJMIbZFOAllrD614AHzAqRngnHD9mlB8qS-vX_UlILctEX56kiSffssX0duiunAD-qZ4X5N_8wpSHdQEj-BunXZP5YkalInQOMb7lrQrSKX247vrcuT-wBo5g3O48GZIyFHiVRm3SynhWZuvsGbKSNibzlPnb2My-o3cPe_lvXyJvOaVp0dUwchMx98kzgO4h41wdi92UEg1sM1Gq7gsZv9I9YFjp-L8VV2r-r3M-ufmniJRN7ArLJN9N6pdgBVTHJmz6IcS5Mdq558KMjXaU3CkXFMiJYuwEg0o5ioNteJL2neVSs-9C0KIyKlO9tQcU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3238aa793a.mp4?token=SxsNJ2CbU7lbrpVaA8OD8rj_lFt2x7BwaxzReoQ6hmUOudye5sQJu7U8EJ9MA07oCsU_Qd2pZWzuyG196QLvqIGC5Sjk8x1hfVQjwCaPNaRaPv-DF_iXp-_NI8rYjcN-uVz4yRoOrFtaGXK_DYU6njiTX71v1vLGq7ce3dZY2tle9ZNpUnf9ZHISMrf7lRX7kHSMd9BGpyo5AX-Ub3LF8qY3AcW37LVg16xWEdraYkD3OtpyEAqb8Dwqd3zNIaE2CXWhHmO52cmAnojPTOqJ15DDzIjkSBbjlCirQful1eReDvgtPfM9qMFiEgLsmq60zkQxBhdjNPwlmkLKVWydOXi2qJ4LIgefxxf_NzVCOhZJMIbZFOAllrD614AHzAqRngnHD9mlB8qS-vX_UlILctEX56kiSffssX0duiunAD-qZ4X5N_8wpSHdQEj-BunXZP5YkalInQOMb7lrQrSKX247vrcuT-wBo5g3O48GZIyFHiVRm3SynhWZuvsGbKSNibzlPnb2My-o3cPe_lvXyJvOaVp0dUwchMx98kzgO4h41wdi92UEg1sM1Gq7gsZv9I9YFjp-L8VV2r-r3M-ufmniJRN7ArLJN9N6pdgBVTHJmz6IcS5Mdq558KMjXaU3CkXFMiJYuwEg0o5ioNteJL2neVSs-9C0KIyKlO9tQcU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
قشنگ ترین توضیح درخصوص بازی تخته و این زندگی؛ واقعا هم همینطوره. عالی بود حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/22594" target="_blank">📅 11:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22593">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iFGCrikPQ0hDV_x4mw_kovaQmf1cEBRUeEC2n0bdvtqVwEwH4_6LLFGNGEVFhKp3SFTBdNsKOVHuwZ1EtmXALkyMNB-rLKN4RXXVIzAhtpDZUIRMlpUllx8PuLkr9YluFw0HfsyyhZXfHL0A5kVsTQyDe5hkTjdPqBk1khn1mJ1a3q0JjbR0oTpKDttmYJ-fbPtobXh9SVdzZrcLSh54pP-hm2DrAsi24__va63oPg2gQQgeu5bu6pX0PGBlg0OPAo0n8pYRVc-Ltkld99mH8WqIwQFjIFjSBh2LOAjSOH6MDaTBCtvYVWdXQpuz6lGbkUAAiN8954bqDjrTDLMSnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکوردفوق‌العادهCR7: حضور در6امین جام جهانی؛ لیست پر ستاره تیم ملی پرتغال برای جام جهانی.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/22593" target="_blank">📅 11:32 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22592">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhKqMkDzF-90_zj99eRBT_bm7C4xMZqVurK4bkz2kEunIbd-oqF5BphKvcdM-L5MizB3_BL83MNX650j5XF0yRMQj9orlHg7nvET8o24MpPnSVzkUbeukvZclKRqxN35wewMSqUjEZqDp47s8WTw41KLm97kwuql8ufUvhsEBLIaB9bWWnii738jrOycDN7eRMzYscTJKkMAHkr7Iin4l-DVvsLPICuywbQhJc_BHlYzOa7L79xZXaKa7ucWVWdexuaaP83UkvOPuKa1aRaddrkYN7nJXVa_bhUNfnnRPgNc_B2hQzZi6XTRMFLEObDLILLxdz3PLq-j9GKfGwBIgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم‌های حاضر در مرحله یک چهارم نهایی رقابت های جام حذفی؛ تراکتور تبریز نیز حدف شد!
✅
استقلال، فولاد، شمس آذر قزوین، ملوان انزلی، خیبر، پیکان، سایپا،گلگهر؛قرعه‌کشی‌این مرحله بزودی انجام میشه و بازی‌هااواخر اسفند برگزار خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/22592" target="_blank">📅 11:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22591">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/miUyRns9kAzznSMQuHteEeJQ7tSBtg6oWD3KNb3n33iIvObJAetmOSCSe57pdLtMrgVcvrkjKh4Gh6tsjlwpsLTgiqOTClXsWRMnBLSxTwSuLJQLl8QcoyYL0FQmX5w8xoDtAJim2FJToVMrRLqUBQ_aNlhoQYAT-fTTNEPyiJsA6SWMzHm1FCJj-cmeAziN2OjsmDotNb18M3i01GP8B9xEfFSj2ysl0_yZ7lDtLA4D6UGGExOOzyB4kXDhqfVgXmygxSdiW-Y_LhTUTpFft5cb4-EHGRDihWYX8bExk9SboiXW_wapu7adxs6kRMoU3hyBIGEwMIHsk44Sgkrd_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
محمد صلاح فوق ستاره سابق لیورپول از طریق نماینده خود به عربستانی‌ها گفته هر باشگاهی به من دستمزد سالانه میده، قرارداد 3 ساله میبنده و تیمش روبرای قهرمانی میبنده من اوکیم که به آن‌ تیم بروم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/22591" target="_blank">📅 11:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22589">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D3Whjs_KUY0n4mfIyE849luP6bJKV5CYz858kdBfclsGpcOYiY6wDJSahDCtwAqdrlAiwKihncAvLw0A2th3GdTWx9EnMdPZZMVaCEg7TGy6Q4hjmxCNkH4K7DxjCthpynPEUP7ioqSI0PTEpt-Mwc70VIvvCASu7tFgGL0VirLzk8m-jlxFGtKm6lkkyMacVk_NDgMXfOJ-30LLFp3BBoabpFO9RYQGBGQhcf7ZhLjRgquU3RpPC5x-FvbXWjdZSYkQ_nd-K41fKtrqI11WwvJQVymOSS49nLjAlMbIdyTn04gsI3hWG82iOfbYeQ8LhY65ytEHjkXspf1WJQCYXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات|رسانه‌ های معتبر فرانسوی خبر از احتمال مذاکرات‌باشگاه رئال مادرید با ژائو نوس ستاره پرتغالی تیم PSG در روزهای اینده میدهند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/22589" target="_blank">📅 10:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22588">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IpC81rtV5zF2mzONiEylesohqUK7_skWQq2PZwh07nvIqWxBoAi0zfAQDyqsw82gjdLe-I0fh7IaXhMT_5w6CCHT7NKpTlMdLT7E_FjS8poA8p65_yUsfxZ07-M44XkBghBnqkTuRYofXoMBOMjoHUqpzmNhXAWbgyJBjT2Rf4-Ihz6n_xzk3emSrUvsKtsWQiOccJZxTPXPOMuezs3W1fJdbb4OgKN1jWMRZ3GnJKiu695AHCxwGqOiWYtEt9A728Mktfi8z1j3rkmvcTfwF3ym_AyNoHc4yLOmbQkr3GIHf2wBcIthVFQ595Hg8i52glc3Ovq3rDvR4QTYZ5T1vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خداحافظی فرعون مصر با هواداران لیورپول با چشمانی اشک‌ بار؛ محمد صلاح فوق ستاره مصری لیورپول بعد از انجام 442 بازی برای این‌تیم بالاخره از جمع لک لک‌ها جدا شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/22588" target="_blank">📅 10:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22587">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f927e35e14.mp4?token=JsfPY5cKoX0t2dNpN6xGleGwOJz0JPplM47sLezEwWB0UcB3HACBell11IoEork7f9Mp8CrGpQ8EBC7SyKPALyM5UkA4B6NXh-nnAYWTDtSBh9cVFKKx462XI6mSlSzpeyp1LtGNBEbPN2AQsKO3mNa2Ugczn3IwgEh97hr9r9nNyoDRv8d_zyVFFaZdTZLNgJEfQRSmc0vIGyskHmEWvpXXhYJmXyJJZuGfrTscChox_28pZCXE9GBx0x1qRpYrYdAtABDnvZc6Dok9MUnIC3-mOKypoduNWiehRRTbw77IbmFzcqc-lx8Bpu4Eqy-wu1idDdOR_R27voCwKX8IJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f927e35e14.mp4?token=JsfPY5cKoX0t2dNpN6xGleGwOJz0JPplM47sLezEwWB0UcB3HACBell11IoEork7f9Mp8CrGpQ8EBC7SyKPALyM5UkA4B6NXh-nnAYWTDtSBh9cVFKKx462XI6mSlSzpeyp1LtGNBEbPN2AQsKO3mNa2Ugczn3IwgEh97hr9r9nNyoDRv8d_zyVFFaZdTZLNgJEfQRSmc0vIGyskHmEWvpXXhYJmXyJJZuGfrTscChox_28pZCXE9GBx0x1qRpYrYdAtABDnvZc6Dok9MUnIC3-mOKypoduNWiehRRTbw77IbmFzcqc-lx8Bpu4Eqy-wu1idDdOR_R27voCwKX8IJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
تو رژه قهرمانی آرسنال بیشتر از جام لیگ برتر به باسن هینکاپیه‌پرداختن؛بن‌وایت میکروفن‌گرفته دست داره اهنگ میخونه هینکااااپیه
🍑
تو نشونمون بده
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/22587" target="_blank">📅 09:46 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22585">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6I8W5qJFiVfFkbfBviRHbCq10FanmtpkLKJu4AN-3V90Qkh3dKt3TdYX0CNjpXB05vAPe-H8Qr0FHtAdoBrMcCdLk8VMS0zDKG2NGMaIrdwu69cZ_IAPzkpTolqFhLy_AtIMdlEBIirNp_LYsAdgq76ScJlcaqmLs5gwIrV7zBE8BkyOO4UYH6By3hMv1KMYCP1Lfh9OQncL3rxc3bzDvwOsjJ5L6eLJbFiu3tun8u2KYDmTLvuymzzHM5rz7zxVWTgTygFxBNiLqM-0dkjLMcW5pfyMpUJ2o4Y3M0FfB5dWsaaAstprOD6RrP4FKnNacSt2LENpmP19K-xf-zAEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدار‌های دیروز؛ از برد قاطع مانشافت برابر فنلاند تا برتری آمریکایی‌ها مقابل سنگال  بازی شاگردای آنجلوتی مقابل پاناما هم تا پایان نیمه‌اول با نتیجه 2-1 به سود سلسائو در جریانه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/22585" target="_blank">📅 09:39 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22584">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9282b8e98b.mp4?token=GWenXKPOAe94dlpln_t-nHlrAIWbjVbJ1WWliDjNCYvd4lvxZLwc39Ul9TEuuU-U22HyE0fXDAKT4BWX6Q2qmCQKfXiDz9KKR25QKxD4DMNUz4pRqJQg7xpXlFOTaxS8XJIKRqkQBGYRyqkq3x0w6OQ3FWWbOJ9q8Q1oCYfBpkLev5eHfht0llXIuOrWDc9HPXEQB6hcgioMsMiuYVurIHgNKNZnXbSZYAmzvtZTCUC3TvHPcQA-6t0PMf_fR51c6EOtLm20r6VM24ktR8fUT9Sw_2cOhdGEXlv9RFb-tD4ghqRJ2rBM8h3RDhE_lXI0A1XzdHuNUmCUm9102Cbf8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9282b8e98b.mp4?token=GWenXKPOAe94dlpln_t-nHlrAIWbjVbJ1WWliDjNCYvd4lvxZLwc39Ul9TEuuU-U22HyE0fXDAKT4BWX6Q2qmCQKfXiDz9KKR25QKxD4DMNUz4pRqJQg7xpXlFOTaxS8XJIKRqkQBGYRyqkq3x0w6OQ3FWWbOJ9q8Q1oCYfBpkLev5eHfht0llXIuOrWDc9HPXEQB6hcgioMsMiuYVurIHgNKNZnXbSZYAmzvtZTCUC3TvHPcQA-6t0PMf_fR51c6EOtLm20r6VM24ktR8fUT9Sw_2cOhdGEXlv9RFb-tD4ghqRJ2rBM8h3RDhE_lXI0A1XzdHuNUmCUm9102Cbf8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
یادی‌ کنیم از این ویدیو پارسال؛ میکا ریچاردز به‌مارکینیوش‌میگه‌میتونم مدالتو لمس کنم؟ هانری هم میپره وسط و میگه بخاطر اینه تاحالا بدستش نیاورده؛ مارکینیوش هم میگه منم مثل تو بودم
😂
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/22584" target="_blank">📅 09:39 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22582">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sZrIfHOXJ0FhyJdlbOYr5CcuuU8RSmqsxDADzwp1zeP9lapmeX_sUafx44SCfjKmcfMLtQz2qf2xYQY0ggT_ysWbSbQdnaKlTI3alx6B_9ybsmJH33RYG48XyjAAW7p0vUcNAaQjymR9tlFooGo7bWAUxqLqxVRZAusL5gbsoVF4y2aRNsser7rRTu6l9CsneDvbG5XPgkD2OxS0F5dyErmhtNuPEgiUvLOKULOY33oTpdhpSvVbfRofiV0h7LpUmNs4nFUeHvw5s5HCnsqA1zpm18SFKcARy1pM50eAvCNKaCsgoop82tBwd7OUDc8QNmwJi2kyelm1MEjiG2FnAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛
از جدال یاران هالند برابر سوئد تا تقابل ازبک‌ها با میزبان جام‌جهانی
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/22582" target="_blank">📅 01:54 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22581">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGJUQBHxVgxdRZX8JgtUSVV-SHiiEfnn_9L11oICBkdMO0RqSDfbyEupufdISojG7wfiw3q7uQmi0230N3OAyw_hOpeIIWRDTFrpIjgAXWISE7GLuxjAxIbYzvJmGocic_qy9Mr7o5MHn0yHjXcMf-ImHNYDLrIdmidOf3IotYU6knpF0INkhJWICMIxVuPM81Ev6iVYipHDjK8V7IZ7hQOZ5sEe-_tNuqBECoFCc6gNf1td_G7154_eNDQVWzKyN0UWcjmPll7mjbExy3J2B8_a_786HCpx0VF8mkhXgtyHpZaaZrzxh7BS9f4YsNtCnPQCZz1WU_Z26cI4gnCsvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدار‌های دیروز؛
از برد قاطع مانشافت برابر فنلاند تا برتری آمریکایی‌ها مقابل سنگال
بازی شاگردای آنجلوتی مقابل پاناما هم تا پایان نیمه‌اول با نتیجه 2-1 به سود سلسائو در جریانه.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/22581" target="_blank">📅 01:53 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22579">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oRuIaTolOY-INglfxGSqxpPL7tZkU-7ExKTGPvFFoNHwrmS4yeIDTyPQKaA6xfRTJZTzAeUj1TVxoLy-RDg5Rfe7bwd8Eq33Y4DuwDFc-70FCPuffIihmUnBhHzJq9u-SRPrAsBsGVcvxQoK7Qj1BmhwaXPAVTdXi_dnz758LenpN9P8SSrTCUhBUjvS-8YhHOLL6yj3c_LS01C96VN9jEcFM65PjPt9tCYXhGambB27agm_Gve7EiKhzyqwMoYIy80by97CfPjaFgVCcuIGTpgSa8OOLBO4UtaAZET1Fikm8-gQwCHt1e-OxxJl9w8ZzDq5EC95n6FfaDEMgp2H0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dlFBV-BVlhn1cb6bTZUlpID7wVumi6XnaypUFJduuG-DLa59eLn0Wr-g3SEo9wrixT71zW2bWgMmuL-Mf7ZwW-Ml9yXfNJpH3zLG1EneBuS26cJLDKtSZz1xrtoUmRulGZ_bGam-fB7K81rzhFjsmOnPur8A8KV4c-_-OoXdalvEg5Jg6C96AH22J-El3rKI_SbFi5cUsMowkaBxOaE5tMYwOzkGb7eMn_rS3pa5oruEYjuI_UE_64h979ZnEKNfKpFSjAhhQMzykqVMFOIa9F1nkESsYy6XaOXps2kEy0B9YOYTVDRrZ7v4yJv9lPQihTGzzKiIs_ax6JzBCtfZ8A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
مری‌راک مدل اونلی‌فنز قبل بازی فینال لیگ قهرمانان به سافونوف وعده یک «شب پرشور» به ازای هر سیو رو داد. همسر سافونوف که از این موضوع مطلع شده بود گفت: شوهرم اصلاً نمیدونه که «شب پرشور» چیه. برای اون شور و هیجان یعنی حل کردن پازل، تماشای مسابقه تلویزیونی‌وخوابیدن‌راس‌ساعت ۱۱:۳۰ شب چون صبح باید بره‌سرتمرین؛ بخاطر سبک بازی آرتتا، سافونوف در طول ۱۲۰ دقیقه سیوی نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/22579" target="_blank">📅 00:50 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22578">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IQGMn8Xg1E8CByebm6mkxsHjX5gTQqM3CD3D3FQchVadFVellS3UrATcvcMyk9h0Gkfh89PjpdKNShRbQQx7zqIZTM_BFktXcW5oTdNpkbOQ43GDSnc35Vh7MXL_M3NiFmLtn1erI_gugtmOu0SL1Xwblf92Ovb-X4ptohnBnvTKAckQrAbtf_qhxDBYIAfgSX_1q6AFNn1eN1TclPeaM85tMFGtzTotJe0k9FfmlvL83Dr7XRQLSL_CLO5uCOqHa_pF113PcWJwu9CwHjWqwsVg21v0u7cQyyMWo9IeGbrUxvR4cr1LUWhiQkQuCksqeRtGb9vwzPG4yxPZDw8sew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
درحالیکه اخیرا رسانه‌ها خبر از مذاکرات باشگاه استقلال با محمدخلیفه گلرآلومینیوم دادند اما اعلام کردیم خلیفه‌ازتراکتور آفر دریافت کرده نه استقلال؛ حالا امشب‌هم علی تاجرنیا رئیس‌هیات‌مدیره باشگاه استقلال نیز اعلام کرده که هیییچ گونه صحبتی با او و باشگاه آلومینیوم…</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/22578" target="_blank">📅 00:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22577">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/909763a6a9.mp4?token=CmfK2as2wM9nUFA2PVen7yCMjh2NaVG0EsgDTfFseezFqpGU4V8a-07ysXHa69-cOqE9d4J96w71uYaw5P2SZMEYwVIwda2v0TqHu73T5oJNC7DGWJcINIAXe57ikrszaeK0FnBmA2XSa0Hf8-92INMPkDqWUADjBhuwz320H9WYB0xEa2wiTG638FEQM6XRwxoZN9bGjsySbC-bvGh4uNrOEHr5sJZ5DDE1Ny3LwqX-VxpPA2QlEL2wn1s4sNOq9QLWcJAiD254_yV1l3hU_uNzJRixGAge4JTSfE4RcnInOp75LTQFqiIL2Q_Y-zYR4IA5a4mFE4n9deBA9O_97Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/909763a6a9.mp4?token=CmfK2as2wM9nUFA2PVen7yCMjh2NaVG0EsgDTfFseezFqpGU4V8a-07ysXHa69-cOqE9d4J96w71uYaw5P2SZMEYwVIwda2v0TqHu73T5oJNC7DGWJcINIAXe57ikrszaeK0FnBmA2XSa0Hf8-92INMPkDqWUADjBhuwz320H9WYB0xEa2wiTG638FEQM6XRwxoZN9bGjsySbC-bvGh4uNrOEHr5sJZ5DDE1Ny3LwqX-VxpPA2QlEL2wn1s4sNOq9QLWcJAiD254_yV1l3hU_uNzJRixGAge4JTSfE4RcnInOp75LTQFqiIL2Q_Y-zYR4IA5a4mFE4n9deBA9O_97Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
پاری سن ژرمن انریکه کاری کرده که دیگه تیم ها برای قرار گرفتن در بین 8 تیم برتر اونقدر تقلا نکنن؛ جالبه که از این 8 تیم 6 تیم رو امسال برده، مقابل سیتی بازی نکرده و فقط مقابل اسپورتینگ باخته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/22577" target="_blank">📅 00:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22575">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eCRUV_rwyx2KJI6BZ43aDcEIa38rryGJYmLmiUL4M26U2M4M8NAiau06Y-SbBYGf6bE6zXBDsE4xRjRmivCBaiGDLDBN_d9aqqDHb8M6abP9tUJDtak6yvEOXF0XBHEcLV6hdXTt2gTMdsjeOICbVmcQSbUWFl4ebrzaQYtntu2JuiHglicMK3wYiiIfTxJRMoXhJV6a6F6z7cZnzlmj0rnLLfoZ1AID9EflDqqY0XVjtdlkxCUFqnFRyEWWG6sruzWL9WblHXgbzq3s-R8aK8DiupmYE93wTGReuHPSMAwLG5xsXmUmTmsmIyqEU0jSC8MjIvnfQAiNDl2jUbCrnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
پاریسن‌ژرمن بعدِ قهرمانی در لیگ قهرمانان اروپا فصل ۲۰۲۵/۲۰۲۶ توانست‌درآمدی‌نزدیک‌به ۱۵۰ میلیون یورو از محل جوایز نقدی این رقابت‌ها کسب کند.
🔵
نکته‌قابل توجه اینه طی دو فصل اخیر، مجموع درآمد این باشگاه از UCL به حدود ۳۰۰ میلیون یورو رسیده؛ رقمی که بدون در…</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/22575" target="_blank">📅 00:05 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22574">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKJj-vu_v78DW2rPAeuGG0WiGD43tf4TP4v8HNOG_aDKOiJZd0b5DMrTK4ir00R02Qfw07DY31NjNaMZAlbesP5oBbrZnM-eZyA2WSPoT4J_ZwuEi2slACwcz3YvVXJFdtiMZhE5gbyxdTwyUxLngAsZmsKcy2wJId_sjRaluLiZ97wfOAWcZPNKcrQeO5n36jlTkafWE44KnVmJOTSkRF6U_zEbhwghc-0ixYv8IhqRbKbGA0b-GOPiWgjzxHTbr6I7-TjXU_CtJvFdVtlCwk_V777lg1tbaxsuE-qoLPcEPb7RWeWqLVS1tF67YdIWVpJ-DIKgeoXxif8xbMZ_tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ باشگاه پرسپولیس پیشنهاد مالی بسیار بالایی رو بمدت‌سه‌فصل به آریا یوسفی داده و احتمال قبول‌کردن‌این‌آفر فوق العاده از سوی این بازیکن ملی‌پوش‌بسیارزیاد است. سالانه 80 میلیارد تومان پایه دستمزد + 20 میلیارد تومان آپشن.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22574" target="_blank">📅 23:55 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22573">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uqnea6C7jRpIxkrrxZ-XHBK0xewP4EjozsU4sgWDIjkRbeDWADXZ8XLzACc67EOfp02J7XkkrkctKGHDDFRC3aOKdeZ9P35AinZ6SFdfqaKmRbpjbyF6yTmuIIOevFoFUpwesFO9Z1_I1NORYfqr9weErIwSpJTBb8nnoq287TW70QBVAHQ6E8Q2X7KX2vat0eQNdJMlk-UUHmoqojbmnssv2A4ATidSzVGwYQGc2ELexAOjiNdJZAzn-JoZuKqTPBd6LNVC29rczqsQyuODw7NB1cLTfma-om6iNguv34INVIPaS94oSxnChrqUyPl0iDEeuJk4lHs1VRVm1uN9_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛ باشگاه تراکتور قصد داره درصورت جدایی علیرضا بیرانوند در نقل و انتقالات‌تابستونی با محمد خلیفه گلر جوان آلومینیوم اراک قراردادی‌چهار ساله امضاکنه و حتی صحبت‌های اولیه با ایجنت این بازیکن نیز انجام شده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22573" target="_blank">📅 23:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22572">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3f2e6ecbb.mp4?token=pWhbMVu9pwU2exbp4MIkf8vqIniFpyAtv6oIAGrpJxTCtEg4Q8TY2eNvJi9zH40k8c-6B4tm3k3_0VsdnCY4pSZJfQcUD9jUOFwhB55G86qh47fYN3hx_aKttfTAnxLbyNoKEpAM-TVzyTIb6XDleS5C3hO9O3Aa-EaERCY15hwcW4wzRZckaUm8XmjecR_ZqUgkNXvrqtl6xP5K0_tSy8eqICABFqFguseyx9AhowZ0S8AA5iaUs0BAYZVDr34oEsaMUwNeujII6qGINXaD6PAIU8Cl8BLbGvii9x6709fBpm5fidaw_QWiux7R8Af0sJrpGmXs0s-AmUdOxwBaxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3f2e6ecbb.mp4?token=pWhbMVu9pwU2exbp4MIkf8vqIniFpyAtv6oIAGrpJxTCtEg4Q8TY2eNvJi9zH40k8c-6B4tm3k3_0VsdnCY4pSZJfQcUD9jUOFwhB55G86qh47fYN3hx_aKttfTAnxLbyNoKEpAM-TVzyTIb6XDleS5C3hO9O3Aa-EaERCY15hwcW4wzRZckaUm8XmjecR_ZqUgkNXvrqtl6xP5K0_tSy8eqICABFqFguseyx9AhowZ0S8AA5iaUs0BAYZVDr34oEsaMUwNeujII6qGINXaD6PAIU8Cl8BLbGvii9x6709fBpm5fidaw_QWiux7R8Af0sJrpGmXs0s-AmUdOxwBaxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
یه فلش بک بزنیم به زمانی که لالیگا اسپانیا برای رئال‌ مادرید و بارسلونا درواقع یه فارمرلیگ بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22572" target="_blank">📅 23:27 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22571">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GMI9bhFxZJtc831uo6csGngDFPAOYtjB3QDRYlsa-TD3KVRxJtQKLR6Q1IFcaMUQbR0Xt7RYHoVGMJG37O3-9nJM5Hlb3vR_o3mCM1NoLoNFpLVUe-zELIEuuPk7dHLHzwnFdsllbUk3IHa_HHFIh-bC909Ddi9TKMB-lANL5XobhaowqrYU3IMgumTUL5oYEu-vXfvfZlbFZUc1-Rykb3aOYYe7vVxuuq9BNo2fA8TF1Ajn0CsWuJpgpTJSkV52enEwq8odeFv5UhqW79_FGJcKN81wWkcJ1E05XtvqlAIYAu_VZIl9IUtPqbXGFdnZ70a_GN66-ppa95QMgqAgoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ابراهیم کوناته‌مدافع‌فرانسوی‌لیورپول قراردادش رو با این باشگاه تمدید نکرد و رسما از جمع لک لک‌ها جدا شد. کوناته هم اکنون بازیکن آزاد بشمار می‌آید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/22571" target="_blank">📅 23:15 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22570">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GoWJ4vKJC17hJKfcT-qQUXj0spwtcesDd3wEtDTowOqGSwZ7aHJMv02Vi1IeDkxRy0cG_ezjjm82cU3h0KFMqbvRkfq5QT-jo59XGdJeOX4Ay4N7sAH2riKguPOTKTpSEBEsnRwP7ft6neT-XUYOn90zQmXP4lZNzDrSfXz2FTTb5oEG4Ayjf7JnSSsLL0wECq2NbvrR9TP9UKNbY2hW598rs0d9cRpid9SyY80qvQ40wxWi7kyaHar8Y9tKzFfsxYJS01B8cM85DcdFka-Bds7SZ_b9wGodOL1muw_Wxv0l4Itu4xLeodv5e14nxOUx4Sb-lGHWen45oWS7xRIWuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ایجنت نونو مندس مدافع‌چپ پرتعالی PSG در تلاشه که درتابستان پیش رو این بازیکن رو راهی رئال مادرید کنه. مندس اعلام کرده درصورت جدایی ازPSGتنهاحاضره راهی رئال مادرید بشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/22570" target="_blank">📅 22:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22568">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EhQrP7oqmu8KmW3s1PdzHzp4duEhaw5oQFKWBIj8XbGuPeQWcc-cv9apvBJqApsIiyJXMb-Qac4Dqdx3ZoJaZdGkY4D8xNBAZoGBo2nc_DLS5OfMhL2TZ0W9-hzlnRJI1NzRWYzJqJqpF_ypsOOqslJ1-O4s74YtM2G4U7QEHsPmPuy9_az3jTe4afZfM4fBAWeZ2u_Ke4AdTsl4_wGjfPUlaomgikYK9cwRhJ4kJd6bvf-70ZPj03hYsntHHEM9VAkruWhMFng0yq4Yvf6v_hW6FEgoQECXer-vDppJsqszQjbMcgFLpwO3inaAt_OgngMFaMk57oUhQ-qnrVMgcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E8M0HEM2Fj5FsXdY6RzExgSsSlXQvISz-MX_B857XLVOY-eIKIx6AG0fPxG2jWHz6m7iMZjtZopPWWcjFlAzEQIQWb64c_HNXQuHDZbnVBI0zX0KebkdbgNtRjbGJSyRkHYyUCk_nn5m4aoFStJwmAQ4GZWQWj1yP-lPTDztQRzm8VqftJ1quSPKLTQzAUBZN4YuVLczikDqfPgW-T97hHnAHTep2S5vZK7flE91PsE1THhLwYNBCaHSZBoIdwRoCjRZOA0lh_xs_-_e4NBivKy2NkVhr5do49TeuBpEe3uLU7TFm6BmdSl-gng2QfhfXTEi41o0Iv27ODfST6IqGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
فواید پیاده روی رو ببینید؛ گشاد بازی رو کنار بزارید؛ فقط یه‌ساعت پیاده روی عادی میتونه بیشتر ازاون چیزیکه فکرش رو میکنی بدنت رو تغییر بده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/22568" target="_blank">📅 22:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22567">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c1BpUWaDXLHpW44cdCmdd5YGE84IcF8XwbTlFQu-LRaVSpebU-qvmHta5ZdvxLeXevo34XvNeXRHkCSznJLkgJP2wfL08ojH5H1FcDOXzPj7s9-yoYZBkMc7AY69zJVI4eFzSHtHEbI-YMwBcIYm5tZWmiZtz0A3vpDfZ9sCjJu4PnUDEDjVWbPHijq4FedVCr5bmMGM9BxzkNlTbRInCqeyr9z5ojXyBRnK1GNKdiYLE2WyRSMJ87XRXrWcS3lEqIYnOvFpEMKcxJLAHCbYdoME-wywges52LjyvuGtljhP1qcR1vVPmNQNebrhodxtYR7Mkk6z5QK2ykFEhr51VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌انتقالات|فرناندو پولو خبرنگار موندو: خولیان آلوارز بزودی‌قراردادش رو با باشگاه بارسلونا امضا خواهدکرد. ایجنت آلوارز به باشگاه‌های آرسنال و چلسی اعلام‌کرده‌است که ستاره آرژانتینی اتلتیکو مادرید با آبی اناری به توافق کامل رسیده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/22567" target="_blank">📅 22:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22566">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KwAZ5BBBD8iQDkT1QWW2M2EkoKfkjs_4AhZmN1lkE-3zGQoQ_BDTWUQ33SfgJgFylD1fecAvDQs4YSwjebG5NF6Y8_AfjUoixPZ66vMMsNArjfVAEKPSr-0Cn38uo46fP2PRJPkDRUiUXwJs-rbsw1fq7nBu4xjQo1q6QCiQs6M6gTYAf-D4I8YxvmCnwi0C-BmPbJRXR5PpjS0_bm3yEn0QNYTLWhE_PRS5yxDlOolDD9cDJ_hY-IbALKw4LnGvFVM4xF07--Q-cp4_IeK5YeygatY36_DHVTksROlCpgjrSWmQDUd8UluhcdpEDLZEZr7VoWCfHiagmZEhvr9uDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی 20 روز پیش پرشیانا
🎙
رئیس‌سازمان‌لیگ: به این نتیجه‌رسیدیم که امکان برگزاری ادامه رقابت های این فصل لیگ برتر مقدور نمیباشد و براساس جدول فعلی سه تیم اول رو به رقابت‌های آسیایی فصل اینده معرفی کردیم.
‼️
همچنین درصورتی که سنگ اندازی نشود بعد…</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/22566" target="_blank">📅 22:13 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22564">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G0QO3zUnShFBXGQL5wZ0KOxbYpWY4LT6A-qmV1CO-ePhqbiFZfybcBj9WAlwG9HgUEbCDqps3N1_MTzzEVmTDtqe3QlJdbze2W6Z5Fq3D1OM9Ukm6nqoDKUg4cuHD4QOsvGqH5bwIyeBHvNijQ4UGD9KCl9I9Oj2cn9OovFw7u4l3r1wiZdo8-Jj1Tlq7Ez237xh7aQsN84mRbpjOklRIqcFWxttaHpeP89E49VACwnTWbDrWoupEC3tHJT1ew1Ie8tAVgdw_-cMFYgCV2lXxbXZ926mHljoHl4veWoHNpUnceK3yfSG3l7qTfpganM0y0T98QEoC3y-F3_0exvCxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pN80t3GzyC8U4L1qfGm0uZvr-2eWwuLHQdm4n9TOra4SqhqMrIJgqg932lks37w1h5oekdazL_0T5Pqau2-OHwPMnOxZsvd7AYyFCzFa-SsaGNGgriPOAOTtR-BSSPT50AiAyUeoqDXwE3yOkoYDaHNc63faKNGR0fIp_n13hn2NKGcf98kctiwT32uE4xHO186-Ot3a6TTpMAR3OKXdiETFaDJTY2eGKd76hMDBgpjAaz6UGIQYgfRRoe7pVoN7gm_1N_xQ3Dxucwt57UK8TG16h_kyEvo0TjJGURcW8pmQNCF96klWFAl7RD22F_3PAWxq8VWfAsMx2IkZcm3QiQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
خبرنگار معروف ترکیه‌ای:
رویایم قهرمانی پرتعال با کریس رونالدو در جام جهانی است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22564" target="_blank">📅 21:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22563">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1dc755209.mp4?token=MbKc__EtLrtuVJcTntUcq6LYC_RgRqG_RqWkYxlcoPXdoU934uw89og2mmRi40gW8e8mP5TNknTtj82bJxBp633J3OBHu4hYuPb4gzDuCJ7l1XbiVWWxZeJ1ZKO9HPGZjuJ3nltZxs3op3xHY-H_ztyRM7gFlliNwpQvMwhPiKDWSnZAaarKiLAbVq_Fd38F0F0_CJvwg0vkixiRuc7PoqxqpoTjwZ5c1owkqXX98dy--ejRRvMVmEbMYdjvhbB6lD0PjO3ubNZv4DP9oW_Wxt8tPui7aAAc4E0ypeSOUeoSdsmgvY6ip9sa83NEmjR6FhiAfWFQsraZwGkA9LgGJxFR6-Be4mce2-tw52B80ztRy_ecsRGh7wecTafZKfxUuAsw4YD0Iq1zKyglys5ElvASE5vz0XXm2Fqpkpl0tYOT9rz-7daygZOmAU4cWNLFQN0jYAwRhxnBfDmQ2hbgz-61UtcOTD4AavdZEtS5XjDzdc1bE9IzTZdQD02g8L9esBWMB8387wVsuvt4fHlTgzKldwuyFQePjQYNsY95nkjaC6yxMOlIPnseoxaflebhV3oE61M-m7A88gJXVgMXnOzTnBYgU0ZFP9RtxJaNyrFqMfOwSrsDPDNSLgXWoAQCUb3N9riN5COW-ZSHzWoHDOO6YRQjp-cXTKwQZBIpGoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1dc755209.mp4?token=MbKc__EtLrtuVJcTntUcq6LYC_RgRqG_RqWkYxlcoPXdoU934uw89og2mmRi40gW8e8mP5TNknTtj82bJxBp633J3OBHu4hYuPb4gzDuCJ7l1XbiVWWxZeJ1ZKO9HPGZjuJ3nltZxs3op3xHY-H_ztyRM7gFlliNwpQvMwhPiKDWSnZAaarKiLAbVq_Fd38F0F0_CJvwg0vkixiRuc7PoqxqpoTjwZ5c1owkqXX98dy--ejRRvMVmEbMYdjvhbB6lD0PjO3ubNZv4DP9oW_Wxt8tPui7aAAc4E0ypeSOUeoSdsmgvY6ip9sa83NEmjR6FhiAfWFQsraZwGkA9LgGJxFR6-Be4mce2-tw52B80ztRy_ecsRGh7wecTafZKfxUuAsw4YD0Iq1zKyglys5ElvASE5vz0XXm2Fqpkpl0tYOT9rz-7daygZOmAU4cWNLFQN0jYAwRhxnBfDmQ2hbgz-61UtcOTD4AavdZEtS5XjDzdc1bE9IzTZdQD02g8L9esBWMB8387wVsuvt4fHlTgzKldwuyFQePjQYNsY95nkjaC6yxMOlIPnseoxaflebhV3oE61M-m7A88gJXVgMXnOzTnBYgU0ZFP9RtxJaNyrFqMfOwSrsDPDNSLgXWoAQCUb3N9riN5COW-ZSHzWoHDOO6YRQjp-cXTKwQZBIpGoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
هفت قیچی‌ برگردون‌های برتر تاریخ رقابت های لیگ برتر انگلیس؛ عالی بودند از دست ندید ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/22563" target="_blank">📅 21:47 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22562">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZVWgGVqvH5HBtYwrJxqKRGUZtH6bKbw-YWLVEGl0mVjONgDyweKjESpN9K190FK3W9QSltsT7GwGD4uvW3i63CbJdGbOgtBF9J_jvWxjxq2Ch-ho-_EnPfcUaq5xvikII6BgWuE7JysaYcWScvctjoUT6Kct_-lSh44E2rVgCRS5IDckrMf2uiSp55bYE11e7aoF-EAImgEy-eoNitnAL92R4J82M0lWSH2bR8Biokp2c5AS5y7UOlIdicm1Vu16bX4vbylYYK7FODii89m_7B7wiRFC_cnQHXAheqK3KWkdK8t3HmxjdYSB_AuRB6VZzK7bBLRL-RE95yrTZBtgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇺🇾
#تکمیلی؛ خبرنگار موندو: داروین نونیز از طریق مدیرام الهلال آمادگی‌خود را برای پیوستن به بارسلونا اعلام کرده‌است. باشگاه الهلال اخیرا ستاره اروگوئه‌ای خود را به آبی‌اناری‌ها پیشنهاد داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/22562" target="_blank">📅 21:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22561">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HcB-YDxFTp-NyMB7_PLgDXwlQPcDYiL1Bd99z0sEj5JR5zKfC9uiu5cpLwj2HmP2vbz9-3xeTNITycmDtz3Yw_aJXcJ8vsChj6igvsXTmyei_xOOVRs4MRivwwdRNkr_NykL19qfYzirqzI4onmbC6huX6mMel4J1oMq8v6gNFN32kTgRPNmr3xJWi6M_np1uQ6jFoaD_LvpMsM7yQYNc08Tn2xzzrWD1h7D5vzfLfL6FjxqhmTSGNs99sRB_w8YTi1aZoUOdEG66XXIZrC53vsrn0tjHqqaddMOjpdYMSCDYVuoL2p1-QMOh685_XtLm2yNrTXKFq9-Ol-hbJ7dBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ مدیران باشگاه پرسپولیس بامدیران‌دوتیم چادرملو اردکان و گل گهر سیرجان تماس‌گرفته‌اند تا رضایت این دو باشگاه رو برای رفتن سرخپوشان به آسیا بدست بیاورند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/22561" target="_blank">📅 21:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22560">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JODISDbOCF0_8Vo6pI6Qy9rlC7krzquLZnWwCFhF1NjXbwvDMzjVK5YYv_Q9RnDbbsJcbOEM1mFK3xAzdvtoTHvwAYSgI7vo6a4jLedIsxGnGkqI3jYbbfM-F6BLSBefAnFtWUwrzHLmP7B4VYteKYfhYjsKGHIGJrO9hLYqNQ4rz1NjrSIjbPaeHM1fjBZNChZrqfmVoPSzJB5lixPGux8ghnE537oxYOBSpdQRjxmPvFQ-E8JxOt6UnTK5FME0Gu7-BGVaWy-nDDvlEgL2RUfIh8_MWlujk2hsnyGngEYfNhxiHVE8aBBriKd6pRUSL0S8pKLaUQxCDbCQMaqKLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
علیرضا فغانی اسطوره‌داوری ایران در اعتراض به کشتار بیش از ۵۰ هزار نفر توسط نیروی سرکوب جمهوری اسلامی در جریان انقلاب ملی ایرانیان، با بازنشر یک‌ویدیونوشت: «برای بقای کثیف خودتون، جون عزیزانمونو بلعیدید. قرار ما با شما؛ نه دادگاه، نه‌بخشش. رقص و پایکوبی روی…</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/22560" target="_blank">📅 20:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22559">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NV8kNIHLkvzknKV7FC4Sml3RBTzmAUEjJeGvpC8KsfLYRZerpciFzwVXK3ftQNvd2faG6rQ0mT8OIuwAMUztmXEpaQ1CSkJGqzcTJvSHhPMr8aEHNKHRIlUuPbdYTOXvkbEtkRxczWqutVw4ZvkYhhwBuTpOWnMdNKYbj8FEfR-1Houfx289euxaDbul1IDEAlrKwkwP3q4goIy2exWmGrdvIWefWwF8N_MdQ5M0XlK-RC0qlh03zW1dD32NYhNyYsSFzBbCBRgsIJW-qR6FhrRkvxZAkOH8x5JWcCjeQsdp4eHsO-iCzCR0i_T2km2TrzDyMmORt4v3lW9G_Kr11Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سرنوشت عجیب امباپه در UCL: سه فصل آفر رئال مادرید رو رد کرد همون سه فصل رئال قهرمان چمپیونزلیگ شد. بعدش این دو فصله که اومده رئال مادرید که PSG تیمش سابق داره پیاپی قهرمان این رقابت‌ها میشه. دمبله هم تو قهرمانی دبل کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/22559" target="_blank">📅 20:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22558">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55a2c0be9f.mp4?token=f4tYMh1ss_tkYD1vhzM7Sbov2UsphizVdnGW2SDZoQN6vA_zIyeK62tIjp9V37_-HOJiScoDXaMVZ05-tVeXrmqyhB2fePJ81haYpIAMXkxpvQK3RnH3hzqs78A5DrOvmgQfLDOeNhBgwjAUQ9aLji-kIhpob1hqLaZsBOrDQvYLyieDWXImkv1XR3UuT5eRVTqsOC19PEUDtSl4SDyeUmu2FPu6r0VFuXsdRXC3pheYsjSvjAUCyjzjJFBPmlKP2daEJlwVbJZKqJk4pHQeKpO8VsU7a3uj42gVjuIy8IWRIHU4Imwu56yc9uIkuts79TdK596w0s6cD-NI_5wvNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55a2c0be9f.mp4?token=f4tYMh1ss_tkYD1vhzM7Sbov2UsphizVdnGW2SDZoQN6vA_zIyeK62tIjp9V37_-HOJiScoDXaMVZ05-tVeXrmqyhB2fePJ81haYpIAMXkxpvQK3RnH3hzqs78A5DrOvmgQfLDOeNhBgwjAUQ9aLji-kIhpob1hqLaZsBOrDQvYLyieDWXImkv1XR3UuT5eRVTqsOC19PEUDtSl4SDyeUmu2FPu6r0VFuXsdRXC3pheYsjSvjAUCyjzjJFBPmlKP2daEJlwVbJZKqJk4pHQeKpO8VsU7a3uj42gVjuIy8IWRIHU4Imwu56yc9uIkuts79TdK596w0s6cD-NI_5wvNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌ازهواداران‌بانو تیم‌های حاضر در رقابت های جام جهانی 2026؛ شما طرفدار کدوم تیمید؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/22558" target="_blank">📅 20:37 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22557">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYJssyQOs9-Em8wNBHny7mFhOU8Lb8k_odQRdMs0VPDNOx_B9LFQV09Se4ppSQdcZKSImLtC-Q1kHrk2sADWOsZyCxFVkP8TkGrqMs5sSx0vRn6fEMUae4oot2EzimerZ3mtOkORn4Yd43Qi6Juqe_JqS0Qv-r2TVGCrge9LrO-43aAsflRKz1rk8pHsRY6n30kQWO70dWopWS0UEiui50nsJZeYOU37NYIxHJR_bjgwmdFAwbB3imSgS-RHAmBGpX8JTNIf7gQVGWF3PJ1oDEUHMtIlKN-EvSg-ccjfYnnBDPBrxaNWhjc7dkPnZwFjCF3-s2QrK2FhXvmPVM9W2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#فوری
؛ مسعودپزشکیان دقایقی‌قبل به دلیل تسلط کامل‌فرماندهان‌سپاه ازسمت‌خود استعفا داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/22557" target="_blank">📅 20:16 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22556">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPq6Y7ighK0moty4ELqQh6eU8lgxyWuN0BlOixRXS6cWx4f1Te5JmOEiu55PCacbkStA-svkSKLkWGybp1O987HrOJYSdGDDi9wQmvc9kj724jMJbVpZ4oMQMzyCgB84sTvsW3_MhrEQampGmxSXfGX2XAFKdphfyUmC-dSZmNaFvSiEpeWWHA9I-_gfN3aRL7upeS5l7eB38nez9CZYbCG7j8caX0kdFM7-5mpRLhGGdEA-OFfDofxot9pyEv3HTWUywpvXk8nGRGYid1nHmCvtKBqz9UV5FKhk00caTyU-_Q0DLBxtI7tmpm6KSMPagWJ9sOgvDHpieS041F-siQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
بااعلام‌کنفدراسیون فوتبال آسیا؛ مجوز حرفه ای باشگاه سپاهان برای حضور در سطح دوم رقابت های لیگ‌ قهرمانان‌ آسیا صادر نشد و فدراسیون موظفه که یک باشگاه لیگ برتری دیگر رو به AFC معرفی کند.
🔴
درصورتیکه که فدراسیون باشگاه پرسپولیس رو به AFC معرفی کند. اونوقت سرخ…</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/22556" target="_blank">📅 19:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22555">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4-QzYMt_eAd9rBpEBFbcYHti3bjGNC2VsurTtL1Dg2TQJaMx7j7iaiD1WLpb3VqtvJFTbQ5Aji580IeWCZxfYcNHOjMjUBqtWStkhTZTeG8x_Y8_mz5aEGrcW5oiRtSvOBgZRZkxFwn_CkhLZ7BmOjlm1F49-BTz_IvGw2z2r18mhI--4lajHUyi6LrYURHNv48GqyY4_1xZy_VXyOFtty7gUIF3xlW2No67g6uYzXfUSIc_wC9cJP_M6Z7o3ypdiQqiJy2Hv-gSbs1-o3i52PDBRrdWf8Ys5E6Oa57Z5M8V2Fc3db6CLub7CNBlRDvX3Xj6JnwLyxodGAj1fAWGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات|کوناته مدافع‌ فرانسوی لیورپول به‌سران این‌باشگاه اعلام کرده که پس از جام‌جهانی از جمع شاگردان اسلوت جدا میشه. از رئال‌ مادرید به عنوان مقصد احتمالی این بازیکن یاد می‌شود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/22555" target="_blank">📅 19:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22553">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eLO2kQDoFyodWmY4p-bTq88TtbsYpfgfFPgjWvDjO5h6kGNjESC1ieg5PS1QijoSu7jDXtcFLr_SXH2UkXmmY5ApvlP4WsUOHhvBjV7DtsTVrv7tYvtKhasJO7NomFxlsfjWUcrKryjrm6-HV1ldjDW_DhJzjbYQRSJg7BfOheKiIBOdD4VW8pzW6tIfd-6NddihrHraPffsjQe2RrOlDT6gU3B7uChDYMpmVinGOFNDS_PYfkH6MrFLIFOior3TNOyAc7wGkxw1emeDaFfwtUGxwjmgHAvp1XIigDQsxFWxvhCp3gQvWUL4aADvz92DQy_KUdHLRT-UXWt-S4ZmsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌انتقالات|موندو:برناردو سیلوا پرتغالی تصمیم نهایی‌اش را برای‌پیوستن به بارسا گرفته و به هانسی فلیک برای‌عقدقرارداد دو ساله با آبی اناری‌ها قول داده. انتظار میره بزودی رونمایی انجام بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/22553" target="_blank">📅 19:17 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22552">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2LG_NQWS5WwpsNr-oSLF8bbRa2GV3jMHyx959Fkqv5D-eugThBDBB4SqxaICcIBGk0KrurLa0LQm6yVKo6kgrz477JWwAfz28avb-PjunBLNI6bxLhhr3ntVr7b_JfFWocCEMvmymIxpUgfoVRdzeLNxD4bmtRR-wcR9FqDvm6se1TK3pjjILISg7aiShBeuJ3cfJE9-juF1ZtFsgtj14NDjB4UImpSABLwWh1ato9p7UzGQjKElF802ApYcin1dx9dSvOXARlYwTS7hFvHwTsWETFzPN963hi0J8hbwv22b4rHMq1OMnBHLu15rH74WuBkc3M1JRlB5SczeMC_Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛مدیران‌پرسپولیس به فدراسیون فوتبال اعلام کرده اند درصورتیکه این باشگاه فصل اینده در سطح دوم‌رقابت‌های‌لیگ قهرمانان‌آسیا حضور داشته باشد موافقت خود را با قهرمانی این فصل استقلال اعلام خواهند کرد. پیش‌تر تنها باشگاهی که مخالف قهرمانی استقلال در این…</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/22552" target="_blank">📅 18:45 · 10 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
