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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-27 22:49:51</div>
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lPw2iJuW7gmTf02_jjn0QvQLP-XX9lG40BVZVlX111CeZIJI8lULEZCsKTJUeGoEnXuhmNZw2CGrRD07f2AkRg5Cu_PK26cDPOzseDisGAtW7-DxLGV_rH7ukSpEp0UfqQLShgWCGo8nFL9vP3XBJV9PTcHNKKUkVNYYFU8fWrvVat1gbTxaBlLnDHZ7kjz5_p0N4_kOeTzYCpAV_gn77aBQ02oetT_-xN4N6bg-IDdWmv5n1XTLpe4xsNSm_Q-Wxv_MwfCwJ3NIRRmRY6KP7j2MqA8ijnXwFz4gBJl7kW7Scr8MllwvJdJDv3p6skuOYiuPygq3_mi4VKU8_DSeXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6745" target="_blank">📅 13:24 · 25 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eAMJfb2Kb9XJGVLFOfwcZoPy9B6HW5Om2Khz2IiVk_iXaxst_nd2ATsYZc1RNNTx9P2NExDZ6ht_0HO80ctvmoMl8gHbEo19bxSvOJfUW0cvB9Z2zEUd9GtwwEnnAoKR5X02koEgI8D5bWdvl-flCEZH10B_LRE9MuBKN7Le7Fa2cobxMWr5NVLdOVy4Maf58xpA7zRRHLN0YlG6HMZfSpnovugQvRSAoS8KREUch98d-OHQbFwU7GsETWvSGCU_CDqTfSXtB92v1TvRV-jsH2VJt8aHhuyhnoy8bwnMCEV94Qfh-Ia94kfapUd6npZn_v-Q1hd-wpMCxCAwioUIlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LrlZByQJ1ygqI5Ir_5cyoWJ7ZnBE8hh4WSOrg_Njy5nGgI64p_VVz2qa1wK52B5KM4JY8BTyuxx30WQmkB2O8j5BblqmEKhQ_2ZtDVwcVyj87IDC5smdvUtXdUvv0u7ZivCHFEM7crgzDu8VBFo0rvrnBmeYi1zn13_xD5y1-oKFjdlg7cZ71j3nBY1JB45kf4cEXhM_TKgmIdBu2rKEq3O4Yoqff3PM_w6Mxub878As7BsFbDGExmUuYZ0MON1nSOW6bcnWJ88_ec9AiymoqS9l6vWBqIWAf3s6wFBnHKUee1JdSh9gt6HdrOZa4xZQGWq_h-miEvEg47tfwg-b3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRKDtUeMfKoWdWlkHgd7bdQqsw6GjiZfDA1gHrR18ESoyCKLgfUdZ74nMzXbfkoa8haNbju9lalHDMHof1GSxGDStJpcVxIqyHFlt8LQJHBXiHebnNxQVEGlK8R4a8SSd7R1ZFHlV01SIiC1hQ-irpFCPBkbfVk62kns0z8QPoZfG6Y4j88BpfCvuBxVlaxPP-B6mOLkJs_uU3c-Q-7aZw43nrAmtAn6gt4WulMaDdt6eYm9V73kJDbqGRyREbXdNeFvx1lZwa-faqiZudFvt9ruBnmtSwcNzvQ_iXF9njeMgj7L84fnXszxjK7uhcSAlgJ1qkeNxQ44SyRPFKpTtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdCZkXWmAK-z-SCDarSmag5q-GnQW0tlVyecvNhue25Q0HCfaDbvpJD32j8xnP1m2Vv_PBgt0kqfcRbStoPwSOLMhmXAiSIRHGIhVTAaB10IYl7YmAIWjywrAweASsEYfwJjMb7jarYyS95GCSXafLfiHY9bNAmNH18aHUqlg1xmDGOWWHmvdwfxDv1ZkmS9VgC94F5n3vPme0BXiMnJjntyc7eKmM5hPqyHOGkUrAT3G_0WQH2c4K8vq7rAF6TUuROi03iL413UgXO9PxXQTku4HVogGQNIyTeh9BaJHY3X3-Bqw8roN0Z7rFKO3VtkelViTJPfUET0v9rsg8zxXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=i-naGJWBc-fmO2-4GXfyqu8TZbnVsyGXnwZmtYeDd3zgR03pARoyPr1g2-4IgItkizZARbwv5TFDrQTdZoKPJHPS1taHY175WbFPyeaS3TmFcQpGOjKCd3RG2UOwc3FRLoYr4aYDK2C9llu_ArQ91Hm-sUo9Aub3VENjBpo8Y32G5CAd_3n-uNIZ05fYdZXYkfld0hpPJzEtI-XyYJbWiXwMN7rO_d0z9GrDXA1dpcL3JP84vbICHBkIBD8P2wK2vo0IYAlJwcx_B8AqpD5C1Bf1cFTJy9Zh9iuMStOWv0OVCn0CiKC2uG08voN8t6bYWwNlQWsWGvH4WY-35YHvnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=i-naGJWBc-fmO2-4GXfyqu8TZbnVsyGXnwZmtYeDd3zgR03pARoyPr1g2-4IgItkizZARbwv5TFDrQTdZoKPJHPS1taHY175WbFPyeaS3TmFcQpGOjKCd3RG2UOwc3FRLoYr4aYDK2C9llu_ArQ91Hm-sUo9Aub3VENjBpo8Y32G5CAd_3n-uNIZ05fYdZXYkfld0hpPJzEtI-XyYJbWiXwMN7rO_d0z9GrDXA1dpcL3JP84vbICHBkIBD8P2wK2vo0IYAlJwcx_B8AqpD5C1Bf1cFTJy9Zh9iuMStOWv0OVCn0CiKC2uG08voN8t6bYWwNlQWsWGvH4WY-35YHvnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/olm5am24RRfGfPsdyO1rE8rQ_118hU05zihiYJRbQiScj8SUIbev1wqpWMF2Xrsu2zdN21cfJ-wVtYnqgDneewcd16qJ9FTHp5hjFGncRx8FyvYOz71XSrT11uxjE8o8EpS3cb3iZ9cSUhugi8WgdZH2gbNg40OCa4kFeE7tX5kQRFpplQOQAf5NMDO8T1PpfsHEBZWPi_DAM-50-vSRoSWCnc23kcSi96R9M1E2R7YwnHDmpPrRw5a7f8QAhSzPjdZf7BsCaAVSxYFVxFLCDR3c6-hSEi54KEvLfeQReO9jrImKxFPuP8bVOT0alPyt3H_wv_MKLwhvUdMn46pMuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VdKr-RXzxRsNaALVmuMwyQDWLnx-ouEBCzKFVpHLEfREF-KdT5Hm70XIdqVIyLdmkjthkpkhCJuJ4yxZHNv9v7FS762K4xXVEYxvAnfXCLQhn0cSm9qlMCvWpJjOsLql4XJhqkxbaOy8JlR1nLd17Z5-ZgIRb3PR44bjfmaGd3HDQAm8AQ_pgAvYDJFawE3P4zyEy6XKUUkNgTaX7LtEQrzL7igWg3bOTOxe-22e1hE5onM66Xwq7WPbLwvx2wy2cX87GtvoTDZXd7DTQucKK_a3uGJwpCRwjwWX9ulYV7_AN2HAakvzj0cE0Gz6GmeSigKND35T07oO0dclFpFM3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=TqQrfocv_oP1BqyLGHpxvcDseB3T7EBg4lXcXozDTokyXM9nIBTKLDodbI9W_EMHQg4nIN9kIeJkfdbVXSZMsdFri8yIKw6euF40x1KHrsyUPcaVtjo6I9hVyy6e3KgnTJKKB3uupkA4kAfRBbjoXCK_j5i-lx2G67CGFktMH8Q6QfGRdfGwTtA1wEnotXVvDOZUqpR5SJQklTzXEu4fcxirYjdLLFnewIwNiA0ngse6mHsgaox2lmgnBIeqdgdVVv3vx42nt-T7fngIvRbBnz4zGFiua9fmeOhNFtH1J6s1VCLg7nX323o9HsvY-C854CuUDorNxMreDK1m1xugbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=TqQrfocv_oP1BqyLGHpxvcDseB3T7EBg4lXcXozDTokyXM9nIBTKLDodbI9W_EMHQg4nIN9kIeJkfdbVXSZMsdFri8yIKw6euF40x1KHrsyUPcaVtjo6I9hVyy6e3KgnTJKKB3uupkA4kAfRBbjoXCK_j5i-lx2G67CGFktMH8Q6QfGRdfGwTtA1wEnotXVvDOZUqpR5SJQklTzXEu4fcxirYjdLLFnewIwNiA0ngse6mHsgaox2lmgnBIeqdgdVVv3vx42nt-T7fngIvRbBnz4zGFiua9fmeOhNFtH1J6s1VCLg7nX323o9HsvY-C854CuUDorNxMreDK1m1xugbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شدت انفجارها رو ببینید
بخشی اش موشک‌ها و سلاح‌هایی است
که درون تونل‌های این تپه بودند.
این دژی که تصور می‌کردند شکست ناپذیره از درون نابود شد.
پول‌ها و سرمایه‌های ملت ایرانه
که دود میشن و به هوا میرن</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6726" target="_blank">📅 09:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6725">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=JqdXZWqlSXQbEpf05GHAlLQw3hhTlpGITzOWgyj-4u06ec7YHHjr51j8P2gy6M-ibICMKFOPL8Y7uu3MO48WDRaNjx484uLqnNvNcm0fvMnlEHUEOqmstpap5VfogrPxVTw_GzlrRmJGVEYf8DgI3HaP8F3uv46Uw6Ztsn4pBzMWpTcLHjwRZKfv7APYrj333HoIKKFLdyZrJwSEye5SBPkQQbeYSpvvo3W5bBcIPBLCZnMF8sKZ_I_3pSo06CfqnLMmWeQmi7AgxatqBATfAGjerOS4asjfnuvF8inRYpljdLhl-G480Q5_vQN_0ccUK6F496LnPQTBBFIwDn1Oig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=JqdXZWqlSXQbEpf05GHAlLQw3hhTlpGITzOWgyj-4u06ec7YHHjr51j8P2gy6M-ibICMKFOPL8Y7uu3MO48WDRaNjx484uLqnNvNcm0fvMnlEHUEOqmstpap5VfogrPxVTw_GzlrRmJGVEYf8DgI3HaP8F3uv46Uw6Ztsn4pBzMWpTcLHjwRZKfv7APYrj333HoIKKFLdyZrJwSEye5SBPkQQbeYSpvvo3W5bBcIPBLCZnMF8sKZ_I_3pSo06CfqnLMmWeQmi7AgxatqBATfAGjerOS4asjfnuvF8inRYpljdLhl-G480Q5_vQN_0ccUK6F496LnPQTBBFIwDn1Oig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=Cs7GbLsi__ZZdiPhE2icoQG9dE2YOnmVxyDW0h3MtiXswliHwTXzUjgRu1bM09F9DGx41lYCELSQIxshS5q0DWMYS_dpI7zyvhjfkyIIWbqHtVGzhJu6q9u7EqCDcy32vMLbtQo9sU0LYoeKBiwRKgG5C5eEEyR0vS4kGDgcO2yiEn1SoLKihqnvd8Jhw2L75F2D1kJxmZAIOPycfm3yJupXZdbXgvxOp0qehGr4LxgR0mAPR0YEBd-n1uGvmQs1nHO2glUgLvNgDRhh5-6Q5-g1wQWue7gXq9NNI0OdM_Cp0DbUq9K8hzirWgs5McYiMkgfmhf1oEpTHix-8xTSJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=Cs7GbLsi__ZZdiPhE2icoQG9dE2YOnmVxyDW0h3MtiXswliHwTXzUjgRu1bM09F9DGx41lYCELSQIxshS5q0DWMYS_dpI7zyvhjfkyIIWbqHtVGzhJu6q9u7EqCDcy32vMLbtQo9sU0LYoeKBiwRKgG5C5eEEyR0vS4kGDgcO2yiEn1SoLKihqnvd8Jhw2L75F2D1kJxmZAIOPycfm3yJupXZdbXgvxOp0qehGr4LxgR0mAPR0YEBd-n1uGvmQs1nHO2glUgLvNgDRhh5-6Q5-g1wQWue7gXq9NNI0OdM_Cp0DbUq9K8hzirWgs5McYiMkgfmhf1oEpTHix-8xTSJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=WODWbVJoCotNMIViK2X2Dhh2UxNzfAfmSit1pAgCfsV6LniPjJ80CK32VGOBDJMWJZFd4LkRkQGdiQYqGexziN7K75AbgccMqoPNWR1L3LMW29RqUxVWojDP3ADmRlUqfWELrWWBZJzjLz7on5mtI7WuYkxhhIhAMYiaVp0waZ5Qlo8-B9z1h711fiCYom62AkjE6u6f6Z69bpzTHG9df9gXRKkAPSSSSOj8J6LQjQ36hWXK9hV7dVDVpYVXAZ9TVOsKrFBp1lpIsc9L3G5t4hEwleK9SExV3EKhUtuJtCqupqhBo6wyIrrWmMTeE5v06gnWS5Ccqa8ur0VQMhFxDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=WODWbVJoCotNMIViK2X2Dhh2UxNzfAfmSit1pAgCfsV6LniPjJ80CK32VGOBDJMWJZFd4LkRkQGdiQYqGexziN7K75AbgccMqoPNWR1L3LMW29RqUxVWojDP3ADmRlUqfWELrWWBZJzjLz7on5mtI7WuYkxhhIhAMYiaVp0waZ5Qlo8-B9z1h711fiCYom62AkjE6u6f6Z69bpzTHG9df9gXRKkAPSSSSOj8J6LQjQ36hWXK9hV7dVDVpYVXAZ9TVOsKrFBp1lpIsc9L3G5t4hEwleK9SExV3EKhUtuJtCqupqhBo6wyIrrWmMTeE5v06gnWS5Ccqa8ur0VQMhFxDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=U6BWFkOUZHo5MKDDi3VI6XjuHeQGYXx-XZr6IJbqPu2PGGgE9JprT18TOFOsq0YOa9gY7EwVjfZfXjyfDKwG-gPMAHJP8u9e74xXSRHfRz8xoMnJ-NqoLSN1fj4R6cbq9d39O3ZLrrwrq1wRTEMFtNH7e8w-8GiH-jYwlpfsBGYHHXyn-vl4gIm4-gETLr3PkeNj1O4kQQwByqgoY32B-DtAvSAVrizkgLnIvP5X2ZvVl1N5ASY1GIhZ61Dpm8u3VxHQNSxz91lPTE4WtVLnX-pSlPr94q3Jrz3tov8MNqJNVD9h0ZwAtRX06FCaA5BmEaZi7ogCSdETB0t0wjrGzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=U6BWFkOUZHo5MKDDi3VI6XjuHeQGYXx-XZr6IJbqPu2PGGgE9JprT18TOFOsq0YOa9gY7EwVjfZfXjyfDKwG-gPMAHJP8u9e74xXSRHfRz8xoMnJ-NqoLSN1fj4R6cbq9d39O3ZLrrwrq1wRTEMFtNH7e8w-8GiH-jYwlpfsBGYHHXyn-vl4gIm4-gETLr3PkeNj1O4kQQwByqgoY32B-DtAvSAVrizkgLnIvP5X2ZvVl1N5ASY1GIhZ61Dpm8u3VxHQNSxz91lPTE4WtVLnX-pSlPr94q3Jrz3tov8MNqJNVD9h0ZwAtRX06FCaA5BmEaZi7ogCSdETB0t0wjrGzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما میگه :
مردم ایران در خانه‌هایشان
«۵۰۰ میلیون تن طلا دارند»
یعنی «هر ایرانی» حدود
۵ هزار و ۸۰۰ کیلو طلا داره :)
روایات اسلامی و معجزاتشون رو هم
همین مدلی ساختن!
اون مجری شوت هم میگه : الحمدالله!</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=M8vzETSuAsnQKHixvaubygUSTALAzgZiHQz-rLR8WmfIn_9dIa9zMsJXKcZrvJi5x_TSpYjNKdk0_RpDaCN2xPk5YWsX0UDqiiub8zLikSyBSOAomJ_sdR-yNJvoyVQajVgfC7osnhxFcN1ZzLY6updAOwKb-b6673lbExk1XUoBAQaNdr37vSKyqXpcFkKL5UqQ547aPgva6hiTRa4mazp34ijVcKqdqf-38QaKk1o8uHbuVHhGmK6rt4rwX0kWBrEq5FKyCTfuB1QhF8KMxftCgIuEmJfWaTiauynNK5FSWajyJqrguDv3JwZL6fpdfsL3uA5yk3aMx4pj-8swlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=M8vzETSuAsnQKHixvaubygUSTALAzgZiHQz-rLR8WmfIn_9dIa9zMsJXKcZrvJi5x_TSpYjNKdk0_RpDaCN2xPk5YWsX0UDqiiub8zLikSyBSOAomJ_sdR-yNJvoyVQajVgfC7osnhxFcN1ZzLY6updAOwKb-b6673lbExk1XUoBAQaNdr37vSKyqXpcFkKL5UqQ547aPgva6hiTRa4mazp34ijVcKqdqf-38QaKk1o8uHbuVHhGmK6rt4rwX0kWBrEq5FKyCTfuB1QhF8KMxftCgIuEmJfWaTiauynNK5FSWajyJqrguDv3JwZL6fpdfsL3uA5yk3aMx4pj-8swlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=N1v5OClbqRKZBKucwgrmIKHOhks0UVt0A_yxPws8b1nuPDFfWlZbNCIEQkETBbEWBdP3bjRiH-PJl3MUPsiSE9lJBMVdoPPhBZUS7wpz2JSd-ArHpBjKSK7kZ8jRkwT_xNhfzRO6C-Rakx1hHf5v04rhV2K2Ak7SIc7Nxi54nbPCXwSII3xBVIpoT_AuLO72UdXXzQZZbmXbf7_3bSZ3Mgj5RIZZFpUzQfDuYGjPuxW9BIit7DSXsOJrjDJ-vzAlmByB3w2meFNO3MCDQkIwzzlpCu5gYT8o2sNOC-BrjgGAcUAZlRkDkOkc41-OuUrXp0StD75MfBGZZPGmnGEFnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=N1v5OClbqRKZBKucwgrmIKHOhks0UVt0A_yxPws8b1nuPDFfWlZbNCIEQkETBbEWBdP3bjRiH-PJl3MUPsiSE9lJBMVdoPPhBZUS7wpz2JSd-ArHpBjKSK7kZ8jRkwT_xNhfzRO6C-Rakx1hHf5v04rhV2K2Ak7SIc7Nxi54nbPCXwSII3xBVIpoT_AuLO72UdXXzQZZbmXbf7_3bSZ3Mgj5RIZZFpUzQfDuYGjPuxW9BIit7DSXsOJrjDJ-vzAlmByB3w2meFNO3MCDQkIwzzlpCu5gYT8o2sNOC-BrjgGAcUAZlRkDkOkc41-OuUrXp0StD75MfBGZZPGmnGEFnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت دیشب این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین،
دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، دلاری گوشت میگیریم،مهریه کم میگیریم!
موجودیتتون ذلته!
دیگه ذلت چیه!</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOd7h1hp_yyUsOPZXwbFWh_Gih9Hy7_3UOmbAOFIgRW3DKxfh32QPF2nRlz6iw0dBUJOem1ha_ll7w_ckjKzMAosHWEhy9C6tSliMCvXBNKWxQiFu2GIJIHiZ7g3i253UAdjlJNY_Y1vSF5g4p7FsZwLznKSQPO-h05FZ_A3sLhOm4ZaC33ub8k7XvMncHq_Qz6pazgLeLSN1hx-HRRmAl1XdHjnfaj9wL3djgQ497lxdDs0gF_jOBKqGdvi4B5eKLW4xqZmK7JI75YojDjaY28Gp69ldXiRJ2D8CzXBntXR-LYWQ-NdoGVhgxaMHoUdeVvyU3EHdsTenC-mqAjTbA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=WIgwkxj31P1HO1eIRpC1IyqJHe0OY9w6KLyIaMA8h38BKMP9oXocWHGr506vpfwz7vQnmYFWx06M2aCn8W9c2be2OI7qIxzS9uhLILqEGa00UotzYSItOCvqONmfM-NNK3iE7l6M8BwOlS3b4Cjs6FSoa-0MLk2ec48bjTxoDjLR6Kf2eWc-kOsGV8UzEtJkiHArTzbPfZrxWlzW9XEpVajHc_O7dRl46ouabe_D1WIy7PazI22ELLcACOCcMG8R1nHBgtpyTG9896f384zt_VhLH-a947hYfFrBIfmDiv1K3Gm33SLlejJvIjjyaBXuIRGYg5bC5HefXty6Pj-YGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=WIgwkxj31P1HO1eIRpC1IyqJHe0OY9w6KLyIaMA8h38BKMP9oXocWHGr506vpfwz7vQnmYFWx06M2aCn8W9c2be2OI7qIxzS9uhLILqEGa00UotzYSItOCvqONmfM-NNK3iE7l6M8BwOlS3b4Cjs6FSoa-0MLk2ec48bjTxoDjLR6Kf2eWc-kOsGV8UzEtJkiHArTzbPfZrxWlzW9XEpVajHc_O7dRl46ouabe_D1WIy7PazI22ELLcACOCcMG8R1nHBgtpyTG9896f384zt_VhLH-a947hYfFrBIfmDiv1K3Gm33SLlejJvIjjyaBXuIRGYg5bC5HefXty6Pj-YGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=GeDEvnDSwNUZmTEW5btuNRrJ7XOuVrDPmVV19UsV2q6Jxa5ftcXITrpuMzGe4k5zXvXCDiRBBokPKWvNmmsK6OW3pBhN4JeP8-thGThOlWHPRDGMYQnnlzqojn9nRlle_AMYpIXpOCDp66ACvFt00EtVk3MwCd5XBlw8fHWym3IO7LTxeqH4I9nWlQbDN9wtlKARYaJffk3URc3bF6gzWZCoRZzx3qXNDuXx0vW-M4m2n9gddHNAoV2rxUNey85_LBP8Se5nEqeamilhLKQyAIBcpTb043-v5mv9gMT4ISFZ5r-QJxoVI4MClkVIJy1vM_BiM949rOzTrS07eUZkhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=GeDEvnDSwNUZmTEW5btuNRrJ7XOuVrDPmVV19UsV2q6Jxa5ftcXITrpuMzGe4k5zXvXCDiRBBokPKWvNmmsK6OW3pBhN4JeP8-thGThOlWHPRDGMYQnnlzqojn9nRlle_AMYpIXpOCDp66ACvFt00EtVk3MwCd5XBlw8fHWym3IO7LTxeqH4I9nWlQbDN9wtlKARYaJffk3URc3bF6gzWZCoRZzx3qXNDuXx0vW-M4m2n9gddHNAoV2rxUNey85_LBP8Se5nEqeamilhLKQyAIBcpTb043-v5mv9gMT4ISFZ5r-QJxoVI4MClkVIJy1vM_BiM949rOzTrS07eUZkhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=O32hEZpRpy_vjsQ0C2Agz-W4fvEaU87ayo977t-PIxhDEzPvEXu0FazCSh10JAuVJSGXGw-7O3gQY94o7LSuxUit2TIzCmammH-ovhaXjP61G0Vn72ciY2dG9hRKM8ic-6CN3338KdQ0Qa7AoKOOShoElLD4xgnmM2O0hNqp0gRYyP6HeMCqt-_rZ-mvSAdevlw971bCYLpVak-y6gfmfitB7lx2BbXJ02O084I5u5Z_oK79TcfRslpbZt8S66raebUFGMxjbDEnj8GawpcqPD-O_ln3TPwTnEHma4E6nOCmH4hSn5ZeoQsF6KZvEjr_ITz-wKOIvMuqVTGR8li1pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=O32hEZpRpy_vjsQ0C2Agz-W4fvEaU87ayo977t-PIxhDEzPvEXu0FazCSh10JAuVJSGXGw-7O3gQY94o7LSuxUit2TIzCmammH-ovhaXjP61G0Vn72ciY2dG9hRKM8ic-6CN3338KdQ0Qa7AoKOOShoElLD4xgnmM2O0hNqp0gRYyP6HeMCqt-_rZ-mvSAdevlw971bCYLpVak-y6gfmfitB7lx2BbXJ02O084I5u5Z_oK79TcfRslpbZt8S66raebUFGMxjbDEnj8GawpcqPD-O_ln3TPwTnEHma4E6nOCmH4hSn5ZeoQsF6KZvEjr_ITz-wKOIvMuqVTGR8li1pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون هم که با افتخار این  تصاویر رو منتشر میکردن!  بگذریم کل سپاه و ارتش و بسیج و مردم و عشایرشون نتونستن وسط خاک ایران،  این خلبان رو پیدا کنن!  فقط هی نوشابه پشت نوشابه باز میکردن و تعریف و تمجید از خودشون! زارت!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=lLsNdTSGLW74QH4j69WawdqRK4orSYoxGFlJTQtIk5rt9m0cBeqEBIhPxt_FjFaRJLQ0L_pFxUYVLqPEJXDJix0LYLDeaiE3e6aUFEYPanoQcVHWm5ClLHHS19BYdxvhBZLLm4RsHlljX0oHnHWbCOLCyVeg3ac5mDIezhEmxCSuaGNJ52R0nsdKZa71V8XB7zuCozYN8RmnMAuehYKflgJrjiNEDxLr1UuRYFbu2Wp9yzG5xHtnA1f6PB4Vrpj1buBPaDs7ijzFWjF3ZZ_biotUcjMdaXxyXZgbSG7qRqGn-oW7CPEnUBpF7cLhlHzE2PA6kinVQUvnhtXM-kLvCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=lLsNdTSGLW74QH4j69WawdqRK4orSYoxGFlJTQtIk5rt9m0cBeqEBIhPxt_FjFaRJLQ0L_pFxUYVLqPEJXDJix0LYLDeaiE3e6aUFEYPanoQcVHWm5ClLHHS19BYdxvhBZLLm4RsHlljX0oHnHWbCOLCyVeg3ac5mDIezhEmxCSuaGNJ52R0nsdKZa71V8XB7zuCozYN8RmnMAuehYKflgJrjiNEDxLr1UuRYFbu2Wp9yzG5xHtnA1f6PB4Vrpj1buBPaDs7ijzFWjF3ZZ_biotUcjMdaXxyXZgbSG7qRqGn-oW7CPEnUBpF7cLhlHzE2PA6kinVQUvnhtXM-kLvCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SLMpvD3UJIIazQi063jR_nql5qUSHN5WhnBtBsWzRpn0UaBH7_ZUxeXB5jFwD_XRXQP1oJoBDhq9y98JuAUIgdsgoA2eNZhmRYbTr8RlYjEOSG0mnpDMU-NANYxzN4qzDGcHEjTjVJttVyrVX6FmLVp_q3KfZp4mHUnwcOz8eBpJWAHCLN8jDJUmJPq5YeU9UAhEi8CJYAv8cAz6Sx48BG_A4b-MjzeNy8eVHmzIet-woyy88pUY6IbrnYPq7QWWz8xx2w0Tm7oGUn_8M7v6b548T6o__m1tpoZiTLpX9JvBvJloFr1wx892D-N7D0zslMNl7np1hudhriceyCGNWQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=B9ZdESG7I7M8Qb9VsbWieQtr8YrA9qz_LTpbTSqkptpZQyAFvxKsFt4yuqmeKJW26I_3VNRa2njdKNJQusajVsut_O7c474jqK9db8foA1B3x7cF5bwYY9_FMjWPJHm8kofgUF4eZimzXFZEOIyQDkATpMkZIf4BL_QlupGhuau7_-bGRpAbROzHog-mtZYpWCQg8mphnG5Ayd1LEK5-GU3Slfg2ZY9MH4Ne9_ao5uUIjp62P2FGg8YoXYEjjqdFKwvCzJGXp0DMgMBEIcFWLmWbmAUKh8LzGvK1t6zLXab4bw8RPwc5d4VXEsKVc_jp4yLn1LIMGKkl-XQPI2Xc4DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=B9ZdESG7I7M8Qb9VsbWieQtr8YrA9qz_LTpbTSqkptpZQyAFvxKsFt4yuqmeKJW26I_3VNRa2njdKNJQusajVsut_O7c474jqK9db8foA1B3x7cF5bwYY9_FMjWPJHm8kofgUF4eZimzXFZEOIyQDkATpMkZIf4BL_QlupGhuau7_-bGRpAbROzHog-mtZYpWCQg8mphnG5Ayd1LEK5-GU3Slfg2ZY9MH4Ne9_ao5uUIjp62P2FGg8YoXYEjjqdFKwvCzJGXp0DMgMBEIcFWLmWbmAUKh8LzGvK1t6zLXab4bw8RPwc5d4VXEsKVc_jp4yLn1LIMGKkl-XQPI2Xc4DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=cAQ50T1YBTPeyJJ3J55QVFaFEbAgpZ_fywre6OD40tmYYF6keLaFEkX1Kx8kwBQ3HM6L0DG1YHpWT4zwOJfTZX-rs7OjHvFFjcWW1CmbRQTYJfoPLa9VptbHET4saZGK0VMZxJ9sFSVRfJviMOb49ZYhZfK95yarggSHzJTlhQ6h-qTwsPWOb1PVPkWfnsiCWcpok6zb7vA3FwYaHvaDupxIJCu-45xkrigDwyqlp3v0H2SwcP7HWW9AQdOlVZquoksrkkjapPkOL8Qcv6r_sLfcFc27ObiyDM4ERgBiNMQE1PvXGqVsuxkBJk2RVX6juzMkB0RW9fIhK3vQDcJjNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=cAQ50T1YBTPeyJJ3J55QVFaFEbAgpZ_fywre6OD40tmYYF6keLaFEkX1Kx8kwBQ3HM6L0DG1YHpWT4zwOJfTZX-rs7OjHvFFjcWW1CmbRQTYJfoPLa9VptbHET4saZGK0VMZxJ9sFSVRfJviMOb49ZYhZfK95yarggSHzJTlhQ6h-qTwsPWOb1PVPkWfnsiCWcpok6zb7vA3FwYaHvaDupxIJCu-45xkrigDwyqlp3v0H2SwcP7HWW9AQdOlVZquoksrkkjapPkOL8Qcv6r_sLfcFc27ObiyDM4ERgBiNMQE1PvXGqVsuxkBJk2RVX6juzMkB0RW9fIhK3vQDcJjNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sImYEJbLDhh7etzFMO0GU1HxHpUBSzOrV6bJ8r-Cwj4NlsiQBMEiYAaWkvKgqyKC1fWDPqCP1P5HwxJRuuoOLcAYbIvG0bweYdnP_1wW8fncRsW6E9h1dKtpoCyxAapC86vTvDI9zV1Hsu7qx_GRb4-gI-pVJedRENNUG1iCOVPHdJJ7DjYigNcBG3uffmqK-qOcln8GjEOqostYMZHGJwQz7sgn1nzxZzLAl7o7ktnp-vfzvLtIJ3jVzWkFKw0N14DXF0__mA3_zP0CjLRxDCwG7lhkBZ40z-vNCSZ2qonCnZ-WSkUHLuEJRm7apiPgSpxoW9OJVV4rXamueIvyZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hhPD19ps0OhV6YXDG1s3ZyoR0V1_TJXsQ31i4X7TdqNaXE7TN6bUxXTva5ka9MpqkgzNEOp-t9cONJMmkuAQzwvXK43agxbh_lOnGVU_q4vwym69ECEV466IwZwPUNjCYWoxvW4bzTd7P1ocQhn9uy3b8UbFuMYN6TFoAMA8FaHLRAxC9NW56-RJQMnJohApi85lCCCA6lFywE1ZiXr3EzJfZqRTivr1MNrCtaVakYPoS18OOnVvKjalKFcULmidD4Gx70ECjuhfZWkHxt15UXQYae0lei8rYN7ozL2m52UW0t2QuCU0rSI4QYr4EBhUzW4HTviok7ZRCJsSaQ15vQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=edvy2JH51W7uz6Bli8MmDdPsSRbt-PWHxh2ype7Oqbv89TRRNJ6Hu-EW2J_qBhpVsxF1ZrI6kD3Q_AW_cz9U38STElY33lEnrGUNunVUztZL2nyW9KEdpqw9seQ4XUXt7cDH_dxKPhuoWxXLapwiuPXghjRriMT6ouIliN-Z3uwxBncuU-L1COxmIiTiANQkFZS5d_aRs0vMts8o0Y-_WeBEKF33dQKdRynXwIqBD7ppUP_sPvdvYkW9p8Ur5M6yKGdLeGWSPI05aDSAJsLmKK2gJ9qIi6r0fqOJSRyl02lEoTfegf4vVWvt3tG_28Y7cJ7C3oF0hYp48FV4bPKwtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=edvy2JH51W7uz6Bli8MmDdPsSRbt-PWHxh2ype7Oqbv89TRRNJ6Hu-EW2J_qBhpVsxF1ZrI6kD3Q_AW_cz9U38STElY33lEnrGUNunVUztZL2nyW9KEdpqw9seQ4XUXt7cDH_dxKPhuoWxXLapwiuPXghjRriMT6ouIliN-Z3uwxBncuU-L1COxmIiTiANQkFZS5d_aRs0vMts8o0Y-_WeBEKF33dQKdRynXwIqBD7ppUP_sPvdvYkW9p8Ur5M6yKGdLeGWSPI05aDSAJsLmKK2gJ9qIi6r0fqOJSRyl02lEoTfegf4vVWvt3tG_28Y7cJ7C3oF0hYp48FV4bPKwtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oLiGV7GlC6xdCjYI7gM8xv6RckKTJUXn6w-gSW74Tzp_5GuCJT2srncFNGkD9aFI3lHanmF7vJQw6tFQ3TydZhGrNNlMptn9bCL4F4nFBbZJEbKHKqERWpuMJbxUTYzbdOSND2J44AHars4WHu4ZxdGbeuQfqr0c3ucKn013hstK7bMRtO5Oox-D8oFMMuvyoQNi0hrcePjb_hmq-Wimavx1XEKDxnSAfLEIfWlq3rqhY_6iJzGbwM1CUoyoM8RZII3DQ3AJpMxxtbBFxoXMcWL9eFNg8U8MpT-yau6YzUp7IAS4A4k8Kkzh7fy2m0YCTSRApdjuokIFhmec8XeK2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y8lDjgYENoRk2dmmKgS79-WurFEkxoEnEi9uQXH2K9XW9UrKQx1hXG5Ow70skXdAXnohmk4Vrhd0SvS5LIdUrIq-KZL_75rXW0B-7MY3cdSh56y12bLZbKGYosCD-zglFEUiiQJKri7HR_2vkDm9Ve4w5sJcLd6M9slCTQHpBOZSYQ1lupSmTJQ4DZ6sTSNSFx5ZAo5xXmu5t3YBACxDZ5Sy7jWLziIKbNUdrLulNQLVYv8fYb78nxx5G9zu_1GQbdg-IY6mAdoc1GRfGP2uCDvUD9jTOWqrv2_XffUmDNcXElovj5ywmVtrvi83uhmUkeBQBlKPOQMa65vOV_6v_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dPzZnABBrImcL9aR3ip7fP9pHiY4lY4pG4fJy1UJvOiKYUiZmlZHraUdS8KiPcXq4rdAkW4-JPRLUvB_xzW_CYufuHkoJZQOIivvZgbaz06NzNbyLsnrln3MXM64ZcVsQMXY3zeqc85XVQIdyaWkgyyqY3_7vwagYLBspv7AttdGEsxravneciA4ezmRlnhU3oTf8c_1HOe36gcGH5lTBf3StqNJuC1JaHkJIMs-2Daa5C89IuTbU259gq2mdMho8YKDiY8ad77EmonDpBk8oa2oRFCwIQR6ILCILQgR8S8-dVBp-8IdEyYL-G2rh3w_evFl9SIwjhzPN40dVw6SjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها به تکرار نوشتم،
تنگه هرمز، تنگه احد اینها میشه،
به وسوسه غنیمت گرفتن و پول‌ درآورن از تنگه و اعمال فشار بر بازار نفت،
دست به کاری زدن که جز زیان و خسران برای خودشان هیچ نداشت.</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6694" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=NeMnkx4v5a2XABzg-AnQgAnUoC_cs2f2-e2A59dI6vJDVxtwy9jwsDiVAK_bharoWvE5Jo2TJoHcm9WrcM3NktzB7LZpe_jvjuyr-3r7mKSumprZ8FKedE3xTg887glPUfHRtKgwaCGTyuP6Hrh5kZq6vnDbr2_MZ234LSw4kp6ZEXghSWKmfy64AKUhPQkAZ-9wkjOqmmayj5NMNZLZUA3LOS1780CAFfdFbEI3bm2WISxzRE5GM37r1CrI2C1mzORNwrwMW8CVxqsr8SYYxWrh23TrOA1fXoQedBJzMGCcVr_1IktTsMqs3-w0-GDLaTpREYtAr2jOpkdpLI1orw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=NeMnkx4v5a2XABzg-AnQgAnUoC_cs2f2-e2A59dI6vJDVxtwy9jwsDiVAK_bharoWvE5Jo2TJoHcm9WrcM3NktzB7LZpe_jvjuyr-3r7mKSumprZ8FKedE3xTg887glPUfHRtKgwaCGTyuP6Hrh5kZq6vnDbr2_MZ234LSw4kp6ZEXghSWKmfy64AKUhPQkAZ-9wkjOqmmayj5NMNZLZUA3LOS1780CAFfdFbEI3bm2WISxzRE5GM37r1CrI2C1mzORNwrwMW8CVxqsr8SYYxWrh23TrOA1fXoQedBJzMGCcVr_1IktTsMqs3-w0-GDLaTpREYtAr2jOpkdpLI1orw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=ZPhy0Dql7hxMqwdxh8JCsW3qPX1rR9Eva0ZTutBlioPmXuNAClLnkBpI_STzvcViORf0_9WHKH0OBKywSiu4PBabgclzf9KkCDdV_SrdWr_Lw3MDjIzW-2SNXrp1oQeHcSLkTaOf2lidiCiqjojpmQG8c9a4ac5HHfPjIK8XiGET7xjiYHuLpHqZ7xDvSvMTM1hrP1I6nRbV9XvtNZk4OYtAqyDd6KhKH7j_5vDVnyG1A3jPP5EIUxbzI6acLjgWDGpxQ7nd6DmhS723pLnbbr5zWUJ11xJZGIv6u_WGmediKSqHPVBQWXSa2AaUCD_uGkIUCNyDlhnsmj3bzqcSPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=ZPhy0Dql7hxMqwdxh8JCsW3qPX1rR9Eva0ZTutBlioPmXuNAClLnkBpI_STzvcViORf0_9WHKH0OBKywSiu4PBabgclzf9KkCDdV_SrdWr_Lw3MDjIzW-2SNXrp1oQeHcSLkTaOf2lidiCiqjojpmQG8c9a4ac5HHfPjIK8XiGET7xjiYHuLpHqZ7xDvSvMTM1hrP1I6nRbV9XvtNZk4OYtAqyDd6KhKH7j_5vDVnyG1A3jPP5EIUxbzI6acLjgWDGpxQ7nd6DmhS723pLnbbr5zWUJ11xJZGIv6u_WGmediKSqHPVBQWXSa2AaUCD_uGkIUCNyDlhnsmj3bzqcSPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=jzsSLwxIk1xeEPR5Jmj0GbAKboNxZjTBIrbN7GhEQS7Azzm1Tlr492Hi-UYPCnLS8Yg5gNHMS7dW1_okSaPXD2aVVdD5zFoFVeRrmImDt55C4h8AiWUizWZV4w-D6LD9Dnxab3YLE0_JGZxVlgKYEvSFz1SCQ_NosNtTf9F_QlU61nqNLS4H7GfD0Rsk_5heRx1yqhjnfeMo_WCBb6eh-_k2ozMCLdgOkPrnBrDvtn6ABlKXMVs-ZZ9QUQkNXtV9gyh6uZmmXaS1Klh-keKGGzBOqBVT7w9wCDtlrsRpKulFCA8j_7waDb4DxXOn0Gdc5q4XXJHM7ZYWvb1Hq7cb4iYGb5JQYKIkKo9Ob-axouCj6kyxZsHUu846_vaABO4kxEnEMePOjlOd7K8FOW5iPS03kzEfyYmEJ6xwb74UlyhRF6KhOAkT1OhlRufoV1Qr6HhScLlZmrQMB6SZltw3ppLYjFZ8hZWLX41rK_avPjznAR69VM3uRkb6Nykv3umSZYRnLOVaW9Oz1b9LQR5P1O4oHeoN9ijMJ6Y9PpQO8Lad1p1-7A3Lpih2rLik7rH_votVdjdS_n6trO5bOeQWPGhHJhxpAtn2N9EwTODLYTWQWkE_pBuOIFE3Wm5jaenhFH6rWye8mCuMBOrQC-LUr2ZHcNUGE9nus4GBILHUPh8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=jzsSLwxIk1xeEPR5Jmj0GbAKboNxZjTBIrbN7GhEQS7Azzm1Tlr492Hi-UYPCnLS8Yg5gNHMS7dW1_okSaPXD2aVVdD5zFoFVeRrmImDt55C4h8AiWUizWZV4w-D6LD9Dnxab3YLE0_JGZxVlgKYEvSFz1SCQ_NosNtTf9F_QlU61nqNLS4H7GfD0Rsk_5heRx1yqhjnfeMo_WCBb6eh-_k2ozMCLdgOkPrnBrDvtn6ABlKXMVs-ZZ9QUQkNXtV9gyh6uZmmXaS1Klh-keKGGzBOqBVT7w9wCDtlrsRpKulFCA8j_7waDb4DxXOn0Gdc5q4XXJHM7ZYWvb1Hq7cb4iYGb5JQYKIkKo9Ob-axouCj6kyxZsHUu846_vaABO4kxEnEMePOjlOd7K8FOW5iPS03kzEfyYmEJ6xwb74UlyhRF6KhOAkT1OhlRufoV1Qr6HhScLlZmrQMB6SZltw3ppLYjFZ8hZWLX41rK_avPjznAR69VM3uRkb6Nykv3umSZYRnLOVaW9Oz1b9LQR5P1O4oHeoN9ijMJ6Y9PpQO8Lad1p1-7A3Lpih2rLik7rH_votVdjdS_n6trO5bOeQWPGhHJhxpAtn2N9EwTODLYTWQWkE_pBuOIFE3Wm5jaenhFH6rWye8mCuMBOrQC-LUr2ZHcNUGE9nus4GBILHUPh8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=gSxSah2ry_2R0t4dVajUsjXdq13N_MBkQTdKbCp4Jmz6ZGkTE2L4D86RevpAr7FARi-EG_vdWkszb8bPFHjLJx3QyAh-lAgPuXgq_n0ZePYoJniNlqF-b1lPYYv6FtYXbGnMo2lUeOc45iJBvbUXlxYw3QarUQnyFUWgYMwGdzaMB26bujSuhBcy4iBORzMIOVsBkpyElLDI85rYbEsMSeNon79DYOvXJWqC5WHVKVJfifvw20_3xP9umULXvMCvKuJF_bXJqU1qXdNz2ZQOZx5fNarDIzCzraz1Ju0T1sez7OSBRiIV5yjvYVAHhLuHIUB_r3P1pvWZEWH2gY7aF5PhHKdev5YRbqc98JH5dPbdmWp08glTKpe72-bKGGow2fUU1jLmjPhJWpjEWVyQhnLb_TsuXue2LnVsnTnM2mDrty5LEfLwafXmslEn766km8XbSAGHM7fwv9f4J3Mpyx8a3tI0aTzGSpdOF7Imx-kSG9WTVOWwVDcNR_0Tlg69mNZG-9LILt7pvfpOCLlBwt5VnawBD5HX_s92gVA82vKkZjLMUfQy9uFgRLlxwQL8IrBqthu7Ki3Cm1HvLow6MsSi1_pMOG_RWW9cpvaPobbKio-U3Pk4uOb2u0WHCLGA_b23P20f2nPWKs-elfYqYO_keFV_esqkq77f04uUGuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=gSxSah2ry_2R0t4dVajUsjXdq13N_MBkQTdKbCp4Jmz6ZGkTE2L4D86RevpAr7FARi-EG_vdWkszb8bPFHjLJx3QyAh-lAgPuXgq_n0ZePYoJniNlqF-b1lPYYv6FtYXbGnMo2lUeOc45iJBvbUXlxYw3QarUQnyFUWgYMwGdzaMB26bujSuhBcy4iBORzMIOVsBkpyElLDI85rYbEsMSeNon79DYOvXJWqC5WHVKVJfifvw20_3xP9umULXvMCvKuJF_bXJqU1qXdNz2ZQOZx5fNarDIzCzraz1Ju0T1sez7OSBRiIV5yjvYVAHhLuHIUB_r3P1pvWZEWH2gY7aF5PhHKdev5YRbqc98JH5dPbdmWp08glTKpe72-bKGGow2fUU1jLmjPhJWpjEWVyQhnLb_TsuXue2LnVsnTnM2mDrty5LEfLwafXmslEn766km8XbSAGHM7fwv9f4J3Mpyx8a3tI0aTzGSpdOF7Imx-kSG9WTVOWwVDcNR_0Tlg69mNZG-9LILt7pvfpOCLlBwt5VnawBD5HX_s92gVA82vKkZjLMUfQy9uFgRLlxwQL8IrBqthu7Ki3Cm1HvLow6MsSi1_pMOG_RWW9cpvaPobbKio-U3Pk4uOb2u0WHCLGA_b23P20f2nPWKs-elfYqYO_keFV_esqkq77f04uUGuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=XqhhzI68KHBChXUHlxeBuwJ44r6ifgHd3GepWQT5-1sasV0zMLr4nXLvH9DGQeI_iC4TZUv1ndRuL4JWny0XaGWnTGg2KrGQfd_HJWNsHfHuPYcG8pR17GgVbqKMhvO1L1qhHP_03RIwLdsLjBNdNp8vqRLVwQN2iBv5EEvvGA7OdH0-OeACFVKos1-pPtK-tg3_WX8mliUy0_MWVUQDOSFfLtiUffHkC-SkKz0uRATibC-gV1lNqpQ-Gmk59XBKQF59bWChX2fUxBhxJR4YUVFJScaLGYoDO-Ont828vfd9UeM2MaLNDAt3hw3ynShv2zDR49d4kxFxA1W_BnArNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=XqhhzI68KHBChXUHlxeBuwJ44r6ifgHd3GepWQT5-1sasV0zMLr4nXLvH9DGQeI_iC4TZUv1ndRuL4JWny0XaGWnTGg2KrGQfd_HJWNsHfHuPYcG8pR17GgVbqKMhvO1L1qhHP_03RIwLdsLjBNdNp8vqRLVwQN2iBv5EEvvGA7OdH0-OeACFVKos1-pPtK-tg3_WX8mliUy0_MWVUQDOSFfLtiUffHkC-SkKz0uRATibC-gV1lNqpQ-Gmk59XBKQF59bWChX2fUxBhxJR4YUVFJScaLGYoDO-Ont828vfd9UeM2MaLNDAt3hw3ynShv2zDR49d4kxFxA1W_BnArNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c9WrgEUpKeWyS7aNTq0Jx7_KWEVkSjSxHZsBH5ZlM5Dt0gnZ9H59lcxmWOQL4s08RGB_rKqCtUapZ8nbi3YOL3CgZKcGeph82hLzI0_SzncdrXhGD6vmTVXyTrmsJUZiwoRWmbqxIwv2Fr3g5Xh1yydvZ_S3MYnNb0GbeW5FtH9blQT0Ni4psCmphO-rHqzhnASGZMuqvyRGdbhNnEM00EY7zAKlJPrGparFsde4zDc15CahI1S75nZP12u5fv6Bao37v2Zof1aBBt8gzmpgMbv2Btu5ayocipF0UzIedNu27sGWUrX1saU4hIv1qIOz8IBlpdjs508GhWVRHRYlQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=ktbiJ412l2DqJ8P9Or9cXZC3J9C6m02-hkDfBVhP1TMrC70HqtGzmva7pdm160dZx0IE_u58H3upMqkQFdXXyKrupmU7qPiivUfExqlnu_-MtqcLgitue0qXIyQ-nAkpS91Sl4IDhNj9ts0RIlmK-_aXeJb1pTP8o76XXKkx49AvFd6X2IE2EwCp2f9VkFzxc5aZQjoxpRTWzzYmg89z99GU1WUo3ZhG2gjHjP7oJPaHBxdkO3WtaQOrE-P7weEVHLIj9XnOdUYb_Nmy_bmuP_O23ZDdEjyHfU4fyTVaVbWjBt5eQxTg9vpfyqIvq00VBIVLChyswmxNw-HcjvC24g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=ktbiJ412l2DqJ8P9Or9cXZC3J9C6m02-hkDfBVhP1TMrC70HqtGzmva7pdm160dZx0IE_u58H3upMqkQFdXXyKrupmU7qPiivUfExqlnu_-MtqcLgitue0qXIyQ-nAkpS91Sl4IDhNj9ts0RIlmK-_aXeJb1pTP8o76XXKkx49AvFd6X2IE2EwCp2f9VkFzxc5aZQjoxpRTWzzYmg89z99GU1WUo3ZhG2gjHjP7oJPaHBxdkO3WtaQOrE-P7weEVHLIj9XnOdUYb_Nmy_bmuP_O23ZDdEjyHfU4fyTVaVbWjBt5eQxTg9vpfyqIvq00VBIVLChyswmxNw-HcjvC24g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=nxQxBPMeOd7Gr8OwAwmuU2sdmZ-kRC5aYNFq6EXZCOmmp9vQ_x37E6nxibNQ6aj-RnAgHuYMMI1MZNcrpcyBKc5iifAFhQm6CW0y41hSP1FHW14ffhZBmve77RQKZXAJmUp1ckphTnStkNLwpYYiEOS6CLqsHWAponFhQrBOfpOpvAfJNtRx3sKXCSZVjrhc7qG9a93RYEhGHbY7VYQ1qNHPOVNXFtdWu2_vkC2thyUcz_5Zwzjy3c_vB8PrpdYvQBsUGsBxDSF9vjm5X3Uwt6LEp19va1hQLXhAzbTYH22BhoJLLjdR6J_BorBe1aBBHl3f9hothDkg5PuvzAlJaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=nxQxBPMeOd7Gr8OwAwmuU2sdmZ-kRC5aYNFq6EXZCOmmp9vQ_x37E6nxibNQ6aj-RnAgHuYMMI1MZNcrpcyBKc5iifAFhQm6CW0y41hSP1FHW14ffhZBmve77RQKZXAJmUp1ckphTnStkNLwpYYiEOS6CLqsHWAponFhQrBOfpOpvAfJNtRx3sKXCSZVjrhc7qG9a93RYEhGHbY7VYQ1qNHPOVNXFtdWu2_vkC2thyUcz_5Zwzjy3c_vB8PrpdYvQBsUGsBxDSF9vjm5X3Uwt6LEp19va1hQLXhAzbTYH22BhoJLLjdR6J_BorBe1aBBHl3f9hothDkg5PuvzAlJaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ysb8Upn3n9_5edS8BaN8HNrglu2bGQq098GckiORifVHJ6tFeoTRAR3wNuhSY0zKBA3VxYYuUngGO9Je2XSVmGwusWQ5P3KXtEz3nHXhjMqaEBqMbhiXpox3XOl4bAB4APL3WO51ylHVZa5uIIe_QXPrhLR5Tr0vyC_4h4j6zcUSH82YXjhvZGRzby_VZv7xD8IEWMDemMbz7dAEqbjEm0sZFE-nHB1djDk7ZohIvpjNGpasD8t5WYQsxyl2XGldb3W0NJMIeJxj7jU0XN5K_uysU5NXYeqpv2qbvVqAy5ZUXqB8iRQjC7oyfjGTYYkzDE2xSk0ttAeQKbKEyLoXNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JHe6_vTPCV3_bCpug_ctvE6iCIYwSPLrJeZtjiKB_KwA48ZL83b3A6ObdQENGEfwsWUQq-tlwS_SU4FFJMo7r5UJYswjIpC5v1CjsbLW_pSMzP7HVYbLdKC7HRP6cZO9rNgkKQu22QbADK_Fp1t8xSd0TjqE5YKXtlUfALGfp4VJ3bGzeoCNCkzefVjCP5aURP9EojLCl3dZQPMLBJAllG9xNnZ7oX5TA-BRW4pGf45tQVpq1pPefZgamY0dapDgejNrPJD2-lb_Dz1glPgBKMGYySsol-G83UNcRMfeog4crWFG7mMq92AZEjVO2I_F3fuLp2x-OzqBx4kY5SjBiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cPStizU77WCZercdtlr1ihNrDgwqwGjCbXmsKGwImXTO-iIPB0ORHXNITgQ3TY_g1K-_sP12cgEAdj4JH5UXG1NBX3SJQwRybhT7zjYUf8rWtlc2agwTUrJqrhWcG5aJ8uTTetOJqybQBaSI5xOg5BxgvPw6atObe0b2TOC5OBHkY3Iyd82k2NAkr0eD1LdcbPwTH6db7otwE1fQifQ88nuYd8WJWmDmAw7c7XMsaP5F4oT1q6HR-pXzX8ObTLZoWX-jIS2a_m9k6vn6BqpumnhMlkIrp8hXN0RMaM-QAerEgmaRcbl7KJx43jy8H96sO_SaflrACiAaU2mf-5EVWA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pWDO1nPrCxNSdLJTtdEHq8rp1KKCEuVywj7MDV6SaYRhekZqNcIxVPBNUz3QTJot-SdGgs_aDRALwOrJRn2loxphohVHhdwJe7osNVJgQ8pasDhnK_P39uQh0hqtYmKL-paRXCV9HWKS9FyVQAlbOkj1MIpdg2aBg1CW6SqdXSHn44YW31ZPX3d8HQX3AZ6plX33-B_OrAMPLkt_UFokL_n9iqRu6RKG69tw0dNhMM_Al3Qio0nccpqFRinrpFUErv1giZoCBrWwOa1Wmj8yA4zLcMiWyhIjPT6UArrsIifvp-wgUZeG-FkrL_dPiVM8elqnPFxXjuqpvoLFb653XA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RtUSxO_x0DW2AXXAisQIsrHTik6MwtRU3eorvIDEykxic1g6mng-BtlpgUHvWH7y1bPSDXwaOemhhiIttw3ASZ90Fo_vGXzkt-xbQA1IOCdpqzyGnZr8nbAxI_SXoVUE4Xq_MV5O4PxoP-jjMbZHc91PgB0SGp9_9EoQZD8ibzyvwrE_cbj_qaJjSBDjoYMA2ZHNbY_GLV6F3qeMBLq-J9YtP-wHcoEQJwC8PRTim8A6_nnnpdltjQYSgXyH1hfHwZAf_4SjmpzCxgOe-7rkg46AZjjzs3G_m5GgITJ3cz5l4Bcp2q8A5qm5DVk7LLvOoley9qM59n-_f3T4jxE_xw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYzNtWRpDtquiFIrAXjtsnczt-fXUHjFMJ8C2NYH0RRbPYh1TUeQSBFVsrqkzK0XzHrv1s42D9BL8cTH2TR2S-ltkVjwrZIhPF3NlZR4REhTw7XiWDmKKAhA3XQ08IvHJHLdgsv2eHA3m9L0t98O8ISozIJa3sprqTjoUTx7pqEfkql-IyKh_1z2FPNWhYh_2u9sSHOJ5coINcHOGq_earcwzlnXfzdnnIsc5WvbJ3C_LFQewP6iqvQ9RHROh4jG9txbP9pUWIngXmxTZxEeOGSkRe0huXUn68qunkK81BcskUXKZWK6_SL5NGqQFs3K8JBVTtJVjr0PyPtAzGQZWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GLWkbP-k4VVXHWj9iubX26pJmmRPb9gCSdlhEHOyAxv16LJIiWe4sHBq_iPbo9pj70vUoXuvalC-sBN_fzi2A_8rAza6pjWVKUVw1eCAYt-yWh5an8ATYCleU1Yv68iWk9NGC_bXe-T6iXL3vgdIorT5C5zLkp5OT38MuzPdaIZEyHtew8IBdd0HjGEaTICLarV3trAizZPGfFFfwEO8oT3Cwq45c97KNqsZAJA1DB6A7tXfFdL_WK1FgJtSZuciufnhyiiqt4bQ0538-xdrygY30lwN7JuVSdHs0bmQCvAumvFj1oDqxVrbL9cHtrFU6lzQTeYPJ6mOvq2u5pNmmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aXCpbUs0A-1LeCi4HopdDWJ6Zpztwp3A5UG5lpI8V5VrksFE6MPqmZ0eR6K_CCp7Qdm_YDhIPpbtelOE-FrhUfIPmCOulEC1_0IXUn9WklWX3L8-KhEmXBcKDN54cQac8Nbft4fYG52iqw_6EWVoX_cd0a4wKbT7BClDIMykU26lIhuN-wAtT_UJT8Brjn6_QTBD2aOOh20EFjj3mFs2n-H5tK2vC96UWBs79vGFPiRaSJiO8h_-LDJDki38PNaGJWrzUsyRA-JZH5MPWnGhEV9RVpPNLm3W29fVNkqFYYIyQ_DFe5g68Zl6FDpcmsREJGmsxtd-ChZsnxF2UzOQwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OVB0x9vl7Wd0SKSFqR_EoeKOTcdB_sFw_7NH2MAlxEmpuvGg9E9oUulW8xQEU95UvFe5Es-zHcJAZBDKAbbnZMn3c1VL0cHuNpnul2psUkVVXWZqxniJA3VYi6CTbCSNhh0jyosu5ITYW6n2hJ8Q3xCMFUGMBhx88EXswyzw72c9_6Kdj1jH91vjrJb1alKdvM2Q1KP7t1N0oHlhCrEPkEZexDzzi6lMMRmcmrPNKaiYwENQvFV2L7MgLEnNUuhF9t0TUGRvoVA4L7khgriHUYhvo72i0kjb9zTNUpctPL_C1j7ez9fW6pMHNbPfPwsLc8sdBj0MBm-9Q7y8UtenQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rB7m3U36JVwXd4bkOyndWbEVf91PFPgC-CCWP-wrpn7hDsg7ZOfxVTFxqj17Nr91fuxr_Rk4aB0yFaWdG13z322xySYHGuDY5vGVRc1lUNgrtWJYK2knJ-c-1Z59HRbjrEpcOsVN5hIHc5vmbFm_Ab60XVhzw1SxJcVXFoBWKmk2-ljMxl-fR0JjbUGtifVCPeu6BhPmo4V66S_JNi7AdEzuOI9T7k0UDkv_d6EPbSvWhP4fnMRITpm9OIWzg1VSOwXgv7MNr8GPGFRcFWIS6uoX4a1nN2FSZXb1KOlvdusTxL12QbiEKcJvqgz5Dondy_kwCMuLbd_KSjght5VZ3Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6669" target="_blank">📅 08:19 · 11 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=aUESQsKF9o3GFdCmFj0Hfoh5eJ7rsDFa9NAh2G8tKn_fEtGRxML9b4Ocrp55DQurBR7wgPB842D9tj6uzOQiGkShSZpYDKEsZwAY8KpOh6MG-U1Pli9YBVvjI9INqFWQ0F2OYi3XFPbEdvM_nVul8mOhkvVPr9yoikIu9bWdskIJ3krz5-k6oHvKLbPtUwWIJXi5H1YQ8Vd34TWd7PDe5TGpJAxIOXuB5q4_yN5Dv3rGLFVzdXYHgB0UKZ52HH2XUbRbjgOklObRpHH2utO1w9IeV1VuesjjaD8dQCE4gWV2vIcOSxZIZ13iAclefNC4bgmALYW_08moRou66OCkcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=aUESQsKF9o3GFdCmFj0Hfoh5eJ7rsDFa9NAh2G8tKn_fEtGRxML9b4Ocrp55DQurBR7wgPB842D9tj6uzOQiGkShSZpYDKEsZwAY8KpOh6MG-U1Pli9YBVvjI9INqFWQ0F2OYi3XFPbEdvM_nVul8mOhkvVPr9yoikIu9bWdskIJ3krz5-k6oHvKLbPtUwWIJXi5H1YQ8Vd34TWd7PDe5TGpJAxIOXuB5q4_yN5Dv3rGLFVzdXYHgB0UKZ52HH2XUbRbjgOklObRpHH2utO1w9IeV1VuesjjaD8dQCE4gWV2vIcOSxZIZ13iAclefNC4bgmALYW_08moRou66OCkcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YMpzsEqrYfmY_CQpvH9usq6TLMIXA7S3zs3aVbeLnurnRU7PJQbm9UpZ9KDeGsgKUO7c--aw6Kdq_rPT4ehx2SgT0jLyrNCBJ6ruRF5n9iyfYa-r787SUlKO1LUngYj5EpWWVoWeSjrH9fWj68v5sMQbQzCOY2PW4sE3KeDBR-YIivoYiGW_3ey1hIDz1EABy-ikyzcelkJC-fP45uZoA-X-kw3hdBGCj6urxzsc9xJ2fN-EKPJ2d8WqyifhZy0JeEwjPxVEAsTN2RdHU5EG324UWyMsttQY0jh9hjj2AoCypA6eTz2IG6ysniUQsHfdpN8_VYwpj74WDJKA9_kAUQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uiaDhSlMlZdUVdUSK2nn1y0g4l4CDs_Q5am6IkN3T1DnL_GfAY8VBn3GIOKXL76w5rWiru9szYrqVbLRxV8hMWBfd-VK8cLhWcHydU8rW3vE8Fq34gjeaNa93EfOyHAsDI1QKzCD-IFVFweHJhC5iN3wkwAw7HZRXe4X37_-EIjzuYQn87gBJAZ3uAkWgX7qOGKYhzpLROZA1PtOjxb9_XYbu6xP4gdJW_-ZqXl7vF2MQgCiE_a7PPHHfjkcmtM2Zglv9YsgSyT1GM53NrzQffqaxacFziK7ifjKXW4V4c4bvvEbYlhuskk_YsJkiLAwWs0n7ZdsHvb0z0-YrwAH5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=iTmDSX0bQFF9w0sZkxdsYhc17A7J6UVAZUrGW-EKzjK5d9a6D-S2wEXuxps39U3GUYOgRnRjZimobFiVrEBomGaf43FBFtwENEM0jGt-6fMuMK0rkQDIf25t_DZK4VkIZvP7yg_x9ME1wVOZ0IHxaETkjpY197B7kW9cyO7fy1PatEG77p7WVmR0X3cJnG7xXQKlLdIApCYoJIjtvZX56IDFMIOrB_i4caRMf8OyYEUiHtPpRD9VhBfgL_2KzW_RfSg2rSFyXcvPUYClQjrXJJAqoFqzRZCqegrakcRVJ4Di_RuwoTBoExI06k5JpjqHwGgTd0rC1pnG6BF7uTnYug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=iTmDSX0bQFF9w0sZkxdsYhc17A7J6UVAZUrGW-EKzjK5d9a6D-S2wEXuxps39U3GUYOgRnRjZimobFiVrEBomGaf43FBFtwENEM0jGt-6fMuMK0rkQDIf25t_DZK4VkIZvP7yg_x9ME1wVOZ0IHxaETkjpY197B7kW9cyO7fy1PatEG77p7WVmR0X3cJnG7xXQKlLdIApCYoJIjtvZX56IDFMIOrB_i4caRMf8OyYEUiHtPpRD9VhBfgL_2KzW_RfSg2rSFyXcvPUYClQjrXJJAqoFqzRZCqegrakcRVJ4Di_RuwoTBoExI06k5JpjqHwGgTd0rC1pnG6BF7uTnYug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=DaUzD0_x3nhwJz0LjBTfq9NuwoNpgn24HfdSm3Z7cAtYaS86U4EhnZdRUEIBvYnCUfdlP_SnfV5GYr37zE9kZx_yPaS9-uN80aLDLPK30lYCSMOlXHKjDEcuV-5-RGXNWYYAwXLgxc1DqKrl_JjmwxkiVsNFZAtLt3yCi0ml29VOQRYoAww3kQ9R4EojiLdiDuPa-d7enCTN3_ewi1cQY10BVDCzgZYKLYV4yR3xyxXIXYN85k2-hGllY1NxFEicsabobQ2RPhSEK2WRyURGDmDJHOwZgvnNt-xVEMg4KLdajyf_kA3YusEurJxQAIDMKW6dnUzZfmo6DAJrEbkOUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=DaUzD0_x3nhwJz0LjBTfq9NuwoNpgn24HfdSm3Z7cAtYaS86U4EhnZdRUEIBvYnCUfdlP_SnfV5GYr37zE9kZx_yPaS9-uN80aLDLPK30lYCSMOlXHKjDEcuV-5-RGXNWYYAwXLgxc1DqKrl_JjmwxkiVsNFZAtLt3yCi0ml29VOQRYoAww3kQ9R4EojiLdiDuPa-d7enCTN3_ewi1cQY10BVDCzgZYKLYV4yR3xyxXIXYN85k2-hGllY1NxFEicsabobQ2RPhSEK2WRyURGDmDJHOwZgvnNt-xVEMg4KLdajyf_kA3YusEurJxQAIDMKW6dnUzZfmo6DAJrEbkOUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-7zkJ471_SLT7L3tEpOLfS4j9TwdB5fab6XyU0HcBgg8kyeVHiSkinyD8GqqkN6Roi7LEwIZ4q_LA5SXDmPiC4X3XM3K28O4Wj59HuBeV68mQcNATIzzWkh8mOuo17FDV4ZhVMhQQn4tzlGdUdVgLC7FZ7oqN6j_YtXlH1H_a5gn9sFKG0qmb_x4kl_v7lI_JGpGXX9w8EBk8AGRix2613S4Bt8TMk_-ijjSRZQftNICSz62NDPuZnrMrwNs5-0pXkVKXF7NQVKPzKMlpm87uFut4BTFwGIGdBbH2KCt8wYWj3qdwCjkXaIkzotOwu3GUJXEnx_kM5hYguNEQmKRg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UiEr2v56QduHW99hbR4e0OWHNUkdFKCkAEmgCg4ghOa3QhRRfGzWpQ4c_lpXyeAVMaO6drbuWwHPxCEOJKrAFQypNKcP4nXxzWOyZTVN5ViMO9S4rZnWfApIy0z0lRLFDE2rjWPmUerM2bebow23hGzdepgQBrgWd5z2R8iv6CGOrwaz6HFBITin05BoOlqIHlqD4Acb4cG3Jyj4vZuKV2QPnWCaR_pKVZyz_WGgDDKZMw1vacIymRxJllmLDiM20dwTzULtTIflAPxx7wcwNMEt7JyFxhIK8DACMq1X-KmJwGhiS7vU378o5CbjeFBiticPCP4hA1_O57LdvX6bSQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KWju0G-OoVkXwRTlFRndvjbhW_TVqo1g-WrIHui_n3WYcutlu0VlDxOrnUB3EOPOjt6Bie2u2Oa5_bHepNj5ImBax2Jzl60F8tG-vUX3YUWGGs8rBBxXxa5QR0QMFI4LwX6gavOhnTl2wyTquPnTjCY2SIDIb7ufD5chppOeEv4BJzQVDHOfTZSvv_6ePhB3evXaHrLi4lphBZrh2CXsUE6KC8eVHykdtdCyddDnQ6PaXy_JVVts6iMxRHhWDENJRo7tlmPc45kqmW8jHGQo-pWOhZlwIqRFFakBv7r6v7mXNyGGwerKc2qVrmHyreUCWacWkyJbhrmBrqBTjFu8nw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Py34k5ma8YH6YfFy90QeyUkk1hBlhfq85eg-pluT1kV7n8mwdfKYJJ1Ed8n9oLs3VaYP_N7NfE6kTnUiqNzDGImzju5X76_Px99SBEjx6Y9qgMptTUGJ7OxjnusA-E9IsdTch5ehrTcsXs9EU2h7sEOCI1WtX6iMFijail9DX9mVpvaJA4r3RQtL2DQ7Fndnrm8PMqpN1pww4btpD2ngvjNOqoihbiyxLp9C_NYGPHJJHRnpGZgE2103aD6widueSuv7xSMcyxIUoUxjOhNGFrLJIiRDFx3bOuG_tWeuxHRsznJ_l5INlxBNZ2sHjubNbyDPK5r1K00G2TXT1guXkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jBjAk238vEKZCmTqmBo9mmQLUN6NjxQ9i_vTOK18pS1FsABrBR2jMVrDrvQxiMA3EHIlJ9xuAYTj0wf0EZc4s-tiLlPM3RTzGvxLTvg-b0CXp5Y5d0eP6Y_fdX0NP3w8kaOruQGC4clv8c3Ia3rrGifO77jGHMUCBhMG4VKP3cC7RprZgzbkezc8b0bG70hs2SCxjQQwXHFwCN5tjF1bB6YBn2PuXwmtqUfhzKtBqCrrHHKAd0nAYvWBSsVJ35Jujsg9dESrFDwc8jCCRD5zKmOAmb6SXoLxHpKJX6NVoJBwIUXuk15pzWqRxiwV_p-lQyItW_BKJ-CJzJpnfM6BkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RYNdy2hr_HRNAAuvDS0yu8decPyuKE1N_melzU8SCRFMSbpJqzb00lAisCXkBD45ad_isNRUd6ERUasdXuxs6ir2Fyby_fXc0XpkT-LGtkZQP4YIvhgMjmder1VIeeN6OsGd8UMWbH38rvEzOSzclu5rh4PDaYtqcZ0Tnv5ongo0GsJmEP3SiXasW3OExFIG6yomKzD79_J59SR2_RV1KiGhzQZcFTfAcRhIep6xtiWCnqm33vu1NIa2i0bHTd3jzRuHYSGYXCurcH68Z50haCOm3FuLJEHSbSqvXh_0NYLWBb153j9DG9j2uWEkKDl2oFyBsqxKt8cH3qv3wPAbPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NMEd1a-A3VrNNMKEp9X_o1NlCt-GhpXz5SwMbwBwSfH515xAXbsp6YxKooYYE3ls4P_YK05lG1S-AIKMTbRN59BT_9NAHssYMcVmGIZw5mh9W307ob5l1jtSQ8256H9vyr79kjYkv3Az0LjInV2H89VWmTD3KMB5vky6xmr_A7MQdGkXslAGiIDu_1HScCR76sIdpOJVMGR50ZNpljUyBW1ZG8c5eTPS4D0-DspdmMJViErzW79RKeHr_V_Zxyp09iW3JrNrvwjQBnf8rxYcmhqb1T6p_rLGuXyqTT5CT334cQ7WMKCODbt3vriAMyirCKcbR_TTvm7bIIt8M1NnXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gvdwdnIR_wG9hkUPqpSebwJ_4aeIgviGgBOm_KAtcSOT4Ms922smyntiYBS2WdRuKFmiOyFREM_8w51InKT2ptvjstXo44--7TU3vIiGM5Jowqr2SyVNqhPRenBaKP-Yo6_Gl2xgK39H_yZj47SJQMRaL-ttZjl4skhdKmtSC74qnqmd7OJEj9ZE94PFkbTi-UQALIrZN_Nlwcjmb9UfxFkCeAa8bokhTWXVIN8iWqM9u_X6stkDtiPnBKBmYmoTL7FO_b6T8iUgGCU2Il0JHA9-mEFdnb9pdh_9UFrBLpn98Cycht_7Nkxd9vvzGoSehvuXxTM8FwJJoz0E7_2ZkA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=sfhdtzmN1d1r2iwARMyHiODK9-eIVYNx8w4Pg-pJ-9Xqc0ul8rxv_4J9zde5-b8ONe3VWwsB2AWPCKIdwrGxWt8cFTF1taPlqLqlRuSRMTDcFqEIOdKBr_8BW7rZ2Ux7rOXsIWDXHnJBALjAOev4krJyKK_gUxv2scFERk5RObqqxV1F7OemDzMNS1UYuhoAyyUn5JSXsaNNUGER2E0cCYKH1NBnZWbiCQxtabYOwYd1SlEQ7vecv4-2s7cX83FgBVkzb0aGbHOt41w6tvmNDpycLKSzdUh0jhi6RUmyQMzspf3TXiPkTSMDzI_yGZdrZAatdL6Bn4abfKJ5Mow7Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=sfhdtzmN1d1r2iwARMyHiODK9-eIVYNx8w4Pg-pJ-9Xqc0ul8rxv_4J9zde5-b8ONe3VWwsB2AWPCKIdwrGxWt8cFTF1taPlqLqlRuSRMTDcFqEIOdKBr_8BW7rZ2Ux7rOXsIWDXHnJBALjAOev4krJyKK_gUxv2scFERk5RObqqxV1F7OemDzMNS1UYuhoAyyUn5JSXsaNNUGER2E0cCYKH1NBnZWbiCQxtabYOwYd1SlEQ7vecv4-2s7cX83FgBVkzb0aGbHOt41w6tvmNDpycLKSzdUh0jhi6RUmyQMzspf3TXiPkTSMDzI_yGZdrZAatdL6Bn4abfKJ5Mow7Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CIT66eXy37ZDwsj9ak8CwYeRr8eDRNjf2Zok8YeI8SS4b6_u29K5P55uIPAXMoeEuwyZFauQTmFReSfLUa_URXZjWgJpd2Xk4KVLAPkPRyUB77hZgeKOi6vUA8VHjmuoLOAtkOuRC7GRCsmy7GLsrzG63P3VMqETj6IyuOQUORB5gCy5QsFx3LDrtx-8SoQoMoSVmB6tWUn42DNIr8TqCtv02HgV4YHrC_8kpneFy4YJo0ZTpl8HSZsK5mhQN9zAXbpSR9QMarMpbWx_j2ASjjwoV7zy6DebZkvN5Vq27VS-OnLbJ0HjAskU90yJzox-jx8JM5IyBlm08IKDyf2Y0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=csrlGyUktxDEWPsA47Dkxn4W-i9cLgrX5CSngNA1Q5URQMLF0oYUNpZP6izjuXTN7weW_Am6_2lmyIaDgU0KzGTp2eeHA7eX0VGSr9S3P6J9NI9sR2J5CFydY2Zb-tsZHlThQtCZCri-KLOhZwtHNCAMpIsx5B8aQEN3eZhaaPrLRe5cL89_WAsDVI5kkxMak1GIi384yedgYQJWnP9tEIns8ZqVkU8foJgiV-u7-883gZPDZMFoHCZbllc0bbUmzC12WfYENxDVBT_cce1apfECq3UDaa2qbiDsClUnaqCoOgVnf2gSsIIo5eIfQm0QAyCmJPCley_AS5y9ovfX6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=csrlGyUktxDEWPsA47Dkxn4W-i9cLgrX5CSngNA1Q5URQMLF0oYUNpZP6izjuXTN7weW_Am6_2lmyIaDgU0KzGTp2eeHA7eX0VGSr9S3P6J9NI9sR2J5CFydY2Zb-tsZHlThQtCZCri-KLOhZwtHNCAMpIsx5B8aQEN3eZhaaPrLRe5cL89_WAsDVI5kkxMak1GIi384yedgYQJWnP9tEIns8ZqVkU8foJgiV-u7-883gZPDZMFoHCZbllc0bbUmzC12WfYENxDVBT_cce1apfECq3UDaa2qbiDsClUnaqCoOgVnf2gSsIIo5eIfQm0QAyCmJPCley_AS5y9ovfX6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=nSMMnfrfte8-Cj0rqsOb8HA9wwjakGqgwuuHFMTwj9V_iTcanqJQ9vQRnD_f0eVtQMzGDbY07ml7ld3LhAJpbLlxtYV0oxX90r_tFNuskUuqnIRuj03cUf0Q7Et4etlCjzKUZ5tskP-r3UhXEZ9vLzL2uy0m-YDdI6JRLCjUGUCDr0VspmNKcUE4Q_Gcl9UEGc6uPilwz7-3P_oqSG8dNNoLqJQ2afHM1S7in3E4vNX9Z6YLWbugql9EOwg0CtCGMwuC0ct0lTji1TIAG9cR6OK3nR3AL6gyRZbMeyL8UlWv-QNBWMbzlK8Ml1YOiV0fyx6ndmW3DaqQKLCL23sRSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=nSMMnfrfte8-Cj0rqsOb8HA9wwjakGqgwuuHFMTwj9V_iTcanqJQ9vQRnD_f0eVtQMzGDbY07ml7ld3LhAJpbLlxtYV0oxX90r_tFNuskUuqnIRuj03cUf0Q7Et4etlCjzKUZ5tskP-r3UhXEZ9vLzL2uy0m-YDdI6JRLCjUGUCDr0VspmNKcUE4Q_Gcl9UEGc6uPilwz7-3P_oqSG8dNNoLqJQ2afHM1S7in3E4vNX9Z6YLWbugql9EOwg0CtCGMwuC0ct0lTji1TIAG9cR6OK3nR3AL6gyRZbMeyL8UlWv-QNBWMbzlK8Ml1YOiV0fyx6ndmW3DaqQKLCL23sRSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M3_kaKzGif9QzaL_bmv0s_smSHnvw89hYxV4z1FhRQbhii9jMIg2-hY4wsiISkvkYetQ0q5QxaEvi_QYhzRsvAWyemovkL9o3jUDYoFUNIoMR9o9PJY7xWkRnSjd_egK4NBVzjH-Nm3YTfBZjJos-hH0Fler7kuloQotTOzqjAROXaNCuseY5Yw59gwYGMuQEisoczAkmn-gZXyl9CJuSIzKuVNHm85mJsw1gsrkdoKArYpmWOjjwlxl_B94huv9FYBmdOo-PUElDKE6HTIp68G8EqlBg2hMjxJFlX3WnTCVCVqbG2j28yyaSvqk8dE4YUNNYOUSulMT9aYA1mdj-g.jpg" alt="photo" loading="lazy"/></div>
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
