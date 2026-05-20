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
<img src="https://cdn4.telesco.pe/file/RT0Y9vEDMtXt0auRdWvIaSKaml12EhoownyGZce2DqM5mz336LwSiJuMv0L425Zd5r7PRyy71QxaSsNOFL0tXpFbxa_0HNQB3NyxJmufBZLjo6Q-MCCcNtPsHOaWydS4sRKWTv3Cs4pX24SA4pplzAoEVzulG0fka03fgo2likFgUzsIi6232vZ20Mry7w27YxjV8CKxOfSBOTYRItkdClZFcTZz06ppjJZaRiDUB34Qa_LKSmLxvBAPZxxUMa2Nv5tttUtxOhp_jywkklYRqi7RCPc7hvNqR-OLJhyzhhzVYvP2elKKNqrZKgqaytWEtg4oUDGZcOJpTCA_2iOh5g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.83M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-30 21:07:19</div>
<hr>

<div class="tg-post" id="msg-436908">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b0109abff.mp4?token=oUBBYO0Wx7QGr4piR7P1BCFgE1SsnyZ5FtbAMbA3M7805JnN8d2vNKQTd6hCUarGXGi0GBF3csWtF3_ppefXXzIDUQ9xVjIp6V65ktommeHKRw-DI4pmlkP1kjlUDlzM0rXeaQhP5zq6bTcyhSr8FMt6eEOAD_tkI3mGe734rQhWoDDHMxZXTFDblk33RWZLNMFrxVIYjWtwRexO9tRAoAeKegOirPzvHDX6ItZe28pIXIDGblJNHfTx724i0YzjXInv6SHw-eb6mog8I6yOkaCzLTqc8RvzQnqmpKgE4SuykajsOxWZ1Lsc7rKZkoohQL65hp68FG7B3WyLxNTsaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b0109abff.mp4?token=oUBBYO0Wx7QGr4piR7P1BCFgE1SsnyZ5FtbAMbA3M7805JnN8d2vNKQTd6hCUarGXGi0GBF3csWtF3_ppefXXzIDUQ9xVjIp6V65ktommeHKRw-DI4pmlkP1kjlUDlzM0rXeaQhP5zq6bTcyhSr8FMt6eEOAD_tkI3mGe734rQhWoDDHMxZXTFDblk33RWZLNMFrxVIYjWtwRexO9tRAoAeKegOirPzvHDX6ItZe28pIXIDGblJNHfTx724i0YzjXInv6SHw-eb6mog8I6yOkaCzLTqc8RvzQnqmpKgE4SuykajsOxWZ1Lsc7rKZkoohQL65hp68FG7B3WyLxNTsaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گرامیداشت دومین سالگرد «شهیدِ جمهور» در حرم حضرت معصومه(س)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 190 · <a href="https://t.me/farsna/436908" target="_blank">📅 21:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436907">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe088cec1b.mp4?token=Qv9O5OPiR7w6kHLXqN2vsfsj6PwGN5zdx0U9pkgKHt2jERCSdo12qrIpMfTvtugZDwWVDnSAuN3bIul-94rTptiKrVnDERIlZs02H7KXmnu_nBiZ2SFLp6a8ExnWF19r3nwiJvYroBfn5ALEXk2f50EE5sQUQ4AfTl3NxRLJUWtyV11_pCjeWdHoR4VOmobVwD0OGjbb0TxHBkZqJkEGRiCYC5IS8FfX2e1WFAa57HG88G1l3SX-bHVDktW7f0JeSj3pR5PD2s_2P7wbpK0PKCrvQGJyctht7qw8ug4c-wBHPi7aQlB21REuafRkVkNEK5-MekesChibYmBN0BJocA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe088cec1b.mp4?token=Qv9O5OPiR7w6kHLXqN2vsfsj6PwGN5zdx0U9pkgKHt2jERCSdo12qrIpMfTvtugZDwWVDnSAuN3bIul-94rTptiKrVnDERIlZs02H7KXmnu_nBiZ2SFLp6a8ExnWF19r3nwiJvYroBfn5ALEXk2f50EE5sQUQ4AfTl3NxRLJUWtyV11_pCjeWdHoR4VOmobVwD0OGjbb0TxHBkZqJkEGRiCYC5IS8FfX2e1WFAa57HG88G1l3SX-bHVDktW7f0JeSj3pR5PD2s_2P7wbpK0PKCrvQGJyctht7qw8ug4c-wBHPi7aQlB21REuafRkVkNEK5-MekesChibYmBN0BJocA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دیدار وزیر کشور پاکستان با پزشکیان
@Faesna
-
Link</div>
<div class="tg-footer">👁️ 666 · <a href="https://t.me/farsna/436907" target="_blank">📅 21:02 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436906">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🎥
مهاجم تیم ملی: انگیزه صعود داریم و آقای قلعه‌نویی می‌گوید باید ۲ مرحله صعود کنیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 969 · <a href="https://t.me/farsna/436906" target="_blank">📅 20:59 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436905">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ajUIj7zrob6A-XrVmSEKdzdnGoVlQkI426qHhlT_cQzAsTfi_SOG1S2slmY9-ChpIN3OBRs1gPjfB41xweBP_mWMPQ0G4Rd0O28gxe0E12KGjw9G_9O_CkCfv8Bn9m_PrqnXwNnR2A_Fg6A1P9Qsn9b0PjLlmtuxWMZRzAHqnZiuiQgNUUXmzABleApKhYTzSdW4pnCPk066oPfnu8cEmRzUM3gIXDduO5y0BW-BJCsaxDEXeGyc5FUxCrfWcgmZAmfXHEP-At0IHNpE8v56CoQbkhFH3D8cYZX7hogYqJdiidYH8Wo25Uk0kWcedg7mozbmvAwA7ZYR9YoH4kiABw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افشای گستردۀ اطلاعات ‌فوق‌محرمانه دولت آمریکا
🔹
پژوهشگران امنیت سایبری از افشای گسترده اطلاعات محرمانه دولت آمریکا خبر داده‌اند؛ رخدادی که برخی آن را یکی از بدترین نشت‌های اطلاعاتی تاریخ دولت آمریکا توصیف کرده‌اند.
🔹
ماجرا از زمانی آغاز شد که «گیوم والدون» پژوهشگر امنیتی، متوجه یک مخزن عمومی در گیت‌هاب با نام «پرایوت-سیسا» شد؛ مخزنی که به‌صورت عمومی در دسترس بود و حاوی اطلاعات فوق‌العاده حساس مربوط به آژانس امنیت سایبری و امنیت زیرساخت آمریکا بود. این مخزن توسط پیمانکار دولتی «نایت‌وینگ» مدیریت می‌شد.
🔹
در میان فایل‌های افشاشده، کلیدهای مدیریتی سرویس ابری «ای‌دبلیو‌اس گاوکلاود»، توکن‌های دسترسی، نام‌های کاربری و رمزعبورهای داخلی، کلیدهای SSH و حتی فایل‌هایی حاوی اطلاعات ورود کارکنان دیده می‌شد. همچنین اطلاعات مربوط به سامانه‌های داخلی توسعه نرم‌افزار و زیرساخت‌های امنیتی دولت آمریکا نیز داخل این مخزن قرار داشت.
🔹
«والدون» در نامه‌ای اعلام کرد ابتدا تصور می‌کرد این داده‌ها جعلی هستند، چون حجم و حساسیت اطلاعات افشاشده غیرقابل‌باور به نظر می‌رسید. او این اتفاق را «بدترین نشت اطلاعاتی دوران کاری خود» توصیف کرد و گفت این مخزن حتی جزئیات نحوه ساخت و استقرار نرم‌افزارهای داخلی دولت آمریکا را هم آشکار می‌کرد.
🔹
پس از اطلاع‌رسانی پژوهشگران، مخزن گیت‌هاب قفل و از دسترس خارج شد و شرکت «نایت‌وینگ» نیز از اظهار نظر مستقیم خودداری کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/farsna/436905" target="_blank">📅 20:54 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436904">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41d3788cc5.mp4?token=iATidZOiHStD4H4dNIaCtVaJ9UDtFN3tDEGpEpvFdudDQKRKvkMrIALPDWCvOrmMbIIAFIb1FCgd1mMyrBkplXt7-PQ-nUTQsfOfx9_4whiSspRx0tzbsy3sT18PR0Yc0FEZWtLesc--u0c2sfi7IXcHMzE9QmWcQMecWEutpJLDeE1QkFGAl692c7YCfcXpHM1-DYtpUvO61wOZO9WDbCcF1L0cAqvcgptXTDPUFLvf45WW0aae1K4K9xsDSvl2pHiRelobsLTSN4US0q6q6Yyr0bKL1TT6QgWtPUVaeAwQGTYyihTit_4jGFfCsx2MCKh0VJK7VWLxFuU0Hxs0ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41d3788cc5.mp4?token=iATidZOiHStD4H4dNIaCtVaJ9UDtFN3tDEGpEpvFdudDQKRKvkMrIALPDWCvOrmMbIIAFIb1FCgd1mMyrBkplXt7-PQ-nUTQsfOfx9_4whiSspRx0tzbsy3sT18PR0Yc0FEZWtLesc--u0c2sfi7IXcHMzE9QmWcQMecWEutpJLDeE1QkFGAl692c7YCfcXpHM1-DYtpUvO61wOZO9WDbCcF1L0cAqvcgptXTDPUFLvf45WW0aae1K4K9xsDSvl2pHiRelobsLTSN4US0q6q6Yyr0bKL1TT6QgWtPUVaeAwQGTYyihTit_4jGFfCsx2MCKh0VJK7VWLxFuU0Hxs0ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای بنر رئیسی مرسی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/farsna/436904" target="_blank">📅 20:48 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436903">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/258c32847c.mp4?token=rywiLfBC86-CuJtZeNVAoLZ6Rh9WIf7EtKVSev5QeCt1YBWCrLqzh9REq26F9_UhrDE5w79um2pQDpjIkiqGJuR29tbOoni7jKzwREiMB5ovylsJQb63FqNxE8tYY6NO5fKTs8m0jnAYmNlyXN2Je_YaMNbEYfDp4FiP05nk84tE4edq4rKnvx2rQ6aROC2j-bhc2KGCV3XUmO1vGJ1iNNQ-RI4ulZ3gtf7duDGQNbOAHIQNhIw7QzQ2YTMgbDdjgajS_JuGs6eNIikmeL0JBEpi82uZA0Bo7kBPm6vl5xpPck0YZNv1Tkkrn2CAKMWOrjhc7eeTrO7yBhfpcTQLFoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/258c32847c.mp4?token=rywiLfBC86-CuJtZeNVAoLZ6Rh9WIf7EtKVSev5QeCt1YBWCrLqzh9REq26F9_UhrDE5w79um2pQDpjIkiqGJuR29tbOoni7jKzwREiMB5ovylsJQb63FqNxE8tYY6NO5fKTs8m0jnAYmNlyXN2Je_YaMNbEYfDp4FiP05nk84tE4edq4rKnvx2rQ6aROC2j-bhc2KGCV3XUmO1vGJ1iNNQ-RI4ulZ3gtf7duDGQNbOAHIQNhIw7QzQ2YTMgbDdjgajS_JuGs6eNIikmeL0JBEpi82uZA0Bo7kBPm6vl5xpPck0YZNv1Tkkrn2CAKMWOrjhc7eeTrO7yBhfpcTQLFoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دلتنگی پسر برای پدر پهپادسوار آسمانی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/farsna/436903" target="_blank">📅 20:37 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436901">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‌ سخنگوی وزارت خارجه: نسبت به موضوع حاکمیت ایران بر تنگه هرمز تاکید داریم
🔹
قاعدتا هزینه تامین امنیت دریانوردی تنگه هرمز نیز باید پرداخت شود.
🔹
طبق حقوق بین‌الملل مجاز هستیم که تنگه هرمز را برای کشورهایی که آن‌ها را برای خود تهدید می‌دانیم باز نکنیم. @Farsna</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/farsna/436901" target="_blank">📅 20:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436900">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">حنظله: در صورت خطای دشمنان به شبکه‌های دیجیتال و انرژی آنها حمله می‌کنیم
🔹
گروه هکری حنظله: در صورت ارتکاب هرگونه تجاوز یا بی‌مبالاتی از سوی آمریکا و رژیم صهیونیستی، حملات سایبری ویرانگر فراملیتی علیه زیرساخت‌های انرژی و دیجیتال کشورهای خصم اجرا خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/farsna/436900" target="_blank">📅 20:24 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436899">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‌ بقائی: ما با سوءظن و حسن‌نیت به تبادل پیام می‌پردازیم
🔹
صحبت‌کردن از اولتیماتوم و ضرب‌الاجل دربارۀ ایران مضحک است. @Farsna</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/farsna/436899" target="_blank">📅 20:23 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436898">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4420d08a0c.mp4?token=E4pm8s32csuYzXGom1y64kbDmaJVxovKLvKWnELz0Yi_WOe5hfilka8QDA9vaiqpBo2NNYKP4-eincoDv4zTCUp0N2468-LW-QX9pPh4vsM_ep_eSrH28lrFmtcL7P-fd-FL9BHdF2h2p34UauruW5Kf4nx7Ls9-2v7G8nqIOpUl8RKNyXNcHA8YeoMK8ttk1GMONlZKY03ilWh2_avp99lstkEu7ZSTfhyX8_jyageMrNCITkPCz89wITUH7kDKWm8hd6YsS1whlvZXZ0_1IbHcw1LlyjqhBMczLA-Qqfn1QMVp-52RjI6OW--9rassbEd8MARY4ZAg-EH319mamA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4420d08a0c.mp4?token=E4pm8s32csuYzXGom1y64kbDmaJVxovKLvKWnELz0Yi_WOe5hfilka8QDA9vaiqpBo2NNYKP4-eincoDv4zTCUp0N2468-LW-QX9pPh4vsM_ep_eSrH28lrFmtcL7P-fd-FL9BHdF2h2p34UauruW5Kf4nx7Ls9-2v7G8nqIOpUl8RKNyXNcHA8YeoMK8ttk1GMONlZKY03ilWh2_avp99lstkEu7ZSTfhyX8_jyageMrNCITkPCz89wITUH7kDKWm8hd6YsS1whlvZXZ0_1IbHcw1LlyjqhBMczLA-Qqfn1QMVp-52RjI6OW--9rassbEd8MARY4ZAg-EH319mamA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شما اسم فرزند آینده‌تون که قراره به ایران جان تازه بده چی می‌ذارید؟
🔹
خیلی‌ها توی پویش «جان ایران» شرکت کردند از جوان‌هایی که ذوق فرزنددارشدن دارن تا پدر و مادرهایی که اسم بچه آینده‌شون رو انتخاب کردن.
🔹
شما هم می‌تونید نام فرزند عزیزتون که قراره به ایران جان بده رو به شماره ۳۰۰۰۱۴۱۳ پیامک کنید.
@Farsna</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/farsna/436898" target="_blank">📅 20:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436897">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tW24Ibmqt29DtvFHtZtLVYJ1hwS97mYt7TJ0jpeSHM6fFpT-rd-uPUPjSVh6pdlU7aTS9N_mpC39GbNj4FIaL3ucUueG4uBTO09QEiKwwY2Y3GMGva7oSSsSfkWfGu_rJ96CZOT2nFXNxn_1lDd4p1cFn_7yAIZOir5OPHltuiCuCX-0xaTaEktIw0btiFVHpaPY8tFEE4BvT-2cKmh-JtUsuDqJOld2CtnsZuJwk6vZmIb3ZKMDaiPXqGKuCXT3CcuPCmHUzysEdnFbrToZec7CXPrk7y2wpqz5rsUWjhjoeVZ9FmA7e7fAqZsUWvhqdAnZRDrFsG8Ydq-zOqcaMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با هفته جمعیت، پویش ملی «جان ایران» با رونمایی از بیلبوردهای شهری، پیام تازه‌ای از امید و آینده را به تصویر کشید
🔹
کمپینی که هر تولد را نه فقط آغاز یک زندگی، بلکه ادامه تپشِ ایران می‌داند.
@Farsna</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/farsna/436897" target="_blank">📅 20:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436896">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_RnPYD13nVT7hy5Uzm1LS3htkshiO19xlM2UpBk-yjarrI-bWJCG_VnT7hvP9KKe4XBA6pE-2uZ9DUy7LRGywY00Vv3IO0l0T0PamcnLv0N3jDCPbq70_IObeEM6rNYolSYPXObai3yRioBybYU9NTHB4SURWrNXKXVTSI5lLR2Xd476T1Dp4tsWbGyNJVibaZb-Xh_iaWxHAfF-ACr2br29uf_l9w6-94T7AUdXA2x6Zcx4LI_PZ6GxsnCU7xfyiIpnq75ENc1Gh3kHNOeLDpnFAMo4NzPCnal7zxhFHhsMjatkJXS1xBSGHp95ERb_tTPd22Tat_yz648zQgWnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با سالروز شهادت شهید سید ابراهیم رئیسی طرحی از شهدای پرواز اردیبهشت در کنار رهبرشهید انقلاب برروی دیوارنگاره میدان انقلاب تهران اکران شد.
@Farsna</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/farsna/436896" target="_blank">📅 20:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436895">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZhNJv8jTlRyHSHVn5h6xXDjIdXc5dpl-prwu7Gv-kgo9i-p21dYUanOTarFMaD2Qs-pxNCXo0EalvfNVC-jfmV6MowWOom_p9qwJdJCMQ9aqwHmyFWJizdudCVXOgnlZIg2ahX7h6WCx5fu0AErnsl0ve74ZmQYu4WzlytHfBOQJD0pMeon21eLi_l1x5xctyMsZR2KZw82p0zAB4Q1GXufCoL-rHQvz1ZD_3EaOV8HSxjtJSB6TcYVlgEad36ARme0yOAs0icvsCrRZ7gchPVEr-Mp-6sWzQ0HPsmzI96D4fdU_kijB4dynS0K9UJBbaP-ENEAfG41O1SvGZB-9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">*
🌐
ثبت‌نام خودروهای وارداتی با حساب وکالتی بانک رفاه کارگران*
🔹️
مشتریان بانک رفاه کارگران می‌توانند به صورت غیرحضوری و یا از طریق مراجعه به شعب این بانک، نسبت به وکالتی کردن حساب‌های خود اقدام و در طرح فروش خودروهای وارداتی شرکت مگفا شرکت کنند.
🔹️
مشتریان متقاضی خرید محصولات این شرکت تا پایان روز پنج‌شنبه 31 اردیبهشت ماه سال جاری فرصت دارند با مراجعه به سامانه محور (
https://mehvar.rb24.ir
) یا مراجعه حضوری به شعب این بانک در سراسر کشور (با رعایت حداقل مانده حساب ۵ میلیارد ریال)، نسبت به وکالتی کردن حساب‌های خود اقدام و در این طرح شرکت کنند.
🔹️
استفاده از سامانه‌های فرا رفاه و رفاه‌پلاس موبایل بانک رفاه و سایت بانک رفاه کارگران، دیگر روش‌های غیرحضوری است که مشتریان این بانک می‌توانند از طریق آنها نسبت به وکالتی کردن حساب‌های خود و شرکت در این طرح اقدام کنند.
@bankrefahkargaran
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/farsna/436895" target="_blank">📅 20:17 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436894">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/farsna/436894" target="_blank">📅 20:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436893">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه: تبادل پیام‌ها بین طرف ایرانی و آمریکایی براساس متن ۱۴بندی ایران ادامه دارد.
🔹
حضور وزیر کشور پاکستان برای تسهیل مبادلۀ پیام‌هاست. @Farsna</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/farsna/436893" target="_blank">📅 20:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436892">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه: تبادل پیام‌ها بین طرف ایرانی و آمریکایی براساس متن ۱۴بندی ایران ادامه دارد.
🔹
حضور وزیر کشور پاکستان برای تسهیل مبادلۀ پیام‌هاست.
@Farsna</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/farsna/436892" target="_blank">📅 20:13 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436891">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4893f2908.mp4?token=SJJZ2SiPnrrE42pl3OM_nDTy6JdjxFslldklbPqgL8eo9V-G6tiAl0UxDJbxpPiBAoQPc7u3OCzaX3KqgyC4cYW6A_8GePeDuzIP9mOe-XWVj_TMvVMh6WVj4cRnyhBAhAKlve7HW-JL-lrd8CB6yi9V0t3Sf4cLjE64fzbFV8bBBdBMfmvHxpQhALnHmD4wK2ZZbxxp0XkEAgebNvli9kVt6sRRQXtOYGisw24bfiotE8tm9v92i4yrwR2nlt6LLHvcriqm4qR4BckWT8d09j8P20iAgngtUk7OdLfV8a-ztN0slNyc2PHv6TWk35IzqSE27C8TIOA7QapxFGCuWT07LCFze4-T2LxSK9YarKtrcwTvwLkvmlwg51jIqA7VAynzziZO8GGCDHy-vA265iExv3cI7PdRSfl9dl1fs0YtwNfBp_6IpfmRmzbAPVdCW9pRcyl9KDwKtt3zlXO5ITyAYBSOgMmVVfBADuQgz8ssXoilviiERzslXOZjjQGNcH33GidyJsdQ6YLtKaFy32ZeJIAQsaN0G3QeWvuoiGeOARtMmdc6J_mnN9gRyvSSxNTwM2NdlBW7qqP5AHiHjbIy-4EiW48fnPFhKxIvKUqFARdAZY-9bFLzo10smPWjhTvdAeSuRswhgM0W4dL9mfDWaSN91_ts7y0mwMLiYFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4893f2908.mp4?token=SJJZ2SiPnrrE42pl3OM_nDTy6JdjxFslldklbPqgL8eo9V-G6tiAl0UxDJbxpPiBAoQPc7u3OCzaX3KqgyC4cYW6A_8GePeDuzIP9mOe-XWVj_TMvVMh6WVj4cRnyhBAhAKlve7HW-JL-lrd8CB6yi9V0t3Sf4cLjE64fzbFV8bBBdBMfmvHxpQhALnHmD4wK2ZZbxxp0XkEAgebNvli9kVt6sRRQXtOYGisw24bfiotE8tm9v92i4yrwR2nlt6LLHvcriqm4qR4BckWT8d09j8P20iAgngtUk7OdLfV8a-ztN0slNyc2PHv6TWk35IzqSE27C8TIOA7QapxFGCuWT07LCFze4-T2LxSK9YarKtrcwTvwLkvmlwg51jIqA7VAynzziZO8GGCDHy-vA265iExv3cI7PdRSfl9dl1fs0YtwNfBp_6IpfmRmzbAPVdCW9pRcyl9KDwKtt3zlXO5ITyAYBSOgMmVVfBADuQgz8ssXoilviiERzslXOZjjQGNcH33GidyJsdQ6YLtKaFy32ZeJIAQsaN0G3QeWvuoiGeOARtMmdc6J_mnN9gRyvSSxNTwM2NdlBW7qqP5AHiHjbIy-4EiW48fnPFhKxIvKUqFARdAZY-9bFLzo10smPWjhTvdAeSuRswhgM0W4dL9mfDWaSN91_ts7y0mwMLiYFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خیابان مگر جای ازدواج است؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/farsna/436891" target="_blank">📅 19:58 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436890">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">‌
🔴
حزب‌الله: یک تانک مرکاوا در شهر الطیبه را با یک حملهٔ انتحاری هدف قرار دادیم.  @Farsna</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/farsna/436890" target="_blank">📅 19:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436889">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c04c242af4.mp4?token=GJXSBQh_lAoFsafSoXEDuxfdb7x531jlUluKP18_fuPiVDQ4Foc49zUNKVU0QbMN86cn_sCJ7TCQNOvme-Kz3dv5ntdGvMyAa5rKgKzdys-Ds-ThH-yZNv3vO1pdAT5QKb2N5HBiJkdfyk0LBykiripvyD0wDm91bDwAQ0hC9eyk99Nqr95BGWuyLh9LJIyAz-WW4Y5Xi3ySX5MQf-nFspet_eFCOaENDxpSSm9kyiGxj1E9C8qnuF6OayWIgyDzEFSL11tejJBQJY2XpQbgeg8EBE3xDGlW6W4wnd8u8qXK7cJMIrauC27SIZATO2S2PdBo-04011fpBt5anstmgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c04c242af4.mp4?token=GJXSBQh_lAoFsafSoXEDuxfdb7x531jlUluKP18_fuPiVDQ4Foc49zUNKVU0QbMN86cn_sCJ7TCQNOvme-Kz3dv5ntdGvMyAa5rKgKzdys-Ds-ThH-yZNv3vO1pdAT5QKb2N5HBiJkdfyk0LBykiripvyD0wDm91bDwAQ0hC9eyk99Nqr95BGWuyLh9LJIyAz-WW4Y5Xi3ySX5MQf-nFspet_eFCOaENDxpSSm9kyiGxj1E9C8qnuF6OayWIgyDzEFSL11tejJBQJY2XpQbgeg8EBE3xDGlW6W4wnd8u8qXK7cJMIrauC27SIZATO2S2PdBo-04011fpBt5anstmgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زاکانی: شهید رئیسی تا سرحد توان برای خدمت به مردم تلاش می‌کرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/farsna/436889" target="_blank">📅 19:52 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436888">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb30e93732.mp4?token=ahWavFSjIAH7Iaql36oIrL--sjc-aYdx7dbN4CjMtc1tdC-vL_VkyOexXTlGiszXcFYxceVPb_nh75LMPj04LEVpEST_SSKswlFm4x4Mk8mmO0CM06n7sCWKERGa8kwcuhOgEtb2Emxfg3UHUOgTYwlU7f9t2Qqj4IvpYvJe4tYGmIoBC6MFOQCBcWxXNobVncs-b04OrbyGTU-Uvdq-zWN0VvQ4gv4HxaPx_ANr5rvh1ZpIkHU3enKMvAbRdyqkAI9lq0nrm11fP8sPXIeeaXS1yoKWGZLxfOPYPiX0QLr6VlixA0Xdafdi-_0uwnM6SQp4Irlx4C3IkJx87rf2JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb30e93732.mp4?token=ahWavFSjIAH7Iaql36oIrL--sjc-aYdx7dbN4CjMtc1tdC-vL_VkyOexXTlGiszXcFYxceVPb_nh75LMPj04LEVpEST_SSKswlFm4x4Mk8mmO0CM06n7sCWKERGa8kwcuhOgEtb2Emxfg3UHUOgTYwlU7f9t2Qqj4IvpYvJe4tYGmIoBC6MFOQCBcWxXNobVncs-b04OrbyGTU-Uvdq-zWN0VvQ4gv4HxaPx_ANr5rvh1ZpIkHU3enKMvAbRdyqkAI9lq0nrm11fP8sPXIeeaXS1yoKWGZLxfOPYPiX0QLr6VlixA0Xdafdi-_0uwnM6SQp4Irlx4C3IkJx87rf2JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سقوط جنگنده پاکستانی
🔹
یک هواپیمای آموزشی نیروی هوایی پاکستان امروز در جریان یک عملیات آموزشی در ایالت پنجاپ سقوط کرد.
🔹
هر ۲ خلبان قبل از برخورد هواپیما به زمین با موفقیت از هواپیما خارج شدند.
@Farsna</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/farsna/436888" target="_blank">📅 19:49 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436887">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f1cb3975a.mp4?token=p58G8Mcq7QMUkVbeINvqVjYEdCjFQVoEEqv7m0uV0YyfXdt9FZcqzO8QZcKHhjcplSkzSvYEY7a9MHK1MfytTNhPcS1EATSwQd6ql6uppk-c4RE6CybTOgpJ8-Eo7usw6XA2_GE68CU4eMwf66BXqHVfDmMm1S2gbWMh1LX36q6Syw9QFon7uLOV1FQ-mpafyFrMR0v8x14rZT7Lz__8Hpjr9DpcQAYD5qqAabSVf6W70eOoSa5Ge28p51-rAvhIkggvi_WoYXH6DjDlSf6G8HiE313Po599UaQ7Y1OP9nkH0BCIL9Cs4pdahnA1jJTiGhGwfXlZNsesTYBAx4bnzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f1cb3975a.mp4?token=p58G8Mcq7QMUkVbeINvqVjYEdCjFQVoEEqv7m0uV0YyfXdt9FZcqzO8QZcKHhjcplSkzSvYEY7a9MHK1MfytTNhPcS1EATSwQd6ql6uppk-c4RE6CybTOgpJ8-Eo7usw6XA2_GE68CU4eMwf66BXqHVfDmMm1S2gbWMh1LX36q6Syw9QFon7uLOV1FQ-mpafyFrMR0v8x14rZT7Lz__8Hpjr9DpcQAYD5qqAabSVf6W70eOoSa5Ge28p51-rAvhIkggvi_WoYXH6DjDlSf6G8HiE313Po599UaQ7Y1OP9nkH0BCIL9Cs4pdahnA1jJTiGhGwfXlZNsesTYBAx4bnzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گوشه‌هایی از تمرین بدنی ملی‌پوشان
@Sportfars</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/farsna/436887" target="_blank">📅 19:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436886">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">شهادت یک پلیس در سراوانِ سیستان‌وبلوچستان
🔹
پلیس سیستان‌وبلوچستان: ساعتی پیش، سرنشینان مسلح یک دستگاه خودروی سواری به سمت خادمان امنیت در یکی از جاده‌های شهرستان سراوان تیراندازی کردند که متأسفانه ستوان سوم امیرحسین شهرکی به شهادت رسید.
🔹
اشرار مسلح تحت تعقیب پلیس هستند و در منطقه طرح امنیتی-انتظامی درحال اجراست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/farsna/436886" target="_blank">📅 19:35 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436885">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🎥
حملهٔ وزیر امنیت داخلی رژیم صهیونیستی به اعضای دستگیرشدهٔ ناوگان صمود  @Farsna</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/farsna/436885" target="_blank">📅 19:29 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436884">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DcmKEjh1lKxslzyqoIN_cHPrCwOvaq9rpfeRyUSQcQcTYRUQOJbUDpN4sERl-sTZr5IHpce4TcrDKFheW7_8uP5D9Tu-O7szOkmaAeB8yn1e_uBAhH2_903b0bhqv8UsrTcOywK_ytw6TzbCgGDVwal-YZ851aF8v0j56cw5rXgPnBhrHTq3Ibl5KkKQhSpp-DLaH2osIRziE2BwMcJnkW-c9DfzLshEnFgZfZryf8-gncphAi8ntbJUTUrdSTOc5UHxw3KvllcuYPCeRmIi0H7WYhbLZio4zq9FTmnBPYGSDXVy1BPdmexhZlAfeEkpoDD7-wPWQgRvz9LiDp4Mnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خنثی‌سازی بیش از ۸۵۰ مهمات در هرمزگان
🔹
سپاه هرمزگان: طی انجام بیش ۲۵۰ مورد عملیات خنثی‌سازی و انهدام، بیش از ۶۰۰ عدد بمبلت را که در جریان بمباران‌های هوایی جنگنده‌های متخاصم و با هدف آلوده‌سازی برخی مکان‌های حساس و مهم استان به‌صورت مین‌ریزی هوایی و با استفاده از بمب‌های خوشه‌ای در چند نقطه پراکنده شده بود، کشف و خنثی شد.
🔹
همچنین در این عملیات‌ها، انواع موشک‌های کروز از جمله مدل‌های GASSM و تاماهاوک و نیز موشک‌های پرتابی از جنگنده‌ها مانند GBU و BLU که در اثر اصابت به برخی مکان‌های حساس عمل نکرده یا دچار نقص عملکرد و انفجار ناقص شده بودند، شناسایی و خنثی‌سازی شدند.
🔹
در بخش دیگری از این اقدامات، بیش از ۱۲۵ فروند انواع پرنده انتحاری شامل اوربیتر، هاروپ و لوکاس کشف و خنثی شد.
🔹
علاوه بر این، بسیاری از اقلام و تجهیزات الکترونیکی که توسط دشمن برای اهداف مختلف در دریا و خشکی رها شده بود نیز توسط نیروهای متخصص شناسایی و جمع‌آوری شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/farsna/436884" target="_blank">📅 19:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436883">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‌
🔴
وزیر امورخارجهٔ فرانسه از احضار سفیر رژیم صهیونیستی به وزارت امورخارجهٔ این کشور خبر داد.
🔹
بارو با اشاره به رفتار وزیر امنیت رژیم صهیونیست با اعضای کاروان صمود گفت: اقدامات بن‌گویر در قبال سرنشینان کاروان جهانی صمود غیرقابل قبول است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/farsna/436883" target="_blank">📅 19:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436882">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68fb73b61e.mp4?token=argcVmRz6LnUuAtWqI2h0p_F4e_pGUFiSSmWXT4PvroZV5m-qSVlzATKYkfcRUfC5jtVCGji5ktHbSxn0FuKZJSGMnFJSFH8yW-Ah7aMXsrNTcaZdpomvuiZfu4oMLZe94oNYahNE7KnHzQl8GpzCyCGsug9MqKpEljNayWvDWQGeEYikhjR2BQruLHaJj7AufNK0XDLYkGkfvVKsLVT65k4ywZMyUSkzjRML-bHZh_9iVgeLiAv0JdnOZ_C3W6MqsT2YxqQUtm3zM1lBBJhUtde_tmdtBQqli7MCHKfbHmG4IgmyYOy2jbz_qTVD3zji2CtIFwBTrRrcJpIa-a7kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68fb73b61e.mp4?token=argcVmRz6LnUuAtWqI2h0p_F4e_pGUFiSSmWXT4PvroZV5m-qSVlzATKYkfcRUfC5jtVCGji5ktHbSxn0FuKZJSGMnFJSFH8yW-Ah7aMXsrNTcaZdpomvuiZfu4oMLZe94oNYahNE7KnHzQl8GpzCyCGsug9MqKpEljNayWvDWQGeEYikhjR2BQruLHaJj7AufNK0XDLYkGkfvVKsLVT65k4ywZMyUSkzjRML-bHZh_9iVgeLiAv0JdnOZ_C3W6MqsT2YxqQUtm3zM1lBBJhUtde_tmdtBQqli7MCHKfbHmG4IgmyYOy2jbz_qTVD3zji2CtIFwBTrRrcJpIa-a7kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ به‌دنبال نخست‌وزیری در اسرائیل
🔹
رئیس‌جمهور آمریکا: من الان ۹۹٪ در اسرائیل محبوبیت دارم؛ پس شاید بعد از انجام این کار، به اسرائیل رفته و برای نخست‌وزیری نامزد شوم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/farsna/436882" target="_blank">📅 19:08 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436881">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XpLHFS4ZisjfSPS-ufLAFgQRf6N8AtjjayBckt6TAiRUJiiS84DazXeRcATUXKrDF-5R_Yfv-gHHmjTHHP0EXbNZN4FzgA687dIWsvgsBGj0_rGd49D81F3n-wrbHa11nmvLDZuygBPcXP8BsQu6g7bJRrQySUF5pnZRNK5nB47n0jBA1D5jV0SkHByIzwsaqP6RAX9gsYbHpAxtP1i6gzaztM4BxHDnpm4lGuLHbrsmSeeQI3hPk38-6QwcIDui4WPAYvy3myNHUjhA5lrnGSVbZkm47ZtldxGRunut6hi1UIaWBgAgiz7jl4_qQz5g3sEhl3_wPzkhhzaw5Fc7xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مادر فولاد کشور به یک بانک دولتی فروخته شد
🔹
رئیس هیئت‌مدیرۀ انجمن تولیدکنندگان فولاد: با تصمیم وزارت کار، ذوب‌آهن اصفهان به بانک رفاه واگذار شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/farsna/436881" target="_blank">📅 18:52 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436880">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mKbC6ekJfvDPwzGdnLaim4OfWPvfyWH3InSY6hO_SCLab8whtJtMGmc2sT1g7-Vc4IcuGdsRyeXdJVLRl3SMqMqINIhgRRYD60tEJggiCoG6TIPM2HcVCz5Fs8b-kQAfGZafUYme4CYmUvIz2wPWvWGVs9fxZxWW4jkmBNRLOyBsaktLwgC29TqtlYYFWm-TpNIHXujlpaFp2_EUuESEHuO5WoStBvE4fgGja8YQC92Kdo0buJV-u2HxXMkPih-PlvIE7rrhiZUS7KAp7q5dv7SdnpZqEEaAtuInvxpfehBfLH4p7dDmZ7F2gwB0l5G7Ij8OAU2ikf8OrdGjb-D0ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آغاز فروش بلیط قطار اردبیل-مشهد از امروز
🔹
استاندار اردبیل: با آماده‌سازی ایستگاه‌ها و انجام اقدامات نهایی، راه‌آهن اردبیل در اختیار مردم قرار گرفت و بلیط‌فروشی اولین سفر ریلی به مشهد از امروز آغاز شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/farsna/436880" target="_blank">📅 18:46 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436879">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‌  ایتالیا سفیر اسرائیل را احضار کرد
🔹
ایتالیا در واکنش به توقیف ناوگان جهانی صمود و آنچه «برخورد غیرقابل‌قبول» اسرائیل با فعالان صلح‌طلب خواند، سفیر این رژیم را برای ارائهٔ توضیحات رسمی احضار کرد. @Farsna - Link</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/farsna/436879" target="_blank">📅 18:39 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436878">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNJLGUl8q03yzy4RN4Aim1vriHlNXLvsJg0QxrYTrW6hi3EMVJH7ptC3wl9nQGnWmCI2McTWrGCMjzKLoTs0lkXzh9XfHHFRTQ54bGXEEzHgTFmIZkevJ8mlAaDKw7j5S0810gOe4LC7ETU5TyVSlBMc9ApwI9YaZmkUUIL81A1z9X5CcSj5_MuKW3ZOF0ED7VBK4PbnNaaLhKb8ASuQo5Eu0Es8hWUn1q2j2Xo_0Th5EmLgrFj3ZL1LT5rjxCufU2eKvfz5yoKLgtnfg8aOCRcFSBscSn5obd4SW7xJHkOO5PGk5HlrNu7wtLgVYKrCV_2dF0Y7mwk17SK_NOQk3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت بنزین در آمریکا باز رکورد زد
🔹
به گزارش انجمن خودروی آمریکا، میانگین قیمت بنزین در ۷ ایالت آمریکا از مرز ۵ دلار برای هر گالن عبور کرده است؛ موضوعی که نشان‌دهندهٔ تداوم فشارهای تورمی و افزایش هزینه‌های انرژی در ایالات متحده است.
🔹
انجمن خودرو آمریکا ۲ روز پیش اعلام‌کرده بود میانگین قیمت بنزین در ایالات متحده به ۴.۵۵ دلار به ازای هر گالن رسیده است و در برخی ایالت‌ها این رقم از ۶ دلار هم فراتر رفته است.
🔹
بر اساس داده‌های منتشر شده، کالیفرنیا با ۶.۱۶ دلار، واشنگتن با ۵.۷۰ دلار و اورگن با ۵.۳۰ دلار گران‌ترین ایالت‌های آمریکا هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/farsna/436878" target="_blank">📅 18:29 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436877">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ct4QISMywCn7bss64deXpwpmCJAwbvB4HMj-xyOccLjQ99FFfzWtZmowadpb1GOfpmVor99M-7x2DRCpkJrozTcBApfG7kPUQ0P3fYkQBi8WldgxtkwJ-kTuco1e4cHNs-QSGcATOYfokqaWFEKV2LgaLIyfDsELLM_WpibHMtd11MnjTmCU7ql399F6VhUfbtnrPOUcgGjfs75HYFrwMlV4fQyY_eqlLvStSsSYUFNHOYmKxAqtOiVPAzvm6rFxIfvONJYCS-1W4oydW-gBE0eVfXjwEwojyD7OiqKPhGLq_NZ1IH7ImJ4mKkLUNlQkT3BG2__l62QIp4cwNE6dzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منابع عبری: فرمانده اسرائیلی در حملۀ حزب‌الله به‌شدت مجروح شده است
🔹
مایر بیدرمن، فرماندهٔ تیپ زرهی ۴۰۱، در جریان انفجار یک پهپاد انتحاری در لبنان به شدت زخمی شده است. یک افسر نیز به‌طور متوسط زخمی شده است.
@Farsna</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/farsna/436877" target="_blank">📅 18:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436876">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SyNV5AX170R3Mv3gCAUUnTy_bQGBU5G3-kBvui2uSky_wJ8mJWucaUOyNjtvo1-oA4KzOEVOcbPlkbFkDYwuSkgsaRbB0RdhkrGTLHAzNcFufPQ7csCUXtgpN206nbpIxNSD_7vKWpiSj9TAir1FkLE1LOcjEZbxxCPwGmBH3DqoFyqO5rCM11J_oK2kJMmAyqBAkBDTLdXnNWHEaLlZxeMQvPiJFZ_1P4cECnHim4TsOI2SC6VcPUyhiDrQfy5ve3fnXUACcVD-wPCbMqiMjdVPwy7teyf0V1GFvrUV3NvbGXx0oOOSl7BtJWZ7d40ENC9qfmFlvU_1U-So0CIETg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترامپ بازهم عقب‌نشینی کرد
🔹
ترامپ: حمله نظامی به ایران که برای فردا برنامه‌ریزی شده بود را به درخواست ولی‌عهد عربستان سعودی، رئیس امارات و امیر قطر متوقف کردم. @Farsna</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/farsna/436876" target="_blank">📅 18:04 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436875">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">خط-41.pdf</div>
  <div class="tg-doc-extra">3.3 MB</div>
