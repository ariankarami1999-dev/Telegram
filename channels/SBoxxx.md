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
<img src="https://cdn4.telesco.pe/file/oM3OYesLYChUAW9yhB0NnUYbO_xUb7shassAGw-aDk6HFYg3suvijLAInyUKIh_zU6ndy7n1xO3FfBJYI4666xNsXzJ1yB_sMmdw9-p_NMzhmo_GrUSoy380j5PfEjibUAq8Gvws6yp9mNlTwLviKy1mA1KUrZF6pRR94kHdGuvuD_AIfCY1tJKhrcDIxwOmfZ4oFASLESVDKVxZVYkiDJjT_FtyASmrTflzhIdzr9U_SaXFmGo37qFv2LxBxodjw6w0IJb7yXSauqh8zCIXOCg4Wx_d4UHDLTkLxyO9ExJP2jx-fj7SIg4IMyRlT78jDVO7QIdFH1y_mhEcbcEr9g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.6K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-05 20:40:41</div>
<hr>

<div class="tg-post" id="msg-20261">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">خبر بسیار مهم اینکه این اسوه تقوا و هنر نیز به کشور بازگشت و به همین دلیل قیمت تریاک در ۱ ساعت حدود ۴۰ درصد رشد کرد.</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/SBoxxx/20261" target="_blank">📅 20:06 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20260">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g-bomYi-mNuENcMu030xr98mOCF2FbwnEJ6RNp4fLWnsq8oWDSqQtZtY61E3wR6bthPM-wDiUVY0bWSKVjK5o3c0rc8KrCRl08FqTKnW7clR94fDKxtJlWZjUZyGvUUn1xtd-VxO2tWhVEJaxqYwkKSp-qYDLN2ezyDTNvUANLy683Cb0vhFirNYMI4qiwsDSQU5IfYFZ8xEh1Rzieq6jjKl-NhKPJNm7Y044jR7z5rBCXImsJPJ4Ds_UgJyHUh7B8jVIgGFSUO2u22zkUjsVLceh0M65vkeVMc3TisKSmklil-6_crmgko7Qq6WXfQ-gVQ4nwyZi_Z5WQOb2_qQxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبر بسیار مهم اینکه این اسوه تقوا و هنر نیز به کشور بازگشت و به همین دلیل قیمت تریاک در ۱ ساعت حدود ۴۰ درصد رشد کرد.</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/SBoxxx/20260" target="_blank">📅 19:53 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20259">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">باید بگویم خیلی خوشحالم که عمانی هم نیستم!  از یک طرف ترامپ می گوید آنها را بمباران خواهدکرد از یک طرف دیگر ایران می گوید که باید مسیر جنوبی را ببندد که البته خودش هم می گوید بدون نیاز به مجوز عمانی ها هم این کار را خودش کرده!</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/SBoxxx/20259" target="_blank">📅 19:46 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20258">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ایران می‌گوید با وجود محاصره آمریکا، همچنان به فروش نفت خود ادامه می‌دهد.</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/SBoxxx/20258" target="_blank">📅 19:39 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20257">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ایران می‌گوید با وجود محاصره آمریکا، همچنان به فروش نفت خود ادامه می‌دهد.</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/SBoxxx/20257" target="_blank">📅 19:38 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20256">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">یک دور از 4570 حدود ۳۰۰ پیپ داد  دور‌ بعدی احتمالا محدوده ها را ببیند</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/SBoxxx/20256" target="_blank">📅 18:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20255">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">محدوده های خوب خرید طلا برای امروز  شاید به این محدوده ها نرسد لذا توصیه می شود به صورت پله ای زیر 4580 خرید بشود و در خود سطوح افزایش حجم داشته باشیم.</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/SBoxxx/20255" target="_blank">📅 17:11 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20254">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">حملات گسترده ارتش اسراییل به جنوب لبنان</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/SBoxxx/20254" target="_blank">📅 16:46 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20253">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">سخنگوی کاخ سفید:
در حال حاضر هیچ مذاکره‌ای با ایران در جریان نیست</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/SBoxxx/20253" target="_blank">📅 16:21 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20252">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">دقیقاً 20 روز از این داستان نمی گذرد و بحث حمله نظامی روسیه به انگلیس دارد قوت می گیرد!</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/SBoxxx/20252" target="_blank">📅 16:05 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20251">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">انگار یک دستمال سفید را دور اسکاچ سیمی بپیچید!</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/SBoxxx/20251" target="_blank">📅 13:45 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20250">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">خالد شیخ محمد، که به دست داشتن در حملات یازده سپتامبر متهم است، قرار است در تاریخ ۵ ژوئن ۲۰۲۸ در پایگاه گوانتانامو به همراه سه نفر دیگر که همدست او تلقی می‌شوند، محاکمه شود.  این تروریست که در سال ۲۰۰۳ در پاکستان دستگیر شد، از سال ۲۰۰۶ در گوانتانامو نگهداری…</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/SBoxxx/20250" target="_blank">📅 13:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20249">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxmDSAXGB5KdVBuNIrkwDjO5lJJzMpE73lkp_xzBEwzpRr-71DCUYK5syLIw_sb8DGYYdnRD14NVQ8Sy-Tb9H2-xywM2waTSKxckPV5MWI3bfIEV5EYLYEZeouLAeeBmJZxWSGpreURt3wVKiyqp6RjuVPkN1JmD906MSKhFkKH3gPCRe7Jz2zExvqq44HR5BSDu4WkI8zopwvx3pPHjoss-PALMYFrCUVtPpK3Q1qSrm-tU1rL1ueQcSzpKQkyv5mpzmclor_11J7AuobqJnCGcbMnP9UkO5MQ1YzmwGixBpUGlra8xxIV12BsgwxpZaoj4tCECN-LUjGMLM_trJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خالد شیخ محمد، که به دست داشتن در حملات یازده سپتامبر متهم است، قرار است در تاریخ ۵ ژوئن ۲۰۲۸ در پایگاه گوانتانامو به همراه سه نفر دیگر که همدست او تلقی می‌شوند، محاکمه شود.
این تروریست که در سال ۲۰۰۳ در پاکستان دستگیر شد، از سال ۲۰۰۶ در گوانتانامو نگهداری می‌شود.</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/SBoxxx/20249" target="_blank">📅 13:43 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20248">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kcna2gyXYyYfZa62N1vbyGe4xOvT4tTuM9vqKG-PCh2FP3cBD1ee1gvDPUX-Ba9UDCA9r8kFgtS4lHnbUDHYb6f8BfNsgLIqr72uqjO5Sc5sXbbXFfxzpFhTGSRPe4B6Q-Svdy8P40yJ3BjXGSmJQm0MiDOWatn1ho0TAgn3LkWNkEtSy5WIqCUgrxVnM-wB2mgm5f2JJoQrA6OHR48KFZ5kpwDzvltzxKbDeVrzB_c8dWCw9l9RXuKcZUIq-ciZrqk--nPpH1VpDnylff4KaTpYP1Mwb4yQwpg7i0-5jHbOglGtGwrU_aIiDpEMd7l2nSf8cvbD37C4fw9f--HhIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  برای امروز شاخص ریسک ژئوپولیتیک در سطح نسبتاً پایینی قرار داد و پیش بینی می شود طلا یک کف سازی انجام داده و رشد خوبی پس از آن داشته باشد.  خرید در حمایت ها شدیداً توصیه می شود.</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/SBoxxx/20248" target="_blank">📅 13:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20247">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQc3LfsdDVrPMvpUtHGxQrAv1iY7KWfSUu_0NtOrPV1RF-YSZhj4Uo-Rxu4POkaJksFcD_Lqw3Y0pM3u9FBqS7DHWh3FBzidCXArm2HIHVkNJsvHVVnnokG6e76b46uC9UiMMv09miu3nZz3HIvyTGiy1iPSY2A-kOh4nIPOIh8VrZuqJaUF8wMPu9C0rHk9bq8K5ehBKPC_1WOeWLO78Qz_o9j6do4G4ViqobnwUjR4QjjokU8So-lOQgwFdaJU32433dybgdZrR2BdZiUY5ZCEmCpWpFbb-pD06_xarbEqfb2fWiazmHl4ADmZhSA1c2q1Bmy8SM9AacPl1LnHWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
برای امروز شاخص ریسک ژئوپولیتیک در سطح نسبتاً پایینی قرار داد و پیش بینی می شود طلا یک کف سازی انجام داده و رشد خوبی پس از آن داشته باشد.
خرید در حمایت ها شدیداً توصیه می شود.</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SBoxxx/20247" target="_blank">📅 11:07 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20245">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nwxgUMN1s_dHm0L86mFqIE94G7VZnkCdIrIU0aJvI87_etXT9uRY6gfmr3f0gJBVPKbXarJ9OShGwzrddrgq97S-JfZNR9M36htmj71kEPWv23rZ4bvCTKOgBcxBgXthvMVrbHaZ3_kMJr4Vse6a74tFllc_8q0ULmyKq8N0dMTN2HTCzvBeeyiASf-GtefXa7O4Ues-N0wrGHiZ2DB-XP9bKmlUn-ucyOhO59lDT-M0YWdqAy7CsyT9fx0-0cKuZwepJK2lStBeIgV9rw5lx4EBkRLSbZduxWz8HS7NE9TLKoWMAub82jI2ne-xWxGFtrotKdXTm5kjpo2hj5YDWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aVb60OZpx5SWMZZqSSYMIiDBUEVbkAFBahiTV0dDU8KcvwePCQftTLheLDB1IK9YiJgVouPVCcZOuOMG71z6Iag9PtCldxAF7F3wC9J-KeYHcHxsm_jCnhft-QqU-Sm6iRfcqTFMgmVJnKwEIfen4h0HqgIvZfkZSKiUx9TgCLqd87_A2NWpW8881gfrMN5ZUYByOcA5v-jjv0cKUqh4huBs3nDxP4YEygEC1us7mfESWGSSfvbhUKuU_KfLYw44G2tDIWkrgfGJ89_HuI3pXvjXmIcK7AID0W6NR520xRUACWz-2JZxjqlgOcfDJk4nwIxxuDCe399I8dlk2lgzBw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز هم در سطح بالایی است و فشار فروش روی دارایی های ریسکی و احتمالاً طلا پیش بینی می شود.</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/SBoxxx/20245" target="_blank">📅 11:05 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20244">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f65ff1052.mp4?token=A9Lq0TSFztcQHnGBSvv-2L-7A7lKM50Wr9_AGlfceuboJSC9ioeikpuFuNRrkKp5Hwh0pJuo_bR9_JSXLz8YD3ylGHoHRJ-1FFtwnGKOM458r8SrWRlaozh3NZkbqcwWhjPsRo_xDT0bcBMzaFS_qvhdHccgCIjD1S4UclwK0EOlXq6t3wfsthhpu2LmTVALx-WlhoJlG8aUSK836pP6tbQJMcQkXlJt9DVSkuHBmR1Uiez_05xPvLnJWskYxouwXc7GVmKZXG2VU7Pul3dZADVX_a6ibZot_7hLowHs-FMxNur8MBhoJ9_7V4LpD9oi7vhthxaJXz1Yfl1aXz44LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f65ff1052.mp4?token=A9Lq0TSFztcQHnGBSvv-2L-7A7lKM50Wr9_AGlfceuboJSC9ioeikpuFuNRrkKp5Hwh0pJuo_bR9_JSXLz8YD3ylGHoHRJ-1FFtwnGKOM458r8SrWRlaozh3NZkbqcwWhjPsRo_xDT0bcBMzaFS_qvhdHccgCIjD1S4UclwK0EOlXq6t3wfsthhpu2LmTVALx-WlhoJlG8aUSK836pP6tbQJMcQkXlJt9DVSkuHBmR1Uiez_05xPvLnJWskYxouwXc7GVmKZXG2VU7Pul3dZADVX_a6ibZot_7hLowHs-FMxNur8MBhoJ9_7V4LpD9oi7vhthxaJXz1Yfl1aXz44LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیخود نیست صنعا را پاریس خواهرمیانه می نامند!
ناموسا این ویدیو را ببینید! پلیس های ریقوی یمنی دارند مردمی را که هر کدامشان یک کلاشنیکوف بر دوش دارند «بازرسی» می‌کنند!
به خود تفنگ شان هم‌ کاری ندارند و اصلا مشخص نیست هدف بازرسی چیست؟!
شاید فقط دنبال بمب می‌گردند چون میدانند اگر فرد مسلحی بخواهد با این جماعت درگیر بشود که ظرف ۱۰ ثانیه به گوشت چرخ کرده تبدیل خواهدشد</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/20244" target="_blank">📅 00:36 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20243">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">به نظر می‌رسد داریم به لحظات ملکوتی وطی دبر حافظه تاریخی با علی آقا کریمی نزدیک می شویم!</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/20243" target="_blank">📅 22:38 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20242">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">به نظر می‌رسد داریم به لحظات ملکوتی وطی دبر حافظه تاریخی با علی آقا کریمی نزدیک می شویم!</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/20242" target="_blank">📅 22:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20241">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">قالیباف:   رابطهٔ راهبردی ایران و چین به اجازه هیچکس نیازی ندارد</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/20241" target="_blank">📅 22:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20240">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MgVp8oS6lo6s_Na4kwE6Ec9Vc1FET4u8DMRnHv2DORFEGQZwNSkCh7W5nEQII5W5wGsO06nHTsoTxbNaCgOKZ16EhOEgRpQdiLh0ba5f0WF6mwbNb6BulFbZZPwi23NGemUr_nvxkFmhyLcZxG9nqGbDsQvdUHi8cdaAAoz1BYXLzVInCFd3il9yfp3V77B57CQsV_24o4KTdDxdEY-UV1jy7ozfTZ9HVuNdIvjKhnNoOwZ8eWs5EmdsCoCHtDMpqAh5DSV1JUHzWM_isHJnzY8jnf7Jz38qsky-yPN4TCDMxal-lr2nuwc78OV2yrQvisBXFMvtfTxuKNpklBKHqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در گفتگو با الجزیره گفته که برای گفتگو با ایران شتابی ندارد!</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/20240" target="_blank">📅 21:55 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20239">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">در دنیای فاینانس میگویند همه تخم مرغ هایتان را در یک سبد نگذارید!  به عبارت منابع درآمدی و دارایی تان را گونه گون سازی کنید (Diversification ) تا اگر یک منبع تهدید شد، منابع دیگری باشد که جایگزین بشوند.  حالا حکایت ما را ببینید که در سال‌های اخیر چطور به چین…</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/20239" target="_blank">📅 21:53 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20238">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">لحظه ای که روسیه ضد اوکراین سلاح هسته ای استفاده کند، آمریکا هم ایران را با هسته ای خواهدزد.  شاید هم اول آمریکا بزند.</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/20238" target="_blank">📅 21:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20237">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">یک نفتکش هندی هنگام عبور از تنگه هرمز توقیف شد.</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/20237" target="_blank">📅 21:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20236">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uhpF0hM4474GeK4nhrV2v0c9n8joCOm682VsBQxetAWbAoetKxOUfJi_1TfJRttoM2OQjZgiR9_wY4XKGjDi-2QpJAphyoBfUXUlHBnnx6b5ZXn62S6SDY2Yedr1ooDXDy7hgETnGV6HeZHlqk_i1DUgCYCqHy1ovEi6TnnEPrMJXj-aZ6x5B4p7elkHsNelEhqP14qEPmr0Go_Zg09bb-rPa9hKtlC1JVjNKYj9Sa2OoqgcWx55hntkeKUZiR2gkiwd9o1Rvw_8EFHYElpPmVMtxuSmvixSKD9NJKDTAqVfAwCzHV2ftAQfbvvs96GK2131U1OdqE4LAExGop4bRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خواننده Secret Box از 18 ماه پیش می داند که چین
«تا جایی که می تواند از اقتصاد و حاکمیت ایران حمایت خواهدکرد»
و البته از
خطر و ریسک این All-in کردن به اتکای چینی ها
هم آگاه است و متوجه است که به محض اینکه آمریکا یک امتیاز اساسی به چین بدهد، ر
وسیه و ایران هر دو
در موقعیت بشدت ضعیفی قرار خواهندگرفت.
اقدامات احتمالی ایران و پیآمدهای آنها را هم دقیقاً
1 سال پیش در یک نشست لایو اینستاگرامی
مطرح کرده بودیم که اغلبشان تا کنون محقق شده اند.</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/20236" target="_blank">📅 19:42 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20235">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">خلاصه مقاله آسوشیتدپرس که دقیقاً تاییدی بر دیدگاه ارائه شده است:   ضعف اصلی استراتژی جدید تحریم‌های آمریکا علیه ایران، نه خود ایران، بلکه چین است.  واشنگتن می‌تواند شرکت‌های ایرانی، شبکه‌های کشتیرانی، واسطه‌های مالی، شرکت‌های هنگ‌کنگی و حتی برخی شرکت‌های چینی…</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/20235" target="_blank">📅 19:25 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20234">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mk76vDlAtwmDC7iJjWnMJdqf8xE-80FGTckOoKoEm5pjSBCfLlwhPf6QUTQXvI-f2cCqULXXZs_fcucK59M0Cyx5cEvYLsSncPAbC-vmgEeth4jT3F14w08ky7OBepMnRAUV_S2-ahPM368lIpSKG0HJvYbfWcssSBH5fY1ZiBF-_qVZNsqG8Dou93okF9pgaEM4HeAvjXxlrjdKiEq8AVckqsoIvQF3331BD2_CB-xRffjUVsoPAq0WNhw6kvZDmMiSCZFP_dbN0OTr5cQzQ-8CrMi90uvRAx--gO4TUdQ6dpUVqXNG8kSyzvCin8sXvmVjkNowh990Jc6rGbr7aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بسته جدید بسنت سروصدایش بیشتر از تاثیرش خواهدبود.  چین اگر بخواهد — که به نظرم می خواهد — به هر قمیتی از سقوط کامل اقتصاد ایران جلو میگیرد و همه ابزارهایش را هم دارد که اینجا اشاره کردم.  کالاهای موردنیاز ایران را کماکان تا جای امکان صادر می کند و پولی…</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/20234" target="_blank">📅 19:15 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20233">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c39d5bd85c.mp4?token=i04nQ068XKcuccj1slpwHj7ZP2oO5taCYQ9wTHTL5fu2Uuk6RezS57RFP0Hg8hbfg9oR_Vrt5eLUR4h94uJQnOdC_3Xv9JtTYznWU4PYT1fm0dIbyx8s_bvbJyqr2egBSYS0neAZerIPX8_WPjJkmg8E7YP5p2KCHI5pt9u_Wlxe1H3bsqu4aG37_cheW4l_-Ex9VfD6QlKJPsxz6YzlqMnhj9n9lbhPVe2L39rvyt8ZvOfVYsq1qF9s4jFA3edwDmLa2bL6Lmc_Kt9N6PzpJOP5fnvflxxnRvSIpb4cnEAWrUNwEBw07j7WmFTe5bQoA1SXsamTzQworhh_Rp_dzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c39d5bd85c.mp4?token=i04nQ068XKcuccj1slpwHj7ZP2oO5taCYQ9wTHTL5fu2Uuk6RezS57RFP0Hg8hbfg9oR_Vrt5eLUR4h94uJQnOdC_3Xv9JtTYznWU4PYT1fm0dIbyx8s_bvbJyqr2egBSYS0neAZerIPX8_WPjJkmg8E7YP5p2KCHI5pt9u_Wlxe1H3bsqu4aG37_cheW4l_-Ex9VfD6QlKJPsxz6YzlqMnhj9n9lbhPVe2L39rvyt8ZvOfVYsq1qF9s4jFA3edwDmLa2bL6Lmc_Kt9N6PzpJOP5fnvflxxnRvSIpb4cnEAWrUNwEBw07j7WmFTe5bQoA1SXsamTzQworhh_Rp_dzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ضرغامی:   مذاکرات مثل خوردن گوشت الاغ مرده در بیابان است!</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SBoxxx/20233" target="_blank">📅 18:54 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20232">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">نگاهی به فیلم «رشته ها»!   امروز، ۶ اوت، سالروز بمباران اتمی هیروشیماست؛ روزی که در سال ۱۹۴۵ برای نخستین‌بار در تاریخ، یک سلاح هسته‌ای علیه یک شهر به کار گرفته شد و جهان وارد عصر جدیدی شد که در آن یک بحران نظامی می‌تواند، در صورت خروج از کنترل، به تهدیدی برای…</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/20232" target="_blank">📅 18:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20231">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ترامپ: می‌خواهم ضربه اقتصادی نهایی را به ایران وارد کنم
ترامپ لحظاتی پیش مدعی شد: آمریکا جهان را تحت فشار قرار می‌دهد تا ضربه اقتصادی نهایی را به ایران ورشکسته وارد کند. آمریکا در حال فشار آوردن به تمام کشورهایی است که هنوز با ایران تجارت می‌کنند تا روابط خود را به طور کامل قطع کنند.</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/20231" target="_blank">📅 15:26 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20230">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-poll">
<h4>📊 اسرائیل تحت هدایت کدام دکترین و چند بار به تاسیسات هسته ای کشورهای منطقه حمله کرده است؟</h4>
<ul>
<li>✓ دکترین مونرو — 2 بار</li>
<li>✓ دکترین بگین — 3 بار</li>
<li>✓ دکترین بن گوریون — 4 بار</li>
<li>✓ دکترین شمعون — 2 بار</li>
</ul>
</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/20230" target="_blank">📅 15:12 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20229">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ناصر نوسان کف دلار را در 195000 بست.</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/20229" target="_blank">📅 13:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20228">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">تحلیل عوامل سیاسی چرایی شتاب شدید رالی اخیر دلار</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/20228" target="_blank">📅 12:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20227">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">دلار فردایی تهران
⏳
192,300 تومان!  کاملاً مشخص است به صورت دستوری دلار را دارند بالا می برند تا جناح تندرو را به تسلیم وادارند یا دستکم گرانی ها را به گردن آنها بیاندازند.</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/20227" target="_blank">📅 12:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20226">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hkeuSP7JgS1rOoRVna4gPSQJz34Wr4OykCnzgIi1n8EG9yNL4fQkT8DZTdklxmn9JrFYDh08-Glhy-ROFJlLkrHNDGUaJJqoZYjMTspfjfwlwYAjdWA22URXrPHGxClFWXdXi8yHov2qbxFhU-NUnFpcVxN-_pm-eYtNZ9zXCLTwLcV-hKtxjWxfDhIFLEmXKB1xuIqmuaXcTlBNWSm2B3FEcd4r-YbbQTQz3-gg20erYpNwH7uZHN3AXsfpHSa80r2GW5Jd7wpDB7p2TcNbXnszpJ1nYrhIS0f_VPrIqVkDIG95wFS7T6ieSwtU81Ukm2czE8b35GTA39iK-v63Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#پایش
تا زمانی که بتوانم پادکست های GeoMarkets را دوباره از سربگیرم، این جدول هر روز ارائه خواهدشد.</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/20226" target="_blank">📅 12:37 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20225">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qiAI3rZUPxED0zqNJusuzOVmHEQ4rlpLBuAe4VLnTVSKOcEGyG6t1hUiebZjOZDnI8UqGE2KZfL0i3N2KTdWgGUTQlBZnsGmw1dqB7HrLak8QK7L1uRmcGlcCKKdn1s_Q9lKwYcRxoXiTGCcPUfytLlQSD-vvknvwbE4y8kqad6YwA8qfDi-nsXZ2Rryz_Gt57ZN7FeiXtrRYMpmdISrCBfo5Z4XEm4uA9w3IV98cqzXvI1uPNeFrYTRPp7O96iu7kHrCOuXB9dAvAs5SZ5cuZKgx3beYAFmlNh6pzt59EQS1DUMPpzwX-YnYtE1wm8VLmtKHoomLuwijB2Bd_FwtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتصال ریلی ایران و چین   پس از آغاز نخستین محاصره بنادر ایران در ۱۳ آوریل، حمل‌ونقل ریلی کالا از شی‌آن چین به تهران افزایش یافته و تعداد قطارهای باری این مسیر از حدود یک قطار در هفته به یک قطار در هر سه تا چهار روز رسیده است.  این مسیر ریلی پیش از آغاز بحران…</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/20225" target="_blank">📅 12:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20223">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ivgx0XWU1IGZxzrqurnC49Z7mZxEDBMPVsh3CdP4ifuivBvFAMw78PCP3s1_4hfaHSxYZqjYglGoNs5deDx2vzXRZsV7bt-mubnbdldlGK0yeW68utuv2joEDuUA-z-Pqg_5wDUPYNudWtDfKtxuccx4QCAu6Mc2Z2r7zChU7BI79lH-U5ki3ILh7pJ8j0wQIJsUGTYcvHZIY7MVGLxouqsQHQbxIytDSF5MCAsMAxhtYgyjYefKgBzeLXK0LvVddZW4nEOFoDW75I9qLF-t37qoFK0ACo4ngXPGsaUR5Sb7UMeBmHZAjdZXq-5iLqO1s_3cwCouTsp5qNPemmp59Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nh4l56QpvKszsR12rAFCoXmqdQZg0sUyjZubRhXHLA9U1RpWOYvK27q2zjt-34kYKaCUetcw19AsKRDVmWlGOfGYr-NDCNpEWQDBnVUKOY-M0mtSnExvBAZQK0KfOyFFC9eFNDzpsLYOr2w4MeRMC0GSBybqTlWqxoDmhHSh8c12sO6ctZHskJ04mpV1NAZ-AFTsKW66VPUHSZbcNa17a2RUu2RQa4hdDaABss7P6b7_2zhk4HsXTAQ-Inmaaua5iKvVVfq39fUjuHLKxSvdBJHtNb3yyBq_d9SrEskDIdb-aSgQenW683NfUIdTJ_IkNIp_fTwzuqK3Yq774E_FZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز هم بسیار بالاست و پیش بینی می شود شاخص نزدک افت داشته باشد.  طلا هم با این وضعیت قاعدتاً امروز باید به افت خود ادامه بدهد.  دقت کنید که سقف دیشب عملاً جعلی بود و بعد از ثبت آن حدود 800 پیپ افت داشت.</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/20223" target="_blank">📅 11:52 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20222">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sEgT9IqkG9deZ9EWyjCLI7gTSwXHypg4htKCDYOngpZzbVBy7fs9bv6X7YtwdkIf7pSPpHF37Wu19biZvCctmZQ2jEWgx2t1pUoLu_DSpXuzEX31W0qMG5nWRmjZwFf8uN-tr6EdgRZVtkpoGAO2hSMkL4ap-fvfUXQmidKNIxrinpAYvSafver5F3-0Lt2Z4QixVwvocvKT8o-t9CkpMi_SS6OxRozEUHtfxaLwPH4BxdC8lE2HgRrGcmSes1JPrOJO-KMJlLcD7QxQwvygyieId2T1ZBi0KoDfYM3qNyrktX7x3vb7HSo-FQksvraKyytjTczBLVQvCe_YFXXMtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز هم در سطح بالایی است و فشار فروش روی دارایی های ریسکی و احتمالاً طلا پیش بینی می شود.</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SBoxxx/20222" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20221">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">عاصم منیر به تهران آمد.</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SBoxxx/20221" target="_blank">📅 11:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20220">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nmXRaZBCmekbA5_21PECdzp5KK-KPJZRyaNvBVtEoCBfRBtllK8wKlaZ1FYjc5OmNXaXWJARjA6LcVX_FE2N3ZuKQTehaCtBXXh6FJ39hktXfkDYypYoLbb3671d2hF1x_Qnu4BIS21Lpphx3xO2257nmTZGoH6Oo02d2yYsj5KkEPpUbpO6JkxF70agHq5KW0PQwyLyxZRbyoiuvVy0OV3V7rCZOV0tLBLUf7HGZKYRnhIgdYcTqAPydoksYoNtetKr5GxRz8BgL1_5hncwcsK7dPt8bQMYCNVOcJZhMubRMOBciwWOTIuDgfkPr8w-o-uHS6DD_WHfV4ArVEKrew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه NBC:
حملات موشکی و پهپادی ایران خسارات بی‌سابقه‌ای به تأسیسات ایالات متحده در خاورمیانه وارد کرده است که از هر آنچه ایالات متحده پیش از این با آن مواجه بوده فراتر می‌رود
- میزان این خسارات از هرگونه تلفات قبلی ایالات متحده در تمام درگیری‌های گذشته فراتر می‌رود.
- بازسازی زیرساخت‌ها طبق منابع خبری، میلیاردها دلار هزینه برای واشنگتن در پی خواهد داشت.
- این حملات نه تنها به تأسیسات اطلاعاتی، بلکه به سیستم‌های رادار، تجهیزات نظارتی و پایگاه‌های نظامی ایالات متحده در عراق و سایر کشورها نیز هدف قرار گرفتند.
- این خسارات سؤالاتی درباره توانایی پنتاگون و وزارت خارجه در ارائه حفاظت کافی برای تأسیسات خود برانگیخته است. کنگره از همین حالا بحث‌هایی را درباره تأمین مالی بازسازی تأسیسات آسیب‌دیده و تخصیص مجدد منابع اطلاعاتی با توجه به افزایش تهدید از سوی ایران آغاز کرده است.</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/20220" target="_blank">📅 10:37 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20219">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط انرژی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c1NJbI_LY9mbd8TRK6ans73FBKPblsBGlnKTtM9wN1gBs1Qqw31jOaDWQfQVei_rJdMdjvh9XgwpRaR4iCmrJnS4OWDH04DsLIBCgaIRp8qJAVqdOF1gpqnap84I7ilZWEf0auKB0ta1ET7bRG-N9k95QdoOo755ru1LirBNN9fKuCaoXHPpMhqdZwvSlLBA7pUz4G3phRv37qWkXIjg9MNRNgI9J261kBp8qH1MAzpOvG7hK2nIjkUTyOSwN8UOYOT810PVdMBy8wlKqT6RBrmNDHNih8len7hbFDIWyyKnHQVN6qH5nru_yYTT2MVvpt00-up9gVD8tvEw0E08uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
روز شلوغ انتقال نفت در دریای عمان
🔹
کپلر: در دریای عمان دست‌کم ۱۵ عملیات انتقال کشتی‌به‌کشتی در حال انجام است.
🔹
حجم نفت خام درگیر این عملیات حدود ۲۵ میلیون بشکه و مقداری فرآورده نفتی است.
🔹
نکته مهم اینکه منشأ این محموله‌ها تقریباً از تمام کشورهای نفت‌خیز منطقه به‌جز ایران است.
@khate_energy</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/20219" target="_blank">📅 09:07 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20218">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ترامپ می‌گوید توافق هسته‌ای با عربستان سعودی تنها در صورتی پیش خواهد رفت که ریاض به توافق‌های ابراهیمی بپیوندد و اسرائیل را به رسمیت بشناسد</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/20218" target="_blank">📅 02:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20217">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67c56a73bd.mp4?token=JSd5YBvCxklqeQ4d-Iap2jkyWZksVPPYyTDNQueC75i7uc0cxkZ3YlgxYAYSFZil8DxTuZifTD026Dzavt7kkGAp1JYgDtJ3jbPDZSFLtYBOAR1wQJnctlLyiSQ7ChAOHTILNO0kRnii0zQEKf_SyCaDNQs8cXZQBODIt6X93EdWP2bM-thm655TAQBZcyXzTdc0FO0nF5CfDE0egaXzY5RYYXFcV_uLXnlgy_BLWr8vQ9czbR_uCOgvFmDUb4SaO2niRSzpzxVCN7zZTdfNb74L3X1fElNkpVY6hiyQz0qVnOmZCETYH4Jxtq3gbMRrnidmeNULv4RZTJb1UxYwwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67c56a73bd.mp4?token=JSd5YBvCxklqeQ4d-Iap2jkyWZksVPPYyTDNQueC75i7uc0cxkZ3YlgxYAYSFZil8DxTuZifTD026Dzavt7kkGAp1JYgDtJ3jbPDZSFLtYBOAR1wQJnctlLyiSQ7ChAOHTILNO0kRnii0zQEKf_SyCaDNQs8cXZQBODIt6X93EdWP2bM-thm655TAQBZcyXzTdc0FO0nF5CfDE0egaXzY5RYYXFcV_uLXnlgy_BLWr8vQ9czbR_uCOgvFmDUb4SaO2niRSzpzxVCN7zZTdfNb74L3X1fElNkpVY6hiyQz0qVnOmZCETYH4Jxtq3gbMRrnidmeNULv4RZTJb1UxYwwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی overbought است</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/20217" target="_blank">📅 01:28 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20216">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">خیلی overbought است</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/20216" target="_blank">📅 01:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20215">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">یکی از همراهان کانال این را فرستاده و گفته:  پایین کانالتون شاهد خروج سفیانی هستیم
😁
سبحان الله راست میگوید این شیُ عجاب دیگر کیست؟!</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/20215" target="_blank">📅 01:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20214">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5affe27b93.mp4?token=SV9JJJlrSTShUES930CJ27lTtU2gZTXkkX8w3bRQgYsTisUikOQ_a6LFiC20q57RLopPw_8e9-53rlqAn7vVkg1wmWpsSQUZiCIBtlRdfkpXyrDS3iyqgyUVeq8vSlR4NMre3OuveJo_Yu2J0FGoGpQmkZ1EXmX5Z05BLsDNwFj1qaCHsUdfb6P6tqEQZSHcrgNk3FE7PJPlK3nE3AXEHwIvL7tufl1Zr4-nvECu-KOzNZMa2n60wyYggcbr-H0widhaPU6KnJ9GP4RIzLWYS3wyhhj5TbBLWFiSxVnLeRuHxTZNd5Ct5FTQY-lMgYt5p-CqJXEzYpkPEFG6DFWXcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5affe27b93.mp4?token=SV9JJJlrSTShUES930CJ27lTtU2gZTXkkX8w3bRQgYsTisUikOQ_a6LFiC20q57RLopPw_8e9-53rlqAn7vVkg1wmWpsSQUZiCIBtlRdfkpXyrDS3iyqgyUVeq8vSlR4NMre3OuveJo_Yu2J0FGoGpQmkZ1EXmX5Z05BLsDNwFj1qaCHsUdfb6P6tqEQZSHcrgNk3FE7PJPlK3nE3AXEHwIvL7tufl1Zr4-nvECu-KOzNZMa2n60wyYggcbr-H0widhaPU6KnJ9GP4RIzLWYS3wyhhj5TbBLWFiSxVnLeRuHxTZNd5Ct5FTQY-lMgYt5p-CqJXEzYpkPEFG6DFWXcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از همراهان کانال این را فرستاده و گفته:
پایین کانالتون شاهد خروج سفیانی هستیم
😁
سبحان الله راست میگوید این شیُ عجاب دیگر کیست؟!</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/20214" target="_blank">📅 01:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20213">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">این مسیر محتمل وقایع آتی از دید من است:  — شکست عملیات طرد اقتصادی در تسلیم یا فروپاشی جمهوری اسلامی — حملات جمهوری اسلامی به تاسیسات نفتی و گازی منطقه — آغاز دوباره جنگ — عملیات زمینی آمریکا برای تسخیر بخش هایی از جنوب کشور با این نتیجه: موفقیت کوتاه مدت…</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/20213" target="_blank">📅 01:09 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20212">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">اقتصاد_ایران_ممکن_است_از_دوره_ریاست‌جمهوری_ترامپ_جان_سالم_به_در.pdf</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/20212" target="_blank">📅 01:09 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20210">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">اقتصاد_ایران_ممکن_است_از_دوره_ریاست‌جمهوری_ترامپ_جان_سالم_به_در.pdf</div>
  <div class="tg-doc-extra">299.1 KB</div>
