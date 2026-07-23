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
<img src="https://cdn4.telesco.pe/file/drVgZTvAC9RJxc242KpFiBczDNIezyEaUb7Vlum5STS5orbOJcm8Q0f-laJij_rgSXad3eOcJn18v5xoIa8P6iIcVkpqsb334QEb3Q5-iAxWo6Ae7e0kPqtMW5_E6XN0jKh9WHjeCaoDdgkZgRRy-CRkcAydTYApZ4SdfUkEk5yhhckHALsuy1LShWHObaTDqs69LZdu0_nmMOSWjGETADIjSR5EPZKvxiBwrQ4KjZna44JjIQskbnAFlP8wpR1UQOId_q9OFdwEZKy8hchMpOXIcmFWn6DGdxFz6d6RUuQhasGZGNZnyWog5im2WjvmvTLnGyDfmUMibz1zSfrDdw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-01 19:50:12</div>
<hr>

<div class="tg-post" id="msg-136549">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">❌
❌
🚨
🚨
مذاکرات نهایی بین مدیران پرسپولیس و نساجی بر سر انتقال کسری طاهری و دانیال ایری به جمع سرخپوشان روز شنبه برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 669 · <a href="https://t.me/SorkhTimes/136549" target="_blank">📅 19:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136548">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1w0NSHRza-53HRMHMIIJcmR3sb2UWVLLJaqIMDdNTNy4kPhS8wQrePd33O65HuiFZxML4EM6TZulW-eygZUiHIW2Rt0TaC3avngOWa1dVFGXs4o7NldElxWU0Nc7gv9t-7dG3Ui9j_tiO54g9FG9P9R1eisA6YO7KeDGx9ja6vrtDZRUvMRr2zpSKzxhkQTe8rNQeaxqqh7Q2i1NYMtrMqv6eF3Q630E25_bsA4fyPn84DqVK-2SDQLpw-UsYwT7s5Rnrz3aR1bY-1xKAbTz7D6MUziCjyht_lYNETxq1zdMCzhTmoctQN-8pb9m8DasStsyyx4U3feDrOefR3rpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
🚨
🚨
مذاکرات نهایی بین مدیران پرسپولیس و نساجی بر سر انتقال کسری طاهری و دانیال ایری به جمع سرخپوشان روز شنبه برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/SorkhTimes/136548" target="_blank">📅 19:18 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136547">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">❗️
❗️
هنوز قرارداد اخباری، ایری و طاهری امضا نشده/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/SorkhTimes/136547" target="_blank">📅 19:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136546">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔹
فوووووووووری
😐
🔹
ترامپ: دستور دادم در های جهنم به روی ایران باز شود  ۰
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/SorkhTimes/136546" target="_blank">📅 19:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136545">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/np_C1r2cRguRy-pXzbUu9Z9WsRckZl_GflSNO5N-0C7vUa8cfm09kZ-PGYirfI9qJm2U2ZcSTVwT4DYPw0Bzw4YvG9WxmUurm6DuqI_umDTo_9eXrtGazYtBY1HRCzQ6lM-8lZhYAH0qYsIQNswKT9gAJGu7TvXdjSNZcaosiVJxxOTj5OzzpQEPXZXRXvzDmwTU7PtUIV2wB6tYjgIwTRewxt4f3xvOiUV9iW0q61F6kr1U5D9FTit6d0NEnPta4fANyN6EuWXbStyyTJt2NT2AJC9wZWcqdfQJ5mTOvdyxDejkGEE-lWFSwR5LGojJSulbMFBBdTRiRp3KHw4Emw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
علیپور تنها بازمانده نسل طلایی برانکو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/SorkhTimes/136545" target="_blank">📅 19:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136544">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/feaf2d5596.mp4?token=Y11cOZXbEpkiuntUla8lffCiOP-YGKX8pIziYD505AN4e3nvIstZKpJlM3rrXaJNdjDBOIESufb811VJAxrFSt7PsGTbvlBYWXZ-5vCrNojYpXcNaDjziBgKIGZzFfTnuCSHtDpUN22RXDtBcV3PRTfhVe8iXIK-N6prZT1k8cpVHdHnM40zQsTRlJoWZqSJN-hTCzqJ1fhMkoj1JNgfCoGJV-GBoXt9bDMzVxYHUi7fwMfUKRsPFDXJbfWgxp7ruohuTN3GkrPanAtzsWSrWdzxUrIDg2B6tBH9lzZPn3-yqRwC-0Nn5xTWknqsfqyoE72DPsIHFq2N2jh9M2g8AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/feaf2d5596.mp4?token=Y11cOZXbEpkiuntUla8lffCiOP-YGKX8pIziYD505AN4e3nvIstZKpJlM3rrXaJNdjDBOIESufb811VJAxrFSt7PsGTbvlBYWXZ-5vCrNojYpXcNaDjziBgKIGZzFfTnuCSHtDpUN22RXDtBcV3PRTfhVe8iXIK-N6prZT1k8cpVHdHnM40zQsTRlJoWZqSJN-hTCzqJ1fhMkoj1JNgfCoGJV-GBoXt9bDMzVxYHUi7fwMfUKRsPFDXJbfWgxp7ruohuTN3GkrPanAtzsWSrWdzxUrIDg2B6tBH9lzZPn3-yqRwC-0Nn5xTWknqsfqyoE72DPsIHFq2N2jh9M2g8AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
استوک صورتی با کیسه فسخ کرد
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/SorkhTimes/136544" target="_blank">📅 18:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136543">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_aFjZBo5ow1d4T4-Umj7RB4zOHKLHeH9kVYxmIZk1TsMR-nBnqOIq1Zf03pvOX1UcK1_GfMujRQvGtYJbVu9vBW7AFIibfKZJlJL4apIg76fF0G3lIOuMY27kOlL7JzRkBAawGOi4M1T7VyJQaYigJaisNOuXwr5putPsUIOpnwWaCXUb5suv_3kle83xfCqZtRA_uFiDaOqFZkoCeqAkA9JFMranl61ymszF3ZN6jHbFxZz8hvZvUXXfrMYHPgb6rjY1i7aTnZXH0UnpASiPZWAfBiteYEyU7gx_PG-6W8LbSLt04EGG4JDya7tqMlb-cu3eBlggAO4nGTlF8nOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
از تمرینات خبر رسیده پویا اسمی کاپیتان ۱۶ ساله تیم نوجوانان یکی از خوب های پرسپولیس بوده
🚨
این بازیکن در این سن با این فیزیک و قد مناسب شدیدا آینده داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SorkhTimes/136543" target="_blank">📅 17:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136542">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tPwTDtBCdzV4wuBbkYBThoV0fjdNB7hAEtEJ8JmSkVyB6ZrkWlRmnU1C2V9l3Jve7WYZaP1Mr-7FdlkVLfNjafKubJgWmkoD95DL8GrzPAqUyx6tFU1PsLsm2I69k06DGGlTUoEPv3PIWo2kCP-rjUJ7sHRQbXacGtmB0KGhGHDvYO_HRoTHmi4I-L5WvGIPbVdevHWFmhuwgyzQpkOSUosxmGQuK_nA2diITinsgmw51Z1z_bDgS25e8d3mApqrX_J6bkMmyCInipxjJ21_MFrqlF0uhX1RrAfSlFFOzqaNd4tcym-CkjPIxdeBoiTytJj0m2U7yMgEcmjm3TS8aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥇
🇹🇷
تیم فوتبال پرسپولیس برای برپایی اردویی ۱۲ روزه تهران را به مقصد ترکیه ترک کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SorkhTimes/136542" target="_blank">📅 17:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136541">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">✅
✅
طبق شنیده ها   احتمالا فردا باشگاه از سه تا بازیکن رونمایی خواهند کرد .که شامل محمدرضا اخباری و کسری طاهری و دانیال ایری هست.
🔴
باید دید چه اتفاقی خواهد افتاد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SorkhTimes/136541" target="_blank">📅 17:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136540">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OvHm2pmun6aKEgoY9u5r2QKamn3Tc_90uZ7MmIL5AwYri3fzFs-K9po6jqgGuwLYp5Kc88onRS1LtFBzRQDjVwjFhvsloNCBvOVpc3zZTV4ZyVoFd7KagKErmtcg-nBueBM4yhcpntQR-q0IBbIvonKv88_FPZdyjxkzKNKdZepUAs4wIrupRgEXyBLFLfUuGEaFdJUEj6oeav8Zvldoh9l_VckhaKqDtYzChZiLoDHcW7EZ_LeL4rGGHQq117-blKtXmRG1youUgr0MbyBLEiiYj5xSZ--J7RNIlFOURWiIZU3eUwYwSA5wCOr14pSM-Vq-KSQQzE9dIpTpf3RDQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تیم رفت ترکیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SorkhTimes/136540" target="_blank">📅 17:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136539">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/875cf546b8.mp4?token=D7P2wP8WtwNPI7M7YQQcsuCl7jLKO5nwiTDmpgwrzxtzJ9ROj3Hq-RDXl9FPTbP2FKk4AE35qnZwHYjfyg7_lxA2e2LgtZbGuGX8ubrTJcKDji2UGSVVjUxvqalhAg7S6nASPuvk-6M9o_aMdA3pRIvm924ma2qZSqqGMsS6Kd1EInzEb7l9ckrutHkm9fQw4US022j5nOxF1iSWRhdx10elEZf7HelXGkoSVIqe6lY4sOlrgCJ4zMLWbCw0xgRDRwE1Ie9C7aeZp4naUei9WwpXvsXNjAtE67SSPzkOlzLgX9FLzUsw3DOpQyJtLzj_qgYV27ocKa8n3f1BdNr3WD9iwhSCXwjofI-wunip5v0lOF0TK-YfZMPG6JCUUDfU7cXb4d2N4ASoEy-XMkf-LGR7vUIAYo00ikdQxSULuvy-qIoh7Tznw2_8SC3OinsbZRHhBChGGjSEd79tzeSqQ-H-DW65BC_8QxobmWXcmCkBRFzDc_NdF_8V2EGZjmP9BpUeieH3C1nAaKpSghANXyJB5l8OZqeRw1rRLPS1GsVBxJDfuFD0my0tNPBzxzBAE8XlP54b6Ha1iZ_vqo4ZYsWhhqzopaRdC9ic34mvQ6_ehFj_4GRG1-Zc9af4VBMDThJke_rn2IW9S1DR8xiORD2-qD0uAX3zhaJVAjCWiJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/875cf546b8.mp4?token=D7P2wP8WtwNPI7M7YQQcsuCl7jLKO5nwiTDmpgwrzxtzJ9ROj3Hq-RDXl9FPTbP2FKk4AE35qnZwHYjfyg7_lxA2e2LgtZbGuGX8ubrTJcKDji2UGSVVjUxvqalhAg7S6nASPuvk-6M9o_aMdA3pRIvm924ma2qZSqqGMsS6Kd1EInzEb7l9ckrutHkm9fQw4US022j5nOxF1iSWRhdx10elEZf7HelXGkoSVIqe6lY4sOlrgCJ4zMLWbCw0xgRDRwE1Ie9C7aeZp4naUei9WwpXvsXNjAtE67SSPzkOlzLgX9FLzUsw3DOpQyJtLzj_qgYV27ocKa8n3f1BdNr3WD9iwhSCXwjofI-wunip5v0lOF0TK-YfZMPG6JCUUDfU7cXb4d2N4ASoEy-XMkf-LGR7vUIAYo00ikdQxSULuvy-qIoh7Tznw2_8SC3OinsbZRHhBChGGjSEd79tzeSqQ-H-DW65BC_8QxobmWXcmCkBRFzDc_NdF_8V2EGZjmP9BpUeieH3C1nAaKpSghANXyJB5l8OZqeRw1rRLPS1GsVBxJDfuFD0my0tNPBzxzBAE8XlP54b6Ha1iZ_vqo4ZYsWhhqzopaRdC9ic34mvQ6_ehFj_4GRG1-Zc9af4VBMDThJke_rn2IW9S1DR8xiORD2-qD0uAX3zhaJVAjCWiJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
علی علیپور: از آقای قلعه‌نویی تشکر می‌کنم که شانس حضور در جام‌جهانی را به من داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/136539" target="_blank">📅 15:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136538">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
فوری، حمید مطهری با جدایی ابوالفضل رزاق پور، مدافع چپ فولاد خوزستان و پیوستن این بازیکن به پرسپولیس مخالفت کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/136538" target="_blank">📅 14:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136537">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MwOpuxnpNMRduNcp6dRk6jUWiX_dZqJpDyFGIzm0JuN-83xgJfqGlTrA2QKLNhpA9w9L-61ficOtRb3G426PBAD0zsI0guGMa6IcbgLEWuqJbBHqQWItnxu1faAadeHSG915OyBLY-8BDGiG20EZck0DPWa_WFp3A-8ZV-rv7tgikqMvSx1GtgVxqjXVaN-hBlAuf6BXmPnVIgkJKTljItJPtJukxf4zMoNsF7b8hN7vrtKUVvyMLuRKvNN37-bDXXnwp9oFa3uYnleCDLJkbDrteYI9xi-b-WKmY7d2XMAgHNo9JzAmQWiMXWvsx7wL1G8dj7014J1uQS-CGn0UFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
پرسپولیس امروز برای برگزاری تو این کمپ زیبا و
اردوی ۱۲ روزه راهی ترکیه میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/136537" target="_blank">📅 14:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136536">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">❗️
میلاد زکی پور، مدافع چپ سپاهان پس از قرار گرفتن در لیست خروج محرم نویدکیا، به پرسپولیس معرفی شده تا جانشین میلاد محمدی شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/136536" target="_blank">📅 14:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136535">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">❌
❌
فوووووووووری از ورزش سه:  دانیال ایری و کسری طاهری از نساجی به پرسپولیس پیوستند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/136535" target="_blank">📅 13:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136534">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
فوری، حمید مطهری با جدایی ابوالفضل رزاق پور، مدافع چپ فولاد خوزستان و پیوستن این بازیکن به پرسپولیس مخالفت کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/136534" target="_blank">📅 13:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136533">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
شنیده ها: محسن خلیلی ساعتی پیش با حمیدرضا گرشاسبی برای انتقال ابوالفضل رزاق پور دیدار کرد و قرار است در صورت توافق شخصی با بازیکن و واریز مبلغ رضایت نامه این بازیکن راهی پرسپولیس شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/136533" target="_blank">📅 12:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136532">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">✅
✅
با نظر مهدی تارتار ، محمدحسین کنعانی زادگان به عنوان کاپیتان اول پرسپولیس انتخاب شد / فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SorkhTimes/136532" target="_blank">📅 11:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136531">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
مخالفت AFC با درخواست فدراسیون فوتبال ایران؛ گل گهر نماینده ایران در آسیا شد!
🚨
🚨
کنفدراسیون فوتبال آسیا با ارسال نامه‌ای به فدراسیون فوتبال ایران اعلام کرد گل گهر نماینده کشورمان در لیگ قهرمانان آسیا ٢ خواهد بود و در خواست فدراسیون برای حضور چادرملو را نپذیرفت.…</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/136531" target="_blank">📅 11:39 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136530">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">✅
✅
پرسپولیس انتخاب کاپیتان را به تارتار سپرده؛ احتمالاً رقابت بین علیپور و کنعانی است.
🔴
فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/136530" target="_blank">📅 11:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136529">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">✅
✅
طبق شنیده ها   احتمالا فردا باشگاه از سه تا بازیکن رونمایی خواهند کرد .که شامل محمدرضا اخباری و کسری طاهری و دانیال ایری هست.
🔴
باید دید چه اتفاقی خواهد افتاد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/136529" target="_blank">📅 10:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136528">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cb-13hPJEeQn74-N4J7Z7dArFeK_zspwmhMkHt4IuB9xDi0w_PH0SutarxWx4BVLgjCWZqvtNA0JS7isGrqGYNbhOiuYc-dWpw1Jvkh00o53-Z6RIbeXszI5VP_CC2DYTvrGds3X0sKTCfRPw5vl7cDzwuB_zqTnpaYqB5Cljoc5DJWQB6oaah-uECAZIXoB5Y4yEPFoDJGFmTDgQAyEyogvhWFx-TNUvuz_6FgU5Tys7I7K1RvwJUZNGY_GEvuEmEvZIL1SIwVSAbZurlvwHkNVHvlG7BWtf3zHsYL_UhbM5LMv_S7vuzRnL_dUeqPzEY74a7nW88WM57iDRc4QUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
خط دفاعو ببین پسرر
...شیر پسر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/136528" target="_blank">📅 10:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136527">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lAEVIfuj--yBnA8fjE2u_IMHhuQRWRBx7hBl3sxlRhOzPhz2Mz8U-4K0tvGVGd7BX2p9vqb6bOOgqfq4bjdSdjAKKYZaUERXOhtVgwNfslMw6iU7Sj_Ys3QN3O0Fap0q22JlngpNnsB_0eJJLA7lL7t0OaNY5xY3cWJNAl5Hh6K23ip0hr8k-1CnIA8MiV5OC3YBMzRC48pAlrJbgy5yLQI13zbkW5BVeNF0IvY2y64wA0oE5DcMNq1v0ICidhuSsV7LKfWD8D9xJdQvxAduEJGN2TXGxBWCu79FGMQ3sxjSfht16m1ILCssQRcKRnH4xRqr89c0i5VutNrfx0oiQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باراک راوید خبرنگار آکسیوس: یک فروند از بمب‌افکن‌های استراتژیک B-1B Lancer نیروی هوایی ایالات متحده، شب گذشته به ایران حمله کرد
❗️
پ.ن بیچاره مردم که دودش فقط تو چشم مردم می‌ره این جنگ ها و حملات
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/136527" target="_blank">📅 10:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136526">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NNe6OU2s89EK8CsXeFzcCQqnv0ZLMgdqvVwoTjU6vh1Sjw3J6_S9p7aXA4RyQT5csL620-x1kdxy4_6UTTH7jZBGLw4YdlHiOBkNVnZYk8Yc799JS73ckKFYv1oFWaya4VcTNR4ISvNgiKyjedEO9hcJwHimWXWhf5lbefN7bOIUCFAXwnghGlad81vLcahvjC4XJQtRtZIy-PF7BT09iLUHWLgpzFXrk_-olzJpkzFzn0eysnTP3O31u8LDnpe5nUhfeOnAK8G8aOSVS-B09EF1V2Hpq7S3k9JXYLpf5Ax2ghMKgmmA6HnmXYZ0IM5XnaMsIZIybJBmGQB6OrsodQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرهیختگان: محمد‌مهدی محبی در لیست مازاد اتحاد الکلبا قرار گرفته و باشگاه اماراتی پولی بابت رضایت نامه محبی نمیخواد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/136526" target="_blank">📅 09:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136525">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">✅
کسری طاهری و دانیال ایری طی 48 ساعت آینده قراردادشان را با پرسپولیس امضا خواهد کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/136525" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136524">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
محمدرضا اخباری دقایقی پیش با حضور در باشگاه پرسپولیس قرارداد‌ دو ساله شو با پرسپولیس امضا کرد / ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/136524" target="_blank">📅 08:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136523">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔹
فوووووووووری
😐
🔹
ترامپ: دستور دادم در های جهنم به روی ایران باز شود  ۰
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/136523" target="_blank">📅 08:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136522">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OdZvr-RcRF-M_-TMUvRvk9bvU7Uo4VBbPuR85f6HzUw20Ml1ofrWrndFUpxSTtEUp2Oh-uwmsaIbzcdLJ43Yq6YOvkB5ErHDTsl-L40_Uvyx8UAHnli8RriXk3iGW9O6zRjDwfeoUrBCqml4oBpaBJn6tXb6wnXt4Syd75MCaLVZurDXkqnxhYE-exn256nOPd6LlJEStKvFJtEQsBGzh3OVStZkI5fVf2TgBnnycZ3aDRRomlUqOJYbMkK39UJgQrr8mrPI2GNT5hcl12OBmDqC8Pzh2Wek0pB-3UhQc7otOyG8zniPf03B4o5SFZffsbM5G5mVUItlrrEvGq3e0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/136522" target="_blank">📅 08:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136521">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">linebet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/SorkhTimes/136521" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🪙
اپلیشیکن اندروید سایت جهانی لاین بت
💳
واریز و برداشت ریالی
🎁
هر دوشنبه تا سقف ۱۳ ملیون تومان بونوس ورزشی
🔗
بدون نیاز ب فیلترشکن
🤩
آموزش کامل استفاده از اپ
🔜
💰
💰
💰
💰
💰
📱
Telegram Channel
👇
https://telegram.me/+dukgrB6-zGsyNGM8</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/136521" target="_blank">📅 01:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136520">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QtV_shmjqBj32TUnqIiKJxGbtKJVoiomnNxh1R5BpxC6OAGhRV8cXpAL7i0Y2Px8m4hmovcpubvXeB7KczkqICH1qDzuOucpSGhJGFDtUGc8OFDJalztTXpT_YDz3K47iyD0LQ0Ymju3OwWjvjyoPgXH-MPHG06rWpJbrdZnpDL_TlQMs7FIrt-mR6LVK_I2jFdQ5zi_ZV7CFZax6f0dFoBeZe0R9Ge1PWmKqsNQxjZYdsiVNZ-3XQox_VS1icYNRyclIzuYdV4I-xWAgaatHarwCPHLi-wb5joYalcTUohGco516nFs3rSCoVvByU4AUK5NrnffWaEFSR6piQEemw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
به دنیای پیش‌بینی فوتبال و کازینو با LINEBET خوش آمدید
🌍
سایت بین‌المللی و معتبر LINEBET
⚽️
پیش‌بینی فوتبال
🎰
کازینو آنلاین
💳
واریز و برداشت ریالی
🎁
بونوس 100٪ اولین واریز
🎁
بونوس 100٪ هر دوشنبه
📞
پشتیبانی فارسی فعال
🎁
کد هدیه ثبت‌نام: L5670
🔗
دانلود اپلیکیشن اندروید
👉
🔗
لینک سایت
👉
✉️
https://telegram.me/+dukgrB6-zGsyNGM8
🌐
برای ورود به سایت از IP کشورهای آسیایی یا کانادا استفاده کنید.
🇹🇷
🇨🇦
🇮🇳
Ⓜ️
📚
آموزش کامل سایت
👉</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/136520" target="_blank">📅 01:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136519">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H2u9HNlMu5_L5FFj-egEn2-eE_Vrd0r-GazdU0mVI8LbM4yckYr5bcnoCGMgBs4rJ7l1alvlfuP9t6dDgYHzO00ZNZWCJtkjzWi9KI2bLIwOLblnABYcQ3D6XIo1sBAIHIVrtRxYBQn6pNTEQCmDIdJqCMyL4lJB_Mb0IOlChzB9xlVGjA2Uk006gUvy_ObgGKobghUH0O_T9iivojpRqSUgTwAJ555Rj01fzOT_jeolyNNO7k-PzzGWHkJdZske4HBIIG8Rqp1PT3bF3zNHgGPucZ4JLEhX1SBQ5zkodT_0IGoUlcwXlm-IXNBqxrGSKZ9AGQduABRO3O-QJgfpQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
درگذشت قهرمان جوان ژیمناستیک‌ تهران
🔻
محمدصدرا رحیم‌زاده ورزشکار ۱۸ ساله و از قهرمانان ژیمناستیک استان تهران که هفته گذشته در حین تمرین دچار سانحه شده بود، دار فانی را وداع گفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/136519" target="_blank">📅 01:11 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136518">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❌
❌
حملات امشب شروع شد و فعلا چندتا شهر خوزستان صدای انفجار داشتن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/136518" target="_blank">📅 00:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136517">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❌
❌
حملات امشب شروع شد و فعلا چندتا شهر خوزستان صدای انفجار داشتن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/SorkhTimes/136517" target="_blank">📅 00:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136516">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❌
❌
حملات امشب شروع شد و فعلا چندتا شهر خوزستان صدای انفجار داشتن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/136516" target="_blank">📅 00:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136515">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">✅
فوری/ سنت‌کام:
❌
دور جدید حملات از الان شروع شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/136515" target="_blank">📅 00:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136514">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
محمدرضا اخباری دقایقی پیش با حضور در باشگاه پرسپولیس قرارداد‌ دو ساله شو با پرسپولیس امضا کرد / ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/SorkhTimes/136514" target="_blank">📅 00:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136513">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">✅
✅
زارع و شهرآبادی دوباره در ترکیه؛ استراحت دو روزه برای سرخپوشان
⏺
مهدی تارتار امروز را به شاگردانش استراحت داده و فردا نیز سرخپوشان خود را برای سفر به ارزروم ترکیه آماده خواهند کرد. در واقع فردا عصر کاروان پرسپولیس عازم این سفر خواهد شد و 10 روزی را در آنجا…</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/SorkhTimes/136513" target="_blank">📅 00:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136512">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">✅
✅
دیروز در بازی با خیبر، جلالی مصدوم شد و از بی دفاع چپی جای خودشو به دنیل گرا داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/SorkhTimes/136512" target="_blank">📅 23:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136511">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
یک مقام رسمی باشگاه پرسپولیس خبر امضای قرارداد دو ساله با اخباری که وایرال هم شده را تایید نکرد.
🔴
وی در گفت و گو با قرمزانلاین درباره اینکه گفته می شود مذاکرات امیدوار کننده بوده و توافق اولیه حاصل شده گفت؛قراردادی امضا نشده است.بیشتر نمی توانم فعلا توضیح…</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/SorkhTimes/136511" target="_blank">📅 23:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136510">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
فوری از سپهر خرمی:
🚨
بعد از کنسل شدن تمام گزینه های پرسپولیس در پست هافبک دفاعی، مسئولان این تیم دوباره سراغ محمد قربانی رفته‌اند اما اینبار با پیشنهاد بهتر!
🚨
قربانی از تراکتور هم پیشنهاد خوبی دریافت کرده اما تمایل داره به پرسپولیس بیاد!
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/SorkhTimes/136510" target="_blank">📅 23:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136509">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">✅
✅
پرسپولیس با محمدرضا اخباری به توافق رسیده و اگه اتفاق خاصی نیفته، امروز رسماً ازش به‌عنوان دروازه‌بان جدید تیم رونمایی می‌کنه.///فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/SorkhTimes/136509" target="_blank">📅 23:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136508">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
🔴
باشگاه پرسپولیس در آستانه توافق نهایی برای جذب دانیال ایری و کسری طاهری است.
✍️
قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/136508" target="_blank">📅 23:34 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136507">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❗️
رسانه‌های مملکت: نساجی با انتقال طاهری و ایری مشکلی نداره و اونا در اردوی ترکیه به سرخپوشان اضافه میشن و حتی ممکنه کاظمیان هم در ازای رضایتنامه‌ی یکیشون راهی قائمشهر بشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/SorkhTimes/136507" target="_blank">📅 21:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136506">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
تیکدری امروز بازم مثل بازی قبلی یک گل و یک پاس‌گل به نام خودش ثبت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/SorkhTimes/136506" target="_blank">📅 21:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136505">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BsKlOhyBjKgliKZAj59PD92x6D38vrb0bnHr4sB5lgH3G7EJWaHsbceYrpI-9o5NteRsPTlH-LJv7RpOPHFNoXyiaH7s0stM0I3rE44IoauihUnIBpLUfrgcSMupI_K6xsdy9XcNWjh0IrgaN6VIcWmR-8deVOaIeIbEsFJqyjbE9_WiA1uJ2kX10nz5knjmBSq9U0FJgt3XPbR-3lt4qn1_6fWiPGwJFOM4fk02ExfBzshmLQJr3kvm9bQNhu489mJ3AGhcfySQtqvS835KUnEIovCUnMcVNxfh6Q96dPzzske677AZF7cd5ivUczsOohnkBnLB2qenfRx6zdQozw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
فوری/ کان نیوز: اسرائیل از سوی ایالات متحده آمریکا مطلع شده است که این کشور قصد دارد حملات خود به ایران را تشدید کند و در روزهای آینده، و برای اولین بار در این تشدید، حملاتی را با استفاده از بمب‌افکن‌های سنگین علیه ایران انجام دهد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/SorkhTimes/136505" target="_blank">📅 20:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136504">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">✅
✅
امیرحسین محمودی در فصل آینده با شماره 10 برای پرسپولیس به میدون خواهد رفت. شماره ای که سالها بر تن بزرگی همچون علی آقا دایی بوده
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SorkhTimes/136504" target="_blank">📅 20:47 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136503">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❗️
پورعلی گنجی هنوز با پرسپولیس برای جدایی به توافق نرسیده است
🔹
گفته میشه این بازیکن زیر بار کم کردن قراردادش نمیره و کل پولش می خواد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/136503" target="_blank">📅 20:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136502">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">❗️
رسانه‌های مملکت: نساجی با انتقال طاهری و ایری مشکلی نداره و اونا در اردوی ترکیه به سرخپوشان اضافه میشن و حتی ممکنه کاظمیان هم در ازای رضایتنامه‌ی یکیشون راهی قائمشهر بشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/SorkhTimes/136502" target="_blank">📅 20:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136501">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">❗️
تکمیلی :فرهیختگان: استعلام از فیفا اومده و مشکلی برای انتقال نیست و احتمالاً هردو قرضی رایگان تا نیم فصل + بند خرید با تیم راهی ترکیه میشن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/136501" target="_blank">📅 20:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136500">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GszvdB1LC81q_DSXqVP0KKReW5QTJlSARn2Act2h3btiRtHl46cI6lH80OssTcvEZtKI8n8JpVMeqiM4OH3BPbSITddknS4fmxR46ErGxPkUj75r1Dk-hKhSlee0Wjsja5D-lHiVxzRAXn-GenShKbU9zia1yGwF0hwDs4xmADE42q9_3jtJKuZtaNVc-_Hu7-fJkcViHwwbrxBhHBicfGuSDm9A-ktAAXLHw7B7WimlTayGSRY1cXYno7wNNT9hPiPF73v9onGqsLW3AIScrATFdyj30jIomolup6FDvL_kIZpKGBj0_yFHVRf5h2VqvL1xr_jYdje5CnQJXiXqvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی طاهرخانی:
❌
میلاد زکی‌پور با ارسال پیغام‌هایی به بعضی از افراد خواهان پیوستن به پرسپولیس شده است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/136500" target="_blank">📅 20:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136499">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">جالب اینه تموم فرم ها رایگانه، حتما عضو شین و‌ چک کنید چقد راحت سود میشه کرد
😉
✅
JOIN JOIN JOIN
JOIN JOIN JOIN</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/136499" target="_blank">📅 20:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136498">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SYQIyFtxtJAGDpBFW0w_NDOh-kwIkgf9xcvYBj0Mp2SLdlOynA96Erm41i2o0IlqTqutj30BNfrOerZ8yD98Jd7HY_nV0f7Y-ENlzktLuLh7RNn6FL2ODrZwJDOcMfKFJLDzct7y5pfYfRJhkUl8FeJfn956iIkKTZO2kui_Y9oU9TqgWll0e8LwfuxedXs2AtRhtb14IPii6zXrwE2Z3-C16S2XjzvcAmVnH3aubUEztrKVb6ftGB0ieml8w7d8Pfpc6MLa_ZBwhWdl6QuPokho8XAnc4hYXc_NEdV99Mnq6aMx_AYoTgd95L-T9YqYAvk9VzEOm7mfGrH0OiBltA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
Ⓜ️
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@ARON_TIP @ARON_TIP
@ARON_TIP
@ARON_TIP</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SorkhTimes/136498" target="_blank">📅 20:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136497">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❗️
❗️
به این ترتیب با وجود رد شکایت باشگاه پرسپولیس، همچنان موضوع اصلی پرونده محرومیت 4 ماهه بیرانوند به قوت خود باقی است و این دروازه‌بان در شکایت به دادگاه CAS خواستار لغو محرومیت و جریمه مالی خود شده است.
🔴
🔴
شنیده می‌شود هنوز علیرضا بیرانوند در موضوع شکایت…</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/136497" target="_blank">📅 19:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136496">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❗️
🚨
خبرگزاری تسنیم: عادل فردوسی‌پور نباید از علیرضا فغانی که از رضا پهلوی حمایت کرده، تو برنامه خودش دعوت می‌کرد و همین باعث قطع برنامه‌اش شده!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/136496" target="_blank">📅 19:11 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136495">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">✅
✅
زارع و شهرآبادی دوباره در ترکیه؛ استراحت دو روزه برای سرخپوشان
⏺
مهدی تارتار امروز را به شاگردانش استراحت داده و فردا نیز سرخپوشان خود را برای سفر به ارزروم ترکیه آماده خواهند کرد. در واقع فردا عصر کاروان پرسپولیس عازم این سفر خواهد شد و 10 روزی را در آنجا…</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/136495" target="_blank">📅 19:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136494">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">✅
پرسپولیس فعلا با احتیاط داره از اورونوف مراقبت می‌کنه و تو بازی دوستانه بهش بازی نمیده، چون دیرتر از بقیه بازیکنان به تمرینات اضافه شده
❌
❌
کادر فنی می‌خواد با برنامه ریکاوری و بدنسازی مخصوص، کم‌کم آماده‌اش کنه تا دوباره مصدومیت های پی در پی نداشته باشه
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/136494" target="_blank">📅 18:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136493">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b27b7114b3.mp4?token=NwVTiIJ6GpXKmOf0l_98Ko0k-SPSuVBuBW22JR8XKbFXZe8Kw5tLN8jl6zSESyxwXgURkcW7SYh9HpPoTkprnU5NHM9RwgqvuPnhjXPCdhNE-vbytwhSo4axMmQya47q0e6EcYsLlC4TfSFWy_rLOwRQpifMAvtDzDsZSIZ9Pj56S81rFr0174zeWhH-gYC0nO22Q8q70moBV7s9NDOXUGP2cu0nOcuss4sKvzQRJbuIN90H53lTBQv5pSi4qzKgHZQtk_mDAhXyt6qrFGUhkFyxBXRQeOj1GiWSYncTLrGcbmfArrI5blPR2y7gu30kkASNpZg7em9UipfG1w5y0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b27b7114b3.mp4?token=NwVTiIJ6GpXKmOf0l_98Ko0k-SPSuVBuBW22JR8XKbFXZe8Kw5tLN8jl6zSESyxwXgURkcW7SYh9HpPoTkprnU5NHM9RwgqvuPnhjXPCdhNE-vbytwhSo4axMmQya47q0e6EcYsLlC4TfSFWy_rLOwRQpifMAvtDzDsZSIZ9Pj56S81rFr0174zeWhH-gYC0nO22Q8q70moBV7s9NDOXUGP2cu0nOcuss4sKvzQRJbuIN90H53lTBQv5pSi4qzKgHZQtk_mDAhXyt6qrFGUhkFyxBXRQeOj1GiWSYncTLrGcbmfArrI5blPR2y7gu30kkASNpZg7em9UipfG1w5y0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
در شرایطی که قرار بود امروز بازی پلی اف لیگ برتر بین مس رفسنجان و صنعت نفت برگزار بشه.. تیم مس تو زمین حاضر نشده و آبادانیا جشن صعود به لیگ برتر گرفتن
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/136493" target="_blank">📅 18:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136492">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
#فووووووووووری
🔴
پرسپولیس در آستانه جذب دانیال ایری و کسری طاهری
🚨
پرسپولیس از فیفا استعلام گرفت و فیفا اعلام کرد مشکلی برای عقد قرارداد وجود ندارد
📰
فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/136492" target="_blank">📅 18:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136491">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">❗️
باشگاه پرسپولیس برای جذب کسری طاهری از فیفا استعلام گرفته و منتظر جواب فیفا ست تا برای جذبش اقدام کنه/آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/136491" target="_blank">📅 18:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136490">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
🔴
کمال کامیابی نیا هافبک‌سابق تیم پرسپولیس در 37 سالگی از دنیای فوتبال خداحافظی کرد. کامیابی نیا قصد داشت باپیراهن پرسپولیس از دنیای فوتبال خداحافظی کنه اما باندکاپیتان سابق که خودش این پنجره مازاد شد باعث که کمال کامیابی نیا در اوج فوتبالش از باشگاه پرسپولیس…</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/136490" target="_blank">📅 18:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136489">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
ویدیو باشگاه پرسپولیس برای خداحافظی و تشکر از کمال کامیابی نیا
❤️
🎗
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚩
⭐️
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/136489" target="_blank">📅 18:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136488">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">✅
✅
زارع و شهرآبادی دوباره در ترکیه؛ استراحت دو روزه برای سرخپوشان
⏺
مهدی تارتار امروز را به شاگردانش استراحت داده و فردا نیز سرخپوشان خود را برای سفر به ارزروم ترکیه آماده خواهند کرد. در واقع فردا عصر کاروان پرسپولیس عازم این سفر خواهد شد و 10 روزی را در آنجا…</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/136488" target="_blank">📅 17:51 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136487">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
🔴
تیم فوتبال پرسپولیس فردا برای برپایی اردوی تدارکاتی ارزوم ترکیه عازم خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/136487" target="_blank">📅 17:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136486">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
فووری/منابع عبری: ایالات متحده امشب با بمب اتم تاکتیکی تاسیسات کوه کلنگ ایران را منهدم خواهد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/136486" target="_blank">📅 17:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136484">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔻
ترامپ:ما اصلاً کارمان با ایران تمام نشده است
🔻
ما در حال حاضر قصد ترک خاورمیانه را نداریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/136484" target="_blank">📅 16:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136483">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">✅
✅
پرونده شکایت پرسپولیس از بیرانوند و تراکتور که دوساله طول کشیده به علت عدم پرداخت هزینه دادرسی توسط cas مختومه اعلام شد!
🔴
🔴
مدیریت درویش و حدادی:)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/136483" target="_blank">📅 16:27 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136482">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❗️
دیدار تدارکاتی پرسپولیس با نتیجه دو بر صفر به پایان رسید و پرسپولیسی ها با پیروزی به ترکیه خواهند رفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/136482" target="_blank">📅 16:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136481">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">✅
✅
پرونده شکایت پرسپولیس از بیرانوند و تراکتور که دوساله طول کشیده به علت عدم پرداخت هزینه دادرسی توسط cas مختومه اعلام شد!
🔴
🔴
مدیریت درویش و حدادی:)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/136481" target="_blank">📅 16:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136480">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❗️
فووووووری؛ با اعلام کاس، شکایت پرسپولیس از علیرضا بیرانوند رد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/136480" target="_blank">📅 15:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136479">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">❌
شکایت پرسپولیس از بیرانوند و تراکتور رد شد
⏺
دادگاه عالی ورزش (CAS) اعلام کرد شکایت پرسپولیس علیه علیرضا بیرانوند و تراکتور به‌دلیل عدم پرداخت به‌موقع هزینه دادرسی رد شده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/136479" target="_blank">📅 15:27 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136478">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❌
ارونوف تحت شدیدترین محافظت پزشکی
🔴
🔴
پرسپولیس فعلاً خیلی با احتیاط از اورونوف مراقبت می‌کنه و تو بازی دوستانه بهش بازی نداد. چون دیرتر از بقیه به تمرینات اضافه شده، کادر فنی می‌خواد با برنامه ریکاوری و بدنسازی مخصوص، کم‌کم آماده‌اش کنه تا دوباره مصدوم نشه.…</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/136478" target="_blank">📅 15:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136477">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
بی تفاوتی علی دایی درباره استوری بیرانوند؛ فقط سکوت
🔴
🔴
علی دایی صراحتا به دوستان نزدیکان خود گفته است که قصد ندارد جواب علیرضا بیرانوند را بدهد چرا که اصلا او را در حد خود نمی‌داند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/136477" target="_blank">📅 15:23 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136476">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❗️
❗️
قلی زاده: فکر نمیکنم تو ایران برای تیمی جز پرسپولیس بازی کنم ؛ چون قلبا پرسپولیسیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/136476" target="_blank">📅 14:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136475">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
📝
سیدجلال حسینی:
🎙
آقای کارتال خیلی ادعا داشت و نمی‌شد با او کار کرد. کارتال باشگاه پرسپولیس را خیلی کوچک می‌دید و نمی‌دانست به یک باشگاه بزرگ آمده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/136475" target="_blank">📅 14:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136474">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❗️
امروز ساعت 18:45 دیدار پلی‌آف مابین صنعت نفت و مس رفسنجان برگذار خواهد شد تا هجدهمین نماینده لیگ برتر در فصل آینده مشخص شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/136474" target="_blank">📅 14:23 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136473">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/352f2979cb.mp4?token=lLxT7EhnvaokWuxM5a4fe1lutuKMiGJMQuGiwZCa_WK2o4S4rd-EN2U-mCwTiKWxzUGq_DbZEfjdry2_dZuRzw6FOjDNw8-p76aIkOVKT3rI2YeNOnZ7UK8L0lQ5IHPc8p5yVdHsvShEqWW3AAC0lKpHRr-CnGNhdAWP53AC9WGXXcqVgRz62Wk6c6euNQ5VBw2C1khAZuzwdPItMB1J8f6D9awNgE7bVHRyTsgr2EZuo796w3DsCNyuLdRu1etmQCCHpwosjPnVHnu3iIIHAxJJxXjrpEoAli7X0gI3dUjCRaJOq71_CX5AFWnz7rI_PyFHpBHhaol_xSATShYdaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/352f2979cb.mp4?token=lLxT7EhnvaokWuxM5a4fe1lutuKMiGJMQuGiwZCa_WK2o4S4rd-EN2U-mCwTiKWxzUGq_DbZEfjdry2_dZuRzw6FOjDNw8-p76aIkOVKT3rI2YeNOnZ7UK8L0lQ5IHPc8p5yVdHsvShEqWW3AAC0lKpHRr-CnGNhdAWP53AC9WGXXcqVgRz62Wk6c6euNQ5VBw2C1khAZuzwdPItMB1J8f6D9awNgE7bVHRyTsgr2EZuo796w3DsCNyuLdRu1etmQCCHpwosjPnVHnu3iIIHAxJJxXjrpEoAli7X0gI3dUjCRaJOq71_CX5AFWnz7rI_PyFHpBHhaol_xSATShYdaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
📝
سیدجلال حسینی:
🎙
آقای کارتال خیلی ادعا داشت و نمی‌شد با او کار کرد. کارتال باشگاه پرسپولیس را خیلی کوچک می‌دید و نمی‌دانست به یک باشگاه بزرگ آمده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/136473" target="_blank">📅 14:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136472">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
تیکدری امروز بازم مثل بازی قبلی یک گل و یک پاس‌گل به نام خودش ثبت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/136472" target="_blank">📅 14:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136471">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❗️
با پنجره بسته، دفاع چپ جوون هم گرفتن!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/136471" target="_blank">📅 14:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136470">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/SorkhTimes/136470" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">💛
آپدیت جدید اپلیکیشن اندروید MelBet
❗️
🎁
کد هدیه 100 دلاری:
giftcodeir
🤝
اسپانسر رسمی جام جهانی
🔵
کاملترین برنامه موبایل
☄️
صرافی معتبر
🤖
آموزش ثبت نام و واریز
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را فارسی کنید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/136470" target="_blank">📅 14:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136469">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">⚠️
خیلیا نمیدونن که اگه ثبت‌نامشون رو با لینک زیر انجام بدن...
⁉️
💥
بونوس خوش‌آمد گویی تا %220 بیشتر میگیرن!
فقط کافیه به لینک زیر مراجعه کنید و وارد ملبت بشید و به راحتی ثبتنام کنید!
👌
🌐
لینک بدون فیلتر سایت معتبر ملبت
👇
🌐
www.Melbet.com
🎁
بعد از ثبتنام، وارد حسابت شو و توی بخش "بونوس‌ها" فعالش کن
🎚️
نکته:
فقط این هفته فعاله، پس از دستش نده
🙂
🎁
کد هدیه 100 دلاری فراموش نشه:
giftcodeir
✅
معرفی سایت و اپلیکیشن مل‌بت
💯
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/136469" target="_blank">📅 14:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136468">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e636d7ab2.mp4?token=ad9PRbSA01_LnSDPBNSJkzGB68UbMFqzAdvs_JK-iaDRTFess1uQ1lgwWcRqGi34DfP60Sh2b2Luo42zu9-917il1NMTRvmG5B3tewU-veo-Hzlj7nMf6TMseO1m3haZiIFm6ONFErXCmcUDhPZ4LAPEIvhwJi4YIZCz76th9wIzbMvhjv-olmBTeuMt0yuDFcBC8IT6zFAg-1WPZ6UuOLw2mG5li0Vlhb8D6_-Z0aUVHYFgED796p0LUkrliND2W4730N3kUoym1Ee4EjL5jsFEiyeViXx8MF7tozH_WMNNlcatGGpP7DDUibklQoHHa4TkDnFYjRy6hvd922U-mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e636d7ab2.mp4?token=ad9PRbSA01_LnSDPBNSJkzGB68UbMFqzAdvs_JK-iaDRTFess1uQ1lgwWcRqGi34DfP60Sh2b2Luo42zu9-917il1NMTRvmG5B3tewU-veo-Hzlj7nMf6TMseO1m3haZiIFm6ONFErXCmcUDhPZ4LAPEIvhwJi4YIZCz76th9wIzbMvhjv-olmBTeuMt0yuDFcBC8IT6zFAg-1WPZ6UuOLw2mG5li0Vlhb8D6_-Z0aUVHYFgED796p0LUkrliND2W4730N3kUoym1Ee4EjL5jsFEiyeViXx8MF7tozH_WMNNlcatGGpP7DDUibklQoHHa4TkDnFYjRy6hvd922U-mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فنرباغچه اسماعیل کارتال با این گل زیبای تالیسکا بازی رفت پلی آف لیگ قهرمانان اروپا رو برد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/136468" target="_blank">📅 13:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136467">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚩
🚩
قلعه نویی منتقدان تیم‌ ملی را بی وطن و وطن فروش خطاب میکنه...
❗️
❗️
❗️
🔖
🔖
خاک بر سر فوتبال این مملکت، که سرمربیش قندلی است...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/136467" target="_blank">📅 13:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136466">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❌
❌
در ابتدا مدیرای باشگاه قصد فروش اورونوف رو داشتن تا فصل بعد ازاد جدا نشه ولی تارتار خواهان ادامه‌ی حضورش شده و جداییش کنسله/فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/136466" target="_blank">📅 13:17 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136465">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">⌛️
⌛️
فووووووووووووری
🚨
لیگ برتر به صورت رسمی از 23 مرداد آغاز خواهد شد.
🚨
همچنین جمعه 2 مرداد مراسم قرعه کشی لیگ برتر برگزار خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/136465" target="_blank">📅 11:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136464">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/641375cfeb.mp4?token=lPa5Jvs3GzMKkOXbwm0yYMrZeI1F_C8kcPozr9It5TKgz4bNVVeRp2CQzLNll8GdxmsIINkKxDD8EKby8iYtagGPH8aWmhFcvvYtrAiKEHMtnSB44ykYvZcciQXZJRSu03xeYHi1KgsRw4D78ozuF_tXU_OEYq1G0Zi3Pe_zsGMi5lnSwmpxcqdsp5CeiaZcW68qBEl9rh4VTjvKMHMsfnQpc-8rLXH12aZT95_J7X0ZWcJ_-JFi4EtdcgC1U2ChYIYA3EjPrjPcgAp3pWbGYqkgYQnc829xNnFJcagK7zXnEojHOa1aOVH23um2alx1WC_U8Sg2alg4zHejIrZ6xk6DO9Hx7ODiWpfkc6YsDhE4FxxDH27ImhgP4utLl2auQjT0UwxcFWVZw2ajN8v04ItfxFh4ZWm2FovFyxI73QwDpWYYSEojQGzov4A-koGmfqwTozf8_J5Kb57yjdAz01_eX8ulR7EZHhzA6bZpaFWQ7t8YNQNR43AR0k2sOLeWVUX7lhQLtYTkWOskJeMBeWwxjVQb10zsj9ZDppQPOWqakQrlldql_-zbc-kV5KzI78r7HSRPt4-p6tDysR132eCKAq6bPFzYK6P1icSUFjE-KuGgcWDFVoGLISKL8eG2mlXfBzBujJvgcgUsrewn96VBYcn230xu26sCwqhbNtM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/641375cfeb.mp4?token=lPa5Jvs3GzMKkOXbwm0yYMrZeI1F_C8kcPozr9It5TKgz4bNVVeRp2CQzLNll8GdxmsIINkKxDD8EKby8iYtagGPH8aWmhFcvvYtrAiKEHMtnSB44ykYvZcciQXZJRSu03xeYHi1KgsRw4D78ozuF_tXU_OEYq1G0Zi3Pe_zsGMi5lnSwmpxcqdsp5CeiaZcW68qBEl9rh4VTjvKMHMsfnQpc-8rLXH12aZT95_J7X0ZWcJ_-JFi4EtdcgC1U2ChYIYA3EjPrjPcgAp3pWbGYqkgYQnc829xNnFJcagK7zXnEojHOa1aOVH23um2alx1WC_U8Sg2alg4zHejIrZ6xk6DO9Hx7ODiWpfkc6YsDhE4FxxDH27ImhgP4utLl2auQjT0UwxcFWVZw2ajN8v04ItfxFh4ZWm2FovFyxI73QwDpWYYSEojQGzov4A-koGmfqwTozf8_J5Kb57yjdAz01_eX8ulR7EZHhzA6bZpaFWQ7t8YNQNR43AR0k2sOLeWVUX7lhQLtYTkWOskJeMBeWwxjVQb10zsj9ZDppQPOWqakQrlldql_-zbc-kV5KzI78r7HSRPt4-p6tDysR132eCKAq6bPFzYK6P1icSUFjE-KuGgcWDFVoGLISKL8eG2mlXfBzBujJvgcgUsrewn96VBYcn230xu26sCwqhbNtM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
در اتفاقی عجیب، محمد خلیفه به سبک رضا درویش بر روی خودش کت انداخت تا دیده نشه و از ساختمان باشگاه استقلال خارج شد
😂
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/136464" target="_blank">📅 10:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136463">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AjIo1YU8IDrXKDn6FDUtbW29MwYnLN4pWk14OGmaYu4LIvdTgnkZVTv_FFUOCWPHVJi-2JI132PdGhC53yY5wTT7mth3YrXUfgWHe_GNUfoThgVziyETl_XtRozqNHIiHSPRNtKqtFjNMLGIQJKpiiX0wocUPSooBCMecTmd_KTdhmTPPaTGqZXrhvIQlm05vTKBs5OFkD9hvnLROoEVRuFk2qE2YcjiI9OI_q4KjeVwR0O6KBZByhcU3YOk4kP_LUefhx_GOyPQqMtlv80FiIm6SAdsx76fW7hKxDGJXfHWmWtIg6DaNgRBq3m0PW-WRs61BwnnCO7qvZjZaFRc0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
شرط پرسپولیس برای جذب کسری طاهری مشخص شد
🔴
🔴
پرسپولیس به نساجی پیشنهاد داده طاهری را تا نیم‌فصل به‌صورت قرضی جذب کند و سپس با همان مبلغ پرداختی نساجی به روبین‌کازان، قرارداد دائمی او را نهایی کند. حالا تصمیم نهایی در انتظار پاسخ مدیران نساجی است.
🖍
✍️
خبرگزاری…</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/136463" target="_blank">📅 10:47 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136460">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">❤️
🟢
مروری بر مهم‌ترین لحظات دومین مسابقه تدارکاتی سرخپوشان؛ دیداری که با پیروزی ۲ بر صفر پرسپولیس برابر خیبر خرم‌آباد به پایان رسید
.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/136460" target="_blank">📅 10:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136459">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❌
❌
سید جلال
:
❗️
هیچوقت به رفتن به استقلال فکر نکردم و نمیکنم به بقیه بازیکناام میگم اینکارو نکنن.
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SorkhTimes/136459" target="_blank">📅 10:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136457">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
تصاویری از بازی دوستانه امروز پرسپولیس و خیبر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/136457" target="_blank">📅 10:23 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136456">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❗️
❗️
لیست تیم ملی امید اعلام شد.
❌
در این لیست 4 بازیکن از پرسپولیس به تیم ملی امید دعوت شدند.
🔴
امیرحسین محمودی
🔴
علیرضا همایی فرد
🔴
سهیل صحرایی
🔴
فرزین معامله گری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/136456" target="_blank">📅 10:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136455">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✅
✅
وحید کاظمی داور دیدار پلی‌آف لیگ برتر شد
🔴
🔴
وحید کاظمی، قضاوت دیدار پلی‌آف لیگ برتر بین مس رفسنجان و صنعت نفت آبادان را برعهده خواهد داشت. این مسابقه روز چهارشنبه ۳۱ تیر از ساعت ۱۸:۴۵ در ورزشگاه شهر قدس برگزار می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/136455" target="_blank">📅 09:14 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136454">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">❗️
دیشب و بامداد امروز هم طبق معمول انفجار شدیدی در جنوب و بندر عباس داشتیم و برعکس روزای قبل تهران و اکثر نقاط تهران صدای پدافند و صداهای عجیب و غریبی شنیده شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/SorkhTimes/136454" target="_blank">📅 09:12 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136453">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
کسری طاهری و پرسپولیس یک قدم تا یکدیگر فاصله دارند
🔻
مدیران پرسپولیس در آخرین پیشنهاد خود به نساجی اعلام کردند با انتقال قرضی کسری طاهری تا نیم فصل و سپس امضا قرارداد دائمی با این بازیکن با همان مبلغی که باشگاه نساجی آن را از روبین کازان گرفته حاضر به خرید…</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/SorkhTimes/136453" target="_blank">📅 08:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136452">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">✅
✅
#تکمیلی | رویترز:
🔴
ترامپ دستور حمله قدرتمند به ایران را صادر کرده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/SorkhTimes/136452" target="_blank">📅 08:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136451">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cg-JRJus1SvxKjUBTmjcbHaAHKZzR1pSdk7InAzCAw-fQimBff_NIkoMDTF0ENaVoj6UsPHPZgPCThOI8Jlv6gaO7C6AHkXkRyWPFZ3YzeqsfAg7FiqCIS24D7mh05pZfpPfOw4HkTmcfTSF7FXB5--kIM3kfy6mK-SgriA4Myehv0s3SqMdkHihCQbeVWU7NfQrrYsAZIBKaurptmnWbYHXZe8j2zH41KGkD5XY_t_AzL8qjV9Msg1FvGcDBXRKESFznD41YuDVLnsm-ll1ke0Z73v5GnUdga8_BzbaNt0yztebdczfAeOAeWrFlBUC8vHZS5dG3DSkhoa70QCh7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/SorkhTimes/136451" target="_blank">📅 07:44 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136449">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">linebet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/SorkhTimes/136449" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🪙
اپلیشیکن اندروید سایت جهانی لاین بت
💳
واریز و برداشت ریالی
🎁
هر دوشنبه تا سقف ۱۳ ملیون تومان بونوس ورزشی
🔗
بدون نیاز ب فیلترشکن
🤩
آموزش کامل استفاده از اپ
🔜
💰
💰
💰
💰
💰
📱
Telegram Channel
👇
https://telegram.me/+dukgrB6-zGsyNGM8</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/SorkhTimes/136449" target="_blank">📅 01:12 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136448">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I8wiBO4jyGX6S3iRG1UEuRtcWvn9TKwkoxnW7PFH7ePliI_Lnp-TJ_Dv_AAhOGQHQgv730zACUCgqnex0q78qyt3qwFMc8JOooXkN3jEgHjjaHdF2Qok8hHlXoyFoBVkbw7y9ftIyBpHjAQTI04mxYkNVgQGPEM-uHRAG7WdZPKXFBhJ1MkLmbU8BCN6-ZTtqZ-0guhoeVMaacSEfQh4cfbeGCam0GvAZk93DNeBtEgfNWqN0gzuP6PXqAAPT5oSf0xaZAlHMg9xiZawG1ufDCNk_-_HgSLgJLFTKp7mnEnXCtgn1V9RsSvUSEy6Tz-Bd5Dkeo6QIPxs7mCu3U9JYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
به دنیای پیش‌بینی فوتبال و کازینو با LINEBET خوش آمدید
🌍
سایت بین‌المللی و معتبر LINEBET
⚽️
پیش‌بینی فوتبال
🎰
کازینو آنلاین
💳
واریز و برداشت ریالی
🎁
بونوس 100٪ اولین واریز
🎁
بونوس 100٪ هر دوشنبه
📞
پشتیبانی فارسی فعال
🎁
کد هدیه ثبت‌نام: L5670
🔗
دانلود اپلیکیشن اندروید
👉
🔗
لینک سایت
👉
✉️
https://telegram.me/+dukgrB6-zGsyNGM8
🌐
برای ورود به سایت از IP کشورهای آسیایی یا کانادا استفاده کنید.
🇹🇷
🇨🇦
🇮🇳
Ⓜ️
📚
آموزش کامل سایت
👉</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/SorkhTimes/136448" target="_blank">📅 01:12 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136447">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
فرهیختگان:
🔴
تارتار یه وینگر تکنیکی می‌خواست، اما بعد از مذاکرات با یوسفی، هاشم‌نژاد، لیموچی، کوشکی و چند گزینه دیگه، مدیران پرسپولیس به این نتیجه رسیدن که محمدامین کاظمیان رو حفظ کنن و روی خودش حساب باز کنن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/SorkhTimes/136447" target="_blank">📅 00:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136446">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
دیروز تو بازی دوستانه امیررضا رفیعی بازی نکرده و گندمی جوون نیمه دوم به میدون رفته
🔴
به نظر جدایی رفیعی قطعی شده!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/SorkhTimes/136446" target="_blank">📅 23:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136445">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P7No3c8lrWvnUXxGjNgYdRfB2Xn-GSO9g0LdVrgYE5t4SFdjhJVb6PgqO_GVpHEKIB2BzFdr9mQuRjmmodWl1jby3dURE8pBOOwvTxPt2kydB7dg6Q-LGAWQyurXGb4J0X3Vtu6yLDCIRd6DmEiU2XAgdJUtYSbmeG8YvpCVa3OLfI5OQ7FZFrbVH62ySGGB7nQwKGawz8xEgpm2czqmugERhTFsRJ_gZStYo-eHhgPoSq6NVd7hKCUWWsOv6ewZZEQ0hCFD7sldUIj_XkeKgp_-dy8lhvj0bVh6q34ZG004JGlOml6OkQt8YNQsHmKRtmQgP7vId1UAWNEGdloNBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پست جدید ترامپ
🔴
جنگ در افغانستان: ۲۰ سال، ۲۰۰۰ کشته.
🔴
جنگ در عراق: ۹ سال، ۴۶۰۰ کشته.
🔴
جنگ در ویتنام: ۱۹ سال و ۵ ماه، ۵۸۲۲۰ کشته.
🔴
جنگ کره: ۳ سال و ۱ ماه، ۳۶۵۷۴ کشته.
🔴
جنگ در ونزوئلا: ۱ روز، ۰ کشته.
🔴
درگیری نظامی در ایران: ۴ ماه، ۱۸ کشته.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/SorkhTimes/136445" target="_blank">📅 23:49 · 30 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
