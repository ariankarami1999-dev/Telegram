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
<img src="https://cdn4.telesco.pe/file/rmx4GoyjeyIPANEXiOM8RG-fzUkdWHrF2z_r9lJ1u3iHMmIc0PEABf-fU0FnKwUl5UK_UMdKeDhA75leLsiJjvvyZUkrwiP24KVCDa_f4DwL23hqj1gw4EcaYy4VabghMu68RQXTgbraZQiwR4aSFAB4GxXwQSrQMj4-JRVgz5tGXrqn1oHjZptaLY3xBPkQ1xC96EXn-2m7ZwcYjKVbHSzudQ97iUiJs01YBh7vZRXq-Ro-qIHYag07rFzUVigERVX9T_Zb5IM6G6cjmDgERfKg5Gv90XW6thUkXLd4Io5BMVkGYfvd_OXmL1tQzHKv399P31CMhYD7afb4ZEVruQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.9K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-01 01:50:47</div>
<hr>

<div class="tg-post" id="msg-21124">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">نخست‌وزیر اسرائیل، بنیامین نتانیاهو، انتظار می‌رود این هفته سفری کوتاه به ایالات متحده داشته باشد تا در مجمع عمومی سازمان ملل متحد سخنرانی کند، در حالی که نگرانی‌هایی در خصوص اعتراضات احتمالی وجود دارد.
نتانیاهو قرار است به جای فرودگاه بین‌المللی جی‌اف‌کی، در یک فرودگاه نظامی در نیوجرسی یا فرودگاه بین‌المللی لیبرتی نیوارک فرود آید، که این تصمیم تا حدی به دلیل نگرانی از پیچیدگی‌های مرتبط با ممدانی، شهردار نیویورک، اتخاذ شده است.
هیچ ملاقاتی با رئیس‌جمهور ترامپ برنامه‌ریزی نشده است، هرچند گفتگوها با مارکو روبیو، وزیر امور خارجه، و سایر رهبران خارجی همچنان در حال بررسی است.
بر اساس اظهارات مقامات نزدیک به نتانیاهو، سخنرانی او قرار است بر ایران متمرکز باشد و ممکن است «غافلگیری‌هایی» در بر داشته باشد.
مقامات اسرائیلی همچنین برای احتمال اختلال در سخنرانی او در سازمان ملل، از جمله آزار و اذیت یا خروج هماهنگ هیئت‌های چندین کشور، آماده‌سازی‌هایی انجام داده‌اند.</div>
<div class="tg-footer">👁️ 928 · <a href="https://t.me/SBoxxx/21124" target="_blank">📅 01:13 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21123">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">صدای انفجار در نزدیکی جزیره قشم!</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/SBoxxx/21123" target="_blank">📅 01:06 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21122">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">صدای انفجار در نزدیکی جزیره قشم!</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/SBoxxx/21122" target="_blank">📅 01:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21121">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">گویا جلسه برگزار شده و به نتیجه نرسیده!  First Time?!</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/SBoxxx/21121" target="_blank">📅 01:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21120">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D8el29hTFhIdETRUfFzvqxNUEP9gweI4FMHCj5HSxzSiFDxGAWURlQ8Me0IPLN9i0wlAm-j5bjMGTe0THtl_-ezD3aj_1enA2_ngHbuOAV7yJm64C4qq1DNqwRCkQmS7AyTfyipGKB9_l9eN4gmvCIuTAcLtKBjKTnsIdAWRhMfKH3VaKOyOAMAZEDnkUu4tbe9n8GENYV7Vx1WP0-J1ra7-ZcYjPifope1icS8WfWN2GlKpHfZwUT7HRy8kra_XFdXc61EkYpAu1WmKVCLknyL--GiD-V1O3mmzIsI-fzCRrWke2vPS1nSmDC0DbWU-x3RibPOo5sueNTJfuW6TWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا اعراب به دنبال فراهم کردن شرایط دیدار حضوری پزشکیان با قاتل امام شهید هستند.</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/SBoxxx/21120" target="_blank">📅 00:50 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21119">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YV3U4Bm9rdpIFRVPiN4JqwyYeurlH_14-O8rBTh-dnk-sXGa1VCkLr0EltJnRHtayLPiDR07ih2e1vKw62J8hdPggt39txERsyu8ZeS_JsagxphzDzHJvlpcDsoBm5OVHnuALFpC78LjShXD3z4i5ZJ7dWqOnz2Bg82srD1Hd9S5DH70JcvU6PB9h8PJIEO2PWJYYzQbE6M3uMXwY2aTwamx4z-6neZNDmedCAMGfmbHdheKl7lE2Ry7Im-0ZChagKIRxci-hfjKgWafRoZ4LeT3_oMROLMBkjnb2IjmYpeiGXMWl3BdXl5suIvWZv1J5q_PAJI57JRTRra2bwd5RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#RUNCFD — W #SUNRUN  مقداری از نقاط ورود پیشنهادی ما پایین تر آمده است اما هنوز بشدت روی این سهم مثبت هستم.  پیروزی دموکرات ها در کنگره و توجه دوباره به بحث انقلاب انرژی سبز می تواند این سهم را به بالا پرتاب کند.</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/SBoxxx/21119" target="_blank">📅 00:46 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21118">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EGvUHd8EO02TXG1iQB6MdhfTJzxxx7P176Jl1KWCszK-gTc283FGFq5EF84lYWjLGUL1prGhpTRBxDK1RdSQXdRPIzfT9Oxe-Tp5OdO-bjcNXyu7aT_M3cVRui3yPU5vYi4QyvYgaOCd7d9cbNFsqzCH1vN0qJy_oIaaqH0XVtIhyIQaA-2K-I-kbPMTJ04smIaXo5ob8wRwkREWwZjSLH5XkfGmoIetthQzPHugh2wIuolRvRwU8h60tc1ZZCHhjPnNi89KOZ_mup95dgP6pYlqYpm52V8Jh0IOebNY_sYt1bSgRF3dVwA54e1jH0RBv41FGc1gbLUDLGGlfuiNRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#RUN_CFD — D #SUNRUN  از محدوده ورود دوباره حتی اندکی نیز پایینتر نیامد.  البته هر چه پایین تر بیاید خوب است، این سهم یک رشد دستکم 3 برابری دارد.  همراهان Secret Box در خارج کشور این سهم را دریابند و هم میهنان اسیر در درون مرزها نیز میتوانند روی بروکر WM Markets…</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/SBoxxx/21118" target="_blank">📅 00:39 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21117">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vtb0C7pHDzjaRhsZG0JWQkDPaOA6mHjU5F6FCSKperm0oTtYTNnfQ8i13bJUV7Q8jADXROjIS92iN_tfZ8N64rajy5AxpXdVcWjmbmgluS8BveEmXQqdCLWPoZBS-mC9II0LkdhkI7gzLQqAMTDQZ_DfkuUgKO6e2R09ksT-vf__MrooOHWnIN0ap9zKO4vQJZo8Mh5JU-h54PUuCETUrvHc-1DiSXQvlpc5L7XJHK4BGLz5UOOYAQ05Xet3c2Uh113_s4BcVdbwz_3Lf0uBGeNIjwSD-mJvnlLzNRSTt522dSglTOordO4JeyQxX000Dkv74ggvh9wj0oa7g1zx_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#USOIL   دوستانی که درباره نفت دایرکت دادند؛  پوزیشن های خرید ما به هر دو TP پیشنهادی رسیده اند و فعلاً خرید نداریم روی نفت.   تحلیل جدیدی از نفت ارائه می شود.</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/SBoxxx/21117" target="_blank">📅 00:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21116">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NvJTUM_ajja6DgMT6J-eV5-Tty95Zqhj_8aoq219g7rAvbkrTf96Tt6xxGcKsx3R1j3KMgTdmfFEzVDEWnSlol3AuCY0f9rcL-5VQWimgwFSL2dF47YY5O-fyNS04gwgmxVM1vhZHNmfy_0zzHZaJJNn7aucMnOPdZapqIYIxzO8JYO-KEHmIdf77j5DD8cTUShCPD0nQXdqPTL_Zx_UQtqD4npmV1cVmkyOZOXan90vYzuxCUh9wGLxU3cKjL-yvuWxg0qR7bx8suW38YurCR0_9N8TxPJmNzV9MbqDok7ms-HPbLLfzd66dvlwigndROc_0EwKlM9yJJDzQh82GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#USOIL — H4  پوزیشن پیشنهادی.  ریوارد به ریسک خوبی دارد.</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/SBoxxx/21116" target="_blank">📅 00:07 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21115">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">تایید دیدار عراقچی و ویتکاف
صداوسیما:
با اصرار نماینده آمریکا دیدار آقای عراقچی با ویتکاف در حاشیه مجمع عمومی برگزار شد
ابلاغ شروط ایران برای بازگشایی تنگه هرمز دلیل پذیرش درخواست ویتکاف برای این دیدار بوده است.
رفع فوری محاصره دریایی، پرداخت فوری همه اموال مسدود شده ایران و پایان جنگ در همه جبهه های مقاومت از جمله شروط ایران برای بازگشایی تنگه هرمز است.</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/SBoxxx/21115" target="_blank">📅 23:04 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21114">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/big8tbY5e-psGLjEkR5impLXyVH_-ASHOUxfgzqaVHCQNBU0tnYnDweyXRxguorQU7AvP7_zTSJXfey8BvHzBbfXWQnBTGWnYHIsUYPE24Kj5i_VG5CpgwhrXrhIB3O8ceD_7X3Bvf_EX7Ue99wNwNNpCm_A2DE78HciBZvSIMeUPBG0Kfsn64qHlmHvoD6RIzP-FBIUnGbVsT7r6btWqY-B7RZmCZcQy4jIVbcKCEX8S_VyNH-B76-alavQZ0HyL-5JYtLKhRysRWhCevJq8gDOwnoNmlv2Am_oNfCF6rbfTlBvKzMbW-s7n5QsaUs1r3hrohz-zsL8M76LLJUZhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشنهاد بز برای پاسخ به کشورهای همسایه که در محاصره ایران نقش دارند</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/SBoxxx/21114" target="_blank">📅 22:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21113">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ادعاى ترامپ:   ایران در حال مذاکره با ماست؛ روابط با ایران در حال توسعه است.</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SBoxxx/21113" target="_blank">📅 22:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21112">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06862e3345.mp4?token=CXPRNZoVyyZFHCp8wriXWAWS7lm8QYBsmw0SsLTwgxIXcc-05X4h6IchZi-heqCiK4JXi3_qXGl3lB6Tuq8mKsl2tC4-J_e6gTMEEH_lzE3Cga1xD-5zXAz1wJjGByT8jUq5Ni78NxbYd9x-nf2Rkc1zQ0aG1pHzKcRrlDVR6lUT3-w4WDUCuxFXPoT92OWyp2Ejy-EskEd-xmV6e7dMtU6-UpXOUEtcw8uuYCHRLjrq3G-cTUV6nggoxvSa2Z2tNCSL93PBKaNuIG-BwER9kjh6R4vfxg5eIvrKqSmCmCnVfNqk2rzkWj5j-c4ZStrraNRNOuXcatvYojD9NxYLU2JsFknKU4TkohPgs1cjpdaIyKIRd2bzD1tpbgxOU9p4q6nI1TzEY_t2P6PMCekjc9NGFxs8uwxiDQChoM-OLGkJ_Tb6zpxuAxddhkAkd4DIR5TluMFe6Blol1b-OwVVgLF25UVTYPr8O5PM-xC1VKSTTpKc5B4lrQYQX550qzt_qUr-YMzM3VSI01Ml63jTb1cDhzJFq3g-0m1cRXc2k49-Hb5KRWwc_KA_YXwlPJ6ABPMYJ7xFb2pnSwT9fuKd-40jYAPlY0a_zi2gg0TDsh9J34Vnj3R9COPlZlDYKgCzIx2GTeE4vQtQjaBZq-ncuX__LmYPfxTC-eADIHbx3SI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06862e3345.mp4?token=CXPRNZoVyyZFHCp8wriXWAWS7lm8QYBsmw0SsLTwgxIXcc-05X4h6IchZi-heqCiK4JXi3_qXGl3lB6Tuq8mKsl2tC4-J_e6gTMEEH_lzE3Cga1xD-5zXAz1wJjGByT8jUq5Ni78NxbYd9x-nf2Rkc1zQ0aG1pHzKcRrlDVR6lUT3-w4WDUCuxFXPoT92OWyp2Ejy-EskEd-xmV6e7dMtU6-UpXOUEtcw8uuYCHRLjrq3G-cTUV6nggoxvSa2Z2tNCSL93PBKaNuIG-BwER9kjh6R4vfxg5eIvrKqSmCmCnVfNqk2rzkWj5j-c4ZStrraNRNOuXcatvYojD9NxYLU2JsFknKU4TkohPgs1cjpdaIyKIRd2bzD1tpbgxOU9p4q6nI1TzEY_t2P6PMCekjc9NGFxs8uwxiDQChoM-OLGkJ_Tb6zpxuAxddhkAkd4DIR5TluMFe6Blol1b-OwVVgLF25UVTYPr8O5PM-xC1VKSTTpKc5B4lrQYQX550qzt_qUr-YMzM3VSI01Ml63jTb1cDhzJFq3g-0m1cRXc2k49-Hb5KRWwc_KA_YXwlPJ6ABPMYJ7xFb2pnSwT9fuKd-40jYAPlY0a_zi2gg0TDsh9J34Vnj3R9COPlZlDYKgCzIx2GTeE4vQtQjaBZq-ncuX__LmYPfxTC-eADIHbx3SI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روند ساخت اسلحه های دورزن در یمن!
با همین تفنگ های دورزن، حوثی ها صدها نیروی مخالف خود را در هفته های اخیر کشته اند!
ثانیه 29 جالب است. یارو در دهانش قات می جوود اما دارد اسلحه دقیق زن هم می سازد!</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/SBoxxx/21112" target="_blank">📅 22:20 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21111">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">خاویر میلی، رئیس جمهور آرژانتین:  نسیم‌های تغییر به نفع ادعای ما در سراسر جهان در حال وزیدن است.  اخیراً، رئیس جمهور ترامپ اعلام کرد که ایالات متحده در حال ارزیابی مجدد موضع تاریخی خود در مورد جزایر مالویناس (فالکلند) است.  ایالات متحده در حال بررسی این تغییر…</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/21111" target="_blank">📅 21:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21110">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ffb8ac635.mp4?token=Uk8K-huiIWR22pf_eclml21CbvgJCP8bfV46RY_kDGgc68w-bJccl6oIXlOmrFLlpvjzTun6CvPPka2EEe8zhfvCaYtmjfthk80HKWonTUTtgnbGWx9YYLRqRaPJdB4CY8zvQxg4lJD_6QRy29W65LqP1ZDkeZ5pxJb7ZlLConHGRORrZzQUrxypjTxdx87ZSz1tg_zw1rSwi6asTFbovOGihGVVcDuxr3SW1-cQPAhzkx6RxKfUuQ0UR9ZGaPOG3LUrhOrfeglfwjt7XOs88zKTm2CrL2ww_eXj6X3xQ5m3WpyEfXKo1_3mQs9hIWb4ZaMXdIx9D4H6_yO0o3CcWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ffb8ac635.mp4?token=Uk8K-huiIWR22pf_eclml21CbvgJCP8bfV46RY_kDGgc68w-bJccl6oIXlOmrFLlpvjzTun6CvPPka2EEe8zhfvCaYtmjfthk80HKWonTUTtgnbGWx9YYLRqRaPJdB4CY8zvQxg4lJD_6QRy29W65LqP1ZDkeZ5pxJb7ZlLConHGRORrZzQUrxypjTxdx87ZSz1tg_zw1rSwi6asTFbovOGihGVVcDuxr3SW1-cQPAhzkx6RxKfUuQ0UR9ZGaPOG3LUrhOrfeglfwjt7XOs88zKTm2CrL2ww_eXj6X3xQ5m3WpyEfXKo1_3mQs9hIWb4ZaMXdIx9D4H6_yO0o3CcWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رجب طیب اردوغان، رئیس‌جمهور ترکیه:  باید برابری حاکمیتی و جایگاه بین‌المللی برابرِ مردم ترک‌تبار قبرس به رسمیت شناخته شود و به انزوای غیرانسانی که بر آن‌ها تحمیل شده است، سرانجام پایان داده شود.  از جامعه جهانی می‌خواهم که «جمهوری ترک قبرس شمالی» را به رسمیت…</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SBoxxx/21110" target="_blank">📅 20:56 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21109">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">گویا اعراب به دنبال فراهم کردن شرایط دیدار حضوری پزشکیان با قاتل امام شهید هستند.</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/21109" target="_blank">📅 20:31 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21108">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">آکسیوس:   تا ساعاتی دیگر جلسه‌ای بسیار مهم و سرنوشت ساز در نیویورک میان ترامپ و سران کشور های عربی خلیج فارس در مورد ادامه جنگ با ایران برگزار خواهد شد</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/21108" target="_blank">📅 20:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21107">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">آکسیوس:
تا ساعاتی دیگر جلسه‌ای بسیار مهم و سرنوشت ساز در نیویورک میان ترامپ و سران کشور های عربی خلیج فارس در مورد ادامه جنگ با ایران برگزار خواهد شد</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SBoxxx/21107" target="_blank">📅 20:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21106">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">رجب طیب اردوغان، رئیس‌جمهور ترکیه:
باید برابری حاکمیتی و جایگاه بین‌المللی برابرِ مردم ترک‌تبار قبرس به رسمیت شناخته شود و به انزوای غیرانسانی که بر آن‌ها تحمیل شده است، سرانجام پایان داده شود.
از جامعه جهانی می‌خواهم که «جمهوری ترک قبرس شمالی» را به رسمیت بشناسد و روابط سیاسی، دیپلماتیک و اقتصادی با آن برقرار کند.</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/21106" target="_blank">📅 19:37 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21105">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">صحبت های ترامپ درباره ایران !  یا توافق می‌کنند یا جوری جمهوری اسلامی را نابود کرده و آنها را میکشم که نتوانند به هیچ مردم یا کشوری آسیب بزنند</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/21105" target="_blank">📅 19:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21104">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64adfd4dd3.mp4?token=MoOgE1rFeCbRuwGWmRstMcxmBhoEXy_lg7wIoYOaKQBg6dIvRwkidWM__KtEWUQmu6GRV3pzdrWTkJrC9WJTTtPXqmCEER5phAkHgpqF-9V_U2tiFrUFWR-Bl1o1WFjiPEClxWD8z5mFi3LQ0uyK5fcVx1P-QMK3NymbBP5zRLLzEMKjwr2haEJH9rEp9D-ojHQXN5HgtZ32QkG_jDo5yKY5eg7rAaJ4Zxq7WNElep4psf6Qsd6Lh8a41l-qv9gYwNAqdPZBEWOn7V735KCRO9zrTGVeAiMaDtMpV0IbToa1vitmv0PiCV4sJXvc0GxPtpLUT9os8cdLcOj1oXbnnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64adfd4dd3.mp4?token=MoOgE1rFeCbRuwGWmRstMcxmBhoEXy_lg7wIoYOaKQBg6dIvRwkidWM__KtEWUQmu6GRV3pzdrWTkJrC9WJTTtPXqmCEER5phAkHgpqF-9V_U2tiFrUFWR-Bl1o1WFjiPEClxWD8z5mFi3LQ0uyK5fcVx1P-QMK3NymbBP5zRLLzEMKjwr2haEJH9rEp9D-ojHQXN5HgtZ32QkG_jDo5yKY5eg7rAaJ4Zxq7WNElep4psf6Qsd6Lh8a41l-qv9gYwNAqdPZBEWOn7V735KCRO9zrTGVeAiMaDtMpV0IbToa1vitmv0PiCV4sJXvc0GxPtpLUT9os8cdLcOj1oXbnnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت های ترامپ درباره ایران !
یا توافق می‌کنند یا جوری جمهوری اسلامی را نابود کرده و آنها را میکشم که نتوانند به هیچ مردم یا کشوری آسیب بزنند</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/21104" target="_blank">📅 19:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21103">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ترامپ:
در ۱۲ ماه گذشته ۱.۵ تریلیون دلار در ارتش ایالات متحده سرمایه‌گذاری شد.</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/21103" target="_blank">📅 18:05 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21102">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">یک مقام عراقی به الجزیره:
«به فرودگاه‌های عراقی اکنون دستور داده شده‌ است از فرود هواپیماهای ایرانی، از نیمه‌شب امشب، جلوگیری کنند.
اقدامات انجام‌شده علیه هواپیماهای ایرانی مطابق با تحریم‌های ایالات متحده است».</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/21102" target="_blank">📅 17:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21101">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ولی من هر چه میشمرم، رفع محاصره یک شرط است نه ۷ شرط !</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/21101" target="_blank">📅 15:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21100">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">— مارکو روبیو، وزیر امور خارجه ایالات متحده:
«ترامپ آمادگی دیدار با پزشکیان را دارد، اما باید بدانیم که تصمیم‌گیرنده نهایی در ایران رهبر معظم است و او یک روحانی شیعه افراطی است».</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/21100" target="_blank">📅 15:56 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21099">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">به نظر من نوعی کرنش در برابر چین از سمت ایران است که نشان بدهد برای حرف چینی ها تره خورد می کند. چین روابط مستحکمی با سعودی دارد و همین چند روز پیش هم مشخص شد موشک های بالستیک DF-21 در اختیار سعودی قرار داده که با آنها یمن را می زند.  در آستانه دیدار رهبر…</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/21099" target="_blank">📅 14:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21098">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">سخنگوی سپاه:   اگر مصلحت ملی ما ایجاب کند که در کنار جنگ، مذاکراتی انجام دهیم، باید مذاکره کنیم</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/21098" target="_blank">📅 14:51 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21097">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - Podcast 28</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/21097" target="_blank">📅 14:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21096">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - Podcast 28</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/21096" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 28
سه شنبه 22 سپتامبر  2026</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/SBoxxx/21096" target="_blank">📅 13:56 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21095">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">— شرکت هواپیمایی ترکیش ایرلاینز، به همراه پگاسوس و ای‌جت، از ۲۱ سپتامبر تمام پروازهای خود به ایران را لغو کرده و حداقل تا مارس ۲۰۲۷ هیچ رزرو بلیطی در دسترس نیست.
تحریم‌های «عملیات سرد اقتصادی» ایالات متحده آنقدر گسترده است که حتی هواپیماهای ایرباس حاوی قطعات ساخت آمریکا را نیز شامل می‌شود و برای شرکت‌های هواپیمایی ترکیه چاره‌ای باقی نمی‌گذارد.
شرکت هواپیمایی ایرانی ماهان ایر نیز پروازهای خود به استانبول و آنکارا را به حالت تعلیق درآورده است.
اسکات بسنت، وزیر خزانه‌داری ایالات متحده، گفت که خطوط هوایی ایران از ۲۳ سپتامبر با تعطیلی جهانی مواجه خواهند شد و هشدار داد که شرکت‌هایی که به آنها خدمات ارائه می‌دهند، ممکن است در معرض خطر از دست دادن دسترسی به سیستم دلار آمریکا قرار گیرند.
ترکیه یکی از آخرین مسیرهای هوایی بین‌المللی مهم موجود برای ایرانیان بود.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/21095" target="_blank">📅 13:41 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21094">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ولی من هر چه میشمرم، رفع محاصره یک شرط است نه ۷ شرط !</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/21094" target="_blank">📅 12:54 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21093">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4lLWAk5pN7nwm794q6FbtOJMnbzmLJZXsVuO9lnEmkIvE3u3bLIq09yVRqY2gFF5TBn2aKk6WQSZruPgSGCO6xeo6Wx0SUnLByBjNPU6aYgkjlYIq34stdF_5pgosSkHCRjuNk3F3PXP4e_ph_ybFSTCyGUEEuMAaj6N0CWpTuTsYsegvEscEdwoK5NuleNpPclH2mIpj5lIYfWA8LGQ9d1jsXRGYf1F8sT_GBUSEpOF7uTcbTZcyRmHB1RaA6TMIXmQJTRTSMlYUCFpnAvSZ_lB34KM0SYF6QtmZ9eRKvioX3uXwGGWlv4PLUk7rzhd1eCUOjDKPpXCDMsPTpc8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران می‌گوید تنگه هرمز را مشروط به رفع محاصره ظرف ۷ روز بازگشایی می کند.</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/21093" target="_blank">📅 12:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21092">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n8w8Tt5BJDSYpqlcIJZDB3ditR3_ZXvGaAskUEuOMS2YKiNaOkQGifGEyVW-FFXyuZARdfBEQRCCgRzjfmm3VuINuEPzE_Iw8SrKgvdmNPMP__cvLbonptJccrr7_ByYAtTLeVx6RtROstvfPAJAwOXARxLf537ohEgo0Kb_Hx1RYXeLt1q-uRNOoDGl3F8ahx0MT2xxI4nuB1ntB1qKYoj73z0W72PqoUwhqSWV_OuH8LntdkaWjaYhA6OmYdjSw3ivlIT4mZ1PWjqKIvc-Cx-LkLmRqxMd_HH_rY6tP8lPzdRpxED763uzvwUVVR862Rgf6rO4xA9wKK0FtZQcdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سه کله پوک پیمان مکه کم بودند، حالا وزیرخارجه مصر فقیر (خر دوم از راست) را هم با آن ریخت و ترکیب ش add to group  کردند!
فقط سیس هاکون فیدان !</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/21092" target="_blank">📅 12:41 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21091">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dfbmBs0LgNwZzM2-bpVOS6vLh_Qd_OBUc1XNlof1ez5T5B_JpXwZG81nmhxlXgF4Z3SPMjcYGzl5IGQHHGdU4mLQi1JP2kfGOhZavd-MYPnlFD5S7ic6axzGXEizj0rHAgj8tAjFbMPDq0d8FJvZsQwGqU1cyypAVDN4-thu66rjjN--9o7ymBA7V2S_7zoe5k2Wwv-Mrem5kReBUm__zWj1Q6kix_tIjLQx3FbfOrIIL_-X1m7xlcyIZAhxBUdRnYkaRIQ_DP0xwJt_nGpfyen5FWPbU5uunnpFAIekggxpJ_t93us5rj__TDfoCRGL_vHX6rkU_1l_nEAzyzF2YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve  نمایه FVC کماکان زیر محدوده منصفانه است و هر چه افت طلا بیشتر بشود برای خرید ارزنده تر خواهدشد.</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/21091" target="_blank">📅 12:36 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21090">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">به نظر من نوعی کرنش در برابر چین از سمت ایران است که نشان بدهد برای حرف چینی ها تره خورد می کند. چین روابط مستحکمی با سعودی دارد و همین چند روز پیش هم مشخص شد موشک های بالستیک DF-21 در اختیار سعودی قرار داده که با آنها یمن را می زند.  در آستانه دیدار رهبر…</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/21090" target="_blank">📅 12:33 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21089">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">چارت نفت جوری است که به نظر یک کاهش تنش داشته باشیم و دیدار شی-ترامپ مثبت باشد.</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/21089" target="_blank">📅 12:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21088">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ایران می‌گوید تنگه هرمز را مشروط به رفع محاصره ظرف ۷ روز بازگشایی می کند.</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/21088" target="_blank">📅 12:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21087">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ترامپ می‌گوید توافق با دانمارک، «کنترل دائمی» ایالات متحده را بر امنیت گرینلند تضمین می‌کند  ترامپ می‌گوید توافق گرینلند، رقیبان ایالات متحده را از ایجاد پایگاه‌های نظامی در آنجا منع می‌کند</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/21087" target="_blank">📅 12:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21086">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SYinTfyKuDi_9aPn7wKa0PEBR3cV2jEu-wyGXnnYbjklI_0jzgxyPLL5loHRZuEasBo-rZKCVUfmjk1AlRsoBOcwPY8XKbUBhvGjPmxOC6v6dF19z0xXE7wl7PDXwEPFs24C42_xUQCeoYSXiS_x0LbcRDynnn-Gjpmk3mKcNp5ldR755vGdeOiVKOtZj7bLUTpjs-6AEQ6Zbx56q9Ymfefjxw9GaeUPqgE90LVTjIQ-rwOgxN6zdIWtEFlDER9lWboaXQBvBwphU3XzZkklqm2rx0HuKyr3mfj5-hTlecES0bpH5izjpgD38qiO3jXOVIZxenkZQ19qGHlW2gO47A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC کماکان زیر محدوده منصفانه است و هر چه افت طلا بیشتر بشود برای خرید ارزنده تر خواهدشد.</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/21086" target="_blank">📅 11:12 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21085">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IsvDG8XbUE1LdEgztfj_gJu0uyKSxdMdMYP3scmGJlhvsdsmZtewojZrt4M802ttofoOqQW88Re-rMjQVtAt8eH4DXGYQOF1vuGtew1QBsYKdTFzmCiGM7QTPqiRNsXjsKNeLxu59dxZcf4ivzG5vtXzhypT7aqMxNgIhTKUUWGDsep2Eps1hVWCwrCkQN4Hf58bdNRdUbQ7NVKEh-KMASKlGOc1T1azfEZ-HbOYF8uBhJNDUt1LQbehg-cAbERSXAlSOMHz2UZQiJ9iGAcWIlaJnqAqEWvSQtuyPcbeST8ykRFf4nTNj7PF1SEODTp8YoLHruC2QFVy8VyToUMbFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح بسیار بالایی است. اما نظر به ریزش سنگین طلا، اثرگذاری اش را گذاشته است.</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/21085" target="_blank">📅 11:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21084">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxb1Ed9I7_YmHeT9Jtnf3ATRX0tTCttvdEkUC0FGkoj6Y6lgIPXlgg1wIYWJh21E_9EFQXPoaHEBmky4P5EAglrY9YEuyvkbwgPBn-49rt4k8R61o9yJKYEHMH80dYnZuyQ7y6gwV6TLGMeHJ2X-gqrnx4uLOSAHz8trz9rG33-U5AUSAhCu90HcG3L03Wd0E55Y98gJjR0Bjqp1wkCw4tLPjlOh4bmic33PzyCqRQDkN2xpVKW9xXbn13rIYffyWJ0LxtZzPsAV0f0yHCF2hDbILdyT0ikdpCWbLFCqB0S_w29n5x1AaHKjBPrdDUeSSdisaXMbxKus4q_CZCDkdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک پله خرید طلا توصیه می شود.</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/21084" target="_blank">📅 11:08 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21083">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">کاخ سفید، پخش ۲۴ ساعته‌ی «کانال تلویزیونی ترامپ» را آغاز کرد
!
کاخ سفید، پخش مستمر
«کانال تلویزیونی ترامپ»
را از طریق یوتیوب و پلتفرم X (توییتر سابق) آغاز کرده است و وعده داده که سخنرانی‌ها، اطلاعیه‌ها و مهم‌ترین بخش‌های فعالیت‌های دولت را به صورت "به‌روزرسانی لحظه‌ای" ارائه خواهد داد.
کاخ سفید در پلتفرم X (توییتر سابق) اعلام کرد: "شاید همه لحظات مهم در تلویزیون شما پخش نشده باشد، اما اکنون این امکان وجود دارد."
کانال یوتیوب، این پخش را به عنوان
«پایگاه اصلی»
معرفی می‌کند و وعده می‌دهد که مهم‌ترین لحظات و بخش‌های برجسته دولت ترامپ را به صورت ۲۴ ساعته ارائه دهد.</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/21083" target="_blank">📅 11:03 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21082">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sp_Em6Iv1JfECJAMUVSuhdgxdJQvKlzz2ugl3du_2La1W7Y73w0csBirII1rNG5ajEZgU3CzMmmXobEOlDm9IrTuAP4-he5LER1D-QJy9fcV-V_uVMl_w8t9Ub5xU5JKijopTwJhqNruvfe4u8gjxaJQPV_E2bOJ5UGrwd5Jx7VrX94fMm6z4JZ8DLeJLuumAv7LnrpSoMu9QWsHkmJ0XLoghYjUYRPSFgdSdznlxHXrMqH_IlNKlSNJbK38kqM0PVz37mEpSGtmW81oNkjYWYbX7O82uBF8Uu1-_traBzo-MnQLgaSbA-CafWDkwU2oBbIeVqmM2wsKgzWpoHQ5BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح میانه ای قرار دارد و با توجه به افت بهای طلا، به احتمال زیاد دوباره حمله به سقف جمعه و حتی فراتر رفتن از آن را خواهیم داشت (یعنی بالای 4400)</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/21082" target="_blank">📅 10:08 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21081">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JS14if3DG4DOauBQ2IztQm7tOyfuPydwuSqqjKqFdQqlA0ECkP4jHwcAp7ZFD045x2NsrIKgRazDaktePncqR1KGjlbn3GQsCrwp9zw3PwjQIrftArLNl16I8bKUHzUG9EXh8SStLCdYpB9a-c5ot9EBQ95XzZHzu9CfZLvT8Pmsbv1hWxIF__xN-DYfxakhODyQW3KIn7VnEMsuXXCFBhZ_Io6Sw-KubMsVvxxOa-ES8llpRREyFuar-L3kGd_LoHgzbO-GRa9lAE9F-XhkNnywiLLKI3TnEEmCfqJS4JalRj6NSvCxoVLpn1ZDWOhhni4fjHrbqhctv5x7ob0wRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمونه ای از جامعه ای سرشار از زور و ریا!
حجاب اجباری بر سر دختر می کنیم تا در بلوغ و بزرگی محجبه باشد اما همین الان مادرش بدون حجاب است!</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/21081" target="_blank">📅 09:50 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21080">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">رئیس‌جمهور ترکیه، اردوغان:
ما آماده‌ایم همکاری‌هایی را که با ایالات متحده در حوزه‌هایی از جمله انرژی هسته‌ای و LNG، حمل‌ونقل هوایی مدنی و فناوری‌های پیشرفته برقرار کرده‌ایم، گسترش دهیم.
توسعه بیشتر صنعت دفاعی — که به‌طور سنتی یکی از قوی‌ترین حوزه‌های مشارکت ما بوده است — هم به‌صورت دوجانبه و هم در چارچوب ناتو ضروری است.
ما می‌خواهیم موانعی را که هرگز نباید بین دو متحد وجود داشته باشد، پشت سر بگذاریم و شتاب تازه‌ای ایجاد کنیم.</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/21080" target="_blank">📅 07:51 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21079">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CvAjKf4uMYEdmdzNGeV0U3ZMeEjgfH9ChpXpKPiryfSNcnNkCigwlzoC14V-fJIx4xXdSPvw6zizPha2AsNdLkUWhK3W_BwN3Rth3rRWygaHJ8w_XneS1kdIxPzAWDZ2By5wUGslDnx6AejUOuxvvy2-kOF-EFNwiGsijJGnLKKMxgNgXiR0jFBlFT3xEae9wsDWJaPI-4_JvvpB6BBYrOtqxFkQQmFLAHDTlSxf-MiyImI0eFYyHS6FEw-ev315Mjzk4aJzhOHyDgj1YCGO0XzMuNlvNqUwKahjpKX3_JBZ57yETnK2QVsBUSho0YE5MkCMzcDVl2ZxoQPluDQTgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
دلار، نفت و موقعیت های معاملاتی گرید از دید موسسه Danske
موسسه Danske با توجه به رشد اقتصاد آمریکا، سیاست انقباضی فدرال رزرو و اثر شوک نفتی، تداوم قدرت دلار و فشار بر یورو و پوند را پیش‌بینی می‌کند.
در بخش معاملات گرید،
GBP/JPY
به‌عنوان یکی از سناریوهای نزولی مطرح شده و ترکیب تحلیل بنیادی و تکنیکالی، افت قیمت تا محدوده 181 را مورد توجه قرار می‌دهد.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/21079" target="_blank">📅 00:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21078">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">— ضرب الاجل دولت عراق برای خلع سلاح حشدالشعبی</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/21078" target="_blank">📅 00:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21077">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">هند نیز‌ به محاصره هوایی آمریکا علیه ایران پیوست؛ گزارش ها از توقف پرواز ها میان ایران و هند!</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/21077" target="_blank">📅 00:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21076">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">هند نیز‌ به محاصره هوایی آمریکا علیه ایران پیوست؛ گزارش ها از توقف پرواز ها میان ایران و هند!</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SBoxxx/21076" target="_blank">📅 22:07 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21075">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DiAuG4mbYCcaPQ9G483xqemqc-D6nL2G_spPDfrc77eOZm-kd6F6AU0U2lTQJPhX86SDJc1_IU54WugyV5Cjz7E7Ob9bOkvofdlESqjYFynyLxC0JRCLgNZUZ5dDiZOr13K7JhpF1cNnaoZd70XL9LMgVIsoIl9Bbm3DocZK-8mLCUSVa3cCehOAjRTkyv3JGEL4yQuDJB2V_v4UMi11R2r9Forj6TWkmH50e-NnFqaoJBDXdFnW9bfz5u-Dd4APH_w_OLmIbAfC5VERDumi-_kfHPC7U0t16JAigZ3gaNcI4INqmkYTySihC6EYsUtCUsEe6AOO9_ofgwy9lHUXgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام وضعیت !  فکر کنید پزشکیان بتواند آن ماموت ۱۵۰ کیلویی را با دستانش خفه کند!  اینها شده اند نخبگان ما!</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SBoxxx/21075" target="_blank">📅 20:08 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21074">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">رئیس خزانه‌داری ایالات متحده می‌گوید تمام خطوط هوایی ایران در ۲۳ سپتامبر «بسته» خواهند شد</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/21074" target="_blank">📅 19:52 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21073">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O5hTFHccTLfvlVR_a2EnnmmUwyhhPuH5A0riX0nAcNeAEj718daJ5WHgMrigzvJgrqVpd5lNrmQKDn6AyT-aPTH5j4FvLKYHm17BwqrDoBR0rGtS4nIJ933o4Ajuer8yVLv-kM7Eq0g8wQNNK986U2SEV2QY0vNKda1dqFsSqSvAgXXZWokzNxCSa0vZWg1lKPqH21qtA5lE3UV4QBTZwz0UYUEl2QI57h901K9mGt_hPnCbIvyxieFV4HtEhcLHVFOVV9NNkhDKCaX1BZvTBBVUaaCdWzq4E0K8Jn_lh23RQs6zgKTU4R_vPNVtrPr1bGVC0SCF0Ei7LlDzg3axFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام وضعیت !
فکر کنید پزشکیان بتواند آن ماموت ۱۵۰ کیلویی را با دستانش خفه کند!
اینها شده اند نخبگان ما!</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SBoxxx/21073" target="_blank">📅 19:20 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21072">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">اظهارات جِی. دی. ونس درباره قیمت بالای بنزین:
به نظر من، همه ما باید این واقعیت را بپذیریم که تا زمانی که ایران در تلاش برای ایجاد وحشت در حمل و نقل بین‌المللی است، ما طبیعتاً تلاش خواهیم کرد تا در برابر این اقدام مقاومت کنیم. اما به همین دلیل است که قیمت بنزین اینقدر بالاست.</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/21072" target="_blank">📅 18:26 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21071">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vjeYcG3NQ77tISdHaoGuWmcN2-9M8sgD6OwqILkahjTdwQeTS7D2N00TO_oPi3cMFwpUTtFRWxUOBikmbC1bv_9JQDz-zoH0V3echyPPqCkmpNhRVBLNP4YX0LtGZ5kYbNXniwRhaznORHNWMllTs3OPhqooFovFzyQqtYN_T2SgZ8YiQN9Hl-TOlDFWY-fAtRsucyInrRwT7bL-dd_mU6HHBnTuYYb47h2WGpi4YTUylSIUZx3DoihNyYHa0ig6hmNDZhnxNCWGDKKzARjQBjUe3R8Oj8UofTwYUt4BYV79bfNuSZzq48J4FBNxsxSxgerCPkTmZwtOS21mGRVsZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/21071" target="_blank">📅 17:51 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21070">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">درگیری های سنگین میان نیروی انتظامی با جیش العدل در سراوان</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/21070" target="_blank">📅 17:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21069">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">رئیس خزانه‌داری ایالات متحده می‌گوید تمام خطوط هوایی ایران در ۲۳ سپتامبر «بسته» خواهند شد</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/21069" target="_blank">📅 17:08 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21068">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">جان کیریاکو، تحلیلگر سابق سیا:
اسرائیل هزاران افغان را در ایران با ۱۰۰ دلار برای جاسوسی به خدمت گرفت.
کار اسراییلی ها اینطوری بود:
«در این گوشه بایستید و هر بار که این ژنرال را در حال رانندگی دیدید، یادداشت کنید و برای ما بفرستید.» بفرمایید صد دلار.
اسرائیل هزاران نفر از این افراد را استخدام کرد.</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SBoxxx/21068" target="_blank">📅 13:20 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21067">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RXiPNvCrJJyO3KBFoNfRik9NCX2HpoGA6Cqm1rXNtsM10CKiMPTDRNHOiTsz_7jA3FvhzGUgTyCpWUYD0zHQZaPSuIhyZBKc2pTT27fKbXsH2vpqCKV2z95VMNks70RxlqPNz-Ljudvyk29JoFHIq5ut4SDnRc2vfjpCsisYFNjAO9Qkxc0QMcZz8noO4W1ZlEdoYYxbdu3sRczqq2dRzvIUFlPL17f4DFt-zqijPb9eBME46CvkH9bmyzWLtzws7pZcQqT5hwm7HpkOx48i2fSA1xtaM6cW-tYa_-V0s5qS4N1MMeZy9skRKS7r-_GG_vA_koUgcvTydUKSmzkR6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC در محدوده زیر قیمت منصفانه قرار دارد و لذا فضا برای یک رشد در طلا هموار است.</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/21067" target="_blank">📅 11:52 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21066">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfQRHpTZPVz41Um1pE-aqWp_LxN_VMUHUUIK4OamYA6aRI0Yg_Nz6NoEOrWSNOX5cvFClNCow_cAz-eig4H31Lp7tAKoLK0EKju1L3ocgTdfp0rEsa7GrzhqZ2KAnUqui0ITpZo2cM1bqat0pV00WVxfikIvCY_0jLIoWS9v5qad2waoQMx4nJ5bq0F277DkQtxReMQdrzQNQHyUv3AtBnGhjXW6wfyMJJZUqWjPSWvR6ohOzA8MHA5eHAWmUfPQWeHODOwMfHoTVycVrPM4bERUQNj_YvPNU5Q6d4RwSYv63A6bDO1yY0L9AOZow25vMUcbw6JsRhibl4F0x25hSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح میانه ای قرار دارد و با توجه به افت بهای طلا، به احتمال زیاد دوباره حمله به سقف جمعه و حتی فراتر رفتن از آن را خواهیم داشت (یعنی بالای 4400)</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/21066" target="_blank">📅 11:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21065">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">قیمت متوسط گازوییل در آمریکا برای اولین بار از
۶.۵۰ دلار به ازای هر گالن
گذشت. از ژانویه ۲۰۲۶، سطح عمومی قیمت‌ها (موزون با شاخص بهای مصرف‌کننده)
۴.۸ درصد
افزایش یافته، در حالی که قیمت سوخت خودروها
۱۷ درصد
رشد کرده است؛ این امر احساس بحران توان مالی را تقویت می‌کند. دونالد ترامپ، رئیس‌جمهور آمریکا، تمایل خود را برای دیدار با سید پیش‌وا (پزشکیان)، رئیس‌جمهور ایران، اعلام کرد. با این حال، گفتمان طرفین همچنان منفی است. توافق آمریکا با دانمارک درباره گرینلند می‌تواند گامی مثبت باشد (بازبینی یک توافق موجود می‌تواند یک سابقة مفید باشد)، اما عدم اعتماد بین آمریکا و ایران اوضاع را پیچیده‌تر می‌کند.
مِرتس، صدراعظم آلمان، پس از باخت در انتخابات منطقه‌ای هفته گذشته به چپ رادیکال و راست افراطی، سوگند یاد کرد که در سمت خود بماند. به صورت ساده‌انگارانه، نگرانی‌های اقتصادی به نفع چپ رادیکال و نگرانی‌های اجتماعی به نفع راست افراطی است، و روند جهانی به سوی قطب‌بندی سیاسی پیش می‌رود.</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/21065" target="_blank">📅 11:48 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21064">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v0649Zq9IwetTKObkrRjjZHqubhj2D-b0kZsYmBq6IZtwLABArHZYkPeUAEWLv12EtTYSPH15BWVLArVUO8viljteXVSWYlp0Ssx3Wo-m5vznLhEiu_qw7N_j2sdAaExin_xVllGpR6mwnGlHTbWaVYhdaQdluoYjZgAr25XVSNJuzCvWmWgL_g1TVLkasJn9XJJDP5dMCs3LDw62FF0mh2-ugLcObe02gY8j2h_zQL_46NT3yYf45Sh8aCJRvRDfmgfVH9lV2HfDGsEORi5rURlRx9Uomt13oSGyAV418x0QyMoLIT6DlactL7BmYto4aglWayspocltdqMljDsTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چین میزان اوراق خزانه‌داری آمریکا را به پایین‌ترین سطح در 18 سال اخیر کاهش داد.
چین بیش از یک دهه است که میزان دارایی‌های خود را کاهش می‌دهد. این میزان از حدود 1.3 تریلیون دلار در اوایل دهه 2010 به 618 میلیارد دلار در حال حاضر کاهش یافته است.
این کاهش پس از سال 2022 تسریع شد، زیرا چین نگران وابستگی بیش از حد به دارایی‌های آمریکایی شد.
دولت‌های خارجی، خرید اوراق خزانه‌داری آمریکا را کاهش داده‌اند، در حالی که صندوق‌های تامینی و سایر سرمایه‌گذاران، خرید این اوراق را افزایش داده‌اند.
کاهش تقاضای خارجی، به افزایش نرخ بهره اوراق خزانه‌داری کمک می‌کند. نرخ بهره اوراق 30 ساله اخیراً به بالاترین سطح در حدود 20 سال گذشته رسیده است. افزایش نرخ بهره به این معناست که دولت ایالات متحده برای استقراض پول، باید مبلغ بیشتری پرداخت کند.</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/21064" target="_blank">📅 10:37 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21063">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ملونی ممنوعیت پوشیدن بورقا و نقاب را در مدارس ایتالیا اعلام کرد
«هیچ‌کس در ایتالیا نمی‌تواند تصمیم بگیرد که یک زن جوان باید خود را پنهان کند. برابری بین مردان و زنان نه در خیابان‌های ما و نه در مدارس ما قابل مذاکره نیست»</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/21063" target="_blank">📅 10:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21062">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">اقدام بی‌سابقه دولت الزیدی:
یک “عراقیِ ارمنی‌تبار” سفیر عراق در آمریکا شد.</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/21062" target="_blank">📅 10:01 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21061">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RLnmgGmbHUp1PNLPO7_59SF1sMuWq6lNbJuIrTUkIpdI_zuU4_YyqarbEYc3zdv1VJoV49HhdZHsROaJMdpEdyZhJlaV_zVaRTPvc5ZR8nQX42wq7P4_-UtTZpYKo9B0AtuO4T4VHNYPPllGwVMngR-PVuKLnNFZh0nQ1XmZ8faywaPJtexr5tBthnyHpRIAXvRcH7tVoLd-9d1yOJEwMJ3tehWTsETgkn-Qm06ehSlJ3yp4u6-xAcgUyZ9CS7ZeuE5XtztTOZGN_nZHg3KYkTHMnsx6mfkDe1UhfbblKc6ZskuMSfaARJk2d3hcJ3We7oLEmIzGmZkmgDxuE3aRRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیده شدن یک هواگرد ناشناش در آسمان تهران امشب</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SBoxxx/21061" target="_blank">📅 01:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21060">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">یعنی همه چیز دیدیم جز قهرمانی....
هعیییی</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/21060" target="_blank">📅 01:35 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21059">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">دیده شدن یک هواگرد ناشناش در آسمان تهران امشب</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/21059" target="_blank">📅 01:34 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21058">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9e029fb89.mp4?token=UI9KQbl5nMRVD8nfs9os6azcnguZtktNcP9N_tJ9MU4pj8bXRw6ewwaZ_K2kiyqJrl6QfctTn3rWxqTroLqffiDJ99Ab5wutMKkSRr_2N9DkIXPQ6MDipoQGDkDz-KwHqvCtEKWj5v4MvvNLvp1v9Tg1R1KRtzu5UxEgI3GOMHZiM8lROgpWmNUtUUBTj50qeBTEsweoOdsnfrtKKoMT-9d--HrQYa7RIB3VuKAOaUopKVypj4xb3WPiqeUBgt9yJHWZYt00A6eb7l720pmazzlPcmdxBdB39m5_4SQuIQuylOwndnacN4JaL5JQTgM1r4zNhinvF7mFMsdsCxKXZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9e029fb89.mp4?token=UI9KQbl5nMRVD8nfs9os6azcnguZtktNcP9N_tJ9MU4pj8bXRw6ewwaZ_K2kiyqJrl6QfctTn3rWxqTroLqffiDJ99Ab5wutMKkSRr_2N9DkIXPQ6MDipoQGDkDz-KwHqvCtEKWj5v4MvvNLvp1v9Tg1R1KRtzu5UxEgI3GOMHZiM8lROgpWmNUtUUBTj50qeBTEsweoOdsnfrtKKoMT-9d--HrQYa7RIB3VuKAOaUopKVypj4xb3WPiqeUBgt9yJHWZYt00A6eb7l720pmazzlPcmdxBdB39m5_4SQuIQuylOwndnacN4JaL5JQTgM1r4zNhinvF7mFMsdsCxKXZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیده شدن یک هواگرد ناشناش در آسمان تهران امشب</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SBoxxx/21058" target="_blank">📅 01:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21057">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/304c99ed1e.mp4?token=R78r2X2K61oGnj_pb0_BDkwHTp3pLWj7p6T_pQvqvIwbcn7DHzVsdOQL4EjAX8RKG0lwcu6ZHkTBH2HIvR4iBZ7q6B6XgG2Apu9dsc2gwjTU7jY8blJq0xmxBp6XamjIO8VgTNVFGklwBr8T6hUkHKrygGxhjy-iuQwkJT7Mr8iCT48bEjCiRMkijbsH8SNQAiSSSh74cVoFw_LMiKPOlazOFIgNkHfEN0yO3HEkoolbQNUHQL4hQ-Beh2wRcBDWskSvHrMW0hNKEEhEFMwvuH4ye9E5p4J-QPqjj_zX3nvJm7X59UHcgWzTIxAVJvXID19QTxBfeUgT3VQvxfboig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/304c99ed1e.mp4?token=R78r2X2K61oGnj_pb0_BDkwHTp3pLWj7p6T_pQvqvIwbcn7DHzVsdOQL4EjAX8RKG0lwcu6ZHkTBH2HIvR4iBZ7q6B6XgG2Apu9dsc2gwjTU7jY8blJq0xmxBp6XamjIO8VgTNVFGklwBr8T6hUkHKrygGxhjy-iuQwkJT7Mr8iCT48bEjCiRMkijbsH8SNQAiSSSh74cVoFw_LMiKPOlazOFIgNkHfEN0yO3HEkoolbQNUHQL4hQ-Beh2wRcBDWskSvHrMW0hNKEEhEFMwvuH4ye9E5p4J-QPqjj_zX3nvJm7X59UHcgWzTIxAVJvXID19QTxBfeUgT3VQvxfboig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مستندی جالب از روند ساخت و امکانات شهر موشکی یزد!
بخش عمده اش به نظرم با واقعیت همخوانی دارد اما در بخش هایی از تخیل استفاده شده مثلاً بخش مربوط به نمایش طبعیت و روز و شب برای کارکنانی که 500 متر زیر زمین حضور دارند.</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/21057" target="_blank">📅 01:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21056">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/desQ-nhaEAWt_1RG4BqEzD4L6WPvAcanR0oLW8EhbIe3tNvhHAGhwmyLb2l7iUzKTcpKdFDw0pw7jf9pImgQsZ6Y0fHXBytFaUc8HFJmiuBkUnbGGMY8cgzu33DwxKZw8eaDMUB59R-R2ey9Cp36rE3y8HG2hASUIgMtvLmWGMO31oYOK-rn_b6Cf159CmKa6Auz5VmipxZeE8x7xur1gb4VvM61h_VtDoJJcm9fQgy5G6wmVuE6pAuDj7hh3izzqozuizrAHyTtu_dq0ia93AtEDi7hb78bmIEOUCvF2GwKhO3lJ8V0KNMFgNKZjDQ_rs9tsvqd7r0SsfgNHMCgsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ می‌گوید توافق با دانمارک، «کنترل دائمی» ایالات متحده را بر امنیت گرینلند تضمین می‌کند  ترامپ می‌گوید توافق گرینلند، رقیبان ایالات متحده را از ایجاد پایگاه‌های نظامی در آنجا منع می‌کند</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/21056" target="_blank">📅 01:16 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21055">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">واقعا تا حالا کسی رو ندیدم  که با این جدیت کصشر بگه
😂
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/21055" target="_blank">📅 00:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21054">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7235f04196.mp4?token=aTuVMmZ4qds0aNnmezt61m2lXUKPNjj9x2NyyPwi_q8KSK-bfFO2VSpJ_KenLF40jl1BVdULd0uRTUGYplBYnt3RuvuidALGZt-fEzWscl00zY6izYgYvzvqSttHG8nNNDvaReA7EkKTJbc53tgyg7b6RRyweB17B4xq-KAgYrJX46BrAKgMgSfKpYtYgsjQpneAeVg4etueEiGtnOWvg_bnkpKxvJ4RjL-RHPEod_f6VXBJO11cu4AuFdPjahNWGt8Q9qfzZv8MxU8Xw23lniv0AfLrqImvXUyszXxKowhY6kL6gvzdxj-IJEjp2VHRRheNMf9Og9i7KlIFF1xkgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7235f04196.mp4?token=aTuVMmZ4qds0aNnmezt61m2lXUKPNjj9x2NyyPwi_q8KSK-bfFO2VSpJ_KenLF40jl1BVdULd0uRTUGYplBYnt3RuvuidALGZt-fEzWscl00zY6izYgYvzvqSttHG8nNNDvaReA7EkKTJbc53tgyg7b6RRyweB17B4xq-KAgYrJX46BrAKgMgSfKpYtYgsjQpneAeVg4etueEiGtnOWvg_bnkpKxvJ4RjL-RHPEod_f6VXBJO11cu4AuFdPjahNWGt8Q9qfzZv8MxU8Xw23lniv0AfLrqImvXUyszXxKowhY6kL6gvzdxj-IJEjp2VHRRheNMf9Og9i7KlIFF1xkgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واقعا تا حالا کسی رو ندیدم
که با این جدیت کصشر بگه
😂
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/21054" target="_blank">📅 00:14 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21053">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kvFlye0dq5ZcgAwgq6fnRENeXVgNEdxKtiXeV_6daZY4a5cisU7O2OyxqpPzNS7dKgtHd52qwwAgmbpEe_mJqEkdk5IzW3EaRT53x9GexwjMNns3eWd9BjNYcQogjzp2DNi6rfSe_XYd-s9o3iCASxDClbdXmD1QM7HkjsmqtvDVSjiulevWFE8orFjNNfpfXTuseVNtBp13ZJKP2-dZOu3qfoPR9Mb_Nz44M4LNWp4MyUfvKT49gbDvlxZYQ_6HAJYwAfL0PMmkrriuMPXUmbx5NLMp1cvoWmzatfwRRgARaUNBUmrf5ZJsHw6jtXJuMT8Tsjhk5pAiDAe7ZLoVmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SBoxxx/21053" target="_blank">📅 23:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21052">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">چارت نفت جوری است که به نظر یک کاهش تنش داشته باشیم و دیدار شی-ترامپ مثبت باشد.</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SBoxxx/21052" target="_blank">📅 23:34 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21051">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oxKxILrtuu97SPnV4qsxkP9riqLP-_8U192bdA4rCvmsbsxUCpQSu5KnCCtgBPX1rmTcdghglF4vr3WIr2DsadskMHphWfBvs6Yio7CeKJNtmPfL4cTz5DfQurRZIAexZhmHQRnne8MeXvzJqxoXyqh3jJz0kSK-39dsBr2nJ22Wp0WTNXtDsRGKmWprilXeXypco0XCtkr3QqjSjvUbcBI-xD7Sn1VCI31H0HesjfrQSczjCN7eMnBJZB1KpBmvr31HCe6S4b4Oal-rtgjnrHIoWL37iQi3wixhG64nBZLwRV-UOxQjZJS68GJ6F1mUAorHULDxVD_YdcJuzpRS0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چارت نفت جوری است که به نظر یک کاهش تنش داشته باشیم و دیدار شی-ترامپ مثبت باشد.</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SBoxxx/21051" target="_blank">📅 23:33 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21050">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">حریم هوایی اسراییل هم بسته شد.</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SBoxxx/21050" target="_blank">📅 21:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21049">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJdccsRaqDJW4K_7GhNuvIWN_o7MZmnjari2HUy4CSqWpVgyVtQCl2C5Okph63wTnZO250ulHbIit6SiHsrJ7AlZo4-LzumoRh2T8AOt9SXWr1e27Gb75Mu8H8Y6macw56iFLSX5A-1rfI5oC7rD1q7XC-GcdEVFAeHRStwfnoGeAYc8YhG1j-gHRowiTZGRV1eYzIN2rtl5zRSR6jCzzRsZEIqVw-ksDJpoae5Ux3dJGKq8bitSZo7U93V_ZbGabSkvr-tdgYkOEdXirXMTprhbfEmWJr4NBFto_kVu_OsG7haievgYaaqpo68BHLpnOtdCwZdKA9GC33bCUdGhMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان:   صلحی که دشمن تو را به آن دعوت می‌کند، نباید دفع کرد</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/SBoxxx/21049" target="_blank">📅 19:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21048">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">قالیباف:   هم میجنگیم هم مذاکره میکنیم</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SBoxxx/21048" target="_blank">📅 19:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21047">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">📌
تخریب تقاضا در بازار نفت و انرژی های جایگزین  شوک عرضه نفت در کوتاه‌مدت قیمت‌ها را بالا می‌برد، اما تداوم قیمت‌های بالا با کاهش مصرف، افت فعالیت اقتصادی و تغییر رفتار مصرف‌کنندگان باعث «تخریب تقاضا» و کاهش فشار بر بازار می‌شود.  در بلندمدت، اختلال پایدار…</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SBoxxx/21047" target="_blank">📅 18:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21046">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SPB427GlPBIBGoYBzMSJ4sK3_VU1CBOnV5ZIe-ZAiG4UEs8pCh6bLVjxh2LoC2mhSB566gK4Sq_7WfVWzOKLUpugRs1Kh0pgNxGEAUFqjtnrNJwYuRbgmEhRwk1cctMoG7v8Nrq28Gb6Bk-ZOfc_PhbiBSBODk6h_Yc5rqhSZg8PzBHBXbrnFK5Q1qDiNqpewuYs3-v4oX1n7CA5pbYnfP1XMiS-RYJYMOykMq0o4aKt4_sxcqi7svmQP33tz3BpjZlPKq4qEn8TZniZ9Wa0-NcJ7zpqQZ8nkuVSh_q7o9Ga7IOnpXXFE3RSgWIdCnxRIA0oj3Lob2ZLAcjwdcszoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
تخریب تقاضا در بازار نفت و انرژی های جایگزین
شوک عرضه نفت در کوتاه‌مدت قیمت‌ها را بالا می‌برد، اما تداوم قیمت‌های بالا با کاهش مصرف، افت فعالیت اقتصادی و تغییر رفتار مصرف‌کنندگان باعث «تخریب تقاضا» و کاهش فشار بر بازار می‌شود.
در بلندمدت، اختلال پایدار در عرضه می‌تواند سرمایه‌گذاری در خودروهای برقی و انرژی‌های جایگزین را سرعت دهد و وابستگی به نفت و اهمیت استراتژیک آن را کاهش دهد.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/21046" target="_blank">📅 18:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21045">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ترامپ به فاکس نیوز:  برخی از مقامات ایرانی مانند موش‌ پنهان شده‌اند.</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/21045" target="_blank">📅 17:38 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21044">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ترامپ به فاکس نیوز:
برخی از مقامات ایرانی مانند موش‌ پنهان شده‌اند.</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SBoxxx/21044" target="_blank">📅 17:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21043">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">این هم پاسخ ترامپ به چموشی سعودی های مفلوک در نپیوستن به پیمان ابراهیم و در عوض دست نیاز پیش فاکستان ورشکسته و عثمانی مقروض دراز کردن!</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/21043" target="_blank">📅 17:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21042">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ترامپ به فاکس نیوز گفت:   گزینه‌های فعلی که در حال بررسی هستند، عبارتند از: نابودی #إيران، یا اجازه دادن به فروپاشی اقتصادی آن، یا رسیدن به یک توافق.</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/21042" target="_blank">📅 17:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21041">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ترامپ به فاکس نیوز گفت:   گزینه‌های فعلی که در حال بررسی هستند، عبارتند از: نابودی #إيران، یا اجازه دادن به فروپاشی اقتصادی آن، یا رسیدن به یک توافق.</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/21041" target="_blank">📅 17:12 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21040">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ترامپ به فاکس نیوز گفت:
گزینه‌های فعلی که در حال بررسی هستند، عبارتند از: نابودی
#إيران
، یا اجازه دادن به فروپاشی اقتصادی آن، یا رسیدن به یک توافق.</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/21040" target="_blank">📅 17:12 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21039">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">رویترز:  در این ماه، ایران فرماندهان سپاه پاسداران انقلاب اسلامی، مشاوران نظامی و تجهیزات مربوط به موشک‌ها و پهپادها را به یمن تحت کنترل حوثی‌ها منتقل کرد.  یک پرواز شرکت ماهان ایر در تاریخ ۱۳ جولای از تهران به سمت یمن پرواز کرد و بین ۱۰ تا ۲۱ نفر از پرسنل…</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/21039" target="_blank">📅 17:05 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21038">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">پوتین:   رهبران اروپایی در روز های گذشته به صورت آشکار اعلام کردند در حال آماده‌سازی برای جنگ قریب‌الوقوع با روسیه هستند.</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/21038" target="_blank">📅 17:00 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21037">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">قرارگاه مرکزی حضرت خاتم‌الانبیا:
براساس اطلاعات دریافتی، آمریکای جنایتکار .... بار دیگر تصمیم گرفته است با چراغ سبز برخی کشورهای منطقه، در نشست مشترکی در یکی از کشورهای اروپایی، اقداماتی علیه ایران اسلامی را از سر بگیرد.
هشدار می‌دهیم چنانچه آمریکا علیه ایران اسلامی خطایی مرتکب شود، تمامی مراکز استقراری و منافع آن کشور در منطقه، بدون هیچ‌گونه محدودیت و ملاحظه‌ای، هدف حملات مستمر، موثر و دردناک قرار خواهد گرفت.
اخطار می‌دهیم چنانچه کشورهای منطقه با تداوم سیاست دوگانه در قبال جمهوری اسلامی ایران، با تجاوز شیطان بزرگ به ایرانِ اسلامی و مقتدر همسو شوند، همگی در این شرارت شریک تلقی شده و دیگر نمی‌توانند از نیروهای مسلح قدرتمند ایران انتظار خویشتنداری یا نجابت را داشته باشند.</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/21037" target="_blank">📅 14:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21036">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">فایننشال تایمز:   عربستان از برنامه تحت رهبری چین که بخشی از تلاش‌های پکن برای ایجاد یک نظام پرداخت فرامرزی جایگزین دلار است، خارج شد</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/21036" target="_blank">📅 14:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21035">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">این هم پاسخ ترامپ به چموشی سعودی های مفلوک در نپیوستن به پیمان ابراهیم و در عوض دست نیاز پیش فاکستان ورشکسته و عثمانی مقروض دراز کردن!</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/21035" target="_blank">📅 14:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21034">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">قالیباف:  جنگ بعدی ناوهای آمریکایی را در هر نقطه اقیانوس هند باشند هدف قرار می‌دهیم!</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/21034" target="_blank">📅 13:07 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21033">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">این تناقض را نمی‌فهمم:   از یک‌سو ناامنی در کشور تا حدی است که رهبر حتی نمی‌تواند یک پیام ویدیویی منتشر کند،   و از سوی دیگر امنیت در نیویورک آنقدر تأمین است که رئیس‌جمهور و مقامات وزارت امور خارجه بی‌دغدغه در خیابان‌های منهتن قدم بزنند.   آمریکا دشمن خونی…</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/21033" target="_blank">📅 12:56 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21032">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRaefipourFans</strong></div>
<div class="tg-text">این تناقض را نمی‌فهمم:
از یک‌سو ناامنی در کشور تا حدی است که رهبر حتی نمی‌تواند یک پیام ویدیویی منتشر کند،
و از سوی دیگر امنیت در نیویورک آنقدر تأمین است که رئیس‌جمهور و مقامات وزارت امور خارجه بی‌دغدغه در خیابان‌های منهتن قدم بزنند.
آمریکا دشمن خونی است، اما با بعضی‌ها‌ کم‌تر؟
✍️
پسر سوم‌ خانواده تیبو
@raefipourfans</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/21032" target="_blank">📅 12:56 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21031">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">قالیباف
:
جنگ بعدی ناوهای آمریکایی را در هر نقطه اقیانوس هند باشند هدف قرار می‌دهیم!</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/21031" target="_blank">📅 12:47 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21030">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pv_cmGAeqOosq-Z2ynw2Lc0Jj9vlgtw44uJx7D1tfiogA_QdNWLNEjneLAfOycDtr8Uje9WlcMURemeVY0yG5qCQ_2rvIwbreugYbcNA64luBmZzTUUojcrxfJjUiaWuaej7N2YfykFIYEdLL8MKTmk803lD6mVNTIfVMJD6uod-AhOr7TsYNvwrvVhyQPFVioUj1bUDJgpIZCUsHoTxd9tOg9RMoxU-k-4rxoRJV5HnZQNStzarbYdWhI2_1Isp11x5wPkkokLlajWN4r4q2TbhQgDCGSDSQ04fGzX2OVObiBdnkMx8Sb1Ezxnl2495KZGdqqxCQk7QJFsIAD3LKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve  نمایه FVC نشانگر نزدیک شدن طلا به محدوده قیمت منصفانه است و لذا از حالت حباب منفی ارزشگذاری فاصله گرفته است (به دلیل رشد سنگین از پریشب) هر چند هنوز تا تشکیل حباب مثبت و بیش خرید بودن فاصله زیادی دارد.  پس بهترین استراتژی برای امروز:  خرید…</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/21030" target="_blank">📅 11:07 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21029">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">کانال 14 اسرائیل:
آمریکا گزینه‌های حمله احتمالی به یمن را بررسی می‌کند</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/21029" target="_blank">📅 11:03 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21028">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EfwaC2fHo2S-HiOcmFEQb-tboPGnk39m-UzOA3ReZ_yRVngASa09fivL5BoTga__-PbL4bLchR5y8Ip8GHCRiL8IXM90dB5xolvrY7MC7ju4ERhKZ14HAD04-g8oWZNc_dxBveKXRQfJeBN9NvuvWvhoc4y45m4E5rGcifYZK79D778f-oJwD-3ZCzVv2I6X21fesbmuqkDfuCpq-t004HFs08jxwc8sLKBafhi2wJkZxlrQKPzpe_asOYukSfYpnydj2GiPh2S6cgkhgKi0FKwDHBgpAVs_m0Pk19QAQvtcKZ3TEGkmOeABcwO6XZrs9KYK_ww-JlrQ8s0uIjEPtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک حمله پهپادی گسترده در طول شب به مسکو و منطقه مسکو، در روز پایانی انتخابات پارلمانی روسیه، انجام شد.  یکی از برجسته‌ترین اهداف، پالایشگاه نفت مسکو در کاپوتنیا بود که صبح امروز آتش سوزی بزرگی در آن مشاهده می‌شود.  ظرفیت پردازش این پالایشگاه حدود ۱۲ میلیون…</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/21028" target="_blank">📅 10:26 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21027">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">یک حمله پهپادی گسترده در طول شب به مسکو و منطقه مسکو، در روز پایانی انتخابات پارلمانی روسیه، انجام شد.
یکی از برجسته‌ترین اهداف، پالایشگاه نفت مسکو در کاپوتنیا بود که صبح امروز آتش سوزی بزرگی در آن مشاهده می‌شود.
ظرفیت پردازش این پالایشگاه حدود ۱۲ میلیون تن نفت در سال است.
آخرین بار در ۱۶ و ۱۸ ژوئن به شدت مورد حمله قرار گرفت، زمانی که هر دو واحد اصلی پردازش نفت خام آن آسیب دیدند و پالایشگاه مجبور به تعطیلی شد.
تا ماه اوت، گزارش شده بود که توانسته بود تنها با حدود یک‌سوم ظرفیت خود مجدداً راه‌اندازی شود.
اکنون دوباره مورد حمله قرار گرفته است.</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/21027" target="_blank">📅 09:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21026">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4607a666c6.mp4?token=rCm7XcpIMmzhXRRNbguN_UFjOiilnmZ86hvsz4DWSMJraG5gSA-864_eR-qQp2HBTaAYqj4u7v4t8ZTFJHsnv_SMdWQQagQPEwxr0uU8P9U4oWph1CukSElBcenrh-MzjnGM_02cB-mFHiIzZ4DSxJfK2yQHrPqLgYOsGVBYMcyDyGMndtMQoHAzrpYL1S7vusLhyX6wlZQOm7R72NaFdlcWlWshAzGDRCu_5F3AwNEc57Ys6KVQf_uioK4hFKQmfKph4k2Mc8J8Ekr-1vxTTr6hIIAUbv9hqWxDyyjYrgKwX9XNE8Z6cptKbfkxjT04iBqRsqyfX0drPMtv8qJjGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4607a666c6.mp4?token=rCm7XcpIMmzhXRRNbguN_UFjOiilnmZ86hvsz4DWSMJraG5gSA-864_eR-qQp2HBTaAYqj4u7v4t8ZTFJHsnv_SMdWQQagQPEwxr0uU8P9U4oWph1CukSElBcenrh-MzjnGM_02cB-mFHiIzZ4DSxJfK2yQHrPqLgYOsGVBYMcyDyGMndtMQoHAzrpYL1S7vusLhyX6wlZQOm7R72NaFdlcWlWshAzGDRCu_5F3AwNEc57Ys6KVQf_uioK4hFKQmfKph4k2Mc8J8Ekr-1vxTTr6hIIAUbv9hqWxDyyjYrgKwX9XNE8Z6cptKbfkxjT04iBqRsqyfX0drPMtv8qJjGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت امروز من در بازارهای مالی
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/21026" target="_blank">📅 09:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21025">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d8265c9ad.mp4?token=GYmPx8bsoT-kpiGiT_ccJMZ7wpNXvnMm3gKKFfCGOH32YVQsA27PUPZlTv808HejFEpwX_jNXdQ9Jl8sls55dJkTq4u8KJYO3SIfMeOKsN160a3AUIV3Lz8ir01WDp0hyBDpF6k_Jj3ycnl0mZXXyzFM8suOo8CcvKFSF6USp0zlRVAvFGSQq3Qu0vGlt9wRX8EWLVcPRBQPaOccmVuXKOP3437XdOMymY7ZpxlklCjJl_xJRpuryVe83dcnqy0CkWpDWYe_7Ybz5MOqcAagkULSukWhWFnHopgCnf9pL5FYY9CA2tObt-JsNrArLuKkqFI-ztBEZZVxC3RpKuWjyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d8265c9ad.mp4?token=GYmPx8bsoT-kpiGiT_ccJMZ7wpNXvnMm3gKKFfCGOH32YVQsA27PUPZlTv808HejFEpwX_jNXdQ9Jl8sls55dJkTq4u8KJYO3SIfMeOKsN160a3AUIV3Lz8ir01WDp0hyBDpF6k_Jj3ycnl0mZXXyzFM8suOo8CcvKFSF6USp0zlRVAvFGSQq3Qu0vGlt9wRX8EWLVcPRBQPaOccmVuXKOP3437XdOMymY7ZpxlklCjJl_xJRpuryVe83dcnqy0CkWpDWYe_7Ybz5MOqcAagkULSukWhWFnHopgCnf9pL5FYY9CA2tObt-JsNrArLuKkqFI-ztBEZZVxC3RpKuWjyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از حمله موشکی دیروز حوثی ها به فرودگاه ریاض</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/21025" target="_blank">📅 09:05 · 29 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
