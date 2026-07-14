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
<img src="https://cdn4.telesco.pe/file/LsrkeohT1HZyMY4KIbpPif9vZ5sidyn60SJXIoNDzWa4cW1e6poaFwPnImsW8g-_E2IvwhDnPRUSKrry1hp-9gZg5__Rtg118-gylyBOfcTaNcTJsO2RyRXHWdn8ercm0A1Vn9Mm0e8T5Ayh9AeL48ZcoTOe1H2yhBgQq_ihvKBtSQREUSDBb6hl_JAUmHSajktA-7mwptc5e_6l-iK8XYvD96I1Vs6x2fQY_kacCSyCcU_U2fr3L6WTcILuEk5nH-MEsqfwKLsu_aPKssh_0HtBRcA9ilENIJ7TydJTHR881Dr_Hk4o5j0DjJNurnXU9NeBV4tbB2RCN6ElNYMtJA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 386K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-23 19:38:12</div>
<hr>

<div class="tg-post" id="msg-18034">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">دونالد ترامپ، در دفتر بیضی شکل با علی الزیدی، نخست وزیر جدید عراق، دیدار کرد. در طول این دیدار، ترامپ به الزیدی گفت: «
او جوان و خوش تیپ است، که این من را خوشحال نمی‌کند
.»
@WarRoom
🤣</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/withyashar/18034" target="_blank">📅 19:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18033">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ایران اعلام کرد که زیرساخت‌های شرکت اسپیس‌اکس (SpaceX) متعلق به ایلان ماسک، هدف نظامی مشروعی محسوب می‌شوند
@WarRoom</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/withyashar/18033" target="_blank">📅 19:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18032">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4d88026e9.mp4?token=OWAVMhKuRIXq9PQ0bHWHHbg6pCC66OiuXpb_KTkBgIqhHDuWgW4NRoY_H01ibwkTs9VPaDVsc1qQ0I3q9UpN0bg3Bj6QYoar1Zfh2GrClzBghcPC6fRj7UZUphc-2XA0o1t8wASOZmcNSBmdZmOx99BbTa3UdmNlhrvcchDp_BGnD3GwRB-PT5ySV4WFClroK14eUwaQfzRLFB9TpzIVxIGmpI-iUkeEH5AnR8cbgBUAFMPo9yWCQUP8MYlMPfKUb0GdVgLIf4CHq9UeXeE4zHtVgzxT1gcyxu12f1xffr4woTgsSapEMfc1z6e5tx7iMmkOlrMM1etlaaM_vfjjvy3AkjU0XoGAjhnGRjth09BTdHkA8V4nourVTng0h6kIJC14QmGhuGEXh93GIDcoVGuPpgKLUbAfwK4b4D_q3NOh6zUfnIAt1w_YNtL4aQ_G2mL7pcuqceVV35RUzoUBpxEnDdJQeKR1rFxftS1F4zpxbfVGZ5UaFh5EB4141wCLD_DD_cQr2jeaX8jLSB_EAgnuX9uGB83_cpciEGfv8N9FJRM2bwm1e0vX-2tssZOWyfba_M-RCCE_2unWGdQfe6xVDLLLfhkNJMXCyckdSIniiIL2j9-7QFq-1yAKA_gDShSZ6tEEDNGnGg12gJW84ANe_HwuRldm_EoZKZWyvmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4d88026e9.mp4?token=OWAVMhKuRIXq9PQ0bHWHHbg6pCC66OiuXpb_KTkBgIqhHDuWgW4NRoY_H01ibwkTs9VPaDVsc1qQ0I3q9UpN0bg3Bj6QYoar1Zfh2GrClzBghcPC6fRj7UZUphc-2XA0o1t8wASOZmcNSBmdZmOx99BbTa3UdmNlhrvcchDp_BGnD3GwRB-PT5ySV4WFClroK14eUwaQfzRLFB9TpzIVxIGmpI-iUkeEH5AnR8cbgBUAFMPo9yWCQUP8MYlMPfKUb0GdVgLIf4CHq9UeXeE4zHtVgzxT1gcyxu12f1xffr4woTgsSapEMfc1z6e5tx7iMmkOlrMM1etlaaM_vfjjvy3AkjU0XoGAjhnGRjth09BTdHkA8V4nourVTng0h6kIJC14QmGhuGEXh93GIDcoVGuPpgKLUbAfwK4b4D_q3NOh6zUfnIAt1w_YNtL4aQ_G2mL7pcuqceVV35RUzoUBpxEnDdJQeKR1rFxftS1F4zpxbfVGZ5UaFh5EB4141wCLD_DD_cQr2jeaX8jLSB_EAgnuX9uGB83_cpciEGfv8N9FJRM2bwm1e0vX-2tssZOWyfba_M-RCCE_2unWGdQfe6xVDLLLfhkNJMXCyckdSIniiIL2j9-7QFq-1yAKA_gDShSZ6tEEDNGnGg12gJW84ANe_HwuRldm_EoZKZWyvmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آسمان اردن
@WarRoom</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/withyashar/18032" target="_blank">📅 19:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18031">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">انفجار های شدیدی در کویت گزارش شده
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/withyashar/18031" target="_blank">📅 19:17 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18030">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">آسیب به تأسیسات برق کیش در پی انفجار پرتابه‌ها؛ احتمال خاموشی موقت شرکت آب و برق کیش: در پی انفجار پرتابه‌ها در نزدیکی نیروگاه برق جزیره، برخی تجهیزات فنی آسیب دیده و در حال بررسی است.  @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/withyashar/18030" target="_blank">📅 19:16 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18029">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">آسیب به تأسیسات برق کیش در پی انفجار پرتابه‌ها؛ احتمال خاموشی موقت
شرکت آب و برق کیش:
در پی انفجار پرتابه‌ها در نزدیکی نیروگاه برق جزیره، برخی تجهیزات فنی آسیب دیده و در حال بررسی است.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/withyashar/18029" target="_blank">📅 19:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18028">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">کاخ سفید:  «به ترامپ اعتماد کنید؛ وحشت‌زده نشوید» @WarRoom</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/withyashar/18028" target="_blank">📅 19:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18027">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ارسالی : پایگاه چهارم شکاری دزفول شیشه هامون لرزید یه انفجار
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/withyashar/18027" target="_blank">📅 19:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18026">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">کاخ سفید:
«به ترامپ اعتماد کنید؛ وحشت‌زده نشوید»
@WarRoom</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/withyashar/18026" target="_blank">📅 19:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18025">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">اندیمشک و دزفول رو ززززززدن
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/withyashar/18025" target="_blank">📅 19:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18024">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">قشم رو ززززززدن @WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/withyashar/18024" target="_blank">📅 19:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18023">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">تحلیل مانوک خدابخشیان در پاسخ به روح‌الله زم(در حضور وی)که باید شنید.
@WarRoom</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/withyashar/18023" target="_blank">📅 19:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18022">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">کویت : ما در حال حاضر مورد حمله موشکی/پهپادی ایران قرار گرفته‌ایم. @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/withyashar/18022" target="_blank">📅 19:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18021">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">کویت : ما در حال حاضر مورد حمله موشکی/پهپادی ایران قرار گرفته‌ایم.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/withyashar/18021" target="_blank">📅 19:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18020">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترامپ در کاخ سفید از نخست‌وزیر عراق استقبال کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/withyashar/18020" target="_blank">📅 18:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18019">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">انفجار پایگاه دریایی بوشهر
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/withyashar/18019" target="_blank">📅 18:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18018">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rGgZhdOexTyxUEkWQoKP7ATtR_RDxi50wx5XcLdhEnpsaCi5OevZ5W2YR9hadSU9TCR9J3LvSS_EQjG-2xCG6lthLsHTZw_Wu2zWXwly5EkJMmd_XAiC7MoLXhM4EukjDwYZaP6AFd9Q6r-m_bDlbHtiOKvmdhIqm0uYUmSuTsyjdX6NuMAfQuVSJJaVP4teEjxpOpZ3qHvSxMKwZVu0_R2CIEHAaQzBdobKNxvEhaQ_B0EvrZwaoj2Jed0FJfZ_607cLrjqjn4O4hBrFMUkj3kQ-k90F674p4sYm27R22kA8MH864fJstpnAbqHhSvW8e2oAaQnwwFyuQh6TnIF9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ما یک محاصره کامل خواهیم داشت، اما فقط بر روی کشتی‌هایی که به بنادر ایران می‌آیند و می‌روند، یا هر چیزی که مربوط به محمولهٔ ایرانی است را حمل می‌کنند.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/withyashar/18018" target="_blank">📅 18:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18017">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">قشم رو ززززززدن
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/withyashar/18017" target="_blank">📅 18:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18016">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3ad064452.mp4?token=bejWCl5HlpTAuHMidSKxUa2qlYF1SJkTzJkkdaD46xXTOq2I_klIHlTIbMSaiiqmwUEpwXqtKXyPk9aAPWvRH0BhpoetSLm1kU8p6FtnnI0ZL_nd6B3CnuQlFyuMiA70wDiN-2PDQaCPYNYogn_r5DHiXX-_-1WhXzGv5xp5mA2WpjKKRx0T5cXAJiBgiPf0JXx7TU9SsLhEEihOd9xTicWgaGrKB04EPoZ3jxGwfpWBos2qaknhGjkXkLRDGDUpqBMvTb0zGCek9cLNJZt5GtJfRl0-Yiurxbv7ZsC3uojqHmAuXOCiKPV_LPrLMp_-dpYQCiaFTDQ6pkhX5NKOMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3ad064452.mp4?token=bejWCl5HlpTAuHMidSKxUa2qlYF1SJkTzJkkdaD46xXTOq2I_klIHlTIbMSaiiqmwUEpwXqtKXyPk9aAPWvRH0BhpoetSLm1kU8p6FtnnI0ZL_nd6B3CnuQlFyuMiA70wDiN-2PDQaCPYNYogn_r5DHiXX-_-1WhXzGv5xp5mA2WpjKKRx0T5cXAJiBgiPf0JXx7TU9SsLhEEihOd9xTicWgaGrKB04EPoZ3jxGwfpWBos2qaknhGjkXkLRDGDUpqBMvTb0zGCek9cLNJZt5GtJfRl0-Yiurxbv7ZsC3uojqHmAuXOCiKPV_LPrLMp_-dpYQCiaFTDQ6pkhX5NKOMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکیه حکم بازداشت نتانیاهو را صادر کرد به نوشته «ترکیه تودی»، این حکم موقت از سوی دادگاه عالی کیفری یازدهم استانبول و در چارچوب رسیدگی به پرونده مربوط به توقیف ناوگان صمود - که عازم غزه بود - صادر شد. فهرست اتهامات علیه نخست‌وزیر اسرائیل شامل «جنایت علیه بشریت»،…</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/withyashar/18016" target="_blank">📅 18:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18015">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ترکیه حکم بازداشت نتانیاهو را صادر کرد
به نوشته «ترکیه تودی»، این حکم موقت از سوی دادگاه عالی کیفری یازدهم استانبول و در چارچوب رسیدگی به پرونده مربوط به توقیف ناوگان صمود - که عازم غزه بود - صادر شد.
فهرست اتهامات علیه نخست‌وزیر اسرائیل شامل «جنایت علیه بشریت»، «نسل‌کشی»، «صدمه عمدی» و «شکنجه» است.
@WarRoom</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/withyashar/18015" target="_blank">📅 18:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18014">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a32f130ceb.mp4?token=lIOWo4uadJPslI3GP-QSEYNPkj_8DrGDcjxvxznYxOUq3TeOvKEyBavq3mtw8bzgmmwkVESRsZB40iocLLNjh_4XuhX06ze28Kt4Rol5lfEqb6-Rw8Uj4_KZRFZzVU-VPldpvnO1vNjV7iEsT3mYQJYLh7qhcmv0wMEsybEL9q7hKn4-dwSyFOfD_jWI5lAxl9nQ17DmVdPNjPM43N7WKQMcVNnlyge3azU8SMWBmq3AnBtOt2V81B7uXoO1ApvSYb6liMASG5XzMQGZMFX43C80C0LvhE7foxL5qTdVdIHtXmqc5rLMSbTpdA-0fZBa2bMxoc_Ht8tz0fatNan_c3riDzXZiD25QBgmF021iux2JWPgw_FNRRJ-o5eE9DGwNI2AGw3pQBWrLTS01iIMiUq1Ic4p9G7c5EGOBx5Jj6xE7y8wjeCHQb327T9SNE7EbZNA608PCL1Oc4d3SigeENR1TYktA5h88RHEPGtaTR3jWbSc0pxvFfVVWX16VJTx3QmOEjpvSBf7JJwWvcdJbIDgOU7Tq2yn457fosxXvi6vm4yCZ23COYvBy2ll5ir96BjwJzFBb7Cn28Ci4S_p28f-sBXJCvJfOrk9L8pqVrAeRAwCv8ioiK8qvfadpQLDumo3UFgbRNsUePtEMi2AA4E0aUwUONdd0NrTuuQuN3M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a32f130ceb.mp4?token=lIOWo4uadJPslI3GP-QSEYNPkj_8DrGDcjxvxznYxOUq3TeOvKEyBavq3mtw8bzgmmwkVESRsZB40iocLLNjh_4XuhX06ze28Kt4Rol5lfEqb6-Rw8Uj4_KZRFZzVU-VPldpvnO1vNjV7iEsT3mYQJYLh7qhcmv0wMEsybEL9q7hKn4-dwSyFOfD_jWI5lAxl9nQ17DmVdPNjPM43N7WKQMcVNnlyge3azU8SMWBmq3AnBtOt2V81B7uXoO1ApvSYb6liMASG5XzMQGZMFX43C80C0LvhE7foxL5qTdVdIHtXmqc5rLMSbTpdA-0fZBa2bMxoc_Ht8tz0fatNan_c3riDzXZiD25QBgmF021iux2JWPgw_FNRRJ-o5eE9DGwNI2AGw3pQBWrLTS01iIMiUq1Ic4p9G7c5EGOBx5Jj6xE7y8wjeCHQb327T9SNE7EbZNA608PCL1Oc4d3SigeENR1TYktA5h88RHEPGtaTR3jWbSc0pxvFfVVWX16VJTx3QmOEjpvSBf7JJwWvcdJbIDgOU7Tq2yn457fosxXvi6vm4yCZ23COYvBy2ll5ir96BjwJzFBb7Cn28Ci4S_p28f-sBXJCvJfOrk9L8pqVrAeRAwCv8ioiK8qvfadpQLDumo3UFgbRNsUePtEMi2AA4E0aUwUONdd0NrTuuQuN3M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ اصل مصاحبه دهه هشتادش رو هم منتشر کرد که براتون با زیر نویس فارسی قرار دادم لذت ببرید
@WarRoom</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/withyashar/18014" target="_blank">📅 18:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18013">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/withyashar/18013" target="_blank">📅 18:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18012">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWQbktwc73kRZrdmnHy1OwSfQq1FgJCEDCtrc2Au1j8SrT1U8lyNtnaB9_p6KWY-LuS_Z4GP6j-KieR-o2lmxasx0ih48ixKAELtRYn5WwnqtnsqdcT-M0c2_lUKTijReIiWL2fXQHqNlvU5W2Amy4MtG4R5N8kpRoZvm7Me9U4As-lo_Q70ftQHiNNcgvt1zUzJ5dwR-ZD4d3WtzQvehR0qI3AAJCU5JfE8YnMTftFj8wWqr6V0oTLhMroiOIoKzHICd8g65J34FVaN_8kA7nnDh__ylW5vbe4cUPrA7qGcr1ulao1ZRnn8l06eHVFMkKL7KYP7-_IT0Q1RJmLoew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ پستی از کاربری که متنی از مصاحبه او با روزنامه گاردین است را بازنشر کرد.
کاربر : «وای خدای من!
اصلاً نمی‌دانستم ترامپ این را گفته است.
آن هم در سال ۱۹۸۸!
جزیره خارک را تصرف کنید!
»
متن مصاحبه ترامپ با گاردین ۱۹۸۸:
«اگه من بودم در قبال ایران بسیار سخت‌گیر می‌بودم. آن‌ها از نظر روانی ما را شکست داده‌اند و باعث شده‌اند مثل یک مشت احمق به نظر برسیم. اگر حتی یک گلوله به سمت یکی از نیروها یا کشتی‌های ما شلیک می‌شد، یه بلایی  بر سر جزیره خارک می‌آوردم و وارد عمل می‌شدم و آن را تصرف می‌کردم. ایران حتی از پس عراق هم برنمی‌آید، اما ایالات متحده را به بازی گرفته است. حمله به آن‌ها به نفع جهان خواهد بود.
@WarRoom</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/withyashar/18012" target="_blank">📅 18:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18011">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اکسیوس: تلاش‌ها برای دور زدن تنگه هرمز ادامه دارد.
@warroom</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/withyashar/18011" target="_blank">📅 18:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18010">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-footer">👁️ 82.4K · <a href="https://t.me/withyashar/18010" target="_blank">📅 17:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18009">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MeEhixUYrwXimwXnXrNigXN5ybGSPOjMa4F0d7p-6VBF6qzGaPwPt6xkorVIpUzF7eZO4mtFZXv9Ejn233-ssrYJKmOyjUo6hN8u3WcXetB7Q_xeDCbEX7gxvIa8JN1RLoavf23szAbw7yX-aS_VtEfitWKjW42DC4nItbs76spPQxed6_zFjPKtW_XNT3r2UuKflR7cvcdwocL6ikWpvra1AD4H314YoaKxeK-z8YalCQ05YGGvGD0bzi7xKDOyxGwundpdfqA8XJV_smTpnwJDeFquhjKjI2PjnKAhW-efGNYcmPplmhh-_DAJR-ZjK7aK2CBgAFuiD6VKkhE7FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارشهای متعدد از مشاهده ستون دود(احتمالا آتش‌سوزی) خ دماوند.میدان امام حسین تهران
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 86.5K · <a href="https://t.me/withyashar/18009" target="_blank">📅 17:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18008">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">اعلام الحربی یمن:
به تمامی شرکت‌های هواپیمایی هشدار می‌دهیم که از پرواز در حریم هوایی عربستان خودداری کنند و هشدارهای ما را جدی بگیرند تا زمانی که تحریم‌ها از فرودگاه بین‌المللی صنعا برداشته شود.
@WarRoom</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/withyashar/18008" target="_blank">📅 17:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18007">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd2ca3903c.mp4?token=F0dlA5Vyx_hZO1Sp7a2xQ29XfOuFBBeVRp4wExy5no5snTBVNhsPN5DPlHUE3Emb7_jZDpdcxHruVNShVkWCBl8CjKnrOrKFbB4M2c-WtQBZOH9cgwRGrr_9M-qh8H4fAikB9bHgkAQQXxTpikvMnYnpKGMlxRF-PujwsdBdPOG-Uay2dgklp1tBqQWe3Suc1Jvj6VdAm0quZ1SICVGkVm_DabRe0uHrlNW9Ih1NV9NtFIdvEhK-08SM2d--VrT4O2WiKQMGoBfOHvusRzpKYzb7LEsL3GyIr8zxRWWIjSCKszTiGfM-goNmoCWXt-wdeRbRYevld7c7c0_P7tdT4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd2ca3903c.mp4?token=F0dlA5Vyx_hZO1Sp7a2xQ29XfOuFBBeVRp4wExy5no5snTBVNhsPN5DPlHUE3Emb7_jZDpdcxHruVNShVkWCBl8CjKnrOrKFbB4M2c-WtQBZOH9cgwRGrr_9M-qh8H4fAikB9bHgkAQQXxTpikvMnYnpKGMlxRF-PujwsdBdPOG-Uay2dgklp1tBqQWe3Suc1Jvj6VdAm0quZ1SICVGkVm_DabRe0uHrlNW9Ih1NV9NtFIdvEhK-08SM2d--VrT4O2WiKQMGoBfOHvusRzpKYzb7LEsL3GyIr8zxRWWIjSCKszTiGfM-goNmoCWXt-wdeRbRYevld7c7c0_P7tdT4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام : همکنون ملوانان آمریکایی عملیات پرواز را بر روی ناو هواپیمابر یواس‌اس جورج اچ. دبلیو. بوش (سی‌وی‌ان ۷۷) انجام می‌دهند.
@WarRoom</div>
<div class="tg-footer">👁️ 92.7K · <a href="https://t.me/withyashar/18007" target="_blank">📅 17:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18006">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef98fc005e.mp4?token=LtsD2EI80jNV2nIFqsiG7LGrer_IsUGO13RaGPJVCLhtdBYOcMGjfaC5S129854S_bSKsoWaYlnkHgf7cSysAvrBt9Y6cLrnQMqF3R2goEO58nWqx1QFl9t5sOfiPHtvu_Vc-W_yVirA_5_j7i6oGGlgeAdlIBRLPjTp8hagUYsFheWMLqDC3BTsyhF3wPuHyUy0WdekFMrve5xWUTjuFoRykIJhUcNMtYdzoBkZpIUqUrNq-5-HWYVm23qQN3nwZymNZcKWLqbhvW-YQasA1mXAbpvbSNMpQ9CJyoHwSyIMxgiR8lGqVu8ZwjgppozIeEnqPbaSKS9mOvF0RqXSLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef98fc005e.mp4?token=LtsD2EI80jNV2nIFqsiG7LGrer_IsUGO13RaGPJVCLhtdBYOcMGjfaC5S129854S_bSKsoWaYlnkHgf7cSysAvrBt9Y6cLrnQMqF3R2goEO58nWqx1QFl9t5sOfiPHtvu_Vc-W_yVirA_5_j7i6oGGlgeAdlIBRLPjTp8hagUYsFheWMLqDC3BTsyhF3wPuHyUy0WdekFMrve5xWUTjuFoRykIJhUcNMtYdzoBkZpIUqUrNq-5-HWYVm23qQN3nwZymNZcKWLqbhvW-YQasA1mXAbpvbSNMpQ9CJyoHwSyIMxgiR8lGqVu8ZwjgppozIeEnqPbaSKS9mOvF0RqXSLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو : فقط یک چیز می‌توانم به شما بگویم. نه، آن را به رهبران ایران می‌گویم: اگر به ما حمله کنید، روی آرامش حساب نکنید. روی تکرار این حمله حساب نکنید. چون تکرار نخواهد شد.
حمله قبلی به اندازه کافی قدرتمند بود. این حمله متفاوت خواهد بود - قدرتمند.
روزهایی که کسی می‌توانست به ما حمله کند و ما دو برابر محکم‌تر حمله نمی‌کردیم، گذشته است.
@WarRoom</div>
<div class="tg-footer">👁️ 99.9K · <a href="https://t.me/withyashar/18006" target="_blank">📅 17:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18005">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQNn6_XUOPIFAPzAjhWhVQtd2CZgK9-NJ_HDevP0U7UWd5Sz1KPGTAjDoi4TvXfRGs3LWTThRfbGZCj0hMhd9Z0mmiFLC9pldwVYkYt37oZUPdOvxwT32n9dR4s1tSamxx8quI9ZAClSoFrFY7ALgiA3lZvY0UJHKGOWgwtd02xendOlWPOFss1J2NQaP5Zx8r058-R8lMPBAU2DB5KRewSRVXDAva9i6qQkoMyfEnhm9cqIyP2L5wb5D5yPdTQiCXKWM3rhlW4BrdSmQ2Mx94UBv4pGQ9dGqyWWW5cz8puSsybSrbR1rih_6vqWcK_JQm9SgR1Ch1bW9ZQdIRADlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز: وقوع آتش‌سوزی در یک کشتی حامل مواد شیمیایی در پی حمله‌ دیشب در نزدیکی سواحل عمان
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/18005" target="_blank">📅 16:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18004">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">سنای آمریکا امروز (۱۴ ژوئیه ۲۰۲۶ / ۲۳ تیر ۱۴۰۵) قرار است درباره لایحه اختیارات دفاع ملی سال مالی ۲۰۲۷ (NDAA 2027) با بودجه پیشنهادی ۱.۱۵ تریلیون دلار رأی‌گیری کند.  این لایحه بودجه سالانه وزارت دفاع آمریکا است و فقط یک بسته اضطراری «مربوط به جنگ با ایران» نیست، اما شامل ماده‌ای به نام «ماده ۲۲۴» است که همکاری‌های نظامی، فناوری و صنعتی میان دو کشور آمریکا و اسرائیل را در حوزه‌هایی مانند هوش مصنوعی، جنگ سایبری، سامانه‌های خودمختار، تولید مشترک تسلیحات و تبادل داده‌های نظامی گسترش می‌دهد و عملا شریک میکند ، همچنین یک نماینده اجرایی ویژه در پنتاگون برای نظارت بر این همکاری‌ها تعیین میشود.  منتقدان این ماده را گامی به سوی «ادغام بی‌سابقه نظامی» آمریکا و اسرائیل می‌دانند که حتی از همکاری‌های ناتو فراتر است و به سطح دیگری میبرد، در حالی که حامیان آن را تقویت ضروری همکاری دفاعی با اسرائیل در برابر تهدیدات منطقه‌ای توصیف می‌کنند که واجب است.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/18004" target="_blank">📅 16:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18003">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">نتانیاهو: به رهبران ایران می‌گویم که به فکر حمله به ما نباشید، زیرا پاسخ ما بسیار قوی‌تر از قبل خواهد بود.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/18003" target="_blank">📅 16:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18002">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KSrJzGzK2QUrxdBGBbMsALNwUJgHznWdP_OlsJUJCqAHqKwfG5s85FAzq7Sp9buE5LBfWSDda78ccJgpaDF3eJ5M9zW2yvJfrky0pn3jxXKqEG8z0VpZxFXN-w5CuKswwZ0V2ubZOKKVEHoaA21bTSngQPEa2tuh9un-GGcH-sW82QflX5G8RyDuxdvTx3XKkQqpAC8UJ5XGt3Sy0rYmHRnUOyxLqlibN_VDko-I0mQaFWTMUmxM1VKU9JUsiFtHWYOrM-dsIouR7Xke5_MK_W6LRlo22L0jqBr2SJlhiHFfS563AQMaJy50izMIyIv1FCX93LWZCByNVkicNNvr6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار امروز رادار سمت اسکله باهنر به سمت شهید رجایی بندرعباس زدن کله هاش‌ پریده @WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/18002" target="_blank">📅 15:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18001">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2558677705.mp4?token=t3ZtAwa3UzIPXJcTXcahG9RgTbiUVRRA5fxHywKPmbiQvG0TucUEQ-SEmcEmtuxrb0hhOz1tClhCGmTZ6qDBUCYRuaxiY_Eq4K7NtUIWdnpBqqamF_lJKe0_opOtIOPUEX38xnbN-QoFnLQWUNuKK8ePeweqqxTvWoQYUosd8DKTHLU8jiEIti7To62pVFwHHg6bQWdQj9DzoUhElFcFM_TkqV_mkrPKSqXssylsp-rd4zOMO7RozEFwLyM5kb_GVDOphISzNBFKbubzw3kGp1SbUzW3pCo_xPKmOWKqv4ax3gsN5kU7cm3zuzKUcTM4V8ctU1h1IUZAfgNVhYv53A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2558677705.mp4?token=t3ZtAwa3UzIPXJcTXcahG9RgTbiUVRRA5fxHywKPmbiQvG0TucUEQ-SEmcEmtuxrb0hhOz1tClhCGmTZ6qDBUCYRuaxiY_Eq4K7NtUIWdnpBqqamF_lJKe0_opOtIOPUEX38xnbN-QoFnLQWUNuKK8ePeweqqxTvWoQYUosd8DKTHLU8jiEIti7To62pVFwHHg6bQWdQj9DzoUhElFcFM_TkqV_mkrPKSqXssylsp-rd4zOMO7RozEFwLyM5kb_GVDOphISzNBFKbubzw3kGp1SbUzW3pCo_xPKmOWKqv4ax3gsN5kU7cm3zuzKUcTM4V8ctU1h1IUZAfgNVhYv53A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عقل عرزشی : آمریکا ، بی ۲
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/18001" target="_blank">📅 15:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18000">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oCNey-D7puIc8_97vx7ONuv1ldehjI3OatOBWoEZIjKP1lKlfy3R8yzrO4wWh_zv4s0Cx37qg7OsksX1AOoLPwj57LSSZY4hDgUobEtJMj-aSidvcmg-IKnDLU8-7DDzqIjOqk2SUeZoHP6AmnqiXGKR-pTD_rii58VNmc8dtwR2sKUyI-1C8FBMtNmZG83RIsgbnGqltc_OSyvq6KAs5YioBBw2GD-ekJvhp86cddUmU-eymV6GA0Veu6ruYsD5CkK7Y_1kbBUtUrLdimDGHBBp9e42rF7IlKf_XzuAByMIyZDWswByhkib2RZQpa2ZeBX1cZttrWcH_jx-8W42aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار امروز رادار سمت اسکله باهنر به سمت شهید رجایی بندرعباس زدن کله هاش‌ پریده
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/18000" target="_blank">📅 15:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17999">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">گشت زنی پهپادهای شناسایی سپاه بر فراز مناطق مرزی شهرستان بانه از جمله مرز سیرانبند و مرز برویشکانی
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/17999" target="_blank">📅 15:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17998">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">فایننشال تایمز به نقل از یک فرد آگاه نوشت که مقام‌های کشورهای حاشیه خلیج فارس مظنون هستند ایران یا گروه‌های هم‌پیمان آن از توافق‌های رومینگ میان اپراتورهای تلفن همراه منطقه برای ردیابی نیروهای آمریکایی سوءاستفاده کرده‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/17998" target="_blank">📅 15:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17997">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f7Gnm3j6XPZez27tb_JHY6x2udE-1R18l4fyS_Za7MX34h7CI7oPuGxwdO8rmfAV71L0kr7GkTRwn3Td40X0fJgkQcr5XHz_nynVxMQRCV8x62lu2BCN_gfX_JVPxEWf6kghC21Ki_k6wHUmPlijYpcuDaX7HSOZt8c22Xj81mdEOrn8fl5d290UHCa5Wb0BNyeyZlzhw3dPb4_hu_G6SAhPoWQ_YxKk-Y0m0tPIxIqgzoqT64c5ClHBDaTW6qDfNNcZLzS_t4IX36fwkhw9BotoLWP83OtQPnKJ83Xx2PlQ14f8QxYk1uAyPA2jOGTCPuBHeCxKXoW45Mip6QKiLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دکل مخابراتی بندرعباس  @WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/17997" target="_blank">📅 14:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17996">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e96d03cec9.mp4?token=Vkfu_m9O6n_Ju9iulITY_9KkH3wwpPP2mJa5lhDUe4AclPBZ6_ihrzb4etNdKGBvt82GWF7Ow1yWKXFEZeyCgA_aOSipPi-8zghdWKlvsSJFlG6c0Dqv4XTXzpXvKU50U7qq_br7GMa_ly9HxH1OK3ZvvSGei141Ipapf1cgqb4JXvUhxg45qy0m1AEFikKzChXDUe5fC37ymvTp7s6w07fovtBk1xNYdjPvAJNEyrBkLiS1LQ7HdILDBQrePLUxJevpT8GKGFUz3k-FAl2R_diDIuFedmaNka3xv8TAIfDBPJ3Xkzl1lRHxm6ja4QcfrsXz4sGJHQki_5xCHtb7Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e96d03cec9.mp4?token=Vkfu_m9O6n_Ju9iulITY_9KkH3wwpPP2mJa5lhDUe4AclPBZ6_ihrzb4etNdKGBvt82GWF7Ow1yWKXFEZeyCgA_aOSipPi-8zghdWKlvsSJFlG6c0Dqv4XTXzpXvKU50U7qq_br7GMa_ly9HxH1OK3ZvvSGei141Ipapf1cgqb4JXvUhxg45qy0m1AEFikKzChXDUe5fC37ymvTp7s6w07fovtBk1xNYdjPvAJNEyrBkLiS1LQ7HdILDBQrePLUxJevpT8GKGFUz3k-FAl2R_diDIuFedmaNka3xv8TAIfDBPJ3Xkzl1lRHxm6ja4QcfrsXz4sGJHQki_5xCHtb7Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر ماهواره‌ای خسارت‌های وارد شده به پایگاه هوایی شاهزاده حسن، اردن
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/17996" target="_blank">📅 14:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17995">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">استانداری هرمزگان: در حملات جدید آمریکا به برخی نقاط استان هیچ مصدوم غیرنظامی یا خسارت به زیر ساخت‌های مسکونی و تجاری گزارش نشده است
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/17995" target="_blank">📅 14:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17994">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">بندرعباس زدننننننننننننن
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/17994" target="_blank">📅 14:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17993">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اصابت موشک‌های آمریکایی به آبادان و حوالی ماهشهر
معاون امنیتی و انتظامی استاندار خوزستان اعلام کرد ساعت ۱۳:۲۵ امروز، نقطه‌ای در شهرستان آبادان هدف اصابت پرتابه‌های آمریکا قرار گرفت.
به گفته وی، حدود ۵ دقیقه بعد نیز منطقه‌ای در حوالی ماهشهر هدف حمله قرار گرفت که در پی آن دو انفجار به وقوع پیوست.
تاکنون جزئیاتی درباره میزان خسارات یا تلفات احتمالی این حملات منتشر نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/17993" target="_blank">📅 14:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17992">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">لحظاتی پیش توپخانه اسرائیل حومه شهر قنطره در جنوب لبنان را هدف قرار داد.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/17992" target="_blank">📅 14:30 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17991">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1235858ce0.mp4?token=oLFw0Ouom0BfAffnRqZGVoLa-sIW2u-kBjrF2Q5f7TClC_pbYiYvcRjItoz_cRslIdxOQ17VFLggYgrgcUHTHYsm9sGIu7vRb7afEbzNfusI9RAm4h2IlzZ4f9Nh5eYGOnuywElJYXAsxz5iZskhm3ItKuc0M73tkgQep0FZO44HTgSt3SiLHCw06R1uSxa_DSrG0qPrcSK3cwigID8lSwE6IIU_JfCVoo1WvxIG5Sx3z1MxTS1fN4K0-TNEM5px_V0tCwtsR4amqH9b6EqlcVqx-m6WmTieZ2IoVkMCSFpEF_LsmGg-FxpH3kR-0RKMQx243EswG5mR9fc3Y75lew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1235858ce0.mp4?token=oLFw0Ouom0BfAffnRqZGVoLa-sIW2u-kBjrF2Q5f7TClC_pbYiYvcRjItoz_cRslIdxOQ17VFLggYgrgcUHTHYsm9sGIu7vRb7afEbzNfusI9RAm4h2IlzZ4f9Nh5eYGOnuywElJYXAsxz5iZskhm3ItKuc0M73tkgQep0FZO44HTgSt3SiLHCw06R1uSxa_DSrG0qPrcSK3cwigID8lSwE6IIU_JfCVoo1WvxIG5Sx3z1MxTS1fN4K0-TNEM5px_V0tCwtsR4amqH9b6EqlcVqx-m6WmTieZ2IoVkMCSFpEF_LsmGg-FxpH3kR-0RKMQx243EswG5mR9fc3Y75lew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش سوزی
ساعاتی پیش فردیس برای یه تعمیرگاه بوده
یاشار : چه تمیرکاه پرو پیمونی هم بوده حتما همون تعمیرگاه بی بی بوده که ماشینارو دستکاری میکره
🤣
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/17991" target="_blank">📅 14:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17990">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">مذاکرات بین اسرائیل و لبنان در رم آغاز شد
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/17990" target="_blank">📅 14:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17989">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">در طویله رو باز کردند با دلار ۱۸۴-۱۸۵ هزار تومان  @WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/17989" target="_blank">📅 14:16 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17988">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nx819Xy9frFeag7gpueDV2iMH5n1XoAelmGfuN5YIVIh0dk_aYhHgZczwFZUSrM0AWR8dYBWrxTq8RW1PRvLZFvwdQvRVE5n8LZ75Qot2LxHZEbBuSAm3Ym7dfDtz4BR6MAxSUQ5ipRv_ABWf123QcTeYRGuUHAweV-SdA6HAX67iAaeH7bPy_Tc0lhiNRQQK5yiZGp_B48WSYKTpI-EnoXXNJWspCFjT38d6z3wNeTMCl107PPa4f5vTbd-OE6VJtTWUEj4qxAb8lmzvwDXj1boaso1PF8poi1ilKVJ731HmdV5i_cKEwcarvsU6ckegqFhwJZH9-HYxfHzdZ8YNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا آتش سوزی شدیدی در فردیس، جاده ملارد اتفاق افتاده.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/17988" target="_blank">📅 14:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17987">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gtCx_soyGRnZOAytsUAkIgCzfhL0WQuleCeBMJ_yQ3OReohxAABsNLZ_Y4LV5VVuXUD_Y23r5HBBvD1iACCN0M4BpXJwK1A7x9X4egJlhQCAsg6RJVBb2GzpWzbou2z5z84j7kBe1Jf4haseVpK8dCCu1VlFcmQFL-iIXyWkPu_ZC30vfUHuVVPy4UL-XCjge-vXqJB5W11pK8i4_gxwvs2Em7NXs5QUS-_3J7X33z5woIGYZr2ynvGPEzhgwF1aBGrKO3FsZpCJZLAYOPn4lmUDtgKWjZJZ_RSttIO4XLWo0mC96Abt7oUqAkbfATxPKqoOSCyzgo_KLoDSJkKqDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقر سپاه ، خورموج ، بوشهر
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/17987" target="_blank">📅 14:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17986">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJVGX7lI7CRwd-z3yhGnPnywPkb1-EFDRzc5rraQ_l11fKfMn9QloKCLBeVnPDfLDdjWM95aYTsY6VlTUtSuzvac58t6NYV7pILkEo6N65OFaf5YVoo6E40uztOzg0o_4X97HEhn-bzePc62VtwzIBUTyGZBAKyeEYeMCcoSZtH_MJ6MK5ba7DSpgHmIYHFVcCiUuIDDEhw8xU3IrZsBc5_r7wvk3u5Sgz-DxITgI1-FXcTwFNEe4cnNukf9sZPMX8ZxkQmP-uNmk2LU_gA0j1zDaTpk_k6M-fm1grPufPUK2uCAQYU0CJA63lxa80w6kiRpFPybJzUH3U17ywSayA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بوشهر @WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/17986" target="_blank">📅 13:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17985">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">خبرگزاری صدا و سیما: یک حمله هوایی آمریکا به ساختمان سازمان تنظیم مقررات و ارتباطات رادیویی در بندرعباس انجام شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/17985" target="_blank">📅 13:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17984">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KyYsmy2pJcbwTHhfYJfKGAukHDz2PylV017T7cOLU1JhNtFjPotbJulnF3DNEQqAMaZKSCUVfzzR0-oLt5dhx_2_JBXmjPvw50poj6w1E0WeI6sE0dZQxI3wSxDK1ldfAqRyNT0sGpqTkigDYXT58I_ZNaHihiQSDC61TgD9OHXzOOv2fZZdsSnvBqIO1wroapyJP4f0aiQVApffA8T6zk09a5ONPiGQztih6RETMOr0eD1YPLjkbyWCZs26yulBH_ZtzeSTJLIS2wK_UR7SHQ5DW408QrlKORTBBGgNit62VtY2TcnDushydfr-oeJGqSxW7HZ-R-HjNMvknVfU6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بوشهر
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/17984" target="_blank">📅 13:35 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17983">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3796203d13.mp4?token=QfIQtb01Bav7nbtCLmNyLsAs0t_D9o_v1bvr64zhd9AvwrpbhVN3l1qDf9ZWtzttKQzjw3_nQtAWsY70uSX0-X7J2xjlDvin0Uvnd5eDGHQJ_ieNVujeK9pCxn1D5Wt9onFEJJ-oPPBZiIiacge3k3riNTTFRkedtJXuPD2kPVgkRVwz6PKUNQI76dq6jyWgJuXW8i_58DZ3gVJWXSDULARj7_GZUeCSsgkdslz-YMr4tlJlY-hSJW_qlxseQX3F3cFm9T-y3auVmd2Mzn7KpmgHdwvrQvOp_h6qAUOwaHDLChf92iBKrhf8d6SPGZlvS1JCgbtEyqZo3psU3rGYxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3796203d13.mp4?token=QfIQtb01Bav7nbtCLmNyLsAs0t_D9o_v1bvr64zhd9AvwrpbhVN3l1qDf9ZWtzttKQzjw3_nQtAWsY70uSX0-X7J2xjlDvin0Uvnd5eDGHQJ_ieNVujeK9pCxn1D5Wt9onFEJJ-oPPBZiIiacge3k3riNTTFRkedtJXuPD2kPVgkRVwz6PKUNQI76dq6jyWgJuXW8i_58DZ3gVJWXSDULARj7_GZUeCSsgkdslz-YMr4tlJlY-hSJW_qlxseQX3F3cFm9T-y3auVmd2Mzn7KpmgHdwvrQvOp_h6qAUOwaHDLChf92iBKrhf8d6SPGZlvS1JCgbtEyqZo3psU3rGYxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صنایع دریایی بوشهر
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/17983" target="_blank">📅 13:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17982">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">خبرگزاری ایرنا گزارش داد: به گفته معاون استاندار بوشهر، ۴ نقطه در شهر بوشهر مورد اصابت بمباران دشمن قرار گرفته‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/17982" target="_blank">📅 13:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17981">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KO-DQMFVKhoanaitKOMeSRVV-ffzloexcjkIATz20666_RO0Aqv1q35iL-1u52sxz8z9FD7k8HerDwBkJ4BtD4TRFnX9OFhblUESS9JzIP53yUr8NIX94CiB-tHvEhAqrFNAUoapARTKeSsUKYUalbcc5aaSDyLkyriSjgQO2mD-dZ7J-CCyknSEVFmX6EhkKj8ZViG9RNHu10WCk9oq6B2tdBhs-iRbBrigy5VnORtQfS_q97-U8OteXdbxr4TIqVDpE0_1EsG2Au0G6mQYkg6tHQoIURoBqW_d9lcJhYyIEP7EivnBUj_weOMhSuTXe2gWXSSm9EJpfQrwo6EtQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بوشهر!
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/17981" target="_blank">📅 13:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17980">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VtD-03I6o6L2XFMEiWG7mDayxxUC9_UC_A6w4sHLDjzBoqq0FeFpIEuCvbsfMbpmZWlyapuVjsIGkHm5eeTKYQwhkK-cMZ43kAlp-htfD9o1_-cPwLse-X4FmQcXlF1udSiATk41hS0-XY3dM7i_dewwatJxZ89FlZuqxPL-vqVMQZ2lnM0O_U1cftAwk5hbv9o6MzvZeThwoKuGn1hoI32UksN6k0n-1JKMVIkdgUlZl4s0U7qELIJpDEttZn6ox8fgeAR49GnG5kgVaAX93loZ5dS4sRZ2XFNzIuogEtijsWS88sccLlk_aApfxr_eEvjThb79RJtslXY-ebjrtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در طویله رو باز کردند با دلار ۱۸۴-۱۸۵ هزار تومان
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/17980" target="_blank">📅 13:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17979">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">پلیزززززززز</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/17979" target="_blank">📅 13:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17978">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GcqeX4ocaLAAd4bneWK_h82_9rxwoAN183KSfG4pI_xkk7Wwg5BPtKsQG6QBlEWoBwslhuIGIdMuKnXenl9oh09Gbp1KIB-mfEdNzXWxTd58prlhBBiwdH0SwLdADVsD0U-ax4qP4WYEDtLkC-1fuVpx4Q6E_ln2oHiFfwJcTXKBAnQWCUROO_NtPwwuyFgbWYMox-gIPcf9qoy0ua_zhV7_4sZG1gQxcIMYTdJBMqM54lmZp0mRWvOUfsDkoQJtDX9gj09NhSX0YGJrhrhuAmcvUa76eRbKObKeWX5rwFVdE1ALbGnOe00zIDz0YLZ-05QsrLVJ_vQiYGOCe1NkFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کارخانه جات نیرو دریایی بوشهر
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/17978" target="_blank">📅 13:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17977">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf78206044.mp4?token=pwfGOhwIngTqMkavTy83rMXFKvVj2UYfgnX0Rf3GxV6DMXR5ukYeiNnBWrgKWzsIUFSDsvLQUhK6PEzfx6L2NhPeRHjeylkjl6cmr4EUqf7IgTnHn6TAd3G5T64iQrGyeK2JlGDZZk8l1FH4AdGmQFIBHrIjWXkmcPHBsZ7JZgxUzMXF-Sr5oQ2c6qP6qqsVLrclHmJVqsmV86GEcnir8XObo5b2JLyctpmyazdOl-msDeRWkscPwosIDGAuo_zDqbuKl0MXW16n2ROEdbUOIEmrgH-sYCQtXNKptLwgbpl6OtTP6BVSvbtM_3sWuPk6ZloO0nsuicy5n4IYsJQGGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf78206044.mp4?token=pwfGOhwIngTqMkavTy83rMXFKvVj2UYfgnX0Rf3GxV6DMXR5ukYeiNnBWrgKWzsIUFSDsvLQUhK6PEzfx6L2NhPeRHjeylkjl6cmr4EUqf7IgTnHn6TAd3G5T64iQrGyeK2JlGDZZk8l1FH4AdGmQFIBHrIjWXkmcPHBsZ7JZgxUzMXF-Sr5oQ2c6qP6qqsVLrclHmJVqsmV86GEcnir8XObo5b2JLyctpmyazdOl-msDeRWkscPwosIDGAuo_zDqbuKl0MXW16n2ROEdbUOIEmrgH-sYCQtXNKptLwgbpl6OtTP6BVSvbtM_3sWuPk6ZloO0nsuicy5n4IYsJQGGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بندرجاسک یه لانچر رو زدن
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/17977" target="_blank">📅 13:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17976">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nqq5-kZcz5KCJyuzdTBoAuhWJu25IV6351Liw8kWY2Vz3HBrwCTZYtBKePWh84MkdObd3Hcwzf6eVWlhrSTm2EBpu02rZPomyzjodC12Wf0z4blSPdvgqZcqaw43qUhkJmwfLkQk1XHs0HSwND5R62qQDjYzSaj1ghnpqnEAoAHd0CITvfTVa5tNaBV_t7m4gn0zs005UZ9fco8RtrJGiY1nscQPBgAcNvWTZbV156xrDRH6rqS7wnpVp0rRKarRVIc8oWiMcNLTvBaKYGyqKzM4D_NsQb6AL3kzq5Efy9TVUE1geIg4Lq2zw2x5aMQl-Su0-dbt7X9-tnORkjcEsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بوشهر نیرو دریایی
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/17976" target="_blank">📅 13:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17975">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50c41ba639.mp4?token=EF-fLyOCrObtMSjo7N2vU0xdyVFo5UTzLBeh1b82ocVysTW5RK-s34pBYckO7-n1zHwtrGbCZgnf-9GPOP8ueslvDOS-K5VZw1U4HahDs5wfdRdCK6KJHdg7h01WaCy7VjO7AbLN48bgASf_AaFjVvxMlLY7KK4Fq1gCTqfJWRssvVKlsPT3fZqPwVxqp1kdMU2xfSxtrP2htFc6knAp0l0rnSIuOSsx55PiBm56wl1pnFik9Hf0MsfDdKqgbWErQxJbKLLHnK0AiBqor0Z3QVw1oBDWIfdpo0oJGPMxPnTrwbJ-HL3Riskei24bn2CI0O7Vmr9aA8v5Cn6lLiZbwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50c41ba639.mp4?token=EF-fLyOCrObtMSjo7N2vU0xdyVFo5UTzLBeh1b82ocVysTW5RK-s34pBYckO7-n1zHwtrGbCZgnf-9GPOP8ueslvDOS-K5VZw1U4HahDs5wfdRdCK6KJHdg7h01WaCy7VjO7AbLN48bgASf_AaFjVvxMlLY7KK4Fq1gCTqfJWRssvVKlsPT3fZqPwVxqp1kdMU2xfSxtrP2htFc6knAp0l0rnSIuOSsx55PiBm56wl1pnFik9Hf0MsfDdKqgbWErQxJbKLLHnK0AiBqor0Z3QVw1oBDWIfdpo0oJGPMxPnTrwbJ-HL3Riskei24bn2CI0O7Vmr9aA8v5Cn6lLiZbwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بوشهر صلح آباد
@warRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/17975" target="_blank">📅 13:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17974">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FsGuhR_SQbcVEovR1AEYpK6rdCM4PcywEtf_9en4o_CY4A-oPVHnT7kj22cxYKBbbuIu1FTl_vAoLVJLkOMmhdehV0F97Lj5jYtw8fZRkW1owKR4oKIk0GkGnU3VLSeorinMWqxl9AnFAob9QmaeT6lrGsVRYiJkeyAD2RmFt1V3jYMGzeEShW7Gncu2dxS_5CjtKjMzFPu_-K6rg53OFRia0wRjVPZ0SD1o55lYcRu0qb9yO5kRftsz2L6GYxKeQrJn9df3SWwfxadjXtELQNWM4XrDUkrfewQopBu8sO62r6WzpNelHXi8OGRmwyQzOT0OCLC2XZ1nGDN1kYuu2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بوشهر الان
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/17974" target="_blank">📅 13:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17972">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bcszrrfVwwQdW6oEtoUArecN1HV01Bsc2QHLE7kEihvYeY5imkDZQql336zfjpu943SD8qYbZe4dXdi4z11U2oY9NpnhAsS3VzeY1DakGqA1mSI1BfB-1Dfd1wJLsWSujsgY4lKQCL41mgkyg6oWCG4mYlEMkHoh1Vn0zd_jH9UNVIXpdJd-6bbOXFWxPm26FFs784W7xA0DYerz-YTXSJ4hhl6ZYAhjcancOY_Z6G2IPHcuyBf1rRS3LZTfotA0lfgQ3uoV5o6MKAWTGfZhbo88R4rvPe6gPBKJ7K79vIYnntl0zoB2IrSIVXzGt9PSj-fq1gL1s0M5OnZ6wOVKEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BTcngc10YI9s6lULhuxABU4va_UQqFV6RnemMA1R8f6RRvaCI1CQqyFW6edUtVYx3g5hXBXn037uebeSKflQBAjFfdJRukYBBQjEGtPuBjTgw9vHq3FdKIu0ALcqcOaV7IFdW1y34rvtF3INZO-QToHfcCeK_Y0qZQu8hmyxKgc7hIEmCKEDG3_OKh0VafF6hANKt0BwaFfB-8nZIfmyIFH4WseGQ5-Pjgsw3IaXpjUQnrj8QNE6T5x2acpGF9GoMoN1Gt6Z8S0bRVQuYxfv9yTg3KYsQ-iah3Z1amcJH9nHshorFdi3f9hk7SlUwJaoUMMJl2cVunzU8PO5akKS7Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بوشهرررر نیرو دریایی
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/17972" target="_blank">📅 13:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17971">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t941yXwqZwgKEK74Fb9Dg-VKb6eroWxNQXJytk-rRI2Y6GJKt4ND82QAI_UN2qhmFORLhs5KvHimxPbmeo6gc7aqojVQVHy6SLeagXPiIxLXcnDvVKQetNEjb2pDY6DGvETIQRn934DJ6i6gpSZ7sa4dUbuyZG6DXjq3rKMlQ87Vk_VKW-Tp0gSBj4BKy-Uy7ce_AcuX8CPdCSkM2zPPNUgOpLf11aVx_463gnT_901cDA0GnEjVfB61Cuj1wOzZFaM6mzVkzzX3riiXMqPl_Kk-mS_4oHEIK9pn3LNXOv5wN8OILtE2KDJ415pzoZuYmvk3RbjUTmapOHK5ZYE7XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و دوباره صلح آباد
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/17971" target="_blank">📅 13:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17970">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">دوباره زدن صلح آباد بوشهر سوله های‌ پهپاد سازی
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/17970" target="_blank">📅 13:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17969">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/np1fMUDfuSHXtL9IChovGY6xKVQ5CI73wEx8cKNzexS9EakvvIvGDdK_JN_St3orCqofeb5eSXwo6kmYRQjmmypqieLBOhqhLHKG_SKWj5y60U75U-2uL0Bj8Msb6xeTK9_hl_aJjetJd2P-Hfr7MggfaNuMyqgmROUbi3mYGn2PAtFwgmfE_OMAR-PlNo1IuKB70vHjyg00hyDsz58fYw18A6fD_P3HA76e0S-GwQsJYJqDK2x8u_yKOO2RN80-c0Av6rdADV_rj6Qsk6_wy-DfYHSExgfXrg03juyOtBUGwmpTkewP6zuAaVbSRx4Rt1i_1A31g9mxOh7-asoHAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بوشهر سمت صلح آباد بود انفجارا</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/17969" target="_blank">📅 12:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17968">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">3 انفجار خورموج
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/17968" target="_blank">📅 12:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17966">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">صدای ۱۰ انفجار بوشهر
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/17966" target="_blank">📅 12:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17965">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">خبرگزاری صداوسیما:  دقایقی پیش؛ صدای ۵ انفجار در غرب بندرعباس شنیده شد
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/17965" target="_blank">📅 12:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17964">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">وایچرت: بن‌سلمان خود را برای جنگ زمینی آمریکا با ایران آماده می‌کند
برندون وایچرت، نویسنده و تحلیلگر آمریکایی:  دلیل حمله سعودی‌ها به حوثی‌ها این است که
محمد بن سلمان به وضوح می‌داند که ترامپ به زودی قصد دارد حمله زمینی آمریکا به ایران را آغاز کند
.
در آن زمان، حوثی‌ها به هر حال به سمت سعودی‌ها حمله خواهند کرد.
بنابراین، محمد بن سلمان در تلاش است تا پیش از آنکه آمریکایی‌ها نقشه دیوانه‌وار خود را آغاز کنند، به طور پیشگیرانه شرایط را به نفع خود تغییر دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/17964" target="_blank">📅 12:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17963">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">کمی‌پیش شلیک از ایران و هم اکنون صدای انفجار مهیبی در بحرین شنیده شد.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/17963" target="_blank">📅 12:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17962">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">کان نیوز: ارتش آمریکا هواپیما های سوخت رسان خود را مجدداً در فرودگاه بین المللی تل‌آویو مستقر کرده و برنامه ریزی برای بازگشت سوخت رسان ها به اروپا را نیز لغو کرده است
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/17962" target="_blank">📅 12:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17961">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ترامپ درباره مرگ لیندسی گراهام:
پزشکان گفته‌اند که یک بخش خاص از بدن او به معنای واقعی کلمه منفجر شد؛ این وضعیتی است که پدرش هم داشت
در پاسخ به نظریه توطئه، دوست دارم بگویم بله، اما فکر می‌کنم او مشکلاتی داشت
@WarROOM</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/17961" target="_blank">📅 12:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17960">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ارتش اسرائیل: نیروهای ما به عملیات خود در جنوب لبنان ادامه می‌دهند تا در برابر تهدیداتی که علیه اسرائیل مطرح می‌شود، مقابله کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/17960" target="_blank">📅 12:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17959">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">وزیر امور خارجه عمان: در حال حاضر، مذاکرات پیچیده‌ای در جریان است تا یک توافق بلندمدت حاصل شود که از آزادی تردد در تنگه هرمز اطمینان حاصل کند.
ما مسئولیت داریم که با ايران و جامعه بین‌المللی همکاری کنیم تا به توافقی دست یابیم که آزادی تردد در تنگه هرمز را تضمین کند.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/17959" target="_blank">📅 12:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17958">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">گزارش‌ها از حمله به سفارت اسرائیل در بحرین خبر می‌دهند.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/17958" target="_blank">📅 12:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17957">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">وزیر دفاع فرانسه: ما برای خنثی‌سازی مین‌ها در تنگه هرمز آماده هستیم
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/17957" target="_blank">📅 11:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17956">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">کانال ۱۳ اسرائیل موساد اسم روز محمود احمدی نژاد رو «گربه چکمه پوش» گزاشته بود  لحظه آخر توسط ترامپ متوقف شد و نقل‌قول‌های تکان‌دهنده رئیس سازمان اطلاعات اسرائیل (موساد) ویدیو ۱۰ دقیقه ای تا دقایقی‌دیگر فقط از اتاق جنگ با زیرنویس فارسی….. @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/17956" target="_blank">📅 11:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17955">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HPeSR0F4WgtarXAUnnwP85zHYeLfFBuRvxSq6ede_r9rEjNa1YPoDXTtlm-ofoKPfsyiKbxn1hZNdmXauDiSLWfJ2Am5ZBIBHbMgcw2tiYC1IfTX0CIM6HxZ7fQTippvjw9LjQgkVCiNIZFsNvylR-nLQ5-u76i_S2czb48XI5GTludkmSfjFcTRpd7G_4FnPmLahaJ-zolNsofi58jRW5xHmGMY2g-l7Z9N3czAY6hpxte1gtTCxQbP-P_71VsDKJSSzeNITCIdn80apoPtpjrIQYGOTJPd_Wj35ArjNQmT3nIXly7wiao6Slwj1PDqj_F29iDF-MlmfVrICo8cqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استاد بیژن مرتضوی، یکی از بهترین نوازندگان ویولن ایران، قراره در فینال جام جهانی فوتبال ۲۰۲۶ آمریکا، همراه با گروه ارکستر به مدت ۱۱ دقیقه اجرا داشته باشه! اون هم در کنار هنرمندان بزرگی مثل شکیرا و جاستین بیبر. تبریک میگم استاد؛ باعث افتخار ایران و همه ایرانی‌ها هستید
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/17955" target="_blank">📅 10:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17954">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iU4qTDRqfGjbSlq58N0dGgUgAiOGehzzNLtspOEbLZN9z6hGrvN1MtQV0FegMUesLXOV0TsAwSjNgwNexlNygenIkug1UgKfyXP3ffp7o_ZgrVoJTM0vk8bkxcYIxNr3ZG4H2Y3cay0FfkjLk_GMhrJpdcjfhJQa6l43hiOkjPC1jph_0VUO_vtrV21UovDGFHWEW2F6ZoTzMrDuzz5cHMXPwPvER-3JxsZSVG5_zz1XEF5GzV-MTjiOcoZFhr7Vrg6YyLhja-LZaOqwkoVP4o1W4F98pz3mDUKpU0fEstzYe3vuUWAVAptSa0NLjY1tADHzDFysy-v5BRvx549mEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوه کلنگ
(یا کوه کلنگ گزلا) به انگلیسی PickAxe منطقه‌ای کوهستانی و مهم در رشته‌کوه زاگرس مرکزی و در نزدیکی سایت هسته‌ای نطنز در استان اصفهان است ولی کاملا مجزا . این کوه به دلیل ساخت تاسیسات زیرزمینی هسته‌ای در عمق ۱۴۰ متری زمین، در ماه‌های اخیر مورد توجه رسانه‌ها و اظهارات مقامات سیاسی (دیشب ترامپ)قرار گرفته است
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/17954" target="_blank">📅 10:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17953">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">وزیر نفت ایران، پاک نژاد: صادرات نفت ایران ادامه دارد، علی‌رغم لغو معافیت‌ها از تحریم‌های ایالات متحده.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/17953" target="_blank">📅 10:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17952">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">صدای انفجار شنیده‌شده دقایقی پیش در اصفهان، ناشی از انهدام کنترل‌شده مهمات جنگی بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/17952" target="_blank">📅 10:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17951">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">خبرگزاری فرانسه:
صدای چندین انفجار در بحرین شنیده شد
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/17951" target="_blank">📅 09:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17950">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">بلومبرگ، بر اساس داده‌های ردیابی کشتی‌ها: تردد دریایی در تنگه هرمز، از اوایل صبح روز سه‌شنبه، تقریباً به طور کامل متوقف شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/17950" target="_blank">📅 08:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17949">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">سپاه: در موج سوم عملیات تاسیسات مهم و محل استقرار دشمن آمریکایی در یک پایگاه هوایی در خاک اردن را که از آن برای حمله به ما استفاده شده بود، هدف موشک های بالستیک قرار دادیم
.
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/17949" target="_blank">📅 08:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17948">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">سنتکام : پایان عملیات امروز در طول این ماموریت پنج ساعته، نیروهای آمریکایی با موفقیت به اهداف نظامی در سراسر ایران از جمله بوشهر، چاه بهار، جاسک، کنارک، ابوموسی و بندرعباس حمله کردند تا توانایی ایران در حمله به کشتی‌های تجاری را بیش از پیش کاهش دهند. نیروهای…</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/17948" target="_blank">📅 08:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17947">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8fdbd7112.mp4?token=MS7UT34xLG_bmkvBl6KKWGdGeWR1Lec2Dzx1Wzmr6nAFSXAZbAHRSAEvwgCGeG__Zrg-We63Nqj5fJN0LNA3SD7cr3DLbfgsI11dv08Y0NoynUQG6l3_WB8EXIQ470YIdk1wihh0e_xKfdh0MH7DpJQV8xVmIDWDDzoF-C6pnlMLIAAhI-hmuusxerUafiOqx01KvWw9-iIU7MUPT6gM2CV1H9F5eJnGnp--lQLx3mdVE67FW0dTCxmd5Df7qTLpG0a7dt3Xqg4g5VGOZReUD10NjMLuSELXzDn3UxOjL_d0uqnG7FJHk2ZMWCyHjlhUkBHMY57tUUkmpmgI0gPpvWHuUH_Ycwf5iwns2FMw8p0FFzBwRFbpZIs8dEk3cibX7JripNaPGH5gYt-8frSYv9LnNF_rDYjX6wBY0Mh6mXzMitQpwsjqeefH42RKSJJrBORQqUkeJRj0tbu-PIojXEAinQYh8yB5J2fXJ_PavlnkkEUetKvAOlnpS5cBgySELrA8GVOEwG9ZVBkARDKj9Pvd0r_eirRV8_uAfXMFBsLBPjfBjqTWCdVCbWPuP4T0HWeAesw1Ktn12wAfo1MF9werub0p0JHBt1vt7N-3NYrKdwq8agoxrWyRnQ_2LQIltHIxeg6csOzsmW9B4_5nlJ0QzlrixU2aPfm6zQNQNDo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8fdbd7112.mp4?token=MS7UT34xLG_bmkvBl6KKWGdGeWR1Lec2Dzx1Wzmr6nAFSXAZbAHRSAEvwgCGeG__Zrg-We63Nqj5fJN0LNA3SD7cr3DLbfgsI11dv08Y0NoynUQG6l3_WB8EXIQ470YIdk1wihh0e_xKfdh0MH7DpJQV8xVmIDWDDzoF-C6pnlMLIAAhI-hmuusxerUafiOqx01KvWw9-iIU7MUPT6gM2CV1H9F5eJnGnp--lQLx3mdVE67FW0dTCxmd5Df7qTLpG0a7dt3Xqg4g5VGOZReUD10NjMLuSELXzDn3UxOjL_d0uqnG7FJHk2ZMWCyHjlhUkBHMY57tUUkmpmgI0gPpvWHuUH_Ycwf5iwns2FMw8p0FFzBwRFbpZIs8dEk3cibX7JripNaPGH5gYt-8frSYv9LnNF_rDYjX6wBY0Mh6mXzMitQpwsjqeefH42RKSJJrBORQqUkeJRj0tbu-PIojXEAinQYh8yB5J2fXJ_PavlnkkEUetKvAOlnpS5cBgySELrA8GVOEwG9ZVBkARDKj9Pvd0r_eirRV8_uAfXMFBsLBPjfBjqTWCdVCbWPuP4T0HWeAesw1Ktn12wAfo1MF9werub0p0JHBt1vt7N-3NYrKdwq8agoxrWyRnQ_2LQIltHIxeg6csOzsmW9B4_5nlJ0QzlrixU2aPfm6zQNQNDo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امشب  @WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/17947" target="_blank">📅 08:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17946">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWarRoom with YASHAR</strong></div>
<div class="tg-text">https://t.me/boost/withyashar
امکان ترجمه اتوماتیک و ایموجی‌جاوید شاه رو از دست دادیم یه حل بدید ، اگه پرمیوم دارید!
اگه ندارید به دوستانون بگید</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/withyashar/17946" target="_blank">📅 03:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17945">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">منابع خبری از یک حملۀ سایبری به سیستم‌های بانکی بحرین و ایجاد اختلال در آن گزارش می‌دهند.
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/17945" target="_blank">📅 03:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17944">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">حملات جدید به کیش
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/17944" target="_blank">📅 03:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17943">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/deE4zGFiZjd-WJ1J6Bb5kC9U7z7X8y_HybZBdKna4Jka7glkgFpwB6HzT9aue6BQlO6P-sgjqBokKmd6cmvmJCkCrx_s9W4RQp1ycNgQpiKBrWEYRAbhUM7qVlvPPuHBVYeXuoNImt02gW3ZwOVRENjxtL91PYrCtxFttc9Dn20sN3JNRol88acYDI-tr1w7VHSWd_xXObLn7MvDk4doWtoHs8Zzd8c99MFuxhbMFq_oe4rSwG30_KT3silKSQnzpkz6m3iajvZalIAlGralQc_XcxAoaTMtf6dzNqCJje9h1tajsXysD3kuheHpX7DQpX9qHMPAgfrOciBvJmMatw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک فروند هواپیمای سوخت‌رسان KC-135R Stratotanker نیروی هوایی ایالات متحده در حال بازگشت به تل آویو کد اضطراری ۷۷۰۰ صادر کرد.
۹ سوخترسان دیگر به همراه هواپیمای آواکس و پی ۸ همچنان مشغول انجام مأموریت هستند
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/17943" target="_blank">📅 03:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17942">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">پایگاه هوایی بوشهر رو صاف کردن
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/17942" target="_blank">📅 03:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17941">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">اسرائیل هیوم گزارش داده که کشورهای عربی برای از سرگیری دوباره جنگ با ایران چراغ سبز دادند
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/17941" target="_blank">📅 03:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17940">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">سه انفجار ماهشهر
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/17940" target="_blank">📅 03:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17939">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">دو تا انفجار بندر عمام
🚨
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/17939" target="_blank">📅 03:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17938">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">منابع عربی گزارش داده‌اند که مقر ناوگان پنجم نیروی دریایی آمریکا در منطقه الجفیر بحرین هدف حمله موشکی ایران قرار گرفت، همزمان با فعال شدن آژیرهای هشدار.
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/17938" target="_blank">📅 03:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17937">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">انفجار‌ سنگین الان بوشهر
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/17937" target="_blank">📅 03:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17936">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">۳ پا به بحرین جمله کرد ، گزارش صدای انفجار
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/17936" target="_blank">📅 03:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17935">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b813cc8e47.mp4?token=fTywFg2t7LgyUAtDMsbfwHePitUrKU4vSbV5yAt81b6by5VhFidNx_rchgwQo4VnywnLlE1H2pIE1K2jQO7D6dCy0bXWaZwJvqo-Bw9QlYvn6MASC204i6spw9IxgG8q3tDaKsOL1aIkIX0Zlk9i-0olhcoYIe7vhkk_z440DeWz2UOXRKSlQUxKPLmOxERGKxbWZTWthJ-_R7uq2upbamzdCZkaVAwGHOnDuhkempS-mebsp8jBxwC0X29IiV1Em0Wst6P_nqiDg52EXZHi99lBshxIJ1G8fA6o6Wbkgc6kdCqaSye8Q48UixEzxVnhZ4VxtajrBXf02-t3PCgzig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b813cc8e47.mp4?token=fTywFg2t7LgyUAtDMsbfwHePitUrKU4vSbV5yAt81b6by5VhFidNx_rchgwQo4VnywnLlE1H2pIE1K2jQO7D6dCy0bXWaZwJvqo-Bw9QlYvn6MASC204i6spw9IxgG8q3tDaKsOL1aIkIX0Zlk9i-0olhcoYIe7vhkk_z440DeWz2UOXRKSlQUxKPLmOxERGKxbWZTWthJ-_R7uq2upbamzdCZkaVAwGHOnDuhkempS-mebsp8jBxwC0X29IiV1Em0Wst6P_nqiDg52EXZHi99lBshxIJ1G8fA6o6Wbkgc6kdCqaSye8Q48UixEzxVnhZ4VxtajrBXf02-t3PCgzig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سراوان سیستان و بلوچستان
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/17935" target="_blank">📅 03:02 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17934">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ca7de4eca.mp4?token=h12RxLKgZ8C_1ajHIaJ1KIWVaD0k1q7f-2X-vs4AMuI7XJV2LrRkhoQgd3-rcQN6xzARh374_UGfEYA9V-eS8Y9DAwLspXm17HuhDZzs6LMfrZL8MZ1HpBopTik5EPuCyaw_2Ll9m01ysIOK7-jVPZOZoIucn0A_hldJM0GGn0zGwkIFHWcBTcUoVnxPuPP3O1-BIZTVNHvDc7nIGuz49iQkqMcmD2eBGNsVm7uQkAeYVtmDG41ezQQShBMxTeB2oeDT3qhhDPLGjycH-COxosrSUWDr5p0Usd2e6A65RhFVwCCQYL5h_5OEFp44bcskyXOmB2yD7kWk5EyHrimZlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ca7de4eca.mp4?token=h12RxLKgZ8C_1ajHIaJ1KIWVaD0k1q7f-2X-vs4AMuI7XJV2LrRkhoQgd3-rcQN6xzARh374_UGfEYA9V-eS8Y9DAwLspXm17HuhDZzs6LMfrZL8MZ1HpBopTik5EPuCyaw_2Ll9m01ysIOK7-jVPZOZoIucn0A_hldJM0GGn0zGwkIFHWcBTcUoVnxPuPP3O1-BIZTVNHvDc7nIGuz49iQkqMcmD2eBGNsVm7uQkAeYVtmDG41ezQQShBMxTeB2oeDT3qhhDPLGjycH-COxosrSUWDr5p0Usd2e6A65RhFVwCCQYL5h_5OEFp44bcskyXOmB2yD7kWk5EyHrimZlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سراوان سیستان و بلوچستان
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/17934" target="_blank">📅 02:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17933">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">لینک های ورود به چنل از استوری‌کار نمیکنه چون تلگرامو فک کنم یغه کردن
😩
دامنه اصلی t[.]me تلگرام در رجیستری .me در serverHold قرار گرفته است، وضعیتی در سطح رجیستری که آن را از DNS جهانی حذف می‌کند و هر لینک t[.]me را مسدود می‌کند.
سوابق دامنه نشان می‌دهد که این تغییر امروز رخ داده است، اما هنوز هیچ توضیح عمومی از سوی تلگرام، رجیستری .me یا اپراتور پشتیبان Identity Digital ارائه نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/17933" target="_blank">📅 02:56 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
