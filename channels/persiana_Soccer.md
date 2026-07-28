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
<img src="https://cdn4.telesco.pe/file/EUTkv9_pExAVTzFRvVPwypqc9r5yOzF8Ov72Gd-vinh0CNWdaFAw7Q-0enw-ZMGxeK1EaiMAbE3PdLs3At1u8MEpBOK74y_Cufu6f9f4kjsG6rA-QAq4SMbNocB447Kfyz7aDXoq9Ywn_h1gkb3KYJ1jh3DRke3r0a7tm74cyFU_jhgUS7Q41nKyeAbCBpQytQ5q38OPbMFZZY8VZ231LzbSKb9fQUPJpjgHBfASUIv8Hf34oixz2O6n0HjktzuVsZXgWknt5bhd0ptQfsTSxZ4jWAOdRHo-BMWtNwJUgYjxViiWuwQ9p1Eu4QSTTP8jlO7EmyJhx93vyCwtqndt-w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 611K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-06 20:25:31</div>
<hr>

<div class="tg-post" id="msg-26710">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24d9dfad66.mp4?token=a8ot1x2Gr0ESD90FJB0UFJswsBTQRXaVDIQnybC1A2QXJ7ARGiztKbwz2_nC3ycnWDy5rl9WP6gdpy971eJHZJKi85A0g9AusrPd3cEU-iZgvzffc_QEQDponLV6jaVZMrkYX9VsJGIvLiE-klLwQwEyTTh0CRzpyi8FY2nM1EsV6Bst8IbeZ1hUAJ0v9dcvqD6JxH5HIX4rmfElZ1PmUvPhaBIfhAC_924QNiFSdzMv8rOt_mquu93qmfaujn202_dQ_DAdJPWnAnxJWUhGISqxRzxLt6AHHjkxfhCaXCe9-G8Sn0QZBLQhvb8lUGXJCCwPB7KwWh9IH221JLAsZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24d9dfad66.mp4?token=a8ot1x2Gr0ESD90FJB0UFJswsBTQRXaVDIQnybC1A2QXJ7ARGiztKbwz2_nC3ycnWDy5rl9WP6gdpy971eJHZJKi85A0g9AusrPd3cEU-iZgvzffc_QEQDponLV6jaVZMrkYX9VsJGIvLiE-klLwQwEyTTh0CRzpyi8FY2nM1EsV6Bst8IbeZ1hUAJ0v9dcvqD6JxH5HIX4rmfElZ1PmUvPhaBIfhAC_924QNiFSdzMv8rOt_mquu93qmfaujn202_dQ_DAdJPWnAnxJWUhGISqxRzxLt6AHHjkxfhCaXCe9-G8Sn0QZBLQhvb8lUGXJCCwPB7KwWh9IH221JLAsZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طبق پیگیری‌های پرشیانا؛ بانک شهر هیچ مبلغی به حساب باشگاه‌نساجی‌مازندران تا این لحظه که این خبر رو اعلام میکنیم واریز نکرده و باشگاه نساجی و مدیرعاملش فشرده در حال مذاکرات نهایی با باشگاه استقلال تهران هستند. علی تاجرنیا و هلدینگ اماده پرداخت پول رضایت نامه…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/persiana_Soccer/26710" target="_blank">📅 19:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26709">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTP0WWgiooWfTUGgsXCY6kvm2z4l1G8duRWdokHr6OkeEOJK6qh1ILcC8POeDZ5h3GqAw3sw4Np-SFUQ4uXOkbArObU1bgrzNQA0H0VZrvM4O2-kkdAhO1s9VQUOawlKi0Pf3YVSUsp6K18atbH4pF4_kNNDdPQ3QB_N6Awuf8IcaZLpXPLng94QcqSnNh38GSjSNBAopE6H5HPR7zF9jUeSV9oNaWHaCEpH4vQv47MAAm74OZ5PuTsESi0f1BK7toqP0w7u7yHoCpwfQbkFdSL1ik3jZe1ylposmZ3cPdB5hI1hh7ZEJx16wydoWxXV_T41xCctmZLp6E-BmbD9fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ میکل آرتتا سرمربی آرسنال تماس های خود رابا وینیسیوس جونیور آغازکرده و در تلاشه که اوپیشنهاد تمدید قرار داد رئال مادرید رو رد کنه و به جمع توپچی‌ها بپیونده. نیمار هم به وینیسیوس گفته جدایی از رئال مادرید یعنی نابود کل دوران کریرت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/persiana_Soccer/26709" target="_blank">📅 19:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26708">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0dDJHf8ElTQlfIU9SP3DR4EzoubMjJA41uACr9yQLxs8aa0hqd0wMQmDPkmEE1t9S3MppFFHSi71QH2ascjnEXRsSdSHsrCu2TQWaC81yAVcJHQP2lBrnQouVogmVbGr5VGjy1wrR_fXzmtV09tRsM5OOzP0BJxcSB_p-W9xDixvaZegZLNHkkqKSc5SOE1siGL7rvPU3paiemFo9rWzSeRzbpd_zt_C1lzLF0_SGIMepyY5kyrX8-B4gGB-o88LLvsNtAQUw14l6zuZjXoiYAp6NHFdzIjozSXb0sjUyRNBr5ZomOD-bIaTLd3TZgkPH_i4iZtdT7Cs-Rnxp_krg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام سازمان لیگ؛ لیگ برتر رسما از روز سه شنبه 23 مردادماه آغاز خواهدشد و روز 2 مرداد نیز قرعه کشی این رقابت‌ها انجام خواهد شد. البته همه اینا منوط به آروم بودن وضعیت کشوره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/persiana_Soccer/26708" target="_blank">📅 19:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26707">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pgYaaYBnWFtM6wUjaRHzFLtGO8oS9gzx5wIj9YN3rVKepHmnMoWGop6Itud43n6EMAwDmo5OTId9yXkhc09NKVxyOwSwebSoitRULv9XiuHVCb2Cvv3jGe3wp3Q_ch7jq_QLEvUSeF5tJ24yJa7NG3IWQN10jLqdaYuMLNYhl75iYa9woNlJr4OFYldAKTmcslLNkE5l8nEGKjzbUOnDHZuS0rWuHI2Ojszh7N2qxFDRpa0rBYhD-yIgP7IkrwXIhUCLZLSVh6yx4-v4NHADs8iccWIonX7OXkkhLzKQ8DdXk6OfisNT4_LLXl3LD1ClJffc6gI8LSg8FoaaikFDmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ مهم‌ ترین دیدار ها‌ی‌‌ امروز؛ بازی دوستانه شاگردان ژوزه مورینیو مقابل لگانس در مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/persiana_Soccer/26707" target="_blank">📅 18:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26706">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c3c711337.mp4?token=YNe5ALQkLsvrx3SOlGyyt-I2i2JgSRE84DTtkrKyzlBLPAo1xFuY7z_itrof5d_ZWaMw1F_VNcq1eX_Q3Vx9J8YheKOp63UEn9Uz_rVlkBzh7dsuWbbWYvYEaIhVNJ2mabaJPEFjTpgVGvjDo99mjzVw2DHtQxstgXZr9zVDGpnLN04uURfp6eEcXAFnbW-eD-XCMAVNTXWwWZ5rUlZI8NrfkBCRl2Pwhu2hJFxHpFrgKnE6OnrjqYHxDtZW3ygnRvrAeJ_wDD4GxvwQrtkYWfGGEirO_5PlJOVh29n4_OhDfTsDoScgxwmzXZSmMyG0xFJKMqEw-VJcx33mjhbDn49UxswJzr7A7rqTl6yltt3t5umAlizphzabhHrXaeonfndMNbILVdOD2FCnnw8ufrjybW8TIeANSPq-AeEOOhz4Wm3KFgpiBlQcWC9u9tsJgMuCjed9nA68xQrWm_TSvGh4ABaLaCViggb6ZNdUlyXDkRKq0Kr0n2IKODTNb0p_ikecOpfHs9AK8FCc3XIOT_jRyvrvqUZuoTYDUG_64wmZCNmlfym88IRgEdHkq94KPqTrtwIjYtuE3nkwdsZ-D8uqx3ojPC2fAaY_PMdaidWcYZivPwWVSoWu7MXAsdGrjoz0SgpVz_tOv1YnK___qFbBK1lY3lYV2W4SLZp6hws" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c3c711337.mp4?token=YNe5ALQkLsvrx3SOlGyyt-I2i2JgSRE84DTtkrKyzlBLPAo1xFuY7z_itrof5d_ZWaMw1F_VNcq1eX_Q3Vx9J8YheKOp63UEn9Uz_rVlkBzh7dsuWbbWYvYEaIhVNJ2mabaJPEFjTpgVGvjDo99mjzVw2DHtQxstgXZr9zVDGpnLN04uURfp6eEcXAFnbW-eD-XCMAVNTXWwWZ5rUlZI8NrfkBCRl2Pwhu2hJFxHpFrgKnE6OnrjqYHxDtZW3ygnRvrAeJ_wDD4GxvwQrtkYWfGGEirO_5PlJOVh29n4_OhDfTsDoScgxwmzXZSmMyG0xFJKMqEw-VJcx33mjhbDn49UxswJzr7A7rqTl6yltt3t5umAlizphzabhHrXaeonfndMNbILVdOD2FCnnw8ufrjybW8TIeANSPq-AeEOOhz4Wm3KFgpiBlQcWC9u9tsJgMuCjed9nA68xQrWm_TSvGh4ABaLaCViggb6ZNdUlyXDkRKq0Kr0n2IKODTNb0p_ikecOpfHs9AK8FCc3XIOT_jRyvrvqUZuoTYDUG_64wmZCNmlfym88IRgEdHkq94KPqTrtwIjYtuE3nkwdsZ-D8uqx3ojPC2fAaY_PMdaidWcYZivPwWVSoWu7MXAsdGrjoz0SgpVz_tOv1YnK___qFbBK1lY3lYV2W4SLZp6hws" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آنتونی‌ جاشوآ بوکسور سرشناس‌ بریتانیایی و قهرمان سابق سنگین‌وزن بوکس جهان، در مسابقه چند شب پیش خود برابر کریستین پرنگا، با آهنگ مشهور «نقاب» از سیاوش قمیشی وارد سالن شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/26706" target="_blank">📅 18:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26705">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d2TygFC0OghHbh1DZGDKMU-7YuKSvBObKUg2QPeEOCUz5DrEbdQwCH_LEibbJNoxVQS-fNM7ontFLiVpK8nHTp7y8QMl6Mh6AtbDswEao5tzCRe5NQxjDElqxMRoKtCO6dt6VgZO4QlHq6wZ9-7Bu6PUmdauXfjUrN4AqzJf1qSW9sCGQ5eXPr9aAN_hw5ZLKM7fpADrHI6UDKw4hXKKR-SXErXVYRCtgSRCK3MBdPau_elwot2O9jVLBBA0B3ICjG-M-Y28zL3J3h4CNLpStGHaOFqQYyrAprO9xcMEnIyRWcYuRN_PWnhMZ674uC1jlnh2PbMcecRAWoDNwstR4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی سه روز پیش پرشیانا
🔴
محمدمهدی محبی وینگرراست سابق سپاهان با عقد قراردادی 3 ساله رسما به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/26705" target="_blank">📅 18:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26704">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">برنامه کامل فصل جدید لیگ برتر.pdf</div>
  <div class="tg-doc-extra">34.2 KB</div>
