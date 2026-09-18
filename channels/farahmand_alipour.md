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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-27 11:00:35</div>
<hr>

<div class="tg-post" id="msg-6748">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=B6sBOdloDVnhFoNbX2_BINbCqZQN3ujpyPB77xVLFnOStA572M3EyvsvfnjU7yxjVoIT4BZyqgZb2ZJnB9zALHyxboDe46S94zHEXk4_BHYdgCEDJa9KZ3kQHXEpHmFKhc1FGd6EWq8xHA1KQHcnOxaixVENkjkYV-xBlVyEwkJMUztMq3r6K__Cp0KOCUzJtH30bYa6_-WjIwpAWs6euV7wh3oRPJmfF1GypwXUrtlFIMBpnIC-rSeGo64eQkR5zzZPdkmLi6s0WLlP7ewkBOHEIRuc-7Ec7NLKkpS-6beavq_3uiHMrNoogKtXW5ml9WXjoMyVSF5i2d2Y-iDu_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=B6sBOdloDVnhFoNbX2_BINbCqZQN3ujpyPB77xVLFnOStA572M3EyvsvfnjU7yxjVoIT4BZyqgZb2ZJnB9zALHyxboDe46S94zHEXk4_BHYdgCEDJa9KZ3kQHXEpHmFKhc1FGd6EWq8xHA1KQHcnOxaixVENkjkYV-xBlVyEwkJMUztMq3r6K__Cp0KOCUzJtH30bYa6_-WjIwpAWs6euV7wh3oRPJmfF1GypwXUrtlFIMBpnIC-rSeGo64eQkR5zzZPdkmLi6s0WLlP7ewkBOHEIRuc-7Ec7NLKkpS-6beavq_3uiHMrNoogKtXW5ml9WXjoMyVSF5i2d2Y-iDu_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lPw2iJuW7gmTf02_jjn0QvQLP-XX9lG40BVZVlX111CeZIJI8lULEZCsKTJUeGoEnXuhmNZw2CGrRD07f2AkRg5Cu_PK26cDPOzseDisGAtW7-DxLGV_rH7ukSpEp0UfqQLShgWCGo8nFL9vP3XBJV9PTcHNKKUkVNYYFU8fWrvVat1gbTxaBlLnDHZ7kjz5_p0N4_kOeTzYCpAV_gn77aBQ02oetT_-xN4N6bg-IDdWmv5n1XTLpe4xsNSm_Q-Wxv_MwfCwJ3NIRRmRY6KP7j2MqA8ijnXwFz4gBJl7kW7Scr8MllwvJdJDv3p6skuOYiuPygq3_mi4VKU8_DSeXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKvxAnrIRfvmwKPBm07HqUGE7UT5g9k2MCfljWLWqFWY4JfXrvgKdld0nrY_haRUhGT2wwmu-iDMo5mLkPapwXAVTEBUSiAT1jxFeV42XLVIWy8zeAek6IRW4gv0vHTukvjr716BTuLHi0iW8zJkkWOsAwxjaqq4eL5J2bwxgiWx9gJZEqdJhl50-6KDIZ-k2AY-5US6wapN4IFIvuTnXCulb2vcfQWaoMI53f1ZJHhogtdP7vh-PUfxld1INwES9F6kGb4tQBfcLMyo2CtbC11-sH1QlzA1KwhkJwus7j0rlz7UA2SspthbD5pDWfiYXAejROTlK2PyE1B5zCHIhA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6745" target="_blank">📅 13:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6744">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=OLWgET2pZzz_aYZhoxG0UzZaqfw-5V5wc3rtd3P65l3PaaSr9_UIaS7qtvCT9OQT3M3T5dKeg2VcjadQHaGTbXtvQe_k7HprRWxVaOFgtlGZ4u4UoVhtbMlqx5Tg-pawkY9xQday4pwAPkKURwF3ecqhGgVP89-_R4wrU6_WAWl4sWcuzH-qAacVAheiJgfPiNwJSfMvpEySVUDL9Lyby9uihJn4rHL5bmVxOSq0tE-0k1DeSmU72RAC0FBfPAZpa0yKcUqquXL_h2JN0vkWONZCjmfcMLN5_3_jvsz8XplghnmVW5bjA4BlxwNsLOAk9gdBUcO5M9f-hlAMz4L9ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=OLWgET2pZzz_aYZhoxG0UzZaqfw-5V5wc3rtd3P65l3PaaSr9_UIaS7qtvCT9OQT3M3T5dKeg2VcjadQHaGTbXtvQe_k7HprRWxVaOFgtlGZ4u4UoVhtbMlqx5Tg-pawkY9xQday4pwAPkKURwF3ecqhGgVP89-_R4wrU6_WAWl4sWcuzH-qAacVAheiJgfPiNwJSfMvpEySVUDL9Lyby9uihJn4rHL5bmVxOSq0tE-0k1DeSmU72RAC0FBfPAZpa0yKcUqquXL_h2JN0vkWONZCjmfcMLN5_3_jvsz8XplghnmVW5bjA4BlxwNsLOAk9gdBUcO5M9f-hlAMz4L9ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ie7_Iuhz4_0xcOrTUmDdDwxOY7thmSJX-6XcyY4-cDjXB5QUuf0jxh2I6hDyZmwLq565APgy4lh6mcQIf3yEyj8zQVvCmSTCxKwP3DD1AGfbdExQez8Uhepwap2xkERjzd-Bojxb9v7kz-_0JhIyjIDiaRvvTdOaPQvAXszzN_5Urs70ijOjPbjmtmvFGiEfctHzv1bvML-zLoTc7jwA5o-MiJu7lsPFNwNsJZwPAOCxEDPymx1DsHdqvDVZ-4xby7sHpjXYdycjuh8RzeM8ot1KFFRtRsE9BwEuSEWq3M7GrErXVkF0vGnCqwa5ns9w-yajNohrO8Hz_khZJYCZKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hP7x72Hy0Fa2XziovhkvqBKFUX2B4L5g1gbWJCIfiauaqmcRDdDcYgY7ppGPRC-fjxmAOABxurOqgEiS6F7sLGo5fyyVlUmmgaeN1kpEnTm6CnTlH3kysJQhftj6Dr7cXv2h5fdZQtdoO4kvSHkwKl_QKOdIYVRH99Pena8aEfvi7bO2b5G6yWrbsfkiOEVSyVbjptD5mLXjGfAlq2htAgHIbaCt-oKXZaPxTn6yR5Si3c_0AmUy0vbSRUllQez61xTJ0RBUJE4bZ1yVXXzkFr5Bp10JbWL4UHmwrtusz-gKLlk_M2jOOdQPy1Pyf2a93V7L5jiTR4v-NetzaUmJgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRKDtUeMfKoWdWlkHgd7bdQqsw6GjiZfDA1gHrR18ESoyCKLgfUdZ74nMzXbfkoa8haNbju9lalHDMHof1GSxGDStJpcVxIqyHFlt8LQJHBXiHebnNxQVEGlK8R4a8SSd7R1ZFHlV01SIiC1hQ-irpFCPBkbfVk62kns0z8QPoZfG6Y4j88BpfCvuBxVlaxPP-B6mOLkJs_uU3c-Q-7aZw43nrAmtAn6gt4WulMaDdt6eYm9V73kJDbqGRyREbXdNeFvx1lZwa-faqiZudFvt9ruBnmtSwcNzvQ_iXF9njeMgj7L84fnXszxjK7uhcSAlgJ1qkeNxQ44SyRPFKpTtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S8KGfBKiFw_3fGy66Azn7-r-N4gZT8-nFls5nnHyPxpytFJ7jHecFsRzibmrOGI3a749vUuFvrdo7zx3GzktcTjsUA9IwjcoqL18lq7F1esTvuVgi8wDP8vyv94scTwJCIVsX1I-NYpgeGRfZgPiEtFyMqCARzWlzzjL4AwIIRKSB0mA8-uZ95AaIh1DIqL1egLkFCizKOq3XhVdiQYT8aHsRcEGUoUpoQnz8rqHcIacc9k3MwYCDGZy57NIfaZYZ_naiZdMh8IMzJvLkXyLVOe2gspDtwIGBKAUkppAk36BXlibN3HpJwxLjl05qsGUsB6bW4h71AYtEDk4Fga8yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGLhFLCPOImDauGioh1et70A0ThVVqcZY_a_TTcy1Jf43VDK-SorLsGFVk_HflowJMjOBvSzMEBQDeARPRJ1jjODgziHmuPajWCsSGq_0QIxhXXYT2Syr-Y3SCylaaW1PGER1fOfCwq1C8aWii8fXNpGRoCSBu8pvWEHrwpRsWdQQOMsdPTBFk3zofMuBKl6GZRInX6-VBpP4ZYyeCRxVOAid9HhLIuiirCGrEtqPzSByKPuY5BG0R03-LlftKJkdy7Bollad8tYwmzwsQfierblpJmyGEJTMpYrVCXaMGBaoKA5uw7phwMiF1xqne6hd_Vk10jSY-kQol_9Aby1qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=QeYUpgBbiagAQ4cNrPuptgWcHe_K3ONYD41hvvjkQAtaaMDvrX3C3BK3vs5l5KotsaAFDbPC7WkUu6Acz7fOf7j9lpfTnDWc6eZ0bgAZK9SeS1peIf9T3VHYqFWtjTb3s39mFSuPoNgKDN0gQ1AuIgo61k_hVzgRTP-3sXtPkc87elq_5k_zYnAodSINAVgyVnzpwbl8Tcl1FhySYHahgi4ijxl3vBNXSNB4igNir_txtXCsFQ5kIpIdpvfbuXiepj6oZvkyYduLaratBtIRNUrvpm870guDOQyhPr7IG_K8wgOytXm6PIy5KiViuFpkar4GfghTrAWwowWFymoKzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=QeYUpgBbiagAQ4cNrPuptgWcHe_K3ONYD41hvvjkQAtaaMDvrX3C3BK3vs5l5KotsaAFDbPC7WkUu6Acz7fOf7j9lpfTnDWc6eZ0bgAZK9SeS1peIf9T3VHYqFWtjTb3s39mFSuPoNgKDN0gQ1AuIgo61k_hVzgRTP-3sXtPkc87elq_5k_zYnAodSINAVgyVnzpwbl8Tcl1FhySYHahgi4ijxl3vBNXSNB4igNir_txtXCsFQ5kIpIdpvfbuXiepj6oZvkyYduLaratBtIRNUrvpm870guDOQyhPr7IG_K8wgOytXm6PIy5KiViuFpkar4GfghTrAWwowWFymoKzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=nZ1fbCc1rrD2ARRLLvrt_sMB0OzctA2-cSxVCF0wtwCC0aQ4rf9oBiNTNk4ht10PM4LJd0d54oiRK3fxs3ng4o-uhQSk1w4bPCwTCsv5k6lz69Z5pg5BvXCpsS5tz9yqGz6jrvmoT9QheKtK80Owjl-8IlOB14557jbgOmRM8en7Okb7tBSU8JBojXRLWkz0NZHk9BvNdekvroDeK1rDFAdfb_TsC_BLbJ3TExuVxVSE6de0HK5JkfVYu7eSwa1HZ6CVhMWpHJwQ7H6e1WGekYi-GRydvTrWrWd7akRiInCTLSu6y6mjLBuOPC8HwLKYm9iqj2VyW7wqjtd9QQ_seA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=nZ1fbCc1rrD2ARRLLvrt_sMB0OzctA2-cSxVCF0wtwCC0aQ4rf9oBiNTNk4ht10PM4LJd0d54oiRK3fxs3ng4o-uhQSk1w4bPCwTCsv5k6lz69Z5pg5BvXCpsS5tz9yqGz6jrvmoT9QheKtK80Owjl-8IlOB14557jbgOmRM8en7Okb7tBSU8JBojXRLWkz0NZHk9BvNdekvroDeK1rDFAdfb_TsC_BLbJ3TExuVxVSE6de0HK5JkfVYu7eSwa1HZ6CVhMWpHJwQ7H6e1WGekYi-GRydvTrWrWd7akRiInCTLSu6y6mjLBuOPC8HwLKYm9iqj2VyW7wqjtd9QQ_seA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی به «علی الطاهر» میگفت «مینی پنتاگون» پنتاگون کوچک. با هزینه میلیارد  دلاری، با صرف ۱۸ سال زمان، شبکه‌ای از تونل‌ها در درون این تپه ساخته بود،  مرکز فرماندهی، انبار تسلیحاتی، محلی برای حمله به اسرائیل و…..
اسرائیل دو سه ماه محاصره‌اش کرد و اجازه نداد آب و غذا به اونجا برسه،
سه هفته پیش جمهوری اسلامی
به آمریکا پیام داده بود که اگر دست
به علی طاهر بزنید، جنگ برپا میشه و…..
اسرائیل در یک شب، پس از شناسایی ورودی تونل‌ها، ورودی تونل‌ها رو نابود کرد و تبدیلش کرد به یک «تله» برای سازندگانش.
جمهوری اسلامی تنگه رو هم بست و خودش در داخل تله اش افتاد!</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6725" target="_blank">📅 09:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6724">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=ZqTo_tFz7JQ-PAkBcwyOEP9gqgNkHrq9HvDiKajUZ66V3I2jqwaE6GZVjF3ApHCES1cMHr1YFIHuswSk3PNpvl5tSQh3hovSCxjKqcRiCIO_pVoeTBMuLLpysCjmgzSFTHaA1kjt-w9lBexrmhB1zqcjEYVfXMO3pVXNXVV4U7CEkEEHagd_2LcaHRlRnrBbWPEzcabDB05F6pG-0idZIxFyYsSrFJ_W_5pLYUeH1cvlG4Zd1N_uKPY2dBxgmO4W4KIDLyFN1fiswk_rffh389J9487ytj-xw4-K-INQZpbzuP4n6Q2Sbu9XCl60uQLY-oS78CV50rqJtXYw3CQ_iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=ZqTo_tFz7JQ-PAkBcwyOEP9gqgNkHrq9HvDiKajUZ66V3I2jqwaE6GZVjF3ApHCES1cMHr1YFIHuswSk3PNpvl5tSQh3hovSCxjKqcRiCIO_pVoeTBMuLLpysCjmgzSFTHaA1kjt-w9lBexrmhB1zqcjEYVfXMO3pVXNXVV4U7CEkEEHagd_2LcaHRlRnrBbWPEzcabDB05F6pG-0idZIxFyYsSrFJ_W_5pLYUeH1cvlG4Zd1N_uKPY2dBxgmO4W4KIDLyFN1fiswk_rffh389J9487ytj-xw4-K-INQZpbzuP4n6Q2Sbu9XCl60uQLY-oS78CV50rqJtXYw3CQ_iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=qFFtnwZowKxs7C2o7yYKDu784xNdDK4I7Son4RKV5Zh2woW0aX0ujwXylU4p9rxnIoWEIIAzms7ZPSjRPyFjeViCvR8qvdZLg6YK2y-rUkXyaj0zNQIz5B-oKyxgzglnUPMMidg9mK5TcaenMq2JHzOP0gFUpZmR-YMeoeF9oxF5_o1Xu_1Pui4GOgbq0wOPe1rNcBMnhEx4bi4jRaEg42Y87bJIsxNlKRE0ES99H0trDcDe8hfuv-KqDXQIFIC9r2m0Iq7g6H7NfLwNWgzCYi1lWhcrvSOyxYC62LzT-snq24LLQ_M9IN61jzypU1g9RLi6T2N92fyZX2Pa71RyUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=qFFtnwZowKxs7C2o7yYKDu784xNdDK4I7Son4RKV5Zh2woW0aX0ujwXylU4p9rxnIoWEIIAzms7ZPSjRPyFjeViCvR8qvdZLg6YK2y-rUkXyaj0zNQIz5B-oKyxgzglnUPMMidg9mK5TcaenMq2JHzOP0gFUpZmR-YMeoeF9oxF5_o1Xu_1Pui4GOgbq0wOPe1rNcBMnhEx4bi4jRaEg42Y87bJIsxNlKRE0ES99H0trDcDe8hfuv-KqDXQIFIC9r2m0Iq7g6H7NfLwNWgzCYi1lWhcrvSOyxYC62LzT-snq24LLQ_M9IN61jzypU1g9RLi6T2N92fyZX2Pa71RyUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=gfHTquBrhDR1VsHk-RN7Qwj6O9EivmZVsKz_YeK_2vLu_-c6vxbm-GnK9nX73X_x0atag-FDTczpfRVbEpuAcJ47bPsNGnVr4T0akeSvIrzUmFKcEsSM2K0PhwPumz5nXsF2F4IuyePENbeAy2Zxz75v6jeqt8B3AZ5qoEIQcOEoIl50-zQzcyOwrObYEmpKSa_IeYgEeZm9XBfHvY27qWLtROF7EAfX8Io8WHgCv-vebe6LoiruCHJuXUTScq2WFBjwrRN0gvGWQgGaQgwqJZE9sZAScDdbeBQRM7aYIctDnqwP9mxFibKf-nn7WDLUTxGEd99e0kx1Hsb2fbORJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=gfHTquBrhDR1VsHk-RN7Qwj6O9EivmZVsKz_YeK_2vLu_-c6vxbm-GnK9nX73X_x0atag-FDTczpfRVbEpuAcJ47bPsNGnVr4T0akeSvIrzUmFKcEsSM2K0PhwPumz5nXsF2F4IuyePENbeAy2Zxz75v6jeqt8B3AZ5qoEIQcOEoIl50-zQzcyOwrObYEmpKSa_IeYgEeZm9XBfHvY27qWLtROF7EAfX8Io8WHgCv-vebe6LoiruCHJuXUTScq2WFBjwrRN0gvGWQgGaQgwqJZE9sZAScDdbeBQRM7aYIctDnqwP9mxFibKf-nn7WDLUTxGEd99e0kx1Hsb2fbORJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما میگه :
مردم ایران در خانه‌هایشان
«۵۰۰ میلیون تن طلا دارند»
یعنی «هر ایرانی» حدود
۵ هزار و ۸۰۰ کیلو طلا داره :)
روایات اسلامی و معجزاتشون رو هم
همین مدلی ساختن!
اون مجری شوت هم میگه : الحمدالله!</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=e77B96Swmq7j-kCQMmD3rUJojm2fPhG1VRHO9hd-uYWjsVBzLzAQ0MO30sawGRDQKZsuLPz2X48B0mIJeOv_B8H9CwJyDpVtPIi9EdmwyA7BDPDd_nrzhF37WTou-UTOR_MRC0YUlnByVvcsCBkgOHCdbeGBdACZPRnoypPgLEPLkK3kHnqF7i_eZAGcfcp6Vne4qMcy9rldRiX7FrMaxLcFNX-HwEOh5f77l648Jpmv3pOJXIvbPERNw2l7V8ytmBemUWYK8EyZXTgJGi3IJCuQK-MHy4QlLM3F9c0wis0o3LX3uzWqfRdNPJPQ3aK1b3Vw4hOY-G3Puw3Qfk6nfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=e77B96Swmq7j-kCQMmD3rUJojm2fPhG1VRHO9hd-uYWjsVBzLzAQ0MO30sawGRDQKZsuLPz2X48B0mIJeOv_B8H9CwJyDpVtPIi9EdmwyA7BDPDd_nrzhF37WTou-UTOR_MRC0YUlnByVvcsCBkgOHCdbeGBdACZPRnoypPgLEPLkK3kHnqF7i_eZAGcfcp6Vne4qMcy9rldRiX7FrMaxLcFNX-HwEOh5f77l648Jpmv3pOJXIvbPERNw2l7V8ytmBemUWYK8EyZXTgJGi3IJCuQK-MHy4QlLM3F9c0wis0o3LX3uzWqfRdNPJPQ3aK1b3Vw4hOY-G3Puw3Qfk6nfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=IwVdlMcbNcvq0SuTvS-gWo6p6Yf38tpWaoa9iSPKMko6GnBdBzC-9BuybRWJlUS_6c_O0jxEjYyVmU7eD3W5Yz6FPb43radtR2P08uDZ1y-dSxOK5GFJ6F5-KEuUXO9S18nlIg1RgusQGsjpxfjFIt5yoJoKNq0NaReb_wc1YCpNKcduUrVXyP4p6F6bvNJpsmw39ueZBfE4fEjAZgpLJ_3FroLU1vyEj8Zvk-9PLTkX3DETIvp5uOZ563xY1BR1hWLLY2-nkFU9lS54kQOZVAEfQVaGoYZzEHjii8ifOIB_EhXFPp6yriCT4Kjv66zpMN-nzjC6ynUNpDZmQTMNug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=IwVdlMcbNcvq0SuTvS-gWo6p6Yf38tpWaoa9iSPKMko6GnBdBzC-9BuybRWJlUS_6c_O0jxEjYyVmU7eD3W5Yz6FPb43radtR2P08uDZ1y-dSxOK5GFJ6F5-KEuUXO9S18nlIg1RgusQGsjpxfjFIt5yoJoKNq0NaReb_wc1YCpNKcduUrVXyP4p6F6bvNJpsmw39ueZBfE4fEjAZgpLJ_3FroLU1vyEj8Zvk-9PLTkX3DETIvp5uOZ563xY1BR1hWLLY2-nkFU9lS54kQOZVAEfQVaGoYZzEHjii8ifOIB_EhXFPp6yriCT4Kjv66zpMN-nzjC6ynUNpDZmQTMNug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QH2YqexLX-oAqt0Frdbx4A3rwtD2kHu6pUDJPF3NIH9IAki6-1PRMSE2TRSG0rZbW19__Vo7mttXHeOj0BhREBJgloUfGZmQrgpTvEA9GE0Lj8DlJ9R6cWA7_Z5YEyn85MwReyrr6d1aWkBEoENliLR4ZMHlthjg6GwWW23ydHGjOtTUZiUBkq10YDwkBEHGd--2U6a-l-2hO61rSV1kSnM2lWq2Xn57CdaNmbcx5HhDFs8KL0CiktaaTFfYM4VKxSJIQAFfq9tx5jucqY6utDz5ROzhLh6YwBTfcQfFSuxXOAdB6uTGGsPi5XJDznY4GmofQTm8kOJizA4-pG1uiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکر نعمت کنید،
بلکه این نعمت‌ها افزوده بشه،
اصلا گیریم یمن نیفته دست عربستان!
بگو اصلا بیفته دست کفتارهای
بیابان‌های سومالی !
همینکه این‌ قوم ظالم در ایران شکست بخورن  و به غصه‌هاشون افزوده بشه، جای شکر داره!</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=Rb4XCe306zZ7e0DTum4qNyuAz8j7cGpGl9rjAY6Tk2Mfdoo8hlvNpQy_50hYilF8h058vxp8rVs71ooCMU6doca2QfBqt0GY229aSF6kH_8xVzFNqjrYmuDPUnfjFkWL-6OP6tqpzt8xCRY5IusB9Xc2HLjTTaB6YUNnlVD2MVN3CYHI3EnYfUrwJvbNDrx8U7axWH6wBIe9zRZj53rk2P4NmD5TDZnr0cCiLNdTwfIjWSxgg_i564p0Dpejvy06XCHwh9NxG38xuVz_XjANsVo5CFDAzQcWlGc6djdaw8jmug9GyrdVV0qgwLIdIqR9G57YcjBluWbLfRJsleJJOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=Rb4XCe306zZ7e0DTum4qNyuAz8j7cGpGl9rjAY6Tk2Mfdoo8hlvNpQy_50hYilF8h058vxp8rVs71ooCMU6doca2QfBqt0GY229aSF6kH_8xVzFNqjrYmuDPUnfjFkWL-6OP6tqpzt8xCRY5IusB9Xc2HLjTTaB6YUNnlVD2MVN3CYHI3EnYfUrwJvbNDrx8U7axWH6wBIe9zRZj53rk2P4NmD5TDZnr0cCiLNdTwfIjWSxgg_i564p0Dpejvy06XCHwh9NxG38xuVz_XjANsVo5CFDAzQcWlGc6djdaw8jmug9GyrdVV0qgwLIdIqR9G57YcjBluWbLfRJsleJJOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=KpC3GndiRYUIyEw1YDXIl0o6f-VYGkd_12aUOWzNChrUX39kLoXi0tPq_uEoaoWHVtDVQ5ZQqTQkKR9aa-_OgvUODTHNg4fxoKPmk6PzaIAspG-YkB7fMm9Tr_uxnaxF6c-S-R9y442zzFDxM4OMdBQWrMrlPEeIFSNHo6hM1sx_xCg6Rg4xnUg3q6KzkZsaiCspstf41KFfb_8h2LgxA5zWnfOrh8ijx4sz-o1Q411-afg04n4sgNWlX8kzPovIMJmiz1OBEu4fedT6yvY03f-7UXPgPV3hDocO5dt_HW934Uxn5CC3AhwoxkfSIeTwwchpq21cervB5FfS4q9i3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=KpC3GndiRYUIyEw1YDXIl0o6f-VYGkd_12aUOWzNChrUX39kLoXi0tPq_uEoaoWHVtDVQ5ZQqTQkKR9aa-_OgvUODTHNg4fxoKPmk6PzaIAspG-YkB7fMm9Tr_uxnaxF6c-S-R9y442zzFDxM4OMdBQWrMrlPEeIFSNHo6hM1sx_xCg6Rg4xnUg3q6KzkZsaiCspstf41KFfb_8h2LgxA5zWnfOrh8ijx4sz-o1Q411-afg04n4sgNWlX8kzPovIMJmiz1OBEu4fedT6yvY03f-7UXPgPV3hDocO5dt_HW934Uxn5CC3AhwoxkfSIeTwwchpq21cervB5FfS4q9i3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=vpUgAdEzX0lTlTgo6pOT5-c6zIFyhO0Tt7N8R-xQJwt3aJY0m6OLcbHvSaCg4TY8h7QoUPJ1NtUrPl5zXkEtTs0yte1MNWouZUYScxglcSRBzi5oaHfxLqWvcC-s9AjZaeMV7SvcvmeFrI4PxmdCtQGjM_RgKB98ox-APTwK53BUZ4ar_Moji9gW-mDQajUa6KtMPNNkrKkes4k_2WBZSgYvxVNqE85loWjx3UL9VvnEx9t5E-E271FkzGfX-mvvu20m7Sui64n079subiEP8pEuOhSY1MMKLzFB0joYeVEnQUVt_0Bmm4E6UeBdF7o52MqETP39fRh817Lc87xG3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=vpUgAdEzX0lTlTgo6pOT5-c6zIFyhO0Tt7N8R-xQJwt3aJY0m6OLcbHvSaCg4TY8h7QoUPJ1NtUrPl5zXkEtTs0yte1MNWouZUYScxglcSRBzi5oaHfxLqWvcC-s9AjZaeMV7SvcvmeFrI4PxmdCtQGjM_RgKB98ox-APTwK53BUZ4ar_Moji9gW-mDQajUa6KtMPNNkrKkes4k_2WBZSgYvxVNqE85loWjx3UL9VvnEx9t5E-E271FkzGfX-mvvu20m7Sui64n079subiEP8pEuOhSY1MMKLzFB0joYeVEnQUVt_0Bmm4E6UeBdF7o52MqETP39fRh817Lc87xG3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=oUjUR5TL3tcFktHs9Jlyi0iPNIsyKdjPB-6IDPtgc7stu758egwZyMaXOxF2nJVAwI6bk9cBY2cLUEp3nVsbHUuLGuEIAPou17lL5uWZjkSYefWLe338RjB_3_RczJtL7bceIo-WAgbVqn7oz4bhFxf8rpx_f1b0l3nV4uUttYvavBWZ4_SheCpowPsSn4DEGRAM4aFMCLyKJG1GKdPLO3iqkbLk0OUNHYl1V45RkHIyYsE_LBei8l-i-vdSTZOOGAUMr_c3z_2hTGAJHTQzWxMjnvPNu_RnsXIO3Qm2cHDspCYC4zWKMBqh_xxbWtSEKx47R5ma7zKTZzGZ0fkVng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=oUjUR5TL3tcFktHs9Jlyi0iPNIsyKdjPB-6IDPtgc7stu758egwZyMaXOxF2nJVAwI6bk9cBY2cLUEp3nVsbHUuLGuEIAPou17lL5uWZjkSYefWLe338RjB_3_RczJtL7bceIo-WAgbVqn7oz4bhFxf8rpx_f1b0l3nV4uUttYvavBWZ4_SheCpowPsSn4DEGRAM4aFMCLyKJG1GKdPLO3iqkbLk0OUNHYl1V45RkHIyYsE_LBei8l-i-vdSTZOOGAUMr_c3z_2hTGAJHTQzWxMjnvPNu_RnsXIO3Qm2cHDspCYC4zWKMBqh_xxbWtSEKx47R5ma7zKTZzGZ0fkVng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n7B4oE7v8Tu6b9HqacrSzv_StDPlxPqiBZr9tQCLCk-LvkdN1YJlXxCEii3vPR1_Es11ikUtrItDnUIBRfA1W_T4IlsgyRf7k6e9Q2fiIXC2mYVUii_eOdyHATXkbF6fkPpzsEuzfV9g-u4P_yCiCuMJj-mafYP9MzbAYDt1wyv4x3_sJYrRzwuydAWtwrRhOO86U77CsHmhHsYFTVtaen1oic-oamhxZstq2K_YNjR9TumjCydModZVViCwPfvO5i0XmAdYQlVxPn3Klyaz2IHLI9W6bvdlMokxqsobR4936r_STFeGtL4BYSWqLKv0WAEw_nAJrCqiDgiLzhsPmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=NnyfnN_UZHN4MrZ4yC2-Lxl1GDfkYrCZ7UppVkFkrTdvnZ6L7welmGnHRuB4nzVzPYIuISRuhBbikUlt1RGt4g2VPcctmTgPORfjj8ZJU3VJGiZv53L6D1qpHs_Skczz-I9-F35_q4MX-RU9OgXib6GMfdRNV3mxfn8aMlfmae8FOowbDq9K89L62rFPuB6gptXJkORxE8tARVH1RIk6kThnnR0pQlcwLx2FRD8EjgehrmmtLPM10nt1ddFtoUeJ_IztI_nCuXzAXJWqBJUPKucV4UxRFzx83Dz9ZsDrRO27qYBISpavphP2TXV0ZGvae4ZHwQUvjvNWl-fcCIfOJDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=NnyfnN_UZHN4MrZ4yC2-Lxl1GDfkYrCZ7UppVkFkrTdvnZ6L7welmGnHRuB4nzVzPYIuISRuhBbikUlt1RGt4g2VPcctmTgPORfjj8ZJU3VJGiZv53L6D1qpHs_Skczz-I9-F35_q4MX-RU9OgXib6GMfdRNV3mxfn8aMlfmae8FOowbDq9K89L62rFPuB6gptXJkORxE8tARVH1RIk6kThnnR0pQlcwLx2FRD8EjgehrmmtLPM10nt1ddFtoUeJ_IztI_nCuXzAXJWqBJUPKucV4UxRFzx83Dz9ZsDrRO27qYBISpavphP2TXV0ZGvae4ZHwQUvjvNWl-fcCIfOJDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=hKjWJyDENR5rDeFhU9GRz0ZAy02Dp0JbHeP7TozlrlPSJBWUixSeclF7MrNEg0P8wmt54ZZWI6V0ay4gkbayNzBXb41G5aCY5Tq70vPPsMul5hsiXxQ68_VJZ2NmnB3CZmzqgaQJ-ufPrl03hssnqvQeMUEp6vDMs4Bt1JCnWQP2oQlJ0_9_RLVlBSHFb-TnCI8eHB3Lgz7OCVoZCFokT4QEJ72lI7MT1ENx6Cpyg9ZqdQUyesep5tkoZcDAhJ-kkuIDCKIBJZa3muSsXoJO3LcCZ-CEB05hXbVibeavpu4y7bBwIwaJtc0ABCiyaRHtmFkcnWLL-ToIoxlQueT-ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=hKjWJyDENR5rDeFhU9GRz0ZAy02Dp0JbHeP7TozlrlPSJBWUixSeclF7MrNEg0P8wmt54ZZWI6V0ay4gkbayNzBXb41G5aCY5Tq70vPPsMul5hsiXxQ68_VJZ2NmnB3CZmzqgaQJ-ufPrl03hssnqvQeMUEp6vDMs4Bt1JCnWQP2oQlJ0_9_RLVlBSHFb-TnCI8eHB3Lgz7OCVoZCFokT4QEJ72lI7MT1ENx6Cpyg9ZqdQUyesep5tkoZcDAhJ-kkuIDCKIBJZa3muSsXoJO3LcCZ-CEB05hXbVibeavpu4y7bBwIwaJtc0ABCiyaRHtmFkcnWLL-ToIoxlQueT-ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q4EgTcwdqw77XzbPr4m59bVyZXVBr60oEHxSKIOZbY4qupjZEMa05OJT0Ef_Q6ufpCgEj-YA7gw2aE02i1wohzeKOFK-xG5VdQ1GEvDk1q1C4ZMKsdBPmYwtFRKj-DKGXyVhD5sxBbepImDa2E3B8WzOciaDYYhzXp_frNfWT_q-3PjaqV5NfjLdYFhdci2CbcspgcLpn5ZTck4IZa2ImEh19WAjP9Qv23rrImwYYnfxlucjy1WjxxXiNsBFnZ3tXUSWOO_LIsOzNOgDVHuaoyjAoNq7gG3RQtRrR75l_DcmC7kqRKcOfSgM4RfcSrHlhOXIincfniRH4x8cIFHJQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QDXJqrQmDmbJFuD4gFF208O87FrxzdKxlfF61t7w6LrRZ31PobRJDwiY2fVzeseGneDBOQGlxtfcIPuVgKewLHOTWVvm8vG6Lt-hU7LTYctgXOLssGcRgb-d_Rfl6LDmL3AruB7vfB2goaT6_KrNdFJSD8o3lx9NAehFZC_CZe_hyEFdse76Ce2vsGhBuVjUqxLhyZmAwRLZZ6kh8jde7Y8vUKRJMQ4TXgiQO3JDgPKRP_z_utJXr3D3BzoR8JULzepcOzbOKevIi5T_xeGy5yjO6aPJOMd0grmeGcuHRq9PH-jlDWYFz5trS9RWVlrkCd4HrvFV0Y0N-OhASJ-XVw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=iJgcG0qIHyoqfTR5YOSBdiJ_Yn8cQWnm44bTnRqzsYuHIErS53DrpuOiVrtH3Jprx_EirweGQFCARhZ4ICZVL-K8R4FsOTP_uo_C9iFHGbMDXNChkaiWA8GOu0sioCxmL6fPwSu17EtBW1bZVfNn3lHHxI0P7mF-PkPHpfyWueMV_LS7R-2bxpHgp3D9k_VO6BzA8gaiZi_fQxd8vX7C6EKIGeJw7Xd-I2chuhSy1-zI9EnVDhhEUxbIFQSHUH6JA8mXRDhNtR9AZO439St_HnfzPLP1Y1zLi9JXX35g8l6hDN9COrQa-qz41kN2PQfckzqYj1vDKlZ5Jemt8IGdVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=iJgcG0qIHyoqfTR5YOSBdiJ_Yn8cQWnm44bTnRqzsYuHIErS53DrpuOiVrtH3Jprx_EirweGQFCARhZ4ICZVL-K8R4FsOTP_uo_C9iFHGbMDXNChkaiWA8GOu0sioCxmL6fPwSu17EtBW1bZVfNn3lHHxI0P7mF-PkPHpfyWueMV_LS7R-2bxpHgp3D9k_VO6BzA8gaiZi_fQxd8vX7C6EKIGeJw7Xd-I2chuhSy1-zI9EnVDhhEUxbIFQSHUH6JA8mXRDhNtR9AZO439St_HnfzPLP1Y1zLi9JXX35g8l6hDN9COrQa-qz41kN2PQfckzqYj1vDKlZ5Jemt8IGdVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZwKipSsKt-X-Ak48vFCZNQI4_2-aFfoVFCkAS5Nr3exEDeK9yxvho27Y79Rn_lsC68LVojqYZ4g-LkYAH1YYBbDqZi4DKEl8e0nXd3DQLxjSyclAPDmxJVQksO65iOPQ8IMQXMc1JXXwYm8AShwO3sMxSAj7CtFpZRaviirJpym5HQkdTreW_lp29ux2cUG_98mXsZ9akmXzCnZEGtNsiy0nj9hDXcmzI9D_XVw2yV6Vdo_AzkukcY98l8Lf16-CLoPBt8JOIERKj-N42foCYtgHv6mXUyIrS_yuOJjchLaA-9G-OjLDo2cwnYFQOa78fh691z0bxR7ytdQ8HoY6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TEwEgqTZk95VWvifPZS0OKr7cZjo1fb-maNhhlFBbly_EshWUHOEmALz_UUYLAntoY8OhQP0lPJuQKQOocvXf27p85OOjf9KiTrUSxklvTGGf3c6c6LcUAW0W5cDxiX4LCQRAkMYTwKY3gzPLPkin0Vx-7XfJhG6lVF1IwDd3A9S0-skDq_TPmRh55ER5xYGg__k20x1mvnsWNO8jOkxf7o-uakHP_442sjXFgIGJqNlTxoN2NTZ0j0uK0VGaDJE8czDv52EtOWhBKywduDtHeVeEJ344X76l895Lov8RU-RJiqxiXMXItB9eH1asZswT2nreUWKL7PXrE-EauxCEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aTwuZRrhrY1w_7ioSPbmk_cT1Y1H4boe_EnZbL9kL2J7ret3i7GCwj0CGk6NvE8pc7efSzptLE1WoexCkQF7V6mnH_B2IkmCZNql3rg-bm536pGAouL2ooHkaC_S8-CVtIK1bmY_QJwSw3ugHcT4VQfVB2N5Dg-r0RptnPq-lgrmfQ4EC8RuubcGD3uHSlqph6Zen2M7cSnXL3Z0LgiXvaim-mcbT5Vyt5F3vd-KcnI5Q-9MLEsvH-4SRSDaxHp6D8wOM3IoZ-rmjO6pypiEHbf6I7Ypo9vOnzlhVElyZhOx9dBZHe_PrCiAF7RpPYfulfLaC-DMDT-Egh7lArJ4rQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=r9_SWCf1zfg_E-lS9ubLcczD0g91il4-HHKY9WXtS6WUwfTvnhw1gx_mkOec_uOSFswT3evdJwjrCIEgQuJjY2bsCmO-Ux45A4lmhE_rNsghJBgKmOekTfanbPuQ8xA7GhSKyX-Rpz-RcLKWBMXuVkAqls5-0PT2pNso9fbd-9lfWRjy8vODi-8c8e942MU5LO-tPeNMivog01hD71eNGhJG1N3cgGy-Lz5fXKEUoB7pBwl6EgK4mHqqX04nRHwZU7FPdCTwPxXIYhR2twD5XRwGFmRVpLjkWj7f_0yfprhwQGGdheL2WYmap2031hy7O4O7Yr865hyqlJqE_Rw_GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=r9_SWCf1zfg_E-lS9ubLcczD0g91il4-HHKY9WXtS6WUwfTvnhw1gx_mkOec_uOSFswT3evdJwjrCIEgQuJjY2bsCmO-Ux45A4lmhE_rNsghJBgKmOekTfanbPuQ8xA7GhSKyX-Rpz-RcLKWBMXuVkAqls5-0PT2pNso9fbd-9lfWRjy8vODi-8c8e942MU5LO-tPeNMivog01hD71eNGhJG1N3cgGy-Lz5fXKEUoB7pBwl6EgK4mHqqX04nRHwZU7FPdCTwPxXIYhR2twD5XRwGFmRVpLjkWj7f_0yfprhwQGGdheL2WYmap2031hy7O4O7Yr865hyqlJqE_Rw_GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ناو آبراهام لینکلن بود که ۶ ماه پیش
با ۴ تا موشک بالستیک غرق کردن؟
خبر موثقش رو هم  صدا و سیما پخش کرده بود،
خلاصه دیروز رفت پاتایا  !
و یثبت اقدامکم فی تایلند!</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=UvE4o_M1rVBkp8gNtpfGKD3LuSlOlhOuWk4zw49U1TED9VKYfBIQhDgtQKueXJ__udu1JkcY3wguuusGe0aAC1i1ZdkTD1CzYS-L9E3-Gd_0CaX-4s4tbgdHHqI6qWVcAAft-_l2uF0JZUfYZIVVFtdUFRLdJFvOUleE4o2sP9waiAyohlfGY6z1ZfcWIudiC_tHQ_ZuCz5rk-6_OtgfvTn6o43WvlWmfHUm_u8wEuNt4ITMT7Js5KkyZ6k3FGHM42L-r_b2tmP76SaEjGM_ZpgnGQbCJA4i1MGJVo89oV4pEDcPfnrul44mwvsrAPUlzfqUhN-qd3qWoq13kN1GCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=UvE4o_M1rVBkp8gNtpfGKD3LuSlOlhOuWk4zw49U1TED9VKYfBIQhDgtQKueXJ__udu1JkcY3wguuusGe0aAC1i1ZdkTD1CzYS-L9E3-Gd_0CaX-4s4tbgdHHqI6qWVcAAft-_l2uF0JZUfYZIVVFtdUFRLdJFvOUleE4o2sP9waiAyohlfGY6z1ZfcWIudiC_tHQ_ZuCz5rk-6_OtgfvTn6o43WvlWmfHUm_u8wEuNt4ITMT7Js5KkyZ6k3FGHM42L-r_b2tmP76SaEjGM_ZpgnGQbCJA4i1MGJVo89oV4pEDcPfnrul44mwvsrAPUlzfqUhN-qd3qWoq13kN1GCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=CIuh0exALBRYVdpZ4Vdgsexbrt8h6LCncP2xMnjx5YD3yNlzbrfJelXiTMS5UI0z5AWhgFV4ABODUMnxWntLqiOHDD9o47YfisS_2U_xp-oo6LA8uSP-iwyvzRY8JWXPePYmTe-E1tjWr4JbJuPIkbF0njY15-ejFvl5zjn7JTaZII3s8_IKQa-7SUuhy4OCh1vqnp6cWvYHHI1AMBMHNlKV9M_tgG48m4__V_z79EFuI2DB2Ryim3Tu7-0bOA9oDgmaRzxXeeOTDJem6lQqwz0sgqI2nFk5V8rdgWZE-AuqH6CupAduJ4Z-gGjw02vGHFBDSUMv1o3UMg5HSbdzTzXDjFl3DTmtTYg4dBMq3jWuUokTZHH8vZPGZ4wsx5S5kyVD1DdKGiMKOVsKO92nm0d2A9h4nBvep6rIgGC-B-0cTQwoX99IbLIX5lBOqxLIQgRWE0kafCHf7AUqH7IMVoznnbo3jvfvm-zsaBqU1ahbiSnPe_a6R8JcjfKEl6COUDFJRHP7H-PSNJiNM9OUgSE1Fa5AxN04D0EvjN_Nr6yngset_gB-TZrPUgE5xvvyRJY_l_Jwj47k-yMxFA2rXGil55Jaq6kV0edfk4te-DLOJPlWo31iR37KB8-iMTBOzKFqAIdZp9yuJfQOaEPmnYB9Lx7AWIHzeNS4_1NcoD0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=CIuh0exALBRYVdpZ4Vdgsexbrt8h6LCncP2xMnjx5YD3yNlzbrfJelXiTMS5UI0z5AWhgFV4ABODUMnxWntLqiOHDD9o47YfisS_2U_xp-oo6LA8uSP-iwyvzRY8JWXPePYmTe-E1tjWr4JbJuPIkbF0njY15-ejFvl5zjn7JTaZII3s8_IKQa-7SUuhy4OCh1vqnp6cWvYHHI1AMBMHNlKV9M_tgG48m4__V_z79EFuI2DB2Ryim3Tu7-0bOA9oDgmaRzxXeeOTDJem6lQqwz0sgqI2nFk5V8rdgWZE-AuqH6CupAduJ4Z-gGjw02vGHFBDSUMv1o3UMg5HSbdzTzXDjFl3DTmtTYg4dBMq3jWuUokTZHH8vZPGZ4wsx5S5kyVD1DdKGiMKOVsKO92nm0d2A9h4nBvep6rIgGC-B-0cTQwoX99IbLIX5lBOqxLIQgRWE0kafCHf7AUqH7IMVoznnbo3jvfvm-zsaBqU1ahbiSnPe_a6R8JcjfKEl6COUDFJRHP7H-PSNJiNM9OUgSE1Fa5AxN04D0EvjN_Nr6yngset_gB-TZrPUgE5xvvyRJY_l_Jwj47k-yMxFA2rXGil55Jaq6kV0edfk4te-DLOJPlWo31iR37KB8-iMTBOzKFqAIdZp9yuJfQOaEPmnYB9Lx7AWIHzeNS4_1NcoD0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=PicMbSSGm659Oy6NYs-bm7r5fNVVatQsXo4sU3qld6DWYrAzjJYAuLN5sSPseKO4eyEd9HjbVMIaCUtiEDjPL8xKX7i7pKNgRXf9LNRVhfTnM0wr4GVryB8LTm3BWwYp3NyoRUkt_F1uhoxSuP4dhiG-QBsBX3CUcVSqq4UH6LxT8FNOMkZvhoGdtU_qTzIQdudcPUzWMYsX6bA_ngK3c23WEkB7YaUCA4jjEny7eBmyF0P-jDOiiVQm9JCk9YWD7WhKuN6vCi4vsBECzXnqkAQoC9Luf4QzfMCDP9bwkmxQtSYfnVTPikUSUImPn-0FbJUNPxhPfWApszMkk91z3Coj9Lbe1VsaXutWFCTv3mMuVUway1FNeloL6qj55lb9OCkhQHpF3BCEoievvC1bW-9NnGllMkKXR13LH_Q4WwqXU1tjC6NeGsGG0ZvITOfXX7iTRRosqBro0MmX-iUAPEu4CjRYFuITyWqYxMlgFuly9mr9sBN9-y5KSc54pDMHb2yAd0y2VmPY1IP1xrNyl8xuXk5Fjy-u5Xo20UWzEix7R3J5fVj7vf7lhf-F4wbamt4Y4EOEENWFlkB-Eok3NKSSegHwIaMpY5L1Tip65TbUnQrgvwiF9UTCAZ6womeWeAQ5deBV_hCuRgekwQUga7o3Us21dfI1YY3HplHmhqY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=PicMbSSGm659Oy6NYs-bm7r5fNVVatQsXo4sU3qld6DWYrAzjJYAuLN5sSPseKO4eyEd9HjbVMIaCUtiEDjPL8xKX7i7pKNgRXf9LNRVhfTnM0wr4GVryB8LTm3BWwYp3NyoRUkt_F1uhoxSuP4dhiG-QBsBX3CUcVSqq4UH6LxT8FNOMkZvhoGdtU_qTzIQdudcPUzWMYsX6bA_ngK3c23WEkB7YaUCA4jjEny7eBmyF0P-jDOiiVQm9JCk9YWD7WhKuN6vCi4vsBECzXnqkAQoC9Luf4QzfMCDP9bwkmxQtSYfnVTPikUSUImPn-0FbJUNPxhPfWApszMkk91z3Coj9Lbe1VsaXutWFCTv3mMuVUway1FNeloL6qj55lb9OCkhQHpF3BCEoievvC1bW-9NnGllMkKXR13LH_Q4WwqXU1tjC6NeGsGG0ZvITOfXX7iTRRosqBro0MmX-iUAPEu4CjRYFuITyWqYxMlgFuly9mr9sBN9-y5KSc54pDMHb2yAd0y2VmPY1IP1xrNyl8xuXk5Fjy-u5Xo20UWzEix7R3J5fVj7vf7lhf-F4wbamt4Y4EOEENWFlkB-Eok3NKSSegHwIaMpY5L1Tip65TbUnQrgvwiF9UTCAZ6womeWeAQ5deBV_hCuRgekwQUga7o3Us21dfI1YY3HplHmhqY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=Lv4EOl4gEGLGD0waRhNTL7dKBMwRLkg4ukEwWQ0FPAtRK6htMuPssNL4ocZwnOP4jk-PfWGfuqCAlLsPa9_UdBHPwujNxuoGYpLmGdvvclIDgz2cB7Sp5sNNB8VUY1BcMlU3CXEPgnEGXC5lxIISs_omrL2B4CEURNzEV5R1b-4npQSakgwdzN9XPpBHCT_m5Iokfn1WzXwcsHWtdDvEqWSQbHHX12AUeUzPFfLyB4V7stqpfaCf_bU8ytSCwkNxn0QKYW5cdTklvdPsPFxCZ-Lb8gI8BaHRIKOdq9mpaWCd5CQm_5UNOEvhv-SPUr8eCvsAUWQVRPLqgR4BCS3ieg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=Lv4EOl4gEGLGD0waRhNTL7dKBMwRLkg4ukEwWQ0FPAtRK6htMuPssNL4ocZwnOP4jk-PfWGfuqCAlLsPa9_UdBHPwujNxuoGYpLmGdvvclIDgz2cB7Sp5sNNB8VUY1BcMlU3CXEPgnEGXC5lxIISs_omrL2B4CEURNzEV5R1b-4npQSakgwdzN9XPpBHCT_m5Iokfn1WzXwcsHWtdDvEqWSQbHHX12AUeUzPFfLyB4V7stqpfaCf_bU8ytSCwkNxn0QKYW5cdTklvdPsPFxCZ-Lb8gI8BaHRIKOdq9mpaWCd5CQm_5UNOEvhv-SPUr8eCvsAUWQVRPLqgR4BCS3ieg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LR5wcuOGgor9jLJC5KvYvGKcEm4D69HYiGd7Z-vyMYLC29-EqDSCLSJa7Kvi7JQS7ifhKZffDZIOXhdgi3D3Xqd2mu6WdxTh-6I6uExPltVog895n59HTngpr4BhE9GMxCrRGa8ScGVa94i4HSCAlnH54nT1S-a2tlNQr5aX5IbgHjza-nvqIHM1w1GPMFCLeJgwpqc5RZ1ePTTmsPFmV9Vb0enCo4chyipgkAF-S1Fi2wQswnXYhycdF7OM2IdVoD45WrSHOfSQrsVy8_kUSGdhuijkfasRRvvJo8rysG2aRA01Z3OrINmPFk5oGCfRYC6FpcFtJpMvyZGJXF2MqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=kXq0H795WvuUlsyrbIDI5RwNEf6Wva1_rXwqoCVJPqd0XiPMYD6R3ZYPrv41SEr56mtglZFhj30XN0tg3UxmKu2zaCMO1-XHvnYSoXuVtH6HBwC3bw1EGlRA1otY5vy-qf-4p4nGar8NgdCWaAb6gtz7ceETs1fTbzxkuMyeoqBphVbcWYO8zeCjnb-laP6ifupSDTVP0KJ9NaQocTV-HK0PF7OpF16P5J-6c1e2nXABPierULCvAXG96w5Z2ZlLSNnUh31xRs2aM36HndlTYWZykFgDiB8wmlU42VLv7ZJ5GdCJwiCzlVNdHNzGMcv5QNvwJHZxPYfqZI74DmC-iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=kXq0H795WvuUlsyrbIDI5RwNEf6Wva1_rXwqoCVJPqd0XiPMYD6R3ZYPrv41SEr56mtglZFhj30XN0tg3UxmKu2zaCMO1-XHvnYSoXuVtH6HBwC3bw1EGlRA1otY5vy-qf-4p4nGar8NgdCWaAb6gtz7ceETs1fTbzxkuMyeoqBphVbcWYO8zeCjnb-laP6ifupSDTVP0KJ9NaQocTV-HK0PF7OpF16P5J-6c1e2nXABPierULCvAXG96w5Z2ZlLSNnUh31xRs2aM36HndlTYWZykFgDiB8wmlU42VLv7ZJ5GdCJwiCzlVNdHNzGMcv5QNvwJHZxPYfqZI74DmC-iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=L2hlu-UZdVIf27R-8ly-IsuWeIeiXDZKG9wl_PP0TZZHHmwW6LyQ8oI9ca4zsvhUwc7CVxTyl01Kzf8m1IZAcTCeer5lu-kzN3KPWyLD9COfqnxzOVQPTxmqzN9RLUgJv9JLmTX9iUYhtp6G8Payrq7cHMvjWNnrQ7VJg5187kTTjGDKLNzNCm-yAsf4kJAzgbViDOvZXkFzdxDNmanBRkvPRm43G-4-H9S20dj8rcEJZvqmQiAVqb2tAC_5XKEKRkXPNzktFQA_RL5qCD3_SZ_ecT-LaUtZTUV0EOJvH6u9vjnfaX_sqIAsHBeyBYHoW9sgA_2ns86LEL6a5vvaVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=L2hlu-UZdVIf27R-8ly-IsuWeIeiXDZKG9wl_PP0TZZHHmwW6LyQ8oI9ca4zsvhUwc7CVxTyl01Kzf8m1IZAcTCeer5lu-kzN3KPWyLD9COfqnxzOVQPTxmqzN9RLUgJv9JLmTX9iUYhtp6G8Payrq7cHMvjWNnrQ7VJg5187kTTjGDKLNzNCm-yAsf4kJAzgbViDOvZXkFzdxDNmanBRkvPRm43G-4-H9S20dj8rcEJZvqmQiAVqb2tAC_5XKEKRkXPNzktFQA_RL5qCD3_SZ_ecT-LaUtZTUV0EOJvH6u9vjnfaX_sqIAsHBeyBYHoW9sgA_2ns86LEL6a5vvaVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aFgJGsaIfWOF9Q0LnO9XXLHGkqgkY9CizfIvw0eiPg0UZKrtWyfjQvwQS7cXHTxUN6pIGUtOMcD3WA3IAf6xiEewdWu58zpSdAwArmMbgNayUzOiNLtP76la0z53Rsx7xo3UfReLFXOeQw_83PnWTtk_qvFugZJohzFzekOFS20hQGfMaMicGT0u9c86NsAXtBPGE6iHY-vxXBRWFbUfoiWBAvDlipkffKjh58-Mtw4vkstF0C3PQZi9t-lxWXaZo71TlGoTcyVceYK3AzHg2TSrwaIJKFCsT4e_ffcGLdsOdM_tIdoH9pI_ZlEyEmTfmSO6NG6hhUwGhsn832x88w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wmbs_bipwyGoAiWp5-Hgmu7FCyNoJcM9OQmS5ZwBzS5KbCyhODF9SeSs1FHABUtyqYLkqDMjAafnx3u0zjRJsL58-4cfN23z0VAv1smFV2ZbijR5tmzcwBC06qjXTyfQrRT7VDPEfCngPc_o25dyc0fw-OifJ4UZENOE_k-3LRa8G3TOP6t0otraAt6YAVh20b1ktZW-tI1xB2OYnGb-sl8uSxiqrdDVuMYXz5Ts5Wk_jvzQD3ePXxUrolAbQyUenQhwRCxOjZD-a5BEJpY_tpXVRDIkDrUxeQFKyQ8SjVm7h1B8tC_v2nNQmpxZfFtJcmMBDY4sHt6Lcrty6G8k3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aM9LrdI1Fq8MCUOys91jcIHquPCW7l3UK5m_hmRPte4dxOGmO_FPeOeEy88YFMs1oqHcjt3kVCEPwx6GNVNxHo7INQqPkXWZYZvhf6br8VWeDFbVAA96C6nRfbQf6Wd6bylyyta6rXE3McLmvxcYcc8BgPdR4zCENO5oB3Bf9_MLzxLKRjbZXo3NqFkr7SpX-NNPpa87vQpK5SJBYis52dYziMO2mzsDUlztx_QWoCpexjm1uMQymlqAVIRZdJl0jbSEPSAMBLhYl6pSidIzdHjKgDtQa5v5ohD6gyybdwRQh5oWowcBd6y49aKaIngttCf1fWdVSgeaIi0ylvwo3w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMmQGTgF-XzXRE8ZBpLKV6xCtzuTfWZB7bOyAMK71V3ZrFNFgQ9tbZ-LUqiW_dvGr7ovtEJp_UWE2214za-YurBtmOhGmbbAQ7Wt6p_ByBNGTOcBumj2Z4eg7Yx3xqEb-es3VWwxIBUgFiHje2g0VxV8yoDbKGQ5LBzZQHCSXsIjFqKODnuWMvvMz58L950MkN6kDBYtxYLT11sllfiJMy5K08mMBhxWHz-hagPoV_gXIwJnCjPrkn1H6l21tY17BFTeoAaPHPHCZBXqxGbPbaLtiJtXXzdOj6AxxRj1SxX1OJ0MjK2V3YctLr6bz54u9OEeTpdk0lR006X1k6IsRQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dnMknphBnCzZ6-QfY5Zy3MIwZkGuav9cYhLBNLqDhHP2a6pp-3X6vsHg5kHUMmUQZtaB5OWN72ZbGP3ly5P34PPeku5wla0d9TwyD-xA0oCN2TQnR-UdSmr5HcmpaSL4SiNQzdAsKaNMrAmjpXTiCmSr1d4Frp2IidPwAx3JRrxxpYsjXqY95A4HECTopzx020fULCbKkZb1zosIdsdXaZWeWZWr9JUMtvSk4JBAXetMFdC_49mEF4QQEmgSRY3NiiASMO5ZGwL1E99gW9PdJoweAOI4crkujO1yDQ3DGPpzkkEIBRjT2lUmmCNVLbcd69OhNT9CjuK0iJJnFiQdJA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ofezz8bjnbSR5DAgMqLbM8waybmkq8_V3uVZApXXStKL8iLC7FijpBS0R1Tr3pXJPWhvSPq95og0gmy_SueT09_-UnA56WQbfsLDQfcUmWAFbb2kWLGhqIAYd0eyiZOvJtkaSwewp9RoS_FeY9dzWKDWA8WsuqheObScQLVrUYT3hU-ykaCzOAiyHhpu-8-Y-0o9ZL2nozAbFhEHP3uHDFBqtFtkbdxbY35bExUSX26FUCE0ImuEPWS7uJbIpORXu3nTJeJWPI-POnaKqQDgZ15FodLYsrzTOAP7HE5S0q7H3G90XXXAg8auVNZ1mNtgKy73_eIAeBsRq3SSVKriUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/phrIBTg2Mqh0bzv4Yv0y-BBxJQzGpARGJJoh1eDmG2YK1LJqGcyCnvFTl06YdIJOHDzmM9IhMA1rvouBx4OtC9jDuFKCm3Q5QnsknkxV30avgNTCdA1Pa3azP9y2QkjZqwsoIIwNGpv57jaUq8wtNlvSiNtJiTqdISKetMZduiwoYbzF5l80d_dIrjMbvvrD1h1y63Wc7u9qkjwddC5fHB7RULnLmL33gORULxVPBCCXvCXmQV7aEzA7qWDj8Tgh7ooVrw4l6XGM1yWAf0knFbYs01n5vX612FIVNpKXge7V-rmlq9mXf3ECMeG3LW73-4DrDYk8ieJpyQRd9MU_2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UrNs_hr5n_KKSJ4G1dS6yxqbAGsiWgxwjUuAHXFhhpshN7r5btNpegtl1UDAAkzZty3rl2lZt4aG_WmgEAt6Y_j9KC-T_6ZJDcgxdnjGOnFxPL3wvl15JDSXkBAAn16YV-WmRlK3FSdhuQiFvn42Gj1iRvnNwYXi3mtRM6ip9eiIBIIZJF24bzPI3BDn9_Ykd4gt3iCjP53-HuUGGUvJU0_h1qI-dmDBublH_vtYiZoCsZLailVXdc4PjJCmSiq88ha_oc97iN6_97CIcy_opwYc-K5ROLzgbyfZBiwB-P1Grui2ohLhiqx_eI__9QcDFivdNhEaDIM2RhRCuOAOzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eBhO6i2Z_ZHoJ-XOt1W3Tc8q4VS-MXLz8UZA1Ap-Snpi4LHQC46yE0NLe4HXy9yMmJ_SyZZPop68J0JqrN5XDTr9OeSnoUaEJtXiM4Qn9G5E-Zm3yOTiNuyw4d_6vU415kH6--sfjLNoKmMTAvKyXJ6wJ36YkRZXM9KEiA9YuTUmU_PBqPWzLeeCnjnswOXLTuo9a8gwEO47OK9WVBcC_PqCXIeFuxNsPjR1QTav8wrmyEUgWtQpdC0qec0SOCik4Y292VbNs6KDNsQBRMYhGRYTP0FasliybpZBTwecDiAt4Nhr15GvFzflwv-Poj7qSb-K2B6X64mj8Rus7Et-CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CNxtB-Rj_BdE32fBnsRWuK5OStK7srhYAcWf2dt_zilqcvWgJVdXi96zImLD7ArQpHOVE1vqmtwvo3vBF4W_qEksECLJWFlBoksnqk91IhY-lgWOKN9r_k8VzVRCz2UGWV78i_HTX6bOSD67owKHajyKCUH-TbUM31RYajlQ30jRUPngtSo_lsh3p_dIbRZvCmaungDkpBxNsjDvX7HUqEkeIbabfKAqL4_YA8Z4vlkYkK-FMc0muo4r0nDBqf6k-sKS05b_VY7nIieq9ZdWLQ_iUiKx4tjMM2goedCFIvTG4Am9MPig1DuqyAGqmgkSb6tsnrwNP6PZ2wwfNI5qgg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6668" target="_blank">📅 08:18 · 11 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=Bbzn8AaQeH-6kspcpkI_-O2YHa7-T60wDZEMXQeRESje71geGSL8qMAeldaEn3PKGYIYibwmCn3DJ3274MbYMDH9SRP9nYfEo6o9h-nGVORYQVbnMp67L-s2EY0uBRMIVZukObexPSLdiyEC2GFYGKLc3Hy9Q8bF041JcqFNfYE-jfWO-nzySVWmdPAYJsYY4wdG1RpBzoSNfCbp3r8ugg2qNMLKMkc6YG0pcXlcA52D4iq7t9QLME3yoopvQDP5zmtL7dzPIBaO7lIno6pbjNIfnR6qpFFDK7z2TRc10sNHelBBpuoX8Dpr2SlgHrwooUf2gjlsWiNAcHR4Cw-bpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=Bbzn8AaQeH-6kspcpkI_-O2YHa7-T60wDZEMXQeRESje71geGSL8qMAeldaEn3PKGYIYibwmCn3DJ3274MbYMDH9SRP9nYfEo6o9h-nGVORYQVbnMp67L-s2EY0uBRMIVZukObexPSLdiyEC2GFYGKLc3Hy9Q8bF041JcqFNfYE-jfWO-nzySVWmdPAYJsYY4wdG1RpBzoSNfCbp3r8ugg2qNMLKMkc6YG0pcXlcA52D4iq7t9QLME3yoopvQDP5zmtL7dzPIBaO7lIno6pbjNIfnR6qpFFDK7z2TRc10sNHelBBpuoX8Dpr2SlgHrwooUf2gjlsWiNAcHR4Cw-bpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mI_NYG4NZlP64YA07a5ij16dOoifbNNjm1HfHwKlOpeRbR5Fb7XagM-xKhfyURQ5VhQ0XYghGaEfI4mj_HyFwSjiizqsTAoKc8K2nMTq_mQMuhGlIXPK0YncZw4znnUR7v5YQi92Xb6vTXHz2hqLYdjnPDYI6_guAd-jfLuU_eKb7UOge9KPDkjMURHoC-yIl8svXf22qJkBW0IdjF_kNbzvHayuFUgeaDCNz4q9TJzGqYctij4DwFNyeRQB6mCEEkbTpI6nuERwPi-_YLtPMlZ4zvs1g137SrzsXy9IoN_r0ty0RmnM9Ra6M5eLkb8qUtMYPiIV3vUp44LUlHoezw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qNkt_KNW1cAVdeM0zhJIxyfg5vEFq9z1dS0MedPmz1X8XuR_S9N0z0i03SdWpoMk56Zfy164vriwqvsdnPZl2l5Pit_4ZF8w0SNIFSAWoQ0Kf1HgrnJk0HVykXhL-BmJGHesQzn5cDL73lekwNZTrOHTGQ34lAER90RDNF2dTVvFVwL7_uEta5re9-VNQlo_YSn65hcj4cXE5bI_eY5x84iEmwzPj8ZQbDC4miAbeG_fBVQH2FULCCjLiIqacBCo5RUSFSUefAJS8RKvwOb0BpuXhhILV0B27AiGtHIh5pNs0Vsw8R5R_inOoK2Uub7NqBMDYHaEYR11szgMAYebJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=WUgTEGGWsTT1jQDYELzb6zy6egVwfUhSXl4hf6QiR9A7Gbxl8Hm_QBfzMm0JFwK-yzv8C0ERREH-oXjbRdEgjooLMrJeGvNirL8X627sB5O6XM00s3m1l4JQh5pgeDMfZUEK5nfFqKqNAhpLve09ThK48UpQyEU0M1ied-dbzGcmLvaw0VSSvdEfF_u8svPhYA6O5buSF-E6knBzSva4m23x8Xn2OI8VmxC9MzZR_52_-PxxdXt3noZ5k4dCjapW7ongLde9d6F5lXFs3GeqxPKYkUz4r2g9Eg1Tad3_hh80zF3YC-o_oNxvueJmC9STFT8PLWZruztjCC4xk5-g8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=WUgTEGGWsTT1jQDYELzb6zy6egVwfUhSXl4hf6QiR9A7Gbxl8Hm_QBfzMm0JFwK-yzv8C0ERREH-oXjbRdEgjooLMrJeGvNirL8X627sB5O6XM00s3m1l4JQh5pgeDMfZUEK5nfFqKqNAhpLve09ThK48UpQyEU0M1ied-dbzGcmLvaw0VSSvdEfF_u8svPhYA6O5buSF-E6knBzSva4m23x8Xn2OI8VmxC9MzZR_52_-PxxdXt3noZ5k4dCjapW7ongLde9d6F5lXFs3GeqxPKYkUz4r2g9Eg1Tad3_hh80zF3YC-o_oNxvueJmC9STFT8PLWZruztjCC4xk5-g8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=Jzp_y8AuV466DI0RR9S-0Q9Xj23Y1kz-BaT28O1cMEgTrfqGERGdyi0b-64IXzXuTmclJQ4cy8Gn9B887OCr7Oz9bAtRDXjPsmklu1CHvUtX96fjAnISUPfYyQA09FZUzqtAek932vXqVFdzx4gLVzHuaS5CAiXz-R1Cpff0D9gfUJkh81AnSIx-B1pONPpom-phNclXCC3TfNG1HplIzx6y1IPEPxaLoEnlIv-0Hyys_JsMK1LNUYAhHD1O_o-vy-K5vBhGZ79rIryCJl7RJY7LvinsoBMS4NvXWbk8pRoLJkX600H3sg5OKG_Dd2NGwS97shTCmeCtARkHepooqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=Jzp_y8AuV466DI0RR9S-0Q9Xj23Y1kz-BaT28O1cMEgTrfqGERGdyi0b-64IXzXuTmclJQ4cy8Gn9B887OCr7Oz9bAtRDXjPsmklu1CHvUtX96fjAnISUPfYyQA09FZUzqtAek932vXqVFdzx4gLVzHuaS5CAiXz-R1Cpff0D9gfUJkh81AnSIx-B1pONPpom-phNclXCC3TfNG1HplIzx6y1IPEPxaLoEnlIv-0Hyys_JsMK1LNUYAhHD1O_o-vy-K5vBhGZ79rIryCJl7RJY7LvinsoBMS4NvXWbk8pRoLJkX600H3sg5OKG_Dd2NGwS97shTCmeCtARkHepooqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GMc84i3L6I1u91GXgzzJvzSrmR5DFTsCqd1I1W8YFNLMLzRll9dk88ZREGsI2XPw4GbfQaOgT-g38CCJ-nlISzpcHTLpbIcxOt3hmQ0SpOYAa86Qof4YDrXKs3PYcSXFD-BcnNt5CuI0ev0GrZSCuN07k1qbiLTqDpBcWMie5BNgrNtcSBx45w-GYKJxy65fTmCS_MyhTI-WPetUNHq02SOqpNJbnmsujAA4yziFenp2XlL0b_ND_ARGR6xNu3BQxz6Z6SfIuVPj_MVEnhT_6wQMnbvDK6zVuRW2LMHXK66WCwmStxOE92f9B7HCnWU_hLUsgcc86M8UPcXjfiMsrQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UXn78GnDgXIoMD8c_oatggMahgxqbnrCkJ_KMQyaDpRxBEuCoaFR87Xcn-mFN00lN1i28EbtCGE36yqfsqnMNbSubrVooHocQwzoXxhcRM764T0y6PmlR_Dq1bmoedxhRGxmjvLL2tgvCB02ZzJq3B8qXGtM4ie9TrsPcBtaPxGKLMolxCVtVKkiZw0F9Tgi_-M1HEaQQoYZaB1LXF1WKYrDGvk9leN-1IqeKjWn1vqxQd3nPm7i_xDlbJXhXo_ftAW_b6I5qtuVdL3F5okxWg-9wVhAqeD29jH4yW8lkFyD3vK48cvjixhaxg4Gdw9seeht50it6I9gQB8AflTCcw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IkUuJ6kxpZyEWvjf-TzWv_-E6eWoMPMGLK8iZzDyPwugYNPAJZLWV0KmwfO8fQbS8wX9LnD-WMQnBiitV9oP5f9TyYXE7kS9OBK5835MXuNnaL9XkvE2ci8SYYFi3aI4qTEWTfzvIN-eaTHQGv-QwcPAPmdcQYXHMlm3gs-BXxqgIvJ4SSFhDoR3DftG0Qzv5hQ3zDmCoHL_-ak_EMnTMHvzyzaRFBuxZdfiJLSJa6Pa635rUvWjs4kLjn5N1FpKd9rZ_DxbRo90wUnJTzfwndYgWTd3Eae0LfwC-NVnjLrTNaxA9BgxW1znyaerLB8PzADtxGsNORaJManROF6OCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YfjOqMAGyHY2C_XebGp34LWHi0v5Y3RSpID87wcPVUFtWXC3RX_0HiVW1TVs8Skwa7GG1qErnk6Gy-0mX4PMkPhwYFa9wHRaLmjpQzLY0tFATInKQzQ8hFvwsHkwHbZ6KHLpSBXHw774OFis_dq-iBk8BRyGQUcSgkjreZb3B8hRHHbnIq6FrqijidB56P-cLIXKfnLfG5K85ytFcvQyrguBdz962T_0FdRW46QFXIKyEjmmu08Fc0qu74PMyncgFuG-CY0zha2iCIyk2utL8L1vbhQXtF39JQRZh7l6wnhm5FNVKS37nIZJTC2XMXEI28iCUNo5su-LcBn80Fs_ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T1MjpyTczToHJLvygvCk6kKH276TPT2C9rtWrBjk9NnzNY3e8CJqOPYZzDCwFoKvlPIAuqB1P4liOJGiIasmKuQGpMd1kzLlidJcXurWNiyvikBhYN8OrWbHcJu-AhPeZhDEtrrdiGhem869JxqiQzvAcG1yqsPdtG7MZcPE15C7utiyVCpNdO2v2HBVtb4xJeNNORqc5Qebmjx2r5IOxjSh_S2FyQS24tslRlRuVOQsds6A8Mw0yIOVY_nfHx-8oA7r4xoG79ZYfBhJJM5OZSM3VLZC3Nol3idiePdG5wFpcus5ccqEftbc4-4e2NslmzXmY7LuNGiOiTamA8Wz-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UDbZX42aTrPsLS-0hEb5iykxgYD0ndCoTaTHGR8lL7NgdlsS6XbSqqO_Ov4Tg9Cc0aFZNB_9DwKYkRhr7QX7DSZ-sslYkGIvYZ4LutAHAsg6R65mumdpvIn9_0YQQISJwONqwMOEkKPcenQwqi5L1V2N-6EQn-fUoK9Fhx_U-nzz1VqIbo4x5J0_T50-fkpjC2XAuBKarhUTg7kXHBoDkCKEa52q9wlNi-lprIe2UfQpLJCanj-AQb6Eox8M6UnoNaWhDbeKDedhBpqVzkrCe_KbPJYS0xUNmaoBp4gBPRo705O9HAOg2CfOU893FzBWzSPZGos3xx8Mo2oJdZoVAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fpGBujJ7Hrk0y09XVrEJvZgBjWUPc0Hwz0r0wm8o_YCke5sqgI6dhQokTaUOhCK7Of3riCmkwhb7gVWpr_NqpBOZc2vlFJoKcKDca98jgJyPjGELu02JQrFN9LemvHGaBeaiummjxET05vyIaZbydzJMWrvR2tpPDCkEPp9SjdMjjtC15rZmZWYP4SK5I1oqd-jYnVy5ee6sxf411sHlKbV4rfiTSUZUGkeU7KIhftHqbY_7SU1M2ZDeqgl4ggHe7IM7Md_yaANgcDDk1qjUPLV1J7iUqYMVzFK3OaORES4_68Ne0Sd8Ucd-ESYnMtXkwM4m1ci0KNXtL3QgPr_z6w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=J8DA5IPfvXT3jT5UHHPiqmiQ3Ym9vtaoDdDkaOamqKuSgMnjT6xtK6_jaP5MiEpBqkRR-DU95StobkjygZ2cp3nBkhYXi5lXR6Iwh17FGlj-Fo7kPLB2R5YwnqM5bMjD9IN5NRMxd_CvJ_z9yVX-NEnAKCbjj8sIknCmNQ0Bs0n15HqM8e8DsSZ2wvaTjg0_Te6Q-54eDYP2XEqJXD7S4M38trD3Cofk2mmxrUh3Aejb8MdIR6qL6C5yuUUFlfClXnLrpntjGYOTZMZG69hSdFUrPd4rsR17UsUTeWRhSvlJ3kkLSL_ZjTbXgm55zq4GfNJr_S7ypYqpY2sElfV3DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=J8DA5IPfvXT3jT5UHHPiqmiQ3Ym9vtaoDdDkaOamqKuSgMnjT6xtK6_jaP5MiEpBqkRR-DU95StobkjygZ2cp3nBkhYXi5lXR6Iwh17FGlj-Fo7kPLB2R5YwnqM5bMjD9IN5NRMxd_CvJ_z9yVX-NEnAKCbjj8sIknCmNQ0Bs0n15HqM8e8DsSZ2wvaTjg0_Te6Q-54eDYP2XEqJXD7S4M38trD3Cofk2mmxrUh3Aejb8MdIR6qL6C5yuUUFlfClXnLrpntjGYOTZMZG69hSdFUrPd4rsR17UsUTeWRhSvlJ3kkLSL_ZjTbXgm55zq4GfNJr_S7ypYqpY2sElfV3DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IDNsJaVthPnkww4pk14LGPL8TuDmQlBANK1Ql16nWOi8Zuz3dv_WXluqz0o3Yh55_F9CKLne3lsDW07iZC4vYJwtMiLI33hPkD997_HfPhmW8pae3syggOAyfqvKbgFVLMeJgRum1MJ3xyKPrMTl67rrhwlXMiOyb4xMbHqeciw7EwVfYjWsOau6IgDi467YVbgd0ZNLPHhCgl02XuYwyEpem3x0C-gOMcg9ZxGasnvaIbLSKlNwpLah-vD-Nu5gdb6dkqAgvLdcCmQgtNxw0aWpZFHV4iRImYcpjJkvAW2Cy2cIcuw88K3uLV2s1_uR60G6phLOagWVIkUV5TwRvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=KXbyP2_XTaz71lXRAO9MmZ1zYrNrQ2lKQFc7EwGpOPVRdwkUToCjwOOfZ0kT8QDPCNQVoDjissp2LOj3jqJGq1pngewqIZYg5UY1FUt3vosmuztVttymrVI4i-hpFbMOAIXHKb-sh__Lr1GWSJMdJroA-YIfiMrGN1FDJ5oMeJNvNyzwuoWQ3py1VP4lv-c91xWt9SGweSmhGt7pduR8OfOia-Tom3pTii5d8k9M4jUqriIF5Us4YeLay0SAGqocGBC414KrTLh7HnqjldoRLEQvXs2l9LNlwxyncdEGHAZiMwuh5QtHuT4fLie8OTLy_7AcGNvvuanXh4AfU8rfuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=KXbyP2_XTaz71lXRAO9MmZ1zYrNrQ2lKQFc7EwGpOPVRdwkUToCjwOOfZ0kT8QDPCNQVoDjissp2LOj3jqJGq1pngewqIZYg5UY1FUt3vosmuztVttymrVI4i-hpFbMOAIXHKb-sh__Lr1GWSJMdJroA-YIfiMrGN1FDJ5oMeJNvNyzwuoWQ3py1VP4lv-c91xWt9SGweSmhGt7pduR8OfOia-Tom3pTii5d8k9M4jUqriIF5Us4YeLay0SAGqocGBC414KrTLh7HnqjldoRLEQvXs2l9LNlwxyncdEGHAZiMwuh5QtHuT4fLie8OTLy_7AcGNvvuanXh4AfU8rfuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=DN4AhRx_iPTOP7QAM3TI4nVVIAsGJ6S2EVdtl9ZNGeoOrIaog-ti89Lf2vpsq31LX-lJRzskthEPmGiY9BLoV-GEKzUGsEK8582z1AubTQKCDyuiyJOzm6p55TbHb4vGDZwkwL2N4mApWycdrAfAzxsM5kZZO18pGvi4ryAm5xhWE3KgJz8LsuDHOPC5mou3v2qr5fzJH9BkBrNBSG3HA25B2r3yRLHDZZuXTU8fiFuMTOaxMp2teIlBTJiaVLo0U-Ltpan7WHuj3eIVUbrZmrhBsIcfgbjIIcC8icwkc-BNAjJkw57uRNEYV27LoTJCJbuu70ueNkY9G3G_AY91KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=DN4AhRx_iPTOP7QAM3TI4nVVIAsGJ6S2EVdtl9ZNGeoOrIaog-ti89Lf2vpsq31LX-lJRzskthEPmGiY9BLoV-GEKzUGsEK8582z1AubTQKCDyuiyJOzm6p55TbHb4vGDZwkwL2N4mApWycdrAfAzxsM5kZZO18pGvi4ryAm5xhWE3KgJz8LsuDHOPC5mou3v2qr5fzJH9BkBrNBSG3HA25B2r3yRLHDZZuXTU8fiFuMTOaxMp2teIlBTJiaVLo0U-Ltpan7WHuj3eIVUbrZmrhBsIcfgbjIIcC8icwkc-BNAjJkw57uRNEYV27LoTJCJbuu70ueNkY9G3G_AY91KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r9bjriomtMhu1Hx9uRbvjEncxzSP34Wg6ZBasXMM0375pEG_7y58GX_OadlmPQcMT2QxB-hxYLv3EUbYl7dY6Jv4oBQ5APJxn9EYdzwwls95aNei4Pndpw6RdEvMOmLVZeRtFv0E7mxdW4GLiV0SRJ_9slGbqPFf5YPA4ZuB6FGvQbIe4HOnJ-DhhkCr-hHfzKslK2nTKS8BJAgSniuBWzRLJCP7fReikPOOjB8FnZkJuuUG2O57a9XOW32NQaZ4wFg9qxsVnjG3Cef0TxirbOqRPmQEi_j_qzA9zmi3vuOvL1rGQIsK0mD26gIIdeD6zb90qM2nLpWnrhcpCLSRKg.jpg" alt="photo" loading="lazy"/></div>
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
