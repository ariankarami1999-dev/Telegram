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
<img src="https://cdn4.telesco.pe/file/i871apWkffRI_T15boix7iBelk-uQC8wQk7xfuk8hbA06nZiHpYC5eBI391lrpgdQtRMcsfmSdjrLHUu3DPzlPMxdgEkOlCH8wOSpBXoORbcCNEEzQkuEYSef0fQp-rUeazATDWCCnEkEUYDbX_mnurg2AqhOd8vnVbSyuMkAl51LRxZPbKLE_ECK3aLzpIN4kROSNeKqFy_bV-fwxph1yvMwdnS0TAMAnhpsV22V-X9qEiTcURTpAa9Th3cBc9mWYLAojALwsIReDNDEdaKfq41WHc74x4jN--zgqU4aU7vCFobrRDUogv361juSaq40T4JcskFZ_wV12ObN0yGuw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 169K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-25 12:08:39</div>
<hr>

<div class="tg-post" id="msg-68250">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OlO0y1BmTZlmKQHlE1PGh47EtMZTwinyZEpmWw_aCDqNEv2Z0EsOIdfkNg6nIrmBp8B80xwcus7a5SmE8Za33zu9hFVO6XcdVLRORTLfeqkX21yaRe2Pp3IaxEAOOy3tcm4WC5-JJOVV797hTm9DsTZkW-LSX4SiDnbbJ2aFyLpvAk5RxTQ3tMVxcxd7Q2kWJwbo6rU99HVuHf3F8ITQWhcG4mI2zHrU2Tj8yZm7QEYw0MU9bME5t8qs7265MS66i-rcvL_DL9NAnaTDZBuzjaLiZTLvSOlaQWak1m14jYjMdBDRCm5LAXdcj1y1fgftEePnjDW7nXK385rjiv6CVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ترامپ:
ایران اجازه داده یک شهروند آمریکایی که در دسامبر ۲۰۲۴ و در دوران ریاست‌جمهوری جو بایدن بازداشت شده بود، از کشور خارج شود.
این زن اکنون در سلامت کامل و شرایطی مناسب خارج از ایران قرار دارد. آمریکا از این اقدام مبتنی بر حسن نیت ایران قدردانی می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/news_hut/68250" target="_blank">📅 11:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68249">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00bc13721f.mp4?token=nTjCUxwO1M8kkDwqZCkbouyunaNn_-U9PfFj8jeumDxXwMzwTwSCo48YnFSOAMZUrmnIECCNw83-kGCEoSIZU5H_7gsdjJR9gfmsyY-aRczK4O140OgBd0r9zJ212rW9I3oA3kLqYm0MqItUvo7gSH9YCd9vkijJsoJMXYhjJsEfWy_2uiwTq1R0gDgsdY78TGRn4ivXkIAyb1DtlofHCD7m0znjT_DpGXm1GbmPmRst7dwCy4MzyYhzQPfHbNgakTQfCjwGaTBgwOgGz14mxhok3KfDcATiqmLwJAwOMrW0RUJTwPKbEVu4GGb-GJ9efS8fwPAnJZbz-RSui_q4qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00bc13721f.mp4?token=nTjCUxwO1M8kkDwqZCkbouyunaNn_-U9PfFj8jeumDxXwMzwTwSCo48YnFSOAMZUrmnIECCNw83-kGCEoSIZU5H_7gsdjJR9gfmsyY-aRczK4O140OgBd0r9zJ212rW9I3oA3kLqYm0MqItUvo7gSH9YCd9vkijJsoJMXYhjJsEfWy_2uiwTq1R0gDgsdY78TGRn4ivXkIAyb1DtlofHCD7m0znjT_DpGXm1GbmPmRst7dwCy4MzyYhzQPfHbNgakTQfCjwGaTBgwOgGz14mxhok3KfDcATiqmLwJAwOMrW0RUJTwPKbEVu4GGb-GJ9efS8fwPAnJZbz-RSui_q4qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
پهباد شاهد در حال رفتن به سمت پایگاه های آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/news_hut/68249" target="_blank">📅 11:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68248">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b8221101a.mp4?token=USAzWNXmfW-Tg4_-aAqTAEyeo2Z9tQycbXDBDoVN9PLvKaf5dngueVmva82FhMvr7NnCs8DDpo8cMsKaedfnop03ANZyrszP2O8qP6CxEINm0D3Dct2sRnufrZgQ6u9XXCZVxnwiIx11Pqna6R4fug1dg2OmUuuxc-AGP-xXtlo0tBausAPNe3nPe3XQMU9eWE0rj_Nak082iYjezpSqEIK8Kh3ppXqnXqIYhwM1VFLnhcpsc3sFt20-F9NnvO8e7YfIc6JioIEKGI0fo2fK6ewJO0kAbx-9Nm_CyxzIXXHDV4XnxCqrzk17VwT1VUq5IoQwwfCZzC_ZfFAeQNmKtqnfHO3hotQ8GhgdCOpLmxVpBxGvndqf2LX2MeaooaZPvxwT2npRh4xmjEMyOorgf2yW02YVgrOczx5AemWgWg9lBf8WQDxATCWp6rtRRnfxDxGmn-fA08gnhrZ-IXA7DOiBmHoqEFEb30tFhdw_DMVSplL2LUvu4ijj_r55xznqXITXUENpWaeiFWJdTsgxJMEm6lj-EOE3_xlFlovk2I7AyuzxT_N19-0jTLBnNMcTnx_c2fKuXGPKuUQ88tttJOi-cn6hpCz1f1B12L4eL9avmIxm-p2eC8wJ7Th21djIwRMl2u2otnZWutbtLif7JpwzfZgQEYtzUxEFYnxiiL8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b8221101a.mp4?token=USAzWNXmfW-Tg4_-aAqTAEyeo2Z9tQycbXDBDoVN9PLvKaf5dngueVmva82FhMvr7NnCs8DDpo8cMsKaedfnop03ANZyrszP2O8qP6CxEINm0D3Dct2sRnufrZgQ6u9XXCZVxnwiIx11Pqna6R4fug1dg2OmUuuxc-AGP-xXtlo0tBausAPNe3nPe3XQMU9eWE0rj_Nak082iYjezpSqEIK8Kh3ppXqnXqIYhwM1VFLnhcpsc3sFt20-F9NnvO8e7YfIc6JioIEKGI0fo2fK6ewJO0kAbx-9Nm_CyxzIXXHDV4XnxCqrzk17VwT1VUq5IoQwwfCZzC_ZfFAeQNmKtqnfHO3hotQ8GhgdCOpLmxVpBxGvndqf2LX2MeaooaZPvxwT2npRh4xmjEMyOorgf2yW02YVgrOczx5AemWgWg9lBf8WQDxATCWp6rtRRnfxDxGmn-fA08gnhrZ-IXA7DOiBmHoqEFEb30tFhdw_DMVSplL2LUvu4ijj_r55xznqXITXUENpWaeiFWJdTsgxJMEm6lj-EOE3_xlFlovk2I7AyuzxT_N19-0jTLBnNMcTnx_c2fKuXGPKuUQ88tttJOi-cn6hpCz1f1B12L4eL9avmIxm-p2eC8wJ7Th21djIwRMl2u2otnZWutbtLif7JpwzfZgQEYtzUxEFYnxiiL8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
ویدیو وایرال شده از یک جوون طرفدار حکومت:
من الان شرایط ازدواج ندارم چون نه خونه دارم نه ماشین
بدیهی ترین چیز برای ازدواج اینه حداقل ماشین و خونه داشته باشی اما خب من ندارم و پدرمم پول نداره که بخره
دلیل وضعیت الان بخوام کوتاه توضیح بدم ؛ سخنان حضرت اقا یک طرف ، وضعیتی که مسئولین درست کردن یک طرف
الان ما باید تا30 سالگی بدوویم تا بتونیم یک زندگی متوسط درست کنیم
الان یک میلیارد طوریه ک ما شما با هفت الی هشت سال کار هم نمیتونی بهش برسی و انقدر هم پول کمیه که شما باهاش نمیتونی یک واحد اپارتمان بخری
با این اوضاع 50 شبه کف خیابونم و هیچ ربطی بهم ندارن.
@News_Hut</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/news_hut/68248" target="_blank">📅 10:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68247">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">⏺
صحبت های روح‌الله زم درباره حلقه نارمک و جمهوری اسلامی
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/68247" target="_blank">📅 10:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68246">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qYp0b4gh2gqoRfL4EZJ4w83Wo6HR2FSR6N_CWh93-_x0xmKCjvCLGNkRRbCNPGp9l4_-RBU8v654nIZbKtg3Wj8khi_HbEIJTVNyO7D6Gujjl7ob3jAhXZTVuCCK7QXTBRyYJydz-VftSUzp-vWEO5la7FhlTFHDYYOFVUQPKW0mhvO-cL_PLxbuNDpHnSZMg_nePjojVXYhLLeZ2Gdu1Li7Hos9VQgcgYmEwmPsQWfX9uGz_pxsXh3kNx22gQlEclPrOtYaVbnD8BUEbzwk8XRR_bO-YQDAobLcTlWCN-H6aeCxMvZEvy6NFFPvYLHnO9Yfx_3MuQiv30ylMQZl7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سی‌ان‌ان به نقل از دو منبع آگاه:
دونالد ترامپ، رییس‌جمهوری آمریکا، در حال بررسی گزینه‌های گسترش عملیات نظامی علیه جمهوری اسلامی است. به گفته این منابع، در نشست سه‌شنبه اتاق وضعیت کاخ سفید، راه‌های تشدید فشار بر حکومت ایران برای کاهش کنترل آن بر تنگه هرمز بررسی شد.
بر اساس این گزارش، ترامپ احتمال عملیات برای تصرف جزیره خارک، مهم‌ترین پایانه صادرات نفت ایران، و حمله به تاسیسات زیرزمینی کوه «پیک‌اکس» که گفته می‌شود با برنامه هسته‌ای جمهوری اسلامی مرتبط است را بررسی می‌کند. با این حال، او گفته است ممکن است عملیات زمینی برای تصرف جزیره خارک را کشور دیگری انجام دهد.
سی‌ان‌ان همچنین گزارش داد جی‌دی ونس، معاون رییس‌جمهوری آمریکا، در گفت‌وگویی تاکید کرده است که جنگ تنها با ابزار نظامی به نتیجه نمی‌رسد و در کنار فشار نظامی، گفت‌وگو برای حل بحران نیز ضروری است.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/68246" target="_blank">📅 09:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68245">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/68245" target="_blank">📅 03:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68244">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Sh2c7CiExExDZH_6VF5C6tdVG9rMUcQGnyFGy0YG7fkVv3rn24zEBONEuOkVky__U2AwTVIl1V61XIi8mVoThO6LluGLhJ1_4gJmhR3v_I5fxTpXnEpIPNLcP9cOOjNzPoQyGVWIp7eU-3_x8m0hUUMY-H4QgroNE9B4eCmaYDS0EZw8QJI68S7Fad7iCMpkYM0MtQrAk-ekT4BQbhKGipAWZL8jx4YhG9ts85QvYURc-ny17Yig0amG5SznsBvdh1IoObbxCkjpseh2ytTZiQ9eXJV7pPMRNvE6YvpXC2lGT38tjBPnb7Aj-5LITqBLdIy8YkKIKXtM7dHMGB9LIQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/68244" target="_blank">📅 03:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68243">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4873db94b.mp4?token=Lo6AKHUP9Fk5clS3OJv7rfYNKvB54WW8jUMgCw6mOEWR93gtkwZoH-K26lV2Y-R4qg-tw9LA0oive37t8nvjQm_XCAL9k_6I_ALK5lyxXFGyLoAaKVK1F5o3b62awdb1gSdF0OokYztiQ3EMXeIIfe4AHUb1fF09Uv4uGUvy0fc2ndPT01cMyYzeEeYJb1vUdMupmXPEC2_NlZ9l71K3McweZbSXPDPCH4M8StvJYKA7RGBzAKNSVcGS4i-IFi8h52cbEuUQRIeEvDC1Xt_fdo8ycQh-Fqk2T_JK8RfHdmbUdmROJxer136IgwR15hqCYaUOd3hqwwQ9fESQmsmcbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4873db94b.mp4?token=Lo6AKHUP9Fk5clS3OJv7rfYNKvB54WW8jUMgCw6mOEWR93gtkwZoH-K26lV2Y-R4qg-tw9LA0oive37t8nvjQm_XCAL9k_6I_ALK5lyxXFGyLoAaKVK1F5o3b62awdb1gSdF0OokYztiQ3EMXeIIfe4AHUb1fF09Uv4uGUvy0fc2ndPT01cMyYzeEeYJb1vUdMupmXPEC2_NlZ9l71K3McweZbSXPDPCH4M8StvJYKA7RGBzAKNSVcGS4i-IFi8h52cbEuUQRIeEvDC1Xt_fdo8ycQh-Fqk2T_JK8RfHdmbUdmROJxer136IgwR15hqCYaUOd3hqwwQ9fESQmsmcbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
پرتاب‌های متعدد موشک‌های پدافندی پاتریوت به سمت پهپادهای ایرانی:
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/68243" target="_blank">📅 02:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68242">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1519c2ac09.mp4?token=TMRPmpKlyVsYXg-F9UvJ2nAeu9ISU2Ev4nxt0pKftAWGPLuh2e5U2E3MASDMqDzdOVaDfao_CwWHhgDpQy1CLURjBqOFowxit0AJTpooBkoy7ewXoXsWsjhXgkKAmnLaETr4jpx-FQnTMMWE0xNTxG5ycuM5w7noeeutC6iJYXb1pMUBZCFE01SUKcFBSosBysya_uPPOVEVpa-WmaM1xO5sj0sUnxta1KRydC-iBhu9ZeKjojspLdCnwK2PXSsL24zF6jBAhy4nE0S2ceKaWREPKUo5LSMYAAX6ZY0EUovpCS7uDYBiZmTjKW5OfQwH5C0zuz5NRT3egFQ1uCzezw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1519c2ac09.mp4?token=TMRPmpKlyVsYXg-F9UvJ2nAeu9ISU2Ev4nxt0pKftAWGPLuh2e5U2E3MASDMqDzdOVaDfao_CwWHhgDpQy1CLURjBqOFowxit0AJTpooBkoy7ewXoXsWsjhXgkKAmnLaETr4jpx-FQnTMMWE0xNTxG5ycuM5w7noeeutC6iJYXb1pMUBZCFE01SUKcFBSosBysya_uPPOVEVpa-WmaM1xO5sj0sUnxta1KRydC-iBhu9ZeKjojspLdCnwK2PXSsL24zF6jBAhy4nE0S2ceKaWREPKUo5LSMYAAX6ZY0EUovpCS7uDYBiZmTjKW5OfQwH5C0zuz5NRT3egFQ1uCzezw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعال شدن پدافند بحرین در پی حمله موشکی و پهبادی سپاه پاسداران
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/68242" target="_blank">📅 02:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68241">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aci8UzDiFtULbTKoiiPmNABF4E7oT1bYeFeHu5xYqiVw4LJPP2wLWEigl66C5kd_5qTCQfRIqF1uz3UR3wDlU0vtm9J7_bABcbMYqQF9l01oCvBtodrTD95asWZTpwJQq6ZrbSGfmWSzOtfW9kFgiFKZLg3-JVtN_AuqURNh8T5WAz-EbL0knrnwuCeErC4DQiByKAMh7vVBdGWr_wgKdq2aj3wJTIa3lKWtmfodE87p2-2GRc5OIhn3KG_LOFftsgzsgLGySd_cbQMlkfbjS0eNKHyteMOaqgAytJ479LsYQOmfJ0fxR5N0AYfi0z9hhOaXe7xRY3eYvnm7gqSWiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/68241" target="_blank">📅 01:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68240">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
انفجار در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68240" target="_blank">📅 01:38 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68239">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cd7e59689.mp4?token=hdLmN7Z-ORDhQkK4cjxM2_hD5gLaaCFqETPgjdH12DoQVPKsom2OzhKmz_PP4xSrhKFGG5XCICrxQ5vwzGV-qyzcnZHp9mYuIafnJZ8u8ea18r6Xc3O_QDE1Fu02-rakOc8tuuiYiKUTBnNUlHJwk21iRm-OJqly_Q_DanuZtxPRo9kYXOvgO-ZE0WwHZRRve0ZgWJIPbKYMnIEI35sdOlGjJOcajffPg5VSCMphEb-johMvtagfiGJvf6MTClMaydQyKU10mTMscVGvXbLQP-KGZYS3NRscH4w7fghR50yIWo_90IvpxgF45yPtxltS6FWzlcbPWwNeaAbj67xm1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cd7e59689.mp4?token=hdLmN7Z-ORDhQkK4cjxM2_hD5gLaaCFqETPgjdH12DoQVPKsom2OzhKmz_PP4xSrhKFGG5XCICrxQ5vwzGV-qyzcnZHp9mYuIafnJZ8u8ea18r6Xc3O_QDE1Fu02-rakOc8tuuiYiKUTBnNUlHJwk21iRm-OJqly_Q_DanuZtxPRo9kYXOvgO-ZE0WwHZRRve0ZgWJIPbKYMnIEI35sdOlGjJOcajffPg5VSCMphEb-johMvtagfiGJvf6MTClMaydQyKU10mTMscVGvXbLQP-KGZYS3NRscH4w7fghR50yIWo_90IvpxgF45yPtxltS6FWzlcbPWwNeaAbj67xm1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
سنتکام تصاویری از اصابت چندین موشک هلفایر به موتورخانه نفتکش M/T Belma که در خلیج فارس در حال حرکت به سمت جزیره خارگ بود را منتشر کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68239" target="_blank">📅 01:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68238">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
بندرعباس بوووم
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68238" target="_blank">📅 01:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68237">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EiZrourKo8VTzQNd10XtY2wz1mVW1tuTmzH8YP9PiLABLBJ-ap_5H9F6WwAQgVL4Y___uPq57exGqIw3dzUZh6CsblSNrqJPOV09VIHDgns9l3CtGq7-7Fx9eDV9NDmXtL1Fa0mDlI9h6MnUhnc4YGnkQFxwL7SZGL9j7VcfnfMKjSDjgg1CGMLIcehLdc6VmkMGXhxlHzpOBH-73M7tp8_trj8ti3q6HlTfXziBkGYVQy7Eo-D0Yq3069M278MxZKDUo3L48CbFQNaJCMKkgCkZiWjX5sYy1_d-1yCvikpDU0GYZqKLRqyITq_IGYvWt-dTz12NbmrycoVsBMsNXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی| امشب روح فوتبال ارضا شد
🇦🇷
آرژانتین
😀
😃
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#hjAly‌  @News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68237" target="_blank">📅 01:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68236">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
چندین انفجار شدید در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68236" target="_blank">📅 00:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68235">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uEQYYWgOAdUAGDHWSJyG01ge7Ol6bl7MfCiPCiPtdm9IRq1x4uMQKXyhOHX8-H_gqyXI-2HUfQ7d2yvPhHO8Okx1WA-_hquLua6zyzlF7Iu1dFRKDQjcj8yFURBp9P05JgQvPPOk-FRpMz8Kw675ExoBDcbPodma0N_rGg_ELnFbX1MTfWm5dR35BHRe4N1G3trohBFhNHT6zLkEaoQ-c2i6rJpKpuZ-j7ZIaBTsSMl_QWmN_RybHlKPp5uW3z6Mr3xSvpP27gSjVLhpmtH9CtbHy3SUodullvtYbprnrONP2WF6PiVsCuL8aVW9aZoSnx_P9Pq4X251B4p43JGuhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی| امشب روح فوتبال ارضا شد
🇦🇷
آرژانتین
😀
😃
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68235" target="_blank">📅 00:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68234">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">من خودم رئالیم ولی برای مسی باید ایستاده دست زد
😑
#hjAly‌</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68234" target="_blank">📅 00:25 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68233">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d327baf32e.mp4?token=EdUDwJbx7As6NyBqfp-H2Bai-v3qIKUK4cDVWuzhIR6fJPc4FQ85wjhxYgoFx1lToPqoTp-7Ls4HnCHf3iFLF3ajOIFt5bVLxEa_n5cTqX-rejkDS0PmV9M5L0ZcLx4LmoX9Z7mZP21EjOhL34nn8GAy-eZUnKAzyhywLzolqL44HX747uFy9ujZHz2eljZICAsjr2GnXtJjDIC-tlNQIXEYtRRlFWjfeTJ-m5iPySwnKlRCPz1KejoB1BdDWvDZ9ie3MsskDoVN4md6Dtn6vSh7hjuqVDYNtYV-Quj26t77uRuXVjX2_o9LMBA0dejFKzG_iGo_tOIWh_w45sKPSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d327baf32e.mp4?token=EdUDwJbx7As6NyBqfp-H2Bai-v3qIKUK4cDVWuzhIR6fJPc4FQ85wjhxYgoFx1lToPqoTp-7Ls4HnCHf3iFLF3ajOIFt5bVLxEa_n5cTqX-rejkDS0PmV9M5L0ZcLx4LmoX9Z7mZP21EjOhL34nn8GAy-eZUnKAzyhywLzolqL44HX747uFy9ujZHz2eljZICAsjr2GnXtJjDIC-tlNQIXEYtRRlFWjfeTJ-m5iPySwnKlRCPz1KejoB1BdDWvDZ9ie3MsskDoVN4md6Dtn6vSh7hjuqVDYNtYV-Quj26t77uRuXVjX2_o9LMBA0dejFKzG_iGo_tOIWh_w45sKPSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#hjAly‌</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68233" target="_blank">📅 00:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68232">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">گللل دومممم آرژانتین
💢
💢
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68232" target="_blank">📅 00:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68231">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">گگیایایتیلیاایایاااللل دوممممم</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68231" target="_blank">📅 00:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68230">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">گلللللل تساوی آرژانتین به انگلیسِ کثیف
🔥
#hjAly‌</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68230" target="_blank">📅 00:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68229">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">گلللللل تساوی آرژانتین به انگلیسِ کثیف
🔥
#hjAly‌</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68229" target="_blank">📅 00:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68228">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">درووود بر روح پاک مارادونااااااا درود بر بیبییی</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68228" target="_blank">📅 00:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68227">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">کلم کیریه، کیر تو انگلیس کیر تو کیراستارمر #hjAly‌</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68227" target="_blank">📅 00:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68226">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/379978a151.mp4?token=BLeV2XQUn54Oj9majlbV0RPCtuQHoMaylAUOjEO7COFxFBbdjUk2ULelWJrAX7BJXZnC5dY71fJrdrXrAM2_s71f1QkCCweHk2f-dwSV_LEJgPoU2KoOvJnB5gEwbhSJ95YolwbqYFHjyAMQxy5qAcXWwWeKuTL_5LWm9Vr1ddg9PoonSxKQF8R6O-blf0uSH9YtDawZvDfCxoj410DnLnIsmsebZXVtOKKPcaIECVw0uWu6cU2TxqFfu2-mzxmJC0_XLBG-XZfrCA-O8HO47LxfNcKm3xA2C0sPQXAGm3x3ExE-HTmf9GIo_bcBpnQv6wmyjCYtyWv39N4MbSzl2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/379978a151.mp4?token=BLeV2XQUn54Oj9majlbV0RPCtuQHoMaylAUOjEO7COFxFBbdjUk2ULelWJrAX7BJXZnC5dY71fJrdrXrAM2_s71f1QkCCweHk2f-dwSV_LEJgPoU2KoOvJnB5gEwbhSJ95YolwbqYFHjyAMQxy5qAcXWwWeKuTL_5LWm9Vr1ddg9PoonSxKQF8R6O-blf0uSH9YtDawZvDfCxoj410DnLnIsmsebZXVtOKKPcaIECVw0uWu6cU2TxqFfu2-mzxmJC0_XLBG-XZfrCA-O8HO47LxfNcKm3xA2C0sPQXAGm3x3ExE-HTmf9GIo_bcBpnQv6wmyjCYtyWv39N4MbSzl2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
جمهوری اسلامی به زودی شکست خواهد خورد.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68226" target="_blank">📅 00:12 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68225">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b94485380c.mp4?token=XWgbUwrv_Lm9NcPsfZfJSVl1twj-nFhCiKkHjzWnDt1ieaV6vLt-ShlnoILF9fUJS6CaFmlvCh6EKWdaEfelY449oZhylPEmZG5XDEGuOlVwf76pZuelbMb3D9P3ggfFMYbdYA69bD7XwUrqZVbYE3K5PJHlpOCXe5CEgTGZCoLL1VgaaIIWGDWmM5ZDLNPUenZrmjCwgEl8EfY6gjbNsGNAMJ-SgqrxclnvuTxHSsf5MpC050_L4GcIfmdC0PEpeexpzwGGNzVo93hGt6UQjIqg6S-pV3Cfb873lDwm5TUllqElHtXkKzDPxTkkAmZ8QSKEUCR18vQbew3lTqv3DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b94485380c.mp4?token=XWgbUwrv_Lm9NcPsfZfJSVl1twj-nFhCiKkHjzWnDt1ieaV6vLt-ShlnoILF9fUJS6CaFmlvCh6EKWdaEfelY449oZhylPEmZG5XDEGuOlVwf76pZuelbMb3D9P3ggfFMYbdYA69bD7XwUrqZVbYE3K5PJHlpOCXe5CEgTGZCoLL1VgaaIIWGDWmM5ZDLNPUenZrmjCwgEl8EfY6gjbNsGNAMJ-SgqrxclnvuTxHSsf5MpC050_L4GcIfmdC0PEpeexpzwGGNzVo93hGt6UQjIqg6S-pV3Cfb873lDwm5TUllqElHtXkKzDPxTkkAmZ8QSKEUCR18vQbew3lTqv3DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
لحظه حمله آمریکا به سپاه راسک سیستان و بلوچستان
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68225" target="_blank">📅 00:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68224">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل اول انگلیس به آرژانتین توسط گوردون.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/68224" target="_blank">📅 23:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68223">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
انگلیس اولیو زد به آرژانتین
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68223" target="_blank">📅 23:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68222">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a007633a2.mp4?token=NQb5nXcYcdHo7BwXCl8Go8t4FzaYiaiyT-rmuX2YTXsxvW2zW8TZBT5yw-YGAoH7nSIuoLpRqX_vcXs_aky7i2Hz1fCgtpAvKLvv_WeTQt4yAbJ8EBqPT9577cGPStyZjHAkI9xyEM0rrtTTJv0-Hw_awbk7giHa_ipasADeTed27i-bpg77IdKX7sK5LYoNSaa7JeE5FFyiNSrXrCqe9a5nogz8Nww1VkA5RAVHLwabw7hWB38OeYSfhDjvN2E97lwrt1z-YB9uyjgiFxqOjH3rYwwxy5t6SCzPPIYoH3fO-FRe94yFP82uKXqNEXfjF6XsH8mKj_FQSy6JXhT_Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a007633a2.mp4?token=NQb5nXcYcdHo7BwXCl8Go8t4FzaYiaiyT-rmuX2YTXsxvW2zW8TZBT5yw-YGAoH7nSIuoLpRqX_vcXs_aky7i2Hz1fCgtpAvKLvv_WeTQt4yAbJ8EBqPT9577cGPStyZjHAkI9xyEM0rrtTTJv0-Hw_awbk7giHa_ipasADeTed27i-bpg77IdKX7sK5LYoNSaa7JeE5FFyiNSrXrCqe9a5nogz8Nww1VkA5RAVHLwabw7hWB38OeYSfhDjvN2E97lwrt1z-YB9uyjgiFxqOjH3rYwwxy5t6SCzPPIYoH3fO-FRe94yFP82uKXqNEXfjF6XsH8mKj_FQSy6JXhT_Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
شما به این نتیجه رسیدید که نمی‌توانید با سپاه پاسداران مذاکره کنید، آیا این به این معنی است که ممکن است آنها را مانند داعش از بین ببرید؟
🇺🇸
ترامپ:
بله. همینطور است. درست زمانی که داشتم به اینجا می‌آمدم، تماسی دریافت کردیم و آنها (ایرانی‌ها) می‌خواهند ملاقات کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68222" target="_blank">📅 23:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68221">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48590994cc.mp4?token=G4xBeeuB1Vo7YKzSkcyVHp0Kdb7NTRCJKKIPqVKZiAtM4GyV6KZZz39IsZwS2NQCbv8icawaT4MrvxcCWyeRAX42VmC6ZG5v0XwBrEOkg1zkpcu4zeN5l7aKMSNRWg6xblgharRHkXhr4XeVIbWthLH0CI6IKHSgl1uDkKcByx9gKiP5_oi9Ij5hyrq2hp6_G8PuRN7nOlV3snsasfINNj_OlYVM-259N31xKBSHx945McK26ES8VDrAWcVGgi2BHCUp3fRxlKMJTrbCssUl__kbv0ZadmGY-dPhVHPVBdtab1Bv2HFf2KJN_zQpsP1CCy1LMfPvOmQ1XQ-n54glhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48590994cc.mp4?token=G4xBeeuB1Vo7YKzSkcyVHp0Kdb7NTRCJKKIPqVKZiAtM4GyV6KZZz39IsZwS2NQCbv8icawaT4MrvxcCWyeRAX42VmC6ZG5v0XwBrEOkg1zkpcu4zeN5l7aKMSNRWg6xblgharRHkXhr4XeVIbWthLH0CI6IKHSgl1uDkKcByx9gKiP5_oi9Ij5hyrq2hp6_G8PuRN7nOlV3snsasfINNj_OlYVM-259N31xKBSHx945McK26ES8VDrAWcVGgi2BHCUp3fRxlKMJTrbCssUl__kbv0ZadmGY-dPhVHPVBdtab1Bv2HFf2KJN_zQpsP1CCy1LMfPvOmQ1XQ-n54glhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ستون دود در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/68221" target="_blank">📅 23:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68220">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">برق بعضی از مناطق اهواز قطع شده، خونه ها دارن می‌لرزن
😑
#hjAly‌</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68220" target="_blank">📅 23:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68219">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ترامپ
مادرقحبه‌ی هزارپدر
: ایرانیا خیلی دنبال توافقن می‌خوان جلسه بزارن
#hjAly‌</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68219" target="_blank">📅 23:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68218">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
گزارش ممبرا از اهواز:
اهواز قطع برق منطقه احداثی
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68218" target="_blank">📅 23:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68217">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ممبرا از اهواز گزارش لحظه‌ای می‌دن، حداقل تا الان ۱۲ بار صدای انفجار شدید شنیده شده #hjAly‌</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68217" target="_blank">📅 23:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68216">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10ead41427.mp4?token=BXYefYgXFBdFDIZqjlYtTx-7tTU1rKgQktPF2Jh4XL6errEDECK2LgR60Ju3uNZFp53gk0dgoQXICGc2aaF7enSVEe8ZdB-r4sAwsBSB6vTbgm7Cvq1EQyAK5creTCaLmuyX4VmI7jiM0jtdJkZ23RIn8zlwI_sO32JumG6VrbnBN7eSr03QN3GMKoXVTHGDUrH_XfPh3ZzAsnMWJfFjqmP6f6w48tOQM0-FI6qW4-IgE7GfAlmFVP3g749nlAxoUtaLGOOe-nOzmI1XzTVb-ZDnREqnVfd2ijfNVauA_sW0GsHmsnPr_7fz_JAXzTh1Tdmq3pHXG4Exn0KZzWiiEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10ead41427.mp4?token=BXYefYgXFBdFDIZqjlYtTx-7tTU1rKgQktPF2Jh4XL6errEDECK2LgR60Ju3uNZFp53gk0dgoQXICGc2aaF7enSVEe8ZdB-r4sAwsBSB6vTbgm7Cvq1EQyAK5creTCaLmuyX4VmI7jiM0jtdJkZ23RIn8zlwI_sO32JumG6VrbnBN7eSr03QN3GMKoXVTHGDUrH_XfPh3ZzAsnMWJfFjqmP6f6w48tOQM0-FI6qW4-IgE7GfAlmFVP3g749nlAxoUtaLGOOe-nOzmI1XzTVb-ZDnREqnVfd2ijfNVauA_sW0GsHmsnPr_7fz_JAXzTh1Tdmq3pHXG4Exn0KZzWiiEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
اهواز رو وحشتناک دارن میزنن
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68216" target="_blank">📅 23:03 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68215">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ممبرا از اهواز گزارش لحظه‌ای می‌دن، حداقل تا الان ۱۲ بار صدای انفجار شدید شنیده شده
#hjAly‌</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68215" target="_blank">📅 23:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68214">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
اهواز رو دارن میزنن همچنان
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68214" target="_blank">📅 22:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68213">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
گزارش ممبرا:
مجدد انفجار در اهواز خیلییی شدید بود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68213" target="_blank">📅 22:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68212">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DuNlz9JoFGV16ojlrUBLMih6UUYa-igFsf2CLOyEB_0vmAxxyxrDzfCGpaUIyEhRc98Z_V2TXUWlGqHvyAteLTbrxG7Ue5RwCoXF8vwq_K9O-uooRcjoyfZw7Str2jr7RMUz_W8VTSRGJ1bGcBvbIC1_5R0Yb01y9IbYp5vTkqN5c1rWiWI6qZqrAgaNy6CSuDN7JA8TdzLnJ0urR78s3wVwsagLZlsjjgod3eSYeXb2jG1iWsRqaIlta-ABGjsz9oEQPzlUpbKpjk8FaHACKCeNusiChjp2slPdNSgdW1gVPcHaWtAfREmCBf7SNPoFwA8jVPyPkWbY3ODFo23LEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
ساعت ۳ بعدازظهر به وقت شرقی، نیروهای ایالات متحده امروز موج دوم حملات را علیه ایران آغاز کردند.
این حملات به توانایی‌های نظامی ایران که برای تهدید کشتی‌هایی که آزادانه از تنگه هرمز عبور می‌کنند، استفاده می‌شوند، هدف قرار گرفته‌اند؛ تنگه‌ای بین‌المللی که برای تجارت جهانی حیاتی است.
ارتش ایالات متحده در پی دستور فرمانده کل قوا، ایران را پاسخگو می‌داند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68212" target="_blank">📅 22:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68211">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
انفجار در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/68211" target="_blank">📅 22:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68210">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
گویا انفجار ها خیلییی شدید بوده
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/68210" target="_blank">📅 22:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68209">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
مجدد انفجار در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68209" target="_blank">📅 22:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68208">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c19ec2f58.mp4?token=p6VXJ4-zzrVY-zm0ICLtxTQYSSorhkUWQDi7uGCIvYF_mVi1hJ7ScTzf8yZzu7BB1rH_SO5wRUSzKWWGchHP01YSUMQuC1LD6BAY1JdP8WEzJ4ChFD9NwAFC6vS528b7gu-hdu7jGTHIcFUkr5cZT50_NBIItCXO9x4ZRakji26FYRY0QdOeK9APj72nEunDFvI9p18ZGwdw4R56OmErwYO9BX8mU1Kx9NoiMAxDY7yQUu7LNDvwuXRt783e5JNtCHjbbP-BbGywaXlT4ADBWtHd5oQaVJq_7gUhQP_a1qvsEC19iFs4Snl4igHPUX7rwr7cbSWpfVA68O_yXf1Zbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c19ec2f58.mp4?token=p6VXJ4-zzrVY-zm0ICLtxTQYSSorhkUWQDi7uGCIvYF_mVi1hJ7ScTzf8yZzu7BB1rH_SO5wRUSzKWWGchHP01YSUMQuC1LD6BAY1JdP8WEzJ4ChFD9NwAFC6vS528b7gu-hdu7jGTHIcFUkr5cZT50_NBIItCXO9x4ZRakji26FYRY0QdOeK9APj72nEunDFvI9p18ZGwdw4R56OmErwYO9BX8mU1Kx9NoiMAxDY7yQUu7LNDvwuXRt783e5JNtCHjbbP-BbGywaXlT4ADBWtHd5oQaVJq_7gUhQP_a1qvsEC19iFs4Snl4igHPUX7rwr7cbSWpfVA68O_yXf1Zbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
شلیک موشک از کویت
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68208" target="_blank">📅 22:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68207">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
سه انفجار در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/68207" target="_blank">📅 22:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68206">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66f6a0a0f4.mp4?token=rCJKkm2wbCx4A1_dS0hPZVqUU1u5ae5vdJTaC7abFQW6pL8vu0Kcl-Iv8VYQ9zupYfHcc8oRsaVMstNiUzt2h2OaQ_4B6IiOvx4lYzJzeu1IwmTikNSov-_qCmOL0-cVEA4KKi5GZ99TSrh8HGdgZMq-_WptOETtDRhMPwJndw9dyz9VEEvYtJDA_Q8uOG56-1fVVUu6eZEzLPt3v5v3ZQrE4VQ46AC2XlDBoDTDce4eeN3HCo7hqXxLLa0Z8IicO_wsVOcX1lOQlZqLYJLhXZ5CpgWwtiU0FO8vPCZx8yjsA5HVGdhwEU1QBapmI5kYqTPlGeJ5vY1EnBLp_7GTBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66f6a0a0f4.mp4?token=rCJKkm2wbCx4A1_dS0hPZVqUU1u5ae5vdJTaC7abFQW6pL8vu0Kcl-Iv8VYQ9zupYfHcc8oRsaVMstNiUzt2h2OaQ_4B6IiOvx4lYzJzeu1IwmTikNSov-_qCmOL0-cVEA4KKi5GZ99TSrh8HGdgZMq-_WptOETtDRhMPwJndw9dyz9VEEvYtJDA_Q8uOG56-1fVVUu6eZEzLPt3v5v3ZQrE4VQ46AC2XlDBoDTDce4eeN3HCo7hqXxLLa0Z8IicO_wsVOcX1lOQlZqLYJLhXZ5CpgWwtiU0FO8vPCZx8yjsA5HVGdhwEU1QBapmI5kYqTPlGeJ5vY1EnBLp_7GTBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از کسی که در برنامه زنده می‌خواست شب‌پره بگیره چه انتظاری داشتید آخه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/68206" target="_blank">📅 22:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68205">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‼️
یه هموطن داشت از محل برخورد موشک ها به چابهار فیلمبرداری میکرد که یهو برج مراقبت دریایی رو زدن
‌
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68205" target="_blank">📅 22:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68204">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nksqSjg8n6CLwx8xkpnWZjJCmU5GubEPqEj1Ko3iL3Beu8RYmte7Ll_5GrNsqT7peMC9hPqqUV6QGw1Z5Ld1sn0MARHfqoxIlKXWvMYf3NwwqoKbn6rHHTlTYqXgnaHM9DXDbe6cYXG_vpSOnArZZvTacXaW7wIcCkkBz4O_3e95KiKaT1vqOSZBiMklSDXfKZGoidPmyZ-jLuED6UNK55tD-5Sbe93eYGur7JdD_3oYlcxQMOlygwA_Ixj6g0xah3MGjt7QdsuO-rEG0A7X970ydgQMEdFwmGr5D9OEUne0vHWqvoPE2nzbDS_k1FU-_3Ot86Zak4nnpeZxBEhhOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
امور کنسولی وزارت خارجه آمریکا تو ایکس، یه بار دیگه به شهروندانش یادآوری کرد که هشدار سطح 4 برای چند کشور از جمله ایران
🇮🇷
، عراق
🇮🇶
، لبنان
🇱🇧
و یمن
🇾🇪
صادر شده.
+هشدار سطح 4 به این معنیه که آمریکا از شهروندانش میخواد که به دلیل خطرناک بودن اوضاع، به این کشورها اصلا سفر نکنن و یا اگر اونجا هستن فورا ترک کنن.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68204" target="_blank">📅 21:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68203">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
🇺🇸
فاکس نیوز به نقل از ترامپ:
حملات علیه ایران هفته آینده گسترش خواهد یافت، و خاورمیانه خود را برای اتفاقاتی که بعداً رخ خواهد داد، آماده می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68203" target="_blank">📅 21:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68201">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EuqjLK28YVYM6vM0RB4Djuca9WFuWPiGND66o_k4ZmmdEz8K_5lAeudahkdKpHJiVKhuUMFwAJPc3N3ZjmPhhLrtaJpJUvf6OIfF47aGvhL-GcxF-o05oc-2Wg8jYWYMD8wSGS5UK4IuWARNQGJNL8Fy2JKfF21Wu2oKI5gw8SF35t2_Oy1iKayidqAi8rbOaiPInJYZAoP4cDIml6npmOg-RMtRkSCLu5EAcTlFEgN2B2SEuL2HODDCx5QW5cqaNis9TJqGTfmdNpGc6_8a_Uv0TxxpNNy6alCoAc7oDLarjMkCe4zR8aiD8o2KnCpHRWM3ozW4jQPInQ6vwMSQ1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GPZSYaTN-Rh-BT-W3syor8mQL6dF9yZxmQu4uxzBt-6cqBuP0dLqz6gD_7FXcrlK9tehmqrEDviTDWuW890NKJpuY1Srn1UmFPuuCyjt8bxvpMSzJSi9bz6N0rjavtvtCEcvuidfJhLb9HSCGInRIApSYTHgDibVZ8oUMwCbuSxxQjDaRdgm0v9ZwCsCljqiYl0oyXPKg5KXeULQGWB3JZgqrweXaScRibVPtB_BmTS4j5Ix7VfDO7a_t5oWIS6qsaNkMoY3Mjc0R2qvWEdcPRlilwfN_VaDUOOpHEmspwSlvtbPOq2CzDyhn4SWsKpsdHi_EA47A8om4xX5rFwjfw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
ترکیب انگلیس و آرژانتین برای بازی امشب
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68201" target="_blank">📅 21:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68200">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
قالیباف:
همزمان با درگیری‌ها، باید از ابزارهای دیپلماسی و مذاکره نیز استفاده کنیم، به گونه‌ای که منافع ملی را تأمین و تقویت کند.
همانطور که بارها تاکید کرده‌ام، مذاکره در این مرحله به معنای تسلیم یا ارائه امتیازات نیست، بلکه در کنار جنگ، بخشی از استراتژی مقاومت و حفظ منافع ملی است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/68200" target="_blank">📅 21:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68199">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
قالیباف:
برای ما مسجل است که انتقام خون آقای شهیدمان را به ثمر خواهیم نشاند
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/68199" target="_blank">📅 21:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68198">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
محمدباقر قالیباف:
تفاهم‌نامه وقتی معنا دارد که مفادش معتبر و در حال اجرا باشد. اگر ایران از آن سودی نبرد، دلیلی برای پایبندی وجود ندارد. ما بر اساس اصل «چشم در برابر چشم» عمل می‌کنیم و در برابر بدعهدی، متقابلاً واکنش نشان می‌دهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/68198" target="_blank">📅 21:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68197">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇮🇷
قراره تا ساعات آینده ممدباقر بیانیه‌ای درباره جنگ و تحولات روز کشور منتشر کنه.  @News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68197" target="_blank">📅 21:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68196">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gw9PgxgzNRSN3_QW1_TJL6_XrI3awcOFbtLlj3cz_Nzx2nlSYmiqIF94rbqKhLCBGkCIdYW2XXP1xUXM0J2QalJE5TRsOwKWTfLIApo3aYzbkG12EuuCHEhppddMjDPKbJI3yOb62viwbPm3VhYUMPRU4vWyqkBmYFGIKmFwrRiVxT-Wgfw6iR0V3mCjEI82evKuargBGw8J3EBDDknwqiUWhT3_y0Rhhhu4X0XBa8U7t8VP8K2svtaQXy05BlSVBCiFzb6c568zxpcLKDrkMhVRQCOJLwlt6MOGpA9fFdEOKkMlYaJEwpX-YX4sMDauYci9s64zHrph65IcaGJLFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویر شهدای حمله آمریکا به پادگان ارتش در ‎بمپور.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/68196" target="_blank">📅 20:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68195">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YKSPKEC6mZjbHdmghtj2F9263_Ng0Kc4REMPHto7kM0dherxA3ts_FjjWN0oewdfMQ4DftVpSUcLB29i24OjjBjn0vRwX7VjM1GW5UDQEhfUgHESJCrFMMqq_wIMjFZoKR3P1CNDM4iojQPac0J9TVuI3woUDojSfVXObeeEdT4L1C8tTLmxmH2pULiVlQRES3ysxDZuREpZX4OQg3jwPwl_W1McEMANEWO6gOTeiFU_Lwwo70aPS2ydPQTuZSMOSlyrebZPJmSTSdtsB1NI_Kg9TEUscO0ZlS9UxEDKpzjDuRnyF2nJsiPFfcFC6njqDQa78-o0TMcJCPwnG632NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امشب عادل دو تا اسطوره‌ی تکرار نشدنی رو آورده، فوتبال ۳۶۰ رو از دست ندین،
کص‌خار میثاقی
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/68195" target="_blank">📅 20:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68193">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMreza</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DI9lqE4sA3BBcqZRWqexaweO4dvG_cz4uz1Q4AP9Q60osj_pBr05qOOKhy1ZTvV3oMIGKgXNvd6PH4NM64PlozWEphc6w7JS1mB9KgG8AxWhFY6lML7Zu8P1c5BMV_R9w_Zkpfi5tfP4J_YAlVoDx010R3MpV8N4Pq8fDzjz-H2tSeMuNQs2x6qQkiI2uAXqzWZJqjqee2DK3q2VqZ2ZcVaHLNT1XTj3DHk3Oo2k3T1_4AtT3-sWrtdeBvU6bKQaPmmVxuWiUJdDQ45wbA3nEzXklTruIN0kqZjA488eB6TWE9kYxpF4ziBvs-8SnfSuic4Kf6l8CfEnE7Yi1Hqp_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DIAMQCkI_7bRpWrddrPZN7yFJJwQjh_WfDF07rch8GF8xFM2CFtoDdKAm7zCkPwPGI60AQ6kwiSwNSzloZ07eP5boZljW4aUfbQ-qsmwoiBU6rq-Io3_8TxURzKD5eGBgdEuJT46ORMDCyMtTyntZOw6ulo4WI3i7GsGYVbL3i-yFnvU-PBg-a5t5SgL7fFlpeF9dep05_Y7pCB0epVjfKaIgfFiA1wHpRk2Dcbbhn1tqlvUCBT2ybA67zkaPyQOKFZJSZFHSWRAk9r9_SANK07QmRQbLyd4NMI1702XWesC-IZJ9DYpxrpQfWtHrz9Ct8bMxoJf-QR7M8N2x_kysQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Siuuuuuuu
❌
Zhiuuuuuu
✅</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/68193" target="_blank">📅 20:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68192">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2e6c5a6cd.mp4?token=E62JRyOQEjmvsL5EzVRcmqlAmY76v3oiZ3CAOUCprVNJeWCDCVrdHDfEBuKNbiZVEVTdA5oNBNMfhCZUd6cSvGMgPaxfyG1ib93ll5TZTABd0qEIxR0rpciFuT-8Z-Aqjc1yvJmJWNOsJC-yyC5J3Wmd7YWtRWFnJhyo_BNE6Qvusm71emJdVJbSI3MB73hki0OcbZSZ9BsePu9fyva9VIHE5MkxNc6PmW27PTSPYvfQ4X4LTCekJ9HJ5fvmOCOAdEQW83LQ2fo44FuQXwzTM1POrV5XqS5CzZDlUFzSNmWinh-v3eRwVmB-0GjMfrR21vg7qW208wCX795CmYtu6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2e6c5a6cd.mp4?token=E62JRyOQEjmvsL5EzVRcmqlAmY76v3oiZ3CAOUCprVNJeWCDCVrdHDfEBuKNbiZVEVTdA5oNBNMfhCZUd6cSvGMgPaxfyG1ib93ll5TZTABd0qEIxR0rpciFuT-8Z-Aqjc1yvJmJWNOsJC-yyC5J3Wmd7YWtRWFnJhyo_BNE6Qvusm71emJdVJbSI3MB73hki0OcbZSZ9BsePu9fyva9VIHE5MkxNc6PmW27PTSPYvfQ4X4LTCekJ9HJ5fvmOCOAdEQW83LQ2fo44FuQXwzTM1POrV5XqS5CzZDlUFzSNmWinh-v3eRwVmB-0GjMfrR21vg7qW208wCX795CmYtu6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا صبح می‌شه به کریستیانو خامنه‌ای خندید ولی کانال زشت می‌شه پس بسه، فک می‌کنه کریس آمریکاییه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/68192" target="_blank">📅 20:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68191">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GzXVSI8rV2an8u2p_e0nxQD3mm5SZA3gv3gGvJ50C46K-w-ti2wkBq4AphtjAGSkUnDV5iX2pUEAOfkhSaItWLJ_tSq881Q4W6GAriEPxEPDzfNRyfZQRsF6zlFh5xt5KlmhnH4mJrezIkJtb_1AEIHXe4L-B7dwsVQuSf4mYS4C-6r0B8jhjBRrPvdO9CGhChbT_2SKTdYYWCziLzPwS5aPWAFNydCz1wGdVBuc-lFyeCXMS6V4lcnvSyreBPX1ATUILSWv2S52QeKMBItRPNl1eFgMf6YmXpdKy3jpGmishSJl1FWg1pqfVwaw-f3Q-ql4qt5vXmz04oiGpbiUiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کریستیانو خامنه‌ای کرایه اسنپ نداشت بره سازمان؟
😁
#hjAly‌</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/68191" target="_blank">📅 20:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68190">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرونالدو</strong></div>
<div class="tg-text">اخه من چکارم؟</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/68190" target="_blank">📅 20:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68189">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SouJKCM5VmheEsgZ3yG6_u79VIdtGfbS6m1Ed5qafh-gngCub2TPQbywhHUukOV8Aoi2cK24viqWPqevNtVTaDm4DGZlx6gkqcNBsQ7RzwLYT3OPTJpzdDJh_mJlP7XmEjCiNeHScH0aLCiN2KvN_TReTrJMDTonHXqg2ClrvABLB-ol8P8M_C9uP4soxPKul0_R0Nl0WydtMFHnXXxg_6jXUl19VcYdgKu_80cycCAudmsAc7WF7OiBlvMSIMZEvsaJ3aZd7kEodWfuSP_uHXwQHGPMMkVqOpPXU3Z6aSV18WJl6UknXh9SRtzI6ggS1HnmPOG9BXwYIG_AT3u3zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عقل بچه‌ شیعه‌ی آخوندپرست
🤯
🤯
🤯
🤯
:  #hjAly‌</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68189" target="_blank">📅 19:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68188">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6b2e5150b.mp4?token=nYu3xwftVtUUt_SFX9ODQxJVWKLfobigYxr_bRdFYd9OogVxb-1hF2ZmMCnnIYsRDGncSCh_IhfMNXEQvJIWttqV9WwDgGfbkqjDcAzWrpZGpxliMy_CVvNLhZsEjVNmo6_bzR4qhjlM8owKxhMeWWDdxU7c-ZPzdpKigMKlT1pFFcqehgV0FK9mV9L9udhuHXUUlitYeVKSS_MBWnqiLfU-3eXTomgtE41GWB6lPKpk0I6zlXv841_HGMG-6vYPNNBxdd3nejt_47AaafFjZBGFXm-hqPJx3P1NzKvhRRAhlUIB0ZRmUNhok9EpsD2E3p8ylQGw1cP79JbWwGT8sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6b2e5150b.mp4?token=nYu3xwftVtUUt_SFX9ODQxJVWKLfobigYxr_bRdFYd9OogVxb-1hF2ZmMCnnIYsRDGncSCh_IhfMNXEQvJIWttqV9WwDgGfbkqjDcAzWrpZGpxliMy_CVvNLhZsEjVNmo6_bzR4qhjlM8owKxhMeWWDdxU7c-ZPzdpKigMKlT1pFFcqehgV0FK9mV9L9udhuHXUUlitYeVKSS_MBWnqiLfU-3eXTomgtE41GWB6lPKpk0I6zlXv841_HGMG-6vYPNNBxdd3nejt_47AaafFjZBGFXm-hqPJx3P1NzKvhRRAhlUIB0ZRmUNhok9EpsD2E3p8ylQGw1cP79JbWwGT8sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به یاد سربازان تیپ ۳۸۸ بمپور
💔
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/68188" target="_blank">📅 19:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68187">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">پاساز علاءالدین خبری نیست، ویدیو های منتشر شده مربوط به‌ گذشته‌ست
#hjAly‌</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/68187" target="_blank">📅 19:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68186">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hP0LNUewoLQ6gg8nY0L4kRAP_3KLvFvkCLlVNmmjTDddHyl13KuerpREeWfFS_QKwg-UHwt3wrFmocsADOaxMPL4cJZfMjrrZ2Dw5LU4GRquc5-wAH7b-wFD4o4sF933c7LDOmCUz1xneV4BtW8kFEN0Q9W0ZhTWRUw3FYH2jGUq2YA_wE-TybfBeJgB4zOqWbVXxar0lqUhrgNnn_nqFKWmNe-5yX05EfTEYZF_mozitHd2UNRvDjGJ0FgJPujjhf9UH3DD3VABzybUO5U0vVFk30DWMBujyFoYRSjS-WQykV3BnATSIfAL4uAgsWwedyIJKgUlj-VFUB7DgR9z8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سنتکام:
❌
ادعا: رسانه‌های دولتی ایران مدعی هستند که نیروهای آمریکایی در تاریخ ۱۴ ژوئیه به یک انبار غیرنظامی گندم در هویزه حمله کرده‌اند. این ادعا نادرست است.
✔️
واقعیت: در تاریخ ۱۴ ژوئیه، نیروهای آمریکایی اهداف نظامی ایران را در بندرعباس، خورموج، اهواز، قشم، تنب، بوشهر و کوه استک هدف قرار دادند تا توانایی ایران برای حمله به کشتی‌های تجاری در تنگه هرمز را تضعیف کنند. در همین حال، ایران غیرنظامیان بی‌گناهی را که از این تنگه عبور می‌کنند و همچنین در کشورهای همسایه حوزه خلیج [فارس] حضور دارند، هدف قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68186" target="_blank">📅 19:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68185">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uR8gqpfJo7b94633FejyiGdHytX-z57IKoKCzxSgqEzPhsFQ0R-WAudo2kbKZk0VpiNpj2azkKb4ZWfosgSjMoQdHN5Oljb_9FsdnHNmYfyLytInP0-1VyS0rUckVNrvouScSQwGqxfc5bcqkyX9KkYNUS2lORhQIBGdlBYi0eoaGTWHCuyjP66fxSwRDgIRYGr3AOyhuPK8M8wggqJWjH4aGC_6We3V9XvyR2IOinhsXmTm2EYe9_JGzAsfdLPJeSCW03fWRqCSCnBUd3bbIs3FjGsRF7v-zaHtF4dWhw5bKFd7APdGsmdQRLgvDZFXVhauz3n6IXSO020B62CuTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قراره تا ساعات آینده ممدباقر بیانیه‌ای درباره جنگ و تحولات روز کشور منتشر کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68185" target="_blank">📅 18:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68184">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ob4Wyo67ICQrtjcPtrOopGmsezBP0UyaoTREb5FnPgimtE32HF2WP1fcLZdaVVoL00phXTTUdSq2F94IvQFPmCZlczJcvkZN55E1-u-9knY6zwk8iPhwwtn3RCz1pzxkUeFXvo28GbXjJueYm9Nl5IZmyFGn2GQT8q1CWQLtzVpV2LtsHARp91OrJ82BqQflbEkaRAX_O8-l33U6pZLghg1bGw22cT2jLRgzx0omLZeOPx0_F5a1Ru4beJ9MU3YAjfBC71ozqmCghjryGrvW9Vzlnq9uZeBUSqdNG6uJwLWIv5YpcS3wpYuWmqspTKIIl6eBcxdOfgVkuooz82Z2ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
فرماندهی مرکزی ایالات متحده:
از زمان ازسرگیری محاصره دریایی بنادر ایران در ۱۷ ساعت گذشته، نیروهای آمریکایی مسیر دو کشتی تجاری را که قصد عبور از این محاصره را داشتند، تغییر داده‌اند. ارتش ایالات متحده همچنان هوشیار و آماده است تا از رعایت کامل مقررات اطمینان حاصل کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68184" target="_blank">📅 18:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68183">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/68183" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/68183" target="_blank">📅 18:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68182">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DN1fTWCw7fsVOiJ_Og9nARVjIP85FvTN35AB3_WMVWnp_QU5eKnEnVx953FgI7MsS-Z7zhor074DZWOjq-9oCqPTOr34m18J9KI2NgRzjJUBc7SXaJzKrPrVi-0eL4969BVGCCEAfefoOmN6327qxhS1mCSvhsHf0-z9e6GvqSzK_zRP9taK52W5YsPNPehjPb12DcZdIkO_HEEsGIyjTRZtGq6XkI1_lfj0e51WIX3Ges5inb6NoAmvqeHf2ErquOhgYM35re2r8jdNjlu0gnG66lmxpGNT1qZ7NRmfbIWyFx-A1sbBt6WN9m2iGoE_E4iK3LALhX3dzPWtgP3keg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
Stand for Victory |
مجموع کل جایزه  250,000€
🎁
جوایز برتر:
🥈
جای دوم — 33,000€
🥉
جای سوم — 20,000€
4️⃣
جای چهارم — 10,500€
5️⃣
جای پنجم — 8,000€
🏅
جایگاه 6 تا 10 — 4,000€ هر نفر
🎖
تا جایگاه 450 جایزه دریافت می‌کنند
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/68182" target="_blank">📅 18:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68181">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
انفجار در جزیره هنگام
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/68181" target="_blank">📅 18:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68180">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/415d2aa12e.mp4?token=VNQvMk2g1jH77juRN41KiPDtVfJFKrIpObIzlGuYVlaLv0KJewF_-fnRbrEW23MLGMKkvdJhVEzhwkvut5-2JLNhdxOvsCLJiTNKca5pqgOnwz7COtkNLkU1cSdtwTB9VHe9zJ5Q7yP5d5qdGIlgiiJhi2Vbarwm9pYVC5vWsvZb7ieT1FbC9xMyu-Cc-U3so5V6M8M5vUOupkOwUTV960NSWWrZsVwbK8ZbJm6noMidf5fISbOnIrNdx7qyJzFV8JpS9qzgkOSqGjKxZ3zE7Je3jfI2Rst7f-vf5-5EmuiHB_GDypZKcqk4gQImU15t_Fs-oUUF9ZsGhvkgwZpOwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/415d2aa12e.mp4?token=VNQvMk2g1jH77juRN41KiPDtVfJFKrIpObIzlGuYVlaLv0KJewF_-fnRbrEW23MLGMKkvdJhVEzhwkvut5-2JLNhdxOvsCLJiTNKca5pqgOnwz7COtkNLkU1cSdtwTB9VHe9zJ5Q7yP5d5qdGIlgiiJhi2Vbarwm9pYVC5vWsvZb7ieT1FbC9xMyu-Cc-U3so5V6M8M5vUOupkOwUTV960NSWWrZsVwbK8ZbJm6noMidf5fISbOnIrNdx7qyJzFV8JpS9qzgkOSqGjKxZ3zE7Je3jfI2Rst7f-vf5-5EmuiHB_GDypZKcqk4gQImU15t_Fs-oUUF9ZsGhvkgwZpOwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
منوچهر متکی وزیر خارجه اسبق جمهوری اسلامی کاملا جدی اومده گفته:
باید به پایگاه های آمریکا در منطقه حمله زمینی کنیم و صدتا اسیر بگیریم ازشون و بیاریم ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68180" target="_blank">📅 18:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68179">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1331c1b8f5.mp4?token=DpzXG9fSPHjbKMarewUmD2_wURkqiJOo_gxZxNriGB3KtWUGtrz3uXtiF6E42AEqaZatdEF_-uW4wy9E4Fna6qH6R7r-2GM6M_7bJ4tfY1cZ4szLgu0RdpwieA3jE8khJoxp1CP2FhogMI0mrPaSLSMS8rwV7fOkiXzCcf-FyXIgvsTWgm2NXogwHFNRqcPA21RT87A5pY28QdjTzkA4a3T6Ee8IhwF0qKjF7nDhppZZUCYezlf57TLQ8kqsOKV0gjTkZiIL7Dhf11xn8zA5ozbkw5lPT2MikeBkYH_5Z9rogUhItYohmwJL_lv669lIeVildXWH9mwAlyMBcajBlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1331c1b8f5.mp4?token=DpzXG9fSPHjbKMarewUmD2_wURkqiJOo_gxZxNriGB3KtWUGtrz3uXtiF6E42AEqaZatdEF_-uW4wy9E4Fna6qH6R7r-2GM6M_7bJ4tfY1cZ4szLgu0RdpwieA3jE8khJoxp1CP2FhogMI0mrPaSLSMS8rwV7fOkiXzCcf-FyXIgvsTWgm2NXogwHFNRqcPA21RT87A5pY28QdjTzkA4a3T6Ee8IhwF0qKjF7nDhppZZUCYezlf57TLQ8kqsOKV0gjTkZiIL7Dhf11xn8zA5ozbkw5lPT2MikeBkYH_5Z9rogUhItYohmwJL_lv669lIeVildXWH9mwAlyMBcajBlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تمسخر لهستان و شوروی توسط چپ‌کش اعظم رونالد ریگان فقید:
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68179" target="_blank">📅 17:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68178">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7f97b887b.mp4?token=sfNQhCkvvHCaMt2hlqVmCgiVx5F2jQsKDcHSIK4X9iB2c1uAOPCPXh_NN3LoRRXWesEvbT-eCS4IIUm9svXuZneGavRqKHNbQ2uhVLR6fws6dJwpn-J9jqIDQabtQOuRf8ICI3RnuRoOkHs8C_mms1deh3TRDgNsm5QuYG2vjoIcCkF58L1Ft1NYHseiNOrC5AsojEGg8j1PQ3_-H1y_TJ6U9l_YrWentIKJxzzaseK6wfxNX8BjGcSukeJCwrb5gMKIQTXyQek9ZoilWIfsUF3PSGWrK3mY1lrbdKBCfQBEvNfHgKu2aZ5fTv1IGyTUsyVLLpJS1VcTu6RZelVQhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7f97b887b.mp4?token=sfNQhCkvvHCaMt2hlqVmCgiVx5F2jQsKDcHSIK4X9iB2c1uAOPCPXh_NN3LoRRXWesEvbT-eCS4IIUm9svXuZneGavRqKHNbQ2uhVLR6fws6dJwpn-J9jqIDQabtQOuRf8ICI3RnuRoOkHs8C_mms1deh3TRDgNsm5QuYG2vjoIcCkF58L1Ft1NYHseiNOrC5AsojEGg8j1PQ3_-H1y_TJ6U9l_YrWentIKJxzzaseK6wfxNX8BjGcSukeJCwrb5gMKIQTXyQek9ZoilWIfsUF3PSGWrK3mY1lrbdKBCfQBEvNfHgKu2aZ5fTv1IGyTUsyVLLpJS1VcTu6RZelVQhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از وایرال‌ترین ویدیو ها در 24ساعت اخیر در توییتر فارسی
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68178" target="_blank">📅 17:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68174">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H6vUBvSvrAC7ag9skrSbgKXdFhE9dVXhpTtTCFTCNQltQrudVjRsIr7j-z-Xr2n7QK7mSqDTJVxz4nd1AiOKQjAlIggvt1vs63KVcaL_O44D1qmVNhjhnNpXr5Hlrs2-UVYDkd3r_BwLLvRhi3VTL-U9bu1bD9JrqG_nSyQiFHfFS2Ove3ZVoNd_4ZI51IM5dixTf6mu4ztfZuRbfhfsJ0nU7iNe6zbP0nCBAPZh9bdnq3ulk17-vj-Gv30rEs9xqFgmY5Sao-12eyHHWA-lEKRGhXQy_1T-WSJrBmnJvMNrl8qm66Y6SN_Yv5TnEp-XCmU7tYp012BtmLhOsRIyjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5effcc1b8.mp4?token=iGSXB96CpjZjj9cKcYHcpTLYMwAxlYsIB8RlanXlnzaO1L-7HcLL8EhpdCwxYobxlmiTNLX6YLuJB7PsdT-n9yiT957PIdzNsP6kaLo4uQIUt-8NYa989YyD9pt8jQFr9SI1HH-wuZ0W0jR_EAUqTPD5V5zxFrC2j6eReGHVxXWPFHF1e--pNAHr0rm4UH-j9VAjQbBNUxegMkrglu-oBCqDpAcEKmMhrVh9WRiTo8gGZTvw9LJaMj41_ZhnpK_UfzKhmYFXzqXnzH7yzYA9bZJDPBipoILLAC6h7elNxSLrLJ9nlYc73yS5XS2WJdfubqAaw1tExuXcD7-H1gNEzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5effcc1b8.mp4?token=iGSXB96CpjZjj9cKcYHcpTLYMwAxlYsIB8RlanXlnzaO1L-7HcLL8EhpdCwxYobxlmiTNLX6YLuJB7PsdT-n9yiT957PIdzNsP6kaLo4uQIUt-8NYa989YyD9pt8jQFr9SI1HH-wuZ0W0jR_EAUqTPD5V5zxFrC2j6eReGHVxXWPFHF1e--pNAHr0rm4UH-j9VAjQbBNUxegMkrglu-oBCqDpAcEKmMhrVh9WRiTo8gGZTvw9LJaMj41_ZhnpK_UfzKhmYFXzqXnzH7yzYA9bZJDPBipoILLAC6h7elNxSLrLJ9nlYc73yS5XS2WJdfubqAaw1tExuXcD7-H1gNEzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیوی منتشر شده از انفجار در چابهار صبح امروز
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68174" target="_blank">📅 16:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68173">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d7965cf40.mp4?token=GAcHVddQ0TcCc0txJzY831UeSdUVETPR6B2oLACegRrnhVT7qxx2OWMxGo9KhxfS_X4jyoOwfx2xdQ-3PgJ8e-IGf47e5RBXkh3bA9mIy3gQhT1yT5eRJVCjH2GS7Fwm1PxxsvvoX95j50rz6mOXvdN79YTLdglgNoUNrAIB7oSZtNkRMAqeZPnu2sVG57W0DCaStm3Yf9Tkakn5G2lFTxZ55kFPDeLNC-plFNloMI3nGhOBMnw60tpD2lQWpq_Un5sd-__C_mjXlIwd0O-02rGLEjO8EW-raXKErxOyeyi47p6jY9WQunWzMefNFCHLvhFdWjSyVDa0bWXN_b9pJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d7965cf40.mp4?token=GAcHVddQ0TcCc0txJzY831UeSdUVETPR6B2oLACegRrnhVT7qxx2OWMxGo9KhxfS_X4jyoOwfx2xdQ-3PgJ8e-IGf47e5RBXkh3bA9mIy3gQhT1yT5eRJVCjH2GS7Fwm1PxxsvvoX95j50rz6mOXvdN79YTLdglgNoUNrAIB7oSZtNkRMAqeZPnu2sVG57W0DCaStm3Yf9Tkakn5G2lFTxZ55kFPDeLNC-plFNloMI3nGhOBMnw60tpD2lQWpq_Un5sd-__C_mjXlIwd0O-02rGLEjO8EW-raXKErxOyeyi47p6jY9WQunWzMefNFCHLvhFdWjSyVDa0bWXN_b9pJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
فرماندهی مرکزی ایالات متحده:
فرماندهی مرکزی ایالات متحده (سنتکام) در ساعت ۷:۳۰ صبح به وقت شرقی روز ۱۵ ژوئیه، دور دیگری از حملات علیه ایران را به انجام رساند.
سنتکام در جریان این موج عملیاتی ۹۰ دقیقه‌ای، با استفاده از مهمات دقیق‌زن، سامانه‌های پدافند ساحلی و همچنین محل‌های نگهداری و سکوهای پرتاب موشک‌های کروز در جزیره تنب بزرگ را هدف قرار داد.
این حملات توانایی ایران برای حمله به کشتی‌های تجاری در تنگه هرمز را بیش از پیش تضعیف کرد
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68173" target="_blank">📅 15:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68172">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e23686eac2.mp4?token=IT88yN4UDZRYpsHBCggdFRecSUvZvR6f24dVLSuzFxykh_bdvo8I5Cqn5oPVouifjgWxfTPnWj3mq56KMQLPPOkG3Oq2tpOeahZn2QWvnmbmb6w8d_Ua5NP8oYH0iTpuXGHKGVkoFSz7Obos_rGSRFgOCEWLA-0TBUxNLvJUYtD2CsSWM9r3iO5BmyWJdxyFiLmTL3DTrrlMg38jkEBt1ITADpfFxNs31xIrT0bNRik_A5tbEfyIYdkNYT9AETCHJd2SpuW-gzfVUzxz0YzsNEVx8XsT3wxPjVx39220WJEOL7bLOyfmjTzPS-O3IJelFxAf0vRmZgAkgRffsQT_GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e23686eac2.mp4?token=IT88yN4UDZRYpsHBCggdFRecSUvZvR6f24dVLSuzFxykh_bdvo8I5Cqn5oPVouifjgWxfTPnWj3mq56KMQLPPOkG3Oq2tpOeahZn2QWvnmbmb6w8d_Ua5NP8oYH0iTpuXGHKGVkoFSz7Obos_rGSRFgOCEWLA-0TBUxNLvJUYtD2CsSWM9r3iO5BmyWJdxyFiLmTL3DTrrlMg38jkEBt1ITADpfFxNs31xIrT0bNRik_A5tbEfyIYdkNYT9AETCHJd2SpuW-gzfVUzxz0YzsNEVx8XsT3wxPjVx39220WJEOL7bLOyfmjTzPS-O3IJelFxAf0vRmZgAkgRffsQT_GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از جنایت ۱۸ و ۱۹ دی ماه؛
تا مدرسه میناب و پادگان بمپور؛
نام‌ها عوض می‌شوند
اما قاتل یکی‌ست:
جمهوری اسلامی؛
حکومتی که برای ماندن؛
ایران را می‌سوزاند
و جوانانش را قربانی می‌کند.
#hjAly‌
@News_Hut
|
@HutNewsPlus</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68172" target="_blank">📅 15:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68171">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H9U_oAPDcSDV1FjtcxBURg4-oJAr3ovbDFjNvqSy2tTOLR4m8OX3QtU4hpKFvpo-pdtce7i5nj5X9dUa53K6rMpNIsVJV8ra2Kne_sedwT-NIvBeipgncOsgzNFcsIV9BG6yzlfEJpr_C22s7h2Bjbll8f8SmzhKReiHBU2hHwewQlB_xXr-kEGSG1JDNrKfxpFAWn1R0P7t4aZ8Yc2d2dl7Ui71ZPgzWO0LDtnaoXN8rLapxE1mtoc9JSvpcig2OA4NfOdb-hP9osrYFj9wTK1gOsESaHO7btqKb2WWLXc-4IMPgsEcQwnW-Z239uXEsoczqNqbtzbLT9WfrfQeJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری حامد‌لک:
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68171" target="_blank">📅 15:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68170">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a4GB5Q3fZdIliLX4rtLy6xruUwrd_cpmE6YhR21MAgr9T5YwJ2DWFQSswiveD0D-JZ1IIJ7lZKfvX0iaLYeMSs5cxilurlyeQplxcv6jv_OAapHNhK6mhHE7stbBXc5HmyfcndbWBS39krLVHv19idAN-L8dhP2MRxgyV4aMoErssqAhxPSBVsYW0Kwh-EsPHRAuNaTl-_b_dNIuUXpNNphUUSnutdi6-vzbC5xp_qEc9eGgKdumP0E9XmykMmiikLY4rMU8hGbntwGpXZHpBpTmTQJvfq1wtPIOw0jwsj0gaQyeTv6h8bdXVkndV-1tgy5WD7EA6DBH6wXDbiyQzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
چهارشنبه ۲۴ تیر ۱۴۰۵ جام جهانی ۲۰۲۶ مرحله نیمه‌نهایی
🏴󠁧󠁢󠁥󠁮󠁧󠁿
- انگلیس - آرژانتین
🇦🇷
ساعت ۲۲:۳۰
ورزشگاه؛ مرسدس بنز آتلانتا
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68170" target="_blank">📅 14:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68169">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
پنج انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68169" target="_blank">📅 14:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68168">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">علاوه بر اینکه سوالات یکیه و باید همزمان امتحات گرفته شه، تسنیم اومده گفته فقط نهایی دوازدهمیا تو روز ۲۵ و ۲۷ لغو شده، این درحالیه که دوازدهمیا اصلا ۲۷‌ام امتحان ندارند و یازدهمیا دارن!  باید منتظر واکنش رسمی اموزش و پرورش باشید @News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68168" target="_blank">📅 14:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68167">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZaACSUzUPRYjRPFCs0eGm6Prc6i6ZYgxVWbaszEGsu10jwGNz4JQ8MSJ7PIIsLKZSEQBP39hjDQVRLSoWJ9zFkbLheGBYE-0h7BMl6KFlPFxVhv8DmaA0yTPNQTcG-cB5XUJ4eajt5ErX7JuLiIjj1vctbqiSswoIPEaDC_Xof9hhcPqm24H-SM8UPUbjmC7LWsZhp4WMRjhprkuK8no9OoUyohbCxVkrVY2LWDWTEkx7JYMurQUPbxlI8Tn26OGXe5jrXH6CFVKMMbEKuSFJaX7_5a1px9y2LkeatNIeSY67K21xGC4v8qoT_RNgYOtMkeDe7aILT49oC-0lBeQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چطوری نهایی رو فقط برا چند منطقه لغو کردین، کاش این دو روز کل ایران رو لغو می‌کردین تا فاجعه‌ای دوباره مثل میناب رخ نده... #hjAly‌</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68167" target="_blank">📅 14:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68166">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce063673b4.mp4?token=Mds_pG4trX084_c11qwu56DScAd3-VxupTWDo8j1pu2RofM9EFwOcrpKo3XS1YUupZpukEXoArWrRh8byKqkvaXlwGzJ90PKYNidIn7xdDQJrfQQUZe2rUj4kX6WXuILAi5VU6r7qYk11hgP_mMNSsl9Ofq1pZCn7ryKJrMxcYJFkZMKDgYqKZHOBNlzJjnhMoIOR9P8aByHN_UsQ5bv0WoMNUaxbZsmG-eGloHmPjrgdtHEVidBmBp9X2BBgwJb_Lm-5GeZpvkOpnBXYQCTuy_7AurjNqicnOMDfCo8fwbakyHwof0D1pfGG_AsJeOmQU1azRXW1Gmkbr-jpzWZkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce063673b4.mp4?token=Mds_pG4trX084_c11qwu56DScAd3-VxupTWDo8j1pu2RofM9EFwOcrpKo3XS1YUupZpukEXoArWrRh8byKqkvaXlwGzJ90PKYNidIn7xdDQJrfQQUZe2rUj4kX6WXuILAi5VU6r7qYk11hgP_mMNSsl9Ofq1pZCn7ryKJrMxcYJFkZMKDgYqKZHOBNlzJjnhMoIOR9P8aByHN_UsQ5bv0WoMNUaxbZsmG-eGloHmPjrgdtHEVidBmBp9X2BBgwJb_Lm-5GeZpvkOpnBXYQCTuy_7AurjNqicnOMDfCo8fwbakyHwof0D1pfGG_AsJeOmQU1azRXW1Gmkbr-jpzWZkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
خسارت وارد شده به یک دکل مخابراتی در بندرعباس پس از حمله آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68166" target="_blank">📅 14:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68165">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
#فوری؛ امتحانات نهایی رشته های تحصیلی پایه دوازدهم در ۴ استان لغو شد.  وزارت آموزش و پرورش:  بر اساس تصمیم ستاد عالی آزمون های این وزارتخانه و با توجه به شرایط خاص کشور در استان های هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، امتحانات نهایی تمامی رشته های…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68165" target="_blank">📅 14:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68164">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
#فوری
؛ امتحانات نهایی رشته های تحصیلی پایه دوازدهم در ۴ استان لغو شد.
وزارت آموزش و پرورش:
بر اساس تصمیم ستاد عالی آزمون های این وزارتخانه و با توجه به شرایط خاص کشور در استان های هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، امتحانات نهایی تمامی رشته های تحصیلی پایه دوازدهم در روز پنجشنبه 25 تیر و شنبه 27 تیر لغو و به زمان دیگری که متعاقباً اعلام خواهد شد، موکول می شود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68164" target="_blank">📅 14:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68163">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TNfLPGHrChmYE0XxCRwd5-ONVfT0mJvVcilHceMGGuu2MGQ_lMxoiqeHyLC7wMuHmzEnFz4amiTxceGcKHqaWR-s6gTommxkloLavMlrtEFOvPN1CExz3DJLIUhu9EWnaa2eSloeEOOIoM6HUogqt87NYJojhW3k6PgkSweLn_564LAY8yesJ3z5LcWIaHJYBjzjEX3euqmvYYQDLGrN7hDtcKEhO5cNRGIvpqoYm8T8eP36BSijEG8_ZdaKJRqmRhxJmv3oojN-znq-ZFoQawbETK0OnI8XcGyXwoRW3xzNupqSDXuoo-xLJuaapdx8YKtT7LDONlaZmsMuYDgB1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فرماندهی مرکزی ایالات متحده:
امروز ساعت ۶ صبح به وقت شرقی، نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) موجی از حملات را علیه ایران آغاز کردند. هدف از این حملات، تضعیف هرچه بیشتر توانمندی‌های نظامی‌ای است که نیروهای ایرانی برای حمله به کشتی‌های تجاری در تنگه هرمز به کار گرفته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68163" target="_blank">📅 14:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68160">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ksh5DwHDEp9dUUxh7-3txkSL1VIQqU-QGf9EBYvgRhdwf7z7okgaN-EbP45x_ZghRubDeSr4nKxWRtodSzHRzuDl01WkPmNDUmT9Dp3wG-K2xfzxjFHGux7tdr-6cd5FXJLvhVqm21MBXgKTRQ01wJiq5TsccAQHranQwEJVJWQgLls8BNtlUhAmzh4eobw4Muq4gDRJ7nI7zHvn_oKPAXsNtxwrvyuYV3LFkRbMilGWPs0jM49tsNc_wYP0Xd1Ae_uLuR8A-lqpsQuWTJecNWVmQLSvnaGJKAWyoa7sZLkOjQ3IZ5VLe33F42AsKRJtG7hAIjEONFWv5Dp6RKBJrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZjekEADr6zLj2rXbHYOPoYA9Kl95yzI3VnlLbQYAH5auHEs2BbthuOYwgU-3sjun24csW8k_ICq1SZdQWqWq_213CxatPg4JKnl3Ev5eUhRVsPLXrURKnv_fWKnEXdSjZG0HQuWO-nTR0Nxt5AJKQcmW3q1hB9wx0oszk5jp0HjdTJYpI5cdgl66wUqV3Nsy__yc7Spe7NuzPBLhaJcfrljY49S1_1VtxBFtAUcrA1ouzahy8Hkp9t2S2aLBIRPXFMkSAf_uCulvgqXkUrd0iMdpDf1Nkjgb0wDU9RXnV3iXHOBtM6nQFnp-FBT6V15zoFLRO3yqHHWxRe9b0CUwgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a57f3aee50.mp4?token=bzrf-nI4mjzQBmgGoWE_Un4cyuyS_UZotK_aFeh4Bavl3njgAHGPFHjuNdXGa_WTKnXvaz-FsikzOlkyOJjh98_n2DWmR-bDXZq9CEJOQDTfYmzNEuTJt-EGJalw-uAexeCi3qOJDOIQA5doLvMp5Ii_YENhBLWG-TIRrocdklC24oLbdeJTrThn7GMZik-PRGaMtvlGDdczu8kkzL9dIaIlLhD22zXQ0OLhXy_3bH4YEVQKKIUvgRBsHpwnxJmVYMZMGdkJ1o45EAtBu2Z7y8ikfR-Ezv4TXHj3Uhhn-Yfconr4OkDfzPG7McqLnSEMt_i0NVJ2Jd5WXHk8qCHxPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a57f3aee50.mp4?token=bzrf-nI4mjzQBmgGoWE_Un4cyuyS_UZotK_aFeh4Bavl3njgAHGPFHjuNdXGa_WTKnXvaz-FsikzOlkyOJjh98_n2DWmR-bDXZq9CEJOQDTfYmzNEuTJt-EGJalw-uAexeCi3qOJDOIQA5doLvMp5Ii_YENhBLWG-TIRrocdklC24oLbdeJTrThn7GMZik-PRGaMtvlGDdczu8kkzL9dIaIlLhD22zXQ0OLhXy_3bH4YEVQKKIUvgRBsHpwnxJmVYMZMGdkJ1o45EAtBu2Z7y8ikfR-Ezv4TXHj3Uhhn-Yfconr4OkDfzPG7McqLnSEMt_i0NVJ2Jd5WXHk8qCHxPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تصاویر منتسب به شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68160" target="_blank">📅 13:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68159">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AuKrZKCJB7KgzYzEUliz5C5bz_mzibs2G65QIhI0SpHKY1WNeUcP_mwwtDErXlQOq_ziprrteWu9lBzj5nXGcuEnMiUq2vAlwbSxxSZsg6_pEH4fv-65ijFfEvw1NWkLMc1zpsRkFVZnc4N7LW8MnsxtbmbWLqLxK2X_egSOp9-LlSefHKjsNWK5mW15dhiNUomV-PUuI0xg3sKDpTtMi3D4Np8H1KbhEZPA5gE1OaI8pcBsM7l11OcOKXjD_53TPFMLr8XZDLNQE4j62tyZmVV_AJxWkLIRpQVinUhf7vRdwnhSl6Tt18QC8gryzV49seQx5OQGavIRp1Z3P2Gs0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
گزارش های اولیه از انفجار در شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68159" target="_blank">📅 13:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68158">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALpg5ws031rYGAHSOxrUzP8R5EYrlA1RSR7TgeY5yqY1evwp1BsRn4m_5CBhKhHQ3QQAFm_Cpl5mCpcyT-NsV0V9SpDjqtvKDKnm1h_cQ5G426cu-MiRdzEyBdF0G-aEuBPCxZ6eyG4ZlUdA-hZUk4M40JNfdosI86oXmPtH_kdX-wFcoPoRgU6CV2-8vNkHziAQy0Z-xB4MboYIkyksMVc6N0KBUfe_PafTLKj03vysVm8ZEAnLXyvXFmmmbwuf1svYCVN95keVPJqQWCEEYODlxkVV3rSgxd-Wu2GQreFG3VQ3tni-bML5JYCy2E6kHrRzOjhij-oRtQ0IgFtpog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مادرِ داریوش فرضیایی (عمو پورنگ)، بعد از تحمل یه دوره بیماری، تو سن 90 سالگی درگذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68158" target="_blank">📅 13:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68157">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">‼️
امریکن گات تلنت یا همون عصر جدید آمریکایی ها
یک شعبده بازی توش انجام شده که حسابی وایرال ‌شده
👀
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68157" target="_blank">📅 12:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68156">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qeu8ByltkWxNvChZHVLgo96fszX0VP9P3cPdGvQpO9hsEKnRPbZdvphEqTl7V_7hCjNzUVpE_4Mz6cRP3DgUb0qqgOGsK7ATq-4AsIPYqf7qs3o5xGYahU8daLxfHiekLMBLQACxPdDP7GAUmrDW5cIhs1CiPTLSkX7XUq6lUpjB0QCEoVrikCEMWyo966rfjmz0uFRZHh4Nntm5r0qIiP8FSxxTiNWMrhkWFFa2aJmp1IUzYy-NQTQVgCbyDa_lq2p8dhuW6E-vZ-iaDLGG_LAQzGhmGn6B40qpwIA331joQdU2evjKU3uPQzr8vPUbjTKR5EFpNffRJ0XAIU1r6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ا
کسیوس:ترامپ در «اتاق وضعیت» جلسه‌ای درباره حملات جدید و گسترده علیه ایران برگزار کرد.
به گفته سه منبع آگاه، رئیس‌جمهور ترامپ روز سه‌شنبه جلسه‌ای را در «اتاق وضعیت» (Situation Room) برگزار کرد تا درباره یک عملیات تهاجمی گسترده علیه ایران گفتگو کند؛ عملیاتی که دامنه آن وسیع‌تر از حملات کنونی در اطراف تنگه هرمز خواهد بود.
به نظر می‌رسد ترامپ مایل است جنگ را تا حدی تشدید کند که خسارات کافی به بار آید و در نتیجه، حکومت ایران تنگه هرمز را باز کرده و خواسته‌های هسته‌ای ترامپ را بپذیرد.
ترامپ این نشست را در حالی برگزار کرد که ارتش آمریکا برای چهارمین روز پیاپی، حملاتی را در منطقه تنگه هرمز و در امتداد سواحل جنوبی ایران انجام می‌داد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68156" target="_blank">📅 11:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68154">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb5c420396.mp4?token=QxmPwYUSWsmt_VxNxkdGtiFSo5NkFgIUkWzh2fWIk_Ef2P4MMTcFg3F2SXhBWz69hcrBwstFVMXbGqE1vy0mEL6TrHQ2pFsoDmSv2UWhNVcUk5SpUffv18nOOIwHJHrkoCobOGl4D5U7I5ffSciS1R5XU5W3I5SZq3CL-GKqu4ihm8hEOrnxXRd1ts1TxkLV2641hOHWbrpY6MoOZziech8fbMHLvppONQ_Tcl1QPYhyGg34PozIOGnVxcsrpEOMVwyiDPVnRCjWpAf00OTVFKHXNU6rnWvnF531mp1pUbzIWkU_9mXXgADLcyi5V2o24xtOVTCNlUa2h2bZ3s7RnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb5c420396.mp4?token=QxmPwYUSWsmt_VxNxkdGtiFSo5NkFgIUkWzh2fWIk_Ef2P4MMTcFg3F2SXhBWz69hcrBwstFVMXbGqE1vy0mEL6TrHQ2pFsoDmSv2UWhNVcUk5SpUffv18nOOIwHJHrkoCobOGl4D5U7I5ffSciS1R5XU5W3I5SZq3CL-GKqu4ihm8hEOrnxXRd1ts1TxkLV2641hOHWbrpY6MoOZziech8fbMHLvppONQ_Tcl1QPYhyGg34PozIOGnVxcsrpEOMVwyiDPVnRCjWpAf00OTVFKHXNU6rnWvnF531mp1pUbzIWkU_9mXXgADLcyi5V2o24xtOVTCNlUa2h2bZ3s7RnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
لحظه برخورد پهپادشاهد ، به طور مستقیم به یک انبار در کویت
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68154" target="_blank">📅 11:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68153">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/povRRdOhRVUQWKE-cPY8rnEdwmgTXUsbVW5oXj_acEcWiZU7g4WekCJA8vCxw_6IMjjT1AW7_1ojHK_x6xVR-CBdB3QZkhh6Nh7zj9PyJcIH8gjt47662rL7KX1JOjdYzh4sxCRs_QZT_orJRYFRFQPetOwze3bvNnRvWTSDn3ldtnwuUAnOONap6Wi3dp6i0wlw7fmCmE4jZL-P6rbnHANODw2BQRWGVmxF6GnQVOdAKCVTRe7sy1moN3XrcK1X1lgb18orVII0UB1zSjbenFr1B3dvqV33mGfJmMvgqlVXlCgK9nxEJW7ctGMAOFc5DNZVQD0kIGdww7F_aYXWlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عقل بچه‌ شیعه‌ی آخوندپرست
🤯
🤯
🤯
🤯
:
#hjAly‌</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68153" target="_blank">📅 10:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68152">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31c4cf4b27.mp4?token=NYj5B3CBV-YY6D8wBJWaRFRJVmdQiKQSoqwkmZA30VtJzfUDnV4E1C1S2vUQUtyIJoZH_U2bFgfvQnXJIagjXiyFolsEBa3bAodRlkHzDivyHGUS5jOfFEZuINV6bqGWa_xbQoBQW8Fp8CPBTKUb5o-_lKEr6B3E_z0tAzwiaoxKCdldr5OZapoOq8joHiG_xczXlkZ6NdrCCgr6VtzntnCEbd-fFANwFfticRvXPf49jPXTMWM5oOU5asOCojd02qLYX3JExQurS22liOhD3a_W6RqdMbEZh3mr0t-hRHJeMrpdOcGA_sDI2xlS-NbRj87mNsNo3L2JsTLH5UzEigXacqjU29oykD3TOvnIwklasFEp_CPGvMuY9qblfjZUxN5gHjyBSwNATtUMzi8T2Ug7uhEeZdvSE4nTScRVRIfrJIuf_V7er66Uwz7OXeFOyp_XWI2d7Yu1TlbNTBAjV6Pm27nT5bO1f2bM75KNOsoqZXc9gvv7RERdQ-Me8JKlIjt5WvQL1VCcSwAMHZkRQlGyVdK5mwkxXBive1Q1h_bmZqDNKdS16QVvgJl7vdgad1gCIBfX-503xuE1D3SnXPM4VJdEYzZWaa0I9dotbGfXvdD9vZDSRhhbHVM6OhgNBgV04jL8wPLNQ9tuf8vzXJqZf-ctkClkuclWgaNYpbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31c4cf4b27.mp4?token=NYj5B3CBV-YY6D8wBJWaRFRJVmdQiKQSoqwkmZA30VtJzfUDnV4E1C1S2vUQUtyIJoZH_U2bFgfvQnXJIagjXiyFolsEBa3bAodRlkHzDivyHGUS5jOfFEZuINV6bqGWa_xbQoBQW8Fp8CPBTKUb5o-_lKEr6B3E_z0tAzwiaoxKCdldr5OZapoOq8joHiG_xczXlkZ6NdrCCgr6VtzntnCEbd-fFANwFfticRvXPf49jPXTMWM5oOU5asOCojd02qLYX3JExQurS22liOhD3a_W6RqdMbEZh3mr0t-hRHJeMrpdOcGA_sDI2xlS-NbRj87mNsNo3L2JsTLH5UzEigXacqjU29oykD3TOvnIwklasFEp_CPGvMuY9qblfjZUxN5gHjyBSwNATtUMzi8T2Ug7uhEeZdvSE4nTScRVRIfrJIuf_V7er66Uwz7OXeFOyp_XWI2d7Yu1TlbNTBAjV6Pm27nT5bO1f2bM75KNOsoqZXc9gvv7RERdQ-Me8JKlIjt5WvQL1VCcSwAMHZkRQlGyVdK5mwkxXBive1Q1h_bmZqDNKdS16QVvgJl7vdgad1gCIBfX-503xuE1D3SnXPM4VJdEYzZWaa0I9dotbGfXvdD9vZDSRhhbHVM6OhgNBgV04jL8wPLNQ9tuf8vzXJqZf-ctkClkuclWgaNYpbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آخوندها عُمر طولانی دارند و بیشتر از عمر متوسط ایرانیان زندگی می‌کنند:
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68152" target="_blank">📅 10:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68151">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1084df804.mp4?token=LE2DAcYnvmM80fjo-xjNK3kvFe8HGK4YnOIu6kYieEJ-56-P1y4yuSZAJt46fl3UnhQWr3JsM_-Mred-XL5O2dPHZLkPikOLLtqdJdtdcbJXVaFGNWwrsAk-d2LAqjJXOCU1MQGRwDpnsH0T1pNu4fDBp1Y2TW7ozUfkixn7eN8v9oqNKg7e0O-5mzOfmLeOUGGo6KuZuUhdplXoS5e1a2nidJqlbB_PgKfi6K23k4H4qH6WWiz0mNXWJvVw13ktVst7eBrfZT46nEDoDVeuTSACbAMk8KRhw_EYaaN2ayqsyO3wr7BQrVzXhvwLBvwUfbw6Bbq2V5Sp52-obmxJuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1084df804.mp4?token=LE2DAcYnvmM80fjo-xjNK3kvFe8HGK4YnOIu6kYieEJ-56-P1y4yuSZAJt46fl3UnhQWr3JsM_-Mred-XL5O2dPHZLkPikOLLtqdJdtdcbJXVaFGNWwrsAk-d2LAqjJXOCU1MQGRwDpnsH0T1pNu4fDBp1Y2TW7ozUfkixn7eN8v9oqNKg7e0O-5mzOfmLeOUGGo6KuZuUhdplXoS5e1a2nidJqlbB_PgKfi6K23k4H4qH6WWiz0mNXWJvVw13ktVst7eBrfZT46nEDoDVeuTSACbAMk8KRhw_EYaaN2ayqsyO3wr7BQrVzXhvwLBvwUfbw6Bbq2V5Sp52-obmxJuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
پیش‌بینی پروفسور جیانگ از تهاجم زمینی به ایران
:
پروفسور «جیانگ» تحلیل‌گر سیاسی مشهور در گفتگو با «پیرز مورگان»، مجری معروف انگلیسی، پیش‌بینی می‌کند که «نیروهای زمینی» آمریکایی از اوایل ماه دسامبر در ایران مستقر خواهند شد
.
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/68151" target="_blank">📅 10:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68150">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f38pz66Lxl-EHaoKj23MC6xffeqh0bxSS9YWVj1HATOYOOA7XOy2QjvDWnTLBcPF5pWRGtEzlIabP-NnCis8qxhoKG5tqCxv-VzwY9R6reb-_5mJpVdHYx63q49aZueqd7J4hqCHh9B7V9hj7KWD4WUY0hRaJnqmPbCRjqE1DlBHhw6N_lUk3YzlH9nwYUcih409K8CAyttS95AhYIKD7Rh56YNTKdSU8IpUaQNqqDXh7RGegI7QbULM1iMg5pxKdJv8bCwzM_tbB5rBcxWukm9VUGZUMzwjENP9Mjv8sruBJE2-7IYljpoThxoMmxD1i6jMoKiZPg7ZiLv8gpWQHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ترامپ: کوه کلنگ ممکن است یک هدف احتمالی برای یک ضربه بزرگ و سنگین، درست به درِ ورودی باشد.
کلنگ گزلا (یا کوه کلنگ) در استان اصفهان و در نزدیکی شهرستان نطنز واقع شده است.
روزنامه تلگراف پیشتر گزارش داده بود که تأسیسات تازه‌ای در مجاورت کارخانه هسته‌ای نطنز احداث شده است.
این مجموعه در عمق ۱۴۰ متری زمین و در دل کوهی به ارتفاع حدود ۱۶۰۰ متر، موسوم به کوه کلنگ گزلا یا همان کوه کلنگ قرار .
ارتفاع این کوه تقریباً دو برابر کوهی است که سایت هسته‌ای فردو در آن ساخته شده است
.
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/68150" target="_blank">📅 09:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68149">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93235f7cc4.mp4?token=UhqIRbXP3jZ0rT_6Jb3s0yO6hzgAYZBhpXwsNViHU3QMBrnr11EP2TdXC11XOTKYV8L6b5-bTuT_SLHTJp_8_LNj42GVuaDxqYkc5In9ucQQ5Cu97RP5d8oRi39iMPGyoSfm3FqaI-f8dDqFiZx2CKfPVZM_SxMmnUS2jykiJhlq155rIy5h5RcNWSxUrKBZyOzssVwR9VwzEtaI0mW4KSlVZwauNso8B0ElLEDgZ4Bxn-cFqd8bmilxp8rvbaPGBA8JfA1JjVI8RqerXuVI0KSn4pFefirna10AkftAn2EkAfbKISlduFCRlNV9pbUP_vtl_l25UryYP041UTaEXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93235f7cc4.mp4?token=UhqIRbXP3jZ0rT_6Jb3s0yO6hzgAYZBhpXwsNViHU3QMBrnr11EP2TdXC11XOTKYV8L6b5-bTuT_SLHTJp_8_LNj42GVuaDxqYkc5In9ucQQ5Cu97RP5d8oRi39iMPGyoSfm3FqaI-f8dDqFiZx2CKfPVZM_SxMmnUS2jykiJhlq155rIy5h5RcNWSxUrKBZyOzssVwR9VwzEtaI0mW4KSlVZwauNso8B0ElLEDgZ4Bxn-cFqd8bmilxp8rvbaPGBA8JfA1JjVI8RqerXuVI0KSn4pFefirna10AkftAn2EkAfbKISlduFCRlNV9pbUP_vtl_l25UryYP041UTaEXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
رسانه حال‌وش: شدت انفجار به قدری شدید بوده که در لحظه اول حداقل ۱۰ نفر کشته شده است  @News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68149" target="_blank">📅 03:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68148">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
تا این لحظه ۲۰ نفر زخمی و ۲ نفر کشته شده  @News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68148" target="_blank">📅 03:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68147">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
تلفات امشب نیروی نظامی در بمپور</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/68147" target="_blank">📅 03:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68146">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
تا این لحظه ۲۰ نفر زخمی و ۲ نفر کشته شده
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/68146" target="_blank">📅 03:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68144">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a28218ed6.mp4?token=iWMTcxmM0zBNSNz9opUvvQ8-PzTl1mp6iZxvFA-xCnWREdFAvdU1ImbFTD2QWjJwyAotdObh1aQ60ASDNcGTBrJwd6d8h8touAb0H4ObFwjmOEyILGis6e3AIajXlO-n0tfGCWvjh7qoJt36vSUu-XtdTa9zhwK6jZtE9Z1WaoqbglrnS0gaMgl-b4JBN4GMLS8WMmnYZnfYY01UuFMmUuxGtvJHh2wGY6Er-ZL5HLdxdxgn5A5eOti4uXYrOZ3WQ4-oUqve3YKY9VMIoIoBg916h2dm_pE8vgqBLSmy254jMr9aJIh-uyJLBhMG0fhXT6PvWHUoc6OqV0qwp77wHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a28218ed6.mp4?token=iWMTcxmM0zBNSNz9opUvvQ8-PzTl1mp6iZxvFA-xCnWREdFAvdU1ImbFTD2QWjJwyAotdObh1aQ60ASDNcGTBrJwd6d8h8touAb0H4ObFwjmOEyILGis6e3AIajXlO-n0tfGCWvjh7qoJt36vSUu-XtdTa9zhwK6jZtE9Z1WaoqbglrnS0gaMgl-b4JBN4GMLS8WMmnYZnfYY01UuFMmUuxGtvJHh2wGY6Er-ZL5HLdxdxgn5A5eOti4uXYrOZ3WQ4-oUqve3YKY9VMIoIoBg916h2dm_pE8vgqBLSmy254jMr9aJIh-uyJLBhMG0fhXT6PvWHUoc6OqV0qwp77wHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تلفات امشب نیروی نظامی در بمپور
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/68144" target="_blank">📅 02:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68143">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">حرفای امشب ترامپ رو گوش کردم، یجا گفت فعلا نمی‌خوام باهاشون مذاکره کنم، تهش گفت اگه تا هفته بعد نیان برا مذاکره پل و نیروگاه‌هاشونو می‌زنیم
😐
#hjAly‌</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68143" target="_blank">📅 02:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68142">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">از تبریز دارن اردن رو می‌زنن، جالبه از پایتخت اردن تا مرز اسرائیل فقط ۵۰ کیلومتره، ببینید آخوندِ گنده‌گوز که ۵۰ ساله می‌گه اسرائیلو نابود می‌کنیم، امشب جرئت نداره ۵۰ کیلومتر موشکش رو اونور تر بزنه :))))
#hjAly‌</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/68142" target="_blank">📅 02:38 · 24 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
