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
<img src="https://cdn4.telesco.pe/file/TsHtSeINuSNnBx8tegBWfWK5_PwlLgkeap7aLRPX0k8-f8LTVDZuiCFHffd_kK2reAGRcsRHyU-FxJ9hFyBltcin3p6gwmU3BiKRXtZ8mPFjvslGkk6T8xmDU-grweQNlHc1bJBimdntzBzMkoARG0qOCe6coBuktnPGhEQ0eyV7bR0_nAsaYlecMOCvf0tqJ0m17h4kQ31aj8vn_Zp_LJiQfxxXOWiRTmhcwhE2yIHgRpzYX9_peQ6lvJzUPz8JHY_3f06D73_OS-S3fUVdJVA_okdz6xebKEugyi-AXbl-T4c-Jv8bbdRFktpuNzPTzwodfGE6KqE3XcY1zQ2sww.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 942K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 07:27:51</div>
<hr>

<div class="tg-post" id="msg-134964">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVMpGnvJwxiTbecz2_jEFBsgzR3V6W9Q2q-d8SEwUEb6kCc5C9f44p6e8Iej4aE_VPDwQXSJq8Txq_jYc5IO8aySyvms7wbG3Wt_PqZqyqjYmbvteoFUl0BCC0m77mjbOXIDUVx4Xk4n486syWFI6jUsYckMLryQ6XIo4LkeMLD4XE4X6jR1r1PSTG1hv3FxvMFv9uHjQMBjJ2s0H0p69VIgaNM5_Ji2A1dRkAb5kvpakckZwwnUXAgbCyDl453-uDNPEe0ALfmP3o_UvWPwKPTvjcQCuGFdcrLrKlpAnrqpwJ2cRp0H2Bdyiww65clCQ09Iek35-1RSKZ5qh-XgtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پهباد آمریکایی روی آسمان چابهار
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/134964" target="_blank">📅 05:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134963">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
ترامپ در پایان سخنرانیش: ما قویترین ارتش جهان رو داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/134963" target="_blank">📅 04:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134962">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
انفجار در چابهار
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/134962" target="_blank">📅 04:55 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134961">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3c26581b61.mp4?token=FFuOKrhPhRvuBOHRurjPegCoeNAdo1TOISyiD5nbu_TTdcu9LFnbow91HU_H-3_JYC6aN8tDZMgohXKvnF7o2eT-Fw2LP8EASPWpHyZGr3jUUoTEoy3fBb7_JaX3p8NPuoR-pLTFaNDRmse7R_n0RL0XvF_joG-pZwf1zTelTzUYKgW7M-6Mda7k2NftECRlNkp9MhnsL6ihcBb3Nlogi8bqXIMBQLczjogGSZjtbsxA2do0bX9Nd6_y_444ibD13vnTnSbHatedmhx3X4qniDYLO1RdXHA3w4lgFh7NGUDoPUpdOzAnhLBaWAzSOzT37igMpVbT3fX-3TQ1mx4OeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3c26581b61.mp4?token=FFuOKrhPhRvuBOHRurjPegCoeNAdo1TOISyiD5nbu_TTdcu9LFnbow91HU_H-3_JYC6aN8tDZMgohXKvnF7o2eT-Fw2LP8EASPWpHyZGr3jUUoTEoy3fBb7_JaX3p8NPuoR-pLTFaNDRmse7R_n0RL0XvF_joG-pZwf1zTelTzUYKgW7M-6Mda7k2NftECRlNkp9MhnsL6ihcBb3Nlogi8bqXIMBQLczjogGSZjtbsxA2do0bX9Nd6_y_444ibD13vnTnSbHatedmhx3X4qniDYLO1RdXHA3w4lgFh7NGUDoPUpdOzAnhLBaWAzSOzT37igMpVbT3fX-3TQ1mx4OeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس‌جمهور آمریکا، دونالد ترامپ
: ما در ونزوئلا پیروز شدیم، کشوری که اکنون با ما همکاری می‌کند تا میلیون‌ها بشکه نفت تولید کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/134961" target="_blank">📅 04:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134960">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f4ce05c84.mp4?token=lyc9L5YSwIrVdHyCvE-b5Win-xjdZEMgSwHGrlI4fQzOz8Sb_wGTYImDHkD31SsfB9LNmE3x8dwCUHHTWobtKTQ0-INM6BlTQsmWWIQ2XH_TG9CzXL4igSNIqV35CLISYBGa_J38H-q4bSrx7twWtOq3W6NNFy1pKVYwqHypCG5okWmOzz2w9teQ_tyjW7guYCSos6yzaEbspXloF36v0nkaGbOpMa4hEJmfcy3ho7JTp_uz9N6wIzv4MzE9lmnXdWJx8lPE2NIaU9TJaL8jCw9jbhsFUQvTbZsMsEqXzQhiw2y6RER6VWvrt-3hUNWXz2xus0eR5gKQIOpl4dZeIzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f4ce05c84.mp4?token=lyc9L5YSwIrVdHyCvE-b5Win-xjdZEMgSwHGrlI4fQzOz8Sb_wGTYImDHkD31SsfB9LNmE3x8dwCUHHTWobtKTQ0-INM6BlTQsmWWIQ2XH_TG9CzXL4igSNIqV35CLISYBGa_J38H-q4bSrx7twWtOq3W6NNFy1pKVYwqHypCG5okWmOzz2w9teQ_tyjW7guYCSos6yzaEbspXloF36v0nkaGbOpMa4hEJmfcy3ho7JTp_uz9N6wIzv4MzE9lmnXdWJx8lPE2NIaU9TJaL8jCw9jbhsFUQvTbZsMsEqXzQhiw2y6RER6VWvrt-3hUNWXz2xus0eR5gKQIOpl4dZeIzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
: چین به اطلاعات ۲۲۰ میلیون پرونده رأی‌دهندگان آمریکایی دست پیدا کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/alonews/134960" target="_blank">📅 04:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134959">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
ترامپ:
اگه من تو انتخابات رای نیارم یعنی تقلبی در سیستم شکل گرفته
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/134959" target="_blank">📅 04:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134958">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b37596bf02.mp4?token=NX1H1lP3phMxIbJP6TolqILOSiTLqZBUEEtzna9v7RX3Hjf9EkuU9ksr6zpY9P9D4tAAzKklZ-JbOTd20n0vjrp8nbEl6kUSqUO2sp6T11fia7IjoePwJY_aQJEtPyE03euDcovqut7SyILcAv5lB5Xa3kj78N9EYSfmyTYKoe1589brqk9K79ELHVBIl4rVkh7mzbrvocH3YB-GjYzZd3gveNGyxwFNDJEFxgWxn5LGDCd1lzlvM0zqo81DCXIaCWJKeX0c1Hmlb4T2La4zliHGdK20x0XXy4WPs9zzbVgWK4CFc7JLh7aJ139ZBYVk-hAjA5po1C29iLJA_9XOxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b37596bf02.mp4?token=NX1H1lP3phMxIbJP6TolqILOSiTLqZBUEEtzna9v7RX3Hjf9EkuU9ksr6zpY9P9D4tAAzKklZ-JbOTd20n0vjrp8nbEl6kUSqUO2sp6T11fia7IjoePwJY_aQJEtPyE03euDcovqut7SyILcAv5lB5Xa3kj78N9EYSfmyTYKoe1589brqk9K79ELHVBIl4rVkh7mzbrvocH3YB-GjYzZd3gveNGyxwFNDJEFxgWxn5LGDCd1lzlvM0zqo81DCXIaCWJKeX0c1Hmlb4T2La4zliHGdK20x0XXy4WPs9zzbVgWK4CFc7JLh7aJ139ZBYVk-hAjA5po1C29iLJA_9XOxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ
: اعلام می‌کنم که از همین لحظه، اسناد اطلاعاتی مهمی که آسیب‌پذیری‌های تکان‌دهنده‌ای در زیرساخت‌های انتخاباتی آمریکا را نشان می‌دهند، از حالت محرمانه خارج شده و منتشر خواهند شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/134958" target="_blank">📅 04:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134957">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38775e5358.mp4?token=X0cdoucBzsYLKSrlKRrXjvfb9Kbvb7ue_etI1GioTTQLLAUvbgmL7wV5La7LK59CGTsLPnqYrY3IiRlsBi85-1xIykOwedXM64TRlUN-zbhetLTGvjHau9O9QpNt-W_73qq64Md6ilZu_Nw-j73zrMmeZtxmpLiNf5XWzYHbo3HZhUr6Lzt7kr4SiLMO_KVOIuk60T8Ztz5HVLGfmF0GtlXTubIAjzL8Mv_ZlmHmXwaNNZGqEi_8uPv5XAUrBpTVCKLgCN732PJwgNkIZp2ECu-UiqfxNEfJ8FAmSyNZS8-wmPKC07Ldn3bGuGMFvsQmcf9qwHN-6TDHIJdNuHZgAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38775e5358.mp4?token=X0cdoucBzsYLKSrlKRrXjvfb9Kbvb7ue_etI1GioTTQLLAUvbgmL7wV5La7LK59CGTsLPnqYrY3IiRlsBi85-1xIykOwedXM64TRlUN-zbhetLTGvjHau9O9QpNt-W_73qq64Md6ilZu_Nw-j73zrMmeZtxmpLiNf5XWzYHbo3HZhUr6Lzt7kr4SiLMO_KVOIuk60T8Ztz5HVLGfmF0GtlXTubIAjzL8Mv_ZlmHmXwaNNZGqEi_8uPv5XAUrBpTVCKLgCN732PJwgNkIZp2ECu-UiqfxNEfJ8FAmSyNZS8-wmPKC07Ldn3bGuGMFvsQmcf9qwHN-6TDHIJdNuHZgAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ما در ایران پیروزی بزرگی به دست می‌آوریم و شما خیلی زود ثمره این تلاش را خواهید دید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/134957" target="_blank">📅 04:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134956">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/857d55ae03.mp4?token=SEo3o0gyZxVTd9OFB3FBMIa4aUpUKc9g8dcUqWNPMJzbdb5oo4UGPsLParjG2hBwIwcKvS16dGy3_AbqzzUjN9KzRa2SYjVuwaiYMKkyJewiwdsuk9lgMzHkvx62cLZjZnsxygd456A1OF0sL0-OLTSCLfc8cImAp5OiFzXpdaok1HdIV8LV37pcYY8jTNcV8QjlpUW8ArslKwsKu1v2abkcujy6CHohVmTe7mDC52w-E2iAR7wfUPRdX_CZuwh7F8Q1o282tqzpXVPgSqitqTNHCsLpjKeu_nf1xHyRWwzMNWxhcVlBrTcuEv7f5FRbkDijQJJ-rPd8eipS51CU3Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/857d55ae03.mp4?token=SEo3o0gyZxVTd9OFB3FBMIa4aUpUKc9g8dcUqWNPMJzbdb5oo4UGPsLParjG2hBwIwcKvS16dGy3_AbqzzUjN9KzRa2SYjVuwaiYMKkyJewiwdsuk9lgMzHkvx62cLZjZnsxygd456A1OF0sL0-OLTSCLfc8cImAp5OiFzXpdaok1HdIV8LV37pcYY8jTNcV8QjlpUW8ArslKwsKu1v2abkcujy6CHohVmTe7mDC52w-E2iAR7wfUPRdX_CZuwh7F8Q1o282tqzpXVPgSqitqTNHCsLpjKeu_nf1xHyRWwzMNWxhcVlBrTcuEv7f5FRbkDijQJJ-rPd8eipS51CU3Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
: قیمت داروها بین 70 تا 80 تا 90 درصد کاهش خواهد یافت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/134956" target="_blank">📅 04:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134955">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
ترامپ :قبلاً همه دنیا به آمریکا می‌خندیدن، اما دیگه اون دوران تموم شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/134955" target="_blank">📅 04:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134954">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
گویا دالامان که نزدیک آنتالیا هست پرواز معراج داره، این پرواز رو یه آژانس هواپیمایی ایرانی چارتر می کنه هر هفته که مسافرش رو از آنتالیا برگردونه ربطی به مذاکره و ... نداره
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/134954" target="_blank">📅 04:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134953">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
برگردید عراقچی نیست توش</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/134953" target="_blank">📅 04:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134952">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
هواپیمای عراقچی رو آسمون ترکیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/134952" target="_blank">📅 04:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134951">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
انفجار ها در پایگاه آمریکایی العدیده قطر.
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/134951" target="_blank">📅 04:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134950">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wCaxd8_6wPqDzPLg2QSU2kaSnpoUMsEV61FEQIBvLhrY1HkX03wwJYwzRiCXR4JhVSdzNCiOTBfmk7Z991dzemi6ulnUdIVYWcIcQOei5uIRH9q25a-ZM4lss7ObXFOMAHhSfA_SbGDfuPOBq9BK8rSookRFHmVamb6_26DCutS30mo8WBzvdAlAS7bHgQj1eVq8S2yM7D1_auWzo4phitseSMF0DmOfwsCzsBMD_z4bfAiCio4Sv6JOQFdGQeRzzOo6TEf0ftXWsH4UTSZ8nAl0duB5TsGbX7oTErZlKCKujQIeRrJKfZe3YMF0Mqb2I_UHkHYO7EaH0zGiN21rZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فعالیت شدید پدافند در بحرین هم اکنون
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/134950" target="_blank">📅 04:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134949">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L9NM8hd9cbL-dFjZNO3p2Kpg5TB9Bx9OdvMwUyikaStTlpfG4Wr9I--mwsvx_lb94vmNUUNM8-h-e7XZFpQTW4ZRqKHv-8RDedrGD--Edryk-p4fSFWUnCai0pjmhmOcmmrt1QeL-T4wug74lOvJXjU4t5xdSQcIvMz4oDxsNRG0ec0TQmHzS0liHpHdhlD4qtQTRh1pgl2fT8zV6MdQiDsSZwx02l6eyiPaOd-xkuB4fWhPqhke2frBPbFgUVdCW8WVof2TlnpZgsOTUmfmy6lZpaQZm5Ru4wu8ihUZ2SWnYitKRmXYNW4kppjbNODr_2mZqmnmLZT-xBZC4qVwIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آسمان قطر بسته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/134949" target="_blank">📅 04:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134948">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
حمله موشکی به العدید قطر
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/134948" target="_blank">📅 04:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134947">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
ویدیو تخریب پل ملک فهد که درحال پخشه متعلق به یک پل در روسیه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/134947" target="_blank">📅 04:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134945">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d99c3c0b64.mp4?token=cuqzTYMdRb8cZ8YFM9Cfn_xS3xyNENRJrhTvEzrlm3UHdog3XuH9voWE2EoEPmYHuUMPGaMf97Exg--NzyEi_9jIA-9nxYdH5f2TJjEzQaj-qYK4DmfJJ1iZFfhNYO1S_0HnM7c9neiUi5RYygFIn850cgBX4DnAp0YPLwc1iQ2WvQU3L004JCtL6q2f6zLtlRc3mtROPNLzfJ-apea407HVm4PUa_Z-5FP-quF4ExVo3FQXpyZQW41g6ngGb2CrWiJEY6AGddRU_gH9Wp6ynobWvXcfL0EjUQVZZ__hzkGTdXE5dysdHgEiXiCQIcAt1QikvKPoZ52JgDVsEy6Y9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d99c3c0b64.mp4?token=cuqzTYMdRb8cZ8YFM9Cfn_xS3xyNENRJrhTvEzrlm3UHdog3XuH9voWE2EoEPmYHuUMPGaMf97Exg--NzyEi_9jIA-9nxYdH5f2TJjEzQaj-qYK4DmfJJ1iZFfhNYO1S_0HnM7c9neiUi5RYygFIn850cgBX4DnAp0YPLwc1iQ2WvQU3L004JCtL6q2f6zLtlRc3mtROPNLzfJ-apea407HVm4PUa_Z-5FP-quF4ExVo3FQXpyZQW41g6ngGb2CrWiJEY6AGddRU_gH9Wp6ynobWvXcfL0EjUQVZZ__hzkGTdXE5dysdHgEiXiCQIcAt1QikvKPoZ52JgDVsEy6Y9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
موشک های ایرانی در آسمان قطر
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/134945" target="_blank">📅 04:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134944">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
وزارت کشور قطر:
سطح تهدیدات امنیتی بالاست و از همه شهروندان تقاضا می‌شود که در خانه‌ها و مکان‌های امن بمانند
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/134944" target="_blank">📅 04:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134943">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
انفجار در قطر
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/134943" target="_blank">📅 04:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134942">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
برخی منابع: اعزام گسترده نیروهای امنیتی عربستان به مسیر پل ارتباطی عربستان و بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/134942" target="_blank">📅 03:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134940">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
چندین انفجار جدید در بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/134940" target="_blank">📅 03:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134939">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18319f2842.mp4?token=VaqvcqP5iupYPzKX1wexRiF-hbE6sq68YFtGPDje0FKsXCTarIKrO7Z4AplVx_yTTaeIn-qSOqT-5rn2OdywSOfZn90qcAoHy4AN6XTh18RZTmPooElCRzPfPw325-EJMqMDK26_3_OIIN3kCrKggoQt-TcXK2Oopi04eqh-jESjH3TlDg6nyD4u5z_qkuO6JJNWE3lr1DHT8jbd1lR9fxsA512BI53pwPZyeYe05J9Cc8p66MkkdVF66vk18vM2Z3xQd9B-syFw-C7ZVeU-QQlmkzKYDEwJ3XhdcVnatylEqRkCB9goA2H1Mzqad2SzRKzZqL9Qxw3SgukjtkZjWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18319f2842.mp4?token=VaqvcqP5iupYPzKX1wexRiF-hbE6sq68YFtGPDje0FKsXCTarIKrO7Z4AplVx_yTTaeIn-qSOqT-5rn2OdywSOfZn90qcAoHy4AN6XTh18RZTmPooElCRzPfPw325-EJMqMDK26_3_OIIN3kCrKggoQt-TcXK2Oopi04eqh-jESjH3TlDg6nyD4u5z_qkuO6JJNWE3lr1DHT8jbd1lR9fxsA512BI53pwPZyeYe05J9Cc8p66MkkdVF66vk18vM2Z3xQd9B-syFw-C7ZVeU-QQlmkzKYDEwJ3XhdcVnatylEqRkCB9goA2H1Mzqad2SzRKzZqL9Qxw3SgukjtkZjWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارش خبرنگار تسنیم از پل بندرعباس به لار
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/134939" target="_blank">📅 03:49 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134938">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JPdYNCY3LiW_44khmyUbjXfSGGiEOVCq0S_sDZA30mTxL5ShjlwxxK6aM8kLvmlIpsDJLBhjCC7aCx0TMfx6L94C3wovWRCJJ3mTNxgtxD_CFyidIWOUbhe-XQEqvQoF-ChBO2x5zTAVZ_4oyJcqomsb-7JdJz85ZIn7GL1ToKBW1F6h73u8qlkbq5ZOtlaQWyOcRuZjoHWQ8fZmuCZU_PNi5qP1CxlqBTlAdQpt2qq3ixXBottF-pUMpgEX3KnW4BkuCiJQL7LfEYT1-84ZBCyPcm0KDqbi-IYAqgGiBPYrAwisStMHVxw7JsTS3g6WtSLPbj5je1v3SSjLb1jMng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مهدی مطهرنیا:
شاید به تهران حمله اتمی بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/134938" target="_blank">📅 03:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134937">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
مقام آمریکایی به وال استریت ژورنال:
حملات آمریکا به پل‌های ایران با هدف قطع مسیرهای تأمین و پشتیبانی به سمت بندرعباس انجام شد؛ جایی که ایران یک پایگاه دریایی دارد و از آن برای حمله به کشتی‌ها در تنگه هرمز استفاده می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/134937" target="_blank">📅 03:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134936">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c9soW4T5P2gisou9jgY3IOvPT3ESKG3PFOhMWqoBh2YKy5wHsB9KIVcSYBZ514jFQUaKaG6EtaKJN-WTG5ySJaD4arXYjR9jDhYZXpf5q30VxcLK3dzFUBQFA7q5X9g5vduPmg92ZVacwoQMOozNUart7hQjmbMcdpKO9Czv4BgQLUXt3kR16CNKlzDySzW5TTivroagtRyEBlLbhP9N99AnEf0TY6KBbrRsj6Fbur19bJTwM6ej6wnyDSa6LMJeI3nBIe164xAJBQSSFZcsHOnWQkTQQ6YNrfuMMhZdsbSeQmBnWZ4bvaSfv1M-3ArzoyRsxJuomd-bPY5AqemJBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسمی: فیفا اعلام کرد که سلاوکو وینچیچ داورِ اسلوونیایی، برای داوری فینال جام جهانی 2026 بین آرژانتین و اسپانیا انتخاب شده، داورِ بازی انگلیس و فرانسه هم یه مشت ونزوئلایی انتخاب شدن و خبری از علیرضا فغانی نبود
@AloSport</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/134936" target="_blank">📅 03:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134935">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
دقایقی پیش اسامی داوران فینال و رده بندی از سوی فیفا اعلام شد
🔴
علیرضا فغانی داور هیچکدوم از بازی ها نشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/134935" target="_blank">📅 03:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134934">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
آژانس بین‌المللی انرژی:
در صورت تداوم اختلال در عبور نفت و گاز از تنگه هرمز طی هفته‌های آینده، نگرانی‌ها درباره امنیت عرضه جهانی انرژی به‌طور جدی افزایش خواهد یافت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/134934" target="_blank">📅 03:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134933">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
برخی منابع از وقوع انفجار در پایگاه‌های آمریکایی اردن خبر می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/134933" target="_blank">📅 03:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134932">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
وزارت دفاع کویت اعلام کرد تمامی حملات ایرانو رهگیری کرده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/134932" target="_blank">📅 03:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134931">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tw7S3lbtmvgEWORIdNUQc2HhCse31D0A0Q57rJ-MNSRCvFRMBC90P1_Zw3kzgwcRJqd4js0olaZV6k1A6QwJ5dAXKP7oFvm22WkrplbRmzu-yugDmWcekTeX5ZkDqxmt3KWo49S1rn2MW89nRmk_Wd7EocKsrHg7JvsRxIBNfW4ZehdEZzYcUF-UrVRSI7NMm8Yhc4nxIUWh_o4yACU8c73H9irn_2HSzVARH3VHMh9Rz8GdD92sQj3P9qsF84E6i209m81qZQ8nlXAaND1J5M5YTxmT7ZTHJpyvwX5pzg7XHwRNxoqzy_x6zNbXT4XTAtSjqMUJPg5822tj5EwNGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیمای عراقچی رو آسمون ترکیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/134931" target="_blank">📅 03:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134930">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
به ما میگین وطن فروش جنگ طلب چون نهایتا ۶ ماهه داریم میگیم ترامپ بزنشون!
🔴
شما که ۴۷ ساله هر جمعه دارین شعار مرگ میدین بهشون میشین وطن پرست جنگ نَطلب؟
🤔
این است شعور و منطق عرزشی‌ها!</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/134930" target="_blank">📅 03:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134929">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
سی‌بی‌اس نیوز:
اگر جمهوری اسلامی نتونه پاسخ قاطع به پل‌های تخریب شده بده٫ حملات بعدی امریکا به زیرساخت حیاتی‌تر ادامه خواهد داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/134929" target="_blank">📅 03:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134928">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eqcuCwJf7Rsdq3OGrUlBriPSFk9BS0xyC7uTEqIALwUYBIjMMzHX5-_BjOwC40Jz3Kzop0_1SiYk8Lr-n91nOUhlx0QdCBqq6FFeMbU1D7cDD2Ky0S_ClGMUh2qzJD30BmWgWlKooBJ3PO0lZyBIElNPozqJm-EumpJhilJTr3LY8iT2W2ityJXqtchzhI2qI1xqRKr5A06IUxYy9TcpwApn-F19GT0tkfRO-k0WuZGMqr-dO4NO6QWXZ5kKNLHZGIjklVQLILMZ5EDZVyedZxBx63ZbAK60sFAJnRuqc_ZUtKTLhYo7kQqUJ5XK7cgnlGdBQl8PLHNGp8vV6O-kcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت آسمان بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/134928" target="_blank">📅 03:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134927">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afvjIyf_6n-EqshjvQ5eXWRj3Kk5cMHH4l3cCKDaQeJ7km06-Giox2VuvWOU63ROrwXTlCp5yXYq51y3uPkKpzyt2nKsx5V4emjTm_MPxr2zcpZXSpv9h8xq-Ymm8UKeLj_22N7iIC3N-Re9IiVQ7UbyhUjgtE3HCSWoUGaJwPHUi9gcNwyRu2jtbxx88RwpPNGrEwQIxuhlOxqNYp6NbYpprO_zFe-vsK-oooM_Cq3c1OVs0M_xc8eS-P7Jp-81e4LQhuogHvuZHlTcDPazGpafUNw-glMLerYU9M_kgKjh2HU_FeDK7FenQDT_2lp7R6MHQk6r6O0Zg8LFBuwckQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق آمار گوگل  تو همین چند ساعت، سرچ کردن جمله[لغو عضویت  جانفدا‌] افزایش چشمگیری یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/134927" target="_blank">📅 03:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134926">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
انفجارهای مهیب در کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/134926" target="_blank">📅 03:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134925">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91c312ce96.mp4?token=O96H3-WmGCjumqmsjK47iY_a3XSUIJF-GjjH6F860zXdocs0CcEwSOmXxdVtAnvvXdv4IE_hX2u7b0TiUL3U5S7vy-EOb-foaT68O5lCwZkNbZA41alPY2c4kR1hJntZ66y4uuY9GnBR5-yuhentgtdQ21g_aArJC-8iFQ44QBoOaozH0n4Elsl6Phf-aVDMMzK2QzYHImy7xoWuqDogQI8ot3LGGEiXg7tfDWIR6Vv7PLZH4COZHoUSTy95H6jw3u1-tiIcvaVWKZOGItHlDdHtZHQwopOg0aAnDxYBIuSezZp1_rYhueJo-syAKjOhcFYPd12dVafInS6iuyptyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91c312ce96.mp4?token=O96H3-WmGCjumqmsjK47iY_a3XSUIJF-GjjH6F860zXdocs0CcEwSOmXxdVtAnvvXdv4IE_hX2u7b0TiUL3U5S7vy-EOb-foaT68O5lCwZkNbZA41alPY2c4kR1hJntZ66y4uuY9GnBR5-yuhentgtdQ21g_aArJC-8iFQ44QBoOaozH0n4Elsl6Phf-aVDMMzK2QzYHImy7xoWuqDogQI8ot3LGGEiXg7tfDWIR6Vv7PLZH4COZHoUSTy95H6jw3u1-tiIcvaVWKZOGItHlDdHtZHQwopOg0aAnDxYBIuSezZp1_rYhueJo-syAKjOhcFYPd12dVafInS6iuyptyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وقتی میبینم اونی که به ترامپ میگفت عمو الان داره واسه جنوب استوری میزاره
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/134925" target="_blank">📅 03:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134924">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d08de537c4.mp4?token=WmYZ0GBJaCPGd44eWEKYZrgXGfr0_DP4HKPQxP1bdqL2c1nEVXgoYUPY78MsoYlxb3PFhbHdJown4pPkoZWVTgV5CNBI-Qo4CkaTij1-mTOzaCDDj0fFMWdBIYx4vZ2C3T5ixz4Wkgw0vBWDbGZKDRpFsRuvbCrfPVXD-dYTLiRKcVx5v6MzdGTdiX29BDBy0t86Lhl2F_JPSi9weli1z0D209y5YNVJ4NBnF4PCngEH4vgtAmMpGHIfFNn4SKBEvHmTkChmiaJl-cXKDiG0gkY0auC4CJSwSdZwM8hOeBX1qiZdl3eQgD5c3rRPaJ8P2UKRQpIAFc2bbZR8XJ7bZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d08de537c4.mp4?token=WmYZ0GBJaCPGd44eWEKYZrgXGfr0_DP4HKPQxP1bdqL2c1nEVXgoYUPY78MsoYlxb3PFhbHdJown4pPkoZWVTgV5CNBI-Qo4CkaTij1-mTOzaCDDj0fFMWdBIYx4vZ2C3T5ixz4Wkgw0vBWDbGZKDRpFsRuvbCrfPVXD-dYTLiRKcVx5v6MzdGTdiX29BDBy0t86Lhl2F_JPSi9weli1z0D209y5YNVJ4NBnF4PCngEH4vgtAmMpGHIfFNn4SKBEvHmTkChmiaJl-cXKDiG0gkY0auC4CJSwSdZwM8hOeBX1qiZdl3eQgD5c3rRPaJ8P2UKRQpIAFc2bbZR8XJ7bZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه حمله به توپ ضد هوایی سپاه در بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/134924" target="_blank">📅 03:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134923">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WtvhRBg7_odCzGcHb3o9Ll0vZwXv-LVyU8cr_FU7G67zmsxYmaw7VVz8NMwkLfNoDO5XeJiVtonQr_vRf8cTi516HSbDEHOet7utzXu7CPKHHhmG8lx3yykjAPaW6yZJO_vEztg_tkKtrcw3895W93eFCSPH-U84HLonwPJ8-vevEHZiEMKy1kypPh4y4nNum_vSUpKmv8C5oSjzZSmV94a1f4-NH-CDjJYHuGb_UaBQFhucYX8qIZpFZdBYn_NRd-fsVN_C954GvfAEuzba1k9JLwIXv9CxLPIdb7IUBgKZk6KVfhhB6EDwHPWkAgqwmQyBiVkXlwJUtZAHSIrKIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش
کویت :
در حال رهگیری حملات موشکی و پهپادی هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/134923" target="_blank">📅 03:01 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134922">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
آژیر حمله موشکی در کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/134922" target="_blank">📅 02:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134921">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/upJqyvYv_cHxZFdvMjcIcJK1eYPNSoUXyyLwGcJ1X5ogdlH6S2STfIdjM2XwPr5uKgQAExjrh-3lbVl1e4H_P17g6v2HdpDPI0bBj9m6Pp4jEztDSOAN-TSqHN68JXlx622QlLBErd4VPBpmMgVRPfkgEXi2EMPBQFd0uNyquRakEj50YSzossiUVXRKTQOYVpfB0el9x5KVz32mksysWR0qTcXKWKutcxByDCcZFGkCxOjiWhV4ADo7lGqaBP5Vqkd3UYt8x5PD6CcVVc7naoAj6IUZ5ZR7dPceTNrTfSBBTT__HglRxQI986hkYJnifWgjzhs93syUPaAqy4-wDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شبکه خبر نام دور جدید درگیری ها و جنگ رو "نبرد هرمز" اعلام کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/134921" target="_blank">📅 02:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134920">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QH11KWik8ACsniQskC57HCkeOl_pJhKpbmSXsi2OTDNGKiaCRUjq9OAXzk8OpNLXvmYf82pyk3SYnP_FYd2VQtnCSlw_chGktEcTw3rpOXgbn_U-KP4s2rpprGD_qCqCWQBrisZfhn6W31nFg-d1eZET3WOb5v-La3Py8E_M3Gs00xVtSOTU70PASH8rhdjFKJr3KJn6wKKrOsuBIZQW1s5_ffY8Uy-no-ccxMClZGMAM-H4tUateYNLvl7vpIgje0AK0WlCfUze7hIB8ygcKVy_MdyeLgrQuN0inGmvHdTDMPb37IW-OBV504WlAZ4eJbDjwlbtPPomfor9a_Yiog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون حمله موشکی سپاه به بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/134920" target="_blank">📅 02:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134919">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JniQAOebjnVQ33vpQ0FwgLdC_wtCEqpycWkUvnluqT7E5-Bb-_YHL5M8CstxEHSDGGL45awiBQLPKbXK8YAuH4lDF1lxFihwES7P5S-ryS0jxRMP4jHR_dNFERuQKPqCmRjNhSjfKX8IvYXHT80KMtL5rGwRFz6kBaKbtw5jY6su_pOv4QwuxvmKvoyvR3ET0JSKON0BmOsToUU6oQeER6jVGTyCmHdXnKjC977muanuIP-rxjt8_JQiw5nA2AC512neivoFJiEeAoYeY6UXcceBw2_rkd9JLt2KDseS2knJ2D-D2f8gcXqcEZRlYe8Jo1dN2i9Xm6OzgUNY-gFNcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیمای عراقچی در حال خروج از ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/134919" target="_blank">📅 02:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134918">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhFSth0sTNguWWJv0Cp-WIY6ag7bl1g62pMtNEz0zATPm5cwkfZFUMDz1q6mljLRA_dfEG2Ut52KEzwDoSHtpJ8SsP-qwgHvtz8FWzXTHTYiE2hgqUVe1cyQCMxPEiGmh0yRdF9eOlp1EzQsI3CRwQFKZJ18IV6QjIFoEsaesgTG8WFLI8lkeVpxYGD3kJYSAvGE_ZUFXEhsNOAoLQR8iYFRCz64D2s8P-qHkzu8ILakWuMEAAZj14raGdV3hN7ZhnpPqtZ136-ozNagE2hvuzp-X64YPTYB10qryW9ELMwG3DTBj95c42aOP37LHXadMa4yqsX-eokJ2iuLsVlR_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ستون دود در پایگاه دریایی بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/134918" target="_blank">📅 02:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134917">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/530b6d1ce4.mp4?token=pD9X261JSqsukBsjoRs5ky33ascdDi5KyaGQK_oBIJBZhJZYZtXLLnl5QsfXbbohLPo4fgGJrdwpOIKcMb1sqQHnxV6ZcYUKkwJGwJaqRm7VP__OhCt1GppCK8REcn78IBpU9-87k5lcZ8pEZMGifMmofnXrIFLXFA2B86ZJbDitzLawSmCzLFF4HVS0Ka60C3quD8hYJhq58gDSQ4LB_puILrbatkq7drREGO5zVjNSJEVjPaj1_k-iBeW-pdKZXz95ti0zzpMS3GRbF5oMBL5gawpFwKiCHy-GvnVHEQ179iEBOTc7FJADO9UONeAXpdFD8U19lw8AcR6Nv538IF5N5W9GnEYuJKcwFB0LiUKc9zlfa-E--DiSKDIIjfqiLAJDuf9rX6r9pv-gQVQZhB_dJDKOtyUFqy_YgSmdHoWW5g5LA83RYeeJSllmGOhnguH--4hBkXr2l9OiypBCUTQgpcuY7grd-6ytxsXE2Ab97pbgN_wMtwYdLyHGir7wQRsxe3D6MK_hlwyIW4K2V71lZv-bO6msF0Fix26T2JbBcsB9ThoBuA3Pf6OovzGGCUjYRO0cgSvsUyzvw4RgtXq7r1T5-DbsxWB7An2QEibiidI1g7Ei9x3H6Ed6hWfrm8kSX6Z_yXqH8iKyKGDl7N_fZ_V2QAn13bcQ367YIqU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/530b6d1ce4.mp4?token=pD9X261JSqsukBsjoRs5ky33ascdDi5KyaGQK_oBIJBZhJZYZtXLLnl5QsfXbbohLPo4fgGJrdwpOIKcMb1sqQHnxV6ZcYUKkwJGwJaqRm7VP__OhCt1GppCK8REcn78IBpU9-87k5lcZ8pEZMGifMmofnXrIFLXFA2B86ZJbDitzLawSmCzLFF4HVS0Ka60C3quD8hYJhq58gDSQ4LB_puILrbatkq7drREGO5zVjNSJEVjPaj1_k-iBeW-pdKZXz95ti0zzpMS3GRbF5oMBL5gawpFwKiCHy-GvnVHEQ179iEBOTc7FJADO9UONeAXpdFD8U19lw8AcR6Nv538IF5N5W9GnEYuJKcwFB0LiUKc9zlfa-E--DiSKDIIjfqiLAJDuf9rX6r9pv-gQVQZhB_dJDKOtyUFqy_YgSmdHoWW5g5LA83RYeeJSllmGOhnguH--4hBkXr2l9OiypBCUTQgpcuY7grd-6ytxsXE2Ab97pbgN_wMtwYdLyHGir7wQRsxe3D6MK_hlwyIW4K2V71lZv-bO6msF0Fix26T2JbBcsB9ThoBuA3Pf6OovzGGCUjYRO0cgSvsUyzvw4RgtXq7r1T5-DbsxWB7An2QEibiidI1g7Ei9x3H6Ed6hWfrm8kSX6Z_yXqH8iKyKGDl7N_fZ_V2QAn13bcQ367YIqU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آخرین وضعیت شبکۀ برق شهرهای مورد حمله، از زبان روابط‌عمومی وزارت نیرو
🔴
مردم با مدیریت مصرف برق، به برق‌رسانی پایدار به جنوب کشور کمک کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/134917" target="_blank">📅 02:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134916">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a82adfa6fe.mp4?token=F8IS48cZxMLTVVr752_oREpjR7fLBnWRTN6um6o7ka4U8J-ZYkNk10D7ZB3Ub05_4QUcohsG1VJXwJ7OQxbwJ32DcZxEh8v5pu4NQ_c6RvAKrYHmRto3F4ccbjd8pTQLQtOyYAd1QxQ3RhFIP79Uyz_lIrfMF8ptTMKqabpKABJyhpoOaNn-e6tZCqoUr0RkYKCTNjwWYYBPdtpBQ9M8bFkrdxGzX82XDcKZ6WGYLJ2Y8qNTG9QO2Gkf8TPC_KoLGK1TXSk00gQa5qJc6yAM2tPK_Mt7bMAl34xkejEcmAXD4pVR8BCN2T3UPaLX5TG1mkUYGDlCX91Y7Mx0k5IUcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a82adfa6fe.mp4?token=F8IS48cZxMLTVVr752_oREpjR7fLBnWRTN6um6o7ka4U8J-ZYkNk10D7ZB3Ub05_4QUcohsG1VJXwJ7OQxbwJ32DcZxEh8v5pu4NQ_c6RvAKrYHmRto3F4ccbjd8pTQLQtOyYAd1QxQ3RhFIP79Uyz_lIrfMF8ptTMKqabpKABJyhpoOaNn-e6tZCqoUr0RkYKCTNjwWYYBPdtpBQ9M8bFkrdxGzX82XDcKZ6WGYLJ2Y8qNTG9QO2Gkf8TPC_KoLGK1TXSk00gQa5qJc6yAM2tPK_Mt7bMAl34xkejEcmAXD4pVR8BCN2T3UPaLX5TG1mkUYGDlCX91Y7Mx0k5IUcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی وحشتناک از حمله به اهواز
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/134916" target="_blank">📅 02:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134915">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fti9tqdW5TLkmzSM3pwVP382PpG7mk7C0IEzlG4ubPEpO7I6ZwHw-6pAsgUcI8LU1Bfeor91ZwHUwynal3mtFmRwZa7lDf3HjJjcmf1u499ndIfz6joPZP8m6oNKDHAyd6qmkGvNWknlhVKEXX6Kfda9whhdiwJZLK3lV1w19hxr6ptjIK61aKW947lF8k7FESDWwPWvz0ilIqS_ebgvh_GcshvAwxitdmZ-BV_9CgQcDDSEjNqkHyA7bc04Icp0C15GvPBC_YvyIfx_JTvX9F_qfSr7n15NaeB87kLB6pQNyCffLmOjjLBBDmZZhBGFzdEM1gMrO3I95Kjb9DWDZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نقشه حملات امشب آمریکا به ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/134915" target="_blank">📅 02:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134914">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
گزارشات اولیه از کاهش پهنای باند اینترنت در سراسر کشور
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/134914" target="_blank">📅 02:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134913">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
چند دقیقه پیش امریکا به فرودگاه بندرعباس حمله کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/134913" target="_blank">📅 02:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134912">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
انفجار در بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/134912" target="_blank">📅 02:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134911">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7aa57774a.mp4?token=aCsG91lqxpevv8sZ_5PiTDQT8k7rw7dd2yTA-HPobUQ4XaRgRb3Bf1fe-pYETzfWp0Lmp4bU8nTsiANxh8HhnjEHkpok1-fgbPqXyLhmCjTJQu94-4zj3PvnQMelsCZOnFH5BfEMvykoIJJjFigVemFvLePdTgieopW1VAXVWOllT9tjLPuMSt5eVLP735MFO45MFeRl7ReaAQOkbgJFSs6vyfoocdKFC8hqg6IbmOtJHjxZP1HMe6puONV6BzYKSG-hX0-det8kHe9ngIDX859QNplEX8MqL3ckTVl7jass2EQUSN2SphQjvTKZhexS246InkcBbk7jn90anpZpUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7aa57774a.mp4?token=aCsG91lqxpevv8sZ_5PiTDQT8k7rw7dd2yTA-HPobUQ4XaRgRb3Bf1fe-pYETzfWp0Lmp4bU8nTsiANxh8HhnjEHkpok1-fgbPqXyLhmCjTJQu94-4zj3PvnQMelsCZOnFH5BfEMvykoIJJjFigVemFvLePdTgieopW1VAXVWOllT9tjLPuMSt5eVLP735MFO45MFeRl7ReaAQOkbgJFSs6vyfoocdKFC8hqg6IbmOtJHjxZP1HMe6puONV6BzYKSG-hX0-det8kHe9ngIDX859QNplEX8MqL3ckTVl7jass2EQUSN2SphQjvTKZhexS246InkcBbk7jn90anpZpUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه‌ی انهدام رادار ارتش آمریکا در کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/134911" target="_blank">📅 02:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134910">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZByEMbWGw6hyH0yVn8YQQdbZYbKQD_TR4m5swhyMhEmn1d2UrfuCq7d8LJZs8_2I28Zk_pfbIwVm68BH2ZOytUUUoKR3_z_KV3yRq-cprY3otFTGU3Nr9bbnoRJoidknMBySE7PhY0gJa9puO4Gbbjl6teoQvI_rDs8ERcJLbBC9m4HElzyeHSb3fiIpkQ8fYIXWRpeTWGTg_f2N6zNLi6OS8pctGT5c5XgP5VqydulPziUgJ-sYlgU3pK4-Hq0T1qfnWJbkNrG18-h60dCPakfUDL6uzdsXxBm_IAXeFLviuHpuys_LX6s0CmcGunMEFmGnjbBcAOeZPpv4gdD8VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سایپا از محصول جدیدش برای جنگ زمینی با آمریکا رونمایی کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/134910" target="_blank">📅 02:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134909">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">💢
پشماااااااااااااااااااااااااااام
😐
برای اولین بار همزمان 25تا سوخت رسان تو خلیج فارس درحال مروازن
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/134909" target="_blank">📅 02:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134908">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HBDLrEtkRwkaAohZ_TRoMN9kRYLKzYYuz4e08Od2en_56gsZaLsI8iw9NGfukkLbBhfgGEji4uFNCPguW87-b7PGkpUU_bOJZQUvImVOsLqnMf6GTJYNeJgAoKhR0QZxRc6KdJiuvm2BbyKQlkS3mWohLaK9JT5YN57JqYNMVjx4dIhgIDVcqtfuf1ELiwAvVuQOzLLHxom0LCVt43hoXyDSWFEtZpIf114C_tdDyKM3eaEfgjwJRegC6l9Ui3InEWI5626_YSFidaAd28dqWtaD90c0aChRlmqqj0VncNQyzQJ9u1DCfQwpluNKP3OftZAeyWG0yZ52yCmHJXujXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هگست، وزیر
جنگ آمریکا :
ایران کنترل تنگه رو در اختیار نداره
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/134908" target="_blank">📅 02:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134907">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
قطعی برق تو کیش برطرف شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/134907" target="_blank">📅 02:01 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134906">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93c5684acf.mp4?token=OvDT9XJgvdDJTXqLZHrwHP1cqMvXTFVVmVSlaA-_r2XE1vDtLgSC89KH7yISG2u-ygkJL2rJgp5rmu6xvp9TGqOpovPfcW1Gp-41KDfS-u4n6euUb1yWTFuglOEnsLq1M1jajzMnsPh7bUNfejMMxBrJKSVJ36-vi5rZ08C7pV4vk6Grwt595qspX4BFejGDvvimTr7oxWPGd7cz_cdGTloVWj250oyZqsBKDuw3xXbQ2DITez2OC2fQzRMg2wQVR2R-EqDC2nxwBA0HEibeHST1eXp63SATCtjMyTpzLWYpri2vipIPEMzD-MwPZmkdbiQVmMlrBqJ-0CJJoG2JUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93c5684acf.mp4?token=OvDT9XJgvdDJTXqLZHrwHP1cqMvXTFVVmVSlaA-_r2XE1vDtLgSC89KH7yISG2u-ygkJL2rJgp5rmu6xvp9TGqOpovPfcW1Gp-41KDfS-u4n6euUb1yWTFuglOEnsLq1M1jajzMnsPh7bUNfejMMxBrJKSVJ36-vi5rZ08C7pV4vk6Grwt595qspX4BFejGDvvimTr7oxWPGd7cz_cdGTloVWj250oyZqsBKDuw3xXbQ2DITez2OC2fQzRMg2wQVR2R-EqDC2nxwBA0HEibeHST1eXp63SATCtjMyTpzLWYpri2vipIPEMzD-MwPZmkdbiQVmMlrBqJ-0CJJoG2JUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/134906" target="_blank">📅 02:01 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134905">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tX2NQ3k442wHkCWCWBNDTeNDLj1i_0ZQ1srr2TaKvkdl-rdqA7V-zTAKdtSbSjRQ_NIN9KLqZLxa3E6CEUKvK6sMgbilD6L1G54_rfKX9CcMXW4zGOSi9EdaQw5jOxwFWEAciOdfUVMhO8BNOh9vsNzXO5OdvBUJnq5p-GDk9vPBYMBfrGQxx4gJ_G9vzmpo0gjxy0Rqyzb1KTKAUfFGVxXqwavxu9H5Mnr1AIa7icMpfumxC1Ee7DMcrG_XfKqnDLmHfzvhg1IqOUvpf30RRSs-qv8ye21fC1h28ZUiRF8V-2s__u-X-hCOEjm67Emz7IETxidFlwYuDNRIVZDB5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اسرائیل
المنصوری
لبنان رو، مورد هدف قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/134905" target="_blank">📅 02:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134904">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83f0d99f1e.mp4?token=EPeuml65HdU4DeSB5k60X8xiUdwleVMgaHpr7NiWUqStXewdiao7Pvq89VHihWAMxIwOXgiu3f306f5G2vDXLj5-_vTvBqA7k3rN-C8_yDvaXft4f0x80G3gJerrKqhS8mhmivKCu8331x1hBqrRtpTcZ_izM6l19yxlK2zoluHl-p6Icf59TsbfuWp7CBoOSPALDO-nKsvJKs7WDAU-QW8UEhhaUJu-uHPU6R7Wz2dmYfucwIBwKnDNucYZ938KDmAEe7AFhTtGhIbdNM3yZf8pc0MfRNAQ5RoZwWVLzYlkRjXCPP0Ih-EUyp5AlhIhrSieeGJhEj0BGfXnOb8YXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83f0d99f1e.mp4?token=EPeuml65HdU4DeSB5k60X8xiUdwleVMgaHpr7NiWUqStXewdiao7Pvq89VHihWAMxIwOXgiu3f306f5G2vDXLj5-_vTvBqA7k3rN-C8_yDvaXft4f0x80G3gJerrKqhS8mhmivKCu8331x1hBqrRtpTcZ_izM6l19yxlK2zoluHl-p6Icf59TsbfuWp7CBoOSPALDO-nKsvJKs7WDAU-QW8UEhhaUJu-uHPU6R7Wz2dmYfucwIBwKnDNucYZ938KDmAEe7AFhTtGhIbdNM3yZf8pc0MfRNAQ5RoZwWVLzYlkRjXCPP0Ih-EUyp5AlhIhrSieeGJhEj0BGfXnOb8YXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرزوی فغانی عزیز به حقیقت پیوست
از داوری در زمین‌های خاکی هاشم‌آباد تا رویای قضاوت در فینال جام جهانی/
علیرضا فغانی بارها ثابت کرده که موفقیت، حاصل سال‌ها تلاش و باور به رویاهاست. او می‌گوید در دوران نوجوانی هدفش قضاوت فینال جام جهانی بود، اما بسیاری این آرزو را غیرممکن می‌دانستند و به آن خندیدند.
#نخبه
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/134904" target="_blank">📅 02:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134903">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
دیدن این ویدئو برای همه لازمه
🤔
مخصوصا طرفدارهای حرام زاده حکومت</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/134903" target="_blank">📅 02:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134901">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/agZZoRrNLba39OeHopqPYlgBi5AelC0keth-nUMIGD52KGCLwJw_V1ZDgylyMRuXBctkTmqTuH75No04h-8fnV0iAP7m_AcUgKBE7FZHkEqWcCUpM6H-U1ETL_Vq5Ye6c8helBNL05OpAQ3mrRwoZeUO3E0IJ30sWuxoExW00CSidYiU0EwmsyiXd3I9xOjHcsD-OrPelOaEPTqDrJF_j-KUgUCkMKd7Ww9ELO0slF3ZUDJ8vw-hZ6olIDZM3BCfsm6mf7twMuOcpqvcG2LH4LHwTpSm2HQLbBWSQNT9WAagxBUlJXkKLfa4TPFp9EiKuJO0Wc_soJhGqYGiKNxeeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بدون شرح در صدا و سیما
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/134901" target="_blank">📅 01:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134900">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KPXWxUx8DLsArzKiMVjFEx9kZyi9wkjntX-m3AcgLMVfT1W1eaa8g4hxnXqU1UCsvFk_89Ce85Q4lqc9n8mvXI28bXqdi2YA34dsr5LLvI0u8rmJEZFuGqjSdmL_MVAcmvltlznPbnLwRhrgF2qOS-9-BNnc7HiHqt-zZHic9e0uE4puoDxJ1xz9zzoIlqTRrjlyHIDxnJeKbrQOG0qJJdP-wDZY1fR7htJGWBKp8nEWkPWSJ7cEYaSTLUrkr3nV9iw40o0AkLSaAB66SxDftEXHb8TeCRwpl7rQdq-VIBJjoHrsHCZoFpZkDDXj23VDLLqU28HWsJkrDQC6IQDnhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
استوری جدید هادی چوپان
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/134900" target="_blank">📅 01:55 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134899">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
فارس: حملۀ موشکی به پایگاه‌های هوایی و دریایی بوشهر
معاون استانداری بوشهر:
🔴
در حملۀ دقایقی پیش به بوشهر چند فروند موشک دشمن آمریکایی به پایگاه هوایی و پایگاه دریایی بوشهر اصابت کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/134899" target="_blank">📅 01:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134898">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
کاربران از شنیده شدن صدای حداقل ۲انفجار در کرمانشاه خبر دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/134898" target="_blank">📅 01:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134897">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NcGOQDK6UPdJN9-_HDrYtMpGOljWo57kDFmeE2EpKbT0TocijAZ8mcLULyJfiOKhpTgHq_N2ZHz_Hmol11k6-wIMbwYNwp7XdcQ5bFnq53XdKUdM3WXr2O91arP4i-vS8tmc2T2AjRN9Y5K7E1w4iss16iwbO9heMCVpxbT8iqeoYDN8uYna6rpC1qmIb8_wHb5d5xNAvgH1EFs4pGp6WstygRfMSXqypklwK9o_jRyq8y4-BqLqscljT1pvV5-SX3okrH6kx1aKJyJRWFH2ICGbVkAzvnFQgoA_U1TbeA0_ZdOhErgkBd4MzL6UNJMJHg3vT4HvCg6CgL3EPziwdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اربیل عراق پس از حملات ایران در تاریکی فرو رفت
🔴
بر اساس گزارش‌های اولیه، برق در بخش عمده‌ای از شهرستان‌ها و نواحی استان اربیل اقلیم کردستان عراق به‌طور کامل قطع شده و هم‌زمان پرواز جنگنده‌های آمریکایی بر فراز این منطقه ادامه دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/134897" target="_blank">📅 01:49 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134896">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/899752499b.mp4?token=u4v8DYQ4j8YFKiLlBh4wnHOsQU7400psTP7t_NRiyM5wkrupPAzrt-N70jVo4fF6rd-BkBWqr9CAslsjrzOJ91pJoTRjiO1wGrv-oBUDNVAMTBkoPelDWkjClS9WqeiLEcCYH9WUzBPPgmE17PiXrgetIxCjM_9JO-Wfzu-qMEnchJabtoKo7jrYaF9QaZxEriUDLunV02e1hPh0p4pEOy5E-Ph_1g6Huxni-5WsvylavqRr0GOVzgJwJZvcQId6pjB-pAr8LrvYzpIUxa4-13zCQfHGc74ROx2pKrcZfy20MEHOq9b_GA3blYnKRJxGqZtTeKC11mX_KbKvHHWbLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/899752499b.mp4?token=u4v8DYQ4j8YFKiLlBh4wnHOsQU7400psTP7t_NRiyM5wkrupPAzrt-N70jVo4fF6rd-BkBWqr9CAslsjrzOJ91pJoTRjiO1wGrv-oBUDNVAMTBkoPelDWkjClS9WqeiLEcCYH9WUzBPPgmE17PiXrgetIxCjM_9JO-Wfzu-qMEnchJabtoKo7jrYaF9QaZxEriUDLunV02e1hPh0p4pEOy5E-Ph_1g6Huxni-5WsvylavqRr0GOVzgJwJZvcQId6pjB-pAr8LrvYzpIUxa4-13zCQfHGc74ROx2pKrcZfy20MEHOq9b_GA3blYnKRJxGqZtTeKC11mX_KbKvHHWbLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آیسان اسلامی درباره ایران اینترنشنال گفته که از امشب باید بگم دایی مراد بیاد خونه؛ مراد ویسی جوری حرف می‌زنه که آدم فکر می‌کنه فردا باید بلیط بگیره برگرده ایران، ولی باز هیچی نمیشه. کانال رو می‌زنی روی مهدوی‌آزاد، اون که یه مدته داره خار جمهوری اسلامی رو می‌گاد و علنا قاطی کرده. قاضی‌زاده هم مثل مبصرهای مدرسه‌ست و اصلا شوخی موخی نداره. بعدش که فرزاد فرحزاد می‌اد، فکر می‌کنی همین الان دیگه انقلاب شد، ولی بعد می‌بینی بازم هیچی به هیچی نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/134896" target="_blank">📅 01:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134895">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
انفجار در کرمانشاه
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/134895" target="_blank">📅 01:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134894">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
انفجار در کرمانشاه
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/134894" target="_blank">📅 01:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134893">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
سامانه‌های پدافند هوایی در کویت فعال شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/134893" target="_blank">📅 01:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134892">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fQVkIo-cA5GtdvsIo2Qij0t5kjq5jBMzhAFuT1Sa2EHhNqq_jz6NFb_ydNjwrOC5wD8BQGxw6K9F4FYe94gJS8IYWFeN3bkZzVpiGKHzhMWgjf_T6cggFVc4-xST7SN5ATwLSwOdZtQ7xDnXcvC_TbDSG0IBDivjiaPHygf34M5IQlqvpKySEu_gD7s2toiWmjdy5fEDmO6CEN5OqVbg_FOM9xgTtixo9GkHr0Zq-taghG_67yWW26WXlVkLaU_DzY4XLbA7pKXpeFdTfDN_s2A3gSaOQv5PhPu859lRxpzASqsEhr5bIz0D9oFM0HFDMGt0j1gLGlwYzxjuBOH7gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
نگهداشتن سرباز تو پادگان دلیلی غیر از گوشت قربانی بودن دارن؟
🔴
آقا زاده ها و پایدارچی ها اعلام آمادگی کنن برای پاس نگهبانی تو شهرهای جنوبی
🔴
30 میلیون جان فدا بودن که! هرکی نره حرام زاده است.</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/134892" target="_blank">📅 01:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134889">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SSMBABRWBwhW__rwRyF4OUPOw1YYNKLkMyFRNpnKSd-vonkfcPuxdiSLt-17WEM-J1a1ABL3LDkn79VsdgftY-JBFf4l3T-GDEvQfUu429swjypuQB6zxXoDZqLd9jZmLmOk16u1OwC9cmUDIwOPmG12x1lEKWYPfTeq_ayOofiFqhCcYpdrkM324QZfJqzPRbv2_PIMo-VHJQ6rD-aCK7BQmFamfod88J7LbialqmpFmnO8oxwrcxhslteBf44o7HqVbUn9UczZQOWHb0fkfsWCs_W1KiKHRWKan9wETGkNGqk3xMQpS5cKIhC3VpnpsgqHSQyYVxibQS-ojRyQ-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lzz3qTSNI4O4v9jB4t6eFI_TKct2us1kOYo54-E7m-EdZMTIcLyviTnL8xmPxF0ccysysQ9V9-L2eZXmmqAOs017hjtdmK1Als8NEjriO-zMyII44g9Kij8Kuu5zmTYgd8jxiTfF2NT0MW7eu2VYiFmZUoHGKS3tRIEj0zvIAu8SUZMZ9P0HUxYbyxNjTAjXgF8LGYqN9Lerkm5f5FCzzy47bFOc11ftNAiB6Hr1jjbaQHB6Y_yEe4OWVjR6Zu2sXo14-I-O_JiICNV30Wqzfqbjhda0c-o-4bbb--Ym0TiIyTqSQ2O67INRNfTFEIxmFxvxfgEMFhG7HzbnOgPjZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3d51fa3abb.mp4?token=T0dzfeExIYHsZE9s8whilU4ngIkV12Qy38UguAczzOoaVQbG0wmtp3RTidhqPL2daIr0oF8iR_vRsdU08xt92iHjpDOKI4aPIYLN6HTtq9U297FFy2dL3HKSliG_5yEIypR-aPsm7IR9cduNw_futBKarNC6BWMgcx2yL-dOfBMZ2s3ZfpZOObaY1JIj_FQ_D_xwAcIHW8aS6KfFCSmK1tEPneVCm6yIAwHyXUqmomiTrdg2GOUxM05otZeVOLA66ABW4MySKG3ZAOQ2Mn_kTOUdLK3fDELAFps1HqzBj9r2FdxjnogqXAx06u50LU02urhy4M8ehdO7v4L1pUtG6w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3d51fa3abb.mp4?token=T0dzfeExIYHsZE9s8whilU4ngIkV12Qy38UguAczzOoaVQbG0wmtp3RTidhqPL2daIr0oF8iR_vRsdU08xt92iHjpDOKI4aPIYLN6HTtq9U297FFy2dL3HKSliG_5yEIypR-aPsm7IR9cduNw_futBKarNC6BWMgcx2yL-dOfBMZ2s3ZfpZOObaY1JIj_FQ_D_xwAcIHW8aS6KfFCSmK1tEPneVCm6yIAwHyXUqmomiTrdg2GOUxM05otZeVOLA66ABW4MySKG3ZAOQ2Mn_kTOUdLK3fDELAFps1HqzBj9r2FdxjnogqXAx06u50LU02urhy4M8ehdO7v4L1pUtG6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
این وسط دیشب توی تبریز یه نفر بخاطر اینکه کل پولشو رو برد انگلیس شرط بندی کرده بود و باخت، خودشو از طبقه ششم انداخت پایین و خودکشی کرد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/134889" target="_blank">📅 01:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134888">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
انفجار در بندر لنگه
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/134888" target="_blank">📅 01:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134887">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
انفجار مجدد در قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/134887" target="_blank">📅 01:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134886">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2492a5baba.mp4?token=NTgKgZOX3i44qLugG4iGnleA708LBYedmyteRzKDpoxzuQI2R0StbeIQki67NOK8-S3cw3dFJqKzwdTlVFddf0HS4U8Wa6c3CMjzS_-bsaa5Q-MfIiDSSJrM8wFJWhxe7sIQggu1Hetnsl_HerJexF8txlnEGZ1A1ztKHNb2K0U-YH93042jIvIcKTI4fMVl6KW7Gxri81jx7rpDEXSjZQsRw87GzJ77ERe_G5kfEj4L3DP5j4DT2MvnqIAx0qYJwkHGU6m8DevTyZJ0EiIYCohrZxubxTDZHg5De9Gu_Q0__aL2M8_1IY1TF7EsiPdCVyoLoHRPY-DYfFPnGpVT2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2492a5baba.mp4?token=NTgKgZOX3i44qLugG4iGnleA708LBYedmyteRzKDpoxzuQI2R0StbeIQki67NOK8-S3cw3dFJqKzwdTlVFddf0HS4U8Wa6c3CMjzS_-bsaa5Q-MfIiDSSJrM8wFJWhxe7sIQggu1Hetnsl_HerJexF8txlnEGZ1A1ztKHNb2K0U-YH93042jIvIcKTI4fMVl6KW7Gxri81jx7rpDEXSjZQsRw87GzJ77ERe_G5kfEj4L3DP5j4DT2MvnqIAx0qYJwkHGU6m8DevTyZJ0EiIYCohrZxubxTDZHg5De9Gu_Q0__aL2M8_1IY1TF7EsiPdCVyoLoHRPY-DYfFPnGpVT2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که از یکی از سرباز های تیپ 388 بمپور به شدت وایرال شده که داره آهنگ میخونه
😀
💔
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/134886" target="_blank">📅 01:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134885">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
نگهداشتن سرباز تو پادگان دلیلی غیر از گوشت قربانی بودن دارن؟
🔴
آقا زاده ها و پایدارچی ها اعلام آمادگی کنن برای پاس نگهبانی تو شهرهای جنوبی
🔴
30 میلیون جان فدا بودن که! هرکی نره حرام زاده است.</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/134885" target="_blank">📅 01:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134884">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
دامنه حملات داره کم کم میاد بالا و به تهران میرسه
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/134884" target="_blank">📅 01:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134883">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
فوری/حمله آمریکا به شهر ویسیان لرستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/134883" target="_blank">📅 01:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134882">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50f3dd4a9c.mp4?token=kv39hoYsWK1s5sfjaBzBcBdHXMB2j3Ycp5DXXdY31zaSZjqrAVDQvpIPM7e4p8oDCMR5st6R67NmjocvgPXYBmIkgw1_XwGU-n17DCfN08cRWctt8e3rZ0NO3E0QEmaCK7QYQLlNjBrs83H5s7zEnIy0pFdO5Jcg075YFthWrLuzcukSEua5jPzl1-ukLT7fOuABdQt9Bja4XIDscxsH3mpKxXJ8FPvZ9_mgEqD1oPWBDWnnwK6SX4o9YfU-_yei4B9AkKTfsTXlHQq2mEcxBvmUU15Xj9aJE-7gka_C6IZSYnnPYaAz4IuFZpCGNEFTPDDvRlWvk1Xyp3VJy_wsFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50f3dd4a9c.mp4?token=kv39hoYsWK1s5sfjaBzBcBdHXMB2j3Ycp5DXXdY31zaSZjqrAVDQvpIPM7e4p8oDCMR5st6R67NmjocvgPXYBmIkgw1_XwGU-n17DCfN08cRWctt8e3rZ0NO3E0QEmaCK7QYQLlNjBrs83H5s7zEnIy0pFdO5Jcg075YFthWrLuzcukSEua5jPzl1-ukLT7fOuABdQt9Bja4XIDscxsH3mpKxXJ8FPvZ9_mgEqD1oPWBDWnnwK6SX4o9YfU-_yei4B9AkKTfsTXlHQq2mEcxBvmUU15Xj9aJE-7gka_C6IZSYnnPYaAz4IuFZpCGNEFTPDDvRlWvk1Xyp3VJy_wsFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارش زندۀ خبرنگار صداوسیما از فرودگاه ایرانشهر پس از حمله
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/134882" target="_blank">📅 01:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134881">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1faf6563c.mp4?token=JnCGqmEYsskwb5BZo0RcqGKg8dWIEPuJBYWPns8d8Xx1GOwzY_OinkBJhmdZydyFtnfMTnULwdcOqwsPlsB-Ra5H7dtOFl2AhEHnlT0faG4-WrAAy1tzRlQl0io_6WBI9mXLoIw0mWm4LXuyMrRiwhUGwiuMHexBbaaX7hZ6rkkLlp0YcK0n5NYspUYB6mz1Ob-QaSjLQ5XeAlNzalQJbetldzXs9hbH8vQsjqfhE5GcIaE4rPSDb2GlKACO50sjihqm0-1WRKOCX0TSvTHCAyYr3URQvqxao5_qTttbiJNVcA7MlBFrA8o6pQFwdNRCDNfSgnO0Z7TOrxR_LmqYXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1faf6563c.mp4?token=JnCGqmEYsskwb5BZo0RcqGKg8dWIEPuJBYWPns8d8Xx1GOwzY_OinkBJhmdZydyFtnfMTnULwdcOqwsPlsB-Ra5H7dtOFl2AhEHnlT0faG4-WrAAy1tzRlQl0io_6WBI9mXLoIw0mWm4LXuyMrRiwhUGwiuMHexBbaaX7hZ6rkkLlp0YcK0n5NYspUYB6mz1Ob-QaSjLQ5XeAlNzalQJbetldzXs9hbH8vQsjqfhE5GcIaE4rPSDb2GlKACO50sjihqm0-1WRKOCX0TSvTHCAyYr3URQvqxao5_qTttbiJNVcA7MlBFrA8o6pQFwdNRCDNfSgnO0Z7TOrxR_LmqYXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رسانه های عربی ادعا کردند که یک رادار آمریکایی در کویت مورد حمله قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/134881" target="_blank">📅 01:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134880">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
از همون روز که ترامپ گفت اگه حکومت مردم رو بکشه حمله میکنم ، همه چیز شروع شد.</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/alonews/134880" target="_blank">📅 01:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134879">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
اینترنت تو برخی نقاط اختلال شدید خورده
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/134879" target="_blank">📅 01:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134877">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7619330353.mp4?token=LRkMyo-7It0EmGm8-UFT96KQZK7OhZYkye_c0ZwCJN17YE7WZe3hs1mPoShVmo1jMQ8oRcuy3sqQhPMWX2cvRV8UWZw9lthJlRR8FnFDLhQ1q20xOA_6KssoJWhILlliYOYDKBr3_RkJzQMiBeWb35Crtg-y9T9gIquZP5ufL3S6ZUiM1HqG1a5dtz8Qia7SfZcCjFX8aVYtlkbuWmS3QZSVrRnLB9bs96MS7yOSHBLSADMXEOygreTd0D__romI76lkQEr-nMus5fJ7zg4h9rWldaDxGa7M__XFQczzvGRRCejCGy1l4E6r_EuIFnNKt8Ym-AyI9T95u1iLv-vXyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7619330353.mp4?token=LRkMyo-7It0EmGm8-UFT96KQZK7OhZYkye_c0ZwCJN17YE7WZe3hs1mPoShVmo1jMQ8oRcuy3sqQhPMWX2cvRV8UWZw9lthJlRR8FnFDLhQ1q20xOA_6KssoJWhILlliYOYDKBr3_RkJzQMiBeWb35Crtg-y9T9gIquZP5ufL3S6ZUiM1HqG1a5dtz8Qia7SfZcCjFX8aVYtlkbuWmS3QZSVrRnLB9bs96MS7yOSHBLSADMXEOygreTd0D__romI76lkQEr-nMus5fJ7zg4h9rWldaDxGa7M__XFQczzvGRRCejCGy1l4E6r_EuIFnNKt8Ym-AyI9T95u1iLv-vXyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امشب، پهپادهای ایرانی به مناطقی در کویت، نزدیک مرز عراق، حمله کردند.
🔴
هنوز مشخص نیست که چه اهدافی مورد هدف قرار گرفتند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/134877" target="_blank">📅 01:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134876">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
فوووووری/همه پرواز های کشور بدستور سازمان هواپیمایی ایران کنسل شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/alonews/134876" target="_blank">📅 01:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134875">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">💢
فوووووووووری/پرواز جنگنده‌های اسرائیلی به مقصد نامعلوم  @MamelekatDaily | پروکسی</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/alonews/134875" target="_blank">📅 01:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134874">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
هم اکنون بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/alonews/134874" target="_blank">📅 01:01 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134873">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
12انفجار تو بوشهر رخ داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/alonews/134873" target="_blank">📅 01:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134872">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
فوری/انفجارهای مهیب در بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/alonews/134872" target="_blank">📅 00:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134871">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99b324f9f1.mp4?token=QhbBSADcXTM_flaw3EbTvPg9kzBwjjKFZDXmI6B4pPVssmwHdUXc5w8Gc4JrHuYSVUYCL6qjE1yb4G--NgrfzOzUnLD7noTSSf__a2IcTuqVW84ES7j-IBblxRlYDoYqrYKcv_5vgy0G2A3S77BAe_V2BdSP3U6TDh26XAcbU6gBBxoeCuf5XALdc7c5v-5CAl8hb3-1vB4I4l64Wb3jyW6T4YnHOv7iDzDW98FYzIpxac5Td3BNCSfaZVu2nRDTA4WPMrJ1oJCmu2onpTEDScXXZKz8O7Iy7R8vNDFPDemHv7goAQS6kBq46ZvaKlIBLWzu3Eti25BzNM6aKteGpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99b324f9f1.mp4?token=QhbBSADcXTM_flaw3EbTvPg9kzBwjjKFZDXmI6B4pPVssmwHdUXc5w8Gc4JrHuYSVUYCL6qjE1yb4G--NgrfzOzUnLD7noTSSf__a2IcTuqVW84ES7j-IBblxRlYDoYqrYKcv_5vgy0G2A3S77BAe_V2BdSP3U6TDh26XAcbU6gBBxoeCuf5XALdc7c5v-5CAl8hb3-1vB4I4l64Wb3jyW6T4YnHOv7iDzDW98FYzIpxac5Td3BNCSfaZVu2nRDTA4WPMrJ1oJCmu2onpTEDScXXZKz8O7Iy7R8vNDFPDemHv7goAQS6kBq46ZvaKlIBLWzu3Eti25BzNM6aKteGpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سنتکام: تفنگداران دریایی آمریکا از یگان یازدهم اعزامی دریایی، در تاریخ ۱۶ ژوئیه، عملیات بازرسی و بررسی را بر روی نفتکش «ام/تی وین یائو» در خلیج عمان انجام دادند.
🔴
تا به امروز، نیروهای آمریکایی مسیر ۳ کشتی تجاری را که تلاش کردند محاصره را بشکنند تغییر داده، یک کشتی که تمکین نکرد را مختل کرده، و سوار بر یک کشتی شده‌اند تا اطمینان حاصل کنند که محاصره دریایی مداوم آمریکا علیه ایران بهطور کامل رعایت می‌شود.
🔴
تنگه هرمز و آب‌های اطراف آن باز و آزاد باقی می‌مانند، به جز کشتی‌هایی که تلاش کنند محاصره آمریکایی را که دیوار فولادی تحمیل می‌کند نقض کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.5K · <a href="https://t.me/alonews/134871" target="_blank">📅 00:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134870">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
شرکت ملی گاز: صدای مهیب احتمالی امشب در نوشهر، مربوط به تست و هواگیری گاز خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/alonews/134870" target="_blank">📅 00:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134869">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
انفجار در قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.5K · <a href="https://t.me/alonews/134869" target="_blank">📅 00:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134868">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
بخاطر جنوب لبنان، جنوب ایران رفت</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/alonews/134868" target="_blank">📅 00:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134867">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cn0rmS3Oc1UH1tWlXM21SBgn_AYr8VLTgIk4sDv5geXnuHjPnyqAEPoUwTbEeVi22wTxapgTAk8t3wpLtgI7TcvLshD_oH_toZSRtWDRi1zm5wkklho_lKct71fMBRgRuLuxPLLNTXR9NANplxPgBS0oJ5MvrUZmL8lXX7nj5oh5ydVjtWcfQ8fu3WXZ2HjUrHoNrIyex6uC407a0VVQZ1UFi32_aSd6FDP5UGtEkm4iUV_bNjKey2AafYUFzygjXVMLczMl0k2v66EDqysSPnQ-8IUDbhxuu9EZKmKlyTsqlc70SWoAvspPMYyVf-pcdDWLrV_H_FLmMWjLtf1KXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم‌اکنون / وضعیت آسمان ایران و منطقه
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/alonews/134867" target="_blank">📅 00:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134866">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eGSrVJchkn2C1svHn7q1t57cZmz0ioxQfR453_iSf0Y4F3UvkZMgY5Mvaabxgvet8wpSN7w11FbUrnfdBzYPKTuG2ebszuy7ZzCcsTl5BYhitK-rvZVa6TXAcb-vvUTmRQ9q5kTjvSS762DpyMkWBLYhaM3QrDfV9GWFQCQ46CzBDXNsMrOhkKd1Ged6aZDl0UUwzTQaM3Q9M1rapCVD0CLjqa1hWJml-6zVJ94CXagT0QwwZ7xaxxSh7GE6Tu4b7v_Lc4qaolW3QoO3QnMDLH7uJzvFDDyxajyqD3RXqbHLmP7v7LyYfx-NOVkVzdPHxMvaKLfjfiaLCpC9f_S8Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق داده‌های وبسایت فلایت رادار، یک جنگنده اف۳۵ در آسمان امارات کد اضطراری ۷۷۰۰ اعلام کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/alonews/134866" target="_blank">📅 00:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134865">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
سنتکام: ما آماده انجام هر ماموریتی هستیم و در حال حاضر ۵۰ هزار نیرو در خاورمیانه داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/alonews/134865" target="_blank">📅 00:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134864">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HFfhhAueEI9I8KhNINYj2hdVwFS_jpNCHvmcqriSczFDvzqLgXFUuH9F9XmZFKPvBRdlfobc0vAYJoDke_mvzyzq3UiNymkZqZmU7by1c6_O2ZKTmHbJbDUH1z4syIGCaVaxfdKkMM1FSkA983PhqpO5fukY2UzipiO-5DAaulShkz9fVR8cp2UduPUQptTlBV-qCubFRBbvH3iBtF-hH6wYRAvfIweAVBxWVCDr1gPWPupYR4VU3OcksK2r20rZK2amA2A3H8uMDV6gpcOnsaAE75utlxqna2uhX8w1Urkg8HOwjMmFwDlHS4nS-QnEq88vdWBz6NUTLH1x0UYC1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اینترنت موبایل تو بعضی از نقاط دچار افت کیفیت، کندی و اختلال شده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/alonews/134864" target="_blank">📅 00:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134863">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">⭕️
چند نکته بسیار مهم برای حفظ امنیت شما در تلگرام
🔴
برای تنظیم بیشتر موارد، وارد مسیر
Settings > Privacy and Security
شوید.
۱. مخفی‌کردن شماره تلفن
وارد
Phone Number
شوید و این گزینه‌ها را تنظیم کنید:
Who can see my phone number:
روی
Nobody
Who can find me by my number:
روی
My Contacts
بخش‌های
Always Allow
و
Never Allow
را نیز بررسی کنید تا استثنای ناخواسته‌ای وجود نداشته باشد.
تنظیم دوم مانع می‌شود افراد غریبه فقط با ذخیره‌کردن شماره شما، حساب تلگرامتان را پیدا کنند. البته طبق توضیح تلگرام، کسی که شماره‌تان را از قبل می‌داند و در مخاطبین خود ذخیره کرده است، ممکن است همچنان آن را ببیند.
۲. محدودکردن آخرین بازدید و آنلاین‌بودن
در بخش
Last Seen & Online
، گزینه را روی
My Contacts
یا
Nobody
قرار دهید. بخش استثناها را هم بررسی کنید. توجه کنید که هنگام تایپ‌کردن یا ارسال پیام، ممکن است وضعیت آنلاین شما برای مدت کوتاهی به همان شخص نمایش داده شود.
۳. محدودکردن عکس پروفایل
در
Profile Photos
، نمایش عکس را روی
My Contacts
بگذارید. برای حساب‌های کاری یا عمومی بهتر است از عکسی استفاده کنید که اطلاعاتی مثل محل زندگی، پلاک خودرو، محل کار یا اعضای خانواده را آشکار نکند.
۴. جلوگیری از شناسایی از طریق فوروارد
در بخش
Forwarded Messages
، گزینه را روی
Nobody
قرار دهید. با این تنظیم، وقتی دیگران پیام شما را فوروارد می‌کنند، نام فرستنده به پروفایل شما لینک نمی‌شود.
۵. جلوگیری از اضافه‌شدن به گروه‌های ناشناس
در
Groups & Channels
گزینه را روی
My Contacts
تنظیم کنید. در قسمت استثناها نیز فقط افراد مورداعتماد را قرار دهید تا افراد ناشناس نتوانند شما را مستقیماً وارد گروه یا کانال کنند.
۶. مخفی‌کردن IP در تماس‌ها
در بخش
Calls > Peer-to-Peer
، گزینه را روی
Nobody
بگذارید. در این حالت تماس‌ها از سرورهای تلگرام عبور می‌کنند و IP شما برای طرف مقابل آشکار نمی‌شود؛ ممکن است کیفیت تماس کمی کاهش پیدا کند.
۷. فعال‌کردن رمز دومرحله‌ای
وارد
Two-Step Verification
شوید و یک رمز قوی و متفاوت از رمزهای دیگر انتخاب کنید. ایمیل بازیابی نیز باید رمز قوی و تأیید دومرحله‌ای داشته باشد. با فعال‌کردن این قابلیت، صرفاً داشتن سیم‌کارت یا کد پیامکی برای ورود به حساب کافی نخواهد بود.
۸. بررسی دستگاه‌های متصل
در
Devices
یا
Active Sessions
، همه موبایل‌ها، رایانه‌ها و مرورگرهای متصل را بررسی کنید. هر دستگاه ناشناس یا قدیمی را ببندید؛ در صورت تردید، از گزینه
Terminate All Other Sessions
استفاده کنید.
۹. قفل‌کردن خود برنامه تلگرام
گزینه
Passcode Lock
را فعال کنید و قفل خودکار را روی زمان کوتاه قرار دهید. اثر انگشت یا تشخیص چهره را هم فعال کنید تا در صورت بازبودن قفل گوشی، دیگران نتوانند تلگرام را باز کنند.
۱۰. مدیریت مخاطبین همگام‌شده
اگر نمی‌خواهید فهرست مخاطبین گوشی در تلگرام ذخیره و همگام‌سازی شود،
Sync Contacts
را خاموش و از گزینه
Delete Synced Contacts
استفاده کنید. همچنین می‌توانید
Suggest Frequent Contacts
را غیرفعال کنید.
۱۱. برای گفتگوهای بسیار حساس از Secret Chat استفاده کنید
گفتگوهای عادی تلگرام در فضای ابری ذخیره می‌شوند. برای مطالب حساس از
Secret Chat
استفاده کنید؛ این گفتگوها رمزنگاری سرتاسری، وابستگی به همان دستگاه و امکان حذف خودکار پیام دارند.
۱۲. کد ورود را هرگز برای کسی نفرستید
کد ورود تلگرام، رمز دومرحله‌ای، QR ورود، اطلاعات بانکی و فایل‌های ناشناس را در اختیار کاربران یا ربات‌ها قرار ندهید. تلگرام تأکید می‌کند که با ربات‌ها مانند افراد غریبه رفتار کنید.
برای حریم خصوصی بیشتر، بهتر است نام کاربری تلگرام، عکس پروفایل و نام نمایشی شما با شبکه‌های اجتماعی دیگرتان یکسان نباشد؛ چون حتی با مخفی‌بودن شماره، امکان تطبیق هویت از طریق این اطلاعات وجود دارد.
⭕️
حتما از تلگرام رسمی استفاده کنید و از Google Play یا App Store نصب کنید همچنین اگر تلگرام غیر رسمی دارید حذف کنید.
#حریم_خصوصی
#امنیت
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/alonews/134863" target="_blank">📅 00:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134862">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
گویا پل فلزی بندرعباس رو هم زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/alonews/134862" target="_blank">📅 00:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134861">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-poll">
<h4>📊 به نظرتون چی میشه؟</h4>
<ul>
<li>✓ تهاجم گسترده زمینی و هوایی آمریکا</li>
<li>✓ توافق میشه</li>
</ul>
</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/alonews/134861" target="_blank">📅 00:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134860">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
فارس:
حمله به پل خمیر شش کشته و زخمی داشته
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/alonews/134860" target="_blank">📅 00:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134859">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
برق مناطقی از کیش قطع شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/alonews/134859" target="_blank">📅 00:37 · 26 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
