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
<img src="https://cdn4.telesco.pe/file/DM4J-7KKmtvgmgL0Z6HKxyCJohe2UynowhQJpMw_MPnxqAe9oBbtEr_5MLCvkMvMzmC8WvID3-MKtN9EbfqsLvOUBVWgni_prH9FpX1KHLSZBINSAid4iOEuieBV_QXz5vLqRUx8ujdpxNkBI9ft-wWzfCqPvsFV8-m6h_bYxkEmXx6Kg2kNuOo_NrpyObRTq4wljlAANYfiXGLhrbesh61DHi4EXpzE-s_loASzmcQ8gKTyWd66Myjq4_u-erIimqjyVaUHlkk1S7jCSwVMyWZDs-w4evizlOtzZjJ-LhyCBdQXuaKdSk65enxbaIUaclE7lQJzKBFP0aqJZyCjrA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.1K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-28 05:53:03</div>
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
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lPw2iJuW7gmTf02_jjn0QvQLP-XX9lG40BVZVlX111CeZIJI8lULEZCsKTJUeGoEnXuhmNZw2CGrRD07f2AkRg5Cu_PK26cDPOzseDisGAtW7-DxLGV_rH7ukSpEp0UfqQLShgWCGo8nFL9vP3XBJV9PTcHNKKUkVNYYFU8fWrvVat1gbTxaBlLnDHZ7kjz5_p0N4_kOeTzYCpAV_gn77aBQ02oetT_-xN4N6bg-IDdWmv5n1XTLpe4xsNSm_Q-Wxv_MwfCwJ3NIRRmRY6KP7j2MqA8ijnXwFz4gBJl7kW7Scr8MllwvJdJDv3p6skuOYiuPygq3_mi4VKU8_DSeXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6745" target="_blank">📅 13:24 · 25 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eAMJfb2Kb9XJGVLFOfwcZoPy9B6HW5Om2Khz2IiVk_iXaxst_nd2ATsYZc1RNNTx9P2NExDZ6ht_0HO80ctvmoMl8gHbEo19bxSvOJfUW0cvB9Z2zEUd9GtwwEnnAoKR5X02koEgI8D5bWdvl-flCEZH10B_LRE9MuBKN7Le7Fa2cobxMWr5NVLdOVy4Maf58xpA7zRRHLN0YlG6HMZfSpnovugQvRSAoS8KREUch98d-OHQbFwU7GsETWvSGCU_CDqTfSXtB92v1TvRV-jsH2VJt8aHhuyhnoy8bwnMCEV94Qfh-Ia94kfapUd6npZn_v-Q1hd-wpMCxCAwioUIlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LrlZByQJ1ygqI5Ir_5cyoWJ7ZnBE8hh4WSOrg_Njy5nGgI64p_VVz2qa1wK52B5KM4JY8BTyuxx30WQmkB2O8j5BblqmEKhQ_2ZtDVwcVyj87IDC5smdvUtXdUvv0u7ZivCHFEM7crgzDu8VBFo0rvrnBmeYi1zn13_xD5y1-oKFjdlg7cZ71j3nBY1JB45kf4cEXhM_TKgmIdBu2rKEq3O4Yoqff3PM_w6Mxub878As7BsFbDGExmUuYZ0MON1nSOW6bcnWJ88_ec9AiymoqS9l6vWBqIWAf3s6wFBnHKUee1JdSh9gt6HdrOZa4xZQGWq_h-miEvEg47tfwg-b3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRKDtUeMfKoWdWlkHgd7bdQqsw6GjiZfDA1gHrR18ESoyCKLgfUdZ74nMzXbfkoa8haNbju9lalHDMHof1GSxGDStJpcVxIqyHFlt8LQJHBXiHebnNxQVEGlK8R4a8SSd7R1ZFHlV01SIiC1hQ-irpFCPBkbfVk62kns0z8QPoZfG6Y4j88BpfCvuBxVlaxPP-B6mOLkJs_uU3c-Q-7aZw43nrAmtAn6gt4WulMaDdt6eYm9V73kJDbqGRyREbXdNeFvx1lZwa-faqiZudFvt9ruBnmtSwcNzvQ_iXF9njeMgj7L84fnXszxjK7uhcSAlgJ1qkeNxQ44SyRPFKpTtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdCZkXWmAK-z-SCDarSmag5q-GnQW0tlVyecvNhue25Q0HCfaDbvpJD32j8xnP1m2Vv_PBgt0kqfcRbStoPwSOLMhmXAiSIRHGIhVTAaB10IYl7YmAIWjywrAweASsEYfwJjMb7jarYyS95GCSXafLfiHY9bNAmNH18aHUqlg1xmDGOWWHmvdwfxDv1ZkmS9VgC94F5n3vPme0BXiMnJjntyc7eKmM5hPqyHOGkUrAT3G_0WQH2c4K8vq7rAF6TUuROi03iL413UgXO9PxXQTku4HVogGQNIyTeh9BaJHY3X3-Bqw8roN0Z7rFKO3VtkelViTJPfUET0v9rsg8zxXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/olm5am24RRfGfPsdyO1rE8rQ_118hU05zihiYJRbQiScj8SUIbev1wqpWMF2Xrsu2zdN21cfJ-wVtYnqgDneewcd16qJ9FTHp5hjFGncRx8FyvYOz71XSrT11uxjE8o8EpS3cb3iZ9cSUhugi8WgdZH2gbNg40OCa4kFeE7tX5kQRFpplQOQAf5NMDO8T1PpfsHEBZWPi_DAM-50-vSRoSWCnc23kcSi96R9M1E2R7YwnHDmpPrRw5a7f8QAhSzPjdZf7BsCaAVSxYFVxFLCDR3c6-hSEi54KEvLfeQReO9jrImKxFPuP8bVOT0alPyt3H_wv_MKLwhvUdMn46pMuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VdKr-RXzxRsNaALVmuMwyQDWLnx-ouEBCzKFVpHLEfREF-KdT5Hm70XIdqVIyLdmkjthkpkhCJuJ4yxZHNv9v7FS762K4xXVEYxvAnfXCLQhn0cSm9qlMCvWpJjOsLql4XJhqkxbaOy8JlR1nLd17Z5-ZgIRb3PR44bjfmaGd3HDQAm8AQ_pgAvYDJFawE3P4zyEy6XKUUkNgTaX7LtEQrzL7igWg3bOTOxe-22e1hE5onM66Xwq7WPbLwvx2wy2cX87GtvoTDZXd7DTQucKK_a3uGJwpCRwjwWX9ulYV7_AN2HAakvzj0cE0Gz6GmeSigKND35T07oO0dclFpFM3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=XVrRH4ZFQ0ilv-88zHHJFXufJh3JTT-ni5ecBm2q40Qfm-Nj0r-lZJNUxi3H4546Pb9-AME3aNR8w2l58FupL2fZ058f0faX55qVAEHQrROXy8iOnfiJ5e1E4Vssn5HCcg5jCjFXnaWsvV9PQcow6pgJCej2VvR7DCEUrtLanqE25ncqj-mfd2NyyDJcXg8Y6XsZzN1EWzAeNjJ-AbOjAcfCdYkqjVhQJ-9LbsXIEIwjMUza1EAAFeX2GPQKxNur5YOtfERIiyHA-t0ldt2-7txeglr8_FDCC1QISonBriOnriIuFX3ZHgXTAeewxaLglnUW8qmUwqRvoU_HobyBmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=XVrRH4ZFQ0ilv-88zHHJFXufJh3JTT-ni5ecBm2q40Qfm-Nj0r-lZJNUxi3H4546Pb9-AME3aNR8w2l58FupL2fZ058f0faX55qVAEHQrROXy8iOnfiJ5e1E4Vssn5HCcg5jCjFXnaWsvV9PQcow6pgJCej2VvR7DCEUrtLanqE25ncqj-mfd2NyyDJcXg8Y6XsZzN1EWzAeNjJ-AbOjAcfCdYkqjVhQJ-9LbsXIEIwjMUza1EAAFeX2GPQKxNur5YOtfERIiyHA-t0ldt2-7txeglr8_FDCC1QISonBriOnriIuFX3ZHgXTAeewxaLglnUW8qmUwqRvoU_HobyBmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شدت انفجارها رو ببینید
بخشی اش موشک‌ها و سلاح‌هایی است
که درون تونل‌های این تپه بودند.
این دژی که تصور می‌کردند شکست ناپذیره از درون نابود شد.
پول‌ها و سرمایه‌های ملت ایرانه
که دود میشن و به هوا میرن</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6726" target="_blank">📅 09:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6725">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=eNNiLWu8EQCXPJp0LCnyU9bi1jnRAQjCIootewCodjVqCPoT3E10Vc7CQmV3FgWqa44n1ChNVmBN8LRa_7XB7ABlPG6OfHg0ATv0oCnLdgKRSUK4wwItIkRvRqNSEp83hvjc-776RTV0_InaUxC6B1gbFeALdqLXPTj0XFZGvygMPYuoYCnG3TIXPCoQf0_3jjbDVqg3yKnGZGJR8he8yTrVSlcnbEapsBxxw2ZNbL9vMjP8GTgDjysBCFDB9N52VkRhjg2SZAqohwH7isKIfxYQQ8Xd2vF9BVFEmhKywr7RumGWfXuB0hOCEnRPhB1BhXjdBJexDcx71XbjHo-XCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=eNNiLWu8EQCXPJp0LCnyU9bi1jnRAQjCIootewCodjVqCPoT3E10Vc7CQmV3FgWqa44n1ChNVmBN8LRa_7XB7ABlPG6OfHg0ATv0oCnLdgKRSUK4wwItIkRvRqNSEp83hvjc-776RTV0_InaUxC6B1gbFeALdqLXPTj0XFZGvygMPYuoYCnG3TIXPCoQf0_3jjbDVqg3yKnGZGJR8he8yTrVSlcnbEapsBxxw2ZNbL9vMjP8GTgDjysBCFDB9N52VkRhjg2SZAqohwH7isKIfxYQQ8Xd2vF9BVFEmhKywr7RumGWfXuB0hOCEnRPhB1BhXjdBJexDcx71XbjHo-XCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی به «علی الطاهر» میگفت «مینی پنتاگون» پنتاگون کوچک. با هزینه میلیارد  دلاری، با صرف ۱۸ سال زمان، شبکه‌ای از تونل‌ها در درون این تپه ساخته بود،  مرکز فرماندهی، انبار تسلیحاتی، محلی برای حمله به اسرائیل و…..
اسرائیل دو سه ماه محاصره‌اش کرد و اجازه نداد آب و غذا به اونجا برسه،
سه هفته پیش جمهوری اسلامی
به آمریکا پیام داده بود که اگر دست
به علی طاهر بزنید، جنگ برپا میشه و…..
اسرائیل در یک شب، پس از شناسایی ورودی تونل‌ها، ورودی تونل‌ها رو نابود کرد و تبدیلش کرد به یک «تله» برای سازندگانش.
جمهوری اسلامی تنگه رو هم بست و خودش در داخل تله اش افتاد!</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6725" target="_blank">📅 09:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6724">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=V7s-dfyW2zNA6D5-G1z-SmqHri8naAWgtKnUMLRpe1RPHZbJSB0cODLenju7h5MzOnHXk10HhWA23824AIuwgnuZpNV0gJ7jxiggeVKr_tNLYj6N7JJPKfaUO4vL5KRh5rwBjD-1F0JaHfOZRCf9wFZz_Cxx7HEDFxAf87GgNQRXROM6RgQoqJBO-Hl5Lur9AwsHEoj4WOCwTD51tay0FD4RQtU3K5T2jI79RlrhnBas02oN5bSo4Y_R0Rywl-I6BW4BEmEeNJuGTgl91tCHTcU4en0peihwgSRDBg4_4Q1o5PHGzrCpP2fuy41VNoRmf0CAe_SzQZ_DA4r7cfcurQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=V7s-dfyW2zNA6D5-G1z-SmqHri8naAWgtKnUMLRpe1RPHZbJSB0cODLenju7h5MzOnHXk10HhWA23824AIuwgnuZpNV0gJ7jxiggeVKr_tNLYj6N7JJPKfaUO4vL5KRh5rwBjD-1F0JaHfOZRCf9wFZz_Cxx7HEDFxAf87GgNQRXROM6RgQoqJBO-Hl5Lur9AwsHEoj4WOCwTD51tay0FD4RQtU3K5T2jI79RlrhnBas02oN5bSo4Y_R0Rywl-I6BW4BEmEeNJuGTgl91tCHTcU4en0peihwgSRDBg4_4Q1o5PHGzrCpP2fuy41VNoRmf0CAe_SzQZ_DA4r7cfcurQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=vSIgtmoRrdbiOnvD_VF4KOfmSRNrCekIKpG04cKS98knp2YSeHXcWht4bAOEOBueZ7hxdWLXksyYKJxZk-4JdJf-mFzl5v6_RgmyRT9Zvg3t2ZKqAg6vAJg5ScRgN-sc6N3Qet10C-dTZPg_yVeh3UWV0bSSCRVMQPtcSL-ZSe2KVj_NIYxgQxewmvFs890T2BDB8E1Q7QYkWCZ6Zvk1Y3A65234wLRgDBPymZKstUKjBVwXHzUCvhxeyAffXQKWxFS2lm8rxebcfI8kGYAf1KMdK1ykbowPbbHsJxtVGNMpumO3UlS6zhzRiu3P0iK3rzQEbHZpbrPCu5HjEfbsrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=vSIgtmoRrdbiOnvD_VF4KOfmSRNrCekIKpG04cKS98knp2YSeHXcWht4bAOEOBueZ7hxdWLXksyYKJxZk-4JdJf-mFzl5v6_RgmyRT9Zvg3t2ZKqAg6vAJg5ScRgN-sc6N3Qet10C-dTZPg_yVeh3UWV0bSSCRVMQPtcSL-ZSe2KVj_NIYxgQxewmvFs890T2BDB8E1Q7QYkWCZ6Zvk1Y3A65234wLRgDBPymZKstUKjBVwXHzUCvhxeyAffXQKWxFS2lm8rxebcfI8kGYAf1KMdK1ykbowPbbHsJxtVGNMpumO3UlS6zhzRiu3P0iK3rzQEbHZpbrPCu5HjEfbsrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=PnxmDQvw_d_NeflYE798mk4-uYJwuu_3R95O2A51fQIOyInsirlHbSt95aYgt7hRBe1tUCY64dlQkhVRREw1-2wYpYgrrVxmKyjGivBV9qdEgjpLuogQEVTs72nG3Kj0EJI27P584LsQVQsfypePholfSv6QQ8fyAaejwFV0AHchNMKBXzNpz6N1STF__SfqMvxRgY1bVkUUzEKBumMJZtuFJXiNTDLBEibYCSKJ6RWcEIU83ZzTvIeTGP5zWeB3XFISMz3HwmLeTDtG650nE-4tJ8mZE1lo9ZUqPwYDdh4k1fjf5X6ciLu84C3AYcP2VVURTFs7rO536xRCMrVzDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=PnxmDQvw_d_NeflYE798mk4-uYJwuu_3R95O2A51fQIOyInsirlHbSt95aYgt7hRBe1tUCY64dlQkhVRREw1-2wYpYgrrVxmKyjGivBV9qdEgjpLuogQEVTs72nG3Kj0EJI27P584LsQVQsfypePholfSv6QQ8fyAaejwFV0AHchNMKBXzNpz6N1STF__SfqMvxRgY1bVkUUzEKBumMJZtuFJXiNTDLBEibYCSKJ6RWcEIU83ZzTvIeTGP5zWeB3XFISMz3HwmLeTDtG650nE-4tJ8mZE1lo9ZUqPwYDdh4k1fjf5X6ciLu84C3AYcP2VVURTFs7rO536xRCMrVzDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=Qqg0WKlrGkS8Ed-ub14a7aMnnG11DW2IXkd_1gU2U2AInDJ5mGRPEIoY1lYyrgwiRQBmN6gUIAlu2u7Mg5SrVOe5lZMurJbnUzfg2X8J-xD9KDdgSmFa7_SCyA9obrAuTkm0uAYohqJgZ7ZGobqUcIZ9F_GXTRqrNAQqGahrP3HxJ4XJO1IdBPX3Grlu4uGz3_x1U8RH9jFuxRworo2b9usItnYhdAWtPyhLda9GJWSlCMV4UxQQZXMq1oNVj7zAFMliOzIEwhlKE-eSC-1w_W5M-ybX0ztdiOs9xM77YpGXDl5gkcKfjKPYCoBlTXkAQ-D83CVfSz7iZLlGeQCwEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=Qqg0WKlrGkS8Ed-ub14a7aMnnG11DW2IXkd_1gU2U2AInDJ5mGRPEIoY1lYyrgwiRQBmN6gUIAlu2u7Mg5SrVOe5lZMurJbnUzfg2X8J-xD9KDdgSmFa7_SCyA9obrAuTkm0uAYohqJgZ7ZGobqUcIZ9F_GXTRqrNAQqGahrP3HxJ4XJO1IdBPX3Grlu4uGz3_x1U8RH9jFuxRworo2b9usItnYhdAWtPyhLda9GJWSlCMV4UxQQZXMq1oNVj7zAFMliOzIEwhlKE-eSC-1w_W5M-ybX0ztdiOs9xM77YpGXDl5gkcKfjKPYCoBlTXkAQ-D83CVfSz7iZLlGeQCwEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه کسانی که دنبال بهانه‌ای هستن
برای پناه گرفتن در آغوش امن و گرم آخوند و توجیه حفظ قدرت در دست این‌ها.
این مفنگی، پدر زن مجتبی خامنه‌ای،
میگه «فعلا به خاطر شرایط جنگ
با حجاب کاری نداریم»!</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=Ko9fiAawIuxt5F_ZMzg6JbwbSxbkfCWOWJhfB9P0iiNYuIyAdNJRXc-4uhBeF5tuqzqwlrkF-UhstWCTvVi492VfGLhvG0d_cx9Xl30tnMEmnPvvmO0OgmMWgUHYSfsgphihTrbjEkwm06GaiWkeEplKiP5B5IUvNrjFdHU1XSGKi1LDveYVjvXjY6XpByDzwVfoh2kmte0Ayr8res_TKfTpYvFgx087j5snwNUKZ0LEFs8uoV8TQIwg9cBQXcGhAanybOLqAzT2hkJvr0UhCPmJrf1NvKH1VKZ_EQD3rBE5fQTcqFDNysMtE2b8tj1eD6jyI3224Qi4usEHaemxIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=Ko9fiAawIuxt5F_ZMzg6JbwbSxbkfCWOWJhfB9P0iiNYuIyAdNJRXc-4uhBeF5tuqzqwlrkF-UhstWCTvVi492VfGLhvG0d_cx9Xl30tnMEmnPvvmO0OgmMWgUHYSfsgphihTrbjEkwm06GaiWkeEplKiP5B5IUvNrjFdHU1XSGKi1LDveYVjvXjY6XpByDzwVfoh2kmte0Ayr8res_TKfTpYvFgx087j5snwNUKZ0LEFs8uoV8TQIwg9cBQXcGhAanybOLqAzT2hkJvr0UhCPmJrf1NvKH1VKZ_EQD3rBE5fQTcqFDNysMtE2b8tj1eD6jyI3224Qi4usEHaemxIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hJtSYYXBURU1tkhNWFruisNz9qeyKrtZjTBe4cb44mzeOyQXolQWJTe4As5tCKnVQyeCOiaj76kMd2sUUGM5wIyETzN5ApjPHOzbRr-UwvQ3lBXMYmFWP7RUUVDGi_w4bNwfBH6PMHgmfTWzHMTedJjWCSSEDF62-hYiJWn6MRuAUGToT7GHxpj_JIsowhaOoHBEzvZ1NbjBiauc-59Tr4rbWkeoEU6ShkcQOaFh7yiQqzhv5X4n68FP8D4uEYWalsDq6XXEz9t8JCqPfTFkVEHJRvLrug-ECs5KdZWa053l-sdFadLyitBm4vmkiRkvqUSuRQedysvDcLjR2BTMTw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=kIUekd2s3ME76IH_rnW_ioPDyr_hlrQXqmz8mV0OBvuVLMyU9pRPO-QIIVuElY3xKXqVIse8o5xTr9wy5-iXxfiSjPWGXHtU90f1BtPxURiWRc9eNi8f5pLJXGHajXRz_Praz69Qz9tMa6-K_kYJ5ZHpfL0x7ZuN_ct1WQz7931eYd3XMERLtIy0-dzZkJ69z_28mAG2qmGII3lWNo2yk7ZV1g1B33gX3ezp7jlK26VMER2snJyC7EuRbrBm3UsNsL1kZUPjeoqNQItDPivaraTD61wX_KTZki99ZlqOEcGt-S6YCz1zs6D7Lb41cs5L3xSa40qfTmvKH95mxTQs6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=kIUekd2s3ME76IH_rnW_ioPDyr_hlrQXqmz8mV0OBvuVLMyU9pRPO-QIIVuElY3xKXqVIse8o5xTr9wy5-iXxfiSjPWGXHtU90f1BtPxURiWRc9eNi8f5pLJXGHajXRz_Praz69Qz9tMa6-K_kYJ5ZHpfL0x7ZuN_ct1WQz7931eYd3XMERLtIy0-dzZkJ69z_28mAG2qmGII3lWNo2yk7ZV1g1B33gX3ezp7jlK26VMER2snJyC7EuRbrBm3UsNsL1kZUPjeoqNQItDPivaraTD61wX_KTZki99ZlqOEcGt-S6YCz1zs6D7Lb41cs5L3xSa40qfTmvKH95mxTQs6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=EIigNolV4bBdwobgEuAJXrEfEaoA5MaAMsdX_XQNhkW6n26j8N-xZJYPkNw8dXN-WMM8GZsH7_vjVvWsf8_8TMhjfZSvReMudKnzw4NEKCzpjpHqNDwaZIpTsZ1IffAF1A55PIUsfwIxjuPQ8DVbvZUJYSOiEDJRtvRl69bG80fXjKmht6Gv9x1OTBV56mfdfUdpgLN5HjH3gWHdk8PUDhI98SvwSH1aXyAOYnfluFtDkhwjf_N1SDOjRmc3EmeKSQgKNQc6hiSYKQI_BcWVC3nK0jsA6tnkGql-29senW1R28LQwLr-ahbqmEYbYsMPDfCBlRi9yBWLDsmceOUL0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=EIigNolV4bBdwobgEuAJXrEfEaoA5MaAMsdX_XQNhkW6n26j8N-xZJYPkNw8dXN-WMM8GZsH7_vjVvWsf8_8TMhjfZSvReMudKnzw4NEKCzpjpHqNDwaZIpTsZ1IffAF1A55PIUsfwIxjuPQ8DVbvZUJYSOiEDJRtvRl69bG80fXjKmht6Gv9x1OTBV56mfdfUdpgLN5HjH3gWHdk8PUDhI98SvwSH1aXyAOYnfluFtDkhwjf_N1SDOjRmc3EmeKSQgKNQc6hiSYKQI_BcWVC3nK0jsA6tnkGql-29senW1R28LQwLr-ahbqmEYbYsMPDfCBlRi9yBWLDsmceOUL0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=lkJ-KMeT5V8bRffvod0ETe7SM0f9_mKDunY8MEr4O_WfApPk0kZfIWyTZgVV7qqMLygu1m1CbiXIDmp1Jpw_NB0JZy4muL2V374oP7smBMuAmuZ8tEQy02uqNn63xbjtUSasvZFCkz7AZYr00Ulc1HG7OMYWd1ouRGTKeBevnMqVeA7HFPWZY2XClNMGNqI1mDOyCvn6mbLsg-jBXYTGtrPePaqd2vO7sMM-vhAIOtDwSjPcBDgYKsR6a77fIeeFEJA3lJTKg5_6ccTqk8-K-AneVdwHelytsXH21f0kPz6FLhEviekwBxaVHUAD9V-dvBa8r5mZwl5PQa7BqDzkhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=lkJ-KMeT5V8bRffvod0ETe7SM0f9_mKDunY8MEr4O_WfApPk0kZfIWyTZgVV7qqMLygu1m1CbiXIDmp1Jpw_NB0JZy4muL2V374oP7smBMuAmuZ8tEQy02uqNn63xbjtUSasvZFCkz7AZYr00Ulc1HG7OMYWd1ouRGTKeBevnMqVeA7HFPWZY2XClNMGNqI1mDOyCvn6mbLsg-jBXYTGtrPePaqd2vO7sMM-vhAIOtDwSjPcBDgYKsR6a77fIeeFEJA3lJTKg5_6ccTqk8-K-AneVdwHelytsXH21f0kPz6FLhEviekwBxaVHUAD9V-dvBa8r5mZwl5PQa7BqDzkhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=VRRtvkJuU4tHSTULiF0L7sVWpXipafqnWWr78qBX3yuPw4Ufvj6Rctol8L2B5v7gA8aiKLFcKvZ2VwyK4OwzPoJvkrKax77HpUSG2K_48pn0nM9Zcq3Z0gweDHW1NuSfeRzflH41Oq7fGV5_cvocGJ7KNlmNpvr7TB7m-k_tC82ll0c_4ETpmuFFn3v5lYdhZXaKIbJ2x_lQbOcoQkKu9C7ytNLVF4Ky-3-NuQijfEkHmNF8B-mY7bin9d9Jc_WRZP4uGCHuZ3B6S2WpeFLuEqeX7uhan9360KSYILQw_XxhQHsh4S_BIpOEeniBWfs41rroNiZcCatjTal8nDLwTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=VRRtvkJuU4tHSTULiF0L7sVWpXipafqnWWr78qBX3yuPw4Ufvj6Rctol8L2B5v7gA8aiKLFcKvZ2VwyK4OwzPoJvkrKax77HpUSG2K_48pn0nM9Zcq3Z0gweDHW1NuSfeRzflH41Oq7fGV5_cvocGJ7KNlmNpvr7TB7m-k_tC82ll0c_4ETpmuFFn3v5lYdhZXaKIbJ2x_lQbOcoQkKu9C7ytNLVF4Ky-3-NuQijfEkHmNF8B-mY7bin9d9Jc_WRZP4uGCHuZ3B6S2WpeFLuEqeX7uhan9360KSYILQw_XxhQHsh4S_BIpOEeniBWfs41rroNiZcCatjTal8nDLwTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kIdP4W8NhnjxZJIbiwUS1K93ioWpg2ENI8vTMoCnBE7NaYJpRVLpY8bklgxV0PH1gjSxfvw3HNllj4s-9H-8Lo8t9rNyksvSDujNCRQkKtXBuKnI0dD0UEfRI8o3iFoQ6OMC7sFblTkpqY79Rkiguj9gZ8HxxcMZ9P7M0ReSojveobXHlsxIUCtAsFRQahEo3w3mJlmR4ffOzCod0q1ouQf-liFgo-X55Eev22XGF6g2e3Et0Dy46LBw3Qi6nWXxnHRg9vQ7WY0giXPZcUKUQF07oYvZVJJOZQEVuicuIv3YB6Rvfi-K57o8bQfnYJM5cZHU-cxz2NrDcuMurGeHYQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=HbrJfE3XxOVAASKO0_i_5usXPRiXiaGzxkEuIQ0iH5bW5SWYmdH0BOYy2MOTNZarCAT2r4folmepaKe3Cke3Kf-TFPzFpPa_kkt3fnUgxsnleRydkHrC_4ZF3f59p7W0gVXXUpkb7TAZMR0WZBCliYPKB7NfB7HnsnooselSn8SBLu0FrK9Vjyj3VYeeKVSNSQmDoaJbxP7B4JbzL3_fiD2ZrqSrP0SwuQRT_SnAbvE-QLyrYiO_HxDB_q5mud5JgpLWBnbOgZp5dZF6RvlNJZMNZK4MSfTXxM0n6P1Yspt6h92xYm1IS4QMsIzsI6znjr6Y5KYEPPmL03dNEC9MU4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=HbrJfE3XxOVAASKO0_i_5usXPRiXiaGzxkEuIQ0iH5bW5SWYmdH0BOYy2MOTNZarCAT2r4folmepaKe3Cke3Kf-TFPzFpPa_kkt3fnUgxsnleRydkHrC_4ZF3f59p7W0gVXXUpkb7TAZMR0WZBCliYPKB7NfB7HnsnooselSn8SBLu0FrK9Vjyj3VYeeKVSNSQmDoaJbxP7B4JbzL3_fiD2ZrqSrP0SwuQRT_SnAbvE-QLyrYiO_HxDB_q5mud5JgpLWBnbOgZp5dZF6RvlNJZMNZK4MSfTXxM0n6P1Yspt6h92xYm1IS4QMsIzsI6znjr6Y5KYEPPmL03dNEC9MU4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=jLSEfmvhG2ZQV_hvwueC_ruq9UeH0NQY4nH08JpJfatgMBbNAV1fd9FgE7giiTl8cvWUbLNqxlHY0Uq0w3jOZb2J_qyL_c7gMaFUwLYRfO0vsK1vBiQLUjuDyqNJDUwRM1TJWlBrIsjlzdxHdHdw86VXr3a6C4bgDSaMIlBP580pAUyvv1kI2wKxy8QF9sTXS4dSjS_iuZLcJiyEr_tz2igCXFemVc0gMyPIVb5TboAaM5BljxoHqhdOmc6zrfKT_MiTnrOJBmEl0zVNzGpOIDaPSon2n6gh_PpgByuGjksEX_W62p-i_MGPPskWoytqk5qi6ZS3Xti-Yiw9Nlzx6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=jLSEfmvhG2ZQV_hvwueC_ruq9UeH0NQY4nH08JpJfatgMBbNAV1fd9FgE7giiTl8cvWUbLNqxlHY0Uq0w3jOZb2J_qyL_c7gMaFUwLYRfO0vsK1vBiQLUjuDyqNJDUwRM1TJWlBrIsjlzdxHdHdw86VXr3a6C4bgDSaMIlBP580pAUyvv1kI2wKxy8QF9sTXS4dSjS_iuZLcJiyEr_tz2igCXFemVc0gMyPIVb5TboAaM5BljxoHqhdOmc6zrfKT_MiTnrOJBmEl0zVNzGpOIDaPSon2n6gh_PpgByuGjksEX_W62p-i_MGPPskWoytqk5qi6ZS3Xti-Yiw9Nlzx6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i7qLkRk5vF6rs6qDhyZV86ntXNNzMTU9VXO7xsYlmJnL1lmyUSndidEfd076zH7qV5Zg-Cp9Qy8gyvoPCfHSmsfvhd0Aj-bx_RpoWJH4nZ5u4aacKUvCmHs403l1w23dc8Yi1Qx_5SXEgQI5fgglzB_OgD02GmKgkHRsr_L0lU5dqcoSbAEqb0vjO87tAMO4jFh3PSL-OQZzd6RK_7b8ogpU8Xn9Eo41AIFPRUjq7EFD5LVyIZy7J-KRvwqThbNnLETcwv6w3Hy04_1a1pbBQeI7FE9tkt3iA7CH-pey4s3hBAhYwKTuGfpHmhuchs0ayub4Dq3Q3HsRXupd1FIhRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n3exiFX0kxy3o1DI3myJmkQLKMMB5LVGMw8MlhcVWV9OuWwvOurdouNnGcwpch4e9Dj4XEx8yx4jwWlU5214FVZ1bdvFqayvg7Bm29B199OtPRfBjNN5Y85Xzn79OAfGjBNUwQWqOdqlTPkPwYfmMohDE2WC621sgBpv2jOv50eHCUdmbjikYhJu5Xggh9MLUAGYEwTuc-0xi41_oi8Bdyti0DSFukV7HEjh3gklEtqI19GjcodCVQat6RXPAtw3-NYXFW2U-1rhdo4bRARxIJa4tDZMhf5NplcKYu5hdufXBZ8BvVmK4OMi6M_g4f9tVNoQdocLjc-9Vz4w9_LJVA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=ONg-Zu04Pubxbm21LjoPl4qWjHkBHREwmu1KpB0--c2r6R6GsegywgKqMCcJ_4aMsB8-siupxTfoEGATx1CPo7_BLY2rhbcL6euwqeNgn6wWfda-LmT4lulvaeHqak5d595YSFFdT1fgyp-yLWLT3Xmzqs1a1XJhvqcGOUJ2f3szkYtllG23TdaA1wvKM7HsBT6G3C1Zh1vAzK4GQrTkFGi0kOBubWtjtIg3qpTnBqQA9n6rtTaBGXjVFp1VcJk3GTZ4WToHpodDBP97W3jTIU1D8K5a3PW1NQUDdqptKWHXuF0JLB_omRYdQum0xpXAG8Fpo44b4j_FCDHg2hP0lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=ONg-Zu04Pubxbm21LjoPl4qWjHkBHREwmu1KpB0--c2r6R6GsegywgKqMCcJ_4aMsB8-siupxTfoEGATx1CPo7_BLY2rhbcL6euwqeNgn6wWfda-LmT4lulvaeHqak5d595YSFFdT1fgyp-yLWLT3Xmzqs1a1XJhvqcGOUJ2f3szkYtllG23TdaA1wvKM7HsBT6G3C1Zh1vAzK4GQrTkFGi0kOBubWtjtIg3qpTnBqQA9n6rtTaBGXjVFp1VcJk3GTZ4WToHpodDBP97W3jTIU1D8K5a3PW1NQUDdqptKWHXuF0JLB_omRYdQum0xpXAG8Fpo44b4j_FCDHg2hP0lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ARDBfqI7FeLDOtZG-lNEcPOoXDLaGZI7DQovXN6t9P2HXh1AXh7DRVJNMgxcJimUFxJ1Tc7Btx4xKg2tNsbavJf-wOFHZGaGjWbfdc7zNs-FfVKq-anY7mlItGYUFX42mJ9ZSkoldNeHYiE_jqXK3DZZ9VPH7gTXigxJtj5sMowkjDR0Cmd1u-LVK3emIV2YCU46wh3Tui2UNcjTjPtPSBSvpNOvh6hPlE3YooAtx2o8hc4yYUmRI83YSSnDjoe3xVIPNUz82JTNls4q7DCoGomxJLCXkUE_mKucf4ys_ZxgRlGoQ8KjVch7-Td6pzTvUo88rupeYUwrGVlz0OVtvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iF7res6J9wN8W6a5OzE7c09jCB1c331XW2YKDH6N4yyLhqLdEVjyywWyzRtsySVNenA9DpmCRIZM2RphaaN0lN-lnkYqQQN6ZXGJDD9OX_wP7YCgCcemUcdf7uRU2MPvQXlJEc0NP8_WdgTzT0Vr557scPcWgEyshJ38W3ot2caTwBIwFgRUdlPi8Hb0UmLOmK5EdvxAQGhSQO5eF2nR5VeYPwcggmtNeAZteKhVRwjChidNqPJSttp7CtD1oRZZykjojt6jGm4Oth6bAIX4q8hvgd7ObI0kX2qrc9P95rKMcf0jDdGaMaabDdjr6A6OflJbkcgd3EXqnWJO81CHIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNY19SwcWPQNWiEBHNZyVsecY1mHVPymbIrkKS5GN3q1d_HSM2zy8mQ-bkaKpXJzmUI8MKOA4VFI2L1pNybEwY1pfN7Ae1Tt0j1YTgksCyOoM5bJ6EknN43qjhKxzSbNlTxbN14gzH-v7aUatQz3ur_WOVI2gHWGMmt-P2IZU6iMoRtijwtjtKksnn8iCWIaVZKbBqmY2NqoGvg2lwGQ5AAJtSMNp0yHabHFL2MLNGYZX72OnmZmziDAAW-djzeecA5Wj-CXKJCg4c94ZEGK0VAzZHzRidxlfnALZ3V8FXMtMP3am_MxoQglrOHkqACZJaZrQ9YyZ-KxdYH0LcFRRw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=YO8NbVr5r5xJJaumB-lphn9kSAhmDYNFBXvaco7i3MgJrYweHJSTptj52nj3tpMk8XedTKOAhN5-f-O0Of72CWicgmETENoPQwGiipb-ugHCMvKAifPhQpiwzOIB7U9sH2BGpFUuGOeJ34HHegRfWaz5QmTDGOnYI-Zhd-AQlMPpNTZknVGT6wr-hST0u9LTG-apAFakgd0XKdH6dPgQjv0vSFX4OYaR-o39LRNBIJl50AXZT-qtbtd7H68LFxZ5P7c4l8J0cR8UkGOckZv8UNAP0i_GmFxVqI-gHTzqYDaLF2YhrVD4RnbWzlI-6olamN6wY-gaEz0yMHjF_B8plA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=YO8NbVr5r5xJJaumB-lphn9kSAhmDYNFBXvaco7i3MgJrYweHJSTptj52nj3tpMk8XedTKOAhN5-f-O0Of72CWicgmETENoPQwGiipb-ugHCMvKAifPhQpiwzOIB7U9sH2BGpFUuGOeJ34HHegRfWaz5QmTDGOnYI-Zhd-AQlMPpNTZknVGT6wr-hST0u9LTG-apAFakgd0XKdH6dPgQjv0vSFX4OYaR-o39LRNBIJl50AXZT-qtbtd7H68LFxZ5P7c4l8J0cR8UkGOckZv8UNAP0i_GmFxVqI-gHTzqYDaLF2YhrVD4RnbWzlI-6olamN6wY-gaEz0yMHjF_B8plA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=QeiVuYCEHasmXeOll1eyJ65byoNrDzmOFP3MK3OKdSj9I-UCV7w0SZjy2WZpV1Nm8hM8FXxVBmR-BZP1Mg43aI5XmqPDK9RCRaSXeOl1RGUFisX8UZ2Ls_sORzwpy53SXVVTctqTdwPjQ46J5b3XaDqEsw7xjPwXmN8GB_kln3VxYhPQDl_N5gazXZbZgQ-Ta96ludr8FFFUxo88Q-rk8fLhQi9n_q-BExzaWi4CBIp_GUQfSPO7dN0FxkkJJCInZvVPvzWpDLPiaQmjvUp1sG0kkPsdMV7UrFwxE8GyifxzF0G5XcZ6aAUlmS6OxNF2SN2O9LXh8GJMdYSFQha_2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=QeiVuYCEHasmXeOll1eyJ65byoNrDzmOFP3MK3OKdSj9I-UCV7w0SZjy2WZpV1Nm8hM8FXxVBmR-BZP1Mg43aI5XmqPDK9RCRaSXeOl1RGUFisX8UZ2Ls_sORzwpy53SXVVTctqTdwPjQ46J5b3XaDqEsw7xjPwXmN8GB_kln3VxYhPQDl_N5gazXZbZgQ-Ta96ludr8FFFUxo88Q-rk8fLhQi9n_q-BExzaWi4CBIp_GUQfSPO7dN0FxkkJJCInZvVPvzWpDLPiaQmjvUp1sG0kkPsdMV7UrFwxE8GyifxzF0G5XcZ6aAUlmS6OxNF2SN2O9LXh8GJMdYSFQha_2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=i1akRlwhnmeqd-csyE7WpxPbwBFumSd0ZZqz1IWBi-1E3Acz69snstxbQ7qq_bKGspgC-UzLOTIXE2DLDYZVxAkrTSvtPvuy9KrEFsgH5wBvFoceYvESHWzX9EVoXnMijm9bqGQnJGiPcFNzsi1TUlPOdNpfcquwedlOY9jjJVosXTGHogcui8z5g4cLIQ880bgjTmP_kyk0d4-UK-25pPTgvtBgROJF870jB7z__adQATvUSos44gkDHQzJMCucHr8cSmU4uHu6OFr1fIGpec2url4LJyudDsZOEJpgxlM77qPPnxXSXyPnmhWCMf-M7KlOoX2kL1MZW4rGL1l21p26yVccK63muD1aQwTwG_HmA1bVpNc0WRzsgGydqhj0ZWcvvU_o8vJMiw-dyyMzPHJ5-XodPKv2WhaKP3kfzmr5-DDnmtLVn90pDiflyZPCkk7X9D48MVrjF3gvIXpcIB6XUab00sdfEPYCM66FwwyXIN1aGeJ8Ny_63ndihZPrxavglfJ90VUqAP9nrYduDEFzxzVUeCUsMuuqcLnu77Z8cVUooHGOx8ghgyA1SHnDYL1a2ooMQ3cF6m8eI3enqT7awwhAkSnTSYNdRX5syTWagqJilp8owkM0yO_cCIc8jWUB7eKi9vsfUe8n0U_jvgeoQTJq6iXqvAFHzeD5P9I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=i1akRlwhnmeqd-csyE7WpxPbwBFumSd0ZZqz1IWBi-1E3Acz69snstxbQ7qq_bKGspgC-UzLOTIXE2DLDYZVxAkrTSvtPvuy9KrEFsgH5wBvFoceYvESHWzX9EVoXnMijm9bqGQnJGiPcFNzsi1TUlPOdNpfcquwedlOY9jjJVosXTGHogcui8z5g4cLIQ880bgjTmP_kyk0d4-UK-25pPTgvtBgROJF870jB7z__adQATvUSos44gkDHQzJMCucHr8cSmU4uHu6OFr1fIGpec2url4LJyudDsZOEJpgxlM77qPPnxXSXyPnmhWCMf-M7KlOoX2kL1MZW4rGL1l21p26yVccK63muD1aQwTwG_HmA1bVpNc0WRzsgGydqhj0ZWcvvU_o8vJMiw-dyyMzPHJ5-XodPKv2WhaKP3kfzmr5-DDnmtLVn90pDiflyZPCkk7X9D48MVrjF3gvIXpcIB6XUab00sdfEPYCM66FwwyXIN1aGeJ8Ny_63ndihZPrxavglfJ90VUqAP9nrYduDEFzxzVUeCUsMuuqcLnu77Z8cVUooHGOx8ghgyA1SHnDYL1a2ooMQ3cF6m8eI3enqT7awwhAkSnTSYNdRX5syTWagqJilp8owkM0yO_cCIc8jWUB7eKi9vsfUe8n0U_jvgeoQTJq6iXqvAFHzeD5P9I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=l5KNQ53lHk39rNOsVootsnEPgdN_S63ggiNNRl6IZCblKulks-DlffBNfBAWRc5OD5o9taPRv7dTvusW07h1zsSOPwtLZiUGAtFlr_UCGewLE-pr6thXsw4iWpQk5IENGUVdGUgKuIoe6TGsO9xjnyUJcuWQpzIj_TqB7m6z55wvUZpG4156iH2aaKRfOf6iKb4JHstkfveaqxGFnctTU0DO0ZJmVjGMBOEK6YucXd6EC_Nf262KP5IMx2TiMxl-Wg_oRrWi9Hnn-zMqGWUJGF_V1hb7nEUXl_-wgPTLkazBxw1vrs-KUiV2R2u8WBdylZt8pRv2r0gC0uz1iJAMdl6FUm06aj5d07pGybt6OZ7NPqIDISFtZ5ig-5OSR8F2L3HOyBDWEyx0sgS84vP7RhG4iOWYPxeijvb_44b4U3jaANXp6hC9O8deJ0BHA_C0fuVhSqjq1iTmDg-vZ6qWiq4XwHbHl-120u1N5_RVZjwxaHZTCtmKP6nyZa-fAgzvTOjGt5X0sAW2kgr4AhcQ1t9ydlXOHVbSzLOmk1HuiWMRqLzAy8mo21nfpW4DYakFUkZT6njlXWkcLNJn1I1DC4SxO0UFAUuD5mWUqyJyE1uayQ5P19Vga0BKsOjEngd8gRoRAs19B4Vd-P8xFHHJ9MDPq_gHE9-f4UFwpu2KF5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=l5KNQ53lHk39rNOsVootsnEPgdN_S63ggiNNRl6IZCblKulks-DlffBNfBAWRc5OD5o9taPRv7dTvusW07h1zsSOPwtLZiUGAtFlr_UCGewLE-pr6thXsw4iWpQk5IENGUVdGUgKuIoe6TGsO9xjnyUJcuWQpzIj_TqB7m6z55wvUZpG4156iH2aaKRfOf6iKb4JHstkfveaqxGFnctTU0DO0ZJmVjGMBOEK6YucXd6EC_Nf262KP5IMx2TiMxl-Wg_oRrWi9Hnn-zMqGWUJGF_V1hb7nEUXl_-wgPTLkazBxw1vrs-KUiV2R2u8WBdylZt8pRv2r0gC0uz1iJAMdl6FUm06aj5d07pGybt6OZ7NPqIDISFtZ5ig-5OSR8F2L3HOyBDWEyx0sgS84vP7RhG4iOWYPxeijvb_44b4U3jaANXp6hC9O8deJ0BHA_C0fuVhSqjq1iTmDg-vZ6qWiq4XwHbHl-120u1N5_RVZjwxaHZTCtmKP6nyZa-fAgzvTOjGt5X0sAW2kgr4AhcQ1t9ydlXOHVbSzLOmk1HuiWMRqLzAy8mo21nfpW4DYakFUkZT6njlXWkcLNJn1I1DC4SxO0UFAUuD5mWUqyJyE1uayQ5P19Vga0BKsOjEngd8gRoRAs19B4Vd-P8xFHHJ9MDPq_gHE9-f4UFwpu2KF5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=lG3r9Qk642CHvdvokTEB5sIEMymF8s1Goy1kUK_FedP5vXJqAWPNQbZB6BfCJzBJ9tkVGIsSR4WanMPjfuC5INP8A1oo0hEmFSb5TuTGsRi0iykbc_GmqJf2DZUl2idhuDMNu8jpNow49AOBK_g9TsyKoHui1MUCJyaN0kgCpAX4PMcWT0iUIbJhJbSKYcVIk1H-Eygu5LBoBPHW7YZUs2Ywh-p0O8zyz_Aa9Na5TIxtMDoPpn8HkWdlbOXgjdkrI_6oyx5Rq-FXzSR-GF2U48oviFzUCB5PqT0v4j9u7_jGlywtGSmyg5q-9A7l2Cb40M5F6N3WNCvi1dEbK2KZeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=lG3r9Qk642CHvdvokTEB5sIEMymF8s1Goy1kUK_FedP5vXJqAWPNQbZB6BfCJzBJ9tkVGIsSR4WanMPjfuC5INP8A1oo0hEmFSb5TuTGsRi0iykbc_GmqJf2DZUl2idhuDMNu8jpNow49AOBK_g9TsyKoHui1MUCJyaN0kgCpAX4PMcWT0iUIbJhJbSKYcVIk1H-Eygu5LBoBPHW7YZUs2Ywh-p0O8zyz_Aa9Na5TIxtMDoPpn8HkWdlbOXgjdkrI_6oyx5Rq-FXzSR-GF2U48oviFzUCB5PqT0v4j9u7_jGlywtGSmyg5q-9A7l2Cb40M5F6N3WNCvi1dEbK2KZeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mc4aajpeQm1-zM-_TxkYu4l54Lftri5joPeoCImpxQZTfqCVH_oLbJTA1zmkUqOW-7-Nbsqn2AHqfEjZ4LpTHgdv3e9LVwQD1bxMMQ-XPlOj9y5r35rejk7J7EBaVX7e7rdPNvxiZR3RtyC_6KHVj4OTnOZWJd6ua1kn5UR37dtFp8tqR1FQFan8u4HtUw5fWMv1o2mtFzT3J3oHllhMaXobG-1JqWr_2b5YX3pz8bd7b6PDm3YAF6frc-WRGVx3D8cgza9lknb5LmLYV8Fwq_4uR1x30Z4xdctFMcoTv0_itB5tdL9SqeByFn0HaStSkMjlGelVuD7QJAsHKjpZuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=PV06EtcqTHh-SsYaAFrOUF28uBwlXh8k_AZ2mzKWlroT2WqMsInnJNw2-zTq0egKD1xuV2kN8G_ubY6K5zDEOkN8P-fzjlcJDWwMp04EZQfFM9c2FZ1d2WuxIfTpQLNloyqzqU1w_mX9eZFersXNLwlQfADDeIw8VFzOWOTowp7glUz5nhT15LzE36SYstcAmGyt9r-zVE0TRhrQycXYgkLqe3UtRMfLkoQiic6bsd3bE1zt4yG8syyHDhE5XQZiGXfQi0NOFbwZwxWLfdlNYIVFfH2R0H6RPSiDe2s6C8yp8qT_ja0pI_thi2kZSltkGPXpF8V1YnVId6EO1AKpPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=PV06EtcqTHh-SsYaAFrOUF28uBwlXh8k_AZ2mzKWlroT2WqMsInnJNw2-zTq0egKD1xuV2kN8G_ubY6K5zDEOkN8P-fzjlcJDWwMp04EZQfFM9c2FZ1d2WuxIfTpQLNloyqzqU1w_mX9eZFersXNLwlQfADDeIw8VFzOWOTowp7glUz5nhT15LzE36SYstcAmGyt9r-zVE0TRhrQycXYgkLqe3UtRMfLkoQiic6bsd3bE1zt4yG8syyHDhE5XQZiGXfQi0NOFbwZwxWLfdlNYIVFfH2R0H6RPSiDe2s6C8yp8qT_ja0pI_thi2kZSltkGPXpF8V1YnVId6EO1AKpPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=pCLoNYx5FfNHp3K9bcyGzaRkL1iZSx3r8sX1qW2iS6fWLqebymPp4YxjwUI-h_QTjvpd8aS76ati-6Sqxsz-7LllS2ayq7mhdjYE3R9OqHUB4ujQrDPpij1J7n7pMBa67N2Py9aLBPqSOJCWQlqI3ZC19Unq2k2_sZy-5v2uypXb3WEFmL4AaP0HERnzqUtplE1eC9dKwivSypvOuotjh7yYRtGapNkRmfj6FRy2WWP1GdNiUhYUT7IA0KAbiVSlMFPQQLhEP0yZlAHcPEyvIX9rgfNlF2hZzKDmr1EWvPe-ru9uPoRYQnUeA4kZ9TTz1tqlJps-vIHHfpQh6-Ad4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=pCLoNYx5FfNHp3K9bcyGzaRkL1iZSx3r8sX1qW2iS6fWLqebymPp4YxjwUI-h_QTjvpd8aS76ati-6Sqxsz-7LllS2ayq7mhdjYE3R9OqHUB4ujQrDPpij1J7n7pMBa67N2Py9aLBPqSOJCWQlqI3ZC19Unq2k2_sZy-5v2uypXb3WEFmL4AaP0HERnzqUtplE1eC9dKwivSypvOuotjh7yYRtGapNkRmfj6FRy2WWP1GdNiUhYUT7IA0KAbiVSlMFPQQLhEP0yZlAHcPEyvIX9rgfNlF2hZzKDmr1EWvPe-ru9uPoRYQnUeA4kZ9TTz1tqlJps-vIHHfpQh6-Ad4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DGxzPL1lvd0x8zNdYWrrJUcMC36u43ILz5XFqM2z5AHlzI07sqMXSM_V-l7Vme_ZKAvJAqPccYlhrsjAEaPY5gzG3SJUX2OqiZgYjExZBF4ZXP980WVi1BUFwMH1upoMMHKYrAn5FOWi0jXMxz-TTyG-xzpv9xnjTLSgzKlzE7yFowOM-151d7d007000UQQvAI82083HCbjJcJ407pE0NOxJUQsdR6w6rHePT3qMS7xoNpAKKVUT4jSnN9X09n9Ro0loi8ZJ3-6fJOCv3_2ARrqVC1uRkMITTyzvjzloi47FdIkM-Yguhf_KBdIzjRncIPH4lSI8d7hxYUw2oCO0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BOYHSdtjN3pW4i_V56uN2DVg_scO8ozt5Bp_814FDgft468x7R3bc-XFpocVCRHEmvXwrEW7vXf4YnlwXQu8ROTWuw4D26VyUZVVk0dqXcoytjfzoaLsMRcCnO1sasrpoQpKxNaZopLGdYKIMREBs6BZydB4CHXbxFxzciDUI0mXlB_ilpF-CK7JT7DUrWUDkjlaP7CXP4Bd4UnToSUz8XFB7ZuwgFp05p3DVu0MFfpOs8RwYzLZ_hOsyEHBP9jndszUubda5d5SUV_Sd7Dq7o9igHV5vq3yy4X-X1IVGsbvQFlTehaCe4RQyl6wIUibYJSYgapAA8AQi4jg0zaOVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KalJFTmPT3423Eo4qrquMkBnwRWqEax8SjrVw1xkMrxc74yjMV8-2XWoz23j-eaA8hy7rw0GKp479iTS-iGiL_sfr8yh8Q3ADf2gd1yIDrkl_Cu3X85Go7DGrJ1w-WY-MXNaITaGNjqfbpqAxskNP8PDNCK7Liev4_vtLESIqeFb9kmwibmBasyLsRzqPrGiEK8AmkXPRGBZcXx1rUSBxEl3u5pqRpEjDhV9D8KdSGxzcJShBxu20F2_7OUdkZcYtaPu8MZkBVaV5Ae-RHl3qxbEXiOu757mf4GE5Ka5QnBSvjzgF0ehYLvkFL6rzxBCIHngoGNGcjeCtXr9Gk9Z1w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q8D4Tk88yzOBvkkadfbBWzak2Sn7NF32gRvtA1bXn08hx7lIK2KqP0fNfj2rFHSAjalQxypOdae92sWSbkSuJqKwNgBZUcwlKDQsfyGi07u_i21ZEugvsx8DbeG71nWj2EECp-Sud6LVqnJ1iy6pdJK-6U2DQzxxJDWjZoE_-bINB3Smw_0A-pdDZCZ5yTA0njpdD872BGInz1OajQbn6mrnvNgtvg_y6rSNSqBnBMIxkbhpvy_pNcHYNRY4YlceDOrzxI_Aw8ubf4fE25r9eVJRxWFLKo_kgXhP95L-rD88zGTlcHnRtqU3vrUj4foJh6HiWtYBSOh4emaFYZum1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mspOO2P-_6O26MNrbyETKai_dz_TD50hCfLIfF54zPlYmfKhdW6V6XWHvQIGE5jJ0AqkdCgRtvcUfx_xcUd5N8Nzz14zYutiH9F6Am7qacxMN6gpwl9B8Ma9LxzlSBW6O0i3IZIuS7QoBWxGmwhlMD0TLqzMjV6NC9A_7MDTGObU6d77MubS6WIQomYr3fMhVPqYG6fy-uwLfs8Ovz1xiYNhD5QRDUJJYb5IRwg-0zsAYgvkO2PXrapPH9Um8bNHOSHOur9MaBB7aG8mfj6CGPr2-PfE8eSR4UayNtECdW88ebLUW49XyzRk7ucw5jyDG1MnnuYuVbWetXwPl92lUg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jYir97CgMnfWQhPY6bXMC9QMCSw6RXo2zE1nQ46wSaTmXo0LOSS93UzfJxjWD-p_aKbna1Z2L7RRfJyENijA32WERnlIJ3eazkf01vq5p43IC5_socuXakaKZEwQI5S4NjlpFOT0lwlnuZmqmN58hNgeRAY81Tc8DXx-VmZd8naNh47tA2_vl-a7JzWtIiSQea5fPy6uKUqSL82RoEzWFDj7NkMh5QoshgwU_c124t2Lo7GojLeIZMMoy2IONc938rKUdkwXKDx5G-kWMZJdCy0SOjpZVoYX3vjRfE1Y--1i7UfZADPs2yWz3golfCFYIvuDCTX-uWAxh_rirorf2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uxX4NRB0m9bqelsVeAmD_kUSAU_VJFujwkB9SRgUFCmCzpZJqzY4Advs_e7OdIbO2-kh11W_CMhoP8bHdtD14jQo7aEVKVCRa4OwOxkHasabWF1FjGQ24csV424oE5gQJxmahQKF-7UOTsxEEpK-ypLymX1y9EFmzBHhGvcqCQ96zXXMwnp-7dFDtl7k_cY3aQZUgsKLIFLQRRMvnbGTlcYuyELKHyTa-QH0cGhx19ebZ50LXakmZ_2WphROeCvNkH_e_r4xoR5G1fLkJzVtxSKybDbeBAMOc6S3B0lppOBJ8q56eju0TzMqVVufNDJ4R6501jZ4eLqhbMKg6HIMTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SmmL8RGqn_vvoTIdJIGH1nGVhq8uKCY-w0Gye5WotAy_Aw-YJVVXRA0t64NRlvyEicnsqFRC4ey8qV4bKIExWqJTpDcZLKiQgsAPSXP4ts21ijVn8wWafz9E9rgdMDjQ7SBE9YQRk0lcyrNto-xpwrfCfb2nwaBPaFE5zDF1CXrjVHVmRobcCCO4etmmaPu0dEy1KOXMiQn368ZpQqe5VQg1bTTIw0nF6wyvUsWlWc7C1oOJ9B6WZ9wPitnNmMrD9Xe4NwLdl8O3Gt2rnGTECueSCUDEsxZo1ziOiH5T3g3BQ9yM66SoQFGwgD5MvuI2vEAdiQPAuBFvRDuget6pxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DXEKZbvVBU1HLmxMuM4pup0cXi3gfRf8ELunKguIgg8Xpzu5RYxiU4iE7TWHdxETpiOO-ASJk9T_xWQgtxJ08aEMTfYKVpdQT8CXbdqp6h_iVWKdrU1E8linJJTTceMo2pFk3IeueMlfneQIk9WL1PhwgrFVzRx9Kj87V5bNIIx7sSdWQyTu2MVz6f8vD-o2GCj8YYxSOPNqqUGwB3QMYdRLZJ3lYtF8jYwsc9_zViHUOdNf1qaMT3mrNOsJ7HfbCY93I8ce3QBzO9fKqfPs_mFdSh8x1QUDn5u21ERHSy7ytqSLoYeESgPCK0HSlYOnC0Rcmb5IiVzLwZbPi8eGbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gmv0vmSR4RfBrLMOGEOLLYNQCc737ywlTf9GG1II0ZJjBObaKpDLFRK0zkt0J__nHQ8wnowDwvYFQxGSX6VZ6jtYIL6YgUhUfE6niThDEYoeG_EMXCjoo0BnFmoMPaJPsB8obn6CsVBCL48udUCDyk9gQcTqfoZRtMxyVIk2_OFfvpzRLOUOkswczFN4BIArMwDFQQfpfgLtfgd6kgUAd0gvjFFw_Tw9yhDkY0InfmLMY3ogM1Cc6y9eS4f2CFGHa7MRIvAVPwHt-fI2j_HAtIJGJT-mCC0zeI-gtrjsvbD4alTSa607bYInPaMLMVFqF8jjC5pnp1zePqHSIXsNoA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=gvq_rnOPDz2LaURnA0zA29F4VZh3tk2kzrE01BaInUGxOvvVoMFlSvBpW0HBmOEYPv40oJS2vTKRsLn68FPyH7wcoLlHHHi8N3nG0MUdOV6rRpaxLks0paJvo9yPgCXRc7v3nMhWtdCohX9REzdPG4vl0Zd6bXrMuSHamU-5u1Mp8sk-uEdNJzS6VBzlpMX6EafOBh1nVZqqy0j3yYqQ8CUuHuGKRDENiqDi7BP536ByEWCvleiaYUsbS06S9T6V9z41ctMG2ZirORqTmiNI99-SypW64_5bNhAPEFJISdRDNOsNt4um7ogmkGcC-_9_Ya7Vd9XfNXmZ7H4maXxnfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=gvq_rnOPDz2LaURnA0zA29F4VZh3tk2kzrE01BaInUGxOvvVoMFlSvBpW0HBmOEYPv40oJS2vTKRsLn68FPyH7wcoLlHHHi8N3nG0MUdOV6rRpaxLks0paJvo9yPgCXRc7v3nMhWtdCohX9REzdPG4vl0Zd6bXrMuSHamU-5u1Mp8sk-uEdNJzS6VBzlpMX6EafOBh1nVZqqy0j3yYqQ8CUuHuGKRDENiqDi7BP536ByEWCvleiaYUsbS06S9T6V9z41ctMG2ZirORqTmiNI99-SypW64_5bNhAPEFJISdRDNOsNt4um7ogmkGcC-_9_Ya7Vd9XfNXmZ7H4maXxnfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nTDrL29uDg1wsKbZKHi4-6_Jgo4SDuzTzz2ZZy7vJk6KCK_wxJ-imYL_J8DhtRpqhkPelLDOG0VCYH3haOZ20aqJRVAlksc3AkfO7XoOqPMff5L1n2cTMDK9zDeB46DajBvVYMvlDuOSkdl68EPlxH2IdpmyZVi72ci9KTkAxgYX0j0Bk2VfxjUFWQGyCJLKugUgbZYBKngYpxRAdC9tHF8ThIn8qO5cYI9S8R40LfqwZa3b5JpfXpKK5eZokFmBJqoe8alSKE3jWcEoPoMshy6dgYzD0bAPEAqUmJMNsoOdoSUlySKIjxdaN1kIHOxpKghCTgLwELFjOfZLFvUrFw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6663" target="_blank">📅 09:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
ترامپ به فاکس نیوز : به حمله شب گذشته جمهوری اسلامی به پایگاه آمریکایی در اردن، به سختی پاسخ خواهیم داد.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P_qxdVEPPVKKoHQa7bfGXZBMHuQl-Zc4lz5phq2qLoH6dHQw88IaKfwBv95BZ54u-_2ZO5ilbzTxXIYUJXsEA8NeZsXsJEwbhRvX2A0-hZGKskzGp1bMDZwYPRtw2nwTUa2UyC4pOg2XSIplU4nSpDtBxbsatTJ1skQ_VwmU4_bcP9zzoAoeb1NcBxZvmR_VZ6vq9JtN1-VXOnU6W4oXHPTg2tRTiBZ4kzrYcMynffBbnCE_Aj1uTJNKGPLL9V4w2uQivyGUwMm6l-ztpBm9Ly-OJL4jhoFWilgLXS_4h0YXcLN3epHkN1XbZmL7YxVLxCc0F-DeErbk7rFjFBdrCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=FdflbUjLAT2Em1pgn-pMFcnpfszXb0l1p1qn4Omeu-P1BLCkuluUsSlmqXnOGO3sYpJYXaGA1kt6KJ7TcxJ5udM4j9w_e7wGOXfh6iV5JbsW7nVqkF5qW56r7lH9AxTz2NhrVEuE8EKZ1T0kMylNuxWOxEDyj7WqyeoTlUCx0k13AGh0Z3MUGbWMB8R1sIJR2k6G_JNSzTB3bmnnqBe3BauO3-3Ew-UnR-ir04wbpjnQr8xNeYV3ZW3IMhOOquxmFe_4OBP0vGJvR3cm33tXCbI2GI1vBlNU9QA0AhMXaOTp7VZctQn2Mh1IwpwL0hgBbCV7_yBbwYKnimH7RldjIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=FdflbUjLAT2Em1pgn-pMFcnpfszXb0l1p1qn4Omeu-P1BLCkuluUsSlmqXnOGO3sYpJYXaGA1kt6KJ7TcxJ5udM4j9w_e7wGOXfh6iV5JbsW7nVqkF5qW56r7lH9AxTz2NhrVEuE8EKZ1T0kMylNuxWOxEDyj7WqyeoTlUCx0k13AGh0Z3MUGbWMB8R1sIJR2k6G_JNSzTB3bmnnqBe3BauO3-3Ew-UnR-ir04wbpjnQr8xNeYV3ZW3IMhOOquxmFe_4OBP0vGJvR3cm33tXCbI2GI1vBlNU9QA0AhMXaOTp7VZctQn2Mh1IwpwL0hgBbCV7_yBbwYKnimH7RldjIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=EUWJpaPEoZC77hoHf1NuiyZUxwjzthvKmASkcQbyS_ILxPNaYO1_SKDmBukyHvoQ6yCyp1S6CZxj3e17p860RaqA-TK3UrH100nxRgYuukSA0RjhVgRdzhCJ5NCsqWp428Vb9-8FfY6pg1y_ecrO00TlEiWmS3UnFET0-3mAjnAMFq04O931jr_2DZE9L8CVj26wkI2-zdJjcYZPN5s9nx9SVGovVr2mXay1CCU6fyNj40fRuwVQop_XlcWm0VXz2AwPTNfsK7CLNMNsp_AWnlOZNby7TADgBDGAhNus1IFh0Qh1e_cnwMvovylPjHBFvoYd3nrsbzCPM4pajelh9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=EUWJpaPEoZC77hoHf1NuiyZUxwjzthvKmASkcQbyS_ILxPNaYO1_SKDmBukyHvoQ6yCyp1S6CZxj3e17p860RaqA-TK3UrH100nxRgYuukSA0RjhVgRdzhCJ5NCsqWp428Vb9-8FfY6pg1y_ecrO00TlEiWmS3UnFET0-3mAjnAMFq04O931jr_2DZE9L8CVj26wkI2-zdJjcYZPN5s9nx9SVGovVr2mXay1CCU6fyNj40fRuwVQop_XlcWm0VXz2AwPTNfsK7CLNMNsp_AWnlOZNby7TADgBDGAhNus1IFh0Qh1e_cnwMvovylPjHBFvoYd3nrsbzCPM4pajelh9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o1JgK-u-Wy0Y631M5b2DMsaxtcmy8ree-DDAuQfmFRDHG-UDdUHnXqgh0scjYf2XCN_4lHKx_fU4SMnSPx7FoGy2RQbZJsr1MroHXUcTmXSvquxWjMckC5UzQe4nNJP_CvOrXS5Qnx5N9tJC2sr9ov4xiCUfqn3k7qg93p5WXZt4uR3z9xU-qEu7s8qJbOC23KCfZpgHciTONaCu-Vb3-wrxQZJT-GYadcsTJM-fu_tTpimPcK0XoxAagPmkDkdWNB2col9tJZqvULCJAvLLB7znGltUnhtcUseo40huaBY5bGHV2lNqd7Pub0PfSyoC-CrGf1KPUZWf7hRwmsa2kQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KGDuCrjRWKGfAGoE0daq2MVfob5lH97rggmAX2IkwmuOw8D7rxi175qxaR9Swa-kEcYM_XV2_IEzwudL6YSnLKAgDmcJogwuYQVFeopYPctuJlNEAj05h05r9eTdZjU_S4Eit0y_YL2AwUV2zyHkYC97emWvtvsybxrnkw8Cegbslzp-p7skJdOnnBvt-HTVHL94cAXKNhaknIxXbCfYTTahOEFV6qlB4RnmAaaBfjeql2Ao0gdgrkppBtxuQG4ZYQuZ9P-eU_yJF9KKa-iX_sdJji3dNCJIIH8HhdtBOrBDKg4tKGRXIJCZ80Beyv1xWtbieLkNj73QTeSEClBI9w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S1EMpZsGQtbh1ofRgMd9kqk4hOxivVJ-RMFjaP1AcksphkZH9fHHjc1Dffpvz9geegOg1_bJ-XqVAQGgwael2lK1OJ9HRaqXczYFewdDehuk6PwyyUDPdm93xY78NEQ1D1dhd_jBo9G6ZkHthMDK296HmAz8y2oMpLErgkykIo2_8nxCXFAzmsTUV8-bZlckQnEYhRZACNZSKlyuZAzLoqtlodsLNDTEr-foKb24kPxVv8zkqgkyDaBCyeEL1pLWCAbKEOANCBKMQpSz2_6o_4u2oDjiVZa0TBWndBaC1UTjQ_b9NFl50i-M2DUQLXKkxHIf_qTh7dz8Kwr-5GaqUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KoMQl07jD1dJTg8xVS7rkuEPF6hwvfnFXjog-hhsJU9FBG9rmBy47LUEH0EMttg3t-JVAZq7znYCpEkr6ttDnQ9YkVecL72g9K6h46qoGgZyQ7Nr8YvQGTPbMi5_2DO8jzZzMTNmnOvL9QMHo4xXcVcINX6CgU9gD-I0jFqQbNl7NF4Kv372BzVM-dDK0IL8zFNAhMi-8mh-guQAlayZXv800Y3YsdgKyB2BKHAgwvHaZHCOYfCbVe5L8lVO7hI6CIFTauI_2xrcRohsEPCi3WfUrxg4IGHdPiWOiTUhcrGn1RXgt7fhNs4od_qXUAXSByeexNjWQ5X1Be4bW60SRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sXwsdkr1gipMDSCtG2y8mI-zeIgobcyqceOd2KlFdeksXUsmfdTrDaLz9yQxCsMpfYk_m0lX--d7m1Uni8K1lbOUfe-ZMULBKQV-dCwqcAR0P5mD6uyJOObPcMybrQwpafcyOempp1ZBRuu8_zKaThXyX_Ptayzn18gQZmWbsu5T-ujSvTPpePFLbpPJ3r_lr9ONg3BJ2WgBzPx1317yDKX0HGLIHwBacOROXR5yhE5AlwPAqmd-VPzYlM9vmnqGh31Z2H11QCd_f-ePiyP1XGfb-_5cDzpNFDHE0Vhh_D57kKpwivt0-Yo72WM7Bab0uu1gzze1GvMRJaCKiek3bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_xSk4fQP6Tw0PPmudPmIS1LKg7gDt1Dac__NmrRstNGV86bnZh8PR8b36EEFRHfSgsmofH8gnT8ID3cxcZxSnetaxn4xC6KK38vmW-Mw_m8IeMak7F4q3klVBPg5CDABnNe7NeYceuRRmGrvgVKBYPcwfHijQmU3EI-lfuBNRPZXliYpxpzTcOutmRS6yX19hVhMVZDLhaRCnMHFQ_xorFy9TiEUyW1Rsxr6d53d-T9r-55Blvd3zpx8H1JGp8yS7oWzltjHSFswZb1ZUStz3HEkGI6b8PXmyrBThtPsdqmTEjlZjq8yIj9khQT68kklAUkJZwsqyWdWGD92KqFCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d0zSpzn2lwk0a-HeOHfPM5a9QFvA6YVCngC_25cAhfQrMoD0rs8nWz77LgD5JnnFjSTkmjC2MNzIoO71yhnULX0xbLuK6E9DZVc8vuEDddswcZZp27RCd1DjOF5SUHYxSh_SnCEoj1k9GYQTFEEvtADomHLO3ZLx2L9WWPQrcynzrDjU1zjP3okbSet72-Dvg1fZrNx-AzDosDOkazR-Kn77n2vXB8vywcvvQWYn329Py53oHBkGe9oeRNou6CuMbUF9Ciay-1faS2ZWwBDsXBdi3ja2WP1iDZMV2WTM5u_j0JJP8kJNn_n4uZYU8QxgHissRFYTUd-yj3LEMzpgOg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=pTsbUvrvS6Fc-UzW35SKDYerRGl1X1gs7Tb_1ELz_4OgCFxlNxJSPzu9zS4FHmNAWHE7FBYbSlEOeGY4xuL91_vw9mnGktllHZD7cZ_tMVbcL45q7OM1PFLlbzEYavEaOp-U0NGzDbzsDpudoTUIiSRa5l1jL0ktXSWl5P2m6B-8LgtHyyHST95v64P_H7qp5t_JdRea__7qkBXGa1DrsQQPc0TKdheDDTFeM87266TLmexYjiqHAG9R6tH19Rx13QpC8-7KCD1Jb64aUKPgFnpOXudsBidc9l4dZHWkwcYaNpKtjt0jBzs0xxWKOAI2XpLM41bHzRDsThBtNwQcaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=pTsbUvrvS6Fc-UzW35SKDYerRGl1X1gs7Tb_1ELz_4OgCFxlNxJSPzu9zS4FHmNAWHE7FBYbSlEOeGY4xuL91_vw9mnGktllHZD7cZ_tMVbcL45q7OM1PFLlbzEYavEaOp-U0NGzDbzsDpudoTUIiSRa5l1jL0ktXSWl5P2m6B-8LgtHyyHST95v64P_H7qp5t_JdRea__7qkBXGa1DrsQQPc0TKdheDDTFeM87266TLmexYjiqHAG9R6tH19Rx13QpC8-7KCD1Jb64aUKPgFnpOXudsBidc9l4dZHWkwcYaNpKtjt0jBzs0xxWKOAI2XpLM41bHzRDsThBtNwQcaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWmhsuZl_Vztm6u9vV8rkFryGiTFMs9SgT5idBiIQFq_iI7C3mFtKr2WuHkf1RUvjopWTvQQT7e0tv0nFZaOjZ2yRJVfotAJBIG1vCOmYjvxnZqtHVqtVlygyZegf-5kAD12NeMwR1jWXBq9blLDET3FK3FT_v7vb3GmzXrNK8Jv-8WOOYvg_lpUh4YJXdA_QebnLccgz65jn4X5RGiKSkr_QcNOpSYbi51iDUbunMRH89VkS0vL8lfxgkVgopydWYLnmQXuSbgOnOhZfESX3POvhzoNbb0wLcqVPRx2uqlW5-0yy_tpqQt3hkZZRkDhmZJKFmx4hk8GNBhR-drvzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=YbZaI35XTwcEMMnoih6v-NHp4US7Qwj5RkWdQOZr_7wmaGyVyaE-71b_PRklguJzjt6JFkO9H9Jtw1w1sHXr8rpom_XdY43fiP4P-CjjaOateY_GEUWUH1Q9rK72jrlN4w1MIIkM7xpn9pYTdBhEqwz6rbCG02lry3qD-SLR6BMZCCq3LotL1QixuyONXEFJu51coppu9O6A69ACL-RZ8Umsop0GBvSac-aBIslt0YD0-HBry2NiUNkG41uDhZFgnBXveXpjPDKap0Ne_YFGwA2M6WlwMopkVGh2xT9rLCB8y4UiikAI979tkJzwwf3u73ULy0kKti0ULgyc3mwYmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=YbZaI35XTwcEMMnoih6v-NHp4US7Qwj5RkWdQOZr_7wmaGyVyaE-71b_PRklguJzjt6JFkO9H9Jtw1w1sHXr8rpom_XdY43fiP4P-CjjaOateY_GEUWUH1Q9rK72jrlN4w1MIIkM7xpn9pYTdBhEqwz6rbCG02lry3qD-SLR6BMZCCq3LotL1QixuyONXEFJu51coppu9O6A69ACL-RZ8Umsop0GBvSac-aBIslt0YD0-HBry2NiUNkG41uDhZFgnBXveXpjPDKap0Ne_YFGwA2M6WlwMopkVGh2xT9rLCB8y4UiikAI979tkJzwwf3u73ULy0kKti0ULgyc3mwYmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=i78KOo_PUbYzG3FIUhgVFAfMFAvRIk2WGb_F34y1IWH9iW6VsjHGnKmPNvMdrPl_BI8ZuP3DEZqOcbcOAjgkInXSgz8FvPf54Mty0Ja7vQotV3ylndsY2Oflb6XG5B_sQSSxNlgaqX-GaoeRnkCK-vmO4QICuumHbZdyzS-1XlbCCUlmiT4k4Kfo_t-d3dJjkwBXtaYLyZcb3VPT4JJk9VITHaRdWVw5IzCNxJp2GtDJ7xav9vtKwTcgvSEOmpauET1BAo0iGXpYxE52UZTUtdipF7wNpTWxtSnsNhLChWol3V6QmYzoRChKYNeIMvesv4HP9jMIgOUV0B48iZIMtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=i78KOo_PUbYzG3FIUhgVFAfMFAvRIk2WGb_F34y1IWH9iW6VsjHGnKmPNvMdrPl_BI8ZuP3DEZqOcbcOAjgkInXSgz8FvPf54Mty0Ja7vQotV3ylndsY2Oflb6XG5B_sQSSxNlgaqX-GaoeRnkCK-vmO4QICuumHbZdyzS-1XlbCCUlmiT4k4Kfo_t-d3dJjkwBXtaYLyZcb3VPT4JJk9VITHaRdWVw5IzCNxJp2GtDJ7xav9vtKwTcgvSEOmpauET1BAo0iGXpYxE52UZTUtdipF7wNpTWxtSnsNhLChWol3V6QmYzoRChKYNeIMvesv4HP9jMIgOUV0B48iZIMtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tzDxISBvHXOyR4k1Eb5aPewQORSi1FDqdLXF5fqEfEUENJ6UcfxwNf126PfHNa5E1jNgM2GkAZVZKbC_dYtRKmXUNp4WGVG3pepg_d-qii3RNyOumBg3ArRgMCw8cAu8Hfuqjn12xUdY-s_c-bbIiFnhVB2PZfEqeA5QhY7oS9Dp5zjah0TeBHuznKMyAhD9B23GLieCAH-Mnh8g5fssKgfs3MZMsU1XsSGcgGEB6e5FSnu-tD5yiS1a4WY-nf9hSQvjbqPXXYf-Lzs6K0vEDvwzQ7SXqihJ0E9HgbMl0zHp_fHR758gUIrp9Kf9Xsj0DDX1qu52y-bbb8ads6qakA.jpg" alt="photo" loading="lazy"/></div>
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
