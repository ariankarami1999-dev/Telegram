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
<img src="https://cdn4.telesco.pe/file/W8DfhZD76nUEnfkiDt7yluAEmiXERInQsqgdZbDt107zZWotuRClQLcoMNJS2qCQze2MmI4f9qnGK67d0jP88Udr9MGj-vuaTc9CO0icWXIqtSBg3PZGDe7-xc-CDsnlizJqg5yBdoRMlTT1n2JeIRUwnUz8PJfGmX9yv3JnIb9dmyCgYBof2395bdBKp44k4AcsAEJ5zImMvJoKn-7aqycWd3DzyTmrcdkMwAbd7Bybq_JobIkEg0_sWowALig5P8s2yu7sujxggbRE1pX7R88ivRsAGPK_1UhNO2SuNDOU0MoXDIkhl8y1sZ-RUEiG5oRJKGHAtgDaUMxQRj69cA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.3K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-20 08:26:15</div>
<hr>

<div class="tg-post" id="msg-6024">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AHyP78d_fSmY-vAEqFik2l7ZlkGJy21Sx5I5dXjWixnIxpRpKMQdGkAI1Oq1KSAenwWGwTeB-J37Ym_eptTW1CdqlhbHYgkJxls9JRsQ6XtTkUONkJqS4JY2SPk50aB4rZOLXPUJiFVeAy3u1w6TP0mONF6NlH32w-dKUTKJRoz7VaBhNN7Z95b8cIM9PlEwtvH-zGzX4l1FtoDauqlw_SNW_Xu1nKSHmCoNkqm82SUg5FXs1X_dz-73zty4MuzmLJ-735vEf_LQIWyQ50EBzG63ad77roh1KcQEy0tAt6VCjwrdaVW1OKXmh-XXe-AltoS88ELnyqYCKtTLo7lkhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/farahmand_alipour/6024" target="_blank">📅 08:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6023">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sFoTgLRG-08-wXkVfnmUjpyU85d5MEOPeSE2RXukUJ7gcjmFTYlZCb_kpnQL7ZIcAAM_lDv_J4qZLl0hoiuQRaoKA_6j-aoodXfesfc3KLW2-ibWZjxvxqxsCsKOE-w13vSFR6YCpn74DYo1NOBBYyEvAsrIYpZHslnt5ahw7Y8rBD5zD72zEjJb8Xbr82oFCT3fbG_O9-gKukh3C2YomWyaoxAn9HMpLntkpivRZrpZ4r0DzEYp8eqAocUxAJO47HRnA1D8xjLyMZVi-YwcsKo3Qk76hvz83eeZEW9VoL3t6eBs0cX36qSbGuiRA1OhvmzravFHMOyi9dx-QJrwew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏رئیس جمهور آمریکا در «تروث سوشال»:
‏هزار موشک مسلح و آماده شلیک، جمهوری اسلامی  را نشانه گرفته‌اند و هزاران موشک دیگر نیز بلافاصله در پی خواهند آمد، اگر حکومت ایران تهدید خود را عملی کند؛ تهدیدی که در گوشه‌وکنار جهان علنی شده، مبنی بر ترور، یا تلاش برای ترور رئیس‌جمهور ‏کنونی ایالات متحده آمریکا، که در این مورد یعنی من! دستورها هم‌اکنون صادر شده است و ارتش ایالات متحده، برای یک دوره یک‌ساله با قابلیت تمدید، آماده، مایل و تواناست تا کلیه مناطق ایران را کاملاً نابود و ویران سازد — الحمدالله»</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/farahmand_alipour/6023" target="_blank">📅 07:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6022">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T6fj-XikOE_vV6gn_Bc8O6-xIM4wgXc4YypxLCBQshzeZI2ex4bJps45gE5IffGwgyOcFmOIBXpQ5LzCUMaN_tBTveENWfWCKP8xENhazzUOnaFAp2M-41EK7Ymex4ZhS70FmJAmyGgh9BYHdlF6czYGHLcTQPXfB5Pl3iD77I8DjDXJa0sUIEh6zuEi1VR39aXBilQoalJgeV9tVniQdu1Klpw0ZHKxsgfSfFTz0JXsGf25mcyADsfQjrHKuvlh0iIPGCR6LoO9Jd48T7nKZvec_4o_-CsQq9qSzSvN6_jHrdi6Ysi5U9_kDIWzg08jSHPScvB1Yh7KR2t3-wfS7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه رسمی وزارت خارجه آمریکا</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farahmand_alipour/6022" target="_blank">📅 01:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6021">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">دولت ترامپ از ایران خواسته است که روز شنبه با انتشار یک بیانیه عمومی اعلام کند که
تنگه هرمز برای عبور و مرور باز است
و همچنین متعهد شود که
دیگر به سوی کشتی‌های تجاری شلیک نخواهد کرد
.
این خبر را مقام‌های آمریکایی در جریان نشست توجیهی روز جمعه با خبرنگاران اعلام کردند.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6021" target="_blank">📅 00:36 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6020">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b03c66dc8.mp4?token=HXuHCAa6L1Kr76JfHGiOfz0dd9cSOebiy8J7TB_81UlCp7Alo6zbul_0mQioZsRVKuwv6VwxE0jLo2Y11E9t9DwAF1PE9EGnJXN5oUJXdLoJlT2-5DHVXRUf7yfsWbCbL5Ix5jYm4sHqthZkQdWfTeYuprh06IQz9iCv52Z1AmAzPb_oMS773GoNzzyK-FoWmcSWXtb43AM8D-HXySDFG8r6lCMRhBieb-hA2jVb_gxgqx7uc-rvn7LoBtMdji1bNpZNWmV94o_r9ZSFuiD6xOLvrLE2eii2pd2NmHQdeSzE2PHr6_gUJ5KNraofyBdhRgEhIYsVdBMK8kwNoKSPAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b03c66dc8.mp4?token=HXuHCAa6L1Kr76JfHGiOfz0dd9cSOebiy8J7TB_81UlCp7Alo6zbul_0mQioZsRVKuwv6VwxE0jLo2Y11E9t9DwAF1PE9EGnJXN5oUJXdLoJlT2-5DHVXRUf7yfsWbCbL5Ix5jYm4sHqthZkQdWfTeYuprh06IQz9iCv52Z1AmAzPb_oMS773GoNzzyK-FoWmcSWXtb43AM8D-HXySDFG8r6lCMRhBieb-hA2jVb_gxgqx7uc-rvn7LoBtMdji1bNpZNWmV94o_r9ZSFuiD6xOLvrLE2eii2pd2NmHQdeSzE2PHr6_gUJ5KNraofyBdhRgEhIYsVdBMK8kwNoKSPAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی‌ خمینی، از اعضای تندروی خانواده خمینی:  مذاکره به قصد صلح با آمریکا خیانت است.  هر کس پیام دوستی برای آمریکا بفرستد دهانش نجس است.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6020" target="_blank">📅 23:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6019">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">علی‌ خمینی، از اعضای تندروی خانواده خمینی:
مذاکره به قصد صلح با آمریکا خیانت است.  هر کس پیام دوستی برای آمریکا بفرستد دهانش نجس است.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6019" target="_blank">📅 23:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6018">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lbIJyOE2Zg99a7z3TD5mDWj0vjc1vH4vH6eeDCZB033bHtcto7zbvY8OM41MekdSJL9DlcS9mLECr4XoRiKdft09qQFx0vnI8Uf4DSB9UJ5SLtKNYr4kzEbFsDroDdylLGJ1uLB_MRRgKpUuLhaWn329PoFDM2Mf7VIe_Vfs2tbR3FlpSShbyJ6hYHVPN45B959Ufyq7LeVRhGgU4i9RBjDSuvUrTRx3kAfK39tQMR-B3y8NO69Z17tPQoOft3RC91injyqPAcnU69MuP_c5i290F9K3QcyL0s-jszxBquiXLylYWfTy2J4tucAQBOGLSqhVQS5QAUus7_jHfnFPmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علویه، خواهر بزرگش (ناتنی)  در سال ۱۳۹۳ در سن ۸۹ سالگی درگذشت.  ۳ سال قبلش، در ۱۳۹۰  علم‌الهدای معروف مشهد در یک سخنرانی گفت که زن حاج شیخ عباسعلی
😅
می‌دونید که علم الهدی اسم زنان رو نمیبره حتی اسم زنش رو روی قبرش هم ننوشت! (ببینید حاکمان ما کیا هستن!)  خلاصه…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6018" target="_blank">📅 20:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6017">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CBCdTL9seDcNwGsIb89YYMmUWZ75YhupG5WpItG-REVUvZfiD6KHiROnXkLn4fzdNEvQCBsplLIerYuH0UMUBEtMsezM3MC7ZKK7Py0YFkm2H0O6mZei_Fnzbygt7tAnrp_QgM6h59w8uxsGJIyNVQN0aLBYMYZwuWWVtE_nnIqjCdwrYgb8nyJ4K2r6_6FmvF1cFmuGuqTGjxgGNBAjAkenwQxu9CHL-SNdywTVANS_otcnr7RB-hd3qv4e8yGeMKp9oah80UsGtFRxbWjhdqYY3e5LcKoObVpckCAzAsFgLiWr1fFP9YOF9Blgz6KLpZDuv4UTBUShsOAstb-pww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواد، پدر علی خامنه‌ای،  پیش از ازدواج با خدیجه (مادر علی خامنه‌ای)  یک ازدواج دیگه هم داشت و سه تا دختر داشت.  از خدیجه (مادر علی خامنه‌ای) هم ۴ پسر و یک دختر داشت. جمعا ۸ بچه بودند.  اون خانمی که ظاهرا خاطره ای گفت که «علی خامنه‌ای وقت به دنیا اومدن گفت…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6017" target="_blank">📅 20:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6016">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">پدر خامنه‌ای، در کنار زن و بچه‌‌هاش غذا نمیخورد!  خامنه‌ای می‌نویسه که پدرشون در یک‌ اتاق مجزا شام میخورد،  مادرش برای پدر آبگوشت درست می‌کرد و اون رو توی اتاقش می‌برد اما مادر و فرزندان معمولا نان و ماست، یا نان و خرما میخوردن.   «ما بچه‌ها در اتاق دیگر لحظه‌شماری…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6016" target="_blank">📅 20:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6015">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gB_jklWp-P3SyRXbm4_EDnMya7QubfMI49g1j4w_VhiPn-iZO2Evl0qL-0_yfAfFGW06qtFJ0UHnNf8VNKezps_esDctb0ISCH2P6bquT2fhd2L-LWktS049d0km2_qfc_tzlCR9l4PnCDawud2NIK3WyD1SKzbAZDNNSsI9Ag2I4XDPwulWsAhcmD5ckwtPta7cd4Q_2LgsjjzJuSBgaE4NfL6ji8a_T2wKx0RQoUsLXHxU_QD0i-XsiaHSvD88FEIKUiIeua4WC6dHLfzg3ljE_VPOoMVDG_dxu9S4sK-nc3_VHIwtLtU2D0qQOoBR2AhqMam6Ajzxy-v-rz5Knw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای و مادرش - تابستان ۶۰   علی خامنه‌ای از سوی دیگر، هر از گاه مجبور  به کتک کاری با همسالانش می شد که او را مسخره می‌کردند و نامش را «آشیخ خُردو» -به معنی شیخ کوچولو- گذاشته بودند.  در این تمسخر هم پدر نقش داشت که کودک خردسال را مجبور می‌کرد تا …</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6015" target="_blank">📅 20:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6014">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tFLFj6blG066qOc9Vz59KMvvnEt9kXhpJ-qtpAmFfW5ICohqG4FNQbWoELS85GqFKPesMMQ0oIfeZTJVY-UBuixdjzb57WF9FRUwO7fSY_zE_YSTtvWkrwiIUm2vO2p_7aXcYiUh9MxrcFc9j22DyifsmU4IGvvMZCwovXGmVQUWCILGwMwwid2CfDJ8gyH-a898QpObWojN6z8_9nSXZslXvmd3cLOi3Mv1Tyvs1VE5qQFTsUJnUtIgorLz8krnFxK_6LS-3AeLXwgACCRvbgX0dymYpAbeS0kksqNXta6BKMCcSOREawZwACz_9ToLVmNrpjPs21FyGGKWgGaYDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای در کنار برادر بزرگ‌ترش محمد خامنه‌ای  علی خامنه‌ای در خاطراتش ار جمله روایت میکند که  او و برادرش محمد،  در هنگام درس پس دادن به پدرشان  (جواد خامنه‌ای)  که «دست‌ سنگینی» داشت، مرتب کتک می‌خوردند.  علی خامنه‌ای نه تنها برای اشتباهات خود،  که به…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6014" target="_blank">📅 20:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6013">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DW3Y8wkErEwjwhOu146AJeeXna-1_Q0yQHyVoQUogvuEw84IQQWdhgrcwU80wv9tXG-1-1jTExHEOTwqgh0A15l5iYi9CWoppsIWSS_H_9MqlPO-ExhLP2LqfKuW7q3xDK4o2mdX_UoqYv7uPLz_u6ilcSEtzGMwSEIrDajTgLwW-XHDpJZvpULYX9Nmzv8qJtpy9PZuvcubBZXBTiJ92E6mS6ggwrjB_PG7OV5UKWrXZQCzHSFlIUOOE6JmN3GhWMWGj7vpEg5yt4XNt_lIBZmLVrNJDyAXQONcTbZ5wKvksbzWFVuWgRJTiWIsxnT8K7PmpZw3v0Ako2lvBbMjoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر خامنه‌ای - قبل از انقلاب   پدر خامنه‌ای فردی بسیار سخت‌گیر بود! جزو آخوندهایی بود که مخالف «برق» بود! و اجازه سیم کشی و‌برق کشی به خونه رو‌ نداد! اینه که در خاطرات خامنه‌ای اومده که از چراغ موشی استفاده می‌کردن ‌و مادرش معترض بوده که وضعشون از بقیه…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6013" target="_blank">📅 19:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6012">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ftoT0vHGzBnDY_XOgrbM999A50vu0U3HCEN_VD19MRDlKDrZhadB94T8TrzcNVRt85obQoUoJlZuJK3fO9oEmw4y29FrXCXwTbD_uGmPLdIeQCkoycDhgOUajra1PbFAt9VMcv8n_IHQ3SHNWnGxGXjVLHBUO55RjZzf5ftn_evCkOxFDKjzuTt0TUvZjEPYx3OWH9NLgMRb4TmkwxQfeP7eyvtHE6V5ul4OKgv-3bLHn9tJpWBBpZHnTHEQ2wJppZGzm0FF5ydGr_3tDiyBeExW8qgAtWyFe2c8Um8pWnXv316Y1cQGaND5plapVjmBIXdW2g2xBfNyjqXDsYpiwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر خامنه‌ای - قبل از انقلاب
پدر خامنه‌ای فردی بسیار سخت‌گیر بود!
جزو آخوندهایی بود که مخالف «برق» بود!
و اجازه سیم کشی و‌برق کشی به خونه
رو‌ نداد! اینه که در خاطرات خامنه‌ای اومده که از چراغ موشی استفاده می‌کردن ‌و مادرش معترض بوده که وضعشون از بقیه آخوندهای مشهد هم بدتره!</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6012" target="_blank">📅 19:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6011">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اینکه خامنه‌ای گفته :« ما از زمان کودکی با پدیده مسخره کردن عمامه مواجه بودیم،  آنقدر کلمات تمسخر‌آمیز شنیدیم که این پدیده در نظر ما عادی شد.»   خمینی هم در سال ۱۳۵۸ در جمع روحانیون کُرد، دو تا خاطره تعریف کرد که روی وبسایتش هست. لینکش هم اینجاست .</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6011" target="_blank">📅 19:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6010">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JBuHBmINNg4wiMez3F-XCUwCh4n-_2LP_GWmwRlvnv3TFyB8RtDkVdxb-Zy4nGNuP-wdA10DlFbZHZ3V7DqWPXgM6jJi_nBBZnfe_VWYMtMZVTwM3Gkw2PHhpNwx5Q94VeSu6SgJCCxIPXPNGYI1f0EMhCXR44ZpGDsZeziddZoIIatPBWIGUFywliuc8Ua_-t0R8rx1NXDW570NgtDN5LEjSln8aVO5c1ZPYPUopYboMTfzkUbascvXkreIKjppVfb7XzKleq3GoqDFwbxxxuEigMvroiMAWjN6zjiNAYNdzrFWaDGyALxHEazfkLoMoyO8bvmEuGzgrWQgGpGQCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای بارها و بارها در خاطراتش  اشاره کرده که چقدر از اینکه لباس آخوندی می‌پوشیده و مردم در زمان شاه  آخوندها رو مسخره و تحقیر میکردن در عذاب بوده.  چه در زمان کودکی که بقیه به خاطر  لباس اخوندی که می پوشیده مسخره‌‌‌اش میکردن، چه در جوانی   او در خاطراتش…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6010" target="_blank">📅 19:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6009">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NN2fLb4cazVvpoyA91J3Xw1V91yDEY7pxYNgyUboOI9fXj91j597ISmxfcEJt_qEUY4Eh2hbwuM_F02Ox3-MqLHnZHt0fMpcP6qVafcVjRFKeAdOP41tExPMPlOR_FAbVXY6TkExty-hZSS58DfVrNyIx-ONpPI0hSn5r5zYv28Xqw3YcMw0ZcKS1d4VuQfoVSoZ-MFA1AI3sWnUVmzgndyX7JEmOz13aMv_PBYicl5pkYcshx58ot7S6HWN2qSBKY87Dy_t2yYzlrpoelwlEQCVAEx7zjN-2n3Ty1JYd8r0GIG1hRHOgavx1i1nkVK_UoB7ksQccoiVrr0GUQT5Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای بارها و بارها در خاطراتش
اشاره کرده که چقدر از اینکه لباس آخوندی می‌پوشیده و مردم در زمان شاه
آخوندها رو مسخره و تحقیر میکردن
در عذاب بوده.  چه در زمان کودکی که بقیه به خاطر
لباس اخوندی که می پوشیده مسخره‌‌‌اش میکردن، چه در جوانی
او در خاطراتش می‌نویسد : «یک روحیه عمومی ایجاد شده بود که و را مورد تحقیر و استهزا قرار میداد...
ما از زمان کودکی با پدیده مسخره کردن عمامه مواجه بودیم، آن قدر کلمات تمسخرآمیز شنیدیم که این پدیده در نظر ما عادی شده بود
... هیچ معممی چه کوچک و چه بزرگ از این پدیده در امان نمانده بود.»</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6009" target="_blank">📅 19:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6006">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6006" target="_blank">📅 19:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6005">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=mDQjlTRqRN0zJeGqSL6LOwovQK7wW_eITT_cqHnlvI_cYaSgjM8iqFfZiCpHrMO0Au1zF2154iIZrnn06Hu05hQgJzHweYyyMausGGrREkheIVMemnuQ97ARaPUlE1wTfY0Sk-RFUINlz-su7NvVOvki1w3MSPN2KD8INpPBYTckOVUsNEVh7oN2UGIXgdfD_w7_6RbAXLFs8Qhc4cKc--EOrLS5vZMje4ARQxlGsZi-IAvQdYjK6mqRqWyGFm3UNv3Bcg0mdutireIPzcj1Us-N9oaKlFd3CoONXfOioQFiiCNeYvg5LblW4ZectUeZDAAYMFI-8o58J7T8vit3Q4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=mDQjlTRqRN0zJeGqSL6LOwovQK7wW_eITT_cqHnlvI_cYaSgjM8iqFfZiCpHrMO0Au1zF2154iIZrnn06Hu05hQgJzHweYyyMausGGrREkheIVMemnuQ97ARaPUlE1wTfY0Sk-RFUINlz-su7NvVOvki1w3MSPN2KD8INpPBYTckOVUsNEVh7oN2UGIXgdfD_w7_6RbAXLFs8Qhc4cKc--EOrLS5vZMje4ARQxlGsZi-IAvQdYjK6mqRqWyGFm3UNv3Bcg0mdutireIPzcj1Us-N9oaKlFd3CoONXfOioQFiiCNeYvg5LblW4ZectUeZDAAYMFI-8o58J7T8vit3Q4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا هم مسابقه طناب کشی برگزار شد</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6005" target="_blank">📅 13:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6004">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">اکسیوس به نقل از میانجی‌گران (پاکستان - قطر) : حمله جمهوری اسلامی به کشتی‌ها توسط بخشی از حکومت جمهوری اسلامی طراحی شد که مخالف تفاهم‌نامه با آمریکا بودند.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6004" target="_blank">📅 10:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6002">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/snnzMcz3inFmx6TanG6GRCd7O9p-D-ITlYAnw1PO4pKhyTt9TcHO75KRhdMUBBV3y-9h84lyQeZQ_bQEydzSFmi8B2jDyz3vaIPy-EY8vtx7mkIG6gTtgjxrlkeW6I7OX7JK56UMSD2r88bFsy_EguWzvxYwAVvYh2o0XJDKWlksI-VTqaurAUMFvbWRXI1PVjAWQ4eLDOW75Y9WmMcYtM9y6WD78p5DmtVEiZsMzRn6MJA6HQJ-Kh5qmTwvEErLU96wwVkia6sSK-_hYlFGbOfQwtghUEQFPOoiLt6NjA9vgHY7UBswCXnUmifw0ulJoeXN_rXsy1AXxJSnAI8Gow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f2581pEOawJV4mFu1HSOkfAfRRmx88xCqz9n_xBfcTZIT6BqUIwdK-sU5_zsA1F5lqeIc05FAY1PqR5RdLZN7XeSfaMtSI8rhEpb8eY_iMU9FkEv8Evfws39KOLkyAO926Lqy-jhTG3dssgp1yfEkNPMJl9-WDUG9aVRi59IDnausAglgx1DN9b5xf2Q1-6qZnZSyY5IfUDSES9TKJX-5UUDfQ83HG5dtv-6bcyiEAlnYS2HEFXPmkOYGFYJkyhenBTO-MiHCsav0ZwU1hiwiGeQm9URhdH4NoKYQpMQbUw7V8nzk_YgMxJ1qdtWaj9PeoDrm5c9d8jgdHg0DiCoHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کارشناسان و منابع رسمی شما  که این آمار و اعداد رو درآوردند، احتمالا همون‌هایی هستن که به خامنه‌ای گفتن در سراسر دنیا دارند «سلام فرمانده» رو میخونن و خودش اومد اینو گفت!  همونجایی هستن  که بهش گفته بودن  نفت آمریکا در ۲۰۲۱ تموم میشه امروزه   در ۲۰۲۶ آمریکا…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6002" target="_blank">📅 09:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6000">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R2naEIcL2NC_h6Fjt8sDJBD7SUb03fbu2o-Z0nrEx2xvNue8iRggYWC70qMOVVxYl86wxs39FYSHBxsIuXkXQ1VLoLwYU1vtRyBYW-Z-SyYX-PNdvdbFdOp26X1f9hB57QOkZKzD7tIzifSZOTkvJx29mVIbJhv36r70qC4JjlgeeYqGNbLzfrRWehBLGNty3Eqe2HFydwGdKPLLCaswJ9Gfs0QsaygkGUF1JDbne0Ees3ztu46L0o6FzNzqHBl_yODLEjdhAnRQH5u98Whn6mvIoKyg_k0W8fhabRSDxx5BlqbNjRix5hf7sV9bbC2SwrmxgdHuh8asSqpTWNKQzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/501e9261a0.mp4?token=PIAjzFfeC6s3zJ_k7g0EflWH6l5gRMQ-6B5wPok1d6GW-cMsfP7NasuhFI8dg5dlowTUrsjfFSaWdze9NTI5Hay8VKP3VjVqVCWLKJK7vMIXRSg2kqDQajXJnMu3Uj6jzH2cA2gJBzePgW3n8UuOvaXIc5dFSQa1x9OAJ_vHNEYb2Y90r87XEiMYDZJP2TRHOchMWcbKaVhkzvSEWgFugiFpo10ft0v3PPAue8d8mRYfKGoC28deKYXeP7TUTb54BArFCFImwZ5amn0jUgrzBJJFMFlkU3a71-RTDMe6IZ_YPT1CgvV93a-LMvTZunRVnZokZdttfAKRHrA177FqlhMNg5zy0LCRazbEWQE7m5vNjN64C1ajUU-sb7Z9BIPa6ujLQc9S46-5hZgHx_OZRc9r0UqedDQ3dYkLf4oG1CbLB0Z9KlkXOeMqUEe9CAzv34y8OTxgFykWzngaXj8NNh1cagzHEKYxzk_tc5QT06wzL5nqcG-h_5cgdVMXZAZZxfcvIKptSRNXztop5TKfJr14I0fJ9iA3Q0CsSu6G4s8fdT8m-j8Gldx3jQvyciaWAZz37sYSFWktWcN577j9fMupRN5Q2rmEyI3iy9ct_PkW6p-4la_BNFS-Guvu0-7aC8SORIAtKChgHnnLTaAX2UAMuk_5uyzFCgtlg8aHGVc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/501e9261a0.mp4?token=PIAjzFfeC6s3zJ_k7g0EflWH6l5gRMQ-6B5wPok1d6GW-cMsfP7NasuhFI8dg5dlowTUrsjfFSaWdze9NTI5Hay8VKP3VjVqVCWLKJK7vMIXRSg2kqDQajXJnMu3Uj6jzH2cA2gJBzePgW3n8UuOvaXIc5dFSQa1x9OAJ_vHNEYb2Y90r87XEiMYDZJP2TRHOchMWcbKaVhkzvSEWgFugiFpo10ft0v3PPAue8d8mRYfKGoC28deKYXeP7TUTb54BArFCFImwZ5amn0jUgrzBJJFMFlkU3a71-RTDMe6IZ_YPT1CgvV93a-LMvTZunRVnZokZdttfAKRHrA177FqlhMNg5zy0LCRazbEWQE7m5vNjN64C1ajUU-sb7Z9BIPa6ujLQc9S46-5hZgHx_OZRc9r0UqedDQ3dYkLf4oG1CbLB0Z9KlkXOeMqUEe9CAzv34y8OTxgFykWzngaXj8NNh1cagzHEKYxzk_tc5QT06wzL5nqcG-h_5cgdVMXZAZZxfcvIKptSRNXztop5TKfJr14I0fJ9iA3Q0CsSu6G4s8fdT8m-j8Gldx3jQvyciaWAZz37sYSFWktWcN577j9fMupRN5Q2rmEyI3iy9ct_PkW6p-4la_BNFS-Guvu0-7aC8SORIAtKChgHnnLTaAX2UAMuk_5uyzFCgtlg8aHGVc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6000" target="_blank">📅 09:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5999">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=kKml_K4q7jp6fn9ciTK02abP39jZNqsLUVY2vdZ2_HJcVkHuTMlZs10R7r5sTYS8_Q1fT7fWpFRbyQV2aREaQrlrZhPTXmS-oz7kiAw1q2mHxx4MeiSRlLj9mcyrm4xzkIv6NEzp_DXA-VQUd41p_kwq5JBmOgik2SxekE3celGsXeTjAxDwSc3Nnpdz5TmIOtGsRjgUe6RMmREOijg89QIzNubuM_op5ea06iPsGfmjRCFCxOPt0cN2tn84SQ9cJvsm-WBh4I9SGLoobxJRYru3R87-M3kw5WIQRbQnv196MKFWQ4QVkYcbY1MsBp2oWk55y_sMZOWW7X8gVjAfYk_RsN45HQWfTvDZoeJvgIHvHR60YWJLLc_vZBHMk4iMCbd_EhVtbVDUBZckLUQpwcgxmAzFhV00CbTdat-njt08iz8hgwhbJ6txOd6dk9d8XdLfyL2PGaJalca73dZyjITxRMBlXbQBIlkdkCLLH_-0ecKYLIsdXrGPw45aAB-sN0ilEsMTutZIZn-AqUMx1kGx05qqopOFyeZdaBaJpPu5YSaEEYx4PAeDotWGX9l7xiMyF8Z0x_oWzH_Zo9gRwoczm2RNRfBgWBhZNZp4w2SaRytCTl8QXjZNoCFafqpqxWuws5DZ7jAqun6iMUE6dueyR8BOZLakXocGD45ZigU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=kKml_K4q7jp6fn9ciTK02abP39jZNqsLUVY2vdZ2_HJcVkHuTMlZs10R7r5sTYS8_Q1fT7fWpFRbyQV2aREaQrlrZhPTXmS-oz7kiAw1q2mHxx4MeiSRlLj9mcyrm4xzkIv6NEzp_DXA-VQUd41p_kwq5JBmOgik2SxekE3celGsXeTjAxDwSc3Nnpdz5TmIOtGsRjgUe6RMmREOijg89QIzNubuM_op5ea06iPsGfmjRCFCxOPt0cN2tn84SQ9cJvsm-WBh4I9SGLoobxJRYru3R87-M3kw5WIQRbQnv196MKFWQ4QVkYcbY1MsBp2oWk55y_sMZOWW7X8gVjAfYk_RsN45HQWfTvDZoeJvgIHvHR60YWJLLc_vZBHMk4iMCbd_EhVtbVDUBZckLUQpwcgxmAzFhV00CbTdat-njt08iz8hgwhbJ6txOd6dk9d8XdLfyL2PGaJalca73dZyjITxRMBlXbQBIlkdkCLLH_-0ecKYLIsdXrGPw45aAB-sN0ilEsMTutZIZn-AqUMx1kGx05qqopOFyeZdaBaJpPu5YSaEEYx4PAeDotWGX9l7xiMyF8Z0x_oWzH_Zo9gRwoczm2RNRfBgWBhZNZp4w2SaRytCTl8QXjZNoCFafqpqxWuws5DZ7jAqun6iMUE6dueyR8BOZLakXocGD45ZigU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرگ بر دیکتاتور یک شعار نبود
آرزوی یک ایران بود، برای سالیان طولانی !</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5999" target="_blank">📅 09:19 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5998">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">مداحان اختصاصی خامنه‌ای،
که توی هواپیمای اختصاصی که تابوت خامنه‌ای بود، از عراق بردنشون مشهد.
نقش «مداح» چیه؟ مدح قدرت رو بگه
و بگه شما بزنید توی سرتون!
اگه یه عده از شما نپذیره بزنه توی سر خودش
هم حکومت میزنه توی سرش و سرکوبش میکنه.
اینه وضع جمهوری تباه اسلامی</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5998" target="_blank">📅 09:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5997">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5997" target="_blank">📅 09:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5996">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های حکومتی از حمله مسلحانه به بسیجی‌ها در مشهد خبر می‌دهند</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5996" target="_blank">📅 01:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5995">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">فرانسه ۲ مراکش ۰
دقیقه ۶۵ بازی
تیم فرانسه در ۵ دقیقه دو گل زد</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5995" target="_blank">📅 01:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5994">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NxBT1INx4ZbLKu3CJTP-CTWPRIcAVE3URHcODUj9Ofko1qS8ge7NGkXrFuhRQ4lkB7VJtmQQpmV-9X4tR1XNdYwEWh8ybmIULLzUyDI25d2LxK22YuKkvEVeOvmzNDIqsqwasa11WkstP_KYYQvTh5w5Taj_IvJ_O_58eur6Se7HSkh5v5ubyI7503W5Jf-v6MqPN7T4rQST_XfqndObH7LVQmqCvk6QlLaZC436jFdtXTY6WhBmmpH9lV7TvwlnOJlLjz3scPrPBJ9ftUct31DaBM-4CLiy7-pS8IlriawKk8V3LawwS8jnshYQrgH8U3X_W2upFowD_E7GvIhR-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام - فرماندهی مرکزی ایالات متحده:
‏
🚫
ادعا: رسانه‌های حکومتی ایران ادعا می‌کنند که عبور و مرور از تنگه هرمز فقط از طریق مسیرهای تعیین‌شده توسط  ایران مجاز است.
‏
✅
حقیقت: ایران تنگه هرمز را کنترل نمی‌کند. از اوایل ماه مه، نیروهای آمریکایی به تسهیل عبور موفقیت‌آمیز بیش از ۸۰۰ کشتی تجاری و ۳۸۰ میلیون بشکه نفت خام از طریق این کریدور حیاتی تجارت بین‌المللی کمک کرده‌اند.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5994" target="_blank">📅 00:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5993">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CqK6sJwe0K_naXOOf6V978ZViKhDli3XiEpyTTb-zD911GhgK2jijqK6G8Atdkf_SKZeqNrYWSAFMlMGVrvjnVldM4mUXeKWgcIhvqERioK4cxkL_L4DmUHskfGSrkuc7UW8Gc8wnsuFHkggGns9QqJmSOKnNjNBelE4oVMnLTYOfHQS_35xc9XcGBihrVPIafOU7bF_G-nmD-J9hPcqhIlT5DAAUwBlbAfBsxe7RQpNGCdhSTtMWJbQoKVe1qYL9bemv8j24c_tgGiv2miOOaHJHSNKACZUDR5JwAiwuH6DN4FczJ9XFOPQcZUHGoC67U6P6wBSY1WhVaO8vF4-eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های حکومتی از حمله مسلحانه به بسیجی‌ها در مشهد خبر می‌دهند</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5993" target="_blank">📅 00:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5992">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">فرماندار کنارک از وقوع دو انفجار در منطقه نظامی نیروی دریایی این شهرستان خبر داد و گفت:
این منطقه شامگاه پنجشنبه در دو مرحله هدف حمله جنگنده‌های دشمن قرار گرفت.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5992" target="_blank">📅 23:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5991">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">صدا و سیما : هیچ انفجاری در شهرهای بندرعباس، قشم، سیریک یا جاسک شنیده نشده است.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5991" target="_blank">📅 23:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5990">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
گزارش‌هایی از یک ترور هدفمند در اهواز.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5990" target="_blank">📅 23:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5989">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=vfOT10qcev6fW2yLBa2IHmpHM3HIQwrYVi4c85LumEoY0I9OgFM_IYBBQn901uujggbrEwsBf6mtm_a8FCNJ3_2notIZKjLXgCD_-QqrqxLpPTCzDlfrMX7rxyGpEWXGG3bYtkHTi7_iKT8ifQgsFT5oPf5XsdKsx8oL2ts4Ll0oTszGHPm_vxqUfyDAkM_HQhv9NakJoPKa-zM-3A_Jdq4CScqdrviz4WV15NQo8ETGhk4SCQQK-8ohoqKGX1C0nUxk37FVNFj5g1NssUwY88nw35Qzw99TBZgQcJsOazwoPdlAjpQ7vjyfTHtNzU7P5Elr28XOGu6WpqG6BCvuwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=vfOT10qcev6fW2yLBa2IHmpHM3HIQwrYVi4c85LumEoY0I9OgFM_IYBBQn901uujggbrEwsBf6mtm_a8FCNJ3_2notIZKjLXgCD_-QqrqxLpPTCzDlfrMX7rxyGpEWXGG3bYtkHTi7_iKT8ifQgsFT5oPf5XsdKsx8oL2ts4Ll0oTszGHPm_vxqUfyDAkM_HQhv9NakJoPKa-zM-3A_Jdq4CScqdrviz4WV15NQo8ETGhk4SCQQK-8ohoqKGX1C0nUxk37FVNFj5g1NssUwY88nw35Qzw99TBZgQcJsOazwoPdlAjpQ7vjyfTHtNzU7P5Elr28XOGu6WpqG6BCvuwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌‌های مجری شبکه سه و تهدید ترامپ</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5989" target="_blank">📅 22:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5988">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/llDfvr5-DEgo0qR5oI6bKHDYeB_QXo3lcwZGiYxh4pS9Asj8C09IerUCXB8MP6LWgF3UoMDWMSYvzYZQrWAtejpvJyykXaSrTr0HFldV28tUnOGjLZ5cAUi_ItUwIFIr8Af00j7EgCPZf5F7Gv9UAJF_gXTbdmCkQVXBD7fH1E6BJ0OujvZcRPHXB2Qu2tM-NFBJaxGCNLd42_BnPrCA-_WfzTPf2ZHUx2p7wiyMXzMoDdNpLSNZGPGXQwwBZuiPTCRcmoKQQB3B3YyX6ukfuLL0n449qWa_S-t8lGI4_l9ew0Cl5KmdpqvYKC1FuU5aw-JX92qXNUGrGUZ1_ZQQyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گمانه‌زنی ‌برخی رسانه‌ها:
حملات امشب احتمالا کار
کویت و یا بحرین است و احتمالا
حملاتی موشکی به ایران صورت گرفته.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5988" target="_blank">📅 22:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5987">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
🚨
آکسیوس و العربیه به نقل از منابع خود می گویند امریکا امشب حمله ای را به خاک ایران انجام نداده است .
ممکن است حملات توسط کشور ثالثی انجام شده باشد یا صدای شلیک موشک های ضد کشتی ایرانی به سمت اهدافی در دریا باشد .
یک مقام آمریکایی هم همین موضوع را به سی‌ان‌ان گفته.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5987" target="_blank">📅 22:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5986">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fffbd82aa6.mp4?token=nl31jGEgxwNscj8xLMbIaC_w3pI_9l11jd-8vmcb-9DM6ZVst0WwhmHGryeQxvjj1U4mnTJHwxpAib-MPMXkt2SO0mlHTWoIlN8JqaUtMZTWL8sITFOD6lkWzlJFb3dYI6PpoL4QnEPmQADYE3ftxifSB7A89Z_jnUdFgJhQPrpfF4FAZkm4XKK-RESFd55G1pOc2mVifr6ajHAAsWKGROKNHJp86o-7p193Z2PfFoo_svTFJXFrlDdCq98HXGd1naeCCK8qHVlMD9MulCTrgoBHN6OEaIPkM3j4er8n0-9I91Kxh4m12W6r5NJCJiFaMVsybmjUxCA1douiOh2bHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fffbd82aa6.mp4?token=nl31jGEgxwNscj8xLMbIaC_w3pI_9l11jd-8vmcb-9DM6ZVst0WwhmHGryeQxvjj1U4mnTJHwxpAib-MPMXkt2SO0mlHTWoIlN8JqaUtMZTWL8sITFOD6lkWzlJFb3dYI6PpoL4QnEPmQADYE3ftxifSB7A89Z_jnUdFgJhQPrpfF4FAZkm4XKK-RESFd55G1pOc2mVifr6ajHAAsWKGROKNHJp86o-7p193Z2PfFoo_svTFJXFrlDdCq98HXGd1naeCCK8qHVlMD9MulCTrgoBHN6OEaIPkM3j4er8n0-9I91Kxh4m12W6r5NJCJiFaMVsybmjUxCA1douiOh2bHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا در مشهد هم دعوا شد :)
چند بار زیر این تابوت دعوا شد؟
توی میکروفون به نیروی خودشون میگه خودت رو کنترل کن!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5986" target="_blank">📅 22:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5985">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5985" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5984">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i0mepONjax_zhd2q1yFKezn9fVAcNQpUSEEzZWckeACqbd6Al990Uf7ZxuJ5_orDRj4MYzT-ILwZWO_Iu4GjDru79fz_tF0KdxTxK7S3hDYRmNpF1bVbOSdPnDzORZftDPTtu2A67liSZtiSLx_XPETrc_uMwZe7BLBC64EQpXsMIoh019h68BxJvXMoEvm6aSpoU3d6c6L3JokH8Ue8lU40CHIhseDX0mcrSX_mHBZM93qJsE8osTSzVDTikVM0zcJeavkA23qw9olkKDuQkMRWR0Xs9ataPc-mqHvBoThEXETT8cT54RsdxAdZm7tT8iN-pEaqQQD5z3ZuHUEHjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آماده سازی قبر خامنه‌ای در مشهد همزمان با حملات آمریکا به جنوب.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5984" target="_blank">📅 21:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5983">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5983" target="_blank">📅 21:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5982">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5982" target="_blank">📅 21:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5981">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">‏پر از خون دو دیده پر از کینه سر…
‏شش‌ماه از کشتار دی‌ماه گذشت.
🖤</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5981" target="_blank">📅 21:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5980">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X7sk9bm45m0EltWK-WBoWp8ToMTI-mrFJF_TsaGjIZJZn3CqQ5-nOAVrBNPA96X2L4Z63UxyrdUmi2ZlItb18BWZhfAL4gW6h3kH6WAkkjUQaytmRV0f9e9vV2Uek0dHnz9XctbMkEkg_AlMzFEF5H9g8cy4pP2wjybRAlxK5judPCSK2tYOwFo018uTzakwTlyB4ujcaW08wTZPk3nmbRPcszp6r7Fz3nx0ZRmnkanyiY7B1SlTox6wt1xzsiQzjxMEQmt1NsPt1MWBbj61JO0CgfdHczugJPw3KjUCCjNxiwUQCNEBjrLUZr3_WCv8In2rhyIkcjkfj6lXNenz4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2075261040867037280?s=46</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5980" target="_blank">📅 20:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5979">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=nb1cDdfXICHv1pDRx9qHy5ub4vCI26yyv3VX9GBYC1KiNw_wK1uE-I-K2iqnMcnGiN_j5pKep1YP1Zuo9YHpqZiEaQSLZptaGk1udT-jb7w7zu3cAz_S03VrD1HQpu49AOrvxRv6yWuGTX0nPcrcok0BI1WhgxrZuN4KhTySwdiLTHsHHcuuWGtwAttbowSQuF15SLwhSOlHlbgma7ScaPfEdVaZpXICfg5kWk4fnCG-MRUrEQa6VOPxNgu-FEPR6OE4xhWWzo72rUhfyY_XtOXo23Qyrc2XIwOY-xTSAacEjtbQm2e3qWucDZ70mQtZ2iQ0mJ_If16AWpAghudADw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=nb1cDdfXICHv1pDRx9qHy5ub4vCI26yyv3VX9GBYC1KiNw_wK1uE-I-K2iqnMcnGiN_j5pKep1YP1Zuo9YHpqZiEaQSLZptaGk1udT-jb7w7zu3cAz_S03VrD1HQpu49AOrvxRv6yWuGTX0nPcrcok0BI1WhgxrZuN4KhTySwdiLTHsHHcuuWGtwAttbowSQuF15SLwhSOlHlbgma7ScaPfEdVaZpXICfg5kWk4fnCG-MRUrEQa6VOPxNgu-FEPR6OE4xhWWzo72rUhfyY_XtOXo23Qyrc2XIwOY-xTSAacEjtbQm2e3qWucDZ70mQtZ2iQ0mJ_If16AWpAghudADw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربها در حال آماده کردن مراکش  برای بازی امشب مقابل فرانسه  امشب چه فرانسه ببره، چه مراکش  مسلمین به خدمت پاریس خواهند رسید :)</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5979" target="_blank">📅 19:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5978">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=JUtgL526B6XUuDNIW9T981i0xyQSf-MghwlPNgM73ssltaxyaLZz8rSFJWblWkzszg2mTDbf3Lkq-jxc89TBC8eXeosNFYCSXROzgW-nqpH0zmrULYbCSPo8KwUNz2iHOb43dbLKyohXoEU6HPgA3rRkDi-y1JmWnNGoaqdTbyJZaV1phUh74n07jRqUrtairriTi4k_SKMD0FEXoUpmGKAvhtusZOz__9g9fosS03Y_BCdGifE5X0iCWXnyePDGz-bgn1CmGyp8G-AByQyCGSt9TfihWWwXbZV7VLkbwshxoxdSM7y84tAZvi38Q3eOWGOk_y_8Tj8187vXHSDheg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=JUtgL526B6XUuDNIW9T981i0xyQSf-MghwlPNgM73ssltaxyaLZz8rSFJWblWkzszg2mTDbf3Lkq-jxc89TBC8eXeosNFYCSXROzgW-nqpH0zmrULYbCSPo8KwUNz2iHOb43dbLKyohXoEU6HPgA3rRkDi-y1JmWnNGoaqdTbyJZaV1phUh74n07jRqUrtairriTi4k_SKMD0FEXoUpmGKAvhtusZOz__9g9fosS03Y_BCdGifE5X0iCWXnyePDGz-bgn1CmGyp8G-AByQyCGSt9TfihWWwXbZV7VLkbwshxoxdSM7y84tAZvi38Q3eOWGOk_y_8Tj8187vXHSDheg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربها در حال آماده کردن مراکش
برای بازی امشب مقابل فرانسه
امشب چه فرانسه ببره، چه مراکش
مسلمین به خدمت پاریس خواهند رسید :)</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5978" target="_blank">📅 19:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5976">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=Gf6SdN0YDWHo0kt03SHy0ymIBxBYenLAligjrMzDbgEKrdSYSBm9tfoJllelkiv9txkZljXlcvGhCxWqY--wtN-5n_AAWnjKJKvNHSkzEw-7XMm7EsChUZTplwUo7_sH2pOE2UxdwiDsSyK9q9msmgKep4MytJbPPPbHrZj-RkQXYUbytU6BwBAccVaPVFmnDX1GqVdcNIfOh253_G5FIvkdPJL3Pt78G9iExGGJPjj4vNf0qMIWxxPCvHBLPKXfYbG5pGFpB1VaBLj_RUAt9pQos6glNUKlOGIZoAYRgllHKjauiFIlJvrFwMzU0k7JezgcQ9VhHtoMVi0iVZCqqWaDvR0k7-hD016y34BlcdVq00kVGYWpIf8IOqrSLDNwqDTlIe1iMrNySolGs2s2Vkha8cV6gN2gZXjrVnpCwjGZltzCYfzI20Uy7AujPfB_DQwKjBecv7uZhv6__Jlj-hro_tVwp820RcVvH1hKo0mwtVybr5uI3fmZRLFBd4vnUNMvSehN8hBzFy2P0bZQT39Up4FcHVo5e4m5nvrfbkSsUZekbksXHann-4XPRQrHm7j9SmVig-Cgm5dJB-xY1gxtRYz8ommN5JHWoS-fIHiuTP-vF3iz1hQu9MPiqsOTynekl-MlCGJdQ56DGXY71Nu3luoA8JyWUngbMBpdxig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=Gf6SdN0YDWHo0kt03SHy0ymIBxBYenLAligjrMzDbgEKrdSYSBm9tfoJllelkiv9txkZljXlcvGhCxWqY--wtN-5n_AAWnjKJKvNHSkzEw-7XMm7EsChUZTplwUo7_sH2pOE2UxdwiDsSyK9q9msmgKep4MytJbPPPbHrZj-RkQXYUbytU6BwBAccVaPVFmnDX1GqVdcNIfOh253_G5FIvkdPJL3Pt78G9iExGGJPjj4vNf0qMIWxxPCvHBLPKXfYbG5pGFpB1VaBLj_RUAt9pQos6glNUKlOGIZoAYRgllHKjauiFIlJvrFwMzU0k7JezgcQ9VhHtoMVi0iVZCqqWaDvR0k7-hD016y34BlcdVq00kVGYWpIf8IOqrSLDNwqDTlIe1iMrNySolGs2s2Vkha8cV6gN2gZXjrVnpCwjGZltzCYfzI20Uy7AujPfB_DQwKjBecv7uZhv6__Jlj-hro_tVwp820RcVvH1hKo0mwtVybr5uI3fmZRLFBd4vnUNMvSehN8hBzFy2P0bZQT39Up4FcHVo5e4m5nvrfbkSsUZekbksXHann-4XPRQrHm7j9SmVig-Cgm5dJB-xY1gxtRYz8ommN5JHWoS-fIHiuTP-vF3iz1hQu9MPiqsOTynekl-MlCGJdQ56DGXY71Nu3luoA8JyWUngbMBpdxig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرچم روی تابوتش رو هم کندن و یکی دوبار هم تابوت رو زیر و رو کردن</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5976" target="_blank">📅 18:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5975">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2Uj2rQ6hLUXhQrpi1XiOjXFMhMnLa-KZz9RonJBNSj_chOhrHfgqMpf6COIMlM5qdH8CMt11Zp3484BK_dHmOxiol1ggzjj407X56BIgqCybpGx8bmHhQj4zH0ikrvG8OSIlriwV3qybrrDbwiwhCfkIgwDRa19D5kaN_Q0fywg58P2r88fhNeghvwcDGAW3IBVyXwPnWVlNi7rO8Dr61eEsZjAIu1WhR1ou4jWg7Ejg5dJaqFtaExfdIeuYMHZb4xO_UvrgSCMJPWHt6cj2kT6hL3nev3_6w_Uxvup1KNt0xpJddQ1lN1PeYRtKrWnKZe6e-xvMKWLaSExccUqAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمد وحیدی که الان قدرتمندترین چهره نظامی ج‌ا است.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5975" target="_blank">📅 15:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5974">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KT15TZ7t0VC3y6LxIfxk_-SfWaFX_b0YHZD8154bX5aZDRK7LLlImEvDykJRgzKmKkouxAEZwBEmudkYwjEYP7rDThQWwdiNyOKThXjMqfVMLoOlfVWwD7KLzxdJ6OZX3aDu44-E-PDaIt8bUDbRAVMQ1tK9TVfMuev9-J93pulwdbHK-gswXsgXr1k276e0rd7iekv6cnPI4OCRvs5voX3vowfvt3QkEpIl4Vs8L_kCsGOYaRnmEC6BMgT_Sh2FAEbVnsfNlLwrzIpjuupfp5lVIn1vukbKfoS6PI4a8Dg7l1bky2e1P2yNrHml93C-oXpymyGSORfEtt3Q9boyFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب با اینکه حملات متوجه شهرهای جنوبی بود، به یک پل راه‌آهن در شمال کشور حمله شد.
در ماه‌های اخیر، جمهوری اسلامی حساب ویژه‌ای روی این مسیر ارتباطی باز کرده بود، هم برای ارتباط با روسیه و هم برای ارتباط با چین.
حجم مبادلات هم ۶ برابر شده بود به ویژه پس
از اعمال محاصره دریایی توسط آمریکا.
فکر نکنم تعمیر این پل ، خیلی زمان ببره.
بیشتر یک اختلال چند روزه خواهد بود.
هدف آمریکا هم بیشتر ارسال یک پیام بود
که جنوب رو محاصره می‌کنیم و می‌تونیم مسیرهای دیگه رو هم از کار بندازیم،
اگه قرار باشه شما مسیر تنگه هرمز رو ناامن کنید.</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/5974" target="_blank">📅 12:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5973">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eix1BQfCXwwvvB1VzgyQ12G0R46Xk-yVxm584XbstBQW5LJrMppt76FJO3Fv3OVgaUttoYsaWBK4RyiCeOdZLEHxXdwsuMJVwj0F0ADpbeZe9SCPmvnzXMdcmbWLCUsc6GCIU4Op1dcNmgEtSutJYvj5jE1gcf8Zx5WDHBFgLE-OrlffLEqrZb1IQml63SdCCk9lDKjbCmr2T9cbfBOL2QdlE8auuM3c5GOnfQMdwOZlj3f45T8R5nRPTxqj08iArzNSl8R3FV50VSN8BoNpGeI48DqO-y7DhOc82OVM3o66aRO5NQimqsHmkDFAHfRYCUJfISNHvom1WSg6OJQU1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منتظریم اول
خامنه‌ای پرچم رو تحویل امام زمان بده
و نماز جمعه رو توی بیت‌المقدس برگزار کنه</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5973" target="_blank">📅 09:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5972">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">بیانیه ارتش : به اهدافی در قطر و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5972" target="_blank">📅 09:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5971">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=rKBDYxrToPOXzOSsoEwAzx1B9ZepDYM2ZESTqigQismYXfSH4NGM9kC8ed-uPDFox0YMCnN3HQZjN-NfzAj2B_-kiYAWWhpuYADrw-cX7T2wNb5zf4WIozvylllxwZwtyTZP4wonFBJJEt-GHZWMAriOgu_aQco8cIO4KcCsnLvdjZNu4wcNa-wzQkr4AX6UretxYqATr-gaks-SJ5TFLdxyYqR4EriFJM-4xc4VdCKGAGL10jrBnrrZcA_VfyY8YCa4b8x09-b4whmKlN1Sda2o6u41aZJOj9NtliLpp4huAfPwqzqGXRi2c2TMn4hDTxphotm18R79aic2J0Pm8YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=rKBDYxrToPOXzOSsoEwAzx1B9ZepDYM2ZESTqigQismYXfSH4NGM9kC8ed-uPDFox0YMCnN3HQZjN-NfzAj2B_-kiYAWWhpuYADrw-cX7T2wNb5zf4WIozvylllxwZwtyTZP4wonFBJJEt-GHZWMAriOgu_aQco8cIO4KcCsnLvdjZNu4wcNa-wzQkr4AX6UretxYqATr-gaks-SJ5TFLdxyYqR4EriFJM-4xc4VdCKGAGL10jrBnrrZcA_VfyY8YCa4b8x09-b4whmKlN1Sda2o6u41aZJOj9NtliLpp4huAfPwqzqGXRi2c2TMn4hDTxphotm18R79aic2J0Pm8YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میانه‌روهاشون : «بهترین حالت برای ترامپ حفظ آتش‌بسه، اما ایران نباید این‌ کار رو بکنه، باید کار دیگه بکنه»</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5971" target="_blank">📅 09:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5970">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=nrcFTCkQ2Sj_TEnkvwb_6Ysl6Ya4qKXJ9yk9FD8eUGimMIaSXMYPv4-xjPgvzCrzw-cnd-vd3ZY0_ParzxbI1o83lnT8KpZsoBFygmb2rfBkAF6glQ5-OPSPtVQczMOS_cDYZ8E0vmCZ0Mcd7TJkxm8rjUDVqDIpRv1BO5ORqzRTF2kQ5C4fA954X-wnWUzCw4OOkTTBNX7gydePWgYvV5MlueJvMAk6npbjpG7TludXyHYuWjN_VtfquVGQbVqkfdxduVbvBCWcAWxAsWf_I6_k5oGEozflteDrLAWH0QiFv_8DEuf9OdWnb9agsYb7HcCtyzrYgKMTfyp5Zvc5kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=nrcFTCkQ2Sj_TEnkvwb_6Ysl6Ya4qKXJ9yk9FD8eUGimMIaSXMYPv4-xjPgvzCrzw-cnd-vd3ZY0_ParzxbI1o83lnT8KpZsoBFygmb2rfBkAF6glQ5-OPSPtVQczMOS_cDYZ8E0vmCZ0Mcd7TJkxm8rjUDVqDIpRv1BO5ORqzRTF2kQ5C4fA954X-wnWUzCw4OOkTTBNX7gydePWgYvV5MlueJvMAk6npbjpG7TludXyHYuWjN_VtfquVGQbVqkfdxduVbvBCWcAWxAsWf_I6_k5oGEozflteDrLAWH0QiFv_8DEuf9OdWnb9agsYb7HcCtyzrYgKMTfyp5Zvc5kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تابوت خامنه‌ای، پهپاد وار به پنکه کوبیده شد
و موجب آسیب زدن به اموال حرم شد.
یه تشییع جنازه برگزار کردن، هر ساعتش سوژه‌ای داشت.  گویی فیلم‌نامه‌اش
رو رضا عطاران نوشته.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5970" target="_blank">📅 08:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5969">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">خودشون داغووون و پلشت دو عالم! برادرانشون در عراق و یمن و افغانستان پلشت‌تر!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5969" target="_blank">📅 08:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5968">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/736101eca8.mp4?token=D0YE5xdug6-UA2-pci_wfnk0hNFjvwSrvcRAQnNGe0j8rdqNVVr6GtkZ-g1WwQG0wpFwnoe0N8Hgal7125V3DoRxxBp9B7cRPgaLHmmY9K_wP3pfKj_ojBg-Qm4pBphyuLxfRl5ewVsvz8fjWIdl2Ih914Byl1mbQ6bhId6X5nQzeZx_etnJ_pTo0BfjhhWScU7-t-voJvDLJz5JPHE_goDaEekVMQONRwgL7BwHZmjRpyYK3sYzkcEgY926fTgQOG5vDX7kCIfJI7TiRu03cGqqYFJXSn3GhvZon6w5gyw4oYSAv--62LA8FePlMZ_-6BNToAu0yHQ9mZg-uSYWqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736101eca8.mp4?token=D0YE5xdug6-UA2-pci_wfnk0hNFjvwSrvcRAQnNGe0j8rdqNVVr6GtkZ-g1WwQG0wpFwnoe0N8Hgal7125V3DoRxxBp9B7cRPgaLHmmY9K_wP3pfKj_ojBg-Qm4pBphyuLxfRl5ewVsvz8fjWIdl2Ih914Byl1mbQ6bhId6X5nQzeZx_etnJ_pTo0BfjhhWScU7-t-voJvDLJz5JPHE_goDaEekVMQONRwgL7BwHZmjRpyYK3sYzkcEgY926fTgQOG5vDX7kCIfJI7TiRu03cGqqYFJXSn3GhvZon6w5gyw4oYSAv--62LA8FePlMZ_-6BNToAu0yHQ9mZg-uSYWqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون داغووون و پلشت دو عالم! برادرانشون در عراق و یمن و افغانستان پلشت‌تر!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5968" target="_blank">📅 08:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5967">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‏استانداری خوزستان: سه کشته و چند مجروح در حمله صبح امروز ارتش آمریکا به اطراف اهواز
مشخص نشده که این حمله به کجا صورت گرفته.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5967" target="_blank">📅 07:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5966">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
سنتکام : به ۹۰ هدف حمله کردیم.
🚨
رسانه‌های اسرائیلی : با پایان آتش‌بس، جنگ در تنگه هرمز احتمالا چند روز تا چند هفته ادامه پیدا کند.
🚨
سپاه : به بحرین و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5966" target="_blank">📅 07:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5965">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
سنتکام : به ۹۰ هدف حمله کردیم.
🚨
رسانه‌های اسرائیلی : با پایان آتش‌بس، جنگ در تنگه هرمز احتمالا چند روز تا چند هفته ادامه پیدا کند.
🚨
سپاه : به بحرین و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5965" target="_blank">📅 06:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5964">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=sswA3paas7lmPCAM3B_ZldHm93HiPjQ_rtKWMqGKT6YG34ifqZFQeT2t8ncE00ummL5RjdyvJCBARa-z0A7bTpG0TCTcoUTLk8IxW0oHFfflTUsJ-d599I2wdsBdFzOT3ZZ3t3QyIUgHV3iVHk1yuWp3u4DkuXGcv4_d4-W-GY2a1gA2os1v7Nsj5oDZSX7oPGnVwJ3NhQNhqxeHtfT679rFdxKJYtZwXBLPm-pyRjG3YtBh8TYw8LwUIVwOkZlhvMVJgrW9ep10iLjd2-fvctYa05RaK871031UQLohMw-bEujz9l9SY2D1LsAW9754e5_MiD7-cZDcttWcllStSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=sswA3paas7lmPCAM3B_ZldHm93HiPjQ_rtKWMqGKT6YG34ifqZFQeT2t8ncE00ummL5RjdyvJCBARa-z0A7bTpG0TCTcoUTLk8IxW0oHFfflTUsJ-d599I2wdsBdFzOT3ZZ3t3QyIUgHV3iVHk1yuWp3u4DkuXGcv4_d4-W-GY2a1gA2os1v7Nsj5oDZSX7oPGnVwJ3NhQNhqxeHtfT679rFdxKJYtZwXBLPm-pyRjG3YtBh8TYw8LwUIVwOkZlhvMVJgrW9ep10iLjd2-fvctYa05RaK871031UQLohMw-bEujz9l9SY2D1LsAW9754e5_MiD7-cZDcttWcllStSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏میرباقری در صداوسیما:
‏دشمن به معنای واقعی کلمه هیچ غلطی نمیتونه بکنه، بنظرتون میتونه غلطی بکنه؟
‏مجری: بله دیگه، رهبر که خودش این حرفا رو میزد رو کشتن</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5964" target="_blank">📅 06:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5962">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJqeF7V7idRUumit7ViJgwtjM7tFWq7lP-HYvxhSVU-oUHagkut2MTtw-CznlVMhXbbooW2Ea_mqyFM5AW_FgGHM8KP19NaCS_392BGASQLwLvk-rAEnCJu6iDoBZImTu43M8_XViFt9CwMP1746fqlu8bwJ8au6_ZGcnrj1djww5mZAFKaJaZQAvdjJcBYKIZdYAG9PBCOLOz4eaTRusoUo_tWvr-lW-HFg4dX5AApc9yIV15ZhXUlCjBf32Rt_Js3BvClS8KEsY_P5CZbw5KtCK-OxVZJuSi8aqwiqm3HvyT0eFahKIb0EbCUGkKJCZ7-oCGaYbHaoV60wIp8tWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=ojB8S3y_Fb0R410O60LrOiP3fLrdAX8gsm23CC6eRG6nojmAcmDIgILJIWh5TIBUpw0qyjrrid_tc3EY-3IsxIxBKbbwQPFx05loOo8sp8EG-Qllb1k4KFyQr4cwvhgw_wevpNUSuz5X-XBFLf6aPxYpMlkj-VyKrPx_6LNSo_X3GH9JNIqdBf9xeE6tPnt_4VtNQFECKySrKnx13uXdXN1jcXI4q4jnrt9VlcOmWWVHd03MCmDy_ld7WNfleCKKVHJlukd29r30VMFqTYwjgvYm0Or8od2HOBdRG2jioqEAD9u1vfmi9t_mz5GiMIf0bTXRGuqkakxFjO5pNjMaVGBgp0NjJy25aLDkT4CUcllNXcQDpSGicc43ILzGZ3FxA59C94ZtlGPMhanNDrzkkedPM_PnHERX5ECNH4rZRyKvI9stYu-oy4DLJcA5JSLCYFnHO6WNv27OtsQTOTWSHSRGV_riUjo2_6pIoy87AFWwNqUlYxiCeNUNLYgbfxW47USMVrVdB56URRpDHrB0iug4y3EHDkEGR7txAq0ZNFFhsmyqkEYYqeFRjbceOM0yk4bNi6U6SNMwBvuZE03MyAE6m15vFfPLsLl5GsEXtKL8XF-ZcJtxg36EMTBZbdGKPfAyYyoOFt-0ZU5eBVoSPl-yN7ivluwikoeoA_1Sb2o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=ojB8S3y_Fb0R410O60LrOiP3fLrdAX8gsm23CC6eRG6nojmAcmDIgILJIWh5TIBUpw0qyjrrid_tc3EY-3IsxIxBKbbwQPFx05loOo8sp8EG-Qllb1k4KFyQr4cwvhgw_wevpNUSuz5X-XBFLf6aPxYpMlkj-VyKrPx_6LNSo_X3GH9JNIqdBf9xeE6tPnt_4VtNQFECKySrKnx13uXdXN1jcXI4q4jnrt9VlcOmWWVHd03MCmDy_ld7WNfleCKKVHJlukd29r30VMFqTYwjgvYm0Or8od2HOBdRG2jioqEAD9u1vfmi9t_mz5GiMIf0bTXRGuqkakxFjO5pNjMaVGBgp0NjJy25aLDkT4CUcllNXcQDpSGicc43ILzGZ3FxA59C94ZtlGPMhanNDrzkkedPM_PnHERX5ECNH4rZRyKvI9stYu-oy4DLJcA5JSLCYFnHO6WNv27OtsQTOTWSHSRGV_riUjo2_6pIoy87AFWwNqUlYxiCeNUNLYgbfxW47USMVrVdB56URRpDHrB0iug4y3EHDkEGR7txAq0ZNFFhsmyqkEYYqeFRjbceOM0yk4bNi6U6SNMwBvuZE03MyAE6m15vFfPLsLl5GsEXtKL8XF-ZcJtxg36EMTBZbdGKPfAyYyoOFt-0ZU5eBVoSPl-yN7ivluwikoeoA_1Sb2o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا به دو پل در استان گلستان - آق قلا - حمله کرد. یکی از این پل‌ها، پل راه آهن است.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5962" target="_blank">📅 06:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5961">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=UimQEwVHkFr4_ODIlSTWPp48Rq0PRo7ItK2Apb7FlvBScMQYa0dGDN1AT4Fgm5uGs4lzNDyDSAhy_pBiwUFDOU7Saqvm5oBsIoacSGGTL6eA31qMKeJH8tAm7lxRF0JEW-RpPSs9r6uRixHQdPaI1cqZsITvGfjoDPoHI7YFRUnlSGqY_HhYOIo-Mfwijisi1OwmNlBuzN_HyHovQ2VcxcmtpkQY7M_OulVovP0jForX2GLYrhzO13lifieUdxHzF879NkwKC98jeY2SnWhEgWRZmnYc4dWSApL6LAOGELW_aEiM6rt06sakVBfRYpthsCblkwj5FVVbMeL2cWNaVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=UimQEwVHkFr4_ODIlSTWPp48Rq0PRo7ItK2Apb7FlvBScMQYa0dGDN1AT4Fgm5uGs4lzNDyDSAhy_pBiwUFDOU7Saqvm5oBsIoacSGGTL6eA31qMKeJH8tAm7lxRF0JEW-RpPSs9r6uRixHQdPaI1cqZsITvGfjoDPoHI7YFRUnlSGqY_HhYOIo-Mfwijisi1OwmNlBuzN_HyHovQ2VcxcmtpkQY7M_OulVovP0jForX2GLYrhzO13lifieUdxHzF879NkwKC98jeY2SnWhEgWRZmnYc4dWSApL6LAOGELW_aEiM6rt06sakVBfRYpthsCblkwj5FVVbMeL2cWNaVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : جمهوری اسلامی یکی بزند، ۲۰ تا می‌خورد.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5961" target="_blank">📅 06:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5960">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bh6OisT2Qi1qUKtlMZs5M9gQLWmAC_nkQlBIeiE7towRqDhKRkYHCGGmfhWb1hRlsnmlLzcJ3zsrsoIdPpzPiSO2PgKOJvV0YmXvlVp_P2zc6xAx8m55z5V6-vmxALu0Py6i8-dnk0vNEAV2keo5SzwM4P4pCasuYPX0VtTJ7IcSPXqH-IeEB4gZy1KTUIQ_X92HNYqFzIIAeeqMozF0MPrOCVJzqZfbOc1AlsHTWMWIlBcQNMSk3jTj3-N1nTCCzp_DqhR5u2uG6vFNC9M15QrBNEMUtcH_uabR2t5jmlBCdaBtAYHDdPuC29o_iAEbBLXYkUiO0m_kOw4CBymmaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5960" target="_blank">📅 05:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5958">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=sLbgaxhmGLe7Qw5M0TfOnhICB7P5N-yMTsNhzXTmGyefH8LpfqJdd2ljS9u-wJu-C11MEiwRSAiw_0QgMgvCsCMD4jB8y2Ac_vrhDGyG_rmsCKVYJDz2NlQ41hY8iHnpKK6nH7p-aI3F5lJHVGpb9iR9BEy8eUcoKhCeIldVQFiXm8L6gNeNrAEr1RrS7vGzBLpT1zbl8Le_101LpiTCcAcKhr2ef_VuUIIq5LL31Rx8IPnCvAEY6SnQLda4C_1kVBzWPIzgj6_9TCHPPkkJ4PeL7RvBsKrKdVbAHIS5fTMhVIiaxkau51i0lKpAJ-ovSCQcIMWkEd8YzNE7R3sfvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=sLbgaxhmGLe7Qw5M0TfOnhICB7P5N-yMTsNhzXTmGyefH8LpfqJdd2ljS9u-wJu-C11MEiwRSAiw_0QgMgvCsCMD4jB8y2Ac_vrhDGyG_rmsCKVYJDz2NlQ41hY8iHnpKK6nH7p-aI3F5lJHVGpb9iR9BEy8eUcoKhCeIldVQFiXm8L6gNeNrAEr1RrS7vGzBLpT1zbl8Le_101LpiTCcAcKhr2ef_VuUIIq5LL31Rx8IPnCvAEY6SnQLda4C_1kVBzWPIzgj6_9TCHPPkkJ4PeL7RvBsKrKdVbAHIS5fTMhVIiaxkau51i0lKpAJ-ovSCQcIMWkEd8YzNE7R3sfvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکله و برج اسکله بهشتی در چابهار</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5958" target="_blank">📅 00:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5957">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
گزارشی از قطع برق در مناطق گسترده‌ای از بندرعباس، بوشهر و چابهار</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5957" target="_blank">📅 00:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5956">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/693dd42141.mp4?token=PaYEre2zuvdjWcnMXc5_cSdRroBs8CRh0mCOJEBhCNV4EzPD6Prl_k2dkhyEuiigbS1_VQ0nP6FRvb6eitvasnbPsVvHMlPeuwbByxDBO4AlAX358LIB3EtrdDT26t_wN11zvnZzX4qy4Tt_S3Xko_XTJj6c9wl8mKtPOBZ0pE0g8HLJ2ZALotvFeDjZHV_7x_qEJrQpIwNyKhKtnkYtIG_iXU8xbb5BYsvVmtzWMVE0_FJD3cEVbFa3Mvl6IIXoxi-VD7XDmKL_qpB3u-eOkG62G1RxxEf9-6riOGWvJ0s5YEBtd1sTTZW2WYgRI0bsblTbPQf0t7UIEXAl3915Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/693dd42141.mp4?token=PaYEre2zuvdjWcnMXc5_cSdRroBs8CRh0mCOJEBhCNV4EzPD6Prl_k2dkhyEuiigbS1_VQ0nP6FRvb6eitvasnbPsVvHMlPeuwbByxDBO4AlAX358LIB3EtrdDT26t_wN11zvnZzX4qy4Tt_S3Xko_XTJj6c9wl8mKtPOBZ0pE0g8HLJ2ZALotvFeDjZHV_7x_qEJrQpIwNyKhKtnkYtIG_iXU8xbb5BYsvVmtzWMVE0_FJD3cEVbFa3Mvl6IIXoxi-VD7XDmKL_qpB3u-eOkG62G1RxxEf9-6riOGWvJ0s5YEBtd1sTTZW2WYgRI0bsblTbPQf0t7UIEXAl3915Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش سوزی گسترده در بوشهر
🚨
کشیده شدن دامنه حملات به جاسک و ابوموسی
🚨
گزارشی از فعالیت پدافند بر فراز آسمان اصفهان</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5956" target="_blank">📅 00:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5955">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jRurjOpaOl32s1CVb74ueAF2WPRvkmsRJTMvkk7NWvaFg3F2tMpE8CiK7Br7o4FFSvfhATUqd0_hrifUp4cirX3gw1a1GY6lpNYzMCMwVy8OyduwROv1GrjFAAeEazAC1agiEhfHiVgabodtFLP9SMPiVNbKyiFoJfShk3I9cW-uU1rmh88EhfGanEld3qDkhKKpqSj2S2q7nYU8v7yPLCTlxK7IYw8eVmx_23Bdwsyl-UHBYxioT66q7ISSAQGRNUXz942ScVptfxoBLcyy078gHlmDxlo1C7nDx7ViZYp3MFh5CGGFOqudFME-My0LrBKL-wt-UqlASBAZydl6HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت مجید موسوی، فرمانده موشکی سپاه</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5955" target="_blank">📅 00:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5954">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
گزارشی از حمله به یک پایگاه بسیج در بوشهر</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5954" target="_blank">📅 00:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5953">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e3ae34ead.mp4?token=JrsgfAOjTjQd4gIjL2CoWHQgVgoPkPkRhx7cA-H1W4J683zGl-NiA4FP3BHNSyUvdSL5TQnoatFDa2b1nexD57KTVGfto1e7xOlCcEenjpQiN8ic8DrzohBztFWqlNIx1dU7iFlJaj_uqToeFQImN6Jvm1IvBDsRIzq_BoHkFRZhXy6W-AMO3XMxYTQglD2BkCkrjoUIqDbrALxMmtpQ0AdSZEkOjbt0kr6NjkgfRipVYDItjOykKr1H0l5LThH0azhZnNbc7rYaL4ADvlWAYAhcQikW1oReE1t0vA8PxRtqJ8aSPpCw5kofZYZzzHIC2lzDkPvopYep2bWMrofgOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e3ae34ead.mp4?token=JrsgfAOjTjQd4gIjL2CoWHQgVgoPkPkRhx7cA-H1W4J683zGl-NiA4FP3BHNSyUvdSL5TQnoatFDa2b1nexD57KTVGfto1e7xOlCcEenjpQiN8ic8DrzohBztFWqlNIx1dU7iFlJaj_uqToeFQImN6Jvm1IvBDsRIzq_BoHkFRZhXy6W-AMO3XMxYTQglD2BkCkrjoUIqDbrALxMmtpQ0AdSZEkOjbt0kr6NjkgfRipVYDItjOykKr1H0l5LThH0azhZnNbc7rYaL4ADvlWAYAhcQikW1oReE1t0vA8PxRtqJ8aSPpCw5kofZYZzzHIC2lzDkPvopYep2bWMrofgOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امشب - چابهار - حملات ارتش آمریکا</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5953" target="_blank">📅 00:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5952">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f1cRRKbbE2cfxeZrdvAEsVLJs1W-wf8_3ztIFb3iugI4bdB-TvhfsXxJmQcF9KArMcKxC_ALfp7Jq3W4sWidPPaywmr41BlpTdHWcYWLx9YEeRgS0rY58-59RCcyd8IIVg614urzJdZvGeYlD7Txx2IOIAye_xt8Ya9lAkW3s4qiROui1xhxyojiMudvDrL7K7cv5ayWKjZKNZuRLrgkhBnXo96HI8qVIjZOgQ0vBdWyxWq6q4niEIMM81ipIdc2lZ4VYKZxVneqVJ5cog5r4i0XXzBQBtvWl-gryyKv3w9C7hhOr_kpuka_WRrj6AA0INLFYi4gvVG1ExrdJstxig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله به یک سیستم راداری ضد هوایی در بوشهر.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5952" target="_blank">📅 00:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5951">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">حملات به قشم و بوشهر نیز کشیده شد.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5951" target="_blank">📅 00:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5950">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‏ایرنا: صدای حدود ۱۰ انفجار در چابهار و کنارک و قطع برق قسمتی از شهر چابهار</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5950" target="_blank">📅 00:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5949">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a030961c3b.mp4?token=bqfXcnbhU9ND-4W7NS_ehu_c_Tb0JSIajzUlN7s3rMLDprUT2xL3bqcbfwZsI-gmA2ssAHpmz40sk2Z5nYkvvRGoITgAAO2zaMSsLy1aPcUHTK-5DtkixEQqSdTm4JEg7JM1in2_t8KbNGHMT3OoPPcB5SFtZWCxUAAPgSDeg75hdmCYsGZlp54KUC5N9yPZV16eZlJ3uoX0iIRhVm9KdH2m5mqsKhmh9pxEepuEhRuhCWhkgPga3_-fcWP6q2I7F9vtYken1tm1o0CLJ1tyJ1J5VkFAuz8Tr70JZXVdPZlTlPs7_4sXQY-3DaxJv3KZix5Y_gsy1KjZNMUVQXZFxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a030961c3b.mp4?token=bqfXcnbhU9ND-4W7NS_ehu_c_Tb0JSIajzUlN7s3rMLDprUT2xL3bqcbfwZsI-gmA2ssAHpmz40sk2Z5nYkvvRGoITgAAO2zaMSsLy1aPcUHTK-5DtkixEQqSdTm4JEg7JM1in2_t8KbNGHMT3OoPPcB5SFtZWCxUAAPgSDeg75hdmCYsGZlp54KUC5N9yPZV16eZlJ3uoX0iIRhVm9KdH2m5mqsKhmh9pxEepuEhRuhCWhkgPga3_-fcWP6q2I7F9vtYken1tm1o0CLJ1tyJ1J5VkFAuz8Tr70JZXVdPZlTlPs7_4sXQY-3DaxJv3KZix5Y_gsy1KjZNMUVQXZFxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از حملات امشب آمریکا به چابهار</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5949" target="_blank">📅 23:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5948">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sanu4eZzBwbdm4T6RGiTt8J2vx2-3Df5hG9F-siqMt2OmqOxh53VikETU8cY9WcCIBEE8-HGAP9XDWRltD9hB6TGxgwd0HYnw9aCrD2WiY1AYTX7bSBSPGY-ucoDOy9wTKUXw6apl9KNyWevmY7hyRWcn8zgZxXeNKO5rMmNAxORfdkndDhzUSGlC_ut8PLyt6d5wQvgyuEol-v6ua8Afk0WG0x7oVQcgSEVvhqqieWlwiyUwkxSTrnCSwpOK5VPwnNrmVyDjQyXB_srztu3oMdPntfiqHaFXubv5nJGHP6Fgz-_Abf5ac24WptgpUxVhaL3VG1-mK_Xdtgiox_JBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به اسرائیل اطلاع داده است که قرار است امشب حملات گسترده‌ای به ایران انجام دهد.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5948" target="_blank">📅 23:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5947">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌هایی از شروع حملات آمریکا در جنوب، حمله به مقرهای سپاه در سیریک و بندرعباس.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5947" target="_blank">📅 23:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5946">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌هایی از شروع حملات آمریکا در جنوب، حمله به مقرهای سپاه در سیریک و بندرعباس.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5946" target="_blank">📅 23:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5945">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">جی‌دی ونس که طرفدار مذاکره با ج‌ا بود:
قرار بود ما محاصره دریایی رو‌ برداریم و اونها هم‌ دست از حمله به کشتی‌ها بردارند. برای یک هفته خوب بودن ولی در ۲۴ ساعت اخیر شروع کردن به حمله به کشتی‌ها.
بهشون گفته بودیم اگه
حمله کنید به کشتی‌ها باهاتون محکم برخورد می‌کنیم. نمیخوام بگم امشب قراره باهاشون چی کار کنیم.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5945" target="_blank">📅 22:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5944">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c3530f756.mp4?token=Z4GA55hN_hSho-1oGBVnc_epH0__KWk_NRDW186dB0VbVMTI54h7x-vt0O2MsCyBMNGIkGkn5dT2HQ9n0GypKX1S8f_wzbHfoJXhkgVC906SXP3AyANP3rPgQoZdJKLb-Yduq_7Kh-N5bLagQzWG4-BXZ8TWxafhZTIbCkznFJ2KQLgYcLI9fCPHAcAurxRxpSK9JU65N-zc3CBX3_wikuRmcyosNJ4-ch2FtDmhgUZnBEHLynam8gUm2-CcvubTIy9ihHpt31EVdRcRCUH_UJuPJuu3v9q7wYDXxn4fzIZl9jMux2wHtNlbSPTsRis8V26gHFiCdIPk5rIOTdL4fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c3530f756.mp4?token=Z4GA55hN_hSho-1oGBVnc_epH0__KWk_NRDW186dB0VbVMTI54h7x-vt0O2MsCyBMNGIkGkn5dT2HQ9n0GypKX1S8f_wzbHfoJXhkgVC906SXP3AyANP3rPgQoZdJKLb-Yduq_7Kh-N5bLagQzWG4-BXZ8TWxafhZTIbCkznFJ2KQLgYcLI9fCPHAcAurxRxpSK9JU65N-zc3CBX3_wikuRmcyosNJ4-ch2FtDmhgUZnBEHLynam8gUm2-CcvubTIy9ihHpt31EVdRcRCUH_UJuPJuu3v9q7wYDXxn4fzIZl9jMux2wHtNlbSPTsRis8V26gHFiCdIPk5rIOTdL4fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/farahmand_alipour/5944" target="_blank">📅 22:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5943">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe5d27edac.mp4?token=HAxQoXabwVa_RO4wkNJLG3e7rEOlQyjbcIchLsdWbLKBh4JfIL87wqmhynp8wjjqe3Nzw7oM4soQZRQTnWBFPaIukYvDwF7H2xD_CkycP696zo_1ELlUglD7aPfjFaU35hiUUKBEv_Qts62kOaFuWQdHtp9K3EAN4trW-s4GAj7-0Zb81EoFW3IsGz7wJnjNGNa7FEbyWr0PZfbNGUm_0ysWzoN33VCy7xdOsUx7PznCN9pO6sawSG6JGXlDJWUP2h33jdYSHymr5cpOmIxJpqeZXyYvTkpxzBMjl5Il-YBaVqxWY6Ht9mtnUXBBOsBTNKV-w1I6mWQ9G7TeM3Zqqnh2SEN4YvvYBxd4XxGS9XENHbw3mj_66gt17gL710cOE0Lw3EsYw_BFeaM86LLrTCe9vkrye8SEDSmX900pQ43fi_g4KMBebWGzeEanTW0F8qY8wDZSogplnjZbeyffYGPOXKWx76exR5s7R6ZMDvHjiIUCSjzcPde-3g39584a5NgA-cczGLrtG9Z1yCZ5KHbxjqu6D6F0uOBl1aMpDTpU80FjCBu3flao7whDMCtcOcd8qrQFQXqYA9GONsyQteFl23pIyU4b31-H04XmaCV_Tg4WHXTLhe68m1MTBtuX77oYz8vSdYvI-FOzm7jLu-v9fqQbJpxWUn3e69gXgN8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe5d27edac.mp4?token=HAxQoXabwVa_RO4wkNJLG3e7rEOlQyjbcIchLsdWbLKBh4JfIL87wqmhynp8wjjqe3Nzw7oM4soQZRQTnWBFPaIukYvDwF7H2xD_CkycP696zo_1ELlUglD7aPfjFaU35hiUUKBEv_Qts62kOaFuWQdHtp9K3EAN4trW-s4GAj7-0Zb81EoFW3IsGz7wJnjNGNa7FEbyWr0PZfbNGUm_0ysWzoN33VCy7xdOsUx7PznCN9pO6sawSG6JGXlDJWUP2h33jdYSHymr5cpOmIxJpqeZXyYvTkpxzBMjl5Il-YBaVqxWY6Ht9mtnUXBBOsBTNKV-w1I6mWQ9G7TeM3Zqqnh2SEN4YvvYBxd4XxGS9XENHbw3mj_66gt17gL710cOE0Lw3EsYw_BFeaM86LLrTCe9vkrye8SEDSmX900pQ43fi_g4KMBebWGzeEanTW0F8qY8wDZSogplnjZbeyffYGPOXKWx76exR5s7R6ZMDvHjiIUCSjzcPde-3g39584a5NgA-cczGLrtG9Z1yCZ5KHbxjqu6D6F0uOBl1aMpDTpU80FjCBu3flao7whDMCtcOcd8qrQFQXqYA9GONsyQteFl23pIyU4b31-H04XmaCV_Tg4WHXTLhe68m1MTBtuX77oYz8vSdYvI-FOzm7jLu-v9fqQbJpxWUn3e69gXgN8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل برگزاری مراسم رو
انگار غزه است! با بسیج کردن اینهمه ستاد و پول و ارگان‌ها و…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5943" target="_blank">📅 21:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5942">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HIYk6RYqsZprnnedxDz9XaOiQEzJerASUb0ogPP36hULmWp56bNH65nOPvMuviKOJ9qUpG1of8tpRNaCjEcMI6kvY2bAabmmkOlB-so3daQgWHVv-5mjBacvB1ThN20YUaPfXKk44dCrnXpNTc96Kv1KvyRX13yhol_8wToihOPWf9MX6F3DRnlK9vOTQ4ZNnkBg-ceFKql2uyrkzgjpHz4h84QtwOHC81-PxHjaksUzXTbPKsE3czw2xcWXsMcm2zdjy-MYRPdWRU2kU18Rt-mLR3ASPHhGoRs5K9xsdxDNwjzoevE0mojw7nZ-jCMwWU7cbTzxYwaTgSvoAbgCjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: درباره جمهوری اسلامی کارهایی انجام می‌دهیم که باید ۴۷ سال پیش انجام میشد.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5942" target="_blank">📅 20:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5941">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c3c23cc7c.mp4?token=jbN0N4AilNX0fHM_p31Gd_zu2gX13LXG8QeA0PHtq52tf8k7QY22b1Xs3L9CtIVpjAL3RHp3MH4l7Zu-P6M6TboyFyCeAF9DcXgqnA3iXQD1qhI6h84n4tY0DZTxWLON0GGogRAsIuGLKhBG0bJb1jdJQ1pk7eU-a-8gLGQoxP71FZZyz0XouIgOpBZY6HAtGrNZa1KqBYR_ZQbLG4VX1mgUAu8YVJjBFfA3652NhKmnYGoCcFUKUHtk00D3MwzLfHK56tjfi_MNvZv1HG1AFHMYrS18mDbFHAKmco3vHMW0SD_0W8c-cwi9R-Q4X1rC3Nx4IXoiMMgFaO0dmlPl6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c3c23cc7c.mp4?token=jbN0N4AilNX0fHM_p31Gd_zu2gX13LXG8QeA0PHtq52tf8k7QY22b1Xs3L9CtIVpjAL3RHp3MH4l7Zu-P6M6TboyFyCeAF9DcXgqnA3iXQD1qhI6h84n4tY0DZTxWLON0GGogRAsIuGLKhBG0bJb1jdJQ1pk7eU-a-8gLGQoxP71FZZyz0XouIgOpBZY6HAtGrNZa1KqBYR_ZQbLG4VX1mgUAu8YVJjBFfA3652NhKmnYGoCcFUKUHtk00D3MwzLfHK56tjfi_MNvZv1HG1AFHMYrS18mDbFHAKmco3vHMW0SD_0W8c-cwi9R-Q4X1rC3Nx4IXoiMMgFaO0dmlPl6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - اسکله بندر عباس
زیر حملات ارتش آمریکا</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5941" target="_blank">📅 20:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5940">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dd51af5b9.mp4?token=Ogd-LgNe_praqw41qkEUqmlIAtaXbY8Ljv2rUZjHK9iVIwnNZy2xV0eYR8Y0rNWu_1wCx5lOrxFiQk32T4AiGTjmWYvDk_o7b38MDcduQ4E3gArqtukjoctBCkhHbZGNh1TUBAyKXTWcpg8Prjrf2MFLtPRynut14o6eB6P97wQ4Nkp4UNcwDhtOzdjeNlBeZDOX1R9b9H_6Xeu2JU-ajvI2ac26HorTgRfRcAERCrizL6OsisSLtgT6P-zWvZ-ufvPA19ZOlkNgrAMxuno2Senqiw33mAZhONZAPE-KENmVE9IvSx7q3PpoDCuO96ZxCigpSKmatNi56dxLEY8d-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dd51af5b9.mp4?token=Ogd-LgNe_praqw41qkEUqmlIAtaXbY8Ljv2rUZjHK9iVIwnNZy2xV0eYR8Y0rNWu_1wCx5lOrxFiQk32T4AiGTjmWYvDk_o7b38MDcduQ4E3gArqtukjoctBCkhHbZGNh1TUBAyKXTWcpg8Prjrf2MFLtPRynut14o6eB6P97wQ4Nkp4UNcwDhtOzdjeNlBeZDOX1R9b9H_6Xeu2JU-ajvI2ac26HorTgRfRcAERCrizL6OsisSLtgT6P-zWvZ-ufvPA19ZOlkNgrAMxuno2Senqiw33mAZhONZAPE-KENmVE9IvSx7q3PpoDCuO96ZxCigpSKmatNi56dxLEY8d-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه مراسم برگزار کردن … ستاد برگزاری ، هزینه هنگفت، ده‌ها ارگان و ستاد زیر نظرشون.
بعد کارهاشون رو ببینید!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5940" target="_blank">📅 19:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5939">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T4HvwxSfvmdf6Hp0rjcVzGVJMBxAqGiRSamOws5ZSffe9fKP_vh__asceHVMdy1ESswwBLljz17fqss-kfpuDm1YtK-tsvyC_-1ExsJCtDMEoapy2AokwTtibBSPAngGOiumPXP_ZDRTr92-gyr7fIBOzQtWRFADScomwu1VPg7tQdVb7HuDL-a_gNBMlOdUoovWlH-abUYjwHjvTfW9chMHZzGf-nE4MJrCTDDvXR8A6u7qXQfD41J4HwWCBDYWqITlNG7BnqGXmuoO-P45CnQ6ml9WwQ2vcuPEak6OHUJLThsGnf8YO636yY15VOJ5HLTlH2e9uayjSRJTLGyCSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کشته شدن ۸ نیروی ارتشی
در جریان حملات دیشب و صبح امروز آمریکا</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5939" target="_blank">📅 19:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5938">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ترامپ: اومدن خواهش کردن زمان تشییع جنازه ما رو نکش. بعد وسط این مراسم حمله کردن به سه تا کشتی.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5938" target="_blank">📅 17:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5937">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=vIWCqa3gRANWwrspkXnrUVM6WFNibPnglM9hdKwdHyr4u7QaOkuzQQIEF2UNWL8zeoNcJVegiQ_2G2jmYV2sWwxmyk_ThzoQfVFk4chxfs3P9ULIOZAqq08lYZkEsi_OQItJtJ3Cd8jV_RHPG6m1TsEzRnyobGTVoo_kPCDs3-v3MJH3tdrhZoAei23X-alEu6xe_wNbxZpBLAAB9jmH9UhN1NaJe_YuheUpHli2NScdk8BOVIfVrRI6H_Ctf1yiJdUmnC3T6ClcijZSldXW5wD_WqVtJgmCwjdwXpC0UnUqs9AT81fikdBGLb_2EejChR4HyRAyML1J3ObGA7Io1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=vIWCqa3gRANWwrspkXnrUVM6WFNibPnglM9hdKwdHyr4u7QaOkuzQQIEF2UNWL8zeoNcJVegiQ_2G2jmYV2sWwxmyk_ThzoQfVFk4chxfs3P9ULIOZAqq08lYZkEsi_OQItJtJ3Cd8jV_RHPG6m1TsEzRnyobGTVoo_kPCDs3-v3MJH3tdrhZoAei23X-alEu6xe_wNbxZpBLAAB9jmH9UhN1NaJe_YuheUpHli2NScdk8BOVIfVrRI6H_Ctf1yiJdUmnC3T6ClcijZSldXW5wD_WqVtJgmCwjdwXpC0UnUqs9AT81fikdBGLb_2EejChR4HyRAyML1J3ObGA7Io1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دشمن هیچ غلطی نمی‌تونه بکنه
مجری : خو اومد خود گوینده این سخن رو زد!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5937" target="_blank">📅 17:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5936">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/046bf7600e.mp4?token=ekRxKkrADVC6h4aKyH8icTHpcC0gKuszANyQfd2nnq3a4h3Fx9ZnRKNO0toCo7HuOrUPWK-p-aNvA9FwWoSkilDy4gjShhWTz01KHMXRX6x0G7sUxhqK0TGh965W1eKXjmcpW1zVF5AT0hgtapmX9mur9RcXQtFH21vLX2cVagJJYTDFfR8laeJw8TiIJcj9hvSFV3-jyC8SianLj7WWiFMK197LNv8aRampEy4I82t5o6W1Rki_01m__tc_uuRG1ev6uq5JNVkoS2gGUPtX14hDWEKoMDkwU8VC7ygsokLlGgsYo9aXx33-OqXfKpEMSKkjEgGuwgutPLYzNNI47w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/046bf7600e.mp4?token=ekRxKkrADVC6h4aKyH8icTHpcC0gKuszANyQfd2nnq3a4h3Fx9ZnRKNO0toCo7HuOrUPWK-p-aNvA9FwWoSkilDy4gjShhWTz01KHMXRX6x0G7sUxhqK0TGh965W1eKXjmcpW1zVF5AT0hgtapmX9mur9RcXQtFH21vLX2cVagJJYTDFfR8laeJw8TiIJcj9hvSFV3-jyC8SianLj7WWiFMK197LNv8aRampEy4I82t5o6W1Rki_01m__tc_uuRG1ev6uq5JNVkoS2gGUPtX14hDWEKoMDkwU8VC7ygsokLlGgsYo9aXx33-OqXfKpEMSKkjEgGuwgutPLYzNNI47w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
هگست وزیر جنگ آمریکا : همونطور که ترامپ گفت امشب احتمالا اونها رو عمیق‌تر و محکم‌تر می‌زنیم.
ترامپ : محاصره دریایی رو هم احتمالا دوباره علیه ج‌ا برقرار کنیم.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5936" target="_blank">📅 17:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5935">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aff1f3384.mp4?token=qOnK9pc84YQuLgejb6AZqvdQRRiU_QOyROXQK7YJng-_f2VBwn4q3wapc8gsKjoNbFiD_Pqy1I4EimniI4m8ijpBeN9yj07OmYgJJpd1KpZInBeaSY8DB-PhLi-DhaCPIEYVXPWg1wQFiSnZ-nbwDtMPG9pYusd9DkkCODWLJb7gT6iGvHeP7o_byMA2S2tKMkCQRq5n4xablcdyCwgNlwfb88vDjOPDA6FETb2WKlP2LOLzx6Glti7PFiig7ieVr9R6YCW10NmpzbCi7J8vZoVg9ITKFmTPF3xm1xLCQwI62UXTChxPy9RTQBDI2ZWCay0WRlOwdPfWxNWeQ0T1qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aff1f3384.mp4?token=qOnK9pc84YQuLgejb6AZqvdQRRiU_QOyROXQK7YJng-_f2VBwn4q3wapc8gsKjoNbFiD_Pqy1I4EimniI4m8ijpBeN9yj07OmYgJJpd1KpZInBeaSY8DB-PhLi-DhaCPIEYVXPWg1wQFiSnZ-nbwDtMPG9pYusd9DkkCODWLJb7gT6iGvHeP7o_byMA2S2tKMkCQRq5n4xablcdyCwgNlwfb88vDjOPDA6FETb2WKlP2LOLzx6Glti7PFiig7ieVr9R6YCW10NmpzbCi7J8vZoVg9ITKFmTPF3xm1xLCQwI62UXTChxPy9RTQBDI2ZWCay0WRlOwdPfWxNWeQ0T1qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : اونها تحت یک توافق هرگز به سلاح هسته‌ای نخواهد رسید، اما شاید بدون دستیابی به یک توافق هم به این هدف برسیم، اصلا شاید راحت‌تر هم باشه، چون اونها دروغگو و‌ شیادن.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5935" target="_blank">📅 16:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5934">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5484fca6.mp4?token=HSW-N-L_9i3P8dXmOAjDoPOMzZCG-G8iOiGbN5LHOHiJcvr20QyYORphbjRwCIsdWg_QHntqdv_3tPuBs_Fv4fZepV9n81-fD2Ifzm1d32ctdTMFM83HoW9VHCwkdk0-f5g9siQyzFHdfcTFtK9t3CveT1bydyW0wMqM_Lzif5VprQP6Ucl7imJkpF2GhvMlFkA40_2yIgX7SSeZLFGJo4AAl4MLSGdAtT_EPdIRa_aWZTRtxbdCYp3zKVevG3BG3WRgxybSJN1SVNPkRO06TA401F9Lwpz8ScTPLHkNsibB5ASvy8M0NZ5nJE5oZ1teS-BP588NoNGVd0vx2SDWJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5484fca6.mp4?token=HSW-N-L_9i3P8dXmOAjDoPOMzZCG-G8iOiGbN5LHOHiJcvr20QyYORphbjRwCIsdWg_QHntqdv_3tPuBs_Fv4fZepV9n81-fD2Ifzm1d32ctdTMFM83HoW9VHCwkdk0-f5g9siQyzFHdfcTFtK9t3CveT1bydyW0wMqM_Lzif5VprQP6Ucl7imJkpF2GhvMlFkA40_2yIgX7SSeZLFGJo4AAl4MLSGdAtT_EPdIRa_aWZTRtxbdCYp3zKVevG3BG3WRgxybSJN1SVNPkRO06TA401F9Lwpz8ScTPLHkNsibB5ASvy8M0NZ5nJE5oZ1teS-BP588NoNGVd0vx2SDWJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ساختمون همون جایی است که خامنه‌ای حامیانش رو جمع می‌کرد براشون می گفت :« کشتن بد است، اما فتنه بدتر است.» (پس معترضین رو راحت بکشید)
و اونها هم براش «حیدر حیدر کنان» می‌خوندن : لب تر کند امروز سحر قدس شریفیم!
ولی داستان یه جور دیگه شد</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5934" target="_blank">📅 16:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5933">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=vsEpA_s_NyHYzzp4THuiCn16PmjpCNn2BGTeX0WN28RwlLQS_SoRm3UmHpWlDQTHvUsl_KSkX4sKJR44zJS-Y5DIYDm0ibYO1M-9LVHuYQcqfjOVxFHTSdgY7CROldbeELr76Ey8tBSiZy_eY0FojDe7z8fchgU6NhPG57LYGQf_fvy2hnjqGQusapPT4O1fhhl9-tiALlni2wmchRQS5oCTrO7bo4_B99Y7iiPqGIUiEvRCbVNq1yp6RIhqN0oZpNTZKYoq1YNjlKBB8Fd7RAFYyvp09LhK0h89PAhn7O8L92kC-deELT7gp6uBM8yZa54qXnHAnN_b-2nqcEyJlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=vsEpA_s_NyHYzzp4THuiCn16PmjpCNn2BGTeX0WN28RwlLQS_SoRm3UmHpWlDQTHvUsl_KSkX4sKJR44zJS-Y5DIYDm0ibYO1M-9LVHuYQcqfjOVxFHTSdgY7CROldbeELr76Ey8tBSiZy_eY0FojDe7z8fchgU6NhPG57LYGQf_fvy2hnjqGQusapPT4O1fhhl9-tiALlni2wmchRQS5oCTrO7bo4_B99Y7iiPqGIUiEvRCbVNq1yp6RIhqN0oZpNTZKYoq1YNjlKBB8Fd7RAFYyvp09LhK0h89PAhn7O8L92kC-deELT7gp6uBM8yZa54qXnHAnN_b-2nqcEyJlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ : احتمالا امشب هم اونها رو به سختی بزنیم. فقط دارم یه هشدار کوچک بهشون میدم.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5933" target="_blank">📅 16:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5931">
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/revpKJ46_bwG2KCR8fhD7x6oSSUdjtXYWeehawbXv5LFVMaFMKNsgDvghTFn2RtSY3bG772RKqaRL5BuZbpUIDnwxadWAv52sffNXoek-mNrOdk3XEyVm6onD2NpLfoLYh8ds4gY7g-6JDwaZ8q4Iw4DPucx71By29N3YiRROK0qnT7kcbafbOIF-lut4CqOOJQ908cSKr9kkPy2Cb1lrG6qxKO-wuPKvPykQtuqcNAGOt026kNPxcH8qCk1gnAte83AC4DeHPGOfLxqr3Lnava91YC9RNVFkP0_L-ccx1jceFd__TbZqsz5jKJXu0vEN_eLwZoXDnlrRbjKLRP8nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه کیهان زیر نظر خامنه‌ای در دو مطلب خواستار کشتن ترامپ شد.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5930" target="_blank">📅 15:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5929">
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D8nOexoSZ3VXjwVxYP-4YySYoWV8BS8F5A5kxT6fbKkoCPKVbF4pz6oi2NMPealaMDQ8JL1aVoj7rzizx2S0ioOUvx_pJSezPkQ2PGwr2LFWAjElc89B9QAVh1OSGXbCoJswhpPHsQcrVAG57BrFA5l4eEgkCq2XpiTuU8SF-5o0TddPYFtFNiWqOR_RQkZgy3tnkaKKanwI1KoBjjNWh2C_la91_YOCiHn5_y7aBmB21jb8vGoy0kZrRxJDrBLxJeeFnFBk5AxfEk8AiFXKWqNVnem6V3omTLMiC38zXJ7ZMFM-wxyZBhMV6YDuXbXC9l-b316RLEhkmZH5ghraAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوش دولت چپگراش رو چنان بکش
که درس عبرتی بشه برای بقیه اروپا!
برو جلو! دعای خیر ما پشت سرته!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5928" target="_blank">📅 13:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5927">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">محمد اکبرزاده، ‏ معاون سیاسی نیروی دریایی سپاه، ‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.   او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.   جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5927" target="_blank">📅 11:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5926">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
دبیرکل ناتو : حملات آمریکا به جمهوری اسلامی کاملا ضروری بود.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5926" target="_blank">📅 11:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5925">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Heo6DCgSmmdmgZxmOR6m7rkH5a1qt_cDrIGEQPeP56R5s4bXwy_WarV0E3ZbC3dihU3-g-DU-oHFhqJxGCfb0L6u0xrisc3tO97iFHrEOHUeCBgF359Fqm3rehOOZcv2YynXpaABSdXOA4DzzonkQgG3Nmv5HVV_f6U0nSO7Yex7gJpB-1OL0zMTNoWYVZlBaiNIoLvR2-mti9MzsSgvPuUrSrv2-yoAr_EK8JwiolrN2oZ69ktP9ZLUq6-JAGLAu_FdcJGh9PLrCQRXUMfWWeDqNV8IcnvNY-vl0tuMrbiuUoYnOvAJJLlNePDWXp4OFd6IILBeQJS63TgxwMseEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بندرعباس - پس از حمله آمریکا</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5925" target="_blank">📅 11:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5924">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">پذیرایی گرم از عراقچی این بار در عراق</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5924" target="_blank">📅 08:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5923">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
سپاه : به ۸۵ هدف مرتبط با آمریکا حمله کردیم.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5923" target="_blank">📅 07:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5922">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aada56b9e2.mp4?token=dG9nxZLyA4IDvW6gN6IvCu78iG5WYRB7x-whI4ZHFl1PS8YtyUf2Ai7mLdgIo-kkAhUCuwX3N1-kuFJ8eVrs95L2SSpjYpSmoV00xhj4DhSCWabwOfiX2BsGT7sgiE2ndX33IHwp1Gl5rPKoQgcjME-oAUHxo39ew3xJnUps6GEHzci0QPlfHwQF9qDEhuuWigxYTEIpSPVo23XgRdni4L7xB6O7zb5rEfBTrk4jAfEppZLbUT-nrURgaIqm2O2rA7HeTT-WNIlryY2bLwaDQoHjfYeNFXFfYFygaXe6Fyv0RTYp5B1_FaJQdnz9aSfvgb746aNuYrZ7Qci4wirjOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aada56b9e2.mp4?token=dG9nxZLyA4IDvW6gN6IvCu78iG5WYRB7x-whI4ZHFl1PS8YtyUf2Ai7mLdgIo-kkAhUCuwX3N1-kuFJ8eVrs95L2SSpjYpSmoV00xhj4DhSCWabwOfiX2BsGT7sgiE2ndX33IHwp1Gl5rPKoQgcjME-oAUHxo39ew3xJnUps6GEHzci0QPlfHwQF9qDEhuuWigxYTEIpSPVo23XgRdni4L7xB6O7zb5rEfBTrk4jAfEppZLbUT-nrURgaIqm2O2rA7HeTT-WNIlryY2bLwaDQoHjfYeNFXFfYFygaXe6Fyv0RTYp5B1_FaJQdnz9aSfvgb746aNuYrZ7Qci4wirjOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بندرعباس - امش</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5922" target="_blank">📅 04:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5921">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YPLPY0CZ9uClgWhz0QeUGlhNg49MHhn4rKyWV6HPCd5y-YoR5ogcIIx--IG30lsBh1PdTwA8dZ6ABzQUf2qIOsViMq0irB5eTj9tOouxJZHUD2x3OfoBo0l2Bz9NJYoJ_gVSO4fTLdG9W3vQEJ1ZfeS9JAYgJhDelyYga89ovjIKNU2YfliW0I1hq5c2_LSEn_kCyn2eNV4RLpVmmk6-mpFOq5PBiGIcAgz_FT4vn4imUlLU1RKatBfPF6IDInI1yXAwr2u5FdX2klyXcdg1SOksbkpk2ZRj_LXdwf1N9spAcGymZEm9ife2BE2amDdwRAWu20rml8dbj0X0mf69kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارش ها از شنیده شدن حداقل ۳ انفجار در بندر عباس
تصویری که گفته می‌شود آتش گرفتن یکی از قایق های تندرو سپاه است</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5921" target="_blank">📅 01:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5920">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا: نیروهای ما آغاز یک رشته حملات قدرتمند علیه ایران را آغاز کرده‌اند.
‏حملات آمریکا در واکنش به حملات ایران علیه سه کشتی تجاری است که در حال عبور از تنگه هرمز بودند.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5920" target="_blank">📅 00:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5919">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای چند انفجار در حوالی قشم و سیریک!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5919" target="_blank">📅 00:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5918">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f02faf66.mp4?token=S9RswPIx7M96lcymCLURjONV6oR7WU6TiRFYOzEX4CuKLNTaYwvm7yEB78E_WdqfsC-LlvxMTgYSeCVSqZIbFuxEjAcUBpfTLLViM4-ZNtZPQFFuZUSPxVOLz8FkRHMd1W2swL2BqADNZXNrJswtzudZ6XRf1C_Mp8G57UAU5qPf1uo3-HhhxePA9xnQSzVtojX0-Ca9q8qHQ_Hz9DCo3oNapzQTcEtMsx9m_HOTIHfS22TkVFFbtmQBNWMBRAKftlJfAeBAv65i5BP_rsqxa71qRNaxj-Bbfc9YkiO1vlMPqI4udoV99daO9Jj6FaACcLKl0ufLOYxdCgkK9pSWgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f02faf66.mp4?token=S9RswPIx7M96lcymCLURjONV6oR7WU6TiRFYOzEX4CuKLNTaYwvm7yEB78E_WdqfsC-LlvxMTgYSeCVSqZIbFuxEjAcUBpfTLLViM4-ZNtZPQFFuZUSPxVOLz8FkRHMd1W2swL2BqADNZXNrJswtzudZ6XRf1C_Mp8G57UAU5qPf1uo3-HhhxePA9xnQSzVtojX0-Ca9q8qHQ_Hz9DCo3oNapzQTcEtMsx9m_HOTIHfS22TkVFFbtmQBNWMBRAKftlJfAeBAv65i5BP_rsqxa71qRNaxj-Bbfc9YkiO1vlMPqI4udoV99daO9Jj6FaACcLKl0ufLOYxdCgkK9pSWgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی این ویدئو دقت کردید یه نفر رو به کامیون جنازه خامنه‌ای وصل کردن؟ :)</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5918" target="_blank">📅 00:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5917">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/skGaA0S1ItxmIGFK32JbccIik7cbcnOT8YD6vBNGsTJgsdWNZxeT3mhI_h0YIUWXG6onlIIR0GK3zgg148Eh4d-7zIxQE7_ZyGooOcJfK1NqVJeu-iy-b-DKuTz3P6GyNwxVLWXunOnQC-kigSPncZAHP86x9Js2TCM062G-bBRMl-8HHbGNDSde3-P6_U09DIgFAYMMYFzqbchOeMItwnbqODxfYPk_T-eX5HJMI6R5hiAVbDNBtYObPpa1CJfFIdLztgqZ4xau5tvORQXcBZwhGZB1zmsXoQTcbhc7s82wzJiDudkVKkXIYge09pDRkYgIeBYkdSq0uSGsTOry8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو حقیقتا یک سکانس تاریخیه، مدلی که دارند خودروی تابوت خامنه‌ای رو اسکورت میکنن :)  دارند جنازه خامنه‌ای رو‌ از جلوی خونه‌اش رد می‌کنن، از همین هم‌ پیروزی ساخته و‌ میگه چقدر قشنگه آقا خودش اومده به دیدن.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5917" target="_blank">📅 00:22 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
