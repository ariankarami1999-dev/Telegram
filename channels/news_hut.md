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
<img src="https://cdn4.telesco.pe/file/QR1ePsiGx-a3pmKpiBAZi5GXhn55iS2k6AzlIscQ0VJDiQb2HnzNbIy58kmgMKbhI1yLumAOisYkIUNJGGylo6lB-4lOC1V-YJ_8k3rDr5crH4q1ZSfaYJEtEtzILLeNGBHD9794uPZBZKE3_1YBaiVeU6PecCpmEuS4gYEbv0_XWbewkNx4WpjL1S9QQn8SgjI2V2xsjfRMWqqH6HbDMKrJvt-Ld17QT5VkrI0K3V1ep7OkTLrFC4w_GWu_Z74-k62-BsJZI_f8qTXhNcYfvvCF71cWG4mMN1IHVciTjhWYmKIqb8wV_1nYgsAZS2Wqsiyi_rO6_CsD3xrTHsfsKg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 193K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 18:23:08</div>
<hr>

<div class="tg-post" id="msg-67532">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0911dd57d8.mp4?token=KdSBRMk7bTP-uXoR6dxGAC-fnNpVZ3mVgnLJRNuT1rF1R6SZT9d95wH7-WKJPUrfFCsH8tuxZq-qF1iPxNN_l-cpNM5qY7p7pG0pxD9OWbGWCkADjxAh12E8O6d0wMUHKOUL0YBNbUwV-AzwYwyt2si3dwRfaFukqcz_0qacl4XJaI17PTQXWTU3pA8xLRQA4IUYNj2MJJGsSJ9mSCg32Ve7TkpNn60IPcYXJ_2jAJpvpFwOLqws2gLEGdxx2VqRG7oCsK564xpf08lM-IK8OACPNbtPUi6um8RTZISU4FrfW4S5OahT3--anCvsjKq7bwr8BEgd7e2p7LlwvAnc_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0911dd57d8.mp4?token=KdSBRMk7bTP-uXoR6dxGAC-fnNpVZ3mVgnLJRNuT1rF1R6SZT9d95wH7-WKJPUrfFCsH8tuxZq-qF1iPxNN_l-cpNM5qY7p7pG0pxD9OWbGWCkADjxAh12E8O6d0wMUHKOUL0YBNbUwV-AzwYwyt2si3dwRfaFukqcz_0qacl4XJaI17PTQXWTU3pA8xLRQA4IUYNj2MJJGsSJ9mSCg32Ve7TkpNn60IPcYXJ_2jAJpvpFwOLqws2gLEGdxx2VqRG7oCsK564xpf08lM-IK8OACPNbtPUi6um8RTZISU4FrfW4S5OahT3--anCvsjKq7bwr8BEgd7e2p7LlwvAnc_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
وزیر جنگ هگست:   «امشب، اگر نیاز باشد، با دستور شما آقای رئیس‌جمهور، حتی بیشتر و عمیق‌تر حمله خواهیم کرد، زیرا این همان پیامد است.»  @News_Hut</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/news_hut/67532" target="_blank">📅 17:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67531">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db8877d1b1.mp4?token=TNjgr6dqDlyKYTB_om83D-IbuKTfaqY_iq0Havns7nxoXFa8Wr1tnmvNJbD0A4LzMGpVpHYVrVrw65Z8DSYDpq4p9Ek4CqsKEXbnUG1XhApp4buwzAH-7o6vI30u8ZGw870wpFjJqor3pcodabQ8OhhQ_7Bg1vwZLUbsAKGdT81u9blxp9uPNCQ3e3qVVbbuKzjBaEpA4m06rePNPB0oIbzOtmuAISKHTtWhghjPEO54YAwAH6B3tY7zXA4944DvYjDqTiLyj2FWNfMD3GTsJDlnp_Hzzb_OQTtL61CoD6HeXXCsqih8hERoAsEAQUyoeHGhMIOKlzABt6ZhN3v0fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db8877d1b1.mp4?token=TNjgr6dqDlyKYTB_om83D-IbuKTfaqY_iq0Havns7nxoXFa8Wr1tnmvNJbD0A4LzMGpVpHYVrVrw65Z8DSYDpq4p9Ek4CqsKEXbnUG1XhApp4buwzAH-7o6vI30u8ZGw870wpFjJqor3pcodabQ8OhhQ_7Bg1vwZLUbsAKGdT81u9blxp9uPNCQ3e3qVVbbuKzjBaEpA4m06rePNPB0oIbzOtmuAISKHTtWhghjPEO54YAwAH6B3tY7zXA4944DvYjDqTiLyj2FWNfMD3GTsJDlnp_Hzzb_OQTtL61CoD6HeXXCsqih8hERoAsEAQUyoeHGhMIOKlzABt6ZhN3v0fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
وزیر جنگ هگست:
«امشب، اگر نیاز باشد، با دستور شما آقای رئیس‌جمهور، حتی بیشتر و عمیق‌تر حمله خواهیم کرد، زیرا این همان پیامد است.»
@News_Hut</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/news_hut/67531" target="_blank">📅 17:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67530">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووری
؛ ترامپ:
به ایران هشدار میدم، دیشب ضربات سختی رو بهشون زدیم، اما امشب قراره براشون سخت‌تر باشه و حسابی بهشون حمله میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/news_hut/67530" target="_blank">📅 17:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67529">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f1152c373.mp4?token=lKW5l4jx1AeuKijz-6cj-VCMqmUHuAYscW6r6lqfwBtwef-os5NuY7sxX1H0V2R85mxVGAWyh5wvoK6lreu2pdkQiNPX8cTfvbsNJvIkVWcmZqW8QSAfI7pmdfZzVJxLhoMfwdxR3lXDekA6nhw-zcTnqqKeLZhzyrBr7cDCdw9y2gb2wBz1bmL2TsQEwmq1jb1ABY1b99m4vTlOpMIgURyOAPMkTFv9hW_LE6w5YmMI5wxxcdIkYHPo8NWuKSHFNAwSfHBYui0pRR9-xXHXdCu_USqby7lqaGXtaueoF3zW4chk5Pu8VR6QrewLrF6zHmjlmY6NbrKZM5Wn-g0lkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f1152c373.mp4?token=lKW5l4jx1AeuKijz-6cj-VCMqmUHuAYscW6r6lqfwBtwef-os5NuY7sxX1H0V2R85mxVGAWyh5wvoK6lreu2pdkQiNPX8cTfvbsNJvIkVWcmZqW8QSAfI7pmdfZzVJxLhoMfwdxR3lXDekA6nhw-zcTnqqKeLZhzyrBr7cDCdw9y2gb2wBz1bmL2TsQEwmq1jb1ABY1b99m4vTlOpMIgURyOAPMkTFv9hW_LE6w5YmMI5wxxcdIkYHPo8NWuKSHFNAwSfHBYui0pRR9-xXHXdCu_USqby7lqaGXtaueoF3zW4chk5Pu8VR6QrewLrF6zHmjlmY6NbrKZM5Wn-g0lkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
آنها توافق کردند که هرگز سلاح هسته‌ای نخواهند داشت.
و سپس، آنها به بیرون می‌روند و می‌گویند که ما هرگز درباره این موضوع بحث نکردیم.
چه کسی باور خواهد کرد؟
@News_Hut</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/news_hut/67529" target="_blank">📅 17:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67528">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff51c5e950.mp4?token=TcM2Ns-vPHDWzf59zyZQkg-k3RkKEOhqQgBJRw7rg6HC8O1bc4mpuzRxXfGySAQTPQCMWKppCJd59bRi0BxN3-RVlmw7pc9XAdyiycMH99_SRb2jgqcWjAgxLjREnbHoRrDnGC6EAdolizF4tHsnjUfWtkl1OtHF505MAuBX9hxulTn0H70vv_y39fuh-rnCKWeqUb_UDNSx0tgcfMv3SeVY8Lg17WIP9qJ3avR1Jb8SyGe3M3oigGaq7LlsI2IJiPY9yxdJbjfktLcmcED1ihDWfkKb0Ls9WZanTg88c26wxQsQJbiidOwITWFi_3CnVF-RQZg27VABjojVAjhbDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff51c5e950.mp4?token=TcM2Ns-vPHDWzf59zyZQkg-k3RkKEOhqQgBJRw7rg6HC8O1bc4mpuzRxXfGySAQTPQCMWKppCJd59bRi0BxN3-RVlmw7pc9XAdyiycMH99_SRb2jgqcWjAgxLjREnbHoRrDnGC6EAdolizF4tHsnjUfWtkl1OtHF505MAuBX9hxulTn0H70vv_y39fuh-rnCKWeqUb_UDNSx0tgcfMv3SeVY8Lg17WIP9qJ3avR1Jb8SyGe3M3oigGaq7LlsI2IJiPY9yxdJbjfktLcmcED1ihDWfkKb0Ls9WZanTg88c26wxQsQJbiidOwITWFi_3CnVF-RQZg27VABjojVAjhbDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:
جمهوری اسلامی ژاپن دیشب به ناو هواپیمابر ما حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/news_hut/67528" target="_blank">📅 17:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67527">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac18509fa8.mp4?token=bkb90r4fV5VdVjuo3STuAyByiawv3D7OCV7xvISAL7sIHCOAOG7bmdlb7SKEB5nYRF_jg-2lcUSkzhwCany2U0RCn7vF_Pf3TytOiTFIXquFqQ9Qmb6cut_0l-uPC3ekVqsChwZuz4qKCG_fTH7ayUW-VbnZbEXiBpy3HzUCuSRV3qgnRFJRoafZMEFyB4ilnTO1vKsLUaedxuWRKvBicyOsSCyBrFgu6UNh6CJ5MmjqME_nSdAcWst18lCndDqZo3sVAou0B6UlgKD7DAqdyeDgtPoPgZT3YklfELYTTeUa0ctCxH23PIfmblFBDW6IF2sGlXIbVmTRz_0I9JQLxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac18509fa8.mp4?token=bkb90r4fV5VdVjuo3STuAyByiawv3D7OCV7xvISAL7sIHCOAOG7bmdlb7SKEB5nYRF_jg-2lcUSkzhwCany2U0RCn7vF_Pf3TytOiTFIXquFqQ9Qmb6cut_0l-uPC3ekVqsChwZuz4qKCG_fTH7ayUW-VbnZbEXiBpy3HzUCuSRV3qgnRFJRoafZMEFyB4ilnTO1vKsLUaedxuWRKvBicyOsSCyBrFgu6UNh6CJ5MmjqME_nSdAcWst18lCndDqZo3sVAou0B6UlgKD7DAqdyeDgtPoPgZT3YklfELYTTeUa0ctCxH23PIfmblFBDW6IF2sGlXIbVmTRz_0I9JQLxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ممکن است محاصره را دوباره اعمال کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/news_hut/67527" target="_blank">📅 17:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67526">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e08b208584.mp4?token=HzumfN0LveMGWXOf2o05EtURfyICDJRqID2r2ULl3RSOMMwvqCCo5JL62lglmHmKaIbCF5YhcIZjgp8g6E1btS9Y2MJni_tw0CCX8Q-x0sNCFTsLYL9w86IUeeYAk-1v5RxDukIKA_ndd3VJupk_NSRZR2kAhqdYq-62plBdiNcTIUKIA1l_ALEnodlgM4RO5WNJCEy6qgrkgib-aCe8mQgtyXKBP1X7e1SzQVhucwZCEaJL8C07tqipfV1kWE02NJ-XAShuxlO8s48RgY9qCsCPAe_6KZg8X2wcoZH7wc81jj8gbm1LI_IHycac3CBg-u8d2tEMmFvzMrE7CFxDMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e08b208584.mp4?token=HzumfN0LveMGWXOf2o05EtURfyICDJRqID2r2ULl3RSOMMwvqCCo5JL62lglmHmKaIbCF5YhcIZjgp8g6E1btS9Y2MJni_tw0CCX8Q-x0sNCFTsLYL9w86IUeeYAk-1v5RxDukIKA_ndd3VJupk_NSRZR2kAhqdYq-62plBdiNcTIUKIA1l_ALEnodlgM4RO5WNJCEy6qgrkgib-aCe8mQgtyXKBP1X7e1SzQVhucwZCEaJL8C07tqipfV1kWE02NJ-XAShuxlO8s48RgY9qCsCPAe_6KZg8X2wcoZH7wc81jj8gbm1LI_IHycac3CBg-u8d2tEMmFvzMrE7CFxDMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
آنها به ما گفتند: لطفا در مراسم خاکسپاری ما را نکشید. من گفتم که این کار را نخواهم کرد، و ما هیچ اقدامی انجام ندادیم.
و سپس آنها به سه کشتی حمله کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/news_hut/67526" target="_blank">📅 17:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67525">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e9aa8bf24.mp4?token=XBa3-NsSD3_QOH5DBRrAQylCMmAEbob0vAXD4_R8TCYMxe2Sq2FYXrfekWPvwFCbYz2iNNSXeHRa16rOBNE9Mbo4kIuvXPQIRByy7OL9S-Ispgk1OtqyKdkJu5gE_UElqe7BMV4kR8oIfjY7uILrRqEM8aoTJjwbh0TsjponlfOUELgwRUX7TXl8TVyKxJBlRAfnBKoWCcYsRou-Oyvx2QKTTIRoIgFnFr4gj2XkmROI7H0r4kKQBsb2ISYYGVsV-tIM5vhqRZi2m4G7nnrgV08ummTE3KlnuooNNxjlYVOtZUJhW2_rEG29JfpGMo37jssgv2k83fyYSyEviW0-CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e9aa8bf24.mp4?token=XBa3-NsSD3_QOH5DBRrAQylCMmAEbob0vAXD4_R8TCYMxe2Sq2FYXrfekWPvwFCbYz2iNNSXeHRa16rOBNE9Mbo4kIuvXPQIRByy7OL9S-Ispgk1OtqyKdkJu5gE_UElqe7BMV4kR8oIfjY7uILrRqEM8aoTJjwbh0TsjponlfOUELgwRUX7TXl8TVyKxJBlRAfnBKoWCcYsRou-Oyvx2QKTTIRoIgFnFr4gj2XkmROI7H0r4kKQBsb2ISYYGVsV-tIM5vhqRZi2m4G7nnrgV08ummTE3KlnuooNNxjlYVOtZUJhW2_rEG29JfpGMo37jssgv2k83fyYSyEviW0-CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ما شب گذشته به جزیره خارک حمله کردیم.
ممکن است کنترل جزیره خارک را به دست بگیریم. هیچ کاری در این مورد نمی‌توانند انجام دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/news_hut/67525" target="_blank">📅 17:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67524">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/204bddd9b7.mp4?token=C9YkfOZ4dRMfumAG6jORKiv_Mt97v5FHXYwU6OJXtMctbYuZoEJRjXJClmPumAajLlK--vNl0C6G_wGKRfOXm3E4yurqYbHqWcjzdBct_PZ8-slZzWbuIbZjDd0Sem1pBzkF2MpOLvuOztCwdlPqqzxW-D5LGRu2eOekLTQQXF65CU60m84WpTFQ7Jc-jbuHd_cTNW-AJJwdOBmLj6vyNE-du-eQbPAWKZhLaake2yTfZn9QozqCGEJ1KQt-u_60q_32VlqsR0b4cn35YUw00raR4PlgjEN8EHAmyNvU7E0w7qpOSZnBrUr2h_kUyT-HW2j64eYvQ0KgzPGpMIrwiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/204bddd9b7.mp4?token=C9YkfOZ4dRMfumAG6jORKiv_Mt97v5FHXYwU6OJXtMctbYuZoEJRjXJClmPumAajLlK--vNl0C6G_wGKRfOXm3E4yurqYbHqWcjzdBct_PZ8-slZzWbuIbZjDd0Sem1pBzkF2MpOLvuOztCwdlPqqzxW-D5LGRu2eOekLTQQXF65CU60m84WpTFQ7Jc-jbuHd_cTNW-AJJwdOBmLj6vyNE-du-eQbPAWKZhLaake2yTfZn9QozqCGEJ1KQt-u_60q_32VlqsR0b4cn35YUw00raR4PlgjEN8EHAmyNvU7E0w7qpOSZnBrUr2h_kUyT-HW2j64eYvQ0KgzPGpMIrwiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
گزارشگر: آیا امشب قصد دارید قایق‌های بیشتری از ایران را هدف قرار بدید؟
🔴
ترامپ: معمولاً این موضوع را با شما در میان نمی‌گذارم، اما می‌دانید؟ آن‌ها هیچ کاری نمی‌توانند در این مورد انجام دهند، بنابراین احتمالاً بله.
@News_Hut</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/news_hut/67524" target="_blank">📅 17:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67523">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f96f01d100.mp4?token=pCi2oSilWDdanGHNCqTEpZGMYsJslJCzQhi2KuvvrdsiRIpVCxF1yoKX8GoKFYXHD5tF4HmJaStGNBoY_e1_VEt_Y1U8JtAAtZmdHWCZjyor2mxsZd1iDxvoO3u_GH5MgEwAQGvMxYMnzAisG-omTb4VmRY408tQymebK2xFYn83LTZip5MG_LwsUB-jF2AKys90rNbwvNb_uwFlXhbjXHWC7G84rXvR-ClW5XVgChStVS5Muf2H8xUZ-urpih9LKlfiwl4TzbGnIZ5yskVJK6ZylArpDbsfajTIQhgd9Bt9HPjI_waBG4GiruH81ucw0spwihcZRxsqxhwECrSD-A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f96f01d100.mp4?token=pCi2oSilWDdanGHNCqTEpZGMYsJslJCzQhi2KuvvrdsiRIpVCxF1yoKX8GoKFYXHD5tF4HmJaStGNBoY_e1_VEt_Y1U8JtAAtZmdHWCZjyor2mxsZd1iDxvoO3u_GH5MgEwAQGvMxYMnzAisG-omTb4VmRY408tQymebK2xFYn83LTZip5MG_LwsUB-jF2AKys90rNbwvNb_uwFlXhbjXHWC7G84rXvR-ClW5XVgChStVS5Muf2H8xUZ-urpih9LKlfiwl4TzbGnIZ5yskVJK6ZylArpDbsfajTIQhgd9Bt9HPjI_waBG4GiruH81ucw0spwihcZRxsqxhwECrSD-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
انگار یه نسخه پرمیوم از ایران هم وجود داره که فقط مخصوص پولداراست.
@News_Hut</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/67523" target="_blank">📅 17:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67519">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hqmCKBTfBHQxhA0cxFao1BqlMGh_ojZxgSLNjIf5fOH_RjR26wX0napGntfOZI7tJTOeTA2mbHYF2yRJmIHwuR8YjKlDduUV-lgwYhQLP208RCcYDxY3GcDRZEmL-Co2XxSRivro1PgeeDDg538R5mnyfnR3FZ4csYWeeiBdIG5qifTqo6x7EeywLV6-ZDmZQy8bJtpIBobUebIAgJif2G3qBloA6tUO_pZGFijiUCAf8DziKc2c-5nk33yFNZE-WX6EUc3n8afJR9hCiuGTJ_tm_Sxpx3t4KIRdmMXwtjodYf7iSat3d_wIVmsFgD2j31gW6U3armDq5dFHrkaoMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41735c920b.mp4?token=Ho2T5JmrNz8-HZ2VTDT7JFuiwOxeXAK1bzUWJH9Ic-c5UXRhFl9MvhRAWWYEPBysTtGm2kw2EFZHsSAFaAbzG78p71P4aqq36bnQvNa6CXUVVyG5jkWA6Hjn1FroOMK0YvhsrEW0mF-Dp0f_mm0_Bl_1cWxHmqFL6guZs8sB7QAO76UIhqivBBFTl30EMFOROOKQZyOLYWoJnJfudvMWqYfYNfkdfsqpUbwSprHzwI2TZlVYGb8AUka0DsJxcmj1dVo-q9tUnauu1DepQ1h-KA5gU78mmK1eqT9xsM7fqjpuRuecwjwiEJKq6xbFo10bhsAQo8YKKKbssD_mClTHhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41735c920b.mp4?token=Ho2T5JmrNz8-HZ2VTDT7JFuiwOxeXAK1bzUWJH9Ic-c5UXRhFl9MvhRAWWYEPBysTtGm2kw2EFZHsSAFaAbzG78p71P4aqq36bnQvNa6CXUVVyG5jkWA6Hjn1FroOMK0YvhsrEW0mF-Dp0f_mm0_Bl_1cWxHmqFL6guZs8sB7QAO76UIhqivBBFTl30EMFOROOKQZyOLYWoJnJfudvMWqYfYNfkdfsqpUbwSprHzwI2TZlVYGb8AUka0DsJxcmj1dVo-q9tUnauu1DepQ1h-KA5gU78mmK1eqT9xsM7fqjpuRuecwjwiEJKq6xbFo10bhsAQo8YKKKbssD_mClTHhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حملات موشکی شبانه روسیه به اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/67519" target="_blank">📅 16:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67518">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-D2AEHQGhfMJv5TEhcYCU84kypFrb3V-KKRuZ9OxgJh7bjeIgW8Y55-5QdPsY1Sbr2CaP3eSYUgfjNw4GXZfJlUMrnECJ2bBRBAvPagbr7mj2LyI8RbvPNdKQOcwVZQMSErVGFiN1kWnRBM26TU-eFzuIrpcBa0_9greRXMtZBvkp3cFOOxLIpk0qlgVlF5YE9XVHGFOBgTUWUosJss_ZetRpgMJ8gYnybBdwL-P42UKdhzAsZjFQFgeXheCIJzE7pt0QcYVzlqfhcsqQl5_MquXIg5JqzjlA9IJkteqg8AxU7d005VPvE6ysn45ydr55GHB5dUmVojx00YF9wBZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری هادی چوپان
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/67518" target="_blank">📅 15:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67515">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cM46MiW1Cpa4OBR27C9eq5_kHYiqoTqX8l-37VvRTY0XnbAmQSp4bWSE2V5rxgWs9oRUZu1OOkhFfd0qYczEbIXF98A4o95nOMQuoEKUmpuWVksWwzatLtDGfBnoGavm0BJs6h36whSEjTy7KzyEWssFdF9AjW5E6d5zLc3nr42i02StpqvbDvNiU4zjEz5P5NEaHMGxXKH9o5iHHD1528TzmU9kPEAU6BinLnsBimi0nTWN8JMzYe4nn28w2hWl4CFLhbjcL6Ke8I-aGVYP68lHnKifJN72lzILT7rHrS_3vUP5M2cyQCY2jEbrecp_dPihH8_OOcMMIqePUpTjcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OiXJAhHKn2_6vJ5D40PUb67u8D6mYbJWbSKMLZPZ--DTT4eNhfn_jrIa6fMrUvaw2otC70cWVhf0NruDaGURXg9lWjCVSPNtKVj1Xhk88N2RnMcIUNVYbE8UD9JZkZwQ43h0YyY_68rsWfRp4kyGuvnsXsn3XhOWUOk5Qkqnskx6CUTiBH2-yp5_7Ruu6_bxgmqhnXTg6F7eGA-BvZqfLSkDpN2jrla4MJlYZuMbtrL0zLpuWyS3oDYXOGqAs3pQlnFc3fJ8lBB6obzioMQd9RU25GIr6RHdJkoBrAhO2yP_ojLVZCk4aF_dVLthVWwyorggz_9BY3EFlnrcU4-YtA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2e58f00c0.mp4?token=XJW_qDfjJoecw6SWjcxMzXbXzV4xTdgwFVJ4mlAFbwW1gEZ5ZkuronpRbVAIh5wER0wJA3ffXGw5SvF-KKS7kGbSoS4YrJ-EoXdg8cD0O405zze5p26CRAyjImVJUzH-Z5FyNqHnwzz7VjhHuwvpbYuMZIggGTNyZrjLUp-bWtnImk8N8j_h00hQvKr3LWZucttdMUcs8Z4bBLu3k4NohxDb-T6OOpXfrxkvqVC4Vwu3cEJlA0Xo868WVId2su5pxEstNDpGYpYwRyFVVbmea69kO2NDsqKSHIU6l5M9gXJlaCn0XV3S3_X6pbSA0hNxYNSKS31Gg5RraI-sUW8QUYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2e58f00c0.mp4?token=XJW_qDfjJoecw6SWjcxMzXbXzV4xTdgwFVJ4mlAFbwW1gEZ5ZkuronpRbVAIh5wER0wJA3ffXGw5SvF-KKS7kGbSoS4YrJ-EoXdg8cD0O405zze5p26CRAyjImVJUzH-Z5FyNqHnwzz7VjhHuwvpbYuMZIggGTNyZrjLUp-bWtnImk8N8j_h00hQvKr3LWZucttdMUcs8Z4bBLu3k4NohxDb-T6OOpXfrxkvqVC4Vwu3cEJlA0Xo868WVId2su5pxEstNDpGYpYwRyFVVbmea69kO2NDsqKSHIU6l5M9gXJlaCn0XV3S3_X6pbSA0hNxYNSKS31Gg5RraI-sUW8QUYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
با اینکه تو ایران با سنگ و چماق میفتن دنبال عباس و میگن مرگ بر سازشگر ولی تو عراق اینجور نیست!
مردم عراق انقدر عراقچی رو دوست دارن که اون رو تَبرک میدونن و خودشون رو بهش می‌مالن تا حاجت بگیرن!
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/67515" target="_blank">📅 15:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67512">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ngv_fEbwCDexdahvAhlJhjNQELPq2xdyO5Mz02vTJ-tyLJoGIkTcPT0VKKj90Vg2AZgUTUYMsT2XAwjSRC0KHapfkjhs_5y74aQapg3C4sgv0HXg81ofHAElcRU8HDkPzBsZuB9QNGalAbqulUSiQDLWtuXmzjjbm3-21s--ptpP6etLaQszg70gmw5NaqI65MAtLfBS0Wv7fmYUj3KSZoo4FfrpSWqPSkoIAUg5Gd2yrhvbWCJigzyE8elgKpWY9OBvLpwbDSRRp5u3YRwU3oZ4DQz6_nbbF4t5q042I5sXN60tXECE3NxQJMsR80nxws2tqdFuhI2hpgEvhP5sZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M22Fir9cGcTZvvxA177nLA6sg3uaGSIBp7fz3tnZVB4V1xUGtgV-Epn3c60In4Sj0TIXVZZ1Fi3Wj2o5nKJCLcjnuddgzRf_ro-pQXoShin9zPYR2pBzO0Z_t-DebO1hWSSryvTQ8j8hOBzEmvH55zRtumBN2eOzo-TVudt-RlMKvqcopEnkLm6ic0nmkaUSO1GjgvAtb7Jbx_zaghGW5c2U2SbqGr1d3fjPGlBFt-wn_2_bN_xKVWOjjxBwVblCTa5QPZMS8WCwshqMSkJqQZMNR0p7gM6jk6-1cofw3nwro0z9y_Q7VlgYN5VcomIY32jRe5EZ5Oz75WaCgbMhlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rhJAaNaP-BVlk3DTgB6VPNmuBnflVX5ccMWmh2Roi1FRbMCm5_k3tivy22LXAdkpZv5UZbsd2Y_xB5CdCWVWey8bwBHGMN0qPBmbrijw3KUt4idEA3SZi2ncl4ECbLC3L_1LZg5dbLTqygtuy06BqsQvJLSPhaWxamX_JEbMDJPJKnm47Iikxj1kzjZUT8HzITNpXg_fng156xfdG2Z6JWcnG0FReswWguqhqVFSxvgj7ucm5Dic6edFr61SPORmHW-9FEYh1snvw_GYAZ6lSZRnxfrbY5nwXo5lU4YIOd5jCLrtNHM0prsUo5eCGH1ud7EpOkrC35TSEJbWvGBjjA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
خبرگزاری تسنیم اعلام کرد یک پهپاد تهاجمی MQ-9 آمریکا در آسمان بوشهر سرنگون شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67512" target="_blank">📅 14:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67511">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/763cc26dcd.mp4?token=rlfl2xU7ztQVFloTJRBhtsDp6qnsErEJkilYtYf_kOxzs45w0aERx5UxbGGyjuq_Wmhw1Iu1l9zNLvVgj1VLHpDwxi9Y7wo8fzzhwc-7abjJJFN-3EiBheZNHlOU6D3kgFtxK0jnFl2523sVwwYtBpRixi9nGF66BdfF73zl1_6gx3hlPFpGRTmW3gcv2PMAAcQJ-Xubp46QamYfd0HBGpjFX_q_oyYTlG08Zt-XpgXy-axACbUdu8_ZCo4Vm20xxQTvZBSgw9JU4kCEFpJPO_veO2Hv_YRoiLDnl5EoBoYK7VE3E3kCJ4opIMY68QDaU3sTeb0RnkEnSC8J4NO4hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/763cc26dcd.mp4?token=rlfl2xU7ztQVFloTJRBhtsDp6qnsErEJkilYtYf_kOxzs45w0aERx5UxbGGyjuq_Wmhw1Iu1l9zNLvVgj1VLHpDwxi9Y7wo8fzzhwc-7abjJJFN-3EiBheZNHlOU6D3kgFtxK0jnFl2523sVwwYtBpRixi9nGF66BdfF73zl1_6gx3hlPFpGRTmW3gcv2PMAAcQJ-Xubp46QamYfd0HBGpjFX_q_oyYTlG08Zt-XpgXy-axACbUdu8_ZCo4Vm20xxQTvZBSgw9JU4kCEFpJPO_veO2Hv_YRoiLDnl5EoBoYK7VE3E3kCJ4opIMY68QDaU3sTeb0RnkEnSC8J4NO4hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
احمدی نژاد : بابا داره بهتون فحش میده،یه مرد بین شما پیدا نمیشه پاشه حداقل بگه خودتی؟!
+ترامپ امروز به مسئولین جمهوری اسلامی گفت آشغال،پست فطرت،کثیف،تومور سرطانی، شرور،بی‌ کفایت،بی ارزش،بیمار،روانی و حقه باز
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67511" target="_blank">📅 13:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67510">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
رسانه های عبری:
ارتش اسرائیل جلسه‌ای با فرماندهی مرکزی آمریکا برگزار کرد، به منظور آمادگی برای از سرگیری جنگ.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67510" target="_blank">📅 13:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67509">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RzvkGyNOk13GwGjCDTQ7zpef8sTQ2vkgpcVLdoE44urFh80d03t9iiLK7VxilkaX6jG66gDU2M2POht1RAciiJjQfa0RvRRFdCd0ccpe0Y9RRsVLmtX4TczOMixnNHc0KmFu8hRaduUY3ACRJdY2RVn8dPU6-Xn2JqFecqwydjIlNO6uHsCVxcvM-5kgURhU1abXIig51glQa533KjJBP1P_sPRe8x2hct_bDt2KKX__FY8XPHz38h6ccE7mtHXNz49hAinW6wqPKkqaKSASAshEViKkN-xh5aj4CDAwi00XwtJff0cC6YxbouKHIQXlVhTC0blimr7AvId3wPBcyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
پزشکیان:
رفتار دولت ایالات متحده به عنوان میزبان جام جهانی، همان سیاست خارجی همیشگی آن را نشان می‌دهد: زیر پا گذاشتن قوانین، زورگویی در برابر رقبا، ایجاد موانع و تقلب. این همان روشی است که آن‌ها دنبال می‌کنند. ایران چنین بازی‌هایی را رد می‌کند. ما به طور قاطع از حقوق خود دفاع می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67509" target="_blank">📅 12:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67508">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W876kx4GOMDXgCwzk6_Q-_IeqbQlq4ducddxlr2zSLwQY7odj6RBwTyYeGLE2ndfk3sNi8XOrHl9DrWeCN9bqTvq0nCG2uPWNuhzK7ZrRkj4qmLITgnCA8oqRx3bF5rRiJluI4d9wcDpvyM9AHXrWP64wUy8XUczoKNAno_dK88aMIIim9fEdDm1vTQkeCjNR7-T8G9VghnObsc5z9js55FkEZHSIYDzY0cteiT3hhKfqkhXZT51KUIXl5VXsAkzljhBDs33z4jz9t6quY6gjw5AkQE0cndSSZYlbWZhasdEXTucqdTH1nx8cA1ErKj0bastd1Y0iMnxnDkjNK6xRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آمیت سگال:
پیت هگست، سفر برنامه ریزی شده خود به اسرائیل را لغو کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67508" target="_blank">📅 12:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67507">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:
«ما دیشب به آن افراد بسیار خطرناکِ وابسته به ایران، با قدرتی بسیار زیاد حمله کردیم... یک مشکلی در آن‌ها هست. ما می‌گوییم: "بروید مراسم عزاداری‌تان را برگزار کنید"، اما آن‌ها به‌جای این کار، دیروز شروع کردند به شلیک موشک به سمت کشتی‌ها. بنابراین دیشب خیلی سخت به آن‌ها ضربه زدیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67507" target="_blank">📅 12:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67506">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb70977fa5.mp4?token=MrDY4ewXPWYQAu-Afk4k0oMibAYq_59VQdrIi_9Eh8aT-fC-sPOFw0QwAfZVttV67S-2xc2vijJkBZbHRRrSm1R6j90KWOdR1h_1H26EqIQWhc0lmPzWgYgHahTU4PFRg_tkjU1nh58a8Y7ZWzmrpGikeNtzJJUWgpkhkuTFqZHpIZMhh5F4Fft5vRK4Yq6e9mVcq_3xAJdo79ZfCP9-vrsfM1-XQ8bk4qQLJHE3VqStFyqs3SEjSVkh6qv5AdGEhbJSlgF8aTiinEbcf1S4HJskAtWZoy7BH6fr0pmpUcbHZLn3O8jz9jwzaIF4keyrnjDaGjr_bG9WaFw69ZULCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb70977fa5.mp4?token=MrDY4ewXPWYQAu-Afk4k0oMibAYq_59VQdrIi_9Eh8aT-fC-sPOFw0QwAfZVttV67S-2xc2vijJkBZbHRRrSm1R6j90KWOdR1h_1H26EqIQWhc0lmPzWgYgHahTU4PFRg_tkjU1nh58a8Y7ZWzmrpGikeNtzJJUWgpkhkuTFqZHpIZMhh5F4Fft5vRK4Yq6e9mVcq_3xAJdo79ZfCP9-vrsfM1-XQ8bk4qQLJHE3VqStFyqs3SEjSVkh6qv5AdGEhbJSlgF8aTiinEbcf1S4HJskAtWZoy7BH6fr0pmpUcbHZLn3O8jz9jwzaIF4keyrnjDaGjr_bG9WaFw69ZULCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره مقامات جمهوری اسلامی:
آنها دروغگو هستند. ما یک توافق می‌ کنیم. همه موافق هستند. هیچ سلاح هسته‌ای. ما یک توافق می‌ کنیم.
آنها به بیرون می‌ روند، با رسانه‌ها صحبت می‌ کنند و می‌ گویند که ما حتی درباره این موضوع صحبت نکرده‌ایم.
مشکلی در وجودشان وجود دارد. آنها دیوانه هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67506" target="_blank">📅 12:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67505">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5877eb817c.mp4?token=e41zJoQ_-Gpvu6Se9GbZmAmiT4qx24_DhQbsLYPKm_LjOW_QGwoRVwlHBHnrJRXTaI1z7SF24Z6qiFZzHFmC4i_DxXBFs_EDOuaaFVfJNo7e0UeHXS995tw78BN_XWA-DYonFIdBuEqU3eUg6ZeYGlwBKq0eOiUGGKkncXh0r2m0GNEcK8CzKFCSeXQEUE3-RJsMUK7cxrFkXm_OeMS1Q2JL26auvlNejpkRYqwVp7RE3q5_3DzLUdl2_3WfRUuAw2zzy315GYVWFazCKRIrQSd6o9jfMo_iGQ_THu33BXz7jSNRpeTUxAGgOd98xaHB4Znj7VSUUyXKq6UKPHg77w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5877eb817c.mp4?token=e41zJoQ_-Gpvu6Se9GbZmAmiT4qx24_DhQbsLYPKm_LjOW_QGwoRVwlHBHnrJRXTaI1z7SF24Z6qiFZzHFmC4i_DxXBFs_EDOuaaFVfJNo7e0UeHXS995tw78BN_XWA-DYonFIdBuEqU3eUg6ZeYGlwBKq0eOiUGGKkncXh0r2m0GNEcK8CzKFCSeXQEUE3-RJsMUK7cxrFkXm_OeMS1Q2JL26auvlNejpkRYqwVp7RE3q5_3DzLUdl2_3WfRUuAw2zzy315GYVWFazCKRIrQSd6o9jfMo_iGQ_THu33BXz7jSNRpeTUxAGgOd98xaHB4Znj7VSUUyXKq6UKPHg77w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:
به نظر من، ایرانی‌ها ناکارآمد هستند.
اگر کارآمد بودند، ۴۷ سال پیش یک توافق انجام می‌دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67505" target="_blank">📅 12:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67504">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48d7e6a047.mp4?token=WGYpBWyU0ZSBAg1b-G3UB55SaYUXA-Pu_908dwmP5W6b2_ydYCM1MXMZK084ksQvo1UR_FzKQg4CCnk4Ipc2mYQQVpZadUh_0nvxHqq-AfinSxpBgyI72uV6EESIfHnN6mgGz1pm8Y4PeblshWLfgQR75ZTN6_uMTE5wrCb8DrcHw-p2CtIUAVXkBF00DtQNvfeVCO2_0NEytFyyyyq84d5PBFexZCmRBflyNH2W-ZpPc_3MSXoW0p91IRZpCv-Ql3SDO42A4t-E4sYWZNs36W8Z_ZMslgIzpbKIE5Zaop3oiWP_IBCpTQnnjEHb96_MVGsNN2SwokGlXkkc3xAFfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48d7e6a047.mp4?token=WGYpBWyU0ZSBAg1b-G3UB55SaYUXA-Pu_908dwmP5W6b2_ydYCM1MXMZK084ksQvo1UR_FzKQg4CCnk4Ipc2mYQQVpZadUh_0nvxHqq-AfinSxpBgyI72uV6EESIfHnN6mgGz1pm8Y4PeblshWLfgQR75ZTN6_uMTE5wrCb8DrcHw-p2CtIUAVXkBF00DtQNvfeVCO2_0NEytFyyyyq84d5PBFexZCmRBflyNH2W-ZpPc_3MSXoW0p91IRZpCv-Ql3SDO42A4t-E4sYWZNs36W8Z_ZMslgIzpbKIE5Zaop3oiWP_IBCpTQnnjEHb96_MVGsNN2SwokGlXkkc3xAFfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ درباره ایران:
من در تمام لیست‌های آن‌ها قرار دارم. و تا به حال، فکر می‌کنم کمی خوش‌شانس بوده‌ام، اما شاید این خوش‌شانسی برای مدت زیادی ادامه نیابد.
چون این‌گونه است که مسائل پیش می‌روند، اما ما افراد بسیار خوبی داریم.
اما این‌ها افراد شرور و بیمار هستند، و ما باید از شر این "سرطان" خلاص شویم. این "سرطان". و شما می‌دانید چه باید کرد؟ باید "سرطان" را در مراحل اولیه از بین برد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67504" target="_blank">📅 12:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67503">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ در پاسخ به سوال یک خبرنگار پیرامون این موضوع که آیا آتش‌بس و توافهم موقت تمام شده یا نه، پاسخ داد:  فکر می‌کنم تمام شده، دیگر نمی‌خواهم با آنها سر و کار داشته باشم، آن‌ها پَست و بیمار هستند، رهبری‌شان دست آدم‌های بیمار است و اگر سلاح هسته‌ای داشته…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67503" target="_blank">📅 12:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67502">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/385c5453ef.mp4?token=Dtk_tkoRGZf3J1g5T6_MOpspH7IZU03O3m5Hhh72kXzAVC7mLRC1tMKlKKHzOsDjUgZlrziifHuncNa8nzkTIj55Y5Jg2HY5dw318yQYT34bpsS2oGditAzH1W3npwOzzuDstBWyDg04Gx8BDu4wuHzmFHPXBzsETFyM3exMtc-yoM-kWUbUGiKKN3I6_ib7CTSlyEVRCVufNFB_mX3n-NOtyoi4oyP3IVmd5d2CxXgUdiv4FJHhS8xr7ZN_BTc25WoywIDUALy0FkD3u86vXyv36m9c9wm_UteUq3l1I3JS6NIV9A9XeOC-ftRFSxojbbA9Yt1tfVRTxNcQ-hjdS4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/385c5453ef.mp4?token=Dtk_tkoRGZf3J1g5T6_MOpspH7IZU03O3m5Hhh72kXzAVC7mLRC1tMKlKKHzOsDjUgZlrziifHuncNa8nzkTIj55Y5Jg2HY5dw318yQYT34bpsS2oGditAzH1W3npwOzzuDstBWyDg04Gx8BDu4wuHzmFHPXBzsETFyM3exMtc-yoM-kWUbUGiKKN3I6_ib7CTSlyEVRCVufNFB_mX3n-NOtyoi4oyP3IVmd5d2CxXgUdiv4FJHhS8xr7ZN_BTc25WoywIDUALy0FkD3u86vXyv36m9c9wm_UteUq3l1I3JS6NIV9A9XeOC-ftRFSxojbbA9Yt1tfVRTxNcQ-hjdS4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ در پاسخ به سوال یک خبرنگار پیرامون این موضوع که آیا آتش‌بس و توافهم موقت تمام شده یا نه، پاسخ داد:
فکر می‌کنم تمام شده، دیگر نمی‌خواهم با آنها سر و کار داشته باشم، آن‌ها پَست و بیمار هستند، رهبری‌شان دست آدم‌های بیمار است و اگر سلاح هسته‌ای داشته باشند از آن استفاده خواهند کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67502" target="_blank">📅 12:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67501">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ssJkR_uO4zMzY31aKIvhac1yKp-1s7BqoEL5SCB-e0XZlydkSEbEhJvr8-lKK6wW1GAE2wV5ungcibjYUY9U764OJ2x1msKOEVzwlMwaj-KSuh999JG7QhIbR9OLfltXgymxc4fQr6gmMdhsB9LWMPhh5azk8KCVosrF8sxeeVFbdtzOXGWZPZeedyYX0lOUWdUUoVIiR_VINQF4ugur4AU_-th1UxyV82KgsBkutF1ieD5f7bNOIihBCnVynvBP1U9IHIEA1AD3ZSX3Skl0MRCPQl4WCku6LsRdy6CWqqJSJnMZWd2xTUyE2lCAqiEst_q8gkkXw_bA6FAZdKWviw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بعد از حرف‌های ترامپ، قیمت نفت ۵ درصد افزایش پیدا کرد و به بشکه‌ای ۷۷.۴۰ دلار رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67501" target="_blank">📅 12:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67500">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b7bb2fcec.mp4?token=ulmW7dq0FbdaqSgDEFbHIyScY9KFqY1OfSJt6KotIZtaBNBB5qB6Irb7B_hOU2vfrvabDddExh_6nDwjcpF_2yuVznhg1fP8XOllh9HAUbSsJcNuc5DcvqfNvR0fP6Y3VnI6pIl3Xj4KffVhCkCdapvoNLjWjG2Ee5Q0nxsgiKAiiTlIkszg0-a9g08wfaLgjj8XEeBj76tT19NQ6WU9OG47Lt_t9JkD0g1OnlftlGX3ca3AkEb7z_DrnKSb55s9ZpBpFpkIK6iJr_J7Y_t3U_FPTBu_BnU525RF_7685FSA32Y8TqSuynUgDWFBVCdXziJCTkUHH7tBQyKVeTNCtix3wvMaGbdE5iSnbgJAwX6DU2tWluwQxAc46qR_OrUlBNchxte98zPYOYC63FWNwT6orJSlNTkTBhNYLqZf-glrv-RiMlYSIaZiVqgYwBRY6qHxsHXsnqjDqdRkJA52SdEefBZ_CErqDrf1KzcPY1ltj-R5FJYqhZWGQyB_LlABe72Y54pnWg6bB7hJgrPMnIRvKByu0Ec1ZCyaPnc5CPnBpP3_--Och-3Ua_ljrF3_CaEIuvIsCW5-C0qwJh_5wdPFQtImg1DicC4ZMJw6DnTiAuljOWXsBj8KWkQp7wdZvH9DVoMTMUhC7hEb2Bf1sgo0UTBwyY7tuywW09s9gjo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b7bb2fcec.mp4?token=ulmW7dq0FbdaqSgDEFbHIyScY9KFqY1OfSJt6KotIZtaBNBB5qB6Irb7B_hOU2vfrvabDddExh_6nDwjcpF_2yuVznhg1fP8XOllh9HAUbSsJcNuc5DcvqfNvR0fP6Y3VnI6pIl3Xj4KffVhCkCdapvoNLjWjG2Ee5Q0nxsgiKAiiTlIkszg0-a9g08wfaLgjj8XEeBj76tT19NQ6WU9OG47Lt_t9JkD0g1OnlftlGX3ca3AkEb7z_DrnKSb55s9ZpBpFpkIK6iJr_J7Y_t3U_FPTBu_BnU525RF_7685FSA32Y8TqSuynUgDWFBVCdXziJCTkUHH7tBQyKVeTNCtix3wvMaGbdE5iSnbgJAwX6DU2tWluwQxAc46qR_OrUlBNchxte98zPYOYC63FWNwT6orJSlNTkTBhNYLqZf-glrv-RiMlYSIaZiVqgYwBRY6qHxsHXsnqjDqdRkJA52SdEefBZ_CErqDrf1KzcPY1ltj-R5FJYqhZWGQyB_LlABe72Y54pnWg6bB7hJgrPMnIRvKByu0Ec1ZCyaPnc5CPnBpP3_--Och-3Ua_ljrF3_CaEIuvIsCW5-C0qwJh_5wdPFQtImg1DicC4ZMJw6DnTiAuljOWXsBj8KWkQp7wdZvH9DVoMTMUhC7hEb2Bf1sgo0UTBwyY7tuywW09s9gjo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره رهبران ایران :
«آن‌ها دروغ‌گو، متقلب و بیمار هستند. به مردم خودشان آسیب زده‌اند. تا امروز ۵۴ هزار نفر از معترضان را کشته‌اند.
می‌دانید بعضی‌ها می‌پرسند چرا مردم حکومت را سرنگون نمی‌کنند؟ چون دیگر زنده نیستند؛ آن‌ها را کشته‌اند.
مردم سلاحی ندارند، اما طرف مقابل مسلسل دارد و آن‌ها را به گلوله می‌بندد. رسانه‌ها هم این را پوشش نمی‌دهند.
اگر مذاکره‌کنندگان فوق‌العاده ما بخواهند، بگذارید به گفت‌وگو ادامه دهند؛ اما من امیدی به نتیجه نمی‌بینم.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67500" target="_blank">📅 12:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67499">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ :
سران ایران یه مشت آدم کثیفن. اصلاً ازشون خوشم نمیاد. کلی وقتمون رو باهاشون هدر دادیم. بی‌عرضه و ناتوانن. بهتره فقط کار خودمون رو انجام بدیم.
اونا می‌خوان رهبر آمریکا، یعنی من رو ترور کنن. سال‌هاست که من نفر اول لیستشونم.
باید سرطان رو از همون اول ریشه‌کن کرد. من این‌طوری به قضیه نگاه می‌کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67499" target="_blank">📅 11:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67498">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ :
من دیگر نمی‌خواهم با ایران سروکار داشته باشم. افرادی بیمار بر آن حکومت می‌کنند و از نظر من، این پرونده دیگر تمام شده است.
«از نظر من، تفاهم‌نامه تمام شده است. دیگر نمی‌خواهم با آنها معامله کنم. و اگر سلاح هسته‌ای دارند... دروغگو هستند... به نظر من، ادامه مذاکره با آنها اتلاف وقت است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67498" target="_blank">📅 11:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67497">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ایرانی‌ها رهبران آمریکایی، از جمله خود من را هدف قرار دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67497" target="_blank">📅 11:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67496">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
🚨
پرزیدنت ترامپ:
این‌ها گروهی از بدترین افراد هستند، من آن‌ها را دوست ندارم. ما وقت زیادی را با آن‌ها تلف کردیم. آن‌ها اصلاً نمی‌دانند چه می‌کنند.
آن‌ها مثل سرطان هستند و باید این تومور را هرچه از بین برد. این احساسی است که امروز دارم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67496" target="_blank">📅 11:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67495">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
قرارگاه خاتم الانبیا:
هر نهادی یا مکانی که برای حمایت از ارتش آمریکا علیه جمهوری اسلامی ایران مورد استفاده قرار گیرد، هدف مشروع نیروهای مسلح تلقی خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67495" target="_blank">📅 11:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67494">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ea62c3daa.mp4?token=H36gZTv84LUAW1cbpAwVo8rK2a3QFtj5_hTj4zcpz0V_-JNF9DGcfDoI3dw68xTGj5VTeg6uG2uCreEGjUALAzdpnCtZSnfh1qCzwFKNCxM0n9nda1Tgx5UXmzC7Q_3H9xESyIRT7jHwM_Tcu9Wod7d8NhsntyVzrbUhbAQUOyhIZeVIQ3A2FeRIxnvFsT2cyd9zrCpBecucou5Y1CHGLC4DneTh8aO7zrHp0LCyEWFLyMma4_fAgXs1tmJg1MLy2wrNoKy9H1XM94KRbyyEZABkRAAZkLWWWI_VoYmjzbkmEc-vrOtD60OMcDuq6meEDmJC6lO9netR9p0OBl5gBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ea62c3daa.mp4?token=H36gZTv84LUAW1cbpAwVo8rK2a3QFtj5_hTj4zcpz0V_-JNF9DGcfDoI3dw68xTGj5VTeg6uG2uCreEGjUALAzdpnCtZSnfh1qCzwFKNCxM0n9nda1Tgx5UXmzC7Q_3H9xESyIRT7jHwM_Tcu9Wod7d8NhsntyVzrbUhbAQUOyhIZeVIQ3A2FeRIxnvFsT2cyd9zrCpBecucou5Y1CHGLC4DneTh8aO7zrHp0LCyEWFLyMma4_fAgXs1tmJg1MLy2wrNoKy9H1XM94KRbyyEZABkRAAZkLWWWI_VoYmjzbkmEc-vrOtD60OMcDuq6meEDmJC6lO9netR9p0OBl5gBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
محسن رضایی:
مخالفان مذاکره صبر کنند، خود آمریکایی ها آن را از بین می‌برند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67494" target="_blank">📅 11:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67493">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌های غیررسمی از شنیده شدن صدای انفجار در بوشهر  @News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67493" target="_blank">📅 10:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67492">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6356a25b5d.mp4?token=qsW-BRLeSwUnDVMETgGBnuiI7NBEX45u2e76eNMlXnMrEZfcm_DUOvAmvXvCi2rttqXfP-LABBOA1Guk6Vg-28Jit5SHcALLE28HgTAEjJrdpU5QWWnBKt1Xgr_D6eU1YzRqfRQDbyPFO-qun9Mr2Jad5gtd7_fQ3EEfm15Gi9-jq01t1SlQD7bEGOSYv8BZ-KkVjrD7tbCjvVVECemJDX5am7pU5yUHgVuZ5tyK_RVVpCDpvMpg-Js1Xh9QO7WbCCuISf52kFz0P6b-I6RLQc5zEtMqOGZ5zO-CTNKu8lXJhainh5jOKl_A43VciR2jF3ZmyDzEnGIX2DJyXT5ayQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6356a25b5d.mp4?token=qsW-BRLeSwUnDVMETgGBnuiI7NBEX45u2e76eNMlXnMrEZfcm_DUOvAmvXvCi2rttqXfP-LABBOA1Guk6Vg-28Jit5SHcALLE28HgTAEjJrdpU5QWWnBKt1Xgr_D6eU1YzRqfRQDbyPFO-qun9Mr2Jad5gtd7_fQ3EEfm15Gi9-jq01t1SlQD7bEGOSYv8BZ-KkVjrD7tbCjvVVECemJDX5am7pU5yUHgVuZ5tyK_RVVpCDpvMpg-Js1Xh9QO7WbCCuISf52kFz0P6b-I6RLQc5zEtMqOGZ5zO-CTNKu8lXJhainh5jOKl_A43VciR2jF3ZmyDzEnGIX2DJyXT5ayQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
مستند حملات امریکا به جنوب ایران
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67492" target="_blank">📅 10:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67491">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
شنیده شدن صدای انفجار به سمت پایگاه هوایی عیسی در منطقه صغیر در بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67491" target="_blank">📅 10:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67490">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rpUeAY-GG0m-xCPyOHkK-YCHb5shBYbifyBlrgEa8gB3sIgsy98jWs380rXk6-2sPXPEtmePQOJtU12QPmIkIQYMkDN0Y_QThsBv5v5TPQDHN2g2QVRmpRteFtyYE4uREVUnYJST8NS73chbzFKFSIdWfx53qES0gDIYMTXzgNS-eeADkQM8lSBFuIixxgoy14LC7ES3E8m8eTMOsPt_JC7qQzLW6nRwOIaCi6BCccUDwOjaw2CIObdWdqVgRO_tOsob6pg-P4BPP4D1DZsbY_xSwBD5ryytJUQeyOjTNIeqa_kfu1BQNgAbdubPlK-Gh0EiCNXsu2Cftef5a2sBoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قالیباف؛نقض‌های عمده تفاهم‌نامه توسط آمریکا:
نقض ترتیبات ایران در تنگه
تهدیدهای مداوم به حملات بیشتر
بازگرداندن تحریم‌های نفتی
حملات به جنوب ایران تداوم
تجاوزات صهیونیستی علیه لبنان
دوران زورگویی و باج‌خواهی به سر آمده است. این مسیر به جایی نمی‌رسد. ما تسلیم نمی‌شویم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67490" target="_blank">📅 10:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67489">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hfVGCm_lTIoGiNdPIq5-NbsLr0RnoXCiBxSfGevdIljW0Vn1w4E3pZ1jCCUAhe2jOLCx2F9kgGM8egxJUPgnRCupgAECS32Rs4KuGU_hG0kw5kSuGxSkEQjf4PoDGGw3M1EnicMgKPV-iYbcwKsoy5315hmr8jCuoYK5WrcUsHDT-kLQO3QSQ8uLHqHMwDUvQWeP7uAH_04sEUPvlsFbxrZKPlx4Z1CuHdQ8x2LTOI40baCM8M1wkH5hVU9LUMIp1vGXHODnuDFSgTGQDU5At8AXTZiqdsiBs0PG2tbvZscumsZVb8Fi4gO7X02_gQ64_R-K9VQX2Wu8QK5IywZIyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
یک هواپیمای آمریکایی مدل P-8A Poseidon که در حملات علیه ایران شرکت داشت، امروز صبح نتوانست در پایگاه هوایی خود (پایگاه عیسی در بحرین) فرود بیاید، زیرا این پایگاه مورد هدف قرار گرفته بود. در عوض، این هواپیما در پایگاه آمریکایی واقع در عربستان سعودی فرود آمد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67489" target="_blank">📅 10:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67488">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای انفجار در بندر عباس
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67488" target="_blank">📅 09:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67487">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌های غیررسمی از شنیده شدن صدای انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67487" target="_blank">📅 09:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67486">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9920364084.mp4?token=OgmJ-FL0h2t_TOd4DwE4YvZupbbC9gt0-a4nv4XHuW3QmPcdowRrb1Nqk5pMFlEYcG9WBlh51ZlDzpm9Jf7Uy3MgXxhiw7j9o2A_uTbycRGNzxr6bmKrY_o2pZRCT0C823sr-FKzjMwLkjredgKvR7QB1d1FpKxD3bPLctnOVOYKXI8pBVhjqrw_4fkbVA-7f4kK2-7Gp4YZ7ILWdZjcm1LdUqnhp6-B0h60c9LRp6QRNxlSWm8Wy5Zq0MrmDpIm-XCom7ezNcqcaxfRxLfWXKnKT6QApuUIVE1-zf2zWxtVvbbUUDkpxwCHPxuFtVKo9Zrdf6SmXe4CZuDD0vUAaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9920364084.mp4?token=OgmJ-FL0h2t_TOd4DwE4YvZupbbC9gt0-a4nv4XHuW3QmPcdowRrb1Nqk5pMFlEYcG9WBlh51ZlDzpm9Jf7Uy3MgXxhiw7j9o2A_uTbycRGNzxr6bmKrY_o2pZRCT0C823sr-FKzjMwLkjredgKvR7QB1d1FpKxD3bPLctnOVOYKXI8pBVhjqrw_4fkbVA-7f4kK2-7Gp4YZ7ILWdZjcm1LdUqnhp6-B0h60c9LRp6QRNxlSWm8Wy5Zq0MrmDpIm-XCom7ezNcqcaxfRxLfWXKnKT6QApuUIVE1-zf2zWxtVvbbUUDkpxwCHPxuFtVKo9Zrdf6SmXe4CZuDD0vUAaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عرزشی‌ها خطاب به سعید جلیلی:
نزاری به مجتبی خامنه‌ای جام زهر بدنا؛ ما امیدمون به شماست.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67486" target="_blank">📅 09:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67485">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HuAGDm8YyT1C6nUlXK1GyZUHH9jjFolL4teRb-LzgPtAMDwL4gi-kWJ67cQGXDV6Mv9-8tD095TWqjPcg0BXljF3lEtMWavf-9gBBbSUhFN_AVOI06yptEZI_PD0DQB3wf4TwMfmdwYhqYp8AebFkx8TB3V9CdWipCn8si7QmPKpHJsMw8zYPlaEZl052FhLWh2-HXypvZthps6tHBZguGVvT7uflPoKjBf-R4iqdEekjVaR7XXMhLyuLIVroeMbmkhd8G-kXUXoCBTxFXZqgXGsLGWZ1OYOz2ETJQsdFVU5A7BUsloi1tywBQfhTmuHRMAQP2KTxV9uiCXXyR_ieg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
بیانیه وزارت امور خارجه ایران در مورد نقض آشکار ماده ۱۰ از یادداشت تفاهم اسلام‌آباد توسط ایالات متحده:
کمتر از بیست روز پس از امضای یادداشت تفاهم اسلام‌آباد، اعلام لغو مجوز عمومی صادر شده در ۲۱ ژوئن، نشانه‌ای دیگر از سوءنیت، بی‌ثباتی و عدم اعتمادپذیری ایالات متحده است. این در حالی است که ایالات متحده، در طول بیست روز گذشته، بارها و به طرق مختلف، چه به صورت مستقیم و چه از طریق اقدامات رژیم صهیونیستی علیه لبنان، به مفاد مختلف یادداشت تفاهم، نقض کرده است.
از زمان امضای یادداشت تفاهم در ۱۸ ژوئن، جمهوری اسلامی ایران با حسن نیت و تمام توان خود، برای ایفای تعهدات خود بر اساس این یادداشت تلاش کرده است. با این حال، دولت آمریکا، همانند روال معمول، همزمان با نقض تعهدات خود، سعی در توجیه این اقدامات با بهانه‌های واهی داشته است.
وزارت امور خارجه جمهوری اسلامی ایران، ضمن هشدار در مورد عواقب نقض توافق توسط آمریکا، اعلام کرد که هر اقدامی را که لازم بداند برای حفظ منافع و امنیت ملی خود، انجام خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67485" target="_blank">📅 09:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67484">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67484" target="_blank">📅 03:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67483">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KX0zEu9lw51s9rE_g2fL-JwuzigLyV_dM6cwMPevvFiBXj9Sh-rAdPHCow3t04KfakHhWm77OpD7i9VOFeJysEYPSQrftQDEXUeW7u4eKy1cdUzmzPdhsQAhw65p7eUe8HLc_1xjmMELgU3SPQIRYwB964-7aZiRivbNNunKiFeEkiTHgm83eUSqw3kaz7-Yj0eQzP9_Df83nrb8UhTQrLD6kF0RbeTezvrIyFB96PFv-Ea1fDHEPYevZCRFH084InP8cpNtScKlp5O_I_6B2iIQaaKQXFvTIJcfFLdPk5CMT4D6PI_O7eCmFbZrn8uDjt6K_YIHOhA4uZja7wB6Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67483" target="_blank">📅 03:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67482">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-AiIJNC8zTScWEphCt-2okf6gGI8P2reKonAr_fVrGvh7KNxHQRX6L6fNSwI7-yqCCRagsq7oLCUma6MTaUf08FZZRmS-UoxZ_rtULkPwPJB_MMzkm0yWhfAZuEN4ILxfv9A1moDe3v7y6rgRjqUPc8yVm8ycBy38cPaq0EfFtogv5kH1AHRLHNF_cj0bTih_kjogTvOUmyPumRK8vdxlg2kdJomqrXlUBTz2dFMHFgEbN_WpiOQ6UDq-G_ojaZgiNWEs3X7G4sXVzMjgX3FyCokGGLWQG73QAoYnU1KVuFTpiUQEvpZk7aoVVLsyTkcphuTsiVtfH7GdkEANY-4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به پسرا فحش میدی واسه دخترا کنشی و واکنشی تحلیل میکنی
😒</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67482" target="_blank">📅 02:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67481">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LjfhU8CyG4eGdTVQ3-gBa5GPzQqg9s60sw4Gp7J2ucR5hBkJijOpEXxMPD4M134Iub927mt-zPjq8R89UDTq4eZDD6r4dSlbdepFYzhGctt9IaiclJWaD19XyD7zFtFiBQn5Sycg6nWRdl-TwVHy_9LRg_0iAkc8b6AnzlxajFTuoDFmevnyqFJNUP09lkBgxw_bNRvdvZPcnen4t6jW51qhmcb0OJ12bKmqMJgWpb7JInkCL4k9byNvDmu6Vccdb8bAL9oai2V0p7g7R1nbtB5XL1wiKccFtpcS8givSg4-E1z_YvmFfVDToFskPf7PBqVALvie6_fkKAGQfHdNxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
صداوسیما: وضعیت بندرعباس کاملا نرماله  @News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67481" target="_blank">📅 02:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67480">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">بنظر من زود تموم می‌شه</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67480" target="_blank">📅 02:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67479">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSor60</strong></div>
<div class="tg-text">به پسرا فحش میدی
واسه دخترا کنشی و واکنشی تحلیل میکنی
😒</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67479" target="_blank">📅 02:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67478">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VqGf9xxG5sYa2NR0RcDM0S5rkjtFoW-1O3RZXPsJF76oneQkQpgsxASKrfRSxR5yKPt4apsFrM_bumcJ1iOCGrEHCXkdaC-9hEAIBxdC6CHz3ybqGDbYPkakD4URp1JoYjp44XHjpb-g7H442pdPg5cSIjK5k7BUbP1DKY4mdY_MBJqLDYHElgWoUcwA3oKWaLc2yyPQgGOjhkBbxpZ84IfzJG1Da8SYOFF8MSNTAj_ISajXOPOZ9IdlC_q5GnFTN0V9g0N1sVlDLaYtA-FtzVZq0oRawFuOLYpuvz9YDc7vZVJVGysuPt3C5yOZulA7BgiPRCUZt5dLuFukXEI-4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من اومدم بعد مدت‌ها، و تازه متوجه شدم این ادمینا تو دایرکت فقط جواب دخترارو می‌دادن متاسفانه
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67478" target="_blank">📅 02:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67477">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
دو انفجار جدید در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67477" target="_blank">📅 02:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67476">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">قشنگ نمی‌زنن بیناموسا، ارضا نمی‌شم دیگه
👉
#hjAly‌</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67476" target="_blank">📅 02:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67475">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهات نیوز | HotNews</strong></div>
<div class="tg-text">قشنگ نمی‌زنن بیناموسا، ارضا نمی‌شم دیگه
👉
#hjAly‌</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67475" target="_blank">📅 02:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67474">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
مجدد انفجار در سیریک هرمزگان
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67474" target="_blank">📅 02:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67472">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80cdbb5e99.mp4?token=QGG_7OZQ23TF-fAZWSVfhMKCU3gjX4Q-fn1aUWi_wMgrwZ1ES7RuH5YywFnF4M1RU2-IZvTTE2wvraWVkocOmsBBVcRRCHSEPL1c-KEssWiHq4cwT80Kxjqta1x_Z5aczyt4F7_yykV-aIMOXB8Pr3yErtKhpN_X3aFW0HKN07YoZQrmWRNTSaIjI1K5a11KM_TPs3A4B7byvmaE1-xJCM4MjaocewxVXJlIgFUBtCwzeB_YLZQvjG3v34NLOEgcE_V7MFml6LV3pVoUwUw9ofjHvWY9bOgzznef9xwyVWZwnXStHam2HNZJj3MZnsv3wOFT1u4m1pu75E6YefH3Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80cdbb5e99.mp4?token=QGG_7OZQ23TF-fAZWSVfhMKCU3gjX4Q-fn1aUWi_wMgrwZ1ES7RuH5YywFnF4M1RU2-IZvTTE2wvraWVkocOmsBBVcRRCHSEPL1c-KEssWiHq4cwT80Kxjqta1x_Z5aczyt4F7_yykV-aIMOXB8Pr3yErtKhpN_X3aFW0HKN07YoZQrmWRNTSaIjI1K5a11KM_TPs3A4B7byvmaE1-xJCM4MjaocewxVXJlIgFUBtCwzeB_YLZQvjG3v34NLOEgcE_V7MFml6LV3pVoUwUw9ofjHvWY9bOgzznef9xwyVWZwnXStHam2HNZJj3MZnsv3wOFT1u4m1pu75E6YefH3Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حملات ارتش اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67472" target="_blank">📅 02:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67471">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
پرواز جنگنده های آمریکایی در نزدیکی بندرعباس در جنوب ایران
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67471" target="_blank">📅 02:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67470">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
انفجار مجدد در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67470" target="_blank">📅 02:08 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67469">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJt1ZreTowLkiLViLYw910m5N81XRqDcVAagxftH1hDtZgHTFrQpb3ssF_B-z4cMcpLkczgH9VceC8LAAjJEWpLV2ZV-i7yZLwf-vY0cJ6pIycaCPIy6jFOW-vqnASAwR33cPzgvkm9HZbiYdG-xgh9a8Pp5MNeXV2BiocgYNyXCLJbj_fV3W2BymDJ2ah1wa0S9PdGMXGlwmUhqHgQ5gjgWEXKYsnPowON5T-Qo-v2uFn_0qDuV6EazmcVNA-jTOZbDo9ElECy57MIAnhKQx4vkeaX1u4ENxQv8NJ5E0Aszu3mi06rEyDHWm6BSn5TNgiipSodhXg9-LCqo87KHVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید:
مقام ارشد آمریکایی به من گفت که حملات ارتش آمریکا امشب در ایران چهار یا پنج برابر گسترده‌تر و قدرتمندتر از حملات اخیری بود که حدود ده روز پیش انجام شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67469" target="_blank">📅 02:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67468">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vUqR5DVLFoMMQ4qPNpnlJmtd_AtRX_4Y7XAKHTh-cM9CAeJYivE73gcDXKj80wz81C8vci18JxLaR9jQgLSgS1uxy_8d579JsGzUBrulHXBNTOgzpQ-RnnBb5d_A1kOWkLou2RKohndWkreVrc9LMcwy0d6DTBSGKolRA1_EvNClaA1DRESkXKMIfLhj_x7HHXxK5xMVAiwacW8bMsjqc6Ni5oEBQCmbZHYTeWR96Zr0RYe-PIhpG064HaEVcmS_788Hwcgrnjev_gTPmINCJ613zTVknRr0PeRxe65U9MOIAyFYGVlyU2eVWRcoyGn66Ust-ikLBzC6028RBmDonw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ستون دود در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/67468" target="_blank">📅 02:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67467">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
قطعی برق در کویت و مناطقی از بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/67467" target="_blank">📅 02:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67466">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
🚨
انفجار مجدد در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/67466" target="_blank">📅 01:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67465">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cfe17753a.mp4?token=OwDp7-M2uUIs_aKdo5aNC8EvLeIrUGrwxkPVVRh3uOzJT1EgMVYAdxmnj8yZwn1jPQiyadz7npUhmbT_wnje0DL3opKeUmrcME71Igjesk5tcJybjWKcWhkaNOsl0bcdD5dkHpIEagTJm8iPoWZqVsLzkDsABiX_pPbFs-SOAsiDbOpX6ypPApKTG8gjhW9sKxaRyCrvnuVllWowH4uYS2SJfMxpKnAinWvMtYkFFSraa1vSBtPSFgVMwGlY4dg_07lutfoj2G3ezwtHzbjQo7XVwWNpA8imI76dZK6zM8sER8sERKU8GLlBjW6LksIfe6CcoOLy4dZZcyytEn2EUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cfe17753a.mp4?token=OwDp7-M2uUIs_aKdo5aNC8EvLeIrUGrwxkPVVRh3uOzJT1EgMVYAdxmnj8yZwn1jPQiyadz7npUhmbT_wnje0DL3opKeUmrcME71Igjesk5tcJybjWKcWhkaNOsl0bcdD5dkHpIEagTJm8iPoWZqVsLzkDsABiX_pPbFs-SOAsiDbOpX6ypPApKTG8gjhW9sKxaRyCrvnuVllWowH4uYS2SJfMxpKnAinWvMtYkFFSraa1vSBtPSFgVMwGlY4dg_07lutfoj2G3ezwtHzbjQo7XVwWNpA8imI76dZK6zM8sER8sERKU8GLlBjW6LksIfe6CcoOLy4dZZcyytEn2EUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات سنگین آمریکا به جنوب کشور
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67465" target="_blank">📅 01:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67464">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hrjEwiy3EmLC3-F2NJJ6S71Z1ZOTwimbnUIvp6y9UdfwlO_rGHM9aKceCpp9FwpjA0Kd3onFiSVRvUyX1RShDclOZtsNC90GGNO44l3Bhjf8N7Tp8Fn5dZpk0OUHK4iZX2r1KRJjdECbzDAyivsHcv5uzt14HlykjvpiF7WU_As40FGuQhEXgtGdmXW5uq3OZNPUHxa8OSY6ebJi4MEmjZ91jPfMZqXeYnFBe82nADvmLPwg5SmNxV89vQ_y3AxWxiYKtZDhnhUuIs8FgqJaq0IQtcfZMxqcBY33dMSAq2HDbO0edp36YBOMGqXJkOTzEUJMjL_LXVNijbAEui6yBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ابوالفضل ناصری، عضو فراکسیون مجلس:
آغاز موج های جدید و بی پایان سپاه
‏تا دقایقی دیگر…!
‏شدیدتر-ویرانگر! ‏
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/67464" target="_blank">📅 01:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67463">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
🚨
کان نیوز :
در آمریکا برای احتمال چند روز نبرد با ایران آماده میشوند؛ این موضوع با کشور های عربی خلیج‌فارس نیز درمیان گذاشته شده است!
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67463" target="_blank">📅 01:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67462">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d35d8f8a5.mp4?token=roRZWGuGVyhnplyDAZ11dtlbkYoCNkwOas9q2okGSQIbnYQBDqjdUcbp4DI2YDyT3EvEaW-Aigr1HLE5lVq-89LWUMN-22PZIUxjX3kSNXhXK112xjn9PGdqmiwoQf9lDGG_-KPg4qmqvu7854-xI1C51AEDgd0PBGSEEVJj2Th6mioxHEnxn9b7Iw2dxWkL0OLac9dFzXSIui_NTHGsVKmy_8i-cnGWz3aszA_5tq4pYY1fqQ87gkzKjTBapbDXJiMap-zNiDytjM8MeGyw1rcEymdLM3JR-CM-X08IBn3rD76-2UqGLAP6OBjSCq_xWFj7odpUz5aIS6lvzeA4IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d35d8f8a5.mp4?token=roRZWGuGVyhnplyDAZ11dtlbkYoCNkwOas9q2okGSQIbnYQBDqjdUcbp4DI2YDyT3EvEaW-Aigr1HLE5lVq-89LWUMN-22PZIUxjX3kSNXhXK112xjn9PGdqmiwoQf9lDGG_-KPg4qmqvu7854-xI1C51AEDgd0PBGSEEVJj2Th6mioxHEnxn9b7Iw2dxWkL0OLac9dFzXSIui_NTHGsVKmy_8i-cnGWz3aszA_5tq4pYY1fqQ87gkzKjTBapbDXJiMap-zNiDytjM8MeGyw1rcEymdLM3JR-CM-X08IBn3rD76-2UqGLAP6OBjSCq_xWFj7odpUz5aIS6lvzeA4IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات شدید و آخرالزمانی ارتش آمریکا به بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67462" target="_blank">📅 01:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67461">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8eaffe3050.mp4?token=iI42L6GjUMV_0eariIBZRrnfq4YNukUh81c6eMq3Suno1yFU54XUNUX57Bxrp4gTj0L8jFOf0WWBmugc8VK2v4V6Z8b_BVUSkTSE4PsPeE46-D_PEG0dS9OlnqonrGlgl8WT-DdbvbMREesnqV0s6lHrFq4Liwmvci0z8eK6BcePe-TroA3ysytIIePi-XbDxk8bMjdgZkfBtAzTZIkySwJDui_cygzvpZ1D7QmRpXm-3eAxmg9b1lOT4mHZ_IQYmVI9qqpaVR9VIEIoPBWlayp3pyn-ONJJvR45SRk5YXsUTN6W3Y8BLPoxZtZaxUlPlrJ5hv8EB5SmbXmbudpaPA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8eaffe3050.mp4?token=iI42L6GjUMV_0eariIBZRrnfq4YNukUh81c6eMq3Suno1yFU54XUNUX57Bxrp4gTj0L8jFOf0WWBmugc8VK2v4V6Z8b_BVUSkTSE4PsPeE46-D_PEG0dS9OlnqonrGlgl8WT-DdbvbMREesnqV0s6lHrFq4Liwmvci0z8eK6BcePe-TroA3ysytIIePi-XbDxk8bMjdgZkfBtAzTZIkySwJDui_cygzvpZ1D7QmRpXm-3eAxmg9b1lOT4mHZ_IQYmVI9qqpaVR9VIEIoPBWlayp3pyn-ONJJvR45SRk5YXsUTN6W3Y8BLPoxZtZaxUlPlrJ5hv8EB5SmbXmbudpaPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
جنوب کشور
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67461" target="_blank">📅 01:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67460">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
🚨
انفجار های مجدد در بندرعباس سیریک و قشم
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67460" target="_blank">📅 01:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67459">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hfwUhBu6EusKKBhxxPzQnY-g-f0g36lDaGXciZKc7-D3veC-lzTk5AwF9fCdzrZRvt48q7RjbS9CqO5vFik0XwIOczVqmvTn85NNjkJhojSuKSxZ334YvXlrFBlMRShC9G6qkMWiP1Ks4Y2ndHA7oA_EyRJYUnAIE-aCsImizZNgsBrMzRaEV9TR-grPDgaIJhR1Sa-Gsh_QbjESnCcpqMXgsd7AB3bX4D6HYM--FGHoAMRt0XY8xoAefhZ00cCVOwZmdaj5lx0OwnA16pRwFL_vr0lBKDemarrSfVPBKO3-4n48pg09v9P2vpRj5xUjek3UqpL_9uj4DgaC0NryGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تحرکات فشرده هواپیماهای ترابری نظامی آمریکا در منطقه رصد شد که شامل برخاستن دو فروند هواپیمای C-17A از پایگاه موفق سلتی در اردن، یک هواپیمای C-17A دیگر از پایگاه ملک فیصل در اردن، علاوه بر یک هواپیمای C-17A از پایگاه شیخ عیسی در بحرین و یک هواپیمای C-5M در پایگاه Alhairates در پایگاه الحائراتس بود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67459" target="_blank">📅 01:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67458">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/761109e119.mp4?token=LdLY_l6pdr-9pekx0NQIEVmkDK0Dhekoljr6QU5DTXCAfPFOQhrcqRZ-_WBI1QlV_R_ien3V64HkQj-YXyLYy3Lh8JSXNNzzw0vwWg4v68q5VQbvyEhakbulEu5YAj8F-rTDgT7cn-VDtezbp-F1SBSvKBCS4fosVqGMhvvNQALD9SpF98Hovli90NZkj1tYDCsUrud6G8dRcDZgPXpNOTk13Gdl3L-N01nruC925BBGFf5EDogWQBf3vh6NgA98bf2QRra1SlJpOUOYOStycwipf5_TNUetbwbbg8NRKlwHkVFMuf3Ir4soj1pwh0-EipkvCTcNM86frDCp0nv_VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/761109e119.mp4?token=LdLY_l6pdr-9pekx0NQIEVmkDK0Dhekoljr6QU5DTXCAfPFOQhrcqRZ-_WBI1QlV_R_ien3V64HkQj-YXyLYy3Lh8JSXNNzzw0vwWg4v68q5VQbvyEhakbulEu5YAj8F-rTDgT7cn-VDtezbp-F1SBSvKBCS4fosVqGMhvvNQALD9SpF98Hovli90NZkj1tYDCsUrud6G8dRcDZgPXpNOTk13Gdl3L-N01nruC925BBGFf5EDogWQBf3vh6NgA98bf2QRra1SlJpOUOYOStycwipf5_TNUetbwbbg8NRKlwHkVFMuf3Ir4soj1pwh0-EipkvCTcNM86frDCp0nv_VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
بامداد چهارشنبه؛ بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67458" target="_blank">📅 01:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67457">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bbd6f07ba.mp4?token=aBONLE1-zpTz1cPbMbSwIIJhKK-ejM3n6RFB9wHbxu0rQJ5BM6HfjorOgLsLHiwEQdJGgQCYBULHqdh5tKn2D-MyGY4w3-H27NSPTwhOsUCEUlVk6zFWtzJw4x-azNzze7fkQJDmjsxCn1ZWiNiWkiAAR47ZPaxEjOYVZzFKc7nBoQNeXpODWCYldbX0SQzkXVbyfdPWmXHbVz5PJxMoXL0N5kQh2v_GIkFhoL8OWaSlfs8dITk2690bKRIit7T6NKwJxjBgg0eptWvzO7obgqfFl5VYxchw5HW1nRm5MZ1dklwq744hq7RsIRHhhXMUV4gmBbd0A8HGeIbyEIqwww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bbd6f07ba.mp4?token=aBONLE1-zpTz1cPbMbSwIIJhKK-ejM3n6RFB9wHbxu0rQJ5BM6HfjorOgLsLHiwEQdJGgQCYBULHqdh5tKn2D-MyGY4w3-H27NSPTwhOsUCEUlVk6zFWtzJw4x-azNzze7fkQJDmjsxCn1ZWiNiWkiAAR47ZPaxEjOYVZzFKc7nBoQNeXpODWCYldbX0SQzkXVbyfdPWmXHbVz5PJxMoXL0N5kQh2v_GIkFhoL8OWaSlfs8dITk2690bKRIit7T6NKwJxjBgg0eptWvzO7obgqfFl5VYxchw5HW1nRm5MZ1dklwq744hq7RsIRHhhXMUV4gmBbd0A8HGeIbyEIqwww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ما که نقض نمیکنیم
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67457" target="_blank">📅 01:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67456">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d512a0d2d.mp4?token=KskKefDbd_ipntaFgxgKvyeLyXlK3vr_sUfeT36H6xnMqnBMauOdeJ2CFNLV8cIyNFMBrgW-qqb0vmPRVal1DSWyuK4QbnVwxPedmcaU5MCGiIBHAardPa-YoK5w9ipIZlJo4O8qXJ3bJn2lBIZlwRJ-fO-5MdGDP_4hQdVzPNORSWVb1rIgiQLf7nfjFBv5c195d6GfxRCk33qEpXVhEFqivhwUL8pitUZJwBfd2whAQEcbCav9R08KxWUDD4paO5nkk5fdkQKZCM1SoANxaQ7PgS8nJbRx9_Fq6yjqWbsg-gzM8cl9Pn2HNfdJn1TnAgxkNM6l7YVla1y0SIo95g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d512a0d2d.mp4?token=KskKefDbd_ipntaFgxgKvyeLyXlK3vr_sUfeT36H6xnMqnBMauOdeJ2CFNLV8cIyNFMBrgW-qqb0vmPRVal1DSWyuK4QbnVwxPedmcaU5MCGiIBHAardPa-YoK5w9ipIZlJo4O8qXJ3bJn2lBIZlwRJ-fO-5MdGDP_4hQdVzPNORSWVb1rIgiQLf7nfjFBv5c195d6GfxRCk33qEpXVhEFqivhwUL8pitUZJwBfd2whAQEcbCav9R08KxWUDD4paO5nkk5fdkQKZCM1SoANxaQ7PgS8nJbRx9_Fq6yjqWbsg-gzM8cl9Pn2HNfdJn1TnAgxkNM6l7YVla1y0SIo95g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
بندر عباس دقایقی پیش
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67456" target="_blank">📅 01:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67455">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a0245f958.mp4?token=PlcdAMNSNlzojxwmpVsSQT2z8mkjuUAk4tXuSiOzwIUhGVNwqBAv4uZrRNZXTXGkZMhPJHTGAivikpFZ6ysfOzi55SeYNuWCzvPsq6ow4G3KM-74kUE-nnZMLCEjWdGS3z4lYx46rb7uwuBG2-E2qxAnRFfA5SwyS2VxP1Q84dZXB56c7AATTg6ruBIAms6qGPsyr83vQmW8U9r_sBowYpMWQBfQ3anEH7O2mt4JFIGQQoewza7rn9C0A2LM_-fK3jDoaUveWC8o5EhsMSKmaZkJfAjSvZPY75rVsnGCM8TzMcLkWMk-kj3wbp1xMZnJ85O_QjAMhnLt9ZdzauNMbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a0245f958.mp4?token=PlcdAMNSNlzojxwmpVsSQT2z8mkjuUAk4tXuSiOzwIUhGVNwqBAv4uZrRNZXTXGkZMhPJHTGAivikpFZ6ysfOzi55SeYNuWCzvPsq6ow4G3KM-74kUE-nnZMLCEjWdGS3z4lYx46rb7uwuBG2-E2qxAnRFfA5SwyS2VxP1Q84dZXB56c7AATTg6ruBIAms6qGPsyr83vQmW8U9r_sBowYpMWQBfQ3anEH7O2mt4JFIGQQoewza7rn9C0A2LM_-fK3jDoaUveWC8o5EhsMSKmaZkJfAjSvZPY75rVsnGCM8TzMcLkWMk-kj3wbp1xMZnJ85O_QjAMhnLt9ZdzauNMbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات سنگین آمریکا به بندرعباس دریابانی
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67455" target="_blank">📅 01:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67454">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🚨
وال استریت ژورنال:
کشتی های جنگی آمریکا در حالت آماده باش برای احتمال شروع احتمالی محاصره دریایی با دستور ترامپ  تا ساعات آینده هستند
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67454" target="_blank">📅 01:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67453">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb48bc0feb.mp4?token=SUh5wXcnzbsf_76vU0w0Xf250H4juS4KMrFuXCukCFzZQIV-tgC7uksibMB4J_kc-7sZKcU3aLwUuW2ADjwAtaLsI2yyll6FXshHEUayhzY9YIFzpMAZLdhq3cqfOLkzj5h78boQPBXYgCAxex0BkuA-mojx42pwMxrIcfKyDKDxHe4OaO5TAV2ZSME8sDEqkRG6BsmJ_JZyFIyv0WrQdeyqr4qQEYncqnB-mKUcbaJJ7oA59aNfyXPBpMd0Oi-nPzyjh6Wan_jZzl26dvFprLgg1hf1n0kDtOKxhlsay-E-_6k5xWIi9WP0oRCczx06LKME6Hr6tWzLpzCltmlZYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb48bc0feb.mp4?token=SUh5wXcnzbsf_76vU0w0Xf250H4juS4KMrFuXCukCFzZQIV-tgC7uksibMB4J_kc-7sZKcU3aLwUuW2ADjwAtaLsI2yyll6FXshHEUayhzY9YIFzpMAZLdhq3cqfOLkzj5h78boQPBXYgCAxex0BkuA-mojx42pwMxrIcfKyDKDxHe4OaO5TAV2ZSME8sDEqkRG6BsmJ_JZyFIyv0WrQdeyqr4qQEYncqnB-mKUcbaJJ7oA59aNfyXPBpMd0Oi-nPzyjh6Wan_jZzl26dvFprLgg1hf1n0kDtOKxhlsay-E-_6k5xWIi9WP0oRCczx06LKME6Hr6tWzLpzCltmlZYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
ویدیو ای منتسب به پایگاه نیروی دریایی سپاه در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67453" target="_blank">📅 01:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67452">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QsD_i7uEmnmzlxR8dr2Xioux-w2b2TQsZfLwjs0f0wbZe_1K9yibMirsty3YLC2OliaQRRQnv7G5g0HgZPnra2QJAkwDaDRL7Dfs51ZUdh9iGimfej7e0LuHFoC7rcYqCzoUGErDtxRMUpp00sxxtxE-pf3oDL2ycoOJ0wPEiSPXV6-Ey0OJonCncpKVLV89ItNpQoj41rAuOBZ6xFOVy7_KTy2mVopwDTvxtcIKr_IO7AAL34IhR_3qBxj_dekB0--jduwJql2U1wlwJeD-_EQq6V-48n4W0X5kmx4s7vfxEJl25WWnb1GcPKcEyM1xBi2UbN6NGHDZvKNIqWxOiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
بامداد چهارشنبه؛ مشاهده ستون دود از سمت پایگاه هوایی بندرعباس.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67452" target="_blank">📅 01:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67451">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m_DOrd08fDSRjZnjQuSVzOfxqDwfQ-SCgBd53QwXCJ6vPHTwkgqyzFLAqcgwj-pOk8Xt-ohgermYmwxxtmki5gX_ON7zGdEPXz5CVbTVCz-7_Wq6VLZGQcxfGnoOhtmTCE7BiiokoUvEatHjwdde8Y4VS7OXoII6VbxU8StEt1m7923RVSRzxTludXcvfMPc_hDER6B8dc5R6EV1q3kJHrZgXhRbO2at5dAq6GP1tJFPqHsbzTHZMGVF3eSRoXdUMp_Bp9bqHQ3PtgYIuc3Q_yjtW8XPANl1O7YC_BlJFqDaekJFr4W_VFmkSq1VK-Z_KLUs7JWHHL31tQ4xSGKtig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
دکل مخابراتی سیریک که هفته ای یه بار مورد حمله آمریکا قرار میگیره :
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67451" target="_blank">📅 01:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67450">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yh2ryrdJBOzmUqZ-uMD1jSbwW0h6JKelKbcsx4rM9nDvQmsdsafsrgGgAbXdxZjejiSzg4XrihnwHLliMBsjvhwjY3iLf5YM7J6eVNnE9kjFmvkejoGs6pWw_R6RKJcIT8dwEihwJj3VcaU11oqnjBBdFBlVd2GlLLSWy65e83bOuceS4IJZoX5ZWASNVtocz2lEHHeTYGjUZRleiOMPLsc8cDQf5F5a3-5o_ObUrDOuYLKCHtw83vbvfJuu-Ve_U8i4GhL6Ssi---MOF2jWExap1pU3SVXxyQizLPXeEeewwA8tS18w1vIWD2lCqcaF_j2Ox4nMISTLM_EDrYBoiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اوه اوه حمله آمریکا به یک اسکله‌.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67450" target="_blank">📅 01:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67449">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cbEPxFkoDP6UH-OrBGLmD6mpqJZrVV5An7c3aliW3N5UyWURcr8ThIx7h0B6YFMjzWeV0Jlb3-HuZyupoegz_zIFPIsuc3Lqz_yNa1bAKhofS4K59KyCZz6N2SFjdN7UBfWYZmxB_TXlA6cNEbIbB5n9N8BUzKayNYhG37-DqCwiuDaCrAjFFbCKYCKvxgHqYli2YwxmJGhvwyoGI6_tex4twjpzBCJzm227k1b4w6jyyDhReryzsUUsncv4VPGd8W-MuduY-RGmjxTU9JIoG_4PIMAqC3NTGCj8OMDhLch9IjYgiDBl8_GzW7c7oC5ysx3_eQhXgm2RWxAQ5WCs3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تصویری منتسب از سیریک هم اکنون
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67449" target="_blank">📅 01:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67448">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hL005wHk9xteXT6ZnIYDxr2SZcVjkdiSFlL3tLmhT0VuhDhRWDnTvlj4sR85EBCIUfAgHb0ms3c5F_fGUDUuM28w1YTrAGSh7CfQrOEJ9GbXvPmeSsyJRyu8GT3z7Ksy4uhXE-nzLhF2YUk5hQIsxkQ7E2QonkYkjJHSzzs9rUbxtkqAHu8NXsnOzLQ0BhhlxFThX4gm9TnR_LVFU9gKEuUbYArYW87HMrU3MRa5jD8OpxNq-PPAPvuZ-Z7fT7g1KVvzlJ-ln7D32pKv60Fao_eLWwEfhN3UY_0R_XpCcq-AQfedPEDWPsMgJW3CNGBTZLPb9PAXDSwmSBdbTmnzDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اسکله‌ی سیریک، شناورهای سپاه
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67448" target="_blank">📅 01:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67447">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1u4xkOtYJhoKb3jBDfONLiL-NcrUBeZJ7GMCwH-4vhTjSN0OBmF9Yu_naRlRD12WJj0rfCxJBuCnx3ID1PSHX5lcxaIW_CzkqhialJrIPrdZbY84gxqJt0_SokVXialZvL06QRhsmcfnmgKdnajBAc8nNcSu_l-EhP5VLSjezhGDRaFK98tu5LVee8hDdAM73z-p39TsTcSl8mSf8WqnkiWCRw-gUyfDtfs4tIJIx-JS4RvdVlnqA89H08NAUcW0ZykPyWAZ7eCiHqsvtXRudu4NIoInvQaTNzZk_6Pc2NnbziYg6K3Tn-G7MH2XA1Teyj6UzvcGj7XQtojh7Z7aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حملات جدید آمریکا به جنوب ایران
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67447" target="_blank">📅 01:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67446">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش ها از هدف قرارگرفتن فرودگاه بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67446" target="_blank">📅 00:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67445">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d3287ab1c.mp4?token=iua_1hW8K1ahcyP-BaeFarktq-Tkgz4y4Sk-PzAMLIzLiA4wRN_Fkt86AoGJ7EezGDkYP8MrzVWMcMPTUluJVS4wVTyOWGF3x2fnPR8NnIYQCA5M5qTB7V4le-NRh593FkveKo-BHeew_n8ojS1wDr1r0ovv0erH4GwELx1i1nUcx3YsVXcdruz7rX4e8O8522jWeLhYtqt89qLDsM1WyqDDCmpswD92O1Jr2mC-D2kkuv0jr1etR7qabdEjrfQe0e9u5O4dxTYxJ8dCmvLiKlFlqjVnO-IYjhGl2tFi0hnZc5orTaSBAlW0DvvxYp-td5Bpr_x1NU478sLT0QU3Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d3287ab1c.mp4?token=iua_1hW8K1ahcyP-BaeFarktq-Tkgz4y4Sk-PzAMLIzLiA4wRN_Fkt86AoGJ7EezGDkYP8MrzVWMcMPTUluJVS4wVTyOWGF3x2fnPR8NnIYQCA5M5qTB7V4le-NRh593FkveKo-BHeew_n8ojS1wDr1r0ovv0erH4GwELx1i1nUcx3YsVXcdruz7rX4e8O8522jWeLhYtqt89qLDsM1WyqDDCmpswD92O1Jr2mC-D2kkuv0jr1etR7qabdEjrfQe0e9u5O4dxTYxJ8dCmvLiKlFlqjVnO-IYjhGl2tFi0hnZc5orTaSBAlW0DvvxYp-td5Bpr_x1NU478sLT0QU3Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
جنگنده‌های اسرائیل حملاتی را در مناطق باراچیت و بیت یاحون، در جنوب لبنان، انجام دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67445" target="_blank">📅 00:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67444">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ از ترکیه و بیخ گوش ایران، دستور حملات به ایران را صادر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67444" target="_blank">📅 00:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67443">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🚨
حملات مجدد آمریکا به بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67443" target="_blank">📅 00:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67442">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UgCWctmstiFBrCsehCmQxnMsEeJb7wU2N8XeOru5iCxGxCyavvRgBIjE89I5mBhGDH8RTrVMAYUAf0UDlUKocSDD6XWz-zHP35ZsPW1D344pgI2-0mXQb1R08DP04FzBsikhvFiXIYvMonO_Vv138qu92lc6WP7sdFzF_n1OEjpcMR3SwMZqT0vLA9l0jlRFwgGTj6jigdJo_9aeuCa-30fmIKhBs3zDcc39a0rEIC7k4BHO0rSFUDYXLBppXCLTshBBaEqxbBuymJQl6J_-jKKnEp-Fn8Ebiqwwco81JMhIUwm30Os4AkIJZK9qs8QB5N1AXmizzW6A3iAT8rUTiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده:
نیروهای فرماندهی مرکزی ایالات متحده، سلسله حملات قدرتمندی را علیه ایران آغاز کرده‌اند تا هزینه‌های سنگینی را برای هدف قرار دادن و حمله به کشتی‌های تجاری که توسط افراد غیرنظامی بی‌گناه در یک آبراه بین‌المللی اداره می‌شوند، تحمیل کنند.
این حملات آمریکا در پاسخ به حملات ایران به سه کشتی تجاری است که در تنگه هرمز در حال عبور بودند. این اقدامات تهاجمی ایران غیرضروری، خطرناک و نقض آشکار آتش‌بس بود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67442" target="_blank">📅 00:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67441">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
🚨
#
فوووری
؛سنتکام هم حملات آمریکا به جنوب کشور رو تایید کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67441" target="_blank">📅 00:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67440">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
🚨
همزمان با حملات آمریکا به جنوب ایران، حملات اسراییل به جنوب لبنان از سر گرفته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67440" target="_blank">📅 00:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67439">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
🚨
انفجار ها در بندرعباس و قشم
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67439" target="_blank">📅 00:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67438">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای چندین انفجار در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67438" target="_blank">📅 00:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67437">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش ها از انفجار در سیریک هرمزگان
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67437" target="_blank">📅 00:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67436">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f7c257f2f.mp4?token=sjM6dc5JdC_1cN7vKzqx5Syba4YOicaxEv0957i1HDkMk8GUO3VFXy_ZdfdM9WJAXHdbHlXc_1jgBRR-l6yW3eN_x5YnsXOMqHjRoM-VbDuUtdqDM0v4AlcZ-3A3W6tteoT0zHzLjy-GawckUBU6XiemZveREVYYOUjwBKXd5HeAizewsxiuuhEabmloNGHZn_Kaw7PjdwYdAKTpdzyGcl_zRdaMokRIuRrqH4CL5K3nx5ASdPnJekmcz8U_zOrvVFH3REOvoTGk7WzGUB7E0ZBMKlblKvZxk6LMbQBo1Tj2ORCyEsJ3rVodTr4Hh240u1c2V8xSwxhBULqY4musPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f7c257f2f.mp4?token=sjM6dc5JdC_1cN7vKzqx5Syba4YOicaxEv0957i1HDkMk8GUO3VFXy_ZdfdM9WJAXHdbHlXc_1jgBRR-l6yW3eN_x5YnsXOMqHjRoM-VbDuUtdqDM0v4AlcZ-3A3W6tteoT0zHzLjy-GawckUBU6XiemZveREVYYOUjwBKXd5HeAizewsxiuuhEabmloNGHZn_Kaw7PjdwYdAKTpdzyGcl_zRdaMokRIuRrqH4CL5K3nx5ASdPnJekmcz8U_zOrvVFH3REOvoTGk7WzGUB7E0ZBMKlblKvZxk6LMbQBo1Tj2ORCyEsJ3rVodTr4Hh240u1c2V8xSwxhBULqY4musPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت های رنالد ریگان درباره جیمی کارتر و نقشی که در سقوط نظام شاهنشاهی ایران ایفا کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67436" target="_blank">📅 00:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67435">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">‼️
مرگ ژوزف استالین و نمایش سه‌روزه جسد او در مسکو، اسفند1331
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67435" target="_blank">📅 23:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67434">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W92wfNLJHaztWSq3mKKkvyBrBUxnuK2PpEbDDcLl7udfcfyBlFgQZma0Cul2M_sGjUsbTsG0Mi2yCv1TKA48dRxIYGAF8R5uZT0FqJmfmmwYxXlaynv_ufixCRvBbEy5CkXmdDgpibmtc4cFZXY9jYIhXAFw7xlQUKXYkOK1Uvku3KjNZmN3y-T6xMaIGSCQsRXDEUHFxsWp7ULFkmnU-eP6gf6PtTP39ortXu8k7aaUaNrQV3oGymd0vgK6-7dRiY3GTKgHSJWFNM_q6XomwWoprTPhS0Xe1ks-he3EVwBgLVCjLaKEH6X19xcBKZL7KaroXMdbIzo1Gpmkwjpg2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو ایتا چخبره؟!
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67434" target="_blank">📅 23:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67433">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
ادعای مقام آمریکایی: واشنگتن مجوزی را که فروش نفت ایران را اجازه می‌داد لغو می‌کند
یک مقام آمریکایی اعلام کرد که ایالات متحده در حال لغو یک مجوز عمومی (General License) است که فروش نفت ایران را مجاز می‌کرد.
به گزارش خبرگزاری رویترز، این مقام آمریکایی هشدار داد که اقدامات ایران در تنگه هرمز «کاملاً غیرقابل قبول» است و «با پیامدهایی روبه‌رو خواهد شد».
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67433" target="_blank">📅 22:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67432">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
طبق گزارش ها یک نفتکش بزرگ دیگر متعلق به امارات نیز مورد اصابت موشک در تنگه هرمز قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67432" target="_blank">📅 22:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67431">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AcVKovf1akt_oFG-5CxaUsIvXOBeAHI8-Yo3wd_1YatbY-onqcunkuS7IeTYYp5xdVSObGmQZszSYf_K1I0bOx2aJTSa-1BBWyXqamW9U8mOJAHlV8k9w8DXB9B9DHeqlhL5hasfUUED4vlNNMvUb8cKTq-t0IT7gWzA4w56-IBth8A5vPM6l4b0zEqH0BG_qz2CXuXEN6stzlkyAK4o9pqfkJA-6X5aW4yKcHT-c4b7VAHu7-vCOxvRkfb44ibEfIQUs9qSRjJwHStcZoMQcsMeZlGRSaT0t5QSS1Tmf7EA4bzjWWD5MkHmLhrIo7GJcwgL0ZYiMmy97VDqMRwszA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
یک‌هشتم‌نهایی‌جام‌جهانی 2026؛ کامبک جنون آمیز و برگ ریزون یاران لئو مسی به جام در تنها 14 دقیقه؛ یاران محمد صلاح بازی دو بر صفر برده رو سه بر دو به یاران لیونل مسی واگذار کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67431" target="_blank">📅 21:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67430">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99630c1014.mp4?token=moETI7seg6LGeIcNsUyjCnOejwnkHpKa1he0q1hUjU4Lg75zVfgfS1xPW03nriwajr2YnIDOU3LtDge0cayh3ck6dh9ABoYsqeRCTXm2v18GRUHPNJ6q3RiY8eIRfY6VpeLK8RBAR7DbMoYktizNv6XoH5wZOuXuUzhoU-RJeH_0TEQG425knxQ-dRZldnYyAcQZ7VbwhS3xqCXuQuORqkO2f779plUdK1FuqLTXV4QxxMilRwrQiPA0E2jAYN6wjzmZoXx9T0YQhSmJBOnWwH4Zgr8DjDLUf2o8Gilk5et727ZtvXO-ajSpv5JosD_4wwFI0VKv-ZrfYEzkHhYMaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99630c1014.mp4?token=moETI7seg6LGeIcNsUyjCnOejwnkHpKa1he0q1hUjU4Lg75zVfgfS1xPW03nriwajr2YnIDOU3LtDge0cayh3ck6dh9ABoYsqeRCTXm2v18GRUHPNJ6q3RiY8eIRfY6VpeLK8RBAR7DbMoYktizNv6XoH5wZOuXuUzhoU-RJeH_0TEQG425knxQ-dRZldnYyAcQZ7VbwhS3xqCXuQuORqkO2f779plUdK1FuqLTXV4QxxMilRwrQiPA0E2jAYN6wjzmZoXx9T0YQhSmJBOnWwH4Zgr8DjDLUf2o8Gilk5et727ZtvXO-ajSpv5JosD_4wwFI0VKv-ZrfYEzkHhYMaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو درباره ترکیه:
من در واقع چندین بار با ترامپ درباره فروش جنگنده‌های اف-۳۵ به ترکیه صحبت کرده‌ام.
به نظر می‌رسد همه درک می‌کنند که علی‌رغم دوستی شخصی که رئیس‌جمهور ترامپ با اردوغان دارد، این موضوع ترکیه را به یک کشور دوستانه برای ایالات متحده تبدیل نمی‌کند.
برعکس، این یک رژیم است که با اخوان‌المسلمین آلوده شده است که از ایالات متحده متنفر است. او حماس، تروریست‌های حماس را پناه می‌دهد. از آن‌ها حمایت می‌کند. آن‌ها را تأمین مالی می‌کند.
اردوغان دقیقاً یک متحد الگویی برای ایالات متحده نیست. او نیمی از قبرس را اشغال کرده است، یک کشور ناتو دیگر (این یک کشور ناتو نیست).
اردوغان تهدید به نابودی کشور من، تنها کشور یهودی می‌کند. ما یک کشور مستقل هستیم و قصد داریم مستقل بمانیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67430" target="_blank">📅 21:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67429">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L51W1RyQh_AG9MiTQLUxznEWTb3hLjTgnRPS2rYtm_jyMO1e9-8xaKhncnPPVY2tzFX6cmemWWD7ImYi6YCqqp-VvzE32lgWBpJe3KEll7UHUxz5hVTuMqBf9xrcmyBXuOganfRaM4cjCMB7qJ5fWItx-g2UkIvMjK40Y9uDLB_GTWJwu5oQVwzvcljQ392SfvmMfJGCTB5uvKjO6LJ4cI1wmEJGFVGBkuOdEu7eUSvryXxjJXvP9hvoNBs5mbciD-W6AGXYReBYuv34BlFd2aY5Z_MBpbZN4PS24yOTZR-KqHwNg38lcaR6FNDYO54pSgcf25NLsrh8NBml7aodaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گفته میشه یه دختر ۱۸ ساله از فشار کنکور و امتحانات نهایی و بخاطر فشردگی امتحانات رگ خودشو زده و خودکشی کرده؛ این پیام رو هم قبل از خودکشی منتشر کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67429" target="_blank">📅 20:27 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67428">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cEQOZ6190wvGGcp8jmx0ZxAwe5jVs6bP6auvd2m-2YwtZf4QvhPRY7EvSnEp9aACxJo062aP0kSyHukm80OVlJcuT6jbcpgNnN3Asb7HypdWZCAx0VFAcFkRq8eD3qrwWshayEiViOwRotqTX1d7LTvpbEtNG2xCsbSlfh3BvCH3svdO21lJh71ywQRkfCgcUbm1jFgxoTfPjU4cn_Ns_EJDQdBGUb47M1uhJIPxRJtW79l9F0u-AkJim8pcSLHKUDgln-zARLd0pZJ819qdz7UFCV4224sH1qWaU3yY2uLvUzcqcu964KUHngOetdFexm-T0s-a_bgZZfGfNYeoaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ان‌بی‌سی به نقل از یک مقام آمریکایی:
ایران شب گذشته با استفاده از دو موشک که مسافت کوتاهی را با سرعت بالا طی کردند، به دو کشتی حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67428" target="_blank">📅 19:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67426">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dMI2NMcStj0diQbPB9TeHb-bgnKiicscp9dl4JQg6qJLZMtqJtoCb8vpK4LjKjFxdu7Hy4C2ZxKxUuUwU2qb_cIY24Lor8ueQVD7bLPpO5EWcmV7-uVBNW1r-_OPXbx0_0xc_oJICoeyuudIZSS-WE1WkLxfmtPcwMISazq4a3vUfdNrl4Tdb1abPPM6hgW4aeyasjeKWGTT56SDFHKms2q5FSuL3s8RlmzpioaR2ssx-ObHoD91gZrFwtKXOhtpliwWk6QDBNAymR8b9k6AvxGTCuJGNwugP3qOf_SWIiHNQVqRNv2uv065IekvpvNdvYexnf4ex0082WJ5H0mhMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/utKxuuvnkcGGyEI84vO-D16tO_Y3enETiBWJn8evWDu-BsHgYCmXDzKRabMPc6o1NctzPkhHlUSfdHVPJ0mBxoxvAk83JjdRwdMza4QsEGkufjMmIqUvdo-5Sbnl5Rvj_eGkKQzp-qI8fv2zbEo8i3D-XkdUhSFLNWK0GBNG062eUg2HpEQa7KxQhQnxjGGd8NWF_Uvpmt0Pm9cQ_VvJwBK3ptDEjVC1kSiHW2sv32fCZy-TJyz9rYCWWbhz1ol8LwBg4AdqnuvAmx7fYJJ-Xm2dhPLBNIt5KVg1yfnIFzcFk7GiDGIwPLiv_4h7nTK5I7rXz4o4ZP9Ru7mBs8wumA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
صدا و سیما این تصاویرو با زیرنویس جمعیت میلیونی مراسم تشییع منتشر کرد :
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67426" target="_blank">📅 19:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67425">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3431abb0e.mp4?token=rab9v0Ft6hXEgLRn8daGbDfuGhUsteH3sn3zvVzgVE8S5deltpU8a3x3dccFoOIDn1rzstZTxfd44oTNtZLLOD3gREf01meocHkyehPDsy66x-ewvVMvGe-apf6SKN6LnnXf0hU4HDWAPPG7pD4euZPLRuWWEMLzqa2gHyzqXy4pLIZ_RWwx5Ck1cEhWfUl13PjlJHlRCFq_gHj9ionvUI-S3d-N1uLBJcdEFNhsUBLG3x8RoN3zeLOrk9nWMbS_UQAcp5r9htVKKdQupg0G282iWFAMrEb3TyF0wyTx1HUiLZriHdwuQ5E9ZbeXwXL98vWQqmcV18EnX-VeNqqDKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3431abb0e.mp4?token=rab9v0Ft6hXEgLRn8daGbDfuGhUsteH3sn3zvVzgVE8S5deltpU8a3x3dccFoOIDn1rzstZTxfd44oTNtZLLOD3gREf01meocHkyehPDsy66x-ewvVMvGe-apf6SKN6LnnXf0hU4HDWAPPG7pD4euZPLRuWWEMLzqa2gHyzqXy4pLIZ_RWwx5Ck1cEhWfUl13PjlJHlRCFq_gHj9ionvUI-S3d-N1uLBJcdEFNhsUBLG3x8RoN3zeLOrk9nWMbS_UQAcp5r9htVKKdQupg0G282iWFAMrEb3TyF0wyTx1HUiLZriHdwuQ5E9ZbeXwXL98vWQqmcV18EnX-VeNqqDKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمزه صفوی، تحلیلگر سیاسی و فرزند یحیی رحیم صفوی، از فرماندهان سپاه پاسداران و مشاور ارشد رهبر جمهوری اسلامی:
🔴
دلیل اصلی ناکامی جمهوری اسلامی در دستیابی به اهداف هسته‌ای «برتری اطلاعاتی طرف مقابل» است و مسئله اصلی، نداشتن بمب اتم نیست، بلکه ناتوانی در حفظ محرمانگی و پیشبرد برنامه‌ها است.
🔴
برنامه هسته‌ای جمهوری اسلامی یکی از پرهزینه‌ترین پروژه‌های هسته‌ای جهان است که این برنامه «نه به تولید برق منجر شده، نه به ساخت سلاح هسته‌ای و نه به کسب مشروعیت برای حکومت».
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67425" target="_blank">📅 18:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67424">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uuwm313-DG_fpLYWu3Y-ytLrLnvQvPzUHZSanHXFYhq6L93FayfyfEkeqorIQ5v68Rce6FvElasMzE5yLSGR_xrl3oBjSuX1oHEz5DpdH-Vs-nSOUldMkLWXgEWiUtoepAHp4d3zpaYT-fHo_BdT3Vz6m42ElpDp4PVDZiclejXFiqNCjF77cscL7VTTtlm2JSkdOeglvJPsu-HERwKbXENdBBnwjZyiGlPN9w3Q1PD8JjPOJhkINu5YMFizs76oReFKFdpBnNfSFl6g0ApysKf8meo1v881j5GHF3bb4G5G7o0CGDKeGY0BGZvRN2NgZG4JCr3ewte1Blcup_B-GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
سازمان عملیات تجارت دریایی بریتانیا: یک نفتکش روز سه‌شنبه ۱۶ تیرماه هنگام عبور از تنگهٔ هرمز با یک پرتابهٔ ناشناس هدف حمله قرار گرفت.
این نهاد اعلام کرد نفتکش بر اثر این حمله دچار «آسیب سازه‌ای» شده، اما هیچ تلفات جانی یا آلودگی زیست‌محیطی گزارش نشده است.این حادثه یک روز پس از حمله به دو نفتکش، یکی حامل نفت خام عربستان سعودی و دیگری حامل گاز طبیعی مایع قطر، رخ داده است
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67424" target="_blank">📅 17:53 · 16 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
