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
<img src="https://cdn4.telesco.pe/file/TpaV0ml2c3MIAnzTZVEg2sFKcvT_DAL42RO67qEmpHUk9w7cKVpVnicdTPAmqbNTgMelC7piRCRYvDjEONi_z0ghn8ttG9ReM4BOI2NhCca_mTUZDoEsRR29pi53BIKU5YN1tvPCtl1HkknLp7zuLoQw_7t3sMbYeUwAr_76_f9xACEru5uNth7yCmWkYaMG5FGwG8oQTmiOuZD2fEGTFkEwNiyX6SQhMpvduM4ZBw2j-0UXOpz7A0PZrtv1jmwMedpenXR8sAVaKZSnuSrg5fhN4DijJNZ7_O9cwnrPf50GYPbWWtRdrUXBoB39l5e75H5RPwX0mXaL6IPSbl3CWw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 171K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-26 06:23:54</div>
<hr>

<div class="tg-post" id="msg-78009">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">شوت سعید عزت الهی از ورزشگاه رفت بیرون
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 368 · <a href="https://t.me/funhiphop/78009" target="_blank">📅 06:23 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78008">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">حسین زاده جا طارمی اومد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 768 · <a href="https://t.me/funhiphop/78008" target="_blank">📅 06:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78007">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">نعمتی چقد دلقکه
😂
😂
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/funhiphop/78007" target="_blank">📅 06:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78006">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">نیوزلند تحت فشاره
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/funhiphop/78006" target="_blank">📅 06:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78005">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">منو بگو که فکر می‌کردم ایرانیای آمریکا از ایرانیای ایران آیکیوشون بالاتره
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/funhiphop/78005" target="_blank">📅 06:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78004">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">محبی گل مساوی رو زد
۲ ۲ مساوی
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/funhiphop/78004" target="_blank">📅 06:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78003">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">از توپ لو دادن محبی شروع شد
با ریدمان شجاع ادامه پیدا کرد
و با جاخالی بیرانوند تکمیل شد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/funhiphop/78003" target="_blank">📅 05:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78001">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">واایییی گل دوم نیوزلندددد
🤣
🤣
🤣
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/funhiphop/78001" target="_blank">📅 05:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78000">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">علی علیپور اومد کارو دربیاره
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/funhiphop/78000" target="_blank">📅 05:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77999">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">چرا سکو ها خالی شد؟</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/funhiphop/77999" target="_blank">📅 05:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77998">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">آقا مهدی باشرف (
😂
) جای آریا یوسفی به بازی اومد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/funhiphop/77998" target="_blank">📅 05:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77997">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">فوری از سخنگوی قرارگاه خانم الانبیا:
به زودی به تجاوز نیوزلند پاسخ میدهیم!!
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/funhiphop/77997" target="_blank">📅 05:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77995">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8vdBdV4MPy2VBd71Zb1FuiHt8fAmf71VpT3lE-aip2xnji7qbLAInfu7ib58wt_948cKgsDGTspFf8QdHgGmbD_ezUujrt5glIlGx1-eJ23uSCRh_6Oww-C1ZdpLWhaXKvtNHcKJeam4VKEAVc1azO0ARiZvAQ300aIwjycOcyjr-c_LpfwXdgb94_LsUNgZnJcuCozub7Aqn-M8jUn_rbQWlUlHocsan2Dw31Yu5-9nthjkymoJw4i_YR4R36ckm3qMHlCqgNF1SUzPJPnNqLSYg4k6XbefwIIgGqZRmXVpFKFAnmcVD31-IRla8cpYUQrA1tuwLndCEQiPv4cJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
امشب اولییین بازی ایران که  داخل ورزشگاه بردن پرچم شیر و خورشید هم آزاد اعلام شده ، اگر میخوای بدون سانسور بازی ایران دنبال کنی حتما این کانالو داشته باش که تمام بازیای جام جهانی کاملا بدون سانسور پوشش میده :
• @
TrollSporte
• @
TrollSporte</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/funhiphop/77995" target="_blank">📅 05:29 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77993">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">نیمه اول یک یک به نفع ژنرال تموم شد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/funhiphop/77993" target="_blank">📅 05:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77991">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ریدم علی نعمتی زد ولی افساید شد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/funhiphop/77991" target="_blank">📅 05:24 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77990">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">گل برای جمهوری اسلامی
رامین رضائیان
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/funhiphop/77990" target="_blank">📅 05:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77989">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ولی شوتای قدوس>>>
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/funhiphop/77989" target="_blank">📅 05:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77988">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">این چه کصخل بازی بود گلر نیوزلند دراورد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/funhiphop/77988" target="_blank">📅 05:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77985">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">استایل بیرانوند دقیق مثل‌ بهتاش پایتخت شده وقتی ک سندروم میمون گرفته بود
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/funhiphop/77985" target="_blank">📅 04:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77984">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZu17L7qz6jP1nUiXbHpbdySiPSLJcSmmKA83AUVDIovABrkfq-OvzzOG3BPtpgme8pc0mn3gNU3OSe3T9ZWppAUcGtlNLhENtOFpIltnCKuVxDKw8tg8WkyrHLb6yRYe0Z447hqECJxaNWhtbKfLRDaZE9FQlPBobonF62NN6O_-iFhBxkKW2QAXokhmzyka7N8Xx_Qj9l0krZhnspOuRFds2rPYh_FEc30gPun6IogFVdQeX9r6jabpw87l8XLH0gs6J8T-CjjDOELEQNvo5vPIvuIv9iw1OnrrU1UPEqXiLf8xCGuLQIpTnQGmcK1HbiN2jW96e1fvGIGP1m3ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گل خوردی ک جاکش
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/funhiphop/77984" target="_blank">📅 04:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77983">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">عجب سوپر گلی زد نیوزیلند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/funhiphop/77983" target="_blank">📅 04:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77981">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
امشب اولییین بازی ایران که  داخل ورزشگاه بردن پرچم شیر و خورشید هم آزاد اعلام شده ، اگر میخوای بدون سانسور بازی ایران دنبال کنی حتما این کانالو داشته باش که تمام بازیای جام جهانی کاملا بدون سانسور پوشش میده :   • @TrollSporte  • @TrollSporte</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/funhiphop/77981" target="_blank">📅 01:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77979">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VZDF4XxRTnc9DOy6k8PiESxVInAoRDJAO1MrAoiu93SqAfNKDL1Q5aBULyhN6Er3TczBeBXNA0d1VWYS8ayQ0fUIOye7bwXGCUPdsyqXECY4ysY4UXVENuU1xIBc-PA6RZRCa2ArOKXTYIIskQe4mLlfmRUgrjrs69_qZ6MxIMU6EhOt4yBzyJ3ajr6t7X7RK-8omoEmVcMnrNk2PHGYbyXnbbQ_8T4sqMnZbu36HmtONACUzS80Kgr7fcN3v2vhaJgmcWn5DrFkPiDLb9w39dB3qbpnKAg4_8_vCYNROUZEPBmcckMdSvfnH-CjsFCkBJy7vFzTozlAQ2NflFPQNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
امشب اولییین بازی ایران که  داخل ورزشگاه بردن پرچم شیر و خورشید هم آزاد اعلام شده ، اگر میخوای بدون سانسور بازی ایران دنبال کنی حتما این کانالو داشته باش که تمام بازیای جام جهانی کاملا بدون سانسور پوشش میده :
• @
TrollSporte
• @
TrollSporte</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/77979" target="_blank">📅 00:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77977">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">بازی یک یک تموم شد
بهترین نتیجه برای نیوزلند
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/77977" target="_blank">📅 00:29 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77976">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">محاصره دریایی رفع شد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/77976" target="_blank">📅 00:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77972">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">عباس و باقر فقط از زنده موندن آقا مجتبی خبر نداشتن و سورپرایز شدن وگرنه همون روز اول جنگ رمضان توافق شده بود بینشون و توافقشونم ساعت ۹ونیم بعد از ۳۰ موشک به بیت رسمی شد.  - تغییر رژیم هم از نظر ترامپ همینه نه چیزی که تو ذهنتون ساختید  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/77972" target="_blank">📅 23:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77971">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jqDDFfP4uANmXhzO40NPeKyGluat3vaCZ_X2aM3jKCbpCOgmkz345mnSG-X_ss6HqIuBBlpUa1OqVxz4K6lD7v5VPz9tBoOQ3CBf1kEXRb_sndjXmjSg6zYtG12Dy2QsdIsivzMen9kziiMMCFEfbcYdKb6LBm1QvxfZh41EJUnQ0Kqh_pV6ltf8SW6Hap1GkbvqLcrlJia9xY2VlmlePTnFcf7WKqdKihUlY-D1CAFZc_rLI8vYxP2JxdKgeZcD0GLLcrII0YuNIqHu9CsIRUlM4eDzokZlrtZP0mPVuDuln4JvJCkX0JejzTk2ZLnVRdDpZedNf-RqmacP6aJ9gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس و باقر فقط از زنده موندن آقا مجتبی خبر نداشتن و سورپرایز شدن
وگرنه همون روز اول جنگ رمضان توافق شده بود بینشون و توافقشونم ساعت ۹ونیم بعد از ۳۰ موشک به بیت رسمی شد.
- تغییر رژیم هم از نظر ترامپ همینه نه چیزی که تو ذهنتون ساختید
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/77971" target="_blank">📅 23:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77969">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_BoXuzsRolD8cVUxWCHq88jr3EKU-NP5RUpEvW1Jqk9QAJOOXnDaPe0LOCC_xP3BdlQ4lTvN2dCAtTXZh3RwahhYp5YErvjQsoyHSvxFWe4fi0cBk5TYSuPsKi1QwFwZNQhi7iDw2wyEfMNImo0n-wauLRPgB8_STdJ_oMIARE5AmvTY2qBY5exAQ-aAWeIAh3nEbE5svnEpD7rOgeDnal8DAfp14ZdRaKUjrIK0MBQUlAsYgGRs_yNz9xe1pT518kCt1_baFWqUcBXo2aH1NYJ9PnjPEDHJCL-4hFjiwqo59Yy6-DASD-5IvphHlKFuj1JsL1SLAH3zJtobDxyOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایان یو واقعا کونیه پسر
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/77969" target="_blank">📅 23:05 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77968">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_ZlU9cAJYTA7uabyLPjmk-Iun9VWmX-QB4aYBQ6IYamfQJrPkstJvE-I3pbDtAGdfElAjN0F9jt_AHVypkAWw47bbUwg3Wd8xQBLOBurpwT1KbOAw9Byey-4OavwOTVIIpIJdQtgeKA1XzKg2tPR37WI0DUef26FSKmL2uj3OjHFCPWrc-kXD9mVlaVOymTPGqHLZMp1sy9I32BmobvDf2uNC0dTdIkjs9o_42_ZdO7RM3Zs9JGzd9WtSl6hIOArPBtRB1VW-YSjtou5tbvveMZzoNBFBm6iST59ZZSYFNaRUSrZDBQlYO_nUgrH0eZN4z3WdA1NsWNy90pz6Xmng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موزیکای قشنگتو بفرست باهم گوش کنیم.
🎵
🤍
گپ پلی لیستمون
🌓
https://t.me/ORGplaylisT
https://t.me/ORGplaylisT
https://t.me/ORGplaylisT</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/77968" target="_blank">📅 22:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77967">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">امام عاشورا برا مصر گل زد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/77967" target="_blank">📅 22:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77966">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">زندگیتونو بزنید رو برد مساوی نیوزلند</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/77966" target="_blank">📅 22:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77965">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmir</strong></div>
<div class="tg-text">اسپانیا بدون یامال در حد پرتغال با رونالدوعه</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/77965" target="_blank">📅 21:57 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77964">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">کیپ ورد جلوی اسپانیا متوقف شد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/77964" target="_blank">📅 21:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77963">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ریدن تو این بازی باعث میشه اسپانیا خیلی وحشی شه و بقیه رو بگاد و قهرمان شه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/77963" target="_blank">📅 21:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77961">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJ9aQsTlMtH2gbsYq9GA6z5oZuVA7m3yTTCkZ577dznpl85pXv4lG7ovKg9RL_94t-ym1n-IeYCHYaNqOWXoJMuiJ188mLLDD3_XnLmIq8SFLiVdW17jX5LSlDckpWd2NpPmdxerWFVPDnlV9CIX4ETHI5zrej4oU0gb-VYG9fRsiy7jYbwrddDo1k6RsmqgGcj3kLIx8Udi5Oo8GecqpT28_T2b1VT6PH5aiSLYok-KaN9NNalJcfjkTcn3F7-HcJ5ewB27bNBuU7njj4PXloLZ1Y40dReeI4uc8C1k0wWiy0ULmhs_37xwNAgSDWX1w3sv3cmrNFljIFw70rgbJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه جدید باقر شاه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/77961" target="_blank">📅 20:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77960">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">آپارات اسپرت با ای پی خارج ایران هم بالا میاد جدیدا، اگه خارج ایرانید استفاده کنید.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/77960" target="_blank">📅 20:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77959">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">قهرمان جام جهانی ۲۰۲۶ خیلی ریدمان شروع کرده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/77959" target="_blank">📅 20:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77958">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">آپارات اسپرت با ای پی خارج ایران هم بالا میاد جدیدا، اگه خارج ایرانید استفاده کنید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/77958" target="_blank">📅 19:57 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77956">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">فردوسی پور هویسن رو آورده برنامش
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/77956" target="_blank">📅 18:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77954">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SOncTAITIeAwCAKppEeBOwqWoLcuMcpz6yxYuo6DoBlSTLRR1ZGVPO94ep2zS0AO97jWt2n8kGzds5zW4Sg-Ajzb3rTCJ8nqWIzmWC6SuZUU8yIu_ze7ZpfSSx4sQCKxCQY_5JERg6NxLMHtX5UFS1raOf6eFFKLYtrv9JXQH47uImSb5ck1ts3iVK_D-RZ0Yn3HVMTaZ0ewnLNXYrPfrtgZ2F7j0BA9I9zAZCQ9itPE39gHbd_lzLf74_8u660X1Mymm5zhoHJdfrw_hFYGQvpb5TrH7yE5AsodR_QV0qaqiw500HKUeQny6dpZ1AtdR8ptKPd2g4f4f_T058IdUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v55Q5TjS3MJAAfONTJ2ThA2E74bNWG_KcSnJ_-xYH5Ei9FlQWadLyASSufe0Zn4mZDj5ZPssYAKT8A32yCJ81RnD_RuNSSwvkRZImzY18QEfHKfu0M_tUbGeAkH3Ocd_V_UbRSP32dTgOOFn8hg8aWytM1FJ6EuD7ipYWGqbHANn7l-LcfwW9L7YXqYN07XMGpg2mob8lGZeJgkscdr-8LaTBan9WC_Zh8v8L_g9BqgoFACHjSpu-PQg5qHC0iOPHvmcYi7i_JAYX1P_mCmuboMPz-dhxVKHMYCSmhyY-vVcIKKF-WF36IBkTHJts7hIWy53yTR5N9d2z9co7UQKag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">استوری شوهرش همزمان با استوری خودش رو میبینید، خداشاهده شوهرشو نبرده عروسی
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/77954" target="_blank">📅 18:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77953">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nh6cvcVLXH7woPpGFddS4Pa2z_JzIHn1kvcfpxvvE56UQQ5CiA2QS4pjMOx4Lv0fDmtQggGTUmSFh1YU1BPtp5iTE5Z40W7PPh9A0OGbnQ2G2GfKd8rMSGXpdOlcvm4wqam6SQfeUns1ni6yQ2u_fqqr0o8RgrbNdA_OSBdxyEhbWL_h3QAOzhySM1S3Ebijk-JyS-VnFa6MSSpgyAaEamcfyq7HUBlAkNT9HCQWJp7WkCgNt3Xt0L26wZYMJ6g6_86Vcte4888_CIXG44eMTy4Z3TopUI5yQtjL2rQYP9N7M8caorXHCUhGj6nNwzJXWZ6THvmzC3umbXOwqd4gEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری یانگ کید
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/77953" target="_blank">📅 18:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77952">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">با ماف بت از جام جهانی پول در بیار چون کلی هدیه هم خود سایت میده
💵</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/77952" target="_blank">📅 18:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77951">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nLVGJGq0sO1ec_oOvOy6nDlD7PzRH6_TSubnAGa9aF-_8LdhZXhhw6X3x9YqrxxTwFoQwRnHhxxXs60GSnrfwLP62TSb3e_DugpwamY6qbtYYaGbpZqIYaqoyU1ZCT4F7YVBlMnLGAI-WohTUi4TNqcEspvN3eNzVlTO06KrpkFjQVtMaesV0Mm3TYsHAY7Iz7py9AwFL61pnML1oUAocUhOsoaPne7sfUfdRdlRpjm4O1IjnGJ9w1SE6pBBpR_VNyWflUgaSWE-Gc24WQmuAERbbv-ujrDbdlGb71SwV_ibo3KlihovOMbi8zPf5Znk0Stzt3B5tWMc-Mv2eLT3PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
چرا سایت بین المللی ماف بت بهترین انتخاب برای پیش بینی جام جهانی
❓
1️⃣
شارژ و برداشت اسان و سریع
2️⃣
پر اپشن ترین سایت فعال در ایران
3️⃣
دارای مجوز رسمی curacao
4️⃣
کارت به کارت همیشه فعال
➖
هدایا بی نظیر ماف بت:
👇
🎁
100% بونوس خوشامدگویی
🎁
برگشت باخت هفتگی
🎁
هر روز 100% فری بت هدیه
🎁
هر روز 20% شارژ اضافی
🎁
گردونه شانس با جوایز بی نظیر
👍
با فعالیت در ماف بت طعم واقعی امکانات در سایت جهانی حس میکنید
👍
🎯
ادرس بدون فیلتر سایت:
✅
https://mafclub.online/fa/?btag=260368
✔️
کانال تلگرام سایت: g25
🅰
🔹
https://t.me/+3Zxs6WU7L_UzY2Fk</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/77951" target="_blank">📅 18:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77950">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mgSHFg_AdwwweEniUEa9bOPi4BuEo_HcsQ9Zdd153yzUIL_TUr14lim_yBGYbwMcg6mVkEokIvH2rsXyXxj86UjhypoyGK1h9WnDRekOyT0VfGQGY5617tQGeXF6qg0NTeAIYYqg_wNAWinbhAh1Z3jB67kUuvdCZNeLVVACsiNJgeT_hV_MvGq-oC10S_ri08s0WgQ96c7SV1SlJfpStUcUuieeuDiCQHFkVS4VHrC8axl189NUJ493p-8czAl5S3KFddarOJ1buyqu7XWZmtEWpBmzQnWxS-deLpmheh14R_ZtIP2_pVS4rvmIUnYOU0FQyL6mPXepROqJ8MEIrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مونیکا بلوچی ۶۱ ساله
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/77950" target="_blank">📅 16:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77949">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EhH6w4xjv_7F-ag8kLKuh95wgaHssLRmwkhTGzcg6RFmnTxvZOqFH7RNaC8LQ1wwNwy3bfQbRetkIa6fco9PvUHcOLLHq-IHtp74iq-VIf29xwAR96zLZImKefQ7kDDqh2ytQLs7SP0Cjqnm1lxRZJwAH721ChrPHq3-gzNqUGwMkr4W3sN-TsASzPFz4FtzYJJCyywRVzW3ZXSRP2sgeUPpPOS-yuEiGn4lVSqd_eYzx8xU5NN7WASyIejatCj7iA0UnvEGHSR1fTXKShuFtsfSzXujhPECIbiHuHFYjPGOwCJxcYDdtzUdZTIuiELkIWspUrYWmCKDhEeTijzFMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
😂
😂
ببخشید دیشب کم خندیده بودم
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/77949" target="_blank">📅 15:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77948">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MOoapnMs8_d_qfd9i4STJBwe4vAqRJp3dcoFUCP8bR3gfMhMqlcZPNY5-GpcHlntuyy1mvt7peK5KzcVz3SO7xSrUi2ZwkAd4qjsEjdfSLcrV7UkJWu9B9nC5nPYvTQY8ld6DpI-tfFXWgvLZU7xYSBkIsPjqoy4bx8eil4-_xZy_DnxgI93gbcvsgMj7sUTIvQ3hCv_j10RlpqvB4uqad--DjFJlTPm07XrkUQ95TZWfOYyIniTvCexNZUet33xYHAKSwG4K0xZGuTCfO0f53T2D0DXf1su8BvO5iFRo56pIEgWuPkfszaRnB1xiZM8XiEdWRlyyDblxWUVE1_O0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمو وصلی؟ نه انگار کانکت نمیشه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/77948" target="_blank">📅 13:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77947">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">در چه حالید دوستان؟
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/77947" target="_blank">📅 13:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77946">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">یعنی جدی ۳ روزه چارتا بانکو نتونستید درست کنید؟ بعد ادعاتون کون خرو پاره میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/77946" target="_blank">📅 12:48 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77945">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YULZ0peeYwAwoUztxKTMDyPRiYDtMNNO3mDn3zE8TszjVjUFZOnO6yqOHt1FKOcn-LxQGbH6N1v9GiqkTeyyK1wRlDFgsv2QaHVtiRnWAt5H26fJavZPy6V1RMQPOpst3a9fAXVmlbsiNErTBj3cr6SFtb-_jhgjY6_BTLps1ubkxA4IKOIC3g8L5_8o593L0HziPaDRQE3yrydJ-eruC5kl5iICbJ2YmYec6W554KFg4gZj2rkH29RU8_MuzqhmFgNM2YRW6VzXZ28c_NreC_pIfgf7pXXGKhNLtlThISSb8UfK78ey3gsioKTGtpOmKTuekOXtFUN8-zgXl1o-BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میدونستید آپارات چنل یوتوب داره؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/77945" target="_blank">📅 12:22 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77944">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">میترسم حرف بزنم رئال منم بخره</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/77944" target="_blank">📅 12:05 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77943">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">میترسم حرف بزنم رئال منم بخره</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/77943" target="_blank">📅 12:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77942">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78832f0cf9.mp4?token=FMgEU-UDfRnYzbUjEWBqdsND66gODvanpCHsDacd3QNAoP4thGRxWYg1gz7mqt7qKwec3jgjcGeLWDgUx4ky0GjeF8pKFTZT2OhQLWGrREnK1KZ7xROHOrDKcrtWYnnScx-IG80VWavU761OKA9Q7McKT_qE31I6P4An70UnE2LIQ6_etK_Dbq4Iarqhr0iWtj57D8t55Lg0t3OtBhXcsS4EiOGsjsiatzBk60UY6nYptsSBNZV72MZpwlKD6aXXaLeUJc4qGuFbFcsSJqgWn8v3SOW34PDcKzofx8UeiMa6a3Fwgty5ol0KuCtOXcndmcPlJCvE8e9h-JwXuVI-sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78832f0cf9.mp4?token=FMgEU-UDfRnYzbUjEWBqdsND66gODvanpCHsDacd3QNAoP4thGRxWYg1gz7mqt7qKwec3jgjcGeLWDgUx4ky0GjeF8pKFTZT2OhQLWGrREnK1KZ7xROHOrDKcrtWYnnScx-IG80VWavU761OKA9Q7McKT_qE31I6P4An70UnE2LIQ6_etK_Dbq4Iarqhr0iWtj57D8t55Lg0t3OtBhXcsS4EiOGsjsiatzBk60UY6nYptsSBNZV72MZpwlKD6aXXaLeUJc4qGuFbFcsSJqgWn8v3SOW34PDcKzofx8UeiMa6a3Fwgty5ol0KuCtOXcndmcPlJCvE8e9h-JwXuVI-sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اول یک قیام خونین رخ میده نتانیاهو و ترامپ وارد جنگ میشن رژیم جمهوری اسلامی رو میارن پای میز مذاکره اورانیوم و موشک و رهبران رو می‌گیرند دو دستگیر و تفرقه بین نظامیان و عرازشه و بعد سقوط با فروریختن رژیم از هویتش اتفاق میفته  - ۸ سال پیش پیش‌بینی های مانوک…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/77942" target="_blank">📅 11:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77941">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">بلایی که جاستین سر ایلیا آورد :  @FuunHipHop | Jenayi</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/77941" target="_blank">📅 10:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77940">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">دیگه زن مانوکو گاییدین هراتفاقی میوفته یه ربطی بهش میدن</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/77940" target="_blank">📅 10:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77939">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">اول یک قیام خونین رخ میده
نتانیاهو و ترامپ وارد جنگ میشن
رژیم جمهوری اسلامی رو میارن پای میز مذاکره
اورانیوم و موشک و رهبران رو می‌گیرند
دو دستگیر و تفرقه بین نظامیان و عرازشه
و بعد سقوط با فروریختن رژیم از هویتش اتفاق میفته
- ۸ سال پیش
پیش‌بینی های مانوک خدابخشیان.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/77939" target="_blank">📅 10:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77938">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">مانوک ۸ سال پیش در رابطه با قهرمانی یک فرد ۴۰ ساله با لباس نارنجی صحبت کرده بود.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/77938" target="_blank">📅 10:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77937">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m3FM18QKZyjUiYoAZgM9g9z1N0hY_kKRO7oT9gYGSMQGOyEDzS2sCvd33FQOzBE2ISq0tj3VcLTOYK9tzJ7KpHkNChE8Jy569g_Wr6msNSqFP6cEfemiHkF4t_h4TBRaU3pLKnDrW27KLZO8dgCTdi39oEQwq3eM-EiQ0ZLJi7X6GaYUYRPxiGlVxU3iClrmW8NqU5S7bUrboFbIOtBBGQDi6E6rse2y3_gPnRfUxY6v640QxdVkoeNz75aTwnijuHspSMw2blutITlQY4ypY4Rq6WLh2bvwMPy_ispiBL7RfM4jumSlfq20GfRPIlJjYUPmJDWlMd1MXoQOkKrNjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلایی که جاستین سر ایلیا آورد :
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/77937" target="_blank">📅 10:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77936">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/77936" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکشن رسمی سایت دربی بت
🌐
DerbyBet.com
💰
امکان شارژ ریالی ، ووچر ، کریپتو در کمترین زمان ممکن
🔥
🆔
@DerbyBet</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/77936" target="_blank">📅 10:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77935">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tVb4SBjAgjsi81YlknamlBZD573b8scevRFv8iqcUNQLuTnv2DG1XSd6_EVDb01saS0s1JYXzmVw6y1o4-TANc6KFfx8G5YlLPOsAebYA2C7eeRbAm-BW1Gpajwnwu77NqSfZ5MsPcwui5e8gwrMZtVrJli5ow46dLH59D50Bu2pkuYb67QgEONgoSQ2wbwBE1uIrmeOWM6Jn3o0yEXFyuPn-voeH-iEh1uvFgwXDt4vXsB2FpVXXs4TSR6VShATHhcOJ2TGKjYxeYyB5V10p5BaQlzjIuDvU0G2XYH0cuufBU3RDUr5yVT4XGrSsPzfjOsWlooFd2zsEzDLqZiyOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دربی‌بت؛ جایی که پیش‌بینی فقط حدس نیست، شروعِ بردهای واقعیه!
✅
با لایسنس بین‌المللی معتبر، وارد زمینی شو که حرفه‌ای‌ها بازی می‌کنن!
✅
آفرهای خفن ثبت‌نام در دربی‌بت؛ فرصت‌هایی که تکرار نمی‌شن:
⬅️
۱۰۰٪ بونوس اولین واریز؛ شروع انفجاری
⬅️
پشتیبانی کامل از همه ارزهای دیجیتال
⬅️
درگاه ریالی و تومنی امن، سریع
⬅️
برداشت‌های آنی و بدون معطلی
⬅️
پشتیبانی حرفه‌ای ۲۴ ساعته
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
✅
دربی‌بت؛ بازی کن، ببر، لذت ببر!r25
🅰
✅
https://DerbyBet.com
📩
@Derbybet</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/77935" target="_blank">📅 10:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77934">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nxr9_VKP08nmazoHq0DDWhkxc-0VdMewoBDJLreeViOAM5RLBLAWIX-tb6ySaVWFZooYcsHZGZOVdNnk0NhLRgHMoryVpci28w1tXYpVfptYm9Iz0ct0V00lwk720Ci8iic20aHY1L-UZJP4323bHG64zk322Sr-rsdTZG6pBIueWrCpga6Dn5pZXw8UWEr5BeyKxPd4Kfo4o2KXRqXkI8Nompn4ov84j8lCuyerTJHfkRIaYLd38dYjHh_8qAHU9ms_O9ZKmCzzdmUs693q4bZLjpjvTrZuFLlMlH_mQbJRtVYHNAnZuUkXC6lGxN8CuaD7Q9xWris43pBarP2pig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بنده خدا یجوری داره آب می‌ره که انگار با سیناب رفت و آمد جدی داره.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/77934" target="_blank">📅 09:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77933">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">توپوریا مادرش گاییده شد و تو پایان راند 4 دیگه گفت نمیتونم ادامه بدم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/77933" target="_blank">📅 08:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77932">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">جاستین بنظرم تا نرسیده فرار کن  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/77932" target="_blank">📅 08:09 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77931">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dBfZV6jq2DLsRnu7Jx0bWc59Z7MUDYIvLzazOYg67GOeu83qh-1v1B1cK-fUue7EsvlEorENpJc27QVmqSObs_ukub-Rbc1QUgj7LKqnNRcPm3d-xHma1aLdWds8zwXu9oSC7QcRzT8xLjdoTwTaLbGG3vPzNl46lGyCcrLZ948G6cQ6iGZB6_heM1G8Yma3RULXcRPtiQPWLzya-BcE1DVtDtKa6mMjvO_b45Dglrkyfqqbo8OoBLdllJ5wP5e7XOVWSf2-1GCSAMUqKatH0pbCmgPEdKU5va0mQ2SKkF0tmOf9SCHx55a0bWK_XXeCuMLYQ7OjurDA3cW2Uxynew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جاستین بنظرم تا نرسیده فرار کن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/77931" target="_blank">📅 08:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77930">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">گوزیدی داداش  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/77930" target="_blank">📅 07:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77929">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPmypVDnpUi2Vyig0VQfOL5T-FJeVCKOAu7Z4TPPqYHR7Yy0IDo9L3q_R77fb6jN5rnD0HY0iRCIOLolWJ94Tx_oYs-hfMjxGcdPDdhj2kcohjtRJzGkG4urU8v1-l0QDkL6qig9wQeibWsyDFPUK88vR60JCfitaAVBpGKVZU1Z8zaVGvtWRx6XT9PzW7LdNqmmGVNmqF_jsBuXgrA5A-70cvokuIc1gjfEHesSn3fdhatA9LpTp3GVnfBXiSGzSObfc1ubgB9bCIdbyLBAkTZlgYZQ8V9nCR7PO8Dc2BU3Xw5zhU76B-OaOZeT25jixynl6UfQXXafKXJRuOk90Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوزیدی داداش
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/77929" target="_blank">📅 07:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77926">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mvI3VJkC2v5zzbwnLoQMGpz-IlrUiBgFAm2BOKvDKGZEuarB2yOINQ_VvHyIi-PWR-b41ez7VXBJre5po2yv8Slbd2ghbCzbzPl-Q0MjwbKUdU3LEVYmjvtAXWElNVKnVHl3koEeMDe5MxX1jZ3HDXhS7aFl2Ihz4tu77FyfSOgFw3tJDpCYbr60gGn8F_zvHSf6HqHjrZ4ZEx0qfBHzc3A6bRkMY6Fr9I6HAbRYLzdAB3jV2ChagyCW7wNFNZS9FzuM7whKITifch0LHH00M1mNsdXmx79bfBJfgCcPJ9kW23H0OYQfQ-lkyud2netGmcE1SlDsqoHW8W8u0OEl1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/77926" target="_blank">📅 03:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77925">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">از اینور هم خبرگزاری سوپر معتبر مهر هم شرایط ۱۴ گانه توافق رو از قول خودش منتشر کرد که اونا برا پوشش دادن زیادی خنده دارن خودتون تصور کنید بخندید.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/77925" target="_blank">📅 02:22 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77924">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">با باز شدن تنگه پس از امضای معامله در روز جمعه</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/77924" target="_blank">📅 02:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77923">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dXj_3eXY1AAEv6zUIlIETW0hTQQeG36G9QtWbAUDklxpJCYfMmcsGOmaLT1qvB226XCaATO0gGEStgbmjZop7_5Fk3UdkCHe21p3S-VmuPFzcmMKVbZF0huvw9QJafY09CzsIzmG6tOIQ9rJv3FPsV6Yjxb-Pj68Fhm9V7X7z15nbU_YRujAZBzB8OeontHocbbblfCNOmQju0qoUtlzzoXqW88ZsSNRuZ7wvTeHWdQFjE8ObbWd2ZeM2VucWK6wfGpfJwOr3bUBKP-CdCotQJz1sKEI6i3RNX-RMugJK1MTbG1N9unWGnAYqejyx4SeNlwHqlKKSDcEdIpShMjC2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این معامله بزرگ، صلح و امنیت را به کل منطقه خواهد آورد.
بسیاری از رؤسای جمهور تلاش کرده‌اند با ایران صلح کنند و همه قبل از من شکست خورده‌اند. (اوباما به کص ننت خندید)
رهبران منطقه برای اولین بار رئیس‌جمهوری را یافته‌اند که می‌تواند به آن‌ها در دستیابی به صلح واقعی کمک کند. (هنوزم داره می‌خنده خوب به صداش دقت کن)
با باز شدن تنگه پس از امضای معامله در روز جمعه، به منظور پاک‌سازی مین‌ها، نفت دوباره در هر دو انتها برای منطقه و جهان جریان خواهد یافت!
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/77923" target="_blank">📅 02:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77922">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">فارس: ترامپ در ازای حمله نکردن ایران به اسرائیل، پیشنهاد خروج کامل اسرائیل از لبنان و رفع فوری محاصره دریایی (به جای رفع تدریجی آن) را به ایران داد.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/77922" target="_blank">📅 01:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77921">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ویویویویوی خبرگزاری Ynet به نقل از منابع آگاه:  ترامپ به ایران پیشنهاد لغو فوری محاصره دریایی در ازای عدم حمله به اسرائیل را داده است.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/77921" target="_blank">📅 01:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77920">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a1eec5a77.mp4?token=m-lFY1K8GJV_9Zc3tc4OqsXCdVnhT332yfepbnD8JdpySNZakjFRPneIvIoPL0xdJHgZyZVMC82lSctwaTkdzOFunkEY93nI8nHdsADhgJW4klO64hdfLp87q4jMnDDxFnzrO8jwQVdjbgmlhZfYuTDQe01UWSN5Vc551OiHEVu5zQkNLQxYgvR11tlDcFX_5qM8ZsH0nidU0Mm9G_y0gWJwDq5H3_PTIEmOLY2eo4WQV_f5OHNPieZBKRTP6haK8K9hmDZWKDU3VoqQk5ucOhRUqz6_vQa6yzpHqwtFshSSnmhInugyQlzhPZ-ZM9ivtw4MJVN7CyI-Zfm4nb3juQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a1eec5a77.mp4?token=m-lFY1K8GJV_9Zc3tc4OqsXCdVnhT332yfepbnD8JdpySNZakjFRPneIvIoPL0xdJHgZyZVMC82lSctwaTkdzOFunkEY93nI8nHdsADhgJW4klO64hdfLp87q4jMnDDxFnzrO8jwQVdjbgmlhZfYuTDQe01UWSN5Vc551OiHEVu5zQkNLQxYgvR11tlDcFX_5qM8ZsH0nidU0Mm9G_y0gWJwDq5H3_PTIEmOLY2eo4WQV_f5OHNPieZBKRTP6haK8K9hmDZWKDU3VoqQk5ucOhRUqz6_vQa6yzpHqwtFshSSnmhInugyQlzhPZ-ZM9ivtw4MJVN7CyI-Zfm4nb3juQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من هیچگاه علاقه‌ای به تغییر رژیم در ایران نداشته‌ام.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/77920" target="_blank">📅 01:05 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77919">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">شهباز شریف: به توافق صلح دست یافتیم. جمعه امضاش می‌کنیم. دو طرف اعلام کرده‌اند که عملیات نظامی در تمام جبهه‌ها، از جمله در لبنان، به طور فوری و دائمی متوقف خواهد شد. پس از مذاکرات فشرده، خوشحالیم اعلام کنیم که به توافق صلح بین ایالات متحده آمریکا و جمهوری…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/77919" target="_blank">📅 01:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77918">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">این زیر یکم فوش بدید خودتونو خالی کنید
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/77918" target="_blank">📅 00:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77917">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJ8JJFOduGwsnpMJuZBuI8q1QREnPdF-6C7vD6EAH6--eW8Sz4ZL9hf3YZc3m2t1KJTLJ2MnPTxoFB7xsg14jtvQPC8ppqtBSQKMB2GTiy_mA0cGjUbL0e9r98nm3oCWMDHSJGQbGN67iIx-9onge7KRrspkaDnmJfAvy-AHDETWOpMRpTv5wI3Si13F3cPzUrFq9c40DJyqXRHPOND6QqQmbd4V9n5AM_xKCTeHqYR6eRVeTvi7gWw2GuZbsNNBL8EvkwgvkXOU_1Yw14WgaVHmv4EruoChqEdXfxetIc4_u5H1sVJaLJhPUjssyQhDspPkRRXAvn1PrjRwD8Iy1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهباز شریف: متن توافق به دست اومده و ما انتظار داریم تفاهم نامه تا ۲۴ ساعت آینده امضا شه و بعد از اون هم یه مذاکرات در سطح فنی برا هفته‌ی آینده داشته باشیم و ممنون از همه‌ی طرف‌ها که به پاکستان فرصت میانجیگری دادن و به امید صلح پایدار.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/77917" target="_blank">📅 00:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77916">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ژاپن گل مساوی رو زددد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/77916" target="_blank">📅 00:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77915">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ترامپ چند ساعت پیش به وال استریت ژورنال:  قصد دارم به زودی بیانیه‌ای صادر کند که تأیید یک توافق با ایران است، اگرچه ایران هنوز تأیید نکرده که با شرایط موافقت خواهد کرد. این توافق به صورت الکترونیکی توسط خودم یا جِی‌دی ونس امضا خواهد شد.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/77915" target="_blank">📅 00:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77914">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">هنوز چیزی امضا نشده کیرم تو چنل هایی که خبر فیک میذارن
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/77914" target="_blank">📅 00:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77913">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">گللل هلند زد
فن دایک
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/77913" target="_blank">📅 00:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77912">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ترامپ چند ساعت پیش به وال استریت ژورنال:
قصد دارم به زودی بیانیه‌ای صادر کند که تأیید یک توافق با ایران است،
اگرچه ایران هنوز تأیید نکرده که با شرایط موافقت خواهد کرد.
این توافق به صورت الکترونیکی توسط خودم یا جِی‌دی ونس امضا خواهد شد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/77912" target="_blank">📅 00:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77911">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">توییت جدید وزیر کشور پاکستان:
الله اکبر
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/77911" target="_blank">📅 00:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77910">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ghRWsiuMtXILnQeTeNjW2CJxg9NVEXU1OVHR4Z12CP68F6IhLH11R8PZXHKPEmpsxoAilqMoFaHDhpDIZ9_ZG9_BXEi-A-4pZlJVHwu2U98vZUREMeDc8HuOByd6y4XwwwlQ3OyFUjAVuXZTDvJENrS-ktcJJKpIHcu7s6U97SG8uJDyEL0T_qS-VOlkokyfLnaeBVUrexYVjHMJi48i92tPW-ToFZOip6qfN_6D0J2IUKL-lKZLJ9RQvfIs_LgwRXy62SLhUbyGZZLZP0BG7VuWGTrMV3b_W7EIGur36gGEdpqvicVqHfMwsqbLVG4A8CFORScl8yGCvj1Mrskmcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از یه جا به بعد جدی جدی داره تمام تلاشش رو می‌کنه شت پست تولید کنه:
ویکتوریا کواتس از بنیاد هریتیج کاملاً فوق‌العاده است! ممنون ویکتوریا. ایران هرگز سلاح هسته‌ای نخواهد داشت و تنگه هرمز به زودی برای کسب‌وکار باز خواهد شد!!!
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/77910" target="_blank">📅 00:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77909">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0800033b0.mp4?token=vRqiGLSRpjYL8GROUmcSdqZWYSy6S400fN2fkCNMKwSH3GgdJXF4gHc0eS5YfNEYMKvUZx7gqXllO4Z6VJeu36GGooWm8Cu5qcYf5YfZdXUCT7u5VlzXJtzB48zE_jHWt0-M6Levg75rDDL_r8I6Yx2MWbmLK3RpiypDzzlDABozBmgsVWu0d983gQgv0bg6J9yBaUbwP6YNFMrqKm5Xw0HbDdgE-a3yGHBw1a739vqVrYICgMDQewy7AKXaAnqJg70z1zTdRo5lY4ITB3yjptzfeHa8JaUZ5A1-Rrgp8mY1A0XEc8Y7ohhHhCfZtRokGYJwaKfUs195_OlNGzCz-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0800033b0.mp4?token=vRqiGLSRpjYL8GROUmcSdqZWYSy6S400fN2fkCNMKwSH3GgdJXF4gHc0eS5YfNEYMKvUZx7gqXllO4Z6VJeu36GGooWm8Cu5qcYf5YfZdXUCT7u5VlzXJtzB48zE_jHWt0-M6Levg75rDDL_r8I6Yx2MWbmLK3RpiypDzzlDABozBmgsVWu0d983gQgv0bg6J9yBaUbwP6YNFMrqKm5Xw0HbDdgE-a3yGHBw1a739vqVrYICgMDQewy7AKXaAnqJg70z1zTdRo5lY4ITB3yjptzfeHa8JaUZ5A1-Rrgp8mY1A0XEc8Y7ohhHhCfZtRokGYJwaKfUs195_OlNGzCz-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش بسیار تند باقرشاه به بعضی کارشکنی‌های بعضی افراد در مسیر مثبت و سازنده‌ی مذاکرات.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/77909" target="_blank">📅 23:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77908">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">آدم شخصیت و استایل مربی ژاپن رو میبینه عشق میکنه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/77908" target="_blank">📅 23:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77906">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">کی قراره چنلای فوتبالی تلگرام فارسی از گذاشتن عکس ممه های طرفدارا تیما با کپشن "کاش فلان تیم قهرمان شه" یا "من دیگه طرفدار فلان تیمم" دست بکشن
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/77906" target="_blank">📅 23:30 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77905">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ویویویویوی و عجب دنیایی شده پسر کانال ۱۲ اسرائیل: یک مقام ایرانی اعلام کرد که دونالد ترامپ به ایران پیشنهاد پول در ازای سکوت درباره حمله به بیروت داده است. ایران آن را رد کرده و گفت ما خیلی زود پاسخ خواهیم داد.  مقامات ایرانی همچنین تأکید کردند که «ما برعکس…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/77905" target="_blank">📅 23:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77904">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">مگه قرار نبود امروز توافق امضا کنن؟
چیشد پس؟
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/77904" target="_blank">📅 23:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77903">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EgCqduvRrA-_z2lITzCuzdtml3rc4O1k3BpP7iL4xaUE40Tf8UKFOdK-762yDjiCYCW0C9xkwRiRK64w_nv2gzoyzCYloeJ3Fsv8Z_9wWZWXbvIi7Bxl9tHUqrrvwvTT1phQeC03bJUvU0dfCljlGTFzyckWeizEMblHu1DVkEENH20GUaXqIT0Uf40DFUoVCYKhoP8VO5GswJDPONOpxz7hKF2xNu432KBkw8g1kzMlAAPHeY_smiqVwfAkAFzB2AzGCT3sc7rSK3zIj0kYoGZU8flD4XiQrcErViJcD3jPlVqcj49jFKQ_YqiPTVjrSzHK620NGJ00yyWc9sSixg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خارکسه تابلو
😂
@FunHipHop | Menot</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/77903" target="_blank">📅 23:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77902">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZdxFlBjExDb9t_JEpXh_3sAlvvS55CA8RnaP0W7klXnPjBoT1PMHTcdPBQWX2vf6CGsr0KokcdRByXi3Jlebm-vhUaHWMjpnz2iC97VJWByD-x0hYVsVluq4jYHt7YmkZJ5qeq25kYe55zHt8QZNL9ALtLIv1VSpQTi4uO_gI12I6v6MtPxBWKF4E9U3SwYZ8BpkOrFkniSwDlc54H08WZ5R_0wijBtdnBWoYPYno_-L0jBB7Or2vlC7c-QHMdtcep3WxXffvEmAo5f-mSV93n2zZf3fyp4F1Qg-yHr0Jbf7AmCERvHLMFHxH1Qp8vdyDa2oGKC7XAODvMtSUlQwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خارکسه تابلو
😂
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/77902" target="_blank">📅 23:12 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77901">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">سخنگوی کمیسیون امنیت ملی مجلس در گفتگویی عمیق و تخصصی با شبکه خبر:
هدف اصلی این نظام نابودی رژیم صهیونیستی تا زودتر از 15 سال آینده است.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/77901" target="_blank">📅 22:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77900">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MswszzjoR69ay5vlTh7GE8kTAM3YdFHY5I2FgYVLO5jJH_WOVoovWT_zS1Q_Mkwi_jjU7vFLfb2TJ4FBibLPROaNJk3tumS86C-CKzBjEcz7_4R3HoubcYp9jWIlMrGw8rW0ECH0_mLNdUKlFweaAchtQh4LUZJEjGHdmABF2VjXVO9th46R5fdJotAbZEXho0uhCRN_eFLvVlftRufRxRnccHib1B9CrfFgwn2VE9QJFfogyFWAq8ulUBZiE6ZCyACJlanQH-jCoEnynlLLr_hxXyYMTcYY6CpvdIQp7OZYF04yKSMx4iZqk8l24lEJVgfu76sow0jPD2PotpF4nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باقرشاه عصبانیه:
آنها هرگز نمی‌توانند هیچ بخشی از ارکان مقاومت را تک و تنها گیر بیاورند؛
مجاهدت‌های رزمندگان غیور لبنان و
دیپلماسی مقتدرانه جمهوری اسلامی ایران، حاکمیت و تمامیت ارضی لبنان عزیز را تضمین می‌کند
و بساط دیوانه‌بازی و جنگ‌افروزی رژیم اسرائیل را بر هم خواهد زد،
بچرخ تا بچرخیم.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/77900" target="_blank">📅 22:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77899">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">هفتمی هم زدن  فشار بخور برزیل فن  @FuunHipHop | Farid</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/77899" target="_blank">📅 22:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77898">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">همچین تیمای تخمیی اومدن جام جهانی بعد ژنرال معتقده که تورنمت سخت تر شده
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/77898" target="_blank">📅 22:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77897">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">هفتمی هم زدن
فشار بخور برزیل فن
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/77897" target="_blank">📅 22:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77896">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">گللل پنجم آلمان  کاراسائو پاره شد   @FuunHipHop | Farid</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/77896" target="_blank">📅 22:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77895">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fAgjlRxERhv3fPACPk2EXbbP-pCRqgnTUawjBoanHjosR9Uh6vzZHNq746dVGDlv4RA8SSfn_roVZAD6_9MeAHbaaC4eNkLsD7zwuAjQNuaM1frzopplk85cMrtBZtwfFMjIBczpVzwRgKyry-xyWcfJhSM82_ONunHdmp0TA5XiTo2yal_PiadwfO2hwvStnFuzAAxTNoP-a4Tv6f8zqqiwyrpV7j6mMFFpfS6ZK1sgE_z4vDnSOqKiX4oaFS8SBhfHw3e6RNrqYETKJ1p440TIGiSSXUyeNbKa-H3DVc561lbdVT3CYNbEA8-cMNkpjctAQ7eK_xT4tnYMsb9htQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تقریبا شامپو شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/77895" target="_blank">📅 22:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77894">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">گللل پنجم آلمان
کاراسائو پاره شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/77894" target="_blank">📅 22:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77893">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">باب اسفنجی امروز زودتر فست فودی رو بست، فک کنم یه خبراییه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/77893" target="_blank">📅 21:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77892">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">این ترامپ کونکش واقعا ریگان پلاسه</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/77892" target="_blank">📅 21:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77891">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ویویویویوی  کانال ۱۲ اسرائیل: اسرائیل ارزیابی می‌کند که ترامپ به زودی امتیازی به ایران خواهد داد تا در ازای آن ایران به حمله امروز اسرائیل به بیروت پاسخ ندهد. جزئیات نامشخص است، اما مذاکرات پشت‌پرده در جریان است.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/77891" target="_blank">📅 21:43 · 24 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
