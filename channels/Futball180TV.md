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
<img src="https://cdn5.telesco.pe/file/PWwb8sLpbgY0ZCNmZQLYm9Zam3CDDTGTgSh341yY00As8IFeXc6Yz9kjw5PFeDoH0cPDDlDtyh0ATYIOUffxHGM8t1B_6FtOKz1dyC7PT8JRLj6euAFG1xQVFpkM30LbnEdVI7VljHokLPFTyhQWMsZzL4z--roudc2rmR1jTVvzaJKc6HjbX_d3ePqCWvp36MaaCOmpBlk4qXzWXZhurtzXp_nfiP9xXfgSIF38tHfxV_jESyY-3PuSEPayEwAcTupwZBiw6z4rPuaH0qkwe9cM8SkxwXr2khVWdUNDBc0vnvP0shln7v-omG2DzjFs89dUres9r3_EiCpxqx7CMA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 537K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-02 01:27:42</div>
<hr>

<div class="tg-post" id="msg-101713">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5f7d69dd9.mp4?token=a6IbRGRSPETUkUrl6dhgUL_lsegTqjebtbNSf77RJhBYO4a2GrJ93-m8O2mmmQOMvO584AY6sBi1PX_5_wRFs5FmCXLEORMjTiWExllkrDUESjQc3YhJWUKgF9K_LzSqjJNSqyIkLItZMjV13BO9WcUnbglWAmtZqVLuf65fs_QNUeNe1r2-QpRX7QTQ2HoY7K7HvPKWh01nQPpO_Zoqs6qqjLNiz4Wfh7P13CT-aSFUe_8mdS8sUa5e3wp5y6imiML-f2kp_QrvmSD5-A3WgfPdafgEc8BF2IQKRSkZaBOpF4XdzvDG5_3UMoBAZtNT0jHtd7COrWq_U86IFaEI3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5f7d69dd9.mp4?token=a6IbRGRSPETUkUrl6dhgUL_lsegTqjebtbNSf77RJhBYO4a2GrJ93-m8O2mmmQOMvO584AY6sBi1PX_5_wRFs5FmCXLEORMjTiWExllkrDUESjQc3YhJWUKgF9K_LzSqjJNSqyIkLItZMjV13BO9WcUnbglWAmtZqVLuf65fs_QNUeNe1r2-QpRX7QTQ2HoY7K7HvPKWh01nQPpO_Zoqs6qqjLNiz4Wfh7P13CT-aSFUe_8mdS8sUa5e3wp5y6imiML-f2kp_QrvmSD5-A3WgfPdafgEc8BF2IQKRSkZaBOpF4XdzvDG5_3UMoBAZtNT0jHtd7COrWq_U86IFaEI3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
نیمار دوباره در برزیل جنجال به پا کرد! باشگاه سانتوس اعلام کرد نیمار به‌جای سفر با تیم برای دیدار کوپاسودامریکانا، در برزیل ماند تا روی آمادگی بدنی‌اش کار کند. اما ساعاتی بعد، او در یک تورنمنت پوکر با مبلغ بالا در سائوپائولو دیده شد! این اتفاق باعث شد خیلی…</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/Futball180TV/101713" target="_blank">📅 00:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101712">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24deb1c503.mp4?token=PLP23K8vul_xJrobCBcq_QPbEfv3NVWYkBy-rbXIa-Mz87xdBX9Xe4fA76ltHn3aEj0U418_Brn7Kxtwn0UGSSplxNgxfdYglkNYyHF9a4UxydkNY4idR1ItAqx_a2JZxjeADBE8CPpUIjUPdBF5VlxJCpRRbQE_v7XYYYcXTYHrVA522cFz782VuXg3ucL9bc1prjpFDPzHA4p4jjDkgpCTUPt5qblPJpO2KfjWMJo75eYjFoT39o37ih1_vuKcr25MH8w83sXhAdLhtpZxxOIb1H64yCiYdUcoirVk2Zq0AcFxoWy32GkTxmKPVC2w3V2Sz9WLu_LCsbeZ_Y0yfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24deb1c503.mp4?token=PLP23K8vul_xJrobCBcq_QPbEfv3NVWYkBy-rbXIa-Mz87xdBX9Xe4fA76ltHn3aEj0U418_Brn7Kxtwn0UGSSplxNgxfdYglkNYyHF9a4UxydkNY4idR1ItAqx_a2JZxjeADBE8CPpUIjUPdBF5VlxJCpRRbQE_v7XYYYcXTYHrVA522cFz782VuXg3ucL9bc1prjpFDPzHA4p4jjDkgpCTUPt5qblPJpO2KfjWMJo75eYjFoT39o37ih1_vuKcr25MH8w83sXhAdLhtpZxxOIb1H64yCiYdUcoirVk2Zq0AcFxoWy32GkTxmKPVC2w3V2Sz9WLu_LCsbeZ_Y0yfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇸
‼️
🇪🇸
یه فرد فلسطینی رفته وسط اسپانیایی هایی که قهرمانی تیم ملی کشورشون در جام جهانی رو جشن گرفتن، پرچم فلسطین رو بلند کرده و اسپانیایی ها هم پرچم رو میارن پایین و پاره میکنن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/Futball180TV/101712" target="_blank">📅 00:19 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101711">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YT3mZwSd9rJx2xLMIyoDO1mSsfj6I-RA_SLs2sTSnmw9CluDYSvqOIoIWo9itGA_l6MLCsnGMSITWqxN4cMHqOQO783UL0UxplirWLs7YHNLHfe6CNhUDBHO1UGfJI-OZ51cs_popUhAtUfkn_Ldqw-wSWSxgz4jfriwO3FophdyuKPUy5T5g_lnzZKTdd1UoT28DXEuzCSf0grHbhw6G-7qd2lB3SiEiE1Qs8hOTU04o5OMg7XgnknxZueeUZMog827KjXQ8j5huroCtQJSLkdQ_cVw88x3E6nKwRMyL8d_IOTzyq6UF4EaFp0R36177ky3dCkXyVJR3kGCYW6ujQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
رامون آلوارز:
لیورپول قصد دارد وینیسیوس جونیور را در تابستان آینده پس از پایان قراردادش با رئال مادرید به عنوان بازیکن آزاد جذب کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/101711" target="_blank">📅 00:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101710">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EY0GAX1GE585Ga_-sXNCMRUWO5YoP7Jpg1dV3RDru3BgUUFPfq7XaW9U_F_ZMfyDRFeLhhecO7WR3y-a5J2cKSzxzw0WhBrm7kfJRAQQP48bAsS5pJzaQTFErKkfVehm6PBsjFDB_yo3zA37cMUIAj3uBozPYm0B_JpxAu3NmETm5QKpQP-ZNCOTtZBEe-pSJDXegRBdHqkp7DG_RFgx_tDQUjsQqNVOal7eNN3y34lEUOgdmEQXeOjgJyv4KOY-0qv_hef9qv3eO_JCi9FYZd2HqbC5KVtYz0OlaHpw_-UZlpDlcNwyQ8OUSt3UgxKjNgexexDB6yTqPyIUBRo15g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
ارزشمندترین بازیکنای دنیا تو ترانسفرمارکت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/101710" target="_blank">📅 23:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101709">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5766dd6b60.mp4?token=dPDccm-ZEelcqwtFTv8wVMOAYHiiEvtAcSd29V_IshGTpveBwMf1KHwmFoCiW5m8ud9X9mQg6JtRFM4ZIQ7IzedW_OLd86p13DSj2hm-kOAbrhBvjTaZ0P9843czpIax8XH-jMWj7EmDfTgcJM2MjsKNwqfr9DSg265qRmkXTPtEN2dMRX1J764sFl9xohYjfzbsFt4aaV-h2FjvBfirNb39JQcO03tdsK0L84d1CzCXWrKpdMTX9dX6lasg9A7FkeyXeD1COEZaVuWWDyNht5DGdQwWGTUq9fFxMmlwZ-ETFfxi3xrolUIUREU-4qIv2IWTz8T2XSADJ_57uZW17Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5766dd6b60.mp4?token=dPDccm-ZEelcqwtFTv8wVMOAYHiiEvtAcSd29V_IshGTpveBwMf1KHwmFoCiW5m8ud9X9mQg6JtRFM4ZIQ7IzedW_OLd86p13DSj2hm-kOAbrhBvjTaZ0P9843czpIax8XH-jMWj7EmDfTgcJM2MjsKNwqfr9DSg265qRmkXTPtEN2dMRX1J764sFl9xohYjfzbsFt4aaV-h2FjvBfirNb39JQcO03tdsK0L84d1CzCXWrKpdMTX9dX6lasg9A7FkeyXeD1COEZaVuWWDyNht5DGdQwWGTUq9fFxMmlwZ-ETFfxi3xrolUIUREU-4qIv2IWTz8T2XSADJ_57uZW17Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔺
▶️
در سال ۲۰۱۶، مرتضی احمدی، پسربچه افغان که توان خرید پیراهن مسی را نداشت، با یک کیسه پلاستیکی پیراهنی شبیه لباس ستاره آرژانتینی ساخت. تصویر او در شبکه‌های اجتماعی جهانی شد و به گوش لیونل مسی رسید. مسی تحت تأثیر داستانش، مرتضی را به قطر دعوت کرد و در آنجا با او دیدار کرد؛ لحظه‌ای که رؤیای یک کودک عاشق فوتبال را به واقعیت تبدیل کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/101709" target="_blank">📅 23:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101708">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b758c8add.mp4?token=Qx51gEOKzRgMTBkIPG5aIp7uZ8ZY9ANmDvJPzD3CMRJzC-BGxFyLShlsWJkwmJF6dxFYY1kRk44HRTmP11xb_VaOCtoWs4929V9LSRgWN_R-VeliaPCRiEY-6DS3jjOk5YhJvkV239y_vVGq27G5RbtRe0dgK3ma5Mu9U9OhQ_pJmQz76VQ2Geh9gxggCXbV4Mq5Vrti-Q-Zd0TOKIklwhHW0LPnVpwaMYXhoici0oRKzjXpZC3_I0WCN3R8SW6CD5iPW7-pcvEao_S_uHQvmvUnGqM_38ViuwV-jJB231gnVZInsGnRNlrxpq38Gu_ePLqIfybtC8a3GlQ2wRsiTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b758c8add.mp4?token=Qx51gEOKzRgMTBkIPG5aIp7uZ8ZY9ANmDvJPzD3CMRJzC-BGxFyLShlsWJkwmJF6dxFYY1kRk44HRTmP11xb_VaOCtoWs4929V9LSRgWN_R-VeliaPCRiEY-6DS3jjOk5YhJvkV239y_vVGq27G5RbtRe0dgK3ma5Mu9U9OhQ_pJmQz76VQ2Geh9gxggCXbV4Mq5Vrti-Q-Zd0TOKIklwhHW0LPnVpwaMYXhoici0oRKzjXpZC3_I0WCN3R8SW6CD5iPW7-pcvEao_S_uHQvmvUnGqM_38ViuwV-jJB231gnVZInsGnRNlrxpq38Gu_ePLqIfybtC8a3GlQ2wRsiTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لطفا هوش مصنوعی رو متوقف کنید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/101708" target="_blank">📅 23:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101707">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/utPP0cOMj-24S5810Uw6MuOAAQ2vtldgmNJXjzHWCN6lczYSzLRBuD9QbGW0PpqFY2Ej8u9aHG7XHOkemSmyRpDmWqBitX-9ECIUcH3fEjbVFb7Iyu_gH7Zd8OIwDiidIW-ctCGGXwU_LcwaiHMcRkDjmCOzawxyJyqg7ntRQyfoRc3jm475h9bSvOZRKp1UC-fqBLOlh-YQDTXW8FRalEmNTJ9vcgpN5yxit6UbGGRI5u5LWbc3ztjG0KWO_BGnrstKYgsrenE_7_4k7sExKJLDTT-jzMxurrydx7EUITSKQ2WnKvNPqk_U-42ufBq-3cBMHMmfhqnRqGsYrj2uEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ال‌کلاسیکو فقط یک روز قبل از مراسم توپ طلا برگزار می‌شه :
🔵
⚪️
۳ آبان ۱۴۰۵ : بارسلونا × رئال مادرید
📝
۴ آبان ۱۴۰۵ : مراسم توپ طلا ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/101707" target="_blank">📅 22:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101706">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I2tRimWTdH1YUTWmFjyw7_wbB-IwpviqrpLd5WRF5WpubB1Hsi0tE_pHV5rasLZ2GF1tcI8GZ8BhicPV99AK0W1euXzbmyFzrpHGkR4QFfvjzZ-WKeqwfSZpr8jrSXPReCyQgFakzxZNl1lf47-8smxzUXELEFeXXBe5du2_miJDu7SzlAA5xUDECfpuYSrlouSRQXFeR7SZtF1CevcDx7SWGrLLXcmzXAnZ2F-kKNJNRlxXB_5t5PTGPAw0nYwpoXj3er7fAUSJ9-qJXn3bugfSLbLOQSfKn35PpFzTTNjKk2UBFINWkLKSvLsxkkPbz8DV7HS2Jbi6WfkYuCROkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنخل دی‌ماریا درباره اینکه چرا همه بازیکنان کارلو آنچلوتی رو دوست دارن:
از نظر تاکتیکی دقیقا میدونست باید چه کاری انجام بده، اما چیزی که واقعا اون رو خاص می‌کرد، توانایی بالاش در مدیریت آدم‌ها بود. همه رو کنار هم نگه می‌داشت. هیچ‌کس از نیمکت‌نشینی ناراضی نبود، چون با همه عادلانه رفتار میکرد.
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/101706" target="_blank">📅 22:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101705">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eH3V7p8ls12R3L2gGM5S0cZiZGeEzPRe7gqBAZ87jZ0G5ehAHKvn_wx_KDh47Qr7zT43YFmgdwvCOPA7Xi5S9RBZtn-prm7Ks8NTyqLIEK2cG3PxRDOC3b5eo-JF7DIiOEOHN-jBXOENwbn32F5oGTx_NkZHg1d7p4Nk6OCyQ-CRQ7R1VYIik4GHGLcm4S1TNsDxmOv01V-8eTAB0-JzSXOXXCr_lKayBY0lFmXprsr_2eCRUmmKzJqCYSSqkEp1yhLUNt8hA46PkICaVn4nw4NKdRr61rvqWP1JxIt98dikVIe0KnkTKIKuGupkZ8my-IeaMkwMcFW_02nBovpEnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
به پرتغال هشدار داده شده بعد از خداحافظی رونالدو ممکنه بخش زیادی از توجه و درآمدش رو از دست بده. کارشناسان میگن فدراسیون باید از الان برای دوران بدون کریستیانو آماده بشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/101705" target="_blank">📅 22:18 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101704">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
🚨
🔵
پنجره نقل و انتقالاتی استقلال باز میشود؟
🔵
💣
همانطور که ۱۱ روز پیش اعلام کردیم، باز هم دقایقی پیش که از محسن ابراهیمی هم ( ایجنت و معرف وکیل ایتالیایی همه کاره پنجره استقلال) پرسیدیم ایشان اعلام کردند پنجره استقلال به قطع باز می‌شود.
✈️
🏆
@abitajsport</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/101704" target="_blank">📅 22:18 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101703">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0GRtTNIFyTx33WdclxNlph7cDXA42OoER4khwL2ZUMsi7myizFdnsEca8AprTbmYF-JgxAktYxKYgL743KzPRQO1NkiEAlvsnCOgDOQPCnpqbQ44IVtPxeUFJISPOtG3eWkEORFFtruy79Q0GJoVhXAV_CVubifJfphfFl863RKxf-H1XegUPKwcRiiY5QiMG-FWU8MsYWjxMqktH-aFk9b53hbpvOxysB-q6MCttU4gQFsf8xxFLEQei-CFdugt4KdqOZQcdjJG6FHL5mrpvqp7smrIbWwMOOSAO30Y5Qcdoz68ImqvIUGjTjd0wHGMpDuxebNO8CkoQagOONz3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کیلیان امباپه هنوز شانس بردن توپ طلای ۲۰۲۶ رو داره.
نشریه اکیپ یادآوری کرده که چند بازیکن قبلا بدون کسب هیچ جام تیمی هم توپ طلا رو بردن.
✅
کریستیانو رونالدو در سال ۲۰۱۳ بدون بردن جامی با تیمش، توپ طلا رو گرفت.
🇵🇹
✅
لوئیس فیگو در سال ۲۰۰۰ هم در سالی که جام ملت‌های اروپا برگزار شد و فصل رو بدون جام تموم کرد، برنده توپ طلا شد.
🇵🇹
✅
گرد مولر در سال ۱۹۷۰ بعد از زدن ۱۰ گل در جام جهانی (مثل امباپه)، با اینکه به فینال نرسید و فصل بدون جامی داشت، توپ طلا رو برد.
🇩🇪
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/101703" target="_blank">📅 22:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101702">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwwQiERcKpOA8yxBfXximaddC0TZh4Tqo9ca-Nx04bv5DDqtdcvAMoReNugauWVT76PKkkSzrozCSHLGDJIHTTh9H3K3r87MWlgoI27zhJzfWdKETGPIdxuCAgAY8_K0-040DO9WZqbNnbEWMhQtS6KNhLzsVn_aFZumNk8Obu-ZgJsYdHKb2ZMUyk-WauqBxhL59FocFDw9Yx5R6QzMHPsZ8voPFem62qvm5sfWZKC7fbDOGlXo0SUW-4kDncmnSuLsa-kSZLVeve0KDYj2zyk2KqemOhBJIpeh0P2pqhNcrVP_8cr0EiD2eg1VUyFD6nZ_mHu3l3rrjcFtVwtxGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
ترکیب منتخب جام‌جهانی از نگاه فیفا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/101702" target="_blank">📅 21:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101701">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ntcWXnJpKYRpwT4MkIr3gx40Nc0PFpZ6XPdvWQINqihnu3C2C5LT1BudJXvZb-l39Zwt0mdKcPaMN9Lyv5pE3YDTgPids2JKlJbN421LXMqXdUTHTnAAysZkaxUETAo8uX0bcC7eN44KveduoQsTFfS-mowwnm02RpOdfgCi5KQdRrhOvr4yBgjAv6H_c3iAqAeuvO4dsBqUg_ay59W7LrG0fz2yJ_btnCiIP-Gn7syBOzsA8oOSt_vO8dZqjdDlIsnMyCD-9ssSYWkd0DzkeUbz-9OuyBKNf2M90AhchSvdAdgjpx0j7rQb1BIaOHnUKT1bxEu8PuMTgwdRhyaQjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنخل دی‌ماریا:
رئال مادرید شبیه یک تیم ملی بود؛ چون در هر پست، یکی از بهترین بازیکنان دنیا حضور داشت. هم‌تیمی بودن با کریستیانو رونالدو، بیل، بنزما، مودریچ، کاکا، کاسیاس، سرخیو راموس و په‌په واقعاً چیزی خاص و فراموش‌نشدنی بود. هیچ‌وقت کامل متوجه نشدم که برای بزرگ‌ترین باشگاه دنیا بازی میکنم، چون فقط داشتم از فوتبال لذت میبردم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/101701" target="_blank">📅 21:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101700">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PMKT1E0a0Y3Duj847s1aPi3yVZtsPKFyjw_yVL1aaX4MnqA9q5zXt74SZzOTc3WuUl2b-B43gWKsyl__wt6KTd7sQjg9IkLcQgaLVU99X7dUQF0SfNk_HSI84DEhd06LH3kD4Huz8sgHBwkRcTQRnrSCeYKZ6hfM_ZSVJfEQGT_deh-GRAc2h3EOwJA4-SC4Rw5PvPvdGBt4kSh2Hx4mv43u4VQ9SQiore4fovRHkZxbh5CSOzNlir3CZBKhUIdKSms7UxfgSYSsiYeFYFxV0HVAjLD2zTUKbXTNIkhHrV06I26pTwGeLVXENLHWLNLRZYrLW5mfCdAB5IHXmJBHVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
بن جیکوبز:
🔺
چلسی به احتمال زیاد قرارداد با ماکسین لاکرو مدافع تیم کریستال پالاس را با مبلغی در حدود 52 میلیون دلار نهایی خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/101700" target="_blank">📅 21:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101699">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHg0s6K5RNVaXy1dubBKUBWZ9ZAxPR1itUcDAiIDU-3ssCVsXz3OkFN_7WrpR-X0J-N4Fcp-hsnLbXmqKnPBYk9KBKLlO5uIuF8H2hem7RuttT-S4a9J59uEasvvLG1ZxUAdo1UYDXVjvxatEewOVLuQ5fCKuVzFLtiLZdBnbDm4_P_uemgNN1zi3p2ndqMmygVRk6X3TO0StiaVDAXiO4ntLB2VlviUr6nN3N_ThMlmorJ-2IIp_fXG7-NRPQic-pMpohX4wauN5i_qG99i-rnMeYL2ufzebXiuLNeLiIFa26V4qj4qeu9V_9fWGRx1hBKC5CbgiSbKQ_4pAKFRXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇳🇴
فدراسیون فوتبال نروژ قصد دارد بعد از دخالت دونالد ترامپ در ماجرای فولارین بالوگون، یک شکایت رسمی به فیفا ارائه کند. این فدراسیون نمی‌خواهد این دخالت بدون عواقب باقی بماند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/101699" target="_blank">📅 21:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101698">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YOKXcMKfvwLwTBMUtBUeFDXeDE4mv2gpJdqxr8-LfjsHJyKez9Czexmjcz56kUrVj0h9eloQYIkwruMUFVqtKd7Yc54yKYK63JC6qax0H6xiZKolErnlK2kDWE5q5EIxzJ3LNEXD-RBPqQep_D35Rsow2YRQZOpV2xGITl7jNmtxAKSS9zH5S68LjBWyoipLryKqxW0vL0hW6p_wqmBXyyX5Dt9VnYWCRHXerZ27HSVV1Q0cI518fyMdFkv4bUO1vOfR-cVaTcIhAP2MpZ_9A2qnHj-iadLisp9CkiDhUTA8UOLhIMEX7EbPcUh3fOSnglMup97pqgPD6MTv2xsX0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
آنجلوتی پیشنهاد فدراسیون فوتبال ایتالیا برای هدایت کشورش را رد کرده و گفته که میخواد در برزیل بمونه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/101698" target="_blank">📅 20:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101697">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/biZxtOpwShWOl0bjJESsqthGHCBBXp0FIYfX1wR7h-a4-rQo7_28eTTLKli0iovODyU0gSNlUCU7d5LCEN-PjyDfLkyUcLiHgEAH5KCI5Ekbnegq8Byfz8S5odYQOU_ZiX9gi7PJ6XJhHJcb6JynMtsuCTZNQ_Bm1IMjvNMHVqsh2Jwze8DmiLCA3tAGu-vlkSYIgq4sG27VhtQuhFj_n3GaZMjdb081SIqhhqrvjUYxhg934xm8xtrKNL07oJem2dsmp2tPseUbUXQRl8dAgC354QxV8IOb_T3jyU3LMrdY5P6EqczemUAPbGXIkruoaNj_6CmkisJ2UA290CYyqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🇪🇸
لوئیس دلافوئنته بعد از قهرمانی اسپانیا در جام جهانی:
بعد از بازی، بازیکن‌هام به من گفتن: ما همه‌چی رو بردیم، در تمام رده‌ها. حالا دیگه چی مونده که ببریم؟
🚨
🔻
یادآوری:
این نسل از اسپانیا قهرمانی در یورو زیر ۱۷ سال، یورو زیر ۱۹ سال، جام ملت‌های اروپا، لیگ ملت‌ها و جام جهانی رو به دست آورده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/101697" target="_blank">📅 20:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101696">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r3wd4s4nAsjhVFAS2JS3kQmHmFE_Rfgg-_egwbPKvr2Yvi1wPJTFdfAcVNanMGfPvDbcOUEd9Pv7yWW75cHuZ5-bu6qrvpnMbg7WUWbvv-v4caX8nJBTqiiGiAHEQV0rUk9awcjlSCMMaYPZVoTZ4xFTC6UtVoozOSGdnc9izFxlIEh91eG-mBuilCRTPHCNbj9qMnZKI4WJ8s1w7dKERX5X7FoNpQhxxgKHrEC52fg3h14nBZLwuiBhpJchzdAG8YBZl1a7ocCxno1g8VExFffLyfl4WIbB1a_mfln2A0Bc4EoYav-K6QaPXy-XGiCt0U9TfldhTY8z6NpzDrYB2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیمار در کنار بتموبیل و هلیکوپتر و جتش :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/101696" target="_blank">📅 20:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101695">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJ9-tqjLnzraQWX6OTQM5d4b6uF0QiUyS22OitZ9sxK9M-LspbgN7X-hL7RIucv4xVzCs0N9HnjbzacC-jCj31mUSGIQ3HBXGCEFVxkgtRPjegttoL0Te7o3n96lIWgF9XEGwh25cXhA1LM6r_rXcZdHv31uww9Lmq2EiBmQBmJdCF3YX-wm4SpZ9q3saMXnLIIpKvkH7LYg9gTiBvbZZcpkhvKqSBzfCOgmPwUCkv1Isji213P_2JNmgG3j4LNTZwP9no7VGdNUcPKgsvKTh-k3utDIVEbNsHow5yu6AuQHL88PHkh7h-F5mw9gQgo_QV6PQhRZzyzjbrgXGO1c9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
❌
#رسمیییییی؛ باشگاه بارسلونا اعلام کرد که رباط جانبی داخلی زانو راست فرنکی‌ دی‌یونگ دچار پارگی شده و ماه‌ها شرایط بازی برای کاتالان‌ها رو نداره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/101695" target="_blank">📅 20:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101694">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KM1UU5RzVARCgNQZDDirfmvhh-_DDfDnVPw7jIxvV9xmckFZ4NuVCUac_gkJT1qmShlADm7lAy3QF5tGmub9Ouw2Dcf9UUA_LF8YjBMQTySzv-SR1-U6l3gMB1ppVAJXJbS5inewWpMQ65ZwHEoEzTHIYdTZutH4iwvxiBHFUl2Zc2Xg_nf032ZvO9BnAEES4Wc74gWWH4Dhnje8fFTeoyCyi2-uTNu0eVkW6pcU8dvByajP_AaMjWoL9Sc8_2whjqi1L2-o7cfVkgdjAAwgk8v6p8OtED_NUulrl4DLHu_i9KaAYf9MgWrSJAaBbYoa2GdfQrCQBI8FOCAXbZASUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔴
سامی مقبل خبرنگار معتبر BBC:
🔻
باشگاه آرسنال قصد داره پیشنهادی به ارزش 70 میلیون پوند برای جذب برونو گیمارش به نیوکاسل ارائه بده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/101694" target="_blank">📅 20:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101693">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d00c416b26.mp4?token=GhoGP0-Pz0VecKxZLQAWG8JZ9ynWtp0LOJamnOsHX1pgqfWLUlR0ZI-htl7t-DzusaU34bjSvdaPubKi4L3XF6BDQmAUnNRrPiBDpAPd3yS2ctueSZPYnIGV06lZElXdcDyw8SHWV8LOOeZmTxbHgKAP3A4EUKb0GxogT8XFA0ds9oUzpUqdEAbhHub6WsyzigJJXFjwhmNp7gfrOQJbk-__Fz8EIZ3PYoMDUQfynhVcTmJlKqthb6cRX4F7cyndXaYEEhvzyUmYfgv6iW0mEjy5N73vHwzUKX3as8JCikLgXP-PbHBnrZomVyx_zmln3wyzH7lNESrmMGFzdyGFGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d00c416b26.mp4?token=GhoGP0-Pz0VecKxZLQAWG8JZ9ynWtp0LOJamnOsHX1pgqfWLUlR0ZI-htl7t-DzusaU34bjSvdaPubKi4L3XF6BDQmAUnNRrPiBDpAPd3yS2ctueSZPYnIGV06lZElXdcDyw8SHWV8LOOeZmTxbHgKAP3A4EUKb0GxogT8XFA0ds9oUzpUqdEAbhHub6WsyzigJJXFjwhmNp7gfrOQJbk-__Fz8EIZ3PYoMDUQfynhVcTmJlKqthb6cRX4F7cyndXaYEEhvzyUmYfgv6iW0mEjy5N73vHwzUKX3as8JCikLgXP-PbHBnrZomVyx_zmln3wyzH7lNESrmMGFzdyGFGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از اون دکتراهایی که دکتر علیرضا بیرانوند گرفته
😀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/101693" target="_blank">📅 20:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101692">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R2JS1pvlAfTi4FSYEZRcJhL6bkQyT_bt8cxBNXcMc7UU6D35jDRSjFVhr1yEK3oKNBnqBXgb0VC4cFTb3KqRD7LRloqKJYwNZVdsNZb5twcTRIO0rw3SAfb1W2Dq1h4-owQohs7JuLxcvBjp7ai5RfKsVzQ38DEHKSavgLgT52D04Ih16Irn9vGpxbNikKs_0KowWDgFiFL8OtZpTGA5eZfF_VGad4pbTUDNRjwwGArV8ZFZ5nMWKg6F40ECPqbCzZlnkwuPNQdWgzAjeDnejs3WwjL4nNk402CKpIokOO6a5mJFdi76epeBFhXBLH3Tv_lwGxvHtaW695LInJMQYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیتی که همه رئالیا رو برد به سال 2013 و اون کیت معروف..
⚪️
😃
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/101692" target="_blank">📅 20:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101691">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H8AZBzTilQ7Wdn0bDKRhw4DK-0324OqXQOTyco-ZHk8joypmaffrqEZQkGnzusgmYNVDFHW1NshyIbZcZyGZamhSNFGLSUW9XQd4xVrxepf2jgaRIS8FnCC6uIWmyHPhcHCgUb4p1z_GywDQdihoSSWkSdYRoXdGk0UVGt43b_QK2ayy9TJVhgmBIymdZzcLZNNpKABCw0nEEMOsw56kLee-5I22lNeeRbQCdgNV1Z9M1pXQ8GjedbeuI6exFPOgGL8yAp-2gKEo6d1aoQeV3lJwn62EsmdYe0UbbFprBcGY_jMaTDGwnw7a_Tjk-M2ORJ-Xz_m_tQGIgQm8-oep_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کاسمیرو درباره پیوستن به اینتر میامی:
بی‌صبرانه منتظرم به لئو مسی کمک کنم؛ بازیکنی که یکی از بزرگ‌ترین بازیکنان تاریخ فوتبال است.
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/101691" target="_blank">📅 20:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101690">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4rsWQMdTDPh2crJjgBkrvaUbM0jtmga0wWmXyFOrsVPaJikeEY9UJD6I4iUL0VRAC9gzQ7wXdCA5-EyDRCY9iSd-zbYOpG_UwZP1MNBOSBFPsFYx2hEIPXxbwoBdCsIFdeP57RNb__mCtCJ9keu4WpC99WG1WKyqUakHQnZj5wJKCd2qW-mrkcNiRL4iJFkcZ-cSNAFPyVPApXf7zrQHz4FmNgRb6vYCuZ__jXffR0h6Bmj48CTsW_WgEMFdGk8rv3Zxwbm88ha_SDKynXnlV820TT1keQoCtpwJacWRFrHt290r2WQxVWuSmhQgwrJtb-jeNpVsXx9DRCdEbjbMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇸🇳
فوت‌مرتکاتو: پاتریک‌ویرا اسطوره فوتبال جهان بزودی سرمربی تیم‌ملی سنگال می‌شود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/101690" target="_blank">📅 20:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101689">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TF2DKYPU7UOIVyKA9tmz801XxkXMG1NP1DXqOd3tr0JV5zFFdI56QCXb9z1Uys22lapQaCjHzXxRiUZ0KkNyGJgpowKc5J9aBg5vaxhZZ9I93s6t_k17vLfch2E2UuU9alGL0hobL1EK-GLcaMLJrOkbqjqQfqL6RGqZjz3Zjw0pBYtnnC_D1Ykiw39ajOa3XHnHcy79cr7GKSAGwqqRrA5Wcp5NsWEwJDpwMQoLxhqq6X26PeHLj5xhhFTG98CtV_V1WQpGA3hrAFizDugUI1Ww9UfwDVlYy8e-FbpahWO6x2ejvDb_pPkeAdNNCKBTXwy0Z8Oyz3NLNPtNJQDkpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
❌
#رسمیییییی
؛ باشگاه بارسلونا اعلام کرد که رباط جانبی داخلی زانو راست فرنکی‌ دی‌یونگ دچار پارگی شده و ماه‌ها شرایط بازی برای کاتالان‌ها رو نداره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/101689" target="_blank">📅 20:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101688">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u5zrh-93QaoOfsjoArYdy1uzzSEU1iftEtDLYl2Mvk3pNw26vpsRvjqfpU-EmIF9k3a2e_xnKd9zgZAhFvp5UWbFAI2DjxKbbnBoZ3X1EOYFuzbk6T8SsSQuEfCkz3r3KnOoCxkVIgF4muLZm9AnsMzIrOFqc9kle1SfhswRnV6asCzQDaA7cvptpDvKyM9DUoI23rAxzq1-YUwd66hDEn8jSYIbZbVAdAjHSigW9UBGO_zaHsfnNdMPHQj8hBFd3cR0KB_YWCO-8vWHz_pWqsP9cum4rdNMjvfHRCi2-ThyLKg-t3404y0pmV40NPeWm6Ej1oQ_FE8eWP1iGgKTcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
توماس مولر در مورد ادعاهایی مبنی بر اینکه داوران به لیونل مسی در زمین امتیاز می‌دهند:
🔺
"در مرحله یک‌چهارم نهایی جام جهانی 2010، ما مقابل آرژانتین پیش بودیم و مسی دقیقاً کنار من ایستاده بود.
🔺
توپ به سمت بالا پرتاب شد و به دست من برخورد کرد. داور بلافاصله کارت زرد به من نشان داد. من مطمئنم که این فقط به این دلیل بود که مسی آنجا حضور داشت. ما 2 بر 0 جلو بودیم، بنابراین احساس می‌کردم که داور فکر می‌کرد:  بیایید کمی به مسی و آرژانتین کمک کنیم.'"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/101688" target="_blank">📅 19:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101687">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
فوووری و رسمی؛ تریلر FC 27 منتشر شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/101687" target="_blank">📅 19:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101686">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IEAmRjWaspdOmK7kunyDZ19wz5y_1jSgSZZo4u5w8cVZUgRGLAa4DBRCQYf-3OpaQ0fKTcC1RHvzj3aN2gBu5cxIhQxuIQ_HdQhLSjA7K4pIra1kbv3dvAjC2Bt2MlwC285YlA79uR-yt5tnvjd6B1T73c3bffRbEvAkTuhyJ741jP0XfRbPtxhPm9j7XhAmtIGkn46yn2ISwHO55BQQlcrKjLpJQbaGqPkvEEsV6zN0cuLRhRDwaUOkHam6Xi3cscU263RIWgtc2Rw9WOj4afVmAqmFUqhAyDEDPiJxoRboayDPMoRLSMZ-9gWzqRlW8gmsUi0bEx9wurqrKgWeKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمیییییی: الیوت اندرسون ستاره تیم‌ملی انگلیس به منچسترسیتی پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/101686" target="_blank">📅 19:39 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101685">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dTeiqp4AmxG_xxm5rCx9tdmuk2D_Rep_1aMq9Jfz-SQ3yiPZo3DrFpLJdiHrVN3xtbXNugz9TRWdayejw_cHA6PxpXILwSKvCimmaAeF-IaRXKQw64CdCBcF9gvYz3TNYEZerSJKsWvt55oPen4hY-q3gRBih5kksUzXPD3CUKRVG-4m9doClApEeZGe41896A-kfVrk6eBO07XeiTiSpc-5SOJZuDzQ73X-fIs5-D8F5hxAgPU6ye1DbNewHT9LdInEVEek5viClDmhM4dqpHRqf6GLOkSkvHWO8Rxbe59hYjZQkVDXIeZ-d2u8UaOTn666QSzDIDyqeDa3RJJ0vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمیییییی
: الیوت اندرسون ستاره تیم‌ملی انگلیس به منچسترسیتی پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/101685" target="_blank">📅 19:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101684">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B2wInQZlJWHqUZHm7eGYuz5JvSjeG01WSmapSUWOIMJWRg8QWq9f8jtkEmRena4uq6gpgae-wXguKTbXxxqoLwQMRrPrExjZgSMc9Kyd_NKrLdl5z-mSDt5ERcOsSJlJX_qVnBYD7ZXTXLU3Bgi-DJYOxHPJpFtcVq36NTpYXvqSjRq3f7IiLJipG-f5VvOlBXBpdKdCByVpW-hdl09--81cJYPMkklWVZdwA-JJ9t2YA5hQnvHyJo05SnHD_F_YU4NGwaJWfmvdZOqmILerSvg48rsWZ8lXiKEB1W02SNOGO8X0xlkp-xIGM3iIKtbuj4qFJ1kAeKms8odbpJl_tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاسمیرو رویاهای همتونو داره زندگی میکنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/101684" target="_blank">📅 19:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101683">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vp8Q2WMOMg7kqEXm43zLLDtv0jSRuMf0CihpPuIOtuAaRaLvyRbitvUUUUFTCe6ZesUesItTBDDwNc48xwr7rIi0IXUy_d3PjW1HdAUgcOX1PV9SeMFYNmV8l7BzpWafG5yu3jpfEIIe_wbfKfDMrcWDmXi9nbBZ8kNH5OnbhfeAJL6KmXiUYUn2cPAARCOZxAZdBt0xaUS0_EFIMV4UxcKL0aF4YbwY8h3h6nFN2cjmHUEzrxk2p5pSH0PfHiLDfX-w3212B9noY6ZmI7y7Nnz5SSAoE3aa6LBf1FMQ5a9k4rvtWK4YbCgJomjE7pNtJBy-Eki-jVGa9kov1ADnpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
#رسمیییییی
: قرارداد لوکا مودریچ با میلان به مدت یک‌فصل دیگر تمدید شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/101683" target="_blank">📅 19:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101682">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5tJxu85fvcxFHfJd7aqM7dvjb3abNkZlimnP76-E-S71SXFX66zk9WarteMiW3iEq30FsrbRXtP9HTZp3SR95vuzmSrBKEAKCWDcnlxqyB9NyFDgapG8klNZV0gnrxGskDmxpNwXKOUoltN4muUZAnLq9dml7IP0S_AZTqwE3fJKNjJLDrJJxxWFko9Ljt1qXUBvu7o163jZ-pns51MEOw3D51WTx-CjUJdwXdvekVCb3zUU4zrTrfPtBmDClUn4si-IwtKY2ABW7FLoVBRaBYRlZoUcuLE6X0sVB5_Gy23gn7qdTJ7kPXx-ocHP9V9MmfNZy4Bp7U8SyogBLT_og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/101682" target="_blank">📅 19:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101681">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4befd2a6b8.mp4?token=jbf4slB-WE9YnFUtCKkUo5c8j8H-_M5iQly2h_kOrG2n3d2HwnQ2lF3nASGsS-ln96b2rD1SlCO37ElxSjH1zp0EANd4zkis52LTtxV6hrcNgghIf3Oj4mqLp1TmZg44fWneJ4mfoK5X9ow_Ou2QmL1VBcT2IH-rtklvyJhxKl0mjM_WnkqsJXXgkjb9e0U4CYAlD5RQF74X_GNVAbZKXVp4zQsPFaZJ8LK1ODsntf47-jQ9NEiSMJwlD774obevYRVa32thGTb8zuunrrAlus3xHN6ipANGhSLHfQ7kamcpM3HN5lrhOtUmW7MfwURkWZUcbHW_QHUSgemJLZlzgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4befd2a6b8.mp4?token=jbf4slB-WE9YnFUtCKkUo5c8j8H-_M5iQly2h_kOrG2n3d2HwnQ2lF3nASGsS-ln96b2rD1SlCO37ElxSjH1zp0EANd4zkis52LTtxV6hrcNgghIf3Oj4mqLp1TmZg44fWneJ4mfoK5X9ow_Ou2QmL1VBcT2IH-rtklvyJhxKl0mjM_WnkqsJXXgkjb9e0U4CYAlD5RQF74X_GNVAbZKXVp4zQsPFaZJ8LK1ODsntf47-jQ9NEiSMJwlD774obevYRVa32thGTb8zuunrrAlus3xHN6ipANGhSLHfQ7kamcpM3HN5lrhOtUmW7MfwURkWZUcbHW_QHUSgemJLZlzgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
سوال: آیا مسی بهترین بازیکن تاریخ است؟
🇮🇱
نتانیاهو: باید بگویم، در کنار پله. اما در دوران ما و در دهه‌های اخیر قطعا مسی. او چند سال پیش به اسرائیل سفر کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/101681" target="_blank">📅 19:26 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101680">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
فوووری ترامپ: من در حال بررسی یک حمله گسترده هستم؛ بزرگ‌تر از هر حمله‌ای که تاکنون انجام داده‌ایم. به تصمیم‌گیری نزدیک شده‌ام. ما برای انجام آن کاملاً آماده هستیم.
اگر از اسرائیل بخواهم، ظرف دو دقیقه به این عملیات ملحق خواهد شد. ایران به اندازه کافی احساس درد نکرده است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/101680" target="_blank">📅 19:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101679">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae47457bbd.mp4?token=h23o_Rb1wRdOIqY5LzJbYpiivR86hWGCT-xhQk9PPzdSvkkG5tJuV_sxV-J0LwCkqs1_ZJh8EMMi95CkZP1M7K-dqlNRgMndwIN7AWiOsSVYpGZ7It2tK6DB9NgP1T8GhVHlz_m0_YFBtlaZNnbB9zAlNwibEgLdtO7m19LIxWHRZiRZTbX4boGKBXLle1bZS1020AYJF3ap_UNhsD4LQPXK8iotzKRs9qepsRlpTLXHkWr_m7ZGhz_F7do-FWgLJSqzEas9UuvfAYcZofk_swLxYMJBOMpQGhMHmNBQuYK6Jw163zTWQyQ7Zp-blrbvHRC3ECMGetKtnxkLxYgoVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae47457bbd.mp4?token=h23o_Rb1wRdOIqY5LzJbYpiivR86hWGCT-xhQk9PPzdSvkkG5tJuV_sxV-J0LwCkqs1_ZJh8EMMi95CkZP1M7K-dqlNRgMndwIN7AWiOsSVYpGZ7It2tK6DB9NgP1T8GhVHlz_m0_YFBtlaZNnbB9zAlNwibEgLdtO7m19LIxWHRZiRZTbX4boGKBXLle1bZS1020AYJF3ap_UNhsD4LQPXK8iotzKRs9qepsRlpTLXHkWr_m7ZGhz_F7do-FWgLJSqzEas9UuvfAYcZofk_swLxYMJBOMpQGhMHmNBQuYK6Jw163zTWQyQ7Zp-blrbvHRC3ECMGetKtnxkLxYgoVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
تنها جمله درست گفته شده از صداوسیما در سال جاری خطاب به امیرحسین ثابتی: ‏مگه تنگه هرمز مال ننت بوده که بدیم بره:)))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/101679" target="_blank">📅 19:18 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101677">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XXPVK0t04VUwlQualOU7-F4PpUw02ZXPhFkY0byyg4Plk_QqvsT2iQZB6UPh8ZL3JKOM3axHARW9JxfpPOL5ei1Iy00HN4qRurWoYmWwrwehszVPapmLq9zJEunyG7N7L7WjR-213KhxXDNp15VncTsfghKc7yn40kkq0CJGAJc7TgugNvle35xB48MSQEccZng_qk3E2nJiBS8pN3aPq3qR7ug4lbQchxwfZHdhRVjIEilBHXUGkwhNWwEMqALtO3BwvBagNjA9Hp9os1WnVPZSPM2iYONHWx__HexmgrH3JYQOXww3TwhPBWwGyqtzfkJ5DK768i5zBdP8qE3vkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L-HbbSD1J4XouxVI5m6JXKiYjd0ZqOb4DehGwWOl2d3PpfcL1QvXOqKZf_WslXf9etBjzBC8fVNV6I2sAVImX64B2cIl0LK22mOjDo1j0gMkAb7qQskRd45auA0xL0jdQh5cCz1qk5r1rR-Q7G4xcEgrhGalFgkBEypjJjZ7frZAToENfpCw0XsFKsbOorLTqlZGY32B752xeVzk1Vvwih3ArhvZC2gnfUCaI6QZK4k1ET4YHnJtT_PJ2P9YaAnwiLzl_f2NBmE3-KI05T9oMcEMhOOiF7K2Ims7G15KvsntV26jPgMwfgQ3hwmtN1FvdGTnDXwL0NHRFywE3RMVKA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
تبلیغات جورجینا واسه برند خودش Mimoa
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/101677" target="_blank">📅 19:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101676">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MlooQFy63H8YB2AwpNcsLfnA9lqeJI05RGL8MpFl5eZwzRVb3ZWi6meEs20wP1oA7MxNLDTI3Fw-Ioer7dBdxSQHW7EnJCCfer8XTmFB0TAKxpVujYxL756q4o93jGEHB5Zep2ELM1tyTZfmUWP3QkYUw7nMzX-eQLGhFeVP2azN1J_hDCu_Zv5iBcbRlY4Nob8FtYu1mnhZotRwL461BfrQB5zqvEbbYwVahDwmCXTZOha0G0yzXALNy2otRDfKI_PrEBZ0JwAHezu1niJWIvBLYXoGGt__5xzCsStqEupipHGZYvRjKgOBwqRQwhiekOW9IerZRfbNvgzOStIkag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
منتخب بازیکنان آزاد فوتبال جهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/101676" target="_blank">📅 19:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101675">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78d6746099.mp4?token=RgI279gLnqBRhoY8h9n6czn12zGJtUSCtZXjn3yfsU2CM0AH339rhingTK0fI8KrMTeA17AYaiTg_6BSNXjwrLuThE4D8nrjHLrbTvpuUup5QHAr34OYaoMsc7EYgwPCuhHs898gSr1Ei7W65pJfT74KNcH7cZBHcoafd2_Ot3xvQHlgwP_VnuyJ5wPObbv_0b42q-WtSCXDCPnoea6oJeW5SMajQLO7mMTGS98MJcpoaMZ5Cirq0cFrf43rl__3__KjAbtjEFGnQRKIKq6zMKb-FrbdQwz0QyI74Zq1CgJwoySEh8iufMZMSAPNbYJocu04HLAxutk8UripS4wIy0T0lDyV5kfvFuaWHshF7BShzbRcQ4YDQeNtbQhmHgQvFq-yAeo-G4MoGvK5n1xXxXPRVYcawfFtpwKGH2LrsEJHbi1xk-HGtNiWz8OX6pu-B1mYQWiw1RlH1axU_L2h1Wyrkq-GlEh7LT0kRdGQb-SwlT-VYNmVjWvzbytIWCrZFtsR5YJxBGhlw4FJHh3dDwl5V6_Uebmcwis51DvGQkX-PlbBmBZ05Vzcg7GkRl4yqNcM7yyUpG9KCp-XKKMoYAKkWAPH36Z8r2D0n__90CkFfTjMapSw5Ow7LrhoE-YUn-mBAgtxGiU09wD_HVrh-NsGxzfCCgMcQ2mlbYtZ0Q0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78d6746099.mp4?token=RgI279gLnqBRhoY8h9n6czn12zGJtUSCtZXjn3yfsU2CM0AH339rhingTK0fI8KrMTeA17AYaiTg_6BSNXjwrLuThE4D8nrjHLrbTvpuUup5QHAr34OYaoMsc7EYgwPCuhHs898gSr1Ei7W65pJfT74KNcH7cZBHcoafd2_Ot3xvQHlgwP_VnuyJ5wPObbv_0b42q-WtSCXDCPnoea6oJeW5SMajQLO7mMTGS98MJcpoaMZ5Cirq0cFrf43rl__3__KjAbtjEFGnQRKIKq6zMKb-FrbdQwz0QyI74Zq1CgJwoySEh8iufMZMSAPNbYJocu04HLAxutk8UripS4wIy0T0lDyV5kfvFuaWHshF7BShzbRcQ4YDQeNtbQhmHgQvFq-yAeo-G4MoGvK5n1xXxXPRVYcawfFtpwKGH2LrsEJHbi1xk-HGtNiWz8OX6pu-B1mYQWiw1RlH1axU_L2h1Wyrkq-GlEh7LT0kRdGQb-SwlT-VYNmVjWvzbytIWCrZFtsR5YJxBGhlw4FJHh3dDwl5V6_Uebmcwis51DvGQkX-PlbBmBZ05Vzcg7GkRl4yqNcM7yyUpG9KCp-XKKMoYAKkWAPH36Z8r2D0n__90CkFfTjMapSw5Ow7LrhoE-YUn-mBAgtxGiU09wD_HVrh-NsGxzfCCgMcQ2mlbYtZ0Q0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇱
ویرجیل فن‌دایک مقابل بازیکنان بزرگ فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/101675" target="_blank">📅 19:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101674">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10e54bda82.mp4?token=YptV7Dgyroy-H10CPSvn7XwKjcQZWJLaiKoQoTBa5VyF-7mH50evgqBumFqZPtCAc1q4YKCeFLqNOZ8-s39TjULjrnaioQ9cB4pXVb9ilyhNDK-pHIcqkl-0uNd3PmiU3aztxVJ983P4Mv0v6PfkQeA4iXPYDm2n31lqiI-i8iFb_zj42dhhN78WP5JZ80TQNv_CQ4k-GvpgCfqD_E9hpHcADgI3yoIJ7NdcvvBlZj_F0GIKYOGG5mfMRVh3nnanaXIKmIwxhc6U3fmElhAU2VdtBS_Y1lwqAK9Grhc0KgHLmLZ02IfgnEzdOF9Hdosio5judoLk69gYJfvRuDFP7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10e54bda82.mp4?token=YptV7Dgyroy-H10CPSvn7XwKjcQZWJLaiKoQoTBa5VyF-7mH50evgqBumFqZPtCAc1q4YKCeFLqNOZ8-s39TjULjrnaioQ9cB4pXVb9ilyhNDK-pHIcqkl-0uNd3PmiU3aztxVJ983P4Mv0v6PfkQeA4iXPYDm2n31lqiI-i8iFb_zj42dhhN78WP5JZ80TQNv_CQ4k-GvpgCfqD_E9hpHcADgI3yoIJ7NdcvvBlZj_F0GIKYOGG5mfMRVh3nnanaXIKmIwxhc6U3fmElhAU2VdtBS_Y1lwqAK9Grhc0KgHLmLZ02IfgnEzdOF9Hdosio5judoLk69gYJfvRuDFP7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
داستان دختربازی افشین قطبی
😂
😐
محمدرضا مامانی، بازیکن پرسپولیس در دهه ۸۰ با یه دختره دوست بوده، افشین قطبی خبر نداشته از رابطه‌شون، قطبی به دختره شماره میده، دختره به مامانی میگه، بعد نیکبخت کثافت‌کاری میکرده و چاق شده بوده میخواستن بهش گیر بدن، این با آتویی که از قطبی گرفته بوده گروکشی میکنه
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/101674" target="_blank">📅 18:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101673">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/601e0d1ecd.mp4?token=RKhy0f0ISd0OtKy0awvUedsoAniV-Pt9RbwQq8hgLiT5NIgley7Z9r2hIKpb5-qD0aNmpXCP3oevAK67XnIGs3457jPQYRbo24qc279JPu-_1hSOq0pLsO1MndqYmw1gGdEwDFHwAtHvUcOpSsDB1JqkLVofpoDFo9GyORKHYOYAhj4MZ1yCSTfdnFkhLF81-_YWy2qs_QpGNUFxeGfTjMcY8pkiivOrJ9XAlaj9LxVJN_jJrhU8v7Wb4hlN5TkRK6jPJrqRTxN8qybt1cfuFuojPdpuB3RLyxur_MIQ8NGHAc_JwXcoo1YKKTlypgrcaIB02j92p_HxipGzk3hQ6QPgO2GWp08Nyus1lZHANOUe5vgvF_Fv-dT5kpNe3UtfZSpd1l4dAuZISQOfs5RZcrWvn8i8jW16cbDF8ZwiMLJy3Xz9dkO3fgUZqwv7ylxBUS0LNiRPFYr_F-W8udw8gWQzb-CC7KshCS5E2LujQOKq8XjoBz2QZxgbavSKJuKJvl-2CDXdFmLckwfmIrEElRBrJOziOVyhqm9uEIBYmbZBprnA9u7qBvzLDXh4duk_PqBFHkwpC-_5PXF3p507Mmceqf4mINGPmRlMEVrkYxU6YrH42R3nblyTl_Jl28OIE02iykbAB9GYykG4108qhqjw7cfFWSMIaAjDTzbqA_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/601e0d1ecd.mp4?token=RKhy0f0ISd0OtKy0awvUedsoAniV-Pt9RbwQq8hgLiT5NIgley7Z9r2hIKpb5-qD0aNmpXCP3oevAK67XnIGs3457jPQYRbo24qc279JPu-_1hSOq0pLsO1MndqYmw1gGdEwDFHwAtHvUcOpSsDB1JqkLVofpoDFo9GyORKHYOYAhj4MZ1yCSTfdnFkhLF81-_YWy2qs_QpGNUFxeGfTjMcY8pkiivOrJ9XAlaj9LxVJN_jJrhU8v7Wb4hlN5TkRK6jPJrqRTxN8qybt1cfuFuojPdpuB3RLyxur_MIQ8NGHAc_JwXcoo1YKKTlypgrcaIB02j92p_HxipGzk3hQ6QPgO2GWp08Nyus1lZHANOUe5vgvF_Fv-dT5kpNe3UtfZSpd1l4dAuZISQOfs5RZcrWvn8i8jW16cbDF8ZwiMLJy3Xz9dkO3fgUZqwv7ylxBUS0LNiRPFYr_F-W8udw8gWQzb-CC7KshCS5E2LujQOKq8XjoBz2QZxgbavSKJuKJvl-2CDXdFmLckwfmIrEElRBrJOziOVyhqm9uEIBYmbZBprnA9u7qBvzLDXh4duk_PqBFHkwpC-_5PXF3p507Mmceqf4mINGPmRlMEVrkYxU6YrH42R3nblyTl_Jl28OIE02iykbAB9GYykG4108qhqjw7cfFWSMIaAjDTzbqA_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
روایت عادل فردوسی پور از الکس فرگوسن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/101673" target="_blank">📅 18:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101672">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EB70JOf1odqxzkYOu6FDTPTFHJbWe8mDCQ6pJkRrH6qdMKjF3vFJgzW14N8kMeIZpFw5YIWb8V3twGlrP2Kpg3xreOSqfP2CPECot1HelVNvWGiPb7dZ11VkYgcX3zOlcUTZ5GhXOzmi7w7ClOOADFwVsQXabcK_tMCropmI4pcvDgqZHy9EU4Lf0280AOuL87kjMx-UFj92i9y1RZPeCJNsMCXZ4rh4pTFP3XPUBX83DnsEBZPYv9kBwQVKWEOCKXd1V9uA2nIXqwsmdO2KlZhgPa5YaEgMEP6VNyEqS-PmpPg-2VSCjCvkw31hAjWGiFgapHoPaGpBunSe0r4P7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_فوتبال‌180
؛ باشگاه نساجی مازندران با ارائه پیشنهادی خواستار جذب محمد خلیفه به صورت قرضی به مدت نیم فصل از استقلال شد. این درخواست از سوی مجتبی‌حسینی به شهاب‌زندی مدیرعامل این تیم منتقل شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/101672" target="_blank">📅 18:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101671">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/815514f088.mp4?token=VXxUUX_kinZ2wdmNjcN694nTBiyonrspYBbogDFIjW-ShBZ9QzHM1q33nrak90xuLBxg39xiOY8wL39b4Vtx7wAO1R3jT6ye6KJ3zzgewmIok6KYWR-q_x6vRzGE4_m1g20SQn-ZSDhxhewkr-VtPBKFIZyVU9hbp8KIWIpZgQgl_0v_q3uV8liaiuiwckcKS3Sw3w0tJeH5YYYVp5HnYLwEgskwMj6qc0DJeAZ_QX_ljgZ1zCOAKbdv8T04A74X6NIMuAmhVg2nnETLhdj9vLjkuwdwtVRgn7ahtOZvIEr_YkdJELuhGT_ZQMoK8UXNuZIHjnHmPrtvPbM2kAcKIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/815514f088.mp4?token=VXxUUX_kinZ2wdmNjcN694nTBiyonrspYBbogDFIjW-ShBZ9QzHM1q33nrak90xuLBxg39xiOY8wL39b4Vtx7wAO1R3jT6ye6KJ3zzgewmIok6KYWR-q_x6vRzGE4_m1g20SQn-ZSDhxhewkr-VtPBKFIZyVU9hbp8KIWIpZgQgl_0v_q3uV8liaiuiwckcKS3Sw3w0tJeH5YYYVp5HnYLwEgskwMj6qc0DJeAZ_QX_ljgZ1zCOAKbdv8T04A74X6NIMuAmhVg2nnETLhdj9vLjkuwdwtVRgn7ahtOZvIEr_YkdJELuhGT_ZQMoK8UXNuZIHjnHmPrtvPbM2kAcKIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
مارک کوکوریا موهای بلندش را فقط به خاطر استایلش نگه نداشته است. پسر بزرگ او، «ماتئو»، مبتلا به اوتیسم است و در تشخیص چهره‌ها مشکل دارد. کوکوریا می‌گوید موهای بلندش کمک میکند پسرش هنگام تماشای مسابقه بتواند او را راحت‌تر بین ۲۲ بازیکن پیدا کند. به همین دلیل هم قصد ندارد موهایش را کوتاه کند؛ چون برای پسرش فقط یک مدل مو نیست، بلکه نشانه‌ای است که باعث می‌شود پدرش را گم نکند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/101671" target="_blank">📅 18:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101668">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ST6eo3B34Xj0ZeqX6Z3tSRbqDchYBiINa-qHASR8aMpOltYsx-9OKR0nD0i2kvw8xmvieaOKmTLXwrfefmHgpdP85m5nFQE8VMeIQgXS1lZuVGbkCTBwSAS64Dgl0YQpVAfWoqN0eEA9xkdhO8B3G80dHz8BD5uVF6mp42QRRs3K_P7UvNVgqzeFaKr140cJI1lJBIg6CKs2Ul-_tYiteRUJ58QKcCsdo-Cdl8lcPS_ApmUJB_bex7T9F1Yrgxd29qYJ217O8hwzUd8O1CfoIoJQ4fDfmwm2EmDCHIad0GVJbf4so-1h4XUmXvEFWKuFFcJVcVSx27Gv1HMN7CA1Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g1vkkjs21BmP7MfMcuyhV9smh1ODH-wqkd1bziKOL0-Pp5ZP6xSvKdRdsc9Qcanv0joIyy3EIN8GYdaBLxhKKrJIaIcgRGQeAK1vHUPDuAiWfCbekfu08ZaHyy01sBs9DkCA-olyU9ymp_zo9nU2RvbvH-Q6sFbuDUsF7Op2xAbycf_NPvHLRi3I3yIUUT29ebq7b8bZLNczV2WAoYXlZXhX7VqmKttJJZVLnVOJvmUqcvqP_k5LOlQk4HeCJRTZo9s6cv41h2k7G1VajipBagkFPM_10SHzind16vwJOBLmeKA6aXm-ppG4g2vQdDNPYlrkWNAc9C7gnntr5uu4Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BRrsPW05O3pwcUa82LJIda_m4qdtmLo4Y-wSmfelMnxaMHDajlA35i_8drW5F5zE7LaBDUWtSMiirTHq0xyiJZ5T1Q31gvEs3m10CUE0ioEF1N977Or1FwqmCUO8hykF3vNr8tAfR0dBN6uxKhkke2PetmyziMefOLqW7RIKMPCtGipe6a-1zGfjtpyWbGZr86veFxRcTzhuyEQaeRzW3DEWXgKot2654zUED9KK2OAwPEyPz2XW0KzMeq1jSJEckzXus65btVowV2T-TQXHZUuQFpjWOO8H7hALMtBTne-iVI6tHe4Y9FnZDSUWc3Ms0_GVZbdyVPIOugKivXij7w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
رونمایی الهلال عربستان از کیت‌دوم فصل‌آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/101668" target="_blank">📅 18:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101667">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qGaeFby7uG2mrVSxh2Vi9NGZf5NOb_CHsP23AMWJqsFpp0Bl6EAVKm1OXp9lnchcuLvm8-HQ33PZLS7Z832YC0liB8JYC3_dq2E2qLozbsSSAjmVhTue4zcsbRbynPsjjG4Wqel4CBxdDzt0gEXNddKSGbe-poL07Uw4d1YtBDdKCqUWoKBm5lh21KMv4r2sqwUfbNXQvUkuoAohf3VQ1_MYz66HfEbbhH09940tJMtoKKRx72sYuV-YL2e3qS94adKcYgdYKmB-NheoNwXG3Bzw_PWWY78O0iuK2fAQiJvUUwMiY1RRV5NJH24ftVFnCIWzL58eKJEzm7Bhk6S4yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
جلد نهایی بازی FC27
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/101667" target="_blank">📅 18:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101666">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7937bcbd97.mp4?token=h31z2uhBPigjGoLQYEi9zAnAItFRDVlvPc03CsZlBM_Ux5MnRV0yBxYg7IfWnpTpTUGK2xUZl1tmjdrQsytYfkLfaX6U-BR0c_M_q4yo5Ye1zBs84yi5YwldDYtttpP2l5SiaMdALCQlwOjUMqXzRMiQ7SRrXcH_ZSs8l5CymW_Gw4xi2cnk_hzEVcK4XEGHL19Z3FJLeRznfA5jJaDg3l2JlDME2Q0bFIzT7j-6eJP_8qiJVHUX8Hbc8zW4X-ziI0tZFqOxbl9yJwUry0xsCPI8EwWJ56d2Tua_Xc19epYnqd1MjKZvj8oUJ2cJv7uKriY2Wo2NJVqzoRxNyGx4ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7937bcbd97.mp4?token=h31z2uhBPigjGoLQYEi9zAnAItFRDVlvPc03CsZlBM_Ux5MnRV0yBxYg7IfWnpTpTUGK2xUZl1tmjdrQsytYfkLfaX6U-BR0c_M_q4yo5Ye1zBs84yi5YwldDYtttpP2l5SiaMdALCQlwOjUMqXzRMiQ7SRrXcH_ZSs8l5CymW_Gw4xi2cnk_hzEVcK4XEGHL19Z3FJLeRznfA5jJaDg3l2JlDME2Q0bFIzT7j-6eJP_8qiJVHUX8Hbc8zW4X-ziI0tZFqOxbl9yJwUry0xsCPI8EwWJ56d2Tua_Xc19epYnqd1MjKZvj8oUJ2cJv7uKriY2Wo2NJVqzoRxNyGx4ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🔵
خاطره قایدی از اولین بازی در استقلال: جمله‌ای که بعد چند سال هنوز از ذهن قایدی پاک نشده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/101666" target="_blank">📅 17:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101665">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f40a1d01f.mp4?token=kJvFWe3mZCGG68cTqHQ2uFqZMqDQ37LZDHlek1YO5aqW2nrQdKW9Ww7_BpkQAJbJEJlE6Si2sp0ThWHFVSW20p8U3jNCofIR58XL9jX1ISgd_kAvIMpikuw8aUsE5WQnCFcrf9wxawysz5HSLC55q5qyP1VZO_VwP89vwRNfJSjbljm-wTJUpTi7EfdVhfS-Pb9-umSImbl2CUEBobmRgBF4maR5mM5AwsWNvPuAtFvj1WyIzKxC-4B0bnwiqYAR4PI-yfbHiBWF3mOYOLHE3Xa-llRHssXiymloOUv-gmT7rY3s_DSbNRU2iDEBWKT1KHZSXvJW3lm9BjcHAYpyvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f40a1d01f.mp4?token=kJvFWe3mZCGG68cTqHQ2uFqZMqDQ37LZDHlek1YO5aqW2nrQdKW9Ww7_BpkQAJbJEJlE6Si2sp0ThWHFVSW20p8U3jNCofIR58XL9jX1ISgd_kAvIMpikuw8aUsE5WQnCFcrf9wxawysz5HSLC55q5qyP1VZO_VwP89vwRNfJSjbljm-wTJUpTi7EfdVhfS-Pb9-umSImbl2CUEBobmRgBF4maR5mM5AwsWNvPuAtFvj1WyIzKxC-4B0bnwiqYAR4PI-yfbHiBWF3mOYOLHE3Xa-llRHssXiymloOUv-gmT7rY3s_DSbNRU2iDEBWKT1KHZSXvJW3lm9BjcHAYpyvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🎙
صحبت‌های چندی‌پیش مهدی‌مهدوی‌کیا اسطوره فوتبال ایران درباره تیم‌ملی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/101665" target="_blank">📅 17:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101664">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PB6aURjh67VKJhAhNBy9vyaTrFb3BVsUtIe9XkvHlJ1FyUvXKiR-s6qgBYIqRj9OUkl6JcTgd0vPtTYadAeuvKC4Akg-lNny8TiRMkkTOlWmKubcg3thbQdGCSiZrNCDNuiM5F1IgQM1IKe61rE2Hkbkh3I2lIkCw7M9U9X4QirgVQFyOTdl0yaWHyzxwiuomxtGvI29Ndyd_uITtmrsXU4daVd4Yz-3f_WuDlrZ2oDRToXzWudkZ0LaYMDDbKcM2XWEOKpgICko6Mj93D6mj2atqceE6L4gxSWsWxXJK8RSrGhLuNoRCVcq_itl56qHrdyamqq25IxufwSw-s8ebg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گارناچو رسماً به صورت قرضی با بند خرید اجباری به استون ویلا پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/101664" target="_blank">📅 17:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101663">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUoWVDp1wJ2xdYE1idcnFrBSYzyEvdEL9EQu7JwCxwlyc93YpfbSRPtCFQZ70296OALQB2uBRAI0mDqsP0y-YG-2Gz9lLoKjHryfzLqhCp9RykDMNmt8cE9eLY_sCcdCl1g--XcBrMaVEI-cIk1OK0L4BNqDCx0U_ICMi3Wmo56XNuOPwgj6A1ciYD_eDQO6LjMFIiUjw3xPLaLwGMMaBNakmSMW8i5Rij8pGnh2d1jOOVgw4ARM1azTAruqp4qJzNPi38kscIA-2B0Bw1jXveEW99c8SNv2ZAFVO7678OnjH8tWri22CLFrN38O8t2mLKjwMOdpAHLRwhNvdR9mDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🔥
آمار ۶ مهاجم برتر این‌فصل اروپا:
🇫🇷
دمبله ۲۶ گل‌ و ۱۴ پاس‌گل
🇩🇪
هری‌کین ۷۳ گل و ۸ پاس‌گل
🇪🇸
یامال ۲۵ گل‌ و ۲۰ پاس‌گل
🇩🇪
اولیسه ۲۷ گل‌ و ۳۴ پاس‌گل
🇪🇸
امباپه ۵۶ گل‌ و ۱۳ پاس‌گل ‌
🇫🇷
کوارتسخلیا ۲۳ گل‌و ۱۰پاس‌گل‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/101663" target="_blank">📅 17:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101662">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb77439ac7.mp4?token=UrS997TzuZJOYvpAJypwo2CjCsqREHKG1OO6Ho-mJ6zlE-b8FykqPNlCqRGzJPC5F9zLYxzc3LlvbsbBtHJa1mi817NmFSHs9pjUFmhp3BshXaAoIr4SMZL00GC0DbmG-zeIubRHQZKm1wiFOEen1Z9EacZlE5DmSsj4-_2dAy-em0wW0pSbE_oOwLUISPXOSRwA7fl36XXf7LfZcP3dDubNXnQRqby_uaLuU69HQd5__cME94MSXtlvhSIv0KOLhdAoEw2n7ae2PO4nQrAdqQKWbSIelrysuY8ZvIV3ONiEzMaIwOdKdkcO7uT0zR5jYmrTo86Su0CEc21uvDvrVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb77439ac7.mp4?token=UrS997TzuZJOYvpAJypwo2CjCsqREHKG1OO6Ho-mJ6zlE-b8FykqPNlCqRGzJPC5F9zLYxzc3LlvbsbBtHJa1mi817NmFSHs9pjUFmhp3BshXaAoIr4SMZL00GC0DbmG-zeIubRHQZKm1wiFOEen1Z9EacZlE5DmSsj4-_2dAy-em0wW0pSbE_oOwLUISPXOSRwA7fl36XXf7LfZcP3dDubNXnQRqby_uaLuU69HQd5__cME94MSXtlvhSIv0KOLhdAoEw2n7ae2PO4nQrAdqQKWbSIelrysuY8ZvIV3ONiEzMaIwOdKdkcO7uT0zR5jYmrTo86Su0CEc21uvDvrVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
حمایت سید جلال و قیاسی از علی دایی و کنایه‌شان به بیرانوند: بعضی‌ها اصلا نمیدونن احترام چیه، هیچی دیگه سَر جاش نیست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/101662" target="_blank">📅 16:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101661">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/098313b0c4.mp4?token=DSE3HdPOFMH0eypkvXK3igm_Wvs1UUa43lnv464WxEMPIsQaODGRxcrMKR2H27gEmQEiyPiQN_zZkwN2rYQleRWxWjU1a3dMI3mgrFy44itNXRjM_2IuNV7dDaX8EURXVH9im8yUnwLQACZ8Xd7hGUC9mTybEUtg5DuCGmHfGVeXyN3I1FRZxpahDl6KwOT3rMQzwoKjeuLNv2kK4ZSt6D2qRyX9lYVWHl1mOSdyCtk8_F7gqzzH_Cv95cBYvWwOWZt5YgT0zY_X72EVN5dEU-TWfYIEfyevX9WqoX381qjqNSOjseshBKWQCjbDY1i7m9FFna4gayYLM1Pq3GpNPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/098313b0c4.mp4?token=DSE3HdPOFMH0eypkvXK3igm_Wvs1UUa43lnv464WxEMPIsQaODGRxcrMKR2H27gEmQEiyPiQN_zZkwN2rYQleRWxWjU1a3dMI3mgrFy44itNXRjM_2IuNV7dDaX8EURXVH9im8yUnwLQACZ8Xd7hGUC9mTybEUtg5DuCGmHfGVeXyN3I1FRZxpahDl6KwOT3rMQzwoKjeuLNv2kK4ZSt6D2qRyX9lYVWHl1mOSdyCtk8_F7gqzzH_Cv95cBYvWwOWZt5YgT0zY_X72EVN5dEU-TWfYIEfyevX9WqoX381qjqNSOjseshBKWQCjbDY1i7m9FFna4gayYLM1Pq3GpNPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
⛔️
نگرش متفاوت دو سرمربی؛ یکی شکست را پذیرفته و با قبول واقعیت به فکر آینده‌ست؛ دیگری زمین و زمان را بابت عدم صعود از گروه در جام‌جهانی ۴٨ تیمی مقصر می‌داند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/101661" target="_blank">📅 16:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101660">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2eee7743d.mp4?token=McoEZ5_BQRDembH1ZNyXeV5lEngGZp1x5N2B1-YYGYMudDA2qLjlEW28lnYFScAZ1DooPgcsb_nr2F22yDoYW3LqTmLTdFiCmpSbWCHxbSf0PAiAalVcsqj92FoNLOVZ-LRo6DOEpKq8co2FIloUqHA1Vj-viUQBpUVJWF3LEar3aMjPgH4uBTdBUx8vPddqpkz10U_rTlFCnQaPBMsSxCkK7CR8LCfnJOf_8RdHhECrCfL8lxtWnIqBHC3rtWneQOizXi-kCIr7e0HxH7Yxuuh3g1JYp0fCa7PoZN8oqrB39rrbTIqKTdAWuxoymmxz-T5ZfqtatYlibzznQjvzKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2eee7743d.mp4?token=McoEZ5_BQRDembH1ZNyXeV5lEngGZp1x5N2B1-YYGYMudDA2qLjlEW28lnYFScAZ1DooPgcsb_nr2F22yDoYW3LqTmLTdFiCmpSbWCHxbSf0PAiAalVcsqj92FoNLOVZ-LRo6DOEpKq8co2FIloUqHA1Vj-viUQBpUVJWF3LEar3aMjPgH4uBTdBUx8vPddqpkz10U_rTlFCnQaPBMsSxCkK7CR8LCfnJOf_8RdHhECrCfL8lxtWnIqBHC3rtWneQOizXi-kCIr7e0HxH7Yxuuh3g1JYp0fCa7PoZN8oqrB39rrbTIqKTdAWuxoymmxz-T5ZfqtatYlibzznQjvzKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
مهدی‌قایدی: حسرت خیلی زیادی دارم که چرا بهم در جام‌جهانی بازی نرسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/101660" target="_blank">📅 16:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101659">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
فرانسه کارکنان سفارت خود در تهران را تخلیه کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/101659" target="_blank">📅 15:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101658">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ca9e664c4.mp4?token=pDg6-wT3h_hqXaXduX-EgTvruowFfNu7IJVbklCPhendsL4OktX6XRBIWscmXMvNP2o4eEk9Hvs21ST-lO-K2OLazh_viNnGPxZ2ZHmtd2QzYy1snKRoJVMw0k7OYNTXerQ8wuPQcwO_oncOJZ3stLlzfUU6_rlooSSpMjhsWGe12F72hD9XAUocgrmUbuDJvaUx0vBOchMfQPqCWqjALf-J6Y5mBYxUEPwfzTGVio7y4Hx78BWx9K3u49WbOAT1xdc3p0RzIyjiKGmWU0D-wb5sI-Z53kksZPU6_TJYqxKZERay3265Kxo2jQOsYcMKoovig7t63I3CB-Xf9tIwgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ca9e664c4.mp4?token=pDg6-wT3h_hqXaXduX-EgTvruowFfNu7IJVbklCPhendsL4OktX6XRBIWscmXMvNP2o4eEk9Hvs21ST-lO-K2OLazh_viNnGPxZ2ZHmtd2QzYy1snKRoJVMw0k7OYNTXerQ8wuPQcwO_oncOJZ3stLlzfUU6_rlooSSpMjhsWGe12F72hD9XAUocgrmUbuDJvaUx0vBOchMfQPqCWqjALf-J6Y5mBYxUEPwfzTGVio7y4Hx78BWx9K3u49WbOAT1xdc3p0RzIyjiKGmWU0D-wb5sI-Z53kksZPU6_TJYqxKZERay3265Kxo2jQOsYcMKoovig7t63I3CB-Xf9tIwgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اجراى مريم اميرجلالى و حميد لولايى در بين ٢ نيمه جام جهانی‌سمه خالص
🤣
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/101658" target="_blank">📅 15:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101657">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔥
▶️
چند سوپرسیو دروازه‌بان در فصول‌گذشته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/101657" target="_blank">📅 15:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101656">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a89e53e52e.mp4?token=DfKOWMRJcQVnfVqhYDDtFfE-fat9g_Zd3CKqNiC-WFPmKonhckqnfXG7vIBqFAdVbzKEukRkq-MYUVWdEvsVdqcuec-xHr6Pt_WjVWXIbVg8ZHoZE9Ix91PaCUO_sCX5Dyq5luXSNgflpDPPfCh1HlgAn3of2Gu8CwIUfDek9e8E24dgSscR80xcHQV5QvNJzPKWHK43w2OzeybnkBhc1jPJZf6GvJDsuYvSyBmeI0_lBZt6FOwIDzpTu8dyUybpciSpYP6EdPq97O-NwiY6qEcu_N3tFQeVS31IoPwiQYk4-ii2KPFrExwOZ0HeZ7zeI4NZkR_EE00XfKef5G0z7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a89e53e52e.mp4?token=DfKOWMRJcQVnfVqhYDDtFfE-fat9g_Zd3CKqNiC-WFPmKonhckqnfXG7vIBqFAdVbzKEukRkq-MYUVWdEvsVdqcuec-xHr6Pt_WjVWXIbVg8ZHoZE9Ix91PaCUO_sCX5Dyq5luXSNgflpDPPfCh1HlgAn3of2Gu8CwIUfDek9e8E24dgSscR80xcHQV5QvNJzPKWHK43w2OzeybnkBhc1jPJZf6GvJDsuYvSyBmeI0_lBZt6FOwIDzpTu8dyUybpciSpYP6EdPq97O-NwiY6qEcu_N3tFQeVS31IoPwiQYk4-ii2KPFrExwOZ0HeZ7zeI4NZkR_EE00XfKef5G0z7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
❗️
علی‌قلی‌زاده: امیر‌ عابدزاده استعداد بی‌نظیری در نوشتن و رپ داره؛ از او خیلی چیزها یاد گرفتم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/101656" target="_blank">📅 15:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101655">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MEXta4jOvFS0jlo8G5qtenvAOSz1qbROLwkgaHVUi9u_Y5fnlOzhZt63E0x_MNUgxnaH1OI9HcYgS8k_rbYdQXapwCi1pPYzh0qqBnTxxanODtl6tl_Fc0GXuR97k4WOGF4MW_CHy2yT1ithKLnItzJLP5Nu5mpypUopM8E6NXoiB6-a6BKXJDphBwa1q1Q6qpua3zjEq0Jc22qeBSCVW3-bUyvtNAkDBwNj0VFHRluGR6OVoeBfKGxzT85zrfxhK-3BhRPQAotr2Cu80t0mc6-mvWiIQKq5z1TvP7ZZb23gAEytyUff0D8gs2NMBxmmOwav47yWZWPx6B3_8xqeGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامنت گاوی زیر پست یامال
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/101655" target="_blank">📅 15:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101654">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00c5973b07.mp4?token=mtxO93sMBvOhGgrxo0fbzTNaWK6XOr0RaS_iItNlzmUEu1B_8hzNWfBFb9lTAv_Xg8J-iFY4ZDBcy2z19hyHVcveYeNS4xHtxCNkR1_zqqCR2rc7EZox4m-u1uxta6yvj4G7_YaiIt7Hq9NMPWvS8rXxtT0cQQkGfjgo6w8FnrvGw0vzEBvLZt1QkUzjjGJItME_nbfCR7v5BVvJ8iRtSVL9vkgQoNPMvJtj2mb7DLYzjkLoqjCW3Knj5n4p4t8GX1UnPaS_gMMdeerp0YBS8h0oNvjQA3Xoz8JiAvorVE7xVyg4lDu9Rf_mqYwthVakZmH83oatO1YGCrZrf7FBdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00c5973b07.mp4?token=mtxO93sMBvOhGgrxo0fbzTNaWK6XOr0RaS_iItNlzmUEu1B_8hzNWfBFb9lTAv_Xg8J-iFY4ZDBcy2z19hyHVcveYeNS4xHtxCNkR1_zqqCR2rc7EZox4m-u1uxta6yvj4G7_YaiIt7Hq9NMPWvS8rXxtT0cQQkGfjgo6w8FnrvGw0vzEBvLZt1QkUzjjGJItME_nbfCR7v5BVvJ8iRtSVL9vkgQoNPMvJtj2mb7DLYzjkLoqjCW3Knj5n4p4t8GX1UnPaS_gMMdeerp0YBS8h0oNvjQA3Xoz8JiAvorVE7xVyg4lDu9Rf_mqYwthVakZmH83oatO1YGCrZrf7FBdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ینی چه بلایی سر اون تیم پرانگیزه اومده بود؟! ببینید قبل از بازی با فرانسه همگی بمب انرژی و انگیزه بودن ولی تو فینال امسال انگار همگی از مراسم ختم اومده بودن.
بازیکنان تیم آرژانتین تو بازی انگلیس داشتن به معنای واقعی کلمه میجنگیدن و بعد از بازی مثل دیوونه ها جشن گرفتن اما یهو نمیدونم چی شده بود که اونا از لحظه شروع فینال هیچ تلاشی برای بردن نکردن!
بحث تئوری توطئه نیست و هیچ خدشه ای به قهرمانی شایسته اسپانیا وارد نمیکنم اما مطمئنم تو رختکن یه خبر بد یا یه اتفاق ناگوار برای آرژانتین افتاده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/101654" target="_blank">📅 14:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101653">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d995b135a.mp4?token=GKgzqka4zAmt4kQ2f2VkNIg-uqpUvgWn_yyNWzzW1o0ngjz_yJRLXIPMEO9U2e5j_w75dFAVCfc5NaMaiEryeM25pT3jsGeYca3DQ5-tUjCdMlw-MLALC02ISWI9tHi0NyiGrIh9pLiVOjcvhwMrJKe_W9uO9vYN1LPDgP8NGft3QMqFEfwb0JScLM1xGCCalry-_BVZgMdJVXThTnbZZp2ybotQM2QLAzTBi3CBEQntju-b9f9NlJs6R5tNmJxJaK5WGygOgssVTzjf2w5lOyp8SBSoVanpk3vNQU60S-piqLWoYR18tNqn_QKptu3U8_1WJmLAsBR-uat3HgndLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d995b135a.mp4?token=GKgzqka4zAmt4kQ2f2VkNIg-uqpUvgWn_yyNWzzW1o0ngjz_yJRLXIPMEO9U2e5j_w75dFAVCfc5NaMaiEryeM25pT3jsGeYca3DQ5-tUjCdMlw-MLALC02ISWI9tHi0NyiGrIh9pLiVOjcvhwMrJKe_W9uO9vYN1LPDgP8NGft3QMqFEfwb0JScLM1xGCCalry-_BVZgMdJVXThTnbZZp2ybotQM2QLAzTBi3CBEQntju-b9f9NlJs6R5tNmJxJaK5WGygOgssVTzjf2w5lOyp8SBSoVanpk3vNQU60S-piqLWoYR18tNqn_QKptu3U8_1WJmLAsBR-uat3HgndLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
رضا جاودانی در جواب نگرانی عادل فردوسی‌پور، به جای فکر کردن به خودش، با آرامش گفت: «بذار بیکار بشم... مهم نیست.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/101653" target="_blank">📅 14:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101652">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7be59d405.mp4?token=sICydQOO5cVaECNUgbqIj7ncQt7112iwEnVaJwEgV638kvPwf4sK3kpbrq-kohukodmjjTJHrOvQ3UJG1ZE-_ca8IsqoaScz-pNA56E2w1wZBl20E_-6J1wQ-unvv-JhBPYqYNw71JgZzYAXRGeBHrBvJrWkb_JS0cENCst-x0HkisT1hqJy4_3mmQfx_x-wxiYPpEIA_KGa3E8cL1iAOn5rE-GZCP0uasBHC8cxzLofA1K0ir4yXjfO_w9Axpj8hLA7LQQ3Toh3QfVB_9MCZRpDPvghCCS8EccY_K26tJNG_bQSMRwXNnIknoHqgG11JPaYPCRTzd11qp8A6K7cTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7be59d405.mp4?token=sICydQOO5cVaECNUgbqIj7ncQt7112iwEnVaJwEgV638kvPwf4sK3kpbrq-kohukodmjjTJHrOvQ3UJG1ZE-_ca8IsqoaScz-pNA56E2w1wZBl20E_-6J1wQ-unvv-JhBPYqYNw71JgZzYAXRGeBHrBvJrWkb_JS0cENCst-x0HkisT1hqJy4_3mmQfx_x-wxiYPpEIA_KGa3E8cL1iAOn5rE-GZCP0uasBHC8cxzLofA1K0ir4yXjfO_w9Axpj8hLA7LQQ3Toh3QfVB_9MCZRpDPvghCCS8EccY_K26tJNG_bQSMRwXNnIknoHqgG11JPaYPCRTzd11qp8A6K7cTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇹
شیروانی، مافیا ایرانی فوتبال ایتالیا: به اینزاگی گفتم طارمی را جذب کن، اما طارمی در اینتر جواب نداد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/101652" target="_blank">📅 14:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101651">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dxg6-eUGn7x1rflQlMmMP5_EvvWdqBLfhpKpf91FB9bXzmJhR0O0ny8n6CfJYMdC4ejeazW5-d2srtAOqfCrYZGGYF2F19-ifY0VakzHuD5dIouCmuSY8SAAvnbmPpGD7qtOmkHM2Ck0fUJRrWP9gHehuoo0jg3htxLMAZeewPZEGAlWTKwqNyWw0RB-aP8xpwoxmqTOih4HgqsRMTlC8eeQQDMDkL1s-fz7-vjvDo_SyMqoerT05fJa49_YDJzkHZ_2b1VjunELmpOX_0-ZQsdPcqZxyXW2pTeHGn_M2AYkfB-BpT7_iea94BjgJSCn1pG23CvpqkI2GgtisRRVtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
کریم‌آدیمی برای عقد قرارداد رسمی با باشگاه بارسلونا راهی دفاتر نیوکمپ شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/101651" target="_blank">📅 14:12 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101650">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d13a0e1e37.mp4?token=Bn5WFWLHbv1Zs1nG2qIJkDukypt0usGwpAkbniaeJK7J_IwHzOyy5Zyet45rVfsx5fxr1ElmMdOFvUTX8bRhYWikBIkD4xmxZEZJ8QVk2jT6ejbXFTDHBb3VHprSeBpEP3C07CH5r4xA3HXuX7SEJxeHEg-TcFZtr0Hj9d39B01mY5R2Yt4jJsBzAXlfnV_GAe7R7L59lDU7YkWvXfTAUd4HG3j3F8C-2RZC6Z8Xumax8A4XeQ6KJ9a8nCAMxHfFU_0nOY-6zEzQr9mDZ0geHwwY9edsEEbl57uugP9RvaFGixOv-5xST0Dox027wKnhy4SkYyjwUOdw5aio5iPa-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d13a0e1e37.mp4?token=Bn5WFWLHbv1Zs1nG2qIJkDukypt0usGwpAkbniaeJK7J_IwHzOyy5Zyet45rVfsx5fxr1ElmMdOFvUTX8bRhYWikBIkD4xmxZEZJ8QVk2jT6ejbXFTDHBb3VHprSeBpEP3C07CH5r4xA3HXuX7SEJxeHEg-TcFZtr0Hj9d39B01mY5R2Yt4jJsBzAXlfnV_GAe7R7L59lDU7YkWvXfTAUd4HG3j3F8C-2RZC6Z8Xumax8A4XeQ6KJ9a8nCAMxHfFU_0nOY-6zEzQr9mDZ0geHwwY9edsEEbl57uugP9RvaFGixOv-5xST0Dox027wKnhy4SkYyjwUOdw5aio5iPa-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
محمد شیروانی از اعضای ایرانی مافیای فوتبال ایتالیا: با دیگو مارادونا رفیق صمیمی بودم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/101650" target="_blank">📅 14:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101649">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/chdGL6bY5nI4c_DVlCJ5kO0kTlIYedWUe3VOEYPKe3QsK7-sXTYgARju8Jz46dvwVcgMy6DJUEciAeNqEZ42PjEkC3HXM-q13MLmoTqP71c6aXYjMeI33tIdTHNOsUWe26VuPpd_I7fz23Bn0hQK0wsWwfuoM5rYsP11MB41eIAjgb9fS-dIQ_BPtSO0xSuGqfaRddaa3xnbbj-B-IknDYD6PH_mupm7cICZkFZDCHY9Q9Qiu2HpEOF6MkNo97btHpndATd7mvlFLuyr41djFpxc1_lZ-q1TsDXaflfBr10yZKaWSFpVm_t7L2p3vNe5z-Ec7ffxwHexyk5ndBKc-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
⚽️
#فوووووری
از مارکا: انریکه در روزهای اخیر با فران‌تورس تماس گرفته و پروژه آینده تیمش با حضور این بازیکن رو توضیح داده. قراره تورس نظر نهایی خودش رو بزودی اعلام کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/101649" target="_blank">📅 13:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101648">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f57cc284b.mp4?token=P5EO4pvyCEe1n5bAGlsuVkpHGWCZU1iB3zlNp3Jw0COFVezMQVuV7ODQw1n4YJcBm2J-ffmQ0a9TymVmbfqsx8GRQ529vZiAV5UhTm2Sb7wFVgSPuile9ubu_IrrcfLbucwdtBM0hygVbNvVxpwig-JwwNGCJ2kXk9O4TKbMmjgeOqwWTA_xPFNw1o7-JpZwNqDh2Kmw8s1ZQZwqEapVkJrVzh_W8YTanaOprfx0WznKwel1tDqoPvwkKQv5VMmZHJv3zqUXRFVqQi-3Sp4eMdZbzdLW9t_dA3lWlw-Gi9_zxthr1zMQ0kni9Yjd0ekiANUJu8UDQ8KRYo712Jkm1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f57cc284b.mp4?token=P5EO4pvyCEe1n5bAGlsuVkpHGWCZU1iB3zlNp3Jw0COFVezMQVuV7ODQw1n4YJcBm2J-ffmQ0a9TymVmbfqsx8GRQ529vZiAV5UhTm2Sb7wFVgSPuile9ubu_IrrcfLbucwdtBM0hygVbNvVxpwig-JwwNGCJ2kXk9O4TKbMmjgeOqwWTA_xPFNw1o7-JpZwNqDh2Kmw8s1ZQZwqEapVkJrVzh_W8YTanaOprfx0WznKwel1tDqoPvwkKQv5VMmZHJv3zqUXRFVqQi-3Sp4eMdZbzdLW9t_dA3lWlw-Gi9_zxthr1zMQ0kni9Yjd0ekiANUJu8UDQ8KRYo712Jkm1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سیدجلال‌حسینی: بدترین خاطره دوران فوتبالم بازی معروف با اولسان‌هیوندای کره‌جنوبی است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/101648" target="_blank">📅 13:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101647">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b841d71bb3.mp4?token=IPLORUASjXv0tQs2IQhDch6Tsxd1m8s6H4eSrfXlsauNMq3gjUI3pGCtfpYdUIEQVGQZ38AMYAQeiAR26vz0bxX1sA1xx3ztlCNU-Zst61q0kQceOuXMfFyJZUPusSGMgR1muDMQh5vjR-7utOKl7Juce3DVzJgnv2YhnR9arzSUDJFIsSfoLhprr2EDAJGaFXwPiutU4aY6LsQB2iwiKb3KMqjEsNxbSvcd6meZaxSgd47frMIU36k-XF2821iWU9LUiek-u2-Vd8XZ-wK68WplsHQLCtAue4By-E_1CFUASeX90N04A8zlDgXOSn3dMm_DWZxrUDS9VeRO7g5Q8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b841d71bb3.mp4?token=IPLORUASjXv0tQs2IQhDch6Tsxd1m8s6H4eSrfXlsauNMq3gjUI3pGCtfpYdUIEQVGQZ38AMYAQeiAR26vz0bxX1sA1xx3ztlCNU-Zst61q0kQceOuXMfFyJZUPusSGMgR1muDMQh5vjR-7utOKl7Juce3DVzJgnv2YhnR9arzSUDJFIsSfoLhprr2EDAJGaFXwPiutU4aY6LsQB2iwiKb3KMqjEsNxbSvcd6meZaxSgd47frMIU36k-XF2821iWU9LUiek-u2-Vd8XZ-wK68WplsHQLCtAue4By-E_1CFUASeX90N04A8zlDgXOSn3dMm_DWZxrUDS9VeRO7g5Q8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
کریم‌آدیمی برای عقد قرارداد رسمی با باشگاه بارسلونا راهی دفاتر نیوکمپ شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/101647" target="_blank">📅 13:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101646">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c225ae4bf.mp4?token=g4rF164kaXI9iF7cdIALLrRV7HQaNEz_nxkRJ9As2xl1mx1yGW271NjPsG1JXO8qLkgFFxMAn50RbmrQGFisroh-1nhmGDqiYuHb5Ms_UosLaqknXAvbDtlzePBW1BfCj9_g3lUOxBzI8tpxO0jQD-mk0jY_yq0OOLdlXz2QG3V_kOmh2u6oCidlLKS5Zb7j12lJRtU3QzQv9fJTdfJ2VfO-y4KKxC8NcD7B37665R4iVtc7XR7fd4OVuAqQey45DAaUDtCCxTBzHTNYy0Sa1yNnhbFPfsq4jyF2YgaK4lVzI0joccWP6er02El4kBojzb4lLi8sATxUcfsfxo9HzYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c225ae4bf.mp4?token=g4rF164kaXI9iF7cdIALLrRV7HQaNEz_nxkRJ9As2xl1mx1yGW271NjPsG1JXO8qLkgFFxMAn50RbmrQGFisroh-1nhmGDqiYuHb5Ms_UosLaqknXAvbDtlzePBW1BfCj9_g3lUOxBzI8tpxO0jQD-mk0jY_yq0OOLdlXz2QG3V_kOmh2u6oCidlLKS5Zb7j12lJRtU3QzQv9fJTdfJ2VfO-y4KKxC8NcD7B37665R4iVtc7XR7fd4OVuAqQey45DAaUDtCCxTBzHTNYy0Sa1yNnhbFPfsq4jyF2YgaK4lVzI0joccWP6er02El4kBojzb4lLi8sATxUcfsfxo9HzYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
یادی‌کنیم از دوران درخشان سادیو‌مانه سنگالی در ایام حضورش در لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/101646" target="_blank">📅 13:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101645">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCzhMXnrcdpJCG0FaLbSnYUYLcDmQU81Sj9F4a39hTboBGvPzFE37YlcGnAKI0thqWRmzeVWC1m_SG9GqEF-P81-P2TVX_QamY2IqoYEwVBxlaXc6OplZwRlBPzIAe1RF4yh5ZXqvRYP18sxk_gBVry9TG_uxBPqszwFgIQZMREL_VM4fgTxc0W-kldrVKFcur3sDRrslfhbBAbi8tAE9sjwKisuNaIbUqjKBsA4EhnJAmOMEVSs5lgt9Q7iVfDxdmlzJ6fJ2_3TQpCThHlvHqFCYyhM0Zbces2IDvR_rCCGXPfpeA8GtEPxPHJtHNZTSyAp5jYJoZFplKY_4NyAlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/101645" target="_blank">📅 13:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101644">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CK7-qgr3Y4xpVikGuNKYFnfeDDhn1B4S7aIvHVt4roRXYvteHwImRbHcp_nsuBUP-Se4bK_o628mRNOvnpENCI-OUBTybC2ArO4uM5qDG-0NZda4X0Now_IRBDNIQproWXRvvxcnly_VTBxXpg5bTBC2TD-B5HuTFk3ZnWc3NNHIblQ5baGvUgS3whNMRilxA5b2SJ_lgckd1j_PGxMA-hLRQbcG3fnAY1plMy9phTJYnx9IuRTUQMrR1sdLUoCO_ev3kP9gmmdmBOVkdjYOI_IU5mA0iyIdUGyKxo5DjNCafA4VtbbUjFucB2NS-f2XQPt2liWT8dLB1KlFe6Ff4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
⚽️
مارکا: رئال‌مادرید فارغ از جذب رودری، تمام تلاش خودشو برای جذب اولیسه به کار میگیره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/101644" target="_blank">📅 13:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101643">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qm8jv_qSNxpqq91jruF3lAug7fIrJRN3rTuhenTKu4L0ONOIGfXcHgy4VJE7fSHB5yLwNIiHUUbTFtp5lti687A7GdDj0U0xDDAl4BV4nKkEAcuWstYzS4nL03tzM9GXeNjelnjWQCB-A5BZlQdz2uIwdq-NfBJqR7ZE6KFYy_S9hGIv6vljpaoxCUXB2Z5yRkYF1KK9BkU1a3SBjX8npsdpj7unNHEwNFvBYkBXv_M7meSbfaHsJDqUI2JZaRqqjswff3cJrh37Ca_r-dp98D6Cw2BfaLlQD2ljUzI-Tvevpd6QsihS_BUyH7tadXoerrgTFIVjFgfDbVazKneZNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
⚽️
مارکا: رئال‌مادرید فارغ از جذب رودری، تمام تلاش خودشو برای جذب اولیسه به کار میگیره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/101643" target="_blank">📅 13:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101642">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c46077059.mp4?token=iW8KNdKeyjip4w_FVUQeqGB8VBwCnXq26sFT-4ppfGPrzNgACL0bhanqEGNcjWGn77lZ9HVMuBWYB-iKk_k_g1Lr-SSz6gSjwg_a5zVJQGvWt42XFyvUaRJp5e3aYUP0t2NyLB8A2Nt4d3kUkjqfRNzuKqhnHfagCexlJYuBLFiabbWVK8yeJ1u814c85UXbZJl1oOCBD5cHCcnJOoAfAdVTJehcNbpsCRdxKQs3syadx3bfQzWbLs_vPvIAteBt1aJznmvowZEavhJmBmIkaY71wksjXyyEBaBbku5uVmGW2osK4_MEKM3eUJ4B-wKKCGSgrZLyAjAz7MMyYifuyBGFTxTrAlrIsaXaEK8wpsTsPUKyhfWGXOxKjPRnQSoGOjoCDM_pAcjRjTvBbilTMcp1MReEBd1EBGn8nGWis3EBUEuLtNgATxp6VfdmJJuYl7CvgmY3fsfjWnwltUMlfWeKBhB5_pGsvY3af2fgPZV-FrnxZNbZAdcVFnY6huf-HIML3iAMnO57cF6OTRTw-nAU8fvJjdI9uYrVS5GXh8ZzuS06MxZ1Af3BAkvNYb0jkVITxg2WMrBMZpcbnUDhTD5gDjqYDP5MbKgzVGVU_LRN02vii_lpHHSumpMTKVMShttYTF7vCGyyhTr-VFtJERFuIVIzzuUjWYOZzpDdYeo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c46077059.mp4?token=iW8KNdKeyjip4w_FVUQeqGB8VBwCnXq26sFT-4ppfGPrzNgACL0bhanqEGNcjWGn77lZ9HVMuBWYB-iKk_k_g1Lr-SSz6gSjwg_a5zVJQGvWt42XFyvUaRJp5e3aYUP0t2NyLB8A2Nt4d3kUkjqfRNzuKqhnHfagCexlJYuBLFiabbWVK8yeJ1u814c85UXbZJl1oOCBD5cHCcnJOoAfAdVTJehcNbpsCRdxKQs3syadx3bfQzWbLs_vPvIAteBt1aJznmvowZEavhJmBmIkaY71wksjXyyEBaBbku5uVmGW2osK4_MEKM3eUJ4B-wKKCGSgrZLyAjAz7MMyYifuyBGFTxTrAlrIsaXaEK8wpsTsPUKyhfWGXOxKjPRnQSoGOjoCDM_pAcjRjTvBbilTMcp1MReEBd1EBGn8nGWis3EBUEuLtNgATxp6VfdmJJuYl7CvgmY3fsfjWnwltUMlfWeKBhB5_pGsvY3af2fgPZV-FrnxZNbZAdcVFnY6huf-HIML3iAMnO57cF6OTRTw-nAU8fvJjdI9uYrVS5GXh8ZzuS06MxZ1Af3BAkvNYb0jkVITxg2WMrBMZpcbnUDhTD5gDjqYDP5MbKgzVGVU_LRN02vii_lpHHSumpMTKVMShttYTF7vCGyyhTr-VFtJERFuIVIzzuUjWYOZzpDdYeo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
▶️
هنر استپ‌ و گلزنی از برخی ستارگان فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/101642" target="_blank">📅 13:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101641">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PMDtsCmPK1lePwhIkapctouD5qdlhvUOSEqYfL_m_fWUbtUOkjpuzDbvUetGGJv24ZA5EEA5998_1z3HUCaPr_10YcTXtUzRCI2zqD6MmaisxrSb_dOez5La4Q82VAMXRzwYCNBoQ_oyb5OE792gr_wsnXSvxulp8AotDmPvJTMDT99609xtltJg6EqA6U8f5Dvr9tqWsen7HMGibb5iDSvDlBUGxyhaGZKmGDs-_koekItXs1oQyPY1FTY6uCAYvIXYkDYxli4NHaBwul46ITmJcR6T4IlL_ZqbV2PqMnEJo83SU1lWGZibbhLzNF59vZfvnrnV3RrP5tJQww134w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
باشگاه بارسلونا در صورت عدم جذب آلوارز، داروین نونیز مهاجم الهلال را زیر نظر دارد
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/101641" target="_blank">📅 12:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101640">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NqDPdcSb6BpClt85IbgQNSYwotGFMrZrwPYlvLagvsb5dMutdzZ7DBP4vR-g6veCOtbXqKAfINN0vrS2nZc_uoYqRxof5NsKslDrdo9_7M1t42YajlqcFzPV7njSX5bFEW54SvwRmsKJPai8zt2ECVGTtq6wauglP5IQ3Lef132JuhH3DLjkrRURxtFOmSWl-mXRgzuL2nyz4K6BatZkYL8tmGR6gxNSVBFoO4CpP7KTee5x2LuE6f_6a5qZE5piEchxKkqtMtaSt1677mtZPBUpQiryB9AFrOhOD5dzDTr29ad9QPtuATTeKRXzuaL_tRdpJ61vleQ5ZpntVegxgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
😢
خانم‌شکیرا و چنتا از اساطیر NBA
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/101640" target="_blank">📅 12:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101639">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8fa0ff87b.mp4?token=pCJxXMdCXAb6gAEqH-EpAVVE6ADVXi2teeXWpEh7J_SceJPyTpUw_W_VfynlhfM3weAkmmpsdizI2j_6wi-mP7E7qqHQbw-adY-PSWnkCRsxlvxbx0jssaLBanwOerEEkjRU4_pliTt_T3X1WDmI83bC1cYIE7rIFd47OI2e4ymYKdbqKSySc2OcbLVUrj3alYVL99d6St6w2rVzrUGn36miTiUzQMSYnZEmKztT6DHre-I0df24Dt2KjYs1N0IUOuaavlPCbAXjb9LMrg-LHjsZU47uNaq-EBdg8OQMZt53_r83Id6VD9XrpBcsnP8iGdlhdYsu0_KMfgY61rUxBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8fa0ff87b.mp4?token=pCJxXMdCXAb6gAEqH-EpAVVE6ADVXi2teeXWpEh7J_SceJPyTpUw_W_VfynlhfM3weAkmmpsdizI2j_6wi-mP7E7qqHQbw-adY-PSWnkCRsxlvxbx0jssaLBanwOerEEkjRU4_pliTt_T3X1WDmI83bC1cYIE7rIFd47OI2e4ymYKdbqKSySc2OcbLVUrj3alYVL99d6St6w2rVzrUGn36miTiUzQMSYnZEmKztT6DHre-I0df24Dt2KjYs1N0IUOuaavlPCbAXjb9LMrg-LHjsZU47uNaq-EBdg8OQMZt53_r83Id6VD9XrpBcsnP8iGdlhdYsu0_KMfgY61rUxBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
سید جلال حسینی: اشتباه کردم همه زندگیم رو برای فوتبال گذاشتم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/101639" target="_blank">📅 12:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101638">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yn6GElbaMHXt7lDOm1G2QwQrEJ4c1eH70Y_mEhH7_Dn5JR2rayh1uayOVvW9Z8lrz77XzIEAbvuOwA97EYrW-WuCtPrVZDpFn9VnVsW4ez03lzvCq7K49SIa5SlpBfXNqpTGLrQ5Wvp6iFYhwV-V77ddl_U1CSgx3CTX941O9_r1i_D9HYDsU-bmsqPpYcmasmcazqZyOxPWFYoqXBHl2g3UXAhUP7X8HnUMCpQTSgl7YXDDaJb6UGpd7UpcEE5FFWuEI5Xp6iaq_Rb5mc1dR9ndHGn6UPLZnagkpwX4NzBJrQ_rwp6VCF_Ojqe6hkoL-LjrRVt4O0VT66ckbWnnVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
📰
بیلد‌آلمان: آرسنال حاضر است برای جذب دیامانده ستاره ساحل‌عاج مبلغ ۱۰۰ میلیون یورو پرداخت کند اما این بازیکن خواستار حضور در پاری‌سن‌ژرمن شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/101638" target="_blank">📅 12:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101637">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e657d4048f.mp4?token=HtdMqQ1S46hWzVepHLJHG5jCBDmJ3iasMxkboArj4NEEQ58MVz3-tqd2c3bMquyXtd1j-3ItIVm9MU4o1UOhr0HZYU4W-Atvm9BaRlddlqInzNOJRZkiMO70-yoaihMO_Z1-vUJB5xXwWMxWAT_o3Iw76A3TsRVTFtj9K0mMe2zaIxzMz6UAkZnEO9vd024m4NPjU4CYN1vvFiOVZtEcynYMtBclwhCO3HtR4jIcjuc-7uP9QTUx26rkS5dHcS0d5awRzZLC3l7lMjlnMvk2XJsss2CeCnvBb-ul-RLhYjFqRm2hd0hNMSFnT6ovrvILfjH8gYrjSVJJ477Ge7m6H1-uTSBZQG1l2fUcvP4PWiRUVtCUYJMizUmPk7txe6lbXafDxQUFrxIxmmMrihOYcwq_OKHJmnLqeyJpV4e_8q8tRUToOD7nyjK11HlhPy2p7O3FKsOGj1uklS9LKTHRUnKTsMR9oCHHHxf0jwUxKD14tsUWjjI5E1bPWM3tSyd4PW-XpUrfc3wQ5KY3pGWEyOBAGT0x14KwWoAK9iqzi-lq2Ii9DUOeUgiZ0At8AEPsbTcHVt24d7TPfsR-WAQhKNOSw0X6L1knlWvKIc8eIza8ksjeebCRB9XL7D5NOihzz2x6nMWxDTAtrdDBoHZ2T9hJCM_KRaC2SrhsAJmP188" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e657d4048f.mp4?token=HtdMqQ1S46hWzVepHLJHG5jCBDmJ3iasMxkboArj4NEEQ58MVz3-tqd2c3bMquyXtd1j-3ItIVm9MU4o1UOhr0HZYU4W-Atvm9BaRlddlqInzNOJRZkiMO70-yoaihMO_Z1-vUJB5xXwWMxWAT_o3Iw76A3TsRVTFtj9K0mMe2zaIxzMz6UAkZnEO9vd024m4NPjU4CYN1vvFiOVZtEcynYMtBclwhCO3HtR4jIcjuc-7uP9QTUx26rkS5dHcS0d5awRzZLC3l7lMjlnMvk2XJsss2CeCnvBb-ul-RLhYjFqRm2hd0hNMSFnT6ovrvILfjH8gYrjSVJJ477Ge7m6H1-uTSBZQG1l2fUcvP4PWiRUVtCUYJMizUmPk7txe6lbXafDxQUFrxIxmmMrihOYcwq_OKHJmnLqeyJpV4e_8q8tRUToOD7nyjK11HlhPy2p7O3FKsOGj1uklS9LKTHRUnKTsMR9oCHHHxf0jwUxKD14tsUWjjI5E1bPWM3tSyd4PW-XpUrfc3wQ5KY3pGWEyOBAGT0x14KwWoAK9iqzi-lq2Ii9DUOeUgiZ0At8AEPsbTcHVt24d7TPfsR-WAQhKNOSw0X6L1knlWvKIc8eIza8ksjeebCRB9XL7D5NOihzz2x6nMWxDTAtrdDBoHZ2T9hJCM_KRaC2SrhsAJmP188" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
▶️
عادل و جاودانی؛ دو مجری، دهه‌ها داستان!
‌
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/101637" target="_blank">📅 12:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101636">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WcCdFs75JxtVTcyNXq7Ie9Qltz3zKTUq5z6bUebji8GEd6UkzT2oEoRPGOdqlZ6B4kmw4bGMUeAEhV-AYRPA3TR1KTh9mnuxvHcUvBCE7bPdsfVl1RV71El1_2E4TJTRUCRd7EuDwBCq9wPLpxduXiHQZ-pJCpI7oSCYpILUIe8koHCXywxnTsNOXKn_89FC1QbEQSZl2rRdOwujBDicNnzuG67TfqB1TEvAy_0JTt1dW4BcXdNKZnD4bUaOySqfW09Y10y3OMlU-ij_mpzhYkqeeivoqc2PDaHkxYCroq_0NagBO8iUarop7FiTX6b8LBrcXrYG4cLJ25UVWWFOVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مایکل اولیسه پس از تعطیلاتش باید به دنبال خانه جدیدی در مونیخ باشد. او از سپتامبر ۲۰۲۴ ویلای ژروم بواتنگ در گرونوالد را اجاره کرده. بواتنگ اکنون می‌خواهد ملک لوکس خود را بفروشد، بنابراین اولیسه باید تا پایان ماه اوت از آنجا نقل مکان کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/101636" target="_blank">📅 12:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101632">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TlSM6gpHrlev-4TfmIfwsAJ2V13D9yzux9FXndcBeyDwYh41lOfWhh8zqLP3QK5aO0b7lPE3xva1MRhbKNWDwZzY0QM6lriM2n-eREGqhF4fQu4fbvvnMfHVAQma4UtBbi4Q686PwQRNOOD7Eg8TPF8V4-jIkKjy5CQoUjbpZ1yNXB1rnXGgAP5lawLeXe8Ryp4Wsuyzm1M4jNDMHMEy9xBaru0rLjAuyX4zujj5CqFbJJYFXBq3pj93kru_44ruAUAQIwYZ36Z0CANK8ibSuXzvGcC66FniEArwnU8h1Fld_4_Jafr22nJltZyF2U6EjHKebRF0rZQZochSHCYlEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cb9xLf6ixor6dmYE1Qpkcw0dp2cOmsKNMy_9cBFOrZUQ_RNwga19bPfmPFvnmQD71WRFm3LGlFH2avWzE0L9QT--Unf8zeduVORIItEpvE4mj1ojQzOs-QwZiMNrnIehh6P6IR_GGd08pDnWSsFvxjJ9lyOHsHObAjr5_MpZpI6MHZl3tDV7gGDLsXMtO92e9C8zIdfq6_uWSYDcvHnQdfRwMq_y8JkVtLo8NjrjBEdNyncAy-Yu2xX4p8QFq4ag-H0ChlTPpjFnlqZXwELJCbGFCvunPtfh6eY44cxVbPNtuG8WmlXzENMpyBVYzJzkrl_5ev6k8LwbZQI7hGRjEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EpmQ-nocKH5V1cpDeY96w-8iOhFmngtV2sh9b7GsGVzFuwaOJclJFKH1Htl7qQSGimU5tkEW0Z3Co4a5kafBZKnG5MioY2aUxLLDXtG7rE27KQUdfWzx9yVTUWx-AbMfRNZrJ_spm_xbdToeikIH9-DQQiUOEWD6GFilUHIBid9do9HC8TkIfzxmNtyskc7ctmhdYLAXRw8MoRGodnBt3ZC9XEeGC4u8DZtfXHxOAlcsBvfiqTezGgJKWDklGAnN8BZ4x3ycJ4BpFpw1tnVdd6ezX4CljPOLyKx6OSaA-sc_KI9WNWTcF-4KJVTOzI2RanH7NWtNys26RKmfjfe-AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GWlmQQkSlTAC_gflym4Y_YVnv3FvLtJBh-QQaGV6sEOg3-1Tc4KtPV-z86PqrPuyL-jNFnT1fnU96G_glz_llLpff8NCUJ8b1312ET5KPBkj9xr2C_nqiD5zkAYU2sUPhXB1KwYj5gFB405R272YAnxV7i3YfjZ4h-lv6HECyjo7CUxcWrazPXMtt6fQWExRcb_0ieFlXzVWpEWh0lUzVX6H7IBqVudNRoumfEA6g34T8_zKefrBc9U3Lr4IslafMOkkzrHgcNLGKKjI75JN9RM4mHSPRxk7oN-r_2U7Xt_nI8aIXcXcoS0SL8x9NeFOBWiLfhs3Iqb0_f--9B5z9Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇪🇸
کیت‌لورفته جدید رئال‌مادرید که قراره فردا رسما رونمایی بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/101632" target="_blank">📅 12:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101631">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HqMN77w4PzRiSz_Rsn9BmpU1if1wW-ygjpvPZGlC3tBZDF2IdIuHlYhWHXUB_y5XQrOuMR-ofdlmFspCAl6IiOFkAtjdv5PmvI4P4EXq_yea4AsWX4u4gQR_ZZf50TX7pL5fYnCr57hI7jhVMTaHbN9r-3EW4WOrxPP8_uN7sGGQ8ZDqFrK2zIUjPIDDAyft-gAA2HEcMhnZsIJXqyGoYAPS48WVu4odPyLYHpSFtVs2m58BHSLR-rfsjG6dWW6s1B-bLfwLQw5A6uwHi-t827Lm8wJDrAGUns_fYbYGkXda6Daaw3a08C8lbpX4uf_1g0pu0gYVOQvqGxz2vZF-DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
هواداران آرژانتین بعد از شکست مقابل اسپانیا در فینال جام جهانی 2026، یک دادخواست برای تکرار بازی فینال راه‌اندازی کرده‌اند. تا امروز بیش از 61 هزار و 500 نفر این درخواست را امضا کرده‌اند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/101631" target="_blank">📅 11:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101630">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TiXm6jExZlItS9lq-ahxSqLtMciW1mZvUcmx9EkhHI1P0an9eg7-lDeR3Bdy7mHmDPetwmYFeoLmV39lYrvNIGQUxd5nSzjcLfmufyiNkYf7dpuWsFm326pxZ1bNSWXk-3z3fea_xjPET7ii8MyCo849HT0dqFoDowCi54L-nDVo1wSpStp7-FHnMbFMbTkgZxnWBBy2bBOfovdHEJWha6B2VXuMMJLQNx0sE5YLK1BvBDwk7EuoGpEVejGcRsGWJQS2n0Yzd8k8tfeQvxSbZrOYUqPN_nIX8UPH7IcbvOUAZvOUe0d2ZQ69N6ZJG-Z-pNAL9O0R4tJqIpzf50TXMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
❌
لاگاتزتا: پپ‌گواردیولا پیشنهاد تیم‌ملی ایتالیا برای نشستن روی نیمکت را رد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/101630" target="_blank">📅 11:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101629">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fde3785bf.mp4?token=hBwZsTx0DQH7zRqZRBHHDKShisqozGwOimc-Cghq8JZOrTaahguYZs4lAURtdiTg6HAQ6cXphdTVIZD9-NTSCFDogzQZfcFXu9TLMnuJ91NieCBO1H3FbSqEYHY_YsuHSYU5LKW6evHiQGY495wF3-opFZ0nQkp-VZoHgycV8gA2FG6EG8ZOIK5wspi_FHWSzdoi-oBBRUDlEx4hge_wM9ahHnucgXNakF1xX_QAiEwnivuiBgaYdyJzFp5R6DzX012uQF9FGIQu9O5j7Z1L6cpmVzz8SqKNMO-WBOiGaf_izaHE6LPaTYAM7vt6lOitNzMpRwfGN49Ew3rQUkPyqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fde3785bf.mp4?token=hBwZsTx0DQH7zRqZRBHHDKShisqozGwOimc-Cghq8JZOrTaahguYZs4lAURtdiTg6HAQ6cXphdTVIZD9-NTSCFDogzQZfcFXu9TLMnuJ91NieCBO1H3FbSqEYHY_YsuHSYU5LKW6evHiQGY495wF3-opFZ0nQkp-VZoHgycV8gA2FG6EG8ZOIK5wspi_FHWSzdoi-oBBRUDlEx4hge_wM9ahHnucgXNakF1xX_QAiEwnivuiBgaYdyJzFp5R6DzX012uQF9FGIQu9O5j7Z1L6cpmVzz8SqKNMO-WBOiGaf_izaHE6LPaTYAM7vt6lOitNzMpRwfGN49Ew3rQUkPyqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
📊
▶️
آنالیز‌بازی رودری ستاره تیم‌ملی اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/101629" target="_blank">📅 11:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101628">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S7T4UYVN6h38ow78zHpCwB_sicNNm8Iiv33awR5J9G1e-UNUOZuGpywI676JucuOLqH5g5w1xk4RlWCpQLRdujXyXkt8YRGVnnEm43v5BXOepVrgdz1q05HjVti3WVs_gAWWjfLuz2bG6vkayvqXbn89lU0cXJssoVCG8hgHaTH_UIpGNG70CFk1S2DCGToMamAriMQwMGWX7DHcvbJclA8zPCYzshkfYYu9HQysTK8N9axjg1syJWvXksdXmZlup_WuYLllHS77BzCm43S0KwBk3j9jy3hiEgnnSIIRU5iqqqWusnAnhTV379kr7OAVD69ZIO62YC7quJiPvc3gRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
🇦🇷
اسکواد احتمالی آرژانتین در جام‌جهانی بعدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/101628" target="_blank">📅 11:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101627">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T8XzgvYBUY56bBVVPz2r0O0n2E3XBOSE20LA5q_-dq0dUvpeSNo1Y62HkRIKww_kSriPno8SY_KIAioE7jKWl_tIvzK42wy6BdXXuGUiyycxdvEKaALw1vlxtHCJUsPAp-B6c2xd0VaFxJGSZsEt0t-Ox2nu8w9qv6XJG2_h3c7JZUUCmx85lVFeulliFrGqbDCzceD6yHn9KAOhS0RVgkrAia0ygxxHHZzE_55rw-L-aJnxKOPckPN9lzALXSKnT9BgBIMCTxGsEsOwdKzljIjA7b7d0-upqOzSULt1UbN4I36FQgptI8mWROZrJc0FZVoJF0yPgNOQhO-Y8XUc2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">+ نیمار بعد حذف برزیل از جام خیلی افسرده بنظر میرسه
- نیمار :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/101627" target="_blank">📅 11:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101626">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nPV9x_ALOMM5jJGyB1Szba_OYFPLQpl8e4ymbMi_8EA8m0qMCmipu5oVP8D8nN4jatRrwzDrsS-Rg6T9w917CAeE3oZZosTxBVzFtgTaKsMehzPk8HefjDPBZbgZcH1oH0p-5zLEkE0CXp4rDXYTbB5o6oRe9IAo1cau4EpX0NIYuKTImok3QBifpXPLU5EybrFyktQIGfmSd3W-aNYCNHUX24--ogkRr2yHRMSXzEK7KrqoY9YtVVb_xEjQ7nMvLJ5laO-64oKcaZkQ2LcG8fO696wf6K-4dUu5xZspE3DBwhvYIl3yjkHZUwKHJ4Q9u8VHb9ceIXticuApQMRuSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
😢
خانم‌شکیرا و چنتا از اساطیر NBA
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/101626" target="_blank">📅 11:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101625">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qADoi8I1OxqVkp7USD-XqE21yMIADCQ4XetEC070KLODaeL8Yn9cn2x-Y-0EON4H6rWJEUJ05nqiA8J9wc9hKVg-0qDWV-_Ihowo9g8xKkAR16QtEOvq3VZLeaW-fwimiJxWCY2GYqtyb5A-U9XY3YELdxetXqu9Eo6xPmkPDfcWmRsUVxPlboPoT_UFpNdXb4wGeOYA2LJ6oTjfrhNWRiX0-gbibP41kYa-Q7JyWC8aaKEig8RMZxoyHBRkpi4DJV8ysdVQ3ejSY71vxfrg5UkpRg6Y0kQZ_M2cr1slk7CCgbZPaJorBOO91BK7-tcjMeGtEdkejnEaJkQ_I1ReVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⚽️
لکیپ: انریکه و پاریس تا 2030 برای تمدید قرارداد به توافق رسیدند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/101625" target="_blank">📅 10:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101624">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9443946ca4.mp4?token=XbLV96LZde9H_kKAVclh4T2FtKe8kQJmohcFHcr_A6ogXb3Oh_iP9qLOigqN_ZFRRolKSfAXyS1_ZQGeheacAj2skngzXF6wrPo5n1pipkDpUuqlAdTqA86t52UNlh4SZWQY69g5cDpRQi39D9cEas1CZhqiMEbOveG8YBtxG-F2fhxNtLFakJ4cbsCBlnvuUN7AMY3bTRwj2zVsxEC4CrsShMLzqJTBtyMwrjnIAKRzY4MAOTUhiKIF0daVTMXo-4OOWGXgJ-P9yI8fKVZksEmBcaDe8YMGzErJhwnNhmIZkORLLGGd3A6uXlrPtvICu_DnfVxmVfKpukOawO4iCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9443946ca4.mp4?token=XbLV96LZde9H_kKAVclh4T2FtKe8kQJmohcFHcr_A6ogXb3Oh_iP9qLOigqN_ZFRRolKSfAXyS1_ZQGeheacAj2skngzXF6wrPo5n1pipkDpUuqlAdTqA86t52UNlh4SZWQY69g5cDpRQi39D9cEas1CZhqiMEbOveG8YBtxG-F2fhxNtLFakJ4cbsCBlnvuUN7AMY3bTRwj2zVsxEC4CrsShMLzqJTBtyMwrjnIAKRzY4MAOTUhiKIF0daVTMXo-4OOWGXgJ-P9yI8fKVZksEmBcaDe8YMGzErJhwnNhmIZkORLLGGd3A6uXlrPtvICu_DnfVxmVfKpukOawO4iCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
سید جلال: حسین‌ماهینی واقعا بازیکن‌نفهمی بود. همیشه منو عصبی میکرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/101624" target="_blank">📅 10:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101623">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/509c49999b.mp4?token=C1bM2le6xAFW39OfM-gnc4GKx32vcGQ-sycYQJ6JyIIgSyTfYThDWCVmImZF0DhQ4dPsDmxZz-JvetAZMBEMOd_M7m6Q3B4DeCQwo6kegU093BXMA1FZBrEN0A09STt66AtEc6FEEuD__XpZ4rB0IycrjBKMNjPJRtU-VPeAZmu3VwnssTk7dYs-dpm6vLwNM6CzFew-ECjajpsF4QL-XCkoYQTafjd3IQFFLOFE1cGUEXthhr8RM6kGxo6gbfqHxnlVn4rC0auy9Gr_336ANh0s9Wprj8IOo-pBeFreoqcvv8jguwqVMcVQbtka0tYKHXZT9bYiJfEtNEGSEYagJJsAolsDAhcP24aZqZ6xBarUrXTHZUI_BWg1ewQdv5FHZSDMGrdNJOcMU5NdE2Ckpv_Uph8dTB0BrGd0s29e-4IEBU1z0mWW-5DB2qp7PmNyw4Ws1soAZkniK_enjGdrV5NvvMbMuflVwtp4NQJcuJzT6DyQAPogiFbUDmUi4UMdxTsFoQrQ5u84udBQsfn3Ofuks5woKQ07RPos3yhYafqEq7MxQcxTeVCfFBmw-yyFOWzA9lnqKG2z3Ek_vEWBVlUXM6XUCv5-KvwwcjwV6XfSkS79lkjWitPPYMl_SZ0adA_X04s4-vgMEcLWyY68_erHhDBe4PPk35hoEZZenxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/509c49999b.mp4?token=C1bM2le6xAFW39OfM-gnc4GKx32vcGQ-sycYQJ6JyIIgSyTfYThDWCVmImZF0DhQ4dPsDmxZz-JvetAZMBEMOd_M7m6Q3B4DeCQwo6kegU093BXMA1FZBrEN0A09STt66AtEc6FEEuD__XpZ4rB0IycrjBKMNjPJRtU-VPeAZmu3VwnssTk7dYs-dpm6vLwNM6CzFew-ECjajpsF4QL-XCkoYQTafjd3IQFFLOFE1cGUEXthhr8RM6kGxo6gbfqHxnlVn4rC0auy9Gr_336ANh0s9Wprj8IOo-pBeFreoqcvv8jguwqVMcVQbtka0tYKHXZT9bYiJfEtNEGSEYagJJsAolsDAhcP24aZqZ6xBarUrXTHZUI_BWg1ewQdv5FHZSDMGrdNJOcMU5NdE2Ckpv_Uph8dTB0BrGd0s29e-4IEBU1z0mWW-5DB2qp7PmNyw4Ws1soAZkniK_enjGdrV5NvvMbMuflVwtp4NQJcuJzT6DyQAPogiFbUDmUi4UMdxTsFoQrQ5u84udBQsfn3Ofuks5woKQ07RPos3yhYafqEq7MxQcxTeVCfFBmw-yyFOWzA9lnqKG2z3Ek_vEWBVlUXM6XUCv5-KvwwcjwV6XfSkS79lkjWitPPYMl_SZ0adA_X04s4-vgMEcLWyY68_erHhDBe4PPk35hoEZZenxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚨
به‌بهانه صحبت‌های اخیر قلعه‌نویی؛ یادی‌کنیم از روزی که مایلی‌کهن با شدیدترین الفاظ علیه سرمربی فعلی تیم‌منتخب ایران صحبت و افشاگری کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/101623" target="_blank">📅 10:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101622">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1802ff2c96.mp4?token=IP8suHzeXqW_H2KQMZ2EqLYBSe8-cB_wiAqSiHo6aMBKKJ6Y36nbJX7yW9N7vU8sf1DysqHp7KrroKHxq95G0RJb9YWHUJrCHWpIrhLoE8_4e-oZukcdp8dJw3v7YkkbXf2DEeaD9hPThJSBX_RCeL09M5vWxfnVxVq5y6WAnqpsWXGjP-Ivdooa6tuCbwKSMTGJl-eS-mHCpUKeJlz8wHDi0i9Lr8-TSm6DjTNo83pBBo2eSdCdQY5PlAfhwTGI43hPDA7FVgBLWUfrkqNw9uDUcp5pAupiTVMP0YyUXlR-oRusUTxlui6xuP6deBmNTrdBifzrHCKM8q10WKty4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1802ff2c96.mp4?token=IP8suHzeXqW_H2KQMZ2EqLYBSe8-cB_wiAqSiHo6aMBKKJ6Y36nbJX7yW9N7vU8sf1DysqHp7KrroKHxq95G0RJb9YWHUJrCHWpIrhLoE8_4e-oZukcdp8dJw3v7YkkbXf2DEeaD9hPThJSBX_RCeL09M5vWxfnVxVq5y6WAnqpsWXGjP-Ivdooa6tuCbwKSMTGJl-eS-mHCpUKeJlz8wHDi0i9Lr8-TSm6DjTNo83pBBo2eSdCdQY5PlAfhwTGI43hPDA7FVgBLWUfrkqNw9uDUcp5pAupiTVMP0YyUXlR-oRusUTxlui6xuP6deBmNTrdBifzrHCKM8q10WKty4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
مهدی قایدی:
۲ سال دیگر قراردادم تمام میشود، اگر آن موقع استقلال من را خواست، برمی‌گردم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/101622" target="_blank">📅 10:12 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101621">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db54c4d205.mp4?token=X6HsfJDpC6jmWss84zy3JAyrvYX3da3Np-MXwNgpz7cV90Nlh0T0YFnDR-ckIlLLcVJXeRA_40JYkX4S16sXuvVGcOC7zN4z1Zk2i8GGouW9n8xNi3tk8fS9D664_5al4bQ6GKhsiajMUhFEy2YeI9GjfwnTmTQoaGDAegPj_-p8sdsGBOO2eJ8q3MYw6-3yNpHSWj3PYWI6fYFQYRizeHTry1750AecbERdFtx6oAXdZ-OzI6Dtwl1tgJbW8gAO8t5p6WWPhMtn2QjOm8q9O9_37NVRK8dea_getDQEdc686efe-TTJKnLjiWFNHliEdRM2SZgpErp6-x1HW9o1Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db54c4d205.mp4?token=X6HsfJDpC6jmWss84zy3JAyrvYX3da3Np-MXwNgpz7cV90Nlh0T0YFnDR-ckIlLLcVJXeRA_40JYkX4S16sXuvVGcOC7zN4z1Zk2i8GGouW9n8xNi3tk8fS9D664_5al4bQ6GKhsiajMUhFEy2YeI9GjfwnTmTQoaGDAegPj_-p8sdsGBOO2eJ8q3MYw6-3yNpHSWj3PYWI6fYFQYRizeHTry1750AecbERdFtx6oAXdZ-OzI6Dtwl1tgJbW8gAO8t5p6WWPhMtn2QjOm8q9O9_37NVRK8dea_getDQEdc686efe-TTJKnLjiWFNHliEdRM2SZgpErp6-x1HW9o1Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⛔️
سیدجلال: بیرانوند رو مخ‌ترین همبازی بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/101621" target="_blank">📅 10:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101620">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PQH-fjZkBMF81qbA1HGrPpcVNUFcjjEP4ykNsu1nv1z-LzxM63ocvyDyYsE9lb_MQMbESK0nqg45NflFQ97Zg3UaWDTGgU7julRe8vIXZEbe3CYhkj6CT4fQKzxIyf9hTl-DOsP6ov23y3jgY4bTkOjqAET3CXnNDPPhEp7-AAv-2gzX47NNDnWFmSQu61jm8fA-NfY6H9jRw3VV_a8O6MebOKfwG_5eBQXstvf_4UrFwPj_8PecRH7siy2XMopax4MyLgbpAZIskTQB8UWIdXWUkH_5yMnUph0t445ojXohqoHHESKpakeAlJXZPbup2JPPPdWifyAZ2V1OxQmgeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😍
استوری رسول خادم برای عادل فردوسی‌پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/101620" target="_blank">📅 09:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101619">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46845c1eb0.mp4?token=Ap7oYCtJBH4UU6vnN6SgauaxWH1vRfa4kJsRwFQukTM3NgWwBI04ReSQdrvIy6a4a2xVEZhgtepFPgYmmEtw5C1m_siUia6zLMPbQqN0ivYubu_uFj8kU7fH0a4JY50tkYrQaFvN6Mq0JMybLwGB2Twj7jbzOdC5ZES5yi1mvjJcrgIi0_7k_L2G6B0IewS5USuTWGzhL3vi6XowxsurKqHZhvM9VCtajQZvNZqpZfvZYyJuVsxE5UfNF9ttyAdyrFOPuGPECrhSCzva5dl1_6O4r6TGeH5_eaTaPWzQ9F3dHcMBZPlPoO5NopfKzQfOCiwbNUKXUSACgU1wusBFzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46845c1eb0.mp4?token=Ap7oYCtJBH4UU6vnN6SgauaxWH1vRfa4kJsRwFQukTM3NgWwBI04ReSQdrvIy6a4a2xVEZhgtepFPgYmmEtw5C1m_siUia6zLMPbQqN0ivYubu_uFj8kU7fH0a4JY50tkYrQaFvN6Mq0JMybLwGB2Twj7jbzOdC5ZES5yi1mvjJcrgIi0_7k_L2G6B0IewS5USuTWGzhL3vi6XowxsurKqHZhvM9VCtajQZvNZqpZfvZYyJuVsxE5UfNF9ttyAdyrFOPuGPECrhSCzva5dl1_6O4r6TGeH5_eaTaPWzQ9F3dHcMBZPlPoO5NopfKzQfOCiwbNUKXUSACgU1wusBFzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
صحبت‌های جالب علی‌قلی‌زاده بازیکن تیم‌ملی درباره همسرش که فوتبالیست هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/101619" target="_blank">📅 09:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101618">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ae48d98ae.mp4?token=K2JpDOA2lBZrbSZwftbIghgJ-HufkcoN75EWhrNYavPj0WepwSH_NelUwe08YhR5jkd7r8ffpDrZjikcsjXZsrArRpmTnwO4f35r7y71ia1q8YvRwRxhtBOXQZg18zr1rRCyrdyKf3HEMYCZaWamKoUCPG9AmBr8z5V5JFUyWIJXRxrzoHmTMlIfRuUseCgyoNdKP3NrgBvHDc47uAIp58VM60U6ihJ3iPutufz2zWgTz2mjhoiBIYGdJT4VaWm6JpFdlORe_VO6ehHOk7Fkmn4whf7Qwe5nY_8Sap---ooOg5v2KChZDROZ1Lzh5dg4X_-Pdq5UkFNI-Cc1vkEO8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ae48d98ae.mp4?token=K2JpDOA2lBZrbSZwftbIghgJ-HufkcoN75EWhrNYavPj0WepwSH_NelUwe08YhR5jkd7r8ffpDrZjikcsjXZsrArRpmTnwO4f35r7y71ia1q8YvRwRxhtBOXQZg18zr1rRCyrdyKf3HEMYCZaWamKoUCPG9AmBr8z5V5JFUyWIJXRxrzoHmTMlIfRuUseCgyoNdKP3NrgBvHDc47uAIp58VM60U6ihJ3iPutufz2zWgTz2mjhoiBIYGdJT4VaWm6JpFdlORe_VO6ehHOk7Fkmn4whf7Qwe5nY_8Sap---ooOg5v2KChZDROZ1Lzh5dg4X_-Pdq5UkFNI-Cc1vkEO8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🎙
سیدجلال‌حسینی اسطوره پرسپولیس: رپر مورد علاقم تتلو هست. بعضی وقتا هم شایع!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/101618" target="_blank">📅 09:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101617">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gWcXJVoYymFVC2_69TuyWACEPII8Vn6uVEfb1UgUzGvLUg49q8qTGF2TltsImdxX6kTA8kl4kncvxgnXUv0WjghsPIBLsf1DyvyV3WsK4zJm3gr42NaD2HUIqYBaScd4wMCUHc6Fd05SQ3gArsPsy2D5sgPpxXL5HvunoVumaxhc6WtcuXAh-MY53Jj9ZgFtESvoYs0PHsI41slmOolJQdllZby0_ZpakLChLTHeviWEpu3GhEisaBe-WuY-9rt2tpsBF8669ry5RlfTWR7VtzKGCQYJLfvNUfubqYkGS7AdT5T98FpgFJxcv3YqhJPmibC2rhiJTrNrguGd7OMrIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فابریزیو رومانو
🚨
🚨
🚨
🔵
⚪️
منچستر سیتی احتمالا مبلغ زیادی رو برای انتقال رودری به رئال‌مادرید درخواست خواهد کرد. حتی اگر فلورنتینو پِرز موافقت کند، باید دید که آیا این انتقال از نظر مالی برای رئال مادرید امکان‌پذیر است یا خیر.
🔹
🔺
رودری هنوز قراردادش را با منچسترسیتی تمدید نکرده است، زیرا منتظر پیشنهادی از رئال مادرید است.
💣
💣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/Futball180TV/101617" target="_blank">📅 04:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101616">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf2512ad65.mp4?token=X0ZS4wftLfwHyUwt64DF3sFHuGCaHx5x8S_8GsWIvDeQtsvuedZbm-NBnNsehSXWEmeQtijlzAOpAh4fWePlSHGyO1xp3F-UCVibolz1JJmKM6zIEjd-4IqkTCC_U4GkLuaZRBQdIm7F4t8ZlYaQGuwxBd3xtyxdGZcNttWAYWPXzMxVsBnl_6glw8ZGdVT_26ip0xPTLCvNH-9uYBhWHWqtIvx0hMjZtFU01fQ7TAAmeKeb_XEloVZ-aReT9kvKdwPqjo_b_VvNqNVw39D4fnPpgApQgGlEfPEBDI9yiamNn3Yjz4F3QEqLsefhsaM0EgpHQS7uzocw_jVnKQsU9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf2512ad65.mp4?token=X0ZS4wftLfwHyUwt64DF3sFHuGCaHx5x8S_8GsWIvDeQtsvuedZbm-NBnNsehSXWEmeQtijlzAOpAh4fWePlSHGyO1xp3F-UCVibolz1JJmKM6zIEjd-4IqkTCC_U4GkLuaZRBQdIm7F4t8ZlYaQGuwxBd3xtyxdGZcNttWAYWPXzMxVsBnl_6glw8ZGdVT_26ip0xPTLCvNH-9uYBhWHWqtIvx0hMjZtFU01fQ7TAAmeKeb_XEloVZ-aReT9kvKdwPqjo_b_VvNqNVw39D4fnPpgApQgGlEfPEBDI9yiamNn3Yjz4F3QEqLsefhsaM0EgpHQS7uzocw_jVnKQsU9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
⚽️
خاطره مهدی قایدی: بیرانوند خیلی خسیسه. یه روز زنگ زد بستنی آوردن خوردیم و خودش رفت، گفتیم چرا حساب نمیکنی گفت فقط دعوت کردم نگفتم حساب میکنم
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/Futball180TV/101616" target="_blank">📅 02:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101615">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FSwKEauJe7VVAV3OFLU3eoFTcLpctG7DxcXR12LbqJAsLlkmnjbodZNNgIPb3u5gRvXAgWQunH7UQuHvie_4-rp68Pt1D7dJ-ycAW0vuN5jvg6m_dhVa7cGNummQ1Kx3LjVHOIpLVsUr24z1jqflQ4K0R8g4lenEWpKrPuIe-Kmb9hz9Lw2nExlhvg2QxumhpKI3DeaLcK-jw4m2TcQYANHPTKxVQWDs0bSiBjXXXjEgplV4W1WHFheOEPQR5y5_QsPmMOzSmtwqucfjBjCbTnUXSQklAzq8atQ2t5grXb4AwWJ3wBM2Qt7T0rgdDZi7xWw5E8UDMybuXPGioSpPGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
منچسترسیتی درخواست اولیه 100 میلیون یورو برای فروش رودری داشته. با توجه به مدت‌کم باقی‌مانده تا پایان قرارداد این بازیکن، رئال‌مادرید می‌تواند با رقمی کمتر ستاره اسپانیا را جذب کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/Futball180TV/101615" target="_blank">📅 01:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101614">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LhLW-2EeJHPpqTy0ufinGn0Rr92AnyWmuvmuOjRg27r1Y6BAl5QQQ5QhZRqSxAosyW8ikvqJl2-kz6IeY3-l6y29ikS1bs3r3kSM76ffdRwHz0l4L9OL367DdjgTpBziSiFjHymlhRovClXrqfIM6dTntvoT9XTY_uxVnsMDiz9Q8mzB9L9zt5oKKN49O0SQdhIoR0Lp0RlwANgMsrBC07TE_qZ9y2E-8nt3FVFev-cV5_rZ8P3FixTkhpeX6gJaqm5D_AAvVKFXdVW20FAYbhlvBWCyDGA2NfYqH3glqUesubRibU0l5BAt7EOWXlF9CWl3dZgIplWclHk0fm-I4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
منچسترسیتی درخواست اولیه 100 میلیون یورو برای فروش رودری داشته. با توجه به مدت‌کم باقی‌مانده تا پایان قرارداد این بازیکن، رئال‌مادرید می‌تواند با رقمی کمتر ستاره اسپانیا را جذب کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/Futball180TV/101614" target="_blank">📅 01:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101613">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oS3OW-NCGLCThaHpUUtdLsMZGe_J0qptvR3cvwifJs_8hza6mZtnhXWkhU8ZBSHR6WvCx0hUexs1pH9-WmOrXNf13666mg30W55Um0lXPpJePsGNnWsnfVnZrFDyLueQ5QrLFm7R7JU0RNR8s-6o-Ykkl-YrmjGOXP0yhL0WMa4JpocLOrRiq-Spf3hMxtOoAReaytpR2E-JMPgFEcFZu2Jt6c4BivKl57erlEOnxBiDqKM0HaHN93qNc-RkX3QXW7Lzd20_sr7IYMX2jSR-mucCO3NZlozPUh3ShaLft_0H-VyBGSMdH9uWwmU5bwbkZZlxc-QOsCg-M3XIbuCDLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیوید بکهام از تبلیغات تو جام جهانی 22 میلیون دلار درامد داشت و شکیرا 17.5 میلیون دلار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/Futball180TV/101613" target="_blank">📅 01:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101612">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cY_diyewSJO8BBF5qqTjK6NzRgS1UZQCeQmwfy90dqA3AWSVbrywp2YZhALMK73L_en2VqzwvOFiCARa_O2AxCdJTO1iZy0F-QC67Jn-7zaj7GDy6xjHPL2RTsAeZzhM1w1XLcP6BQAqwv89mi7uXQ4VfHjxv1FTPknrsMYbDPOrzNMXWfjBQePevz2xIU2MK6mom98K4xn7wZmrIi2pZm55SJtFLskoq4z48j4Htn-llbgtE29-wUWfnJrTRYNyWN4DIpSyiE4NvbJbq6NNP4bt0FoVF2L8VI8QNCKmU5Pkifrb-8tZUwl9v5LmV1dMa76vSD_SoHuDapHrJRzg5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط 3 بازیکن فعال حال حاضر فوتبال این افتخارات رو دارن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/101612" target="_blank">📅 01:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101611">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vRpS7rGyy9FFFlGeVFcVt4pD6GO8DgNBHvEu5KZmgljKrtvxfKr_v3o9XXcMr9dUqJBm_8BYNraPm3KiIvlhtAm099097vvpzMPVT8h74DU65DQT8v8AOHEVivA5bCxmueiq-pW2QK7w5Z7sVuHN4RzVNjqq17QrFUcVNnOW5pYJqLvK4gaaTVDFvTV3if8SeJ_TLwdR_6Y8awJFCXv9qVVbiANdvtUhfzuCpsTwVMl9zGY4rMXcaPB9HQL9MzU1fY3XxenzCKvct9rh3XiTjuDdg3yNe73WsZdZPUi9bDQDNeVm7lbh_29A0CmW3n3egKigoQPyCMZYwhdcfcYH9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/101611" target="_blank">📅 01:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101610">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hnmSGeLEadc3hNnFZ6bIv-O0EUbZ_nYfUCjDC8627tX6xn7CmyVoTDMKjJNnuEVsjQPZXzP4nDeSvipaJ9XvIRoTVGABv7-70tqwSaPASOC9l8gJ0qswjwy6OgVTrN931P-Lmw_x0T__yfVmtTOco5qxTQ8itoCLtUVGw2swjPVZkB0aZ9f6Bu_kYgg3-nUG_yK8jryR_7flOanaRrRpvPHpqDe8gONFXvjpIf_uII7tCGmu1QY17QB5y273BOP3qYaTQvhniRnKmwOq3fLi1_GDvVXIB5ZMh6fBi3LFpzQk55LfPIPnJK_DwkLBmE5nW9Dpzs1MkRuiqZy844WWag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
کیت‌لورفته جدید رئال‌مادرید که قراره فردا رسما رونمایی بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/101610" target="_blank">📅 01:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101609">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
⚪️
فووووری از پپه آلوارز: رودری با قراردادی 4 ساله به رئال مادرید پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/101609" target="_blank">📅 00:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101608">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pzBF0rhVbIsm4AlUoZtx7KeojSmTh9VPv3_KSmLpOJrfMl4CfQZ6h_0DtrMresEgSDJHCMntyv5H6psfkjq1IWJVsg_Nqtm6o2nLPAHCX9SCzb2Sep--8lmZWBVD9tkfLM4vLm3WFIPlcWGW2c2xR5BrlNYfD8ewM9_nnzHmrv3ZGV6upurFq19c8IpsTroGfPKsIv8nNL-_4urYhyi8YSYlqzWMvnknuB-UI7xcZisLIWR8WcKabs3H4yIThZTfZCLBEouMuF00Ny58IMfZCcq6d8xRMpzjXc4ll4vp2VzKa8Rnr-nDHAMzLlg0rNeacVCB0L_Vl7nYdQtpUwgSVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
والنتین بارکو با قراردادی به چلسی پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/Futball180TV/101608" target="_blank">📅 00:45 · 01 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