</div>
<a href="https://t.me/SBoxxx/20210" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">این بسته جدید بسنت سروصدایش بیشتر از تاثیرش خواهدبود.  چین اگر بخواهد — که به نظرم می خواهد — به هر قمیتی از سقوط کامل اقتصاد ایران جلو میگیرد و همه ابزارهایش را هم دارد که اینجا اشاره کردم.  کالاهای موردنیاز ایران را کماکان تا جای امکان صادر می کند و پولی…</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/20210" target="_blank">📅 01:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20209">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ونس:   کنجکاوم بدانم قالیباف چقدر در درک زبان انگلیسی خوب است</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/20209" target="_blank">📅 00:57 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20208">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TKSYZOMoX7E4RWQCqL1AOIG_MkyOQeJzccD7ei-noUvhNe6SER7m6MrS1xwbM_VKxPCdNBg_msE7mAUskmXFkh9TYBzwzuBn_KPthw9aUqEmP5LXyqu-Ia7e3MsF7BRYPyCXj6YYZuCcaytyHJS4w3xuW8iX0gm9SmQZy0PWWuPMdzoMBncD34gD4lUUSSraLKA90DTcB-OzrIBiPTLSRcdM8lhQzSoC3Zh5MZVPxpWZyM5WmNiRsf6KDPs9JrYICyFqGMy8VMtc9zUW1vcajeYSGyTf2LSDI9_lRW3XWjd_R9WZ2x_HgOmYxpKKxKrkOf1C_S4XbtKnTmxNRu9VHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت قالیباف در تمسخر اسکات بسنت</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SBoxxx/20208" target="_blank">📅 00:55 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20207">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">باید بگویم خیلی خوشحالم که عمانی هم نیستم!
از یک طرف ترامپ می گوید آنها را بمباران خواهدکرد از یک طرف دیگر ایران می گوید که باید مسیر جنوبی را ببندد که البته خودش هم می گوید بدون نیاز به مجوز عمانی ها هم این کار را خودش کرده!</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/20207" target="_blank">📅 00:27 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20206">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">غریب‌آبادی: در تفاهم جدید عمان می‌پذیرد مسیر جنوبی را کاملا ببندد
البته درحال حاضر هم نیروهای مسلح ما اجازه عبور از مسیر جنوبی را نمی‌دهند.</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/20206" target="_blank">📅 00:25 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20205">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">کاظم خان امشب اساسی رو بای نفت است</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/20205" target="_blank">📅 00:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20204">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">چرند.</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/20204" target="_blank">📅 00:10 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20203">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">با این وضعیت می‌شود فهمید چرا ناگهانی تصمیم به دوبل کردن قیمت بنزین گرفته اند.  وقتی عرضه سقوط کند، کاهش تقاضا با جهش قیمت یک گزینه است.</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/20203" target="_blank">📅 00:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20202">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FqIO7njdBD-LTa-Na9sY4dBW3gGcAvVHaHvBxp1oKLT-XxRBG1mmfgs1k5sa_R6H4Fb7mbexiD54pUH_JkDVGkCjtpRucDW9liJlf8A6lNfLFv5pq3HL1vfQTrlndTq_znqzC6lmrmp1NUiPTjJbDt_ISSRm-pn1oCUXK7PsOKTupfZ3PZQTbB2u6LJ5-RXOm6fLmEIp4-HIT6zbKVgNGYwqaCJLiQsrfsZkW4vl9rplM1fn8QPCwAsTO8NurA9sN80mbjBVl6ll--gpery3IxI3cq2Rve4I1Wk1OSGBDVZQbjw8FuSUuASAU7iXWQjw7YcxWHHvEQ2UDnFGaM8B8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#Gasoline
— D
قیمت بنزین به نظر چنین مسیری داشته باشد.
کاملاً حرکت نزولی اصلاحی به نظر می رسد و تریگر آغاز چنین حرکتی می تواند زدن تاسیسات نفتی منطقه توسط سپاه باشد.</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/20202" target="_blank">📅 21:07 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20201">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/erONaaBfMSg2msoxVLgKgYeYD7xDwWGNPq9QY_j80cR9-Hx0DjwpqHRLcB_bV9H6Kwyrlt_oVEuyk6RAebajhi4BTh2xkaHljbfWTr-Nf3K1-OKSsapK_z0L6M7BoCFj_NXwBGXKgtJ3iov3zKDYTvqWYL5UnoiS9LpbOeECW73WmGP-qy1WKhkxOQyYVcEfxb7s8v6Z2enINAoTxrQPBh_buQsmCf-zI8sFxrqq05tNEtLVw-5bya5spPlbu9emNCm3I9VDkkgvbp2fExUsDsqrKjUVp-oBY6lBHqSi6dmet69z1ynFq_cLl4bpcgcH5QdBE1F3UfKiiuIi_lLwgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید اسکات بسنت وزیر خزانه داری آمریکا
رهبری ایران در حال اعتراف به شکست اقتصادی است.</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/20201" target="_blank">📅 19:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20200">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">وزیر جنگ اسرائیل: از سوریه خارج نمی‌شویم
کاتز: تا زمانی که تهدیدها علیه ما به قوت خود باقی باشد، ما از جبل الشیخ یا منطقه امنیتی در سوریه خارج نخواهیم شد.
ترکیه در تلاش است در سوریه مستقر شود و ما به همین دلیل وارد عمل شدیم؛ زیرا منافع امنیتی اسرائیل در معرض تهدید بود.</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/20200" target="_blank">📅 19:31 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20199">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ایران و عمان گفتند که پروژه‌ی مین‌روبی در تنگه هرمز را بحث کرده‌اند</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/20199" target="_blank">📅 19:20 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20198">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y0ZKz3DFOY0EZMB_wwj7aFg1SbWa3gqmnLO7HWPmMuzyh-KVVmCbEj9d5oGkjwsQ1g6e6fBR0Ek97WK48nPs-z4GQaBgjHhZS_x_CR6V1khpEdjH4ni6YAbd7E1toJ18TjLcRwa70VB9-C3FNOGw0tduk9zjIVo6smVcNDsJbdeVcKA-2jV25L4ND_p4-Mg-q0zu5v2_XyHqFF3DDYoF6-hSLh2C6LAFJcMdwOBE0oF1L8cubVmPSTYNU4D4yhnOtQkipxuZbpV7bj_ODLg5krOP_HKV-cZ1UGYVGgWt6GU41KODYwUubRQa7IhKRtg-zlr0nEtj1hl8WcGIFrJ20g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
تمام مین‌های دریایی که سپاه پیش‌تر در نقاط مختلف تنگه هرمز قرار داده بود منهدم و یا جمع‌آوری شدند.
همچنین وضعیت تنگه هرمز به صورت وجب به وجب تحت رصد ماهواره‌ای (نیروی فضایی ایالات متحده) قرار دارد و هر اقدامی در جهت مین‌گذاری مجدد با پاسخ ارتش این کشور مواجه خواهد شد.</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/20198" target="_blank">📅 18:26 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20197">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qR_WuMqzYMnPzMdtjbhyKwGAdRWjGvsIGuYSNpHvXfxlFK3ZKUwuVeCi_69b4f3mhOtrMF5w87p2DlRAJM_DT9aetbFPoKK5bZ-3SbaDFQlMz_2Zs0gZC2mDrcEfiFRCaYcUguUzxeMMfhmGHt48YbgHuReF7E7BLaJ1-uZ9rYoMtUSUMktxFvfK5eILCNI058SHs48TBUgM1QEeAz3kxYOcYWUjsAg7E5JjQAkNGyJYSYPWMYRMVP2TXODRvZeOsrgudKgFjt3-3YMUQBAgaKuKQXw4ZVfT3xQNahB6GQDQeG_ECX6Qcx62ZUYa42WdTaqt1y9WGyLjVJUcBs3Aew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عن این مفنگی را درآوردید!  ولش کنید دیگر بگذارید بمیرد.</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/20197" target="_blank">📅 17:16 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20196">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/daq4KfIQ5PT4XNHl54nFLfsspAkFRM9IPjovYPuHiBNzFOQJUGLQsvpUOBFamWK90A-Odrmx0uPvHdBBsOSNBgRiouKHiNb2raWh07fcp7zzDEvfv2QC2VN1ETlYxjlBu_ORm_D2uitDv7Jc9ZRB20UeqfB9ekdtDYY9Em_kFn7QbxRpaS1C_F7s_zSC3DcnJzk_Lz4pDGeCg575J4Sf73mD2R4FJBOMpGTWu2WPx-d2urJ-YIuBux5d3d2AKW1T5SMo817L3hlPDYOo3WxBxHkvvAasZhMBOSMcffYnhowiNcAPE-aV7nIjnIlhMFd9PQOxFg8cwkyKXMvBo4TMbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ
«جمهوری اسلامی ایران که در حال فروپاشی است، بخش‌های بزرگی از نیروهای نظامی خود را حقوق نمی‌دهد و هم‌زمان، در سطحی بی‌سابقه اقدام به کشتن معترضان می‌کند؛ حتی افرادی که در حال اعتراض نیستند.
این یک بحران انسانی با ابعادی بی‌سابقه است و باید همین حالا متوقف شود.</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/20196" target="_blank">📅 15:19 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20195">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">لحظه ای که روسیه ضد اوکراین سلاح هسته ای استفاده کند، آمریکا هم ایران را با هسته ای خواهدزد.  شاید هم اول آمریکا بزند.</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/20195" target="_blank">📅 14:47 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20194">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">حالا اگر تصویر میکنید که یک فروند ناصر همتی میتواند جلوی این روند ژئوپولیتیکی را بگیرد که ولی خب.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/20194" target="_blank">📅 13:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20193">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبلومبرگ فارسی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cU6EUGXwbmqA_mveijnIpVV8CwU7_FHLgYJed1Nb4ai5yOJn5D2t7AGyOOTR3VaClhis7V3sIUWfxuoyh_tKvIAyrv3XqhKEYAfldz9PRSlGE5r6fZzk83UpepiATGaVv5eMNicNG3I6Jp1JatuKm7m8IQHwMXMvz1SDYcx9tD8gw4GuRG7V0BvmJTvPCeUM3UH2WI_RlzYpxn2vP93wAfv69aMeTcfWQMU44NrNnOmWaVpueAezCrdfMQrBkBENpp9eH14WX_TDnwhjPhq3izhG3S1YfmQTs084JvQAaMYE4fuPdtWBC3f7kcteLSyabv2ZDRCqUhafAhRBClzgqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقای همتی از زمان دلار ۳٠ تومانی تا امروز که دلار ۲٠٠ تومان را پشت سر گذاشت به آینده اقتصاد خوش‌بین است
☑️
@persiannbloomberg
بلومبرگ فارسی
✔️</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/20193" target="_blank">📅 13:55 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20192">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bwu5px-TZ29ND1ZgzUepZB6PWecUJB9NBZeD_zapdtvNyqASsOBSDYdOUYKYQ7lqYoxA7MX9A9fIDAOKNvldJ3nf658ycnIMcdlLSLDvZHkRtgGrGJAAgWsWopR2O6zScXlW02Y0_mAjI7YUXZYAadiGdsJ1lGj_A95L8FsQgQUN3catCowu7WTHwv5CDW8VobI9sP6rUknJmryJXmANuHYD67GaXjNFZTLambk_RBTk3TBMnoVHkqHxveSQRKWWFRL2JkM8dKib6gQm7HKBkGpf_GfHX8bG-dyKB-kqK49E9w3uxjJxX5oFfAqusxib9o2-Mm0prHvedIJ_U5ibjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادغام شبکه خبر و اینترنشنال</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/20192" target="_blank">📅 12:12 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20191">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">چرند.</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/20191" target="_blank">📅 12:12 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20190">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">یک منبع مطلع در خبرگزاری العربیه:   آمریکا پیشنهاد کرده است که در ازای باز شدن تنگه هرمز و توقف حملات توسط عوامل، محاصره را متوقف کرده و تحریم‌ها را رفع کند.</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/20190" target="_blank">📅 12:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20189">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">یک منبع مطلع در خبرگزاری العربیه:
آمریکا پیشنهاد کرده است که در ازای باز شدن تنگه هرمز و توقف حملات توسط عوامل، محاصره را متوقف کرده و تحریم‌ها را رفع کند.</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/20189" target="_blank">📅 12:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20188">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dtg1bmdYF2xMRCc2REFxwlGIaPwLJ0B1R6isnlYnM_YvWc9vBKcyy5BhQjtyjxWkLfcO-LGoyZYHgGsSxy9H_nlcnqvXMp3ATZzvZ_RUIbomzw5yXP3L8NaMmxU-Qkpnwwsl0R1o3xm16cQVYEgElWQR8RgFYo23CuDncy8ipyt6arp3O6Uu3HcpsZBGk1adONVoTcYpXfSqAq6BkWxGqZXIL4HQmXy_-7DN_QnKLiCL7hoQo--zrJ9SPtszV2UvLzkpdADwIFJYiOdQZqCHf1gThSzSqgTNVWYJgoZK0yzeYbytkoy5xtduVUkbqC-XAcEKsCn5KmC_c-q77KiA6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز هم بسیار بالاست و پیش بینی می شود شاخص نزدک افت داشته باشد.
طلا هم با این وضعیت قاعدتاً امروز باید به افت خود ادامه بدهد.
دقت کنید که سقف دیشب عملاً جعلی بود و بعد از ثبت آن حدود 800 پیپ افت داشت.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/20188" target="_blank">📅 11:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20187">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJpW4_TkZpfft-yYHn8qJy1Y350iNlKo3GzaewolkWQVZtahqtq_v-l1KhLWz3QeUAG2Lm20bKfIajc22Lr3oYUs9pyx1dQBoFDHSD1D0lMCQjn9NrtB4L0CRrXdUnbQzXSpGC6kkGm_Z7YzNCjaVA5mvKwphnn2DNLeEKYJSTHsFAsUeFxNTVqf1_S9C5sZG3pBL94aN5UfE-844lMuT0nQuWXF1I1YcqizNkEBRV2FU4MSopx4-QGUpAHNCFXPbRCY1KY7jsJBgrweaCbmG1FfOISqX04A3lthbaE5bT1-q0Z-2xwzVSc2uG_NveN-8qsouTY87BfEa_vB4UzO_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موج 2 نفت دارد تمام می شود.  موج اصلاحی دلار به ریال هم قاعدتاً باید آغاز بشود با تارگت 240 به بالا.</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/20187" target="_blank">📅 10:38 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20186">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gidUqY7z5fFywNEJbMIvXlqvQ-uj9j6e4HCijYJDjHjFdlqRh1c8G5WAn18lLSiBKq9sAcEbASeMFUiclPciskRM428DX8t1TqrhpHTjoGlD-Ee1YS8LrWx9xyx-67m8tc7nOQFEVBVTg-RQ6Oyh9spPpLDhgYsiMFgj98SxLgP6TTbvjPITGFiQM1bUB3m3Hc3ozpyHs8XVsyUSlSxGB03u3Ew_aQCJp3Ww17uHHoI4_vYGDOw2gm-2RGgjB1pUfh01wq7KrTI-9WiwOxFdaePR1mp2nmMrF3re-808TgZD5EsCTtu-4gI8B2YomsSKAB74h-S-QS8WZLy3RwzQ2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بسته جدید بسنت سروصدایش بیشتر از تاثیرش خواهدبود.  چین اگر بخواهد — که به نظرم می خواهد — به هر قمیتی از سقوط کامل اقتصاد ایران جلو میگیرد و همه ابزارهایش را هم دارد که اینجا اشاره کردم.  کالاهای موردنیاز ایران را کماکان تا جای امکان صادر می کند و پولی…</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/20186" target="_blank">📅 03:24 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20185">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BYeO1uoH-RnsoXOzPhIyaqsqeM1ueSYQ4xYU3N8qDLYLokI5g1WHLpfjmeJF0e6hWc20QBFDMTKKjcFa1I5lrntRpNGOJ8WrfFNzVamAWOhGo1HNJv5DPv_zfV25D7an0GwyKsILIbr-_ycajFtaBPjQI_jZZqddhhBy3iFwwiWs9qLBUoyZWesYGP8u0IcfUIyqqQ-Rtv-a2TAmHrrPbb2JUnzdRGctHIQ3CjvFJH1zhocAj1CwFYftUvQhfjQxBy-VXoeJD-nNl1DvLtfjcUd0Uahvnc4N9WWWH9zpUSUzafT5Tqp5hGyhapoM-OAmAR3iGqdP8Ix9YgjBvGsnyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح بسیار بالایی قرار دارد.  دقت کنید که با آغاز برنامه بازخرید اوراق قرضه بلندمدت خزانه داری آمریکا، یک عامل جدید وارد محاسبات شده که در این شاخص هنوز آن را دخیل نکرده ایم که روی طلا موثر است.   ولی با این حال، پیش…</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/20185" target="_blank">📅 03:11 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20184">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">فرمانده انتظامی کل کشور در ساری:  جنگ سوم هنوز تمام نشده لذا باید با آمادگی کامل در برابر دشمن، غافگیر نشویم، چرا که خیلی از غافلگیری‌ها نتیجه غفلت بوده و دشمن از ما دست برنداشته و جایی از ما دست بر می دارد که ما دست برتر داشته باشیم.   دشمن به‌دنبال ایجاد…</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/20184" target="_blank">📅 01:24 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20183">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">تحلیل عوامل سیاسی چرایی شتاب شدید رالی اخیر دلار</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/20183" target="_blank">📅 01:23 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20182">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/313a4a00f6.mp4?token=QlA9-PfwWUqT9affTii4Ciwd62C5NjDzOqqv9sXM0A059R9CsnvJ8ortgR891IArru8FrNuEjjkVRxmUQ4ajNQoQqem29GN57tW4hD1pfLh00cw2SmQZfFRuNFg8q5k57R9NnNd7w5se73kIRXui7GehmVtikhdbvodp1dcfAyaLlUCUYY8Psbr2D8Bpg-V07Qe_LHEeMO0KX05ruvE-0jw9rQyoJOaOnAzIrSwXtdAB6tTmLkvY4izmxTb47yGg-N9aoYMTwLC5Xa8tDJw8pRMXy2CxbmiJ58eC33VeEW1lV9knjTvyJMiOFzP-QDnzZQGL1dMxHauw-jYRJbPsGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/313a4a00f6.mp4?token=QlA9-PfwWUqT9affTii4Ciwd62C5NjDzOqqv9sXM0A059R9CsnvJ8ortgR891IArru8FrNuEjjkVRxmUQ4ajNQoQqem29GN57tW4hD1pfLh00cw2SmQZfFRuNFg8q5k57R9NnNd7w5se73kIRXui7GehmVtikhdbvodp1dcfAyaLlUCUYY8Psbr2D8Bpg-V07Qe_LHEeMO0KX05ruvE-0jw9rQyoJOaOnAzIrSwXtdAB6tTmLkvY4izmxTb47yGg-N9aoYMTwLC5Xa8tDJw8pRMXy2CxbmiJ58eC33VeEW1lV9knjTvyJMiOFzP-QDnzZQGL1dMxHauw-jYRJbPsGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت های امشب محسن رضایی دیگر قطعی کرد که جمهوری اسلامی به دنبال زدن چاه ها و تاسیسات نفتی منطقه و نیز خط لوله های جایگزینی است که از سوی عرب ها و ترک ها دارد ساخته می شود.  منتظر نفت 130 دلاری باشید.</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/20182" target="_blank">📅 01:16 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20181">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">کری خوانی وزیر خزانه داری آمریکا برای عبدالناصر همتی:   به زودی دلار 300 هزار تومانی تحویلت می دهم</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/20181" target="_blank">📅 01:12 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20180">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6P16qgxt0Lk2Cm7ds_Tu0ITyCg1i1v1SDkTNCHiaI3hEhdVchx79UAJ6CPNiqyqTWE0vdsVI0MhHNRbF42EoWUgN2ZVBjr8zXcxz1XrQ6PFb6KelpYdRIdUjjRzM1FnuLOUBigzI5EtyN9oCkHKKbWjg5ZduoOlxAWIvDcp5sYjDJl4WTCRMCru1zrpIGv9oXIR0jjmdn_PUIsdrcA_wG7N7U90NCBu31D6tU8Z1OvxJoYmk5gMwAlfSeemoqFKvebadLO8kWfjiv4UUAL_Cs3aEUemarMTbWB-LgcYxuZFFtUsG8Mup6Iy8pNq36B3iK4Zs-Lj6V2QPPhV9D88kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ذخایر نفت خام آمریکا به سطحی پایین رسیده است که از دهه ۱۹۷۰ شاهد آن نبوده‌ایم.</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/20180" target="_blank">📅 23:53 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20179">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">— اسکات بسنت، وزیر خزانه‌داری ایالات متحده:  «امروز، وزارت خزانه‌داری ایالات متحده عملیات طرد اقتصادی، یک کمپین بی‌سابقه علیه جمهوری اسلامی ایران را آغاز کرده است.  ما در حال آغاز یک حمله اقتصادی علیه ارتباطات مالی ایران در سراسر جهان هستیم. هدف ما قطع هرگونه…</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/20179" target="_blank">📅 23:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20178">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c9M4qFXWAVA14y9UR_KkUKJW8qdHO9tLKmIt-Giu-L-4_1rAcaSjuPFbeMrZoo0PRx6bdnuMc-CUdTYdR8r9nxp8VtdnyZAyRcnrgVkaopM6H-f5DO-pL2M2XQTO2Gi61XWl0kWsWvZYZv0q6cJApXsUNP9DRXYL2whYBGXWbwErKVO2UkOrLPXNZmz5SsBC7bC22MC2_kcgxXipNB0R1hk1msyp94CEDkLmM_pRC2RvLFHn9bgN7sw1DQfQCL78vd5HvsobM6VZmF_tW9WewYOmClEQXA5frsZWgHldP-7HUVqrIrwA1CDnp7gBHWEFPcMVDmk9ESFfYWh4Exw0xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">— اسکات بسنت، وزیر خزانه‌داری ایالات متحده:  «امروز، وزارت خزانه‌داری ایالات متحده عملیات طرد اقتصادی، یک کمپین بی‌سابقه علیه جمهوری اسلامی ایران را آغاز کرده است.  ما در حال آغاز یک حمله اقتصادی علیه ارتباطات مالی ایران در سراسر جهان هستیم. هدف ما قطع هرگونه…</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SBoxxx/20178" target="_blank">📅 23:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20177">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">— اسکات بسنت، وزیر خزانه‌داری ایالات متحده، درباره‌ی چین:  «ما می‌خواهیم امروز اینجا روشن کنیم که هیچ‌کس فراتر از دسترس تحریم‌های ایالات متحده نیست.  اگر آن‌ها تسهیل‌گر معاملات باشند و بخشی از اکوسیستمی باشند که نفت ایران را به پول و سرکوب تبدیل می‌کند، هدف…</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/20177" target="_blank">📅 21:57 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20176">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">نتانیاهو: ایران تلاش کرد یکی از پسرهایم را به قتل برساند
کانال ۱۲ اسرائیل: سانسور نظامی ماه‌ها انتشار جزئیات تلاش ایران برای ترور یکی از پسرهای نتانیاهو را ممنوع کرده بود.</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/20176" target="_blank">📅 21:39 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20175">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">— اسکات بسنت، وزیر خزانه‌داری ایالات متحده:  «خطاب به سربازان عادی حامی این رژیم: همچنان که حقوق‌هایتان بیشتر و بیشتر قطع می‌شود یا ظاهراً فقط به تعویق می‌افتد، از خود بپرسید که آیا فرماندهانتان کشورتان را برای پیروزی ترک می‌کنند یا برای ویرانی، و به یاد بیاورید…</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/20175" target="_blank">📅 21:26 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20174">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">— اسکات بسنت، وزیر خزانه‌داری ایالات متحده:  «ترامپ در حال برقراری تماس‌های تلفنی با رهبران جهان است و درخواست‌های مشخصی برای توقف تعاملات آنها با رژیم ایران دارد.  اکنون زمان آن رسیده است که رهبران جهان بین آمریکا و ایران تصمیم بگیرند.  هر نهادی که از طرف…</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/20174" target="_blank">📅 21:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20173">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">— اسکات بسنت، وزیر خزانه‌داری ایالات متحده:  «امروز، وزارت خزانه‌داری ایالات متحده عملیات طرد اقتصادی، یک کمپین بی‌سابقه علیه جمهوری اسلامی ایران را آغاز کرده است.  ما در حال آغاز یک حمله اقتصادی علیه ارتباطات مالی ایران در سراسر جهان هستیم. هدف ما قطع هرگونه…</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/20173" target="_blank">📅 21:24 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20172">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">— اسکات بسنت، وزیر خزانه‌داری ایالات متحده:
«امروز، وزارت خزانه‌داری ایالات متحده عملیات طرد اقتصادی، یک کمپین بی‌سابقه علیه جمهوری اسلامی ایران را آغاز کرده است.
ما در حال آغاز یک حمله اقتصادی علیه ارتباطات مالی ایران در سراسر جهان هستیم. هدف ما قطع هرگونه شریان اقتصادی است که این رژیم استبدادی را حفظ می‌کند تا زمانی که تهران به تنهایی بایستد.
از امروز، ما حلقه محاصره را تنگ‌تر کرده و هر منبع درآمد بالقوه‌ای را که سپاه پاسداران و رژیم ایران را تأمین مالی می‌کند، مسدود خواهیم کرد. ما در حال اجرای رویکرد «بدون نشت» هستیم.»</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/20172" target="_blank">📅 21:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20171">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">صحبت های امشب محسن رضایی دیگر قطعی کرد که جمهوری اسلامی به دنبال زدن چاه ها و تاسیسات نفتی منطقه و نیز خط لوله های جایگزینی است که از سوی عرب ها و ترک ها دارد ساخته می شود.  منتظر نفت 130 دلاری باشید.</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/20171" target="_blank">📅 18:31 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20170">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TPNfUAABp-ObjlzAe2V9y9kmDWw3eYSfK9wQwK95imPLeK70bwbRKQWtk2U58_PiJJV4RYR9QWGNimFi3KU4S42blJVFlht9rwxtM9FYGbwQR-3oc04y9yf7JuHnEO-vDEPBXvH9sao0xpbehukXslU-3g7n23kC01VM7SY4ARNPizLbbWPNcBGffLKTK1RlN4Xgj4nU-e961KQAiystzof1tKysXuE7cfHX4WXkqx5yZvWFF9JajH6_21oOX0K7kqWxpKlR5FGhChPajwWtPUcuBpzwHCWRwiqRT82OJEG_fXNkyFd1TQFoOiKbujhAFiSs0l6Qw_cuGTcNC1Dp4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خواننده Secret Box از 2.5 ماه پیش میداند که هدف درگیر کردن ترکیه چیست. بزودی یونان هم به اسرائیل خواهدپیوست.</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/20170" target="_blank">📅 18:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20169">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">جلسه گذاشته اند برای بررسی وضعیت صنعت برق کشور بعد در همین جلسه برق رفته !</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/20169" target="_blank">📅 18:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20168">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">جلسه گذاشته اند برای بررسی وضعیت صنعت برق کشور بعد در همین جلسه برق رفته !</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/20168" target="_blank">📅 18:17 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20167">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c94f2d5d3.mp4?token=GbLGMNdOSUzD00NowDNDbgQ59Dz-qGgtinDZ06SIoRDQKdGctNis2omClheDB9EcRfi7kAmRmwdLBUjr4nctgqL16Nj3xElndz3RTq0OrW0P9LjpPgFCyDs6bdJFCr2_jD6HcBpywFvwGlnvtqRycPqBsR8SRWXs9cAWpSL7pknK_KpO63CInpvmA_ozScHlUOrFxtiDG2bnO2hJP61MgcQz2yXhRw7iNwtH29IcId8wTeSjmYECfXZfjHxR0TIa6K1mCIexWMFFNCAvqzVWxeWbP6mN77El8Tbcbiedm3Bw_CN0yvX1xIyWIfsHo8EE6rAbCIU0gWtmGnEDGZR0Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c94f2d5d3.mp4?token=GbLGMNdOSUzD00NowDNDbgQ59Dz-qGgtinDZ06SIoRDQKdGctNis2omClheDB9EcRfi7kAmRmwdLBUjr4nctgqL16Nj3xElndz3RTq0OrW0P9LjpPgFCyDs6bdJFCr2_jD6HcBpywFvwGlnvtqRycPqBsR8SRWXs9cAWpSL7pknK_KpO63CInpvmA_ozScHlUOrFxtiDG2bnO2hJP61MgcQz2yXhRw7iNwtH29IcId8wTeSjmYECfXZfjHxR0TIa6K1mCIexWMFFNCAvqzVWxeWbP6mN77El8Tbcbiedm3Bw_CN0yvX1xIyWIfsHo8EE6rAbCIU0gWtmGnEDGZR0Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:  ایران به صورت کامل در‌ حال فروپاشی است.</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/20167" target="_blank">📅 16:21 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20166">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y5w9cqbF9ixaYCGc97bgOwqopQzso320vVD2rDyDhJgGLpTIjYRKr6oChvpHBnNEz6BLxKn2dbCPsfZRx-46ovq7PjdPYHUpYXFz1HI6GxQaehF042_0YFDMSYUg9ZAsow_GtkL5leV52WN1apzOlISOvxzTLmPGeyoZG0xuZSLt-6jrIxDTcDc4k97L-O7FyVVKMWhnXO-TLhOlM88Kx7v-U7InywA6YkXdAZwdHmTAYP3OPurw7uMva82YF5NElUtqxtmFX7H9q65XlS07A-1ylkInMtA8TwwhNkk2csX5wqtLlZJL52Jnm7d_uufJyj_oF6vdXZNxZwy53k-MNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
ایران به صورت کامل در‌ حال فروپاشی است.</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/20166" target="_blank">📅 16:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20165">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">وزیر سابق دفاع اسرائیل، یوآو گالانت، درباره ترکیه:
باید درک کنید که وقتی ایران تضعیف می‌شود، آن خلأ توسط کسی پر خواهد شد.
نامزد طبیعی، با آرزوهای امپراتوری در خاورمیانه، ترکیه است.
ترکیه یک کشور قوی با میراث امپراتوری است. آن در پل میان آسیا و اروپا قرار دارد.
آن بزرگ‌ترین ارتش ناتو را به جز آمریکایی‌ها دارد، یک صنعت دفاعی بسیار قوی، مردمی سخت‌کوش و در عمل یکی از مناطق اصلی صنعتی اروپا است.</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/20165" target="_blank">📅 16:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20164">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJm3GqzJ5JMpY_GNdons9_UIC7BhPdb_WMG-LwfF96T_5HeOUxWauvU3YpiIUxjY0lvz2411qEir3AIRg66HRu089pu07s5ZSBx2oN6Z5yr4p0stsJi3HWQBNoapcHr0HXjin0z-2QbMhO4PpK87Ntln0Ktjld5VmYExBg7-xnJEwyKGM5o_IbzU7v4p4kxXptSQPZtjR60-kshiqI37hxeMmTW3B6kTQ0BTxn6vogO5LBtqqvKUH5nPDN93xnl_OWYl4zu9h980f-_Fkti95UfbhR0n_zGsR6aA-MIFODcbodZHzToxdEAmneWlAayRQAqsg5x529SpHWJfFcpQGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موشک PL-15 و تحول در نیروی هوایی مصر  همانطور که در یادداشت پیشین گفتم، محدودیتهای شدید اعمال شده روی تامین موشک های دوربرد هوا به هوا برای مصر از سوی غربی ها، مصر را به خرید جنگنده J-10 CE چینی واداشته که مجهز به موشک دوربرد PL-15 است.  اما این موشک چه ویژگی…</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/20164" target="_blank">📅 14:00 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20163">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">Secret Box
pinned «
این بسته جدید بسنت سروصدایش بیشتر از تاثیرش خواهدبود.  چین اگر بخواهد — که به نظرم می خواهد — به هر قمیتی از سقوط کامل اقتصاد ایران جلو میگیرد و همه ابزارهایش را هم دارد که اینجا اشاره کردم.  کالاهای موردنیاز ایران را کماکان تا جای امکان صادر می کند و پولی…
»</div>
<div class="tg-footer"><a href="https://t.me/SBoxxx/20163" target="_blank">📅 13:17 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20162">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">هر وقت پاکستان میانجیگری میکند یک جایی ازشان منفجر می شود</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/20162" target="_blank">📅 12:59 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20161">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bded5954b1.mp4?token=ohitIbk_GjnXbZ6dMUoabE24IwEIOMM9WrlGvtG70_5Uc3dmMR8QKfvaj_2sstTkb2ZFr0BtHWOA88D742_IKgjUTHoq02payAknn7Zv3gtDYbQ_WVfZAx8MDUHG_IyRQhDxM22sLBHdes4EP7toeQXr6c8S9b1Zi9M_pZRGWLqG9srwRoGbSjgmP7-ZwLjDmgZ1SQuMhwPXO_clCEckd8b1e7ddxr2qic1euPTdh5hEhnEd8n91f_Et4s-lRA82QCIw13ThVm0BLVvFYuJZaD6J5gu4w1dREGc9L7KKqAo5hs4cu1S069J10QWJFBMJ6OiwtLPt4YWw47Jxj4lGbwjuVVdLyox-nqU5_cLRXW_uqvoqvNbpb7WqDQSJHf61js6lxfBgb3GPlpj2fKLAZBmU1xJr1louOzvfdCoV345MlO2YlIvxSWAsDF2Vt7d3Qt43oXbLpHZGsAMuAzWqY7KFNuhhDeW4nW_SwgE3WAiP_G1gG5QOl41-WR2osYbZAjbuBhccPe7QfMHLZ0TsaDSsEP0YxWSxKkEKV_RCDy4AlZq8GQuQOUFWHcRTT96XyW8C-w9V02YUW16ICs6zVFeK-r1M7IMdUvcQABHO-o_1JzQY_i_-HpM0xTm_R_N1fVEbkLg6pnTwdixIRpD6aqca0hGVXmE9G5IyDXnH21g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bded5954b1.mp4?token=ohitIbk_GjnXbZ6dMUoabE24IwEIOMM9WrlGvtG70_5Uc3dmMR8QKfvaj_2sstTkb2ZFr0BtHWOA88D742_IKgjUTHoq02payAknn7Zv3gtDYbQ_WVfZAx8MDUHG_IyRQhDxM22sLBHdes4EP7toeQXr6c8S9b1Zi9M_pZRGWLqG9srwRoGbSjgmP7-ZwLjDmgZ1SQuMhwPXO_clCEckd8b1e7ddxr2qic1euPTdh5hEhnEd8n91f_Et4s-lRA82QCIw13ThVm0BLVvFYuJZaD6J5gu4w1dREGc9L7KKqAo5hs4cu1S069J10QWJFBMJ6OiwtLPt4YWw47Jxj4lGbwjuVVdLyox-nqU5_cLRXW_uqvoqvNbpb7WqDQSJHf61js6lxfBgb3GPlpj2fKLAZBmU1xJr1louOzvfdCoV345MlO2YlIvxSWAsDF2Vt7d3Qt43oXbLpHZGsAMuAzWqY7KFNuhhDeW4nW_SwgE3WAiP_G1gG5QOl41-WR2osYbZAjbuBhccPe7QfMHLZ0TsaDSsEP0YxWSxKkEKV_RCDy4AlZq8GQuQOUFWHcRTT96XyW8C-w9V02YUW16ICs6zVFeK-r1M7IMdUvcQABHO-o_1JzQY_i_-HpM0xTm_R_N1fVEbkLg6pnTwdixIRpD6aqca0hGVXmE9G5IyDXnH21g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در حالی که ‌وزیر کشور پاکستان در ایران است تا معامله تمدید آتش بس میان ایران و آمریکا را جوش بدهد، شهر دالبندین در این کشور بدست جدایی خواهان بلوچ سقوط کرد!</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/20161" target="_blank">📅 12:58 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20160">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ترور یک مامور فراجا در ایرانشهر  به گزارش مرکز اطلاع‌ر‌سانی پلیس سیستان و بلوچستان، ساعتی قبل افرادی مسلح به سمت مأمور انتظامی در ایرانشهر با سلاح گرم تیراندازی کردند که در پی این اقدام، استوار یکم «مهران سالارزاده» به درجه رفیع شهادت نائل شد.</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/20160" target="_blank">📅 12:55 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20159">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvSdsxI_lozprSa_8OTSsDgcWyqn-icpTiVQBL99TjSuBTmLT-CAWRO8_mo4PxiQgwIJLai_v5sw-FU_t66uoodnpqosw9YXLx7kD4lgYqAM9jajJDs9WCBPv6XA4QW2Ziu0D8Ogr6Qik3niswf5StnegULL11HCwf_C-nWZs44n4nzHF2iR6z7nq5SxwHFl8wVBCi2P8ZO-PgShBnTKAb9-bw78zANfGVI6mMVwFRri-PF9OKK7HLSgoWth_7vuZkfxRohP2tEGo3bWNECSEVzJ9r69HztYqH_3oPOzw9Gs3Clp7ZoUdNw3SRJskVfPSQcthaPwPB8IyL9WeqXslQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس بانک مرکزی:
مشکلی برای تأمین ارز نداریم و هر کارآفرین هرچقدر اسکناس بخواهد تأمین می‌کنیم</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/20159" target="_blank">📅 12:52 · 02 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
