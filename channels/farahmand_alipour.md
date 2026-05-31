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
<img src="https://cdn4.telesco.pe/file/Jz4z5M8k1pk9wKee8DeZy6w8rwrMfuafvIx5P5GLcaMxqFN4IIJDst0u_RsQC1ZPWs59w065FZ4Bq2ZRMmoj2x-MqrYyw8i4t5jXeS1i2GOC2Ixt4lKY8aXFJe6WPKl7lKqjewdocHRaCDbSidb0FN6N-Um0G_Yn3kZWDK3dl9Q5IsrAXCeoEzCllELzaxMDixKQuzPblSQYZp82QXI1m6VZFD-BWvIyH4Yanh1qm8slSe1ORS4h6IC6jS_yu2eN87xuK7s6t8RcVzKRjllR-YtwdkiHmi6EtMR8c708VAu6_gXN4CdpasAN10jMJdcEthw6wB6pClRJbCem8PQdqQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.2K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-10 22:11:35</div>
<hr>

<div class="tg-post" id="msg-5219">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gpy1JM5fwzJjJGWrKp-Q7z92eGk3OSmukfPNypFYhNW58uf2uFFjxK29nvFRhTcMgLUkLvHL8-2VQQxAih9r1YlvpdC-tV-vRbfjcpyVFfZ5k0FMW2XHMgoeUATlHuy4cZFF3fpV9mE3WZjk4RLFcuWZkDdgZs89tWdofTOskqgzd4EXniSM0gh7y4mfrr3HAIzW0SYk6am2zKVRuvzO64OL4greRiK6s4U1JMeWgPPrknYux72PLhmzfxeiixN5n2HqrbBWPtehxBqEBKA1zT5dd-WN4AxKSKTF0DaNxn7YdmAmoVdU2FmDm0hbKkRxmffEupG6pTPY99Od0KpV_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KOhBBYuoneVwKMxHPANxiEjP9jaZktLo3vZxVazHcK9li-O7iOWaLWXxrJqLm5RrRKPdsGbDDQKAA2o1oopnghuovtXFKfG-D75OWqMvLk44ad893VN-yajEFXil3lnDBq0efQbhnjoncW8GdsrUKrehOXGR85Ag9kWaBW6Rz9rkuLde4a4-2_VndJpmryRWDl-B5w_AQVH8xy1Rklj_K1XB-fn_lAQVN8AXD82WeMbRMkLaCrmS_wP6rBocpr3uHxCDZInbG7YgwPiB9sXb1CXxcQyGu1_5f9z1-Bamv74t5R3Kk9IPaP6p1dP3iEp9jtbnxTs6sRDwGU972mTBfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VdYHPuhZq-3_DC_K-fsLWy3y76dHzSe5aNTIfxQbxU_n5OTn2RVL9_3zsUY2lCljEnNKlHWSez2ATNo5N6XPWtRT4WWbcVbscW5mFiO_KUbbncrX0VP0ApMPLsmuAXFk7yU52bD4aeXAXBUwx9CZxbx_OmAcj8qmk8J2KFrtZ7yLzFhHVt_WUtrJxmXICM_zJ6pzDv1O6blQbU0wp_prl1iWI4VJmGHNx95NyTWwC7rA15wjeNMSss5hVv-9paHWl95xMR377-boNzoLDDhZKmTuU23ASoyodtVegyjBFeDztmL7n4C36colcu2LxYVA2-su1FsSntayau6lNVQL9w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یادتون رفته میخواستید برید
پشت سر خامنه‌ای در قدس نماز بخونید؟
که شما تاریخ خوندید نه؟
تاریخ جمال عبدالناصر و صدام و قذافی و بشار اسد رو لابد خونده بودید
که همین هوس‌ها رو داشتن!!!
و به همین نتایج هم رسیدن!</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farahmand_alipour/5219" target="_blank">📅 18:19 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5216">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b0siclmglcX21YxQDq0gz6PxSoDcpuHH9r8Mp9tbejNHBY8bPJxhPFO7F2Zlxg_X6XOFPu13MApuMMIXuwrrgtwZKPoRTYNCjg0MBdB4t6bYctWy9n-hkM5BjpT9B-7PrhXvMyqXt69kdFCFzUTcDsiXUdnTkAQ6WyB-fjutBuMvt_9T0t_Yv7eJiej40IeEH5ERtHn0cTFgH1bNunG1zvcjLHo3fQkwWMDI0xtUIu8NUk_LuIX5vvoItS53POF9fJn_qPKr3HPuwHYhU9drmSNJEhgNwOJGaoccgMmtxXB1QQxspiqqKwkNTBTQGJ6uyn7_TCjpecJ85uKcq39yqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nsRdiJ0pik7_sIxIw_8yaxBf0w-Jw7HU3updWbujd6NyztnsBNCl528m4pOpWIRB5HgbraDjqMRh6uuuP0gcVDW7f_IAagHZFjqhlKTNGYWpI-hnOdWf2_erxi_krgRqlrDjeAYcqM4He4xlBXSKSBFINb3V9auSuTt1mfC9ZGG0-0-dYkyM5P-DB8alG_MEeyXyeTV46Iv4R_3oadY3WzdTzRc4yMJliJ7vaAhah1PhEOzjqZrECmM2fKsjZYaO1b99auH1_WEtIK0Su_lv-Z_SLgzAsd4jYD4f5NHa0bBDxgAPIvELLjbj3huSAE_RJW_fAlpUltH1pUyo1AeXSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N6V9GavrQG6nzumLG598vdI7ibpWJCv5Hy11Ay0hguuQYQnM3ag9FTrzv5UuCU_G6_qhn-8RuXR9q4xf931OFOKiCsfdSr_WiYT9nf_IFGI7p6xJv3L8l0YkN-VB-8_wyrmJchSsA12fN2nwLJzzDD-ih3bOP8x0G9n9Wh2y_Kv3_WefEJ43Ov8FMLhSeF_jWsZSXCY-wFnoAHzVyDb0kDYvMfxeZ9EgIwoLYaoo0iQarrfKeJiWpc4id5vm9ZzACkFC3U2Eill9w2kjTH3P-Y43yV95C85thC3nUMVVojxIuPEiP6ONyvaijVwnlUyKGE29zJ0jsuMfQILPEL3QUg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رفسنجانی سالها پیش گفت من به خامنه‌ای گفتم پاسخ این همه ضررها در دشمنی با آمریکا رو شما به عهده میگیرید ؟؟ خامنه‌ای گفت بله! جواب خدا با من!!!  و خب این جنگ‌ها و تحریم‌ها و آسیب‌ها و کودکان میناب و... همه همون مسائلی است که خامنه‌ای گفته جواب خدا با من! یعنی…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/5216" target="_blank">📅 18:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5215">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db68225cef.mp4?token=q1zaCiCLK184XTAMOTnnm88m3eRKWFjXSS721j98HBGiQijyR1wAq3gfwBkQt0b0t2uBohP_wInAAoJAG-3sjAiVEYEGUOVa0Box78ysQeN9jlaGFafMHfoOuUeJZhyVzdGvzBT2PoL5obJE3M14x2QjESQtdANcMXbo97HGg0qoLU3ODxvZ5SnT6m4oUitLHS-Pb6TIEcCK2rpsxN_sOzXIlsD4Th8DWSvvBMzT9vtdeNzFkGNKPhdvitUkLVdMXCoH3g30tHfCe84u7XuD0zqpr-HssNDXevV32RL-bNaJTmWigtQOpHHW4HWS9sDTyu7NYsIvhnKG0QNkySmX7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db68225cef.mp4?token=q1zaCiCLK184XTAMOTnnm88m3eRKWFjXSS721j98HBGiQijyR1wAq3gfwBkQt0b0t2uBohP_wInAAoJAG-3sjAiVEYEGUOVa0Box78ysQeN9jlaGFafMHfoOuUeJZhyVzdGvzBT2PoL5obJE3M14x2QjESQtdANcMXbo97HGg0qoLU3ODxvZ5SnT6m4oUitLHS-Pb6TIEcCK2rpsxN_sOzXIlsD4Th8DWSvvBMzT9vtdeNzFkGNKPhdvitUkLVdMXCoH3g30tHfCe84u7XuD0zqpr-HssNDXevV32RL-bNaJTmWigtQOpHHW4HWS9sDTyu7NYsIvhnKG0QNkySmX7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی در تاریخ ۲۹ آبان ۱۴۰۴ در تلویزیون جمهوری اسلامی میگه ترامپ به ما نامه‌ای داده و صراحتا نوشته «دو گزینه بیشتر نیست» یا جنگ و خونریزی یا مذاکره مستقیم «برای از بین بردن غنی‌سازی و موشکی»  این مصاحبه چند ماه بعد از جنگ ۱۲ روزه بود! یعنی در آبان ماه، مشکلات…</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farahmand_alipour/5215" target="_blank">📅 18:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5214">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=EOdOSg05Yi5cZxi2gwHUr_1IXJFEqy1bJUTkxkgfTtqbLRj6uKXKzOei_vdKwY7AEX8YnJGF6HryUtqfJhjHs-mSC9hfU2Cg1hqPyfMr8CY_IYojtKy-nDsxVX_UiHLgIav9zK8gLz0G0oBDMLPmHBPLeBNiW665UNlxrXq7RtKyYraiSp4rMHXU5s1phltN--euve1lUb142br9Mc98qGARZD80HFK4c6p9st0rxLYgNtk-2a_q_wPLhRmltGTBOkY7Q7aZhA7WHLX3sbfVF6U_vDkClgViXtrbt54oO9jE5sd4w6cU3FAP0SQgEDLAYomVdyI-Y_0uOApN6GowoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=EOdOSg05Yi5cZxi2gwHUr_1IXJFEqy1bJUTkxkgfTtqbLRj6uKXKzOei_vdKwY7AEX8YnJGF6HryUtqfJhjHs-mSC9hfU2Cg1hqPyfMr8CY_IYojtKy-nDsxVX_UiHLgIav9zK8gLz0G0oBDMLPmHBPLeBNiW665UNlxrXq7RtKyYraiSp4rMHXU5s1phltN--euve1lUb142br9Mc98qGARZD80HFK4c6p9st0rxLYgNtk-2a_q_wPLhRmltGTBOkY7Q7aZhA7WHLX3sbfVF6U_vDkClgViXtrbt54oO9jE5sd4w6cU3FAP0SQgEDLAYomVdyI-Y_0uOApN6GowoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">می‌نشستن و  با نخوت وعده «دردسرها»  میدادن برای آمریکا و دنیا!  «حالا حالا دردسرها» خواهیم داشت!  بعد که جنگ شد تقصیر مردم ایرانه که تاریخ نخوندن!!!  تقصیر تلویزیون اینترنشناله!</div>
<div class="tg-footer">👁️ 186K · <a href="https://t.me/farahmand_alipour/5214" target="_blank">📅 17:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5213">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab893ceeae.mp4?token=XaGLMaH7Y33Ip_hysDM-olVUUcT8Y3rz43ETnqwlZxxVO8-EYTJ4aCfSdKh6R6CIRZ2QTPKEBCRJzCDYj8qkOiHDDJ6XGzO3QL5FvEJL-9wAwGQ5RDZ_1TEIzC9kkvJ6JENn2-Yd0ua1hu_QmQWLpz4tz9uHDpTmc1Hs2aeqCO9qTeYNwmZSzXq2DAqtJCygV2pmJUY2sVnCBAhx0SQIn4a-MJGiTcYCWaljo5cih6Vfl8N3eoqgrvtq1yqPJfGkd9Fn56SnxBWyEQfwAO9PmnrKgpxGNE4FPhkjHsDISguAQO01zLF8xAkEziuhIf29MeGPL2xnqF8deHRDXTjCYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab893ceeae.mp4?token=XaGLMaH7Y33Ip_hysDM-olVUUcT8Y3rz43ETnqwlZxxVO8-EYTJ4aCfSdKh6R6CIRZ2QTPKEBCRJzCDYj8qkOiHDDJ6XGzO3QL5FvEJL-9wAwGQ5RDZ_1TEIzC9kkvJ6JENn2-Yd0ua1hu_QmQWLpz4tz9uHDpTmc1Hs2aeqCO9qTeYNwmZSzXq2DAqtJCygV2pmJUY2sVnCBAhx0SQIn4a-MJGiTcYCWaljo5cih6Vfl8N3eoqgrvtq1yqPJfGkd9Fn56SnxBWyEQfwAO9PmnrKgpxGNE4FPhkjHsDISguAQO01zLF8xAkEziuhIf29MeGPL2xnqF8deHRDXTjCYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بله جنگ ۴۰ روزه به خاطر ایران اینترنشنال بود و دیاسپورای ایرانی! جنگ ۱۲ روزه هم تقصیر افغانستانی‌های ساکن ایران بود!!! یادمون هست!  فقط فعالیت هسته‌ای و موشکی و نیابتی‌های جمهوری اسلامی و ۴۷ سال سیاست آمریکا ستیزی و دنبال نابودی اسرائیل بودن ، بی ایراد هستن…</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farahmand_alipour/5213" target="_blank">📅 17:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5212">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7hEb1Ixi08niB3wUx3nUshwrLU6Dig8Ppg2KZdrTHIytZ7fAoNCNo2oH4eKJJJZYJ90AjPbqMX1vLrtxaWCC5tA6am7bOq7NqI1eGiRgJyT2rM7zomxz3abH5d_OtAilUIsGJiNYm2ITDnpge2s8HjSDDKPoxzRc4owzGHjOHK9tQbYNyTerkNCO4L1XDEYJQD9fR9XuYoaoKf6BCkBGL77XM2WtjAEqcOwV9NBMCbkyEzjPsochity-OFvTpCxdtcOUBxrH4xVb_MVqKl0qeAsGO_fIj9eCwNjMXLsp64ZOal9OuqvNCR9CN2WTnbAnwJBstEt4Ai1hjdTlFT-rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بله جنگ ۴۰ روزه به خاطر ایران اینترنشنال بود و دیاسپورای ایرانی!
جنگ ۱۲ روزه هم تقصیر افغانستانی‌های ساکن ایران بود!!! یادمون هست!
فقط فعالیت هسته‌ای و موشکی و نیابتی‌های جمهوری اسلامی و ۴۷ سال سیاست آمریکا ستیزی و دنبال نابودی اسرائیل بودن ،
بی ایراد هستن و مشکلی ندارن!
و همونطور که می‌بینید روی میز مذاکرات هم بحث ایران اینترنشناله و افغانستانی‌های ساکن ایران و دیاسپورا! مشکلات و دعوا سر اینهاست!
خوش به حال آخوند که چون شمایانی رو داره! هر بلایی که سرتون ببره، آغوش گرم آخوند رو رها نمی‌کنید!
شما اگه تاریخ خونده بودید راه شوروی و کره‌شمالی رو نمی‌رفتید! راه
صدام و بشار اسد رو نمی‌رفتید و چندین هزار نفر رو دو شب قتل عام نمی‌کردید! بی‌آبروهای تاریخ!</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farahmand_alipour/5212" target="_blank">📅 17:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5211">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HmKdX7iAAV_0FbKT80yAN7DArHTlFDRi2T7Si355aHREG03VFU6YTttO3tgxQa4A30MvuBPVqNWFLoY-cD8zfNSrw1wYSuMG2wI45ND5qrlReDh_gGJoGh2I65w5V20q1bCOoR_VmMm1ER5GW_Cz8fNjUTXCNgx7NLBsgfecrMysgv408tvMLERo51bVS51lJEdIwLWOManVCa6Xf-JCX5KFu7Kwxd3c-uqqtV7Wu1tMCc8xMEbIeydTCCkT2a6FNFsaueQShwzSn8sdrRJdiezxEF4eob7HU7JHonWozfdjoR32dBdaEJf1Q31pmbC8eF9zXCt5rmxwDrlG6U2udQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بله جنگ  ۴۰ روزه به خاطر ایران اینترنشال بود و‌ دیاسپورای ایرانی!
جنگ ۱۲ روزه هم تقصیر افغانستانی‌های
ساکن ایران بود!!! یادمون هست!
فقط فعالیت هسته‌ای و موشکی و نیابتی‌های
جمهوری اسلامی  و ۴۷ سال آمریکا ستیزی و دنبال نابودی اسرائیل بودن ،
بی ایراد هستن و مشکلی ندارن!
و همونطور که می‌بینید روی میز مذاکرات
هم بحث ایران اینترنشناله و افغانستانی‌های ساکن ایران و دیاسپورا! مشکلات سر اینهاست!
خوش به حال  آخوند که چون شمایانی رو داره!
هر بلایی که سرتون ببره،
آغوش گرم آخوند رو رها نمی‌کنید!
شما اگه تاریخ خونده بودید راه شوروی
و کره شمالی رو نمی‌رفتید! راه صدام و بشار اسد رو نمی‌رفتید و چندین هزار نفر رو دو شب قتل عام نمی‌کردید! بی‌آبروهای تاریخ!</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/5211" target="_blank">📅 17:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5210">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KmIvLdkJtJ-H4ashSsXFRPIF2CkWhQsvVcP72lPeieY88PM3NITPXi_o5ftMjwS0DAEThjv4hrDjv7-mBOIPN6xOENUH2SIVs5LRnBb2y510ZDXWul07shbE8j7h_46PJUWbZdC7NlKcKNGjiVqq9YsynGehqkp2LjVyzukxyu9P9fmE5sefN60AVu2SUx38mq6O-JzeKJIqZxAVxpIIyR4Z8DloYWRAuSn4W6z84JtzUZtf832B8MpJXLHq87KBTooL4t61EtXtSC9-weuyK6Bz1I5go74PyCH4oUO4P71WgyPftKVlHwvmmb0R8srtWUl4-gpXBbdiKLrMaIka3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما:  آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده   ‏۱. آمریکا متعهد به عدم تجاوز به ایران شده  ‏۲. استمرار کنترل ایران بر تنگه هرمز ‏۳.پذیرش غنی سازی ‏۴.رفع همه تحریم های اولیه  ‏۵.رفع همه تحریم های ثانویه ‏۶.خاتمه تمامی قطعنامه های شورای امنیت  ‏۷.خاتمه…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/5210" target="_blank">📅 15:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5209">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3y5v9TVPX2Z6WqVIxW4dEikujMlxZ4gzAzRPSL3sRovpP2nrg_baDiavHpTCk-MfmZSKScdh-Nm73PYUbZfzg5sanuSn7zoMriKDP7Lx8tor8VZnl5HOeAl5Wxpn_BImobCzgi5PW33XDJDwdwC1Q2oKBgMQjfE8eqLSNHLLuH9XviY3AACVBk8rwcmwgDZPReky2rQ9lqbAOk7aBpJvzr-57J-MgaAaO2bBaDTCY3sfFevBvbUprbJ8qB8z_arJi-t5GhtQx8MLIPWptVCzgpLFVUrdaKRFpwCaHtJwKJKdyEod4BEvsOmgXCpQDMBcxHw1R2qQQc1MzVZZB4lIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل قلعه شقیق در جنوب لبنان
را تصرف کرد، این مهم‌ترین پیشروی ارتش اسرائیل در جنوب لبنان از سال ۲۰۰۰ میلادی است!
گروه تروریستی حزب‌الله لبنان،
بدون اجازه گرفتن از دولت و مجلس و ارتش لبنان و در خونخواهی خامنه‌ای،
به اسرائیل حمله کردند، اسرائیل نیز در پاسخ دست به حمله گسترده به مناطق شیعه‌نشین لبنان زد، بیش از دو ماه است که حدود یک میلیون شیعه لبنانی آواره شده‌اند! بیش از سه هزار تن کشته شدند!
چند هفته پیش دولت لبنان قصد مداخله داشت و تلاش برای «آتش‌بس» اما این گروه تروریستی و حامیانش مخالفت کردند و گفتند که جمهوری اسلامی باید این آتش‌بس را برای ما بیاورد!
(که بعد تبلیغ کنن قدرت ج‌ا بود)
جمهوری اسلامی نیز توقف در جنگ لبنان را در صدر خواسته‌های خود از دولت ترامپ قرار داده ولی هنوز به تفاهم با آمریکا نرسیده و اسرائیل هم داره کار رو ادامه میده!</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5209" target="_blank">📅 12:09 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5208">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c1b13d62.mp4?token=E00oJc9EyoqeLC8pfYKtV7GnU1PjpfQp52NStzGDesMeiWRzN31ZvuScumaLQpGr4kjo-r1mw_837f_Qhfk-pHVmgCsJRIY0ailiHVVcFBs7lgeJlfftf3-RHCGTnTbjeZfs_QVX1V8UprIHo7bXX0uDYqO1rFIY7hraDdrAQROLJx2Xt5IPa-B9vpTfJNdVjKko4vog43KaVpCF69MhVTq1FoYEBvwUPwjUAxJ4auP0e8hM0C7iDDRjyaPjLh2mZuG1RNi_KCtaBF0mdpo_im99niOO6M9BO3K0U07_l82wazuhdTjljbZeQ-otnpBpTp8qhWxokt_MypraXaXy0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c1b13d62.mp4?token=E00oJc9EyoqeLC8pfYKtV7GnU1PjpfQp52NStzGDesMeiWRzN31ZvuScumaLQpGr4kjo-r1mw_837f_Qhfk-pHVmgCsJRIY0ailiHVVcFBs7lgeJlfftf3-RHCGTnTbjeZfs_QVX1V8UprIHo7bXX0uDYqO1rFIY7hraDdrAQROLJx2Xt5IPa-B9vpTfJNdVjKko4vog43KaVpCF69MhVTq1FoYEBvwUPwjUAxJ4auP0e8hM0C7iDDRjyaPjLh2mZuG1RNi_KCtaBF0mdpo_im99niOO6M9BO3K0U07_l82wazuhdTjljbZeQ-otnpBpTp8qhWxokt_MypraXaXy0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امیرمحمد شاه‌کرمی، نوجوان ۱۴ ساله، ۱۸ دی در جریان اعتراضات شهر قدس بازداشت و پس از ۶۰ روز پیکرش تحویل خانواده داده شد.
امیرمحمد ۱۸ دی‌ در اعتراضات ناپدید شد. خانواده‌اش به بیمارستان‌ها، سردخانه‌ها و پزشکی قانونی مراجعه کردند، اما هیچ اثری از او نیافتنند.
پس از دو روز و در ۲۰ دی، تلفن همراهش روشن شد و ماموران حکومتی از این طریق به خانواده اعلام کردند که امیرمحمد زنده است.
خانواده پس از این خبر، پیگیری‌های بیشتری در دادگستری انجام دادند و آنجا نیز به آنها اطمینان داده شد که پسرشان زنده است و حتی برایش حکم صادر شده است.
امیرمحمد دانش‌آموز مقطع هشتم بود و خانواده تلاش کرد از طریق آموزش و پرورش نیز این موضوع را پیگیری کند، اما در آنجا نیز با پاسخ‌هایی مبهم و با برچسب «پرونده محرمانه» روبه‌رو شد.
این بلاتکلیفی و بی‌خبری تا ۶۰ روز ادامه داشت؛ تا اینکه در نهایت پزشکی قانونی با خانواده تماس گرفت و اعلام کرد پیکر امیرمحمد شناسایی شده است.
پیکر این نوجوان با کد «ناشناس ۱۱۷۵۴» به خانواده تحویل داده شد.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5208" target="_blank">📅 10:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5207">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8afd0458a0.mp4?token=PZmA0qixw3GXghrdp2s000s7a6LSVAqQUa3ldb31z5FMDSO3EDpsyiwc76x11s5kVRoMjxbR5RDhPwspb2ssgu3Cq-w-0Q2d1Ne70Y982JLBrN8rdh5B5Eh0fm4C1dM6oblpXWaNIaix2Wg3oVzcRa_eVLb_BkVJyXh2qTlwXtwxSVSTnjep5JuJIaMtOKYpmFB-KIqBguNMugCvByApIo5r_QGZA35M7Km8-wUDOOESvnILvS_bD-SNFFbHTWGIPDRzwrPjUGifpViqSstLDYwZhDeaWkiTJ0RrL-K39ZP4lApWf94WItct6jLNdgR_xe8ceOK4Nbs8_kd6w58N4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8afd0458a0.mp4?token=PZmA0qixw3GXghrdp2s000s7a6LSVAqQUa3ldb31z5FMDSO3EDpsyiwc76x11s5kVRoMjxbR5RDhPwspb2ssgu3Cq-w-0Q2d1Ne70Y982JLBrN8rdh5B5Eh0fm4C1dM6oblpXWaNIaix2Wg3oVzcRa_eVLb_BkVJyXh2qTlwXtwxSVSTnjep5JuJIaMtOKYpmFB-KIqBguNMugCvByApIo5r_QGZA35M7Km8-wUDOOESvnILvS_bD-SNFFbHTWGIPDRzwrPjUGifpViqSstLDYwZhDeaWkiTJ0RrL-K39ZP4lApWf94WItct6jLNdgR_xe8ceOK4Nbs8_kd6w58N4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔈
🚨
چرا خامنه‌ای در پناهگاه نبود ؟  چرا خانواده ، چرا فرماندهان؟  چون «اطمینان داده بودن که کار نظامی در این چند روز صورت نمی‌گیره و اتفاقی نمی‌افته لذا شرایط عادی در بیت بوده»  صدای ناصر رفیعی</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5207" target="_blank">📅 18:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5206">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LRqi7Lfn_3lGj7QiqiQ_tX63UhxMLubkf4GHEN_vQrhKl46xrZcHPaOoC4VzH5cENbTIqrbK38mmnGeonjTOzPniZfk_Kk5JjqFtFnBEMIKFd698FHP3rFqYDnXnn_pCLjiFrhmOc3S60dgJkFtRB2UOb6ZugDbml9BOVBa5sKXSRR6zMNWOz7PiCwVAmZ4kuvqCFhEzDQR4uLIY4J7uhMI8Y7bVOy7YuwsF5uFABnTRVtgncdQ0nQSRBd33Zc6xpGxj6c9TZMKrNYUCmi1dlZhEK8vwjY6TYtj1gJOH2q0SZlOQSsTbqKBA06BAJmW2wCsjudviSNyO-QrgULKT2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی با آب و تاب می‌گفت
به امارات حمله موشکی و پهپادی کرده،
حملاتی که ۹۵ درصدشون توسط
سیستم دفاعی امارات خنثی میشدن!
اما امارات در عوض پنهانی با جنگنده‌هاش
حمله می‌کرد و جمهوری اسلامی هیچ سیستم تدافعی نداشت!
یعنی اگه به ایران ۱۰۰ جنگنده، یا ۱۰۰ موشک حمله می‌کرد، میشه با اطمینان گفت ۹۹٪ ماموریتشون
رو انجام میدادن و اهدافشون رو میزدن!
کما اینکه اسرائیل ۸۵۰۰ سورتی پرواز در آسمان ایران انجام داد حتی یک هواپیماش آسیبی ندید.
آمریکا هم ۱۳ هزار سورتی پرواز انجام داد.
آمریکا همچنین ۱۰۰۰ موشک تاهاماک به ایران شلیک کرد، جمهوری اسلامی قادر نبود حتی جلوی یکی از اونها رو بگیره! یک در هزار رو هم‌ نتونست!
جنگ با امارات رو جمهوری اسلامی کلید زد
و هنوز هم کامل مشخص نشده چه آسیب‌هایی
ایران در این جنگ متحمل شده!</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5206" target="_blank">📅 10:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5204">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JfITlRtSvEC1OTDiV05ti9nTfEYIO9cYxBjfQwRK3riRC94lDbYdwsYofNbbXMiCSj3uQw21iP0d3Ae49X3tANRTh59CIbr8F9mKM2ntMTgckdMBfeljAmFPvuzbas3ZiY-15yCcaPexG2ZusPMui8dd3EKpi1k5As6v7rKXcCy2LpWHxDmNrDRqfqL8E_6jT9jy5c_sVSOfNL1O822V418o8HjXFXXSE5z1nVw5oaRe73oaIJyTa1YXr_HMdsA-oaozHUoMC9U0s6_mnsqGQ_TJMKn2apRR-aF8ylvknOidlkVTV4x8H3yna-bpb-33rW_VOf2tU1-dSvL6s3J02A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5204" target="_blank">📅 21:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5203">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ktitNWd3wDwak0i69ADFOKa0_LNXoHkK6xNlih4CpD-xRsBBN5VGjwvK2OzBatUjHEzkobf3pgLUWfxVan0NxWs2Iw4DOdUMYM891um2wLYWwcWIr25EssKPrS8nIGWT3hFU6unqQBsxqukKRCMTVFU_7s9lax1nJym0wxLK57NZKlFGfo07mrVU3QCW4A3OgMYOKRrJdQm3io6D2CX_mPEmKHEJizE_EyzWLJLnTdUFqJ8VVb5HmOXqvaJc-ohsf4ZD4ny6qC229NDkoSJzyyjuOQ2x6bG8aSSBGfI6CeKvzkknzIFJ1hlOBcPKupifBmyh38h-tAp83n6Wc56rcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5203" target="_blank">📅 18:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5202">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rz7-hdDg05ACcILAJpq9f2S0v8TloebV5oicX_UtZmhp3uTKUS88N4wGgxNCm3QRMyX5ZG-JMlgTCOXFgGQFW6wZ2QhmVRZobfNELiHgSMFrmWVZGOcNtVyBDvuwZLXID3BSRLexHkoCl67zgS_DYjfhTypkq12PgELf2z-dj73ILKElnmPPDqtlEvi2d4lc6EtwYQXJ1B66vu5K0ArAk9IsDGNKXtyQMIgeeBFseOVQDPbXV9leu9l_njEye69f5ORmVi7IL3QyBMzrdd5drtv3ipf-YEJ_7FoZs96fjEiLnJdEpOrqQ7tZNxdCcXs-4a0bjTyp89gPKeKff6tYAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمادگی بهتر برای جنگ بعدی …</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5202" target="_blank">📅 18:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5201">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : برای اتخاذ تصمیم نهایی اکنون به اتاق وضعیت می‌روم.
«ایران باید موافقت کند که هرگز به سلاح یا بمب هسته‌ای دست نخواهد یافت.
تنگه هرمز باید فوراً باز شود؛ بدون دریافت هیچ‌گونه عوارض یا هزینه‌ای، و رفت‌وآمد کشتی‌ها در هر دو جهت به‌صورت آزاد و بدون محدودیت انجام گیرد.
تمام مین‌های دریایی (بمب‌ها)، در صورت وجود، باید از بین برده شوند. ما با استفاده از تجهیزات پیشرفته مین‌روب زیرآبی خود، تعداد زیادی از این مین‌ها را از طریق انفجار نابود کرده‌ایم. ایران نیز باید فوراً هر مین باقی‌مانده را جمع‌آوری یا منفجر کند؛ البته تعداد آن‌ها زیاد نخواهد بود.
کشتی‌هایی که به دلیل محاصره دریایی بی‌سابقه و فوق‌العاده ما در تنگه متوقف شده‌اند ــ محاصره‌ای که اکنون لغو خواهد شد ــ می‌توانند روند بازگشت به خانه را آغاز کنند!
از طرف من، رئیس‌جمهور محبوبتان، به همسران، شوهران، پدر و مادرها و خانواده‌هایتان سلام برسانید!
مواد غنی‌شده‌ای که گاهی از آن با عنوان «غبار هسته‌ای» یاد می‌شود و در اعماق زمین دفن شده‌اند ــ زیر کوه‌هایی که تقریباً در نتیجه حمله قدرتمند بمب‌افکن‌های B-2 ما در ۱۱ ماه پیش فروریخته‌اند ــ توسط ایالات متحده از زیر زمین بیرون آورده خواهند شد. (طبق توافق، تنها آمریکا و چین توانایی فنی انجام چنین کاری را دارند.)
این عملیات با هماهنگی نزدیک جمهوری اسلامی ایران و همچنین آژانس بین‌المللی انرژی اتمی انجام خواهد شد و این مواد به طور کامل نابود خواهند شد.
تا اطلاع ثانوی هیچ پولی میان طرف‌ها رد و بدل نخواهد شد.
در مورد سایر موضوعات ــ که اهمیت بسیار کمتری دارند ــ نیز توافق حاصل شده است.
اکنون برای اتخاذ تصمیم نهایی به اتاق وضعیت می‌روم.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5201" target="_blank">📅 18:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5199">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hqr54aAzkFoRusYSy_L-Xs8xNF6AoktHWTR9dPAHUWtsYbW7YV75SLvqhct9W-7TaTY9Zo0opBZUSzWWDQTjm5-tpZyUz5AR1Jdpm-E8axcCz_vxj1ybp_Snw4r6OONlru90l4ggKBK4KbYgi2KrYEm0JGz5D9d3tYjSnajdRJOwoxwR6Aqaql0sundYQm-pG0z4mJtyEx0MINq79lRf34fFdSgDwPblle8wmMYnpotXKxE9nrgv5OPx7byxtj6xE0Waf0bM3Nlwq2JbDwrxP70fFbHaD8k5Iv7y326w1sYloMZJ50up3YOOPK3jXYS_zexbh81tLbwBmMHu9wEApg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iQdBjxvSnT66oHoSnBNA7kuOP8hspYtKc_r_V_Qu1lX6u13gxzL38Unth0hL6w4SwJmRcTtNo7rvImyBYupSwQHw4KBHvfwlXeub9OsvEvQ-jFsWQv0QAoDgyL2hdxe4DXz9Qd1p9xetBT-m1iuy80w3udbw5RYNmn8Y6NSvXJr8H363OnY4gS9mz1puavsoLPVLJlA-22iBIeJHHfG9xdUiRyqlNyHkWdPWMW8LaKJKTjSqowe220O2WM8DwPytne9w2saZmejg_BsIN33k8-pFmk8fo529BSMl7-afjU9cE8PzErrq9qTprRYilRRoC4h4GMHASXkdVzWod5GAeA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
لبنان سفیر جمهوری اسلامی رو اخراج کرد!
گفت «عنصر نامطلوبه»! گفت که جمهوری اسلامی عامل وقوع جنگ در لبنان شده و جنگ
رو به مردم لبنان تحمیل کرده.
اما سفیر جمهوری اسلامی در درون سفارت خانه موند و گفت برنمیگردم ایران!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5199" target="_blank">📅 18:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5197">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hhc1aWzUQRJdfj0-WfndOfmYzVmt147o45tLgLB08jclml1NZc7zHAJhLehiOiFaetT2SJhbtLKZV8C8mw2NkM8nS0qoAINOR_vVaqRns4Xl76Q26cLyZxdmtLox-tKzOdyCfgJSnhPIqq9_mTHjuBrF_f2uiSsI5LtCZb9b3hFAcAC0cnheaJxtpuX66aD5aUlLcCTobjJu9tNNdRbpvY68OoBQLog_9tRb7SwYWqKAsCkDWN7sX3KgD5bMAlXC0ex71RYlOI_4HDmGDJ_U7Jn2A98CLzf3fnad28w_UgMitCuDT_Rgc19EEiw4UOoevy4JWwv2mcDD7KZP-fLZ9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IO4kxTIhVqM01uSr7lIBeInmvB5BeueaFBh6_9oCHGbSHr2x4FmZqWBcBdsoAn1etahf4Kj8DseEHpOhKnsCzz3ZuTW6-0bnopucmkEBAmqdvXvOvDxBzFeqg6rIj212tSKkh2-oYQ4fEPETIggca6bR4isU6SE9xBOGlrm0-jkOajBZNzbkO0XSm0JpA8YA5dif_S9ESBptg3KmNLT59HDQBADa_cz7GpXZ_nfEKlK6hfTp__dkYXZs2D9QkY1mmRI_rFmIbnGaz_OIoZ6dwTT2QTvPDEUJp-6_GOFNvqsxnykL5034QmvtD-Gzj0GCI3k7hzt_xhA_J6ClPlifgg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
درسته هر شب توی خیابون‌ها بزن و برقص و عروسی داشتن اما در افغانستان گدایی پول میکردن :)
سفارت جمهوری اسلامی در کابل در اواخر اسفندماه رسما تقاضا کرد که  مردم افغانستان به جمهوری اسلامی کمک مالی کنن!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5197" target="_blank">📅 13:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5196">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=I81f2bR_GB3gLOWawG_7D6qWLjaM0hi2nxu3yM-fv6kK5E4S0R1-j2eKTa9pobkDUgy5huvPulz9DWgCC8NIamHUuG1y32jtlsixa0WNYHB8bU3NWwi7Zu3KRJi58kCU6BMlfxOIiANXBoychQGyP65aLE7aiODWCXmbE63g0IVBs_nc7W0uuqS3uuD1hPYUr6cUH87hc6PsWz88NbHBEnlFtnDKq91aiZvecTm98Vh_2FZcA0Esh4S9T5KGwOSER_VmcoPmKAMhFFpdqtm6mqeXt0H_u2ihDseLa_0gfUQbr_xsq0RaTKrRCgKiyHEog8lrQj4A17HpIGby8p5EvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=I81f2bR_GB3gLOWawG_7D6qWLjaM0hi2nxu3yM-fv6kK5E4S0R1-j2eKTa9pobkDUgy5huvPulz9DWgCC8NIamHUuG1y32jtlsixa0WNYHB8bU3NWwi7Zu3KRJi58kCU6BMlfxOIiANXBoychQGyP65aLE7aiODWCXmbE63g0IVBs_nc7W0uuqS3uuD1hPYUr6cUH87hc6PsWz88NbHBEnlFtnDKq91aiZvecTm98Vh_2FZcA0Esh4S9T5KGwOSER_VmcoPmKAMhFFpdqtm6mqeXt0H_u2ihDseLa_0gfUQbr_xsq0RaTKrRCgKiyHEog8lrQj4A17HpIGby8p5EvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی شما نبودید در اجتماعات حکومتی شون هر شب عروسی داشتن!  «صیغه یک ماهه»! در برابر «یک سکه» :)  با کسب اجازه از امام زمان</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5196" target="_blank">📅 13:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5195">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f5663381.mp4?token=n5gOWGxUx-PX0TooQROhD7aS02-bZyywQ-hPXmn4Du23qt1vBHw8HpZKconEKGArMZLNLI0sNf9RpeP_dZu6gw9z_n6Ay_-VJVUT6qz3qigohL3KAUq7w1KPqqwUC1UaG7pEogDIGfmme1qlktn6Y5FHXKTGUWP5d1ERC7LIeI2PEyGHmcjvTnTpw_cSpNbdD8KjHM_YoeMRWLICunliKWQVkRKs0AKxL0RPMJKnUxvVYY3OCk5wb6fp1iYF7M8JN9-Oix8voX3k_4VCzpEULEMkV6yDJ7aMqadNjLqc74r1uypGpD_DWtsbhdfw9jgabn8goE79AHK0DPRCcReKbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f5663381.mp4?token=n5gOWGxUx-PX0TooQROhD7aS02-bZyywQ-hPXmn4Du23qt1vBHw8HpZKconEKGArMZLNLI0sNf9RpeP_dZu6gw9z_n6Ay_-VJVUT6qz3qigohL3KAUq7w1KPqqwUC1UaG7pEogDIGfmme1qlktn6Y5FHXKTGUWP5d1ERC7LIeI2PEyGHmcjvTnTpw_cSpNbdD8KjHM_YoeMRWLICunliKWQVkRKs0AKxL0RPMJKnUxvVYY3OCk5wb6fp1iYF7M8JN9-Oix8voX3k_4VCzpEULEMkV6yDJ7aMqadNjLqc74r1uypGpD_DWtsbhdfw9jgabn8goE79AHK0DPRCcReKbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی شما نبودید
در اجتماعات حکومتی شون
هر شب عروسی داشتن!
«صیغه یک ماهه»! در برابر «یک سکه» :)
با کسب اجازه از امام زمان</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5195" target="_blank">📅 13:18 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5194">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">وقتی شما نبودید پوتین پیام تبریک برای مجتبی خامنه‌ای به عنوان رهبر جدید جمهوری اسلامی فرستاد،  پیام پوتین حتی قبل از پیام گروه تروریستی حزب‌الله لبنان صادر شد!  حتی زودتر از پیام‌ شهردار تهران!  حتی زودتر از پیام جوادی آملی :)   پوتین در پیامش نوشته بود :…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5194" target="_blank">📅 13:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5192">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tQahXi5lC0w-fJzYAUXU4wn3sfrmCUhx_7RwQeVUsskltcvZ2oZq9uLhmZYSrglsMbdBTvrjFrN__heju8NjrbGU5mUEn9H2zjY-v6Fny5iXPQhzD2RnOyF9YEhZ-G3WooBqMGo-a7g19R4fYTktyQVwrhrIk8KlP1CxxYxpTySe7WH4Tm8tkTGCHitQkXjN15zu0pPqgutlOURd-8Ht3LSHcGp-_IaKuXyo6JojvY5ubPf2GyBCvWvdMW5IiUPuKxcx1ibzZ64folw2e6D_S_t-oA-e2VuiymFOlvrpaN0Ak6ceugvspO3mOk5CGknmTeae4hUS-g4ZbKGkdSbkHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lc93j-ZuO-EtJxgHrAdzHDEX6WPZ76dUW83HRmW8dxgX3uT_qGT9jQdIs0638ovkAUyqeGw0PBQOZrUa3f7jgZTxBNJ1o8nDmpFHMI-iuXbQomQ5fNR1LbGgBDnzleiVIw0sZnOXVsbCq3uIz9a_O09rHPX_BhksEmMMRpQ893oVAQRK7GTJ9kq8tDMCkIeSDKk3-UGw5-BaWGy6A0MCtRss7OsJdUMYUGXjErBBOvqnV6yJe2nvt-Rn8s-u_f3ZIivyecmn9kDUmMYd4zDhUr1gS0egQW5yLDyc3M6aen1T4LQ0qOg05iBJ8VnFGa2M38h7AhedJk1kxom0jd2SMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
پوتین پیام تبریک برای مجتبی خامنه‌ای به عنوان رهبر جدید جمهوری اسلامی فرستاد،
پیام پوتین حتی قبل از پیام گروه تروریستی حزب‌الله لبنان صادر شد!
حتی زودتر از پیام‌ شهردار تهران!
حتی زودتر از پیام جوادی آملی :)
پوتین در پیامش نوشته بود :
«اطمینان دارم شما راه پدرتان
را با افتخار ادامه خواهید داد.»
پوتین راه پدر مجتبی خامنه‌ای رو دوست داره :)</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5192" target="_blank">📅 12:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5191">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9993037d5c.mp4?token=poSHuVAd1CZG5uWf-hIBPfFqsEacdMBm7EJnoQHnT_W3eUDiPyJWMKmx3e5R9viGZloV3mcfNZyKBlLhvZstYVPB3tm-SMkwn0sCNHvdYo4BciveXPTHhUDiY3d67W6317UlDhr_qtnSr3VLaxcmEHtUc-zkv734ssJqIMVTCDKiudAvV4qVJiGtLjJYx1iwhAwFrGzxsujZgXtrYInFPp2-Sb9Dvo-nX1HLSmdwdqPhe58F8W1Nsp9LmmjoCVfFi0BSs2B4LiZp0S1MDN7-eUdoEwZA_eTbb7V8AISK9vhbL8hyj_LIzue-lxFxelZIRGl3I6NWVnBurIYFZh1Cfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9993037d5c.mp4?token=poSHuVAd1CZG5uWf-hIBPfFqsEacdMBm7EJnoQHnT_W3eUDiPyJWMKmx3e5R9viGZloV3mcfNZyKBlLhvZstYVPB3tm-SMkwn0sCNHvdYo4BciveXPTHhUDiY3d67W6317UlDhr_qtnSr3VLaxcmEHtUc-zkv734ssJqIMVTCDKiudAvV4qVJiGtLjJYx1iwhAwFrGzxsujZgXtrYInFPp2-Sb9Dvo-nX1HLSmdwdqPhe58F8W1Nsp9LmmjoCVfFi0BSs2B4LiZp0S1MDN7-eUdoEwZA_eTbb7V8AISK9vhbL8hyj_LIzue-lxFxelZIRGl3I6NWVnBurIYFZh1Cfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شادی مردم مشهد از خبر کشته شدن خامنه‌ای</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5191" target="_blank">📅 12:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5190">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTHPGofyWvmF0gfxDpgXQxV8R6rSBD2gL5ciJpbyWa-WDfIX6pATnSzlVpz798J0dEDue9RvM14AyY4ns4ScA_Lu1obO6IkuHBl_6uj5GJhNN0mfGuo1v7_U6JaIXtPCALqL9CL1iWxyhocVgULls4Ld99P4pRHzqlF0h4GijLcbdpdqghkSs8a83vEO2LW5pFW_U-KAJ8PuP-4ytkhDnnrt4f_AO7dhZjdssc4vsbbW7ME9kufSQ7VHTcF1cF78tQotLGHM9YDpKKGKwgkuPVkLZ62C53Nkl_kHsuDgp086qIRBksCEceasuLS3ODC_kzyPukFAOm31JRFzEiXDxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نکته جالب :)  امروز ۲۶ روز پس از کشته شدن خامنه‌ای  در کره شمالی هنوز خبر کشته شدن خامنه‌ای منتشر نشده!  فقط اعلام شد که مجتبی خامنه‌ای،  پسرش جایگزین او شده،  اما اعلام نشده که در طی یک حمله نظامی  خامنه‌ای کشته‌ شده.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5190" target="_blank">📅 11:09 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5189">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‏حالا که تشریف آوردید:
‏از ۵۷ کشور اسلامی، فقط ۸ دولت کشته شدن «ولی امر مسلمین» رو تسلیت گفتن و ۴۹ کشور سکوت کردن!
‏عراق، آذربایجان، تاجیکستان، پاکستان، لبنان، الجزایر، عمان و قطر تنها کشورهایی بودند که تسلیت گفتند.
‏بزرگان جهان اسلام چون‌: ترکیه، عربستان، اندونزی، مصر، مالزی،ازبکستان و… سکوت کردن!
‏تروریست‌های طالبان هم حمله رو محکوم کردن اما تسلیت نگفتن!
دولت فلسطین حتی حمله رو هم‌ محکوم نکرد! سکوت کامل!
فقط تروریست‌های حماس محکوم کردن و تسلیت گفتن!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5189" target="_blank">📅 11:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5188">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
🚨
امروز : کشته شدن ۱۴ نیر‌وی سپاه زنجان بر اثر انفجار مهمات عمل‌نکرده</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5188" target="_blank">📅 10:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5187">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های جمهوری اسلامی  از بستن تنگه هرمز خبر می‌دهند.
🚨
🚨
🚨
سخنگوی قرارگاه خاتم : به ۱۴ پایگاه نظامی آمریکا حمله کردیم و «صدها» ‌تن آمریکایی و اسرائیلی را کشته‌ایم.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5187" target="_blank">📅 10:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5186">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">پایکوبی مردم در تهران</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5186" target="_blank">📅 10:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5185">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔺
شادی مردم ایران از شنیدن  خبر مرگ خامنه‌ای
🔺
بیانیه رسمی دولت اسرائیل تا دقایقی دیگر</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5185" target="_blank">📅 10:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5184">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">حمله به بحرین
😅</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5184" target="_blank">📅 10:31 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5183">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">شاهکار جدید صدا و سیما  اینها رو باید تلوزیون‌های جهان در بخش سرگرمی نشون بدن</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5183" target="_blank">📅 09:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5182">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">«دیشب مردم تهران در کوچه و خیابان  کل می‌کشیدن» مرسی از بابت این اعتراف و این مستند سازی از وضعیت تهران پس از انتشار خبر مرگ خامنه‌ای</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5182" target="_blank">📅 09:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5181">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83519ba27a.mp4?token=giYeTTuRLDq6KxuS7nCN8dHQaQw9lSfVNKu_Gu7Q7pIzjsvXPQAHJIwqBQIT-65D_zBs3ZXIwJSoX7KRQXrDYSY0oD1Y8-Fk6JZzHC0vWKmYUWdoIi3awFJGF5MGNJObXP_wmKYp26HC-ZlxDbnyC1HbcWgxn7diutjjT_PWrSRbUHBFSoqu6sk_nKxoBRGsbw0r9uyjMN1tfg6efoIG49UtTvCBVSx7sEMunh7THS6dEpS7vhW-D0RbBlI6D9FlOUBqrITjVM51FTS2_0Lex6CjksJrEagb_4VrAJfnCxHpYdtXu943X0RUS0BWqfCH8fL3VPuLhz4sN4Vp0BzuHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83519ba27a.mp4?token=giYeTTuRLDq6KxuS7nCN8dHQaQw9lSfVNKu_Gu7Q7pIzjsvXPQAHJIwqBQIT-65D_zBs3ZXIwJSoX7KRQXrDYSY0oD1Y8-Fk6JZzHC0vWKmYUWdoIi3awFJGF5MGNJObXP_wmKYp26HC-ZlxDbnyC1HbcWgxn7diutjjT_PWrSRbUHBFSoqu6sk_nKxoBRGsbw0r9uyjMN1tfg6efoIG49UtTvCBVSx7sEMunh7THS6dEpS7vhW-D0RbBlI6D9FlOUBqrITjVM51FTS2_0Lex6CjksJrEagb_4VrAJfnCxHpYdtXu943X0RUS0BWqfCH8fL3VPuLhz4sN4Vp0BzuHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پلیس پاکستان داره عزاداران خامنه‌ای رو با چوب میزنه  دیروز هم پلیس پاکستان ۶ تاشون رو کشت.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5181" target="_blank">📅 09:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5180">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">بخش خبری ساعت ۱۴ شبکه یک و تکرار ادعای زدن ۳ جنگنده آمریکایی  در آسمان کویت و تکرار این سوال که چطور در آسمان ایران به این پهناوری نمی‌تونید ‌، در آسمان کویت تونستید؟؟</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5180" target="_blank">📅 09:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5179">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">فرماندار جم در استان بوشهر، می‌گوید که یک «پهپاد متخاصم» منهدم شده و وضعیت شهر به حالت عادی بازگشته است.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5179" target="_blank">📅 00:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5178">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از شلیک موشک از منطقه جم بوشهر به سمت چند کشتی که در تلاش برای عبور از تنگه هرمز بودند.
گفته می‌شود در جریان این حملات موشکی که از سوی سپاه صورت گرفته، به سوی یک کشتی آمریکایی نیز شلیک شده.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5178" target="_blank">📅 23:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5177">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7730b3f12b.mp4?token=o60xG84LntYZhhaXHiOriXj78Bn04HxQVYxhh_Z7ucFURDMsvGm8rqqEtGYYEgwpJQ4Eu2y65vM4g76lLTK2g5Vrbo4pONvZedbhp5nhHtuKUI7RWUIkMVRCvJY9-b9Bm_ZTx8AQcfsSZTSDR3ky3dLSER4hKApKnEul_hPD-bgHHQgpgJwPhMQmeAkb45lpJ7LCjlqOU6MDbnZx81Mfsa-wpS38UZQzJHoZXlQPUOVHtP5d6NaEymXtIBK0Kzuc5uJIudHZcVTf94enw2zWme_-g-FZx9zdxyoYVYZ9yB7SNXQTLcfSqFUQUTOxzGPP3LNFWXCnU95eBycDO5KQHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7730b3f12b.mp4?token=o60xG84LntYZhhaXHiOriXj78Bn04HxQVYxhh_Z7ucFURDMsvGm8rqqEtGYYEgwpJQ4Eu2y65vM4g76lLTK2g5Vrbo4pONvZedbhp5nhHtuKUI7RWUIkMVRCvJY9-b9Bm_ZTx8AQcfsSZTSDR3ky3dLSER4hKApKnEul_hPD-bgHHQgpgJwPhMQmeAkb45lpJ7LCjlqOU6MDbnZx81Mfsa-wpS38UZQzJHoZXlQPUOVHtP5d6NaEymXtIBK0Kzuc5uJIudHZcVTf94enw2zWme_-g-FZx9zdxyoYVYZ9yB7SNXQTLcfSqFUQUTOxzGPP3LNFWXCnU95eBycDO5KQHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف رهبر شهیدش رو پاره کردن :)</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5177" target="_blank">📅 20:23 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5176">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bbac44461.mp4?token=OPf7OmR0hqeMOvXhcdEzQu1d1rUjxIMcUcAkz8F0hhHIkBSfwXVMSqnOt3NKloQyz7ubyySiUq0rg5n6FA4xD0lmhzNdQ4Gxx5zLF4ExfjyeX9O_IIe2p0yDKVLJ-Of0d-4Xklsf_GLyJ4f7pFzHblW0j5SoYdJ-aFXiMkvQc-oa_uP7M8OiRKVnIvUGeFa-C4NGEbf402kFIC_1YEz5Ap-yLuhk3fciiXno6947u_Em5gBIJlbiqrTsXms-LfidWINhUAw_vS0kVDTh_GIWwOXQHBaPjdLBcuMmF2yJ55z_zFH0_OtE1voFEiUWAvu6EwD8DKNht72Hb1c4lEEkbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bbac44461.mp4?token=OPf7OmR0hqeMOvXhcdEzQu1d1rUjxIMcUcAkz8F0hhHIkBSfwXVMSqnOt3NKloQyz7ubyySiUq0rg5n6FA4xD0lmhzNdQ4Gxx5zLF4ExfjyeX9O_IIe2p0yDKVLJ-Of0d-4Xklsf_GLyJ4f7pFzHblW0j5SoYdJ-aFXiMkvQc-oa_uP7M8OiRKVnIvUGeFa-C4NGEbf402kFIC_1YEz5Ap-yLuhk3fciiXno6947u_Em5gBIJlbiqrTsXms-LfidWINhUAw_vS0kVDTh_GIWwOXQHBaPjdLBcuMmF2yJ55z_zFH0_OtE1voFEiUWAvu6EwD8DKNht72Hb1c4lEEkbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد از ۹۰ روز صدا و‌سیمای جمهوری اسلامی می‌پرسه در حمله به بیت کیا کشته شدن؟
کمیل خجسته، برادرزاده منصوره خجسته باقرزاده، همسر علی خامنه‌ای، میگه  افراد خانواده خامنه‌ای که کشته شدند، همه در یک نقطه نبودن! در جاهای متفاوتی از منطقه بیت رهبری بودن که به همه اون جاها حمله شده.
این همون حمله‌ای است که پسر عبدالرحیم موسوی ،
رئیس ستاد کل نیروهای مسلح میگه ؛ ۳۰ روز گشتم و جسد رو پیدا نکردیم!
عجیبه در این حمله فقط مجتبی سالم مونده باشه!!
چرا خامنه‌ای در پناهگاه نبود
!؟</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5176" target="_blank">📅 19:41 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5175">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
آمریکا و جمهوری اسلامی به یک توافق ۶۰ روزه رسیده‌اند تا آتش‌بس را تمدید کنند و مذاکرات درباره برنامه هسته‌ای را آغاز کنند.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5175" target="_blank">📅 19:14 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5174">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/208f980645.mp4?token=VoYywUekaV-4Cu8eOOqSzWK2IkqZEDa4piWhkepjIFeAU0G89j_TB8iPnVxv1QsUoQ7r5GdDWHeqqwqPorF0kjWn6RQIoUl6oSuEtyY6pQo3FzLf6WnRp9-WI3odMTto25Mc5Mi6ts54MR7addQxlC-FPtNALNVcgDhPClA1vNkL5pFZkQ6VC5smsDBQjW2lr-DGBD47uB3Pfp8gZxvN3xPypJw5-0zpX0MiFp6FYP9RhhbNhTs0tJhdjH76J5zpE57QlJ-u6B05-KeDCWfHAPtVkz2Em46Ztb31NQJRGMWRl3Kuh40povd5OO7i0PHGukEI7P_bm7GdymjbYOfVSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/208f980645.mp4?token=VoYywUekaV-4Cu8eOOqSzWK2IkqZEDa4piWhkepjIFeAU0G89j_TB8iPnVxv1QsUoQ7r5GdDWHeqqwqPorF0kjWn6RQIoUl6oSuEtyY6pQo3FzLf6WnRp9-WI3odMTto25Mc5Mi6ts54MR7addQxlC-FPtNALNVcgDhPClA1vNkL5pFZkQ6VC5smsDBQjW2lr-DGBD47uB3Pfp8gZxvN3xPypJw5-0zpX0MiFp6FYP9RhhbNhTs0tJhdjH76J5zpE57QlJ-u6B05-KeDCWfHAPtVkz2Em46Ztb31NQJRGMWRl3Kuh40povd5OO7i0PHGukEI7P_bm7GdymjbYOfVSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش زدن ظریف :)
نوبت عراقچی هم میرسه!
این مسیر رو خیلی‌ها رفتن!
از منتظری و بنی‌صدر، تا موسوی،
خاتمی و روحانی، احمدی‌نژاد و…..</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5174" target="_blank">📅 19:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5173">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47b8458a9e.mp4?token=b5xatZ3Hf8TWr1OyYUcAw7xb4YOX074Dw20kda3ETmivjE2Ppyt2nglRtzMIMgHmppc0jEPBZJiAS327BLieLkBfsRO4EQyb2K5I5DmzguTgHc9zYDcHxoPSIyj-nuQ8L81xmyOvG_-aA2Gvgv-YaheZOCYQpbTlA29L1Ajljz0_ypGqZFD2CImO-VHq14EHuDIIpNIDeNHbaQTupVRYNd_XJTIvIaWXpVjRgeZLJuAXzpsY-SzSa5oV-S8LjYTQSMs4WtbBY2-rQzK4NYSILakYVWteBi7q41Sk4rfsEZyzPaOjF3NVuMFuyCf7vKQKtIgChftDqztwTFPXx6KhPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47b8458a9e.mp4?token=b5xatZ3Hf8TWr1OyYUcAw7xb4YOX074Dw20kda3ETmivjE2Ppyt2nglRtzMIMgHmppc0jEPBZJiAS327BLieLkBfsRO4EQyb2K5I5DmzguTgHc9zYDcHxoPSIyj-nuQ8L81xmyOvG_-aA2Gvgv-YaheZOCYQpbTlA29L1Ajljz0_ypGqZFD2CImO-VHq14EHuDIIpNIDeNHbaQTupVRYNd_XJTIvIaWXpVjRgeZLJuAXzpsY-SzSa5oV-S8LjYTQSMs4WtbBY2-rQzK4NYSILakYVWteBi7q41Sk4rfsEZyzPaOjF3NVuMFuyCf7vKQKtIgChftDqztwTFPXx6KhPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله یک مرد مسلمان چاقو به دست در محوطه یک ایستگاه قطار در سوئیس موجب زخمی شدن ۴ تن شد.
او با فریاد الله اکبر دست به این اقدام تروریستی زد.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5173" target="_blank">📅 14:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5172">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cba2527ef2.mp4?token=Nv4JFUXoX2H7yUr73uD2IfNY7Q8GARPhlYIhzb1jgtsNW6Df6UJetC7jJiTpNvWficSrBNoMmcdRZ-QmM1y_JywbwcNsk1AjPOuDIrjcQi3y1MrOjby6Th_U22cSj5fuqF5lM2DCLWUAbK76qd2t3L3QZsjTpOpRWPj3bLTAr_iSI8aVYwBRPbzEoq9Kut2WlhmgxkKPr6YRX5h6kCmxBztsGUry722MlmeMlhw1BKSDSAyZaxYSdVlmZQHJKFNNY_KO0tHT-1S-KsOhoWDDkcZ6YAdR7YAkH9amisgJA8z6tafSCYyeWfHlibyDlOlrL6klNNm0W80pR5iUQK46Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cba2527ef2.mp4?token=Nv4JFUXoX2H7yUr73uD2IfNY7Q8GARPhlYIhzb1jgtsNW6Df6UJetC7jJiTpNvWficSrBNoMmcdRZ-QmM1y_JywbwcNsk1AjPOuDIrjcQi3y1MrOjby6Th_U22cSj5fuqF5lM2DCLWUAbK76qd2t3L3QZsjTpOpRWPj3bLTAr_iSI8aVYwBRPbzEoq9Kut2WlhmgxkKPr6YRX5h6kCmxBztsGUry722MlmeMlhw1BKSDSAyZaxYSdVlmZQHJKFNNY_KO0tHT-1S-KsOhoWDDkcZ6YAdR7YAkH9amisgJA8z6tafSCYyeWfHlibyDlOlrL6klNNm0W80pR5iUQK46Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله هوایی اسرائیل به بیروت
🔺
آمریکا از دولت اسرائیل خواسته بود تا به بیروت حمله نکند
🔺
گفته می‌شود که در جریان این حمله، «علی الحسینی» مسئول ارشد موشکی حزب‌الله لبنان، که در واقع یک عراقی است از «فرقه الامام حسین» از گروه‌های نیابتی جمهوری اسلامی در عراق، کشته شد.
🔺
اسرائیل دیروز هم در حمله‌ای به غزه، فرمانده تازه منصوب شده برای «گردان‌های قسام» (نیروهای نظامی گروه تروریستی حماس) را حذف کرد.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5172" target="_blank">📅 14:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5171">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">علی الحسینی‌ از فرماندهان ارشد و مسئول واحد موشکی «فرقة الإمام الحسین» حز‌ب‌الله عراق در حملات امروز اسراییل به لبنان کشته شد.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5171" target="_blank">📅 14:44 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5170">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G9gxIaYSSCGPlzgqPrGo6QF-mdGBMNxfJTQV8aZTmPoFAi6JWFhJ2NNoPvX7RsrYYRFi1iIRu1EKoDuH3kM3jWm_kkC2aYsCQkU0XB5rJ8i4fAPYX7gaY-ST-Rio86s-E4KURLi0LPF5D19CBnyjUFiQm5fRpWG02sF-xmFtUcVLI6hFUD6LMS14e--PlJeYLgsOkRMIScU0wKRlNibHMpe0OPJc4-XiL-M_TgvuEg4Ak_TK3XmIpHtWkMqKeoCqYPn8DlY9IouGB47-3cljAAcI3wbpKaHD2FXHUKM9zN3oeC2VvhtIdrPX7H5b4wZLh2KkfcGp3EG-JU1NYuWDAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه سنتکام:
ساعت ۱۰:۱۷ شب به وقت شرقی آمریکا [۵:۴۷ صبح ایران] روز ۲۷ مه،
ایران یک موشک بالستیک به سمت کویت شلیک کرد که توسط نیروهای کویتی با موفقیت رهگیری و منهدم شد. این
نقض فاحش آتش‌بس
توسط رژیم ایران، چند ساعت پس از آن رخ داد که نیروهای ایرانی پنج پهپاد انتحاری را به پرواز درآوردند که تهدیدی جدی در تنگه هرمز و اطراف آن ایجاد کرده بودند.
همه پهپادها توسط نیروهای آمریکایی با موفقیت رهگیری شدند.
نیروهای آمریکایی همچنین از شلیک پهپاد ششم از یک مرکز کنترل زمینی ایرانی در بندرعباس جلوگیری کردند.
فرماندهی مرکزی ایالات متحده و شرکای منطقه‌ای همچنان هوشیار و با تدبیر عمل می‌کنند و به دفاع از نیروهای خود و منافع‌مان در برابر تجاوزات بی‌توجیه ایران ادامه می‌دهیم.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5170" target="_blank">📅 14:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5169">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f7f2acbc1.mp4?token=Jus1Xf6o1g9ZBruT32SqCeeEUmDvakG5pCChieQGVbk-soFkBJl86L6ozM28xBi1EbM0cIJDw9TJyWIbVOjQpcKLQX3UrRPNQ7K5WaBF1PDksHKVrBIb2trs__K6eqXoPaGsiwg90G0OJBrIy4iP7jOFUEwa7K4OesEMVxT-PLq2pFETY0woF5zCrEv8xLKj2lYi4iw0kNVmv3LxiY0c1unN8J4q0P27tyYJWpjoG3IEoG2RRjI5hlbA2x2mdqNLzslwKZsVc9_fPlwBJqi4eVd2J24kjELfLeSowYlOCGbJ9mR2fQL5ywBC3wx2BbNIocKeSQxVmjKC0ZqUUbWodw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f7f2acbc1.mp4?token=Jus1Xf6o1g9ZBruT32SqCeeEUmDvakG5pCChieQGVbk-soFkBJl86L6ozM28xBi1EbM0cIJDw9TJyWIbVOjQpcKLQX3UrRPNQ7K5WaBF1PDksHKVrBIb2trs__K6eqXoPaGsiwg90G0OJBrIy4iP7jOFUEwa7K4OesEMVxT-PLq2pFETY0woF5zCrEv8xLKj2lYi4iw0kNVmv3LxiY0c1unN8J4q0P27tyYJWpjoG3IEoG2RRjI5hlbA2x2mdqNLzslwKZsVc9_fPlwBJqi4eVd2J24kjELfLeSowYlOCGbJ9mR2fQL5ywBC3wx2BbNIocKeSQxVmjKC0ZqUUbWodw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسلام یک دوره کوتاه از رشد علمی داشت،  که همیشه هم سنگش رو به سینه میزنن،  ولی حتی اسمش هم گویای همه چیزه!  «نهضت ترجمه!» رفتن شروع کردن به «خوندن» کتابهای دیگران!  کتابهای ایران باستان و یونان باستان و هند و روم و……  خوندن و ترجمه کردن و شدن باسواد !  اونهم…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5169" target="_blank">📅 10:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5168">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZpYpq7u7XQHUsA2LFsz2kdAxz4h3zbZkixZczzYpkdODeDVSYEjBtZpFNuA6OVAPVkaoblcxVK1Nws5dN4qPKDpJ5WGoyyeDKuZovEXZBZt8JG8pzkd8Gdn3A4VEFKcKnYhTsrTQWqwyID3GQ-rBFrCLbHBvRxoNcfOIjBhgU2TaXYunC1tzbTMAJpiZ0A8KK5xYtmE6Wav0DoJjgAHWbxMvmCTlqxbRQ_PJzpBOtUB2TcG4Y8hfO_6iMSz84JRTlvYNValOL_KysAcKO29QHrbUZOhvtMyuB24mV_esS-ybJnI9rzJZF3D32LA6npDmHvDwXYvll-tnD15C-mpCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سر و وضع شهردار نیویورک رو!  دیروز !  جوامع مسلمان، از غربی‌ها، آموزش مدرن رو یاد گرفتن، آموزش دختران، مدرسه، دبیرستان، دانشگاه،  انتخابات و حق رای، تفکیک قوا، داشتن حزب، داشتن انجمن و سندیکا، داشتن روزنامه و رسانه، سینما و تئاتر و موسیقی به معنای مدرن، مناظره…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5168" target="_blank">📅 09:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5167">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67cdb18f71.mp4?token=DxW_3kB7JuB_-zLCgt-OAO5YeE_ypGZDs6BdPwOP5-y0wlK2UBnAaeexiDKPo3mf6c3x4rPwDjm2hFH7XnSjDWDWXMYrTWQMcE-S02VWFmgYUNx66fdtZBpBeCyszgTbFDuOsAJv2ogOwgjYZfpedRv5R41gqSd3OiDBv9iHr5gsLcYF6H3mD10LN47F_99i90skIanrA0_5WbhF2tbgHkFrvJNefjIWzPaDXEXFkDHT82JeWdxShJZyhzk7oynDbGf_xIex-bsg9yNiipU73zvRoU-n3ikueybGwQJ69zEvPTdo49FasMIpwnvvR1zXWXelCetVG5UUbUI1BcHCkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67cdb18f71.mp4?token=DxW_3kB7JuB_-zLCgt-OAO5YeE_ypGZDs6BdPwOP5-y0wlK2UBnAaeexiDKPo3mf6c3x4rPwDjm2hFH7XnSjDWDWXMYrTWQMcE-S02VWFmgYUNx66fdtZBpBeCyszgTbFDuOsAJv2ogOwgjYZfpedRv5R41gqSd3OiDBv9iHr5gsLcYF6H3mD10LN47F_99i90skIanrA0_5WbhF2tbgHkFrvJNefjIWzPaDXEXFkDHT82JeWdxShJZyhzk7oynDbGf_xIex-bsg9yNiipU73zvRoU-n3ikueybGwQJ69zEvPTdo49FasMIpwnvvR1zXWXelCetVG5UUbUI1BcHCkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سر و وضع شهردار نیویورک رو!  دیروز !
جوامع مسلمان، از غربی‌ها، آموزش مدرن رو یاد گرفتن، آموزش دختران، مدرسه، دبیرستان، دانشگاه،
انتخابات و حق رای، تفکیک قوا، داشتن حزب، داشتن انجمن و سندیکا، داشتن روزنامه و رسانه، سینما و تئاتر و موسیقی به معنای مدرن، مناظره و مفهوم «شهروند»، دادگاه و وکیل و حقوق مدنی، پزشکی و بیمارستان مدرن، بروکراسی اداری، مفهوم حقوق فردی، مفهوم و ارزش آزادی بیان، مفهوم دولت و ملت، سرشماری و شناسنامه و داشتن فامیلی و..
صد مورد دیگه!
مسلمان‌ها در دنیای جدید چی داشتن؟ هیچی!
هیچی!! لباس سنتی بپوشیم بریم توی خیابون هاشون نماز بخونیم و بگیم خدای ما از خدای شما بزرگ‌تره!
با نخوت بگیم ما خیلی از شما بهتریم!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5167" target="_blank">📅 09:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5166">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
🚨
سحرگاه امروز ارتش آمریکا به ‌منطقه‌ای در اطراف فرودگاه بندرعباس حمله کرد.
سپاه نیز در اطلاعیه‌ای اعلام کرده که در پاسخ به حمله آمریکا ، پایگاه هوایی مبدا این حمله را مورد هدف و حمله ‌قرار داده.
بیانیه سپاه اشاره‌ای به محل این پایگاه هوایی آمریکایی نکرده.
اما خبرهایی از فعالیت مقابله پدافند هوایی کویت در برابر حمله پهپادی منتشر شده.
🔺
برخی رسانه های حکومتی نوشته‌اند که یک نفتکش آمریکایی قصد عبور از تنگه هرمز داشت که مورد حمله سپاه قرار گرفت و در واکنش ارتش آمریکا دست به حمله‌ به اطراف فرودگاه بندرعباس زد که ظاهرا مبدا حملات بود،</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5166" target="_blank">📅 08:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5165">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ  به PBS News: «جمهوری اسلامی غنی‌سازی را کنار خواهد گذاشت و «هیچ» تحریمی هم برداشته نخواهد شد. هیچ خبری از لغو تحریم‌ها نیست. »</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/5165" target="_blank">📅 19:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5164">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/etnfa0TfoijcLEpEXPIYt5Ft3wHq1EDvYjwLBG7UvBcwxa13RAo8pGIzS4CaBywzKyQu7SPXnsiaco8F0znTKB8dMlvsZgIOruC9u8sKCFs7mjGyyXmNdtr2g8FKiVt3QEkzP0CjKuHd8ug_642aj-xqcauaZG8d1qBjm9KMK4_n8-zw3uNE4TFL0XNwWVD-MvsSjGUKeahmWOeZDlIbk0VlxgEie_Tf3120qHZm2SrEF8oDJcobXQMimx2LRAAKSzVD31ufk5Kh0hD8hgX331EW1XJWbRC6ArSuEriW9zrbuH6CrKVtICQ3BjJ7pd0_eBLHt1SpiR5xcpq59w1r5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۳۵۳ سن  حداقلی ازدواج برای دختران ایرانی از ۱۵ سال به ۱۸ سال ارتقا یافت.
جمهوری اسلامی اما سن حداقلی رو
به ۱۳ سال رسوند تا کودک همسری کاملا قانونی بشه! جمهوری اسلامی اما ازدواج زیر ۱۳ سال برای دختران رو هم مجوز میده.
فقط باید دور زده بشه، اول صیغه جاری بشه
بعد برن دادگاه و قانونی اش کنن! به همین سادگی!
در بهار ۱۴۰۰ ، حدود ۱۰ هزار دختر ۱۰ تا ۱۴ ساله در ایران شوهر داده شدند!</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/5164" target="_blank">📅 12:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5163">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qa_lpvB0E28nK59Wk2W81fQ9s50nAQUPgG47q7aQcQkqNyMlrxMzTEkIFGc_xQsoabu7JwXieMc0QVF2P_HRCNeqUv9VbMfRGJS83Vk1Lc7yYJ-ZSu5qFcROpknkI6loXfr1yocZdRVwfac4wz3z_d46zPlbm_kG40BdGL-8B3VRIXEyIAipKK8bzbZIma4ffb8t36YxR2mVqfDtCjYexS_OyUMQLJkySb-zvbAM0LqD6scOaB5aCzc53mI_-0M1Ljd6PcdcXjntUUB1Ezwc7ktrakgvdch9bmhvOCSw2PjHKIbpdTqGmNDM-EoBWeH4_p1I4PQfi8yqXDpa1LY_uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،  یا به اصطلاح روشنفکران و…..  تا این اندازه در آغوش آخوند هستند و مدافع آخوند!  «ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.  اینها ایران رو سنگری میخوان برای مبارزه با غرب و با اسرائیل…</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5163" target="_blank">📅 11:08 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5162">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NLIuqcAizjTaGuPLdAyBzI0xv0KXByfGVsGNFk_NcrWpa4JhZFWedIR6b1zfPP9SY5x_UKCEEkn-kbZoKbIJbHyzgUuBeUhrlujRd0jXYftaNJisofrSYQxTZz2VHUqjCev9wsJAQiKB8OVzGTT6K-efFBsSvs-s998qyngGM7s9Aw5kNC8Lbhj-2S_vNFMC7EQHIKcHEeWw7F9k2hGJOay5J8sqmomLhH4HOPN-uU_PTduvqCcKrVSc1XRJ1CuCXPcFPLNKtJVZXweX2L4iYzTBzDcqutlaACk7E-L_GqD9JrPOmByo2hIbPhBbmGEpWEQ-81RDcnBJMvDpojTz7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسه هم که فکر می‌کرد زرنگی کرده و با حاتم بخشی از خاک چکسلواکی، کشورش را از ورود به یک جنگ رها کرده، هزینه بسیار سنگینی پرداخت!  به قیمت تصرف پاریس به دست آلمان نازی!  آلمانی‌ها دقیقا با سلاح‌هایی که  از کارخانه‌های عظیم نظامی چکسلواکی  به دست آورده بودند،…</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5162" target="_blank">📅 10:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5161">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KNyhbZrijjs-Qm5nh0FEpP7EjsBtJ4fVajmvQWzF26iURs0ozEvpYQHb-kQtXlhZTO1I9Qvy3SrawKkQ6Hv5v-P1e_FcP4pPKXVGo2EuGju-XmNFgOjZnAOqZtV1vL7zfoCDYAf2rF2U7DTLMix_GAc-RCLPsA_fa5w6_zi9G_zmBE-SzIlCGAqgZ4UeV22uIbcFOHbpx9pJ7rkWU0mjAckQUNe1M9TdvI6kLw6sNMvbBZePC8pUjHe0RTZzqHQ93J2VfiqIdQUxmkgX7xkXiTnUkNSCNvTUvaWH3mS88b_W11hDOD5TLekO0DUubHdoi6jc8Wvbikh0YjoT2BIsqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرچیل اون موقع نماینده مجلس بود.  دولت چمبریل رو سرزنش کرد و گفت :  «به شما حق انتخاب میان جنگ و ننگ داده شد. شما ننگ را انتخاب کردید،  و با این حال جنگ هم خواهید داشت.»  پیش بینی چرچیل خیلی سریع به واقعیت پیوست! آلمان این مناطق چکسلواکی را گرفت اما دقیقا…</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5161" target="_blank">📅 10:11 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5160">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EDpeJnHsi7f_BrQC-BYBlUr31Tz9CuKWE-hciYvfjGYlPcs0KCtO3yz382U9jOxmVkNl_Ckcohtq6BddBQF2-XNwHtGS2Getq0f6lL0F-FWuYiFlOF03MvWmcOMsQAWciAiXDtWXJksJhRfbR0yca_qL0reW6oRLPgLIYSYDuG1emnNOjrT4havo2NxFw2w1IM5m9olNLLq2ob7tjutkhMnyVplcLIn8JGx-AIK3rYvgTkD2cn8IEbRNVa6PKxXN6TsNixesNW_x_uMdN7tQKVv7G4e1LqLJqa9420vUPZVkfhNcxA2fx5tK2BcQVIwi4Ft07ShMLzg8-2UXS-jo4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چمبرلین، در صدر دولت بریتانیا،  به همراهی فرانسه، قراردادی را امضا کرده بودند که بر اساس آن، ۳۰٪ از خاک چکسلواکی به آلمان نازی داده می‌شد.  مناطقی که مردم آن آلمانی زبان بودند.  هیتلر میخواست همه مناطق آلمانی‌زبان در آلمان باشند .  بریتانیا و فرانسه، عامدانه،…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5160" target="_blank">📅 10:04 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5159">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Md7x_9Lleu9u89u_0STzzFUmNd2fJVD5gStqHPQ4afgHmjpStNll7T4Ppq2vmATHM3SBoJp3uudAwL_R4bBcwFyTvTcLfmxzWOjDbRZMn5Wll2wpV-KnPqHY5AEneY2EUguITJBuif5JM1NKFWpLAUYWbgl-gQEDvSe6dK6jUSF_Sig_F9bwmcIDz1JIJc6eiBQ0UmC7qVmFE7PnAusDcYv4zOm_HvLClZc0BZpfbLkqmSJfUhhc7v9W7ar1G_LBMdFyQhFpJfLpFapGVr7F7_sag6STLZIIjovzo8K-VETarS184vUsUZXIFw2McDWTR5JSrQVT6kNT5vo5QcQ1ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۳۸ چمبرلین، نخست وزیر انگلیس  با این تیکه کاغذ به لندن برگشت. کاغذ را پیروزمندانه به خبرنگاران  و جمعیت انبوهی که جمع شده بودند نشان داد.  او می‌گفت که به یک «صلح برای نسل مان» رسیده ایم. می‌گفت این قرارداد اروپا را از افتادن به دامن یک جنگ بزرگ نجات…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5159" target="_blank">📅 09:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5158">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X3X0c4lYByy_eD-n15vduhKjcQWcEOkLuzngOsTqdnP3OFeWI6YzKEwLgw8v3O5PXlKbX-BNCQ-QbouXaRZnSHOziJ5p4YBhGB9uPjUlWr5joPLvz2CULVub22R8TnOKLEVAFwa7paSb2ZsJ11b1cZs7xleWqI3YuQ2IgDOYH4KwZnrwpfkuLUyx_c_vCuiWFVmRu5PwaEltwKuJxL4Asfi0bSXfPYnWnzrjrDN_d4prnowU2X40x1erT_3IaiEojKk9DxAA3fxV74K_tG9-dyUlt7D8ReQQQ0QPxO6QDGdLVTgm8ZirNtny1_r-65dOYTNnB30aHfdPEERlxL82XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۳۸ چمبرلین، نخست وزیر انگلیس
با این تیکه کاغذ به لندن برگشت.
کاغذ را پیروزمندانه به خبرنگاران
و جمعیت انبوهی که جمع شده بودند نشان داد.
او می‌گفت که به یک «صلح برای نسل مان» رسیده ایم. می‌گفت این قرارداد اروپا را از افتادن به دامن یک جنگ بزرگ نجات داده. این تیکه کاغذ اما یکی از «خیانت‌بارترین» قراردادها بود.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5158" target="_blank">📅 09:47 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5156">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hmPjra285NmzrlB8xarOhXlALdaIFinsZfdlx4yY30tDKbGJhwGp4rGID_pHFhIbN7exCmyUPkXJsP_N-8LjwYDD_EUzPCyWwNyWbDAPsGfVhfvqpvI_9iNev22uEmmn3y3BUm3HSyWJEcOd2Gf4VHiE9inska3daXCzbXWVBuCgmorlZiWpYJKcG5ve3MTfsybjz6LrDC0YFdX5ND9FemL_qbG8X9syVVSTNQ8WI7y-T0JEE-FuXHkEHhA-OwWh5xqK0X8TyEI73MD9wmBEiz_g8V7sIH8p1qGWoLLx0wyGv1DH1Oh6qDJrdZc5VzAubrA-cicWQUcg6T-p1SoOWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما دیشب بعد از انتشار خبر شنیده شدن صدای انفجار گزارشی تهیه کرد و گفت : منبع صداها مشخص نیست!
بعد صابرین‌نیوز و خبرگزاری دانشجو و… حتی اسامی کشته‌ها رو منتشر کردن
بعد سخنگوی سنتکام رسما گفت حمله کردیم و زدیم و…!
دیگه صدا و سیما در همون مرحله « منبع صداها مشخص‌ نیست» موند که موند و داستان رو ادامه نداد .
«مصلحت» نبود!</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5156" target="_blank">📅 23:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5155">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fbae4d271.mp4?token=AlhqXsforqn80Fh-0440D3Lfa1EENnGuWuOqeaMw-Exdnl-KrHiqHo90p7xtnh9bZe7h2S1hdQe9HQuvSDjb_T5skwEsgsSUe_rmfUY9fH7861ZfsOVbOn1P61ISPGZozzgSvvKBow6wQQDGHE6GdFo0_Y8WI6osJpVpxG6YXd0KxJ7UJUjLbZaqDi8Eb8MSEt2SqvGs0qbfTggTDYYbIHQTR-aZDBmE_xVAN338831drkKUQ2EgyjcQD4PY6-Fm-jQSjqovssleQF0c1scWi253inP-8bYO-7oQjE_L8chs8fDJ7cAVIpmsg5Gi7S2yAmEQ7lSHvoUEd1TK9kWAsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fbae4d271.mp4?token=AlhqXsforqn80Fh-0440D3Lfa1EENnGuWuOqeaMw-Exdnl-KrHiqHo90p7xtnh9bZe7h2S1hdQe9HQuvSDjb_T5skwEsgsSUe_rmfUY9fH7861ZfsOVbOn1P61ISPGZozzgSvvKBow6wQQDGHE6GdFo0_Y8WI6osJpVpxG6YXd0KxJ7UJUjLbZaqDi8Eb8MSEt2SqvGs0qbfTggTDYYbIHQTR-aZDBmE_xVAN338831drkKUQ2EgyjcQD4PY6-Fm-jQSjqovssleQF0c1scWi253inP-8bYO-7oQjE_L8chs8fDJ7cAVIpmsg5Gi7S2yAmEQ7lSHvoUEd1TK9kWAsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علیرضا دبیر: کارمندان بهایی من‌وتو می‌تونن
در صورت بیکاری، تو پارک دانشجو مشغول کار بشن
مدیرِ تراز جمهوری اسلامی</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5155" target="_blank">📅 22:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5154">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sO0wSVg3niLLXEEWVUJJl12D13FL5x8MBZKvQ2ZG82wlTq_laTKrQl6LWqCFgfFIX6GtZBkfhz9qvPSSSZHLymeNhEsrUS-FL56ByfZ9n-AzbVs-sULkHrvxnX-V6gSb-ZxNO0Eu9ns1rQqqZVCawAeJT3iuTLcf0p8Z_ssBPC4IzWtldRqYSX7sPaROzF9HzB8QZ_NTyEBr2ShU098jJCe9C6QQzg2oth04sQQifc_Q6I4Pe4SOJjADHhiHb-XgCDjZRffhhodJwOauIehDPOCETO9POYBhkolC36h-Yhna9UI8CYcd883KAPCMxo4YGlCRZSo7y1d4rsrvKFZb3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاریکاتور شارلی ابدو
از قصد جمهوری اسلامی برای گرفتن پول برای عبور کشتی‌ها از تنگه هرمز.
آخوندی که میگه : به نظرت
چقدر کاغذ توالت بهمون میرسه؟
اشاره به پول ایران و بی‌ارزش بودن
ریال ایران که ارزشش در حد کاغذ توالته.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5154" target="_blank">📅 20:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5153">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">‏پیام منتسب به مجتبی خامنه‌ای به مناسبت حج: رژیم منحوس صهیونی ۱۵ سال آینده را نخواهد دید.
باعشه!
بابات هم همین‌ها رو میگفت که باعث شد امروز ۹۰ روزه که معلوم‌ نیست هستی یا نیستی، اگه هم هستی طوری قایم شدی که گویی هرگز نبوده‌‌ای :)</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/5153" target="_blank">📅 14:43 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5152">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2PxmyGe9p_I6A1oloo2_pvLbGc97f5DUnwITGetNTZaHcTp3gFo1iATH8M8ln8Vc6RvJAuR0TU3h0HLIxxSqL9PCHx3gUt0Y-rJ7PyQ9hZWXCz22VhmamacMEDWH-vbaQfezh8dNhbGterkqcOJ6kjH63uqQT774v_EZdA_kA1ruXw18R0NNkmjjIlyi10ZjsSrWNRu8qapg67kd0WuPkHNl34G0hulMLGBrazdLSdQTn8i79whVvHzVjEKGYHV7-1K3wV0IVc8sjCofxviXvTXzSEOtrDL-gq-YD517SAHJIRYqGMOKhFt8TCfmpmoOiwjYKdHIdya3zZXTAPVig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ذوالقدر دبیر شورای عالی امنیت ملی، میدان جدید رو معرفی کرده که هیچ کس نباید حرفی بزنه که وحدت شکن باشه!
دستور خفه شدن همگانی تا رسیدن به پیروزی!
اسمی هم از مجتبی خامنه‌ای نیست.</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/5152" target="_blank">📅 05:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5151">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A3fBkp5ZdlgT89g7JsHToRFwdusqpX9cWx47-JiFkqy0GoS0-Ix630hCseGbrc_FFsc-2eFU0zr34xxtdRHbsHDuU-Zz2oJeLFRCErwregKbFxEerNFNygp2dtC7LavnN3DWyPoSk0rvl4jgjXSzDyLpzW2YFG852v0EDS-O-h5DfZUWIAjpxQDzIUcljHKJ5kOapBZUZSs7VvzusIPRxT2ZLHjzXapafmX4QEAgQtQYJdwv2T3bJdYDajDsUwvpNP1L4jhOkQ-mzNzinSvW-lguym2qYV9q2B4ZePg9son8c3EBoWvGGjjMSZbLhHIGDW2U4JMh4nf_qv_3qBZIbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا حملاتی در جنوب ایران انجام داد / کشته شدن چند نیروی سپاه.   سخنگوی سنتکام رسما اعلام کرد که جنگنده‌های آمریکایی به چند سایت موشکی و دو قایق که مشغول مین‌ریزی بودند، در اطراف بندرعباس، حمله کرده است. خبرگزاری دانشجو، وابسته به بسیج، تعداد کشته‌ها…</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5151" target="_blank">📅 04:57 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5150">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sOiCwsxZiGcI64JLyKPyigF3THHjPl3x8YxeKDAL8-KxWPaJ8as1QUmrt4AtnFP0XPyhk0371WXy00luJhA90H0dtFd9PXdOXfvublM8nUhz3d0MD5WfdMA0TbOYv9m5LyRfJhAZImyvva8L5IqL_KpdchxHFrlqYr5EUUwD9rfk0ugdzYxK2u_IaaAuqTBZOkejk-Erv4mmkYUJmW5gAjehPycRJSCQIC7zD8SS0S5NR0SFe4kXSmx8u6TY_tNSiAJZ79v6GNMId_h174iAXav6cIcJNhfMuDiVissYQZfzQ4OZIhosWJoPv-sUtfmFQ1VLH_EOf5OnWM79nSKdYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا حملاتی در جنوب ایران انجام داد / کشته شدن چند نیروی سپاه
.
سخنگوی سنتکام رسما اعلام کرد که جنگنده‌های آمریکایی به چند سایت موشکی و دو قایق که مشغول مین‌ریزی بودند، در اطراف بندرعباس، حمله کرده است.
خبرگزاری دانشجو، وابسته به بسیج، تعداد کشته‌ها را نامشخص اعلام کرده اما اسامی سه تن  را نوشته.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5150" target="_blank">📅 04:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5149">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ترامپ : یا یک توافق عالی برای همه خواهد بود یا هیچ توافقی نخواهد بود.
اگر توافقی نباشد آمریکا به جنگ بازمیگردد.
کشورهای منطقه باید عضو پیمان ابراهیم شوند.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5149" target="_blank">📅 17:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5148">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">قیمت نفت : ۹۷ دلار</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5148" target="_blank">📅 14:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5147">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tLqhEwvj3OcW7ERa3boVTqxlA7AdcBSikkk5OwRAiRN3QxydoYxbvdTnYb82-bjvH3wrBV2lsU4vKUvp9ta9A6at_EUL5P052cdwGW_NIq1f4Fl58gMsTd3Jzzn0p620v94QvqD6WcIiithQn9saXHM1mR8irGw-vCOhYoRHtYLxaTKxQZAsMUEfq30WelT0W85EYX0kvEFoitn2c6KBXB0e2tsVhbkF9-Z_HTNeeFebvoYpK6Qv6rG2mke4aEA4rSgwGuOzRu9SieuhGDq3xa_e8Tq1V40YuQ6HtmlE5Zg0qKDBRyyuzL4hmgWBTBsbCGoWnrnXZPv3DSZcGgCYkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که صدا و سیما شیپور پیروزی میزنه و از موافقت آمریکا با هر ده پیش شرط جمهوری اسلامی میگه،
سخنگوی وزارت خارجه امروز گفته : کسی نمی‌تواند ادعا بکند به توافق نزدیک شده‌ایم!</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/5147" target="_blank">📅 14:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5146">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔺
بقایی، سخنگوی وزارت خارجه:
آمریکا به عباس عراقچی، ویزا برای حضور در سازمان ملل نداد.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5146" target="_blank">📅 14:16 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5145">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77b6861470.mp4?token=VuZUpAsEaUOJEmjAkdlHZNxVSzxowoiO9MNKopY0KWXCznQDfMcY3n8R5h_RVhZaXiSguQjhkES7vMaGYbwoEs9r-uy0hXnP2XVO_isj4QjLU1TU55dm5gmxZYdqJR0d2Uh6-ARgb4v8-nruNEuui6liQT_ACX0rhn2oq6jd8YdI3mMlBrnTMI3WBxPUDAhPqI3E3HQPzg2l-z8_75FTQbn3J1a-Yb4ZDuFrJxeIDc_Z5izbSifIIDGPtROQ8TKq8V0-19gT0tZ1Ur_UF09vLiKMKIstysPcgCPgCPfDOZ3PTNSnqk9oIAoV_d5wMkUI4jtAOwJRZN3pWGWJtL71Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77b6861470.mp4?token=VuZUpAsEaUOJEmjAkdlHZNxVSzxowoiO9MNKopY0KWXCznQDfMcY3n8R5h_RVhZaXiSguQjhkES7vMaGYbwoEs9r-uy0hXnP2XVO_isj4QjLU1TU55dm5gmxZYdqJR0d2Uh6-ARgb4v8-nruNEuui6liQT_ACX0rhn2oq6jd8YdI3mMlBrnTMI3WBxPUDAhPqI3E3HQPzg2l-z8_75FTQbn3J1a-Yb4ZDuFrJxeIDc_Z5izbSifIIDGPtROQ8TKq8V0-19gT0tZ1Ur_UF09vLiKMKIstysPcgCPgCPfDOZ3PTNSnqk9oIAoV_d5wMkUI4jtAOwJRZN3pWGWJtL71Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمایی از شهر رفح در نوار غزه و پیروزی‌های محور مقاومت
قبل و بعد از  حمله تروریستی ۷ اکتبر</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5145" target="_blank">📅 13:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5144">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل - توی این مایه‌ها -  گفته: «در پاسخ به هر حمله پهپادی انفجاری حزب‌الله، باید یکی از برج‌های بیروت رو هدف قرار بدیم.»
حملات حزب‌الله به اسرائیل رو یا دولت لبنان باید متوقف کنه، یا اسرائیل.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5144" target="_blank">📅 13:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5143">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYi0DX1Wg4QQEov9XnIAi6Lwk0Cn9UofE7qULZPW8qLW_cPkoNw8EzduFL84QlzI0nLu342i9QeGODCw3wtGFw7S4kl-QChptRVJlfb8kYHU_IGLz2Ud06LCp98qu4u6ui6H7bSqovYSexX0lORAeLVgM09cTG7Nw4GYESxU1gQm19bjry9tpiSMv5qcnS5Tq4x8xnQygxhWWSOuKbJfcD3yxGXvSVxDn4UdSdHMuIyAHEUMfXQ9aarpSKfwq8cTLmLaXBjpfRuCZjon-x5KF6981XAQFnPH4fx8QdThzs0xndw5X1dGWT9GVgdsGzSmj0mkuIt4Ry3REany0iC5ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبح در ایران با اذان و با اعدام جوانانش شروع می‌شود.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5143" target="_blank">📅 11:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5142">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69381f4f87.mp4?token=l1LmTPz7S7gVuuFccpvGqapRKTMFNkd5UUYf59pOX_lwBARscjfqbyPiweWJkofQNdwq_tNk90RR-GbVNn-rfXl8n2JpjkfcsNjBd6ci2sEZLTt9u3H_Bo4Mf1FmOiyBv7ChkwA6-KFuc8N8z0Dg7_vcxdt-1yigmBRKkY85rY_4ahUgakSIPuh59goC6K6CdUvqNBsTIRkalYtSTJsYQQdxwdxaIOrYenElV-wPLSHwQNsMBG0e2Z3kP3poPc1OSnYray9iE5fFvaHvKCi67niEVOMuIPNiDzJKpVjTCAvzMFS3BJwRLQC722FWlZqo9nOQwugie8jBxKVhtfYp1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69381f4f87.mp4?token=l1LmTPz7S7gVuuFccpvGqapRKTMFNkd5UUYf59pOX_lwBARscjfqbyPiweWJkofQNdwq_tNk90RR-GbVNn-rfXl8n2JpjkfcsNjBd6ci2sEZLTt9u3H_Bo4Mf1FmOiyBv7ChkwA6-KFuc8N8z0Dg7_vcxdt-1yigmBRKkY85rY_4ahUgakSIPuh59goC6K6CdUvqNBsTIRkalYtSTJsYQQdxwdxaIOrYenElV-wPLSHwQNsMBG0e2Z3kP3poPc1OSnYray9iE5fFvaHvKCi67niEVOMuIPNiDzJKpVjTCAvzMFS3BJwRLQC722FWlZqo9nOQwugie8jBxKVhtfYp1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برخلاف
گزارش صدا و سیما
۱- بسیار بعیده آمریکا و اسرائیل
به جمهوری اسلامی حق غنی سازی رو بدن،
۲- غیر قابل تصوره که آمریکا
کنترل تنگه هرمز رو در دست سپاه بگذاره و چندین کشور ثروتمند عربی
رو بگذارن گروگان اینها باشن.
مسئله بزرگ‌تر از جمهوری اسلامی است
مسئله سرنوشت منطقه است.
۳- غیر قابل تصوره آمریکا تحریم‌های اولیه
و ثانویه و….. رو برداره و دارایی‌های
مسدود شده رو بهشون بده!
🔺
اما اگه این حرف‌ها ۱٪ درست باشه :
۴- فاصله میان جنگ ۱۲ روزه
تا جنگ ۴۰ روزه حدود ۲۵۰ روز بود.
ترامپ بعد از جنگ ۱۲ روزه گفت بود :
« جنگ تمام شد، ما پیروز شدیم و تهدید
را خنثی کردیم! »
۵- ۱۶۲ روز دیگه در آمریکا انتخابات میان‌دوره‌ای است.
ولی شاید حتی پیش از ۱۶۲ روز دیگر،
جنگ سومی در راه باشد! و شاید پس از انتخابات.(با فرض اینکه حرفهای صدا و سیما درست باشه!)</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5142" target="_blank">📅 11:04 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5141">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">صدا و سیما:  آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده   ‏۱. آمریکا متعهد به عدم تجاوز به ایران شده  ‏۲. استمرار کنترل ایران بر تنگه هرمز ‏۳.پذیرش غنی سازی ‏۴.رفع همه تحریم های اولیه  ‏۵.رفع همه تحریم های ثانویه ‏۶.خاتمه تمامی قطعنامه های شورای امنیت  ‏۷.خاتمه…</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5141" target="_blank">📅 09:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5140">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc885feb3.mp4?token=lxIU4XaS7lKuwR-ietd04zX2a1kpYsJKUJemHJInr5bKUmxatRBwCzFuj6FMoohNFVYf3hD1Z8ZsRRq2Iz3DHfJ7zQEL4gfIY_D0rTlnc7pmJKf6qHx6HjlhFp9tZnpm7qPDjRcAxsH-bigYSN4G0IhHxJkez1fNylC1zdUITotnfJTb_xKTisptDAELzEAj7TxxwVCI8vcOeyQhwUjXaP7SMdsNZtt3Tczf-oxeP_Lwnml3b3DLt4N90JQZg4RPdERBjdHCWXZenNYKkvZ4RSB65cqk5zyt6WleJesTpUmK5ROCeZoocjxmRYcgsOGCChUgVahtJ9LA6ndd47ZT8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc885feb3.mp4?token=lxIU4XaS7lKuwR-ietd04zX2a1kpYsJKUJemHJInr5bKUmxatRBwCzFuj6FMoohNFVYf3hD1Z8ZsRRq2Iz3DHfJ7zQEL4gfIY_D0rTlnc7pmJKf6qHx6HjlhFp9tZnpm7qPDjRcAxsH-bigYSN4G0IhHxJkez1fNylC1zdUITotnfJTb_xKTisptDAELzEAj7TxxwVCI8vcOeyQhwUjXaP7SMdsNZtt3Tczf-oxeP_Lwnml3b3DLt4N90JQZg4RPdERBjdHCWXZenNYKkvZ4RSB65cqk5zyt6WleJesTpUmK5ROCeZoocjxmRYcgsOGCChUgVahtJ9LA6ndd47ZT8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدا و سیما:
آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده
‏۱. آمریکا متعهد به عدم تجاوز به ایران شده
‏۲. استمرار کنترل ایران بر تنگه هرمز
‏۳.پذیرش غنی سازی
‏۴.رفع همه تحریم های اولیه
‏۵.رفع همه تحریم های ثانویه
‏۶.خاتمه تمامی قطعنامه های شورای امنیت
‏۷.خاتمه تمامی قطعنامه های شورای حکام
‏۸.پرداخت خسارت به ایران
‏۹.خروج تمام نیروی آمریکایی از منطقه
‏ ۱۰. توقف جنگ در همه جبهه ها از جمله لبنان</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5140" target="_blank">📅 08:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5139">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">برخلاف خبرهایی که یکسره از احتمال توافق می‌گویند، فاصله خواست‌های دو‌ طرف هنوز آنچنان زیاد است که بشود گفت :
توافق بعید است!</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5139" target="_blank">📅 01:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5138">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
اکسیوس : ترامپ روز شنبه در یک تماس کنفرانسی به رهبران کشورهای عرب و مسلمان گفت که اگر توافقی برای پایان دادن به جنگ با ایران حاصل شود، او می‌خواهد کشورهای آنها به «توافق‌های ابراهیم» بپیوندند و با اسرائیل توافق صلح امضا کنند.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5138" target="_blank">📅 00:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5137">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
اکسیوس : ترامپ روز شنبه در یک تماس کنفرانسی به رهبران کشورهای عرب و مسلمان گفت که اگر توافقی برای پایان دادن به جنگ با ایران حاصل شود، او می‌خواهد کشورهای آنها به «توافق‌های ابراهیم» بپیوندند و با اسرائیل توافق صلح امضا کنند.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5137" target="_blank">📅 22:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5136">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدماوند</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ve6S7MALC-GPekT8ZJivpA4Nn7_2eyUFLLNh-EYaviJjs-yUWNth1iceew3Kyj7UCWFqbKVp3mco_5PGrU7FTpVuVSOhOWYiUQxg5JtOTl_2HmJ3fJUHUGx2zQOnv41Tpm2c1DySxHgompWiLqQabnJ4jCPF90mbZd1bLzBRf2jjSBaPQEVGbcf4fD974S8q77I106fJJ7tkd5Epu1bmfyZ5iW22ztBVZJe_H9ClHKVdqnnGGc30hnD6ShmJQhoRG4sMjMz-2WWHg1mRAeu821UCXhxhBZQjOjbxQl8-T3QzoTSotghQ83eqixHKNMm_8QMrmgT4BpO1oU79nN-pUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗
یک اعدام دیگر
مجتبی کیان، بامداد امروز و همزمان با اذان صبح، به دست جمهوری جنایتکار اسلامی اعدام شد!
جرم او را ارائه مختصات صنایع تولیدی به شبکه‌های ماهواره‌ای اعلام کرده‌اند؛ انگار که اسرائیل که اتاق خواب رهبران رژیم را می‌داند به اطلاعات دیگران نیاز ندارد...
خبرگزاری سپاه نوشته است: «وی در پیام‌هایی به شبکه وابسته به دشمن، اطلاعات محل شرکت مرتبط با صنایع دفاعی را ارسال و با قید نام نخست‌وزیر رژیم صهیونیستی در پیام ارسالی به عوامل این شبکه تأکید می‌کند که موضوع را «به بی‌بی آمار بده»!
T.me/irdamavand</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5136" target="_blank">📅 15:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5135">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">️
🚨
🚨
آکسیوس: یک مقام آمریکایی گفت که پیش‌نویس یادداشت تفاهم شامل تعهدات ایران برای هرگز نرفتن به‌سوی ساخت سلاح هسته‌ای، و همچنین مذاکره درباره تعلیق برنامه غنی‌سازی اورانیوم و خارج کردن ذخایر اورانیوم با غنای بالا از کشور است.
☢️
به گفته دو منبع آگاه، ایران از طریق میانجی‌ها به‌صورت شفاهی به آمریکا درباره میزان امتیازاتی که حاضر است در زمینه تعلیق غنی‌سازی و واگذاری مواد هسته‌ای بدهد، تعهداتی ارائه کرده است.
- ببینیم چی میشه. بعید می‌دونم جمهوری اسلامی اورانیوم غنی سازی شدهاش رو تحویل بده،
خبر هم میگه ج‌ا به یک میانجی (پاکستان / قطر) شفاهی گفته!</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5135" target="_blank">📅 07:35 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5134">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‏
🚨
🚨
ترامپ :«من اکنون در کاخ سفید هستم؛ جایی که همین لحظات تماس بسیار خوبی با محمد بن سلمان آل سعود، ولیعهد عربستان سعودی؛
محمد بن زاید آل نهیان، رئیس امارات متحده عربی؛
امیر تمیم بن حمد بن خلیفه آل ثانی، امیر قطر؛
نخست‌وزیر محمد بن عبدالرحمن بن جاسم بن جابر آل ثانی و وزیر علی الثوادی از قطر؛
فیلدمارشال سید عاصم منیر احمد شاه از پاکستان؛
رجب طیب اردوغان، رئیس‌جمهور ترکیه؛ عبدالفتاح السیسی، رئیس‌جمهور مصر؛ ملک عبدالله دوم، پادشاه اردن؛
و همچنین ملک حمد بن عیسی آل خلیفه، پادشاه بحرین داشتیم.
موضوع این گفت‌وگوها جمهوری اسلامی ایران و تمامی مسائل مرتبط با یک “یادداشت تفاهم” در ارتباط با صلح بود.
یک توافق تا حد زیادی مورد مذاکره قرار گرفته و تنها نهایی‌سازی آن میان ایالات متحده آمریکا، جمهوری اسلامی ایران و کشورهای مختلفی که نام برده شد باقی مانده است.
به‌طور جداگانه، من همچنین با نخست‌وزیر اسرائیل،بی‌بی نتانیاهو، تماس داشتم که آن هم به همان اندازه بسیار خوب پیش رفت.
در حال حاضر، جنبه‌ها و جزئیات نهایی این توافق در حال بررسی و گفت‌وگو است و به‌زودی اعلام خواهد شد.
علاوه بر بسیاری از بندهای دیگر توافق، تنگه هرمز نیز باز خواهد شد.»</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5134" target="_blank">📅 00:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5133">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tGbLhnIFuW44n5M9IlzDYum250DbavhRPu_23TU6jx-Py-hpeXF8j03bGQkIaav8PVJdqRSuTsVyQO6Umwn7TTFmNfNRX_XKApvsWgLsZ_T4TLON4-8ZzKyfjMyIrs8OWD_h-6t6SLj0mjNmkiPHhv7KcHfk-PZG95fqzGZjOunimWDrNF1IRrT9wYQjbP_24bzCf_3TzTw_IY4lX9jAZbc4QNipAObRgYDzrF4_bM6Kzojw9cdJdgE_mhj6uo4ySIYR21IKV6BeoHZjuK4--KtCIEX-Y__d0S6TklD00gry-XLBp_5GMkOa4ENeLYyG4MJnL1gw3RUNfkKjp0zw3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با هوش مصنوعی طراحی کردم.
گاو : نماد فراوانی و ثروت سرزمین ایران و منطقه.
تن زنانه و نیمه عریان: نماد پاکی، نماد لطافت و ظرافت ، در نقطه تقابل با خشونت و توحش و درندگی
بقیه هم‌ که معرف حضورتونه، آشنای دیرینه.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5133" target="_blank">📅 22:09 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5132">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ترامپ به اکسیوس  گفت که درباره توافق با ایران یا بمباران، «کاملاً پنجاه‌پنجاه» است. ترامپ گفت امروز با مشاوران ارشدش دیدار خواهد کرد تا آخرین پیش‌نویس توافق را بررسی کنند و ممکن است تا فردا تصمیم نهایی را بگیرد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5132" target="_blank">📅 20:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5131">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
آکسیوس : ترامپ ساعت هشت شب امشب ،  در یک تماس کنفرانسی  با رهبران عرب شرکت خواهد کرد تا درباره پیش‌نویس توافق با ایران گفت‌وگو کند و نظر آن‌ها را بشنود.
🔺
نظر شخصی :  توافقی در کار نیست!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5131" target="_blank">📅 20:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5130">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
آکسیوس :
ترامپ ساعت هشت شب امشب ،
در یک تماس کنفرانسی
با رهبران عرب شرکت خواهد کرد تا درباره پیش‌نویس توافق با ایران گفت‌وگو کند و نظر آن‌ها را بشنود.
🔺
نظر شخصی :  توافقی در کار نیست!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5130" target="_blank">📅 20:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5127">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b5c3d0822.mp4?token=SzpN6bUPKbetXuglsX_G14p5HS3toZFK1RRwxt8cI5fxKy9YeALxT-U8BPJ_32fiRfKaJjihnk7Dpd7F_L12En5NA8myFb67kzlPQ1_nSwpbovjlip34dCdsjuX8xbV_IcK9a3NyD53xX9muj8iK-nzZn0J-P2_1FLVchAy-JsmEsEfvMxYxXnTWhhhhLjiksC_x7wzR0mv_d4PBAAxAknqOa1PpH0pslXfw_ZVqaYCF526h0C0qYO4eBQL72ZD57Y4JXUirfzuCQqqoZoJw2YPm5O5wbDW1iR3Yf1Sje58kLHQUBdSv-Mr9Qh9UOcvX61wn2SqCLSIFpVGIqdlvHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b5c3d0822.mp4?token=SzpN6bUPKbetXuglsX_G14p5HS3toZFK1RRwxt8cI5fxKy9YeALxT-U8BPJ_32fiRfKaJjihnk7Dpd7F_L12En5NA8myFb67kzlPQ1_nSwpbovjlip34dCdsjuX8xbV_IcK9a3NyD53xX9muj8iK-nzZn0J-P2_1FLVchAy-JsmEsEfvMxYxXnTWhhhhLjiksC_x7wzR0mv_d4PBAAxAknqOa1PpH0pslXfw_ZVqaYCF526h0C0qYO4eBQL72ZD57Y4JXUirfzuCQqqoZoJw2YPm5O5wbDW1iR3Yf1Sje58kLHQUBdSv-Mr9Qh9UOcvX61wn2SqCLSIFpVGIqdlvHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی بعد از صدها سال
مردم شمال مدیترانه و جنوب مدیترانه بهم رسیدند
الجزایر سال ۱۹۵۲  (۷۴ سال پیش
مناطق اروپایی نشین
و مناطق مسلمان نشین</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5127" target="_blank">📅 19:52 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5126">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NP6oAjfJdBx_mAArKCTcZsv_gwBFFapNA10NlaJHTzxR50o8p7f-qs9W8tqMSwGVnDwTc2ZVh75cdMpxWLWSqiFXqtm7li_50sobFb-sazHQra0Ks0N_VQ0VgCro8HMDjtROKJfA069GF1pmSeRZZQpsKB7QWUTwLawNWcGfLYr64kcqQGofjuyp2N7Q-vinvivWFDhkG9Wwg18VsdgkPblI_Iadhx-0oIjkjVSfrkotxZSxOE4BDJ0GvqsWqAdonWfnduNtk9MZpe--NMGTp-Hd2VAgBXvXRX3FgMevEawv_48ITbVNpXxBH4Vi5NpGALg0DWaIdKMLjZMs-bCy7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شمال دریای مدیترانه، اروپا، نماد پیشرفت
آرامش، ثروت، هنر و معماری و….. است.
جنوب مدیترانه، نماد فقر و بی‌ثباتی
و جنگ و سیل مهاجرانی که
از این سرزمین‌ها می‌گریزند و …..
مصر، در جنوب مدیترانه، برای ۹۷۰ سال بخشی از جهان یونانی - رومی بود.
لبنان و فلسطین هزار سال، لیبی ۱۲۰۰ سال،
تونس و الجزایر و مراکش حدود ۹۰۰ سال.
تا اینکه اسلام از راه رسید
و تفاوت میان شمال مدیترانه
و جنوب مدیترانه شکل گرفت.
و دو سرنوشت متفاوت، دو چهره متفاوت گرفت.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5126" target="_blank">📅 18:48 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5125">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IaHTTr1eBeh-f3beybVibngf3Jf2ZkarwJCdyPjDJCLN_GoQbMf1XUpPaMpWhWgGlFyjdXzFAVs_BOcSOqao-l25-B7KYDwUrxdA07Iz0gEc_KUEO_xFShGtlogYvdM5CCP6nzY5Ay4SlDZYUGSXMyJJbAXKoCUrVLsXXdZMDZgkrwBy3Z5DyKa7UeDHbXOfpZbetNLoNSyePhP6n07v7sgoS3QllNEh-1AETYTOLMo2jWhBnkm7-kF73UwTDSkYjs0wa8RCDTWP1p_rEBycqCgk8uSadSywh93FGb4wlTwzfdPlS8Z9PQeWIIhoiXZOfC-CnWkh0opP2A8l85XSQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ که پرچم آمریکا را روی نقشه ایران به تصویر کشیده و تیتر زده «ایالات متحده خاورمیانه؟»</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5125" target="_blank">📅 18:16 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5124">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">مارکو روبیو در خصوص مذاکرات با جمهوری اسلامی:  شاید تا عصر امروز خبرهایی باشه، شاید هم نه. مطمئن نیستم ولی امیدوارم. پیشرفت‌هایی صورت گرفته. شاید عصر امروز، شاید فردا، شاید این یکی دو روزه، چیزی برای گفتن داشته باشیم.  جمهوری اسلامی باید دست از غنی‌سازی بردارند.…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5124" target="_blank">📅 17:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5123">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">مارکو روبیو در خصوص مذاکرات با جمهوری اسلامی:
شاید تا عصر امروز خبرهایی باشه، شاید هم نه. مطمئن نیستم ولی امیدوارم. پیشرفت‌هایی صورت گرفته.
شاید عصر امروز، شاید فردا، شاید این یکی دو روزه، چیزی برای گفتن داشته باشیم.
جمهوری اسلامی باید دست از غنی‌سازی بردارند. اورانیوم غنی‌سازی شده را تسلیم کنند، تنگه هرمز باید باز شود.  ترجیح رئیس جمهور ترامپ دیپلماسی و رسیدن به یک‌ توافق است.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5123" target="_blank">📅 17:25 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5122">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EryfovAiMcoHM1dIg0Iwr4NDPs-DfjTXHflQiwIWlmCF-KSXoy5atzaaIa43-T4BL2GF2XnpdQzjJBnqdQD1jTiAFM6PpsmznyK0llVu-Yhx183LPMtGrapYVtww50VGyLa6p2CGjO5WcCcFlEXfdvf3Gaot62hcZir7yNTlXTXErlTW7MsaXsxv-8yn2YGY99nVLylAk_s42e_OVzfg8OH43QkQW0djOdBngsLVpbta788in1T_kBiAm_kqzhXHtOjOFQkoZMeymNO7GryxHyOP-ixfCPBlvW3qnERZnfXj0OxuObcCiq98gMbO_4jJGOhu4X7saBNoOnp7yhfzQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چقدر ایران باید هزینه بده برای این گر‌وه‌ها
و برای این جنگ‌های بی‌پایان جمهوری اسلامی با آمریکا و اسرائیل.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5122" target="_blank">📅 17:18 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5121">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">به خاطر ارسال ویدئو ۲۷ سال زندان!    مجازات پدر «رومینا اشرفی» ۱۴ ساله، که با داس سر دخترش رو برید: ۹ سال زندان   حکومت اسلامی! عدالت علوی!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5121" target="_blank">📅 13:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5120">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DDD-XC9IM1X6tDOu7IGA_uAHymVp-Sta4Dut3q689MQ1aFn_dRKtW-V40bU2el1ndL8S0V-WqVQOiNl8m3FAVgouBD5GiUGm79DRBn8sKgsDe-0aV2KaBGKmIcZXbE3kDof3N-fqJd93mVoUyoJYG6M273A0t-jz5PxDZUSdsY2uPZw-M990DrkKFXbWqed9dq4_LfvMFc9NhlyXBFQpAfBJ_420eruGDmw5g_2jozl-VtxsijY5wJsgV61gQa0Cw4lVyD-uqVH0ppSQCnDi74oMCQmm_f1C3pSaHJn9n4SkbPw_u4lXQ4r-S9xaqlMK09LwB07xvSX7Zc_fMxhE4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به خاطر ارسال ویدئو ۲۷ سال زندان!
مجازات پدر «رومینا اشرفی» ۱۴ ساله، که با داس سر دخترش رو برید:
۹ سال زندان
حکومت اسلامی! عدالت علوی!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5120" target="_blank">📅 13:20 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5119">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🚨
نیویورک پست در گزارش اختصاصی خبر داده که طرح ترور ایوانکا ترامپ خنثی شده
.
فردی که برای ترور دختر ترامپ تلاش کرده «محمد
باقر
سعد
داوود
الساعدی ۳۲ ساله و شهروند عراق است که گفته شده توسط سپاه پاسداران آموزش دیده.
انگیزه او انتقام از ترور سلیمانی عنوان شده.
نیویورک پست نوشته که الساعدی از اعضای ارشد گروه شبه‌نظامی کتائب
حزب‌الله
عراق (از گروه‌های نیابتی مورد حمایت جمهوری اسلامی در عراق) است و گفته می‌شود
آموزش‌های نظامی و اطلاعاتی خود را مستقیماً زیر نظر سپاه پاسداران در تهران گذرانده است
. او با قاسم سلیمانی و جانشین وی، اسماعیل قاآنی، ارتباطات نزدیکی داشته است</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5119" target="_blank">📅 08:14 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5118">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">حریم هوایی ایران در مناطق غربی بسته شد.
پروازها فقط در طول روز</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5118" target="_blank">📅 01:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5117">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
براساس گزارش آکسیوس، ترامپ به‌طور جدی در حال بررسی آغاز حملات جدید علیه جمهوری اسلامی است؛ مگر اینکه در آخرین لحظات، گشایشی در مذاکرات حاصل شود.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5117" target="_blank">📅 00:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5116">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">وال‌استریت ژورنال:
واسطه‌ها در تلاش هستند تا یک توافق موقت بین ایران و ایالات متحده به دست آورند.
پاکستان، قطر و دیگر بازیگران منطقه‌ای در تلاش برای کاهش اختلافات بر سر برنامه هسته‌ای ایران، رفع تحریم‌ها و امنیت منطقه‌ای هستند.
هدف، یک توافق کامل نیست، بلکه یک چارچوب موقت است که آتش‌بس را تمدید کرده و امکان ادامه مذاکرات گسترده‌تر را فراهم کند.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5116" target="_blank">📅 23:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5115">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a3vUbFJ0at3-u1mu1EROTDtdEQK0QexziNnlAgZ-g_rWTCF2e47ruO-1QD11zkvV9AFjWo9UJZa9_KLxyhZsZDox9I4Lb-TxqP-zcOiizRwRmrwgD1JVYzIzz9N8O1Z9mAviFuBXuzvt7DtyeoaW8D6ocQ6cqtanQ4Kp55h3RieJE1rbaCA9HSHqPg5b4CYAemeC7H6mEFvrbWvhJ3CyW2RqvUu5WcVRPlVIATfk1R9kEROn_VXnzw_c2_4U_eKh8otyFftPuGA1kH1lO3dzaz7bPtzg71Dd7B02FQ6U5tDeCsGKJqwSHVq3saQxlUkS-86utSOrlxLrKEgmS9Fpsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری وابسته به سپاه این مدلی تیتر میزنه
ولی در واقع «گابارد» از مخالفان معروف جنگ علیه جمهوری اسلامی بود که الان کنار گذاشته شد.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5115" target="_blank">📅 22:55 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5114">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LCpbcKU9KEJvmTjD3EiGaVWSgesj4Poq5Jr7dYQI6RsBdL29XYYrL5jPK07lVSvfbxvUKYn0ktdB-JsN-H4npQIsTYEDvALppMxjQNnaJDzjPaD4kSwFdVPmnBTwA1pY-08qIzrIC4ggBwT5FoRAxu8hz-Mtok6j8Xy9WKdi_vweNInWHYPLxXha8gAofQSZSXx6Ek8Z0rT2L7P3WJSS_egHYiNuw-pMcP_8VrxfhJ20_6QeUBoVvxz7KhQZPCjdHO-_Ay8T80zdOVKm8AxKUNgBkDnxo75ZjHRmS1OeaKjpo9jeJiiZsO1UL8kPzUft3xO8OVvnloXKOLkceLYb7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به بیانی دیگه : توقف جنگ در لبنان، پیش شرط اساسی جمهوری اسلامی برای مذاکره با آمریکاست!
خب چرا جنگ در لبنان شروع شد؟
چون گروه تروریستی حزب‌الله حمله کرد به اسرائیل.
مهم‌ترین دغدغه‌های جمهوری اسلامی نظام خودشه و حفظ نیابتی‌هاش. نه ایران و منافع ایران.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5114" target="_blank">📅 22:18 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5113">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">سخنگوی وزارت خارجه ج‌ا : «اختلاف‌نظرها بین ایران و آمریکا آن‌قدر عمیق و زیاد است که نمی‌شود گفت با چندبار رفت‌وآمد یا مذاکرات ظرف چند هفته ما باید حتماً به نتیجه برسیم.»
🔺
یادآوری : جمهوری اسلامی از سال ۱۳۸۲  (۲۰۰۳) مذاکرات جدی! در خصوص فعالیت‌های هسته‌ای‌اش رو شروع کرد!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5113" target="_blank">📅 21:04 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5112">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-text">مصاحبه اختصاصی با قرقاش: ایران در موقعیت ضعیفی است، دور دوم جنگ فاجعه‌بار خواهد بود
🔸
انور قرقاش، مشاور رئیس امارات متحده عربی در امور خارجی، می‌گوید دور دیگر درگیری میان ایران، آمریکا و اسرائیل «فاجعه‌بار» خواهد بود.
🔸
آقای قرقاش که در نشست امنیتی گلوبسک در پراگ حضور دارد، در گفتگویی اختصاصی با گلناز اسفندیاری از رادیو فردا، گفت که کشورش از یک راه‌حل سیاسی حمایت می‌کند، اما در صورت بروز یک دور دیگر از درگیری‌ها از خود دفاع خواهد کرد. او همچنین گفت جنگ کنونی نفوذ آمریکا در خلیج فارس را پررنگ‌تر خواهد کرد.
🔸
رادیو فردا
: آیا امارات از مذاکرات با ایران برای پایان دادن به جنگ حمایت می‌کند یا ترجیح می‌دهد آمریکا و اسرائیل فشار نظامی بیشتری بر ایران وارد کنند و همان‌طور که برخی می‌گویند «کار را تمام کنند»؟
🔸
انور قرقاش
: نه، ما به‌وضوح تلاش زیادی کردیم تا از وقوع جنگ جلوگیری کنیم، زیرا روابط ما با ایران در حدود ۴۰ سال گذشته همواره رابطه‌ای پیچیده بوده است. ما همسایه هستیم؛ تجارت، سرمایه‌گذاری و پیوندهای زیادی با یکدیگر داریم. موضع ما این است که حل این مسئله باید از طریق سیاسی باشد.
راه‌حل‌های نظامی، همان‌طور که امروز دیده‌ایم، پیچیدگی‌های بسیاری به همراه دارند. ما همچنان از یک راه‌حل سیاسی حمایت می‌کنیم، اما این نباید بهانه‌ای برای درگیری‌های آینده باشد. مسئله تنگه هرمز روابط را پیچیده‌تر می‌کند، به‌ویژه در مورد دسترسی آزاد برای تجارت و انرژی جهانی.
🔸
رادیو فردا
: پس در واقع، همه‌چیز به جزئیات بستگی دارد.
🔸
انور قرقاش
: بله، جزئیات بسیار مهم هستند، اما ما همچنان نمی‌خواهیم شاهد تشدید نظامی باشیم، چراکه می‌دانیم تشدید درگیری‌ها در منطقه همیشه به بن‌بست منجر می‌شود و آن بن‌بست مشکلات بیشتری ایجاد می‌کند. همچنین باید در نظر داشته باشیم که منطقه نیازمند ترمیم فراوان است. به‌طور مشخص، امارات هدف ۳۳۰۰ موشک قرار گرفته است.
🔸
رادیو فردا
: که حتی بیشتر از حملات ایران به اسرائیل بود.
🔸
انور قرقاش
: بله بیشتر از اسرائیل و ما همچنان در حال پیدا کردن پهپادهای زیادی هستیم، بنابراین شمار نهایی از ۳۰۰۰ فراتر خواهد رفت. کار زیادی برای ترمیم روابط باقی مانده و پل‌هایی که سوزانده شده‌اند باید دوباره بازسازی شوند.
🔸
کامل این گفت‌وگو را در وب‌سایت
رادیوفردا
بخوانید.
@RadioFarda</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5112" target="_blank">📅 18:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5111">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qRxV9C6IiGzOsQp3S4duqh24TWduVh_-GmXmUqGU1K9DJIzd3WjvZHE4T8BAkEX4rd-qkb41tSAj5OJE9JD1HxT7QFxaC8ymT6IqyfTQwcA8QkP7nNSXOGVabOMTl8tokEIMBezZobEJ5O0IO1JmD5MRmpltHDg_K4JjvHihahejyanmbudODoPaPjYnXRsltrbYK4NqmJ3G340x__JF46sEFwX8_MvDs1fxXTB8GYPMR05rm2h2aA6t_5bmgbqQuY_iHy6hxiDY1vZ1MI_MBeVDBv2h_d7zNrLJkUCnqOS38s1wx5TaAnGN4nnvjDdpUjl7R0xqhTK2qyoH5WrWgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خانم! از چهره‌های معروف چپ  در دانشگاه تهران! در تظاهرات حکومتی شرکت میکنه!   بدون توجه به اینکه جمهوری اسلامی طرف  دو‌شب دست به یک قتل عام هولناک زد!  پس چرا کنار جمهوری اسلامی است؟  چون جمهوری اسلامی ضد آمریکاست!  از اسرائیل هم فقط به این دلیل بدشون…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5111" target="_blank">📅 18:52 · 01 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
