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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-20 01:02:14</div>
<hr>

<div class="tg-post" id="msg-6021">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">دولت ترامپ از ایران خواسته است که روز شنبه با انتشار یک بیانیه عمومی اعلام کند که
تنگه هرمز برای عبور و مرور باز است
و همچنین متعهد شود که
دیگر به سوی کشتی‌های تجاری شلیک نخواهد کرد
.
این خبر را مقام‌های آمریکایی در جریان نشست توجیهی روز جمعه با خبرنگاران اعلام کردند.</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/farahmand_alipour/6021" target="_blank">📅 00:36 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6020">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b03c66dc8.mp4?token=HXuHCAa6L1Kr76JfHGiOfz0dd9cSOebiy8J7TB_81UlCp7Alo6zbul_0mQioZsRVKuwv6VwxE0jLo2Y11E9t9DwAF1PE9EGnJXN5oUJXdLoJlT2-5DHVXRUf7yfsWbCbL5Ix5jYm4sHqthZkQdWfTeYuprh06IQz9iCv52Z1AmAzPb_oMS773GoNzzyK-FoWmcSWXtb43AM8D-HXySDFG8r6lCMRhBieb-hA2jVb_gxgqx7uc-rvn7LoBtMdji1bNpZNWmV94o_r9ZSFuiD6xOLvrLE2eii2pd2NmHQdeSzE2PHr6_gUJ5KNraofyBdhRgEhIYsVdBMK8kwNoKSPAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b03c66dc8.mp4?token=HXuHCAa6L1Kr76JfHGiOfz0dd9cSOebiy8J7TB_81UlCp7Alo6zbul_0mQioZsRVKuwv6VwxE0jLo2Y11E9t9DwAF1PE9EGnJXN5oUJXdLoJlT2-5DHVXRUf7yfsWbCbL5Ix5jYm4sHqthZkQdWfTeYuprh06IQz9iCv52Z1AmAzPb_oMS773GoNzzyK-FoWmcSWXtb43AM8D-HXySDFG8r6lCMRhBieb-hA2jVb_gxgqx7uc-rvn7LoBtMdji1bNpZNWmV94o_r9ZSFuiD6xOLvrLE2eii2pd2NmHQdeSzE2PHr6_gUJ5KNraofyBdhRgEhIYsVdBMK8kwNoKSPAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی‌ خمینی، از اعضای تندروی خانواده خمینی:  مذاکره به قصد صلح با آمریکا خیانت است.  هر کس پیام دوستی برای آمریکا بفرستد دهانش نجس است.</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/farahmand_alipour/6020" target="_blank">📅 23:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6019">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">علی‌ خمینی، از اعضای تندروی خانواده خمینی:
مذاکره به قصد صلح با آمریکا خیانت است.  هر کس پیام دوستی برای آمریکا بفرستد دهانش نجس است.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farahmand_alipour/6019" target="_blank">📅 23:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6018">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lbIJyOE2Zg99a7z3TD5mDWj0vjc1vH4vH6eeDCZB033bHtcto7zbvY8OM41MekdSJL9DlcS9mLECr4XoRiKdft09qQFx0vnI8Uf4DSB9UJ5SLtKNYr4kzEbFsDroDdylLGJ1uLB_MRRgKpUuLhaWn329PoFDM2Mf7VIe_Vfs2tbR3FlpSShbyJ6hYHVPN45B959Ufyq7LeVRhGgU4i9RBjDSuvUrTRx3kAfK39tQMR-B3y8NO69Z17tPQoOft3RC91injyqPAcnU69MuP_c5i290F9K3QcyL0s-jszxBquiXLylYWfTy2J4tucAQBOGLSqhVQS5QAUus7_jHfnFPmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علویه، خواهر بزرگش (ناتنی)  در سال ۱۳۹۳ در سن ۸۹ سالگی درگذشت.  ۳ سال قبلش، در ۱۳۹۰  علم‌الهدای معروف مشهد در یک سخنرانی گفت که زن حاج شیخ عباسعلی
😅
می‌دونید که علم الهدی اسم زنان رو نمیبره حتی اسم زنش رو روی قبرش هم ننوشت! (ببینید حاکمان ما کیا هستن!)  خلاصه…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/6018" target="_blank">📅 20:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6017">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CBCdTL9seDcNwGsIb89YYMmUWZ75YhupG5WpItG-REVUvZfiD6KHiROnXkLn4fzdNEvQCBsplLIerYuH0UMUBEtMsezM3MC7ZKK7Py0YFkm2H0O6mZei_Fnzbygt7tAnrp_QgM6h59w8uxsGJIyNVQN0aLBYMYZwuWWVtE_nnIqjCdwrYgb8nyJ4K2r6_6FmvF1cFmuGuqTGjxgGNBAjAkenwQxu9CHL-SNdywTVANS_otcnr7RB-hd3qv4e8yGeMKp9oah80UsGtFRxbWjhdqYY3e5LcKoObVpckCAzAsFgLiWr1fFP9YOF9Blgz6KLpZDuv4UTBUShsOAstb-pww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواد، پدر علی خامنه‌ای،  پیش از ازدواج با خدیجه (مادر علی خامنه‌ای)  یک ازدواج دیگه هم داشت و سه تا دختر داشت.  از خدیجه (مادر علی خامنه‌ای) هم ۴ پسر و یک دختر داشت. جمعا ۸ بچه بودند.  اون خانمی که ظاهرا خاطره ای گفت که «علی خامنه‌ای وقت به دنیا اومدن گفت…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/6017" target="_blank">📅 20:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6016">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">پدر خامنه‌ای، در کنار زن و بچه‌‌هاش غذا نمیخورد!  خامنه‌ای می‌نویسه که پدرشون در یک‌ اتاق مجزا شام میخورد،  مادرش برای پدر آبگوشت درست می‌کرد و اون رو توی اتاقش می‌برد اما مادر و فرزندان معمولا نان و ماست، یا نان و خرما میخوردن.   «ما بچه‌ها در اتاق دیگر لحظه‌شماری…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/6016" target="_blank">📅 20:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6015">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gB_jklWp-P3SyRXbm4_EDnMya7QubfMI49g1j4w_VhiPn-iZO2Evl0qL-0_yfAfFGW06qtFJ0UHnNf8VNKezps_esDctb0ISCH2P6bquT2fhd2L-LWktS049d0km2_qfc_tzlCR9l4PnCDawud2NIK3WyD1SKzbAZDNNSsI9Ag2I4XDPwulWsAhcmD5ckwtPta7cd4Q_2LgsjjzJuSBgaE4NfL6ji8a_T2wKx0RQoUsLXHxU_QD0i-XsiaHSvD88FEIKUiIeua4WC6dHLfzg3ljE_VPOoMVDG_dxu9S4sK-nc3_VHIwtLtU2D0qQOoBR2AhqMam6Ajzxy-v-rz5Knw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای و مادرش - تابستان ۶۰   علی خامنه‌ای از سوی دیگر، هر از گاه مجبور  به کتک کاری با همسالانش می شد که او را مسخره می‌کردند و نامش را «آشیخ خُردو» -به معنی شیخ کوچولو- گذاشته بودند.  در این تمسخر هم پدر نقش داشت که کودک خردسال را مجبور می‌کرد تا …</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6015" target="_blank">📅 20:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6014">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tFLFj6blG066qOc9Vz59KMvvnEt9kXhpJ-qtpAmFfW5ICohqG4FNQbWoELS85GqFKPesMMQ0oIfeZTJVY-UBuixdjzb57WF9FRUwO7fSY_zE_YSTtvWkrwiIUm2vO2p_7aXcYiUh9MxrcFc9j22DyifsmU4IGvvMZCwovXGmVQUWCILGwMwwid2CfDJ8gyH-a898QpObWojN6z8_9nSXZslXvmd3cLOi3Mv1Tyvs1VE5qQFTsUJnUtIgorLz8krnFxK_6LS-3AeLXwgACCRvbgX0dymYpAbeS0kksqNXta6BKMCcSOREawZwACz_9ToLVmNrpjPs21FyGGKWgGaYDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای در کنار برادر بزرگ‌ترش محمد خامنه‌ای  علی خامنه‌ای در خاطراتش ار جمله روایت میکند که  او و برادرش محمد،  در هنگام درس پس دادن به پدرشان  (جواد خامنه‌ای)  که «دست‌ سنگینی» داشت، مرتب کتک می‌خوردند.  علی خامنه‌ای نه تنها برای اشتباهات خود،  که به…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/6014" target="_blank">📅 20:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6013">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DW3Y8wkErEwjwhOu146AJeeXna-1_Q0yQHyVoQUogvuEw84IQQWdhgrcwU80wv9tXG-1-1jTExHEOTwqgh0A15l5iYi9CWoppsIWSS_H_9MqlPO-ExhLP2LqfKuW7q3xDK4o2mdX_UoqYv7uPLz_u6ilcSEtzGMwSEIrDajTgLwW-XHDpJZvpULYX9Nmzv8qJtpy9PZuvcubBZXBTiJ92E6mS6ggwrjB_PG7OV5UKWrXZQCzHSFlIUOOE6JmN3GhWMWGj7vpEg5yt4XNt_lIBZmLVrNJDyAXQONcTbZ5wKvksbzWFVuWgRJTiWIsxnT8K7PmpZw3v0Ako2lvBbMjoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر خامنه‌ای - قبل از انقلاب   پدر خامنه‌ای فردی بسیار سخت‌گیر بود! جزو آخوندهایی بود که مخالف «برق» بود! و اجازه سیم کشی و‌برق کشی به خونه رو‌ نداد! اینه که در خاطرات خامنه‌ای اومده که از چراغ موشی استفاده می‌کردن ‌و مادرش معترض بوده که وضعشون از بقیه…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/6013" target="_blank">📅 19:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6012">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ftoT0vHGzBnDY_XOgrbM999A50vu0U3HCEN_VD19MRDlKDrZhadB94T8TrzcNVRt85obQoUoJlZuJK3fO9oEmw4y29FrXCXwTbD_uGmPLdIeQCkoycDhgOUajra1PbFAt9VMcv8n_IHQ3SHNWnGxGXjVLHBUO55RjZzf5ftn_evCkOxFDKjzuTt0TUvZjEPYx3OWH9NLgMRb4TmkwxQfeP7eyvtHE6V5ul4OKgv-3bLHn9tJpWBBpZHnTHEQ2wJppZGzm0FF5ydGr_3tDiyBeExW8qgAtWyFe2c8Um8pWnXv316Y1cQGaND5plapVjmBIXdW2g2xBfNyjqXDsYpiwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر خامنه‌ای - قبل از انقلاب
پدر خامنه‌ای فردی بسیار سخت‌گیر بود!
جزو آخوندهایی بود که مخالف «برق» بود!
و اجازه سیم کشی و‌برق کشی به خونه
رو‌ نداد! اینه که در خاطرات خامنه‌ای اومده که از چراغ موشی استفاده می‌کردن ‌و مادرش معترض بوده که وضعشون از بقیه آخوندهای مشهد هم بدتره!</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/6012" target="_blank">📅 19:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6011">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">اینکه خامنه‌ای گفته :« ما از زمان کودکی با پدیده مسخره کردن عمامه مواجه بودیم،  آنقدر کلمات تمسخر‌آمیز شنیدیم که این پدیده در نظر ما عادی شد.»   خمینی هم در سال ۱۳۵۸ در جمع روحانیون کُرد، دو تا خاطره تعریف کرد که روی وبسایتش هست. لینکش هم اینجاست .</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farahmand_alipour/6011" target="_blank">📅 19:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6010">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JBuHBmINNg4wiMez3F-XCUwCh4n-_2LP_GWmwRlvnv3TFyB8RtDkVdxb-Zy4nGNuP-wdA10DlFbZHZ3V7DqWPXgM6jJi_nBBZnfe_VWYMtMZVTwM3Gkw2PHhpNwx5Q94VeSu6SgJCCxIPXPNGYI1f0EMhCXR44ZpGDsZeziddZoIIatPBWIGUFywliuc8Ua_-t0R8rx1NXDW570NgtDN5LEjSln8aVO5c1ZPYPUopYboMTfzkUbascvXkreIKjppVfb7XzKleq3GoqDFwbxxxuEigMvroiMAWjN6zjiNAYNdzrFWaDGyALxHEazfkLoMoyO8bvmEuGzgrWQgGpGQCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای بارها و بارها در خاطراتش  اشاره کرده که چقدر از اینکه لباس آخوندی می‌پوشیده و مردم در زمان شاه  آخوندها رو مسخره و تحقیر میکردن در عذاب بوده.  چه در زمان کودکی که بقیه به خاطر  لباس اخوندی که می پوشیده مسخره‌‌‌اش میکردن، چه در جوانی   او در خاطراتش…</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/6010" target="_blank">📅 19:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6009">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NN2fLb4cazVvpoyA91J3Xw1V91yDEY7pxYNgyUboOI9fXj91j597ISmxfcEJt_qEUY4Eh2hbwuM_F02Ox3-MqLHnZHt0fMpcP6qVafcVjRFKeAdOP41tExPMPlOR_FAbVXY6TkExty-hZSS58DfVrNyIx-ONpPI0hSn5r5zYv28Xqw3YcMw0ZcKS1d4VuQfoVSoZ-MFA1AI3sWnUVmzgndyX7JEmOz13aMv_PBYicl5pkYcshx58ot7S6HWN2qSBKY87Dy_t2yYzlrpoelwlEQCVAEx7zjN-2n3Ty1JYd8r0GIG1hRHOgavx1i1nkVK_UoB7ksQccoiVrr0GUQT5Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای بارها و بارها در خاطراتش
اشاره کرده که چقدر از اینکه لباس آخوندی می‌پوشیده و مردم در زمان شاه
آخوندها رو مسخره و تحقیر میکردن
در عذاب بوده.  چه در زمان کودکی که بقیه به خاطر
لباس اخوندی که می پوشیده مسخره‌‌‌اش میکردن، چه در جوانی
او در خاطراتش می‌نویسد : «یک روحیه عمومی ایجاد شده بود که و را مورد تحقیر و استهزا قرار میداد...
ما از زمان کودکی با پدیده مسخره کردن عمامه مواجه بودیم، آن قدر کلمات تمسخرآمیز شنیدیم که این پدیده در نظر ما عادی شده بود
... هیچ معممی چه کوچک و چه بزرگ از این پدیده در امان نمانده بود.»</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/6009" target="_blank">📅 19:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6006">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6006" target="_blank">📅 19:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6005">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=mDQjlTRqRN0zJeGqSL6LOwovQK7wW_eITT_cqHnlvI_cYaSgjM8iqFfZiCpHrMO0Au1zF2154iIZrnn06Hu05hQgJzHweYyyMausGGrREkheIVMemnuQ97ARaPUlE1wTfY0Sk-RFUINlz-su7NvVOvki1w3MSPN2KD8INpPBYTckOVUsNEVh7oN2UGIXgdfD_w7_6RbAXLFs8Qhc4cKc--EOrLS5vZMje4ARQxlGsZi-IAvQdYjK6mqRqWyGFm3UNv3Bcg0mdutireIPzcj1Us-N9oaKlFd3CoONXfOioQFiiCNeYvg5LblW4ZectUeZDAAYMFI-8o58J7T8vit3Q4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=mDQjlTRqRN0zJeGqSL6LOwovQK7wW_eITT_cqHnlvI_cYaSgjM8iqFfZiCpHrMO0Au1zF2154iIZrnn06Hu05hQgJzHweYyyMausGGrREkheIVMemnuQ97ARaPUlE1wTfY0Sk-RFUINlz-su7NvVOvki1w3MSPN2KD8INpPBYTckOVUsNEVh7oN2UGIXgdfD_w7_6RbAXLFs8Qhc4cKc--EOrLS5vZMje4ARQxlGsZi-IAvQdYjK6mqRqWyGFm3UNv3Bcg0mdutireIPzcj1Us-N9oaKlFd3CoONXfOioQFiiCNeYvg5LblW4ZectUeZDAAYMFI-8o58J7T8vit3Q4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا هم مسابقه طناب کشی برگزار شد</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6005" target="_blank">📅 13:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6004">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اکسیوس به نقل از میانجی‌گران (پاکستان - قطر) : حمله جمهوری اسلامی به کشتی‌ها توسط بخشی از حکومت جمهوری اسلامی طراحی شد که مخالف تفاهم‌نامه با آمریکا بودند.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6004" target="_blank">📅 10:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6002">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/snnzMcz3inFmx6TanG6GRCd7O9p-D-ITlYAnw1PO4pKhyTt9TcHO75KRhdMUBBV3y-9h84lyQeZQ_bQEydzSFmi8B2jDyz3vaIPy-EY8vtx7mkIG6gTtgjxrlkeW6I7OX7JK56UMSD2r88bFsy_EguWzvxYwAVvYh2o0XJDKWlksI-VTqaurAUMFvbWRXI1PVjAWQ4eLDOW75Y9WmMcYtM9y6WD78p5DmtVEiZsMzRn6MJA6HQJ-Kh5qmTwvEErLU96wwVkia6sSK-_hYlFGbOfQwtghUEQFPOoiLt6NjA9vgHY7UBswCXnUmifw0ulJoeXN_rXsy1AXxJSnAI8Gow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f2581pEOawJV4mFu1HSOkfAfRRmx88xCqz9n_xBfcTZIT6BqUIwdK-sU5_zsA1F5lqeIc05FAY1PqR5RdLZN7XeSfaMtSI8rhEpb8eY_iMU9FkEv8Evfws39KOLkyAO926Lqy-jhTG3dssgp1yfEkNPMJl9-WDUG9aVRi59IDnausAglgx1DN9b5xf2Q1-6qZnZSyY5IfUDSES9TKJX-5UUDfQ83HG5dtv-6bcyiEAlnYS2HEFXPmkOYGFYJkyhenBTO-MiHCsav0ZwU1hiwiGeQm9URhdH4NoKYQpMQbUw7V8nzk_YgMxJ1qdtWaj9PeoDrm5c9d8jgdHg0DiCoHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کارشناسان و منابع رسمی شما  که این آمار و اعداد رو درآوردند، احتمالا همون‌هایی هستن که به خامنه‌ای گفتن در سراسر دنیا دارند «سلام فرمانده» رو میخونن و خودش اومد اینو گفت!  همونجایی هستن  که بهش گفته بودن  نفت آمریکا در ۲۰۲۱ تموم میشه امروزه   در ۲۰۲۶ آمریکا…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6002" target="_blank">📅 09:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6000">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6000" target="_blank">📅 09:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5999">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=qKuTfaYk5kX3pTKxI8VAA2VouOmw55mnpsNSda0nEw-KC7gQpCkt9rj3cNvJbUDno_ymPfEtyf8BvL8XQMbX7nnWn3EoNavZbpCEVmWO5d8LMdf4SaHYFWimSQM6aJ3fO7MQYOxVvAuOzY2OnvkBpPW0nkwrmw_VT1qIvJ_0_UwSkB4ld_2cIo-4D0iFo6bvNf9eyVxguwZSQPnVxRwKraiFFcZOXTYk8Rlz38Bbq1F1HqrHHIigqT3KnnbhiKLjSIXOeYatf9tZKbioMhnaxCdXkbXCO5yUrxxjtfctaaO9c5T53Er3V7XMhBVu1vnrci9klhoRGNybHaNQzad_bxf_M3bkOuM-jE11yUAJ9-qmIvMnttSXlbFghOOwfKvAINnNVpeAr-0_M-fmgS_eBAJfeim2R0P5SXTE6_gH-HuRs1v7EOwDLZa9fzbOZoFuS-Q8-EUwlFPQT9VXY5lQRPjAOaeo0o4zeDMvhtbv4Pg9mgx3slPFHZ1zTJWOq82z5J7PtC6WHRaPryeOGha4pB_49SUklw18muLievnm9GQiHKHjNkS6nJ47GwLsf7My9CaYeusmscjKUMkqzsQD4aMGcsTQm6TuNnc02WQfxx_TuUpWeWFWuwbGuswUvrhWB3-vn30NuVc2qjYtzuSd9kOysyWnbM_96Uqvrp1i5eY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=qKuTfaYk5kX3pTKxI8VAA2VouOmw55mnpsNSda0nEw-KC7gQpCkt9rj3cNvJbUDno_ymPfEtyf8BvL8XQMbX7nnWn3EoNavZbpCEVmWO5d8LMdf4SaHYFWimSQM6aJ3fO7MQYOxVvAuOzY2OnvkBpPW0nkwrmw_VT1qIvJ_0_UwSkB4ld_2cIo-4D0iFo6bvNf9eyVxguwZSQPnVxRwKraiFFcZOXTYk8Rlz38Bbq1F1HqrHHIigqT3KnnbhiKLjSIXOeYatf9tZKbioMhnaxCdXkbXCO5yUrxxjtfctaaO9c5T53Er3V7XMhBVu1vnrci9klhoRGNybHaNQzad_bxf_M3bkOuM-jE11yUAJ9-qmIvMnttSXlbFghOOwfKvAINnNVpeAr-0_M-fmgS_eBAJfeim2R0P5SXTE6_gH-HuRs1v7EOwDLZa9fzbOZoFuS-Q8-EUwlFPQT9VXY5lQRPjAOaeo0o4zeDMvhtbv4Pg9mgx3slPFHZ1zTJWOq82z5J7PtC6WHRaPryeOGha4pB_49SUklw18muLievnm9GQiHKHjNkS6nJ47GwLsf7My9CaYeusmscjKUMkqzsQD4aMGcsTQm6TuNnc02WQfxx_TuUpWeWFWuwbGuswUvrhWB3-vn30NuVc2qjYtzuSd9kOysyWnbM_96Uqvrp1i5eY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرگ بر دیکتاتور یک شعار نبود
آرزوی یک ایران بود، برای سالیان طولانی !</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5999" target="_blank">📅 09:19 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5998">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">مداحان اختصاصی خامنه‌ای،
که توی هواپیمای اختصاصی که تابوت خامنه‌ای بود، از عراق بردنشون مشهد.
نقش «مداح» چیه؟ مدح قدرت رو بگه
و بگه شما بزنید توی سرتون!
اگه یه عده از شما نپذیره بزنه توی سر خودش
هم حکومت میزنه توی سرش و سرکوبش میکنه.
اینه وضع جمهوری تباه اسلامی</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5998" target="_blank">📅 09:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5997">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7rmLsYn9b-2eD6lbL_as5vpKZiNTcRsB_SwJNeHwh8llBCHA_1_7euiTkgWBn2O5PGx0HC704miFpvzVmQCPhEnJj4aMrm4gvL-4FS-vRziWU5oHBPOihSfHXxaje_am6kN4VcGqYfHt6loKYQ7MSBqjHidBLEWYKXCViXqxCM99HhB0z3yJcIKpES6vSePKe8whvjdmSwIclrH7-dari1I0uayHu0YbLFqbBoHH3ESU26GCrHVWBWLeV2HAxIlATsLIgbL6i69E3Mp1yYmfTx0RCGg8_wwhGAG-ia44_-IFCi3g9jSWH1x_B6rlMFFm_mfBpOZwBsGZrqCFyY4MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سی‌ان‌ان : اسرائیل اطلاعاتی در اختیار
آمریکا قرار داده که نشون میده
جمهوری اسلامی طرحی برای ترور
ترامپ در دست داشته.
(این چند روزه در مراسم هم پلاکاردهای
بزرگی به انگلیسی در دست داشتن و خواستار این‌ کار شده بود، مجریان تلویزیون، مداحان و روزنامه کیهان هم همگی صراحتا خواستار این کار شده بودند.
ترامپ نیز در ترکیه، زمانی که از تفاهم نامه خارج شد، حداقل ۳ بار گفت در لیست هدف ج‌ا قرار دارد.)</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5997" target="_blank">📅 09:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5996">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های حکومتی از حمله مسلحانه به بسیجی‌ها در مشهد خبر می‌دهند</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5996" target="_blank">📅 01:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5995">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">فرانسه ۲ مراکش ۰
دقیقه ۶۵ بازی
تیم فرانسه در ۵ دقیقه دو گل زد</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5995" target="_blank">📅 01:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5994">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NxBT1INx4ZbLKu3CJTP-CTWPRIcAVE3URHcODUj9Ofko1qS8ge7NGkXrFuhRQ4lkB7VJtmQQpmV-9X4tR1XNdYwEWh8ybmIULLzUyDI25d2LxK22YuKkvEVeOvmzNDIqsqwasa11WkstP_KYYQvTh5w5Taj_IvJ_O_58eur6Se7HSkh5v5ubyI7503W5Jf-v6MqPN7T4rQST_XfqndObH7LVQmqCvk6QlLaZC436jFdtXTY6WhBmmpH9lV7TvwlnOJlLjz3scPrPBJ9ftUct31DaBM-4CLiy7-pS8IlriawKk8V3LawwS8jnshYQrgH8U3X_W2upFowD_E7GvIhR-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام - فرماندهی مرکزی ایالات متحده:
‏
🚫
ادعا: رسانه‌های حکومتی ایران ادعا می‌کنند که عبور و مرور از تنگه هرمز فقط از طریق مسیرهای تعیین‌شده توسط  ایران مجاز است.
‏
✅
حقیقت: ایران تنگه هرمز را کنترل نمی‌کند. از اوایل ماه مه، نیروهای آمریکایی به تسهیل عبور موفقیت‌آمیز بیش از ۸۰۰ کشتی تجاری و ۳۸۰ میلیون بشکه نفت خام از طریق این کریدور حیاتی تجارت بین‌المللی کمک کرده‌اند.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5994" target="_blank">📅 00:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5993">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PyCk-TKvyN0SkrDj4SEo-YD4Uy8lp3rkZIHJRwMdsFrmW8Y4XnkRnE357R6Cp2z3dNTFVF2NlxTRt4oES9nHBvWCU4a8KsmR6XcFxY4BCI2s9hS--O36JPUdL5jf7f2GBt9aRIL9ByZAeImeSFMgGh19hbZ9HWToauAF_AhIxOSqF56bAZH6b1_UmrUJRSrZ7KBxHlbx5h-f_fqIxazQihra6HBm0qmP1aTVLOISKU54etTI69LDs1pSpfe6Jh5V7UWuMH6wGkXx0hte6WuA9yA3UxilvtPzv8R1IzYntpLRPV4KfU2qFXHsPDLk22EcmH1wAKBQBK52Nlu823YMgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های حکومتی از حمله مسلحانه به بسیجی‌ها در مشهد خبر می‌دهند</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5993" target="_blank">📅 00:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5992">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">فرماندار کنارک از وقوع دو انفجار در منطقه نظامی نیروی دریایی این شهرستان خبر داد و گفت:
این منطقه شامگاه پنجشنبه در دو مرحله هدف حمله جنگنده‌های دشمن قرار گرفت.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5992" target="_blank">📅 23:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5991">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">صدا و سیما : هیچ انفجاری در شهرهای بندرعباس، قشم، سیریک یا جاسک شنیده نشده است.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5991" target="_blank">📅 23:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5990">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
گزارش‌هایی از یک ترور هدفمند در اهواز.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5990" target="_blank">📅 23:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5989">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=vfOT10qcev6fW2yLBa2IHmpHM3HIQwrYVi4c85LumEoY0I9OgFM_IYBBQn901uujggbrEwsBf6mtm_a8FCNJ3_2notIZKjLXgCD_-QqrqxLpPTCzDlfrMX7rxyGpEWXGG3bYtkHTi7_iKT8ifQgsFT5oPf5XsdKsx8oL2ts4Ll0oTszGHPm_vxqUfyDAkM_HQhv9NakJoPKa-zM-3A_Jdq4CScqdrviz4WV15NQo8ETGhk4SCQQK-8ohoqKGX1C0nUxk37FVNFj5g1NssUwY88nw35Qzw99TBZgQcJsOazwoPdlAjpQ7vjyfTHtNzU7P5Elr28XOGu6WpqG6BCvuwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=vfOT10qcev6fW2yLBa2IHmpHM3HIQwrYVi4c85LumEoY0I9OgFM_IYBBQn901uujggbrEwsBf6mtm_a8FCNJ3_2notIZKjLXgCD_-QqrqxLpPTCzDlfrMX7rxyGpEWXGG3bYtkHTi7_iKT8ifQgsFT5oPf5XsdKsx8oL2ts4Ll0oTszGHPm_vxqUfyDAkM_HQhv9NakJoPKa-zM-3A_Jdq4CScqdrviz4WV15NQo8ETGhk4SCQQK-8ohoqKGX1C0nUxk37FVNFj5g1NssUwY88nw35Qzw99TBZgQcJsOazwoPdlAjpQ7vjyfTHtNzU7P5Elr28XOGu6WpqG6BCvuwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌‌های مجری شبکه سه و تهدید ترامپ</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5989" target="_blank">📅 22:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5988">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/llDfvr5-DEgo0qR5oI6bKHDYeB_QXo3lcwZGiYxh4pS9Asj8C09IerUCXB8MP6LWgF3UoMDWMSYvzYZQrWAtejpvJyykXaSrTr0HFldV28tUnOGjLZ5cAUi_ItUwIFIr8Af00j7EgCPZf5F7Gv9UAJF_gXTbdmCkQVXBD7fH1E6BJ0OujvZcRPHXB2Qu2tM-NFBJaxGCNLd42_BnPrCA-_WfzTPf2ZHUx2p7wiyMXzMoDdNpLSNZGPGXQwwBZuiPTCRcmoKQQB3B3YyX6ukfuLL0n449qWa_S-t8lGI4_l9ew0Cl5KmdpqvYKC1FuU5aw-JX92qXNUGrGUZ1_ZQQyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گمانه‌زنی ‌برخی رسانه‌ها:
حملات امشب احتمالا کار
کویت و یا بحرین است و احتمالا
حملاتی موشکی به ایران صورت گرفته.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5988" target="_blank">📅 22:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5987">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
🚨
آکسیوس و العربیه به نقل از منابع خود می گویند امریکا امشب حمله ای را به خاک ایران انجام نداده است .
ممکن است حملات توسط کشور ثالثی انجام شده باشد یا صدای شلیک موشک های ضد کشتی ایرانی به سمت اهدافی در دریا باشد .
یک مقام آمریکایی هم همین موضوع را به سی‌ان‌ان گفته.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5987" target="_blank">📅 22:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5986">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fffbd82aa6.mp4?token=Ws3y7gxxfyxB23H6MsD98QWzXwHb7-mJjpwcaZznIKs5lg4yQSFYtXnPnog3v61JbQ1OMjUk7TSSgfbKj4bnfrijHpZFMX0LvQd1Rx9O-3St9HlyUPu4MuE_ac4kSiLW-5RGMJitYkC_A2KYCb88IlL99hh-RQFa26SQ1_aW3eIK5KIa931k5MvgG6g69wK8KH2H2W8MtW7M_ZZC-nO2qJzUD0TrXlVNz6HS94x-JLNqFMdgtFQUCThfa2If4-DVpTwkxaPxqfYaOZyrVee7qtD0ksnBw6Z5s3uEpsDkRIaxdNq1zHAAXD_TXulAsGlUHU4gcRjtFgHCVfeI_hFUrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fffbd82aa6.mp4?token=Ws3y7gxxfyxB23H6MsD98QWzXwHb7-mJjpwcaZznIKs5lg4yQSFYtXnPnog3v61JbQ1OMjUk7TSSgfbKj4bnfrijHpZFMX0LvQd1Rx9O-3St9HlyUPu4MuE_ac4kSiLW-5RGMJitYkC_A2KYCb88IlL99hh-RQFa26SQ1_aW3eIK5KIa931k5MvgG6g69wK8KH2H2W8MtW7M_ZZC-nO2qJzUD0TrXlVNz6HS94x-JLNqFMdgtFQUCThfa2If4-DVpTwkxaPxqfYaOZyrVee7qtD0ksnBw6Z5s3uEpsDkRIaxdNq1zHAAXD_TXulAsGlUHU4gcRjtFgHCVfeI_hFUrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا در مشهد هم دعوا شد :)
چند بار زیر این تابوت دعوا شد؟
توی میکروفون به نیروی خودشون میگه خودت رو کنترل کن!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5986" target="_blank">📅 22:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5985">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5985" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5984">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_yiPTVLso4c09iv9mjOXr2kyULLS7hN00-CSmP2qxdcja-A167iTfvBlKv6VRW6_3Ptk0_Wqf-qFwkd-cFAWkydJuP56qLC3TG3huS_arqNXLq-PYVFrt0dfKlxGpIjpk7mZ6Npl6E-IoJWv2UoPl5Gu_cJRo5fUZAhxI0MF6RuO-nXcqqadPgaJCh_4D8yp4jfHfOJ73Cmo-Oa4ffaLlRg-iqxXWHQQLH4UzK7H6R0zjnlhxylo1NwIZunSz2np4SpkIX-hopGfNrOumaSW_nTdIOcMN1Dlnnys-DSvRp9kD1N-X2bhR2mrAD1zLtcj3prfaCIgzYo2nKYZD8FJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آماده سازی قبر خامنه‌ای در مشهد همزمان با حملات آمریکا به جنوب.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5984" target="_blank">📅 21:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5983">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5983" target="_blank">📅 21:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5982">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5982" target="_blank">📅 21:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5981">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">‏پر از خون دو دیده پر از کینه سر…
‏شش‌ماه از کشتار دی‌ماه گذشت.
🖤</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5981" target="_blank">📅 21:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5980">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B6119fj48qvC867X3f8aweLBxx6GmWlwgxIjq28Y74upOMLxIUSy8EUYJD2lElNqU8dz-2ALYpSpcxXNobPCoWlG1O4La7lAZHV1HOXxo8-OlAAW1cxIY4UQXFc1USj_qG2vc2EhVYl57oCi05y488vxYp9_jh0d0cDRB9EqWTKd3JTk26dgdDrTp8n1_xaDUbv-cReB7BP6ZAOqeawnFla1TG7xjpnXMRjpBbvc67y__CmKgZNin9-p3RKdI_cI_0ovbSUz-AObsT8aprp9xjyg4krlLXFUAKiYM2eSlc1fiTvAGQYJAPd_y0jq5v0tVnmUhdHixWB0qgeaRcVwTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2075261040867037280?s=46</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5980" target="_blank">📅 20:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5979">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=t0eEnZglzZmmYVA5lnt3N78Zzq3bMbCUmNkeJBXGWfNb9Quk74wYI04LHdxKxn7add5S2tFFRA_UwClf1sVv-6q81Xihj1-OwIehtOKwLtL2eHxEPRevYArICeQd0z6PS9qK62SUwfnbsK3NPGmqRsTC4U4VNqU9jsATK-XCIcJQ0Yb25LHVte5CZ0Vm8YeH0JAi3vX2RdoEODB4vvElwNV4Wssdtbt07hzOX5l7-hI8x2FdIPAZQtC5Zgqu5WQF-UIx-RtZhKEDMHjPbx_JvvwMEiqw35hvLQ3f8Q3fyoZg-t3_-UDELrl0R2zjs0GozicuKceDaBlI_BC0Gb23tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=t0eEnZglzZmmYVA5lnt3N78Zzq3bMbCUmNkeJBXGWfNb9Quk74wYI04LHdxKxn7add5S2tFFRA_UwClf1sVv-6q81Xihj1-OwIehtOKwLtL2eHxEPRevYArICeQd0z6PS9qK62SUwfnbsK3NPGmqRsTC4U4VNqU9jsATK-XCIcJQ0Yb25LHVte5CZ0Vm8YeH0JAi3vX2RdoEODB4vvElwNV4Wssdtbt07hzOX5l7-hI8x2FdIPAZQtC5Zgqu5WQF-UIx-RtZhKEDMHjPbx_JvvwMEiqw35hvLQ3f8Q3fyoZg-t3_-UDELrl0R2zjs0GozicuKceDaBlI_BC0Gb23tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربها در حال آماده کردن مراکش  برای بازی امشب مقابل فرانسه  امشب چه فرانسه ببره، چه مراکش  مسلمین به خدمت پاریس خواهند رسید :)</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5979" target="_blank">📅 19:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5978">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=fOiRQryPRt_BOJ14D4awPzUNIbeC9hFJ96f4dtpOAcIOZn5h-RS0J84oT__ItwiWpYW3Mb8-bLq9r63Sr2aZceOgxsQzFe9voDLCLNH_eOmWKMXCrjD1xug_PcuoL01jkZ82WLYBoXlVPaMGTPpZZW5p55mfhMO_4WZw6GhD5D1PYn11k5zleVUqH0wl6NdhM8iXUn6Eq_VoceVDjco0GQGiZ2GMX3q5okXn2IZFkJBUCp_kycF9AJFoPCUpMODC7F3ja0jkBbjYccqarAAIt4V4iUMEgkoK79PVlFieKPCFgCgPH424C8OzfrlGpsoOB2WHLyQ9Irw2P9BkqF5gCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=fOiRQryPRt_BOJ14D4awPzUNIbeC9hFJ96f4dtpOAcIOZn5h-RS0J84oT__ItwiWpYW3Mb8-bLq9r63Sr2aZceOgxsQzFe9voDLCLNH_eOmWKMXCrjD1xug_PcuoL01jkZ82WLYBoXlVPaMGTPpZZW5p55mfhMO_4WZw6GhD5D1PYn11k5zleVUqH0wl6NdhM8iXUn6Eq_VoceVDjco0GQGiZ2GMX3q5okXn2IZFkJBUCp_kycF9AJFoPCUpMODC7F3ja0jkBbjYccqarAAIt4V4iUMEgkoK79PVlFieKPCFgCgPH424C8OzfrlGpsoOB2WHLyQ9Irw2P9BkqF5gCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربها در حال آماده کردن مراکش
برای بازی امشب مقابل فرانسه
امشب چه فرانسه ببره، چه مراکش
مسلمین به خدمت پاریس خواهند رسید :)</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5978" target="_blank">📅 19:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5976">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=QrCv_pScEQO54WQRaR8hDtBcB_WuFWzwGCE4PovEPfmYO9zM15txLD4ITdUWHeH_F3LuvITup9ZoV37s0F2ng8C0nE-Cg-wDjAkUnOzqUT_KdwRnzx_8J7PTqXLWJ1SmuI8O5uX5eI8hBObnK72K0zd3Iq6y4Jo77ZaFo7LXHaZWh4CJiJOrU-yGrLwVFIHNmdc-o3UeLmIfLmyYfHPrzM2VvRAYw5KwP6Eetp-gEq7rp99ko_SfkZM8Pk8cepukfLZUQGdkv6Mw55IjNvfk3b0pHIWDlMWmrUe7YMznRG4MK9A1CRmre2us3AFCgtTxbSUwYlM4XU-uZmzd0YnpjUQ3fmyXDPV99sKutYGtzb4eNW7xMZN1dhe4IMw4DhAUQ05pjQnyOTHHxzUwDckXOqW93fwylqN-V3WsEnwlrk_x6z5uuueMXcT389hiTmHUXGvpYEMx3ZxR7-aqnYWb55mNlodkow3Bo9s00BWOlS8aU1s099K7Nbsv6Owo099hE-tVVHQXvG2R6WxnPLhONrbMymZMrrj9BRjHTzUu52VHx5VqebUNl0XDlI_zyzBrjDQjnLuY-UjWwBRtAo9DHZJtjcts2_p0iOvhfU1MzGasyCQ8GsnGBtbzzX-VfsgxYZz9W_XpmiKqiyZt4rMky50_q2AZFizpnyvIwOA-Uzc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=QrCv_pScEQO54WQRaR8hDtBcB_WuFWzwGCE4PovEPfmYO9zM15txLD4ITdUWHeH_F3LuvITup9ZoV37s0F2ng8C0nE-Cg-wDjAkUnOzqUT_KdwRnzx_8J7PTqXLWJ1SmuI8O5uX5eI8hBObnK72K0zd3Iq6y4Jo77ZaFo7LXHaZWh4CJiJOrU-yGrLwVFIHNmdc-o3UeLmIfLmyYfHPrzM2VvRAYw5KwP6Eetp-gEq7rp99ko_SfkZM8Pk8cepukfLZUQGdkv6Mw55IjNvfk3b0pHIWDlMWmrUe7YMznRG4MK9A1CRmre2us3AFCgtTxbSUwYlM4XU-uZmzd0YnpjUQ3fmyXDPV99sKutYGtzb4eNW7xMZN1dhe4IMw4DhAUQ05pjQnyOTHHxzUwDckXOqW93fwylqN-V3WsEnwlrk_x6z5uuueMXcT389hiTmHUXGvpYEMx3ZxR7-aqnYWb55mNlodkow3Bo9s00BWOlS8aU1s099K7Nbsv6Owo099hE-tVVHQXvG2R6WxnPLhONrbMymZMrrj9BRjHTzUu52VHx5VqebUNl0XDlI_zyzBrjDQjnLuY-UjWwBRtAo9DHZJtjcts2_p0iOvhfU1MzGasyCQ8GsnGBtbzzX-VfsgxYZz9W_XpmiKqiyZt4rMky50_q2AZFizpnyvIwOA-Uzc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرچم روی تابوتش رو هم کندن و یکی دوبار هم تابوت رو زیر و رو کردن</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5976" target="_blank">📅 18:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5975">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sQ_by8vh9qKcrtlgU5tlBV8gXCns5LNGzyrOhFKdOMTaDKEdXZ84-46hqehxdFxP_ilvpXxBcnCaM6Ru3h4mVex7W-CSR2TjtSRB3wEn7qNH2f2keIH7a-y8P1WFJ_jTcxa0Xr3YKUw9_c-AUMkc49vTdYZ-LuMUk1SMdg4WgtirMRGhUbkPHE6xOAe0rHupwv23kiaFgmgE2yo4UMZUIHBuZMHCmtCuR5bgeRnWXQvys6vTG0Dd3kXxpJtgt8P5UA2Z1G5V9fF62POxCoj3QgstxegCnVpQ0D7NoV0sThAFLwy-viIA-9lTogTDmM3wtndFogez1kiMkg9HmRN3xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمد وحیدی که الان قدرتمندترین چهره نظامی ج‌ا است.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5975" target="_blank">📅 15:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5974">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/daTfJrjQu7CG86xEmzueHq-n3FUW8koPU0LTZiARY2FceoyCCFurEIULNzVe8RNQQ8WrRNHhlHXhKDpvIHkFFGWQ0H3AeH-tMi9BjN1Qg9cKoJCP_qSP2TR4aGO8EA8talNffdKCgQ6qphhpfpmW_EYGpI2aEVc_IN4a7Y2RiRy89AQyOrbeg72ck8KA3banYUNybfjrMRS92EGo5ZHQXbjDWc31AtJktiBi3TpIhWvN-lQN8rZ7mhLUVpL8-BJ8ZubSlNKN67bif93Ke-Q_-6rfKDawRnSfFhzO1tSBUer76Zqe1xNA1XJpt6JEQ8OtBw5Vb1pQaIVruZ0M1dOfcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب با اینکه حملات متوجه شهرهای جنوبی بود، به یک پل راه‌آهن در شمال کشور حمله شد.
در ماه‌های اخیر، جمهوری اسلامی حساب ویژه‌ای روی این مسیر ارتباطی باز کرده بود، هم برای ارتباط با روسیه و هم برای ارتباط با چین.
حجم مبادلات هم ۶ برابر شده بود به ویژه پس
از اعمال محاصره دریایی توسط آمریکا.
فکر نکنم تعمیر این پل ، خیلی زمان ببره.
بیشتر یک اختلال چند روزه خواهد بود.
هدف آمریکا هم بیشتر ارسال یک پیام بود
که جنوب رو محاصره می‌کنیم و می‌تونیم مسیرهای دیگه رو هم از کار بندازیم،
اگه قرار باشه شما مسیر تنگه هرمز رو ناامن کنید.</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/5974" target="_blank">📅 12:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5973">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MrDf0Qbe6xzzQyp2uGPD_ZmnRtvfFZsjPUNrJnRtvseJWvSpFXd4vMDr6FSsod2w2X98UMaI3RTL0qLDUbE8Ww4v-HK6esaFI4EWQc63Y5FZuJ0zP_08FXDArM_7IHembX_a4qpjt3Bk57rKTiUYg68XbvmJfulIa5yCZu_Q3Laq6_7rCrZKsEReH38gejj6jIpY5xEyr3d2rpOp2QSRZ8O3xrSMUjlx1riE-P0EMrxnRwx7f-q-ECJOn1kReC2GOwcWsmcIAAi6YFovdRYkiVfi_S6B_ItjXRPaVig3M42m22-Hm5xLl2_byzfRcmJy7be0hhjdFyTsGbQLClKDDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منتظریم اول
خامنه‌ای پرچم رو تحویل امام زمان بده
و نماز جمعه رو توی بیت‌المقدس برگزار کنه</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5973" target="_blank">📅 09:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5972">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">بیانیه ارتش : به اهدافی در قطر و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5972" target="_blank">📅 09:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5971">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=HeCYp-kNqau-uzr-H02SgxNMpNY87Ip76LORw8q9LSYFhcK5wfN5jHWffBA6tG6771rITxuFl2jHKoxv2n6485iKcSpBB2u7ZqPienuPLFgnleT4bZX8QPtxUX6xVWTkk2U97_--p3t7L2frUtT89yh7zbAziRwH2gLqmQm4dLm4qn7AVVo8FrVYwBq2-0CHNTEQ-hHxNZci_AezSiD-icpH_2ABad4NCqaKCgiI3Hs2K81kYwlP3PS4iABXlCCJd82wWR3aKOznAkybZO-YZSNESSCIcoykup3jF3ZQbZSKIDQGCMKCJhYpVzr4sf5RAEfYC3Oy7JYvhI_ofwRGnDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=HeCYp-kNqau-uzr-H02SgxNMpNY87Ip76LORw8q9LSYFhcK5wfN5jHWffBA6tG6771rITxuFl2jHKoxv2n6485iKcSpBB2u7ZqPienuPLFgnleT4bZX8QPtxUX6xVWTkk2U97_--p3t7L2frUtT89yh7zbAziRwH2gLqmQm4dLm4qn7AVVo8FrVYwBq2-0CHNTEQ-hHxNZci_AezSiD-icpH_2ABad4NCqaKCgiI3Hs2K81kYwlP3PS4iABXlCCJd82wWR3aKOznAkybZO-YZSNESSCIcoykup3jF3ZQbZSKIDQGCMKCJhYpVzr4sf5RAEfYC3Oy7JYvhI_ofwRGnDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میانه‌روهاشون : «بهترین حالت برای ترامپ حفظ آتش‌بسه، اما ایران نباید این‌ کار رو بکنه، باید کار دیگه بکنه»</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5971" target="_blank">📅 09:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5970">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=TGGc23GvSIBhrl-CFJRnl068ss5uEQcXeNRqYDXYzE54V6sGEnDZh7OzN82hWyWST_W-aMVdyq9jfyRAE_5vepxh5O47hTis-ymL4f6sDSRyeAIgVU61LcXZZKhj3rXQ52s2gfk68zwXNxghC2L-tlZ9ao4aDvgfpXBUzJgQ7ZMkT_sVzDJ_bko_iAWTHigzidtWT1JmN4G_Zm1zyhuMImbfQIkdLMTLl5zI3ldTesdQ5MCtQXdfjw9nvCgRVUNgcsK8SXQvEpoXWvycWTMccMufOUOZeotgoWlE9r3scQpIYf5a5LZkGcN6idbJtptBaecOwYoCslcKK0zu8-jlzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=TGGc23GvSIBhrl-CFJRnl068ss5uEQcXeNRqYDXYzE54V6sGEnDZh7OzN82hWyWST_W-aMVdyq9jfyRAE_5vepxh5O47hTis-ymL4f6sDSRyeAIgVU61LcXZZKhj3rXQ52s2gfk68zwXNxghC2L-tlZ9ao4aDvgfpXBUzJgQ7ZMkT_sVzDJ_bko_iAWTHigzidtWT1JmN4G_Zm1zyhuMImbfQIkdLMTLl5zI3ldTesdQ5MCtQXdfjw9nvCgRVUNgcsK8SXQvEpoXWvycWTMccMufOUOZeotgoWlE9r3scQpIYf5a5LZkGcN6idbJtptBaecOwYoCslcKK0zu8-jlzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تابوت خامنه‌ای، پهپاد وار به پنکه کوبیده شد
و موجب آسیب زدن به اموال حرم شد.
یه تشییع جنازه برگزار کردن، هر ساعتش سوژه‌ای داشت.  گویی فیلم‌نامه‌اش
رو رضا عطاران نوشته.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5970" target="_blank">📅 08:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5969">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">خودشون داغووون و پلشت دو عالم! برادرانشون در عراق و یمن و افغانستان پلشت‌تر!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5969" target="_blank">📅 08:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5968">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/736101eca8.mp4?token=OQahP5geU7PGonWLi2hfwfSXYHdZbXJa_laIyeBv2P3C36fEzJt-b5iAhUHpbpE08-o_nQAjFflTlvOuLIuLtEpfv6nRmYQ0E6VkvFlo-aI3YKzFApjKzJCwJihlZgItvs4M_emleSPIq5cTxchLJ-Ug4imxva2E_ZnBsdLl4BizLMc1oyjSkhb_J5_lnyuDV9M-eN4XpVNCZaheADB9q0X4K3df5bYHSCVpPjjsiwUB42Xw77seTDiDrXqeIgLoUNJE8tzU0fog7RLjj7zQFTVjgWkJyCaKBrE61M0zzC1flQfGUgf5vcJkbCNFXaOqkoXCibyDAlmkJ30FCtjIig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736101eca8.mp4?token=OQahP5geU7PGonWLi2hfwfSXYHdZbXJa_laIyeBv2P3C36fEzJt-b5iAhUHpbpE08-o_nQAjFflTlvOuLIuLtEpfv6nRmYQ0E6VkvFlo-aI3YKzFApjKzJCwJihlZgItvs4M_emleSPIq5cTxchLJ-Ug4imxva2E_ZnBsdLl4BizLMc1oyjSkhb_J5_lnyuDV9M-eN4XpVNCZaheADB9q0X4K3df5bYHSCVpPjjsiwUB42Xw77seTDiDrXqeIgLoUNJE8tzU0fog7RLjj7zQFTVjgWkJyCaKBrE61M0zzC1flQfGUgf5vcJkbCNFXaOqkoXCibyDAlmkJ30FCtjIig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون داغووون و پلشت دو عالم! برادرانشون در عراق و یمن و افغانستان پلشت‌تر!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5968" target="_blank">📅 08:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5967">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">‏استانداری خوزستان: سه کشته و چند مجروح در حمله صبح امروز ارتش آمریکا به اطراف اهواز
مشخص نشده که این حمله به کجا صورت گرفته.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5967" target="_blank">📅 07:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5966">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
سنتکام : به ۹۰ هدف حمله کردیم.
🚨
رسانه‌های اسرائیلی : با پایان آتش‌بس، جنگ در تنگه هرمز احتمالا چند روز تا چند هفته ادامه پیدا کند.
🚨
سپاه : به بحرین و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5966" target="_blank">📅 07:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5965">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
سنتکام : به ۹۰ هدف حمله کردیم.
🚨
رسانه‌های اسرائیلی : با پایان آتش‌بس، جنگ در تنگه هرمز احتمالا چند روز تا چند هفته ادامه پیدا کند.
🚨
سپاه : به بحرین و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5965" target="_blank">📅 06:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5964">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=U6EMWMwJSkT_zsHkPEoNGlknHDngOYLiyN_ob4pEObuerp360xXwf-XWQGSIp6WCnx_befReKeC3OPlj0gr7yxZFbVmYOyvkDciohQ-nLJV0dzVw2l8M5OrAA1R5RaOkmi6-5rOS9hE1ozmv0CzzOj7iT8LwCO4jFDbSzAzl_CVk21U48GHYnk85_498TzxW-akHsj03zGiDLWmEd3FVHH7bDeU3N2TpPN1qNKj77GfCEfMdP0vgRFs_ABPdOLZTgtQXFGjX_bgpDShKPXFTf26CeeK0CYtiihKlel44mx0o5UfHuUfVKLwlPTi6Eb5pV77PdZuuxDwu9XITXzj3sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=U6EMWMwJSkT_zsHkPEoNGlknHDngOYLiyN_ob4pEObuerp360xXwf-XWQGSIp6WCnx_befReKeC3OPlj0gr7yxZFbVmYOyvkDciohQ-nLJV0dzVw2l8M5OrAA1R5RaOkmi6-5rOS9hE1ozmv0CzzOj7iT8LwCO4jFDbSzAzl_CVk21U48GHYnk85_498TzxW-akHsj03zGiDLWmEd3FVHH7bDeU3N2TpPN1qNKj77GfCEfMdP0vgRFs_ABPdOLZTgtQXFGjX_bgpDShKPXFTf26CeeK0CYtiihKlel44mx0o5UfHuUfVKLwlPTi6Eb5pV77PdZuuxDwu9XITXzj3sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏میرباقری در صداوسیما:
‏دشمن به معنای واقعی کلمه هیچ غلطی نمیتونه بکنه، بنظرتون میتونه غلطی بکنه؟
‏مجری: بله دیگه، رهبر که خودش این حرفا رو میزد رو کشتن</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5964" target="_blank">📅 06:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5962">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJqeF7V7idRUumit7ViJgwtjM7tFWq7lP-HYvxhSVU-oUHagkut2MTtw-CznlVMhXbbooW2Ea_mqyFM5AW_FgGHM8KP19NaCS_392BGASQLwLvk-rAEnCJu6iDoBZImTu43M8_XViFt9CwMP1746fqlu8bwJ8au6_ZGcnrj1djww5mZAFKaJaZQAvdjJcBYKIZdYAG9PBCOLOz4eaTRusoUo_tWvr-lW-HFg4dX5AApc9yIV15ZhXUlCjBf32Rt_Js3BvClS8KEsY_P5CZbw5KtCK-OxVZJuSi8aqwiqm3HvyT0eFahKIb0EbCUGkKJCZ7-oCGaYbHaoV60wIp8tWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=p4bfz6S7khqBFc-5cTlEoNtpaYm0vhGC9qz2r7mfR1RirPBBqp31vInnLGYECVOuUIY6U18TUDHzzPmxdDGnmbDZ5j_m3poJpYgm0cidcVgZqbeyJId3IuM-5IMRjZmNOUQ0l1-el1HXqCa2rEYBH_Capeb9_RKXDszyA5XAKrK3VoDwHzSJlnmsqvkHFHmeq3Jquc5sD2cLGEfSqIGytZulJ8JkK00CsPJMOEatH8oda-qQEoZEZ84SN4_m9jC2eUqbRNAIHAJBi28EmCoVrCJkqTQifvQLkLNrPA8IVldIbMSHTwsERnouOnUAFRRl6nnJXCBWqM05gg0UpxUw-0WosDfHfG5Kw9EEtLb-nOPXRUrkdQTNCTxW2NrvTkVDY7-gaJeNg77zr_4E1Nes6FmL3_e1yozbxTK-0M-EcSuTV096EgTESJKpLAxBltqsbOdqkYXHiKCWzaR3ilds34-mVPtOg7fzqzBSYv6AsdrKfg86hRgxZkbuvDvdJe8rhMeBD4x8qmwxV42867f6fQMbRYHC_7fEYoXNOb0HlkIrRZ3TMsLnBE-LYSk6BPiWK_HinDlX978euhd2Qqu8H2I8wLy2IfqBcOH2AgWnrn_LFmjz7HjKRQWeiJ8iBeayysTdm2N8sp-VRgLHiFHtQR61ZRyB4_33GYQFJkNVVts" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=p4bfz6S7khqBFc-5cTlEoNtpaYm0vhGC9qz2r7mfR1RirPBBqp31vInnLGYECVOuUIY6U18TUDHzzPmxdDGnmbDZ5j_m3poJpYgm0cidcVgZqbeyJId3IuM-5IMRjZmNOUQ0l1-el1HXqCa2rEYBH_Capeb9_RKXDszyA5XAKrK3VoDwHzSJlnmsqvkHFHmeq3Jquc5sD2cLGEfSqIGytZulJ8JkK00CsPJMOEatH8oda-qQEoZEZ84SN4_m9jC2eUqbRNAIHAJBi28EmCoVrCJkqTQifvQLkLNrPA8IVldIbMSHTwsERnouOnUAFRRl6nnJXCBWqM05gg0UpxUw-0WosDfHfG5Kw9EEtLb-nOPXRUrkdQTNCTxW2NrvTkVDY7-gaJeNg77zr_4E1Nes6FmL3_e1yozbxTK-0M-EcSuTV096EgTESJKpLAxBltqsbOdqkYXHiKCWzaR3ilds34-mVPtOg7fzqzBSYv6AsdrKfg86hRgxZkbuvDvdJe8rhMeBD4x8qmwxV42867f6fQMbRYHC_7fEYoXNOb0HlkIrRZ3TMsLnBE-LYSk6BPiWK_HinDlX978euhd2Qqu8H2I8wLy2IfqBcOH2AgWnrn_LFmjz7HjKRQWeiJ8iBeayysTdm2N8sp-VRgLHiFHtQR61ZRyB4_33GYQFJkNVVts" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا به دو پل در استان گلستان - آق قلا - حمله کرد. یکی از این پل‌ها، پل راه آهن است.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5962" target="_blank">📅 06:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5961">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=r3LSEQtf61qodhQ5UjZUdOoUqC2rt3LJ2Bxn64vtpl9k4aefdl9f6-adaLt4PrTZVqonAOBho4W-pQAn5AtHHqjh0Kj7jwCgz85vW4ePuUvlz0SZ1oUUxN26G3Pkv21GdG32qqx7A63mEk4alz4Hx2TDUZfhnU5cO3otetPS6W9lkdaF9Vfq_ag8AsmgJopHwIHg4ZmNLyV8d06E_2EPQUaUg6U4aDC-VNUZTwCLo9TexwOk2hC97JsaVJMNFGlBsuAYifRKf5HjgXt3fO393asXNwJlHieCdG63gMXfBHdWT6lqibkTy5JyB2M6jMJdKX1uk-YJZ6RVqKuMxILN_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=r3LSEQtf61qodhQ5UjZUdOoUqC2rt3LJ2Bxn64vtpl9k4aefdl9f6-adaLt4PrTZVqonAOBho4W-pQAn5AtHHqjh0Kj7jwCgz85vW4ePuUvlz0SZ1oUUxN26G3Pkv21GdG32qqx7A63mEk4alz4Hx2TDUZfhnU5cO3otetPS6W9lkdaF9Vfq_ag8AsmgJopHwIHg4ZmNLyV8d06E_2EPQUaUg6U4aDC-VNUZTwCLo9TexwOk2hC97JsaVJMNFGlBsuAYifRKf5HjgXt3fO393asXNwJlHieCdG63gMXfBHdWT6lqibkTy5JyB2M6jMJdKX1uk-YJZ6RVqKuMxILN_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : جمهوری اسلامی یکی بزند، ۲۰ تا می‌خورد.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5961" target="_blank">📅 06:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5960">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iKeNorqo5p5P-pMdDkJ3TayVCYXA_unLnXqc-rn0LS0XWa_0OHunrgl6RItYJ3AmAKc1RKGwtLpN8E3UkBwGruUjxfoW9V7sZ5wbLiFHohdEVLbxrXXl678wJ0i1p5XQxp7a-sEeCyZpDjkK_DrEwJwRnyYaB_e9BhXrEQf7POyoxqKBQERszpQY6lNPO17ZYRGJhPdDmxiksvGRlz4GY7QVk3Q5Tn5aTWZDzxI4vxBqVyTgUSuBFaMYM9w18rVqajkjgOWRsKA1A7qytuzTT29LW0d5okMXooxcZbyn4seuxPtZsd-do9Nb2ED5aylkaQ5ej94yLYJuZ3da2Fdh7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5960" target="_blank">📅 05:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5958">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=EDVVK3FMwcT4pScCiwx4IzCKtFkncS0LVEz8hstvLoZZrRsZ-kmEHDT5wfEGBr6b-RZtYvpR_ZjMO8W5cdOOy-SbhqY-CdLmhqwWKC8UQGNEe7JRKn3sDPf8otqsybio4pa8EWshqOWvwe4HN6Yiw7NlnKxnWkSAs-LFyrXvdC93vcXkUceBwX-yA3SjDOzcUVZzV49PzHWTCUB9p4z2wyO5UCFMZcQJI4DsB71yfUuUZycBUXZ5za9fBDYGEbIjL0E5Rq3ObOJGIwoK5juSeQp6FTKX45Bj4bBv6SZnsnEUtHTlQ_04B7nX1johnef3iIjhUZv-dlkobI284iSu_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=EDVVK3FMwcT4pScCiwx4IzCKtFkncS0LVEz8hstvLoZZrRsZ-kmEHDT5wfEGBr6b-RZtYvpR_ZjMO8W5cdOOy-SbhqY-CdLmhqwWKC8UQGNEe7JRKn3sDPf8otqsybio4pa8EWshqOWvwe4HN6Yiw7NlnKxnWkSAs-LFyrXvdC93vcXkUceBwX-yA3SjDOzcUVZzV49PzHWTCUB9p4z2wyO5UCFMZcQJI4DsB71yfUuUZycBUXZ5za9fBDYGEbIjL0E5Rq3ObOJGIwoK5juSeQp6FTKX45Bj4bBv6SZnsnEUtHTlQ_04B7nX1johnef3iIjhUZv-dlkobI284iSu_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکله و برج اسکله بهشتی در چابهار</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5958" target="_blank">📅 00:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5957">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
گزارشی از قطع برق در مناطق گسترده‌ای از بندرعباس، بوشهر و چابهار</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5957" target="_blank">📅 00:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5956">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/693dd42141.mp4?token=MYYgdJz5JYlZ8EzdCYYzaCM8LltuvGZfFkgY5YVilGYtkOz6dPOI6blRKkECpzNLV_ykej6sdSvNBucT7fcmhZAFORCGtL8QDeGoVFk2tAqUdhVxc_Zw5sZHoOPuASFdUjc4n-UHN47_-q6BVjHaUuIwYYA7dq-Md2QQOxlXexE1ORIovr89oAYUht36A30YNpeQY48DQxZXvVobDje8jTmjNeNhm2WB9V6iMxvn4jV2yqinR9502xMveW6BhFduiRu49YbZp9jrI2EBt_OckYLAmZRjNGyhSfJY-MkD6RtC4Q8HM3hFtMjuH-F8eNB_bZwnlXq-w4WZBl5tzHQoCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/693dd42141.mp4?token=MYYgdJz5JYlZ8EzdCYYzaCM8LltuvGZfFkgY5YVilGYtkOz6dPOI6blRKkECpzNLV_ykej6sdSvNBucT7fcmhZAFORCGtL8QDeGoVFk2tAqUdhVxc_Zw5sZHoOPuASFdUjc4n-UHN47_-q6BVjHaUuIwYYA7dq-Md2QQOxlXexE1ORIovr89oAYUht36A30YNpeQY48DQxZXvVobDje8jTmjNeNhm2WB9V6iMxvn4jV2yqinR9502xMveW6BhFduiRu49YbZp9jrI2EBt_OckYLAmZRjNGyhSfJY-MkD6RtC4Q8HM3hFtMjuH-F8eNB_bZwnlXq-w4WZBl5tzHQoCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش سوزی گسترده در بوشهر
🚨
کشیده شدن دامنه حملات به جاسک و ابوموسی
🚨
گزارشی از فعالیت پدافند بر فراز آسمان اصفهان</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5956" target="_blank">📅 00:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5955">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LY7hAKtRUp0bx2ajK_oEltf-GDo-48GNMD3qSq0AIQZaOVCBz4_K1u10pM-ei8QF8SU_p4Sle3aA2FK_KcKQ3HxDpAFxZUnLa_tOuJfkibY1lTG83O9qVaprngzgTqYt886aIFIk1TUTuhbmKPv9mihtJZ41tUrHknbBdHeual6NgODc99jTP59jRsE7D6RX-gO-YvBMavxs4jcGH74cJwbgJPwMay9Jo6uKbN2YfnVjctQcKAZXVdpgjKG3ybDUvZYL4cJox9FvrGjSpUX3oPpbvHTrP5ZhOcoacZxTUVAto_agEmldfNvuwJriggmQry7GfAHaWBRmjJR8bruiqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت مجید موسوی، فرمانده موشکی سپاه</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5955" target="_blank">📅 00:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5954">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
گزارشی از حمله به یک پایگاه بسیج در بوشهر</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5954" target="_blank">📅 00:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5953">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e3ae34ead.mp4?token=hHxXhA53kWoGbELVqfwiGmlu_TourSAkNfuFFLeUkQiwOiUXpL5OI6FivQ3Fv9X0vnHdErdX612mNzHXdVGPykErYLBajIl8vqlwgH2eYc6E1Xuwb99NQ7-FCaKF1bRkFygoJgHej7jRAkyyBeZEwL9BahvtTFVfO_pq2cDQQvuHt4Q1KiCq5tB07gTqYazY__6GHX4J5f2o3p4IRsC3TLJlEXabHm48Pws1yV8CB-9EsdXOZYF6CI2xhYQlqMJniMv_rR6I7l_DgqrJNpG6qKOUh15G9kKsj-HHp-5lP1vsPfCukALLtygZuR0ISNwFnYpWE1i8EKrfJgXcHTSpdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e3ae34ead.mp4?token=hHxXhA53kWoGbELVqfwiGmlu_TourSAkNfuFFLeUkQiwOiUXpL5OI6FivQ3Fv9X0vnHdErdX612mNzHXdVGPykErYLBajIl8vqlwgH2eYc6E1Xuwb99NQ7-FCaKF1bRkFygoJgHej7jRAkyyBeZEwL9BahvtTFVfO_pq2cDQQvuHt4Q1KiCq5tB07gTqYazY__6GHX4J5f2o3p4IRsC3TLJlEXabHm48Pws1yV8CB-9EsdXOZYF6CI2xhYQlqMJniMv_rR6I7l_DgqrJNpG6qKOUh15G9kKsj-HHp-5lP1vsPfCukALLtygZuR0ISNwFnYpWE1i8EKrfJgXcHTSpdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امشب - چابهار - حملات ارتش آمریکا</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5953" target="_blank">📅 00:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5952">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l6tDpTNKS3jJo0qwcmKJrbloPajWb564EQxomSFP7ZW70XNo4gHa09WPeix59Qd5WVoxOq7CqXUX8HyRcHirEGxkREPGxl2WQ3qY_e36P-KHQFVheUryG0dCYqSYRSagDLBrX6vJEEpACkzmsm42zhl1KHW0sTiw9ygCN6E1Q_QDuCylYKBCNRIRbIkSfo6XZjIZaNQQ2_ncztv7ZgFSVPNYbWqeBgzUd9A0c_eC1Yshv7-3xhVSkT7cFRyI1rLbb2fgQGH770_5Gt4_ZSVwn44hWVD94ZxHUEVus30-IfHzUk3NF0MiYNYXpNGgnHpEPEZJLg7VDpEFh83KynCMJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله به یک سیستم راداری ضد هوایی در بوشهر.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5952" target="_blank">📅 00:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5951">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">حملات به قشم و بوشهر نیز کشیده شد.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5951" target="_blank">📅 00:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5950">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‏ایرنا: صدای حدود ۱۰ انفجار در چابهار و کنارک و قطع برق قسمتی از شهر چابهار</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5950" target="_blank">📅 00:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5949">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a030961c3b.mp4?token=psRNg61gsYmuLd09ux829q_smUZOiPr6hpI8vkgfE7fCZoGHcbCipzkgK3s6IJ0kGA-psluua0UZuOfsOaZasTtzA5IsF-itpWHya3kOgNYr9aDfpK4ZcNjAH67vRXY9GH4ZqlKcYjBUlnSgodCvPyjsXSuTxs5P9mzpTI_7Z1aqr-x8UMWnwvQFC4RisaahVn-5Xk_dZZMdSr4ARBhgQI5uY8_C8hhEFmQTdTFaZwp5v9RdVPF7FbB5cfaP-nsZ79uoXtAbY4vFXUM0rNoVI6L8Ua1rUPJu6BvUSxrQ80wzzUh4oQvUtGyMVw8uDGXTsft7kEL917XNhxiei7C1Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a030961c3b.mp4?token=psRNg61gsYmuLd09ux829q_smUZOiPr6hpI8vkgfE7fCZoGHcbCipzkgK3s6IJ0kGA-psluua0UZuOfsOaZasTtzA5IsF-itpWHya3kOgNYr9aDfpK4ZcNjAH67vRXY9GH4ZqlKcYjBUlnSgodCvPyjsXSuTxs5P9mzpTI_7Z1aqr-x8UMWnwvQFC4RisaahVn-5Xk_dZZMdSr4ARBhgQI5uY8_C8hhEFmQTdTFaZwp5v9RdVPF7FbB5cfaP-nsZ79uoXtAbY4vFXUM0rNoVI6L8Ua1rUPJu6BvUSxrQ80wzzUh4oQvUtGyMVw8uDGXTsft7kEL917XNhxiei7C1Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از حملات امشب آمریکا به چابهار</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5949" target="_blank">📅 23:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5948">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YW_KwtxNfGyA2uOBS-myf9SJudw4Nz_J61T8sJtZyHlqV9HgKZDOYOm5TReTbN7ts-td9SJvGPEQkQama4OxfRWMEmBp-8cGIkDUWrTL_Rod8Jn60kCk8QOy5jO4QcK1n0i5ZNMYLVuvIumEaT29siQSSLO1k1PjecEjzFpqpenrytXMFYT2Zuu_Y5GHoQQ8WNBl88__UqW7hjSpX0Ingczcgoc6oeL1hHADJdLUIbsNvQbYAqCvETWGaM8LX2WJMllzYpTsKaO-hCb9ZWxF37ObD2TTNfeqpXiNMUPmSUWcr1vj8j8PN_L8NkibV6H-QBFSL_Kx0rR0LyZhoiURNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به اسرائیل اطلاع داده است که قرار است امشب حملات گسترده‌ای به ایران انجام دهد.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5948" target="_blank">📅 23:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5947">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌هایی از شروع حملات آمریکا در جنوب، حمله به مقرهای سپاه در سیریک و بندرعباس.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5947" target="_blank">📅 23:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5946">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌هایی از شروع حملات آمریکا در جنوب، حمله به مقرهای سپاه در سیریک و بندرعباس.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5946" target="_blank">📅 23:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5945">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">جی‌دی ونس که طرفدار مذاکره با ج‌ا بود:
قرار بود ما محاصره دریایی رو‌ برداریم و اونها هم‌ دست از حمله به کشتی‌ها بردارند. برای یک هفته خوب بودن ولی در ۲۴ ساعت اخیر شروع کردن به حمله به کشتی‌ها.
بهشون گفته بودیم اگه
حمله کنید به کشتی‌ها باهاتون محکم برخورد می‌کنیم. نمیخوام بگم امشب قراره باهاشون چی کار کنیم.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5945" target="_blank">📅 22:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5944">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c3530f756.mp4?token=BIiLI88hNIpNq8LPL0Gif4r2T9IytPYSyDQj2thygsrTvN9OsuMHC8ZKfZQEpbj-KDvG9PYRr4xFb0UpuKyHLbKiNFnuJW8JA10J4UztLGd3HOp1yanbJ7sLjFNMRhC0FsCdn9gR4FRGPZBreC-8_SaHhgwNqMckJsqNQrzCUtnGWM9CusPmYYt-R5iSwKwFLBDqI1UXRket-aNHcQqcGRLiW2XUrus6doyogYWdma32sRhpfvZTh0Qcz5a4Pju2YvNaWOq1daDLpbklh9FZWB0URlzCx33qqDaLCXmCrF2OrbZGlfnciWYmObYQI9Jv8W39hZjDk1v12Tzg765_0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c3530f756.mp4?token=BIiLI88hNIpNq8LPL0Gif4r2T9IytPYSyDQj2thygsrTvN9OsuMHC8ZKfZQEpbj-KDvG9PYRr4xFb0UpuKyHLbKiNFnuJW8JA10J4UztLGd3HOp1yanbJ7sLjFNMRhC0FsCdn9gR4FRGPZBreC-8_SaHhgwNqMckJsqNQrzCUtnGWM9CusPmYYt-R5iSwKwFLBDqI1UXRket-aNHcQqcGRLiW2XUrus6doyogYWdma32sRhpfvZTh0Qcz5a4Pju2YvNaWOq1daDLpbklh9FZWB0URlzCx33qqDaLCXmCrF2OrbZGlfnciWYmObYQI9Jv8W39hZjDk1v12Tzg765_0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/farahmand_alipour/5944" target="_blank">📅 22:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5943">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe5d27edac.mp4?token=KkkseBSes2NikL4SONuUUVQzS8T4vy3vBnjL1RD-JqmMnmyLB_1JHwpsCzWLkVUnWcFuzg4GVlA9wMb1e1NXsiS3Jnd2LpGRlWI_vVRAG1dDtL4mEtt-vYFOEhrf0ma27BD23VK-iRqb5S0n3ntdFJY5sr1XFJqIJCGsAJTt5gGLOANvsjAt4GQ8IfNR7q0sHOTWTPUnEiUWwKTk2JErKEBFO2OjAHMARO8SovUY7jaqiFloO43wc0_h5Nc8PYNWbp6vEWSWsUDz4DVLlVVLEccm5WZKl7n1LEe7KIJiIBntikf4jVqOy8-eweNcIMYbjVM6kyr9SXzLxXZOFzllJ4UL292V5BsRIik6XwwgbeA1-KlniCMvGFQRr1jIx1k-ss_Fb8fgwrZkU30Xv2bmmjT-UTGo-4qbWc9oqNinwERFRUhZK1UCYK-HvTfZ25TOxHKBdOcWb-5BLJ7oSVx9JfI5geNxUcha1R5eDR6kqDy4qNaJBhbo3L-IlvtMpBTGAVZ0StTdyMEVRd-1BDEwaw8PrmnHWdCaQDmcc7fP55k9UBWX0BCQjCSLhq8URy39MehICnWeKpOuQcVa3D2TCOJ7kQ3itd8xu7v7afVX1TLJTo4JRyw1CwpJnB40ebxwNQ9Bl6f00HUVOT0ObXiaLZcNFkmLLeY_aG8qjoKv6A0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe5d27edac.mp4?token=KkkseBSes2NikL4SONuUUVQzS8T4vy3vBnjL1RD-JqmMnmyLB_1JHwpsCzWLkVUnWcFuzg4GVlA9wMb1e1NXsiS3Jnd2LpGRlWI_vVRAG1dDtL4mEtt-vYFOEhrf0ma27BD23VK-iRqb5S0n3ntdFJY5sr1XFJqIJCGsAJTt5gGLOANvsjAt4GQ8IfNR7q0sHOTWTPUnEiUWwKTk2JErKEBFO2OjAHMARO8SovUY7jaqiFloO43wc0_h5Nc8PYNWbp6vEWSWsUDz4DVLlVVLEccm5WZKl7n1LEe7KIJiIBntikf4jVqOy8-eweNcIMYbjVM6kyr9SXzLxXZOFzllJ4UL292V5BsRIik6XwwgbeA1-KlniCMvGFQRr1jIx1k-ss_Fb8fgwrZkU30Xv2bmmjT-UTGo-4qbWc9oqNinwERFRUhZK1UCYK-HvTfZ25TOxHKBdOcWb-5BLJ7oSVx9JfI5geNxUcha1R5eDR6kqDy4qNaJBhbo3L-IlvtMpBTGAVZ0StTdyMEVRd-1BDEwaw8PrmnHWdCaQDmcc7fP55k9UBWX0BCQjCSLhq8URy39MehICnWeKpOuQcVa3D2TCOJ7kQ3itd8xu7v7afVX1TLJTo4JRyw1CwpJnB40ebxwNQ9Bl6f00HUVOT0ObXiaLZcNFkmLLeY_aG8qjoKv6A0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل برگزاری مراسم رو
انگار غزه است! با بسیج کردن اینهمه ستاد و پول و ارگان‌ها و…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5943" target="_blank">📅 21:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5942">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c0giL4AEv78UX4fPc5gjrCs9YLRd-PEhlZ-rQD75omOPuxIClyJ9Btjju8A7hCJKk4c9h18nnKUGlBHYt2seNq2tSqr4txtK2gGpZJDpPKNanHaoRZP6d97UibkHDZwTrj2tFEyxhMDKI9EJG1q5qzfGS980ccOIHdlXLLRhAVYCcW6DnJ9e6jh9Ue3GaypYB8YqieJpobkSoyIapKeVFdKfzfU94YoxOf5wRtz6zAivQXIHCjmIhseLalka7lFvzB_0rHa3VvCom-rawa2_WX-ypzDEBgcCFuM37NvhqHPROsk2Mc83vbD7wfmfcccU0rn1AJ3mG-oizkAylvTbww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: درباره جمهوری اسلامی کارهایی انجام می‌دهیم که باید ۴۷ سال پیش انجام میشد.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5942" target="_blank">📅 20:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5941">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c3c23cc7c.mp4?token=T73tXQNGCeZmA4IcrfWfea4EYPUzSxvkNlgeKihSXaOef4Ft1Su3REXvsT5st3O11kbxThnpxFfnC94BuKW8iXqGfQZ6daj25uTDxgr5flJJHJxs0n3ESbx9iE_wZuzBOG-32AC4n8OfTTNeqbFoMre72bOLlclUBjdx3SbqaQd6-TPrlbWrZijQjgEAtq1vqqCu58Q_z0ucrHEOUREakGE_8eoXdQm7yFJxyA6342rFqJ_YnTibRNRh-CqbJDloqasJrYZkhGl5GOr3xCkn-mCeaSHxBGQ6vhVNofUqa0f14E1VrYzUB7jYRT693B7A21SUoGYtGh-xVKy-qJBKHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c3c23cc7c.mp4?token=T73tXQNGCeZmA4IcrfWfea4EYPUzSxvkNlgeKihSXaOef4Ft1Su3REXvsT5st3O11kbxThnpxFfnC94BuKW8iXqGfQZ6daj25uTDxgr5flJJHJxs0n3ESbx9iE_wZuzBOG-32AC4n8OfTTNeqbFoMre72bOLlclUBjdx3SbqaQd6-TPrlbWrZijQjgEAtq1vqqCu58Q_z0ucrHEOUREakGE_8eoXdQm7yFJxyA6342rFqJ_YnTibRNRh-CqbJDloqasJrYZkhGl5GOr3xCkn-mCeaSHxBGQ6vhVNofUqa0f14E1VrYzUB7jYRT693B7A21SUoGYtGh-xVKy-qJBKHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - اسکله بندر عباس
زیر حملات ارتش آمریکا</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5941" target="_blank">📅 20:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5940">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dd51af5b9.mp4?token=i5Qh_sCg74boa8bc0Rk6N8l-WSEL9-lx22glmUgOfxUv2yNd3fWpVsFMNxLBODNKqM0MJey2twok0td6mfaCY5FuI2yPuyTA0Fbb6XxuPBeqtomNC1696z2nNAF-smA_tOS54qwLTJ6iIx7RBKlnuIVrQ0cjdPbBMW539r5eA-UCXjUcZD6HDf54-oOW9w2LSwBU7tSknqqhcVQC3CZ6iaiIQKC0MsyVnxWjzOm2JEwqYXENWa2c89y1eWmyTEU9JV6goAbqos6wAWAua61C9NM1ocn_w2qwjQ5oG2ocMDkXocPWBcrhZbQdE4eXUXA2BVatPzii3H7705e5HX6-YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dd51af5b9.mp4?token=i5Qh_sCg74boa8bc0Rk6N8l-WSEL9-lx22glmUgOfxUv2yNd3fWpVsFMNxLBODNKqM0MJey2twok0td6mfaCY5FuI2yPuyTA0Fbb6XxuPBeqtomNC1696z2nNAF-smA_tOS54qwLTJ6iIx7RBKlnuIVrQ0cjdPbBMW539r5eA-UCXjUcZD6HDf54-oOW9w2LSwBU7tSknqqhcVQC3CZ6iaiIQKC0MsyVnxWjzOm2JEwqYXENWa2c89y1eWmyTEU9JV6goAbqos6wAWAua61C9NM1ocn_w2qwjQ5oG2ocMDkXocPWBcrhZbQdE4eXUXA2BVatPzii3H7705e5HX6-YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه مراسم برگزار کردن … ستاد برگزاری ، هزینه هنگفت، ده‌ها ارگان و ستاد زیر نظرشون.
بعد کارهاشون رو ببینید!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5940" target="_blank">📅 19:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5939">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nAiOEoiAkwdU735m6J9vqD5Sf4T1ehD3OEUTSiwkyl47PEubO__Ijl9WSzE8D36Q4BT-yNvybohueSaClqNtUl177IypYv1FPjCd1ISImuMJ2QeAgDfg7c1HYFZoVEfAkkE-g9dJj3_4SbzRaxnA8wV9QSusvW7Bt2Y6DXiZ3zymFQ6Pimh6o7DxBxRudc2OEyryIBiAIhoaGqV-b3Ygq8IyWiFfsUSHL8lTRdYyrdAF-r_sknMV7QVCSqCX0X5lmglCcdpuLM0vQo4XyhH0uuxW_PFe00RvtTQT3ZUf3krUnR-uwB07hBtr4LdNhHp7YCOd23wLTmDqdRBb3LyY5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کشته شدن ۸ نیروی ارتشی
در جریان حملات دیشب و صبح امروز آمریکا</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5939" target="_blank">📅 19:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5938">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ترامپ: اومدن خواهش کردن زمان تشییع جنازه ما رو نکش. بعد وسط این مراسم حمله کردن به سه تا کشتی.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5938" target="_blank">📅 17:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5937">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=ENkOZk5zqtI7P5_sl2TLH9lCeLMIGu5pgJGUODQzK2I8agSiedH9gT7eCRZ9g-ZzcwTrwFe2ZV2U3IzmwIdvDLj0oHHYfMt4Az_nHe_otdQElM7ll0FNxd8srcYAiwq1QvCAFNar9DjKy6pX57QPxJn9UXncc-rAuAAmPnYoVrtji1ysJaBO78E308x7LNcuLNctqSB0yEZVPzGhPUJSgRZLgvukMUJ64PZFGuy11k035msCGFknjigV3pn_u2v3fY699Jk96or5VXcb8Qk1DapFZvI6ptl2_HmF__2Rk5XHPEW8g_-MLo8scrQ2bQH0WTPf-T8RIjEqIqcRK1k0qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=ENkOZk5zqtI7P5_sl2TLH9lCeLMIGu5pgJGUODQzK2I8agSiedH9gT7eCRZ9g-ZzcwTrwFe2ZV2U3IzmwIdvDLj0oHHYfMt4Az_nHe_otdQElM7ll0FNxd8srcYAiwq1QvCAFNar9DjKy6pX57QPxJn9UXncc-rAuAAmPnYoVrtji1ysJaBO78E308x7LNcuLNctqSB0yEZVPzGhPUJSgRZLgvukMUJ64PZFGuy11k035msCGFknjigV3pn_u2v3fY699Jk96or5VXcb8Qk1DapFZvI6ptl2_HmF__2Rk5XHPEW8g_-MLo8scrQ2bQH0WTPf-T8RIjEqIqcRK1k0qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دشمن هیچ غلطی نمی‌تونه بکنه
مجری : خو اومد خود گوینده این سخن رو زد!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5937" target="_blank">📅 17:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5936">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/046bf7600e.mp4?token=c_u68F_d1D24PAjpMkVFa4ynO1FuoSaLDtgujrvl32LbLBN2FuLL36nNQ7IWPSXEsjmHVeayJ9uI9cQzI_UvynkhzafTEofvR6y85iATND4LxGexbNn6Sdds35VNDq2gUHIfd3IfV6MRGjAG3AgdmXYjM2zKOlQfk4k-AkkRo3ejzrcC8f-P74Yk_sasDeVMvMmegGQublP1iP0MvpiM5TMcezF8Ayxl1ntI9b8KIou-XVdK-6uIR1ODgettFoCSB7LbHX1etZhIIQkC1RRNhIzEZXvRGf4owF4PFz23v2lJMqvX_iPtfwZrWF_RfSbCFi6gZkfMhh1Q0ShnPlNobA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/046bf7600e.mp4?token=c_u68F_d1D24PAjpMkVFa4ynO1FuoSaLDtgujrvl32LbLBN2FuLL36nNQ7IWPSXEsjmHVeayJ9uI9cQzI_UvynkhzafTEofvR6y85iATND4LxGexbNn6Sdds35VNDq2gUHIfd3IfV6MRGjAG3AgdmXYjM2zKOlQfk4k-AkkRo3ejzrcC8f-P74Yk_sasDeVMvMmegGQublP1iP0MvpiM5TMcezF8Ayxl1ntI9b8KIou-XVdK-6uIR1ODgettFoCSB7LbHX1etZhIIQkC1RRNhIzEZXvRGf4owF4PFz23v2lJMqvX_iPtfwZrWF_RfSbCFi6gZkfMhh1Q0ShnPlNobA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
هگست وزیر جنگ آمریکا : همونطور که ترامپ گفت امشب احتمالا اونها رو عمیق‌تر و محکم‌تر می‌زنیم.
ترامپ : محاصره دریایی رو هم احتمالا دوباره علیه ج‌ا برقرار کنیم.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5936" target="_blank">📅 17:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5935">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aff1f3384.mp4?token=D1XnvR1HDo7qTR_KBFDZVCkry37DkVVAiTVxmudzCzglgbdkjzvWpRsnyF4IwgR_gj0agXwAvOLpFPgToq_rbxvtBhQBZW0NoY817TYoW3nIMB2Ov6ltCTLHVsz3JsCLZAJDxk5wHqnpE2zGnGdmBx8m2hZVlxfEUC_-chma2eATIqOjtj1nT5b4RMp6mNck797xxL_U-EatboqY0UZ7toS86_oA7dO_uGHPQt6RzMLLI2hFwC82AafsqQ1MdNJBX3oef6zkcw9yax5Y21ENpDHFdmfKPXyivA7zEBjU4JZcU-VR7IrhiUA1YyKnBG3i_WaTor1IWRpkPO0wJbtN1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aff1f3384.mp4?token=D1XnvR1HDo7qTR_KBFDZVCkry37DkVVAiTVxmudzCzglgbdkjzvWpRsnyF4IwgR_gj0agXwAvOLpFPgToq_rbxvtBhQBZW0NoY817TYoW3nIMB2Ov6ltCTLHVsz3JsCLZAJDxk5wHqnpE2zGnGdmBx8m2hZVlxfEUC_-chma2eATIqOjtj1nT5b4RMp6mNck797xxL_U-EatboqY0UZ7toS86_oA7dO_uGHPQt6RzMLLI2hFwC82AafsqQ1MdNJBX3oef6zkcw9yax5Y21ENpDHFdmfKPXyivA7zEBjU4JZcU-VR7IrhiUA1YyKnBG3i_WaTor1IWRpkPO0wJbtN1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : اونها تحت یک توافق هرگز به سلاح هسته‌ای نخواهد رسید، اما شاید بدون دستیابی به یک توافق هم به این هدف برسیم، اصلا شاید راحت‌تر هم باشه، چون اونها دروغگو و‌ شیادن.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5935" target="_blank">📅 16:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5934">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5484fca6.mp4?token=fK4YHv7wYmxVkuTjgpZtaVIusU9aa_j1ja3lBFCIeshRCBO7QaR6CAU6CsDXUhx86CxU1zJ3oYeSZas2Mreth1VC7W0n8q7Uwb9pHkNgQaFfZ1eTjqkK6FyB24EoH1LOrPlUaigam7uifWS_WPFUKI0lEuZXYFk7lrFgNJYl0rqyrCMnOuCMgcL7iSDF-qB5MS9lv-1xMa8Jr5HtMO3P7mGngMIaWGhZNpx7mARrqTDHQENG8c3gK2AcFPjk4kjEyBFwnkuFaX-b0z3OonYgOJZXhRIBCnOE9nHYnfvpkdDQKSmyxF6VB5uJ7tq-y5ed5PxrOuhccOKQKSQqtRnDUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5484fca6.mp4?token=fK4YHv7wYmxVkuTjgpZtaVIusU9aa_j1ja3lBFCIeshRCBO7QaR6CAU6CsDXUhx86CxU1zJ3oYeSZas2Mreth1VC7W0n8q7Uwb9pHkNgQaFfZ1eTjqkK6FyB24EoH1LOrPlUaigam7uifWS_WPFUKI0lEuZXYFk7lrFgNJYl0rqyrCMnOuCMgcL7iSDF-qB5MS9lv-1xMa8Jr5HtMO3P7mGngMIaWGhZNpx7mARrqTDHQENG8c3gK2AcFPjk4kjEyBFwnkuFaX-b0z3OonYgOJZXhRIBCnOE9nHYnfvpkdDQKSmyxF6VB5uJ7tq-y5ed5PxrOuhccOKQKSQqtRnDUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ساختمون همون جایی است که خامنه‌ای حامیانش رو جمع می‌کرد براشون می گفت :« کشتن بد است، اما فتنه بدتر است.» (پس معترضین رو راحت بکشید)
و اونها هم براش «حیدر حیدر کنان» می‌خوندن : لب تر کند امروز سحر قدس شریفیم!
ولی داستان یه جور دیگه شد</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5934" target="_blank">📅 16:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5933">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=RvWmpU1cIHEXlv9AK-bgOmNd2b8n2PSKpqbNYt0rCDmG2Ex69RL9k4kyEgmpihqQUKsg6xcbTDA8eC5B3NRtypWveJ1IeEtR80io9JrHXCjftl4mwjzUeZm4xLVtxgJWKQAQFypPxn1RYDqW1ECIq15PruSIzBmpZFfcXw2y1CWi78_c0QjskwrVp1kzKisqk7EPRMwh_SA9r4SO27gXuZ3LmhI0_qta8rIrcI2Skac6EcGmTdIMINRr_nEr-TNW-VjY59yylIDqxWVd7_Rds_4Iz1-0dr9gcT59CvBRzjbRltS8z4WJ6MquUr6OwFgKcy9aZzvaCuq6-tBF2vF5qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=RvWmpU1cIHEXlv9AK-bgOmNd2b8n2PSKpqbNYt0rCDmG2Ex69RL9k4kyEgmpihqQUKsg6xcbTDA8eC5B3NRtypWveJ1IeEtR80io9JrHXCjftl4mwjzUeZm4xLVtxgJWKQAQFypPxn1RYDqW1ECIq15PruSIzBmpZFfcXw2y1CWi78_c0QjskwrVp1kzKisqk7EPRMwh_SA9r4SO27gXuZ3LmhI0_qta8rIrcI2Skac6EcGmTdIMINRr_nEr-TNW-VjY59yylIDqxWVd7_Rds_4Iz1-0dr9gcT59CvBRzjbRltS8z4WJ6MquUr6OwFgKcy9aZzvaCuq6-tBF2vF5qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ : احتمالا امشب هم اونها رو به سختی بزنیم. فقط دارم یه هشدار کوچک بهشون میدم.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5933" target="_blank">📅 16:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5931">
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jOFjdnIZ3wt5YV1STXfWUKr4j6hm3jDNpoIH5dlbC4uz7xqfDCOuq3C4t8jJQgzp3YKtzLWhXAMJS7pfTwawLLAC3CObooFA2yleXvM--qOtVuqLmzTxRCgCth6GTBS2XV0DOWo9XBNldnXB11FlRVzN0HdGjRFoALfCKIMU5rUrju65tUY-Z4MDfLT-r3ZmL8kCAHFBbDraTWv0nLSJpb3KTBdBBygfFTktvWNG6SxmwIegOeJeRxP3F9di0DPA2FSOrN3DsIAyGPbuUi_Z1UWCaFCh6eAe83Bf8KeWjLR7OmQsObVP8Q3QLwyV6f4sun6cjD9_xBqtPeBPPLFBFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه کیهان زیر نظر خامنه‌ای در دو مطلب خواستار کشتن ترامپ شد.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5930" target="_blank">📅 15:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5929">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : «آتش بس با جمهوری اسلامی پایان یافت. مقام‌های جمهوری اسلامی شرور، بیمار و فریبکار هستند.
آنها مشتی آشغال هستند.
به آنها یک هفته فرصت دادیم برای مراسم خاکسپاری، ولی در عوض دیروز به ۳ کشتی  حمله کردند.
آمریکا زیاد از حد وقت خود را با اینها تلف کرده است. اینها شبیه به یک غده سرطانی هستند. غده سرطانی را باید سریعا جراحی کرد و دور انداخت. »</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5929" target="_blank">📅 15:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5928">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XmbAyo-lAo1zKku3xDph5kfEhREaFA6hS_sDIIECAw66gcxr0HtCSBIHS-svGw5w96kTOy-7mzPpB3LAGXsmpmtJxjO78p-EjJh_-KFzF3dt0b_B2lbJeihcY5hP-34N4LXiiYosL04MwUyEN1d28Jfo3ox39h9-XcE7-CQRxmU9QbXC7S3ZCkgYqGBNKS49b36Rq7XlCEftHIFBI3plnE0hYsxDisjumbFKV3b2ro1MyPb2fuj9p-GRys-ZZHTeznPqoTRMQancrY2_T6TKN9pG7lBKTHa9Z3cNyUbDEACBCA9eGo59AFIt44bQDR5H6TyE877DQajBiy71JBJw6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوش دولت چپگراش رو چنان بکش
که درس عبرتی بشه برای بقیه اروپا!
برو جلو! دعای خیر ما پشت سرته!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5928" target="_blank">📅 13:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5927">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">محمد اکبرزاده، ‏ معاون سیاسی نیروی دریایی سپاه، ‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.   او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.   جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5927" target="_blank">📅 11:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5926">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
دبیرکل ناتو : حملات آمریکا به جمهوری اسلامی کاملا ضروری بود.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5926" target="_blank">📅 11:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5925">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OUw8MDX_c3iCxeRsMUh-YJxl13ZTG0MXcAzewm11-yzuD-uw7KWgI4ImeQd-VbaVU_UAAQdG2ZTZqSRemgALVKVc4nHADoCAIXlXrKbHIwS_Ltmd-n_RW1sldZcV9C711oqz2AsVwgql7aMu6JdEPG5FTxsGBouEk6zvzNPXmsKVEfY8uFGHQadrWyGlE9kezgWaTFos4Lb2weHxjglRD-GBgCOsmUOqz7bZcfeR3QWEsMZhCsAjXlUkUpWrvStSely9ahf4GET2ZjZv1b4ADxBT8l4hZPxUNYFQ8jrmjoa_QZrp5eJthwQ4EOpqZT7OTAwh_oXFt9FVvFhTq0PuaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بندرعباس - پس از حمله آمریکا</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5925" target="_blank">📅 11:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5924">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">پذیرایی گرم از عراقچی این بار در عراق</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5924" target="_blank">📅 08:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5923">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
سپاه : به ۸۵ هدف مرتبط با آمریکا حمله کردیم.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5923" target="_blank">📅 07:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5922">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aada56b9e2.mp4?token=UjvbF2e117KrspP8a2hWFrAlswPairjqKFFHZMG5yLXKFpBVic8qV_Y-9JNLZJVhvWNRGGRhAjPuTbstAOtnOBiWOi0gIajtoyzEo9l0S2Lg6Rmvn4oAat6yNKxRKwIe3H2QNuXzcy5VxqccXj8ZBo1YSE3PlqnKULNRN-Ps0nSZAbAGvYi-ik6rBk12j52GG4najy2LbrOPpdCRlDQY34ShDmjVWYAd6UfACqG49c5Q0cY8JIQBEVaUoSyseFhzTs0Fqr0UC6U1mgUaFjwZAuFSk3hrGygDU01A0dy7xpWkaE8KJBRAfH_OPf3b9BOjUk_BxpNzoQszpJ3TrIn76g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aada56b9e2.mp4?token=UjvbF2e117KrspP8a2hWFrAlswPairjqKFFHZMG5yLXKFpBVic8qV_Y-9JNLZJVhvWNRGGRhAjPuTbstAOtnOBiWOi0gIajtoyzEo9l0S2Lg6Rmvn4oAat6yNKxRKwIe3H2QNuXzcy5VxqccXj8ZBo1YSE3PlqnKULNRN-Ps0nSZAbAGvYi-ik6rBk12j52GG4najy2LbrOPpdCRlDQY34ShDmjVWYAd6UfACqG49c5Q0cY8JIQBEVaUoSyseFhzTs0Fqr0UC6U1mgUaFjwZAuFSk3hrGygDU01A0dy7xpWkaE8KJBRAfH_OPf3b9BOjUk_BxpNzoQszpJ3TrIn76g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بندرعباس - امش</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5922" target="_blank">📅 04:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5921">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ffEWoxJHQvggoh8_Hk5j-AciKzW52umsvoqv9fm-4lOpfm2qyq4CQ0lMYX8GNfE54ulUcz7b9tO_vTXD00SJX8OoAt2npDFSSn56HRHc_WKn_xmXhYcJTZ9q2KSnISNa9NM2DVOkTrASUcAM-QTYcqZQP4WqfQs5Dv5FVgwB0_8DaqD0Nr4oX1oXx199xgwEw-2Y3GsmK9pnYNHmG-EoY6WistBFWvFPe-P_v11D9ZHVjQSjXG31maKLUhwEnDo7arLSGTRtyW7wxc9Fn8kdDqnDIUNpuNLEmRCpjee3aeE06WC9MmHTUUfVQuAi9Lg4dxz219KCwK4MvRLiGbcvAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارش ها از شنیده شدن حداقل ۳ انفجار در بندر عباس
تصویری که گفته می‌شود آتش گرفتن یکی از قایق های تندرو سپاه است</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5921" target="_blank">📅 01:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5920">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا: نیروهای ما آغاز یک رشته حملات قدرتمند علیه ایران را آغاز کرده‌اند.
‏حملات آمریکا در واکنش به حملات ایران علیه سه کشتی تجاری است که در حال عبور از تنگه هرمز بودند.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5920" target="_blank">📅 00:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5919">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای چند انفجار در حوالی قشم و سیریک!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5919" target="_blank">📅 00:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5918">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f02faf66.mp4?token=sDL3arUrG7MMWgVCKOKxhB6Sb04yNOJJ2ZWqneGiL-zXaR8HUUF9nwnyCLcPrBuK4MfUIeV9BEFdQsqwzAjfGnd-arpvvFbQOMmFZCirKpzUzpjpTM2ZSPY0F7cQEO3ZJpiAzoSZXuqgJ_JzoaINEKKzcaowHI6Rdcp4iJt5pTVtpeVj9uBkmkeOysJi064rxnU39lH7l8U9BthJmZ5NO8s4PA2V-I-OaYkPgBfHLD6SWK-XOk98kefxZwhDkGJLWsbBYQdBCa9d72yP9F_hqyh2rvblaqedO6uspYi7v__bTSiH5KvutlC5TEPgQh4Ofdrqjr4lp43YOXagMqgD_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f02faf66.mp4?token=sDL3arUrG7MMWgVCKOKxhB6Sb04yNOJJ2ZWqneGiL-zXaR8HUUF9nwnyCLcPrBuK4MfUIeV9BEFdQsqwzAjfGnd-arpvvFbQOMmFZCirKpzUzpjpTM2ZSPY0F7cQEO3ZJpiAzoSZXuqgJ_JzoaINEKKzcaowHI6Rdcp4iJt5pTVtpeVj9uBkmkeOysJi064rxnU39lH7l8U9BthJmZ5NO8s4PA2V-I-OaYkPgBfHLD6SWK-XOk98kefxZwhDkGJLWsbBYQdBCa9d72yP9F_hqyh2rvblaqedO6uspYi7v__bTSiH5KvutlC5TEPgQh4Ofdrqjr4lp43YOXagMqgD_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی این ویدئو دقت کردید یه نفر رو به کامیون جنازه خامنه‌ای وصل کردن؟ :)</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5918" target="_blank">📅 00:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5917">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NONSaQVZ4IVu0OwY04SGOje4__tSb3676EPYeJUiUNsePehfWssl3Q6b8RgdvaJ7jRiQUiV8NrMXNjw1xlsWjuOb9Sri6wxTAlPQRk4c7lT1lk4F9SZIj_Gx5lJFeDJBIkSEAhiUvU3an7SuY1bwSQu8vrI8F62NRdlsSi-zyS1odxWwP7_x3C11s4hP6A9CLSmVMNxd1qhfhYoo8ZYDpTLQ8NaqMdWXOGqUpbxISLfGATuTE2MYS8fT_6PCHOmmtp3bhDAuLncFf08ZsQN9O2J4e_NZ7RgC6LywEr_v8H9XWtsxmjzTg56gnDMoeJEcZFxObmG5tCt1N-CcSOIWeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو حقیقتا یک سکانس تاریخیه، مدلی که دارند خودروی تابوت خامنه‌ای رو اسکورت میکنن :)  دارند جنازه خامنه‌ای رو‌ از جلوی خونه‌اش رد می‌کنن، از همین هم‌ پیروزی ساخته و‌ میگه چقدر قشنگه آقا خودش اومده به دیدن.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5917" target="_blank">📅 00:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5916">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkhpuQB_RaE2Kpv6NHjzl5uZ4j7YXqg9QaU4rK52tH5AHPaDc725qhafbugKcy_lnpnl2d6gEwu9jF2q3rGYVBHCR5CRtZrmMuFeBHFSfo1Hkx4MCU8lqNj4czIURNW7o1nKPnLafeca_gRVmYyKWBUtx4z7gAE43XSm-d1cWosKgLbWfr4QDreTE_Dg-lxn-2Td5cQbRmbkYGLdNkQwjSaTJZYuEchnHBlztQbrDPqRCQCtCfPe68006jDP_5quG-smYRiuXrk4I9nyJDoeH4IyCETsLQPO70Mvc62QpxZtHRuOUf_-PJxgHhhBN9Pkco_JdcPZrwX3d31n1OwQvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ما موشک میزنیم بر اساس حسن همجواریه
شما بیانیه بدید اعتراض کنید
مغایر با حسن همجواریه!
کشورهای همسایه هم تازه دارن می‌فهمن
مردم ایران از دست اینها چی میکشن</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5916" target="_blank">📅 23:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5915">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e58e9ca73.mp4?token=WXwg1tWB5rge5UJf36NH2gCfnkBMoviNcOhSqteHrGxcA-h1Ggu6QWpzMK8_Mpa2JPU3WzYi4Nwx4i8RMUIB6wEGiycNPFx7KZebE15XnFt1AJGYBy_LnKWj2Oh5ofV7P4JR355f0zLS_Qt-WUavu-fSei75CZ4GyPOBukykdghLs-Q_CNT-kxscUEqNWufBzWac8wmEfUFfDSr4AElDndd4e1O14Yai_WevriiqveFlgQ2qYPv91wUjRI44P8gnagOjtZsSIPqwNJJI0_Q7RJpwVh38FKOlNJFHc8ZY_pqvEhbY_gosOfx70xy4xbY-E4j7asXemmJM_XdqoDTRyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e58e9ca73.mp4?token=WXwg1tWB5rge5UJf36NH2gCfnkBMoviNcOhSqteHrGxcA-h1Ggu6QWpzMK8_Mpa2JPU3WzYi4Nwx4i8RMUIB6wEGiycNPFx7KZebE15XnFt1AJGYBy_LnKWj2Oh5ofV7P4JR355f0zLS_Qt-WUavu-fSei75CZ4GyPOBukykdghLs-Q_CNT-kxscUEqNWufBzWac8wmEfUFfDSr4AElDndd4e1O14Yai_WevriiqveFlgQ2qYPv91wUjRI44P8gnagOjtZsSIPqwNJJI0_Q7RJpwVh38FKOlNJFHc8ZY_pqvEhbY_gosOfx70xy4xbY-E4j7asXemmJM_XdqoDTRyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نحوه حمل جنازه خامنه‌ای</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5915" target="_blank">📅 23:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5914">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">فرهمند عليپور Farahmand Alipour
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/farahmand_alipour/5914" target="_blank">📅 23:12 · 16 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
