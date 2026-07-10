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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-20 03:21:07</div>
<hr>

<div class="tg-post" id="msg-6022">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T6fj-XikOE_vV6gn_Bc8O6-xIM4wgXc4YypxLCBQshzeZI2ex4bJps45gE5IffGwgyOcFmOIBXpQ5LzCUMaN_tBTveENWfWCKP8xENhazzUOnaFAp2M-41EK7Ymex4ZhS70FmJAmyGgh9BYHdlF6czYGHLcTQPXfB5Pl3iD77I8DjDXJa0sUIEh6zuEi1VR39aXBilQoalJgeV9tVniQdu1Klpw0ZHKxsgfSfFTz0JXsGf25mcyADsfQjrHKuvlh0iIPGCR6LoO9Jd48T7nKZvec_4o_-CsQq9qSzSvN6_jHrdi6Ysi5U9_kDIWzg08jSHPScvB1Yh7KR2t3-wfS7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه رسمی وزارت خارجه آمریکا</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/farahmand_alipour/6022" target="_blank">📅 01:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6021">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">دولت ترامپ از ایران خواسته است که روز شنبه با انتشار یک بیانیه عمومی اعلام کند که
تنگه هرمز برای عبور و مرور باز است
و همچنین متعهد شود که
دیگر به سوی کشتی‌های تجاری شلیک نخواهد کرد
.
این خبر را مقام‌های آمریکایی در جریان نشست توجیهی روز جمعه با خبرنگاران اعلام کردند.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farahmand_alipour/6021" target="_blank">📅 00:36 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6020">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b03c66dc8.mp4?token=HXuHCAa6L1Kr76JfHGiOfz0dd9cSOebiy8J7TB_81UlCp7Alo6zbul_0mQioZsRVKuwv6VwxE0jLo2Y11E9t9DwAF1PE9EGnJXN5oUJXdLoJlT2-5DHVXRUf7yfsWbCbL5Ix5jYm4sHqthZkQdWfTeYuprh06IQz9iCv52Z1AmAzPb_oMS773GoNzzyK-FoWmcSWXtb43AM8D-HXySDFG8r6lCMRhBieb-hA2jVb_gxgqx7uc-rvn7LoBtMdji1bNpZNWmV94o_r9ZSFuiD6xOLvrLE2eii2pd2NmHQdeSzE2PHr6_gUJ5KNraofyBdhRgEhIYsVdBMK8kwNoKSPAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b03c66dc8.mp4?token=HXuHCAa6L1Kr76JfHGiOfz0dd9cSOebiy8J7TB_81UlCp7Alo6zbul_0mQioZsRVKuwv6VwxE0jLo2Y11E9t9DwAF1PE9EGnJXN5oUJXdLoJlT2-5DHVXRUf7yfsWbCbL5Ix5jYm4sHqthZkQdWfTeYuprh06IQz9iCv52Z1AmAzPb_oMS773GoNzzyK-FoWmcSWXtb43AM8D-HXySDFG8r6lCMRhBieb-hA2jVb_gxgqx7uc-rvn7LoBtMdji1bNpZNWmV94o_r9ZSFuiD6xOLvrLE2eii2pd2NmHQdeSzE2PHr6_gUJ5KNraofyBdhRgEhIYsVdBMK8kwNoKSPAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی‌ خمینی، از اعضای تندروی خانواده خمینی:  مذاکره به قصد صلح با آمریکا خیانت است.  هر کس پیام دوستی برای آمریکا بفرستد دهانش نجس است.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/6020" target="_blank">📅 23:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6019">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">علی‌ خمینی، از اعضای تندروی خانواده خمینی:
مذاکره به قصد صلح با آمریکا خیانت است.  هر کس پیام دوستی برای آمریکا بفرستد دهانش نجس است.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/6019" target="_blank">📅 23:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6018">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lbIJyOE2Zg99a7z3TD5mDWj0vjc1vH4vH6eeDCZB033bHtcto7zbvY8OM41MekdSJL9DlcS9mLECr4XoRiKdft09qQFx0vnI8Uf4DSB9UJ5SLtKNYr4kzEbFsDroDdylLGJ1uLB_MRRgKpUuLhaWn329PoFDM2Mf7VIe_Vfs2tbR3FlpSShbyJ6hYHVPN45B959Ufyq7LeVRhGgU4i9RBjDSuvUrTRx3kAfK39tQMR-B3y8NO69Z17tPQoOft3RC91injyqPAcnU69MuP_c5i290F9K3QcyL0s-jszxBquiXLylYWfTy2J4tucAQBOGLSqhVQS5QAUus7_jHfnFPmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علویه، خواهر بزرگش (ناتنی)  در سال ۱۳۹۳ در سن ۸۹ سالگی درگذشت.  ۳ سال قبلش، در ۱۳۹۰  علم‌الهدای معروف مشهد در یک سخنرانی گفت که زن حاج شیخ عباسعلی
😅
می‌دونید که علم الهدی اسم زنان رو نمیبره حتی اسم زنش رو روی قبرش هم ننوشت! (ببینید حاکمان ما کیا هستن!)  خلاصه…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6018" target="_blank">📅 20:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6017">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CBCdTL9seDcNwGsIb89YYMmUWZ75YhupG5WpItG-REVUvZfiD6KHiROnXkLn4fzdNEvQCBsplLIerYuH0UMUBEtMsezM3MC7ZKK7Py0YFkm2H0O6mZei_Fnzbygt7tAnrp_QgM6h59w8uxsGJIyNVQN0aLBYMYZwuWWVtE_nnIqjCdwrYgb8nyJ4K2r6_6FmvF1cFmuGuqTGjxgGNBAjAkenwQxu9CHL-SNdywTVANS_otcnr7RB-hd3qv4e8yGeMKp9oah80UsGtFRxbWjhdqYY3e5LcKoObVpckCAzAsFgLiWr1fFP9YOF9Blgz6KLpZDuv4UTBUShsOAstb-pww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواد، پدر علی خامنه‌ای،  پیش از ازدواج با خدیجه (مادر علی خامنه‌ای)  یک ازدواج دیگه هم داشت و سه تا دختر داشت.  از خدیجه (مادر علی خامنه‌ای) هم ۴ پسر و یک دختر داشت. جمعا ۸ بچه بودند.  اون خانمی که ظاهرا خاطره ای گفت که «علی خامنه‌ای وقت به دنیا اومدن گفت…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6017" target="_blank">📅 20:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6016">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">پدر خامنه‌ای، در کنار زن و بچه‌‌هاش غذا نمیخورد!  خامنه‌ای می‌نویسه که پدرشون در یک‌ اتاق مجزا شام میخورد،  مادرش برای پدر آبگوشت درست می‌کرد و اون رو توی اتاقش می‌برد اما مادر و فرزندان معمولا نان و ماست، یا نان و خرما میخوردن.   «ما بچه‌ها در اتاق دیگر لحظه‌شماری…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6016" target="_blank">📅 20:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6015">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gB_jklWp-P3SyRXbm4_EDnMya7QubfMI49g1j4w_VhiPn-iZO2Evl0qL-0_yfAfFGW06qtFJ0UHnNf8VNKezps_esDctb0ISCH2P6bquT2fhd2L-LWktS049d0km2_qfc_tzlCR9l4PnCDawud2NIK3WyD1SKzbAZDNNSsI9Ag2I4XDPwulWsAhcmD5ckwtPta7cd4Q_2LgsjjzJuSBgaE4NfL6ji8a_T2wKx0RQoUsLXHxU_QD0i-XsiaHSvD88FEIKUiIeua4WC6dHLfzg3ljE_VPOoMVDG_dxu9S4sK-nc3_VHIwtLtU2D0qQOoBR2AhqMam6Ajzxy-v-rz5Knw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای و مادرش - تابستان ۶۰   علی خامنه‌ای از سوی دیگر، هر از گاه مجبور  به کتک کاری با همسالانش می شد که او را مسخره می‌کردند و نامش را «آشیخ خُردو» -به معنی شیخ کوچولو- گذاشته بودند.  در این تمسخر هم پدر نقش داشت که کودک خردسال را مجبور می‌کرد تا …</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6015" target="_blank">📅 20:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6014">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tFLFj6blG066qOc9Vz59KMvvnEt9kXhpJ-qtpAmFfW5ICohqG4FNQbWoELS85GqFKPesMMQ0oIfeZTJVY-UBuixdjzb57WF9FRUwO7fSY_zE_YSTtvWkrwiIUm2vO2p_7aXcYiUh9MxrcFc9j22DyifsmU4IGvvMZCwovXGmVQUWCILGwMwwid2CfDJ8gyH-a898QpObWojN6z8_9nSXZslXvmd3cLOi3Mv1Tyvs1VE5qQFTsUJnUtIgorLz8krnFxK_6LS-3AeLXwgACCRvbgX0dymYpAbeS0kksqNXta6BKMCcSOREawZwACz_9ToLVmNrpjPs21FyGGKWgGaYDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای در کنار برادر بزرگ‌ترش محمد خامنه‌ای  علی خامنه‌ای در خاطراتش ار جمله روایت میکند که  او و برادرش محمد،  در هنگام درس پس دادن به پدرشان  (جواد خامنه‌ای)  که «دست‌ سنگینی» داشت، مرتب کتک می‌خوردند.  علی خامنه‌ای نه تنها برای اشتباهات خود،  که به…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6014" target="_blank">📅 20:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6013">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DW3Y8wkErEwjwhOu146AJeeXna-1_Q0yQHyVoQUogvuEw84IQQWdhgrcwU80wv9tXG-1-1jTExHEOTwqgh0A15l5iYi9CWoppsIWSS_H_9MqlPO-ExhLP2LqfKuW7q3xDK4o2mdX_UoqYv7uPLz_u6ilcSEtzGMwSEIrDajTgLwW-XHDpJZvpULYX9Nmzv8qJtpy9PZuvcubBZXBTiJ92E6mS6ggwrjB_PG7OV5UKWrXZQCzHSFlIUOOE6JmN3GhWMWGj7vpEg5yt4XNt_lIBZmLVrNJDyAXQONcTbZ5wKvksbzWFVuWgRJTiWIsxnT8K7PmpZw3v0Ako2lvBbMjoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر خامنه‌ای - قبل از انقلاب   پدر خامنه‌ای فردی بسیار سخت‌گیر بود! جزو آخوندهایی بود که مخالف «برق» بود! و اجازه سیم کشی و‌برق کشی به خونه رو‌ نداد! اینه که در خاطرات خامنه‌ای اومده که از چراغ موشی استفاده می‌کردن ‌و مادرش معترض بوده که وضعشون از بقیه…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6013" target="_blank">📅 19:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6012">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ftoT0vHGzBnDY_XOgrbM999A50vu0U3HCEN_VD19MRDlKDrZhadB94T8TrzcNVRt85obQoUoJlZuJK3fO9oEmw4y29FrXCXwTbD_uGmPLdIeQCkoycDhgOUajra1PbFAt9VMcv8n_IHQ3SHNWnGxGXjVLHBUO55RjZzf5ftn_evCkOxFDKjzuTt0TUvZjEPYx3OWH9NLgMRb4TmkwxQfeP7eyvtHE6V5ul4OKgv-3bLHn9tJpWBBpZHnTHEQ2wJppZGzm0FF5ydGr_3tDiyBeExW8qgAtWyFe2c8Um8pWnXv316Y1cQGaND5plapVjmBIXdW2g2xBfNyjqXDsYpiwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر خامنه‌ای - قبل از انقلاب
پدر خامنه‌ای فردی بسیار سخت‌گیر بود!
جزو آخوندهایی بود که مخالف «برق» بود!
و اجازه سیم کشی و‌برق کشی به خونه
رو‌ نداد! اینه که در خاطرات خامنه‌ای اومده که از چراغ موشی استفاده می‌کردن ‌و مادرش معترض بوده که وضعشون از بقیه آخوندهای مشهد هم بدتره!</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6012" target="_blank">📅 19:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6011">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">اینکه خامنه‌ای گفته :« ما از زمان کودکی با پدیده مسخره کردن عمامه مواجه بودیم،  آنقدر کلمات تمسخر‌آمیز شنیدیم که این پدیده در نظر ما عادی شد.»   خمینی هم در سال ۱۳۵۸ در جمع روحانیون کُرد، دو تا خاطره تعریف کرد که روی وبسایتش هست. لینکش هم اینجاست .</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/6011" target="_blank">📅 19:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6010">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JBuHBmINNg4wiMez3F-XCUwCh4n-_2LP_GWmwRlvnv3TFyB8RtDkVdxb-Zy4nGNuP-wdA10DlFbZHZ3V7DqWPXgM6jJi_nBBZnfe_VWYMtMZVTwM3Gkw2PHhpNwx5Q94VeSu6SgJCCxIPXPNGYI1f0EMhCXR44ZpGDsZeziddZoIIatPBWIGUFywliuc8Ua_-t0R8rx1NXDW570NgtDN5LEjSln8aVO5c1ZPYPUopYboMTfzkUbascvXkreIKjppVfb7XzKleq3GoqDFwbxxxuEigMvroiMAWjN6zjiNAYNdzrFWaDGyALxHEazfkLoMoyO8bvmEuGzgrWQgGpGQCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای بارها و بارها در خاطراتش  اشاره کرده که چقدر از اینکه لباس آخوندی می‌پوشیده و مردم در زمان شاه  آخوندها رو مسخره و تحقیر میکردن در عذاب بوده.  چه در زمان کودکی که بقیه به خاطر  لباس اخوندی که می پوشیده مسخره‌‌‌اش میکردن، چه در جوانی   او در خاطراتش…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6010" target="_blank">📅 19:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6009">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NN2fLb4cazVvpoyA91J3Xw1V91yDEY7pxYNgyUboOI9fXj91j597ISmxfcEJt_qEUY4Eh2hbwuM_F02Ox3-MqLHnZHt0fMpcP6qVafcVjRFKeAdOP41tExPMPlOR_FAbVXY6TkExty-hZSS58DfVrNyIx-ONpPI0hSn5r5zYv28Xqw3YcMw0ZcKS1d4VuQfoVSoZ-MFA1AI3sWnUVmzgndyX7JEmOz13aMv_PBYicl5pkYcshx58ot7S6HWN2qSBKY87Dy_t2yYzlrpoelwlEQCVAEx7zjN-2n3Ty1JYd8r0GIG1hRHOgavx1i1nkVK_UoB7ksQccoiVrr0GUQT5Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای بارها و بارها در خاطراتش
اشاره کرده که چقدر از اینکه لباس آخوندی می‌پوشیده و مردم در زمان شاه
آخوندها رو مسخره و تحقیر میکردن
در عذاب بوده.  چه در زمان کودکی که بقیه به خاطر
لباس اخوندی که می پوشیده مسخره‌‌‌اش میکردن، چه در جوانی
او در خاطراتش می‌نویسد : «یک روحیه عمومی ایجاد شده بود که و را مورد تحقیر و استهزا قرار میداد...
ما از زمان کودکی با پدیده مسخره کردن عمامه مواجه بودیم، آن قدر کلمات تمسخرآمیز شنیدیم که این پدیده در نظر ما عادی شده بود
... هیچ معممی چه کوچک و چه بزرگ از این پدیده در امان نمانده بود.»</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6009" target="_blank">📅 19:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6006">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6006" target="_blank">📅 19:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6005">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=mDQjlTRqRN0zJeGqSL6LOwovQK7wW_eITT_cqHnlvI_cYaSgjM8iqFfZiCpHrMO0Au1zF2154iIZrnn06Hu05hQgJzHweYyyMausGGrREkheIVMemnuQ97ARaPUlE1wTfY0Sk-RFUINlz-su7NvVOvki1w3MSPN2KD8INpPBYTckOVUsNEVh7oN2UGIXgdfD_w7_6RbAXLFs8Qhc4cKc--EOrLS5vZMje4ARQxlGsZi-IAvQdYjK6mqRqWyGFm3UNv3Bcg0mdutireIPzcj1Us-N9oaKlFd3CoONXfOioQFiiCNeYvg5LblW4ZectUeZDAAYMFI-8o58J7T8vit3Q4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=mDQjlTRqRN0zJeGqSL6LOwovQK7wW_eITT_cqHnlvI_cYaSgjM8iqFfZiCpHrMO0Au1zF2154iIZrnn06Hu05hQgJzHweYyyMausGGrREkheIVMemnuQ97ARaPUlE1wTfY0Sk-RFUINlz-su7NvVOvki1w3MSPN2KD8INpPBYTckOVUsNEVh7oN2UGIXgdfD_w7_6RbAXLFs8Qhc4cKc--EOrLS5vZMje4ARQxlGsZi-IAvQdYjK6mqRqWyGFm3UNv3Bcg0mdutireIPzcj1Us-N9oaKlFd3CoONXfOioQFiiCNeYvg5LblW4ZectUeZDAAYMFI-8o58J7T8vit3Q4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا هم مسابقه طناب کشی برگزار شد</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6005" target="_blank">📅 13:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6004">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">اکسیوس به نقل از میانجی‌گران (پاکستان - قطر) : حمله جمهوری اسلامی به کشتی‌ها توسط بخشی از حکومت جمهوری اسلامی طراحی شد که مخالف تفاهم‌نامه با آمریکا بودند.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6004" target="_blank">📅 10:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6002">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/snnzMcz3inFmx6TanG6GRCd7O9p-D-ITlYAnw1PO4pKhyTt9TcHO75KRhdMUBBV3y-9h84lyQeZQ_bQEydzSFmi8B2jDyz3vaIPy-EY8vtx7mkIG6gTtgjxrlkeW6I7OX7JK56UMSD2r88bFsy_EguWzvxYwAVvYh2o0XJDKWlksI-VTqaurAUMFvbWRXI1PVjAWQ4eLDOW75Y9WmMcYtM9y6WD78p5DmtVEiZsMzRn6MJA6HQJ-Kh5qmTwvEErLU96wwVkia6sSK-_hYlFGbOfQwtghUEQFPOoiLt6NjA9vgHY7UBswCXnUmifw0ulJoeXN_rXsy1AXxJSnAI8Gow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f2581pEOawJV4mFu1HSOkfAfRRmx88xCqz9n_xBfcTZIT6BqUIwdK-sU5_zsA1F5lqeIc05FAY1PqR5RdLZN7XeSfaMtSI8rhEpb8eY_iMU9FkEv8Evfws39KOLkyAO926Lqy-jhTG3dssgp1yfEkNPMJl9-WDUG9aVRi59IDnausAglgx1DN9b5xf2Q1-6qZnZSyY5IfUDSES9TKJX-5UUDfQ83HG5dtv-6bcyiEAlnYS2HEFXPmkOYGFYJkyhenBTO-MiHCsav0ZwU1hiwiGeQm9URhdH4NoKYQpMQbUw7V8nzk_YgMxJ1qdtWaj9PeoDrm5c9d8jgdHg0DiCoHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کارشناسان و منابع رسمی شما  که این آمار و اعداد رو درآوردند، احتمالا همون‌هایی هستن که به خامنه‌ای گفتن در سراسر دنیا دارند «سلام فرمانده» رو میخونن و خودش اومد اینو گفت!  همونجایی هستن  که بهش گفته بودن  نفت آمریکا در ۲۰۲۱ تموم میشه امروزه   در ۲۰۲۶ آمریکا…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6002" target="_blank">📅 09:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6000">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6000" target="_blank">📅 09:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5999">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=qKuTfaYk5kX3pTKxI8VAA2VouOmw55mnpsNSda0nEw-KC7gQpCkt9rj3cNvJbUDno_ymPfEtyf8BvL8XQMbX7nnWn3EoNavZbpCEVmWO5d8LMdf4SaHYFWimSQM6aJ3fO7MQYOxVvAuOzY2OnvkBpPW0nkwrmw_VT1qIvJ_0_UwSkB4ld_2cIo-4D0iFo6bvNf9eyVxguwZSQPnVxRwKraiFFcZOXTYk8Rlz38Bbq1F1HqrHHIigqT3KnnbhiKLjSIXOeYatf9tZKbioMhnaxCdXkbXCO5yUrxxjtfctaaO9c5T53Er3V7XMhBVu1vnrci9klhoRGNybHaNQzad_bxf_M3bkOuM-jE11yUAJ9-qmIvMnttSXlbFghOOwfKvAINnNVpeAr-0_M-fmgS_eBAJfeim2R0P5SXTE6_gH-HuRs1v7EOwDLZa9fzbOZoFuS-Q8-EUwlFPQT9VXY5lQRPjAOaeo0o4zeDMvhtbv4Pg9mgx3slPFHZ1zTJWOq82z5J7PtC6WHRaPryeOGha4pB_49SUklw18muLievnm9GQiHKHjNkS6nJ47GwLsf7My9CaYeusmscjKUMkqzsQD4aMGcsTQm6TuNnc02WQfxx_TuUpWeWFWuwbGuswUvrhWB3-vn30NuVc2qjYtzuSd9kOysyWnbM_96Uqvrp1i5eY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=qKuTfaYk5kX3pTKxI8VAA2VouOmw55mnpsNSda0nEw-KC7gQpCkt9rj3cNvJbUDno_ymPfEtyf8BvL8XQMbX7nnWn3EoNavZbpCEVmWO5d8LMdf4SaHYFWimSQM6aJ3fO7MQYOxVvAuOzY2OnvkBpPW0nkwrmw_VT1qIvJ_0_UwSkB4ld_2cIo-4D0iFo6bvNf9eyVxguwZSQPnVxRwKraiFFcZOXTYk8Rlz38Bbq1F1HqrHHIigqT3KnnbhiKLjSIXOeYatf9tZKbioMhnaxCdXkbXCO5yUrxxjtfctaaO9c5T53Er3V7XMhBVu1vnrci9klhoRGNybHaNQzad_bxf_M3bkOuM-jE11yUAJ9-qmIvMnttSXlbFghOOwfKvAINnNVpeAr-0_M-fmgS_eBAJfeim2R0P5SXTE6_gH-HuRs1v7EOwDLZa9fzbOZoFuS-Q8-EUwlFPQT9VXY5lQRPjAOaeo0o4zeDMvhtbv4Pg9mgx3slPFHZ1zTJWOq82z5J7PtC6WHRaPryeOGha4pB_49SUklw18muLievnm9GQiHKHjNkS6nJ47GwLsf7My9CaYeusmscjKUMkqzsQD4aMGcsTQm6TuNnc02WQfxx_TuUpWeWFWuwbGuswUvrhWB3-vn30NuVc2qjYtzuSd9kOysyWnbM_96Uqvrp1i5eY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرگ بر دیکتاتور یک شعار نبود
آرزوی یک ایران بود، برای سالیان طولانی !</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5999" target="_blank">📅 09:19 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5998">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">مداحان اختصاصی خامنه‌ای،
که توی هواپیمای اختصاصی که تابوت خامنه‌ای بود، از عراق بردنشون مشهد.
نقش «مداح» چیه؟ مدح قدرت رو بگه
و بگه شما بزنید توی سرتون!
اگه یه عده از شما نپذیره بزنه توی سر خودش
هم حکومت میزنه توی سرش و سرکوبش میکنه.
اینه وضع جمهوری تباه اسلامی</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5998" target="_blank">📅 09:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5997">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5997" target="_blank">📅 09:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5996">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های حکومتی از حمله مسلحانه به بسیجی‌ها در مشهد خبر می‌دهند</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5996" target="_blank">📅 01:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5995">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">فرانسه ۲ مراکش ۰
دقیقه ۶۵ بازی
تیم فرانسه در ۵ دقیقه دو گل زد</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5995" target="_blank">📅 01:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5994">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NxBT1INx4ZbLKu3CJTP-CTWPRIcAVE3URHcODUj9Ofko1qS8ge7NGkXrFuhRQ4lkB7VJtmQQpmV-9X4tR1XNdYwEWh8ybmIULLzUyDI25d2LxK22YuKkvEVeOvmzNDIqsqwasa11WkstP_KYYQvTh5w5Taj_IvJ_O_58eur6Se7HSkh5v5ubyI7503W5Jf-v6MqPN7T4rQST_XfqndObH7LVQmqCvk6QlLaZC436jFdtXTY6WhBmmpH9lV7TvwlnOJlLjz3scPrPBJ9ftUct31DaBM-4CLiy7-pS8IlriawKk8V3LawwS8jnshYQrgH8U3X_W2upFowD_E7GvIhR-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام - فرماندهی مرکزی ایالات متحده:
‏
🚫
ادعا: رسانه‌های حکومتی ایران ادعا می‌کنند که عبور و مرور از تنگه هرمز فقط از طریق مسیرهای تعیین‌شده توسط  ایران مجاز است.
‏
✅
حقیقت: ایران تنگه هرمز را کنترل نمی‌کند. از اوایل ماه مه، نیروهای آمریکایی به تسهیل عبور موفقیت‌آمیز بیش از ۸۰۰ کشتی تجاری و ۳۸۰ میلیون بشکه نفت خام از طریق این کریدور حیاتی تجارت بین‌المللی کمک کرده‌اند.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5994" target="_blank">📅 00:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5993">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PyCk-TKvyN0SkrDj4SEo-YD4Uy8lp3rkZIHJRwMdsFrmW8Y4XnkRnE357R6Cp2z3dNTFVF2NlxTRt4oES9nHBvWCU4a8KsmR6XcFxY4BCI2s9hS--O36JPUdL5jf7f2GBt9aRIL9ByZAeImeSFMgGh19hbZ9HWToauAF_AhIxOSqF56bAZH6b1_UmrUJRSrZ7KBxHlbx5h-f_fqIxazQihra6HBm0qmP1aTVLOISKU54etTI69LDs1pSpfe6Jh5V7UWuMH6wGkXx0hte6WuA9yA3UxilvtPzv8R1IzYntpLRPV4KfU2qFXHsPDLk22EcmH1wAKBQBK52Nlu823YMgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های حکومتی از حمله مسلحانه به بسیجی‌ها در مشهد خبر می‌دهند</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5993" target="_blank">📅 00:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5992">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">فرماندار کنارک از وقوع دو انفجار در منطقه نظامی نیروی دریایی این شهرستان خبر داد و گفت:
این منطقه شامگاه پنجشنبه در دو مرحله هدف حمله جنگنده‌های دشمن قرار گرفت.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5992" target="_blank">📅 23:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5991">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">صدا و سیما : هیچ انفجاری در شهرهای بندرعباس، قشم، سیریک یا جاسک شنیده نشده است.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5991" target="_blank">📅 23:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5990">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
گزارش‌هایی از یک ترور هدفمند در اهواز.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5990" target="_blank">📅 23:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5989">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=vfOT10qcev6fW2yLBa2IHmpHM3HIQwrYVi4c85LumEoY0I9OgFM_IYBBQn901uujggbrEwsBf6mtm_a8FCNJ3_2notIZKjLXgCD_-QqrqxLpPTCzDlfrMX7rxyGpEWXGG3bYtkHTi7_iKT8ifQgsFT5oPf5XsdKsx8oL2ts4Ll0oTszGHPm_vxqUfyDAkM_HQhv9NakJoPKa-zM-3A_Jdq4CScqdrviz4WV15NQo8ETGhk4SCQQK-8ohoqKGX1C0nUxk37FVNFj5g1NssUwY88nw35Qzw99TBZgQcJsOazwoPdlAjpQ7vjyfTHtNzU7P5Elr28XOGu6WpqG6BCvuwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=vfOT10qcev6fW2yLBa2IHmpHM3HIQwrYVi4c85LumEoY0I9OgFM_IYBBQn901uujggbrEwsBf6mtm_a8FCNJ3_2notIZKjLXgCD_-QqrqxLpPTCzDlfrMX7rxyGpEWXGG3bYtkHTi7_iKT8ifQgsFT5oPf5XsdKsx8oL2ts4Ll0oTszGHPm_vxqUfyDAkM_HQhv9NakJoPKa-zM-3A_Jdq4CScqdrviz4WV15NQo8ETGhk4SCQQK-8ohoqKGX1C0nUxk37FVNFj5g1NssUwY88nw35Qzw99TBZgQcJsOazwoPdlAjpQ7vjyfTHtNzU7P5Elr28XOGu6WpqG6BCvuwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌‌های مجری شبکه سه و تهدید ترامپ</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5989" target="_blank">📅 22:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5988">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/llDfvr5-DEgo0qR5oI6bKHDYeB_QXo3lcwZGiYxh4pS9Asj8C09IerUCXB8MP6LWgF3UoMDWMSYvzYZQrWAtejpvJyykXaSrTr0HFldV28tUnOGjLZ5cAUi_ItUwIFIr8Af00j7EgCPZf5F7Gv9UAJF_gXTbdmCkQVXBD7fH1E6BJ0OujvZcRPHXB2Qu2tM-NFBJaxGCNLd42_BnPrCA-_WfzTPf2ZHUx2p7wiyMXzMoDdNpLSNZGPGXQwwBZuiPTCRcmoKQQB3B3YyX6ukfuLL0n449qWa_S-t8lGI4_l9ew0Cl5KmdpqvYKC1FuU5aw-JX92qXNUGrGUZ1_ZQQyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گمانه‌زنی ‌برخی رسانه‌ها:
حملات امشب احتمالا کار
کویت و یا بحرین است و احتمالا
حملاتی موشکی به ایران صورت گرفته.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5988" target="_blank">📅 22:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5987">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
🚨
آکسیوس و العربیه به نقل از منابع خود می گویند امریکا امشب حمله ای را به خاک ایران انجام نداده است .
ممکن است حملات توسط کشور ثالثی انجام شده باشد یا صدای شلیک موشک های ضد کشتی ایرانی به سمت اهدافی در دریا باشد .
یک مقام آمریکایی هم همین موضوع را به سی‌ان‌ان گفته.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5987" target="_blank">📅 22:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5986">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5986" target="_blank">📅 22:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5985">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5985" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5984">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_yiPTVLso4c09iv9mjOXr2kyULLS7hN00-CSmP2qxdcja-A167iTfvBlKv6VRW6_3Ptk0_Wqf-qFwkd-cFAWkydJuP56qLC3TG3huS_arqNXLq-PYVFrt0dfKlxGpIjpk7mZ6Npl6E-IoJWv2UoPl5Gu_cJRo5fUZAhxI0MF6RuO-nXcqqadPgaJCh_4D8yp4jfHfOJ73Cmo-Oa4ffaLlRg-iqxXWHQQLH4UzK7H6R0zjnlhxylo1NwIZunSz2np4SpkIX-hopGfNrOumaSW_nTdIOcMN1Dlnnys-DSvRp9kD1N-X2bhR2mrAD1zLtcj3prfaCIgzYo2nKYZD8FJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آماده سازی قبر خامنه‌ای در مشهد همزمان با حملات آمریکا به جنوب.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5984" target="_blank">📅 21:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5983">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5983" target="_blank">📅 21:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5982">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5982" target="_blank">📅 21:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5981">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‏پر از خون دو دیده پر از کینه سر…
‏شش‌ماه از کشتار دی‌ماه گذشت.
🖤</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5981" target="_blank">📅 21:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5980">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B6119fj48qvC867X3f8aweLBxx6GmWlwgxIjq28Y74upOMLxIUSy8EUYJD2lElNqU8dz-2ALYpSpcxXNobPCoWlG1O4La7lAZHV1HOXxo8-OlAAW1cxIY4UQXFc1USj_qG2vc2EhVYl57oCi05y488vxYp9_jh0d0cDRB9EqWTKd3JTk26dgdDrTp8n1_xaDUbv-cReB7BP6ZAOqeawnFla1TG7xjpnXMRjpBbvc67y__CmKgZNin9-p3RKdI_cI_0ovbSUz-AObsT8aprp9xjyg4krlLXFUAKiYM2eSlc1fiTvAGQYJAPd_y0jq5v0tVnmUhdHixWB0qgeaRcVwTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2075261040867037280?s=46</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5980" target="_blank">📅 20:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5979">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=t0eEnZglzZmmYVA5lnt3N78Zzq3bMbCUmNkeJBXGWfNb9Quk74wYI04LHdxKxn7add5S2tFFRA_UwClf1sVv-6q81Xihj1-OwIehtOKwLtL2eHxEPRevYArICeQd0z6PS9qK62SUwfnbsK3NPGmqRsTC4U4VNqU9jsATK-XCIcJQ0Yb25LHVte5CZ0Vm8YeH0JAi3vX2RdoEODB4vvElwNV4Wssdtbt07hzOX5l7-hI8x2FdIPAZQtC5Zgqu5WQF-UIx-RtZhKEDMHjPbx_JvvwMEiqw35hvLQ3f8Q3fyoZg-t3_-UDELrl0R2zjs0GozicuKceDaBlI_BC0Gb23tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=t0eEnZglzZmmYVA5lnt3N78Zzq3bMbCUmNkeJBXGWfNb9Quk74wYI04LHdxKxn7add5S2tFFRA_UwClf1sVv-6q81Xihj1-OwIehtOKwLtL2eHxEPRevYArICeQd0z6PS9qK62SUwfnbsK3NPGmqRsTC4U4VNqU9jsATK-XCIcJQ0Yb25LHVte5CZ0Vm8YeH0JAi3vX2RdoEODB4vvElwNV4Wssdtbt07hzOX5l7-hI8x2FdIPAZQtC5Zgqu5WQF-UIx-RtZhKEDMHjPbx_JvvwMEiqw35hvLQ3f8Q3fyoZg-t3_-UDELrl0R2zjs0GozicuKceDaBlI_BC0Gb23tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربها در حال آماده کردن مراکش  برای بازی امشب مقابل فرانسه  امشب چه فرانسه ببره، چه مراکش  مسلمین به خدمت پاریس خواهند رسید :)</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5979" target="_blank">📅 19:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5978">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5978" target="_blank">📅 19:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5976">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=QrCv_pScEQO54WQRaR8hDtBcB_WuFWzwGCE4PovEPfmYO9zM15txLD4ITdUWHeH_F3LuvITup9ZoV37s0F2ng8C0nE-Cg-wDjAkUnOzqUT_KdwRnzx_8J7PTqXLWJ1SmuI8O5uX5eI8hBObnK72K0zd3Iq6y4Jo77ZaFo7LXHaZWh4CJiJOrU-yGrLwVFIHNmdc-o3UeLmIfLmyYfHPrzM2VvRAYw5KwP6Eetp-gEq7rp99ko_SfkZM8Pk8cepukfLZUQGdkv6Mw55IjNvfk3b0pHIWDlMWmrUe7YMznRG4MK9A1CRmre2us3AFCgtTxbSUwYlM4XU-uZmzd0YnpjUQ3fmyXDPV99sKutYGtzb4eNW7xMZN1dhe4IMw4DhAUQ05pjQnyOTHHxzUwDckXOqW93fwylqN-V3WsEnwlrk_x6z5uuueMXcT389hiTmHUXGvpYEMx3ZxR7-aqnYWb55mNlodkow3Bo9s00BWOlS8aU1s099K7Nbsv6Owo099hE-tVVHQXvG2R6WxnPLhONrbMymZMrrj9BRjHTzUu52VHx5VqebUNl0XDlI_zyzBrjDQjnLuY-UjWwBRtAo9DHZJtjcts2_p0iOvhfU1MzGasyCQ8GsnGBtbzzX-VfsgxYZz9W_XpmiKqiyZt4rMky50_q2AZFizpnyvIwOA-Uzc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=QrCv_pScEQO54WQRaR8hDtBcB_WuFWzwGCE4PovEPfmYO9zM15txLD4ITdUWHeH_F3LuvITup9ZoV37s0F2ng8C0nE-Cg-wDjAkUnOzqUT_KdwRnzx_8J7PTqXLWJ1SmuI8O5uX5eI8hBObnK72K0zd3Iq6y4Jo77ZaFo7LXHaZWh4CJiJOrU-yGrLwVFIHNmdc-o3UeLmIfLmyYfHPrzM2VvRAYw5KwP6Eetp-gEq7rp99ko_SfkZM8Pk8cepukfLZUQGdkv6Mw55IjNvfk3b0pHIWDlMWmrUe7YMznRG4MK9A1CRmre2us3AFCgtTxbSUwYlM4XU-uZmzd0YnpjUQ3fmyXDPV99sKutYGtzb4eNW7xMZN1dhe4IMw4DhAUQ05pjQnyOTHHxzUwDckXOqW93fwylqN-V3WsEnwlrk_x6z5uuueMXcT389hiTmHUXGvpYEMx3ZxR7-aqnYWb55mNlodkow3Bo9s00BWOlS8aU1s099K7Nbsv6Owo099hE-tVVHQXvG2R6WxnPLhONrbMymZMrrj9BRjHTzUu52VHx5VqebUNl0XDlI_zyzBrjDQjnLuY-UjWwBRtAo9DHZJtjcts2_p0iOvhfU1MzGasyCQ8GsnGBtbzzX-VfsgxYZz9W_XpmiKqiyZt4rMky50_q2AZFizpnyvIwOA-Uzc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرچم روی تابوتش رو هم کندن و یکی دوبار هم تابوت رو زیر و رو کردن</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5976" target="_blank">📅 18:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5975">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sQ_by8vh9qKcrtlgU5tlBV8gXCns5LNGzyrOhFKdOMTaDKEdXZ84-46hqehxdFxP_ilvpXxBcnCaM6Ru3h4mVex7W-CSR2TjtSRB3wEn7qNH2f2keIH7a-y8P1WFJ_jTcxa0Xr3YKUw9_c-AUMkc49vTdYZ-LuMUk1SMdg4WgtirMRGhUbkPHE6xOAe0rHupwv23kiaFgmgE2yo4UMZUIHBuZMHCmtCuR5bgeRnWXQvys6vTG0Dd3kXxpJtgt8P5UA2Z1G5V9fF62POxCoj3QgstxegCnVpQ0D7NoV0sThAFLwy-viIA-9lTogTDmM3wtndFogez1kiMkg9HmRN3xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمد وحیدی که الان قدرتمندترین چهره نظامی ج‌ا است.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5975" target="_blank">📅 15:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5974">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/5974" target="_blank">📅 12:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5973">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MrDf0Qbe6xzzQyp2uGPD_ZmnRtvfFZsjPUNrJnRtvseJWvSpFXd4vMDr6FSsod2w2X98UMaI3RTL0qLDUbE8Ww4v-HK6esaFI4EWQc63Y5FZuJ0zP_08FXDArM_7IHembX_a4qpjt3Bk57rKTiUYg68XbvmJfulIa5yCZu_Q3Laq6_7rCrZKsEReH38gejj6jIpY5xEyr3d2rpOp2QSRZ8O3xrSMUjlx1riE-P0EMrxnRwx7f-q-ECJOn1kReC2GOwcWsmcIAAi6YFovdRYkiVfi_S6B_ItjXRPaVig3M42m22-Hm5xLl2_byzfRcmJy7be0hhjdFyTsGbQLClKDDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منتظریم اول
خامنه‌ای پرچم رو تحویل امام زمان بده
و نماز جمعه رو توی بیت‌المقدس برگزار کنه</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5973" target="_blank">📅 09:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5972">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">بیانیه ارتش : به اهدافی در قطر و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5972" target="_blank">📅 09:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5971">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=HeCYp-kNqau-uzr-H02SgxNMpNY87Ip76LORw8q9LSYFhcK5wfN5jHWffBA6tG6771rITxuFl2jHKoxv2n6485iKcSpBB2u7ZqPienuPLFgnleT4bZX8QPtxUX6xVWTkk2U97_--p3t7L2frUtT89yh7zbAziRwH2gLqmQm4dLm4qn7AVVo8FrVYwBq2-0CHNTEQ-hHxNZci_AezSiD-icpH_2ABad4NCqaKCgiI3Hs2K81kYwlP3PS4iABXlCCJd82wWR3aKOznAkybZO-YZSNESSCIcoykup3jF3ZQbZSKIDQGCMKCJhYpVzr4sf5RAEfYC3Oy7JYvhI_ofwRGnDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=HeCYp-kNqau-uzr-H02SgxNMpNY87Ip76LORw8q9LSYFhcK5wfN5jHWffBA6tG6771rITxuFl2jHKoxv2n6485iKcSpBB2u7ZqPienuPLFgnleT4bZX8QPtxUX6xVWTkk2U97_--p3t7L2frUtT89yh7zbAziRwH2gLqmQm4dLm4qn7AVVo8FrVYwBq2-0CHNTEQ-hHxNZci_AezSiD-icpH_2ABad4NCqaKCgiI3Hs2K81kYwlP3PS4iABXlCCJd82wWR3aKOznAkybZO-YZSNESSCIcoykup3jF3ZQbZSKIDQGCMKCJhYpVzr4sf5RAEfYC3Oy7JYvhI_ofwRGnDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میانه‌روهاشون : «بهترین حالت برای ترامپ حفظ آتش‌بسه، اما ایران نباید این‌ کار رو بکنه، باید کار دیگه بکنه»</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5971" target="_blank">📅 09:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5970">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5970" target="_blank">📅 08:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5969">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">خودشون داغووون و پلشت دو عالم! برادرانشون در عراق و یمن و افغانستان پلشت‌تر!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5969" target="_blank">📅 08:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5968">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‏استانداری خوزستان: سه کشته و چند مجروح در حمله صبح امروز ارتش آمریکا به اطراف اهواز
مشخص نشده که این حمله به کجا صورت گرفته.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5967" target="_blank">📅 07:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5966">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
سنتکام : به ۹۰ هدف حمله کردیم.
🚨
رسانه‌های اسرائیلی : با پایان آتش‌بس، جنگ در تنگه هرمز احتمالا چند روز تا چند هفته ادامه پیدا کند.
🚨
سپاه : به بحرین و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5966" target="_blank">📅 07:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5965">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
سنتکام : به ۹۰ هدف حمله کردیم.
🚨
رسانه‌های اسرائیلی : با پایان آتش‌بس، جنگ در تنگه هرمز احتمالا چند روز تا چند هفته ادامه پیدا کند.
🚨
سپاه : به بحرین و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5965" target="_blank">📅 06:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5964">
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=IS4N1FlO_eHWSizdW73y8rhEVFrPISiSpyTuJCY_0oNM7equ5oqQ68fhOeWeH3fEdRNz96ORNz9BiwclBCFY7ASBl22C8plFRMLUsU5iKQibtQmZ2zr8vqVeJ4gQsnzUlKWMH41zzKfkDPu3O3uZrYUgt8VH-dDC7cqKSNKIDN-Vo82KOnxWorteNYu56iM_MZkCsqdopn2rKMOi0PKn9A00D_af7jJsKU1cQPvxbSZeVYLdIp1tup7DEoFrzbyVBIwXImUtC_fz368wecpSdm8Hma_s_9DLLhpX6lZ1d4OfFYCWMtuAiQ16Oiqbxll19YjqKw3jLYfuhXmcGTjgNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=IS4N1FlO_eHWSizdW73y8rhEVFrPISiSpyTuJCY_0oNM7equ5oqQ68fhOeWeH3fEdRNz96ORNz9BiwclBCFY7ASBl22C8plFRMLUsU5iKQibtQmZ2zr8vqVeJ4gQsnzUlKWMH41zzKfkDPu3O3uZrYUgt8VH-dDC7cqKSNKIDN-Vo82KOnxWorteNYu56iM_MZkCsqdopn2rKMOi0PKn9A00D_af7jJsKU1cQPvxbSZeVYLdIp1tup7DEoFrzbyVBIwXImUtC_fz368wecpSdm8Hma_s_9DLLhpX6lZ1d4OfFYCWMtuAiQ16Oiqbxll19YjqKw3jLYfuhXmcGTjgNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : جمهوری اسلامی یکی بزند، ۲۰ تا می‌خورد.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5961" target="_blank">📅 06:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5960">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JtHlZHpYBzFcCk7aKxelmi9c1_Hj1HROHJ3CZuY6_7DeGPjXbohbUjhpqfagb87QORFL-Mv4mcNaAYcdB526VPPs2-g_swcyI58RW_GGubbHONIoeVqAKaZnJ2T0LCu0pbftxFbtjbhQ5aD8k3KhIcg633tjexQY7Y09_jWO3kJo4Y_YXP50ENuCvUKpFIh-eNHtAG0qsH5LOQNFWtSUW33paJbOPkHKGe0sbM1gkwbmh1ueztUV9BeJ4q4_rc9YTo6jDwZk5OzhAr-KTAGPUy6c-jsmF0RUcjpn6ZPq2T2VBzR2Wm4rHNRyQfp7zpKUACwAh1B4gRbKUBSCXg4lAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5960" target="_blank">📅 05:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5958">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=jIaKcNhmgCH6pa54dlcTqXDX5pEahcKG7RPAw5anTmMsjRMfMpVa4SFNrCRU9zewvxViGEWeuXxwisWsb5ngp9jcIrjDWVOC8GzBHWXG-FONfiHQXi1qQVle4oTdWY3ADdUD6HAvcR1L1Mo34KM60DH0UTXcHnttyJOJ4sjPrbmDsmxFhZidzObpi7ewFp3E2iNOwQ1mORYddAjbInOrCfQ8QSmspbYzPsR7rtulcAU8wXH8VgRk4Ro0wsfjDIS9crutS_Isx14fMUQcF9OLtuvaS0RJgtuVJ2B92-omH_yPGp-rQA-bOj7kobnsVm0ohZL0TncTzKcB5pacg9hGBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=jIaKcNhmgCH6pa54dlcTqXDX5pEahcKG7RPAw5anTmMsjRMfMpVa4SFNrCRU9zewvxViGEWeuXxwisWsb5ngp9jcIrjDWVOC8GzBHWXG-FONfiHQXi1qQVle4oTdWY3ADdUD6HAvcR1L1Mo34KM60DH0UTXcHnttyJOJ4sjPrbmDsmxFhZidzObpi7ewFp3E2iNOwQ1mORYddAjbInOrCfQ8QSmspbYzPsR7rtulcAU8wXH8VgRk4Ro0wsfjDIS9crutS_Isx14fMUQcF9OLtuvaS0RJgtuVJ2B92-omH_yPGp-rQA-bOj7kobnsVm0ohZL0TncTzKcB5pacg9hGBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکله و برج اسکله بهشتی در چابهار</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5958" target="_blank">📅 00:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5957">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
گزارشی از قطع برق در مناطق گسترده‌ای از بندرعباس، بوشهر و چابهار</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5957" target="_blank">📅 00:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5956">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/693dd42141.mp4?token=TIe8jX_iQM5OcIBVPTg2d6iZpUhQ3pDpRQTcByxuqQ9Di_TaTovWr4Vaet_Pcsy73j3Edug-6OG55kmhFbaFTObXMaTdjaSLFIanVDM8TL60TYbru99P9sdOP7XD1N6rr_v7OYUdup0HdDWlE20ZoRVtVJo3bABaZiqAOIjetAYMwR9Lr2A1MLvj9shNxTWvlyPDD6cpIV8adL2pneLbOJSsAf7wtdRYLOtHZkTbS2wDEt-laZvk3Ock6icoKZJra-H9sV6vJ1pldB7dm5H3ASK8VjshUfjKk6yI7x2J8k0ALGkeDF5widDYZ3LjQ223EAhYoomGisUfrVaU7wt81Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/693dd42141.mp4?token=TIe8jX_iQM5OcIBVPTg2d6iZpUhQ3pDpRQTcByxuqQ9Di_TaTovWr4Vaet_Pcsy73j3Edug-6OG55kmhFbaFTObXMaTdjaSLFIanVDM8TL60TYbru99P9sdOP7XD1N6rr_v7OYUdup0HdDWlE20ZoRVtVJo3bABaZiqAOIjetAYMwR9Lr2A1MLvj9shNxTWvlyPDD6cpIV8adL2pneLbOJSsAf7wtdRYLOtHZkTbS2wDEt-laZvk3Ock6icoKZJra-H9sV6vJ1pldB7dm5H3ASK8VjshUfjKk6yI7x2J8k0ALGkeDF5widDYZ3LjQ223EAhYoomGisUfrVaU7wt81Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش سوزی گسترده در بوشهر
🚨
کشیده شدن دامنه حملات به جاسک و ابوموسی
🚨
گزارشی از فعالیت پدافند بر فراز آسمان اصفهان</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5956" target="_blank">📅 00:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5955">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qUG6yxXhZw_9e80TcUmgsVuhYSokjbRw7rurvldxUbXDiHPSk1o3IkD6ilC63J-Ijgc9dYc2MS7JSY1wUEuEQfQhdtT85llrt0oFyIqDy_gX5Daf1Gp9C72_Iq3exsjvMP9vKBHm_vk6Gc4JAV4-nPmR9EZS2Qurpd_Tz95ZrwlT8VEw_Qm7ivB5PU5INGwymJaThVke_Wv-HH9KeyO1crzfUQnYHUZxgL8a0tW_tgcdY6K4f-MDr4HZ3-bnDh5NkOrlRchEdscYhsUIGnbJ6iMiY16zWtzURzkFiHaZcsCsq4LpaoBQr0jz--QuYtgjV28ZJGxd9yJfVjQqOBAr8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت مجید موسوی، فرمانده موشکی سپاه</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5955" target="_blank">📅 00:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5954">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
گزارشی از حمله به یک پایگاه بسیج در بوشهر</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5954" target="_blank">📅 00:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5953">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e3ae34ead.mp4?token=m6sWR9nBR2u7n2xQRzPCVZwVzHegFqVVT5VnMtxse0xoOD47iDMd3d1bJTZyPOULXWMDggMhs6_52wlpZW2N6N5XN5_ijxnKvgg0bT1r9SK1vPJibCNarETdn8j_HF8mOpzk6RpBFaMRNSeAfxjJOdnoW9XFWNSfgr3Y0fVVfrtwBSLi5LppBy4bkvI3zt2q7UeaY6bRxAyiYQdzndjkWVrGIqqIFUPIcfnl_pPMJE5RmsP5o_qGn1wGBebom-Uny3WdTOfGug7MNnUKwMDPtnCLHvoLF5VnKwASiLMitUPv0m98QP8AcCvSFzGg1OxdWgVvLDANCsfwtUmOyhUDrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e3ae34ead.mp4?token=m6sWR9nBR2u7n2xQRzPCVZwVzHegFqVVT5VnMtxse0xoOD47iDMd3d1bJTZyPOULXWMDggMhs6_52wlpZW2N6N5XN5_ijxnKvgg0bT1r9SK1vPJibCNarETdn8j_HF8mOpzk6RpBFaMRNSeAfxjJOdnoW9XFWNSfgr3Y0fVVfrtwBSLi5LppBy4bkvI3zt2q7UeaY6bRxAyiYQdzndjkWVrGIqqIFUPIcfnl_pPMJE5RmsP5o_qGn1wGBebom-Uny3WdTOfGug7MNnUKwMDPtnCLHvoLF5VnKwASiLMitUPv0m98QP8AcCvSFzGg1OxdWgVvLDANCsfwtUmOyhUDrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امشب - چابهار - حملات ارتش آمریکا</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5953" target="_blank">📅 00:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5952">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMUzXU--cWKeTj2_9GffljhDo6McWfoXM_isRA0G1AI1eu9122kQg_LSjjRlGABJsoMGJ4WQdD_78GAQ7X5vCImqXAxR283RbBf1UUn9M-gN1PO6qh1wUeQkYw2B0MILEYul4NI5dIXEN7eLITkZNqabizrc04AfBuovLshvgVfgW7RCFZwYVjUjvILHmMAiLY5I6mAqDh7UMAxAVSBIa1qp7rQ9AVcg5CxlUAv1JGvDMxZoVJDn8zvbTa5o14NZO8t_WLbi03te7mky5I097sJSOrpa6GTkDS_OqCWi1qDCsR6qyswHtGwm12OyrbVpO9ClmrmJZB-YfsVVK-m4XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله به یک سیستم راداری ضد هوایی در بوشهر.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5952" target="_blank">📅 00:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5951">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">حملات به قشم و بوشهر نیز کشیده شد.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5951" target="_blank">📅 00:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5950">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‏ایرنا: صدای حدود ۱۰ انفجار در چابهار و کنارک و قطع برق قسمتی از شهر چابهار</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5950" target="_blank">📅 00:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5949">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a030961c3b.mp4?token=BfVjPK0YcDSVwFxO9QnGLdzjNgQpk8sE6dtMhvbN0fi_En8trwHnKYJBUkn6fbzinUIkWYMICBWGWny5wf_ox3u-WSEqNPooA1bpFWQwVN8GQOSEiWQifo784ceBdYT9z5X6PqVf1Oo8NOTDP9UtEsobfPe1cMBpmgfm_a_tPjuFAokQjtopcbRcat4SpdrPIOR6hU8OIbmvWwdpfrxp_AX24KfGVPr99Mw_zZBsDHl-q0xdZPbZnPi-bHqvM8kT29qZWAPoQFmCYlSNsWQEVgjAZRqy1EFRyv1tVlAfd4Esr6NZhKfYJ4vQUCDDQgArDr2l6hEacsJlphq8TOTHeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a030961c3b.mp4?token=BfVjPK0YcDSVwFxO9QnGLdzjNgQpk8sE6dtMhvbN0fi_En8trwHnKYJBUkn6fbzinUIkWYMICBWGWny5wf_ox3u-WSEqNPooA1bpFWQwVN8GQOSEiWQifo784ceBdYT9z5X6PqVf1Oo8NOTDP9UtEsobfPe1cMBpmgfm_a_tPjuFAokQjtopcbRcat4SpdrPIOR6hU8OIbmvWwdpfrxp_AX24KfGVPr99Mw_zZBsDHl-q0xdZPbZnPi-bHqvM8kT29qZWAPoQFmCYlSNsWQEVgjAZRqy1EFRyv1tVlAfd4Esr6NZhKfYJ4vQUCDDQgArDr2l6hEacsJlphq8TOTHeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از حملات امشب آمریکا به چابهار</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5949" target="_blank">📅 23:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5948">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hNuJcyMqY-dU5tkgpn2I4dun2kMN3zqBvauHojxxHfrPFgEZVQ-ErbeMckG86ZPJKw2GPTKQLu-0_i7qwFYEfdVPFsJ7VnfI9OKuXIvnCIQVKWgQsz5L6uVDshIHRq69ozwV1GzebPuLIFgAJxPVcjyqpZtuChuqhcjs8EpS9v6ZtgPFxZH7ufDJm0LD3konaeLTqcquFCnVaAI0EKdpyPlLSaeL7HQhxR93AoaxojCg8DDpU_7_R4h9Vr9xjev9vZMi3aTCsIE4VXLYUgn2PajQkdNuOPT1peP_eVvji17wcdxpE7xygiNqJsHgSy1ezuPAl3OPm4WRoLgQI3rtjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به اسرائیل اطلاع داده است که قرار است امشب حملات گسترده‌ای به ایران انجام دهد.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5948" target="_blank">📅 23:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5947">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌هایی از شروع حملات آمریکا در جنوب، حمله به مقرهای سپاه در سیریک و بندرعباس.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5947" target="_blank">📅 23:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5946">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌هایی از شروع حملات آمریکا در جنوب، حمله به مقرهای سپاه در سیریک و بندرعباس.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5946" target="_blank">📅 23:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5945">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">جی‌دی ونس که طرفدار مذاکره با ج‌ا بود:
قرار بود ما محاصره دریایی رو‌ برداریم و اونها هم‌ دست از حمله به کشتی‌ها بردارند. برای یک هفته خوب بودن ولی در ۲۴ ساعت اخیر شروع کردن به حمله به کشتی‌ها.
بهشون گفته بودیم اگه
حمله کنید به کشتی‌ها باهاتون محکم برخورد می‌کنیم. نمیخوام بگم امشب قراره باهاشون چی کار کنیم.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5945" target="_blank">📅 22:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5944">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c3530f756.mp4?token=uZr0SIbmYA-RH2YwOu-oonqZ2pB6K8efZ3yO939ScVMHfzlyQPahamtjxMO7ktoymzALtUIWWZLJmttDws8tTfy2yDSALXWeYoQuehThfBRhECPNhyzhSADYPG5b_H1tG8_QUSKc2gK9u-v-TsHns6hI2xXeu2CaaApPRKYl0tc1G3qiRlKNHI902cwJOKnAVOqXxFqI7Ee-B0_5VUCeoqeXO91ChuGaYAbcQf7rbw7Vj6eHz9JrSSEG1IG41wLHfuYd7i4j9y9qhnj0WmQTFe5ZWuzQJeT0UsZIiQM8AO7rKjRtseboBIgdazjP3bwswDnYacmPQv-IJaigii0-OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c3530f756.mp4?token=uZr0SIbmYA-RH2YwOu-oonqZ2pB6K8efZ3yO939ScVMHfzlyQPahamtjxMO7ktoymzALtUIWWZLJmttDws8tTfy2yDSALXWeYoQuehThfBRhECPNhyzhSADYPG5b_H1tG8_QUSKc2gK9u-v-TsHns6hI2xXeu2CaaApPRKYl0tc1G3qiRlKNHI902cwJOKnAVOqXxFqI7Ee-B0_5VUCeoqeXO91ChuGaYAbcQf7rbw7Vj6eHz9JrSSEG1IG41wLHfuYd7i4j9y9qhnj0WmQTFe5ZWuzQJeT0UsZIiQM8AO7rKjRtseboBIgdazjP3bwswDnYacmPQv-IJaigii0-OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe5d27edac.mp4?token=HAxQoXabwVa_RO4wkNJLG3e7rEOlQyjbcIchLsdWbLKBh4JfIL87wqmhynp8wjjqe3Nzw7oM4soQZRQTnWBFPaIukYvDwF7H2xD_CkycP696zo_1ELlUglD7aPfjFaU35hiUUKBEv_Qts62kOaFuWQdHtp9K3EAN4trW-s4GAj7-0Zb81EoFW3IsGz7wJnjNGNa7FEbyWr0PZfbNGUm_0ysWzoN33VCy7xdOsUx7PznCN9pO6sawSG6JGXlDJWUP2h33jdYSHymr5cpOmIxJpqeZXyYvTkpxzBMjl5Il-YBaVqxWY6Ht9mtnUXBBOsBTNKV-w1I6mWQ9G7TeM3ZqqoBhztftnM2HNydwhKt0VMOYE2k1AcBEiY2Nuz6IpUTFCu-e9kYhoIhahPCjubCYm4XrF81LQfb_g3cBRPBRRu7oXAEVhoWUL7_0m-CHrO7qQuDhMOISIgoi5mia6JHqSBXHy5cnmsps_BU0THYwdENr4zyxSt-xlv4o4qaCZpnCDSUX6C1RPb8qKXDPMVfOLazGklwfrEjBMwRqrtoOIEDjAxaUws3EygI1fK1HW_eIXQnYFhWkYXJOiL7Wk1x64tA77yIcAfRy2yJiM8OodN_pRWvrATEkmAsLuzI0KUIYFsx7jDsVYyU37IXVhgjeiVRadZHVVoVq31jktANyhsE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe5d27edac.mp4?token=HAxQoXabwVa_RO4wkNJLG3e7rEOlQyjbcIchLsdWbLKBh4JfIL87wqmhynp8wjjqe3Nzw7oM4soQZRQTnWBFPaIukYvDwF7H2xD_CkycP696zo_1ELlUglD7aPfjFaU35hiUUKBEv_Qts62kOaFuWQdHtp9K3EAN4trW-s4GAj7-0Zb81EoFW3IsGz7wJnjNGNa7FEbyWr0PZfbNGUm_0ysWzoN33VCy7xdOsUx7PznCN9pO6sawSG6JGXlDJWUP2h33jdYSHymr5cpOmIxJpqeZXyYvTkpxzBMjl5Il-YBaVqxWY6Ht9mtnUXBBOsBTNKV-w1I6mWQ9G7TeM3ZqqoBhztftnM2HNydwhKt0VMOYE2k1AcBEiY2Nuz6IpUTFCu-e9kYhoIhahPCjubCYm4XrF81LQfb_g3cBRPBRRu7oXAEVhoWUL7_0m-CHrO7qQuDhMOISIgoi5mia6JHqSBXHy5cnmsps_BU0THYwdENr4zyxSt-xlv4o4qaCZpnCDSUX6C1RPb8qKXDPMVfOLazGklwfrEjBMwRqrtoOIEDjAxaUws3EygI1fK1HW_eIXQnYFhWkYXJOiL7Wk1x64tA77yIcAfRy2yJiM8OodN_pRWvrATEkmAsLuzI0KUIYFsx7jDsVYyU37IXVhgjeiVRadZHVVoVq31jktANyhsE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل برگزاری مراسم رو
انگار غزه است! با بسیج کردن اینهمه ستاد و پول و ارگان‌ها و…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5943" target="_blank">📅 21:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5942">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7FhH3cFsPIxi-T9wOYVElQJk-T56RytDC93rKcCHmVmUu24oerm5y5cRMlsSUjorvxgDz_0Z9ijb3ELocylKsst4Fv6LwcMPrpgD-p3GQ_QS41IdvTFT8ldj86nt4T8feApnEMpAM9la1bgxQB8KM-QRb48lwKcRqC7E4p-uHchFV9Dyp5XTwJd8M1SZVbs7blKCQ3ScD60Z4_BZ8RTtRGiKGSfQJ3oeGgT9J_GlwaIbsNMA8ESCS8_z9r79Xf31XZ9B0Za4I7jWWXxjbW_jqgctv2c5lJcXPGEoAOuVrL4oiOckNnBcfZQ1yhSsTEsRgyPjghq8GERNaCPfIsb1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: درباره جمهوری اسلامی کارهایی انجام می‌دهیم که باید ۴۷ سال پیش انجام میشد.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5942" target="_blank">📅 20:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5941">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c3c23cc7c.mp4?token=mfRf7vqMVBKvQahxVm3LSDNFqjRbv2hfoGWP3GRfJSH2sgxD8YGukBRnqEsGwDIylIPm7ygbUacTIQRmar3_6g5rFllI3y-pDpXnAnEFS9Nicw0mF8BnnA1YVfrQ0Kp3nBJnIcCC5DcE0MbxoBut-SmnjV8CtmdyczHM5nEQT1qHJ9HcVXQUpG0FcOvRL0D2Y0tkJQ3Wx8fKAGYXJsL2poyJVq3VwAYPoxaeHj6EmGOVYi_1ExOGwFmPPdbx2FA_lkp5ESGxCxqWVIw_RQ_raZ90_kYlfm8Dc9HrU7EfQ3DC2oCSKz-ZmgeQsxLf-Pi620ISzpUdEbXBOGppEuOs3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c3c23cc7c.mp4?token=mfRf7vqMVBKvQahxVm3LSDNFqjRbv2hfoGWP3GRfJSH2sgxD8YGukBRnqEsGwDIylIPm7ygbUacTIQRmar3_6g5rFllI3y-pDpXnAnEFS9Nicw0mF8BnnA1YVfrQ0Kp3nBJnIcCC5DcE0MbxoBut-SmnjV8CtmdyczHM5nEQT1qHJ9HcVXQUpG0FcOvRL0D2Y0tkJQ3Wx8fKAGYXJsL2poyJVq3VwAYPoxaeHj6EmGOVYi_1ExOGwFmPPdbx2FA_lkp5ESGxCxqWVIw_RQ_raZ90_kYlfm8Dc9HrU7EfQ3DC2oCSKz-ZmgeQsxLf-Pi620ISzpUdEbXBOGppEuOs3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - اسکله بندر عباس
زیر حملات ارتش آمریکا</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5941" target="_blank">📅 20:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5940">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dd51af5b9.mp4?token=SttpExIqZC_8dctwW1s6Wv5S4kQow245qMGxOEcNK6D4Atj54hrG-DxuhHUbH0ivgyM0xkiIpco0N4NQWg9bRSqXBHphr-c52GtFAGBnwcUPFGTH4qIyCmDbplTNQDTIlpPK1xnVTo4lLQDHZzouEayeXyoQ9i-EDG7qfLH5oHu3q9eGMmfThVccmtBG2Xux0l-d1mmlddm7O3Fwz9IFz0exNL6uXN3BZcbvCMPQgHtSE2LK8xS6lXXL094K_I1ozTfnofV7tzSsMMFgviRy9bsWRGmGHOtgduTDjAJKuxuBvzInWxvG-ss-V0_q8zGj6CguKNrkQMdVCUAtl3vA_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dd51af5b9.mp4?token=SttpExIqZC_8dctwW1s6Wv5S4kQow245qMGxOEcNK6D4Atj54hrG-DxuhHUbH0ivgyM0xkiIpco0N4NQWg9bRSqXBHphr-c52GtFAGBnwcUPFGTH4qIyCmDbplTNQDTIlpPK1xnVTo4lLQDHZzouEayeXyoQ9i-EDG7qfLH5oHu3q9eGMmfThVccmtBG2Xux0l-d1mmlddm7O3Fwz9IFz0exNL6uXN3BZcbvCMPQgHtSE2LK8xS6lXXL094K_I1ozTfnofV7tzSsMMFgviRy9bsWRGmGHOtgduTDjAJKuxuBvzInWxvG-ss-V0_q8zGj6CguKNrkQMdVCUAtl3vA_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه مراسم برگزار کردن … ستاد برگزاری ، هزینه هنگفت، ده‌ها ارگان و ستاد زیر نظرشون.
بعد کارهاشون رو ببینید!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5940" target="_blank">📅 19:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5939">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UxqNrH3IbYewOBXCn5MELnQaXhqWfue5elDTt7B_O25wMZKBcwFlzXwwNHg666Og-JYWWJOZNAzrSUvcVQb-3QyZGXvWdMBWG_IEWQMD6ol_8lEFito2sORBDKBVhuWIHMwl5xR2GXFY81aBZrgM_m7RHzahLz1P2Eoj9f3W8eWV7EhggB81O40CKLd3Jz4eMEPvvR5dixhlj62gb1lt7_AW7fvLJAuJ4oSx3b4mgv28LAAVs2iKhu7TzlhNYjlHQWo7hGy7uWhcjkAVMZs3qprBGuLI178ugrenhb9Z1lFShxx2Y_Nh49rOsF_2u14w8De_CuFch5E-djwEpMhUOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کشته شدن ۸ نیروی ارتشی
در جریان حملات دیشب و صبح امروز آمریکا</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5939" target="_blank">📅 19:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5938">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ترامپ: اومدن خواهش کردن زمان تشییع جنازه ما رو نکش. بعد وسط این مراسم حمله کردن به سه تا کشتی.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5938" target="_blank">📅 17:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5937">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=qgNQ3DbbYXJwz0b5YGsdIrM1MumiO-qBmlMbmejhwWbEU9XKuhrex69Go267lIstr4dFn3_choGsi7UGHa8Y233XSWKmp_Jo0uJydN-y_PrddY66q4d_6FotM1ttMxoRxBMaiiTWQ7MAfm5DaAXiXDL9kMEzconmWo8Vp5TiMgiCCH7FuLLM54EWfNHdzrFqUaud9mi3qJ6u7Mtr1OJkhrH9jvKby730O5NB_6ystsjp-1HtcbqfeeS7dfmrEB7j2-okXpBV3nuT8zVuthNlNHopXwEkp-oY0Tj6Tw92YwDiCGwI1RjK08L67eBt9OQF6JCRbnag8xHIBnhTzrJBpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=qgNQ3DbbYXJwz0b5YGsdIrM1MumiO-qBmlMbmejhwWbEU9XKuhrex69Go267lIstr4dFn3_choGsi7UGHa8Y233XSWKmp_Jo0uJydN-y_PrddY66q4d_6FotM1ttMxoRxBMaiiTWQ7MAfm5DaAXiXDL9kMEzconmWo8Vp5TiMgiCCH7FuLLM54EWfNHdzrFqUaud9mi3qJ6u7Mtr1OJkhrH9jvKby730O5NB_6ystsjp-1HtcbqfeeS7dfmrEB7j2-okXpBV3nuT8zVuthNlNHopXwEkp-oY0Tj6Tw92YwDiCGwI1RjK08L67eBt9OQF6JCRbnag8xHIBnhTzrJBpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دشمن هیچ غلطی نمی‌تونه بکنه
مجری : خو اومد خود گوینده این سخن رو زد!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5937" target="_blank">📅 17:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5936">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/046bf7600e.mp4?token=QQ6Yzl_B9wdxA-imWwTv8HuJ7nvghNw7cz4EhxiAkKd3x2srh_d3bs-UY8_3DmHGf6EZ_bbeUjjnSnJyPZUXq39H2UtTtx2Azv2qsChBtnS_EkUCbvgNwovGPsUNxNgIRd04XLFeVCJ5yV-TrYRoXR3wB9wvUb0kPY-b9fS_eb5XK40T7W6JBm1dlvPANmbi32yVGaIhR0GWqbf2d75u7G6hpU--oERZLvAxqcddO-0R0sZDp2RmIqIKGL0Xz7lpRaTuAw_EMg98VNWo-ueBZJYSgyZGl0Q5_m2zDyxLzTGGT5967cgUEATtVHz79oJ7hzsT_FzN50k5uXXbXE0SXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/046bf7600e.mp4?token=QQ6Yzl_B9wdxA-imWwTv8HuJ7nvghNw7cz4EhxiAkKd3x2srh_d3bs-UY8_3DmHGf6EZ_bbeUjjnSnJyPZUXq39H2UtTtx2Azv2qsChBtnS_EkUCbvgNwovGPsUNxNgIRd04XLFeVCJ5yV-TrYRoXR3wB9wvUb0kPY-b9fS_eb5XK40T7W6JBm1dlvPANmbi32yVGaIhR0GWqbf2d75u7G6hpU--oERZLvAxqcddO-0R0sZDp2RmIqIKGL0Xz7lpRaTuAw_EMg98VNWo-ueBZJYSgyZGl0Q5_m2zDyxLzTGGT5967cgUEATtVHz79oJ7hzsT_FzN50k5uXXbXE0SXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
هگست وزیر جنگ آمریکا : همونطور که ترامپ گفت امشب احتمالا اونها رو عمیق‌تر و محکم‌تر می‌زنیم.
ترامپ : محاصره دریایی رو هم احتمالا دوباره علیه ج‌ا برقرار کنیم.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5936" target="_blank">📅 17:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5935">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aff1f3384.mp4?token=svdXkaqEjUdRgdBUty8DEnAl6fNr5YmvoJa0Xg436RPgoXJkxCAv4VhzlwgTN5JrKOSD1m_AI4cqaLKhCZe0hX32VijfEpPQgWZjDSEB_N0phlK808tlQ219915kIrgC4dUAtKve24OosQNYpqTeGahLcUYKnognI8AbRYwiJU4V0Hi7tZvEx4qQnUwQa_iDVcDPgqZhOLK2yfCWTxzmBzHNcOv9-qX78_iMQdJw5hiRcJaxodf3Ydnw4Mw_3AML9S_Ev_5bC7VzpTIdZy10S5b5puMoZgheEF2GFBxassXL5a3tFveF8MaTJGUuODx2K93gYQR_EfDTtQL6lX_KPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aff1f3384.mp4?token=svdXkaqEjUdRgdBUty8DEnAl6fNr5YmvoJa0Xg436RPgoXJkxCAv4VhzlwgTN5JrKOSD1m_AI4cqaLKhCZe0hX32VijfEpPQgWZjDSEB_N0phlK808tlQ219915kIrgC4dUAtKve24OosQNYpqTeGahLcUYKnognI8AbRYwiJU4V0Hi7tZvEx4qQnUwQa_iDVcDPgqZhOLK2yfCWTxzmBzHNcOv9-qX78_iMQdJw5hiRcJaxodf3Ydnw4Mw_3AML9S_Ev_5bC7VzpTIdZy10S5b5puMoZgheEF2GFBxassXL5a3tFveF8MaTJGUuODx2K93gYQR_EfDTtQL6lX_KPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : اونها تحت یک توافق هرگز به سلاح هسته‌ای نخواهد رسید، اما شاید بدون دستیابی به یک توافق هم به این هدف برسیم، اصلا شاید راحت‌تر هم باشه، چون اونها دروغگو و‌ شیادن.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5935" target="_blank">📅 16:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5934">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5484fca6.mp4?token=Zk4zgF-EGTYzpbFQ6B6DCifM07zUM3XAC4auYvyfnEkMmjEwoukJuZ8MWsOLTuM1RxVy74In2aM_qyihbE2zsgGDhcVPztUL6eje-XaGCF3zhSymrlx-joSAl57bcjcy62ln8DfcHaN1ToebYMg1ZBpbjupcmE92j1FlTe64-HZs7BjbplcFqIkzm04lWQJq0lEnaddQ_RcQfl9AfKM4oy5bhQ_UxPrdQv2fJg7LnBpPBjtjwsnKsoVNMZW_CMtM645gIBNeC7wL90LyWgvq7CzNV9weojU3WEY1nHig1tbIIBybX09prcEmJoGfbS8J1w0XH7LQqCz_LD_7bDj5vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5484fca6.mp4?token=Zk4zgF-EGTYzpbFQ6B6DCifM07zUM3XAC4auYvyfnEkMmjEwoukJuZ8MWsOLTuM1RxVy74In2aM_qyihbE2zsgGDhcVPztUL6eje-XaGCF3zhSymrlx-joSAl57bcjcy62ln8DfcHaN1ToebYMg1ZBpbjupcmE92j1FlTe64-HZs7BjbplcFqIkzm04lWQJq0lEnaddQ_RcQfl9AfKM4oy5bhQ_UxPrdQv2fJg7LnBpPBjtjwsnKsoVNMZW_CMtM645gIBNeC7wL90LyWgvq7CzNV9weojU3WEY1nHig1tbIIBybX09prcEmJoGfbS8J1w0XH7LQqCz_LD_7bDj5vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ساختمون همون جایی است که خامنه‌ای حامیانش رو جمع می‌کرد براشون می گفت :« کشتن بد است، اما فتنه بدتر است.» (پس معترضین رو راحت بکشید)
و اونها هم براش «حیدر حیدر کنان» می‌خوندن : لب تر کند امروز سحر قدس شریفیم!
ولی داستان یه جور دیگه شد</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5934" target="_blank">📅 16:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5933">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=KqJ8SbhQW32HAJYrxlJcXdigC-4KWmPqYBVsz0YFWr-SMqXX_wbW2GLouG_e_2sCyk_nN8NBC8BRFB4drLP_jDf0y18ejZUjeR8ElOYpnYoL0gJ9VhrynGMhGg-kxVxY06GRlGxlKtXDVrnjIloJgSdQmFMpDMwxhRSSYgCn0Re8Ku8bII6j6otiPpcE8oRSqKGTkRIeDBl3WTkAS83fAP_7SXEznujvjtkTenPdefU2vTek_imIgtToZpoKhtNX5C7AFXMRdaVnfe3FlEQikDcb1q_ecX0Fd3pXSWsx_REqdH6U-NkbPNQaB2PvEfIEd0GC-zixvxhzZl_6PY2BSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=KqJ8SbhQW32HAJYrxlJcXdigC-4KWmPqYBVsz0YFWr-SMqXX_wbW2GLouG_e_2sCyk_nN8NBC8BRFB4drLP_jDf0y18ejZUjeR8ElOYpnYoL0gJ9VhrynGMhGg-kxVxY06GRlGxlKtXDVrnjIloJgSdQmFMpDMwxhRSSYgCn0Re8Ku8bII6j6otiPpcE8oRSqKGTkRIeDBl3WTkAS83fAP_7SXEznujvjtkTenPdefU2vTek_imIgtToZpoKhtNX5C7AFXMRdaVnfe3FlEQikDcb1q_ecX0Fd3pXSWsx_REqdH6U-NkbPNQaB2PvEfIEd0GC-zixvxhzZl_6PY2BSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ : احتمالا امشب هم اونها رو به سختی بزنیم. فقط دارم یه هشدار کوچک بهشون میدم.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5933" target="_blank">📅 16:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5931">
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BEbucKL3MZS2JweHjnvrvcZjpH-b0137RXnSAMDfp39ER9oe8gdx8uAsYnm4ZRGichf9MQ9FkdOFYFrqN45zbDvVw-yz9Cg0EoPJ4_UXDCnnxcTMxqS_chTDxkNQZs5Gdafz8awvhhoVI9PXpVngOc2LR-NsywmFisn-Zks71yCOCmoKj_5MsE8gkD-EP6BtPh-SGzLNsO80ikBhgJ0ILbzAKDwP74TXB5MNf1ND-9qMhnD9JwRHBI4q3uzjmw67sT-qrjtOW_SOqZFG-mBAfuxj-filMZlen7rJ7J5xjcYE7sfuNIf4y8-TseRDeFlX4W4LONXajZQq6OixJZ6sFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه کیهان زیر نظر خامنه‌ای در دو مطلب خواستار کشتن ترامپ شد.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5930" target="_blank">📅 15:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5929">
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BHhBDIOBV73sRptA6O7SoXQukEsNU1sEIS0TQES1mWQvY3GMWW5ez5vsXiu6C_fmmSDi_FwBtfrWXvDLuS99p_l841LRWNUrtw8zjqRCPwoUT333mwfR4H5eejcoC5ORILwQPuYZbqgimhI9gO_4CAozHwmbDmWq5O9F0Cl9p6budgfIoSs3slCp4AH_pjcebWyYZlNvjv2sQU_rFNx_00FbR4jVU23SLiILFOkk_0pCRmSzgTlGOjgkMbu8IoNruO3lrE9GgkMEz7Jg0PxkJx-s4Sx79xFc0Wy8oJ6p7JPhFHqbRzqr1qWcuH0Vt9bHzXh-1nCM3tMsVkkFRExIcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوش دولت چپگراش رو چنان بکش
که درس عبرتی بشه برای بقیه اروپا!
برو جلو! دعای خیر ما پشت سرته!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5928" target="_blank">📅 13:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5927">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">محمد اکبرزاده، ‏ معاون سیاسی نیروی دریایی سپاه، ‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.   او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.   جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5927" target="_blank">📅 11:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5926">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
دبیرکل ناتو : حملات آمریکا به جمهوری اسلامی کاملا ضروری بود.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5926" target="_blank">📅 11:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5925">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hmCSxlxG7faC6eDM-smsiORj10eO2pNVcbQX2zhLMZNkzVx-eViQ76kxfy7Nv24E8XaD2cU-cimf4cyRR3sRBPuCxDhaqs5cP3ywXwqUtVgwkTNwSBb6SGm1hbeaxSjBWMCCZ2kWuGyqBzlNeaedEGoX-WjKPwMeQPHlzRItH_hZNbhi9Z6SAISmk4Zs84vLBd_YCGQ4WLtANCVabyenigUSe6xBDcy4EmBp_VO2mMrZA6NRnhb9uKuZ5QQjWcFKnMgCbFZ3OcBqFf49YTFK0VOEltxvgy5Fpi4eE_PAysS62h9QdYuS6apjgEYiadI5ADhLsCz0cTw4bGJhbt0p_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بندرعباس - پس از حمله آمریکا</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5925" target="_blank">📅 11:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5924">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">پذیرایی گرم از عراقچی این بار در عراق</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5924" target="_blank">📅 08:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5923">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
سپاه : به ۸۵ هدف مرتبط با آمریکا حمله کردیم.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5923" target="_blank">📅 07:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5922">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aada56b9e2.mp4?token=eEKI4uORybkkUT1ISEZS60JoK3VMssXwC3say2sP1abER_rlubCScjAHQcsBVDB9vK1RFwQ1b3dH4CaKwERAHgY5_BvU2W4yA3D1LMelmDPwFz9dStpOTPCOh8ByAsTAbTjczPmtuSfe3hoFdf4Yi8uPCcPHPcSLpgsTbEM5BZmOUXZwc1JF1nhMuXLZYBQ4pk4j5UFMauSEP-_A3RFxX5tWNSQxmw8lbEB8Zow3wXcW075-qm2YvXjgMfbf2xv8twqyCpPiNR_XyTjGg1_1-qtNjFWWiMvgnAjkCDpKfeqaMF8hc7U47B0D5F9em7lloMq3yJDS-etxlPLPc4Q5CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aada56b9e2.mp4?token=eEKI4uORybkkUT1ISEZS60JoK3VMssXwC3say2sP1abER_rlubCScjAHQcsBVDB9vK1RFwQ1b3dH4CaKwERAHgY5_BvU2W4yA3D1LMelmDPwFz9dStpOTPCOh8ByAsTAbTjczPmtuSfe3hoFdf4Yi8uPCcPHPcSLpgsTbEM5BZmOUXZwc1JF1nhMuXLZYBQ4pk4j5UFMauSEP-_A3RFxX5tWNSQxmw8lbEB8Zow3wXcW075-qm2YvXjgMfbf2xv8twqyCpPiNR_XyTjGg1_1-qtNjFWWiMvgnAjkCDpKfeqaMF8hc7U47B0D5F9em7lloMq3yJDS-etxlPLPc4Q5CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بندرعباس - امش</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5922" target="_blank">📅 04:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5921">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYz9GW3gfDfvTH_Xm0ugaXJv2EQopf7bYx8x_VoIleJzOHJ7MuX_xdKBzgKtyivR2wSLkgpXe1st62Y52YgxSbZBOiYJ7_3DafxrSpeLWSbVj5357OP6EC48AbFkkdmnOidefE5uuTcf0sQa2ppo41s3DJHKJNi6ThoV4lyfmWwigruWJ-qZx_q_PqA-J-TnC2OiTATn24znTbviwlZJUa3fUMtDhgfRSa3SYdAXRGai0mldMAPG_YG-Pk6mXMmX2HTSU5DrP6vha7RLQhwmeKZJLDfv0MkJjDOkA_APQvf-z2iUirP_WNN9u-v77mzppDJ6W8_YvDLvHlWwjcTylw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارش ها از شنیده شدن حداقل ۳ انفجار در بندر عباس
تصویری که گفته می‌شود آتش گرفتن یکی از قایق های تندرو سپاه است</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5921" target="_blank">📅 01:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5920">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا: نیروهای ما آغاز یک رشته حملات قدرتمند علیه ایران را آغاز کرده‌اند.
‏حملات آمریکا در واکنش به حملات ایران علیه سه کشتی تجاری است که در حال عبور از تنگه هرمز بودند.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5920" target="_blank">📅 00:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5919">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای چند انفجار در حوالی قشم و سیریک!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5919" target="_blank">📅 00:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5918">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f02faf66.mp4?token=OA9Xh8Cmyhhwdswfg_JBfl_KbClBL6oegWtQCh9qBBrAw9eZZ8D_8p1tBuxpvrKGc3WFoWlIWg1xXUclQiRWpg89nwUyqDarp-7IKCevtPm463PU1W_HRLHtMrizdeahvcYjcy_A_c4R05GiVqzZRBaQHTwHRLo2pE5Cd5fyHAsd_XqWQJwg5gELugPhXfiGVNI9Rij0we9h2QGdof9qiPAyvQYmF1lDllGANxSMx8eX9ZHskKY9J7Lg-0_EIjKALvE1Zm2xeQ2Dsv2RjlxI3GfHPKQgH98lrM1hW-J9zyU0jBGApyRYjj8h9DTK1srH3EK4efE81WxgLV2KfhwkUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f02faf66.mp4?token=OA9Xh8Cmyhhwdswfg_JBfl_KbClBL6oegWtQCh9qBBrAw9eZZ8D_8p1tBuxpvrKGc3WFoWlIWg1xXUclQiRWpg89nwUyqDarp-7IKCevtPm463PU1W_HRLHtMrizdeahvcYjcy_A_c4R05GiVqzZRBaQHTwHRLo2pE5Cd5fyHAsd_XqWQJwg5gELugPhXfiGVNI9Rij0we9h2QGdof9qiPAyvQYmF1lDllGANxSMx8eX9ZHskKY9J7Lg-0_EIjKALvE1Zm2xeQ2Dsv2RjlxI3GfHPKQgH98lrM1hW-J9zyU0jBGApyRYjj8h9DTK1srH3EK4efE81WxgLV2KfhwkUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی این ویدئو دقت کردید یه نفر رو به کامیون جنازه خامنه‌ای وصل کردن؟ :)</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5918" target="_blank">📅 00:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5917">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JavKbCKMd-g6OjmNXD41wTS4O92zIbneUxi-8WCvQ7xVklnTO3rLbWA1Qng3LDzxAaQt6_gaxySas1eXT7Jp-W8trWGaC9x2f8r2vlXiFA6x47Vb2YXde2L3m52UBLzDA_M8UjqMm9xGisxjBgAKElSRL_inieA06BTEAMGGgJHplTo5xyi08hYauCr3_AtY1nvBznzBavjEE7OjNb0bDZUoKCYuKyXnKFnMSSEM7LAbhblNmg69SQhvrxuyfeHKtAw82fOZLiSsQCnioMkmqRJ7Rid6Dq-oGVTp-BtuYwNBriZMIqvTkKg38WIxiAKl1jMK0xUEyNt11ASoQbfFeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو حقیقتا یک سکانس تاریخیه، مدلی که دارند خودروی تابوت خامنه‌ای رو اسکورت میکنن :)  دارند جنازه خامنه‌ای رو‌ از جلوی خونه‌اش رد می‌کنن، از همین هم‌ پیروزی ساخته و‌ میگه چقدر قشنگه آقا خودش اومده به دیدن.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5917" target="_blank">📅 00:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5916">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ttWmaHLDtTDd0VGqucPGLI48QHUHfCf85PpZIDYOj-E3PXHX7XCU-f2AY6PR9AOjFUGE1e7ecijDVJ2ThrgqADsJDeG5slQoCfT2QPsRFtUO-c8fqlm8WJ3GKj2siGLOmaBHNqdnS7g9izPT-OAWZDdXRXRngQQbiyM1viZGahex8qJ4OE73FJ9bbGjtG5uuCXwpRuZ0ZCzXIcOhkRTGsiL7FxGHDcJSOPwtQP2GsEmdY5M89vW5vxZAQEJt4RQ5ob_BND-TdeeWo8HoNLz8ZbRGINfA--g-3Jpasu-39eOb4v1OTJLcS7Lo3SmwErm_m-xqPi-xUZxvS1VzTINLVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ما موشک میزنیم بر اساس حسن همجواریه
شما بیانیه بدید اعتراض کنید
مغایر با حسن همجواریه!
کشورهای همسایه هم تازه دارن می‌فهمن
مردم ایران از دست اینها چی میکشن</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5916" target="_blank">📅 23:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5915">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e58e9ca73.mp4?token=RbbuLqtQaFmu6Gshcq1y-yL6lYmE94s_uxZw4GfACfOmTrT5wZ8C7ld4iU0I_hQGZZjacw0vhE7RmQvgGfluITiFk34AktJ_3v0IBDGATULQeuTpgG_F6PnIUx5qxZqvnUBGWd9DPep7L1Gqnm2ZeTnue8c4rzTYC5cZuGWmDKtK0FtioS-pQtxO0Hy_ogaDv570Cj_WqwBJs99RkDimXYK24khtxT-4ktbRVAVHUBfdLOZ3196iJf_SE1ZxYVSSRczUlglA7paiDzjYveweAJZ889nwUAOiZOvGIPGnYfSp12L9ilPJ8Sxwk5dg1i9UV9n-U2kKQoWPzpqqca3zVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e58e9ca73.mp4?token=RbbuLqtQaFmu6Gshcq1y-yL6lYmE94s_uxZw4GfACfOmTrT5wZ8C7ld4iU0I_hQGZZjacw0vhE7RmQvgGfluITiFk34AktJ_3v0IBDGATULQeuTpgG_F6PnIUx5qxZqvnUBGWd9DPep7L1Gqnm2ZeTnue8c4rzTYC5cZuGWmDKtK0FtioS-pQtxO0Hy_ogaDv570Cj_WqwBJs99RkDimXYK24khtxT-4ktbRVAVHUBfdLOZ3196iJf_SE1ZxYVSSRczUlglA7paiDzjYveweAJZ889nwUAOiZOvGIPGnYfSp12L9ilPJ8Sxwk5dg1i9UV9n-U2kKQoWPzpqqca3zVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نحوه حمل جنازه خامنه‌ای</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5915" target="_blank">📅 23:26 · 16 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
