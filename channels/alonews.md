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
<img src="https://cdn4.telesco.pe/file/muQNAevQnzCpyE6TwLUaFcwc77yvDswawaAvRoEzAL3HdtvFRZScQv13OhImWgsuf5x0mwx-UzPHflXzdcvU8nPHxIIWyMd2SG96HhcbUDIYKAedV1F1PpoAZd3Tm88smepCgW_NMPlxOo7KV1pjtDvQ9nZQbGB5ehnxS909mhc2Kq72TtqHLMnpt9CvMAPJLsAagcqsHsbpswbcjUZ9w0yRBZP98hn01ev_RVhD6fWZO5F2eYK7azai4gWO_TYkQtNRMh_yNta26tRTLNxNE0CeOr67MEFXL67RA8Av3R_QDN-UhhjZeJyhDh2Rcws2L6OGgmRPm54QcY4dWRAIwQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 938K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 08:29:30</div>
<hr>

<div class="tg-post" id="msg-135884">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
انفجار در قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/135884" target="_blank">📅 03:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135883">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
انفجار در جاسک
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/alonews/135883" target="_blank">📅 03:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135882">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
منتسب به تبریز
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/135882" target="_blank">📅 03:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135881">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vYe4iwUG4lO09OIzS5zHAwMHDEp9mcVz9YEbY2reqmtfeflN1SGY4a5fVdXXVsg5w5qCkODT86dRSrFVWQm6R43CRVDNVHm9NE6lwoFjiW60_JNdwUKtZk6C39Q5_QiladL4sndaItI6pfx-nOxk9i4r5IgBhbtt5_dyMOr4o3QF83DZaziaKHE9JEL2Wd--2ZK9apLsLHarwBub6_BXSE6UEWbFWMZmoEW1fUBpFvAPRn9oPtoINZh_KlE0YFiQpYi3j-msemnClkS3yvhwKtiQfkFdJ5TP6qITFYk0DMXOHFt_f7lal5fOTX2tH2147-lDBvPAjcZxqScxVBeJqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منتسب به تبریز
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/alonews/135881" target="_blank">📅 03:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135880">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GRY4jF7uV4P0nDalqyRVX3z4s4scTczZU_Gt_gBCS_aF4Mi9M-damoEmCiQqb8tB5Ij43Zh1OHh5Z2BKl_qa6GTIPn2XuIJy9V_0n9ZtZUd9ab9QZK3npqG1nlb2Arz9ansJ0tJLoyiCEVnciGZ79hkseViMts3CbDpAxTQMlEPbZrPNrBcZek-EzB6nPTK7Yb0kr1BNtdYaIv3d2H35J-v8YFOh4nAVYBeV_QTJgA8BWCzZ8h1mH3Yv6Rjso2kAjzRIeaN5yGteLfUfgXqI2K-wlnnV0R0ulEqzQL-YrycrVvzyXGsLkg4YWZSA3X86QcMntyOA2cRm9ELbAdbWvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت بندر امام
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/135880" target="_blank">📅 03:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135879">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RFrbbm_B_gFvuF-lTHeQvCJeAnkTZtzBJqMNYbTQLbYFEM3SkcBFr3-hcZM2talyKyM_U3tvbdLhsYc-z88qJJVsx5BosKTLP_JR9Csgj3FWV3KwennQPlJsjE_17B-YPvkt2MckyI-sE5IbtUUpqj_Jk_f90wd6_-GI_T9oevcMD18zPr_5JTIZ7Q4KasizgQQowMNPX5yE0xfBUR7E6jP5IJtk-d2Wd-BFCsaDCi8CNVJpcOkFJKjCGovsgXGwWO5E1tS0VF-XdRL5FTiSMBw_MR3AI1LY7a6Y6_0sRg6JTTl6SxZmXxoBKbTlP21OlcfOTh7HNY2aCuFImz7npg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یه کشتی تو سواحل تنگه آتیش گرفته
✅
@AloNews</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/alonews/135879" target="_blank">📅 03:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135878">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
انفجار در راس‌الخیمه امارات
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/alonews/135878" target="_blank">📅 03:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135877">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
انفجار در بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/135877" target="_blank">📅 03:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135876">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
ستاد فرماندهی منطقه سوم دریایی بندر ماهشهر مورد حمله قرار گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/135876" target="_blank">📅 03:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135875">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
انفجار در سیریک
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/alonews/135875" target="_blank">📅 03:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135872">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/baefb3737a.mp4?token=YcrBGW7ADnb2spwcKyZtEGstyLNKr2DGBEKWnNnlAi706NcrL6BofbSBNvV5R4b1G3p6ZVp_WgNlwejF9vPwwy3kV9_CEoRC3dNgfmAsZaERpE85PtEH0XDhpFnIEqwAI0S9MSBEqI93KcKVrTwb3h2yxOx04A_Sqr2QM2aq-IV3LXN61ztJMxzyGSZUtXgDphh30VJ_bIKr5kYSjxfjf3qNa9wEqBrxDtw4qPlgrAHrQp8ywtP68tMApxgKw4zTYAjYLPVR_Ora-1sJfWk36hMuBLuWcRw86UsLxmvxnm8aqn1dX8us0F6XHfs8O3eGkXSB5a26FBIqZLpbVH2rDg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/baefb3737a.mp4?token=YcrBGW7ADnb2spwcKyZtEGstyLNKr2DGBEKWnNnlAi706NcrL6BofbSBNvV5R4b1G3p6ZVp_WgNlwejF9vPwwy3kV9_CEoRC3dNgfmAsZaERpE85PtEH0XDhpFnIEqwAI0S9MSBEqI93KcKVrTwb3h2yxOx04A_Sqr2QM2aq-IV3LXN61ztJMxzyGSZUtXgDphh30VJ_bIKr5kYSjxfjf3qNa9wEqBrxDtw4qPlgrAHrQp8ywtP68tMApxgKw4zTYAjYLPVR_Ora-1sJfWk36hMuBLuWcRw86UsLxmvxnm8aqn1dX8us0F6XHfs8O3eGkXSB5a26FBIqZLpbVH2rDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر منتسب به شهرموشکی تبریز.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/alonews/135872" target="_blank">📅 03:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135871">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
حمله آمریکا به سایت موشکی خورموج در بوشهر
🔴
۵ انفجار شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/alonews/135871" target="_blank">📅 03:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135870">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
انفجار در سربندر
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/135870" target="_blank">📅 03:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135869">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
انفجار مجدد در خرم آباد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/135869" target="_blank">📅 03:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135868">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
انفجارهای مجدد در چابهار
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/135868" target="_blank">📅 03:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135867">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
گزارش تایید نشده از انفجار در ساری
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/135867" target="_blank">📅 03:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135866">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afed7de895.mp4?token=HLn3DnDtIUF67ohVC8JAaKdsf6A5KyIO94GbxcALeKxJl7Mb4mJdBT1shIFY7s8M7pDG_vtF840bhqGQ19bBie5YUZ_QelY4H4qrpMiZKJ0oCSF5eEkBC3PV0IXMeWJm68f_APUE-KHCIGpabZ0y9GcipfcZ8QeP9WsW7moPeBsz80LwSWYRvhSdK0avLBsRQiaoQKbp2JJruS_Gr11wmiLb4Ol17T85vkx9eiXi4pFeMdeIZOYeMN54vVrlIVh3zaoaDYkKe_03P2SgIRqPbmvvEWr8oXddYASUg114TMWQYhbZU7Dspv-JUirpp1TGuJIZrUalyQ6sBHV0C6eQ1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afed7de895.mp4?token=HLn3DnDtIUF67ohVC8JAaKdsf6A5KyIO94GbxcALeKxJl7Mb4mJdBT1shIFY7s8M7pDG_vtF840bhqGQ19bBie5YUZ_QelY4H4qrpMiZKJ0oCSF5eEkBC3PV0IXMeWJm68f_APUE-KHCIGpabZ0y9GcipfcZ8QeP9WsW7moPeBsz80LwSWYRvhSdK0avLBsRQiaoQKbp2JJruS_Gr11wmiLb4Ol17T85vkx9eiXi4pFeMdeIZOYeMN54vVrlIVh3zaoaDYkKe_03P2SgIRqPbmvvEWr8oXddYASUg114TMWQYhbZU7Dspv-JUirpp1TGuJIZrUalyQ6sBHV0C6eQ1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارسالی از تبریز
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/alonews/135866" target="_blank">📅 02:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135865">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4e26657ab.mp4?token=dBPDKnqetdCR2v8pX4bEM2ejAGS8c6wbAEKCUlQh8Y85QucZBPgbU4Pbeflx2g4egtmUdttbWJhCYLpw-qAkn67BIA_INWsFBZZu1flhf9-ixwBdV5rCtxMEn3kIli6HObRs6w1yFHOkzKUotv9ynSiRYFqQWZ0UBioLvYZtCTHNsL1ExHJlDttZEoP19Dc2MALCMtlLeMtZx6EPPkrLYQzUJw_yiroRFfPQukuEFCSh-XtrBxRkT3qV9bueuykaoFvmx-Ti-37T0Wlort8Yn7Qh6CwIizhehZAoBI72EWyvgAF9G5ARMhWprF333rK_eiBSEIsmq7irhu0Z6Nv2YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4e26657ab.mp4?token=dBPDKnqetdCR2v8pX4bEM2ejAGS8c6wbAEKCUlQh8Y85QucZBPgbU4Pbeflx2g4egtmUdttbWJhCYLpw-qAkn67BIA_INWsFBZZu1flhf9-ixwBdV5rCtxMEn3kIli6HObRs6w1yFHOkzKUotv9ynSiRYFqQWZ0UBioLvYZtCTHNsL1ExHJlDttZEoP19Dc2MALCMtlLeMtZx6EPPkrLYQzUJw_yiroRFfPQukuEFCSh-XtrBxRkT3qV9bueuykaoFvmx-Ti-37T0Wlort8Yn7Qh6CwIizhehZAoBI72EWyvgAF9G5ARMhWprF333rK_eiBSEIsmq7irhu0Z6Nv2YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
موشک های آمریکایی‌ای که از کویت به سمت ایران پرتاب شدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/alonews/135865" target="_blank">📅 02:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135864">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
حملات امشب خیلی گسترده هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/135864" target="_blank">📅 02:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135863">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
انفجار در چابهار
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/135863" target="_blank">📅 02:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135862">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V7pAQ8RTTY8G8rH3-u728S_be3prG8GguDUcGo1Fp_iROd8qu9PWJs_HK51y7VFPbuje8pTsTJvoNtATtyrAhuDsNb9MQ8uyiDpiPUhQnG_jXlxHxfOCrWmo9pEtzwRGowmq7uYa7j7ZLQ17JGGEg4rdBY16UM3oLnRaDwxHQbbKKQPqLrVKc1dP-_eitqmYZQUB2TRb2pM_LuPWVvzwBkK7N6BFpp7DFkfr8utsLybTbw70gVd9mJm1leiqBm59epKB6LNJfKvss4tOHtIIpEe6IinyGfIc535oySj8FQ_Wv5mI72lewK3pOKNpdpRGZApUuJ0NHX5KyY_zBvm41g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام: امروز، ساعت ۷ بعد از ظهر به وقت شرق آمریکا، موج جدیدی از حملات علیه ایران را برای نهمین شب متوالی آغاز کرد. این حملات به تضعیف قابلیت‌های نظامی ایران که برای حمله به کشتی‌های تجاری و دریانوردان غیرنظامی در حال عبور از تنگه هرمز استفاده می‌شوند، ادامه خواهد داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/135862" target="_blank">📅 02:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135861">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
انفجار در کنارک
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/alonews/135861" target="_blank">📅 02:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135860">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
انفجار در ماهشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/135860" target="_blank">📅 02:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135859">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
انفجار در خرم آباد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/alonews/135859" target="_blank">📅 02:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135858">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
هم اکنون صدای جنگنده در تبریز
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/alonews/135858" target="_blank">📅 02:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135857">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
فوری/4انفجار در تبریز
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/alonews/135857" target="_blank">📅 02:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135856">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
گزارش‌ها از انفجار در تبریز
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/alonews/135856" target="_blank">📅 02:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135855">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e891d77eae.mp4?token=gpdz1RLFaTTgE_H0A-MMZ76N5acff0OvjstFFFPnQO1lxgFuchG3a5mexwVN44-02kilMyR28eq1klmEPb_19SeNpSV4SU7E9BjqyuIwfUmWCDy-varEx8V4x5WdSuIH07lIx3bXC7QcgGmIDI4-EXOveGvmJKrGKlZLNCAuEwbgs_sNh4qHs4u97eKR7erd48l-GFoCJ1jFYh2i5V20u3sNZlHWzl0Vhzm12cIbO60Ht4z8NhBQn1eqJpca7xaibp48tjypj3JY2CdVb_xXBqZY0kxamc6OUzuilog0HPPM_bhT_VACUxuLol5h6K3pek_F8ufh6w8mrbTsgxGa4YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e891d77eae.mp4?token=gpdz1RLFaTTgE_H0A-MMZ76N5acff0OvjstFFFPnQO1lxgFuchG3a5mexwVN44-02kilMyR28eq1klmEPb_19SeNpSV4SU7E9BjqyuIwfUmWCDy-varEx8V4x5WdSuIH07lIx3bXC7QcgGmIDI4-EXOveGvmJKrGKlZLNCAuEwbgs_sNh4qHs4u97eKR7erd48l-GFoCJ1jFYh2i5V20u3sNZlHWzl0Vhzm12cIbO60Ht4z8NhBQn1eqJpca7xaibp48tjypj3JY2CdVb_xXBqZY0kxamc6OUzuilog0HPPM_bhT_VACUxuLol5h6K3pek_F8ufh6w8mrbTsgxGa4YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عادل: قلعه نویی موقع جنگ رفته بود ویلای خودش تو آلانیا ترکیه بعد میگه کنار مردمم
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/135855" target="_blank">📅 02:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135854">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q3tgl0Mz-8iZcf5qi18uC_PXYLCLw8K97QWvmU0_GAqQpTKyZ0MEQ8XtFvzJVDjAOVrHC62WdE4bGbDmFW-Fu7lFfGPVeOMinqnE0O4QPSCbi2V7_x2SrxkcHleskUQt25Qke-VMbzbWA-j5lMR5bmo2bRe0_J1dm1Adzv4DhZGLxl0sJVZFOrPMHa0g4LhiiBKCjmwgxdQm5_DTmQuXIT3LxME_q6Qi61bfy-9i5qQulPdT29tTIphyDelEGX_nL189OfiPQhHuQ1hLNYsYjgZCS8kQHVzmND_0-20sn1xO-27CQ81UzyuaFoH0MJILSc0dTmP_Epgje4huwSe2JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از دختر پادشاه اسپانیا در استادیوم
سفیده
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/135854" target="_blank">📅 02:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135853">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
این وسط یه مدال هم به ترامپ دادن
✅
@AloNews</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/alonews/135853" target="_blank">📅 02:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135851">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
ترامپ میخواست با بازیکنا اسپانیا قهرمانیو جشن بگیره که اینفانتینو بهش گفت مشتی بیا اینور
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.5K · <a href="https://t.me/alonews/135851" target="_blank">📅 02:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135850">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
صداوسیما قاتل رهبر رو نشون داد
✅
@AloNews ‌</div>
<div class="tg-footer">👁️ 81.1K · <a href="https://t.me/alonews/135850" target="_blank">📅 02:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135849">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KTLWqMUHXIDf7MTg1aPsLzKn6iWSzA49iIGfkJKpycMwxAdUen1FixaT8N6hwnS_eCaEjh4JPG1IoJ34R2Wy6LQPxZKTZtT6ZYhlyXiPWaLMCg4vWY-jiSsxZh-TCYAorEmD-vx2Qgfm-sidsDSNaIjQCVqMQcGagXlZcIcZVExmoThovB0C7EZGyvWoo8nG0gSNzHgFuPTdtfn2eas5GmyoMNtVTNBbhrXoPz7VzaMs1MV9u-PrwhEKhn2H5IZrAJ0hqjyerzlTcKELFdBtuGRckwTp2lnfQTBEXY2tn1jm63OQ1bSUnzd-mfMkaffLMsviwZhRvfC9OXejAXjNRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صداوسیما قاتل رهبر رو نشون داد
✅
@AloNews
‌</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/alonews/135849" target="_blank">📅 02:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135848">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/UpY321M0t0WVAKwEzQC65i7_Ia9KL7K_sDzKV9EjhZX9RtmERTCIP6zdewMIDLwDu4NQYPZFDIVuqFhxe8kyRerYAvys2mkfJxYy_MJwtCIA6gIFM0EAY2C5c8VcGDsBp1R2Yj2YtJvNYQ6-czrxNis2FCVZ3hZ7ZtLgx9JEusSNEARb-Xy1gtFO6ylNKDfTgevA4J1dQ5oYuOqLWEFZLtIeNpfiFOsrlcDSvnf_x2055iVvaxhQxOAf9xlaOtpADHdc3Z59tCntzjKQkLJ6wK3m3r7nTv178pJJ8GLkPOpmvV458OFeKdXPB0a0ZC8uvptSReyU-xpRStOeh9kvpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسپانیایی‌ها و ترامپ جام رو بالای سرشون بردن:
✅
@AloNews</div>
<div class="tg-footer">👁️ 77K · <a href="https://t.me/alonews/135848" target="_blank">📅 02:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135847">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab00af27c2.mp4?token=P_iZXHjK4fFws1xB7K7iBY_fQxdKSTdsvMIuWB87KAbfZXQm8l0hbCnewKiVDgR35qlNtA0V-bCkIhdjHMqqUGnzkjc5VF1du6EafPej-Zmw-Hj3XEjE1_eHXAJgPPun1Iw8so6Ch_MoXRZBtEa9ERbe7G_EcL8pF1cKtOWG9pTC0UedcMp_vkn6zSBQWJiuuYw4I7AnGjMrnbJwYyclJEn0uU3h6hEwY6heNgzm2KK1IefOWd36-tmPzkSuIZHDK0Vsg7S7_pzW1uDnywNejm2nl9Rk_l1JKwxSfzyR1QXmNjrMfZL0zQ8rbRhJa0-DoySDyJSHZkrXnSUiOI_Y2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab00af27c2.mp4?token=P_iZXHjK4fFws1xB7K7iBY_fQxdKSTdsvMIuWB87KAbfZXQm8l0hbCnewKiVDgR35qlNtA0V-bCkIhdjHMqqUGnzkjc5VF1du6EafPej-Zmw-Hj3XEjE1_eHXAJgPPun1Iw8so6Ch_MoXRZBtEa9ERbe7G_EcL8pF1cKtOWG9pTC0UedcMp_vkn6zSBQWJiuuYw4I7AnGjMrnbJwYyclJEn0uU3h6hEwY6heNgzm2KK1IefOWd36-tmPzkSuIZHDK0Vsg7S7_pzW1uDnywNejm2nl9Rk_l1JKwxSfzyR1QXmNjrMfZL0zQ8rbRhJa0-DoySDyJSHZkrXnSUiOI_Y2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اهدای مدال طلا به بازیکنان اسپانیا توسط پرزیدنت ترامپ
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/alonews/135847" target="_blank">📅 02:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135846">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JzcQzsWzEQLfFYEcLGIvmBE47osNWDbABMY7Uv1StwbhtNE-EFr4O0WtN1EKZvnRLOWGoWxFMRU3qxNlj6MEvJHVWk9E0MUZvJOZ6rVclB1bdbxjFYAaRFMNS8dOAb3lRsfCoDP4rnyLVNI4kNhZKxeBMofodd4UpNHirPKp-3W0DsVGmg8vpaZ-xBPTI5BCYFYhcpWoaUoMKhg_IFPcU9f1jJ-xyH4wN-usA3R7AhwE61OV4daLkELPHK6c6GsyujwLu2q_Yp1mZzXh-mL5MvGybCg8nSLzryiKdakYtozeJ7_Uv6DxmL0uqswsJ3qqGCPijkUcPvu9msA1M7Naqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت عجیب ایتا
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.3K · <a href="https://t.me/alonews/135846" target="_blank">📅 02:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135845">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mLH_3H2uQ2uY4ETXopgUGKVmeeOQwRWgMb8CLDNIgIjGqQQR6p4rQVBh6LFezKc-sFMh4bld3Xsksm8zJmsgsUW4sAHP3g20yuV-V81amp6Ckka210v5-RD0W-uDZqzc7bXKvrux3TMB40xfTmFYH5PKvRnhq4MLocYDvIoQ6uiVjHpRXQmBmDibc9eY2GY6icznr-6PphLeIfJM5-BoDXw3Tchx19eoqfOBv6BtYoLno6PxiMBZ8G1ZU_UoLeaQFQhB6kionjaNlvHytc5pUhaOSEc5rtXDxgUZ87xtcNwoTqZgcL4b1UpZ1K67gKb1jOosrhtPMnXOjG6OiB4U2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گریه‌های مسی
✅
@AloNews</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/alonews/135845" target="_blank">📅 02:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135844">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
مسی گریه کرد</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/135844" target="_blank">📅 02:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135843">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
مدال مسی رو ترامپ داد</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/alonews/135843" target="_blank">📅 02:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135842">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/od71Jtz7tYBHjbCkSp5TiDJ2D4mbsHogoqZvS12rJm9SSR1_HjmVd2hFuUzR1bKWg_YYxpQm-hq966j-q6NLN9BBLDn_7xdGW4H2-WkmP0d8n3h2lhkT0ajZlC8N7wTRHvfz-eBmcsRjpNMuQruJ-6BWZExYAA-6f0ihICkgI5KRA2bXUh9hOjbQww2KzgBCiAq8FbNbNvklBCyHgY353bCi4V10YLE9chdXORvlC-wkFQfWtZg236mqznmO98knex7ubPM3DvtZjy30XUvfTgABdwlYZcf4tHiJoIa_S3XQ5k8uPMFVyKJvfaEz4XWuKj8YtmexCt2pg8euja1GHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ و بچه‌ها
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/alonews/135842" target="_blank">📅 01:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135841">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
ترامپ برای اهدای جام اومد</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/alonews/135841" target="_blank">📅 01:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135840">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52273b72da.mp4?token=Ffa2gMuCKRpN_-_3I3Tw5rU8b8_xvlQ3S7Hmj6d2tivF5eoIZJMY3lYJBfNNE9VlNmu8OzhX64oYNutwvwwaMm7lGaJ78gffbqOPFe6rRC5tyIvAnZ4bEuTJi4SFYCCPVxA6Fa1cQhVqja58VIMhMgajlRR4YHcTZOTE-C2_2LEiYAhgISuLh2ZzvfGgHGGMVsfKnxli7ep8QcXZBYRh55NO1Rpn_WzG0vOwJSJiNJpqTpd96wHBqqcMNgsoAIR6CEV-tdBMNiwV9ErbvDqITpXufP_MgbinTJSwu6xs22dpeowL45F2AKT2tJN3SkSOeLQefqGP1oy7b7_IRjP5JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52273b72da.mp4?token=Ffa2gMuCKRpN_-_3I3Tw5rU8b8_xvlQ3S7Hmj6d2tivF5eoIZJMY3lYJBfNNE9VlNmu8OzhX64oYNutwvwwaMm7lGaJ78gffbqOPFe6rRC5tyIvAnZ4bEuTJi4SFYCCPVxA6Fa1cQhVqja58VIMhMgajlRR4YHcTZOTE-C2_2LEiYAhgISuLh2ZzvfGgHGGMVsfKnxli7ep8QcXZBYRh55NO1Rpn_WzG0vOwJSJiNJpqTpd96wHBqqcMNgsoAIR6CEV-tdBMNiwV9ErbvDqITpXufP_MgbinTJSwu6xs22dpeowL45F2AKT2tJN3SkSOeLQefqGP1oy7b7_IRjP5JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قلعه نویی قبل از واریز 140میلیارد پول
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.5K · <a href="https://t.me/alonews/135840" target="_blank">📅 01:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135838">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QczISdx46XLBmFkVY3SojE6Od2wgKxKbbGND7yVj-6jqAYNdTn4DMLhvwIVpOoHxlQcYs3UJtrvZ5soB-KsGlAP5251MKTKjrdhiHZSkcacMyYwej4KWiocJhy0CJdn41Sbu-CAigM54rOYNHOIFzkarXeAuwgwXrsOSfF-soIY5uJqEJFpDN6rFrFycNM8m6y-QszpG1DDDdlpLwWTvLDSQxgv6QsuFPQAu06VG4CjXxB2i_c0oOBB-CuktZ_gCkByIaXZOEY_VGO4jWqS1nEQoLBCdSixj-8B0SapN68CA_CNqZkbDEQqjBCrg0GQOn6fL7qYdTRz6JbODxYqaoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tAM0Njnsb38nTYXmYIFeh7t5so1_0ekzyCoMVPCJdoe88T-dby549y7-uVe15YOy7r-ts7yc3-3J-7v_I97aLt618BV89tim91PbFhiOKm_yQg2L9yY-plymGMhnJHe9hdm2H96YFu_Fi-TaNu9WHrC0rcJnpwD6sc9Kcv9b2H0aF8F5_oY6mkZzdCHoVSn4vG57uXAYEkKcU3yDxk7H2fuqDvp0H2QoIoHmKftck0Np_kVq_q0t-CpTc_mHo8DW3bCI3J1O-FvfNX1cp3rMExEQfuI1eukLHArLndokaD0Lp-d9GJZsqXWRC46pEubeqblolxjT-KQExnJ0WEY-Jw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
مردم روی این دختره که امشب سرود تیم ملی آرژانتین رو توی ابتدای بازی خوند حسابی روش کراش زدن:
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/alonews/135838" target="_blank">📅 01:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135837">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a6163e56d.mp4?token=f04ZEjpHpbvTOaE1WCm93nIAfxY4EfGAtdk-i2cRfinMlcoyE9WRFJKwJ_-w4CPmsmi5kl1-Vt4aV0msMqJb2JOoFh80c3I46JpRpW4490MZs_6WLUGvKe1KMf_gKBz7LjpFeLGM5t-fqT9qfT2qNmr1fBIuuyf7tVQi2aQzPcvIRdXDOpezdHHOzS5T2VzlhR8N1t7vFvjlGheNze2mITwvTsBJx00UPQiGYSPf__rok26PKCMwTFYYrLdug_FysTy57t72N2H7h06NkhIdEdwwjpGQDiu5RypWNGWfo6FJpFVUHKZ7b6tLdNIwky0AkRYcuUIGjSSTp6HaiPFwlTF_fuuMxOGcC4Va8GhckEpyZtkkeri6jK64YCbyzyeCQjjYV_BuPZ40T86aRe2wSf3TbQ5XAl4ILmZxu_r9-KLB3wEQ6uy30bo8Gpx153mKIC3PBoBd3w0HqX13Fny9-5jdXxnJ5D0lL_E9TjuO1zfLAraT3tqAkv-C7sVAgANZQh53qsISGWAeR7thDbBrFVMXqfBCcFPHjxD2JjxnwicR9rhJ7288678Nl9AVZTfijtIK5KwurlmohSM_yXN-j1isDoLLb0XLfdHzxmdiq4TP_fAeqVZYiOTRiPM37UEsPpbP-FO3OnJaa6faZy3BQFY-3iOx303ZvEwLxhaU0Es" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a6163e56d.mp4?token=f04ZEjpHpbvTOaE1WCm93nIAfxY4EfGAtdk-i2cRfinMlcoyE9WRFJKwJ_-w4CPmsmi5kl1-Vt4aV0msMqJb2JOoFh80c3I46JpRpW4490MZs_6WLUGvKe1KMf_gKBz7LjpFeLGM5t-fqT9qfT2qNmr1fBIuuyf7tVQi2aQzPcvIRdXDOpezdHHOzS5T2VzlhR8N1t7vFvjlGheNze2mITwvTsBJx00UPQiGYSPf__rok26PKCMwTFYYrLdug_FysTy57t72N2H7h06NkhIdEdwwjpGQDiu5RypWNGWfo6FJpFVUHKZ7b6tLdNIwky0AkRYcuUIGjSSTp6HaiPFwlTF_fuuMxOGcC4Va8GhckEpyZtkkeri6jK64YCbyzyeCQjjYV_BuPZ40T86aRe2wSf3TbQ5XAl4ILmZxu_r9-KLB3wEQ6uy30bo8Gpx153mKIC3PBoBd3w0HqX13Fny9-5jdXxnJ5D0lL_E9TjuO1zfLAraT3tqAkv-C7sVAgANZQh53qsISGWAeR7thDbBrFVMXqfBCcFPHjxD2JjxnwicR9rhJ7288678Nl9AVZTfijtIK5KwurlmohSM_yXN-j1isDoLLb0XLfdHzxmdiq4TP_fAeqVZYiOTRiPM37UEsPpbP-FO3OnJaa6faZy3BQFY-3iOx303ZvEwLxhaU0Es" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Comming soon.....</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/alonews/135837" target="_blank">📅 01:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135836">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
گویا صدا و سیما مراسم اهدای جام رو به دلیل حضور ترامپ نشون نمیده
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.9K · <a href="https://t.me/alonews/135836" target="_blank">📅 01:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135835">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oIVdJ9vLRunhhLHVRw-w-s1XZWuVxMlI9o3yeClJ5Dx-LrunbLGkBK-aq9e0xQGaNxu1szaFVItKH9NyFinFaPHNTjhZVw2HNbUuRwWlUI5c9F7LIMD0pbp6SzsF0hmwlTcETdu-mEDivzvl7gmVhJCC_-Ne278RNKjPJoM49j77wbvdi47gbytoZ_GZE0Tk_-8Y4Kw38cDtKKHg6eF3x2li5UTm_M3aSKzvpcsXkiXbCvgsofIoKBXweHaXfAZvWkGpJ8su5CnIi9-nwxpwEqfQzhfI60t2v-gJLWgV36U04Ykdn2fDRu-nf-RkfNpGvu1YCrHGJD09BoowUyKrYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت مسی بعد بازی
✅
@AloNews</div>
<div class="tg-footer">👁️ 86K · <a href="https://t.me/alonews/135835" target="_blank">📅 01:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135834">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">اوه اوه پشمااااااااااااام
😐
😂
هوادار معروف آرژانتینی بازم تو استادیوم لباسش درآورد تا به بازیکنا روحیه بده
😐
◀️
◀️
◀️
مشاهده فوری فیلم</div>
<div class="tg-footer">👁️ 85.4K · <a href="https://t.me/alonews/135834" target="_blank">📅 01:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135833">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
تنها دو تیم اسپانیا و ایران نباختن
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.9K · <a href="https://t.me/alonews/135833" target="_blank">📅 01:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135832">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xzw_Gmdms7SGIIaRfCWq_rnpbzSDhiyDhS05eNG58DFKBvL11swBsx_b0Zkn_E3CLLbxNS_yxnPxEuVoRJZ6S5rWJWr-redR7oZPEHQeWW86rxVY69Z_N2DijJfW2zEcWuTJHCmf8IIgltXwgdxBC_9NGY1VeySLkxGDi_GPtNvrZ6O7kCFFQ8kRHG7uRCPMkE5wFiikNIoyqbNuolpSxcMvpg4Hgxzj0BgBUjoJ4r3OzoatYHRVhug7_koixei1FasSn7oULPRH1s6fI_vAjJbtftkoeXiyFcqsFAPPEwwAGoHssWTqOQUiValltoHsBKPJypR0snKHUmIFIsN_5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دلیل قهرمانی اسپانیا
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.8K · <a href="https://t.me/alonews/135832" target="_blank">📅 01:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135831">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">اسپانیا با شکست آرژانتین قهرمان جام جهانی شد</div>
<div class="tg-footer">👁️ 81.3K · <a href="https://t.me/alonews/135831" target="_blank">📅 01:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135830">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">تمااااام</div>
<div class="tg-footer">👁️ 81.3K · <a href="https://t.me/alonews/135830" target="_blank">📅 01:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135829">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
فوری/چند سوخت‌رسان از عربستان، برای عملیات علیه ایران بلند شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/alonews/135829" target="_blank">📅 01:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135828">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
فک کن هم طرفدار آرژانتین باشی هم طرفدار جبهه مقاومت</div>
<div class="tg-footer">👁️ 82.8K · <a href="https://t.me/alonews/135828" target="_blank">📅 01:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135827">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">کجاش آفساید بود آخه؟؟؟؟؟؟؟</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/alonews/135827" target="_blank">📅 01:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135826">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">آفساید شد
😂</div>
<div class="tg-footer">👁️ 80.8K · <a href="https://t.me/alonews/135826" target="_blank">📅 01:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135825">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">دومیییییییی</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/alonews/135825" target="_blank">📅 01:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135824">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
مجری تلوزیون: اسپانیا طرفدار جبهه مقاومته و ما خوشحالیم، این بهترین جام تاریخ بود چون هم ایران هم اسپانیا نتایج عالی گرفتن
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.1K · <a href="https://t.me/alonews/135824" target="_blank">📅 01:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135823">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UkMJv4fqe-StabwjI2Ivp-s4lY2tCkwaj6n7r7BcI7ldGlJxUsJYjcmwTIOqV7RwI0JOkeFWPaplxxO7yigCAfwrNsyYAIwuMkSZYunWDyerTl6-IssiwMhdUeS9y2FErwMQ9ekD-5MWnHVMAO-1evD3WyW8fB-UgkuE6-WelZHtoPks3_y-xq3UGtNGGWluY_1lzZzhwp_HRePh4lTr90-Ga3iviA1wk9KqiTUGka5vlbZ51QCKFeA6uM9mfWUQAyDhGTPlbDeOuMkNSPa33sN5K03FVqaWs1brdbYAzNh_Yyj2Syo5mAdNqlIacqOuQuQNumNnfyzqyz24nAzQlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینفانتینو بعد گل خوردن آرزانتین
@AloSport</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/alonews/135823" target="_blank">📅 01:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135822">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/419e6d9637.mp4?token=Y5e3x_VEMT051GSb6t8-3x9MHm6QuHAuWUYnjP1jGab1cK2KEes1wmru49w6411M1e0UDuTMDP4exmjIejiqWOvLTxhAJ3wxp1n4H8jjwtl_vhrQDu-VvYKW4GS-MFlVG3pD4kK2Of0bc4KXZV5pnXFlirY7Iqx5cftbex4RBTf_LjlmTBRlDf61aaIX3pEJ8d13FTpXkgoGti5VtKlzc3THxxoOYVLs-5DpgnlSVOEE5u_90QGOMRJ1Ggw_BrQHvyYdoyvrtwLoLlOp4bxus873p358k1pqZ7TF4Ewm3Qm8FwEy1iqP-g-BdU_gV2ImKabAM8GhTa3BXW88BswVSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/419e6d9637.mp4?token=Y5e3x_VEMT051GSb6t8-3x9MHm6QuHAuWUYnjP1jGab1cK2KEes1wmru49w6411M1e0UDuTMDP4exmjIejiqWOvLTxhAJ3wxp1n4H8jjwtl_vhrQDu-VvYKW4GS-MFlVG3pD4kK2Of0bc4KXZV5pnXFlirY7Iqx5cftbex4RBTf_LjlmTBRlDf61aaIX3pEJ8d13FTpXkgoGti5VtKlzc3THxxoOYVLs-5DpgnlSVOEE5u_90QGOMRJ1Ggw_BrQHvyYdoyvrtwLoLlOp4bxus873p358k1pqZ7TF4Ewm3Qm8FwEy1iqP-g-BdU_gV2ImKabAM8GhTa3BXW88BswVSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گلللللللللللللل اووووووول اسپااانیاااا به ارژاااااانتیییین تووووسط فرااااان کوووسه دقیقههههه 101
@AloSport</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/alonews/135822" target="_blank">📅 01:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135821">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">اسپانیا زد. فران تورس</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/alonews/135821" target="_blank">📅 01:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135820">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">گلللللللللللل</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/alonews/135820" target="_blank">📅 01:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135819">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KW3pCHzt2ImYKY161s2a3O2Un0zrclCqvAUYR_21CEZnUT2b15HvtlOsgmCm-5OGwWxHy9Z6OvLqpZYp95Bu6zNaUFj3Aqw7KUfyipM1EM43WBlyZITZ_v78ex90VhQVFBUr9T8zRPr8KDQan-EmYuMmy76h033_eyCyDNeYcn5Yaj5hH-pSqWkb17A4pjsPiy4Mjl4FHPws418xK8ZlkC8FiNLzCqochx73ZLaG-7whu5WVCooH1f-C4j1teGjQlPPlg_bx0IDnV6yjD470cvF77-R53J17_pjWenY6SCkMUtzCFlKjiA-Luw6jTW5ErLvwjeN72EwHM1E5z-ceWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پسر فیفا
👍
👎
؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.9K · <a href="https://t.me/alonews/135819" target="_blank">📅 01:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135818">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
مقاومت اسلامی عراق اعلام کرد در صورت ادامه تشدید تنش‌ها علیه ایران توسط ایالات متحده، مستقیماً نیروها، پایگاه‌ها و منافع ایالات متحده در عراق و سراسر منطقه را هدف قرار خواهد داد. این گروه افزود که در روزهای اخیر هیچ حمله‌ای به پایگاه‌های آمریکایی انجام نداده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/alonews/135818" target="_blank">📅 01:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135817">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tlHKmb_Wg6Uiv636pOQj6yd3kVxKbr6TINgFkthDxhn3RCqy4gejI-8EqH-029_DQ4M9ia88ureDPmF-tBLEaPWjcVh6Wf0YpqRbVrWdlF15JNrP4BeD0H4AU9mywOddTNZXtJl7QFqMwqd0-hxNO5WgsQcvcfXTKPSCyg-fpj8alMb0irjsPxWaYBmvCPY-QV5fRW4BgsM3toanaIL3wRV03INjUXCbOXa3uzrRoFNVDKlmJ9zeGb8FAdTKS3nxNuhlrSw_AdvMuS5Y3EzYNAKJerKQEnZgDpE3D4wjWd9HDD91aRr6YLaigQyKnHb137dMUbfJxlZYtlLKvo9wSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اینفانتینو بعد اخراج دادن آرژانتین
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/alonews/135817" target="_blank">📅 01:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135816">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0f9afce47.webm?token=UNzzZHXkM3QluLkDfOSS4vvwKhyu9wd8mIKKctlMYip9t2P3JgDek1Co30CS_6z981fZ3VR6mB32r36HR-SOZgYytVZov1DwdBTg7ED9lSbt69FQNU-dX-p2dR0yE7SnIvvBD2BN8WHIrMbE6-s__hIeSuVrdqj6uFnbPAW2rJsGJUW9n00fjxEDY0UXZx7iqL7FBo0ZbtamFIFvQZyTyPtsgqEeCd_apCmUqd-ZtF_5FveQqt-jOvb4SI6_Y4PDXZ0WKJ7GnLP6LeuXgFhenJumJszPphTNOCLFXuhAjxOQx9b2vD1umxYrKwQxNNom620Z_x_Uw2RyzSjAqQgQhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0f9afce47.webm?token=UNzzZHXkM3QluLkDfOSS4vvwKhyu9wd8mIKKctlMYip9t2P3JgDek1Co30CS_6z981fZ3VR6mB32r36HR-SOZgYytVZov1DwdBTg7ED9lSbt69FQNU-dX-p2dR0yE7SnIvvBD2BN8WHIrMbE6-s__hIeSuVrdqj6uFnbPAW2rJsGJUW9n00fjxEDY0UXZx7iqL7FBo0ZbtamFIFvQZyTyPtsgqEeCd_apCmUqd-ZtF_5FveQqt-jOvb4SI6_Y4PDXZ0WKJ7GnLP6LeuXgFhenJumJszPphTNOCLFXuhAjxOQx9b2vD1umxYrKwQxNNom620Z_x_Uw2RyzSjAqQgQhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: آرژانتین امشب قهرمان جام‌جهانی میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/alonews/135816" target="_blank">📅 01:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135814">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/ITIGqZnwfnobmGTrWRRC_ZrNzlYFNQ7XFxGIcmaZsX0c_4R94lrzzO10BjAu3ngtCTfLK9DbXzQVwcyMQ1d6I3Iyv1N1vC7QFDvcdlCeEeHtx_nLyhU2rV1rInmVJv_l-tyyU2SsOWMzfI864UdETOpUkkykZw_qq0snvrX5bnwcx_xO9oOYYw5pbYF7XUpG-DeYzfVhwZisqH5No9M_4D6OYqpD8GKMa40sGfDvt_TugCUKNzx1Ck43QChGm57euAbepAEuJ4BHJ-nfepJ3GN7XMq5n3E69vOlOD13Nsz24Rt-27zCHW4CV_xtJaPT2jdgPfg7oScBNK7HzHL8AUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/a_NayItX7DdhDdDZzLh-MSmZxHKa6cSFRNwFKEAI0SrioAPdvXBtWWowmmXJZZDaH4CHhlHua4Wi_xSclz5C-Z5lk_58T8BEPGGMYGYyP6sGG4R71f8QT6_8WGBwAe73YWDcnlZkw1WwGjvBKtupt_fCAQet5PANdnQwqpVFJnbRPK0aCO6NZpA-QXYt826uU4N50o_jGrah7tJl8wF90NPwMUBJWbmKGPPI_HtWTP1IU2HSSs_l-yzyqMSFUkOvBVoI8-q44R7kO4UiXqeYZvUR7newxZ9N-30Fm1d0ZQjLrr0jHaQr9LRnN5FXjf4QXX7NjlyuWNqLp4TAcN7lcg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
آخه این کجاش خطا بود؟
#لابی_صهیونیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/alonews/135814" target="_blank">📅 01:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135813">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ttzdvsqBIvNEz7oV-dUtmDxyvRFBSlxIIt4cl2VMhT5LIPGx9TSY4V8-HBvhvx8Ug0ZqaIDpYJrxOsyghHqdGami4OaQyqWAfsWiiqPj9U-Ki-TzykIi3K6D8ZAIML54xH-Xo3z2wwfctyGdcGtGw8CczfOz8ezZcI1HoRHHC1m4ofFBFJqClD_fzoNbIrVBze9cCJfgjpLrtaQskPgM5i5oCzsCM3HvtgOogPt553m16fDdA2Q-6r8sIYxF3x1fgrLwcUbhJVA_562vjp1_RwK2RZDquOWFemHlAnaCOT9_F6IUJY-PoshBNLjFQ9zUFWFYjRNkORDDZGyvyq_q4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پرچم شیر و خورشید پشت دروازه
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/135813" target="_blank">📅 00:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135812">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
داور حکومتی
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.9K · <a href="https://t.me/alonews/135812" target="_blank">📅 00:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135811">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
اسپانیا گل زد ولی خطا بود قبلش و رد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/alonews/135811" target="_blank">📅 00:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135810">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TWsVyLcQZUwJ7sxvnfwhjpVPvQNySjhzSspWgj_Zv7ZvlbctRDPDvPx1a29SCjvXyyIBuKuptnGKvzhrL2Lrdi1Ndgl07y9PYp3lhDxBGqoh2L9iawG2B0jm4uSZNYxe8ov7Oi8ErAAxfCZrtAlE49Rj7sZWccfJt4CN3ZtB22L1mwaA6Kzz7lAb4mRUeCBVVb80RGZaV1QE2HXZPQNW3L4hVT4RTOfl5P3hOWqFm3vn065kQYDMrCj70zXplgpOXfsinVceiuryMI_YFWrPDcUUsBXOTgrg8ZdmdiVWPUamzdcKeiDtBo8Z7-ICWvhz7RbubP1FrU5mybbap7phcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دست خدایی که آرژانتین برای قهرمانی نیاز داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/135810" target="_blank">📅 00:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135809">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/skz9IIW0yaSKFKJE7zlUkaDTfssLQVY_3-BggI1IbNwhkeaWQKyYER-OfQPVytJsck6w5Qx4NjJWPLv5q9U3nrmRcb18bk37T_RSo7w8SMPX0SkJITa0IjNOKW-o7aMkqV8a_s1XNjsohkhtB9PFP3jVe7yOcu4Xz9uFZ9au8VU9MdNwdfiR9mgY0UbXWIX64F2pilSLwSXjn06mrJKseTCZlXjQ3HdO2q2YPe6PNbL4myfoWw9iYKADcuTK8BA7BrRY_DCjNq2gKihBQ_gtU-xxLJrQ1O0yQvIliYyMtXdUZk20ZG5XxoXl07hpO2fjki35xEKB8OKL7l7g-E1ZGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام اعلام کرد که نیروهای آمریکایی، از زمان از سرگیری محاصره بنادر ایران، ۶ کشتی تجاری را تغییر مسیر داده و یک فروند دیگر را با شلیک غیرفعال کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/alonews/135809" target="_blank">📅 00:55 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135808">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HCIbK-DC86hsVtaeqBms3srul_mIT7oOSFe0devN3vQERmT3MOCzauiyFiYJWeOGwtRW67_e5dJL6nH_fnlEzTpdWP8UFZA1RRZrWqKFANSHxdmti_NVHHey9VdRK4ZEubhpf_4ZUhHQY452T30ugQza3wocBum-idd5HgMwo_iMf-R51C44p6vyioBZc7oRimwSzyKOYOv4A3M8vsQhJg49cKQ5RlP2NeKiZ3B9NHPfNEafifMsq52LnQnaRG26TW3PtF_Hs6AAETH0EvEe_DSiwaDg7tGj5NXymUEVQWVuEKKqN1wbLG8UkPLpJrXhq5ouiinsQJG1WNJeZ6Wjtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آمار باورنکردنی 90 دقیقه؛
😐
آرژانتین 0 شوت در مسابقه ثبت کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/alonews/135808" target="_blank">📅 00:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135807">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6f213bec9.mp4?token=ItdxyOkKdmKI-kZuy4T_7bodsGaEPPvAWlb1JT2yRVGsvIUqRx0Kkyk1T9nQNuoZlGGCVRisPPfB-aXTDbU8q8KajPJv5NW1Twmk8brX6y8qOeaehvD3HxRyJ68IZzON4Zpgt8wnmCu6kJ18TlMIG9cdohVtTzg-qutBLcLTehKLWA7_p24L7VMyp639G2619IskYTtCXI1REA3_5uOnmnlZ6EuMZsWL6Tvdo3DHJsxSp8Y73uNVEtvNnV3TUGAHKnpLFiE8S4PXEyLcYZ-0Cdy730tCmfY0UNvVCELB0L2FpgFZUwt2E5vazQ7dq1bkf8Jm-7mQDNe-znX_aU1MRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6f213bec9.mp4?token=ItdxyOkKdmKI-kZuy4T_7bodsGaEPPvAWlb1JT2yRVGsvIUqRx0Kkyk1T9nQNuoZlGGCVRisPPfB-aXTDbU8q8KajPJv5NW1Twmk8brX6y8qOeaehvD3HxRyJ68IZzON4Zpgt8wnmCu6kJ18TlMIG9cdohVtTzg-qutBLcLTehKLWA7_p24L7VMyp639G2619IskYTtCXI1REA3_5uOnmnlZ6EuMZsWL6Tvdo3DHJsxSp8Y73uNVEtvNnV3TUGAHKnpLFiE8S4PXEyLcYZ-0Cdy730tCmfY0UNvVCELB0L2FpgFZUwt2E5vazQ7dq1bkf8Jm-7mQDNe-znX_aU1MRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ببینید چطوری زیر ساخت های مهم وطن رو زدن ولی یه عده حرام زاده نفهمیدن چون سودشون تو نفهمیدنه.
#علیه_فراموشی
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/135807" target="_blank">📅 00:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135806">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
جذاب ترین بخش فینال تا الان این بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/alonews/135806" target="_blank">📅 00:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135805">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
میثاقی: آه مردم مظلوم غزه و ایران یقه آرژانتین رو گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/alonews/135805" target="_blank">📅 00:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135804">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
رفت وقتای اضافه
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/alonews/135804" target="_blank">📅 00:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135803">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
مجری تلوزیون: مردم ایران از آرژانتین تنفر دارن چون حامی اسرائیله
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/alonews/135803" target="_blank">📅 00:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135802">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
آرژانتین اخراج داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/alonews/135802" target="_blank">📅 00:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135801">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
فوری/انفجار در بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.5K · <a href="https://t.me/alonews/135801" target="_blank">📅 00:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135800">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">الان ترامپ میاد وسط فینال میگه ایران نباید سلاح هسته ای داشته باشه.
اونا میخان توافق کنن…
خواهیم دید چه خواهد شد!</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/alonews/135800" target="_blank">📅 00:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135798">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a67fe75354.mov?token=g7ZhiZj6O_TzMqlVxFwmeYoF-Qan2fHQJwutLB_2fqOPqqyIr-F-CtwidTmTo9mzyOkDEri1q9Ch3y7C_t56OU6KW3a0VJxSOx-s7XuoYYft9LwZGLcZL6HWIHIG16oiAZl0TD26MPMk0DMBCSiPFpHdHhSDRzahDmKDYiyvDhcya-8IUGV4sLTOCpnffmp6ccYb37nupJFNZwF97_X0eIx3-lGfaAnXt5amGhfUfo6QsWtJXYzWL_W0l-Q0xSCaWFnhRGHBa9mFxUNNOTyxe_VyI9xRxx7CQsQe2Pj1XZ3eFIyO-uTjv2O1lcye37XrGeVyjcn4TUkq-B-EQC065Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a67fe75354.mov?token=g7ZhiZj6O_TzMqlVxFwmeYoF-Qan2fHQJwutLB_2fqOPqqyIr-F-CtwidTmTo9mzyOkDEri1q9Ch3y7C_t56OU6KW3a0VJxSOx-s7XuoYYft9LwZGLcZL6HWIHIG16oiAZl0TD26MPMk0DMBCSiPFpHdHhSDRzahDmKDYiyvDhcya-8IUGV4sLTOCpnffmp6ccYb37nupJFNZwF97_X0eIx3-lGfaAnXt5amGhfUfo6QsWtJXYzWL_W0l-Q0xSCaWFnhRGHBa9mFxUNNOTyxe_VyI9xRxx7CQsQe2Pj1XZ3eFIyO-uTjv2O1lcye37XrGeVyjcn4TUkq-B-EQC065Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرتاب موشک از ایران به سوی اربیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.2K · <a href="https://t.me/alonews/135798" target="_blank">📅 00:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135796">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0dg6JAE2vL8uKP9fOxTHntSR15B2I5SWBUyH-GFmHybsiD-NbfPZYjX4Kqt74zCgfPwsn1bA42hKB0_4KpILZ3KlW0jFAEtK7f21pPLkcZOgXh4IjoDWSoFnfswoYrSccPbzrcc3disC0Ld6qeiMP7CB90OCWusId_NJzidkaHGIOqD3m7aaI0pR4XZHOZulaZ2v7NrSJL0dpEQdprYeEfXAuB9K0Oe6bBRdls264YfyWfdTUBKCR85f7lY8SmXaJfU1GXaN8XIFVYxtcI_x7HgGOVnnLRbeK-NYOKMhKeCSojusbaiTj_3DcqlC-Ecrn2BSK7Xp9jQaxw_kX97QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاتی جالب از مراسم که یادآور تجمعات شبانه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/alonews/135796" target="_blank">📅 00:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135795">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">نمیخوام جو بدم یا ته دل کسی رو خالی کنم ولی این چنلو داشته باشید بدونید چ‌خبره :
@khabar
◀️</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/alonews/135795" target="_blank">📅 00:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135794">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
فوری/واشنگتن پست: آمریکا در حال برنامه‌ریزی برای جنگ  گسترده‌تری علیه ایران است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/alonews/135794" target="_blank">📅 00:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135793">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-text">🏆
اجرای کامل مراسم بین دو نیمه فینال جام جهانی 2026
@AloSport</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/alonews/135793" target="_blank">📅 00:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135791">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
فوری / گزارش انفجار در قم و اراک
🔴
ممکنه شلیک موشک هم باشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 86K · <a href="https://t.me/alonews/135791" target="_blank">📅 23:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135790">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
فووووووووووووووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/alonews/135790" target="_blank">📅 23:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135789">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
فووووووووووووووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/alonews/135789" target="_blank">📅 23:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135788">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HrmU1tF-sYpjg_MX6tz3Ncnaw9fEMazaDLfthamvzDgAUArNPIVW8PKCEYkztdcOnoWaa-P6G4tsb0LgM27fslmNbqqQckQNB9B-PJ5Uu8skBKMUvCQuCnf5MtVGhCFHSej66K1Gjbbbbm6MD0XJptFT7B5Ww4_B_qqz1QUPa4Xr2_gUlTTQ8VlnMtZ2qCXz-iHxALduPj-FwXNsnG4CjIOMQRg99HFY_FuwaKUG-g9qJleqo9rhn3Phny27FSrHyKz6jiPi98W84va9qOEAWr5dC92mWDwTbp4--81dTiVWIKFXH2DZMGdyt2vwf1WtBwqqB8a_uvrUACFvWr5A0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاتی زیبا از اختتامیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/alonews/135788" target="_blank">📅 23:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135787">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
محور قدیم بندرعباس - کهورستان - لار بازگشایی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/alonews/135787" target="_blank">📅 23:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135786">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-text">عادل تو پخش زنده: آرژانتین بار ها ۵ سانت و ۱۰ سانت و ۳۰ سانت از حذف شدن فاصله داشته
😂
@AloSport</div>
<div class="tg-footer">👁️ 85.9K · <a href="https://t.me/alonews/135786" target="_blank">📅 23:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135785">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
از اجرای بین دونیمه و شکیرا لذت ببرید
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/alonews/135785" target="_blank">📅 23:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135784">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YExjjaDjXdJQ7CSlCczo2HYmxanAb8rt1Dj3QBMYVcrz2cyz9yrt_3b11UQ8eVWCeIo13WMD-jjinRWyMZ0XWy8qHrYc0PRwaJHoeArX0GU2QUUwaM6G_mDWgux6dgEM7M_vP4H5I4WC5zlO8ni4Gt8OyL2-IZVVfBZw-PMUojET9q29LOvCua6pfbQMd7CUC07xvmNZPmjKojyEoB3UBS8nodCpFWFe9x6RZjAVGs_Vd4I8goOLu2LMGZQc0EyT6o4WZ7x3DfymQG5g56uZd2oq6pRZxoprVZQkNSTxFYwOt9vxt8_c0_Zu1_CcM350RqrK0VqMrnn2Ahi25igJBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تماشای بازی نیروهای ارتش اسرائیل تو لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.2K · <a href="https://t.me/alonews/135784" target="_blank">📅 23:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135783">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
اجرای بیژن مرتضوی بین دو نیمه فینال جام جهانی
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.5K · <a href="https://t.me/alonews/135783" target="_blank">📅 23:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135782">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7492701943.mp4?token=OnyeJKveunLyhTDNpKbD_fptU3Be930BzTWDWWdMgPNVPkSgAg8-iM9bwbl9RoL566K43SNk74q1WB7nVcsoyqxvm01O5rwSV90Xek2LYyg1Nl7jVsR8iTCptWxwKQ8UUVWpgsgSMPXpWmhwzLn4PNPWqQARKUXEgR58CRGmgx5tDUwslVaLTQb4Oo0tXHqkaqnOwlDZmujHLsBHT42oLzdP4HPeI_sYLT2arB4FofTmpucjWqTsucxgWfzxl7Ld5OrCSCeLnW89G45fAcJAGM6TlqU3XPF_vS_LtLZsyjBGHhODcV3bxcti_1zwTe5wJnnLDp02ynivMnKDbdDrFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7492701943.mp4?token=OnyeJKveunLyhTDNpKbD_fptU3Be930BzTWDWWdMgPNVPkSgAg8-iM9bwbl9RoL566K43SNk74q1WB7nVcsoyqxvm01O5rwSV90Xek2LYyg1Nl7jVsR8iTCptWxwKQ8UUVWpgsgSMPXpWmhwzLn4PNPWqQARKUXEgR58CRGmgx5tDUwslVaLTQb4Oo0tXHqkaqnOwlDZmujHLsBHT42oLzdP4HPeI_sYLT2arB4FofTmpucjWqTsucxgWfzxl7Ld5OrCSCeLnW89G45fAcJAGM6TlqU3XPF_vS_LtLZsyjBGHhODcV3bxcti_1zwTe5wJnnLDp02ynivMnKDbdDrFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اجرای بیژن مرتضوی بین دو نیمه فینال جام جهانی
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/alonews/135782" target="_blank">📅 23:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135781">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-lkORT7pRBLCfaH9uGWdoDnbr0SmLOmYMbMES1_0ePi6FmD5K_BwEwjmJ78J0CprMI41goObdp8PrEpYLVqCwM1wD1RxKSm-liB2AAva0yqI3W2KJELglKOLqKF5A4s6IVQxKWANhtmZWj2StDycLvP7T38qP6K9zguHq0QjgcP3XW83eaecQkMaSc2lOTq2acogPbBwlQbktdaWSysWXF2DOby_e5h7LY652c2xHKHEprcd1uiEtD1oZok9Xxswt7U4twMvb7TY_B0UM78HqcMzX8eiD3Q1MgQmZ2-1veb0tnrfsCxBjA2AKJHjxM9fAy8t-sBkHAqdg4JuH0ZNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیژن مینوازه
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/alonews/135781" target="_blank">📅 23:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135780">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21017332c0.mp4?token=WEgrYwasRyvH9Y8t8-kNfK449gxmMdeGYKdoo7BFa0Z5SRRytH8AIeayEBQzYb450wTD_DATbgSWnLQPrY4U5MY2QdT9_xm-BIrE0IhDT_sbU-pCfYZaxUo45I8VsVcwaYOCHkWCsx-MQwdqNFYBpG5iGstpQ0Up_hT1DBW6zioxaappkTnPHBtFvxYSmPcJEk-zXNVa9xasxfCnFOoFhWZepURZ6F5Sq5nQMHTdUsStVVHCsauwXfeXCuNHU-GXmJHSweyr6_CupHSGh1oCEnhj2RGWQ9PsOfHDFtAhTZpV49FlDs0UQFLz9p4d0TLbBg-UZBt_AO_UQzgAqq5nFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21017332c0.mp4?token=WEgrYwasRyvH9Y8t8-kNfK449gxmMdeGYKdoo7BFa0Z5SRRytH8AIeayEBQzYb450wTD_DATbgSWnLQPrY4U5MY2QdT9_xm-BIrE0IhDT_sbU-pCfYZaxUo45I8VsVcwaYOCHkWCsx-MQwdqNFYBpG5iGstpQ0Up_hT1DBW6zioxaappkTnPHBtFvxYSmPcJEk-zXNVa9xasxfCnFOoFhWZepURZ6F5Sq5nQMHTdUsStVVHCsauwXfeXCuNHU-GXmJHSweyr6_CupHSGh1oCEnhj2RGWQ9PsOfHDFtAhTZpV49FlDs0UQFLz9p4d0TLbBg-UZBt_AO_UQzgAqq5nFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده از گاوی ک صاحب خودشو کشته و پلیسی ک رفته بوده اوضاع رو درس کنه
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/alonews/135780" target="_blank">📅 23:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135779">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
ببینید چطوری زیر ساخت های مهم وطن رو زدن ولی یه عده حرام زاده نفهمیدن چون سودشون تو نفهمیدنه.
#علیه_فراموشی
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/135779" target="_blank">📅 23:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135777">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RdoOC7wd_im8aHakzgNpvm39Tm5TgmUGimfDp_sVzqIZ9B08LM1toa63E2PpeQMgOlGYx8l5wKkutI-7UifLxV-lTOTFlcAmdlGmL1-hukx7sfi6yW-SAR_RhOj7bzukZuDrdwqgj4urMLr00WBnQzT10rx4uXcWn17lhECqLHEkh-N8tATYHJkUBcl2spNvCPilnHCMSvVZldjgCxH2uDh6xF2ZDVLoC8xT3G8_iE9aMjIL-7G8ZqBlLW7Gf6IOx86ij5A-OzBJdm9ntE0AU548d5fi3_q6j1tzRMmqvEmkMTt9arROTkWAxbZyR5PQCL6OgTX1pfDUwKUHBkNNDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pr9jBL3c-vZnZS3l3nqvE7dSBCUl1lFeukPjqiroAruma-ErvSs8rBZqUOgCNkWHvbPK5SWZizeDOXvS-s4KlJFluccQbNjKbofAuBVl4EPmu3w6cgVeLWOlIcu0ha0Zr2Vi21_fdQ4HDFkJIMQ0NpCVCNbrJctltu9KekFMb0iDPnWpYpm_V0YITQLhU-fKHsPZn_q1SNuLO3lNN-BKVHkmJBRwqjER62f1OpRAFBieazgEK_owymV18EL3z4PbGr6Jh71pILYlu0UpqZVzPjMpnAaTYim23oMbIZr7P4Hvf9nvHE2hIGAx6ABw8S4wd5xGczpMtlTp3BHrG15BeA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ملت موتور پهپاد MQ9 رو انداختن پشت الاغ بردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/alonews/135777" target="_blank">📅 23:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135776">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
اسرائیل هیوم: مقامات می‌گویند سفر برنامه‌ریزی‌شده نتانیاهو به آمریکا برای شرکت در مراسم تشییع جنازه سناتور لیندسی گراهام در هفته آینده به دلیل تنش‌های امنیتی منطقه‌ای در معرض خطر لغو است
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/alonews/135776" target="_blank">📅 23:32 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