</div>
<a href="https://t.me/persiana_Soccer/26704" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔹
این هم فایل برنامه کامل فصل جدید لیگ برتر؛ ذخیره کنید و برای دوستانتون هم بفرستید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/26704" target="_blank">📅 17:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26703">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMcHg-jxHzgFYIIZF1vt-mo05SEU605OoB2GIqYVxMXEjI2ZBFnUugydd5tS41-1rqun25317wvUMnQhNMJhrB5YmkbwMxOyxUGYUJVY64ktP3oXwh48jH4bGFbNS9p9hHVitCGryNihZHytDsECEWFFIClqTmPKO-wn5Dk_-W6lmEmA-Srgos7xZYXfBUNk8nCeyQUusySGF4M_7GydBznsvC6SzOtD_s_k2piMq3F5-g7vIeGWDC9obt9AqfsHlbCPZk-t5So_aBYyvD97y-YIpRb9GfptvzaOZkgC0e_-ZpEmHFwcCieU3G1rWpDpCzvaaYCiA8DMvBjM69r5sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه دوئل‌های جذاب 4 تیم مدعی لیگ‌ برتر
🗓
هفته دوم:
سپاهان اصفهان
🆚
تراکتور تبریز
🗓
هفته‌سوم:
استقلال تهران
🆚
سپاهان اصفهان
🗓
هفته‌سوم:
تراکتور تبریز
🆚
پرسپولیس تهران
🗓
هفته پنجم:
استقلال
🆚
پرسپولیس؛ شهرآورد
🗓
هفته هشتم:
تراکتور تبریز
🆚
استقلال تهران
🗓
هفته‌پانزدهم:
پرسپولیس
🆚
سپاهان اصفهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/26703" target="_blank">📅 17:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26700">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QclHNdLBiBVTEbLtWC-zNWhLhbIf1x0bggpXPW8Qz2oYnBQniz9bF40qz3JWJvr1V-j3nCYhuclUISJwSrt9I9urfZr6-7hoqGEEti-KTDhqyhRhnXZPb3Zsr703ZLEWw9qjQ6-DbPZ32R-gjU-b3Doj3tvoqXDLQt30oHgZz3IKis81GJSMd_8LLbQH8GjVc0vRMcZoo06ZfDM4rmnE_UInkUuxJZtY_0Mmw1FNFxHJg-2ztXAFYILFw30OOXaIZwNlW70mUZcmXxXs6N7O3EMlrhBDFI0XPfym2gtinVNzKgGtlHxt5Uo8F_IDdHQ6goxlPF2ahIUbQhrW7AemgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐉
میخوای به راحتی از فوتبال و باقی ورزش ها کسب درامد کنی؟!
⚠️
پس همین الان وارد کانال
Evil Bet
شو
چون بهت اموزش میده چطور دلاری پول دربیاری
❗️
💵
اینجا میتونی روزانه درامد داشته باشی و سرمایت چندبرابر کنی
👍
آدرس عضویت کانال vip:
https://t.me/+TmGWkUYH_8c0OWZk
https://t.me/+TmGWkUYH_8c0OWZk</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/26700" target="_blank">📅 17:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26698">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iZgrqZ830FfA4cDC7KmXrsJv9aPRLpR5dmlRIb7VVuAkABhV0iuH5R4ODfMo3m5odAwvI_9Rqb2DW3BDXO3wDTqfohgVddOXjVTxTd0OmW4T3HEfEn9Mw-K_d-fPBZUX6MShIODUkDVuK7BOgzSFISNim6VzG4r-mi_OMo17mhbcefvownxltGlbmkWoYmxRHd5_ky9AD0IVqzyrQmtaTnhrFdnahuFz_LjaNb9lZrtSeO2QhSi8EjedmItwLuX8q0d2uhBAR-k6Ssd5EFU2Fb025sawt4MXulu3479_U2246wX4h3DNAviiRk9g8D1n2R2s7-twgr8beiYZIt6M6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B357tKHCB4INedvy_8hxa-KwJZRMvDhJhZ_eEAFuPjwoDvN7MnPDhOO9SRGLMhvm7DBh-FEUwEt9fDI_1-pPh6nex6-Nq4h_fzrI34i0XYNEZLhmoJFvXZmSwwEV4OarV6WOSLVeT-zwnTYWicQtUTSEfKTSdnYQWpRdf1NlPgczikzDA6pThLrrZkG-RNvDWSiq4RKAKVjRhe-qX2Cxn81PSKYDXG_HCuk9YRxVrmRodW6A-wuGhDCawt8MCz1Zc7WD_-JArB4xpchleRvXpCZdO-FKoeyO_gf5F-DlSLzHbiSfC4-vrbMZR68ethYEiyvrps00eF1EHFmo1jjYug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
برنامه کامل فصل جدید رقابتای لیگ برتر خلیج فارس؛ هر هفده هفته مسابقات تو ویدیو هست. یه جایی سیو کنید و برای رفقای فوتبالیتونم بفرستید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/26698" target="_blank">📅 17:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26697">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tOM7tl8D_8ZMYk3uvCSXnGA4r_VG-1_VHqagYpNzgjQ9Pvoqh8XIZe1nyz5jSzXMyJuHs1hzela7LIHfH1fbJKXzXa7pTpu3gk0y8b3aQ6BaTPhkThjPiag8PvuKYld7kMDHC4iFpyas_C7W303Cuj4O8Q4UzqAkjCpy3kwz2CxqsURKhvD2qxdbbJh8WbWrwkeN3cRuDQCd_yu0S7u8Vf1ihBJOz1VGB_MAKtpQVLCXelmXCBMjpjQDCGAoJ938piwicj0CC673UQFYHb9g3eTTCD-PJTFl0h905M1jzhqwMWMWjB9WA_CsuUgWGsXi0Cvb2XImqH6qcO-gwN8iuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
برنامه کامل فصل جدید رقابتای لیگ برتر خلیج فارس؛ هر هفده هفته مسابقات تو ویدیو هست. یه جایی سیو کنید و برای رفقای فوتبالیتونم بفرستید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/26697" target="_blank">📅 17:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26696">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WrEZDrSpZi__Cz_PkyGd3Kijqvrla5kmi7hZXTQz13KeQJfgMYP5NCLki0C-5pDEnTse1k1YZ0f3c3n65xz6sMqz4_hzteJV_pS1_SO54WefeC7DE_cybdhNU7-lO4jhKImUzmx5OGSItMFa3uDiLK4lV0WUGnasnp6o7FTr4JLps5y5C6T8lgQE80-2CMH_keFwgD52wqq4obrxMJU06XANnIg79nAnVkGsFeEd4iCuFqeSSY8HMAZoMgfd8YtzECNir1PM7U1YktEF4uObproxvfyr8GZmonZgPThaBho2v8zpt__XPw2QBwToR9DZLuMsYbYB1p-PmoOB6kC1OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ بعد از عدم موافقت باشگاه تراکتور با پرداخت مبلغ رضایت نامه سنگین‌محمدمهدی محبی؛ مدیران باشگاه پرسپولیس ازشب‌گذشته بامدیربرنامه‌های محبی تماس گرفته‌اند و پشنهاد مالی خود را برای 3 فصل حضور در باشگاه پرسپولیس داده اند. مدیر عامل باشگاه…</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/26696" target="_blank">📅 17:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26695">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/izdm8cA1pw2W5z-7tJUn-biYbsCzEbXtcC0RPtd5tEZl8odOmq-zfQDVvDdBw_RiOHM4TbQ8bookna-04QIVkgcuoyf2aIU5ga8t2xsI5mK_Ous3_r23exOJ-lv3vAlrJVyQdB9nZvbV9DHxQLijUiBrQSLdLG98sFBTo9W32y08eCRHRMy9wQan_8wgIYTDh1O50y0bOcgfaiJUYHbmx29MqYyxd_tghyFilUV_xGu2QbVMvuPhLO1elVfrGbflM_erkG8qV1EqQPyvYFpdNxlUhOZv5LM36v1W9EC0u0Na5dRmeEkujmiaYQ6Jy__Aa-VPdJHUyk2r_Qi24zMTiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
برنامه کامل فصل جدید رقابتای لیگ برتر خلیج فارس؛ هر هفده هفته مسابقات تو ویدیو هست. یه جایی سیو کنید و برای رفقای فوتبالیتونم بفرستید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/26695" target="_blank">📅 17:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26694">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31211ab420.mp4?token=nmoUds6rczoHpOShT1EKN3FJZZc7axDf-ZXKIVZO1bhAOqWvAhXHMaM8YtwpF9GYix_Znvc99Eq9ZQrsPmTczuu6joYnxZExAppk3Dk7VzaeFm9M1rc3g0tttUVkJwOHL9prgG8B8BAJfzqnEptbu1UhdLGE9ESA12THy7rfouxT9g2Ygc5a_3uEYJXR63DcO8jcfV6nzIftafajW_RmiCR5TNlREi_z3ybP-rhNhB9ncf8ASh_0b9lCENjsciOgdX8mGGryId8DCfDHbUGxT-Py1uyTdN4HWCqOQzmdYGBIeRisu00Mxo_3m6QmmHSE1iKGRi4QwSpnlhIUvFs3mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31211ab420.mp4?token=nmoUds6rczoHpOShT1EKN3FJZZc7axDf-ZXKIVZO1bhAOqWvAhXHMaM8YtwpF9GYix_Znvc99Eq9ZQrsPmTczuu6joYnxZExAppk3Dk7VzaeFm9M1rc3g0tttUVkJwOHL9prgG8B8BAJfzqnEptbu1UhdLGE9ESA12THy7rfouxT9g2Ygc5a_3uEYJXR63DcO8jcfV6nzIftafajW_RmiCR5TNlREi_z3ybP-rhNhB9ncf8ASh_0b9lCENjsciOgdX8mGGryId8DCfDHbUGxT-Py1uyTdN4HWCqOQzmdYGBIeRisu00Mxo_3m6QmmHSE1iKGRi4QwSpnlhIUvFs3mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🔵
مسابقه بین دوتیم استقلال
🆚
پرسپولیس در هفته پنجم رقابت‌های لیگ برتر برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/26694" target="_blank">📅 17:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26693">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0yPY4D-v7YPaAXxBH0v82ESKkI0qH3bU-OmLZQkZYDfFtUvYzptSkGOvtYZ9bgKsRdMxS5TEzB43A4eJqI_eih-W7wLsJkUbAVhMuh5nqnuS4vmnwMDoWa02AVQYCFElDAjQ6b4pc6qzQ7fWSBs9ZHNyPeuBf-J6VnhnENa7yduQy_SzMTnkteaGt3BS3N7sQNMPb4xTk36-xSQ_tslGKfiDN_K0zmSvBLlTDcVTu3XQKOB_4qPA55dmPU8c-wZTanTY9jlbOvbN2w5fsM_98D_jDgQsXGpv_M_5yVdT2344a1ywqCkzYOfeSabS4_UX1m9IL-kcTiYh-DXwhkOZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
فرداشش‌مردادحوالی ساعت 16:00 قرعه کشی فصل جدید رقابت‌های لیگ برتر خلیج فارس انجام خواهد شد. مراسم از شبکه ورزش پخش میشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/26693" target="_blank">📅 16:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26691">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nYqoUW_4JOCrDIdea6eVgBK3UuqYLILK5keZk7AYm-nmBQDS0qarZg5fI5u_NaYUECP6OGdxTF8bfCOeBleDR1CnIkbg6gudYWO3xIHyQ0xIttcry6amx6dS0qMMJl5CQysJoT_ekVZigY7hp8kzabOtnICqozbuzHdIlwK1xx10mjn6gXtbcu_TDAZ3GJPBerb8A44q0n7DRdaEfUqjbv3vlHz7A9btJVG8dA7ouZlEAsnGqC-apNEVLru-Q3lQVgrrnuTPhD17nGyinoV34FO1APOx4gN55fUanV57wZRwJ7d-pG4tSmFCNOpNMHuZHKzTTNM8pagkov1pqUjg0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ محمد مهدی‌ محبی دقایقی قبل بالاخره قرار داد خود را به مدت سه فصل با‌ پرسپولیس امضا کرد. ممکن است باشگاه امشب یا فردا پوستر محبی رو منتشر کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/26691" target="_blank">📅 16:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26690">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8LKrM4_iBx-NhmGtl9Bfs8dQJxstM32T0gc87kciglmArUaiLEdMpO8NldGjxHtXojfFFva0sJF7LukedNGj8iR7EEgNTYlJY9k5VJ0s4HULPSXx95xf9lucET_iq0zMIKwYLyTpAsaqIlJOS-xyqjC6XnlKDz2XoAb28j90yJokEMZ8rHo-OadKs_jzgFZa1bPqETLE-wZnLBDiR7G0l3u0LAe1G0C2dW-OAMP7611fcNQOKdDYc2QW3wtVc_nGh3A2F6gScjE8uJLjY5oyCk9oQz8iacKn9vD3IOsUKpLNaA-tEFC4hRkTghkGnNHTHosQD01RS8wYzdUpiP71w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افشاگری‌عمو کسری‌طاهری ستاره تیم نساجی: مهدی تارتار به بانک‌شهر اعلام‌کرده با وجود علیپور، سرگیف و شهر آبادی نیازی به جذب طاهری ندارم. تارتار سر انتقال 150 میلیارد تومانی شهر آبادی به باشگاه پرسپولیس 35 میلیارد تومان به جیب زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/26690" target="_blank">📅 16:21 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26689">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ccc06fbcc.mp4?token=r8IbanOygJJkEVJ0KHmIjeGV3hI1eJC8BPnpbpSsYO6PYbmteBz96sMkN_HgGoTHHL8m6DMhyCWNQxv2iClkHf1jz4vtoARIBoY6xfZ_i91yT0O_Mo_RNV0EtAVBLIIVtIQJCXQ5tRrUsuCE3KIeEAeHv31iAoAjqHNgvtU7xp8EjUBlrrWs4MzcSfxwqkHH2zR4p9IXMtDG7-CGo_3Mb2oSllbyprCqYtxZ9xHFphBCgKVaciEbJHQEFUhAPrBMDf2LyIroK1-59M6ekuMlXoJdpf-OdhOGJErHBS2w6T7LW6BSu3SZxB7djo7lGedMH06a56V5sUgQGfZyQJuDBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ccc06fbcc.mp4?token=r8IbanOygJJkEVJ0KHmIjeGV3hI1eJC8BPnpbpSsYO6PYbmteBz96sMkN_HgGoTHHL8m6DMhyCWNQxv2iClkHf1jz4vtoARIBoY6xfZ_i91yT0O_Mo_RNV0EtAVBLIIVtIQJCXQ5tRrUsuCE3KIeEAeHv31iAoAjqHNgvtU7xp8EjUBlrrWs4MzcSfxwqkHH2zR4p9IXMtDG7-CGo_3Mb2oSllbyprCqYtxZ9xHFphBCgKVaciEbJHQEFUhAPrBMDf2LyIroK1-59M6ekuMlXoJdpf-OdhOGJErHBS2w6T7LW6BSu3SZxB7djo7lGedMH06a56V5sUgQGfZyQJuDBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
هر اثری هنری دیدنی یک کپی بی ارزش داره؛ در نقاط سخت زندگی فردی به دادت خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/26689" target="_blank">📅 16:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26688">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YW-QpSOMkBtsuYc0qeOlLH72-tfv9qfb1ezWpFmS8JjvmSsm-EU8dUwknxWUA3RXimabdwYO2XDlxBuR-sz2YesnCL6A887k1h6G2FQeFE1SN_nxYXuKSRa07eMoirksBbp8DLBS2rbccnjdickJA0Mbx0IYvJzGnHwKRMhi-6hv9Pwu7vbW0ibd-nM8a3bdaBsBCm_i4LFKUB5h9nKQiHS6c03IVQDFp7I03WCmOpsrWdXM8rk9u0JTC78ADP_UUUNAZ9KoC2-j3qxu0VvE83SgKreBTcVsXcz3qmrWMoWDzrlnti7LJXoQ7HEVRznPSodjUw9yF8pyyYwUCjnGDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
مارک‌کوکوریا مدافع‌تیم‌اسپانیا: اگه قهرمان جام‌ جهانی شویم و همسرم‌هم مشکلی نداشته باشه میخوام که عکس دلافوئنته رو روی قلبم تتو کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/26688" target="_blank">📅 16:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26687">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3fWqGRMGuV06tdwIHXzYzoH_-KMhDpgStENOjEkFgfMVwCquCVxL1NyO4fSKo-FXEJRprZCTdetHLpF00O_xzQF9EPM49lJ3b0NUc2Nmyhj19WzkdjQJAu48pDyiiY7X9wKNkRki_I27uFkiNXPzgisg8q_d52kzyqgOCyDr0h6Yxyb_Gb2PZrrigiFon3ShmU4vWfZdJqccFxW3nOi7YLvJdVV7RV2XjHcwrmCKrpS1GBo4YHCf4WSeB_f1emw8x6Gj0Zg7D9NvHR-k4qxVRgaS_XSpo3yvDFrzjDIvfp3G9ooISVvVLHD8v1Mf-OhV6tJRKWhaBBjvNo814p0Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ یوشکو گواردیول مدافع 24 ساله منچسترسیتی قراردادش‌روتاسال 2032 تمدید کرد. سیتیزن ها اعلام‌کرده‌‌اند که هر باشگاهی یوشکو رو میخواهد باید 80 میلیون یورو به ما پرداخت کنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/26687" target="_blank">📅 15:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26686">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sD-2hP3m5E4whotycVNUC2w3VuEzHYbhy26XUBiswK-n7NmKd7pvZQJ6SKh7sgJcsY2O1GocV9QNPcOxnVfRZeQmxT2CQS_CEY-cccPh1AH9at5bJkeDUGT6aAoJfg1FGfXO-DqrIadLpKhMqQ-IWxuvxUj5PX3mT7XS2MMfmkh1PbXzd6PsQ6fz1iVmeCF4pQlcSxB6Atlpbp2mM5j2z4egvgQBW0UIjdIgCkkHFYAeGyQXGL3eOBjUMc5Qykai60eMuisolEivqKZrVRf5GXDRwv8YgD7EbhHsHJylxaNGOGacr7RLCy5F3hGbGOdo9TDEdZPfD-zC0fpFrcieMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
👤
#تکمیلی؛فیفا درروزهای‌اخیر رسما اعلام کرد که ازنظرحقوقی‌هیچ‌مشکلی‌برای پیوستن کسری طاهری از نساجی به تیم جدیدش نداره. هر باشگاهی پول رضایت نامه طاهری رو به نساجی پرداخت کنه باخیال راحت میتونه باهاش قرارداد امضا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/26686" target="_blank">📅 15:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26685">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JoZk9IJe2RnXn_RrV9xJWHc4qAXCLekJO2_-4BhQxd1bibGNoCFGiXq1uM9gP71GG79_75Q6rbHVBU-NNokazsV4-WyTGvc8FeL1fkKhFKCYxbjb1B3ONpIa2bOtdPjs0x1AEzHf1QWeMQNTU5XzyXyVJzSN6n9goLTIRo7cZgNyf1hFBJy-NRV97HMbJZDGmPRoEl-02YI8yvGc6ZS85COKhRzyI_8-fRAlmLnek-w6-THHLLqFXQS8GSaU1hrbx4DTsB0Q3j4LYWySEAMEAv0I39V5Vs0WIOJbsTIhqxwMapgLMKGPiow121qFXwGjkzBiftsOtgBLUxYq1TNf2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آرام‌جوینده همسر سپهر حیدری کاپیتان سابق پرسپولیس:
برای پیشرفت نیاز داشتم پارتنر بهتری پیدا کنم برای همین‌ازسپهر طلاق گرفت. دوس پسر جدیدم یکی‌ازخواننده‌های خوش صدا و خفن ایرانه که‌مردم خاطرات بسیار زیادی با آهنگ‌های او دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/26685" target="_blank">📅 15:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26684">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YBpUXjINQzx2fOjf4y04nHGcvgRCr8mHjIKgNNSpJjc8asmpLCYllAQ3jKfveW9eLeMX-4U6RdQltbzCF0weO2q63IDp0zWkgctcN7_Eo5OEUyw1rmP1aTThtmmNJFdtqU9vi897aCu7I4xmUW6JNEPxFDPqmjCpkSSCnuXsJitPlQie2UjNJjNBGFA7_WX1YS7qI2z6bRVKoToW3qWwP0XkUeSnSIjf-eMCrMz6waCHGMQY5no_yOXhRxY6j-3Oha9AF0OWbVFmV18UhGjfxQafd1Zw4Bg7L_JDbDDykie_YFy9vb2YxAqXhQSn9fr9DnDwhU4cj2SfG_nlsC9DMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
خبرنگاروگزارشگر معروف ایتالیایی: فدراسیون فوتبال ایتالیا به زودی روبرتو مانچینی رو بعنوان سر مربی جدید آتزوری در یورو 2028 انتخاب میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26684" target="_blank">📅 14:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26683">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B6B4CTncacLnc2bdpKxQ3xpry_VNSYAlP17tQILgsXaOQ8KsV53FWhVZVG6sojXRo3Q7TmfKWo8dMFfPCfDpB2nh2m84jCih19epAq4SVeSCXeSwiybaLh6drwOkiYaXBeAOFhJpvTMuPWutHDomPPYsLbfZUSXden0hiwf9r3SICj6Mb2dGmgocRYrnEoS0_AO5UgVlsiSqXJ-b76ulhBWr9zsqJtm5QPNoomzCt4h_MLP_dE_g2HiRNpCHewa_c2m25tyVQAaw4PdshQEvDsESB_JeZur_qj9V9V_iDTE1Dim9SFl-z7x_r7LdqnJV4VTD_Av3MdX1sc0xti0O_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ دقایقی قبل استعلام فیفا به دست مدیران باشگاه‌پرسپولیس رسید؛ فیفا رسما اعلام کرد که هیچ‌مشکلی‌برای‌عقدقرارداد کسری طاهری مهاجم جدید نساجی با باشگاه پرسپولیس وجود ندارد. حالا باشگاه با پرداخت زضایت نامه طاهری بزودی از او و دانیال ایری دیگر خرید خود…</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/persiana_Soccer/26683" target="_blank">📅 14:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26682">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hdKduYnV642EFcI4hFF7A0Gc3GrBjWlvIngQa700mvMl5kJz5jRKZJv6EvZxUrHT0Fkrt_kjRuUg42eNKbczQXBT4u3bQlx0eoM3VtR76u-fTYkr3HfpumCM4t-9fWAtsXkUajstq8nFPyjUM04tHk7V0_l2WBPmrCuTWm1vi0avS6SYGolcW4tN43eTMaa3s0SV3jewOp6lmMeC6ggURF7KR1ymm3BXGH6zIdZ3ret2K0gUuvf-GZF-8w7V-MW96imA93NDM80iWCdYgdK8z6HH7BcNxjt0lSJGGqq8MEQuHhGJV8E6bIK3acsEgLZCNTH-I1YFyLAj53gRP2zm6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ ایجنت رضا غندی پور به مدیریت پرسپولیس گفته درصورتیکه درجذب این مهاجم 20 ساله شباب الاهلی مصمم باشند با 1.2 میلیون دلار حاضر است رضایت نامه رو از اماراتی‌ها بگیرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/persiana_Soccer/26682" target="_blank">📅 14:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26681">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s3GQUh6MM4wRwQp4UBAv-UmOarHzZzI_tjUxuEfIOXbFWnwABe23vBrRqhLMFuQ1xAc65z2LvvUPXhTpJIxVEp4SDsMTxrjxGmoAraAYJd8jh3Bb4DnTjmv1hi-lkT4-_UeGk9znhsaWEZnu3wtVRvbWJJI7S_MmY0eTsq7gf2L_gR6AbBcErj-VYM7CJNmtN80IcP4-vSTo36ZR46PKMKbIiuWsvXQZcH9ISSw1zWPU74Z_jFDld3AObxA4HVdXstvpAbt3uO_jhWluLxxPHCdT3srimbYTbFIhfi3REa3EAL8RDW88SWzljRBO_01tBhiJVNQnDskptpQZfbo82Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
مدیریت باشگاه پرسپولیس تا امروز ساعت 14:00 فرصت‌دارندبرای‌پرداخت رضایت‌نامه دانیال ایری و کسری‌طاهری بامدیریت‌باشگاه نساجی تماس بگیرند و گرنه تموم توافقات روی هوا میره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 78.3K · <a href="https://t.me/persiana_Soccer/26681" target="_blank">📅 14:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26680">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/txL9eKwwMWHPkhOENtHZ_oi124I59Bo5liASTpkPueyaFJqbbzwFMzVffS6V5yW4kuGWDZK3vp6mvFgAl5JWTBcyyMGSnHJlFSBThrHEIY8LsewK7rQAZJ7Bn4M7nBrKimaPFEVLmd18wk-g3SqgBvc90Iesyk4zVNFlIzP8fLat5DFRZZ4_OXp2s_s8Abf5tjSNb9uqh_lxRKysK9-F7EefWxADQPjUEDHiIMtos-MlaSEhR0WSSTlRbRKwO4Xlf2NzUZU6twt-3iscrY6DwchshIDFqdiC37oh79tmPEVNyCMiw0vybm14YhFtQA7o1wZxLNtb09W7lzUOXxApOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پوریا شهر آبادی، ابوالفضل جلالی و مهدی زارع سه‌خرید جدید پرسپولیس که سابق بازی در تیم‌های امید و بزرگسالان استقلال رو در کارنامه‌ داشته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26680" target="_blank">📅 13:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26679">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZNIr9PqhEOdQ7pP-E1W3z3D1NOtkN6oikbbGlkBriYUoh54Dkydot6aKmczjjycEzSKyXM0SJZck2q9PCwIQlif2bx_a7acj37vyrZb2DioDfrEV-XqmDHHxHQ1dckr55JzU4wJus9GJD7GobIBv_qoCdjI1Z23SguV88PR87hx_Dey5gdeL22-u2Jg5s63etchMRoDZg7nPzzgUbdXzQUbiWO3OnaPiNikB4C1wlIBkIwchLcqNhUz8wdM2kkc5FhCaZ_A1j5cKyfSXnpwg2_q87AVnYkOPdJc_1H491yq-3wblalWJ-H3wX9n74birG4GDzyO6qxZNhRpcaJjmUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی‌پرشیانا #فوری؛ محمد قربانی ستاره الوحده‌امارات‌امروزظهرجلسه‌ای یک ساعته با منصور عظیمی مشاورمحمدرضازنوزی و مسئول نقل و انتقالات تراکتور درهتل‌المپیک تهران داشته و برای عقدقرار داد به مدت سه‌فصل با تیم‌تراکتور به توافق کامل رسید. عظیمی به قربانی…</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26679" target="_blank">📅 13:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26678">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ApciXWaTGlIKVK78YTQVXONj31dVDj_rJkCct9hyuFF_8xGPk_ee_bMRrJFpF_aVxfovOT2jegdiWhXGQ4RIdol0xDhP4SfOHqmCkVdVebn-a09YpvfsXaZilUUhaWNklv_U5fjVlVDVkEWh8-6JMVOguj1zOKHd7qfSlfd5mZyjtrvzUU75ZsBZbRq0GnaZ4RRTpwg-l8NRhQwkMoHOP3J-4h80pH1NGNmNfQj-obSEPgFlXv3HBCDSnqCwJl4jtYCnnDhNcPKhnCdM1CNVBRhzT1uEvMs0pdzY-ohJUBvUl1rncc4p9XYVM8Aac_lxeOtGlQXpnv9r5V-Mk93dHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ محمدمهدی محبی تا ساعات آینده قرارداد رسمی‌خود را به‌مدت سه فصل با پرسپولیس امضا خواهد کرد. تمام‌توافقات بین محبی، اتحاد کلبا و پرسپولیس برای این انتقال نهایی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26678" target="_blank">📅 13:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26677">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N5uGRLyA8K6KnayJABSO5twvfCZR1Mx0Bo9N5AEDRodUMM2IwB2MhJTVH0rDbOXqGCZg-J_HDJXRbhz3zlcNbYQD4XgK64Q1zsFVIX-oOMKzwof2On3nFZZzJO_Ugcm4kM-6QuYvptKQyYr7CxcNy1qhgnuqjIWhwo7fKay6GvCJndHNGXwxAK2UwyuVfehaK-PJ2Szx6xpFi7aDQfNjPWQs60rmww4_0_uc2NKnHT4DqigtUUD3VUKxNsw2R41tV58X_UC6u_9qPOwaUUgURAQvV07sm0-6PTDVUYKLf9nSuUyKc6F42eXYAAXlV-1NhLbBAHC8N-zUJjfDdPSFOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
اینستا یه آپدیت جدید داده؛ میتونین تو قسمت «یادبود» اینستا یک نفرو مشخص کنین که بتونه بعد مرگتون در پیجتون فعالیت کنه و توی بیوی پیجتون هم میزنه صفحه یادبود و یا کلا اکانتتون حذف بشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/26677" target="_blank">📅 13:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26676">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v4wz9CHpYHt0FIUNF_s357illLzZd_U7IqAN8A4jlMT5mfMp4BQXp5sFtrngwt7Z4wwa8EHV4xrkUKFVfXwnrJbrYr9AEYJC-ZcB3U_hKhY9EiAXhqTdDcbubHBTO4IwpOQVp25PjopTwTuX3NjE7COsV8JZB_nZg1vzy2NnNxhAH64H_gUcPu96uAL4dyePJbJngD1CSWF6HxTuxp9zA7zNtj1_Dc7fxV3kX8M7B5tTYv6YlzyhVfNs1mZeBu4wiFg36t9sxzyotGLfbV1uNe4HwsGTgKXlHnTEzKGHjmwLprKFwCZb-nbhkVnmb5ljJpb5buMw5WC8SxRTAS72fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
باشگاه‌بورسیادورتموند درطول‌سالای‌اخیر عثمان دمبله، جود بلینگهام، جیدون سانچو و ارلینگ هالند با ارقام پایین خریده و با رقم‌‌های نجومی به بارسا، رئال مادرید، منچستریونایتد و منچستر سیتی فروخته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/26676" target="_blank">📅 13:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26675">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/llrYzOx1-Emt4ozlw2-q9rK6AkEA9s8amf85meO8zk7AgIQGefAqwTn0lWCpB64xUUytEik1M8sWJubytI8p4p-KOBTyptNmVVaTAQ7xy6pr-JeZnJPSTB4RCiqgjpy_Uu1rDNA-uA3ylWojWq1o1F4u74aEUT-YkEZis89DrrJ1t5n_HWq_ZFr-vzS_RLMfX2IlSL-Gyds31EiEl_pP2jYyX4YiasCWstj4ZDEYmnpAih-ctaVR1py6cvt0bzQFTQcFTyje186UTNyy_6OXBBCC5qJMAFGxXLGjOheZhQm_UUlirHWMusW8xek77KaG0USfvtIXZnsqpvoh1vhxiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌رومانو، توافق زیدان بافرانسه‌نهایی شد و این سرمربی جانشین دشان روی نیمکت فرانسه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26675" target="_blank">📅 12:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26674">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P8mw_pYgLQquK3zKVGzdG7HmmrXEZxQCmTGLY7yNemL4eoRGKDvrpoCUnvF6BY8DAuov1LrNYH1GJ1OH6CaSRpEQAt3HBFx-m7pxJc8DchJOCF8RH1zWbuE1vt4oWVtdtmYh9yCbaPUyURZRx4-lJE-gucjWXwp5K8--BjtGX0oDAL1xifpO1nEF-YRbbZxYlrKNKU16uwsA16CiHsVZwwacoKzxS2AqSVJPTqlHyKDDk8ExiXUSHKVzn9aDNk09uxZaEgem8wBUDY8i7Vh5vOrDIgo7JZDK1OWPeT1d6Loix50obi3jLCXzWw1Z3P_FcP32Hge1zFB7roLoedi2jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
عجیـب‌ترین‌تولد ۵/۵/۵؛ یک‌اتفاق باورنکردنی!
‼️
صبح دیروز یک نوزاد دختر در تاریخی خاص، ۵/۵/۵، چشم‌به‌جهان‌گشود؛شگفتی‌ماجرا فقط تاریخ‌ تولدش‌نبود! مادرنوزادمتولد ۱۳۸۸ و مادر بزرگش که برای مراقبت‌از دختر و نوه‌اش در بیمارستان حضور داشت، متولد ۱۳۷۰ و فقط و فقط…</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26674" target="_blank">📅 12:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26673">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AtmPQxEl0usVgaKCXIBgBsNk-1wzP6on8afUBIu1ZC2rF_RNY2nEEp08YejP5_QbUPD2NhhGf2shTCcfnxIoL8Rq_5y0iF3zXzK4wXwOQIGGpkVp6oNEQk_-AAA96dN5ExrXJsNbzyvfS8bUk4y1llyAS4s8evrJPkzVRdsIgda6xX6u7IckgsKcMkHnuvDzFpcYpPF0ActLazecVegmrBielFe12snSpGv10Oy98WdOD2Q30m5poNDAMNs3smMvlR0MvMYwFfrMvR-YBKAJaKIg3huVJN3qeWe-tBvuAeV0MSmwHjczHZ__HfV_B3SqY4bIpRTYhYBoVh7a6Bp4Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
«گونزالوتورس»پارتنرسابق«اینس گارسیا» یه استوری گذاشته و خطاب به لامین یامال گفته: او عاشقت نیست؛ فقط میخواهد از تو باردار شود و با گرفتن نفقه یا حمایت مالیِ فرزند، تو را گیر بیندازد. امیدوارم قبل از اینکه دیر شود، خودت متوجه این موضوع بشوی. گارسیا فقط بخاطر…</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/26673" target="_blank">📅 11:59 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26672">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jWR0ppIRrFU0xOhsfDdx0tVzd9EGjfmfWQmVRfvRcX73vFuonIM9nFDvLDiKHBZMr0QLfd9nv8hQ10X7Uc6UlyoFvwKhLinncegnTegC4wx2ehKmGNyUInihezICiMv6l5nt84SNPYukF1gF-5xUvanwJDkQAcdnfWHinZqjjLHhlwLOK45-4TRHnLcRY6HVTN1cZ_xTJovL0SPz-Gkp0XxAwoKFWjTSrjjKIl9sTZsqcsOS0NmwRWUTSOl6YGuzT_rQus4-qs9wtZ0rPL7Vrw7vKuVqvvxqCS1RNDCdJDIMR4UvQcxGL_tmVJoD2KEG-Ia5CqJxwtuz2DHogVYFCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ اکثر رسانه‌ های یونانی از جدایی قریب‌الوقع مهدی طارمی از المپیاکوس خبر میدهند. این‌تیم‌چهار مهاجم داره که گویا سرمربی این باشگاه تصمیم گرفته طارمی رو در لیست مازاد قرار بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/26672" target="_blank">📅 11:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26671">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7fa18a77b.mp4?token=dPGuy40l4HZMrbB1WAIpSj9NHwsVV_-Y_zIPoSFy773Ls-zd361XoRNets9IQAcPt6NLRRw3LJEhsKMo8tJt3QKI5is5RHod_IklkK9kCRmOTm4QyWUILlvEjiIJck7p6YHNbSd45o81dkBSpbkBcNei-I12tWgSrllQgbvE6syqxCFAYm8070rahetoljIvzQ0cyU08LYg4r6hV1-ZXnn4tK9dnti6ZxmLaK1iwH-ybNQaO_k6hzuJabe7bnU0pFTwJMdbNuzmxfSSCDCC6j7OqmAGdK51gpRRvg2mhag7WTtBQsQBvjyjwcPwxgcN5kJEi95_ZzfoaT2WV61dl7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7fa18a77b.mp4?token=dPGuy40l4HZMrbB1WAIpSj9NHwsVV_-Y_zIPoSFy773Ls-zd361XoRNets9IQAcPt6NLRRw3LJEhsKMo8tJt3QKI5is5RHod_IklkK9kCRmOTm4QyWUILlvEjiIJck7p6YHNbSd45o81dkBSpbkBcNei-I12tWgSrllQgbvE6syqxCFAYm8070rahetoljIvzQ0cyU08LYg4r6hV1-ZXnn4tK9dnti6ZxmLaK1iwH-ybNQaO_k6hzuJabe7bnU0pFTwJMdbNuzmxfSSCDCC6j7OqmAGdK51gpRRvg2mhag7WTtBQsQBvjyjwcPwxgcN5kJEi95_ZzfoaT2WV61dl7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
🇦🇷
پائولو دیبالا ستاره آرژانتینی آاس رم قرارداد خود را به مدت دو فصل با این باشگاه تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/26671" target="_blank">📅 11:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26670">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">چرا
3️⃣
2️⃣
1️⃣
انتخاب درستی برای بت هست؟
🔢
امنیت و اعتبار بالا
→ چون ایرانی نیست، مثل خیلی از سایت‌های داخلی آینده مبهمی نداره.
🔢
سقف برداشت
→ در ریتزوبت سقف برداشت معنی نداره و شما میتونید بدون محدودیت شرطبندی کنید .
🔢
بونوس‌های فوق‌العاده
→ اولین شارژت 100% بونوس داره، و یکشنبه‌ها هم هر مقدار شارژ کنی همونقدر جایزه می‌گیری!
🔢
فعالیت بین‌المللی
→ در کشورهای بزرگی مثل برزیل
🇧🇷
، هند
🇮🇳
ترکیه
🇹🇷
و بنگلادش
🇧🇩
فعال هست.
🔢
اپلیکیشن اختصاصی
→ با اپ اندروید سریع ‌تر شرط‌بندی کن بدون نیاز به فیلترشکن .
➖
➖
➖
➖
➖
➖
➖
➖
🚀
لینک و اپ رو همینجا براتون می‌ذارم . برای
جام جهانی
هوشمندانه انتخاب کنید
✅
⚡️
اپلیکیشن اندروید ریتزوبت
👇
🌐
RitzoBet App
⚡️
لینک سایت معتبر ریتزوبت
👇
🌐
RitzoBetLink</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/26670" target="_blank">📅 11:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26669">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qhqp9vBJai-rdu8px4AkGoK1NtVbR46OD_gd4qanj8c64wc3IHebChtLDVxfMxFo4acCa50htZctjr7DNz6TWHEjXaVHXJRnnXD_rUDuHT0eH8uNqYh17OkKsZt0WLLE56KJs04ZZhPGd11MrkOYqgaH-BVVlPenL8CmTuM_DgudRuZWGWlmUpAQxOFeaDZMYw18i2ZowjfP5PIo2vTvJlVFo-x1m53qu0XOOavIn_7PHRM9RCA66r_sGv5axXU8Iaqxyz7m8Qa55QdMEYuuq3VFRNu8sWgZQtGILjPMH_WzsKlJkzcK56CWl5UrhWmO8J99daN-WGhlEwh9doa9Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وندا اکس مائورو ایکاردی: علت‌جدایی ما این بود که ایکاردی با شغل من مشکل داشت و شکاک بود که باعث میشد هرشب که برمیگشتم باهم دعوا کنیم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26669" target="_blank">📅 11:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26668">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HoDS9wBqEGASL_wOEqhh9P9IyneFuwHZpYm7IKVA82ZAF04DouV7a61aEeD_eT8cEd6X1tGQons6JDtmdm88_Vqp7Vt81N1p7Hvq7VPXm8-CSra-I1ZHjBHHwy4pX7iv0koj8rilXR5hS39eyB7AbKlX0QiNgORPQbLQsrUzBT__hUvf66PF9mbMIMdxWNEU-8T7nGWoytmHfs5wJKw_wY7UoLuuuoL0npnb1L6VayDMB01jwu10tTqcLJSAwbX_iljAV_dVs5UGu43DvGYYV9lFjFjuveE5fqfoU6ZzTQVNEBqMlpI0ZK7w5U9Ls8k-1W-zMKdQ4WnP2ev3crLnqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
کریس رونالدو قراره وارد دنیای سریال‌ها بشه!
طبق‌گزارش‌ها رونالدو توی‌سریال‌فوتبالی Day 1s که با همکاری متیو وان، کارگردان فیلم‌های Kingsman ساخته میشه حضور داره. جالب‌تر اینکه رونالدو فقط بازیگر این‌پروژه نیست؛ خودش یکی از تهیه‌کننده‌های سریال هم هست و در کنار دیمین لوئیس، تیری آنری و رپر معروف Dave ایفای نقش می‌کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/26668" target="_blank">📅 11:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26667">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bMKRjzRKIZ5CH2nhi-TFX1Yug3tYb2F9Ia_I6d1iYschMovi7nUs10v84JoxgtDlcR2KFetXPN6GlQ6B9HZOyl69KuszZdGUqSmC55j4acirMcQsw_sfPloYI8Wts5-C4QRVUc5qR-e2ux0XuRSJdLEzPSMZmbkNcpmo43b2F0UrYL2NjkYyJO7gSfQk0l9DqvhcgIpDLz1wkHs_l39FN2nM7vAb1euYm8ig7nOF72FeJlDFMZ2aQGJ-4AL1-J0_haOXxb1A7dpH2r52bMzfptU1oX56Q5EO-MeupZwAG5M__FT8U8Ig9yTGXbRqM2VzOcSS7xZ3T_k-ziLZWSkHmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
مدیریت باشگاه پرسپولیس تا امروز ساعت 14:00 فرصت‌دارندبرای‌پرداخت رضایت‌نامه دانیال ایری و کسری‌طاهری بامدیریت‌باشگاه نساجی تماس بگیرند و گرنه تموم توافقات روی هوا میره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/26667" target="_blank">📅 11:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26666">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QpWugJ_kYQhkY4JwCnXn7vF9mFfklfwE-6em4XupR7MNtKtTRrYGOFbjFTtRvFzmY60Ic4S6Z-boYPXBAt5iutOIttrADjrpqBfYKqjTj8QkB25VwdFQyV0rCY0OLcaywYspmPm2xjQDbpo0AZIoRzmnfi3kcrX7NLCepMv8Zx6Anhzf1zW897D2plDqsDzuV_YokteT7qcic-4ONCovW8hlCyph_Zc9ODhYNmfQrbiim9xpSCvanV4kPBdWAok9PQvp8L99m-gRqNuiqFHIMG_J2jlWJ6hUAX_3Szeh28gzhBqRsKqJy6qeiYTNyJrH8f2eC-pm_TYiLb8IYeX0Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
فرصت 24 ساعته نساجی به پرسپولیس! اگرپول ندهید دو بازیکن راهی استقلال میشوند!
‼️
علی تاجرنیا رئیس هیات مدیره باشگاه استقلال امروز ساعت 11:00 باشهاب زندی مدیرعامل باشگاه نساجی تماس میگیره و به او اعلام میکنه که حاضره رقم رضایت نامه کسری طاهری و دانیال ایری…</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/26666" target="_blank">📅 10:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26665">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/snTkGJF3_5DOx6FTdnk1WcCfjv_HocVNi7-bOc8mlQgszp2OMMfZWcPgkNGkTPlrVJlCIvy9YXha8vBKBEo-5KnNLKEHqzi37AnXGTe_-VZFXz4EeKHJZ00f9lAxJc_1uCsO-lIn2CRfGwP5PBjIJswCyUZCDL0DvQmArRdpjtHNtOODYTCwqfGCAJZn-uXLRFDnCFXZQygSpnWzcyuQ39NexeQwfX3-ifuhqeQlLWslrtT4H87ke4X7_QKYotSQQJzZ1bW-BNiY0HAukFbxoladCs9dyAIWEAJ_2ZrLUaby5Dxl9wgkS4fHaAVzW7hRc7GO7-2yUv7F3-Mrh7ttpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
#تکمیلی؛ محمد محبی هنوزآفر ارسالی باشگاه پرسپولیس روامضا نکرده و مدیریت باشگاه پرسپولیس نیز همچنان منتطر امضا قرارداد توسط ستاره سابق باشگاه سپاهانه. هرلحظه که امضا بشه سریعا توکانال پوشش میدیم. توافقات نهایی انجام شده و فقط امضای خودِ محبی باقی مونده…</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/26665" target="_blank">📅 10:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26664">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dfGO96eNwvSkxBRIq58ga65QEWMITM5FMwBsBorwWxra9liQgFv6rBq-SpKbFeA8_eT2Dvj9Vwl0jwdoAH_m1_7bf-ZhucA8rTabnPwoTbdkmHNA3lKtgMwLaCoE-dzQmgWTgAXK51npgZBja7TzrWWktU8EESw9bVUBg1N68G4BN3Ee5i8R5K9HFjWG0NJWALfB7u7MKzk67ytJ0wVMS655e1XGUWwCSzyCJ7uF7Pi2ZKiWPGFv-pUJb6PmNDMTNnb83YJEu2cSKNAo293GO2bUVYlSYG_4Ez5XTyt-WPyC2Py8YA8CTJm994-8P0zDv6sVQWkeePa8DTMxo-eJ1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام رومانو؛ پائولو مالدینی اسطوره دوست داستنی باشگاه آث‌میلان از مدیرفنی تیم ملی ایتالیا استعفا داد! گویا قراره از بین مانچینی و کونته یکی بیاد بشه سرمربی و مالدینی باهاشون مشکل داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/26664" target="_blank">📅 10:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26663">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b74f72d96e.mp4?token=m2B3rK7vPnaR7Z3Gq_TCZK0jeVSBYcRmxALBxJt8VbMjO1_eFkG99whsJkxoWEMkUobUogLgKFopA0PHoxzTffXfdop6eL86UXa_2TV9kbGNikVM8BC_A7zxnRXdnMpdxVE_uhJfU5-EIZnBLeLHdlGVADGfWMCTSS-xgcG0xXulXOyIPAp-xokIcGgx6ish8Zo5IAAuFifTOYwt2koflkBh_8X0upf8B59m1xWq3qdhlV-i0tkmFjDR-0ZIV3NfU553nN3tR-JoQrAtBjz3W444eJ407pxikyiTtapLgj7oHz2JGCA4We8bgPjTJX9Y8KI1md9abyLl1KdCyi6pT0pbhEYjZexK6u_hswGuga6FUQhjn3R-lFA9bCl_WKxE43soM0STgvxXEvx9BgK65vdfrYx8qk3zKROE2Hw1PS6bcM2eIxB5yb8YxDC-vOsWDVjisZNgtSw2qS5xts1E9cihZkHC5UncrJ1iYDPhL8_YGpKZVsc8MI-K7SZBSO5TUB1_XIJGKYPcU_lPv-Tg--0r8saEYC_2bfQukBtnWsUXcBpHEAl8gOqdzUkbpfO4_0lK_0uf7oxTycLPKuTX6xhe2jyGvWNxE2CccXcIRj2v8PQOeMOKEIbmqcjlDOdlNv3B_1t1TdqibjhW96QPfY5x2y3EqGU85OKtdL_JHpc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b74f72d96e.mp4?token=m2B3rK7vPnaR7Z3Gq_TCZK0jeVSBYcRmxALBxJt8VbMjO1_eFkG99whsJkxoWEMkUobUogLgKFopA0PHoxzTffXfdop6eL86UXa_2TV9kbGNikVM8BC_A7zxnRXdnMpdxVE_uhJfU5-EIZnBLeLHdlGVADGfWMCTSS-xgcG0xXulXOyIPAp-xokIcGgx6ish8Zo5IAAuFifTOYwt2koflkBh_8X0upf8B59m1xWq3qdhlV-i0tkmFjDR-0ZIV3NfU553nN3tR-JoQrAtBjz3W444eJ407pxikyiTtapLgj7oHz2JGCA4We8bgPjTJX9Y8KI1md9abyLl1KdCyi6pT0pbhEYjZexK6u_hswGuga6FUQhjn3R-lFA9bCl_WKxE43soM0STgvxXEvx9BgK65vdfrYx8qk3zKROE2Hw1PS6bcM2eIxB5yb8YxDC-vOsWDVjisZNgtSw2qS5xts1E9cihZkHC5UncrJ1iYDPhL8_YGpKZVsc8MI-K7SZBSO5TUB1_XIJGKYPcU_lPv-Tg--0r8saEYC_2bfQukBtnWsUXcBpHEAl8gOqdzUkbpfO4_0lK_0uf7oxTycLPKuTX6xhe2jyGvWNxE2CccXcIRj2v8PQOeMOKEIbmqcjlDOdlNv3B_1t1TdqibjhW96QPfY5x2y3EqGU85OKtdL_JHpc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی‌خاطره‌ای‌انگیز ازسوپرگل‌های لئو مسی از روی ضربات ایستگاهی در دوران حضور در بارسا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/26663" target="_blank">📅 10:12 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26662">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQlON_82FxRKcC1IBwlABnhWHNu0qrjieJvpcCz9ZPur42-DkWXLydoWx37kCwjMozC7gIdqPfbajpyosR1yBpBtVkoOA3cjKBgnnGLhAeab3PjDqsBkU6yavqbPbHyWlWCc1mYT0IHw2KbgOG-JgySXq0PM0Hd8YQvvn-S8XCrj9MhrLJr7QpEufQ7Tl4qYhC6GIezHqLM2-tGDVJdTnUvLHD6OJSMgpPzH9pgMAPkS0tT_q92sgMiwWBxm-H1MXGwRdbYl0GfeCYQrARsXu8hMJ9rFlQIPFt-9QRcsOx8j83tVS0ilK_6xop4KN9xk2Aeo2fW5GNYmO_6pbHcttg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
یان دیومانده؛ از دزدی سیب‌زمینی تا تحقق وعده خواهر مرحوم و پیوستن به رئال مادرید.
❌
یان‌دیومانده‌وینگر ۱۹ ساله‌‌ساحل‌عاج پس از ثبت ۱۳گل و ۹پاس‌گل در ۳۶ بازی برای تیم لایپزیگ، راهی رئال مادرید شد. او در دوران کودکی شرایط سختی را پشت سر گذاشت و برای رفع…</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/26662" target="_blank">📅 09:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26661">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVQzSIUDU5IPUM-rZzfwhhiBZWHknKIc0Ka7QBLEKytg7BoYRkOf0o2ytR2z_gc60D6CViDMYPHv6HNVhhNu4caFYAbIfgEHCxOO1sfOfQu4vvnKBw2pxo3QDw7qiNsgtJc_y5xYk4kVR1yA-u2465FxPAKSMAIr89Xs5Wo-PDCKPwOqoUde0rD9X1ptaY64tWTxiaLycvNzuuwLmXDEZRPU5i-tQ96sxF_7Pk1j2LB7UEt1yQTx7cX8j6pnurncA2dN9jaZExd7AJkTSII8YxAJJexGR7bUgd6oM0Qy-uzbog1BuLaOv4L3g9Uk-S7MYUCHxuSy1tjvwZl_tlddYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
صحبت‌های جالب مهدی ساداتی گزارشگر شبکه پرشیانا درباره زندگی قبلی دوس دختر لامین یامال. بزرگ‌ ترین خیانتی که یه پسر میتونه بخودش بکنه اینه با یه دختر متاهل و متعهد بره تو رابطه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/26661" target="_blank">📅 09:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26659">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZluhxNGpOYL3IrA7TyPWTvyaxILAXoN1qku7IELWbPtx2XojYXCfCLWKx9-gA-KtVU5LjNq6TL2uGIPS5HqCRwRaPCulIpmP7_eo1QSwCJbUyuoKQLdJE4D2OyLA80Mbvo7dJa38T7VyR7YIHcjVaW0GGA3-0R8Z21_T3c_OG19coHph0rOCjhn_2L0_9rwPsME7DlCNy_8gnMznBYmVnumAWO0PmhGPSyZ-q9QX07BhsqkeQjG3ahGLg4bJmGteD4QiOgxpOx8t329MaSxUUT0uJ-FeBTYcF8Lqr2ez8gfcq9LuDBMiTBwer5zcjXfy1o_3RcPAoJcKyt8B5VMLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
با اعلام رومانو: یان دیومانده با عقد قرار دادی تا سال 2031 رسما به رئال مادرید پیوست و مدیریت این باشگاه بزودی از او رونمایی میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/26659" target="_blank">📅 09:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26658">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8feaae9b61.mp4?token=CfxmozsDnl5pixo96hIwtF-daxu96AVbm9DuHp5fXFR73DplMsimuMGOAvKCTFqp0xzKXQ2-hq9zQcsZYjf8SIW1sVEvUkVD2WxweSX0Ry4kh4Gys4jAK6dltx38bt6t2T3WBAI42Y6L_C2NoHURXRzVzKMhNtr9keBrKTfd43e1JooN0Ni32Iz96cLVahgKeVtuWGQZ-U90PWoWrIJNTtQvVOticwtzSZ-gx-VWK24IJKS_FDwC2eeCc3atxp7WpPJkvi3sx0G2CmtwgCAYZYflSsnux2z9B9b0s2-OztBnK9Evl9xo81QcPxegy5Sy_MaXfTXLNcUJOOcutOJWlX_0v4n44ge1GgKdr07sxVl_CfVCuG5Jg-CB_mGxChmb7zpuOkVzozVWfzU2eW6LI1Ea001HHFt527-rhAHJaISFBSiBoCriBgaf0oDrzf2Q65H8NtNJ025LudbWPVRWLi3XNdPTN7xUl_rYjaT808UcG_DU6LALekvh-VixYdCnArA4wLyV0--zPPzhDpG0IQU_JTHmtnhjJ83zwqJiHyEZmcp3HH7z-apEW_zrCPioQPuovOMU1K-zvTS9Wvg2Wj6-LuBDOJgfdQchYq9xvNsTi2sFI56eAIeN29bQnaAjz37OjfCbUIZAdpt3_G2dj5qfbnzNRgTfDwtZtsmsOnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8feaae9b61.mp4?token=CfxmozsDnl5pixo96hIwtF-daxu96AVbm9DuHp5fXFR73DplMsimuMGOAvKCTFqp0xzKXQ2-hq9zQcsZYjf8SIW1sVEvUkVD2WxweSX0Ry4kh4Gys4jAK6dltx38bt6t2T3WBAI42Y6L_C2NoHURXRzVzKMhNtr9keBrKTfd43e1JooN0Ni32Iz96cLVahgKeVtuWGQZ-U90PWoWrIJNTtQvVOticwtzSZ-gx-VWK24IJKS_FDwC2eeCc3atxp7WpPJkvi3sx0G2CmtwgCAYZYflSsnux2z9B9b0s2-OztBnK9Evl9xo81QcPxegy5Sy_MaXfTXLNcUJOOcutOJWlX_0v4n44ge1GgKdr07sxVl_CfVCuG5Jg-CB_mGxChmb7zpuOkVzozVWfzU2eW6LI1Ea001HHFt527-rhAHJaISFBSiBoCriBgaf0oDrzf2Q65H8NtNJ025LudbWPVRWLi3XNdPTN7xUl_rYjaT808UcG_DU6LALekvh-VixYdCnArA4wLyV0--zPPzhDpG0IQU_JTHmtnhjJ83zwqJiHyEZmcp3HH7z-apEW_zrCPioQPuovOMU1K-zvTS9Wvg2Wj6-LuBDOJgfdQchYq9xvNsTi2sFI56eAIeN29bQnaAjz37OjfCbUIZAdpt3_G2dj5qfbnzNRgTfDwtZtsmsOnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
🇪🇸
دقیقا
20 سال پیش درچنین روزی؛
رود فن نیستلروی ستاره‌تیم‌ملی‌هلند با عقد قراردادی به رئال مادرید پیوست. این سوپرگل دیدنی او رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/26658" target="_blank">📅 09:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26657">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qlf3SyU2ZpHDSVApg0Ks-12ECN7UZf3Xq2wouRWnQN-QY62GDMiGbZ8HOcA7ZcAC2u9V0uXS-6wF-MafTJuZ_UwsLrE08Pgt7vVTggltSB7_x0KTISnw0XDI3ja4C3BYItXF65nrfb2EZg2DdbxxEFulb_Ae3OwTaiLPx31A1_zJphi0CF8c72Nz8tirUsNdb2rR4Zrp1A9xNhtYu1SO6pYyhuHFMBgPxMgV9NQaPAiHoZNaUcuS3v3HN9On91g1E7FY6SL2-l_R3BNcjnN82u_U58JDqDGj4L_qJ0kEEmP9calBV-rWR0WQt5Do3AAjnzabHmcfWzEfPGmh8z8SVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ مهم‌ ترین دیدار ها‌ی‌‌ امروز؛
بازی دوستانه شاگردان ژوزه مورینیو مقابل لگانس در مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26657" target="_blank">📅 02:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26656">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMLKYweGBp_sS8Iju1yqsifsEtvwHbhRvkY7dHSylPcDCfshD8CWdsWvD7-Me7gZaftSXGewwqExCUFr4fFmkJJOfz4j0_0yqaMEFNwotMxvIA2Hg49lTiAyd9LbkWUA0_Cuav547CfZCo50DAZWXRcZS_gihQdQQ0ucpEhFbhogaLSjdksXVvzh6-ZbWfOYLSeXYaMI70BtbJl_e-QZK3lmJsGERbqt0nZu9RrA9RyIuFdAgQJteIiiZbR9ULvdEMn1w3Do9OdzhWY04CTki7HaUlIcQlri76lT2hsHzfYW3esj1Zr9plCVlixxKmEnWr0drvJP7Sg1VY8-fINotA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ میکل آرتتا سرمربی آرسنال تماس های خود رابا وینیسیوس جونیور آغازکرده و در تلاشه که اوپیشنهاد تمدید قرار داد رئال مادرید رو رد کنه و به جمع توپچی‌ها بپیونده. نیمار هم به وینیسیوس گفته جدایی از رئال مادرید یعنی نابود کل دوران کریرت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26656" target="_blank">📅 01:44 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26655">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47adf0f058.mp4?token=Dq6J-2_Wft8Fm21A3xbusNQ_0lxzXiZTix0k9D4KaM1aRfIyy1hO-N8Su7NAOxkCZ7L_6ikkAuOC5r73bx8LKFyqHUOrMNcaOqkX3-YgVx6ckUSPIRdUq_ygCz-Qrvme87mUlvyi8BiK35NZxlGou9nK8LOtCfLtG41fFChjjK55N2ssTyv98sOjmpjC565UvRTRsJqJcoie3HfsS1XaAG8zdP4KPNLsHMu2w_WPBWgxSKrfiHQAx3jNqOJ3YUYhZoJYZupoai8HWsA8EazdYt16BJ19S_rdp8dgiECQH56Mq3DxUi4rW0XSEtTBwcrBpIoWmLOZh5Jv_3lixMxjrH6ggtxAzF0aWxLU3IrqBW-szMlH4Wpw5f5nye0ibd9TsqBFj2zoY5UoZ-yNeYc-yEuTzb-a0Soopy0YLkKodQYhrnYTZBx_PpxA4Z3YPirpB6XhfEFqPkOjKGRWXMZx_7k1psh-WZVd2Ozk9wXZewtLIzew7BNn5UH58nPAvkMz1kEjdgWVZrUZruISDFNcfmegU4Cdxaue1uTB4hjeuGdngLMplDKYVxtvTKVftZ98Mjjl3w8gTQ_GH40ZwsLAj899jkm7kpwQUbTZBWran4kk3gOHcqIshUWfKVyJ5rSjFk7wAiP-Momz3GFgcIP5NrA_m9TTiktuGoLDI7PNTqo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47adf0f058.mp4?token=Dq6J-2_Wft8Fm21A3xbusNQ_0lxzXiZTix0k9D4KaM1aRfIyy1hO-N8Su7NAOxkCZ7L_6ikkAuOC5r73bx8LKFyqHUOrMNcaOqkX3-YgVx6ckUSPIRdUq_ygCz-Qrvme87mUlvyi8BiK35NZxlGou9nK8LOtCfLtG41fFChjjK55N2ssTyv98sOjmpjC565UvRTRsJqJcoie3HfsS1XaAG8zdP4KPNLsHMu2w_WPBWgxSKrfiHQAx3jNqOJ3YUYhZoJYZupoai8HWsA8EazdYt16BJ19S_rdp8dgiECQH56Mq3DxUi4rW0XSEtTBwcrBpIoWmLOZh5Jv_3lixMxjrH6ggtxAzF0aWxLU3IrqBW-szMlH4Wpw5f5nye0ibd9TsqBFj2zoY5UoZ-yNeYc-yEuTzb-a0Soopy0YLkKodQYhrnYTZBx_PpxA4Z3YPirpB6XhfEFqPkOjKGRWXMZx_7k1psh-WZVd2Ozk9wXZewtLIzew7BNn5UH58nPAvkMz1kEjdgWVZrUZruISDFNcfmegU4Cdxaue1uTB4hjeuGdngLMplDKYVxtvTKVftZ98Mjjl3w8gTQ_GH40ZwsLAj899jkm7kpwQUbTZBWran4kk3gOHcqIshUWfKVyJ5rSjFk7wAiP-Momz3GFgcIP5NrA_m9TTiktuGoLDI7PNTqo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اوایل‌لیگ‌برتر
؛ یه‌باشگاه‌‌ایرانی‌یه‌بازیکن خارجی اورده بود "روزی صد تومن بهش میدادن میگفتن برو سر کوچه فلافل بخور… نوشابه هم نخور!"‌با نوشابه میشد ۱۵۰ صبح‌هم بهش یه بربری میدادن با چای! تو یه بازی گل زد یا تعویض شد، یهو فاک نشون داد بعد اوردنش نود که ماجرا چیه، اینارو تعریف کرد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/26655" target="_blank">📅 01:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26654">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uL1n5zYhbeyTXvN3OOCkx0c8h37cJAlu4cw4gXXWQkDa76refZ65uZMspzITsaIpZDCuLUag82ofOZxGVBMLvqzazuSygsslSYFExR6tLCQCF__26L_zeMmLWPRDMl_t0y3V8XTNt_ip0VPvum0gSh7Dm3nEUXGeAyrVEarhd1nUJJYMuSWwmAdQ4ysj1iZsWA02oic1qQDNt8nF-M_Uwcwv7o6M8_YwQoj33zAKyT0l3qQ1rpRXxxG7pnkbRzefr1IQVof9X0GJQgjFJ2QJfwnhfLO3_rJv_2esShHWsqMuNOYpOXjZ586CNeDKbPCXhvecd8-aT0OSDbdl_vCl8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فلورین‌پلتنبرگ: رئال‌مادرید رسما آفرخود را برای تمدیدقرارداد به وینیسیوس جونیور داده. آرسنال هم بلافاصله اولین‌پیشنهادخود رابرای وینیسیوس و رئال مادرید فرستاده. حالا تصمیم نهایی به وینیسیوسه که کدوم باشگاه رو برای ادامه فوتبالش انتخاب میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/26654" target="_blank">📅 01:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26653">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fUepIvp1rCGov8MMtIs7rWEiJzTa2NdF-XjDJ9VT31ILHZtRVIrJXnoOTqXeJIPw_A9pg-nix_-WQdvyk5DAfU7R13rLIzu9j_NwRdKqAxg5AcrW5N1XBYM7GGToPKL08pSxUd8FxZavPIFg47W9Xb861ixx8KVb4b59FlmJUsM7K2Y-ncDn2hu1xO1uVL_BI1CbWw8OUXZZdp8R1JfWlHJc-4UCAa0ZGYT3v5Njkoz7KaJo50e0wJCbSMImMa-WlOAdHTCbG8f5_ZuqkdNbfuMrpqNHWt6EIt0BbMtE3a4MQ-RRWN0jZLDKCf7KgUnu_Mu0Ht4KYhIgDtacIj-NlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
حضور کوین یامگا درتمرینات تیم مغرب الفارسی مراکش بدون استفاده از عینک؛ معجزه خدا تکمیل شد. بینایی او صدرصد برگشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/26653" target="_blank">📅 01:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26651">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dW70tAP9A0_0O8pfUryhs8obk7jbx1eP7-Hacx517_jHCfnMq6DxLHhjW1MCtyV5SEWVDQwbbLINR7z3WrSfLvyJNxXlcodYnl1GxKH5s5hgFOIA3RtuBJZf9hWKpYa6ZIMpjb6EHida0_UqtLG2tW9Hl8YqDsHalifNOXDCvu8yL6wdUPDTGBtnNNY6Ahnq1dyfZeteK0exx_TPsOB-Mf_R1yUqvgpzqI-7_uRdEqzs70wqjxdn82924z8M8YbYvvNIiR7Ae4Iuc0hCCSyy1jiYUzwf-nbZ_PV1bYjcRUNAU4AvOjy1wnrzB9Cf3zJd-2A0O9ol74q5G9oIj3obwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇪🇸
🇧🇷
خوزه فلیکس دیاز: باشگاه رئال مادرید برای فروش وینیسیوس جونیور ستاره برزیلی خود رقمی بین 160 الی 200 میلیون یورو میخواهد.
‼️
آرسنال آمادس تاحقوق‌هفتگی بیش از 450 هزار پوند به وینی بده که در تاریخ این تیم بی‌سابقه‌ست!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/26651" target="_blank">📅 00:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26650">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/185f669e03.mp4?token=tyx4ekd-t8cRnm-irIe7jOx_qypo-tEM-o_GrHEHeVYz5MadR7wpaxr0CnfXVY5pGGrIj5YjSiD55OFt-kRZHkt6AP28hffby-iUqQ9s6WA6H7gw2hfUk5JwMGQZ9AXb4lAqB4bPAZW-Gns7x931e_al-obEQHUcIgAfJQ5GOSMxw7cjh88v3saxqB3GgS9HkAh-cZWVZ32k1qsIvSBMneeVbUFl4FKb8FJIvaF4rJgdc5ptu62xh2Mtia4wK0dDcAzGGmCkTS_miJQtnGKe5f3Ox_Vt9D9ZvOHBetbbUuj5HU_XCqma7697ppPm2-jtONXrJHDmYllI0TuNzr8niA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/185f669e03.mp4?token=tyx4ekd-t8cRnm-irIe7jOx_qypo-tEM-o_GrHEHeVYz5MadR7wpaxr0CnfXVY5pGGrIj5YjSiD55OFt-kRZHkt6AP28hffby-iUqQ9s6WA6H7gw2hfUk5JwMGQZ9AXb4lAqB4bPAZW-Gns7x931e_al-obEQHUcIgAfJQ5GOSMxw7cjh88v3saxqB3GgS9HkAh-cZWVZ32k1qsIvSBMneeVbUFl4FKb8FJIvaF4rJgdc5ptu62xh2Mtia4wK0dDcAzGGmCkTS_miJQtnGKe5f3Ox_Vt9D9ZvOHBetbbUuj5HU_XCqma7697ppPm2-jtONXrJHDmYllI0TuNzr8niA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های‌جالب بلینگهام از زمان‌ بعداز پیوستن به رئال مادرید: کارلو آنجلوتی گفت فکر کنم بلینگامِ اشتباهی رو خریدیم. باید برادرش رو می‌آوردیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26650" target="_blank">📅 00:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26649">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U2LjSGXO4SudXRPZR2MsOltg50LkIk-AKrKJqwxe1cHZH-Dn-Ph17KmlTxkd8lvgkxYSH39dLJJfdXJ13pTzkDBtSL773P7GpOq0TbMPKRJa0F9hc94Ic58Aou5npt2DHBvjmWzq9Nwy65AxR25IEgIMKVvadAzDIMCzAuK0MsRmrP9fpDRg3ZLIpfmScV3PEVi43tGGcXAR1-PGTzBgE2j5Cio-f4YRpuIRtBegiizdfONXDuitMpheDdmwvL2UffxKNVNeHCp2Ukg4DybCqQxjPNpW238ZZPCJsWQneqcKcblji_x51Y4y-pMkf_B9uS3jisTo6kFW_cOm4vB07A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
#تکمیلی؛ تمام خبرنگاران معتبر خبر از عقد قرارداد رودری با رئال در آینده بسیار نزدیک میدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/26649" target="_blank">📅 00:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26648">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h6nSJv5H7rV7LTeikO-pJ83BSNg7wC_dgb8d9kx0e70JMhBG8VzLi-YCTg46ppWGqMzTVddHf5_xDiQQsb0RHofa6TvTDNJxm6Jcxwush9MAomYuJ-Ghz_6BeQLhDr-3NpUAr7fwK12AiFswBbfcCNVH6MfifC2nY6KuyuOUlwmmeVPhZjnqUPTJ3ZuEzyD88UM2JmP3DW_lCwY45A1nvGPzOGvvZeJc6BejDhaN9GkFki2dgqT0nYQqANUi3LVMLGaGBZgDEWttpn-IdrvwAlhvHvZ1ga6zRTdQscBbLIy6dYwhDTudr1UOP1qm2LhMOVepxhna0bL24ZSZBRWJfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جان استونز مدافع میانی تیم منچستر سیتی برای عقدقراردادسه‌ساله با اینترمیلان به توافق نهایی رسید. استونز به‌احتمال‌زیادجانشین باستونی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26648" target="_blank">📅 00:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26647">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rdPqL6nxZkH04-KcyadvfYV2ZcydNhgGc_0ENuvAtEWYP07Q8cswSXXgAdMaVTIlZtqwrgJfi-P0lW1etQJqdp86dyKfOwHNcU88lSquSVW9-K02hPC_DyTKneUf62bakB_fGFDlpl8PlP7JhA_8w1tnk8-uDpIIUP7CPP9g_ggqzdhMtLp_ZU-7-XXpKYJPYjZ_St_MXFB_2tySisie8MMhH8GwrnnGjYciV_mrfYzHoiUHP1km_1BsOZHxGbiTy-fKchQmxi-ePToTU2deEw4vbDCStXRJr_RWrWvRMxF0quL5KFNGOwQvHNwOJbfkmqx8neWhAv6bmPnjZXwQwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
امشب‌محمودرضابابایی ملقب به "بچه" به رفقای نزدیک جواد نکونام گفته "بی ناموس عالم هستم اگه اجازه‌بدم‌باشگاهی با جواد نکونام قرار داد امضا کند.
‼️
سرمربی‌سابق استقلال ظهرامروز با مدیران ایران خودرو برای قبول هدایت‌تیم‌پیکان به توافق رسیده و قرار شده فردا به…</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26647" target="_blank">📅 23:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26645">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e09976f50c.mp4?token=vyAOC6iAj7EcF-Q_sh-_nhuaRHrMQ5y-3VRuGVUpN11cw1PU79uemtlXexkHF8_dnFh-pFs6nQY3MRnfbCXtt_SrDmNgWvDnfQvjinQ9k-UO-6wUplQoM4j2AFqZnK2UeljC3Z05NS0MYsGFiojP8ngODwMD9TPjos3gfX4DlL8Ewrx7h33goAFlNDq1ii-cKEtaz_xuIz5xabAGBuXKgEK9NQvK8VJ6yIeVrdodetNryKgh5qk_ePaSFfewG5BC2msN1MtmzhtNFKvY8ZnlYLWuZNrjhF8pT_HmMC0-gwiw8Ckt3-7ajDW1tm8mdxgjLWkjDStu1yBEHOAkZTUqVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e09976f50c.mp4?token=vyAOC6iAj7EcF-Q_sh-_nhuaRHrMQ5y-3VRuGVUpN11cw1PU79uemtlXexkHF8_dnFh-pFs6nQY3MRnfbCXtt_SrDmNgWvDnfQvjinQ9k-UO-6wUplQoM4j2AFqZnK2UeljC3Z05NS0MYsGFiojP8ngODwMD9TPjos3gfX4DlL8Ewrx7h33goAFlNDq1ii-cKEtaz_xuIz5xabAGBuXKgEK9NQvK8VJ6yIeVrdodetNryKgh5qk_ePaSFfewG5BC2msN1MtmzhtNFKvY8ZnlYLWuZNrjhF8pT_HmMC0-gwiw8Ckt3-7ajDW1tm8mdxgjLWkjDStu1yBEHOAkZTUqVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟢
👤
طبق اخبار دریافتی رسانه پرشیانا؛ پس از کش‌وقوس های فراوان و مذاکرات با باشگاه های لیگ برتر؛ دقایقی قبل جواد نکونام با مدیران ایران خودرو برای عقد قرارداد یکساله با پیکان به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26645" target="_blank">📅 23:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26644">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OKnxgnd9YaZGSbgMskp3pR7FGqq3_5gbP3EJN4Kd1DmNB83uyexI4INEYahdjxyLCw5xKEvgNkuZpNRM0W74nzUAdDnAv4-w2ZzHL0MsiSm-U7Rq75DpNRT-A1NRRauXboF1u7P9V5DCQjkTm32skyWJ_ojaPaUGasIqAKhgW2PkLhQ5s5OhTxCTBbgXGds8LrGlwPww_B-1Wf37U5PKj5FgBz97OkrpHsUo7l91i-kU1wMy8Vo2hQf8OieXyDPOTeeknX4HZ7m0qUvi--SAZFFBw-Md10dbQYho3kB-udYIhbNdP2W5wg4jLP2HwB94-r19pGR8TwaqUw7d8-LOow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
فرداشش‌مردادحوالی ساعت 16:00 قرعه کشی فصل جدید رقابت‌های لیگ برتر خلیج فارس انجام خواهد شد. مراسم از شبکه ورزش پخش میشه.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26644" target="_blank">📅 23:28 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26643">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PLDhG3WxObIJ7wmBXLLbNLkbs2AWpbOML5iWkS0KFmvj5qfKDTC_EGivDYXFa-7nRMvMlDCDxcwBKfSt22qWg73-obDo38yEkxgFDXcZGWOil7h89wGlmz-e_MrO8d22CkqRmneZy71hMbINZia4IoW-oS_du-KOXQ3OpoSkQ8ddgDL-vYDggqVcJ5iIc0PifrH6IHZh3X_NZA5pFLlqpbHZnh6srbQ6Jso9SVye5Gx4cHLm8QNoRloMpmKTdpNXO-cIRl6WN3eEwzqdGWHqV9zzyZF55opSFMbfWW4rAHJVenxsW8P9mzDwLeDntgwFQDq7cdbV7RO-o9_f_nRCdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
یکی از مدیران باشگاه استقلال درباره آسانی:
🔵
با توجه به اینکه فسخ قرارداد آسانی در سازمان لیگ و فدراسیون‌فوتبال به‌ثبت نرسیده و باشگاه هم اسم آسانی را ازلیست‌تیم‌خارج نکرده‌ونیازی به ثبت دوباره (new registration) ندارد بالغو فسخش و توافق نهایی، طرفین به قرارداد…</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26643" target="_blank">📅 23:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26642">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/idwIvnXSpJkIcV9VVoqRNiBXprrpBCCTB1ZGkAnMd3mT7Jg28-BijC509Zojolo48_w4M73kio0r_9wqV8dScgIjvnWmp1lOKpfFxnjLlM-A05ce6l72tX3GlLHWkQkoE5q5j-8mWIbIfSxE0QRWybCmjW249vrZtWVhyCh5YK4zbqyw3E0jz5ZlGFmtHh8CTRSpHgY83Ja7a7EPhz3UbC5HBbsEhtHV5Xuv7PZHLiN-yLQA_lc8ihX-kWW31kU_VCw_qDeHb1DXFVgnF_cSAEW1SS3_E5KMD_iiOQp-WudzzQXS2hHrzgnyUfzcGLsUZXS3S3doRJ5ldim3koi-qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پرنسس لئونور شاهزاده اسپانیا امروز درحال شنا کردند که ناگهان با شش تا پسر شکار شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26642" target="_blank">📅 23:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26641">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KO5loJKzq1SRydLdwAaCuqHUpA0TpXZx7x9QQb51gXgD31gIjNoHkdMX8JvPXex9vAKpexpo5dvSkwexj1iG_FX2blm8W84mas-bFUbpPoXWkopKmdoivH9ZZDdID0cbJDXpIt5q8B-4dVTIHmfH0I2RfORq2LGaYg-bQ4x0ZGFpuD3GT__o6nOx46id8hZhBu1L6i3EhK1RfSHxDtf1YzVAvvG96WXP68YmSTxmnSJeC2jNrtXDb0ATj0ia-EKjqcs9XEgRiQX67_STge55pQbhVoFRT7HkiIBMqaYdCYYB3HHv7qjxgIslohRrXKrIzpZvnNlj1Gnp5Y7_NFLNPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇪🇸
خبرنگارشبکه‌باشگاه رئال‌مادرید: به احتمال فراوان فلورنتینو پرز بعد از جذب رودری برای جذب الساندرو باستونی مدافع اینترمیلان اقدام میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26641" target="_blank">📅 22:48 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26640">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBqWSW34HwO4Fs62q-u5c6WLrCBZgJVIyqIbXBNH7KI87gZxmynkdeEmxr4ja_PDmD-s1dlZF-u-75kGUpP0qzpt8MOAWcic7x7uOUv94kpjud6r4F3YzqV-xwDyyuor5P7YEluZsi-eBJ5Y3QCYV0OMKistPo_7YDoOVNASHuTfKVRTtmY7ava0BFXEQZEncRkWCUSaQGTY1rFVZz5qutJ3zkkpryavkf9JvMYCdyEFfvwJSKwgweoX_hGdFPAxbezAYnFzjKsbaKlFjC9d1H9UY9LFSHRaYK2Rz1mft_alRPRCGHTNZ9WWFh4LtzAkNcy1tDUeHJybHqxeTfRjaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#نقل‌وانتقالات|جیمز ترافورد دروازه‌بان 22 ساله انگلیسی برنلی باقراردادی‌بلندمدت به منچستر سیتی پیوست. احتمال جدایی ادرسون بالا گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26640" target="_blank">📅 22:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26639">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BWARjWBcxL8t-jP2pMzuUBlmxStrxof3D92Vh0rWlqv7TIc77U94Q258HUdRhIbA2-98829udZ4J6zX_DSwSlObZ7br7x63MxCSnsitJdAe1g1vjirqHdCq2fqf7NMytn4TvOjwN3XctLvgS96te24QUPb4X9Wpx0VdJupoRRpY0SPKOEMcaddKkkHXd8Hq1Mt-OBbJW9yYQt7lJFooNUvSXu_QP90Ax9_djkfJixGU0JK4Y5cu5QJipAytGlycHEN4oYhBsYkxbVZXn3CVfDwWbJEBHmH2mES5l-ZYwdOpkoe8w_mfT375CWdg3xukZjhnFFA5EoR74P3zQdmsOJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
🇮🇷
#تکمیلی #اختصاصی_پرشیانا؛ منصور عظیمی تا ساعات آینده راهی امارات خواهد شد تا رضایت نامه این بازیکن رو به الوحده پرداخت کنه. انتقال محمد قربانی به تراکتور نهایی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26639" target="_blank">📅 22:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26638">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJPjtIw4NcNlqUh_SV2PG0n44HRekp_lWVb-3JWnd1u2gE63NEjPuDqLHKSg3ghIget2r8XnW6Dq3CAvFVKafC0zUl_Oaa5ts4otPBxuK60ss8hltiJ2YKxCl7EOhn-Ta98Dd7Q44FiYKME4NehrttwkX4mDrpPX14PYSwm855Z5fAR2LjTG9rEQlWVChOy1R-d-2npZF9brY7qBOzH0-P6j0tRKMtHSj5PhD-pVRsekCA1nWDUOzFNmWeD0M4t5-j6En4rh2K7AX6YaE3nnmi6Mbo3wju6yJQSGYeF3vq4T5cWIUnehTJ0_0KuEwkTywWaI4fhb1ijK7cR4UuPYWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇪🇸
خبرنگارشبکه‌باشگاه رئال‌مادرید: به احتمال فراوان فلورنتینو پرز بعد از جذب رودری برای جذب الساندرو باستونی مدافع اینترمیلان اقدام میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26638" target="_blank">📅 21:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26637">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M8Wr-CvZN0fou0QTl4Fz7DAURlimouhYLrvMNCpDchWAf6elHBGSJFpJ1PGIcZ9B_6opgcWM-egmDHOuv9Q4RUXzujj4SE8siTCItyQQKUi2WNWasyy5ozCX5CKthvSNHSMl4MB73l_Rc86Pliz7YJF1wpMAak19j4UOfoRKL9MWaEYeiFGhaGnCggE7xyvPx_a8yRbEW9ofRmum_Y4J-40U71Ag1JidVK79_qVmiGNSjSi_AqY5x69jxwybuxagAKLsZBKI6MKLbPQ8mxFIBq6RNHjMqAfzS7dERYePu5chgYYCBJH8tCkUK4CAlMSYlL-qG5eTeeEKtvVqRLnvbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رسانه‌های عربستانی: باشگاه الهلال عربستان در جدید ترین اقدام خود با پیشنهاد سه ساله سالانه به ارزش 65 میلیون یورو به دنبال جذب لوئیز دیازه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26637" target="_blank">📅 21:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26636">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISZz-_9TmCxzv4RYPV6tpALAnKSY03u6J5MoQ1dS8ybNR4puWz8GzE3P_98AN7LyEp22n--futVaJhlku0THrYlUAjzdt8cW59bBl2KSRLwEhOcVzP_h1AP7bUFjOjh8SVv3HzXJqPMhD6JzFsGRoGwDazDv-P_zVSgy1iysM3b65HAVAdP4bTAMFBY34585WXSXvpKbupy2F8K_qsIfV_g73AXfnuhTD2vHexGx0tMDNoJ9PSE87wUUZbI2GQbyucqe0p30-KXk4NiSROfdO72vP_UBp21W2bXizrWx63WJhUEYD4T15F00VZPhUtSG9dKLo7OWRPMZrRBafm7Ppw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
فلورین‌پلتنبرگ: ژابی‌آلونسو برای تقویت خط حمله باشگاه چلسی خواستار جذب دنی ولبک مهاجم انگلیسی 35 ساله سابق باشگاه آرسنال شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26636" target="_blank">📅 21:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26635">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWPXYRdUwFLEC2zafy37UwQrZvsf3wkhoYAY6Wqc1ZS3u7fq42jxidHctKO7dCQo_0aEPyw26ypFZjX9q87hf_FLL3vkYbz7IZ__R90SxKQ-d7Bd4qttLAi__lEyM6gzivfyVmKLy3EbcbxyDumlypnQqnNaGLyf62UBwbGmIH9dNyW05ibjSoVWaKSswh65hgno8Sm9Yp4e2csxsSO6AM1XCKFlSf4ndAJ3ievNdXTCadblzOygPqp9W86IMhy2WcOlxQP2LdZo7Y0pvghV5TGR-_OCbfV--lqj8hoz5mNe3HbH6tJFKvnVV_jb7CKAusuDar2jfyturtzmj7BwJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آتزوری‌درحال‌شخصیت‌گرفتن؛بعدِانتخاب روبرتو مانچینی‌بعنوان‌سرمربی؛حالا پائولو مالدینی اسطوره میلانی‌ها بعنوان‌مدیرفنی تیم‌ملی‌ایتالیا انتخاب سد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26635" target="_blank">📅 20:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26634">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qkc4IXwJZnYKVGmOmQdjoUhT4kxkq1LrS8zXa8ah9ne1L5rcdphmM1WyfaFo9Ke2CN85Y5PPllzjZ4_8zOHKnWSakqU2VaYEweAEi6oNkXv8-KuS9oI_x2xnWuGWwbv6gmianrxRW6D4oaWQnpH-utdAg6u3DZ5_iLfjR9TalVDtUjK5QEsuXhjB3XB2PVINViTFUR4QZ-qBWF5_IGwGqUU4Rz0OcF3zPE_TXCd58Qhw6jSGEUBMAcy6KoNwCtWbjlCDnaCAUDySKyJ5rrrOJ2C42XTOPNMDXW5C-zcw7oFNDMU5yu4U7VwufItgU78919xJXVkZUAFGWzbm4FaT-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه اتلتیکو دالاس که درسطح 2 آمریکاس و سال 2024 تاسیس‌شدامروز به عنوان نخستین قرار داد تاریخ‌باشگاهشون با چیچاریتوی مهاجم ۳۸ ساله سابق منچستر یونایتد و رئال مادرید امضا کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26634" target="_blank">📅 20:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26633">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i6D85CUIfdsxqkZVOiq0qLP4PbcSOgG-AIGSQaeBvCm4qlJbvufq-zaolxZLBp7jzH3e2YXap8Foy86P0m-vqALW0cBZGk88-89ZogJSDQinAsipYorBnu60ymTkSvM_yShDlgjwYReKA01X5uXKstE1Ad1izqfGI8Wb67VQPCqqisYoTnAsH7OtevK0akR7qNjvGrGvOGwfH5RyjNvZvNlix_fMNCSybJBhkGMPezIR4GFArHuE8J574OqV-t7-pVhFmQ0jhuuEDCZgpMw8Fl1aWG6OjjbmCmgIhQKrr1l1hNBVllawLQBvMCZOvOmbBH7YYs9AC8MAu5BwQhtaaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میلاد کرمی دهن سرویس بلاگر محبوب ایلامی تواین‌وضعیت‌که‌میبینید داره شیر آلات تبلیغ میکنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26633" target="_blank">📅 20:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26632">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g8l24TSWE9YPHrpwnVKN2PzPqdzU8ft9_CnowbVSjYtdkaVoc64z67mVl6NKfondOL-NiX3R6lUQrzB-lGkGxPlJebho2Gk5EdAVknf2NW7ymoIAYc-FqRBIBIygtEirxPJwfOv1RV-5MZDW18L663a2cMkguqQZogBykBS5YGLbqnpkQ_y5einUvOPjRvXsI4ptLzlJgGlPKft4J_g_v4QGnCNtq3GrBoPdtDHHN96kj40K9SqIW3oiWLubhuRrZ3QXhfsBbWQQ7mNcLqMgiqfln0KfgJcVQjfpc95foeyJfr3g1HSzUTe-bx98SQtS-VEey3aru4aGeOKuZGx2VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ روزبه چشمی کاپیتان33ساله استقلال ظرف فردا یا نهایتا پس فردا با حضور در ساختمان باشگاه استقلال قراردادش رو تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26632" target="_blank">📅 19:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26631">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y98xVeJHA0cUwuc_e_msNJCr35Xgpb5rR2vjrxWWtllPa1uID3fSV9G8mHhSEPWXfjm6BMo1Nfb-gBziuhs7ms2ZaMFXoGb3UCA1o1EUs1mLoQ0krjJlEPq-QShwZLl_0M_WrNlq9hyX-dGljtK3NP9m3Iv_7EIG1qAz2TTDMuLnDxE7VM6bjHjJ1fF08S2gK_OK8TUliHvHofDNdtCkOeb3GQ8jwcRfNFZif-cAK6E52AIBJyROy2uLlY_9od0dbrzpMn9YLpYeJ5VAeX5lyGHhy6W2Lce1e4X3U5jth2cRjraIgYtFsCVxUiwujmLRHCS5RQ2105fU_S71XGrmXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
فلورین‌پلتنبرگ:
ژابی‌آلونسو برای تقویت خط حمله باشگاه چلسی خواستار جذب دنی ولبک مهاجم انگلیسی 35 ساله سابق باشگاه آرسنال شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26631" target="_blank">📅 19:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26630">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ttg5Bs_fo1-k9h484UmfluiXU_Z_WVHyXGcxHGmNoDp8yWbHRRB04WllhIFAIrm_fLASykoD6ESt2nW65hF4V8P9oFtPML603cO-Iax60GbreJL0baVYuyGs9gXMUqr2yJlqGIVkwLmruFzWCquosxHPlQQ4HTyrTAyeSJHZrp3G7lPw2hkLhRzGYY1GaolzQMoWUzyejRdq7psKuC0PklqzLO2-A4mySQHND_H1AyJrj0MAW-vqZUwPMxvyDAm1eo-j4Jxv2LbJrj-u5V41MQjNCYpvmNLCCHKoYwgMbJIa1ICXZNR0PgJWmN55NY7RlyGWYkL5t-nOBxE0S215fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه چوروم اسپور برای جذب مامه تیام 150 هزار دلار به به باشگاه‌ایوپ‌اسپور پرداخت کرده بود و 750 هزاردلارهم به تیام برای 1.5 فصل؛ روی هم جذب این ستاره زیر یک میلیون دلار هزینه داشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26630" target="_blank">📅 19:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26629">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T8Kf60nHEjlN6RB36ldGChVLkMVuC86CugQUtzGNO6gRV4e0yKNE0ulbXEt3g1zrrUMxs0OMUn2VLUBaQn8Uq-hkiCUbUY9LT5Y-WbuAiO6IlxQfumL7NpSkjnsATw-gxY3IS54t_fQB2HgIx7fR2z1L5sQPcgDV_Ld_zHz7yLidUQVYgmKeVN8_JWa3fyznjaO4AJ1HqZH2dOlmJEaZrBMHOBiZYoSobbJXko4F2pI0MBVEcePtZHEzmYNlTQF-CIp06TdLrbvhq7mX5G6h4zgRGqc5mqzAwwBSzbpFAIbvmZhTycUAalVJu0c9VwRpNcB7PXGTG53aGuhjKyd-Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
فرصت 24 ساعته نساجی به پرسپولیس! اگرپول ندهید دو بازیکن راهی استقلال میشوند!
‼️
علی تاجرنیا رئیس هیات مدیره باشگاه استقلال امروز ساعت 11:00 باشهاب زندی مدیرعامل باشگاه نساجی تماس میگیره و به او اعلام میکنه که حاضره رقم رضایت نامه کسری طاهری و دانیال ایری…</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26629" target="_blank">📅 18:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26628">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e2-PBXigATv996h7Avm1bcmRlPO9JYyq2VuGzkdze9Jw8zoBqNoKognbHaSKXNC-SK6QKSkO2eMa5_8Epy1m8ZQNp5XhzlOtsm88C6OHcSZ--w0aurf8fXjzqCw7G5dSDlA2POiHBebZ1B6A5qRHI8H6HdoXATUC1aHrNa77L0QpxvybCycpYIstUPcq8Z1T14sC8q4y4lx7IWnTcOn_ApIyPcqJloy2T7s31OIqSmt7Wap1ZISaKQw5SzNouyA6q8qHkx6p2ZIrHefMHu-ETRPkQ2KdmD1qAKDPMVw0OIDHjclheWa7yPoRgZINHYwTO6UljKDks3lsxDsz1wfnXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#فوری؛ نشریه مارکا: الساندرو باستونی مدافع میانی اینتر میلان درآستانه عقدقراردادی چهار ساله با رئال مادرید قرار گرفته. توافقات شخصی صورت گرفته و باپرداخت50الی60 میلیون یورو بند فسخ باستونی 27 ساله توسط افعی‌ها فعال خواهد شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26628" target="_blank">📅 18:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26627">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b902abcc5.mp4?token=u2rOT0wQzcF6BBc8TmpLNgq6G8DEm_9P0yrfNCv0F74xjwcQbU7h9pl2St0C6lomSZ78l9seBlwxU0_8bdcYOY-3Zwh_WGXVk0yeojMcvvda6qm-EV4hEUEWcUDnL6xGLEI71Z2yu1pjmD5bdyIWV0WQAq42X0Qoq0kR4ZTiL3W6iLD7-MMgOK4YRCyQ_xyeyZITz2nQre74M0lQHtKtIQMQajMrEYLwOWqq_qL5uIjUE6uyKsr8kQc0wFIrpeVRWr1xxssAWBFxOuJHyr5HNluOUQU4FDK_b9FM56VzTVZs9okj3cVhjI3iGDZ6q76mXSu8Yivyu55gIYX99H9vJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b902abcc5.mp4?token=u2rOT0wQzcF6BBc8TmpLNgq6G8DEm_9P0yrfNCv0F74xjwcQbU7h9pl2St0C6lomSZ78l9seBlwxU0_8bdcYOY-3Zwh_WGXVk0yeojMcvvda6qm-EV4hEUEWcUDnL6xGLEI71Z2yu1pjmD5bdyIWV0WQAq42X0Qoq0kR4ZTiL3W6iLD7-MMgOK4YRCyQ_xyeyZITz2nQre74M0lQHtKtIQMQajMrEYLwOWqq_qL5uIjUE6uyKsr8kQc0wFIrpeVRWr1xxssAWBFxOuJHyr5HNluOUQU4FDK_b9FM56VzTVZs9okj3cVhjI3iGDZ6q76mXSu8Yivyu55gIYX99H9vJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
8 سیو دیدنی وزینیا گلر کیپ ورد در بازی مقابل آرژانتین؛ پبجش از 18 میلیون به 20 میلیون رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26627" target="_blank">📅 18:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26626">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3df251c94b.mp4?token=H1ITdHZWIiflmnAB_ZhWx_CmZOEW0zHrWFpy4frnV8BjlcxVvt_LdSsJnvhQjJ3apVjlrX_VHTsZKugOmE88IXQoJsk1Q6biMEjaa-6IQT6lUch-kvx3LUCP9SuNc6bWAmD8HI1i9UFb66XfhaK8Zg85HapK-BkHVhrLZy4_ydAPeDhIORv1skrj94-nbEFErRtKGOtvwNBG6DKmBmEvEBtzaS2y-Z2QcHLKhK6mGAhlpWS_4pQZChtELA9QqA9DrzZ_aLrR_2L9cldbx6kZd3irqdhqYifspCoAt94yDC8LyWVScCHXR8E8cwXclFEgAbJKMI3S7wQnXNxvCmRm6SwvP8O6M-tufr27HytMsFumIzLTbd-0vtnmB6sxAWtP0eKHA4QGCt-AR7i4ERqMPRsrvTRGMbE0lxzzubp95nw3Vhav1l-h-7Baqwt-Cn3eauS_IhJph6sR7p681_ZzXwJs0Kkp2KY6joPtDy7JTK6ritjZwl6YLFdMT-r1rJ5upg8X9M0zGJ2EhbQLitvxZ91GZII1iuRMz4FTSlea9cyHkKVfX26miwdMV9Ap2eLQkKru81r8rWBeHMRb3KvZRAc--wAxAeHrNZR2-1oxGelikRAIV31kkLE5YyE8Pzo2BM0ISolqTAVa0RlFCrUHV5XEbcDl3Q_kC8l_hEjs4SY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3df251c94b.mp4?token=H1ITdHZWIiflmnAB_ZhWx_CmZOEW0zHrWFpy4frnV8BjlcxVvt_LdSsJnvhQjJ3apVjlrX_VHTsZKugOmE88IXQoJsk1Q6biMEjaa-6IQT6lUch-kvx3LUCP9SuNc6bWAmD8HI1i9UFb66XfhaK8Zg85HapK-BkHVhrLZy4_ydAPeDhIORv1skrj94-nbEFErRtKGOtvwNBG6DKmBmEvEBtzaS2y-Z2QcHLKhK6mGAhlpWS_4pQZChtELA9QqA9DrzZ_aLrR_2L9cldbx6kZd3irqdhqYifspCoAt94yDC8LyWVScCHXR8E8cwXclFEgAbJKMI3S7wQnXNxvCmRm6SwvP8O6M-tufr27HytMsFumIzLTbd-0vtnmB6sxAWtP0eKHA4QGCt-AR7i4ERqMPRsrvTRGMbE0lxzzubp95nw3Vhav1l-h-7Baqwt-Cn3eauS_IhJph6sR7p681_ZzXwJs0Kkp2KY6joPtDy7JTK6ritjZwl6YLFdMT-r1rJ5upg8X9M0zGJ2EhbQLitvxZ91GZII1iuRMz4FTSlea9cyHkKVfX26miwdMV9Ap2eLQkKru81r8rWBeHMRb3KvZRAc--wAxAeHrNZR2-1oxGelikRAIV31kkLE5YyE8Pzo2BM0ISolqTAVa0RlFCrUHV5XEbcDl3Q_kC8l_hEjs4SY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
تیم ملی والیبال زنان ترکیه با برتری سه بر یک مقابل تیم ملی برزیل قهرمان لیگ ملت های والیبال زنان شدند. زهراگونیش‌بهترین‌بازیکن تورنمنت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26626" target="_blank">📅 18:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26624">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WEG2Qb2jgzPibeHNQvJAgSQ2MW49-c6UEqv9icd5mzS8IyZDmZXLE0EVzng3Um0w7Z48fyaeeNIi0nLmH9GLiqODRqsJKRfa5l0nFDJA6mgRJ7ayD6viilsNN1QF7sZ7DYu4FbqzJlfJFiiiBgUvB5mNOggtParSZU0xX9L1ABBWJY28p_1uoHudyFfeO1OvaeOFMK6qz9T4Ulz3zd47c81N3Ammlhcq0RKQEqs6y8yRIJQfDItGnwMJDMHT3fJtxxp1gwMBEZJj_O3o7laTlBgs6BPJ5Kzgl8MWH52S98Jt_Uji577PrT7anjV_wVE75eoeZWCflQ5qTa89jXm-EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#مهم؛ اینکه‌بعضی‌کانال‌ها میگن زندی مدیر عامل باشگاه نساجی‌پول‌پاشی کرده که با قیمت بالا تری دانیال‌ایری‌وکسری‌طاهری‌رو به پرسپولیس بده واقعاصحت‌نداره. زندی‌بارها تو جلسات با مدیرعامل پرسپولیس حاضر شد و گفت حتی حاضره با همون رقمی‌که طاهری رو از روس‌ها گرفت…</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26624" target="_blank">📅 18:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26623">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VSdTsP37JfxIMGxwRrBR_xleMxkWkZ9DjBj7xttPFk8iCTO5lMSwEkEVawv3y1mKHOvEVgvr8tN_eeDsG7j1nR78pgFVBGU3nD-_GZbe0_c673Ly6MolGw-axucbHQNk4cT-i9A1d6eTiNElC2pb_cCVhngi0VdCAaLP4mzY6oup_lMGrpNZEFOcN-_Krsog9aWyKZoq6OMCu48m8p3xRRSxrIalPD50HZlFVbmCHfLGYjaJ95hv2M5sk3T-LSnqawVB88yf27HxQm6I0NkjPBsDzhjzPzq4RMnzws9b5Pm6iLqMI8nc8ScoFcrTaBPgF1ufj5g_YHtUafwdM4BkYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇪🇸
🇧🇷
خوزه فلیکس دیاز: باشگاه رئال مادرید برای فروش وینیسیوس جونیور ستاره برزیلی خود رقمی بین 160 الی 200 میلیون یورو میخواهد.
‼️
آرسنال آمادس تاحقوق‌هفتگی بیش از 450 هزار پوند به وینی بده که در تاریخ این تیم بی‌سابقه‌ست!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26623" target="_blank">📅 17:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26622">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fNsrgxFvHRcYn4o7uNjUk-6IiJGhcs_MDlIFlV5qT8opk7_1cQm3NS2Jjo8Vlz6ZQ3qm5oKcNL4SyH8qaCxj6bSKoYxJbhXuTvi0tKtkNdUYhkflkcrGKFHzTbsfjHooyf_dCtv2PNvP16Z42weiQpdzCGcW8GLZzMmkCO7X2F_dJvUwjNzJrYgodd5bfEJZqEE9R0w_x4fO_UT8kn4y03x7Rkb2p5RID3iW5QP-5EXafOGTZZncXYGsUPVWgU0YPi4uGt7MvMkhmC36whPRvCFJw8axa6DhfbM8_LOEqBSzHHU6Xoo9QIxwkBPOad-jG3yIk7TFagziComvcyWoHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام فابریزیو رومانو و علی رغم شدید مایکل اولیسه به پیوستن به‌رئال‌مادرید؛ این ستاره فرانسوی این فصل هم دربایرن‌مونیخ موندنی شد اما تابستون سال بعد به احتمال زیاد این انتقال انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26622" target="_blank">📅 17:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26621">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iedkmNoCv4B4ns15tmp7Yn1DqjZ7jbg0QT5r47RGplRgxnDnNeUfE-BJeq-k3NVag7d_ue8w-o7jkw9tDgfb9p5wcaapKk1ZkKdE8UWS9zIF33Yo_SkQ8_CWp8KiddpBKhPwMEiPT9cPXn1UuI95PLB0ltGAEfslZiwxdSyzikw8uMh7DBsR6iz532oc3GZmorbt8uMuvRzgHbSNNXNADuosJXXJZ-XUQxVI0rPqNSfd9_m9nS288jdzy0bXxV0-M3t0vBztzzccIIVtEoBKrgLP0r89olxvYC8zJutMwFio9Hks2pMmAHR4o8n5G9DUVBjdioiX6Upg20rI891qkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
🇵🇹
فرناندو سانتوس‌سرمربی‌سابق تیم ملی پرتغال:
حقیقتا من هنوز از این‌که رونالدو رو در جام جهانی 2022نیمکت‌نشین‌کردم پشیمونم. ازاون زمان تاالان‌باکریس صحبت نکردم و رابطه‌خوبی نداشتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26621" target="_blank">📅 17:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26619">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1a0b40618.mp4?token=Bswi2yF0_aLYqVs_OS1lffiV3BsINGOI8bOpxYpJ_Pp3ucHf06QT1HqbMQ1TT6RYMiG03r7_P5VpLP4vZzvbOSCotKo_RqNhzkg6Zfp1v1S8pOXIAUu1fvbWt1QK_-9EG32LVNhRQKOpl0CgmOaLl35qcOpQZDRLeNCK5pGbQNi-gYaVhVsBevTQC39OvNipZCmWs4Z21bhoRvfkvQgeNLd1cs8bOhohIy9bgxBJFd9l2LChAd4sDq8VOn3HiI3TlsyfsBnwRObkO8-RqLUIJ8FUecPJxjNstTnbDxJQogd9KYH6OUk57UOSaQJblcgv9FVBXXboyFuDK7KGc-Mvhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1a0b40618.mp4?token=Bswi2yF0_aLYqVs_OS1lffiV3BsINGOI8bOpxYpJ_Pp3ucHf06QT1HqbMQ1TT6RYMiG03r7_P5VpLP4vZzvbOSCotKo_RqNhzkg6Zfp1v1S8pOXIAUu1fvbWt1QK_-9EG32LVNhRQKOpl0CgmOaLl35qcOpQZDRLeNCK5pGbQNi-gYaVhVsBevTQC39OvNipZCmWs4Z21bhoRvfkvQgeNLd1cs8bOhohIy9bgxBJFd9l2LChAd4sDq8VOn3HiI3TlsyfsBnwRObkO8-RqLUIJ8FUecPJxjNstTnbDxJQogd9KYH6OUk57UOSaQJblcgv9FVBXXboyFuDK7KGc-Mvhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
تاتیانا دوس‌ دختر هکتور فورت ستاره جوان بارسلونا و حامی تیم ملی اسپانیا در جام‌ جهانی 2026؛ گفته چه آرژانتین چه انگلیس بیان فینال قطعا اسپانیایی‌ها توان‌شکست دادنش رو دارند.
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26619" target="_blank">📅 16:54 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26618">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KtnsUOUbGxqlhmP2vCzjq8tMevWzL_qlVVRWHroRxLs4yhZr9c-78jEyUy-SI9SQwfof6-H9DOz6KZZfq6XJAKvpOSatUI58Ey8YgU51wKD7UXJUQ6jsLkdbg2F_bpVrcUbXqMN-oMjFCGucaOv_CMNZ3PGkcjMKyl7rqhlD_2sCC1CDSLVi5NzhKtOKeCr6Ch35S4uA3O3GFEAiyYNNQm23VVyk29D2-YIa_uo5H0SGAW3xVpGX4N7oJ8FpKrywETbAtKaKYWvy6Gv5YhuapZSZWRzsk5lrf0OUt0qU1TQxuJaBNucdOafYAOmbilemrMTduaOx7--qg7y3W4iTSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی‌پرشیانا #فوری؛ محمد قربانی ستاره الوحده‌امارات‌امروزظهرجلسه‌ای یک ساعته با منصور عظیمی مشاورمحمدرضازنوزی و مسئول نقل و انتقالات تراکتور درهتل‌المپیک تهران داشته و برای عقدقرار داد به مدت سه‌فصل با تیم‌تراکتور به توافق کامل رسید. عظیمی به قربانی…</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26618" target="_blank">📅 16:38 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26617">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mlGQ32oOj2yGYkXWdcEXdAjYECwJW7pxugG9abJPpx0D3jesIf9osT6XVuY2lw9_vOL7NW5aApELpW-wKOQDYEkbZtzB2nunRTWh33XbOPP5rhaBlywqj7SmLj-76QGAJxvTVA2KRFyFZLMm8Va4C2iDbH3ySmU3u0WM4MVeHZ0rUUzoWHqt40XrnZyALON_2ecft3bAq_9Zf7YDHIhrnqQGCLCMTuFqp7g6kbA3Bk4thvlORM4eD6rDRAXghM9LjJj0k3fTyI4oeNLn93mFUd1RSv8KsTo8djLikcTT0ZAouvdW0XbkHAVHm9QL1_4OUWgns_Ggidd0gIUuu1ZC3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی‌پرشیانا #فوری؛ محمد قربانی ستاره الوحده‌امارات‌امروزظهرجلسه‌ای یک ساعته با منصور عظیمی مشاورمحمدرضازنوزی و مسئول نقل و انتقالات تراکتور درهتل‌المپیک تهران داشته و برای عقدقرار داد به مدت سه‌فصل با تیم‌تراکتور به توافق کامل رسید. عظیمی به قربانی…</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26617" target="_blank">📅 16:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26616">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Id94iwpMiKfP2Xpq4d5REHuK96kqHqV193s5WBeV0CgsIGNDfN3txo9D_-1TXgNFMdRPUiifUxUKNOpyjVSuF0HGgXRXmnnj4qzCzA4qAqPUvu6pCTufNvc8evqEwQIXgd8yD_A4qsqXP0dH8JSuE9_C39rq6KbELExgw2ZNJojIY_TNpgsd6RYqQd91uWvEz3Q3xokLFfPAEmTXs4-peONfIt2Q0-2Mcf9I4IIno5BbtIHSGX9QgXI6YqhyH52kTTkMPWinNs-ywLYiqPq3i2xIunkGcgOLNEFDnJnKZ1hjiJQnywBj1j_0HIRHE2bsan5hMLFKSeg00ajftIS89g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه پاختاکور ساعاتی‌قبل با مدیریت تراکتور برای جذب خامروبکوف‌به‌ارزش 800 هزار دلار به توافق رسید.
‼️
درحالیکه مدیریت تیم تراکتور با پرداخت رقم 2 میلیون دلار برای رضایت نامه محمد قربانی مخالفت کرده‌بودحالا بافروش خامروبکوف…</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26616" target="_blank">📅 16:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26615">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RAQiQIF8iPCd_B8eaRhAjdyxeHTFTNfCPnLEHTKtAqy1mqXZULmvFBOUFSdD3F1I3Q368F6PvanB5IIZPDWUE0NORZ5Eo-7PgqJhaAmRcqao6eig5GQm9-yLJI-OAgcXYcJM-L1XP5JebjsrPtj-kOqssEZsu3iBv3fHxGuJxOvh2iPoTAAUsrR0x7Nqr4bOVsL_TEffPhydPzPwvoKQ6S-2nBM9Z98tjz2JGL6AQWxAvbweKG5RVshn2azTVpxQ9fdIB-GPbEoKbkvhf6zfRC757BvO76xXeNIoO2Ao71zeaggPDq7HYdLkKeisO-5csuAljU_NEXKYyPlVy0rMmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
طبق اخبار دریافتی رسانه پرشیانا
؛ باشگاه پاختاکور ساعاتی‌قبل با مدیریت تراکتور برای جذب خامروبکوف‌به‌ارزش 800 هزار دلار به توافق رسید.
‼️
درحالیکه مدیریت تیم تراکتور با پرداخت رقم 2 میلیون دلار برای رضایت نامه محمد قربانی مخالفت کرده‌بودحالا بافروش خامروبکوف بزودی برای جذب ستاره 23 ساله باشگاه الوحده اقدام خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26615" target="_blank">📅 16:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26614">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tg7vRXNq8RalxlBb1TSxT6GEjaZ55ZrVh7_0gYYwdDL0vasWZNjrmQdB2oHUIoEbXr9MTDUch-qW3GVMnM2RSZI8w93TXC-K_0D08UXKSxFh7SR3bMfgxipu87vll-GLg-bj-3qjvFHJYRmTvwZIpytDWNcYS6zm0rlGkkYwAenlT3sBh3oorLKryzscYvddFrXStJb2xHyHKBCIm7Vez1RJvRGfsLE9aTdfGSJK-wl5Y98Bees3-Yi9wR978R7kPYGdvFYkDSmh1WzxdtZRs4a70_M0Uaq-pV8S9pn0u1rXLby3OHa97shBrAAWp8JGtAVsC78-DBbNpPOF2eeVlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
فرصت 24 ساعته نساجی به پرسپولیس! اگرپول ندهید دو بازیکن راهی استقلال میشوند!
‼️
علی تاجرنیا رئیس هیات مدیره باشگاه استقلال امروز ساعت 11:00 باشهاب زندی مدیرعامل باشگاه نساجی تماس میگیره و به او اعلام میکنه که حاضره رقم رضایت نامه کسری طاهری و دانیال ایری…</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26614" target="_blank">📅 16:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26613">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BACd8jrzW_FVIC1U8f3v-c0-osmrYT5hynkn1SeZNHrTQtK4EbFPYVCS9Kl6ZSL63EJhAbdB962uwOLPcjOgSUW7HTQcUF7TPZsIVvKXPG9n9BUqpamp6cGB9Yz4RwgZon8k1oZxBl8o5Mwm_z3mzPIaziLPgDGPw1KgLA1S1ucAjIUp22jOWgpqHpmizbK00vnFU0yitacDeQT7aFil4oLmOcm8epbj5tesWvAs__9QXLaBb0pVLs7-X3InmB_vhMv8qc5yea-h1qPMdu2q0nEGkYntZAr1W68YaqW-U_ShvYnGcpjj-5oLZxHnIqbPhJn7Gw0Ks11BeYk-i4lQdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
👤
طبق اخبار دریافتی رسانه پرشیانا
؛ پس از کش‌وقوس های فراوان و مذاکرات با باشگاه های لیگ برتر؛ دقایقی قبل جواد نکونام با مدیران ایران خودرو برای عقد قرارداد یکساله با پیکان به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26613" target="_blank">📅 15:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26612">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/amtGZ_1gevUigt6MfXPOK7D4OVKrGAT4j_ulnbva4pTlq1orKXfxdkCSvYiF_McJ-lbWjyL4lZ76gnpol1AA6T_8b6d7unLa5q1PwSm1w_vL32aCJfmGFdpA5a8QB0SMQtnTFpVHg7rvq28afPe7lJCtsjJbIxvs6_wMnsN_7IUTHCqJ4bhGotRXWFmGv8VPYj1JT4eza51v4vESYH-A6A8mjHAS_K6Dzpekj52GzQ5ixuVTuE1p-fnz1sWN3u1qEU0X4n30e--S5zIbFhJB5hyUFfTQ6BJBn5r1EaHTTzWUVg8USDjkNKStH9JnL84H0lleJOtngk9FjnHHjfD1Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
یان دیومانده ستاره جدید رئال مادرید بعد از پیوستن به این تیم این تصاویر رو منتشر کرد تا نشون بده از بچگی فن رئال و رونالدو بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26612" target="_blank">📅 15:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26611">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4HON00uxDq2ATLejb4GBV4ZOI3qRi0CX7cCSKZMir8XF8EyQ4qCnI64mrj6hSn7YEJarcgO8mUctrNuUotO8mQI0WmFxKm0npXVfBERBQWyfWhI8F8RP_4R0o9JjFrvCqrWWX53Oj-qy2qS23ccwuUiMI3IJ-PU3Y35F-M3p6u0SGCJKzTh6oHxjZP8ISY5VMMw8XVXHMWHeWlABG7gPudHTeft3JLCOxTHBNLgleq6xsko7ytmPx5_0lo586kAXW7K2VWMCTmWe1uDbNLExFL7gmJa2jwa8NgxB8kewYlGx0BXtqXuyaOpxpCQrBXef-zqMlfnLwQqfI-QZIy2Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی 14 روز پیش پرشیانا؛ با اعلام‌باشگاه‌پرسپولیس قرارداد محمد امین کاظمیان توافقی‌ فسخ‌شد. امین کاظمیان پارسال در شرایطی به پرسپولیس اومد که لقب فوق ستاره به او دادند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26611" target="_blank">📅 14:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26610">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZYDIJcWwGPLlpZDDfoL_mynnU_BX_idSqXY54FSiiE2ONZsjGifQKM7AcbkmsOoIHm48Ex-T1RpWOZlufbNFMdMthxz-XrlvqRp6ridHFDd0lAp8vsXCwr9CBNdYMhDNEjkx8RFZN5H8DDhYZ9bAdiZKHgC9Jv6AbXxXlSyn5gX9_OzWY5pfCzIn5nA9KxTtAeC2YeT3l8VGiPjHebBXW5WOuDvpq92MmwZ_VUQG2RmiMd-Yed-EmiU2gUHZc5UeGx_WlxT9rfBIyNrgfGHKyH-mzPw_IITxYCefef8V4D23JT6LgUEp5HujpjRmN5Iz2fjeEyhM4UBnaKqAUMA3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
فرصت 24 ساعته نساجی به پرسپولیس! اگرپول ندهید دو بازیکن راهی استقلال میشوند!
‼️
علی تاجرنیا رئیس هیات مدیره باشگاه استقلال امروز ساعت 11:00 باشهاب زندی مدیرعامل باشگاه نساجی تماس میگیره و به او اعلام میکنه که حاضره رقم رضایت نامه کسری طاهری و دانیال ایری…</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26610" target="_blank">📅 14:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26609">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b74811f44.mp4?token=ezGz9v-kmx6EdbXrWpd2Mu7UDP9GXxfnxM-XOyUSWsJysLLMN-peUMjdDiGPoyrZln2ZkGvCWIWCl4fnQ3MlGCfc0lyJcTf3hH5_4JwCIzG7Fv914WE_3FGEFNCg_UTrw_cIm0FGhOr0Tb8bI_YteJU_uk_VUana-bvFQQvBxLSmg2y2xUdjw-vwm6DbQ63sLA5uRFPuJMQ_Aopsb8ynvLFpodtubZIu6O0Z0oRGbCx8uf4h5e5PgCiVfcgNcH-NuILoitQsohd1Z2oiSnxuKJE52sGYQy14SNAdAQ2rkCn51d3dxZ_Swg3AWjSFLeT3lJpQvAXa6E7qhadZPHg6aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b74811f44.mp4?token=ezGz9v-kmx6EdbXrWpd2Mu7UDP9GXxfnxM-XOyUSWsJysLLMN-peUMjdDiGPoyrZln2ZkGvCWIWCl4fnQ3MlGCfc0lyJcTf3hH5_4JwCIzG7Fv914WE_3FGEFNCg_UTrw_cIm0FGhOr0Tb8bI_YteJU_uk_VUana-bvFQQvBxLSmg2y2xUdjw-vwm6DbQ63sLA5uRFPuJMQ_Aopsb8ynvLFpodtubZIu6O0Z0oRGbCx8uf4h5e5PgCiVfcgNcH-NuILoitQsohd1Z2oiSnxuKJE52sGYQy14SNAdAQ2rkCn51d3dxZ_Swg3AWjSFLeT3lJpQvAXa6E7qhadZPHg6aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
پوستر باشگاه آث میلان برای روبن آموریم سر مربی جدید روسونری؛ قرارداد سه ساله امضا شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/26609" target="_blank">📅 14:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26608">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ulwrXQSJmXfPOZxEEQZdWKaMeM4il3xcYSkcINaracsw8w64yY9hT17HXOzdJ2dEvHVHSLPt6qz1yffkBEalTpf2M_QzhOh0MV0EBVSJMOWNKDM3T_k_stMuP4vyx-zgiLC6t2K5XpOVpb2ULCN6KfDdhVY9uLiQ52OUpELSF0fkne6tc3lA86yR5sr-wjO2mjt2ubGYe7sDPyVxEpkq8-TF2Tt2I45q6KVNGBS1qDSSkl6df7a6y-zgFsQ7FOJDZdHRv8vUs9YZZNoYgI6BrDFoSvO3eU-6UfOxz23UwzoMlMwcfOHY4pTjKIL5hND4vLvrLnB51DoIYmE02LbOMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#اختصاصی‌پرشیانا #فوری؛ باشگاه نساجی دقایقی قبل رسما بر سررقم رضایت نامه دانیال ایری با باشگاه پرسپولیس به توافق نهایی رسید و به‌زودی رضایت‌نامه این‌بازیکن رو صادر خواهد کرد و باشگاه پرسپولیس پوستر ایری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/persiana_Soccer/26608" target="_blank">📅 14:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26607">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZ3UD0g9snRKnictXTyfMvtsJk3NShJt3v1N9lMBk6uqUFWhv7kS0loeMu5ntdAHuez0sXWnpXJSnYoyBquuzRDfhRt-9dt6uuJJ9h2xIfhvvsjfBkw5xPWxn9T4d4O7FGoQB_MHqCLigYZYAJaTjJxwAU8dNIYr8jEa_3NkvhNqBlneVe829Mf7S9L4eq6waceUY-nPSOq3oH5RZlEgSoLmOlODPcnXohkV16EFxqluFhzh1ILMpJQika2sx1M1uELMlJyCo3sHrwOBPbgWK4fkzXZMdNGIC5zddZKCAIbxbbHak8PTpaNud1ava2wA8Ir3KG7uoAu_eR7ECNg7Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جایگاه لیگ‌ های آسیایی از نگاه Opta Power Rankings؛لیگ‌برتر جام خلیج فارس ایران در رتبه پنجم قاره آسیا و 61 ام جهان قرار گرفت.
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/26607" target="_blank">📅 14:08 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26606">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i_36yjRkfGkPchI9I8zmgcC7qKbt8YD2vxGTxTieriemnU-59SdzRy-4_oXZ4y5Ly5Uh_f1xalmUzm2ZFvKRXXlkzB8m2kqfnz9Q7uvKHJUq6g-7hEcNQEb0icNJJODx0uSOjUgnb02n3QqhZObYRGgnKNa1E5rFplJAMPSVvMMtFtwdm6G1bkVuTHVTlr8fLbkWXSRngoKhl-MN3fbdc7AFwg8r6M_zDaL1w3OyyOZ_482MRnACev44-q8vLXhfYaIgQEd2muXlOF3mnkZRhRyZFWQP_SjSJcRBPQvF0WYKixBbzZqMmwZvW77mgjwB1ZmUOWLYi_rp1IqTBeOiEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق‌شنیده‌های‌پرشیانا؛ باشگاه نساجی مازندران با هومن ربیع زاده مدافع‌میانی 27 ساله‌تیم شمس‌آذر به توافق رسیده و این بازیکن‌جانشین دانیال ایری در این‌تیم خواهد شد. جالبه‌بدونید که ربیع زاده با اینکه مدافع آخره پارسال در لیگ برتر شش گل زده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26606" target="_blank">📅 13:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26605">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sHvjtl4EB4RsJtl7X8mgSGuk7M6eOjqrlua5qjBY7rv5sWtQOfJ84CjH0-mRV3P_XdL28ROVciVF3mQFi1C5tzPJLb8bU_5V5CS3CwTqed9v9r9fSPAWrOQNJgGRpfFTJqrla09j9Jos60F_DFMNjO-FTduTZKt3gEw6ifHiLD0C-1bwF3VepnnxQUHzcCRqMg5IRLtqaaD2ZYkXUnl_GwvINDop5-DbtCMvA8stNwzstssiVs059Pjub54PSEHnFYLwxhGq6DBDZ832-JEKvd8hlLtKe-Xi8TJN8RSqTup9_LNPLUfVpDEWqiBQJlxb1ovbViuvFJ-rS1zCHodE0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🟠
فوتبال ایران فوق العاده‌ست
؛ داوود نوشی صوفیانی پری روز رفت باشگاه مس شهر بانک پیش پرداختی گرفت و رونمایی شد. دیشب پول رو پس داد و امروز با ذوب آهن اصفهان تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26605" target="_blank">📅 13:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26604">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XzPOIweLlKKPtWeD_wq1V4el2-xsVH865C0zmf9EBGdgF6W4BqPBcoepzInxuga7h3SXqSXjRz6YtTuDzvxBgEQGhKGsAlxWAHcInrQjztf171bSw9HMS9Ut-Wa5NC43YKcc64ulsxgeHG4c64GNU3l_bdXq5c9ZO6Td8nZbRf2fyqYF6hqpEUxacQerC9938d3hXgosrA61_ZlAk05-lZuspPfeg_Xe2_KRGLn-bllJxEMNX8wVzbNqm2yH_op-0QEiz3Ey4kpdTdDmPcp_71zYIZjIUltaZsDHa_t5C_JsQGav1iOfTs9cMsFftOqb-V8v2IzofQZfFuSxTG02Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق‌گفته وکیل‌ایتالیایی‌باشگاه استقلال؛ ظرف امروز و فردا دادگاه‌عالی‌ورزش CAS رای نهایی خود رادرباره پنجره‌آبی‌پوشان‌خواهدداد. یا پنجره رو بازی میکنه یا بسته میمونه تا نقل‌وانتقالات زمستون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26604" target="_blank">📅 13:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26603">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0cb160c99.mp4?token=B5iTQI9VQZR2UupV2OTcoZ2C24iZ955gtXZx00V_10ED5aeAC3YxmCMhkR62Uo7nEwIJVcZEZrZsWPO2ljkgpip28ANhVyBwrsDCXKVPGQw5bu2WqsNPOD0XD_0IoW4uXMgtfDjzHhANdsoEQK6pJXNdqBG_REd7G42CHxe1oR_7FTkH34ySV0BqCM3Wq8xrUPiwjmFPsVZxpOlS27KZQUwXe_5t3sYFBd68FVFxNS6QbOYNjZ1ZEI9FUvl6555VJC8XTawo17nhfOzwALXbtf9t8aZvsYAzshk_vhLbiipElMKabzSPDcOjsdY30L_Ohd_KHMGSVM7_udzzMAo9qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0cb160c99.mp4?token=B5iTQI9VQZR2UupV2OTcoZ2C24iZ955gtXZx00V_10ED5aeAC3YxmCMhkR62Uo7nEwIJVcZEZrZsWPO2ljkgpip28ANhVyBwrsDCXKVPGQw5bu2WqsNPOD0XD_0IoW4uXMgtfDjzHhANdsoEQK6pJXNdqBG_REd7G42CHxe1oR_7FTkH34ySV0BqCM3Wq8xrUPiwjmFPsVZxpOlS27KZQUwXe_5t3sYFBd68FVFxNS6QbOYNjZ1ZEI9FUvl6555VJC8XTawo17nhfOzwALXbtf9t8aZvsYAzshk_vhLbiipElMKabzSPDcOjsdY30L_Ohd_KHMGSVM7_udzzMAo9qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علاقه بسیار شدید غزاله اکرمی بازیگر سینما و تلویزیون به مهاجم سابق استقلال: غلامرضا عنایتی ستاره سابق استقلال کراش دوران نوجوانی‌ام بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26603" target="_blank">📅 12:58 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26602">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Li0KLIp4M9HrK0MlxB7Jo5Wc7cqRmpMelQcG9yPRex7R7tx1nfiJ9RV1yKnDt32DNH9y3fQBoXRyAjGccCCuilXliiiIrTcsorHfqc4sAm8D_YAQXm9l0sfyWAg3RF_l3UtobaBG6dTWO5ntjSR848fDlaIOWvaDEACQ6OTf8XdS8KIeX7Um68vsjX3ajN9FDuAGtAXvT6sZNgEtP94hOKKwWTKAk8fgLJ8cqJjmaPo1uXMFa48jpvkCKJV0rgHrKKmQcwPiRACw3PgvTi3QDhwH5WPLNEOuxSJpSBCkxASy3uC0Yz2zDOMBms_TdMQAO11JI1VUishdm2WFEsW3dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ویدیویی‌خاطره‌ای‌انگیز ازسوپرگل‌های لئو مسی از روی ضربات ایستگاهی در دوران حضور در بارسا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26602" target="_blank">📅 12:52 · 05 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
