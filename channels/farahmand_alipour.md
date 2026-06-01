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
<p>@farahmand_alipour • 👥 62.5K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-11 07:45:52</div>
<hr>

<div class="tg-post" id="msg-5224">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SI9CYUUbwLxx9LWIdoESF2vBjoDmQtNLiZIpccSjtP-YF5eGfUa3rX6W6G8tLmIAOUGREBArNTF5pYyDW-KKMnedia21jvt5EI5sZZZ51YKmFGutbYL1g4kthmxgVN7zQoyvTX2-qKwFucwANiqTMWd-KTcmivj9YiRChJuemsgql1_Tt70YBt32OIKYsJjlL-B-iP6NHGz4RG_frJw3_dg2HFWQR6uow5VqWf4c03DdMxsaVCMtzKQlLOHE_k9th7YmTDzt1vjb3AlWvBA3oVuSRkQrkuBCdI4tOLgGs7f1dIasw9eFgqU7UxAc8U0-FLcDJB7F1B6hEeNomMga6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چطور تریتا پارسی در آمریکا
متوجه یک «طرح پنهانی» برخی نهادهای امنیتی در تهران شده؟!
معلومه یا این طرح رو خودش داده
یا با این نهادهای امنیتی رابطه داره!</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/farahmand_alipour/5224" target="_blank">📅 02:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5223">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
مایک والتز سفیر آمریکا در سازمان ملل : جمهوری اسلامی با حمله به کشورهای عرب همسایه‌اش اشتباه بزرگی مرتکب شد و تاوان آن را خواهد پرداخت.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farahmand_alipour/5223" target="_blank">📅 00:41 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5222">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqA0YJraytWtV6rAzmAWG58GdXEVQx1-Nr8ruktgtnljgq0zzjmJiffUgb7-gwV8yUZ9FH75MEneitnhqZ7sOQWlgyl5f8981oyifM8_dk_35Ww2Mk5IvNFsuuM6RgFvIeBSkEGHxkQXXZwQy7UCaXjtUtELMTvekkSNphqZ2CzxbndOP5przQERwjLT16alrZhV4yTcJEQtcaP2NSxEgmnF8X9uTMDSIwUIFrGT7XN1TcF-Ke1R6YP9HUd2ozpus_WjwEPnfz6_lTN5j0TVnKoDWWWdrMEtcjCYMgz0OaVdxWeWU4HF0LvC7iqPVXhFNE9IvdPNtoPYbrTxwghpyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌های ضد و‌ نقیض از استعفای پزشکیان از ریاست جمهوری</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/5222" target="_blank">📅 00:37 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5219">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5219" target="_blank">📅 18:19 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5216">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b0siclmglcX21YxQDq0gz6PxSoDcpuHH9r8Mp9tbejNHBY8bPJxhPFO7F2Zlxg_X6XOFPu13MApuMMIXuwrrgtwZKPoRTYNCjg0MBdB4t6bYctWy9n-hkM5BjpT9B-7PrhXvMyqXt69kdFCFzUTcDsiXUdnTkAQ6WyB-fjutBuMvt_9T0t_Yv7eJiej40IeEH5ERtHn0cTFgH1bNunG1zvcjLHo3fQkwWMDI0xtUIu8NUk_LuIX5vvoItS53POF9fJn_qPKr3HPuwHYhU9drmSNJEhgNwOJGaoccgMmtxXB1QQxspiqqKwkNTBTQGJ6uyn7_TCjpecJ85uKcq39yqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nsRdiJ0pik7_sIxIw_8yaxBf0w-Jw7HU3updWbujd6NyztnsBNCl528m4pOpWIRB5HgbraDjqMRh6uuuP0gcVDW7f_IAagHZFjqhlKTNGYWpI-hnOdWf2_erxi_krgRqlrDjeAYcqM4He4xlBXSKSBFINb3V9auSuTt1mfC9ZGG0-0-dYkyM5P-DB8alG_MEeyXyeTV46Iv4R_3oadY3WzdTzRc4yMJliJ7vaAhah1PhEOzjqZrECmM2fKsjZYaO1b99auH1_WEtIK0Su_lv-Z_SLgzAsd4jYD4f5NHa0bBDxgAPIvELLjbj3huSAE_RJW_fAlpUltH1pUyo1AeXSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N6V9GavrQG6nzumLG598vdI7ibpWJCv5Hy11Ay0hguuQYQnM3ag9FTrzv5UuCU_G6_qhn-8RuXR9q4xf931OFOKiCsfdSr_WiYT9nf_IFGI7p6xJv3L8l0YkN-VB-8_wyrmJchSsA12fN2nwLJzzDD-ih3bOP8x0G9n9Wh2y_Kv3_WefEJ43Ov8FMLhSeF_jWsZSXCY-wFnoAHzVyDb0kDYvMfxeZ9EgIwoLYaoo0iQarrfKeJiWpc4id5vm9ZzACkFC3U2Eill9w2kjTH3P-Y43yV95C85thC3nUMVVojxIuPEiP6ONyvaijVwnlUyKGE29zJ0jsuMfQILPEL3QUg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رفسنجانی سالها پیش گفت من به خامنه‌ای گفتم پاسخ این همه ضررها در دشمنی با آمریکا رو شما به عهده میگیرید ؟؟ خامنه‌ای گفت بله! جواب خدا با من!!!  و خب این جنگ‌ها و تحریم‌ها و آسیب‌ها و کودکان میناب و... همه همون مسائلی است که خامنه‌ای گفته جواب خدا با من! یعنی…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5216" target="_blank">📅 18:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5215">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db68225cef.mp4?token=q1zaCiCLK184XTAMOTnnm88m3eRKWFjXSS721j98HBGiQijyR1wAq3gfwBkQt0b0t2uBohP_wInAAoJAG-3sjAiVEYEGUOVa0Box78ysQeN9jlaGFafMHfoOuUeJZhyVzdGvzBT2PoL5obJE3M14x2QjESQtdANcMXbo97HGg0qoLU3ODxvZ5SnT6m4oUitLHS-Pb6TIEcCK2rpsxN_sOzXIlsD4Th8DWSvvBMzT9vtdeNzFkGNKPhdvitUkLVdMXCoH3g30tHfCe84u7XuD0zqpr-HssNDXevV32RL-bNaJTmWigtQOpHHW4HWS9sDTyu7NYsIvhnKG0QNkySmX7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db68225cef.mp4?token=q1zaCiCLK184XTAMOTnnm88m3eRKWFjXSS721j98HBGiQijyR1wAq3gfwBkQt0b0t2uBohP_wInAAoJAG-3sjAiVEYEGUOVa0Box78ysQeN9jlaGFafMHfoOuUeJZhyVzdGvzBT2PoL5obJE3M14x2QjESQtdANcMXbo97HGg0qoLU3ODxvZ5SnT6m4oUitLHS-Pb6TIEcCK2rpsxN_sOzXIlsD4Th8DWSvvBMzT9vtdeNzFkGNKPhdvitUkLVdMXCoH3g30tHfCe84u7XuD0zqpr-HssNDXevV32RL-bNaJTmWigtQOpHHW4HWS9sDTyu7NYsIvhnKG0QNkySmX7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی در تاریخ ۲۹ آبان ۱۴۰۴ در تلویزیون جمهوری اسلامی میگه ترامپ به ما نامه‌ای داده و صراحتا نوشته «دو گزینه بیشتر نیست» یا جنگ و خونریزی یا مذاکره مستقیم «برای از بین بردن غنی‌سازی و موشکی»  این مصاحبه چند ماه بعد از جنگ ۱۲ روزه بود! یعنی در آبان ماه، مشکلات…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5215" target="_blank">📅 18:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5214">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=EOdOSg05Yi5cZxi2gwHUr_1IXJFEqy1bJUTkxkgfTtqbLRj6uKXKzOei_vdKwY7AEX8YnJGF6HryUtqfJhjHs-mSC9hfU2Cg1hqPyfMr8CY_IYojtKy-nDsxVX_UiHLgIav9zK8gLz0G0oBDMLPmHBPLeBNiW665UNlxrXq7RtKyYraiSp4rMHXU5s1phltN--euve1lUb142br9Mc98qGARZD80HFK4c6p9st0rxLYgNtk-2a_q_wPLhRmltGTBOkY7Q7aZhA7WHLX3sbfVF6U_vDkClgViXtrbt54oO9jE5sd4w6cU3FAP0SQgEDLAYomVdyI-Y_0uOApN6GowoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=EOdOSg05Yi5cZxi2gwHUr_1IXJFEqy1bJUTkxkgfTtqbLRj6uKXKzOei_vdKwY7AEX8YnJGF6HryUtqfJhjHs-mSC9hfU2Cg1hqPyfMr8CY_IYojtKy-nDsxVX_UiHLgIav9zK8gLz0G0oBDMLPmHBPLeBNiW665UNlxrXq7RtKyYraiSp4rMHXU5s1phltN--euve1lUb142br9Mc98qGARZD80HFK4c6p9st0rxLYgNtk-2a_q_wPLhRmltGTBOkY7Q7aZhA7WHLX3sbfVF6U_vDkClgViXtrbt54oO9jE5sd4w6cU3FAP0SQgEDLAYomVdyI-Y_0uOApN6GowoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">می‌نشستن و  با نخوت وعده «دردسرها»  میدادن برای آمریکا و دنیا!  «حالا حالا دردسرها» خواهیم داشت!  بعد که جنگ شد تقصیر مردم ایرانه که تاریخ نخوندن!!!  تقصیر تلویزیون اینترنشناله!</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/farahmand_alipour/5214" target="_blank">📅 17:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5213">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab893ceeae.mp4?token=XaGLMaH7Y33Ip_hysDM-olVUUcT8Y3rz43ETnqwlZxxVO8-EYTJ4aCfSdKh6R6CIRZ2QTPKEBCRJzCDYj8qkOiHDDJ6XGzO3QL5FvEJL-9wAwGQ5RDZ_1TEIzC9kkvJ6JENn2-Yd0ua1hu_QmQWLpz4tz9uHDpTmc1Hs2aeqCO9qTeYNwmZSzXq2DAqtJCygV2pmJUY2sVnCBAhx0SQIn4a-MJGiTcYCWaljo5cih6Vfl8N3eoqgrvtq1yqPJfGkd9Fn56SnxBWyEQfwAO9PmnrKgpxGNE4FPhkjHsDISguAQO01zLF8xAkEziuhIf29MeGPL2xnqF8deHRDXTjCYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab893ceeae.mp4?token=XaGLMaH7Y33Ip_hysDM-olVUUcT8Y3rz43ETnqwlZxxVO8-EYTJ4aCfSdKh6R6CIRZ2QTPKEBCRJzCDYj8qkOiHDDJ6XGzO3QL5FvEJL-9wAwGQ5RDZ_1TEIzC9kkvJ6JENn2-Yd0ua1hu_QmQWLpz4tz9uHDpTmc1Hs2aeqCO9qTeYNwmZSzXq2DAqtJCygV2pmJUY2sVnCBAhx0SQIn4a-MJGiTcYCWaljo5cih6Vfl8N3eoqgrvtq1yqPJfGkd9Fn56SnxBWyEQfwAO9PmnrKgpxGNE4FPhkjHsDISguAQO01zLF8xAkEziuhIf29MeGPL2xnqF8deHRDXTjCYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بله جنگ ۴۰ روزه به خاطر ایران اینترنشنال بود و دیاسپورای ایرانی! جنگ ۱۲ روزه هم تقصیر افغانستانی‌های ساکن ایران بود!!! یادمون هست!  فقط فعالیت هسته‌ای و موشکی و نیابتی‌های جمهوری اسلامی و ۴۷ سال سیاست آمریکا ستیزی و دنبال نابودی اسرائیل بودن ، بی ایراد هستن…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/5213" target="_blank">📅 17:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5212">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7hEb1Ixi08niB3wUx3nUshwrLU6Dig8Ppg2KZdrTHIytZ7fAoNCNo2oH4eKJJJZYJ90AjPbqMX1vLrtxaWCC5tA6am7bOq7NqI1eGiRgJyT2rM7zomxz3abH5d_OtAilUIsGJiNYm2ITDnpge2s8HjSDDKPoxzRc4owzGHjOHK9tQbYNyTerkNCO4L1XDEYJQD9fR9XuYoaoKf6BCkBGL77XM2WtjAEqcOwV9NBMCbkyEzjPsochity-OFvTpCxdtcOUBxrH4xVb_MVqKl0qeAsGO_fIj9eCwNjMXLsp64ZOal9OuqvNCR9CN2WTnbAnwJBstEt4Ai1hjdTlFT-rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بله جنگ ۴۰ روزه به خاطر ایران اینترنشنال بود و دیاسپورای ایرانی!
جنگ ۱۲ روزه هم تقصیر افغانستانی‌های ساکن ایران بود!!! یادمون هست!
فقط فعالیت هسته‌ای و موشکی و نیابتی‌های جمهوری اسلامی و ۴۷ سال سیاست آمریکا ستیزی و دنبال نابودی اسرائیل بودن ،
بی ایراد هستن و مشکلی ندارن!
و همونطور که می‌بینید روی میز مذاکرات هم بحث ایران اینترنشناله و افغانستانی‌های ساکن ایران و دیاسپورا! مشکلات و دعوا سر اینهاست!
خوش به حال آخوند که چون شمایانی رو داره! هر بلایی که سرتون ببره، آغوش گرم آخوند رو رها نمی‌کنید!
شما اگه تاریخ خونده بودید راه شوروی و کره‌شمالی رو نمی‌رفتید! راه
صدام و بشار اسد رو نمی‌رفتید و چندین هزار نفر رو دو شب قتل عام نمی‌کردید! بی‌آبروهای تاریخ!</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/5212" target="_blank">📅 17:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5211">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/5211" target="_blank">📅 17:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5210">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KmIvLdkJtJ-H4ashSsXFRPIF2CkWhQsvVcP72lPeieY88PM3NITPXi_o5ftMjwS0DAEThjv4hrDjv7-mBOIPN6xOENUH2SIVs5LRnBb2y510ZDXWul07shbE8j7h_46PJUWbZdC7NlKcKNGjiVqq9YsynGehqkp2LjVyzukxyu9P9fmE5sefN60AVu2SUx38mq6O-JzeKJIqZxAVxpIIyR4Z8DloYWRAuSn4W6z84JtzUZtf832B8MpJXLHq87KBTooL4t61EtXtSC9-weuyK6Bz1I5go74PyCH4oUO4P71WgyPftKVlHwvmmb0R8srtWUl4-gpXBbdiKLrMaIka3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما:  آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده   ‏۱. آمریکا متعهد به عدم تجاوز به ایران شده  ‏۲. استمرار کنترل ایران بر تنگه هرمز ‏۳.پذیرش غنی سازی ‏۴.رفع همه تحریم های اولیه  ‏۵.رفع همه تحریم های ثانویه ‏۶.خاتمه تمامی قطعنامه های شورای امنیت  ‏۷.خاتمه…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5210" target="_blank">📅 15:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5209">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3y5v9TVPX2Z6WqVIxW4dEikujMlxZ4gzAzRPSL3sRovpP2nrg_baDiavHpTCk-MfmZSKScdh-Nm73PYUbZfzg5sanuSn7zoMriKDP7Lx8tor8VZnl5HOeAl5Wxpn_BImobCzgi5PW33XDJDwdwC1Q2oKBgMQjfE8eqLSNHLLuH9XviY3AACVBk8rwcmwgDZPReky2rQ9lqbAOk7aBpJvzr-57J-MgaAaO2bBaDTCY3sfFevBvbUprbJ8qB8z_arJi-t5GhtQx8MLIPWptVCzgpLFVUrdaKRFpwCaHtJwKJKdyEod4BEvsOmgXCpQDMBcxHw1R2qQQc1MzVZZB4lIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل قلعه شقیق در جنوب لبنان
را تصرف کرد، این مهم‌ترین پیشروی ارتش اسرائیل در جنوب لبنان از سال ۲۰۰۰ میلادی است!
گروه تروریستی حزب‌الله لبنان،
بدون اجازه گرفتن از دولت و مجلس و ارتش لبنان و در خونخواهی خامنه‌ای،
به اسرائیل حمله کردند، اسرائیل نیز در پاسخ دست به حمله گسترده به مناطق شیعه‌نشین لبنان زد، بیش از دو ماه است که حدود یک میلیون شیعه لبنانی آواره شده‌اند! بیش از سه هزار تن کشته شدند!
چند هفته پیش دولت لبنان قصد مداخله داشت و تلاش برای «آتش‌بس» اما این گروه تروریستی و حامیانش مخالفت کردند و گفتند که جمهوری اسلامی باید این آتش‌بس را برای ما بیاورد!
(که بعد تبلیغ کنن قدرت ج‌ا بود)
جمهوری اسلامی نیز توقف در جنگ لبنان را در صدر خواسته‌های خود از دولت ترامپ قرار داده ولی هنوز به تفاهم با آمریکا نرسیده و اسرائیل هم داره کار رو ادامه میده!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5209" target="_blank">📅 12:09 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5208">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5208" target="_blank">📅 10:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5207">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5207" target="_blank">📅 18:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5206">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5206" target="_blank">📅 10:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5204">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JfITlRtSvEC1OTDiV05ti9nTfEYIO9cYxBjfQwRK3riRC94lDbYdwsYofNbbXMiCSj3uQw21iP0d3Ae49X3tANRTh59CIbr8F9mKM2ntMTgckdMBfeljAmFPvuzbas3ZiY-15yCcaPexG2ZusPMui8dd3EKpi1k5As6v7rKXcCy2LpWHxDmNrDRqfqL8E_6jT9jy5c_sVSOfNL1O822V418o8HjXFXXSE5z1nVw5oaRe73oaIJyTa1YXr_HMdsA-oaozHUoMC9U0s6_mnsqGQ_TJMKn2apRR-aF8ylvknOidlkVTV4x8H3yna-bpb-33rW_VOf2tU1-dSvL6s3J02A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5204" target="_blank">📅 21:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5203">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KGv0rQbhnSOiwRAqHhKtwJT9SCFQdWg_BpKy98lB8PWKO29JJoQfXw5fpa4i-QEj6xXBAgd82TrhQLkkaOxGq85GfCXzdauLjhmLnqpVtXg3dXW1J__XBy9rtVaRyyIr5yF57PUS0A-JUzkmSxya2FtDqtwB4sFiS2gAq0zlQFquwbyADmgPlZWzqJnChMkhmsbJa5QZcDbDX2BiVIhKsTaaovRKB8lxpizxb8MW6TZ1fR3E18C-03RsyQdko_WPGaL2kvOrCXh739vtxnoyb8zSuadMb8EpW6pZVZtPLO5XGCH7kRKi1S6tbHGT_nXISEnYIMCSv3wzhiJRyaGuig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5203" target="_blank">📅 18:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5202">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YFqIECR-grcXsgyd9UcgfUr5-tG6MCSKjJHA8Ry6nKT3J7yq3PNNv_ssStV_M2uw_1JkwoWOyVM8SGmmOdNng0vfj8uYaX8Xt8ExzjVRlcDnssJdmtSWgPucXzMbWBuTLpQFNpBXXmJsCkFckPUKYnt_UwWXLQc_uyRiF20LzelrrTpDy0_GAosB8LBtE_iYSG1sqPdU7o7Ld0zu9pHuPMj9pNmnYhtLwMiL84r2SrTF6gF-8eILDtB73690JkM3Kx0qKZpMnST-FBkD0qLa0fku6Kozt66KJpdpAFdLUU-MQxrFXgZSeg2tl-4Vh1AlHgaIFd3Ki1otpjVeH2ys8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمادگی بهتر برای جنگ بعدی …</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5202" target="_blank">📅 18:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5201">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5201" target="_blank">📅 18:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5199">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bh6Pm0aQbsD41z5etLHeqlPUFl9BOnthpIa40l71JKeRTN3aUGkMKfDcD2XgfTnWKrOu48kwmOMGe3OE7TxsHAz4pjYvQDY_vRmZML1-n9WjtUNkmvc4Lf9VeiQPgDloYMQl6GGBLx9KxgCRmZ7x1gyixYydvk3FXJhYsSvgZA7eE9v4b5bdenVbqFR-LfTCIKCPXyNtJD8FYPn9jJbqx0x6mVK_r0_wUNuv-lZleubNHwpn2x78hQU5vMDlYCIc3ZKTSuN7Oh0ZqFTkGcg_ImmrYJZMSQ9QureuJguHx5n6glhpVdV_EcQ7DV8wqE2iTlb_y6oQuIb6kdFTlSyYgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kp6gvNQd-2hFPEPTQXozw0CaiQFIkW9Dh4f8RCC7YXyky1Vir8mZfEl4JqCMog04Cbn6-BYAPDdkmuetwVlIxJ_wwzxCy_-qaYQZ2KX6VeMEAJyHPLptsO2EWTkFIgm_eG30TRwep62bjnd7b3UDnNevTFkW8RYhftmnNVP4RcVUPaUJf0r-zG8XP9-u73By7t0Ga42FQnybqnqR-2hh_hBSQg2gMryLXVHrzqVTCySuXHNh6jCkz2zIjz9lM949hDq-CDZrNxnvyicJu1MoBGa65x_tOKKv4zwHh-sSQYOsZExmr9qCSvdePqzOXWP1wxMDQ_jzb3LuA0kwpElFaA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
لبنان سفیر جمهوری اسلامی رو اخراج کرد!
گفت «عنصر نامطلوبه»! گفت که جمهوری اسلامی عامل وقوع جنگ در لبنان شده و جنگ
رو به مردم لبنان تحمیل کرده.
اما سفیر جمهوری اسلامی در درون سفارت خانه موند و گفت برنمیگردم ایران!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5199" target="_blank">📅 18:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5197">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hhc1aWzUQRJdfj0-WfndOfmYzVmt147o45tLgLB08jclml1NZc7zHAJhLehiOiFaetT2SJhbtLKZV8C8mw2NkM8nS0qoAINOR_vVaqRns4Xl76Q26cLyZxdmtLox-tKzOdyCfgJSnhPIqq9_mTHjuBrF_f2uiSsI5LtCZb9b3hFAcAC0cnheaJxtpuX66aD5aUlLcCTobjJu9tNNdRbpvY68OoBQLog_9tRb7SwYWqKAsCkDWN7sX3KgD5bMAlXC0ex71RYlOI_4HDmGDJ_U7Jn2A98CLzf3fnad28w_UgMitCuDT_Rgc19EEiw4UOoevy4JWwv2mcDD7KZP-fLZ9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W0nAisBXNqL3bLnC62jGw-Y5df5os6xL3DYb45VLYs1MLoDfINsfeSqis0UlvKzua5G7g_V2QPCTZLGldi1GqD9CUDHwcWZ12FaqHKwr6zborhareExQaQNZUIV2LRbLUXaCFcGIWsk6PqC9-EEwm3Hz-wWtDi305gOHA5209DyqeqNnGu2vWCoRQWBuQKJJGvZLa9WBb2JOYlePlMr9Jkk8mSq0kGx4MhEBfTTMHEvBbiqbnGXOWArtKNzU1Jg3puiQQv5lUv0LfmKrfvIUB5BwDaOSYmxlOQWNFRH4VG21aD-Z8zD-yvDc9Q03HdB7nAoRoeZN76wVhSLp81UICg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
درسته هر شب توی خیابون‌ها بزن و برقص و عروسی داشتن اما در افغانستان گدایی پول میکردن :)
سفارت جمهوری اسلامی در کابل در اواخر اسفندماه رسما تقاضا کرد که  مردم افغانستان به جمهوری اسلامی کمک مالی کنن!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5197" target="_blank">📅 13:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5196">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=U07V1kuTswaxKqGFwsbfqTR24xVCKPRszvoGcXTirtZDwvBZ--xtT1wZilIWsAt0VGjmiGZUsiy1Lf0vd4N0kK_FS899uQkTe-FTUwi8pIUjZtSXvZRoPn-SPuxgB8jUjB9NeR9A5EetTSE88dDxG60jZKr7A3ARogsriYzYNKvjxLduiNKvWf9AwUxD126sPZRU7_cm-tUMsVRB9PxnaOvTv4MJcddaGSTDz1bsriIGz66uvgTYNfm2O9OPNpIMAaLzVX7ACAGu-W6fmS2LR-0rgtQz9uKmeZ_bQqyJYjsDHBl6MXatx2_6NdY13nT8AlN80vBL532mr2baxECgjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=U07V1kuTswaxKqGFwsbfqTR24xVCKPRszvoGcXTirtZDwvBZ--xtT1wZilIWsAt0VGjmiGZUsiy1Lf0vd4N0kK_FS899uQkTe-FTUwi8pIUjZtSXvZRoPn-SPuxgB8jUjB9NeR9A5EetTSE88dDxG60jZKr7A3ARogsriYzYNKvjxLduiNKvWf9AwUxD126sPZRU7_cm-tUMsVRB9PxnaOvTv4MJcddaGSTDz1bsriIGz66uvgTYNfm2O9OPNpIMAaLzVX7ACAGu-W6fmS2LR-0rgtQz9uKmeZ_bQqyJYjsDHBl6MXatx2_6NdY13nT8AlN80vBL532mr2baxECgjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی شما نبودید در اجتماعات حکومتی شون هر شب عروسی داشتن!  «صیغه یک ماهه»! در برابر «یک سکه» :)  با کسب اجازه از امام زمان</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5196" target="_blank">📅 13:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5195">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f5663381.mp4?token=o4v3JZjsC1CPCpF1OzyVTa5v3zDxikstbonPGhDjcpOjAis2o1auC-GSHzUmogDLCUDJjh-llXJAe_kTApQrGJlDgYlb1vz07-yAhs2pVVMXSL6pu0AuHzuFlOR4dTI2f-tmvAJ8wj6cQp0eEYRGHUN1NEmwrHVoubwLA42hfCXsrYAlEnr8fVRmRuYjc728hrlEtZ05SkWpDUSlib1Tp09F9eyKa4a7fpcQYku7353hq8EbqLpnMwJB4PQKKTFCQAa0U2V53AHPPYTjzDpEroNT4SiHf9rAOwpJ8NKEpZCRA0nUVtML0QXuYIoUYvpSyMT8tTXJz7-wMzNO8shVLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f5663381.mp4?token=o4v3JZjsC1CPCpF1OzyVTa5v3zDxikstbonPGhDjcpOjAis2o1auC-GSHzUmogDLCUDJjh-llXJAe_kTApQrGJlDgYlb1vz07-yAhs2pVVMXSL6pu0AuHzuFlOR4dTI2f-tmvAJ8wj6cQp0eEYRGHUN1NEmwrHVoubwLA42hfCXsrYAlEnr8fVRmRuYjc728hrlEtZ05SkWpDUSlib1Tp09F9eyKa4a7fpcQYku7353hq8EbqLpnMwJB4PQKKTFCQAa0U2V53AHPPYTjzDpEroNT4SiHf9rAOwpJ8NKEpZCRA0nUVtML0QXuYIoUYvpSyMT8tTXJz7-wMzNO8shVLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی شما نبودید
در اجتماعات حکومتی شون
هر شب عروسی داشتن!
«صیغه یک ماهه»! در برابر «یک سکه» :)
با کسب اجازه از امام زمان</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5195" target="_blank">📅 13:18 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5194">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">وقتی شما نبودید پوتین پیام تبریک برای مجتبی خامنه‌ای به عنوان رهبر جدید جمهوری اسلامی فرستاد،  پیام پوتین حتی قبل از پیام گروه تروریستی حزب‌الله لبنان صادر شد!  حتی زودتر از پیام‌ شهردار تهران!  حتی زودتر از پیام جوادی آملی :)   پوتین در پیامش نوشته بود :…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5194" target="_blank">📅 13:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5192">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5192" target="_blank">📅 12:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5191">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9993037d5c.mp4?token=qbM_hO7aXL1iT4_SaqoZ52wfIVpNeLVmwBVR5KrElsdzVINGBnkaLUiBSxAcz7-4nTgInwRo_kyKNC59ctumOtxyUz3wGhGuZQhJp_uky9drwe8aPmtZUy6JaowPwpFP0vo0J0FPCwKIKxM6uqH4akfCXZhL4MsawR9jubB1j4cG0Sb8OjKV1gJNhucxChozrdTniaQoH7VdNxYHCf4jraiIXYGCnQRejZRwLDai3j5pao77EH-tZEbXZyz_EbQvnNlqA8pFYjOWaRblyjjxvQf0cmfpZtUqrwltrd6wCdavSNN169farSl3FcJ_5T2kkz29g-v0erLdArNWsPUTsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9993037d5c.mp4?token=qbM_hO7aXL1iT4_SaqoZ52wfIVpNeLVmwBVR5KrElsdzVINGBnkaLUiBSxAcz7-4nTgInwRo_kyKNC59ctumOtxyUz3wGhGuZQhJp_uky9drwe8aPmtZUy6JaowPwpFP0vo0J0FPCwKIKxM6uqH4akfCXZhL4MsawR9jubB1j4cG0Sb8OjKV1gJNhucxChozrdTniaQoH7VdNxYHCf4jraiIXYGCnQRejZRwLDai3j5pao77EH-tZEbXZyz_EbQvnNlqA8pFYjOWaRblyjjxvQf0cmfpZtUqrwltrd6wCdavSNN169farSl3FcJ_5T2kkz29g-v0erLdArNWsPUTsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شادی مردم مشهد از خبر کشته شدن خامنه‌ای</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5191" target="_blank">📅 12:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5190">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jTcgoGmpWcqce9jQyO05uvqkpossuZiOsbAF4aiYXPkADOlIhDxWPugo4wpf_3EmDhPBfHiLrUMbLmTUoR9kFWWYKeNzKwK2Uwype6fdXjybTclVYROpLK3rd2NAZifUxLf-mGokYKFYzzuqYkTWJK2QwmBc6YaqMQngwMmSIXoObQsSotvnpwOBtiNPj2SpC7PLtAmAbfLrX7JB86VrTvfpqnLmzq0c-vhmGsA-MHIh604wohgasd1-knfUKVMPjUl3HzixMWAsfImdPgkK-4SZRtBwrReRfR2rajjHdxytaEFcFfdjBACNkMz0n03MwteSOd5ZEk70PZovv2ayqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نکته جالب :)  امروز ۲۶ روز پس از کشته شدن خامنه‌ای  در کره شمالی هنوز خبر کشته شدن خامنه‌ای منتشر نشده!  فقط اعلام شد که مجتبی خامنه‌ای،  پسرش جایگزین او شده،  اما اعلام نشده که در طی یک حمله نظامی  خامنه‌ای کشته‌ شده.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5190" target="_blank">📅 11:09 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5189">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">‏حالا که تشریف آوردید:
‏از ۵۷ کشور اسلامی، فقط ۸ دولت کشته شدن «ولی امر مسلمین» رو تسلیت گفتن و ۴۹ کشور سکوت کردن!
‏عراق، آذربایجان، تاجیکستان، پاکستان، لبنان، الجزایر، عمان و قطر تنها کشورهایی بودند که تسلیت گفتند.
‏بزرگان جهان اسلام چون‌: ترکیه، عربستان، اندونزی، مصر، مالزی،ازبکستان و… سکوت کردن!
‏تروریست‌های طالبان هم حمله رو محکوم کردن اما تسلیت نگفتن!
دولت فلسطین حتی حمله رو هم‌ محکوم نکرد! سکوت کامل!
فقط تروریست‌های حماس محکوم کردن و تسلیت گفتن!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5189" target="_blank">📅 11:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5188">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
🚨
امروز : کشته شدن ۱۴ نیر‌وی سپاه زنجان بر اثر انفجار مهمات عمل‌نکرده</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5188" target="_blank">📅 10:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5187">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های جمهوری اسلامی  از بستن تنگه هرمز خبر می‌دهند.
🚨
🚨
🚨
سخنگوی قرارگاه خاتم : به ۱۴ پایگاه نظامی آمریکا حمله کردیم و «صدها» ‌تن آمریکایی و اسرائیلی را کشته‌ایم.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5187" target="_blank">📅 10:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5186">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">پایکوبی مردم در تهران</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5186" target="_blank">📅 10:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5185">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔺
شادی مردم ایران از شنیدن  خبر مرگ خامنه‌ای
🔺
بیانیه رسمی دولت اسرائیل تا دقایقی دیگر</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5185" target="_blank">📅 10:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5184">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">حمله به بحرین
😅</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5184" target="_blank">📅 10:31 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5183">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">شاهکار جدید صدا و سیما  اینها رو باید تلوزیون‌های جهان در بخش سرگرمی نشون بدن</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5183" target="_blank">📅 09:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5182">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">«دیشب مردم تهران در کوچه و خیابان  کل می‌کشیدن» مرسی از بابت این اعتراف و این مستند سازی از وضعیت تهران پس از انتشار خبر مرگ خامنه‌ای</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5182" target="_blank">📅 09:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5181">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83519ba27a.mp4?token=Mo0Wq1NYHIV1q5uOQ69gLgATuKaFu--YzBu7oFf5AUVrNPZe4LMqYkYaQyOglRvZvPak9-fCxtGH3IxjbLXzHRi46uabPDgQChsZiS79wQlsrPGDzGldJurZEXDVcG8AeSvKf6dFEVmlzV7_Tr15VaMYrZT0gmjT-fiUn0FMx04MJpttZwtmpF_3wpSbhhKFHinVDl-kiztquN8W3RKyPUCXX-xbM5bbAp3B2P69RPRDt7IVgEk-4eqvmYZabLU5Xv5_TmAokrQP_Eb8MW-s1jYq8wB6LNReVmofAxmVHbzsmG0hVQKjyOIDz58X8R9uYGaPN3NQiLlK5JnSSqTe2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83519ba27a.mp4?token=Mo0Wq1NYHIV1q5uOQ69gLgATuKaFu--YzBu7oFf5AUVrNPZe4LMqYkYaQyOglRvZvPak9-fCxtGH3IxjbLXzHRi46uabPDgQChsZiS79wQlsrPGDzGldJurZEXDVcG8AeSvKf6dFEVmlzV7_Tr15VaMYrZT0gmjT-fiUn0FMx04MJpttZwtmpF_3wpSbhhKFHinVDl-kiztquN8W3RKyPUCXX-xbM5bbAp3B2P69RPRDt7IVgEk-4eqvmYZabLU5Xv5_TmAokrQP_Eb8MW-s1jYq8wB6LNReVmofAxmVHbzsmG0hVQKjyOIDz58X8R9uYGaPN3NQiLlK5JnSSqTe2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پلیس پاکستان داره عزاداران خامنه‌ای رو با چوب میزنه  دیروز هم پلیس پاکستان ۶ تاشون رو کشت.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5181" target="_blank">📅 09:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5180">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">بخش خبری ساعت ۱۴ شبکه یک و تکرار ادعای زدن ۳ جنگنده آمریکایی  در آسمان کویت و تکرار این سوال که چطور در آسمان ایران به این پهناوری نمی‌تونید ‌، در آسمان کویت تونستید؟؟</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5180" target="_blank">📅 09:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5179">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">فرماندار جم در استان بوشهر، می‌گوید که یک «پهپاد متخاصم» منهدم شده و وضعیت شهر به حالت عادی بازگشته است.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5179" target="_blank">📅 00:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5178">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از شلیک موشک از منطقه جم بوشهر به سمت چند کشتی که در تلاش برای عبور از تنگه هرمز بودند.
گفته می‌شود در جریان این حملات موشکی که از سوی سپاه صورت گرفته، به سوی یک کشتی آمریکایی نیز شلیک شده.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5178" target="_blank">📅 23:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5177">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7730b3f12b.mp4?token=lBw4JcWz2G_gUs7M4o8sHCy_bo_OXoHGm9SCowmZ1wCRTqnQeXeg6FR9j2n-RP0UVKq6COXy1ClVuoiXp23Wr8aNn2svJFk901KsYLTEGKh8OZTtHADNjwL_fQyd0__pwzDot0Ng32Z9CLDzjNlnKMjk3Xm6bxk7UecIKY_1Gea6smJBC2DYU0DMy8200wG9_dokTGsYTHsoDDRiV9knyRW2heZGYyoQfSU5zvaM-ZyE8uLDG-2-WIq09NZCNUmzshRoIxJUh1cgPTyYk0l0VzvCBRBnPq8YNdafMLcdLHokgY_0tG47zbXPpWbjDReKlkDeaCAwmtr-sYu_X74eDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7730b3f12b.mp4?token=lBw4JcWz2G_gUs7M4o8sHCy_bo_OXoHGm9SCowmZ1wCRTqnQeXeg6FR9j2n-RP0UVKq6COXy1ClVuoiXp23Wr8aNn2svJFk901KsYLTEGKh8OZTtHADNjwL_fQyd0__pwzDot0Ng32Z9CLDzjNlnKMjk3Xm6bxk7UecIKY_1Gea6smJBC2DYU0DMy8200wG9_dokTGsYTHsoDDRiV9knyRW2heZGYyoQfSU5zvaM-ZyE8uLDG-2-WIq09NZCNUmzshRoIxJUh1cgPTyYk0l0VzvCBRBnPq8YNdafMLcdLHokgY_0tG47zbXPpWbjDReKlkDeaCAwmtr-sYu_X74eDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف رهبر شهیدش رو پاره کردن :)</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/5177" target="_blank">📅 20:23 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5176">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bbac44461.mp4?token=aTMZ2UkUJSumuezE3XC70tvc7bTcuqzHKV8gLSVlngNuWy3yqlFS9qM6t-RpMG4HwAHg9S9jWJdqiA0DHtx-VFEpbEIZMpn7WchE1CC3HDlTc6RlMF25V9ROHHc_Z8csXdAZRv2UkVptHJJe4FYeZQz4T_LzEv9uxrgWBNNZ1OAwx3xwQZwalrL4OiPwKzZdI6SA4B7q-rJpOTddKT_4IoChHKNJ_E3SkB4kNrpWY-burAGeKXgmP-zkBzqGALkCK8nMeHCeJzhh_iPEC3Ok96kFeRK8vB-YMTJng-GwgyYJUG2Oou_Xa-tU5fGbEUW-liAeEMcDwd6Hu-rey2rY6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bbac44461.mp4?token=aTMZ2UkUJSumuezE3XC70tvc7bTcuqzHKV8gLSVlngNuWy3yqlFS9qM6t-RpMG4HwAHg9S9jWJdqiA0DHtx-VFEpbEIZMpn7WchE1CC3HDlTc6RlMF25V9ROHHc_Z8csXdAZRv2UkVptHJJe4FYeZQz4T_LzEv9uxrgWBNNZ1OAwx3xwQZwalrL4OiPwKzZdI6SA4B7q-rJpOTddKT_4IoChHKNJ_E3SkB4kNrpWY-burAGeKXgmP-zkBzqGALkCK8nMeHCeJzhh_iPEC3Ok96kFeRK8vB-YMTJng-GwgyYJUG2Oou_Xa-tU5fGbEUW-liAeEMcDwd6Hu-rey2rY6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد از ۹۰ روز صدا و‌سیمای جمهوری اسلامی می‌پرسه در حمله به بیت کیا کشته شدن؟
کمیل خجسته، برادرزاده منصوره خجسته باقرزاده، همسر علی خامنه‌ای، میگه  افراد خانواده خامنه‌ای که کشته شدند، همه در یک نقطه نبودن! در جاهای متفاوتی از منطقه بیت رهبری بودن که به همه اون جاها حمله شده.
این همون حمله‌ای است که پسر عبدالرحیم موسوی ،
رئیس ستاد کل نیروهای مسلح میگه ؛ ۳۰ روز گشتم و جسد رو پیدا نکردیم!
عجیبه در این حمله فقط مجتبی سالم مونده باشه!!
چرا خامنه‌ای در پناهگاه نبود
!؟</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5176" target="_blank">📅 19:41 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5175">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
آمریکا و جمهوری اسلامی به یک توافق ۶۰ روزه رسیده‌اند تا آتش‌بس را تمدید کنند و مذاکرات درباره برنامه هسته‌ای را آغاز کنند.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5175" target="_blank">📅 19:14 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5174">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/208f980645.mp4?token=l3jC8SNHjkNHY-UEZ30JGUD1MhI8AE0JGlb-EKpbLImZFl4D-fp-FkTXQP1xhN4HOY4jJev3JJEyZ60RjRG0LSHZLn6S_aCRlIwxcllWx36zbQjW3g8bi0-eH0h7APZ1a5Yb6VG28PIL_NOdBmeVnJfS42S9sSKEeIjKPat5_aYknysxCR8pL0ItcwXscyBWbzRU_C_kUwIGa6il6-mLVJr9h_s3UADuSz_XKWRXmBvO4Fm6t9VKasy7dJzv3Xl9fCFYIKCC94IAwuucY8VOZMtIzIJ928c2cvFfs8FIo2KpKlLKVvwKsZ0j3-tQf2P4klROjbbWRB-N6tZoe8C7Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/208f980645.mp4?token=l3jC8SNHjkNHY-UEZ30JGUD1MhI8AE0JGlb-EKpbLImZFl4D-fp-FkTXQP1xhN4HOY4jJev3JJEyZ60RjRG0LSHZLn6S_aCRlIwxcllWx36zbQjW3g8bi0-eH0h7APZ1a5Yb6VG28PIL_NOdBmeVnJfS42S9sSKEeIjKPat5_aYknysxCR8pL0ItcwXscyBWbzRU_C_kUwIGa6il6-mLVJr9h_s3UADuSz_XKWRXmBvO4Fm6t9VKasy7dJzv3Xl9fCFYIKCC94IAwuucY8VOZMtIzIJ928c2cvFfs8FIo2KpKlLKVvwKsZ0j3-tQf2P4klROjbbWRB-N6tZoe8C7Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش زدن ظریف :)
نوبت عراقچی هم میرسه!
این مسیر رو خیلی‌ها رفتن!
از منتظری و بنی‌صدر، تا موسوی،
خاتمی و روحانی، احمدی‌نژاد و…..</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5174" target="_blank">📅 19:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5173">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47b8458a9e.mp4?token=b5xatZ3Hf8TWr1OyYUcAw7xb4YOX074Dw20kda3ETmivjE2Ppyt2nglRtzMIMgHmppc0jEPBZJiAS327BLieLkBfsRO4EQyb2K5I5DmzguTgHc9zYDcHxoPSIyj-nuQ8L81xmyOvG_-aA2Gvgv-YaheZOCYQpbTlA29L1Ajljz0_ypGqZFD2CImO-VHq14EHuDIIpNIDeNHbaQTupVRYNd_XJTIvIaWXpVjRgeZLJuAXzpsY-SzSa5oV-S8LjYTQSMs4WtbBY2-rQzK4NYSILakYVWteBi7q41Sk4rfsEZyzPaOjF3NVuMFuyCf7vKQKtIgChftDqztwTFPXx6KhPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47b8458a9e.mp4?token=b5xatZ3Hf8TWr1OyYUcAw7xb4YOX074Dw20kda3ETmivjE2Ppyt2nglRtzMIMgHmppc0jEPBZJiAS327BLieLkBfsRO4EQyb2K5I5DmzguTgHc9zYDcHxoPSIyj-nuQ8L81xmyOvG_-aA2Gvgv-YaheZOCYQpbTlA29L1Ajljz0_ypGqZFD2CImO-VHq14EHuDIIpNIDeNHbaQTupVRYNd_XJTIvIaWXpVjRgeZLJuAXzpsY-SzSa5oV-S8LjYTQSMs4WtbBY2-rQzK4NYSILakYVWteBi7q41Sk4rfsEZyzPaOjF3NVuMFuyCf7vKQKtIgChftDqztwTFPXx6KhPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله یک مرد مسلمان چاقو به دست در محوطه یک ایستگاه قطار در سوئیس موجب زخمی شدن ۴ تن شد.
او با فریاد الله اکبر دست به این اقدام تروریستی زد.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5173" target="_blank">📅 14:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5172">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cba2527ef2.mp4?token=HB6o9-E68iQhbglI1VqUp6F9VqqHN765e3SDzs32y0IH6H9eES7kSwA-5KGWIRcl6p-8y8jIoaC9wWZj2iaSNJnZzLH6kxMKbhyeuQOrfeRUbxU144LH_39fbNZJBd8Vs9NvgVTqldxQ68RXTSxGzZSBs3Y9fLQKz0JaZmo7L6O2tQA6cwP7ipwC2eXnmlh2ym-T7q-_SENJWCpW1_DBJahoWTgl6GbPB3JKUfpmy0Ox84P_uiApN_GUXKlH9GxYuoehJBkwrBYRhy2IXSDoCGwUqcNUZPYPUbbLxP6CHD6Qog-YujLffum6MGO5bRO2oDgz4mEtBE2nb1uLP55Zdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cba2527ef2.mp4?token=HB6o9-E68iQhbglI1VqUp6F9VqqHN765e3SDzs32y0IH6H9eES7kSwA-5KGWIRcl6p-8y8jIoaC9wWZj2iaSNJnZzLH6kxMKbhyeuQOrfeRUbxU144LH_39fbNZJBd8Vs9NvgVTqldxQ68RXTSxGzZSBs3Y9fLQKz0JaZmo7L6O2tQA6cwP7ipwC2eXnmlh2ym-T7q-_SENJWCpW1_DBJahoWTgl6GbPB3JKUfpmy0Ox84P_uiApN_GUXKlH9GxYuoehJBkwrBYRhy2IXSDoCGwUqcNUZPYPUbbLxP6CHD6Qog-YujLffum6MGO5bRO2oDgz4mEtBE2nb1uLP55Zdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله هوایی اسرائیل به بیروت
🔺
آمریکا از دولت اسرائیل خواسته بود تا به بیروت حمله نکند
🔺
گفته می‌شود که در جریان این حمله، «علی الحسینی» مسئول ارشد موشکی حزب‌الله لبنان، که در واقع یک عراقی است از «فرقه الامام حسین» از گروه‌های نیابتی جمهوری اسلامی در عراق، کشته شد.
🔺
اسرائیل دیروز هم در حمله‌ای به غزه، فرمانده تازه منصوب شده برای «گردان‌های قسام» (نیروهای نظامی گروه تروریستی حماس) را حذف کرد.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5172" target="_blank">📅 14:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5171">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">علی الحسینی‌ از فرماندهان ارشد و مسئول واحد موشکی «فرقة الإمام الحسین» حز‌ب‌الله عراق در حملات امروز اسراییل به لبنان کشته شد.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5171" target="_blank">📅 14:44 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5170">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dYiZypZyOFXIsHdjLfZC-TgbckuJ4L0DV8ooZjSZn7OK2FMKE_6q0DlZhKJzOGsvKGSR8Aq1j-B2iac-oh0u2jSLLN1AJ3OYayf6smlHxFe5fP8OBR_FZwT5B3GHJviRRn5Hh1Ubq9eU6_HhjVOb96I6LBZcu1DCU1HwGsLONg6quBKiXOlt8hdDRvbu_N2deJeCZj3SRI_DOnvr1d7TZ0G4C6T9KFmYI85MZV_HITKNPmP7VgmmrrILYXtdAEj2DS-7sNle-xskeiirwc-ulN9q9klICeuhyVD9UPwh4vPrFcJAijUmw4ezHFsVGwJIdRzA_IYY5PepiRhqEzeI0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه سنتکام:
ساعت ۱۰:۱۷ شب به وقت شرقی آمریکا [۵:۴۷ صبح ایران] روز ۲۷ مه،
ایران یک موشک بالستیک به سمت کویت شلیک کرد که توسط نیروهای کویتی با موفقیت رهگیری و منهدم شد. این
نقض فاحش آتش‌بس
توسط رژیم ایران، چند ساعت پس از آن رخ داد که نیروهای ایرانی پنج پهپاد انتحاری را به پرواز درآوردند که تهدیدی جدی در تنگه هرمز و اطراف آن ایجاد کرده بودند.
همه پهپادها توسط نیروهای آمریکایی با موفقیت رهگیری شدند.
نیروهای آمریکایی همچنین از شلیک پهپاد ششم از یک مرکز کنترل زمینی ایرانی در بندرعباس جلوگیری کردند.
فرماندهی مرکزی ایالات متحده و شرکای منطقه‌ای همچنان هوشیار و با تدبیر عمل می‌کنند و به دفاع از نیروهای خود و منافع‌مان در برابر تجاوزات بی‌توجیه ایران ادامه می‌دهیم.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5170" target="_blank">📅 14:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5169">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f7f2acbc1.mp4?token=vVoSF1zCahQ2Ud6UuFFDGUCvJ58KxrHehYQEnrXu-roSLUIM-c-kOqLX2_h-5U_OVGKEV_Tggr3YUM4Qla8tYL0-tqudov69_nS_a3uJ637KVM8bbDDhJmpQhTijZfh8_aO0CjTrlA30hZC5X_jetVPTXp2yMhk3XuUmuiCpKjkiE_qP0UkAceEK6b6Gnf8Li4FsKUNajaoooiQXk_amrS4OzkkiZNnNmMImCvJyG14QLYiZ4a8J2PML3ssCIeIfoj9GEqGx0_6BeY7EEyHswDga13NXJBxsLNKBhTnMEF9pwC-mF9tNpvIM7jiFnU_II34u5h8dm02vJ8oXqM9GwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f7f2acbc1.mp4?token=vVoSF1zCahQ2Ud6UuFFDGUCvJ58KxrHehYQEnrXu-roSLUIM-c-kOqLX2_h-5U_OVGKEV_Tggr3YUM4Qla8tYL0-tqudov69_nS_a3uJ637KVM8bbDDhJmpQhTijZfh8_aO0CjTrlA30hZC5X_jetVPTXp2yMhk3XuUmuiCpKjkiE_qP0UkAceEK6b6Gnf8Li4FsKUNajaoooiQXk_amrS4OzkkiZNnNmMImCvJyG14QLYiZ4a8J2PML3ssCIeIfoj9GEqGx0_6BeY7EEyHswDga13NXJBxsLNKBhTnMEF9pwC-mF9tNpvIM7jiFnU_II34u5h8dm02vJ8oXqM9GwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسلام یک دوره کوتاه از رشد علمی داشت،  که همیشه هم سنگش رو به سینه میزنن،  ولی حتی اسمش هم گویای همه چیزه!  «نهضت ترجمه!» رفتن شروع کردن به «خوندن» کتابهای دیگران!  کتابهای ایران باستان و یونان باستان و هند و روم و……  خوندن و ترجمه کردن و شدن باسواد !  اونهم…</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5169" target="_blank">📅 10:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5168">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i-m2jOFzzSZs7N1URhTHf3XqP6b1T5oT68kiYACiPVHJc5Mz8fRIU2zFJXq6jleKUhMzgEdvFvOJI1Ta_joDzqlK_GYbogRliOd1pF7hFrQlNrbb5ifCQTw7r_CChxpKWZgW05ZLs5JunxLk4Hx6PWDLxjxV3wIKrvTUiwJwYQvyEocNbGSXfHkRcZOOcOhi65COmFP3QYubgkVeJiuQvVTL7haOy1_lih1TdO4pT7PBC8402XSDuAshZCSQyOm4zXt-y2ZTyK0q-AR-MK73fpbTqOB2ft8fbH5FqFzQCfhSybadc-wHHdRiwtfU4srVL500L2dGsVHOUqntS4ip4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سر و وضع شهردار نیویورک رو!  دیروز !  جوامع مسلمان، از غربی‌ها، آموزش مدرن رو یاد گرفتن، آموزش دختران، مدرسه، دبیرستان، دانشگاه،  انتخابات و حق رای، تفکیک قوا، داشتن حزب، داشتن انجمن و سندیکا، داشتن روزنامه و رسانه، سینما و تئاتر و موسیقی به معنای مدرن، مناظره…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5168" target="_blank">📅 09:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5167">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67cdb18f71.mp4?token=D6y4Lv1h7eSbGkGlajWom_cdcBJ7rylQwrxuGiEMds9JhHE6uRpgBD0yi_F1u7eEX60jDISNaURO_X0nqp1xqe2r9eK0l3cEr5xSk_DEoLfPRUtSWXLQ_6L1rPNkXE4H0WUHos8gvskT2HFP0ZeOCW5-jLUhjxPzr3hHIic5QsldKzk0hUSTBThzn512C8sceHEqniKtkWGZ3AWz2yW5c94sQI7WZmGS-AdT9ndkXkNK3Tf2jvA2j0dfZEMxpMYQqjrKXseEsl0ZC1htYMcoOsVkCJnvoeF16usOM6vM4gyNczZbViXrcGGYuwfmwltJf1ANRwELd62KVAGpaX6NLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67cdb18f71.mp4?token=D6y4Lv1h7eSbGkGlajWom_cdcBJ7rylQwrxuGiEMds9JhHE6uRpgBD0yi_F1u7eEX60jDISNaURO_X0nqp1xqe2r9eK0l3cEr5xSk_DEoLfPRUtSWXLQ_6L1rPNkXE4H0WUHos8gvskT2HFP0ZeOCW5-jLUhjxPzr3hHIic5QsldKzk0hUSTBThzn512C8sceHEqniKtkWGZ3AWz2yW5c94sQI7WZmGS-AdT9ndkXkNK3Tf2jvA2j0dfZEMxpMYQqjrKXseEsl0ZC1htYMcoOsVkCJnvoeF16usOM6vM4gyNczZbViXrcGGYuwfmwltJf1ANRwELd62KVAGpaX6NLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سر و وضع شهردار نیویورک رو!  دیروز !
جوامع مسلمان، از غربی‌ها، آموزش مدرن رو یاد گرفتن، آموزش دختران، مدرسه، دبیرستان، دانشگاه،
انتخابات و حق رای، تفکیک قوا، داشتن حزب، داشتن انجمن و سندیکا، داشتن روزنامه و رسانه، سینما و تئاتر و موسیقی به معنای مدرن، مناظره و مفهوم «شهروند»، دادگاه و وکیل و حقوق مدنی، پزشکی و بیمارستان مدرن، بروکراسی اداری، مفهوم حقوق فردی، مفهوم و ارزش آزادی بیان، مفهوم دولت و ملت، سرشماری و شناسنامه و داشتن فامیلی و..
صد مورد دیگه!
مسلمان‌ها در دنیای جدید چی داشتن؟ هیچی!
هیچی!! لباس سنتی بپوشیم بریم توی خیابون هاشون نماز بخونیم و بگیم خدای ما از خدای شما بزرگ‌تره!
با نخوت بگیم ما خیلی از شما بهتریم!</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5167" target="_blank">📅 09:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5166">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🚨
سحرگاه امروز ارتش آمریکا به ‌منطقه‌ای در اطراف فرودگاه بندرعباس حمله کرد.
سپاه نیز در اطلاعیه‌ای اعلام کرده که در پاسخ به حمله آمریکا ، پایگاه هوایی مبدا این حمله را مورد هدف و حمله ‌قرار داده.
بیانیه سپاه اشاره‌ای به محل این پایگاه هوایی آمریکایی نکرده.
اما خبرهایی از فعالیت مقابله پدافند هوایی کویت در برابر حمله پهپادی منتشر شده.
🔺
برخی رسانه های حکومتی نوشته‌اند که یک نفتکش آمریکایی قصد عبور از تنگه هرمز داشت که مورد حمله سپاه قرار گرفت و در واکنش ارتش آمریکا دست به حمله‌ به اطراف فرودگاه بندرعباس زد که ظاهرا مبدا حملات بود،</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5166" target="_blank">📅 08:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5165">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ  به PBS News: «جمهوری اسلامی غنی‌سازی را کنار خواهد گذاشت و «هیچ» تحریمی هم برداشته نخواهد شد. هیچ خبری از لغو تحریم‌ها نیست. »</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/5165" target="_blank">📅 19:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5164">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nH7uQ50kpeeFV3dP8J54uM9m7c5JqJ8SRnOoDiIECwwKD-eqINs45aUfQKtWqIUTq00DGD80GVniVsPP1K-gUgS6Atyw7AKzrh6kFPgMxk6RbW_kac49acm2j-q7smZxADAQf7WUnCJse45e2oXXcZ_PNhvsKHJZQtrFGTSR1CaaBraXmqdayNiv-LMyFFPfPnT8tP1fNMTNeQzzUMzkG4d1m06uv848Pf3sQUw9Xku2TL2MOt1YdEWslnacTVN0rnwR7hvLatJK1Ve0ucaA9fzFCmCBKU8VNeD0_telgXU02tr0EgZOvLooylgwFUZj1KRgluu3-aHkZttauBBozQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۳۵۳ سن  حداقلی ازدواج برای دختران ایرانی از ۱۵ سال به ۱۸ سال ارتقا یافت.
جمهوری اسلامی اما سن حداقلی رو
به ۱۳ سال رسوند تا کودک همسری کاملا قانونی بشه! جمهوری اسلامی اما ازدواج زیر ۱۳ سال برای دختران رو هم مجوز میده.
فقط باید دور زده بشه، اول صیغه جاری بشه
بعد برن دادگاه و قانونی اش کنن! به همین سادگی!
در بهار ۱۴۰۰ ، حدود ۱۰ هزار دختر ۱۰ تا ۱۴ ساله در ایران شوهر داده شدند!</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/5164" target="_blank">📅 12:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5163">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qa_lpvB0E28nK59Wk2W81fQ9s50nAQUPgG47q7aQcQkqNyMlrxMzTEkIFGc_xQsoabu7JwXieMc0QVF2P_HRCNeqUv9VbMfRGJS83Vk1Lc7yYJ-ZSu5qFcROpknkI6loXfr1yocZdRVwfac4wz3z_d46zPlbm_kG40BdGL-8B3VRIXEyIAipKK8bzbZIma4ffb8t36YxR2mVqfDtCjYexS_OyUMQLJkySb-zvbAM0LqD6scOaB5aCzc53mI_-0M1Ljd6PcdcXjntUUB1Ezwc7ktrakgvdch9bmhvOCSw2PjHKIbpdTqGmNDM-EoBWeH4_p1I4PQfi8yqXDpa1LY_uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،  یا به اصطلاح روشنفکران و…..  تا این اندازه در آغوش آخوند هستند و مدافع آخوند!  «ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.  اینها ایران رو سنگری میخوان برای مبارزه با غرب و با اسرائیل…</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5163" target="_blank">📅 11:08 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5162">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKFY3-hzqeNTBhZ1g7VYx9dqWDYv5Dl-cjP8hhRGVNt0v2-e9Jv197nI6B6q8NuHBx2ODU6lgp7vkSOzMo2Plt6AEJomp6ZrVaWrvUgIL7snZhfGlVMVGkB9cuwTPG-raly1tvzTdSqjZbIItroFlCF2jSXSIV38SukdfsMaHGOi9vyaNArgh5y0Yls-GTaHnGGJM6WFg8bHaaEeFMPCgOAw3U3SXke2vys9eKjP-h3YGJbWSkyxbYGlHx0UYZlW3Y9EtCiF-L2aJI13-i1HhGJj5YTJD-6ugzJAFUqU4HiNbfrwhASkEk8_yt1EjhLaZIIDM4QD-1Twyi5_CZFLdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسه هم که فکر می‌کرد زرنگی کرده و با حاتم بخشی از خاک چکسلواکی، کشورش را از ورود به یک جنگ رها کرده، هزینه بسیار سنگینی پرداخت!  به قیمت تصرف پاریس به دست آلمان نازی!  آلمانی‌ها دقیقا با سلاح‌هایی که  از کارخانه‌های عظیم نظامی چکسلواکی  به دست آورده بودند،…</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5162" target="_blank">📅 10:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5161">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lsh5CGFJJ0GZ3ncpyLWWwISJu0tR1KQ-D53v0yY7z0Y4Oh2cn0QKo53pMmgOXrSRC88mZS9oIeOHFbsij9fd_CE4ZAk4VmVMeED8RDUiHRO_nnVvQiItc3NqN6fNoec6eqlV0czsLwHrNGixy_0pSikCkR5PivGVIgtsfNNNZJe4XQrQnBOpFY_AEv-uMBnJHZaOfjKiv1kQDHVwHp7Z1ArGj7aR1P1JKEfE_C1crPKgfCuQy0joLDtuCW5IkjfN-K3kgE0SsXIniVHRzV7jqj0kD794FuRUz_TUwXw2Uo7GHbN81qKp0jvYmyFK_kIXrWUw8YyQf9RLa_5CgMi08w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرچیل اون موقع نماینده مجلس بود.  دولت چمبریل رو سرزنش کرد و گفت :  «به شما حق انتخاب میان جنگ و ننگ داده شد. شما ننگ را انتخاب کردید،  و با این حال جنگ هم خواهید داشت.»  پیش بینی چرچیل خیلی سریع به واقعیت پیوست! آلمان این مناطق چکسلواکی را گرفت اما دقیقا…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5161" target="_blank">📅 10:11 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5160">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6gcPH0ILYY2N7LSpr3c-3nK72U_kAsHp9G1Pw_e-jafUGDUs3D12gnnEwmQ0-7hKjdolZ2keQZWfP3A5EbS1HtZa6DrRIV_ACdOcpwNqMtHEh6ZEWR10jyfE60_RuZEIBiHkQVnVwyqE78Vc8GsjIkZsk-ez8-_l6OqvyJ8P7MK50kcAui5HkhfjalhT-L9eIxJpIIBrytKvfMKIBB23docVhf1_oEar85Fbe0y-ESF1X6ZcU3rwCwgXGoFHC094QqdkhnwbtLLRRUqwiB5nh0uHhFmuRsS3FCb0jSUw6sBdsbgiO37C4lfSrq5QIj6zekwZYo8AkUthsSgRND5cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چمبرلین، در صدر دولت بریتانیا،  به همراهی فرانسه، قراردادی را امضا کرده بودند که بر اساس آن، ۳۰٪ از خاک چکسلواکی به آلمان نازی داده می‌شد.  مناطقی که مردم آن آلمانی زبان بودند.  هیتلر میخواست همه مناطق آلمانی‌زبان در آلمان باشند .  بریتانیا و فرانسه، عامدانه،…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5160" target="_blank">📅 10:04 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5159">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Md7x_9Lleu9u89u_0STzzFUmNd2fJVD5gStqHPQ4afgHmjpStNll7T4Ppq2vmATHM3SBoJp3uudAwL_R4bBcwFyTvTcLfmxzWOjDbRZMn5Wll2wpV-KnPqHY5AEneY2EUguITJBuif5JM1NKFWpLAUYWbgl-gQEDvSe6dK6jUSF_Sig_F9bwmcIDz1JIJc6eiBQ0UmC7qVmFE7PnAusDcYv4zOm_HvLClZc0BZpfbLkqmSJfUhhc7v9W7ar1G_LBMdFyQhFpJfLpFapGVr7F7_sag6STLZIIjovzo8K-VETarS184vUsUZXIFw2McDWTR5JSrQVT6kNT5vo5QcQ1ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۳۸ چمبرلین، نخست وزیر انگلیس  با این تیکه کاغذ به لندن برگشت. کاغذ را پیروزمندانه به خبرنگاران  و جمعیت انبوهی که جمع شده بودند نشان داد.  او می‌گفت که به یک «صلح برای نسل مان» رسیده ایم. می‌گفت این قرارداد اروپا را از افتادن به دامن یک جنگ بزرگ نجات…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5159" target="_blank">📅 09:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5158">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PsTANk0b7-zd9qClaLqdo8vA520k3QkeJCUoYz5b1lwgeClM98lEVqK2iPOTfxwnnD8rB_pH7UgOqdJw5x_KjZpJK0_a0Y-1DdMm-vuK6JKTL0xMDhP_-EtVwyL-xGHvG9F1XGCPeChscvmWaOtl3Y4Xe_kp-q-MbscTT73p-E2k3rQpHwmERlkCbx7MWbTGLnceFkgAguN7IlXaZoGFibMDC3QRpdCaThLrnCr79An4hZ8tpCVCg-SCHGQobDAncc0WPUqUb7ZXqMysHMjATZssS2YDdTj4q7I_MXjqQGa8cu6uaLeMhwmSsE1iD4UsAiMJOGGcwOsU_1rQ2xsQ1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۳۸ چمبرلین، نخست وزیر انگلیس
با این تیکه کاغذ به لندن برگشت.
کاغذ را پیروزمندانه به خبرنگاران
و جمعیت انبوهی که جمع شده بودند نشان داد.
او می‌گفت که به یک «صلح برای نسل مان» رسیده ایم. می‌گفت این قرارداد اروپا را از افتادن به دامن یک جنگ بزرگ نجات داده. این تیکه کاغذ اما یکی از «خیانت‌بارترین» قراردادها بود.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5158" target="_blank">📅 09:47 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5156">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PwqFaAczgWw8KkUKiKhy2X1evRNOJ9vt3VZeQ4R0bZsocrsVXSn1703Ev8KXlMs8jC5jdiBYL_37hIT9R7dXz61wKdLWgsw2jB9gqFjicnLe9H06HWrJCk6aN5TGUaWPGkFC4Tclua70xgESHGDXWmMB73WQlhHlpHutD6aca4CUY489vTqVQQ60l_YATGkeY0KVAhrJe2RG9SJPOd05N9aSos7QEPO9GT1tEmPa2EClVon14yWAv9eBm2ZahvHagZ62RmqoQyBAFxDS2T2Kdmos0VxYBJ-75y7kp6mchrFu0WALVPIGAyTacfd0MI3t-qHD4RrXQQ7GQTkbYhOhNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما دیشب بعد از انتشار خبر شنیده شدن صدای انفجار گزارشی تهیه کرد و گفت : منبع صداها مشخص نیست!
بعد صابرین‌نیوز و خبرگزاری دانشجو و… حتی اسامی کشته‌ها رو منتشر کردن
بعد سخنگوی سنتکام رسما گفت حمله کردیم و زدیم و…!
دیگه صدا و سیما در همون مرحله « منبع صداها مشخص‌ نیست» موند که موند و داستان رو ادامه نداد .
«مصلحت» نبود!</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5156" target="_blank">📅 23:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5155">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fbae4d271.mp4?token=eKddSKPQL-hgz9pTDpDuhQSu2n-Crsxx-mQubSIadvgaUNVS9JyEu_UbUeWBZAdhGnHEyA4xw0CsWq7mhDw7S469Abf4exWCjyAZyZzwKnzUC7gnejdBqPkR9LAhcPDXFhG_FKo4ZSSSUDI8w8hgvfspqgXYqpkjMOYyRLXmuntEvukCceqW-N_NUbwHMyLZcIEBpWnJZk3fchkL--HEqvCNVtuTG_PGl1A-fZtkeBUtn669OaQIur2YLKDXpFiVVZwHfzzmB4OFLZ4uU_viEzHPEPf7-ub2j7M1YO-BghSTxsX7fGfwfUAryiYGZX67QdFbrEnLHuQ2XeyzH-b2XA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fbae4d271.mp4?token=eKddSKPQL-hgz9pTDpDuhQSu2n-Crsxx-mQubSIadvgaUNVS9JyEu_UbUeWBZAdhGnHEyA4xw0CsWq7mhDw7S469Abf4exWCjyAZyZzwKnzUC7gnejdBqPkR9LAhcPDXFhG_FKo4ZSSSUDI8w8hgvfspqgXYqpkjMOYyRLXmuntEvukCceqW-N_NUbwHMyLZcIEBpWnJZk3fchkL--HEqvCNVtuTG_PGl1A-fZtkeBUtn669OaQIur2YLKDXpFiVVZwHfzzmB4OFLZ4uU_viEzHPEPf7-ub2j7M1YO-BghSTxsX7fGfwfUAryiYGZX67QdFbrEnLHuQ2XeyzH-b2XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علیرضا دبیر: کارمندان بهایی من‌وتو می‌تونن
در صورت بیکاری، تو پارک دانشجو مشغول کار بشن
مدیرِ تراز جمهوری اسلامی</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5155" target="_blank">📅 22:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5154">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/umh4bvKRMzGl8LYygGtO6R7GTVDgZW0vcsSHwrcKwrV8YSeOC1xk38DoJGe6cuvsIgkoaXkw0sDwMinzRu_pEfPYqzdvtmn7i845BGODJLsPam-yqBCuV6O2QfNGbAmKDhU98-r19-s3dURD9QUkXJNS3DeTb02vno7DjXRtU7mVbpM15jHRnzvBloBQ8zn04mFsnKVfVpwgahOiBWGUnxepuza6xFdYeSRmBdzLML4V8SADz8Rze74pwRh5iE78FsCI_s7XN0ohIPj4SlmjF2PlJYMwGJqJcVOtYS06-E3DeRwyUtVLx5YCBV-66bsi5hz69bdfVdlAW5SbD2bSMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاریکاتور شارلی ابدو
از قصد جمهوری اسلامی برای گرفتن پول برای عبور کشتی‌ها از تنگه هرمز.
آخوندی که میگه : به نظرت
چقدر کاغذ توالت بهمون میرسه؟
اشاره به پول ایران و بی‌ارزش بودن
ریال ایران که ارزشش در حد کاغذ توالته.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5154" target="_blank">📅 20:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5153">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‏پیام منتسب به مجتبی خامنه‌ای به مناسبت حج: رژیم منحوس صهیونی ۱۵ سال آینده را نخواهد دید.
باعشه!
بابات هم همین‌ها رو میگفت که باعث شد امروز ۹۰ روزه که معلوم‌ نیست هستی یا نیستی، اگه هم هستی طوری قایم شدی که گویی هرگز نبوده‌‌ای :)</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/5153" target="_blank">📅 14:43 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5152">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2PxmyGe9p_I6A1oloo2_pvLbGc97f5DUnwITGetNTZaHcTp3gFo1iATH8M8ln8Vc6RvJAuR0TU3h0HLIxxSqL9PCHx3gUt0Y-rJ7PyQ9hZWXCz22VhmamacMEDWH-vbaQfezh8dNhbGterkqcOJ6kjH63uqQT774v_EZdA_kA1ruXw18R0NNkmjjIlyi10ZjsSrWNRu8qapg67kd0WuPkHNl34G0hulMLGBrazdLSdQTn8i79whVvHzVjEKGYHV7-1K3wV0IVc8sjCofxviXvTXzSEOtrDL-gq-YD517SAHJIRYqGMOKhFt8TCfmpmoOiwjYKdHIdya3zZXTAPVig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ذوالقدر دبیر شورای عالی امنیت ملی، میدان جدید رو معرفی کرده که هیچ کس نباید حرفی بزنه که وحدت شکن باشه!
دستور خفه شدن همگانی تا رسیدن به پیروزی!
اسمی هم از مجتبی خامنه‌ای نیست.</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/5152" target="_blank">📅 05:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5151">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hpQpD5s3IQVb4d5h3XFhwm1DrCYSd0jVg3uL_6i82VCi5azwnhmv7_rafqcEDahj4NSJJ7ZoMwljE1n57hBSzphdrVGeRRp3jeyP4sNa9gugTDabULG-LXPxCALvYN5UF2xiPw2mLk2mVJVh2bbtQgK-Hf7-dMRP1U4RdjFGPx3oKVzbM7G7H3w6_pCniUw8-yQFf9DdxHQxskKZxGQkv6yhS4cJpIXF-aagotDJvPDc16M0HfCKJCGSSSyVuMbN0hjod4pfCFlnvFbnMREipNz-QElaECFRwRH1oi_ue6AIHT_QxZ6XbugHeTjVfPQzP2IaG50hK1qBVOuGCvxg_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا حملاتی در جنوب ایران انجام داد / کشته شدن چند نیروی سپاه.   سخنگوی سنتکام رسما اعلام کرد که جنگنده‌های آمریکایی به چند سایت موشکی و دو قایق که مشغول مین‌ریزی بودند، در اطراف بندرعباس، حمله کرده است. خبرگزاری دانشجو، وابسته به بسیج، تعداد کشته‌ها…</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5151" target="_blank">📅 04:57 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5150">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aSkaAwH6BbjftblMEKC6jpAP6b02Dg5no67hHvMERJOVZ5cQQNPZy4ihjYKbHPWsngZWY8U_hef92ErwDgfbrawcWFfwomcSf71zPWLwoR6CvTJ0KzPfBLGvjjAw5tAdPCw64UKeNqf9jBz4wb4Irnq7JX4f6k4bjQS-X_HEGOUZFDIaQanT0vUsvTXUHrufkmm7knQ53plLeW3vWcmNal_9XPvLldNaMSy9B9QWbuu5Q3HtSJfhaVblqUSCjl3X0SP-RimbJHiW5EqOArhTWWgFuQynox46BUdoc14Ob86_vViQnJXjtN5w7jict4GczZd9ZYkvFtbbSSvOiPJMXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا حملاتی در جنوب ایران انجام داد / کشته شدن چند نیروی سپاه
.
سخنگوی سنتکام رسما اعلام کرد که جنگنده‌های آمریکایی به چند سایت موشکی و دو قایق که مشغول مین‌ریزی بودند، در اطراف بندرعباس، حمله کرده است.
خبرگزاری دانشجو، وابسته به بسیج، تعداد کشته‌ها را نامشخص اعلام کرده اما اسامی سه تن  را نوشته.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5150" target="_blank">📅 04:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5149">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ترامپ : یا یک توافق عالی برای همه خواهد بود یا هیچ توافقی نخواهد بود.
اگر توافقی نباشد آمریکا به جنگ بازمیگردد.
کشورهای منطقه باید عضو پیمان ابراهیم شوند.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5149" target="_blank">📅 17:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5148">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">قیمت نفت : ۹۷ دلار</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/5148" target="_blank">📅 14:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5147">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vFgzTZI3w6CMr1tJVhpQe5-g_v2ReeJBQ8o1RLUwC2M-DwcfYLHorNEUD1tf2VDz3pIbDO5pkHM_zDTRJ4dJSKjCLOIHo7Sj5bhL92u1jTbaNUyfXo4HkJuVCwD6ZJlOE6RlGyDFZPJdJkuyoNvKlAEoIbQ3CXFS4IcWlU_i7cjZ4dJtfVk6-TPIQqe0W8ze32OepcgW5TW-KtzhO9mzkNgA75GRQIcY5nCQduxfYPumZm7ouwkkrbfVH_MSYyCYQTpC8Q5idvI8YvNan8H2RYoNoBXtyuF2Ww4ZhEROS9LWONFUavfJX9q3XuhSw96BtJmMqVAhDmVvmYW79CKBAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که صدا و سیما شیپور پیروزی میزنه و از موافقت آمریکا با هر ده پیش شرط جمهوری اسلامی میگه،
سخنگوی وزارت خارجه امروز گفته : کسی نمی‌تواند ادعا بکند به توافق نزدیک شده‌ایم!</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/5147" target="_blank">📅 14:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5146">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔺
بقایی، سخنگوی وزارت خارجه:
آمریکا به عباس عراقچی، ویزا برای حضور در سازمان ملل نداد.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5146" target="_blank">📅 14:16 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5145">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77b6861470.mp4?token=U2crS2fV7fcmNGOMJtAj-zJjG3uwyF_o_sIoei0OD_jjMhZaSDXNEiKJ6aemt1nvHJPVLj8_tXZjkl_6-6R53jZv4EwJQOVkKO2c8ez0K9JGzT3TDW9ZYNhEjWxvwPcYBpyjRMSHp4thktjeilxlMPvk6Z1Fa7t6akugLLojbEud2Gs8e9ETbJuJe-MwOYeNeB0i-mwEzNMJ0oznFQrDgTIvdc339T4KWON8FviV8dxKoBGiJkgbD0389y6Qv66HPhwb4pgkD251jgRlM2QikwOqALXBWuADPhNfe2CIfOChcjC2kbwFu7eEuF1Egsok3BzUPaBlu7Wc0ezkVBcdzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77b6861470.mp4?token=U2crS2fV7fcmNGOMJtAj-zJjG3uwyF_o_sIoei0OD_jjMhZaSDXNEiKJ6aemt1nvHJPVLj8_tXZjkl_6-6R53jZv4EwJQOVkKO2c8ez0K9JGzT3TDW9ZYNhEjWxvwPcYBpyjRMSHp4thktjeilxlMPvk6Z1Fa7t6akugLLojbEud2Gs8e9ETbJuJe-MwOYeNeB0i-mwEzNMJ0oznFQrDgTIvdc339T4KWON8FviV8dxKoBGiJkgbD0389y6Qv66HPhwb4pgkD251jgRlM2QikwOqALXBWuADPhNfe2CIfOChcjC2kbwFu7eEuF1Egsok3BzUPaBlu7Wc0ezkVBcdzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمایی از شهر رفح در نوار غزه و پیروزی‌های محور مقاومت
قبل و بعد از  حمله تروریستی ۷ اکتبر</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5145" target="_blank">📅 13:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5144">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل - توی این مایه‌ها -  گفته: «در پاسخ به هر حمله پهپادی انفجاری حزب‌الله، باید یکی از برج‌های بیروت رو هدف قرار بدیم.»
حملات حزب‌الله به اسرائیل رو یا دولت لبنان باید متوقف کنه، یا اسرائیل.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5144" target="_blank">📅 13:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5143">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VJgpXwyA7saZH4kqottUy-OfJA1FCQEF7puPtFmFTVgLhgV-Zmd9SY2ez6dtpvNchlkgw0xqoborOTATYj3rhYqz3oRaRZdNUh57waUrnSAsofjuM-4O6LZFtcH6EOzBq2tLofTXlG4NttyU92TBC1y9m-vhYiJCDOC0-j3Yox8V-IJnJLY3G5UDXfN7WOKGq8Lzr-p92cd4MWUqTPnm3gX-v9no_sc270GAAXFQTthD-93awktcKu4-b69lcmXhzdcRc5kxmmTYhFUbTnrvZ4ZeI6ln3KH4UpDchI2rDQFxGqkBL-Bp9T1RbFK6BRIyZRHxHve_ogI9rjBbVDVODg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبح در ایران با اذان و با اعدام جوانانش شروع می‌شود.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5143" target="_blank">📅 11:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5142">
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5142" target="_blank">📅 11:04 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5141">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">صدا و سیما:  آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده   ‏۱. آمریکا متعهد به عدم تجاوز به ایران شده  ‏۲. استمرار کنترل ایران بر تنگه هرمز ‏۳.پذیرش غنی سازی ‏۴.رفع همه تحریم های اولیه  ‏۵.رفع همه تحریم های ثانویه ‏۶.خاتمه تمامی قطعنامه های شورای امنیت  ‏۷.خاتمه…</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5141" target="_blank">📅 09:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5140">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc885feb3.mp4?token=Tpo7eLYup46SSF-lSsvmRz4_HCq5RqBAgW1EexJbU50v20nKWdgP4XiXd97Pja7qOSFpw_ES1gCVay0irzuXyWNhP4nIaLvWa3GJ-LjIVogWPZCIiG_UIoXrOBhlCFmW22qFPVkvxlCmW_MjXlPUg3mEEV0bFlGQdRNmKHJu-TQqme88BE9J9BUIFWrNvtBO1FcLhiPDY_RdIetQ-ZE9gpZ47LM1q4kwphu6YHfXl66etE5HCBtMdiWRKWGzhnmHiQeUQCYqxWwSNlRwQysalquKBuRFKonUjhE8syLh94WpAKob_aGIqmEU6w2JGWjgeRWsWG9loI9meqb-KLQLIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc885feb3.mp4?token=Tpo7eLYup46SSF-lSsvmRz4_HCq5RqBAgW1EexJbU50v20nKWdgP4XiXd97Pja7qOSFpw_ES1gCVay0irzuXyWNhP4nIaLvWa3GJ-LjIVogWPZCIiG_UIoXrOBhlCFmW22qFPVkvxlCmW_MjXlPUg3mEEV0bFlGQdRNmKHJu-TQqme88BE9J9BUIFWrNvtBO1FcLhiPDY_RdIetQ-ZE9gpZ47LM1q4kwphu6YHfXl66etE5HCBtMdiWRKWGzhnmHiQeUQCYqxWwSNlRwQysalquKBuRFKonUjhE8syLh94WpAKob_aGIqmEU6w2JGWjgeRWsWG9loI9meqb-KLQLIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5140" target="_blank">📅 08:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5139">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">برخلاف خبرهایی که یکسره از احتمال توافق می‌گویند، فاصله خواست‌های دو‌ طرف هنوز آنچنان زیاد است که بشود گفت :
توافق بعید است!</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5139" target="_blank">📅 01:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5138">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
اکسیوس : ترامپ روز شنبه در یک تماس کنفرانسی به رهبران کشورهای عرب و مسلمان گفت که اگر توافقی برای پایان دادن به جنگ با ایران حاصل شود، او می‌خواهد کشورهای آنها به «توافق‌های ابراهیم» بپیوندند و با اسرائیل توافق صلح امضا کنند.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5138" target="_blank">📅 00:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5137">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
اکسیوس : ترامپ روز شنبه در یک تماس کنفرانسی به رهبران کشورهای عرب و مسلمان گفت که اگر توافقی برای پایان دادن به جنگ با ایران حاصل شود، او می‌خواهد کشورهای آنها به «توافق‌های ابراهیم» بپیوندند و با اسرائیل توافق صلح امضا کنند.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5137" target="_blank">📅 22:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5136">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدماوند</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ve6S7MALC-GPekT8ZJivpA4Nn7_2eyUFLLNh-EYaviJjs-yUWNth1iceew3Kyj7UCWFqbKVp3mco_5PGrU7FTpVuVSOhOWYiUQxg5JtOTl_2HmJ3fJUHUGx2zQOnv41Tpm2c1DySxHgompWiLqQabnJ4jCPF90mbZd1bLzBRf2jjSBaPQEVGbcf4fD974S8q77I106fJJ7tkd5Epu1bmfyZ5iW22ztBVZJe_H9ClHKVdqnnGGc30hnD6ShmJQhoRG4sMjMz-2WWHg1mRAeu821UCXhxhBZQjOjbxQl8-T3QzoTSotghQ83eqixHKNMm_8QMrmgT4BpO1oU79nN-pUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗
یک اعدام دیگر
مجتبی کیان، بامداد امروز و همزمان با اذان صبح، به دست جمهوری جنایتکار اسلامی اعدام شد!
جرم او را ارائه مختصات صنایع تولیدی به شبکه‌های ماهواره‌ای اعلام کرده‌اند؛ انگار که اسرائیل که اتاق خواب رهبران رژیم را می‌داند به اطلاعات دیگران نیاز ندارد...
خبرگزاری سپاه نوشته است: «وی در پیام‌هایی به شبکه وابسته به دشمن، اطلاعات محل شرکت مرتبط با صنایع دفاعی را ارسال و با قید نام نخست‌وزیر رژیم صهیونیستی در پیام ارسالی به عوامل این شبکه تأکید می‌کند که موضوع را «به بی‌بی آمار بده»!
T.me/irdamavand</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5136" target="_blank">📅 15:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5135">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">️
🚨
🚨
آکسیوس: یک مقام آمریکایی گفت که پیش‌نویس یادداشت تفاهم شامل تعهدات ایران برای هرگز نرفتن به‌سوی ساخت سلاح هسته‌ای، و همچنین مذاکره درباره تعلیق برنامه غنی‌سازی اورانیوم و خارج کردن ذخایر اورانیوم با غنای بالا از کشور است.
☢️
به گفته دو منبع آگاه، ایران از طریق میانجی‌ها به‌صورت شفاهی به آمریکا درباره میزان امتیازاتی که حاضر است در زمینه تعلیق غنی‌سازی و واگذاری مواد هسته‌ای بدهد، تعهداتی ارائه کرده است.
- ببینیم چی میشه. بعید می‌دونم جمهوری اسلامی اورانیوم غنی سازی شدهاش رو تحویل بده،
خبر هم میگه ج‌ا به یک میانجی (پاکستان / قطر) شفاهی گفته!</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5135" target="_blank">📅 07:35 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5134">
<div class="tg-post-header">📌 پیام #19</div>
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
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5134" target="_blank">📅 00:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5133">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDx5_TjYgXZy6AmTLO6Xj0nLJ1eGNNjUYxsKXF_hB6foL_VFUH4hwEktFHEYVQuqkWyHC8Xj601e2uZ-0gV-ooG7_4BoiJnp0_EU9simICwknPiMU5hfKK7Uq2TVn5HVk2w8Hes_YK8i_Hjr8eHJSa6ORgwGmh0eHmHMDo0XgoGMJ8TYIZO5rIshPc4YJoBJwK1wpik6Uni48A9bFQG5ckmwnKpadLxsonzUrsexvS4k8JmYwkPE8U9jumZj_T0WIs5_6uxQe3kfwJRpbvXRf4SyLolA1iBQz6uZpnt5M5oX5I17jnrE7pnH3EpgK7lCMGRjAWAdEjUt9FMMh1uKZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با هوش مصنوعی طراحی کردم.
گاو : نماد فراوانی و ثروت سرزمین ایران و منطقه.
تن زنانه و نیمه عریان: نماد پاکی، نماد لطافت و ظرافت ، در نقطه تقابل با خشونت و توحش و درندگی
بقیه هم‌ که معرف حضورتونه، آشنای دیرینه.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5133" target="_blank">📅 22:09 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5132">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ترامپ به اکسیوس  گفت که درباره توافق با ایران یا بمباران، «کاملاً پنجاه‌پنجاه» است. ترامپ گفت امروز با مشاوران ارشدش دیدار خواهد کرد تا آخرین پیش‌نویس توافق را بررسی کنند و ممکن است تا فردا تصمیم نهایی را بگیرد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5132" target="_blank">📅 20:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5131">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
آکسیوس : ترامپ ساعت هشت شب امشب ،  در یک تماس کنفرانسی  با رهبران عرب شرکت خواهد کرد تا درباره پیش‌نویس توافق با ایران گفت‌وگو کند و نظر آن‌ها را بشنود.
🔺
نظر شخصی :  توافقی در کار نیست!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5131" target="_blank">📅 20:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5130">
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b5c3d0822.mp4?token=bG__2-0AqXeaD9sNsQOaV8WLW731CnpPST6Ju0RuykJBrw6TarHYxOx_cUSzH53YrPHQkuTHaOiqc5gt-nNPzTJZzWTLqagZOh_lv_f9yRfePpOuT_AWnRAT1O9MZTsSTtOuhQHccSvn9tlQZilTq36a-cPKh_VWia3dmm7hI8mg0q7puhglPe_U8CyuoJpiCSwioA5VmT4OXRYZ9LhKtJ3OQ7e1exmmJmSQLCJOp0mfsNnlGLz59GY1KT-725gs8L_8X5bpPNeFiyy9YLQhqPMeckYQ52f7jFg2s4b7uRbsIYKEvcYyPOIHpOxH4jSUvDYN_OzNlU6xtGUN99af3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b5c3d0822.mp4?token=bG__2-0AqXeaD9sNsQOaV8WLW731CnpPST6Ju0RuykJBrw6TarHYxOx_cUSzH53YrPHQkuTHaOiqc5gt-nNPzTJZzWTLqagZOh_lv_f9yRfePpOuT_AWnRAT1O9MZTsSTtOuhQHccSvn9tlQZilTq36a-cPKh_VWia3dmm7hI8mg0q7puhglPe_U8CyuoJpiCSwioA5VmT4OXRYZ9LhKtJ3OQ7e1exmmJmSQLCJOp0mfsNnlGLz59GY1KT-725gs8L_8X5bpPNeFiyy9YLQhqPMeckYQ52f7jFg2s4b7uRbsIYKEvcYyPOIHpOxH4jSUvDYN_OzNlU6xtGUN99af3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی بعد از صدها سال
مردم شمال مدیترانه و جنوب مدیترانه بهم رسیدند
الجزایر سال ۱۹۵۲  (۷۴ سال پیش
مناطق اروپایی نشین
و مناطق مسلمان نشین</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5127" target="_blank">📅 19:52 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5126">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RBCQ8CpM_Jgmpu9Qn_OtN3IjmnmFirqSjeYzRd7A8mDaR7-TgsJoie_S4vYRlMSly1o8tEImLui-QdoLyZ47PgC9cWdg50QcMPIFWcMUERSFjDqJN8alTmDG4KjHGVxQmAhGtz9vSbmHJANCv7Wa8VV866baZ7MQUbbX2_fC_XsQ7GHyBNiIdl4-mktunzbILUhYxiF1EcgMLyEDnc_bT9091BZH1MplVayndX-hH9A3hpMfA3ZXJ0v-xp1Uomjp5VKdZi8sceVc3yoe0iEejmQBjHf6b2mgo_OcshgTHB_DYqSy0n8Z63QXora-MWdCKaXO0_hvOSNbng2x0FM91w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5126" target="_blank">📅 18:48 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5125">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UcvGFZlTe7IxzTayamCG0VQl6Qx7Fu-hl3NstStCq3LPprrweFHvmYkc6HQfmS0QJcgQAvEsNF8stODqfDdqmzjCRr2_g2yLPDcg2MVSW2UNzlSvrsuOmW79lbO0FvlMs_fL-xrkWkLHaO7eFLO01wtz-Qz01UhceDqeUptBvPGEIgQWtoi_Z5WyTik28b3IBJ2cpve5Q8ZHJAJbcm-X1hWFAp_bwX-HTRGNe72uEAlsmg7mUAGufmS97iWZ2pKqjSsUw-jV_yBXi6pNd8zwmm3qCyjI4gKZvB19VmOqykPUCuG-yunLCiOUySiXfDz1Z2D6WfeZHK7gNnEXSZxulg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ که پرچم آمریکا را روی نقشه ایران به تصویر کشیده و تیتر زده «ایالات متحده خاورمیانه؟»</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5125" target="_blank">📅 18:16 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5124">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">مارکو روبیو در خصوص مذاکرات با جمهوری اسلامی:  شاید تا عصر امروز خبرهایی باشه، شاید هم نه. مطمئن نیستم ولی امیدوارم. پیشرفت‌هایی صورت گرفته. شاید عصر امروز، شاید فردا، شاید این یکی دو روزه، چیزی برای گفتن داشته باشیم.  جمهوری اسلامی باید دست از غنی‌سازی بردارند.…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5124" target="_blank">📅 17:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5123">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">مارکو روبیو در خصوص مذاکرات با جمهوری اسلامی:
شاید تا عصر امروز خبرهایی باشه، شاید هم نه. مطمئن نیستم ولی امیدوارم. پیشرفت‌هایی صورت گرفته.
شاید عصر امروز، شاید فردا، شاید این یکی دو روزه، چیزی برای گفتن داشته باشیم.
جمهوری اسلامی باید دست از غنی‌سازی بردارند. اورانیوم غنی‌سازی شده را تسلیم کنند، تنگه هرمز باید باز شود.  ترجیح رئیس جمهور ترامپ دیپلماسی و رسیدن به یک‌ توافق است.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5123" target="_blank">📅 17:25 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5122">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/izmFS29GWrgz1IqybqBAszq-ZYQxpny09F7aRL_6rCLdsRStRII7cwtg1mPQHcZqmImkh6x49IqLjOBNnOicFqQIC1j2rqzr4N0lyhcLj1kjwMRB7aH_bTmu-YY7ysx4Pb1FTyEIB2UVerlJURitVORNCBTC_cfh2EK6eatWTIIbKQ0igD82nTKpSG9wGyT3ruL1bjo3UNwhJMzzxSYrhXHBsjfzguP-7aswYK7XCZjoXqddcH3fYDLxNwkoOGl-ZUht8OIQeKVKQq8Vkuy3HCGz6EDH1rMAYk4bCAc4_rcIRn4Z3xnkrM6iuzt_OTvm-b5IrM-lkWig5z6DLnIZDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چقدر ایران باید هزینه بده برای این گر‌وه‌ها
و برای این جنگ‌های بی‌پایان جمهوری اسلامی با آمریکا و اسرائیل.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5122" target="_blank">📅 17:18 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5121">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">به خاطر ارسال ویدئو ۲۷ سال زندان!    مجازات پدر «رومینا اشرفی» ۱۴ ساله، که با داس سر دخترش رو برید: ۹ سال زندان   حکومت اسلامی! عدالت علوی!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5121" target="_blank">📅 13:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5120">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RSVItgPpIB0c_t8brjYKunJK9BGSDE9S4P8I7wlxUqwMAAtz92E5GAnRjqsOqMtOzSIjEdw1OOTo79ZxShbpLCLfM9uZYIgS8uSg3vgFgx1dwMTp1BhI4SB6Bo7-s724JuLbahxIvknbwPtbBMm6OaWVJJUqwEEjIwhbK3UqVWoitBVTT0_rjrswc6krzAdi60iuY490VI-Z12VPhJ3Qta66zwcajq3CZzIvSpkE7QJhF6kwj_Olpq8tPOtk7R5L7fXVKfJheYjY5C8IrA0O3dBUGG6b-S99-YTPFhwAHGgwneS_TKzq4eeKZ0iB9ifooCXwMemE45mBsMFxFbhnxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به خاطر ارسال ویدئو ۲۷ سال زندان!
مجازات پدر «رومینا اشرفی» ۱۴ ساله، که با داس سر دخترش رو برید:
۹ سال زندان
حکومت اسلامی! عدالت علوی!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5120" target="_blank">📅 13:20 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5119">
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5119" target="_blank">📅 08:14 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5118">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">حریم هوایی ایران در مناطق غربی بسته شد.
پروازها فقط در طول روز</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5118" target="_blank">📅 01:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5117">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
براساس گزارش آکسیوس، ترامپ به‌طور جدی در حال بررسی آغاز حملات جدید علیه جمهوری اسلامی است؛ مگر اینکه در آخرین لحظات، گشایشی در مذاکرات حاصل شود.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5117" target="_blank">📅 00:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5116">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">وال‌استریت ژورنال:
واسطه‌ها در تلاش هستند تا یک توافق موقت بین ایران و ایالات متحده به دست آورند.
پاکستان، قطر و دیگر بازیگران منطقه‌ای در تلاش برای کاهش اختلافات بر سر برنامه هسته‌ای ایران، رفع تحریم‌ها و امنیت منطقه‌ای هستند.
هدف، یک توافق کامل نیست، بلکه یک چارچوب موقت است که آتش‌بس را تمدید کرده و امکان ادامه مذاکرات گسترده‌تر را فراهم کند.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5116" target="_blank">📅 23:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5115">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o5wbSjKo3CHbYkD6Jyx2KwoCNmEP-nMiwsxjkoJllRLicPZ4aB5ePEPkpc82jRKDNhkLG3FnGcr7spHrnQeSaeyMTKY7xJGLvY1ziwATWUdkn6Mn6DQ65TTyKBcvbHnW1nrzW2-tLgc6cHVYF0MqbFIyWr65HydQpYZyMaHgwl7H7i9_AUv3oZBKZsjG9rtcqlchKxNAkcbyRaZqYhHn7jmjI6up-oA7cS4h8x0c-86VqfdYOOBO0s6hXwV7nw_G6I_MnlBTkQxukauQXJ3x_LH3VobVOLZzcOx4GGfOiT-HxarTCQSkbu_cj-KLIZXtt5dn6f-s15D-YlELr35oIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری وابسته به سپاه این مدلی تیتر میزنه
ولی در واقع «گابارد» از مخالفان معروف جنگ علیه جمهوری اسلامی بود که الان کنار گذاشته شد.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5115" target="_blank">📅 22:55 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5114">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OApVkXp_CtCunoDK3cijfEZcrY1_2HyWQuM5F7oRSvbdL1FqvM9etq1Me5m9IZEOLJ6tYIyZg5mO1FJmJNF_pTgmFov-KN6tRxpViulKzR_Cx2sxZz21ABDpkUHMTlwm9-Gd03WZDiYTBGU0yNDNfpmDrgh-rtcFaieyqO2v28yc5h7Punq3DAPRh7NUAWP_BDToCJHg-B-whBGyr4iFtLUiTq81LuQqx5fL03phK4E7yy1WDf4q-LV0ZHxMIqW47zf_Kr_1jiNVz7WuXnoBNJKSMDuxNlojZiU5a3Rr91vROWqs9z0NG75fndIoZtOzk3r-4vFjjcIYzAvE56C9-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به بیانی دیگه : توقف جنگ در لبنان، پیش شرط اساسی جمهوری اسلامی برای مذاکره با آمریکاست!
خب چرا جنگ در لبنان شروع شد؟
چون گروه تروریستی حزب‌الله حمله کرد به اسرائیل.
مهم‌ترین دغدغه‌های جمهوری اسلامی نظام خودشه و حفظ نیابتی‌هاش. نه ایران و منافع ایران.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5114" target="_blank">📅 22:18 · 01 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
