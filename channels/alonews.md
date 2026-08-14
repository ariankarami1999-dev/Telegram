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
<img src="https://cdn4.telesco.pe/file/KpebWi3jpUVCimGycKlS_HxOxJKDa8hBP1YHkL9Jfol61RhAAff9XI3AQ1RgSg4_ctR2S--424UtHzSjKOalZxVdKMCmWro5iDkjlG4ScG-MumznVo99Dl1mJZcDp47GS5Dp-5PvKkOGNmzR_84vqAUPxN7hG7GtJZdCNZ0wc8YW5gPkM9KFxl4E0H9Eou0nixA-eBu9bmKBdZDIw-h_4rPCbDNiqKoRJkqOH3Z08nLw8PhIc3YNawXnE6ia3Xz44Sq9MbpHh_fiZNBSnMmgHy5CIqbl-dN4kq9S7fMZFlvTKyEGnfuFz0Rg2BZe_Cm8TGOEWGT4JAfKgXqBW_ukxQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 965K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-23 23:31:21</div>
<hr>

<div class="tg-post" id="msg-141727">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
پزشکیان: گرونیا طبیعیه، درآمد نداریم، نفت هم نمیتونیم بفروشیم.
🔴
اما عرزشی معتقده پیروزه جنگه
✅
@AloNews</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/alonews/141727" target="_blank">📅 23:30 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141726">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/907acfd306.mp4?token=J3xizQ4ihPtbGkOFTRYx6h09-IMZBf-Yy3MMHLk43rc33kWZJk6rg6BI0wbSUs4ByYmKuh0PmFScWd5qKTpaxs2o_HBJ0eme8tg5UGQra4-Bl7IoOaYRjH-Ytb9U7AnlclCVuvrmxHFwp72e7gZwj7jjhqQOnWpydlyKPnqvcitUTVc1ci37Jllf-cnQjCXF3X7MWUQTwj5nG1pQxADpDnRcWHcyxNPVdx2652m1zm5XSXcQJdw085C3Jw6athKgtkjKs2K0O0LqeVgSBsZaYG4ugFW79-MwopbYsLdWiTLktTyXHnYUwiQlmEePKDfZ4_jWj6T_vsxHf8HFg1XnpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/907acfd306.mp4?token=J3xizQ4ihPtbGkOFTRYx6h09-IMZBf-Yy3MMHLk43rc33kWZJk6rg6BI0wbSUs4ByYmKuh0PmFScWd5qKTpaxs2o_HBJ0eme8tg5UGQra4-Bl7IoOaYRjH-Ytb9U7AnlclCVuvrmxHFwp72e7gZwj7jjhqQOnWpydlyKPnqvcitUTVc1ci37Jllf-cnQjCXF3X7MWUQTwj5nG1pQxADpDnRcWHcyxNPVdx2652m1zm5XSXcQJdw085C3Jw6athKgtkjKs2K0O0LqeVgSBsZaYG4ugFW79-MwopbYsLdWiTLktTyXHnYUwiQlmEePKDfZ4_jWj6T_vsxHf8HFg1XnpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : ما ۱۹.۲ تریلیون دلار برای سرمایه‌گذاری در کشورمان داریم. می‌دانید دلیلش چیست؟ تعرفه‌ها.
🔴
ما با تعرفه‌ها، ثروت زیادی به دست می‌آوریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/alonews/141726" target="_blank">📅 23:28 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141725">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
ترامپ: به زودی تنگه هرمز را قلمرو آمریکا اعلام خواهم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/alonews/141725" target="_blank">📅 23:26 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141724">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ae2e03e6b.mp4?token=CvyK8uksxa4G7YYfVxfPFKmrUJ3vFQzg3uVQ4SsdICwcUuljzMJib6xummw-v4KDtB3E4LF_2Jiuln-eCdL9cDGFTLyUJnLwrP7RnoLax4KWwmpFGWX5-VPZVwAXNzCa-kMjThQkjjGqtH2plIHFHPaT6BTYjeaAtaeUwUjM4RAopOYo0_WeuHU0kqTu8LuEzSXlx2uXplmRYfzPZ4bekrw5WMTsQdx5iLb8_4_-GgLbVjy2ihCZ81M6umOeqOiHBKmBwQPCur3GXWOXXhNf-DECHbdby3lyPGx-Aa08pDnqqdQ6LDUbqffG_xFpC0lO6FD_njDwh2dFN8D-zYNFhkvVKluyC9JRg3XW0SsNPMN585sABHWosg2SQ0pcykLKUoY0YdRRi87ZQOFTXmPJrZBWSrAveeqzEnjfGoaZmYdBOsals-XHrPgvg4f_UL_LLdxkWX955HZ5IkjaIxwGj-d1HmP6xfy5DFNT6bHfjrJ6oIjmDkW-0_5kVqhXLjr_i8T-JtMhh8hQLDt2DSD8ekELgkbRCLB0ZN0zM4yTPorOJOgJyiq4auVto_LRJERMFtb_JugenJ1LkK-DsrHEsa4g9C6sfOTQppebby13V1bRUiIeMYcAxbJzKG5R82qpnmMFMMO5vMleWZsteASvtaYGVFuDqcGD7Ccn3R2RsjU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ae2e03e6b.mp4?token=CvyK8uksxa4G7YYfVxfPFKmrUJ3vFQzg3uVQ4SsdICwcUuljzMJib6xummw-v4KDtB3E4LF_2Jiuln-eCdL9cDGFTLyUJnLwrP7RnoLax4KWwmpFGWX5-VPZVwAXNzCa-kMjThQkjjGqtH2plIHFHPaT6BTYjeaAtaeUwUjM4RAopOYo0_WeuHU0kqTu8LuEzSXlx2uXplmRYfzPZ4bekrw5WMTsQdx5iLb8_4_-GgLbVjy2ihCZ81M6umOeqOiHBKmBwQPCur3GXWOXXhNf-DECHbdby3lyPGx-Aa08pDnqqdQ6LDUbqffG_xFpC0lO6FD_njDwh2dFN8D-zYNFhkvVKluyC9JRg3XW0SsNPMN585sABHWosg2SQ0pcykLKUoY0YdRRi87ZQOFTXmPJrZBWSrAveeqzEnjfGoaZmYdBOsals-XHrPgvg4f_UL_LLdxkWX955HZ5IkjaIxwGj-d1HmP6xfy5DFNT6bHfjrJ6oIjmDkW-0_5kVqhXLjr_i8T-JtMhh8hQLDt2DSD8ekELgkbRCLB0ZN0zM4yTPorOJOgJyiq4auVto_LRJERMFtb_JugenJ1LkK-DsrHEsa4g9C6sfOTQppebby13V1bRUiIeMYcAxbJzKG5R82qpnmMFMMO5vMleWZsteASvtaYGVFuDqcGD7Ccn3R2RsjU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ، رئیس‌جمهور: در عرض ۲.۵ سال، فردی انتخاب خواهد شد.
🔴
لطفاً یک چیز را به خاطر داشته باشید: ترامپ کسی بود که این کار را انجام داد.
🔴
این کارخانه‌ها همگی دوباره راه‌اندازی خواهند شد و آن‌ها خواهند گفت که چقدر باهوش هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/alonews/141724" target="_blank">📅 23:25 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141723">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e62055fa68.mp4?token=caOoagcbsDVCckmRFx7kXRxBtylonK-Eo_oOjDWa14x3feuo6B1uvihegiz1B0ve6d3YwBYTR9tPkaG_XvXI_4nQAHhyPFxKjxSiT1oaKOw_Tx3EqeTAhXKn0Oiox3ABo1lmIsj0gjT9-VryfIVUxzgkDmFzdhRevZDFAX6hozmdTuHKX8e6aqv0p7AxtBezaxZ5JZIrQXZdFR_vej1fmuxLEbTqeuwBtD3n_t-MB8pA0H4aGb_A3AwXRNXFDPqXOB_Yel47WQbrD9Q0vZOc9--O0AMsFSoRE4mJ0-kRUyF3cXmI0VpG2sn0gx1Il7do945cl4boBzcg8ZZlIRF_Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e62055fa68.mp4?token=caOoagcbsDVCckmRFx7kXRxBtylonK-Eo_oOjDWa14x3feuo6B1uvihegiz1B0ve6d3YwBYTR9tPkaG_XvXI_4nQAHhyPFxKjxSiT1oaKOw_Tx3EqeTAhXKn0Oiox3ABo1lmIsj0gjT9-VryfIVUxzgkDmFzdhRevZDFAX6hozmdTuHKX8e6aqv0p7AxtBezaxZ5JZIrQXZdFR_vej1fmuxLEbTqeuwBtD3n_t-MB8pA0H4aGb_A3AwXRNXFDPqXOB_Yel47WQbrD9Q0vZOc9--O0AMsFSoRE4mJ0-kRUyF3cXmI0VpG2sn0gx1Il7do945cl4boBzcg8ZZlIRF_Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شوخی ترامپ: فکر می‌کنم باید دوباره کامالا هریس را نامزد کنند؛ او نامزد فوق‌العاده‌ای بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/alonews/141723" target="_blank">📅 23:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141722">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01f438219c.mp4?token=JAynmoQPz8bLx2D2dzHsxJD95cWkAJHlJXdl2Dvj7ZE23ReTfIIJ7aOFCtq7T_Y17eqBH834ie9mCm40nkM50NARcBphg9_oBAfKySeqaLmnzPCGu5FTmUC0GMVKZ6XJfGaM_P2nxD4T7FLGcrAxv4oA-kI1F3OqTqrQ4YVps0G4AKMU-Gi_oorOvrc_zFMw2lcK03GfIifxyfJnItkA2piPnPuDMY2ErroTvJ-HpBC6T3in5D4naBuRrntAbUCjOWW2AFgQ8V8Oe5AOIeWjNv1ILCkJqeXyfWtvj-8lgkNMx1gk7R28VDs85XbqSRMRsYvQaPbwzQLZBj3cRWiUqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01f438219c.mp4?token=JAynmoQPz8bLx2D2dzHsxJD95cWkAJHlJXdl2Dvj7ZE23ReTfIIJ7aOFCtq7T_Y17eqBH834ie9mCm40nkM50NARcBphg9_oBAfKySeqaLmnzPCGu5FTmUC0GMVKZ6XJfGaM_P2nxD4T7FLGcrAxv4oA-kI1F3OqTqrQ4YVps0G4AKMU-Gi_oorOvrc_zFMw2lcK03GfIifxyfJnItkA2piPnPuDMY2ErroTvJ-HpBC6T3in5D4naBuRrntAbUCjOWW2AFgQ8V8Oe5AOIeWjNv1ILCkJqeXyfWtvj-8lgkNMx1gk7R28VDs85XbqSRMRsYvQaPbwzQLZBj3cRWiUqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: دغدغۀ من معیشت مردم است و نمی‌توانم نسبت به آن بی‌تفاوت باشم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/141722" target="_blank">📅 23:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141721">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35c2eb2723.mp4?token=WfHpcU1-hJPZpebJzWhM--CrOiRu7H-BKeqOBOOdQ3D-QKRRFW5ZW7rIx4Z4xp4NsegxdqwVwwJIUMOSaiNLbQuy3faACfv1_Wu67e-Pz77okGdopUYnG8bzRPF1rFSc1W0lMhF5TLzdFnDGf4th16q2c0JzSa91HiO_pgHOGdPUo_cxk9ZG8muPR2MejH7k_d7adWzlSFxsBXbUqVMyHJALaJIZ7WiAOaC330La5EOkOnArTbFNlKh6Y0-qydRPEEHd5ph5c3xG3a2tVCATjxy0NGZ25NB0-iGGvTV-nk8saqPD-5Vqtf35qXG8kH71kC38jOplzjvrD4K_oALztw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35c2eb2723.mp4?token=WfHpcU1-hJPZpebJzWhM--CrOiRu7H-BKeqOBOOdQ3D-QKRRFW5ZW7rIx4Z4xp4NsegxdqwVwwJIUMOSaiNLbQuy3faACfv1_Wu67e-Pz77okGdopUYnG8bzRPF1rFSc1W0lMhF5TLzdFnDGf4th16q2c0JzSa91HiO_pgHOGdPUo_cxk9ZG8muPR2MejH7k_d7adWzlSFxsBXbUqVMyHJALaJIZ7WiAOaC330La5EOkOnArTbFNlKh6Y0-qydRPEEHd5ph5c3xG3a2tVCATjxy0NGZ25NB0-iGGvTV-nk8saqPD-5Vqtf35qXG8kH71kC38jOplzjvrD4K_oALztw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در مورد نخواستن اینکه نیویورک به دلیل جرم ها سقوط کند: «ما اجازه نمی‌دهیم این اتفاق برای نیویورک، ایالت نیویورک بیفتد. و به همین دلیل است که باید بروس را به سمت بیاوریم.
باید او را آنجا بیاوریم. هیچ‌جا حمله کمونیستی به جامعه آمریکایی واضح‌تر از اینجا در ایالت نیویورک نیست.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/141721" target="_blank">📅 23:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141720">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ed040a20e.mp4?token=COdhxNeiFNV-6Ji-2qU_iXw12EGJSGSvGCVC3OQYXDkrx6M0eVvH9bKu0RQLd9skZSebF1pcQw0UjIxYd8VNCby2CLQif1M_zRqpXVo0utXitiaQXhIdLp_vDJ8U055M1rXUOSg5tM83ShbnCDCuav5J5RZYggkq9S7D4t_VZjH-jZMATwpLQEOrCYXuaRINH9OtZTYMmMLvnDVCYi5904mrVGqDQm6m_tU6ME7bJVpX69KKfoR1nwAXtEh9MteYfm8Qqv7VyU3YMSYqf2zoYGQkpl5lWy7cCoxboSzITrjTcLwo780E3jsRNfUxjDzOJ-CcxCvFwp4iHsEPHaVrzlCURb77DuvtFM_x1CO4Qq-Wwj1e7HC6D33tQJnal4XGjGAFArq8yHciXIa9Me52_pvn_W4tI-PUkGYmwUyY05FpL_u7upcdtIoziazlS_WLIgvEdJSvPXX_MpLQPEfEcqnkeUZodMOwcBs4shlZnGY5YpjlSLJgypSfEYgsBnF-RYfrorK9_KkY8mTnxjA0HKSgWi3dM-vKkpLjknZpdtbmpCUDukUj4E5Yz_JCgnRVWz0MGDmLuG7keI49sPYIzldJ5ZhYo0jr7-Px9X5N7O67Gud1rLiD_4JNHgObKtklKxDG-2RLvoWrMk4bMJtuGxMQX8m-5PRNBAQA6t_gjEk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ed040a20e.mp4?token=COdhxNeiFNV-6Ji-2qU_iXw12EGJSGSvGCVC3OQYXDkrx6M0eVvH9bKu0RQLd9skZSebF1pcQw0UjIxYd8VNCby2CLQif1M_zRqpXVo0utXitiaQXhIdLp_vDJ8U055M1rXUOSg5tM83ShbnCDCuav5J5RZYggkq9S7D4t_VZjH-jZMATwpLQEOrCYXuaRINH9OtZTYMmMLvnDVCYi5904mrVGqDQm6m_tU6ME7bJVpX69KKfoR1nwAXtEh9MteYfm8Qqv7VyU3YMSYqf2zoYGQkpl5lWy7cCoxboSzITrjTcLwo780E3jsRNfUxjDzOJ-CcxCvFwp4iHsEPHaVrzlCURb77DuvtFM_x1CO4Qq-Wwj1e7HC6D33tQJnal4XGjGAFArq8yHciXIa9Me52_pvn_W4tI-PUkGYmwUyY05FpL_u7upcdtIoziazlS_WLIgvEdJSvPXX_MpLQPEfEcqnkeUZodMOwcBs4shlZnGY5YpjlSLJgypSfEYgsBnF-RYfrorK9_KkY8mTnxjA0HKSgWi3dM-vKkpLjknZpdtbmpCUDukUj4E5Yz_JCgnRVWz0MGDmLuG7keI49sPYIzldJ5ZhYo0jr7-Px9X5N7O67Gud1rLiD_4JNHgObKtklKxDG-2RLvoWrMk4bMJtuGxMQX8m-5PRNBAQA6t_gjEk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرزیدنت ترامپ:
تا این هفته، نه نفر از ده نفر از لیست متهمان فراری اف‌بی‌آی دستگیر شده‌اند.
🔴
این یک رکورد تقریبی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/141720" target="_blank">📅 23:21 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141719">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a10222396.mp4?token=F1De4N-HZHc1-TB6__XQhJfKl7wBiHdObwp8Vi8GPQoNEmLpwwBniwY3cZ0mTnTPm3seM7w7Jxdt4NkjCFcCcRzbsqlh3_MUiq3Q7e1EvBEa7CzBzAbT9mqBktBg120l070T-MXfGqSRPziFnUAUL4wWdhfHzz9NggiquwbOu2hkCVPllNB1S9dVesBuYPVbfOqLCbfpWuzwRAT4UBlFG46odYsmfjEbgHU8qIOGKNCcgLgr68bOEttpNehdgGk-K_EBJJSLuN2wezqgdlGC-tklWbi32CXdTcJAWF0xbKVhUyHnF4PDZZbSw0g8MuhrdlIY_5QQEOTmqTOu7gRqNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a10222396.mp4?token=F1De4N-HZHc1-TB6__XQhJfKl7wBiHdObwp8Vi8GPQoNEmLpwwBniwY3cZ0mTnTPm3seM7w7Jxdt4NkjCFcCcRzbsqlh3_MUiq3Q7e1EvBEa7CzBzAbT9mqBktBg120l070T-MXfGqSRPziFnUAUL4wWdhfHzz9NggiquwbOu2hkCVPllNB1S9dVesBuYPVbfOqLCbfpWuzwRAT4UBlFG46odYsmfjEbgHU8qIOGKNCcgLgr68bOEttpNehdgGk-K_EBJJSLuN2wezqgdlGC-tklWbi32CXdTcJAWF0xbKVhUyHnF4PDZZbSw0g8MuhrdlIY_5QQEOTmqTOu7gRqNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان
:
بارها گفتم و باز هم می‌گم؛ من هیچ‌وقت در برابر رهبر نمی‌ایستم
🔴
این حرف رو فقط برای شعار نمی‌زنم
🔴
چون برای من اتحاد از خیلی چیزهای دیگه مهم‌تره. اگه اتحاد از بین بره، قدرت هم فرو می‌ریزه
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/141719" target="_blank">📅 23:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141718">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
ترامپ : ما نماینده کل جهان هستیم، هیچ کشوری مثل ایالات متحده وجود نداره
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/141718" target="_blank">📅 23:13 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141717">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
ترامپ
:
کسی اینجا هست که طرفدار قطع بودجه پلیس باشه؟ اگه هم باشه، جرئت نمی‌کنه بگه
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/141717" target="_blank">📅 23:07 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141716">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
ترامپ به فاکس نیوز: ما یک ضربه اقتصادی قوی به ایران وارد خواهیم کرد و برایم مهم نیست که این قبل از انتخابات میان‌دوره‌ای باشد یا نه
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/141716" target="_blank">📅 23:06 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141715">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05ff8a9360.mp4?token=HerTz8zS-P0PCHmi_c5v6YAHDW9TJAE1aCf9an1t0nE_nSS0bvQVWKFn41pcrV1yA9pyO-ipZvf5uV9Nzoq80y28JunhMwvJEMudaNjbgJgIRlkrQp1RIklyTsc8kWH6rq-KXFoQvz176mOquJKpYDzGsPjlf_mEv19MEaTl4rwJPppX9VaC1SmNc2Jah8SQCIEQSMVLx18_XaYi_dRtCbu8crj4iygf-B09AfPR6b26XqsJ65lTLTAYyAGKw3xLjpDa-pzLNMTo4ueHlmQJnRUr6RzXwH-_ymf85OJmDYIEbZcxqlTl81-Cjscob7BIAtZm6HZzKSRxSdcQ_Vod6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05ff8a9360.mp4?token=HerTz8zS-P0PCHmi_c5v6YAHDW9TJAE1aCf9an1t0nE_nSS0bvQVWKFn41pcrV1yA9pyO-ipZvf5uV9Nzoq80y28JunhMwvJEMudaNjbgJgIRlkrQp1RIklyTsc8kWH6rq-KXFoQvz176mOquJKpYDzGsPjlf_mEv19MEaTl4rwJPppX9VaC1SmNc2Jah8SQCIEQSMVLx18_XaYi_dRtCbu8crj4iygf-B09AfPR6b26XqsJ65lTLTAYyAGKw3xLjpDa-pzLNMTo4ueHlmQJnRUr6RzXwH-_ymf85OJmDYIEbZcxqlTl81-Cjscob7BIAtZm6HZzKSRxSdcQ_Vod6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ، درباره وضعیت فعالیت‌های مجرمانه در ایالات متحده پیش از ریاست‌جمهوری خود: «و در چهار سال گذشته قبل از اینکه من کشور را ترک کنم، کشور ما توسط مجرمان خشونت‌پیشه غرق شده بود. منظورم این است که به یاد دارید چند سال پیش چقدر وضعیت بد بود؟ درست است؟ واقعاً بد بود. باند‌های خارجی، اراذل وحشی همراه با بایدن.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/141715" target="_blank">📅 23:03 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141714">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
حمله هوایی اسرائیل به المنصوری در جنوب لبنان انجام شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/alonews/141714" target="_blank">📅 22:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141713">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
العربیه به نقل از یک منبع نظامی یمن: حوثی ها با ۴۴ پهپاد و ۶ قایق بمب گذاری شده، بندر المخا را مورد حمله قرار دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/alonews/141713" target="_blank">📅 22:58 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141712">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
صحنه‌های ویدیویی شامگاه جمعه 23 مرداد حریق در بندر المخا یمن ناشی از حملات موشکی بالستیک شبه‌نظامی حوثی‌ به زیرساخت‌های این بندرگاه را نشان می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/141712" target="_blank">📅 22:52 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141711">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
فوری /  آکسیوس: کاخ سفید بدون اطلاع نتانیاهو در حال برقراری ارتباط با اپوزیسیون اسرائیل است
🔴
آکسیوس به نقل از منابع آگاه گزارش داد، در بحبوحه کاهش محبوبیت نتانیاهو، دولت ترامپ برای جلوگیری از به خطر افتادن ابتکارات خاورمیانه‎ای خود، شروع به برقراری تماس‌های مخفیانه با رهبران اپوزیسیون اسرائیلی کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/141711" target="_blank">📅 22:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141710">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
در دومین حادثه ریلی از نوع خود ظرف شبانه‌روز گذشته در بریتانیا، جمعه 23 مرداد، یک قطار مسافربری در نزدیکی «ویکفورد» در «اسکس» از ریل خارج شد. روز قبل از آن بر اثر واژگون شدن قطار در «لویس» 20 نفر زخمی شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/141710" target="_blank">📅 22:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141709">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ds9u1-HE5SCjK1FOayCwHLuyYvBIO18TiZjVA7FA1swOw5fFnlC-u_RG-qweLJmEZ2Q_D5t5FVxzXlwUCykmWf6IGvhB59A-rmX_AUdd0gWAirc3miINsPwNOwhaSRGVn4LFcoXozZAqBwJArEl_cpSzPxVUBJfUJajif6r1Op9FVsPv8Wcn6j7M4nDgyKj5PFP4Dc-sQjB0fwkPQvTxgtVN4ejGeDAbhsLxxOoLsDxzKNtAbg3yz9VL5izI0032iaBy9jngqyx50tJSjkr9nX1Ua67532-t_gn4KdBc6054Ni1uEdJng9FSnITP3Hn_rXo0VGvftmwTE62CChfXCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
با پول یه ماست پرچربِ امروز،
۱۰ سال پیش میشد خرج خورد و خوراک خونواده رو برای یه ماه داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/141709" target="_blank">📅 22:25 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141708">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h0SgEH4Bj4t7PZO7mkxQUyX8cvt5GTSze8Y2HufKxCimsgKP0h5iAzBS19eP4gT_h3dGsu4Q2_WcSfRLLjc5-u_X5GWt5tT5iTf0s9bRL5EqWHyx6YYvHR_G9cX-Vfv_wC8hE1X7SY0eSWX3u4BV18zskjDxGPrv4qs_DSufSi0naenkdWKSEDNsnZrZi11QQYPMPuYql8aJS4Y7nSKmqxzwh2SRQk_yopa3l-6H9cuEB3CorYzoI0D-shJ2Sq2r8QDrMYdfHZTOLe1na9AxqY01icXMhlb_dVK9pMJCKDzRAZj3U1ARIdF4ELxIEZ1FSc-rCA2RSCZkovs8uhGUSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تعداد دفعاتی که مناطق مختلف تهران توی جنگ ۴۰ روزه، مورد حمله و اصابت قرار گرفتن
🔴
بیشترین: منطقه ۴، ۲۹۸ بار! که شامل: تهرانپارس، حکیمیه، پاسداران، لویزان، مجیدیه، شمیران نو، هروی، نارمک شمالی و شمس آباد میشه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/141708" target="_blank">📅 22:18 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141707">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qbuyVZFucBgPhMSV1dqfA2bln5w4gJ-sZwrHd5_ELd8agHk6EAmWZrFgGzz4EFN6yx3IVhSjrzyXwKdVZp8HP0eOAnpTEFV98kx5TD1HZXcB3zkyNgJPeS5lLIDpBn3kVIcWXJplGtVRzrSeOH-0vD76iZFoWz7yv7HUHI_-TLEM91MQmiG8n8XJgrg6_K4w1dY1eNJBpak7f4NLuZwKnXh57XxYpbr9SBgacHy89xMyWNdwKwfXYLd8volfkxiOXO3ApgwwjNZ0OOhKwwC_aOBu2ulP_qkNec3WaW5BzbDHRwg_ElaJR3XwP9xbf-fTIMGm9r7vrhq6ZZjA0BiwLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
افزایش خطر آتش‌سوزی در سراسر بریتانیا
‏
🔴
مقامات بریتانیا درباره افزایش خطر وقوع آتش‌سوزی‌های طبیعی در سراسر کشور هشدار داده‌اند و از شهروندان خواسته‌اند از هرگونه فعالیتی که می‌تواند باعث شروع آتش‌سوزی شود، خودداری کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/141707" target="_blank">📅 22:12 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141706">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‏
👈
کانال ۱۳: اسرائیل قصد داشت حمله‌ای دیگر را در سوریه انجام دهد، اما ترامپ مداخله کرد و این اقدام را متوقف کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/141706" target="_blank">📅 21:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141705">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rxREali0h3gTWpGaGOvqZ5fH9eFrrlOYMLsyn_WJT5fFu8ErVEGyJ81Vmgv2esNV-UR41pUHICX61ZUqpeYs-6zNdjvxecD_qtOP9UTizm5dPuE3eD9_9Pm1flSHnqEsMsnrr0yfz3nuMz2G5MLkaJNP69Xbe7QzsPBpN3Ro8WBvtcq3jWUimyRs3qgjo1zF0_ias9w233Lx7Rn7GNi-KjQm0HvOrbAWnff8InoqzPwCcpXQVuq5EtJGcqLtvvKQCun6kyvtEmubnTilAbi8V0HZ2WwB6G8LGWN1VTRj7ouvpnHYKXiCjLPI1eNJmSPVgtFtLh-GJvj7y7cLvcQdsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جلیل محبی معاون حقوقی مجلس:
تو مصرف بنزین صرفه جویی کنید تا گرون نشه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/141705" target="_blank">📅 21:53 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141704">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
سخنگوی کاخ سفید، لیویت : آمریکا همچنان می‌تونه ایران رو تحت فشار بذاره و اقتصادش رو فلج کنه
🔴
ابزارهای بیشتری هم برای افزایش فشار در اختیار داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/141704" target="_blank">📅 21:48 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141703">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
یک منبع نظامی انصارالله: شرکت آرامکو در جنوب عربستان را با پهپاد هدف قرار دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/141703" target="_blank">📅 21:37 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141702">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eTLD9tfWOJrJxjfl0PYb-UHSWHTWsaFfkqJUB8MbvakCy6U6_LUgJt5w7uhV4cowbzzrDmZxWILxu6E7bJ91otKJypSThc28p0D6eOAii5uT7L3625J4st9fAY8vBb6PfvoZjJjo_HYWXi4MBJS-lkQ4VKLGJ8klWzOMXtePsrOgnMfvNkixrAmQnJvqTOQ-udwZRrCH638x0yHAnulyfAYJiTg80voOn34X83IZl4M7yH34wNXaC6HQKgHdfE7ILConY2HTfsPCN_9oawSEVni6vMM8O_ntE6llYdOH7bfhjhvGn1sUFzJnNLhJg2tNkvWWRmvrXxanNvXaXAFhlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
داعش اسپانیا رو تهدید کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/141702" target="_blank">📅 21:28 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141701">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
دولت کانادا امروز جمعه اعلام کرد ۵ مقام ارشد نظامی ایران را به دلیل اختلال در تردد دریایی در تنگه هرمز در فهرست تحریم قرار داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/141701" target="_blank">📅 21:11 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141700">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
ترامپ : از نظر وال استریت، وضعیت اقتصادی به طرز شگفت‌انگیزی خوبه
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/141700" target="_blank">📅 21:09 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141699">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bb239496d.mp4?token=YQsUZst93C-8A3c_bZHzGFs5Qtt_UyFbmn0iK5NgMD0WohENtGz3HQjhPH-fQTzldVrhnHM5V7Wb0IlN7tNpiYfyjLWqMM-8uMdPd_ceQV6MHujf9hKaTUx3-eiJ4L8KNRQTrAWwuooL5-jI7i0ek3GTFdcTnVxFovC36zSPFuVb-wNmTZIY1dUWEs_YS8hmMe1bjnJ-a7TLPOvrydqSCxXb0kqWob7H1xc3xSxIV6aauGrZrUkS4D-SS2SMP7VVz1l0_4TtOrgogcQUKx6jfX95cSgj6N_b1dvkGAD5KqDJuSzVVMX50WBvSDWVpJ9I3pylGq50nSdQamIlpQxwDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bb239496d.mp4?token=YQsUZst93C-8A3c_bZHzGFs5Qtt_UyFbmn0iK5NgMD0WohENtGz3HQjhPH-fQTzldVrhnHM5V7Wb0IlN7tNpiYfyjLWqMM-8uMdPd_ceQV6MHujf9hKaTUx3-eiJ4L8KNRQTrAWwuooL5-jI7i0ek3GTFdcTnVxFovC36zSPFuVb-wNmTZIY1dUWEs_YS8hmMe1bjnJ-a7TLPOvrydqSCxXb0kqWob7H1xc3xSxIV6aauGrZrUkS4D-SS2SMP7VVz1l0_4TtOrgogcQUKx6jfX95cSgj6N_b1dvkGAD5KqDJuSzVVMX50WBvSDWVpJ9I3pylGq50nSdQamIlpQxwDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: مأموریت نیروهای مستقر در ناو «آبراهام لینکلن» بیش از حد طولانی نشده است
🔴
خبرنگاری از دونالد ترامپ درباره نگرانی خانواده‌های نظامیان از شرایط نیروهای مستقر در ناو هواپیمابر «یواس‌اس آبراهام لینکلن» پرسید که ترامپ پاسخ داد: «نه، آن‌ها نگران نیستند.»
🔴
در ادامه خبرنگار پرسید آیا این استقرار نظامی بیش از حد طولانی شده است؟ ترامپ پاسخ داد: «نه، نه، نه؛ حتی نزدیک به آن هم نیست که بگوییم بیش از حد طولانی شده است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/141699" target="_blank">📅 21:02 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141698">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
مجتبی یوسفی، عضو هیات رئیسه مجلس: وزارت خارجه وسط جنگ به ما نامه دادند قانون تنگه هرمز را در مجلس تصویب نکنید تا ما با طرف عمانی تفاهم‌نامه بنویسیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/141698" target="_blank">📅 20:56 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141697">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">💢
زود بیایید اینجا خبر خیلی مهم
👇
https://t.me/+nCexQYLuuONhYzg0
https://t.me/+nCexQYLuuONhYzg0</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/141697" target="_blank">📅 20:54 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141696">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f84d0c51a.mp4?token=CZWjGGvaBKjnq8E_T9J8alUyre54_0Eh6dFlfdBhvVyDS-0RY9Ly3nY240i4w8t1JWXagijOVi3mQQq3YJidwsPMO9aPREUNCojbmANOvOfy0CrrfWtOe1EtShhl7hodHGS7pQOTUWCSidpIpaI31hYmOV5O8eQWvfmiLs-O_njZXISkgA8OJH0tI4PYAwDpitKw0umNnMAt5u27zv85KSX-WHko-_Q4KTSqNleefhNrgp_utozA16nKIwgFJDARpl3yryod0YYprRzg_tvIwgSjnDFf0m61AkHHtpIkGz992Ly2LhmtTX9Bhpo4-BQ1PDbx5gm2Z0p_-_G_qOxA9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f84d0c51a.mp4?token=CZWjGGvaBKjnq8E_T9J8alUyre54_0Eh6dFlfdBhvVyDS-0RY9Ly3nY240i4w8t1JWXagijOVi3mQQq3YJidwsPMO9aPREUNCojbmANOvOfy0CrrfWtOe1EtShhl7hodHGS7pQOTUWCSidpIpaI31hYmOV5O8eQWvfmiLs-O_njZXISkgA8OJH0tI4PYAwDpitKw0umNnMAt5u27zv85KSX-WHko-_Q4KTSqNleefhNrgp_utozA16nKIwgFJDARpl3yryod0YYprRzg_tvIwgSjnDFf0m61AkHHtpIkGz992Ly2LhmtTX9Bhpo4-BQ1PDbx5gm2Z0p_-_G_qOxA9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بلوسوف، وزیر دفاع روسیه
:
جنگجویان شجاع کره شمالی که کنار نیروهای روسیه می‌جنگن
🔴
منطقه کورسک رو از «گروه‌های نئونازی کی‌یف» آزاد کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/141696" target="_blank">📅 20:51 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141695">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a627737cf1.mp4?token=uCLmpjHTBbbHZwt_mLCMjmKfRa5uGv-yoiRRcrZNc1DyXKlNvQqmXG9Fv8ZWCQmWYBsCP1qjL4m9xwXIOXTwDC1jRGOVEvsFEY_jXTxfjotYwGC6upBy3GfckfOV9fO04cD7AZGvNKoRPQeHkoxY4MmocTzDTB5yGcLPLI1KWagB0rVHcBj3GIguiVHj3bydmSp8pSKTDKPl-X5Lf4ShWmihbQXhZJsPOOJdTHSpY4bOZyXkl_qH-aX4iZCX2kx1ZPAt-zeAyyMvwXX7FQ806dXYfUnz1_BRguEmjlznjLnPyPIZIaENgdu42jpEPnQ5d8u56zEHi81kS22zHmfKHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a627737cf1.mp4?token=uCLmpjHTBbbHZwt_mLCMjmKfRa5uGv-yoiRRcrZNc1DyXKlNvQqmXG9Fv8ZWCQmWYBsCP1qjL4m9xwXIOXTwDC1jRGOVEvsFEY_jXTxfjotYwGC6upBy3GfckfOV9fO04cD7AZGvNKoRPQeHkoxY4MmocTzDTB5yGcLPLI1KWagB0rVHcBj3GIguiVHj3bydmSp8pSKTDKPl-X5Lf4ShWmihbQXhZJsPOOJdTHSpY4bOZyXkl_qH-aX4iZCX2kx1ZPAt-zeAyyMvwXX7FQ806dXYfUnz1_BRguEmjlznjLnPyPIZIaENgdu42jpEPnQ5d8u56zEHi81kS22zHmfKHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
ویدیو وایرال شده از یه مسلمون در آلمان درحال تخریب شیشه های مشروب یک فروشگاه!
‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/141695" target="_blank">📅 20:47 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141694">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tfCUUD4UC_GHWJxSbLYSbPlIEPYCaGX7p65xpbGTsASHSOtpj3Y6NdtGvAGdwCtEwhKmayTcTHBZGBHcBYRDprbjndqMxlwajGN5dwBJDZRs1xCvvBKfR6mQV7n8T-ioN1ifOI6wvlKu1LQ-SbjerJ0QbyT_kex8iKErqtcjO2BYiXyN_Rwge9pNXi-QjyPzUI_p0AsMcVhihKfE-MK2cJ3lZ93TU_0sn4UCzPu2645z9xmAHqt4zqkUebc6DOOjwdyWSM1B9O5QpGmEaY8CanLny63HJhFpBhZx7bRUjX5BiirWeyOz7bpzBRx-1VtANU9LY621pa5k4LErcdB_TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
‏ترامپ در شبکه اجتماعی خودش تروث سوشال مصاحبه بسنت وزیر خزانه داری با نیوزمکس را بازنشر کرده که وعده فشار اقتصادی شدید علیه ایران را داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/141694" target="_blank">📅 20:41 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141693">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8cda1283e.mp4?token=FtS0eI_vVcdRe3cmDXnAOedfq1vso9-RSZQwM3b7t6au92MYx0dzZpv_NtGQzwDO1Cer7UIS8c9SyhNgn7Di5jbaYWbuA-GOCqPD37aF8EaNs_ra93dz2Yo34y91ocUd-rP4ORK-l4M_6khDK2JlM8gLTc0jvRT71CuMzmrinGWF9pw1Xe67LnCCpSEb-yg9K42d1eBLCcrEoRTW8jd3w6Mn5ATK8IUvGf2RFxd4jLwL0HwL-wTzJbzJ4Cni-l7sDM0RyGke-cJD8vCqInvzcFBlOtUqSepBHPDM1o09mpsJayKkoDywruuHbGapU_HSMyq5D8evr6yzgWVLmj7Efw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8cda1283e.mp4?token=FtS0eI_vVcdRe3cmDXnAOedfq1vso9-RSZQwM3b7t6au92MYx0dzZpv_NtGQzwDO1Cer7UIS8c9SyhNgn7Di5jbaYWbuA-GOCqPD37aF8EaNs_ra93dz2Yo34y91ocUd-rP4ORK-l4M_6khDK2JlM8gLTc0jvRT71CuMzmrinGWF9pw1Xe67LnCCpSEb-yg9K42d1eBLCcrEoRTW8jd3w6Mn5ATK8IUvGf2RFxd4jLwL0HwL-wTzJbzJ4Cni-l7sDM0RyGke-cJD8vCqInvzcFBlOtUqSepBHPDM1o09mpsJayKkoDywruuHbGapU_HSMyq5D8evr6yzgWVLmj7Efw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حوثی‌ها همچنان المخا رو با موشک بالستیک و پهپاد هدف می‌گیرند
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/141693" target="_blank">📅 20:33 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141692">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
تسنیم: دود مشاهده شده تو جنوب تهران مربوط به آتش زدن ضایعات پلاستیکیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/141692" target="_blank">📅 20:29 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141691">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
رکنا: تو تهران دو تا پسر جوون تو فضای مجازی سر دختر دعواشون میشه باهم قرار دعوا میذارن و دیشب تو یکی از خیابونای تهران یکیشون اون یکی رو با ضربات مکرر چاقو به قتل میرسونه
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/141691" target="_blank">📅 20:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141690">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OIuE-X1ZVfGyzp1cB6VPyv7EkCtl-Msd8anpfm-_emiFvOjJyEHm92siE2YZGOCxmoyWoDKX_6IoK88TXIlEZ08B9dmebygx5Xf7n1AW_l1Qmebl2Dz7PA7xRBVe8P-yLHSrtOoUyClXI5-I56VI3rQXp56ogZWvEcUk_bFadac6EwQBsmmujxyLOHiw1xDO4mcUvtJ0QVHHe0TYU6qwmHA8Wd5-GkuYhQ0IFKeXVoqfpjHaf8OxyFKx32IRISCDwEznMguwswzqezxdS2hiek_6Sn5ufvk2gGuBSgqufrXxqhFt7XpJLjMxiwzFl0e4kti-n6_vAuxfE2VhLCiRMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث‌سوشال
:
من با افتخار اعلام می‌کنم که کوین رایدوت، یک مبلغ مسیحی عالی، به بازداشت ایالات متحده بازگشته است.
🔴
کوین توسط تروریست‌های جهادی در آفریقای غربی — کانون اصلی تروریسم اسلامی، جایی که در سال گذشته حملات مرگبار بیشتری نسبت به هر جای دیگر روی زمین رخ داده است — ربوده شده بود.
🔴
کوین، ایالات متحده آمریکا مشتاقانه منتظر خوش‌آمدگویی به شما در خانه است. خوشحالم که کمک کرده‌ام! پرزیدنت دونالد جی. ترامپ
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/141690" target="_blank">📅 20:08 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141689">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
شیخ نعیم قاسم: اینکه ایران نخستین بند در توافق‌نامه اسلام‌آباد را عدم تجاوز به لبنان گذاشت حمله دشمن را مهار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/141689" target="_blank">📅 20:05 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141688">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
رویترز گزارش داد پس از حمله به دو کشتی متعلق به امارات، عبور و مرور دریایی در تنگه هرمز به‌شدت کاهش یافته و این آبراه راهبردی به مرز توقف کامل تردد رسیده است.
🔴
براساس این گزارش، تشدید تنش ایران و آمریکا و بن‌بست سیاسی بر سر بازگشایی تنگه، شرکت‌های کشتیرانی را بیش از پیش محتاط کرده است.
🔴
ادامه این وضعیت می‌تواند فشار بر بازار انرژی و نگرانی درباره گسترش بحران منطقه‌ای را افزایش دهد؛ هرمز حالا مستقیماً به یکی از اهرم‌های اصلی تقابل تهران و واشنگتن تبدیل شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/141688" target="_blank">📅 19:56 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141687">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mfy0YPXBiGX8aZoJI6qwK-wQR2FFay4M8IQsOS1GOMZM1PrT0dr2ciVRAdhTam2nLjFFhVtKPZ7aHkUfLv4-nVTiVAlt8_2-0bYRW0rDqNS81vyGRT2EzQN9lbwbhCPKcizTpKefDrfEpvWsIq0_30ictD3uKVYgW4nkCbZ6P8xOhlbE1UMUMvhQ049xEWNDM2QpnZzb6PXOjMW9cTq_QGXWegX5mKUwkn39F5aEWtGNEr8G98ejcwytA1f-6-sO3wRZQte7cqLObUDmfxF0pUOV92FXTF8bab9F2qZxXUQjUHNARuCQqvDRdoKSMsI8JRX763OO_C16SZpdOiZW8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر تازه‌ای از نوستراشیمی (۷۷۲)، یک ناوچه موشک‌انداز کلاس نوستراشیمی (کلاس یاسترب) پروژه ۱۱۵۴۰ نیروی دریایی روسیه در ناوگان بالتیک که در حال حاضر در دریای شمال در مأموریت جنگی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/141687" target="_blank">📅 19:51 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141686">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u1J9FahsAQ1Ya3hTPW_kzZhoHnbbeN0LHkVFTb1iquwTWlGajq-25aoz8bY2q-8JfRLxwKVLTN17NBkrpzbWG7u0yOkKXIa_jbMwZXE4UJ00QTYQTqrJc_qQuqN9a2tth5yEOWqXm_LMBFUZluu2NkmneRgWXvmM6KO3oJPCJ27_6VUbqI2YETM1RVk7RjD--TpooUfv8Keoc4knjN5j_hqX7TX9yM2JNjNjJ1hi6BZHNUlFbaX2KFqqFM8i8M8TpCuwFCz6PAT_KEhaZpmlbny8mtflGjgbjaLU0LvYWI4j0K6jzJ6nGnKpNyPhyeH1uRbMXQO9F3zE5mN9bNK6iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خورشیدگرفتگی دیروز از نگاه فضا
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/141686" target="_blank">📅 19:45 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141685">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
سنتکام :
۶۲ فروند کشتی تجاری رو تغییر مسیر دادیم، ۳ فروند رو از کار انداختیم ۲ فروند رو مورد بازرسی قرار دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/141685" target="_blank">📅 19:41 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141684">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
نخعی، نماینده مجلس: بخشی از قاچاق سوخت تو کشور «رسمی» و با مجوز انجام میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/141684" target="_blank">📅 19:30 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141683">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iz-PU4_bH8JM3oLEu5U8tUOzU4ugPi1vr8fZhNl1zjAXtolzR2j74_iFajDdUjkSww5RzmDa8lFETo8pkbxiAYCaEg_B_M9FODiISvbAUkfg6hONcAt_1gRwEvBv056mxtdFQkk-vW3t3N8AssIrncvWgFXRSdtoEsuj8K3_GkqM7FJXIMAw336oCS5WdeurP_K21jJN9LPXd2wqbyUZ3IMXGjgaqPouAJP8X07JsI4gUlXlvAs5OuouOaNq0pfUCg58hN-evsM-IeOm0QA--7znxLLoE3ew_TbtwEdQZjoFvoRbeDu9xGywKpdnzJuT7nlXNdxvhA1JygIcV6Mobw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نوسان قیمت نفت برنت در ساعات اخیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/141683" target="_blank">📅 19:29 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141682">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
حملات اوکراین به بنادر روسیه واردات نفت ترکیه از مسکو را کاهش داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/141682" target="_blank">📅 19:18 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141681">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SgE4MNcPP-QTnKgDUCdEKgbqYDCuIIWKa5nG90OZXCBVQsJiE7olDB9ChH-tSaFRuei9IIIpjbhsZzVmHQr9ivMmAS7P75BBlcIeGYRF7xx2DcSQaoLpP8c5XEa3Gf7Km8Um4H2tMWNkmfkBVDIIxaXiFPHS9qemuSvBrZV5rfqxIhLekcmpCcVuZ8prJd6zq_dB-2MHpyZQoBCHH3JiKRuXuE9bTtV3COKXpa7nkR6dV3wOIbEXNcFWQx37_3JtA3Je4ME_YayahVSDf4vWESYYKnwMOSWZ6lZQT_824MVIPW8EUiTpi2FoeNNl9ugrvNJxdRq8AefJM4KHPobwpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت دفاع روسیه: دو بندر «اودیسا» و «یوگنی» در اوکراین را هدف قرار دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/141681" target="_blank">📅 19:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141680">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
فرودگاه بین‌المللی قشم با پایدار شدن شرایط امنیتی، آماده ازسرگیری پروازهاست و برنامه پروازهای تهران، مشهد و اصفهان طی روزهای آینده اعلام می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/141680" target="_blank">📅 19:12 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141679">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
فوری / وقوع حادثه امنیتی در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/141679" target="_blank">📅 19:10 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141678">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f35437e583.mp4?token=nlpneAc5dXFk_Z-o3EO_41Ek1OZK-ZGfFk8xu4KZwJcXqLZt0JsF5PSewXTK8C47xCDy2rUmP3FZOGOi7v5_WpV_8GVKHYBTCLQmjBuwIWIvkg_UxXi7JmB5om6p2zk5RN_Fj8pWPygzFF8Hbt4Nc7FRV0Bg6vp-jjGs2vPTSelkTlvqnytD2PTrjDPbjBpgBgWkM4CGUV8zJaczXykQ2sRIvqm_VV5aqPQtP-o2O-oqplauqO9p5DVgIrBx5nZ19SqesCMt17VtlDIFP4yPwZp4AUv3Hr2Yxo-1k4foVKcYuoIv9sLdu0kxqUyJbbqynAqRAbzuBnTuPZrVw3m1J24FHL-GaA1aoj_zzlEajFTzPH8eQ7A1vb2wP9EeT4myVYSKMRCS3X3jkBaODZ0ck59h3GTdMcT0R1C6HeGHOWWsyFInbnkrKY90M8DYpOuQC7XJoXA-IqY119zuYsC5d682ggKhldo4ryV66Nft5IdijXsY-rdZQ2ny-weLleIsFHDL_cPFSkKPZeL0hA5OqxEYS5XEUhgYPO3c3BmAfXHsyxlewg6L3mmf7lpT4QfJpI7kdOLgiAHfIUyomNAzyPxJv-LeycRrWrBKl6Ck8eSixnvwo2BOgbpezqq0fBxMjaY05tAfC5v6uegdcQn98uWh0YnAp6c9uozTW5tnhfs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f35437e583.mp4?token=nlpneAc5dXFk_Z-o3EO_41Ek1OZK-ZGfFk8xu4KZwJcXqLZt0JsF5PSewXTK8C47xCDy2rUmP3FZOGOi7v5_WpV_8GVKHYBTCLQmjBuwIWIvkg_UxXi7JmB5om6p2zk5RN_Fj8pWPygzFF8Hbt4Nc7FRV0Bg6vp-jjGs2vPTSelkTlvqnytD2PTrjDPbjBpgBgWkM4CGUV8zJaczXykQ2sRIvqm_VV5aqPQtP-o2O-oqplauqO9p5DVgIrBx5nZ19SqesCMt17VtlDIFP4yPwZp4AUv3Hr2Yxo-1k4foVKcYuoIv9sLdu0kxqUyJbbqynAqRAbzuBnTuPZrVw3m1J24FHL-GaA1aoj_zzlEajFTzPH8eQ7A1vb2wP9EeT4myVYSKMRCS3X3jkBaODZ0ck59h3GTdMcT0R1C6HeGHOWWsyFInbnkrKY90M8DYpOuQC7XJoXA-IqY119zuYsC5d682ggKhldo4ryV66Nft5IdijXsY-rdZQ2ny-weLleIsFHDL_cPFSkKPZeL0hA5OqxEYS5XEUhgYPO3c3BmAfXHsyxlewg6L3mmf7lpT4QfJpI7kdOLgiAHfIUyomNAzyPxJv-LeycRrWrBKl6Ck8eSixnvwo2BOgbpezqq0fBxMjaY05tAfC5v6uegdcQn98uWh0YnAp6c9uozTW5tnhfs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو درباره هند: این هفته، من مکالمه دوستانه دیگری با دوستم نارندرا مودی، نخست‌وزیر هند، کشوری «کوچک» با ۱.۴ میلیارد نفر جمعیت، داشتم.
🔴
حمایت‌ها در آنجا عظیم است. ما در حال تبدیل آن به روابط امنیتی و اقتصادی هستیم.
‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/141678" target="_blank">📅 19:03 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141677">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
باراک راوید، خبرنگار آکسیوس: با توجه به نظرسنجی‌ها، نتانیاهو در انتخابات پیروز نخواهد شد و ترامپ نیز همان حمایت مورد انتظار را نشان نمی‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/141677" target="_blank">📅 18:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141676">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
رئیس صنایع نو سازی ایران: هرکی خودروی فرسوده خودش رو اسقاط کنه بهش ۴۰۰ میلیون تومن وام میدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/141676" target="_blank">📅 18:54 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141675">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
آکسیوس: اندی بیکر، مشاور ارشد امنیت ملی کاخ سفید، در هفته‌های آینده از دولت ترامپ استعفا خواهد داد
🔴
این در حالی است که او نقش مهمی در سیاست خارجی و تصمیم‌گیری‌های مربوط به امنیت ملی این دولت ایفا کرده بود و شخصا در مذاکرات با ایران حضور داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/141675" target="_blank">📅 18:49 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141674">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
الجزیره: اظهارات ونس مبنی بر پایین نگه داشتن قیمت بنزین به عنوان هدف اول درگیری با ایران، نشان از تغییر موضع در قبال جنگ است
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/141674" target="_blank">📅 18:45 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141673">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
فوری / وقوع حادثه امنیتی در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/141673" target="_blank">📅 18:44 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141672">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
خبرگزاری هندی: پزشکیان به زودی برای شرکت در اجلاس بریکس به دهلی نو سفر می کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/141672" target="_blank">📅 18:41 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141671">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
وزارت نفت عراق اعلام کرد برای صادرات نفت عراق و عبور از تنگه هرمز، با ایران و آمریکا مذاکره می کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/141671" target="_blank">📅 18:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141669">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LnbZwwlslvlsEzwnzs0GkLG2b_nRoMpVX0jCg3kA-qwgTdU8RIz2R_W8odfoXkdBSwB1VMr38vWm7JITAreTyYfZ1WoMnLZTwNbyrlv3fyJcrJeNkoppE3le8IbgNsT2KNZZgx2sGfeSL6kxZVBiHVDVupd35Z6SzYBIIIB9Kyyhs7N5IttDkOll8FxB1EbOjJXjy-QzIzeFCpNJtMGoCTQ3b119eAq_wzprLyFIVxzPV5ot-we-vZ09YE210LmhfoJOxi-8j2W-bYkjM8MfJAsyUdE2txMqQnnoGSA2DDGgfNuxkNr3yeyiYnSjOSN0v-wAnojqrnqbVD_EPOfnig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار آمریکایی: کارولین لیویت، ۲۴ ساعت پس از آنکه متوجه شد ترامپ او را در هواپیمایی که فکر می‌کرد ممکن است به آن شلیک شود، رها کرده تا بمیرد، استعفای خود را اعلام کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/141669" target="_blank">📅 18:26 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141668">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
رویترز: اوکراین از روسیه خواست تا در دریای سیاه آتش بس برقرار شود اما جواب روسیه مثل همیشه “نه” بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/141668" target="_blank">📅 18:23 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141667">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
خبرگزاری رویترز به نقل از یک مقام آمریکایی و یک مقام اسرائیلی گزارش داد: مقامات کاخ سفید به نتانیاهو فشار می‌آورند تا خشونت شهرک‌نشینان در شهر قصرا را محکوم کند.
🔴
واشنگتن پس از اطلاع از هدف قرار گرفتن خانه یک آمریکایی فلسطینی‌تبار در شهر قصرا، اعتراض کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/141667" target="_blank">📅 18:19 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141665">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c20969ce7.mp4?token=q8A2dxIz2leWihiKMcbbpaRB8vo4rVT4ExC-TdJjJuwNdbWQvKVvMf0F1D8dYIzIEZYQ4NoltNk08fsgyEfISCnvjNsuNJh26JOq6sDwIKHy0WNn3ZRjGsAY09E4Wgq9rkj6kHSw6aMDY5DZAW6dta8uOxd1mrOjwCuxvaGDddMIMzO0EQfF1ZCFSuvE5U6fEIbgDWPTf4Dd5ciz2D6sie8NSEO6rd-xkuvOsIRhYb0Wn_348CXljjD9a17EPqX19NiegCWuyoH2TZeuI19AfwwoI_oh_pFE1e1pHNvGoaVfLKEsugbbujXfITKxzWDDfwFHhe6ttrGRY5AjrnOKJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c20969ce7.mp4?token=q8A2dxIz2leWihiKMcbbpaRB8vo4rVT4ExC-TdJjJuwNdbWQvKVvMf0F1D8dYIzIEZYQ4NoltNk08fsgyEfISCnvjNsuNJh26JOq6sDwIKHy0WNn3ZRjGsAY09E4Wgq9rkj6kHSw6aMDY5DZAW6dta8uOxd1mrOjwCuxvaGDddMIMzO0EQfF1ZCFSuvE5U6fEIbgDWPTf4Dd5ciz2D6sie8NSEO6rd-xkuvOsIRhYb0Wn_348CXljjD9a17EPqX19NiegCWuyoH2TZeuI19AfwwoI_oh_pFE1e1pHNvGoaVfLKEsugbbujXfITKxzWDDfwFHhe6ttrGRY5AjrnOKJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک فروند جنگنده
MiG-29 اوکراینی
امروز در منطقه اودسا در حال تعقیب یک پهپاد روسی Geran مشاهده شد و در نهایت موفق شد آن را سرنگون کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/141665" target="_blank">📅 18:12 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141664">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O3z84ZGg4KlrTuBHGhm6EdzvygbLka3N097lk7KyyYk3sn5lVUNixvv9xFRItKr9cU87hvTA5XQWMRq5xjUvJ0_9aHltOrcAVV3lVXK6gYy2y-LbVMehfNIrgKvd2DrepJ0-jW4aYOmZSjE42klnKy9-A2UAPU5v1SFySi6jcMl7nXtDoiZHW1gHbQW0n6Uzh-3Nhl03-YzbCMQdJ7rgC7qAInE2RjOwsYvarxFg8wDDBb4m5IkHqbZ_Ixk8rfg9n32xZq-TZ1J6uQFVSFxQnQjyLH7oEX0pQNepjLzcRD3rGBzkLbRNCir9aJinV-SMDd2T77nWW6_GUSoQy_seVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بازگشت فعالیت هواپیماهای سوخت‌رسان آمریکایی در تنگه هرمز، همزمان با نزدیک شدن به پایان آتش‌بس ۶۰ روزه میان آمریکا و ایران.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/141664" target="_blank">📅 18:03 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141663">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ms1w8YbLLqLK6rTJC_9EWPprx7dxz7nVmKaITsOsarqUgu1e5tDO4lw519F6AG1o-klvNent8KFMxEraPiRgJvPd_zxWY1YxDtX-lvnL9fxjNOF1QrGupHdMFqOfEojpF7Su6O5Z2aZqPfR7zWTmNkEw0go4FoLA7BRskAHR7DFusXTkgOrWb5xygSkFi88AygWtIzHAoudTgNNVRUvfvYi12Qjm_1w_zgYofw9_O82CSWBQ5-Uzpc-ztXPo00UioG1HPwX4LhGyXdau5uy6tS1kKr7YkIs8YblKjFusPpp6skcmziPw_d0-_xXwpvwyfcmdnPyNLk74rR5kL4JAWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تانکر ترکرز: امروز (۱۴ اوت ۲۰۲۶) یک ابرنفتکش از نوع VLCC متعلق به شرکت ملی نفت‌کش ایران مشاهده شده که در حال بارگیری ۲ میلیون بشکه نفت خام در اسکلهٔ آذرپاد در جزیرهٔ خارک، ایران، است.
🔴
اگرچه این اولین محموله‌ای است که از اواخر ژوئیه در این جزیره مشاهده می‌شود، اما ایران بارگیری نفتکش‌ها را در سایر پایانه‌ها ادامه داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/141663" target="_blank">📅 17:58 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141662">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ckQNkCsX71nbFbUGyt1cmQQUUPcxmGF4b5O3iUFgmIu_YNd-jPP3_duhbft71NwBUw0vfYVtg_r-t8tv8wVgshIlNHkUsMCBbCTZj6I-qcZxJqM6DVKcw5EkyPNoBv1A9TgqybwO1nFMXR1P-5DSKAKsuKMPRu10ZkJWIUTI1GcxcyBkn1Kp6lXCDBz_yug9FcXKWvfL66ckdy2gpcfOfh59xzGpaFwP8D2TA4Zbp-AbYBIS1cTNuis3x6FSSm-weBQ3zxlX-jxbxOzBrA62h9qycrjUTYJi2zZSaoyCZjX4eXaIGtdMnIS32skYxy8BkCCif5H4WVj4l7nplu0bfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
خاتمی، امام جمعه تهران: آمریکا بیچاره و بدبخت شده،  جمهوری اسلامی به یک ابرقدرت در جهان تبدیل شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/141662" target="_blank">📅 17:47 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141661">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
سی‌ان‌ان: هیچ مسیر واقعا امن کشتیرانی در شبه جزیره عربستان وجود ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/141661" target="_blank">📅 17:30 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141660">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/len4Uir4rO1TVDcvs61E-OrKIjJknKjWIp3Rcd8O5dRL3qevTW2TLB1p0L1g8md9aP7zAzoTJA4sZLSlrzVkYh45W2l68SQ4WMlDmFuVlKRVSBBHNxudxzO7LcEVqyj4r2ZUTTmplvsqmCAgD6X-pochLIokgDB-IVaIQExcAhkirtNtutAoTLcO6VDZQ5m4JLZFh4iA3KArsmdkfyNNJ3F9rMnU0ZoePSsXSc63qFlY8SNDy8CubRPuEl5AmPZGxeQR6rlJeB2s_vPkHt9qKhDnE4s0jb94ea3keu6eN2zSAn7Qa0klDmcmoJ0i_bsmviYicsxEuPraXLcRdggP2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انتقال تجهیزات نظامی ترکیه به عربستان سعودی از زمان توافق اخیر مکه همچنان ادامه دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/141660" target="_blank">📅 17:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141659">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
نیویورک تایمز :
پوتین به نظامیان ارشد خود گفته بعد از تموم شدن کارش تو اوکراین، می خواد کشور مولداوی را تصرف کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/141659" target="_blank">📅 17:06 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141658">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SZYRm2F4sxDpo3PlORZjKriG-1Sk2qvM87tpbDevIKYrEbn9AKXxuyH6kUPqNwzq9cP0owWKJ7S22eIUkqiYgJ3pmkWHdnv0MuynIEoA3HEvNlcyBpTg2Ua_9B5AdgTnn-GmD6aZZlieHPFhBbforc7bO5sxiZ8FruUSqKlkNmj8kMFW7eODBcbYRFSYAjzEN0Inddhb2K6PEfugiJtVKD0AH5DGClio7pPyMlXLtp4tGhGMxPvnhbpNacwsdkSMwQE-DP5Er3ytgIymlmLXBLzdN3EHYFkzd4p0k_boa2zzgwj8_OOMnvFVWjVDXFg6oK_atuUU6LzWXNJaWXsgmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علم الهدی: دشمنان جمهوری اسلامی مفت خور و شکم باره هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/141658" target="_blank">📅 16:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141657">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
واشنگتن پست:
حتی اگر جمهوری خواهان در انتخابات شکست بخورند و سنا و کنگره هم رأی به پایان جنگ دهند باز هم ترامپ می‌تواند وتو کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/141657" target="_blank">📅 16:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141656">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kW68-mmoUzr4mwwdBQMjJgYvHgYptxuZgxJAJnB_7_NPERjC4jutW8heh-hH0IPjnBTwkQC_4HW1hTtOKwl6VkQszFfQS8QjMYBsT67CvYlVvq1RPUQXYvHeRGSAC_tq63sOorwUrTD59-jn4MkC6bJfGtLsxtm_Gz_9XL6qeQahrZJph_5X5cfLKGfCDuVCeXo3WJJ2EM_rOvAqpFd-cMRXY9cCBWNo1CUOV1jfqo2viCjVJI8YYCR1bS-Xswpp05xgWzXeNFeQyTluXE4sMYw0xfFCw_gp2HSSVseU7AOJCnCoD0YdOyVdOKdFuuuQxQUOXEaL75EBZeZpLha0-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منطقه علی الطاهر هیل در جنوب لبنان، تقریباً هر روز مورد آتش توپخانه‌ای اسرائیل، حملات پهپادهای کوچک و حملات هوایی قرار می‌گیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/141656" target="_blank">📅 16:30 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141655">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea185b49e4.mp4?token=JW-wK_fok3p4wJZEOO3MIPgKL9cS-jcYtzAIplJSkxLQCmLgvKDqtJEmBddVBrWJ6CF6oma_6bLPOrRGr8VVT4WBiI9Qj5EE12ci5FzGYh7xV0sxOcQ86IBNrGQ-IkhA0Kk67MPnOrNqs5aBJtc84JrpBmblon8bMy1LEivzp63CF-c35UdR0JVJ45wIoKRfVvygsC10fYf8CzRAlOhmPCT5DPR4dZLT9OVVn2zfm2xAouozMxbeB2Jhe_R6yzAawuat6NJ-lXGvoVrYTR2UZmxvlZyYTXe5g_mdaFs1WBBRnxm2X0Dtu-MsVl5V6IydasJB2vJq2gHRrxQ9oDm39jtX2uXoWgSLngNtiAbgZalb0z3y_cXOicZhgt9P_QaOROeAlDELdv1B1H4-jfPgOxAYusA9DNBuvxSkVfmuSB6uwA_cIuJXs4ZI5q1fXVR0IB1eDqRq7u9Fxc0XVWwr5oI0ndGU5mMVFxZGQnAVyPEESRundT8q6COBDIdsauTQ64meY5XFwVF7sW37gX51kOVcym5-iat9FbPooSQU-WotJGn5YjmHsVKmskTd6l0EjzQjS3WEJGHprk5xd1lONH9f48Y1_uRx-MTO3jn-z33aRt1kQZ6S6vMU5lR2CX3hCz2_xszNUk0Vk-jQ5eYF3bp9sWi7I88o60IWHelznBc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea185b49e4.mp4?token=JW-wK_fok3p4wJZEOO3MIPgKL9cS-jcYtzAIplJSkxLQCmLgvKDqtJEmBddVBrWJ6CF6oma_6bLPOrRGr8VVT4WBiI9Qj5EE12ci5FzGYh7xV0sxOcQ86IBNrGQ-IkhA0Kk67MPnOrNqs5aBJtc84JrpBmblon8bMy1LEivzp63CF-c35UdR0JVJ45wIoKRfVvygsC10fYf8CzRAlOhmPCT5DPR4dZLT9OVVn2zfm2xAouozMxbeB2Jhe_R6yzAawuat6NJ-lXGvoVrYTR2UZmxvlZyYTXe5g_mdaFs1WBBRnxm2X0Dtu-MsVl5V6IydasJB2vJq2gHRrxQ9oDm39jtX2uXoWgSLngNtiAbgZalb0z3y_cXOicZhgt9P_QaOROeAlDELdv1B1H4-jfPgOxAYusA9DNBuvxSkVfmuSB6uwA_cIuJXs4ZI5q1fXVR0IB1eDqRq7u9Fxc0XVWwr5oI0ndGU5mMVFxZGQnAVyPEESRundT8q6COBDIdsauTQ64meY5XFwVF7sW37gX51kOVcym5-iat9FbPooSQU-WotJGn5YjmHsVKmskTd6l0EjzQjS3WEJGHprk5xd1lONH9f48Y1_uRx-MTO3jn-z33aRt1kQZ6S6vMU5lR2CX3hCz2_xszNUk0Vk-jQ5eYF3bp9sWi7I88o60IWHelznBc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رو خانا، نماینده مجلس کنگره آمریکا: اگر روزی رئیس‌جمهور آمریکا بشم، بلافاصله حمایت‌ها از اسرائیل رو متوقف میکنم و کشور فلسطین رو به رسمیت میشناسم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/141655" target="_blank">📅 16:24 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141654">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">💢
زود بیایید اینجا خبر خیلی مهم
👇
https://t.me/+nCexQYLuuONhYzg0
https://t.me/+nCexQYLuuONhYzg0</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/141654" target="_blank">📅 16:19 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141653">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
وزارت جنگ ایالات متحده با شرکت‌های "بوئینگ" و "آر‌تی‌اکس" قرارداد بست تا تولید قطعات یدکی موشک‌های SM-3 را افزایش دهد. این موشک‌ها برای رهگیری موشک‌های بالیستیک در خارج از جو زمین طراحی شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/141653" target="_blank">📅 16:11 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141652">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lnZ1GKoE5ZebT0VncwJ3BYYN2tPBz2GOt6iwKCHZ7sX6b9tLC9xnLKE7Kdfr4s-6s6A701_jnN-t7QPlg2tPnaj7TQbzMdLmYUJ99cX_LEhFHt84luG35NKU5cPeECJ1Bl-XBJ4n09-YsJfAFyd2zA7OIXn-E0Z7am-TtGSB3skZlO80Jjxrstva0GuVgueFuEyeUd-7CKdVYd3M_IcCE6bRJTU9qZEtBuYKi3pNbeF8evnY06adTZP6b6_86TNSBMz67LSXfG5mV4j70bz7Rl430ssYK5-sarRyJ5hkw8_o4c6VC9gxkAaCXvX5GmivrUIHD9HuTk4pNZWwRmXtUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیران خارجه ترکیه، سعودی و پاکستان با هم دیدار کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/141652" target="_blank">📅 15:55 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141650">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mm8p_WC6czKsuC5R6pbYpfP4mktnLGcApvpCf1Jz0k25mHLCqFYlxoQWVxaDeU0zJ5D5VQxeSTocxk3_RvBQu8WtChtk5vjm2dx-Cw8uhTkkgXYKkFYrlVLeTuGsGEhpHr-A_trjwCOGSe3vqP6wNlHk-Qc3u1SJ67bArCbzDq3fgPr5sGsNm4bYpSrDFSPsJAQnr_kCSjCFKeK5gRY6QWUyiM724WwDQ6k7jin_pxMLFH6RU55dCEYxySAphzNctNUZnop3swCCH1bhYmkJZVuyKA10yAIg7PAyN_PAJ_XgympzJlHmFgKnbsYkKmi-I1Ui91nL_ldy42_-NKSLJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علم الهدی امام جمعه مشهد: آسایش و زندگی راحت بدون داشتن انرژی هسته‌ای محقق نمی‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/141650" target="_blank">📅 15:44 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141649">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
به گزارش وال‌استریت ژورنال، ناتو پس از ورود یک پهپاد خارجی به حریم هوایی لتونی، چهار جنگنده را برای رهگیری آن به پرواز درآورد.
🔴
این پهپاد در نهایت توسط جنگنده‌های ناتو سرنگون شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/141649" target="_blank">📅 15:39 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141648">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
وال استریت ژورنال: توافق ایران و عمان برای بازگشایی تنگه هرمز در حال نهایی شدن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/141648" target="_blank">📅 15:35 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141647">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dqsDyTXQlanMTK8zBHkdC78bxzJgEZJrXNhK8_MhyL7G-gb4EHp-2KV_nuYoARgOG2M-2fcRCR8Osp5s0z2PUhFKQfHmLmWTyMJ9p7UAtQC4SEDpWAYG0zkCuWe_xaSIZbkjXgODrKfAhSo6ZZww26wufjcjrXyzDe-T2LMnrC_Vdx8hdLwtBqaydim75OpqIwh5YMpCVlEtwoIpvANIesB2WNjk2EpKmu36WPqxTaM7xkWx42sf1hVNZQu76IufggsRRM1iM5ZixOa4GTmzkcKe8KNXxjTTQfunCe5uaK3kuDrN3CIJmRgliv5pTTpebvk-g5seTHSWSiH9VaG4ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
از نسخه افغانستانی دیجیکالا به نام افغان بازار رونمایی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/141647" target="_blank">📅 15:29 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141646">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
اکسیوس: فاصله‌گیری ترامپ از نتانیاهو؟ او هنوز از نتانیاهو حمایت انتخاباتی نکرده
🔴
رقبای نتانیاهو از ترامپ خواسته‌‌اند بی‌طرف بماند
🔴
ترامپ از تصمیمات نتانیاهو کلافه شده و گفته «بی‌بی بزرگترین دشمن خودش است»
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/141646" target="_blank">📅 15:23 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141645">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
به گزارش بلومبرگ، روسیه هم‌زمان با ادامه جنگ در اوکراین، هر ماه ده‌ها هزار نیروی جدید را به ارتش خود جذب می‌کند.
🔴
این روند نشان می‌دهد مسکو همچنان در حال تقویت نیروی انسانی مورد نیاز برای ادامه جنگ طولانی‌مدت در اوکراین است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/141645" target="_blank">📅 15:14 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141644">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
پلیس اکوادور در روز سه‌شنبه، 469 کیلوگرم (حدود 1034 پوند) کوکائین را از یک کامیون در نزدیکی مرز کلمبیا کشف کرد. بسته‌های این مواد مخدر با تصویری از ارلینگ هالاند، ستاره فوتبال نروژی، مهر شده بودند.
🔴
مقامات ارزش این محموله را بیش از 11 میلیون دلار آمریکا و نزدیک به 20 میلیون دلار اروپا تخمین زدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/141644" target="_blank">📅 15:04 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141643">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
سپاه: بازم پهپاد زدیم الله اکبر
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/141643" target="_blank">📅 14:58 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141642">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">💢
تحلیل عجیب از اقتصاد آینده
👇
https://t.me/+nCexQYLuuONhYzg0
https://t.me/+nCexQYLuuONhYzg0</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/141642" target="_blank">📅 14:55 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141640">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/016cac103e.mp4?token=snY3u2plfyK5YRMImNuVyvIL60RvfyxkciYYcvnKtDB9Db-3bJ20-xyXiEMZsQo0hmgZplvXoPLlFk0IBEMDJGX9DdgyrpSYowe3IuMfN7xSW1cgCuURTz2NMDMii25f1j7n2QM6B4cIBS0Vv4a4Ih44Dvczy7n0luaytUz0Lgtx9mhw8wPB47vagS9XMYl2Rd_8CCHD6p0uwMYiwG3itmPoeY7rZBoBZYVDZFl7Jloo-Mr6naOFEvC8pqzxAg8fOVGrtHEPdeYwPGJ58fgk9aIfks6Ie4-gjvmUJ6YW_4wO4FkHa9PbkE3iQWHG-_RKgs9r4OASZHFjIIdfOJBUVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/016cac103e.mp4?token=snY3u2plfyK5YRMImNuVyvIL60RvfyxkciYYcvnKtDB9Db-3bJ20-xyXiEMZsQo0hmgZplvXoPLlFk0IBEMDJGX9DdgyrpSYowe3IuMfN7xSW1cgCuURTz2NMDMii25f1j7n2QM6B4cIBS0Vv4a4Ih44Dvczy7n0luaytUz0Lgtx9mhw8wPB47vagS9XMYl2Rd_8CCHD6p0uwMYiwG3itmPoeY7rZBoBZYVDZFl7Jloo-Mr6naOFEvC8pqzxAg8fOVGrtHEPdeYwPGJ58fgk9aIfks6Ie4-gjvmUJ6YW_4wO4FkHa9PbkE3iQWHG-_RKgs9r4OASZHFjIIdfOJBUVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
سفیر آمریکا: در صورت تحویل سلاح‌های حزب‌الله، حملات اسرائیل متوقف می‌شود
‏
🔴
میشل عیسی، سفیر آمریکا، در پاسخ به پرسشی درباره زمان پایان حملات اسرائیل در لبنان گفت: اگر حزب‌الله سلاح‌های خود را تحویل دهد، «همه‌چیز متوقف خواهد شد».
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/alonews/141640" target="_blank">📅 14:45 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141639">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2252485e79.mp4?token=mCtKLucJQQDcMbLDw4S8-3H71mB6QYVKpH7IwEQ1Uubch7t1pMJg0SMSMNw4mrelQNelYXsuRJVS_-jQ4khgNRhDBaZ-cY6tEAlRQDUUgWrs37N9xVGp_mzknoUELq0OgVlu30yXhYb8ZpEb2AKFnra5dZ_FszrnXxtGEXSc3aVru-CysjzcR9KQIH1ts1RB0_vlNutT_NNJ3SkzSXUBZjHJfHJ5qy_N535_PAZ83Szd3bJIi1FDBPSe7QZghUo3l6abag6T153RqwwborQjAD1v4f7XQbU68b9u8W2vUzTLkBtJtZ52LJGvjgIj6ajMMk38y_btsZ8PDZzd1vkIIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2252485e79.mp4?token=mCtKLucJQQDcMbLDw4S8-3H71mB6QYVKpH7IwEQ1Uubch7t1pMJg0SMSMNw4mrelQNelYXsuRJVS_-jQ4khgNRhDBaZ-cY6tEAlRQDUUgWrs37N9xVGp_mzknoUELq0OgVlu30yXhYb8ZpEb2AKFnra5dZ_FszrnXxtGEXSc3aVru-CysjzcR9KQIH1ts1RB0_vlNutT_NNJ3SkzSXUBZjHJfHJ5qy_N535_PAZ83Szd3bJIi1FDBPSe7QZghUo3l6abag6T153RqwwborQjAD1v4f7XQbU68b9u8W2vUzTLkBtJtZ52LJGvjgIj6ajMMk38y_btsZ8PDZzd1vkIIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از بقایای جنگنده اف۱۵ منهدم شده آمریکا
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/alonews/141639" target="_blank">📅 14:39 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141638">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
ترامپ در حال باز کردن در برای نیروی دریایی ایالات متحده برای ساخت کشتی‌ها در خارج از کشور برای اولین بار در چند دهه است
🔴
سازندگان کشتی خارجی که سرمایه‌گذاری سنگینی در کشتی‌سازی‌های ایالات متحده انجام می‌دهند، می‌توانند تا دو کشتی نیروی دریایی را در کشورهای خود بسازند و به ایالات متحده راه سریع‌تری برای گسترش ناوگان خود بدهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/141638" target="_blank">📅 14:30 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141637">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
وزیر خارجه روسیه، لاوروف، در مورد اوکراین: ما روش‌های خود را بسیار سخت‌گیرانه‌تر خواهیم کرد تا هر چیزی که ماشین نظامی اوکراین را از سوی غرب تغذیه می‌کند، نابود کنیم
🔴
و ما همین حالا این کار را انجام می‌دهیم. و آن‌ها همین حالا شروع به ناله کردن کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/141637" target="_blank">📅 14:23 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141636">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DnbICnGPkPiOJqd_o_s304sAQOXhS01akJmpRZzHMuO__Beb_JHiMorbaatDGxd5D2VRbjTRL6zILEeIUoG3RiMx9xSTm9SCcRpVwSbw-GopuvnuqZTnwSlZSsYI-bRwVkxWR8ovFwj_TXRyCYnq0LSxrw5jXi7FjKZ1d6QkZS1ZyZLkG6bzXo7M6VNs4mug_MNq6CoKso1QGbv3csW2dGUaCEsYwWQPUYWMqRg3mIzDJ5dL4xkbM3gf2kffksVCQ8uvk6nGmrWN9nLsn9u-14n_kQSoyjD8EMY1T8pLV_GQQjL21yGdVwco4ticAp8DUxIZuzcGB24DaqhYR9iUsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کویت، بحرین و مصر حملات ایران به دو کشتی اماراتی را محکوم کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/141636" target="_blank">📅 14:14 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141635">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
سخنگوی وزارت آموزش و پرورش: مدارس در سال تحصیلی جدید همزمان با اول مهر، به صورت ۱۰۰ درصد حضوری فعالیت خود را آغاز خواهند کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/141635" target="_blank">📅 14:10 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141634">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ejo5iTuXM3UCZq51Xl38HYZLO7ZbfH0msPTGvpFOOJogyt4-Z8qjY-8pD9msJ0n7prVMa4-V0Ud_5rjnSHjloXsF3r1IwZPLtdHyMeFl2TZx2K61UZLbtrZE1nOEdgo9tr4dXdikqEXFRz3zFDtMAL66hHIrZ6v3qkEOxyzLf7jnobnEISRymQwLXLx7JOwCBJ-PpSJEWVwUEpbNV7R-4kmAD6mc_f9iEb7T79l02rSSlLbvYP_msy5wyjiEZ2fQeIiY9FR5-g7MXStyVqfGVawvYYnVffEJncvFFTRFPdgwTyH9gcGtMV3PQyVJic4fpIAvxy9SRSjAXzSw8yzgoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لهستان در حال بررسی انتقال یک دسته اضافی از موشک‌های رهگیر دفاع هوایی پتریوت به اوکراین است و انتظار می‌رود تصمیمی در سطح بالای دولت در چند روز آینده اتخاذ شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/141634" target="_blank">📅 14:05 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141633">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
دیدار کاردار ایالات متحده با وزیر خارجه پاکستان درباره تحولات اخیر منطقه‌ای
🔴
اسحاق دار: اجرای کامل و عملی در متن و روح تفاهم‌نامه اسلام‌آباد تنها راه پیش روست
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/141633" target="_blank">📅 14:03 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141632">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
وزارت امور خارجه عربستان سعودی:
ما با شدیدترین لحن هدف قرار گرفتن دو نفتکش متعلق به شرکت اماراتی ADNOC هنگام عبور از تنگه هرمز را محکوم می‌کنیم.
🔴
هدف قرار دادن دو نفتکش شرکت ادنوک تکرار غیرقابل قبول حملات ایران به کشتی‌ها و نفتکش‌ها است.
🔴
ما ایران را مسئول ادامه این حملات می‌دانیم و خواستار توقف فوری آنها و احترام به قوانین بین‌المللی هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/141632" target="_blank">📅 13:55 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141631">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
شورای عالی انقلاب فرهنگی: ۷۰ درصد مردم کشور تو تجمعات شبانه شرکت داشتن!
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/141631" target="_blank">📅 13:49 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141630">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
زمین‌لرزه‌ای به‌بزرگی ۳.۹ ریشتر در عمق ۱۱ کیلومتری زمین، همت‌آباد خراسان‌رضوی را لرزاند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/141630" target="_blank">📅 13:46 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141629">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
ان بی سی: بخاطر نگرانی از شرایط خدمه، ناو آبراهام لینکان به آمریکا باز می گردد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/141629" target="_blank">📅 13:44 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141628">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbd7a971f8.mp4?token=En5HIkbmFw95ZC67nsdFfp3rzm7FRkHp5gJvkFop4OstlVpRG2Lj4d_bRG4gnpFbqd2Nj-qCPChbK-lC2Iw0hlJhdw1ePiMc0Zu88Vatz67NlW4O5eOErnsPKQTC22rO7Xpuxy8kaudzNiiRC0pup6BghLeTz6mq1tDDKUxmOCW6rj-ZmIor-T-S9FpzAZVntNn_ZGxN26GUkiSl8c1na9jybXJG4ppqcc6iUn-0GcdGuFMwPP9KPdvNQxTs0qGzBlWPx8ftc9aEkoIub-PWwgFduct61BkRjalbqIEvhHq99dOpWoTRHosn_68hvdrAAvVyWezZEzafEXCVcJznow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbd7a971f8.mp4?token=En5HIkbmFw95ZC67nsdFfp3rzm7FRkHp5gJvkFop4OstlVpRG2Lj4d_bRG4gnpFbqd2Nj-qCPChbK-lC2Iw0hlJhdw1ePiMc0Zu88Vatz67NlW4O5eOErnsPKQTC22rO7Xpuxy8kaudzNiiRC0pup6BghLeTz6mq1tDDKUxmOCW6rj-ZmIor-T-S9FpzAZVntNn_ZGxN26GUkiSl8c1na9jybXJG4ppqcc6iUn-0GcdGuFMwPP9KPdvNQxTs0qGzBlWPx8ftc9aEkoIub-PWwgFduct61BkRjalbqIEvhHq99dOpWoTRHosn_68hvdrAAvVyWezZEzafEXCVcJznow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صداوسیما: همه چیز دوباره گران خواهد شد
🔴
رهبرمون هرچی بگه همونه
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/141628" target="_blank">📅 13:44 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141627">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qdwFxJ2O1I52QW8bLgkCNlWPEAdW4dXGJJXC2-6PpbVcJuWnD64V90ApHUkdimxIsCNDOgNvpYVJVUTQQuaurw5_Fz1odIt9CHGdzGEurL6wU9VZCRxefPkmsgZ3cfqYdRRDPsb9sxI9x9j_0Pdu9z-uIm-AOvlvIyvbf7MeS4vQ72VtpZmYvN-wYN5kLdpypKx7YD1OrYDssbKCLEpU24ZP7fcL95XWPxiXkdAOu1VOys_FDW0J-gelEI0pZO-IePdK_xs1DAG7YyAwhnR4BGvnPPTeDJuOOK2oRjmO94ortvwLVVspsbmD4AO-eay6IM111GptLU1G9Im4M2JHaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امام جمعه قم: آمریکا و اروپا و اسرائیلی ها می‌خواهند از قم انتقام بگیرند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/141627" target="_blank">📅 13:41 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141623">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K0B5TtkuyH_O9za2hQxoj2frfowLVWi4_B97jQANB7eWaiWA6Z13UfHk2XRsT_IRkAwH96jTjH8rZdt-bhTDZI-ZaEVJQFuzT0TbWV5sxdvmfSQZlIdC3H_bPw_c2gXOV3p9JTFlIG8v2zTnKPlNH5m1yTZkglosFy-cnwMnPwErOnrBksR2NuRKa2GKCvHxEF6T9J9MzEquE0swJaL4oKeWEqydpDU5FwaVRv5YTb7pSsJLFR9xSxLzZxHhSxPjIr4k4uhWgNyUDysq2XLDu6sJImm8nHWULvBu3NZGkcO-2f-xgWkkN88Y2Ma956Zwhtqh2UBmXrei4BMuTliYXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EADHLwurSDo7D7WQ0jdcov-a9q74Qe5SJ82rKb0ScHBKrP8sR9P0moXgshJQmUDC9PRBzhxaosYYyVEG4-LgM2NLMB0vdObQ5-dSuPyHmDlBS2ia0YG8-RASGUk7-m2XQdcOIEsKnwnyEMnpiPzmCyC8PO1FMcXf7RB70A3ZXoVJj4HcwhDy8v1fwp3P_ETNOHhojgKIqdXX5HNfcvVvMXVQ6yiN1_9_O8hZggufH1i-fLV7voURkh2YD8-CrqZ0UiCL-gERZi4MLuTmyPMnzdoKTubdiic2kZSCDS_TYDr7gtYJ1QcRaxuMl3n28sRHuVFAkAlgY31FyHHv4fkULA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T9TieTSM_fh2jygiga_vTja8flAU5Wfy_JMZgw6ahxBhRJQ0YZ2AC5umPR2LXuRjwvpOIY7eGPV4E8tUJDyd7XLNIYbBJPJh8YZtuU3fHarrMhbzIbVR-jKrLg7gV_MlyV7Bgf-PKiqknl-Bs2gVZhTCyFQu2Oiw7QhOV0hkM0a-3pXB8CIlYZapDpR24ukh6WHRKO82tEHbDlybyGnuYetq8K0VVLZ5cpNXV4M0EQv9stwr7K9O-sGzyj-mcjiAs9Vsr4qQgqHEf1JHh8ywyubysK92bLWt9P1zO1WortuWyvj5006rO_-3wubnoHrijmk2GiHvmc9PsIQyY7lk3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S1c3QaDZAY6vnpqQXk7zKU6-0bNOgsyVjeg6ysU-K-NUruHG4HyebyYjHNxc1CSTY5LykHdnghq3Qx7lS1THBb1YHp-IEkz2QcMRHgvagzBhm791r2v3HKPxgj9VTXnFQfzOr-Q0wIxB3BjttxHarKPIRTbmm3bZSsRcBl7iWhzclaLMD2lPHmoa4ZRIUJEoLv_hd4u01_2_IQZs205LDa_2JlPJQWzHEAE5kbT35n2D3oStedOGKCIYAm_wyLjYG6u6-qWs-EJHapRMkrxANaKzC-Gz2IZjJKiAoeXwqj6zyvQ9wh1gdCaICgirm9abmB38uWomc-faKvuEfJCCGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
هگست (وزیر جنگ آمریکا) این‌بار داره شنا میزنه
:
چندروز قبل از جنگ 40 روزه 143 کیلو پرس سینه زد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/141623" target="_blank">📅 13:34 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141622">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c22R0tIUbD6d8TZ3zVGfIcx5ZR9PGy37gMJ7hbG6nSwHPkwiA8sfSkvoy27EgUxSx6tuXpcjlh2gRThQ9RosN4i1G1xrsoDTlc7c1dtvp5wksDxE7B9swyVUbuAF8rpkkiUj8Xlgqzo_YI5ovU2fV2lmMjciBPhGFj8GJQfDLGZ7kGW00IGPI1w-I3cH-KwbSz97HGVqndwZWbhT_MkgNKKXPSuYHaLgpLlk40QV_AxkdsDM3vb3ZbPT_sECPGYGX_G3kVOrKRB9kyaVxr5uRg4kXFeVGIfJUMsIi1Ti6_vJzLswm7tqmLohxhgXg1zgiOzGx8vmfis8iMRRdFNaag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز تولد بهترین پیامرسان دنیا، تلگرامه.
تلگرام امروز 13 ساله شد
🎂
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/141622" target="_blank">📅 13:33 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141621">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19124ce5da.mp4?token=iGiMH9Q1EvwLilVo_7iaUPO-uQQyfbI7JFhMM3gG2bm9Jqvocwy7ELFXTtcFkrZ5l2seXScGHk2RLN7bKEGdISn_lNu42bIwhMMkpz1iGh4-uWTvA-kM-2c9oDPxcE0bwAe5zTZCZw1JW1yuoP_hPgCV8xdUoOdnEwY10BNgHV19WuECya8fEkd6cLEm3GqS5VBAZ7uq3K6xmCJAaCCEDdgSwDeIeGFxIojJG2u3nWd74iiaTAbkfVyQ91cUdq2xwZZfaT56uMIv2LGWCN48YyYmENXkPOOwjzGiap6k5dkmGJsSpUao33szBQXSWgD_wtnXh73MiWa11Jwdv0zaXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19124ce5da.mp4?token=iGiMH9Q1EvwLilVo_7iaUPO-uQQyfbI7JFhMM3gG2bm9Jqvocwy7ELFXTtcFkrZ5l2seXScGHk2RLN7bKEGdISn_lNu42bIwhMMkpz1iGh4-uWTvA-kM-2c9oDPxcE0bwAe5zTZCZw1JW1yuoP_hPgCV8xdUoOdnEwY10BNgHV19WuECya8fEkd6cLEm3GqS5VBAZ7uq3K6xmCJAaCCEDdgSwDeIeGFxIojJG2u3nWd74iiaTAbkfVyQ91cUdq2xwZZfaT56uMIv2LGWCN48YyYmENXkPOOwjzGiap6k5dkmGJsSpUao33szBQXSWgD_wtnXh73MiWa11Jwdv0zaXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای تایید می‌کنند که یک رادار در پایگاه هوایی الظفرة در امارات متحده عربی، پس از حملات موشکی ایران در ماه جولای، تخریب شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/141621" target="_blank">📅 13:32 · 23 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
