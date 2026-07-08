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
<img src="https://cdn4.telesco.pe/file/jlemP-NkJMeld-NrjcZ2hpCIXiVA0hYpupmLE_Ekvk2_dDYlNKEQ4hfwXNm4p6PGp45AG6stlAOY6Efg3HXkMLXdmbrJPsK5DoQjYwpDpkisPttTCCeBq8PxVxhhUqCXUUKc9zkglhruVM3N9gq8UZPHaeuNFs8VjPAJOeR-NDU0GYt4x_qX_GixzgbEOq2bTMjDaGnzL9TAfQAuZ-xF5QtLHiaLRYkaccLJcSDIOokOBlDDkUvL2vQPMzaVaxFmeBk8WEmimr3o2IlXc9pPPGu1XEX6kKiPbdJwpowFy3kUOWVJfobTFW0hA0Wx2oWeMRYo02kLJo5M0wlEiUN83w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 197K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 08:43:32</div>
<hr>

<div class="tg-post" id="msg-79690">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fab96f279.mp4?token=cii83K-Wcfl54G5VYUZYETtKMcDYlnd5B4KsMpEhhcoN5wj6tdQYghxSXGA5TMc3Cojk4tboFd9QNaN82sGN7D9N9xVFraR_OWCxPYwO2RBuh4gFi40MwGh3_34djDiau383CUrtyDQ0VQOfPMDhD1uw0zsOyyJAH3Svs6rjJgGFLMyyYt-Y0pk0eHu27Q2bXn8M6JCVymBwVBmQ4oOBrAYZBB83TsweD4Wleh6uH09MIsOUfelNwI0P8tqJGIXtPAvLDgZNDp2SYq-IYPYgTN4W5tx1el7pD7AWnOfjHGfHcZL4jHFDMFQD4KnJOEFP8SMO87VV59QrLzwWHlVKqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fab96f279.mp4?token=cii83K-Wcfl54G5VYUZYETtKMcDYlnd5B4KsMpEhhcoN5wj6tdQYghxSXGA5TMc3Cojk4tboFd9QNaN82sGN7D9N9xVFraR_OWCxPYwO2RBuh4gFi40MwGh3_34djDiau383CUrtyDQ0VQOfPMDhD1uw0zsOyyJAH3Svs6rjJgGFLMyyYt-Y0pk0eHu27Q2bXn8M6JCVymBwVBmQ4oOBrAYZBB83TsweD4Wleh6uH09MIsOUfelNwI0P8tqJGIXtPAvLDgZNDp2SYq-IYPYgTN4W5tx1el7pD7AWnOfjHGfHcZL4jHFDMFQD4KnJOEFP8SMO87VV59QrLzwWHlVKqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سلام صبح زیباتون بخیر. 3
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/funhiphop/79690" target="_blank">📅 06:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79689">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">دوباره انفجار و دوباره جنوب کشور.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/funhiphop/79689" target="_blank">📅 03:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79688">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">حمله‌ی عده‌ای اغتشاشگر و آشوبگر با سنگ و کلمات زشت به دکتر سید عباس عراقچی. تقاضای برخورد با این اعمال زشت و تخریبگران اموال عمومی را داریم. #منم_به_این_مذاکرات_اعتراض_دارم_ولی_الان_بحث_بحث_سویا_و_ذرته #منم_به_این_مذاکرات_اعتراض_دارم_ولی_به_این_مدل_اغتشاش_هم_انتقاد_دارم…</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/funhiphop/79688" target="_blank">📅 03:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79687">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">در مقابل دوتا کشتی اینهمه اسکله و جزیره یکم اور ریکت نیست؟
@Funhiphop
| Erfan</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/funhiphop/79687" target="_blank">📅 02:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79686">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">خاورمیانه داره برمیگرده به نسخه پرایمش.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/funhiphop/79686" target="_blank">📅 02:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79685">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">خاورمیانه داره برمیگرده به نسخه پرایمش.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/79685" target="_blank">📅 01:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79684">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cfe17753a.mp4?token=Na5Z-eKYoJ03Seg6nEfUZOf1tggXrMPRJ16RqBSHHROPpTjrB4dKSt1MQxXgV9pkHfQD-obDdmgBDY9AvuIIty_yjGGYVerHBkwQfdHAeVPpjBQG-vAcj_LYR_XXd6stYjU8rLJO7LH0HbYewa3ufx1F8L1FnjSjANA4pMa7ucgAOwn9QEjUcuDmBD6qBAGUv_nTeVyZ1TRUKsQinDqXFcyuHKklbdrl_jmQEqUdDi_sKh7jPGkSI1z4k-dAxugCTAaNAiVDarC8uUxi2tHkzeySyD_p5ETTAKK3bZuJn6TNKHKjPRr5cPrIeIbJqKp7jhvTYCQpkJ6y7aaNEItBfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cfe17753a.mp4?token=Na5Z-eKYoJ03Seg6nEfUZOf1tggXrMPRJ16RqBSHHROPpTjrB4dKSt1MQxXgV9pkHfQD-obDdmgBDY9AvuIIty_yjGGYVerHBkwQfdHAeVPpjBQG-vAcj_LYR_XXd6stYjU8rLJO7LH0HbYewa3ufx1F8L1FnjSjANA4pMa7ucgAOwn9QEjUcuDmBD6qBAGUv_nTeVyZ1TRUKsQinDqXFcyuHKklbdrl_jmQEqUdDi_sKh7jPGkSI1z4k-dAxugCTAaNAiVDarC8uUxi2tHkzeySyD_p5ETTAKK3bZuJn6TNKHKjPRr5cPrIeIbJqKp7jhvTYCQpkJ6y7aaNEItBfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط اونجا که یارو میگه خارشه گانوم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/79684" target="_blank">📅 01:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79683">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">سد مجید بیدار شد
ابوالفضل ناصری، عضو فراکسیون مجلس:
‏ ‏آغاز موج های جدید و بی پایان سپاه
‏تا دقایقی دیگر…!
‏شدیدتر-ویرانگر! ‏
﻿
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/79683" target="_blank">📅 01:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79682">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">کان نیوز: در آمریکا برای احتمال چند روز نبرد با ایران آماده میشوند؛ این موضوع با کشور های عربی خلیج‌فارس نیز درمیان گذاشته شده است
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/funhiphop/79682" target="_blank">📅 01:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79681">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5fd7843a1.mp4?token=hqd0minbOB-M3VpfXEiQ3EZfVxJE5aNP09bA8r3e0nrhls3QtbLkibTfQlcaJZXh50zyn7dQ7rieGfmI7xtwuyC63U85xQNTWMciE4xLcrEP3uu9l-l5ue7YI1uQCmBm8ckbNNhz1YQB3PSFAo-twvEKVza5fXsuE_5Y-iEdbTdAPqMXrpbf8kwcqhDzcXxKLA6FwmuSvlGFaT0zdND6NHck4T4QsZOPoDTSA1n4zuU28APtL7BKHnlbjUxcjT8zDa6xjJ1aZN3_PHiwhtmCx1CJTZoTfkZrJJF2hXjFnn38AjpLd329oknDsto-ttMoqDl_xUnaslQ_l8dA8TiFyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5fd7843a1.mp4?token=hqd0minbOB-M3VpfXEiQ3EZfVxJE5aNP09bA8r3e0nrhls3QtbLkibTfQlcaJZXh50zyn7dQ7rieGfmI7xtwuyC63U85xQNTWMciE4xLcrEP3uu9l-l5ue7YI1uQCmBm8ckbNNhz1YQB3PSFAo-twvEKVza5fXsuE_5Y-iEdbTdAPqMXrpbf8kwcqhDzcXxKLA6FwmuSvlGFaT0zdND6NHck4T4QsZOPoDTSA1n4zuU28APtL7BKHnlbjUxcjT8zDa6xjJ1aZN3_PHiwhtmCx1CJTZoTfkZrJJF2hXjFnn38AjpLd329oknDsto-ttMoqDl_xUnaslQ_l8dA8TiFyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم دیگه ای از حمله امریکا به بندرعباس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/79681" target="_blank">📅 01:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79680">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/087708ce6d.mp4?token=cbK78GhFNLRTpw4coA1A9GdKkmXAavDaAsYShNyeeBlsIMiJQbhK18hdETa4-H4unpYwTT7LB2RI0YE39HWfavbTlrZmET7S0Jg0qNwgPvsKWq-pdqx1mdtmQUfBz3CKfu1Yv1pbhrdNddKDtNHd1_6TyosuU64-_sLIaNuO6pr4KUhypeyeP4pi7yPELSUN3WplhK4TAzTsnDE758CK9A8ySW3Y4D73YBVmoCojNgeEC0WRVaFandjXqtbJQ_EAQ49SiFruWAuIFaMOh4ZlkOVHW7bkDyRYlvN4JGRA-qeQpzJCNriBiOO_Sf2p8RVFxBhM0xu5iAgJuLdvxE02Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/087708ce6d.mp4?token=cbK78GhFNLRTpw4coA1A9GdKkmXAavDaAsYShNyeeBlsIMiJQbhK18hdETa4-H4unpYwTT7LB2RI0YE39HWfavbTlrZmET7S0Jg0qNwgPvsKWq-pdqx1mdtmQUfBz3CKfu1Yv1pbhrdNddKDtNHd1_6TyosuU64-_sLIaNuO6pr4KUhypeyeP4pi7yPELSUN3WplhK4TAzTsnDE758CK9A8ySW3Y4D73YBVmoCojNgeEC0WRVaFandjXqtbJQ_EAQ49SiFruWAuIFaMOh4ZlkOVHW7bkDyRYlvN4JGRA-qeQpzJCNriBiOO_Sf2p8RVFxBhM0xu5iAgJuLdvxE02Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گویا پایان جام‌جهانی ای که پیش بینی میکردن، برای ترامپ حذف شدن آمریکا بود نه فینال
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/funhiphop/79680" target="_blank">📅 01:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79679">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">قیمت نفت به واسطه ناامن شدن تنگه هرمز دوباره کشید بالا
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/funhiphop/79679" target="_blank">📅 01:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79678">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f8b205f33.mp4?token=ZxxKDNwNe76O2Y9y2NGDloTuaTbmMgFLJ-SZuFY1uC5R_dW8zOz78jRPfnE_uKsB464hi8DHQHLUdatXK0zWct9ODfw96Qi6MrljeomMEKS4wb5vxp34ptEeqURfbMEbsIPeltK5L3fzassmbYZS6K-_5ktae_bgH7O3Qa1sUANuWmzUFVbEiyBD1J2CDH4lUU_EGnmqKeb7Vch7u1w1vY5rVI1PFhELDrLziT4Uru6qcdqwmb9sBANnFUW12UjHNOPMfPnBUk6EvyT4POpCJ_qfsuAZvAhAMLkvoSvhnGkyMzFn3SvgDWCIdEh_8h_-o2c28uPcuAC88Zr78jFEmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f8b205f33.mp4?token=ZxxKDNwNe76O2Y9y2NGDloTuaTbmMgFLJ-SZuFY1uC5R_dW8zOz78jRPfnE_uKsB464hi8DHQHLUdatXK0zWct9ODfw96Qi6MrljeomMEKS4wb5vxp34ptEeqURfbMEbsIPeltK5L3fzassmbYZS6K-_5ktae_bgH7O3Qa1sUANuWmzUFVbEiyBD1J2CDH4lUU_EGnmqKeb7Vch7u1w1vY5rVI1PFhELDrLziT4Uru6qcdqwmb9sBANnFUW12UjHNOPMfPnBUk6EvyT4POpCJ_qfsuAZvAhAMLkvoSvhnGkyMzFn3SvgDWCIdEh_8h_-o2c28uPcuAC88Zr78jFEmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات شدید امریکا به بندرعباس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/funhiphop/79678" target="_blank">📅 01:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79677">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">سیریک و قشمو باز زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/funhiphop/79677" target="_blank">📅 01:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79676">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">تنگه هرمز ارزونیتون، ذرت نمیدیم بهتون.
@FunHipHop
| USA</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/79676" target="_blank">📅 01:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79675">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">انقدر اسکله زدن که از بندرعباس فقط عباسش مونده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/79675" target="_blank">📅 01:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79674">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">این دیگه بخاطر کشتیا نیست
داره حرص حذف شدن از جام جهانیو خالی میکنه
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/79674" target="_blank">📅 01:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79673">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">سی‌ان‌ان گزارش می‌دهد که حملات نیروهای سنتکام علیه ایران ادامه خواهد داشت.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/79673" target="_blank">📅 01:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79672">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">فعلا اوضاع ارومه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/funhiphop/79672" target="_blank">📅 01:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79671">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">آکسیوس:
به گفته مقامات آمریکایی، این حملات به سیستم‌های پدافند هوایی ایران، سامانه‌های نظارتی ساحلی، سامانه‌های موشکی زمین به هوا، پایگاه‌های موشک‌های کروز ضدکشتی، محل‌های پرتاب پهپاد و تاسیسات بندری هدف قرار گرفتند.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/funhiphop/79671" target="_blank">📅 01:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79670">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">وال استریت ژورنال: کشتی های جنگی آمریکا در حالت آماده باش برای احتمال شروع احتمالی محاصره دریایی با دستور ترامپ تا ساعات آینده هستند
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/funhiphop/79670" target="_blank">📅 01:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79669">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">بندر لنگه انفجار
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/funhiphop/79669" target="_blank">📅 01:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79668">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rdbU1nVWbmw2_M24AAfp8DqNSfn5D_JV7l_vu1NNL0ojPg2ZvFMfpa1sLR1xVEDLFk9gLbwCu2QTrCcCC26U4xGN2Diff7xGtMxO8NLlX7C-DUhLZVZxCNfyz-bBQsuYKUifEn92Jb890MsPlVY7Kk5SBCaqwChY9PxY9Y7eTdLQmqKArR-WO3jTAdUeAqwZslLV-0LoQEfvqCozHQ2TtE1BGARhxCk3TgU6_zjKW8hj9T4SJHLgDYbgKjhrm-PafFzI9ofZDirxV9jtMY3byMDwmeeHLxZDCd0pZZhNb1r5VSUCNdb-InFQnG6oo4E67H7l7oXCS87dgZoCD_zfbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنوبیا صبحتون بخیر.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/79668" target="_blank">📅 01:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79666">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c80819d7cf.mp4?token=Z8uFOjqX6m5-VF1HAC8-Zl5ZLtjBTQ8aMhFrCRWukjwS3XRa1Iu08BSYi7f7A-DJ_W6VH3qvX-vIxFSQIYMv5tJPEkXVSXv6dlUYOBRm5aMMJBZBA3-mI-vs-_HUhvaNSJ6jB_Vc2xfgo6-qwTxpv0pyDT2yFs2yNPoAF4rxzkPznxdJwf17sPwLgayP2_gbCWg2W7zQX_BYnUNDj7FHJcinhSGDsjV6uywL6MbKgwrs_tKpc-GEv4uM7uRD4TeFNnl3ugEIQS2FbuyNivj-BnFdA8S5rxil5Al1KzygwzVRbrEtQd1kALXNgau7RRaXpaX8LMLGpM9uuL2jcOpatA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c80819d7cf.mp4?token=Z8uFOjqX6m5-VF1HAC8-Zl5ZLtjBTQ8aMhFrCRWukjwS3XRa1Iu08BSYi7f7A-DJ_W6VH3qvX-vIxFSQIYMv5tJPEkXVSXv6dlUYOBRm5aMMJBZBA3-mI-vs-_HUhvaNSJ6jB_Vc2xfgo6-qwTxpv0pyDT2yFs2yNPoAF4rxzkPznxdJwf17sPwLgayP2_gbCWg2W7zQX_BYnUNDj7FHJcinhSGDsjV6uywL6MbKgwrs_tKpc-GEv4uM7uRD4TeFNnl3ugEIQS2FbuyNivj-BnFdA8S5rxil5Al1KzygwzVRbrEtQd1kALXNgau7RRaXpaX8LMLGpM9uuL2jcOpatA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا کی قراره در ازای ۴ تا کشتی یه زیرساخت پتروشیمی و چنتا رادار شوهر بدیم و آتش بسم برقرار بمونه خدا میدونه</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/funhiphop/79666" target="_blank">📅 01:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79664">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">بندرعباس هم زدن  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/funhiphop/79664" target="_blank">📅 00:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79663">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">سنتکام بیانیه داد که مهم نیس توش میگه اونا زدن مام زدیم اصن هم اتش بس نقض نشده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/79663" target="_blank">📅 00:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79662">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">بندرعباس هم زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/79662" target="_blank">📅 00:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79661">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">دوباره صدای انفجار از قشم و اطراف روستای تهرویی شهر سیریک
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/79661" target="_blank">📅 00:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79660">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">سلام فرید جان وقتت بخیر اول بابت برد پروردگار فوتبال حضرت لیونل مسی بهت تبریک میگم دوم اینکه ما قشمیم و صدای انفجار اومد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/79660" target="_blank">📅 00:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79659">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اسرائیل هم حزب الله رو انگشت کرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/79659" target="_blank">📅 00:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79658">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">سلام فریب جان توپی که یامال دیروز شوت کرد همین الان افتاد تو جزیره هنگام
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/79658" target="_blank">📅 00:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79657">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">پایگاه دریایی سپاه تو سیریکو کوبیدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/79657" target="_blank">📅 00:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79656">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">دوستان نیاز به تعجب نیست، آمریکا خیلی شفاف گفته با خوردن هر یدونه کشتی تو تنگه هرمز یدونه زیرساخت جنوبو میزنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/79656" target="_blank">📅 00:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79655">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">قشم هم سلام
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/79655" target="_blank">📅 00:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79654">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">امشب سیریکو میزنن بماند به یادگار  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/79654" target="_blank">📅 00:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79653">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PGnphRMsf3oKhWWqUqFAajC0XcJjTKayWKJ_WP26mmRkDPodx_F0W4Gck4PITtSk0ggT6xy3p_uYPn5hPxYsmSfP4qfTephxgRXKwjq480OVk2b7bE4YzhPkaVhZ2uezCTMoTy9q0nge597tov0T5E491ZJAbWzAMmOsanOm6DJbCLaPJpz3Rs9xd8zl_U774czoJSzk53M7U8yx2Ut8egWdJ5XAWxvA6g6zAuKfaA2_gptwuyq4FVyPb_z6NDby43h0CHYqNpICO1hUo_jfCaFhb3K4-u4aW4QpdSva7nXu4LNCeeGK_s9d_cOGSq6r54ul_b6PD1kIx6jM4Bhvlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسنپ چت هالند و چک کنید ببینید خایمالی مسیو نکرده</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/79653" target="_blank">📅 00:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79652">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dkPGpeqEHRxoZAbAu4Seug_vMCmfmTvx0Yyy827BhjB4MpNfYNhi-f_68Dq77rOD-Pyw3zBPDnKxcdh6NPiu6jdROI9KsiXh8dzCLs2Ol4OHBBtI8NfK86KjlUqE3VdmJbTqCszhAnlog1OVGkxEGEsAmfFlk7Bbr1bydwpkfhgyEPKa-SYIY4JfCPSAuJJNRt_R8FpOS5_VuuW8jeFENICtE96KUK8QMDEQIKYNoQM6ieSQ5VPfV_9J_HUeK3p0zJsXm9EpemOkvsR2CALNYK7eYiE3Ng9OjMhJBCrPVw-RFzjdCCY5SNw9uQL0j-MkZtn0K4niMFDj76F_mezNAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موزیک جدید "پاکار" به نام CML منتشر شد
🟠
SoundCloud
✅
Download</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/79652" target="_blank">📅 00:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79651">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">خامس چرا دیگه خوشگل نیست</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/79651" target="_blank">📅 00:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79650">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">زیر این پست آهنگای رندوم بفرستید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/79650" target="_blank">📅 23:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79649">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">امروز سپاه 4 تا کشتی رو زد امریکا هم معافیت تحریم نفتیو لغو کرد و یکی از مقاماش گفت که بزودی چند تا سایت نظامیشونو مورد حمله قرار میدیم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/79649" target="_blank">📅 22:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79647">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BeI4Zes6zDcRPP5k3wM6XzKrY7Qt3tZb8Gpwuw1Isr19Mf-P7aE0neeXj9uaP9s6wPTpNg1Jf0a_FteA6yMnu42WP3_noWDHe7GQ2Y_t2VTYfVHjxA1EiLd6ACfKsG3HVJV85LZWUjeKZQebVLo_5_iZlPf3CWwkw_sftUqH40EkMPsSvu7sppDs9XOjSKhFQDTUnwB0gfq0nHL4CIUls5ioz-lUx5EQKq1A7k2Edvm383-fO6kF4obYuAPvmr3_UFfrMIO_kU-SytjAx3_eH3DiPSLou7l9aD3n3iQ51TAeyDqDkOsNCRDI-JXvN2ht9la7YBCLyhLYPiwZvBOYxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pFge03K_SjoIN03O_JiVIBbWuOSZabQrEcsU2oLy0vJkCae01rEgCFkRZa1E6vwP7y1y0lpf6UDrl-ADibQHHobk1lta6zpQUZJPX1RyD3GX5kospD4ITH1vbS6o8DAroonWiwM9ZjDaIpcDp9KRwXJ8s6vAz8GCZxB2xejchF_5TuUzdwsYLHjUpH7nrNNe_jJWt9lxH2kQWQVUzt8ZH2lT0Qcy3Qeu5y1Kusn8Nkng44YJ-L3vFE1att6p6GjM-h-lVp9lJhDHW31wMiFtoshH6Ti6axKKb3L_vVqn58kMfEc1X-iFImZVFQjqTUXpAi5t6hJZbYmsNzIhvl4dVA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">با این صحنه چندتا فحش به برونو و نوس تو ذهنتون پلی میشه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/79647" target="_blank">📅 22:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79646">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">حالا به رونالدو فنا ربطی نداره ولی بنظرم آرژانتین یا یک چهارم یا نیمه نهایی حذف میشه، خیلی کیرین
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/79646" target="_blank">📅 22:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79645">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسرویس رفع محدودیت و کاهش پینگ</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8STiHdsdaAjU_K2uPGSghg_dKczX7LE-umyAJzQ1BKrJghs1SVDmKqJFjS9w859nBaUpH_au4hP8fY1ciz2x1PoTZTlFbuWSCLzbsTovGkusCpTbZsV61KWkWzDV91qW-2fcH3fVDQw2EUCXNh0TEtCHyhjhsf00wZDV8YYfEyGUAUsK860JBivhVXo4gpfIejGAl9O-6h6Izh_SzF9FM5bMKPTljVLp8eDlKbCwbIG5uQEBSu0tOh3nY-tEc8OzYENEu1cvErKuk9rVOrgWZ5OmVcz4ZmCipQIXCfZF6xz9kRj7yADLziYOyOn10sjcVfEwIRiX9Yt0N2EdkCZww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡
یه اینترنت پایدار، تفاوتش رو از همون دقیقه اول حس می‌کنی
😎
✅
سرعت بالا
🌎
سرورهای متنوع
🎮
سرورهای Gaming
🛡
اتصال پایدار و امن
🚀
اگر هنوز از هاب شل اشتراک تهیه نکردی، وقتشه تفاوتش رو تجربه کنی.
🤖
خرید آنی از طریق
ربات
🧑‍💻
پشتیبانی تلگرام
@HUBSHELL</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/79645" target="_blank">📅 22:13 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79644">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">اسنپ چت هالند و چک کنید ببینید خایمالی مسیو نکرده</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/79644" target="_blank">📅 22:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79643">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝑬𝒉𝒔𝒂𝒏</strong></div>
<div class="tg-text">ایران چی میگه؟
😂
سوئیس</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/79643" target="_blank">📅 22:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79642">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">حریف ارژانتین امشب تو بازی کلمبیا ایران مشخص میشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/79642" target="_blank">📅 22:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79641">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UQliqBlyqFuXBrGu1aI1bVGDmo2WpkezRotfWEKKUtHQhIaanOKdJrNg-W9MhfJwHSFXvDAldaqNFE1LcqlfJP7r66dFNA2n-Vxdl8szWTK-6QdGRiSzQGDOSnB3HUHmgKJixuqq89S_dd9IiSKE1BVPXKsHugtoet6KCmY2u1JSoEe4yRlvp1PtZ-NYqeNXPh6n3_zFosotGuVUS5YTbdR0mj6Ocv0VwyBGCkJzzaqyB2C3X8r8kKJvNUwVBUgSDcl8wusiNswlDCxCUh56FZLvaSokczZBj7vd8P82F_9WE-1V6KhBpTvgNMcjA7C6MMQ5x7fxMvn9KFW-Wh99_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هعی روزگار
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/79641" target="_blank">📅 21:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79640">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ولی دیگه مثل قدیما استرس بازیا مسی رو ندارم، فینال ۲۰۲۲ تا نزدیک سکته رفتم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/79640" target="_blank">📅 21:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79639">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">آره دوستان، مسی منتظر نمیمونه پاس بدن، خودش پاس میده گل بزنن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/79639" target="_blank">📅 21:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79638">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gfea1eTiYDReNf6uRwuvpPG6G9bJsTniDRGGyyrGwKcSZ-TquNrVAaaBt5UNm9a14Fv4ZFsawEw4C1TXJFBxpJ8OIt2rJXbLO9_dZ5GrydWN_6yLk0Kzaowc_DgZcTjaKvqQ6vGXlwuC9cprnMJF6hwM-v7cs_ZXDVlwyCpg3yuW20PzVmEc0NW9TjLLYnySDU6pQ7Gk40JVe2T1296UjyL--j9_BJjBjcK0LDQd0n0bqVS7XwSXXRj1j44WiieVuYgXvI2b-BjyP-j2kguE7jXfUU8AwP9tc5MkrJEDdYRUxYW18HzT6uBupKbkhi92ivnVhuBBoHAQcQ6t2x7eSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیبایی خالص
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/79638" target="_blank">📅 21:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79637">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">پروردگارم
💙
🤍
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/79637" target="_blank">📅 21:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79636">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PTHNNdL4sfk7bs8fvfGrFvleilIPk1eL73LurS4WI_DRdkB3bete4uQWKHVu9g_lbEZIfA_CK6EUjDZjX28-vrOIuDOL_tvIRZ-uy4eAkv44rv3qI2Y2nDIJ0n_hOQZeOXh9Gi2jqNa_qEojoqvAFNVK5ecFwAN1j8rfbydL4BZtCPur7OSwICs5IIOF-QPyA2eNDsHpIH5ySOxEBhMGxgbS-rJYkkco2-9uEfiEc0ihWP7oSQ7WBssh-5YW3mPFgqRj3TzLCu9mJDNTpQaf69JMiUV-S8DvouCoVadGaIdsD4syIJuIuXfNLnZgj1fidClOLmyompYQTNn0Y5CJtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی فنای رونالدو رو نا امید نکرد، داره گریه میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/79636" target="_blank">📅 21:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79625">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i-ws33urv4E3PBPZMo1aFaYPKNo2JziJCnUF0cU7sd3E3X9baOFlTU2wLoCgf_F57bDoVQ-qU7q-xEgmvHx10V9LrDQPBQWzBq7shEKLDkBPrFcd1DnOOT7tW7ScxzD9rNO1nYeDqsbpjfWWzVklEgPqg7SVuJNVWy9rOrN3J_nOjdeDa4HGOQ4z9ZH-9aqjAlEMTwM0f4DKTClyT46E2RpGSogLYdoGWkiyy8Lwa0KzUM_jvz1mB16YWGKsvpKgKeQON6mdIPplPb4RQbTnXA-oZlj8jVu6e3aJ4FthBkb0YPU0qec-ZoE9JBUII5joM8ZlTStUhRLrbaRDeUVeYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/79625" target="_blank">📅 21:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79622">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">عجب کیری خوردی
😂
😂</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/79622" target="_blank">📅 21:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79621">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9531c4e029.mp4?token=GRaF56ifvE2HqNX14qIzokmivepJpGwIGqGjqJWC29cog603b3-ETn-FWnT1MBZmKDX55VRYZa2cjr86BdIpEGXXEA4M7OTyccbWRLWDBTiboQ2WrKkV3vHPfh7qmi9AY0z1u7kE6AnvM32jHzO5PAzNphycimOXcO4foqPcCbkmfUF0lHegVATae_IsAag-F6msUKGyJZegZ3qgHbyBAZ47_8WIY-R2Hw2MpxnUIRm4T0vddlTkaUPaQvbuHEpZfaF52IN0gbfeUiAo97KnanzTuPL_01TNdesSnhBxN1WcgRQEm0p5eyXMxXeOoNSp98nbfg9-NMd31XgtfE5aLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9531c4e029.mp4?token=GRaF56ifvE2HqNX14qIzokmivepJpGwIGqGjqJWC29cog603b3-ETn-FWnT1MBZmKDX55VRYZa2cjr86BdIpEGXXEA4M7OTyccbWRLWDBTiboQ2WrKkV3vHPfh7qmi9AY0z1u7kE6AnvM32jHzO5PAzNphycimOXcO4foqPcCbkmfUF0lHegVATae_IsAag-F6msUKGyJZegZ3qgHbyBAZ47_8WIY-R2Hw2MpxnUIRm4T0vddlTkaUPaQvbuHEpZfaF52IN0gbfeUiAo97KnanzTuPL_01TNdesSnhBxN1WcgRQEm0p5eyXMxXeOoNSp98nbfg9-NMd31XgtfE5aLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/79621" target="_blank">📅 21:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79618">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">مصر آورده میگه ببر، صد بار گفتم فقط کیپ ورد.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/79618" target="_blank">📅 21:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79617">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">یه گل یه پاس گل</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/79617" target="_blank">📅 21:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79611">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">مسیییی</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/79611" target="_blank">📅 21:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79610">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/79610" target="_blank">📅 21:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79607">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">لاشی
امام
حافظ
زیکو
چیزی نیس اسم بازیکنای مصره
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/79607" target="_blank">📅 21:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79606">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">مصر آورده میگه ببر، صد بار گفتم فقط کیپ ورد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/79606" target="_blank">📅 21:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79602">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">آرژانتین بخواد اینطوری بازی کنه قطعا حذف میشه</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/79602" target="_blank">📅 21:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79598">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iOqaGHM1jFe7eE-PcaDSL9SKZBQ3PpNrX2q8c9z6ncnYdP3RJ9fNW3WBHqkFepyQ-RPIbkf7DegdfA2zRtQmWXsvxHShRUKhGOHBqLgzeUlEBbG2vbHV7vSt9PKFtb7IYLYRq6emO5X3JeQhblQJPkXEb0cLxKVLamdgBBeSGr-WYqUpzkodL0eLSX5D58Va1r1hhVrc611Mhi60p5I5KNFCiHmYNQxT0ndW5w4I4u4BpmSIuN2pqQE8mPrr6-o9DIxRTn3uj75OFlaWdZ7FJR_bicrT2O2EOW8QpG2NpS6HDerHKG7Jyr4k1uvUOrFQR_1OtrHLUecBlrQQFnS5vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی تو ادوار جام جهانی 8 تا پنالتی زده که 4 تا رو گل کرده و 4 تا رو خراب
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/79598" target="_blank">📅 20:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79597">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">حوصلم سر رفته بود این گردونه صراف رو زدم، 5 دلار داد
😐
😂
گفتم لینکشو بذارم شما هم بیکارید یه تستی بکنید ببینید چی میده بهتون
👇
https://r.saraf.app/s/agrd042</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/79597" target="_blank">📅 20:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79596">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">شما چرا از حذف رونالدو خوشحال بودید؟
😔</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/79596" target="_blank">📅 20:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79595">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">یجوری خوشحالید انگار مسی حذف شه جام جهانی قبلی رو هم پس میگیرن</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/79595" target="_blank">📅 20:11 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79594">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/COI6lSAFM73lyjcUB_b0lgOh4n7oZC-ovU67BKQyd3UsyXxggYb4GzBic0XPlvtK4rd2PaAM6kMatoimpWWARqXvd2nduqAXFF-pnrL-EaiTBpRmn3_u_c32g412_bmJ3VAM0CvqoFNgEWh7eNrH2PoNQMFG46KtnhHWGyuy7fUCjHMUm7_nen8BZdTgplvauubCAdbuIMbBI6qogp1tOP0SkP5YutP9S7BDeD3ERB1pStaVlgplxiH77KG22OprxBWshg3V3bh1c8myTiPoMyYM22_RZ9jj0x7ihwVa_Xy6BFw7dsWlckPRI1Mo_mwrSARNO6kflpqijaNBScGUZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپویل عکس مسی بعد از بازی
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/79594" target="_blank">📅 20:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79593">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">این دومین پنالتیه که دروازه بان مصر تو این جام جهانی گرفته</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/79593" target="_blank">📅 19:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79592">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">این دومین پنالتیه که دروازه بان مصر تو این جام جهانی گرفته</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/79592" target="_blank">📅 19:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79587">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">به گزارش بابک تقوایی نویسنده و خبرنگار حوزه نظامی: متاسفانه چند کماندوی تیپ 65 هوابرد نوهد ارتش که از اعتراضات حمایت کرده بودند بازداشت و در خطر اعدام به جرم قیام مسلحانه و کودتا هستند. نام دو شخص از این کماندوها: سرهنگ حمیدرضا خلیلی و سرگرد حسین مجیدی است. این عزیزان از حق تماس با خانواده های خود نیز محروم شده اند.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/79587" target="_blank">📅 19:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79586">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cTaumfgjFAHwpc7KHhURTkLopAr9JhhiDkkiq3RFOathWUiUD6L85qYC-k0Wi9MRY2e7vxPsOYB2a6aSTzSoceBqZYaFqeFJOdGH1lBIYF1n-R3SVDiMQG18otGkIDmrwMF4WQKHGTcRnRx80KwRzMSrpwyCrXuEAeVx0MAV2azyioR-4BRFyIGBDjrH_6H5PvYfEtGfRWGilU7V6g1qBRSOUjKwvucPZ6CrxJCYWdF88D_nPMrmwxF_74vJ4GlqvRO3yDjF3GY5QkHKUHdaduvX1kwLjePw_YIJI9RQ6bkVbyxCsyGn2WN1NonZh2epqoJ3uc5sZgzoUgKlXuyNrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خط مخصوص نابینایان پیاده روی شهرداری که مستقیم میره تو تیربرق.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/79586" target="_blank">📅 19:11 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79585">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lw5Ne6GvVrjDz35aWYqOEnNx6Prz6a5NfXuxmdULD4hQz1wRwezjxQ-6CahXO3CLWW_R3vGC9morq0j9NFjxp5ZVna4jd86rOkGXHDmdXfY6MknzxjywNPCJKFAf9kWyis9_HYigTPmEod2jH9zAOkBnAUIqGBtDwaC0QvruMKcr9mNOmdw668A9Nz31yroivHnPcIrcoiVFeEZNAhQGDlz8_G2qOfvlKzclGqPt5Wgssa6vfPmfm2ItqTKRykyedanLILgRFUuKj0EVkN90M5HYrkhn60PXGWUB2-j06aolWEBS7gFOJDPrJj7ABy37Z3n7QwcO26JRtxTBTaoziA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید پیدار به نام “بریدم” ریلیز شد.
Soundcloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/79585" target="_blank">📅 18:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79584">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sgH1OGSZZEub8WcoHQ-mgGUtA6ABaDh_wfmHdkmrG5VLDzUZ4zCJfjSvM7m6RqmKyGxgIE8wTd765-DKS-CvKYC0PzcHZDphdcWQar54CQIx0dLl_GSBKVZdeiGiW5xoylFTPHkxIMj7D5jYGedGw1qwgWXat-9sdk6Q7IOU1jZMZAtOhTECtEI9JtBXNzYq9LWFs2YLcrZh8dwKMZxI-EKvqKu5gNI2cmYovXB_-dIkYzdyzgTWZMA_fnFA3EaCD3rLpSXiBGlKYgbiICSNKCFCgiPEmJvU5tny6kvwysWMcRKcDZfDYfuuYIKds97elD3CH1WaVkOFZa-nPjy4KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار: بغل لامین یامال؟
کریستیانو رونالدو: چیز خاصی نبود.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/79584" target="_blank">📅 18:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79583">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F-m_pA8_D1UndlRvKk5L-gevBslHM-MS-wUqT7gsBgmF0TlhlotoAFwQJ16ApGaAzAbylj8ZHAnIM_lZOCAt7FiwGzYcRfVfTpAslaEEcIBTiculkpQ8bU_FOdibkXLVY4GJC5k6SorO2R9n2lM8De5WKXNJvt-PSuM_rwrNZ4S02MOH92clfuNCzvoa5T9kxVpt9isscugw88Y0mJt67Ar5oe5GPBM8eUFPK8QmQlXJle3Wl6Y5oOec3dZyWyZFEH5sE3v_b1ipuKnOkLzl-JOS4dg4LYJfz1FbO_8Me9uSWB-4eprIvQKlbQG0p0mabajKAMTVyslO4EL64yHMCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا رونالدو کاپیتان تیمه موقع باختا اول خودش گریه میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/79583" target="_blank">📅 18:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79582">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">⏩
دسترسی به اینترنت آزاد، با ربات تلگرام بت‌فوروارد
🟢
🔥
با ربات تلگرام بت‌فوروارد، هر روز جدیدترین کانفیگ‌های رایگان و پروکسی‌های به‌روز را دریافت کنید و در سریع‌ترین زمان ممکن به بت‌فوروارد متصل شوید. کافی است وارد ربات شوید و از بخش
«فیلترشکن رایگان»
، کانفیگ اختصاصی خود را دریافت کنید.
👍
همین حالا ربات تلگرام بت‌فوروارد را دنبال کنید و به جدیدترین کانفیگ‌ها و سرویس‌های فیلترشکن پرسرعت دسترسی داشته باشید.
👍
ورود به ربات تلگرام بت‌فوروارد
کلیک کنید
@betforward_bot
کلیک کنید
@betforward_bot
R16
🅰
💻
@betforward_bot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/79582" target="_blank">📅 18:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79581">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0addb56dc0.mp4?token=vaNqDLwS3JXa1hFp2xPQgDoDXTn4b57lPZNegQfSXBKYIi-UMEz8_B2n0b-mp_dfM72xwibUBy7FmnZkIteCNN1G-noOr-j4XpFrWk-v-1oEloBFFFLlLtLdgeRHTDWhD7xFRFFqgPGquB8QGY4-EZCN1dFJss7HpWRkuiMBrJvdHbTO7yq0z59uNanFnz0MfDDPe18rzSymqVbhAvxdop7nc8YIEmA9POLsSvb1BTnBoQTRdDKE2F1ss0dlXPgpyQ8RknD4AVJmfEq8vg_XiFAwc5FO2IKFznouAYpnUjJqlLAuZfMHdCjiWhw_nVqs-CoGrAXQS8bLKgDnmer_WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0addb56dc0.mp4?token=vaNqDLwS3JXa1hFp2xPQgDoDXTn4b57lPZNegQfSXBKYIi-UMEz8_B2n0b-mp_dfM72xwibUBy7FmnZkIteCNN1G-noOr-j4XpFrWk-v-1oEloBFFFLlLtLdgeRHTDWhD7xFRFFqgPGquB8QGY4-EZCN1dFJss7HpWRkuiMBrJvdHbTO7yq0z59uNanFnz0MfDDPe18rzSymqVbhAvxdop7nc8YIEmA9POLsSvb1BTnBoQTRdDKE2F1ss0dlXPgpyQ8RknD4AVJmfEq8vg_XiFAwc5FO2IKFznouAYpnUjJqlLAuZfMHdCjiWhw_nVqs-CoGrAXQS8bLKgDnmer_WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله‌ی عده‌ای اغتشاشگر و آشوبگر با سنگ و کلمات زشت به دکتر سید عباس عراقچی.
تقاضای برخورد با این اعمال زشت و تخریبگران اموال عمومی را داریم.
#منم_به_این_مذاکرات_اعتراض_دارم_ولی_الان_بحث_بحث_سویا_و_ذرته
#منم_به_این_مذاکرات_اعتراض_دارم_ولی_به_این_مدل_اغتشاش_هم_انتقاد_دارم
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/79581" target="_blank">📅 16:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79580">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e8hgdi215uTnrAjOBS5uO726TE_XMII0h6qV30MAuarlxlOJgb5aPXPRNzVH-UhQR8fMzjEzbfdl0f3QILv75DC3Y0PK_gQBx3f_ERnA7feNkiOUFHVMjuSYSckkZuFXKw_huG3nWxN0h_5DFo-Y3ViQ49nHL8ggbfPWgXpHOXoFRST9FfOWtRTtqBWlwu8LXO7tnf1T411D9Mf2chOp09nvJjGAfRpaDYapR2m7rV-hdZLF0DLOFuSGgo9nkK9R2GTZaogSU4F466x2OIF7IF2rEtEGUXbz9kZtPRw1lcM2NaG8t5at_Qw7ImBR6b3NpORa64Cvuum87WgKUjOkKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ازدحام پشممم ریزون جمعیت در تشییع جنازه خامنه ای  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/79580" target="_blank">📅 16:13 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79579">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OeK4Ytxp9A8e0e4y754jo4CZJWdJ3wAx4hjVHC0owSr-xKbvibJla_R-LXZLsVrmvMPprWAeIdN1eE8_yuWOQS72WV1KvyMq3J7jGzpOS57stKvmHOqQOuOemLl4psmFYwu0lHoJvza-BavyH1_eu45mhwvlhFoAS0C97D_TjiVNTjZtraEG5HKum_PmlJSuOgz9ebhMDS80STZtnBTwqSNg-zyo4JFVpH1hr1DsxyJ0xXab0hwOSCthjOnPp_6ifiSjg33eGLyDhrM02RU7q5abQTPx8EuQecqieEtyR9YdhZqMCF7ZMv3to5wCijE01m4KdrmW1TstrxDRpmscmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ازدحام پشممم ریزون جمعیت در تشییع جنازه خامنه ای
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/79579" target="_blank">📅 16:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79578">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">یادش بخیر ی زمان هر چی میخواستیم هلدینگ میخریدش.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/79578" target="_blank">📅 14:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79576">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iOHdwQZqJWeoZtzmuXkgpC3B65c1rzwMQzvXeRaQgsGfIoRWw-XvwLwICc49xfq2g44xAaVtuxr41DyF81VX3Q3IfkVAqPl0H2frvDjJAOpclb9VA8bc2Y6w2lsHqBqKf-mXahtMS85jXhtr6rGEq5h-QVEJpW2U2Fsl6gyWHa1M3HqHqm7SyLdgGx56RoyA3SS5JbyEJvy_RSiaAXT2Xs0mK3pyngO16rTb7XFU2VKbPP3bjTx_qNNGO0-diO7Ov-2rqEq7eCNuj60iGOfZZc2fD5bXhkRRnmmS911Ur0eEwaLxVeFbhWjH-ppUy9MUOtLaf7X8_dE6CqJqFK9wIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BblbHHBK9K-5du3sk3x1K6SJiLv4viId_in8fpobuJIO-0aPsX9XPPOsPxBRyU6wyOdqPrt5PmsMSbSaQHRpi-TSH4pPI_zCIWbSrK5nTCNLYqTEsnbbgHrSwN3UTj9twHNDdnafSgPe69xxDPweWR1JmSUZPdQV7fb7cOsRWMWgVKUnyrIlIPd9mfmfdAADcqVOPNtBTEGeY6pMKmRBVrjPtySkuO9UnTUmssjxn0dax8yEWyTlPfsa5-SG2oubnC5ahNsNGLryc1Twa46din_hyujxhgBPpaNHrtKHvlYVNsIssHJohoMWzZGvEmpC-O2s06myA957Ves06gnLtw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیوید کیس مشاور نخست وزیر پیشین اسراییل و از افراد نزدیک به موساد:
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/79576" target="_blank">📅 14:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79575">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ویناک بلادو دوباره را انداخت</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/79575" target="_blank">📅 14:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79574">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O87moylNzYldv4tEhn4cxtmlxlB6R0YOAGpwwAWOtxzJT0Z8MGe7QJzwDzasMbLTk_GnWa9eFAIIMjDUzPjWQAWvbGTM-txUHEY6aUeGNitU-QAJYwI8dOybpdyA-zHDA_lrrYka1ICvZK0IgxOXAnP4ceQScXWRe2ixEA2fSwVY_MLTnNeIvwC8eRWC2s_KYzKAYuIB-g5zGPNCsMhjxtl_OOYVG8Iv1Ar3NZwJmRzF1xC3l_myzIFvcsm9rP2wcEs-BEQYD8N01gJpmj1GHynGvX4tPC91sbgRTzEwbSBMQ5ErGxacTqbmxxdgYXjmjOvF4gyW_pnf1yUTN4KD0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی میتونی با کلاهبرداری از ۱۰۰ هزار نفر که ۲۰ دلار دارن ۲ میلیون دلار در بیاری.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/79574" target="_blank">📅 14:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79573">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">هیپهاپولوژیست ی فوت فتیش دزده که بعضی وقتام آهنگ میخونه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/79573" target="_blank">📅 14:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79572">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ویناک بلادو دوباره را انداخت، بنزین زن دکی هم عضوشه دکی لباسا و کارت صدا عمرانم برداشته نمیده  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/79572" target="_blank">📅 14:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79571">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBhyhuP9O1-xAZD5UuVuMGcy3ffuEE4D4peReudOS9y0MGu6EvGWN4RBCcyevaHzzQC8cEtC-6J_HvCsg4OQdGmnZWq3AgZn8FA_JcdZGocSISqJh-6tmNXPvvPRMh_Y1wtoZ7cALskxsFsi5y0hZ5k3bw8piCKLNBHXVMn4PMDHGmovJHXbJjbLuvi3F4fOORMANV5DQPAXrMz4swn4BnSasmID8tfpeuZFPYIwf5JAtuE4yvlwsDDhdgF2GNewW-LIOATY3N589TTeHDrQuc5s_aWltoy7qhP5O74yaMlQ7G_rHSdxtjAhTfg5PUqI4Z9wW4hza_LwDoaaA8EIyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویناک بلادو دوباره را انداخت، بنزین زن دکی هم عضوشه
دکی لباسا و کارت صدا عمرانم برداشته نمیده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/79571" target="_blank">📅 13:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79569">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQUW1HPWtcxHwuFhIOH3Ry_hvZ7DmVqoev1jLN6QNSlcSkgGL8Sv8uqqSS_lztH-AkpwyBB__fWHMfsBiTd26J77uQRAW1QKgbuVPMFRyvte1V8SEZWR-8pyC4gRTXsE7rYgHK9aVPFltlcDovaotAkjLOB9T18ELB0SafdmdpG71deRb8ZzhD9jMmiGkCaeCz_MFOYiPxYFcjrC7JEh0-cxv24_L4qnKH0Xd2UOv9C-6LsLcGmO2sz0WsP-U_nXtust2aMGL0hy9hPaB2lyUZ-3oOSOLexwdXVIegn7SBIjirYzI6S4p3gMJzaumJgzwi05NtwR1KgrIlb4g81Ngw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق این نقشه باز هم میشه نتیجه گرفت که سمنان چیزی جز یک تئوری توطئه که ساخته دست دولت ها برای کنترل انسان هاست، نیست.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/79569" target="_blank">📅 13:16 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79568">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">امشب سیریکو میزنن
بماند به یادگار
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/79568" target="_blank">📅 13:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79567">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qv_yaMIG3nHJpVorqMEuXH1JRqPM-7KlUO5r4k-a8CdeqLdDF5OyHk28nQseAtNQR801ToNSaQW0x0168-BUoGd5YU0CK8GZyw-rhlhBA49Qv-aGToqb2az8EvEjOUeWoEfRD5Yfbq8XPn-VRR9s3ow7Y0ui-c328VoFjOoPp7oP8qsRsWiGuzIUZHgYk582x2i2jJv6ee5gvQbLLGgebQ0e7lUpO9_00Xo3pKy_aHoM3wOKslyXU9LtY1OGmbPaHxsX-DQXQZRAz5jSqRDZRMH7t_pXP2xrR4Q-mKabmTjq1ZsNDZhNqjn-BkTQRiez3JDvrSXFyl9AAdsbFPMxOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من که میدونم مارتینز مادرجنده از قصد باخت ولی نمیتونم ثابت کنم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/79567" target="_blank">📅 12:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79566">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">امروز تا اینجا اتفاقات زیاد هیجان‌انگیزی تو خاورمیانه نیفتاده متاسفانه.
فقط یه سری آدم ناشناس سعی کردن با ترکوندن چند تا ماشین روبه‌روی هتل محل اقامت مکرون تو سوریه، مکرون رو ترور کنن و سوریه رو به دوران اوجش برگردونن ولی ضریب هوشی‌شون اونقدرا زیاد نبوده که بفهمن برا ترور رئیس جمهور یه کشور دیگه، علاوه بر تروریست بازی به نقشه و برنامه‌ریزی و اینجور چیزا هم نیازه و متاسفانه موقع انفجار، مکرون اصلا تو هتل نبوده که بخواد آسیب ببینه.
فرمانده‌های سپاه هم دیدن حواس باقرشاه به مراسم تشییع پرته برا همین دستشون خورده دوتا کشتی رو تو تنگه‌ی هرمز فرستادن هوا که ضمن تبریک این پیروزی بزرگ، متاسفانه باید بگم که اونقدرا هیجان‌انگیز و خاص نیست.
به امید اتفاقات هیجان‌انگیزتر در ادامه‌ی روز.
❤️
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/79566" target="_blank">📅 12:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79565">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ULQmKuKiO_bLeCJBNlWd7jCquUF1tetCC4dLmeoVdDUq8HE71UAWXuejJz_khg6OiGfYRwND2gjhaPoSmhfAPUd0biZTLDK9ld4Pv-LznsGYllWXz2RLWQ2mQaAdWPk2qivLHSXbOLqJo_aUjAnd1FzFluUrNwfvJM8wVBuxmHB_PVCEJGQFu1FMpNKoxgLHl8e6vlLKOaCJYiHyVQUC_jvsLuli2gp062Ild8x3iSFB5bY4z0za6iB3TnAs77MQ-I-1fdxkoNFgeZspyHuYg1tTPLaUvfJPf1Z3RiHYoJ4tPYEvUnyg30u-qy6eznoDFUKJRRu8agfnoK08lAFdPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده شدیم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/79565" target="_blank">📅 12:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79564">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">اینهمه به یامال فحش دادید گفتید بزرگتر کوچیکتر سرش نمیشه، تهشم همین یامال بیشتر از هم تیمیای رونالدو به فکرش بود
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/79564" target="_blank">📅 11:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79563">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ببین تلخون چه موجودیه که برا اولین بار حس کردم ادرویت کارش خوبه و بهتر از کسی بود که باهاش فیت داده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/79563" target="_blank">📅 10:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79562">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R6fyzChlfYJW3_lk8vJlYR9R5uDQaMlHXIHlraCBZzVBNIVTZXbmzShqLUqj4BQbqzgj30ILQ2vEwOOBmvDYNWXsZt482VjqsS95g_iwkxsYszxd_l1uczAzRsfs9iJpztNl9sI165yB4d3WIKV1GEyd1CClLGcK_wbKsliR-Do4uD0yzaUc13RvLFvXRrzmWPLv4Bb0bnMYFvl6PNok3AD7vypCScg1aUO3qWfzyWjrhcXy43tni86Wh2OKqT9vSr8f5UId35bIODT1HiWc5gASAvv8h4XfSJ3natKaN1xLjju2GXDcnIvTTzZB1V7HsOJo9BDFDGMvBa5u2mNp3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با این رفتار لیدر طلبی برونو فرناندز که حتما باید خودش همکاره تیم باشه بعید میدونم منچستر هم گوهی بشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/79562" target="_blank">📅 10:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79561">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">⏩
دسترسی به اینترنت آزاد، با ربات تلگرام بت‌فوروارد
🟢
🔥
با ربات تلگرام بت‌فوروارد، هر روز جدیدترین کانفیگ‌های رایگان و پروکسی‌های به‌روز را دریافت کنید و در سریع‌ترین زمان ممکن به بت‌فوروارد متصل شوید. کافی است وارد ربات شوید و از بخش
«فیلترشکن رایگان»
، کانفیگ اختصاصی خود را دریافت کنید.
👍
همین حالا ربات تلگرام بت‌فوروارد را دنبال کنید و به جدیدترین کانفیگ‌ها و سرویس‌های فیلترشکن پرسرعت دسترسی داشته باشید.
👍
ورود به ربات تلگرام بت‌فوروارد
کلیک کنید
@betforward_bot
کلیک کنید
@betforward_bot
R16
🅰
💻
@betforward_bot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/79561" target="_blank">📅 10:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79560">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">عجب یک چهارم جذابی شد ولی</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/79560" target="_blank">📅 09:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79559">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">بلژیک ورژن فوق تخمیشو برا قلعه نویی گذاشته بود
از بعد اون بازی همه رو درو کردن
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/79559" target="_blank">📅 09:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79558">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">سلام دوستان صبحتون بخیر
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/79558" target="_blank">📅 09:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79557">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mPVfgr3eHFlrprZL3iebyBOBA8nfdqFeuUK-N_OXavfA-7l7LM0VnEDxpksR05fKeiP-AG1qWDq1vxwyp5gy2UjZFrfa6F20ofHFpwnTJ46qPCbO98OTTqGDx6vtyXCDSZpd5BL8Bm-vAAH9Ej4I8ASVuINLEP8VEhbgagezg__rf-Upt6XONel8PO9lMCWN0UsxUNuwKE1jYqn5vJlAn7oqkb-uzibEYQrs0l69x9A6HxvEUHZnx3C_KRPkJZlY6T3yiUTEodsysRwR6I3UupmVGxcIVOcnHK3fGTF67DMxT4rKrLy3cePjB7Ym6NDSom0BX4qyt7N6ig-b8h38YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه ذره حرفات به قدت میومد هم باحال بود
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/79557" target="_blank">📅 02:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79555">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EnK2ww8W4TmfNb7Owek985TdGcMNswjLAAmuTV0WXv2ZEWRkyQARMlC3FO_1mioA2OJMv3Kfx6FEiXugPVh-QqunP2NbaMClQHxR6bP8QHFEAuQ_YjrjXzQRi83M5nferI4YeK3Q6X668BBz4zwty7Tby_hFiQXUD927Qu3BEredRJIJcjBc6mfM1ewck1Are7Q38fEC97umXjEb5L2Oc8MkYkP0SQOMjXxgeO085x4JI4jgjP11DUyVHRq_Cw5773njrI24lJwDVfv4qmHFxsZBMz0VsJPCqoTAYO4wSg28iHwP31jAUxb5vYR22i1UJdBi4FJ87PRzXEe54MbBHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kcXxaUcN6nEDJXrfn4pBDqYOa6NETbSAvFTQ1jvbwpo6PaRaPKAmSAB2tA7G3RyKn7lZE6hZ2jLytSGz-icHxSiaB1VYk9_yu5_fUaFVfPpSZN7GxXzlr6UtpniYE5xTmHGHVjTrnq765SxgtnGPjKtDfqUNXa1a0aeP8dLhGK6oHtZZE8vQCIqV3KmlNHb8v3OnInVgbhnWVDXTcfJtr7qZzbaTVFyzjPTWJjzaGa-bYsJ7-zvtcJUR-eRXK-JdlcbfShnyQjZZDS53ADn9FLLTLj3G-eBvkMCkvBCAx0AW30sMFQRpb4kBs7qnw0G4BsqNUn8K4QPvhuc3crLotw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فک کنم دعای خیر زید یامال بود که بردن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/79555" target="_blank">📅 02:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79553">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">دخترا پاشید بیایید چنل دیلیم دلداریتون بدم، پسرا میتونن برن بمیرن  https://t.me/+q5Ml6Hl1Af5lMTI0</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/79553" target="_blank">📅 02:34 · 16 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
