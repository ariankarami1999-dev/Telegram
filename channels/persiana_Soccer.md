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
<img src="https://cdn4.telesco.pe/file/t__wUD5960hfXh1yJzC1VboECe33bVVc130ScU6CzuLMnVPSJ1z8_IElWBps-Ya-jwkz3N-gF55iFyySrQSHJFl4XnWK8TUP-4TV9B1FXWUozqNLN0UW1BiXlXh5PvDY5i5FzPrCUgGUkInFiGcjmwSpJAMMfu5mkyOl3ixhfmbnYSOQxh77fdbFeexTdvgRUGl-n94PUl_BwykOCNRB1jqTfl7Po8aY7OU6oXwjej0mMqQdliB4KoojOuPbKyuq9gSEQM0kJd76mINUPOWVbehrU3VzpVl3nqFsi43_t1IPketbQsb3eea_J0a-UjZT_avp9lx1MddaDI4GNRWb-A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 479K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-25 04:26:11</div>
<hr>

<div class="tg-post" id="msg-25825">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nl7yIoSIFVxt7bRdLSt2_wfDcjHE50AiBiqrduLpwfh2jTQGQLNFLfHVcj6oOnsDMQjuRpVsru00WkXRQOue0UWli0mPRuePsUCyK9mdevFrhUPf20KILLN5cH0y8KspkHx0HionXjXj12heDDqvDeuGV-mDg09klreecnKgHnEMcZWlYtbUp3m4RhB3OVsNHmN-sc4uzxHVhbrbNyak6homBNvk_uIdpJRn_1I0mRWp92j-rVqOnf-jOBHWOevgbG5znmPKPTKmLza7efCFNp8a_PJBT2Mo2gHKJDEK69dpdqXA28k6eSo4AkV2j1KvWwAh-z_9AIQcuOnumB9o-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
#فکت؛ تو تاریخ بنویسین، مسی 39 ساله، پرایم هالند، امباپه، کین و بلینگهام رو گذاشت تو جیبش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/persiana_Soccer/25825" target="_blank">📅 02:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25824">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LiZZcVtczkCjPLF7wgdNyVFnMYgzv-vbsHjKU_G2pfMTxJOtdI2cWeuYDSQV5CVlICy9OS2duw0PqfPnPpct0b3SyShMhQ6uZVvl1X3LCSvka4ltWR-k3wsNZdfkZfo4zufWVqK2MyvxYsTjckRzhbe008uabGZ4Y8W_wGfMedspg4gJ6mM8znCyguqfFpmHUxebpvH9vR7lOHt16DLK-Af7ndemBd71nrH1q7ONYug71CxIJC8mahsG9MwalLa2neiGTEiAmPmsphAakjpt8-dxaImy-fmwUxrybCZyqxIQlq2XQwl1fqDm7_i0WG6uZxusSx4xjJfuL-nYuyWdBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه ‌تنها دیدار‌ دیروز؛
کامبک دیوانه‌ وار آلبی‌ سلسته مقابل انگلیس بادبل‌پاس‌گل لیونل مسی؛ جام جهانی 2026هم به‌آخرش رسید. روز یکشنبه 22:30 فینال و قبلشم بازی رده بندی. بعدش یکم استراحت و آغاز داغ رقابت های باشگاهی در فصل جدید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/persiana_Soccer/25824" target="_blank">📅 01:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25823">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29e18a8789.mp4?token=lYeZkKmeX4jzAE6OiDhSElINAJENgkXtl0b9APuvbvRb7NrWufXPFk05UvQrKVdoV3w3flzrdXUhl82pU0wuDKUcRk2Qr9vmce6Kp-EiqxnYu-OcKJAbLu85CZRvLAyz4asz1rKUJPSwIypwVkpkko_O7WLPCyPXuXVcjZpiOUGJRqw-c3T_u7_jh7_ccZbEtlMjYN_cWcDDO6Ue12JNWZtG39lrfCj4z-uh41qHG6k50Xgul1kjXz5DuDF71fu3uE46OZeNtmSQtmVtHBYH80RKHfYEWd1DxmORqtUO-BpvJlYTk1d_C2l326ryMOOjorUk5w3WzzJTr504RZahDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29e18a8789.mp4?token=lYeZkKmeX4jzAE6OiDhSElINAJENgkXtl0b9APuvbvRb7NrWufXPFk05UvQrKVdoV3w3flzrdXUhl82pU0wuDKUcRk2Qr9vmce6Kp-EiqxnYu-OcKJAbLu85CZRvLAyz4asz1rKUJPSwIypwVkpkko_O7WLPCyPXuXVcjZpiOUGJRqw-c3T_u7_jh7_ccZbEtlMjYN_cWcDDO6Ue12JNWZtG39lrfCj4z-uh41qHG6k50Xgul1kjXz5DuDF71fu3uE46OZeNtmSQtmVtHBYH80RKHfYEWd1DxmORqtUO-BpvJlYTk1d_C2l326ryMOOjorUk5w3WzzJTr504RZahDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
واکنش‌برگ‌ریزون‌اسکالونی‌سرمربی آرژانتین به گل پیروزی‌بخش این‌تیم مقابل انگلیس رو ببینید؛ چقدر تو خوبی مرد؛ مگه میشه تا این حد خونسرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/persiana_Soccer/25823" target="_blank">📅 01:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25822">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🏆
تصویرجالبی‌که ESPN با عنوان " لیونل مسی و بادیگاردهایش" از بازی امشب با انگلیس منتشر کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/persiana_Soccer/25822" target="_blank">📅 01:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25821">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QLrcfHAIJE9i6_dTJ8pU1QiIGR5dBaM2wjsQI70Z3QWfTdsBbojuVhUy_Ab3ycyQW_TSjFKUGlhOIq5K7YTUVF44-jHy33GTj7cPI-A5FL9u7-jkEm7N0s9ITDOoz4Sk5AFhPHwqjF69osqH4bC2amPhk9_K6SW84CaQ-Bs-W1CNZC2ZcKj5eRBX6NjWXvWvP9Qx08EQZmKuICBhmij9bMFwJ-8JvlrrdUXB07sR1M7AF3STd54qdCiC8qOgHx2XoncK1q1eVn6VqU8jDY9a7I-6XJr_aTxi2kgvamWWLUJ7S802s2Nx5h0jV-zy324wFKdoc9xRF92Vwd3sHDXvag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
انزو فرناندز ستاره آینده رئال مادرید با این شلیک دیدنی مانع حذف آرژانتین از جام جهانی شد؛ دقایقی قبل هم گل دوم رو به انگلیسی‌ها زدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/persiana_Soccer/25821" target="_blank">📅 01:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25820">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efd102a0a9.mp4?token=LaaVBJki3vC3xGxCur_sB_YqvAfahrj9Rg0oXOZklCecg0SIUGchnWg33ao4LjdvXxAJx43U7z8QBa8kMkXMyFvV44r0vHicnPTK8CdbCFUsNmbuNqR4S2RSJWDhxDuGf3nDMRs_DNQRuPOWufY0Qh7iWSrAL5kQu8ySkpkiCIFbyMCT8tZ3pztN0Z62SjsaYfQblpenqlxyVS5fzLJ312lY2Lxbo1Bad8k-i9_R8nRvn3DIkyvTR3IBadueBPKnv0lrLiksW1iAaYbtH1tADjzJtsyIFprGO2As50tBavZt4gc4xh7AutHfKETD3PhNgdc_BX3O1LTIOZ9UL_MGPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efd102a0a9.mp4?token=LaaVBJki3vC3xGxCur_sB_YqvAfahrj9Rg0oXOZklCecg0SIUGchnWg33ao4LjdvXxAJx43U7z8QBa8kMkXMyFvV44r0vHicnPTK8CdbCFUsNmbuNqR4S2RSJWDhxDuGf3nDMRs_DNQRuPOWufY0Qh7iWSrAL5kQu8ySkpkiCIFbyMCT8tZ3pztN0Z62SjsaYfQblpenqlxyVS5fzLJ312lY2Lxbo1Bad8k-i9_R8nRvn3DIkyvTR3IBadueBPKnv0lrLiksW1iAaYbtH1tADjzJtsyIFprGO2As50tBavZt4gc4xh7AutHfKETD3PhNgdc_BX3O1LTIOZ9UL_MGPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
سرخیو اگوئرو که امشب بازی دو از نزدیک دید گفته اگه آرژانتین‌قهرمان‌بشه به هرکدوم از بازیکنان این تیم یه گوسی آیفون 17 پرومکس هدیه میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/persiana_Soccer/25820" target="_blank">📅 01:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25819">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Hj14qodLy0kYEqy2XBeZRnFtikMvYmoVNfQ-CgZXH9vgrbOdC6JX_8g3bDO4uLI9GX2bSiRGvyCbdUiVlY7RheRkYaWYce8pZmGvKskXarP5dPRCWISzbkD9LRaGWZr1BoJVtH6MHx3lW89SaVu2gnYwmBtsJKNk8TN2YZqr3iEIm7v3FzVgnjP0CgWZ7U8fnb31jaOfjjQ244GFyKlyXOkbvscA5Ii5CZgRfGe6ug8yvITVPO8-h8EkLL_HhkILWefYGUM7l85qNQYgVwi3VGjK0vuhP4s3sw5QiRu-ZBR2F-ttHrfC4Z4IOQVp2hI-4VXgXYADU0RL1Z52aRjYxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک‌کنم‌اگه‌هرشب‌با ۱۰۰ هزار تومن میومدین چنل بت ماشبی‌بالای ۲ میلیون‌سود کرده بودین مثل دیشب:)
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/persiana_Soccer/25819" target="_blank">📅 01:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25818">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmYJ6fiq_ccNo6ABk7L_Z2u-uJ0o2vpGlF43vplJkrmSP35c74BKqrlKjqq4MtzRuZCaDH2DCYTDVROuD10n4FA_Q889hanbeltrs2lV91iGAqvwqLfZJDWUQwRepXhlZZvHpU0g4iKgm4upbi4tcjLp9caGoZA-quhOdts9SpXs1z_7XhgNNJtZxkzgVPwZGx0NMBqb1-deoP3WkMnVzdQDWgYEUrMw5O6issSi9TPykYwN0OpmkuJytTxmIjMzBlCNijaB0UKtM-obnBwzilLdforuejy_jjVn33xdIcceSRlDATKpAEdBQKLj50Y_RatQ3jUWaPhFiiCpTt64_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
انگلیس‌دقیقه۵۵جلو افتاد و توخل درجا تیمشو تا منتها الیه باسن‌جردن‌‌پیکفورد عقب کشید و ۶تا مدافع گذاشت تو زمین‌چون میخواست تاخودسوت پایان تو محوطه خودش دفاع کنه. تمام این باخت گردن خود توخله. حتی اینکه بعد از عقب افتادن هم میخواستن سانتر کنن هم تقصیر خودشه…</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/persiana_Soccer/25818" target="_blank">📅 01:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25816">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1FPKZem2D_GqdXjMSEUjAC0k-1NLaVITW7SYVNi8z1JPmd9VnxLPXJHrXRgM5_-krdCqrDQk6g8T907hAFHWyNuJ_ZJjwOw_zw-R_u43P04fvrSDo8pGGSHJ6aQZzitGKInAcmVb-cKwnaWC0W7MAGI1cc0XKRTkSUQl2-kT5NnQ2ee5icMU-gOB67l-CZMDvTTW-x1OnuTGkpym_2ihHI4-I1fvAonMWO3-8pVTpnr6KMTMcmk1ISurhMENHxeoAcTOeOaL77-fM5L5nxSmqCSWqM2JSDyI8cZ6pJCilZRKt_y_I_yf29zHCa51tN-Lh3jO8FROpMnYiWWOItSTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
بهترین‌بازیکن‌جهان؛ اون‌حتی از جام جهانی ۲۰۲۲ قطر هم‌قویتره. لیونل‌ مسی همچنان به نوشتن تاریخ فوتبال ادامه میده. عملکردش رو ببینبد فقط.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/persiana_Soccer/25816" target="_blank">📅 01:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25815">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OeP39BCQ9PziENzDbszGIpTEwcVJX-Vg_YKvvTop1Cw4saLAGZUEPRzCiy45BXRpnPsfV4YVF_3Kw97j7ZvrXoMuGZzFFrVL_SMasPbIlDyBcP9_CkmExorirNbSVfybtyNjZ-vKj0l1mgGy2wgkYcCP_pGCNxTRC0kpL147sdjTMogpPb8kOtDSBtPY4rF0vmzA6zjpT0yBegR1I2l6oy_KL9VmTvqE08tzI3021dHH3weByJisSWlK45zUvmGT7x0b52IAHmvAkkasg9X_CJRH_bTGRkMqtLyjtBwBAN4cijVgRdhDKke3444IJBE5L7CKVe5J_G7R1X_2x-UtZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فینال‌جام‌جهانی2026؛ روز یکشنبه بین دو تیم ملی اسپانیا
🆚
آرژانتین برگزارخواهدشد. امیدوارم قاضی این دیدارحساس علیرضا فغانی عزیز باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/persiana_Soccer/25815" target="_blank">📅 01:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25813">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PcEFqQhZ0DllI0yiTumTYgOkTUiCeXYtkbix7Z78b8x-eYXkesKG9tXZWD-1AYtQ2jfHpfK1wpj3mw0zqvW7hlsto4Qy4D3zMzdK5CA-vzgZB6xcreujEM2pOAxzf_fKgUl0vesQZnvAngOyNWg-vVaOte6zdnrnKim8KplGN5A-mIDxrvzDoOTOh3d6I5ll7saXcEjufqYOLPQ8UhXpwY6UIr1U2sWvlIBn5-SWZ2ylS90GX2B66MBxZwMmi3ZR0TvHmjjL3QoCRfEriM8cJXq9p5696-wn-CLyofKqmrY-YFSiUGjXAnhmtZ_Wyhz6xS8v_8DwwVXk6lP9vbK5Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آقا یکم جمع و جور تر بشینید امباپه هم اومد:) فرداشب یه ستاره دیگه به این قاب اضافه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/25813" target="_blank">📅 00:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25812">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MsnydyTGNgktuQxkJT71dQZy8p6wpvuRo4y4zSLaVQlyyQmUj-lHyR6K_DbcMuNg5_nt_8wDQdRh7JL-DAn4y6eFqbYt1_2-p2lVXXeAz2JJEQxjM-kK-xAkkOmIzXCfupLqLytlCqArNB26M0BdUu2ooUZJRbwYWk17CkpjJmSmxsSAlfvofuLQKYWyzYiQVklw9tRJ5J_-6VLqUDtlN3fMUQMM07cX-RnGlioN6fzSgpHi88UdQ-WD9PlkssLaaHUkEl7clf_HOlDAe_7qtfVCOCvArKG001aAB-fU0q-zAjfAKC59UppbP8X5G60emkvoA5IfAn0p1YBnXr0wBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فینال‌جام‌جهانی2026؛ روز یکشنبه بین دو تیم ملی اسپانیا
🆚
آرژانتین برگزارخواهدشد. امیدوارم قاضی این دیدارحساس علیرضا فغانی عزیز باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/25812" target="_blank">📅 00:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25811">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VOCYWebnztwqiXGijjhcwocz_s9UUNfysrJuw89OiLiztK7wDN0_33SMA_MzRaOcx5ApA1wGl3D2GCNvRQpdxW_3_cUvIAFNryUGQH6UwRIroVpDmAMABA9PYWRDDZmWVHxtyFVQ9QXwbapHSD0iQMKSMkrINbvBNibanUV4qEgldZCMwV_UtApiG_uOMMFvXg4nErV3biLinxbsCrWNsLMCmk6178lJD9puLacQ2UffAeHNdJVhii2sbc7sYBhv_lfIyPqsa2FpBK1QyYuP1Y4Wji5PjzFOx6_nqPMhTzJnQHF-7BQT_BOOVRuIPTa4g04k_5Ry0i23sNkbaWHwig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نیمه‌نهایی‌جام‌جهانی؛ صعودتاریخی و دراماتیک یاران لیونل مسی به فینال‌جام‌جهانی بابرتری سخت و نفسگیر مقابل سه شیرها با طعم کامبک.
🇦🇷
آرژانتین
2️⃣
-
1️⃣
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/25811" target="_blank">📅 00:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25810">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lf5WluhlqDQyN3MxbTm6rl7L-HLX8NDbWsrxJTSrtmwuk4vuY-_ymfEE28tCHTfGcExAfm0O247rBnS5xOU2gK6vtH-kqN5Vg7X5AGOR9mRL4HzlvQJVLGULYRcGK8zzvwbDAG71RsvJj3EXd7RTf7vtUjGzVmeb2oTEXOH1LO_iutg_rAyFKVPCz8oGvueZrGe5AuTyNVRFrvMOiMxGV7y6gI4K0njNFj64JySlR7ZWhxDXb4LMj7EaRmSiOfx8cOuo5E4pcnU1qx6BTWrV0gzj_sdk-7EnHo4A8bL2G6C9J3oozbZmsMuM5Svh1lqHpRN7uZNU3AXMaRybhKZ4gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل مسی 39 ساله با دریافت نمره فوق العاده 8.9 بعنوان بهترین بازیکن زمین انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/25810" target="_blank">📅 00:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25809">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZZaIPU2bizYWIGbHu56bqYygynfYgJhPKevcgg-gYWLdekVT_kS8zdYG3Y3gt-shLvalyD6djtIsiL0dynGuPeAhJp1-l51Qt14GKdBRd80DOJ9s1YN0PdtTGAybUSBo45BPgUbDRdRxZyePudO3_0lRnpwo0WPGg_2lyZwoGqRF2ftfoMaggOJeVSKz7muNyr2CWavlLLXo09Kdd2AFypFCzEpe0Dd5a1R6kh9w0HEHDwN_T3OMu-5UhfZpe7M7XQkDLKgthBDwvrxmg-nAAKbo_rK85uAB8ILzuF8rqQu3UBx5mgILZWRB_ZzxVpysPMxc66ZfAsBFv3Rbjn-YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل مسی 39 ساله با دریافت نمره فوق العاده 8.9 بعنوان بهترین بازیکن زمین انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/25809" target="_blank">📅 00:38 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25808">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ovZy_yrznIlZvq2ncejJtQtc33ctt8ch3zSMZf0hiCn-duWoGpERp2JhptA4WZ3LDTKB3uPMre5yfIy3k9izsUbIGXF_0Rxj7uzDBH2ByCStFQPyzeSnKAYTpKgV1gArTTGgMRg6oDhl95ZIjyCh-44pVEBzNlG4jRi9SP-0MbSZBw41BJCPh7p5QmbBNKoppZ3UvqpGRkJHmLiv6POt_XHXpei41plLiEp5qfcxE_A8Lq_Ldi-Acy6-Jf9e1kEbZ_T-XmXSS7ZlU7e1VFpHi2WkDfkfnUfP8Ymw3Gky-9gfgQnMv3a-l40mC7juXDfpSS641vELy5g-xBxPk345Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نیمه‌نهایی‌جام‌جهانی؛ صعودتاریخی و دراماتیک یاران لیونل مسی به فینال‌جام‌جهانی بابرتری سخت و نفسگیر مقابل سه شیرها با طعم کامبک.
🇦🇷
آرژانتین
2️⃣
-
1️⃣
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/25808" target="_blank">📅 00:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25807">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oj0Wa3xfTQSBBpeA4cKcP1zkwzxSbWaBxh0nDd1kW3qAJKAMjnqjxFfqidLzN0dKc_rvhxBFJhsURhUYjjGyO4FwgwPlyRchufNwCfpJKb-z8zsxXFiAKIQMxiy2NclZRv25VxoFvkic89RwH02wSsEyUvY_Vh9rIPZJh1dRtisdX79gDvmFH6-gcuAbr0FFAi9S9vHDuLjUuBHlhjOnOC-YMtED7Qd-XuAKGmcG0qRxZQLjYVUswV2a3o7LpffA9Cj58k_Q3FqcnmqUQVOMkmJxZTAOeNeg79qQpGO04oaofiReE5qIh-Cz3bFDx1f-hM3KRXI9SUDDoLYyGfgV9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
گل دوم آرژانتین به انگلیس توسط لائوتارو مارتینز روی سانتر فوق‌العاده دیدنی لیونل مسی؛ این یازدهمین پاس‌گل لئو مسی در تاریخ جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/25807" target="_blank">📅 00:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25806">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d89d4e5750.mp4?token=AK5MefpCNRmrwJV6cxBsWVKOpaEl6PQkHmhl7mQJLqURUs33xBSlnKUigyhIG3Zz5VjPZcPrOtFZmbPmJbNoagLmu5WgZAyrblIT5Wz_3KuDrKRylZwUaRtEJ_amFl0z4ZHQFmRRpANQ5x2-hlfyzJ7UCx7F813O5Q-itguOLPuwa9YVeTxZpXsiyXs4pQIvyziR1fX2RROuhkTymG3Yh4UP0SjQ9sbWNM9HU3dIcDq7VmkALyZynVzJDxjFR7RE97VRTYHbmK30-NGjdEe_DVF5HUk4Ur832u81Kih2rOp-vP6naAmLC7obHp_y825s7s4bKlnWrvvjXJYyWV_tng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d89d4e5750.mp4?token=AK5MefpCNRmrwJV6cxBsWVKOpaEl6PQkHmhl7mQJLqURUs33xBSlnKUigyhIG3Zz5VjPZcPrOtFZmbPmJbNoagLmu5WgZAyrblIT5Wz_3KuDrKRylZwUaRtEJ_amFl0z4ZHQFmRRpANQ5x2-hlfyzJ7UCx7F813O5Q-itguOLPuwa9YVeTxZpXsiyXs4pQIvyziR1fX2RROuhkTymG3Yh4UP0SjQ9sbWNM9HU3dIcDq7VmkALyZynVzJDxjFR7RE97VRTYHbmK30-NGjdEe_DVF5HUk4Ur832u81Kih2rOp-vP6naAmLC7obHp_y825s7s4bKlnWrvvjXJYyWV_tng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
انزو فرناندز ستاره آینده رئال مادرید با این شلیک دیدنی مانع حذف آرژانتین از جام جهانی شد؛ دقایقی قبل هم گل دوم رو به انگلیسی‌ها زدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/25806" target="_blank">📅 00:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25805">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c0c717972.mp4?token=fsaddars4hUrHUiqz2RRNOyv8SPPXo7blEj_geXikWXfhduTCvvEA9Hwzs4pySSTB1PWs6sdfB_TFi-hafqdhT_Qu7yWcsVYipRjfrnzXNVOsOc8H5BRNuwtTPQK0uw5v51VP9z5JUbL2rsj8CAyufdEfHIYZXClZ-Jn4UvZ9FifpMh04jeavHGIX5qQgtLaFo7vTjxETkS40O5AgBLaEPM6QYN8b59unee2x0cFCYWfSqtbQaTBYQhOqmV5oSQuoKyBEEOeVLrr0QOwayC3ifaQAWGFVPZYCgzyM44WhxL1xJHwYLbhrKsx5x_Fz_rquH63HxzsJP9mqHmyJHTFoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c0c717972.mp4?token=fsaddars4hUrHUiqz2RRNOyv8SPPXo7blEj_geXikWXfhduTCvvEA9Hwzs4pySSTB1PWs6sdfB_TFi-hafqdhT_Qu7yWcsVYipRjfrnzXNVOsOc8H5BRNuwtTPQK0uw5v51VP9z5JUbL2rsj8CAyufdEfHIYZXClZ-Jn4UvZ9FifpMh04jeavHGIX5qQgtLaFo7vTjxETkS40O5AgBLaEPM6QYN8b59unee2x0cFCYWfSqtbQaTBYQhOqmV5oSQuoKyBEEOeVLrr0QOwayC3ifaQAWGFVPZYCgzyM44WhxL1xJHwYLbhrKsx5x_Fz_rquH63HxzsJP9mqHmyJHTFoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
نیمه نهایی جام‌ جهانی؛ شماتیک ترکیب دو تیم ملی انگلیس
🆚
آرژانتین؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/25805" target="_blank">📅 00:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25803">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4db22288ce.mp4?token=nBXRtdhQpMLsmfJR3CfPniXzOSEuuez1-xcGea2pNkFMVp6Er0sgsVFM9NWRjlTtxqE9wWIs6thcI2zohbie10MCuaBv9VIYpFEE4zcMmQA2T_UMb6v0nyk6SjNLPcb6U1GW-8CdcHBZHqSqxShtuzbRIBWSbWdL7b42iHUdQkqHsr1-f1E8nU9EJ6GplXi1g8sTxnInKuRyzjxErFVicVA_BGOLuCSGdA_-BhAYIyPCTUkvpT6qCEPYIpEXLwZ5ZaylSxyBIstkcNV6QDauEO3bYR4hlW5a4IB2CaDVwgvoYX5nKlRqeAuAYGCFcyNF9_jiWwE_nvNKefa8gM-T0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4db22288ce.mp4?token=nBXRtdhQpMLsmfJR3CfPniXzOSEuuez1-xcGea2pNkFMVp6Er0sgsVFM9NWRjlTtxqE9wWIs6thcI2zohbie10MCuaBv9VIYpFEE4zcMmQA2T_UMb6v0nyk6SjNLPcb6U1GW-8CdcHBZHqSqxShtuzbRIBWSbWdL7b42iHUdQkqHsr1-f1E8nU9EJ6GplXi1g8sTxnInKuRyzjxErFVicVA_BGOLuCSGdA_-BhAYIyPCTUkvpT6qCEPYIpEXLwZ5ZaylSxyBIstkcNV6QDauEO3bYR4hlW5a4IB2CaDVwgvoYX5nKlRqeAuAYGCFcyNF9_jiWwE_nvNKefa8gM-T0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بیرانوند: چرابعضی‌رسانه‌هااومدن‌گفتن مصاحبه‌ های مورینیو درباره من فیکه؟ اصلا فیک باشه وقتی می‌بینی همون‌مصاحبه فیک داره به من روحیه میده چرا توهم نمیای همون مصاحبه فیک رو پخش کنی؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/25803" target="_blank">📅 00:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25802">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HsLsHrOWAEEVhVUDrG1UIogHpSuv9FIBzdqI0u2rrYY5bp6Y9ETH67JBrX4znLNN17d3VsFqFMMeFizkxl9BmVXtNzAUJlULXm0R-i4Gnq2ahHSApfDwcdOJpXSwDy8ikcDiJoqIdEQ05Onmm9Ka0k0BsHBvkPPOntAwNxWko_g0CP0i3k7SK0fT6yMDKhJOWmO3q1j3RFxcuktaHFKmQTKgQpGhRtLYcuNBQIlIt2XYr49-HrMHsZ8FyVTVSF3FO1m8VcOB69ENjaMdzXksGo42o3MKkO6EEAirB-FS8ULvRtlVXHxVlhCuCgMcoFW32nEIKYoLrh27OsQJqsZI6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برخلاف اخبار منتشره توسط برخی کانال‌ها؛ درترانسفر مارکت رامین رضاییان همچنان بازیکن تیم استقلال بشمار می‌آید اما همانطور که بالاتر گفتیم دو پیشنهاد داره که درصورت توافق با هرکدوم از باشگاه ها؛ با پرداخت تنها 200 هزار دلار به باشگاه استقلال قراردادش رو فسخ…</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/25802" target="_blank">📅 23:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25801">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FsO6lWmlYZx4vdwgs8XOQVhfchS6Wiic4AgtgsZ6NWvuCRKcdOy0S6koCXrb42IRQB1H82WjrZBtmLIis9QMXUr-aZ6vYKpjJ9SbFijK8nCLfkkF3tG3n5GQQz6Xzxbul7nrGdopeWQK950XqSGghN8sXnB_L_uuSLqEdb-Q1_d4b-BM-5x8b22evPSwGbzEGQB45pp2_MjWnNeDEksXUve5ei6BPTVMb3POFfDUii8C1XzJKp8lIdxsdFsuS9gTlLWgUQ368MrIvwJMXBW5Ekpgl6muz0_4_CfznRXi_FwnIRCsHoI7lteWG5f5-VkFBDE0xrk40QsQycJ0j1jEtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه پرسپولیس با مهدی زاری مدافع‌میانی سابق گلگهر به توافق‌شخصی‌رسیده‌است و این بازیکن‌موافقت خود را برای‌پیوستن‌به پرسپولیس اعلام‌کرده و تنها توافق و پرداخت مبلغ‌رضایت‌نامه به باشگاه اخمت گروژنی باقی مونده که انتظار میرود ظرف…</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/25801" target="_blank">📅 23:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25800">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8axSPAWzmwnKQsPI8bjgwlz7mRCIBI8h1AahwzB4TgQqMFA0J7X0HPlefynVvM0MO7Dp4AG1S24QZnNT1chsIwk0zmm4OKGOZWWINraGp7lO22A32TjO9qfIOoNGr3tckeaS3uG__bBYw_hYpn_SIqzI9TL2zS6BPc1S27pCMKLYIKeVw2sRme9zyu5Qib8ICh9F-DPVjobFAo3vA-zNxf04aQqSajM_DaJVrtD6E3B-3T1Or08t1mDILhAkX2ZC36i79OTz5wT2b3OVEfaNoNSAgYjEj-3SSqTgzseQPffPCr0uh8a-k_mcS1z0BPoeJ5fMolOQqJfs8OoYZOmOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه اخمت گروژنی روسیه رقم‌رضایت‌نامه محمد مهدی زارع مدافع 22 ساله‌خود را 1.5 میلیون دلار تعیین کرده‌است. باشگاه پرسپولیس‌نیم‌نگاهی به جذب او دارد. مهدی‌تارتار شخصا با زارع صحبت‌کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/25800" target="_blank">📅 23:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25799">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30d2d3139d.mp4?token=uXY9WxJ8pgG93CTLJ8KturRkXM2ciqaRwYIcIuFeYb2BCIM1XKirXL4xT56-ij2GOH49jB0bhKXzIHLgI5r-uhp2cdSVjoJNXeP-WS1boWZT_lXgmIb6DyuSArQh3SBuyEa0abQdnUUeenm-1zMQln-IWexMXWQdZ8X5l4IjqgnmXz_g8jZ5knKA6X20kFkTy-V3PAL9ZWqo7M6B89UcrHiqbleGsR3GHN_1Ul2RnWqP2NniDtsRureg9dRV3cMR354_0XkYIaqHLK_e945p4LZGbxJfU0AdDO94MwGU6UVP--dULRsWzCl6jeF7ewY5aEHy_F-Jt3B6FIgadYo15w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30d2d3139d.mp4?token=uXY9WxJ8pgG93CTLJ8KturRkXM2ciqaRwYIcIuFeYb2BCIM1XKirXL4xT56-ij2GOH49jB0bhKXzIHLgI5r-uhp2cdSVjoJNXeP-WS1boWZT_lXgmIb6DyuSArQh3SBuyEa0abQdnUUeenm-1zMQln-IWexMXWQdZ8X5l4IjqgnmXz_g8jZ5knKA6X20kFkTy-V3PAL9ZWqo7M6B89UcrHiqbleGsR3GHN_1Ul2RnWqP2NniDtsRureg9dRV3cMR354_0XkYIaqHLK_e945p4LZGbxJfU0AdDO94MwGU6UVP--dULRsWzCl6jeF7ewY5aEHy_F-Jt3B6FIgadYo15w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های سنگین کریم باقری: مسئولین سرشون شلوغه. علیرضا بیرانوند خودش یه مجسمه از قلعه نویی درست کنه بزاره خونشون لذت ببره. علی آقا دایی هم میگه نگو بیرانوند؛ بگو دکتر بیرانوند:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25799" target="_blank">📅 22:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25798">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_yKkza6KYFUfJ1rYTlitJQbmASfdIkQo509TR7drT48e45x-DjibM38TsbW1nX989xXOwLMEhOFWJ2yy5g8bfoqCIKtiN2-MqteOquVC_-FHkNfj8Bnj4oGjp_7fEoDXuO4jrUfxPBLg2WiU0sjjnYes75ejmRhkHt8RjhrXjs_l7zlBzyBPrpBSnQlVRzItiRVtaJSAWgM2fqbMqiGDFrzchJjh3myGTzwlUouTJBjJKi7b1GqHUP9uqgOJc5yfIQWM5q1oSAzL-KOGc8S8g2vLq492ZFKhWfeXF0ZG7rCyTXcetmJSrYZC19xLFGk-6HVSKvSsxB2wGPtEMkQdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
معرفی زیبای عادل خان فردوسی پور از مهمون‌های ویژه‌ برنامه‌ امشب؛ علی دایی: تیم ملی ما وقتی‌حذف‌شد که سردار رو خط زدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/25798" target="_blank">📅 22:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25797">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c436909609.mp4?token=eG_B0Avi9111S5aQo-sHxtYdxgcr9t1m52FwqRhMwh_m8q0UpuEyZzKKQU4G0Dtwjn3fiLkmZXFSLRNSZLxxXw5atnEkeK5rCN7QdQ_n7jonKZEs7qN7LqDkGoYMdx_3Bx8gZcqxdvvCjun9J6i5rv9XxLf1E-4-eswdsdwg8ptNhnM2RYPtBHCNvEBNmssgcs3NUeC2axg2Z5NsKQ1-O1FOr-8jU53OH8Bej75buzchBekstHDbnTtIMS4jeGQqHbjr2qt5iDK4Z2j2BQYQbdD2rM3s72XRQk9rPwGghHcbcGs8XA359oUNuBx6S-JeOvPt0ATJhwscJ0JAZ16vMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c436909609.mp4?token=eG_B0Avi9111S5aQo-sHxtYdxgcr9t1m52FwqRhMwh_m8q0UpuEyZzKKQU4G0Dtwjn3fiLkmZXFSLRNSZLxxXw5atnEkeK5rCN7QdQ_n7jonKZEs7qN7LqDkGoYMdx_3Bx8gZcqxdvvCjun9J6i5rv9XxLf1E-4-eswdsdwg8ptNhnM2RYPtBHCNvEBNmssgcs3NUeC2axg2Z5NsKQ1-O1FOr-8jU53OH8Bej75buzchBekstHDbnTtIMS4jeGQqHbjr2qt5iDK4Z2j2BQYQbdD2rM3s72XRQk9rPwGghHcbcGs8XA359oUNuBx6S-JeOvPt0ATJhwscJ0JAZ16vMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طبق دستور علیرضا بیرانوند مجسمه امیر قلعه نویی درمیدون‌ازادی‌ساخته‌شد. بیرو دیشب گفت هر مربی دیگه‌ای بجزقلعه‌نویی این نتایج درخشان "سه مساوی در ضعیف‌ترین گروه ممکن" رو گرفته بود تا حالا مجسمه اش در میدون آزادی زده بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/25797" target="_blank">📅 22:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25796">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mx2MTsnyryxDtBHHMBRTM_DAOTwiUTDL92YSPvXoQxb61rQFArBD43j6BB6aoPyZF1SyScSREXCzMTQw_fo_hzd1OYYUriwG-KMCACyUm90wkXZLAsvZp2p0BQXhy5taNbTxyU2DMJ4IpXnmUE1lOiGxg3xo4ku6zLDWlqEXjV7mVnNC1hWHiEVdlZcowFmksA3IqRbrgrNgv0oRkE6qkfLya91RTd76rr5VD3Zf2ZXT1Nf2ALPVY86Bk9zq5XF4jXKN04m3lKeZR-eNv-Zc9s6Go_QOsgKXwrJtuLVxGArKgESgRw_6h0ysXKsPD_E_6xWqkH1s5gT9_N3jqjsf2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
هفته اینده هلدینگ خلیج فارس؛ تغییراتی مدیریتی گسترده‌ای درباشگاه استقلال ایجاد میکنه و بچه بالاخره از هیات مدیره رفتنی میشه. شخصی که تاثیر زیادی در جدایی ستاره‌های این تیم داشت.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/25796" target="_blank">📅 22:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25794">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/113eaa3d5a.mp4?token=IPxthAn9epxc_wXkbgSZMBKA48LXyS9fat0I9j7bFYE0pcc20o1VceKaEpFaNdRsT3xkvnhjx6Yt1khg32cVqMT4hXs7fKbNYonamAK1TNjvISd9HygOJOF39MuOatXOcVxOsYoNhxPdNlnNC_D8Wkn-lb6Bm6qUw1qcQ_616ay3FvpGAKZigaVdmr1V5dMEPbdRtwCFlz_AcSYpD1dGE5MZ-DuPNORjR2YE_bcqdvAGoF96ZITGbXcUrcc814ybijHhnTXmxpzARQcq4elHD4KjdHDr4Y4t6YbkB907syMPpMMn3lx4g8A9fGiLu4uQ4RCOR82sanm6GSuMQI-CdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/113eaa3d5a.mp4?token=IPxthAn9epxc_wXkbgSZMBKA48LXyS9fat0I9j7bFYE0pcc20o1VceKaEpFaNdRsT3xkvnhjx6Yt1khg32cVqMT4hXs7fKbNYonamAK1TNjvISd9HygOJOF39MuOatXOcVxOsYoNhxPdNlnNC_D8Wkn-lb6Bm6qUw1qcQ_616ay3FvpGAKZigaVdmr1V5dMEPbdRtwCFlz_AcSYpD1dGE5MZ-DuPNORjR2YE_bcqdvAGoF96ZITGbXcUrcc814ybijHhnTXmxpzARQcq4elHD4KjdHDr4Y4t6YbkB907syMPpMMn3lx4g8A9fGiLu4uQ4RCOR82sanm6GSuMQI-CdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
قابی بسیار زیبا از سه مرد شریف و عزیز ایران در آستانه دیدار امشب دو تیم آرژانتین
🆚
انگلیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/25794" target="_blank">📅 21:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25793">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/558fc696a6.mp4?token=ISyZOCKv0RWZr0VNa2Dayxus6rEyDz4eVwTW3YzCMyMwLuMckOoXPNEYbC8SAzEwv9hYr1ypWGLOyly28G6s3StH-UuXVNk4e9BXT75WoU4dxjmogYKXp6CbAnr1pRhLASLJZjjYB6Fnzvk03TDplkicn-_SGlnu3U2-F3VJP5o_tHSKQOKZHUPZlk6vPAbAmeNzyseQrjqqZARfxZ0C4T37PNOehVEJ3hqEiGpVYAyebINljnuu4VqQm3rEBz0iDeQwIGk7aF6UnRfa8IQyZNGK7piBj0KD70sPG-qnga68orjheE95sEPt19ldeBeYFoPfRG2zCmRwpV48hfAGmoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/558fc696a6.mp4?token=ISyZOCKv0RWZr0VNa2Dayxus6rEyDz4eVwTW3YzCMyMwLuMckOoXPNEYbC8SAzEwv9hYr1ypWGLOyly28G6s3StH-UuXVNk4e9BXT75WoU4dxjmogYKXp6CbAnr1pRhLASLJZjjYB6Fnzvk03TDplkicn-_SGlnu3U2-F3VJP5o_tHSKQOKZHUPZlk6vPAbAmeNzyseQrjqqZARfxZ0C4T37PNOehVEJ3hqEiGpVYAyebINljnuu4VqQm3rEBz0iDeQwIGk7aF6UnRfa8IQyZNGK7piBj0KD70sPG-qnga68orjheE95sEPt19ldeBeYFoPfRG2zCmRwpV48hfAGmoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
#فکت؛ ‏بیژن مرتضوی تو فینال‌جام‌جهانی حضور داره، اولیسه و امباپه نه؛ تعز من تشا و تذل من تشا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/25793" target="_blank">📅 21:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25792">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MNFO3j7cliQT8lVASY8LkjeLi6isZRsakB_ogDe5NvqD46zhwteD3mzvp7WL8lY_HNmmlHCmDaHWXzyhxlGJUB3fuKcREnl5Woi8o_lQ7siU4_gpfgsMz18ZynDmIciqi--AB2b1Orhb8KpREQm0KC4wGrEbuoKKdj0QXunVQolRNmHyxrQ50ElanFloN3gD-qNZnmpL3tllOlvL9ufZe0heiMNNKL9yAuu_bLzaaoEEQt-KV4BCohn02yJsoXArbKHDoKt69lJxSsClu-MUVrWe8abeE1ajZtokEhQWADWEhbzWLWm9mVlfu_3NIxtXo9QnuvKAR8a4xTRXoCoG9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇫🇷
🇬🇦
#فکت؛ با دبل‌دربازی‌امشب مارسی؛ پیر امریک‌ اوبامیانگ برکورد 400 گل‌زده در دوران حرفه ای خود رسید. امار فوق‌العاده اوبامیانگ در این فصل درمارسی: 18 مسابقه، 10 گل زده و 8 پاس گل.  گرینوود هم که در منچستر سرنخواستنش دعوا بود آمار خیره‌کننده داشته: 15 بازی،…</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/25792" target="_blank">📅 21:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25790">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GX99Y_HuA4cO-xdaIKvjb9H26NnT54BJtfCd5AMwNrPTp1SlEqNlFUDU77UNJNd14hj5wC6-roCA-UZUONlr9lh4UmRuqxHR2vHtUek3EtT4UXefOk7iex-egi-dNU4o3SEu07WSE1UGXzHdw3M6c-Oy_XyKMgNfNAIfKaZ-riuUu9R0B_DeAzS58Gq-lpzjp15doMb2QguBHbqZq70c2FduWKBPP9reWV6wLDsWMTelVpfepYGBtlsg_ledm-HKG1uiOLusVL3SOgS3Ps3NdbiBM7_nVvUvvpH7wdc0Zl7inK5d9P3eZPEMpYCUwexV6pnla1r5Be-LOoVUjBfBhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UciGm-K7cCiVReEYyecFcTGG3G0neNxpOihPJUw8bnfMULB9aN5H5Uf7OYWwNYiRtZtdst0SFhiRqfJO4HZGllzInUhetO23iizYW7xQhZNH-Lvn2_wOjxNlqER4lcgZ3dT5pt2yOG8hzgMhfNcudBFihfRq03lHNSQqpkcgU-_nx1Srb_locf3ZjgQm77VHyeTpAqTAw_ejSMZ-B9k1oLk-r0xxav_G3oslgKybmnJn3O0qFepo4ZgBUdNKs1Hj5sDuzM5HAsrBKVlIe6iCWtwPN2uZaA9h6_nibYlk6YjLc0kqrCmiAVtRrHW74G3AibSWPyBNo_H1t550Irb8lA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نیمه نهایی جام‌ جهانی
؛ شماتیک ترکیب دو تیم ملی انگلیس
🆚
آرژانتین؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/25790" target="_blank">📅 21:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25789">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BB-F3OfstbJwU9bsLg5qqqGRXX5FDUxj8zOci0e2wPtT35yTFv3NWev5jxIGxxfJyYM1A_d8QJUyrowp0ZCKQ4b5Buta7qhzPNWMAmef8bie2KaEjClD47h1-eqfzi4nEIBHe5Vhg2WI0UqSFX7jKbKoTtVxeLBnIDujEIYqGRy64jvqSA5tICw4kFxAgxc5wZeqo_14oI4EAm1ml7AzubcS8zZfXdK-d8dYaBIcKAjs2yJu8Lg0pIJkx21U_r1UWJNrxgS9ACvhNGUQAfnfAqfUvkmeTqfen09uj7n9ispQ2jo9BtEUZNXBX93tv_LXx96UU3MRi-vdWmVnPfs1KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#فکت؛ تیم ملی اسپانیا با رکورد تیم ملی ایتالیا برای‌طولانی‌‌ترین نوارشکست‌ناپذیری در تاریخ فوتبال ملی مردان برابری کرد. 37 بازی بدون شکست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/25789" target="_blank">📅 20:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25788">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kSJVe8IUBdBNdawenDOcRf0Heh9krbxA2Kacs0jtV9VSZ0iOFMgUmKZHXG5I0gnNvAB7WgAcDo0tckKFDE2nUp1-2_t3SfJZ3VY-3QWb3VA8fRt67EaST1ZFsoFc9ii431D6lwk1WjaV75elybDlwnZpSE_Wn1XghQ63i4W5rOWN29sUWTJUn-7xguQCGNd9nAtFVEovCNAJMQJRxp83mXKXJHkH9PUTWPK5yDfScEE4HyTemRQaXtxlAMnXYnDT_z9lw_sy5ZHQBuRe4eQqzXnbRzfLWnQ5slTlBluRy5hpPaq-yOMpb6J061mFozMYPOSCGZ9qIAsGyodJh7HdsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لئو مسی در نیمه‌نهایی‌های جام جهانی:
دو بازی، یک‌گل،یک‌پاس‌گل،یک‌برد، یک تساوی؛ هر بار که‌ مسی به‌نیمه‌نهایی‌جام‌جهانی رسیده موفق‌شده راهی فینال شود؛ این اتفاق تاکنون دو بار براش رخ داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/25788" target="_blank">📅 20:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25787">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b4c95cb5f.mp4?token=gRFpzwIzZM4RxPRl4UdhMG-Y5SnPPgd5zJJguyx7cIFG8duIemGdPoVsxpbutHw7UATqag4He-gOvRDsNt5XyqTabaJUKnc4FHUOO0rtQkHPE_kTTpYJYpTg8a_fEu0TWueujmx4D6AnH7B8nhJv3d1Al4n8s0_g7yKmpFYwB9G5GhPHA9_ZhfXHLeANufZj-T1WAazWjp--vwJWJHG-3X0rXjrt1azhC5QU7R8xOME-R5UG1HRBvUfitumdPIrTgDP9Z9tfKutOK2aIGhdKR2KIDsN4-Gk2AvNy0QsabcP_OQrck-x8MLdjUm1nGZAtYf47ipZOJiNnYapvzTo2xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b4c95cb5f.mp4?token=gRFpzwIzZM4RxPRl4UdhMG-Y5SnPPgd5zJJguyx7cIFG8duIemGdPoVsxpbutHw7UATqag4He-gOvRDsNt5XyqTabaJUKnc4FHUOO0rtQkHPE_kTTpYJYpTg8a_fEu0TWueujmx4D6AnH7B8nhJv3d1Al4n8s0_g7yKmpFYwB9G5GhPHA9_ZhfXHLeANufZj-T1WAazWjp--vwJWJHG-3X0rXjrt1azhC5QU7R8xOME-R5UG1HRBvUfitumdPIrTgDP9Z9tfKutOK2aIGhdKR2KIDsN4-Gk2AvNy0QsabcP_OQrck-x8MLdjUm1nGZAtYf47ipZOJiNnYapvzTo2xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇭🇷
چالش ترند این روز های اینستاگرام این بار با آنا ماریا مارکوویچ ستاره تیم‌ملی‌کرواسی با خواهرش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/25787" target="_blank">📅 20:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25786">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sUNo-ttyVjLvGfVYFn1e0camMucDES_qLgOndyUqAfMCKJgl4aQEM2F68YjT0GAUoBqcqWRAj3ntkwK4lrV4UfUiDVn9wgWn9KR02DSydRXrujdgLmIIepC7Mqqgu4Zrh2AG4QPxSFQlL3OA94Si8feEHXXKYhCWaCni4NI4jktYxTDl2Jdqmn32tMLCmCp6UvRX1NKx0iYaXgzBMMJtX_pgJ6WT5sl6zAGd3zwiXb-mJxcYYYelE-XGd03gEF8RyfDNL2dXos0EkbcoCAA4TyBfB3lq_v8g_-inUymMCwEimyAd5lq_UjCCVZVpARDnxxlwoJ6tj_b2d6gQ-oOX5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
— آرژانتین
🇦🇷
🚨
۵۰۰ دلار جایزه + ۱ گیگ اینترنت یک‌ماهه برای همه پیش‌بینی‌های صحیح
نتیجه بازی را تا قبل از شروع مسابقه ثبت کن.
🏆
مبلغ ۵۰۰ دلار بین برندگان تقسیم می‌شود.
📶
هر برنده یک گیگ اینترنت یک‌ماهه هم دریافت می‌کند.
🎁
جوایز به‌صورت
FreeBet
پرداخت می‌شود.
👇
ثبت پیش‌بینی:
https://t.me/betegram_bot?start=p8_r4EF37DCE</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/25786" target="_blank">📅 20:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25785">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jgzhJJ8U6P0klz_QtszAjNu_IF_p2I4q4UeZBj57u4gHRAGkSpywXgGKDBFmAOVpDVLO2zo5UpTC7SOzQksp4uJTj3WfQueAvStDSnXm_O7PmXcjrxE5mvlLEEhWixO9JLgFl50DNtx8bXRPKRTLPfn_qDTKq445r4uL4SfW1zeteJNVDsL0ErqS3Lc8DI-boxPQL6wkGPKk0dMYSjdw84vh5gbTXgH-xJzCRguaJY-IjeosPRaUn8FGU3h0sd-AnQ6Mop0tZaq7cKzCwDURjjfQyYJw7yy2zODrsN-_fFj0elWzA-Ln1QgU-rboWab-KQ8hEmFc7X5VAfLj4csTsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
علی‌دایی‌ و کریم‌ باقری دوتااز اسطوره‌های بزرگ فوتبال ایران مهمون ویژه‌برنامه امشب عادل هستند. ویدیو کامل برنامه رو در پایان این گفتگو میزاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/25785" target="_blank">📅 20:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25784">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sz1VgjnzTYZlBd9ZVrWgWVShn7_w4gkTlXrpdCO-jYOhlvcGwRXLS9iIwLB2zP11jyihWbPINdATn7SX2PZ3cVRlMm7Cxmi2ABrTRUHmwAwi6yH0uCa2NAXkLgWQ9vVB7GJ_wkFd0SR0sfZox6R2AK4zW5V_WTizSV-5lt6mmyZm4QHCJXv4m30zOaKMPq2v0nFLRK9TRGpTsQT2tnZHBPfqxN4zpPHeg06og7QxGE7q9_hpdQt71yj7LXe-smMnTUNe50z85LhfLQ78IfANTXc3eN7LUpUZcPC6Vm7cHzBrIjvRnaYyExpxu2uU54ZyY5ldPOdDHFl9Czf4_tbBhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سرویس برگ‌ریزون بازیکن جوان تیم ملی والیبال در بازی امروز مقابل تیم ملی اوکراین؛ خودشم فهمید خرابکاری کرده زد زیرخنده؛ اشکال نداره این همشون 17 18 سالشونه جوونن. اونیکه تو 33 سالگی و اوج فوتبالش مفت پنالتی خراب میکنه اون درد داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/25784" target="_blank">📅 20:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25783">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_YEOQW4R6G8zz00w1FNI_ErnKY38hTodgz-Yji5g-ep3eIa6oerSlUSS4MYpa0PydOPrrlRTnrmoK8iqhVHo-P8aCStnf5d4kRXzzIFU_nLu3kryWFBRF97-URaGBcXUSR2bCaa6UgkU_wQ7Kso9m-L4Xp6BOWLKBxaCnt45o-BoMPEp4kyiasChPTJ2-DSaLM6b3GnEM5rSz-pT8k50VCKLhApt-tZIMamgzcMNjMhU8dZyeL7yrAHy7mG4PhEHGXiLweKyvSjD2akyrLSed0fHqYwKyMGy_Ys46uoupEmFwypyxhuxM0sv0xoWL33TnH8mOxBVVstHU3KHAKN8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
واکنش جالب ابوطالب به انتخاب بیژن مرتضوی بعنوان خواننده بین دو نیمه بازی فینال جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/25783" target="_blank">📅 20:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25782">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87ed733fb0.mp4?token=rZ8c5QieMUm0HBt-DK0VwPDh_WhDkuxP_VaQjHD3U0PF7L7GIFnJfkXUTr_bS4zcSWqkQS3K0A8X3BBQJrL9p6jiAAeXn_ua5MJwNu96BKqH4Pdnr6nDnqzfJ6aMV6WpFNMPfIM11Zne61dhlebPfS-45_W_SX52nQAdIU1M9DNNKxnChInLGZWGz83RiIvzg_TjfgqB6PutziWUOl94IU-CSegj-Pha6k-0Imx-IcxIiSW8I8UcMvHBpXhNYWu94Ee8z8K6ymVv9javgtg9Dn12FQRq5lC2NMGjtmqT4j2QGOoI0CsjnVTN7D4uwABTDqLRlQIpCvRwGZ--yMIV_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87ed733fb0.mp4?token=rZ8c5QieMUm0HBt-DK0VwPDh_WhDkuxP_VaQjHD3U0PF7L7GIFnJfkXUTr_bS4zcSWqkQS3K0A8X3BBQJrL9p6jiAAeXn_ua5MJwNu96BKqH4Pdnr6nDnqzfJ6aMV6WpFNMPfIM11Zne61dhlebPfS-45_W_SX52nQAdIU1M9DNNKxnChInLGZWGz83RiIvzg_TjfgqB6PutziWUOl94IU-CSegj-Pha6k-0Imx-IcxIiSW8I8UcMvHBpXhNYWu94Ee8z8K6ymVv9javgtg9Dn12FQRq5lC2NMGjtmqT4j2QGOoI0CsjnVTN7D4uwABTDqLRlQIpCvRwGZ--yMIV_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه بازی‌های تیم‌ملی‌والیبال+جدول رده بندی لیگ ملت‌های والیبال قبل از شروع هفته سوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/25782" target="_blank">📅 19:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25781">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a5e427ee9.mp4?token=nxePHNwwlJQXYsVuU8HWp3klrMFIhQh18b1cZtu8eYAYkEjbfipHhBp--bSz0eA2GjQPw-wdeBDTGfFu5HXJcvj1FjR6PA46m-JehS9dFKq0iArYZvWqxiSZOKYKGOh9d-XJG0k1WrNL2ab7AFglATbOPBRtAvH6YDZhfCY07JPkOlVPxTvmZdSRWoIgoV94UMyZF7jR3LSKypzch9tg5Hh2C5s5lTFGAvwEpCVIbl53aHRTnfvB1ZqD6Ca4RVr5mQG6GgLMdnqWWhw54kxBkX31cnfQ2h1HJ0ki67CpqFKyWKaXolOEoJVifd6t7Jg6AeJKilUba8BwjuwsfwfCnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a5e427ee9.mp4?token=nxePHNwwlJQXYsVuU8HWp3klrMFIhQh18b1cZtu8eYAYkEjbfipHhBp--bSz0eA2GjQPw-wdeBDTGfFu5HXJcvj1FjR6PA46m-JehS9dFKq0iArYZvWqxiSZOKYKGOh9d-XJG0k1WrNL2ab7AFglATbOPBRtAvH6YDZhfCY07JPkOlVPxTvmZdSRWoIgoV94UMyZF7jR3LSKypzch9tg5Hh2C5s5lTFGAvwEpCVIbl53aHRTnfvB1ZqD6Ca4RVr5mQG6GgLMdnqWWhw54kxBkX31cnfQ2h1HJ0ki67CpqFKyWKaXolOEoJVifd6t7Jg6AeJKilUba8BwjuwsfwfCnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویدیوزیبا از حضوراسطوره‌های تاریخ اسپانیا در حاشیه دیدار شب گذشته دوتیم اسپانیا
🆚
فرانسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/25781" target="_blank">📅 19:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25780">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f78ae3e4c.mp4?token=cLlk2bKYJdQs8jbw8q-LHWviHmxe_n-D1m2uO6c2klyGBUk1bpPP9tyyNqMfDlmihFmd4UFYa9GVNxo6ra7Qhckl9SmQYsZvAP9J4lCbajfA5snn8PWYcIAtXh-HjK-y_5KSG9oa4ChzYE49HTT0GLzMXHsrbs9pIcWMUQEhBDoK6aEEi3UZxzxseJTUYs9wnc1LuXor9xZTFU5mWYE-9iSafy4C-ogVX-I2HIb9FVeRb2M3ojynmLPwYehhWzjsEISIrq0qrRJvUgWg5w4Nd-82yP_HowVld1ZgYt_89WM66lLB-nG2vdS5fWmGQjaGSNDyYWPioFN7TU-xHMMQ9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f78ae3e4c.mp4?token=cLlk2bKYJdQs8jbw8q-LHWviHmxe_n-D1m2uO6c2klyGBUk1bpPP9tyyNqMfDlmihFmd4UFYa9GVNxo6ra7Qhckl9SmQYsZvAP9J4lCbajfA5snn8PWYcIAtXh-HjK-y_5KSG9oa4ChzYE49HTT0GLzMXHsrbs9pIcWMUQEhBDoK6aEEi3UZxzxseJTUYs9wnc1LuXor9xZTFU5mWYE-9iSafy4C-ogVX-I2HIb9FVeRb2M3ojynmLPwYehhWzjsEISIrq0qrRJvUgWg5w4Nd-82yP_HowVld1ZgYt_89WM66lLB-nG2vdS5fWmGQjaGSNDyYWPioFN7TU-xHMMQ9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
#نوستالژی
؛ یک زمانی میلان تیم نبود مجموعه از سوپر استارهایی بود که همه جام ها رو میبردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/25780" target="_blank">📅 19:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25778">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RoX4Jh0IkGo6VKuVOI3FHFMtPLR-gjH7MvU5o-Ts9ekHY0uDEH1GBWwP-ctxCxDUu8bJ2_MCSj2xqEe5lCLmgp9zw9dbNLBrYNn661sl-JzPzYgHN9Ufr-NxxB6jVTkaplvVOeLzOd2Q-T7OZnytri1g4zdIa6ptr7HAB1s8t-RayMlA4UlwOMvRoHWsWRkxZ-fqJVb6F0aTLrsRKstwyEZldRz0mINQTCxkdy9l_u__P17752-xazBGJsa94QHZaPXgGHM_sieAtyMbtIrBAFHxQUYtWkt7LGVI3CvP56aYp400HcA1tQCokzZIWe407u4j9MvRoKeq53Dvwyt78g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r-f8BESUnPFVEorN_FGGR_JzEtM9jIrVF75IQ8ewrlxnT5en8zo4Y_Xl0WSWxapDVNy_fNQ_kQdkUgPnk54fjygMCor9Q6ExDlC-sGuuLV84km7-EkVGDBdcokbCk-UES9Xe6oycdO3UHPVxNJ6yWGU53a0vEl3n7_S_3trsaBx7-HOVKmPkCtlB-aXsxrfymH6H2DAn9ODQ2srBl25topB0PHw4PjRNtdnYYWJpwdi3O3GJ-AtrYXSbf4nCBAJ9_U_J6jxC8_Cwgl3g1xljDFmiFAzKdcbwYcWXF9XDMAuiSy_Lj0wlDrJ9YdwOl-HLqpRz4IKy3OYLfLDagQ3c-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
👤
مدل موهای جدید مهدی قایدی ستاره ملی پوش النصر امارات؛ اماراتی‌ها رقم فروش ستاره ایرانی‌اش را 3 میلیون‌دلار اعلام کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/25778" target="_blank">📅 19:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25777">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cS5-wcs8Lib8dOEBIp4ggO4swlfMcWtMqQe8-pZA0xtTxFb-6-T7ykJQFoulY-_i9s9ARXy3xY728aNqfCAFDzOps8NQrs-3UvALDq9zaXCLL7K2hg6WdXZv_KSmPapDhWLJv7acXHEtYjsr73RNFEMyN7U1GsDe93MDzP7xdOYq5JmmV_Ph77Oit_a1gJ3xWJ4P1T4cb8GdHcqbNwvKIv7RoBIt4bRAD9LPl0dLQXyg2-DLUCCq42wajmILawZypvWvwJ4dEicIQwkPmA4ChhpnTKcC5g9fypDr7u-mJYKp6EwqLQFZdxKRUruJ4jCm62shr43jr8Vd54bTxCznSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها دیدار مهم امروز؛ جدال تماشایی انگلیسی‌ها برابر یاران لئو مسی درنیمه‌نهایی جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/25777" target="_blank">📅 19:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25776">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tsRkYQjdCm0RQsQjDb5vBBAYixARnoeQSfThGdseyDddwwWoyRPsd6bumQpRXb0aU4ZR-ldTClOI3qI8Ba68Ni_xU5oSayEpHfFhS2h6IvHYRvOllOL0sXJYC6fedhR8-OfFXhfzgwoFZ1PRiej65G8kkxJLIuqXYL6cfYT9VeaiA6PDKqPaz3A_CRlatA6DT_TqQ7i3JAfYP1iaK2f7mdoUNiEcG2xj6Fk7SVQLppXI1nM1960OD13S5OAAwZE4LlTPDMNQ_-EYR0ZdfZ2uScJ2mNmk-UjPzlttXzWmcZ5tl5wjcsmh6wBBRYP576nfqFqCH-kjud-3gEUe8N4G9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ سانتی‌آئونا: باشگاه رئال مادرید اماده است هزینه بسیار هنگفتی برای جذب مایکل اولیسه بکنه. بایرنی‌ها به‌احتمال‌فراوان با 220 میلیون یورو موافقت خود را با فروس اولیسه خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/25776" target="_blank">📅 18:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25775">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/isACpuYeNbFIh0kK1qIA9gvDWehlCkP-WZjE0XgRZEzDyDW4s_WtVjHgoAm9hq-a_5v347hIbnKSIjbkLsJhgCp20UTORSpWfMQU9b-N_rUeuKgTxvZY74SOrMStg2Z48OGlAO_pMH5taMLguN-Qb4ZaKqvPwarSoYaFTwxjvWY2I8v_xmK2IbJOJqrqBYfE2jxYU1KzPnJmCM44I5blTnjjIdAU507WTLdyGBxo-LxTvwl0ydcZQ2vNQmTyhxkw5WkABHf2HKgVlx480EzG74IaibfEXJgdSCK_2D8lBVAvLQx-ovO2kJYoKY4Blxok97kc6yvUOHd6vDjem7oo4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
👤
طبق‌‌اخبار دریافتی‌‌پرشیانا؛ احسان حاج‌ صفی قراردادش‌روبه‌مدت 1+1 فصل دیگر با سپاهان تمدید کرد و تا 38 سالگی در این تیم خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/25775" target="_blank">📅 18:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25774">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/urlZd5TZMgYSGIGTUmd_VCqwha8rxEf58HMVc0PXcMp0DlRLQMTCk2hB2E-sAoFVt9WdAn1-Io07Q-qyiQ23hW_gOWeCHWljft-Dn4ArVvt2rxYRqnLATHbZFYRjvFEh7LjmyiMwKO6_w2ZRT9k-yj7zOvOczoxsQ_15wgSKfIcjptI-bdZgYr0ZbfL4qWvaAHf8zDiLllmGqCsSR7tnmnp_xZyv6aLwxpNycEAh4LMxLxpaHFb8KLQGc4Pm-GmqofWG5_XMNAKWoF1RwVfaZnauwg7OkiCOa3WIrU60abYCjY59rF5RC4RyVnCs-cXDpXYTaXPAIDnGKt27r9wzGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
#فوری؛ سانتی آئونا: مایکل اولیسه می‌خواد درهمین تابستان به رئال مادرید بره و این موضوع رو نماینده او به مدیران‌باشگاه بایرن مونیخ اطلاع داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/25774" target="_blank">📅 18:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25773">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lvIlWO5eB03H3KzkqBZCS5fEaZLaJPcSYSguABjoz_gMPPsWSpmgbA0T-U0oHFPzOR2RRRBfm6r6C5vplxHIyWUhMa5xCSO4g5rlNYluEix84oefenBk0rhxXkQjWWQzWFUtcv_RT6AoBf5ipDF1Ex-4taWrRMqaiBMV1yx7AWSDrgTf0YazFOdb0Z8uA-qunfK2twYqPJYbBtZnzotfSUDRz90gbR0__4hDgXIlJHXX_21VpOzTjtNwd3g9KHQ49JvKTfdwX9cV6Xre6H0Jb6Dmr4sdCQ3SbHl8p0AIsYQfPYxmRWuy5C-zcCTlCYp_nYx-Rk_qssg5v0cKTXDqmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
بازی فوووق جذاااااب
انگلیس
و
آرژانتین
رو با آپشن های تخصصی در
MelBe
t پیشبینی کنید!
💵
امکان شارژ
کارت بکارت
و
هات ووچر
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
🌐
دانلود مستقیم اپلیکیشن اندروید
🤝
اسپانسر رسمی جام جهانی
🇮🇷
پشتیبانی از زبان فارسی
✍️
حرفه‌ای، مطمئن و درکلاس‌جهانی پیشبینی کنید!
برای ورود بسایت‌فیلترشکن خود را خاموش کنید!
‌
🌐
Link
🔜
MelBet1.net
🌐
‌
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/25773" target="_blank">📅 18:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25772">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KvZsLVeSkpxrnPe4168BmNhxlIFksHreVTxvTWdRTWXOI_nEehNYZu07GDKGlTQIYOeY01NRMLCE70A3Kd6LWN8qeG8x91-OHkViM9k31VL7b_jxnvlebGbnq52v_AZNxfmOQvNzZUv0qNygbpRcB6gdfED-2P2E0P-miUtTeaygUMlLNSU7w_3oP1Ga7rZTiODJDWpHXBjTM-FytBjL2EbCQ8z-5DFui1W0iIA1XvtcMCRNrSc-vArZiwdYHJTUihrKCdoafq6uSZvlrIXYyUok94XcimmZsdngzVzdRDzUgHSUlVMy5KrupVu3BJwprJttF4pVgS1Vxx1jOpgHKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
فابریس هاوکینز: مایکل اولیسه پس از جام جهانی دربارهٔ آینده‌اش بابایرن‌مونیخ گفت‌وگو خواهد کرد. اگر آفری‌بالای ۲۰۰ میلیون یورو برای اولیسه ارائه شود ردکردن آن برای بایرنی‌ها سخت خواهد بود. پرز رویای حضور اولیسه در رئال مادرید را در سر دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/25772" target="_blank">📅 18:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25771">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ayabq7mACFTNWoXuw-ia_Rv7QgIA_bbOBf3iRRy3n65EvnDC2OPdt46LBpqwu_gLjjVbdW9jv9qHN9gvuQ3HBb_Xh2gXKtEm1vVfJ4OkqwUYLUCx5re3b2wdabV696-nKyPSg4wYvtpOj8S8d5HlieJbPkbT6F84PSLYo4agX-IDyfafSgHw8SYhqAExe0GlZXCkaQSMwuG47iFL4qRbZbpNOT0UfXto5t-8n_WXNgRLn69tuaSKVnSk-c9ph55HniKggQtzSL976IiWU7GsAzNbzJgEhsjzF2RhdhKzkawOMAZLc_QryJEKfdZ9_r8BOW-5PtwhbbUiWSPfmWDDHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درحالی استقلال پنجره‌اش بسته و دوفوق ستاره فصل قبل‌خود یعنی یاسرآسانی و منیر الحدادی رو از دست داد که فصل آینده نماینده ایران در لیگ نخبگان آسیا خواهد بود. کار بختیاری زاده سخت بود سخت تر هم شد. ممکنه حتی بختیاری زاده استعفا بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/25771" target="_blank">📅 18:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25770">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qM9YqYLXkaElqMTmpsqVh_cka2oGjO9Snwew6Pl8y5HVpyfYcR7L82J01YryHVKQvBmffjYacXgXpA_VJXb3UZH8Nn6O9Zc5V3rUQ4_SVRN-Uxzn6uSnIrd1dcy76cJQOhNL3jlFrP7FYlgDiQDNK7cjpkFUEBUOE52TDloNNKSkjV2_B01P343ffOFsLdNLN4rZzKnXm_xkiCcWmAAw9R5KwiQDE7kqiFhuFCirbKoToZBzEXirX02d6Yu6US9UrrKxMtvLCZXkn8GmKMfMUemEFlf_u3usdzHD_4PsLE1-ThqMch53zvDxGPSgbYFEBnhFFxgHHNJxzwqipa4TKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیشب‌بعداز بازی فرانسه و اسپانیا درنیمه نهایی جام جهانی؛ خونه یامال تو بارسلون مورد حمله قرار گرفته. دزدهاداشتن‌از دیوار بالا میرفتن که نیروهای امنیتی بارسلون متوجه‌شدن‌وجلو دزدی‌رو گرفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25770" target="_blank">📅 17:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25769">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UtVxvLonZIV1GrpWAetpdY59LI8F_hV7Zg3NQl_ALolPTggS2R-S_kQSOmJFi_6VuN2Gi2Z_jmx6zM4hWyksR3BFfF72L7qitRl1y5lysj-fFXL77autWfiavHlqk2oLTs4Vk2byeK_P_CYiQucVnYRwoY29WI0lWXFMyYucO8YHt14MAYmU2MiQfyxjp3kVvZmPqTm8jHqQAp7RsHnnMZSi9jWtlfYt8uKdgPmL71y3WSmxe-9aiizWB7KXB3WGHnnKGDCM3p8TCXQJoILmf3vCxlIxnksHiPRKRv-UGYYH2XQa7d2aIfHGT3E8XexZPmmYXCFfPc77MV36B2F28Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ بعد از باشگاه‌‌تراکتورتبریز؛مدیریت‌باشگاه‌ پرسپولیس نیز با ایجنت ایرانی یاسر آسانی ستاره سابق تیم استقلال تماس گرفته و از او خواسته که یاسر آسانی رو برای پیوستن به پرسپولیس راضی کند. حدادی به ایجنت آسانی اعلام کرده حاضره اون رقمی…</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/25769" target="_blank">📅 17:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25768">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NEK6Zkbd32dcADu4f2S3R0POHpIcgTu2aHiv0O02Sc9jFtFfG8kSRKNMy7OxxHeRBQJ4uT3-qmf_I9eVZ6oreESiWJB5ahmYeE-uoQ4QY04QbWwxPM2vVuFYVk1cDsSuydvUA2U485XFWqanXGdvER83G4cq8jzTOvzN4XB_JX-EbRyhlQs-5Dfyn9M3RrbH1vMiS4wgnqkj29Bb1QA3Cp7hWLLpgTEvPNsFrjrOQsGGvSs2X9gmQ6BZiV2_IM9ECkGwdCcjI9khGm1bp7q8-vRRVdWZ11v3B1KWYfuEbTgociaUXKbP-4-H2rrLYhIQiE3njl7f5rIdLph59QpfZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های بلژیکی مدعی شدند که جرمی دوکو ستاره تیم ملی این کشور دیدار فرداشب مقابل تیم ایران در هفته دوم جام جهانی رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/persiana_Soccer/25768" target="_blank">📅 16:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25767">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dq_Ta0GdY-X7eXcci6-kFo7h88w_eAXREQnjODnp9P-3POIcCHQj1yd3qRme5y9oOy9h48GgQb3MSnrtkBf6LMHRuO5vjuuyBjs9yS9-lYMUCXLRQOzGtg-nvRI7jiH3PbeO2_EB5kheppA1dLc_fHmQxTbvI9LVQtlOdy47Li_UwGVywn_Avwj4anyHeUS2Cy23FjGWEmrjWuAAz0mKKIsgH-c3VbfSws80RbZ2VqbrFgaN5djvnk_HrC_ACYiWYr_pXK-1Eq5sdxE6dS7PCFEXTgrC2yfrQUUCNnlmpyyfTNzCiCfIhU0YUYC5SrxudccgCUz4zeCHBvbaw_xyqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌ های قطری:
باشگاه الغرافه قطر به دنبال جذب منیز الحدادی ستاره سابق بارسلونا و استقلاله و مذاکرات رو با نماینده او آغاز کرده است. علاوه بر الغرافه یک باشگاه مراکشی دیگر دنبال جذب منیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/25767" target="_blank">📅 16:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25765">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb986dc0f7.mp4?token=U87LHwnNizeuU5hNCWaP9GyTi5Qme0xVb3mmeDMVei2YtGSfRY1HUaMbFwtSOcveBJEzqHBPBCcMg8RL_hGcE37tYAiTy2uDCUeNXBmqHCLEcfKZ-IKsL9L6xl9m3CGO7E7llDMJMLhR5p5RupsaLMa6-DnJsuwcLxma3y295B-FHBNIEP9a5TbtTZNR4MT2v1I5ecao-mxdzdr1JQCk67MZXc6MM9DwzUrwSlkGek6_Y3lShQFpqO8vaxOckCRqmiSvO9llRKyH76M-ssmFVBK6Ujg-vynwYUCmOAqTFaIdcGERddUKEJIV_KqBkGMnpXhNqSIXUxG3sxhAbvEFAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb986dc0f7.mp4?token=U87LHwnNizeuU5hNCWaP9GyTi5Qme0xVb3mmeDMVei2YtGSfRY1HUaMbFwtSOcveBJEzqHBPBCcMg8RL_hGcE37tYAiTy2uDCUeNXBmqHCLEcfKZ-IKsL9L6xl9m3CGO7E7llDMJMLhR5p5RupsaLMa6-DnJsuwcLxma3y295B-FHBNIEP9a5TbtTZNR4MT2v1I5ecao-mxdzdr1JQCk67MZXc6MM9DwzUrwSlkGek6_Y3lShQFpqO8vaxOckCRqmiSvO9llRKyH76M-ssmFVBK6Ujg-vynwYUCmOAqTFaIdcGERddUKEJIV_KqBkGMnpXhNqSIXUxG3sxhAbvEFAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخرین‌آرزویی‌که مادر عمو پورنگ داشت. فقط اونجا که میگه بالاخره‌آوردمت. عمو شما بلیت بهشت رو با همین نوکری کردن مادرت گرفتی خدا بهت صبر بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/25765" target="_blank">📅 16:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25764">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K51F02mwc8Z_xeej-_UgelMRlRZqDQSDGjsNE_lrYoLEW_wa1asZ_INk_HgGtUE7ucN78hvWyTpgugfZrOOkNF4artP338Eaveiu-fqbTkp9YR81T8a6njjN1RjrjEQkQcVDxJE1-Rvz-bh0Lc0uAzhudD7UPKOuJTJf9h07RRGy88vwBsKFWiB-YXOd5NSRh_vGJ2Bsu_F9Ik-X_7K9PYsht8KSVSDkmCgYqmympGV6SsSfJsuk9HCe8JArU2soAXAiIobPvA_o-u2e6QipiiT4KhFc2cU4xKdnqKVG-UbQFARB2jcA5tNK-ChXZirw9E7yFzf-K7iruq1NuRYIOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
بااعلام باشگاه فجر سپاسی؛ فیروز قربانی سرمربی جوان‌ونسبتاموفق‌ شیرازی‌ها از این باشگاه جدا شد. بر سر مسائل مالی به توافق نرسیده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/25764" target="_blank">📅 16:08 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25763">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o2oDBZNv1u87a75hTpkYRxbKGkllMAgNPNmusctW4syyysF4jvIdgjshlr1XLTJx1Sm_3x9hYrLpu_IRIxN1NPqLJZGu5kR671VfEpP8LFLFM2zixWqscPWfbjWCcea5B5XkDWw37Ds35mkTighA2wSwlL-JK4BlgWaTVWd9do1oI-wyj89bRVf9gUCSVFOu7FoU8m95ry4rIVi-hWjfJNAjD_SlrGgmJGb9PKy4T4F1bhKOoiUs7beHp5MiMaozN_g-VHA6QcIH9dWsgowwgkaTVeTsNZs_V1U4XyHPZOae8KJzC4fG5xhulpnXYEuxI8N0bCgkISAFnkyLeMrgbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی #اختصاصی‌پرشیانا؛باشگاه تراکتور از شب گذشته با مدیربرنامه یاسر آسانی تماس گرفته و آفر دوساله‌خود را به ستاره 31 ساله سابق استقلال داده است اما برخلاف‌رسانه‌ها توافقی صورت نگرفته است و تراکتوری‌ها منتظر پاسخ نهایی آسانی هستند. ولی پیشنهاد مالی خیلی…</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/persiana_Soccer/25763" target="_blank">📅 15:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25762">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgLiFfxNPsvDFwqpU1em7GKwgWKmcVkFDcPTZh0itGsOTs11UQfTnCqxgcQPgMigCQ6Lx7EPYnqyX9Pir4aBh6tbELDimjYJucxspOe6WnVCL_PJhsdGSnElfEmblCyNfF9UodTOR49Hz87Q6J0Ai2fZZcNQ62MEXoHjeDKZPTDthIl04k33o_0I_xgbXN_1vJaoJ3pGG2cvcqFFBvXTV9ui3AfECeHvZLskowDE3J-3MlRWJE2AKTinCLgy8y08Xzdi4lrSNMF4OatZfdZEqvBV0GwgAqG1-1JFZrYDy2zc20cmw-m6aEsRuTqty9u8dJMHhcvfoQTemb8anB2-aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی #اختصاصی‌پرشیانا؛باشگاه تراکتور از شب گذشته با مدیربرنامه یاسر آسانی تماس گرفته و آفر دوساله‌خود را به ستاره 31 ساله سابق استقلال داده است اما برخلاف‌رسانه‌ها توافقی صورت نگرفته است و تراکتوری‌ها منتظر پاسخ نهایی آسانی هستند. ولی پیشنهاد مالی خیلی…</div>
<div class="tg-footer">👁️ 79.5K · <a href="https://t.me/persiana_Soccer/25762" target="_blank">📅 15:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25761">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33fde3599e.mp4?token=qC6M1S5EXV98JNhuK878Rx9t1OBkY0kp4Tovfm4fCkDkNs4bB4LHYa0rPzmaP26anEyFt-fMYcIvJsCmSNKZCMUAvbTMWj4ELeS6OnTQdp02SB-och_5XVYK2-6ZkEHPiDyJy8LBD8z-cj-fPb7ZiSaGKFCvarTmLNHyr1ZW89jgCJlpnQMhgtOL8d1oDGZLT_e-_VT59Ded2Yxbc49FofPzEc_XCtPtM93CJkDWTRWA-0-wS0-dNknRspjs19JDp8j8JyQcW2clBwzVjiu5gkOIyrsPZMLrHJp58BQsJ4sbyaByabXiT4YQ2c1iNSVqgHtPNFwRfS86Y0UlmkzxLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33fde3599e.mp4?token=qC6M1S5EXV98JNhuK878Rx9t1OBkY0kp4Tovfm4fCkDkNs4bB4LHYa0rPzmaP26anEyFt-fMYcIvJsCmSNKZCMUAvbTMWj4ELeS6OnTQdp02SB-och_5XVYK2-6ZkEHPiDyJy8LBD8z-cj-fPb7ZiSaGKFCvarTmLNHyr1ZW89jgCJlpnQMhgtOL8d1oDGZLT_e-_VT59Ded2Yxbc49FofPzEc_XCtPtM93CJkDWTRWA-0-wS0-dNknRspjs19JDp8j8JyQcW2clBwzVjiu5gkOIyrsPZMLrHJp58BQsJ4sbyaByabXiT4YQ2c1iNSVqgHtPNFwRfS86Y0UlmkzxLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
حماسه‌ای دیگر از جواد خیابانی در ویژه برنامه دیشب جام‌جهانی؛ از خداداد سوال میپرسه نمیزاره حرفش تموم بشه دوباره یه سوال دیگه میپرسه:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/persiana_Soccer/25761" target="_blank">📅 15:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25760">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GMmek5x1ahWyLjnmHYz6zYDGlz_h1eCw8Sh59NWBqeXqXxf1O1ouYY8IkroLHHqMNbraJ4aDhaBNSQ2ObscDiGdtTsW7xP4i9I4Ge7Qrcp0SwM1J0SrMg_rMhSg3aXcfcVKDRfpLmIO7C4lz1UVm2XgH5vgHMCZJEJHk-yViZdm4Mml2Y3gAKyhhzZUZnKFWiXCWtWTDkfraLXjFhW0g_RzYm77CZmS8kvr-izY37EQceSrqz3Mes8V3Lz-a7HhhrSAGlPyS0HRdJRS8Y4PI0VsmFsZZH1Qpk-huKhFj0f-NzSd8GP_UGQIlsLPhSP8YWStaS1Aue8f2a5JO7-xyNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🤩
#نقل‌انتقالات
|اسپورت:
سران اتلتیکو بدنبال جذب رونالد آرائوخو مدافع 27 ساله بارسلونا هستند. مذاکرات باشگاه با نماینده آرائوخو آغاز شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/25760" target="_blank">📅 15:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25759">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bSISFbQpxyYkarBuhJ9k_gK0Y9xA-trOgdhAQMROS3x5_lzxiAWPPHuzGgbv_aAvookmmDUvlWhchdpIzTl8OKPaLi-zNf670EhjfqNwuNUWJr-A9HWogu76Zfm2G98UzWj7X7D3_2tLhNPW7TTkYgAS_WFInsXUmFF1qL6J5e7i8sH5cb97FcQrzmTa1Q4YIxn_6AyRMevaePR7Fs9AD_HS-IBKy0G4fKjc5BhiFYve7Fwt_rhIj6sI56uzENEDHNzC0uJPuPVNyJ3l8UEMcK7Uejo8Fk-0pLGSlGnu9w0QtfwyqqCHtMu6370Dv6fTT6G9Xcgg9BijF32d0u0KPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25759" target="_blank">📅 15:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25757">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LfRuLGO0JeZnLBQxkHU2DBhHn7U4HM5CjctDenbT-HQJ_4t3NaUle7OHYoYY14QEGsHPg8lKKTzbje9g9RtaK1TnhJLIyWwnn4WktU3uVLo49hUoy_8Bf5eKv873uqPQQ3Xdu8sHLhJvDIJY_xT3aOR9wUMyH5MxrKu6qZCRUQvjdSbIxvMDi5HQfRCbmdp7ytQCiKvhwciap1qXhPeCrlDtiZfq4fR3uUeuQg36cPz7zo3gjIxZRo7lTvsa8wMBpYuA_9WGPYqMZwiLI24kN9wqKqt9v5iMZoO7UzFaEDIx-dAb0FFVtRrKV17j9oHJVKSgEzSUT0PSj_XQmqUn1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق‌ پیگیری‌ های‌ ما از ایجنت ستاره‌ سابق استقلال؛ قرارداد فصل‌ آینده یاسر آسانی 1.2 میلیون‌‌دلاربوده که فوق‌ستاره آبی‌پوشان برای تمدید قراردادش1.5میلیون‌دلار درخواست‌کرده که مدیران استقلال با این درخواست مخالفت کردند و به مدیر برنامه‌ های او اعلام…</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25757" target="_blank">📅 15:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25756">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYCCDeCYFyYFSdXBIuZJJq6iNjHNI6c_SPU0uBITIVIJmAv4wyngsrHsP_bJcJAlwI5DomkqYORiOc2W6SawKeCJvvOdcoqO_wTsR--bKfYOiSJf1_pEgggzBqeR_SnpGUu9KeI9RiG21bXt2ljw3dPDJ6I1t9O78c3N6ZxrmuPxydUxQfUXd1X2v3y7KCF-X2U7TWvtq9PPfAL0sixy4FMfIRQRwW1p4MlI2z90AytTXhWHQykdvTPwP12EWqrq0vZW_sWn4ZpSlMlfG20OogO5MJMMt9lX_m8tfn6e5n3AvJnyOXE8Q_WsU_alXTbi-7jtS2HOXIrD2vzFOs-xvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نیمکت‌های جام‌جهانی 2026
؛ چه کسی ماند و چه کسی‌رفت؟ از 48تیم‌حاضر درجام جهانی 2026 برخی سرمربیان همچنان هدایت تیم‌های خود را بر عهده دارند و برخی هم از سمت خود کنار رفته اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25756" target="_blank">📅 14:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25755">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MDgWOu9zghhhpTUrc3cW21DfKFTakoILvaiqNrfE29RDaW6ZXw5Bpn5XRpJoorJ_GJDToitoaAl4aUbo7D6yxIldvkL_ZUmK4w7yRjz8kMCciPINv6jZlqRzm02lRSerf80ffPwhAIyrj6gxkZh1P5KI5SWY0zHLZmtlB34Pm9qPldGZTutG09F15iRYkKsBF66AEpPRpiAaXofPwyeHTYUDWqsjhyQM0kf9TrWXMEviTy_zUwpk0BL5nYm6UsqpfcP_PJ_I6UiLRvjSAIS9ptjKrLxfJkmyFzvbJeBMP74X-u1G4ASQwGjnd30ZjZvnoX39kedliMo1KQCRDMPBZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
همانطور که دیشبم گفتیم؛ سهراب بختیاری زاده قصد داره درصورتیکه تا یک‌هفته اینده وضعیت استقلال سر و سامان نکند از هدایت این تیم استعفا بدهد و این موضوع رو به علی تاجرنیا اعلام کرده. سهراب بختیاری زاده به تاجرنیا گفته با این وضعیت اسفناک آبی‌ها از آسیا استعفا…</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25755" target="_blank">📅 14:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25754">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ue24IirjiGrilob_oLJa_ewRTtz46HQjeiTitbRn39rBw5IDA9aGPBjo8csxXFxYgpJsLeShlfPpO0nb_Zjsz-qE6UHc4RLQCRCh1SnmGXWacVPW8f78CQgy-vDsdYhY9J-DegRKQkGOx9BrKdvuP5UGzyx6fAW2AAd5n5PdtwD6X7iX5zKE49aOJT3dzzRvMuIdMBaZzR10MKetN0QR01QLZDH4iA8geyjuZ5un9iibXBkYg8Y73JkrvJ9BYKW72qpy9O8oARhluTTH27liqcu0qSl0EzFCXqKuqfzWCVuQYjGlcWjWJmC57g6ZUFVyJ7Yr0H8J-P52aZeaQmODWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
خبرنگارمطرح‌باشگاه شاختار دونتسک پیش بینی کرده آرژانتین میره فینال و اسپانیا قهرمان میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/25754" target="_blank">📅 13:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25753">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gDRVb38_GuzPkWB66IV6LXlYYnQgidyNn8sBEeahIcGrysxYjGdTPl3b0L6sPEgRQ4mMln6htQjX68zNRVsUGqYDr7eWsxc4kP9vPmuih7fiovCOKzZjdFmMWQWY2UgFinVQrUMyy54Yd_FEWI95oCYctcI8UAxpkmmZZsYLNofL6YMTQIo9MoOxJdWxkQWuNv15A9LNWWX5NKPYek0f6Q8HYS7GONb-tIecKM8LqbxVkDIJb1u9iCyy-axRMWJtcZvij7W3DFkpGDrQR4yvcz_SmnjcY3X8gZtwQWjOZCoc_6TGisq9XwnZrGUs_2rAvhWejRYFU0eiZNKX0HaD5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ممکنه حتی بختیاری زاده استعفا بدهد.</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/25753" target="_blank">📅 13:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25751">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4Ff4dOA6VYVeqHGuOKN5XJEoIL_Oe00FotMTU5_FwP1gZDNXCF2b-1-zNBZBhjFkKDfaYB-9LsbsXDtUC7AxfOh9ahxZh7czuYn2NdwlulcnEITfUeduntk8pWvHcMUne5fcoYvVpOGwJEdv_b6-8HA2akiCEUd0sllrsc1ivkYAbgXZG8Q4NpXlNWm455m9IV7wgsgyUmb2ZRZwgti2A950cNSK6tp4zgmaWZrOG5IZYc3pzS3Th8u1JHeTjKaHKKjLVHuzUS-6NKdsgfD2hxD5EW0ML84J6c01NyovDOY54P9kAQlSjSPuuRTADY8Phh2zCuW7LhsEjTI4CfOBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
کمیته استیناف حکم خود را درباره پرونده باشگاه پرسپولیس و علیرضا بیرانوند اعلام کرده که باشگاه‌پرسپولیس موظف‌شد که مبلغ یک میلیارد و دویست میلیون به گلر سابق خود پرداخت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/25751" target="_blank">📅 13:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25750">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FXuZo3VASZ8QOqHppAP6R3RlVRAwWMa2l_3KtueV7v4ooy6dp1baN2Lb7mcY85IUzjyJCgHwGRKj6QSwHpM8dEjOpybIgStbtzEAyN4BWsVqRy7WrZMduFd66IqXziszzx0S6sQeBhti4rwyLH_QPlnWHjb7xPGQRFxNe3xN-1h-wBHQXACkVrFngFe1mUkOA8EICstxcR7Gy0fjKSet7GOdum9iN9q3P00Z4-ifmWWHmBfig1gL1uREqGG5mMKPJjwGc2fnVAT3_C07MS1w2UlH6HJRGR-TDbSToxfpq80rtJ_vMVpKb_A7Mlb2dVcU0xuBA7YRnU_RXotc58WtzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فکت؛ امسال سال‌ خوبی برای دیکتاتورا نبود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/25750" target="_blank">📅 12:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25749">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dba39423e.mp4?token=MB2fJ5aQ1EWedJBCYIldYjMCUeF5rSH6Gsl6h7cQ6kmqYblMPuL02WMI6xkYc-sYkQmKMZ7bttir17ng4gOeKi4LntBLxqfXxHPW24-fN8n6_SlgTUJ930cxKOIPHG0S5SqFDpsMt_epXZvvmU-n0_Z_YmMX4E39_SCP3M2AUq5O87yXQ_brVx6U30gR8k9HSNsnaM9CEdlWrACnr5G5TpsJ-3ei5Q-hPQTb0yu4-HY4jL28rDw-NvLHMOpZ3QQ3qnAgGKdoV8hMUtsoPGfMaBjt431fYhah2UodMpuF6XoHyChGdo26VgcTtJvPB9irLWU7vnsxj-8rdpuGQdkYrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dba39423e.mp4?token=MB2fJ5aQ1EWedJBCYIldYjMCUeF5rSH6Gsl6h7cQ6kmqYblMPuL02WMI6xkYc-sYkQmKMZ7bttir17ng4gOeKi4LntBLxqfXxHPW24-fN8n6_SlgTUJ930cxKOIPHG0S5SqFDpsMt_epXZvvmU-n0_Z_YmMX4E39_SCP3M2AUq5O87yXQ_brVx6U30gR8k9HSNsnaM9CEdlWrACnr5G5TpsJ-3ei5Q-hPQTb0yu4-HY4jL28rDw-NvLHMOpZ3QQ3qnAgGKdoV8hMUtsoPGfMaBjt431fYhah2UodMpuF6XoHyChGdo26VgcTtJvPB9irLWU7vnsxj-8rdpuGQdkYrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابواطالب حسینی در برنامه دیشب خود خواننده آهنگ‌معروف "جناب‌سروان ولم‌کن" دعوت کرده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25749" target="_blank">📅 12:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25748">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tnGWl1b3VVBhZ_GGPJlq0Ay-xFxTYGJ9xexG9QQ5RFNkBEMrp2EVHDy74EiBe2gVqu3LHYw_x_U2uiW-0iEW1yLpB89Uo4kN7bkVLPxRdM8WbefENwYHUWLnrPRqAy-p3SuUHuVEZBdEAe4VtF8K7gjRYvHGiWwfyYgOnvbYLY77M_g6PFEhbdNwqJH2oh4P7d53UOEcPiHXwcxDdyWf6HNpTdhvBM1bh3JXCd5DgwOUhWiUfq6wjul7d6rbOmoMcVVFrQlRs8RN908tFA8PDd2YGooUTIuK25EECNCr4ZhoG5oNecc0DqdiW8GFIFMiTy7_tsgQVva70KDIAjMvMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیران استقلال: آسانی برای ماندن مبلغ جدیدی میخواست که مابااین‌موضوع مخالفت کردیم و رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/25748" target="_blank">📅 12:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25747">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SOsw6xXrueYozR5rfxmjWobeRRt87SwxSc2GO4GL8zuaZDbeAc1Vk6JXbLcLXcpOGU1IfXyL2dqt2EaLv1kVKhu-7Hej_OrO2EyL8Nrt69gXK4tvRiQpASEUrFbdImM1n1_B_jsOgC2tPyEzihNrteluDQyxhl1WZpvog5F45NxvswLQacP3KkBPZcC77K5Wc-ngQZb060eL3nf234oiZ62Yi-WgIfgfj6g8f3lZmxdnj-wTGmvw4CMhp6gflveSI283dFknVB5BnBTgNSkSsDCUePyBMzlvcL0knywxQBVOFT9TRoxmrnENgmI3GIUMTsERTzQ190onMqnlqLGI1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آندرس‌اینیستا اسطوره‌بارسلونا درگفتگو با عادل فردوسی‌پور: لیونل مسی بهترین‌بازیکن تاریخه. از او همیشه انتظارات بالاس. لیونل مسی فراتر از کلماته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/25747" target="_blank">📅 11:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25746">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-vLMcJdg6CjO9OPYqobqK1vIDXtSId4je0EEMiZO0GVoN-P-jumfWgqCTvIEPpIwJahW4vik6-s-lZjwulvdezuSM_1iBwnx129x7vNnx6gOT1DgJU80liHKDmBu-JBRAW1NksbxjMJYwS7KgjG1UPJCUJe45hN8kgvDgI1__s2om_xYqJCo5aJE3la5xFPseH1Rpdp3kgsah6hRD-X6Dbgxjti4Xx1gNS5dVjQ_4UKSaIvbqOV3bF85eC8QAoGYfea3hzK-E67vBe94DEzcQL2stk4hUAynPZZ_t2eyNHPOoKVsO_QJn1BkcFQodXXf2XOreSHqE1ZlyjI4tPf2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هایلایتی از دیدار جذاب و تماشایی شب گذشته دوتیم فرانسه
🆚
اسپانیا در رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/25746" target="_blank">📅 11:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25745">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bTDExJvMnZNUDiWXauWX4val2Wov1k4zS9BQ6gPOfPMC4CISaEP91gnMzKJupjtG-iMuTMs8MKFrIuSh5DS0Ixj3Zky7oQqJYU8VMmAglGG9RjqO52hEr4BwEArs04N26LFZIAZO2pehTEff5nv3aeMAZoS5WpV338o-VZbVoeu-GGGihvjQ4sZaJiIl6mNpNErWi92cjySBHbvWczzBp3eXYNQCFayHQYZeC54Ly7bKNwzrNbyLATqX3wnL8hrhGrRYJ4pTugH_SvKC4ILKkCFor_Vg8FOR-N06rVjfoRqb6wScTCr2GZLdiexnEJoqM2EaQL4dtXy3UESKKAUGsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛دیشب‌مدیربرنامه‌های آسانی به ما گفت که‌باشگاه استقلال ریالی به آسانی نداده و به او گفته که‌میتونه بره قراردادش روفسخ کنه ولی اگه بعنوان اولین‌رسانه این‌خبر رومیزدیم قطعا هجمه‌های زیادی به‌ما وارد میشد پس صبر کردیم همه بزنند بعد ما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25745" target="_blank">📅 11:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25744">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/thfPZad21WBUStcWQhRdsWH9fYpcpp-UyPhzsVfFBTynhcCLyUrk6JtrN-FGH929nyqiPG7oVcHJj_VtmhGwfKNyumZ7nJviNlVhz5pJEB2Cfati7nhi41IiTREoe1Lbk_U7hONOnmU7QQ-W59_E9EPQ9rrkW6eph9aJOU6zkJllmbnu2-C_uVSwzafhNYd4I8yl0WGVgdzS7wpSyEl9Kkl1f5jIMsYfoZJ25xmobTGax2T-lBapqAWX32SsyYZ6__msx-7E6CrIsrEhc3mRSHUJjk4oS5I8ta8oqge8AQxFbOEabCizz_cuM6XODK3zDnHcWcIbV7YrRRjxgjw11g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
#تکمیلی؛ پیشنهادباشگاه‌سپاهان به امید عالیشاه دو ساله به ارزش95میلیاردتومان است که به احتمال زیاد به آن پاسخ مثبت خواهد داد و بزودی با حضور در باشگاه سپاهان قراردادش رو امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/25744" target="_blank">📅 11:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25743">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1866f42adb.mp4?token=rLk0ZCYkgJ4skd28fOwI_X8HgMWgxtEJjHOPARYo1y5VsO0W1G1HtmkSYM-llWNX5xnn2WzjJ7ZhbLTeITN-yDYz-1n8ZOysDpzhDSnQR6iyk0BtVl4RMMo8E3nTYOiYvFsnk6wNeRmIEB3EVBEwqWHtXFH5UvHeN6cyZNCzajN4OVgUPmR9TEmZ9dRMm67-6cGlfkUVRIDJLeaEWehR8UCN9d_-ZeIravPlkvm5tG-UEoDoiyc44_z1ABXyTOVFV0X_UIdPk5zEnbiMEAV2-JCyE5VgNDIPsdHmi7b00952XkOLrx-RhyCxtrxP7e_K5JhR4HPVs5RKEubvB8RlpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1866f42adb.mp4?token=rLk0ZCYkgJ4skd28fOwI_X8HgMWgxtEJjHOPARYo1y5VsO0W1G1HtmkSYM-llWNX5xnn2WzjJ7ZhbLTeITN-yDYz-1n8ZOysDpzhDSnQR6iyk0BtVl4RMMo8E3nTYOiYvFsnk6wNeRmIEB3EVBEwqWHtXFH5UvHeN6cyZNCzajN4OVgUPmR9TEmZ9dRMm67-6cGlfkUVRIDJLeaEWehR8UCN9d_-ZeIravPlkvm5tG-UEoDoiyc44_z1ABXyTOVFV0X_UIdPk5zEnbiMEAV2-JCyE5VgNDIPsdHmi7b00952XkOLrx-RhyCxtrxP7e_K5JhR4HPVs5RKEubvB8RlpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
آندرس‌اینیستا اسطوره‌بارسلونا درگفتگو با عادل فردوسی‌پور: لیونل مسی بهترین‌بازیکن تاریخه. از او همیشه انتظارات بالاس. لیونل مسی فراتر از کلماته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25743" target="_blank">📅 10:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25742">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ پیروزی قاطع و ارزش مند لاروخا مقابل‌یاران‌کیلیان‌امباپه با طعم صعود به فینال جام؛ دیدیه دشان حرفی برای گفتن نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/25742" target="_blank">📅 10:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25741">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IEe15Rx_p2OG0IvTK44QtUsKvD_bPpafUwB2uZ6WO7ayyqZ5h0FLTqSIBlTkcdcThXr5DwbO_b0offVjtPlgBNGCMydTbzXfUSejZtuwDGrxYQhZi1dmQWlMd5AnhtAzFUSofQS2VgEUuFh0mzIsqw50wAZfJIlFhiRi2A0yF4c7jg66m8zHub39HD1DKrnRqUvG4PfMAvIJ1EkKR_oqx0UDjaJ6P_5saUwwLrsZz8VKGeTVj4O04NjDWRG8JFxcF3f5f9cZKLHuVOPkQllcbCuv1oP_YNtQsWVe4KQe0tDhy4XD5CcpxU2YXyOCxnGhqxGvEEKqH-2l0yqMSCsMKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
محمد عمری وینگر 26 ساله پرسپولیس دو پیشنهاد از امارات و قطر دریافت کرده و به احتمال فراوان فصل آینده لژیونر خواهد شد. از این انتقال 600 هزار دلار به باشگاه پرسپولیس خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/25741" target="_blank">📅 10:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25739">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MiW1l0rN_SeVn7KJRKu7vtRagMDw3wWDLdlxucYsp3l2ZkfOS8ZqirKPtSjNQrp4Z6kl6qyHP-9Glcm0ktH_6-9W3gyvjOeOSkoiGF6nePFIAUWinKuRKw30LTMg08JSlq23fM7Mopl_sHd3t4npGsCwo2QnCOy7P1UP-5akUi1bJJ91tPNSDT1VLdnWWUkcD9kdHwdMAXZ3_3imDne_V1oEy4Er8YKmD5PTsS4v4Mea_MbIhtatIryEbnnKR5y1bmGfKH97ZB5o7VQ5yNL4C8dv2Xb8gXVojvNaFB5nglLyAMDJte7R_fq61fmLRKD8SXBDUtVmd-pdnq6QLHnTsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تقویم؛ سال 2016 دقیقا در چنین روزی؛ باشگاه منچستر یونایتد با عقد قراردادی آزاد زلاتان ابراهیموویچ رو به‌خدمت‌ گرفت. زلاتان در مصاحبه بعد از عقدقرارداد گفت به‌جرات میتونم بگم که من بهترین‌خرید باشگاه منچستریونایتد خواهم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25739" target="_blank">📅 10:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25738">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89f9fe6011.mp4?token=A9UUopoK3sCU8P_OTGCg-rhBfd1D9h3Y7_HUE6AcZ2gW79QX6vD_GOkLuuhrI6BJxIkY0qHjv6V_kBMd6VgNvs7-RNQ7GshQVJa2F7eDCAceMoG2dPY_t4a-eDXmRsG7r_599Zi818FpNAlaIiDL7TqBehdd8dNFa54VzDTLGQ_1IfvUdHYnUAGdVHFZPh03rLscgMq09xXNOjdgJQNpjSj3rHbnFdbAYSxyahcqO9lG8bviSMT2tZk6JLahyKTOLMy9aflpOUSksWMY0HLXgqk3X3vDzY-IxBNeNUv5J-k683ufWc_lT6tjrITpi9AQRF7uTMoTAYIpjQwNaKo9DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89f9fe6011.mp4?token=A9UUopoK3sCU8P_OTGCg-rhBfd1D9h3Y7_HUE6AcZ2gW79QX6vD_GOkLuuhrI6BJxIkY0qHjv6V_kBMd6VgNvs7-RNQ7GshQVJa2F7eDCAceMoG2dPY_t4a-eDXmRsG7r_599Zi818FpNAlaIiDL7TqBehdd8dNFa54VzDTLGQ_1IfvUdHYnUAGdVHFZPh03rLscgMq09xXNOjdgJQNpjSj3rHbnFdbAYSxyahcqO9lG8bviSMT2tZk6JLahyKTOLMy9aflpOUSksWMY0HLXgqk3X3vDzY-IxBNeNUv5J-k683ufWc_lT6tjrITpi9AQRF7uTMoTAYIpjQwNaKo9DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو لو رفته‌از اعصبانیت‌شدیددیکتاتور کیلیان امباپه در رختکن فرانسه بعد از دیدار برابر اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/25738" target="_blank">📅 10:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25737">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B8XnuY7vNBr_cfq60JwLnLfQpRExEzt_hV_GNs5fSgqEWVsnTtnD0vromL4HjWghKSmAknviDH2t1vUT2JNh0EdknXcCBtvOGZ_4SVmaQAh2DsK0CCXOrR2cV1VkW3BQeio8BSMG4i7zfQnF5iw_BDPsxulsd_FguIHUoSlx3QvwnyWKkCtt_4unabSDkbySX1qs2Rzy4M6OM4PeJdWl4cGuaaJVKKoSf7P7SWReHhQZ_xPugKa-dWJxugngzkhAUUg-nNX9fgWI3ht2x7DpI5ffIr9LtpsXFkj_4yXBD_mQ9ky479K6Kf_oU3Qa05o_eSdjq28R7gMAoKDBMZUIjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک‌کنم‌اگه‌هرشب‌با ۱۰۰ هزار تومن میومدین چنل بت ماشبی بالای ۲ میلیون‌سودکرده بودین مثل دیشب:)
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/25737" target="_blank">📅 10:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25736">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8e4998f7f.mp4?token=QhahqKxVsRCflLFg_vvoAFHLEVKZ1yh2OwExg3yZStolsBE-dIEZhg6W7bclJm58MpXsgP6WtpFw0C_OeSCi3z87fq8CWfHGsDDmvYHJ7rZCM3wFeK7RO_SJCIHkvppSTaTAaSsaQuR-U33JJJ49NRr5hhHT2bsIB01wTTrggsjYkqub7lAIJB3teSjKhg5oTn5koxMiW9rCIsuHoAB4xi0EOno2AU9VTvD5hnRXyeXXc0P3F6-YloAIcewe8sEtHPGUpotB5sPvIq9ORZS1S7SFus1-DaJ7f2SlFYtJcVhjt_lpTBPtuAQfuGnX9Rz467Ixx91LnMqI7gzN0PDiZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8e4998f7f.mp4?token=QhahqKxVsRCflLFg_vvoAFHLEVKZ1yh2OwExg3yZStolsBE-dIEZhg6W7bclJm58MpXsgP6WtpFw0C_OeSCi3z87fq8CWfHGsDDmvYHJ7rZCM3wFeK7RO_SJCIHkvppSTaTAaSsaQuR-U33JJJ49NRr5hhHT2bsIB01wTTrggsjYkqub7lAIJB3teSjKhg5oTn5koxMiW9rCIsuHoAB4xi0EOno2AU9VTvD5hnRXyeXXc0P3F6-YloAIcewe8sEtHPGUpotB5sPvIq9ORZS1S7SFus1-DaJ7f2SlFYtJcVhjt_lpTBPtuAQfuGnX9Rz467Ixx91LnMqI7gzN0PDiZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آقا یکم جمع و جور تر بشینید امباپه هم اومد:) فرداشب یه ستاره دیگه به این قاب اضافه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/25736" target="_blank">📅 09:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25735">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BdF23f2CLCHi_TN6Q37LAJlYPU9TtFu_YDtMOTWqU0xROqHhIU0v20CXHgX0QzhWHcFVk5O5dtiESXZdAjcTw4ndl3SIraHop1BEX8gYE2yF7ET1d0lNSd67JsTQbAjOuZ-HxNUOFgNhv28ZlkCH-q7GAfEIiYqN-JWg_mR4tFC5H6vspmzkCcrlafXDCiWSEarpgMKzxkxqRHIdxzkYtINiBhJr6UHvcOM2vFUxIZIezgWAytJRde0kMQ7h7makit9Qbk_qALnq2BXASmscr9-KC6WPrdui2dfcEnh43KJ6XWYk3bAUybD1CbjhEhkxNV_-wfKFoi_bZP3T79MGWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضعیت‌بین دو‌نیمه فینال: بیژن ویالون بزنه شکیرا شیک، کی میخواد جلو این ترکیبو بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25735" target="_blank">📅 09:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25734">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RkS85KtrsjkmqMsaGfJFcLkJh6sZwScE07Vj5LQ2Gp4lq9cQ0ebgfwOkxz-jNEYtTuSJaYZTt-DmhyCUxi6ce-S2ODxGMMy6aXtEfccFspokp4iCksbBcI-G--XiyICABzzGAzLR_MaiaynExRSZQyX5Kp0wdxvxMShQzMNnKuzlAc9Bcy3PZAdtTyXxyiFbsJXTvscT7-7CCqDY9kG3ipH4tlDFTdXhxDWeuDRYzvHaaRpZGhKvMAe15snH5bFXJS8ecZSfEaCUN5YUzC84rWsR3j0y-rNtyeHgK-QM85nJh_FWHtndy2aaGUlPApmcoyM_JiQAkWO4RWMVyScLgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گویا فوق‌ستاره‌انگلیسی‌ها شارژشده؛ دوس دختر جود بلینگهام: فردا یک‌ورژن‌جدید و فوق العاده ازبلینگهام مقابل آرژانتین خواهید دید. مطمئن هستم جود میتونه انگلیس رو به فینال جام جهانی ببره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25734" target="_blank">📅 09:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25733">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0f3f3f6d3.mp4?token=b6IA5gY1sdKooZ40mnDpIxiBs8ftILVcQsARvXuYmZtWM_Nq6tuMiSE4Hwxa3qETHQ-PhrKLGBNb40s5eEsQUv9uvRYGt0fnZqt9IMEiru7vYS0jh4HC2B9uOwVQXXTe5LYHfy8lFei6bZOVXoiOJAbWsW9zVQXpczM5nPr1Uwii1FDVGYvg_INBPboASQyh6yM5Y_aj58t90x0j_akiJNEmnWP9HmsuuZBEu1gdUbBEG9LZkdlvK04rUQcrKN-V8ec43giu24e3zpaOr28Tr70oeInEzNyRNMgCOEgAEEx_91-RUvf_8_Hu7-xQ9f_ZadK0etXgOCHz2CtvZ1bqe0ehSDjURrc2ruCWvZAM3YkQkJ8Fmm2aYX9yEhbZ1pRggiPE9rCoUd0bGI8bm0yqmACje54M1ICFCrBAbAaErGGqjdhEMkuYSs5cyjtvo4JN9YfyKMNCm3Of1216-_Tu0jjgSaLjXbPTEm4jNw0n3Fy44ypl3qQSn4z1CZS5J3GWrP9YOrI62FGJV79nq-My4lR08im0cXf4OQYtPli5hvbdgheWhkWxwb-X001FmCVEtLiFqQKpCD21j9VB_ko3nais53ZtIFxODPh_4a27YF7akt1vy2feZA8w2VBdlBaFzgrqzGnExOxM7oEZMiQAsICDCJvkBHwcJfmwxnbuhB8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0f3f3f6d3.mp4?token=b6IA5gY1sdKooZ40mnDpIxiBs8ftILVcQsARvXuYmZtWM_Nq6tuMiSE4Hwxa3qETHQ-PhrKLGBNb40s5eEsQUv9uvRYGt0fnZqt9IMEiru7vYS0jh4HC2B9uOwVQXXTe5LYHfy8lFei6bZOVXoiOJAbWsW9zVQXpczM5nPr1Uwii1FDVGYvg_INBPboASQyh6yM5Y_aj58t90x0j_akiJNEmnWP9HmsuuZBEu1gdUbBEG9LZkdlvK04rUQcrKN-V8ec43giu24e3zpaOr28Tr70oeInEzNyRNMgCOEgAEEx_91-RUvf_8_Hu7-xQ9f_ZadK0etXgOCHz2CtvZ1bqe0ehSDjURrc2ruCWvZAM3YkQkJ8Fmm2aYX9yEhbZ1pRggiPE9rCoUd0bGI8bm0yqmACje54M1ICFCrBAbAaErGGqjdhEMkuYSs5cyjtvo4JN9YfyKMNCm3Of1216-_Tu0jjgSaLjXbPTEm4jNw0n3Fy44ypl3qQSn4z1CZS5J3GWrP9YOrI62FGJV79nq-My4lR08im0cXf4OQYtPli5hvbdgheWhkWxwb-X001FmCVEtLiFqQKpCD21j9VB_ko3nais53ZtIFxODPh_4a27YF7akt1vy2feZA8w2VBdlBaFzgrqzGnExOxM7oEZMiQAsICDCJvkBHwcJfmwxnbuhB8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابواطالب حسینی در برنامه دیشب خود خواننده آهنگ‌معروف "جناب‌سروان ولم‌کن" دعوت کرده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25733" target="_blank">📅 09:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25731">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EsRjCvGKjC6x6qkF7zDuEA8Ombc36OxjqZV6U3NqUrxugNB1o60hOfH3xzr2uXpJxkZhlN10_RRWQ_LVTo6441N8txgU8LL4doArR6nmnvnKQ2p2v5gZ6KFFrs7-qhaBiqqbyDciIr1KnqyS-cl2yP6Nb9Y8zP9vXek-YKuRWYRS6a5RVKSzLovqsep0r6j1wbUlWT03eHTVB9zsPkmOaZdJS3C1ZSIUje_YEW5MfRzlfqjukZX8exJKa1YxJadEGTl6I0mfe1sMtFfgnoKggJreFY6XUvXMSpu7H3KwuDbq-MkP1ZRAMGRPxmBnFokYQIry2yTfGpqP9k0JWIgzBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#فکت؛ تیم ملی اسپانیا با رکورد تیم ملی ایتالیا برای‌طولانی‌‌ترین نوارشکست‌ناپذیری در تاریخ فوتبال ملی مردان برابری کرد. 37 بازی بدون شکست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/25731" target="_blank">📅 02:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25730">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQEWACiCf8bhysqio7Vr5Aqlt5nCFsaTlo0uc1oNHuSIOEjZDvyJFGPgtfxNNjGC1aYe2M5I6DsTuMvQLxoHvjfoeXJPB7q11gW-q1yGrUzJztB6JYBcNBXFIEmliJSbnylgk9oN1qdAshkNTH_8ghNWzOkgAeW3o1OF8cZPj5s994znPb_X4sK_sgl7X18AP4t-6pqUEKi6UeSpp5hr-lbdscMZo_Np9qni_0wB_LwYixXgh33xy5Oj-5T-tQZd0s4MDlotjurEiIFykgESCIVE4xmpuOMzfr9_7vp30jHSQQHA6eCR8MoQovjKUwp7TXg80MFocKRTmatFV40pRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درسته که کیلیان امباپه امشب تو زمین نتونست گل بزنه؛ دقایقی دیگه گل رو توی تخت خواب میزنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/25730" target="_blank">📅 02:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25729">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PronfBLSxeOHBPWi_9M5Vaqvo2dkyJUhKNs5iKyxex0aNkvxuXVskgmmaO8SeX-hDX4WJN23x4GTSA9iiHitC9kqCz1E5yxgYNGu5Uw_CIoxb1_pPIx9mtztTwZglFZ87ClXFSPnVHiF1qGyjspQiZQQUfzICP9TFR9jsVQqI4mSEM0GJsykL9J7dnnO0xHuWrp5p17fS6nGOm22-Rs9BQJaB04aJGTY-ycTQdXdTSTobYA4E0R_VBQBjRLaCx1oiqVlvdMV1W8N5bFrgp4by7VI3XZUPn1jf9wx5tHhWYqe1DcW9jAYFyRLId6gA1119vD_mIFb1-XLStLP6b0grw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
جود بلینگهام ستاره‌انگلیسی‌هاگل‌هایش در جام جهانی رو به دوست دخترش که قبل هر بازی به او روحیه میدهد و او رو شاداب میکنه تقدیم میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/25729" target="_blank">📅 01:51 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25728">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RpeCuW2SYEHdxzmZlaI570FoqMONebFMn8_h4IHGqtzAnMCAt0sDmAzZVf3Nx8Xobpc3jHRGj4yY8_kEjcTCsdzpbKvm3JOfXszqr7YQxdK9AoLm6m6sWREuJJf6ROeN2xf0Oa1LjKTEV2KV1UOgP2hb7QxuYEwP3mpgp48Zbf6ME_mD3qv96SxeblHYM1Sy1Y73mUkMdLxZ8e66hGbj9A0hOft7XV6tDtkzD4cKzXUwVmZMfj1kuRdopJ-lyHH4kB_PSFawOmbRhNFgnRelte6XPUFEFce3ycICSMGn4dKDkUQ5mUz0RH5AxRCoJn0hM5eL90-5gBfRGKaNuYbhpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام وکیل اسپانیایی منیر الحدادی؛ این ستاره اسپانیایی به خاطر مسائل خانوادگی "بارداری همسرش" و آرام‌نبودن وضعیت‌منطقه برای جدایی و فسخ قرار دادش با باشگاه استقلال به توافق رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/25728" target="_blank">📅 01:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25727">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50f8c52913.mp4?token=FqAy3kSY9_yicvuEfn3R-ioYUOCaq_voYcMfi3QkFKr64WatsNOvrhN7C8Q2FvTeNlWW4URZvpEnPX1L-yZYvS-R9sXQLNCZlnwjx-8BulrLEHAsHOqnnV-3E_gzRefuQrDOsoiRTf1FKbLgZKOwcsMJrS5D9JVOh4EuSv8fowEigcriFJfETc4XE3qZaJMAaRQ_sHkLSmZYegOPWPsgqBcXr-B2edX8cF7RBiF207F2Vu1_fyIdGv-yByxqvTY9KAjstW6pdTOQBCyEGRxsMcXAKmEFMeDug70r53Joq3S-MLtssML5RiuWDvltzMUFKYCUDEaCbG9_h6TylHIsUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50f8c52913.mp4?token=FqAy3kSY9_yicvuEfn3R-ioYUOCaq_voYcMfi3QkFKr64WatsNOvrhN7C8Q2FvTeNlWW4URZvpEnPX1L-yZYvS-R9sXQLNCZlnwjx-8BulrLEHAsHOqnnV-3E_gzRefuQrDOsoiRTf1FKbLgZKOwcsMJrS5D9JVOh4EuSv8fowEigcriFJfETc4XE3qZaJMAaRQ_sHkLSmZYegOPWPsgqBcXr-B2edX8cF7RBiF207F2Vu1_fyIdGv-yByxqvTY9KAjstW6pdTOQBCyEGRxsMcXAKmEFMeDug70r53Joq3S-MLtssML5RiuWDvltzMUFKYCUDEaCbG9_h6TylHIsUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آقا یکم جمع و جور تر بشینید امباپه هم اومد:) فرداشب یه ستاره دیگه به این قاب اضافه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/25727" target="_blank">📅 01:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25726">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8utm4y-q9yuZBA7vl_PiZevEcNI4Jea1gQSvjv-54zneRI1AqqSwXtEL5K4qCS-5jH9wTZh-DqAlfOIFx7PrmfRdBBdzYGpnCcA66k7KWUvb5cHNg9why23SPIHCbu86E9Syw42TRgZsiWHwvyxR2j0ve9Dezs5sgs0CcGLNvQ1EXktZzH7sIr51rg7w54XYnCTHMTuwzHyMPFpywv0p597F2d_UIenQm_ewQQWjUB6PL6hQ3kszqlmrhoTkd1qC80rodWl1Fig7Vphx5aEfb_LulnEiZJwV8ithROBenhDv39JRb9Ql2L4MRjYPv-6xD9juV-dw1ND6rCoCw90jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇫🇷
استر اکسپوزیتو دوست دختر اسپانیایی کیلیان امباپه امشب تو تخت: آخه من چکاره‌ام؟
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25726" target="_blank">📅 01:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25725">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZAPsFwaiqtMrft1tPqiNSh47C33aHJoJBCJWiZ7__pnVtlFu9QmtGAbqdXWzdHbrOVj7Bqmhv5Rwz7o2cW2cbbVqeC8SXteUooJoH4e1gTmOu9DRfRG25rkYzavWJLs8Q-Cjuy_nOPIZiulei3hXchS1IIR0ZwgzuMah2tFtntCg8x3mYa4PLvQYA-uEJFeS5x-aCUam1mAsYm8G-bJvQD-hTRJbXmqp-KzO30I3W1-cJrywzGyWccPj7gVt2U9xVOdg_cdWrf7a0VuDT6RmiMPxlCeH42EmEeXFPrRpAEzR8lgb_3caMXWR9bI-_2TD9b9sW2ubruknpFx4CLdzaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فکت؛ امسال سال‌ خوبی برای دیکتاتورا نبود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/25725" target="_blank">📅 01:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25723">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/brlI0oZ9pQxnuzy5CsTHcq9F8mZ4az5SgjaHWGAjVjeIImyA_YCLhq3ldQ4nlqDMMkpaiBJNkl4GJsWqNu_7X7kth5m2nweUWNU-IAfEeh_fUT9lqasdk75LfByUIOseMGBG7_ERHS-_E3exPGbZdy2w3dIaVQr4CThb25xrkQaFTXgvKkKxLMQsjtBZ6K1mTWUF9ciFNm8SDkV_iKb20erhoHntGxfkbYeoVu_Lc0-LfLLLrsAcD4ONSAvmE5fdS4JSl-nxKbTNpvo7PvS_iHYVWxG2CsLfMQ-rqFlxOHAPYUC7WpwAln594KU6No8hQHXqw4dweMrSbo_w-DMXQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OjApaMDzxsXG7xZX4furhl3NUFYPBTHMpJoEQYr3yAF9kC8fBKsCdDD4O2YWpDbGAUVtVGKd1vi2onNAq4GlFSun_WLOEoKd-11EfpdSVKAXCRB7Sg1Eo5hl3VhYbiY6RTvAEf5f21xbgq7shDdXrTZGqnMdu2UTTuU5yWai7u6l3dLEKEtnH_Q_sKo0RB_13OmJ2FwiRQL1mlbbZMXBGKLkvW1v-f5-B0SXp5wA0wP19PFfoHY6aXklOa1QRVyZxDJ5hpqO2rf2CYf8b0sqFdzMMixE8r-jXEQSaDzOQlCs3nur8MBCj2qcVG4IT8q_2GfNLp7QKbI-W_uWkOlbsw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25723" target="_blank">📅 01:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25722">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HFR7SWUc3PBn2dl5Oyy4qJF34DBgSyfNRVdnEyK0Rmwz33s2EYya2XqC9wbJflMSRLeQrRY30Tea37FuKYSjIhyOYmWsMpkyeD2bOJhhhpjpmrai--9ARQmlZCBvPJcdC2BKAOCZ5Zo9cbjDJKXMt_3S20GgHChVSo_RU_qj2oFvJiOIy_zYgTwq0UGBZfG58qaSmbyLpuVRAiVlYA4CZL1tydagns8ztbO_knIUQXCliPjDu-mPSZ0EExa-fSB0ZymCNk8oCU4QWs2OZAFyiYKpShf8VqANfFTk45o2fWp4CpN3ha4IlmyUv2e03ez7xdNigPctALacTfnoS2Hntg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها دیدار مهم امروز؛
جدال تماشایی انگلیسی‌ها برابر یاران لئو مسی درنیمه‌نهایی جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25722" target="_blank">📅 00:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25721">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GrJOjxOd7VL8O6XIuo_J1h27KvsF_QHZjy1J5zMUQNyR4xTg_rN4OVJlEXLYcgZRIf70nD0rJDudHEZTj8uWPQhNQf0yQA2Zs5FRMVdkB6jggTBQV2gEfmNI0PMly1CNF9psDkw5V9ARW0wUewhilMTGGVcl7rLldOGSDZVfg2t-hgpi7SFOwqNlIGadOtvGCeZRFwMCGycSP5-kILT4iceNocfezp6tj15kukcHSEOY5rz5y8POyGxS3RwctzX3EOij6uWMO_TF44Kp-wfwhDBpHlRyNmd-ByiFhD88-7FDnKtzWqOX1rNgI2ItL150ujCzaChDez2wd1fQbjkE3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌تنها دیدار‌ دیروز؛
راهیابی اسپانیا به فینال جام‌جهانی با نمایشی منظم مقابل شاگردان دشان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25721" target="_blank">📅 00:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25720">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hO06uigU3WylLOenoekx7mtv9QIX9lvZ4jI6yYRH7YKR9ZqRZjrsSBweb7K9e3u8HEdjlnMFOaGO0tMDEAWBIGy3gslvL0sDeEUquPQCJKYi-gfM1qvurwi5ajYv7Q1eatX0MK20dOiTFCx9X2T7D8RfDmZOMIdVMOR-y2nNdD21zfKR2Pdg6i1gEjMSHhBpVIYMt0G0AfOkQQ-HK8gVSdcqgRS-WAkm9HS189ZevhaPflYROVQYVcx7BDFvgsmOqCB3oK4XMkcWqbbg91ZrApGzeSEztfFdB793YkpnVKxe2qeBirN8qLwEy4NoRnUD3lw4kKS9uI28ha1Q6NNWpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#تکمیلی؛ زین الدین زیدان برای قرار داد 4 ساله بافدراسیون‌فوتبال‌فرانسه به توافق کامل رسید و در پایان جام جهانی 2026 جانشین دشان خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/25720" target="_blank">📅 00:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25718">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a0jR_o7M3SXyZnBae5Finq0-euPgqNH7vhdWgTkCjkUD8Tu7exKy5O56nfGgS5-BgdmmxtDUKoPLGTRnB-05qz42dH_CgX921m3pIyDGJ3PtnyOTmkU7-KLn1ixQo22javiFIEf2AyxikF0lF9Ff1tLgEeYHehH9Sk6kfRFPXkASimf110sFTINUoNT8W1PVLBfFXg6vvYwTmYaMtglzrQpR5kpTxOBXZ1EZDGXSDc-GmBzWscDfF2y4GKxAZ3Gkp_ARE7__IdwSkQb8LA5m_pmvP2s0G5ELA4juWGezCKCFv7uWnkUjH9MYv-XTQSG-9MAgiFm8WsnJfGPuwwzPqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kby4K6jyss4ATk6q0UmMlncALl_RlKA2RwZWrb1HWyO5wF0pYv1az32sgAIQNcwrS5UEA3i3MAQR8hRaM7P7-7lCP44ry86-D4FVkKT-hE1aC7DuuLelZKbr1TO2Y-OoJmf9p5EjgjTAuLkxP-uijV8d4_3OGupFnyu3_xRKsrXvaMZWaHFDlc0VxgkG7EyUBFt2TCYiRRUf87cOVFSIgLLq-QLGrWRPwRQON4k1wZCJzquf6IEjt5rtQYlWA8dBb4iMVhVea_arKS7U_ixPyLzCAg_wJPW6MYssU8Xv_HOUWJ3BQ7r3GzJX-2Nw24ZZ_377_v9D-onTqXpNuF8Bjg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ پیروزی قاطع و ارزش مند لاروخا مقابل‌یاران‌کیلیان‌امباپه با طعم صعود به فینال جام؛ دیدیه دشان حرفی برای گفتن نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25718" target="_blank">📅 00:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25717">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rgogNaEOpdyWkS87kjaKku0aRx6MKO8kT_eX0A-tTmWwWBGZXTQ_zTK5sflVbANOPnYojJ5_yFSNJofIx2gQhibPxQ4qQPzULbRHrLOqKd7MM_k4rgxM21KPAc0i46_uxPl43Kd5oZEmzZ5y1-AbSY09HZJ3-8D8NfQ-kgzBx4M5KaeOkV0ADCIx66GKU1V63CEPJ1iyjqUZBjmzHr4-dIBUCML27gfHtUZNKd9p0-qup6DWJymeNjcsR8eRK3smEl7ADQwmLhMhup9pjVzXcs3Q0xvRLve-LLomzRgFKiNhZdxfabrLgxjW80XYibryEZ_GGh-tqFn8MmRRVIPAjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ پیروزی قاطع و ارزش مند لاروخا مقابل‌یاران‌کیلیان‌امباپه با طعم صعود به فینال جام؛ دیدیه دشان حرفی برای گفتن نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25717" target="_blank">📅 00:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25716">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AmiGRwqh9IOBG2Cx8r_CbjqPt9OAlOtgasKjF7Z__V2Twa768COusiZeq38IerltFwHZjQVKk0kPO7Wfr2KgVixBPgfNDHKkORcHfxXAHUNAV4JksBqyxFSDJi201mhHwCLxBvFN1uZdzEHLsmnWQmzU0h46zu3cI4hQcKmKpAVVx6lR8GYabfHjBmkX-SY7BEJZn5Ppzu5vtuSCEPFvc8Y_EwPcMEFjR8rU0s9wWtcj8HWIphWWdBSecWp5n_Ltja1tWnyrkXgRYAbziMUwiDGkrAPq10g6YsP67kLg89d8mL4pNr1VQgtNNDzJcH6Y3xj2utMseKIrFtvSirPUuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار نیمه اول دیدار اسپانیا
🆚
فرانسه در نیمه نهایی؛ برتری نسبتی ماتادورها در نیمه اول؛ رودری با نمره 7.2 بهترین بازیکن نیمه اول این بازی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/25716" target="_blank">📅 00:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25715">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cL8CmTR290hnsk9jVclfrgaG2F9bllETt0O7w2pDUxtk4kqMc6ire9BD5JtMcvLtWKFnXhAl0W0kxIDHkZIX-1pL5TW87AJYlpz88igbPgg9KhGv4vjnMPfger2gciYg_QnjBz4TmAz5dZg-pTZ8dVywHcXkvk3EOshQg1P0dyg0ZqEtwR0hDWS-SHc3FDVPtBgJJInlHNVNehAZNxk3SaAdJi0WyOzFIHyOkvXl-cl77py1DGCaDJScdDK7jyxr7KYj83ORTYQUHSJfbq5xrs2YvI_qYfUuX5kbuL4gquhimELCOX0lSgIWEujVcBDh2GGnP3SWeNq5YJBrflXylw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باشگاه گلگهر به‌‌درخواست‌ مهدی رحمتی خواستار جذب امیر رضا رفیعی دروازه‌بان جوان پرسپولیس شد. این احتمال وجود دارد که درصورت موافقت خودِ رفیعی، این بازیکن با پوریا لطیفی فر معاوضه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25715" target="_blank">📅 00:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25714">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t45TzCHi-Nzf0B6x2crGOIVLF10_brXzckzfwQkmTh59YP0aH0Q8-vTq5ubHSHXONaBsbW5hn3D98tg_jP_tNnKcn-fTqyco41hCyZR-Nr9--s3pXiRyP_IIFe4ohqm7oIN5IKi3djnNM5cQ-96Vvobi7CmhLIV8Bo5IvAZj4FwyqtgaBlRNjl6KVIe0-F-Uqf4Hd8JhNJ630L2x7nOUXjhfE7tQImmlihAi2mZbH4XHi8LhrGItSEFrW8u-IRlSINpN6ExGBY3r3Gtaw-_n5MCbyn8GSTw6UyudCp64lGX3obv08pzAdVujocLds3mQr11yHt-MVkiFyfvCfn1org.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
وریا غفوری کاپیتان‌سابق‌استقلال درگفتگو با عادل اعلام‌ کرد دیگر نمیخواد بعنوان دستیار فعالیت کنه و به همین خاطر پیشنهاد کادر فنی آبی‌ها رو رد کرده. وریا میخواهد سرمربی تیم لیگ برتری شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25714" target="_blank">📅 23:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25713">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/te_uP6nxuN98tIzxHZfi3Be6JU-uSVXwbCT-8odtr-hQDNfakru06NwEFmIlTH2u5MLzlFOsXz1tQbzzdW1H-tM8SJkYhUExKVm5XbCbj-v74nDcDC6-0cFgtsQyIqLGc3fwovB8zgReugpP0l6uuV_4oO_hlzDQZB2UVk2fHDGOaLkUy9-x3nD14TTNKKzGCmpyJ3aSlxPDnS20r4NvgEDSkzQ76335pBzTHtbMLPbm1Ie95Pf7CFIt1J7EnxJoyAfGYTYrrCueKKWq0HSGbHmO0nwhridGF9ohUB29FPRKdJ1ZjpIu2TDFrca8-w_9QrnNiS_QyfJc3Fel61UiwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار نیمه اول دیدار اسپانیا
🆚
فرانسه در نیمه نهایی؛ برتری نسبتی ماتادورها در نیمه اول؛ رودری با نمره 7.2 بهترین بازیکن نیمه اول این بازی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25713" target="_blank">📅 23:33 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
