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
<img src="https://cdn4.telesco.pe/file/IDlIcgVzMC4pt-LUkL68bFxexMQ55XE5dU7OKE9PK8O5hOlBj3zUxsmfyp7hUjR_IvosrcnS3bgIo0bJgHepZqZON23PGvpHckxqKM2XqndUBST1OZuvrSNplbttYq_A2a9h4wge3yb5GS5YQr9608ZqGT34Petkh2D9MooMv5kvqg52t-wCvP1M7-RKVoFJ_LZ9LGYEQEV6Shse8m1_CeQsVuCyjbbgyHx6Yu-hgTBdXtx0Ah_FSf9cW_7Ca9QwljBjUNJpbZK4t49-PfF_PaVn6jirZs8W5Ik9xQ7oIMp2bhk8NGsaI2CqwjH0O-tHlFszLgocRnZDdpMuR7pIEg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 627K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-13 23:36:34</div>
<hr>

<div class="tg-post" id="msg-27117">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VBk-DGzMHI1C3v6qzozIqC6zcMlfw-_VcQ4vfTSr4NR-4h91M8Od_zdBmYQ2jjwZvLm2EVdTDy22siyZAPck2xtNR_ZWAm1VlFizwQBTIiM6P7Wt3C6lafJDxLfvT5hWp77WqoXmFGJKCrSrDbOo19NP3zEJ9PdkFV8EK3pVTtM5aEh3e2LUu61gdkKdM9eP6SpUCIvCdXgi_y2_5IR6Lk4myjE9iVIWoBwaWFs9gYkeWj9RvHyMw1zapOq83nl2Tx25kSoPraaAmCHWAV4uxGJdsduCWh-ZK2zlHV8m0hLexYp4EpKuomGgb2i4lkaxFKcnEPRTuL_vIUTxsE9DGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🤩
رئیس باشگاه اتلتیکو مادرید به زبان عامیانه گفته؛ خولیان آلوارز خودشم‌بکشه نمیزاریم از اتلتیکو جدا بشه. 100 میلیون یورو که هیچی 200 میلیون یورو هم بارسا بهمون بده آلوارز رو بهشون نمیدیم. مصاحبه های آلوارز اهمیت نداره. او موندنیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/27117" target="_blank">📅 23:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27116">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GAbD3C145jxhbnWFCJmbqcOQ_tdXfrF1UK4aN48q6DCP-Ot1HWpT4glmz000nrVRaNU-q-b4311BCy-NWHNfKAkuzzhE3D_rrjlXzGkRuyPNWOm7uweoYzCHh3pAg9-j3qGhJyNG4P0H0rk0H1boaphGnnVSeiSis2C7egV2ma_pjgGQeOT8b928FyCJ2WvWqcmAudbQZVs1mr4JjlEm8LgjAS9T_NfoRjbX7GJW6HSAMQuFPtowEGeaV-qCu2MtrXz_QrSA2BZ2rDLRZzmfoqDuHZ_UlF6WFWMyS27t3LhAWY2-Aoi7RCyiLazsJQzEQ4WhCfSTn_Yr5x5XgpFC3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌اخباردریافتی‌رسانه‌پرشیانا؛ مدیربرنامه‌ های رامین رضاییان امروز با مدیریت باشگاه استقلال مذاکرات مثبتی بر سر رقم قرارداد این بازیکن داشته و قرارشده‌ که رامین رضاییان عصر امروز برای انجام مذاکرات نهایی و عقدقراردادجدید با باشگاه استقلال وارد ساختمان این…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/persiana_Soccer/27116" target="_blank">📅 22:56 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27115">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52510ee628.mp4?token=rr--AiL2JPfaLwGgC_AIS5yjzdB5xXh1foiUN9-RrJs8-4GFiO31YahcD8YtIkV5dKEtN9PtLmrx7Rp9jBeZaEBW8tO2H-3ZUEwnYOE0JTT2nSEGp-9b4q3jj3lop9fToSFUsBkqMyVAhlLgKVwQfUr5p8QVmt9VRvwnQw-6Ok8hmrW6iT_SRRihXfW1cuzkUuoavVxpJ243pOTE98zLtoDqFuIQ9UV2bT8d2s2z_UC3BIciOzGZcl0eYCv2XNNWF8ncgfTsusH9qZZDaZqzOdEYgINRkfQcUbydbO4yhCJBnJGIPGzfnTPUYbH-kxYNTZNSu9RumgE6ohpfMBxHiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52510ee628.mp4?token=rr--AiL2JPfaLwGgC_AIS5yjzdB5xXh1foiUN9-RrJs8-4GFiO31YahcD8YtIkV5dKEtN9PtLmrx7Rp9jBeZaEBW8tO2H-3ZUEwnYOE0JTT2nSEGp-9b4q3jj3lop9fToSFUsBkqMyVAhlLgKVwQfUr5p8QVmt9VRvwnQw-6Ok8hmrW6iT_SRRihXfW1cuzkUuoavVxpJ243pOTE98zLtoDqFuIQ9UV2bT8d2s2z_UC3BIciOzGZcl0eYCv2XNNWF8ncgfTsusH9qZZDaZqzOdEYgINRkfQcUbydbO4yhCJBnJGIPGzfnTPUYbH-kxYNTZNSu9RumgE6ohpfMBxHiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
درمصاحبه‌جدیدخانواده‌نیمار؛همسر نیمار از قلب بزرگ او گفت؛ ازکمک‌هایی‌که حتی دور از چشم همه برای اطرافیان و گاهی حتی غریبه‌ها انجام می‌دهد.
‼️
البته ستاره واقعی این مصاحبه شیرین، شیطنت‌ های بامزه دخترکوچولوی فوق ستاره سابق بارسلونا بود که تمام مدت توجه‌ها را به خودش جلب کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/persiana_Soccer/27115" target="_blank">📅 22:28 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27114">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfkCS9H68mU_PJJtPR1dOj_zvtBqLmWrHEBgmfGKBzOrx8zItRR1UIjCV41Cdo9kd9W5ZpdUS6OFTBHGUEzQCkXovolfusvDX29tFSviGG38CfqP6z-kIABjDh-bT5pHioP94zmJswh9i371SyM_0tyg5EOWiWIyYgB5KVUPCz7onqdJnxgIRvAbkMIUWCl71pxKr_OaOFEIW5ko0J8tcPCCq37A0sWbgYWVfk09JyIOl-HJ0abi40KoA0xaFRNBPkmnc1gFaAOXa0Z7gR1Bda1f1-V1zImoo0gqqs894k3JXsOxrpPsbb_LqBmEZg3CuD5nb7SCtSmYBnzKzQXRoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌انتقالات|نشریه‌ سان: سران آرسنال به درخواست میکل آرتتا به‌دنبال جذب یان کوتو مدافع راست 23 ساله دورتموند در پنجره ژانویه هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/27114" target="_blank">📅 21:47 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27113">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WWGgN0qtBBCTMP_re3UDCOz8IgBCMni7cgENy8NjJmaZRx2YzWfvdGL2ElgugbNdXJ7TBFE9RwtxWk4VLKaXK42-SejSVIYcPs0Y2NRH1rm799-KACoJfQoAqe9TG_6bcWBeB_Xm-MExwJh0WNv2VowYgZNdwxEyAsRm2H-OBwZkdaUkoZ5MZMHK8bWcxDTa7OBxsZ1uMhgXJv4WpeW_1CgGNLM3C4ze4P2iShQlNEHpJVfKTr8CpKD3yNwkTJ_bx7Q749Yf4Uhj4Y0mq-pyyacQ5_Jy4mlpolISTnQmhwWwQtHkDY1FUF7iHw-UWn5-dZzNPwbv9N7fj4eF0EXXQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کارلوس اسپی مهاجم رئال مادرید:
الگوی من در رئال‌مادرید کریم بنزماست. میخوام با گل‌هایی که میزنم همچون او در مادرید محبوب بشم. برای دیدار مقابل بارسلونا در الکلاسیکو لحظه شماری میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/27113" target="_blank">📅 21:26 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27112">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q42LjlUXyZKsYxEcyOkQ4OAsqVN1BZXGncGQNwkfjawuPGyr8C3hE_2zQQ3O5V0gI3MaND3-dPr2ir2Ag_X9v_GA9g9kabdr3qktNI44Q_O19vYezQIq9wi57U_aZSRlcD8V2gYsxpjJystLiUt575-ASyMbHnbAg43-QZSPT1nHJ4B7ywMPzdqQyzj41MWN1s3psmuwOMHoF1Bk3GQtBoEXKorHYUnJyG81cEYu3SPREVDYYiEcKTG2q6tSZPaUv9FQQHbdKKxnP1TDao92Yi_2fSVBKjmctvmWziAJ3-zNzXdBnfpng-wg8bczxYHLp7kk9CRUI6EpqBT8xIguQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌اخباردریافتی‌رسانه‌پرشیانا؛ مدیربرنامه‌ های رامین رضاییان امروز با مدیریت باشگاه استقلال مذاکرات مثبتی بر سر رقم قرارداد این بازیکن داشته و قرارشده‌ که رامین رضاییان عصر امروز برای انجام مذاکرات نهایی و عقدقراردادجدید با باشگاه استقلال وارد ساختمان این…</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/27112" target="_blank">📅 20:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27111">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfAbLigdGpwzS_SYmd_1vgERTjy0PmcML2IPdP_qvpouPooVLwk16OtQ29vLshI7Ci-ubf5gRc0g-kxeDvG4JVIGBsCz_F3mBd630hgHDNT3u_ymPD7iGfIrLFnFiikU6Nh67mm2AqVOEuPH8UHdI-fyIluAcGBOym0KmvZ26_U-JFXe0IojGMIsnaGpk8_M4g-SOHxXPzog78uhSA8KzrenlMS-wvf0NwAaknVo6pbiiN5nzKD3VDGtuYhV05LNVyz24K9ar9PagXygk7FyNAZCMz65gMgv0s6yNwEZess_unswvs6VSqmsv23aKnji96rHmlCmGss-X2slisS73w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فابریزیو رومانو: باشگاه ترابزون اسپور ساعاتی قبل‌پیشنهادی دوساله به محمد صلاح ستاره مصری سابق لیورپول داده و منتظر پاسخ این بازیکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/27111" target="_blank">📅 20:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27110">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMQyx7PA-jBPQvZFi3GpzPsRZUeE2yT817Y65ilecfajIxOcqqEhZJxS7iiZfm5xshl-3HXG9boPpHW9Nl1ytXCgrZZ-_qW1pEozmfZff8nbLa9kvVuKdqmSFVqaS_J2f5MYLakmrM7l1Rar-w_JWX_xTCTg7j-u7P0jcaCmjJ2thf_Yn2R7HbA6Rk6Pmfi5BUHPHrvGXcKj-JrzVu4S1qGZs5b6GgtSZvI20O6niV0-Qj5WOawq8e3iKkJnArAB11rxuzHWvuEF4u72HSoY6m5LOztnhi49zKfZ_SB2vIMhmyi0sKTzNB09TQn1ig9nkLC5cDI97aZbbWRLmbpOMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔴
استوری جدید آلن هلیلوویچ هافبک تهاجمی کروات سابق تیم بارسا و مدنظر باشگاه پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/27110" target="_blank">📅 20:30 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27109">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/St3TS7ZhautjT2ckPJwIiaQU2fsKPAfhod6KrA4CKqgNwVkwuiCi39UBREVRgKMxJ5fHPOsGypjqvtjLOdhYODbppXu2KQUR9T-oNVSl-OlcalTKoh7lMOueDVa0nVV45IPYlTI6hkUNr2Wg4ww7IhLhXyiGR386JDtjG83CbyzTiavImulp4gPno2vn_6YTk7YvyKqa7UkerG4jEsjNinX0r9XiEF0HC5p9Eh1BmXqRLXnoZZ_oVlgY5N8NHuPs_gZasAVY6vwnSRckL_2G8697oIIlrk1Nr58VOVcN9IqZwqnu-KI355ObxgwvzzuP3Cs2kJL-pdigVjktOYgc6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
نشریه‌مارکا: انتقال رودری و یان دیومانده به باشگاه رئال مادرید نهایی شده است. بعد از رونمایی از این دو بازیکن پرز پیگیر باستونی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/27109" target="_blank">📅 20:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27108">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nWWYupexukNNBV-_I7mZoohWSz0Vl7sUyAQ190tOTdnuaLgNAF-uNpGkKsT6n_24lWbWdVTKBnVEePd7YkQHtszi6ysyPQTa_ce7KkILcxzeHAKgJczeSJX8B0P4oLys4oc772Tk7n-2KN5DNZBZcj5ax25f-37_5ExI0Qct8mYLDoEC3nBukSeHw0YrxEiUUa871cyvYjgrUTQ0fjRDjW1J_VmC9s59saWFJr_y60VAfp4isUBjh5LTacKcJkJLwW0DWd0WfBsghjD7rlx8DRAl2lqCyYLtzLlA-Igo37L8iRRbfVjsJhG6DEj-gO3wT_jwmg6w5kmWNItL6kopcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
پاسخ‌نهایی باشگاه‌فولادخوزستان به پیشنهاد باشگاه‌پرسپولیس‌برای‌خریدابوالفضل رزاق‌پور مدافع چپ‌فولادی‌‌ها: 200 میلیاردتومان نقدبدهید تا ما هم رضایت نامه رزاق پور رو براتون صادر خواهیم کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/27108" target="_blank">📅 20:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27107">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EtnEIbR83MrbJpjsDoxH6kHY5mweSj7Hv3dPEi0V85QKnYS-6ZQExnRZD3kQAYaUEfsoLihvka9UFpSLUNNQrIquhVtI7isS4kU8xK4SpZIx5db0iur16bgSB5UOKNO340dmyjZwChgkVieTeF1vDJGnqygGWL1T3Hol1N-MMkjbWK0gkEMJTrX1YocReize_-62EcAvfDfWmp5i5D4d31eFyIQXQy8fgtO8C3mIxpHa6nBeXtyoratOxNjhSRA5hJWzF1yO0n1iP6RgiDbyJla552XjG3UVk8hq5u-nyl3wOETM4tkes7lJjgs2Jqd0rN1Un6RwCZDdxOueq2Mclg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام مدیربرنامه‌های علی نعمتی؛ این مدافع ملی‌پوش باباشگاه‌لوسیل‌قطر درحال انجام مذاکرات نهایی است تادرصورت‌توافق با این باشگاه قراردادی دو ساله به ارزش 850 هزار دلار امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/27107" target="_blank">📅 19:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27106">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd6169d08e.mp4?token=HK8pVCyOu5Kt2cvZjlFypSxXu_gJaWGums6yKfw80I_Pg9U_nwpFxOYcgkQ6zUJQd_o2ASSQolhLuaZYYiCnC7ync8G-87zauYJTik9HjiA9ZYJBeIBma06myeR3JJJ2Wlv7ewLbAd0Ft6Yiid1Lq2H9bflog1nZKaxB15C0oGIa4QPgyvCMdOeXKqFElg0fZxmNm2HHD3C9MtD7gGzAnbVeLoK0A3Fawre51yDaQ692VNJXuBeg9nuD0Y7RTK58J6AR3yn68TbB0eX05ArkXgNZSZanBEDj371Tzb0r30u5i_wG4gM85mXntAu5h141eXo8MTPf8CMkBjBbZl8GVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd6169d08e.mp4?token=HK8pVCyOu5Kt2cvZjlFypSxXu_gJaWGums6yKfw80I_Pg9U_nwpFxOYcgkQ6zUJQd_o2ASSQolhLuaZYYiCnC7ync8G-87zauYJTik9HjiA9ZYJBeIBma06myeR3JJJ2Wlv7ewLbAd0Ft6Yiid1Lq2H9bflog1nZKaxB15C0oGIa4QPgyvCMdOeXKqFElg0fZxmNm2HHD3C9MtD7gGzAnbVeLoK0A3Fawre51yDaQ692VNJXuBeg9nuD0Y7RTK58J6AR3yn68TbB0eX05ArkXgNZSZanBEDj371Tzb0r30u5i_wG4gM85mXntAu5h141eXo8MTPf8CMkBjBbZl8GVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیش‌بینی عجیب احسان علیخانی که چند سال بعد به واقعیت‌تبدیل‌شد! حدود ۱۰ سال پیش، زمانی‌ که عادل‌فردوسی‌پور و محمدحسین‌میثاقی هنوز در کناریکدیگر در برنامه«نود»فعالیت میکردند، احسان علیخانی با لحنی شوخی گفت: «میثاقی رو آوردن که‌بشوننش جای فردوسی‌پور!»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/27106" target="_blank">📅 19:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27105">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qViPoyhAKcyGDIGj8HrUC-WKhfRq6ZFY4OJ5voLu29LRw_kv8_k6bG4ucQoLC4q6pKFReMvqwek0KWXeNPF9STGF-1rtOpQ7ET7IgEm8MTnJwj2aPqvp-0DA-PRJwkS_2cFt90Utq7BvE1aEm_5vN-e6FgwRPmI-1UXZqmvc0o7MZiVM2EnNNLA44iVR1qo2VceoHbe2XRy8NXE-P0y0lsusAR_hmqpu5Rn5u0zndELr6ScbLF6OfhQ5SHA7aLRVtzI7Bhv8AZ93n8_yzCPbp0HQkmpWoszV6msQRr9RJy9bo8YMN7APvngZ1A7YZRJAkGhSLoaIs_VgujQWqaW43g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
🇪🇬
سانتی‌آئونا: محمد صلاح ستاره‌مصری سابق تیم لیورپول برای‌عقدقراردادی یک‌ساله به ارزش 12 میلیون‌یورو بامدیران تیم بشیکتاش به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/27105" target="_blank">📅 19:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27104">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe05053c48.mp4?token=spbmxaiU1X2Ny2waH22WB-N1KTFNOa2ddzmhd5afZ_mjDkfb_7UAVB20OneEEf1lkV3e8n3z9BOXh7JxOgZmKIkBKavTbOgJ_iDwxmcjbBnnrjqQVEc49crFobwx3rYnI-rnpl-ImOpCkoMCxAwlrXgZqxqoK0IntxaqyqLYxc51UjwqPrjkjoBtBOCEDKdjGdcTxfpqZpl8-Ea7Mw1m5sDVrxmah9-vVbpweG2va8ftnOfo1HX4qYHI9NzOAtTpkFM_MW4yriX7h2LstPPCh8gkf9a2qFiLZmNXE9Ro-ge3_uMbH6_Lh_y9o4YDEuJud8pITSggOqAqfNECC4FJQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe05053c48.mp4?token=spbmxaiU1X2Ny2waH22WB-N1KTFNOa2ddzmhd5afZ_mjDkfb_7UAVB20OneEEf1lkV3e8n3z9BOXh7JxOgZmKIkBKavTbOgJ_iDwxmcjbBnnrjqQVEc49crFobwx3rYnI-rnpl-ImOpCkoMCxAwlrXgZqxqoK0IntxaqyqLYxc51UjwqPrjkjoBtBOCEDKdjGdcTxfpqZpl8-Ea7Mw1m5sDVrxmah9-vVbpweG2va8ftnOfo1HX4qYHI9NzOAtTpkFM_MW4yriX7h2LstPPCh8gkf9a2qFiLZmNXE9Ro-ge3_uMbH6_Lh_y9o4YDEuJud8pITSggOqAqfNECC4FJQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دخترِکپی برابر اصل نیمار جونیور!
ماوی، دختر سه‌ساله نیمار باشیطنت‌های بامزه‌اش وسط مصاحبه اجازه نداد پدرش‌راحت‌صحبت کند؛ همچنین حرکات شیرین و بازیگوشی‌های او دیشب بازتاب های زیادی در فضای مجازی داشت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/27104" target="_blank">📅 17:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27103">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/835360d02b.mp4?token=pJcMFkVMdxvQsv7jjRkpadJ_lm56GjR7qQIiuC1lD5Rw2AtgXTLvfqSPYRathAd54D3Lpw_y9YkH8dX1_UtHaRvy-YexkXvNHrcga6KJMDO4GVTEzL4464u4VNgeofO9raSG1dmkfP6R23DCTdMVKmFV1DHHwpucfTYjFTLMk4xZCBFlXekx_JuOKRRr9xICSEbHQKh0c3HzCUi0eQjpqUVGOGvpo8BUJiC9HZ--eQhbpw650MCuWUeAa3njvLGJXRSNEKMBsQN-ASPIR_W_xh4ME47xL6zMn7fFxZPN1XUCbK8XHNHfYxz26GTz1suFxF7t4WP8vRefPxct9EcBbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/835360d02b.mp4?token=pJcMFkVMdxvQsv7jjRkpadJ_lm56GjR7qQIiuC1lD5Rw2AtgXTLvfqSPYRathAd54D3Lpw_y9YkH8dX1_UtHaRvy-YexkXvNHrcga6KJMDO4GVTEzL4464u4VNgeofO9raSG1dmkfP6R23DCTdMVKmFV1DHHwpucfTYjFTLMk4xZCBFlXekx_JuOKRRr9xICSEbHQKh0c3HzCUi0eQjpqUVGOGvpo8BUJiC9HZ--eQhbpw650MCuWUeAa3njvLGJXRSNEKMBsQN-ASPIR_W_xh4ME47xL6zMn7fFxZPN1XUCbK8XHNHfYxz26GTz1suFxF7t4WP8vRefPxct9EcBbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بنظرم‌جذابتر از گزارشگران ماگزارش کرد در حد همین چندثانیه؛ گزارش فوق‌العاده گزارشگر زن لیگ MLS روی‌اولین‌گل‌لواندوفسکی برای شیکاگو فایر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/27103" target="_blank">📅 16:47 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27102">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ub71iKPswRgLY_pqQAnpWF1mflkhQfAMMTwaxcRGo2Ng5c5OUfApefUoJ8Kj5ymojBSskX9ufMRSGhTNRs4zM2XGCCoaIxiuS26aC1BgDYt7d4SSMLHcNMT72J_sye3JPROBZ9_8gU_5MpPoiL-5gHu5foc_WDiE56gaBw_6xNDpHZobpluluHvCLHtMFuYIKG_Kg1zdMXMNTfWarTxP-h9dH8bjl-ePOVU3zv6Hzrml_nunFTbTLcjNBs1ZQwnT_aXUVzyAhGSpDh0gn9TcVkDw_SKlPZoiRada1EkVwLKkDdXaiSTpOeKNktQgr7XA3VJplk79uvllVWnKCI2AbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
رتبه‌بندی با سابقه‌ترین سرمربیان حاضر در لیگ برتر انگلیس براساس‌تعدادروزهای‌حضور مداوم روی نیمکت باشگاه فعلی‌؛ میکل آرتتا با بیش از ۲۴۰۰ روز هدایت آرسنال، با فاصله‌ای چشمگیر در صدر جدول تکیه زده است. اونا امری در رتبه دوم قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/27102" target="_blank">📅 16:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27101">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40f136b3eb.mp4?token=tJMs9_a1C74XTqOA17GB10lRolWV-6sQaXzb6dgPSxnwzxHeLn7dtwToeE1zza4SC9_QRGRWkdu7hPcl5tvv3gKm2pt6rhKB6O90_WkYRo7JBedVvKY9n8fBFW1MmobDvj1VWjSoMAoHKR10x5DG5aCrmoJob24pbgHWPicweh8xPhiF8mldaTCLNq9_M6QazZJyBItI_7xINyK2HI3sIJYUzzJsvBvPmy_4aS2Brhj07VDByQamFC3ocJl1pOP_cFrMVzLj3JBba2rh3mXJEFPxYI7v6AVaD7x-07wygC371F6BKv4IDODWwxCaJH9Zj6uUYbGVYcEd-MtVMmDR-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40f136b3eb.mp4?token=tJMs9_a1C74XTqOA17GB10lRolWV-6sQaXzb6dgPSxnwzxHeLn7dtwToeE1zza4SC9_QRGRWkdu7hPcl5tvv3gKm2pt6rhKB6O90_WkYRo7JBedVvKY9n8fBFW1MmobDvj1VWjSoMAoHKR10x5DG5aCrmoJob24pbgHWPicweh8xPhiF8mldaTCLNq9_M6QazZJyBItI_7xINyK2HI3sIJYUzzJsvBvPmy_4aS2Brhj07VDByQamFC3ocJl1pOP_cFrMVzLj3JBba2rh3mXJEFPxYI7v6AVaD7x-07wygC371F6BKv4IDODWwxCaJH9Zj6uUYbGVYcEd-MtVMmDR-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدیو تو چند روز اخیر بیشتر از 12میلیون ویو خورده؛ رونالدو بفهمه تو ایران دارن باهاش چه تبلیغ‌هایی میسازن میاد از همه‌مون شکایت میکنه. طبق گفته رسانه های معتبر، کریستیانو رونالدو و جورجینا قراره بزودی بالاخره باهم ازدواج کنن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/27101" target="_blank">📅 15:44 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27100">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ntd67xHqISAR5W5dG0dF_bUYZBjbSpxtrsw6x2qduNwK2hgzj0Tqv4M7euBEHTRXQaV-rG6a99RjIHAQylbiani7fIGSqHgXI8ppN_EoaX4xmIrq_fluY9Sz-MH7B7_IewnkUP2FHIkB7URKePcMkkTiY54yvSOu8ZaKNlAID5kR0Vcsf_YPfWL-_-p85N46yjDW5NpdqMqCu-HFZyVc7t7w8XflhItvEe_XKUgobp6P5HewTvtZ7PyHZBR_OGk25ZmX7UjcUO7xXWa8qTY9Go4HoMMofecTWpGuzoPcReVwNiGCXzaFAL875fHALPY4KNCvoFiRMR2sgZ00Qgkmdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنایی که بهترین بودن ولی از تیم ملی شانس نداشتن و از داشتن یه تیم ملی خوب محروم بودن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/27100" target="_blank">📅 15:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27099">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">قیمت محصولات ایران خودرو و سایپا 13مرداد
🆔
@Persiana_Newss</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/27099" target="_blank">📅 15:39 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27098">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aTDN_x3QE3uP_JvF5TFkLLB_EDGieavdvxyAiiUNzkwZRYWXRHGjRpPOXXt_qLs8_IQ3zgky-brhVtANdzf-b8L7pPcB1oZGHxto3-QpDTlmIw5pSHrP69e7mVasqT1zi_ohujOJKubVXNvvNxvEgLgsYnb_MIzA8HEwxMZ-_prg4Ma2xxJR2Yhhn8-MEvXaISn1ljunE8Plg7RHv1rsLkzg6fK7ylENKqcLIyXx_HPAVzEq9pQcamPPv0suS1Qiwy53mjCkZbO_eNxPdxBOL6TMXcEH5v_W9rSYtfAt6trkCcNwI0Vtn8J4Ulyum160n7RhzKHS2JkpauHF5iwMuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کاپیتان‌ های پرسپولیس در فصل جدید:
حسین کنعانی زادگان، علی علیپور و اوستون اورونوف.
🔵
کاپیتان‌های‌استقلال‌درفصل‌جدید:
روزبه چشمی، صالح حردانی و امیر محمد رزاقی نیا. البته درصورت تمدید قرارداد رسمی رامین رضاییان با آبی‌ها، رامین کاپیتان دوم آبی‌پوشان در فصل جدید میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/27098" target="_blank">📅 15:24 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27097">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o3q5es5ZJXPzY9caEIVD3wd1NdShJci-46wmrakSzImGF2hLeVYNM7CuohQdGg8ZRr013ukL6yDFJvkFgrQOVoLRz6wp-ba5lGo5xpbIjJ6FeukO7GOCLw5sQcCYwiyxby2SY-y8biayJMUypirmSbzWUdFGoFhPvxbCvz80fsKa2icAh9wgQSDz5yARiefEXL_p2OEq2o6dHP6x3Ebrx5CxMCLO4nev4HIxI4q_ypw5OpGPpkPJJdqT9S3TAO0mnzC79yWxn7N--17Y_rZYc12V2wQSjhXMat_Fzn5iPYxQM7OlJw_OkJXfEVYFk5ecEuoeeHXwzl2U9-nwetPBYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟢
👤
عبدالله‌ویسی سرمربی‌ذوب‌آهن: دوست دارم کاری که‌سال 95 بااستقلال خوزستان کردم رو با ذوب‌آهن تکرارکنم. بسیارسخته‌امانشدنی نیست. امید عالیشاه مذاکراتی‌بامدیریت‌باشگاه‌داشت اما درجریان مذاکرات نیستم. امیدوارم که قرار داد منعقد بشه و این بازیکن با تجربه رو…</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/27097" target="_blank">📅 15:06 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27096">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/retUssdp_gfhy1ihfY55xqHPDRHRLzKuragYTz6un0tFHl38XQYOQq30ZqpDPzrqw19b79sv67Q9VgUn92AopM_3qfoRAzJDgMgGzeRUxtfk7bqhUPwVLHWmPMOqyZxmQFnGBNVHV27DdjbOCZwVyJ9F4FJUTyvL9rth2xNl2tk_cZ_mXxyP85fCPHPPlcvds4zX796obyFqZPaeosf8U5DPJGw-62eKV5thTGHRLb-XRmdD8RSGluQE3inAbi4BJ_oNHqIM-l2rEslYLyQfU5xHJ3a76GfaoAGLjKApcX4CuB8mOzqjujyJoU05wovyWRaFqkz_3MJ5h1ZKkbzIkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛مدیرعامل‌ تیم پرسپولیس امروز به حمیدرضا گرشاسبی مدیرعامل فولاد خوزستان اعلام کرده حاضر است برای خرید ابوالفضل رزاق پور 120 میلیاردتومان‌پرداخت کند. گرشاسبی به حدادی اعلام کرده تلاش خواهدکردکه مطهری رو راضی کنه تا این انتفال انجام بشه. مدیریت پرسپولیس…</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/27096" target="_blank">📅 14:43 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27095">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d39tCvmdr27z7WLjfXiQOkJGi8rrSlvAu-JmpU_in267MKkDSvnH9stfeOJN3g0ekJJrA5FSBzoOnZuP88U8Z5VG70IkUIvA-MCVxa0R7PTW630ta57ldh1g1mJRS7NkCyamAQP5VddPerTDPq375TVhZA94-cbYso1DqGQMRm2NVV8V8XPoLM5K-oJWWE8YpM4uT4eu_DGSgzNQdt72QIDVDIXr32nmTSGx-YudUDAWvhTakMko9tRnCx5enbmwcsBOXwpxJc8kIMME_AGckdsgKq5OVJJcs3scUiMjQyuZte4Nkecr69vWV68WrYvzMTlTwjYjB0hH3shCqzEnPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌_پرشیانا؛ آفر جدید استقلال به رامین رضاییان برای یک فصل حضور در این‌تیم 150 میلیاردتومان + 50 میلیاردتومان آپشن گل و پاس گل و قهرمانیه. رضاییان قراره ظرف 48 ساعت آینده پاسخ نهایی خود را به این آفر بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/27095" target="_blank">📅 14:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27094">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZYTRdXCs3BXfRJb1LPdWxP0KEliF41D-w_dOG95CjOIIymS-NgEpoOesPNa7PgN5PZaZgQ92pPv_VVRb5X_BXI7BK-KjPVQQsoFkkBFCHh-MJmS1GxUcdcQ6vPmr0-i5BvwAbCg1Aivn9sFVOJ83sf_nj2nLrQ6vrFI0v1IxD_oRqzKeSOC9Qr9c84PB4V5HF99wiPlJxYcG7QI3ewYJcUM7rRpHztU1CJN4HjAVyk46-xflrmxDVDFUxuHiFHEGY7bKYjsBiWZC5tnQ-LnIZ39jcEg4-0azeBZw3rMreWWA0uk1iVu3qpiMsfXXOJddrZwsBdgm_fK6yaXuLRVvWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
عملکرد نیمار جونیور فوق ستاره سابق بارسا و PSG در کل دوران حرفه ایش در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/27094" target="_blank">📅 13:43 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27093">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJvdcyCSPugtiPgFv6dr4N-G3hcs7QcHiyeoYlY5edVAcfvCI41c-G5jDLnaemM7fMJVHZ5iBBYl3iZV643wZ0i2O-4Epa3Vmb1d6HB69S5_l99O0810ZuyvSU2MXuI3DSC97dDFLL8oKxZp8mGgu9BED8iO-y3ZznuDau8sSypIdTdq-fRAclbzf1WNV55uueEwiJZmLnllJwPAXtGdO2enwwo0CYfm1ER6p3iF-pnrI26UGN_8JfeaTM0E94KrSPSjVQLR92eLPiVr2tnNKQ0YW2jYv1TnCbTEN-m8b9FgjXcHKV0wcDA-nwsH7SLrAPNc-oi6XAL3VAAwZYvA8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روز گذشته شایعاتی بود که فصل جدید رقابت های لیگ‌برتر یه‌هفته‌تعویق میخوره که سازمان لیگ تکذیب کرد. لیگ برتر 10 روز دیگه شروع میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/27093" target="_blank">📅 13:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27092">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fgc-Z9q_aOBXjeeBHJzmOKKhsLkP0WEB1VeDH7C_pWmOXZQwfjm-r9BPAcq6so5MrW7Aycbu_9pGvcNs82CfNFacUEIm2f9pQkopzTYydY_h7vFev9gyRdhyPtk070JCgdhX1z57vwvuMVluTE3tRno_mpKlkQX8ctn6PUYH2tja1zxgDj3ahbQy3EUsQ2ZYkoIR5nxCY3V85DyggXzJXAGIPofxTEzIgskfSUAsJwYjvyAMIolR4-GwmSV8LuYsM2WQwNePsPgxu_4LZPaDTtpwXOyvswB1GUthSKVmjbCMtchUDh7lkSh8Y05VaWmPBwoEdm5sOHZM98DuVFRBNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
استوری محمد جواد حسین نژاد ستاره ایرانی ماخاچ‌قلعه: پروردگارا بخواه برای من که مسیرهایی نروم که باقلبی‌زخمی‌بازگردم. کمکم کن جایی برم که دوست دارم اونجا باشم تا همیشه شکر گزارت باشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/27092" target="_blank">📅 13:12 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27091">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df9be54cc9.mp4?token=XrplykliL1HXjaLDUnCNlpIH_D2Eg5VZRMX-hiPakKmu9NEjLcTkGLR0EVfK7RCICswB-lPRP8iKYjhUj6Hk6CRDiTVqwvb0gdIFBb972eJFwTXhIBnlglXfke-krCpnmoqkqJ44J1zKMKj3_36i3CdbyRwVlD_iyMocOogtVMr4st2mgDclCNuWlg7cuCDeSLF35pG-557bc2atZE3rBbvh7iosZZEdYNVSAfp_oQD7V3S52mscKD_rOU75HikAobTcs6_vKHq-3hw4cCyE07kz4JphklFWrhcA69Zvh0RRtmjwzMK0AnGWTLwdA_Ji8mjzuG9t4HtlFTWQPInBwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df9be54cc9.mp4?token=XrplykliL1HXjaLDUnCNlpIH_D2Eg5VZRMX-hiPakKmu9NEjLcTkGLR0EVfK7RCICswB-lPRP8iKYjhUj6Hk6CRDiTVqwvb0gdIFBb972eJFwTXhIBnlglXfke-krCpnmoqkqJ44J1zKMKj3_36i3CdbyRwVlD_iyMocOogtVMr4st2mgDclCNuWlg7cuCDeSLF35pG-557bc2atZE3rBbvh7iosZZEdYNVSAfp_oQD7V3S52mscKD_rOU75HikAobTcs6_vKHq-3hw4cCyE07kz4JphklFWrhcA69Zvh0RRtmjwzMK0AnGWTLwdA_Ji8mjzuG9t4HtlFTWQPInBwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیویی‌جالب‌ببینید از نحو پنالتی زدن برخی از فوق ستاره های فوتبال دنیا و واکنش دروازه‌بانان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/27091" target="_blank">📅 12:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27090">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17e27275fb.mp4?token=cbIq-mxaHRHcedyn8yCBQHo5uwW5YnQdgnOyuqEvDMQ2J5p366t0ExVi-Sx2Gi7qrcmOULpiR83eMVwBAvDPJJ9Fm9vJJWX7YE_ZJEEJkwRR6qAK13iVi_-v4k1cFSivHX63WpEXdyqSZUrOprUpU3o2NkLRRiq-E4L9KmNKbVmohXxz-kttWufLhtVrbGQmmrC5vcJ0Y8Qwk0F7n4wfl74HFE4SXl-5YOvjeH2izDA1Az1b5xho8KaWBreefM0GKOGA6-wekPfYSftRf_fUeKaetlHxUoJmb-8sekl7_Vq1rE1mbBZnkm37i3aWl1bhHqDyS3r9TMKrAMmzGK9zFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17e27275fb.mp4?token=cbIq-mxaHRHcedyn8yCBQHo5uwW5YnQdgnOyuqEvDMQ2J5p366t0ExVi-Sx2Gi7qrcmOULpiR83eMVwBAvDPJJ9Fm9vJJWX7YE_ZJEEJkwRR6qAK13iVi_-v4k1cFSivHX63WpEXdyqSZUrOprUpU3o2NkLRRiq-E4L9KmNKbVmohXxz-kttWufLhtVrbGQmmrC5vcJ0Y8Qwk0F7n4wfl74HFE4SXl-5YOvjeH2izDA1Az1b5xho8KaWBreefM0GKOGA6-wekPfYSftRf_fUeKaetlHxUoJmb-8sekl7_Vq1rE1mbBZnkm37i3aWl1bhHqDyS3r9TMKrAMmzGK9zFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بااعلام رسانه‌های افریقایی؛ پیتسو موسیمانه در آستانه عقدقراردادی چهارساله با تیم ملی آفریقاست.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/27090" target="_blank">📅 12:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27089">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/370ff98a06.mp4?token=CwGjIp9Imw5JEBWb2nViqiJkAzYOz6AFOWMAcLIrbsQwKIze5UFGhtymwKipVDtCrHV3cxsRRz0Agj3077gFmzqzjfHLzQCfjwnb3Izxtzt_bSH2uOH2UHC5RAeTY9LAhkRyZ2gKPjsvyoEnRb3JgbbyiMjwauUhn4YVguezaCGut6Xx8mQHAJ_i8KHWl-ppwDuxw7YCUDdJl4AO9dois9dwRNZlShkhySSswjONR6i1CTIoc8eeHms5IZcb85dvaJZc24aZr5otfyjU4lH3ElARJi__OcKFvIK16GfA2RAdBVGb_j3nSzO9VxrVTuva-f4vVJ0OuMv1OPMW7DeI-ndWL0x6t5fuhsDOdgVWHuv1SPu4wKVe3yKiVgl1JFuhHjSNdiLD5AJiDYekRZqA7QaIf5Y6Mk1y3dQjI_zo90IQ7BCKkL8RA1ZU43iwLiHuOkX6MNBq6G6gXhDnXcHxg3oPPFgBbx1rzoKkuWiU040EJZk-l_j6zSMfbaAIdRyaIfHAqhW6jt3pejFBagLluDJTH3yersQ7ewlR2z9W8DI91B8wMmgeSd_PlgGPekhEW4vbs47vG1FG1z1YjI0BYr2Gn5tspJume8cOJIzWyUdlHrReYfRzEp-p-jZuovxXELxPRywl46z7feqPvBzzkq7pLSMYdvNkmjVlSRvPN1s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/370ff98a06.mp4?token=CwGjIp9Imw5JEBWb2nViqiJkAzYOz6AFOWMAcLIrbsQwKIze5UFGhtymwKipVDtCrHV3cxsRRz0Agj3077gFmzqzjfHLzQCfjwnb3Izxtzt_bSH2uOH2UHC5RAeTY9LAhkRyZ2gKPjsvyoEnRb3JgbbyiMjwauUhn4YVguezaCGut6Xx8mQHAJ_i8KHWl-ppwDuxw7YCUDdJl4AO9dois9dwRNZlShkhySSswjONR6i1CTIoc8eeHms5IZcb85dvaJZc24aZr5otfyjU4lH3ElARJi__OcKFvIK16GfA2RAdBVGb_j3nSzO9VxrVTuva-f4vVJ0OuMv1OPMW7DeI-ndWL0x6t5fuhsDOdgVWHuv1SPu4wKVe3yKiVgl1JFuhHjSNdiLD5AJiDYekRZqA7QaIf5Y6Mk1y3dQjI_zo90IQ7BCKkL8RA1ZU43iwLiHuOkX6MNBq6G6gXhDnXcHxg3oPPFgBbx1rzoKkuWiU040EJZk-l_j6zSMfbaAIdRyaIfHAqhW6jt3pejFBagLluDJTH3yersQ7ewlR2z9W8DI91B8wMmgeSd_PlgGPekhEW4vbs47vG1FG1z1YjI0BYr2Gn5tspJume8cOJIzWyUdlHrReYfRzEp-p-jZuovxXELxPRywl46z7feqPvBzzkq7pLSMYdvNkmjVlSRvPN1s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری؛ رافائل لیائو ستاره‌پرتغالی سابق آث میلان در آستانه عقدقرارداد چهار با باشگاه منچستر یونایتد قرار داره و توافقات درحال نهایی شدنست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/27089" target="_blank">📅 12:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27088">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKA5Nx577lVIQpa1BqEE68BCWiSYC6cbIs6lUA0Y4jM05x2hDAr3VIHpvFFY5W-AXc2CBi3l-bsCYrPKA04F8uc_8zkxwRtwfjszX4p3fYnQl67aslEmyUet1_R0zl0C_GMbB6CfugYkEcK0-UXP3WDLaTn64QVA74OtusYwp5ez0OrJ0mDIY325GCzQXl6aYnsRUt9NNCaawVo0_3h59Kb9i7iZ2s7-c68TGPwFjNym7eRHmhonMk5dUPx6gPHKwhVYUT5WyWo2fsaEfxAARY4OEUq5dfPkx2zqhrLRxyziuIXM2qZeqqAIg7wbu8gOcTpkoAJZZJnnTHCwgGisUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پیشبینی در سایت بین المللی ریتزوبت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⚡️
فرآیند ثبت نام ساده و آسان
⚡️
آپشن های متنوع با ضریب بالا
⚡️
امکان شارژ حساب با کارت بانکی
⚡️
شرطبندی بدون لیمیت روزانه
♠️
کازینو آنلاین شبانه روزی
⚡️
پشتیبانی از 61 زبان
🎰
بونوس 100% اولین واریز
⚽️
بونوس 100% ورزشی یکشنبه ها
📲
اپلیکیشن موبایل برای اندروید
🌐
http://ejh7qy8d.lol/L?tag=d_4828009m_69797c_&site=4828009&ad=69797
🌍
ریتزوبت؛ همراه همیشگی شما
⚡️
@Ritzobets_official</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/27088" target="_blank">📅 12:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27087">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cFGPBChoz1tQC4CJ5fGzY0Ax0FnCLMU9zr2OAZA1rM6vjNzc3H1YZvhlrw_ncEFANfnoEYL5R_yuvFak66ekPrU30GkAZqh5XtL8z58-8s63k50-R6JSNZzZeZF5WJp1CDWve55BV6pln5daMO3-C5VtvdJX32jo5fhCaQkB2NAKXBUwYIenhHCfydsNOXJjAFcztZnL1mGzEB-nknqLrrGf-VIOW8ViSySSQJ2SESmfrDGfrT2A8PSaAAWhDNrDZXDhinRp65dFbD7ZJ3gOscIMp8FfMsJeymOa0300cyXUOQvZsCpmuqOdO8Oe-ab1xPYSlY1Hc9rXk8K6xdR70w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اینکه‌گفته‌میشه؛ باشگاه ماخاچ‌قلعه رقم رضایت نامه محمدجواد حسین‌نژاد رو 4 میلیون دلار تعیین کرده کذب محضه. بار ها این باشگاه به مدیر برنامه این ستاره اعلام کرده هر تیم ایرانی دو میلیون دلار پرداخت کند و خودِ حسین نژاد هم راضی باشد این انتقال انجام خواهد…</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/27087" target="_blank">📅 12:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27086">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7kInltQnZitUpPE3rBlOE0CHQQ2mL-DguptyD7ePWVRXIj2TN6fUc8wZZpIDHJaHcuTggICeAcCq5WswGHXghokJpfr4yEBm-mb43osMRTeGpMDicj1G55W_zJpr_vm4xS2Jemx---8ENobTJhh2saxCOd8yPGYUey0f3qd_ByYKD0AVypujkjmUhVdXcPbUteqTLtEoEla3rQy3iZWd403XzB6zFWDw1hWkPDo5G_EcodHyEfhlVvHfc-IcrDid8TnAR1zKLPKhybno0X3M5H21vzjBaaTO6k5Gx6m7hz8iAOLANtfRW7cb4SwApyh7H7l6WvkPTD_YtDtAZqQmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
رودری ستاره اسپانیایی 30 ساله باشگاه منچسترسیتی:من‌تمام‌پیشنهاداتم‌از تیم‌های بارسلونا، پاریسن‌ژرمن و منچسترسیتی ردکرده‌ام و تنها هدفم دراین‌تابستون پیوستن به باشگاه رئال‌مادرید است و مطمئن هستم که این انتقال‌بزودی انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/27086" target="_blank">📅 11:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27085">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vz_h5oWkQoJei4d8EFySMhfiRRYiNhFfbtwVoKCLOFu1cETFLQlWynW1MX5SFL1RuoPqNHx4nN5UTrV3tsR2Yd-Lt0VHNjRhu-59LFdQmty8FizZPsVT3ruGDCyAFFxLTmk_dRMGUP1sSLr90fpHxgWB5jRZy5yL8v1AvA2lHd0YSlEuxJbYGi_JbMSvjj_UdU1YuJHLp3cbWVZW7xS9t3J2MH0yH8i3fYu6s-Ga3TKMCcHM9FQp9zOWmhnqHv_TDdaOGo4VXQ09ot_NeUWBBQi8BBi9zgvcwBxDIVWtKaW_Jb0VWGVneip5r5mxlB9RSabgT2L4fhBncnLEhCtxvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
ویدیویی یک دقیقه‌ای از سوپرسیوهای تماشایی مارک آندره‌ ترشتگن در دوران حضورش در بارسلونا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/27085" target="_blank">📅 11:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27084">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kjerXJSK2j6_mZJaTJICVMs4NWIWT2WeuHl2aP5Uy4oJ22Kq-0Xr555cjbKhZ7S1ejl01WvpOCAWefFxNwTS4JuP3cv0u-I39i8g8mhZwGrw4REC5cu-SkWzmBZHu3rRE6Bi7FFwHzCyBPCJ9GxndZyr6jG5Wuk-ZQU6uhezjpcuxz9TRKhxNuNT6y5ZlOy0FV1HMSUai7eWss6vNPtKpEJaOZJzUQNXBvUKP5zj0AQ4l5aaY-YBHtSkLjw5rluN6cjQH43ToWTZp5kSJ_gUGUOvtevQBXy1mg5v4uz0fFqUMvUTBZVWIAuzxYfiWVoGgmMeQf0wDjb_ryJ5KdURNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دو گزینه نهایی تیم‌پرسپولیس برای جانشینی میلاد محمدی؛ اولویت مهدی تاتار مدافع جوان گل گهری‌ها شد.
🔴
باشگاه پرسپولیس بعد از توافق شخصی با امیر جعفری مدافع چپ 25 ساله گل گهر سیرجان؛ امروز صبح با ارسال نامه‌ ای به این باشگاه خواستار…</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/27084" target="_blank">📅 10:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27083">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/222ef9e7d6.mp4?token=fnuhmhj_aiPpibHors_6D4Aj7oIZIHaLuzVA4HvqqvXDYG2SbA4ib_Oeptwspu68NYT2sK73-GOzMkkNlzawajvgE6-dpMENRB0W8Dq5cnGfQjYUZBDDM-q0QoHxhEO8BknXE0DNBWvrHfqiUU4DXO84BpJ1vkTBT7KQh43V23j2uONiPCFD6irKqTQ1SLWVOZprTEbK6bRyL6vdbwbgju_nQ2mPd9Ke1euWjruLNVFD4XdTffHrwxdav1BsgNAc0bcu5mro-gvwsY6X602g8W9fuXkbhwO6nrQem1_lHEZrjl1bF5jY87tBSAODsnTXBG1VdZQRZ8aOxxh2CMPf8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/222ef9e7d6.mp4?token=fnuhmhj_aiPpibHors_6D4Aj7oIZIHaLuzVA4HvqqvXDYG2SbA4ib_Oeptwspu68NYT2sK73-GOzMkkNlzawajvgE6-dpMENRB0W8Dq5cnGfQjYUZBDDM-q0QoHxhEO8BknXE0DNBWvrHfqiUU4DXO84BpJ1vkTBT7KQh43V23j2uONiPCFD6irKqTQ1SLWVOZprTEbK6bRyL6vdbwbgju_nQ2mPd9Ke1euWjruLNVFD4XdTffHrwxdav1BsgNAc0bcu5mro-gvwsY6X602g8W9fuXkbhwO6nrQem1_lHEZrjl1bF5jY87tBSAODsnTXBG1VdZQRZ8aOxxh2CMPf8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هونگ‌میونگ‌بو سرمربی‌کره‌جنوبی درجام جهانی ۲۰۲۶ مجبور شد دربرابرمجلس ملی کره حاضر شود! او توسط نمایندگان مجلس کره جنوبی درباره تک‌تک تصمیمات تاکتیکی‌ اش بازخواست شد. از تعویض‌‌ها و دعوت بازیکنان گرفته تا ترکیب اصلی تیم و سایر تصمیمات فنی اش، همه‌چیز زیر ذره‌بین پارلمان قرار گرفت. هونگ در ابتدای جلسه هم از تمام مردم کره عذرخواهی کرد و مسئولیت نتایج را برعهده گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/27083" target="_blank">📅 10:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27082">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCRmZe_LKHdUMGPvHHGqUzauQukFYdY49Nkv043SzQg4LWtQnAHi7pHG_2wN-0ubHLAX5hAImZTOO1-yd0_yUxJNU-FdHQMzbHpEkG6Ha4YvtFmLDl7s2W5UMy4_ATB97nFZznpymnshPUljEymbFDXOgkFXoppaxJkUScqGysItSFSyDWPW8USI-Su6Td9IT-KfovvpMVKTPu4KvHYo3h9iUNXQcQLVYhzLuYgWDW-FnVRixrpaEfFIQVBOJTveMKIuZ11xJqB1brAMhsHEnowrPfT-QkScdJqnBJigMiBI2Bedp3Uej8z_Rc3TpUUilTbGUhaJZbu4k0dY9ekIZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
نشریه‌مارکا: انتقال رودری و یان دیومانده به باشگاه رئال مادرید نهایی شده است. بعد از رونمایی از این دو بازیکن پرز پیگیر باستونی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/27082" target="_blank">📅 10:23 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27080">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0hub9yQ0YJ1yJvtR6-Z9KiAza10A6iNcbxDW0XcADwNbgwe3YAb5eZncnI1ZPiSDWP8w-hUtjY6AZ_I4uyNAYqcGg5QwHjVxeBVCdYNbqkqO9npGnl_O3OlVW3ZpoL8iuYkEwWFk2VzGO7XmaqQ9cyZYnALSsR9cxo-GM5HCXwY2MCyJtdzH30ilNhnA9yWtHGATT-rUddcdrvf5P6FkxDTmhgFYNArePav7PUaRSRpWY1S9i4KhI5TAL3V5E1rxYX2NGw4-GqSENnAk-U0G2TZWZW250sP9t8C0wJlTJsZgv1WvbmHmbsSCEiTy1uiKpx2Wa3tCBT-iH3EQJmXXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جایگاه‌جهانی تیم‌های ایرانی در رتبه بندی قدرت اپتا؛ تراکتور تبریز درصدرتیم‌های ایرانی قرار گرفت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/27080" target="_blank">📅 10:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27079">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DXpgzN3Y3cG06A4c0q8AR0REf301MDFh1YJeymoMv9dqTgin7wtA4g542-Vqlzx5v2r2JkxVlzYC5KnbH8VVT6wnrFQxgsC6u63fj4DD6XBppj30OFdNcofdAJbCCJEu6TLxiZI81M-S2AmVasbw-jJW5gIk_vmZzYqJfkyki76OlhyiDxj79zptKqGqbW7tuAjUuQxucQQtnjcHlqWHQ4KdgAhwAfhFvHvlfz7KLroxpaOq7tjU2_UHvXEfkTnzV0MHqa07KGUzrUWmUv27B1EVGcwqpt5s9SuXyVTPuer63_kbWxPqJX5_sLeVIH3hH1R-JC3mxZPOHDUYG_rd_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
طبق اخبار دریافتی رسانه پرشیانا؛
سعید واسعی هافبک تهاجمی‌سابق تراکتور و مس برای عقد قراردادی دو ساله با سپاهان با مدیریت این باشگاه به توافق رسیده‌است و بزودی باحضور در دفتر مدیریت قراردادش رو امضا خواهدکرد و رونمایی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/persiana_Soccer/27079" target="_blank">📅 01:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27077">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hLjgwdgTc6hqhBdTjGFqaNREo0k5uwLcw430sO2yoob3z-dz6A_qh8175IiorAqCS0ZLFJSGZvP7NQefYsi4BQpWYZ4-LT5Xi2j4UhR_-oBj-SSsocnQhbZPDMcN14lQSYutjx6wlKr_A0P0_8PrxACLk5RmT88MBiBI2ZtRBDYyPWCjLKThL5Yy6UACoDQ20LnSrjgLgs3U0iz7UdVZd6CCaIoYLmgdlyYhdlhvOYMDllKDKeDdX88nX6N9GjYmwJnJfe05sMcpLyuG9NAw6Lnse08BL9DUjo93l52dP-MV11Kuiu7es-tkx_hxvkrBKYrRR5TIzuLwyapBoHPUHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌ امروز؛
مصاف تدارکاتی و راحت باواریایی‌ها با تیم میانه‌جدولی کی‌لیگ کره‌جنوبی
🔘
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/persiana_Soccer/27077" target="_blank">📅 00:58 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27076">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hI6Na56tW-jOn7jl1Z_heFEhwrRJU4-bC_GcLje5pYVEgv4cEqNXFxLw5QAFhba2h0ur7cC9MtbPFp5_z35hWn1R1ZujglHqowUfwHW9CMeW5hJzCs0n-iG8DrhT8hrZw8UrG94Hd007JZUnnrgR8zy84SEYTItTm7G-xZRaghzPKqkddcG1f8N8G9t7B7Nzy3cdokQaCxwz0DO4fUjvj1y3ZQr1D9yNNu1OMeTrZd5vLPKSED25mtiDuV2ruHwBHENbtt7IvloavUD53_OxkduoHUiANueIPPCVlh_j5FNmJZZh1M3pdqnbKiwWOCdYxiBoltLzyy_xgRUw6koY8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
روایتی‌جالب‌از آیمن حسین ستاره تیم ملی عراق و زننده دومین گل تاریخ عراق درجام جهانی: در سن 12 سالگی یتیم شد و پدرش رو از دست داد. بعدش داعشی‌ها داداش دو دزدیدن و هنوز هم پیدا نشده. بعد بخاطر جنگ آواره شد و یه‌مدت هم بخاطر اینکه مخارج خانوادشو قید فوتبال…</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/persiana_Soccer/27076" target="_blank">📅 00:47 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27075">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mREO0kSN2ovoaxJqC4YZvoj_nJvLgGfKs6V_TrrVLXjOlaUMKh0rDhqfEwGU2C6gh6wQy00n7HpX7p05WYlDb6zpHEC5OXpksa6etXpYkATd68uVwhdMtMdPWxHBchWleIWB8CZ-OLhLNfeXAo1sC1QKU4YroB7lOmPbczZ6Jk9YvpruH3cNQsKBLeR6aHX5jlWctPIhwUsaa93BYjN2XsBvqEit94d3LlrjmUVMpYQrUvd1sBIqLV9_iXod8n5-6yAC5JfxDs2Zk6ktK4m77-Is432oPh_qQA4kR1R2xyk8yNWLQsvaAPzhwtSPQTDS_vtqYLtpzt1NYJ3pc-jQGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
محمد قربانی میگه‌الگوی من از بچگی تا حالا کریم باقری بوده. حسین‌نژادمیگه‌من از بچگی طرفدار مجتبی جباری و فرهادمجیدی بودم. خودشون با زبان خودشون دارند میگن که دقیقا فن کدوم تیم بودیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/persiana_Soccer/27075" target="_blank">📅 00:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27074">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPqpoTI_5z63JolSUxtZwW_BCuvOIGKRo-p8jSJu0TfQyjoNc6BXV-DS24qWqf-DvZeXrmVh8jJUJseVp9_Il0VqSoov2M71kp7DzxMPZyoVha7s3_bXPz6-tz-nPWhqZUH2OqKvfH_Fk3q9SJHwS73m8vsxnOSIWUjBbmhXcwxt7tYv7JynAtM95wnjisFp4CY15SCENkBWklnylJZkv18bkGeNb1XR7v8U481dWWCBf_3WXVcEl3rvK6WPeXba3pKxHWeLo19jRvmDld7-JLQJgeGOuA0EMDZGHL2rphWjSG8DFA0F6r6uLxPHaWpcWh-mHcyC3eBmbH4Y5SGBaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری؛ آلوارو آربلوا سرمربی‌جوان فصل گذشته رئال مادرید با عقدقراردادی سه ساله بعنوان سرمربی جدید فولام انتخاب شد و در فصل جدید لیگ جزیره شاهد تقابل جذب او و ژابی الونسو خواهیم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/persiana_Soccer/27074" target="_blank">📅 23:56 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27073">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N8BF_W24KbIi26CLAswoww03XtqNl5Z6ajsHy0ePBD9i-WnGB8xKmONYeoFwHraMWxrPZdhxQfSwspUS83nEQSiPzXyowZ-9LQtd9sNlG88a8pJt7meuz1oH-UMW47L1OuwYWXChxI1DneDf-Vv-GbiOcoRqZizO-nFPHGPYTLe5QrUsEdJBr74BgPkT_xBwIDt9X-pYrE91q1Z2C7bFZCMxBnjd6wkhiL5iz5Pks-UTNcSxalS5Un3UHFmZRUYyAqpfRGV67IN0I5QJut0NzVGMj9XAy1_Q8-FIUsSfZN3ytAsQLFxHGM_5xKGbuDQV1Hdfiq06u65qgvgYkRKvOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
دادگاه‌عالی‌ورزش "CAS" روز سه‌شنبه پیش رورای نهایی‌خود را درخصوص‌پنجره نقل و انتقالاتی باشگاه استقلال خواهد داد. اگر رای مثبت باشد فیفا پنجره رو بازمیکنه. اگرهم رای منفی باشد این پنجره نیزبسته خواهد ماند و با شروع نقل و انتقالات نیم فصل پنجره آبی‌ها توسط…</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/persiana_Soccer/27073" target="_blank">📅 23:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27072">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szZoBX0M02-UboudNUPwXCoeWcQPiAwZGXPnActfrd026Z2G54lS2qGDL7-BRqr0IOv0Mx9q4jJasApIbY54cLBvRqFwtGCI0P_H67XJkkWiG026qJGJaDvR2IWZjA7euDNx5_xrHpbOxuXC7uDPwu5gXPFPzH0dCmvQuPAyaQqydLbHG2E1M6iwc8WwLmbamoNG56Whe6HrI1nqhxiQbev-pmyl2CeCAXgZXtz5ZORdd0Orr40E8z6PJp553kfzL_dsrCQCODC1gycxbThrjncmSJgOZpFrKzsa9Mceq6iZc0keqmG5XJ7zili7xSZ4K9cr18nIQXjj_FVu9CY0HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇪🇸
اسکای‌اسپورت:الساندرو باستونی مدافع 27 ساله تیم ملی ایتالیا درخواست جدایی از اینترمیلان داده و به مدیریت افعی‌ها اعلام کرده با جدایی او و پیوستنش به رئال مادرید دراین‌پنجره موافقت کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/persiana_Soccer/27072" target="_blank">📅 23:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27071">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FDj6r0CCzr0rPJSYaKg9OmN7kY1ej5WdOUpVVRAgT37DJRKVSgiXtRN0xqFmQgrTKrNa7pKMrgt3erLSiTpO_KHaq5t80_KAkvXYT1axU1rQieqMqFROBKjWGBR9T1Hg2QzWVkj-5izPFveUUQBxILU1I9Gfy5OdXkYUNfTn8lTEXOrde3Uczice9ODHPappsUHIcGG5CMMv-RnjD9ZKf2pV-6t2WsDFq_xGRvG_kcZzDfkEgtFLUbQzyrVndOhCNkqhwhGMKgEE9YWXC2hQnuvMixA_agUDOn5Gy0JUq9jrLOcRnCHpfjGJ5p_0d9IRcYe_SbFd910KTKjW2FsouA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌پرشیانا؛مدیر ورزشی ماخاچ‌قلعه به‌مدیربرنامه‌های محمد جواد حسین نژاد اعلام کرده که تصمیم این باشگاه برای فروش حسین نژاد قطعیه. هر باشگاهی دومیلیون‌یورو بدهد و خودِ حسین نژاد هم راضی باشه این انتقال انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/27071" target="_blank">📅 22:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27070">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/US5UXCbdPa7G-fiYPThNytNUB4DfGAM1Y9Gz5EwBNT9leeuIK3iJNeLWf4aP15IqYPexrjaeobyffA87h3-VdckY3dh-A_MrlaJ6T0n4vcZiBmVojnSPWN6v5-2QGPdRTtlh62SU4OPh8QV7XKC8nc59xcnMyR6FzdJGwfhtrKwL_GO95Kt_wLFe3WdJ3X4UPwa7SsOXYjWBkqdYJReLOSD0YiG8mT8YEfdd5tjZrn1f8wtAYFK3TfAMMD1kPiR33K0xDJMuXEw3DhLUQq-Ep2xx16SFge2fOLKax7DGE4XHAPGLVxIcO4YD0p5vI13Z2Q-3e0ZkEYAAp-a5UAgQ8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فوری؛ دونالد ترامپ: این آخرین فرصت ایران برای امضای یک توافقنامه خوب است. امروز یا فردا می‌فهمید که چی میگذره. قراره به زودی و به یشکل دیگه، مذاکرات پیش بره. کار خییییلی پیچیده‌ای هم نیست. قراره فرداتنگه هرمز رو کامل باز کنیم. بعدش هم در مورد ظرفیت هسته‌ای…</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/27070" target="_blank">📅 22:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27069">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QeZfVjE3fvKWTj--mYPu5qvQuR_vCRhdUGvJoTq0Zg66LC4HX-9mQ_NRp277CtjUYdi8c2Bsqf47Yw2YGOFrw0UN0EHqQuXBbpUMupA6ofRnKS-PX2E585POmtMZorGDZTeMRlMndLSAl_3Mm70LaU7HBCrFjOixg-uMZZ7cHegU3pu5HDGj-BaH_Iy3PUFuv7bmWfhiNhIYELbJhmGUvFXwgaBCD_e24X3FV2GndtBI-NHFArmryFtG00PQVyrk2d6wXezWewr5-BFv-0zCKp0hLyK8PRWmw-Triqi32IWfJkboOYk64Eh_yDrnmvLycmXTI9r2wJ-f0ODqpb4oLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
نام مهدی طارمی کاپیتان تیم ملی از لیست اروپایی المپیاکوس یونان خارج شد تا این بازیکن در آستانه جدایی از این تیم یونانی قرار گرفته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/27069" target="_blank">📅 21:38 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27068">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e97c6b80b0.mp4?token=AxZmd6ikRPE1A2-h8c7EhkqE9R1hQhoT-dSBt3qiWc7YbycofIawbSx3kv_5C7c9Pj59mLhhtMSKBpNMIvPqmGCFyAy6lpjCQVvj8qNk95hCDld-amZLsc8SNqgCf1lfJQc781ni23juSKGVs8BHIffM2B57xqtqfsanmWhHggJOetXw7TinGwpxJLuQVf0Xexq2CtqsqhMG0Q4rOOFDCConLoPxCQEqKZqzCrU5-GaYBNeYFaT3ZtDxgREbPAmT6rbsVQ3NBRtugPZG_e9grp1uVLiyrdIKTkEPvMo9J_vD56kmFd0oTLTI7u8XgIyf_DpaOOVSUgYm1EhXO4aH9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e97c6b80b0.mp4?token=AxZmd6ikRPE1A2-h8c7EhkqE9R1hQhoT-dSBt3qiWc7YbycofIawbSx3kv_5C7c9Pj59mLhhtMSKBpNMIvPqmGCFyAy6lpjCQVvj8qNk95hCDld-amZLsc8SNqgCf1lfJQc781ni23juSKGVs8BHIffM2B57xqtqfsanmWhHggJOetXw7TinGwpxJLuQVf0Xexq2CtqsqhMG0Q4rOOFDCConLoPxCQEqKZqzCrU5-GaYBNeYFaT3ZtDxgREbPAmT6rbsVQ3NBRtugPZG_e9grp1uVLiyrdIKTkEPvMo9J_vD56kmFd0oTLTI7u8XgIyf_DpaOOVSUgYm1EhXO4aH9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
فصل آینده تو بارسلونا میمونی؟ فران تورِس:
‏من‌قراردادی با بارسلونا دارم، اما در فوتبال نمیتوان پیش‌بینی‌کرد چه‌اتفاقی دقیقا خواهد افتاد. من هم فقط منتظر هستم تا تصمیم درستی بگیرم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/27068" target="_blank">📅 21:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27067">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d787366ec9.mp4?token=sOhWdqyJy2wQodtMvHLh1K-Z7LpEQKGYM5arK7-c6tpUAjH--QRCJgJNfuEhrs86L2l53LcHbuUMFmwI64PqlBVDkFPt4C0c6QUO2k6_9jYsVowDt2T14qq0YiltwXHDrE3y_KcWhYkv-hEG1QTLzNGNXvCiuafiDIKrZofuoSD3vFQ0rgfz5eOlpaQkFkrs7W7Fy4DFGOFINc7j0QQLVkNznnN4iXQfC4FuF_zpzdjzk3cVaqfnP2l-XFlAnGSyM11nvZdHjV1jJgyKPMxYb72toExgzQdu8Tl9CXIwv2jIafiGyVVzESS1kYEGhONEUHyPGsO8N7rVMROiWB3q7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d787366ec9.mp4?token=sOhWdqyJy2wQodtMvHLh1K-Z7LpEQKGYM5arK7-c6tpUAjH--QRCJgJNfuEhrs86L2l53LcHbuUMFmwI64PqlBVDkFPt4C0c6QUO2k6_9jYsVowDt2T14qq0YiltwXHDrE3y_KcWhYkv-hEG1QTLzNGNXvCiuafiDIKrZofuoSD3vFQ0rgfz5eOlpaQkFkrs7W7Fy4DFGOFINc7j0QQLVkNznnN4iXQfC4FuF_zpzdjzk3cVaqfnP2l-XFlAnGSyM11nvZdHjV1jJgyKPMxYb72toExgzQdu8Tl9CXIwv2jIafiGyVVzESS1kYEGhONEUHyPGsO8N7rVMROiWB3q7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
دلیل ازدواج کریستیانو مشخص‌شد! حتی قیچی‌ برگردون تماشایی به یووه هم‌به‌پای جورجینا نرسید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/27067" target="_blank">📅 20:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27066">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cObgWUvlnbK-WWkoUBk8SSOSJ_T7cKetvdyuu68x-IvCMEppIae69TJma_dC3fzrQNwRr7a2HVR9dC2kujw9AGZubQSV4hafvnwgIOqS_cvfNDGugAc2-DyX4SL16uvA_3Rl1PTOTkjZ32HcQoRzsP_GSAP2tD-chc6gbWVcguEh7KIbksDc4_Sl2qzQzpy6iUWakSh9mVKmntw53Vwj-FtUdoIHrlYgvh7W8DlyZjQuS-osK3RFnQV7X8h0mJpACy6l_bTCtNgPCdCK44sNHV_eCMeC6Y2WkdiplJlOsGRHG8TFBVhUUdO-RKHR7wAzBmxJ9ezAcaH6oMxxPL_AbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🟡
طبق شنیده‌ های رسانه پرشیانا؛
یاسین جرجانی مدافع‌میانی22ساله‌سابق آلومینیوم اراک که فصل‌درخشانی دراین‌تیم داشت با نساجی مازندران و سپاهان اصفهان مذاکراتی داشته و بزودی راهی یکی از این دو تیم خواهد شد. شانس نساجی بیشتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/27066" target="_blank">📅 20:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27065">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xe-rrW1N6MgiZ-pck2a_zr_c5uidxc6BAUczC5302JQ07xA_T6Cl0PJ1Ymc0kW6bGMGUWgpX64Mn59wUJLdcbHin1MmBBH-YETflvlF2YoGu5boJiUA2hj9JJxOfFFnhxYNCu0MknuqwWqc93y0wH5BsTd3Bed-DgHRlyetJ-LnlHscPIuhFewPzdP3xcTrbaTs8Tq8YGhnCTgUbsnqeZF0VuIJn6N-xDEPhFdzuAwIyIbqzOrRuO8s7MsSc9Il-c7ZtjWimnOjPlbZHaQ-1snnAzO23sLeuqp-LHxOSiXih7nJsYEVsv2E5R5kbogbHTcOZ40pZeDbF6krXAUKWOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
👤
طبق‌اخباردریافتی‌پرشیانا؛بعداز عدم توافق با مدیران سپاهان و فولاد؛ امید عالیشاه عصر امروز با مدیران باشگاه ذوب اهن جلسه داشت و برای عقد قراردادی دو ساله با گاندوها به توافق نهایی رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/27065" target="_blank">📅 20:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27064">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QAoSeJiSjLyVOqyxrlfWaE926WRkFi1LuOK76cCL99Nb5UIoqxUmn3-AtGsaBPmpwWtVL39FYyZjLA9ZISAQ2dDVxwPOjInA_s8LsuiLQHcrAcJF2Tu4Wg8xIrhLqhlF76yvvhdL2kCNpw8w2dDe8F7drqOVo-cbeUIPtBHQKKeXp0-S2cST2pT23afcZS0L5okSQcySMU4sM7AmpwsoPI2pgd_eDl18lHDBr8QjZ3wnCcwnLh3wx3VHVMwUaW6LbVNWi7U-lDdPIYWe-CU_eNro4yUdo3r6Xp4qm6Pm_azMTRkAWurs9Y8F2F7y5yOH-izLrnhdjpcsLrDsKWsYFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔴
تایید خبر اختصاصی‌پرشیانا بعنوان اولین رسانه؛ اولیه هدیه ارزشمند سعادتی به زنوزی؛ هادی حبیبی نژاد ستاره فصل گذشته چادرملو با عقد قرار دادی 2 ساله‌رسما به باشگاه تراکتور تبریز پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/27064" target="_blank">📅 20:01 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27063">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e9EuOUZMYW77le1-LOzoJqXSmWKwzuGQMiPz4aOWkNwhGcWK5rf1O790u07LU7mNJlGRWIfP_PZOG14HTG5xkpmFGkNg3GOXlYUh7Oz9R2w-tlZCaETpwFMpo2TVO7_Erb9TahH2YF68060F4RFTg6FrtoNHBxMLRttTkMnkYQlYT1Huc6B9Om02f3Fkl1n9UQIAr2zsHKFarc19p5qy0xliYIUznrPxeLGQCF1yI0YjjkCCGOc2w36Qdo-3yU1fW6OpHNc-sajUrfU_uhdcdrlBD3iJ4A8A0HsaaZZ2ZyE6TyN_fA8rBmTtxac-DXBp8k0ioo1elbjCCDpsI2YcMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
روبرتو مانچینی سرمربی تیم ملی ایتالیا:
🔵
ماجرای‌من و تیم‌ملی‌فوتبال ایتالیا مثل داستان یه‌رابطه عاشقانه است که به خاطر اشتباهات تموم میشه. متاسفم به خاطر اتفاقاتی که در این سه سال رخ داد و تمام تلاشم رو خواهم کرد واسه بازگشت تیم ملی ایتالیا به جایگاهی که شایسته…</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/27063" target="_blank">📅 19:52 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27062">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ab970d5a0.mp4?token=l2k84PC5xcOrmfezRwg-ZH-rrqRp3M8TKamRjPNi0OV5-j2EDudnZ66rLNLxycfGbGS3d8UgfhidQjFLSsjwXRoJGHFH0fvtA9aKCr9NpvNh1knXOaeVsvEBqpBDDASLfBxWvJ3Za_NSlhcX-rTygUrPKEbsq3Q94XnZdQe3-MW6qWhdWM5g-MM1mIVS7p_m-0rqodoR5UqqyaN_DBZDZsxZIFVMtv2R7v5H-r2D6qDZSsnTklBBnPhBMFoK9khmYI61PBsINrE9VJ6RGeGTthMh3GthNzL8G3MsJifINSv7w0zh8r0fq1zDWoCHPUfiuFhVUogp4MYy70TgG1PbEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ab970d5a0.mp4?token=l2k84PC5xcOrmfezRwg-ZH-rrqRp3M8TKamRjPNi0OV5-j2EDudnZ66rLNLxycfGbGS3d8UgfhidQjFLSsjwXRoJGHFH0fvtA9aKCr9NpvNh1knXOaeVsvEBqpBDDASLfBxWvJ3Za_NSlhcX-rTygUrPKEbsq3Q94XnZdQe3-MW6qWhdWM5g-MM1mIVS7p_m-0rqodoR5UqqyaN_DBZDZsxZIFVMtv2R7v5H-r2D6qDZSsnTklBBnPhBMFoK9khmYI61PBsINrE9VJ6RGeGTthMh3GthNzL8G3MsJifINSv7w0zh8r0fq1zDWoCHPUfiuFhVUogp4MYy70TgG1PbEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این‌ویدیو بازی‌بیلیارد تو اینستاگرام 224 میلیون ویو واقعی خورده بود که یه رکورد محسوب میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/27062" target="_blank">📅 19:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27061">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvvS8P9kuQaMBxMiRRuIStoWXTcwpvXIMpXzzcQZCoT_yHtnfP0FEGB1zeWPLosLdCI4qEyTvvw_drUQZ5h-QRaIdCcjiSN1JepuAYsTTjdaMykg1HAjVhqxFo6UwF-nmiPJ-bVVjAMH6N6SlfULO8S--Lj-Jkg18Wvyl8kDA_LGAvQWMTdTIr_HCnNujvuLDuVbZeS6u4DLc7eR9j5CBTw-dMXqkPBGNOzTVpR9XqeVG6h_Z2SyyzeeWcJAvEPzZW_rqyaQydKuq-OErrQmybCVzpDTgbJQPNuLjkELKl1yb0h2YPp753H0ZJTHs9_9x7LtMbNwGxVWvQYQYyT7iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بعدازجذب دنی ولبک؛ چلسی ساعتی قبل جردن هندرسون کاپیتان36ساله‌سابق لیورپول رو به خدمت گرفت. حالاجالبه‌بدونیدکه هدف ژابی آلونسو از خرید ولبک و هندرسون‌بحث‌فنی نیست فقط‌وفقط میخواد تجربه تیمش رو بالا ببره چیزی که توی تیم خیلی کم وجود داره و رختکن تیمش یه رهبر…</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/27061" target="_blank">📅 18:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27060">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bm7zWTtG70DwcFgfd0xVYip2GGItfFL43B2oHmCtUPP7MbK2a0vXmtBH1yV2HQh_HqeCcGRk8tpV-kl0HfOPwxmzIoBQMu67JW_M1rG-DqLpUhdkpTykA0l6xlbIigD5nUJOMFcYH9uVYOtqI2uq-D7qfbgdJ661PGbIfbUeTepHJAdRQLo30COd2vYM--zR_mm6KMYCwvOyCONze41VETUZcEFcnh5VkMwTld6SyS-D1oBDEdT9jzhRnVle_SyuWe9K4emozaiMi5v2qf3v7VYjqYFQReRwBHhJc1bgneJlyfmImc79nLShOVfN8OT-eCBfyQOvx_mcX48xp4E31g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
#تکمیلی؛ نگاهی به کارنامه لیونل مسی در دوران حضورش در پاری سن ژرمن در تمام رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/27060" target="_blank">📅 18:22 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27059">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vB4ul2XndvkVIDGC2QUz9J4dt2Eoo2BYutzw2hOkQ-SpaNW3nenuoHN6LUg25LhGsQ3q67JybpknXMgJCEAxYYqtXJSZIdFOaxJWqbGTqL-GdUK6QDufXdIkiUVWWbC223GfZQu7_RrTYnEhSTmSvU2LTpZT4zDzA_ZEJ4MGxI1jccsodehXffxbksi27DcA_5bB0N6GNU09R_4576Q5wgs752yLUyrzghSBfxfLzx5pgY6UkM84YyyjJ-mMwYO6ERR6WwTvw1B80BR1GQbVkvHuCUjOwpuocYfE7EuUR_SadFKY0J5huWVvTPPHv1ndhq7hf2q4CaWO-I4tlWvpvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدشد؛بااعلام‌فیفا؛ دیدیه‌اندونگ هیچ مشکلی برای عقد قرار داد با تیم استقلال ندارد و این بازیکن بزودی قراردادش رو با آبی‌ها تمدید خواهد کرد و از هفته اول رقابت‌ها در خدمت این تیم خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/27059" target="_blank">📅 17:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27058">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/um3-XxdO0ycFFoRY0mpSSCjv2mH5F7D2egqh0eClNat1S2ttEUJpM-ZJfGMARjff_7P0seozXlhqNhYBUjf5T3oCsXfJ-4OFTqfHAjjAvQ7Wtz2xN4NJRetpZ61YfvRVvfOzKifZcJTmKQBn7gRif3SfGR-hPFrI-Ppgb0BQ92vDuplOm-7PbjsSJvBE3sVGuPTx0YHmeG1s62InhuP_bGCSVVcXO5A1anSMdhrSvQx7matyCa9zSUsydKbo5sUa2JlRbaE2S4XleoI5PZAV3VshSetTTLbSae1sseXdurbIk_nCDYwsXky6OIeQFoy9EbyQQVfenBBm2g6uid8nEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
هانده ارچل: من از بین تیم های اروپایی طرفدار منچستریونایتد هستم. علاقه من به یونایتد به زمانی برمیگرده که کریس رونالدو در آن حضور داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/27058" target="_blank">📅 17:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27057">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ar-iKsAFI8Z9Qw54ozdZ-VL5irfFruQN60wzNrKqzueA7ahSkF7Or4vjpYaB3VmADUgdAWlYZ2-QULIpos-enI4c5XYfMZmcRQHrwh13zHHQEk2UAiwm_UnWEuTKWec5D9sG1jtdv9URchp4W5LoejJBC8KLQn-RL1_067EnTrX25mp0_26nEUjNEmbMThcYs7HoWB4hyRpXjruaOEi1LtlAZ735c3usAd9lmb8XbB-SUxCKtPUN8VBpXBIt3jST2j7qb6BWug8zFviifYswsbh6RkpzExkMBW-HhI1bOQODl4Mp5TdDrn-DDszSBuIVCTwlLQuAWvbDpxrttBAQUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
نام مهدی طارمی کاپیتان تیم ملی از لیست اروپایی المپیاکوس یونان خارج شد تا این بازیکن در آستانه جدایی از این تیم یونانی قرار گرفته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/27057" target="_blank">📅 16:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27056">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LQIZKoho1s-Esz0hz3B6jx-ZAkTbPbD1ovYkJAQ-i6iHd5kn0lI_IsX7RVTr7HfBwAUWVPXk-PMabkJ0Qpt1B-qjW8iLxderJji-dToiQbA5qtmcIrcrxqcXTuz6sKnz5ZSzltrYucjpTn9wKawgMCU_K4JuiZkA874BsmwZOBa_j2CVR9L5Vdu9fZv1brX9vH3DgkAX59lVcJ7aRrQ_fMVHGSHc1CPLogjsotokqhueHSn347q-Nq8RVbHS-lneVQhY9eboNYRCORQtbqYZUGpombtXK8hwj08qrIuZ-XFzEsPiH24bjYJQH7sfSZZuTODSUUD55K6cofy3tUZltA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ سید مهدی رحمتی سرمربی‌گلگهر ساعتی قبل در تماس با مهدی گودرزی شاگرد سابق خود در خیبر به او اعلام کرده که پنجره باشگاه استقلال باز نخواهد شد و قید عقد قرارداد با استقلال رو بزند و راهی تیم گل گهر شود.
‼️
رحمتی پیش‌تر نیز مانع حضور…</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/27056" target="_blank">📅 16:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27055">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jkOkWfIy9AfGKrXQCNDXBcw-QZbIpcgzZuHhep911LaMzOLGTcet1mHl98IgxG5mw0ZRQC4faHECY8QwToWLGuz5z-pE6GCob7Iu7CknCkjMiSY6bWmfDMJxWin47JoF5ef-2Xc2I0nsyMqUToEBFBqErqcHFadxHG_OiurTbpBuSs9cwYH5k343Gz0NMg0dNMVrbzh4km657v7rOH7pIXlbdllEkf-gr8r0vasRKbBdnSURseEhNH8UIRUW22tr6fPklr18W8Zkvceycs2yrw70nMKNmAomHbNYIj6GX82pqc6qRnZcZewZExWMIR9JbQzAbx6yHvmVkz74mTo96w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🔴
یکی‌ازمسئولان‌باشگاه‌ملوان‌انزلی در گفتگو با پرشیانا مذاکرات و توافق باباشگاه پرسپولیس بر سر انتقال فرهان جعفری به این تیم رو تایید کرد و گفت تنها مانع این انتقال مدت باقی مانده خدمت سربازی اوست. درصورتی که فرهان جعفری بتواند کسری از خدمت بگیرد این انتقال…</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/27055" target="_blank">📅 15:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27054">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2279080601.mp4?token=fbWxIFPKuRIF5qDKEPVKX5Tcz6V1PIfWjfKARw3f_8aoakX9p1_ZoWokhhTaOlydBGuWrYycMPWCxPluSUngKkGQ-iXfv5XbB4Sy9xujsNulP-mj-Nr1E1BQgBsbeKQJ3E0Jx4J7GQV0AFg-WXukiGeaXf8HVBC9rExyOy49sq4-3275eUqwv3tjYOUaQQpQPH2oz33va5Q5mS_IS8rA-lniW5DJ4MGFea4YBCCeuv7uRlEeAIQtu4pQEwvWmSxsOz7WxtcN8jsr6fxZKx9nYtjo2Jl-NKvE3pU73dfKwdOQNVQJkiba-KUuiDhSVWhKyKq9i7CvTDLTfgJ7mEHR1jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2279080601.mp4?token=fbWxIFPKuRIF5qDKEPVKX5Tcz6V1PIfWjfKARw3f_8aoakX9p1_ZoWokhhTaOlydBGuWrYycMPWCxPluSUngKkGQ-iXfv5XbB4Sy9xujsNulP-mj-Nr1E1BQgBsbeKQJ3E0Jx4J7GQV0AFg-WXukiGeaXf8HVBC9rExyOy49sq4-3275eUqwv3tjYOUaQQpQPH2oz33va5Q5mS_IS8rA-lniW5DJ4MGFea4YBCCeuv7uRlEeAIQtu4pQEwvWmSxsOz7WxtcN8jsr6fxZKx9nYtjo2Jl-NKvE3pU73dfKwdOQNVQJkiba-KUuiDhSVWhKyKq9i7CvTDLTfgJ7mEHR1jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
انتقادحديث‌میرامینی‌ازشرایط‌سخت‌اقتصادی:
یه‌جوون‌چقدر باید کار کنه تا بتونه یه ماشین بخره؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/27054" target="_blank">📅 15:40 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27053">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WjpoD6Hi8CTXNSlop2wCUBF5PG0uyrKXSuOzvlGa5liuzXNJBW_f8XOH1_1LESR5mo08EyzZiGX2nnNTjQy3IlD4cw50glOgnxZGXhOfqi1mTaFNuk_JSgFbVyXv_gmM4hC5fY_cU4yfR5t_lT5CaAy5SB6MafZfD0ioYWmAYQ0dkUpY8GFaZfLhbKEXip0Wa8z-fy0POoas4-adNXza2bPHKlA_Qc8WDYDIwpoI5uj5SiyC739mhkvkrSFcbRdXg6uE2l8WaAabIlLFD4_qrEuLaaWVmVAi_AnHa8hVFsHtyV_plCW1eXSCu5SnhWuFG05au-vpmbmXiNYI5MrbZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
عملکرد فوق العاده لیونل مسی فوق ستاره آرژانتینی‌فوتبال‌جهان در دوران‌حضورش درتیم پاری سن ژرمن: 75 مسابقه، 32 گل زده، 34 پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/27053" target="_blank">📅 14:56 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27052">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uqCf-rB7gLKkVBkllhiyZjwq-SsTccXkX9AWgb2ldVCopjsOgwLiLwTlh9RT_ph-AR7mYZy14n6nOepDCTJ-zebDIgk3evRHyGODUFPqiugE-zQ9oEFQAN20l3ifGG93wruU-xkPQ6bpAgWmxxESIK2GAMRMC9RqyQ7mCv5-pMLODw5wR1IWvivJCsyomtA6dwhgK2pDLSOVk7zUa2E4d68IEah-F-TBgwigugEGpghG-YHFWFbQtu6EEi30dR0DJ0taWu-fqOxuCfETuPKy5xmNinx5Khf2vNzJx1743_2yrlpX5SeB2sY2jgr_nLZ-Uc9OQGAFhKYsAYvTNpMC-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
احمد گوهری دروازه‌بان‌سابق‌پرسپولیس‌با باشگاه صنعت نفت آبادان به توافق نهایی رسیده و بزودی با عقد قراردادی یک ساله راهی این تیم میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/27052" target="_blank">📅 14:24 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27051">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AB4Ga63vaslTjaOXnQT1xWREzYHouVjqWgHW8jcn7Wh2_VJ7u7mVJsZ1YvGbDSP0VisMiikDVl1Ha0WBs61E_Ek1L44hm-eBACoVJ6Io4ebdOjdDjRvfmk2lPOkGQ2Z6WP_A_HMudX55vMRzdYP3GUED9kLMpgL73xEsYGzp9-Of_NQ1T25M2B31Q9sZRcoXeCXdDwLR31JgVixHUdC5MR6h1BIniT1vXh_DpDq7EkESVEaKe5ZmPKdzKOO_lxja9J7xKnAoeIJdPaJTeKDmjIDoevW933D6-7RWXOQpQi7rh8hEx0KoA1aE0iI-AY4mLZ1TDWdGKg_TPbx-U0ZTZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌_پرشیانا؛ آفر جدید استقلال به رامین رضاییان برای یک فصل حضور در این‌تیم 150 میلیاردتومان + 50 میلیاردتومان آپشن گل و پاس گل و قهرمانیه. رضاییان قراره ظرف 48 ساعت آینده پاسخ نهایی خود را به این آفر بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/27051" target="_blank">📅 14:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27050">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gdES0DGtSNAC0EI7TxWpDbgHF5-VA7eX29_82xOuW454gsY5TYaklgdFw3MKb64qrLz-1DIj5DvM44zIfh6HQhtT5QvNxZujD_mRMwWBLs0IfQuvbYWOFeHOc2mG7gmnPsaQJkdHWR44crDnBPc98RzfK7rypEQp7DBhn9e0_Ljub-uCVP4xS87ZUYErMefHqRSEjhlGPT-NlXTyr1mIGEnPE9B5gZRCCCc9g1eayNGC9EeVe5ANhaOCmXmQJcmQ9OERB97xhjws_wCgQMlXeZ__3lRH1q7gYJkGA4QFv9MTIE__NrOE_s6FrOqsgcIKfFHoVxAZjCfAZ6cBw4jA4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ جلسه پیمان حدادی با مدیریت فولاد خوزستان به صورت ویدیو کال و حوالی ظهر برگزار خواهد شد. حدادی امشب به تارتار قول داده تا پایان هفته پرونده‌نقل‌وانتقالات‌رو با جذب 3 بازیکن ببندد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/27050" target="_blank">📅 13:29 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27049">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dac122529.mp4?token=V30TSmidXx0tBxH1tD9ONR5nOFrq4Os5bZjPFpVzHtJQmBUrkUDZ_utNDLBouY2H1yorMi5Ia3uelpNS8EVWtV-aH2lxd6ATo2ray8rNCRGn-4sjta7Fxy85x3leguxl-prEC6nkWzTDR4HKwpVQoy658tQuiVY1u6nk3eSAIJy2TkegUKW_qC4Jtl578XIhyAi8xxaLOm9rdIO1hqrkGqRcxu42f_2PhCcVQUcwsOG3w99IdVkp2u1DEh4w7FiPQaADW2aHvA7ttxVr8i1Up4QyxKtytghrOcmfL5BpniajEpvBTKzt-yRKERpwK_gOpzgSMk-0SaRY_wLPnOUK3FiXYjOUFx-aVKJSq6wQz3hACJ95r0OqZwANTw85A3yUnJQXFJS2EmIcD2efkhgy6Uwo33Al1yfhVJY81wt62s2WoUeNtq2vGLegev3D1s0f_qyXqAw2SsfUTmYKpUwXVGe4LZiHR0995a1bkQVY_cIB5hj9LGfHbD6Eq8ZNaPLImpUGhMy2KVREue4FGh2qUSmqXciVluxBfIKNhTzEUEP1G5Gp8o6W7jEWS5-gIEnBEwCDwFkZDamyDakI0qEw7KUYPnUUAgjcCR-Oh5Xi7okjSMyqIRzcDM0HH4Bv2oPWm0fENrCFADCSMdlscbKAYwXPzxOb56WBUEQY09RD4a0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dac122529.mp4?token=V30TSmidXx0tBxH1tD9ONR5nOFrq4Os5bZjPFpVzHtJQmBUrkUDZ_utNDLBouY2H1yorMi5Ia3uelpNS8EVWtV-aH2lxd6ATo2ray8rNCRGn-4sjta7Fxy85x3leguxl-prEC6nkWzTDR4HKwpVQoy658tQuiVY1u6nk3eSAIJy2TkegUKW_qC4Jtl578XIhyAi8xxaLOm9rdIO1hqrkGqRcxu42f_2PhCcVQUcwsOG3w99IdVkp2u1DEh4w7FiPQaADW2aHvA7ttxVr8i1Up4QyxKtytghrOcmfL5BpniajEpvBTKzt-yRKERpwK_gOpzgSMk-0SaRY_wLPnOUK3FiXYjOUFx-aVKJSq6wQz3hACJ95r0OqZwANTw85A3yUnJQXFJS2EmIcD2efkhgy6Uwo33Al1yfhVJY81wt62s2WoUeNtq2vGLegev3D1s0f_qyXqAw2SsfUTmYKpUwXVGe4LZiHR0995a1bkQVY_cIB5hj9LGfHbD6Eq8ZNaPLImpUGhMy2KVREue4FGh2qUSmqXciVluxBfIKNhTzEUEP1G5Gp8o6W7jEWS5-gIEnBEwCDwFkZDamyDakI0qEw7KUYPnUUAgjcCR-Oh5Xi7okjSMyqIRzcDM0HH4Bv2oPWm0fENrCFADCSMdlscbKAYwXPzxOb56WBUEQY09RD4a0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇧🇷
#تقویم؛ 9 سال پیش در چنین روزی؛ PSG نیمار را با مبلغ 222 میلیون یورو به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/27049" target="_blank">📅 13:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27048">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SV7dVaX9Dl0Dh7pDd7xHKvb-nBiPaQw8eEY9sRQ-CjJAjBA-bFpgF9EYfZ-oy1mtLSxGwzX2cFq_FQD5hE7WYtm8nNM9-B56NpjR8KyT6UoMJ3cBmwNW8DUmy_x2Xz9kVwT_k2smFktqy7KEjChBbjp_QbFOqlvs6tSD9XKJhjIAvdANmG1Hbg1Ry8tOarIDHKlnN7pIDJ-GqnFgCoEZe9cf6OAx7hoagxoZQ_raPDz4Ph63_dbApUwy2PhFVMCyj-1q4PVOUXE07RPReFzLADpHj5Bn_B1VuWPO5alfO4OrKmeQuwZqu8bup0eOEpMTMXj2Davv3pMhkkmU0V4niw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
باارزش‌ترین بازیکنان بر اساس سال تولد از سال 1985 تا سال 2008 با نظر سایت ترنسفرمارکت
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/27048" target="_blank">📅 13:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27046">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGM78ytP3iuwzUSVtmkWCYcgfePYzuwd5YUf5muGBJCkxsqAHM9UUZmRxXbnj5hjR3TP5ooqoq8C8AXqXS2ltYDpVCLAXirXyW0b_1JTa5WD4yhos6j9mWP51vvtLPggAshIB609N5hITHaFy7vyg2z9SE4Qjj9J_3P4vd4HJXBfgD53wI6P0TGJ_dR8qcdRuA3H7c3xxpHi4LQOMhO3tJxFYg0EroHvJjlBiorpQh2DBxHXMWQT5npKpCb9zJ913gMmPHgD-wZGekO0WP-xfeojkZZAtS1_cEU5LAExa5ERsKybn_O8exUa99WXXtMXKIriP6aAZsWaVYlJq3OmVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛دیدیه اندونگ بزودی با حضور درساختمان باشگاه استقلال قرار داد جدید خود را به‌مدت دوفصل امضا خواهد کرد. تمام توافقات لازم بین اندونگ و باشگاه انجام شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/27046" target="_blank">📅 12:52 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27045">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EO9b5kVcrnpL6yCizhdHDz8vdhmlGsJDZMCxnOurxdIBApqnWF_Wq0G-tQX1bI_Llq43Mun8hBopNH2BlWem59XSbzuDgdNs1vckEfqgI8o49pEYk3NtvAbNEwyfAp6qZbJJDaKNAwN6Jo7Ccvt0b8w1QTddyZ4xiNTgDKMqiqor-D1HNzTmhAaoXa6Owh5k9-FUAcqqGJVpOyCXRtDyoRI9C8r85VzOB8vbgHWsU8Kx8W4EPloNlO52QIk-lzRAVyVrVpdxQjWEa8-RJysApmIuoFUbeXhYw2KdrtD0LfM5FPOBBlsZPHkSSdIeQaZtBFvp-XXRdCSoy2snVTjycg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
برخلاف شایعات مطرح شده؛ فسخ قرارداد یاسر آسانی با باشگاه استقلال در فیفا و سازمان لیگ ثبت نشده است و درواقع‌فسخ او یک‌نوتیس ساده به باشگاه استقلال بوده و با بازگشت‌ او به‌جمع‌آبی‌ها او هیییچ مشکلی برای همراهی تیمش از ابتدای شروع فصل جدید رقابت های لیگ برتر…</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/27045" target="_blank">📅 12:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27044">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7821302722.mp4?token=Z3djGk2Rh-KK4piKfqaQ5guMKv40YJKCtytMndv8StHVstoU8z0aIYzPLOPjOSLqKZDm7UVSsQDmK2gVg84Fu1VeMQvUG_5qT4aR2NEyPGGIU-SlJ1XfBIAVNmG-gL0B6azO15l2rucIl3SYFXcUJTAvUiTfW0CT6teOaeSOPfmz-H36JzZO4QQ1i8xUOrMK1lvuBCYJG25GjORAlcPr7QrbruZsoAaC6FGfc0y2gC0iL1Vmfom4eFuJ_UhK6n3g8zlLK9N2QIQX04BlkRRHzfDud94NYggagqM2rlu0FpfaSKU0hB1QMv5y92UbJsFkspZBZIg6dITOmYY9Xq4t5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7821302722.mp4?token=Z3djGk2Rh-KK4piKfqaQ5guMKv40YJKCtytMndv8StHVstoU8z0aIYzPLOPjOSLqKZDm7UVSsQDmK2gVg84Fu1VeMQvUG_5qT4aR2NEyPGGIU-SlJ1XfBIAVNmG-gL0B6azO15l2rucIl3SYFXcUJTAvUiTfW0CT6teOaeSOPfmz-H36JzZO4QQ1i8xUOrMK1lvuBCYJG25GjORAlcPr7QrbruZsoAaC6FGfc0y2gC0iL1Vmfom4eFuJ_UhK6n3g8zlLK9N2QIQX04BlkRRHzfDud94NYggagqM2rlu0FpfaSKU0hB1QMv5y92UbJsFkspZBZIg6dITOmYY9Xq4t5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
ویدیویی‌خاطره‌انگیز از شوتای‌ فوق‌سنگین و برگ ریزون کریس‌رونالدو در دوران‌حضور در رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/27044" target="_blank">📅 12:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27043">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-twx7_hBqN6ntg3eRDBUqtBf0z9GOkOb2wSfX2gFJOPA6Wb-vxFpNyGsdlc7xEXFlsXbVkA8BS7Fg4PpjAeMlp3nh0omwiM0IlZkKK5IlRiydD9EB4Y51Kzblt7rswDtibHFiF-LKS2XXXoI_Ouc_rmJj86hOBUO_eQzAAM3ONiNytg-Ch_OYb_H3Gi7fs5iEeBm01yuL-J3kUB2bZ-W3WfF1vwVafcuFlGcoteUKsCT2Oy8DRjS1P6H8BqNt2r7WN_4mLZFZNBmwIx0JbQNh7EJ0Z46-KilLzoFE4r-cUuOHko0EmdKw8woeeoKMayp3oQ9QGGmodhMt9ZfV-snQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
ویدیویی‌از تکنیک ناب‌وفوق‌العاده تماشایی نیمار جونیور در دوران حضورش در بارسلونا؛ حیف صد و حیف که به اون چیزی که لایقش بود نرسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/27043" target="_blank">📅 12:04 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27042">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iukl74YHeWK8TcdRdiX-UX_oA64Pxpi-Om9zy5lbI2BjeDoU5b3OYEiZZKULIioaQtY2yG6hIVHFH7EHaOmNZsrTIcZTRObh2VT8um2HyKjD9hOfG0KqkLRgX6CWZvmHDkLxQrGYKlkUuAbpGM6ntsJ2b4UnKcoRlmgIYmxE9J1Ctjo9i_3ziNCZbc4YHGSYukihe-e2kKDyro8WwZQ2EfuNl_f24oAG8T6zTMMBZFb8UAZHZJL2-ymmEMrNUNy9dJc2ANNUqQ8FGqY-eKzemAAIseO4X_ppdiwxV_dSzXQqzhwWqK9PJIxdDbq-zJD8MbKSOrKtk5uHh7DryBLsMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟢
💰
#تکمیلی؛ بعداز موافقت مهدی گودرزی با درخواست سیدمهدی رحمتی برای پیوستن به گل گهر سیرجان؛ مدیریت این باشگاه 80 میلیارد تومان بابت رضایت نامه گودرزی به تیم خیبر خرم آباد پرداخت خواهد کرد و بزودی این انتقال رسمی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/27042" target="_blank">📅 11:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27041">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e1VVVTl8p08eLo-rNeIROgNDfFcLepaifN1I4vvJGhimxfS5f0OMLk7PHd_hDe2KPnIBZgAINt0UjPz-XI16n8o7O_oVBDEqgKikccKdcGQQjGBwjs9oEGvLFibtFCl3kySq7whllTQiqBn3JVw7vulrXKAuZOXulEH6ckH-Kj3IOlUbUCuHU8zYN1snAhzcDoviw59SGMv8qh3Ri4fEw-RCr5MlHHqxJWs0HqwYSvT_t5MfnzeknsQPLOKAOAZz4Vpa9j40Vz3XQSJIbe3EAATenk7RO_FPErVbrLS4_oVAeUET-uH_YBikEHPUwoDnBog0qoPGHUV12gdEsJbXPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهارت‌هایی که توی ۲۰۲۶ درآمدشون میترکونه!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/27041" target="_blank">📅 11:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27040">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YDg8reJeaSWDPNTC-588ufc54k5qcKFUFWhBhEPmnyYs2VZucfjZlAoNG_k-uEK9tbCaoh42rGhDRAnR49cINOs1SUNQReBqGssNQMp1VP7zeCG2ZwF3MhZkiEAdzUW15yM2r-4EApkPJ7WklghjkwzLpHlx6vFAD7NHiowJkJCZxBz5019-1he19V5KHK7UKJNEzgFKZY7UIjbPzSOz5MopC5RwgDj_-SLo1kqgPxnCMsEOVt3zARDOqnxJcLta6oWRJKf2harFsI3d-BeXLjZu-OtsfOMndgqF0s2XiPsB1FUyNIDCm6Xzax5iJuty5qRLZwuf-x4lgikm8AKpgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
عملکرد فوق العاده لیونل مسی فوق ستاره آرژانتینی‌فوتبال‌جهان در دوران‌حضورش درتیم پاری سن ژرمن: 75 مسابقه، 32 گل زده، 34 پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/27040" target="_blank">📅 10:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27039">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SW6DsgcMvPxumtlT-SvLbtaYfxtMhqWT4lxYmKNdsL6BlDd4MfuhVXPJKT6f4vXRgqySthkzU8DYsc4WrR0K6-jqqvD2E9nMWj1uzIcw25m2aqeRfHKFWeYA8vGkmOz8VdSZjX2AxZFXOS0lYDsyI9p-7g7YBiI3TwQFrXXnZVh1Vmm5RX8OMZjDsjUnBTPTQM3V6oXadZL5gwp7UIXNqfu7kFcYavBsoftMbkAByNtEDTf9AEKykvc5-qy0VTN69lamDcPntLrexVeLWjwWESz3YXTiQdhnWZ5MhS3MPm_SfTvu5v_L3Ph-u6-CeFae9g0YinM4zbLuogL7q4mkMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌وتاریخ‌برگزاری‌دیدارهای‌ سه‌ هفته ابتدایی فصل جدید رقابت‌های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/27039" target="_blank">📅 10:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27037">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DKsNDQoHzxIdSHHACFPgQnQbv87uaIsyRhy87jU1ALqtxa29yNDdg6mqI8z4MhaTouF_-Ow4VvpTReVSa8JRE0CNgiJo00vlu00hG9gZWnprxluLIkbFJdS3nR2QWeKmsNTYFXJ_TYAN1viQTRJ7nSshdtf8udCTAKepDGP1hYlmmwXjSgk3lzVS_ZAC3pwPY52z4bPe1G_zYDYgyNBKC6Q0QwkW-FyjrcMLfTw2IKqxiEFZCa6SycP-sJoPXy8pkPSRnjYqGlD2HSCuXE1eFrmcY6WCkogyDPsjvK35Na_YgeP234YpkRa2q8_z4mEGca1iJIIGrMzDo4fNU-cmsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
هانده ارچل بازیگر معروف ترکیه‌ای که گفته درفصل‌جدید رقابت‌ها طرفدار منچستریونایتده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/27037" target="_blank">📅 10:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27036">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZGiM7wauOFIKEwu2Vc-XZoAx9uzHm0eyrZLoNgo7qaioUK2mP6tFsBtRlUYIehzWdNLrMjDRKQLsu98fZ4eWtRhQzlYyiznX5WnjPW1gcN1uh0TsLEb2029aqqH96tdS6NoaOLhYsB00bqOdRPEUykoh_tbLAPF8GJVf6U_PjwCt0I_xCgk5zyylZwAbDApSMQwQFkpNDYJY2xpUn9ocG9ZvYl1TdtyKCYJ4D4YECQnAq081GbNDqC-_-7GJqfTs0THOaEPfq1RzM0NOIiwNb99sXbzb2zv8g5UL5WPHr0b9fJdVLtSXJXFaI9VNtVzNQRfwG1UrOHCOit_0shd4ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌پرشیانا؛مدیر ورزشی ماخاچ‌قلعه به‌مدیربرنامه‌های محمد جواد حسین نژاد اعلام کرده که تصمیم این باشگاه برای فروش حسین نژاد قطعیه. هر باشگاهی دومیلیون‌یورو بدهد و خودِ حسین نژاد هم راضی باشه این انتقال انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/27036" target="_blank">📅 09:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27035">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pr30je4QPTpmS143dolKnmoNFnr5ekelqWU0LXMQwKMRmXfgOTdezkHPQO_FZsUPn9x5U2luL1HG3abf1lvjeyRsqHi8SV0WSO1B7llcIR-X_971tXY5fk9fGgJMTHxNE61b05M-5HY-xca0z2V_JzMS94nisPSuJmSY2MrMCa6mZJsfy_05Ohn6SqPZ_jMuWX3ZGxQiIHxwYiIq1qwtPRAPMsw_OP6P68nSFUMtOKJq9WIm3qjuKH2iFsn0LILfuyAJ5vT6Rr1a4DIR260shIX5gFf9QHt-zV1RiSufWM-Foft8mzSwyjNWDwB9gOfekklmzc8SPL19SrhWFOjXOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
احمد گوهری دروازه‌بان سابق پرسپولیس اومده ویدیویی‌ازعملکردش‌رو توپرسپولیس رو پست کرده. تاجاییکه خبر داریم مذاکره شده. توافق هم شده اما تارتار باید تایید کنه. بین گوهری و عابدزاده یکی به احتمال فراوان گلر دوم پرسپولیس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/27035" target="_blank">📅 09:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27034">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f85ecaf4a.mp4?token=Mx3ZAzMSYF630gob_6a-aXIxWGZTktIOM6qQx_vw3DtUHrcJ1Qt0e3o9tNWuoSgCup9fpchTb1k22U2xi9cytfeL24vM3N3Cc3H_BzRq51H9N1XsNiIMRPZFTxjskklDN5IzbLRf8kDG6Nn2ZmQ6z5cH7QGXF4uFAfboVQdWjHP9ZkUR_xnTmU5rEfVk50P_dDulwannPGtXqAmbs8zLwx3wXM3tkvnFU9DvTYoNJMjc0evQa6h8dkVyrvbRvBKFb9IMsjguSwRrZ_7-iGps93PraJkI3XxOzMt53catNH4serdKN-cM_KxZnqQe57z4SNkHNrfpGOhJeYBRSYv4Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f85ecaf4a.mp4?token=Mx3ZAzMSYF630gob_6a-aXIxWGZTktIOM6qQx_vw3DtUHrcJ1Qt0e3o9tNWuoSgCup9fpchTb1k22U2xi9cytfeL24vM3N3Cc3H_BzRq51H9N1XsNiIMRPZFTxjskklDN5IzbLRf8kDG6Nn2ZmQ6z5cH7QGXF4uFAfboVQdWjHP9ZkUR_xnTmU5rEfVk50P_dDulwannPGtXqAmbs8zLwx3wXM3tkvnFU9DvTYoNJMjc0evQa6h8dkVyrvbRvBKFb9IMsjguSwRrZ_7-iGps93PraJkI3XxOzMt53catNH4serdKN-cM_KxZnqQe57z4SNkHNrfpGOhJeYBRSYv4Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇦🇷
عملکرد فوق العاده لیونل مسی فوق ستاره آرژانتینی‌فوتبال‌جهان در دوران‌حضورش درتیم پاری سن ژرمن: 75 مسابقه، 32 گل زده، 34 پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/27034" target="_blank">📅 09:24 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27033">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/371eeda394.mp4?token=DD430l3rYz74O2P5H-WnqagV1yY78NyqjnlUsnXjsjHuAWNxpM2qU6AQZuKY0LusASF8p6iJhzo37vtQNMyDMqV5vbAsuWTC7WbbMmtPx8GTwwXoilGFQyF2QPiHGzlckNaWFpFFwJZdVmKmnwR8LwspgljU9JBOGndlThD1aAqa8YkKs-REC93iKrxSpO8siQPKdMyIv0Es7W0OiW_mssbsonBXljCm3WFZQk-uOWjgcvofv3wf_6LuxZzrFWNyOpumJeWfyK3kl5oXPsg5Qa2OB72pmL_rjNnlDMQ5je2ReP2BSMJQPtvikelNv9klA3thoFjAC2AsCrrOtdbMHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/371eeda394.mp4?token=DD430l3rYz74O2P5H-WnqagV1yY78NyqjnlUsnXjsjHuAWNxpM2qU6AQZuKY0LusASF8p6iJhzo37vtQNMyDMqV5vbAsuWTC7WbbMmtPx8GTwwXoilGFQyF2QPiHGzlckNaWFpFFwJZdVmKmnwR8LwspgljU9JBOGndlThD1aAqa8YkKs-REC93iKrxSpO8siQPKdMyIv0Es7W0OiW_mssbsonBXljCm3WFZQk-uOWjgcvofv3wf_6LuxZzrFWNyOpumJeWfyK3kl5oXPsg5Qa2OB72pmL_rjNnlDMQ5je2ReP2BSMJQPtvikelNv9klA3thoFjAC2AsCrrOtdbMHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚫️
آرتور ویدال ستاره شیلیایی سابق یوونتوس یکی ازبهترین‌ پنالتی‌ زن‌های تاریخ. ببینید چجوری میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/27033" target="_blank">📅 09:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27032">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OOamcYrjgzJG3ama_5dHeohJ4aqz0gaJAbaPNiIrC8WkW_3WTk6k4xf4kc26nX3qNA0qXlAhGeK_bOWR8UHkZWXePscWJ50P6Q0OTS1KYX0GFYn-DBzXnpPeay2XpmhzwFkU0WIU163MIJLUOt1oWr2Dk1t11er0du8Rfkifu61fnC6hIU7JWNxET83eohlEzQaD36E0haEkf42yL4uBc3Kl_bv6SbbdF51cpu66n6tzYRt1bgdcQyfzP6Xxg_SkS6burdJF6eTXErbNoATytrGrLszsbJdzHXjqIUxv8iygeoF5PoG1y8gJ0OLHDub7BVnUMgsyLYWqVJURMSK6bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
درخشش‌ادامه‌دار سوارز در میامی و شکست عجیب شاگردان ایرائولا مقابل لیدز
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/27032" target="_blank">📅 02:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27031">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71e2aeddb1.mp4?token=QjbgK4Go4aUr2F8YVHT9EYD3gQdQnbP1a96PI3W1SAX8db5XsubgyWJTMV_0aY-ozYbrqLdEvV6W9I9noQLeLh4BIkaiVwU_ymoJfwyh1h_aMjfMuaDXZrJXdzI7QAaQKR51XfSA_hvvC1yg6hiE40enTA-tM4vrUg1AJ92ZuiyCTuRVT-fJP8ohWyZfIk_F9S1rApbBOK_BdWdloL8ZOuoCvTHYnGnfMermLbFRuAMoToXL28BgTl8pvsiWdSMTjlTc3UuHIqWA_wPxCAGQMx4ek17CtVqQiKVU9rj6SoPst-3cEf8vwGCn_R3gf1V2fUDwzLZNhF7fSJaRItZhmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71e2aeddb1.mp4?token=QjbgK4Go4aUr2F8YVHT9EYD3gQdQnbP1a96PI3W1SAX8db5XsubgyWJTMV_0aY-ozYbrqLdEvV6W9I9noQLeLh4BIkaiVwU_ymoJfwyh1h_aMjfMuaDXZrJXdzI7QAaQKR51XfSA_hvvC1yg6hiE40enTA-tM4vrUg1AJ92ZuiyCTuRVT-fJP8ohWyZfIk_F9S1rApbBOK_BdWdloL8ZOuoCvTHYnGnfMermLbFRuAMoToXL28BgTl8pvsiWdSMTjlTc3UuHIqWA_wPxCAGQMx4ek17CtVqQiKVU9rj6SoPst-3cEf8vwGCn_R3gf1V2fUDwzLZNhF7fSJaRItZhmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🔹
👤
طبق‌شنیده‌های رسانه پرشیانا؛ با دستور مسعود پزشکیان؛ مجوزفعالیت فرهاد مجیدی در لیگ برتر صادر شده و حالا به‌خودِ مجیدی بستگی دارد به رقابت‌های لیگ‌برتر فوتبال ایران بازگردد یا که خیر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/27031" target="_blank">📅 01:24 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27030">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KUr-19Rs0HKnf0OKfzFxanI650iAvXHYvQWHA1pUE-Y_75NFvLm6HK33YToryV-yfQ134-31bfsl17b3LNSeqPJUJV2t9NkCZ0fpI-QBAzMbqvQBsB9gjW8Fl4S4wYVbpaplrsgZWrs-_D71QXHsuB-M1InrtXhkJOLeJa4N3A_6jYQuqMrZ0aB1uK9KhDzqdMAujAn4izEdd9lsFIaoCpTitLj8wx91uTxjtXqhsgZsCS20FFbo3iURYJ9v8Eq7Tn34CPlBFP-LJN5Z-6FC-mGXzbXc_vS-1_Q6gwlFdyyIYwbDOSwiItccTGMV0r2XQqcDKpLeDH9CbVSTolvNlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
آمادگی فوق‌العاده لوئیز سوارز در 39 سالگی؛ تو بازی بامدادامروز اینترمیامی‌این‌گل خوشگل رو بثمر رسوند. کاسمیرو هم‌که‌گفته‌بود اومدن‌اینترمیامی که به مسی برای بردن جام‌های بیشتر کمک کنم تو اولین بازی اش برای این تیم در دقیقه 34 گل بخودی زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/27030" target="_blank">📅 01:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27029">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SCd-V7V5Kpe74NEwCrPq0_3S6PDCmpa_sgZ26X489ubuLfMOWfXGhwHrHmVXKk4FiB5Pn_ueY66P69BFs3vaoTJcZt9G_LtyvZZFy0GX2tbvqRxShg6JW2AX01hHHyFzSLXPB8l3DmtZOz_34omigtY0a60oGJUkwdThmuFjyG0l1o7DTIGz3Z1B2IlQIJpuJyKOK42qipy_7-j-TBKdHiGEXJu8ghfqfVIK1-_2soj9fY5phpj_MOXCN1OcTI0RHsHB8M3g9T1BiJwurN5xv3bySuvmTkmAyKRD6iVVtfHL-mIsJRXYbB14RTP9g1OtYoAk5Gd1qkmvfQpeRfsQTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطورهفته‌پیش‌ازتغییرات مدیریتی باشگاه استقلال خبر  دادیم و امروزهمه رسانه‌ها این خبر رو پوشش دادند. حالاطبق اخبار دریافتی رسانه پرشیانا؛ مالکان باشگاه پرسپولیس درپایان‌نقل‌وانتقالات قصد دارند تغییراتی در مدیریت سرخپوشان ایجاد کنند.
🔴
طبق‌شنیده‌های‌مو…</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/27029" target="_blank">📅 00:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27028">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aXZk--jZmcBdQGxhCPLilcrIrybUu5BqhGP47m2P06vDTxvaL4DtVqrgccxd4u-e9MMfmiUQ8syno8u__iyUZyVm5BbiJB5bmTOzMMg_fdc8MLb-A4wPxw4e5Gt_JLb4ODMGnnyeTyV9xhGFJTLqatwo1ufoERphpnrj3AYlULhb0J4W6TWKoLJUqmSmum5OikzQe33XAKI6Guyfwx40aJpfQxj6OlSyQXT6QSrXAriSfMm9ujpGO3wU3mLCBGLPvXtPggBYKRmGwskpH22DueXU480Ws58nWgomy5OdpvIwJGa6hqOnv0Gmw6fK3BiIkPtX28wQayBiNFaGtXW-Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
کادناسر: تمام‌توافقات‌بین‌دوباشگاه منچستر سیتی و رئال مادرید انجام شده و باشگاه اسپانیایی تاساعات آینده پوستر رودری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/27028" target="_blank">📅 00:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27026">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJ3yqV27OCI3uyMkL2uxeo5DpF06nFEMC4t49pgGjnSxZMrrb-tjwwfqZPVCayi7imyPmG6T0d-aZPZrW3OCCcMQgHiOxraN-K5v2piRV_7k1xa-U1HS2UoMlj5ksUHjHJR3L6PX0oLxE-wvm8TEy9xT1yOYMBjwFqZgcvR0q02N4ihU1fc6EhiKt2FIt5FGY0BhdZzWKp0PFa9F3zxOrqxfhJQmqcdnOcj6GsYxOTCpNOd3fUXt0fBpWjhKxhOhN0W5uxE_Tepq7DR9yYaRLMPEstAWafR6c9WpqQbdn9L1cUa8OIVSroKcK6IQPwPwOR93-WBobaJG8yfoaJIAoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شروع‌رویایی‌پرسپولیس‌ِ تارتار در پیش فصل؛ پنج مسابقه، پنج‌پیروزی، پنج کلین‌شیت؛ امروز هم باشش گل تیم ترکیه‌ای ارزروم رو شکست دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/persiana_Soccer/27026" target="_blank">📅 00:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27025">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWMvfwE3LyZrX8XZKAvu_R8whN0G_fZGHzX_SOBxrvzKp4VEGKQ_V79GDhaeqrriku5lzJAM0_yYVSrao6QDEy9a0a_GfR3cfM5aVHR9Xk_n9jpDSG4gObYSeOPi7HI5SlQAkuzsD54sIZ_3WdRjMMhCKxf4z70KWNKegI0NG0v-W8c32yOUn6kAhAW5aVkw1Pz01kPYyGkSiS7HdvLIUg-2A0qFZHwASxXdMoD9JyJ55bexU0r4h2FnAAGnjOK91a4fudutZqHoDQN9i-rC7bR1nY_AaCQh8Kw_crSjjGOlFsslmumf3mAzApNWMr6CaEu28lWDuSbC2etvtzSlvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
الهلال برای جذب رایان، استعداد ۱۹ ساله برزیلی باشگاه بورنموث و تیم‌ملی‌برزیل آماده آغاز مذاکرات شده و این انتقال را بعنوان جانشین احتمالی مالکوم دنبال‌میکند. رایان جوان یکی‌از استعدادهای آینده‌دار فوتبال برزیل به شمار میرود و درسال ۲۰۲۶ باانتقالی به ارزش ۳۵ میلیون یورو راهی تیم بورنموث شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/persiana_Soccer/27025" target="_blank">📅 23:35 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27024">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pAySLS88rtIEPWhXpjp5pirfuR7QWA7gk4bRltT6PdmC0sKwlzf0zH5er8t6MdDIqu491XyUHBRLgpPtW8LFR-mBRpAWy-pQGSU5HlXRkI0i3VoAwop3o2IIQVX4bQ9JQUz7ywQ5TIEzQXSrXkdu9IkBpMR04u0lmBrFEoQ6Wp2oEHRCRIK37fsacbopJQoIXiwtj5yPir1kHrcPStk5_pQp8yY7_qmxfr57yf9_cnNkM0CYK8lhQXxc4D0eF9wrQhSpIFd-pIVWrjtUbvW239N7UxFvYdliJWjG0u3nb9jjv_QY6TIH78GdOQFYjMcaLr2FC-UteYo8_1PQ0UhlIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛ پیمان‌حدادی‌مدیرعامل‌پرسپولیس فردا بامدیریت باشگاه فولاد خوزستان جلسه خواهد داشت تا آخرین تلاش‌های خود را برای متقاعد کردن فولادی‌ها برای‌فروش ابوالفضل رزاق پور ستاره چپ پای این تیم به کار ببرد. گزینه دوم امیر جعفریه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/persiana_Soccer/27024" target="_blank">📅 23:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27023">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ajLV3Bgh4yUBDNNPNHPlV6HIH2EB0tse6BSd3G3M5yIwneSPqzSoo9C2zbLdhYbNvE9wWTTx0Ffmips-TJarLeLi_AKA8h-G0hIAaX-_kalb99JpVEH11pz0BAGhOKkjERc0kYgOsm3GOPfXzQZBYtEOP-JmnhwI1sA28Vwqtzv-UtR77_ieMngoGqIqq4S_-nALxmvG2Hf0u0UGNaoyNTzd634Z3bvSQ6Ki77FbpIBRbSKPPoaHsaITwiGP0eR-L_kW5WUzGDZn6nU91oh6vZN3gNryVS_z3iFmsl6Lm99vRcZNZh1JsAtZZKenrpSKRaYm-f71wBKED0lNlPZoIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
#تکمیلی؛ حمید مطهری به مدیریت باشگاه فولاد خوزستان اعلام با هییچ رقمی ابوالفضل رزاق پور رو به پرسپولیس نخواهد داد. مدیریت فولاد به پرسپولیسی‌هااعلام‌کرده بود اگه‌مطهری اوکی بدهد این‌بازیکن رو با دریافت 80 میلیارد بهتون میدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/persiana_Soccer/27023" target="_blank">📅 22:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27022">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ht791JLDCHeVZNcFfumNaJkM99wYxjSdYnUQu_vzoPp_dTsb62-hDJUZ9y9qAMiE-KhvuAhvoo0iY-JZfvc3j-cdE3XGO9xNlL0h_HmKY0Cv-zQ2rvzrAUofwYex9x9sRVQwRFs2KRq0avqhN9VsPIqrC-WxOKuuui4A-gV_zcTjV2mcL-riuUk4IdrRxiiR5s5-ZcTU2PVqffjIUMMPrxBJ7_9alzJz9ZiWgWtyiqsbGWZtFahkmtKjqbSHaxQTpcnbcANAZV7Kw7brMbY5Y7Nvv2u_aFrEtkyUkkkdOPjEmFbA9r7ZTc5XKYnVLeVwi7i68e3tCT66p0E1ZC8-JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
دادگاه‌عالی‌ورزش "CAS" روز سه‌شنبه پیش رورای نهایی‌خود را درخصوص‌پنجره نقل و انتقالاتی باشگاه استقلال خواهد داد. اگر رای مثبت باشد فیفا پنجره رو بازمیکنه. اگرهم رای منفی باشد این پنجره نیزبسته خواهد ماند و با شروع نقل و انتقالات نیم فصل پنجره آبی‌ها توسط…</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/persiana_Soccer/27022" target="_blank">📅 22:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27021">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JiUg_kat-_XbD4uEvhniIl6dGCPap8EtnYDgeUqEkTUhPGo8KmSruNAl9I6ur7bXB9UjXOXHpJq76enueuHXZ-cIPr8CiZ08T6O75X9-m5tB96sotJsJhDc1KfGKgQ6YLicUWsgackkjNNKyowvLE-_yTJ2JwmxvUz7TXyEHn80z9Vrpw1I1_799xHD34_zwS-Srqiao8H-FxkHp4Fvxfu6jYeniKdUB-fya3OOqDp8ubexB3RWpgd5G7DZ6e7raWQBK2nUscxyKVs07C0yTM7W1iwjhg0csZuiNN396Wb8yV9udCPZT9UFihQmXVWg4-TVjkpqLGK77uDkw4VFtdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
این‌روزهااینستاگرام رو باز میکنی، همه نفری یدونه‌مجلس‌عروسی‌واسه‌رونالدو و جورجینا گرفتن؛ ولی این یکی واقعا تمیز و زیبا بود. ببینید حتما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/persiana_Soccer/27021" target="_blank">📅 22:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27020">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMc3kc_o-zonYw2jD29O5y48OFFKTMkiL98TLXwd12JHcmAVI17lkDpKA46cr-6-QryULNd89OgmgSoQogdBNGWtOLd6w_GHGwxjMzmDyK8F80Z-dAl_RhfdaAHTmohtNn_9CdRK6kv_XhwLCvaqEcVvn1iyzWr1HU64c1lnWL0EuHoq9arMRpSeSqrP4pIbXuuu7Hq2C6K9uyuL1eTEwfF8hTz5gR7krrRYFeea50F3vCOl1k7fUE5J87CuENyvvWz8iraIzh2C6PgvOXOL9hfWX7nG9T4BX__aS_ZNAAowZc_BhRnQleevLiqbx0qlX-oiubmzKrGJfnTjdYrVVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
باشگاه‌فجرسپاسی‌رقم رضایت‌نامه یادگار رستمی وینگر 22 ساله خود را 50 میلیارد تومان اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/persiana_Soccer/27020" target="_blank">📅 21:42 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27019">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1714deeba5.mp4?token=spf2VUk6AeGORy_npxgzggj7qRKLamPpyIC6OXaymnahLqMcL3bdBjwAwSO8K059s6gNVfdNiV3ZSapk2WXrdxSwFslzI5BrwzuARc_yVP1FysBjXKlWXJDr3KkanMVBJ3SLu6AVgoecV1D7b-Wrrb43KKdwjC-5g2jl_GF454xsOWabKu6eaPayTqCZNTLMRhC6SxHkPw2o4GgkS8BAnOH71KzYPyOMJstb7u-XnaGeLj62_rf16qDRotC6sJ6BmOSqeKqM006TZn5c5xaplvM7zLJUE_p0j9445Qx2V53Rh1RcPs3Zir0gvIY93I9ftd_nnBXoPw0lw-jYo437tDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1714deeba5.mp4?token=spf2VUk6AeGORy_npxgzggj7qRKLamPpyIC6OXaymnahLqMcL3bdBjwAwSO8K059s6gNVfdNiV3ZSapk2WXrdxSwFslzI5BrwzuARc_yVP1FysBjXKlWXJDr3KkanMVBJ3SLu6AVgoecV1D7b-Wrrb43KKdwjC-5g2jl_GF454xsOWabKu6eaPayTqCZNTLMRhC6SxHkPw2o4GgkS8BAnOH71KzYPyOMJstb7u-XnaGeLj62_rf16qDRotC6sJ6BmOSqeKqM006TZn5c5xaplvM7zLJUE_p0j9445Qx2V53Rh1RcPs3Zir0gvIY93I9ftd_nnBXoPw0lw-jYo437tDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
این‌روزهااینستاگرام رو باز میکنی، همه نفری یدونه‌مجلس‌عروسی‌واسه‌رونالدو و جورجینا گرفتن؛ ولی این یکی واقعا تمیز و زیبا بود. ببینید حتما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/persiana_Soccer/27019" target="_blank">📅 21:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27018">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jrp6_cEtOb7JlP30gJt8sX7zHmC8nPJjv77ZX0pPbyFGSa2-kRDq_t7e61zbx2q-mDYJl27pkC0F-qzXbI2CMNEVhjWQRRdZDFvwwRnl_JoZxWO8iPcGX-Nhqy3WNXQc7Kck8S_hQBZiMxizEQh54q7EcgHyGCZ1LXyoeMAW8j1Jm6Ko3FBH7uMWIQUB2AN2tAYG5_nDZ_CGb-ShZCQwiWaIJPsBnBMhLOM866x8abZNlMzFfJlGwHRwjVa-2DtFrI9lCNRrGrrxin1ZjZAbVRJlkh58XRE73HN5EzPn8CnKYXb-20ZmvCjhvlXwE-TIUui1UKYdbPGzpqwrVcONJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه گل گهرسیرجان‌رقم‌رضایت‌نامه امیرجعفری مدافع چپ 24ساله‌این‌باشگاه رو 70 میلیارد تومان اعلام کرده است. مهدی تارتار بشدت دنبال جذب این بازیکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/persiana_Soccer/27018" target="_blank">📅 20:56 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27016">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TCAur60NO-kvhfTDKw1XMVO-TM-e5DtDxqLR5TBIsK33Pft1Li_BAXZiiIci-begniYfYJvzAzZxqkKdXHAHbJT3Co1HtF9KETqD6Pq8yEI7Tb8NMeERO-7nrri4izXGguL6IkNV60pgOJZY_gNSNjZyr-jnYoUQT4LJ8eKsVApAim4CWdtxQtxiaVPSPjhQjAWppg8d_89bmxjpfsGqyhEAw46EG7apoIVPJQl0dF0KeLFLmbM4nHQ6TPzxN9_e0eo-Yz_IPBop1olJZOO7sqksxAAe2rNqy4z5AYW8-kLQJtMYp07rowA8uqBckMlw70LHQEukdLozPpuLu33HKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق صحبتی که با یکی از نزدیکان محمد جواد حسین‌نژاد داشتیم این‌بازیکن‌هم‌آمادگی خود را برای بازگشت به لیگ برتر اعلام کرده و به احتمال فراوان راهی یکی از دوتیم پرسپولیس یا استقلال میشود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/persiana_Soccer/27016" target="_blank">📅 20:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27015">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CY2ot23X7ytSPHeWlMXhOGPC8RJbT8LfIHf_Kjp7R4O5g5mFA29ftZnB9fjBTEY4IGX_uKscou_CilOZUYP3j5bhR0H4kG8CFwpN9jynMixi1MlHSUf1jEpJKbPb53wX0b0mGZoC_Z24vPmQSEjVhD-eD9UT6AzsDMvncKlxN7peMIeFc2g1jpJawu-q7LZvD3xDGNVPnpv3Ow_l4T0f8x4ea2H2zssN5P98C-01yHzLKMDxmwrjyZCllB4eLrsg2bj0STI63XFkFrrZVqUKDfQaVAFezryJCUK3lILJ92Coimqtffn7gmTxrae2pTKHr-PpTlYPVor21RlOxSOoqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو درحال‌آماده‌سازی مراسم ازدواج با جورجینا رودریگز برای هفته آینده در مادیرا است. این‌دونفر در کلیسای جامع فونچال رسما ازدواج خواهند کرد و سپس جشن‌ها برای مراسم پذیرایی بسیار خفن به هتل پنج‌ ستاره و لوکس ساوی پالاس منتقل می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/persiana_Soccer/27015" target="_blank">📅 20:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27014">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cxKPEnHg2XkoNVSVVNOtGe_Dhxha5T1no_UKTu3gPkTO7_Dw_YJJMqvZazJr82Kz1OtkZj-vN2UbTi1ZUOpa_Rhr1YJN7u2JD08U1saiPqEA2WgZjrk-nMIGtLMSlEtv_CyvN4KAsccafjGN_yfL6GCYe9Xea9BlaNxxtJ14MBZwN0JirYxvDhbYSx_l5Xf4lsjKumXchuzXtqLBmuirMJk7GWh-L8wPRW-KEMG11ggkcxUyjCkEEQGYdoxCq8d57Cw53eBfCXJncmiRnwMfMUzzgOyNOvZckhAnjEttgTu2Ir0Ey1oVVA7c63vLabXkse8EZVbxHe7YvyNeVXz10Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
ترکیب‌پرسپولیس برای دیدار دوستانه امروز ارزروم اسپور؛شاگردان‌تارتار فردا به‌تهران برمیگردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/persiana_Soccer/27014" target="_blank">📅 19:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27012">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c5f5546ea.mp4?token=Hto7zy8yd_lVHjdnOgTtbRUNRxLwz2pyjp09uj3nLr4RXTeTMGlMEeazb9NQPBBM6EPBMxrISrTbuRDKOOwvQYa2jYnG4p5GZmrlaJyDmhfyTMT49dT6oy7P8hLjURtMefnD2JYBqq_Uxs7nWtWCGBTqaGCcmlICdu1aZaft-gtYjkJOfJencYDAvtw8nfOw3-wgOmgO8RnQ1cJnvnKcT_5FSv9eoCvU7XBW9jiz2a4hJRg1gAHj6lLUChkX026X0tjzOGUTI9aoYBgPRtjJmh1cxhAbR6kZ5FTEfqxEeBns-GKXAUrLYzCW1DaPegAfJSfyUf4vFWjMoqaZjo350Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c5f5546ea.mp4?token=Hto7zy8yd_lVHjdnOgTtbRUNRxLwz2pyjp09uj3nLr4RXTeTMGlMEeazb9NQPBBM6EPBMxrISrTbuRDKOOwvQYa2jYnG4p5GZmrlaJyDmhfyTMT49dT6oy7P8hLjURtMefnD2JYBqq_Uxs7nWtWCGBTqaGCcmlICdu1aZaft-gtYjkJOfJencYDAvtw8nfOw3-wgOmgO8RnQ1cJnvnKcT_5FSv9eoCvU7XBW9jiz2a4hJRg1gAHj6lLUChkX026X0tjzOGUTI9aoYBgPRtjJmh1cxhAbR6kZ5FTEfqxEeBns-GKXAUrLYzCW1DaPegAfJSfyUf4vFWjMoqaZjo350Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
عشق و حال مهدی قایدی ستاره ملی پوش النصر امارات با پسر کوچولوش میلانِ عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/27012" target="_blank">📅 19:40 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27011">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bcsn07f_PBVe0wW1qRp7Rvn5dboTfJ3HLh20U_xApG_NzYUm96T13ZWKo28g2s4bDEIaBhmQUoRc4hvtm63zAR49HzWSOGqJTGXQiFYBJHWISOAKw6etp9Pbm_hwXI03jN-V5Zy_NlQtsNuF6TpWvW0HxDNk4eZPkTHidGeR5BDqlw44mODPnwYHgBQpMG3Q7ErX7Uy49-MwpgpcWA5twtGVGCsGXuxV3nOJZK9eP0vPrHjB-fYMGT9CXsB737_T2b0Ms0oyCSYwB-VxDors7OupbuUywgMXhsDRP4AYUb3KxM9hT9KUUzXO7Lk13SbbkgJFunwrzMnJf_LFo84swQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ ایجنت مهدی لیموچی ستاره 26 ساله سپاهان امروز باردیگربه‌پیمان‌حدادی اعلام کرده این بازیکن اماده‌عقدقرارداد باباشگاه پرسپولیس است و درصورتیکه‌سرخپوشان بتوانند رضایت نامه او رو از طلایی پوشان بگیرند لیموچی سرخپوش میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/27011" target="_blank">📅 19:00 · 11 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
