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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-19 20:46:25</div>
<hr>

<div class="tg-post" id="msg-6018">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lbIJyOE2Zg99a7z3TD5mDWj0vjc1vH4vH6eeDCZB033bHtcto7zbvY8OM41MekdSJL9DlcS9mLECr4XoRiKdft09qQFx0vnI8Uf4DSB9UJ5SLtKNYr4kzEbFsDroDdylLGJ1uLB_MRRgKpUuLhaWn329PoFDM2Mf7VIe_Vfs2tbR3FlpSShbyJ6hYHVPN45B959Ufyq7LeVRhGgU4i9RBjDSuvUrTRx3kAfK39tQMR-B3y8NO69Z17tPQoOft3RC91injyqPAcnU69MuP_c5i290F9K3QcyL0s-jszxBquiXLylYWfTy2J4tucAQBOGLSqhVQS5QAUus7_jHfnFPmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علویه، خواهر بزرگش (ناتنی)  در سال ۱۳۹۳ در سن ۸۹ سالگی درگذشت.  ۳ سال قبلش، در ۱۳۹۰  علم‌الهدای معروف مشهد در یک سخنرانی گفت که زن حاج شیخ عباسعلی
😅
می‌دونید که علم الهدی اسم زنان رو نمیبره حتی اسم زنش رو روی قبرش هم ننوشت! (ببینید حاکمان ما کیا هستن!)  خلاصه…</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/farahmand_alipour/6018" target="_blank">📅 20:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6017">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CBCdTL9seDcNwGsIb89YYMmUWZ75YhupG5WpItG-REVUvZfiD6KHiROnXkLn4fzdNEvQCBsplLIerYuH0UMUBEtMsezM3MC7ZKK7Py0YFkm2H0O6mZei_Fnzbygt7tAnrp_QgM6h59w8uxsGJIyNVQN0aLBYMYZwuWWVtE_nnIqjCdwrYgb8nyJ4K2r6_6FmvF1cFmuGuqTGjxgGNBAjAkenwQxu9CHL-SNdywTVANS_otcnr7RB-hd3qv4e8yGeMKp9oah80UsGtFRxbWjhdqYY3e5LcKoObVpckCAzAsFgLiWr1fFP9YOF9Blgz6KLpZDuv4UTBUShsOAstb-pww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواد، پدر علی خامنه‌ای،  پیش از ازدواج با خدیجه (مادر علی خامنه‌ای)  یک ازدواج دیگه هم داشت و سه تا دختر داشت.  از خدیجه (مادر علی خامنه‌ای) هم ۴ پسر و یک دختر داشت. جمعا ۸ بچه بودند.  اون خانمی که ظاهرا خاطره ای گفت که «علی خامنه‌ای وقت به دنیا اومدن گفت…</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/farahmand_alipour/6017" target="_blank">📅 20:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6016">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">پدر خامنه‌ای، در کنار زن و بچه‌‌هاش غذا نمیخورد!  خامنه‌ای می‌نویسه که پدرشون در یک‌ اتاق مجزا شام میخورد،  مادرش برای پدر آبگوشت درست می‌کرد و اون رو توی اتاقش می‌برد اما مادر و فرزندان معمولا نان و ماست، یا نان و خرما میخوردن.   «ما بچه‌ها در اتاق دیگر لحظه‌شماری…</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/farahmand_alipour/6016" target="_blank">📅 20:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6015">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gB_jklWp-P3SyRXbm4_EDnMya7QubfMI49g1j4w_VhiPn-iZO2Evl0qL-0_yfAfFGW06qtFJ0UHnNf8VNKezps_esDctb0ISCH2P6bquT2fhd2L-LWktS049d0km2_qfc_tzlCR9l4PnCDawud2NIK3WyD1SKzbAZDNNSsI9Ag2I4XDPwulWsAhcmD5ckwtPta7cd4Q_2LgsjjzJuSBgaE4NfL6ji8a_T2wKx0RQoUsLXHxU_QD0i-XsiaHSvD88FEIKUiIeua4WC6dHLfzg3ljE_VPOoMVDG_dxu9S4sK-nc3_VHIwtLtU2D0qQOoBR2AhqMam6Ajzxy-v-rz5Knw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای و مادرش - تابستان ۶۰   علی خامنه‌ای از سوی دیگر، هر از گاه مجبور  به کتک کاری با همسالانش می شد که او را مسخره می‌کردند و نامش را «آشیخ خُردو» -به معنی شیخ کوچولو- گذاشته بودند.  در این تمسخر هم پدر نقش داشت که کودک خردسال را مجبور می‌کرد تا …</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/farahmand_alipour/6015" target="_blank">📅 20:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6014">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tFLFj6blG066qOc9Vz59KMvvnEt9kXhpJ-qtpAmFfW5ICohqG4FNQbWoELS85GqFKPesMMQ0oIfeZTJVY-UBuixdjzb57WF9FRUwO7fSY_zE_YSTtvWkrwiIUm2vO2p_7aXcYiUh9MxrcFc9j22DyifsmU4IGvvMZCwovXGmVQUWCILGwMwwid2CfDJ8gyH-a898QpObWojN6z8_9nSXZslXvmd3cLOi3Mv1Tyvs1VE5qQFTsUJnUtIgorLz8krnFxK_6LS-3AeLXwgACCRvbgX0dymYpAbeS0kksqNXta6BKMCcSOREawZwACz_9ToLVmNrpjPs21FyGGKWgGaYDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای در کنار برادر بزرگ‌ترش محمد خامنه‌ای  علی خامنه‌ای در خاطراتش ار جمله روایت میکند که  او و برادرش محمد،  در هنگام درس پس دادن به پدرشان  (جواد خامنه‌ای)  که «دست‌ سنگینی» داشت، مرتب کتک می‌خوردند.  علی خامنه‌ای نه تنها برای اشتباهات خود،  که به…</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/farahmand_alipour/6014" target="_blank">📅 20:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6013">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DW3Y8wkErEwjwhOu146AJeeXna-1_Q0yQHyVoQUogvuEw84IQQWdhgrcwU80wv9tXG-1-1jTExHEOTwqgh0A15l5iYi9CWoppsIWSS_H_9MqlPO-ExhLP2LqfKuW7q3xDK4o2mdX_UoqYv7uPLz_u6ilcSEtzGMwSEIrDajTgLwW-XHDpJZvpULYX9Nmzv8qJtpy9PZuvcubBZXBTiJ92E6mS6ggwrjB_PG7OV5UKWrXZQCzHSFlIUOOE6JmN3GhWMWGj7vpEg5yt4XNt_lIBZmLVrNJDyAXQONcTbZ5wKvksbzWFVuWgRJTiWIsxnT8K7PmpZw3v0Ako2lvBbMjoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر خامنه‌ای - قبل از انقلاب   پدر خامنه‌ای فردی بسیار سخت‌گیر بود! جزو آخوندهایی بود که مخالف «برق» بود! و اجازه سیم کشی و‌برق کشی به خونه رو‌ نداد! اینه که در خاطرات خامنه‌ای اومده که از چراغ موشی استفاده می‌کردن ‌و مادرش معترض بوده که وضعشون از بقیه…</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/farahmand_alipour/6013" target="_blank">📅 19:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6012">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ftoT0vHGzBnDY_XOgrbM999A50vu0U3HCEN_VD19MRDlKDrZhadB94T8TrzcNVRt85obQoUoJlZuJK3fO9oEmw4y29FrXCXwTbD_uGmPLdIeQCkoycDhgOUajra1PbFAt9VMcv8n_IHQ3SHNWnGxGXjVLHBUO55RjZzf5ftn_evCkOxFDKjzuTt0TUvZjEPYx3OWH9NLgMRb4TmkwxQfeP7eyvtHE6V5ul4OKgv-3bLHn9tJpWBBpZHnTHEQ2wJppZGzm0FF5ydGr_3tDiyBeExW8qgAtWyFe2c8Um8pWnXv316Y1cQGaND5plapVjmBIXdW2g2xBfNyjqXDsYpiwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر خامنه‌ای - قبل از انقلاب
پدر خامنه‌ای فردی بسیار سخت‌گیر بود!
جزو آخوندهایی بود که مخالف «برق» بود!
و اجازه سیم کشی و‌برق کشی به خونه
رو‌ نداد! اینه که در خاطرات خامنه‌ای اومده که از چراغ موشی استفاده می‌کردن ‌و مادرش معترض بوده که وضعشون از بقیه آخوندهای مشهد هم بدتره!</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/farahmand_alipour/6012" target="_blank">📅 19:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6011">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">اینکه خامنه‌ای گفته :« ما از زمان کودکی با پدیده مسخره کردن عمامه مواجه بودیم،  آنقدر کلمات تمسخر‌آمیز شنیدیم که این پدیده در نظر ما عادی شد.»   خمینی هم در سال ۱۳۵۸ در جمع روحانیون کُرد، دو تا خاطره تعریف کرد که روی وبسایتش هست. لینکش هم اینجاست .</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/farahmand_alipour/6011" target="_blank">📅 19:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6010">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JBuHBmINNg4wiMez3F-XCUwCh4n-_2LP_GWmwRlvnv3TFyB8RtDkVdxb-Zy4nGNuP-wdA10DlFbZHZ3V7DqWPXgM6jJi_nBBZnfe_VWYMtMZVTwM3Gkw2PHhpNwx5Q94VeSu6SgJCCxIPXPNGYI1f0EMhCXR44ZpGDsZeziddZoIIatPBWIGUFywliuc8Ua_-t0R8rx1NXDW570NgtDN5LEjSln8aVO5c1ZPYPUopYboMTfzkUbascvXkreIKjppVfb7XzKleq3GoqDFwbxxxuEigMvroiMAWjN6zjiNAYNdzrFWaDGyALxHEazfkLoMoyO8bvmEuGzgrWQgGpGQCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای بارها و بارها در خاطراتش  اشاره کرده که چقدر از اینکه لباس آخوندی می‌پوشیده و مردم در زمان شاه  آخوندها رو مسخره و تحقیر میکردن در عذاب بوده.  چه در زمان کودکی که بقیه به خاطر  لباس اخوندی که می پوشیده مسخره‌‌‌اش میکردن، چه در جوانی   او در خاطراتش…</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/farahmand_alipour/6010" target="_blank">📅 19:44 · 19 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/farahmand_alipour/6009" target="_blank">📅 19:33 · 19 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farahmand_alipour/6006" target="_blank">📅 19:00 · 19 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6005" target="_blank">📅 13:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6004">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">اکسیوس به نقل از میانجی‌گران (پاکستان - قطر) : حمله جمهوری اسلامی به کشتی‌ها توسط بخشی از حکومت جمهوری اسلامی طراحی شد که مخالف تفاهم‌نامه با آمریکا بودند.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6004" target="_blank">📅 10:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6002">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/snnzMcz3inFmx6TanG6GRCd7O9p-D-ITlYAnw1PO4pKhyTt9TcHO75KRhdMUBBV3y-9h84lyQeZQ_bQEydzSFmi8B2jDyz3vaIPy-EY8vtx7mkIG6gTtgjxrlkeW6I7OX7JK56UMSD2r88bFsy_EguWzvxYwAVvYh2o0XJDKWlksI-VTqaurAUMFvbWRXI1PVjAWQ4eLDOW75Y9WmMcYtM9y6WD78p5DmtVEiZsMzRn6MJA6HQJ-Kh5qmTwvEErLU96wwVkia6sSK-_hYlFGbOfQwtghUEQFPOoiLt6NjA9vgHY7UBswCXnUmifw0ulJoeXN_rXsy1AXxJSnAI8Gow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f2581pEOawJV4mFu1HSOkfAfRRmx88xCqz9n_xBfcTZIT6BqUIwdK-sU5_zsA1F5lqeIc05FAY1PqR5RdLZN7XeSfaMtSI8rhEpb8eY_iMU9FkEv8Evfws39KOLkyAO926Lqy-jhTG3dssgp1yfEkNPMJl9-WDUG9aVRi59IDnausAglgx1DN9b5xf2Q1-6qZnZSyY5IfUDSES9TKJX-5UUDfQ83HG5dtv-6bcyiEAlnYS2HEFXPmkOYGFYJkyhenBTO-MiHCsav0ZwU1hiwiGeQm9URhdH4NoKYQpMQbUw7V8nzk_YgMxJ1qdtWaj9PeoDrm5c9d8jgdHg0DiCoHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کارشناسان و منابع رسمی شما  که این آمار و اعداد رو درآوردند، احتمالا همون‌هایی هستن که به خامنه‌ای گفتن در سراسر دنیا دارند «سلام فرمانده» رو میخونن و خودش اومد اینو گفت!  همونجایی هستن  که بهش گفته بودن  نفت آمریکا در ۲۰۲۱ تموم میشه امروزه   در ۲۰۲۶ آمریکا…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6002" target="_blank">📅 09:46 · 19 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6000" target="_blank">📅 09:35 · 19 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5999" target="_blank">📅 09:19 · 19 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5998" target="_blank">📅 09:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5997">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qnekhk6G9gitDyPDZAw2NtW9oXaN22gYXz_9JlkcBegjoOEBqadvSBFdUQJfTJ0-UJZxlHKmBzLlGmZoMtlv1t7BPC-ES53uHwX_jEq13hbRAa1nraD2StHvYPWuK3hPvfj0SRcti8HsqhJir9seQdWRe9X3MPcbHfCC_3E16L1xe_boi1Wzqhpq73fVsTT4RpwsXIdtEAv6VgSSXlFeoFtQigT1l6wqiP5o0rkV8dwfcsMwOX4flNoA76YLVsCgVKnzSgXyfeM9d5lzJuzM35zo1BPLFpgOLV-fteiuLdCZstd9bAEc5bAwGkyCh17FgWByH_xEmD81g9c6xKuChQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سی‌ان‌ان : اسرائیل اطلاعاتی در اختیار
آمریکا قرار داده که نشون میده
جمهوری اسلامی طرحی برای ترور
ترامپ در دست داشته.
(این چند روزه در مراسم هم پلاکاردهای
بزرگی به انگلیسی در دست داشتن و خواستار این‌ کار شده بود، مجریان تلویزیون، مداحان و روزنامه کیهان هم همگی صراحتا خواستار این کار شده بودند.
ترامپ نیز در ترکیه، زمانی که از تفاهم نامه خارج شد، حداقل ۳ بار گفت در لیست هدف ج‌ا قرار دارد.)</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5997" target="_blank">📅 09:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5996">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های حکومتی از حمله مسلحانه به بسیجی‌ها در مشهد خبر می‌دهند</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5996" target="_blank">📅 01:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5995">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">فرانسه ۲ مراکش ۰
دقیقه ۶۵ بازی
تیم فرانسه در ۵ دقیقه دو گل زد</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5995" target="_blank">📅 01:02 · 19 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5994" target="_blank">📅 00:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5993">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pabgq-du6dDgLFpsDNMCzU5VShy3qM5jEn06jg-3MbuepfgVd7fuTEIi5hUwXjKM9_1MFa5fBZStC8APTW7m77xLob2kSXU8Ujvz3kkXZ8wezDDG8-9Nac7Yl9HMsIwNWQXGHrOp2eqArf6QEgYoGhn5g3Hq7-BEOD8ByLc07dpAPt9wjfjBbgOeitYWYzgsA8Jt3k7ReChTcOhdkWJ8dPPj3GMKxv1hBnxqneZZpVut6EoUe-2XW6GwQZVKYaZ7k0QrrQ8JPEFDQKK60jDlgwpydHoIWvC8IPpo4dygreiKJ62t1ujiRuQNPWxzhCN35khuuhgq55S_JP8GpOB1uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های حکومتی از حمله مسلحانه به بسیجی‌ها در مشهد خبر می‌دهند</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5993" target="_blank">📅 00:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5992">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">فرماندار کنارک از وقوع دو انفجار در منطقه نظامی نیروی دریایی این شهرستان خبر داد و گفت:
این منطقه شامگاه پنجشنبه در دو مرحله هدف حمله جنگنده‌های دشمن قرار گرفت.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5992" target="_blank">📅 23:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5991">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">صدا و سیما : هیچ انفجاری در شهرهای بندرعباس، قشم، سیریک یا جاسک شنیده نشده است.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5991" target="_blank">📅 23:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5990">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
گزارش‌هایی از یک ترور هدفمند در اهواز.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5990" target="_blank">📅 23:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5989">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=quRvkxBN-Xr-wOx4666BodHr-JIZ-AkArTAv7Ob0DaVZYl4P7VqxXPpRBYPQL0NqN_mKyQlnT930riRGJJ-K1dvEIWwP3w1S0iV_dUSVeJbEn_pY8MOih8LDWO4xSG1tXmwtg5eT0iM604W1c-mNjAFCgefmPgYWq4NZVEL1pdrgx_WX0FSl0VyGp9m1hH87wTxA7ICaeKc9BDjem6Ejr45t8ywgAUaPBJe3evlKGxrZidzZ02ULbzomHLGbDOkaGmxwTBflgAb6-L-4rLy0zDKjLb3iH7_CLAWeI5tiGoPFzqzTnmo4M0GlsUtw-YimFqtrW6YjHMFc6DwuiJAZ_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=quRvkxBN-Xr-wOx4666BodHr-JIZ-AkArTAv7Ob0DaVZYl4P7VqxXPpRBYPQL0NqN_mKyQlnT930riRGJJ-K1dvEIWwP3w1S0iV_dUSVeJbEn_pY8MOih8LDWO4xSG1tXmwtg5eT0iM604W1c-mNjAFCgefmPgYWq4NZVEL1pdrgx_WX0FSl0VyGp9m1hH87wTxA7ICaeKc9BDjem6Ejr45t8ywgAUaPBJe3evlKGxrZidzZ02ULbzomHLGbDOkaGmxwTBflgAb6-L-4rLy0zDKjLb3iH7_CLAWeI5tiGoPFzqzTnmo4M0GlsUtw-YimFqtrW6YjHMFc6DwuiJAZ_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌‌های مجری شبکه سه و تهدید ترامپ</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5989" target="_blank">📅 22:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5988">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iIpLlTI0pELFXOsNeFkZw5ajMZbyea7hENTtUPJQpK7rD4cqzItgPA8iR8ItnUvuhVuvAgH7jxbhBcTZN3eXjPTJLgcstdANXgCfoK0ZpniCxfJdxOFNUlftaaBcpkoeLYy7mRYnH_MJOK-ARIWvQal1GomGdPcpcYKC9lPU0pxunj7KWeykYuFBBU1BmH6IAVsrCY5q6cTfyyY3_FIUatv7Wb6AuO3qvIFlbiGK0iGNIkR7zRzwO-K0blK5YxkxqovFuOEP5N0CndrQERqAugZUHuKoZeNG_XDCu8jw7bLKO1y7l-8w8g-luImbBe6tcCK9wWGRKdbg0zxs22WlvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گمانه‌زنی ‌برخی رسانه‌ها:
حملات امشب احتمالا کار
کویت و یا بحرین است و احتمالا
حملاتی موشکی به ایران صورت گرفته.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5988" target="_blank">📅 22:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5987">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🚨
آکسیوس و العربیه به نقل از منابع خود می گویند امریکا امشب حمله ای را به خاک ایران انجام نداده است .
ممکن است حملات توسط کشور ثالثی انجام شده باشد یا صدای شلیک موشک های ضد کشتی ایرانی به سمت اهدافی در دریا باشد .
یک مقام آمریکایی هم همین موضوع را به سی‌ان‌ان گفته.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5987" target="_blank">📅 22:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5986">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fffbd82aa6.mp4?token=EFoyVTj7KkeocAjT3AO7FEPm8swzkBIlAmf7qI_tQ6tHXF0D1DWHl476f5isT1TZvAdiAqgmAXcPBe_0DijsbrA14IHS3mWlxhoc6mLtdcasZqMZUGBXaqQ2UYCNILv3KmdzVm-FnPIMYPssv2vhrL6l_H4giTwchowJ7-IdOQkwTzBbB2wAJVaPiI5l0rWj5WCW1X-HnhMYv1v2E0DGFwVgrugW5Xi9GJ1pQthaZy4IHnK-XL3BOrV5GCsWEGkU-yVgF4ofjtn0YP5SwrN9XhEfGKxua3rxkZ5oeN7kLabW4FZAJaUaqGaVUX8csxG9JDuPJR2bf_Y4_PYXWIDj4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fffbd82aa6.mp4?token=EFoyVTj7KkeocAjT3AO7FEPm8swzkBIlAmf7qI_tQ6tHXF0D1DWHl476f5isT1TZvAdiAqgmAXcPBe_0DijsbrA14IHS3mWlxhoc6mLtdcasZqMZUGBXaqQ2UYCNILv3KmdzVm-FnPIMYPssv2vhrL6l_H4giTwchowJ7-IdOQkwTzBbB2wAJVaPiI5l0rWj5WCW1X-HnhMYv1v2E0DGFwVgrugW5Xi9GJ1pQthaZy4IHnK-XL3BOrV5GCsWEGkU-yVgF4ofjtn0YP5SwrN9XhEfGKxua3rxkZ5oeN7kLabW4FZAJaUaqGaVUX8csxG9JDuPJR2bf_Y4_PYXWIDj4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا در مشهد هم دعوا شد :)
چند بار زیر این تابوت دعوا شد؟
توی میکروفون به نیروی خودشون میگه خودت رو کنترل کن!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5986" target="_blank">📅 22:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5985">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5985" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5984">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vzvPUpQY2QSHSRHWxAKxUqfzCuPeg7qMV_iXz54qbmbdBb_f89e0zV2EfKUXYkGkkgjEl-tMMVjJR9OpmzEr3Zba-hu-qs74x00hyUEpUJ95YTOLMjxV94frPukKWFyxo22ZDxDQX2SKpTWzIqVHTip_FLnfTtJfidzFFp0KP_rWRp4M_fVust37mmjBwxwAe6GYMhfsiQSgzx4AD1jQg865VqhCbOZVAAcyBRxdCw5gVd-Sl8_s0C97RRxVjxNW8gfVka24SpzTzmhtJdMc3cgHrVyTJPRicDiGWyz8BW3en0XNgNahzLB8EWD_5UdlSu9yvMNZvP4pE59QHrftcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آماده سازی قبر خامنه‌ای در مشهد همزمان با حملات آمریکا به جنوب.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5984" target="_blank">📅 21:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5983">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5983" target="_blank">📅 21:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5982">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5982" target="_blank">📅 21:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5981">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">‏پر از خون دو دیده پر از کینه سر…
‏شش‌ماه از کشتار دی‌ماه گذشت.
🖤</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5981" target="_blank">📅 21:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5980">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EpQNPHCTChJNPuVvtDyNOnGJwtO05mfaupoA7QP1AeT2OrB8beePmNvjxNPdBphxqEV7jM8NT3f0sbr_RDZSDv3k7dOYxWMZlojG8d9XFg8kc9GLqNphGl4YFTA8FpOz_Ieo_5HzLKKr_H__KPlymsm8nIc1bUgUnmTqkp1m0jKZ1RoISkAv0oDqmq_TegpuMakhPpEXjPulDg5REIXpNSeok-BH0FMyH6YkHcWs_ILfvbIyccnCNrI5PNxk6zWClsrkpdemSedzzJ2rlQ-P5rmyZPaAQWGZtiHOEOvUu3LF1lgk5s8qsZc5YE5FYTL1HfeEnSPG8TqrVaj7_z6D0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2075261040867037280?s=46</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5980" target="_blank">📅 20:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5979">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=NAca7VB276W_55iLDgKTOtOJEBBrZzuGimPyt3loOsTKBYN8tMtzgVCNa600aezZ4zT-2wY8wxzKdF4O70461zWRS1O90g2mS5F1WWsKNcxVkUr1sxi5MZvcYiyv1H7Ae9F3cETakYXz0prc6hIe2nG4Wc_m8JcvYp7w3OezCslK71qKS6_XiuP34b92invRDnRL_YiNQMnFGKTlmi6l1JZynn7kkLSAHC9jJ7tkhA0085jEqMJSvXx_YqaqHf-LTwSpI8BJSjCVM1VMtfMMHTOPCIUAU8xnB-ZkzOKRTHt0my6k6FE8m4ksSIL07JEK8kQ5ZsE958ADo296il7sTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=NAca7VB276W_55iLDgKTOtOJEBBrZzuGimPyt3loOsTKBYN8tMtzgVCNa600aezZ4zT-2wY8wxzKdF4O70461zWRS1O90g2mS5F1WWsKNcxVkUr1sxi5MZvcYiyv1H7Ae9F3cETakYXz0prc6hIe2nG4Wc_m8JcvYp7w3OezCslK71qKS6_XiuP34b92invRDnRL_YiNQMnFGKTlmi6l1JZynn7kkLSAHC9jJ7tkhA0085jEqMJSvXx_YqaqHf-LTwSpI8BJSjCVM1VMtfMMHTOPCIUAU8xnB-ZkzOKRTHt0my6k6FE8m4ksSIL07JEK8kQ5ZsE958ADo296il7sTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربها در حال آماده کردن مراکش  برای بازی امشب مقابل فرانسه  امشب چه فرانسه ببره، چه مراکش  مسلمین به خدمت پاریس خواهند رسید :)</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5979" target="_blank">📅 19:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5978">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=JX-tznTfJu527isHZN3RN-SU5szacZQZOhuytkAxp0Fvz7zIcHHtvs8KPREGBjsgO64x_GOuiRYrdUEe2IRmPFavFXZnkb-7MR9N51fSkpt3kWKA-Gffv_2McgiuIKRoo7PGv0ZoX5pCP6dhRLJGmHquzws-a51Zro10ktn_nZvzd937Fytu21I4B4YD489A2yOz6wgTx-LmBDEdSPLuk6Bw__yL7qfAji9k72liV375nzqXTK-XFxhCv2mAVL6uhi7hr38bWtAXFLAuq-wfb-O32gj_rf3Qxnt-nok18efuozk6smv-T6ii0vUdLQDUdG7DB2jz8opyDamUgFfpPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=JX-tznTfJu527isHZN3RN-SU5szacZQZOhuytkAxp0Fvz7zIcHHtvs8KPREGBjsgO64x_GOuiRYrdUEe2IRmPFavFXZnkb-7MR9N51fSkpt3kWKA-Gffv_2McgiuIKRoo7PGv0ZoX5pCP6dhRLJGmHquzws-a51Zro10ktn_nZvzd937Fytu21I4B4YD489A2yOz6wgTx-LmBDEdSPLuk6Bw__yL7qfAji9k72liV375nzqXTK-XFxhCv2mAVL6uhi7hr38bWtAXFLAuq-wfb-O32gj_rf3Qxnt-nok18efuozk6smv-T6ii0vUdLQDUdG7DB2jz8opyDamUgFfpPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربها در حال آماده کردن مراکش
برای بازی امشب مقابل فرانسه
امشب چه فرانسه ببره، چه مراکش
مسلمین به خدمت پاریس خواهند رسید :)</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5978" target="_blank">📅 19:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5976">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=OTKpHv6I7dmxk34bnfDLnu8BKBqSKNVuDpO-VdBUgiGS49zxzCQKzpwxhxKfQUgKoDe8D2WknPMsHpZsC0ySyncMXgo6KHL8MTF4EC_4ZZ_XLUo0-Cy36ZLPpKTLDYxCGmtXm5P0pavmGR-u_UaE6G4zJjF0oIuwKuDDG8yv48-ZpcCgHDsF6-34sAnWcPlNeT3ffL43EcQWpnS8X1h_-bBJQFbxDNbwjDH_-RSkh-pJPEsKEwb6qmO9UMXslp7GaI5EWt1Ctbh_S9gtErvqw-uHAerzUWfPotANB5Gjx5nZgjYkQs8Oy7YHSnfglvnXqYvj0t0w3sEYdh77NEVGUKKFh2PIQsTP1i-ClzovLFIi2CSJ-La4Ncuyj0KoNuXwKrfUOKwogiy0xARGiAhSxQdaZVqNGv0BPGVU90_fZHTNz7eGVx0P1E4gcyAswFpFcXuUZFNAN0pYYGx27gY0ZdBc4TlWGm-UEEmtodwiS71CE2RjG3SVUk6y1TNUbLJY5wYyGh5uhfVJ9_AV58-Chbf4oJM3yP9T88vaPiMbS98gYFUiVJDxdoGFafCeidmD5Ik1q3W3_Ubpw7GHoaVqSabEU1Xt4mk6RKGmk3mYbYEiRw0MWxt0ECXNMvTz7S1gH5DKmGPu30qD0u0ijNGCXz3GYTdfAnE3fyYpt9I07Es" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=OTKpHv6I7dmxk34bnfDLnu8BKBqSKNVuDpO-VdBUgiGS49zxzCQKzpwxhxKfQUgKoDe8D2WknPMsHpZsC0ySyncMXgo6KHL8MTF4EC_4ZZ_XLUo0-Cy36ZLPpKTLDYxCGmtXm5P0pavmGR-u_UaE6G4zJjF0oIuwKuDDG8yv48-ZpcCgHDsF6-34sAnWcPlNeT3ffL43EcQWpnS8X1h_-bBJQFbxDNbwjDH_-RSkh-pJPEsKEwb6qmO9UMXslp7GaI5EWt1Ctbh_S9gtErvqw-uHAerzUWfPotANB5Gjx5nZgjYkQs8Oy7YHSnfglvnXqYvj0t0w3sEYdh77NEVGUKKFh2PIQsTP1i-ClzovLFIi2CSJ-La4Ncuyj0KoNuXwKrfUOKwogiy0xARGiAhSxQdaZVqNGv0BPGVU90_fZHTNz7eGVx0P1E4gcyAswFpFcXuUZFNAN0pYYGx27gY0ZdBc4TlWGm-UEEmtodwiS71CE2RjG3SVUk6y1TNUbLJY5wYyGh5uhfVJ9_AV58-Chbf4oJM3yP9T88vaPiMbS98gYFUiVJDxdoGFafCeidmD5Ik1q3W3_Ubpw7GHoaVqSabEU1Xt4mk6RKGmk3mYbYEiRw0MWxt0ECXNMvTz7S1gH5DKmGPu30qD0u0ijNGCXz3GYTdfAnE3fyYpt9I07Es" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرچم روی تابوتش رو هم کندن و یکی دوبار هم تابوت رو زیر و رو کردن</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5976" target="_blank">📅 18:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5975">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pvLevNex5YAhmGB__T_VpGVveXuo98YCw79qqINwAwZZscIE8DGByiMKdqpZsLqIrnNslhHQZvrX8KLY3cvIBpIMZ_98MwSM3nwPkEzm6YcOL6a9RcLtjHKEdmk1TKam0l--JPFhGRsW5n_Sz3gQHkvmRhcGwi3IndvN4nlVHZy5wkyOCO8unp7DdkgZED1w_ZCKwsI-R6QhGPsPEl-iDcjSzngz5xqfyxQx6nBHi9El1CSjGbsZ0QE0iNVsPTclP_kJBmRVmeVIsTlEwSmpUn3Zs_V2KrSFHgkuqcKdrcUden1btKCkFq6-xI2pznlo1y1U0fdbt_iZSMByQnH33Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمد وحیدی که الان قدرتمندترین چهره نظامی ج‌ا است.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5975" target="_blank">📅 15:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5974">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJQV7f4nVoA7BleEaiH9cOy28Tkkx1mB0tL_L3R0bcO4P83-Rp_W5gQesnpNDS8Yf3y4VBwhkZTQGBTpoCGiyjAJ-9HJXB7hzth5-FjWjz8JkZFzKuufKbpbejY4xqlkIbx4AflIXfiNWloUpnpDlqTXFpGxhXmk-006_mhy-e4KJKD2STUpcw5gG7eTACdXHRo6Sa3ZoLfK7pDHSwWtZRPaSHZwuN9bzFMfZVHavfCxzj8VYYYCEQnSaVSoh62U6EYGArzwzNYsC3_Wi5qB06n1PzSj7IgURyIaf9Lw18XO0_SrRkUS0EobkGf_AFfU2-dpCxF5MwgrCJFj2Z2GKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب با اینکه حملات متوجه شهرهای جنوبی بود، به یک پل راه‌آهن در شمال کشور حمله شد.
در ماه‌های اخیر، جمهوری اسلامی حساب ویژه‌ای روی این مسیر ارتباطی باز کرده بود، هم برای ارتباط با روسیه و هم برای ارتباط با چین.
حجم مبادلات هم ۶ برابر شده بود به ویژه پس
از اعمال محاصره دریایی توسط آمریکا.
فکر نکنم تعمیر این پل ، خیلی زمان ببره.
بیشتر یک اختلال چند روزه خواهد بود.
هدف آمریکا هم بیشتر ارسال یک پیام بود
که جنوب رو محاصره می‌کنیم و می‌تونیم مسیرهای دیگه رو هم از کار بندازیم،
اگه قرار باشه شما مسیر تنگه هرمز رو ناامن کنید.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/5974" target="_blank">📅 12:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5973">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6kArZK-uTZZuMDXY_9Zlp5KbaO70jzOFjet4nmoM6lucg2vO9b5lE7wwboLvPyOVJOLL7HssQSGKaTDJ19I42iye0YRibBSIN3XnmWDeaJ71C6Be-nrTGufTTYMwI1GSSobVat1nBR-4q2ohCkNwtnAwAb_nyYzDvlwntrANXW0d7vXk10Os1c5Df-GMS0w9ZjLhyqZKjKz3EA48Ae6e6u2AtTb9u7XNvy6xDl2m89GNF_Lt0FZOHlVJ8JlD_fbaQiYiJsXgCuE4cysxmTz0q00B63dI9tcitGvqqIfondJNLXJervzVljycddsVVZ_7HQkjeIZ4dfTjyQncTif2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منتظریم اول
خامنه‌ای پرچم رو تحویل امام زمان بده
و نماز جمعه رو توی بیت‌المقدس برگزار کنه</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5973" target="_blank">📅 09:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5972">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">بیانیه ارتش : به اهدافی در قطر و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5972" target="_blank">📅 09:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5971">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=H3qmBerLb_m6Pk4jGO63Y9aC5x5b0S4IsN_arKyXcQuxa4dVfoDABNt1NmbKXu3Yf0bjCtPOKB6jFVaNOn0qAS00VUy8eYNQYCw1YRYqr7dwVknPpN0vdtcv1QmAGuAyiWX3OCTE4HPMRfW5ZygH93zUokSea6OZ_bpK5ZJgrn1jpaB7NmxlSL9DznvDs7vDsFEMRgicpiK9i8yGtLw9ZsK_vZv92B_KOwFJQW-OXGYhlYCQ7-siCKHHdbRDs93ZyQENnW6zeUkm4VibyTEnQ1uMjna452E4UE5dUZeyuYaQgc7UyF_rsiOcqDldg6mfWgBALtnKqNHXK45XXMQZFTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=H3qmBerLb_m6Pk4jGO63Y9aC5x5b0S4IsN_arKyXcQuxa4dVfoDABNt1NmbKXu3Yf0bjCtPOKB6jFVaNOn0qAS00VUy8eYNQYCw1YRYqr7dwVknPpN0vdtcv1QmAGuAyiWX3OCTE4HPMRfW5ZygH93zUokSea6OZ_bpK5ZJgrn1jpaB7NmxlSL9DznvDs7vDsFEMRgicpiK9i8yGtLw9ZsK_vZv92B_KOwFJQW-OXGYhlYCQ7-siCKHHdbRDs93ZyQENnW6zeUkm4VibyTEnQ1uMjna452E4UE5dUZeyuYaQgc7UyF_rsiOcqDldg6mfWgBALtnKqNHXK45XXMQZFTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میانه‌روهاشون : «بهترین حالت برای ترامپ حفظ آتش‌بسه، اما ایران نباید این‌ کار رو بکنه، باید کار دیگه بکنه»</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5971" target="_blank">📅 09:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5970">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=Uqoes8vQ3nn4GYa8NsgNeU2sIL4LN8dAls-bck30YT3X6OGTrFrh1dMqdZ_l8Ao3MzIYBGyrUcoM3WGoySVvhFO5XovVPYsiUV3ig-ZnuQ4Be8rC60kuqQYCj3jIBXoskwkT1TS86xd6u_Fkr3Lm2CCP-y7A4IyKuyBlpCI1L11-Wukt6C76-19Y8Pl4Da9VCcg2znE4n8ucqrxDHJo4fRqde_VGF4stWGFq9DjjR1aLKaVmB0iBWTcnbDxJAbnY5UkS-81bZII1ZzDJf3JpP622osBiesoACePZRpQNl3MPwUvNKYIatgrNdUEDui08bjElK7Rp_ZI_9ygjipqG-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=Uqoes8vQ3nn4GYa8NsgNeU2sIL4LN8dAls-bck30YT3X6OGTrFrh1dMqdZ_l8Ao3MzIYBGyrUcoM3WGoySVvhFO5XovVPYsiUV3ig-ZnuQ4Be8rC60kuqQYCj3jIBXoskwkT1TS86xd6u_Fkr3Lm2CCP-y7A4IyKuyBlpCI1L11-Wukt6C76-19Y8Pl4Da9VCcg2znE4n8ucqrxDHJo4fRqde_VGF4stWGFq9DjjR1aLKaVmB0iBWTcnbDxJAbnY5UkS-81bZII1ZzDJf3JpP622osBiesoACePZRpQNl3MPwUvNKYIatgrNdUEDui08bjElK7Rp_ZI_9ygjipqG-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تابوت خامنه‌ای، پهپاد وار به پنکه کوبیده شد
و موجب آسیب زدن به اموال حرم شد.
یه تشییع جنازه برگزار کردن، هر ساعتش سوژه‌ای داشت.  گویی فیلم‌نامه‌اش
رو رضا عطاران نوشته.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5970" target="_blank">📅 08:47 · 18 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/736101eca8.mp4?token=va27Kr4MBM6zArVNx_XXAse1AcE4yckf33ta-MSQq3Bh0EueTWsdFUApV08SeYCesew2Unc2VBhWVBTZ-OeDxM1p8q_mWfbCbXmG9arle3kroJR95ZbRpwn3pmTDIVo1t-DaNE6tEVDpQn5kgMVvqsnH5MVgTiMS_pbHvGrOzYojS7sIiAUUGKdDjz52O3Kj5a9gGedifjdvApsbZ6It1uH8dXQ8AgnKa3iIysdAA_FqcB-Q1gqRpd6x9_CmX46A1TH-DZNjJuxX4TsWN0Yasu7-28GGRCGLn7zfLKMmmDQiThPU0DgjhmsUEoksJn3bPTFilETDp89KS0yJTNvMxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736101eca8.mp4?token=va27Kr4MBM6zArVNx_XXAse1AcE4yckf33ta-MSQq3Bh0EueTWsdFUApV08SeYCesew2Unc2VBhWVBTZ-OeDxM1p8q_mWfbCbXmG9arle3kroJR95ZbRpwn3pmTDIVo1t-DaNE6tEVDpQn5kgMVvqsnH5MVgTiMS_pbHvGrOzYojS7sIiAUUGKdDjz52O3Kj5a9gGedifjdvApsbZ6It1uH8dXQ8AgnKa3iIysdAA_FqcB-Q1gqRpd6x9_CmX46A1TH-DZNjJuxX4TsWN0Yasu7-28GGRCGLn7zfLKMmmDQiThPU0DgjhmsUEoksJn3bPTFilETDp89KS0yJTNvMxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون داغووون و پلشت دو عالم! برادرانشون در عراق و یمن و افغانستان پلشت‌تر!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5968" target="_blank">📅 08:42 · 18 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5965" target="_blank">📅 06:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5964">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=L2BpRz0JVbv2qDmpsAuqJjJEdy-SXsgb1S-tSaNbP46WIio1AfWMUyOUby8EVwO5FkzVfYhL5_fk7eaqpL0CZtG8zPBwYbXHo3WmdHi0RM-HHBad0PgipfSc1NF50iQRSgjHSRHU8HZz0gU9A5NCcDRX_WP-6doEKREoR0AvZdlVmYdTqnDd3qVuzvhl0olD9jC2qeUJaH8hLBy33W48wujG-VWB161xgq1Yp0jHqopjqhSVMmbvksli3SdCfdmMJBWeM837ZRnwDHy5A25NuUGSs5V41aj8LBoG7IqbcgaR-iy-OBaR21t-jRcORuY26usACHfqdJyqJO7LGng5aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=L2BpRz0JVbv2qDmpsAuqJjJEdy-SXsgb1S-tSaNbP46WIio1AfWMUyOUby8EVwO5FkzVfYhL5_fk7eaqpL0CZtG8zPBwYbXHo3WmdHi0RM-HHBad0PgipfSc1NF50iQRSgjHSRHU8HZz0gU9A5NCcDRX_WP-6doEKREoR0AvZdlVmYdTqnDd3qVuzvhl0olD9jC2qeUJaH8hLBy33W48wujG-VWB161xgq1Yp0jHqopjqhSVMmbvksli3SdCfdmMJBWeM837ZRnwDHy5A25NuUGSs5V41aj8LBoG7IqbcgaR-iy-OBaR21t-jRcORuY26usACHfqdJyqJO7LGng5aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏میرباقری در صداوسیما:
‏دشمن به معنای واقعی کلمه هیچ غلطی نمیتونه بکنه، بنظرتون میتونه غلطی بکنه؟
‏مجری: بله دیگه، رهبر که خودش این حرفا رو میزد رو کشتن</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5964" target="_blank">📅 06:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5962">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nF_JJfyAGweOe2pD13tg8bJne7sjcIrKV3Gy5EbQqiPwQizS8g8BJy1oOG02NhiFtfBSnGrNUJGqZC1nc6aPd8WHP8UMkq9q_H6EIU-69GsL-lQ0-3TbpSRzIvN2l9hftMdN_kpAQU24ZHp3O3YPZSzJaYmLVCEmZCoXxI4PlwBeFUdKOy8NgKo80qWJFh54SVwhKZw4kOepPN6e93n6rbs95UrL_MsTk_tnP2jAlMDxi_fuCqWjUodSHe9Sba-CEfuLTTLFCPOxdMMXX_eY6xISQ7YrFID_Thg-301bZTCjlLg7OkFu73DuLk7fRmwTWmf5L66z8Yduxl44wHhjbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=cTQaOHJXPd48lX67ISCWxXKto9MYuaV1QxN-qxYEVsXyF8IVy-v1aMy46I1zpwdLVuDb0hhaOkACZUkQJjZpOY8nTW3gWf21-pbYlS3Ba6H8mfRY-Pu2YegHdlMywSIgsS-V-4eUVv8rDC96ibaqkhdlk8MnxEQaVh0qTmvGVOjR52JYCUngpc8R8M2_sjShGkNEEH0CBB8k_eL091kRs2FBM75GXK0v7vvie5a4iv75qddQUqJTt1oVBwrynAHZb8H3EKssiglkvEaRjTzVL4GY-qfM8XERCr_dn7LOvoWgkf9ytQxAu9vQQUgpc-x-sZ5v6kd-xt0xrvXQ_mC0cl_qwsol8gXW6oFxFCvO1LHZymxiXMmLPVPYxnQobM0I91A2Uwuo_jnKCA-fGV10eBgI5VT6c4MTV1BHRBiiOGasIpRDSQUF716ddZP6Q4CbtZez0tGvHTT0iYgz2wOBsZ8Q22VVfKMFLgpiRhupdNzviY7I878NYNOiXE5VAKkUeaiSW8vgPHU02J4cdLRH9d7CIY11rXXuf6A3tyDkd_JsLVzhggm4sv9vEUzDf_ZBqBvL1pif_8UxunXAVj3zPvWISvT9iUlTTx92iVig5ALN98FjpKCMB00CMQt4WyLHmdSJObyPWfvlQFbCpHDIK_s2yCYqw-ugraPz8ItN6f0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=cTQaOHJXPd48lX67ISCWxXKto9MYuaV1QxN-qxYEVsXyF8IVy-v1aMy46I1zpwdLVuDb0hhaOkACZUkQJjZpOY8nTW3gWf21-pbYlS3Ba6H8mfRY-Pu2YegHdlMywSIgsS-V-4eUVv8rDC96ibaqkhdlk8MnxEQaVh0qTmvGVOjR52JYCUngpc8R8M2_sjShGkNEEH0CBB8k_eL091kRs2FBM75GXK0v7vvie5a4iv75qddQUqJTt1oVBwrynAHZb8H3EKssiglkvEaRjTzVL4GY-qfM8XERCr_dn7LOvoWgkf9ytQxAu9vQQUgpc-x-sZ5v6kd-xt0xrvXQ_mC0cl_qwsol8gXW6oFxFCvO1LHZymxiXMmLPVPYxnQobM0I91A2Uwuo_jnKCA-fGV10eBgI5VT6c4MTV1BHRBiiOGasIpRDSQUF716ddZP6Q4CbtZez0tGvHTT0iYgz2wOBsZ8Q22VVfKMFLgpiRhupdNzviY7I878NYNOiXE5VAKkUeaiSW8vgPHU02J4cdLRH9d7CIY11rXXuf6A3tyDkd_JsLVzhggm4sv9vEUzDf_ZBqBvL1pif_8UxunXAVj3zPvWISvT9iUlTTx92iVig5ALN98FjpKCMB00CMQt4WyLHmdSJObyPWfvlQFbCpHDIK_s2yCYqw-ugraPz8ItN6f0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا به دو پل در استان گلستان - آق قلا - حمله کرد. یکی از این پل‌ها، پل راه آهن است.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5962" target="_blank">📅 06:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5961">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=BbktplMHXbF1Y8Q7sIH9XHvGA4B2ZZ6iMbCdNtabZP8THPR9Owvu6hGaWx51h_MaVN0x3BdP47S8PDBXg3kdsGx1BNG6pU9NTtFPsHQjefQJnsZaBBT-e84UnNE7lF0gKSGToQZohXqg2bvTnbyAe7pfcYNdwMWYNvtm8ZUMYdMc5DyPsUz2_xiXcdvDTyQ7aWlnnk14-epJ9oynQZfNrRJF13yRCc6teg77CQxXnVz2-MqVv88HPz-cpNuUA4qyOqFyvjx75Qzp-n8Chj0Y7sc8HxojlRWIl-7fEse-pqMgp4CtV3TCqDSqJQgU1M7ZGlrHlSEpSUn7t1G8GEtbAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=BbktplMHXbF1Y8Q7sIH9XHvGA4B2ZZ6iMbCdNtabZP8THPR9Owvu6hGaWx51h_MaVN0x3BdP47S8PDBXg3kdsGx1BNG6pU9NTtFPsHQjefQJnsZaBBT-e84UnNE7lF0gKSGToQZohXqg2bvTnbyAe7pfcYNdwMWYNvtm8ZUMYdMc5DyPsUz2_xiXcdvDTyQ7aWlnnk14-epJ9oynQZfNrRJF13yRCc6teg77CQxXnVz2-MqVv88HPz-cpNuUA4qyOqFyvjx75Qzp-n8Chj0Y7sc8HxojlRWIl-7fEse-pqMgp4CtV3TCqDSqJQgU1M7ZGlrHlSEpSUn7t1G8GEtbAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : جمهوری اسلامی یکی بزند، ۲۰ تا می‌خورد.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5961" target="_blank">📅 06:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5960">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hJF-ln_rfFqi82sPsc0PyFcs9GriP4IjZc-G-ky0WLGhekOj_WsMfzB08FSIwrTVJfkrtWtjr9U3Lw930SdRxY6CsxRVQjoWwsdlR9jzYSDhnnl4oNf5KvnX4ZvYrhPEvZo2suiC2kydOHlyph6Dp_cVRdbhavQHf6MuCNkzv79L8GpuPMnOhS7tPTUAxpnzVnNVHf706tDwfi-ViTJrYroka6aa61siuGDejUY1q-cGLIpG80sdMa8wvo9J83VW63Vp3gY8qj-MbJa9nQptAHZsgsa7XNLTLv76r1_63VKUBIZwHohuKGv8e85VLcO7UyQgSpreorhorg7SktDY9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5960" target="_blank">📅 05:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5958">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=Gl08tKnM9q64pg3uZ-Wh2u83wnU6V2sQ3ljRqoOc1kc85tMWSjjW-La0lbWZIPuQJ8_uJ3YcG2X6p7MYSyRPH6bz-PN0zzsCU_RVosFVGeterLJSgIY9-PCH8g6s043Uvj0Xcoce58JoP4ZjKlV2f4u5p-VsqQFVtgl6XMbucWLxysU6UC8-c6QrG80l-g2nGRaxU99H13eApFAVCx5-Zyy6ULDC13_fDn8G_rLY__1jXf9Yy9NH7Sk2m7MGYVwWUQIIgZFp8LFS9pPeA_2dAEazpsQoHoL-EomL3kjku_ySzRQGHQ4MFlUSEGUhQwYj34M7SUOKdYUN3YFem50y0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=Gl08tKnM9q64pg3uZ-Wh2u83wnU6V2sQ3ljRqoOc1kc85tMWSjjW-La0lbWZIPuQJ8_uJ3YcG2X6p7MYSyRPH6bz-PN0zzsCU_RVosFVGeterLJSgIY9-PCH8g6s043Uvj0Xcoce58JoP4ZjKlV2f4u5p-VsqQFVtgl6XMbucWLxysU6UC8-c6QrG80l-g2nGRaxU99H13eApFAVCx5-Zyy6ULDC13_fDn8G_rLY__1jXf9Yy9NH7Sk2m7MGYVwWUQIIgZFp8LFS9pPeA_2dAEazpsQoHoL-EomL3kjku_ySzRQGHQ4MFlUSEGUhQwYj34M7SUOKdYUN3YFem50y0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکله و برج اسکله بهشتی در چابهار</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5958" target="_blank">📅 00:53 · 18 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/693dd42141.mp4?token=aH4ut_A9onQ4-yo-hHhPA0XOu4QjJTJ52uYlfEGbLrYfhmr5i-xGeGsqwrnwfMV-uutb4blJA-i3NCwU4KS5tSuP3MqPHCm4ILdEe1Rj70QmzBGgjWjlOIcLyLYGC0ufLykGPpqYi62E-MiW1dK263j_bbXGWBbKzQzWEK4J9fzNoPCAW5pdyADGn6VPdXkqp94Vg6Kgmeve9PADrfX0LV9FGr4cqnMabP83PxwYH7UYTUpIKFcs3rYxzL16bLoatQFj8gxyRRa21cHAY08V3bPkTt9tI-hotmBTbkVQFtlluMb_H44I9mXtasCGwJvBA9ge46CcwOAOKViH3w2XjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/693dd42141.mp4?token=aH4ut_A9onQ4-yo-hHhPA0XOu4QjJTJ52uYlfEGbLrYfhmr5i-xGeGsqwrnwfMV-uutb4blJA-i3NCwU4KS5tSuP3MqPHCm4ILdEe1Rj70QmzBGgjWjlOIcLyLYGC0ufLykGPpqYi62E-MiW1dK263j_bbXGWBbKzQzWEK4J9fzNoPCAW5pdyADGn6VPdXkqp94Vg6Kgmeve9PADrfX0LV9FGr4cqnMabP83PxwYH7UYTUpIKFcs3rYxzL16bLoatQFj8gxyRRa21cHAY08V3bPkTt9tI-hotmBTbkVQFtlluMb_H44I9mXtasCGwJvBA9ge46CcwOAOKViH3w2XjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش سوزی گسترده در بوشهر
🚨
کشیده شدن دامنه حملات به جاسک و ابوموسی
🚨
گزارشی از فعالیت پدافند بر فراز آسمان اصفهان</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5956" target="_blank">📅 00:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5955">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lM9-Ss5waKTDHB6iOaGMbUIqdKLZGTUJ6pmVit-SgmTCdl1dlPVDxVeRai_-GCCxpTbunDfaxfruV81DVjOW26Uzv1nk9iH_X_ihNGzER8yF-PPIi8rh989fIBqAXcWpMVrxYPEakB-IXiHlBAoIZ6XYifVqNz3IIWOe28ceIgp9F9Bk8RJ0P5_a6hiJdBI3xnN0xjnh1CswOhu36v1atJSP5-n3NPXAswLVoiMByO5J6kipwphQHTqQbnH-2rotaUuaaEYVjSH8fCAYY_LuSSWJyKvXvxf9bBml-8v6uon-FOr-vACDQ0U2YpF1j6-hwTrJS7Hz58BWPDi1qAfzVA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/2e3ae34ead.mp4?token=FK-pjy13Xuf8IIqqoMFN2mJTHibki5gZ3Rutoz80rMqxDnGKZqK5XzXrcEPDP_WE8WohPis1JEnD8fv7Bq8AevCzZE9-KSGsR6NvvoRpKJTnAUGBje7aas02LHKNHXXp1Cayw_ov6FbxFIbvJQDuduI5D1gbdqCoErR-v-XfmuKO6FO_9oWPQhkCQmGq6FzmsSyBPyIY08g1Q066TnjAabcbu-HZOWmVQFfdQEIsGC010Eopl0GfkR_UiMP3B0tIB-w_WeRrQybpw2xVzHPYQ3Zf6_Y4ZVwgzF2VpTjsadCkjtQdhO5WzTa2BGGU4-HCmpMEjZpztlugVix2VZZb2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e3ae34ead.mp4?token=FK-pjy13Xuf8IIqqoMFN2mJTHibki5gZ3Rutoz80rMqxDnGKZqK5XzXrcEPDP_WE8WohPis1JEnD8fv7Bq8AevCzZE9-KSGsR6NvvoRpKJTnAUGBje7aas02LHKNHXXp1Cayw_ov6FbxFIbvJQDuduI5D1gbdqCoErR-v-XfmuKO6FO_9oWPQhkCQmGq6FzmsSyBPyIY08g1Q066TnjAabcbu-HZOWmVQFfdQEIsGC010Eopl0GfkR_UiMP3B0tIB-w_WeRrQybpw2xVzHPYQ3Zf6_Y4ZVwgzF2VpTjsadCkjtQdhO5WzTa2BGGU4-HCmpMEjZpztlugVix2VZZb2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امشب - چابهار - حملات ارتش آمریکا</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5953" target="_blank">📅 00:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5952">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZqYKSjYpsyjgydBgdh_S5WArX_fZGWJz31cGXOFBVeoa1SCo7XVQuUer3aKaFETA2jgjS8DFWB3vuFYEVEFnzVDQGKFAhqb8jI2PHo6AukyvC1AYjPiILX2jWzvdtitYTYA9P2hSIQCDdwJBERQTxbHVEPD1AKc7Uy9pE7WKNZeP6ls2L829jUcI6mXpOl7wW72jVVRoCWyh4RdTE-jeMnAOMkcfX6M6iUlOt-Z7wM2IJn5gdnmtErZQmwm4zB8YsMXDv8vXMCxm5dsS_XjJkbuluOAX0vmacJLcj0P7yijbh1_Ajd_mptCsEHhM996F0V5MU8bSqBKEPDDaigKE9A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/a030961c3b.mp4?token=VXtFC1HG2ss_gUqRjPqNl8PVf-_9ynkqy8ajEi635naQH-KtRnyQM-YZxteH3iIT7w-WeqzxCvHzEgaExovqDSKYmrs_x5vJiCjxyayjMGqTvcn_wN8g2ASllJpk6v4lnLG9rQYeE6-1MpS_OGtRut2TC_EM2Rs8TZA_6KzKKY4BcxGgwOeAiB19YIvJ9ElUXVs8CJg-kDw49QKJjm0nYE11Qx7Ey9lLleblnTMJGWcG8z7kn0pq7D_1wNvfnbGmGivIjOwUjVFVyQxgcd-z1ksPl_NFp6t_8HImEwlJ2fS0I6VH3b2WDV9Z41eXce3AWSIJ7fYEKqrKnc5gLFbbDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a030961c3b.mp4?token=VXtFC1HG2ss_gUqRjPqNl8PVf-_9ynkqy8ajEi635naQH-KtRnyQM-YZxteH3iIT7w-WeqzxCvHzEgaExovqDSKYmrs_x5vJiCjxyayjMGqTvcn_wN8g2ASllJpk6v4lnLG9rQYeE6-1MpS_OGtRut2TC_EM2Rs8TZA_6KzKKY4BcxGgwOeAiB19YIvJ9ElUXVs8CJg-kDw49QKJjm0nYE11Qx7Ey9lLleblnTMJGWcG8z7kn0pq7D_1wNvfnbGmGivIjOwUjVFVyQxgcd-z1ksPl_NFp6t_8HImEwlJ2fS0I6VH3b2WDV9Z41eXce3AWSIJ7fYEKqrKnc5gLFbbDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از حملات امشب آمریکا به چابهار</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5949" target="_blank">📅 23:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5948">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ggkgzgj1eSxoYrMM_gfOFnk1JWNddu9GQDROGs933AUijY1AV9PSmNCJVwx_w2KCq3saEsl__F8ALgb20nLC6IYo_QszT8-fSYTUELgwgFnTEow4d0yAKm0p-lB561mjcuHcA1bH-vJ8p_bQ-0x2JwQSAWqLmclj3sMnbsHyq8CT7IAFJUNET81b_ynEN9E6STV4_qkyfC04AFGXHNuzOUgL9x7Sighg1Ljap5OKSBcVao_BvX3rumU6VlRndCOHgxB8zdBE4bHi3ezzi2xMDDihaqBNBe65-g-45F4CSTwmWRtn8XJ5t0tLnFkMnjbqZgQ4QfH5qSLp5FNu4u8V7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به اسرائیل اطلاع داده است که قرار است امشب حملات گسترده‌ای به ایران انجام دهد.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5948" target="_blank">📅 23:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5947">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌هایی از شروع حملات آمریکا در جنوب، حمله به مقرهای سپاه در سیریک و بندرعباس.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5947" target="_blank">📅 23:35 · 17 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/4c3530f756.mp4?token=NnTP1L5EoZXJwoL094GoeM9HEOrU7AfzHuR7rSU2QBBg0U1fJueZ7hHCMOZtdeuAMJ2ulig25w4WQ7NcDmVdWhTtsLCkrf6LeFCxNjPci6jvRONdLqbIq8rqp_u46pFLqMAdzUme4J79DcTMKxOQHixmDAK9ovztoDpuvkaV9Y1kxctzpzkPsOiRqSn16oKhCrQhRs7jD9g-5ZA4y0QvDVtmNv9OAsq-kOG0S1jLOXLllCx8cQbGwtzdPtzdXscMhJkZ4Cy0_1rrLF6ZmoQCTXKQfypAdlKuXZkjqXTc0K8IkE4_14_--qq29ReZVVkAsH8cm6FjYMC_E2OKkjSsww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c3530f756.mp4?token=NnTP1L5EoZXJwoL094GoeM9HEOrU7AfzHuR7rSU2QBBg0U1fJueZ7hHCMOZtdeuAMJ2ulig25w4WQ7NcDmVdWhTtsLCkrf6LeFCxNjPci6jvRONdLqbIq8rqp_u46pFLqMAdzUme4J79DcTMKxOQHixmDAK9ovztoDpuvkaV9Y1kxctzpzkPsOiRqSn16oKhCrQhRs7jD9g-5ZA4y0QvDVtmNv9OAsq-kOG0S1jLOXLllCx8cQbGwtzdPtzdXscMhJkZ4Cy0_1rrLF6ZmoQCTXKQfypAdlKuXZkjqXTc0K8IkE4_14_--qq29ReZVVkAsH8cm6FjYMC_E2OKkjSsww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/fe5d27edac.mp4?token=HAxQoXabwVa_RO4wkNJLG3e7rEOlQyjbcIchLsdWbLKBh4JfIL87wqmhynp8wjjqe3Nzw7oM4soQZRQTnWBFPaIukYvDwF7H2xD_CkycP696zo_1ELlUglD7aPfjFaU35hiUUKBEv_Qts62kOaFuWQdHtp9K3EAN4trW-s4GAj7-0Zb81EoFW3IsGz7wJnjNGNa7FEbyWr0PZfbNGUm_0ysWzoN33VCy7xdOsUx7PznCN9pO6sawSG6JGXlDJWUP2h33jdYSHymr5cpOmIxJpqeZXyYvTkpxzBMjl5Il-YBaVqxWY6Ht9mtnUXBBOsBTNKV-w1I6mWQ9G7TeM3ZqqoKHmIrUoRsOr1IkBB_asifOaKR6xKMBx02InB9osPlH3ohwDxZ4aqEIkSdc92rDoH8cLKe-jRegBLR9JPIkMEZePHXK_9bcjU9VPOcXmanBViYFp5H1XHY1HdiHPsYDAkawoVjoLYaNyW1LlSQaLdLOzaCXJ9GhvuV8CYvVL82-NtW9wYw8aEw9FMNdY93VFKiok9KA0cExRFUuVII70EH826xr_90dvOHsjf3ZHUbPCanAXir5Us2c3GmJT4FyAMZc0qMiNivZC-Z7aLZ-nbqB7mW7tHKeUDLPtVizThdIMvHBgaovgY7HBED8edtrh1mLCPfUeQQ5p_rLbEkLDIM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe5d27edac.mp4?token=HAxQoXabwVa_RO4wkNJLG3e7rEOlQyjbcIchLsdWbLKBh4JfIL87wqmhynp8wjjqe3Nzw7oM4soQZRQTnWBFPaIukYvDwF7H2xD_CkycP696zo_1ELlUglD7aPfjFaU35hiUUKBEv_Qts62kOaFuWQdHtp9K3EAN4trW-s4GAj7-0Zb81EoFW3IsGz7wJnjNGNa7FEbyWr0PZfbNGUm_0ysWzoN33VCy7xdOsUx7PznCN9pO6sawSG6JGXlDJWUP2h33jdYSHymr5cpOmIxJpqeZXyYvTkpxzBMjl5Il-YBaVqxWY6Ht9mtnUXBBOsBTNKV-w1I6mWQ9G7TeM3ZqqoKHmIrUoRsOr1IkBB_asifOaKR6xKMBx02InB9osPlH3ohwDxZ4aqEIkSdc92rDoH8cLKe-jRegBLR9JPIkMEZePHXK_9bcjU9VPOcXmanBViYFp5H1XHY1HdiHPsYDAkawoVjoLYaNyW1LlSQaLdLOzaCXJ9GhvuV8CYvVL82-NtW9wYw8aEw9FMNdY93VFKiok9KA0cExRFUuVII70EH826xr_90dvOHsjf3ZHUbPCanAXir5Us2c3GmJT4FyAMZc0qMiNivZC-Z7aLZ-nbqB7mW7tHKeUDLPtVizThdIMvHBgaovgY7HBED8edtrh1mLCPfUeQQ5p_rLbEkLDIM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل برگزاری مراسم رو
انگار غزه است! با بسیج کردن اینهمه ستاد و پول و ارگان‌ها و…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5943" target="_blank">📅 21:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5942">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PnyhLYyMKyXuGac736ew5_ij3Zy0hN2khAlpJFhHDcchcP3n4DDOJnnAqGbiDPIp9GiPHHLW6u2ddX5tkQ1vXJkXJL2y3M1yChfDI2SMht562YZ6RbZm3ssLD8AQAHoYQSSLXFCMcdmZLPnr6dO8whWXV0CekTEwoVtt0UJ5zDhilSIwj8SBfeczLACj6Nc5z27orpYCUE7cp9EZttngu2WuDAWIzfYzv3sla_tZg0xSbb0fRxYq7mr1F0eDRDGqQs1NMcOdh9kqagdY-StuSwGm8IiDoSW6jaND9-g34-chPYVbDhDKQb1A27g59uR9B9V5-R9AaoEDVSp0VLV0cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: درباره جمهوری اسلامی کارهایی انجام می‌دهیم که باید ۴۷ سال پیش انجام میشد.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5942" target="_blank">📅 20:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5941">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c3c23cc7c.mp4?token=nuBW3bF2B2ZjkYZRo6SDVAEYemNsyMD4-boJSeacwrdfrLVLEyfw2wID6Dk-km-Vueg2dqYCWBzBYLD6GnPPLyeWi3ZWzWuiOQPvKOlqtw6Yza0RZGw4nC26z2yhRTRyu8zsP07aQnDg0eSmgJYyxO1lWJaFW1NrLyCPbcXsEIgLc92a6n9xu_OhyFZEyRzHBfJo-MhMiJBh9aHW8Sgk6me5UvnIaTUwyaXM0kLT6niXU6VwBZo9-fG37lMaItqodztAwN0AmUCVGLpDOytozXiO3iVC-Qt-NAWKXb7fTUikSN_9LZ2tG38W73i9A99cfqgmkgSoS3m5HRSNnTH61Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c3c23cc7c.mp4?token=nuBW3bF2B2ZjkYZRo6SDVAEYemNsyMD4-boJSeacwrdfrLVLEyfw2wID6Dk-km-Vueg2dqYCWBzBYLD6GnPPLyeWi3ZWzWuiOQPvKOlqtw6Yza0RZGw4nC26z2yhRTRyu8zsP07aQnDg0eSmgJYyxO1lWJaFW1NrLyCPbcXsEIgLc92a6n9xu_OhyFZEyRzHBfJo-MhMiJBh9aHW8Sgk6me5UvnIaTUwyaXM0kLT6niXU6VwBZo9-fG37lMaItqodztAwN0AmUCVGLpDOytozXiO3iVC-Qt-NAWKXb7fTUikSN_9LZ2tG38W73i9A99cfqgmkgSoS3m5HRSNnTH61Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - اسکله بندر عباس
زیر حملات ارتش آمریکا</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5941" target="_blank">📅 20:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5940">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dd51af5b9.mp4?token=FUdYGZC6krfzH1XX_hRx36w-KVE4w5fUa6hbgnFM-jZKLzW3bSDqQMADXTT1gxVGLX6nBAOZe25_0_182yiPvDGCHZHJuM8RoRkQxGhfQnxzADZZ3BRC0ecF-SWsCEgR66p-NEoWNotiEt19C5STWcLzGj-0mRonjlgVT3koGqrEVhhvvA2fV49kAQTXQFXWlMZNOQAOa6th6BrfGslgyY_sPK6SS0-yirSMYvaVlBwWil2-Rzo433CyOx9zYZ1qc-WYJR5XLVOGjmnAtT_Y0Gxd6f6JHqLgqdedEappFrGOHu8ezAAP8clbnCfr_ALCE5DhuigmTpwgNfXYqET3Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dd51af5b9.mp4?token=FUdYGZC6krfzH1XX_hRx36w-KVE4w5fUa6hbgnFM-jZKLzW3bSDqQMADXTT1gxVGLX6nBAOZe25_0_182yiPvDGCHZHJuM8RoRkQxGhfQnxzADZZ3BRC0ecF-SWsCEgR66p-NEoWNotiEt19C5STWcLzGj-0mRonjlgVT3koGqrEVhhvvA2fV49kAQTXQFXWlMZNOQAOa6th6BrfGslgyY_sPK6SS0-yirSMYvaVlBwWil2-Rzo433CyOx9zYZ1qc-WYJR5XLVOGjmnAtT_Y0Gxd6f6JHqLgqdedEappFrGOHu8ezAAP8clbnCfr_ALCE5DhuigmTpwgNfXYqET3Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه مراسم برگزار کردن … ستاد برگزاری ، هزینه هنگفت، ده‌ها ارگان و ستاد زیر نظرشون.
بعد کارهاشون رو ببینید!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5940" target="_blank">📅 19:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5939">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I9BA-aa0GnQ2ZRI7zXn0kPEldQux1ARwgKbxlq79saFd7uxJz3LKVjl_hlwgqjvIAL5beFs-VxdkQV7Zzw5Jx9m9kRJvN6wpneYLAWUWbttr5cq3jLu8VWcKs9PnoCkOtDktHT277CliyQoYEWbSqzRaDeMBrc54wcoToW7B_jBVoCAF6a4gX9l2yPYvt_RVuINwwnNDWXHFWcOYJEKm4QsILA5iJksUqFV9BbkTlgptgAa4ydk0S7-NJRloeQRBtv31VIBCR7N1MTRbgU3RA2i6MZG3cUMdoOvyznVmmP7D73sr8BEtgld-TmZkokuuY7u2ScqwBGsOUZc2OtUPSg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=ZljEJFinMJZLbgqk8wYonzlFMF7v4yN3tnY32w699Dg0x8dQlJe-NgJZcpzNVhQvQx9m13kAtJ7J2oWe-gwSSw3CJW9ed71OHpoBYrKVpozEHqsRui42rQrv0U9yOJtd_ne_-1ntlSoU5H66fYEfhF0jA9qDkOMz6AwLxWujXPimpe7Zvrv-E60NpeM-I4pepFUiuZ4KbwNhF-DDH2Ux-bdw_C5YBfPVrwerTCYZ8G4FR-8Mbgy9aw5FXSgd4w0uJTe_0BNVuaQixDrWyv6eiGkuGUgh1ufMHw7NCUGC4Rrz-qrtI9czox14btNLVst6jyt-7W2ryynv7S4gDl-ybA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=ZljEJFinMJZLbgqk8wYonzlFMF7v4yN3tnY32w699Dg0x8dQlJe-NgJZcpzNVhQvQx9m13kAtJ7J2oWe-gwSSw3CJW9ed71OHpoBYrKVpozEHqsRui42rQrv0U9yOJtd_ne_-1ntlSoU5H66fYEfhF0jA9qDkOMz6AwLxWujXPimpe7Zvrv-E60NpeM-I4pepFUiuZ4KbwNhF-DDH2Ux-bdw_C5YBfPVrwerTCYZ8G4FR-8Mbgy9aw5FXSgd4w0uJTe_0BNVuaQixDrWyv6eiGkuGUgh1ufMHw7NCUGC4Rrz-qrtI9czox14btNLVst6jyt-7W2ryynv7S4gDl-ybA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دشمن هیچ غلطی نمی‌تونه بکنه
مجری : خو اومد خود گوینده این سخن رو زد!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5937" target="_blank">📅 17:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5936">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/046bf7600e.mp4?token=OgEdRGA_5cLW7udv9IKLYIkBNNIY4b26QsVDQuMDJSTIuapXipZIf_AuPgGMrGSyALIUH4zYdjpgVfhpDdrVfC90-P62iLPcqVsSLY_5O-lf_XFQw8ZbyrdZJocBlHhsSF2NoGCHfKVlAT0wneeRxTWGKD3Ws9DrQ1420Abv8V3bBPtwI3LHJmUvIrL65DRW1IL91c-XdbdoeOUHLOgOoArMbj_l9DSVthvOqLupiYHHKuIP6F0Wj-HH95ci8jWaPvNCA-rxMNm7_qnhiM6pa-_dh5p0K7qwEFy7W7-EK-rO5h7cHORjCpTqjnGm2hqMFkgn7XawJVYZNmKwb_4OXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/046bf7600e.mp4?token=OgEdRGA_5cLW7udv9IKLYIkBNNIY4b26QsVDQuMDJSTIuapXipZIf_AuPgGMrGSyALIUH4zYdjpgVfhpDdrVfC90-P62iLPcqVsSLY_5O-lf_XFQw8ZbyrdZJocBlHhsSF2NoGCHfKVlAT0wneeRxTWGKD3Ws9DrQ1420Abv8V3bBPtwI3LHJmUvIrL65DRW1IL91c-XdbdoeOUHLOgOoArMbj_l9DSVthvOqLupiYHHKuIP6F0Wj-HH95ci8jWaPvNCA-rxMNm7_qnhiM6pa-_dh5p0K7qwEFy7W7-EK-rO5h7cHORjCpTqjnGm2hqMFkgn7XawJVYZNmKwb_4OXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/8aff1f3384.mp4?token=AMEC0L0EZ4bOlPUrRpylqcfN9Lz0RoMK-WfS-kWyhNR8KAWNx70iXzXfFwfs-nLZS7fTZ0_oh6kyPhwdt5ggcHlR2j2RJbf0Xa9g-uea_WMF9ICZu3llGX3dpntlXFV5CRzN8SwkbgHAhWpd6MnIXkIQvk6pW3y5FV199MtiNJLPAQC0vh3mVrNTHhwjtu7UKV5TKgNxCT6HFirBJJD7uxPS3WbGssjIEyGgWSZcABXYr1ctwedBhe_he30g1oVfe1GdVK7cboj3Tf4okd2PI00HaGxuX8DkyNlJHsCAjXsHF1s8vxNDve8kOu0ciI4yVP84Hch-VR9leby47opU5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aff1f3384.mp4?token=AMEC0L0EZ4bOlPUrRpylqcfN9Lz0RoMK-WfS-kWyhNR8KAWNx70iXzXfFwfs-nLZS7fTZ0_oh6kyPhwdt5ggcHlR2j2RJbf0Xa9g-uea_WMF9ICZu3llGX3dpntlXFV5CRzN8SwkbgHAhWpd6MnIXkIQvk6pW3y5FV199MtiNJLPAQC0vh3mVrNTHhwjtu7UKV5TKgNxCT6HFirBJJD7uxPS3WbGssjIEyGgWSZcABXYr1ctwedBhe_he30g1oVfe1GdVK7cboj3Tf4okd2PI00HaGxuX8DkyNlJHsCAjXsHF1s8vxNDve8kOu0ciI4yVP84Hch-VR9leby47opU5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : اونها تحت یک توافق هرگز به سلاح هسته‌ای نخواهد رسید، اما شاید بدون دستیابی به یک توافق هم به این هدف برسیم، اصلا شاید راحت‌تر هم باشه، چون اونها دروغگو و‌ شیادن.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5935" target="_blank">📅 16:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5934">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5484fca6.mp4?token=AaBvHE2ym18ESEcHPPlFa8TyBKwb020oqYA43fQ8yo3nAXM3_uFZnGrCTu1MBCpKwLOS47-M6gIm1QTkoJcnNTTwcXsVCMII76kQa4TpiDKbT2K_gNMqNp255BdwjJDTpHplOuLkt7geCsGBs81Jx5rGIpxc_3NYYbyEWIpDV3uhCk6BM0xw_Ug5j9l_RX0_DyRTRpIfL-jax-M3z-BWMbnMA9GjsTj35Z8i83dZACXRidcNYdFIaWlxiU-BJtFRDqf-XsBLkT71HH1IipaaQun8dUdREfkwkwe6TGSVJSJkMljjVpKva_WASMkj8YTT-batSLsdHmlF2NINQ7q0zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5484fca6.mp4?token=AaBvHE2ym18ESEcHPPlFa8TyBKwb020oqYA43fQ8yo3nAXM3_uFZnGrCTu1MBCpKwLOS47-M6gIm1QTkoJcnNTTwcXsVCMII76kQa4TpiDKbT2K_gNMqNp255BdwjJDTpHplOuLkt7geCsGBs81Jx5rGIpxc_3NYYbyEWIpDV3uhCk6BM0xw_Ug5j9l_RX0_DyRTRpIfL-jax-M3z-BWMbnMA9GjsTj35Z8i83dZACXRidcNYdFIaWlxiU-BJtFRDqf-XsBLkT71HH1IipaaQun8dUdREfkwkwe6TGSVJSJkMljjVpKva_WASMkj8YTT-batSLsdHmlF2NINQ7q0zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ساختمون همون جایی است که خامنه‌ای حامیانش رو جمع می‌کرد براشون می گفت :« کشتن بد است، اما فتنه بدتر است.» (پس معترضین رو راحت بکشید)
و اونها هم براش «حیدر حیدر کنان» می‌خوندن : لب تر کند امروز سحر قدس شریفیم!
ولی داستان یه جور دیگه شد</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5934" target="_blank">📅 16:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5933">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=Zwv2HJIpD4bLnOyueEx2TITQ3Ko0aILuE1C5JYlEbxQ6JpbU5iwkuoeRKcEJejoyoyj4dy8XMyete3pB5BWgVIOhtSHn8N3RDN7RruZmBIP0cStv5fA_uBeiCQslDtOQBTXtF_nvC1ori9KkAZKkXGG5sG4Nj6HiYbb6fPT3L6FOGjXGjYUV-lR6ccBFAVIphHzpvEoihvw8CTWYMmoXjR53_UjnOXfwCrISLVb6EEaw6uXOampdpz4R43cbuAmOBqT0o_3PR_AEL_Pmor3atYo6xeJfNuItdx3c6FBMBR0QWzCLcjWAYaMrZuzY5NIAJoJNHtspw2kTfk9lyGOH2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=Zwv2HJIpD4bLnOyueEx2TITQ3Ko0aILuE1C5JYlEbxQ6JpbU5iwkuoeRKcEJejoyoyj4dy8XMyete3pB5BWgVIOhtSHn8N3RDN7RruZmBIP0cStv5fA_uBeiCQslDtOQBTXtF_nvC1ori9KkAZKkXGG5sG4Nj6HiYbb6fPT3L6FOGjXGjYUV-lR6ccBFAVIphHzpvEoihvw8CTWYMmoXjR53_UjnOXfwCrISLVb6EEaw6uXOampdpz4R43cbuAmOBqT0o_3PR_AEL_Pmor3atYo6xeJfNuItdx3c6FBMBR0QWzCLcjWAYaMrZuzY5NIAJoJNHtspw2kTfk9lyGOH2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ : احتمالا امشب هم اونها رو به سختی بزنیم. فقط دارم یه هشدار کوچک بهشون میدم.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5933" target="_blank">📅 16:40 · 17 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5931" target="_blank">📅 16:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5930">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rG06I4JuOePTqnsxlTC7anApFLKNDiM1io-O_m6TivFeNWAcTwpAqwlSROxBgToZwxzibPBKR0flxG1IGY7gFUv8w4GbEF10d_q3pHvSV7ESSYHIsvhQNgRKFhWmjlHChsEG7CN85dB8nRIURPZ08_jBWCgnrakt2f-FY0u4ltOivYcvrd53qhrD_9lzYMKgn0lKZHeXT-eOyion_AJkwDb2J1hzvkJwTvE_Jm6ArIC2M65T9E2RScTlgGpfeq0T-ndWom1eDjCc8A8R-BwwXw7u7Ism_AOCgHnXJo7G8PRG6c6wa_jEvgDXF81kgityIxdhSiK022U-7GYHtdvJ5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LCoQRBRcZE8piVXbz8PX7G8kkhRSU_8tFQ0_TA7o0e4VqV8ZqS9yqMzY_zDFq_VXdGYknaQOgzOgdWGEpIQoTNOK1aiQU7zfrwJPnKfW8Nx6GRh3_gHuHa7K9UJxdVBPP-pCa22RMv68vnfTIfXXgkHAhTTFzgmcjZF6Jg8Gym4dEnIFYAoS8jWcXZ-wmX6IyJ6wMPKpRZULEjC3wohbzMw3LaPgmmQrHPaNV5biPhel0VVx1u4nvMbE-lwD5ZW4E9EKGZz4i51Dt72BJrk8YGdhTZoRs7SXI2CXq9Fu2VepwXMWdjm1tznRSUnOhTlR1chEMN15KM_mIfE8ALUrNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوش دولت چپگراش رو چنان بکش
که درس عبرتی بشه برای بقیه اروپا!
برو جلو! دعای خیر ما پشت سرته!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5928" target="_blank">📅 13:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5927">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">محمد اکبرزاده، ‏ معاون سیاسی نیروی دریایی سپاه، ‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.   او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.   جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5927" target="_blank">📅 11:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5926">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
دبیرکل ناتو : حملات آمریکا به جمهوری اسلامی کاملا ضروری بود.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5926" target="_blank">📅 11:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5925">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Io3u9-2ZXda32B9O80jN7ZDTitvHTD1zo6l3NYeIp1a5xkYn6W7ZAUX5vgHDFnUbMV8DGZxBsBLqxbFLGSDJE_zam36bcvp_yv8jQpJAvR_B7yeyoA139YI_xFBVVdgKekdqSDCxkDEaLCAWIwUUB_ySEYgQ448Q2UFVjELZfhUjF8hPUZxERRxGHTfbvSGL9n1jBBL5_dqKR0GHBOl0MMZQ7wZJZ4-Kzkuy9hehNdHC3JXa7dhN0cqCCgIP8YZmheIf5ESnKQbJRQ5E8MrKD2WaR1W1QnOiDaQF8E_YCvIHt09x7j1qOu1H4RUjU5v1mHGGy7DozmPV6tqbEZtK5A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/aada56b9e2.mp4?token=afMBgbw_NuJk7giy7Xo95BzsvI1SMN_6KkpPJO8wfWDsZWesQtNFncYB2JLEz0EvH9Tl0HHjMYz1x32mZNQB4PiXubU2N4Uo3_9OVr7bDJ54oSngMbt0-B6InCPr-RJJ0-7JTYjDFT7DiTQQFv0yKP7NJhKJZB-Yc2f8QU0Qrns3XUYvQaQV0Yb3QRyYMWj26a7gkaLqTpwxLHyacnGMTKoqaRV_VABzzSlvkd0kV0qeZI3oOU1q514cpnDTuQD5IPDyXj1TrmiAm53loOzaS-hSNwzzyPmvgOQZ5af0gs6rwG5Qkw_got7VchLkG9DZuJDnR8V-AwAsuZbal3e6FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aada56b9e2.mp4?token=afMBgbw_NuJk7giy7Xo95BzsvI1SMN_6KkpPJO8wfWDsZWesQtNFncYB2JLEz0EvH9Tl0HHjMYz1x32mZNQB4PiXubU2N4Uo3_9OVr7bDJ54oSngMbt0-B6InCPr-RJJ0-7JTYjDFT7DiTQQFv0yKP7NJhKJZB-Yc2f8QU0Qrns3XUYvQaQV0Yb3QRyYMWj26a7gkaLqTpwxLHyacnGMTKoqaRV_VABzzSlvkd0kV0qeZI3oOU1q514cpnDTuQD5IPDyXj1TrmiAm53loOzaS-hSNwzzyPmvgOQZ5af0gs6rwG5Qkw_got7VchLkG9DZuJDnR8V-AwAsuZbal3e6FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بندرعباس - امش</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5922" target="_blank">📅 04:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5921">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tu3dYzFTp4G4CjW5DnamdN8HE_ICgKnLPfUQxMqjqQfdyDDY5Gf1-2sLbAgyutv93JTxEKZABEbpdnEX5lCnDjHt1V2OskDVSiu_uH3bfUJpVLHYrEjzPYqY6y4G1rF7tVy3YFYoullrELP2ViLYQ6Z3NqLa8JybK1PjI5UAXFBFI5dHEBADW_s4LkrPbI1xbZYMYnQT95yq60v7H3neNl-0HTZe04ws0EFION-UbNBXkagKXWKTNizhbL82Mk7yWicigQEQqQAib7u4yP0CdyyTEthY4Tlcz3djUGL987QCZcyE1IH2Y7kIGiLoPtAKBV1-3hkPo6pbt0WUqO2H5g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5919" target="_blank">📅 00:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5918">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f02faf66.mp4?token=O1MgrFBJhSUKJAl9JY6ldE5r-IggFIKHHJJrOEOdEk-C8DkzPDbuHRlKAQPOccMUE_jaFlbj3mL4fUN5uMTG2EtOHsu3NXgnCdM8g9cXhAxWE2uZsLnM3VA9YTWR58AH5Ji8kJNFcrT0L98KQjx7zGQr4GJinjCENLqcRmfK3OU7t13B3JcJswAMjt8NR5n-tWU2B8ulaSkc99mSCMZZXaUNmyPM1uqv9SRabgpEgYni-NI63ARoUUsZpMwurhhc1bGiNCqSR976ROuD1IHX49whQcWGmIOlWWr6JprbN3v0CUf5jV_O7xSGeXeuTV6c3Olw5nhtwtlfnlJgEn6NgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f02faf66.mp4?token=O1MgrFBJhSUKJAl9JY6ldE5r-IggFIKHHJJrOEOdEk-C8DkzPDbuHRlKAQPOccMUE_jaFlbj3mL4fUN5uMTG2EtOHsu3NXgnCdM8g9cXhAxWE2uZsLnM3VA9YTWR58AH5Ji8kJNFcrT0L98KQjx7zGQr4GJinjCENLqcRmfK3OU7t13B3JcJswAMjt8NR5n-tWU2B8ulaSkc99mSCMZZXaUNmyPM1uqv9SRabgpEgYni-NI63ARoUUsZpMwurhhc1bGiNCqSR976ROuD1IHX49whQcWGmIOlWWr6JprbN3v0CUf5jV_O7xSGeXeuTV6c3Olw5nhtwtlfnlJgEn6NgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی این ویدئو دقت کردید یه نفر رو به کامیون جنازه خامنه‌ای وصل کردن؟ :)</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5918" target="_blank">📅 00:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5917">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C93amHYXT6PvmYs2ybS9dDweiY572ZgybcQ_8YJqp_wX16vjM4y7EwQMJVUA2TIaIAwo9gcNAoc9wDIJM7bgc_G5hL166zuFWXqj9OGaHjHdk1MrLsL8BQH0Yp25IGJRf9PwTP08vl6-OxzxcKZVRhtPz771_3dHi19zOnwRxbmt_Hlg7C8dHuYp3hs99i5qF-v9jhBCrJdUoO6vlfjTzkmLdd_vuT9ZE8px9U8kzDsgw5o6BCL0z22BuGDohYx--YWmq3wRDEN96qnMI1Xi8qI3HSNxKyHFA1kH82UKYKGXJBgjs6itB0zHrwBgmgKox8TF0EhCmSfYsKzkZSoY9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو حقیقتا یک سکانس تاریخیه، مدلی که دارند خودروی تابوت خامنه‌ای رو اسکورت میکنن :)  دارند جنازه خامنه‌ای رو‌ از جلوی خونه‌اش رد می‌کنن، از همین هم‌ پیروزی ساخته و‌ میگه چقدر قشنگه آقا خودش اومده به دیدن.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5917" target="_blank">📅 00:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5916">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_WgnlBMpzvWDMMS9OQuoz_Fsod9N27j82Qj_NjxV8gCK4PshxSYIzEfVQP62uNEN89qj63QzPvvVl0Pqpwq3ZPUnKCEV70YAUkbrVajOQJTBR2F14LWoCmN9l3Lut0_sL4lTfmzIh4Di3y3JM_SeYVe9S15q9MJdwabO56Ucive14G6pYE7SQqAtrgFf2cSlBMD1vwu_Uwd2JjRsHjc9mJUSo4LSWLWYVgY0YRbvRQhu3HIySHh1kXV5PeRUe6ffn33Sg_0HuLk9WcJ_sr-m0sEsEvR5D-lC_WmEmbfkmgZuYRTDtNwMAUDnj-7Kpy5K3IjWemiXr02PSj_YQQuOw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/5e58e9ca73.mp4?token=v2d3TOX51LIwzmowDs2_BG4fqeOrAryeLbnpPUROZYP2EaeRXDUcjGcW3RfNPMpDmHWgQxfMgSjrk8qkO3b_f69eZ-gk4n-AiGI2KdKhddTlkFsqNAkzae3N6Uk5q3C1xSU0JQRiR-mPocMrrQf4rDeY4GzTgx9fonDEXg-ChDb0uC9Ayx03pNGnoQGNTadp4WbPOD1GFxG-etU4womJIcqsRxHw2JV4CDZ3_89QDZOkO0HT0TY5p4VhtkoAok9D0bceR0IVtudDTfk5_SO91hDYkoj3qm-uDo1EDgXuXxmTt3kdCGqd3MaDX09Y4Mn0qFEHAb0_F1JubiGHeFi_Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e58e9ca73.mp4?token=v2d3TOX51LIwzmowDs2_BG4fqeOrAryeLbnpPUROZYP2EaeRXDUcjGcW3RfNPMpDmHWgQxfMgSjrk8qkO3b_f69eZ-gk4n-AiGI2KdKhddTlkFsqNAkzae3N6Uk5q3C1xSU0JQRiR-mPocMrrQf4rDeY4GzTgx9fonDEXg-ChDb0uC9Ayx03pNGnoQGNTadp4WbPOD1GFxG-etU4womJIcqsRxHw2JV4CDZ3_89QDZOkO0HT0TY5p4VhtkoAok9D0bceR0IVtudDTfk5_SO91hDYkoj3qm-uDo1EDgXuXxmTt3kdCGqd3MaDX09Y4Mn0qFEHAb0_F1JubiGHeFi_Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نحوه حمل جنازه خامنه‌ای</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5915" target="_blank">📅 23:26 · 16 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tgog21wp7vImJlU01OwQlapCpmG3375D9sZCvCxzApbnls02IfO3ZIH2SRWkhhE7V0xmFR_YEbf3UP4i-RmovOZkwTDVw-TbpPSiYyKpSihsFGLEz-uGTuTplAAqb6U_puCPcXjPsD956Bd-6pS2KKmVQGoGTLi9HITFN3m2EziQq7v9hgyLS8QbWMzmaIaqyZ3HtjRyhg-Gne1RkLF_XrBhVnsMD1wOsQg1Fpgm1yqgVzRyHCPS5xlM8AYVLgE0dANiqoirGaMw138tMAkgGfksarXQF-Qa6Yo5FiHrVS774F0GRUEDeTOFibRyZBGcS0VohYNHbGLM_RMuQFkN2g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QT7kwKK1tjrTMnLLIu5JU5sTtRbGcGC3WOYrr8TAj-mqPebvzWtKHrNjcGxYxcupevfPsaX7NaCFjINKK6klU3duyCJ1IdzfH7KGeQxCWgmU_VZvVDxkC35jUyFWuPQLER0Iqp9kxme502rqlkHePFO5j5yfRd2-g0TcHhZUu_M7BY2tDNfqUEqfVpMykZPAschYd-QKo6ReGJZJ7pjTbcXvni_2scc_R1mlEZXyXDWFed3Q0rfp-OSVI_i20xqLH2jZSc5sbysdJtVxNpAubq2wyGXlNaxrkHS2PMB1CNsqMaoUJAhf1EcWBdHhxIfZ_zWqReoYGnOyIDCYOPNmdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آمریکا مجوز فروش نفت ایران را لغو کرد!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5911" target="_blank">📅 22:44 · 16 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
