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
<img src="https://cdn4.telesco.pe/file/GwcQr_z8mE_mkQtDnw5jWt9L1psO7YQ_0l5xpA6-XLcpH9TSxG0ZGYuaLYaUx8D6s1BqYtLhfOkCf7tn2VaxLkTFDmhPkh3F9AnkdbP2_ilmFdI18Iu9Yr60lc_EwlgPo7NwodIO7pGCAUWG6HLkJTsi-9EuTwQIJT-M__8JOZRwUJwnwyAribB-ps5bzuABfT6_24e_A0d079El9JzntVcfZAofKZY_9pcQv72fwMpJACqEBjIimEcT7Xqhjr-7iwD3UrtgLRfS0Y_PX4ae_EjCpujc1uxk_FIZ5dl8Qm_SO3GxoorpByDO_CooiAAeBqhnOq6Miq-Xxx6HZnpibQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 366K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-20 10:37:55</div>
<hr>

<div class="tg-post" id="msg-17380">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اتاق جنگ با یاشار : به نظر میاد خودشون دارن ورودی های سایت های موشکی مسدود‌ رو با عجله باز میکنند ! @withyashar</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/withyashar/17380" target="_blank">📅 10:36 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17379">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KfYDKFQBA4AE5pS3XkcG_iLkoO-gPSQXqTvi94YX01qiMp4ydE-DM1whMOKJLufg6olWzeCNW9gm3YEsHh2_HmZUct31d6FGSDHXbzz00aje-PVfQv5BKAKGOtDPySk6KUqW_ggJh6med47pFIQ7wfSqzz0fvjKHBkc9LmfSzRSPIzvTLxMyjloNnA81p_NCpRvk-6AL4nVbHV5lAsNv2XvVGg33Nman3EKaNgtmNcFNBSFSbety5bTTd2Tr6Vv1w_1boVUA-ykYp22KuSdVNeneWQBdlheblnab9xMHdmNxen-hSbKQgVO368B_VOR4MuubCkdGHO5VM71o--FjIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شعبه پاکدشت
🤒
@withyashar</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/withyashar/17379" target="_blank">📅 10:33 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17378">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">شبکه خبری ABC به نقل از یک مسئول آمریکایی : فشار نظامی، دیپلماتیک و اقتصادی مستمر بر ايران وارد است. ما گزینه‌های زیادی در اختیار داریم اگر ایران از تحویل مواد هسته‌ای خود امتناع کند.
@withyashar</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/withyashar/17378" target="_blank">📅 10:25 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17377">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">اتاق جنگ با یاشار : به نظر میاد خودشون دارن ورودی های سایت های موشکی مسدود‌ رو با عجله باز میکنند !
@withyashar</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/withyashar/17377" target="_blank">📅 10:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17376">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">صدای انفجار تو قسمت نجف آباد اصفهان شنیده شده
@withyashar</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/withyashar/17376" target="_blank">📅 10:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17374">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">لطفا دایرک بی مورد ندید !!! هنگه ! خبررسانی‌رو کند میکنه ! دایرکت جای نظر و کامنت شما نیست !!!!!</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/withyashar/17374" target="_blank">📅 10:03 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17373">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-footer"><a href="https://t.me/withyashar/17373" target="_blank">📅 10:01 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17372">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">فرماندار پاکدشت : صدای انفجار مربوط به عملیات کنترل شده مواد منفجره‌ست
@withyashar</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/withyashar/17372" target="_blank">📅 10:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17371">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MaM-EX1Kced-zxSLSPm-SJDsZh7-lxu2CXEVXFzBBK6e9R5KE_vCMv8bGMdbhiL3RjHgpvoGQHvpfZSUIm-SnoLav7CuWQh8Imk71bmFlHjQPo_eActvtrvyqWd3vtjZpA0kRt5Av0uYSDLWoLAJkeAtmemsgddyOy2acxyu1R1H8ZAK8bMjLPouqGVVGcxsgZQ9bq4Z8M4zw8xrXcLohG1oddAIAd-Ms6tO5IPnItgBwDUGMzxy1i-bNUyPPLvPiNlgmXyPtsG2ZzGP_-dSaH-GyYW5c13s9tcO_KBrgtkp_zoW1DEgUEK7fiT64srdCmXdIi9SFrJq5m-FzwCtEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/withyashar/17371" target="_blank">📅 09:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17370">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IHwjif2eQ1ul70inNLQcegZp4iCzXwhKuFEiESvojvTiOhUvcl__aPSqvH8KzQNto7_k3QMlgV91yfZffHQAcYmSDPRK1W4Jr7zy61auasW4Dk_TW5UK-K7jwE9FmsLDQWlLbQ0kobLNKeQZHpPXQ3KW3rQO8MiAxTnDlzgJMvCRkZMojj_KQxYR6DPRdFYnV_NKO6BzoTANKbilCZEpWF6fi3bZnMWb_xxANZt95CL8soVePnxWGMQbippnI3MU3QEqFQffTYISMHDv25XWuIJqAa0tF5LNt0N7q-U3BjzsG5_kqtCHSVvfvcxwxy9iCxeeSmvO1y-VJ00ZcB1XMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار شدید پارچین
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/withyashar/17370" target="_blank">📅 09:55 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17369">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxlkX11L36GbTucbhQZVJO7EGQUur4dQ6AHglIXzZ4Ct7bwscaDM8UZav_G4ileyRByS_rMWUs5G8DYx2x16kfOyHzN_IHi48dBP2OXSkAKl3wP64_23tj2HbxrvOUvwhrDp-6HQulBDerZTJC9FJKqsVTXkzmHO6MaYRtTS3UYfqqHUR9DWqOkGHD8Oj_L-LjauuefGQfwqhXBq8ba1QmfPqyyS2_IYvsEedLajCQeJpQ3n_F-YZHUusTIFDPVwHyOjWx-ElXVspX7F1PXBxGaQ2tZ2cI8V8_A1m2YlSXouRgU2M7Pc6BjBCu3qrnZV2m4Hv8aMinyj1tndml2jjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار پارچین
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/withyashar/17369" target="_blank">📅 09:55 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17367">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y_m-DqUesofqtp92lNtb0kkZX8sN23SqANK20mNL92NKKWRJe_k6fkF3OILl7dJ7opyB3JFqetKUNYv-qz_ZytR9VRpOfoMMkqBTk72QRrIHc7JU2lNi7ynN_yl3AcfIPVdMm7TCjchChLGH3S6HfXvJeQDJIJlY-GnBHTSVFOgNrjGwV8P2N1nhmyygiEKiKxGkpKCGV8-Kae077E2HJSKuzTNGIuyyObizNSzaXfMVM2rdIxzQp5ZQAGXYbFvHbMLXu-rJgeKBOqEXoL0OmCDty0yrbTN3e8iu_Zvt5kTly1atj7oQVmSKPo6D1aID8yUdmRwxclfb0SvxL4BRCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار پارچین
@withyashar</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/withyashar/17367" target="_blank">📅 09:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17366">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">سایت موشکی پارچین / پاکدشت رو زدن
@withyashar
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/withyashar/17366" target="_blank">📅 09:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17365">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tu0dy4HqGgFTlIp2ySqZBzmORnkVbUiZqADIFoTavevwrry7dk7Z68V1Xtejv-ldsOuf4kG-tksigfL2FRLygEBTJIFSkf87x4Ncvy-g3UzXYQ39wTRCVu06nS2wLTYILC6HGBcgFU4nYJcjeUgOqc0n2ClfeMQPQHWdfs0NL9ypant7nNbwU5xelMaXFD5GsvNi95JPbZda4hgFp2CjOT2EMeDBw16Ue-mSEVBIa0OIDh1cMLw9dYoRVh_p4Cq3K0eiICfDbYLCNxp1kMhyiw5TssOmlzrIgDvQ3Y0_rCjQqeHpRXoi6t5bUwl10H5wKtbGWtTGXbnh9oaA0X-V8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی وارد مسقط عمان
شد
@withyashar</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/withyashar/17365" target="_blank">📅 09:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17364">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">صداسیما: ایران به دلیل پایبند نبودن آمریکا به تفاهم اسلام‌آباد، آماده ادامه مذاکرات نیست
@withyashar</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/withyashar/17364" target="_blank">📅 09:36 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17363">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">سی‌ان‌ان: یک مقام آمریکایی اعلام کرد تا زمانی که ایران اجازه عبور آزادانه نفتکش‌ها از تنگه هرمز رو نده، واشینگتن وارد مذاکرات مربوط به تسلیحات هسته‌ای نمیشه
@withyashar</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/withyashar/17363" target="_blank">📅 09:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17362">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XCTC4Tw6WvHlao6GMOzRGqw8Sm0g3nYo9lnCQ2SFL0d20On1prGNhT_snzY3o6K9xSwto0bmsBgP26DNx9LTxBXMk9txgaW1LPKjXeq6fk6tq-XP_rmrRPyRiMYy2DbWsW-YAyZx6MtYkLtIq57TNK9wwZ0GsxJzoL9HzCWqEF2y2oA-GoO1_0SyHnZf_DXUmPsxR5dQS0jXomk2NIfMcvCQMsfiEbumqcr40JMv6nmw4PXisqevN_kaHIuGzJ2CPUlAuItTbDRTn-q-2ZOoX6WirvmZ42sTSY4Tc9b_qezQk8uFYiLxMsJq1bUVSmTHvRJCDWlIpxziV3iHvkrYoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ۱۰۰۰ موشک در حالت هدف‌گیری شده به سمت ایران قرار دارند و در صورتی که دولت ایران به تهدید خود مبنی بر ترور رئیس‌جمهور مستقر آمریکا که در این مورد، خودِ من هستم عمل کند، شلیک خواهند شد
دستورات از قبل صادر شده است و ارتش آمریکا آماده، مایل و قادر است، برای یک دوره یک‌ساله که قابل تمدید است، همه مناطق ایران را به طور کامل نابود و منهدم کند
@withyashar</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/withyashar/17362" target="_blank">📅 09:33 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17361">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">هم اکنون حمله اسرائیل به جنوب لبنان
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/17361" target="_blank">📅 02:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17360">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">سی بی اس : ایران در گفت‌وگوهای محرمانه به مشاوران ترامپ: در هدف قرار دادن کشتی‌ها در تنگه هرمز اشتباه کردیم
به گفته مقام‌های ارشد آمریکایی، مقام‌های ایرانی در گفت‌وگوهای محرمانه به مشاوران دونالد ترامپ اعلام کرده‌اند که هدف قرار دادن کشتی‌های تجاری در تنگه هرمز «اشتباه» بوده و این حملات از سوی یک جریان «خودسر» از تندروها انجام شده که قصد داشته‌اند روند مذاکرات را به شکست بکشانند. همچنین ایران تأکید کرده که مایل است گفت‌وگوها ادامه پیدا کند
@withyashar</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/17360" target="_blank">📅 01:03 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17358">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">باراک راوید: دولت ترامپ به ایران 24 ساعت فرصت داده تا به‌صورت علنی اعلام کنه که تنگه هرمز بازه و متعهد بشه حملات به کشتی‌های تجاری رو متوقف می‌کنه؛ در غیر این صورت، با پیامدهای بسیار سنگینی روبه‌رو خواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/17358" target="_blank">📅 00:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17357">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGazy3FUZlRdf0JED0wU95KAyW1ZaICLANveURd35GRfUM3YR4qIfx49-B6pDUt89IoPUeMcxk44iYRw04eirWTtKzxxHnRhA2eK6islX8S080_jZRZnECxxuNzJyjEVNkoz8YzuNA9-c-LdQupn_poQOW-wPDigibbUPt6SmsRqYSdWDzEPlx5o6QgINM2NX4QZGxsD4GWNlC_zw85s_lokA7Fb5w5QfPbcnpj9ImZuAxcbKu0RtptD92Vz6Ftbnec-AVDnW53spm0na0CtK_vBgIiM27hbyeEP0QaS0l_0cbyeiGq1B5Hwj1jgxqiZhcWLWhHm6nxy5ts2hvnnTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو : من تو جام جهانی طرفدار آرژانتین هستم.
@withyashar</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/17357" target="_blank">📅 00:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17356">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">فوری | بر اساس گزارش نشریه "اکسیوس" از مقامات آمریکایی: دولت ترامپ از ایران خواسته است که شنبه‌شب بیانیه‌ای عمومی منتشر کند و در آن اعلام کند که تنگه هرمز باز است.
@withyashar</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/17356" target="_blank">📅 00:41 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17355">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d3fe5b208.mp4?token=f66i1c3QYG2DhrqI6aTB5S7Y50QipEYuuTkbcdB_wx0qWBegUTbe7kOCn6x5e3dF6tLq3rTNquC27iMBKYeTgqGVgYtzoHK8yGezqV0TEvmgiNzHaK3wg__-5p6GGOCJxwYJwM6qpEjCASCjJVQBtZxtoO8UCfDNUqaHomN660kL53xvT0t35VV8eMVesCh6bcUGu1XdSDjccklkM2AnUMIKU72bm86_7rVUIREeSXt1WR2wPriO3eYW8WK09Yx_kryiIB226F8Y9TNeI05BY1w_mi8a5BJ35GL-cCv8_01k9fKUME8NUaVyMpzM0LKArhQ41Vj8TIu-0B1_hYqdAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d3fe5b208.mp4?token=f66i1c3QYG2DhrqI6aTB5S7Y50QipEYuuTkbcdB_wx0qWBegUTbe7kOCn6x5e3dF6tLq3rTNquC27iMBKYeTgqGVgYtzoHK8yGezqV0TEvmgiNzHaK3wg__-5p6GGOCJxwYJwM6qpEjCASCjJVQBtZxtoO8UCfDNUqaHomN660kL53xvT0t35VV8eMVesCh6bcUGu1XdSDjccklkM2AnUMIKU72bm86_7rVUIREeSXt1WR2wPriO3eYW8WK09Yx_kryiIB226F8Y9TNeI05BY1w_mi8a5BJ35GL-cCv8_01k9fKUME8NUaVyMpzM0LKArhQ41Vj8TIu-0B1_hYqdAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام با انتشار این ویدیو نوشت : ملوانان آمریکایی در حال انجام عملیات پرواز شبانه بر روی ناو هواپیمابر یواس‌اس جورج اچ. دبلیو. بوش (سی‌وی‌نی ۷۷) در حالی که این ناو هواپیمابر در آب‌های منطقه‌ای در حال حرکت است.
@withyashar
ناو بوش و لینکلن در نزدیکترین حالت به ایران هستند</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/17355" target="_blank">📅 00:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17354">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aa058f243.mp4?token=mKkj7GK_x1tH7hk1zoYahtTV0xNo7_eC8aBSOWXn55OKHOroTvuNw13wyyWicTAOUeiUZ2u_D3GjDVxBqYPbeNNpBwluvXGxI1OH1_OwbQJEm-Rdae_h-0BVNJGV7CDteMknL948Iy4CpvaSMpZmAVaqbZcDjU4Jq8MgcunbwbUFtXi4SuO-z6Jv_sqtXOmyILN2c6xgaeBj-bcfwRICTb_FfJXXNhOwZzLFtEgpzuNlXZrVTAbGp1ZRIDgiCbXO9v4Wdypw4dgK1xiZj5C2_GJl0aKGZ31JrVa34NmI0FnVrvPM_unjBxGttdalKVabcSUejCPm2offPAzCwlKTLYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aa058f243.mp4?token=mKkj7GK_x1tH7hk1zoYahtTV0xNo7_eC8aBSOWXn55OKHOroTvuNw13wyyWicTAOUeiUZ2u_D3GjDVxBqYPbeNNpBwluvXGxI1OH1_OwbQJEm-Rdae_h-0BVNJGV7CDteMknL948Iy4CpvaSMpZmAVaqbZcDjU4Jq8MgcunbwbUFtXi4SuO-z6Jv_sqtXOmyILN2c6xgaeBj-bcfwRICTb_FfJXXNhOwZzLFtEgpzuNlXZrVTAbGp1ZRIDgiCbXO9v4Wdypw4dgK1xiZj5C2_GJl0aKGZ31JrVa34NmI0FnVrvPM_unjBxGttdalKVabcSUejCPm2offPAzCwlKTLYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا این شکلی شده
💀
از کاباره تا کان پاره
😂
@withyashar</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/17354" target="_blank">📅 00:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17353">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">سازمان بین‌المللی دریانوردی خواستار عدم به رسمیت شناخته شدن حاکمیت ایران بر تنگه هرمز شد و تلاش‌های ایران برای این کار را محکوم کرد
@withyashar</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/17353" target="_blank">📅 00:08 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17352">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">رئیس ستاد مشترک ارتش اسرائیل در سخنرانی خود اعلام کرد:
احتمالا عملیات‌های بزرگی انجام خواهد شد، برنامه‌های جدیدی در حال تدوین هستند، انتظار می‌رود جنگ مهمی در پیش رو باشد، آماده باشید.
@withyashar</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/17352" target="_blank">📅 23:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17351">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">وزارت امور خارجه ایران: اعمال تحریم‌های جدید آمریکا علیه افراد و نهادهای ایرانی، نقض آشکار بند ۹ از یادداشت تفاهم است.
@withyashar
😁</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/17351" target="_blank">📅 23:55 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17350">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">منابع عبری  : هم اکنون تحرکات نیروهای آمریکا در تنگه هرمز
@withyashar</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/17350" target="_blank">📅 23:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17347">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا:
به اصطلاح “رهبر معظم” در انزوا پنهان شده است در حالی که رژیمش در حال فروپاشی است.
ما این پول‌ها را برای مردم ایران حفظ خواهیم کرد.
@withyashar</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/17347" target="_blank">📅 23:17 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17346">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">خبرگزاری CNN: تصاویر‌ ماهواره‌ای‌ نشون میده که ایران داره تلاش‌ میکنه که تاسیسات هسته‌ایش رو بازسازی‌ کنه.
@withyashar</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/17346" target="_blank">📅 22:52 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17345">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">اسرائیل کاتز
: خلبانان تازه نفس ما منتظر موج بعدی حملات هستند
@withyashar</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/17345" target="_blank">📅 22:52 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17344">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">آتش‌سوزی در نیروگاه تبریز، استانداری آذربایجان شرقی ادعای حمله خارجی به نیروگاه را تکذیب کرد
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/17344" target="_blank">📅 22:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17343">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ef2410203.mp4?token=nP23_su4syOMD2K_b0ZbUEcKgYmAdEWq-QC-5yVaQb5M5Jd6x3uemxzNQiD6K5XSw3nkLxtAjxOKQweAYTE7VcQBfc-4QnRpKKl3kgzztAMDmm1Mi0JNG2FCSiEAC-43LtOAapVbtmjRJIvFwn3L_7tNDyYKOld2j9ryiKr5-i3nrBjlI5sawYsShsR0DXVBolDJx5H07r_uCc8S3iampuLeKvndsHhOkY-_Fcirgqa5CgydUnyQPeBcYc1zdxA-3BWRssQeVYhQ0zGplp5Io3aYeQd4Tm6pcrRuUV-2TgIVSHcCUF-ZQG2mOuZvDsBxuYuflrWc2_Kc4LL5fRtxdoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ef2410203.mp4?token=nP23_su4syOMD2K_b0ZbUEcKgYmAdEWq-QC-5yVaQb5M5Jd6x3uemxzNQiD6K5XSw3nkLxtAjxOKQweAYTE7VcQBfc-4QnRpKKl3kgzztAMDmm1Mi0JNG2FCSiEAC-43LtOAapVbtmjRJIvFwn3L_7tNDyYKOld2j9ryiKr5-i3nrBjlI5sawYsShsR0DXVBolDJx5H07r_uCc8S3iampuLeKvndsHhOkY-_Fcirgqa5CgydUnyQPeBcYc1zdxA-3BWRssQeVYhQ0zGplp5Io3aYeQd4Tm6pcrRuUV-2TgIVSHcCUF-ZQG2mOuZvDsBxuYuflrWc2_Kc4LL5fRtxdoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انرژی بدید امشب غده سرطانی رو بزنه
@withyashar</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/17343" target="_blank">📅 22:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17342">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">شورای رهبری یمن: از رژیم ایران می‌خواهیم از استفاده از یمن به عنوان میدانی برای درگیری‌های منطقه‌ای دست بردارد و از تشدید رنج مردم یمن جلوگیری کند.
@withyashar</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/17342" target="_blank">📅 22:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17341">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vbf7psvqLqQ_ljs1JUuxK38HRi06Nu_0mP99sWrenxPSheP9YZn7ZsLAv-n1AyTYR7Sw82e_XgNVwGHB9Mf7a6huwU1vKVXZ-kM5UNQ-bfVYfT014NWWbGZI1d-lmB9qPW3SEeGWsVsErYAuVcpfsqBsjvCyhUGGxOpBCiFYjXD3N7lBEi73X1N5EJYmKLp5V1T9NREoJ8jvNFWIpJfiWEfwgXvpXPz37QdSqXq3W4SJ076NWrBKLh3KPweVE_cjeejtfoSJJdDmqJYH5tf1Fi3OJVJ8abs83525KYUk_FmfssQnJdC7en_Gv5o7ghTuD3vFNBXCF9IPCTalrUvlQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستون دود ، کرج الان مثل اینکه یه چیزی هست که کلی پیغام اومده
@withyashar
به علت تاریکی زیاد نور تصویر رو خودم زیاد کردم</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/17341" target="_blank">📅 22:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17340">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">آخرین فرصت , طبق گفته رئیس اطلاع رسانی آموزش پرورش فردا قراره جلسه بزارن برای تعویق کنکور و نهایی
@withyashar</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/17340" target="_blank">📅 22:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17339">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">کرمانشاه الان  @withyashar</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/17339" target="_blank">📅 21:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17338">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">بند دیگری از قرارداد تفاهم ایران/آمریکا به فنا رفت
وزارت خزانه‌داری آمریکا تحریم‌های جدیدی مرتبط با ایران را اعمال کرد.
@withyashar
یاشار : این تفاهم نامه رو رو دستمال توالت نوشتند !</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/17338" target="_blank">📅 21:53 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17337">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44bd1cd0af.mp4?token=wCDQW_T4bCXdN-Vqc2dMAZAKTYVIrRrBbRl_Ad_suiP7px-uQnzl0ZteKuY0hrj7ehq-px9ST3XyvWZ0B-Gl4sPaNC-XwdEGsk_rtMp_OKqBBkusnoJwehGlgH6mLc0P-MDmCzxeFPrz1XwcIBiZjnugupz8xUPm9-0XELa8RQ-d_BKR3aAba0jExgG5zWAWVhM2vBUQYt-bUr68YCrjzaQvXFUVNmUQqrC10RPD3gv4rc-DvtomSam5iVO_j_oU8HADb0U7WdPKZys5_7ndphSCz-cDIBiVmJMS_EBSQ5H8nNjAGWr30o9ih_QngfmAWd6mnATVm88Tw9QxbgSoEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44bd1cd0af.mp4?token=wCDQW_T4bCXdN-Vqc2dMAZAKTYVIrRrBbRl_Ad_suiP7px-uQnzl0ZteKuY0hrj7ehq-px9ST3XyvWZ0B-Gl4sPaNC-XwdEGsk_rtMp_OKqBBkusnoJwehGlgH6mLc0P-MDmCzxeFPrz1XwcIBiZjnugupz8xUPm9-0XELa8RQ-d_BKR3aAba0jExgG5zWAWVhM2vBUQYt-bUr68YCrjzaQvXFUVNmUQqrC10RPD3gv4rc-DvtomSam5iVO_j_oU8HADb0U7WdPKZys5_7ndphSCz-cDIBiVmJMS_EBSQ5H8nNjAGWr30o9ih_QngfmAWd6mnATVm88Tw9QxbgSoEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کرمانشاه الان
@withyashar</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/17337" target="_blank">📅 21:50 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17336">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">حمله کنکوری های کرج به اتاق جنگ
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/17336" target="_blank">📅 21:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17335">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HorChGH2VMn_dTmI7QSNgYuIE3fnnHdXlzVdBH1Jf4r-tabkJiWg2vvUAxuJhwFmCE8bySfWvzWLOKYaGFBXnLLbTLmNPoS7chaUHmPmbIAxM9TKB8djobOjtqTE-ws2xZEHVU1_nVcImgyLU2HrrpoG7ZuKN2uKdIPrKd9gzl60rpMu0WDm17XUs4mNDnNVJBXvo80rzbLGFzKKNcii0uNcWV5NT5fcuD2r9wT3MhRtIoHomxJ06ESU-vmN1BfpZtTf9V0B5sABk7F495XoGrNi-BmIlvUUnGcRZxWD5G2ALMSYuAKHS-sxUd32zwouMgdODfwLBJfO__hJUL2nug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرم‌ترین شهرهای جهان تو 24 ساعت اخیر
@withyashar</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/17335" target="_blank">📅 21:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17334">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">نیویورک تایمز: ایالات متحده و ایران در لبه پرتگاه درگیری نظامی هستند واسطه‌ها تلاش می‌کنند تا دورشان کنند
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/17334" target="_blank">📅 21:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17333">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">صندوق بین المللی پول IMF پیش بینی کرد رشد اقتصادی ایران امسال منفی ۵.۴ درصد خواهد بود
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/17333" target="_blank">📅 21:32 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17332">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">تایید نشده گزارش زیاد از صدای انفجار کرج
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/17332" target="_blank">📅 21:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17331">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/17331" target="_blank">📅 21:27 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17330">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">خبرنگار CBS: مقام‌های ایرانی روز شنبه برای گفت‌وگو درباره تنگه هرمز و اختلاف بر سر مسیرهای کشتیرانی که از آب‌های سرزمینی ایران عبور می‌کنند، به عمان سفر خواهند کرد.
میانجی‌های قطری به‌تازگی مشهدِ ایران را ترک کرده‌اند
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/17330" target="_blank">📅 21:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17329">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">تصویر ماهواره جدیدی که منتشر شده نشان میدهد ناو هواپیمابر جورج بوش و گروه ناوشکنهایش به فاصله(۲۲۰ کیلومتری)  از چابهار قرار گرفته  حتی نزدیک تر از ناو لینکلن @withyashar</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/17329" target="_blank">📅 21:22 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17328">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/470c8df2f2.mp4?token=kyQXpxrCxDGuHYf_6g43TeCLDgIHTEPKPJc5Dp9HACMy-Xm-lH3mN8mDysD_wex8eIbKEK-qmZIVaSb9Yp_VwAJltG4Jgjgg3DbjgAGzYHHFdxYjIWRdL_Sevh4F98nLpM4QOyxcj8Hn0g35ICDusZi6WTe8F6019Y6fG8UKIkEOy_tkak-XueYIN_6YfXPcrus44dXYvHLNVtaCwGvI9SFis3jr3REM8Sm9esfGmpfzIAk-wOMQ9Shs5Pv1X92X7jw6TOlUYhtOkqCFQRzn_htRLHpaTgn_2Hpzxa2pT7KdvsVV5xbS47P2-JlIQxeEdyiXtpiow-mQrk5-6wAqyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/470c8df2f2.mp4?token=kyQXpxrCxDGuHYf_6g43TeCLDgIHTEPKPJc5Dp9HACMy-Xm-lH3mN8mDysD_wex8eIbKEK-qmZIVaSb9Yp_VwAJltG4Jgjgg3DbjgAGzYHHFdxYjIWRdL_Sevh4F98nLpM4QOyxcj8Hn0g35ICDusZi6WTe8F6019Y6fG8UKIkEOy_tkak-XueYIN_6YfXPcrus44dXYvHLNVtaCwGvI9SFis3jr3REM8Sm9esfGmpfzIAk-wOMQ9Shs5Pv1X92X7jw6TOlUYhtOkqCFQRzn_htRLHpaTgn_2Hpzxa2pT7KdvsVV5xbS47P2-JlIQxeEdyiXtpiow-mQrk5-6wAqyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داده های ماهواره‌ای امروز دو اصابت آشکار در باند فرود در فرودگاه بوشهر در ایران را پس از حملات اخیر ایالات متحده نشان می‌دهد.آثار سوختگی نیز در اطراف باند قابل مشاهده است.
@withyashar</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/17328" target="_blank">📅 21:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17327">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">اقوام ایران
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/17327" target="_blank">📅 21:10 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17326">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">تسنیم : بررسی‌های میدانی حاکی از آن است که اخبار منتشرشده درباره وقوع انفجار در شهر یا سپاه ناحیه قائمشهر کذب بوده و در زمره عملیات روانی دشمن قرار دارد.
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/17326" target="_blank">📅 20:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17325">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ee9a172fe.mp4?token=oZcKuygmpix4O_P7KySv53BzOAg5M0_P1pIYW-_vwezg4wuz_Qhcgo1IhwJspBISISWojOHENafvm2zBFRsSF2E-NDLHJDyJnSAcy3skwoUiVFM0WzAiqD1zKCL-vNg4xXGmm_qVLLsa_N1Ept57qRg6-ZwHTbqTFogc4-SVvRwXzwrhDsW4fTAg7LVxcH2MmJeUh_cpiIRHxJtyS23aXoLt-9Y0skx5THk7f_JrPqMhHVb9P9mPr-wOprVvtJjxP7kUgHUcjGeTI5d0mCEgEOXT3kULM_Aa4NMUe4A6zqVFNziwag77VyRLW-1FfagCh6o1D6-6VVGyrS5CbfStkqrcZlyzYC9oyrHKN2fEB1VhkX_0xGgBboOfjkqHrMzQI0lNXQJyp7eTZDemMxUiUGxEPRpaXggl85HdoDp9G2ndLe5mirlantQYGUXyJaTAmH743tZ2AEFJ8KVOy_z8qaAnXY5e9mSs4O_5NJfNhP8GV6aHFzdQnGLnUuop5Xpr6QMekb_ULsc6TgwuZYnI5OuxqILvvBbH3etGeOmnuy3BPBPo_x4ILhzdvB2ncEGoTvBQ9f1tgQH41oAgJwWFBLhjoDJa08G1mmgVV37_8q0RiUSUPsAU9ESgcks8CxnF4QozbZPOe9LASn-Oo7sDiIPei_4DrpuDmiEYVFnQb3c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ee9a172fe.mp4?token=oZcKuygmpix4O_P7KySv53BzOAg5M0_P1pIYW-_vwezg4wuz_Qhcgo1IhwJspBISISWojOHENafvm2zBFRsSF2E-NDLHJDyJnSAcy3skwoUiVFM0WzAiqD1zKCL-vNg4xXGmm_qVLLsa_N1Ept57qRg6-ZwHTbqTFogc4-SVvRwXzwrhDsW4fTAg7LVxcH2MmJeUh_cpiIRHxJtyS23aXoLt-9Y0skx5THk7f_JrPqMhHVb9P9mPr-wOprVvtJjxP7kUgHUcjGeTI5d0mCEgEOXT3kULM_Aa4NMUe4A6zqVFNziwag77VyRLW-1FfagCh6o1D6-6VVGyrS5CbfStkqrcZlyzYC9oyrHKN2fEB1VhkX_0xGgBboOfjkqHrMzQI0lNXQJyp7eTZDemMxUiUGxEPRpaXggl85HdoDp9G2ndLe5mirlantQYGUXyJaTAmH743tZ2AEFJ8KVOy_z8qaAnXY5e9mSs4O_5NJfNhP8GV6aHFzdQnGLnUuop5Xpr6QMekb_ULsc6TgwuZYnI5OuxqILvvBbH3etGeOmnuy3BPBPo_x4ILhzdvB2ncEGoTvBQ9f1tgQH41oAgJwWFBLhjoDJa08G1mmgVV37_8q0RiUSUPsAU9ESgcks8CxnF4QozbZPOe9LASn-Oo7sDiIPei_4DrpuDmiEYVFnQb3c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مانوک : ساعت ۲۵
@withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/17325" target="_blank">📅 20:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17324">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">@withyashar
ماتریکس</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/17324" target="_blank">📅 20:47 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17323">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">قالیباف : تنها با کسانی می‌توان با آمریکا مذاکره کرد که برای جنگ آماده باشند.
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/17323" target="_blank">📅 20:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17322">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">@withyashar
اتاق جنگ با یاشار</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/17322" target="_blank">📅 20:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17321">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ایلان ماسک می‌گوید اگر اسپیس‌ایکس به اهدافش برسد، «ارزشش از کره زمین بیشتر خواهد شد». @withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/17321" target="_blank">📅 20:26 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17320">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ایلان ماسک می‌گوید اگر اسپیس‌ایکس به اهدافش برسد، «ارزشش از کره زمین بیشتر خواهد شد».
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/17320" target="_blank">📅 20:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17319">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f319acbe99.mp4?token=LI-urAJh9gWHoUhlKa87cAihfgRIfeF2pq4-17qCsYjHE0v3y8n1BDVYBiWBm8XXHiYQx7sxtP2yZbJaJJRo3BfBcPEZTK9nOUdK9hO2gEbqMUlg4sDVV1wvWt35TZ1eS-WjglnXo_McbwWgMg3T5HbPxa-Avfdup54Cv2mE-M6qdCSBuyfX8ZYIhY8_kZo0sWKGPBhw_p-JNa56ieIZMTa3ZMveVh2DoFbnoxhePQaygohkl6pl5baJRmc_r2u7VThjGFGawkv59DVBxiVwnuzqVgEL5rhm4TXVTNi0LXEIR0fEncK58meHD6RKeDj6-T7Rhnpvy9txM5uNTntUUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f319acbe99.mp4?token=LI-urAJh9gWHoUhlKa87cAihfgRIfeF2pq4-17qCsYjHE0v3y8n1BDVYBiWBm8XXHiYQx7sxtP2yZbJaJJRo3BfBcPEZTK9nOUdK9hO2gEbqMUlg4sDVV1wvWt35TZ1eS-WjglnXo_McbwWgMg3T5HbPxa-Avfdup54Cv2mE-M6qdCSBuyfX8ZYIhY8_kZo0sWKGPBhw_p-JNa56ieIZMTa3ZMveVh2DoFbnoxhePQaygohkl6pl5baJRmc_r2u7VThjGFGawkv59DVBxiVwnuzqVgEL5rhm4TXVTNi0LXEIR0fEncK58meHD6RKeDj6-T7Rhnpvy9txM5uNTntUUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کرمانشاه دید بهتر و نزدیکتر
@withyashar</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/17319" target="_blank">📅 20:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17318">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZfE5QIcFPUY_PnywiIexqGKMHG4gGa2i4u2RLCQ8O1YRlM2DRdmLnWywS0lgfUov4yO-A_B0ZiZ0pMEe1eSKOc-tpcEyFpJe3EoXToLq2GOmnoasSof8Is4-3AWejALFc8s8py1Pw5KONhSwFOLVo9OBAwX3NJPrSnx0qsoW-TnsqyB_WkzMDVSKYZQbix-l_PEsVaV8V1SRuug5DQN_4vULKf4-sdza5rRy7FXtvYFRQzvyUK5fcIOPAH6fr0iIgKXXIxzo2s5D9T4nE8rcunM7Wu6YHsVHfFZ_2b7_wAASuCSVSGvGz00QxfW684y-ST3U190LQvvica96YJaRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کرمانشاه الان
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/17318" target="_blank">📅 20:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17317">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IjhaGehQJe3jkBVgD4yXqVUZICKfatt4vAuxXeeQzI34pWQL9qM-xubTyDEpGPe4OF3FRkiBcEdpqLXo6GR6ehMpRSjm-A3kLVjvdP33QJiz6uzDynA4PYIk_ITl_hi3RQWb_kxx-EKehY8scLxgIVjXGHBxQEHWEGZ_rKXj7Uv_Tf2D2A_sLNi1WOIvoZ6tQHOzfUf5s5J60pFVa3M9LJ_h7Usco9Mpo8bt9LDG8DSAMqc5DuvukuPSiiST-YRw-C8oaulnJb1m36TP3gg7nO_-whvBzwir6V3xpPIQCsE5sY12wppQcFDbJJbLRCrbuEvMg9rF5r7fk4B985hohA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کرمانشاه الان
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/17317" target="_blank">📅 20:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17316">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">فارس : تکذیب شایعه مذاکرات جدید ایران و آمریکا
یک منبع آگاه در تیم مذاکره‌کننده ایران:
ادعای العربیه و فاکس‌نیوز درباره برگزاری دور جدید مذاکرات در هفته آینده کذب است
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/17316" target="_blank">📅 19:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17315">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RSYl9TxSIRN4v14Jh9drf0o9U1jAXwAlAtjOZ2v9Fxj4k2mh4wnETRJz8AayB-S4taKub78ukKnkKfeJkb_yKIHTVwhzBCNCjMpOa8QaUoGI0AfyyHoOvuMMgNvxFsnuLsV02mEnBa4ArX7D6Ye1mXqReENPeLDE0rQeSDyHqbidBCpbxD-fBPCFkvwsyRUIaVEWhNCVIV7IYDp2mvaTzQL3Prwftnk3VVr5jxSqMbvBUKurTkGSD-Ryox8q-l3gmWdfYUDWu1LuWsY118cwLgNYeYYNBfVlkVBMv8pGysXacFEflEMUDf5eTFxa69Y30A9X3YAy2RsKb5C0hMw0uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از سری انتشارات فرازمینی ها پنتاگون این عکس را که توسط فضانوردان در شاتل فضایی کلمبیا گرفته شده است، منتشر کرده است. در این عکس، یک جسم ناشناخته در مدار پایین به دور زمین دیده می‌شود. در اولین عکس از مجموع سه عکس، این جسم در نزدیکی مرکز تصویر، و سمت راست کره زمین قرار دارد. این عکس در طول ماموریت STS-80، بین 19 نوامبر و 7 دسامبر 1996 گرفته شده است.
@withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/17315" target="_blank">📅 19:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17314">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">اکسیوس: قطر، پاکستان، ترکیه، مصر و عربستان سعودی در تلاش برای کاهش تنش‌ها بین واشنگتن و تهران هستند
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/17314" target="_blank">📅 19:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17313">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">چندین گزارش تایید نشده از انفجار/زدن ساختمون سپاه و اطلاعات (کنار هم بودن)  در قائمشهر مازندران
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/17313" target="_blank">📅 19:19 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17312">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">گزارش‌ انفجار اهواز
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/17312" target="_blank">📅 19:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17311">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">آکسیوس: دور جدید مذاکرات ایران و آمریکا، هفته آینده در ژنو سوئیس برگزار میشه!
@withyashar</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/17311" target="_blank">📅 19:09 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17310">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f831f063a2.mp4?token=Ja22fDxweLWq1wXFpfqVFrSQ2E9eJr0FyuioUnJgF3DXq0OKz56CVF6SprRp4hA89RDWj1Hd7pK7oN__1qmeOGwae3KRHWUMvpVcgN87UJdAKsvZFrj6RM6gvhhXAsI6NNSnIQujUlHmre0LtCgFUR39D-zKoNFPKO8pRzUvHXXnbCXR33zHoLziY5748Z8i4A8GLZupIxbjMy47lovnQGA9T99ZlrXJh2lRiY59jdzQ0lvAamsVUcHnewCuUvAkzF-G1tVLr6IOzO0y1IjFMD9Qh8m5zk-uXXFneyv0cD0oaVfQKBrWoeoK0kfliBEKDUNt0OoyHQQdsf4g4dXgxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f831f063a2.mp4?token=Ja22fDxweLWq1wXFpfqVFrSQ2E9eJr0FyuioUnJgF3DXq0OKz56CVF6SprRp4hA89RDWj1Hd7pK7oN__1qmeOGwae3KRHWUMvpVcgN87UJdAKsvZFrj6RM6gvhhXAsI6NNSnIQujUlHmre0LtCgFUR39D-zKoNFPKO8pRzUvHXXnbCXR33zHoLziY5748Z8i4A8GLZupIxbjMy47lovnQGA9T99ZlrXJh2lRiY59jdzQ0lvAamsVUcHnewCuUvAkzF-G1tVLr6IOzO0y1IjFMD9Qh8m5zk-uXXFneyv0cD0oaVfQKBrWoeoK0kfliBEKDUNt0OoyHQQdsf4g4dXgxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجموعه اکسین پلدختر
@withyashar</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/17310" target="_blank">📅 19:09 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17309">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">گزارش انفجار جدید از بوشهر و بندر
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/17309" target="_blank">📅 19:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17308">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uUBjnd_xJT_Yo-qVTQ7duvMmjPuOerzHZwSVeSWCYECeh28X75KYzMM5b-Pw5pdG5wUVC_7gyjX4654SZbnZhaOLuCwzws6KbJGr_QUBwvvmr0wkhnadxtHqJrOkEET1bfHJ33EncZSFzzwjXlTOlMp7Gl6uZkYawf1ID3emTMmtV14ju7HcZVPODdedT5yvtPv0r0WTPIAqirjWHMM3yxS-mroAFUCY304yCKe8ZqMBmZSJoS_vdO9yAIwoOH0t5fzJY5rE52cqc5Zdx8dAo5N1ChotfwtgOw1EABrhdRWr57qgLMIC9-SUljVilRQT1hRpchV5IaDkmueIxBheAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پالایشگاه نفت پلدختر,
یاشار : بعید میدونم کار آمریکا باشه
پالایشگاه نفت پلدختر در استان لرستان، در حاشیه شهرستان پلدختر و در مسیر کریدور انتقال خطوط لوله نفت خام و فرآورده‌های نفتی کشور قرار دارد.
@withyashar
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/17308" target="_blank">📅 19:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17307">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PNMQzgMJGFNSYYqMRknMrO7H9VDJuAIp-n-p3gdfGWjXF9yvs92PvHhHv0MUBn1cvQZr8HnjNL-2B8mscYTR6zEkr7M_8oVFoXrHdmvL-KvpAlAeowRJvra_lMYzypKFp-Lxp3OBg9oZQzOm_-rMPPKawnTx5ORy2vnktAS0ItGspbf-HgiBrfDcfb4Vw-fLt1bAC4HzSVb-vuhwrEgXssv7lKzFQSsCzV0hi3YWFt3xQhXgQp142nI9i0qbXzmg5EgupRaQIz3doanEO6Lhmd9MqyBpRJ_6EOX6Pbd07DUWYw1IFEbb5TevQESSwgZGyY4FGCekY9jn22vkBqqsxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پالایشگاه نفت پلدختر, همین الان
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/17307" target="_blank">📅 18:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17306">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cbd4b57ad.mp4?token=qkxIL9tajYrLa8taViEdT-GrzV1FVjAojbOxkDlqbHRYHFE_OdxWMCGmZvegU116PLVgJs93I7jdVuHP1QaqtcdVHLIuqiRQ9v0bxe5yQ3IaVV2eWWu5FiuSpqhUCVdnB1A4C66qne-PMFGzuV5RiqCyU0pPYUjdiFv0t3wCpHzhnwAL2grfgedZBy0i-7k1hUKrkXz1HyQrI_f0ERJuGeo_Wg32i0HqnAVRbPaR18HZ_u8jYPSKUOlAzbd7JaazaXZYNYJj5fswekHqs3j4hHNQ7oPl2-bxTDWolAIheoB3k1h55UTrHwHonUq9cvnWgLsbJQqhBHiO5ndyXHC-WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cbd4b57ad.mp4?token=qkxIL9tajYrLa8taViEdT-GrzV1FVjAojbOxkDlqbHRYHFE_OdxWMCGmZvegU116PLVgJs93I7jdVuHP1QaqtcdVHLIuqiRQ9v0bxe5yQ3IaVV2eWWu5FiuSpqhUCVdnB1A4C66qne-PMFGzuV5RiqCyU0pPYUjdiFv0t3wCpHzhnwAL2grfgedZBy0i-7k1hUKrkXz1HyQrI_f0ERJuGeo_Wg32i0HqnAVRbPaR18HZ_u8jYPSKUOlAzbd7JaazaXZYNYJj5fswekHqs3j4hHNQ7oPl2-bxTDWolAIheoB3k1h55UTrHwHonUq9cvnWgLsbJQqhBHiO5ndyXHC-WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر ماهواره‌ای، خسارات ناشی از حمله موشکی اخیر آمریکا به پایگاه موشکی ضدهوایی بوشهر در جنوب ایران را تأیید می‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/17306" target="_blank">📅 18:55 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17305">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، در مصاحبه‌ای اختصاصی با روزنامه نیویورک پست: «اگه مردم ، امیدوارم دلتان برایم تنگ شود.»
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/17305" target="_blank">📅 18:50 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17304">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">سی‌بی‌اس: ونس، ویتکاف و کوشنر در تماس با مقامات قطری در چارچوب تلاش‌ها برای تقویت دیپلماسی با ایران هستند
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/17304" target="_blank">📅 18:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17303">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H7Gw9pfJGjNYHrPIT1vxTCcspui4dZlAkh_nIrWH4jVkwfI5MTmcfo6SBZNGjeSR8VFHHzCGxnxQ41tCD7m3CPZSlVNkCFeUZgnBsBzhpDjI9h98A7ekpOoFVPhEY37O5SFG4VyK_cDQATmk8sscLbUqz3Tw0Pt-KJ7YQqNzCYw9HEd9T68xvYMZkBGQvFJO7vA5EvF8EwV7ImyIzrlS2sTdpbtNLd4rSS9qlMHa_4JL9GiRpwDkFP4LAPj3DRkF_vF6cgNpmseBKD8ZyUVmzo5F4oN4wqmVso2JE5OwNGllTxFOTxN8XpzYZZIEYxrp1VhAsIPlaS80PmEaqB1oxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر ماهواره جدیدی که منتشر شده نشان میدهد ناو هواپیمابر جورج بوش و گروه ناوشکنهایش به فاصله(۲۲۰ کیلومتری)  از چابهار قرار گرفته  حتی نزدیک تر از ناو لینکلن
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/17303" target="_blank">📅 18:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17302">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/17302" target="_blank">📅 18:37 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17301">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EU8dTgNQGcD2tQryi0a2WP6Kgo5y7wD0Nju_NEevIlN2bUDWGRPy75b5wPt8r_HVVdDA-9dcCAUqN_6smLSDYK6bn70S-bWFjw9HB46XhNLyTaknlBFJ4ypAd9xzPVe90VuNRqLBNOXt0BrJN3pguxo09_hFFt4MJ8vJXlvX8ozoTBoy2YtGRf6ZWDm8B4saVrWhmYim3ixZR9EonpwbnsRWTVkuPDuBHO2cE5EXxPgBq8LiC1LS3nQwUZLDlN5zlQM20hhIXiXaTmwscl95COG4sgaTZfI3zPRiGvxld8usd-cOvpxvSx-TCk5g3rmFK0MeHLPnlhDJuFBjV0lmdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهراً پایگاه دریایی ارتش در کنارک هدف حمله قرار گرفته. @withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/17301" target="_blank">📅 18:34 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17300">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">گزارش تایید نشده شنیده شده ۳ انفجار کنارک  @withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/17300" target="_blank">📅 18:26 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17299">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">زدننننننن
🚨
🚨
🚨
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/17299" target="_blank">📅 18:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17298">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">گزارش انفجار بندر عباس
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/17298" target="_blank">📅 18:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17297">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/17297" target="_blank">📅 18:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17296">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">گزارش تایید نشده شنیده شده ۳ انفجار کنارک
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/17296" target="_blank">📅 18:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17295">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JNW2UvQcrkd0sdJJ1m9ujV9O7pTjqcdhQjVMVmiZPg_HMbzH9k1Zc76rGcAS0Of6zDakFC-qHot6SK5gCxZYWFQOeAvQb8_6GxX2mvPdto2alCqG-7y6FyDezC9JF3hecIxD7eF82GDOtGrPozlfRJaUc8IdupYEMw5kVGlT3m4k73BG7x8eXz91gjtb6DLE8MX0tPd5Rw7kKNlUmMddiXZbT2q1GaR-T58exvowfeaAChoEYy68P9fejXdarY9W3Ho7WfURKtwHmcCNKZ1J8DHmnLeNGKJx5isju2OaqxnKhlET_mcQnd_4HfCo3KjGOg5OFbGm-wtXXIXzDtMgZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعداد هواپیماهای نیروی هوایی ایالات متحده که امروز در پایگاه هوایی شاهزاده سلطان در عربستان سعودی مستقر هستند، به کمترین میزان خود از زمان آغاز این استقرار در اوایل ماه فوریه رسیده است. آخرین هواپیمای نظارتی E-3 در اوایل این هفته از آنجا خارج شد. در حال حاضر، یک فروند E-11 و ۹ فروند تانکر در آنجا باقی مانده‌اند. به نظر می‌رسد که ارتش ایالات متحده بار دیگر فشار خود را بر ایران افزایش داده است، و به همین دلیل، بسیاری از تجهیزات حیاتی مورد نیاز برای انجام عملیات‌های بزرگ، از این منطقه خارج شده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/17295" target="_blank">📅 18:17 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17294">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ترامپ: اگر جمهوری اسلامی در ترور من موفق بشه، از قبل دستورالعمل‌هایی گذاشته‌ام و در اون صورت، ایران به هدف شماره یک آمریکا تبدیل خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/17294" target="_blank">📅 18:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17293">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mDHyZeWRWaBBR7cnlyAbyroauzeRc9ilnfc-n_Jy8UctiUjnwSTUEbPTzx1qKFtcHGilWG3ZxlpPnWUWEjA2O6ypVP4shdMRQ2ur9UzbG1LF5f8qvtlNSRkb9vNs9_1aCDtqBYHMT7lRVkCGH1o4lmwiH8jTvzasMZHW7XxIXEjcpxYVYKIEDbL9gO8UFZkO5Pz0x-Za08FZtclRGjNA4X8K1-wh0kBHtvUGrh_3t6yE3T3CwJe-sWiM8Hx1sNJm-avQikPqz0aM2su0deWUh5v4bEHzFIh2u_LciL42DQ2wd9aOCuRYcgC8JA0LgJmWp0mMoiH4lMpjoPseNRT4rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی ایران از ما خواسته است که به «مذاکرات» ادامه دهیم. ما با این کار موافقت کرده‌ایم،
اما ایالات متحده به صراحت به آنها اعلام کرده است که آتش‌بس پایان یافته است!
از توجه شما به این موضوع متشکرم. رئیس جمهور دونالد جی. ترامپ
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/17293" target="_blank">📅 18:10 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17292">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X2-1GqVDSdpvGzEtSjVfq_qfmzEbyt_PzzJV8k2iIF8ktoxoWNnfXo06e8alfG0OqTkcw47u9GjprhgUlaZGLRvJqNe243TUZzGeuUdqIsMxGCjgmXN46j-QeUhZiKcbACMBtkbgxlIcI-lJt2g3R6nNTUDGFNmwS-uJY80hPLSztUdxV5TszhaJPa8lgF0xZI8U8mowZI_qgGP74_PNhQbasHDE53eP2XN0VgB1z-IqLdORThhm2-fPSy6Z6tRlUuPOYbSfNf8WhDQ6ZDfGTkPQKrUSGs9JhXmJPoMN8s2QAc2j-ZSNmo_engkIY8IbiatU-YUck3c4WTIiimi5KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق تصاویر ماهواره ای منتشر شده؛ ایران مسیر های منتهی به سایت هسته ای فردو با تپه های خاک مسدود کرده تا مانع حرکت سریع با خودرو به سمت این تاسیسات شود.
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/17292" target="_blank">📅 18:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17291">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4rIckR4Spt-edB4rxZ-mnceQesfD1zdV168ggy6klhKS6iEHard16HC7oO2Zz0hzS8qAhRi9NcxFwys9Rjpua-NNFQKVeQJpdBuKUDXfyBpF07fYiTK_RLYWg33ThLMAMWZS-LJVXsKhcXbdg7kObnnysPN2E0pHhHSVMPQh786YjI8yLpM0Rwz9f6h7nKFpYoeFSMue-N6VoNIfiPBfcX007ANstwHAJL76L2FZ5SIyecxW6LE4TeTmX57JOc_fZMY9bWaziNHpASdKX4o4jQpBQS4q7EWB1nLziva9J58aJg_Yf1nPL3kaB-hInvQvqpKhnYeLYjRABkPoy8x6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر‌ ماهواره ای گروه رزمی ناو هواپیمابر آبراهام اینکلن و ناوشکنه های گروه ضربت ناو هواپیمابر ۳ در نزدیکی چابهار که شامل :
* USS Spruance – کلاس آرلی برک (Flight IIA)
* USS O’Kane – کلاس آرلی برک (Flight IIA)
* USS Frank E. Petersen Jr. – کلاس آرلی برک (Flight III)
میشوند
@withyashar</div>
<div class="tg-footer">👁️ 98.2K · <a href="https://t.me/withyashar/17291" target="_blank">📅 18:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17290">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">بازهم روسیه و چین با طرح بحث درباره برنامه هسته‌ای ایران در شورای امنیت سازمان ملل متحد مخالفت کردند.
@withyashar</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/withyashar/17290" target="_blank">📅 17:50 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17289">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZx00usw90dIG0DlI5fgmbpVgEVb6XUwuuM3UrY289pa5n9itlCxzTYsNhKcxDH29ty0RQtheCovJjHfUyKSB19zsghnDyg9U4D7YCzUV7K3aWJSDhflWCddCcygYbjPjHIMORwz7fuAXdrA6tRZ3Ol1miAbzonSedlItp9Tx7RlIgdkDm-swVJiS1_XFPEStcXoZEvwfoXBzQG7mZ_vKD_Hyt8wNRNYguxr1CV1Wm5R-cN4JGhiZ1VOmuyKjCcxXAeoxN4l_ROUlJlgjgivTuO1VIOYMshP80tQ4I8gASEgLPUc9WWUVbM0a2kbbFoJe-Lnua6Jo4Kcolyds2z8vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناو هواپیمابر آبراهام لینکلن (CVN-72) و چندین ناوشکن مجهز به موشکهای کروز تاماهاک در خلیج عمان، ۲۵۰ کیلومتری چابهار آمداند ، همچنین دو فروند هواپیمای P-8A Poseidon نیروی دریایی ایالات متحده از جیبوتی از صبح امروز در حال اسکورتش‌در این مسیر بودند
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/17289" target="_blank">📅 17:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17288">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/withyashar/17288" target="_blank">📅 17:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17287">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">تسنیم:یک هیئت قطری به منظور تلاش برای تثبیت جایگاه میانجی‌گری قطر، بعد از حوادث روزهای اخیر به ایران سفر کرده است.
گفته می‌شود هدف اصلی این سفر، تلاش برای تثبیت جایگاه میانجی‌گری قطر، بعد از حوادث روزهای سه شنبه یا پنجشنبه باشد که در جریان آن متعاقب اتهام زنی قطر به ایران در رابطه با یک حادثه ادعایی در تنگه هرمز، ارتش آمریکا حملات گسترده‌ای را طی روزهای چهارشنبه و پنجشنبه علیه مجموعه‌ای از اهداف نظامی و غیرنظامی ایران انجام داد.
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/17287" target="_blank">📅 17:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17286">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">خبرگزاری CNN :
دولت ترامپ در حال بررسی آغاز مجدد محاصره دریایی علیه ایران است.
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/17286" target="_blank">📅 17:22 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17285">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">https://t.me/boost/withyashar</div>
<div class="tg-footer">👁️ 99.3K · <a href="https://t.me/withyashar/17285" target="_blank">📅 17:19 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17284">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/withyashar/17284" target="_blank">📅 17:19 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17283">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/429ce7bfbd.mp4?token=f8PVYYrMV0SWgrMttKhw9xFMa-ZOKCFuGI0ucWlUS-uJEJzTrjcmkU1XLXxd8HJrGNEVOvKTvJODucO2IvoY097J0-q1Sdkk4aVn_0zHWd37GEdPrn4yqO1OJs_WCIdLy9zhj5kDNikcPNuW0r8l-oQxd0m2vjkbIBodC_WM95lhHWOy4xItX2MOIo5FeeVISfmG-zWfxwUl8rKqLqZrglwA_gxD3_C1_bhdFqqvoDnyahguzInKE-v3X9IQWtMmVR9HhEiWi4HM6x5v02I89eavMRJMfj2U8e1gN13ywLxWJM8kVI2KDrEsiBogRYirdxHqrWkMDPaSUYPwELsdtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/429ce7bfbd.mp4?token=f8PVYYrMV0SWgrMttKhw9xFMa-ZOKCFuGI0ucWlUS-uJEJzTrjcmkU1XLXxd8HJrGNEVOvKTvJODucO2IvoY097J0-q1Sdkk4aVn_0zHWd37GEdPrn4yqO1OJs_WCIdLy9zhj5kDNikcPNuW0r8l-oQxd0m2vjkbIBodC_WM95lhHWOy4xItX2MOIo5FeeVISfmG-zWfxwUl8rKqLqZrglwA_gxD3_C1_bhdFqqvoDnyahguzInKE-v3X9IQWtMmVR9HhEiWi4HM6x5v02I89eavMRJMfj2U8e1gN13ywLxWJM8kVI2KDrEsiBogRYirdxHqrWkMDPaSUYPwELsdtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اولین تصاویر از قبر علی خامنه ای
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/17283" target="_blank">📅 17:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17282">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">گیلا گملیل وزیر وزیر علوم، نوآوری و فناوری مصاحبه با اسرائیل هیوم:
"شاهزاده رضا پهلوی و من، «پیمان‌های کوروش» را آماده کرده‌ایم؛ آنها آماده‌ی امضا هستند و نتانیاهو با سقوط رژیم شرور در ایران، این پیمان‌های صلح را به خواست یزدان امضا خواهد کرد.
رژیم ایران درگیر جنگ‌های داخلی است،
و هیچ شکی نیست که این رژیم سقوط خواهد کرد!"
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/17282" target="_blank">📅 16:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17281">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83d923ee58.mp4?token=NZLgYcPEpPFLUIzXICNVQMilrcvX_vJdUe6mOxpfngya0lkdMWllglqtknGxsRA0n6zaFENvRylhVkPGkLnLHXSIkT31YmIbWXOpa52DzR3D5qlUEBw7Kulnmxwe5PrnOKX_pK8WRG32dpuiZ3SfX2ID-ZVgbNjmmrwgp8HlFyxee-T5ZEIXjIHwEBbcF-J8E7YHPxrz8S_8G-EG06bR5z5b9aG2gDarrd3Q_No4Q0-5JFLJEmTnBeo-nR-rr7nxL3dV4EzBFo-1NAwCJatZOGcoVJ9F0UiWyZEu1hSBIILA2yj87MY0yogi2cbGy5x-7CuMRPOY_UJ3ocmJdnWPPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83d923ee58.mp4?token=NZLgYcPEpPFLUIzXICNVQMilrcvX_vJdUe6mOxpfngya0lkdMWllglqtknGxsRA0n6zaFENvRylhVkPGkLnLHXSIkT31YmIbWXOpa52DzR3D5qlUEBw7Kulnmxwe5PrnOKX_pK8WRG32dpuiZ3SfX2ID-ZVgbNjmmrwgp8HlFyxee-T5ZEIXjIHwEBbcF-J8E7YHPxrz8S_8G-EG06bR5z5b9aG2gDarrd3Q_No4Q0-5JFLJEmTnBeo-nR-rr7nxL3dV4EzBFo-1NAwCJatZOGcoVJ9F0UiWyZEu1hSBIILA2yj87MY0yogi2cbGy5x-7CuMRPOY_UJ3ocmJdnWPPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو آفریقا جنازه خامنه‌ای رو بدین شکل تشییع کردن
@withyashar
🤣</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/17281" target="_blank">📅 16:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17280">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">سی‌ان‌ان به نقل از مقامات اسرائیلی:
دولت ترامپ تمایلی نداره که اسرائیل در عملیات نظامی علیه ایران شرکت کنه.
@withyashar</div>
<div class="tg-footer">👁️ 96.5K · <a href="https://t.me/withyashar/17280" target="_blank">📅 16:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17279">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">خبرنگار آکسیوس:
به گفته یک دیپلمات آگاه از این سفر، مذاکره‌کنندگان قطری با هماهنگی ایالات متحده به ایران سفر کرده‌اند تا با مقامات ایرانی دیدار کنند و در تلاش برای کاهش تنش‌ها و ایجاد شرایط برای از سرگیری مذاکرات باشند.
این دیپلمات گفت که جلسات در تهران بین مقامات قطری و ایرانی هنوز ادامه دارد «اما واضح است که هر دو طرف می‌خواهند به یادداشت تفاهم بازگردند».
@withyashar</div>
<div class="tg-footer">👁️ 99.3K · <a href="https://t.me/withyashar/17279" target="_blank">📅 16:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17278">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oN_RZE749gh_vYb6O7R279JmMTxstas8bD3atxD3pGPcRDNz39HrAxjWQZ1Qw5cwr4L7PlYMNSDpNmakcdMmXN3txG_310EoeBHd_ruHTFXoO9_pvclgr-edolfX73FoAUIka5Rs8xeKiQw8dsba4fDZBgqcxQ8vo6qGxcdlg7e_kOAtMtDzw5Dz2TPi0nxMGE6HCw6xJy2LqZZDFMHAu8lPLvDMplY0QdbngeNS3rPc4A-MgeSKhITGnhIIjXQ1095o_owsDEVX32kadP0M5LmifxrtJ_SLrJaer91rjoM1dYRH-44Te-4apwkywi6d3pQRxPgYKdSVu1x7WkXA5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همکنون  گزارش های زیاد از ستون دود عظیم تهران فکر میکنم سمت شرق(بزرگراه امام رضا-جاده مشهد)
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/17278" target="_blank">📅 16:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17277">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ShasZViBBWkGYl2JPeOnFITuhTbJJjItcYZagG-3UAy0hr3sysL-d_aG-QtsP208kLvNWyZuhruH8ApualqJf_s1A4I-4JEbiRN6M1h-67N_ug_lYgSH9uy6n1I16E7cBiZHXbC-uRpThfVivEX858EYakEn5HnbqFjy6XW4YP7W-IRpVgZ2bAJOa-zGrAOhvolxhnB7TIIfwUMD92DKbXW8_4Ls76RPxTJdMVDhG29nkrU6N4Xf77FD3mAGK5dQJ1FhZtj5uxAKTNQdpFiVMdDXQcrNVxRJdFr20yDCa_kCOxmuWwVWhs8tTZzCGQi4UVOgn2KaYDMrinv7qn_wuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏دستگیری 8 جوان امریکایی باتهام تلاش برای ترور ونس و ترامپ در هنگام بازی بوکس UFC در محوطه کاخ سفید . این طرح از ماه مه شروع شده بود . یکی از این جوانها    Tycen C. Proper, 19, of Danville,  تایسون کوپر 19 ساله هست و عضو گروه ازادی 250 سال -هست . این طرح خیلی خام بوده . امنیتی ها هم اجازه دادند اینها کارهایشان را بکنند 4 روز قبل از مراسم ، با شواهد دستگیرشان کردند که به ترامپ نشان بدهند تهدید برای وی جدی هست . این 8 نفر از 8 نقطه امریکا بودند
@withyashar
حقیقت یاب اتاق جنگ : خبر پخش شده مبنی بر ترور نرامپ در‌ امروز و دستگیری ۸ نفر فیک نیوز است</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/17277" target="_blank">📅 16:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17276">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ترور ترامپ</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/17276" target="_blank">📅 16:04 · 19 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
