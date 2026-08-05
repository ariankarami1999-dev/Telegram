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
<img src="https://cdn4.telesco.pe/file/l3XCj1zHx-5TpoF9_7laM280Vc6kMFgBWVeioevFRmucSq9GhVQYLlM07zdyy_mTyNm__sD7Z3FnAYfAoiqKC7_tl_zTtC66OhnEjqrCBrdjznwnM8P18cdbShcQD_Oh8jMyluDA5VZ9ni42Q_L6iiX98glykT7grMi_122j0gf1091yZ7dLugp9AIij2H4QUk3lPZ7vjsjd-ZFgXM5eOFkm5kX73KNMKZa_cy2IwQ_LUqBBRgDhVCSkluraZVxgx6TDAh-n10dXWJY43XrlpyTovppLHKZ5y72aHKVMAE9yEHKPqN352nMG8b2Oznj6bHAWBIt0cnFWk2-Beb0D6g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 64.8K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-14 15:51:59</div>
<hr>

<div class="tg-post" id="msg-6501">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2a5730f1c.mp4?token=cY-kW-aEjtnJCHLGEGC_Uhshm-KrI9-iqPl-1qJ-zG2Q8xno2-T4s6Rg0gBHB6pwcZDXCYIO3q650D66Z1VMzAOZDO7bjT1reSwtLe5G7d3NGPNwM2cLdySoYOkx_s_mZbB0jst9cbIJ0v8PKJDkfC8JtRnosGYHafI8Wr0tIYfxvwbDAli3aZD5hz2TZOcHBw4BmGmSg5qzZd4balUOzcdpDcDL8qCylzvi0Jvp58amATRUtDzJBAGCvDpSVvi7npL1ANtXZ9441_C_W4iLUSVJUx-017yM0ltSwT5dAK09SuJkmDxw2WDg3U36FTH-bKvwwtaGp_Sm5cIyw19tSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2a5730f1c.mp4?token=cY-kW-aEjtnJCHLGEGC_Uhshm-KrI9-iqPl-1qJ-zG2Q8xno2-T4s6Rg0gBHB6pwcZDXCYIO3q650D66Z1VMzAOZDO7bjT1reSwtLe5G7d3NGPNwM2cLdySoYOkx_s_mZbB0jst9cbIJ0v8PKJDkfC8JtRnosGYHafI8Wr0tIYfxvwbDAli3aZD5hz2TZOcHBw4BmGmSg5qzZd4balUOzcdpDcDL8qCylzvi0Jvp58amATRUtDzJBAGCvDpSVvi7npL1ANtXZ9441_C_W4iLUSVJUx-017yM0ltSwT5dAK09SuJkmDxw2WDg3U36FTH-bKvwwtaGp_Sm5cIyw19tSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی منطقی بود!</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farahmand_alipour/6501" target="_blank">📅 12:11 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6500">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5ac92640d.mp4?token=gBkgMzN09B9NddrsWUchv2DCOfnd-eceDTqM4N0sAomLp9sE7Qz6MUymHrFMM5dp7l9LlsdKYzVUfrtB_luSqmdIImrB05SjawA61rirNG53iUytPQjocp3mgWqjkpl-lXLayMhL90CywBAzWN74esxfFI-fFkCRzorp_DP8ruYSjFPVXdIhS-Szv3mYAgI3OljinlvwbXcliif6EeYF0IWB0mPhvIZjGTlDaLYmheQCsVLJygiJ3RuAVKenZPC6TDNOjzsUAuWdsgWNHyxA5uufjgg0lfUt_Ey8ng3ksMV40wuPhpaY1Bv0HyVfHP8_5ZylbwA84BQeBY_K28uV7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5ac92640d.mp4?token=gBkgMzN09B9NddrsWUchv2DCOfnd-eceDTqM4N0sAomLp9sE7Qz6MUymHrFMM5dp7l9LlsdKYzVUfrtB_luSqmdIImrB05SjawA61rirNG53iUytPQjocp3mgWqjkpl-lXLayMhL90CywBAzWN74esxfFI-fFkCRzorp_DP8ruYSjFPVXdIhS-Szv3mYAgI3OljinlvwbXcliif6EeYF0IWB0mPhvIZjGTlDaLYmheQCsVLJygiJ3RuAVKenZPC6TDNOjzsUAuWdsgWNHyxA5uufjgg0lfUt_Ey8ng3ksMV40wuPhpaY1Bv0HyVfHP8_5ZylbwA84BQeBY_K28uV7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عمان مخالف اینه که از کشتی‌های  عبوری عوارضی گرفته بشه،  جمهوری اسلامی چند هفته است عمان رو گذاشته زیر فشار که باید بیایی با هم این کار رو انجام بدیم!  عمان گفت : تو توی بخش خودت اعمال کن!  در آب‌های سرزمینی من، رایگان خواهد بود!  که خب جمهوری اسلامی فهمید…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6500" target="_blank">📅 18:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6499">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TZ_sdZL2628-noW0FD2mYU48mgldBc2IS37VcvyEac1ZcqmTLzL7-7vDbc71QfTWq2LFnva_relaLABuYiHkU6WR7fpl8rOqw0x4ff9KT2H79K56KQ4VWGBvTUsw8GzVUf1KelDFSyfN8ZN3hHla6IJVLHfddl6CvScYf5gOMHx7s_wk6Rwvk-Nc1Sjj1826qSD4rr7A-nJL9jwP0e740HPFaoZO0jfmXHL7DTY7RTiYmjPdAjy3WkR0JrefxM6MJOLZlIL6zgWtw7bX7vUytOtu8eLokyDJyCXxbFR8wfcwOWpn-WuocBBrh7q81KkElOpVOaaj94jXYwrN2PZkiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کار انتقال گاز از ترکمنستان به پاکستان  و هند که چند سالی متوقف شده بود،  دوباره با شدت شروع شد.  کار انتقال گاز ترکمنستان از طریق دریای خزر به آذربایجان و ارسال به اروپا در دستور اقدام قرار گرفته.  قزاقستان هم در حال احداث یک خط لوله انتقال نفت مستقیم به…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6499" target="_blank">📅 17:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6498">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q0Zbkwfj_VVRNft6m2I5vtNvWV_JfD1Rp77agvSiugy4LvHYH3fat9MP4bptUCdTYZqchjvslc4vMcXUwNjbiOxfcsT63JVZAkvC5Vrk1zR4c5EW47qEL9EXOx-5Sh3m65xCUqKmgRK6co8huTimliggOo5r9FyNV9midpHdn_dHc0HXSiWy5OTwMNwFX6kBL1G71_l6QlWjil_oMRCnaLhMx7Ba0PviCcuEEIf9uB5BsLF3Do_mlFlFAApHHkaJppQ5RrZ3YSi_LCL8n72I15uM8QpXtOBA0BrGBfTzalXSWrLHPBTJ-DxAt4qw_CvEUXM_hmhVpZ9oaFIbIWV0vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه‌های بزرگی که کشورهای عربی برای دور زدن همیشگی تنگه هرمز در دست احداث دارند.  عراق : از طریق خط لوله انتقال نفت به ترکیه  کویت : خط لوله به عراق و ترکیه و همچنین به عربستان بحرین : از طریق خاک عربستان و‌دریای سرخ   عربستان : صادرات از طریق سواحلش در…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6498" target="_blank">📅 17:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6497">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_j_GRhHWokd2FQULc5nH1CzR2-LNk3NtfjVXNQZZvGLK6RRZ1Mvjfe55GB0sazqmwlL_qI8GRGiqg0GtJhuh-Z7Lc9jhorwe_15xJeo5Gg9hRzRaf-MsyCqcWt8q7DEX5BvHQFUyVNWXHdEM8hVwziJGZ8KGa2BKhFuukaYqbNH3SKMsci0WzS40fq2LlzaVc7PYQ5TK4OOppq0ly84GYqm3aGfW8gjl6zP8qYIa8PU2-pdj8oZ1RsYplw2-8-vM_1NRRVd94gvo9u_6M-4GoFjiRDwAdBLcxYQ7ZjNdzcEDSDGQF3fCS3ERhqv8WQvwgU9srXOYRe5vRS5PYKMBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه‌های بزرگی که کشورهای عربی برای دور زدن همیشگی تنگه هرمز در دست احداث دارند.
عراق : از طریق خط لوله انتقال نفت به ترکیه
کویت : خط لوله به عراق و ترکیه و همچنین به عربستان
بحرین : از طریق خاک عربستان و‌دریای سرخ
عربستان : صادرات از طریق سواحلش در دریای سرخ
(همین الان هم ۷۰٪ صادرات عربستان از دریای سرخه)
امارات : دور زدن تنگه و صادرات از  خلیج عمان)</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6497" target="_blank">📅 17:38 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6496">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
امارات ورود هرگونه کشتی و لنج ایرانی به سواحل این کشور را ممنوع اعلام کرد و خواستار خروج فوری کشتی‌های ایرانی از سواحل این کشور شد.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6496" target="_blank">📅 15:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6495">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce8527f3a7.mp4?token=QmegI3wJRHE6Z68AKejtYXjTqDwhC2CP9umqFi0zdFI28dDpMNZQgG6QXqfIOkFE5UiV4bj2L6VZqKtbGFa5DSkBbGxULTeN7hq5Wiu2ZfMShT0kB0Msr6p_3ZRbdV1_CG3Zlz1Ty-_PshJ4K8BbdXCYU1GlWG1iL481MaQ7qQ7O4ceomIEKMWafb1YB-6aiEyRcgZ55kkWTDI_YMPZO_uqXXT5-IfSwvA3xkxBKkTnk_zQfCZ0R_VUh-eRliSWTwGcOCzk7oxV6DQO7vmzL8CT-DYj5I8dnVNsQGF9ODxYqVc-RZc9Ybv4DNO_dHwoG_JfWCqO-TkZN7Jz1uruGaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce8527f3a7.mp4?token=QmegI3wJRHE6Z68AKejtYXjTqDwhC2CP9umqFi0zdFI28dDpMNZQgG6QXqfIOkFE5UiV4bj2L6VZqKtbGFa5DSkBbGxULTeN7hq5Wiu2ZfMShT0kB0Msr6p_3ZRbdV1_CG3Zlz1Ty-_PshJ4K8BbdXCYU1GlWG1iL481MaQ7qQ7O4ceomIEKMWafb1YB-6aiEyRcgZ55kkWTDI_YMPZO_uqXXT5-IfSwvA3xkxBKkTnk_zQfCZ0R_VUh-eRliSWTwGcOCzk7oxV6DQO7vmzL8CT-DYj5I8dnVNsQGF9ODxYqVc-RZc9Ybv4DNO_dHwoG_JfWCqO-TkZN7Jz1uruGaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان:
اگر استعفا بدهم، رسماً اعلام می‌کنم؛ استعفا نخواهم داد و خواهم ایستاد
ما با نیروهای نظامی، کاملاً هماهنگ هستیم. می‌خواهند اختلاف درست کنند که رهبری یک چیزی می‌گوید و این‌ها یک چیز دیگر
همه مردم برای ایران سختی‌ها را تحمل می‌کنند!
[تحمل نکنند هم یا زندان یا کشته میشن]
یک عدد سه هزار نفری را سی چهل هزار نفر گفتن، نشان می‌دهد که این‌ها چقدر نامرد و وطن‌فروش هستند.»
اونهایی که به قول خودش بین ۳ هزار نفر رو کشتن، نامرد و وطن فروش نیستن، کسانی که به کشتار و ظلم معترض هستند، نامردن!!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6495" target="_blank">📅 12:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6494">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-text">جزئیات تازه از طرح تغییر رژیم ایران؛ قرار بود کردها «زیر پرچم شیروخورشید پیشروی کنند»
🔸
یک روزنامه‌نگار سرشناس اسرائیلی در گزارشی تازه نوشته که هدف حقیقی این کشور از جنگ ۴۰روزه با جمهوری اسلامی ایران، تغییر رژیم در تهران بود نه صرفاً نابودی برنامه هسته‌ای و موشکی‌اش.
🔸
نداو ایال مدعی است که ساقط کردن جمهوری اسلامی در حالی به‌عنوان هدف اصلی تعیین شده بود که نقشه راه حقیقی برای عملی کردن آن ترسیم نشده بود؛ تناسب این هدف با امکاناتی که اسرائیل در اختیار داشت به‌طور عمیق بررسی نشد، دولت بنیامین نتانیاهو هشدارهای ارتش این کشور در مورد مخاطرات این طرح را نادیده گرفت و به عواقب آن، مانند آسیب به جایگاه اسرائیل نزد آمریکا، فکر نکرده بود.
🔸
این روزنامه‌نگار در گزارشی که روز ۹ مرداد در مجلهٔ ضمیمه آخر هفتهٔ روزنامهٔ «یدیعوت آحرونوت» منتشر شد، جزئیاتی را از مباحثات کابینهٔ اسرائیل و اختلاف‌نظرها در میان مقامات ارشد سیاسی، اطلاعاتی و نظامی این کشور پیش و پس از جنگ‌های اخیر اسرائیل با ایران ارائه داده که خود آن را «اطلاعات تازه» خوانده است.
🔸
گزارش «رؤیاهای بزرگ؛ افشاگری‌های تازه دربارهٔ طرح تغییر رژیم ایران»، نتیجهٔ «یک تحقیق جامع» نداو ایال بر اساس گفت‌وگوهایش با ده منبع نظامی و سیاسی اسرائیل بوده است.
🔸
این روزنامه‌نگار مدعی است که تلاش او تصویری دقیق‌تر از پشت‌پرده‌ها در بالاترین سطوح امنیتی و سیاسی اسرائیل ترسیم می‌کند؛ فراتر از ادعاهای پیشین که دو روزنامهٔ «نیویورک‌تایمز» و «هاآرتص» در ماه‌های گذشته در خصوص تلاش دولت اسرائیل برای تغییر رژیم در ایران و جلب همکاری محمود احمدی‌نژاد، رئیس‌جمهور پیشین، به‌عنوان یک گزینهٔ رهبری منتشر کرده بودند و به‌شدت بحث‌برانگیز شد.
🔸
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، از بین بردن برنامهٔ هسته‌ای و مهار توان موشکی ایران را هدف‌های اول و دوم جنگ ۴۰ روزه اعلام کرده بود.
🔸
نتانیاهو اما از آغاز کار پنهان نکرد که هدف سوم جنگ هم فراهم کردن شرایطی برای مردم ایران است که بتوانند کار حکومت جمهوری اسلامی را یکسره کرده و اسرائیل نیز از وجود چنین رژیمی که نابودی این کشور را عملاً دنبال کرده و با تشکیل گروه‌های نیابتی در محور موسوم به «مقاومت» در اطراف اسرائیل «حلقه آتش» به پا کرده، رهایی یابد.
🔸
نداو ایال گزارش خود را حول این ادعا نوشته که «تغییر رژیم ایران» هدف واقعی جنگ بود، نه یک خواسته فرعی یا شعاری تبلیغاتی.
🔸
به نوشتهٔ او، چنین هدفی قرار بود بر اختلاف‌نظرها دربارهٔ ماهیت نهایی جنگ با ایران در میان مقام‌های اسرائیلی نقطه پایان بگذارد، در حالی که برخی از مقامات و نهادها همچنان خواهان محدود کردن جنگ به اهداف مشخص و معین نظامی بودند.
🔸
نسخه کامل این گزارش را در
وب‌سایت رادیوفردا
بخوانید.
@RadioFarda</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6494" target="_blank">📅 09:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6493">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d5918459d.mp4?token=r7X-3-vboGHzU6442C7jbjplfboxRFRc_Qqdh1stWFaqGtuDoDT7yD5anUiq7US2o1CKcnQteTTyzYziZKuTSdWI3oGrORjJ13-RGGophaXcwj-p39FTSrus0n3Q7KbbJ49yC5fEIRAk_GQ5s8JfAuKush2TcPFGqNqerbKhjiXZgrCr5tEdJnpvH0dwMdSLkonyqx3AB8yQToQsFWXKb0f69CvMOO18V3ko-dN0g9w2t93I3RNTJJ6807pnVVLLx7faB08AYReVByhpyzuGcl1hBNrn_snYuTuddwYpaV4lTnXmoWn7bg1-LzfiZqPYwTIIzgTyvxsWF_o69S_lUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d5918459d.mp4?token=r7X-3-vboGHzU6442C7jbjplfboxRFRc_Qqdh1stWFaqGtuDoDT7yD5anUiq7US2o1CKcnQteTTyzYziZKuTSdWI3oGrORjJ13-RGGophaXcwj-p39FTSrus0n3Q7KbbJ49yC5fEIRAk_GQ5s8JfAuKush2TcPFGqNqerbKhjiXZgrCr5tEdJnpvH0dwMdSLkonyqx3AB8yQToQsFWXKb0f69CvMOO18V3ko-dN0g9w2t93I3RNTJJ6807pnVVLLx7faB08AYReVByhpyzuGcl1hBNrn_snYuTuddwYpaV4lTnXmoWn7bg1-LzfiZqPYwTIIzgTyvxsWF_o69S_lUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد باقر خرازی ، برادر همسر مسعود خامنه‌ای :
پزشکیان ۲۸ بار استعفا داده
و دیگه «کاسه کوزه‌اش رو جمع کرد»</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6493" target="_blank">📅 00:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6492">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a204c96911.mp4?token=VkgOXo0uZkLAuw4qfxLPRvmdELrQTHzPUGgIxXBWN0WE5UtozNSrJ78M74CPtWHfCPkBV1oBTYnW_lZK6DRHqLxEl156xOnaQhMcxDPx50DTBPI0XzT5S_r2EqTii40kBZU7syiU7yhkTRD-wQMVkLPtGqEkRaN63lTN8ZWp8eWjEPDBuds6rxaDBIk2aRvYD7bL6H6DzeDcwU3BheWGKVPPYW4Pvs0ES0rmtjOVBApbqeIQfrVHxUeghFYJIwCA-wv-onBpZ_MiM_yKXA3BzfmLv3gpoDrVugTsZgivBYz1s37KOPIL0VGRAmSRk70EQSRRmnocLMM77CufeTKznw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a204c96911.mp4?token=VkgOXo0uZkLAuw4qfxLPRvmdELrQTHzPUGgIxXBWN0WE5UtozNSrJ78M74CPtWHfCPkBV1oBTYnW_lZK6DRHqLxEl156xOnaQhMcxDPx50DTBPI0XzT5S_r2EqTii40kBZU7syiU7yhkTRD-wQMVkLPtGqEkRaN63lTN8ZWp8eWjEPDBuds6rxaDBIk2aRvYD7bL6H6DzeDcwU3BheWGKVPPYW4Pvs0ES0rmtjOVBApbqeIQfrVHxUeghFYJIwCA-wv-onBpZ_MiM_yKXA3BzfmLv3gpoDrVugTsZgivBYz1s37KOPIL0VGRAmSRk70EQSRRmnocLMM77CufeTKznw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«تبعیت از ولی‌فقیه بر مسئولان واجب است»
می‌دو‌نید شمر تا آخر عمرش
از اینکه در کربلا شرکت کرده بود
هیچ گونه پشیمانی نداشت!
شمر خودش از فرماندهان ارشد امام علی بود!
توی روایات اسلامی هم هست که
هر بار بحثی پیش می‌اومد دفاع می‌کرد از کارش! میگفت  تبعیت از حاکم اسلامی بر من واجبه !</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6492" target="_blank">📅 17:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6491">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30ad02e26e.mp4?token=lK6y3k7hlCU0wfaWTyVpV1jiHKCpel-FG7JDNzFW-dIimq4o3-BV4eYJnXpWTRSLgKQyf1kOypQuPGwf2m3lN-wJCi7cBR-wrH_KBin7d4CXthn_iLQxF5rt8goAPtLPSDZpgrom8r1u9OPXBvcnK6Tmr6qYR16afW0f2TREIRSOPJCDsTaQ3MUXo8W--HyOtV0GTD0EEDANlDZqgaqBZpshTrVn-v4iiliZ93z7eHE5j95k_-6jQkYqxdYp6MHd6Je0Ec40BrkxduFfz_OK66Y3BU7kcSOjIVCHhLiA_xofErl6r0yGHqpmbxrxSj12MciWQPOyQstrt7hso5OzjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30ad02e26e.mp4?token=lK6y3k7hlCU0wfaWTyVpV1jiHKCpel-FG7JDNzFW-dIimq4o3-BV4eYJnXpWTRSLgKQyf1kOypQuPGwf2m3lN-wJCi7cBR-wrH_KBin7d4CXthn_iLQxF5rt8goAPtLPSDZpgrom8r1u9OPXBvcnK6Tmr6qYR16afW0f2TREIRSOPJCDsTaQ3MUXo8W--HyOtV0GTD0EEDANlDZqgaqBZpshTrVn-v4iiliZ93z7eHE5j95k_-6jQkYqxdYp6MHd6Je0Ec40BrkxduFfz_OK66Y3BU7kcSOjIVCHhLiA_xofErl6r0yGHqpmbxrxSj12MciWQPOyQstrt7hso5OzjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استقبال گرم نیروهای نظامی مراکشی، از مراکشی‌هایی که از خاک اسپانیا (سئوتا) بیرون انداخته شدن :)</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6491" target="_blank">📅 23:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6490">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KuTDziwN04fXK41NIBTUchPlO5gYpc2KrMTUDwD9SuObJlTcCAbiwPqHY5j5Tc37CCw4MqgfEyaPgKJ-y-bvXAG40KcadQQle6KDry1fBbtFftUj0oIPt2DCq001MsVJbbEvIY1UthJqjCuEttvmRS9uV6JlrDg-fH7PKHyz2QmqqCwuaBiNkA25ZrPgiES-DX_9wRpsHEV_m9hTCPq197GzzvLNiQ_OQxsZblzmFR7Uh6r1mjr-z7O6uY3-bLWauq8__Rkq4FnPJ5GBnbeMqrC19kX6Cb4HyRdDYLjM-Suf2zdNHGjn02XI0ZfyEHZtWGKtsD2sTWrIvE6OJq5bcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرگ نخست زادگان مصر اثر نقاش بریتانیایی «لاورنس آلما تادما» در ۱۸۷۲ تمرکزش به تصویر کشیدن  اندوه یک پدر است.  نقاش عامدانه موسی را مرکزیت نقاشی، آنگونه که سنت نقاشان بود، کنار زده،  و برخلاف نقاشانی که به خاطر آموزه‌های مذهبی،  روایتی یکسویه را ترویج می‌کنند،…</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6490" target="_blank">📅 16:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6489">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebLmprlv5B29-ycbENvbpkaPG3Wy5RTVgBVw6zIKGeGOq5VMbsa0rybXDqbuAz17D3gphJq-iz3-wDCbjIGq9pr0om0C-T_6IJhpwhFgGOJTXXitbWzZvWnMzD6RegLLwYNHKnebt5dBSgB_BgcAjQg8rRCnUkc-tcbGmhYS8noqpLUR8-be1Jo4idENs5P7_ebtqx7VzLR4aJRQXqkyqfl2R5vfTY3wIOefgtwqL-Tkn1jCYs0QSECMzCFGCXHRkbyWM2L85T1qz1sHzfi8TYWXOCBjZqnaum18pWFg39CBF0mdjBk6bW8Fd8DpTgtsvDQZqGJ82ffEr0oj5AFAmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6489" target="_blank">📅 16:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6487">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KvtSvsV1bcM7QDFgdQMfXNB90H8Uw2AIoDqxs-2vOLWIh2-Mn54CpzsfOpp9bMHORlPY9EwN0TcByvoZC7M7yIp07kS37by5HpraL7YV5ifPUeTkVGSJEbZAmSIjbMeXWnBCkI0GHp2Y2OCZNfUOGZAd77Dtbd3P-dJzAUI9C-zMbwgaAJDs63HtrrKnAxfzvTAJIki4pH4kZ75CRx5pULvXrJuMJyR1aZLcBCwqKPB4xvI-bWZw8RSo2q2YuSvieJF6PS5ilZuTUOOmFlh_RJ4ZUoo34EjNkiRDBg8hMBJzBXtSMdyujdLP3m7vu8x2s-gkWE5u4I1dfHfXUqYEqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ecwIk7MdzeiOmAtI3huYKz8IBgEYx1uQrgOMebq433RwZpR89mvbqNk4SDCjP4dIJkFKg6YbT6QsdwxIKLnWYwdRrqWkfqCxw_wHrK1YGMraPfZtbNGnBMlgXqR2q3mMAsAUjgsJhpzoiqiSNAa05EbO5bl8ursccFNj0K6i_JOenLAL4ZBs9FXiIOvtSDJR2hUIWe7fTrYIJ9gtZVzc0LQX7yIPoU8jgWA13FljTCXe-GsakB4X1br6ccXijxUWd7yOaFlnB_k3ZAFT0_fRq0pmjtR-w5NeMkF10l2XU3HiznS3-5z9FnqaUeqtM5EEcauQmF4ZbJUEaFTo8aXarA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هدف فقط رهایی قوم بنی‌اسرائیل  امر مصر بود و اسکان آنها در «سرزمین مقدس»،  سرزمینی که قرآن میگه :« کتب الله لکم»! «برایتان خدا مقرر کرده!» ثبت کرده! سند زده!   آیه ۲۱ سوره مائده  موسی خطاب به قوم بنی‌‌اسرائیل میگه :  «ای قوم! وارد سرزمین مقدس (کنعان - فلسطین)…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6487" target="_blank">📅 16:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6486">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dBrGm3N2XO7Vu0qxqnqhWzs26GL-wBz0sXgSCSg0TkL3PZaKh2VZ3iZRTGbtiNSd3CbSs_xJkF1Piq9VDQlmenJtxrKuxTVR82WlrS2FN_-Px9JAZ5XEebErwDvI-CbnXuENC7Vyo16jGsaNkciRnkEm2iM9YMwVOReY1T63ejfv3LSps6FcHT922ijr1cvS_csm_lwubSD_dagWiMArDZv52fZilKNIw69TPGU8InnY5wzF4UiavAnwtDSfmijllKFUQu5WM3iGniBDqbwx6MxsQCsaeGf8R1y-YlXh4V98ord3QT2-Pl_t_kb6SBHYsoKXyqAEMQgdEEcRSKM7gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همونطور که اشاره کردم، هیچ جای قرآن حتی  اشاره نشده که موسی رفته تا مردم مصر  رو از ظلم فرعون آزاد کنه!  هیچ جا اشاره نشده که رفته تا دین مردم رو عوض کنه و دین خدا رو تبلیغ کنه!  نه در قرآن و ته در تورات!  اتفاقا نه تنها مردم مصر، براش مسئله‌ای نبود  که در…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6486" target="_blank">📅 16:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6485">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O4enV613tviTkG1rNbjW-QfEtzvRpR0pgJoXqX_IVFEyP8R5T_D6tz8h0kvsMCb2JNvCXf2gm6ocdUDG5dnRnpQ4_kwByLFaSu-wTHIVkOR5Ge5Q2wC9ouSqiIKVjXJBMQOH2ThE8-SGY5pQdcHGYgyhNTZnCBdyCLGs3bhv3TEQD446ANYlg6wM5lXawBb3NKwn3gAyldxcuknQ4DhLEKjWdQb2IMdFM1xXV8pdhs_mMb-_EzTf-1YqC6AqW43K16amu2i1kfWQGgH3CtrnQpU5J_hUpoCRPn0XapqoSzyyuMQGqV_7OCWZdpjXSRhvArbQdh9xK69nKF6_9Ovnrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشتن همه نخست زادگان مصر در یک نیمه شب،  تنها مجازات عمومی خدا،  در برابر سرسختی فرعون نبود!  قبلش آب رود نیل را تبدیل به خون کرد تا کسی نتواند آب بنوشید،  نه انسان، نه گیاه و نه حیوان!  قبل تر از آن آفتی فرستاد تا همه مزارع مصری‌ها از بین برود و قحطی و گرسنگی…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6485" target="_blank">📅 16:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6484">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJyQnPgj7vOfE0EK7pBKZ0i8qFsUQYIq8ZDe5gRbvfAhV5NJZEIGn2K0TIAVHFSmnZDT0i7tRFiJagXuPDEuqWqJX8cJmbEZuJgQDT3L8VWzfForkcKBVluElTCjbAxe8EYblzqiuqjt3CEmpFTbY1DTQ-d4qoTDF_HsAOxwKahfdZhZ3L2pAoMlv3INrvgMumFPTitqoORW6NE3xIdtnG2Reu-EbBn4axidBYhpu-L_vjEP5ZaMNrRXNcQI8-PgxkUuR9kKdyhNowbnO8rWmpWuaeTbuW_vySC0ly3BsVrYtpoIxLtebTGxm0jDzV539Bhw_WKKDpCGFz2ia4mWrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا، موسی و برادرش هارون رو فرستاده بود پیش فرعون برای آزادی قوم برگزیده‌اش، «بنی‌اسرائیل»!  فقط برای همین منظور! موسی نه رفته بود مردم مصر را دعوت به دین خدا کند و ایمان آنها را تغییر دهد، نه ماموریتی داشت که علیه دین مصری‌ها حرفی بزند!  هیچ جای قرآن هم نیومده!…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6484" target="_blank">📅 16:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6483">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RaMaNHjlqIfd47pwWe__gqzAwv3Wa12nVmhYzynG3e4wQcAKihShk0a0AglYarpbeSZxuXyUZyjK5O5TxazKySkUlOizCKywpdVqyLMi3OAOT-3ECWch0TGOdWQT-Pcw0tbKo33B_GcvNp7m_h1xCYGe0fpiP49q6Gzz19WlAEf7ajwneepuzShTLVSwc7vTYjykd4hxxuU-UwoSUciSWBNUl1gBWRQ0nFAYPU1K1lwe3BIyL00Z_WMXPAnvLkzabHtgBBmyxVTYxqfY_0EhnuL8CjO8RY00473NUWSAGWsSYxoL3Ho8ni8z08lUOxyyEy40lX1ZTTdGQtd2_x1fKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و همان نیمه شب …..  فرعون به هارون و به موسی گفت :  «برخیزید و از میان قوم من بیرون روید،  هم شما و هم بنی‌اسرائیل!»  ایرانیان زرتشتی، وقتی داستان‌های  کتاب‌های ادیان ابراهیمی را می‌خواندند،   دائم دچار شوک می‌شدند! و حیران می‌گفت : خدای ادیان ابراهیمی،  عجب…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6483" target="_blank">📅 15:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6482">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">فرعون، جسد نخست زاده خود  را در دست دارد، زن فرعون گریه می‌کند و موسی و هارون،  در گوشه‌ای از تصویر دیده می‌شوند.  برای مجازات فرعون، پسر او، و نخست زادگان «همه مصری‌ها»،  «حتی آن زن کنیزی که پشت سنگ آسیاب نشسته بود، حتی نخست زاده آن کس  که در زندان بود.»…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6482" target="_blank">📅 15:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6481">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pN7j_zfTlvob6kplPUB8pP_r5UaXqwsXdKf8hKLLqD-nGvJj1pWZmgGxzRHvbHtZwPbVmnzOFz6ncXAd0M-HSwC2tjv-uZkxYpnPnnXjuDcq7Cck36fjcbtuG1J5N5jrr3JvrZfTVr3AyD1iBZ48-A6nRbrlqysrCliwX8tT9_KgsHuGZ6byJ68kwmtccYu4GgWzevvMbJzPqNZobn7AqoYbSD76QIcyo2Dmh8SVojm5lw6U3pfLFTnmTtSwY5flR99CgJUMeE5DexqPvWrZw904GQ-W-_tI4-cJcndM0KQFmxS7iuc6Xz60OZhnOyRZNYhgvbxiBOYgvqvYezOoPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرعون، جسد نخست زاده خود
را در دست دارد، زن فرعون گریه می‌کند
و موسی و هارون،
در گوشه‌ای از تصویر دیده می‌شوند.
برای مجازات فرعون، پسر او،
و نخست زادگان «همه مصری‌ها»،
«حتی آن زن کنیزی که پشت سنگ آسیاب نشسته بود، حتی نخست زاده آن کس
که در زندان بود.» همگی کشته شدند!
حتی! حتی نخست زادگان گاو و گوسفندهای مردم مصر!
و این تصمیم و اراده خدا بود!</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6481" target="_blank">📅 15:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6480">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p1uLyL37YJNAonV8Rnq6uicdN6aJqbIgKktNt6djv5LwraWfLRFqf7Hbaa8KwjryQ_HPi1Q2D4SMM4YR5j8uC0Eva01rAFV751cuZuuKq-H-9iwyRXgK04ZNkY1o4ZGS4X6OMAdpmsZlGSQ8Bvo1qwru48xZthFEacxZWOwAQVXjsYePpcT2yzPW3TZyDFIqoBXQ5AGsM7MI8l81Iul-UwTRtARKZ99_3UQ-3Zf18UiPpot4UxTu6Iez-F2XOjFKNzNg1EvypltujWfko_UqHoGBXplzDB84soeSha8ZJ0iYwYamlfyoBRsPfxmx2c9Y9YQOBl0WfM0afN5HI0_brg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.  ‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،  ‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6480" target="_blank">📅 13:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6479">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J5GcPVNdZBI1dMeX_qGtmIND7-8uIgPh4Xp9byr_fcCTBFiAWgSI41sAZjSAnrRakqu66UpqXYozvCrIUh7224UqP6AkZsqtiHFLAo01vQpbeWMo1yUsOFsnvcqbX46hNW5cTkJqLQG2Pxxy8H3mRmhJPyQ0IU_5JDYngv9P46vEXMRLdi5YNdfFbHrrA0ysOkNLgg5xvF1a34_REPgJVu3Rsi5lLNpjdNVS5MRzxxJbetEW8yHOCgimQ4IKPyM6OHZT4MS9rmWRkyfsp0uenGbiIdirm3YrrXdN4B77MxV1E4s3K3Jx-c9QxE8HA6E-Mvzp_qUIz0uzX1vrq0DeWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.
‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،
‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا بتونن بچه‌ دار بشن. این رو خود آل احمد نوشته،
‏او اما آنچنان ضد غرب بود، که میگفت باید از اسلام، از منبر، از مسجد، سلاح و سنگری ساخت برای مبارزه با غرب! تمام هم و غم او‌مبارزه با غرب بود. می‌گفت روحانیون تنها رهبران طبیعی مردم هستند.
‏اساسا دنبال این نبود که اسلام تقویت بشه تا مردم برن به بهشت! میگفت تقویت بشه تا با غرب مبارزه کنیم!
‏علی شریعتی و علی خامنه‌ای، از چهره‌های شاخص تحت تاثیر اندیشه‌های او بودند.
https://x.com/farahmandalipur/status/2083853984113054084?s=46</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6479" target="_blank">📅 13:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6478">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-9ZjDUCZI26_ktlYF9hsKvFBibRjOzyAgsRf_RQ4ayv5BcZVdDjFK5MC39OUEas-O1V0Zs8HQkFMfnZ5KG-T9HLPdctS5vqUy6AZizJe0fXVM68iCASsvloFYsDRHhtdiNAOK2ClflVl3kKoKQtVyfhV2SP5rg6QgssCWr8GCY8WcIObNj2HCnQyCMVnIiizqnlTpGdzY2IW9RAH7TkthPiY9TtRHMxoyQocrfbjmrklnSv7xr6ZfZDQyPjg6U73hmSvlSXgFjnI-bD3ngZqX-KXE07A8_t3mcE9vhymsxahBTXQMbaJmlARBpcUScDhuInlptcbkWYmnl_bgCzFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه شعرا و نویسندگان به مسعود رجوی  - سازمان مجاهدین خلق -  سازمانی که ترکیبی است  از اسلامگرایی افراطی و کمونیسم و مارکسیسم!  تباه در تباه!  خرداد ماه ۱۳۶۰ نامه نوشتن برای «تجدید عهد  با آرمان‌های زنان و مردانی که برای رهایی ایران پایه جنبشی انقلابی را گذاشتند».…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6478" target="_blank">📅 12:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6477">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ubC_wHS_5xYb4N5qe6ezcdkUUmZ1riHnOj6DixtsvSVzwgDJrYPGbZ9kyXUy_trGImZFLuGvRWJpeGqJ5-jJIAjeBnqJk2iWPiMkQwMlUxSPRCyPxLGZTdrcp9LSosa2bT0bOTRnGu1nliYhh-IoFI4_PP7rnSBGyBBanBohCAHMxWBU4-sBVas8DXmU4HeO5yEgAzY54o6lNbVI3X89w9v8-gKQHJfbGrzIQnrtNh1BJG9cOj2kwgmfBV--0r6bmLmp_vZ5f1WSZ4V6NqNJlvvjSft-2A1JZ-SjftjryePEjrvjmfQahKGWtNDiDXtAU9lF3mF85J_My_ikiklHGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه شعرا و نویسندگان به مسعود رجوی  - سازمان مجاهدین خلق -
سازمانی که ترکیبی است  از اسلامگرایی افراطی و کمونیسم و مارکسیسم!
تباه در تباه!
خرداد ماه ۱۳۶۰ نامه نوشتن برای «تجدید عهد  با آرمان‌های زنان و مردانی که برای رهایی ایران پایه جنبشی انقلابی را گذاشتند».
احمد شاملو - غلامحسین ساعدی - اسماعیل خوئی - منوچهر هزارخانی - هوشنگ گلشیری - باقر پرهام - محمد علی سپانلو
اینها روشنفکران ما بودن،
جامعه آرمانی اینها، ترکیب کمونیسم و اسلامگرایی بود!
از مسببان انقلاب تباه ۵۷.
از مسببان گمراهی یک نسل از ایرانیان،
از‌مسببان  تنبیه نسل‌هایی از ایرانیان که هنوز  به دنیا نیامده بودند!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6477" target="_blank">📅 12:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6475">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C6ld7r0cN8csux-AzIZjKOKYUspOW6Eairtmy8OfAuyEHbspt4_cf27KPrbVSyV2dt6E5z-vV4yhShVw2bfasi5xuK7M47s5ea1i8Diso82AUxfw1BXPE2uL6dnUQlrxhKLnk_L35e3lYd3Fa16GdmRuZPksrxYVtLnJfmrocXa3dJMm91Gp_Vn7SzcfSX4FeZZ1bRcCT-ACEhxbZ_0OXxJykildym678yFov48W8ihIgBimJs5n_ZhYjty82Hmk33yYsCimxFnh6CKNIuRRk5YLlk1HvPlNJq3lGvP0wHQUHNYXAAmB-PGoeT3W-oyfAIgV7WoJzn1wxwiSJg3RjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=WbIxct6yw68Lo8NDDNhg4-KjRc714KhwFkwd5n8Z0h6QiC54Yqmn0phxZnSIJm26LXKaV1lx-qgXmsKuoFEy8D_MIdjJx5AoLz1zUgkZ9OofHOZbmvg4GJvA9AW0lxGHea0_6FzMCelXQbb6VNQgtpbJUiMPgyXsP0qHc0BRjcXj2Z_IaGreOxquSy6zUru5sGlR5JHVCafMEQPAc5BaPAkPHc4mPDm0pn77zH2AZhYrlUug1ahPEImFvAgALBvMNH70ZBMB3AnBHqIQny0620mLBDZHf-uhWKEaEXlixPJreoWEcF2rElrJxAKfgx2REO0ydnM-OnOQqZTZvmGULQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=WbIxct6yw68Lo8NDDNhg4-KjRc714KhwFkwd5n8Z0h6QiC54Yqmn0phxZnSIJm26LXKaV1lx-qgXmsKuoFEy8D_MIdjJx5AoLz1zUgkZ9OofHOZbmvg4GJvA9AW0lxGHea0_6FzMCelXQbb6VNQgtpbJUiMPgyXsP0qHc0BRjcXj2Z_IaGreOxquSy6zUru5sGlR5JHVCafMEQPAc5BaPAkPHc4mPDm0pn77zH2AZhYrlUug1ahPEImFvAgALBvMNH70ZBMB3AnBHqIQny0620mLBDZHf-uhWKEaEXlixPJreoWEcF2rElrJxAKfgx2REO0ydnM-OnOQqZTZvmGULQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل برخورد سربازان مسلمان با مردم مسلمان.
نیروهایی امنیتی مراکش برای جلوگیری از خروج گسترده جوانان مراکشی در مرز مراکش - اسپانیا مستقر شدن و مشغول ممانعت از گریز جوانان مسلمان از کشور مسلمان مراکش هستند.
تصویر البته مشخصا با هوش مصنوعی درست‌شده.
https://x.com/farahmandalipur/status/2083837885224988931?s=46</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6475" target="_blank">📅 12:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6474">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W5wEfEgb1ewcJMHRlBeQyI1VpQUAXTrjBxPvhHL0MG-cDvb12ba2aIvBvdh2_xd6HDO4cjt0B6ZizXruz4oPia3gRAtTjieDoo69MbILyFquvw2-iSIhHjcbJdBEHPQDRALbUy5fdhFedrazwKl75-FLUjcxHB6jsSpHCDoo1pFltpHQ8ZfN-kS1yOvBNZyvC02vJDfz8Ia4bC1Nc4P0e3fRGBna6A4F7vbEWqmBqwoBsslhHa-sg0iE6XDWO-i1IBK6gP7qJvGRHrx5RO1-sX2Yi96p4rS4g2f2Sgs9RGArpNc4yjK_rQhm0QU3EKG82T6MqIkfSw_vO5xE3PFvPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامپ : ایران و چند کشور خاورمیانه درخواست کرده‌اند که حمله متوقف شود چون چارچوب یک توافق شکل گرفته.. این توافق شامل بازگشایی کامل تنگه هرمز و پایان تهدید هسته‌ای ایران است و
به همین دلیل آمریکا و اسرائیل فعلاً حمله را لغو کرده‌اند
تا فرصت نهایی کردن توافق فراهم شود.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6474" target="_blank">📅 10:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6473">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVKsnifmgP5jUweiwyOE_pbQprepSg5XrxIOWnz0ILZEG8bFF273pOGSs4O8IkN7CZ2S5guRuJk7dFicAiJvbUL-zfI1--JTtGgz9JP52bqOJCCEShzdUTPZKxUiB0stZVgQr29MVs2IJmk2U8a2VYnS_ePyUutbZwPOOoOPPyj_UwRdLHgSVYbIEXV3U-4g2W6JZ0QvzQUfX19un90pHsIhJZtuL2ccFqkZfAwg6JB-NPC0LmwHAaaOZgYY0vjc8B-KlC7psad0KThtk5A94NM46c1YJuH5NtsAdKmm5G9ejSZ3cLRwHYk_8PMRrb-yylsSIQFPhizRFEpc7xHQKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ترامپ در آستانه
احتمال شروع جنگ</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6473" target="_blank">📅 21:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6472">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1QRhL-xZF96QSh5wV3Q6a8-a6WBC70M13oxs3PVX1y9TDbO6mlUWfUlb3aj6SZbSILOFS4bmkAowL4i6EcNd0WyaGZeGjtP9eccKsbro-EG12bKM4EEKOMX31jIU0jjk2es4SP4yWORcs3l5J9VnA8STFWXaZuPm9UJ1zyjz5xG5VGp1hQZqGlhwrT2oIS4v3lQ_PZP94khM7zP9vnehcyJJWbm2IuMIYFELtaLGRPUKkrOrmuY65WxLvS_TRM6Tu2zZOMgXfN5NBT4l_wQ47fj7rwuMbO-iSFRvOLPywN1FRBYtM57Elktryie53S_Ym0YTTqOnegcuNE8p1BavQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه تنها بنزین گران شد بلکه سهمیه نیز کمتر شد.</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/6472" target="_blank">📅 18:19 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6471">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‏سفارت آمریکا در اسرائیل از شهروندان آمریکایی خواست خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6471" target="_blank">📅 14:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6470">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nhiOTJZJ0qqepQadhq4R2brTEPSQsKxAjgqLOGmL2V-WDwSofOeOqi0GX8hnoDA7vm7BSSvQHkCVAlf_ACvqRiDe1iljBPDhLaC4i_CvrEO788HQutrR4ijnvE0-ZL61JXdMMjCyz7blm8g0DSXKSRrJFKaRVCtSI5y9FWoV3G9ZsX6K_6LwxrldBdc0nnXkIz_E8_ssSHsu4hs10toPIjBM-I6Iu0KmggRediKDPmeLerV1zpv4YG7rPh07WPMwwGMpFhzGpFNgtSyxe_SWLJuQHvTkCv2qWqIPfEQQXspKuGAQ0VJzq_UaiTGINF-WXQg6-q55sz-H2yHGZgK8zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرمین ۲۰ ساله و اهل شاهرود بود.
لعنت به جمهوری تبهکار اسلامی که هر روز ماندنش خسارت و زیان و هزینه به ایران و ایرانی است!</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/farahmand_alipour/6470" target="_blank">📅 14:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6469">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‏فارس: شنیده‌شدن صدای انفجار از حوالی اسلام‌آباد غرب
🔺
دقایقی پیش صدای انفجار از حوالی اسلام‌آباد غرب شنیده شد. هنوز محل دقیق و علت وقوع این انفجار مشخص نیست.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6469" target="_blank">📅 13:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6468">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">وقتی یک نماینده مجلس به‌جای سخن گفتن از پایان جنگ، حفظ جان مردم یا ساخت پناهگاه‌های عمومی، از ایجاد «شهرهای حکمرانی» در دل کوه برای حفاظت از مدیران و مسئولان سخن می‌گوید، این پرسش به‌طور طبیعی مطرح می‌شود که در این نگاه، جایگاه مردم کجاست؟
اگر قرار است منابع کشور صرف ساخت پناهگاه شود، بدیهی است که نخستین اولویت باید امنیت شهروندانی باشد که در زمان حملات، بی‌دفاع در خانه‌ها، محل کار و خیابان‌ها قرار دارند، نه مدیرانی که خود در جایگاه تصمیم‌گیری هستند. منتقدان می‌گویند این رویکرد، به‌جای آنکه دغدغه حفظ جان مردم را نشان دهد، بیش از هر چیز بر بقای ساختار قدرت متمرکز است.
مگر مردم تصمیم‌گیر آغاز یا ادامه جنگ بوده‌اند که اکنون باید بی‌پناه بمانند و سپر بلای پیامدهای آن شوند؟ اگر امنیت حق همگانی است، این حق پیش از هر چیز باید برای مردمی تضمین شود که بیشترین هزینه هر جنگ را با جان، خانه، معیشت و آینده خود می‌پردازند، نه برای حاکمانی که قرار است در «شهرهای حکمرانی» در دل کوه از خطر مصون بمانند.
اخبار جمهور</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6468" target="_blank">📅 13:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6467">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJPaO0YAWjOUxhp7F75w7VcCheRonxlIsP2drCgQl5a2Gr_KlgRyVBiLRKiXcEwAp8RpruEsM7ip9KsRJ4htJ1ZE4DIyJ2OpD_MY9CLGlfeBJWYY7qJis7dquPi9evgoxFvP3uvv8I6-GLAzETFHY-YifmSH2lBGduriyel5j8aauTZxdgymiXmTvsZy3soQITtzxWvulTewriue9-KFToBZwg2z0ZBnd8BUSAd-AtMiaLOfuvlQ2bj42CafeXBPvTloukpYuIFOygbWnBEWUDc4JxW4A67g-22X4Uc1gK51fNXm35Uz5_xa9pF6xXgYvdWPrIvQTuwYb8SIXzPwjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«علی لاریجانی» !!
در زمانی که رئیس سازمان صدا و سیما بود، بزرگ‌ترین دستگاه پروپاگاندا و تبلیغی کشور!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6467" target="_blank">📅 13:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6466">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DuMZKL9eXXtqDNEEoLSusZUvq1uSp16PsprRfK8HO8mF5sIILFK3CDjSY55sLxhaNWkXxBjTYBPA3QIkYUcMEQsp6a_11BLHN873fto1VaIAGdYEIgPW9bpcZiWCcoum3qFrs-cltqpIaD8_5LoTZfa6ivUS8sxUpNSRKaFoM8G3fkEECT77asvRZHVuT830EMbE-CTBn6nIh4VocAHfwN69Dd_mhPHMQOiA22H7pJLaCjfnIM3gHzzk3k47WYGehhcLdy-M43RufRC_EHN6o-YY-p3p_C_DjZQ9bqrboeClU4ZTSc1SF9IDyE2kXJ5V4X07pg8Z29wTZQRlxQsw-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌‌ان پیش بینی کرده که حملات همین آخر هفته (همین امروز و فردا)
شروع بشه
ترامپ گفته راه دیپلماسی رو نمی‌بنده
و اگر ج‌ا کوتاه بیاد از برنامه هسته‌ای و…..
حملات رو متوقف میکنه.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6466" target="_blank">📅 11:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6465">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ev5LXy2_l1XqNkKu-KgtQ3i9jSo-_y1_gtPZs3gdPsRhNHjWSq_6KvuVzzfHtA49f-UR8I7RXLRZWPFfiHkKrSJVpBUr3mnxny9zoBotfEBduaNwNnXG_KYmPRq9DWvbMdriY6sD2eAZg8qhofYHh5RB-391zZnMA8aOBqFZ4qFxW5oWnZ1Tme6PwFiRADHEYq0R_Tjv9sEaTg_CHbzfPBGHEXWxocc_xVKQU3VIsDOxNy3YqS7fcj_29U-LyJxqtSNBbotdLZpgMZ5qZLFWPCZzs-amna7S-Trjzba-PcbP93L_NYxFWYLvqX8MqXYJZ-vVy1RiQwrVD3DV3c6vKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ دستور حمله به ایران را صادر کرد. حملات احتمالا از آخر همین هفته شروع شوند و برای چند روز ادامه داشته باشند.
بخش انرژی ایران از جمله اهداف اصلی حملات خواهد بود.</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/farahmand_alipour/6465" target="_blank">📅 01:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6464">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_dEbtekUFK1XKOJ5yGx4PQBHZK6XOGKclvicDVI-mcjYEAiQFifyraokv8I0hxoXr9Gr3471EW-qWRHuXIgPmuTliQOOluQk9NJnvZow4rdmYX2DI0iUtebVhpzm9DZAF1B8QugoJ_nqQhuUTfbUJot8XPUqImRoIsjymANP4pxVNW2vMeNageeC5HXt95U5Ranu1xEbqA2sws338e-tYnUQqkJHYt_rVAvBPO6Y6u7y3Uwk4Z-gHLtPDWr4civafDaufX2059tvoqk8WVEBY9Yg8RE5ukB7P7_Eh3GacQrk27zKh4pm_9Vst5DnoETCT2sGs6ScxkskTPQoyYpQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
دولت ایتالیا آزادی رفت و آمد هوایی و دریایی
بین ایتالیا و اسپانیا رو به طور موقت لغو کرد!
این بدین معناست که تا اطلاع ثانوی،
پروازهایی که از اسپانیا به مقصد ایتالیا است،
دولت ایتالیا مسافران آن را کنترل خواهد کرد.
اقدام دولت راستگرای خانم ملونی،
فشار بر دولت چپگرای اسپانیا را افزایش می‌دهد.
دولت پدرو سانچز هم اکنون نیز دارای کمترین حمایت شده و پیش‌بینی‌ها حکایت از آن دارند که در انتخابات سال آینده از قدرت کنار خواهد رفت
گرچه برخی از راستگرایان امیدوارند با انجام انتخابات زودهنگام، انتقال قدرت سریعتر انجام شود.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6464" target="_blank">📅 23:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6463">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6463" target="_blank">📅 19:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6462">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6462" target="_blank">📅 19:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6461">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا  نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6461" target="_blank">📅 18:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6460">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا
نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6460" target="_blank">📅 18:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6459">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=t8-0akWh2qTHgZFMkeYPa5oTeu3zRPkzCnY0PX8mrUEdp9S_Fm_P_4SrYsJ3nb_dO8RczDCJRn6qJkzw-tyx-ye6NvDiSqDZDMvYz-L-7PEuYqYcuBeYjiLHaMlmU2Za8bxAjmSWVX2pjGv6Ep4n4xAfuaYUAJJUD4geqY5NfDzxzAljeUf1S5qe8q9vOH5NbIAdnuPduBjYqISwWFtXfcj0BKva3KF5snJc_sK3RoZ-3GCcr9SKb_iSq-pK7axtCLKDT-T-5bTX34XMdr0BCOr8btzPk7ZB0wzGWu2uxI8wnAbt3PmIoUB18yFyNqWnyOxnW-RB9Rc5SQENuboRhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=t8-0akWh2qTHgZFMkeYPa5oTeu3zRPkzCnY0PX8mrUEdp9S_Fm_P_4SrYsJ3nb_dO8RczDCJRn6qJkzw-tyx-ye6NvDiSqDZDMvYz-L-7PEuYqYcuBeYjiLHaMlmU2Za8bxAjmSWVX2pjGv6Ep4n4xAfuaYUAJJUD4geqY5NfDzxzAljeUf1S5qe8q9vOH5NbIAdnuPduBjYqISwWFtXfcj0BKva3KF5snJc_sK3RoZ-3GCcr9SKb_iSq-pK7axtCLKDT-T-5bTX34XMdr0BCOr8btzPk7ZB0wzGWu2uxI8wnAbt3PmIoUB18yFyNqWnyOxnW-RB9Rc5SQENuboRhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سانچز در میان اعتراضات مردم سئوتا
وارد ساختمان فرمانداری شهر شد.
(این شهر خودمختاره)</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6459" target="_blank">📅 18:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6458">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qv5hfy0VnpXLylbQz0942d1SGGqCpzQ1D6uZPnP76RJ-nvJrabpLLfCNplsk2AlsoeFSquwTrVb6bIqSUK4Jz77LXKcekjJBgXlveS5brN-xziHuhf9R-DiUi9mGHzTker2xgySjGM_Zm2ybwubsGW3M_LUHw-loCFfgadFSjFiqwCpIDjTY-S3Bv4UtABSWegOvjgHBe6KicxGAy-JpveJTHNnBRDfi6CN2dCcH8ktxX4LjdJzvSDR_AdE_rLiSDI7Wm5j02R_q1ZaGyxGbsdpY8oVQ76dP5CE7MaYsmA2yG7A3OvjqRthNBIyk6Hi964sUHk4TuHTdmVQ_exRb9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته مهم :  چرا از دولت سانچز انتقاد میشه؟  به خاطر اینکه این پرونده حدود ۲ سال باز بود و مشخص بود که یک «خلا قانونی» وجود داره! و رای دادگاه سئوتا، ۲ سال پیش این مورد رو عیان کرده بود!  دادگاه هم قرار نیست طرف دولت رو بگیره!  انتظاری ازش نمیره!   اصلا دادگاه…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6458" target="_blank">📅 18:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6457">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">اینها که رد شدن روی شبکه‌های اجتماعی نوشتن که پلیس هیچ کاری به ما نداشت!  و فهمیدن اگه از طریق دریا بیان، دیگه پلیس دستگیر نمیکنه و …..!  خبر سریعا از طریق شبکه‌های اجتماعی دست به دست شد، چند روز پیش مثلا یهو ۲۰۰ نفر وارد شدند، اینها هم نوشتن که آقا مسیر دریا…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6457" target="_blank">📅 18:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6456">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pP_5TDYh8e78ulHrDrItTfjrH403Tv8Hz_86s6CHz0kyu28nC2_2dNlKRR0H_t881Io7-djo7PsSuNMzfO_rB5X56VyIAOPa3OVwcCtBFCwcC1cm8IkryHYk7Lyd4Kp0sG4Vw9sjK3l85javQLKkLDKtr2Vr9SdNp5lhV1Xpfwr_AyH1qMbEXVDB9gF1BGb_S4uGP03pCEazyfSG5c8Cbo_7mDx7wG9XaovcRyyhKiEGMIGH97Sqrf1XwcOCpwAHkB3T2XqLkzLK4o37GyKp7xRtWErU-vlkyc6gAIM_rW6_vDog7x3SOdf96WNExxAA8XdZqfrwxM8f6BcwYYIVwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه سئوتا گفت حق با مرد الجزایری است!  در قانون اومده «موانع مرزی!»  دولت اسپانیا به رای دادگاه اعتراض کرد  (چون یک طرف شکایت پلیس بود دیگه،  و وزارت کشور و…..)  کار کشید به «دادگاه عالی» اسپانیا!  دادگاه عالی کی رای خودش رو داد؟  همین ۳ هفته پیش!  و گفت…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6456" target="_blank">📅 18:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BHEs6Dg7mprM_SqgyphTEWZ2MKpZ9tVUpdEhH9ALRAv6tQZu0R52a3ic6g7rRxKpVW-nj5-JpQA6hLZwrY13q8FyiadTVjUftNYApDXZVP8nOd1p5OM8tTKF1oSlJzNSMbX7kxYvCSM9-aY0F7KQLMkmMElWSGbs-g9dk3vL9a6B1s1BA1gQpAVontpHG0g63qfwtNslH37jimTCPuIyODzd7PnYo6qsds9Z7IvWkNg8q49rjO0JblOS5FUl85-8S8xqhyKwYRSg1i28n3hVHYbNDf8ua__-_i1v0GZWJPReu0z3qI2ZRtzIB16SUY9iT9rKfxNgzu5o_Dlhnh_0QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داستان اینه :  حدود ۲ سال پیش یک مرد الجزایری  شنا کنان رفته بود «سئوتا» پلیس اسپانیا سریع دستگیرش کرد و تحویل پلیس مراکش دادش  (چون مرز بین اسپانیا و مراکشه، و اون از مرز مراکش وارد شده بود)،  این مرد الجزایری با کمک ۳ ان‌جی‌او اسپانیایی، شکایتی تنظیم کردند…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6455" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kspgCz0SgbIdMSG-TaWVTn6hGSm-M7JdO3WTWhUqftX0i_FAvUj0_o0NB_TAY9xrl65PQsYvElorvL2unNrhaIBtsEWj4vJSXoYQeNIq-TlRd6aO5IBS0lwZyc_qAJhBn2idYFBPqc2mRnPg9_MA6xrkYTHnz6xr-NcvJOyc8WgMZ5zDmd2946IobH_lQqqEgmpUE2q6mfRcZoRPiPqQ4jOGllIc03gERAcn_lfhtmkddAWsIfuPXZWrCt5feuEflJQYs3BM8JKZ9nCW5TcLcy_nNkGD1rCooKsZMUZymSTjkrJT4gXbRs4ke9gtCp8iSyiUTeMdSfjKWHCSoGttQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایس نقشه رو نگاه کنید ۱ سانتیمتر برابر با یک کیلومتره!  اینقدر کوچیکه! با این وجود ۸۰ هزار اسپانیایی اینجا زندگی میکنن.  حالا چی شد که یهو این همه جمعیت روانه اونجا شدند؟ چی شد که پلیس کاری نکرد؟</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6454" target="_blank">📅 17:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6453">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N2Zpq0OEZ9og-FVf5Yr93iwNPkykqTrmHpkCLRCCDVVLHXThUeu_kVBYaJ4bNmOisoks0MeG3B9R3hXrRG2XHp_Py-o8SSJbWA-Vsi4UYQ09ejGHgqanLn5nVOeCkPznzrXLCeONweaRwyYGEWTD68KfBBkPXOpMUruCMYw_N2VGDROqwKIwX1iihIqNcSL540T7T7vIf1ZkmJ4_QjloqgTrI8FR0979YVapMbDDHnP1vg2QgRPJk7SrOkTMKSgAdpCRzQnCjZcQOt-HcUe_aaJRfJ9OKmd6iRFRGym3o28FnOC0WQBtTkWSERg3uUITZztndEzLBNVE82KxnaLcpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲- دو تیکه بسیار کوچیک از خاک اسپانیا، از جمله سئوتا ، که خیلی کوچیکه!  اندازه مثلا ۳ برابر شهرک اکباتان تهرانه!  چسبیده به خاک مراکش.  و بین این سرزمین کوچک اسپانیا  و سرزمین اصلی اسپانیا، دریای مدیترانه  و تنگه جبل الطارقه. پس برای مهاجرین مراکشی خیلی ساده…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6453" target="_blank">📅 17:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cF40MEHnFvx2WIWSz_xfmmb3pvAxtVjoGycBKM0-w5nRJliIOgM29f9kainXzrBMl4UKvhUHCOw2Jai_WB2mIzLTsPdcgTjXV_G5EzJajjiT8OwW5TfAWjek7RTyQyMRfYolBC9hGjhtVdz_Mi4qrLQqyDKAGQ6zKGxsjW1wzO7jwCWLlf5m6-ri5hmoBxjvJT3LjKST1sMkzRM7t458Lb7r56izsxM2c07VDDVpTO1b_3t88q-4u9T_1gTSLRhPilj9QG8vMCdnSwR3W5-y_LB_TTmYl6jpu6F1hiV_YIZIQoJdTHZ8Cf0SCZlapy4S7pnXM1daC94bZSfaD0Ju5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا  دقیقا چیه؟ و مشکل از کجا شروع شده؟  چرا انتقادها به سمت دولت اسپانیا رفته؟   ۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،  حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند. …</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6452" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6451">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HMRB4Z02T-aO_5U_jlHt0-BPqn3rlEgfAkpPVZ2LVJePE6T70i2iEhZG6D10JCex2U6fVpCIzffewhznQ15LHySdAG7gDdFAnq1h3cMcHW6N9YKly7Rj7Xo_PZ9aBrDfBCRu3vHSIrxzoiME4qcg6AzRA1AEM9rs08NTZUk5EEGzmhyCc6457wb5dYU6JFQglF4h0aG-UFNTegtg9nwHajkkUdMnkWZwrCXJ-sBZtIvFbOqHG9zex03QakgWrLMJugHDJC_6MCPmimiGNSLhK_R9dcRQvGfgpN50_uJG2iGtfvKeuqk_4-Z99gGDqkxV4taSQ0axX68Dy7bMfsWsiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا
دقیقا چیه؟ و مشکل از کجا شروع شده؟
چرا انتقادها به سمت دولت اسپانیا رفته؟
۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،
حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند.
این خبری که می‌بنید و تصویر هم مال همون سال ۲۰۲۱ است که پلیس اسپانیا مهاجران غیرقانونی رو دستگیر کرده.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6451" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6450">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=FaUJ5mz9ZZ50NLedYle1M0FEewrfMd21_FPeUf2YfYuZTlNn2glJ9l321WsM1uiZPS94nUuI1Vo40rnsMwlMfhFwRlPkPiwuSIAzNo2-qSOm__80QiUQQ11ye8Jp3kFOV1Y8wcJ_mp_R7ImtpvU6ElfGrB8ukWrpTI7wkygH-b007PwMf0_1HCwWST-ZB3ewU3kBxpahrf508WZKpWwzrWlF8hAqr9TSTNVZHG2Ipml2qMQ-pgp6pULsWK3kJcFSMafvYa-HgY4rfR3KcJgp7QUzzwXoeUvTAHV8L4YCfyGAJa0aWBmjMN13cCNw7N6y50NbzrUmmjp5e8pSFb18pFuA66WQF5eDV-rxnT97Q72rEO-9sys2GzAG7DirX4Jdnnn6wONTNPqhxWMDrgSS6MlIorOv434oRTqNuCL-GMI1HXCLzJpiPaLKEQippdAR23RywWwVpxtmrGEHcmmcRcrU7yb5St4uR1Cb-EKlSuV4mCAzmdRJfafZ0qn-7L_BHcahHKmZLnHkES2fZaXd1cu_JTRggiDqjSwpOqDDKUQ0ylgx-sJo1igS8bd1_APdJkTB5cn0HL8b4vnfgzgar3POhjqV0N1a0gHu6_m784V-BBAkSk4Z3tv_PhnjnsU88ed9zzCiapUQmVo9-uR7_Mp5G4JjT6rrqEHjRbtsLBE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=FaUJ5mz9ZZ50NLedYle1M0FEewrfMd21_FPeUf2YfYuZTlNn2glJ9l321WsM1uiZPS94nUuI1Vo40rnsMwlMfhFwRlPkPiwuSIAzNo2-qSOm__80QiUQQ11ye8Jp3kFOV1Y8wcJ_mp_R7ImtpvU6ElfGrB8ukWrpTI7wkygH-b007PwMf0_1HCwWST-ZB3ewU3kBxpahrf508WZKpWwzrWlF8hAqr9TSTNVZHG2Ipml2qMQ-pgp6pULsWK3kJcFSMafvYa-HgY4rfR3KcJgp7QUzzwXoeUvTAHV8L4YCfyGAJa0aWBmjMN13cCNw7N6y50NbzrUmmjp5e8pSFb18pFuA66WQF5eDV-rxnT97Q72rEO-9sys2GzAG7DirX4Jdnnn6wONTNPqhxWMDrgSS6MlIorOv434oRTqNuCL-GMI1HXCLzJpiPaLKEQippdAR23RywWwVpxtmrGEHcmmcRcrU7yb5St4uR1Cb-EKlSuV4mCAzmdRJfafZ0qn-7L_BHcahHKmZLnHkES2fZaXd1cu_JTRggiDqjSwpOqDDKUQ0ylgx-sJo1igS8bd1_APdJkTB5cn0HL8b4vnfgzgar3POhjqV0N1a0gHu6_m784V-BBAkSk4Z3tv_PhnjnsU88ed9zzCiapUQmVo9-uR7_Mp5G4JjT6rrqEHjRbtsLBE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقاد یکی از سیاستمداران اسپانیایی
که مخالف  دولت پدرو سانچز است :
می‌دونید که پدرو سانچز بهترین دوست
آیت‌الله‌ها (جمهوری اسلامی) در اروپاست
و دوست خوب رژیم مادورو بود.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6450" target="_blank">📅 14:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6448">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=akC-cyySoBgs_k8f5Ianhdiqa9LblOe5qCD-7PiYsciAkMcjY6I6Oo3RT9UW9l0UqOOkWqoXrwBv4V3T7lm4MlwboB0DUbWFN1GIp4BbDU7gaaTFch2JpY50Ms0lUqGxv8uqX1sHvGZpyQ1c6jQQJYx9cqb01L3Ac_wzWOeGFZVXngoRTINsxuFZHAELP4eLqdqfSGzdGIucrIS4w_RxOOqH__7ovoQ8zUmm16gZqakQWbNxq--nbORmo97ihwQ4vYLfy3IqDShE_vpgg52iU7PUuCTAZoY-WmJqyhhLSPsDLeCtocUouSsbWM7RDZ7ZI8aRU2gTWT6WgPsvzyu-Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=akC-cyySoBgs_k8f5Ianhdiqa9LblOe5qCD-7PiYsciAkMcjY6I6Oo3RT9UW9l0UqOOkWqoXrwBv4V3T7lm4MlwboB0DUbWFN1GIp4BbDU7gaaTFch2JpY50Ms0lUqGxv8uqX1sHvGZpyQ1c6jQQJYx9cqb01L3Ac_wzWOeGFZVXngoRTINsxuFZHAELP4eLqdqfSGzdGIucrIS4w_RxOOqH__7ovoQ8zUmm16gZqakQWbNxq--nbORmo97ihwQ4vYLfy3IqDShE_vpgg52iU7PUuCTAZoY-WmJqyhhLSPsDLeCtocUouSsbWM7RDZ7ZI8aRU2gTWT6WgPsvzyu-Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟  دستاوردش برای انسان چی بود؟؟  به اندازه یک قرص سر درد،  تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟  اینها روشنفکرهای ما بودن!!  این‌ها بت‌های یک نسل از ایرانی‌ها بودن که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6448" target="_blank">📅 14:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eg_v6gH5Qtd6uDg2Riafiz3yD0lQ3cLKi5CEiVRn1Gv4tFQOwhihK01y1wRwlhqcRNqaqgAe8Zq3skT3VZvLikxQl6Uv1x3wKIxlkYjRfoS4GYW5igQWIWmjfc0tZXdZL_Dr8RFH0TuPwvP6KhSF5xvMKB_hZ07w7wku39WvG-NlcXcV456qTkdCPRIHY-illdfHIDtFY6X62-U2KP0CKLvlrthptmK0KEF_pDTJISvtrMMiPtVJvQMfOK2d585A-j0eiWNd-ocPCg3oxOjCnoTfSt4Ubki7arPxa2NWvt96_zOnGZApAs3YAgaEZK_77gQmZOeWdMV4I9mAvSNfOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟
دستاوردش برای انسان چی بود؟؟
به اندازه یک قرص سر درد،
تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟
اینها روشنفکرهای ما بودن!!
این‌ها بت‌های یک نسل از ایرانی‌ها بودن
که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6447" target="_blank">📅 14:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6445">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JAQoG8tiOqt1kdK7c-7_XDUyBwKLA9pBzM2PLlkU4LxeTjxLiePp5cn-0NdA_espCtqXcpPOeipmDaMFgjtbJGHNPVRsokpP3rcX16qk4-T8q7lIwGbwNCFca96ebTKW8qXluzfaW4lfPvB6Hnt2ZtRyD2DQBzBtEmBe-7VrLJoT5x0WXJ8R2Hqsj5_Z_RxHUDtMRP4jGm3FYc0HWakXAs7Ry9O1mhb_NHmtven-9jivVOOBzHeV7UXbyRhflNE3k6cyL-mgPWOTfQD7744OrcD6oySAvIPcUmPdJjy8DDXPXpv8KN0c557jQhYPf_Om0p6Hpj0A6J41_FwtPn9pkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=AzWFuiszuhyl0fvZVm3beZVGvP5Pg5MnuqYk8Cpbeg7tGs6cMg8v5vdsL69A7t-V4zk8gdynwJKckkKLVmTQ2ngqGuQ8SUMKFy9Z97f6SIrcYxrYSynANzhgIDlQEo3hxtXfvIpGl-bjnCWap3C_tgGpvE0C8yozY5DKbosBASTIiRx6piBFucuGDjtAgDucWJGRcqbNYY63USF0-rEZxZFVHjPDHInglNnK7rn_kTpCVwM_Oik-wJMu3SqhbTi2Qcu9y7RwkYrhM1MYUpvv9GhGNA1aslnu3VxtU4L2MCumU-7y8D85AgEnp5IpJUluMmL1u3mIQXfZs_tulRIgzYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=AzWFuiszuhyl0fvZVm3beZVGvP5Pg5MnuqYk8Cpbeg7tGs6cMg8v5vdsL69A7t-V4zk8gdynwJKckkKLVmTQ2ngqGuQ8SUMKFy9Z97f6SIrcYxrYSynANzhgIDlQEo3hxtXfvIpGl-bjnCWap3C_tgGpvE0C8yozY5DKbosBASTIiRx6piBFucuGDjtAgDucWJGRcqbNYY63USF0-rEZxZFVHjPDHInglNnK7rn_kTpCVwM_Oik-wJMu3SqhbTi2Qcu9y7RwkYrhM1MYUpvv9GhGNA1aslnu3VxtU4L2MCumU-7y8D85AgEnp5IpJUluMmL1u3mIQXfZs_tulRIgzYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شما مشکل کفش‌هاتون توی مسجد
رو حل کنید که پلاستیک به دست نچرخید،
نمیخواد نظم جهانی بسازید!</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6445" target="_blank">📅 13:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WwtgSXDhmTnBbrHiV74cCoDs_9VWq1wb0isjJjLIBGS4RQGMovwB_3zQ4G6Wo6e5G_4800cU_paDKMCr3BAxzlsDKT2NLYuzctcGkL_9b8mhD8LePDyWA_FMcSmXMlNF-sQtkDa9lOcPUtaYiF6HC805tBqQbIidn4xdmguuRzguSfUmT3XTw5y9k3k9738qNeZBgg5qBAz825rvf5F1R3oAmZN1QGg0OBZZJvb2_XEqnq57JjfYDW4Su0ID0s43-soeRbDk-Q05voDC-0gx51cLRy8ycbkkZ99Eah9SnCp1nmcZ7C1cvJrTFplCEdscl5BRD-HussjOvV5S_38iyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس عراقچی ۶-۷ جمله نوشته که خط به خطش دروغه!
نوشته که مصر یک شریک مهم منطقه‌ای برای ماست و نمی‌دونم امنیتش برای ما فوق‌العاده مهمه!
در حالی که مصر و جمهوری اسلامی ۴۷ ساله هیچ رابطه‌ای ندارن و مصر حتی ویزای توریستی هم به شهروندان ایرانی نمیده!
همون موقع که پروازهای جهانی در اوج بود، حتی یک پرواز بین دو کشور هم نبود!
نوشته که اسرائیل علیه اتحاد و همبستگی اسلامی است!!
مصر حتی برای کشته شدن خامنه‌ای، یک خط تسلیت هم نفرستاد! براش این اندازه هم اهمیتی نداشت! کدوم همبستگی؟؟!
🔺
دیروز به دو کشتی حامل گاز مایع در مصر حمله پهپادی شد، دو تن از مقامات ج‌ا به روباز گفتن این فقط یک هشدار بوده از سوی ما.
دمپایی پوشان یمنی هم گفتن کار ما نبوده!
حالا این اومده میگه ما روابط مهمی داریم و همبستگی اسلامی!!</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6444" target="_blank">📅 13:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6443">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mAxvcCb8i03ycAo-oqNOROmAHqVoxjBaiEoDfIoJK3r-EcZE0CitTXMtnUUOphsOI7Jc5J_l1zojKyDZ-X_sHVTtArnjkAF1z7REkLM7E1pviV97mZhjwmfhBQhZSVlrN2uxAGy8pJO_JTVtzHXtRc075yQmLuhr-qlr4LLF6j9cxDqKmOqwqe_mzeWj6q-4t4AzSdEMastGyDyurHxBaPl24VQxEuBRWd4tlDv0zfcau3kMcnolzPKsTPg-QUntFk-ALD77mvJyKc0yt0jMqVLDL1aTRs75cb260V_fqKiB_Ei3mXJQbImRzZTkcDujOSmo5kCcgapx5y4zQZ5WmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه امروز هم اعلام کرده که به دو نفتکش در تنگه هرمز حمله کرده.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6443" target="_blank">📅 13:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6442">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pcm9eS_Q6uHxVO9wuQv01MrZ8ExL5N8_UK6tNsipGcAzrocA0RZveyXfJ7HyV0geDGhEaNVBqo0CdCgOEI2CUxfyHBd8IlCaHmTj0WvF_h1kPVbCQnWh9k6ynlLKgEmsMFZLMFxJSz3P4JxgfLb2AHwEr_JTp-gM0jSeQpWA7lCvw7dh70XUHk25PufeOPqXLRY87rxlH5Gz2VfhE_MhERxwR4XYRvklm2iTyGF007jg6jkdV1QQU2SniZloA_FLnGoH1H6LMl9wxHwHohMxjnZzGYZ_ZFvJapwqIcH6iTt_-MHlLwxr5yfn9VDHmZ8F-SgMYx2YiOBh9SkiE78zJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۵۰ هزار نفر عمدتا مردان جوان
در ۲۴ ساعت
گذشته وارد شهر ۸۰ هزار نفری
سئوتا در اسپانیا شدند.
🔺
احضار سفیر ایتالیا در مادرید.
در پی انتقادهای دولت ایتالیا به دولت چپگرای «سانچز» در عدم کنترل مرزها
و درخواست بستن فضای شینگن بر روی اسپانیا، موجب خشم دولت اسپانیا شده است.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6442" target="_blank">📅 13:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6441">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CIQrgP9ko5fcLV4oKhWOLwEemju1X6AgdEWe42w_D7h1cnsUvxkumTrVttY1OT-UF1o4oArVrwWg9WT_OBclLG6pWm7879rx_aHV6NSfnUrhSUu9mzbmeTsPoc_cqUAxnFK6Xj6awZV36ydLYhpreWydcJsIMbl1ehibj3b2G3EeoWKLgZpSU5AqDG76M1enU9kpasq01hHipr8D-aym1WYVIho0YtRDJMd5JufnkPHPj8ybUPcItjRh3wbq1p10eSxvxoiOVu3Xc5o_sWw9GfN9EwaeLeJvC-_8IHSH60ufLIZlFwRYoTr8lYdvYP5MJBUcWSNdhdUw9sFjLm9J7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه بار هم درباره حجاب نوشتم،
در حالی که اکثر زنان جهان اسلام
(نمیگم همه‌شون، ولی اکثریتشون)
دوست دارند مثل زن‌های غربی لباس بپوشن و…..
زنان غربی هیچ تمایل و انگیزه ای
به لباس‌های زنان کشورهای اسلامی و چادر و مقنعه
و عبا و نقاب و برقع و پوشیه و ……. ندارند!
نیاز نیست حاصل تمدنی که اسلام
و جامعه‌ای که ساخته رو در ده تا کتاب قطور جستجو کرد! همینکه جمهوری اسلامی با حکم
«۷۰ ضربه شلاق» و «گشت ارشاد» و بگیر و ببند و پلمب، ظاهر حکومت و فرهنگ اسلامی رو حفظ میکنه، نشون میده، این تمدنی که میگن،  یک آدم برفی و یک توهم بیش نیست!  که به سرعت آب میشه و میره!
فعلا پول نفت پشت سرشه و بگیر و ببند!
حاصل ۱۴۰۰ سال عمر و ریختن ثروت و اموال مردم ده‌ها
کشور برای صدها سال به پای این درخت، هیچی نبوده!
نه هنر، نه علوم انسانی، نه صنعت، هیچی!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6441" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6440">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rx4I1-Jb4KqcclCBSoe4jyNC-xiuz5dQWuw4nqS9XBeYOsLvOeQfwnV5bTFd635kjZzd3eDCmY1ncz67gaYgZErfWVeVv-shk_ajzVGnBKEc3me91hr2RQ_ox4IYXFUOyyN22EekCwNjhs2-nmyVj-ElnhH7w50I5QuJzdwwdapmweHaeBkPjtkfLi7so2gPOZ8S4JrJhO4f6Y4I2MmK2G9G8KmO3HfIL8TZ9QaoZQbVvaevASbVuku9GO1bWRWfp9JArxx9Yv7xanzEZu8qBt_xbmQ9rRu9QnGQuXaDjvi-nsoHQOn5eRZI1AXGBguE9Yb_mjcMfYT3l6qcvFTS9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منطقه‌ای در شمال مراکش نوشته :« راه سخت است، اما رؤیا ارزشش را دارد.» پرچم اسپانیا</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6440" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=gClhvqRqodctA9oP9Pdg0bqJBgE_BCfgcHbtvNgTtfmIldMlzZPGRcHqbHDjl7IGBJDTdEifUYQsnJPLmoXwFqmjvXNpLK08mXhY69pro91iN_TCFVJgexzQLt-5CKm6YvU4eC_Uqu9hUsLUQUFjlIACD7R_lB0Z0JzkNBdi6C1qw61iC-wYwprJyi-UFWSSi9GK8le9SrSqBFXNYV9A1H8ChUR3T-El7hG6ccmLJrP0THsOM7VkRZHCRF_rkFFS5c7A2Ti1WuKf7IcUXbM9s41VoX0kZFFAR0M_b3x-Nz7_abTVpBSEsbeyUh7hJJegsHRcxTe0cDerVN0Imlyx5UmRh4yXGo-pMP6VHegP2cpozuEAu2-RcZ7aWsbgqbKM_dONB5tJw7TLuxW-qmSxXwj7vUvBTe7-PQyVeVFn5qwLD-HX1brGZF3UGY03aXYngkaLiLlLv6AmSBVDxMm3yiZhQAN6QCPsGXRN_GLdOHPiTS4QXOv8ls1lqG5KPq0wWKDEg90wx57ZNn14bPOYh1R-DdYm4SMYRg837_v6U3EgonaPKyOD2z8U8xpYQ9zGmB28qylVCbwZvSqr760iNphmL4FFv8l7mxd04Oa2iEBabhl4kS9TNG5ZRx9IWVtlA_bax0MZIpRURnq0jvmUpC5cjwIroGkDWeEBkmv5dHk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=gClhvqRqodctA9oP9Pdg0bqJBgE_BCfgcHbtvNgTtfmIldMlzZPGRcHqbHDjl7IGBJDTdEifUYQsnJPLmoXwFqmjvXNpLK08mXhY69pro91iN_TCFVJgexzQLt-5CKm6YvU4eC_Uqu9hUsLUQUFjlIACD7R_lB0Z0JzkNBdi6C1qw61iC-wYwprJyi-UFWSSi9GK8le9SrSqBFXNYV9A1H8ChUR3T-El7hG6ccmLJrP0THsOM7VkRZHCRF_rkFFS5c7A2Ti1WuKf7IcUXbM9s41VoX0kZFFAR0M_b3x-Nz7_abTVpBSEsbeyUh7hJJegsHRcxTe0cDerVN0Imlyx5UmRh4yXGo-pMP6VHegP2cpozuEAu2-RcZ7aWsbgqbKM_dONB5tJw7TLuxW-qmSxXwj7vUvBTe7-PQyVeVFn5qwLD-HX1brGZF3UGY03aXYngkaLiLlLv6AmSBVDxMm3yiZhQAN6QCPsGXRN_GLdOHPiTS4QXOv8ls1lqG5KPq0wWKDEg90wx57ZNn14bPOYh1R-DdYm4SMYRg837_v6U3EgonaPKyOD2z8U8xpYQ9zGmB28qylVCbwZvSqr760iNphmL4FFv8l7mxd04Oa2iEBabhl4kS9TNG5ZRx9IWVtlA_bax0MZIpRURnq0jvmUpC5cjwIroGkDWeEBkmv5dHk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا  خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6439" target="_blank">📅 10:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=cfEFSZqkFD-tpSe0yArs7edwi8rs30Vuor-FA9ObipI1_BUfei9lmZhW1BOrMihp_9gu1jQ_eDs0GtBwEuwAeTwP23yJOvf9v1aYzytGyNM_FCoGyAcLNprFjQL1mUg6Jghd9ihsrM-yzNhURQpVHxy6-fnmjj4-uTkoQbPE8r8ECFxuO8iJrwA2DKQ8WXxlVzzDghD3akgkk9_qtZvcUB27SJShSYhmNo8bLMrrb7teoX2CMcK87SHzywENDkjqgWy19qk9DInALTYRp5_Te4T4HVTAsk2rsKt9KgxH5YmdqrLGNMrKyOTqi4_Szke2z2gzwdHkZTKK_N7JBOPCnCkEJf_DQ_nV3JcxXxuJh5zqEwZHnkso7p3zzDU2kjD34TbjMl4z_r9m_47EkUi6JNZBFBb2ydSlESNd-SMgjmi7QrIiipBDDr_EeEst9FYPDnzQWwUNyvQyarFv8gUWPMkRf2JAtlK0bckji0fZeIJhDMOy5nNS44Kfl_2tuZn97ept7-JBh4U-0dXTL1QgtVco5-bZnjdyu697pBO4VQ9lYLooutBFBxBk_yfxfqPD_cnO0vBceqn4iHPWspLWnZqBLS_whFaQ-EstkTocgAB7IS8LCKjBef-pRI5Ju3cOT68Yv8GEr6zqlE2_Thb56jlvI2bAC9ycYnSRG95X5_4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=cfEFSZqkFD-tpSe0yArs7edwi8rs30Vuor-FA9ObipI1_BUfei9lmZhW1BOrMihp_9gu1jQ_eDs0GtBwEuwAeTwP23yJOvf9v1aYzytGyNM_FCoGyAcLNprFjQL1mUg6Jghd9ihsrM-yzNhURQpVHxy6-fnmjj4-uTkoQbPE8r8ECFxuO8iJrwA2DKQ8WXxlVzzDghD3akgkk9_qtZvcUB27SJShSYhmNo8bLMrrb7teoX2CMcK87SHzywENDkjqgWy19qk9DInALTYRp5_Te4T4HVTAsk2rsKt9KgxH5YmdqrLGNMrKyOTqi4_Szke2z2gzwdHkZTKK_N7JBOPCnCkEJf_DQ_nV3JcxXxuJh5zqEwZHnkso7p3zzDU2kjD34TbjMl4z_r9m_47EkUi6JNZBFBb2ydSlESNd-SMgjmi7QrIiipBDDr_EeEst9FYPDnzQWwUNyvQyarFv8gUWPMkRf2JAtlK0bckji0fZeIJhDMOy5nNS44Kfl_2tuZn97ept7-JBh4U-0dXTL1QgtVco5-bZnjdyu697pBO4VQ9lYLooutBFBxBk_yfxfqPD_cnO0vBceqn4iHPWspLWnZqBLS_whFaQ-EstkTocgAB7IS8LCKjBef-pRI5Ju3cOT68Yv8GEr6zqlE2_Thb56jlvI2bAC9ycYnSRG95X5_4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا
خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6437" target="_blank">📅 10:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=nn8VjQnTdCZVx31XLlIj2JVz4biJEHlZexkjMZRa6YgjcJU-aUc3Vz_2c7FE2ivEKTr1E99PHScorkf-HfcHczQACxXcmjPnQ0FKMTzaleXk9ZZeIi9xILoWR67amWeuOBG2nmYLpJRUHB8AiI0OmiJElVCfAGvfUgdkQVVf4B3EPdU2jvR_8VtOHPQsLjcX3A8qnan2DyDLOsutrmO8WxdP7P2rNF5HTKkBNZidM_fYm9d6RN6XxGRf2bITh2IBDQCga8CQPgtVuxTGe3IentCzfxJXJNvGS3J8BYHyoyqpQA38u3v9efWGytYR_Zou5xL4wsrRbLPu3mvHnjtixA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=nn8VjQnTdCZVx31XLlIj2JVz4biJEHlZexkjMZRa6YgjcJU-aUc3Vz_2c7FE2ivEKTr1E99PHScorkf-HfcHczQACxXcmjPnQ0FKMTzaleXk9ZZeIi9xILoWR67amWeuOBG2nmYLpJRUHB8AiI0OmiJElVCfAGvfUgdkQVVf4B3EPdU2jvR_8VtOHPQsLjcX3A8qnan2DyDLOsutrmO8WxdP7P2rNF5HTKkBNZidM_fYm9d6RN6XxGRf2bITh2IBDQCga8CQPgtVuxTGe3IentCzfxJXJNvGS3J8BYHyoyqpQA38u3v9efWGytYR_Zou5xL4wsrRbLPu3mvHnjtixA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساکنان سئوتا تجمع اعتراضی برگزار کرده‌اند و دولت چپگرای پدرو سانچز را «فاسد» و «خائن» توصیف کردند.  سانچز شخصا فردا به سئوتا می‌رود.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6436" target="_blank">📅 09:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6435">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ODrWwbcgvw0PP-yPCqC_bmGHJiPAdUdimOd5y5ePBNowgWpz9hS3ACJMsLhnquZID3ce5O3R1xpShUdwqHB0nkwTXkwVQJADiS8qKU5EHJig_Gbl2MOodbmUSL8PZn5Dm4jab_HX6PLhsnkzcrzz7XmEqIpc4hds_qmub6mXJN5tnn4Uet1IEiofRYT73r9ezY6YYIU9XV9ouuF0SZ9gOw7aPaHNOM5eK6qFkXw5hmjdMb9pLqmbO1oUnpYkkr8psd9xQKKVoXZESyIj9_icelNLvtQb-PUJbvWRDCHjpOUH8oGmNbBaKs4tIAu4l6ipQ-gBin5VXrp_lagy0T27Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی امضا کرد و خلع سلاح رو پذیرفت!
نتیجه عملیات ۷ اکتبر که خامنه‌ای میگفت :
« تاریخ ساز» و «ضربه فنی جبران ناپذیر» ، شد نابودی غزه و کشته شدن ده‌ها هزار نفر و از دست دادن ۷۰٪ خاک غزه و حالا هم امضا کردن خلع سلاح شدیم!
کی به این گروه تروریستی پول و سلاح میداد و برای این برنامه ها تشویقشون می‌کرد؟</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6435" target="_blank">📅 08:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iETYx0DtZKlpZO_TRz9k59CD99wZUC2pjV3JQNZhQfSm9shHZh1V6CzETISwBX3f6IXbg9CqS-7eRXPvop26W7HBip3DJeB5kGtPU3BZQvS_K7l12J-MB1JiIWKcZi_6r18HvBsKW0tw2WSMPuPTWAnN2q-bHNq3p-Ghlk8M9YzHfOJBhgR4fj30wtApbRsFDwhK8-7J5-KC8aM3VIuUm2cD5SMlKMS4lYARPJMpUN2K9QMINUkUWAOpCThyaCGVspTCK2qqvCZYO7nkyvbjXI41kHAMuaBehAs18zSXH_GRmCZ0MTeGwj5s1TehWtemZ6XpH1fcWhyPtg4X2AGFDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جوون‌های مراکشی رو اینطوری میارن کنار  مرز اسپانیا
🔺
در یک موضع شدید انتقادی نسبت به رویکرد دولت چپگرای پدرو سانچز، دولت ایتالیا خواستار تعلیق امتیاز شینگن برای اسپانیا شد.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6434" target="_blank">📅 01:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6433">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=ddpoPayZaMHfIM9P8hc5MG3cOBgA52l76CBapTZTzR5VWseQvNijKRxhMnCWHmNmGU487ziggeGQ-ce8jS9AjKFRebESmXmULoJBzHEVFXtES8kFPVmoVc0L-mQUO3Q-m0ofzZcKZuQysTwGnswCbY4nq_5k7WxrJhtVkyGgrmLqBxDkoteJEJj_nAbIYaVymihgvEcr9ctXLiQ8TgWG7MS_G7ubhQf4A6omhnTQ2Lh3IaJ6pkb5A-3eDZb4V-quqfDD0iUNUBhfYWyy6euZcIpwlb2chWJjTkRqnLuLo4Rgq6PaUMI8KHLwCDqwFQHiml8FPrDGhUNBpaBCRy0Qw1DPAJxuyFVjcuIWygSlo7dk-CIEbXYUhNhm44GR9zAnNeB-iJgyK39cjgsiT-81ZB0jF3-Izxc4rgasY0uAnh6ngZrUaHyrTxiDVP0-KW3h7eLZJov6OYTFRX6FOEaTIv9UsaYbCAOGMJHj4Sda9AJx3laJyQa8UmDHED7lQvoD0BCJxjUD9pkwY3NGLFQAQ3DFyuA_Wt8ZXukSRkB5kTMRMUIB1E4NE4MrStV919i0OwAwbro4WBRQzCQP8yr-8CAakHkdJvq8319orZpiyLosqb27T1kIoiN9rOGjWSQVOTEn9_c9Y8_Pbq449vQa1NymqU5xoI4I2624OcAwnrI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=ddpoPayZaMHfIM9P8hc5MG3cOBgA52l76CBapTZTzR5VWseQvNijKRxhMnCWHmNmGU487ziggeGQ-ce8jS9AjKFRebESmXmULoJBzHEVFXtES8kFPVmoVc0L-mQUO3Q-m0ofzZcKZuQysTwGnswCbY4nq_5k7WxrJhtVkyGgrmLqBxDkoteJEJj_nAbIYaVymihgvEcr9ctXLiQ8TgWG7MS_G7ubhQf4A6omhnTQ2Lh3IaJ6pkb5A-3eDZb4V-quqfDD0iUNUBhfYWyy6euZcIpwlb2chWJjTkRqnLuLo4Rgq6PaUMI8KHLwCDqwFQHiml8FPrDGhUNBpaBCRy0Qw1DPAJxuyFVjcuIWygSlo7dk-CIEbXYUhNhm44GR9zAnNeB-iJgyK39cjgsiT-81ZB0jF3-Izxc4rgasY0uAnh6ngZrUaHyrTxiDVP0-KW3h7eLZJov6OYTFRX6FOEaTIv9UsaYbCAOGMJHj4Sda9AJx3laJyQa8UmDHED7lQvoD0BCJxjUD9pkwY3NGLFQAQ3DFyuA_Wt8ZXukSRkB5kTMRMUIB1E4NE4MrStV919i0OwAwbro4WBRQzCQP8yr-8CAakHkdJvq8319orZpiyLosqb27T1kIoiN9rOGjWSQVOTEn9_c9Y8_Pbq449vQa1NymqU5xoI4I2624OcAwnrI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تداوم ورود هزاران نفر به خاک اسپانیا  اغلب این افراد مردان جوان و نوجوان هستند.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6433" target="_blank">📅 01:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6432">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=MUAEmaeS0W236oIvN0_PbYJ8d9TyV4svE5ZFmHhQMxzjpUZXh9XHZoIrpdKYSbHCk0N5-Lh51bBCb3AZekqy2yGhd5JYwb3kYsVDqGIz9CYmYaRo6xR2LSFgrotgIy1vMlS-_vBLa-g4eLn_rlAkeeAnXclIiy5tVirCBsIFcvDR3dSFeZVJgHG0oz01HXcnjD1jUinKAsXY4_0DuQfa2z3De3njZhe4zian9xY-j7Je1HBg-MR9PQ-eMszXTJhKFAwduhHFP_T8VmqL3fGg_4yJo5w1D1og5WT65FT9lKutD_t-t2I4xnFlI0JgAm3QzAqh5nDr6wDrOYv_KWyvzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=MUAEmaeS0W236oIvN0_PbYJ8d9TyV4svE5ZFmHhQMxzjpUZXh9XHZoIrpdKYSbHCk0N5-Lh51bBCb3AZekqy2yGhd5JYwb3kYsVDqGIz9CYmYaRo6xR2LSFgrotgIy1vMlS-_vBLa-g4eLn_rlAkeeAnXclIiy5tVirCBsIFcvDR3dSFeZVJgHG0oz01HXcnjD1jUinKAsXY4_0DuQfa2z3De3njZhe4zian9xY-j7Je1HBg-MR9PQ-eMszXTJhKFAwduhHFP_T8VmqL3fGg_4yJo5w1D1og5WT65FT9lKutD_t-t2I4xnFlI0JgAm3QzAqh5nDr6wDrOYv_KWyvzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حدود دو هفته پیش دادگاه عالی اسپانیا حکمی داد که افرادی که از طریق دریا وارد خاک اسپانیا میشن، نباید فورا دستگیر بشن و عودت داده بشن. اما اگه از موانع مرزی عبور کنن، پلیس باید اونها رو دستگیر کنه. این چند روز عده‌‌‌ای جوان از مراکش و از طریق دریا وارد اسپانیا…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6432" target="_blank">📅 01:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6431">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا چسبیده به خاک مراکشه.  خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند در Ceuta</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6431" target="_blank">📅 00:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6430">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oNP_HDVVlMo37V6fEyttLNynsysFjRXESiuKaSB0Hzc2fRRkeTHwH5QGWa0Grpi8Al6lEgCU3bPvqVSyP3TWEVaBJVwSMzJbxsQ-IFkoraOn3d90B12I84pARGZ92wT35TezlItDA9XJFILfnJ8G9xIkH-EWJHIodp5dle9-uHJ0bVAaUSPUpfYLUFkPYfmWQnzBTPDRWYJjvKuJ08B8YekUZQsRseZy5B04NdN8MoMjT-Hlc2DCHjj_IDzx9_JlRxYdB_cjxjAK9-ka-TTUTUS1scOc-npwaJkdqB4BAHQCVjwp2C0aeBTtTaLWlVuDG1b6IeccvBDBkHQKruuzew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکنون ۱۳ کشور اسلامی
به درخواست عربستان لبیک گفتن!
برای حمله به گروه تروریستی حوثی‌ها در یمن،
از جمله : پاکستان!!
مصر و ترکیه !</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6430" target="_blank">📅 21:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6428">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oq_xyaIqw2wewBmubmwiHURGH-DhT0WiNwLX9jkgODb2RLeDlsvIgK_lrWEg1D_dLoQoIDu5D_yV91EQvPTaC5nYfcyCbc6NTswCyM_o4E-6hhH9-2q5vFhrXwQxgmSJmXz9U_1bZW8iEDC7Lk3iPkignJwgmWu0tFCH8CDvfSooKLZLdYcUJZK4BZSMslh0hMpnJCyqYCAM_BbGbYLE3S2wRc4rjXlkfjvpUA6fsvNQI-Ro6adShlTmJaFjKAGTMqxxlp0Pdonb6P7_y34Z8lbMFB_JLZWkXCOHgjCecoUqodzc9DuL-oWIHlH1KPfHN_xsLvpomthB2fYWvJzSCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jZsMQggBBd8fRQkC1jtROAX7EIeKBaCQIvdSfgYtYNx-WCJNTQO87GiA2QaVLnLyjOa2SFRy0dtvWWWplikGeHYqn9cewrTBZwXNDNcVYn0q3itec7mK2zc1Q40C0edADY8WpCi-Tsc3YTaDZSWE5uz0U7h9rz1En8xrdCn30ro9qkgSNMr3unv8VEZdRfFG7PYry4CtjPPj-bapNbuvPDt_LaBeip_yRznnH4YdLMoqr-aDZg1kesQ1ow1MNPMYEj7Nfr7KgZbcYWKGO_U9cO9vXsqgQC1AR4rDbWaOc-IKddDrghvXXj6eHCe-40lhVTzZayLWkb_W0GBPvXxFEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا
چسبیده به خاک مراکشه.
خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند
در Ceuta</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6428" target="_blank">📅 18:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6427">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39130dc900.mp4?token=fr4GL9D55fIQWMSyDeuqy4LpiZdtg8iMaCK2aJav53jpNVr1Ar3_6GAvOFEZDm4EGXFZMOOSquNBPHv8TUMkXQeGAav4iC-j2IrUhiI4YfULCcW3wkn_byyJHeMqbR33blJumLKr_rBRkrbUZiELKAriRRYm_eLdXqf3ogym6ZXq7McLFZy491KB2zXXR4ewfVz8lJQlLI9VFh_RW3OyTDphu75NM6llCh0TFx-VfheUfl_rak5Ugy-_Tldnfh8I1RkjpBen1ED2I5AFEdVEZrl8hd2YVX5QvsNFxkOCQtqnBW9IkpusEKJ0OyE1kelpYefzirKDEHYrl3fDOK7Y_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39130dc900.mp4?token=fr4GL9D55fIQWMSyDeuqy4LpiZdtg8iMaCK2aJav53jpNVr1Ar3_6GAvOFEZDm4EGXFZMOOSquNBPHv8TUMkXQeGAav4iC-j2IrUhiI4YfULCcW3wkn_byyJHeMqbR33blJumLKr_rBRkrbUZiELKAriRRYm_eLdXqf3ogym6ZXq7McLFZy491KB2zXXR4ewfVz8lJQlLI9VFh_RW3OyTDphu75NM6llCh0TFx-VfheUfl_rak5Ugy-_Tldnfh8I1RkjpBen1ED2I5AFEdVEZrl8hd2YVX5QvsNFxkOCQtqnBW9IkpusEKJ0OyE1kelpYefzirKDEHYrl3fDOK7Y_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6427" target="_blank">📅 18:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6426">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=LUyLO6mOWrJBRZejphBap2oDZfQYNwZQ5_DO9rpsFir_3mdd3KQA-u7hsiwQSu1W3CA5V30ldbED0ptxIzYMXJhwQHrg3jvfgotPv0ly_6tsGiaO_yQMx2s4_ayEz8l2CbRs6L7UpLJw_aXhbEgEf6U02zAeJNbQ6YQOR5FMAoqc-bg4ffgGj3VDgIpfwU5vyuz4OynGYJwWDxNOmtdSqxeoS9tkf6KmAedRoiL22NbzAUyl8l6Dz44pUy6homq6fBZFRuUyWEMSUpZnm5nCwgDOUcDDSvaeSIDv37nsqO3pqc58_op1d_18K4ogTeVMj8BG5P-Coq0curYRvbg4ZoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=LUyLO6mOWrJBRZejphBap2oDZfQYNwZQ5_DO9rpsFir_3mdd3KQA-u7hsiwQSu1W3CA5V30ldbED0ptxIzYMXJhwQHrg3jvfgotPv0ly_6tsGiaO_yQMx2s4_ayEz8l2CbRs6L7UpLJw_aXhbEgEf6U02zAeJNbQ6YQOR5FMAoqc-bg4ffgGj3VDgIpfwU5vyuz4OynGYJwWDxNOmtdSqxeoS9tkf6KmAedRoiL22NbzAUyl8l6Dz44pUy6homq6fBZFRuUyWEMSUpZnm5nCwgDOUcDDSvaeSIDv37nsqO3pqc58_op1d_18K4ogTeVMj8BG5P-Coq0curYRvbg4ZoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6426" target="_blank">📅 17:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6425">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
سپاه از کشته شدن سه تن از اعضایش در جریان حمله شب گذشته آمریکا به زنجان خبر داد.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6425" target="_blank">📅 14:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6424">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qdQpZUem2V87WDpE5ut3c7MckUpW9TqcWlj6nnKhUAbqz10ikuBwVzDPzFqUVJs91GYrS8h9MkvI6XdEX96EUCy-MGXU-33Mkzt_86lXaHsbzS-ghGN6SY7RSM_b7dy_6fHCbnUl4TovjJCc-aXNyNTCqhAnSdpH3Uga_LW2j6_cHNpVxEB9robwy7bRsnnVVwortmmLgjrmb56bCLCXVITZHq9zjO7cW_gClfwrRgIy4Dk9ynylh2y8yVqSTeXBUAF5Dmh96J0yZvae-Fh8l9NvaiwlO4STRGCNoQAsQW9LjAqPC59ULKWwDGQH9Vpp0CsGXOzUEydxFXGUNxoL3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو رهبر شیعه، هر دو مبارز علیه آمریکا،
هر دو حامی سرسخت فلسطین
هر دو خود را پیرو مکتب حسین معرفی میکنن،
هر دو اتفاقا دشمن پهلوی،
هر دو هم در غیبت به سر می‌برن
و پیروانشون در انتظار ظهور!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6424" target="_blank">📅 14:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6423">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،  ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6423" target="_blank">📅 11:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6422">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mE46xjYQptlpH9RfLEXOOA0b5aZwDqRe_nfOJnET-5vWvNHE4YzJLvzmd5ZrKCzzdNUUA329sr0xcrBC6Ur_pYeFXcJ7wYxH4y6HIuhKjg4xsAAQ6nladnW25NXTSrnQwaJYWlcfWq9zQDdHs9RLW35wiADynuAyxITNokDQLHcHpSVRK2Yr6S1KhHHMH0EB0RF2STGYM2ewofWp0ttpfOa27XUI15w6c237CfQ4SG16NLfDspQo1Eja0ITfV7pwFAp8YIpZg-RC5XjAfZKNluv0VU12EQi-l4za9_6kzup0dJJaee0Li-SoiDhF5iJtNbWCOT7lV8tKMYCteKahwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جاوید نام «امیرحسین صفری»
که جمهوری اسلامی دیروز او را در
اصفهان اعدام کرد،
فرزند شهید بوده.</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6422" target="_blank">📅 11:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6421">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=MAmzjEuG4vgE32rVWwvqquNCZCx7VQmqIxI3fId_6zYmcaBprnmES54V-hKBZNISMXkIcVjlsM-3u7_lgDRjQhnhIdJGEmFG7fd0TiRTZqgsF-Q-8xcZTkIuDB6zh0kY98xlTnd69x4fNJyveOCNacFLLiAhhhVZu0_9N1iSza_b3JooRLySKqpgKCS08sPlzuehyaDdJmp6UyqM67G2g4dbygB8REEAnSE-nNIln7H7eV9VkipxgRc_g8zNO-ADHs8Ki4L2vXVxp0RARrgoc8ZOBOMQ-gVng4OjxqOZgHqHtkY18ux1GbHLZhKMhJ2xC20BjBnll21EdUxSTllVBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=MAmzjEuG4vgE32rVWwvqquNCZCx7VQmqIxI3fId_6zYmcaBprnmES54V-hKBZNISMXkIcVjlsM-3u7_lgDRjQhnhIdJGEmFG7fd0TiRTZqgsF-Q-8xcZTkIuDB6zh0kY98xlTnd69x4fNJyveOCNacFLLiAhhhVZu0_9N1iSza_b3JooRLySKqpgKCS08sPlzuehyaDdJmp6UyqM67G2g4dbygB8REEAnSE-nNIln7H7eV9VkipxgRc_g8zNO-ADHs8Ki4L2vXVxp0RARrgoc8ZOBOMQ-gVng4OjxqOZgHqHtkY18ux1GbHLZhKMhJ2xC20BjBnll21EdUxSTllVBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته می‌شود که در جریان حملات شب گذشته آمریکا، ساختمان «اطلاعات ۳ پ»
اهواز مورد حمله قرار گرفت  و ویران شد.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6421" target="_blank">📅 11:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6420">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
سپاه:
به حول و قوه الهی، امروز مجازات متجاوزین اعمال خواهد شد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6420" target="_blank">📅 11:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6419">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mb4tXNOFKMqLXjI3-YCguh0-N2_LVAl8PkSmczUiZNeCQFdr9olm_glaH8_OsBfP9UxDM3mXIUL3kEtVWVZZom416jRVCkAxeNfVCs8Xf7Qk2HQWbrUJBFI4N_-ZsBCdsgRr1WTEHtbgEULBqP2bqZ5V15DrpJ8Sa34LxkikJpl-D-r1MMAHYqGans2A6a02zGDfhUzKIGuh7BTSF5HvAF723V_AXyoYhufiBrjj-XyxlfMjFI1uZ0tM---WmMcYd9zROTQ8V8EpvI7w7BhoSmXb5T7JOe2hta0GLMc54EVWmSk74BPqVJuCp3XiI-posNVj5rletGE0R4wC3Do-mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
دیروز جمهوری اسلامی با پهپاد به دو کشتی حامل گاز مایع در مصر حمله کرد.
امروز دو تن از مقامات جمهوری اسلامی به روزنامه نیویورک تایمز گفتند که این فقط یک هشدار بود.
(که علاوه بر تنگه هرمز و باب‌المندب،
می‌تونیم در مصر و کانال سوئز هم تاثیرگذار باشیم)
🔺
صبح امروز هم سپاه بیانیه‌ای صادر کرد و از حمله به دو کشتی در تنگه هرمز خبر داد که قصد داشتند از طریق آب‌های ساحلی عمان از تنگه عبور کنند.
🔺
دیروز صبح هم به سه کشتی در تنگه هزمز حمله کردند.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6419" target="_blank">📅 10:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6418">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rvLvpsNLLXvb6dLQePavUQBf7i4mpfsj_KNGm4KEswErB3ZebxbE8m-EIVRU9tPmxk0dTtFd-rSPqRvEKovcaYJSuois3wHvFuynovgs4jSNpweqAj6B56ZJPgVFeATGvIut8Z2-jVxKkSrXsyFf5E8Wp_h2zh_iJ7W5PCHVlWw7vOhmrNd7Awjk88gOV3aIIp5Ddm4fmmPKrMOlRZ-r46OCzUouoUhZpP95bI-pPVxLTGcCFp7GyCATTCjXyAn6LPNdsIT-GevF3Hw0fMRab4y3YQPmO0ETGJcVMzB2zTfkm3QGWccI4LD9SA_Y9tzcmyXIsQ5VKM9FJ-WsVHQyLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز صبح گفتن به سه کشتی حمله کردن
امروز صبح به دو کشتی</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6418" target="_blank">📅 09:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6417">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
🚨
حملات موشکی آمریکا
به چند نقطه در اطراف آبادان.
شنیده شدن صدای انفجارهایی
در قشم، بوشهر، کازرون.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6417" target="_blank">📅 04:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6416">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
ترامپ : ایرانی‌ها می‌دونن که ما امروز شدیدا بهشون حمله میکنیم. اکنون نوبت ماست. ضربه سختی به آنها خواهیم زد.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6416" target="_blank">📅 23:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6415">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h58SSLKnTXjEwp_NumHbeC_VPHF1YCo9TXqfz9sm_gVOjHMG2GL_LQZkx0OvDDlLZOPMvxFzrxD2-tin3rVC1JROBwRsXtbss94dUXIo4DkXX7Zk3zH7KOwyTou49LoAVm9y6zOIAQjCTyFgLpCXKc7y-W4M1VH6LoXh-IEdSwubtrBTLpnF7Qw4TgoSCozJVdXGvzu0ag92oPRYHsuJAq94cIcX7SjAVU6arfQjG9NxWxwuOT_qDU8-HQk8CVe-_dRQJV0VL-Wx8njPW7AOwhYh2Mo_HXAmLR9PK--k31QMagf3OiVbEL4i6vVsdUpJo0n2Xap2C20miZpmVJsF-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تعداد تلفات گروه تروریستی حشدالشعبی به ۸۰ کشته و ۲۷۰ زخمی رسید!
ایالات متحده و عربستان شب گذشته در پاسخ به حملات پهپادی گروه‌های وابسته به جمهوری اسلامی به عربستان،
به مواضع حشدالشعبی در ۷ استان عراق حمله کردند.</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6415" target="_blank">📅 19:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6414">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=u7upMfX1E4hXA5sNZbH9MPZseef-5TqLgntayvo-2jj5y_Znolm_7Jedti2ttL5k4PtOvGwHkY3LFPTL7e9i0OqRnRQChlv4n2ufY21FC9UPcHjbpc_eSUmGmO9yiPpzgZRG0FKc1Zp3QMF6v7CGDcxK8yrH4HlTF1bf24QRYnCrhELnmG_fSuB0CXifs87Up4a5mIBktfZMg5CfgV0CxYCoo5ORfFHRhi6C0XNvD9GeNyYgKWvs-X3aUlDa9mMW4sbYg2lKfaEvMJp5Nria1mrFZP6ZJU4cmFkF41NSuj4w7wsv4JXQm2a0x1_lGLgGTVGEniF0vlO6aUPAA81hLabsy7omE6YClRlDZn8aeMIOJAchedgccTlmzmxr8v91_zHbgMqhmRlkOBYyuQS4zOisXFG1IUlUHu_O4y7ZdYnrB2bSQ6QTVNzMOJ3WBlhybT3xtZxmyMDJwK1Tl3duLqN37ocZFFckGizZEz9sCmFiLDn5cEgiSqMk5jBI902Y5OicVDa52BA3djPVXOtWa86axpWjx1Jtcx_BTv3PdyHRXln3p8tBuhXslL1A3RfwUEgOVPa_47BFm-B3D9k70J07NcWaq-W70oHkfh_RulpdA9NSdy5rl4SkTFwF0dq5v13QmrIno-bpCF3CZUMSNJtS9xQpc97JfhpVuZsil48" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=u7upMfX1E4hXA5sNZbH9MPZseef-5TqLgntayvo-2jj5y_Znolm_7Jedti2ttL5k4PtOvGwHkY3LFPTL7e9i0OqRnRQChlv4n2ufY21FC9UPcHjbpc_eSUmGmO9yiPpzgZRG0FKc1Zp3QMF6v7CGDcxK8yrH4HlTF1bf24QRYnCrhELnmG_fSuB0CXifs87Up4a5mIBktfZMg5CfgV0CxYCoo5ORfFHRhi6C0XNvD9GeNyYgKWvs-X3aUlDa9mMW4sbYg2lKfaEvMJp5Nria1mrFZP6ZJU4cmFkF41NSuj4w7wsv4JXQm2a0x1_lGLgGTVGEniF0vlO6aUPAA81hLabsy7omE6YClRlDZn8aeMIOJAchedgccTlmzmxr8v91_zHbgMqhmRlkOBYyuQS4zOisXFG1IUlUHu_O4y7ZdYnrB2bSQ6QTVNzMOJ3WBlhybT3xtZxmyMDJwK1Tl3duLqN37ocZFFckGizZEz9sCmFiLDn5cEgiSqMk5jBI902Y5OicVDa52BA3djPVXOtWa86axpWjx1Jtcx_BTv3PdyHRXln3p8tBuhXslL1A3RfwUEgOVPa_47BFm-B3D9k70J07NcWaq-W70oHkfh_RulpdA9NSdy5rl4SkTFwF0dq5v13QmrIno-bpCF3CZUMSNJtS9xQpc97JfhpVuZsil48" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عروسی، طایفه «آل العرعیر» -  غزه</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6414" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6412">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U5X0bRscK_AZ3KMTK9s_lhsanAjMs5wABfv_a3HMA7Z1N-6jIEuJtkUth49cq31TVlkyTT9lTiSrfc-w1eJ8M8i17BkMlGVAFQZ3NjhT-dxnsstn80iMTCzNemixLHZ_mqoLqcKkSz0X1QHwOWjdDGPiwNwq8w4hcBIMDpDeRvjkH--rLSsJIjw1x4400XxPtWaXVBb8kTHPpJUds7O-zBxZwQtyTjtQ61z1zqMGTPw8W_25s_KAD7A2N6phMsczS7MnPo29ya9E_mnub2UNLd8CZwjCysMYvAvaTljiRHOykvKRg9w7NHf7wY8tPT26T6qubG2vL5nv5hBbxIvPbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s1DM9kQHHVSaZFY5Il9I3-75vvg2H2tn2-YWZ88k8V4HFyyTaHYndKGi9soA1RjLNz_IhomriwHO43jfNNny7tZqKLpyP15o6Di1o8p9l3JoVQEmDoBpE68nZj59P92SV96qdQVuhI_IopFyVmRUjzoIWff8VUuVKap23HVM6OEMeua-BxurAreSnV7_PF7oWcE8-u4CreQvkEIb23Ze7xMOLp26tXNuKvaL5QRZoDUWAAxSi6KuWZHWldE_K_S2nt8jw-j9zIPQiWZb-_amdTN_uYOrIJn1-yUqQo-IUjOBrWqhv7ug63JFD6SA3ksFtO0hkspecpbRQ8QPQKo8og.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
رسانه‌های حکومتی از کشته شدن ۴ پاسدار در جریان حملات شب گذشته آمریکا و عربستان به مواضع گروه تروریستی حشدالشعبی در عراق خبر می‌دهند، تصویری که جماران منتشر کرده اما ۵ تابوت را نشان می‌دهد.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6412" target="_blank">📅 18:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6411">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
وزیر جنگ آمریکا امروز با نتانیاهو (در واشنگتن) دیدار می‌کند.
نزدیکان نتانیاهو دیدار دیروز او با ترامپ را «عالی» توصیف کردند.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6411" target="_blank">📅 16:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6410">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :  ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6410" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6409">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/436236e24c.mp4?token=pS9V7N5SoMpvqS-O01rRZtve68idN5MJCgAScVQaQrlm9RRuzUUidw7O-n3sniiJNwE3wvo2MfnqR-KxPFQwn6LF_eO8ujvmw0QGTpJIiuqv_O9mUtPiPl2rMdHamGq9X23QcgRw5DSyt0qU88Rso4pYSRUw82YU_2cEx7VbUAsvTxD28v_Cn6cKsJPHqlDvxsio9BYDKjRs_dDTzulK_s9i3mwfi83grsnsr1Txhh-hi2EYhFhSSUP_CPKo5a-3QX3Uw9JzsemWCsxoau4m04W-FykH2xXD6HdNCnGfQ7gwS8S8s9NxyxPbLrb3XoyLBNCXIjLz6dYtbDswd-IgyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436236e24c.mp4?token=pS9V7N5SoMpvqS-O01rRZtve68idN5MJCgAScVQaQrlm9RRuzUUidw7O-n3sniiJNwE3wvo2MfnqR-KxPFQwn6LF_eO8ujvmw0QGTpJIiuqv_O9mUtPiPl2rMdHamGq9X23QcgRw5DSyt0qU88Rso4pYSRUw82YU_2cEx7VbUAsvTxD28v_Cn6cKsJPHqlDvxsio9BYDKjRs_dDTzulK_s9i3mwfi83grsnsr1Txhh-hi2EYhFhSSUP_CPKo5a-3QX3Uw9JzsemWCsxoau4m04W-FykH2xXD6HdNCnGfQ7gwS8S8s9NxyxPbLrb3XoyLBNCXIjLz6dYtbDswd-IgyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :
ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6409" target="_blank">📅 15:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6408">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،
ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6408" target="_blank">📅 15:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6407">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=HC48bujtiNg1KA4l2-23cdQ-Sld04CbpKzquRzwcFdjWnUuPgB3y8j-WQmWKyWBGTNfvgh-cfT4gKmJ6YX-xaahpGTlDB43p8VC8I03XiTdRbPcCyJfYiw1-hDyDAAVeg-T02YfYH_kiM2uy19pjeXuf1GG2wQnGxudALoi7T6jC6F0ouL5At0Hr01pyPcZg9qhi88mR5B_2s4S8VXRtnh7RgJEJuUVT57-Bef21w2SuwALJvGjA2iZu42XVGNKWCY_aM6ssDLUJ_qWHnExCoK_WYImdytyfYlhS9Jqpm4IKZWr0oDdBx1hC7zccH0EQ1_wSV3R85O5wMD3MWReaZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=HC48bujtiNg1KA4l2-23cdQ-Sld04CbpKzquRzwcFdjWnUuPgB3y8j-WQmWKyWBGTNfvgh-cfT4gKmJ6YX-xaahpGTlDB43p8VC8I03XiTdRbPcCyJfYiw1-hDyDAAVeg-T02YfYH_kiM2uy19pjeXuf1GG2wQnGxudALoi7T6jC6F0ouL5At0Hr01pyPcZg9qhi88mR5B_2s4S8VXRtnh7RgJEJuUVT57-Bef21w2SuwALJvGjA2iZu42XVGNKWCY_aM6ssDLUJ_qWHnExCoK_WYImdytyfYlhS9Jqpm4IKZWr0oDdBx1hC7zccH0EQ1_wSV3R85O5wMD3MWReaZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاکسپاری اعضای حشدالشعبی در استان دیالی عراق که دیشب توسط آمریکا و عربستان مورد حمله قرار گرفتن</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6407" target="_blank">📅 15:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BfUhl5-yXKosRH0fdXWrtMQU1-ZnwA8fgtLdr1PQlrurmna2uyiqo_rBIJ4Nd_zzwOQe2qCfuSy5YFUDxRbwVa6sUWcFETzlHnqk1QPRsyygLgRK3z3w6qNDOg81gRWg0CDC1zy0dTjPSbEfmklcBc2_b40c7-BNYZ-4CIXEMlkCyQ7slxMrRYzc8b167WSlgvQG7nfL5qEsxa-A7EvFbXwX2Vw93o8LuBYvTeX5Ph93TpH2H7hW6bQSPDe6sHsair0NSmBc3nJboQV93DS6sOjR2Rwx-0hff58jC_tg0tb9eXE2Mo_attKnSGWLxgssV5SLnkyXEbSkq8zg8vSzKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز وزیر دفاع اسرائیل برای اینکه جمهوری اسلامی رو تحقیر کنه گفت که حملات این دو سه هفته اخیر، از خاک اسرائیل انجام شده و جمهوری اسلامی
به همه کشورهای عربی حمله کرد
اما به اسرائیل حمله نکرد!
(یعنی از اسرائیل ترسید و بهش حمله نکرد در عوض بقیه رو زد)</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6406" target="_blank">📅 15:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iFa56gt0nudbDIs_RwnNkOaW4Hf968g_q4nv9QrspOX0_2DI9a5O2Yi9lZBf1ga8W76SZcR8Dl2nFFby9bowexPcXA7gCDDAsJwcn65pqfER0KnjsoZkA2UuI8-i94FVVwDWUb0n5Rs84z_wt-mt8ViajiO2_eSCepKLHi38EzcM86WHuOOwcKz20--UICPVhmvdsFMKYcitG30cYrCWIm0lAQBp_JuqxetSCHYAuPplVauz4p6IABsD607QzlG5ZmuoHrFwIMNOR8mmemIwv7MYyWK-WizMZFn_UXCFebVYdz5SwCetwXiuvAAfbKxVuTeJskxw59TSkFRgFSDLjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقتدی صدر با صدور بیانیه‌ای به شدت از «سپاه»  و «شبه نظامیان افسارگریخته» انتقاد کرد که از خاک عراق به همسایه‌ها [عربستان] حمله میکنن و موجب میشن بقیه کشورها
- عربستان و آمریکا - به خاک عراق حمله کنن!
این داستان دقیقا همون وضعیتی است که سر لبنان آوردن! از خاک لبنان حمله می‌کنن به اسرائیل، این بار هم برای خونخواهی خامنه‌ای از خاک لبنان به اسرائیل حمله کردن.
ولی اونجا مسئولیت دست آقای «املاکی»  - ترامپ - نبود، اونجا اسرائیل بود و چنان درسی بهشون داد
که خونخواهی و انتقام رو فراموش کردن و «آتش بس» در لبنان شد مهم‌ترین و اولین خواسته جمهوری اسلامی!
سفیرشون رو هم از لبنان اخراج کردن!
در هر جا و هر مدلی، تحقیر بشید
خوشحال میشیم
✌🏼</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6405" target="_blank">📅 14:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6404">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
صدا و سیما: دقایقی پیش نقطه ای در نوار مرزی پیرانشهر مورد حمله هوایی آمریکا قرار گرفت.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6404" target="_blank">📅 14:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6403">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=vtAWBp5SJjUwkiKcC9Zou-zNzILQN1kFZoBWS2Kdz6JnDQo9yoTRLmGXeWHJ0wocKGL9i1pmY49dLrAB19AtLbj-aHsqVxOpDQLQMlwNqOBN_nVvWv1mGdc7300oBJQym0ysppB_Am73KMRCQJVGpZrEwoRCrXU16UnOQ8aHkIy75XF1R_CiwtCqmTiRBhvkOlruB_CuKlpmQq_THu8QqilhN_evnvs0NFohLrJfqm5s2bSi6YzTsutvHsXlNbt8RK7m4B6V4lmTAbrFCNcScahGijJTYqw98Ov7vCLmB5mHNIrdUUj1yjhdbYLAIpOvD1LgUivSpARgha0sqa4sqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=vtAWBp5SJjUwkiKcC9Zou-zNzILQN1kFZoBWS2Kdz6JnDQo9yoTRLmGXeWHJ0wocKGL9i1pmY49dLrAB19AtLbj-aHsqVxOpDQLQMlwNqOBN_nVvWv1mGdc7300oBJQym0ysppB_Am73KMRCQJVGpZrEwoRCrXU16UnOQ8aHkIy75XF1R_CiwtCqmTiRBhvkOlruB_CuKlpmQq_THu8QqilhN_evnvs0NFohLrJfqm5s2bSi6YzTsutvHsXlNbt8RK7m4B6V4lmTAbrFCNcScahGijJTYqw98Ov7vCLmB5mHNIrdUUj1yjhdbYLAIpOvD1LgUivSpARgha0sqa4sqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا و عربستان شب گذشته
به چندین مقر گروه تروریستی حشد الشعبی
در عراق حمله کردند و تاکنون اعلام شده که ۳۲ تن از این نیروهای وابسته به ج‌ا کشته شده‌اند!
حملات به مقرهای حشدالشعبی در ۷ استان عراق صورت گرفت بصره، کربلا، نینوا، کرکوک ،
دیالی و واسط.
در ۷۲ ساعت اخیر حشد الشعبی بیش از ۳۰ حمله پهپادی به عربستان انجام داده بود.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6403" target="_blank">📅 11:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6402">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=Ue10DFUvDo6hsOH9DM1hgi_OeDIXOX0B78HMlKvv2CuAkLRMCPkrPas3dO4edgFXMT9lWicNKApgt01IMy_SptuT_-AvPZmxSqTxYkGQCTLscIqtSDppL5v9VJEySXmGAXLdG07SsZvIsk8YWmBcWW2HOd2IULCo9cJ38PHiREcUW1tK_d4TlzVt2hxGoQPjkMZzdh33rcO8TvYNYRLN6Xpdgl1zrxfvtTKDjssXpxlna9cTMD7D136v4RwSEIIsHLCU1ovG5ZKzSL6_-NsEGYSKv1u8RIZFZtG54ai84dYs18z4ncZEFKKMTWMxRsB4l3u3_hsKuUpwir3ywCSBdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=Ue10DFUvDo6hsOH9DM1hgi_OeDIXOX0B78HMlKvv2CuAkLRMCPkrPas3dO4edgFXMT9lWicNKApgt01IMy_SptuT_-AvPZmxSqTxYkGQCTLscIqtSDppL5v9VJEySXmGAXLdG07SsZvIsk8YWmBcWW2HOd2IULCo9cJ38PHiREcUW1tK_d4TlzVt2hxGoQPjkMZzdh33rcO8TvYNYRLN6Xpdgl1zrxfvtTKDjssXpxlna9cTMD7D136v4RwSEIIsHLCU1ovG5ZKzSL6_-NsEGYSKv1u8RIZFZtG54ai84dYs18z4ncZEFKKMTWMxRsB4l3u3_hsKuUpwir3ywCSBdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب چرا همون موقع نیومدید از تفاهم نامه دفاع کنید؟  این تجمعات شبانه دست کیه که هم دولت و وزیرخارجه ازش  ناراحته و گلایه داره و هم سپاه!!   کی بهشون یاد میداد که بگن «بزن» «بزن»؟  کی موشک میزد به ۳ تا کشتی در روز و توی خبرگزاری خودش (فارس و تسنیم)  می‌نوشت…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6402" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FnBDUtHDOQno--0WCff9jcPkYgMmjw43qA98rlE_zXvaIiYH5xX2Y9zTNDcLfBQEobnFuvf2n71-xT7peqbOZJwtEf7PFho3NNJcWMBRvsXnj-atDi5HXIKEK8y1MmNc-G9g0r12E6tjGhCYLM5eHhc9FdIv8ud16dCLJZa0Ahy8hFwFTpSorkSACn1a2VKyZgldwGbi5e-0vxcMta59RZTat4RpCacMYH7ARx66zGGdoHca-aWFdihsXJTyRV3Mfaac5dFzC3Jd1OCGp_kVVJhFPE9zKs2MS0rDIq3jp91sFXGLRAhabtILlGi4m0XvD7LOrr-IGdh--f9S_3jf5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب چرا همون موقع نیومدید از تفاهم نامه دفاع کنید؟
این تجمعات شبانه دست کیه
که هم دولت و وزیرخارجه ازش
ناراحته و گلایه داره و هم سپاه!!
کی بهشون یاد میداد که بگن «بزن» «بزن»؟
کی موشک میزد به ۳ تا کشتی در روز
و توی خبرگزاری خودش (فارس و تسنیم)
می‌نوشت : «به تیر غیب» گرفتار شدن؟؟
مگه معاون سیاسی سپاه در یکی از همین تجمعات سخنرانی نکرد و نگفت
: حملات آمریکا به ما «واکنشی» است! یعنی ما اول میزنیم و آمریکا پاسخ میده.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6401" target="_blank">📅 11:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6400">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
سپاه ساعاتی پیش از هدف قرار دادن سه کشتی که قصد عبور از تنگه هرمز را داشتند خبر داد.
همزمان با سفر نتانیاهو به آمریکا
هر روز دارند به کشتی‌ها حمله می‌کنن ولی به اوکراین میگن حمله به کشتی‌ها خلاف موازین بین‌الملل و  حقوق دریاها و آزادی کشتیرانی و … است!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6400" target="_blank">📅 09:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PiHZjzDHGzXSV_lCya_ZEi3-D43Km4MVOBRUhnfctIfzb2spoOvJNakGn3RQdx3KgPdqcoWG1fUdkOnNMcTcaczvN_XnvlL79O4a7II30L5iaxredHC2-8K9eGmrWqpdDjXri8Eb1yhhlOkx9c2-gqLKSbG96aoV8PtfxhUTaaqhce-ygRs2JFiwrY27NxXKzPVa7metM0D1RrDtnWbbCp48xQrXSaG8ZkZA8hq-ndA5d9HTzFvlhOoo4U27XIZg4coZKYKYC5kUxDUM6B2MEB9IL6zR1ARZdug22MnsvyDHy1nOFv91bE0tQbteAhoxfGMVUOxVHHkrYCnwdZa4Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دائم میگن اگه جنگ زمینی بشه دیگه قطعا ما پیروزیم!  این تصویری از عراقه و نیروی قدرتمند زمینی ارتش عراق!  نیروی زمینی که پشتیبانی هوایی نداشته باشه وضعش این میشه!  فکر میکنن سرباز آمریکایی قراره مستقیما  بیاد با سربازان ایرانی بجنگه. بالای سر اون سرباز…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6399" target="_blank">📅 08:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R_evM-onLORWggVlYxfULLxiOOn5SXRPnqQ1izQS9U0k9dT4q26Ed1NDouJrgA80GMPsG1PWKu1XlW74kx_mSGplFgP-zxmYKhFFreCrhTi23Tzci9s5ivYZHua1_HFM2w4hvp3eKDRNHsVRud7bPy05T-qJG80BF6hoOpWu1IhhuJQfluogXk2WHux1ptwbsdnlGS1SvMFnfDxe2fztdDsFyXeCnwND2EBhaSwXMxel0rSvE2e88m0fTrNybRj5JC9tdjiADishUGL_nirUIQhs1DPrKg01IBLq9zzwPMNGG1XwSV5P9x0Q2N3U7SLWI0uvFesxm_W6pGHkojcbZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست! ۲- اینکه جزایر رو بگیرن،  اتفاقی نمی‌افته! جزایر خودمون  رو میزنیم و بعد پس میگیریم!   اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6398" target="_blank">📅 08:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6397">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست!
۲- اینکه جزایر رو بگیرن،
اتفاقی نمی‌افته! جزایر خودمون
رو میزنیم و بعد پس میگیریم!
اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6397" target="_blank">📅 08:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KSk7H372tjIpLtfKBP1aMm35eeDeyuH6lh_FnuuhBBl_25FBFPAfDNRRC7JeZfsD3yid5csWqJqJfD-rN6TtIXDQ6lt7Ulg7lqF97XsBRrgWpkmcbOnenIeorKRR-hnBCDtZroS6a7X0u8RqJcgvOwY0NVfhFHnX90ttRI8twHmwJzGtf9ZZE5GIBteGgoJ8vDIG0US_9oLsKuEoD2vkFr57URlg5ErFZsT3LQSi53XUYmrBryMM2UUViSHiCtIV7zjO-PZwcam17mm32ENRcFAhIaDwzX2h8tymeMR5eUWEbpBLjpKF7nrth42cuy0Tqa3sq3--J6EgeHUohZFdRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۱۵۰ میلیون دلار
هم براش هزینه کردن</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6396" target="_blank">📅 21:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NLx1R_UTvSN6A4wDn7jlDtGWioe5P_iMXBjtuBG9uMH_epk8szFT1_2jXGCx1FpCb6yAIWz4ndJRrGu6ozv2KOBkKwB7eyS9U2cQFyH9w4wV33lSRd3-oAMTdq9GYicia-ibHAnY7upN2Mvlb0aT7718ldDt7yTRJ2qIQJsyBcr1AGTHpiDdKH-me7qYusU2whbQUyzhtCMm533EXdT-r8zpazSzxsJBGK7XAmSW6vLTObrXIBbzL10jeaymZRu_O6B7JNf5NL-c85I5Si_jkOghkMGBInCkGMe5gYM4kkqXbUEmF4W77x-AIcFuiVdZUNq6tFj1LwV9GePSak4R4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ag6dS7_2MrpcJ3fBDDTqR6e2UrNqvFROtgYp_3NzaTp3CcrFfN1K2r2GJvmil6TUBkS6uwI0aFPinf_v21tUmtGdPBhscj0vebiF9dBghToB4Do8gTBAJqOvUYitrWYOdS5xZoa5pN56v-_xr0Y-BLAHG2eCpQsnMKTexHRujHkjX5abwTW68LHtaSfW0sL571uO2gEieVyOc6_R_BtQ5LtAvI310Lxky7v5E9Cu4FwlgeKKkXGTYGulNoIgGRzoWql8HzEnak8YMrTeQBe4vnO0ldDfHcPIOMCGBCKCS5UugbTfW3Lav69yKfxthqbYhJ3hgUb84bFnELscDs4p8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N7iW41_pUQrraCmAt-8NJPyr3zolqP7ylO5K2XX9ZkOBgDV_3EzVfWphuxTJsKoCkRMesVacSujzLt8rfaRKdLe48Tf_i20ZI5yLGjfO1RALgz730TXxcockb25-qx-DY3fQcCqAlqpv_Xvcg6h0DkbW3u50ukw4QTFtNG4XhZrdQyAQ2yQTXw4TfegyctNmbaS3nRSoJXxai_Qrd1wsLLmdLv8Lb67CAj6IaSUt3_18eXWvpZIUYTmG1pU5JpC9Zc-ZIBr8FsFWtXasudVkqaaTMN828lW-LM5Rf6zx3NgHEloUiN3x_NVln-CWj37V2xwUrhFEK2qwwWFQoUORDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kbkUhPWgyD2g8GQcOFdShKZPuWeYJPck3ioweDjRZyj6ZMaJhuspSKPuLhPzr1AhdGc6y6jVkg1QGaZjqyOVAGUp58Kq762Nqfrk_NIlAVWVYIfxDcUXVz-7Qn4js69RHdIboaL2xNDXz-7xJb_cnPiz0Fq9GW0UUkqT6ZE5ra_OF04E3kC75hiqak8eqjgTIzFyoHiSQ1pkigHKtG43qTv1ufgSESKdORF82ZHxnDyTPM7Ij5JaI-6jeMcWepSQw4LEE314yhm2keu2AVMjrM7gm2gN4d6c6b2Yig_YqHz_oBxExGRGsQzaGQ8oX7s04GhHpqlwuRjEfOv1cTPb4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری از ویرانی فرودگاه بوشهر
از این هواپیمای مسافربری تنها دم آن باقی مانده.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6392" target="_blank">📅 19:06 · 06 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
