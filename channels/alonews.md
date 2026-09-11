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
<img src="https://cdn4.telesco.pe/file/kq-TLgnxTQKix_8NehwwZtXcnZP_ybdflKCc8zOrPVDPYKKu5sQOM6-OkvAS52GTnX-vdvvD_DjZL4VNgk5QunWhmJr7gZePtOqJhkO2mUd62yB3dk4UrZ5BYMBbEr_F4FK846amyD9xcCxNMI7B_RV7KLapgT18xVQfuaivOrQ_aLAEKE2NDjjkWvuKAeAp89rNWMjGwE3eNJTg4pT9EYYLLc4lvZvzVSLH2trSV4YGSdJeR2LGeGe0g19UBceP-wYSbqAURI2DBZUUOddj46Ve8WQM7P6xtw8HRG57ef3sG9blqzX1wy0ldL-0l2puCW8FwPq2-JdtA873C3QWbw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 924K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-20 22:23:04</div>
<hr>

<div class="tg-post" id="msg-146930">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nvLX7KtOHPzijfTokMVzoElHlJu0mHA7DJ28ZppLYVvXB8htiNIMpR1lPxWWc8mWEkCGfBcAvBQmetOmaE7lGbSNbY9N-0eqlI16ABJ_Khcm0o7guKKrh5zQuT4YtAMWBf3vS5-2DFB5RNpeq2KQGq7zzjmxtbhCAUgTjW76nfnXXjn8cg-QotDHki1u0qJAyfqqqYWn3RcXsWVB9k8yr9cKmX0XE4kC6_tpOeaBMo2tKd7ymvIjzQTbO47AQQD5rUtMssUUOBKPXCpRK4nmYsvefOjnlVF4a3GYJfWpMudW04-juEH-AVrpoDgcQN4tljqBnx-vEvY_Qdb8n1u6vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نه نفر از خلبانان سابق نیروی هوایی سوریه، که در دوره حکومت قبلی بشار اسد فعالیت می‌کردند، توسط نیروهای امنیتی سوریه در شهر لاذقیه دستگیر شدند.
🔴
همه آنها به اتهام بمباران بی‌هدف مناطق مسکونی در طول جنگ داخلی متهم هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/alonews/146930" target="_blank">📅 22:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146929">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
طائب، رئیس سازمان بسیج: اگر دشمن درخواست مذاکره کرد، باید با قدرت و با هدف گرفتن حق با او وارد گفت‌وگو شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/146929" target="_blank">📅 22:11 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146928">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
وزارت انرژی عربستان سعودی اعلام کرد که به عنوان یک اقدام احتیاطی، لوله‌کشی نفتی شرق-غرب را به‌طور موقت متوقف کرده است، پس از چندین حمله به این لوله‌کشی در مناطق ریاض و مدینه در روز پنجشنبه.
🔴
این حملات همچنین منجر به زخمی شدن چندین نفر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/146928" target="_blank">📅 22:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146927">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
نماینده ایران در آژانس بین‌المللی انرژی اتمی خبر داد: برنامه بازدید بازرسان آژانس از نیروگاه بوشهر
🔴
ما به همکاری با آژانس ادامه خواهیم داد و برنامه‌ای برای بازدید بازرسان آن از نیروگاه اتمی بوشهر وجود دارد.
🔴
آمریکا معمولاً پس از تصویب قطعنامه‌ای توسط آژانس، حمله‌ای را آغاز می‌کند و این اتفاق می‌تواند در آینده نیز رخ دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/146927" target="_blank">📅 22:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146926">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJQoNvWoQbPTBAImGdp4Z0eJSfQiz10QOLW2PqS1kaSzGUHLe8z12XYYJYqxpUx_1J1R88kbDEjnBhCNREhvXl3ttPV5EBK612mK8Yao0LjP84VCcJXL3GQVGr2PsIw15vHxfpny75Z07ygfWg1DJYUDBlwBVD7xeInG82wPEGZb0HFNgt7pAfaVu5oleaiGoyEAp5zYY8-0IJOAO8CqztsLB-lGJhh6GBM_f2wY5fz1T_OEkFG2nKSUUspz7d_WdjiEItUDfvoaygYk9zKWHJhd8dSHG2NQa2WZ2d2fT2y0PZcK9E8ae63PDR6M4cWSwviXoCl62N2sIScBnjJ39w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مقامات رسمی امریکایی در گفتگو با CNN هدف قرار گرفتن خط لوله جبیل-ینبع عربستان توسط پرتابه های یمنی را تایید کردند و تصاویر ماهواره ای با کیفیت نیز منتشر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/146926" target="_blank">📅 22:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146925">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aby7y9gIYxhrT12T6riNlkI2-K8wiME6Rw_orXfbP9JBpA53UXNvCwv9FQGCdH6R9ve3h482O1OnG9rcxaUbkgvDZmY98t9tox2IaeMEKFPJUSHd6OW0ylbKUVPr3CYPS9YHRIc3XMsAAyClwCu4LqNq4xRukmao-huK8BX5H4mMuqY3orTSBIVXciA53DqlXWc53zNVcoIzPG4T0bdCYswKuEaEtg2LGlvfpRw0qh0TgvYzqLxEWhuhWgDbrhgO1iU12PMC-YTvzEYieLmP_R7e5JO2yDz-KABaqCiS_mMFhqdtp_ly7oUBjpaapcgQWlyvaAF1cjkET3ekoilrnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از پزشکیان و نخست‌وزیر هند دست در دست هم
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/146925" target="_blank">📅 21:59 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146924">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
پزشکیان: ملت ایران بر اساس باورهای انسانی و اعتقادی خود، تسلیم فشار و زورگویی نخواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/146924" target="_blank">📅 21:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146923">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ocv-a3GGpLSRa-Kqp77G5NdZNRSV4JIXLrA_g2KWyZQEokdXHYzo4BxnE6leRS2m0TsNXOREN1y_xXNfK85cdWOF3Bd1MIz7MCtBpZcySUxNAxOEDCBKcOKawuZqJlw-nHZuq3GjY0KrwZw7_7EbLk0mkYj6E36d-WbJjUTvDygpJYYubdhPXW_xBr_7n458Ihm_z9KpWzrm1QmMoKUdWXzlaAkZUS_d1PMNf2i86se374YIZh7lfgQyNFQpOsSCdqKr94RAvpz22M6HneOUq7yd6aRngDSas_lDUr0shqivksUbBDl2n70Cbr2IzHhYES2xQK5Ff1jfF9W1rEYKgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله علی کریمی به رضا پهلوی:
من از 13 سالگی پول درآوردم و خرج خودم و خانواده کردم
🔴
منو با کسی که پول تو جیبی از مادرش میگیره مقایسه نکنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/146923" target="_blank">📅 21:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146922">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb519e251e.mp4?token=QE-42ijNIQ0WFXZqWvyJ1qZYf-tj9PNF0KJU8pImc4wcSZS9FhEIqG8LoFz5dl3aBqAG8_IYyh-Fs216E04KW0VpUU8SWPI9_o0O7mVg90KBnABsABSJ3s1sdlZzyes8o56rqVAhLUk5f1u8W_2g5GSLSLQ_e6scUf_YVnJmkVBbIrOzAN1jktY_5HEcg8NkI4W2JO9HLw24YfwFsmBjTaKPf7ikgFKtjLcH9HQwho6h7LJGRxvRZEbDOr9XHIhRfQL5VZuzbIwMQcr5rhA_h_yo-Yr7Pn9oxu5Agdo4VFbQaqWicjm7u_r4QXGk_2xzeybGMzYwGF3YK353npU-pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb519e251e.mp4?token=QE-42ijNIQ0WFXZqWvyJ1qZYf-tj9PNF0KJU8pImc4wcSZS9FhEIqG8LoFz5dl3aBqAG8_IYyh-Fs216E04KW0VpUU8SWPI9_o0O7mVg90KBnABsABSJ3s1sdlZzyes8o56rqVAhLUk5f1u8W_2g5GSLSLQ_e6scUf_YVnJmkVBbIrOzAN1jktY_5HEcg8NkI4W2JO9HLw24YfwFsmBjTaKPf7ikgFKtjLcH9HQwho6h7LJGRxvRZEbDOr9XHIhRfQL5VZuzbIwMQcr5rhA_h_yo-Yr7Pn9oxu5Agdo4VFbQaqWicjm7u_r4QXGk_2xzeybGMzYwGF3YK353npU-pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارشناس صداوسیما: آقا مجتبی دستور بده توی 24 ساعت سلاح هسته‌ای میسازیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/146922" target="_blank">📅 21:35 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146921">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DsXzO_w1JKbf0LUU-d-V6sAV0dqeBNPcAliE7p10TCp-Qg4LYKiIdyn-LgAeYZiO7zqKlK1jMNeL7cR45YuPGfxVSixDm3JktGLxjZdmHsdialX4PlNajDYLDEy3abNCjU4rHvIc5gJXRsF0MFtooISlSEqQLUXjeDlUUCNc64CIXZcq3VvTLdEgW-RNfaN_677xhgVXEomqD1Sw-Ydf50je_2AVNmPmURToVpHzO0B5g3npHy00oKHEXLQSCasMmeRk3YnNEKNKemRZwEdpAgOhsQd1jZ4QAWh5oAevkKq0iegPF044LbAJ352JDNVpYGVoVrr80E10pBh_xgMYcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شعار جدیدی که دیشب علیه حسن روحانی سر دادن : نهپاد، نفوذی هدایت پذیر از راه دور
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/146921" target="_blank">📅 21:11 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146920">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SYIyKhXqB87c4juZb4NI5Tlg_C4ZJUMt4ufaQ-uJpds2Kgnsl8_HuA5cu3vDK3MmrkXTbQp_e-FcDwxd9lWU7rzq8AKVM5y280do2sdi8iskSuOlT_0G3vRhhwKFOaP6mRtmLi5QxgfeFgxNYpHQKMaDNea57gZstAuhLmOT8gYp3qp9RnUHCegy-1CPG5ZeSwxN0h8krKqIzUdtrvMAl-aTEClN2da4se6-yUstfDfzfTh6LKbCs7_lmJ9fXVRP-0xRSFaZPWb2ICCH8EOuzZ0S8Rvwyel4SuPR7cF-7eDhhrnISvNPWEBa9fq9oWbSKYY9S2dQ0FscXIhyhm3OsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان: و اعتصموا بحبل الله جمیعا و لا تفرقوا و اذکروا نعمت الله علیکم اذ کنتم اعداء فالف بین قلوبکم فاصبحتم بنعمته اخوانا و کنتم علی شفا حفرة من النار فانقذکم منها کذلک یبین الله لکم آیاته لعلکم تهتدون
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/146920" target="_blank">📅 21:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146919">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WeVj6HxMjzwhFeo-fL-e7EUz5LIJ_aVZjc6JGX4L4zHmzrK0f4RLcbuqJ5YOooJy4sC2aAsemGH2aCbqmEzoDvW5KbF57DJj21X9PdotLtO4A6AtZKi3d7P4xxYTXEPj631ix9kfgbm1yoztyrrB7qm30qOyMBT72CBNMJfqL_NKIDaii21P9TtVM7B8txnVYDsXP69CsppKLt3DQXM4rc1RFG5j_RF3Z1gTAZT9MOr2ksKM2s3dtfMdb7MWDZSEGX97guRNHYgOKqlU15XmAGlA6gY6IiGNJe_I2p-SaA6l4_0dtvVDHM4uxMRlDlPHEQRLSTFJEKRA5NLmVcs6yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دنا پلاس توربو ۳.۵ میلیارد تومن
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/146919" target="_blank">📅 20:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146918">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
صبح دلار ۲۳۵ بود پزشکیان رفت بریکس پیشنهاد اقتصادی داد، الان شد ۲۳۶
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/146918" target="_blank">📅 20:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146917">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/465d849e71.mp4?token=sT-ldZu6jlYXsqfCZCWnpCQ-fYjZ1fdITGotn49IWKuZ_aacAbprJYaIGRt-6wJ6iIZXKRWRVTy9CNucMAeI2PipEDwC0sQ9knIEyN6ewR2MyCkooq1AZhCASm9ck4uBQj1SCvWpTR6rb0NbzzpndOJ2-5l0EqwPiTvsmstsLwzV-Xyywn9gR6Zo2sU2ElHdeaTGujBrD5hjvXKSr98spYnodW3aIJsrkQ5_GywDnB32_dWmJH55UnOJDs9wTSv1FSUYSm6PRj1OwKlHLhS6BFPuQzdK7LfxvROVWJcwsrbJ_2AB6vMR4KCkVVWYRV3sYTiyoRVvOjzuQaKzjjus8oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/465d849e71.mp4?token=sT-ldZu6jlYXsqfCZCWnpCQ-fYjZ1fdITGotn49IWKuZ_aacAbprJYaIGRt-6wJ6iIZXKRWRVTy9CNucMAeI2PipEDwC0sQ9knIEyN6ewR2MyCkooq1AZhCASm9ck4uBQj1SCvWpTR6rb0NbzzpndOJ2-5l0EqwPiTvsmstsLwzV-Xyywn9gR6Zo2sU2ElHdeaTGujBrD5hjvXKSr98spYnodW3aIJsrkQ5_GywDnB32_dWmJH55UnOJDs9wTSv1FSUYSm6PRj1OwKlHLhS6BFPuQzdK7LfxvROVWJcwsrbJ_2AB6vMR4KCkVVWYRV3sYTiyoRVvOjzuQaKzjjus8oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یاسر جبرائیلی؛ فعال سیاسی اصولگرا: ایران ظرفیت سکونت یک میلیارد نفر را دارد
به هر خانواده ایرانی ۴۰۰ متر زمین میرسد اما زمین را احتکار می‌کنند و به مردم نمی‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/146917" target="_blank">📅 20:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146916">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AgoPHGITDy8bPK_LS9eZ-hOLrK2eVRy1QmEWT1JB3cN5DYNd0FvVJxSvOeio5UyH9QMs5oGu_n4OxgkvoS2TYc5kcwUSWxiqR8N7t07UJnjmXdMhQvVRgy109JN0ETh-UHeVGF2CeiAB12ZWRptY1DlxWJxPqx7GzNkNgjucEA3JUjKgJrqj0jN5NikXK18vdXfw5v7nrsSwsRV4As7328sa_srD6Xfvs_4dVmifUhx_qsDfGjjAwGct1DfBCSALJLbFNCITsoyJmxjDipSrHCAUIuzqMyk8Ft-XFPWpfBlcjTZqAQsoiwAsG_fho6HOaEkVzW5W6IEsZTcO3oQzjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ادعای
امام‌جمعه یاسوج:
اقا مجتبی روزی ۱۰ ساعت فعالیت داره، تو ختم پدرش هم حضور داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/146916" target="_blank">📅 20:10 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146915">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aECLPVhXMjH1GGS0v57w09Ri31xCm1xYwKJ412XkgWDgJfP-C1UXTBy4cF_c7hF3cMvVRX--2JcTFiweLHXM-hrtVxk0J_4-iuzHNVMKr-ZOW1wIwLfxnLs65SRzJe_2dYqt8C2poJNbrJIBAPmkjxsNUHvtTh53Tgcaak5IO8UhwTkEZqovbacmJHMT9vQPuFXIvyOuzxBDAxE1-Ze0c9tn2DAzMj7t_Ni3Bu2ArGgFuW2RTj4qzKzDIL-SDIqmS4lepQf---dAiYJuVnoD65_-RW1A_FelKxCRzjyjHuyLz65n-CJ0NJauMjWaIXpFvuvKTsfLoWP0wBAuTdO03w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق پیش‌بینی‌ها، یکی از پربارش‌ترین پاییزها در راهه
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/146915" target="_blank">📅 20:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146914">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‏
👈
مهر:
صدا های شنیده شده در قشم تست پدافند هوایی بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/146914" target="_blank">📅 19:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146913">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zji1VdM7DXWPEPJwwf_KsUkHWY88Od_ftGN6P7V6lv1M7C7K20M_YlQESlCQzY8_VGWh0rMZ1yQuTy8NHFkre3dQfFk5mYaGxzoNJv9MiJmYeLqV1nvMNqxcLOtGByVPQekHhbqWR03hxydrE1K-Y1JF0LEH2h4HeLTePgYhEA04lTMMNrOtGldjCUlk5GOl2sR1d68LSNekZItKXdr7IFvUb0MvrEJWRxCzcEGQm4ngsbjRcYAY-XmOSN9GlSqQc24emaCSVIncTrE23j-foISe5Sp6cHEuN6V-1RCxyz2ew-yBRX-Q2Mo5JGp2axN-OoYrKn9SpMWNdJ3vByapnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امام جمعه تبریز:
اسرائیل ما را به بمباران اتمی تهدید کرده؛ از همه مسئولان کشور می‌خواهم دکترین دفاعی ایران را مورد بازنگری قرار دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/alonews/146913" target="_blank">📅 19:37 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146912">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63cda7faae.mp4?token=TBQV0ffltitKCOBTWulkNwbnLzNuaPvi_e8hXypO4ELo1jPT6Geu0zJrYr8sxd7vm1FNFva7nLzpunT8HZc-gtkNsdfftGwNlS-hI0ZlYdmo3LbVY-VZle8zfEbCut_g2BvNqdQr7fwEUlBEKmTlZFLdAcrQCFgv9bPoZwoI0M5sYv6tVNL_P0L9Hu2SoQJLh8Xac5sifKk_xZeAeaUC5cQszmbu4ILBBq7zfon0HVklRX2556-Z0mKr9MGoiueGx_Uxr22AlMl7miGglSKGNvGp0Q8RPxOgnT7rGwItf7cHse7zTCGh6Et1cgjL3gh0pHfSyOR2DbNln_qq46E6cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63cda7faae.mp4?token=TBQV0ffltitKCOBTWulkNwbnLzNuaPvi_e8hXypO4ELo1jPT6Geu0zJrYr8sxd7vm1FNFva7nLzpunT8HZc-gtkNsdfftGwNlS-hI0ZlYdmo3LbVY-VZle8zfEbCut_g2BvNqdQr7fwEUlBEKmTlZFLdAcrQCFgv9bPoZwoI0M5sYv6tVNL_P0L9Hu2SoQJLh8Xac5sifKk_xZeAeaUC5cQszmbu4ILBBq7zfon0HVklRX2556-Z0mKr9MGoiueGx_Uxr22AlMl7miGglSKGNvGp0Q8RPxOgnT7rGwItf7cHse7zTCGh6Et1cgjL3gh0pHfSyOR2DbNln_qq46E6cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پوریا بختیاری، فعال اقتصادی:
خودِ ابراهیم رئيسی می‌گفت که اقتصاد رو نمی‌فهمه!
از ما دعوت کرده بودن که واسه رئیس جمهور ممکلت، انیمیشن‌های اقتصادی درست کنیم.
تازه گفته بودن این انیمیشن‌ها نباید از 3دقیقه بیشتر بشه چون ذهنِ حاج‌آقا می‌پَره.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/146912" target="_blank">📅 19:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146911">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gnEYEddVORO5spW3dddJdU3-NVY6A0b4i5RH-3F6xP_fUhb-3NCvV6d-KSqEUsqyKhf9Si-zS_tiM3vdp-9jJaF_sR749RY3USPp9M1EwrpmY-qofFNO17WeIDLt7uEIfpVZ0CZpcTyJBGDMTSR2JiAFpU5zYfY6uD67_QBre4uj96Tdz489LTwMn6_0xmraI3FqZSfwYKR6Bw7WbdY1Ars2puTVPnl-YsvMYHP5Bq3xDDkvmn0etpmmzAn3VktM48dP2oghFcsWttX78CTAwWtIObI_oKX2zxo6beC0lLWy4WfOG7OgkmBzy9K-lzdHd0MgZlGHYdbLrjZ6T4X4Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله هوایی اسرائیلی به نبطیه الفوقا در جنوب لبنان، ساعتی پیش انجام شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/alonews/146911" target="_blank">📅 19:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146910">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p1X2k3iTgn6Yr_mdXYLPQ4XDKtp500XNCXqGzzUalLnzlb_gncg8r_NWa4RpQRksbieEGxow9pcT0SuLRyornIl1iJTNl5McGzqK043IU1sjaleTIXeqpzUY0tP31WwiGvvNm7hmaw8UD-8pi5HhJ6AGjIzy7yuUw4mgZn1qC0kSVkonbGJk0uM03ZJsRbKAQqTENB2nrHBQyyOnXTFZWglzVkxK8U-IElBYXqV8Qdir2XUSaI5C1qEXUgcCQHrUNwzGJNt1AO-dL6P5iYe0C4ktCPuEqgnHOZIzwXgucElorrYS8eXHzee8dyO7S6082Rn_cS7BwhIZHQdQ6ZGLfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کانال 14 اسرائیل:
اوکراین
مرکز کلیدی لجستیک جمهوری اسلامی و روسیه در دریای خزر را هدف قرار داد.
حملات شبانه‌ی اوکراین به بندر مخاچ‌قلعه، پل ارتباطی و حیاتی دریایی میان روسیه و ایران برای انتقال پهپادهای شاهد، آن را از کار انداخت. در همین حال، ۳ ناو جنگی روسیه در نووروسیسک به شدت آسیب دیدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/146910" target="_blank">📅 18:55 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146909">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HkskbwmMIuIhzgN7uEEdO3dMSTfoLXLFTTPamwR7oM-UjawRHq9w9QPTkc92ZTSwuYnHj0j8MEl83EmHkn8blxFxBPHXwBupTGQX6sHuF4uXe2h5CZaYgEA81_06WNqwR5IOZY77vTNOfCWSeM-Fu6QkyhZrDIh4VmknkooD2I2TGFeMgQmOeH05f83g2tfyCxGpKNqkNZdWlsf04QhXap2e5mKpsUyq_oxcq1ODoBo33kC5Ih4koRgG9aGeH3bU_SYD4oj6e2M91rxjk3VYRsp25OTAq-Mt8ywZkdJWxOoK2HJhc932ug5CNOE9UYtvX6mzvVs6Fn1NG0RGnyl29A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
VIP مخصوص روزای قطعی و اختلال اینترنت!
😍
اگه نمی‌خوای وسط قطعی اینترنت بدون دسترسی بمونی، از قبل
VIP
تهیه کن و خیالت راحت باشه.
🚀
سرویس نامحدود با قیمت فوق‌العاده
😍
قیمتش حتی از
پاکت هم کمتره!
⏳
ظرفیت VIP محدوده
و ممکنه سریع تکمیل بشه.
❤️
برای خرید و فعال‌سازی
👇
👇
❤️
@NetAazaadBot
@NetAazaadBot</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/alonews/146909" target="_blank">📅 18:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146908">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2f8a98470.mp4?token=GAjZUFjHmXXqF_KRrNhJNDcvowLqTHO8EHfuknRMd0gsXW-5GkSTxfzci_g3Cq6snjd3TSXCyQv6w5B6x3rcPJqvPiqQHLlYmG5cHK7TTIKPyzLzHVuIf4eb_U__51Qvgcs5H2TF8SLKJW8oiCNbor98opuvZ9MwEdXzYRnG6CrTzTFmkIRvpt1TaZx3-vlY7J-33Nou_bYvyAh0eD1AjAcYHFyVsGX7LMcth6dBIRUUC_iZSBUowjAKMMv2LucMs2K3Tqjb10kgYDANlQ16GtG3eDePNc-wEaV3ub1K-aNhfk0sGSz6qEH3fWYH-V_XY6Pa6hjjhfRG6r_oKAvLvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2f8a98470.mp4?token=GAjZUFjHmXXqF_KRrNhJNDcvowLqTHO8EHfuknRMd0gsXW-5GkSTxfzci_g3Cq6snjd3TSXCyQv6w5B6x3rcPJqvPiqQHLlYmG5cHK7TTIKPyzLzHVuIf4eb_U__51Qvgcs5H2TF8SLKJW8oiCNbor98opuvZ9MwEdXzYRnG6CrTzTFmkIRvpt1TaZx3-vlY7J-33Nou_bYvyAh0eD1AjAcYHFyVsGX7LMcth6dBIRUUC_iZSBUowjAKMMv2LucMs2K3Tqjb10kgYDANlQ16GtG3eDePNc-wEaV3ub1K-aNhfk0sGSz6qEH3fWYH-V_XY6Pa6hjjhfRG6r_oKAvLvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیتر هگست:
تاریخ به پایان نرسیده بود؛ هیچ‌وقت هم به پایان نمی‌رسه. مبارزه با شر ادامه داشت و الان هم ادامه داره.
🔴
و این مبارزه تا روز قیامت ادامه خواهد داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/146908" target="_blank">📅 18:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146907">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06eee79e79.mp4?token=CRXzeH_5tUbFwbn39h_w3Zt8rSPjWBk-MpR91mHa9S6DPqqQMafgguh3RboJn08qkYt4LYuhVBiiWdt6yOJbY2pCOA6C6yC_XGBwKI0bZ56m8JzlzMH39k92-1e5OrYjmO7BwztynqwDOZuvgHTWDwTGmzYt_X_w2GETufz6mYYGuSpMndrONkR5dI1_lrZv4j7tjoqzGEwbvzFBVRuSBAgq37y6W8wH19bdNyuhjw1-q7K364SFcOjX2ucL6mB0xSWlbFJ-3nE82bcQi2pRNNqAYhYq6isvhsyona6c9vUIbvVuAlIldTppCADWdCplpCbKgCEAGXgh34X3W-EXng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06eee79e79.mp4?token=CRXzeH_5tUbFwbn39h_w3Zt8rSPjWBk-MpR91mHa9S6DPqqQMafgguh3RboJn08qkYt4LYuhVBiiWdt6yOJbY2pCOA6C6yC_XGBwKI0bZ56m8JzlzMH39k92-1e5OrYjmO7BwztynqwDOZuvgHTWDwTGmzYt_X_w2GETufz6mYYGuSpMndrONkR5dI1_lrZv4j7tjoqzGEwbvzFBVRuSBAgq37y6W8wH19bdNyuhjw1-q7K364SFcOjX2ucL6mB0xSWlbFJ-3nE82bcQi2pRNNqAYhYq6isvhsyona6c9vUIbvVuAlIldTppCADWdCplpCbKgCEAGXgh34X3W-EXng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
هگست درباره ایران:
تنگه را ما کنترل می‌کنیم و این نبرد را نیز تمام خواهیم کرد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/146907" target="_blank">📅 18:12 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146906">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e4eb98a5d.mp4?token=gU6G_XvJmcRxUcDpHLL3AgpXS7eHmQN3jH2aETOiC8guK2tO2H3LVML8Gh-L-9RjF4OOaTBb5x9gNeETuAyz0lVx9HJjFdsyqY0tpElukB02jDl1-dgFiwCRbh1RWoj1gt-pLEytEDPiij_uXg7WX8W2lD31whpwei5mb_scbdT3iOCgLjn4AQwOQ_Yb4ngDiUCGpj5jtZKFfT4yShROV7BJXgBnYEC0wUVZErUFOyv6rym4Z6o6RcXJVzDTdwIGgD-YeRG19gvn8GkRIGnf_EKLza3nvWM-Dy7i5ogmpAK8Y9KzYGQz6in16goqZgiCuVMEYbwTQDBe10KGIexvwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e4eb98a5d.mp4?token=gU6G_XvJmcRxUcDpHLL3AgpXS7eHmQN3jH2aETOiC8guK2tO2H3LVML8Gh-L-9RjF4OOaTBb5x9gNeETuAyz0lVx9HJjFdsyqY0tpElukB02jDl1-dgFiwCRbh1RWoj1gt-pLEytEDPiij_uXg7WX8W2lD31whpwei5mb_scbdT3iOCgLjn4AQwOQ_Yb4ngDiUCGpj5jtZKFfT4yShROV7BJXgBnYEC0wUVZErUFOyv6rym4Z6o6RcXJVzDTdwIGgD-YeRG19gvn8GkRIGnf_EKLza3nvWM-Dy7i5ogmpAK8Y9KzYGQz6in16goqZgiCuVMEYbwTQDBe10KGIexvwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ما هیچ‌وقت، هیچ‌وقت فراموش نخواهیم کرد.
🔴
به همین دلیله که ما امروز می‌جنگیم. ما انتخاب دیگه‌ای نداریم
🔴
تنها چیزی که می‌تونه وجود داشته باشه، پیروزیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/146906" target="_blank">📅 18:08 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146905">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7dd01ae09.mp4?token=pJk0fS2w8AF5xrQJB7VqNqDDxUMXHXRp4H6_7FmROKoZXvDAkA7YIk5o88_N5TnPfpgNPeaHJ-NF26hUroV-irsrroJcso4yfEsfC6VdkzdtObWWxuT8NnaWS8j4LzRhB0cIJpTrdhANDTcSSnxW_hQSAZMd1wTnOFLqEKjzSMtRetWlfgeSooRUT5I-6u1mLMuIdpTIJVVxaRfGfE68c9iytGQCptRxV8YnlEcUAl3AEZFQhc8vkof21wkcKa6rUVuTNmZ-w8LJjVcAqeOk-xb3Zqaxc4W4MM3S7TJaE7MqiC79PMAQUAq1DH3axZf2uWWWMUAuLqvVjh8CO98no7QS6RBSfEWG9XGQWclgQhKdFC2e3fTiJ7r6xPGTFoCOkZLffZPDCp8cP85z5y2zSR6GMdBCHcs8XrOh9EVy1_TBNJxpYY3zSYWdJpKyZ8h-FgeylK--YSAmch8RSBQbt-U--M4KpVDCE-DQq68WAO9qzj2kB0Eu_OVAs5aTg3UGZHALXV12qRFy-4Vf7JPGjB-CbWc3rPmCOpWFCIrRl17Gcs1Lkt6USFAzuZxPrm-Rp4JKl2k7VTLLJRJmiTL5rjyBvZCIDHNxrTuBTzasXlsIIwCwojAnCwY2208cGjV1NBBK4docEnZY5-0zR3L9vrLDYDYBKoAtvz24EQAhRIM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7dd01ae09.mp4?token=pJk0fS2w8AF5xrQJB7VqNqDDxUMXHXRp4H6_7FmROKoZXvDAkA7YIk5o88_N5TnPfpgNPeaHJ-NF26hUroV-irsrroJcso4yfEsfC6VdkzdtObWWxuT8NnaWS8j4LzRhB0cIJpTrdhANDTcSSnxW_hQSAZMd1wTnOFLqEKjzSMtRetWlfgeSooRUT5I-6u1mLMuIdpTIJVVxaRfGfE68c9iytGQCptRxV8YnlEcUAl3AEZFQhc8vkof21wkcKa6rUVuTNmZ-w8LJjVcAqeOk-xb3Zqaxc4W4MM3S7TJaE7MqiC79PMAQUAq1DH3axZf2uWWWMUAuLqvVjh8CO98no7QS6RBSfEWG9XGQWclgQhKdFC2e3fTiJ7r6xPGTFoCOkZLffZPDCp8cP85z5y2zSR6GMdBCHcs8XrOh9EVy1_TBNJxpYY3zSYWdJpKyZ8h-FgeylK--YSAmch8RSBQbt-U--M4KpVDCE-DQq68WAO9qzj2kB0Eu_OVAs5aTg3UGZHALXV12qRFy-4Vf7JPGjB-CbWc3rPmCOpWFCIrRl17Gcs1Lkt6USFAzuZxPrm-Rp4JKl2k7VTLLJRJmiTL5rjyBvZCIDHNxrTuBTzasXlsIIwCwojAnCwY2208cGjV1NBBK4docEnZY5-0zR3L9vrLDYDYBKoAtvz24EQAhRIM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ از ارتش آمریکا تقدیر کرد، اما هیچ اشاره‌ای به نیروهای کشورهای دیگر عضو ناتو که پس از حملات یازدهم سپتامبر در کنار آمریکا جنگیدند، نکرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/146905" target="_blank">📅 18:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146904">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
ترامپ: ایران بزرگترین حامی دولتی تروریسم در جهان است و هرگز به سلاح هسته‌ای نخواهد رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/146904" target="_blank">📅 17:56 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146903">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93e991788b.mp4?token=a7ch57Umu53k2-spBKMNkur1Ci_vnu2Lq1_1jlhf11r8YQD2XTR9l8vxGuplPT0YwC4YfAwkDOvwFoi097S2ORwofL-UqBMA6t_Sdh1EkjO5il3Bd11XiCYYbgHfgtWhTKWzGr-ToxK-kkwEr2YOvLeYJawT1qMcauQ4Wifa3xuNPME6Sic5bJL39FLzYP7hm7HaOVlQtHT6R54hKUb_81ys_2BurIi_j5OIEPOPNU6t7jmmk-B6Hf1sVQPAGinw0W0Clb5bTn2eqzcv42rZaOsI3H4SBv49941xQVpAGbVQR6DGLCPlu2lkzBKWRd4JqiXhrc-rME9WIahR2Sm-Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93e991788b.mp4?token=a7ch57Umu53k2-spBKMNkur1Ci_vnu2Lq1_1jlhf11r8YQD2XTR9l8vxGuplPT0YwC4YfAwkDOvwFoi097S2ORwofL-UqBMA6t_Sdh1EkjO5il3Bd11XiCYYbgHfgtWhTKWzGr-ToxK-kkwEr2YOvLeYJawT1qMcauQ4Wifa3xuNPME6Sic5bJL39FLzYP7hm7HaOVlQtHT6R54hKUb_81ys_2BurIi_j5OIEPOPNU6t7jmmk-B6Hf1sVQPAGinw0W0Clb5bTn2eqzcv42rZaOsI3H4SBv49941xQVpAGbVQR6DGLCPlu2lkzBKWRd4JqiXhrc-rME9WIahR2Sm-Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره حادثه 11 سپتامبر:
ما همیشه قربانیان و خانواده‌های آن‌ها را که در حادثه 11 سپتامبر سال 2001 جان خود را از دست دادند، به یاد خواهیم داشت. متاسفانه، این یک تاریخ بسیار مشهور است.
🔴
آن روز، در ابتدا، روزی بسیار زیبا به نظر می‌رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/146903" target="_blank">📅 17:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146902">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dd606e096.mp4?token=jpgCMU_p7DaMJ0EG1JkZsKtC80tQWqEkXXXE4xozCBS9zeqBg1nAtcoxqwHEg2lXlpADVWM9wFJ3l4x1qemEUqyJ1UH71nKcIIhhOj-eFpEHH8rdT0IVSl8YRA9YLkzaaZOYUnnkjoEqnXJbX6t8z_GTaSljiwwkiNcNSAojDX6Ph9U7fZqBAfkW0_cVnVYA8h_hqq4L9R_BoxlkeZ6Y-S3saa4oLrvIr0qu6oEbqTDyvmVw16Gv6hx5_fNTdTexdOqwe2CuyoRQIc1LD48JZboKA6-9NIcpy7JXCFS50pjZRxLk-0-Fpv8X53OYLazsl3xuYC-ye3lH5qILK09feA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dd606e096.mp4?token=jpgCMU_p7DaMJ0EG1JkZsKtC80tQWqEkXXXE4xozCBS9zeqBg1nAtcoxqwHEg2lXlpADVWM9wFJ3l4x1qemEUqyJ1UH71nKcIIhhOj-eFpEHH8rdT0IVSl8YRA9YLkzaaZOYUnnkjoEqnXJbX6t8z_GTaSljiwwkiNcNSAojDX6Ph9U7fZqBAfkW0_cVnVYA8h_hqq4L9R_BoxlkeZ6Y-S3saa4oLrvIr0qu6oEbqTDyvmVw16Gv6hx5_fNTdTexdOqwe2CuyoRQIc1LD48JZboKA6-9NIcpy7JXCFS50pjZRxLk-0-Fpv8X53OYLazsl3xuYC-ye3lH5qILK09feA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ، حملات 11 سپتامبر را با جنگ خود علیه ایران مرتبط دانست: ما هرگز این واقعه را فراموش نخواهیم کرد. به همین دلیل است که امروز می‌جنگیم.
🔴
ما هیچ انتخابی نداریم. تنها نتیجه ممکن، پیروزی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/146902" target="_blank">📅 17:51 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146901">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YU6XvKQvy3yM8lqW01chd8GronMwizD0oUwKTQ-kr-JOMR_p2Cy9ottk_eTHuFjQtC2Z0WHdSC91BROCkfZ0K05xA50hVFBq_z_qIfqBX0TKWrS2b1ZX_VcOaTB8pManw5rXVTxA_bd5UPz0285ztCMRyhvHPnH9IyPcuSBw2vWvTZK8tTxC3tXkbat8N2G_ceKRHv8YgSaQPczDbI4eWG7vOX9WYp1Zqt1CGWXRQWMHmCSd5SFnjOX0LW8V9anUT4-7_bkp99_yySe9WKFHLGUn-j2zYyLA-AdcDL3EI40VUJ1mvacr4Tir0k2hT2MnKU7re-tEbxp1bauR4R75FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی:  اخیرا محسن رضایی از عاصم منیر گلایه کرده که چرا صرفا طرفِ ترامپ بوده و از نقشِ میانجیگر خارج شده است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/146901" target="_blank">📅 17:42 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146900">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
رئیس جمهور اوکراین از حملات شدید پهپادی به تأسیسات نفتی روسیه خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/146900" target="_blank">📅 17:37 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146899">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14e35d7d19.mp4?token=IzP1Q8-tfNA9c1nXZsgWvC8OwO5aaMheXtveYjjfdHJ3c7fwqhNZiYEh9d2FFugaBoebJRKCGuOhGTW1ZyAJLO3a6sDWZ_VL91rmHcbPULJnoHQq8X2WA2-gx8lDQXEO9f4xEPlPRWEK1Nk8VMsylxw46O8MyBksl2EXqH73J0Y33jcPk_8FeG_BYdYh_wM8UmFqJ7UyrZxxqNq-FdPcDE6kyteEDuc6_luDCDhbct71G3vQ5-gYc61G_G3WtsJYGfibfoO-G3D4U3dJgpvDEd0BkxT69xGWnVg7BsX5HHJHP3-boU2ZP_BEP57kREsxR9GAjcp64UlvUOUAyLyYKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14e35d7d19.mp4?token=IzP1Q8-tfNA9c1nXZsgWvC8OwO5aaMheXtveYjjfdHJ3c7fwqhNZiYEh9d2FFugaBoebJRKCGuOhGTW1ZyAJLO3a6sDWZ_VL91rmHcbPULJnoHQq8X2WA2-gx8lDQXEO9f4xEPlPRWEK1Nk8VMsylxw46O8MyBksl2EXqH73J0Y33jcPk_8FeG_BYdYh_wM8UmFqJ7UyrZxxqNq-FdPcDE6kyteEDuc6_luDCDhbct71G3vQ5-gYc61G_G3WtsJYGfibfoO-G3D4U3dJgpvDEd0BkxT69xGWnVg7BsX5HHJHP3-boU2ZP_BEP57kREsxR9GAjcp64UlvUOUAyLyYKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پوتین: طی پنج سال گذشته، بیش از ۴۰ درصد تولید ناخالص داخلی جهان توسط کشورهای عضو بریکس بوده است
🔴
در حالی که سهم گروه موسوم به «هفت بزرگ»، نمی‌دانم چرا به آن «بزرگ» می‌گویند، تنها ۲۹ درصد بوده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/146899" target="_blank">📅 17:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146898">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7637eba24e.mp4?token=q3ZAhzzxC1XxHJebpIMN1Y1U7KYcrZufUZKj_4LWDpxuq_czqptQwJbB62vej80J7hmArdhJNPcr_6DP0ripCdWuPMsu4F1i3Ay9QqbJ9qHUnrW7QdYyqUFpEGsUPUDjnW-NB5uzHHURN0cpoUSQF0K3EA_oaoI1XU5KDtbv3ITlDxazlct6qL2-zuzVB_C5ViKXeEInMVrxCPMJLEMo0AUeGfSo8J4U4AH_kCpmI8gSv3kR8Q9QTzev-UXPFwnAqIm9hb0z7FKEyqDLkb7nM27PF7ULv_a0fhuu7Ujtp3AMbYhbtTZbQeKq9VgdwHnrqtX79XaBf8iwV6VZVs-0-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7637eba24e.mp4?token=q3ZAhzzxC1XxHJebpIMN1Y1U7KYcrZufUZKj_4LWDpxuq_czqptQwJbB62vej80J7hmArdhJNPcr_6DP0ripCdWuPMsu4F1i3Ay9QqbJ9qHUnrW7QdYyqUFpEGsUPUDjnW-NB5uzHHURN0cpoUSQF0K3EA_oaoI1XU5KDtbv3ITlDxazlct6qL2-zuzVB_C5ViKXeEInMVrxCPMJLEMo0AUeGfSo8J4U4AH_kCpmI8gSv3kR8Q9QTzev-UXPFwnAqIm9hb0z7FKEyqDLkb7nM27PF7ULv_a0fhuu7Ujtp3AMbYhbtTZbQeKq9VgdwHnrqtX79XaBf8iwV6VZVs-0-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا: ایرانی‌ها در تلاش‌اند تا در آمریکا مشکلات اقتصادی ایجاد کنند
🔴
اگر به حساب‌های کاربری ایرانی‌ها در توییتر نگاه کنید، می‌بینید آن‌ها تلاش می‌کنند در آمریکا مشکلات اقتصادی به وجود آورند؛ چه از طریق تغییر نرخ بازده اوراق قرضه و چه با دستکاری قیمت نفت.
🔴
رسانه‌هایی مثل بلومبرگ، فایننشال‌تایمز و وال‌استریت‌ژورنال تا حدی به «سندرم اختلال ترامپ» (حمله به سیاست‌های ترامپ) مبتلا شده‌اند که حاضرند به ایرانی‌ها تریبون بدهند تا علیه ما مانور بدهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/146898" target="_blank">📅 17:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146897">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-zEWriLsWCd5So2cHiNgJM77oeWYEyuEEsB0_5AZ9UzZStgyR4wKQc9H5BVV0AFIigz_qiHl28ywIHpDNhicCirb9RhJBNQ6slBT9dQK_Q0iYveJKiFN9USpYVk09bqxdJForAhKRXk3U2Q-3w3gM4c-yxIYbFuVIQdYzB311T4qug1GTxBXu1XhlpXolMho4k3rsQxRl-F5Fh_9lwMSSXfwkx4ZGTB-K4JcMoa-YBu17hP8kQNsbZ-nXn7YwFX780BEzAHO-OV9pAUSqfE9c9ks9y2ZeAQlIi-ds9_Hq0rF4R3KzLTYeVTKonaNVuT3vyzprc8OgLDE68zoHhyUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان با نخست‌وزیر هند دیدار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/146897" target="_blank">📅 17:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146896">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
وزارت امور خارجه : ما روز دوشنبه، با همکاری عراق و کشورهای خلیج فارس، نشستی در مورد تنگه هرمز در عمان برگزار خواهیم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/146896" target="_blank">📅 17:17 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146895">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
امام‌جمعه یاسوج: اقا مجتبی روزی ۱۰ ساعت فعالیت داره، تو ختم پدرش هم حضور داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/146895" target="_blank">📅 17:02 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146894">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d562e33a76.mp4?token=tGZpsbGxb-AzgbdGnYPgCoWDwLzeFrWhdHekPo_8VDRDbiLIo4InWXo9WTDAa91tQdHS27c0jMqEp2Nv5W13QfsMVfWy8VQa0mgqelM1o4AQXzEiIVc79jCOhz7S6e2rBYdbrHjVdGFdirxzIlCLisF1h9X03TrVhj7kROnraCUuL_zzWbjIQINKzxL0YfsQX2l8rIwtWzYQ99HqhfZFY9LqxcjOZ_E6BeSv4aDNEaCmSPO2PeO8_7tnjYGE9cXljvCvNDIThIYSZndwW1Cp1K8Ei6HEtLyobvS-1gccBBjuyFLvB_d3KS45SIsfjUF9rAkil_0qzgx3cymCaGXSzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d562e33a76.mp4?token=tGZpsbGxb-AzgbdGnYPgCoWDwLzeFrWhdHekPo_8VDRDbiLIo4InWXo9WTDAa91tQdHS27c0jMqEp2Nv5W13QfsMVfWy8VQa0mgqelM1o4AQXzEiIVc79jCOhz7S6e2rBYdbrHjVdGFdirxzIlCLisF1h9X03TrVhj7kROnraCUuL_zzWbjIQINKzxL0YfsQX2l8rIwtWzYQ99HqhfZFY9LqxcjOZ_E6BeSv4aDNEaCmSPO2PeO8_7tnjYGE9cXljvCvNDIThIYSZndwW1Cp1K8Ei6HEtLyobvS-1gccBBjuyFLvB_d3KS45SIsfjUF9rAkil_0qzgx3cymCaGXSzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ا
سکات
بسنت: ایرانیها، اگر به حساب‌های کاربری آن‌ها در شبکه X نگاه کنید، تلاش می‌کنند مشکلات اقتصادی در ایالات متحده ایجاد کنند، یا با دستکاری در نرخ بازده اوراق قرضه، یا با دستکاری در قیمت نفت.
🔴
و می‌دانید، صرف اینکه رسانه‌هایی مانند استیفانی، بلومبرگ، فایننشال تایمز، و حتی وال استریت ژورنال، به شدت تحت تاثیر "سندرم اختلال ناشی از ترامپ" هستند، آن‌ها می‌خواهند به ایران‌ها بستری برای فعالیت بدهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/146894" target="_blank">📅 16:55 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146893">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03112531a9.mp4?token=U79zsmzK2-k_jRVkIpZ4FSjL0amuPNxIV2xOHvfddhQ4FKOrmiB6mvrFy6L5RZ5TIBILdeddTD3LW2ffmbgJDR8tPSK9Ma_DSV7mORGSpYTu5IanB1chLNU8cy7eTIR0iVCZeDGGYFos09t3qu5T_EMy5uxCwUki2jjnKGVHFYOMSarVLlUTH_vHvQ6Mzt7vlpUmo_ny6Fyqs2UY3inY1TcaS7texNGq2w_RXoTMCdPGERnv9WC0X23IzEVlXSDupHpu05g4fRd0csDLO2UJvPCOSN2pKjn5WTBoHXMlNZLuAHLgT1yyjKL4KtUoYvM0w0eIzDp3F-8rG12g04VeXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03112531a9.mp4?token=U79zsmzK2-k_jRVkIpZ4FSjL0amuPNxIV2xOHvfddhQ4FKOrmiB6mvrFy6L5RZ5TIBILdeddTD3LW2ffmbgJDR8tPSK9Ma_DSV7mORGSpYTu5IanB1chLNU8cy7eTIR0iVCZeDGGYFos09t3qu5T_EMy5uxCwUki2jjnKGVHFYOMSarVLlUTH_vHvQ6Mzt7vlpUmo_ny6Fyqs2UY3inY1TcaS7texNGq2w_RXoTMCdPGERnv9WC0X23IzEVlXSDupHpu05g4fRd0csDLO2UJvPCOSN2pKjn5WTBoHXMlNZLuAHLgT1yyjKL4KtUoYvM0w0eIzDp3F-8rG12g04VeXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: استفاده از ارزهای ملی در تجارت بین اعضای بریکس باید توسعه یابد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/146893" target="_blank">📅 16:46 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146892">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SDbdxI4_70D2lWmDWw6GAIAMfDZEQ0oiU2fESrz-kJCBd1ChdGH6ipmdybdRWDk6GexwiKsNGUmXmdkQ_lNXUaZqAzPUaHk1-zdwQVQQxWimYWSr5dr7hYjoeiWOCt47Tzg7FvNJb4LsyjdHLzeFTPPhRqAg8EvgJ54Y3rstxo1QZfhuELAZoOWrRUk8tzTu3qkfDvk_LsKhoXdFP9DAGN972MoG-ETniIbv7kl2FXTpYs7jC0KgT-EpgLTe3NZIo9UuOo7iHYwrjfSfr791_zhZi0tsnMJL2c3McOGJR0dAJtDKlZ1gQQ93J6rn0p4KbLijj6nDl6CsWvuWqAjkfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی: وزیر خزانه‌داری آمریکا با خوشحالی به خود می‌بالد که می‌خواهد ایرانیان را فقیر کند و اقتصاد ما را به فروپاشی بکشاند. اما در عوض، او درمانده و ناتوان در برابر افکار عمومی قرار گرفته است؛ در حالی که جهان روزبه‌روز اعتماد خود را به نظام مالی آمریکا بیشتر از دست می‌دهد.
🔴
بحران ناشی از هزینه تأمین مالی بدهی‌های آمریکا تنها آغاز ماجراست
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/alonews/146892" target="_blank">📅 16:41 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146891">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
پوتین: کشورهایی که فشار تحریم را علیه روسیه و ایران آغاز کردند خودشان با افت صنعتی و کسری بودجه روبرو شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/146891" target="_blank">📅 16:33 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146890">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cac53a8e4.mp4?token=N4hacsl-8hZ6jNdjZB6OQwwrAHKW6n2bcUanSNUoH_hqfbJ6ExVPoKULgjD3IS_TX3fBi61jt3bZwsCtPjAs-XrkYeAsQ5H4VIhOeNCSMGGdiSVpWqRuRYmzH-Rrpy1_yq2nZT3TUkNuFvaQ6H4zL0GMieBvifLdF162baJUn-e_Y8zTRkYJJnnDu8bNOq04Ej5d2VF7TNoZgZeUcxyP40P4MBu4xE2syF8xkDpEiQbtCeNmfioCaMKgbFPSZ-GRt1z2p9OjGly3I6ap6gVLnrgN0_oDaPnADRjKZl-IS2b8eLfaUwb247k1rXtJR4TkBfI3YDxa9qkRpQEC4wxGS4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cac53a8e4.mp4?token=N4hacsl-8hZ6jNdjZB6OQwwrAHKW6n2bcUanSNUoH_hqfbJ6ExVPoKULgjD3IS_TX3fBi61jt3bZwsCtPjAs-XrkYeAsQ5H4VIhOeNCSMGGdiSVpWqRuRYmzH-Rrpy1_yq2nZT3TUkNuFvaQ6H4zL0GMieBvifLdF162baJUn-e_Y8zTRkYJJnnDu8bNOq04Ej5d2VF7TNoZgZeUcxyP40P4MBu4xE2syF8xkDpEiQbtCeNmfioCaMKgbFPSZ-GRt1z2p9OjGly3I6ap6gVLnrgN0_oDaPnADRjKZl-IS2b8eLfaUwb247k1rXtJR4TkBfI3YDxa9qkRpQEC4wxGS4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا: ما نفت صادر می‌کنیم، ایرانی‌ها صفر؛ نتیجه ۱۴۰ میلیارد به صفر به نفع ماست!
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/146890" target="_blank">📅 16:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146889">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51fe8f52d9.mp4?token=nB8ukwdpAloy1WmjOx8XZstGqT_3trzE6q4E4RzGA_TSOUxpdAdbH5Lc7eHKyeI2a7_e3AXnLg3k6XiPwAzan-2P40jgKoAdnOD9vNQNtfuIi1Kjjjmq1UrL4X5GIvAeFQEftmFdJDMk6jvo8HKwaqaZUixsxPWOeS8Dak75yLpnjZKCHWdhX5Fb_6yDJF56-AIGgK5_q8zTbCKLY6qmY8ORZPQ1PWV76MArn2FfTkY3_UJ7Hcjlq2EJ1Mb-RkMvAlz4Mkab2nXXPBHV8L41-OSMdGNDalGNc6v-Jnzmyu1LbvIRjjQO8Xknl3EDZ_KC2E7Zb5Yes2n1-eXbMzkOuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51fe8f52d9.mp4?token=nB8ukwdpAloy1WmjOx8XZstGqT_3trzE6q4E4RzGA_TSOUxpdAdbH5Lc7eHKyeI2a7_e3AXnLg3k6XiPwAzan-2P40jgKoAdnOD9vNQNtfuIi1Kjjjmq1UrL4X5GIvAeFQEftmFdJDMk6jvo8HKwaqaZUixsxPWOeS8Dak75yLpnjZKCHWdhX5Fb_6yDJF56-AIGgK5_q8zTbCKLY6qmY8ORZPQ1PWV76MArn2FfTkY3_UJ7Hcjlq2EJ1Mb-RkMvAlz4Mkab2nXXPBHV8L41-OSMdGNDalGNc6v-Jnzmyu1LbvIRjjQO8Xknl3EDZ_KC2E7Zb5Yes2n1-eXbMzkOuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسکات بسنت: هر آنچه که ایرانی‌ها می‌گویند، بیشتر یا بخش زیادی از آن، ریشه در خیال‌پردازی دارد.
🔴
بسیاری از این حرف‌ها، آرزوهای دست‌نیافتنی هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/146889" target="_blank">📅 16:22 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146888">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1144f5e406.mp4?token=o9rjquLW98pS16BruycVN5F0TZQVF8Gl55mVsFmbVSgiGh8O-JkKBx9miIvYH_dnOLBDAN_MKZ8jUfPLF0rwDdPKFXbGhX9tTB5uGrEwjOON-NS1-QkbfvC4qXG92j8p7KxnhYK0oj2VGbmIL1hddMG-Iivm9TOtDb1OzIl8IpmVBzutP0am02ac1FDXoKd0xvplecDdR0klsCwNNSGRx7eBDvgRFimrZHG22njobVD1_WvWy2DdltbIqQ3vzlguYDSghqy6pF509MrlhZk-nZKA6m1rnsxeXdEJsXpQrQg7G7m2mqi5KTAC4Ze4SRxnAiKfVaFfMlH7ovrg2ah4OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1144f5e406.mp4?token=o9rjquLW98pS16BruycVN5F0TZQVF8Gl55mVsFmbVSgiGh8O-JkKBx9miIvYH_dnOLBDAN_MKZ8jUfPLF0rwDdPKFXbGhX9tTB5uGrEwjOON-NS1-QkbfvC4qXG92j8p7KxnhYK0oj2VGbmIL1hddMG-Iivm9TOtDb1OzIl8IpmVBzutP0am02ac1FDXoKd0xvplecDdR0klsCwNNSGRx7eBDvgRFimrZHG22njobVD1_WvWy2DdltbIqQ3vzlguYDSghqy6pF509MrlhZk-nZKA6m1rnsxeXdEJsXpQrQg7G7m2mqi5KTAC4Ze4SRxnAiKfVaFfMlH7ovrg2ah4OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بسنت: روزنامه وال استریت ژورنال گزارش داد که ایرانی‌ها در حال بازسازی ذخایر موشکی خود هستند.
🔴
شاید همینطور باشد، اما میزان و گستره این بازسازی چقدر است؟
🔴
ما ۸۵ درصد از کارخانه‌های آن‌ها را نابود کرده‌ایم. پس آیا آن‌ها هر هفته یک کارخانه جدید می‌سازند؟ آیا دو کارخانه می‌سازند؟
🔴
می‌دانید، این‌ها فقط تیترهای خبری هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/146888" target="_blank">📅 16:17 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146887">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a99219ae2c.mp4?token=TrPEWQ_tcU6XYQrFkD90W4qzE0OagQHDZhCAyHH9cCugmPD-DwUr2HSFPlLvAF4P4me0J4mO1Kbb64ZoaMLDL6-w-Wyz8pyN_bxOzRZ_yj7CaKvggUTfvdIZVZUZ7Y2DWJ2SGdJUWNOhYPyfMoTtTe_qtNeu2cQZFUUeBml6_XU-RHCpYcv6vtuJAor5zsdvihfRShsGQyOl6Ve6RweVZ_UaGrSuIU35OnVhtHoMMb1a_enYSOg1C7McfTD61RP61nzE6cKo-hcLQaVRV8GtNVwoMzLsiqSBVUPIpFbGc-qU8CMVLUDX2WTHoJqRNB_JNsAKf_MgDvJrcqUyQ9R68A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a99219ae2c.mp4?token=TrPEWQ_tcU6XYQrFkD90W4qzE0OagQHDZhCAyHH9cCugmPD-DwUr2HSFPlLvAF4P4me0J4mO1Kbb64ZoaMLDL6-w-Wyz8pyN_bxOzRZ_yj7CaKvggUTfvdIZVZUZ7Y2DWJ2SGdJUWNOhYPyfMoTtTe_qtNeu2cQZFUUeBml6_XU-RHCpYcv6vtuJAor5zsdvihfRShsGQyOl6Ve6RweVZ_UaGrSuIU35OnVhtHoMMb1a_enYSOg1C7McfTD61RP61nzE6cKo-hcLQaVRV8GtNVwoMzLsiqSBVUPIpFbGc-qU8CMVLUDX2WTHoJqRNB_JNsAKf_MgDvJrcqUyQ9R68A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: بریکس نباید صرفا مصرف کننده فناوری باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/146887" target="_blank">📅 16:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146886">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
پزشکیان: ایران آماده است در کنار اعضای بریکس برای ساختن اقتصادی بازتر و عادلانه تر تلاش کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/alonews/146886" target="_blank">📅 16:08 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146885">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/29761d0702.mp4?token=grlYjGCUXfcmLHAGF7eIv02cuUv4S6RbiYMqO2TTVYEi9sfHoIKKy5ioQ76ymaDUlBHXt1wWqcanaHvDgYZSXx9jVw-raAWfOWNt5NMM5p6VBbx4-Z1KmHX5IehCyBbcxYstXoY8JTBwUhVG5WgWVNkJ6dzhiXdwcUw0Y5ckviRoqlrHpfKWwc2KJtHiU23ssvK5sNfNOp_FstSYOgqydJTHverK-PVbqwMG5mXP5fwmxItiKd2-J5V2xbApu9-672sgS2lYYiezrg1AkakPqoPSZtYUwXb3cHKvYPFQSj6dLNBIBjvIjyWQ3Vm3SJVZ3HM3Ixy1SUxYx__h7SC30w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/29761d0702.mp4?token=grlYjGCUXfcmLHAGF7eIv02cuUv4S6RbiYMqO2TTVYEi9sfHoIKKy5ioQ76ymaDUlBHXt1wWqcanaHvDgYZSXx9jVw-raAWfOWNt5NMM5p6VBbx4-Z1KmHX5IehCyBbcxYstXoY8JTBwUhVG5WgWVNkJ6dzhiXdwcUw0Y5ckviRoqlrHpfKWwc2KJtHiU23ssvK5sNfNOp_FstSYOgqydJTHverK-PVbqwMG5mXP5fwmxItiKd2-J5V2xbApu9-672sgS2lYYiezrg1AkakPqoPSZtYUwXb3cHKvYPFQSj6dLNBIBjvIjyWQ3Vm3SJVZ3HM3Ixy1SUxYx__h7SC30w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: بریکس باید فضایی را ایجاد کند که هیچ کشوری نتواند تجارت مشروع کشورهای دیگر را مختل کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/146885" target="_blank">📅 16:08 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146884">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SJ_iIRLfhD_CKtzFrXUA7qhcfFKhuDR9H8TKr4F0Yf-FjBLHRq9b2ovrNpYh1RLyViiqf_KI35sDgsjOevBvTqWfeCTZAZCF5Z-3wt5IdVJPFt73JjRRXVyocEAGKDw8ABXwYkmurETa2HtoBBln7sp_Kez6WLSjUDnBmaW-qmBk5tF4VS59sMCcuyRjMO7C9VUGLRIxXsLRz9L7xx6QAWKkY9EG8nD3-G78NUlAP69yABNGXeA1Fh61X_uqMsCpCCWVOVW2IExKzt3xPAxaxbEg8_sqWa-hjJP8Vs7rJ436JVM4e7dOJGaOMagWjZWsDBDq8FIleSxEbZ2FwWaJ_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سازمان‌ملل با ۱۶۴ رأی موافق در برابر ۱ رأی مخالف تصویب کرد که نقشه مرکاتور کنار گذاشته شود و از نقشه "Equal Earth" استفاده شود که سایز واقعی کشورها را نشان می دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/146884" target="_blank">📅 16:07 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146883">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
علم‌الهدی: دشمن تا ۲۰۰ هزارسال هم بجنگه، باز دفاع میکنیم،‌ تسلیم نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/146883" target="_blank">📅 16:02 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146882">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad5d711ee2.mp4?token=kS0oJBEdx5Iep5ekEYZHwUsuBO2Xmfe3CchZTLX_epmB2XpQWfdCAPYQUkB5gOj5iOykNjPiIN1cMilsQ8KfZmWXAnrKV-YzqZ2TwAgSX4BhXy5jGNKeohe6Wt6hDNugw_w1mPlziA_hPjlQ43tPtmJ7HvrL6LX13bwbuPK85lMktiYpC1ytkqrKsjVxA9KMPZBYhj8nYnwleEyHAsIcATiHIPfptQcr7I9Rx9j84jbH7w8YJoXe8e_fMxIXNDvO3KOMM2uDt0HRA5ObXH5EMKh10efE0nksd2nsbjiuD5ggPOxe3yC8IFxNsl07iiFI8Q8zb3-OKn6uMGc4hmortg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad5d711ee2.mp4?token=kS0oJBEdx5Iep5ekEYZHwUsuBO2Xmfe3CchZTLX_epmB2XpQWfdCAPYQUkB5gOj5iOykNjPiIN1cMilsQ8KfZmWXAnrKV-YzqZ2TwAgSX4BhXy5jGNKeohe6Wt6hDNugw_w1mPlziA_hPjlQ43tPtmJ7HvrL6LX13bwbuPK85lMktiYpC1ytkqrKsjVxA9KMPZBYhj8nYnwleEyHAsIcATiHIPfptQcr7I9Rx9j84jbH7w8YJoXe8e_fMxIXNDvO3KOMM2uDt0HRA5ObXH5EMKh10efE0nksd2nsbjiuD5ggPOxe3yC8IFxNsl07iiFI8Q8zb3-OKn6uMGc4hmortg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عکس یادگاری سران بریکس در دهلی‌نو
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/146882" target="_blank">📅 15:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146881">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dcf6775e9.mp4?token=fjs7Qm6xu7sE5Y7XW-7Hv9WL4lTH-GWJR2Mnt2mj6yPahI0tkI1G_VWNNv6zCM1YBiNKdJk7pT_DHXhrBqw8Eahl3qgRhRn-Op5KXh4abVFbMRZOWRXWacUlpn3YCZq8ib36EyA6eu36vsbex-8tw1e9RPW-HB3R-1GCcFVYNoDQ64kEblTx2xiDOtX1B8ep2JZ1ad3Fq8Pm0QdJehZ-H4sgyVbdieQSOzIp_d-hyoTf-lwqwNgsRC95GLG84bzWthA59icqitqIOqyR_HfVp9u3qN8rIbZOngbdHuYtE7roo2RTSaktDq7ofwLNkctjKEcJZ8z2v5ERXKIfFvoAJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dcf6775e9.mp4?token=fjs7Qm6xu7sE5Y7XW-7Hv9WL4lTH-GWJR2Mnt2mj6yPahI0tkI1G_VWNNv6zCM1YBiNKdJk7pT_DHXhrBqw8Eahl3qgRhRn-Op5KXh4abVFbMRZOWRXWacUlpn3YCZq8ib36EyA6eu36vsbex-8tw1e9RPW-HB3R-1GCcFVYNoDQ64kEblTx2xiDOtX1B8ep2JZ1ad3Fq8Pm0QdJehZ-H4sgyVbdieQSOzIp_d-hyoTf-lwqwNgsRC95GLG84bzWthA59icqitqIOqyR_HfVp9u3qN8rIbZOngbdHuYtE7roo2RTSaktDq7ofwLNkctjKEcJZ8z2v5ERXKIfFvoAJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترکیه مرز بازرگانو به روی مردم ایران بسته و اجازه نمیده مسافرین ایرانی وارد ترکیه بشن
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/146881" target="_blank">📅 15:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146880">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
وزارت امور خارجه : گروسی گزارش‌های به اصطلاح بی‌طرفانه آژانس بین‌المللی انرژی اتمی را به ابزاری برای توجیه آغاز جنگ‌ها تبدیل کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/146880" target="_blank">📅 15:39 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146879">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/REPpIp5andTEJDXkobcEm3Fj0DcObBNSyaP1Of1iouWu7bb2jcFudQpZJgDUj4BGz7UeVnlIBjSSoyT5O6a-KLDQTrdUqK2Iq87-2mPMaq37VglYBlWlT31ZdqBhzoV1OQUV-dMO4Dh3MkBl317O6bF-4lr9mgnGP9Rkn1zXfYY9jHNkNtEl_CGj-V9cUgs_JqtEl0-Fza-0XH9LK81Et5Uf1_q1KWIxRQ6j1BgmhswQxSL4SorExRHWg2GvseuMVcnugPaLkAUbdIse9vTeEBfVDFzVARnXhuOJjAhjP1BBdQGSUeSRMjFjt17JbHxatoRIXOTVwmuuBX9W9NjoCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چندین انفجار در شهرک المنصوری در جنوب لبنان رخ داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/146879" target="_blank">📅 15:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146878">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
فوری / وزیر جنگ اسرائیل: برای حمله به حزب‌الله در سراسر لبنان آماده ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/146878" target="_blank">📅 15:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146877">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0be2bebccb.mp4?token=EU-e2tpPOGP-8LOG9YFr9X0NewSzf783tWNVdTT2QvELibZQQCCcxoD2kDT7HYPN0urfEbxicfJ7vTRZ4r3ImIJ9gVqegncIYZdMtteNeDlaKu84AcPurokcV8VBMlfraHB2V7irUh7XPNvzUWzM_H1wwdXovihvGCe1rUI_x-yKmXhe83Ev3U11sCFpPWpgCQJW3IEL4S1-wJKggfHqc9ph3dEzxgHRcNHoC9u9Smd_WCLyjSTYVoqTBANIoEKXU_J3WlOD7blcL_hQ42L3ytWwtUroRjsHNvugMPFNKTlxzRrdLHpgtzWCg8iC_HaANDahdjZa8vEswOvUNqFB-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0be2bebccb.mp4?token=EU-e2tpPOGP-8LOG9YFr9X0NewSzf783tWNVdTT2QvELibZQQCCcxoD2kDT7HYPN0urfEbxicfJ7vTRZ4r3ImIJ9gVqegncIYZdMtteNeDlaKu84AcPurokcV8VBMlfraHB2V7irUh7XPNvzUWzM_H1wwdXovihvGCe1rUI_x-yKmXhe83Ev3U11sCFpPWpgCQJW3IEL4S1-wJKggfHqc9ph3dEzxgHRcNHoC9u9Smd_WCLyjSTYVoqTBANIoEKXU_J3WlOD7blcL_hQ42L3ytWwtUroRjsHNvugMPFNKTlxzRrdLHpgtzWCg8iC_HaANDahdjZa8vEswOvUNqFB-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسموتریچ وزیر اقتصاد اسراییل : وقتی مردم ایران چیزی برای خوردن نداشته باشند دیگر چیزی برای از دست دادن ندارند و این باعث سقوط رژیم می شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/146877" target="_blank">📅 15:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146876">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iLiu8l7Gg47h-OT6N37At5CR5o6BARf7jcm9tqdODRRk1ymLv9-KnIprAbXIB9ac_NKf0u2YmNBMZUdAx-T9vJ-DHgM55imjgC4VJ657LZcj9XUAPSYxTmt9MsqYw6CfFHjXZMkDs1L4OxFqK60M8Yv8O2sVBDNG9hu44e7GSB3iprAH5quR2R6XVAyYEFkbUKoGEX4cdJT9ZFTe4jOqbjoeXlyL9fN3XSwLdRTSiL_TJdKW1TBhA4SmWjZFkWxZSEf1Ds43CgV14adAstdJgN4RusUWLAQSk6T_mwlBhtLcOWm3q89wkuti-UaVCOCJ1iyLPGlAr_VU1z5VMuQg-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروهای یمنی به شورای محلی منطقه "ذو باب" در نزدیکی تنگه باب المندب رسیدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/146876" target="_blank">📅 15:18 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146875">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
المیادین: امروز نیرو های تحت حمایت عربستان سعودی در استان البیضا، در جنوب یمن پیشروی گسترده ای داشتند و به ورودی های پایتخت این استان نزدیک شدند، دو استان الجوف در شمال یمن و البیضا در جنوب یمن در آستانه سقوط قرار گرفتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/146875" target="_blank">📅 15:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146874">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
اتحادیه اروپا ۶.۱ میلیارد یورو دیگر به اوکراین اختصاص داد
🔴
اتحادیه اروپا اعلام کرده ۶.۱ میلیارد یورو اعتبار تازه برای تقویت توان دفاعی اوکراین اختصاص خواهد داد.
🔴
براساس این بیانیه، منابع جدید صرف خرید تجهیزات پدافند هوایی و موشکی، مهمات، پهپادها و سامانه‌های جنگ الکترونیک خواهد شد و خریدها از شرکت‌های مستقر در اتحادیه اروپا و اوکراین انجام می‌شود.
🔴
اورسولا فون‌درلاین، رئیس کمیسیون اروپا، گفته این تصمیم به کی‌یف امکان می‌دهد تجهیزات مورد نیاز خود، از جمله سامانه‌های پاتریوت، را برای حفاظت از حریم هوایی اوکراین تهیه کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/146874" target="_blank">📅 15:11 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146873">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=fWYyb0FJ5YhRwM-VxMFA9Ut_Lz753GdsE8kUfI7oyhnglW9JNs3XMulcE1FaIQGctUjg1we7JbU0TrNveknb3gGEGWwp0ghtJ36oynrPztYfTIifLBVS10JRr8xtNLF-ecrtLyBSQHNrH1qe-63zGKLQAm4gW931NkRSljDmCO8y_GyicEWVz8phPRbLddD0rKfJI2qm5mZbCo2V3nrOIINQQme78DO_rsI7Q_93-g-buRWAwNPr6GzfHjULWG4UFrQcGOkAetu3zGM_Nccvk4tPH2OmmfzKyag6EOYPC9DQ-qRyRrb_DK9I8M6Er9oqmgB-N3AIwX7g-FZGGYS2qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=fWYyb0FJ5YhRwM-VxMFA9Ut_Lz753GdsE8kUfI7oyhnglW9JNs3XMulcE1FaIQGctUjg1we7JbU0TrNveknb3gGEGWwp0ghtJ36oynrPztYfTIifLBVS10JRr8xtNLF-ecrtLyBSQHNrH1qe-63zGKLQAm4gW931NkRSljDmCO8y_GyicEWVz8phPRbLddD0rKfJI2qm5mZbCo2V3nrOIINQQme78DO_rsI7Q_93-g-buRWAwNPr6GzfHjULWG4UFrQcGOkAetu3zGM_Nccvk4tPH2OmmfzKyag6EOYPC9DQ-qRyRrb_DK9I8M6Er9oqmgB-N3AIwX7g-FZGGYS2qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صدا و سیما:
گازوئیل تو آمریکا ۵ سنت گرون شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/146873" target="_blank">📅 15:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146872">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5db101496.mp4?token=hHZ7U2x5cFHVLuyh-XoCGVhv8e7q6ElCNUq9SdjFWCFFEjfhf511Wtt2IXP7FrXjZ9jpulVkcJXxtlO_9U9F0bWXppLV1PWx_PbNbN-SvLlmZ3S5IBAOcg3Xs2NYWzwHOorkOinGmlf7GfCfWforF9L9_SIFb6vIL05V0tIIc7rOZzGupNU7frB71OxLs9GObcNF_WSyam7i5zTkH3UmIAl8kbRMc9TglaMa0L33-71zAiiBiInrwRq1Y7ON2VmE-D8jsMq-QCDNHfkFJXAEVhiZktA1faa3kVK7NQVH-08fPszfVYoG9fZAebIIkPXz7seRWsFikzHDgYx9eSPtp2lGTqC2_jMUp7OP21YOFCorcGu0lw9aJBPCOD6XGiZjzj9pxNAG-11wsVzgLzNX3YPfOH7Q8pybAfKUS-cxbawtlIrRvQBxHOnWKYLhMBi4exuM6BApo3NPtp98DMC3rJAOpJn83sbAWurfl0QtLIxpVP568ezHhCiW5J3itLOjx0OuEjp2dpcs-7PcZmBWfuQhdP_YwB9bXdDGzzHUbcq2rzpiVtEYn5lpCTZF9kOLmyMnU9rbtgLW1z5SqZOwpcPNaYx_v1ZvCAcjX03shgYFQ0ZvbUAYygRVlKd4ZV8S1KrF41gw55JQ3pfkbbSrRLqe44mtTyXCplqM15g903k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5db101496.mp4?token=hHZ7U2x5cFHVLuyh-XoCGVhv8e7q6ElCNUq9SdjFWCFFEjfhf511Wtt2IXP7FrXjZ9jpulVkcJXxtlO_9U9F0bWXppLV1PWx_PbNbN-SvLlmZ3S5IBAOcg3Xs2NYWzwHOorkOinGmlf7GfCfWforF9L9_SIFb6vIL05V0tIIc7rOZzGupNU7frB71OxLs9GObcNF_WSyam7i5zTkH3UmIAl8kbRMc9TglaMa0L33-71zAiiBiInrwRq1Y7ON2VmE-D8jsMq-QCDNHfkFJXAEVhiZktA1faa3kVK7NQVH-08fPszfVYoG9fZAebIIkPXz7seRWsFikzHDgYx9eSPtp2lGTqC2_jMUp7OP21YOFCorcGu0lw9aJBPCOD6XGiZjzj9pxNAG-11wsVzgLzNX3YPfOH7Q8pybAfKUS-cxbawtlIrRvQBxHOnWKYLhMBi4exuM6BApo3NPtp98DMC3rJAOpJn83sbAWurfl0QtLIxpVP568ezHhCiW5J3itLOjx0OuEjp2dpcs-7PcZmBWfuQhdP_YwB9bXdDGzzHUbcq2rzpiVtEYn5lpCTZF9kOLmyMnU9rbtgLW1z5SqZOwpcPNaYx_v1ZvCAcjX03shgYFQ0ZvbUAYygRVlKd4ZV8S1KrF41gw55JQ3pfkbbSrRLqe44mtTyXCplqM15g903k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از خودروهای متعلق به نیروهای سعودی و اماراتی که این نیروها در هنگام عقب‌نشینی خود به سمت شهرهای جنوبی، آن‌ها را رها کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/146872" target="_blank">📅 15:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146871">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
خبرنگار صداوسیما: یک شهپاد آمریکا امروز توسط نیروی دریایی سپاه مورد اصابت قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/146871" target="_blank">📅 14:46 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146869">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jBPb8Rt6BD7YL6f-hRTYbYLW-JunmnxJrJaT05uxj_eZso9wCFfGoFjt-P45-zUj5ovh3KeZ0WBgRX-FXPR_4MHFiCuxTVcN4btln3iJXZw9hwN-GiZVl08Bl6BeTrX-bqcXFe44r9dJfm5fvLcst1_U84yNiM4ooBBRwpTSJf-vVUSQZ1EZS2DKR_GJ8lfyF_9-ovykyga-uw9Szd4uAnM4s9AgzDXV6sAYRUU6utaijuX63b1zfTOKbUmSA2C5LJRGVqsh7BC51Gf7BQpUq1ZXxGy0NntP8uEIYIDQ-QMrEvaD5RWJWyi7pm_v87ISX9rBHr-thivlfIpMRkwABg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KUy0O0tWLkKEUAFnA04JCp2q8y9N7bb3zQX29B8NNOXnKzWldtQMq8wMqcgj8COM-GCLOYm3wGr-_mGN-fsOP6b6wSRLwqrWG2bpHMXr6es6t8P4t68PMBGg_pYlsbulS35wOH9Ze9L2e4wpnWvbhQJYcXRqDtFd3ycIVGjGBAnxmDl8dXvQ62MzbEj0rs-UkFe83Lw3tvLyuZb1roFXVzD0w-wWUlS-1ahwVHORZgd7nZf0ZLAX__i7h8nGr3EmC2OtYQclN-HyxG-Nsj7yIjHo0veo_jUxOBA9g4KRRlRcuwmZg_bKfzfbmPyWoj7vdqstRU4nFxxiqVoOG-DG1w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
انفجارهای ناشی از عملیات اسرائیل همچنان در شهرک اشغالی المنصوری ادامه دارد و از بامداد تاکنون بیش از ۲۰ انفجار در این منطقه ثبت شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/146869" target="_blank">📅 14:42 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146868">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faeb6ddc51.mp4?token=m11n1amkcNeAwpLQ5Sn8PcU7cePKhHKNMbRG8oE78PRJU_Dd7W6eni9J1rpAbswHsvvwRx_9xzNimfRAJZ_9XKzBr6Rw0vRNsEyqHsgN-uRMxMuRweFlgwDX3JR2UjQTHYgcotsUiUj2NCZQwlyt8L-52kgELUC9WwQvhzzauIT0eufy0Zxf88wpX2sDGHaXiPVE7LgejwBYViQzzu47XEt3ZHm1Zi6FiHfSfqJK8bLQaEkz0bF4XpRJNP52-DlciZcAK353WvhF8OFwXPfI0YBw5OlvuWKZLSAEl3rRSz3motfIaHlNd1ox-_EigVGU2KDYQ8HJQiWskXav5gqr5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faeb6ddc51.mp4?token=m11n1amkcNeAwpLQ5Sn8PcU7cePKhHKNMbRG8oE78PRJU_Dd7W6eni9J1rpAbswHsvvwRx_9xzNimfRAJZ_9XKzBr6Rw0vRNsEyqHsgN-uRMxMuRweFlgwDX3JR2UjQTHYgcotsUiUj2NCZQwlyt8L-52kgELUC9WwQvhzzauIT0eufy0Zxf88wpX2sDGHaXiPVE7LgejwBYViQzzu47XEt3ZHm1Zi6FiHfSfqJK8bLQaEkz0bF4XpRJNP52-DlciZcAK353WvhF8OFwXPfI0YBw5OlvuWKZLSAEl3rRSz3motfIaHlNd1ox-_EigVGU2KDYQ8HJQiWskXav5gqr5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ولادیمیر پوتین پیش از برگزاری نشست سران بریکس، با نارندرا مودی در دهلی‌نو دیدار کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/146868" target="_blank">📅 14:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146867">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
اکسیوس: فرمانده سنتکام برای بررسی پیشروی‌های انصارالله به عربستان سفر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/146867" target="_blank">📅 14:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146866">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YGD6K2A_qB05pbUyd7ZPu-U71Bbb71zYTCBiTmge7IGrEd5BMmePSp511OFeeRMLQpUL5dKCnvkFMyJmJ43ckYEYgyJDgAoGhowWNqGN9_XWlNfx83-NI9t_hUVKC_TCC6yWeqwZj-rGDWLknxiYShj-Tp8Gmb2pQrXh2_PbneigJwLYOnI_d1h5WbspRM7_JmuUb3IZh3oX3BOefKxdYCu7irTmN6pdkwQGG9WMLpJqdfHyT-ZtxzJhqLFotUc0CHYyKCPmTNoO86kdSqCsyKsQVZCZsn_m0kv5yPOsXL1oWYVG-tiBPIsiR313pssNncOtVns9WqLv-Djd9JZJ3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بلومبرگ: به دلیل جنگ‌ های ایران و اوکراین تولید نفت خام ریاض و مسکو مجموعا در ماه گذشته حدود ۵.۵ میلیون بشکه در روز کمتر از ژانویه ثبت شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/146866" target="_blank">📅 14:22 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146865">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b97ba68995.mp4?token=QktY6uGqeRobWrD82S1zPOKj7H1K6sKCUUKkyI8ZE7FRR9I9yuF2ejeZpZlSgxKsYMPx4_F0ynDIsg-NAz5kgyFWADdSvngbiOBIbNcQ3EltyhCRXzix-ZIKwN-vehY-KSWpkuEE22yziHwREe6AhJy9slA8gnuUo0nEkK1f4M5QtjA4zkHjlwjmOuQHBLTh0goCBJsIcgnLFpPuvcm3z51OKSI8oM9yH48UANR784bu3S_LnM6FOms81fA6Ny4A_gsXm26ickq68L7cBht1T0A569zNfqIu312h2wO2V3L0KZmArpbhi1-lzzE6icSTVQk8WUz2G9PMQtdwEmRV4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b97ba68995.mp4?token=QktY6uGqeRobWrD82S1zPOKj7H1K6sKCUUKkyI8ZE7FRR9I9yuF2ejeZpZlSgxKsYMPx4_F0ynDIsg-NAz5kgyFWADdSvngbiOBIbNcQ3EltyhCRXzix-ZIKwN-vehY-KSWpkuEE22yziHwREe6AhJy9slA8gnuUo0nEkK1f4M5QtjA4zkHjlwjmOuQHBLTh0goCBJsIcgnLFpPuvcm3z51OKSI8oM9yH48UANR784bu3S_LnM6FOms81fA6Ny4A_gsXm26ickq68L7cBht1T0A569zNfqIu312h2wO2V3L0KZmArpbhi1-lzzE6icSTVQk8WUz2G9PMQtdwEmRV4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: آیا نگرانی‌هایی در مورد این دارید که هوش مصنوعی ممکن است منجر به انقراض انسان شود؟
🔴
ترامپ: خیر، من هیچ نگرانی‌ای در این باره ندارم. نگرانی من این است که اگر ما در زمینه هوش مصنوعی پیروز نشویم، در موقعیت بسیار بدی قرار خواهیم گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/146865" target="_blank">📅 14:18 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146864">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
ترامپ : لطفاً دست راست خود را بالا ببرید: «من به بزرگترین رئیس جمهور در تاریخ ایالات متحده، که ما را آنقدر دوست دارد که حتی نمی‌تواند نفس بکشد، تعهد می‌دهم که من با خانواده‌ام، با دوستانم، به هر شکلی که شده، این کار را انجام خواهم داد - مهم نیست که آیا ثبت نام کرده‌ام یا نه، من تمام تلاشم را خواهم کرد تا مانند آن‌ها تقلب کنم... من خواهم رفت و رأی خواهم داد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/146864" target="_blank">📅 14:18 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146863">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ca989d528.mp4?token=AicuX37NC4mcoG2gj7TyfIcUVxGSPcHWimF4EcN-LzScGV5QpUrUeLN3ZuhKA2r9ovHorYUgf1KfwmFSPlwiQPSbERIW3ouWZGw6F73U6oTZMELiDk_YcagjX0lE7uACLKxqDIfi0DUrHO5egeugh2Eo-PRrHPnUD5A05b4F1Zfh3vG9_VLj_nWW9L7dg5vN1EKpmxZqXFUyClxoCd-wl8_ekeUnxfgc2bu9wpFyKVIhuY19HIQ13_5xNuu8BqguZX-Yh9wlN_z3q3y4bUc9upitEWuLvKE5IWxofMtT69xjh_fyey9ROCZ-UVTacVDyYRSERQYSlCth5qREUaGjlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ca989d528.mp4?token=AicuX37NC4mcoG2gj7TyfIcUVxGSPcHWimF4EcN-LzScGV5QpUrUeLN3ZuhKA2r9ovHorYUgf1KfwmFSPlwiQPSbERIW3ouWZGw6F73U6oTZMELiDk_YcagjX0lE7uACLKxqDIfi0DUrHO5egeugh2Eo-PRrHPnUD5A05b4F1Zfh3vG9_VLj_nWW9L7dg5vN1EKpmxZqXFUyClxoCd-wl8_ekeUnxfgc2bu9wpFyKVIhuY19HIQ13_5xNuu8BqguZX-Yh9wlN_z3q3y4bUc9upitEWuLvKE5IWxofMtT69xjh_fyey9ROCZ-UVTacVDyYRSERQYSlCth5qREUaGjlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: ما تنگه را کنترل می‌کنیم. من آن را "تنگه ترامپ" می‌نامم
🔴
ما "تنگه ترامپ" را کنترل می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/146863" target="_blank">📅 14:17 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146862">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64134abd7d.mp4?token=aI01aiGeIoNlyqenuQVm_02r2LYJIhI96e5AyLuVcuFfDb9ULPaTpBSYkTujV1wRUixh5ssHufEiBoOFaelm8wMctxAgl4kenFm9hvJbWvsWMFGX6l8fVcDIrABCmheNvsfUXRS7KcyX3UJkhCMxbVIIECDcXNQDRXtzIL1qhSQyzGFORZevchTjNWVUW9gtTqAbUMLwsCG3YMLUPiX1btBxRIhdjTwokdh5VFGvGH8piAnkg6411sZRUzZVMHyfdQHMpou5pfbUAT2KoW8gwJ2qf6wWUuV6IajyJ5y42Gs21t1sZYdedemocTJg5-NFINIifZEfn7K4L2U8tnQEgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64134abd7d.mp4?token=aI01aiGeIoNlyqenuQVm_02r2LYJIhI96e5AyLuVcuFfDb9ULPaTpBSYkTujV1wRUixh5ssHufEiBoOFaelm8wMctxAgl4kenFm9hvJbWvsWMFGX6l8fVcDIrABCmheNvsfUXRS7KcyX3UJkhCMxbVIIECDcXNQDRXtzIL1qhSQyzGFORZevchTjNWVUW9gtTqAbUMLwsCG3YMLUPiX1btBxRIhdjTwokdh5VFGvGH8piAnkg6411sZRUzZVMHyfdQHMpou5pfbUAT2KoW8gwJ2qf6wWUuV6IajyJ5y42Gs21t1sZYdedemocTJg5-NFINIifZEfn7K4L2U8tnQEgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : ما کنترل منابع نفتی ونزوئلا را در دست گرفتیم - ۶۵ میلیارد بشکه نفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/146862" target="_blank">📅 14:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146861">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/566fe0667f.mp4?token=Yf7bl-bNRjP98UVwePPLN40iDghkyzt6Bo9Sm0-Wt2dsfr0OEq3J5a6yWqjEHe7GjdtWcyGo_1jknVZ-a-BtffU9t7Jg4cc60GQH1Wr1cHV_45VGSl41o0lw-2adJPQ0i37il7wBA4uNji4VT9uhrFkPs4K_MSqB751-KNizJk7AATh0RzTZ-m86vzHq8H97VYvk5edA2k0944LPgNRW2yIqpYoDKNkLgkd9HtA3bL_vFt4M1Usb3JIcrnY5N94d_RX26vid8BsDZ49hQzaxkFZWo0nTTHXUQttX5O61xSJQCt4xoyASoTx-_zUyYk3Mdcfilx7RHKw0vsB9PmuMcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/566fe0667f.mp4?token=Yf7bl-bNRjP98UVwePPLN40iDghkyzt6Bo9Sm0-Wt2dsfr0OEq3J5a6yWqjEHe7GjdtWcyGo_1jknVZ-a-BtffU9t7Jg4cc60GQH1Wr1cHV_45VGSl41o0lw-2adJPQ0i37il7wBA4uNji4VT9uhrFkPs4K_MSqB751-KNizJk7AATh0RzTZ-m86vzHq8H97VYvk5edA2k0944LPgNRW2yIqpYoDKNkLgkd9HtA3bL_vFt4M1Usb3JIcrnY5N94d_RX26vid8BsDZ49hQzaxkFZWo0nTTHXUQttX5O61xSJQCt4xoyASoTx-_zUyYk3Mdcfilx7RHKw0vsB9PmuMcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: شما می‌دانید چه اتفاقی می‌افتد اگر رای ندهید: شما به جهنم می‌روید.
🔴
من نمی‌خواهم این اتفاق برای شما بیفتد، پس لطفاً بروید و رای دهید
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/146861" target="_blank">📅 14:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146860">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
اکسیوس:فرمانده فرماندهی مرکزی ایالات متحده دیروز، پنجشنبه، به عربستان سعودی سفر کرد تا جلسات اضطراری درباره پیشرفت‌هایی که حوثی‌ها در یمن داشته‌اند، برگزار کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/146860" target="_blank">📅 14:08 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146859">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
وزیر دارایی اسرائیل، درباره ایران:
«در نهایت، ترامپ کاری را انجام داد که هیچ رئیس‌جمهوری پیش از او انجام نداده بود. ما در این کار، شانه‌به‌شانه یکدیگر پیش رفتیم.
🔴
او این کار را در شرایطی انجام داد که تنها ۴۰ درصد از مردم آمریکا از آن حمایت می‌کردند.
🔴
من سیاستمداران زیادی را نمی‌شناسم که حاضر باشند برخلاف پایگاه سیاسی خود عمل کنند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/146859" target="_blank">📅 14:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146858">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebf8674ee4.mp4?token=TovOl9SlEXmUKuiBszxOFtMjrFymW45msc81w_UmJokIcEBuJv0BDSTWtOnOLnWs811qisV-s2IOVyOGSXkLMeaAVntClPBYroXAuZs8HYxX4fipZNtk5iHtEB3Edd97wVtTCMnQWWudq2MGCw-ryXwbiWhxXHtJW9KUE-cydH6upG9Aw97rggC8X8vFcJcEPMAWQ4dyP9AB7eTKDoA4XWKmaQ9RfK77s5HT5og7GPSn_AdCKqamjicuJvynWDtaUK5yF3crNOJ-J9jx6qkcEXOP-oeo_rH2GG9gPYL4J972y9PH6lf7SoLZ6NhYy648jv27nzCBaXW8-i2PniaMsjePtGwdw_nRbF5cfichLSr_S-tSWz2a70XPnjOpOjX7TqSxBPhg-UyL_VKRf6_4klrgL-W6zSy7NXCQxOD2rdG0KY9BCaI6Mm1NBPK1NORX-UXo1oBHRDsgq_L8Qop4gu3pLCCLQ7QgUdZBaljF9trbYTGpsCvshItkBDb9XwITAV9bfcfgHL5sjmjQnTF4aNY5YxdXAcF5n2Y8-3AAs673hxK2Uh4S7t31FrjMuLhmFvV0gWnrktMD-os5yeL2YgRA9EFZInwVQrm433z7txvhsD1eaQ-QUOfmErDYjANIzEZaPhznNK3Bt_ERIvHKgFc6auOgadqxColS7u3OzD4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebf8674ee4.mp4?token=TovOl9SlEXmUKuiBszxOFtMjrFymW45msc81w_UmJokIcEBuJv0BDSTWtOnOLnWs811qisV-s2IOVyOGSXkLMeaAVntClPBYroXAuZs8HYxX4fipZNtk5iHtEB3Edd97wVtTCMnQWWudq2MGCw-ryXwbiWhxXHtJW9KUE-cydH6upG9Aw97rggC8X8vFcJcEPMAWQ4dyP9AB7eTKDoA4XWKmaQ9RfK77s5HT5og7GPSn_AdCKqamjicuJvynWDtaUK5yF3crNOJ-J9jx6qkcEXOP-oeo_rH2GG9gPYL4J972y9PH6lf7SoLZ6NhYy648jv27nzCBaXW8-i2PniaMsjePtGwdw_nRbF5cfichLSr_S-tSWz2a70XPnjOpOjX7TqSxBPhg-UyL_VKRf6_4klrgL-W6zSy7NXCQxOD2rdG0KY9BCaI6Mm1NBPK1NORX-UXo1oBHRDsgq_L8Qop4gu3pLCCLQ7QgUdZBaljF9trbYTGpsCvshItkBDb9XwITAV9bfcfgHL5sjmjQnTF4aNY5YxdXAcF5n2Y8-3AAs673hxK2Uh4S7t31FrjMuLhmFvV0gWnrktMD-os5yeL2YgRA9EFZInwVQrm433z7txvhsD1eaQ-QUOfmErDYjANIzEZaPhznNK3Bt_ERIvHKgFc6auOgadqxColS7u3OzD4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بزالل اسموتریچ، وزیر دارایی اسرائیل، درباره ایران
:
«اگر ایران به ما حمله کند، ما به‌سادگی تمام تأسیسات انرژی آن را نابود خواهیم کرد؛ حتی تأسیسات داخلی.
🔴
نفت، گاز، پالایشگاه‌ها؛ ایران دیگر چیز زیادی ندارد، اما هرچه باقی مانده باشد.
این کار می‌تواند یک کشور را به فروپاشی بکشاند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/146858" target="_blank">📅 13:56 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146857">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2ae746b81.mp4?token=FNOeic67WzFiIru0DCIVArcIcxkLLMYmLJu8G7GvDbhnv-onCv8anPId6A7-E-TSvh3OVNKuDoIGUZil8sEJxmguIrlKJWAJM2AhZeam7azX24wwx3GvSvr5lTDSepMQupYQ2q3cwmBxhRKCUViw0zfUXupXDYIjrDK8nrybl6izwQsLNjZlm1TjMQceeYjl6m9U5g14CIEAeB7iM6Gb7KbF3nBYO_jDRWnp4vMTtPbPhkX0pua2lCn9Qs6o6waEh9XOwkzhdglWxJkmXCkQhXNWuNEaCN1xm0qNia4finuyC8D0NoWiLWpnI07ETAfiwQtH3gilhBGLi27nWuOx3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2ae746b81.mp4?token=FNOeic67WzFiIru0DCIVArcIcxkLLMYmLJu8G7GvDbhnv-onCv8anPId6A7-E-TSvh3OVNKuDoIGUZil8sEJxmguIrlKJWAJM2AhZeam7azX24wwx3GvSvr5lTDSepMQupYQ2q3cwmBxhRKCUViw0zfUXupXDYIjrDK8nrybl6izwQsLNjZlm1TjMQceeYjl6m9U5g14CIEAeB7iM6Gb7KbF3nBYO_jDRWnp4vMTtPbPhkX0pua2lCn9Qs6o6waEh9XOwkzhdglWxJkmXCkQhXNWuNEaCN1xm0qNia4finuyC8D0NoWiLWpnI07ETAfiwQtH3gilhBGLi27nWuOx3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بزالل اسموتریچ، وزیر دارایی اسرائیل، درباره ایران: «ما تحت فشار نیستیم. ترامپ تمام زمان دنیا را در اختیار دارد و
ما هم تمام زمان دنیا را داریم
؛ این آنها هستند که تحت فشار قرار دارند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/146857" target="_blank">📅 13:55 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146856">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f2c659dfc.mp4?token=FVdX2NVxHzcKXdm6ufIGt_eRtmtZSB6wVzH16iZMDaYF_wyUH1haNHQmm2ymFaFO1-s20IpxVtYQUrzuDmkwfOwy37wXVHxBi2QGd5jtSNHVB-lXUOmnftVg1EpIdJE9UhZ6yGuFKRhR7_2YZ5ZwRYJkyIuVkOY2BuX62xgfanUMPyqyO5DrGi2iPeuWzlPJuxWxUmTUZS4nu7-JeGDlubp328Y6L5Y5v13NrUL5P9xoIXDAYdX2Bn4o0irFCnXWJNjSG8sp-VqPe3QAl_r9z8L0R2pry4aO_H5WPMSXC1aesP3mgOWasrmEXX2ui33hWuil7R-hBvJQ2vz10IQZfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f2c659dfc.mp4?token=FVdX2NVxHzcKXdm6ufIGt_eRtmtZSB6wVzH16iZMDaYF_wyUH1haNHQmm2ymFaFO1-s20IpxVtYQUrzuDmkwfOwy37wXVHxBi2QGd5jtSNHVB-lXUOmnftVg1EpIdJE9UhZ6yGuFKRhR7_2YZ5ZwRYJkyIuVkOY2BuX62xgfanUMPyqyO5DrGi2iPeuWzlPJuxWxUmTUZS4nu7-JeGDlubp328Y6L5Y5v13NrUL5P9xoIXDAYdX2Bn4o0irFCnXWJNjSG8sp-VqPe3QAl_r9z8L0R2pry4aO_H5WPMSXC1aesP3mgOWasrmEXX2ui33hWuil7R-hBvJQ2vz10IQZfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بنیامین نتانیاهو: «هیچ زمینه و توجیهی برای زنده‌زنده سوزاندن خانواده‌ها وجود ندارد.
🔴
هیچ گلایه یا نارضایتی‌ای نمی‌تواند قتل عمدی افراد بی‌گناه را توجیه کند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/146856" target="_blank">📅 13:49 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146855">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0f323683f.mp4?token=PTtexrQkj51cXgC2blQtzV99S3vf4Oures_RGv-ZjmjQOaexB5e-VV7gZZ6gCD0UZkZ5LAfJ5w3VvllXgYfBjQRs4oFRX4kf66rHmp4uS9uAraVtMHKY5CU0kcUBbW3jVVKIi3AI-o6U2PELMPKmmQzF1QQgrE0GMkmflZiGx_Mci7v_VCLViX3YyxZlqucyc6ZSv7xaRDFsWYngHVh0IdJAq6PIAujjaLbtYMTpsvwmaogrJzUihn9hzdpCOLufLMYbG8IdSTWDIqjrj6tP_DbRjt19HNFGAIAd2dtq3lyp5U-oDoYIXGoUnFRJZ6eH5CzGdnzoywfJtffgpXUM3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0f323683f.mp4?token=PTtexrQkj51cXgC2blQtzV99S3vf4Oures_RGv-ZjmjQOaexB5e-VV7gZZ6gCD0UZkZ5LAfJ5w3VvllXgYfBjQRs4oFRX4kf66rHmp4uS9uAraVtMHKY5CU0kcUBbW3jVVKIi3AI-o6U2PELMPKmmQzF1QQgrE0GMkmflZiGx_Mci7v_VCLViX3YyxZlqucyc6ZSv7xaRDFsWYngHVh0IdJAq6PIAujjaLbtYMTpsvwmaogrJzUihn9hzdpCOLufLMYbG8IdSTWDIqjrj6tP_DbRjt19HNFGAIAd2dtq3lyp5U-oDoYIXGoUnFRJZ6eH5CzGdnzoywfJtffgpXUM3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بنیامین نتانیاهو: «در ۱۱ سپتامبر، آمریکا هدف شر مطلق قرار گرفت.
🔴
در ۷ اکتبر، اسرائیل بار دیگر هدف همین شر قرار گرفت.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/alonews/146855" target="_blank">📅 13:49 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146854">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
علم الهدی: اون ۴نفری که کنار خیابون ماشین بهشون زد شهید هستن(چون سمت ما هستن)
خدا:
😐
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/146854" target="_blank">📅 13:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146853">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
نتانیاهو: مقادیر زیادی تسلیحات را که ایران برای حزب‌الله فرستاده بود از تپه علی الطاهر استخراج کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/146853" target="_blank">📅 13:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146852">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73948ccb6f.mp4?token=pKeACXbHUDGvHJFpVK0Mb5b3SRR0vYZp6VwIcNjKv8AqMeOKrjdtoA015VJm9ZtBlUyZ3V1eZuV-q3sei88Qcm2IeU0r45VUG5nfoW_Y25yvvW2Qvru4fSXesXFyLSwyKER-i3OyIr2yre1yNSAfDVN7kfNc3e4hVJzxtchXlujYngNqcGmeXKU3GqtE6moXVZagrphxg733twukh2uiZmLGsQQ1nb7DzQ1qcW2WPLGH3nVLRR5vpwIbKDNy4k1kPYxVjJYuUtObybNt9fCu9N2UvlPo3kTJ5xDhytjlYLTvwIp-XWjZLuIKwuZC2NDNyq0g1hFoBlFYnykNTGEyiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73948ccb6f.mp4?token=pKeACXbHUDGvHJFpVK0Mb5b3SRR0vYZp6VwIcNjKv8AqMeOKrjdtoA015VJm9ZtBlUyZ3V1eZuV-q3sei88Qcm2IeU0r45VUG5nfoW_Y25yvvW2Qvru4fSXesXFyLSwyKER-i3OyIr2yre1yNSAfDVN7kfNc3e4hVJzxtchXlujYngNqcGmeXKU3GqtE6moXVZagrphxg733twukh2uiZmLGsQQ1nb7DzQ1qcW2WPLGH3nVLRR5vpwIbKDNy4k1kPYxVjJYuUtObybNt9fCu9N2UvlPo3kTJ5xDhytjlYLTvwIp-XWjZLuIKwuZC2NDNyq0g1hFoBlFYnykNTGEyiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از ارتفاع دود ناشی از آتش‌سوزی در منطقه رأس العاره، واقع در استان لحج، پس از هدف قرار گرفتن آن توسط ارتش یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/146852" target="_blank">📅 13:37 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146851">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
گرجستان اعلام کرد تحریم‌ های جدید آمریکا علیه شرکت‌های هواپیمایی ایران را اجرا می‎کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/alonews/146851" target="_blank">📅 13:29 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146850">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
فایننشال تایمز: به دنبال گزارش درباره تلاش‌ها برای دستیابی به توافقی موقت با ایران پیرامون تنگه هرمز، بهای نفت بیش از ۲ درصد کاهش یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/146850" target="_blank">📅 13:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146849">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
مصاحبه جدید هادی چوپان: هانی رامبد بهم خنجر زد. بهم گفت پشت ایران نباید باشی( منظورش جمهوری اسلامی و حکومته) ولی من قبول نکردم و اونم همکاریشو کامل باهام قطع کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/146849" target="_blank">📅 13:21 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146848">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffb4e73a23.mp4?token=YHPStgfK-cC3iKAoc0BEEhPMvk7hL_J1W1IlVQjTVHHJkgpyVIFu9Wh4uGhHffGoPssEYu6leLJ_Vbma9R3xmzWysbnCOA9S0SzSCXiBnnHJUpLhoOw95kdk77koGA3xzwTT-9fBITZD1FPGKjhhvoO9OAYYLnghn9Op4yI1XQxRFF44LloRR8ZjZ73PUndI8Jz9pcgKu_GVWnkouZULf2OYWAoNiob19OWyFFqP35Yn4sW4yIKk44oa7sWqWe0tTQ9KULWbVr_lImXggWnmOMeRx9_EqUDV61HBkFjew-BV9yXWYf_0mA0eTJMNYoVBNT-Oloqmo-yWtFPgjX8FCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffb4e73a23.mp4?token=YHPStgfK-cC3iKAoc0BEEhPMvk7hL_J1W1IlVQjTVHHJkgpyVIFu9Wh4uGhHffGoPssEYu6leLJ_Vbma9R3xmzWysbnCOA9S0SzSCXiBnnHJUpLhoOw95kdk77koGA3xzwTT-9fBITZD1FPGKjhhvoO9OAYYLnghn9Op4yI1XQxRFF44LloRR8ZjZ73PUndI8Jz9pcgKu_GVWnkouZULf2OYWAoNiob19OWyFFqP35Yn4sW4yIKk44oa7sWqWe0tTQ9KULWbVr_lImXggWnmOMeRx9_EqUDV61HBkFjew-BV9yXWYf_0mA0eTJMNYoVBNT-Oloqmo-yWtFPgjX8FCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مصاحبه جدید هادی چوپان:
هانی رامبد بهم خنجر زد. بهم گفت پشت ایران نباید باشی( منظورش جمهوری اسلامی و حکومته) ولی من قبول نکردم و اونم همکاریشو کامل باهام قطع کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/146848" target="_blank">📅 13:17 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146847">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
رویترز به نقل از یک مقام پاکستانی: اسلام‌آباد تلاش می‌کند از کشیده‌شدن به درگیری میان عربستان و انصارالله اجتناب کند؛ زیرا همزمان می‌خواهد روابط خود با ایران را نیز حفظ کند
🔴
هرگونه مشارکت پاکستان به دفاع از خاک عربستان محدود خواهد بود و شامل اعزام نیرو به یمن یا پیوستن به حملات تلافی‌جویانه نخواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/146847" target="_blank">📅 13:12 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146846">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YP7QWEvlIdyf19ddYjrh2KVCK_nmrUVH3QevyzUcPqxomZf-MM2ij-2OM61VJA1MGUvuKcT6vcniol533wbCV8cGdKkBhgTMiQFdEyuvr3DxTaEPRPvJwc6Pk03H2EU48u0Iy-Bd4wGTMOtob2QqTuSZZJCKv1c4W417GZPR7zzhVhBhbJUNjzfG1sp6Ptu7QI49FAYXn8JcwVR_OeLL-EyLf0li0TIjkxUJnBACYBWC0V6UtedYwUmed-FHBz8Eedv9F9foBjVTp6gf4kVId_27W6RE9rw4dMu41efpzj2utWRh8AOu9DiP074lUA776rd4_PWwesC42jdTwQd3ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
باز هم شعار علیه حسن روحانی
🔴
نهپاد: نفوذی هدایت پذیر از راه دور
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/146846" target="_blank">📅 13:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146845">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
رویترز به نقل از آژانس بین‌المللی انرژی:
ذخایر نفت جهان در ماه اوت ۹۵ میلیون بشکه دیگر کاهش یافته است.
🔴
بازار نفت بیش از هر زمان دیگری به پیشرفت در مسیر حل‌وفصل درگیری‌ها در خاورمیانه و همچنین جنگ روسیه و اوکراین نیاز دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/146845" target="_blank">📅 13:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146844">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا: دوشنبه یک بانک بسیار بزرگ را به دلیل معامله با ایران تحریم خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/146844" target="_blank">📅 12:59 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146843">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hpnNcYPlzIog9BfRXd8gjlqB3sqqqcKdlFYfwZvPwVLLlDuuINGE6_o6AGdJoeYvLmk_-nygklVVTGUnH0PCGNZbaowYJE-CKcr7j6Z7tx-DdMPs71XBmSeOay0THlqBP5xWpJLo2u2hVGpDmoLOhidS90M1zuDbmjw7a4VEXer1KbSiru8aMI_5kQRnGUeNelT-3VqWfrc9ceWqWT9UEUawu_dbXeWmSRBHFUax2YgCMowDnj9E1Uaj69z8zSxmLz1fBrnoKrdo4CCrpYXtvmyMniKFCZdC-FX9W3t4_76MZnZUPx_eT3LAf7-d296wAupQYp07s5X0KQOZd6gXqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صادق محصولی رئیس جبهه پایداری درباره مفقود شدن ۱۶۰میلیارد دلار پول در زمان وزارتش:
🔴
اون سهم امام زمانه که دست من امانته
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/146843" target="_blank">📅 12:55 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146842">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
دلار بزودی 300هزار میشه
⁉️
🔴
تحلیل ترسناک نوستراداموس ایرانی
👇
https://t.me/+WZbLEaPPJQUwZDU0
https://t.me/+WZbLEaPPJQUwZDU0</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/146842" target="_blank">📅 12:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146841">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd237427b5.mp4?token=ZLBFUnuHEXXfhUuBDcaFsFPQYUu-X5sPH6BQ99GA7cULyKpnss66UGRyDsHN8XoD5Nz5J2o2y45IblqLnFD69UbHVHPv4Eknnpi7n7Ht2PUHkh212XsntOu9-lQXAAytYOBDoCczb30II7NKGR2eu_OK7bTKFcP0jZ4S_5sr0etzvMSjC8ADgoUh9RZvSln2VBJTQRncHnWOlFqcL-pZt5DhEffk9IssCBvW6KkhoOIF_Y-UeDvrxsF_bBPuGBXMr1Snt95KFWYQ9LbayjeqKnBmjPD6GB6wu2yOODSHB5m4do8TlEt7D_FAXXKnkQzv6aqGdDTMzUsOaicLiZwODDnbHVv7tWSK6aw8GdwmUqUQq7ctISKdctmce_1de-ycJe3f00TkDcKN1v_O4ueDAGI5U4nCgs_tDHxG_cRWUFmWYhGtY4O8n8h5FIrzImwZzjYxp9UO3iB8wlgGYJeBtiRovXfhrQkRXz8EAOLwRnPs3Bae_ODSfnp7OGw2f3e7Q0Ow3L0dkZiawEoeuCtuWPzHbFsEJ7MBCIlPCY4-QeiKb8a49I-TkCvv31-lBQTWVikKA7aDRo-uLHL4Fcdp7bsT9780LvsfDT8OfLy5omDDGdM2RMTSchw3MQcPhu3Irx41Kxx0sJlHAF8c5lb8OF9Ldq8ZmCm8duSebPClM-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd237427b5.mp4?token=ZLBFUnuHEXXfhUuBDcaFsFPQYUu-X5sPH6BQ99GA7cULyKpnss66UGRyDsHN8XoD5Nz5J2o2y45IblqLnFD69UbHVHPv4Eknnpi7n7Ht2PUHkh212XsntOu9-lQXAAytYOBDoCczb30II7NKGR2eu_OK7bTKFcP0jZ4S_5sr0etzvMSjC8ADgoUh9RZvSln2VBJTQRncHnWOlFqcL-pZt5DhEffk9IssCBvW6KkhoOIF_Y-UeDvrxsF_bBPuGBXMr1Snt95KFWYQ9LbayjeqKnBmjPD6GB6wu2yOODSHB5m4do8TlEt7D_FAXXKnkQzv6aqGdDTMzUsOaicLiZwODDnbHVv7tWSK6aw8GdwmUqUQq7ctISKdctmce_1de-ycJe3f00TkDcKN1v_O4ueDAGI5U4nCgs_tDHxG_cRWUFmWYhGtY4O8n8h5FIrzImwZzjYxp9UO3iB8wlgGYJeBtiRovXfhrQkRXz8EAOLwRnPs3Bae_ODSfnp7OGw2f3e7Q0Ow3L0dkZiawEoeuCtuWPzHbFsEJ7MBCIlPCY4-QeiKb8a49I-TkCvv31-lBQTWVikKA7aDRo-uLHL4Fcdp7bsT9780LvsfDT8OfLy5omDDGdM2RMTSchw3MQcPhu3Irx41Kxx0sJlHAF8c5lb8OF9Ldq8ZmCm8duSebPClM-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شعار مرگ بر «هیلاری کلینتون» و «مرگ بر حسن روحانی» در تجمعات شبانه
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/146841" target="_blank">📅 12:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146840">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
فوری / نیروی هوایی عربستان سعودی دو حمله هوایی به بندر المخا انجام داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/alonews/146840" target="_blank">📅 12:38 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146839">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3890ff4c6d.mp4?token=Y8xu3TKjewP_dit1qXhkPWe0yC34DrQ1lFYL4OAvYp-JUxk6QgIr-JUf7rOpw2t53iz3gs3luQvrEvY6jJq1cBDewGY6NFOveaqd7ZhPh7XwMBMLwFbhpQW2HZYVB4LLwX7IHjai8Qeo7rYbm9Vej25BdFcQZsunC31tlLCA2dYq8se9rG_ii1uAw9UgyVk12RdLnFvJ2ilnY3xQWeClA34OpIDuF35LmOkX4ZCu1q94UPmFGugOJqA4q_roDN7RF7PUA90FOhuwZkP7JcrKCAqdHuxd3P3du7KDyuVRROm_x5sJUDf5odrx1ZEajqab5CSpOfwTNiLA5zXDd1NBeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3890ff4c6d.mp4?token=Y8xu3TKjewP_dit1qXhkPWe0yC34DrQ1lFYL4OAvYp-JUxk6QgIr-JUf7rOpw2t53iz3gs3luQvrEvY6jJq1cBDewGY6NFOveaqd7ZhPh7XwMBMLwFbhpQW2HZYVB4LLwX7IHjai8Qeo7rYbm9Vej25BdFcQZsunC31tlLCA2dYq8se9rG_ii1uAw9UgyVk12RdLnFvJ2ilnY3xQWeClA34OpIDuF35LmOkX4ZCu1q94UPmFGugOJqA4q_roDN7RF7PUA90FOhuwZkP7JcrKCAqdHuxd3P3du7KDyuVRROm_x5sJUDf5odrx1ZEajqab5CSpOfwTNiLA5zXDd1NBeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پست خواهر امیرمحمد شاه‌کرمی از جانباختگان دی ماه
🔴
۱۸شهریور، برگشتم به همان خیابانی که اخرین نگاه های برادرم آنجا بود ؛ تا صدایش را از همانجا دوباره بلند کنم.
اینبار ایستادم برای صدا زدن نام امیرمحمد شاه کرم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/146839" target="_blank">📅 12:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146838">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
یک منبع پاکستانی با اشاره به گفتگوی عراقچی و عاصم منیر گفت: این مذاکرات بر جنگ میان واشنگتن و تهران، امکان بازگشت به مذاکرات، و همچنین حملات انصارالله و عربستان سعودی متمرکز بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/146838" target="_blank">📅 12:35 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146837">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
روسیه،‌ لیتوانی را به حمله اتمی تهدید کرد
🔴
سخنگوی ریاست جمهوری فدراسیون روسیه: استقرار سلاح‌های هسته‌ای در لیتوانی قطعا علیه طرف‌های خارجی خواهد بود. بدیهی است که این سلاح‌ها علیه غرب نیستند، بلکه به سمت شرق، یعنی روسیه نشانه می‌روند.
🔴
اگر سلاح‌های هسته‌ای در خاک لیتوانی وجود داشته باشند که ما را هدف قرار دهند، آنگاه خاک این کشور نیز در تیررس سلاح‌های هسته‌ای ما خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/146837" target="_blank">📅 12:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146836">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L1qku51G39Ko6WVyrTdd41dd9T9HuVjrKBYmZ46Otb5Cp3Htv74vJm6-Rk4wxD50ZZM4PR0PIXaHFKryjSR1ocdQWka_J6R8AeiV2m86nAO-jXbjuaZ0YfeagvjB9a3Owc2wD0DFt_BG8IghqwdoX6U3KEyBeXVD8IFc_hllK_KnFK6HriUTJtPdDNypgSfrlfvhQYE0YZkhnp5dUMvjgaFdDANinNnJlXIN4CLdOj78yAp64MkFKe82a4KgIi2mG0C8wIFQtfTdTFRioH9DNkgRaiIcP2DZUZ19harNXPHVnVqLsfNFrlxe_cCzLXNVYRGdmRuIurWj2lBTZATtxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نفت برنت 5 دلار کاهش یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/146836" target="_blank">📅 12:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146835">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SklBNOFpGpcZJWA-gpQ8fmOymvW4tkJkYijdLyNqk7Vwctw70ss-Gf0wOEN71qPi2_7suG9eBdwRChByQOAuB4cPfv9wA39Pl_JuMI2Dbtw2g1vLRluIfqxlGbo2mOYFUsRE8bxOECppWuS9u98W2THf82iPnIOY6__5ORhS9ZgWTQe-Zm6ppSRYJnuT4s-0b8H2T2kIZkPPIELR_zj15xHcYRxaOw8E2Cnpn_6zVVAYmzw-6pWbmH-imcCnERVjqsCd9s8uM2pMyL2idIXIPCoyQ48demlBPUKku4Mf79pGTyRClhbnimFixLHFmiksXv2FTMIbOJ1ZXFdDojXbZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ادعای دو منبع دولتی یمن به رویترز: نیرو های دولتی یمن از جزیره بریم در تنگه باب المندب عقب‌نشینی کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/146835" target="_blank">📅 12:21 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146834">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
پزشکیان دقایقی پیش وارد دهلی نو شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/146834" target="_blank">📅 12:17 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146833">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/htV5WqM2uWgzRahXKDrqdH5gAAnF7nGQotSx3K8GfX9mV0LRkTPOOxP2CJkXq-_CbIN_t5jt3PRtKvVeC6Y5aUGAV5KOvCSQU2pULv2HPAUJ0gfZ2V7MXAOg8nyF6A2RRSLCQkX8fKnVuyPXhoZnCsoW4F-fcWEEs93Pmo32cyhFl0rFgljxBywoxtKyQGp51K0MgE30dt2a2QG8CAEJgKmk2We9-sjuSzR11ouNp6QBgqx7vz8t5ye-OfBqUwhuh2eKPo_PRYLyBiwqtpN3xITW7Rp1JqQgSeMSc6KGgoACp0o6j5NPPByJjcOROmDZlYwkCsk9g24JGJna9l2bcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
25 سال پیش در چنین روزی گروهک القاعده توی 11 سپتامبر به رهبری بن لادن، برج های دوقلو آمریکا رو نابود کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/146833" target="_blank">📅 12:07 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146832">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
پزشکیان: موافق ادامه جنگ نیستم؛ اما باید تاب‌آوری کشور را افزایش دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/146832" target="_blank">📅 12:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146831">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
وزیر خارجه مصر: باید به یادداشت تفاهم اسلام آباد به عنوان روند مهم برای رسیدن به توافق فراگیر بازگشت
🔴
ما به تماس‌های خود با طرف‌های مختلف برای پیشبرد آتش‌بس ادامه می‌دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/146831" target="_blank">📅 12:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146830">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
خبرگزاری رویترز به نقل از یک منبع پاکستانی گزارش داد: وزیر امور خارجه ایران و فرمانده ارتش پاکستان در مورد راه‌های احیای تلاش‌ها برای کاهش تنش‌ها گفتگو کردند.
🔴
در مذاکرات بین عراقچی و فرمانده ارتش پاکستان، احتمال بازگشت به مذاکرات و حملات حوثی‌ها به عربستان سعودی مورد بحث قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/146830" target="_blank">📅 11:48 · 20 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
