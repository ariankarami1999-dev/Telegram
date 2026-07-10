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
<img src="https://cdn4.telesco.pe/file/bxX24fpGpzD1IT84ZjRrbyD-jykMfcUgvVZGEjfUtKwW5SIY16NYAt5U11e6g5XdYE1DyagqT9I0bACtNzhjZqZNWscWfzQFQ-jTYgYDSbZkmKKegUunDxnSIhJVyfJoiWK_bHacvjY0Fr5b0wHF394syS6h9vkJhpHJElYqVFTTB0L2p8ywwzZZYjU3c4LSmlUwMJ7qFyAPO_Cej1iYGkBKp_VXPml9uoFUnJ0EPT70_woxeWjDFo0v1dVoy02ew4F-3FX3hnU5vDKDS6e5fFumCiXaMQcim2K_bxHvWsXN5FzChEKjTFwtEKrpxBjWHDR5hCPKeX4450-Q6PhfZg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.3K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-19 22:25:00</div>
<hr>

<div class="tg-post" id="msg-6018">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lbIJyOE2Zg99a7z3TD5mDWj0vjc1vH4vH6eeDCZB033bHtcto7zbvY8OM41MekdSJL9DlcS9mLECr4XoRiKdft09qQFx0vnI8Uf4DSB9UJ5SLtKNYr4kzEbFsDroDdylLGJ1uLB_MRRgKpUuLhaWn329PoFDM2Mf7VIe_Vfs2tbR3FlpSShbyJ6hYHVPN45B959Ufyq7LeVRhGgU4i9RBjDSuvUrTRx3kAfK39tQMR-B3y8NO69Z17tPQoOft3RC91injyqPAcnU69MuP_c5i290F9K3QcyL0s-jszxBquiXLylYWfTy2J4tucAQBOGLSqhVQS5QAUus7_jHfnFPmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علویه، خواهر بزرگش (ناتنی)  در سال ۱۳۹۳ در سن ۸۹ سالگی درگذشت.  ۳ سال قبلش، در ۱۳۹۰  علم‌الهدای معروف مشهد در یک سخنرانی گفت که زن حاج شیخ عباسعلی
😅
می‌دونید که علم الهدی اسم زنان رو نمیبره حتی اسم زنش رو روی قبرش هم ننوشت! (ببینید حاکمان ما کیا هستن!)  خلاصه…</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/farahmand_alipour/6018" target="_blank">📅 20:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6017">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CBCdTL9seDcNwGsIb89YYMmUWZ75YhupG5WpItG-REVUvZfiD6KHiROnXkLn4fzdNEvQCBsplLIerYuH0UMUBEtMsezM3MC7ZKK7Py0YFkm2H0O6mZei_Fnzbygt7tAnrp_QgM6h59w8uxsGJIyNVQN0aLBYMYZwuWWVtE_nnIqjCdwrYgb8nyJ4K2r6_6FmvF1cFmuGuqTGjxgGNBAjAkenwQxu9CHL-SNdywTVANS_otcnr7RB-hd3qv4e8yGeMKp9oah80UsGtFRxbWjhdqYY3e5LcKoObVpckCAzAsFgLiWr1fFP9YOF9Blgz6KLpZDuv4UTBUShsOAstb-pww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواد، پدر علی خامنه‌ای،  پیش از ازدواج با خدیجه (مادر علی خامنه‌ای)  یک ازدواج دیگه هم داشت و سه تا دختر داشت.  از خدیجه (مادر علی خامنه‌ای) هم ۴ پسر و یک دختر داشت. جمعا ۸ بچه بودند.  اون خانمی که ظاهرا خاطره ای گفت که «علی خامنه‌ای وقت به دنیا اومدن گفت…</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/farahmand_alipour/6017" target="_blank">📅 20:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6016">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">پدر خامنه‌ای، در کنار زن و بچه‌‌هاش غذا نمیخورد!  خامنه‌ای می‌نویسه که پدرشون در یک‌ اتاق مجزا شام میخورد،  مادرش برای پدر آبگوشت درست می‌کرد و اون رو توی اتاقش می‌برد اما مادر و فرزندان معمولا نان و ماست، یا نان و خرما میخوردن.   «ما بچه‌ها در اتاق دیگر لحظه‌شماری…</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/farahmand_alipour/6016" target="_blank">📅 20:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6015">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gB_jklWp-P3SyRXbm4_EDnMya7QubfMI49g1j4w_VhiPn-iZO2Evl0qL-0_yfAfFGW06qtFJ0UHnNf8VNKezps_esDctb0ISCH2P6bquT2fhd2L-LWktS049d0km2_qfc_tzlCR9l4PnCDawud2NIK3WyD1SKzbAZDNNSsI9Ag2I4XDPwulWsAhcmD5ckwtPta7cd4Q_2LgsjjzJuSBgaE4NfL6ji8a_T2wKx0RQoUsLXHxU_QD0i-XsiaHSvD88FEIKUiIeua4WC6dHLfzg3ljE_VPOoMVDG_dxu9S4sK-nc3_VHIwtLtU2D0qQOoBR2AhqMam6Ajzxy-v-rz5Knw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای و مادرش - تابستان ۶۰   علی خامنه‌ای از سوی دیگر، هر از گاه مجبور  به کتک کاری با همسالانش می شد که او را مسخره می‌کردند و نامش را «آشیخ خُردو» -به معنی شیخ کوچولو- گذاشته بودند.  در این تمسخر هم پدر نقش داشت که کودک خردسال را مجبور می‌کرد تا …</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farahmand_alipour/6015" target="_blank">📅 20:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6014">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tFLFj6blG066qOc9Vz59KMvvnEt9kXhpJ-qtpAmFfW5ICohqG4FNQbWoELS85GqFKPesMMQ0oIfeZTJVY-UBuixdjzb57WF9FRUwO7fSY_zE_YSTtvWkrwiIUm2vO2p_7aXcYiUh9MxrcFc9j22DyifsmU4IGvvMZCwovXGmVQUWCILGwMwwid2CfDJ8gyH-a898QpObWojN6z8_9nSXZslXvmd3cLOi3Mv1Tyvs1VE5qQFTsUJnUtIgorLz8krnFxK_6LS-3AeLXwgACCRvbgX0dymYpAbeS0kksqNXta6BKMCcSOREawZwACz_9ToLVmNrpjPs21FyGGKWgGaYDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای در کنار برادر بزرگ‌ترش محمد خامنه‌ای  علی خامنه‌ای در خاطراتش ار جمله روایت میکند که  او و برادرش محمد،  در هنگام درس پس دادن به پدرشان  (جواد خامنه‌ای)  که «دست‌ سنگینی» داشت، مرتب کتک می‌خوردند.  علی خامنه‌ای نه تنها برای اشتباهات خود،  که به…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farahmand_alipour/6014" target="_blank">📅 20:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6013">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DW3Y8wkErEwjwhOu146AJeeXna-1_Q0yQHyVoQUogvuEw84IQQWdhgrcwU80wv9tXG-1-1jTExHEOTwqgh0A15l5iYi9CWoppsIWSS_H_9MqlPO-ExhLP2LqfKuW7q3xDK4o2mdX_UoqYv7uPLz_u6ilcSEtzGMwSEIrDajTgLwW-XHDpJZvpULYX9Nmzv8qJtpy9PZuvcubBZXBTiJ92E6mS6ggwrjB_PG7OV5UKWrXZQCzHSFlIUOOE6JmN3GhWMWGj7vpEg5yt4XNt_lIBZmLVrNJDyAXQONcTbZ5wKvksbzWFVuWgRJTiWIsxnT8K7PmpZw3v0Ako2lvBbMjoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر خامنه‌ای - قبل از انقلاب   پدر خامنه‌ای فردی بسیار سخت‌گیر بود! جزو آخوندهایی بود که مخالف «برق» بود! و اجازه سیم کشی و‌برق کشی به خونه رو‌ نداد! اینه که در خاطرات خامنه‌ای اومده که از چراغ موشی استفاده می‌کردن ‌و مادرش معترض بوده که وضعشون از بقیه…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farahmand_alipour/6013" target="_blank">📅 19:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6012">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ftoT0vHGzBnDY_XOgrbM999A50vu0U3HCEN_VD19MRDlKDrZhadB94T8TrzcNVRt85obQoUoJlZuJK3fO9oEmw4y29FrXCXwTbD_uGmPLdIeQCkoycDhgOUajra1PbFAt9VMcv8n_IHQ3SHNWnGxGXjVLHBUO55RjZzf5ftn_evCkOxFDKjzuTt0TUvZjEPYx3OWH9NLgMRb4TmkwxQfeP7eyvtHE6V5ul4OKgv-3bLHn9tJpWBBpZHnTHEQ2wJppZGzm0FF5ydGr_3tDiyBeExW8qgAtWyFe2c8Um8pWnXv316Y1cQGaND5plapVjmBIXdW2g2xBfNyjqXDsYpiwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر خامنه‌ای - قبل از انقلاب
پدر خامنه‌ای فردی بسیار سخت‌گیر بود!
جزو آخوندهایی بود که مخالف «برق» بود!
و اجازه سیم کشی و‌برق کشی به خونه
رو‌ نداد! اینه که در خاطرات خامنه‌ای اومده که از چراغ موشی استفاده می‌کردن ‌و مادرش معترض بوده که وضعشون از بقیه آخوندهای مشهد هم بدتره!</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farahmand_alipour/6012" target="_blank">📅 19:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6011">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">اینکه خامنه‌ای گفته :« ما از زمان کودکی با پدیده مسخره کردن عمامه مواجه بودیم،  آنقدر کلمات تمسخر‌آمیز شنیدیم که این پدیده در نظر ما عادی شد.»   خمینی هم در سال ۱۳۵۸ در جمع روحانیون کُرد، دو تا خاطره تعریف کرد که روی وبسایتش هست. لینکش هم اینجاست .</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farahmand_alipour/6011" target="_blank">📅 19:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6010">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JBuHBmINNg4wiMez3F-XCUwCh4n-_2LP_GWmwRlvnv3TFyB8RtDkVdxb-Zy4nGNuP-wdA10DlFbZHZ3V7DqWPXgM6jJi_nBBZnfe_VWYMtMZVTwM3Gkw2PHhpNwx5Q94VeSu6SgJCCxIPXPNGYI1f0EMhCXR44ZpGDsZeziddZoIIatPBWIGUFywliuc8Ua_-t0R8rx1NXDW570NgtDN5LEjSln8aVO5c1ZPYPUopYboMTfzkUbascvXkreIKjppVfb7XzKleq3GoqDFwbxxxuEigMvroiMAWjN6zjiNAYNdzrFWaDGyALxHEazfkLoMoyO8bvmEuGzgrWQgGpGQCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای بارها و بارها در خاطراتش  اشاره کرده که چقدر از اینکه لباس آخوندی می‌پوشیده و مردم در زمان شاه  آخوندها رو مسخره و تحقیر میکردن در عذاب بوده.  چه در زمان کودکی که بقیه به خاطر  لباس اخوندی که می پوشیده مسخره‌‌‌اش میکردن، چه در جوانی   او در خاطراتش…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farahmand_alipour/6010" target="_blank">📅 19:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6009">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NN2fLb4cazVvpoyA91J3Xw1V91yDEY7pxYNgyUboOI9fXj91j597ISmxfcEJt_qEUY4Eh2hbwuM_F02Ox3-MqLHnZHt0fMpcP6qVafcVjRFKeAdOP41tExPMPlOR_FAbVXY6TkExty-hZSS58DfVrNyIx-ONpPI0hSn5r5zYv28Xqw3YcMw0ZcKS1d4VuQfoVSoZ-MFA1AI3sWnUVmzgndyX7JEmOz13aMv_PBYicl5pkYcshx58ot7S6HWN2qSBKY87Dy_t2yYzlrpoelwlEQCVAEx7zjN-2n3Ty1JYd8r0GIG1hRHOgavx1i1nkVK_UoB7ksQccoiVrr0GUQT5Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای بارها و بارها در خاطراتش
اشاره کرده که چقدر از اینکه لباس آخوندی می‌پوشیده و مردم در زمان شاه
آخوندها رو مسخره و تحقیر میکردن
در عذاب بوده.  چه در زمان کودکی که بقیه به خاطر
لباس اخوندی که می پوشیده مسخره‌‌‌اش میکردن، چه در جوانی
او در خاطراتش می‌نویسد : «یک روحیه عمومی ایجاد شده بود که و را مورد تحقیر و استهزا قرار میداد...
ما از زمان کودکی با پدیده مسخره کردن عمامه مواجه بودیم، آن قدر کلمات تمسخرآمیز شنیدیم که این پدیده در نظر ما عادی شده بود
... هیچ معممی چه کوچک و چه بزرگ از این پدیده در امان نمانده بود.»</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farahmand_alipour/6009" target="_blank">📅 19:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6006">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i5pP0lmx3WUstOIKRKK_l_UDOEul8FC-JWHpGrPa_axYQ2mDHF5ACRkp8s7tUlyk4BjRyAhePViQaFA-90HYT6bUFUvZGhy_moyO4eV5R0mpuW42xThDm5IdvZXoB5cM2SQjcpVPROftZWcPZhsLRTo3te_p1BnluZAEpkVgZ5RRN3A--N582SKvrBZZS1UBLWJo9-ca_wyEjMa6jMRN2Vrcrh2LoSApSMwp2fTZ0-NuDdGuFHjkeIyPcsgqqU6KGWd-cI4XDFrMmDuRjFXRGsSXjU1_qlNSIyTnJRefXCvnxWxVZAb7JgMiU8WNy0gktVsMNRHDRRkeLZYCXLDICA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CbsLCCtH71ZrpXCrC5283G3reQ0lrzIk8Ofdd7D28B3RSongqUvYtbtvyX3eAshVAwHeFDeakHAC3is3ItsUfGTzo-z2iJJJkwnCs2exCRj_gOUZ7e23JBeXzrJ4BX4cxN2Y-OUq_7_q-dHoEt9mFu2k1Q0VbSAtLnwRfkZkVJbO8qZXGWm5UBcWn98hEhUbMaHaxt_YyvjaicBeYaArxLK65cG4b6EipZDoFNBel3lg6LK_NCsTp4fVIswVayjyNEFD5oZWTNHzzuhDrFfC416d_h278MkunOXhb3xEfnPrxchETaRG6Tlc3nDnvcMr39BHI6MHvFwRBmjHlgRFvQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6c19fbc0a.mp4?token=Jme2LP2pLiozT4LeANJG6a2vw_i20l1S_gGa5v2WCKbUzCXL4l5LGAIp9zSOgCGZkNgNM8Fe0fN5cdwugQVhdE4hXSivJGfZwOKFhxsyibp5dfX3rrsl9XTudlcghHepur8N_7tni4c1EUkW0nul9DseUZII4gLxe17ULS-NmMl9H8FPg7GiAu_wOOsq6UlvBwkjRjY-vyllovjT8_2LTnbd730-iVGD1rIgIYX87ablxZHiaSY5BnDE_YL-1W9vtKO_7RgTFBDEjYZ8MWYWFHlXAB9zSvxw-lneaU4WjK1sUomCUAOjMvbwU7CRHE8oUaZ9edu0ofajc0gHfABHkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6c19fbc0a.mp4?token=Jme2LP2pLiozT4LeANJG6a2vw_i20l1S_gGa5v2WCKbUzCXL4l5LGAIp9zSOgCGZkNgNM8Fe0fN5cdwugQVhdE4hXSivJGfZwOKFhxsyibp5dfX3rrsl9XTudlcghHepur8N_7tni4c1EUkW0nul9DseUZII4gLxe17ULS-NmMl9H8FPg7GiAu_wOOsq6UlvBwkjRjY-vyllovjT8_2LTnbd730-iVGD1rIgIYX87ablxZHiaSY5BnDE_YL-1W9vtKO_7RgTFBDEjYZ8MWYWFHlXAB9zSvxw-lneaU4WjK1sUomCUAOjMvbwU7CRHE8oUaZ9edu0ofajc0gHfABHkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب در حرم امام‌رضا چه گذشت؟
از صبح رفته بودن حرم که تابوت خامنه‌ای رو ببین، ولی تابوت رو از در پشتی برده بودن، اینها هم شروع کرده بودن به اعتراض!
از ۹ شب تا ۱۲:۳۰!
اعتراضات که بالا گرفت،
به جایگاه حمله کردن و با خادم‌ها درگیر شدن.
بعد که آروم شدن بدون هیچ حرف اضافه‌‌ای، خادم‌ها رفتن و چراغ‌ها رو هم خاموش کردن و بهشون گفتن خوش‌اومدید، بفرمایید برید
😅
حکومت آخوندی، مدیریت آخوندی</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6006" target="_blank">📅 19:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6005">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=mDQjlTRqRN0zJeGqSL6LOwovQK7wW_eITT_cqHnlvI_cYaSgjM8iqFfZiCpHrMO0Au1zF2154iIZrnn06Hu05hQgJzHweYyyMausGGrREkheIVMemnuQ97ARaPUlE1wTfY0Sk-RFUINlz-su7NvVOvki1w3MSPN2KD8INpPBYTckOVUsNEVh7oN2UGIXgdfD_w7_6RbAXLFs8Qhc4cKc--EOrLS5vZMje4ARQxlGsZi-IAvQdYjK6mqRqWyGFm3UNv3Bcg0mdutireIPzcj1Us-N9oaKlFd3CoONXfOioQFiiCNeYvg5LblW4ZectUeZDAAYMFI-8o58J7T8vit3Q4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=mDQjlTRqRN0zJeGqSL6LOwovQK7wW_eITT_cqHnlvI_cYaSgjM8iqFfZiCpHrMO0Au1zF2154iIZrnn06Hu05hQgJzHweYyyMausGGrREkheIVMemnuQ97ARaPUlE1wTfY0Sk-RFUINlz-su7NvVOvki1w3MSPN2KD8INpPBYTckOVUsNEVh7oN2UGIXgdfD_w7_6RbAXLFs8Qhc4cKc--EOrLS5vZMje4ARQxlGsZi-IAvQdYjK6mqRqWyGFm3UNv3Bcg0mdutireIPzcj1Us-N9oaKlFd3CoONXfOioQFiiCNeYvg5LblW4ZectUeZDAAYMFI-8o58J7T8vit3Q4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا هم مسابقه طناب کشی برگزار شد</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6005" target="_blank">📅 13:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6004">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">اکسیوس به نقل از میانجی‌گران (پاکستان - قطر) : حمله جمهوری اسلامی به کشتی‌ها توسط بخشی از حکومت جمهوری اسلامی طراحی شد که مخالف تفاهم‌نامه با آمریکا بودند.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6004" target="_blank">📅 10:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6002">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/snnzMcz3inFmx6TanG6GRCd7O9p-D-ITlYAnw1PO4pKhyTt9TcHO75KRhdMUBBV3y-9h84lyQeZQ_bQEydzSFmi8B2jDyz3vaIPy-EY8vtx7mkIG6gTtgjxrlkeW6I7OX7JK56UMSD2r88bFsy_EguWzvxYwAVvYh2o0XJDKWlksI-VTqaurAUMFvbWRXI1PVjAWQ4eLDOW75Y9WmMcYtM9y6WD78p5DmtVEiZsMzRn6MJA6HQJ-Kh5qmTwvEErLU96wwVkia6sSK-_hYlFGbOfQwtghUEQFPOoiLt6NjA9vgHY7UBswCXnUmifw0ulJoeXN_rXsy1AXxJSnAI8Gow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f2581pEOawJV4mFu1HSOkfAfRRmx88xCqz9n_xBfcTZIT6BqUIwdK-sU5_zsA1F5lqeIc05FAY1PqR5RdLZN7XeSfaMtSI8rhEpb8eY_iMU9FkEv8Evfws39KOLkyAO926Lqy-jhTG3dssgp1yfEkNPMJl9-WDUG9aVRi59IDnausAglgx1DN9b5xf2Q1-6qZnZSyY5IfUDSES9TKJX-5UUDfQ83HG5dtv-6bcyiEAlnYS2HEFXPmkOYGFYJkyhenBTO-MiHCsav0ZwU1hiwiGeQm9URhdH4NoKYQpMQbUw7V8nzk_YgMxJ1qdtWaj9PeoDrm5c9d8jgdHg0DiCoHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کارشناسان و منابع رسمی شما  که این آمار و اعداد رو درآوردند، احتمالا همون‌هایی هستن که به خامنه‌ای گفتن در سراسر دنیا دارند «سلام فرمانده» رو میخونن و خودش اومد اینو گفت!  همونجایی هستن  که بهش گفته بودن  نفت آمریکا در ۲۰۲۱ تموم میشه امروزه   در ۲۰۲۶ آمریکا…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6002" target="_blank">📅 09:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6000">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R2naEIcL2NC_h6Fjt8sDJBD7SUb03fbu2o-Z0nrEx2xvNue8iRggYWC70qMOVVxYl86wxs39FYSHBxsIuXkXQ1VLoLwYU1vtRyBYW-Z-SyYX-PNdvdbFdOp26X1f9hB57QOkZKzD7tIzifSZOTkvJx29mVIbJhv36r70qC4JjlgeeYqGNbLzfrRWehBLGNty3Eqe2HFydwGdKPLLCaswJ9Gfs0QsaygkGUF1JDbne0Ees3ztu46L0o6FzNzqHBl_yODLEjdhAnRQH5u98Whn6mvIoKyg_k0W8fhabRSDxx5BlqbNjRix5hf7sV9bbC2SwrmxgdHuh8asSqpTWNKQzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/501e9261a0.mp4?token=PIAjzFfeC6s3zJ_k7g0EflWH6l5gRMQ-6B5wPok1d6GW-cMsfP7NasuhFI8dg5dlowTUrsjfFSaWdze9NTI5Hay8VKP3VjVqVCWLKJK7vMIXRSg2kqDQajXJnMu3Uj6jzH2cA2gJBzePgW3n8UuOvaXIc5dFSQa1x9OAJ_vHNEYb2Y90r87XEiMYDZJP2TRHOchMWcbKaVhkzvSEWgFugiFpo10ft0v3PPAue8d8mRYfKGoC28deKYXeP7TUTb54BArFCFImwZ5amn0jUgrzBJJFMFlkU3a71-RTDMe6IZ_YPT1CgvV93a-LMvTZunRVnZokZdttfAKRHrA177Fqli2_fLbB2uW6Q92rWo33maiZp73yFMdtvOTMCGwVKGzE7rYHJx3yXXCpOONc_pxA0OoN-TcRu6rQC0yucnz6pCSFmlRkUEjJYkojg7OvgwiCPAlnAzWM-FpDO2PGdJcJDmul3mlPkGmJweyBILOBnFhLXmdixaTm8ZGonO_km7-ZcE_aL5fILWrtLxyLshlzi8znL3dyrXjlOEdXKsuvnCodgEJF6wxSOmQJLiuzt-t7dmqOd1vxfKy5WMcoD4AZzdGYHdGlz_Y3hOZrb7Cw44UklTSg5JCDNeCERw5EBOFdohp741o6ajUW_zPZsnTNi3WpnN3p-BXfM585zbVjsuU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/501e9261a0.mp4?token=PIAjzFfeC6s3zJ_k7g0EflWH6l5gRMQ-6B5wPok1d6GW-cMsfP7NasuhFI8dg5dlowTUrsjfFSaWdze9NTI5Hay8VKP3VjVqVCWLKJK7vMIXRSg2kqDQajXJnMu3Uj6jzH2cA2gJBzePgW3n8UuOvaXIc5dFSQa1x9OAJ_vHNEYb2Y90r87XEiMYDZJP2TRHOchMWcbKaVhkzvSEWgFugiFpo10ft0v3PPAue8d8mRYfKGoC28deKYXeP7TUTb54BArFCFImwZ5amn0jUgrzBJJFMFlkU3a71-RTDMe6IZ_YPT1CgvV93a-LMvTZunRVnZokZdttfAKRHrA177Fqli2_fLbB2uW6Q92rWo33maiZp73yFMdtvOTMCGwVKGzE7rYHJx3yXXCpOONc_pxA0OoN-TcRu6rQC0yucnz6pCSFmlRkUEjJYkojg7OvgwiCPAlnAzWM-FpDO2PGdJcJDmul3mlPkGmJweyBILOBnFhLXmdixaTm8ZGonO_km7-ZcE_aL5fILWrtLxyLshlzi8znL3dyrXjlOEdXKsuvnCodgEJF6wxSOmQJLiuzt-t7dmqOd1vxfKy5WMcoD4AZzdGYHdGlz_Y3hOZrb7Cw44UklTSg5JCDNeCERw5EBOFdohp741o6ajUW_zPZsnTNi3WpnN3p-BXfM585zbVjsuU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناسان و منابع رسمی شما
که این آمار و اعداد رو درآوردند، احتمالا همون‌هایی هستن که به خامنه‌ای گفتن در سراسر دنیا دارند «سلام فرمانده» رو میخونن و خودش اومد اینو گفت!
همونجایی هستن
که بهش گفته بودن
نفت آمریکا در ۲۰۲۱ تموم میشه امروزه
در ۲۰۲۶ آمریکا بزرگ‌ترین تولید کننده
نفت جهانه!!
سال ۱۳۸۷ گفت بر اساس محاسبات کارشناس‌ها تا چند سال دیگه  دلار و یورو نابود میشن، در عوض و در عمل این ریال بود که نابود شد!
کلا محاسبات و آمارهای شما همیشه خیلی دقیقه!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6000" target="_blank">📅 09:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5999">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=qKuTfaYk5kX3pTKxI8VAA2VouOmw55mnpsNSda0nEw-KC7gQpCkt9rj3cNvJbUDno_ymPfEtyf8BvL8XQMbX7nnWn3EoNavZbpCEVmWO5d8LMdf4SaHYFWimSQM6aJ3fO7MQYOxVvAuOzY2OnvkBpPW0nkwrmw_VT1qIvJ_0_UwSkB4ld_2cIo-4D0iFo6bvNf9eyVxguwZSQPnVxRwKraiFFcZOXTYk8Rlz38Bbq1F1HqrHHIigqT3KnnbhiKLjSIXOeYatf9tZKbioMhnaxCdXkbXCO5yUrxxjtfctaaO9c5T53Er3V7XMhBVu1vnrci9klhoRGNybHaNQzad_bxf_M3bkOuM-jE11yUAJ9-qmIvMnttSXlbFghOOwfKvAINnNVpeAr-0_M-fmgS_eBAJfeim2R0P5SXTE6_gH-HuRs1v7EOwDLZa9fzbOZoFuS-Q8-EUwlFPQT9VXY5lQRPjAOaeo0o4zeDMvhtbv4Pg9mgx3slPFHZ1zTJWOq82z5J7PtC6WHRaPryeOGha4pB_49SUklw18muLievnm9GQiHKHjNkS6nJ47GwLsf7My9CaYeusmscjKUMkqzsQD4aMGcsTQm6TuNnc02WQfxx_TuUpWeWFWuwbGuswUvrhWB3-vn30NuVc2qjYtzuSd9kOysyWnbM_96Uqvrp1i5eY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=qKuTfaYk5kX3pTKxI8VAA2VouOmw55mnpsNSda0nEw-KC7gQpCkt9rj3cNvJbUDno_ymPfEtyf8BvL8XQMbX7nnWn3EoNavZbpCEVmWO5d8LMdf4SaHYFWimSQM6aJ3fO7MQYOxVvAuOzY2OnvkBpPW0nkwrmw_VT1qIvJ_0_UwSkB4ld_2cIo-4D0iFo6bvNf9eyVxguwZSQPnVxRwKraiFFcZOXTYk8Rlz38Bbq1F1HqrHHIigqT3KnnbhiKLjSIXOeYatf9tZKbioMhnaxCdXkbXCO5yUrxxjtfctaaO9c5T53Er3V7XMhBVu1vnrci9klhoRGNybHaNQzad_bxf_M3bkOuM-jE11yUAJ9-qmIvMnttSXlbFghOOwfKvAINnNVpeAr-0_M-fmgS_eBAJfeim2R0P5SXTE6_gH-HuRs1v7EOwDLZa9fzbOZoFuS-Q8-EUwlFPQT9VXY5lQRPjAOaeo0o4zeDMvhtbv4Pg9mgx3slPFHZ1zTJWOq82z5J7PtC6WHRaPryeOGha4pB_49SUklw18muLievnm9GQiHKHjNkS6nJ47GwLsf7My9CaYeusmscjKUMkqzsQD4aMGcsTQm6TuNnc02WQfxx_TuUpWeWFWuwbGuswUvrhWB3-vn30NuVc2qjYtzuSd9kOysyWnbM_96Uqvrp1i5eY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرگ بر دیکتاتور یک شعار نبود
آرزوی یک ایران بود، برای سالیان طولانی !</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5999" target="_blank">📅 09:19 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5998">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">مداحان اختصاصی خامنه‌ای،
که توی هواپیمای اختصاصی که تابوت خامنه‌ای بود، از عراق بردنشون مشهد.
نقش «مداح» چیه؟ مدح قدرت رو بگه
و بگه شما بزنید توی سرتون!
اگه یه عده از شما نپذیره بزنه توی سر خودش
هم حکومت میزنه توی سرش و سرکوبش میکنه.
اینه وضع جمهوری تباه اسلامی</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5998" target="_blank">📅 09:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5997">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uwCv_QtBKt7KINfPPK32jAHD-qZbLZETa2wdbUCoqed5YleR3nmpqYCaDOThemR5daMaDExKgsicw5ZxAehUjc7ElN-XW1GnM0YbQ0fjBbJz4EqWixuL9sDdSCHNuU6BQZpKwQOt9EFA-G7jlajIjI0GagqgVNRRGjovtTotypy6NGcFIJOH5P2kn-Ah623CvFoa3P61bl8KPquy5DueUK82fiZOhXCeoMq2BwZGjzM1oZQfpetp0wX4N-AM9xvTDb31DP7izN4pEaQmGgtNzieRUI9uu8i-DFz73-Db-NdT-_DhsqJeG4bN-_v9CzsRwmyZE__Bu3LW1Z6lKbUYug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سی‌ان‌ان : اسرائیل اطلاعاتی در اختیار
آمریکا قرار داده که نشون میده
جمهوری اسلامی طرحی برای ترور
ترامپ در دست داشته.
(این چند روزه در مراسم هم پلاکاردهای
بزرگی به انگلیسی در دست داشتن و خواستار این‌ کار شده بود، مجریان تلویزیون، مداحان و روزنامه کیهان هم همگی صراحتا خواستار این کار شده بودند.
ترامپ نیز در ترکیه، زمانی که از تفاهم نامه خارج شد، حداقل ۳ بار گفت در لیست هدف ج‌ا قرار دارد.)</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5997" target="_blank">📅 09:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5996">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های حکومتی از حمله مسلحانه به بسیجی‌ها در مشهد خبر می‌دهند</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5996" target="_blank">📅 01:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5995">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">فرانسه ۲ مراکش ۰
دقیقه ۶۵ بازی
تیم فرانسه در ۵ دقیقه دو گل زد</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5995" target="_blank">📅 01:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5994">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NLt7piwegmwr9yR1tpqHsuMNyxHBTpGQt9S0Hg0hPfau8WfCLj_OTwIe5NuvGIFxRpe6CjLfCSk7zH7aZScDOmpMbhae7RK7mYyzhn3mILofWCix87ipyc5DmupNSND5WfaBPMwB5qSnjjblsiBeMbmIfM2tGVVzCbGAMPnWBPdukf0dhi2EicwTNi2FDGyTQyCMs8kx3UQmDvJqgLClzYHPu94U7m-Lp174GmU7LcPmlp_CW9tIM48uc_efUW4m-tBY_foioNAdztHrTmBM5XQ3LWY7iXfrrN3ijETGAtUpZkd9nIjUfq7BCKL_cXMKBtU6tat31cfG-Xv5c3Cruw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام - فرماندهی مرکزی ایالات متحده:
‏
🚫
ادعا: رسانه‌های حکومتی ایران ادعا می‌کنند که عبور و مرور از تنگه هرمز فقط از طریق مسیرهای تعیین‌شده توسط  ایران مجاز است.
‏
✅
حقیقت: ایران تنگه هرمز را کنترل نمی‌کند. از اوایل ماه مه، نیروهای آمریکایی به تسهیل عبور موفقیت‌آمیز بیش از ۸۰۰ کشتی تجاری و ۳۸۰ میلیون بشکه نفت خام از طریق این کریدور حیاتی تجارت بین‌المللی کمک کرده‌اند.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5994" target="_blank">📅 00:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5993">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vd6p0RYB16WKVQj7SHNDXTB13XdIXf51Fb8LM-cTD_Q5CiwNJqLSk7OR7Cq4mMbTBbM8180-_Lee5SIq5loK3XSvkFnHRHctvBDUDIMY2gD64FYsn0bvmjJujFasZVjly-AarstqkjY_JRGKItyNa0ZSbm6w8VFlAE_MkwNJChPbsp-z4mIYDq3454hhg_u-yuGe1JhrmEbf3fpzlhqRj3D1T9MggQEkKYnlE_fyM_Ht1IrrfXOUZ4W0vLSdJWTDVOWPOlqnIL0l12nzWDOE96niZBImmUaXdyCdJkKvLeBOC8_wh7TYBDoWBPywOBMZ0rHAZeSp9PZZP2IDm6UmAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های حکومتی از حمله مسلحانه به بسیجی‌ها در مشهد خبر می‌دهند</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5993" target="_blank">📅 00:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5992">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">فرماندار کنارک از وقوع دو انفجار در منطقه نظامی نیروی دریایی این شهرستان خبر داد و گفت:
این منطقه شامگاه پنجشنبه در دو مرحله هدف حمله جنگنده‌های دشمن قرار گرفت.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5992" target="_blank">📅 23:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5991">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">صدا و سیما : هیچ انفجاری در شهرهای بندرعباس، قشم، سیریک یا جاسک شنیده نشده است.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5991" target="_blank">📅 23:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5990">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
گزارش‌هایی از یک ترور هدفمند در اهواز.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5990" target="_blank">📅 23:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5989">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=EbLxNPjS6as2eL261gUNvGE36aLzoYhcbyAZmW7-j7ikcxyxv6-sU_OadExQlKaYRThyv9CjvCcJ4Q05QtDFiI-t-I8CW6zf4ISlsmINX0MuvMp9liV1noFBFv-pTEMSQLVuQeRU9libKxPKcyxWqzBalReCSlkGad1rbhEN-FxoEXjQqlsmstpwJbXYH2f6qU3bhsbuGN28oMaPXthI0e5UgRyCwCyMST-i13-EJ3kktwb-YS_9Dw6RXg2YJVky2XytqX-BzShc-isHxFHL2Fh0olURVQYcYzrPYyygyHkxsE_HjtHBdnvWbAGucxlMu5XzRU0aPq_3AkuZq8L4gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=EbLxNPjS6as2eL261gUNvGE36aLzoYhcbyAZmW7-j7ikcxyxv6-sU_OadExQlKaYRThyv9CjvCcJ4Q05QtDFiI-t-I8CW6zf4ISlsmINX0MuvMp9liV1noFBFv-pTEMSQLVuQeRU9libKxPKcyxWqzBalReCSlkGad1rbhEN-FxoEXjQqlsmstpwJbXYH2f6qU3bhsbuGN28oMaPXthI0e5UgRyCwCyMST-i13-EJ3kktwb-YS_9Dw6RXg2YJVky2XytqX-BzShc-isHxFHL2Fh0olURVQYcYzrPYyygyHkxsE_HjtHBdnvWbAGucxlMu5XzRU0aPq_3AkuZq8L4gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌‌های مجری شبکه سه و تهدید ترامپ</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5989" target="_blank">📅 22:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5988">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dcPSG-OzsarDL4h868CyZeapgIOzHQIa6OwJcRHGXKAIGZdk50NUB8wkoYaVe1Wur3FkvGFpOv-LGEb2NV0MvNraJz_i1PkmZWzDBhGdDT6i0P5p4HVA_Jo-81xJ3MADUWpMSOrK6omqK7u5WaVsGqxjO--ZFDh-NiZn0tNehnDYZrxcgKOp1GY2ZPcKzn3n19EgQXnkH7YII9xrNDcar_HD11RafJShGao4OcSjSU3FhO74_rmrSuhgPXFn5nApTySs9EMFw320R0WoPm4Nwi4uO8LMlJzceBkzjJmwq2R0dU9jJ9BgqCqnI8SREObfmMx3PFJFDrTqBVbHBE262A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گمانه‌زنی ‌برخی رسانه‌ها:
حملات امشب احتمالا کار
کویت و یا بحرین است و احتمالا
حملاتی موشکی به ایران صورت گرفته.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5988" target="_blank">📅 22:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5987">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🚨
آکسیوس و العربیه به نقل از منابع خود می گویند امریکا امشب حمله ای را به خاک ایران انجام نداده است .
ممکن است حملات توسط کشور ثالثی انجام شده باشد یا صدای شلیک موشک های ضد کشتی ایرانی به سمت اهدافی در دریا باشد .
یک مقام آمریکایی هم همین موضوع را به سی‌ان‌ان گفته.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5987" target="_blank">📅 22:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5986">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fffbd82aa6.mp4?token=n2SlgkYVypH6yzKj1dlpoUidc2XOpibiVVSSEBiodkg2gC7OjyEPTv3ZL4hhgIPfX20PyYVabL0yYmOScHi6vmJd95FpMQq-9PJYdOIsqdViPmsi-qYNprYujKEr3eEYCCQ9QlTdGBEEYvCCShY6VIfDwPAMbVkR4753wfaeq5YgIdbLpOvMD4quevF2CmZy5he7IAZUBVgiCiOqErJdvKs74VlRWeEqusFcyFrXfa0Z3WbPY9z2MSJ3l5QYzn7U4-VHiMhzWYbtaY7GfDOznB2odKZLYRkjs_SOehQuxkow_f9YwlSnVuHwiKmq6lNeSJaotPd3TefbNVE3XLWWUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fffbd82aa6.mp4?token=n2SlgkYVypH6yzKj1dlpoUidc2XOpibiVVSSEBiodkg2gC7OjyEPTv3ZL4hhgIPfX20PyYVabL0yYmOScHi6vmJd95FpMQq-9PJYdOIsqdViPmsi-qYNprYujKEr3eEYCCQ9QlTdGBEEYvCCShY6VIfDwPAMbVkR4753wfaeq5YgIdbLpOvMD4quevF2CmZy5he7IAZUBVgiCiOqErJdvKs74VlRWeEqusFcyFrXfa0Z3WbPY9z2MSJ3l5QYzn7U4-VHiMhzWYbtaY7GfDOznB2odKZLYRkjs_SOehQuxkow_f9YwlSnVuHwiKmq6lNeSJaotPd3TefbNVE3XLWWUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا در مشهد هم دعوا شد :)
چند بار زیر این تابوت دعوا شد؟
توی میکروفون به نیروی خودشون میگه خودت رو کنترل کن!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5986" target="_blank">📅 22:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5985">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5985" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5984">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A3ffMPYyaemnXI5YnQlDGNEfkrRpCDAgtDEENHe1w-hRL4Un38Tq8lFx9FD9WOSuFbTWoXR8colUktJoCsCuL6OlwY2BlBQPgV0w8U6JtQGWp7KRQJyNTA5deJ1r4lUdYxyfch_j0ETEtbLn0DnUv2GoVTJKtrlSPbaMb8fNs1PeGf_bPXB2L6p-ONzFG18EdR3UEB3CT4IEQ05xT0mdRjCDlZcHUBepA_p49rYSOJnMpouysUEJwBhcvn-5-Cr4S93iRhr0ViQKSrEiFB6ElqkA4Pb2juqluNL4Qd_-e69faH2ST-fsvenJldmQ2B4Y6cDrfdzsX5dC0j2rd-djAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آماده سازی قبر خامنه‌ای در مشهد همزمان با حملات آمریکا به جنوب.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5984" target="_blank">📅 21:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5983">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5983" target="_blank">📅 21:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5982">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5982" target="_blank">📅 21:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5981">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">‏پر از خون دو دیده پر از کینه سر…
‏شش‌ماه از کشتار دی‌ماه گذشت.
🖤</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5981" target="_blank">📅 21:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5980">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCNA7uU6GAZFIeok8-XeR-w33HGBqwfqr2IEy6H_6qrpmCci6E070FXGpjeM0P2bMiRdJNjNzCJ-T0PG8yvL1bJ3UGpNv6qYAhSkhdV-BkqxaD1MPGjPwBcJOsgDr-K_8-KIrSI2169A15lPE_xuh0Hvt52Nz3kgvl4kEEyF56Z3QEBYsd0Skrwl5-f_g-PvCWA4bK7t4TM86bPoeX2AYlXEE47M4qh_X6KVtKeEv18Qg6FJuHiLjR5a8KFDviJUhdubJsfFZHWo8K-sRiGBG8QF5Hlc27qp3mEbI6KgaAdzGSVUVr2azY61vr1IkJ_H3PblfZDKlbfIoVIX2uoVuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2075261040867037280?s=46</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5980" target="_blank">📅 20:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5979">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=chrbI9oYj_FJrh0PBO61RMcSCS2ZK58-2sA4yCU-5AjET7Yr1hzpCQcJKDg-bnAwGf07wGmosEZXS4mbH09HFQeUQi7FXtndD34BXWuY7rsMcdf0lbPvcE2-Q1cSlg1EX5tvn3QW4E1i5qejYapztj8I-45b41yP1FMTbY7VuBg3UWmSPLtOgNYo9HAchkJP_Vf54UgKQOS6BpINczBCKIJI_oSBJKCOAkxI0LtTYnLKqTaVl0Qi0lQIih-PfQSnahcm0SB_t6I-pfq0xiQat-y9tVhnM7ZegIXhHNsIWuebQc-0dv5tbRm7E3fIUk3bAh0LSnhbQ87peI8kvVnotg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=chrbI9oYj_FJrh0PBO61RMcSCS2ZK58-2sA4yCU-5AjET7Yr1hzpCQcJKDg-bnAwGf07wGmosEZXS4mbH09HFQeUQi7FXtndD34BXWuY7rsMcdf0lbPvcE2-Q1cSlg1EX5tvn3QW4E1i5qejYapztj8I-45b41yP1FMTbY7VuBg3UWmSPLtOgNYo9HAchkJP_Vf54UgKQOS6BpINczBCKIJI_oSBJKCOAkxI0LtTYnLKqTaVl0Qi0lQIih-PfQSnahcm0SB_t6I-pfq0xiQat-y9tVhnM7ZegIXhHNsIWuebQc-0dv5tbRm7E3fIUk3bAh0LSnhbQ87peI8kvVnotg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربها در حال آماده کردن مراکش  برای بازی امشب مقابل فرانسه  امشب چه فرانسه ببره، چه مراکش  مسلمین به خدمت پاریس خواهند رسید :)</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5979" target="_blank">📅 19:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5978">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=pGkQ2zJZkcWO3JIbaI45xqP8nw-XoLa9yovUlQd6v545Lfn5eiUhhAu6uF4JEgMcMD2Kb_hpoo1sQuuz_GVlhE-58SIEIWmgB6ie8ArT-DnpFRoFvfN9CUOgexJV50VewSg4q413Wh0gT_JtE-kmZaaP3xwb-JYVPL7upLTQACJxUc_YGscVMoJxaWiU3GMXZXzZhjIZJN33_zt0nbS_HISWSEsOuoeTZ7BFjYAGNzstkXmfHzP9g0pFUK-eLHae__7_y3ckw6fq9SJd5lnfYyxNfNr_uJazUcj0mCNmGIFiq9HQeMzNiOreWBtvkGQ6SaQMCCuvnrXkWT_voaBWag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=pGkQ2zJZkcWO3JIbaI45xqP8nw-XoLa9yovUlQd6v545Lfn5eiUhhAu6uF4JEgMcMD2Kb_hpoo1sQuuz_GVlhE-58SIEIWmgB6ie8ArT-DnpFRoFvfN9CUOgexJV50VewSg4q413Wh0gT_JtE-kmZaaP3xwb-JYVPL7upLTQACJxUc_YGscVMoJxaWiU3GMXZXzZhjIZJN33_zt0nbS_HISWSEsOuoeTZ7BFjYAGNzstkXmfHzP9g0pFUK-eLHae__7_y3ckw6fq9SJd5lnfYyxNfNr_uJazUcj0mCNmGIFiq9HQeMzNiOreWBtvkGQ6SaQMCCuvnrXkWT_voaBWag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربها در حال آماده کردن مراکش
برای بازی امشب مقابل فرانسه
امشب چه فرانسه ببره، چه مراکش
مسلمین به خدمت پاریس خواهند رسید :)</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5978" target="_blank">📅 19:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5976">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=k3qI3egErTBcUUe_qBMB-zdGTKvCpEoNXIh-9Wv6tzfAnPWO3REFCX0xtBtqxA-Zdxs_g08mPgK7ZI-YhLpHlKu_0gYMTQ5xoeBMIXh-7RD8OQGtevSjlV4-ZeXDsfKJmreM9RB5d-5iPijqQVIUgRZh8FA2zfYjYTET_ppR83bFFijbqo9nE1bT_nB5tZTqvrUch14ewPxUo0DP9MRrp_25wfHl6Xx8Qvl4KqRwaK0ezWmXPL5-FMU40EVBJJ9szoY4ghn-yKD2XhyjxhOjOojM07kLfO6gPAI5UAJo4gpULObwMZHdG5bjfAA6Bza30GUVksTJtDbHtVnRxfrkC06ayeBAUiucfF2GwGH2VnX3Z8-ahCYCWkFyis1Q-KHGcpmXG1NVoS7Ltv3N1hyO6tMN1okAgn9xnJ53qJZf6wRaKJBGpNjl-5-Pqr42LoIwibpJ4gUYTEWrL-NlT5YNOXUOcn7xv1MnRdd_b3ujv2dV9qsdHwm4s0B0SkSy5Av8A-ig9enm1n4R-JGDpD8Knx6g8FJW-PK3ltIXw4c-jvbhDCsx3L06PP93ud8GYstdhqepfUts4um9toereAN_42zjThCHwfhMLRutCrHi_ou2xlNnz8U94rp4MmSCBFFcLqTYfRgirBIhCocxT0B0eSYLqMLcnTe2C92crlzW5ic" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=k3qI3egErTBcUUe_qBMB-zdGTKvCpEoNXIh-9Wv6tzfAnPWO3REFCX0xtBtqxA-Zdxs_g08mPgK7ZI-YhLpHlKu_0gYMTQ5xoeBMIXh-7RD8OQGtevSjlV4-ZeXDsfKJmreM9RB5d-5iPijqQVIUgRZh8FA2zfYjYTET_ppR83bFFijbqo9nE1bT_nB5tZTqvrUch14ewPxUo0DP9MRrp_25wfHl6Xx8Qvl4KqRwaK0ezWmXPL5-FMU40EVBJJ9szoY4ghn-yKD2XhyjxhOjOojM07kLfO6gPAI5UAJo4gpULObwMZHdG5bjfAA6Bza30GUVksTJtDbHtVnRxfrkC06ayeBAUiucfF2GwGH2VnX3Z8-ahCYCWkFyis1Q-KHGcpmXG1NVoS7Ltv3N1hyO6tMN1okAgn9xnJ53qJZf6wRaKJBGpNjl-5-Pqr42LoIwibpJ4gUYTEWrL-NlT5YNOXUOcn7xv1MnRdd_b3ujv2dV9qsdHwm4s0B0SkSy5Av8A-ig9enm1n4R-JGDpD8Knx6g8FJW-PK3ltIXw4c-jvbhDCsx3L06PP93ud8GYstdhqepfUts4um9toereAN_42zjThCHwfhMLRutCrHi_ou2xlNnz8U94rp4MmSCBFFcLqTYfRgirBIhCocxT0B0eSYLqMLcnTe2C92crlzW5ic" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرچم روی تابوتش رو هم کندن و یکی دوبار هم تابوت رو زیر و رو کردن</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5976" target="_blank">📅 18:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5975">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kBXtjCnsOu03QIHJugN9mJQcPn1LQZ14aihgRYg0w5Ump05tQ4kDgzbV7gwz5W9eas1CZB4G3o_qLyh3WIVXxlCJLUUuPu5MAtTFYJG_ag8AjzJFwx1qI998-gZpJ6Nr3zdmF65TvgKF5kvEebmSsV-jUabvFSJ64_kd7Oob7-ZJXl3Hxn5y6OLPEiOu5mo38r2Nx7b_A32KEGcX1QIVPunIMw9yjcTTMn3i8Rp1Y-fTQJ_B6nZP081mlWOoa95jNdGQDhVY_LfYs0dvaSYKhZhK8Yv82HcVJXT5CU4mLY-wl5VEpIaoEilKrtyEi7fD_J7j8_joUNSCBYwQ3IwToQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمد وحیدی که الان قدرتمندترین چهره نظامی ج‌ا است.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5975" target="_blank">📅 15:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5974">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nKPSSujH0eCIYk5Lx1qzPytNZuRAQhAlwNsx0jK_1ZCV3SB8Sjh-6eDooB8rm7YZnjq__gi7oNuwo5NAQNV18YZak1yBPMQHJLQtZNuQGJkIJzIIM4wL00VPrmmnzJWQOykkk8JrIrsRdVndr_SiIBrdFW3Os9NWjDjsSjLPyJUjKwdmbfQ44T9lGpCtEJishI1vE8ZdPSyOzKyA49aFGrRFsbX3yueKG2F1avuUveMYjpSZMoaY8ofGRrR7ikv8OX7cfTujdLWXVcmfl_4sxOa7FsujNdwHrAWgdc_ldpq0gIvubqfvzBW4BX8nXbc_tfmsQCg1ntL8WSgW9wBs5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب با اینکه حملات متوجه شهرهای جنوبی بود، به یک پل راه‌آهن در شمال کشور حمله شد.
در ماه‌های اخیر، جمهوری اسلامی حساب ویژه‌ای روی این مسیر ارتباطی باز کرده بود، هم برای ارتباط با روسیه و هم برای ارتباط با چین.
حجم مبادلات هم ۶ برابر شده بود به ویژه پس
از اعمال محاصره دریایی توسط آمریکا.
فکر نکنم تعمیر این پل ، خیلی زمان ببره.
بیشتر یک اختلال چند روزه خواهد بود.
هدف آمریکا هم بیشتر ارسال یک پیام بود
که جنوب رو محاصره می‌کنیم و می‌تونیم مسیرهای دیگه رو هم از کار بندازیم،
اگه قرار باشه شما مسیر تنگه هرمز رو ناامن کنید.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/5974" target="_blank">📅 12:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5973">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CeRKmybuHIvIuv4SFET1OUerpXl_XKt11tl2bDx_JJADgkK0D8rNgQlHTy2BgIXccGXtBrohPmuMVSQJ9DHsfmmfkD7pQ2LbxYds2zLsa3v8Q8IStgjwJPfUE2Bomlw3y6xNQQEo7-0BYnKH1KR8a05Rwdnuzp7qfG7-zXT61ibxpJj149le4Y9yrdYiwiRv8IbPrwVdbzHNElpfXMKfxPcEOFI1BW5chfyo3ggGQ7Td3Sciovm8T-sd5j_DjmCLmbrG6-QZEFBdxRGF5Y9hBT-WkZBmJIrMEqtgykCwdtrmpP52FDPdmqktT2K1ObpgX0BH6CspBOIF_c4z8Z6Kdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منتظریم اول
خامنه‌ای پرچم رو تحویل امام زمان بده
و نماز جمعه رو توی بیت‌المقدس برگزار کنه</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5973" target="_blank">📅 09:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5972">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">بیانیه ارتش : به اهدافی در قطر و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5972" target="_blank">📅 09:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5971">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=ARJep1tqD0e6r3gzyYBAp_vKkZ6KY6D8kr3-Apx-R66fzhHDVy100XWCWuG9LgKetqWoPW0yo7SNP3qrTyRe3i-JRBfMdG8UoFtLIp_R0b97Tlq4L5IQfNUYgs3jg9fhLbwqzjBgfMmG5la55wsp9JNeAn0Cy-qajk-qNx5d4r3MEcF4sy0Apqbjdx17fBQ793GMVkOAMHOVHRdRF_hM4cmIqsBsVD9-y490Gh-MxWCdako0s38ny7SC-38wtCBaRwCIFtpvr1O9o04mL8IY0YUk45CSY74AKZQnslYJGLX3VupV_TW0E8ZF2bUjTwgKc0spJxW46VRp6SiS9X31tIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=ARJep1tqD0e6r3gzyYBAp_vKkZ6KY6D8kr3-Apx-R66fzhHDVy100XWCWuG9LgKetqWoPW0yo7SNP3qrTyRe3i-JRBfMdG8UoFtLIp_R0b97Tlq4L5IQfNUYgs3jg9fhLbwqzjBgfMmG5la55wsp9JNeAn0Cy-qajk-qNx5d4r3MEcF4sy0Apqbjdx17fBQ793GMVkOAMHOVHRdRF_hM4cmIqsBsVD9-y490Gh-MxWCdako0s38ny7SC-38wtCBaRwCIFtpvr1O9o04mL8IY0YUk45CSY74AKZQnslYJGLX3VupV_TW0E8ZF2bUjTwgKc0spJxW46VRp6SiS9X31tIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میانه‌روهاشون : «بهترین حالت برای ترامپ حفظ آتش‌بسه، اما ایران نباید این‌ کار رو بکنه، باید کار دیگه بکنه»</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5971" target="_blank">📅 09:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5970">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=STUe5_VEbeAgHdToAeYXcuMHOq59Yz2a8XtYJ8KCCMnMXIt2nhcW7cxIgRhBrSgSvgmFJiV5fKD4ZYyGp18bdOMc4VmBK-DSgsnbK5Ov548oU6LjFsbwN54dBmb9rwhuA7LWtvJwZhBcxtkPpkc2AIcXTggKGMhESqO97EAKUYJjSK2O52u2fKhkX3gCQ1cezWvG9Eotl9DqQKCfcdoCPnO5cTTLzjXdKiM-7TYeeZdPOIs8p3yaj4VM5qKbDsQsLAUzm8So2U8a3oV5ELKdjSim3TehzuPuU9jL7ZLLytMn0qRCTzYfzxxVISfjHqfYufZK276ZdFmcO2KT21JXdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=STUe5_VEbeAgHdToAeYXcuMHOq59Yz2a8XtYJ8KCCMnMXIt2nhcW7cxIgRhBrSgSvgmFJiV5fKD4ZYyGp18bdOMc4VmBK-DSgsnbK5Ov548oU6LjFsbwN54dBmb9rwhuA7LWtvJwZhBcxtkPpkc2AIcXTggKGMhESqO97EAKUYJjSK2O52u2fKhkX3gCQ1cezWvG9Eotl9DqQKCfcdoCPnO5cTTLzjXdKiM-7TYeeZdPOIs8p3yaj4VM5qKbDsQsLAUzm8So2U8a3oV5ELKdjSim3TehzuPuU9jL7ZLLytMn0qRCTzYfzxxVISfjHqfYufZK276ZdFmcO2KT21JXdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تابوت خامنه‌ای، پهپاد وار به پنکه کوبیده شد
و موجب آسیب زدن به اموال حرم شد.
یه تشییع جنازه برگزار کردن، هر ساعتش سوژه‌ای داشت.  گویی فیلم‌نامه‌اش
رو رضا عطاران نوشته.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5970" target="_blank">📅 08:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5969">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">خودشون داغووون و پلشت دو عالم! برادرانشون در عراق و یمن و افغانستان پلشت‌تر!</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5969" target="_blank">📅 08:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5968">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/736101eca8.mp4?token=v849zhIuQnYxEY0NMu4S6Hgkuiz9xAHCrz0CWkW__I8oAwCVn23vT4SjP0PZfVALa8nex4y57y_OBGnDcxQkRYUPv6myZkAOEzK6yfw680lF8CE---pItDhF3fd1mec6Z6M3EnJtpdYPrJTMTvmYYeH3AuzEBe5EJkS21QjrKqYTLliR7HkHajZJpNBrF0-vRQJdiGybtZrGe1Iz4v4HjAj2G2pDAY13-vRkemGiZGUv0HlEB3VSqAAoRrmhXyiv8-QTbZJTrOQ7HWF6bxkQIgwBMrBj7BfRCqJf2ICmst3Djj8aPGjaCeqyjqytdKXi8tFcIAzA1aQVGpU3_vzzCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736101eca8.mp4?token=v849zhIuQnYxEY0NMu4S6Hgkuiz9xAHCrz0CWkW__I8oAwCVn23vT4SjP0PZfVALa8nex4y57y_OBGnDcxQkRYUPv6myZkAOEzK6yfw680lF8CE---pItDhF3fd1mec6Z6M3EnJtpdYPrJTMTvmYYeH3AuzEBe5EJkS21QjrKqYTLliR7HkHajZJpNBrF0-vRQJdiGybtZrGe1Iz4v4HjAj2G2pDAY13-vRkemGiZGUv0HlEB3VSqAAoRrmhXyiv8-QTbZJTrOQ7HWF6bxkQIgwBMrBj7BfRCqJf2ICmst3Djj8aPGjaCeqyjqytdKXi8tFcIAzA1aQVGpU3_vzzCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون داغووون و پلشت دو عالم! برادرانشون در عراق و یمن و افغانستان پلشت‌تر!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5968" target="_blank">📅 08:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5967">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‏استانداری خوزستان: سه کشته و چند مجروح در حمله صبح امروز ارتش آمریکا به اطراف اهواز
مشخص نشده که این حمله به کجا صورت گرفته.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5967" target="_blank">📅 07:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5966">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
سنتکام : به ۹۰ هدف حمله کردیم.
🚨
رسانه‌های اسرائیلی : با پایان آتش‌بس، جنگ در تنگه هرمز احتمالا چند روز تا چند هفته ادامه پیدا کند.
🚨
سپاه : به بحرین و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5966" target="_blank">📅 07:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5965">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
سنتکام : به ۹۰ هدف حمله کردیم.
🚨
رسانه‌های اسرائیلی : با پایان آتش‌بس، جنگ در تنگه هرمز احتمالا چند روز تا چند هفته ادامه پیدا کند.
🚨
سپاه : به بحرین و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5965" target="_blank">📅 06:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5964">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=YiaITZO1MieFgzNxJ1JQaUmdHgAuhO5rvLVNl2Hpd0U6Cb7isI7NaB20CQaTTxtL2mQToJCYWP-Shl_hvBHiI2aADMOkeTL0YNGD3x4EtxCz7ODo88wiuDquHb_WiTbxL-xj0O63g1ern7TAIRM-PNpR9S9miN_OqD1iOVoQHQi9_NuEJlUI-MHD0DB1FM-uturjJZ7g6q7AfQX9ZoxDXgAGOSxaHhYhmspvn7bCSDwlJIpSwgJ_X3AAxpXfW0Xi4LN4n0AbIs-TzqILp0R-mvpaaTfs9tlg3QwvdaVv2_Oir5Ab3GYeMmjKKmhV7laehmG9XpBMmUzJMFfZmUNZCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=YiaITZO1MieFgzNxJ1JQaUmdHgAuhO5rvLVNl2Hpd0U6Cb7isI7NaB20CQaTTxtL2mQToJCYWP-Shl_hvBHiI2aADMOkeTL0YNGD3x4EtxCz7ODo88wiuDquHb_WiTbxL-xj0O63g1ern7TAIRM-PNpR9S9miN_OqD1iOVoQHQi9_NuEJlUI-MHD0DB1FM-uturjJZ7g6q7AfQX9ZoxDXgAGOSxaHhYhmspvn7bCSDwlJIpSwgJ_X3AAxpXfW0Xi4LN4n0AbIs-TzqILp0R-mvpaaTfs9tlg3QwvdaVv2_Oir5Ab3GYeMmjKKmhV7laehmG9XpBMmUzJMFfZmUNZCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏میرباقری در صداوسیما:
‏دشمن به معنای واقعی کلمه هیچ غلطی نمیتونه بکنه، بنظرتون میتونه غلطی بکنه؟
‏مجری: بله دیگه، رهبر که خودش این حرفا رو میزد رو کشتن</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5964" target="_blank">📅 06:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5962">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nF_JJfyAGweOe2pD13tg8bJne7sjcIrKV3Gy5EbQqiPwQizS8g8BJy1oOG02NhiFtfBSnGrNUJGqZC1nc6aPd8WHP8UMkq9q_H6EIU-69GsL-lQ0-3TbpSRzIvN2l9hftMdN_kpAQU24ZHp3O3YPZSzJaYmLVCEmZCoXxI4PlwBeFUdKOy8NgKo80qWJFh54SVwhKZw4kOepPN6e93n6rbs95UrL_MsTk_tnP2jAlMDxi_fuCqWjUodSHe9Sba-CEfuLTTLFCPOxdMMXX_eY6xISQ7YrFID_Thg-301bZTCjlLg7OkFu73DuLk7fRmwTWmf5L66z8Yduxl44wHhjbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=Qjjipwm_d_Pa12eeM0luZU_kEv4QbvLO13Hu-IF9OmoCpGgsDSfWgEaErVFCqCwuxIEJgT7KCvE5DmsQ8xIeakdU-ziNlkyE_m_uZ1vDgbUv5yWgXhYNDryAC-9Pli05nrwVAXlc7WT9m8O7BqbQFXCTQ8uAdx2nVLjpgZgv9P624Nl0xmAMjzZY0C4dFA2Je6_OtD35LjzsNORHHwnwnku41-j18JVverORegG-1f-KMS9VwdNrlEE9j4rwKROV9X1Klh8skyL59zZSyf7xvgLnXTnVOpaMB6eMi66WVkDNBCwnl1a751hjQaRcqjSWlPwXU3ncfj8VLK4ZOB1x_Azh4RWu20ZH-EqnmngOphSzPPfjQj0vOhDkmmikfPNwsZRsJNY0Lhu4w0xKmiLjSiagLPXvjqhm65MQZLZr0e52VAIHCy8HHPdoFtL605jX_VE1ZBWuUFfPrzObk_Pd1zRRMUrwHtP7csU4Ln9JNOn7XQUAZkMqaTmLISAM2h3v0x7Qw8QdBMOQs1P3EJDZqa1Wy4szJkRGR6UevXPouGnGINP9bSDY8zw052cPZKBtppYJDIQfEvt0Eckyzt4ItZ03vTHUtf_FN-ZWCbV4G7O0RKzefxiL6n2VWttrEZdr_z4LlBv6q0RMsTbe2D8QikrwU0Eq9W9LdhHgZ2p5WXo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=Qjjipwm_d_Pa12eeM0luZU_kEv4QbvLO13Hu-IF9OmoCpGgsDSfWgEaErVFCqCwuxIEJgT7KCvE5DmsQ8xIeakdU-ziNlkyE_m_uZ1vDgbUv5yWgXhYNDryAC-9Pli05nrwVAXlc7WT9m8O7BqbQFXCTQ8uAdx2nVLjpgZgv9P624Nl0xmAMjzZY0C4dFA2Je6_OtD35LjzsNORHHwnwnku41-j18JVverORegG-1f-KMS9VwdNrlEE9j4rwKROV9X1Klh8skyL59zZSyf7xvgLnXTnVOpaMB6eMi66WVkDNBCwnl1a751hjQaRcqjSWlPwXU3ncfj8VLK4ZOB1x_Azh4RWu20ZH-EqnmngOphSzPPfjQj0vOhDkmmikfPNwsZRsJNY0Lhu4w0xKmiLjSiagLPXvjqhm65MQZLZr0e52VAIHCy8HHPdoFtL605jX_VE1ZBWuUFfPrzObk_Pd1zRRMUrwHtP7csU4Ln9JNOn7XQUAZkMqaTmLISAM2h3v0x7Qw8QdBMOQs1P3EJDZqa1Wy4szJkRGR6UevXPouGnGINP9bSDY8zw052cPZKBtppYJDIQfEvt0Eckyzt4ItZ03vTHUtf_FN-ZWCbV4G7O0RKzefxiL6n2VWttrEZdr_z4LlBv6q0RMsTbe2D8QikrwU0Eq9W9LdhHgZ2p5WXo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا به دو پل در استان گلستان - آق قلا - حمله کرد. یکی از این پل‌ها، پل راه آهن است.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5962" target="_blank">📅 06:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5961">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=mO_cRE4AV-_6BW14eKi4HXlXsNUSDNkMAYad_sAcSxG4QZVcaJd9WFNYBq6zZaQQhvO0sBbZIrbFsObrDnVUneO9_Q1v6GktiTrVLV5vQzYzhckvnXEAN_R1Zlm4RaKhFTbB5JkTQ2i0QP5GRdS-B9FvSi5oK9CFIm0sHrPa2CvMvJjoTk9BIUjoVOCRbFUk4KF0ttP0qPECx3eHRJpz77rSnSEDs3G4VBADNBzpm_WWBan7Ubv1WZ3OUFwx_yy2CnogTgxH_exdsf9ciE2OYmjzT1Ms1k4kd4TZ6NIfs2b1JSHUVrpuX1KA7_CozdaO9-Bis4pqx5MaVJp_ja8lyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=mO_cRE4AV-_6BW14eKi4HXlXsNUSDNkMAYad_sAcSxG4QZVcaJd9WFNYBq6zZaQQhvO0sBbZIrbFsObrDnVUneO9_Q1v6GktiTrVLV5vQzYzhckvnXEAN_R1Zlm4RaKhFTbB5JkTQ2i0QP5GRdS-B9FvSi5oK9CFIm0sHrPa2CvMvJjoTk9BIUjoVOCRbFUk4KF0ttP0qPECx3eHRJpz77rSnSEDs3G4VBADNBzpm_WWBan7Ubv1WZ3OUFwx_yy2CnogTgxH_exdsf9ciE2OYmjzT1Ms1k4kd4TZ6NIfs2b1JSHUVrpuX1KA7_CozdaO9-Bis4pqx5MaVJp_ja8lyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : جمهوری اسلامی یکی بزند، ۲۰ تا می‌خورد.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5961" target="_blank">📅 06:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5960">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QRZtrdTlY7bR4-pYAZXEqu_IfH5bMwmkgCB6WCpqyKd3yeJ8oE5EQbuDwMxezzTGn3kJ079VSWgNLEAkeXol-02uMD_MQypZX0ne8fzOu0BSyOjeLU1sN9ZLYai6z1nxx3j7NHJvJ5nRyz8QJhZzu9iLr2BH0ZMeXZZmSyYKc3f-5AFXHdSS11RBADbsVOAMRwwoiwv4SIQaBLHFBrxoY-ZvE3BrZMM7xmhjf_CiVH8_6nSk0QpBtgyIePOHgRkiypQsaApjW_wSCzHScF6FQ-SGmS7ae5IWIujrYF-K7OORGNkzDoczbfHfs8Aw6ypV9pJZM4XdICzE9DZUsgl8mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5960" target="_blank">📅 05:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5958">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=ZYQT8yDHoZi8oKvEzaFjB2NiP-6JuMTtLUqFqG56I_ogAhk3IAa_1ey1wKSXeymMp4FjPtyBTLHx6qOFNT2Ds1cnk06k-eiEhH_FcbAP4iU7lvzeIgDVgm791sxqljoQAtQJeYyHGZhqiJ24BjBb3Cahr0QwyoIG1EgGx1mUNhlvFRO9a3GByXIZF-43CJAI2zYzrVetBsviNOWcfkQAUkcgS1mKQnUiI-04ilk7QFlkBkwahkZGFac_WVwzDJCknsNPyVmQXwNBocYCsvc9BWrR8Vp34YKd_WS-RmrMjuihx11zTfSHPZd1dBzqaWVdsO5yiDeQHUJ4XCf6YAagmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=ZYQT8yDHoZi8oKvEzaFjB2NiP-6JuMTtLUqFqG56I_ogAhk3IAa_1ey1wKSXeymMp4FjPtyBTLHx6qOFNT2Ds1cnk06k-eiEhH_FcbAP4iU7lvzeIgDVgm791sxqljoQAtQJeYyHGZhqiJ24BjBb3Cahr0QwyoIG1EgGx1mUNhlvFRO9a3GByXIZF-43CJAI2zYzrVetBsviNOWcfkQAUkcgS1mKQnUiI-04ilk7QFlkBkwahkZGFac_WVwzDJCknsNPyVmQXwNBocYCsvc9BWrR8Vp34YKd_WS-RmrMjuihx11zTfSHPZd1dBzqaWVdsO5yiDeQHUJ4XCf6YAagmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکله و برج اسکله بهشتی در چابهار</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5958" target="_blank">📅 00:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5957">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
گزارشی از قطع برق در مناطق گسترده‌ای از بندرعباس، بوشهر و چابهار</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5957" target="_blank">📅 00:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5956">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/693dd42141.mp4?token=avotG6Dr1_I3pq-ClpvJuJdU4KygfvXvFiBkOcTTcdFY17EQ1mBRS7g9zdUhi4_DHZVh7e4FSxKiRZc4ck5RRJsKes91sra9fuGdOTuuBOlTlmUrMG2tytxJUzqZ-fDzggVocagjMbPJ4qYD8RPxpV4zXQ1sriM75chORI7iMPPRi1EuJrhslh5hjbmSU5FuTWMeZweSjfd5T2y6EhpZeVcqLMsxDwUYgvCnoTDwM0N9pbjQ55-Cp5MSQ9chUn9pqgoOV2CeQTa8or8gvw6jBddx5kXFlH1VRmnZ5INs2taOsBFmzoIBLIcoLSKaBqFgVQJNCbExEtfDw7RWxuqw8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/693dd42141.mp4?token=avotG6Dr1_I3pq-ClpvJuJdU4KygfvXvFiBkOcTTcdFY17EQ1mBRS7g9zdUhi4_DHZVh7e4FSxKiRZc4ck5RRJsKes91sra9fuGdOTuuBOlTlmUrMG2tytxJUzqZ-fDzggVocagjMbPJ4qYD8RPxpV4zXQ1sriM75chORI7iMPPRi1EuJrhslh5hjbmSU5FuTWMeZweSjfd5T2y6EhpZeVcqLMsxDwUYgvCnoTDwM0N9pbjQ55-Cp5MSQ9chUn9pqgoOV2CeQTa8or8gvw6jBddx5kXFlH1VRmnZ5INs2taOsBFmzoIBLIcoLSKaBqFgVQJNCbExEtfDw7RWxuqw8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش سوزی گسترده در بوشهر
🚨
کشیده شدن دامنه حملات به جاسک و ابوموسی
🚨
گزارشی از فعالیت پدافند بر فراز آسمان اصفهان</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5956" target="_blank">📅 00:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5955">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c7ItFrEnCqGDemby7THVci5V66STSLomBsZ7Mk9j4dkuQ0r88KAg-4Uq_MMyR3J2-3vCkM42e5QSOMe8O0slryKGk55oKtoefdZRDPCukN1ikW8yPIioQsuvKeT3xYVfgJmCL68DGtsFa_Ck_MM1EO4qSNPhbX2aDlNXMkv94JIdz7CP_NcTllSwHnykp20R6rLHA0Svev-nDjsixCauHjwDRFidGhuAuvrMJvnk_btNQG6WFT_L7XupLKcjUwMm8Q7sSzUIJ7ERvLZa67UTrEXVySb9O2Zk2Xk6iobGyflmsF5pxaIq31MP1bvZh4nT3CGteibN9CO4Kgfj41A9eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت مجید موسوی، فرمانده موشکی سپاه</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5955" target="_blank">📅 00:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5954">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
گزارشی از حمله به یک پایگاه بسیج در بوشهر</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5954" target="_blank">📅 00:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5953">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e3ae34ead.mp4?token=YX5PiJadldadNs5CAUwbFqgz0CfkeqSUbsZYKsDhyCUUZoTKEmaMljM5_2wyVfSiVA0WxkkLAdCNA4I0jdGpBeClOj5amOYjwra60o1DRvjnok3XtmtC2vLHN8qaB0HsEE4qrUKB99ZUE94_nU8aqS2RtERrbL-g4g42wocuQIp0IksdM2Kwi7NXusapN3ivP1n2OGftb1W4B6tHkzRMvB1NySTah-Nbo667e_zuGPO76wsF36vCFf4yAmfCNyCi2my1qx0SKGt9zdDhHT4_STVqsYjD0_20J-810ipjz0zpp5Q0YPdwsM90G_ppGRMe13NyfbLgNnn2AOUVsj8bGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e3ae34ead.mp4?token=YX5PiJadldadNs5CAUwbFqgz0CfkeqSUbsZYKsDhyCUUZoTKEmaMljM5_2wyVfSiVA0WxkkLAdCNA4I0jdGpBeClOj5amOYjwra60o1DRvjnok3XtmtC2vLHN8qaB0HsEE4qrUKB99ZUE94_nU8aqS2RtERrbL-g4g42wocuQIp0IksdM2Kwi7NXusapN3ivP1n2OGftb1W4B6tHkzRMvB1NySTah-Nbo667e_zuGPO76wsF36vCFf4yAmfCNyCi2my1qx0SKGt9zdDhHT4_STVqsYjD0_20J-810ipjz0zpp5Q0YPdwsM90G_ppGRMe13NyfbLgNnn2AOUVsj8bGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امشب - چابهار - حملات ارتش آمریکا</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5953" target="_blank">📅 00:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5952">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aKl7Aen8kAQyxEQX7RWzWXhrkeouce2pgEpvfE0hZQkKEaz8ZlB8Ae575FOAZ31loRsnPMgQ5A9leqiKXoHNMh_UzviQaiGrN_vmPgO_5jCtHQaFVYZFTUVVNsPRHbmNx7rvTC17EYbxJQFpb9M75WFRSn1tU5Cn0cCyN_gd4YIbOLsBHC8ogvOlZ0RrVBgy899M_UyVnarNJ9s22PaF_ZOR-H0cA-xTum5Y99D2Q7tz8zYQY06zIL0s3F2moSFlnR3FFviTcawC3MoMP8sEWWeykL40vXo5GjewY82P63-7JNM3bnuAehVlQrBph_hSTn4bnVT3G2sgx9YmvX5yPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله به یک سیستم راداری ضد هوایی در بوشهر.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5952" target="_blank">📅 00:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5951">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">حملات به قشم و بوشهر نیز کشیده شد.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5951" target="_blank">📅 00:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5950">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‏ایرنا: صدای حدود ۱۰ انفجار در چابهار و کنارک و قطع برق قسمتی از شهر چابهار</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5950" target="_blank">📅 00:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5949">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a030961c3b.mp4?token=UdMWgI-Xn4v8WHFfqqj-_m4V99yLcneehDy830vemfkHOlHPo5Ie2LTJHU8ZlfhcVjQUkBWRyt2BP7bY0DSlsydKY2TogyDfU0a5xEGlRYW5xbOF6248dMhBDU2oMH4yM-ntFdUL7CJejrZqkGWoz8cTXUl1ZpkOYymwF1tuSse1ADIR-5iv4Of34PF3oKUGQfSWgNRmW9iePQl6lCLIk9_UEvxFrorc4UeEIOMByOrdivJiUz7NXWU6pPeNKtOr6iUcm8AWP0yZKLXOpO9EFcK7IVXIsgVFXO12jvmIF6N8bGNEizlInGSnvy5RSHryfGrulGKtjtQ_5SSsJtCCEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a030961c3b.mp4?token=UdMWgI-Xn4v8WHFfqqj-_m4V99yLcneehDy830vemfkHOlHPo5Ie2LTJHU8ZlfhcVjQUkBWRyt2BP7bY0DSlsydKY2TogyDfU0a5xEGlRYW5xbOF6248dMhBDU2oMH4yM-ntFdUL7CJejrZqkGWoz8cTXUl1ZpkOYymwF1tuSse1ADIR-5iv4Of34PF3oKUGQfSWgNRmW9iePQl6lCLIk9_UEvxFrorc4UeEIOMByOrdivJiUz7NXWU6pPeNKtOr6iUcm8AWP0yZKLXOpO9EFcK7IVXIsgVFXO12jvmIF6N8bGNEizlInGSnvy5RSHryfGrulGKtjtQ_5SSsJtCCEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از حملات امشب آمریکا به چابهار</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5949" target="_blank">📅 23:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5948">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1h0SnXMji6cj00hlWmoFS2jzHv3M0u5tz96Op10ATXBAjWZAEpaGybh4fSxjUq5nI2x-AoaRbSkzeqDL6mTOyUQgSLamSSU2M5881KIcHubp-W8CvJ2eCmWiyU5cIP0BoxDEnSYlHkHixSO-AacTLNBQ9CcYJXlwRvpkQakG0-AxTAYFWfnMvtX7iSjQIFdEaocMf50JSKpxvI6q38t5vKOjIlllS1cdhwJqU0HLjKT2ek01QJ6H6rvZA29mzwKLZyw7ezTSQFlxa_uoiKB6Pj5bQhO-NwcNr4owQjsSqs4-vdtsXwJZYP-RzDdxMQ1czpXnEwminRdMhkDA2nNsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به اسرائیل اطلاع داده است که قرار است امشب حملات گسترده‌ای به ایران انجام دهد.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5948" target="_blank">📅 23:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5947">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌هایی از شروع حملات آمریکا در جنوب، حمله به مقرهای سپاه در سیریک و بندرعباس.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5947" target="_blank">📅 23:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5946">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌هایی از شروع حملات آمریکا در جنوب، حمله به مقرهای سپاه در سیریک و بندرعباس.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5946" target="_blank">📅 23:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5945">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">جی‌دی ونس که طرفدار مذاکره با ج‌ا بود:
قرار بود ما محاصره دریایی رو‌ برداریم و اونها هم‌ دست از حمله به کشتی‌ها بردارند. برای یک هفته خوب بودن ولی در ۲۴ ساعت اخیر شروع کردن به حمله به کشتی‌ها.
بهشون گفته بودیم اگه
حمله کنید به کشتی‌ها باهاتون محکم برخورد می‌کنیم. نمیخوام بگم امشب قراره باهاشون چی کار کنیم.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5945" target="_blank">📅 22:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5944">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c3530f756.mp4?token=GAsGgv5OFkt1h6PHTHLJeglOwTCQd7ANND2MFnal9Ro2_4kcp-9LSd8MZNmVayOWUMr-0gkR5vN-B7OIG6iakPehmuupN1VSSM8MqJ5tjgrIcg3Qbb15RaPAUB6z7ocIS1eIpA6qbVHYXuAL0fPrGLT2boSoKUDkN6hLsScbE9OEFAwoYOFFeA4YUlXRQ7Q03Tx0d0QMfxBlv6jE0YynBGejePH-hvQMDNNQKDatWuNr9H-x8bHWJP7ADqVadlqR5r7Lw8RtWNtHH2ds6QxYWuVJhb2b5y1HIJpfANwXfHiyysvWHedAbrOSoLR7PTujbOgTFB2XOlEP4TSHGRcE7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c3530f756.mp4?token=GAsGgv5OFkt1h6PHTHLJeglOwTCQd7ANND2MFnal9Ro2_4kcp-9LSd8MZNmVayOWUMr-0gkR5vN-B7OIG6iakPehmuupN1VSSM8MqJ5tjgrIcg3Qbb15RaPAUB6z7ocIS1eIpA6qbVHYXuAL0fPrGLT2boSoKUDkN6hLsScbE9OEFAwoYOFFeA4YUlXRQ7Q03Tx0d0QMfxBlv6jE0YynBGejePH-hvQMDNNQKDatWuNr9H-x8bHWJP7ADqVadlqR5r7Lw8RtWNtHH2ds6QxYWuVJhb2b5y1HIJpfANwXfHiyysvWHedAbrOSoLR7PTujbOgTFB2XOlEP4TSHGRcE7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگفتی سران فعلی ج‌ا آدم‌های باهوش
و منطقی هستن، چی شد امروز گفتی
که یه مشت بیمار روانی هستن؟
ترامپ : شناختمشون!
و لبخند رضایت مارکو روبیو
[معروف بود که روبیو ج‌ا رو می‌شناسه
و ونس اینها رو نمی‌شناسه،
ترامپ امور رو داده بود دست ونس،
که الان ظاهرا دوباره برگشته به مواضع روبیو]</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/5944" target="_blank">📅 22:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5943">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe5d27edac.mp4?token=HAxQoXabwVa_RO4wkNJLG3e7rEOlQyjbcIchLsdWbLKBh4JfIL87wqmhynp8wjjqe3Nzw7oM4soQZRQTnWBFPaIukYvDwF7H2xD_CkycP696zo_1ELlUglD7aPfjFaU35hiUUKBEv_Qts62kOaFuWQdHtp9K3EAN4trW-s4GAj7-0Zb81EoFW3IsGz7wJnjNGNa7FEbyWr0PZfbNGUm_0ysWzoN33VCy7xdOsUx7PznCN9pO6sawSG6JGXlDJWUP2h33jdYSHymr5cpOmIxJpqeZXyYvTkpxzBMjl5Il-YBaVqxWY6Ht9mtnUXBBOsBTNKV-w1I6mWQ9G7TeM3ZqqhL6SqOLLB0a4h_cn17xHTLSBk8b0Rz5iqU0N3UpSBd4HcQxJVzytepnighOx584EMEKddp5HaOaEsJY41FT3ay5TWLx8sg0zbgdvChv1T5ZNZTxEM6bMdDpefdeAAJLs4IZG4VZe83Si5rxZckEe5oEU87iAh6MhTe4cwKGEtjaeArVJtIjC9CjksppkBvvd925SEgv7ud3oqLRzddkJSvJS4yjrJBXs0XnQMz92cuj1RLqHUEmbql3-TgF7UYJhe6ai74jzISuBwnLigJMpal1sl08mZPwyYCp2UkYP_BYzL1W1yj2SM4Mal7TLezMvPam5H2aDtMRqcwFAAeWg5k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe5d27edac.mp4?token=HAxQoXabwVa_RO4wkNJLG3e7rEOlQyjbcIchLsdWbLKBh4JfIL87wqmhynp8wjjqe3Nzw7oM4soQZRQTnWBFPaIukYvDwF7H2xD_CkycP696zo_1ELlUglD7aPfjFaU35hiUUKBEv_Qts62kOaFuWQdHtp9K3EAN4trW-s4GAj7-0Zb81EoFW3IsGz7wJnjNGNa7FEbyWr0PZfbNGUm_0ysWzoN33VCy7xdOsUx7PznCN9pO6sawSG6JGXlDJWUP2h33jdYSHymr5cpOmIxJpqeZXyYvTkpxzBMjl5Il-YBaVqxWY6Ht9mtnUXBBOsBTNKV-w1I6mWQ9G7TeM3ZqqhL6SqOLLB0a4h_cn17xHTLSBk8b0Rz5iqU0N3UpSBd4HcQxJVzytepnighOx584EMEKddp5HaOaEsJY41FT3ay5TWLx8sg0zbgdvChv1T5ZNZTxEM6bMdDpefdeAAJLs4IZG4VZe83Si5rxZckEe5oEU87iAh6MhTe4cwKGEtjaeArVJtIjC9CjksppkBvvd925SEgv7ud3oqLRzddkJSvJS4yjrJBXs0XnQMz92cuj1RLqHUEmbql3-TgF7UYJhe6ai74jzISuBwnLigJMpal1sl08mZPwyYCp2UkYP_BYzL1W1yj2SM4Mal7TLezMvPam5H2aDtMRqcwFAAeWg5k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل برگزاری مراسم رو
انگار غزه است! با بسیج کردن اینهمه ستاد و پول و ارگان‌ها و…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5943" target="_blank">📅 21:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5942">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N6XG7Q3xg1Rawu6zByGuBLQCyq9O6FuvfrJYpJmWGK4nR1gzrybb5lMdljT1g5bf2P7ok0GeZ-cB4jsKGygNW_N2LimxWW_NEiMtPHYKc3NRXawUbg2K1LIuHAeXWk0-j-CnMPMM1g_yCMCaHx56T3cjom2p2YEWRsh29Ydl4CGr7oXdv0T_lj-0f7_fHKidhB1aKzSTViHDlrpUtxlSQ7_ZG-EL228v04VH7e-Pb8OxVaTyNOjthhPrzm0WDN7HNGy87ac6gnXA2J4RAGFA452ymmk5TA8tH1pIiBWU6tkKbkVXYWTWpcRDJVZYhfVbENNn2NYiTmS21jme88-chA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: درباره جمهوری اسلامی کارهایی انجام می‌دهیم که باید ۴۷ سال پیش انجام میشد.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5942" target="_blank">📅 20:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5941">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c3c23cc7c.mp4?token=obO1vKuTv-DRH9aW7JsMuy04UaJ48ZV5Xn6QDve6iwsKO6kix4wXqUYF8_BNSvoRaEtJE-_WzwcR1xcViMDdTmFNuFZrYc_M1wtgMsWQBAZGFUmPQNfj-yspJqRLZNabmLsiH_GMX6RNFgAQ3q-Lc1AVxYAo3Vnq1SRe6vfdKdRIaw9A-MwyPJIwlX409eG0ExbF8YTwnhzLPFtEUCJErzxq2MJfKCuLhVa9CJH7R95glQo82akQFoEfwb2qluz_GERBhd7DQHvVKjg3ecQy-hcMyj3yNaRuSV9VT_1XLOZ2jYD5qH3KKhSvUPxX1to6WLyYq3XBHhavJ-zrVFz9bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c3c23cc7c.mp4?token=obO1vKuTv-DRH9aW7JsMuy04UaJ48ZV5Xn6QDve6iwsKO6kix4wXqUYF8_BNSvoRaEtJE-_WzwcR1xcViMDdTmFNuFZrYc_M1wtgMsWQBAZGFUmPQNfj-yspJqRLZNabmLsiH_GMX6RNFgAQ3q-Lc1AVxYAo3Vnq1SRe6vfdKdRIaw9A-MwyPJIwlX409eG0ExbF8YTwnhzLPFtEUCJErzxq2MJfKCuLhVa9CJH7R95glQo82akQFoEfwb2qluz_GERBhd7DQHvVKjg3ecQy-hcMyj3yNaRuSV9VT_1XLOZ2jYD5qH3KKhSvUPxX1to6WLyYq3XBHhavJ-zrVFz9bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - اسکله بندر عباس
زیر حملات ارتش آمریکا</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5941" target="_blank">📅 20:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5940">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dd51af5b9.mp4?token=CYCMWf0xOKSZsATk6xc3kCSVB2a2mRxms0tNO6OEjCN79zj70sfFMLm8ot9Drtr2FS0MqdA1v4QBWARJik0G1MaTtDBKdwpTrKiDPanNnjiVDdLM8Skm3TmgA_NVtoDHRgV8OHP78a3C2W4ijRIfTHLyWe7RtyPpbQUIiQkOyu1v6MnagDZPOUJZbjpK29R_cRV2JDPPQSsYA9PY5W1sYZckWTdev4i3jhKLzu5eha2jao4f6Xh-6Isq5ZbIkYk8c4n0zeHhXdqspcxaXcg9SZfyZWXfVqGVtQmF3mHF05JYs7TL5G5EJv28AuY1KbtnPu-MhbR2Relt7og_Qym2Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dd51af5b9.mp4?token=CYCMWf0xOKSZsATk6xc3kCSVB2a2mRxms0tNO6OEjCN79zj70sfFMLm8ot9Drtr2FS0MqdA1v4QBWARJik0G1MaTtDBKdwpTrKiDPanNnjiVDdLM8Skm3TmgA_NVtoDHRgV8OHP78a3C2W4ijRIfTHLyWe7RtyPpbQUIiQkOyu1v6MnagDZPOUJZbjpK29R_cRV2JDPPQSsYA9PY5W1sYZckWTdev4i3jhKLzu5eha2jao4f6Xh-6Isq5ZbIkYk8c4n0zeHhXdqspcxaXcg9SZfyZWXfVqGVtQmF3mHF05JYs7TL5G5EJv28AuY1KbtnPu-MhbR2Relt7og_Qym2Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه مراسم برگزار کردن … ستاد برگزاری ، هزینه هنگفت، ده‌ها ارگان و ستاد زیر نظرشون.
بعد کارهاشون رو ببینید!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5940" target="_blank">📅 19:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5939">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FtCXwBANBB0dAcPINFOeB-ICOaaM9twA70rGzA1OpLcWxxgBn3SJJ-Bo1iOMpOsudOy8S76klKPTRm-1sU7eGhzhqW8lNmAaFK_CsPHaCHj1hzpiFoS-7rGGQdvsi9Hs-kSqc_YhAF8hRH2N0PezQoEtRZVRvEPY8THIUSCLq7UOKRDiKfAugvNnYVeUgU3WcAcpEXjWHxRJMebLYTkwz47BEXf02nCskYhZ6RekZhfhi6RjAV4Q3M77fd8cL4zqDsotjEZVTo1bZL5VMXT79JOuyuVqUjucP3YeA6MlXbcznRnokqQcSvHrPMToryQICu165C0Qq4Ima6n9G52YEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کشته شدن ۸ نیروی ارتشی
در جریان حملات دیشب و صبح امروز آمریکا</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5939" target="_blank">📅 19:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5938">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ترامپ: اومدن خواهش کردن زمان تشییع جنازه ما رو نکش. بعد وسط این مراسم حمله کردن به سه تا کشتی.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5938" target="_blank">📅 17:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5937">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=Dcq6LlWNG7BUH_pPCXf13sXY2k_KMiT6A2zzPIQes7geKJdnpp-Y2aJ5NFwfEYGPncCAiGc20L4_73lQ5OePvbmGM3K9fvYzlpDmeyhj2SnbYqScwuAteZttKg6fSAphR7msh7mkqF9n1dGEOHeEsycZJjQn4Ly9UIAkl2Q-ZzFbMgnPV4drFV6bO2eqMax7i4gXRGrFCgbanh-dU0kmYdczsiSL0cVdsPS3pPSUYmbiLC892AOJDRG-qXWrHa-Ry5CulrH5lecYyXXsXcQZV1BxnloZn0x53ry0d2Bxn5rWSUP9-dbbwm-h2zp7syWYAMEC5Ip4bpjwtu_aGmwaDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=Dcq6LlWNG7BUH_pPCXf13sXY2k_KMiT6A2zzPIQes7geKJdnpp-Y2aJ5NFwfEYGPncCAiGc20L4_73lQ5OePvbmGM3K9fvYzlpDmeyhj2SnbYqScwuAteZttKg6fSAphR7msh7mkqF9n1dGEOHeEsycZJjQn4Ly9UIAkl2Q-ZzFbMgnPV4drFV6bO2eqMax7i4gXRGrFCgbanh-dU0kmYdczsiSL0cVdsPS3pPSUYmbiLC892AOJDRG-qXWrHa-Ry5CulrH5lecYyXXsXcQZV1BxnloZn0x53ry0d2Bxn5rWSUP9-dbbwm-h2zp7syWYAMEC5Ip4bpjwtu_aGmwaDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دشمن هیچ غلطی نمی‌تونه بکنه
مجری : خو اومد خود گوینده این سخن رو زد!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5937" target="_blank">📅 17:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5936">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/046bf7600e.mp4?token=J3Jb9AQb14QtdI3pukBpfVZtmW2onXNSKUNzEhlHjgzPuK5Jt1TwdV6ksRcUwUJJEaybab-kGvdHMI6SG9BimkXzxIafpvk5V2ArqMy-63xDxcbKM5PWAKHcbTjQ4cx1eCZKi-qO0pCfug2TPCjrqWtLgXvq1UaGrdGM51VksA2m3Kr5bLoqIYzqhCvrNJEr5tnIoAP1S9znAP5K_FxslrpE0Gn5wvRooSubnreJMfx5K9IcnhwJ9axaWdz_iATUpzREculFR1f686AgVbYQ3s2mv3blZcp03eW_h2naAIkzYZkH4ihm4qK2YGp5nv4Ik4OEyuZuG_Ey6LipCxYgJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/046bf7600e.mp4?token=J3Jb9AQb14QtdI3pukBpfVZtmW2onXNSKUNzEhlHjgzPuK5Jt1TwdV6ksRcUwUJJEaybab-kGvdHMI6SG9BimkXzxIafpvk5V2ArqMy-63xDxcbKM5PWAKHcbTjQ4cx1eCZKi-qO0pCfug2TPCjrqWtLgXvq1UaGrdGM51VksA2m3Kr5bLoqIYzqhCvrNJEr5tnIoAP1S9znAP5K_FxslrpE0Gn5wvRooSubnreJMfx5K9IcnhwJ9axaWdz_iATUpzREculFR1f686AgVbYQ3s2mv3blZcp03eW_h2naAIkzYZkH4ihm4qK2YGp5nv4Ik4OEyuZuG_Ey6LipCxYgJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
هگست وزیر جنگ آمریکا : همونطور که ترامپ گفت امشب احتمالا اونها رو عمیق‌تر و محکم‌تر می‌زنیم.
ترامپ : محاصره دریایی رو هم احتمالا دوباره علیه ج‌ا برقرار کنیم.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5936" target="_blank">📅 17:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5935">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aff1f3384.mp4?token=YLVO_v-O5czJBd9VP-haK8d5L01tjOJdMQsZMr4zp3jLMHpSgLoHGZm-6tHVOuj-zKFPbuBTy2lD5rX4WVc1hg1WuigPnDL2DmnATBgIB4Hj_HzqdFYjyveb8f6we2yS_uijkNB4Ef5jxryekeVvk6MyUqbSFmuCMfh1hSru1VmjQTwmHGTdR-5gX0epjdSp-TCrnTte59WdKzReFv-DCF7E221IM4nDM5qJ47Y5ZZehr440hj9jBvgmHgIR1fA358f0O4aE9NasjR4ouZh8XF4fwuP416NbsWGcRXl4nA9vPJKjgcZ6fgBX7uRY8UGVjl8UbN_leikDmmeG0Eurog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aff1f3384.mp4?token=YLVO_v-O5czJBd9VP-haK8d5L01tjOJdMQsZMr4zp3jLMHpSgLoHGZm-6tHVOuj-zKFPbuBTy2lD5rX4WVc1hg1WuigPnDL2DmnATBgIB4Hj_HzqdFYjyveb8f6we2yS_uijkNB4Ef5jxryekeVvk6MyUqbSFmuCMfh1hSru1VmjQTwmHGTdR-5gX0epjdSp-TCrnTte59WdKzReFv-DCF7E221IM4nDM5qJ47Y5ZZehr440hj9jBvgmHgIR1fA358f0O4aE9NasjR4ouZh8XF4fwuP416NbsWGcRXl4nA9vPJKjgcZ6fgBX7uRY8UGVjl8UbN_leikDmmeG0Eurog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : اونها تحت یک توافق هرگز به سلاح هسته‌ای نخواهد رسید، اما شاید بدون دستیابی به یک توافق هم به این هدف برسیم، اصلا شاید راحت‌تر هم باشه، چون اونها دروغگو و‌ شیادن.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5935" target="_blank">📅 16:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5934">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5484fca6.mp4?token=VFOuq1KEVvpJPvwo2mSYBLHYToJVDC4BqujDC9wGA2Lw0CiPH4WOlNmwRkLi_bq7YyMGyZKbjkLsI5TwRe6LhUuiJstb7KceiRjeS35WYoJBuU5Lnvzl6lE_w81XQRhOQs7oTYmIAlusMOPojZUMcA7-TyB5X9GN1jHMyAqyzxcC7IWcJcysCQeSj3NSplJGJQHJrtgI-NzbSqzSaZculgKRkyfXcXOmWsqo2IAPp7fK1a_c2ycBip3btknwVEJVLo5lvoGLryddAwaWrMov0kHTPhTTo7umACWASRY7w9a-xpbaMQCTW5iffrsqbTMi030IXHvKkhVRhk7KM_IU_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5484fca6.mp4?token=VFOuq1KEVvpJPvwo2mSYBLHYToJVDC4BqujDC9wGA2Lw0CiPH4WOlNmwRkLi_bq7YyMGyZKbjkLsI5TwRe6LhUuiJstb7KceiRjeS35WYoJBuU5Lnvzl6lE_w81XQRhOQs7oTYmIAlusMOPojZUMcA7-TyB5X9GN1jHMyAqyzxcC7IWcJcysCQeSj3NSplJGJQHJrtgI-NzbSqzSaZculgKRkyfXcXOmWsqo2IAPp7fK1a_c2ycBip3btknwVEJVLo5lvoGLryddAwaWrMov0kHTPhTTo7umACWASRY7w9a-xpbaMQCTW5iffrsqbTMi030IXHvKkhVRhk7KM_IU_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ساختمون همون جایی است که خامنه‌ای حامیانش رو جمع می‌کرد براشون می گفت :« کشتن بد است، اما فتنه بدتر است.» (پس معترضین رو راحت بکشید)
و اونها هم براش «حیدر حیدر کنان» می‌خوندن : لب تر کند امروز سحر قدس شریفیم!
ولی داستان یه جور دیگه شد</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5934" target="_blank">📅 16:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5933">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=YRYHGIRyqUp-Y9USCLG1kJHukjpvgCrN5KQc2x5mY3F7BUiekwKVcvTCyroY0teEioRLp9MYRouPWbk_-DmtIAMCcb1TL3kspXgj7o_JpdyHmGcEWUIfQlIFKCESNRkQVIdPLhgDlZZ28E9JhVYhDUjKFmbHRxpYLeZS7VWkS1kNcR4Lh0DzJCFpdxjM2GmFa5vEk8TWNKG2syYsB1feNE7OOTmW9MqQAyb3KIccuZqGGH927be5644pCSGuGhIFnNeFKliIdbPPznTs4N5kdoS1FnLwwdr4YMHShWb6L4-joEstQXkEIHD5tdTSDkod9ikhItAPNyJbfZFvsiqIww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=YRYHGIRyqUp-Y9USCLG1kJHukjpvgCrN5KQc2x5mY3F7BUiekwKVcvTCyroY0teEioRLp9MYRouPWbk_-DmtIAMCcb1TL3kspXgj7o_JpdyHmGcEWUIfQlIFKCESNRkQVIdPLhgDlZZ28E9JhVYhDUjKFmbHRxpYLeZS7VWkS1kNcR4Lh0DzJCFpdxjM2GmFa5vEk8TWNKG2syYsB1feNE7OOTmW9MqQAyb3KIccuZqGGH927be5644pCSGuGhIFnNeFKliIdbPPznTs4N5kdoS1FnLwwdr4YMHShWb6L4-joEstQXkEIHD5tdTSDkod9ikhItAPNyJbfZFvsiqIww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ : احتمالا امشب هم اونها رو به سختی بزنیم. فقط دارم یه هشدار کوچک بهشون میدم.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5933" target="_blank">📅 16:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5931">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">هزاران نفر که اومده بودن توی خیابون‌ها رو کشتن!
صدها نفر رو اعدام کردن، هزاران نفر رو زندانی کردن. اومدن با وقاحت میگن ما اومدیم توی خیابون! طعنه هم میزنن!
شماها با وعده امنیت کامل رفتید
با پذیرایی و امکانات. حتی خیابون رو تخریب کردن برای تجمع‌تون، کولر گذاشتن براتون!
خود گدا گشنه صفت‌تون رو با جوانان شجاع ایرانی که جون شون رو گذاشتن دستشون
یکی می‌کنید؟؟ طعنه هم میزنید!
شما هنوز نه این یکی رو خاک کردید!!
نه اون یکی رو می‌دونید زنده است یا مرده!!
هست یا نیست! توی چند سوراخ قایم شده!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5931" target="_blank">📅 16:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5930">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0GK5BQu2X3fZvkaXStZP4V4A-6yRokvQu_oQ1LwlnpJqxAhIHfkf6VmXS8AY9bL-SP0gtVWzUH_1Y88eRlVQNUp54uANc0czi-WLQp0xHSVgrx4uyd4ZGFe5mTcwgbBTVovNSRi0rcsERc2ZEcmMefHU3_uMs9jYNW5X1UTHv0imPjPL5FfpWuAN3Hoq0TN1PkdUlojGX1g45XyXf7V1Ta7H-iMJc3JK5lzQaNpIMe8Mn9nhkBgdVE94NkpAxukD2uv9h-7-u_8MRClvwzTuHFBsOns-HBdKaivarShJU1PC1o2SaLjFuTjf_KHdwX86GmPxB6wpUlBXys9zvqLJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه کیهان زیر نظر خامنه‌ای در دو مطلب خواستار کشتن ترامپ شد.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5930" target="_blank">📅 15:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5929">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : «آتش بس با جمهوری اسلامی پایان یافت. مقام‌های جمهوری اسلامی شرور، بیمار و فریبکار هستند.
آنها مشتی آشغال هستند.
به آنها یک هفته فرصت دادیم برای مراسم خاکسپاری، ولی در عوض دیروز به ۳ کشتی  حمله کردند.
آمریکا زیاد از حد وقت خود را با اینها تلف کرده است. اینها شبیه به یک غده سرطانی هستند. غده سرطانی را باید سریعا جراحی کرد و دور انداخت. »</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5929" target="_blank">📅 15:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5928">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nFnSM0fu5efi7SmQCYu8USYwE6OrBjtSnkbl9og5CqOxI-7TNfMgDzOoc-RtInRyx9v3en0S4sEx-_ziYVmGaPPDXLfG8vpO9uywofZv553zwEw_BrSR5B1wOInjchPnrenAyWyH6U75DODxkIuwvgEU51x97rE570ltmcFqSLyX4h2xzRx3RH3SOsi-oanfLniZCiRqepUnbdRvnbqZfbnO7ZoO-eYWBtjfvKSs-wrzpziFbTOMmP7WNYQpm10a7c7j2yaoMzkjtxXsxGWCUII2ZIkPzQPI_Cz91HnBLlndJChG8GiFipesM5HeSxMeprK2c43U_sK7s7QmlnrfxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوش دولت چپگراش رو چنان بکش
که درس عبرتی بشه برای بقیه اروپا!
برو جلو! دعای خیر ما پشت سرته!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5928" target="_blank">📅 13:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5927">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">محمد اکبرزاده، ‏ معاون سیاسی نیروی دریایی سپاه، ‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.   او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.   جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5927" target="_blank">📅 11:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5926">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
دبیرکل ناتو : حملات آمریکا به جمهوری اسلامی کاملا ضروری بود.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5926" target="_blank">📅 11:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5925">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IvrBtoxtm63VsKmJfa9hPESEJHZEuM1UAAI5j3zWT1Azz7TetFoeS4EGN2POVGRCLI5Sn8JCa8j5AyhGQoQ4mcxA-1E9TRX9l8psH0EfIt0RO4RaollGb5HSHRmADgopb1yXzg1eLZnmfl_alGnVGVyXkWEkgw5kHna7gos77b0Y3Sd07Njgxu9swMpnGc7-STnm1LaaqWxnNkYn--Ph3t3YmM_yL007V7X04Y9tnLTeX-c-r30ZYvJ9hy6ApUenIQcc4ZoXIMdMogukvpmeh3sURBZkiBMe6o7mWFJpwwb4nZvJqi2tEJvmABpqyfODAl-yqQWP1YcxRo3yVstnPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بندرعباس - پس از حمله آمریکا</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5925" target="_blank">📅 11:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5924">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">پذیرایی گرم از عراقچی این بار در عراق</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5924" target="_blank">📅 08:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5923">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
سپاه : به ۸۵ هدف مرتبط با آمریکا حمله کردیم.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5923" target="_blank">📅 07:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5922">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aada56b9e2.mp4?token=KUgc_NJWfVm376aHqYGMM-v5UyFDEye_zwhEdz3RW8nln5Jkf-rQEMUHsJlB3qZpl9HrdP4-jOPhgWhImu_TLP6F_ZAwI8ZRRMEOcg8Ix71Y-mI6HMWjsgIiFEROu5AtJaJ5lvWT79eoHHicqdsBQQcFACvaNoVsZNQbfRvPyrCuD6dFWG3gblHV_7SwZaPX2a-Shbj1RKLr-H8UtrNiwvOnswKv8wQ76yoHhAvaGp4mpyLdIFOrktmX6Wuub5309NE7FyT-_WuGTwnd_LT_XctoLuNdQ-KP06EJ3Ekbql77fMwZF7PEuiCOSDoN7Q0quYC1zTQixjby_WIk5BYFGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aada56b9e2.mp4?token=KUgc_NJWfVm376aHqYGMM-v5UyFDEye_zwhEdz3RW8nln5Jkf-rQEMUHsJlB3qZpl9HrdP4-jOPhgWhImu_TLP6F_ZAwI8ZRRMEOcg8Ix71Y-mI6HMWjsgIiFEROu5AtJaJ5lvWT79eoHHicqdsBQQcFACvaNoVsZNQbfRvPyrCuD6dFWG3gblHV_7SwZaPX2a-Shbj1RKLr-H8UtrNiwvOnswKv8wQ76yoHhAvaGp4mpyLdIFOrktmX6Wuub5309NE7FyT-_WuGTwnd_LT_XctoLuNdQ-KP06EJ3Ekbql77fMwZF7PEuiCOSDoN7Q0quYC1zTQixjby_WIk5BYFGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بندرعباس - امش</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5922" target="_blank">📅 04:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5921">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vUzK4YCtKfdHP7TGyyjB5eoXV5uH1XZtCqD8flIS44kiu7lklvkHKSvsoGmcTO6jtvXE_asIYukEc6kxelaKFP62UtHb-qR8xg9MeZrpAG2iPC3ol2ZTLizoqnfz716Hb2BkIPMw0fSUpNJa9m3bpM9R9G5GS7BkJuw3phUwG0DkjSMohnH7hxViTYJSgl6kh5s4dnjqhmY3lwFBClHsutrA9fZuDjuyr5p8PTu_efQbj6GXC7vecneE_cKWd_7VMrqzF9APfmHNfMV7HktPNZokUsIOaZX-Ox0q1nwgP8-OuBAI8_wQb5dtwRTJjdr8JVAyQZfOxfODs3YcR6Y_XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارش ها از شنیده شدن حداقل ۳ انفجار در بندر عباس
تصویری که گفته می‌شود آتش گرفتن یکی از قایق های تندرو سپاه است</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5921" target="_blank">📅 01:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5920">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا: نیروهای ما آغاز یک رشته حملات قدرتمند علیه ایران را آغاز کرده‌اند.
‏حملات آمریکا در واکنش به حملات ایران علیه سه کشتی تجاری است که در حال عبور از تنگه هرمز بودند.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5920" target="_blank">📅 00:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5919">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای چند انفجار در حوالی قشم و سیریک!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5919" target="_blank">📅 00:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5918">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f02faf66.mp4?token=cMSw6ybZC9WHxEPzXCVGIrg7AY47IgKlMw7lEzaAiVsL-E1ulvpwcLHhUGBD5f5WkvZrjRiwfPQyWgNkAOJJcnGN8tob3seWcSwKu4hw3P_KeQCFZaMJvNbk47b_jbAhG4IHXm29Y_LDXUwXr2voSXFTY8gTJgpLYmORFmPi8hEDqPYCaFQHV-XqZswjYvIDeCeAfOibaYTPH9U62ihee9fQAbsBrgUpmA-uNp0Q26tsLgsoWvRdovtHcVgYaUyjCFBQLy_adr_koQxgfkQ94Mlh4XVsNW2kJNclZ7qBYw6Tk7AIj8tKt6hKqYivK4fqMJLNYr_Wj_sOkjFOZKMghQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f02faf66.mp4?token=cMSw6ybZC9WHxEPzXCVGIrg7AY47IgKlMw7lEzaAiVsL-E1ulvpwcLHhUGBD5f5WkvZrjRiwfPQyWgNkAOJJcnGN8tob3seWcSwKu4hw3P_KeQCFZaMJvNbk47b_jbAhG4IHXm29Y_LDXUwXr2voSXFTY8gTJgpLYmORFmPi8hEDqPYCaFQHV-XqZswjYvIDeCeAfOibaYTPH9U62ihee9fQAbsBrgUpmA-uNp0Q26tsLgsoWvRdovtHcVgYaUyjCFBQLy_adr_koQxgfkQ94Mlh4XVsNW2kJNclZ7qBYw6Tk7AIj8tKt6hKqYivK4fqMJLNYr_Wj_sOkjFOZKMghQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی این ویدئو دقت کردید یه نفر رو به کامیون جنازه خامنه‌ای وصل کردن؟ :)</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5918" target="_blank">📅 00:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5917">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6i11p2fgVOdZ0duWivDBAa6kxZzhPL4ilmwAocl1zEpYm76HZaw3jag-Hg6l1DKa0wF7XSqEEVGh3zdTPBmocovS-wSlRXZSLBoC5qgN4ho7FVgpTeTKM_x1LNMCtYOg4hSX4eWXL5cp9l7y3OaXqsds5_7jIWgjcQu6y842afkT3SI7yo5OQpC8A8-kUS9ajy9Bdq76p-MZcJslLWFlG0npHMph4nM_sxJqJvuBH7lTzVxauz1a_ithw2QVDiYq8I3ftN-X0joHBilbZ68rLoy_NNCMXsEc8jINiMUUgoa_ujZ0iErvwXZh-aZbsLXnw_7VDVnVSW0h8Fuk_eXwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو حقیقتا یک سکانس تاریخیه، مدلی که دارند خودروی تابوت خامنه‌ای رو اسکورت میکنن :)  دارند جنازه خامنه‌ای رو‌ از جلوی خونه‌اش رد می‌کنن، از همین هم‌ پیروزی ساخته و‌ میگه چقدر قشنگه آقا خودش اومده به دیدن.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5917" target="_blank">📅 00:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5916">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NfJbVwqz2rLJFf3ug1UCSFk5mluIof3Fyh-NIvG-PkBWocqgL1IKw7C53-NDCPFRn5-CEQ-LTizoXkdxcaZwdnY_fbrTCPBl6bIjRDSrg2TWzrQIUp8dGleclvLpbjqh5lPdktgRxpN-0oX4IazzmansueRWj9I-ZuG20HFtj-13U2wzQjcly3ImLS9HKxnQUCJqJk7-VRdFeknlgOczcqza6qB6eKFd_p5VpmAkOEQRhzq7Y9FVnWKdQYrSQbaV1eYbwI9kD11j91WRUYT41Zz0XjEpszTEtkdY1W6WQlmRa63K6mJSEaQSkXmEGlP-64VNJdiSA03iDTgtnm_AJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ما موشک میزنیم بر اساس حسن همجواریه
شما بیانیه بدید اعتراض کنید
مغایر با حسن همجواریه!
کشورهای همسایه هم تازه دارن می‌فهمن
مردم ایران از دست اینها چی میکشن</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5916" target="_blank">📅 23:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5915">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e58e9ca73.mp4?token=F00LFDp91vleWhha8J-GMFDBHpTQ_BHEQr8He7Y-PuP5CcQGdZRBCyNmeLLtIs1WkI9THS8XPEGGFKPFBtcE0Sk6l7vrm_da0jC7kvBNRRgZmj0k7sSAxut7Gq3HWargKSnna0gzeZlCmENMi8SbLbry7HYrb7E5nSH1L788nEYbg3r_z0zm0SLuS59k64ueUXKBwfoSmkEI4OKQkM2-CSKGIfENa4mVLSxKcQLMYRW_IGjfiUbRaFxcyPvQETmViWozkbggNLoGPwIKCRDu9jA4TSSEn04F6W71fJAODJVYHcg11v_Nqozjnsb0Hj41kpAW_YAkz30ga8SGpJQjAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e58e9ca73.mp4?token=F00LFDp91vleWhha8J-GMFDBHpTQ_BHEQr8He7Y-PuP5CcQGdZRBCyNmeLLtIs1WkI9THS8XPEGGFKPFBtcE0Sk6l7vrm_da0jC7kvBNRRgZmj0k7sSAxut7Gq3HWargKSnna0gzeZlCmENMi8SbLbry7HYrb7E5nSH1L788nEYbg3r_z0zm0SLuS59k64ueUXKBwfoSmkEI4OKQkM2-CSKGIfENa4mVLSxKcQLMYRW_IGjfiUbRaFxcyPvQETmViWozkbggNLoGPwIKCRDu9jA4TSSEn04F6W71fJAODJVYHcg11v_Nqozjnsb0Hj41kpAW_YAkz30ga8SGpJQjAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نحوه حمل جنازه خامنه‌ای</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5915" target="_blank">📅 23:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5914">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">فرهمند عليپور Farahmand Alipour
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/farahmand_alipour/5914" target="_blank">📅 23:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5913">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">این ویدئو حقیقتا یک سکانس تاریخیه، مدلی که دارند خودروی تابوت خامنه‌ای رو اسکورت میکنن :)
دارند جنازه خامنه‌ای رو‌ از جلوی خونه‌اش رد می‌کنن، از همین هم‌ پیروزی ساخته و‌ میگه چقدر قشنگه آقا خودش اومده به دیدن.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5913" target="_blank">📅 23:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5912">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/naHAUWFESKOgybcbZecQE_C4a8vqFBhJITjaq_DnKWWLouRUsJDcPd18CTk81tNdPL5KLjkxLL-JGqmv8YvHd52SKOnsWCwRKRAw2AmRu6ozlF9fLYdj0DP2lLxvfdvTY-AcI3PIyC-GNALo3IwErd-RWLztivgeM08NJugJVmrJt1CBDwQoa53jv04sr6nE2HSbMf_q3yTtkJ_ozudlXsOO9bVmNJDeROqO9Tvb39t9fGZsutE2yHvEmmC3JWPv7fjgwQa8F5cU0QLMl5EBau8A10miyd22O73I9uM2fM-MfcCUPc-e3_h_QnhxTJdlc-Qlm-BGR9D74knuV04H_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط امروز به سه تا کشتی حمله کردن
بهشون که واکنش نشون میدن میشه نقض!
جای ترامپ بودم یه توییت میزدم خطاب
به نخست وزیر عراق،
هلی‌کوپتر از وسط راه برگرده قم!
بیاد دستشون!
برای آمریکا خرجش یک «توییت» زدنه!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5912" target="_blank">📅 22:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5911">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P4yh6zg49EGCq6zKd-aVTVtE4sIEoEz638JdQfpcLQ-Cpl7G6zadWgqNAZjf9tZOGJzdOlhaG-hFRlCBla2FMziAc3AkWT1rEBZY0kOPacRdbGTzuRQ-dpQwUrs498kqRL8IH_XrixM7LKdFAwgSs4upWuwAQhfmHaHYnB_KBjSbWfmCk-4lnhdbXMT3yk1JH2tUr79AXT9aU_coD6wbX9ijE_-22dBO9Mk4WGHB63O0B-SZD-3HzmTBuqeU7QJalx9SxvOUEB4_8-PB5QxLLI7ZLZhIsA01a8Cg3oLIGNPydqYfgDDpRLs7X-57GDQGK9U6z_CDjG_genLB2UW8pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آمریکا مجوز فروش نفت ایران را لغو کرد!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5911" target="_blank">📅 22:44 · 16 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
