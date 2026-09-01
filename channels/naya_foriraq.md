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
<img src="https://cdn4.telesco.pe/file/TDm8nRhYSf-VQkdZdpu25tigChcSMyTLswhXzFeABSaKzQzn-O7O9qoR5H1c1sHudFuo1ZKCD1_tqtJTa_PqGgKrfHOF5HeoPkxTua-mb3suoskAhSF0yK8wKcTrw6AmKo75E7MnR2-ZSeX4uNHsA3MXEw2A-CbYgd7MxLYlTfEz-n1lDk9gmQDSALfTZbidu8shJIYI_Cf5Xp2rwt9HMkno75QliH4Vmff15Mj2MuLeNvDJ9viX710iaN3w5n_0HgiIw10JxHBag9-EDLg7UKbfKLe0F3UwML4QmpnhKE2PbWXvt81SL90lC5AzlpfRwcgH7zyp1r-W50vLXIde9A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 268K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-11 01:22:27</div>
<hr>

<div class="tg-post" id="msg-89113">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/080cbe3f92.mp4?token=COjiBrM0i3icB9N8XZNLjpnsdleBuQ4y8SLjf5qapPb9agxVeGfLYQh6Y1jrXPk8r6gOiLKYR2kU7uoC_0rJ_T421S71rR2xoFFFDFcUj90wf8P-P7WUVmh4VsA-YLXrBxhxgNpO9HO7RpIJ_i_3qZ7b4j--IvCAYn5Ql7SxfCB8nW8qJZ9Qg8t21rzTf-QOfEFEA2J36JcwLyBaXW8MROz5AcA3VPxiiu5w07ePuYnyDxYj_1iBl9VKJnIGkToI7MtMy1ieWnFAYFVbWvp4XQfPRugHn2BKN6OHUFMrVuoR59axeg7woKvvHYkmsCjbWBsjV_VOwDiFaLAy_DVz9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/080cbe3f92.mp4?token=COjiBrM0i3icB9N8XZNLjpnsdleBuQ4y8SLjf5qapPb9agxVeGfLYQh6Y1jrXPk8r6gOiLKYR2kU7uoC_0rJ_T421S71rR2xoFFFDFcUj90wf8P-P7WUVmh4VsA-YLXrBxhxgNpO9HO7RpIJ_i_3qZ7b4j--IvCAYn5Ql7SxfCB8nW8qJZ9Qg8t21rzTf-QOfEFEA2J36JcwLyBaXW8MROz5AcA3VPxiiu5w07ePuYnyDxYj_1iBl9VKJnIGkToI7MtMy1ieWnFAYFVbWvp4XQfPRugHn2BKN6OHUFMrVuoR59axeg7woKvvHYkmsCjbWBsjV_VOwDiFaLAy_DVz9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
الجيش الإيراني:  في المرحلة التاسعة والعشرين من عملية "البرق"، وردًا على تجاوز العدو للمناطق الجنوبية في البلاد، استهدفت القوات المسلحة الإيرانية، قبل ساعات، منشآت الرادار ومراكز تجمع القوات الإرهابية الأمريكية في قاعدة الشيخ عيسى في البحرين بهجمات مكثفة…</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/naya_foriraq/89113" target="_blank">📅 01:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89112">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇮🇷
الجيش الإيراني:
في المرحلة التاسعة والعشرين من عملية "البرق"، وردًا على تجاوز العدو للمناطق الجنوبية في البلاد، استهدفت القوات المسلحة الإيرانية، قبل ساعات، منشآت الرادار ومراكز تجمع القوات الإرهابية الأمريكية في قاعدة الشيخ عيسى في البحرين بهجمات مكثفة باستخدام طائرات مسيرة.
تعتبر قاعدة الشيخ عيسى في البحرين واحدة من أهم وأكثر القواعد الأمريكية حساسية في منطقة الخليج الفارسي، وهي مركز مهم لإصلاح وصيانة المروحيات وقطع غيار الطائرات المسيرة، وتستضيف طائرات استطلاع.
أكد قسم العلاقات العامة للجيش أن مقاتلي الجيش الإيراني قد ردوا بضراوة وبشكل واسع على أفعال العدو، وسينتقمون بشدة من المعتدين، انتقامًا يترك آثارًا عميقة.</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/naya_foriraq/89112" target="_blank">📅 00:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89111">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔻
الحرس الثوري:
أي نقطة تُستخدم لمهاجمة إيران ستكون هدفًا.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/89111" target="_blank">📅 00:49 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89110">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ترفيهي
🔻
الجيش الأردني:
منظومات الدفاع الجوي تعاملت مع 13 صاروخا باليستيا دخلت المجال الجوي للمملكة.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/89110" target="_blank">📅 00:44 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89109">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f42b196ef1.mp4?token=IIjlqQXI1pk0Q7fnm7tvpa6wIOOQZ-VFRyJfomAgWf5-2mFXrHs35iXKpgBgvutwTi-XxqEQLhN2qAn_x-x6M0oybL5HezvErWomfxUfEwzAWb7t3Od7YmK5ZfMz09nUCaP5VmOyEXG0FIQudKVzACnzr2iBtB3oRFLljVahnIIodhFYDYzitoyEKywihBq84tvX2neT94g9ecQc9_AAEN5YpUtPP4mQ527soICaLAFLuUb0t_QLJEt-HSoxI7asyrm5EDbag7J-pFSGwQtmeV91aT1-7EvJNwC90F0oUemuxwZz_74dmJSdIvzGlrqtmQn-1RKL3O1t0-Pj59YYFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f42b196ef1.mp4?token=IIjlqQXI1pk0Q7fnm7tvpa6wIOOQZ-VFRyJfomAgWf5-2mFXrHs35iXKpgBgvutwTi-XxqEQLhN2qAn_x-x6M0oybL5HezvErWomfxUfEwzAWb7t3Od7YmK5ZfMz09nUCaP5VmOyEXG0FIQudKVzACnzr2iBtB3oRFLljVahnIIodhFYDYzitoyEKywihBq84tvX2neT94g9ecQc9_AAEN5YpUtPP4mQ527soICaLAFLuUb0t_QLJEt-HSoxI7asyrm5EDbag7J-pFSGwQtmeV91aT1-7EvJNwC90F0oUemuxwZz_74dmJSdIvzGlrqtmQn-1RKL3O1t0-Pj59YYFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إرتفاع حصيلة الشهداء إلى 5 بينهم أطفال ونساء، جراء العدوان الأمريكي على مدينة سيريك جنوبي إيران</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/89109" target="_blank">📅 00:41 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89108">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">أطفال بينهم رضّع تعرضوا لهجوم أمريكي وحشي أثناء تواجدهم في حفل زفاف بمدينة سيريك جنوبي إيران.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/89108" target="_blank">📅 00:37 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89107">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔻
قسم بالله
🔻
قسم بخدا
🔻
We swear by Allah
🔻
مونتاج نايا:
#شاركها</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/89107" target="_blank">📅 00:37 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89106">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d973383857.mp4?token=qa7lIFAL25n4YoHBdF7NGWDYz6x42i3kDJQ5JfELGguHqF6K5_1Yax1CiIyvyxP2ZUpWjYtB14OXEx85kBph-D3CK7-ph7nyZIvZTsyIxbw8_2NnP-ZUF4wp6D1OtqF_S8dgqNMm-SeT4Nq9wq28UxyToaCmMo3bcsXfzdNKZEBGDAg8QWymvGKJepaC3oSGZAKNVm9mE7o_JahI-PLQcAUSw26uCoxGke4jTvivjq-RAqIPaRcFDGvlhqmOwkkmedyGZDRq_kiwGuSqaycy4tR1Xzf-408ZaBQ-0wmB4kg8-TwhpNnxdMe7PcCAQ4hphj9S6UmQ8GsQViRm5TzByA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d973383857.mp4?token=qa7lIFAL25n4YoHBdF7NGWDYz6x42i3kDJQ5JfELGguHqF6K5_1Yax1CiIyvyxP2ZUpWjYtB14OXEx85kBph-D3CK7-ph7nyZIvZTsyIxbw8_2NnP-ZUF4wp6D1OtqF_S8dgqNMm-SeT4Nq9wq28UxyToaCmMo3bcsXfzdNKZEBGDAg8QWymvGKJepaC3oSGZAKNVm9mE7o_JahI-PLQcAUSw26uCoxGke4jTvivjq-RAqIPaRcFDGvlhqmOwkkmedyGZDRq_kiwGuSqaycy4tR1Xzf-408ZaBQ-0wmB4kg8-TwhpNnxdMe7PcCAQ4hphj9S6UmQ8GsQViRm5TzByA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
حادث إصطدام عجلة بجموع مؤيدة للنظام الإسلامي في مشهد المقدسة أدى إلى وفاة 4 أشخاص وإصابة أكثر من 10 آخرين كحصيلة أولية.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/89106" target="_blank">📅 00:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89105">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c16e8d54b6.mp4?token=kwAs1lbfMkv2Btw1Fui5VcbJNaxQQWShr5ibH-E9OYAzHAOfMiI2Hs-P-B7U4qcxvKzlpdD-ZZSApymwQa8UsduLiz3NpEdiA9oTXbgEKEgMCtx-vNh79-Lw8RqyoT6807hO0m5jZqf0F3jVs05lqVHHmjlAA38yrtZBH_v2zkEBw5BEgL1TmKPR5dyq941FSHLilpCzLTS7gY3RsF5UcI7h800E5RzLd0sv9CpjtgSPz5NG0o3v19RZwBbJJgde9ED-zxqpL3_jHlIVfxCJKCV_iKWkkHUoCfjbyBVv9biqEzQffYGYv1VwVhtVj53z1SM2xcOZGPbadBhYDXB0cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c16e8d54b6.mp4?token=kwAs1lbfMkv2Btw1Fui5VcbJNaxQQWShr5ibH-E9OYAzHAOfMiI2Hs-P-B7U4qcxvKzlpdD-ZZSApymwQa8UsduLiz3NpEdiA9oTXbgEKEgMCtx-vNh79-Lw8RqyoT6807hO0m5jZqf0F3jVs05lqVHHmjlAA38yrtZBH_v2zkEBw5BEgL1TmKPR5dyq941FSHLilpCzLTS7gY3RsF5UcI7h800E5RzLd0sv9CpjtgSPz5NG0o3v19RZwBbJJgde9ED-zxqpL3_jHlIVfxCJKCV_iKWkkHUoCfjbyBVv9biqEzQffYGYv1VwVhtVj53z1SM2xcOZGPbadBhYDXB0cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سماع صوت طائرات مسيرة في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/89105" target="_blank">📅 00:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89104">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">سماع صوت طائرات مسيرة في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/89104" target="_blank">📅 00:29 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89103">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14fc3cc3b9.mp4?token=hYFwCKiBOfwW-RRAOKKMTG4jzIW7CQAYSbSrUQwgkz4lNtud1dFJgBBhn2ftJTwIlIvIpRRrGY_zLbFWLJ2R_uxmxG04QhFjeWvNHhsYV6CnRcldwHf5ugIh8ZTPUN2GPRJAVukAH1dRWtffeLQysVmAJwiPo811C-84Q6Z34C_BrJ1I_rn6XB9qJ2HiNEXpl90JuPZPNW0ZafYOC2qr1Y7dElUdaIt5UjLpbWybjM_E7rEn3_RgWoTXxe5rx8CtRYoVHSMHDg6wEiNKmJ4Oz7XXl1UR3jIeEIvBz4oF35Kb9wslBWLq4GFYOMc77YijJZi8jJsGqFAaGNCWAEi1Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14fc3cc3b9.mp4?token=hYFwCKiBOfwW-RRAOKKMTG4jzIW7CQAYSbSrUQwgkz4lNtud1dFJgBBhn2ftJTwIlIvIpRRrGY_zLbFWLJ2R_uxmxG04QhFjeWvNHhsYV6CnRcldwHf5ugIh8ZTPUN2GPRJAVukAH1dRWtffeLQysVmAJwiPo811C-84Q6Z34C_BrJ1I_rn6XB9qJ2HiNEXpl90JuPZPNW0ZafYOC2qr1Y7dElUdaIt5UjLpbWybjM_E7rEn3_RgWoTXxe5rx8CtRYoVHSMHDg6wEiNKmJ4Oz7XXl1UR3jIeEIvBz4oF35Kb9wslBWLq4GFYOMc77YijJZi8jJsGqFAaGNCWAEi1Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله اكبر لحظة السقوط المباشر داخل قاعدة الاحتلال الاميركي في الاردن.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/89103" target="_blank">📅 00:26 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89102">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ed96b09fb.mp4?token=Vo30SgVYI0-yG6gWxWXIc80eSnaLCkiJtz-rijHoBbSf7NaErSYu6W7rTFy0HfIX6-uelqJ1ORteot_4mqzXJpXg5ffoiHYUMh_-xiVOeVNjgsQZq90yHMf7kRas8veR-5yw6cz0EnwiJ7jwniN2KDjhMO7nvT281bgGyS2pSJsEYuRfeOvrXnRUJtYFNKC5Lgf-dkcHdynUfVT4twfxTgtoLoPSfF4DBExkEXq1-Ls1wX_1cDDf0OldUmGkOLGDf9XsYhGHGx3k84fAPgGllA9XKnrco4JkSenwbq-IqVBw4jPF1mZFEQe13ph0JFCeBFjTejvpspSpjzBQTnETuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ed96b09fb.mp4?token=Vo30SgVYI0-yG6gWxWXIc80eSnaLCkiJtz-rijHoBbSf7NaErSYu6W7rTFy0HfIX6-uelqJ1ORteot_4mqzXJpXg5ffoiHYUMh_-xiVOeVNjgsQZq90yHMf7kRas8veR-5yw6cz0EnwiJ7jwniN2KDjhMO7nvT281bgGyS2pSJsEYuRfeOvrXnRUJtYFNKC5Lgf-dkcHdynUfVT4twfxTgtoLoPSfF4DBExkEXq1-Ls1wX_1cDDf0OldUmGkOLGDf9XsYhGHGx3k84fAPgGllA9XKnrco4JkSenwbq-IqVBw4jPF1mZFEQe13ph0JFCeBFjTejvpspSpjzBQTnETuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">أثار الجريمة الأمريكية في سيريك حيث تم قصف منزل أثناء تجمع المواطنين فيه خلال إقامة حفل زفاف.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/89102" target="_blank">📅 00:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89101">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">تحليق مقاتلات حربية عند الحدود العراقية الاردنية الانباء تشير محاولة تصدي للمسيرات الايرانية.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/89101" target="_blank">📅 00:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89100">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WjPJQGOZrv-VIbgJOhsWUQ1mepIiwoevdFKrjV5aYU5LLrImFiq4sxaiiLBVprHk1XG3a2csjCi4biKT6V6Ncx3pS3cC8yJoMB1WIzr6XExZmYqcpVr5YyCQtqPx1atM3ZY-R-vkMM60lAG8J3pggicpCjIY6TrgjxPuC6OyxjWXUkSAZoaX4Ob6pimVG3k09-rai8wavL4OeyvzaE98SLK3JdMiP84yQVuMFZxX0i7lDAzuWGaaEA7solqpsXLxR3Rl5HmlUyATUy5XS5f8_4eZX1Cwq2mwZXEsWgHwCF_szJENli2NVJ8p0VUFy2bFrdrRGWTNxaj13DgEZ9kVPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إصابات بصفوف الأطفال جراء العدوان الأمريكي الوحشي على حفل زفاف في مدينة سيريك الإيرانية</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/89100" target="_blank">📅 00:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89099">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b044a65a7a.mp4?token=iHVSIF6QHcfZe3gb74tGt7KX-J6DDu16Pa_Chm4KvVnuYprXnMDJ4e6iMrtG7Z1czjiSg4bzVz6w3_AsMTajdWAzNY4WVGrPOvHD8Ji5utsjO8xqWCFQiD_BsYJAVmnb5LbSD5HdtHECBAb_xFyKAxI0reUA1iQuUd_Lsz5QBREyi0bB1IRGz7G6JoMOQcVd-hcwoINs-KGF4kou6vpLY1G-fFWMWoiFkufpLkrDtMbTnGuE8BfAJnQ_hY6Fbyek1uqkV39ExI7O6JirBl36ifz_Sx3sKRIl1W3lP6sbE_pAmWZ-bycLKLDwNZQyKmSPq5ebYWaT7MspKmnCSs3zZgygOnG36tsyU1jbjiVI_RFZFFBkDNvrQuEKslK_nyguzfjlIuVU3Tn2jpE-mpy2-rUCfJeee804cvqRIuVlRdgCA1Kb8khabP2OYojWO9wpw89Sv5kkf--4aWg_w4JHKtHdkOSs7l1TzcZK8C4GusjZ1llrSnklBYtmqH-xScGw1m2brVfaqjRkFV7HOKUlasg9cPo45ucF_WJsyehZwZB0jMh4tqlck_Ei6BKs1x0cQ_s7V-L1yN_I6mWFTECCybDn53Qq-Dq_yOTjkaCZvKIWfs-kejjfZ1tBzfgXVPVdqV11qzQ-H2lVOf0TyZoedvPj_p5XozIGkfSe8OT1Oms" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b044a65a7a.mp4?token=iHVSIF6QHcfZe3gb74tGt7KX-J6DDu16Pa_Chm4KvVnuYprXnMDJ4e6iMrtG7Z1czjiSg4bzVz6w3_AsMTajdWAzNY4WVGrPOvHD8Ji5utsjO8xqWCFQiD_BsYJAVmnb5LbSD5HdtHECBAb_xFyKAxI0reUA1iQuUd_Lsz5QBREyi0bB1IRGz7G6JoMOQcVd-hcwoINs-KGF4kou6vpLY1G-fFWMWoiFkufpLkrDtMbTnGuE8BfAJnQ_hY6Fbyek1uqkV39ExI7O6JirBl36ifz_Sx3sKRIl1W3lP6sbE_pAmWZ-bycLKLDwNZQyKmSPq5ebYWaT7MspKmnCSs3zZgygOnG36tsyU1jbjiVI_RFZFFBkDNvrQuEKslK_nyguzfjlIuVU3Tn2jpE-mpy2-rUCfJeee804cvqRIuVlRdgCA1Kb8khabP2OYojWO9wpw89Sv5kkf--4aWg_w4JHKtHdkOSs7l1TzcZK8C4GusjZ1llrSnklBYtmqH-xScGw1m2brVfaqjRkFV7HOKUlasg9cPo45ucF_WJsyehZwZB0jMh4tqlck_Ei6BKs1x0cQ_s7V-L1yN_I6mWFTECCybDn53Qq-Dq_yOTjkaCZvKIWfs-kejjfZ1tBzfgXVPVdqV11qzQ-H2lVOf0TyZoedvPj_p5XozIGkfSe8OT1Oms" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
الحرس الثوري:
مشاهد من الهجمات الصاروخية المكثفة على الأهداف الأمريكية في الأردن، وهي المرحلة الثانية من عملية "تصحيح مسار المعتدين.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/89099" target="_blank">📅 00:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89098">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f76b7785b5.mp4?token=kEuBYmRk8lAYDunSeUHv3rou7MgIvcd4pcfs46ChiWERV-VBHFUVGBMRb5n00xkT1awlRuS5dfbcGdTqAEtRuukaumclLEBimqVNJhmJBwteSA0RnHy09OZ5pOTJXVKwoC31b7OWmecgq7oj-eudVMXawzUj90rNrQS3uhGkxs8NedBiI-kS8QirSsA4UW5GUBn0_8WQUSntSr8sUG8DWvifybfdKKyBOkYs6gQ2SEOjJ6qkov9QrMh0glD7cZiJ_O3AG6y86GEO83RSWcEkkU7BePi1ZqnlgYIqwlKafbsr1EPsDUlvgrOIlIyvOlIx571-frqiOE92caFwduw7yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f76b7785b5.mp4?token=kEuBYmRk8lAYDunSeUHv3rou7MgIvcd4pcfs46ChiWERV-VBHFUVGBMRb5n00xkT1awlRuS5dfbcGdTqAEtRuukaumclLEBimqVNJhmJBwteSA0RnHy09OZ5pOTJXVKwoC31b7OWmecgq7oj-eudVMXawzUj90rNrQS3uhGkxs8NedBiI-kS8QirSsA4UW5GUBn0_8WQUSntSr8sUG8DWvifybfdKKyBOkYs6gQ2SEOjJ6qkov9QrMh0glD7cZiJ_O3AG6y86GEO83RSWcEkkU7BePi1ZqnlgYIqwlKafbsr1EPsDUlvgrOIlIyvOlIx571-frqiOE92caFwduw7yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إستشهاد طفل ذات 4 سنوات جراء العدوان الأمريكي الغاشم على حفل زفاف في مدينة سيريك جنوبي إيران.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/89098" target="_blank">📅 00:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89097">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔻
الحرس الثوري: استهدف صواريخ باليستية قاعدة مشاة أمريكية في الأردن، والمعروفة باسم "معسكر تبتين"، مقتل عدد كبير من القوات الأمريكية.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/89097" target="_blank">📅 00:12 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89096">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed7201cf8c.mp4?token=ePZwrm_nLxMuRodphWbTK8f1EFguQajRhwHuv4ejBBshIUig6Ym4X4fnkimHe2ifQ6K7gIwRJ3hZadduA0jyaWJkbEO2dQfUh6hcT2K-iyTnfUyKFYu-3Copga0lFLAczsSXfl5Txe-_rflKJooMvzD_RkxOJPFkVy1Qc81xBuy65YJKmtnVQoBAipM-0lRREEWjOOMakoCLUAr-FfRYVYoaQDo7WDyPrqB2E3Q1_chnInlSdsDd7qjK8nWUJPNswD5j0FL0up1-9c586aBlOMfaKopnpkkXm7sB4He0twO3y5gZ1PX8_gEcMbslBD65H80zdLVvMFliXtjq9RV2uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed7201cf8c.mp4?token=ePZwrm_nLxMuRodphWbTK8f1EFguQajRhwHuv4ejBBshIUig6Ym4X4fnkimHe2ifQ6K7gIwRJ3hZadduA0jyaWJkbEO2dQfUh6hcT2K-iyTnfUyKFYu-3Copga0lFLAczsSXfl5Txe-_rflKJooMvzD_RkxOJPFkVy1Qc81xBuy65YJKmtnVQoBAipM-0lRREEWjOOMakoCLUAr-FfRYVYoaQDo7WDyPrqB2E3Q1_chnInlSdsDd7qjK8nWUJPNswD5j0FL0up1-9c586aBlOMfaKopnpkkXm7sB4He0twO3y5gZ1PX8_gEcMbslBD65H80zdLVvMFliXtjq9RV2uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدون اي مقاومة تذكر... الصواريخ الايرانية وهي تسقط على اهدافها في الاردن.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/89096" target="_blank">📅 00:12 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89095">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔻
الحرس الثوري: استهدف صواريخ باليستية قاعدة مشاة أمريكية في الأردن، والمعروفة باسم "معسكر تبتين"، مقتل عدد كبير من القوات الأمريكية.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/89095" target="_blank">📅 00:10 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89094">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">منظمة الطيران المدني الإيراني: لم يتم إصدار أي إشعارات للطيران (نوتام) بغرض إغلاق المجال الجوي للبلاد.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/89094" target="_blank">📅 00:10 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89093">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b18f5c7683.mp4?token=Bz6w847fmscpdT62yhWSBUn4-nRtNtWMABbMIhnionMDW0rHCRhD8q5OHN8rKzrPoFzjp3fCvXPjV9hWVYo91afA4Dk62XvJ_S_bdFtTV4ZU53CfTIvWpSdqcHUw4xHAEtTdZYlaA8tyKbPPV359l_o8jgiAu0xYUkeIKTVCv4MY-pEbXGnp9px5p_BR59M5_iWJI_pQ7Cnq6Ap-91evXmXw0c4qE4OT42_7EoAM-cflPnW4o8DDVGOYhVlEWoQR4QceEhBpSLpSpWzpXsomBow2aqwdwcH7qrAxriwI60LcSEovHA696UL7bmfDAQwPDeL1eCxRctqSUM-NRyYjdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b18f5c7683.mp4?token=Bz6w847fmscpdT62yhWSBUn4-nRtNtWMABbMIhnionMDW0rHCRhD8q5OHN8rKzrPoFzjp3fCvXPjV9hWVYo91afA4Dk62XvJ_S_bdFtTV4ZU53CfTIvWpSdqcHUw4xHAEtTdZYlaA8tyKbPPV359l_o8jgiAu0xYUkeIKTVCv4MY-pEbXGnp9px5p_BR59M5_iWJI_pQ7Cnq6Ap-91evXmXw0c4qE4OT42_7EoAM-cflPnW4o8DDVGOYhVlEWoQR4QceEhBpSLpSpWzpXsomBow2aqwdwcH7qrAxriwI60LcSEovHA696UL7bmfDAQwPDeL1eCxRctqSUM-NRyYjdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدون اي مقاومة تذكر... الصواريخ الايرانية وهي تسقط على اهدافها في الاردن.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/89093" target="_blank">📅 00:08 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89092">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce4cb478ba.mp4?token=onajLHmF4AKzQZT_2WrGMbLu6t_I7zjd0nL5nBUR6gPk4GYUtKx5kJ7hVEMjHpXXmnq8-2NXkLEQ-uZOpxR7LTqbz1ZlJAiauz_EAIw1pqCuzicuf4HCuCiLNLhgO51ErwDiCWSXDd433R4purEduqlxH8YpcHZS0ZHqidgWI7q63asPSUTQZt3nTVHVbu3BV-aIeM_J_g4gYNXaRbcflG_EJezZl8V6VW9wX4t7KaMtqtvdtGzzCzonPhPVcpj3c9JIzCcb5OzlaG2dfJCsPqdoy-PS5fWErfFwl1xqwBqvoN63VfPSX-MYGBbKRKl66W7d3lOt71vNRstfAsIudw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce4cb478ba.mp4?token=onajLHmF4AKzQZT_2WrGMbLu6t_I7zjd0nL5nBUR6gPk4GYUtKx5kJ7hVEMjHpXXmnq8-2NXkLEQ-uZOpxR7LTqbz1ZlJAiauz_EAIw1pqCuzicuf4HCuCiLNLhgO51ErwDiCWSXDd433R4purEduqlxH8YpcHZS0ZHqidgWI7q63asPSUTQZt3nTVHVbu3BV-aIeM_J_g4gYNXaRbcflG_EJezZl8V6VW9wX4t7KaMtqtvdtGzzCzonPhPVcpj3c9JIzCcb5OzlaG2dfJCsPqdoy-PS5fWErfFwl1xqwBqvoN63VfPSX-MYGBbKRKl66W7d3lOt71vNRstfAsIudw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد اخرى للصواريخ الايرانية وهي تتوالى نحو القواعد الاميركية في الاردن.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/89092" target="_blank">📅 00:05 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89091">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce4e3347d0.mp4?token=WecSZxOBBG-HxC5tqlEiEzgqZRBmSKX9c8xfODzBmDrL201az9GI0V_43ynWM5K6bhPP3bZqEPqaadRc3sEXa4ygqTe1ASnEv1KUFsg-xFZfJuL-pj6PsOZkl4N4gmro_61vs8L_ERkG0RHP6F6_3_X8xrKJqzfbWkc6OcSHHMFTyVNSwfR5A3PFCfgSd1O8W0f6rWu-d9ef7XuvINtIyhCdiBzPKi_BN0OBajtnfYaHSCXZvr8BsegHH4bvrHaq7qm0fLRL30kZEZ-eO_Jj0dyygSoENhUegw6EgvqsoPOJou_b37QlzFmGjRENKTBHSTnwr9BhpwooARdIGCeMiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce4e3347d0.mp4?token=WecSZxOBBG-HxC5tqlEiEzgqZRBmSKX9c8xfODzBmDrL201az9GI0V_43ynWM5K6bhPP3bZqEPqaadRc3sEXa4ygqTe1ASnEv1KUFsg-xFZfJuL-pj6PsOZkl4N4gmro_61vs8L_ERkG0RHP6F6_3_X8xrKJqzfbWkc6OcSHHMFTyVNSwfR5A3PFCfgSd1O8W0f6rWu-d9ef7XuvINtIyhCdiBzPKi_BN0OBajtnfYaHSCXZvr8BsegHH4bvrHaq7qm0fLRL30kZEZ-eO_Jj0dyygSoENhUegw6EgvqsoPOJou_b37QlzFmGjRENKTBHSTnwr9BhpwooARdIGCeMiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد للصواريخ الايرانية وهي تنهل على اهدافها بدون اي مقاومة جوية تذكر في الاردن.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/89091" target="_blank">📅 00:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89090">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">مصدر إيراني: عدة نقاط في شبكة الكهرباء بمحافظة هرمزگان كانت هدفًا للعدوان  الأمريكي.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/89090" target="_blank">📅 00:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89089">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔻
مصدر مطلع لنايا...
الأصوات التي سمعت في بعض مناطق إيلام تعود إلى انفصال محركات الصواريخ الايرانية.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/89089" target="_blank">📅 00:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89088">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pcqG_gnX7mSTJLdEYKYjRB9Ol4NLr8pLXLC-YeopIhGo-7gjII6Ivd79DHZUcOFjdMASvlZcQsPuG3OMV5hGXCARKxNeqZ79zFJxnWJCBfE9gkyYYCEa0T_vGDDda9kH4VBwM54VsQXEpq7hkFJvuyRloBQbPYSycjdkeRUugfMl-NzCvQVSnSW_TlBIaaEJ0wuR_4ixhhpEcM5Z0c-wfTD0fkMcf1KuCW8yluw493vAkdZg35w8efgavDX63VRFv51n0pmTxiqpqyA5UO91UGTBMix7CzCUalXgdbzNF-a8t0btF9EGj5b298oRy04DnIB7ix-IfVnZb87bvQI1Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاهد أخرى للجريمة الأمريكية في سيريك</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/89088" target="_blank">📅 23:59 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89087">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88e9a34976.mp4?token=qfNGL-84xQxdPstqs-2v2AJFaKmwDxTR3sZJ4BoXB5G9BS4J_3cHwc7ZFgDEOG2sPffXzXlmjFScaw5FVARTk-jzYiSYJu_rnR265MS2xLs2p2cWAMPLGbHQ8yHww5htZPhZEas4mnd_mao8hg0xpfgVCwC_DS5WvBsUkANfElAIbi2QTDSt9ezTPKm316r1vCBSkKeXZsRMTe2JIa_uspNu82pcMEUih75smyx1nvd7oCWuMSj2PB_tTEL7dUnFY804keaVko_3QBm1i4dtPnCJPqGXvxqk5XhhCJdf3cnx9p__xjP_3FxcVbNp1U7hLsk6ZTgcRjo0IZRAkqec6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88e9a34976.mp4?token=qfNGL-84xQxdPstqs-2v2AJFaKmwDxTR3sZJ4BoXB5G9BS4J_3cHwc7ZFgDEOG2sPffXzXlmjFScaw5FVARTk-jzYiSYJu_rnR265MS2xLs2p2cWAMPLGbHQ8yHww5htZPhZEas4mnd_mao8hg0xpfgVCwC_DS5WvBsUkANfElAIbi2QTDSt9ezTPKm316r1vCBSkKeXZsRMTe2JIa_uspNu82pcMEUih75smyx1nvd7oCWuMSj2PB_tTEL7dUnFY804keaVko_3QBm1i4dtPnCJPqGXvxqk5XhhCJdf3cnx9p__xjP_3FxcVbNp1U7hLsk6ZTgcRjo0IZRAkqec6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد اخرى للصواريخ الايرانية وهي تنقض على احد القواعد الاميركية في الاردن.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/89087" target="_blank">📅 23:58 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89086">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49aae8ff22.mp4?token=X7bsYS4ZT0U3PaYTfwmh1bgvYh8c0qoFepD_3MnOWNV80umtrHCtOhYYQQtVybnGgN2TjWtvtvfES-RVtVTej7fAadRwfOAxp_wfj4H0e0YhlJobTDm3RWuoC6yovUhOa2nB6BXRLvU6D1B2z3Cz0iyZelhXx5WLfE2tc-ZK5j5hyUufu1ZJotsmhCaGD2JpMz0yYD7ph42AJwwEsUhVEm3y9HJcurCsApYOPetnxNBN1agslMJp11lJyytwjBfa2d_HqUjDwQ9AlKnrO-hEut_EROykwaNKt98fHtp-qC3_B24lJYUJpW_TEyC4LgqCfQhV2ws-ChbfW6p5oayQlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49aae8ff22.mp4?token=X7bsYS4ZT0U3PaYTfwmh1bgvYh8c0qoFepD_3MnOWNV80umtrHCtOhYYQQtVybnGgN2TjWtvtvfES-RVtVTej7fAadRwfOAxp_wfj4H0e0YhlJobTDm3RWuoC6yovUhOa2nB6BXRLvU6D1B2z3Cz0iyZelhXx5WLfE2tc-ZK5j5hyUufu1ZJotsmhCaGD2JpMz0yYD7ph42AJwwEsUhVEm3y9HJcurCsApYOPetnxNBN1agslMJp11lJyytwjBfa2d_HqUjDwQ9AlKnrO-hEut_EROykwaNKt98fHtp-qC3_B24lJYUJpW_TEyC4LgqCfQhV2ws-ChbfW6p5oayQlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توثيق اخر يظهر لحظة انقضاض الصاروخ الإيراني على القاعدة الأمريكية في الأردن</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/89086" target="_blank">📅 23:56 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89085">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fba7f7492.mp4?token=Nkyyix9aDW5Y1Z7ckqBwWw3ejvVTOMLfP3cH0HwtgFPzlT3s9FhUxZzXuywu5nJUdRCu98OJb_PHkC-EUgwDsEInfMHQiwEWXUVskmuQFLT1tRVvIqdSCkQSzL7s6DQckH6RKR0RKzY4ApuUHzHiyIPj4UiozoHFjbK6dbnudZsIGDsEwevcxXN83l1NtTjlNyRcnBPIX8vYqotFoW8S5arqXa5arDWZ9BNj6-5vjwGL81h8fnX0tVz2nLAljcITs-hJ3Do6aITzFSFBpa3wx9GTP8UUENUKHEdLaMZoUYDQS00e3l4SR9FGg00Vev88xgPLjoce-7kTEDvbMXy3rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fba7f7492.mp4?token=Nkyyix9aDW5Y1Z7ckqBwWw3ejvVTOMLfP3cH0HwtgFPzlT3s9FhUxZzXuywu5nJUdRCu98OJb_PHkC-EUgwDsEInfMHQiwEWXUVskmuQFLT1tRVvIqdSCkQSzL7s6DQckH6RKR0RKzY4ApuUHzHiyIPj4UiozoHFjbK6dbnudZsIGDsEwevcxXN83l1NtTjlNyRcnBPIX8vYqotFoW8S5arqXa5arDWZ9BNj6-5vjwGL81h8fnX0tVz2nLAljcITs-hJ3Do6aITzFSFBpa3wx9GTP8UUENUKHEdLaMZoUYDQS00e3l4SR9FGg00Vev88xgPLjoce-7kTEDvbMXy3rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توثيق اخر يظهر لحظة انقضاض الصاروخ الإيراني على القاعدة الأمريكية في الأردن</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/89085" target="_blank">📅 23:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89083">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c7600425e.mp4?token=UD1cP51UXGbfClQD7RUMvbYQ-SporJEQkzUo--YsiymWmxeX7fb8-elG5-OSD6Mi4g7Q617pq4SGEvWYWtNiQcjAnksoi6i8TBNtViNsxX1FohmWvadivlnUBMWkegLvTieNQfdbfwk1m3MWXAHQGk8YehqeicktgF4xwWx0FFDpSL2g_Q48E4XtAm8CbGyJ0Owwm2IFfGLZUOfo1aC_Rbh95J0dbkY4Uk2s24cc0jCtYDASqVsXfUYrP6f5hQh4RyQgvPAVmcmKUK-Nx7_nfm0fPDmg_TbIR1psecYdcIlMZDj42Bcpwlvlskw_FH4B9Unvn5rTdRe5s1sw0mE6Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c7600425e.mp4?token=UD1cP51UXGbfClQD7RUMvbYQ-SporJEQkzUo--YsiymWmxeX7fb8-elG5-OSD6Mi4g7Q617pq4SGEvWYWtNiQcjAnksoi6i8TBNtViNsxX1FohmWvadivlnUBMWkegLvTieNQfdbfwk1m3MWXAHQGk8YehqeicktgF4xwWx0FFDpSL2g_Q48E4XtAm8CbGyJ0Owwm2IFfGLZUOfo1aC_Rbh95J0dbkY4Uk2s24cc0jCtYDASqVsXfUYrP6f5hQh4RyQgvPAVmcmKUK-Nx7_nfm0fPDmg_TbIR1psecYdcIlMZDj42Bcpwlvlskw_FH4B9Unvn5rTdRe5s1sw0mE6Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات جديدة في الأردن</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/89083" target="_blank">📅 23:51 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89082">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">انفجارات جديدة في الأردن</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/89082" target="_blank">📅 23:49 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89081">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ab492be24.mp4?token=Pg2xn_TkNFUX-ho_9G71jQXuJt3fU4TnnmmQkh6XVGCCZ9ka6ur98Ko41Anb_bwRNKbaq0r-_IzHAXC_wjxaegrtmBxV-vl7Aglxilbhz4GvBgW-4RFGh5jAhCwQzjF9pDqw3tOehxEpxOEM7XscuFUqKoiP539jEeSpNGDQb9H_NZQx3iCcKJmknVUfuokt9pnsC5HgamuQKk3Zy0oe8xPH4k2SVG5GVNt8yiF3ZKW49ilwGfNJbGXVJXYbVZfVx8qRw8LGbGDXmzcXCM-WNloT4hgo7ND1vgCVLeUn8brDgWfSxZ8dQYHXknjg39oAQdDn78hunzlL6QbuUNyjhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ab492be24.mp4?token=Pg2xn_TkNFUX-ho_9G71jQXuJt3fU4TnnmmQkh6XVGCCZ9ka6ur98Ko41Anb_bwRNKbaq0r-_IzHAXC_wjxaegrtmBxV-vl7Aglxilbhz4GvBgW-4RFGh5jAhCwQzjF9pDqw3tOehxEpxOEM7XscuFUqKoiP539jEeSpNGDQb9H_NZQx3iCcKJmknVUfuokt9pnsC5HgamuQKk3Zy0oe8xPH4k2SVG5GVNt8yiF3ZKW49ilwGfNJbGXVJXYbVZfVx8qRw8LGbGDXmzcXCM-WNloT4hgo7ND1vgCVLeUn8brDgWfSxZ8dQYHXknjg39oAQdDn78hunzlL6QbuUNyjhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توثيق اخر للإصابات الصاروخية المباشرة في القواعد الأمريكية بالأردن</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/89081" target="_blank">📅 23:48 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89079">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88410a6767.mp4?token=QUKFMfu5lzrswLPEjrE01MV3pO5bTOaqycGV2LyCGU_6-RNNmClJVazzDF01lCiga3KGnzzyAIBdShJuWnH-oebVhveLGKhEdAr19RrgApT05qrqlLsoD_3YQSuJIPIvhG6moWFT-nfAgLxHZ62LU27_-FzrhpG1hhxroSdQ96NBpbfWHvsxowihzFiWeO6dmXN2tVgkus8P-rYIUIfm8pdVVLGgzWMv4u6hzol8HDrTsjjNvAcb8owM6EYEKHNSNkbiVmS4yJZPlcXC5UkxW-OL9dqWBgQvLuns-oD67aBFd_WWptTR0JzEVzMqH0G8983hmqL1VoSupzIyswjUXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88410a6767.mp4?token=QUKFMfu5lzrswLPEjrE01MV3pO5bTOaqycGV2LyCGU_6-RNNmClJVazzDF01lCiga3KGnzzyAIBdShJuWnH-oebVhveLGKhEdAr19RrgApT05qrqlLsoD_3YQSuJIPIvhG6moWFT-nfAgLxHZ62LU27_-FzrhpG1hhxroSdQ96NBpbfWHvsxowihzFiWeO6dmXN2tVgkus8P-rYIUIfm8pdVVLGgzWMv4u6hzol8HDrTsjjNvAcb8owM6EYEKHNSNkbiVmS4yJZPlcXC5UkxW-OL9dqWBgQvLuns-oD67aBFd_WWptTR0JzEVzMqH0G8983hmqL1VoSupzIyswjUXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتفاع عدد الشهداء إلى 4 وإصابة أكثر من 50</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/89079" target="_blank">📅 23:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89078">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/580ec8cb1c.mp4?token=FyYGC2ki0eWbODJ1cwBFz_ExoqaEGQoz8GemwywUvJuDcc3BjG43IR_GXYu02V3T-4j4vqNzkxBK0OlT2fHTTdAZIjS6iuXR7ga0mXHJ0mWOlcXXdEzkZ4Way8KaTxKEhLtbXiJbb4HBYzben5yb0wCpoxnLlZLWetXqydett_wSIsj_hzQB6lY1pp1MxKdS372UkGHkjr5rPgEQqAmp3QJyq7CbVnRfUtjJu2y-XNE4Ia7seKnQP085oh1caZIlGwIGz3o2uzQHhaH13hAC0lhnw30HiXfq13vmHO4kyKgaTaV2Z3ajgcfjS1fzasvAULdDRjVlCxwyoHJm1XeXCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/580ec8cb1c.mp4?token=FyYGC2ki0eWbODJ1cwBFz_ExoqaEGQoz8GemwywUvJuDcc3BjG43IR_GXYu02V3T-4j4vqNzkxBK0OlT2fHTTdAZIjS6iuXR7ga0mXHJ0mWOlcXXdEzkZ4Way8KaTxKEhLtbXiJbb4HBYzben5yb0wCpoxnLlZLWetXqydett_wSIsj_hzQB6lY1pp1MxKdS372UkGHkjr5rPgEQqAmp3QJyq7CbVnRfUtjJu2y-XNE4Ia7seKnQP085oh1caZIlGwIGz3o2uzQHhaH13hAC0lhnw30HiXfq13vmHO4kyKgaTaV2Z3ajgcfjS1fzasvAULdDRjVlCxwyoHJm1XeXCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من الهجوم الصاروخي الإيراني على القواعد الأمريكية في المنطقة</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/89078" target="_blank">📅 23:43 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89077">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3896fd682d.mp4?token=fhxAJ9JVsPmegwjE00Vjzg6bf8LBdtHyXRpXsZcFPeA38FWrftIuk0cx-No1ATqKGmLCFW6_HCl9G3XJUT0kVcr9-avl_5wU8wl21pnVV0EPI-dVJ1LdlDbJI3YgIlzZUTziQR1JhIYVfjdJKLvpy_Pu91WNeYFlDEAtQuCnfZN1Qm1Qh6IiuOUE3BNSzNVtblP8qAiI5_vjFfEr19LsKw_JhUhu67YY7stom1eVac9f5G5N7ObOShM3GWeCaVbCLsM5UIP4m0uVgRGKzFE4_AhnPheZHkjF4XHwEv7Q3cpKoVR0qkwQP90mqpEUIVffOkVdGROqUlX7LFheb1xo-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3896fd682d.mp4?token=fhxAJ9JVsPmegwjE00Vjzg6bf8LBdtHyXRpXsZcFPeA38FWrftIuk0cx-No1ATqKGmLCFW6_HCl9G3XJUT0kVcr9-avl_5wU8wl21pnVV0EPI-dVJ1LdlDbJI3YgIlzZUTziQR1JhIYVfjdJKLvpy_Pu91WNeYFlDEAtQuCnfZN1Qm1Qh6IiuOUE3BNSzNVtblP8qAiI5_vjFfEr19LsKw_JhUhu67YY7stom1eVac9f5G5N7ObOShM3GWeCaVbCLsM5UIP4m0uVgRGKzFE4_AhnPheZHkjF4XHwEv7Q3cpKoVR0qkwQP90mqpEUIVffOkVdGROqUlX7LFheb1xo-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الاردن تشدد على منع توثيق الهجمات الايرانية من قبل مواطنيها: المستوطنات الصهيونية بالقرب من قواعد الاحتلال الاميركي
😆</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/89077" target="_blank">📅 23:41 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89076">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XkOxlk4RyTJmg6ovXp52T9EJxvhoA10xHff6ryeQRHWceAa-KaE8whq4R9uA1nM2OYDUuoyW7tG_CBCXykxGslYR0ohEesuY7WkUQGkcG5jgtHlwSgAvL6pypR9C-MPtfRh9_7MtobC4JQm60nMpTkIUszi5uJm9vHTmfZaB0myOeYsgMHYvo4-tMWgw5-nLVWI4COadiiWRyBuNNJJdch66xP6KrQR3Bi1KB8GxEFmt9fMQfIzzchT2FJm9VS2_CSyMYEO5prs6e6OYDTkFGq1V6lkyxJnCmBy-p7_jTbMvBTrrb7Wo6OaniFdnmtZ1guuo2CNHAb6MnUAenBcc0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إن عدتم..عدنا.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/89076" target="_blank">📅 23:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89075">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a815d4d7a.mp4?token=KZw0qXUzIhYU5gkKkIMAd7k0qoMC4lwoU1Ca3xkkBkb69FsSwhO4lwmS98bbOpaOU2bztis-78g68KjDn6OFNtR3U6sl1vf3C0dvA9ut7UxGkU6EJ_zFWZZn0RvKImk7MTFCyDR0hqGrOdTtt7oDFr_gd3l0RiMkpWPE40WR5k-QYG9Frd_QYx3638C2iSHtPMCSS2cGiUN66uyAZexPIq7jS7eirtLsgtrS1BlqRXhQdqjo2q9C5rzH0jEI8_c4vrblI9k5c5eKl0knE-1xRsceLuFK0-cDjyOtpN8mieTx8y7rIy96UCzn5fSzgx7BDVtaV_nVba81gV1nDC9QAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a815d4d7a.mp4?token=KZw0qXUzIhYU5gkKkIMAd7k0qoMC4lwoU1Ca3xkkBkb69FsSwhO4lwmS98bbOpaOU2bztis-78g68KjDn6OFNtR3U6sl1vf3C0dvA9ut7UxGkU6EJ_zFWZZn0RvKImk7MTFCyDR0hqGrOdTtt7oDFr_gd3l0RiMkpWPE40WR5k-QYG9Frd_QYx3638C2iSHtPMCSS2cGiUN66uyAZexPIq7jS7eirtLsgtrS1BlqRXhQdqjo2q9C5rzH0jEI8_c4vrblI9k5c5eKl0knE-1xRsceLuFK0-cDjyOtpN8mieTx8y7rIy96UCzn5fSzgx7BDVtaV_nVba81gV1nDC9QAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد اخرى للصواريخ الايرانية في سماء الاردن.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/89075" target="_blank">📅 23:38 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89074">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cbd023f64.mp4?token=aybmjpLiZMvVnz4IgpYti14ArTa_Z0MoetaXzhYv-7RIQe9X6XpcLkWdGKhpIgQXx8wukjjoncjuCbMvgEDj6i3gJSGaPa9xE9vAogksACa4sYUyFe87f8nuX7VUYp8-XgqaHztIuMfxxc_nO1INKEpRee6WmhUVhvE0Wt0tW4smR573vTbIt9S9EYYhRJA4Ws_JZX6MBZpHEgZ_kYo6CK1M5ioBxd-36B7lwUVfpQp6X8_vLJ8lqe7s27wOaYonu8A9O38bt_UoxE-_k1ayAZB7eySQv7jZKnzYlnh3Smep_FVUSIZu0V4WQLNX7f64FOKLU1_fN5ha6umDGw_trQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cbd023f64.mp4?token=aybmjpLiZMvVnz4IgpYti14ArTa_Z0MoetaXzhYv-7RIQe9X6XpcLkWdGKhpIgQXx8wukjjoncjuCbMvgEDj6i3gJSGaPa9xE9vAogksACa4sYUyFe87f8nuX7VUYp8-XgqaHztIuMfxxc_nO1INKEpRee6WmhUVhvE0Wt0tW4smR573vTbIt9S9EYYhRJA4Ws_JZX6MBZpHEgZ_kYo6CK1M5ioBxd-36B7lwUVfpQp6X8_vLJ8lqe7s27wOaYonu8A9O38bt_UoxE-_k1ayAZB7eySQv7jZKnzYlnh3Smep_FVUSIZu0V4WQLNX7f64FOKLU1_fN5ha6umDGw_trQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد اخرى للحظة سقوط المباشر لصاروخ الايراني في العقبة</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/89074" target="_blank">📅 23:36 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89073">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccc852903a.mp4?token=heqmXDKLYbG2dDCfa7TBWlow4WYnUINTQvKVJHiqPvxOyjuPBS4uOROnHPWsp-q8nD7AzTkzMpvLShmUfR3y9ukLXgOEGtSC7QqlqGl1IWuRYg-WSzCUcWy4TWm5BcEZWk5eF-HLkmcz3MG0By_zFaPORDocJsL1DcKQvMY6l8HbhEkHWx49bqopez0mB-0PRzQ88ozCH1GqMv7N3tFVw7-KI5OAZRsYaur0TUFNanPmMWde-u83Dm9TUo9agygSLhP2mqEI2A-Svle6cSugtNV5In4fKVdUYjJrzK2C6oHjep8FXMGn_sb-lbBeyLdfauMe_8ommXcktDBg5UaJwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccc852903a.mp4?token=heqmXDKLYbG2dDCfa7TBWlow4WYnUINTQvKVJHiqPvxOyjuPBS4uOROnHPWsp-q8nD7AzTkzMpvLShmUfR3y9ukLXgOEGtSC7QqlqGl1IWuRYg-WSzCUcWy4TWm5BcEZWk5eF-HLkmcz3MG0By_zFaPORDocJsL1DcKQvMY6l8HbhEkHWx49bqopez0mB-0PRzQ88ozCH1GqMv7N3tFVw7-KI5OAZRsYaur0TUFNanPmMWde-u83Dm9TUo9agygSLhP2mqEI2A-Svle6cSugtNV5In4fKVdUYjJrzK2C6oHjep8FXMGn_sb-lbBeyLdfauMe_8ommXcktDBg5UaJwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إطلاق صواريخ إضافية من إيران نحو القواعد الأمريكية</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/89073" target="_blank">📅 23:35 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89072">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">إن عدتم..عدنا.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/89072" target="_blank">📅 23:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89071">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/541d79e411.mp4?token=C-5UuOezacyiqok0Jmd2f3YfSdalzDvVC9g1wyqfTJWBsPC_mGzBafOSJykBK-TvKd808QuDMm5cR20V89jxAVpRe8Ei3Wtv_uNllKiwOdf_eiZ635V52QPk9RCbwC_32fr1byuxwOLPxC2BMIqoafpiGMD3wdi8bH6DbzlH5g0ppFKPvSHHY3PhkgmSfJSjaDWwa8I4zySxP2Rbzj-YUeme5Dgvvs0jUjCNOkQjeeksafjLsNt_Tirw6hBJIWvnQa9H2py1O_V-A1l34OadKF2xvUeqckM8zG7V5XVuRxr4tVa6avGrla_8vwLWbTb38ODZLbpBjWC_dcWvT9bk9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/541d79e411.mp4?token=C-5UuOezacyiqok0Jmd2f3YfSdalzDvVC9g1wyqfTJWBsPC_mGzBafOSJykBK-TvKd808QuDMm5cR20V89jxAVpRe8Ei3Wtv_uNllKiwOdf_eiZ635V52QPk9RCbwC_32fr1byuxwOLPxC2BMIqoafpiGMD3wdi8bH6DbzlH5g0ppFKPvSHHY3PhkgmSfJSjaDWwa8I4zySxP2Rbzj-YUeme5Dgvvs0jUjCNOkQjeeksafjLsNt_Tirw6hBJIWvnQa9H2py1O_V-A1l34OadKF2xvUeqckM8zG7V5XVuRxr4tVa6avGrla_8vwLWbTb38ODZLbpBjWC_dcWvT9bk9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سقوط مباشر لاحد الصواريخ الايرانية في معقل تواجد الاميركي في العقبة.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/89071" target="_blank">📅 23:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89070">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9514f73c43.mp4?token=vldUVkZ7j0I-_QIs8BSwcMBUrUNvP45_Gk_3Yi-dknP4bJmwPnhud7scYPfjpGWsFFJ_UF0V778tiDRtvo_dBpxUNrLVW4N1gCtHIUDFEWhkUjVCPD3M2Wq6Iln5Tl2f1w9V7rX-NzuKp2vu44PXSQo8jeT-3kLk7VYD74FPuYO4xLGAqImsImB9UG5JitqHq_570DhmupQShIJ_YZF6gB93NNQ0pJYn_rLxrIe87uu4fxxrS3_hk1_OTbtfdQbngc3HAt5IjGTNOjOEHSXeghtUQJ1wuNeOWVuDIdRA_XtiR_NlEiIvTjcfwnDa2MLAbu-gcCyQksNI2hjQrQCPwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9514f73c43.mp4?token=vldUVkZ7j0I-_QIs8BSwcMBUrUNvP45_Gk_3Yi-dknP4bJmwPnhud7scYPfjpGWsFFJ_UF0V778tiDRtvo_dBpxUNrLVW4N1gCtHIUDFEWhkUjVCPD3M2Wq6Iln5Tl2f1w9V7rX-NzuKp2vu44PXSQo8jeT-3kLk7VYD74FPuYO4xLGAqImsImB9UG5JitqHq_570DhmupQShIJ_YZF6gB93NNQ0pJYn_rLxrIe87uu4fxxrS3_hk1_OTbtfdQbngc3HAt5IjGTNOjOEHSXeghtUQJ1wuNeOWVuDIdRA_XtiR_NlEiIvTjcfwnDa2MLAbu-gcCyQksNI2hjQrQCPwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من سماء العراق</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/89070" target="_blank">📅 23:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89069">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f504b9e686.mp4?token=b2zTihoaW-J0wwl1s-vB9xe2IVQbFzzOEwoS8n1gnDriZIVCWokVn2FPe7r99SWPYlYvHT3BiOh2MwuFjSS-g3IaH14Pzd4x0_1sBZ-s_eTLBA1SI-N1dw3GgN0GiTG7L6Dlz2L30SMXFVhtH0dxG4JOGuie9XUoBrza6DA03ChzxoPkMmovgo1t9os2wuL60X-yutvuNzDwT0JqWlmVaSwbfIHAcTF28Yx44v334Cz8o7WntMZQHQ2dia6zAcQGW7fcg_aJhwVmjiq2EvRep6r-ntlNeMixC-0R6vehqNCuQ6xfQMxBX-Dx6QIVVpqAs6Sbpc0HKLPtE8SlYW87OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f504b9e686.mp4?token=b2zTihoaW-J0wwl1s-vB9xe2IVQbFzzOEwoS8n1gnDriZIVCWokVn2FPe7r99SWPYlYvHT3BiOh2MwuFjSS-g3IaH14Pzd4x0_1sBZ-s_eTLBA1SI-N1dw3GgN0GiTG7L6Dlz2L30SMXFVhtH0dxG4JOGuie9XUoBrza6DA03ChzxoPkMmovgo1t9os2wuL60X-yutvuNzDwT0JqWlmVaSwbfIHAcTF28Yx44v334Cz8o7WntMZQHQ2dia6zAcQGW7fcg_aJhwVmjiq2EvRep6r-ntlNeMixC-0R6vehqNCuQ6xfQMxBX-Dx6QIVVpqAs6Sbpc0HKLPtE8SlYW87OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد اخرى للصواريخ الايرانية في سماء الاردن.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/89069" target="_blank">📅 23:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89068">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/89068" target="_blank">📅 23:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89067">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69cdf007b2.mp4?token=uvNSR3fXk-XK-TJtd8vXvraIRcxblOrm7NtLShc8NqHSbirYeeIPOs_KoA5LIgMPzKcrYi3BNjBrehqeGEBgIYSlqd7_7urxDPs3bEWu_m59EJ-CJ33URFkfwNX-eknovn8du0sBhyZFRnLVctNxcgNo4a7X9dtZIIkWckHx_aby3fCXAqJVoKlhAQd-4-f3lQI2qvlD70P7qaa5gvKNLcmF1AKlF5uuBD4D0ADU7VfQidKA4Kvwzof7Jky65WKuh43HL5hooLMckY8CThI1Xxk4OBlGO5_fIh70LG7-llyb6pX0y8Xumaq1EnolOBvx8m93PU4w7dMtQ-PfqdGe_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69cdf007b2.mp4?token=uvNSR3fXk-XK-TJtd8vXvraIRcxblOrm7NtLShc8NqHSbirYeeIPOs_KoA5LIgMPzKcrYi3BNjBrehqeGEBgIYSlqd7_7urxDPs3bEWu_m59EJ-CJ33URFkfwNX-eknovn8du0sBhyZFRnLVctNxcgNo4a7X9dtZIIkWckHx_aby3fCXAqJVoKlhAQd-4-f3lQI2qvlD70P7qaa5gvKNLcmF1AKlF5uuBD4D0ADU7VfQidKA4Kvwzof7Jky65WKuh43HL5hooLMckY8CThI1Xxk4OBlGO5_fIh70LG7-llyb6pX0y8Xumaq1EnolOBvx8m93PU4w7dMtQ-PfqdGe_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الصواريخ البالستية تنطلق من مناطق واسعة في إيران</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/89067" target="_blank">📅 23:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89066">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">المنزل الذي تم استهدافه في سيريك من قبل العدو الأمريكي</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/89066" target="_blank">📅 23:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89065">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81644ef76b.mp4?token=GQP1W8sl6uXTLEc2C8le3paY9a4nw19Nlwf8dlsNwDvOOXWNmCVJYCLjJF-22dqK69H_UHh5LUcYKCTfRL1hvT6jHtHGtbdUCb1oYk901y3rEypQAcqxDvebGs0-T59JBSbhGxr7c-qk8ZaiVdbWILNOr0BP0HaIzxipbgJdx7uB9E5HC2PC0agLdY-AiM3xo3jlnYH8p_bzXgxSQEpvvqrxqdLCsgbmEOGwPyR1bfZp5bZXeY9spqeQ6idf8yUGT_I8fIWJQe82zboas-DBV6mHXKtVowO-sqHXZn5ma3pTi8oY04dKUSCvBhYEUmRfWVsPI2gCaLdRLfyDnproZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81644ef76b.mp4?token=GQP1W8sl6uXTLEc2C8le3paY9a4nw19Nlwf8dlsNwDvOOXWNmCVJYCLjJF-22dqK69H_UHh5LUcYKCTfRL1hvT6jHtHGtbdUCb1oYk901y3rEypQAcqxDvebGs0-T59JBSbhGxr7c-qk8ZaiVdbWILNOr0BP0HaIzxipbgJdx7uB9E5HC2PC0agLdY-AiM3xo3jlnYH8p_bzXgxSQEpvvqrxqdLCsgbmEOGwPyR1bfZp5bZXeY9spqeQ6idf8yUGT_I8fIWJQe82zboas-DBV6mHXKtVowO-sqHXZn5ma3pTi8oY04dKUSCvBhYEUmRfWVsPI2gCaLdRLfyDnproZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله اكبر انفجارات تسمع عند مستوطنات المجاورة للقواعد الاميركية في الاردن</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/89065" target="_blank">📅 23:28 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89064">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28f73c571c.mp4?token=cvLbtpsICoPV8OFPgtt8u_qcLhCSs7uwqHYbQ9Ae9HTjQAfrZCOIJitXRMda0jvCXBNQ4u6Deb8mHqdzTuVzrIXTlfY-1aHMILmeFZnbXBFK8UmkBaKd1BUuryhusT_9nJ4cR_No-YxJbuhpZbBfOP1We6pDn5v-_k2tR1f9WkTJ4ND5-oWfZzFx9Bj5S2FEg5ifPkWgaMXY4wdhhy99lNFOCflLUjjNxv3xVXUI3BV_N6JMqicqlXmAVuGi7G22GgCsZnUsE8eT4nHZPRf5dqgYjC4fePJUBjyehQbJ2gCh2OLa6HQQmEPW14W0u26AZFWZ_ICEqtp6ffyYa10g2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28f73c571c.mp4?token=cvLbtpsICoPV8OFPgtt8u_qcLhCSs7uwqHYbQ9Ae9HTjQAfrZCOIJitXRMda0jvCXBNQ4u6Deb8mHqdzTuVzrIXTlfY-1aHMILmeFZnbXBFK8UmkBaKd1BUuryhusT_9nJ4cR_No-YxJbuhpZbBfOP1We6pDn5v-_k2tR1f9WkTJ4ND5-oWfZzFx9Bj5S2FEg5ifPkWgaMXY4wdhhy99lNFOCflLUjjNxv3xVXUI3BV_N6JMqicqlXmAVuGi7G22GgCsZnUsE8eT4nHZPRf5dqgYjC4fePJUBjyehQbJ2gCh2OLa6HQQmEPW14W0u26AZFWZ_ICEqtp6ffyYa10g2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله اكبر انفجارات تسمع عند مستوطنات المجاورة للقواعد الاميركية في الاردن</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/89064" target="_blank">📅 23:28 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89063">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">الله اكبر انفجارات تسمع عند مستوطنات المجاورة للقواعد الاميركية في الاردن</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/89063" target="_blank">📅 23:27 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89062">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea16e5cf1.mp4?token=RIkCkJor-aPTFMBjEyFhmpR4b37JYdUZj6Vt89J2NlacKt2d_lVICuLJAi-zOcrbWu62HYwKBXVlyFa8Qy29PAd5vHDb8YYZ3xJ0rZE0IIwAP67PGFME475sKpIIgfkritM1pJQrpnYXKTglJtBlwFO-0NTXlVlbMcrUOtpjQgygfuO6BIID2IWxeUiIcZABcd4pf1k1wZ-OVexjyP3ITowZjooJR6MItQs_wnHqpbZFN95IHn2TNEuUJ8a8tsHk_s4J4qSyUj50CMnVH8O3Nzql8a6Tif-JpLtZV4JgSSNYjrDgcVWfF6yye4StjIMsOzI2jJuG2dYrtWhIeEfZhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea16e5cf1.mp4?token=RIkCkJor-aPTFMBjEyFhmpR4b37JYdUZj6Vt89J2NlacKt2d_lVICuLJAi-zOcrbWu62HYwKBXVlyFa8Qy29PAd5vHDb8YYZ3xJ0rZE0IIwAP67PGFME475sKpIIgfkritM1pJQrpnYXKTglJtBlwFO-0NTXlVlbMcrUOtpjQgygfuO6BIID2IWxeUiIcZABcd4pf1k1wZ-OVexjyP3ITowZjooJR6MItQs_wnHqpbZFN95IHn2TNEuUJ8a8tsHk_s4J4qSyUj50CMnVH8O3Nzql8a6Tif-JpLtZV4JgSSNYjrDgcVWfF6yye4StjIMsOzI2jJuG2dYrtWhIeEfZhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الصواريخ البالستية تنطلق من مناطق واسعة في إيران</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/89062" target="_blank">📅 23:25 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89061">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1053f11638.mp4?token=Oq0ilvmn1bHmS1WDfrvJAjWoZ-iuekPYyi0DyHypnlYr9hkjGR-08wcN_92ZwBoWC7zK4h_oMKri9hE0Hx3z2dCzY9-TX08SNhIRo6amQhkz1WCE-GD-d8fGXAUCKlHpPUHx_iMOb_sd6TZ4Zydtia9fwjKgeg7mXNEawJR5uRtNebIjtEO5qL1zuXMnQl4SBM4AD1NuYeaK7xSXSGU2MV5ZUehNZgUaq5_1FiLAzn8yrO5I98iev9JEFNUlEHbBppxHXVkhKW32zoZKmsLg61ppoem2W_PbiK9cBTwRZbhoEtesRpGak-McSeLnpR2voXB15ugveqbOmypaQLVqwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1053f11638.mp4?token=Oq0ilvmn1bHmS1WDfrvJAjWoZ-iuekPYyi0DyHypnlYr9hkjGR-08wcN_92ZwBoWC7zK4h_oMKri9hE0Hx3z2dCzY9-TX08SNhIRo6amQhkz1WCE-GD-d8fGXAUCKlHpPUHx_iMOb_sd6TZ4Zydtia9fwjKgeg7mXNEawJR5uRtNebIjtEO5qL1zuXMnQl4SBM4AD1NuYeaK7xSXSGU2MV5ZUehNZgUaq5_1FiLAzn8yrO5I98iev9JEFNUlEHbBppxHXVkhKW32zoZKmsLg61ppoem2W_PbiK9cBTwRZbhoEtesRpGak-McSeLnpR2voXB15ugveqbOmypaQLVqwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوي انفجارين في مدينة جابهار جنوب شرق إيران</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/89061" target="_blank">📅 23:25 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89060">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">انفجارات عنيفة تهز القواعد الأمريكية في الأردن</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/89060" target="_blank">📅 23:24 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89058">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9953fe1fa7.mp4?token=sUPWdVPEr88F--_BNOxWbp6A-h3cJmAXyF24Zdqh8pG_5DMLOhJdSLUDNWjzr7IjG32zDzanDUVxDeTKTRipOs636ZL1YCgaXXsTgdJFUXkAoTbTlFKUOydqgx600_Aty3Q-Ef-8Bx7C4sPaYgLckKWmVOE8Sy4pdyNAq_ASOpf-rgyBB5eWE2CKPfnrrMpDP6mfIQrEDO9F7JROlLeTek_R8PqO4KDyOAd6qWj0hyKYP309jgKIpeOQdPLrOK9NzmCG8ODIgp7l8S9V8qx1FQvFWhuv0C9GMq3-POYueBC6vv8xq9EYw94K0WiNoY_hGDt68pOjZYF3cin6cG8rKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9953fe1fa7.mp4?token=sUPWdVPEr88F--_BNOxWbp6A-h3cJmAXyF24Zdqh8pG_5DMLOhJdSLUDNWjzr7IjG32zDzanDUVxDeTKTRipOs636ZL1YCgaXXsTgdJFUXkAoTbTlFKUOydqgx600_Aty3Q-Ef-8Bx7C4sPaYgLckKWmVOE8Sy4pdyNAq_ASOpf-rgyBB5eWE2CKPfnrrMpDP6mfIQrEDO9F7JROlLeTek_R8PqO4KDyOAd6qWj0hyKYP309jgKIpeOQdPLrOK9NzmCG8ODIgp7l8S9V8qx1FQvFWhuv0C9GMq3-POYueBC6vv8xq9EYw94K0WiNoY_hGDt68pOjZYF3cin6cG8rKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله اكبر
تستمر اطلاق الصواريخ الايرانية من عدة مناطق في ايران نحو القواعد الاميركية بالمنطقة.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/89058" target="_blank">📅 23:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89057">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">طهران تفعيل الدفاعات الجوية</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/89057" target="_blank">📅 23:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89056">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">طهران تفعيل الدفاعات الجوية</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/89056" target="_blank">📅 23:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89054">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kaRq0i_8Q-Q37kgWVSbGKLq39sl9F6lRZbKhnLb29erm51flgDZLkQSbdsroSS79vZXUMEGR20iIRvI0YnTb_Gh63K1fDY21rHXfzqQMAD7S4RgJO5k4nw0x-QmjQXg3dE4Ca1su2GqlXvxLss0dBSKLnb8OQ8J_9wCXvk7C5-k4cWl5adFCJh0-Sh42PzW8tcqqLUFaDCcZYcHnWhQvXC5nJ9YoFwtsuUnZ0Bvo32NtJfBR-sLNnDRy5Z8PYpR8y4jhn_EyzNPvkVoPow8RFaBWJGsZis001_l8Y0XMQPE5w6c4llNBVGWxqExFZT4uMJYY2uc4qvMf0iRGGRSQIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gdqdks1uthnlYpBYmKkn0AKn0ClIXlFf0dZfxtSFSBgUmqnTnvnCpyseauYtNLsd4B4oTEjn85oGnPuirbd1vQa1X425PnPJ-Pv8ysJ06u_EtBH8_tXrNzwkS-qrtjc-HGQb5-t6mDMyJQj7t-LqH59qRngEltOBkbTRDyEHvANRZyzOFbsQFBnhfsSQPzp94n86Umj9kmZcSUTlN1IfGt_xY6wEKRdJ8qOeIK_h8Rc_CZ6Fq2SFEZcZtBGliDH4aEfEZDtIcJ8tYgXlOACN7iXM99vBG0DnYVDEun-w4Ga8xSh0RxAU1ILZJmLkp7OYVXapcOS5jkfgmuUcxvfVWA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من العدوان الأمريكي على سيريك جنوبي إيران</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/89054" target="_blank">📅 23:22 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89053">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">متحدث باسم الجيش الإيراني: لا شك أن الانتقام من الجرائم والاعتداءات التي ارتكبها العدو سيأتي قريبًا، وسيكون سريعًا وقويًا وشاملاً.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/89053" target="_blank">📅 23:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89050">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a805be5241.mp4?token=oZm6ZpbtG73fvyIAFuZI4sLSQFztpHCf0Q604mLu3R5N5Ki5DxPNFVGLKhIGDXgLSjMLsNi7oATJN6yZ3YEJ6Ak4M-ecVj1_E_pYapo6HAticVllF-Cf7z3-HIO1KWSDmzU3deqN9zFf5jg7IoRAyRrC4wxUfeRzejpy9ktRv1oNpC2nIPwMTOHFGAmWsBFAbsGtjMnyV_v7LtGUqyHn0y1M4gGvb0wP_bwGtCTqjv_bjC6zSNWz0I-km9qpZODAHp0wOyitZT3FDnEJqj6PcF6ZH9WkOayzLfi7jDqXmxOB5GVOLlUSEzVVf7xdecu0BUtIITBTITEDtT7hEJVVIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a805be5241.mp4?token=oZm6ZpbtG73fvyIAFuZI4sLSQFztpHCf0Q604mLu3R5N5Ki5DxPNFVGLKhIGDXgLSjMLsNi7oATJN6yZ3YEJ6Ak4M-ecVj1_E_pYapo6HAticVllF-Cf7z3-HIO1KWSDmzU3deqN9zFf5jg7IoRAyRrC4wxUfeRzejpy9ktRv1oNpC2nIPwMTOHFGAmWsBFAbsGtjMnyV_v7LtGUqyHn0y1M4gGvb0wP_bwGtCTqjv_bjC6zSNWz0I-km9qpZODAHp0wOyitZT3FDnEJqj6PcF6ZH9WkOayzLfi7jDqXmxOB5GVOLlUSEzVVf7xdecu0BUtIITBTITEDtT7hEJVVIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صاروخ أخر ينطلق نحو القوات الامريكية في المنطقة</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/89050" target="_blank">📅 23:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89049">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">الله أكبر
الدفاعات الجوية الإيرانية تشتبك مع الاجسام المعادية في سماء كرمانشاه</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/89049" target="_blank">📅 23:19 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89048">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a139d16973.mp4?token=icQAlwyCnYpgSPUqNiFXEQc6WZUl0RIU6aNXkbnfMn93aSmXwySSCtl2sPRnGphydAgx_LhV3ay_w2zF6qOY3dUsaDOLesx7UuZxSjTiXR2s8ImfLDzvuamplMhDPH-fQ3hKXaBQ5xI71L3PDaIGp9-BTqa3FbwI502qkqv5YvhEqJP9jzpB5FJgvaC1287_vNqrAaRoj0LqMqnhZnb_BO_PG5jk6A09DWyTxHBVfzREtbGxZoahX7RsBZqPY2u9mBYP9qCTn9wKd9ga-Iwa1sz1_oEnk2Y_LRjgqJYKVcxet4JETpqUTn8bUdbUo06DrDMwIkhf73vku3yqG3fgTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a139d16973.mp4?token=icQAlwyCnYpgSPUqNiFXEQc6WZUl0RIU6aNXkbnfMn93aSmXwySSCtl2sPRnGphydAgx_LhV3ay_w2zF6qOY3dUsaDOLesx7UuZxSjTiXR2s8ImfLDzvuamplMhDPH-fQ3hKXaBQ5xI71L3PDaIGp9-BTqa3FbwI502qkqv5YvhEqJP9jzpB5FJgvaC1287_vNqrAaRoj0LqMqnhZnb_BO_PG5jk6A09DWyTxHBVfzREtbGxZoahX7RsBZqPY2u9mBYP9qCTn9wKd9ga-Iwa1sz1_oEnk2Y_LRjgqJYKVcxet4JETpqUTn8bUdbUo06DrDMwIkhf73vku3yqG3fgTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صاروخ أخر ينطلق نحو القوات الامريكية في المنطقة</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/89048" target="_blank">📅 23:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89045">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9fcd9c7a2.mp4?token=c8c-sKBOlz_F2vUERPUxtqqvZC3ytNU-fIn7mw8-Y16Z-7CNavjoBd3eD4G4hgqhk0Illq4wZW_7jfYqzfSmOOThWndYIea8nfClUe7A9o-upF2bcYNstbfFMNINIJkngfJZGiathiLouYmgXs61A65a6XQD8nIVYUG7UlXkLzOAMWJS7jnLq9OV_5dd_FuT50gUombJhEiFrBnY6JGAm7YDfZukoZcQB1uhcGXSzFCMKCiQ3A0eo4yGVzNZemrbQy8GE_t7E1a1loArCdubNu_aH9QLkR9SVgKuoBDz-SxIaR0b5ml7Td5MZdC9t71Q70mIWyitZNh1JZ9vg-dFhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9fcd9c7a2.mp4?token=c8c-sKBOlz_F2vUERPUxtqqvZC3ytNU-fIn7mw8-Y16Z-7CNavjoBd3eD4G4hgqhk0Illq4wZW_7jfYqzfSmOOThWndYIea8nfClUe7A9o-upF2bcYNstbfFMNINIJkngfJZGiathiLouYmgXs61A65a6XQD8nIVYUG7UlXkLzOAMWJS7jnLq9OV_5dd_FuT50gUombJhEiFrBnY6JGAm7YDfZukoZcQB1uhcGXSzFCMKCiQ3A0eo4yGVzNZemrbQy8GE_t7E1a1loArCdubNu_aH9QLkR9SVgKuoBDz-SxIaR0b5ml7Td5MZdC9t71Q70mIWyitZNh1JZ9vg-dFhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اطلاقات جديدة من إيران نحو القواعد الأمريكية</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/89045" target="_blank">📅 23:17 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89044">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/89044" target="_blank">📅 23:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89043">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/89043" target="_blank">📅 23:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89042">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be141a5175.mp4?token=L_06fouSmHmM4i9lFGeNcPKniFkeOAiZlwKKRMRsenH_bTxmKqFQQQ-k2i9M_1-q_TEccHBchgP0-FfnO9mqJiynIkdUe7KHE1CYCf9-bUN9FCEJ4skeQfq1DP3lKIxfd-5jXs47U6TfQ7NzWlvAxL6TryFMMEl1n_wt3nEAoheYzng54RrK-XJfJEwajTiPULFOs303C2K_mUzAq7wtHmLEAO_qDFFhiC0me7FGRwqUOn4-5alBV9lZxk_QNtuDG7vv4GwU3OcCFToIxRgzLtLPagYv8MYcrhzYu-NGae-8aruQHkfMRkxle5HDtPkuh0BSVqRzcDpmzHmM2HBQsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be141a5175.mp4?token=L_06fouSmHmM4i9lFGeNcPKniFkeOAiZlwKKRMRsenH_bTxmKqFQQQ-k2i9M_1-q_TEccHBchgP0-FfnO9mqJiynIkdUe7KHE1CYCf9-bUN9FCEJ4skeQfq1DP3lKIxfd-5jXs47U6TfQ7NzWlvAxL6TryFMMEl1n_wt3nEAoheYzng54RrK-XJfJEwajTiPULFOs303C2K_mUzAq7wtHmLEAO_qDFFhiC0me7FGRwqUOn4-5alBV9lZxk_QNtuDG7vv4GwU3OcCFToIxRgzLtLPagYv8MYcrhzYu-NGae-8aruQHkfMRkxle5HDtPkuh0BSVqRzcDpmzHmM2HBQsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موجات الصواريخ لاتتوقف</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/89042" target="_blank">📅 23:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89041">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ed5024135.mp4?token=t2Q5SVet2pxrLxtnKxBez-NAv94KZ2P6pOWWGkdp3E81xUh9ghvF-NoUXcYKLhKK5ZQpj_prNZiFHp8Fg1hOds-Lcdc5-BO23vPaS5gBQ2p-XE8SVrJPsjw_5h6l4Cg-PO2xhYJKdg-l0c5RtSPadppQnOHmnXsq7d9I4We7boJN4r8Zgs7DQzJveYyeg6fIrWo8K2H0dniHF9lHb8vZ5XWbXy4SEfAzlP5UJIeyQJcctRh4oTdpcBPmMPwrCG7EsGt1X8LsVKL4cZYaa8fz2SLuadCFS4NaFWcgHT3ZZYiKwyK_MkhtBAdjovA0hYOUNTLrSUKHu4k90ERalYexYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ed5024135.mp4?token=t2Q5SVet2pxrLxtnKxBez-NAv94KZ2P6pOWWGkdp3E81xUh9ghvF-NoUXcYKLhKK5ZQpj_prNZiFHp8Fg1hOds-Lcdc5-BO23vPaS5gBQ2p-XE8SVrJPsjw_5h6l4Cg-PO2xhYJKdg-l0c5RtSPadppQnOHmnXsq7d9I4We7boJN4r8Zgs7DQzJveYyeg6fIrWo8K2H0dniHF9lHb8vZ5XWbXy4SEfAzlP5UJIeyQJcctRh4oTdpcBPmMPwrCG7EsGt1X8LsVKL4cZYaa8fz2SLuadCFS4NaFWcgHT3ZZYiKwyK_MkhtBAdjovA0hYOUNTLrSUKHu4k90ERalYexYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">2 شهداء وإصابة أخرين كحصيلة أولية جراء عدوان أمريكي طال منزل في منطقة سكنية أثناء إقامة حفل زفاف بمدينة سيريك جنوبي إيران.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/89041" target="_blank">📅 23:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89040">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a56dee0dee.mp4?token=ZyXv8N0BhlmHDmAj6U3XLG2RgGkY-2S8KTaJHpI5jSmysg7bViQAjzHUGA66eois4B1CcsgchiDqU87l2keOo1lqomlNWmtUf4CBUkbw1Cmsma5_9L3NqfcKNs9YoDI_5uP_KNC1GX3YODRJmqoH2R2dBy1Vha40eyXv1tiYMJnu5kgqsXcnypw-61eO5PM90EqDiWZ_27cxDDhx4AXGgqtFapw-Q1fETejPvX0wB7QO891kXCY7rlHbT1-RT_lOQGYOgFGjW_ytN3v0IvnXZ4r7_rydl2jTjY-VyqNgYBLM-Y6KkY4BpD1h7YUgSJtJ70oxvnq4XQTYtNmLHtJYxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a56dee0dee.mp4?token=ZyXv8N0BhlmHDmAj6U3XLG2RgGkY-2S8KTaJHpI5jSmysg7bViQAjzHUGA66eois4B1CcsgchiDqU87l2keOo1lqomlNWmtUf4CBUkbw1Cmsma5_9L3NqfcKNs9YoDI_5uP_KNC1GX3YODRJmqoH2R2dBy1Vha40eyXv1tiYMJnu5kgqsXcnypw-61eO5PM90EqDiWZ_27cxDDhx4AXGgqtFapw-Q1fETejPvX0wB7QO891kXCY7rlHbT1-RT_lOQGYOgFGjW_ytN3v0IvnXZ4r7_rydl2jTjY-VyqNgYBLM-Y6KkY4BpD1h7YUgSJtJ70oxvnq4XQTYtNmLHtJYxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله أكبر  موجة جديدة تنطلق</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/89040" target="_blank">📅 23:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89039">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e502f1620e.mp4?token=XWM2YVegt-_HtJnKnzKipwzqOXV4TNrhkwbPanRBBpIQzQ-R2bJyRkxAOe83zV6wJLaVyxJk18Eg8z71UG23C960KeyHxI0nP7qo0f-94JqV46QBTxIR59fxXA3p4kM8aduie182gt0G8fz3YdHMjSt_ptvHXZ0I3VIC-2K5GjnQGrN_AhxE4NAP7WKsJaUOsru86LLHcrp2UZbdPBtJxpPtR48UQRwNP9uXd_x98dTkZrlLrxtCbsFYhFP7yPnqpaNcTaNF9IR8A6a_upAqyDEyjfOwDO00aUGyWJ3g2XltDJEwGS862RThr9cycKI86yvu7zbos9LcSLSjnJdf_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e502f1620e.mp4?token=XWM2YVegt-_HtJnKnzKipwzqOXV4TNrhkwbPanRBBpIQzQ-R2bJyRkxAOe83zV6wJLaVyxJk18Eg8z71UG23C960KeyHxI0nP7qo0f-94JqV46QBTxIR59fxXA3p4kM8aduie182gt0G8fz3YdHMjSt_ptvHXZ0I3VIC-2K5GjnQGrN_AhxE4NAP7WKsJaUOsru86LLHcrp2UZbdPBtJxpPtR48UQRwNP9uXd_x98dTkZrlLrxtCbsFYhFP7yPnqpaNcTaNF9IR8A6a_upAqyDEyjfOwDO00aUGyWJ3g2XltDJEwGS862RThr9cycKI86yvu7zbos9LcSLSjnJdf_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله أكبر  موجة جديدة تنطلق</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/89039" target="_blank">📅 23:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89038">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">دوي انفجار في كرمانشاه غربي إيران</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/89038" target="_blank">📅 23:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89037">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">الله أكبر
موجة جديدة تنطلق</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/89037" target="_blank">📅 23:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89036">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd5293feb2.mp4?token=vfXSeJ5LtMU_gGjlRiBkwNlesCIU-YIfFalRdJzWCROKcyRh6emZ0LvAX2799BBXW0sBD3lYbbguIYOFEEusyZMGludYET-YOdhP9ClvPAZdH4C4jY3ZRNBOzby0yt6TbTSbC6HcMAve-lnzuow1dwuWVls3vy8n0L0DVw7gPH7Rl0_yJBYq3h5uQMg-fC86DtpCzsPuVnXu-_6OR0UhK67DKEltl9y6D1zf_IWl8CADdYISXJO4Vip3T7pR8DBzbMv0_P8VyhuLK4gTWv73GbvNgtQTAexfkQjIuxbX7WqdAOg8e7wpk6XsDWt0Cq1a0ehEyqXrWM5av5x-l1PCQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd5293feb2.mp4?token=vfXSeJ5LtMU_gGjlRiBkwNlesCIU-YIfFalRdJzWCROKcyRh6emZ0LvAX2799BBXW0sBD3lYbbguIYOFEEusyZMGludYET-YOdhP9ClvPAZdH4C4jY3ZRNBOzby0yt6TbTSbC6HcMAve-lnzuow1dwuWVls3vy8n0L0DVw7gPH7Rl0_yJBYq3h5uQMg-fC86DtpCzsPuVnXu-_6OR0UhK67DKEltl9y6D1zf_IWl8CADdYISXJO4Vip3T7pR8DBzbMv0_P8VyhuLK4gTWv73GbvNgtQTAexfkQjIuxbX7WqdAOg8e7wpk6XsDWt0Cq1a0ehEyqXrWM5av5x-l1PCQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله أكبر  اصابة مباشرة في القاعدة الامريكية بالأردن</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/89036" target="_blank">📅 23:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89035">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">عدوان أمريكي على نقاط في محيط مدينة الأهواز جنوبي إيران</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/89035" target="_blank">📅 23:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89034">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38dce6ec6c.mp4?token=PXpzS3IDaMhoGutOJBgfGsFJTjtRvvsgzUdwvrwqpmleEQTz-omk9YVmFbOcouKOYdmrHzX0Xk9iJ1ZQXMKuG-v00B7AqktAYBA8wnOhhcOjkXO47qIi9l3DEE8Xg0r9JKRrHc1vO8UPnaJlvwAuHqia87XjrjrDRR5KwUZcZtspgXD0MWdX4P7Szv129txuqdEu7GAMm1e8bnAMq5tkiXLjy70gdXCrsc38-K8mExkEh0-VgHrjIQrIHzVwOD4-ZDsBgrIXHr8yGm-71o6yRtoIkPueE2LE8Oo3eQ-_pdJC7Cpmgzc-FcRvrhsP7dWx0MnStbd_MAoAhylFoMsGLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38dce6ec6c.mp4?token=PXpzS3IDaMhoGutOJBgfGsFJTjtRvvsgzUdwvrwqpmleEQTz-omk9YVmFbOcouKOYdmrHzX0Xk9iJ1ZQXMKuG-v00B7AqktAYBA8wnOhhcOjkXO47qIi9l3DEE8Xg0r9JKRrHc1vO8UPnaJlvwAuHqia87XjrjrDRR5KwUZcZtspgXD0MWdX4P7Szv129txuqdEu7GAMm1e8bnAMq5tkiXLjy70gdXCrsc38-K8mExkEh0-VgHrjIQrIHzVwOD4-ZDsBgrIXHr8yGm-71o6yRtoIkPueE2LE8Oo3eQ-_pdJC7Cpmgzc-FcRvrhsP7dWx0MnStbd_MAoAhylFoMsGLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الدفاعات الجوية الإيرانية تتمكن من إستهداف جسم معادي في سماء البلاد.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/89034" target="_blank">📅 23:03 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89033">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">القواعد الامريكية في الاردن تحت مرمى صواريخ الجمهورية الإسلامية.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/89033" target="_blank">📅 23:02 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89032">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">انفجارات تهز الاردن</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/89032" target="_blank">📅 23:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89031">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/89031" target="_blank">📅 23:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89030">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/89030" target="_blank">📅 23:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89028">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b7b249727.mp4?token=YC9oOiJktxVq5sPLGrIBhEzcdwapX09bqAzRWD127fvj7v4WrEHIQD5hqQ2HryTIdEF9cojEhTzzvGAgWhm8en4ka5JDEKLaVhLt4AO-u9tFOIpcRg8kp1zy8fH3PPUSw6hHkNt9Nn1XxaI5mKXqMqI0vzqFwoubG-Rte781mPe_Vlh1fb95GHHTjazklyszjED-Tkp2Z62Zih76IV3ef1reMfh85v4EQFLzzUUpchmTXCnei_N9eGuyz0i3BosUg-fcHNIszWAX5Ks56k_Fb-I_kyf_EM27o2Rti8BSg3zFW36pj5-H4rYchEG5Sj7c8bNP19XTnpEGHW1wDKJJig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b7b249727.mp4?token=YC9oOiJktxVq5sPLGrIBhEzcdwapX09bqAzRWD127fvj7v4WrEHIQD5hqQ2HryTIdEF9cojEhTzzvGAgWhm8en4ka5JDEKLaVhLt4AO-u9tFOIpcRg8kp1zy8fH3PPUSw6hHkNt9Nn1XxaI5mKXqMqI0vzqFwoubG-Rte781mPe_Vlh1fb95GHHTjazklyszjED-Tkp2Z62Zih76IV3ef1reMfh85v4EQFLzzUUpchmTXCnei_N9eGuyz0i3BosUg-fcHNIszWAX5Ks56k_Fb-I_kyf_EM27o2Rti8BSg3zFW36pj5-H4rYchEG5Sj7c8bNP19XTnpEGHW1wDKJJig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اطلاق صواريخ من إيران نحو الاهداف الأمريكية في المنطقة</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/89028" target="_blank">📅 22:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89027">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/89027" target="_blank">📅 22:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89026">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/89026" target="_blank">📅 22:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89025">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">اطلاق صواريخ من إيران نحو الاهداف الأمريكية في المنطقة</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/89025" target="_blank">📅 22:56 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89024">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇺🇸
🇮🇷
في جريمة حرب أمريكية.. إرتقاء شهداء وإصابات في صفوف المدنيين.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/89024" target="_blank">📅 22:49 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89023">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">الله أكبر
🔻
تأكيدا لمانشرته نايا.. الدفاعات الجوية الإيرانية تتمكن من إسقاط مسيرة أمريكية من طراز MQ9 في سماء مدينة خمين.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/89023" target="_blank">📅 22:41 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89022">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">الله أكبر
🔻
تأكيدا لمانشرته نايا.. الدفاعات الجوية الإيرانية تتمكن من إسقاط مسيرة أمريكية من طراز MQ9 في سماء مدينة خمين.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/89022" target="_blank">📅 22:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89021">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">مصدر إيراني: لا وجود لعدوان على مدينتي كنغان وجم جنوبي إيران.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/89021" target="_blank">📅 22:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89020">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">دوي انفجارين في مدينة جابهار جنوب شرق إيران</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/89020" target="_blank">📅 22:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89019">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">الله أكبر
تفعيل الدفاعات الجوية في سماء جزيرة قشم</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/89019" target="_blank">📅 22:30 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89018">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">الدفاعات الجوية الإيرانية تتمكن من إستهداف جسم معادي في سماء البلاد.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/89018" target="_blank">📅 22:28 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89017">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔻
مصدر إيراني: حفل زفاف في مدينة سيريك استُهدف بشظايا هجوم وحشي من العدو الأمريكي.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/89017" target="_blank">📅 22:22 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89016">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔻
مصدر إيراني:
حفل زفاف في مدينة سيريك استُهدف بشظايا هجوم وحشي من العدو الأمريكي.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/89016" target="_blank">📅 22:19 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89015">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">عدوان أمريكي على مطار مدينة جيرفت بمحافظة كرمان الإيرانية.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/89015" target="_blank">📅 22:19 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89014">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">انفجارات في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/89014" target="_blank">📅 22:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89013">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">تتجدد الانفجارات في جزيرة قشم.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/89013" target="_blank">📅 22:11 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89012">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنایا به فارسی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99659660c5.mp4?token=Bk2cPHPrdRnwuDhNdJixy7r5v2PR45GzR-MqQiVUefpinBSooQugLV1_E7xAeZ1ET-0v0q7_ia01E70JSfJTCmqxGQPF8RfQ19vhEOpsUeI6JS3Ib1cP7OCwdzBbQ6Z6L8Mok5vMkX4KnICogXNeM5d-nTYCPudkcMlqgKOhS5eUlF24wztxYYl1Tr5Yxdzpu5nARqRmlEJ-0h06WWrQXZjed-FWu9fF8pnV-lwLEqJ7MICGFAml2N-pkywFpca9xGzakkyD_Vgpp9SUkZczrd6OLL73mttg9qb03YDVsPmsmK-YSsS3efAcv9LcrQW874fuV3kZ9Pk0tuToBSLMGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99659660c5.mp4?token=Bk2cPHPrdRnwuDhNdJixy7r5v2PR45GzR-MqQiVUefpinBSooQugLV1_E7xAeZ1ET-0v0q7_ia01E70JSfJTCmqxGQPF8RfQ19vhEOpsUeI6JS3Ib1cP7OCwdzBbQ6Z6L8Mok5vMkX4KnICogXNeM5d-nTYCPudkcMlqgKOhS5eUlF24wztxYYl1Tr5Yxdzpu5nARqRmlEJ-0h06WWrQXZjed-FWu9fF8pnV-lwLEqJ7MICGFAml2N-pkywFpca9xGzakkyD_Vgpp9SUkZczrd6OLL73mttg9qb03YDVsPmsmK-YSsS3efAcv9LcrQW874fuV3kZ9Pk0tuToBSLMGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴
زمان شکار است ..
@Naya_Presd</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/89012" target="_blank">📅 22:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89011">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af4a346104.mp4?token=D3TiKIsMiF1o74Qj-KWoMZ-wKmChHrGoc_D9b4bbK4_SYcEU9iiEEiG8q5z4s5y59XVV5luLA9KEGWS70knibsK0gjrmHm3A9EQEZ6jZKgo60difaxEsmTx2RqUllaHytZdUU_w9FNYuNFGTHt6BfrdKG4ev3zBANDLYSlVRSbZ0DZ7BPldSfnhVfZe-ASpGt4gcpBwVMHmuE2Nd88oqtfOK4lEMh197ObfSacQXSRGrUNBUDmRLJiAdN5y_TmdmjO3UaBLVKxygQPoQfyy70Tf6gCgGhocx1_CHn-ET08rv_0pMY0wzCe_qu4IGExihXwUvOKTyrnPjyS88bAITSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af4a346104.mp4?token=D3TiKIsMiF1o74Qj-KWoMZ-wKmChHrGoc_D9b4bbK4_SYcEU9iiEEiG8q5z4s5y59XVV5luLA9KEGWS70knibsK0gjrmHm3A9EQEZ6jZKgo60difaxEsmTx2RqUllaHytZdUU_w9FNYuNFGTHt6BfrdKG4ev3zBANDLYSlVRSbZ0DZ7BPldSfnhVfZe-ASpGt4gcpBwVMHmuE2Nd88oqtfOK4lEMh197ObfSacQXSRGrUNBUDmRLJiAdN5y_TmdmjO3UaBLVKxygQPoQfyy70Tf6gCgGhocx1_CHn-ET08rv_0pMY0wzCe_qu4IGExihXwUvOKTyrnPjyS88bAITSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موجة صاروخية جديدة تنطلق من إيران</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/89011" target="_blank">📅 22:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89010">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">موجة صاروخية جديدة تنطلق من إيران</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/89010" target="_blank">📅 22:07 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89009">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/89009" target="_blank">📅 22:07 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89008">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ترامب:  إيران لن تبقى قائمة إن ردت على الضربات الأمريكية الأخيرة.  إذا ردت إيران سنضربها بقوة أشد بكثير.  ضربة اليوم لإيران كبيرة جدا وإن تكرر الأمر ستمحى كليا.  الاتفاق مع الإيرانيين لا يساوي الورق الذي كتب عليه ومنحناهم فرصا كثيرة.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/89008" target="_blank">📅 21:58 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89007">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b224f120e8.mp4?token=UcO3MzzQocqEsetQliyRhh-SlWQc96bssZsrAhnusSbvCEJ0b9vJIAT5s-r9BSrRJoFSrIeTf3Lz7F7iib-ZCXE-iV__XHVXwIcYj023Kdp08_Gd4slo-DJhGgi-R0As-egIgx59poG91p6rgkbnwBOuCw7FFBuoazks0qZYh5AXrnCDuQfBICzHGbznxc6nm4sA5wUVlx0Paw3RsXJukUjDC6WF0pZq6HiFInVGU-6l2F0toh0vMtbeNzSEiJdMvWkQpih3nW_2jeE0pxVWyPdiVv1cQvMmtxeXIIESRywS875LE3SrAJRTznv3Ida0TsczperO4iKNBLXU3sN6Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b224f120e8.mp4?token=UcO3MzzQocqEsetQliyRhh-SlWQc96bssZsrAhnusSbvCEJ0b9vJIAT5s-r9BSrRJoFSrIeTf3Lz7F7iib-ZCXE-iV__XHVXwIcYj023Kdp08_Gd4slo-DJhGgi-R0As-egIgx59poG91p6rgkbnwBOuCw7FFBuoazks0qZYh5AXrnCDuQfBICzHGbznxc6nm4sA5wUVlx0Paw3RsXJukUjDC6WF0pZq6HiFInVGU-6l2F0toh0vMtbeNzSEiJdMvWkQpih3nW_2jeE0pxVWyPdiVv1cQvMmtxeXIIESRywS875LE3SrAJRTznv3Ida0TsczperO4iKNBLXU3sN6Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصدر إيراني: الرد الإيراني بدء</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/89007" target="_blank">📅 21:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89006">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/89006" target="_blank">📅 21:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89005">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/89005" target="_blank">📅 21:57 · 10 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
