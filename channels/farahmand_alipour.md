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
<img src="https://cdn4.telesco.pe/file/YnJ1ZbuvPz8H1VbPaMNROje7lSqP0dsEWVsid2zpqear60J3CKMUXMZD4gZpPXFU6b_pF5AAAEtACItld6mIa_nF54x9hOdaX0J4Olp307Omb80wYNmcKLst-G-Ro2VWjMPJrAnmRDUsHO0IkINBEkK2HZBAT4OJFoRYiGQ34DMBkFOsu_mMfJshxNerIGNVrdC76nKIA0dxuOpnDLtsOxtAt4YwvZqiBQRL9YN4_pqZZaNRJpT_hPWayaWzitH93qLN78qfSXKT3M32FmJBBY7Mmt_g_kcLjlVo5dmfjUoGkmJDkJ6iAdEBdJBlfK0cpZbdzIZ6HN2xXJcaotOeKw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.1K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-27 16:01:22</div>
<hr>

<div class="tg-post" id="msg-6748">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=GFwINfV6g5amFzus_aTWpLZn2kYItUs1TN5n8UUWO0sO-2xBeSpitN0yp8h6Wp1xQtIu1oRIDfln046ZhxpIkpIkGpTJ8IJa6u_8-1VyEhxPA_HcAGPLFbKesIwY3lVGGRfsJJpsk5eb_BBkKDGbki7Uwmq4pCLMpxAkOo1xMhHwtZZUgVzA_o8A4IZH4qVjqiPCN0pQueDPpXOS3Tk3G-GATi0TV1m5g31NeyI7G3rvLvwoLXu-RcT79lW-pvIw8RFWLNrubo_wKF7K1aiA4_cK3RZKD1dj5WA8Qgo9RTHSxolN2sgR1vFAiFJNHXkiEH3ncECLr_-j-PTErD8vUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=GFwINfV6g5amFzus_aTWpLZn2kYItUs1TN5n8UUWO0sO-2xBeSpitN0yp8h6Wp1xQtIu1oRIDfln046ZhxpIkpIkGpTJ8IJa6u_8-1VyEhxPA_HcAGPLFbKesIwY3lVGGRfsJJpsk5eb_BBkKDGbki7Uwmq4pCLMpxAkOo1xMhHwtZZUgVzA_o8A4IZH4qVjqiPCN0pQueDPpXOS3Tk3G-GATi0TV1m5g31NeyI7G3rvLvwoLXu-RcT79lW-pvIw8RFWLNrubo_wKF7K1aiA4_cK3RZKD1dj5WA8Qgo9RTHSxolN2sgR1vFAiFJNHXkiEH3ncECLr_-j-PTErD8vUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lPw2iJuW7gmTf02_jjn0QvQLP-XX9lG40BVZVlX111CeZIJI8lULEZCsKTJUeGoEnXuhmNZw2CGrRD07f2AkRg5Cu_PK26cDPOzseDisGAtW7-DxLGV_rH7ukSpEp0UfqQLShgWCGo8nFL9vP3XBJV9PTcHNKKUkVNYYFU8fWrvVat1gbTxaBlLnDHZ7kjz5_p0N4_kOeTzYCpAV_gn77aBQ02oetT_-xN4N6bg-IDdWmv5n1XTLpe4xsNSm_Q-Wxv_MwfCwJ3NIRRmRY6KP7j2MqA8ijnXwFz4gBJl7kW7Scr8MllwvJdJDv3p6skuOYiuPygq3_mi4VKU8_DSeXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=F43T-49j8dhQiHwspUSSflGyB8LG-O_Qp0YfaOriqK6bjNfpO6KHi60UC9qm9Biv-eQI0HrG6-fXL90WNf75H0R99gIIXkPAYFAskDWbiqT29N1fh0edzywcAkcxmiFPIDrcLXHqPurQG8JOgtf2WfQlbXuWkk47eJtfX5c_AQwfaIDhCxjIwirlEdK6ebZtLbpfR0Hl-HHnsIDmxPRhaXppSxWIbkhhZsohx8Ztty5jUwsqhUIdaT_4SZhLSrBnkwBzhvgi6dt6ppmiWMxCxoL93nHjuiwAtBn0TJ-sxDXSN9wB1_ZCgkrphKe035_1axGXVTRSAajEXhZ8_OkzdZMB4dtxe8sWWXkwRAng5Bmx6fJFZd8yjos1s41VDBQY16xlbfLzJEhdKoxsApcLeGJRrnwwvEwGKAKT_bFTLh2HTFARxwvU_KqtpsNpll3LwmO8_GINLehAWtrKradC3AQnTatU9SrKUG_42Tqgz9IgovknDglfGJs7DzOo4BPg-RO0xe80ImnGJcul3WIHurM0BEd5Zdb8QzUSxvUlKI3j0mEH7QQU2JjC-tplPo744KiRUsYbCrP9I5JdvHvfXsBDvCg4lgW2jY526KX-VKLoicJw2ocu0He_YaqDF81ufDI4P9YfaP3qjMv6rH92hMLsi29pd_bNAaDY_EBv8Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=F43T-49j8dhQiHwspUSSflGyB8LG-O_Qp0YfaOriqK6bjNfpO6KHi60UC9qm9Biv-eQI0HrG6-fXL90WNf75H0R99gIIXkPAYFAskDWbiqT29N1fh0edzywcAkcxmiFPIDrcLXHqPurQG8JOgtf2WfQlbXuWkk47eJtfX5c_AQwfaIDhCxjIwirlEdK6ebZtLbpfR0Hl-HHnsIDmxPRhaXppSxWIbkhhZsohx8Ztty5jUwsqhUIdaT_4SZhLSrBnkwBzhvgi6dt6ppmiWMxCxoL93nHjuiwAtBn0TJ-sxDXSN9wB1_ZCgkrphKe035_1axGXVTRSAajEXhZ8_OkzdZMB4dtxe8sWWXkwRAng5Bmx6fJFZd8yjos1s41VDBQY16xlbfLzJEhdKoxsApcLeGJRrnwwvEwGKAKT_bFTLh2HTFARxwvU_KqtpsNpll3LwmO8_GINLehAWtrKradC3AQnTatU9SrKUG_42Tqgz9IgovknDglfGJs7DzOo4BPg-RO0xe80ImnGJcul3WIHurM0BEd5Zdb8QzUSxvUlKI3j0mEH7QQU2JjC-tplPo744KiRUsYbCrP9I5JdvHvfXsBDvCg4lgW2jY526KX-VKLoicJw2ocu0He_YaqDF81ufDI4P9YfaP3qjMv6rH92hMLsi29pd_bNAaDY_EBv8Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBgiKWzDsyFQKbC1gEx65ogAuoWPyQrOmBgyRp5-rUaQesw3Gne6u5Efd_cLuvPeZCQ8fRJIl4G1ABpUCoSUq6mINfXJWgQvasLaPzlJJEEAd9pk_-KkYQ_7iJwjjjN9zjGZrRj7_t_S4DDhJHFS_rKIb4C1I8LuO-vvtJZRExVETPcZxeChWRLYHbH99NAuvLWlmxsXp05c8ZNpgU0AvyqbmiUBTCbx6D1Ram9RM6Cax5W3a7y6YNTbuATMay7lXaPpIH_2uxr1aJmqVABwnXmSLytIxpA2X7KxY7OXcYeHu6T9-VnbhkiFSXzRRpLs1VfOZvFlDE_PCdxAKYX0gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان جمهوری اسلامی این روزها
برای عروسی در یمن شیرینی میدن،
۳ سال پیش برای عروسی
در غزه شیرینی میدادن،
پارسال برای جنوب لبنان!
عروسی‌هاتون و پیروزی‌هاتون پی در پی
✌🏼
۲ میلیون اهالی غزه سه ساله زیر چادر هستن
۶۰۰ هزار شیعه لبنانی ۵ ماهه
توی توالت‌ها و گاراژهای محله‌های مسیحی و سنی پناه گرفتن!  پیروزی‌هاتون پر تکرار!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6745" target="_blank">📅 13:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6744">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=UozVxjnXEDrgnV6hyx-Qb7lGQAaxEDSc9YbrPPa2Ydz0jgkUgOtuFkLqQBjvvzhWbXlPmQItLSwXXimhFQnt_psJSvlBlN3JnqWup-QNfvPUMET0jFfhlpsgAKVyiR0brpbhmVLM6xXm5Xi5FrGvjatNxe2_UK2J0QMKD4Y1izPrQFulRBVx32fJMHc2HnSlidFSQ7BUTq_jVhiBiIzri7I6PKOFcxOSN9RbCjiNQGbU-OutCs1LKiuUQ1vNGL3jYn4yB2iCL4y2572TSny6qKFdyDfIsfiZjIuPxapS9xjPz6xiQN9qmA0sf-LmRiBzW0IUfM3dtecGsdg8RgPNrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=UozVxjnXEDrgnV6hyx-Qb7lGQAaxEDSc9YbrPPa2Ydz0jgkUgOtuFkLqQBjvvzhWbXlPmQItLSwXXimhFQnt_psJSvlBlN3JnqWup-QNfvPUMET0jFfhlpsgAKVyiR0brpbhmVLM6xXm5Xi5FrGvjatNxe2_UK2J0QMKD4Y1izPrQFulRBVx32fJMHc2HnSlidFSQ7BUTq_jVhiBiIzri7I6PKOFcxOSN9RbCjiNQGbU-OutCs1LKiuUQ1vNGL3jYn4yB2iCL4y2572TSny6qKFdyDfIsfiZjIuPxapS9xjPz6xiQN9qmA0sf-LmRiBzW0IUfM3dtecGsdg8RgPNrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eAMJfb2Kb9XJGVLFOfwcZoPy9B6HW5Om2Khz2IiVk_iXaxst_nd2ATsYZc1RNNTx9P2NExDZ6ht_0HO80ctvmoMl8gHbEo19bxSvOJfUW0cvB9Z2zEUd9GtwwEnnAoKR5X02koEgI8D5bWdvl-flCEZH10B_LRE9MuBKN7Le7Fa2cobxMWr5NVLdOVy4Maf58xpA7zRRHLN0YlG6HMZfSpnovugQvRSAoS8KREUch98d-OHQbFwU7GsETWvSGCU_CDqTfSXtB92v1TvRV-jsH2VJt8aHhuyhnoy8bwnMCEV94Qfh-Ia94kfapUd6npZn_v-Q1hd-wpMCxCAwioUIlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LrlZByQJ1ygqI5Ir_5cyoWJ7ZnBE8hh4WSOrg_Njy5nGgI64p_VVz2qa1wK52B5KM4JY8BTyuxx30WQmkB2O8j5BblqmEKhQ_2ZtDVwcVyj87IDC5smdvUtXdUvv0u7ZivCHFEM7crgzDu8VBFo0rvrnBmeYi1zn13_xD5y1-oKFjdlg7cZ71j3nBY1JB45kf4cEXhM_TKgmIdBu2rKEq3O4Yoqff3PM_w6Mxub878As7BsFbDGExmUuYZ0MON1nSOW6bcnWJ88_ec9AiymoqS9l6vWBqIWAf3s6wFBnHKUee1JdSh9gt6HdrOZa4xZQGWq_h-miEvEg47tfwg-b3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRKDtUeMfKoWdWlkHgd7bdQqsw6GjiZfDA1gHrR18ESoyCKLgfUdZ74nMzXbfkoa8haNbju9lalHDMHof1GSxGDStJpcVxIqyHFlt8LQJHBXiHebnNxQVEGlK8R4a8SSd7R1ZFHlV01SIiC1hQ-irpFCPBkbfVk62kns0z8QPoZfG6Y4j88BpfCvuBxVlaxPP-B6mOLkJs_uU3c-Q-7aZw43nrAmtAn6gt4WulMaDdt6eYm9V73kJDbqGRyREbXdNeFvx1lZwa-faqiZudFvt9ruBnmtSwcNzvQ_iXF9njeMgj7L84fnXszxjK7uhcSAlgJ1qkeNxQ44SyRPFKpTtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=KiinADucpFsfTppljEF3vyjF5QV1e40qrOmTCaGWM34-izTORFt4IWf7StdGsBWvmNU-qYbMwaE2OOsZczO1mnjo5eUtKAEvMl1cms54DMkmd0_8ydVmWb8Mu6Y7NFTNprjm_LPdCuCcBz7ee8mxHqzejyGICpR3FuIUekbIuYLrhgh2crsJBw5DBZXHPD5TGONS4FFva54I63LyGOOK0soX4ESqkTunZTZS4uWOVT-a-ibMuwdxikvpXRaTr-bG5ND8G2pnBK4IfRpE1Pf8Edp1QAppGgNzzld5KPlIhc6GTUfixsa5nlqJ8KHbcNIyl1Xj6CZsH_FfQhIjMDDGuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=KiinADucpFsfTppljEF3vyjF5QV1e40qrOmTCaGWM34-izTORFt4IWf7StdGsBWvmNU-qYbMwaE2OOsZczO1mnjo5eUtKAEvMl1cms54DMkmd0_8ydVmWb8Mu6Y7NFTNprjm_LPdCuCcBz7ee8mxHqzejyGICpR3FuIUekbIuYLrhgh2crsJBw5DBZXHPD5TGONS4FFva54I63LyGOOK0soX4ESqkTunZTZS4uWOVT-a-ibMuwdxikvpXRaTr-bG5ND8G2pnBK4IfRpE1Pf8Edp1QAppGgNzzld5KPlIhc6GTUfixsa5nlqJ8KHbcNIyl1Xj6CZsH_FfQhIjMDDGuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S8KGfBKiFw_3fGy66Azn7-r-N4gZT8-nFls5nnHyPxpytFJ7jHecFsRzibmrOGI3a749vUuFvrdo7zx3GzktcTjsUA9IwjcoqL18lq7F1esTvuVgi8wDP8vyv94scTwJCIVsX1I-NYpgeGRfZgPiEtFyMqCARzWlzzjL4AwIIRKSB0mA8-uZ95AaIh1DIqL1egLkFCizKOq3XhVdiQYT8aHsRcEGUoUpoQnz8rqHcIacc9k3MwYCDGZy57NIfaZYZ_naiZdMh8IMzJvLkXyLVOe2gspDtwIGBKAUkppAk36BXlibN3HpJwxLjl05qsGUsB6bW4h71AYtEDk4Fga8yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu0sodWRZ1yLYmbuBJloAYbBUw2DxdTpncIokohm_Aql5HD6r0NaYRoJajPRI-ZZaI0WlaknEZoOX9eM5LJWVBQlKlf9jD3pSux17ViJvRx6iHL_spjYKD--OMt9-wmWS7SyLuTSMPvg2v_gHsItz5DFMP0JWF2qodh_FBNpx4K4MFBC5D51GRoLKFwyBipaoFkuq34fN5gD3pH8jimE0sn8LAoHcIJyf8Y1XpSuhHK3pd5Gy_ifjlkvTpXxXyswslVfsfjnNFF2SMDUQWJ_dbJJGnMQWuhvRF6-Htbj3B-eFdZGJFsC6KXdQetbB5r_gtzJ6XtPa3sshoU21-hhGXEc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu0sodWRZ1yLYmbuBJloAYbBUw2DxdTpncIokohm_Aql5HD6r0NaYRoJajPRI-ZZaI0WlaknEZoOX9eM5LJWVBQlKlf9jD3pSux17ViJvRx6iHL_spjYKD--OMt9-wmWS7SyLuTSMPvg2v_gHsItz5DFMP0JWF2qodh_FBNpx4K4MFBC5D51GRoLKFwyBipaoFkuq34fN5gD3pH8jimE0sn8LAoHcIJyf8Y1XpSuhHK3pd5Gy_ifjlkvTpXxXyswslVfsfjnNFF2SMDUQWJ_dbJJGnMQWuhvRF6-Htbj3B-eFdZGJFsC6KXdQetbB5r_gtzJ6XtPa3sshoU21-hhGXEc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=D_7DrXNN0LyJceOSGSUJrjHoYEOOgIt6--DjU_DzQxaHYLs8wEyC_ixQZsnT6BRf4j48eSoIDkJnSBzOIENQ6ruPWLYnzCbKhrGr2HBokSOnPUFIsPPbsozyg2HlK2lhPDDsCwqneUbnykkLybcGNWhYJ21_3iZhGAKpepWb3xiVstSYwTtq_-MZr_LFJX4X__T9qek49evdo1inXzIB2OzZlnFW_QgJ2CD0DK7TWpB2K6OFjHVY1LG-hBrmI-kPaHuhHnYg5HQc6CGb8WgF9CcSY46_ES3925V7sk8EGKsuhTU6bO9iPTGe31rytZ1h2sedW7wX_VKIh7E55Q67fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=D_7DrXNN0LyJceOSGSUJrjHoYEOOgIt6--DjU_DzQxaHYLs8wEyC_ixQZsnT6BRf4j48eSoIDkJnSBzOIENQ6ruPWLYnzCbKhrGr2HBokSOnPUFIsPPbsozyg2HlK2lhPDDsCwqneUbnykkLybcGNWhYJ21_3iZhGAKpepWb3xiVstSYwTtq_-MZr_LFJX4X__T9qek49evdo1inXzIB2OzZlnFW_QgJ2CD0DK7TWpB2K6OFjHVY1LG-hBrmI-kPaHuhHnYg5HQc6CGb8WgF9CcSY46_ES3925V7sk8EGKsuhTU6bO9iPTGe31rytZ1h2sedW7wX_VKIh7E55Q67fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=UdqxC38VjXLlUHuuTFwzZ8Js8X6txm-Bzvh-mvef-FTDuqJMm6qZP1_L1UboPvH4vSPmj0IfeHkcoUeOqQY_zPVv-4guY0Cm9NUQbzlaICluJ--zybFJnuQEztzG66Dus_se9ebv0nJnjjA6kkvhO5Lpr89hx9Xx1ks1m6dKuGSvQx2yNUILBYV_vlZtUiukP0g7ftWfM3SviCeB_MfhjxyG9YcXlWDqk7wqSWhAMqC5Xgu6Be2H8AH6THfskedZtzI9q-u1XvqEOWBVxD6wwxiFtWL_KdqVEJLOxBWuXYEwSTlDhZtKNJpODDPELTR5VnDEsxjLAy7g4h7onP8R_DXFli0iaORNCRXMCGTDgux2upm8lEC_t39pJRPAAINGBMixZHwXVgZUgysEjtSLzxHAfu6oiF6q8GXW_fUEMX5W7ZyxZbxM2WILjeTbfxa10-hgOuAqskA0Q_VETMwzbTMGiJo_CwFZLnRc5PjPVq1UsDeoexYePK3L5hV1ieojs23JX_whOXBXdFFkqCf82FzbTT4zAr-DWrldL5wrMg-9XTwfH7gNndaaGdXDcXhQkX4ZS9793nvKFdhRKt1gv0q3UoHPd9y_90K4Co6e05tHQRTpl80lh76NJJoj2fZf3rVJVUOWvhU2wOsOaTd1oCcVMhmtSci7NgCDxyvK_dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=UdqxC38VjXLlUHuuTFwzZ8Js8X6txm-Bzvh-mvef-FTDuqJMm6qZP1_L1UboPvH4vSPmj0IfeHkcoUeOqQY_zPVv-4guY0Cm9NUQbzlaICluJ--zybFJnuQEztzG66Dus_se9ebv0nJnjjA6kkvhO5Lpr89hx9Xx1ks1m6dKuGSvQx2yNUILBYV_vlZtUiukP0g7ftWfM3SviCeB_MfhjxyG9YcXlWDqk7wqSWhAMqC5Xgu6Be2H8AH6THfskedZtzI9q-u1XvqEOWBVxD6wwxiFtWL_KdqVEJLOxBWuXYEwSTlDhZtKNJpODDPELTR5VnDEsxjLAy7g4h7onP8R_DXFli0iaORNCRXMCGTDgux2upm8lEC_t39pJRPAAINGBMixZHwXVgZUgysEjtSLzxHAfu6oiF6q8GXW_fUEMX5W7ZyxZbxM2WILjeTbfxa10-hgOuAqskA0Q_VETMwzbTMGiJo_CwFZLnRc5PjPVq1UsDeoexYePK3L5hV1ieojs23JX_whOXBXdFFkqCf82FzbTT4zAr-DWrldL5wrMg-9XTwfH7gNndaaGdXDcXhQkX4ZS9793nvKFdhRKt1gv0q3UoHPd9y_90K4Co6e05tHQRTpl80lh76NJJoj2fZf3rVJVUOWvhU2wOsOaTd1oCcVMhmtSci7NgCDxyvK_dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=bi2fymb0A8mmxN0siU7BOj_XCpRZOdz0RB_JtHULWQlqzre6nlhydYBWxkXHti0bD8FVLPAuU4nICoJX6kzHgkS8yEeZ5dpBqVIU-c9sJt2elJyyXJ0MwW-O3OwbQwfqon4m5-J6PsJAtIgK_SJV8YUDW3tzdpKgNkQSbq4eBym-opMgMyo8ARQy9TgftjKC1dPVJEKZoab5Io6NOhJy68n72GG19WvW-thm5pfr2jzNIi43IcM92OYdJzoMjQy-jbYsAyqOBJkQQxRjcrdWzZ0rzXaiwXFAQGP5x-f4xGzUoxy6nq86sKct7v4EeokvVC_VrSuhZba5MuqEvX3H9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=bi2fymb0A8mmxN0siU7BOj_XCpRZOdz0RB_JtHULWQlqzre6nlhydYBWxkXHti0bD8FVLPAuU4nICoJX6kzHgkS8yEeZ5dpBqVIU-c9sJt2elJyyXJ0MwW-O3OwbQwfqon4m5-J6PsJAtIgK_SJV8YUDW3tzdpKgNkQSbq4eBym-opMgMyo8ARQy9TgftjKC1dPVJEKZoab5Io6NOhJy68n72GG19WvW-thm5pfr2jzNIi43IcM92OYdJzoMjQy-jbYsAyqOBJkQQxRjcrdWzZ0rzXaiwXFAQGP5x-f4xGzUoxy6nq86sKct7v4EeokvVC_VrSuhZba5MuqEvX3H9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/olm5am24RRfGfPsdyO1rE8rQ_118hU05zihiYJRbQiScj8SUIbev1wqpWMF2Xrsu2zdN21cfJ-wVtYnqgDneewcd16qJ9FTHp5hjFGncRx8FyvYOz71XSrT11uxjE8o8EpS3cb3iZ9cSUhugi8WgdZH2gbNg40OCa4kFeE7tX5kQRFpplQOQAf5NMDO8T1PpfsHEBZWPi_DAM-50-vSRoSWCnc23kcSi96R9M1E2R7YwnHDmpPrRw5a7f8QAhSzPjdZf7BsCaAVSxYFVxFLCDR3c6-hSEi54KEvLfeQReO9jrImKxFPuP8bVOT0alPyt3H_wv_MKLwhvUdMn46pMuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=rf7oQIY7M68jYATCbk1V6YxCMHuB8XpJl-QQlxZbe-iE0TieFk1XsGLPbuMx-mGWcFZFYhvPdsr82pglb3MCX7b2EQYCwtComzDN9Owcoj_GXpzy2ZsChdYbop7GrecE85x89q5pQNpFtmWaqfnH7NM1NxEN4XNxmDrOTEL36U8v3M1jud5g7Onwt-sB0feOHWJVcGEn866Q-ycZ3TFMp-p-SuYEIdfjY0fr4kaRlwSCS_tFU_exrS-c-8nckrFbySPxztdQGYzdMeYPTjyL99klHvjOFWKwAD0XR0U3ngMlSAEhl-DBCDwmZNTxthafwcPtFKGTIDCTeNjShQB-lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=rf7oQIY7M68jYATCbk1V6YxCMHuB8XpJl-QQlxZbe-iE0TieFk1XsGLPbuMx-mGWcFZFYhvPdsr82pglb3MCX7b2EQYCwtComzDN9Owcoj_GXpzy2ZsChdYbop7GrecE85x89q5pQNpFtmWaqfnH7NM1NxEN4XNxmDrOTEL36U8v3M1jud5g7Onwt-sB0feOHWJVcGEn866Q-ycZ3TFMp-p-SuYEIdfjY0fr4kaRlwSCS_tFU_exrS-c-8nckrFbySPxztdQGYzdMeYPTjyL99klHvjOFWKwAD0XR0U3ngMlSAEhl-DBCDwmZNTxthafwcPtFKGTIDCTeNjShQB-lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زهران ممدانی
به مناسبت ۱۱ سپتامبر که هزاران آمریکایی به دست مسلمانان افراطی کشته شدند،
با صدایی بغض کرده
از عمه‌اش یاد کرد که بعد از ۱۱ سپتامبر
از مترو استفاده نکرد، به خاطر اینکه حجاب داشت و در مترو احساس امنیت نمی‌کرد!</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6730">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=RjXQIDddswqUAEHPPBfxdWbtzDCea1__HXOkIn7-ubUMUSc_6eCdoVWgf5vn-CeZS7ouqiT7aD1XDHMM6nw1SpcurNtpnWAYfEkNzldf9SWvwaWc-LTQ2JXhhDL42jdNgJx8Gh2YNJnS3C8Cc4Ml2xeq2lwqYEJTSpmPF_VALchiEKMFyMCpYWCocVAd1JQPwy37PKWl0Qzd-OeB5VkIz4pDD71TscFMVVQYy6R0PObSkBbpHxdkSTakMeSI-SZYoKotw-D-FJ_5ValThJib-nnLOTsGGBdxTZzO8-2O_ClfEGgx69zgnPx4Dty6PAvBJDAzia1XkZm-wAW5jYx-bgCOqZEwmIXasG0N1qpEqPKlkAkDaVog8p0cPegybiho33_4T3P_kkhZ3lFHFK9UDzTXqLNP4mNBN6DEWGroZzn79FhjkXwQBCW3klOTIlufbBhZtAFPg6pKHm8W91xI53XT_pr_ti6V_NuuYu4_NTwBfOvnZQT4Ps503gAvBNgiaofSYkOJfY3HZd4tORU0ZWXuGaawte2UzOWJJurN3rJCO3NANYadpPoKcuMr3Rb_Q7vrA_Hgz-VYV3YQuQV0ykvyidcMxzgYD5ayG4TLFQP_t8QQCyU0m-rdmwddLACTaLAn-jR6woVtBlxe9QWU3eFk_kWTa5vuwAZU60HudJk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=RjXQIDddswqUAEHPPBfxdWbtzDCea1__HXOkIn7-ubUMUSc_6eCdoVWgf5vn-CeZS7ouqiT7aD1XDHMM6nw1SpcurNtpnWAYfEkNzldf9SWvwaWc-LTQ2JXhhDL42jdNgJx8Gh2YNJnS3C8Cc4Ml2xeq2lwqYEJTSpmPF_VALchiEKMFyMCpYWCocVAd1JQPwy37PKWl0Qzd-OeB5VkIz4pDD71TscFMVVQYy6R0PObSkBbpHxdkSTakMeSI-SZYoKotw-D-FJ_5ValThJib-nnLOTsGGBdxTZzO8-2O_ClfEGgx69zgnPx4Dty6PAvBJDAzia1XkZm-wAW5jYx-bgCOqZEwmIXasG0N1qpEqPKlkAkDaVog8p0cPegybiho33_4T3P_kkhZ3lFHFK9UDzTXqLNP4mNBN6DEWGroZzn79FhjkXwQBCW3klOTIlufbBhZtAFPg6pKHm8W91xI53XT_pr_ti6V_NuuYu4_NTwBfOvnZQT4Ps503gAvBNgiaofSYkOJfY3HZd4tORU0ZWXuGaawte2UzOWJJurN3rJCO3NANYadpPoKcuMr3Rb_Q7vrA_Hgz-VYV3YQuQV0ykvyidcMxzgYD5ayG4TLFQP_t8QQCyU0m-rdmwddLACTaLAn-jR6woVtBlxe9QWU3eFk_kWTa5vuwAZU60HudJk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VdKr-RXzxRsNaALVmuMwyQDWLnx-ouEBCzKFVpHLEfREF-KdT5Hm70XIdqVIyLdmkjthkpkhCJuJ4yxZHNv9v7FS762K4xXVEYxvAnfXCLQhn0cSm9qlMCvWpJjOsLql4XJhqkxbaOy8JlR1nLd17Z5-ZgIRb3PR44bjfmaGd3HDQAm8AQ_pgAvYDJFawE3P4zyEy6XKUUkNgTaX7LtEQrzL7igWg3bOTOxe-22e1hE5onM66Xwq7WPbLwvx2wy2cX87GtvoTDZXd7DTQucKK_a3uGJwpCRwjwWX9ulYV7_AN2HAakvzj0cE0Gz6GmeSigKND35T07oO0dclFpFM3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=eR3JEAED7prrEpvcmV-7lWNGJRcyJbQFjbCSGlfkNbTiSAOcr-Ga8ZJa4F8Veav0t2n5eW5wz0qCh2h-3jTczVkoiswiAB1qfX5kMqLQe62rl7o2P88MFdA5Cjln8bbHMncCxaUCBqVvnL6MlrFAPh2IisZmc85q8ocGVblFiWjvLAAOjNsa4iRF5mxl6kESyGtRorlJ8m0Pioj5BuRcSChiXSitgi5kZb5ZozTjcDUFYx_owFJv2kdYXg0JoufW6JJZE8nAnBrJvnxS7nF0Q_XtKYVBvT7nJfbkKd7K6KFfkgXAXQidd5qGYzPtmQoUoebL1EJsdhpZxde9K9aGEYUnFzyAyaqNuFlW3zsRRDGRJQyatsxR6kCNDKRTf_-RiSIkGaXC7iYFqxf9ANHUJsIBxLuM2E6GhnAeQxkkxVzSm6c9l3-owdWUNgAXRfUwRaK259WUk4OBX39WqMCwDFw8LeszYtpCpk2VCENLPGek18XmYQYeYKdWY-wqrzWrsXtyJUUpo3Bpbj1UezdYScXHjfSSxY0XXkZcIMXwJltire8bnHiFo8LFjJBUz2WWYJDNT64wt0biEddvoCvlUJJ1DSWaMslSFtSRBdKPU_b5VL6-c26Jsa43NXdB-QScfmms7-sWobjP6SvGcl3IU_WPjgtI4-uwoH7HYuEidbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=eR3JEAED7prrEpvcmV-7lWNGJRcyJbQFjbCSGlfkNbTiSAOcr-Ga8ZJa4F8Veav0t2n5eW5wz0qCh2h-3jTczVkoiswiAB1qfX5kMqLQe62rl7o2P88MFdA5Cjln8bbHMncCxaUCBqVvnL6MlrFAPh2IisZmc85q8ocGVblFiWjvLAAOjNsa4iRF5mxl6kESyGtRorlJ8m0Pioj5BuRcSChiXSitgi5kZb5ZozTjcDUFYx_owFJv2kdYXg0JoufW6JJZE8nAnBrJvnxS7nF0Q_XtKYVBvT7nJfbkKd7K6KFfkgXAXQidd5qGYzPtmQoUoebL1EJsdhpZxde9K9aGEYUnFzyAyaqNuFlW3zsRRDGRJQyatsxR6kCNDKRTf_-RiSIkGaXC7iYFqxf9ANHUJsIBxLuM2E6GhnAeQxkkxVzSm6c9l3-owdWUNgAXRfUwRaK259WUk4OBX39WqMCwDFw8LeszYtpCpk2VCENLPGek18XmYQYeYKdWY-wqrzWrsXtyJUUpo3Bpbj1UezdYScXHjfSSxY0XXkZcIMXwJltire8bnHiFo8LFjJBUz2WWYJDNT64wt0biEddvoCvlUJJ1DSWaMslSFtSRBdKPU_b5VL6-c26Jsa43NXdB-QScfmms7-sWobjP6SvGcl3IU_WPjgtI4-uwoH7HYuEidbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :
«مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»
و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6727">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=ENIv_-iLwXOeM8nEoQr6bgfInAtByge3ptFGiUkmHp5vTk3yc84Jqk7TvVca3MIYakZ_Ylx-MVE8M4bAHkqHnsufQ4qMPZ0h3Eqa3hvrN9cw5pb6hRiJP28EDCA7JJVHX2j992XWIeatMvdnZlQNh9LoJRyMj3a0ipl-jERjK2Z9LoxqoebkC42ZwV2R8OktWKu5PK3Umbed_HZeZ7WOEDcpT5CvHi6mxBhnNkoOi2IZQ0WTPAG0KAFEjOMaDiFkc8r9MCTzGqeeRQ5XNJxpEAlOluaDE22UfyKyFKXyf2YlaEKEClMQ16aZWSicDgZDCAJrooZdaOUU9PPUd_LCmjXlSOZFbKEemjuhkw9gBZ0dIWCzjhm3gbo6Gas35KmxKwSInU5xQlNm3qrW6hnl6yLqhNP1KdWZPDfLA87xulDcfcI6u82snW3FBIiqc7v9EQE5nU3r1iecO_gS9GuQUCQPh4-S-gEKhDNuJ2aaT6CCm9c0yfI_2NLgZ9YkJjQjMTS57pO51IBZ7oH8no70y7AKZaE0HAYkbSun35rVRlETE5P8z2z3yJ0-CApYtiFyZoLVwIUbY-g8PyQLedY3dlqANZOOHSDGaI3R534uRpc65ZgY_jZTn1ekDECwydZtS4OWaMOgBq7fKkYp74IqirMnkiuHZZBJalxvQmRtoTE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=ENIv_-iLwXOeM8nEoQr6bgfInAtByge3ptFGiUkmHp5vTk3yc84Jqk7TvVca3MIYakZ_Ylx-MVE8M4bAHkqHnsufQ4qMPZ0h3Eqa3hvrN9cw5pb6hRiJP28EDCA7JJVHX2j992XWIeatMvdnZlQNh9LoJRyMj3a0ipl-jERjK2Z9LoxqoebkC42ZwV2R8OktWKu5PK3Umbed_HZeZ7WOEDcpT5CvHi6mxBhnNkoOi2IZQ0WTPAG0KAFEjOMaDiFkc8r9MCTzGqeeRQ5XNJxpEAlOluaDE22UfyKyFKXyf2YlaEKEClMQ16aZWSicDgZDCAJrooZdaOUU9PPUd_LCmjXlSOZFbKEemjuhkw9gBZ0dIWCzjhm3gbo6Gas35KmxKwSInU5xQlNm3qrW6hnl6yLqhNP1KdWZPDfLA87xulDcfcI6u82snW3FBIiqc7v9EQE5nU3r1iecO_gS9GuQUCQPh4-S-gEKhDNuJ2aaT6CCm9c0yfI_2NLgZ9YkJjQjMTS57pO51IBZ7oH8no70y7AKZaE0HAYkbSun35rVRlETE5P8z2z3yJ0-CApYtiFyZoLVwIUbY-g8PyQLedY3dlqANZOOHSDGaI3R534uRpc65ZgY_jZTn1ekDECwydZtS4OWaMOgBq7fKkYp74IqirMnkiuHZZBJalxvQmRtoTE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=F-x-Bzreswlveyo-ZwJM39irxlklqaLO6sGYf-oB4UL3Xc8Eok2eIg3H-YAs_P4Xv5vM9TVfujwm9B-EqSLeLKyAiXBvKArv7L5Ryv75oG3mjx33UIamAnq4EkkP-dvGm2C1ayJCm6YdVMr3-Py2h03tJqYKZMNu1EZVOqoabWJbjw_-QAWiQKzowrduoR-3yNhQwEayKBj5GpiPR_RM71n6WC8PYhh1dAyVxn96pdMpoa8Yob-e6jxPpFvlVPxULyeSGeIJ7OtWKPFhwVEgWzyajZiulg7JCSR5zEA_ZLEwKjWlU9Dxr_gCytvolN-WyrFposhcaBpk3EoCpCINUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=F-x-Bzreswlveyo-ZwJM39irxlklqaLO6sGYf-oB4UL3Xc8Eok2eIg3H-YAs_P4Xv5vM9TVfujwm9B-EqSLeLKyAiXBvKArv7L5Ryv75oG3mjx33UIamAnq4EkkP-dvGm2C1ayJCm6YdVMr3-Py2h03tJqYKZMNu1EZVOqoabWJbjw_-QAWiQKzowrduoR-3yNhQwEayKBj5GpiPR_RM71n6WC8PYhh1dAyVxn96pdMpoa8Yob-e6jxPpFvlVPxULyeSGeIJ7OtWKPFhwVEgWzyajZiulg7JCSR5zEA_ZLEwKjWlU9Dxr_gCytvolN-WyrFposhcaBpk3EoCpCINUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شدت انفجارها رو ببینید
بخشی اش موشک‌ها و سلاح‌هایی است
که درون تونل‌های این تپه بودند.
این دژی که تصور می‌کردند شکست ناپذیره از درون نابود شد.
پول‌ها و سرمایه‌های ملت ایرانه
که دود میشن و به هوا میرن</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6726" target="_blank">📅 09:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6725">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=tOFE4JE3OzqpVppt7aYCazaUFFb7-hMYeea2WRodHJBuNqxnwnQ0FWmG_1EaXMqw5UTkPBwdujBA2pwkhE0haNlqX8egmLNocXu6NRT9snlaZ_5nzitGCKS1zJig91El6_BFpdVG3kVx9npL-MFbdm9kmFXJKJOsRZpEaYRcUCnh6UgZkVVwDYx2lGX6StjaqH6o_TSrmMhLMw4n4vEjFsUvPoIaORvAH9EP0MRHGfItL0Z18CEMq_US2BNCWRjAK9yXlH5oF4zqcNdHHu4EyUiXjXuw9J2aehwGLNbMT3IiR2Wk1BIMCCQs6ODIS1tKdCk19LuLZzowU9ZNPbk-uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=tOFE4JE3OzqpVppt7aYCazaUFFb7-hMYeea2WRodHJBuNqxnwnQ0FWmG_1EaXMqw5UTkPBwdujBA2pwkhE0haNlqX8egmLNocXu6NRT9snlaZ_5nzitGCKS1zJig91El6_BFpdVG3kVx9npL-MFbdm9kmFXJKJOsRZpEaYRcUCnh6UgZkVVwDYx2lGX6StjaqH6o_TSrmMhLMw4n4vEjFsUvPoIaORvAH9EP0MRHGfItL0Z18CEMq_US2BNCWRjAK9yXlH5oF4zqcNdHHu4EyUiXjXuw9J2aehwGLNbMT3IiR2Wk1BIMCCQs6ODIS1tKdCk19LuLZzowU9ZNPbk-uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی به «علی الطاهر» میگفت «مینی پنتاگون» پنتاگون کوچک. با هزینه میلیارد  دلاری، با صرف ۱۸ سال زمان، شبکه‌ای از تونل‌ها در درون این تپه ساخته بود،  مرکز فرماندهی، انبار تسلیحاتی، محلی برای حمله به اسرائیل و…..
اسرائیل دو سه ماه محاصره‌اش کرد و اجازه نداد آب و غذا به اونجا برسه،
سه هفته پیش جمهوری اسلامی
به آمریکا پیام داده بود که اگر دست
به علی طاهر بزنید، جنگ برپا میشه و…..
اسرائیل در یک شب، پس از شناسایی ورودی تونل‌ها، ورودی تونل‌ها رو نابود کرد و تبدیلش کرد به یک «تله» برای سازندگانش.
جمهوری اسلامی تنگه رو هم بست و خودش در داخل تله اش افتاد!</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6725" target="_blank">📅 09:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6724">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=RZNrEx8X8q6SKmBNZ-E9PbAYLw3BnjiJTpLvwIWKgJ73C853iuPeoG3HGVwyK2cbRc6uqK9G6U-NKQ1kfJckvwK9jPZI873tPgWBNEauzOIwdXaGCO_ZE3SEsC3-7vEishmo7zyqNIiY0nBDiG8J9Vmoc1PSEnI_4wTsQtEN3Rej6ibpnmL8Kz2kvS7QfNiUFaakgz-O8ZmNlckywEzpwE9MeuAeuyXzvpVHufwYcLS9mm2hEWAB_pOhQITgpqBpjTi7WbMC2BsggSCceOth3ilHExzqIgOFGQV2v0lCmmmlmQmujbxC7QClILT9DuofwhMQV0Nkw1gOSAfJAeIUUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=RZNrEx8X8q6SKmBNZ-E9PbAYLw3BnjiJTpLvwIWKgJ73C853iuPeoG3HGVwyK2cbRc6uqK9G6U-NKQ1kfJckvwK9jPZI873tPgWBNEauzOIwdXaGCO_ZE3SEsC3-7vEishmo7zyqNIiY0nBDiG8J9Vmoc1PSEnI_4wTsQtEN3Rej6ibpnmL8Kz2kvS7QfNiUFaakgz-O8ZmNlckywEzpwE9MeuAeuyXzvpVHufwYcLS9mm2hEWAB_pOhQITgpqBpjTi7WbMC2BsggSCceOth3ilHExzqIgOFGQV2v0lCmmmlmQmujbxC7QClILT9DuofwhMQV0Nkw1gOSAfJAeIUUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=oqgRhZJVSV8jMYfwL_GCaCMyYLE9bxgTx0pE0rBKGdQ41hvkXcjuxk-p--cK5w4vPggpxGsesA4uFPAPeT5r1BTt2d-3NxUVm1lVw5u_ulGEdI9VTUVx6q3J5CRfyKOyI3r0Qh7LSuep1Xwy6bCEFUs5SOYmbS7co0TIbR0w4mV1KxIRvFZ_vbbJd_Y6XLx-1dzq8RiaQNYAAKuQZg_AeSPrzmtXTukI7OBC_YAcJ0OhohH-d9sBfa-5O8jQhe05395Vw_y2N1xHvQWXOoT5TkOuJ9hsZwmbRJfau2DF8NEzfoYT00gBFl0XW_RqHmX3dLSiNxFvJ8PYb9lDEBQgTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=oqgRhZJVSV8jMYfwL_GCaCMyYLE9bxgTx0pE0rBKGdQ41hvkXcjuxk-p--cK5w4vPggpxGsesA4uFPAPeT5r1BTt2d-3NxUVm1lVw5u_ulGEdI9VTUVx6q3J5CRfyKOyI3r0Qh7LSuep1Xwy6bCEFUs5SOYmbS7co0TIbR0w4mV1KxIRvFZ_vbbJd_Y6XLx-1dzq8RiaQNYAAKuQZg_AeSPrzmtXTukI7OBC_YAcJ0OhohH-d9sBfa-5O8jQhe05395Vw_y2N1xHvQWXOoT5TkOuJ9hsZwmbRJfau2DF8NEzfoYT00gBFl0XW_RqHmX3dLSiNxFvJ8PYb9lDEBQgTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=fKd2SwL268TDy_agTk8oGMlR84ygW83lMbfl3zp4bTZ5vKro1qnr2V8gk6EdB1Xoj44NySdcKfA2LsWcwjxzGoc_ixSsKSQQeY6i-F7tpvn_mInOM7AUooI3zXXsmmDEqCo-qXqVYKno4gOKMvLXFwWetlEUx6twDb-kbZZk6JqjOjo0AiTj3r9jc-BUZ9IXGssTqiU0syvCuaZ5SDbnHyrtwwt7jv_PIEJjoFnHaJK9cSZ73s8DMlvSmdG94tkG5UGuJW9xnEPZUtwPPQE7W9l-KUBIY0ih_7vQBQmHRAz1cxBCgyyFJq0lqQ3EhqqR-3XEi7nCJ4EJZHBYjuyDEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=fKd2SwL268TDy_agTk8oGMlR84ygW83lMbfl3zp4bTZ5vKro1qnr2V8gk6EdB1Xoj44NySdcKfA2LsWcwjxzGoc_ixSsKSQQeY6i-F7tpvn_mInOM7AUooI3zXXsmmDEqCo-qXqVYKno4gOKMvLXFwWetlEUx6twDb-kbZZk6JqjOjo0AiTj3r9jc-BUZ9IXGssTqiU0syvCuaZ5SDbnHyrtwwt7jv_PIEJjoFnHaJK9cSZ73s8DMlvSmdG94tkG5UGuJW9xnEPZUtwPPQE7W9l-KUBIY0ih_7vQBQmHRAz1cxBCgyyFJq0lqQ3EhqqR-3XEi7nCJ4EJZHBYjuyDEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما میگه :
مردم ایران در خانه‌هایشان
«۵۰۰ میلیون تن طلا دارند»
یعنی «هر ایرانی» حدود
۵ هزار و ۸۰۰ کیلو طلا داره :)
روایات اسلامی و معجزاتشون رو هم
همین مدلی ساختن!
اون مجری شوت هم میگه : الحمدالله!</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=eCnPTLO50vJHh5dtZJRCcqXRzSE9kmHEvzvQfgCb1gaAPspTPuXeG6DkClmq_Ms3VWZlQElnfJb1cCUusTtc4sIW5ytqwvIS7xeEbz07qHqYeMr7_bA6bjvnHlzr0fsvWbGnKlYEuBuAEZgBn2esS9Iw-eOGP9sAV2ERA4kxqv6MHyeN8Q-GdHn4ThkHHMaI5vA7xOJxf09MsPBLOP8b52_Qwd8DiT9ArAKiQ7Ve0-mwZNPGkMxcTnKcJWQBOIR2VSpT3SNtHv76CKYDjBRP7Ij9lSmRAOYEpfHBygdNBptHhHahfcHabWI3zpvHio3xD4Q1j1GoBdeGRcVfwt1Qvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=eCnPTLO50vJHh5dtZJRCcqXRzSE9kmHEvzvQfgCb1gaAPspTPuXeG6DkClmq_Ms3VWZlQElnfJb1cCUusTtc4sIW5ytqwvIS7xeEbz07qHqYeMr7_bA6bjvnHlzr0fsvWbGnKlYEuBuAEZgBn2esS9Iw-eOGP9sAV2ERA4kxqv6MHyeN8Q-GdHn4ThkHHMaI5vA7xOJxf09MsPBLOP8b52_Qwd8DiT9ArAKiQ7Ve0-mwZNPGkMxcTnKcJWQBOIR2VSpT3SNtHv76CKYDjBRP7Ij9lSmRAOYEpfHBygdNBptHhHahfcHabWI3zpvHio3xD4Q1j1GoBdeGRcVfwt1Qvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه کسانی که دنبال بهانه‌ای هستن
برای پناه گرفتن در آغوش امن و گرم آخوند و توجیه حفظ قدرت در دست این‌ها.
این مفنگی، پدر زن مجتبی خامنه‌ای،
میگه «فعلا به خاطر شرایط جنگ
با حجاب کاری نداریم»!</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=UR_qCM3rrLMYdPQxHo0gBOfctRH-k4xCqT9F6VK9stBydtDa-K-R4gwF1QCG2uUiD4ZS1FqBKyJZw3yzusGWYT_tHnEto01gSJryqjAJCMj3qSXL2MIk-llftbndqmOZEurhuSVD-5ZJF2qkJg4qtRdt9k_p10Qp-59b0SinIuyEVC6Nl-70vfKOaf6kOwXDK174kufg5Ad_6LcXo9RvJidiPu93JWHdBVlc5mECEjrQ3iz7uzAgsG7aL_6DmDQsDdJA5SpnxhT2oirr30TPXbDzdbRRFsbtvHEkPk5CxYl1zNQPsVA-d9rCnubXx2j_f6xL4GorL0suAtDRdJXHYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=UR_qCM3rrLMYdPQxHo0gBOfctRH-k4xCqT9F6VK9stBydtDa-K-R4gwF1QCG2uUiD4ZS1FqBKyJZw3yzusGWYT_tHnEto01gSJryqjAJCMj3qSXL2MIk-llftbndqmOZEurhuSVD-5ZJF2qkJg4qtRdt9k_p10Qp-59b0SinIuyEVC6Nl-70vfKOaf6kOwXDK174kufg5Ad_6LcXo9RvJidiPu93JWHdBVlc5mECEjrQ3iz7uzAgsG7aL_6DmDQsDdJA5SpnxhT2oirr30TPXbDzdbRRFsbtvHEkPk5CxYl1zNQPsVA-d9rCnubXx2j_f6xL4GorL0suAtDRdJXHYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت دیشب این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین،
دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، دلاری گوشت میگیریم،مهریه کم میگیریم!
موجودیتتون ذلته!
دیگه ذلت چیه!</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ppmAJrKJprCmnqsZE-fCPAO-b3uLUBGfY4LqyN4l5Cte8wX3d71Sh_wCEYKz6R6KRcaVzBxJoUaHsn4FiFz1Ubiyk_5guWQTPFwKPxKeBBVTUWcOHzL5p-_qXlsqS9mXH2kZF0UBm_KTx4I6BWcVsns2OjqYU1J4Ri8yLrINqeiFNs-uMmQe01NhqznPyTuxcQx3XIoi7LGxuf_6-pNNCkXqw078lmQ7FusXyGPOo-UO-e-Ux18iSubzgQg-ZLQubtZtSB_KCFMMU47KeQrhtKjaq7hoSdgkCtaSmfYbH2jaGstuy8v-0L8k-2109FAPYI5DnH8a7UFuYCr_8YC7iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکر نعمت کنید،
بلکه این نعمت‌ها افزوده بشه،
اصلا گیریم یمن نیفته دست عربستان!
بگو اصلا بیفته دست کفتارهای
بیابان‌های سومالی !
همینکه این‌ قوم ظالم در ایران شکست بخورن  و به غصه‌هاشون افزوده بشه، جای شکر داره!</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=odtSBwiAV__UFimaD3IW3lbExDhwsXAEZjeS-9zd2fnkZ6I8bObSv-0g0j4tFJ3aPUCy5qwENW0nkBvPhXWsQLV0WkbLBM6okrFsjAxsjvNVBqMJtAhqt3cbbshD_b9426hTTYPC-QL5cYqHtRe1bPnFnW7tQMxa4AmTx2wAnmv7dTqHDJopOFEzz_iBlvZZiWVX-RPNoNkUO4Ei9NcYb-uQmuquKXfdn350pnrI2PiGamL-CSeV8IwguPDiLVJHSS2Nevr26ka_AJgyoWu5ADv6iLnSlvzvTVswJNHbk4ko_us938v2fg5c3kQgIQmCKDATvcS9XEaPwqx5OZaJvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=odtSBwiAV__UFimaD3IW3lbExDhwsXAEZjeS-9zd2fnkZ6I8bObSv-0g0j4tFJ3aPUCy5qwENW0nkBvPhXWsQLV0WkbLBM6okrFsjAxsjvNVBqMJtAhqt3cbbshD_b9426hTTYPC-QL5cYqHtRe1bPnFnW7tQMxa4AmTx2wAnmv7dTqHDJopOFEzz_iBlvZZiWVX-RPNoNkUO4Ei9NcYb-uQmuquKXfdn350pnrI2PiGamL-CSeV8IwguPDiLVJHSS2Nevr26ka_AJgyoWu5ADv6iLnSlvzvTVswJNHbk4ko_us938v2fg5c3kQgIQmCKDATvcS9XEaPwqx5OZaJvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=KjdOwPFv1W2v3Z7XGopE6Xn1-pZa6V2RnCzUbdLQCNkmXrhJebNtMhtJCIdRoeTe47jc91WseYjH2HgVsnEXTEXQ7I6hq_48DyFE--J2cH0uGJbdmahPY4iRw3nKb9B9MvQStTNC9U7zriaWnhznBnc715Un92b_KuLgm_LJBBQpsm_0kiYniBxPuavc_0oM8ZGaj9cD2OsdOZ36s6YP0XeyQE8IaNXsypXU76fykAGkrzb40kZbToXpJZMXc3XIbodkpC6crrYxyHcWrRVzDqrrn0gsTKpYhSreMDkvG8PMshYSq01jQoWNJ2HVdcvbJNufvnrsvwDInYSqlQD9mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=KjdOwPFv1W2v3Z7XGopE6Xn1-pZa6V2RnCzUbdLQCNkmXrhJebNtMhtJCIdRoeTe47jc91WseYjH2HgVsnEXTEXQ7I6hq_48DyFE--J2cH0uGJbdmahPY4iRw3nKb9B9MvQStTNC9U7zriaWnhznBnc715Un92b_KuLgm_LJBBQpsm_0kiYniBxPuavc_0oM8ZGaj9cD2OsdOZ36s6YP0XeyQE8IaNXsypXU76fykAGkrzb40kZbToXpJZMXc3XIbodkpC6crrYxyHcWrRVzDqrrn0gsTKpYhSreMDkvG8PMshYSq01jQoWNJ2HVdcvbJNufvnrsvwDInYSqlQD9mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم
همون ۱۶-۱۷ فروردین، کارشناس
صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه
رو رها نکنیم تا قیمت نفت بره بالا!
و فشار رو بر آمریکا اعمال کنیم!
چون خواست مجتبی خامنه‌ای اینه!
نتایجش رو هم همین روزها داریم می‌بینیم!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6715" target="_blank">📅 11:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6714">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=N9MFPrQG6cvSSzCxuvkxa2Bw4GSuZ9MKzvc6O8xmqZLUNhI1Uu_BzhIvr-xGc-qgvysGFA7AXh9wymYADvRjN_yanG7lLXJjsn53Fay9dn4vpIawKbUQVcEOv1zM4mSP-6-IR04Icspbdd5nWRVFn6bt8EwHpvI27p9Hp9sWyUy5kTijeBj0LbfLhAL6RR9hQyZnNZEU9NToj-_SaLOuPzGAVloTlR5_Chq49KHS_8MRO85uiEYyTIF9RR4v0u6EQzGsyQFHtXLkhbhs3ag4gyqO6Lq_JurIUYwk_wHbcgOIcXzHPQh9DzH-56v3a2u-ayE1z5ONjUX0rvTyRwQ9Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=N9MFPrQG6cvSSzCxuvkxa2Bw4GSuZ9MKzvc6O8xmqZLUNhI1Uu_BzhIvr-xGc-qgvysGFA7AXh9wymYADvRjN_yanG7lLXJjsn53Fay9dn4vpIawKbUQVcEOv1zM4mSP-6-IR04Icspbdd5nWRVFn6bt8EwHpvI27p9Hp9sWyUy5kTijeBj0LbfLhAL6RR9hQyZnNZEU9NToj-_SaLOuPzGAVloTlR5_Chq49KHS_8MRO85uiEYyTIF9RR4v0u6EQzGsyQFHtXLkhbhs3ag4gyqO6Lq_JurIUYwk_wHbcgOIcXzHPQh9DzH-56v3a2u-ayE1z5ONjUX0rvTyRwQ9Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون هم که با افتخار این  تصاویر رو منتشر میکردن!  بگذریم کل سپاه و ارتش و بسیج و مردم و عشایرشون نتونستن وسط خاک ایران،  این خلبان رو پیدا کنن!  فقط هی نوشابه پشت نوشابه باز میکردن و تعریف و تمجید از خودشون! زارت!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=p4mXPwoh2wHy6FJMOnTZYU35MzHsy-523zO3FQdMuJ0-MKlSn48Y82fMtzKtPO7bJF1FqKWsJC9Kmo-s6E05onrULPJX0wECNGcr5GgrjT410opwWn1Zi7tE7cvbv5LiP-eKf3PfUItKiev20F5p7OCDcIAcaD7OpHSknoT8g4PcWFq8f-ahPNCBgQq9m9QXLuyn4ER4FjcRgJGVFsqhvKf-0KKeF2lmkcK5RiJKuXsd1ODgwYNnQ49c-geRton573Or0paR2RhkYJmOUqAuo0SbDwQnE6oqnUSRe-v2EvHvaCY6CpOnKePjpMZDNQqmZVgHgjAOaU5eY7_b0jEMYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=p4mXPwoh2wHy6FJMOnTZYU35MzHsy-523zO3FQdMuJ0-MKlSn48Y82fMtzKtPO7bJF1FqKWsJC9Kmo-s6E05onrULPJX0wECNGcr5GgrjT410opwWn1Zi7tE7cvbv5LiP-eKf3PfUItKiev20F5p7OCDcIAcaD7OpHSknoT8g4PcWFq8f-ahPNCBgQq9m9QXLuyn4ER4FjcRgJGVFsqhvKf-0KKeF2lmkcK5RiJKuXsd1ODgwYNnQ49c-geRton573Or0paR2RhkYJmOUqAuo0SbDwQnE6oqnUSRe-v2EvHvaCY6CpOnKePjpMZDNQqmZVgHgjAOaU5eY7_b0jEMYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NLSRukpPy-V9buIsoENFWuOVZEIhoQaoxI_kMDXjEmQ2yszxP8J8mU8cskCbauxSUX7L4dnXps6C9SG818SdB2GYVWtKEcMUsvDoV3LYy2SJhqVqIT48jv8yI_dNbxzB0Ve2qa_hFpWdqfq1iFiZokt80yPSO3GAMlx5fmSpSINGGOt7l28eewuB4OKdV8SSxGz64FoLTVKLYHxsgF7dUcTmXlOPLEYkJ3j1cy133QdZWWxG_m-sDpii1Nn00Z2eM1BThrIz9n7WEegkznEmHAyqK4xjEfRlBgZ2onufsoMjB7RVnwDrEZ6dmI2x4pyEyMDjeM9uo97x6zkCGe0cFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
ج‌ا با ۱۳ موشک به اردن حمله کرد</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=qFp7gKNE9ecWTcJogIMpICHYCWCo8H9eLzIoGY5muV8dkIJh-BclFwX14mzWP37J8lNKEKaop6OfOaBtB2hGj7HAL3f7HxbqI-YFzHy46vLyCy-L-g6DeHozgSIHoGnDSUvuj3djTZSReo5QXHXVVhohw7wwq3F9M0t1IpsL1owAxTA8eoSyNYkh8ugfToVP4iSx7hKYacZpQ3d6LWfnCXrkTjC2t29BGOQh7TrDRbmQ7q-pAaYtJi_DtQKMYhGA3avi0dSovS8PXj2c-8TXRWnt2HA6QENwIIOTHZnIO4cQGfmAGA_JI7PiTkMCHYYnQuYXQ_YPIXwyKdock3kyfYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=qFp7gKNE9ecWTcJogIMpICHYCWCo8H9eLzIoGY5muV8dkIJh-BclFwX14mzWP37J8lNKEKaop6OfOaBtB2hGj7HAL3f7HxbqI-YFzHy46vLyCy-L-g6DeHozgSIHoGnDSUvuj3djTZSReo5QXHXVVhohw7wwq3F9M0t1IpsL1owAxTA8eoSyNYkh8ugfToVP4iSx7hKYacZpQ3d6LWfnCXrkTjC2t29BGOQh7TrDRbmQ7q-pAaYtJi_DtQKMYhGA3avi0dSovS8PXj2c-8TXRWnt2HA6QENwIIOTHZnIO4cQGfmAGA_JI7PiTkMCHYYnQuYXQ_YPIXwyKdock3kyfYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=jaUT88TuRik33n0DQdnpbDchSPsX88YPICElIkuNj0IXpqUUXOjgzSxBcWsU-wSTV9P2MUOhGozqKh315X-O6Id4OalhfXHrNFQxiIFJEkcldV2jGN_agBztrBwlFDykYMj4jd2csoWfgxC9hGREJGkrtJKy8KXeMnyaTRXudc9_uykQR9mJF91c6r9mDUjOQm2-dVlAsViAFC-V42H9ipeuov24glman6JbwuFm_REsDDoVupoVkY8FUlo_3AACJW5Nm2oOjKpOCrVhv7UKDPc6Xu2aa58dqkgRAYwzcvUXaMTrdbpkTHn2cUS6lBtBttUKyUtucmLI-Tolt87K3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=jaUT88TuRik33n0DQdnpbDchSPsX88YPICElIkuNj0IXpqUUXOjgzSxBcWsU-wSTV9P2MUOhGozqKh315X-O6Id4OalhfXHrNFQxiIFJEkcldV2jGN_agBztrBwlFDykYMj4jd2csoWfgxC9hGREJGkrtJKy8KXeMnyaTRXudc9_uykQR9mJF91c6r9mDUjOQm2-dVlAsViAFC-V42H9ipeuov24glman6JbwuFm_REsDDoVupoVkY8FUlo_3AACJW5Nm2oOjKpOCrVhv7UKDPc6Xu2aa58dqkgRAYwzcvUXaMTrdbpkTHn2cUS6lBtBttUKyUtucmLI-Tolt87K3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lp3bTmgYXl414qMfjf7S_6Y6xlXElbAMJpOwU-LgVELsSsyn8Woq6sRISa5ZIEVIXaqDt5HLsxo_Q-cAKldRF5noSYnpRPoQ_MkP0AiOI4GYyusUeQ56bgYxJwX4M9_YmDGF7hF2Gc578u4Uo58AihBha3hqlkrXj2ZuXzc1-fYqlg8SyOFNIShoY90FChtfto1pv9CcC1WbsMw_LjFTl8kexSMogbwIDEUpQ2CIGLHtqVzU0qUm05RuJjhm39tflwymkJNEIdyBB56vSoKsEOXj3dS8oyf5bznz4BHftenjr41ohPgMrAj5FR1MAZn2zLVNeA7rSzF-todf58D7Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FL3iaNErd9Tl48Nsvlip5jB7a-aLqJ9_-Qc_rX28UTWYyPlPPy8uC-at3GJmu7Rwj2CXzn1Jgv-Agn65O7W_4RAo3w_mMN01fGnfUCUqXM7HXpaEVaK0_ogDydOYA-6XunGJ6v8CSMcqS84iRDgUzuJcbw5O3Fyxf3UEdFGcTpi-xjgHpQrHmTqZstSJeAL4_dmdlBejOuOR3y8s_lJbf5iJ_7L6nzoxCHc-DblKjo8wbP4TN0xYqtPnZ-1Uai6L_j7EB3IlmYMQCorInattyzhS-XFagkEKUeBh92JEg2-wvQowDL0neYCACcS_nk1emoQ9GbI_1aLDbVf2RYSVXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=JvfDXK8KCyFwIlN05GF2RXbAtHRo6J3oxdJi027uEkiau7iR_O1yfFlpcM4fR1YkBGLYEMhoVGgdjeXOl3hAOrryBD6i-K_ReMrd37z8hwoUZvwJh5meNO7Q7iJK_uNdB2RdqJ72GCGqUd6FgoYkW_FwIVQMHY6BNPOnwfo4o5GI9Ontx0boVjD_00Ix0lWubIEHA6wFP4PYk5yXkRLzt_3rRqpo4sCA5FkVfcWGo6cq5jzEK7H9TmgVxxTFRIUwEhiuZJRGo2uS4aAsc-oCQp7n2Y4AivDZDTrHvC9Va5_i7GsAyfMtk9JpTCJzZon2zIGsB2Jaa6BVRQ-9OPORBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=JvfDXK8KCyFwIlN05GF2RXbAtHRo6J3oxdJi027uEkiau7iR_O1yfFlpcM4fR1YkBGLYEMhoVGgdjeXOl3hAOrryBD6i-K_ReMrd37z8hwoUZvwJh5meNO7Q7iJK_uNdB2RdqJ72GCGqUd6FgoYkW_FwIVQMHY6BNPOnwfo4o5GI9Ontx0boVjD_00Ix0lWubIEHA6wFP4PYk5yXkRLzt_3rRqpo4sCA5FkVfcWGo6cq5jzEK7H9TmgVxxTFRIUwEhiuZJRGo2uS4aAsc-oCQp7n2Y4AivDZDTrHvC9Va5_i7GsAyfMtk9JpTCJzZon2zIGsB2Jaa6BVRQ-9OPORBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m_kCJVFkKu4ib85MiGETQQ9mopvidTSHeKABHxiA-MLPkTLmk5BRz8UecQWBMmjfCgEiDUd3lpY62_5ZEbMTtd8nKrEj1Ww_PHzOAO7wfnvqg9jKSV_bKS-euj-anb3W37OSf24vCiD3A2bCOy3j6mhcTZrk9I_vM4ptu_DTH5vZsrcjC7j0OT79OpPVTfWEUMbRazk8Y90gnLCRGOF9kVowKO2YR6j1fqUFEYteodTetrqxBk54nf54wPrmHusyyYFrAk7Q04bob8MtZ38_e9OLns6AkUp1ogAHfyIUt-Nn9kEBbErcm-rt3FjW1dq4sTQPj5FgX4goeuHv9k2Psg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gtWOKFA3iYeAxTYfRtrAoybfoVShXY81L8lrqY-eliyd8O9Rt6KusL-ljWTO6t6liIJgrTLCmMHETuWQheCWllHc5HublnAmIrbkmRgGoX06zYk8xHSfK-PIEH-khAQnZhWEuaJxF6Fmy66EbxTkFlELD8giZd079-2WcL1-gaA8M7m4sEuUzvZn9xHEDp8rsu_rsDlpgiQOelCMuDglYsVKmHMiOEW_eWOVgflq6SqpRlZz4XXsKRGeJyWz7XxArOOOSRF7BWrcXC2F8C7hNKUNw-aiOZMu8LwD6gjxtD5OdOftjPSNcNCKrNYWozGMTip9hzkDNOE9ZhmtWTE_DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NLH2nUxGs1vFSMD4mz_N7d0JZoIVP29XpsEswlFFcVfr5ph9Q2OqMJsQlfqjnt-9FjROgGJcVx7SkBs9lWRT4iz3v7RliG5KF02-eSfZoTxUiA_u9MDpm89B8_SzAWBN6hV0D6lXjsh5YBl8pRTSg4MrE7aHZdPw-DjPVR-TsSqNNkMKaG6-3GDR6z7Kb9Ae7YBSc422-LnyOmcClwL36EDviC3caRY1jm4Hn9ff2KdVwTmhGXPCVZ36SdA-KvSOgYzfd6GAN-GCJ3xEDu8y7iEkuT_lEL-eEnl6nKxEdQJ1CGS0fQzfCajR7x2z4kCSRwXBRDscXjRmofZ6EyEcEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها به تکرار نوشتم،
تنگه هرمز، تنگه احد اینها میشه،
به وسوسه غنیمت گرفتن و پول‌ درآورن از تنگه و اعمال فشار بر بازار نفت،
دست به کاری زدن که جز زیان و خسران برای خودشان هیچ نداشت.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6694" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‏یک مقام سپاه پاسداران به نیویورک‌تایمز گفته از ماه ژوئن تاکنون، بین ۷۰ تا ۱۰۰ عضو حزب‌الله، از جمله مشاوران ایرانی نیروی قدس سپاه پاسداران، در تونل‌های اطراف ارتفاعات علی‌الطاهر گیر افتاده اند و مقاومت میکنند.
‏این مقام گفت حزب‌الله بارها تلاش کرده است با استفاده از پهپاد، غذا و آب برای نیروهای گرفتار ارسال کند، اما نیروهای اسرائیلی، رزمندگانی را که برای جمع‌آوری این تجهیزات از تونل‌ها خارج می‌شدند، مجروح و تا سر حد مرگ زخمی کرده اند.
‏او اضافه کرد ایران و حزب‌الله، تخلیه تسلیحات و نجات این افراد را در اولویت قرار داده بودند، اما اکنون به نظر می‌رسد احتمال موفقیت در این کار روزبه‌روز کمتر می‌شود.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=ZNTTaeogQGy7dypmjFXdOTBpNgfZGHdOzbQoYlZvcpn6Z3GP4XW61DaOifWOiI-uNSiZ8a2eFDEcI862Irs5vznvcTgB4LKWhUP2BNi0YVWV55HQ8xiwD9ECNVfDWGroZjyajbfPXyhUhYNxOrhu6uiph9u4Vfi8nfvOZLdV4tg9RM977ld71vfEd-Z7aqNsHI12CTlN1rkXP1qZm4osBZUreatwiVXRN0ooTvedEzbP1dQaCE5djnKv5HIXWuAlcd6hLWluXjr1cC0n9Gzn8rWMqOIKDWVCfsDMih8zoTePvkz7c02fZRQrwUGhB7cCKl-wxq5Yaazk3akMd4GLsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=ZNTTaeogQGy7dypmjFXdOTBpNgfZGHdOzbQoYlZvcpn6Z3GP4XW61DaOifWOiI-uNSiZ8a2eFDEcI862Irs5vznvcTgB4LKWhUP2BNi0YVWV55HQ8xiwD9ECNVfDWGroZjyajbfPXyhUhYNxOrhu6uiph9u4Vfi8nfvOZLdV4tg9RM977ld71vfEd-Z7aqNsHI12CTlN1rkXP1qZm4osBZUreatwiVXRN0ooTvedEzbP1dQaCE5djnKv5HIXWuAlcd6hLWluXjr1cC0n9Gzn8rWMqOIKDWVCfsDMih8zoTePvkz7c02fZRQrwUGhB7cCKl-wxq5Yaazk3akMd4GLsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ناو آبراهام لینکلن بود که ۶ ماه پیش
با ۴ تا موشک بالستیک غرق کردن؟
خبر موثقش رو هم  صدا و سیما پخش کرده بود،
خلاصه دیروز رفت پاتایا  !
و یثبت اقدامکم فی تایلند!</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=Fx-CBoshzoeyAoUuiMLgdhjbUtu-z1AwbDVOMm9eWQHjYgJ-LypF2MpBTkh853C8jMb4rs6lr8seuFohWjzT2VBaaSCn4uVCQCNtBGvpPXG3SaCaJb_paZNNKS86jHdMCbn-JACnYexLGeYITYy8M2JJT94o6iWFeVdn2VEsddIF6uTjcLAmvgh_dviaIPGPVcL7pG5vGRHrwJm2GeUQVbXK7GIObZvMSWALhKCWp4RXMg0gplUb-6NzO8ltYDWYSVQFbzc8i4F-bLSUJ3oXD5yYvCHp6dIMzQ_-_dfAJwM0ik_UIjpLIH9QD--iGNh3wOH_APh8D5-Iva4jgNsP4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=Fx-CBoshzoeyAoUuiMLgdhjbUtu-z1AwbDVOMm9eWQHjYgJ-LypF2MpBTkh853C8jMb4rs6lr8seuFohWjzT2VBaaSCn4uVCQCNtBGvpPXG3SaCaJb_paZNNKS86jHdMCbn-JACnYexLGeYITYy8M2JJT94o6iWFeVdn2VEsddIF6uTjcLAmvgh_dviaIPGPVcL7pG5vGRHrwJm2GeUQVbXK7GIObZvMSWALhKCWp4RXMg0gplUb-6NzO8ltYDWYSVQFbzc8i4F-bLSUJ3oXD5yYvCHp6dIMzQ_-_dfAJwM0ik_UIjpLIH9QD--iGNh3wOH_APh8D5-Iva4jgNsP4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادتونه قالیباف برای لبنان
از اینها
⏳
میگذاشت؟</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=lt8QRjSjOXZjWB2O8x7pkHSbAo3v7N9H3RzPnomgOI-IAFLbDeOT-6NAmIZdjn7-kHUht40plvIO9rOKnadYYK5lgCCzi424qAfAl623KCTUero0_rwXPwTkfvVrAWlUT_Zfb-DUAmrA-dYdGm8pvmeaXUuF19waAgngKrurwKKM-83AigseNTRrpwstgzA0g4EstA_ZoNtQLVFjaC193ubFprA7SpIR4Fw8152O_V3VJFhZJKMiNKdRF1g5oyl4izc_0JDytGJJv_fGEVO3v_5pol9r60CSJAFUj1aXVx6Rb3z-17JaupSY2ZiplDxYT8LnnOY7RXhvD-ekpIXB0gpQ1A7fz5NdSETLpKbENb1Pix56uFwCGzSVi_XnMp2zEVZ-h63dDf4YkUr47Y8f_JsCUMAsWXGKdshAPeBreCmkq8znLten4mWejPPFglRfidOairKo2tjWv_hktbti0S7RnDnaEmOUPgs4VZ6vc01Z_7iK3XPr79hmZ051Mc0_Tks7jDJ5Ik0DezwoLaGtHRRujhAjn-WoWRHr6noNIzM2MLFJKiZqh4fGTHeJyuXmW1KkX_JdEKI0-GEUm8WH85iU0Dc8XFpDP3PcJeCjzjpt4biOt5Bg_TOZEKgfm4wfmzjeVQBFpFegueLRuyJvFE764vwxW81DAI_TG3RmsF0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=lt8QRjSjOXZjWB2O8x7pkHSbAo3v7N9H3RzPnomgOI-IAFLbDeOT-6NAmIZdjn7-kHUht40plvIO9rOKnadYYK5lgCCzi424qAfAl623KCTUero0_rwXPwTkfvVrAWlUT_Zfb-DUAmrA-dYdGm8pvmeaXUuF19waAgngKrurwKKM-83AigseNTRrpwstgzA0g4EstA_ZoNtQLVFjaC193ubFprA7SpIR4Fw8152O_V3VJFhZJKMiNKdRF1g5oyl4izc_0JDytGJJv_fGEVO3v_5pol9r60CSJAFUj1aXVx6Rb3z-17JaupSY2ZiplDxYT8LnnOY7RXhvD-ekpIXB0gpQ1A7fz5NdSETLpKbENb1Pix56uFwCGzSVi_XnMp2zEVZ-h63dDf4YkUr47Y8f_JsCUMAsWXGKdshAPeBreCmkq8znLten4mWejPPFglRfidOairKo2tjWv_hktbti0S7RnDnaEmOUPgs4VZ6vc01Z_7iK3XPr79hmZ051Mc0_Tks7jDJ5Ik0DezwoLaGtHRRujhAjn-WoWRHr6noNIzM2MLFJKiZqh4fGTHeJyuXmW1KkX_JdEKI0-GEUm8WH85iU0Dc8XFpDP3PcJeCjzjpt4biOt5Bg_TOZEKgfm4wfmzjeVQBFpFegueLRuyJvFE764vwxW81DAI_TG3RmsF0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهم‌ترین مرکز فرماندهی در جنوب لبنان
و مهترین سایت موشکی در جنوب لبنان
که از دست دادنش یک فاجعه است.»</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6690" target="_blank">📅 21:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6689">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=bV_-62nhtWYO3r6100t8N4XcazcVlQ3UPizzt2QC8ClDTTDbnNKt_cK5jUp8PQ7tWcAqCWM6JS5hUjLmDV1fQxJSsCy9VpOcC4-HD8l8d1cu5t3i4TwlEGRaA6K52i2zJUY9--BG4PuhfB8AM2_-A9yZk3VcJ4g7Z4yXVx9Fm3xl3HWvZx7Lce_jSxzCywxOhm020SdUbnNYN3iLqKCDJU4g44OZLmuy-WgzZxKCDIPmeXwdYysG_SM4F_-75fEAEZK73Oz7C487Yc-ESVfql_qPOI2Gb9NLPnRhbFgXzAgG9eoEwYQ_cGa1ESuurBfrWRm7R98AJ9xWXwIVUS-wsYEIwRUERPxeuMYrV8P3-7yYxh91zmaB_KSutWjPZc4S8KFD7abcwYz1KKubG6gtxCRCXQlDHb2NLa-X_0KT-B7H73edQfMryMjr2m1WuQIL8n-vPrvhHNZIbTr89rIJvzW4hFD3pl1kGpTNMI6x_8jsWQaOp6mrentLWKKVom-JIcTZZxekROv4KciJRcInuckq4krOvB0lQRRDtH2TJkDiM_qiIg7ocrHdWzo1L5bX84QMm6YZczdnMnwrP3-H6GbhNbxXL9vdsTvSp69TaL7KjFxmGgeYBM4FsvCYOQn-PDwRoa364BPkjKd0c3jR9s4pEbRdSWOBo71h5--TsVY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=bV_-62nhtWYO3r6100t8N4XcazcVlQ3UPizzt2QC8ClDTTDbnNKt_cK5jUp8PQ7tWcAqCWM6JS5hUjLmDV1fQxJSsCy9VpOcC4-HD8l8d1cu5t3i4TwlEGRaA6K52i2zJUY9--BG4PuhfB8AM2_-A9yZk3VcJ4g7Z4yXVx9Fm3xl3HWvZx7Lce_jSxzCywxOhm020SdUbnNYN3iLqKCDJU4g44OZLmuy-WgzZxKCDIPmeXwdYysG_SM4F_-75fEAEZK73Oz7C487Yc-ESVfql_qPOI2Gb9NLPnRhbFgXzAgG9eoEwYQ_cGa1ESuurBfrWRm7R98AJ9xWXwIVUS-wsYEIwRUERPxeuMYrV8P3-7yYxh91zmaB_KSutWjPZc4S8KFD7abcwYz1KKubG6gtxCRCXQlDHb2NLa-X_0KT-B7H73edQfMryMjr2m1WuQIL8n-vPrvhHNZIbTr89rIJvzW4hFD3pl1kGpTNMI6x_8jsWQaOp6mrentLWKKVom-JIcTZZxekROv4KciJRcInuckq4krOvB0lQRRDtH2TJkDiM_qiIg7ocrHdWzo1L5bX84QMm6YZczdnMnwrP3-H6GbhNbxXL9vdsTvSp69TaL7KjFxmGgeYBM4FsvCYOQn-PDwRoa364BPkjKd0c3jR9s4pEbRdSWOBo71h5--TsVY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=DNDtxKNNQIO5x5nfiEoOl5xgcgk4OcW9_a4tmpQuMJw2HxTXa2-cPvBOOfgt276TV0ZCXy0og65ZvX2lxSbXD555fVqbaSQkn1h2HDGhbrV3VNvci7pUjbO1kY516-lJnmxl57SmtRn6VcchreDZ0TXp68S6TtDXXsATCmVFys2Hion9sum-OB4Sx6PUz44u1636wd7r1UGtC7YGsH_hkSfVM58TXB71aGoKH1T6mhA3WKMyrII9eRbkp0hGu3CsCgu38G1Tnn3r60KDI_AIDGVHdeCt4FZkch8iJ7IuyPnP_kGV9hN2abhg40y8-UzewEL4tOnDztF9Wvw5BW2zjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=DNDtxKNNQIO5x5nfiEoOl5xgcgk4OcW9_a4tmpQuMJw2HxTXa2-cPvBOOfgt276TV0ZCXy0og65ZvX2lxSbXD555fVqbaSQkn1h2HDGhbrV3VNvci7pUjbO1kY516-lJnmxl57SmtRn6VcchreDZ0TXp68S6TtDXXsATCmVFys2Hion9sum-OB4Sx6PUz44u1636wd7r1UGtC7YGsH_hkSfVM58TXB71aGoKH1T6mhA3WKMyrII9eRbkp0hGu3CsCgu38G1Tnn3r60KDI_AIDGVHdeCt4FZkch8iJ7IuyPnP_kGV9hN2abhg40y8-UzewEL4tOnDztF9Wvw5BW2zjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FfX4ISWgxPXj15XUwIk2JTRKsgqIPpVJzt8oBz6Bp7oeYzXsYcPLXn9FlZwKafJpzScVZVgNTyXs0nvuXT6nDM0Jl6tdujwkdXymF8L2zUlmyKKkpb8a15iT4nvfWWCrgtdr5z6v5OTQSEuE9zg50bv-mt2007xKfpdPSexowz1Dq-w0IRLI-pGafoy1xmy6EyIWZMkQLGks597--bbLh88pLgx6OPk-vKvSNvHvnNExaAckvycqzGzlJ9nlF2CLVrwIEGXk1p6sEWK9vJwG68fYzx8n_4YcjmHnthgwCOOwu-3DyNQCiiroMwXj_0W9TEe_aPD3kLKxmXAJSFJ3fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=UCqYiZD7Om1-KteTCzxMZS3k9japyN4czyo45LVaExNs4f4C11Ao8R9_-c9wUJwRM-UXbdBje2IUy8QobgHZC3BcgBwav6gBQQ9Z7sYlg6EtEowakVpbsdMTf77KmIgj4I6wPNffNehC-VsT-M1zm-IxVMvSoK3t4f_wtxf_WMQBwyXBrLTZTagbH725ZYL1Al5Sb979iGzMSLQY14ur9HzL2rvxAk_d5CnrHxDNmdX2Kvj9FIboqsKKTy1IKSY-HEm26bfqtljuS2JgKIBMLb9aBIWzSGgpG3WR4e2uT_3nmrNDOVF3oX1AsUSFVdKEofEJQYJ8SAXh5wxi7NXmFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=UCqYiZD7Om1-KteTCzxMZS3k9japyN4czyo45LVaExNs4f4C11Ao8R9_-c9wUJwRM-UXbdBje2IUy8QobgHZC3BcgBwav6gBQQ9Z7sYlg6EtEowakVpbsdMTf77KmIgj4I6wPNffNehC-VsT-M1zm-IxVMvSoK3t4f_wtxf_WMQBwyXBrLTZTagbH725ZYL1Al5Sb979iGzMSLQY14ur9HzL2rvxAk_d5CnrHxDNmdX2Kvj9FIboqsKKTy1IKSY-HEm26bfqtljuS2JgKIBMLb9aBIWzSGgpG3WR4e2uT_3nmrNDOVF3oX1AsUSFVdKEofEJQYJ8SAXh5wxi7NXmFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">جی‌دی ونس در خصوص ایران:
ما با ایرانی‌ها مذاکره نمی‌کنیم و تا زمانی که آنها شلیک به کشتی‌های تجاری را متوقف نکنند، با آنها وارد گفت‌وگو نخواهیم شد.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=hhQZxvppo9RwkiZIEzuwBVIsFEmfKpLeBPCNQkyG5Tby8hA9QnoNSe-nyMmdbZn3xiW1qaRUm8A4_8F0rGgRbLg_cy8cfXNdwrGKJs280-AAJaJXfoYm7hg_odNwIVivYWP7ZAD8qyTq-aVqgshdYZMcWgnL5iyJ-RIB4b2YRdiJw0Ydj4FWJ8_GAhyWDENbYlDcGS1-PkpfeiqPDNZAQjBEvJd3pVaIXFF5fUPEz6FnhEZbZYRHPBjzUFCWgQJg66CKXfVRuosaK-dv1GBM89cpd31V91KF3t6QTo5KKutikAdCvZmlwYXVgD_zfLy-hg746Kz1zAMrL58sPArP2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=hhQZxvppo9RwkiZIEzuwBVIsFEmfKpLeBPCNQkyG5Tby8hA9QnoNSe-nyMmdbZn3xiW1qaRUm8A4_8F0rGgRbLg_cy8cfXNdwrGKJs280-AAJaJXfoYm7hg_odNwIVivYWP7ZAD8qyTq-aVqgshdYZMcWgnL5iyJ-RIB4b2YRdiJw0Ydj4FWJ8_GAhyWDENbYlDcGS1-PkpfeiqPDNZAQjBEvJd3pVaIXFF5fUPEz6FnhEZbZYRHPBjzUFCWgQJg66CKXfVRuosaK-dv1GBM89cpd31V91KF3t6QTo5KKutikAdCvZmlwYXVgD_zfLy-hg746Kz1zAMrL58sPArP2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gzZHRK3MSKyQwZ2sO5Mt3aVYa3j-uNwb0fLAitI-quSwEiMxiQlA2ynboV_d-Shx4g5OCky-3-KX11S-kvMZs9JfBvMcfpGwVigxJSNBV8Mk09ZiG4fQX-gwtFbHxPd94ySmOQJeyYy_p-u0zvVxfiWg1_bvH9GEcMeKSIkpkL5ZECz89vlarYJ-HKoaVtfpeSbywoJDuylcAGkYA094SYQYJ56gsfclCwo7FOcnBpMMi0l_hNvhdmnOSD7jxQq4XfiEbs9v-66jmeAIfgnvytij3RC6GCaVc5PuWsL88j0jjFpwykLYCq7hA1asz_w6QaK6jw5gUoruYWoI4nF6RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tsE-dReoUE4lqHj07yaNt1ZyYMWswOl1Ounm2dcECA36JSi-G_UmRbK8clgKuA9rZhrp9n3DltQrqHurgPPDkXskWg1YmMk0Y9WDAsBtjv3aScy14e5Ylcr2isNoHVbcFXJ21SaEijyJ6pa3hmoZEpo1vPZPkdS6wX-cTIae6j-P04hKIibI76U-dS_aVwwqVRZCTC4G9oqE9tsoCgSYr4NBRPdt0CjV69j4W7ty_L9nImzy8BemKu_84bTU31qh0izkljLEo-U-zezWsWXQl1JZ8pJINcCYjALlW-dLzHu0XNbnmKQG04vCV2ZcIxfWvFPOaPfx0vOTxprbeGGUiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vNSOqY5aWtzqM-Bx4pytKGKs4d3QPzD-YTsoNTgcpZuPxKOsIOH9bYJC6ek9Hxxq1PQEY2btI7aelvNnFKVpErtd6AaYALUwN0VTdxXQ7VXxWy3sjgpB3QIc_mhljyMT1lluLX6keHt5NcoUDGelv5GqFG9WKn3o8S12x-2klyWycFPVzekRXf8-ZCbASp3ZjWB2y8MA5sVi912Bz2BsXOxANubwU4CdQ0vdPg7Htv66oSKXSfSAyuq8NqcVys9V1Lwbj3XPUPuisZGcGca3dz9zJOFQDwoa9DkmNHigHaEYPtD1FBPqbJcWL2tAVCa5js60xLTTkIZJ-9MXvX2l9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بزرگ‌ترین تولید کننده نفت جهانه!
آمریکا چهارمین صادر کننده نفت جهانه!
آمریکا بزرگ‌ترین تولید کننده بنزین در جهانه!
آمریکا بزرگ‌ترین صادر کننده بنزین در جهانه!</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
مرکز رسانه قوه قضاییه: حکم ساعدی‌نیا در دیوان عالی کشور تایید شد؛ ۱۲ سال و ۶ ماه و یک روز حبس تعزیری و مصادره کلیه اموال و دارایی‌های منقول و غیر منقول.
اعدام، مصادره اموال، کشتارهای دسته جمعی و در کنارش روضه‌خوانی و قیمه است که اسلام را زنده نگه داشته.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Or8vJYoWk9jeCyrD3GmvM97socjk0-TB1nOg5y2klnevB7Y_f06JweotmPRtr524LBrvRXth18MLb-Ydt4uL0AuKyydwp5DYgZ-ZFnSv7oDUjcoHxpbcI3Q1aKPKIv7ucVOAuz6_-hs_JeeSMvEFptUbFqrVojtYHrSvyUkWbeuUirb5XU659xtya5Qdnmw6D3WWvABjG26dH0OD61ieXS2XL_zNK0CqqyLBH4l56CSinbVMLsQCBjYaKXYZXxKOnArAgdwOFU0yH2e4612L8gP-_43Q-Viwty8zuSyavxTiKNJgUuGsOBKZYaN7S_NBR1Fz2WwNZpu7V3e98z208w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پزشکیان
حالا قالیباف هم از آمریکا خواسته
تا به تفاهم نامه برگرده!
تفاهم نامه کی شکسته شد؟
وقتی حمله کردن به کشتی‌ها!
و گفتن امتیازهای بیشتری بگیریم و غرامت و پول از تنگه هرمز!</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nw6iN1T3IY8ZfHglXDZOYiumccobc9LzHokduk1Yy-B5ifnPlGCiD4aXScaUOoiilvF1f9M3oIYgEug5fa1AeMl5MB3ldlD95TRkckBQI-5DLjU6ddc_VomRWJqHfgX8Lamh0zvtxqB4UW_dnT69PvdSqRThXznFkhHelcOu2FH8QNln8e8rCPiJtLKFjUzhK3SbYC9hhUCt5N0RYwVTBjKupuCWw6-eaPVbUtZ8SVrXMrZ_ZRsYP410E8vpBQSoZk328AZD2qFLzUYpqdusX9vzcMOLZKUfNOrMVwZ6CE1Jf6mGH9HkItUb7R1fOGCEPSgvHqen__pRCpVVwU--Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vmAfu-YmuOFZVAhxyMJqxOMdtl1K0-AEue5cfjQ2WDncXESttZPSlzqyNu17eTcU1xiyB5e95QIhz3fuExp1meYbhtLdwBDTQQ_G8SSLtvymIb3FYCzmvKOKv5EzIuSjiWdIVIVwluuAL1cq5nXeJJG7ZBNUS1CgZN1A6SqEeIcwoTJsFmgVVV93xk5GeJfODkAGZYoAAIepoAJ4GSgCuFmJYn2bOdj0Lxg4-ocbXNqKgApEvaJ8Mdos5QEJC3mvlZs6mZME9kobStRKC0LOvhSLVzIvlol_knTHghUQGIlF-fLSiCZmbRZoRqMm10dX3CEhxdJZ2iI_J1lWIqVUQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EeZdq_pCJagd7TJNU8_eRNw1924hLtKZxgbCq_l4AOjme_qswtDLYbUmYBqaOD-brmto_fDxt_Ivx-vthS02NCwtevGVju4YJcx1JNiZPGFuSRbHALtbr94a83wqCKRtCo-_5V8bY8CxBcUVoHJamgI9hye6m_e3CPxh4wYKRZerbeFTn5ZUsX35JWG8FCg7yOBXC-g8Bj1YA3FOujFb1zSMKXImnn_gYDtlYr4_-N_Adkp9z4j3plJ4HoA2qKnL2lCtAygzUojL6VM4KdnHM_cZUG2bTr_ZSfXJWmCYX1N2tK0avwroq1ptGw_tBvV3OCJ9MfV-Iw6TTfh-kFpEGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GQMLakp0zZ6aaCVqY3KFq7ZiZsPXwKhscfmVXOCZy0qEVD_9Oqs64dBkaZdKmxLDAkVqRFA-vTqm9VTBR7GHBCKi5IN1yKv4_VjuWPGJkfLxARNk-vwyroJLz9ZH66zovlaYslgzyPkPMd5AFmfJyZW5mT0WpI8eBB-30OBeZCI4xCQuLoVo0yFdd92hMXXsp_Ahoz8eYWABT2LAP_sVYKmEEq3auwKnlybZmMgesmLg7aVEw2d_hyEibWAbZ7d-Mrky__sH4jBnBDToAlSUjpnrhYmhUBJCetRUVo42Atb_c1qfGCcCPomIVmeSyXHQ-SuQRXaO2u4BhLXN2af0gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qKyJrlK7NShrGNJvt73k-YM3jOi5WVjB_vpFrSvlaBtpCEMVnIQji4pZTvO4eaC2ciFZHTO5QenlvDAbPLnLPFE7zhF4iBe3d54l1SI6UrCcgEykfpQ522A7imSRb8SAYQCcJQbVR4ZJsk7zDf0oCXGx7w1MtUIjHVufqwks6cB-sE2sYbUm3w802eNyOFrxDugqbkVTuuH9natPQNqhV-9W5NzgYf97RmUejY-izHRyhwDMDfOyxkPXPLSGExTKVJ83TirbQSI_vYvKp8deobIx-9yw222hMs6x8shHb7mDRumciMW5-l3xoa9l3O1Jc1PMXfyOXaJEMsHEC5OaTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UZ1MuIZACDTL8TKX4HxJ2h6g0WkNd8GkTd0C8IwwpYOo2pGgCYGlSP5LkleHkIAPEZuGSHmKzsSIT4gZKPtxCL6MXdblQJm30Z9r06U7Kcw1KIi4kyQQNh7uxMSUgsCuAzzomNilET8lqByFtYpZkZQAT16zRCwZHVQHVKgsMfgucg1wrPf2buXCCw5uAYiZvyArd-d1CEsm7YGjQvNu1qX3rLjd2UNROy3jZ9msgdgQ41FHFFBR7egbzsUIgSM6EiinCq0rbzhwYYn-wpkHASwFKdUxPKPgp9RAyB15FrQK9dppiXEu-w9W3WEwrmRLmMH3i-VOxx7K-z62_-VD9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس جمهورچین  حاضر به نشست
و دیدار رسمی با پزشکیان نشد،
به طور معمول در حاشیه اجلاس‌های مهم
بین‌المللی، روسای دو کشور در یک اتاق و در حل اقامت خود با یکدیگر دیدار می‌کنند.
(مثل دیدار دیروز پزشکیان
و نخست وزیر هند و یا دیدار دیروز پزشکیان با پوتین)
اما رئیس جمهور چین، فقط سرپایی
حاضر شد با پزشکیان سلام و علیکی داشته باشه اما نشست و استقبال و…. نه!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6670" target="_blank">📅 08:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6669">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
حسین مرعشی دبیر حزب کارگزاران سازندگی:
«چینی ها رسما به ما گفته اند؛
۱- تنگه را باز می کنید.
۲- عوارض نمی گیرید.
۳- مسئله تان با عربستان را حل میکنید.
۴- مسئله تان با امارات را حل می کنید.
بعد از این آقای قالیباف می تواند برای دیدار به چین بیاید.»
نکته : چین در ۲۰ سال گذشته کمتر از ۵ میلیارد دلار در ایران سرمایه گذاری کرده، اما  حدود ۲۷۰ میلیارد دلار در کشورهای عربی سرمایه گذاری کرده.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6669" target="_blank">📅 08:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6668">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
۷ کشته و ۸ مجروح در پی حملات آمریکا به خوزستان
استانداری خوزستان:
در پی حملات موشکی شب گذشتۀ دشمن آمریکایی به ۳ نقطه در استان خوزستان، ۷ نفر شهید و ۸ نفر مجروح شدند.
🚨
دولت پرو روابط دیپلماتیک خود با جمهوری اسلامی را قطع کرد.
🚨
در جریان حمله آمریکا به کوهستک هرمزگان ۴ تن کشته و ۵۰ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6668" target="_blank">📅 08:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6667">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">نیروهای امنیتی اسراییل (موساد و شاباک)
با ورود به نوار غزه، رئیس دستگاه اطلاعاتی و امنیتی حماس را ربودند و با خود بردند.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6667" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6666">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=XPTRgXPwU2JiYewnArT96ZIIL1NEDgryPLp_o3ET49dvRskgDdC6WCdUSQZAXPi9kjBVRAH2a13Vtq1hLrFN7KjJWIkYL9FsZa23HHWjS_mVnh7UL8CkXfXq1FnkPWsmqco36CJ7jN1yZ-o3erIJFwU_h6hOjMSAzk2MHCKMbyvNHipURY06Q_UFLs-xa1EvIWorVmWpT14H5JL2pdkyxQuCXFmkGpZUUhfYBPWXlQIuKfBsua_RjpxFisu7_LYRG7PzxTs0novlFHpHJF2kgd6dxdyDL2arbeET-F3gI3yse14ql49q4ebTzUzvND6429VmeK0Ssd6cUq3bM6zWkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=XPTRgXPwU2JiYewnArT96ZIIL1NEDgryPLp_o3ET49dvRskgDdC6WCdUSQZAXPi9kjBVRAH2a13Vtq1hLrFN7KjJWIkYL9FsZa23HHWjS_mVnh7UL8CkXfXq1FnkPWsmqco36CJ7jN1yZ-o3erIJFwU_h6hOjMSAzk2MHCKMbyvNHipURY06Q_UFLs-xa1EvIWorVmWpT14H5JL2pdkyxQuCXFmkGpZUUhfYBPWXlQIuKfBsua_RjpxFisu7_LYRG7PzxTs0novlFHpHJF2kgd6dxdyDL2arbeET-F3gI3yse14ql49q4ebTzUzvND6429VmeK0Ssd6cUq3bM6zWkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها یک خودرو وارد جمعیت حامیان حکومت در مشهد شد.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6666" target="_blank">📅 23:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6665">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در بندرعباس، کنارک، چابهار
سنتکام : «امروز ساعت 12 ظهر به وقت شرق آمریکا، [حوالی ۱۹:۳۰ به وقت ایران] نیروهای آمریکایی حمله به اهداف سپاه پاسداران در ایران را آغاز کردند.
این حملات پس از حملات اخیر سپاه پاسداران علیه کشتی‌های تجاری در تنگه هرمز و علیه نیروهای نظامی آمریکایی مستقر در منطقه انجام شد.»</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6665" target="_blank">📅 20:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6664">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BNyncVw7SWu_Wx9bLW0Kk29BF-0CM6VoRD0goy6nc6C0yCPaJZiEJmn5pJz9m5_aMByurVo14pKqLzW3lkneHL0zj18nIDchXpGfPQH4X6t9ARc1FAcb5-SFZB1NPaEpxNbcwt0ru4eK_ecseEK2rKJnIs-IAFfuK6jE0ElZ4kzHvKAMHQ6HK0HO_6Fe96B05wL7VHF3YHH1vdO-TbseZ4Am5AQRWzDC6YgAgQTSNR4uFBYkprLerf-Dd9oeIWeCLNzWIkoToVyKON6r2eUKZPvjOE4AQAE7S0TGfO_8fxSmHBZ3uksGwlCoNfJnHIr3rjShC3qtTuTRaPuMRnR5Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه شورای عالی امنیت ملی!
دستاورد تازه : حوصله آمریکایی‌ها سر رفته،  یکی از معاونان و زیر دست‌های وزیر دفاع (هگست)استعفا داده.
حالا این سمت : از رهبر گرفته تا ۵۰-۶۰ تن از فرماندهان ارشد و وزیر دفاع و وزیر اطلاعت و … کلا کشته شدن!!
تنگه رو بستن قیمت نفت بره بالا به آمریکا فشار بیاد، الان کشورهای عربی نقت صادر میکنن خودشون هم‌ نفت نمی‌تونن صادر کنن، هم مجبور شدن بنزین رو گرون کنن و وعده خاموشی‌های بیشتر  و… میدن!</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6664" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6663">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">‏ پزشکیان:  اینجانب به صراحت می‌گویم چنانچه آمریکا به تعهدات خود در یادداشت تفاهم بازگردد، ایران نیز بلافاصله عمل متقابل خواهد کرد.
خودشون با حمله موشکی به کشتی‌ها از تفاهم نامه زدن بیرون، گفتن تنگه رو بگیریم و بهای نفت رو در دنیا ببریم بالا و فشار بیاریم به آمریکا و ترامپ و امتیازهای بیشتر بگیریم،
الان افتادن به التماس که برگردیم به همون وضع!</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6663" target="_blank">📅 09:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
ترامپ به فاکس نیوز : به حمله شب گذشته جمهوری اسلامی به پایگاه آمریکایی در اردن، به سختی پاسخ خواهیم داد.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SyXpY0MxLHOzZE1bIabaEH-po2XuCAdDL3ICbr9zAqXMbuKGpCvwalgAD6JhWim9fKjmTr65Kd_h5sJgWFlOFZ-zGJpB-0LaMVdi8R-4uYrqXyv-11H1rc7b8IPHYDQDwiPggcQMBUuAUYf0xQMWauAtiIcSmnyKXasgr5cj5qmlotOLQmmWYyDlJPrI7K3FEW5GLX0LQ9wZteQgvsCK1TngrV4YGsR2siIp1EWBujrShrxc250q3tFWavmk9ZHaJxDlPuPOvM_pg90SscCBHt7sg3Pm6O61eOeiV6MqrZyPY3MoDdvlEdIh_kARTpoONIaEP4UNB2Opt7MwtswaFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=UA9tDD7JZ8JbqUZ7r-xR5YuJEiYNfCSvWLikb-InFUoHw91ndT84QzIOqbXYNCytT_7wIa-BnsCf0ZuAK0YnlfIP9SIXEuWLza2Y_j33HjXCXrRbabW1PqRAVbFYkpdsNYafPGZ0KOLaGWW7THLA0AsBIUiwbNHKNtkDTDUQiDfWk_sb_Ud3TkuczuGvHLyYO3lgj8zpTLCIZFP4V0wBR68G3yVFfC83YVhcVtSTB9EC2VjvrzPCLNz9Y-Ko71cPG99aU8lBXGwPiduCgyi-xA9N7Y0gR3EcsSLMSGvNEZ3R4z3yWLb7tZp7KUmHpAB5MhN-01FRz2DMnH3y3PSiEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=UA9tDD7JZ8JbqUZ7r-xR5YuJEiYNfCSvWLikb-InFUoHw91ndT84QzIOqbXYNCytT_7wIa-BnsCf0ZuAK0YnlfIP9SIXEuWLza2Y_j33HjXCXrRbabW1PqRAVbFYkpdsNYafPGZ0KOLaGWW7THLA0AsBIUiwbNHKNtkDTDUQiDfWk_sb_Ud3TkuczuGvHLyYO3lgj8zpTLCIZFP4V0wBR68G3yVFfC83YVhcVtSTB9EC2VjvrzPCLNz9Y-Ko71cPG99aU8lBXGwPiduCgyi-xA9N7Y0gR3EcsSLMSGvNEZ3R4z3yWLb7tZp7KUmHpAB5MhN-01FRz2DMnH3y3PSiEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ظاهرا مشاور قالیباف،  «قیمت پوشک»
و «خون خامنه‌ای» رو توی یک جمله گذاشته
اینها هم ناراحت شدند.</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/farahmand_alipour/6658" target="_blank">📅 08:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=Ur-tlLImOv8Nt239xMlrPVhsjuXATpr7LhJmyr3all54_steuUF0ILorTUESc1jyAEltcmwNuQidVpGLUoavbhuZ_3wiu13Ru2mDBsvyShuynA_Lifa0V4C9t6ZY7qLOlaW3GT2MtIo1wy0W_IfGW69-cXAZ3CGUy5Fa6jR68O0orFWuWQosGldx0dZl0bD_Ko7lP6yKjYs6NXn5bXtrDfd7EwoP-1Jx-O0wO080GLuDnjnscUbRbJN-3hCO0qhe0xqNtjy7ef_VVUSCuQEVMN4uXuMPlzWLVRqJKq9A35lK7NrNC6zEmg6VN24G9wjs3Buyi2tS7LY39P24ZNnP3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=Ur-tlLImOv8Nt239xMlrPVhsjuXATpr7LhJmyr3all54_steuUF0ILorTUESc1jyAEltcmwNuQidVpGLUoavbhuZ_3wiu13Ru2mDBsvyShuynA_Lifa0V4C9t6ZY7qLOlaW3GT2MtIo1wy0W_IfGW69-cXAZ3CGUy5Fa6jR68O0orFWuWQosGldx0dZl0bD_Ko7lP6yKjYs6NXn5bXtrDfd7EwoP-1Jx-O0wO080GLuDnjnscUbRbJN-3hCO0qhe0xqNtjy7ef_VVUSCuQEVMN4uXuMPlzWLVRqJKq9A35lK7NrNC6zEmg6VN24G9wjs3Buyi2tS7LY39P24ZNnP3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iOv8s3PbfkUWp14CeeuMKT4y236-_JIYGupws5789EVq-C-9Lbp7UDlO1vVtFfXtuZcCGLBCnn9qhcQ4T12kmiA07WIrQCiSR1LMWWp89M223awOjcUsrsqAePJ59GZ1Lzz4xqt13SskOrSxFfmoWZ7wX32xWTHD4XtJ615OhxOiSaIE8TIVZBaGbDVpsHUHsvFcsnlpZR-RqU4R3K-2-NM7mfK6k6u6L2wGBweHS5nZttOnBHPO-pd55AtXHGx5pOsvw8k0zf-Lzq1Vqo02dd00Pwkh8I-EKOjnxEIVfzj3tMxUiK9FWh2JJar12cAjrAmLWqgnxHDXkyRNu_wRgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ رو به بهانه خونخواهی خامنه‌ای راه انداختن
۴ هزار لبنانی کشته شدن
از جمله بیش از ۷۰۰ کودک لبنانی را به کشتن دادن!
قالیباف رسما و علنا گفت
«برای جمهوری اسلامی» بود.
بعد دست به دامن دنیا شدن،
با التماس و با تهدید به جنگ با اسرائیل
و با قراردادن «پیش شرط  شماره یک»
برای تفاهم با آمریکا
در پایان دادن جنگ لبنان،
اینها رو از زیر چک و لگد اسرائیل کشیدن بیرون
حالا اومده میگه ما فلان کردیم!!!</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/farahmand_alipour/6656" target="_blank">📅 14:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6655">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pnCAJekwwlN9teD8rRM1Ywyg7wBNWUSkirYaTCWPbR6FAae4MFDKjrvgfIcCOD6el2Cyk-GMQXF5XsqsvCcAI2epmrQ7XqG9RVpAdqX5WEImHwqkP5OMK--KBQVKUxhfXUtx15OOEr56i9i37_kgup36ONUMTgM0-3ESe4KgBUWuDr26ZvlY5B1Byw8JecqI7c8JHjyZ4zbqhQwDcY9_tbdeaUwh7JfLvb8w3P365AD3CCrVCMZZADUbXR4MZZ535p2YbiwDPJmfXYq93xqDK9qm41iSL1R0p3g5GhLOM7JB0PCXI_w5h_gPSjParAGPZw_C7b16ZwnV1bhL2504mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات نفت کشورهای عربی
خلیج فارس در ظرف یک ماه، دو برابر شد.
جمهوری اسلامی تنگه رو بست و فروش
نفت خودش متوقف شد.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6655" target="_blank">📅 07:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6654">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">داریوش، در لس‌آنجلس روی سن زنجیر میزنه
محسن نامجو در ونکوور کانادا، سینه میزنه
دختر بی‌حجاب ایرانی در کانادا روی
ماشین قیمه عاشورا نذری میده.
ای آخوند فرورفته در مغز استخوان ایرانی!
روزانه چند جوون رو اعدام کنی، ایرانی‌ها بیدار میشن؟ چند تا جنگ و مصیبت و کشتار دیگه باید
سرشون آوار کنی، تا بیدار بشن؟</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/6654" target="_blank">📅 19:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6653">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_3N2A-rBHhvhOO9eNuuCvGUC97VOBF7FJTUd-MSf9jrB_UfwpEHKNnAZwbG_Y2obGoQC59t0_4BtzeIqS0uwuQflvyoDag-Cs5wJ8xnR1f_nyoYDyi1_kVJb6OO6NCW49t8P57odLMJN89KQO_CAjZZ2ZcLP6c4GRNOpgQxzopQ4CYQUDLhfMztz2v97gcPuRa2jQc5Ex8bP-C7sAw0WJovnzh0Ez4xsOzHXLUsa-bg3WE4roogUMT9HnW0fj3lgPBHSPe8vlIoUB7jKOgUYpRg68jkiw9u96rCKMm0lxZiiRPTqrXRLW8mKbUAyTOWxuCCBe3HKgbCMEZfxA8nMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از آتش گرفتن یک فروشگاه فیلم گرفته،
دادگاه گفته این اقدام «مشارکت در آتش‌سوزی»ست و حکم محاربه و اعدام داده!
همون حکومتی که با جنایت سینما رکس آبادان و ترور نخست وزیران و بمب‌گذاری‌ها شروع به کار کرد و قدرت گرفت!
بعد بگید چرا مردم در صبح ۹ اسفند
و شخم زدن بیت رهبری خوشحالی می‌کنید!
هزار بار دیگه هم شادی می‌کنیم
از مرگ و نابودی و تحقیر شماها!
هر جا که تحقیر بشید و نابود بشید؛
از غزه و لبنان و یمن و عراق تا تهران!</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6653" target="_blank">📅 18:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6652">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZjaHe4Aa4EeZy2NEn7FaK_RLWWCOahTCAIQKidnZHcBYjEnSbR6IMApwrI5yu1NU8lJaHs86eU1HMsx9Noqs7k5s4_lnUBlpDBRiYyxMiFEoTU9giqn-VZpfmyMRDFvHcNMxQRU6RZ3g-69E-93Tq4Ld9P1ft2ZYOrCat4KoZr69XZHRK5wzX5pwa8p_EEwOPLqdaK0rDIiV6iC2LAWcMXsMQqq88qeurh3iM-jWAKEqXo8Kv7dli3Ld6zON17HM_RbYHHw5-7M4TIEOqPcaZSKQlZRNlfRTYNRWodzWSrFqYoepQ8VRllYNs8s4gpBursD3eAXQga5c1unmKLZzrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dlwFbVQsFSrJXz1gW1dZU8bJsclp1TIzQwkY8CEjpgHhoroiG6F11o1Eg366SFH_G46HGefVigKM21xLsr8PaApYISKryPMbSOSfgLyCHUv4ppU4_1AMDWqzL5AIFNZE9SPFV1OmCGAgrGeDAhwapJtpzFDhHZZHhfooje7dm4TiQgAHXaxv_x3ip-1dWcJg4KJ44nK1mYV5411rGjpEQSS7MYKOnya0TpUdx5p3SsMKmg3Gw_0N3sWv-lM9yT5C1ZQOnfQ0yQUpZz3gkLzrPOc8zWkEbtEqxTh01zJypF30ZO9lXOCDKlV_kBggqlCdiStRt3pX80CH8yYwWuRiYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mqxne8r5HKPntlE0I6XrnnyuvdVYx-FmwYCgNawbXYGq-TybhxY0RoRu83tJ0gDWdCTP1dUQ_opqvQseAaExLcvLBSMV-TTxKDluQj6RqAck12mmfbQNdK8KRWCtkICrRtekHtsTXNgEx7WJuYp5L7dn-gkdAVyzLg_iZIO9qwKj_JzjfEgMgl5604TeDulI76r0HjNmr7vxLx2NLGQLVBMPgb2gEjIRZmSA0xp7fRlkJfZay6laJdaNRtItLtGknZaskJapky6QynZb20q7KqYVGiIlJMEQVR7kUFuJLh3rQVJ9dqT-MtxRlsNd9ppfQlV0Z0AdOss6HgxXjM-Q6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BfDVnuGkSKHOLU8b5Vza8e7ekNrf9ZskvOVPvlmtclwDD-quSRAt3l5iFsOBfCB_rlRR2iHgRojo0RoMQW_wTslN_TzoytwEpOBpmSrEbr2fptXE2LVKCL8eYmh0IMYyI_BNTf5vwSK9MFLklzd7OnLPC9a78sD51Q1ftxPIor2HMMqnPfrlc9zdnohB3wlrrD6Hc2CA-OHiJvR7wN_TCzNTFcW19hffMUVpSe2wJtmMoKsSw4aSjAxY1mzo71uaAWE2eoEkCCyKKcut3kE8tLCspnuzX-KUgm5KNGt4P7Ww25Qw4uz8Guqn98SFbS9IOWhL-mG4-mkP5VtMU1URCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a3LC8aqqHMHDM89McVsDIz09BTVowNRKgZ6NqYMR8QY01DF8I0-DFia-SjD12-Butax7qVKmD5Cec71akuwyu5RE_qVHb5hJNDEJYJzESmuopz7CRkjOiKQsxG4wVaWz9ForT6H2ZhdMHdUu04nEf9nvTnr3W-DZ832r91TkWcgd1jiT6SOGL6QKWFJKsxdkL-HSLDHSXG5eZM_p2cUA--TltklZWCDC0SwHC98trqP0EYDWSHZ9oULVMZtY0w8Cu4xV9sQrLFnHyhTP8xYcKVgsHQPlZV3Ib1ZSeXRhuOLcXtz1omMrjOUP4Ama8zB0R99G6P-4-whFZavAxZ5TyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی،
دیروز به عنوان رئیس هیئت مدیره
دیجی‌کالا منصوب شده!
نام او با واکسن کرونا گره خورده،
او سخنگوی گروهی بود که مخالف واردات واکسن بودند.
رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و برای ماه‌ها
مانع از واردات واکسن شدند.
تحت هدایت رهبرشون خامنه‌ای.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6648" target="_blank">📅 09:14 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6647">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=e8SvUooShyjZnLavtmw0GS4gvh_8Nm2rPtBugg8TQbC2n4AdDSmd-p0gWWekMKhQ1OLlFvjWm3CjDZzFQJHO5KK3Mw3M35tHdrW60XoIziWRAqbXPMb7BfD7arbGJusTe3oousnQ0M5sIh09GVz3ROlMr8Q5k2_P4_i2Iyj0M7Ah4Eo4entuYeAGSYy4hNIKEDGMhak6BuFODIIhBevsBy3Et3v4UZ5NqqXVbw6rukwLIvVIecxGtl8nT3qTr65__p4YRk8ZVz0m_IBCZl9mqit7r1BKCQooWeWIhdtiwCJ8-81quulSDX1ZVLv1C3D-XqnQkhISUtgJkEr2MB796A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=e8SvUooShyjZnLavtmw0GS4gvh_8Nm2rPtBugg8TQbC2n4AdDSmd-p0gWWekMKhQ1OLlFvjWm3CjDZzFQJHO5KK3Mw3M35tHdrW60XoIziWRAqbXPMb7BfD7arbGJusTe3oousnQ0M5sIh09GVz3ROlMr8Q5k2_P4_i2Iyj0M7Ah4Eo4entuYeAGSYy4hNIKEDGMhak6BuFODIIhBevsBy3Et3v4UZ5NqqXVbw6rukwLIvVIecxGtl8nT3qTr65__p4YRk8ZVz0m_IBCZl9mqit7r1BKCQooWeWIhdtiwCJ8-81quulSDX1ZVLv1C3D-XqnQkhISUtgJkEr2MB796A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GxFr7zLglcx1htf8irQMz__T5IqXeuGNAiKkIbV56xvdR2-87R5IiPT8sFEZ5_mHR3pN0xxHgHtErO_xWeLl0qLYskEx08lcCn2LMaFI82xFkld3JVyaJleEK53_k-UP9q-a3xKv_LR3hijN9JxQhkRK7TK7iORZY5rNobeBq83CEDlVlj02vcJ6t_qOrCVJ-vUrgCIL3ToX6Kr8SMdLd7_fZeBy9j-BQ3dUYsCzOxfETJ1k4Wrm3ev48wy5D-Ftej_PfByLLui8T3nQbWffMz-R728KJbe9qG9Y8ocsHOEpRAT3kOEd-wKt0GjbYtZ6NWMOEHJSerV5NCxQVKCqIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=j7rBMJINk30EthNztPsb9WEtGGP1whwagSiC98l3SHMI-AqTJTo0fHOrxaBdXuXDZvrdkmBsSc89keH39o6OcTS2hLxyBCpiT0psnDcBHiMUKGe0YLVuFR_SRJ7HqHgY5chdtX2Pan_uspaRwaj6fGrirmCnCMGl2zm4Mnj4shqGwsXHDmypx4_xkdRSIyCteC3OGlZQrLixMKjZMo7NkpbC9HFYBoeXLCLAFxQeREHmrSMLG4JwKfbZK2guJZj3mCp8JHgJHGCNx7wUnw79aQJReFOpLkqJ7eg8VIYcitOFvQXFLARh7PzFkZXYk3SJGAf393Ml4uLDfBB3AHLfeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=j7rBMJINk30EthNztPsb9WEtGGP1whwagSiC98l3SHMI-AqTJTo0fHOrxaBdXuXDZvrdkmBsSc89keH39o6OcTS2hLxyBCpiT0psnDcBHiMUKGe0YLVuFR_SRJ7HqHgY5chdtX2Pan_uspaRwaj6fGrirmCnCMGl2zm4Mnj4shqGwsXHDmypx4_xkdRSIyCteC3OGlZQrLixMKjZMo7NkpbC9HFYBoeXLCLAFxQeREHmrSMLG4JwKfbZK2guJZj3mCp8JHgJHGCNx7wUnw79aQJReFOpLkqJ7eg8VIYcitOFvQXFLARh7PzFkZXYk3SJGAf393Ml4uLDfBB3AHLfeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=apxzXNVaQ5la0MekUGEA0XPFEavPzJa4Ot6S6MaN77FY0CKyJH8WHvqLyxL5KVL_3caH1m33SkhM4OTXssYICIbA61wgv2m5xmT6TnxFZPptmGJ8tw1sIvSZevTDHvC8m9q0TYo2PcXm9x9zjo-QWd10JOwuiUjgWu4Iwyx_caV0NLmjvnq3Swl-fyT47f5ANdSpnpB_UPrL5hDCIWOMjSRhYos7p18rNg7GZOiKFfdZ7ZT4LnARkgfBf_tjxCR-KfuZHq3MSjspLUPpa1_15TTcIuHdon5lkaVOyXQu6I6hn1mxafEsDn2LnbsbkIljik7MUIH_d7KKEUvut_uv4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=apxzXNVaQ5la0MekUGEA0XPFEavPzJa4Ot6S6MaN77FY0CKyJH8WHvqLyxL5KVL_3caH1m33SkhM4OTXssYICIbA61wgv2m5xmT6TnxFZPptmGJ8tw1sIvSZevTDHvC8m9q0TYo2PcXm9x9zjo-QWd10JOwuiUjgWu4Iwyx_caV0NLmjvnq3Swl-fyT47f5ANdSpnpB_UPrL5hDCIWOMjSRhYos7p18rNg7GZOiKFfdZ7ZT4LnARkgfBf_tjxCR-KfuZHq3MSjspLUPpa1_15TTcIuHdon5lkaVOyXQu6I6hn1mxafEsDn2LnbsbkIljik7MUIH_d7KKEUvut_uv4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pUEGtne9Vem9Vk_ggS_pefbxqFXTPmaRoSTj4MECUpZGr3AZD8gWdQBbK9q_OQCyV6UGA8UCTlMxKUaznL1XsgTtB1MxGD7NFPqSd1pgiAc7_hSFkhqnx7XtP4OWayL8T0V78pFsJH73pp_-wXr1XDgP1NaAMqm_JOW64RUKpNb-HMFGCcvIN93RT_Sk12OK0euziXXKmhsJx8-19NDmKtq_DaI7d0nRTi6KuZ0gWpDTvvBWAF6QrMVZB9qS9aC7NK5TANr3GhbBCfwG_2dtfHWCiwGfesVL84nu_UNoi9kFv-L7sCrF2hWzrlk3xr2oFfO6CgrIj_0HAHhOVC53LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارائه دومین هواپیمای غول پیکر سوخت‌رسان‌ به ارتش اسرائیل.
دولت بایدن با تحویل سوخت رسان به اسرائیلمخالفت کرده بود و مانع ارائه سوخت رسان به اسرائیل شده بود.
دولت ترامپ اما مجوز ارائه هر ۶ فروند
را امضا کرد و سوخت رسان‌ها یک به یک راهی اسرائیل می شوند.
نیروی هوایی اسرائیل، قدرتمندترین نیروی هوایی منطقه است [برای یک دوره کوتاه، در زمان محمد رضا شاه پهلوی، نیروی هوایی ایران قدرتمندترین شده بود که امام با آفتابه از راه رسید]
اما تحویل این سوخت‌رسان‌ها تحولی بسیار مهم در شصت سال اخیر نیروی هوایی اسراییل است و دست اسرائیل را تا فرای دورترین و شرقی‌ترین مرزهای ایران باز می‌کند.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6643" target="_blank">📅 11:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6642">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">رئیس سازمان اطلاعات آمریکا (سیا) برای یک سفر عازم مسکو شد.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6642" target="_blank">📅 19:32 · 03 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
