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
<img src="https://cdn4.telesco.pe/file/NaYTvHoa1w6nI-dbIMTPVjIzvNm5vDMpCuDMz_WRBW68T39iSlpjl2a3ayDPAHH5ORIKwvxBitZFEDa75kZkItA6fNfZmN0PFptp5s0FC36l-nlwbUf8TaWbUuazLq3k2zLeqrqQlEY4aBAV4hlq8qYwA_GTB27vcisPR4nzPTJtVPiKuZq80Mzv3q-8gLj4gCVRr6yI1UDRDRBnIs5ODs5RdKm44GKAtUgYepsCbhi1yQh_e1q6iY3MEyHlEL9oblcYApEWamZH19YQVYqP6cdtxKirnYQLNwlc63dSa_dgMjDu8lKot96VoI0tjae610L-HybiZiz_yfmpS7ZLRg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 938K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-05 22:44:31</div>
<hr>

<div class="tg-post" id="msg-130394">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
وزیر خزانه داری آمریکا: ما مجبور بودیم به ایران حمله کنیم، چون آنها دو هفته با داشتن سلاح هسته‌ای فاصله داشتند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/alonews/130394" target="_blank">📅 22:41 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130393">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
حزب‌الله: چارچوب توافقی که در واشنگتن به امضا رسیده، از دیدگاه مقاومت مردود است و هیچگونه الزام یا تعهدی برای مقاومت ایجاد نمیکند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/130393" target="_blank">📅 22:28 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130392">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/124d0585ad.mp4?token=JDalwuAMrEmCslPVofRg0IN6SEuU0XOtBeGEuovMAKipozKNneDqO_agv2PfnyJ1qsZaA7mXerZGn2DV3gn76R0UkJyLt_9nJd1txPGaVYwLTUJhT6HJEzaO5p1QXDzEOrmdHh44eYV39FHsNsH_xQiJEyDlW62R1XXfYOd71fJieoNiLV4ejwfnUVmLq_yL9-8Nml7DAdDEKy9T_7VIJEzgnKo1VpHVGsVtxLBbn7OJMr6U7I8eBtr-xAol9ShczdMdp5IBGai2Var8hTdfn91WhoqHj9lHx9iWFS-gfvt2FElv48A28Zj_zkEqp8ESxLQm0TgoHF419ejo9Jel6oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/124d0585ad.mp4?token=JDalwuAMrEmCslPVofRg0IN6SEuU0XOtBeGEuovMAKipozKNneDqO_agv2PfnyJ1qsZaA7mXerZGn2DV3gn76R0UkJyLt_9nJd1txPGaVYwLTUJhT6HJEzaO5p1QXDzEOrmdHh44eYV39FHsNsH_xQiJEyDlW62R1XXfYOd71fJieoNiLV4ejwfnUVmLq_yL9-8Nml7DAdDEKy9T_7VIJEzgnKo1VpHVGsVtxLBbn7OJMr6U7I8eBtr-xAol9ShczdMdp5IBGai2Var8hTdfn91WhoqHj9lHx9iWFS-gfvt2FElv48A28Zj_zkEqp8ESxLQm0TgoHF419ejo9Jel6oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ توافق اوباما با تهران را «JCPOC» می خواند.
🔴
پ.ن:
Joint Comprehensive Plan of Action
است که در فارسی به آن «برنامه جامع اقدام مشترک» یا همان توافق هسته‌ای ایران (برجام) می‌گویند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/130392" target="_blank">📅 22:26 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130391">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
ترامپ: کشتن سلیمانی یکی از بزرگترین اتفاقاتی بود که تابه‌حال در خاورمیانه رخ داده است.
🔴
من فکر می‌کنم خمینی (منظورش خامنه‌ای‌ست) و دیگران در ایران از اینکه من سلیمانی را کشته بودم خوشحال بودند.
چون آنها هم از او می‌ترسیدند.
🔴
او یک ژنرال درخشان بود. او مردی بسیار بیمار از نظر روانی بود.
🔴
کشتن سلیمانی یکی از بزرگترین اتفاقاتی بود که در خاورمیانه رخ داد. مردم گفته‌اند که بزرگترین اتفاقی است که در ۱۰۰ سال گذشته رخ داده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/130391" target="_blank">📅 22:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130390">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9bda5bb20.mp4?token=c3TPtRcy9eEj5Ra8IbyKKEvUxOoyDLZUC6Ixi7-cQC9OC68wMLJWTMHtAOkpJuM8KQekBaHoHiDVDj5HfVredhvjO8939bt627gqCY1b1dBfZxopJKeAiyfDzoKmukYlFfW5GWKZHiCsYY5fp4zrTgpyWDsBHxNeUDxnLKCSZ4s55mU7f4pla1BOxAVV2CDik3XuvaPAaHjeVDdIQ5BhwUGMDma4lmV35jj6WJqaLsrnmsAi-eYAvlktdDPfDarLs-dckgEzUK2HZSNPxifwjYU6PREiok1kaTl8OkGWq1uoy8VwWkMflWPd1Db8_gPtcKReAPkhxW2eSgmyIC-CH20Q3K0okWcz_NfDzzsg2jPoSkLLKfsgM6UuLeYPL3uSUFC2dXOrYRgpBfjmbO3dNPRLCMvnkYFis4ce61qgNRZV-TjuPNJP4UhC-CR6426bkxm--nE90IavKJEaMSfeNeSEoruabN-iRJmq0iEOHAElQdGgiqS67wKpl5VjQgd8SOSDWpmwHZYH1QeEhDipKMftvsJlzN92o-4G-cAdvzBlja0h60cGZXSWRR7jy7chr1gdo7DvvebwGWtW-eNX7eDpyI3pcigkPUUceAtSMAGn8HABEOhiYiPAZcpgI5SLqT_ZSXQe1g4KdWHFtUbqiNC3hzLtfJN6yvo0g7dD4dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9bda5bb20.mp4?token=c3TPtRcy9eEj5Ra8IbyKKEvUxOoyDLZUC6Ixi7-cQC9OC68wMLJWTMHtAOkpJuM8KQekBaHoHiDVDj5HfVredhvjO8939bt627gqCY1b1dBfZxopJKeAiyfDzoKmukYlFfW5GWKZHiCsYY5fp4zrTgpyWDsBHxNeUDxnLKCSZ4s55mU7f4pla1BOxAVV2CDik3XuvaPAaHjeVDdIQ5BhwUGMDma4lmV35jj6WJqaLsrnmsAi-eYAvlktdDPfDarLs-dckgEzUK2HZSNPxifwjYU6PREiok1kaTl8OkGWq1uoy8VwWkMflWPd1Db8_gPtcKReAPkhxW2eSgmyIC-CH20Q3K0okWcz_NfDzzsg2jPoSkLLKfsgM6UuLeYPL3uSUFC2dXOrYRgpBfjmbO3dNPRLCMvnkYFis4ce61qgNRZV-TjuPNJP4UhC-CR6426bkxm--nE90IavKJEaMSfeNeSEoruabN-iRJmq0iEOHAElQdGgiqS67wKpl5VjQgd8SOSDWpmwHZYH1QeEhDipKMftvsJlzN92o-4G-cAdvzBlja0h60cGZXSWRR7jy7chr1gdo7DvvebwGWtW-eNX7eDpyI3pcigkPUUceAtSMAGn8HABEOhiYiPAZcpgI5SLqT_ZSXQe1g4KdWHFtUbqiNC3hzLtfJN6yvo0g7dD4dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ:
اخبار فیک/جعلی گفتند که ایران امروز بسیار قوی‌تر از ۴ ماه پیش است.
🔴
آن‌ها تشنه‌ی انجام یک توافق هستند.
آن‌ها به ما بسیار زیادی می‌دهند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/130390" target="_blank">📅 22:13 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130389">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e369539a42.mp4?token=kDq-G5CdcqC-YWMU1Wkx9bXodAsKnkw71R-I-jYPRuhH3l4-bBHoS07TpK2jV2wk_2jB_EEV41UlqaVBQRzDaBrUvlafT99LYtqobSZbdPgLb5L05cCoEOHnPys2T9DpiUBfAwNi5pZfhcx2FZ6KxcsqjRRAOBQdVwyQG_FwFICIehqwYjAukdvqw60RSxDcpFuokWw4lkkM-jGa8Ty3aMNQpUsb4rYnJn6mjjNmfDn9K4RVWr8GLIFVybOBYjJ179ocBTxncYqjtqcx4tk-QmwH-7HwQz_SplgVjL7Hwilbcv2uzEYmFksK__N5GXt_YoA9CGlTS0EomBC0ROi-Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e369539a42.mp4?token=kDq-G5CdcqC-YWMU1Wkx9bXodAsKnkw71R-I-jYPRuhH3l4-bBHoS07TpK2jV2wk_2jB_EEV41UlqaVBQRzDaBrUvlafT99LYtqobSZbdPgLb5L05cCoEOHnPys2T9DpiUBfAwNi5pZfhcx2FZ6KxcsqjRRAOBQdVwyQG_FwFICIehqwYjAukdvqw60RSxDcpFuokWw4lkkM-jGa8Ty3aMNQpUsb4rYnJn6mjjNmfDn9K4RVWr8GLIFVybOBYjJ179ocBTxncYqjtqcx4tk-QmwH-7HwQz_SplgVjL7Hwilbcv2uzEYmFksK__N5GXt_YoA9CGlTS0EomBC0ROi-Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره رهبری در جمهوری اسلامی ایران:
دیگر کسی نمی‌خواهد رهبر ایران باشد. گفتند: «چه کسی دوست دارد رئیس‌ باشد؟» و همه گفتند: «نه، ممنون.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/130389" target="_blank">📅 22:11 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130388">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
ترامپ درباره شهردار نیویورک:
شهردار ممدانی که به نظر آدم خوبی می‌آید، گفت که قصد دارد مطمئن شود مردم افزایش اجاره‌بها را تجربه نمی‌کنند، حتی اگر هزینه انرژی افزایش یافته باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/130388" target="_blank">📅 21:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130387">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a205f15b6.mp4?token=Y7j5zWxVceNlI_0aJHmsK1gK6OL2KiY0DHH3nPrrOS-YZexJIlwBMyXiYJoKqj16br2dYqKNLueBcO5y0GIxJa1zsvcCuruRaxxZqgTM92dmf9j0fR09TvADf9JcJIJ3vmm1dZCa7lUHJoj90BIo6PQMke2xx_8RLK1vrI8Msy5isA_cINmimi_suGXRM0VYhetJaXxNvnyEeHsg8hLop6dF8qkSyPc-ak_EpXBaBRJsRjcdJFvky4K3LkKKbb0AGYJDB_p1F_bEyYOYfJ_LhQ6o3Rof54WD6ye1woSfMuM0tvwBnBAl4zFRUMwoOtuSnQPx45SJFzKkpdHQ3yRS-LggHxWj6eCharL-RLc6Beu1ZuQcbqlvHTttP11K0FB8P9FpGcgRudsWCxCDPgZboioJ6g4kI5SkwOGc2ywy6lBWSkz2o8XuqSS7A_gMm7UIiAlbiOt_I6dbSX8MeXjjrAie2zT1W2aWNiobaLv1ZGq234oCi_jHcso-AxXW_sIgmzyRKuQQpyx6mMgdJUOeb-yUNd7C_qgJJ4XNq73GX4A1PkoFyg3fOpaFIm45arkESe14MKNBcNZDbxAMebIuHL3rFzYsUDjMsrRLfWQfNWCx0c81txPBz9_FyjW_hGHk1GqulQJpYbNzH0zL9hENa25N8dthW0DQdoWuOOTbNRE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a205f15b6.mp4?token=Y7j5zWxVceNlI_0aJHmsK1gK6OL2KiY0DHH3nPrrOS-YZexJIlwBMyXiYJoKqj16br2dYqKNLueBcO5y0GIxJa1zsvcCuruRaxxZqgTM92dmf9j0fR09TvADf9JcJIJ3vmm1dZCa7lUHJoj90BIo6PQMke2xx_8RLK1vrI8Msy5isA_cINmimi_suGXRM0VYhetJaXxNvnyEeHsg8hLop6dF8qkSyPc-ak_EpXBaBRJsRjcdJFvky4K3LkKKbb0AGYJDB_p1F_bEyYOYfJ_LhQ6o3Rof54WD6ye1woSfMuM0tvwBnBAl4zFRUMwoOtuSnQPx45SJFzKkpdHQ3yRS-LggHxWj6eCharL-RLc6Beu1ZuQcbqlvHTttP11K0FB8P9FpGcgRudsWCxCDPgZboioJ6g4kI5SkwOGc2ywy6lBWSkz2o8XuqSS7A_gMm7UIiAlbiOt_I6dbSX8MeXjjrAie2zT1W2aWNiobaLv1ZGq234oCi_jHcso-AxXW_sIgmzyRKuQQpyx6mMgdJUOeb-yUNd7C_qgJJ4XNq73GX4A1PkoFyg3fOpaFIm45arkESe14MKNBcNZDbxAMebIuHL3rFzYsUDjMsrRLfWQfNWCx0c81txPBz9_FyjW_hGHk1GqulQJpYbNzH0zL9hENa25N8dthW0DQdoWuOOTbNRE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ با اشاره به پیام کمی پیش خود در تروث‌سوشال در طعنه به کمونیست ها:
راستش را بگویم — فکر می‌کنم من بزرگترین کمونیست در تاریخ می‌شدم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/130387" target="_blank">📅 21:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130386">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
ترامپ: تمام کمونیست‌ها بی‌خدا هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/130386" target="_blank">📅 21:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130385">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9aa291828e.mp4?token=hmqZMB6HWT1VX6860kOmeIKPaOetsOjJdQmBvMWIdf3YgEP9ALb708F669EfKXOhdd1VsXJ9RBQXiffTRd_J2waXCkTHJ_mW6vmrm1MlrLofVrtolxIeKXuvdoQc5q-TyljXRFCqCgTTseeO82uRO-lBDsosc-fqu9tXSHlleJc909QsMpievjPhQ9hoxuD_wQDGY2gH2dfZnkSYu2NyZhzDkLzKuCgZ51UlukZHr-n7AQGOs07OGXFHgORU7zEukUoRySiwQtRgmnLnAOETbh5lFIMwJFDwsA9w-AfrPesmMSzDIOlZ21eghVYfNDhC6fnI3xePBYMDh-OvWBE9FrLX0m_rdSP2Vs45DrLS2dtnkG-pC6IQODl10Daq-qKMtliiRg3em2Q3GbOCmgEI5_F-9Rod2imcIJ_jR9njj_rhyiG13irC90Lg8sCGgxbHXeqMkibq9EqgcPbVWxPPXXocJFvj-xuzstozORzciIVVNl7QvABdxP6nfY_1vc2gQNhHlwSE05RBJR_lzDdqdSNC7e5x4IIAb9NJm4chQwa72g4ps5cXGm6Unf4UcI29UHaQlifaTj73mmws_oWrs46LW8uAKJaSfaHggurlbvqL73Y4aLeQGfL9tlOirfQf46Etiay0KXPSdvAqLK20NbLLukkdde06FtphhzPI0qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9aa291828e.mp4?token=hmqZMB6HWT1VX6860kOmeIKPaOetsOjJdQmBvMWIdf3YgEP9ALb708F669EfKXOhdd1VsXJ9RBQXiffTRd_J2waXCkTHJ_mW6vmrm1MlrLofVrtolxIeKXuvdoQc5q-TyljXRFCqCgTTseeO82uRO-lBDsosc-fqu9tXSHlleJc909QsMpievjPhQ9hoxuD_wQDGY2gH2dfZnkSYu2NyZhzDkLzKuCgZ51UlukZHr-n7AQGOs07OGXFHgORU7zEukUoRySiwQtRgmnLnAOETbh5lFIMwJFDwsA9w-AfrPesmMSzDIOlZ21eghVYfNDhC6fnI3xePBYMDh-OvWBE9FrLX0m_rdSP2Vs45DrLS2dtnkG-pC6IQODl10Daq-qKMtliiRg3em2Q3GbOCmgEI5_F-9Rod2imcIJ_jR9njj_rhyiG13irC90Lg8sCGgxbHXeqMkibq9EqgcPbVWxPPXXocJFvj-xuzstozORzciIVVNl7QvABdxP6nfY_1vc2gQNhHlwSE05RBJR_lzDdqdSNC7e5x4IIAb9NJm4chQwa72g4ps5cXGm6Unf4UcI29UHaQlifaTj73mmws_oWrs46LW8uAKJaSfaHggurlbvqL73Y4aLeQGfL9tlOirfQf46Etiay0KXPSdvAqLK20NbLLukkdde06FtphhzPI0qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره کلمبیا: من ال تیگره را تأیید کردم. او را دوست داشتم. می‌دانید چرا؟ چون او مرا دوست دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/130385" target="_blank">📅 21:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130383">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
ترامپ: بنیان‌گذاران ما چهار بار در اعلامیه استقلال به خالق اشاره کردند. چهار بار. من حتی یک بار هم ذکر نشدم. من بسیار ناراحت هستم. حتی یک بار.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/130383" target="_blank">📅 21:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130382">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
ترامپ: دین در کشور ما بازگشته است، بزرگتر و قوی‌تر از آنچه در سال‌های بسیار زیادی بوده است.
🔴
برای اینکه یک ملت بزرگ باشید، باید دین و خدا داشته باشید. اگر آن را نداشته باشید، به نظر نمی‌رسد که کار از آب دربیاید، آیا نه؟
🔴
زیر نظر دموکرات‌ها، کاتولیک‌ها توسط اف‌بی‌آی هدف قرار گرفتند.
🔴
مادر بزرگ‌های حامی حیات به زندان افتادند برای دعا کردن.
🔴
اعضای نیروهای مسلح ما به خاطر باورهای مذهبی‌شان از نیروهای مسلح اخراج شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/130382" target="_blank">📅 21:47 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130381">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e316bf1446.mp4?token=Iw80NbdszIxa9G_WcBuGSU9BkWVzL_p28FuAQkuA5zpbogJS4EEvOvwViqG_NZoTUWfNtgdaYuz-WPH1HY5Z3jOQjPPPVXvpsJj0yP4m_gvVa64MsNXEPkDcMsk8VGF9WuyyjAXA_t8Spp8pCK5dWY10NkrSST10KTe1KMKEuTm7yUqa0bYFqNrci29VuXHcC83VNG7YcpbuMw3TZk5aOZoftjyZSbB2YvSvjsiIveTslCk11JtQ1nZWEmD-0ejSizYUTvQ4fdiq_QA0TJSY3ZfAX_rSn9jiFTp9ptG-pFOfgh_hnZi2mBFpmPJv_Z44ldVf_gCRQW0Wth0xr7wLow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e316bf1446.mp4?token=Iw80NbdszIxa9G_WcBuGSU9BkWVzL_p28FuAQkuA5zpbogJS4EEvOvwViqG_NZoTUWfNtgdaYuz-WPH1HY5Z3jOQjPPPVXvpsJj0yP4m_gvVa64MsNXEPkDcMsk8VGF9WuyyjAXA_t8Spp8pCK5dWY10NkrSST10KTe1KMKEuTm7yUqa0bYFqNrci29VuXHcC83VNG7YcpbuMw3TZk5aOZoftjyZSbB2YvSvjsiIveTslCk11JtQ1nZWEmD-0ejSizYUTvQ4fdiq_QA0TJSY3ZfAX_rSn9jiFTp9ptG-pFOfgh_hnZi2mBFpmPJv_Z44ldVf_gCRQW0Wth0xr7wLow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رسایی وقتی قالیباف رو تو مجلس میبینه
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/130381" target="_blank">📅 21:44 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130380">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aa0bb5024.mp4?token=pMDpMmRwW04PWyJHYFIN1NovsvT395swG0c5WQQY1Wov8MMFbsitamkIaTGJEQflEFA_a1LeEwS42KgLnQdq8rcNlnxzvFC8Hv5LdEleI3x-NIPXaFnNhjd8RMyYoYQXELb1_l52l7Ts5jVY3i7hwN7vL4herTBt1hrm1KqTJbE5ZBa_CSJWP-Vpj3u9UYswvak13Rwtg7NWSK0v3lSkCZ27JWEoktiV5WBSSu5tQRzUhhAjZefjwP_BNThZF19RFnBYb6zHrslwwn6pL6vd1zfiiig2B9pOqO0089LcOQQAAKNVQ1dopOAARXMpd7jrrn6bBleY1V3c8_vItMLTtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aa0bb5024.mp4?token=pMDpMmRwW04PWyJHYFIN1NovsvT395swG0c5WQQY1Wov8MMFbsitamkIaTGJEQflEFA_a1LeEwS42KgLnQdq8rcNlnxzvFC8Hv5LdEleI3x-NIPXaFnNhjd8RMyYoYQXELb1_l52l7Ts5jVY3i7hwN7vL4herTBt1hrm1KqTJbE5ZBa_CSJWP-Vpj3u9UYswvak13Rwtg7NWSK0v3lSkCZ27JWEoktiV5WBSSu5tQRzUhhAjZefjwP_BNThZF19RFnBYb6zHrslwwn6pL6vd1zfiiig2B9pOqO0089LcOQQAAKNVQ1dopOAARXMpd7jrrn6bBleY1V3c8_vItMLTtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حداقل ۹۲۰ نفر کشته و ۳۳۶۰ نفر در نتیجه زمین‌لرزه‌های سه‌شنبه در ونزوئلا زخمی شده‌اند، طبق گفته خورخه رودریگز، رئیس مجلس ملی ونزوئلا
🔴
او افزود که حداقل ۱۷۲ نفر همچنان زیر آوار گیر افتاده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/130380" target="_blank">📅 21:32 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130379">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09db5bdb36.mp4?token=kohSJifwrdoEIEsSLfsO-9u6UqEst-ogU-sn2hYukYYB9zlv9vYK20zKoaUf5bjbIj99C3z1XwsEg0V4pjQHMRmYVZDvJiNq32qhh82BVZaspCZ-7ZSfoFkny64nEr1dMSRKpFJ0TlLywP5DLPRMQCXj4hqcLFliYyGQPoZ3PWIotyM0bP2TZF8JITVXPrvG6dbL1K9Bllf0GAeaBwlr_N1PbXSE87_QvHpPzMDsRgjgfiLqZECWsW2wp5ezH-Ew9cecDv3-6Ei633CQqMaZeeyzldX1-1qAT0LqjGGASV88JVaqAQkucwqop1VaBtgoXXCMdtLDwkv82HHHfkNprDYFVxqrmpJVLN7y5wmHyoMYcxX3ua0vb--2Or1AQeHUhc66HJPkWx_PEunQ9yH2y3X9r1szQuppZ_NRgWaMoJH54XkJBr4GBqWFGSAT-3933s28KUofeTpVpXCjQuPeC3DsvIu_sxNmCa7iX5So7RYZrxLzoIBboDogFN9TcbaIq52OjTf9yHCKw7CPK5rWfGT4bjGQxpOxHx870bM3N1LrZkt3lnrsz5mpkiQGme5j34ZRmqTyEtmd9VjFCBmPja2DlZe3s06p_7Ah6rOkFnbSnb7Beex8aUdd2y8Rm8t5VomMT_1h0xEDy3z0-ubLrnDwWr8H-A0UwNvoZZ__uow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09db5bdb36.mp4?token=kohSJifwrdoEIEsSLfsO-9u6UqEst-ogU-sn2hYukYYB9zlv9vYK20zKoaUf5bjbIj99C3z1XwsEg0V4pjQHMRmYVZDvJiNq32qhh82BVZaspCZ-7ZSfoFkny64nEr1dMSRKpFJ0TlLywP5DLPRMQCXj4hqcLFliYyGQPoZ3PWIotyM0bP2TZF8JITVXPrvG6dbL1K9Bllf0GAeaBwlr_N1PbXSE87_QvHpPzMDsRgjgfiLqZECWsW2wp5ezH-Ew9cecDv3-6Ei633CQqMaZeeyzldX1-1qAT0LqjGGASV88JVaqAQkucwqop1VaBtgoXXCMdtLDwkv82HHHfkNprDYFVxqrmpJVLN7y5wmHyoMYcxX3ua0vb--2Or1AQeHUhc66HJPkWx_PEunQ9yH2y3X9r1szQuppZ_NRgWaMoJH54XkJBr4GBqWFGSAT-3933s28KUofeTpVpXCjQuPeC3DsvIu_sxNmCa7iX5So7RYZrxLzoIBboDogFN9TcbaIq52OjTf9yHCKw7CPK5rWfGT4bjGQxpOxHx870bM3N1LrZkt3lnrsz5mpkiQGme5j34ZRmqTyEtmd9VjFCBmPja2DlZe3s06p_7Ah6rOkFnbSnb7Beex8aUdd2y8Rm8t5VomMT_1h0xEDy3z0-ubLrnDwWr8H-A0UwNvoZZ__uow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بنیامین نتانیاهو، نخست‌وزیر اسرائیل: شهروندان اسرائیل، پیش از آغاز شبات، می‌خواهم دستاورد بزرگی برای دولت اسرائیل اعلام کنم. می‌دانید که مذاکراتی در واشنگتن بین نمایندگان اسرائیل، لبنان و ایالات متحده در حال انجام است. مذاکرات طولانی که امروز به ثمر نشسته‌اند.
🔴
مهم‌ترین نکته این است که اول و بیش از همه، اسرائیل در منطقه امنیتی جنوب لبنان باقی می‌ماند. این یک دستاورد بزرگ است و ما آن را تا زمانی که حزب‌الله تسلیحات خود را کنار نگذارد و تا زمانی که تهدیدی برای دولت اسرائیل وجود دارد، حفظ خواهیم کرد.
🔴
این همچنین ضربه بزرگی به ایران است. ایران سعی دارد ما را با زور از جنوب لبنان عقب بکشد. و در واقع، اسرائیل، لبنان و ایالات متحده به آن‌ها می‌گویند - این کار شما نیست. شما هیچ نقشی در لبنان ندارید. نه شما، نه حزب‌الله، نه هیچ سازمان تروریستی.
🔴
نکته دیگر این است که البته، ما به ارتش لبنان اجازه می‌دهیم تا برای به دست گرفتن کنترل اراضی سازماندهی را آغاز کند. ما در حال انجام دو منطقه پایلوت هستیم. هر دو توسط ارتش اسرائیل توصیه شده‌اند. و یکی واقعاً خارج از منطقه امنیتی، جنوب رود لیتانی است، و دومی شمال لیتانی، بخشی کوچک از آن در منطقه امنیتی گسترده‌ای است که ما در دو هفته گذشته تأمین کردیم و ارتش اسرائیل به آن نیاز ندارد - این را بسیار به وضوح می‌گوید.
🔴
ما دائماً منطقه امنیتی اصلی را خارج از برد موشک‌های ضدتانک حفظ می‌کنیم. ما اجازه نمی‌دهیم حزب‌الله یا جمعیت وارد آنجا شوند. این حفظ شده است. و مهم‌ترین نکته این است که اسرائیل می‌گوید: امنیت ما اولویت دارد.
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/130379" target="_blank">📅 21:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130378">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
اسرائیل و لبنان رسماً یک توافق‌نامه چارچوب میانجی‌گری شده توسط ایالات متحده را در واشنگتن امضا کردند.
🔴
این دو کشور مذاکرات رسمی را در سطح رسمی آغاز خواهند کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/130378" target="_blank">📅 21:28 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130377">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1b3AXQj9igHMPuQhrXwccUDgfNe_JJ96L9A-ahGsrxMlHcwSEgrO64jJWR_8L7VZGbBogkNJVwuz7pes6kwLBPM1dWgtXAQZnZKKn0e6URH6JE9PG_Sn96h0pGlR_yecBlfgidelVkVJRG_dMKnMyY3y_CtLTXlv8vZmDhCIQtm5KP7r7VL4P1yZrOucwp3BMl_nkGEjV4O5I1ZiG_-1kgRpIymmUW_nkspvMaTmWzVaP1Ct6If75G91hoa5sbFQIcA1ebISue10pg69OSWjrQzpgoOlbOP8DmdulW3OCn_qOzW1k4Db6NKgxMWastn8uUKW9E6jl9YqQ78IynACw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث سوشال: کمونیسم بسیار آسان است برای فروش. من بزرگترین کمونیست در تاریخ خواهم بود. من اجاره رایگان، خانه‌های رایگان، غذای رایگان، همه چیز رایگان می‌دهم. متأسفانه، پس از دو یا سه سال، کشوری که این اتفاق در آن رخ می‌دهد شکست می‌خورد. همیشه اینطور می‌شود، و سپس شروع به زندگی در فقر و فلاکت خواهید کرد.
🔴
غذایی نخواهد بود، مسکنی نخواهد بود، ارتشی نخواهد بود، هیچ چیز نخواهد باشد. شما از هر نظر یک کشور جهان سوم خواهید بود و همه رنج خواهند برد یا خواهند مرد. متأسفانه باید بگویم، اما ترور کسانی که با آن‌ها مخالفند، یک عنصر بسیار مهم در ایدئولوژی آن‌هاست. آن‌ها حیوان هستند! در بسیاری از موارد، باهوش نیستند اما، در برخی موارد، آن‌ها هستند.
🔴
برای آن‌ها آسان است که پیروان جذب کنند زیرا وعده‌هایی می‌دهند که می‌دانند نمی‌توانند به آن‌ها عمل کنند، و دموکرات‌ها در برابر آن‌ها نمی‌جنگند. آن‌ها به آن‌ها اجازه می‌دهند راه خود را بروند. آن‌ها می‌ترسند که انتخابات خود را از دست بدهند، آن‌ها از درگیری می‌ترسند. آن‌ها به اندازه کافی باهوش یا سخت‌گیر نیستند که با این طاعون بجنگند.
🔴
اگر آن‌ها را همان‌طور که با جمهوری‌خواهان یا من می‌جنگند، بجنگند، پیروز می‌شدند، اما آن‌ها شجاعت انجام این کار را ندارند. این‌ها دموکرات‌های اجتماعی نیستند، این‌ها کمونیست‌های سخت‌پوش و بی‌خدا هستند. این جدی‌ترین تهدید برای کشور ما از زمان تأسیس آن ۲۵۰ سال پیش است. آیا این مسخره نیست که ما در حال جشن گرفتن یک تولد بسیار مهم هستیم، و به جای صحبت درباره مسیح، آزادی و پیروزی‌های انواع مختلف، درباره تهدید دیگری برای بنیان‌های آمریکا صحبت می‌کنیم؟
🔴
این کمونیست‌های بی‌رحم به تمام ادیان حمله خواهند کرد اما، به ویژه، مسیحیت - آن‌ها همیشه این کار را می‌کنند. تمام کشورهای کمونیستی به خشونت به ادیان حمله می‌کنند. همان‌طور که می‌دانید، ما اخیراً به نیجریه ضربه زدیم و عمدتاً کشتار جمعیت بزرگ مسیحی آن‌ها را پایان دادیم. آن‌ها می‌دانند که اگر بیشتر پیش بروند، حمله بسیار بزرگ‌تر خواهد بود و، در آن، آن‌ها نمی‌خواهند درگیر شوند.
🔴
من مسیحیان را در سراسر جهان نجات می‌دهم، حتی اگر ما در آن کشورهای مختلف نباشیم، با ضربه زدن به این تروریست‌ها به شدت و با خشونت. آن‌ها کلیساهای شما را می‌بندند، مردم شما را می‌کشند. این همان چیزی است که درباره آن صحبت می‌کنند. این بزرگترین تهدید برای کشور ما از زمان تأسیس آن ۲۵۰ سال پیش است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/130377" target="_blank">📅 21:26 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130376">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
روبیو وزیر خارجهٔ آمریکا: لبنان و اسرائیل به توافق چارچوبی دست یافتند
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/130376" target="_blank">📅 21:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130375">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
سفیر لبنان در واشنگتن: چارچوب همکاری که امروز امضا کردیم، گام نخست برای بازپس‌گیری حاکمیت لبنان است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/130375" target="_blank">📅 21:19 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130374">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f979ed21d.mp4?token=qy2yZ7yaq_ut8K83TOrfFD_A_VACrswfqbA8v0G8gbMBDKVgmOxmLOa_8-_Ed66KX3RMRnJ2F3P4Iw9mxgEMd5hEhZlpkMMGTY5W_rLFP3pvuTOG3wJXD0yeRMb9_huyPtHZI9oJ9e_ynA3uQYn4zE-ZGrR9yFBnjZq127Pb2JU4SCzz6zH_FfvNMeiHzJ7WAvP9IilOxvpUJ0tbJtEG6UHCzZEjEz1zJw2HVJ6D9o-Dwd_B2-vtXI5w1zTiuIOut_xheJUryFZVTHGwJX70J5T-fxBprBh7FygTws0XRvjTnR2pTfaWYerLSBvCB1tDlr8GKuBf8pkEgxuiUnu7iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f979ed21d.mp4?token=qy2yZ7yaq_ut8K83TOrfFD_A_VACrswfqbA8v0G8gbMBDKVgmOxmLOa_8-_Ed66KX3RMRnJ2F3P4Iw9mxgEMd5hEhZlpkMMGTY5W_rLFP3pvuTOG3wJXD0yeRMb9_huyPtHZI9oJ9e_ynA3uQYn4zE-ZGrR9yFBnjZq127Pb2JU4SCzz6zH_FfvNMeiHzJ7WAvP9IilOxvpUJ0tbJtEG6UHCzZEjEz1zJw2HVJ6D9o-Dwd_B2-vtXI5w1zTiuIOut_xheJUryFZVTHGwJX70J5T-fxBprBh7FygTws0XRvjTnR2pTfaWYerLSBvCB1tDlr8GKuBf8pkEgxuiUnu7iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس مجلس نمایندگان ایالات متحده مایک جانسون در مورد انتخابات میانی:
🔴
اگر در انتخابات میانی شکست بخوریم، خدا نکرده، این دموکرات‌ها، همه شما، نگرانی بزرگ نیستند
🔴
آن‌ها هر کمیته‌ای از کنگره را به یک نهاد تحقیقاتی تبدیل می‌کنند و به دنبال خانواده رئیس‌جمهور، کابینه، اهداکنندگان و دوستان او خواهند رفت. نیمی از شما در این اتاق هدف قرار خواهید گرفت.
🔴
من برنامه حفاظتی را اداره می‌کنم. ما مراقب شما خواهیم بود. ما در انتخابات میانی پیروز خواهیم شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/130374" target="_blank">📅 21:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130373">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
روبیو وزیر خارجهٔ آمریکا: لبنان و اسرائیل به توافق چارچوبی دست یافتند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/130373" target="_blank">📅 21:11 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130372">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
روزنامه تلگراف در گزارشی می‌گوید برخی منابع اطلاعاتی و کارشناسان امنیتی اسرائیلی احتمال می‌دهند حمله سایبری اخیر به چهار بانک بزرگ ایران، کار اسرائیل و گروه هکری «گنجشک درنده» باشد؛ حمله‌ای که باعث اختلال در خدمات مرتبط با کارت‌های بانکی شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/130372" target="_blank">📅 21:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130371">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rInppMM3PLWjiJhzBq-c_Wugs-2cqnD5xQT7dDCL9Zwjl-OdJNoVeIgBWvHIG5vNyK7ND_fPrYuYALxGKuXZHGfxCUVdoNNcclwBx_52JClBRr0Fsf9vzIP6vtECmNflZaF1FBZogkGmFJlH0D9LTyrWVmjrsUN-DtSgsBdnvGPddPxeUcZXHi_7FF6HYOxdkadqO5c8k4VhF00tD6qrdxwAG8cMjh9yIwM6j0vTfK8FBcEwzY6afYLPM-yOmekfVNVLelBiO2fZEAwS7ztrPzhwcK169tEbzCoIKAw8848Tu3s7oABeTsZg763NHYdjOOrKB-D_FeSwKkNddFckVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سردار محبی ، سخنگوی سپاه : تنگه هرمز سرزمین ایران است و هیچ ارتباطی با آمریکا ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/130371" target="_blank">📅 20:59 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130370">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WzK_AUJBME14WO4KIyWbLfQBiBb4mmFPuLGFcIcNvu31WUyjLMkodkqHTgRGvlyQvvMQTT1phlI3zCRG64vn3O2kRaVItSGWN5OEyuY0rQdFVBvxRXc2V2boGk4I42vPAq8xKClAPds1kJX3k-OHfAY2oGWrjDid8EtXe7ZVY_KpK4hZp98m5ZJRMRR0fbbH1Q6xtHQxIDOtfRzZMIcVX7es0t3yQBoRZa4kTvmP1j0CFEgOVc6ZiWCMPx-ccyb4JfLYPZVbV0EV8ipBZeNurDSQ4UET6339l8KScDvk4kBYUOwEExsYypndqY52zvpfiAw4vGnhQjsU85BTPF0HQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از دست‌نوشته‌ای در یکی از تجمعات شبانه با حضور سنجاب انیمیشن عصر یخبندان!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/130370" target="_blank">📅 20:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130369">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
ارتش اسرائیل مدعی تسلط بر تپه علی الطاهر در جنوب لبنان شد و گفت که نظامیان اسرائیلی کنترل این نقطه را به دست گرفته‌اند.
🔴
این ادعا هنوز از سوی حزب‌الله تأیید نشده است
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/130369" target="_blank">📅 20:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130368">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
نیروهای مسلح لبنان در دو منطقه «آزمایشی» که توسط نیروهای اسرائیلی تخلیه شده‌اند، طبق چارچوبی که در واشنگتن به توافق رسیده، مستقر خواهند شد و نیروهای اسرائیلی تا زمانی که حزب‌الله خلع سلاح نشود، در «منطقه امنیتی» گسترده‌تر باقی خواهند ماند، طبق گزارش کان نیوز.
🔴
طرفین همچنین به تفاهماتی در خصوص مقابله با شبکه تونل‌های حزب‌الله و افزایش توان نظامی آن، و همچنین آغاز مذاکرات آینده درباره مرز زمینی بین اسرائیل و لبنان دست یافتند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/130368" target="_blank">📅 20:41 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130367">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
خبرنگار i24news: توافق لبنان اسرائیل حدود ساعت ۲۰:۰۰ به وقت اسرائیل در حضور وزیر امور خارجه آمریکا روبیو امضا می شود
🔴
یک منبع رسمی لبنانی به الجزیره گفت: جدول زمانی برای عقب‌نشینی از این دو منطقه مقدمه‌ای برای عقب‌نشینی کامل اسرائیل در آینده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/130367" target="_blank">📅 20:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130366">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
ترامپ : نمایش هوایی چهارم ژوئیه، بر فراز واشنگتن دی.سی.، پایتخت بزرگ ما، بزرگ‌ترین نمایش در تاریخ ایالات متحده آمریکا خواهد بود.
🔴
صدها هواپیما، از انواع، اندازه‌ها و سرعت‌های مختلف، به نمایش گذاشته خواهند شد. من تقریباً ساعت ۹ شب سخنرانی خواهم کرد، پیش از آتش‌بازی که مانند نمایش هوایی، تقریباً ده برابر بزرگ‌تر از هر آتش‌بازی در تاریخ کشور ما خواهد بود.
🔴
پس اگر به هواپیماها، آتش‌بازی و رئیس‌جمهور ترامپ علاقه‌مندید، حتماً آنجا باشید!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/130366" target="_blank">📅 20:32 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130365">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
وزارت بهداشت لبنان: از ۲ مارس تاکنون، بر اثر حملات اسرائیل، ۴,۲۴۳ کشته و ۱۲,۱۸۶ مجروح ثبت شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/130365" target="_blank">📅 20:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130364">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCkomMEcP-1iQiUcInpB7CCshgfOlAFimylpAZuAffO4nujFADbOXAOpc724Pmr7mGLY2Gga9i-qHu6nE2pqL0i5YmKLmR4nG-ZhWCd_ogr3ldvhrNsAyiMlBubEFciJyE7GURmoWFB-UsRQKHspOPmrxAqbS2cLa6ObW2ufontnxqA_IcmDhIkD_SSGDD6p203Euhm1xgvBVj3GdG614hE2v9fBtu4pzEJhBzaXLfeIIevm9rAhgI-4fS5nLmSfCaMv2E3q44J-6sLkd-FHT3j6NO947YDT28eP2AiWahPrOcNwU8UZnu8XSs8BdHQT8yP_rzgDvq8e8IyKl4DNWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / خبرنگار آکسیوس از امضای توافق بین اسرائیل و لبنان خبر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/130364" target="_blank">📅 20:17 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130363">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mI6Qczlei1OZIS97M72B920Cw6YE7MN8PmAkVW_xE5EINY8LpW0I44rGF44DyxLAadBzbyhSKFzkYRSop049u9dntMqp3vKYrh_kFOyThsW217RtPm204ZyzBiOJpPmOXzhHyUoOtvoSkzqa_TGwH4w7o-t3HcibOfqfZTMPD-OUtfD8p3_2dgCIP85kSg6ZYm1e9ZrnEQhu4yvAgRwkSBe3E_w-68FHDGRbZuYZWcO378bZ5bqshpAkBC15VzOwzbo_GFshRGPtB6kFabWooMl5UhNdjxFtCpFUT8qWKjWQRwnZH45Q2vcAjc1y6wDEUd77a4AgdD0LGppDeJymVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس کمیسیون امنیت ملی، کشورهای حاشیه خلیج فارس را تهدید کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/130363" target="_blank">📅 20:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130362">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V1winPD-PosD-PftPg54CHMoJl8X_iX3MoQmn15C3tBWRuNvKG0XiFZ9IeZeC6sslL_dPRBKY5m1DKqf4QsogLpAtq53nvJ67rS6lIsgLUGBx7GSozQQ0uXZTG3Bt9L3FFJmDhRu3fJCo0gERMuYU-Su05LFPmA7Co34ZudKPTSNvxzbidDnpP_GT6AUO6KWTGGXBRTbN1Mc-GRUoYbfzhFuEPJu73fA7m6yUaJg3MYoZPWiDHpNnvwHcNY79RV2fsUpoaHvxGXA-2smxFx3G0yBB1nKturhIgmGctTsyzgP2cJSvRy71Syag9MZskBdNa261ZTHnUEcpASyujwucA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث‌سوشال: کشورهای اروپایی متعدد در حال بحث درباره اجرای فوری مالیات خدمات دیجیتال بر شرکت‌های آمریکایی بوده‌اند. برخی از این کشورها به انجام این کار نزدیک هستند.
🔴
لطفاً اجازه دهید این بیانیه به نمایندگی از هر کشوری که چنین مالیاتی را اعمال می‌کند، نشان دهد که بلافاصله با تعرفه ۱۰۰٪ بر هر و تمام کالاهایی که به ایالات متحده آمریکا ارسال می‌شوند، مواجه خواهند شد.
🔴
این تعرفه بر توافق‌نامه‌های تجاری انجام شده با کشور، چه اجرا شده باشند، چه امضا شده باشند و چه نه، ارجحیت خواهد داشت.
🔴
علاوه بر این، اگر آنها پیش بروند، تعرفه ۱۰۰٪ بلافاصله اعمال خواهد شد. از توجه شما به این موضوع سپاسگزارم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/130362" target="_blank">📅 20:12 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130361">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2d110c5d9.mp4?token=mtB3Gbyj8-nRsPrLcq-F3O80eMwRSXI2bkhPAcNQYV_BDsOQ6YCMCQWCAPxuhQzQ7Cu-K9QQVg2aYUthpDAvKW_geQjRliA20sh8Mv6t2L3jTkLK_5UEgfncSDe3Mtkzm6dNajlxqL7FLYM2UfOIRAXOHRO6ZnroWn-rKRX2orMKbIj3ZGklFM1366xw-fPIOcnwbq3iAIN8xr8EqeIQcwItRF1h5nn1H4hbLG-zjAXNFHCxNWTqWGJT0aAmancScmL-29L-T1yW7sGZE4_y-fmaT0hscprRqznTDBC_yyaGr0lJp4oIySQ3QpD3sfmafaRYDu0DvCvtzzyOR4xQdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2d110c5d9.mp4?token=mtB3Gbyj8-nRsPrLcq-F3O80eMwRSXI2bkhPAcNQYV_BDsOQ6YCMCQWCAPxuhQzQ7Cu-K9QQVg2aYUthpDAvKW_geQjRliA20sh8Mv6t2L3jTkLK_5UEgfncSDe3Mtkzm6dNajlxqL7FLYM2UfOIRAXOHRO6ZnroWn-rKRX2orMKbIj3ZGklFM1366xw-fPIOcnwbq3iAIN8xr8EqeIQcwItRF1h5nn1H4hbLG-zjAXNFHCxNWTqWGJT0aAmancScmL-29L-T1yW7sGZE4_y-fmaT0hscprRqznTDBC_yyaGr0lJp4oIySQ3QpD3sfmafaRYDu0DvCvtzzyOR4xQdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
طبق گزارش ها هنوز 50 هزار نفر در پی زلزله های دیروز ونزوئلا مفقود هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/130361" target="_blank">📅 20:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130360">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91151c5fc0.mp4?token=DtSDiSAONHLfZLjxxcXvVIgjZD02L9jNvuFTMbMqTYDOGtsH_nI21SwvOhlL6T1I1MQCcSUpgIHVpQg6ULQI3TAzXWE6IxgiraqPkpVB1pHdlo9HUTqxLNbd6cswhH-c4_2I9zJaaXNgL7WF7cWVMi18iREoBWdjOUu36HnwAHUkuplYvtbi-FVAekqxwP4iUuBPeqOId46LFJgiE8GsPBTfTmYejmKAJE9gHG3bS4v7QoN3AIXuySDx1H6hmtJSIveYjE5zGjUBFYK6EasofP56LArCzVBnFYB6U_oh-NwmPZI6bavCEtwtWb5Z24imstm6-EkjoDwxOn7b0ZMNoxFSU8NGl2KCczAgM1GrcxE6SFO_DpRibmYxRHCakxAKZehLRgxu6C_pln8DqNV6a7l2brDP12vZZzizBUMuyopAHQ3bK0TxE4N_iuN_auSltOzctWP9ra5aGup05IsZI2ManSvCV2zoZnFI5n0gUI7hsEn_nQg_MiRmf0n7wTMTrd4_nlJAbUCWLIVPYpSP8PRQAFuDEeVHgkeX1TQCYDHRQ7ztQfjyGXFHc62Sa9VtsvBD1TskCsxLC8rP5Stx8xFGUf6pWm4HiIc8iFrAObAaH1-iFNkAMFjvurlvUo4oPwYaJ9M3YpnK0VYHu54Kbk22URPVoV_9-eETRx_l96U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91151c5fc0.mp4?token=DtSDiSAONHLfZLjxxcXvVIgjZD02L9jNvuFTMbMqTYDOGtsH_nI21SwvOhlL6T1I1MQCcSUpgIHVpQg6ULQI3TAzXWE6IxgiraqPkpVB1pHdlo9HUTqxLNbd6cswhH-c4_2I9zJaaXNgL7WF7cWVMi18iREoBWdjOUu36HnwAHUkuplYvtbi-FVAekqxwP4iUuBPeqOId46LFJgiE8GsPBTfTmYejmKAJE9gHG3bS4v7QoN3AIXuySDx1H6hmtJSIveYjE5zGjUBFYK6EasofP56LArCzVBnFYB6U_oh-NwmPZI6bavCEtwtWb5Z24imstm6-EkjoDwxOn7b0ZMNoxFSU8NGl2KCczAgM1GrcxE6SFO_DpRibmYxRHCakxAKZehLRgxu6C_pln8DqNV6a7l2brDP12vZZzizBUMuyopAHQ3bK0TxE4N_iuN_auSltOzctWP9ra5aGup05IsZI2ManSvCV2zoZnFI5n0gUI7hsEn_nQg_MiRmf0n7wTMTrd4_nlJAbUCWLIVPYpSP8PRQAFuDEeVHgkeX1TQCYDHRQ7ztQfjyGXFHc62Sa9VtsvBD1TskCsxLC8rP5Stx8xFGUf6pWm4HiIc8iFrAObAaH1-iFNkAMFjvurlvUo4oPwYaJ9M3YpnK0VYHu54Kbk22URPVoV_9-eETRx_l96U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تام هومان وزیر مرز های ایالات متحده آمریکا: من به اندازه‌ای که به پدر خودم احترام می‌گذارم، به رئیس‌جمهور ترامپ احترام می‌گذارم... من می‌دانم که در درون او چه چیزی وجود دارد.
🔴
اگر می‌خواهید رئیس‌جمهوری بی‌نقص داشته باشید، بهتر است منتظر ظهور دوم مسیح بمانید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/130360" target="_blank">📅 19:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130359">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
تام هومان، رئیس مرزهای ترامپ
:
من نمی‌خواهم حتی یک کلمه دیگر درباره دروغین بودن رفتارهای غیرانسانی رئیس‌جمهور ترامپ بشنوم. او هر روز جان‌ها را نجات می‌دهد.
🔴
وقتی رئیس‌جمهور ترامپ مهاجرت غیرقانونی را ۹۷ درصد کاهش داده است، چند زن تجاوز نشده‌اند؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/130359" target="_blank">📅 19:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130358">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
ارتش اسرائیل: نیروهای ما در حال تحمیل یک واقعیت امنیتی جدید هستند که به حضور حزب الله در این منطقه استراتژیک پایان خواهد داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/130358" target="_blank">📅 19:46 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130357">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
ارتش اسرائیل مدعی تسلط بر تپه علی الطاهر در جنوب لبنان شد و گفت که نظامیان اسرائیلی کنترل این نقطه را به دست گرفته‌اند.
🔴
این ادعا هنوز از سوی حزب‌الله تأیید نشده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/130357" target="_blank">📅 19:44 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130356">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WIz29DKGTJQZlgI9608X3bECOhn7slUofcYz_DWnm9Yx2McNUiD5odLJ51bH6WNmg1UjW4zQ0RdFBkhnD7yp2gLjPUdfOIy1hHh_kpYt2J4zy7eVQz61lrQmW-soZF7ZniIFqVFHQ1oRASGy16IUg0fzCZ9pmaMBBpLLDUbvCqB6tj0Ed9kPOWteDQ62d7Hg9puYl_ZPdIDNve1SSUvYRH_Pm0z72HHLThPejZKY7sRfnp2dLOKzEFfDpYakowgH-udXT_SgPsV6zWM6F7qJ0_PMGSM1dyhvsFsjm8YEy_ys-HCKxb5FnFgQdTL4wmRTDHOnEbRKcY_sTMKfCJlHzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / ترامپ:  ایران حداقل چهار پهپاد تهاجمی را در یک جهت به سمت کشتی‌هایی که از تنگه هرمز عبور می‌کردند، شلیک کرد.
🔴
یکی از پهپادها به عرشه یک کشتی باری برخورد کرد و ایالات متحده سه پهپاد دیگر را سرنگون کرد.
🔴
این نقض واضح آتش بس است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/130356" target="_blank">📅 19:32 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130355">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
فلاحتی، امام جمعه رشت: شعار مرگ بر آمریکا همیشه باقی است.
🔴
ما با مردم امریکا مشکلی نداریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/130355" target="_blank">📅 19:22 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130354">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
پرس تی‌وی: یک خط ارتباطی ایران و آمریکا در تنگه هرمز ایجاد شده است تا از حوادث نظامی جلوگیری شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/130354" target="_blank">📅 19:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130353">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
منابع داخلی: حملات امروز اسراییل به لبنان نقص اتش بس محسوب میشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/130353" target="_blank">📅 19:12 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130352">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FZq5nKT9O9h8zupCLrcf3u_QjN_sRe-j6fPZUVf0fX4sOfczie6UBo3TahhkSSrrF0OdImUSyKkdqZbe7UymjxLHe0dJMb52Op6oKLoqA9MpktRj5GzmMGWz7eB2d9nRfogHGFNhFnIn2XVUOWMNehdEaDkZwr-92NVQtonZo_dNJQE9Cyerodbw0W2JgsoSLyK781EHQIqdyIzVU7MZ1mYPWHHfTgIHfBoBnQD1733mtWpa_GSygLj0QyIGh5b8yM37m31XsuXncakLRCyDqFyNYfeoLUVqgfXzSfT512_-Jx2ZSYEUIowW1inUFppPiHab6DnbYNcg6Qck7XbsTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث‌سوشال: همین الان اعلام شد و من لزوماً از صحبت درباره آن خوشحال نیستم، زیرا اصلاً خوشایند نیست، اما دولت ترامپ بالاترین میانگین نرخ بازداشت روزانه توسط اداره مهاجرت و کنترل مرزی (ICE و CBP) را دارد، از جمله کل بازداشت‌ها و دستورات نهایی اخراج، که به مراتب بیشتر از هر رئیس‌جمهور دیگری است!
🔴
دستورات نهایی معلق به دلیل دادگاه‌ها به شدت به تأخیر افتاده‌اند، اما این نیز یک رکورد است. دونالد ترامپ با وجود اینکه اعداد خود را دستکاری می‌کنند و افرادی را که هرگز حتی تلاش نکرده‌اند وارد کشور شوند نیز در آمار لحاظ می‌کنند، بالاترین مجموع اخراج در ۱۲ ماه را به مراتب نسبت به هر رئیس‌جمهور دیگری دارد.
🔴
همچنین، میانگین روزانه دستگیری و بازگرداندن به کشور، به مراتب بالاترین میزان تحت ریاست جمهوری ترامپ است. هیچ رئیس‌جمهور دیگری به این ارقام نزدیک نمی‌شود.
🔴
بنابراین، وقتی این لایه‌های خبری، کارشناسان، دمکرات‌های احمق و کمونیست‌ها سعی می‌کنند استدلال کنند که ارقام باراک اوباما با ارقام دونالد ترامپ قابل مقایسه است، خوب است افرادی مانند «شانون بریم» که به «شیر و نان» (Milk Toast) معروف است و دیگران، کمی مقاومت کنند — فقط کمی.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/130352" target="_blank">📅 19:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130351">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
منابع العربیه: دور آتی مذاکرات میان آمریکا و ایران به‌طور فنی در سطح کارشناسان و با حضور میانجی‌گران طی روزهای 28 و 29 ژوئن در بورگن‌اشتاگ سوئیس برگزار خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/130351" target="_blank">📅 18:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130350">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
وال استریت ژورنال: پنتاگون در حال بررسی انتقال نیروها به پایگاه‌های دورتر از برد موشک‌ها و پهپادهای ایران است
🔴
ارتش آمریکا در حال بررسی بازسازی پایگاه آسیب‌دیده در بحرین، کاهش حضور در کویت و عربستان و انتقال نیروها به پایگاه‌ های دورتر از برد موشک‌ها و پهپادهای ایران است
🔴
به گفته مقامات آمریکایی، احتمال دارد برخی از ساختمان‌ها بازسازی نشوند.
🔴
مراکز فرماندهی و کنترل ممکن است به زیرزمین منتقل شوند و سایر قابلیت‌های نظامی‌احتمالاً به طور گسترده‌تر در سراسر منطقه پراکنده خواهند شد.
🔴
اسرائیل یکی از مکان‌های مورد نظر برای ایجاد یک پایگاه جدید است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/130350" target="_blank">📅 18:47 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130349">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
سازمان بین‌المللی دریانوردی: از کشتی‌ها می‌خواهیم که با پیمودن مسیرهای غیرمجاز برای عبور از تنگه هرمز، خطر نکنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/130349" target="_blank">📅 18:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130348">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
عمان به متحدان اروپایی هشدار داد که ممکن است نیاز باشد هزینه‌های کشتی برای عبور از تنگه هرمز را پرداخت کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/130348" target="_blank">📅 18:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130347">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
روس اتم: متخصصان در هفته‌های آینده به نیروگاه هسته‌ای بوشهر بازخواهند گشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/130347" target="_blank">📅 18:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130346">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bb5026706.mp4?token=JMjREAO0_vWokp1_DWyPRhtJAjWI_tQgttjRGmdr--pQLn4U_h7-zilgSkHJeLMq2KPYLrS_jqAaTDBSp18qw0eMfesimBVqdRS0lz-SVKB3NNuF7QQDLq9Ozyo5RmM8L9aG2tMOMBVkq_qGx05Wqcu4RN6DNvWSr47edbrb56-FhV55bQ_3Blr7mxrlnelzWNNKZQ1PFw7dV-cD2XGKcxSAoh6aZKc2tvvq1XyPxDXX7YlUabP-UzmD8WDD0p972coXEjGJinf1DSHaZ1pyToWYCexEsm5C94adPsn3dkUIZD_edT4ozJ5vE-xVsx9aZ5b9BnCEwWRMkez6gvTWHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bb5026706.mp4?token=JMjREAO0_vWokp1_DWyPRhtJAjWI_tQgttjRGmdr--pQLn4U_h7-zilgSkHJeLMq2KPYLrS_jqAaTDBSp18qw0eMfesimBVqdRS0lz-SVKB3NNuF7QQDLq9Ozyo5RmM8L9aG2tMOMBVkq_qGx05Wqcu4RN6DNvWSr47edbrb56-FhV55bQ_3Blr7mxrlnelzWNNKZQ1PFw7dV-cD2XGKcxSAoh6aZKc2tvvq1XyPxDXX7YlUabP-UzmD8WDD0p972coXEjGJinf1DSHaZ1pyToWYCexEsm5C94adPsn3dkUIZD_edT4ozJ5vE-xVsx9aZ5b9BnCEwWRMkez6gvTWHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
امیر قلعه نویی درباره حضور پرچم‌های رنگین‌کمانی و برگزاری مراسم حمایت از جامعه LGBTQ در ورزشگاه سیاتل
:
ما اینجا برای فوتبال هستیم، نه مسائل دیگر. تمرکز ما بر روی مسابقه و کسب موفقیت است. درباره موضوعاتی که در دین ما ممنوع است و وجود ندارد، نمی‌خواهیم صحبت کنیم.
@AloSport</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/130346" target="_blank">📅 18:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130345">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
بانک ملی ایران در اطلاعیه ای از اخلال مجدد در خدمات کارتی این بانک خبر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/130345" target="_blank">📅 18:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130344">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngxAiwYtylqVwwxApH-HS4ZPRY-9ST-vOgNoegoMz2xMCycpltYC7Gt8TUPaBRXeCOJh1LnZVH9jUsaDr09-dfHlun-A8vTLOjl_YbqYQ69fIXddWvxkkz2WepIhjtqFSunyQyX5u8SZKmhw1Ozmo7FedcO_nhn_-QZ6dRgpdhVaRj9rKNODCh78YzlOjtNwNFlk2XJMGwOuQWNPKw_JNSFls_LMtB68FCCYF9pyvKsrzrqO1v9N0u2_nwOk2o6o1pMvDM01YiXfN0qTX56GH6YM2D8A1VO_ZN-iiqLjkxHwAiZCYrUGveyPNXgR7GcQ4PBMJE8xdR6ehdE5iDwKUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان به همه مشاغل علاقه داره به‌جز ریاست‌جمهوری
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/130344" target="_blank">📅 17:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130343">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
۲۲ خدمه ایرانی نفتکش توقیف شده توسط آمریکا، در کراچی تحویل سرکنسولگری ایران شدند
🔴
۲۲ خدمه ایرانی یک نفتکش که توسط ایالات متحده در آب‌های بین‌المللی به طور غیرقانونی توقیف شده بود، با پیگیری های سفارت جمهوری اسلامی ایران و اقدامات تسهیل گرانه دولت پاکستان، امروز به نماینده سرکنسولگری جمهوری اسلامی ایران در بندر کراچی تحویل شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/130343" target="_blank">📅 17:46 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130342">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
نعیم قاسم، دبیر کل حزب‌الله:
«ما در کنار ایران خواهیم ایستاد و می‌خواهیم متحد باشیم زیرا مشخص شده است که قدرت شما، همراه با قدرت رزمندگان مقاومت در میدان، به ایجاد تعادل مناسب برای شکست اسرائیل و اخراج آن از سرزمین ما کمک می‌کند».
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/130342" target="_blank">📅 17:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130341">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">دعوا سر نذری تو همدان
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/130341" target="_blank">📅 17:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130340">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه ایران، اسماعیل بقایی:
همسایگان جنوبی باید پاسخگو باشند: چرا خودشان برخلاف اصل همسایگی خوب و قواعد بنیادین حقوق بین‌الملل، به تجاوز علیه همسایه مسلمان خود دست زده‌اند و اجازه داده‌اند از خاکشان علیه ایران استفاده شود یا موشک‌هایی از آنجا پرتاب شود؟
و چرا چشم بر مسابقه مخرب تسلیحاتی و خرید و انباشت صدها میلیارد دلار انواع سلاح‌های پیشرفته که هیچ توجیه دفاعی ندارد، می‌بندند؟
و چرا تجاوزات مکرر رژیم صهیونیستی به کشورهای منطقه و اشغال سرزمین‌های فلسطینی، لبنانی و سوری را نادیده می‌گیرند؟
چرا در برابر زرادخانه هسته‌ای اسرائیل که خارج از نظارت‌های بین‌المللی است سکوت می‌کنند، در حالی که توان دفاعی متعارف کشوری که بارها تهدید و حمله از سوی کشورهای همسایه را تجربه کرده، به عنوان «تهدید» معرفی می‌شود؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/130340" target="_blank">📅 17:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130339">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8be098ed9.mp4?token=uLRZ1UmSdJLSCnyA0JKQpblHiTROFDW46ExU2LpzhBh1-vwN4uxEhdncwVa5fAmP7NBuh-XlLsw3Jd5z_C40zjM_9LnhTZhHSCK8upAEa5AztKcWuz0C8kPlMigTbvUzLWiI2YgSVVUmHoG286TDP9u2s1xboMnEbKL6Dgsjv-slLqTRkcAsW1k_LyazZOY2I5hQeTQpmIFngvIghIEV15zOHvZ-sv7yroVprc6wqG8wZnM4KP-ZYwhYzfrtqY7fEKdybh-BnLUg9az-mfUgusuEvCADXFLIzOrJSbZVyLItQUdIgzRhWJAvb8NMkhc98fWUpdpIuWRca_rF6eUqFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8be098ed9.mp4?token=uLRZ1UmSdJLSCnyA0JKQpblHiTROFDW46ExU2LpzhBh1-vwN4uxEhdncwVa5fAmP7NBuh-XlLsw3Jd5z_C40zjM_9LnhTZhHSCK8upAEa5AztKcWuz0C8kPlMigTbvUzLWiI2YgSVVUmHoG286TDP9u2s1xboMnEbKL6Dgsjv-slLqTRkcAsW1k_LyazZOY2I5hQeTQpmIFngvIghIEV15zOHvZ-sv7yroVprc6wqG8wZnM4KP-ZYwhYzfrtqY7fEKdybh-BnLUg9az-mfUgusuEvCADXFLIzOrJSbZVyLItQUdIgzRhWJAvb8NMkhc98fWUpdpIuWRca_rF6eUqFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کوروش احمدی: اگر توافق نشود، ترامپ به سمت محاصره می‌رود، نه جنگ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/130339" target="_blank">📅 17:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130338">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
هشدارهای حمله موشکی در امارات متحده عربی فعال شده‌اند.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/130338" target="_blank">📅 17:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130337">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
هشدارهای حمله موشکی در امارات متحده عربی فعال شده‌اند.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/130337" target="_blank">📅 17:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130336">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KPt8FcpQi6NZ7MIOQM0Yb6L_5Kb5UR_mz6J6tIcI6WiMIR8zfZrZb3PA2LUMd5St5PCLyZzSFL4bLcn8cCeB-WoeqxJyquSZtFAcT9ic1VMZG_6GTqPXkLPeZC4fAFEzVxvpiPkNsa5sE2g60bwjeMdUxYUjiw0_J2Ht04y1MggAstXhZIVUmFQPIQ0glKkmwsgXfjnrsTdfbJlERKh1E3-VBgE9j0r1cybCghIZ3Juse5XgS075YWMNjYYnRJ0mNHsfaNHDVWUoXyKB4qEFaaByNgfQFPrisISBkGrWFiQA9F2ubOgoLyGKsNCp5iQmZ7Bo1c0-mKyS6f4O7eLIaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هشدارهای حمله موشکی در امارات متحده عربی فعال شده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/130336" target="_blank">📅 16:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130335">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
العربیه: دور بعدی مذاکرات آمریکا و ایران در ۲۸ و ۲۹ ژوئن در بورگنشتوک برگزار می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/130335" target="_blank">📅 16:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130334">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4a208c87a.mp4?token=sjdI1PbB10uZl-mEEoYm_eHxHQ2TdcjBkJ-WkPGZil-kydRzJcxX29bnUrbpuWmKTKyGjxp7piR6vrcKlJl-iGuYDrTW4wWCNR86LPnxS5iL6WVZ3qGDBF-YBqoeXQdnXBl3gQ9cF9J3wQVwWd2XhulyCrw8d-vNzLCw7kJuaj-dh68lgar8HxpVJBtFZZrFon3_mLXFpIJbPY3HTFwX9hlaa0E15JsmIUPGKbNfKxr7lnyhZfud8IfBVfr07nP5yZPGN2kxBANC4bxMcHHibLFWDDY3WrjSCJmD-4PJ_vf2VLof0xvfuf_6GR5Q6_5Nf5l_VdUqx2PLtExqPwot1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4a208c87a.mp4?token=sjdI1PbB10uZl-mEEoYm_eHxHQ2TdcjBkJ-WkPGZil-kydRzJcxX29bnUrbpuWmKTKyGjxp7piR6vrcKlJl-iGuYDrTW4wWCNR86LPnxS5iL6WVZ3qGDBF-YBqoeXQdnXBl3gQ9cF9J3wQVwWd2XhulyCrw8d-vNzLCw7kJuaj-dh68lgar8HxpVJBtFZZrFon3_mLXFpIJbPY3HTFwX9hlaa0E15JsmIUPGKbNfKxr7lnyhZfud8IfBVfr07nP5yZPGN2kxBANC4bxMcHHibLFWDDY3WrjSCJmD-4PJ_vf2VLof0xvfuf_6GR5Q6_5Nf5l_VdUqx2PLtExqPwot1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
این سکانس مختار دقیقا برا این روزهای جلسات دورن نظام ایران ساخته شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/130334" target="_blank">📅 16:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130333">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/554e768468.mp4?token=Hl9GPLpxl2o7dOGxHdQvHF07RShEcYeGW12qT-7pwTv3kb4wW39ycVVbo1fiolOYwsBgJ8BXVvBUhEADRLXIvu-LWpUye99rESNBLdyxOfyRTuSMb2UAXv0NxNTkQ_B_WiP8J6CwPMe2p3D5gFvIHv9nafc3PeXvQdUHO6JU56-UkmR-b3Nt3B56G5wxHVTwgFhXMOoeXxwuQgaZCTmoP1RohxL_tefyf-r6togR4jxci8DYbRg2LbmdriOQ1rLL9SpNj1vk2gJgO-yFtoFsMWNzcn1DqUr0AI0aRimeNWJhrqvlK1-viPTnDKMPekdMEtxESdzY7h9p_Op62c1-Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/554e768468.mp4?token=Hl9GPLpxl2o7dOGxHdQvHF07RShEcYeGW12qT-7pwTv3kb4wW39ycVVbo1fiolOYwsBgJ8BXVvBUhEADRLXIvu-LWpUye99rESNBLdyxOfyRTuSMb2UAXv0NxNTkQ_B_WiP8J6CwPMe2p3D5gFvIHv9nafc3PeXvQdUHO6JU56-UkmR-b3Nt3B56G5wxHVTwgFhXMOoeXxwuQgaZCTmoP1RohxL_tefyf-r6togR4jxci8DYbRg2LbmdriOQ1rLL9SpNj1vk2gJgO-yFtoFsMWNzcn1DqUr0AI0aRimeNWJhrqvlK1-viPTnDKMPekdMEtxESdzY7h9p_Op62c1-Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اقلیت کم عقل در ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/130333" target="_blank">📅 16:26 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130332">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ICMU15syI4ClMM5wsBAKSGkQOYVOq1jBQK3jbZajZ9hpTtcrVrvfM5n9YobwKIgOx89ZUWBOX0-UoouWkOzPF3tNx0fBrNUaDxJ1wqXvAbzpbuldsRfRGK0UQVrPEtKgMHxk7l2DPeMv1b4fibXl19Mck4I9PFuJqJWd7-HOwXraN7G2bc6DrSyBIHU54PBkjxEk0F3d80lmAz5-W0xvThMM-3H_EFJ4eplT37MMhr4ZgDmMk6vYIYGOi0S0p-fpEI-bP5otqmF-gmjJD8uSNzrz2rpJk-j4xbvvnX0gxfATBpGQmJshzDksYQPXi45vsy5NqP_nWSV_t85CYKsuew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش وزیر دفاع اسراییل به سخنان سردار قاآنی: اگر ایران به اسرائیل حمله کند، بزرگ‌ترین اشتباهی خواهد بود که تاکنون مرتکب شده است.
🔴
نه هرمز و نه شلیک به غیرنظامیان در اینجا به او کمک نخواهد کرد. هیچ چیزی ما را متوقف نخواهد کرد.
🔴
نیروهای ما آماده‌اند تا کار را تمام کنند.
🔴
وی در انتهای توییت، پزشکیان، قالیباف و عراقچی را تگ کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/130332" target="_blank">📅 16:22 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130329">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gwEedEbXrtjkZCZPlodfuoRg0aXIOiRoxUVQS6X9KL6k8ZX6Pdzw_Hvqp-yatyfi6jSpdHI1nhlHlgtOT8iBGoV8XM6vx-_A8aj2LMKoDV0P03dGohhkLQZJ11nOq-j2Gba-9l_bZ_9iypM5nXR3UEY2SN57wSR82jpICdbfmY04jR5Ul2efU7sHga-wjqNJsC3S41FacnvY1_OK1CWfUzU-XN3qbQ7210Yi5tEpZ7udH3phx6gCBgtnZd_pAmI-LOx7s-FkqeSzK6PMO0_zz3DsLw8g4RXHGcWKAwdrkPiOcZec9rhkIRPi3QFjSZOFi4qd8B8PL_n7Fhy3JrnGQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y0uioFrM-Ub9qxml8-bZKPKv8uFp7TCapTJ0JNjZ5gB4KGdq9BQKSDs6bXIhcjj6weGAcewe-XUiExXIW2el8nL3jHPNG9H5sD1sQo_1Z_oGh6XBwpjdivvW7G92NY0vnBuofzg6ibfYkdrPJZ0L9MkCr-xRLTgxCi_ZqHZwl0HaGjDsr8lXuJp8pzXnKPR8CYJgn5QgO4lWF-ZrAZmBaE_Y6hIhu0Je_ArhfDy9PLHZdLhoRwhv8FelCKRpNbq9NF3--hXyZEBPjC7zIarnC_EbY8yor3Kkov8gH86vxK4LE5qpD_8ICHePILQ-KQZ9QuyDMvaEuiXDn7i_JvXXBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/812712f3b6.mp4?token=cBLgFxDIFAl4mRALSg7BCTFxXfi4aI9hAdU6a6yNMAl2IceGcpIyu5D3j1MYvbARbwuZEFakivJgbH7m1upwBFe23cF6iqJX2GoEUN9R_TAflUOW7PJkLovhngBwHuOIQ-TbeXpkR7KHTmgCn7E8y1TBYQVreRasTJtThZNMFD3EfBCz-6XQUIRHoR2epa5nO1b2W-CvknGAR-j15IIFVLy13YniRMaIWux7AgHehvzFzoXYHbEU9q27D7f56xnrlCo_7mRomr7BqI0erpS3CZZmJQmLysiC0RJVVdFkf3wRoqDtWas8SwwFqBdI6bRPn0WLy3qMLYiUcgbDij0lpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/812712f3b6.mp4?token=cBLgFxDIFAl4mRALSg7BCTFxXfi4aI9hAdU6a6yNMAl2IceGcpIyu5D3j1MYvbARbwuZEFakivJgbH7m1upwBFe23cF6iqJX2GoEUN9R_TAflUOW7PJkLovhngBwHuOIQ-TbeXpkR7KHTmgCn7E8y1TBYQVreRasTJtThZNMFD3EfBCz-6XQUIRHoR2epa5nO1b2W-CvknGAR-j15IIFVLy13YniRMaIWux7AgHehvzFzoXYHbEU9q27D7f56xnrlCo_7mRomr7BqI0erpS3CZZmJQmLysiC0RJVVdFkf3wRoqDtWas8SwwFqBdI6bRPn0WLy3qMLYiUcgbDij0lpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
برخورد هواپیما به آسمان‌خراش ۵۱۸ متری در پکن
🔴
یک هواپیما با آسمان‌خراشی به ارتفاع ۱۷۰۰ فوت (حدود ۵۱۸ متر) در پکن برخورد کرد و سپس به زمین سقوط کرد که منجر به تخلیه ساختمان شد.
🔴
در اثر این برخورد، دو پنجره ساختمان شکسته شد و هواپیما کاملاً متلاشی گردید.
🔴
دود غلیظی از طبقه همکف ساختمان، جایی که لاشه هواپیما پراکنده شده بود، به هوا برخاست.
🔴
شمار تلفات هنوز مشخص نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/130329" target="_blank">📅 16:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130327">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OHACeryeIKUcIfJeNkihUVT4P5JUpSzq-p5GsRa0gta5DCNm2sJyh-2dCsk6CibTxP7PWNIcCBtEMGI00NLC4zsGdENQGrZwXC6eWHvQXoxiZ-bzNi-zK0JJB0EaXEJsJt2o_qA1O5p4tRgWzKF2yBeNyhhxiuHxOSzgL87GyZiOhVTV856_e9NPUioaNi9tPSnuByGKUgyypYuva0T1xD6xYQjXLk6ZjwW6Z-38X5NF8FslIZ8tXSKbr8v81zH-ulG9-kuWBK2f-E-t6NyPBXEt4Si99SfsK0rKcJk7dWPNoUcSXRH9s8VUPKsA51z7R10uKZj_yLm89bZogwVycw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بازی ایران و مصر که به عنوان مسابقه «افتخار همجنسگرایان» نامگذاری شده؛ فیفا اجازه داده فردا همه با نماد و پرچم رنگین کمان
🏳️‍🌈
بیان ورزشگاه و معلوم نیست صداوسیما چطور میخواد بازی رو پخش کنه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/130327" target="_blank">📅 16:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130326">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce3a84c436.mp4?token=lvit0ECmtmLXVBy4oJKZvWU1PfEb5PTlECUDaLv_x-b4u-FxG5WPk_drq1HnFJzoLPNDDy1ZVxNlTjgn6uMtVq-XAqi9UXMDvkkY9Uv5ry5t8mqQweg1sCuJWycHagZP2lavkmb8QntH_d9srxJ8wpC5N-AVTTMedfvgKtpgXMO0n0ze_6Ru8KbB-Of8DFttd1i2FWDXkSrNo3t_nkUhME4CiuIGhrCI_9xCNYWF27mCvOA85cElDiJ2-p_kqIOe8XKluvQlZqhyIGa4bwOYw2bN0hDDAA7KmOo1bouRP6LtEeHSxEMe6GUgqQlAvMe1-j3pryZSWbTJJAwuINQOOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce3a84c436.mp4?token=lvit0ECmtmLXVBy4oJKZvWU1PfEb5PTlECUDaLv_x-b4u-FxG5WPk_drq1HnFJzoLPNDDy1ZVxNlTjgn6uMtVq-XAqi9UXMDvkkY9Uv5ry5t8mqQweg1sCuJWycHagZP2lavkmb8QntH_d9srxJ8wpC5N-AVTTMedfvgKtpgXMO0n0ze_6Ru8KbB-Of8DFttd1i2FWDXkSrNo3t_nkUhME4CiuIGhrCI_9xCNYWF27mCvOA85cElDiJ2-p_kqIOe8XKluvQlZqhyIGa4bwOYw2bN0hDDAA7KmOo1bouRP6LtEeHSxEMe6GUgqQlAvMe1-j3pryZSWbTJJAwuINQOOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
این شخص غلامرضا قاسمیان است کسی که یه مکانی درست کرده به نام پناهگاه زنان خیابانی که اونجا زنان رو جمع میکنه تا خدمات جنسی بدن! و اسمشم گذاشته شلتر
🔴
قاسمیان در این ویدیو میگه خودمم اینجا میرم و میام
🔴
صدا و سیما هم یه هفته هست اینو هی میاره تو آنتن زنده تا از مزایای عدم توافق و مقاومت و بدبختی بگه
🔴
نون این جریان تو بدبختی مردمه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/130326" target="_blank">📅 15:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130325">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
مهار آتش‌سوزی در پتروشیمی کارون
🔴
روابط عمومی پتروشیمی کارون از مهار آتش‌سوزی امروز در این شرکت خبر داد و گفت: این آتش سوزی تلفات جانی نداشت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/alonews/130325" target="_blank">📅 15:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130324">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
ایتمار بن گویر وزیر امنیت داخلی اسرائیل به کانال 7 گفت: آتش‌بس در لبنان نمی‌تواند پایدار باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/130324" target="_blank">📅 15:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130323">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
هم اکنون، هشدار تخلیه ارتش اسرائیل برای شهر منصوری در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/130323" target="_blank">📅 15:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130322">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
فارس: مذاکرات بر سر بحث هسته‌ای برای بعد از حاصل شدن توافق نهاییه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/alonews/130322" target="_blank">📅 15:05 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130321">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/955a11f8e7.mp4?token=HoDHhNwSrZ1V7HGC_EPRYaW72K7R6IxrNed0JiLqm75nYbrDRHriizdPlsUxGVSLI7GfDT9-YLT8j8vQsUVGBH7jmYYQfQmoSTBvsovfhVU5Wyn2W2-3nvG5n5Ch_S9HBB1JELbSA7ia9zasyoUlCqv4xMZFMlLlbJ527F7BrQ2QGSE_NkJ14YxGMNitoiYkVIGvaZGid9wSRpIChavPUR5nqlrHR7_wtvXlN_dwn6hQGlz_QNtL2Wi-4qdtetqV5mpjZqL79e_9f_7bmu8WTtObUoHp90swlpXJp5EASKK2xpjfSUDFK4e4zYloHhBUw_WJ-5AYJWfYlPYiPNYXjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/955a11f8e7.mp4?token=HoDHhNwSrZ1V7HGC_EPRYaW72K7R6IxrNed0JiLqm75nYbrDRHriizdPlsUxGVSLI7GfDT9-YLT8j8vQsUVGBH7jmYYQfQmoSTBvsovfhVU5Wyn2W2-3nvG5n5Ch_S9HBB1JELbSA7ia9zasyoUlCqv4xMZFMlLlbJ527F7BrQ2QGSE_NkJ14YxGMNitoiYkVIGvaZGid9wSRpIChavPUR5nqlrHR7_wtvXlN_dwn6hQGlz_QNtL2Wi-4qdtetqV5mpjZqL79e_9f_7bmu8WTtObUoHp90swlpXJp5EASKK2xpjfSUDFK4e4zYloHhBUw_WJ-5AYJWfYlPYiPNYXjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروی دریایی سپاه: عبور از تنگه هرمز فقط از مسیرهای اعلامی ایران ممکن است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/130321" target="_blank">📅 14:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130320">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d81ff4ef1.mp4?token=bjc4NjpMm9qYenhPQc5aLLH47bUuWpI7q35c6PrHCgLYdN9CST2mxS5k3VFmEl_M8HFCjAxzOTfb9IqACihdjJfkRlt3VYeQh6sfoPXzZu9aKwlCf1m7X0gizaZ0rVeeZi4rbM9At-r7vGCB6oUi8LBrEABxKtEr7Y0CRqLE7wxWF-J6WXXphOwANlDsDa4ZioMcVukgqcosAa7QBbtx0xvyPF571xpE80mwpwgDjgV_cDZWllilLKa_EqgzDtHxhDvW-KXCML6jEYRmjOjFPc9G_F8b1oIDcW8Cb8mTj-z_IcwBy3I7mARQV_Zaixtx5Pxcgw0Og1cJ1QGrMJZBCobXTVV0mzUkzo5I7r-T0vMClEuQTJXUhd6M5TsC9xU5pqtGy_P43VX-iZuXUXDsCwxZBZB03-Q3Q7e0sVqa_VlLhag6n_H2PXlHO8IdIuwmLX1WDAmrpBx68qf8mLwqV20UUqzKFtCAeejOsNQ-_eo3HVrjsnOEGcJdmjz8l0l9i_ln98hKPv-xA07FiKahDMSNRKGlFiN8uy2X1i36LpRxJQ2rFSvtAZMGAp3lEhqye5JNlZJDP5Kdd89lnqxaIo8AIPDMg7ZeWee5NRzSWt-w3IOmCcLK7vlgL-bQHTmhir43QcfxzAQT5HB8HLwhdA6r6c-wjFC86buWgFKlftg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d81ff4ef1.mp4?token=bjc4NjpMm9qYenhPQc5aLLH47bUuWpI7q35c6PrHCgLYdN9CST2mxS5k3VFmEl_M8HFCjAxzOTfb9IqACihdjJfkRlt3VYeQh6sfoPXzZu9aKwlCf1m7X0gizaZ0rVeeZi4rbM9At-r7vGCB6oUi8LBrEABxKtEr7Y0CRqLE7wxWF-J6WXXphOwANlDsDa4ZioMcVukgqcosAa7QBbtx0xvyPF571xpE80mwpwgDjgV_cDZWllilLKa_EqgzDtHxhDvW-KXCML6jEYRmjOjFPc9G_F8b1oIDcW8Cb8mTj-z_IcwBy3I7mARQV_Zaixtx5Pxcgw0Og1cJ1QGrMJZBCobXTVV0mzUkzo5I7r-T0vMClEuQTJXUhd6M5TsC9xU5pqtGy_P43VX-iZuXUXDsCwxZBZB03-Q3Q7e0sVqa_VlLhag6n_H2PXlHO8IdIuwmLX1WDAmrpBx68qf8mLwqV20UUqzKFtCAeejOsNQ-_eo3HVrjsnOEGcJdmjz8l0l9i_ln98hKPv-xA07FiKahDMSNRKGlFiN8uy2X1i36LpRxJQ2rFSvtAZMGAp3lEhqye5JNlZJDP5Kdd89lnqxaIo8AIPDMg7ZeWee5NRzSWt-w3IOmCcLK7vlgL-bQHTmhir43QcfxzAQT5HB8HLwhdA6r6c-wjFC86buWgFKlftg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری شبکه ۳: این تیم پیر دفاعی، ابزار بازی جسورانه با مصر را ندارد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/alonews/130320" target="_blank">📅 14:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130319">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/guLa4wcWgNImC7aZfkwd5KSBSw7Y0e7WSqme07nJa7lg1cSN4_hzcFHBSeuXzwbepxUjqTjbs3r7JSvP9N9JmH34pOzZjrvSwL5oGhSog264WIU87IFiHCuiZy1aPNKD9jmmc5A3Yb-ILJse7TFz0Dd-TiSl6MzdTtpUdbz7BMmu25ePFPzqadiOWi0U6vDXE995sP3-G3XVuGgZGNRaMvvjxbcg1uyDYmL4wPlj6TlpN7MMbAYZBEoZiGagGWO6sLR1cHESwiYxFaHl-a4OFDvPRGZLhGM_ubN25u1FCIzu2YRUs85CT5EAssNm1akXixw_Iz_F0eYLbNTWxeTQzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آغاز پروازهای فرودگاه کیش پس از ۴ ماه وقفه
🔴
پروازهای فرودگاه کیش پس از چهار ماه وقفه با ورود نخستین گروه از مسافران و گردشگران در سال ۱۴۰۵ از مسیر هوایی به این جزیره آغاز شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/alonews/130319" target="_blank">📅 14:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130318">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
سخنگوی ارتش اسرائیل:
در طول این هفته ، بیش از ۱۰ ترور در غزه؛ ۶ حمله در جنوب لبنان؛ بیش از ۱۰۰ بازداشت در کرانه باختری داشته ایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/alonews/130318" target="_blank">📅 14:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130316">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4BE3f3JfiTYipIIzbJNKa_lwckT78eokY89-d-lAwNejfV__oCU_UdYtPxfd5ErfZmwGy8-DeAzVONazwc9gY1dNGL7zDjXqE6lSv67rZutFVHb3p2w0eLYhnrrP59A2ja9OupnEvYSxjXRhcUad2CMDqAA0yNaAuOWni0i4GrBWJYGLlbHQWKP1J3Or-LNMsCsytjvyOIa1kgGQTT02ZRrO-uDrj3c5_fe0nOpmPOtHd5CgAkTdzHAH-lLyTNP37zhC2mriHSZJ6MFO-gqkX5vwDA5u0xd_s0WH42VqD2sbGzOJsyYD30uXTJNhDELeaB31us73SeSDLzckzi-3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قاسمیان، موسس شِلتر:
مذاکره‌کنندگان وصل به شبکه یهود هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/alonews/130316" target="_blank">📅 14:24 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130314">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52da7df95b.mp4?token=dGF0eoNggcyMUKU5xRdT8aTae5i7iByXw6aj20a_81wFR2KwpQEZgjUIpLyta0sFe_5usO6um3Iicriw4njdZRNh73xwK8g0t8a7OuPj8ztcMtcL8YnYnlAqNsJj76CTYfeMQ0VaYDnn3KoLkwiGME_6ElzihhZxbqqv7YM3mYFNASf9r62Z6PFT70kCI3dCSxiFywenFU4b2ZL8cCVazEkt7iyNrK1FLOorXPpwYncuKh9R2YxP28WpWz1tUuM08zkB67LHY1n0ZmlR91_O8aZQwNPtVbfCodU7mQM4ZARYo6UKYGBEKZiVvy4MHkm6KujeVTqet_ZDnd5CbX_7Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52da7df95b.mp4?token=dGF0eoNggcyMUKU5xRdT8aTae5i7iByXw6aj20a_81wFR2KwpQEZgjUIpLyta0sFe_5usO6um3Iicriw4njdZRNh73xwK8g0t8a7OuPj8ztcMtcL8YnYnlAqNsJj76CTYfeMQ0VaYDnn3KoLkwiGME_6ElzihhZxbqqv7YM3mYFNASf9r62Z6PFT70kCI3dCSxiFywenFU4b2ZL8cCVazEkt7iyNrK1FLOorXPpwYncuKh9R2YxP28WpWz1tUuM08zkB67LHY1n0ZmlR91_O8aZQwNPtVbfCodU7mQM4ZARYo6UKYGBEKZiVvy4MHkm6KujeVTqet_ZDnd5CbX_7Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلم وایرال شده از صف نذری تو الهیه تهران.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/130314" target="_blank">📅 14:17 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130313">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c4fae070c.mp4?token=SWm6qC8mo3b1QfAHd6w6PrYN8d9KmHDXEYRaNZ61m1q9a-fUdoofpGG2hFblz9owsbm0YTs_CbxRYXLKKaAWkMCVZLbQnaWmip5UZwTvH5hPiPvQ2t-Che5guNREVbhWJpUFwQROqLVX0xks0IEmRK3Cj7Fd5y9U7FFrrKeJfwtIvtSUW8NdyOJLnpS3KQsn7ixy-9DhxN9svxvJ83G2vKPtg3GzdBcbH5GOJncpXnJYqNGgJYdnDP8caU_QeOo1pDUTUIBtRTuXxJXGCMKzniX4WJB9HKYPmFdgPgmen2Xkuh3_Zb--5Fx90_pc9PLbDOXj_44V0_LiP-SCr6nkRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c4fae070c.mp4?token=SWm6qC8mo3b1QfAHd6w6PrYN8d9KmHDXEYRaNZ61m1q9a-fUdoofpGG2hFblz9owsbm0YTs_CbxRYXLKKaAWkMCVZLbQnaWmip5UZwTvH5hPiPvQ2t-Che5guNREVbhWJpUFwQROqLVX0xks0IEmRK3Cj7Fd5y9U7FFrrKeJfwtIvtSUW8NdyOJLnpS3KQsn7ixy-9DhxN9svxvJ83G2vKPtg3GzdBcbH5GOJncpXnJYqNGgJYdnDP8caU_QeOo1pDUTUIBtRTuXxJXGCMKzniX4WJB9HKYPmFdgPgmen2Xkuh3_Zb--5Fx90_pc9PLbDOXj_44V0_LiP-SCr6nkRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حسن رحیم‌پور ازغدی: تُف بر روزگاری که رهبر ما را شهید کردند و ما از صلح با آمریکا حرف بزنیم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/alonews/130313" target="_blank">📅 14:05 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130312">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
فارس: درب تاسیسات فردو، نطنز و اصفهان به روی بازرسان آژانس تا زمان رسیدن به توافق نهایی بسته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/130312" target="_blank">📅 13:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130311">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pxzh90W2lRKcnhzrSolfZLHRaM_mkjTtNww6URi1hEiNtMnwbU07paVrqDv_QKwLVkvvMY8rY42x8CdtdHc-IGN6DgliH4fF1q5R1CRZ3EqWrPTJZtG2vPppMXLc8reD8QZOBLHBQnXjV5rBcKXPaIuNtlA0zytotglDvalMMMAUCr-kKPrqcqiCCGmkCNGoAfpngzEB2nVcChWyo8Dyz2BPy4fPOSmfznPdWfgwLsSyDVk7spAVlnvAowLl0eqoC59st44YZeTjUlvi6Dx7qNQwHIdB1MbEHPhQfcVyldGGkpR9gJHUJpmRitU_eTGDARikRTN1dAeqQO7DqK62Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ :
ما یه بازار جدید داریم که داره شکل می گیره و اسمش کشور دوست داشتنی ایرانه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/alonews/130311" target="_blank">📅 13:44 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130310">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mxDL0QStG0axoceWQ3Za1bzQZ4VYLHo0vvsZegMAT10ujhe3epi7oe5BupGpndxUM08NH6-Rp6hhfzytgfx5mICf3gawdSiioAYKYZc0hpzZ_FetlNTfV8KGtZQAyGBXcZ_KmztEbNB-1poXDTr_I0TxJhmDHp1Q_DquRJeyPWjA40BDZYOtQdjz7cdBIvDNe0trR7UWj5nDnDJNAxwCL21h3Ic7SOuOSC4WyUzVX3a0zPbpff2SK4eihOyPrsp9yjbPfbQRJ_gRN_MtjExPNX_vi_ppKzvJfR3Nw8tZVh_JkxdU5BIpiE4_HCFPYcKZ-ZAroGl6myBbg-lUjykEDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روحانی: امام حسین هم روز عاشورا رفت با عمر سعد مذاکره کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/130310" target="_blank">📅 13:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130309">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bfb3904efc.mp4?token=EkrzbwW8E64jp4bDHov0KF5eNMD8BTTzMmtYe6WGJyxHHWX_vKDv5hdwkYA8T4EdCz6XROlMuaN7BuI7Jo3tMZMbThl20WXAAhdkOv1rF3jXx7rh9KUoq3O9-wYuN_0h-LNyFo0A6haKiXND6bvYNYvyhiAq6q2GZ1fAcUp3PGF1sFwxyfRoF-GZhzppq1Fww3gUVqTToAv_4xOBXbbWSinOC_LsOADgscqFoHthZufvdMLOROJ4XnKMg_SZVL3rjKNLL--FaN4d-qfzxh1MAKjKlvN3mnHHJlqs6IWif_V6DCxmBKUXAO_Kv7s2c2NPFBTJOGLOKGi5MwM8-77rHA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bfb3904efc.mp4?token=EkrzbwW8E64jp4bDHov0KF5eNMD8BTTzMmtYe6WGJyxHHWX_vKDv5hdwkYA8T4EdCz6XROlMuaN7BuI7Jo3tMZMbThl20WXAAhdkOv1rF3jXx7rh9KUoq3O9-wYuN_0h-LNyFo0A6haKiXND6bvYNYvyhiAq6q2GZ1fAcUp3PGF1sFwxyfRoF-GZhzppq1Fww3gUVqTToAv_4xOBXbbWSinOC_LsOADgscqFoHthZufvdMLOROJ4XnKMg_SZVL3rjKNLL--FaN4d-qfzxh1MAKjKlvN3mnHHJlqs6IWif_V6DCxmBKUXAO_Kv7s2c2NPFBTJOGLOKGi5MwM8-77rHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو یکی از مراسم محرم، شیر تعزیه افتاده بود دنبال یکی از لشکریان یزید، که یه لحظه جلوش رو ندید
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/130309" target="_blank">📅 13:28 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130308">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
حزب‌الله: با تفاهم ایران و آمریکا، ما به یک پیروزی بزرگ رسیدیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/130308" target="_blank">📅 13:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130307">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kUtJGCIhh5Dkbfbaz-aoJWDbnKbaECgKy745tQXEmbY9m7217EUIgs-Rp5wIGa40VEhFN116CFnSR-o9LmNCk141CHpVVqJps-6lwBlULZE9xo_aebqmyjcHAuCqRzy1DwmbpZ6SyqcjYMmcVNohSAIudPtt3C75LzEzBQWV_5zLD_yL7OPF6U4unr_t5jsjRU4_Ox7SEHMox05JwMZOOcWxOm4Y1fU7kvk7vUMc5YCJU5g3GMyf6YUMOkonDt3kMa6aaxxJ4JQK1beJIWlLnUYBOAFcGnN17sNCBqnOARVqsXFfw9ToGtvbCwnOivDgIDrgVbF1U03Np-mzCz5kQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شبکه ۱۳ عبری به نقل از یک افسر ارشد اسرائیل: فروش جنگنده‌های اف-۳۵ توسط واشنگتن به ترکیه، آزادی عمل نیروی هوایی اسرائیل در خاورمیانه را تهدید خواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/130307" target="_blank">📅 13:12 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130306">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
قاسمیان: به تعبیر قرآن باید اینقدر با آمریکا بجنگیم تا صلح پایدار برقرار شود
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/130306" target="_blank">📅 13:10 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130305">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99cd497f75.mp4?token=QQBK4j4kbNnbA2F8oOzMJ-3jgF9tfhVYKB1bRw3dzVmfq2xebIKK4EGBamNg9tUndtE775DbZ9bmkODR43UQh2xxbXzoYjGDOEEGgH1afN3ZFsc44ZJejA9UV0Ps8JJzYvPBdomCCwJ_t1glJtHCAxMUF0AW-S1EXRxKCVKD7aGFTwEpS3vEhzJCXsv1HBubXD62e3SeBPU4gDXkfKBArPnLkUQ3ctYE-KC_s-bA9i8TtOt4gyyWitHRtIRJy2okAVtW_ZxQ-DKeOsTP0RM8U4wLJ5B26p7l_wcSXTWIyEjZSAMiXKFdw-LbKKr_cRBVbF2V1oLNhebvchd5FMftkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99cd497f75.mp4?token=QQBK4j4kbNnbA2F8oOzMJ-3jgF9tfhVYKB1bRw3dzVmfq2xebIKK4EGBamNg9tUndtE775DbZ9bmkODR43UQh2xxbXzoYjGDOEEGgH1afN3ZFsc44ZJejA9UV0Ps8JJzYvPBdomCCwJ_t1glJtHCAxMUF0AW-S1EXRxKCVKD7aGFTwEpS3vEhzJCXsv1HBubXD62e3SeBPU4gDXkfKBArPnLkUQ3ctYE-KC_s-bA9i8TtOt4gyyWitHRtIRJy2okAVtW_ZxQ-DKeOsTP0RM8U4wLJ5B26p7l_wcSXTWIyEjZSAMiXKFdw-LbKKr_cRBVbF2V1oLNhebvchd5FMftkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قاسمیان: به تعبیر قرآن باید اینقدر با آمریکا بجنگیم تا صلح پایدار برقرار شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/alonews/130305" target="_blank">📅 13:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130300">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nlKyexjd-RAY5yi_rwnUVGuTsgbDcb-xS8IGMiqwPO44I_ng4NKuPIgt_fgMmddPGCAv02XqW8Th2dbavTempegaJR-MjOkx3kU-j425Hd5XZYpmoBKzlPKZd13aSnky4Brjk63tcfJwi9kAh10drzhfxAPq1RWVyq1rn8Rn00GsGYlPHsN4EFAnkmmos3qd-LxjJ-_Rqri9lJefYEnUq3_S5MAPtRJkdSYdTVEPMlZNdkD8P4YPVni4nOAFRYpSdj31geIyJCn79vxYKpJqqyN0GA5s-pZ02jWGodaBrxQNa5ANUiuxDRvVEIXaoYvs8vXvGKN4ArHgdFZcOPlHhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O1lUIItBCAEft-3vgJXpwdeTDyMljuV5iG0rCQDFl9_73ip86iluCy0ARtBzEv9HaAnPZ5qDFxB186ZulE043Yxas_zbsDvu7faGjF7xOZm0sHHISn_8Bv3zdfy-rx2YfBk26oqmEhsmXfbV4uiwPkuTWlw2YtkwnYaGdHObd8Hp1mpoK533SE3Ufwt1fj3ITK00o__MM8ofPomZKtLV2SDIWhTJoKtum5k97r-KZo2yiD-UgRYapIX_Y5fySyqRiBJKT6CUBg_HGoWUAihhqw90BcmDMtPyBFNQiOPuYk21k-dZquVFzvQuCI6TwTyIsb0NI2EiJrm00nxWB4wVRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XBJ8u6-eFdtSVD-6lY5EbyU_jiVAwBBcJeeWigkJvrgDASnlJ7RI7_aX3z-K3xs2D4EleOH1abQhZYeiBXiwURWFy5er6v5m7QPQ8yMrZ2TbH8AweRNRoD1V6l--qmx-NMODmdO2-d02Os9Ch4BUeu1iD1ps0RiPVe_WofHwCi6Jk8cM9WI8AnQODQ8OT5lqHsBvTE16abA7uyTcK17Oy4Qpmne2vQ-Zlo1i23iH8tgedk0fFwdYZTNxMxQGhKWkOoQYtzZ0OwANG_9bjB5z-fmOMCqYI2huqPEdP_SYyYXXbaDfEoh3AWjp2D9P-61N0YdSkFZ6kYrIpQusOXKLWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D9pvrQyZjcJXxfg4noqjzjDymaDvbB43ta9GDBxe-Pmpzn6s28jZtjnLlzethzwexMg67IW8TnCy44FrU1GhGDabMryPb3MUMmJts0GKMIuqvm14XCH5lSguxcH7atwiNJUS_jql9H7LkBEIOaiUfaNt_TzPSqnIGZLQTbDwhk8XbGXcEu4zOGvH4CdX2kcRtB116GQ64KfvpQ-eGjUr86mmVCs9JO4PmuQnN2nhdvRcIQvJ3Z4t56-VMDqdG0YMj7DBqMwNJXgidULQ4Ut-_TrEDPOZ4NDQ-mfMqElRGdRgXi45cttY7uo2jkttp7gceLqDjU3FeSvq39Q7suHwIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SJXUaWO7howdl2NgN936ZyOR7R_o7atDOYCD_esb0WBSq2NqCjwYr5yW4suBhesX-Jv9bkotA8HoQp3pGqVDf3nh2a03V4YxeEPVua0mi4wSBT-kcqIeTAWzK2gF_o1HaqPUd1tfj8WiQT_ZWAtHcAvltyDBSeroYdpYuq_N632KAZiJ3KrnkWy4EJaomsg0XycI46kXHKzLOLJCR9iOp6o2NFqbTX57-BAF8G4-gf_6IoRUYVgpYdNAqhSfayMJJQtUfIZFXIskxHup68m4NFvlBR96Si4YaJ2n8he7bTmgrol44Mxo0_ba1JYSS22coq_bVUrDfPQZjIRlbS8UfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر جدید ماهواره‌ای از خسارت های سنگین حملات ایران به پایگاه پشتیبانی دریایی آمریکا در بحرین
🔴
در این حملات، ساختمان فرماندهی پایگاه، دست‌کم ۱۲ ساختمان دیگر و همچنین دو پایانه ارتباطات ماهواره‌ای به‌شدت آسیب دیدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/alonews/130300" target="_blank">📅 12:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130299">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
استارلینک به زلزله‌زدگان ونزوئلا یک ماه اینترنت ماهواره‌ای رایگان ارائه می‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/130299" target="_blank">📅 12:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130298">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
طبس گرم‌ترین نقطهٔ جهان شد
🔴
براساس داده‌های منتشرشده از سامانه Relay Weather، ایستگاه هواشناسی طبس با ثبت دمای ۴۶.۸ درجه سانتی‌گراد در ۲۴ ساعت اخیر، در صدر فهرست گرم‌ترین نقاط جهان قرار گرفت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/130298" target="_blank">📅 12:32 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130297">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ppt7SLp6hfCnzDQ97-f4UhBTt3kF0npcblaD0YGGqpZ6GwvbyDS17SIzGmXLs35_RVybK4t5KXBihaICKi3bxxyVFMclYOozjI1j3Hg2Vulm5H1CNwu2zilBeNxkqjMP5dbvm39lZ7TzkuxtPzbUMGc0RzI1fJOO9oBPNuQMhqWqMcXmmFFGE6nQpzt6Svd5UpOzHLFkrp3pH591t80_QFNZ0N4GEThDT2z1Khlig4xLzIKTj1uf0aMl8SkPfKIMAymceF_1ssSkgnMP1z2l50sWkVwPBRqhupfY3ISriK2OM1sU3ivaLdvBQYunqyX31WLCwLLHtQSVUcAuqvkwKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آزاده مختاری، خبرنگار: سال گذشته بانک مرکزی رکورد ۱۵ ساله چاپ پول را شکست
🔴
پ.ن: چاپ پول، یکی از اصلی‌ترین دلایل تورم در حالی به اوج خود رسیده که کشور ما در ماه‌های ابتدایی سال گرفتار جنگ و محاصره دریایی هم بوده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/130297" target="_blank">📅 12:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130296">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
عراق شایعه خروج احتمالی از اوپک را تکذیب کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/alonews/130296" target="_blank">📅 12:05 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130295">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb2e1ef960.mp4?token=Nk52RDnnHgrgpQpNKuXRBnRrUceGF9UX9SaZkKFAtqkFaJDSzMauCDmbpIv-tppMrKo0lhnR4GKSO0NE8Io1Z6FnKQWmBjEQg0CxpdV3eer0rY3LIJdQniR4dGRC35cz0czeTZut2i5oidgL5IEbqBIlqitOoZdTmzmHMFhic8OcKsgUGBG3iJbbHF2taXQj72fHkiQ3Ldn46-_zP5xr_4zIWOWFHrz9SemGX2CSDLnukNOmtMrcLMlUe8Mh9L4JoBBWOscjfq86wX8Md2R0tW3mJRR_jQtrp-bk3fTFcQW4zKQWNsPh1-xs2_RNSgVfGlZOIiBCYJQ65wyRmE3Kqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb2e1ef960.mp4?token=Nk52RDnnHgrgpQpNKuXRBnRrUceGF9UX9SaZkKFAtqkFaJDSzMauCDmbpIv-tppMrKo0lhnR4GKSO0NE8Io1Z6FnKQWmBjEQg0CxpdV3eer0rY3LIJdQniR4dGRC35cz0czeTZut2i5oidgL5IEbqBIlqitOoZdTmzmHMFhic8OcKsgUGBG3iJbbHF2taXQj72fHkiQ3Ldn46-_zP5xr_4zIWOWFHrz9SemGX2CSDLnukNOmtMrcLMlUe8Mh9L4JoBBWOscjfq86wX8Md2R0tW3mJRR_jQtrp-bk3fTFcQW4zKQWNsPh1-xs2_RNSgVfGlZOIiBCYJQ65wyRmE3Kqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یاسر ، جبرائیلی: اگه قراره با آمریکا ببندیم؛ ظریف رو ببریم
🔴
یه بچه و بساز بفروش و پاساژدار رو به مذاکرات فرستاده‌ایم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/alonews/130295" target="_blank">📅 11:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130294">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pTAR7mKCjs4cEKaCvfYxQmH2YSgsQF_j317P6b1ol1wvI1PTnMbolJjH-8HD61LrY-qH7BRjLkPGoNT2nAAXCpHvlSl4cLNZfZUmDTehrjyODlPwEQ2Jog4jhL4Y66ykSkgfdxbm2gqc43GXGzzst29ri0kAvgqad9nblSdfFM3j6g9LjgGHA5UxHT9Ke7HDMEBIiAg1y1ZE4e_E31SxY40o7X0wpZH89AF_eop5wreK-eC17mooNMMVkAtA-Xqk5vcioGiy0wpuYubIZ5JnqFQxEQSt8iV6y_MzH8S0gK7ArzCL4YQjPNm5tkKXGemjuJ112rQcOgOU6neSIOJU6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی: امام حسین سیدالشهدا شیعیان بود و امام خامنه‌ای سید و سالار کشته‌شدگان انقلاب اسلامی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/130294" target="_blank">📅 11:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130293">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kG9TEV9ahE_7ZS8ArNvSCLLyGiYqTQRcF6JFwHS4Lo-8zCNwUNpKWpWB3Y50Y0S4W8cJcyMK7ibAPXJEz_7OsC07EJRx0G35sRjGCp_YVY4jx-oO8Y7QH9lP8wW_AXkXqP0VE3aQinltchVmFjxNn3A8cN6Okc0ZvjLiBXfHr-wvwAHxtneFtU913StGxLAFaCLBZLLr9yTpXNbO1SjKv8u5n3DWYn891VlTwcm85eHisK_bQMthHjHR2UYB35-ndQEDenL8x7kCLmJwMPKvxLwinBoYA-pYOywrB6qLnSEf09qvL2dP_ByPNlrgIGxdhA53YEOXwSsWXPQNcKqezw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
۵ زلزله بزرگ در نقاط مختلف جهان طی ۳۶ ساعت گذشته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/alonews/130293" target="_blank">📅 11:35 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130292">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
وزارت امور خارجه آمریکا اعلام کرد مذاکرات غیرمستقیم میان لبنان و اسرائیل که قرار بود روز گذشته در دور پنجم خود پایان یابد، برای چهارمین روز طی روز جمعه تمدید شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/130292" target="_blank">📅 11:25 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130291">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
استارلینک به زلزله‌زدگان ونزوئلا یک ماه اینترنت ماهواره‌ای رایگان ارائه می‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/alonews/130291" target="_blank">📅 11:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130290">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
بلومبرگ، با استناد به داده‌های ردیابی کشتی‌ها: ترافیک کشتیرانی در تنگه هرمز روز جمعه در هر ۲ جهت ادامه یافت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/130290" target="_blank">📅 11:08 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130289">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
مذاکرات لبنان و اسرائیل در واشنگتن باز هم تمدید شد
🔴
این مذاکرات که پنجمین دور گفت‌وگوهای مستقیم لبنان و اسرائیل در آمریکا است، قرار بود روز پنج‌شنبه در سومین روز خود به پایان برسد، اما اختلافات همچنان باقی است؛ به خصوص در خصوص نحوه عقب‌نشینی ارتش اشغالگر از جنوب لبنان که تل‌آویو همچنان بر ادامه اشغال این منطقه اصرار دارد.
🔴
هیئت‌های مذاکره‌کننده لبنان و اسرائیل امروز (جمعه) نیز نشست‌های خود را از سر خواهند گرفت تا به ادعای این مقام آمریکایی به توافق دست یابند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/alonews/130289" target="_blank">📅 10:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130288">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
قرارگاه مرکزی خاتم‌: تحرکات و حضور هواپیماهای نظامی ارتش تروریستی رژیم صهیونیستی در آسمان برخی کشورهای همسایه به سمت ایران، اقدامی خطرناک و تهدید علیه جمهوری اسلامی ایران می‌دانیم.
🔴
اعلام می‌داریم چنانچه آمریکا قادر به مهار و کنترل رژیم صهیونیستی نباشد، جمهوری اسلامی ایران هرگونه تهدیدی را علیه خود تحمل نخواهد کرد و پاسخ به این اقدامات خطرناک را حق خود می‌داند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/alonews/130288" target="_blank">📅 10:41 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130287">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V3-vUIjqLK2pYoDTWykqcoBYjc2kjQfcXO_i95tPhsbSjBCk6klMnHwEVlEQPSTOvEFH9-xQ4sfkOoWphJ7vsg8rTA7RFaEhUaWltZWdZBnIbmvBzjewRl2jlcYtz1zbQx4XcCkTlRFkEgQXrH4r-l0MfgCng5AHdR8uwJ5nDTg0TPlx9e-wcJW7twEhj24gR4yFc0wAGnUsTTDiF57xRu24jl7hGZa7nv1Z5C41mEHZDJXL0bLYEEZS9m_f4C7wd5OWnCp4n_qaiXRI50mSZg_n3gm_JtleSlBf3mkBg6x3kzKfEtyn64u_C87BMXQkEdIFFWeaBrAFDb_xSHNNMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نبویان پیداش شد: مذاکره‌کنندگان برای هفته بعد قرار مذاکره گذاشتند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/alonews/130287" target="_blank">📅 10:28 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130283">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S8iI6HoVqutlJmbFQf8GM34C_nahWMqhlsWpPJeJMsY-d6SRlLJnxHCLIn33_N35_NypMKUOD8IUNwbtzTX31x-5NpPD--1KONvY80h_tfFC3HpgX9l4JzfR4rX_8TZWjzGUayBKEaxIcK7ZbNf4RjpmivHsEps0Zkw6O9Gi6o_GPo38CFxuJLx71ELOutr7J5lelLJCMoCOlUGbUir18iJe_sFN3KrbKVtQ3Akm2xzJtsYc1zTaEaeKzgUythapgl5zvErmc8a8JzR5H038GfrSivHj2V8WSoJh0zAxx-sMiPZbmL_UOBrw-fvZjr4ejdvx60Y-Pcf7owXUnhBdig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BGs97_DvEX82MsCHDS8r_uv_QpUF5lcGbsAP4lBRLcET-b4n5SZ_wRRec9Po7_j_e9W3Y8syI5Ox60AwageHOAYHipURlJYHpff8Lt8NQOMaelQ8yxsr_g9H966nuwN4BC4rYVsiIn1hdaiKIClZC1vyMJ5UEriSajBfRwwQoADbOUD9JR64aswXS2qXsx6jHrHFG4kEB0R_WtKLDT6uKvw6B5aJUGMRF0Yrq2EqTAaLq9oebLny3i-A-TLgkxKcz7EzVjx9lQGjOCY43iGNRiJ6j9Aqh72uzzg5PODgmGuba-9gz98hkdnWOuFehD9A_rC85QHtnti4WfBDGyTl1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sxSTBRs-mqO6X6WtOvRFh0RybTUAKgtTR7ZvcPOf6P_BDi7mN6qka10KDCcmN2zstMp7RSWbDhjFPcGBI0gL9Hf3_UV5j-EGwEFQxRq6lCZ-K8LFUr4OoWFwQNO6i8HePkNTyBdfKOZvDKYtcLPLzzmtT2stIiFcudmIJr1GDOtbvRcgbC9H7dgsvlPDEsVulxV2HMnetqMF_IipYu-FodQtgRuDm7qGhtWvqSmmX9wVdrW-9FHI29VgRyC013TMnxF1LpXJtoDA_k7gW5JT2SKQPFhEINtuVV-lxqYn0yY0e5TnVUzcLr5SXyP_9sJGX8ofLnE5DhuPxY6wAdtPQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FVRD_zq5I92F7uSEHiuvuTbI2v5MXOKoG2i-5T3sAO7CSW633YAmOWIQe_KCsgktPvXCcJhqUSag4jL9GP-6qdMnmgTaHrxGhxpLDYYk_pBZkthOnyIXDazf0L465Aqzf67hR7SYlWo2vCTFJra6j3wS8qvM4nOKNFDGha25xR4zAGtuOJW55UlT_sz6PGux1iNf5ibWrp-cbYHZTqQKiqBmUuJTEBv7cMoGEgSDMJcqvFOkFqoShAu6JQA0NTTlnnvSF_pruiGFNfmsabg7PCN0Jck7qwckW0HIQniMFwR6pInC8ow8zIiSrMq4rDNQZpAVfzrThOtcmHqGtnfPWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
کیم جونگ اون، رهبر کره شمالی، بر آزمایش‌های جدید پرتابگرهای چندگانه موشک، کلاهک‌های موشک بالستیک تاکتیکی و سامانه‌های توپخانه‌ای با برد افزایش‌یافته نظارت کرد و بر لزوم تقویت قابلیت‌های تهاجمی «مرگبار و مخرب» کره شمالی علیه دشمنانش تأکید کرد.
این آزمایش‌ها شامل یک پرتابگر چندگانه ۲۴ لوله‌ای ۲۴۰ میلی‌متری ارتقا یافته با سیستم هدایت دقیق خودکار و برد تا ۹۰ کیلومتر، کلاهک‌های ویژه ماموریت برای موشک‌های بالستیک تاکتیکی طراحی شده برای وارد کردن «خسارت مهلک» به فرودگاه‌ها، بنادر و زیرساخت‌های برق و گلوله‌های با برد افزایش‌یافته ۶۵ کیلومتری برای یک هویتزر خودکششی ۱۵۵ میلی‌متری بود.
کیم گفت که این آزمایش‌ها پیشرفت در چارچوب طرح نوسازی نظامی پنج ساله کره شمالی را نشان می‌دهد و «تغییری در وضعیت آتش در مرز جنوبی» ایجاد خواهد کرد.
او افزود که سیاست دفاع از خود پیونگ یانگ نه تنها با هدف تقویت توان دفاعی، بلکه با هدف ارتقای «وضعیت تهاجمی مرگبار و مخرب» آن نیز هست، به طوری که «هیچ دشمنی جرات رویارویی» با این کشور را نداشته باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/alonews/130283" target="_blank">📅 10:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130282">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
رادیوی ارتش اسرائیل به نقل از سفیرش در سازمان ملل گزارش داد که طرف لبنانی اظهاراتی قاطعانه مطرح کرده
🔴
وی افزود: «هنوز به مرحله صدور بیانیه نرسیده‌ایم، اما درباره مسائل اساسی گفت‌وگوهایی در جریان است.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/130282" target="_blank">📅 10:15 · 05 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
