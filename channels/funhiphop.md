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
<img src="https://cdn4.telesco.pe/file/vkhcwemlJbPYmHtMrLqr8bhhac4GPVW7D6W2HLA5JuSceKzNkcC6SbtN1Se8HohsHhlg2YW56ZApC6RDhNqsiS59cLiYmfYi9ZNv0pS4KKIyCnrX-k3dsefdBDkyxRjw2oEpD7CAAyqq0zgGNXx4Ah6GbIhddloSYOEJFJxUzgKyonpb71o6R0V9O6Bn6viP3XsFd2XfgWbiQ_2aX_qBRa6Zia33JNGzHYqcXM9aar_2A8S-jA_9Fmm8FPTcpq__dT-VbhHvNXh-1mSDK-f1ELlKf3z9Zt2mlXd12xV7DHrBKds_XCoHPUXB1xFumCY4-HFNrAEibA-_LT_6PaKLxQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 172K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-23 08:27:04</div>
<hr>

<div class="tg-post" id="msg-77756">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">رویترز:
ارتش آمریکا امشب چندین پهپاد انتحاری سپاه که قصد حمله به کشتی‌های عبوری از تنگه هرمز داشتند را منهدم کرد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/funhiphop/77756" target="_blank">📅 04:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77755">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NiJreJl8gv12rht4c-3HzkQ6FjCQpSWPvwIwnn0508j6hOrPK61APagaScuLJB08X3ffKCxaOAkxrPiws418u9EXgt-74Slq_bZlhONdeaypWoTKsDofMn4P78q-dEvrVMDUwDLy65ppbbgIfrY6TG3UIAXM0yx13t5YN71vHz829_Ew2zdxaj0PygvPgfUXZf3-T44-0u6Lo6nCDSCVXJz6QLEKHSSXwcEbhFc0qXxs4Itsn5XLgCFndAxHNc-ALFy8N5sFMH18fYNnjxkRMFxZZ_-adYmNAUEbf3Kah5BckNOuUf2x1OJ495dZ1F7qK-IvaZiejKFzELfRAqFQmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار باقری هم در اتاق جنگ بود
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/funhiphop/77755" target="_blank">📅 02:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77754">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">یک سال پیش در چنین روزی جنگ ۱۲ روزه شروع شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/funhiphop/77754" target="_blank">📅 02:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77753">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">امارات آزاد کردن پول های بلوکه شده جمهوری اسلامی رو تکذیب کرد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/funhiphop/77753" target="_blank">📅 01:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77752">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">زیر این پست قهرمان جام جهانی رو پیش بینی کنید، هر کی درست حدس بزنه صد تومن میزنه به کارتم.
@FunHipHop
|  محمد رضا ناصری آزاد</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/77752" target="_blank">📅 01:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77751">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e3c0e5144.mp4?token=kin3-FC-Nf4nXHcUIhj_eK-tnsC0CHAoDy15DS3YYRDuq7hJc3ncSooEpLxwmV_mbke_Dv01Ag_bVyiRORYEVGXMCbAtPc1bb-CXn4Enit5O34RaRcah8IaXFOnGqucAnBcM4BZjvZ_ySfV0odXoJTBcEenUroNiWdqPMbimbCYo3GSBfOPjl1MajdG7_U605EOJtQ0e3npfeDjIFdzsj0qFvuXlFcES7h6yw_6mCxObZxiJlGuTulB-0SgDowtjIwsGUjdPgDjWScz7e7g5jHkHw0_f36vLpyn5DA3eHeAk3GvU034Gt506JCmxCmbMfd-hCi3YddeeJX7F4PGB0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e3c0e5144.mp4?token=kin3-FC-Nf4nXHcUIhj_eK-tnsC0CHAoDy15DS3YYRDuq7hJc3ncSooEpLxwmV_mbke_Dv01Ag_bVyiRORYEVGXMCbAtPc1bb-CXn4Enit5O34RaRcah8IaXFOnGqucAnBcM4BZjvZ_ySfV0odXoJTBcEenUroNiWdqPMbimbCYo3GSBfOPjl1MajdG7_U605EOJtQ0e3npfeDjIFdzsj0qFvuXlFcES7h6yw_6mCxObZxiJlGuTulB-0SgDowtjIwsGUjdPgDjWScz7e7g5jHkHw0_f36vLpyn5DA3eHeAk3GvU034Gt506JCmxCmbMfd-hCi3YddeeJX7F4PGB0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میساقی تو آنتن زنده خطاب به کسایی که مخالف تیم ملین: آدم مفت بر از خاله کسکش تره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/77751" target="_blank">📅 00:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77750">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">سیریک صدای انفجار
😂
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/77750" target="_blank">📅 23:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77748">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">عراقچی:
دو تا موضوع مهم هنوز مونده برای توافق نهایی؛ یکی بحث تحریم‌ها، یکی هم مواد غنی‌شده. راه‌حلی که داریم اینه که غنی‌سازی ۶۰ درصد رو رقیق کنیم. در مورد تحریم‌ها هم، ما مشخص می‌کنیم که دقیقاً کدوم تحریم‌ها باید برداشته بشه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/77748" target="_blank">📅 23:25 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77747">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">عراقچی:
برای خدمات در تنگه هرمز هزینه دریافت خواهد شد و این خدمات دیگر رایگان نخواهد بود. این موضوع مهم تأیید شده است: پرداخت هزینه‌ها الزامی است.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/77747" target="_blank">📅 23:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77746">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">عراقچی:
اگر در ۶۰ روز به توافق نهایی نرسیم اما دو طرف از روند راضی باشند ممکن است تمدید شود.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/77746" target="_blank">📅 23:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77745">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">عراقچی:
محاصره دریایی آمریکا اولین چیزی است که در این توافق به آن اشاره و تاکید شده است که باید رفع شود.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/77745" target="_blank">📅 23:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77744">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">عراقچی:
به‌زودی ایران و عمان بیانیهٔ مشترکی در مورد ادارهٔ تنگهٔ هرمز منتشر خواهند کرد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/77744" target="_blank">📅 23:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77743">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">عراقچی:
دشمن تعهد میده که دیگه آغازگر جنگ نباشه و از تهدید و زور استفاده نکنه و دوطرف به حاکمیت یکدیگر احترام بذارن و در امور داخلی یک‌دیگر دخالت نکنن.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/77743" target="_blank">📅 23:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77742">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">عراقچی:
توافق شامل دو مرحله است و موضوع هسته‌ای را به مرحله دوم انتقال دادیم و هر وقت همه چیز قطعی شد به همتون اطلاع میدم.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/77742" target="_blank">📅 23:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77740">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDiscography ship(blue)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P0oTxD4HGRlF2aoKTAdvg5Y-yIby0nLcWhZv3CfkQnsV6x6x_3_zHNeoVw6I3dFT2uqjJutUlx1lNya85GrKot1FIjjHlHMgPUepxgi9l8ZhC4T1hMYuWQMEQDNn9Zk-keZN8_nN_-ilA0XGaFNiP3j0tf0Bweuie9hDpoQcrtkaTCEN85u73hLd47eV4caYESsuPd57NWwMoWjOl_VqqRE1e7TNAeBW8F9rhcb4cJ32_OJH7SwHTXdvp9Sroehft1bu57jVa0I4hGP5icWusC8KT4_gvMjcP11D5c6dUybR9rWpQAbOgy0-MUjSr5dN1s8XqYKLclQiJ7BhYBS-1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Complete Albums Of
YËAT
📌
ADL
📌
Lifestyle
📌
2093
📌
AftërLyfe
📌
Lyfë
📌
2 Alivë (Gëëk pack
)
📌
2 Alivë
📌
Up 2 Më
📌
4L
📌
Alivë
📌
Wake Up Call
@DiscographyTship
🇺🇸</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/77740" target="_blank">📅 22:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77739">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_K6SOe1wvCCUaHRUNiGVLTujfEceX1VJMY8ZXsYoIJNudSnolM1BKVsyubgMsKDu6Ou7jJXZpkXnJRojpELZWqjPN3NXEyK5vYOgMN2rUMcvNZetsHM7bS6Pa19Y8iYVBBZ9p8rQm6sR6PzVsI3kEN0xYbO8n6_hmWUUG-dAz9skGLf1I686A0E4TbbzAMfu-biu3ZJppU3QbvurJnGO0m_9KcLi8sZ7r-HpowivyFsS5dJd54SHFx4JW1ha4Z2lRdom9h_lCfDZDkDo-2Vz9ulNMyBNrdL68dEGnF8PP_v2WvmJ2HVyMfvaTjZy53m4lO2fkzo7axE0MIx11o1sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوف خدایا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/funhiphop/77739" target="_blank">📅 22:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77738">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uIK_0l96Msbuid1UXezdWdYBjWL23UUZxNNp_4tf_0lJ6ll5YFBm7Nf4P6aErf1cMedB_gy58W7q59IK9vjnwQ4bEo-0i7U2l_0-RzeXSqjX0yhTLokc_TmNGV5ax-rk30ShEqkHgVxF-bU3qHdlHB6zg8NZMT_bkj1kT_qxdNSa4XVdoFbSL9B43QsExn-kW5JSwDrurLJtMdVOCV5FuLRVQa73wKYVfy7PvYScK0WojTbCZIvC5HUZIyPFJnWN2VYQxzNzp2NKFXXV9myRztJBwpJC328oODvSg2OiAHQ6R5wk4fqyYMSWNixR5hr3CXUTTv8ZiIJ0NvoxBVLsXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود دوستان شبتون بخیر
💤
امیدوارم حالتون خوب باشه
❤️
کانفیگ داریم سرعت جت
🚀
(جتی که حرکت نمیکنه)
کاربر نامحدود
♾️
اتصال پایدار
✅
قطعی ام نداره
❌
(چون اصن وصل نمیشه که بخواد قطع بشه)
هر گیگ کمتر از 7,500 تومن
🔥
لیست قیمتا توی عکس هست
👆🏼
ایشالا که گول حرفامونو میخورید و قید پولتونو میزنید
🫶🏼
Channel ID:
@RezoraVPN
Robot ID:
@RezoraVPN_bot</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/funhiphop/77738" target="_blank">📅 22:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77737">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">دوستان عزیز در خدمتتون هستم با یک برنامه دیگه از سیاست با فرید میخوام فلش بک بزنم به حدود ۲ ماه پیش  عباس عراقچی در یک توئیت اعلام کرد که تنگه هرمز باز شده و ترامپ هم در مورد این اتفاق بیانیه داد نتیجه توئیت عراقچی چیشد؟ رفتار خودسرانه یکی از باند های قدرتمند…</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/funhiphop/77737" target="_blank">📅 21:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77736">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDiscography ship(blue)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pb26cPcqUrojE-dLGU4nzfM3SKXP07oNUKiicN__3jtlSrlzdIfECeKTT6Ze9UtQBIlPXY9g97je-_-azCfUSaShOIeq764Xq89aXlVBTh32UmbmXV59_pAmDrZWP-ogr7nHLGiDyyjG3ipDEfIO2SJqvnjDPKxaBp6KT_IZ9ED_uIARNSbvpt1S1z754MWdI8TCaN8eb7maLz-onMA4g6hZ_n2L8qYJLmfhvK0FzrgOnWxpDy_KdQYzBcQYTVntpDN-dhgEjJPuNFPIOcwurgyZYnE-Si0f7Zo4p-X9ySfk82luuDW25l3zipcjBB3l7L-N30bb4Da1_AL56JrHlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Complete Albums Of
Kendrick Lamar
📌
GNX
📌
Mr.Morale & The Big Steppers
📌
Black Panther The Album Music From And Inspired By
📌
Damn. Collectors Edition
📌
Damn
.
📌
Untitled Unmastered
📌
To Pimp A Butterfly
📌
Good Kid m.A.A.d City (Deluxe
)
📌
Good Kid m.A.A.d City
📌
Section.80
📌
Overly Dedicated
@DiscographyTship
🇺🇸</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/77736" target="_blank">📅 21:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77735">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MmJzRB0vmZ6cC5Dm-8hDuAzzssiGWgvyvQe8FjMlwbyS4zAvbifhs-T1_1GSDCG_pEhtedV767k6QUnM_YF7B2ffRpe1Bw7o_l4E_MZT_mgVli1w7DlqF3IUHNu-983HKDf0A3X7JRHpkyjoRLOKanWjeHi80ufK_FAV39URUS7t4tTCx2TEzpw715-jXZUOq7l-4ZVc1cTvJfc9bd-PVRBpFqp-1Ts3evns7V4IVY97nw2PG4DZjhKWiIQI4Y5dENod3Gd8b5XiSIivA3hRQsEhR-9oYTZqCYsuiFd4uVUTpK47YbdZja6vtBdfFrIuRpVDJOy9a8JrXy1Z75bgxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شنیدم مردم افغانستان میخوان قیام کنن، میرم اونجا هم یه سر برینم امیدوارم اشتباه شده باشه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/77735" target="_blank">📅 20:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77734">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">مردم افغانستان برای امشب علیه طالبان فراخوان دادن و قراره به خیابون بیان
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/77734" target="_blank">📅 20:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77733">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">دوستان عزیز در خدمتتون هستم با یک برنامه دیگه از سیاست با فرید
میخوام فلش بک بزنم به حدود ۲ ماه پیش
عباس عراقچی در یک توئیت اعلام کرد که تنگه هرمز باز شده و ترامپ هم در مورد این اتفاق بیانیه داد
نتیجه توئیت عراقچی چیشد؟
رفتار خودسرانه یکی از باند های قدرتمند سپاه و بسته موندن تنگه هرمز، ایجاد جنگ داخلی، حمله خبرگزاری فارس و تسنیم به عباس عراقچی و …
الان هم به احتمال خیلی زیاد توافقی که ترامپ ازش صحبت میکنه با باند قالیباف و عراقچی بدست اومده و این میتونه تنش رو در بین مقامات باقیمانده به حداکثر برسونه
باید کمی صبر کنیم که ببینیم واکنش باند مخالف توافق به این توئیت چیه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/77733" target="_blank">📅 19:31 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77732">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">میشه بگید ژنرال یه عکس دیگه بزاره؟ من نتونستم ساعتشو ببینم
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/77732" target="_blank">📅 19:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77730">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jV7V1fLCxGofK2XwGYvHhDlTVpnWM5_MS7pnodaWEVJNeKBEZT7bRmPQC5_fNgE_3Rr5QZZeezTrzJW4IIMP46CwFcrYhqxuHst5erJ6qVQ43a6hmoOHmE1xM7pnRUZ6aWxaxJB_WU2zC3elHc6MiQ8cIkiWAvwHfjublQFHwVBzRAccu745-WVpWKJNEMMUDZdNYC9oDAe2mqIstfrw1xDJSxTG-y_sGaYN3TSk2hxpp3ApH-ha-OCbhOpmpPYmhQGqj6AAOut1evJjHvQmfaW73hUzojhf8hIkw8U-1Ux-8FKFQTWBkQ7ldneb2Wvx4-iyiumiYYBwJ7Xd_hSuKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دالگخیز توییت عباسو ریتوییت کرده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/77730" target="_blank">📅 19:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77729">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rre38sxhiIz5zJSfFrDhDIpgDD28skit617sBn92t2dLFOOu_z4Fadk0u--_5HBDqakCaJ7rbTr-5EkxhsslykpztFeuPTBwKZ9hz2-BUPI-ECqRu6QFLyOG6SPB47jchT6997g9jf264xtFxmiIPMhdkWcfO4pxaDPahD5rvGVLQGJtIKuBu_h-UKnS0rb9ZS9ffNzCk1vDya-6Z_w9SledS9DkDANWId-Dr0Y_n0NG2TiTnprfisLDwoJeS7JAwQMa4v8L6ooQJKDqhPR3y9XpodsGIdkcEubqRETckqk_2zZwsXBUfpLgZtR6HY4fmD7NA85_UGWbWwILzQQgIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سری آخری که عراقچی گفت به توافق خیلی نزدیکیم هفته بعدش آمریکا و اسرائیل حمله کردن پس تا یک هفته دیگه جنگ میشه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/77729" target="_blank">📅 18:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77727">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">عراقچی:
توافق با آمریکا هیچوقت انقد نزدیک نبوده و مذاکرات به جدی ترین حدش رسیده، بزودی جزئیات رو با مردم به اشتراک میذاریم.
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/77727" target="_blank">📅 18:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77726">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">شاهکار ترین عکس روز  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/77726" target="_blank">📅 18:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77725">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_MJICodsTr4jcxuwFfXBjUs2TsBZVp-Ab9y1dXXHa7MLrJnjWVH73LEuYevwXTo9TcorR_u_pN-XepY7DkHHLH0gxARnCNkyvVHCuwjnfqDfIJySqwpmQ8_4xLgRCgv8xCB_LDUkIE0Vsds5DnlrfuiNYERaWVm1S2Ry1jq5AgwGJtyMUd4K0ka8JI8zAF9eX43I1ThDIZR56iRF5g5zivLo6QVOu3x9sFOYkOYFvGCXU0W0ztyALKDD7eMEfyfYNPVimQFLkihx9XSOU3axT0205flbJ-AUV6-PlvDnxkG1WgdJ-FLHswblxGgDbBQvAc-FWwBgLOf52zXDVq69A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاهکار ترین عکس روز
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/77725" target="_blank">📅 18:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77724">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dtd74wyI180E94XC2kUHPNEtnhqfFXb1_q8dtUXiQRhxMb_RXAbHUb-CS2XR0qIgRmOko7IaLTPa86Jamk5BaHTxDO1Beigl6ovMMPwBuFu92rzjoBpsPOzRcfKiHvocLIKmfcBNIQ8Rw60vnYhXYIqSm-exjJ92KQAxaSE_AhadwtI7L_bppVdmKJH7S53V-HhLX_dDkWNW_xUXLqJBzWTlWVCbKqdVBk-HwntKMBoALXdWKvlzHABrLNqKUIcnE525ZZEpEq63otmv3oJlnecnV5iCyTeKOL0RZedU8tbI_auFLOk9sPehPdW51ocRUqgNNUf5UiDegx9u7SK1xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این کره جنوبی هم خوبه ها، حالا در حد تیم ژنرال نه ولی خوبه
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/77724" target="_blank">📅 17:51 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77723">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FjJvTeclVyehFnrrR1TTtWh927UWzCtHo3weKwwYlE4-mWTolzi7CYUg2SyPW5URuKHJTnb_kHqxnOgLsnSt8igKz-H3PO48tn-DxIVxwEhPahLuo5jFv61zyoKOqLGokZvtMYkvzKmPWOM-QugS5NyyGUGjV8wNU36GeT2zCvEOTCQQf5j1YvGABy8aXS5mEKoy4GXxUBrdWWOHg3Umjkwqp8qObU_YgKi4mBSzNykKk5Zm-DxtORQZ6RP-3B6fA1xyPSwW_C5kTc-UiWyFF_j9FDgrm_puLn2uIPnNr23uaJPY2I0i9iZIRl4ww2mCk1-9CgMY4kM8cNyBifnrbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو روزی که همه ویژه برنامه جام‌جهانی رو با رامبد و دیبالا و... شروع کردن ابوطالب رفته «علی پروین، مادرقحبهههه برو دیگه» رو دعوت کرده باهاش برنامه ساخته.
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/77723" target="_blank">📅 17:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77722">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">با ماف بت از جام جهانی پول در بیار چون کلی هدیه هم خود سایت میده
💵</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/77722" target="_blank">📅 17:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77721">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/va_6v3SzGEh9aOlEyjZKWt3OwlCa64ptX7TzSR0Nu-uL5gZ1TSzOLjn2rfdymKlhhcYH8sIfmKJ4zuu-OrS6jm_2y9GF9Xyr-huxZRJ8cia7xxtHu7okxpLgkQzYIhf99EDO6G-LvxOOpTQ_bLq7pBOJwWZ9uYFLIeSBBqksSBirCTlSlav5PUMslXs_Y3ZpaZdVxaaFlYnFkGNYpbXjFFRWZBZb7OZzbgTyALyprwq8VuqQb8XAdl5Gv5NKeJlVOdUrmPSx3rP6mJp2deMdPQjxvybtqljoOh-bJ2VTFFR0LHe_MvRslM7W5wfTKn-8cKk2R40M_i7TIV_wGWxmQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
چرا سایت بین المللی ماف بت بهترین انتخاب برای پیش بینی جام جهانی
❓
1️⃣
شارژ و برداشت اسان و سریع
2️⃣
پر اپشن ترین سایت فعال در ایران
3️⃣
دارای مجوز رسمی curacao
4️⃣
کارت به کارت همیشه فعال
➖
هدایا بی نظیر ماف بت:
👇
🎁
100% بونوس خوشامدگویی
🎁
برگشت باخت هفتگی
🎁
هر روز 100% فری بت هدیه
🎁
هر روز 20% شارژ اضافی
🎁
گردونه شانس با جوایز بی نظیر
👍
با فعالیت در ماف بت طعم واقعی امکانات در سایت جهانی حس میکنید
👍
🎯
ادرس بدون فیلتر سایت:
✅
https://mafclub.online/fa/?btag=260368
✔️
کانال تلگرام سایت: g22
🅰
🔹
https://t.me/+3Zxs6WU7L_UzY2Fk</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/77721" target="_blank">📅 17:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77720">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">رویترز دیروز: لشکر 82 هوابرد آمریکا خارک را تصرف خواهد کرد.
رویترز امروز: جی‌دی ونس و مم‌باقر قالیباف توافق امضا میکنند.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/77720" target="_blank">📅 17:42 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77719">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">فاکس نیوز درمورد مفاد توافق احتمالی:
مواد هسته‌ای ایران نابود و خارج خواهد شد، برنامه هسته‌ای آن متلاشی می‌شود و هیچ پولی آزاد نخواهد شد تا زمانی که تعهدات خود را انجام دهد.
یک مقام کاخ سفید گفت که تنگه هرمز به طور کامل باز خواهد شد و ایران موافقت خواهد کرد که از حمایت «گروه‌های تروریستی» دست بردارد. (دقیقا کی موافقت خواهد کرد آخه حرامز
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/77719" target="_blank">📅 17:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77718">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24c4a7984e.mp4?token=XWacPQYgIJBBwGem_7XIWsaVyxBJwVmSZIClwSbViI6F3AC_DhTojFwTHxdA_R-J098zwhxzt6ymuiyfESX0qYPpqn2kuVh7tsZx45je_dmWm2CZp3aNe3mHOA-Wx0mbs_HndA0epk7ITdVpsotoJV6O1oF4KDLazQ7YEuhWu1fBLizdwKsdRV0fgXmfiPDrutLkCqaSHrlUL0t44gMUF1tOXLOXo3o3tvd-N3QJsLwgnXdPnPr8kY6tt50iMX217km6x0SWRKv2hgMbJmf5FzhH-rZB8NuHj34lGHFnWdnCaGKSaODxSiNF2vj23QEpxTLM1EsA7e-J0RNhFsfH0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24c4a7984e.mp4?token=XWacPQYgIJBBwGem_7XIWsaVyxBJwVmSZIClwSbViI6F3AC_DhTojFwTHxdA_R-J098zwhxzt6ymuiyfESX0qYPpqn2kuVh7tsZx45je_dmWm2CZp3aNe3mHOA-Wx0mbs_HndA0epk7ITdVpsotoJV6O1oF4KDLazQ7YEuhWu1fBLizdwKsdRV0fgXmfiPDrutLkCqaSHrlUL0t44gMUF1tOXLOXo3o3tvd-N3QJsLwgnXdPnPr8kY6tt50iMX217km6x0SWRKv2hgMbJmf5FzhH-rZB8NuHj34lGHFnWdnCaGKSaODxSiNF2vj23QEpxTLM1EsA7e-J0RNhFsfH0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/77718" target="_blank">📅 17:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77717">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ترامپ یهو ریج بیت مودش فعال شد گرفت رو مذاکرات و رسانه‌های ایرانی:
شرایطی که ایران به اخبار جعلی فاش کرده است، هیچ ارتباطی با شرایطی که به صورت کتبی توافق شده بود ندارد.
آنچه گفتند، از جمله بیانیه ضعیف و ناامیدکننده‌شان درباره داشتن یک توافق، هیچ ربطی به حقیقت ندارد.
افرادی بسیار بی‌شرف برای معامله کردن.
با آنها، چیزی به نام معامله با حسن نیت وجود ندارد.
شگفت‌انگیز! همچنین، حمله پهپادی کاملاً دفع شده آنها دیشب علیه کشتی‌های هندی که از تنگه هرمز خارج می‌شدند، کاملاً غیرقابل قبول است.
بهتر است هر چه سریع‌تر خودشان را جمع و جور کنند!
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/77717" target="_blank">📅 17:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77716">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PeDRJIGSC4Vf8jMD2v2MpydKvGZAc2H9T9oAQS51xnEmQpLPJKTpVbiWnSW7r6MUB5tExajKJVQCkXIku6v49zTiMPZz8brRZBCOuK4u0J65qZUIbSBEZMNG4miMpd_hJZ84vypva3xEdxqAoXwFQQwF2zCAvvgz7CacMewmBHq7n7r2tTmmKfDF0aOB9qvKvPh-MeMyS5y7X9T9HpVlfCfMqB3Tzhu_uMuWjaiwybdKzMClYdzY5ChgJ7cWA1hd-y5Q_5a7bvFZVJHqwWhaOqdyvq2k3cuIvAZU0_cxmYv4lh2U-X5r6-NgUPk_swtpNn7zJbNnpsmAB1vbo0-vyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ببخشید ارباب سعی میکنیم درست بشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/77716" target="_blank">📅 16:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77714">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">انتظار می‌رود امضا اوایل هفته آینده، احتمالاً در ژنو انجام شود.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/77714" target="_blank">📅 16:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77713">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">من تازه فهمیدم چرا علیرضا منصوریان کچل بود، خواهراش کنده بودنش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/77713" target="_blank">📅 15:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77712">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NrD1mehQK486aw7woypXQWNoo1q6XNm7oXicsstdu0WTud0BGve033zjA15W-GFZwDhH7nENx9y3sS9k9kCvP600pBDHpYjkrotUuWbXTe5eHOKtkbaCkTE1IThwhk_I8ivtagqnIw1tkwIvWW8cv0sAQeAQdghsGupU05OaHGHTDqmz_WA7r62uYj_Pyp5LzVjxzHALyPgTgRCPwo6GwFS4il9XHDeWwv75OCsGc77S3ABS32SHv_tbcZFHjt8zY2xEtNnKmT8xFVSd_4OVZ03-upChKzTZXJ6uoV6TkFNqyiVPARkeoi0vAjJqTuk9daMp3ryf7TnO8gKfeGSGLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام:
کشتی‌های جنگی و تجهیزات هوایی نیروی دریایی ایالات متحده همچنان به گشت‌زنی در آب‌های منطقه‌ای ادامه می‌دهند و محاصره علیه ایران را اجرا می‌کنند
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/77712" target="_blank">📅 15:51 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77711">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1716c7017.mp4?token=Y7xyEh6bG4vvjqsK294jBWGEBgD1MqkIjF-a9FHShJVdj4ez4Ix_3YQz-MscjyNculGo-kIrcDDlbECGy3pQ5JLwPf-k7R2PEvJv6XYSWMFxWbdwQzDEmspFbx7M-CeqBlxOMM244g6XVbCjDJZyphMgOndwgnZV0fA57RfdrRn5rpbfKCc5gvFNjGfbtKUnKxP7MgwKe_-8u-Nqo1dNpPH8ATu5OwemaJa-HUh-l9TI9Wn71TwqSoy38kZwyCHO8YvLiaydWNNjQ6VyI5ZxM0-EAdnW9scAOmGUz7ijwCRbfpRCchpXV2wVYXTIJ5nbmGFNHjnQkuD62xqdPKaoOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1716c7017.mp4?token=Y7xyEh6bG4vvjqsK294jBWGEBgD1MqkIjF-a9FHShJVdj4ez4Ix_3YQz-MscjyNculGo-kIrcDDlbECGy3pQ5JLwPf-k7R2PEvJv6XYSWMFxWbdwQzDEmspFbx7M-CeqBlxOMM244g6XVbCjDJZyphMgOndwgnZV0fA57RfdrRn5rpbfKCc5gvFNjGfbtKUnKxP7MgwKe_-8u-Nqo1dNpPH8ATu5OwemaJa-HUh-l9TI9Wn71TwqSoy38kZwyCHO8YvLiaydWNNjQ6VyI5ZxM0-EAdnW9scAOmGUz7ijwCRbfpRCchpXV2wVYXTIJ5nbmGFNHjnQkuD62xqdPKaoOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
توهین بسیار زشت صهیونیست‌ها به رهبر معظم انقلاب.
🔹
صهیونیست‌های ساکن سرزمین‌های اشغالی که فهمیده‌اند کار جز کودک‌کشی بلد نیستند، اینبار در اقدامی توهین‌آمیز یک مقوا با سیمای زیبای آیت الله سید مجتبی خامنه‌ای به همراه رنگ‌های مختلف را در رژه روز همجنس‌گرایان نمایش دادند.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/77711" target="_blank">📅 15:36 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77709">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gumW-NQY8DvkrW3bdlG8EXvqADjsjFq1UTzDkdlhk9VgbpMXIB99uBPXhGQn7_QwiXjCPObfqY9L8gLt4L8iTj-Cn7kiZyg0vNEV_QzcHdGM6h3u4MZlqIrPFJtYQFmlNFIi8SXLWEORIMmDX6K-A0RExRuYgtUaDAX1gchrHHvSbEesEyH6RXQja17FexGquNH74LfnVof7rX2bfyrywI9-U_pPPj0_4HbyDylQW3HN6KnLYiYysA7aNiyizsxLo72sIs2SjoFGEqDrmejITXbnjBbg6ILL8XVQfBl-IquVlGJjWVrA8IyUu6chZGa6HhI7JiRHzA2j4Ioi0_zoYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#رشید_مظاهری
را فراموش نکنیم
رشید مظاهری دروازه‌بان سابق استقلال و تیم ملی پس از حمایت از مردم بازداشت شده و ازش هنوز هم خبری نیست
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/77709" target="_blank">📅 14:48 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77708">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UBW9ijgjTUicSpMQEw95ynPPTJXC8g0cp3cUIjxEAFlPzdfrRSOqkkexjCjEAnLcDjQhNshIk7NO9vkLHywwZrD_ng0oiy2ytfQOHc4ZJFh_cSUfL2iT_SkF-Eui5w7Y1ZgNu3veVYx03OaKTSALw9x2U7j1aC0twscPsND1MdZeBdsX54ovfForvpZwMxBgqkhRjCjqpX1-ZZAKAVukJId7w0oPz_0hHtPA4ZWjad13Veyn_fDfgP6DiKEF5K0Yo9XIcMPkjAowUQf3a_ifhHyG-i0WkC3KiO7wG4xt73CVbZofR7xt3UYab0lwgeP_ikpIt9gUxm-J4oNg3RWlBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بمیر دیگه کصکش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/77708" target="_blank">📅 14:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77707">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ojCVAsb8VY-J8aIwG_cqOF_DjZ4zYYyjcytDc6xB9q3ryCZ6cD3BH4PyExqJqkqscZUNDXCPz02YDyK8ppQnjx9w9vSlxoM6Jr76mgSV0zXVXsqGN6VbhHzErjCzxPwmM-wtZXz6OuV43E9Ywx9HCGPw01afTlnXvypk8TeBtQ33BFJ_QQ9wgkL8fQXLlqJA-yF2vQuChLuvtYiQhXpOIsXpgUAdeCL94fzHfIUcHhUbp1xS43mEJzwLp_XzRUFKCoHv26uW8JqXnijAW0Cpdhug6X38p5zZ1y3w1vbPlrsJ2ZEzC0uR0LLXF--oA2YBuIvfwQlrvkymXgexdWJ0OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیسو
😂
😂
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/77707" target="_blank">📅 14:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77699">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">اسرائیل هیوم تقریبا توافق احتمالی رو کامل تشریح کرد: ایران اصولاً موافقت کرده است که اورانیوم غنی‌شده بالای ۳.۷۵٪ را منتقل کند، از غنی‌سازی بلندمدت صرف‌نظر کند و از به‌دست آوردن سلاح هسته‌ای، از جمله از طریق خرید، خودداری نماید، به عنوان بخشی از یادداشت تفاهمی…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/77699" target="_blank">📅 13:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77698">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">اسرائیل هیوم تقریبا توافق احتمالی رو کامل تشریح کرد:
ایران اصولاً موافقت کرده است که اورانیوم غنی‌شده بالای ۳.۷۵٪ را منتقل کند، از غنی‌سازی بلندمدت صرف‌نظر کند و از به‌دست آوردن سلاح هسته‌ای، از جمله از طریق خرید، خودداری نماید، به عنوان بخشی از یادداشت تفاهمی که منجر به لغو حملات آمریکا به ایران شد.
تنگه هرمز پس از امضا به طور کامل بدون محدودیت یا عوارض باز خواهد شد.
هر دو طرف متعهد می‌شوند که در این ۶۰ روز علیه یکدیگر یا هر کشور منطقه‌ای دیگر اقدام نظامی نکنند.
این پیشرفت در مذاکرات پس از تمایل آمریکا به آزادسازی ۱۲ تا ۱۵ میلیارد دلار تحت نظارت قطر
برای خرید وسایل بشردوستانه
ناشی شده است.
یک مقام ارشد آمریکایی گفت هدف استراتژیک تغییر رژیم «فعلاً» کنار گذاشته نشده است.
انتظار می‌رود امضا اوایل هفته آینده، احتمالاً در ژنو انجام شود.
بند آتش‌بس لبنان همچنان باز است: آمریکا مایل است به اسرائیل اجازه دهد به تهدیدات نوظهور پاسخ دهد، در حالی که ایران خواستار آتش‌بس کامل است.
مذاکرات آینده ظرف دو هفته (مطالبه آمریکا) یا ۶۰ روز (مطالبه ایران) به محدودیت‌های موشکی، حمایت ایران از نیابتی‌ها، خروج آمریکا از خلیج و تضمین‌های بین‌المللی خواهد پرداخت.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/77698" target="_blank">📅 13:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77697">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">فوری
پیت هگست 44 تا پرس سینه رفت و ویدیو شو منتشر کرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/77697" target="_blank">📅 13:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77696">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">اسرائیل بمباران جنوب لبنانو از سر گرفت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/77696" target="_blank">📅 12:52 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77695">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EU5MFQ0d9LR3_jSwGkxbolqoYK7WtOp_czZJTjw9zAKDidV43W7lusGcYZT79SHxXY3L3NH54e-xf1CaHTBIMINxoJMLhzDWTAp-mPwZbWOW_vom8UjHc3QWDMG0IJdslNGELamspJjX_H_YOmB9GeTr9_3unKtcfSft29ZXdWq6wNp-bINzhNhBlykF9YymyFgPsNMdFkQ2j6f3sYekVa2XvlryxjTdwNvLcL2G0XfhWf6ar3Mqg7IFkDOI63OlBOMtj7Fdjk2yEd-x_Z3k5jxFiTrwSob2yfifIwWmrrIf51f8zdwu9MfdwgdmV7RtFnqOZy3Jn2KvqW548UimIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پوشش اسلامی سال 2026
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/77695" target="_blank">📅 12:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77694">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">فقط چرا اون پایین زده ۲۰۲۲  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/77694" target="_blank">📅 12:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77693">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UzjrJM7kIDdZkEcv_jEo6S1NUSdR9AgcBWXzpI345tJ-X22xCikCLv2vBi9dnlQ3vLhUSY2UCIqsl64obL48zMooO6x-XmsP_SdEtyoS1TBXx-5uOUYU9vffJCnNXoqMniNA9yzVWpOdbWibPvwpyHWnSffUEAy8gCzofNextaDXdpYxfqSvBEN6owCND2bYvA5luZMfptmraNviDgLJg1E_k305tUit7NrP1Xt2Q77qWBg2IAShHc66IuLm5bLjD6Lr4HnutSu5QkQRB3vBM6mi4glYNwxfNeJ8h3re33UMftFGkIyXiXjBiFbzdlJUGITsVoApnRVf64apT3R1rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط چرا اون پایین زده ۲۰۲۲
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/77693" target="_blank">📅 12:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77691">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kfHchuibUaMoYi_WjebWBItH1G9qFXty2OVsnIy3mF4pmEOTLX48818_4PDFNw4v7wjPM8AGq7mclviRILVpMS7JfJc0g5Y5fO5wMHwoGSRI5owWuvMex6bB8ZPJXSwaC_BgG8JwDPlIvltXyRxXigjq2upgCALSq_DAdTUDvvQUmjLXHN5B8WED73dj5FckgJCbbEJsO74wYZF00eCr3aMtXlJBf0X-vJG8BF-ki20a2JB9GK8TD4rA0x9cyaaf9R7ahl6g9x0-YBG8iw89BWhZncSEh1Trj1OaMVzkkcQuryQB--wQAfyRppNC7A2om-8-PaQLXm0Po2kI-AeWeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خواهران منصوریان ساعت 11:08 صبح رو بهت بخیر میگن.
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/77691" target="_blank">📅 11:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77690">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VI37lA54W2--nKfOSwV1bIZAv3yF5xluy4UCjeG2uRAygc2-euDxGoJLxsqISS2TBj_ME8XzqHAXEs0fyGSohIr6xiiO9sOuFJ2RLPH3THa6evtb1VC90yMowh3tPCuTtv0tRrVlVxan0bsbszZ45JtdKxA0TIzg1_8qaL28F39wbjcsTDjAfah6K9aLGhw3PPHlETP1bghYn7P76B-5HE73UkD3sG68_elgNLZFIf5gp-sTB5--lQ_lSIH1vTwpcVqc0RZXauO5T_ty10uUZA8QF5OhrmosR4zRZS_fgDRzdVIvF5aJF4qLF3furch63bUQV6WGGTXDqPUkZ1ODIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افتتاحیه جام‌جهانی
❌
فیلم سوپر BBC
✅
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/77690" target="_blank">📅 11:03 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77689">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/77689" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکشن رسمی سایت دربی بت
🌐
DerbyBet.com
💰
امکان شارژ ریالی ، ووچر ، کریپتو در کمترین زمان ممکن
🔥
🆔
@DerbyBet</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/77689" target="_blank">📅 11:03 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77688">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMkbAwBiSNxbEjipRZDwuC_Fr3mt28B5jM58mNyO1MgVbS7fQeJCJP_XDSK-DkzOIHW6XRySoleKNR-jW39vGOfeUpD2Ui0KIARqjKzwC4eDljTKziGwDwjJq5sZGkX-fzJSGBrvMojftyKgQdqGQvCLCbfzN7vBtcD3GS-8JhnwlTzbiInD_zc6MJaPUTmWA7HMqGRTcuKvBOcrCLB8tscsXccQkDu7NjPJS76EIwGcur9ern2ZD_8kXyaa6YojddlSyEuqm4LGE9T-oKW_D4s45BtxozX-z3Fujq-092Fi5QsxCKgU9xBxjv7Jy-idiGiPItXjCSJQcfoyF86n7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دربی‌بت؛ جایی که پیش‌بینی فقط حدس نیست، شروعِ بردهای واقعیه!
✅
با لایسنس بین‌المللی معتبر، وارد زمینی شو که حرفه‌ای‌ها بازی می‌کنن!
✅
آفرهای خفن ثبت‌نام در دربی‌بت؛ فرصت‌هایی که تکرار نمی‌شن:
⬅️
۱۰۰٪ بونوس اولین واریز؛ شروع انفجاری
⬅️
پشتیبانی کامل از همه ارزهای دیجیتال
⬅️
درگاه ریالی و تومنی امن، سریع
⬅️
برداشت‌های آنی و بدون معطلی
⬅️
پشتیبانی حرفه‌ای ۲۴ ساعته
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
✅
دربی‌بت؛ بازی کن، ببر، لذت ببر!r22
🅰
✅
https://DerbyBet.com
📩
@Derbybet</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/77688" target="_blank">📅 11:03 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77687">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">شاهکار جدید جواد خیابانی:
خلیج فارس خاک ماست
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/77687" target="_blank">📅 10:52 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77686">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcee0eb614.mp4?token=R1OguoUZM3bZCHf317jZdiaXvsO1oTDxcXSzslUcl5e8yl_xdi8daMcnDnZJDu3qKy74h_b3xsi6cmUO_kgypPmGrQQV9Qv8d94MvzmHcAld6tpqMoT6HHBpCTlnAxJfodXBSExB8mfBkYUSJpt4SCJxxav2vVBkyFsZO-ZsDoGvCpSDZ0-cOAfT7pVPt8tVFy-d-kFEpXACQxKunEj63qUtoQGKWErkB-tcd5D6KsjP0RMZLVAyy61ZsJVJusfBadhPXKFL24RAhPx1_ccbZCe4LtVNW2CwWGJSILBhhJYGUKWDg4KJhp15FWlRD54maOC6OAuxChMpuq9wGuGFbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcee0eb614.mp4?token=R1OguoUZM3bZCHf317jZdiaXvsO1oTDxcXSzslUcl5e8yl_xdi8daMcnDnZJDu3qKy74h_b3xsi6cmUO_kgypPmGrQQV9Qv8d94MvzmHcAld6tpqMoT6HHBpCTlnAxJfodXBSExB8mfBkYUSJpt4SCJxxav2vVBkyFsZO-ZsDoGvCpSDZ0-cOAfT7pVPt8tVFy-d-kFEpXACQxKunEj63qUtoQGKWErkB-tcd5D6KsjP0RMZLVAyy61ZsJVJusfBadhPXKFL24RAhPx1_ccbZCe4LtVNW2CwWGJSILBhhJYGUKWDg4KJhp15FWlRD54maOC6OAuxChMpuq9wGuGFbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه بنده خدایی هم به توافق اوباما که بدون ریختن یک کیلو بمب، حدود ۱۰ هزار کیلوگرم اورانیوم رو از بین برد می‌گه شکست مفتضحانه ولی خیلی جدی معتقده ریختن چند هزار تن بمب و بگا دادن کل اقتصاد جهانی یه پیروزی تمام عیار بود چون بعدش ایران قبول کرده بهش قول بده که…</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/77686" target="_blank">📅 09:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77685">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b774ac8b5.mp4?token=HKJjav4xhYDuQTnf1dXrgLiOsXcH2WFzhBqCnKUR47ymT5ETm7agPAbuldQx1wytVeaKJ4ABym5kIwCb_OivNRXol82NNcBBy2KV8tXgM7gC-jb2aUJWHWiIH270QuPl-vX_dsunNzk9Xy9KROFrWh5Opf25G_fxk0C-qLVPQuqGl6pV_MiWybOfwvAaS49L8LGAv0o3A6mIBtxCaxwR4OqYxrvGq1bYUGAkN0RGgd6VYtvfkDptbbUYk4xI-Z8IWhYS04bLKd0nAY5Bb-Feuvg0u1dmwxkoBl6J1inhh_mgDOM9tJZ03Z9JxvyHR9uomAJ8SW-cQjKu5IaemXl0mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b774ac8b5.mp4?token=HKJjav4xhYDuQTnf1dXrgLiOsXcH2WFzhBqCnKUR47ymT5ETm7agPAbuldQx1wytVeaKJ4ABym5kIwCb_OivNRXol82NNcBBy2KV8tXgM7gC-jb2aUJWHWiIH270QuPl-vX_dsunNzk9Xy9KROFrWh5Opf25G_fxk0C-qLVPQuqGl6pV_MiWybOfwvAaS49L8LGAv0o3A6mIBtxCaxwR4OqYxrvGq1bYUGAkN0RGgd6VYtvfkDptbbUYk4xI-Z8IWhYS04bLKd0nAY5Bb-Feuvg0u1dmwxkoBl6J1inhh_mgDOM9tJZ03Z9JxvyHR9uomAJ8SW-cQjKu5IaemXl0mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه بنده خدایی هم به توافق اوباما که بدون ریختن یک کیلو بمب، حدود ۱۰ هزار کیلوگرم اورانیوم رو از بین برد می‌گه شکست مفتضحانه ولی خیلی جدی معتقده ریختن چند هزار تن بمب و بگا دادن کل اقتصاد جهانی یه پیروزی تمام عیار بود چون بعدش ایران قبول کرده بهش قول بده که سلاح هسته‌ای نداشته باشه.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/77685" target="_blank">📅 07:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77684">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lIuA2HAMRFggN4lb3ucaTbVb0clUTiRYeBEjm6WUvEm4YgkVoIo3ISIRWp6rkHNN6q4lM5Rqf1R8ArGwwXcVV8G9vUrZzYU3KsDna5EvnAWouF-r6JMojZphVUJP9evz4h58RjKCpxQc34guaTWZk2p6CLGW0Yn5BLY53LGa0v7AhRaghhVfb_dXHKTmll0Z3vrge-xK5ovwKmnsJGqwNZSsC7CMBog9-LfwT9xg0U1GHRVgSuGUKzF_SSIE8VeCYqJRtIyJ2iiMa943eVqwVUWfgT8l38dxYHenpV1EQHEbCev8ydRKd6c5cC5_Qz0TY-H0bvCH79jUvBA5VUELdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمنا می‌کنم هر کجای این کشور نابغه پرور که هستید همین الان متوقف شید و سعی کنید یه مدت تحلیل و تفکر و کلا اینجور چیزا رو بذارید کنار ممنون.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/77684" target="_blank">📅 04:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77683">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">یه کودن زاده‌ای هم نیم ساعت پیش اینارو گفته بود ولی از شدت کصشعر دلم نیومده بود بذارم:
ما امروز جنگ با ایران را به پایان رساندیم و آنها موافقت کردند که هرگز سلاح هسته‌ای نداشته باشند، چیزی که ما بر آن تأکید داشتیم. این هدف اصلی بود.
این ۹۵٪ از هدف ما بود. و، آنها این کار را به قدرتمندترین شکل ممکن انجام داده‌اند.
ما، آه، با ایران توافق کردیم.
معامله بزرگی انجام دادیم. هیچ سلاح هسته‌ای وجود نخواهد داشت.
اه، نیروهای ما خیلی زود شروع به بازگشت خواهند کرد.
تقریباً، اه، تقریباً کامل شده است.
ما هر چیزی که می‌خواستیم را گرفتیم. نکته بزرگ این است که هیچ سلاح هسته‌ای در ایران وجود نخواهد داشت.
آنها بندی داشتند که توسعه نخواهند داد. من گفتم، «خرید چطور؟» آنها گفتند، «خب، ما آن را پوشش ندادیم.» پس دو روز بعد آنها با آن هم موافقت کردند.
ما هر چیزی که می‌خواستیم را گرفتیم.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/77683" target="_blank">📅 03:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77682">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">عرازشه ای که میگید آمریکا نباید فوتبال و سیاست رو باهم قاطی کنه پس میشه بگید دقیقا سردار آزمون چرا دعوت نشد؟
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/77682" target="_blank">📅 02:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77681">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iS3pXb_VaFnVrTxEFupfny1XmyuaaHOkqq5dLyq9nXrd6UzzhGk0tRxJX2ubtSzYCvqoI8TUbsx_1KiWgBRmuQRWmPyZ7hy17UHvhxGw0cCyazAcFitOTJxMeaYYcQD_DEpBQY1dHeDoq6_lXy0ME_tZakjj-2Kg-245ZbCkt9eq2O1CzepXpMfyT7sspbXYdezCdYrSuwKQhnIviFnPvCbxkj0XlQFyv70rYNfA6DYsJ5ugp1jP9s7kNJPelWRxEJmqb9PxeG8TJDAuvFmddEp8F9qQEdCX2JqOHNZ8h1TL4thGJy0MiUGScHQAv427s6En-iHUPRZulj4YumWXcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیست ترور بیکینی باتم اومد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/77681" target="_blank">📅 01:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77680">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">میناب انفجار
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/77680" target="_blank">📅 01:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77679">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">تسنیم: متن تفاهم تا این لحظه در مراجع ذی‌صلاح  ایران به تایید نهایی نرسیده است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/77679" target="_blank">📅 01:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77678">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">چه علاقه‌ای به گوز داری مشتی</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/77678" target="_blank">📅 01:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77677">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">بازم گوز  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/77677" target="_blank">📅 01:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77676">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">سلام فریب صدای 2تا گوز قوی از سیریک  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/77676" target="_blank">📅 01:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77675">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AanG5VCrPbir6pOHF6GSxfawc-qSOJkjq34OW9qJ9EvZ_IAXXdGjV7uJYZYCM1VjcrjajDnSQ2GYYSYKgGb5rhWtdOAUWJfp3TVWnc0AtcI1fv8wfG_mftdAe-yI9FX-NXJ_tEBhvNRtlGzU8I0OLrz65zz5hnmjI_v-JbLi2KTwmclKqHvE6SjBHC3tXzlGVQpVk6imn0isw6192S4KS-E_P4K-uBE-JtKus01fjotQ-gY-LWsvb9l2eyrMBY9c9VlLXkZSmaEAlyeRicA0kiSothfEnfipezIvwdqcjKJNVOfoOHeLwZbdVeBPfXrYsyaD3aEzdVIk-nweEdq8LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه اواکس هم داره فعالیت میکنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/77675" target="_blank">📅 01:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77674">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">پرواز سنگین جنگنده های آمریکایی برفراز عراق
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/77674" target="_blank">📅 00:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77673">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">گناوه صدای انفجار
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/77673" target="_blank">📅 00:57 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77672">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">درگیری ارتش امریکا و سپاه در خلیج فارس
تایید نشده هنوز
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/77672" target="_blank">📅 00:56 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77671">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">سلام فریب جان هم اکنون صدای توافق از خونه همسایه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/77671" target="_blank">📅 00:55 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77670">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">سلام فریب صدای 2تا گوز قوی از سیریک  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/77670" target="_blank">📅 00:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77669">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">سلام فریب صدای 2تا گوز قوی از سیریک
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/77669" target="_blank">📅 00:48 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77668">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">خبرنگار: آیا رژیم ایران عوض شده؟
دالگخیز: بله، نه یک بار بلکه دو بار
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/77668" target="_blank">📅 00:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77667">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">3 تا توافق رسان KC-135R هم از اروپا دارن میان خاورمیانه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/77667" target="_blank">📅 00:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77666">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">رسانه های مختلف خبر توافقو میدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/77666" target="_blank">📅 00:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77665">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">الان یعنی با قاتل
حضرت سید علی خامنه‌ای
💔
، قاتل خانواده‌ی رهبر جدیدمون
💔
قاتل سردار سلیمانی
💔
، قاتل سید مقاومت حسن نصرالله
💔
، قاتل شهید فقید اسماعیل هنیه
💔
، قاتل دانشمندمون محسن فخری‌زاده
💔
، قاتل سردار حسین سلامی
💔
، قاتل سردار محمد باقری غلامعلی رشید
💔
، قاتل سردار موشکیمون امیرعلی حاجی‌زاده
💔
، قاتل شهید فریدون عباسی
💔
، قاتل شهیپ محمدمهدی طهرانچی
💔
، قاتل سرلشکر شهید احمدرضا ذوالفقاری
💔
، قاتل سید امیرحسین فقهی
💔
، قاتل شهید اکبر مطلبی‌زاده
💔
، قاتل سردار سرافراز عزیزمون علی شمخانی
💔
، قاتل فرمانده بی‌بدیلمون محمد پاکپور
💔
، قاتل سرلشکر عبدالرحیم موسوی
💔
، قاتل سرتیپ عزیز نصیری‌زاده
💔
، قاتل عزیز اطلاعاتیمون اسماعیل خطیب
💔
، قاتل شهیدان غلامرضا سلیمانی
💔
و مجید خادمی
💔
، قاتل سردار سرافرازی که بر بستن تنگه اصرار داشت یعنی شهید علیرضا تنگسیری
💔
، قاتل رئیس جمهور آینده شهید بزرگوار علی لاریجانی
💔
، و قاتل شهیدان دیگر مانند محمد کاظمی
💔
، حسن محقق
💔
، داوود شیخیان
💔
، محمدباقر طاهرپور
💔
، بهنام رضایی
💔
، اسماعیل احمدی
💔
، علی‌محمد نائینی
💔
، مهدی رستمی شمستان
💔
، سعید برجی
💔
و منصور صفارپور
💔
توافق کردن؟
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/77665" target="_blank">📅 00:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77663">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ترامپ حملات امشب رو لغو کرد چون مذاکرات داره خیلی خفن جلو می‌ره و به زودی مکان و زمان امضای توافق رو هم اعلام می‌کنه: بر اساس این واقعیت که مذاکرات با جمهوری اسلامی ایران به بالاترین سطح رهبری ایران منتقل شده و تأیید شده است، من به عنوان رئیس‌جمهور ایالات…</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/77663" target="_blank">📅 23:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77662">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">☁️
✨
HappyCloud
✨
☁️
🔥
تخفیف‌های فوق خفن
🔥
فقط برای مدت محدود
💢
+
⚡
قوی • سریع • پایدار
+
🌍
مولتی لوکیشن واقعی در ۴ کشور:
🇩🇪
آلمان
🇳🇱
هلند
🇦🇹
اتریش
🇺🇸
آمریکا
+
🛜
تمامی سرویس‌ها آیپی ثابت هستند.
+
🎛️
پنل کاربری اختصاصی و حرفه‌ای
---
📦
20 گیگ | ۳۰ روزه | بدون محدودیت کاربر --->
❗
فقط ۴۹ تومن
📦
30 گیگ | ۳۰ روزه | بدون محدودیت کاربر --->
❗
فقط ۷۲ تومن
📦
50 گیگ | ۳۰ روزه | بدون محدودیت کاربر --->
❗
فقط ۹۹ تومن
📦
100 گیگ | ۳۰ روزه | بدون محدودیت کاربر --->
❗
فقط ۱۶۹ تومن
📦
150 گیگ | ۳۰ روزه | بدون محدودیت کاربر --->
❗
فقط ۲۳۹ تومن
📦
200 گیگ | ۳۰ روزه | بدون محدودیت کاربر --->
❗
فقط ۲۹۹ تومن
✅
خرید فوری از طریق بات
👇🏻
🤖
@HappySmileVPNBot</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/77662" target="_blank">📅 23:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77661">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DAA6--GJGhI9-v0Mdo3S7835oc8YpxuH6KYrS1gmHo-ZwynX4aAqjfXQxK9-keGLqlL8k_LGgJlkWvZ0gkKY0k6FVYzyOrPaKiBnf3PFfPH4eC4laXED0OA931vZRtctxSgaCXBOriigu1J1pBjNC7w7hLHJrnPKiQew16LnUi2HCxSY3mSxcCEQTzCaNY_AoG9WhWHTssd3XXzSocL4b7koTyRnV8IGSrGkD94F5vApqwtUO1b-P2JARV6zOnpWfXUd3cNQXz1_1qUrFcUx_Pf_JoNfMxaW3IIQ2cNxm5wZgw-eo3w4L39R6P4OUWTHYSNc9UG30behbX1HOxASDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انشالله بازی کشور کوردستان با مکزیک  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/77661" target="_blank">📅 23:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77660">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">انشالله بازی کشور کوردستان با مکزیک
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/77660" target="_blank">📅 23:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77659">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromcина</strong></div>
<div class="tg-text">این برای امشبه؟؟؟؟؟</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/77659" target="_blank">📅 22:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77658">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59ed6deedd.mp4?token=NAdRklOdjYWpBO8-D5---NOjzBVs_H-zbTQfWMeqfXHab66xu6-k3hJPUJyiP8zDEzXb7l1oNJj-XB6B_UK04sh9gideDxEvBuq1ryU1NYDtKWHYtX526nUFB2X5enestcco76boV2t-sqZ9lbRIW8laq2FmtsJ6twHHqwuqhdf4sn4-w0rsRj_UavV0hw9rzxEIqXCfbn99v2JkO5z7JpKEa8jy_HCYxE-Ah3PPeDyEigfvP-Nd4QpiJbYiejn5o8FSXizGQRwu4A_zVqJBJaKQcDiN0dGAv_FOugsyD9MWgDhGOPObhg1pfJyiv_4b7Er5DU7BbhKKAugelVhOhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59ed6deedd.mp4?token=NAdRklOdjYWpBO8-D5---NOjzBVs_H-zbTQfWMeqfXHab66xu6-k3hJPUJyiP8zDEzXb7l1oNJj-XB6B_UK04sh9gideDxEvBuq1ryU1NYDtKWHYtX526nUFB2X5enestcco76boV2t-sqZ9lbRIW8laq2FmtsJ6twHHqwuqhdf4sn4-w0rsRj_UavV0hw9rzxEIqXCfbn99v2JkO5z7JpKEa8jy_HCYxE-Ah3PPeDyEigfvP-Nd4QpiJbYiejn5o8FSXizGQRwu4A_zVqJBJaKQcDiN0dGAv_FOugsyD9MWgDhGOPObhg1pfJyiv_4b7Er5DU7BbhKKAugelVhOhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جدی مکزیک همیشه تو جام جهانی ها تیم قدری بوده و مدعی ها رو به دردسر انداخته  باید ببینیم این جام جهانی هم همین روند رو ادامه میدن یا نه  @FuunHipHop | Farid</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/77658" target="_blank">📅 22:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77657">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">جدی مکزیک همیشه تو جام جهانی ها تیم قدری بوده و مدعی ها رو به دردسر انداخته
باید ببینیم این جام جهانی هم همین روند رو ادامه میدن یا نه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/77657" target="_blank">📅 22:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77656">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">توووی دروازه
مکزیک گل زد
اولین گل جام جهانی
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/77656" target="_blank">📅 22:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77655">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">جام جهانی شروع شدددددد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/77655" target="_blank">📅 22:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77654">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aG0vIPWjjNz01_cgo_1V8ZBVwAVEEluIyv9YTw1UvwGbRXd0BoeL4oKbLmNm4neDZhfSssumOH3eWpYIcKTpnDMrjTemanrXAkwATkf7FS7pEv89tLGmXi14m_PRgzPhKt99A6hx_R-Tq9T1a1dsxtCRHud_bH4QdL6dpefvmtgy7MUYA6a8eTX5K_zUsQKcBbBvWSMKfT1LG8Klbpl9c9MQaNMv5XE4CCtEJtCt-qwBmCs2t0mM-v3QOI4T_XtRmQ1deaHPzzsflscWzFKI42tNyON8xt9R8eSJeC3nskjoq9hy5CIr5RtTK4bron_cjxJPBz_joTKdswAc6aNa1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مثل اینکه سخنگوی کمیسیون امنیت ملی و سیاست خارجی مجلس هنوز نمی‌دونه توافق نهایی شده:
من از نمایندگانی بودم که خلیج خارگ و نیروهای پشتیبان آن را از نزدیک دیده‌ام؛ پای ناپاک شما به آنجا نخواهد رسید و اگر بیایید، زنده باز نخواهید گشت.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/77654" target="_blank">📅 22:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77653">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ترامپ حملات امشب رو لغو کرد چون مذاکرات داره خیلی خفن جلو می‌ره و به زودی مکان و زمان امضای توافق رو هم اعلام می‌کنه: بر اساس این واقعیت که مذاکرات با جمهوری اسلامی ایران به بالاترین سطح رهبری ایران منتقل شده و تأیید شده است، من به عنوان رئیس‌جمهور ایالات…</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/77653" target="_blank">📅 22:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77652">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">دالگخیز
🔙
عمو ترامپ  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/77652" target="_blank">📅 21:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77651">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">نیویورک تایمز: امیدها برای یک پیشرفت دیپلماتیک پس از آنکه تیم ملی میانجی‌گری قطر روز چهارشنبه بدون پیشرفت در مذاکرات تهران را ترک کرد، کمرنگ شد.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/77651" target="_blank">📅 21:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77650">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ترامپ به نیویورک پست:
توافق مورد انتظار برای آغاز مذاکرات هسته‌ای با تهران «تقریباً کاملاً نهایی شده است.»
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/77650" target="_blank">📅 21:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77649">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">دیبالا هم از خودشونه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/77649" target="_blank">📅 21:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77648">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ریدم
عادل فردوسی دیبالا رو بعنوان مهمون اورده برنامش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/77648" target="_blank">📅 21:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77647">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ترامپ حملات امشب رو لغو کرد چون مذاکرات داره خیلی خفن جلو می‌ره و به زودی مکان و زمان امضای توافق رو هم اعلام می‌کنه: بر اساس این واقعیت که مذاکرات با جمهوری اسلامی ایران به بالاترین سطح رهبری ایران منتقل شده و تأیید شده است، من به عنوان رئیس‌جمهور ایالات…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/77647" target="_blank">📅 21:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77646">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ترامپ حملات امشب رو لغو کرد چون مذاکرات داره خیلی خفن جلو می‌ره و به زودی مکان و زمان امضای توافق رو هم اعلام می‌کنه: بر اساس این واقعیت که مذاکرات با جمهوری اسلامی ایران به بالاترین سطح رهبری ایران منتقل شده و تأیید شده است، من به عنوان رئیس‌جمهور ایالات…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/77646" target="_blank">📅 21:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77645">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uiIbCluIKv-ODL4PsJIi4FDMZ0IC_ur07fm7rb6Cxiwi0Z_uUUOauWU3jdNJO3GrVsp4yd5r7wlF0bDdsHP4OOlAwvda4a8eKYpawPex5Hma9bH3_MEexu12AywZd8-rywj-8mklFVszvfL_2LQGkDESC0ZHZiAI_CpSzIpHoeBirr6YK-0aWPJPzvaA2Fzu7OCWRxJufafOtEs0FIAtlgW2gee26FHT-tA4LsdIUFeKHfxlZa2T0Btnqes3pfO1YPmftuTCGfuQlO4Tlf7RVAh-G90KFH5xQp9CQv3aPeBtRXYOqLJhNukEGEQmazcjbHbrXHF4smd5ePrhOrODPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ حملات امشب رو لغو کرد چون مذاکرات داره خیلی خفن جلو می‌ره و به زودی مکان و زمان امضای توافق رو هم اعلام می‌کنه:
بر اساس این واقعیت که مذاکرات با جمهوری اسلامی ایران به بالاترین سطح رهبری ایران منتقل شده و تأیید شده است، من به عنوان رئیس‌جمهور ایالات متحده آمریکا، حملات و بمباران‌های برنامه‌ریزی‌شده علیه ایران را امشب لغو کرده‌ام.
مذاکرات و نکات نهایی، هم از نظر مفهوم و هم با جزئیات کامل، توسط همه طرف‌های درگیر، از جمله ایالات متحده، اسرائیل، عربستان سعودی، امارات، قطر، ترکیه، پاکستان، بحرین، کویت، اردن، مصر و دیگران تأیید شده است.
محاصره دریایی تا زمان نهایی شدن این معامله به طور کامل ادامه خواهد داشت — زمان و مکان امضا به زودی اعلام خواهد شد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/77645" target="_blank">📅 21:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77644">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">07. Pashmam</div>
  <div class="tg-doc-extra">Maaniac</div>
</div>
<a href="https://t.me/funhiphop/77644" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/funhiphop/77644" target="_blank">📅 20:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77643">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">06. Adama</div>
  <div class="tg-doc-extra">Maaniac</div>
</div>
<a href="https://t.me/funhiphop/77643" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/funhiphop/77643" target="_blank">📅 20:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77642">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">05. Khatereh</div>
  <div class="tg-doc-extra">Maaniac</div>
</div>
<a href="https://t.me/funhiphop/77642" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/funhiphop/77642" target="_blank">📅 20:59 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