</div>
<a href="https://t.me/farsna/436875" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📎
دستِ پُر به میدان بروید
🔹
اگر برای اجتماعات انقلابی به‌دنبال شعر، شعار یا تک‌بیت‌های روز هستید، ویژه‌نامهٔ «خط» پاسخگوی نیاز شماست.
@Farsna</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/farsna/436875" target="_blank">📅 18:02 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436874">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d045ee94bb.mp4?token=g4KrLwVnIqDmjxSr3IhYPklIXcgj8mPcIQ8wSDUt8_lDRj3tLJbgkui95q7Em52lc83XiWIKgMzVVrregLKD50onnnbLPU90Keu6dGmkFVfdehdiK4-yVF8IuKqvKY6m2Ucbx7bBQE4erkHYGU5oIbSjRw17kdITnCecp1QOMX4kl79oMPtmYlSqKt_ONbV2_HCtqIyS1fHDgKY87g5sl5OmwL5y_T3MXaJa9peVnc6cuilzwxhBhCeqa8MvarK5s5aoXDRUfnf1LuncAC_dBdlnu198L_mZYpWTtXQtG_M4umQRZ6TxWUzP0kyZd3-dYjKeRopeObLlFctrgIUpt6tk0Wg-1ai4P8YlC1Dy1BEqR7lk7vehYsHjzjj87Jhz5bqHeURk4f2_0_bzHOdY1iytjekvXHvA_1TEHmNNa5yH0s6uhzvdImu01IokydkjeQL-GLVVqFROLuP2jxnNtdOlnwcN2WKTrUXPDknBFFxhvUcOUsU5hUke5J5gcSZAB8lgfOjARwNTeI-7xeZdaStdymQrHSvQjVJNeE98Tv1oWXQedEnOuejmXYqmdymBhtztFxefPnj9yrH6P-eudJvYNVin43EFVDpPcu-bfqJ4Nnn6eyHHm7lCbkH1ef6jVzNGFPFLfUPbCElnMTKSgzrMqjRYkjk2j-ImwLsvHj0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d045ee94bb.mp4?token=g4KrLwVnIqDmjxSr3IhYPklIXcgj8mPcIQ8wSDUt8_lDRj3tLJbgkui95q7Em52lc83XiWIKgMzVVrregLKD50onnnbLPU90Keu6dGmkFVfdehdiK4-yVF8IuKqvKY6m2Ucbx7bBQE4erkHYGU5oIbSjRw17kdITnCecp1QOMX4kl79oMPtmYlSqKt_ONbV2_HCtqIyS1fHDgKY87g5sl5OmwL5y_T3MXaJa9peVnc6cuilzwxhBhCeqa8MvarK5s5aoXDRUfnf1LuncAC_dBdlnu198L_mZYpWTtXQtG_M4umQRZ6TxWUzP0kyZd3-dYjKeRopeObLlFctrgIUpt6tk0Wg-1ai4P8YlC1Dy1BEqR7lk7vehYsHjzjj87Jhz5bqHeURk4f2_0_bzHOdY1iytjekvXHvA_1TEHmNNa5yH0s6uhzvdImu01IokydkjeQL-GLVVqFROLuP2jxnNtdOlnwcN2WKTrUXPDknBFFxhvUcOUsU5hUke5J5gcSZAB8lgfOjARwNTeI-7xeZdaStdymQrHSvQjVJNeE98Tv1oWXQedEnOuejmXYqmdymBhtztFxefPnj9yrH6P-eudJvYNVin43EFVDpPcu-bfqJ4Nnn6eyHHm7lCbkH1ef6jVzNGFPFLfUPbCElnMTKSgzrMqjRYkjk2j-ImwLsvHj0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جان مرشایمر: تنها راه پایان جنگ، توافق است اما ترامپ حاضر نیست تن به پذیرش پیروزی ایران بدهد
.
@Farsna</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/farsna/436874" target="_blank">📅 17:59 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436871">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RQ4o1sUvFIxWlBIe9Zl866IcmWEBeRKgtBaTbYwDEFFf-zeZAWQsu38ezMC6UL6ELthVpIX9npJsO9PX2-3Qi59Sgv-lWVOukJJ4npP1y8GPcf8z3Ro0bryqE81GhnLAr5JcbyrWFWHakTbMAhh8B_NR-tcFd3YQApSqLWSDKhzlKMfS25bWW6JlZTClMItoQjiLUyoKwicvAqYWlUfVyv7SlGzX4BMH9ygi-iA11Dx6VzMN-XzzGgzZTrrqUdwaD5i6thlnAoB0T0aVqp0R9oU8SnC8bE3t3j1RVUS2u-OMegqfLGqlzRsgNIfAePB_F5RYk9-1b5f2VvGFA2yuVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه: راه شهید رئیسی، چراغِ خدمت در میدان نبرد پیچیدۀ امروز است
🔹
بیانیه سپاه پاسداران در گرامیداشت دومین سالروز شهادت رئیس‌جمهور شهید: آیت الله رئیسی نمونه کامل «عالم عامل» و «مدیر متعهدی» بود که مدیریت را امانتی الهی و مسئولیت را پلی برای خدمت می‌دانست؛ او در اوج مسئولیت، ساده‌زیست، متواضع و در میان مردم نفس می‌کشید.
🔹
امروز که دشمنان انقلاب با تمام توان در میدان نبرد نامتقارن و جنگ شناختی علیه ملت ایران صف‌آرایی کرده‌اند، بازخوانی سیره شهید رئیسی - که تصمیماتش را بر پایه تکلیف، عقلانیت، صداقت و توکل اتخاذ می‌کرد - یک ضرورت راهبردی به ویژه برای کارگزاران و مدیران کشور است.
🔹
خادم الرضا شهید رئیسی، در سخت‌ترین شرایط با مجاهدت‌های صادقانه و بی‌منت در متن مردم، امید را در جان جامعه زنده نگه می داشت و در نگاهش پیشرفت نه یک شعار که مسیری روشن برای عزت ملی و شکوفه‌هایی استعدادهای این سرزمین بود، او با برافراشته نگه داشتن پرچم مسئولیت پذیری، باور به راهبرد "ما می‌توانیم"، را سرمایه گران بهای کشور برای استمرار حرکت انقلاب و پیش برندگی توقف ناپذیر "ایران قوی" به سمت آرمان‌های تمدن ساز و ناکام سازی راهبردها و سیاست‌های اهریمنی و ضد ایرانی دشمنان علیه این سرزمین قرار داد.
@Farsna</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/farsna/436871" target="_blank">📅 17:52 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436870">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QiSFL2t-xaUAe3IidXCgVKD8GG3LPjIOV5bD0mDoVEtsNLqXX8USWGZjiWs9I6FJIQjCCx5GPDZZeEoBQQc-1xV3Ws0QKfhkoAGOiDpXp5JEMlH-tHEpFqlmfTuRcU87AJARh2yk55FvAR48RXuYTx3HDYbM9lL0s9_ydGKHDfOtGomwiSx6Wg5naUEM7i6jty1mIlooMbE70_FfqdS8Z8KMScQYTHrSYxOBSjBs1vK-e9tljflHpbA4a0-fAI8SOEn_YmPLYglwIuSahpTcV3uAOdHj-Dhvz-21rzg76aKjopAscQbw7iQ9WR3WZWpncdmbnH6GNUAQS6s1lDEgbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار انجمن اسقاط درباره تخلف در شماره‌گذاری خودروهای نو
🔹
نایب‌رئیس انجمن صنفی مراکز اسقاط خودروهای فرسوده: طبق قانون مقرر شده است در ازای از رده خارج‌شدن یک خودروی فرسوده، ۴ خودروی جدید شماره‌گذاری شود.
🔹
شواهد نشان می‌دهد درحال‌حاضر این عدد به ۱۲ خودرو افزایش یافته که مصداق بارز تخلف از قانون‌گذار است.
🔹
علت اصلی این کاهش، با وجود قوانین به‌روز، نداشتن یک آئین‌نامه مصرح و صحیح است که موجب شده سیاست‌گذاری‌ها در این حوزه به درستی اجرا نشود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/farsna/436870" target="_blank">📅 17:45 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436869">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38474ee2e6.mp4?token=UE9PfvPTO4X6b_R93Kpita3YG9Fc7TduOr9XFlFiUvEQXru_nU26FERjj7AER8KF3oA35dGXWM6U1FheuX4c0YvI-bqS3KrjP-HPwNqiXrbNscgzqpUjE_CDpN6XpCVlKxggSPpja9iWyJ31_o3pKj-oPKs6TdeD7VWkT6R_GKowpU2JQcPpo8YlahDFREYeCtrqHntAgdAM9QdLhRhlv3QFUlYdkUj_9LUOsZ4TGF18W-GXo2KfImWULmD3Y4i7AuoQNDObhJ_Tf3rA5_x_c0gZ3x8s4V28y-OFMPrXBNd0YVHEQyQ3EEG291RZLZ4ApH8emEzTBT4q9yzZ-HfarA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38474ee2e6.mp4?token=UE9PfvPTO4X6b_R93Kpita3YG9Fc7TduOr9XFlFiUvEQXru_nU26FERjj7AER8KF3oA35dGXWM6U1FheuX4c0YvI-bqS3KrjP-HPwNqiXrbNscgzqpUjE_CDpN6XpCVlKxggSPpja9iWyJ31_o3pKj-oPKs6TdeD7VWkT6R_GKowpU2JQcPpo8YlahDFREYeCtrqHntAgdAM9QdLhRhlv3QFUlYdkUj_9LUOsZ4TGF18W-GXo2KfImWULmD3Y4i7AuoQNDObhJ_Tf3rA5_x_c0gZ3x8s4V28y-OFMPrXBNd0YVHEQyQ3EEG291RZLZ4ApH8emEzTBT4q9yzZ-HfarA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیال‌بافی ترامپ در مورد ایران ادامه دارد
🔹
ترامپ: ما کنترل ونزوئلا را به دست گرفتیم، اساساً کنترل ایران را هم به دست گرفتیم! ما آن‌ها را تارومار کرده‌ایم. @Farsna</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/farsna/436869" target="_blank">📅 17:37 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436868">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1112f38c2a.mp4?token=swx1RBasR7tx4VRv0_iKqskg-_ugEpfXAlZOSIcAWsYj97JLvQWjrZdVLYlBpzSmquKiLFH-u8Jk59qzMRgkmtXU2-m4h9P_iJGkgWHHHKZj7KZwDRvTocV37UGzwOgCkTAm2CYvhMe2Avcx-tFjZ5ygkwXh_0RAy3Y3FNC4YJSaGH6IF1b9ofokzCOaaexvY9usNXozUyqrG8cVJ4-SFndSeAAVwHp4nnnzCVEfOv5X7fbRTdRq4GRtEsJnzfRhAYaf-55OOPa5G-4W0O2jJJWe8T1GeShP55gqgRU3zArGrWtcGfwlnpeIwq19OmwPJMS-DU0Hvjoebo688kZuVWf4ocrB6EgiASAcRj5_yMqpLFsU43ZTc5wQn6MN8Rp_avcuj9Lxa-0TJTvjsUeQaPTvnaaMKcS2LZMGzkHYTfRl8K5Ty8bXurVucSr9-ukv_Be0F6QVURa5Z1fZIU5jZYg2ofvw73Yc93sKKJyNY5zMtcv6aO_UTT_3fUXMAkzw8WNyFAWZOCPpiuge_gWHAVmPTkci9dNlXi9upPlC0UY5tOJKvJyfTmsPBOpoCUfJ2j7VY62b2mf2Y0j6JljHqusy1G7w-DZ4lBbi5UE9WKaSBof64iIn74c8T6mPMmsxETwzkoQ_Mv_vd7Mqjf2hvglp90ipZXY9rzkKDX3fOKs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1112f38c2a.mp4?token=swx1RBasR7tx4VRv0_iKqskg-_ugEpfXAlZOSIcAWsYj97JLvQWjrZdVLYlBpzSmquKiLFH-u8Jk59qzMRgkmtXU2-m4h9P_iJGkgWHHHKZj7KZwDRvTocV37UGzwOgCkTAm2CYvhMe2Avcx-tFjZ5ygkwXh_0RAy3Y3FNC4YJSaGH6IF1b9ofokzCOaaexvY9usNXozUyqrG8cVJ4-SFndSeAAVwHp4nnnzCVEfOv5X7fbRTdRq4GRtEsJnzfRhAYaf-55OOPa5G-4W0O2jJJWe8T1GeShP55gqgRU3zArGrWtcGfwlnpeIwq19OmwPJMS-DU0Hvjoebo688kZuVWf4ocrB6EgiASAcRj5_yMqpLFsU43ZTc5wQn6MN8Rp_avcuj9Lxa-0TJTvjsUeQaPTvnaaMKcS2LZMGzkHYTfRl8K5Ty8bXurVucSr9-ukv_Be0F6QVURa5Z1fZIU5jZYg2ofvw73Yc93sKKJyNY5zMtcv6aO_UTT_3fUXMAkzw8WNyFAWZOCPpiuge_gWHAVmPTkci9dNlXi9upPlC0UY5tOJKvJyfTmsPBOpoCUfJ2j7VY62b2mf2Y0j6JljHqusy1G7w-DZ4lBbi5UE9WKaSBof64iIn74c8T6mPMmsxETwzkoQ_Mv_vd7Mqjf2hvglp90ipZXY9rzkKDX3fOKs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: نتانیاهو هر کاری من بخواهم انجام می‌دهد
🔹
دونالد ترامپ، رئیس‌جمهور آمریکا امروز چهارشنبه تلاش‌ کرد به انتقادهایی که او را بابت راه‌اندازی جنگ علیه ایران بنا به خواست اسرائیل مورد سرزنش قرار می‌دهند پاسخ دهد.
🔹
او گفت: «نتانیاهو کارهایی که من بخواهم…</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/farsna/436868" target="_blank">📅 17:31 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436867">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/izEyyi2Vti-W1z_QK6SHzPyZFysQc246ZdzLpaIgKjV4lqivzjyaJJKcCAybgMEdluWLqwMVb89NgpiDIGGdogDhQzTPX6Wi3r-HFAwI5WXx2NOQn9zyo1FNSa5hEPCsS-vSeecnIO7KesnC9g67gBBC_ZuHSA-aX2nMDDIDS__shZW0llX3WAID0XAWF5iWA6WrHJw3rdUGd6woW7YA5bbavZKT2l4B-d9mq4mFi7M2H1BCy3txXbi3hl36JpULuSU5bbxuKdzsu5MLIwP6atinEc5N8mKq2CMtzZiuvqhweTeJIWJBQtrulZL_CJAtu3DE5dm43sH4MODUyZRRsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: نتانیاهو هر کاری من بخواهم انجام می‌دهد
🔹
دونالد ترامپ، رئیس‌جمهور آمریکا امروز چهارشنبه تلاش‌ کرد به انتقادهایی که او را بابت راه‌اندازی جنگ علیه ایران بنا به خواست اسرائیل مورد سرزنش قرار می‌دهند پاسخ دهد.
🔹
او گفت: «نتانیاهو کارهایی که من بخواهم را انجام خواهد داد.»
@FarsNewsInt</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/farsna/436867" target="_blank">📅 17:23 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436866">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rxbs8aN3-vW6h7qWS1RZlklbxE2BbMDv61Nk_aKystE-4CNmg__c5Gg1C1TqIjNowo7o1qBGX_wD5ZRaoRKKMcqA938dVKsGMogybhM8Bq7R9wmWv-UQXDFRAUjTaYx9yTtL8i9KtyZw4AFbSVJWOiz1ei2TbxRXaEJ0qd-bjsad-mnoi4c_Jsv5AILcPZtRqsRdaDecgJVopOXP6mziPEhpqvKKifuHT1bqePLfK-LbInphGYpcNV3hm2Pj8gE00LfTvcyQ7jvN_CNyq6X9ruVynwxnJvMYTCVqGmz5Z19Rddb6Fbj9B0bJA6Sx7cpxCiWLRA2ohAdLy-Qq9mDWaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استعفای مقام ارشد اطلاعاتی دولت ترامپ به‌دلیل مخالفت با جنگ ایران
🔹
واشنگتن‌پست: آماریلیس فاکس کندی، یکی از مقامات ارشد اطلاعاتی دولت ترامپ و متحد تولسی گابارد، مدیر اطلاعات ملی، این هفته از ۲ سمت کلیدی دولتی کناره‌گیری می‌کند.
🔹
خروج آماریلیس فاکس کندی به‌گفتۀ یک منبع، تا حدی به‌دلیل مخالفت او با اقدام نظامی ترامپ در ایران بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/farsna/436866" target="_blank">📅 17:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436865">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">‌
🔴
قالیباف: در شرایط جنگ اقتصادی روش‌های عادی کافی نیستند و وزارتخانه‌های اقتصادی باید با روش‌های خلاقانه دنبال حل مشکلات باشند. @Farsna</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/farsna/436865" target="_blank">📅 17:14 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436864">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‌
🔴
قالیباف: متاسفانه برخی با انگیزه‌های سیاسی و به بهانۀ گرانی‌ها بدون درنظر گرفتن واقعیت‌ها، انگشت اتهام را فقط به سوی دولت یا رئیس‌جمهور می‌گیرند.
🔸
برخی انتقادها از دولت به‌گونه‌ای است که گویی جنگی اتفاق نیفتاده است.
🔸
من منکر برخی ضعف‌های مدیریتی نیستم…</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/farsna/436864" target="_blank">📅 17:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436863">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‌
🔴
قالیباف: مردم انتظار دارند همه مسئولان هم‌راستا با بعثت اعجازگونۀ مردم برای حل مشکلات معیشتی به صورت جهادی تلاش کنند. @Farsna</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/farsna/436863" target="_blank">📅 17:09 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436862">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‌
🔴
قالیباف: از جهش قیمت‌ها و بالا رفتن هزینه‌های زندگی مردم اطلاع دارم
🔹
دشمن تصور می‌کند اگر زندگی مردم سخت‌تر شود، انسجام ملی تضعیف می‌شود اما مردم ثابت کردند که هم‌چنان در میدان مبارزه با دشمن حضور دارند و انتظار دارند که مسئولان مشکلات را حل کنند.  @Farsna</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/farsna/436862" target="_blank">📅 17:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436861">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‌
🔴
قالیباف: دشمن هنوز نفهمیده که ملت ایران در هر شرایطی در برابر زور سر خم نمی‌کند. @Farsna</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/farsna/436861" target="_blank">📅 17:06 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436860">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‌
🔴
قالیباف: باید با تقویت آمادگی برای پاسخ موثر به حملات احتمالی و همچنین با افزایش تاب‌آوری اقتصادی، دشمن را از خطای محاسباتی بیرون بیاوریم و ناامیدش کنیم. @Farsna</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/farsna/436860" target="_blank">📅 17:03 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436859">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‌
🔴
قالیباف: دشمن هنوز به تسلیم‌شدن ملت ایران امیدوار است و به غلط فکر می‌کند می‌تواند با تداوم محاصره و ازسرگیری جنگ ایران را مجاب کند که به زیاده‌خواهی آمریکا پاسخ مثبت دهد. @Farsna</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/farsna/436859" target="_blank">📅 17:02 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436858">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‌
🔴
قالیباف: دشمن را از تعرض مجدد به ایران پشیمان خواهیم کرد. @Farsna</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/farsna/436858" target="_blank">📅 16:59 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436857">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‌
🔴
قالیباف: مردم اطمینان داشته باشند نیروهای نظامی ما از فرصت آتش‌بس به بهترین شکل برای بازسازی توان خود استفاده کردند. @Farsna</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/farsna/436857" target="_blank">📅 16:57 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436856">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
قالیباف: تحرکات آشکار و پنهان دشمن نشان می‌دهد که به‌دنبال دور جدید جنگ است.  @Farsna</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/farsna/436856" target="_blank">📅 16:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436855">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
قالیباف: تحرکات آشکار و پنهان دشمن نشان می‌دهد که به‌دنبال دور جدید جنگ است.
@Farsna</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/farsna/436855" target="_blank">📅 16:55 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436854">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/783ffb553a.mp4?token=MGlHCVqZYYh3uUs86vY8Tm_YpPTJ9wZtNr8lk4g-3FBFeEY6wrXceS4kMbUUg7m5D-qAJ4ZfiitezIyz1OEAJFFsTHX6QO1xBjurGz526YxpYs5pXSyHpk8q-Bf7BOKSV0tuGIydGllqDBQLOIhCXSPnSbqYfIzR8ihqyHje8iluGSp5DzVpeYqkPK1QRYCl1rz1xd8VNNz2PjXR-8pkZisN2TzjboHztqqB7ncudnXxRPfo56mCAHqWf2en6mTUBWLEcgryQl8DrGPN7xgfSjMNiOnXlCTj61bIMadqbZJCqqpBljZXQ9oHxsqb6N33o4jtA1j5K2BmDTigupj1MFc3gVqDB7yy6OhWhkszkHBP78azZEsAQUQRxqVxaPfqV-zp7SYfGGshnNrBlscc0al-ilNe3vshVTCqz2GUndpHKKrMzQHURYUoHirAaSIry-uZcqs1PZ-w6bxu63Us1rH7nYlbPCVGvPDFmJhdI_QArhm8wp1x4DvhTJC5B1JcwHYD6P5hIt4TOzf_71hI8X3RHCkcOnn-xIr60ze4TqUg5953BiQICvBMXgnVl0Z0VEiabpEYDcML82xBub8Nj-TRv-XFQR7GbbyTr1-VmOU-iisQcIYddGoNVF-ulJxqOJ6zhfWZ39HPMf4BpEJOWjwbZVMcOoaFyexe7SyawfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/783ffb553a.mp4?token=MGlHCVqZYYh3uUs86vY8Tm_YpPTJ9wZtNr8lk4g-3FBFeEY6wrXceS4kMbUUg7m5D-qAJ4ZfiitezIyz1OEAJFFsTHX6QO1xBjurGz526YxpYs5pXSyHpk8q-Bf7BOKSV0tuGIydGllqDBQLOIhCXSPnSbqYfIzR8ihqyHje8iluGSp5DzVpeYqkPK1QRYCl1rz1xd8VNNz2PjXR-8pkZisN2TzjboHztqqB7ncudnXxRPfo56mCAHqWf2en6mTUBWLEcgryQl8DrGPN7xgfSjMNiOnXlCTj61bIMadqbZJCqqpBljZXQ9oHxsqb6N33o4jtA1j5K2BmDTigupj1MFc3gVqDB7yy6OhWhkszkHBP78azZEsAQUQRxqVxaPfqV-zp7SYfGGshnNrBlscc0al-ilNe3vshVTCqz2GUndpHKKrMzQHURYUoHirAaSIry-uZcqs1PZ-w6bxu63Us1rH7nYlbPCVGvPDFmJhdI_QArhm8wp1x4DvhTJC5B1JcwHYD6P5hIt4TOzf_71hI8X3RHCkcOnn-xIr60ze4TqUg5953BiQICvBMXgnVl0Z0VEiabpEYDcML82xBub8Nj-TRv-XFQR7GbbyTr1-VmOU-iisQcIYddGoNVF-ulJxqOJ6zhfWZ39HPMf4BpEJOWjwbZVMcOoaFyexe7SyawfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی: بیشترین آمار وزیر شهید، مربوط به وزارت خارجه است
🔹
همۀ مدیران وزارت خارجه در زمان جنگ در محل کارشان حاضر بودند. دشمن خیلی تلاش کرد اما حتی یک مورد پناهندگی در هیچ‌یک از نمایندگی‌هایمان نداشتیم و حتی یک دیپلمات هم محل کارش را ترک نکرد. @Farsna</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/farsna/436854" target="_blank">📅 16:55 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436853">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9abe99cec4.mp4?token=S2c3yyqEVCGBLMDdsBBS4uJuKG2ReQFngy9KZVD17gTzbsXV8XUtzBxfZqyObitLPu9_vZigDpYzGuk1UbMXAuY6daniL6lZbbmmrJ-0T0oYk4i01oPq6A51nBMc93CDYVlslnGUAEYZsQe0v5DPbEAdhxbUPyyi6V0QrMlHKA9YPBEezIt_Z5dWscALFW0XrXMIu6wKS9cCeDqAPGev7g6EtUIqHou5TqEcLnugXX0ErkPNcXjKGWD0TEZHAoWE6SBXfEcJ1rCtpXzzsXNFA3DdAidOMdNDE2Rhf4StYI_9FXjufqMuzF2HIrRD4KL7JssgpSk-tFn7esmd4TsOtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9abe99cec4.mp4?token=S2c3yyqEVCGBLMDdsBBS4uJuKG2ReQFngy9KZVD17gTzbsXV8XUtzBxfZqyObitLPu9_vZigDpYzGuk1UbMXAuY6daniL6lZbbmmrJ-0T0oYk4i01oPq6A51nBMc93CDYVlslnGUAEYZsQe0v5DPbEAdhxbUPyyi6V0QrMlHKA9YPBEezIt_Z5dWscALFW0XrXMIu6wKS9cCeDqAPGev7g6EtUIqHou5TqEcLnugXX0ErkPNcXjKGWD0TEZHAoWE6SBXfEcJ1rCtpXzzsXNFA3DdAidOMdNDE2Rhf4StYI_9FXjufqMuzF2HIrRD4KL7JssgpSk-tFn7esmd4TsOtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی: وزارت خارجه با فرماندهان نظامی هماهنگ است
🔹
دیپلمات‌های کشور در صورت تغییر نقش، با همان صلابت پشت لانچرهای دفاعی قرار می‌گیرند و نیروهای نظامی نیز در صورت اقتضا، با همان اقتدار پشت میز مذاکره خواهند نشست؛ چراکه تمامی نهادها هدفی مشترک را در یک مسیر…</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/farsna/436853" target="_blank">📅 16:51 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436852">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mQnME-4JR7oNZMDmfLziUIpUj1jf6qPLyU8mK0kNyjAyc06aypcmuZnTxWFZLlwN3LxaOeUsHLNWeDgnyqff2In1dkzadrtIjUPoUqlN2-meJ5vEM4NRLQoQ9YlARHrM4Lo_rqQn9x3qmI_f7eV-T1jkBThDsBxgCh0y2iZk8Y_NtQ1i2-SjxYbW4Ruhiq72tUJrRb1u42WvhJy3N3dMqq981UK7d3L_5X_-Y9CfzGu8gFC1WC_EnX6f_oKl8s7NHwzVBVd-0yFYatyTX7LTcNlW_ry24D8Gbo5oilcW3OM42tYBGt3tq_U1yqbRhtw4ezHbin_eMG9fg24MtIWbxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف: آمریکا دوباره در جنگی بی‌پایان که در آن امکان پیروزی ندارد گیر خواهد افتاد
🔹
رئیس مجلس در صفحهٔ خود عبارتی از فصل ۱۱ کتاب خاطرات ونس، معاون رئیس‌جمهور آمریکا نقل کرد: «ما احساس می‌کردیم در دو جنگ بی‌پایان و بدون امکان برد گیر افتاده‌ایم و سهم نامتناسبی از سربازان از محله خودمان (محله فقرا) آمده بود.»
🔹
قالیباف در ادامه نوشت: این وضعیت (گیر افتادن آمریکا در جنگی که نمی‌توانند ببرند) دوباره درحال تکرارشدن است. این‌بار فقرا و فراموش‌شدگان آمریکایی باید هزینهٔ جنگ‌افروزی الیگارش‌های نزدیک به کاخ سفید، افراد شیطان‌صفتی همچون جیمی دیمون و لابی تاجران جنگ در واشینگتن را بپردازند.
🔸
گفتنی است جیمی دیمون، مدیرعامل موسسه مالی و بانک جی‌پی مورگان، در آمریکا و از مهم‌ترین چهره‌های حلقهٔ تامین‌کنندگان مالی جنگ آمریکا با ایران است که به‌تازگی نیز علیه ایران لفاظی کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/farsna/436852" target="_blank">📅 16:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436851">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUmrsOgwpM6GxPD6SGwSiHNawkxkmRESgA63ZB8Lk55or7A1ePuB6fMPjDD6I1hZQL3GGoWBa9n3bwLmfAL3ZKyUgPpy24GrVob8yaR0VuUp08VPOk_dg8Ln8PfVl5Sg4BbomBgMk8B0AbaVzLBw972Bil-7dLRRG6DDMpJokjkXDTk2ixEX87WIvDMAo1N5nP37JdEkNUR9wdvW53onR8EHrX9x3zpiZ1EaplItzA6fnPeMrstRWRrvn5hYI3JHiOKBz31iEJRb1HOz8vE_8C1WV7JriQZ5_jMV1VKZASj9d5ceH871gyQHsoKSadKPUbV3bZ2geR7LuNF6KVwRmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور انتشارات فارس در نمایشگاه مجازی کتاب تهران
🔹
انتشارات خبرگزاری فارس با کتاب‌هایی با موضوعات رسانه، علوم شناختی، هوش مصنوعی و سیاست خارجی در هفتمین نمایشگاه مجازی کتاب حضور دارد.
🔹
کتاب‌ها را می‌توانید آنلاین از
صفحهٔ نمایشگاه
تهیه کنید.
🔹
ضمناً، علاقه‌مندان می‌توانند کتاب‌ها به‌صورت حضوری در «خیابان انقلاب، روبه‌روی دانشگاه تهران» با همان تخفیف‌ها تهیه کنند و از آثار ۷۰ ناشر حوزه رسانه نیز بازدید نمایند.
@Farsna</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/farsna/436851" target="_blank">📅 16:45 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436850">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kadhEgyh3XUktXiJ3kUoCz_PZLgAhp7DtAVV1iX3ZBZsSnC4FrTSHdI9_z7xRawswbnxNFkQIOzgSP1m4bF39u5ch9orn1YlHHv0T0rEmMYHiHxX_rTU5AVtARV9a3yEuXX49rXQW2zw4ccFZckPFEnnv3Yitwc7tQnsL60B6p5dt2bBeMzpQ4n72YDCeUiA0slqNYJlPHheEhJx_lzpK8F9ukCm4qjHJ6DFNQcc-4j_k70Wi3Pf7Xx1wGsYEsJDJPq78vPY5KY9yBH2cYDFSBwTyYW3axUdDYXGwkUMIJf0RvERvCzBkN9txzzbS6ktjMiXxCAClXa8prH0BYi1cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هتل‌های خالی آمریکا در جام‌جهانی
🔹
انجمن هتل‌ها و اقامتگاه‌های آمریکا (AHLA): ۷۰درصد از اتاق‌های رزرو شده در بوستون، دالاس، لس‌آنجلس، فیلادلفیا و سیاتل لغو شده‌اند.
🔹
طبق گزارش‌های منتشر شده در ماه گذشته از سوی صنعت گردشگری آمریکا، بیش از ۳۸۰۰۰ رزرو هتل مرتبط با جامجهانی ۲۰۲۶ در ایالات متحده ماه‌ها قبل از مسابقات لغو شده است.
🔹
حالا برنامه‌ریزی ترامپ با همکاری اینفانتینو و تبلیغ مداوم برای جام جهانی آمریکا کمتر از یک ماه به آغاز این تورنمنت با مشکل جدی مواجه شده و آمار فیفا از ۵۰ میلیون درخواست برای حضور در جام جهانی با هتل‌های خالی متضاد است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/farsna/436850" target="_blank">📅 16:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436849">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">عراقچی: وزارت خارجه با فرماندهان نظامی هماهنگ است
🔹
دیپلمات‌های کشور در صورت تغییر نقش، با همان صلابت پشت لانچرهای دفاعی قرار می‌گیرند و نیروهای نظامی نیز در صورت اقتضا، با همان اقتدار پشت میز مذاکره خواهند نشست؛ چراکه تمامی نهادها هدفی مشترک را در یک مسیر واحد دنبال می‌کنند.
🔹
نیروهای مسلح همواره قهرمانان ما هستند. در مسیر تحقق آرمان‌های کشور برخی جان خود را فدا می‌کنند و برخی دیگر از نام و آبروی خویش می‌گذرند.
🔹
ارتباط و هماهنگی مستمر و روزانه میان وزارت خارجه و فرماندهان نیروهای مسلح در سطوح مختلف جریان دارد.
@Farsna</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/farsna/436849" target="_blank">📅 16:37 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436848">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🎥
حملهٔ وزیر امنیت داخلی رژیم صهیونیستی به اعضای دستگیرشدهٔ ناوگان صمود  @Farsna</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/farsna/436848" target="_blank">📅 16:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436847">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cGaSVcmzL7WedypBGW3CYO3IogFm9DM0Vntm0mFkL_0DoDtII9lnqChZzqT5vnGZ9T296T1rd4LBXcHQrh3b-2AANNQJDEEC4_FIRH-OvlruW0swMFi3dl-awM7fk4aIPld5Cj3hmWeOktLzuiRdWXNv45j93yxuKuDkIPNCZbUqONDDPHOx8uqQSQ7xTgW-fJDc1kfoA6_GDu2-DAg8hHIZ6a8gDGgUVMpDgljBiwtqdrlfyD8thxuIegcNmdL5PSSnzPBYsBVjzkctLXcXfeP8UTF8OQO-HP_Ikw5KGr6q2IlLQSk_03aYbHYSXUWMp5mIy4XKumJcbBWf8f2jhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف: شهید رئیسی راه حل مشکلات کشور را در بازگشت به آرمان‌های انقلاب می‌دانست
🔹
پیام رئیس‌مجلس به‌مناسبت دومین سالروز شهادت آیت‌الله رئیسی و دیگر شهدای خدمت: در میان شهدای پرواز اردیبهشت، فقدان برادر متدین، صادق، ولایت‌مدار، پرکار، مردم‌دار و عدالت‌طلب…</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/farsna/436847" target="_blank">📅 16:19 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436846">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pWo3TDcWxcuWUyEwd3TMrRQbfDItnS9PhqLet1SmNvom77-BRZrP1qDGfzukgb5xok9CBmjNJn-ejM4qB-6iH8oJveHR8Pyd4pwkDKc-gp9WQlmaVcCFcQjQUMMuuos6QCXY5lQ1O8vegZ5ik4-yUWW88Ltdf_nBq6wZ2QpDW6GFUtjLDDEk1Se6kOi67Fdsywry2Nf64jdXVjE8xo5qMkm2a0QKxuV9Hv6O32nvpibjABIpEeiMKk5MLDsnWWAlVd1_CJFpVRIBgTxeS71BVVbpFrN3WHZbF94rdO0Ver7iYfJCbdNS_v9RS8fmCRTXBV1jMeHoKaLHWtxxZwkLqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار ارتش اسرائیل: با کمبود ۱۲ هزار نیرو روبرو هستیم
🔹
سرتیپ شای طیب، رئیس شعبه برنامه‌ریزی و مدیریت نیروی انسانی ارتش رژیم اشغالگر، نسبت به تشدید بحران جذب نیرو در مؤسسه نظامی این رژیم هشدار داد و وضعیت فعلی را «مشکلی هنجاری و قانونی» توصیف کرد که نیازهای عملیاتی را تهدید می‌کند.
🔹
به نقل از المیادین، طیب در جریان گفتگویی در کمیسیون روابط خارجی و امنیت کنست (پارلمان اسرائیل) در مورد قانون معافیت از خدمت سربازی، اظهار داشت که ارتش به طور فوری به حدود ۱۲ هزار نظامی دیگر نیاز دارد که ۷۵۰۰ نفر از آنها نیروی رزمی برای پر کردن شکاف‌های میدانی هستند.
🔹
روزنامه یدیعوت آحارونوت گزارش داد، این مقام نظامی، به حدود ۳۲ هزار نفر که در حال حاضر از خدمت سربازی غایب هستند، علاوه بر بیش از ۵۰ هزار نفری که تحت عنوان «دستورالعمل دوازدهم» قرار می‌گیرند، (کسانی که مراحل خدمت را گذرانده‌اند) اشاره کرد و ابراز تأسف نمود که بخش زیادی از آنها به زودی به غایبین از خدمت تبدیل خواهند شد، مگر اینکه همکاری نشان دهند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/farsna/436846" target="_blank">📅 16:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436845">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QcW1CSEY1Ww8sdSCbIxxgp1iAddI6pvyNPzGtDdJ-0tTvMK7kaQ0JNgB_F47vsRX8RTSV-FX5B5fOw3JcPn7FC-KWkkJnK0QPiQaHNxQ7YVOmWy8M74L20MEilnpsSlPR_oKXkOQV46Z7S3ArvUJnxYFRJXNsf9eQ8Iy6xyzy2zERz8S3fALiwFWPsgKPHpqB4q9-fDnEPA3s10oElkqdnKZzVs1Ty378OpRhTMH72CQm4lP0qSuW1uH-Ed2bkGImWURCskP7dNQ3KAz5Mxgt57M9hRYiJf_XeEh-yli1xkfcwNgWt6HbZIB5uwTKzEF5BwEOsrcCBWLu3FT6Pifsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری قوه‌قضائیه: [رشید مظاهری] بازیکن سابق فوتبال هنگام خروج غیرقانونی از کشور بازداشت شده است
🔹
خبرگزاری قوه‌قضائیه نوشت: «در روزهای اخیر همسر بازیکن سابق فوتبال، در فضای مجازی ادعاهایی را در رابطه با همسر خود مطرح کرده است.
🔹
پیگیری‌ها نشان می‌دهد نامبرده…</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/farsna/436845" target="_blank">📅 16:05 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436844">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBVaBqaROAE5ydJCCuTRqZzUATdezbDYZC6vxowqkOqC2L1cqC7caonBezxzbNZp9nBk61Kb67ds6MjnoHhwlgTql4UptyucSIFvL8J1fm8W6rv_ABBwakZQgds832QU3FsEbOztsKf1QQFBVKz_m2jE3epLniM505uA55DMXzvMOXS3VpXGBGV3QQ4I-HEy619CjnZYhXOfDfjKrwrFqvfSzpMcPq8jL1uQuNg9DfxnYauINrYIvxcK0e2yuAprFY7sD7_aUSQxQxGVFT-qhUI1sBZWf4eHI_x96sOUWHC1oktawKZ9bt8n-yYK8XauU-I3Az0CEdxjH5PDqmBPiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه: ۲۶ کشتی با هماهنگی نیرودریایی سپاه عبور کردند
🔹
فرماندهی نیروی دریایی سپاه: در شبانه‌روز گذشته ۲۶ فروند کشتی اعم از نفتکش، کانتینر‌بر و سایر کشتی‌های تجاری با هماهنگی و تامین امنیت نیروی دریایی سپاه از تنگهٔ هرمز عبور کردند.
🔹
تردد از تنگهٔ هرمز با کسب مجوز و با هماهنگی نیروی دریایی سپاه درحال انجام است.
@Farsna</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/farsna/436844" target="_blank">📅 15:52 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436843">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43e5a15433.mp4?token=kddohwS9CL2sm53-aqXm1SlTTOFfH6j-2Apl7gZmxJdFPTk8YjeQ_bO--t4T1pgnKEMK11knBVpFyNehk3IqjQfB9sNtFyKKqSklrqdM_uNlVav4CZ-iT_ywWfxQGSeh5dm_9tn2xa-xamCMAncPEAu-ZcMbQw7XtCF25PDd0Blht4VEkc2xG4GuzuA6yWbGZklIFw9vnox3vdt-QytO2VEWxvUj8HkgGRhqxqPlIqs5U4vLiwPP4p2yMfzZrGHjfs3QdK06rTeeTord_e9IvGU6clzopN-QCambsHu3oMd3mvWwGFBBOio5c9icgW7JpwKgJgw52VR0zy6h7ugN9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43e5a15433.mp4?token=kddohwS9CL2sm53-aqXm1SlTTOFfH6j-2Apl7gZmxJdFPTk8YjeQ_bO--t4T1pgnKEMK11knBVpFyNehk3IqjQfB9sNtFyKKqSklrqdM_uNlVav4CZ-iT_ywWfxQGSeh5dm_9tn2xa-xamCMAncPEAu-ZcMbQw7XtCF25PDd0Blht4VEkc2xG4GuzuA6yWbGZklIFw9vnox3vdt-QytO2VEWxvUj8HkgGRhqxqPlIqs5U4vLiwPP4p2yMfzZrGHjfs3QdK06rTeeTord_e9IvGU6clzopN-QCambsHu3oMd3mvWwGFBBOio5c9icgW7JpwKgJgw52VR0zy6h7ugN9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دستیار ویژۀ وزیر کشور: در صورت تعرض به ایران، باب‌المندب به معادلات جنگ وارد می‌شود
🔹
سرتیپ نامی: ۳ تنگۀ هرمز، مالاکا و باب‌المندب مهم‌ترین چک پوینت‌های استراتژی جهان هستند. تا الان بنا به‌دلایلی فقط از ظرفیت تنگۀ هرمز استفاده کردیم.
🔹
اگر زمانی مجبور شویم…</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/farsna/436843" target="_blank">📅 15:48 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436842">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5536424c44.mp4?token=eDypT9CcIHWEdkXIsJF0blIVQAYRVDfj_jh8J40YLXXj098-E4rIFR62wxmCxVjao5Pb3rLE0qTVGWHtTsEjrKii1B3Rx4t2LDgQf9NNfgQAXoAvfeflM6BLcB0xDQBtdcKfe0TNhShD8GYQVDczI-vAR4yNmfiyAGAxjXvUhp2RSFuuM7omGf_mDh4YqEfRt4-tOB9SIsybzPI32MbcV_oHw0KUV459jRXlhe8VZLoxGJDsKsWa1nFYXnCbIYtAv2TLOTbkv5a7j0VGcFHoBQO05oT53LYuQaYPuG4DshxcM5uqXYEspKcszkNqeAgNUqyk49ivTiBxU938WVKKow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5536424c44.mp4?token=eDypT9CcIHWEdkXIsJF0blIVQAYRVDfj_jh8J40YLXXj098-E4rIFR62wxmCxVjao5Pb3rLE0qTVGWHtTsEjrKii1B3Rx4t2LDgQf9NNfgQAXoAvfeflM6BLcB0xDQBtdcKfe0TNhShD8GYQVDczI-vAR4yNmfiyAGAxjXvUhp2RSFuuM7omGf_mDh4YqEfRt4-tOB9SIsybzPI32MbcV_oHw0KUV459jRXlhe8VZLoxGJDsKsWa1nFYXnCbIYtAv2TLOTbkv5a7j0VGcFHoBQO05oT53LYuQaYPuG4DshxcM5uqXYEspKcszkNqeAgNUqyk49ivTiBxU938WVKKow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شکار یک سکوی گنبد آهنین توسط حزب‌الله
@Farsna</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/farsna/436842" target="_blank">📅 15:30 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436841">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‌
🔴
حزب‌الله: تجمعی از خودروها و سربازان ارتش رژیم صهیونیستی را در مسیر رودخانه در حاشیهٔ شهر دیر سریان با گلوله‌های توپخانه هدف قرار دادیم.  @Farsna</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/farsna/436841" target="_blank">📅 15:23 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436840">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af878bb26d.mp4?token=AK_OmdEfcC65YXnaFIvEdjkAVa4i6etvke0JzdkvOIQsQneXL-8TmZXOkv5OpvvdN-UMJkmMWTjkKLMzQlPSkgzwKlccEesupdd0WqWzV9m7mj_cbI_1pyoTpkk177MjyGm1Br7D5i6sms7NKPZnjQzuzD13OvsDtZQF8y838-N2ap9GjceZysCW6sPjKPmvjOS9SVhOx73vEmGQN19_oCfo8HJ_B9mnr9-v6kRlGwJJ8iWA9pNBNYmTkCSCnaLINMaH2wBU8ikVvzRU7LJGH3bwLZn_RP5-aT_K-VXUwcK6Tbolt9LfoWtT7BxZI-j8MUTTrsrU_n8HhtXbyRoBRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af878bb26d.mp4?token=AK_OmdEfcC65YXnaFIvEdjkAVa4i6etvke0JzdkvOIQsQneXL-8TmZXOkv5OpvvdN-UMJkmMWTjkKLMzQlPSkgzwKlccEesupdd0WqWzV9m7mj_cbI_1pyoTpkk177MjyGm1Br7D5i6sms7NKPZnjQzuzD13OvsDtZQF8y838-N2ap9GjceZysCW6sPjKPmvjOS9SVhOx73vEmGQN19_oCfo8HJ_B9mnr9-v6kRlGwJJ8iWA9pNBNYmTkCSCnaLINMaH2wBU8ikVvzRU7LJGH3bwLZn_RP5-aT_K-VXUwcK6Tbolt9LfoWtT7BxZI-j8MUTTrsrU_n8HhtXbyRoBRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فعال اصلاح‌طلب: مردم‌داری شهید رئیسی در تاریخ ماندگار ‌شد
🔹
باقری، دبیرکل حزب عهد ایران: اگر رؤسای جمهور ادوار را بخواهیم مرور کنیم، شهید رئیسی از حیث مردم‌دار بودن، پروتکل نداشتن، هدف قراردادن منافع مردم و توده‌های مردم، خصوصاً توده‌های کمتر برخوردار یک ویژگی بارزی داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/farsna/436840" target="_blank">📅 15:20 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436839">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
حزب‌الله: تجمع نظامیان و خودروهای رژیم صهیونیستی در شهرهای دبل و رشاف را با حملات موشکی هدف قرار دادیم.  @Farsna</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/farsna/436839" target="_blank">📅 15:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436838">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IM_wSbaaAMySCX6z5k6tcNvfaKJFAPoWyhoQLYLVxvfWCfwgG3PSohxKq9lpNXa5JNVga6GDiAVLgYgk4VsCCvDo0ttMIUNXhug0GaSaKOVpXMDR2ihMxKD-osByo9cVs2bdRokR1-wChBM0QtyjPu3PfY3Nii_4MOtxoU2iqV6ENUA0Fu6u8kaKr7mpqzPnSt3iimpIXc5gaKw6Do0-sgdjG5a8mVURcw4LqNg8K_sDHow7iRL3Ye-rLG3R8OMR3LLjwGB7bWdpeXKmp7w8PJruH0U7pqAXOEWEbgYuedomWdckBse-hS5eFLPJbir292kmLiPq9Es-MElfZVzqGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازگشت بنزین سوپر ایرانی به جایگاه‌ها
🔹
دولت به پالایشگاه‌های کشور دستور داد، تولید بنزین باکیفیت موسوم به بنزین سوپر را از سر بگیرند.
🔹
از سال ۹۸ کمبود تولید بنزین نسبت به مصرف سبب شده بود تا تولید بنزین سوپر متوقف شود.
🔸
بنزین سوپر نوعی بنزین با عدد اکتان بالاتر نسبت به بنزین معمولی است که برای کاهش پدیدهٔ ناک (احتراق زودرس) و بهبود عملکرد موتورهای با نسبت تراکم بالاتر استفاده می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/farsna/436838" target="_blank">📅 15:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436837">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3ac56848f.mp4?token=pfWRZtlhxvIcf874Jj9YqvB70Ap63J-Xocy6Vc3o-C5KayXlTP4byT6NW4lN4l4-eoxhDBKr5yynmx-Nag5gP-QRtSgMwOYPeYT4pDqr99P3BZjvPHaLJNGAgh9bCe5ggCopHWQztPNq5Bz1Hdt7IABy5zbul9p0wV90st4hEYpIoKjqpbyDQeRyfylGe9QkKdqTmVX8AB1b18YZq7bpR-psBCvrZCNLWnG5LsrcbsSf_A7p7p6xD9z6BxHLHPr9F8CZB6MwfOQoHbW1bbUOV84io9QHmtFrKczBXErPuM8Qchr4itGtEAvB9paRRrOMgxkAeVeqRg7Vcf4y9jsDew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3ac56848f.mp4?token=pfWRZtlhxvIcf874Jj9YqvB70Ap63J-Xocy6Vc3o-C5KayXlTP4byT6NW4lN4l4-eoxhDBKr5yynmx-Nag5gP-QRtSgMwOYPeYT4pDqr99P3BZjvPHaLJNGAgh9bCe5ggCopHWQztPNq5Bz1Hdt7IABy5zbul9p0wV90st4hEYpIoKjqpbyDQeRyfylGe9QkKdqTmVX8AB1b18YZq7bpR-psBCvrZCNLWnG5LsrcbsSf_A7p7p6xD9z6BxHLHPr9F8CZB6MwfOQoHbW1bbUOV84io9QHmtFrKczBXErPuM8Qchr4itGtEAvB9paRRrOMgxkAeVeqRg7Vcf4y9jsDew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تکمیل دزدی دریایی صهیونیست‌ها علیه ناوگان جهانی صمود
🔹
نیروی دریایی رژیم صهیونیستی ساعاتی پیش به کشتی‌ها و قایق‌های باقی‌مانده ناوگان صمود که برای درهم شکستن محاصره به سوی نوار غزه در حال عزیمت بودند در آب‌های بین‌المللی حمله و آن را توقیف کرد.
🔸
نظامیان صهیونیست…</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/farsna/436837" target="_blank">📅 15:02 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436836">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a162fc100d.mp4?token=bf2sPjNxk5edQrZ1lb8c_0fw_uKSbdkMDQ1lfWjyoRc48aK-idnOQJy48GCP0xFPVuCOal-kQ8b_wt95gxfSEzEb4p5J3vCFS3V7GdMG1Khua_ntC4pvN-iLvqQz0-lxf4boQ--8Uj2rEl6OcDPcEhBqts8M54Cdz1xvHpOaUGMOiiudp4Vpp2MxqQ31yckPoR1eo01SmqXppiYJDpK030S4B47VZXUIKMBHOYCqyFCj5lS-IWGPHrcYtS4HHwuPpvFumvIHw5GQ1MAU0ipdQTSVKcj3J4_cbLF65uIQEsKH72cdLPJNul54y8rCwGRk5C1sgCOLA0htkt0aRI5rWoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a162fc100d.mp4?token=bf2sPjNxk5edQrZ1lb8c_0fw_uKSbdkMDQ1lfWjyoRc48aK-idnOQJy48GCP0xFPVuCOal-kQ8b_wt95gxfSEzEb4p5J3vCFS3V7GdMG1Khua_ntC4pvN-iLvqQz0-lxf4boQ--8Uj2rEl6OcDPcEhBqts8M54Cdz1xvHpOaUGMOiiudp4Vpp2MxqQ31yckPoR1eo01SmqXppiYJDpK030S4B47VZXUIKMBHOYCqyFCj5lS-IWGPHrcYtS4HHwuPpvFumvIHw5GQ1MAU0ipdQTSVKcj3J4_cbLF65uIQEsKH72cdLPJNul54y8rCwGRk5C1sgCOLA0htkt0aRI5rWoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور: با روش‌های گذشته نمی‌توان بر همۀ مسائل امروز کشور غلبه کرد
🔹
پزشکیان در نشست سراسری استانداران کشور: روش‌هایی که تاکنون برای اداره کشور مورد استفاده قرار گرفته، در شرایط فعلی به‌تنهایی پاسخگوی همه مسایل نیست.
🔹
ضروری است با نگاهی نو، روش‌های جدید…</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/farsna/436836" target="_blank">📅 14:55 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436835">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ساعت‌های سرنوشت‌ساز برای انحلال پارلمان اسرائیل
🔹
در بحبوحهٔ افزایش تنش‌ها در ائتلاف حاکم رژیم صهیونیستی به رهبری نتانیاهو و تشدید بحران قانون معافیت حریدی‌ها از خدمت نظامی، کنست امروز در بررسی مقدماتی، به طرح‌های قانونی با هدف انحلال آن رأی می‌دهد.
🔹
کانال…</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/farsna/436835" target="_blank">📅 14:45 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436834">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14687e4509.mp4?token=P0a9XJaH_4ZxtVXqKioZtnym7QRaCdC7Jnr93HuL8eJ_K0_vLWPkCyTXSnUvHsPmYofkwvEMOwSQQJZccmVmf44Vw6oshqZB83MG7Ub_xKAvkiAdbC-cMQ59iRUH2NmE1cAKkeLOKvykilZjma8nkUINBgCc4ERvhHSNSu6MMe3156euAMg-8qNDP6Qe9DD-ovkgSWRqx68Kg0MXvn3vw1eV1ILV-7lvcgOOi3L7Kww2lafrxDePCgYWLXWRk8229DGZgDEo3IAqCX4XythL9q7GIwEJzPpmbYn6h2bon4dAYIydGWqWum-JxSxQxx0W2WGFQwoq0c7jmI1q8Cm1TZDHdTJpindjvvz53_0VnDDi76AvlzBDlmvOgWQ3pTVXQOMaWn9AjVG0Zs_vcMPesVI-T9clR8PmWIyiEnWoBcUHWHxxjKDIiNKWijNR82nhrO1nhESg2hDeLoIWzfufgEiEn440BvuoEFW9Xi4J_LeBEZzlw5BgzcRQtXZ295cBNhZWRlem7z_muXJVvV4CcJuauL-LdDsAb706k8eFeoRrHWQdQeH4GQugBQgPmXDrxnrFXrDWfzSzdmOmecC-SyILNk0AhHtNyYYKEnQs4SP1n6YiVfibWOIpxqwPhzqU4lu5zhVj90ze4GVD2V_RRcOXGq27K3DH9HytiKC0-Z0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14687e4509.mp4?token=P0a9XJaH_4ZxtVXqKioZtnym7QRaCdC7Jnr93HuL8eJ_K0_vLWPkCyTXSnUvHsPmYofkwvEMOwSQQJZccmVmf44Vw6oshqZB83MG7Ub_xKAvkiAdbC-cMQ59iRUH2NmE1cAKkeLOKvykilZjma8nkUINBgCc4ERvhHSNSu6MMe3156euAMg-8qNDP6Qe9DD-ovkgSWRqx68Kg0MXvn3vw1eV1ILV-7lvcgOOi3L7Kww2lafrxDePCgYWLXWRk8229DGZgDEo3IAqCX4XythL9q7GIwEJzPpmbYn6h2bon4dAYIydGWqWum-JxSxQxx0W2WGFQwoq0c7jmI1q8Cm1TZDHdTJpindjvvz53_0VnDDi76AvlzBDlmvOgWQ3pTVXQOMaWn9AjVG0Zs_vcMPesVI-T9clR8PmWIyiEnWoBcUHWHxxjKDIiNKWijNR82nhrO1nhESg2hDeLoIWzfufgEiEn440BvuoEFW9Xi4J_LeBEZzlw5BgzcRQtXZ295cBNhZWRlem7z_muXJVvV4CcJuauL-LdDsAb706k8eFeoRrHWQdQeH4GQugBQgPmXDrxnrFXrDWfzSzdmOmecC-SyILNk0AhHtNyYYKEnQs4SP1n6YiVfibWOIpxqwPhzqU4lu5zhVj90ze4GVD2V_RRcOXGq27K3DH9HytiKC0-Z0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر: قلب ما برای بچه‌های فوتبال است. دعا می‌کنم تیم ملی از گروهش صعود کند.
🔹
۹۵ درصد ایرانی‌های خارج از کشور بی‌نظیرند. نگاه به درپیت‌های اینترنشنال نکنید که می‌رقصند. آن‌ها برای ۲۰ دلار پشتک می‌زنند.
🔹
ایرانی‌های واقعی در آمریکا نگذارند کسی بیاید تیم ملی فوتبال را اذیت کند.
@Sportfars</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/farsna/436834" target="_blank">📅 14:35 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436833">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94271ae1b3.mp4?token=vOXFWF522DZdoPVt5v_BKUZp_BIocc0YePIeBBbEuaZCkVKEaL-ez2CgT-WlacAX1_IZzGvwtPr6Z6SuEPdSSvD7e7gA4KdSiILvJAHt1yQQCl3at694JRCdXYejvEoZrPFl0QxiNruBRSgveZ99gzK9v4lwI_QwBR6qZusguFZgm_XQiZEVdMWF0dffwA92kuusJRTSp4lRMPvfn09KlPwJ0yVzoypq6ZzkDlcSln7lmhjiv45KmIwDpS-AFiXLsuQCABlIYpWjnO3uh1M6D4owkDEs2lU5NlA_jOMLCA9Og6DJZL_7x3VzSae6ccP61KEbaG14Cbbc-0CVKkg8Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94271ae1b3.mp4?token=vOXFWF522DZdoPVt5v_BKUZp_BIocc0YePIeBBbEuaZCkVKEaL-ez2CgT-WlacAX1_IZzGvwtPr6Z6SuEPdSSvD7e7gA4KdSiILvJAHt1yQQCl3at694JRCdXYejvEoZrPFl0QxiNruBRSgveZ99gzK9v4lwI_QwBR6qZusguFZgm_XQiZEVdMWF0dffwA92kuusJRTSp4lRMPvfn09KlPwJ0yVzoypq6ZzkDlcSln7lmhjiv45KmIwDpS-AFiXLsuQCABlIYpWjnO3uh1M6D4owkDEs2lU5NlA_jOMLCA9Og6DJZL_7x3VzSae6ccP61KEbaG14Cbbc-0CVKkg8Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عبور شناورهای ملیت‌های مختلف به‌ویژه شرق آسیا از تنگۀ هرمز بیشتر شد
🔹
خبرنگار صداوسیما در تنگه هرمز: سفیدپوشان نیروی دریایی ارتش در عمق تا شمال اقیانوس هند آرایش و بازآرایی متناسب گرفتند و از این سو سبزپوشان نیروی دریایی سپاه در همۀ سواحل و جزایر برای دفاع در اوج آمادگی به‌سر می‌برند.
@Farsna</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/farsna/436833" target="_blank">📅 14:27 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436832">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27322a441a.mp4?token=l8-mGeVpl1a_U7ZjFBVP7e8divUr8SvXxT7LHrg7mjshVv5lYwRPLgLHh5BlHr_cfKuToenuXA4VutNWyrRX59huH5SVmTBKiB7bV3uginxXO4l0Knmbq6YdgTdJ3Oie4BGZKYVVVEMFB_Jr7y-hYSqvwsntr7ngS6q0S8WaQcXhH6UHetYLizvKxu-B5wjsAVTvFOYdTY3qv70uQpwMXzilmfsNp4zejyLX4OcqtnBLSTFQy55_JLCAWZalKzewhKf-FG2AJH8loZyAZ8UlAS77E8bYEW2z9EP6eAjjVCXhLvHefBb6XUwcHWgxDCCEdMcuqK5znD4xPj4H8AHbAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27322a441a.mp4?token=l8-mGeVpl1a_U7ZjFBVP7e8divUr8SvXxT7LHrg7mjshVv5lYwRPLgLHh5BlHr_cfKuToenuXA4VutNWyrRX59huH5SVmTBKiB7bV3uginxXO4l0Knmbq6YdgTdJ3Oie4BGZKYVVVEMFB_Jr7y-hYSqvwsntr7ngS6q0S8WaQcXhH6UHetYLizvKxu-B5wjsAVTvFOYdTY3qv70uQpwMXzilmfsNp4zejyLX4OcqtnBLSTFQy55_JLCAWZalKzewhKf-FG2AJH8loZyAZ8UlAS77E8bYEW2z9EP6eAjjVCXhLvHefBb6XUwcHWgxDCCEdMcuqK5znD4xPj4H8AHbAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام رهبر انقلاب اسلامی به‌مناسبت دومین سالگرد شهادت شهید رئیسی و بزرگداشت شهدای خدمت
🔹
گرامیداشت شهدای پرواز اردیبهشت و در رأس آنان رئیس‌جمهور شهید حجت‌الاسلام والمسلمین رئیسی، یادآور شهادت خیل شهیدان خدمتگزار در جمهوری اسلامی ایران است؛ از مطهری و بهشتی…</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/farsna/436832" target="_blank">📅 14:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436831">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">پیام رهبر انقلاب اسلامی به‌مناسبت دومین سالگرد شهادت شهید رئیسی و بزرگداشت شهدای خدمت
🔹
گرامیداشت شهدای پرواز اردیبهشت و در رأس آنان رئیس‌جمهور شهید حجت‌الاسلام والمسلمین رئیسی، یادآور شهادت خیل شهیدان خدمتگزار در جمهوری اسلامی ایران است؛ از مطهری و بهشتی…</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/farsna/436831" target="_blank">📅 14:04 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436830">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EhnLQYgqwRlhA0od9xwcf9Lwg7YqNH5JNETIaMCVt8V8rnSJCng9YPc5Ih6iMrjJWto4Pn7VuNpjJYV2OLXZgjs5le1KE0DCOVTO49pawWo5rOF3ekw_hTyUP3HgLw-eHL8c5aQmKuaZruHgrSadXQrm2ZYFbl99IAABoKDjh6MyuFezfeYJNOlH890fuQL-62ZATZlQOuHTGDooMAB90URSAyDP8QS6TpTf1SknNfXNizWAJRHgNKsyhNZByQmAauiOhtj_mwyR5b14tHk3sw4KACQRJIdY4bRipBZsoxppnHmcl59vUZftrG390hj4lIUsWeifwxhZ1mea0jvlhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
تا ساعتی دیگر پیام رهبر انقلاب به‌مناسبت دومین سالگرد شهادت شهید رئیسی و بزرگداشت شهدای خدمت منتشر خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/farsna/436830" target="_blank">📅 14:01 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436829">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/078eb7e4b1.mp4?token=cwikG9LSDzH_OpOvB_xMRPZ2UOo_Tuufa3V-I0cafk75R-rvgca6iGk0QxI3JRnomnJNRGdUljZGnSiu3Qmecjby8tuS4iCjFH2PVrIM_Ri7WKaF5IcrUtDCNcxvqCDqXWzVf-Cm3g8GUK989eHgYlTNzhe6Wkd0dDHYx2A4HWxW_iXyFe3NZhVTueHuTX6z9hDOY6llbmauixle08FX_J_1rmT4ACwC7Omk-Ybgb9IXcnRtgYCZ7KET9EtFTo00CIom5SSyZG921fCaKOl9QS6CEuhirX51Fqw1FuUNqKC8CLzNJ-FQVEYL3m1oXmnuI2Opr--aMSVClv1NwQXpsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/078eb7e4b1.mp4?token=cwikG9LSDzH_OpOvB_xMRPZ2UOo_Tuufa3V-I0cafk75R-rvgca6iGk0QxI3JRnomnJNRGdUljZGnSiu3Qmecjby8tuS4iCjFH2PVrIM_Ri7WKaF5IcrUtDCNcxvqCDqXWzVf-Cm3g8GUK989eHgYlTNzhe6Wkd0dDHYx2A4HWxW_iXyFe3NZhVTueHuTX6z9hDOY6llbmauixle08FX_J_1rmT4ACwC7Omk-Ybgb9IXcnRtgYCZ7KET9EtFTo00CIom5SSyZG921fCaKOl9QS6CEuhirX51Fqw1FuUNqKC8CLzNJ-FQVEYL3m1oXmnuI2Opr--aMSVClv1NwQXpsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">احتکار ۱۴۰۰ تنی مرغ منجمد در شیراز
🔹
تعزیرات حکومتی فارس: در بازرسی از یک کشتارگاه در شیراز، ۱۴۰۰ تن مرغ کشف شد که از ابتدای جنگ تحمیلی در ۹ سردخانه احتکار شده بود.
🔸
یک محمولهٔ مرغ منجمد ۹۰۰ تنی دیگر نیز روز گذشته در شیراز کشف شده بود.  @Farsna - Link</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/farsna/436829" target="_blank">📅 13:58 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436828">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJwFbjd6g8k9ia0LLOzh7lt0xZqKhajaHhfSL1xFTeo2a3Bjuq_MDa4UYkwzV1B69DB2o8CzsKNd_IGHA55YxOye4eJyKC2YObgQ6ZB-51gHEC-grQHs3UaDVeydAFrYcuVqQn_Qy1yfCeSBvzCS2npqK_EV7qZZDRso2efvuOFxsSPiOpED-F3rr_X2ZE5TjLQ2l0HY8vCfanDlc-1cO2HBkf_JmslYDWcmdCCZbblrYJ3fTtI3epgWEcNktIC3DlI6YuowWzAQ9KdEaZqOv8SNQ5aPCWKyomOUvNdLStaz7PkO09-caOqrfQzADdyMSbPVkqaKjZu2qDHyu3nTVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس اولین روز بعداز جنگ را مثبت تمام کرد
🔹
شاخص کل بورس در پایان معاملات امروز با رشد ۲۵۰۰ واحدی به ۳ میلیون و ۷۱۶ هزار واحد رسید. @Farsna</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/farsna/436828" target="_blank">📅 13:36 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436827">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">خبرگزاری قوه‌قضائیه: [رشید مظاهری] بازیکن سابق فوتبال هنگام خروج غیرقانونی از کشور بازداشت شده است
🔹
خبرگزاری قوه‌قضائیه نوشت: «در روزهای اخیر همسر بازیکن سابق فوتبال، در فضای مجازی ادعاهایی را در رابطه با همسر خود مطرح کرده است.
🔹
پیگیری‌ها نشان می‌دهد نامبرده قصد داشته با تغییر چهره و پرداخت رشوه به ماموران مرزبانی از مرزهای غربی به صورت غیرقانونی از کشور خارج شود که در هنگام خروج‌‌ بازداشت شده است.
🔹
همچنین ادعای نگهداری متهم در سلول انفرادی نیز صحت ندارد و نامبرده در بند عمومی زندان حضور دارد تا به اتهامات او از جمله پرداخت رشوه به مامور دولت، فعالیت تبلیغی برخلاف امنیت ملی کشور در شرایط جنگی و اقدام به عبور غیرمجاز از مرز رسیدگی شود.»
@Farsna</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/farsna/436827" target="_blank">📅 13:26 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436826">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db8f77da65.mp4?token=oFCpistVBZ-2VU5ICpUIo8zQC0-QuSHmhMAIb7GzP53WT_6OJfgiKGQ3_d6Zek-bOrkFuiB5WveAFQhL2SAmzYMDu6BUYOxAMLcYSXE_vYQpkxdOBnys6OOt3Xr87ZYA2vEn5zUZiRtQD1WGBcPQkPOXDSvyLqBjL5j8OE80cBfGd6heeuP2diIq9Pj8N29XJN-qsNayVe8162_Qnr4BxFqcq5BH5viIHJeKgLcdWxzaiQ4d6BLfbYkoIIooy9QZW3GigljQD-oU8cj6QlYUz7wuxo2EO6opRk7TSIDPjz4wwf57SHsYBsCS2GvXciAGG2Puqfta10NzwoQ3ppTpkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db8f77da65.mp4?token=oFCpistVBZ-2VU5ICpUIo8zQC0-QuSHmhMAIb7GzP53WT_6OJfgiKGQ3_d6Zek-bOrkFuiB5WveAFQhL2SAmzYMDu6BUYOxAMLcYSXE_vYQpkxdOBnys6OOt3Xr87ZYA2vEn5zUZiRtQD1WGBcPQkPOXDSvyLqBjL5j8OE80cBfGd6heeuP2diIq9Pj8N29XJN-qsNayVe8162_Qnr4BxFqcq5BH5viIHJeKgLcdWxzaiQ4d6BLfbYkoIIooy9QZW3GigljQD-oU8cj6QlYUz7wuxo2EO6opRk7TSIDPjz4wwf57SHsYBsCS2GvXciAGG2Puqfta10NzwoQ3ppTpkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دستیار ویژۀ وزیر کشور: در صورت تعرض به ایران، باب‌المندب به معادلات جنگ وارد می‌شود
🔹
سرتیپ نامی: ۳ تنگۀ هرمز، مالاکا و باب‌المندب مهم‌ترین چک پوینت‌های استراتژی جهان هستند. تا الان بنا به‌دلایلی فقط از ظرفیت تنگۀ هرمز استفاده کردیم.
🔹
اگر زمانی مجبور شویم از تنگه باب‌المندب استفاده کنیم، قیمت نفت به بالای ۲۰۰ تا ۲۵۰ دلار می‌رسد.
@Farsna</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/farsna/436826" target="_blank">📅 13:23 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436824">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kmL62fDGFzOXJoJouvhXrmKPbPIRXdlVXTx0cyeXIATCRVP_h7oWQs8de__Pe7cm6pTZNHUhdVZO4IhO-0zTMtOvEXPxLmrp_IPZi9suqjUjhRCZDDQOLD5sYhFXWzKV-Naz6aolPvix8KjOh9BHMPNHY97oLYDjgBxVNsypGTp_LLh9idjXCLXFD13Tvey7_DsaGGVLE7KYbi-maJR1Vs1Ot-CPyNdaZVAmu0YVaxG1x9Cs3rjBmDi9vESTpsMnVb1azFKcVNRpaXgluj8-zgddf7Db5s1WATR8q0el-ShGw6dvmFMfitQzf6gXmWJbB31ZvKC3w3reD9p-DUbkCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
تا ساعتی دیگر پیام رهبر انقلاب به‌مناسبت دومین سالگرد شهادت شهید رئیسی و بزرگداشت شهدای خدمت منتشر خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/farsna/436824" target="_blank">📅 13:01 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436823">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ae425b97d.mp4?token=DIjCclr1PsknrZXXfIvmEWaGpyIRmPozhtEpHoB_O77Lw0Mx4YW5QL3zw91qA_0QgppIZz8Gh8vxzUlmgNWg053Gb5nA2Pdih56Buh86AVKnUm-Du1dXCKLogAJ8jJnfazLRffjgHZX85AjQlILIivNvrry8zGwnmyEnbJutHxBm-WYW1aHcnR3W5rmczXvUvdAiRlatfnWutv9_OPpJFyHnADwbHUv7wS111HzWkfnuOlPoPITBFK1Odmj-Yfui1MX2p6Inp5lwNrybvLzDGrpt6BnpcKxFjE9JzePIZhJWwhGhD04NoxXiukyVnDQuBJi2rhdjWonEvOhh_BV8KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ae425b97d.mp4?token=DIjCclr1PsknrZXXfIvmEWaGpyIRmPozhtEpHoB_O77Lw0Mx4YW5QL3zw91qA_0QgppIZz8Gh8vxzUlmgNWg053Gb5nA2Pdih56Buh86AVKnUm-Du1dXCKLogAJ8jJnfazLRffjgHZX85AjQlILIivNvrry8zGwnmyEnbJutHxBm-WYW1aHcnR3W5rmczXvUvdAiRlatfnWutv9_OPpJFyHnADwbHUv7wS111HzWkfnuOlPoPITBFK1Odmj-Yfui1MX2p6Inp5lwNrybvLzDGrpt6BnpcKxFjE9JzePIZhJWwhGhD04NoxXiukyVnDQuBJi2rhdjWonEvOhh_BV8KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تعجب زن اسرائیلی از حماقت سلطنت‌طلبان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/farsna/436823" target="_blank">📅 12:48 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436822">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GjDN2zP-mPdHC9l_ZlyCbBLyt2J0h0UUpLsQWCcb8k41vE5f8bRKpC-sVc9NEr9bI7ob73DXQySLT--EpNoDYFqqJdSMnnKVN754zppm0Ydh7BSwIIJM9MxB0a05-Mpq5Ps8PSSqyPDqm8rOGD7ZtM2yztjEhU0apS--Q5yyohZgmu8OMQXbX1Jg9UF_Y7o2HrWj6cNegTNdqdxyJuuKO8Ql7X4lthDP06tQrGopNupScyOLQzw3wwo1ZQhz-RDO6uF-EKWwkj2DF5D84hnU7gdH_k7mcby94uva5DKbhas7Iu8FZ052LVACgNvDdMNXorZAskH3zdjtYen5Etuabw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ علنی پرسپولیس سر سهیمه آسیایی
🔹
‼️
شایعات از احتمال لغو ادامه لیگ برتر و معرفی مستقیم نمایندگان ایران به آسیا حکایت دارد. باشگاه پرسپولیس با این اقدام مخالفت کرده و آن را غیرمنصفانه و غیرفوتبالی خوانده است.
🎙
یکی از مسئولان ارشد باشگاه پرسپولیس گفت:
🗣
ما…</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/farsna/436822" target="_blank">📅 12:45 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436821">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P1vqbOhE38yQq2PtEurDW_lGto9v8wvBCXgI9pc3ec4Gnr6LfSfbwc8IhcM24Pk6ES5kW9T92tmLe2FnhCr6KM4kMXEclv3rM80DWMpIqJuJiphirgdys1yRhGiMASOVSB8iwIThkRY03UBcnZOrobj3c7V_RxCEHVbV0quJE4Ctwv4NLmNGy-OGMFFFENLQ8apC6KA_5PCE2UyyOHmWW0rcCatzKmlHxiXV3PyfGLK9gtC8VjxsronSEuO4wShr5CXiaQ4N3-djXbBakrfSXV8yRJCN3KFqWRoGjee3iWorK7Y-0IesO0akod4iFt7gtHufVOI01J9VgppD_hVfZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
«درخشش روابط عمومی شرکت صنعت فولاد شادگان در جشنواره سلام خوزستان با کسب ۲ عنوان برگزیده»
🔹
روابط عمومی شرکت صنعت فولاد شادگان
در ششمین جشنواره «سلام خوزستان» با کسب ۲ عنوان برگزیده خوش درخشید.
🔹
این جشنواره با حضور ۷۰ روابط عمومی از ادارات، سازمان‌ها و شرکت‌های استان خوزستان برگزار شد و آثار ارسالی در ۱۲ بخش تخصصی مورد ارزیابی هیئت داوران قرار گرفت.
🔹
در این رویداد، روابط عمومی شرکت صنعت فولاد شادگان در بخش‌های «تولید موسیقی و ترانه‌های حماسی» و «هوش مصنوعی» موفق به کسب عنوان برگزیده شد.
🔹
آیین اختتامیه ششمین جشنواره «سلام خوزستان» روز سه‌شنبه ۲۹ اردیبهشت‌ماه ۱۴۰۵ در اهواز برگزار شد و در پایان از برگزیدگان این دوره با اهدای تندیس، لوح تقدیر و جوایز تجلیل به عمل آمد.</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/farsna/436821" target="_blank">📅 12:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436820">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PsrxsZvJZ-zRjc7jx8gq1yYRCbToIcFvLql5yA-U2h7NOYQqp5Mcjf3gKJZA2kf1spj6-H9ERNSg0jlRMnG6i9LgxAXWS7kER8iVuj6SBhNTiG1o4MQrzSXSUhXKn4sNAtiFSX4AV0FuLlf4oPeD_x45yyN6yTs3JQ3OjH6BSPcsYm_Bo3_6jp4KYRnGwmbA_atNqPsMYywI1s2fkHTwZTDSZ2fiDkuL50ky89AC0AFqLT-92Xk8OSRSm35sr2QEXcu77_WUhnnZJ7G0R-tfni_QXdaWXdItbomR0VH5FTabgbfz53n7YU5FTdD7GEbhtBKwMeXpG4028ADg1LPM3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">*
🌐
سامانه فرارفاه بانک رفاه کارگران به‌روزرسانی شد*
🔹️
با هدف توسعه بانکداری الکترونیک و به منظور ارائه خدمات مطلوب و متمایز به مشتریان، سامانه "فرارفاه" (مبتنی بر سیستم‌عامل‌های Android و iOS) بانک رفاه کارگران به‌روزرسانی شد.
🔹️
"درخواست کارت رفاهی متصل به اوراق گام"، "خرید بسته اینترنت اعتباری یا دائمی"، "فعال‌سازی حساب کاربری" و... از جمله قابلیت‌های نگارش 1.5.6 سامانه فرارفاه مبتنی بر سیستم عامل Android و نگارش 1.17.0 مبتنی بر سیستم عامل iOS است.
🔹️
سامانه فرارفاه از طریق پورتال اطلاع‌رسانی بانک رفاه کارگران (
https://www.refah-bank.ir/fararefah
) در دسترس قرار دارد.
@bankrefahkargaran
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/farsna/436820" target="_blank">📅 12:39 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436819">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/farsna/436819" target="_blank">📅 12:39 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436818">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62fe7d131d.mp4?token=u4shJ7VfCqCFk48-SBbpzr6Xjruo9cqiix5nAD2qwTsE93Ltwl1SvqYRwNDvffR8jO6DQbT0dJ-ojRp1OrHFXoqnvz1220DvIwZPfprgW5H7IuAaG6MYNm9qIzZkqxzhXPtli9DJCPHPZsa0S_sRWj6EI7zRxuw8u1q8yKlRAjMMX435rSu2j3hJYOguBkmonziC4wrCiJt2kkmDzMAq0abk0sNRDLDo4LEEZIC4oy7r-4qCVkLr_uLXkhXiqx4M3Tg_sgbd8_jKq5h-q3I1N0fZxtWIUWpWcLOWN5PBHF0Iw3wQlbCpoQf-DtEQoAk43F1AFmCZoMo4Qo9WUM4u3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62fe7d131d.mp4?token=u4shJ7VfCqCFk48-SBbpzr6Xjruo9cqiix5nAD2qwTsE93Ltwl1SvqYRwNDvffR8jO6DQbT0dJ-ojRp1OrHFXoqnvz1220DvIwZPfprgW5H7IuAaG6MYNm9qIzZkqxzhXPtli9DJCPHPZsa0S_sRWj6EI7zRxuw8u1q8yKlRAjMMX435rSu2j3hJYOguBkmonziC4wrCiJt2kkmDzMAq0abk0sNRDLDo4LEEZIC4oy7r-4qCVkLr_uLXkhXiqx4M3Tg_sgbd8_jKq5h-q3I1N0fZxtWIUWpWcLOWN5PBHF0Iw3wQlbCpoQf-DtEQoAk43F1AFmCZoMo4Qo9WUM4u3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تحلیل‌گر مسائل ژئوپلیتیک: بازگشایی نظامی تنگهٔ هرمز غیرممکن است
🔹
کمپف: نمی‌توان تنگه هرمز را با توسل به زور بازگشایی کرد؛ همه دیگر توهم تغییر رژیم، سرنگونی حکومت و امثال آن را کنار گذاشته‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/farsna/436818" target="_blank">📅 12:38 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436817">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e50ab77ba3.mp4?token=psnr1Dn2z6EuqzYL82oloFm8W2BUheo2LxZpE6cPdZ--I1s4JYbBTtKfoA2DqXuQ7rPuJgieBuz6AYmoN3g9skPaRUbTIww-3J8rMEXPqvK5QMRWBdetw6Ls_9SlVnK7rUanfxYQaD7PvyUYUMeSTFC02Quh28C0v5VWzVCkFAri5WLfahP494672zYkzrVvZxwuR376aIz0UF2vSsR7_6d9gcoyHPSdstRQD-_m6sPPFEnFp8ml8GelTf1tVVz7kzex3vBt259_GC8-xBfwV6EqKYBpFmX50vOVODweDizm8QlyfTIYG8ARuPSP7op222p8IMJE2jnzNzEDzKtNaXRhwXTCSErPFpSNd_U-Fa7zo2BmcC2AfmMPBqOfb7ihjlrHZVmlHhwXPxpGd6wIo-6vQBDbvgzQKtJQVmhInRKzguF1woPcy7bdbi2CYFET06jIAWAmSOUnnEXi3kByB119edzkB2U3x8c417vfHM46DwBfdLU_xbdHdoMSgsXm2rLHkp3IZ6gVY-wyf6dmaGFmtNvRmmcsH-Z00TyrLyIgoU_y606QdyJOBrIUn0lATkKensWSXtAc6AgRQy83rYSKzECup-UF2p8TZHMW8m1rzTVzb011yDtqCRZwVv91n-d2-S-seDrUkJMdbrre4MPSfxnisssLZG3Ocdwxirs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e50ab77ba3.mp4?token=psnr1Dn2z6EuqzYL82oloFm8W2BUheo2LxZpE6cPdZ--I1s4JYbBTtKfoA2DqXuQ7rPuJgieBuz6AYmoN3g9skPaRUbTIww-3J8rMEXPqvK5QMRWBdetw6Ls_9SlVnK7rUanfxYQaD7PvyUYUMeSTFC02Quh28C0v5VWzVCkFAri5WLfahP494672zYkzrVvZxwuR376aIz0UF2vSsR7_6d9gcoyHPSdstRQD-_m6sPPFEnFp8ml8GelTf1tVVz7kzex3vBt259_GC8-xBfwV6EqKYBpFmX50vOVODweDizm8QlyfTIYG8ARuPSP7op222p8IMJE2jnzNzEDzKtNaXRhwXTCSErPFpSNd_U-Fa7zo2BmcC2AfmMPBqOfb7ihjlrHZVmlHhwXPxpGd6wIo-6vQBDbvgzQKtJQVmhInRKzguF1woPcy7bdbi2CYFET06jIAWAmSOUnnEXi3kByB119edzkB2U3x8c417vfHM46DwBfdLU_xbdHdoMSgsXm2rLHkp3IZ6gVY-wyf6dmaGFmtNvRmmcsH-Z00TyrLyIgoU_y606QdyJOBrIUn0lATkKensWSXtAc6AgRQy83rYSKzECup-UF2p8TZHMW8m1rzTVzb011yDtqCRZwVv91n-d2-S-seDrUkJMdbrre4MPSfxnisssLZG3Ocdwxirs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرار فرمانده سنتکام از پاسخگویی دربارهٔ جنایت مدرسهٔ میناب
🔹
خبرنگار شبکهٔ اسکای‎نیوز خطاب به فرمانده سنتکام: تا کی می‌خواهید پشت این ادعا که «تحقیقات ادامه دارد» پنهان شوید؟
🔹
تیمی از شبکهٔ اسکای‌نیوز همین الان در میناب هستند. آنچه آنجا رخ داد را دیده‌اند. هیچ مدرکی دال بر وجود پایگاه موشکی در آنجا وجود ندارد.
🔹
تا کی میخواهید پشت این ادعا که تحقیقات در جریان است قایم شوید؟ حداقل بگویید تحقیقات چه زمانی پایان خواهد یافت؟
🔹
فرمانده سنتکام به‌جای پاسخگویی مسیر حرکت خود را تغییر داد و تلاش کرد با کمک محافظانش از دست خبرنگار فرار کند!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/farsna/436817" target="_blank">📅 12:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436816">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Da05Mgi9PDMbg6QlgEh5RujgZ2Ges4n11dXmLhyJq-N4YFzN5KhWCF_K0H-H9BdOyZgiP5ophdClZRvBpnwWaDAN-AnHThLVGNq5qjxPBSeREgSn-B_0PdHuOgJHmxxRgYOUC4sOBIClnTe_rrc9XHbDcxQKWqOMhVD5H4UVOLjz1wyY2RV82IQarxjBelvvZh9i7WFOaRQBGc7QZCcZP6T556BaN23QQ_nziG7jt5q6xPTpBulKG9A9Nj7Iw4xor-oDuXoashUE7yhAWJrBMsMwx_xV9uSz4TfqHRcIW3E-iwOpDfTOkKRggcjkUweR1FjhdA16iCZYEn7GOOchNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تداوم بازداشت ۴۱ عالم شیعی در زندان‌های بحرین
🔹
جمعیت وفاق ملی اسلامی بحرین: از زمان قطع ارتباط با ۴۱ عالم شیعی بازداشت‌شده بیش از ۷۲ ساعت می‌گذرد؛ امری که نشانگر ادامه جنگ سیستماتیک علیه شیعیان در بحرین است.
🔹
رژیم بحرین همچنین ۱۰ شهروند را در پرونده‌های…</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/farsna/436816" target="_blank">📅 12:08 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436815">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس نوجوان‌</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0486d5e9bd.mp4?token=scblDeOmmDFKYLaESSU8fh6HvGomkR4ZZyvv_7f8zJvJ_w5uTZ-B90mvK3tmv_D75vlgJariWBkdMvFzvh-EuBsV494bYFFm-bErJXCbqbl8DZZsAPZHoevZ4Gl3dfyzDhQ9WBlWMY0bNpFl1EcpkZi6N9L5q5tdQQ2Pnl_FDL-Y335JtelVHMkfimb-SrWPfgnp84a56jQ8273wLZ-vJAlpZjVxT8SiXu2FCdxNN1KlxVRJQdoDBgbFM5CwEwFke9sZKaIZIrgqhnqq2aGIr6jpQgGdNOvhakLbsw1GEiFtpkFI8i69zWgJsNhXxWPaC2p8OctV0GbaHBbtsb_nBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0486d5e9bd.mp4?token=scblDeOmmDFKYLaESSU8fh6HvGomkR4ZZyvv_7f8zJvJ_w5uTZ-B90mvK3tmv_D75vlgJariWBkdMvFzvh-EuBsV494bYFFm-bErJXCbqbl8DZZsAPZHoevZ4Gl3dfyzDhQ9WBlWMY0bNpFl1EcpkZi6N9L5q5tdQQ2Pnl_FDL-Y335JtelVHMkfimb-SrWPfgnp84a56jQ8273wLZ-vJAlpZjVxT8SiXu2FCdxNN1KlxVRJQdoDBgbFM5CwEwFke9sZKaIZIrgqhnqq2aGIr6jpQgGdNOvhakLbsw1GEiFtpkFI8i69zWgJsNhXxWPaC2p8OctV0GbaHBbtsb_nBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اگر دوستمون تو ایام جنگ احساس ناامیدی و شکست داشت وظیفه ما چیه؟
به نظر شما چرا بعضی ها نمی‌تونن واقعیت صحنه جنگ رو ببینند؟
جوابش رو اینجا بخونید
.
@Fars_Nojavan</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/farsna/436815" target="_blank">📅 11:57 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436814">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XeQXVz1vwaWydDDZ3tf-HwVH7t13FF903OKbwEoZF0PDXR6KxumeOXy6yjCTtiJOuBDeaa2GSmfbvTrXVZ3I77f6yw2UfzpDLLL46IMhu45CLj-y12Xlk6Tf3z0EFSpJpBsfD0HE-PqVNfYoxKK19S5mYhco09xujRqk0a9cL7c35SV9sd3LkD0bDjijy8OFqbzF9L_I0Fk_hIaFQWLi7eREYjzC4xXj0VjFxPz-KOgY6BbsxwI0nQ04s_teU0OYSaJEXfOWKFC53xEGCXRRSZPkOVfWRPowxBlB9Wq9bKlhQJIynx2TAbG10WKzmZVs0lprf2FIXyUdaRiBj4vQIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصوبهٔ جدید قیمت چای اعلام شد
🔹
براساس مصوبهٔ جدید کارگروه تنظیم بازار کالاهای کشاورزی، تشکل‌های مرتبط موظف شدند با هماهنگی سازمان حمایت، قیمت انواع چای را به‌صورت دوره‌ای تعیین و اعلام کنند؛ دولت همچنین بانک مرکزی و وزارتخانه‌های صمت و راه را مکلف به کنترل بازار چای کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/farsna/436814" target="_blank">📅 11:52 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436813">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uiwIlKZqCCa6Ku0qdb8Q3ZcVKb98RLLEGa5834EhvtUIkc9hZUy4-J-Pgv7EjtUgFlsmpZGzEQyU8CPfOHt3slz-ybVEUOBNsQGZzRLNzlEwvLBTScGcgM1QC3fgWvMUcHgGQ-Zb6nnpAX09VoveSPlIIH4Ygh3qyeWGjqUsltoy4nhhYQqR4R2Sz3LIuknUz-_FppRiOExema1utTXTQuH5xmqrAItz0dS1O7-X-eiQHeeKZ_0RK_Ap8TO8YCBXkszfKcP92QNaVbzcbVMx_JpnHVfj1wcMmn6EX1umFbbmcL8zPIMGVeEt6-CyEzZUObLNP9P_vHgQEN_0PPa42A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شی و پوتین حملات آمریکا و اسرائیل به ایران را محکوم کردند
🔹
رئیس‌جمهور روسیه ولادیمیر پوتین و همتای چینی شی جین‌پینگ امروز در بیانیه‌ای مشترک حملات نظامی آمریکا و اسرائیل به ایران را محکوم کردند.
🔹
در این بیانیه آمده است «طرفین اتفاق نظر دارند که حملات نظامی آمریکا و اسرائیل به ایران، ناقض حقوق بین‌الملل و اصول اساسی روابط بین‌الملل است و به‌طور جدی ثبات در خاورمیانه را تضعیف می‌کنند».
🔹
دو طرف در بیانیه مذکور، بر ضرورت بازگشت هرچه سریع‌تر طرف‌های درگیر به گفت‌وگو و مذاکرات با هدف جلوگیری از گسترش دامنه درگیری، تأکید کردند.
🔹
آنها همچنین از جامعه بین‌المللی خواستند موضعی عینی و بی‌طرفانه اتخاذ کند، به کاهش تنش‌ها در منطقه غرب آسیا کمک کند و به‌طور مشترک از اصول بنیادی روابط بین‌الملل حفاظت کند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/farsna/436813" target="_blank">📅 11:46 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436812">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CjLL6LocSXjjw8ujAxiQPEt0pBqQnOI1ZXTEJ2KihcPj-cHFVWbBDppJyxdRC0ThWtkT4krOjSxj9U_sNcidHxETXqLPEHcGrcPVK_0bS0a8XC3tEvbI9KtTgL4Q9kOzAOHGcACIBBk7L_Vmt2pAEXgDf1YT6tkDtG82gudr6g6QThcEhzEGl7cE_BAsT7ciqwkEXiqYm73yzL-8wk-VQyVMK-g5B7bwbEGNrRBvWq9jiepx9JF1aVQfIdilBY0JY1TAwzwL8WJ4OtYBrT6tWqXdxYq-pYtcKLWI0vUgrcB-fp77k5uHFF4A06ARij9aVAgijtS4oKBDoMYMChY8WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خشخاش به مزارع ایران برمی‌گردد؟
🔹
شهریاری، عضو کمیسیون امنیت‌ ملی مجلس از بازگشت دوبارۀ خشخاش به مزارع خبر داده و گفته «خشخاش ارزآوری خوبی دارد».
🔹
سالانه ۴۰۰ تن تریاک برای تولید دارو‌های ضروری نیاز است که به ارزش ۷۲ همت و عمدتا از کشور همسایه وارد می‌شود.…</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/farsna/436812" target="_blank">📅 11:41 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436811">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LkrAxqZoym1ucVtrjzTb_knN6avyxAUkrMrOTEgHVoe5sDyvNChvJktKxNg54_bozjrQV9zb34bgKBUIVVYYrLjZ0G9MToGCtvPqRHlwPRMG2zcY7_IHx5JBQ_5x4zxSJl0o433qv0BxW6qLaSkmOtibBK4KFRRJEyH5ntP5U-cOzFeJvT0shlIdGxBwhSbQ6sI2Yc9Tm--cbySX2XnA0wsKg_dH818uQLe8X81Kq_-Hkpd_nDpnHbDhbN4NLrpOad0clC1UlI18yNxliPpE2KoS2Fcd6_J5_4xGhMlhL6LYcLCKTtlEb-slvFI6SiytITg2_Tu9F8nnszP47KMy1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس اپوزیسیون اسرائیل: روند انحلال کنست را آغاز می‌کنیم
🔹
یائیر لاپید در شبکه ایکس نوشت: «با همکاری سایر جناح‌های اپوزیسیون، اخیراً تمام لوایح پیشنهادی را از دستورکار کنست (پارلمان رژیم اشغالگر) خارج کرده‌ایم. در غیاب اکثریت، ائتلاف قادر به تصویب حتی قوانین…</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/farsna/436811" target="_blank">📅 11:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436810">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DoYSskMuQeo3G3AAwReidsjY8qrFX8MLrkeqAoiLN12eYY5WbFGNPzW-OkILLESm2_cKXAxS_bgifVUMmZW-td0qiBfb5le9g8ujM8NvLu89hu9SWjXg2ZYoZCIRof9Ux9TB8PNZ4mDnxSuFx3RgVMSV8xrQYGYjNe5Tedm3IGY1hmcYN8lzI1ZpIPzJFP5DEbiSsUbXrjFRMdwrmakdZtqOgT5djUG6DmKV1dPrZ79roAMvg95A31s78KlYqkfWRRgl2VZqlBaC0SM59Rx9UeqRqjqrLoVRjaQGtAmMN4jodUgkXRvMZBcufJB6VsGvVj3aFaOIAgAVa99v8GcB3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده قرارگاه مرکزی خاتم‌الانبیا: شهید رئیسی با روحیه‌ای خستگی‌ناپذیر، میدان خدمت را بر هر مصلحت شخصی ترجیح می‌داد
🔹
پیام سرلشکر خلبان علی عبداللهی به‌مناسبت سالروز شهادت آیت‌الله سید ابراهیم رئیسی: آنان دل در گرو مردم داشتند؛ ساده زیستند، بی‌ادعا کوشیدند…</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/farsna/436810" target="_blank">📅 11:27 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436809">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
حزب‌الله: تجمع نظامیان و خودروهای رژیم صهیونیستی در شهرهای دبل و رشاف را با حملات موشکی هدف قرار دادیم.
@Farsna</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/farsna/436809" target="_blank">📅 11:25 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436808">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromانتشارات فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTJcqX7o7EszH-4gkJRA-FV0-ZuCV59yjUldkGx125xzr4VqsnFlrV0BOZB3VzmyRWA5f2lz7lnxPBVIf43NabgxiOD7Yn-ctR7nr5_5haVe_wPfFz0hS7O8MtT-gqN7ZxjYk1Ce5i8aqiNcX5Wk5qW7QfLiFui1iOhHxNNbE9zgQgxY-KGaqyC9HdHyaue0wJTw3IwEOYC5gBwCHkVQ85H51Ejk-UkxoAd7P7ZTgQs8XX0iLHkGQkR1BL2wDpjLQ0PAEfx7SMZsOaunvWjzou-x_u19aV5HsPKTRwo0D34srcS4yvBKiDeW0kWXUW_cw5iYJhpoNsvXv7uF3yFdLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📚
۱۱ بسته تخفیفی انتشارات فارس؛ فرصتی استثنایی برای خرید کتاب‌های رسانه‌ای
🎯
انتشارات خبرگزاری فارس در هفتمین نمایشگاه مجازی کتاب تهران، با
۱۱ بسته موضوع‌محور
و تخفیف ویژه مهمان شماست.
📖
این بسته‌ها شامل حوزه‌های تخصصی و عمومی:
✔️
آموزش رسانه | روایت‌گری | خبرنویسی
✔️
خانواده و رسانه | برنامه‌سازی | تدوین
✔️
دولت هوشمند
✔️
جریان‌سازی در آمریکا و ایران
✔️
صهیونیسم‌شناسی
✔️
علوم شناختی
✔️
تاریخ انقلاب
🎁
مناسب برای دانشجویان، اساتید، فعالان رسانه و همه علاقه‌مندان به کتاب
🛍
با قیمتی مقرون‌به‌صرفه، کتاب‌های موردنظرتان را راحت‌تر تهیه کنید.
🛒
نحوه خرید:
🔗
لینک خریدآنلاین از سایت رسمی نمایشگاه
https://book.icfi.ir
📌
روش‌های خریدکتاب از انتشارات فارس:
🔹
ارسال پیامک عنوان کتاب به شماره ۵۰۰۰۱۶۷۶
🔹
تماس با ۶۶۹۷۳۹۹۶ و ۶۶۹۷۳۹۷۴
🔹
مراجعه به سایت
انتشارات خبرگزاری فارس
🔹
حضوری: خیابان انقلاب، روبروی دانشگاه تهران
✅
انتشارات فارس مرکز جامع کتب رسانه
#انتشارات_فارس
#نمایشگاه_مجازی_کتاب
#بسته_تخفیفی
#کتاب_رسانه</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/farsna/436808" target="_blank">📅 11:20 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436806">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
سپاه پاسداران: با تکرار تجاوز دشمن، جنگ را فرامنطقه‌ای می‌کنیم
🔹
بیانیه سپاه پاسداران: دشمن آمریکایی‌صهیونی که از شکست‌های بزرگ و راهبردی مکرر از انقلاب اسلامی درس نگرفته و بار دیگر زبان به تهدید گشوده بداند، اگرچه آنها با تمام توانایی‌های دو ارتش که پرهزینه‌ترین ارتش‌های جهان هستند به ما حمله کردند اما ما همهٔ ظرفیت‌های انقلاب اسلامی را علیه آنان وارد عمل نکردیم.
🔹
اما اینک اگر تجاوز به ایران تکرار شود جنگ منطقه‌ای که وعده داده شده بود، این‌بار به فراتر از منطقه کشیده خواهد شد و ضربات کوبندهٔ ما در جاهایی که تصور آن را ندارید شما را به خاک سیاه خواهد نشاند.
🔹
ما مرد جنگیم و قدرت ما را در میدان نبرد خواهید دید و نه در بیانیه‌های توخالی و صفحات مجازی.
@Farsna</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/farsna/436806" target="_blank">📅 10:58 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436805">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">افزایش وام ازدواج و فرزندآوری در بودجۀ ۱۴۰۵
🔹
سخنگوی کمیسیون تلفیق بودجه از افزایش ۱۰۰ همتی سقف تسهیلات ازدواج و فرزندآوری خبر داد.
🔹
بر این اساس سقف این تسهیلات از ۲۷۰ همت به ۳۷۰ همت در سال ۱۴۰۵ می‌رسد.
🔹
هدف این افزایش، جمع‌آوری صف حدود یک میلیون متقاضی…</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/farsna/436805" target="_blank">📅 10:55 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436804">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R8vGUTZOJdEdIPTiHlXHozvQ1C0OmKBrtQAeyMRk1mXZ2mo4FNUrIaKkeBQmjrPcq7xE8WcWk1Dd0bomrQ9dYra1FOwRzk6TGj850M0b9JuBc-uhWTVD2Ls2YzjWJCgUPfB-ZaEzLnBrjId424hmHy6HsfoixDuU9Q1rDX2D-ghXpXKrc7YEVqod1Dv5H5e6sWgVmwq2SUaa-_z2d_9I06FlnKkGlLTqdpkENc8IGvyYRXUhLefPy5qSVYNDplnDo4an0hw8D3m0Nls9502eK9spdcgfzrpXFbLzkf3tA5phYCwXv93jx52b0ubUwGwtgOhLLHH-LJcGlwgtee2lpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
همکاری همراه اول و پژوهشگاه زلزله برای توسعه هشدار سریع
🔹
همراه اول و پژوهشگاه بین‌المللی زلزله‌شناسی و مهندسی زلزله با هدف تقویت زیرساخت‌های ارتباطی در شرایط بحران و توسعه سامانه هشدار سریع زلزله، تفاهم‌نامه همکاری امضا کردند.
🔹
در قالب این همکاری، از زیرساخت‌های ارتباطی همراه اول برای انتقال داده‌های شبکه‌های لرزه‌نگاری استفاده می‌شود و پژوهش‌های مشترکی نیز در حوزه هوش مصنوعی برای بهینه‌سازی زمان صدور هشدار انجام خواهد شد.
http://mci.ir/-F4RHS6
@mcinews</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/farsna/436804" target="_blank">📅 10:54 · 30 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
