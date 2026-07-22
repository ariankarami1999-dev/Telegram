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
<img src="https://cdn4.telesco.pe/file/nWmmIbWfzOCvUSXZpld2h2pKB1Y1bN4nXJwkLgXsT2k60RJRIfPEcd70Vtpgx6cDvDnhLq_paLk3jYP-9HXIsnYEM6cm_0qqjj-si2kLhUe1iG10Y0ebltp4RKaQpc_CQjcwZX0ra63uHsp1Sl6lQIFZPkw76i4OZStWY4i78I2DumCql_KLsYTpSI6L56Pf8DwYZU_Ijic_cjEwn477RGs9ZI_pKRc7D3JKcWRAaHVHYMa905J4gEIwpyT5w08mTPzkFWpvOfu8ba8kQTrYznZ5aKMspjQTtrAhxnXciFGz2cv7zEaItqzmRz0WC08GFnFVhXfcoT4hWovI273xkA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.35M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-31 19:44:47</div>
<hr>

<div class="tg-post" id="msg-674202">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kHdlpIAzn4jPtZLqCblgkKn35i5TKxjnI1_1__mL5FAKmoKbVqYMHPM2vjmKJPkWzlz0IZ0icJuHCjJ2jTAt4qOu7l5Y5Q1AIRKMIiU16KGklIegb-zCyy2r_2LxTbPCeNmF4rj7r3_VrmEZnqX-gjZwOxNA9-oYFFILdhkT2w71j3RvEzguIqC4t9fYCcCmZXmf6mNNSWuYCJg1BEYudKKGxq9jOb-MTzcSIj1nBC3Q5ZsJ2GoEJorgP5U6XVFA-mMuxVORrKu_sqI6iMJA7YiPnYnEfpiVvrv790FPZnL-2qadqrBHIU__g49Xe2eNh4Xulvg9B5VxppckFhzhyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NbW0zC040mnN8Y2JCqrGlhpiLbvVSJDj1MzdURhYvkqknv8Kdkhhe_FfiYDlAJc0VUsis112O4FTUEJujHxa7qL5_iUe6gxv6jMTybblnB4V0jxsNsDej9U64O0GXsWfBWBMam2587-XMRgfotUSXOuHDFh-u248iQvABqbo5aOAT4LdekVDhjEa8UOgF60fyqLooUsB5dxQRNbKrSfSWe6TED1b7p7HMlFd34d7GbA_-UXUHOpOScTaf9i7fZopiDnnS0Pu0Io1Nt6C8F9wtAAVaY4g6y37O2CB7TRI1VciGOYX0nlWZk17w-gZSlWq2JiY0fzBSZW_GB2dZybSlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JlQFRGKKpmN7RmOyLv-La9-0I9NxLK_9zGC6OtQKlrPN5zyCcnM5pN6ibbI7foBCSrx97wT3DT_fSULVwqfrfZ0L4lTFzOwQp6i8y7DOj5PxNyo7x-7pvIEuUvOYvVPNGC6CUmKD0gw5qvAmxSzumOOW1N1oiJ7EjctzlMtDHjjWMvtvi9UPUOkTjsFx-XKpCNvueKatVKTQ9f9NTQhtQMpVtHwJ7rb9RLyBVHHNwHN-YhJdJXUzJgw6VBvfdcl1zilzOAV96RSwqTMx_fNdyy_P_uC5392HKzAN9J2IZ8p203dqY0JqgM_IqNDwK7wiVinNIjrHWffwRjt2iW7rfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ti8BZSlWXrml1tPsQMPbogPOqgRbIzVxV6z7yWzvy81aGP2VK4-cABTKEmSGENlYg_Vbw4FFu7pqeNTxF_pq-KqllJO3dHjKbmtz0naAnCm_vtxk4TjCxmpmb8HyUraYNsyrUjJH7b_i258bCFUYEZrt11xUgHRsHGz32k2JjK1rpPxYE7WopH0PoVavnysCyU32ywokBTjWvA8oIV2pbxg-OGgn7zP3Df6d7W7Dg9Rp3Qz0c8Aa5BCbxZZhw9PNxwzpQyQQPbw-MAn7axvZqVjDvmvfHqVugR5MG4Vpd3IcXkXebYJBvGDJz2dItQqgLbo5A_Dli_id_wljq4mOPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TbTZ3W9msnOGSP_UNkq3rfD5e0vwlogG7qrbT1UTa1Y0PuuMSt7yHBKJDSAT95gn7hfAr1AaE3KiO6H1_Akixo07OEmH7JugEkrMRvjNprPe_-QQnStq-qAxzqtm5VPHvR25o5Ab6s7oK17hAw_Ct4u1PROM3SvrsUfbLHWBppLI8tKMyzDpTekFf6q1kg5HODhhfNL-tVE9UBha4o1JtEMy7M0MIPJljS960SJgsEgdDxytHOE4XzWwfv8MbcFfIy_9KODLOMGxrmImj8Wn0FCwNEs60ugEaWGkE9j71z6tN997GInsODaUbLvHfSkwKm7TyZk3T-ZXt13G_nZkdw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
شهرداری تهران برنده تندیس و لوح تقدیر جایزه ملی انرژی‌های تجدیدپذیر ایران شد
🔹
شهرداری تهران در دهمین کنفرانس و نمایشگاه بین‌المللی و هفتمین دوره جایزه ملی انرژی‌های تجدیدپذیر ایران، به دلیل اقدامات مؤثر در توسعه انرژی‌های پاک، عنوان شهرداری برتر کشور در سال ۱۴۰۴ را کسب کرد و تندیس و لوح تقدیر این رویداد ملی را از آن خود کرد.
ادامه خبر
👇
https://shahr.ir/xJNm
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/674202" target="_blank">📅 19:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674201">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
اختلال جهانی در شبکه اجتماعی اینستاگرام گزارش شده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/akhbarefori/674201" target="_blank">📅 19:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674200">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
تشریح علت صدای انفجار در تهران: انهدام پهپاد متخاصم توسط پدافند هوایی
🔹
پیگیری‌ها حاکی از آن است که هیچ حمله‌ای به استان تهران صورت نگرفته است؛ صداهای شنیده‌شده در بامداد چهارشنبه، ناشی از فعالیت سامانه‌های جدید توپخانه‌ای پدافند هوایی برای انهدام یک پهپاد متخاصم بوده است./ فارس
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/akhbarefori/674200" target="_blank">📅 19:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674199">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cc6b36616.mp4?token=dtvp21Hgr4O3mMwMKN1Va_kYl1usK18X7hcCkmZil-TRGaRnGVxSXfA98aJIhfDQoncUkxgh2bu5bLZ5TsRfiUhFgzd8zzlGxRYIpE70gdhWbLzpuS5_abnaJqEx-sNiS_C15AOfKJeNU2Ap1hviXfwV65EIaLv6nnQ8tRAjvhMEbQ9lJGckZByQlgC3SjQig5FEpF91NK0X0EH7_PL1osATsCVqU2--kMZD06qWNA_0DC0AxGUvqe06irX6NO50r9vfUHDaTGmcHjcYkHvd_kVcZuJKs_WDQxfBvwj5D4_lGgorMabYf-d--okaTAIhJc8xL_kfQxo4Fzx0-8XdYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cc6b36616.mp4?token=dtvp21Hgr4O3mMwMKN1Va_kYl1usK18X7hcCkmZil-TRGaRnGVxSXfA98aJIhfDQoncUkxgh2bu5bLZ5TsRfiUhFgzd8zzlGxRYIpE70gdhWbLzpuS5_abnaJqEx-sNiS_C15AOfKJeNU2Ap1hviXfwV65EIaLv6nnQ8tRAjvhMEbQ9lJGckZByQlgC3SjQig5FEpF91NK0X0EH7_PL1osATsCVqU2--kMZD06qWNA_0DC0AxGUvqe06irX6NO50r9vfUHDaTGmcHjcYkHvd_kVcZuJKs_WDQxfBvwj5D4_lGgorMabYf-d--okaTAIhJc8xL_kfQxo4Fzx0-8XdYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویر ماهواره‌ای از حملات امروز ایران به پایگاه ملک فیصل در اردن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/674199" target="_blank">📅 19:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674198">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/271f439d8a.mp4?token=GbawAqVuBCt4qXfEgz164Wxj6wGZZwbLAlFgbWp21j739MDgMnqMVhfACqesCHC7uRdnUt9wIfpD3B1DacoFdqk2Ko6szPCLSSsAUBW9PRy3jZruL4nfDQLRNG_vQAJuOF-H8n_Ii0wmIWrXpl9dpdre8k4qFlXldIPUu1bB9dgAes0AoGdZByK-dRdSGptXorjG689BOW0Mz-c-JSkhISAsmLUajZziFeXYfHrcGo13pIEZu2NLdkWfYLHjAPJE8Y5qN9GJ5Pt9rHJu3A4hkrWfXOKB3vi4SfBuSMrWJDAD99_V44mfJ_WIzWX2c4_Vr_ISrcN6sC763OkzI-llAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/271f439d8a.mp4?token=GbawAqVuBCt4qXfEgz164Wxj6wGZZwbLAlFgbWp21j739MDgMnqMVhfACqesCHC7uRdnUt9wIfpD3B1DacoFdqk2Ko6szPCLSSsAUBW9PRy3jZruL4nfDQLRNG_vQAJuOF-H8n_Ii0wmIWrXpl9dpdre8k4qFlXldIPUu1bB9dgAes0AoGdZByK-dRdSGptXorjG689BOW0Mz-c-JSkhISAsmLUajZziFeXYfHrcGo13pIEZu2NLdkWfYLHjAPJE8Y5qN9GJ5Pt9rHJu3A4hkrWfXOKB3vi4SfBuSMrWJDAD99_V44mfJ_WIzWX2c4_Vr_ISrcN6sC763OkzI-llAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برخورد دم بوئینگ ۷۷۷ با باند فرودگاه سینسیناتی
🔹
یک فروند بوئینگ ۷۷۷ هنگام فرود در آمریکا دچار حادثه «دم‌سایی» شد و برای تعمیرات از ناوگان پروازی خارج گشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/674198" target="_blank">📅 19:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674197">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXRaffnXk0RTJJP7-Qm5wbdpo2s8ud_XiHxDqbsy0Aci5AkkKmTg6i-GtrQwm7SjFlircZaNbyfxEPgjkgnlR5wofgB5ml742iJh9wlwRRjcZKvP6O_o4K-h2MUQQt0F2F_blam6m1D22akBAI5I9KDClH3YO3Z1HxBIgCCQoX9P4qxFPT9wvSCEgumnV7xLyVpIIrsb-DG8q9vPWDzLTQfGZTPbUHqWtD05JfJPddosNogMGLK_SZyE6PpuuTr1ofS8SlmnXetEC-louEz0YnlsrquOm7elqP6E8OClg8GrparQWPtewPF9ERaBm7eHzSJccrQJdivmigBj2c92Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جهش ۱۰۰۰ درصدی سود تقسیمی پترول
🔹
مجمع عمومی عادی سالیانه شرکت گروه سرمایه‌گذاری و توسعه صنایع تکمیلی پتروشیمی خلیج فارس (پترول) برای سال مالی منتهی به ۳۱ اردیبهشت ۱۴۰۵ با ارائه گزارشی از رشد چشمگیر عملکرد شرکت و تصویب ۲۵۳ ریال سود نقدی به ازای هر سهم برگزار شد.
🔹
بر اساس گزارش مدیرعامل این شرکت از صورت‌های مالی تلفیقی، در سال مالی منتهی به ۳۱ اردیبهشت ۱۴۰۵، درآمد کل گروه پترول با رشد ۷۴ درصدی از ۲۸.۵۳ همت به ۴۹.۶۵ همت رسید. همچنین سود عملیاتی با جهش ۴۶۱ درصدی از ۱.۴۷ همت به ۸.۲۵ همت افزایش یافت و سود خالص تلفیقی شرکت در پایان سال مالی به ۱۰.۱۳ همت رسید و از زیان خارج شد.
🔹
در شرکت اصلی نیز درآمد کل با رشد ۴۲ درصدی از ۱۳.۳۰ همت به ۱۸.۹۲ همت، سود عملیاتی با رشد ۳۹ درصدی از ۱.۰۹ همت به ۱.۵۱ همت و سود خالص با رشد ۲۱۰ درصدی از ۲.۲۹ همت به ۷.۱۰ همت افزایش یافت.
🔹
حمیدرضا خلیلی، مدیرعامل پترول با اشاره به جهت‌گیری برنامه‌های شرکت اظهار کرد: تمامی اقدامات پترول با هدف کاهش شکاف میان ارزش واقعی دارایی‌های شرکت و ارزش بازار آن دنبال می‌شود.
🔹
وی افزود: تکمیل پروژه‌ها، پایان کلیه فعالیت‌های پروژه پتروشیمی صدف خلیج فارس، آغاز تولید تجاری پتروشیمی ارغوان‌گستر ایلام، عرضه اولیه سهام شرکت‌های واجد شرایط در بازار سرمایه، واگذاری دارایی‌های غیرمولد و توسعه هدفمند سبد سرمایه‌گذاری‌ها از مهم‌ترین برنامه‌های ما برای آشکارسازی ظرفیت‌های پترول و خلق ارزش پایدار برای سهامداران است.
🔹
در پایان این مجمع، مبلغ ۲۵۳ ریال سود نقدی به ازای هر سهم به تصویب رسید که در مقایسه با ۲۳ ریال سال گذشته، بیانگر رشد حدود ۱۰۰۰ درصدی سود نقدی سهامداران است.
🔹
همچنین امسال پترول مجمع عمومی سالیانه خود را حدود دو ماه زودتر از مهلت قانونی و در روز ٣١ تيرماه ١٤٠٥ برگزار کرد که این اقدام نشان‌دهنده انضباط مالی، آمادگی مناسب صورت‌های مالی و رویکرد حرفه‌ای امسال شرکت در پاسخگويي به سهامداران و بازار سرمايه است.
🔹
به اعتقاد کارشناسان بازار سرمایه، هلدینگ پترول با برخورداری از سبدی متنوع و ارزشمند شامل شرکت‌های تولیدی، پروژه‌ای و سرمایه‌گذاری، در آستانه مرحله تازه‌ای از رشد و ارزش‌آفرینی قرار دارد.
🔹
به‌نتیجه‌رسیدن پروژه‌های راهبردی، ورود ظرفیت‌های جدید به مدار تولید، عرضه شرکت‌ها در بازار سرمایه و بهینه‌سازی ترکیب دارایی‌ها می‌تواند سودآوری پترول را تقویت کرده و زمینه کاهش معنادار شکاف ارزش بازار و افزایش بازده سهامداران را فراهم سازد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/674197" target="_blank">📅 19:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674196">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vSTcWEejnEDN6amaCT14A3EW6wOAswXdJTSDvsFEIiuiafGIS95bEYipHxHT2AkzhQ1l9sRz-dq-9N7Cy8eYreX0siiCDQSedmz-qjbJooCXOrO84D1SOyRaIn9MuX3utHrOdxTKiSCP6-Uj-eGk6R3gM_EhVeSwsPSuvXCUDfC6YSiWn87KhIVHGHLmUcbY0Kr6IlA5Fe_Gq57zlcLRPplOcHlXhwZsNexSX1kDIgCs3HiNcF59MlVkv6JfxVAOp6U4HNvfcMqQuw5DhmUBBrXvjXrUlDjxrgNitbkp4-p-rJQDu5K0IMebIM3dIEYYyMfktNKVghQqDiyUnEnOyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بلغارستان در جنگ ایران رسما به آمریکا پیوست  خبرگزاری دولتی BTA:
🔹
کمیته دفاع پارلمان بلغارستان به تصویب پیش‌نویسی رأی داد که به هواپیماهای سوخت‌رسان آمریکایی اجازه می‌دهد از پایگاه هوایی در خاک این کشور، از عملیات نظامی علیه ایران پشتیبانی کنند.
🔹
واشنگتن…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/674196" target="_blank">📅 19:08 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674195">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qIsDg0Og0cylHB--WWXMXCt4R2Fe3d3LZgrX9EdEBR0NGgCdqUfeY120xDA1R5a17wcaXWObOwvB9h66cDOdAJKEl9R6DOkhIf6vDV9bQRyzECWUUqj4ZStadj-Sv0l6xuxE6NI-7csjQs9hVD4OsCtVA24eTWNE6pW8G8fPJJTra5vdQCwotRkUuGuK68I5WozrX2Ix-1QHu94GeYMT8mMgLF8S6o9lzST4JOzm0avu_YhL-fWT8AKVV-FmZztluyEb_lJdCWm0-bsiAj4Aa1PuYDX9k96YKZo_JI7SYFqCoN9bxcMGi1sZ8EHjm0ofWY5Y-CXBtIxCyOdquUMVxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افسانه‌ی «داماهی»؛ ناجیِ اسرارآمیزِ مردم جنوب از دلِ امواج
🔹
در افسانه‌های جنوب، «داماهی» ماهی عظیم‌الجثه‌ای است که چشمانش چون ماه، تاریکی دریا را روشن می‌کند. اما راز اصلی او نه در بزرگی، بلکه در نغمه‌ای جادویی است که از درونش برمی‌خاست؛ موسیقی‌ای…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/674195" target="_blank">📅 19:04 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674194">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
فرماندار بوشهر: انفجار و آتش‌سوزی در جزیره خارگ روی نداده است
🔹
حریقی که در تصاویر ماهواره‌ای مشاهده شده ناشی از مشعل‌سوزی (فلر) است.
#اخبار_بوشهر
در فضای مجازی
👇
@akhbarboushehr</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/674194" target="_blank">📅 19:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674193">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from| نَبض تهران |</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FId7PICKWZgRBsfAZegNAoZDnPUwMqgxVJW60TBRPm5CCE-gM1L53o_qabwBuFRE9aJQBI0I9tdarib0AZifVJgNBg-_qHEE5IAQLVUA6Kn3uzDUeFFa-gKPn-3L39gr8c6rUAx1eCCUc9GJZgHmdONdl_3ai1opA65MUbAeubsCwOUB484sujfLNEDCc329JNxYyNEdpEMOayitNfa1ZXL7w9gPBx9wHw7owVrpiIhuuxchEqWap09aDp67oCpXWcaGhZU3pF8fYE9_Wf4KqUw5zcFHfn2RXNgUoOv7HYk0a426xOCjnLqNK0olXruQhAJbsT88BUfa5fivZ902hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
مدیرعامل شرکت توانیر با تقدیر از مشارکت کم‌نظیر و حماسه‌آفرین مردم در بهینه‌سازی مصرف برق اعلام کرد: طی ۲۴ ساعت گذشته ( امروز ۳۰ تیرماه ۱۴۰۵)، رکورد بی‌سابقه کاهش ۱۵۲۰ مگاواتی مصرف برق در کشور به ثبت رسید که این دستاورد بزرگ، حاصل پیوستن هم‌وطنان به پویش ملی «قرار همدلی» است.
🔗
مشروح خبر
#قرار_همدلی
|
#بهینه‌سازی_مصرف_برق
#پویش_۲۵درجه_قرار_همدلی
روابط عمومی شرکت توزیع نیروی برق استان تهران</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/674193" target="_blank">📅 19:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674192">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
سی‌جی‌تی‌ان: تصاویر ماهواره‌ای نشان می‌دهند که هیچ هواپیمای آمریکایی در پایگاه هوایی العدید در قطر حضور ندارند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/674192" target="_blank">📅 18:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674191">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
رد طرح‌های آتش‌بس زمان‌دار توسط ایران
خبرنگار الجزیره در تهران:
🔹
ایران هرگونه پیشنهاد آتش‌بس با مهلت زمانی مشخص را رد می‌کند؛ از دیدگاه تهران، این وقفه‌ها تنها فرصتی برای تجدید قوای طرف مقابل است و مذاکرات باید صرفاً بر بازگشت به اجرای مفاد «یادداشت تفاهم» متمرکز باشد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/674191" target="_blank">📅 18:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674190">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
«فرار» هوش مصنوعی از آزمایشگاه و حمله به «هاگینگ فیس»
🔹
شرکت «اپن‌ای‌آی» تأیید کرد یک عامل هوش مصنوعی در حین آزمایش‌های امنیتی، از محیط ایزوله خارج شده و با دسترسی به اینترنت، به زیرساخت‌های پلتفرم «هاگینگ فیس» حمله کرده است؛ این شرکت این رخداد را «بی‌سابقه» و «هاگینگ فیس» آن را حمله‌ای کاملاً خودکار توصیف کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/674190" target="_blank">📅 18:47 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674189">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(El Nv)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CD4jHq8-4sneAnU48wumn66JWFpEvmunyAAAiMoF0NJh_lQXULJglXFuKR_r0dT2ktnayhhK36WEQ2NlwHLmrNh5f69Xda7nbNpGg_tjebLIDtVOTLW0tnp3dxR2s0i5sYNYCM96NXkRk4GF2abDv9LE6muLQBZ7J3K0CooZI9yC7_BdSEaCB11WX9wUqS2XNHRLUCh2T6g_MNaOqIZ8jYzpAIQyeglT0JY-M8ieTBcJzgFkv0kmUvrEz6RxjC_w6NFfuBym1bSQilqbwY76dV24dncwhr_jgbICiV0s-zMedkxegJxzQM1jIeYrbVrL6x0VCSSRbNCIz08kYiDlBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
برگزاری مجمع عمومی عادی سالیانه بانک شهر با حضور بیش از ۷۴ درصدی سهامداران
⭐️
«بانک شهر» با تأیید قاطع سهامداران، کارنامه موفق خود را به ثبت رساند
⬅️
مجمع عمومی عادی سالیانه بانک شهر برای سال مالی منتهی به 29 اسفندماه 1404 با حضور بیش از 74 درصدی سهامداران حقیقی و حقوقی برگزار شد و عملکرد این بانک با استقبال و حمایت گسترده سهامداران مورد تأیید قرار گرفت.
⬅️
به گزارش روابط عمومی بانک شهر، این مجمع با حضور نمایندگان بانک مرکزی، ناظر فرابورس و جمع گسترده‌ای از سهامداران برگزار شد. همچنین امکان مشاهده آنلاین این رویداد از طریق پایگاه اینترنتی بانک شهر برای سایر سهامداران فراهم بود تا روند برگزاری مجمع را به صورت زنده دنبال کنند.
🔗
مشروح خبر را
اینجا
بخوانید</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/674189" target="_blank">📅 18:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674187">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/In6AweTtJJ5PdSeubu-lBzETJ1fDSBCJ3Ae8H0Lw1Qj2NkzcstHNhzRWKrWmwqiulD_URzDLPlKz6_s1PzfRpSXsgN_EJCNWnGB6vEcLhgN-cZ-nTp33KPhkHRsBF5xpoa7y7OOSWyRVh4BXXSxNyWp1DjbZx7DcozDMljm9Uv-ZbXWNSqLopmyp67L2SWXALt_UHXJNZy3kNT-12VrfrIyWVX97H1Wqli7C5X78-7Kwm7HIGnkVHmXdlw6NZyGM-Szwy13ceYvh0MZrWLKctRmxVNl3Hs9JLN2-ORcWmYKo-E8QyKNebETc9f-WBd3zCwk608qXvuypUAlpyKdbGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گزافه‌گویی‌های خوک زرد: از این لحظه، هر زمان که ایران به یک کشتی در تنگه هرمز شلیک کند، خواه با موشک، موشک، پهپاد، یا وسیله یا سلاح دیگر، ایالات متحده یک پل یا نیروگاه واحد، اعم از نزدیک یا داخل تهران، پایتخت، را بمباران و نابود خواهد کرد #Devil
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/674187" target="_blank">📅 18:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674186">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
رایزنی برای دیدار احتمالی ترامپ و نتانیاهو
کانال ۱۲ رژیم صهیونسیتی:
🔹
گزارش‌ها حاکی از مذاکرات میان کاخ سفید و تل‌آویو برای دیدار ترامپ و نتانیاهو در هفته آینده است، اما این ملاقات هنوز رسمی نشده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/674186" target="_blank">📅 18:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674185">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
هشدار دادگستری استان تهران درباره بکارگیری استارلینک
🔹
معاونت اجتماعی و پیشگیری از وقوع جرم دادگستری استان تهران در پیامکی به شهروندان هشدار داد: نصب و راه اندازی و بکارگیری ابزارهای اینترنتی ماهواره ای، از جمله استارلینک، ممنوع بوده و مشمول مجازات قانونی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/674185" target="_blank">📅 18:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674184">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9GxqFtalZNN7Bug3Kv6Qruy_Y_QziXFES_xj3MzdnFpaR1VNXeme5fc0bHGRHuzHW2yJKwAILjeRGRNBZFoIvvxX9Wpc5Dv3HOxraQFS9wKPldjSTXA4O-7Y14L_c4lS8-lmB_qE8Zl9XPep3Fsq4lzAEnJ9EQcDAb6cGznfxhIEkd0PHnGbc1rlZqO05DaxlsTS9s5jWVU5uLPVL5CBTCBjNZJ5d0eE7SUkTwB2g50MKBlomo76BZHVAnuGxeNlB9zOm8n8yeVrQHXa_2MiSy2MayJvetDArR0DT-p7z3-C-jDtLwJ1sIgMIqLmGKmb3Ci4p0eLWdIT8NNDEwVSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افتخاری دیگر برای خانواده بزرگ فهاب بتن
🔹
شرکت فهاب بتن در آیین گرامیداشت روز ملی صنعت و معدن، از سوی سازمان صنعت، معدن و تجارت به عنوان واحد برگزیده کشوری در رشته صنایع معدنی (تولید بتن آماده) انتخاب و مورد تقدیر قرار گرفت.
🔹
این مراسم صبح روز سه‌شنبه ۳۰ تیرماه ۱۴۰۵ با حضور رئیس‌جمهور، وزیر صنعت، معدن و تجارت، جمعی از فعالان اقتصادی، کارآفرینان و نمایندگان تشکل‌های صنعتی از جمله حسین فروتن مهر مدیرعامل شرکت فهاب بتن در سالن همایش‌های صدا و سیما برگزار شد و از برترین واحدهای صنعتی و معدنی کشور تجلیل به عمل آمد.
🔹
این افتخار، نتیجه سال‌ها تلاش، نوآوری، تعهد به کیفیت و همدلی خانواده بزرگ فهاب بتن است؛ موفقیتی که با اتکا به تخصص، مسئولیت‌پذیری و اعتماد ارزشمند مشتریان و شرکای تجاری حاصل شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/674184" target="_blank">📅 18:17 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674183">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDgDA90pEJEaau8BtwEJBxMgmWM-VHm3T7r3angMvaVNvn9CpWfEUJ0RqbF-7puZjDAqJ1ayJ5qsbQlhinnBX1owXvPcOKVhsLQqTGBdp-psTohDmB8Z24ltjtTdmPhcibLF9ye7www5yeabrrELjgUG8ebTDx9EvXD-A6LmgID4Omy3U0PtIYgsSSq6RnZ9mjElw2FbYvQAVBaYDdf84qsbhaLgrBhqRjYq1mJyDds4q9iCISeVNxur5SrrwlpjGDrwfFjGkwoBZAtIeu2aLRJdYhaOwmN-nioLK6S2Wdo9c61XbJfve_TVjUmaBndNVnsgorkSprtsyKiHEqrIzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاهش شدید حمایت هواداران ترامپ از جنگ با ایران
🔹
نظرسنجی پولیتیکو نشان می‌دهد حمایت طرفداران MAGA از جنگ با ایران، تنها در دو ماه ۱۳ امتیاز کاهش یافته و از ۵۰٪ به حدود ۳۳٪ رسیده است. این تغییر ناگهانی نشان‌دهنده همسو شدن سرسخت‌ترین حامیان ترامپ با افکار عمومی آمریکا علیه هزینه‌های اقتصادی جنگ است./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/674183" target="_blank">📅 18:14 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674182">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uAQudZoh0R_xDX7hxhvs6JDGJvanVUVZB6jmQPxyZKRdo7KvyJw5MBYegjiicbY_7w9j_OgLrv6oPe98XUaRw_RMjdEzX22OWC-Dyybma4jy_fJ9GLlUk9IezbEAL8m6fUBaQvEhdPdNlQQ4p0laLkd2q2nfwokol2tGicy-xzg20D85pKlsxYgAh_6oEMEEbri1o4hULXGdK7f6ihBnZLB6R_FaGfjbT9MdHHhCOGYy7Z-Cp4J8xsw17zN2YXVGe-CU6iBt6_j6cGDtzuHcDEC1WvNvS3JkHSNxxOKq6ZNMeahXM2IYXuAi11MXyDb3T0PznATJqKwJaeIgqN_IvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش اولیانوف به موافقت انگلیس با جنگ افروزی ترامپ: کارت را با خطا شروع کردی
🔹
میخائیل اولیانوف؛ دیپلمات ارشد روسیه در واکنش به موافقت «اندی برنهام» نخست وزیر جدید انگلیس با استفاده امریکا از پایگاه‌های این کشور در جنگ افروزی علیه ایران نوشت: انگلیس بیچاره.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/674182" target="_blank">📅 18:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674181">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
نیویورک‌تایمز: اگر انصارالله یمن از تردد کشتی‌های عربستانی از طریق دریای سرخ جلوگیری کند، حدود ۴ درصد از عرضه نفت جهان از بازار حذف می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/674181" target="_blank">📅 18:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674180">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a739f4d8b6.mp4?token=RL8ufSQWWjJ8eaJ6YV51Q4LUkKHXi3OGPc7HYWuEDcHs6XYiZPLY8mO7n4wg8xdoJwebtU-ijfBWZSc9YHHTRUo0ahkrOqA-z3er3AigXo9-Oqol9CppB_ELHjgg_KfDBVSSVI-Ie4lxX2x_xd8YE3bBuGgBD9brpcrjwE36PHDltUBCWKoIyIsa5K9hxEU6jzvHziTYFzRbApFYW00epxUSf_hKPi70U31p_U4NOUSDaUnrnapo3dPzTIn6cguq6enmtHvhB_5-35iH0ZT5bbZYTriJDoh4TMsv_kOxDncD7zF7UVj5vP6eSjrNHrbDrKwx5yxjHG-JxIPPEdU3BnwqUmOOqU9RTdlyFfoZQJbftP54yCTeG0Au9djxfD3jqaa5p3ZmJlJjnn3iXr5qP36Xz2-Aaau0L6q0knmlYxp2EaRyqCrLkIvdhwbdxmhLpc4Ig0B4F92s8Xt7stU5IsFKYjGJymXj67HOeKve5Wrf5Cv8G-gGHO2T9eFybKBP6y6k7PsF3hJvVaY-UL0qBQhjbZGrQwqSd4lzTHXSmOho-l1ICckxkG-LpIEwEeXB1guX3JvGGkN9-syyySGawELZcBrTcaCPfBFHnmPi_APRw6Gc9s8Lf09iNfZEDfnsvFXUKrDLS5-2p3wqMhmQEx37Plb8D4BP7hULR1f4Xjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a739f4d8b6.mp4?token=RL8ufSQWWjJ8eaJ6YV51Q4LUkKHXi3OGPc7HYWuEDcHs6XYiZPLY8mO7n4wg8xdoJwebtU-ijfBWZSc9YHHTRUo0ahkrOqA-z3er3AigXo9-Oqol9CppB_ELHjgg_KfDBVSSVI-Ie4lxX2x_xd8YE3bBuGgBD9brpcrjwE36PHDltUBCWKoIyIsa5K9hxEU6jzvHziTYFzRbApFYW00epxUSf_hKPi70U31p_U4NOUSDaUnrnapo3dPzTIn6cguq6enmtHvhB_5-35iH0ZT5bbZYTriJDoh4TMsv_kOxDncD7zF7UVj5vP6eSjrNHrbDrKwx5yxjHG-JxIPPEdU3BnwqUmOOqU9RTdlyFfoZQJbftP54yCTeG0Au9djxfD3jqaa5p3ZmJlJjnn3iXr5qP36Xz2-Aaau0L6q0knmlYxp2EaRyqCrLkIvdhwbdxmhLpc4Ig0B4F92s8Xt7stU5IsFKYjGJymXj67HOeKve5Wrf5Cv8G-gGHO2T9eFybKBP6y6k7PsF3hJvVaY-UL0qBQhjbZGrQwqSd4lzTHXSmOho-l1ICckxkG-LpIEwEeXB1guX3JvGGkN9-syyySGawELZcBrTcaCPfBFHnmPi_APRw6Gc9s8Lf09iNfZEDfnsvFXUKrDLS5-2p3wqMhmQEx37Plb8D4BP7hULR1f4Xjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
داستان نثار عشق از جای‌جای ایران به جنوب/ پویش "قرار همدلی"، برق جنوب را پایدار نگه داشت
🔹
در شرایط خاصی که کشور با آن روبه رو ست، پیش بینی می شد که قطعی برق در جنوب هم رقم بخورد، اما پویش "قرار همدلی" و پای کار کاهش مصرف برق از جای‌جای ایران برای بقای برق جنوب، کاری کارستان کرد و در روز گذشته باعث شد فشار روی شبکه سراسری برق کمتر شود؛ اتفاقی که به گفته مسئولان، به‌ویژه برای استان‌های جنوبی که در هفته‌های اخیر با آسیب به شبکه برق و گرمای شدید روبه‌رو بودند، اهمیت زیادی داشت.
🔹
بر اساس آمار اعلام‌شده، مصرف برق کشور در ۲۴ ساعت گذشته حدود ۱۵۲۰ مگاوات کاهش یافت؛ رقمی که تقریباً معادل مصرف برق دو استان متوسط کشور در ساعت اوج مصرف است.
🔹
همراهی مردم در مدیریت مصرف برق کمک کرد تا احتمال قطعی برق در بسیاری از مناطق، به‌خصوص استان‌های جنوبی، کاهش پیدا کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/674180" target="_blank">📅 18:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674179">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
درخواست ۱۰ میلیارد دلاری پاکستان از آمریکا پس از میانجیگری در جنگ علیه ایران
رویترز:
🔹
طی درخواستی که به اسکات بسنت، وزیر خزانه‌داری ایالات متحده ارائه شده، اسلام‌آباد به دنبال ایجاد یک «تسهیلات حمایت از تثبیت مبادلات دوجانبه» بین ایالات متحده و دولت پاکستان به ارزش ۱۰ میلیارد دلار با سررسید تا پنج سال است.
🔹
در صورت موافقت، این تسهیلات ذخایر پاکستان را تقویت می‌کند، فشار بر روپیه را کاهش و وابستگی آن را به تامین مالی چندجانبه کاهش می‌دهد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/674179" target="_blank">📅 18:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674177">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jel2-IlUsIqGh7MUuatOmkbaESmBD8ZCfaHsgFV1ckVoquNEylB3_fQkC_MdyaxdzVRssqqTZuEZe7x-3Pga_h7NBFWw10FoolW67MrcXoWMBcUybQxE5jObL8Ua-ukCqV75q05nGg92I3UPd8vLuAEyKufXDGCLy2qjYaejsX1Ft7eZD-xxanD9I8msNCgeZhDBF02HFLF0QSWoYe9kcAWF8elJc7oA1MKrm_TzCggGZs4hohxp9SHAp-cLPAW_JkgLH70H1KzYznqpji4kHV4qcnTwKIs0fMF4AH1yh0BTvW2zvjSz-gdIS081jeCOFZBgavH45XTkcHfgqy2XaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
من چاق هستم یا لاغر یا متناسب؟
🔹
می‌تونید با پیدا کردن قد و وزنتون بفهمید که از لحاظ تناسب اندام در چه وضعیتی قرار دارید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/674177" target="_blank">📅 17:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674176">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/664d0747c0.mp4?token=lz4OaN_uqk0Cr4KtPj_Q7QUCq0dr2e3vUlU-hsZkux7CfX-dLCe_QCkOLEmbY8wzgJQoA0XAW2M8gvSqdFnF4JtGisKT9usmJW1xF--hil4PL4LUOtjCRcqlezHI8tRYFc6p_oCpFJVHfkbhuANHZu9C3HQlsn4ZgQzNNph48eWXktIh1EqgpCwB5NcNP-D831C87ZrsiTWTd5eJfCvYxnYxYAwwKiGrogI9m9-eoW51IuDx9-2kX_l98IUs_djAuMibKQZXxxkq4B6Vc46tohgKJ1onysvatJfrMyUxpP8tbcxNj18M1B5FjtjorZrbdM7dIfEMMY6cgsc32VakNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/664d0747c0.mp4?token=lz4OaN_uqk0Cr4KtPj_Q7QUCq0dr2e3vUlU-hsZkux7CfX-dLCe_QCkOLEmbY8wzgJQoA0XAW2M8gvSqdFnF4JtGisKT9usmJW1xF--hil4PL4LUOtjCRcqlezHI8tRYFc6p_oCpFJVHfkbhuANHZu9C3HQlsn4ZgQzNNph48eWXktIh1EqgpCwB5NcNP-D831C87ZrsiTWTd5eJfCvYxnYxYAwwKiGrogI9m9-eoW51IuDx9-2kX_l98IUs_djAuMibKQZXxxkq4B6Vc46tohgKJ1onysvatJfrMyUxpP8tbcxNj18M1B5FjtjorZrbdM7dIfEMMY6cgsc32VakNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پاسخ به تهدیدهای ترامپ از نقطۀ صفر مرزی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/674176" target="_blank">📅 17:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674175">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
یک منبع نظامی: هر پل و نیروگاهی از ایران هدف قرار بگیرد چندین زیرساخت و تاسیسات انرژی منطقه را می‌زنیم
یک منبع نظامی در واکنش به تهدید جدید ترامپ مبنی بر اینکه «اگر ایران هر کشتی را هدف قرار دهد به ازای آن یک پل یا نیروگاه از ایران را میزنیم»:
🔹
ایران در اعمال حاکمیت بر تنگه هرمز اراده فولادین دارد و به هیچوجه اجازه نخواهد داد که تنگه هرمز بار دیگر به عامل تهدید علیه ایران تبدیل شود.
🔹
عبور و مرور کشتیها از این تنگه در صورت هماهنگی با ایران و ذیل ترتیبات ایران امن خواهد بود وگرنه ایران از اراده قاطع خود برای کنترل این تنگه چشم پوشی نمی‌کند و آن را در راستای ایمنی درازمدت تنگه می‌داند./ تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/674175" target="_blank">📅 17:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674174">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
متکی: هیچ کسی بدون اذن به مذاکره نرفته است
منوچهر متکی:
🔹
ما معتقدیم چه در زمان امام شهید و چه در زمان رهبر سوم انقلاب، هیچ‌کس به مذاکره نرفته مگر اینکه اذن مذاکره را گرفته باشد.
🔹
اگر آمریکایی‌ها با حرکت جدید رزمندگان ما مواجه شوند، باید هر روز جنازه نیروهای خود را به واشنگتن بفرستند؛ در آن صورت، خود مردم آمریکا ترامپ را از کاخ سفید بیرون می‌کنند./ ایسنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/674174" target="_blank">📅 17:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674173">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
بلغارستان در جنگ ایران رسما به آمریکا پیوست
خبرگزاری دولتی BTA:
🔹
کمیته دفاع پارلمان بلغارستان به تصویب پیش‌نویسی رأی داد که به هواپیماهای سوخت‌رسان آمریکایی اجازه می‌دهد از پایگاه هوایی در خاک این کشور، از عملیات نظامی علیه ایران پشتیبانی کنند.
🔹
واشنگتن از صوفیه درخواست کرده بود تا با استقرار حداکثر هشت هواپیمای تانکر بوئینگ KC-135 و حداکثر ۲۵۰ سرباز آمریکایی با تجهیزات مرتبط در پایگاه هوایی بزمر در شرق بلغارستان بین ۲۴ ژوئیه و ۱ اکتبر موافقت کند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/674173" target="_blank">📅 17:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674172">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
سگ زرد: آمریکایی‌ها مخالف افزایش قیمت انرژی هستند نه جنگ
🔹
رئیس دولت آمریکا در مراسم نظامیان کشته شده: آمریکایی‌ها مخالف جنگ نیستند، آن‌ها مخالف افزایش قیمت انرژی هستند. #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/674172" target="_blank">📅 17:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674171">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/935ae20c44.mp4?token=d89Vgn3nvZByu5saNPjx2MMhq2ci-Y2yJMLzd7WLwiy1tHStzREPhLEpIqqvxVoEt6urZLmYPCIRw0UTDwJPnkRe5a8EpZq6eCSsHlufZUTS2NS1s0C9Vt6UpDPJ7DKkwgBZKfSrZ1ceh0pp-u-hFcWHSmJKsBM0Zt7yklVHKdSAU8PZiwM35neW-LrE2o65xWuzU0HSwAFTovRKVKZ-IEBVcUk5NML9_pIQEKQ4nmPYjbHoDxyt5sA68RkdZ071xxQtR5077WJZolheoX7UnPoBALfnhRSd5WWkmAj6RQPYZXXx-g_3QP0HhjpinQBmDzIiLBk1skQPyjoxWDhXUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/935ae20c44.mp4?token=d89Vgn3nvZByu5saNPjx2MMhq2ci-Y2yJMLzd7WLwiy1tHStzREPhLEpIqqvxVoEt6urZLmYPCIRw0UTDwJPnkRe5a8EpZq6eCSsHlufZUTS2NS1s0C9Vt6UpDPJ7DKkwgBZKfSrZ1ceh0pp-u-hFcWHSmJKsBM0Zt7yklVHKdSAU8PZiwM35neW-LrE2o65xWuzU0HSwAFTovRKVKZ-IEBVcUk5NML9_pIQEKQ4nmPYjbHoDxyt5sA68RkdZ071xxQtR5077WJZolheoX7UnPoBALfnhRSd5WWkmAj6RQPYZXXx-g_3QP0HhjpinQBmDzIiLBk1skQPyjoxWDhXUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سگ زرد: آمریکایی‌ها مخالف افزایش قیمت انرژی هستند نه جنگ
🔹
رئیس دولت آمریکا در مراسم نظامیان کشته شده: آمریکایی‌ها مخالف جنگ نیستند، آن‌ها مخالف افزایش قیمت انرژی هستند.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/674171" target="_blank">📅 17:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674170">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
وال‌استریت ژورنال: ترامپ با توافق هسته‌ای ۳۰‌ساله با عربستان موافقت کرده است
🔹
این توافق دسترسی ریاض به برنامه تاسیسات هسته‌ای غیر نظامی و احتمال ساخت تاسیسات غنی‌سازی با مشارکت شرکت های آمریکایی را فراهم می‌کند و همزمان نظارت واشنگتن بر این برنامه را افزایش…</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/674170" target="_blank">📅 17:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674169">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
اولیانوف، نماینده دائم روسیه در سازمان‌‌های بین‌‌المللی در وین: ایران درباره مذاکره جدی است، اما دیکته و ضرب‌الاجل را نمی‌پذیرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/674169" target="_blank">📅 17:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674168">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2152d3a8aa.mp4?token=u1tj55o8d9XID_WgQJJxgRO6IypOBAvLyFILa4cZh3iIusDeXtlqi7rliHAsX9hlxNWdfRDk7WiCpzcCKW18M4boWsVfRqR4d2aDEJUx93KPrceitQVaCA-xZtkCc-crrCmb7Ya1QbN4XUGKvIWvG6JswKfZlZ2dniEFjJK6SNyGihfwbQjcnf1xc4ePQfBAZhvd0a6mMzDzcIHSxsjRYtEXQfCmR5X-YVFF3W7KHTzEQN9-D-kHywD3o-K8br4nvJAwY3upgbzNZp_11o7QF0cZ8gNueEkLIwHfn0dDERaJH8ngZNj9Pm90dH2Kf5OAkh6kE1w06Tu2kbJtIqdW0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2152d3a8aa.mp4?token=u1tj55o8d9XID_WgQJJxgRO6IypOBAvLyFILa4cZh3iIusDeXtlqi7rliHAsX9hlxNWdfRDk7WiCpzcCKW18M4boWsVfRqR4d2aDEJUx93KPrceitQVaCA-xZtkCc-crrCmb7Ya1QbN4XUGKvIWvG6JswKfZlZ2dniEFjJK6SNyGihfwbQjcnf1xc4ePQfBAZhvd0a6mMzDzcIHSxsjRYtEXQfCmR5X-YVFF3W7KHTzEQN9-D-kHywD3o-K8br4nvJAwY3upgbzNZp_11o7QF0cZ8gNueEkLIwHfn0dDERaJH8ngZNj9Pm90dH2Kf5OAkh6kE1w06Tu2kbJtIqdW0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به بهای جان، پای این عهد ایستاده‌ایم
🇮🇷
#همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/674168" target="_blank">📅 17:23 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674167">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cGaTkyrVGk1LBgURzzPQ7KPy1iQBTcS570BoSzsCRfg6PCAgDX0BW-fPbJqx-LD5wVCAWBXlP0x-Sq9aTrPT8c0jpjaQEL3QKSm_argHRJqczcM0oaWE-N7x5ZnT8QoEIs-jUHyr4C639L4LEy58sNhGbYEfaUyJZGyQwpeam2us4mS9B32ph2h8v8wAYmQ7RgCtziUs84nJlO8X6zQGpOOu-uw-q85uLSH4Gg9luqjsFbQcQRq2oFn8dBuX7tUOppQcVPN5s7_hTE_biFbppMGLvl_zvGvlmmu-JJbHlMVBNkVyhyKSv4iX_ac3pd51I2wA3NEkkiQkyFs6F9n-CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان ناسا برای زندگی یک‌ساله در محیط شبیه‌سازی‌شده مریخ با حقوق ۲۸ میلیارد تومانی
🔹
ناسا برای سال ۲۰۲۶، داوطلبانی را برای زندگی یک‌ساله در محیطی کاملاً شبیه‌سازی‌شده از مریخ جذب می‌کند تا شرایط انسان را در این فضا بررسی کند.
🔹
در این طرح که پس از موفقیت گروه اول در سال ۲۰۲۴ اجرا می‌شود، علاوه بر تأمین تمام هزینه‌ها، سالانه ۱۵۰ هزار دلار (حدود ۲۸ میلیارد تومان یا ماهانه ۲.۳ میلیارد تومان) به داوطلبان پرداخت خواهد شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/674167" target="_blank">📅 17:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674166">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b9b1f8637.mp4?token=lEWOcCz4f4A9e3lrfM_FEUc0XkTVgzor3aSwu6PZpjRZ3ASetPiDxJInC89uz7tUbYxF6jqkvHq_WW7MQzexvOJZq0mvffmR8DuJf0Hd8UbZJ9sirKEongs_Irq0fHPL-PU7D9IsDfHfXKWITnjSBoR6u0RoPzU9WZzEIMylsyFAd54e99q2B4mZ5Yfd-KUdWfCCuzSoOXVVuBYASucpqtklIPtLWgRwARMgR8_bFlWGYAcprpNQTo1Utli7tNk_eeLmVl38ruk1_ajc5mjCpBtdKSdbOWde8-TklQw6Uh3_Jd-lNP0QlAb36l6eFTn1gjhZBjAlP_21THdY10LgLRYnz4KPLYxwcgv3fRNmOdxICtJprS9XyICysuihOMrULmsiNRooR6-tbr78AZM-GiX4ezfVFLrTMoHjoz-tZpdv1nnhbtcTVcbXD-3OGu3X3fbcbgWXWZrP7qly_vJU2xnkA1lc9k51FgiUwijobDhCiODlSgVQYeadMs9VyccxoAaKatPzZSRHtPSd69DTd-8XY1wJx5JueHWcWnU6NVBM3K1Mveq-PV0zht93NegLFXlmFZ9tujtzamlGPM-ZKJJ-Hwuslggx2XTKFuCtGQpt9nZNPBOPBBGNl2xyOx_aQkBIu6cAPKazG_8BqjxYQaQUMAfbk_w91Cby-goNNcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b9b1f8637.mp4?token=lEWOcCz4f4A9e3lrfM_FEUc0XkTVgzor3aSwu6PZpjRZ3ASetPiDxJInC89uz7tUbYxF6jqkvHq_WW7MQzexvOJZq0mvffmR8DuJf0Hd8UbZJ9sirKEongs_Irq0fHPL-PU7D9IsDfHfXKWITnjSBoR6u0RoPzU9WZzEIMylsyFAd54e99q2B4mZ5Yfd-KUdWfCCuzSoOXVVuBYASucpqtklIPtLWgRwARMgR8_bFlWGYAcprpNQTo1Utli7tNk_eeLmVl38ruk1_ajc5mjCpBtdKSdbOWde8-TklQw6Uh3_Jd-lNP0QlAb36l6eFTn1gjhZBjAlP_21THdY10LgLRYnz4KPLYxwcgv3fRNmOdxICtJprS9XyICysuihOMrULmsiNRooR6-tbr78AZM-GiX4ezfVFLrTMoHjoz-tZpdv1nnhbtcTVcbXD-3OGu3X3fbcbgWXWZrP7qly_vJU2xnkA1lc9k51FgiUwijobDhCiODlSgVQYeadMs9VyccxoAaKatPzZSRHtPSd69DTd-8XY1wJx5JueHWcWnU6NVBM3K1Mveq-PV0zht93NegLFXlmFZ9tujtzamlGPM-ZKJJ-Hwuslggx2XTKFuCtGQpt9nZNPBOPBBGNl2xyOx_aQkBIu6cAPKazG_8BqjxYQaQUMAfbk_w91Cby-goNNcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جنوب؛ جایی که تاریخ بارها از نو نوشته شده است
@TV_Fori</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/674166" target="_blank">📅 17:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674165">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lBrwWEHc-L7scUeVsOhZlAKCzPd7ndc9DE77shh8FYi12rryzgcS6eNKWQgfYipZ0Go5nY7UH9qu586fRBlJdNheM3AVaCZRB7isBSN3HRBU4jlmcnmNW70W5sg0b-N9yw5CWa32c5y_uaqha6qzXYrKfjluGPxuUotwILZ1SmNqmBD86Nm-xrFIn0Qxmf-sWioDQBPAeVUF8c3dikWosa-6wHpEvNFygAHv6KqsR60BdRhTqeVu2LR-MPFwU_sQfY1d17R6hmnEH442UwdwLTFAdh0mM9rrCXng85XsWBPsRDHxZk6btDobRN7d645hFFmLDeUIVFZgd8J7zct7_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راغب: ماکان پیدا نشد
🔹
مصطفی راغب با بازنشر خبر تفحص شهدای میناب، تصویر ماکانِ ایران را که هنوز پیدا نشده منتشر کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/674165" target="_blank">📅 17:14 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674164">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
کلید اولیه آزمون کارشناسی ارشد ۱۴۰۵ منتشر شد.
🔹
سفارت آمریکا در سرزمین‌های اشغالی برای شهروندانش هشدار امنیتی صادر کرد.
🔹
سازمان دریایی اروپا: کشتی‌های مرتبط با اسرائیل، آمریکا و عربستان از باب‌المندب عبور نکنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/674164" target="_blank">📅 17:11 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674163">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cb631f5b8.mp4?token=FhqsTnHLw2XcCd2KBswW435lzir_IXjJ8FHtd-__79Ofs8I1DLAmATwECPdo2MQ2nlRXRPjk5dvZeviAv5GVA31JKvUdQxgE2VIrgIi3JAbiaiDuXLy1U-ECWCUKc1JzLWMYeXVvsDitBiJ-6_ftWiXKXjm_QRoIy9ZSNioATLh_zj_WEeg0d0d32JCyH5xWEJpUxAbnQY9h5MviWseNv6MtiNLMZFhsRk9D14QCdQPR7kKo-hzCW-_g5LAfkdWuwtSBeApDgoOud1wo_sUAe3_TvN46aHGxFLs-7vgTtee3O4pwlo_7LWkF0AEm2bRLPr3eAokm_fVY6iC2vwvvzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cb631f5b8.mp4?token=FhqsTnHLw2XcCd2KBswW435lzir_IXjJ8FHtd-__79Ofs8I1DLAmATwECPdo2MQ2nlRXRPjk5dvZeviAv5GVA31JKvUdQxgE2VIrgIi3JAbiaiDuXLy1U-ECWCUKc1JzLWMYeXVvsDitBiJ-6_ftWiXKXjm_QRoIy9ZSNioATLh_zj_WEeg0d0d32JCyH5xWEJpUxAbnQY9h5MviWseNv6MtiNLMZFhsRk9D14QCdQPR7kKo-hzCW-_g5LAfkdWuwtSBeApDgoOud1wo_sUAe3_TvN46aHGxFLs-7vgTtee3O4pwlo_7LWkF0AEm2bRLPr3eAokm_fVY6iC2vwvvzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش گرفتن هواپیمای ام‌ وی-۲۲بی آسپری تفنگداران دریایی آمریکا در تمرین آموزشی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/674163" target="_blank">📅 17:08 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674162">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from| تهران روشن |</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8s999IEMBT2Zu4dz1ECh7foUXp8EeFflzbqVX2xrUpqjE5-K9YQDXrPbBHVvqSSraQcPByGn70Op9B-tYe_kw8AVDCQUj9zLQkZCnyXtg4xih6HhiFpTOMFElUkf54dAFH37B8HY-YdJNWD5ob6tWPZMHPO-H0yjNMzLdsxrrjNLJFesN5ewpNxSiTIFQoPVMV0MHwlD1Cgyvgp6mjbWTUF3DNCHzJ0b2GUKqBAiyGbBl9ZCYIdYeekqvHpNDHakSl4lpI_LSkjTR7yVnL7pPY6xXZnEH_92iqG3CDOFi3zFwOLOlGdOptG5pBMvM9NQ0nS5hL8nWs73G6vRGL8_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
رکوردشکنی تاریخی در مدیریت مصرف برق کشور؛ ثبت کاهش ۱۵۲۰ مگاواتی با «قرار همدلی» مردم
✨
مدیرعامل شرکت توانیر با تقدیر از مشارکت کم‌نظیر و حماسه‌آفرین مردم در بهینه‌سازی مصرف برق اعلام کرد: طی ۲۴ ساعت گذشته ( امروز ۳۰ تیرماه ۱۴۰۵)، رکورد بی‌سابقه کاهش ۱۵۲۰ مگاواتی مصرف برق در کشور به ثبت رسید که این دستاورد بزرگ، حاصل پیوستن هم‌وطنان به پویش ملی «قرار همدلی» است.
🔗
مشروح خبر
#قرار_همدلی
#پویش_۲۵درجه_قرار_همدلی
🆔
@tehran_roshan</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/674162" target="_blank">📅 17:08 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674160">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MVXOWjw52_DJfq0itNPbGjc-uG3lA3-CINuW63TLewcQCzXZzyncM9pIN9Q1NYF-YcnA5sX87qY74MFDhi_By5oMinPUIP80DE4Vc8ytffDkK1WHVZt9D9rRXI_pjligdqpCQHSIvrQq2uOmbYwiWP8xtr5ugoycDR8_kFD4Et2b8VhHij7CvkBRICot2nwjXfhK1nVr4MsRxP14TR2_llByA5D6wj6_ZUxcBeKiA1zQw_43TRyIB3pT6qCM-1Vxat1vhL1EqUqRP0L4A22VnMjt76-dLwYpxMsEflvIWew8Y9vqn0Iai79564AtaWzOCJ7DqO_eUfoOe4Ka6t5vCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بستنی سنتی زعفرانی ایرانی بهترین و خوشمزه ترین دسر سرد دنیا شد
🍰
🔹
فالوده شیرازی هم رتبه ۹ رو گرفته و آب‌هویج بستنی هم در جایگاه ٢١ قرار گرفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/674160" target="_blank">📅 17:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674157">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gf1SI78II9qgUTZzB0M45aQeGVjzVQ6ot36k_0LPzcunMjH67VptQm1xTpDYjZYdkrH33SkSqh_pJ6Pl3I4As4Fvem8IpJHD9u5GNslK09qNSx8DzknZ40LEvIjYi4SvBfC8-cY0DbXU2i4WCByPgct-xW7edwYmIGsRVtITAHBGdZ4csQaiwa-57riyXz-Qjo-vazWcGq62e2MiOvEYONBNAimTLDOx8YBGxpuBpVFpZI-tUcOPzr58y1HZAeCsg0OZeU4ojNsmVrHrve6Q2wuKxuevv9UNJ0kK54knSMI0KZQrrqP8MeHHWaHw1YU_driiC6rlpOxXHWlhj-xH7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebeb54b065.mp4?token=c6HOX46h3PtgLFGkS5-U1DUromA_G4Q9EBNR5_AGryVEke1H-_xd4a7bbi2Zl6mzfbcFFXWEFXy-Otzakm-yMd3yReg4XnoA-NuXCaRRhKIjvTSlezAub5uKnusNU4kdqRpgplkSVXR-OTeAZJYWVIhIodw6wbIDWGfbtnx32WMHw4FSO3fPJSEFwJoS7yPq0ynyWqmhOoB-Czc3HD4zbHKSFJbjz-1Et5xTucNeNE1YwihjbQMrwjGsYJIbE50MpMJnDohqm91HPe27vJA4Il2ko4KVAPKGuksE54BJ4avKlosWXzNz8Vvd9P6i1laFl2qlkxbWAiP7D2Z0cY0_VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebeb54b065.mp4?token=c6HOX46h3PtgLFGkS5-U1DUromA_G4Q9EBNR5_AGryVEke1H-_xd4a7bbi2Zl6mzfbcFFXWEFXy-Otzakm-yMd3yReg4XnoA-NuXCaRRhKIjvTSlezAub5uKnusNU4kdqRpgplkSVXR-OTeAZJYWVIhIodw6wbIDWGfbtnx32WMHw4FSO3fPJSEFwJoS7yPq0ynyWqmhOoB-Czc3HD4zbHKSFJbjz-1Et5xTucNeNE1YwihjbQMrwjGsYJIbE50MpMJnDohqm91HPe27vJA4Il2ko4KVAPKGuksE54BJ4avKlosWXzNz8Vvd9P6i1laFl2qlkxbWAiP7D2Z0cY0_VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهوارهای تأیید می‌کنند که یک آشیانه هواپیما در پایگاه هوایی ملک فیصل در اردن در حملات اخیر ایران مورد اصابت قرار گرفته است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/674157" target="_blank">📅 16:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674155">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6852fb7775.mp4?token=BxnQPefNbJiJpc9Vk_6BiUU9erRtE39Uz0YGsaOIsPVmfmZ44_7I0_u5WfwSgTotClmwfRIsXN29Ib0P022cbsGlitxt3hhTk1xGnzcYHsMNIVKyVVBq6UNKzsfCjz-D7whG_5jCtQq0DP9-PUBYKmEaqpE-sAy_Y3HwAfiMAiWYqb87jZzWY5a6l9Cg9XGGMNizI3EwfCmL_rY4JHUMEqzz4iMzYcEW1MDWRvCsFPOu2RJ09x3oB0il_MA08uWnrjR9iG79Q9BAmq1UXsdPk1auN9lggaZNdghmebYIQQ2hvd-Z5aibWJmTkbrarDflQh7n2jPlZr0Lb6enNxPe1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6852fb7775.mp4?token=BxnQPefNbJiJpc9Vk_6BiUU9erRtE39Uz0YGsaOIsPVmfmZ44_7I0_u5WfwSgTotClmwfRIsXN29Ib0P022cbsGlitxt3hhTk1xGnzcYHsMNIVKyVVBq6UNKzsfCjz-D7whG_5jCtQq0DP9-PUBYKmEaqpE-sAy_Y3HwAfiMAiWYqb87jZzWY5a6l9Cg9XGGMNizI3EwfCmL_rY4JHUMEqzz4iMzYcEW1MDWRvCsFPOu2RJ09x3oB0il_MA08uWnrjR9iG79Q9BAmq1UXsdPk1auN9lggaZNdghmebYIQQ2hvd-Z5aibWJmTkbrarDflQh7n2jPlZr0Lb6enNxPe1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار شکارچی: آمریکایی‌ها هر سلاحی برای جنگ جهانی سوم کنار گذاشته بودند علیه ایران بکار گرفتند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/674155" target="_blank">📅 16:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674153">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JdJBK-nCax6OqqgSJ2sAAw-DLX1k8zoab_f72cgpGn-KpkGOsTLPlGe1q_vGg31YvVQOmbtK7WAgIMbXdfPwlCtZJibJxoyVDl4SeaFh4imBnDELlak6agXC0UGrTwmGJ6VJUJtCmQDt1PBgppQH3oms8nc21wDbsLmsk9osVmB78r_x9a0BtwUwCluG9hPNAqi9KfxuMWANj5JJPAOTmLX6A0WxmSFrMHQ96W4snfUGt_kDfoFu4y6S23sWoBIEZsTw52vBhmstXNLRBfNoWY8U2n91Nw_g2b6a6JmQZ-lwoyweM4Xs0PdwuOBNIbc2H8MKNitH_u6o_ZoCgJdjmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گزافه‌گویی‌های خوک زرد: از این لحظه، هر زمان که ایران به یک کشتی در تنگه هرمز شلیک کند، خواه با موشک، موشک، پهپاد، یا وسیله یا سلاح دیگر، ایالات متحده یک پل یا نیروگاه واحد، اعم از نزدیک یا داخل تهران، پایتخت، را بمباران و نابود خواهد کرد
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/674153" target="_blank">📅 16:34 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674151">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
جزئیات تلخ آتش‌سوزی ۵ هزار هکتار از علف‌زارهای میانکاله
امید محترمی، سخنگوی سازمان مدیریت بحران کشور در
#گفتگو
با خبرفوری:
🔹
محدوده میانکاله از چهار روز اخیر تاکنون سه بار دچار حریق شده است. اولین آتش‌سوزی در روز جمعه، دومین آتش‌سوزی در روز شنبه و آخرین آتش‌سوزی هم روز گذشته اتفاق افتاده است.
🔹
۵ هزار هکتار از علف‌زارهای این محدوده به نام سازیل ( نوعی علف تالابی) دچار آسیب شد، اما به پوشش جنگلی و درخت‌های اطراف آسیب وارد نشده است.
🔹
طبق بررسی صورت گرفته علت اولیه آتش‌سوزی بی‌توجهی گردشگران و دامداران آن محدوده اعلام شده است. همچنین گرمای هوا و وزش باد شدید از دیگر عواملی است که در این بررسی شناسایی شد.
@TV_Fori</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/674151" target="_blank">📅 16:27 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674150">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15eae37357.mp4?token=mJu7dKjNS_xmBzp8LCJtvg6AvVZWaNXvki6fNh3_5D21qAGXHR4PIRcjFvmmeHZwxxMr-81FZmLzXiGko8kkGWrz7OQBLZOCVDlLdKA5RnZc9jF85Lr2-ViuxFJfbu6_atvA9kHteHUif9gblYmZ5RxOksAQ2gYAxqY3Thf6tN8-wMBoj0W37kOI3nukO56bE8eqqNC8bco3CyQlRVJ4CZo6jmxxUXLg3MBEJwS-y3JTOGWtcilho14uxInYwj1TjiRiWsTmpwAmiziQrwzQ0dG0c3mbdWPCrdtjJ-bM5GfczHMnqWTwiniuRBj8UdwOwQIZqvTGNNlfjL_bEqkdBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15eae37357.mp4?token=mJu7dKjNS_xmBzp8LCJtvg6AvVZWaNXvki6fNh3_5D21qAGXHR4PIRcjFvmmeHZwxxMr-81FZmLzXiGko8kkGWrz7OQBLZOCVDlLdKA5RnZc9jF85Lr2-ViuxFJfbu6_atvA9kHteHUif9gblYmZ5RxOksAQ2gYAxqY3Thf6tN8-wMBoj0W37kOI3nukO56bE8eqqNC8bco3CyQlRVJ4CZo6jmxxUXLg3MBEJwS-y3JTOGWtcilho14uxInYwj1TjiRiWsTmpwAmiziQrwzQ0dG0c3mbdWPCrdtjJ-bM5GfczHMnqWTwiniuRBj8UdwOwQIZqvTGNNlfjL_bEqkdBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار شکارچی: عقب‌نشینی در برابر دشمن حرام است
🔹
اطاعت از نائب امام زمان(عج) بر ما واجب شرعی است.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/674150" target="_blank">📅 16:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674148">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbfaa44a40.mp4?token=VgB_Sg2_Ltgm9Y084EFJqMNzwTGWchHg5EOoW2KLcnpTEd1zR-3osOHFMfKhQrKRxJpP8Z_tE4uqd-efRUv3EXvwwBnPi0S36ztG30Q7qaBC0Nl98rO6xoNTI4CFL42qDCCvi7DGAVB-C0uBJnbgzGKQdCewn2GRg4dmG2KvaQOPDV9mEclt5oglPwLTs_IUDuDBqa6AfVTWEENQ9Gx0vDL4dKJAFyD_96HtpxTuHooQPUWCIFmt3pM62k06jY-aRg_IJWi0rezGTSt_DwsBBG4a5lt-vAWmYD2DsAFTBgm1zdaUwjsNMs90xQlDXwiJDlzn1qpFsmwVUYG8sGezcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbfaa44a40.mp4?token=VgB_Sg2_Ltgm9Y084EFJqMNzwTGWchHg5EOoW2KLcnpTEd1zR-3osOHFMfKhQrKRxJpP8Z_tE4uqd-efRUv3EXvwwBnPi0S36ztG30Q7qaBC0Nl98rO6xoNTI4CFL42qDCCvi7DGAVB-C0uBJnbgzGKQdCewn2GRg4dmG2KvaQOPDV9mEclt5oglPwLTs_IUDuDBqa6AfVTWEENQ9Gx0vDL4dKJAFyD_96HtpxTuHooQPUWCIFmt3pM62k06jY-aRg_IJWi0rezGTSt_DwsBBG4a5lt-vAWmYD2DsAFTBgm1zdaUwjsNMs90xQlDXwiJDlzn1qpFsmwVUYG8sGezcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
لحظه بالا بردن جام قهرمانی توسط رودری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/674148" target="_blank">📅 16:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674146">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b693b8dce.mp4?token=QiQdl_iwAckLNS2yxwfYpkTsFQCtYdHq9_4AloMQDmHvzXIFTkK8umxkIZoQqQyFC1wTR4I4z_W60Uach3Z7TWdBEP_sTxniSMpUhTcmDKxbeEFhqg8cri4ILFtdTZhKbPoQ9R_B6fx_qoOL5-m1BbTHmbXu6KjMSlHvTY45lDWVNOKVbVRtJn-5U3JrKlOJ72Zt9bQnxY7iyWFdtu6O_rm0vBiIlr9EjEdr_-j7sjVJal-1HZcwsDSnNoiXXGpV3HZq5nli_-Go2HbVOMdFGjK7spy-7oLPQ-sseQu4Ja_j0H3J9vZCPlizoE1ml4OV0ywoZao3ChdvUhQOnDA2sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b693b8dce.mp4?token=QiQdl_iwAckLNS2yxwfYpkTsFQCtYdHq9_4AloMQDmHvzXIFTkK8umxkIZoQqQyFC1wTR4I4z_W60Uach3Z7TWdBEP_sTxniSMpUhTcmDKxbeEFhqg8cri4ILFtdTZhKbPoQ9R_B6fx_qoOL5-m1BbTHmbXu6KjMSlHvTY45lDWVNOKVbVRtJn-5U3JrKlOJ72Zt9bQnxY7iyWFdtu6O_rm0vBiIlr9EjEdr_-j7sjVJal-1HZcwsDSnNoiXXGpV3HZq5nli_-Go2HbVOMdFGjK7spy-7oLPQ-sseQu4Ja_j0H3J9vZCPlizoE1ml4OV0ywoZao3ChdvUhQOnDA2sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرار هواپیمای صهیونیستی در حمله ایران به بندر عقبه اردن!
🔹
رسانه‌های صهیونیستی گزارش دادند که در پی انفجارهای متوالی لحظاتی پیش در بندر عقبه اردن، یک هواپیمای غیرنظامی رژیم صهیونیستی در پی انجام این حمله از پرواز خود منصرف شده و به فرودگاه بازگشته است. …</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/674146" target="_blank">📅 16:12 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674141">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mPhhuDVtP4BYDRqhwQ-PiihBExPXood6VlfL0CkU7jEyyO237NEzLfzmGd83spnvLG-mi13GZai3sai5Am5QnKkadmUqZ7S1NSDX_d-h4ZuOttloWCDJJOoq3uEjVnpKKRHQW5nI_xT7mx6CIvwbE1BOR5UX9NJ1WOrFZdVUjXRDXUPGi67luwxpVK3qApuSlO-jdAcl6HD1xaeZWdZSFWWmdG3SX-utN9hNOTMS3A2rsLIsfkyaoANSkvzYXjcY6Wwyhlmy09YLDdLKKeEpxvYlt3PWBAaMoPtfG4MsvSrJU2kkHAGfelZDIHDrMrQsg08-QFICBzulbwOH_tGpgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WJQJkph9J6EgIxgzHR1cjYZLA-7NTK-LTBZdDkg4hINe2ybMWwlcX_ljlySI0yQFrlsNFoRPOLrrevSSX9esLG4r8US1UlhExqW9taWME6Jcg2o6SVmRzKj9YJCsNwPWV7TZgaQcThPUGjkJw5o2YBzZqX6AGg4LHrYUtZ5uV-qFLP7BxggtDhjqAZBs3NNxJltvcqxDtVR-lQgldczvDvG9tDP1moZ_4jKCcbC_t2UizRaXPqn-fs_rd0uFjAsn7EWLEBdlw4bZnYHqCT6YUwUAo332fbu6X7lmqpVIvCV3TRiQChV1a0_YBQwmBFiGloa8PHuAlxJ7K9Uair86OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GEDdSdpJ3khWzu6boL_tIhWoqcqFT0hd4S1FUw6og_XipMf9oYTc24gnNpe9xgzwF-WmiBuQG8HqzMBYLcNSVQ102DKlQUwzbl0nU8eAcONeCGCiEA1131eJQCo71MHH6gxXlw6SziPJYFUzRw7AZtC-7PxZ2e84rxFQP1t-UeBkN5lkqjKq2kx1pyCYmChXQn_ckSzYBR0_tVe_mzgXCMhCmhRF4I4k5EWkLn2TsX0eA5dyWrGbXMlIYLOWr_jJMtTkQwF2ucpyRjb1rSAX4ExusLGDnpwjjJalkUnt9lsGfkAIOWMbpgq_fneOGgLzhwKE6qn4ayKEtrH51GLjhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tLsw6NSokEbaSiHC1V32e8-QbuGD5tXGbRd7Zuf4CQPOjjXEx4xe3YofOH8gce4RGF8hG9UfDYbwRmbEUk1xhRF5sqdxvwIXNvZnPc5-R49PPyepxfHS_-ZanH8rzO1Lse8UvxgrpKhFA0HDY6_WtskWeFHcfD_54p8dlkOpBUwGLVjEYeRrVDS6f8hjZa3m7SKjS7NL33zaOIWkW_Bds9pHq2nAFVpW5PqnYTmSPzhpaPiaLbSyu-4NkWwMjR6nt-Suy-rDohY3rtGmDpfG9DAQmxTwWWK9wvKmaLAHPNBOVmQR_i7HCSzAY3eFe753woFSz8NEGuCq6-roVS_bKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lzPGvEFTXhHBgJpt-52lhsYF71uR6AaT9YzfuhK3ph49sf5FmAd2ptd5n5YbtV9OrA7Dqrk1ea4qn6U5YiW-cfP8rxVSvEld6oQa5lB6urIxdcMm2uRmAOqsq352CB3Mifl1TE25AkkPaA_D9z_vZFb9urVw8KcIKwtz0Ep7yKJxfh-gIepvauCc5ccZ-FcL-mEOCC4a137C0ppRfNHtzgA3eMxJtQOG7udauxU2xFuH1Yoevy0D96bpdmvVfdmIHJOkR0mbZ5EdBb8dOgc0XVk_UD6JPNmQaSOFJd55uu2Vt4QlLrZDoydGirbh3zhr4WR7xSsud6Kr-9gwk--X3g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اگر صاحب کسب‌وکار هستید، این فیلم‌ها رو باید ببینید
#دارایی_هوشمند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/674141" target="_blank">📅 16:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674140">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e4390107b.mp4?token=FPsaeV3ZonIpLfUSqV45GLi9d8IxBJnuavqI_SMhnfgtavLLEi8P2uHRaV27dkbYf6Cp_YmJAkRJZakejk6EANTetGwM7MLkx0TK2lISPk03hPjPLPY4AVhuYL8f4Hg1PA-gECyw8VZ93qH8HSEZJ2A5AOecT8IgGGxEsfeHC73xpD6Vab4Br-ifjhUQg-EhSeTooTe5bVVV_p8sd6puJ5HqM7ASWQu3VIHnj_FpItZp-9Dbhu55xUk5K9_kTF9eS_Hjuu3EK-cKY7IK9U8hGSPjY9DM5-oIf4H1jJB0dMSgdi3ENURxivFfyaR18BBIrxLVtQYeHKvYXHXU-zSp_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e4390107b.mp4?token=FPsaeV3ZonIpLfUSqV45GLi9d8IxBJnuavqI_SMhnfgtavLLEi8P2uHRaV27dkbYf6Cp_YmJAkRJZakejk6EANTetGwM7MLkx0TK2lISPk03hPjPLPY4AVhuYL8f4Hg1PA-gECyw8VZ93qH8HSEZJ2A5AOecT8IgGGxEsfeHC73xpD6Vab4Br-ifjhUQg-EhSeTooTe5bVVV_p8sd6puJ5HqM7ASWQu3VIHnj_FpItZp-9Dbhu55xUk5K9_kTF9eS_Hjuu3EK-cKY7IK9U8hGSPjY9DM5-oIf4H1jJB0dMSgdi3ENURxivFfyaR18BBIrxLVtQYeHKvYXHXU-zSp_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار شکارچی: با اخراج آمریکا از منطقه رژیم صهیونی محو خواهد شد  سخنگوی ارشد نیروهای مسلح:
🔹
راهبرد نیروهای مسلح اخراج آمریکا از منطقه غرب آسیاست و با اخراج آمریکا از منطقه رژیم صهیونی محو خواهد شد.
🔹
هیچ‌وقت تولید موشک و پهپاد متوقف نشده؛ حتی در طول جنگ…</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/674140" target="_blank">📅 16:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674139">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">▪️
در بحران، ترخیص سریع‌تر کالا با مشاوره استاندارد اتاق تهران
🔺
اتاق تهران با ارائه مشاوره تخصصی در حوزه استاندارد، فعالان اقتصادی را در مسیر تجارت سریع‌تر و کم‌هزینه‌تر همراهی می‌کند. آگاهی از الزامات و مقررات استاندارد، می‌تواند از توقف کالا، افزایش هزینه‌ها و تأخیر در ترخیص جلوگیری کند.
👈🏻
کسب اطلاعات بیشتر: ۳-۸۸۷۱۴۴۷۲(۰۲۱) و
www.tccim.ir</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/674139" target="_blank">📅 16:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674138">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3b7972740.mp4?token=UQ7SHiUNrtiSCOuxRGLyqyDWqNLSTonMghFb0HlNKdyY6cSNh_CkBQ5Fo0nxhW0V6QElNMHdlyyyQE0dQkgNHWevVMVmsDf0l8Qt03_jsoHcUqxTXu64JR7uOV4icXS63RNp8VLdsu_56i_i2TeV3UBzSQkE9tXTAFyDCFpp7mrQh8lBBKIgb-XedNtrXX26jpV44loyPVy6eUDZe46EJPkYJXcEO0mqmJ4YoCSvddrUIRWPOoaBikVonpmEOSdX7w9HpDc_L2zynslsySRstkp25tmyGTs3mAVg34tf2-Bl2Ary2FekpewkkdK-FRt3WekVh8DC_o8bB70UdH-vuWBUYrai9poe74OMFhYUD2pOhSvIPG_5l9Bwdy2w5HtsfHUyxItzvuYOS0gFc9Vzh0dyt1PwFt6DshvsspW13I4L_i4ZcoEbsDk5Iik1jtalb1zyw042jlDiyJTatssyHFRWDeqdb41ds0VS5n79V8KrJfH8SlHjtyfmCtZoFeY6BO1McWckYmoP55JbsUM_b7y7ZAjxSb-OKENiU8tPLnc4sVPW2H8GElBINYTXKyPn3ACrc-NZfTy7QjyBLqRtcB3AkRl2aWERZd_U-o4Co-zLOWy2-qxIU70pJE3SaN23kGVsPb_l8l4mVAZZZXZfNNq9rCyPP-LAll3uaizqpuU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3b7972740.mp4?token=UQ7SHiUNrtiSCOuxRGLyqyDWqNLSTonMghFb0HlNKdyY6cSNh_CkBQ5Fo0nxhW0V6QElNMHdlyyyQE0dQkgNHWevVMVmsDf0l8Qt03_jsoHcUqxTXu64JR7uOV4icXS63RNp8VLdsu_56i_i2TeV3UBzSQkE9tXTAFyDCFpp7mrQh8lBBKIgb-XedNtrXX26jpV44loyPVy6eUDZe46EJPkYJXcEO0mqmJ4YoCSvddrUIRWPOoaBikVonpmEOSdX7w9HpDc_L2zynslsySRstkp25tmyGTs3mAVg34tf2-Bl2Ary2FekpewkkdK-FRt3WekVh8DC_o8bB70UdH-vuWBUYrai9poe74OMFhYUD2pOhSvIPG_5l9Bwdy2w5HtsfHUyxItzvuYOS0gFc9Vzh0dyt1PwFt6DshvsspW13I4L_i4ZcoEbsDk5Iik1jtalb1zyw042jlDiyJTatssyHFRWDeqdb41ds0VS5n79V8KrJfH8SlHjtyfmCtZoFeY6BO1McWckYmoP55JbsUM_b7y7ZAjxSb-OKENiU8tPLnc4sVPW2H8GElBINYTXKyPn3ACrc-NZfTy7QjyBLqRtcB3AkRl2aWERZd_U-o4Co-zLOWy2-qxIU70pJE3SaN23kGVsPb_l8l4mVAZZZXZfNNq9rCyPP-LAll3uaizqpuU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیروز حناچی، شهردار اسبق تهران: برخی از شهردارها به تراکم‌فروشی افتخار می‌کردند/ با فروش تراکم شرایطی را فراهم کردند که تهران غیرقابل زندگی باشد
پیروز حناچی، شهردار اسبق تهران، در
#گفتگو
با خبرفوری:
🔹
در سه سال متوالی، هر سال ۳۰ میلیون مترمربع تراکم در تهران فروخته شده است. ۳۰ میلیون مترمربع پروانه در سال، معادل یک شهر ۸۰۰ هزار نفری در دل تهران است.
🔹
شهر تهران برای مردم آرامش‌بخش نیست و مثل شهروند در شهر زندگی نمی‌کنند، مثل شهرنشین زندگی می‌کنند.
#فوکوس
@TV_Fori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/674138" target="_blank">📅 15:58 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674137">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed7e731719.mp4?token=gmF45yUxHXZxm2sTaagzux20rHGKe5BIVhMoJZBFe4ODSOD2AkdKgaeOhRbOcb54X_EyZ10phhKGeB-600DHbk8figw8cdSPZKgi-QWY3APCl0FN0Ljlf1d-r4YAJ9KWEfX3q-HPfcpZ90Gb2iSw_lVsQnT3_1qhJiuSrk05U9qgppn7B7baZ5KWcxd4zIFIf4wXDI0BLBKyK9cTGYumVqV5jXvforfjAfn6FjLKGXuMAaWrZEElx6rRPlJLpzBZql_0QKgzrgVT5UJv2Ne8zn17ABIlnKTe1hy0d1XbmC3iYkSAQnPlD0YR-VN4dzJl7mAt9WzT19Hs01HjEUQz8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed7e731719.mp4?token=gmF45yUxHXZxm2sTaagzux20rHGKe5BIVhMoJZBFe4ODSOD2AkdKgaeOhRbOcb54X_EyZ10phhKGeB-600DHbk8figw8cdSPZKgi-QWY3APCl0FN0Ljlf1d-r4YAJ9KWEfX3q-HPfcpZ90Gb2iSw_lVsQnT3_1qhJiuSrk05U9qgppn7B7baZ5KWcxd4zIFIf4wXDI0BLBKyK9cTGYumVqV5jXvforfjAfn6FjLKGXuMAaWrZEElx6rRPlJLpzBZql_0QKgzrgVT5UJv2Ne8zn17ABIlnKTe1hy0d1XbmC3iYkSAQnPlD0YR-VN4dzJl7mAt9WzT19Hs01HjEUQz8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
سیر تحول توپ‌های جام جهانی؛ از چرم‌های کلاسیک تا فناوری‌های هوشمند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/674137" target="_blank">📅 15:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674135">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oaZoQlk30kM7mazaOUs5NZr4T2S7m1q1ToHDn7iYpXHfhzMDkbPIELmU-B5WUblgq7fWIUtTvPIiwmbK-wcKyvpQZjLzRxgI8aP7K_uqFJ9HANqOzRfKghV2OO642C_tMd_TyvUKd8hM5QlVghY6SvCDrNX1RkcJvdQzdvEvfUgU7mbhbOi3pj2QKxACmG0hmJ8wOHarUMWZj0NLR3DLYF8JnNzcTZ-bhccx9jl7CMFEA-Y_Z7oeRVrSTqYMAlQ3bs_jYhS4Z2Gssg4ND6nxGHeTLVy49vIp8TRTvU-JCt2Nq4WjUuYnuh0puTGU8y_LCBKj946iDMlH56bWF5FI7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنچه روی نقشه می‌بینید، اندازه واقعی کشورها نیست!
🔹
نقشه‌های رایج جهان، به‌ویژه نقشه مرکاتور، برای حفظ شکل و جهت کشورها طراحی شده‌اند؛ نه نمایش دقیق مساحت آن‌ها.
🔹
به همین دلیل، کشورهایی مانند گرینلند، کانادا و روسیه بزرگ‌تر از اندازه واقعی و کشورهای نزدیک به خط استوا مانند برزیل، هند و کشورهای آفریقایی کوچک‌تر از واقعیت دیده می‌شوند.
🔹
در این تصویر، رنگ تیره اندازه واقعی کشورها و رنگ روشن اندازه آن‌ها روی نقشه رایج جهان را نشان می‌دهد؛ هرچه به قطب‌ها نزدیک‌تر شویم، میزان این خطا بیشتر می‌شود.
آمارفکت مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/674135" target="_blank">📅 15:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674134">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b134cc9aeb.mp4?token=GjUOzKhMV-g9I9H73QzOMM_iErGoE55rIN_Q5xwnQq1lD5isGvFr7MZ802UjGDQv4rhlgwuFPLoesPkEmc5zhEOUHAwalGUUt0z2cSxxh7SIy4pRLDQ6D4z6Nlzdq1VLS-YGaUJ9IlYhX4NtQAenMGFuF9IPXR2WC6F9w9OVWCVoN4RVhLxiLHHSziFVNrn3NKXxTPeeClZHJGGUwQ9GTM2onSqGmAItzFsREu57Y4qcPoIDCc0AYZbj2P1RzeAvSUCqgtSBtR8TOvPisn4U8ROqD0G1sQ0E0mk8M3BaoqP8QcXaDsZJWj0QuTMNrgCZ-rNwaUZIzM2v1zQCZW0bMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b134cc9aeb.mp4?token=GjUOzKhMV-g9I9H73QzOMM_iErGoE55rIN_Q5xwnQq1lD5isGvFr7MZ802UjGDQv4rhlgwuFPLoesPkEmc5zhEOUHAwalGUUt0z2cSxxh7SIy4pRLDQ6D4z6Nlzdq1VLS-YGaUJ9IlYhX4NtQAenMGFuF9IPXR2WC6F9w9OVWCVoN4RVhLxiLHHSziFVNrn3NKXxTPeeClZHJGGUwQ9GTM2onSqGmAItzFsREu57Y4qcPoIDCc0AYZbj2P1RzeAvSUCqgtSBtR8TOvPisn4U8ROqD0G1sQ0E0mk8M3BaoqP8QcXaDsZJWj0QuTMNrgCZ-rNwaUZIzM2v1zQCZW0bMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار شکارچی: با اخراج آمریکا از منطقه رژیم صهیونی محو خواهد شد
سخنگوی ارشد نیروهای مسلح:
🔹
راهبرد نیروهای مسلح اخراج آمریکا از منطقه غرب آسیاست و با اخراج آمریکا از منطقه رژیم صهیونی محو خواهد شد.
🔹
هیچ‌وقت تولید موشک و پهپاد متوقف نشده؛ حتی در طول جنگ نیز این موضوع ادامه داشت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/674134" target="_blank">📅 15:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674131">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/386a38abce.mp4?token=bQAFNtXA2Xq6FHuaz3o8vUgFJUjKqw26RA0AVwSAZMHGvT7O_b3ny03LNGbS_l9-dUBXYKR120lalRaXR-6SeZJIYds1ISYulbypwS3T8TgV2VjZyvoXH6ZE2p_1YfKQOfQJv1LxVvzJnaI5KSf4lQvjVnk5tdw5EQPW54ZYpeyHMssns5m3lk3dseclcERZYlgLaxmqOxzSzUGJxQMLXBuwwh-SgCS3nIFbGFhDIyive4X1Nl2xiA0A7hhQSxRMzk_xi-7D_Z8HeVQ--BIx_kfRFeRkk5eVOdZJRh6qNoTYGHcOUsi1h2wS5jq2C557Xe5qe092QWdxeM5GMD7fiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/386a38abce.mp4?token=bQAFNtXA2Xq6FHuaz3o8vUgFJUjKqw26RA0AVwSAZMHGvT7O_b3ny03LNGbS_l9-dUBXYKR120lalRaXR-6SeZJIYds1ISYulbypwS3T8TgV2VjZyvoXH6ZE2p_1YfKQOfQJv1LxVvzJnaI5KSf4lQvjVnk5tdw5EQPW54ZYpeyHMssns5m3lk3dseclcERZYlgLaxmqOxzSzUGJxQMLXBuwwh-SgCS3nIFbGFhDIyive4X1Nl2xiA0A7hhQSxRMzk_xi-7D_Z8HeVQ--BIx_kfRFeRkk5eVOdZJRh6qNoTYGHcOUsi1h2wS5jq2C557Xe5qe092QWdxeM5GMD7fiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی ارشد نیروهای مسلح: دیتاسنتر عظیم دشمن در امارات در جنگ تحمیلی سوم نابود شد
🔹
این دیتاسنتر در طول ۲۰ سال با کمک و سرمایه‌گذاری اروپایی‌ها، رژیم صهیونی و آمریکا در امارات برای کنترل منطقه ایجاد شده بود ؛همه سرمایه‌گذاری‌های آمریکا در طول ۵ دهه در منطقه با نابودی پایگاه‌هایشان بر باد رفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/674131" target="_blank">📅 15:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674129">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
گزارش‌های رسانه‌ای و غیر رسمی از حمله به پایگاه هوایی ملک فهد حکایت دارد/ تسنیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/674129" target="_blank">📅 15:34 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674121">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
خبرنگار مستقر در تنگه‌هرمز: صدای ۳ انفجار در جزیره لارک و سیریک  شنیده شد  #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/674121" target="_blank">📅 15:12 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674119">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ddc3c5467.mp4?token=kh8tSus4dvlpzvKI351GI7BXPWNeNKUrZPv074nuv7s5ap6LnqQVdy8Wzc_7zU0GklBfW-OAWjzbTVSWFup1jUbXKeh4qNV93GXa6iqQrPJO1XvGRWJnlGGKZEpxEyi2XovuobiqO9oQNTreI-HQODwr1v-v9dtZhSmUaou1whbtjDg4Gi9QHx0GVXuLIVYTXP0nvPYjLVnyi1E5f2eWJ3TYXWQXdQvQI1d7tQa4PSEgEMPdkzY6y21zus9ljM1CbHhjPVOiPIW4ItgSL6oXaAi-2tQy1eV5jWhLktiM4Qo5zbqenghlZXnSbd_WK-4DqnYt9vdkzVeO4jdDN_W7Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ddc3c5467.mp4?token=kh8tSus4dvlpzvKI351GI7BXPWNeNKUrZPv074nuv7s5ap6LnqQVdy8Wzc_7zU0GklBfW-OAWjzbTVSWFup1jUbXKeh4qNV93GXa6iqQrPJO1XvGRWJnlGGKZEpxEyi2XovuobiqO9oQNTreI-HQODwr1v-v9dtZhSmUaou1whbtjDg4Gi9QHx0GVXuLIVYTXP0nvPYjLVnyi1E5f2eWJ3TYXWQXdQvQI1d7tQa4PSEgEMPdkzY6y21zus9ljM1CbHhjPVOiPIW4ItgSL6oXaAi-2tQy1eV5jWhLktiM4Qo5zbqenghlZXnSbd_WK-4DqnYt9vdkzVeO4jdDN_W7Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله پهپادی اوکراین به مرکز توزیع شرکت تجارت الکترونیک وایلدبریز کراسنودار روسیه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/674119" target="_blank">📅 15:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674112">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lqEZTnNAdUPU8wywHjn18gtDxZHU7C3pE4o8qiUgULTYFkJYuEkUhb_zcXH1Y-AOkOGhHpbo8XOrPbND0uTAfixsmy6-bXkk3Iat1crK5wDs_0uQ1bVor366BYbrqQnR4LXt-8yvR_l_glxSp_bC5KbxWlN9XOnkrs0Lj0XbZrginuBbAWyVAnahLiJZjjmCu37UdLpuk7UtymMGQFv3bcMNLAi0mArKKBdkJJBiK2zgPHpXELfACw4BZqqT8qf7vfkDAjA0K7IPmOHZla89LL6495CADVI4Zz6WjPJJaeLnShlsUekHKYZhwYwQgcyUgX7XmZNlI4m7OoNrawOc0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qf4Xe6Ip5rW6P-IB8O0LUmaGglIIFEM7xJyI4LSGqXbls7ILwwtDc1bN1__ifz0Kh05rMNCg1DUagSaWGg4beVTj8JBL6yzg_DWkWKio9OIFGG3Hsl7VTjmPw6PB7HF4K7xGbOHj4dAMtAi8Yl46oaWn8SWo2fE79kPp5GJwK6zm8nntLqo8lFyqLwPyAkuJ7qaEgZl-64OUfzEiuJxMk78ybRaLceuMgisSL2aQ9FYN0x1rmKpyQefg9cTbkx01gajFt8hlxryEHkJ5IZmK-tKCyNsUSxhxm7rFR65jlgNHG-YmEAeWXWsNTIQ6VDt_cHZPTia8kAQLawU1H4pfUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sapby0KbLJJvGEWecR2IbxYkasEA0Tklr3tc6hXBm01qNfqbh8wsUq7UiANFAUJa6CdrZiQlq5F3R9AwWnGMmDTlkyYuXFBQBiHWg9IxHu_cjIoh1fCG0REO1wrOzD1Yxddt1IiC3I4i8hi1ZqONvPzgfqSw1yZFws8IqAA0MHqsv51cl24whBSeEZy9ZDa_u2TTf8bIFqNwdlP4fiSDo8JeHBHnlxhlLMeY7TRMXQf6Oc9zpa6VNJ9ZJLXMW5lEbhiBlUm2tLognZVS5r7x971SlaUhrQEzTDZRhUUJl82Tb7ZfZNbqbz5WhTS1BMyXLN0VklwoYzszc8SBpptMIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IOnvPg_za2a1uM7cFzCQ1vrpwnuK_KLbh45e-fgYGvaxe8psgikc-JwHhSo5UIPOFw__QvNkcrtPpqpjbFmTajgg-yWNTk06J9e21GCER-muEsUsKG4xV0B_v5gU9TCPbNoN6rJYPp7Eyy9ljAAdG__zwqaCTQ0WcgxxJ-8YaqT-O8aameKb_ZATLe93jK7BMSuK4grIwQCSO5caPCHh0Pu3bcWO6oW-GD1RDIMkOD467yWAg3ZKXEeZkjKEgGNsTPr-SPJ0VHDf1Wz-HgqPD1g2XkRd5CK_pRCE7AJ49kGKw-4ZYmJdTW4xecWXhQHc0iOBRmWlmn8yCHJm7Na9Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DVyfJHYAGxOHZ9LXHRf7cGkdxTM6ez6LxKopsOMym-pfe68MiVgWSY7SGmgoudFIBBNy5G6LHZVFoi_PoMw_PeRmoIZW36jNcRsYpvnSkSzSXWFtkMdRWli4MHS0FcGBAYjowQgMJIVT446Phn5YJ_fAuaTOXF7Y7ooDqwjkLWvmW7AXG1udpW6FVdDc5wSG2w2bADJdQbyWMfAKn95uN7rVAAw-dQa77eD8FY8pZZrasosKqbOkhhKqRxZ1aiXOSF041rcYiOPYmk8KGcd9xf3i14xLqvLQVQkHCUUSFqHxplokPAQZrFa_tyvppULisY0o3cwgwfkfyi-EocB-3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HS5d-c9rpwlyVPpFwI5phc15XaikdmyRVUbKTRh1892Gtp1WT4ktv5A53jwgK3Lzw0Bf68m1nHBiRd49B9-CmcXPz4UgG3dNIQFZJ-gqT9r_v5k6-DhmRrV9k94Edrxqc8cqPyxuGh6NogExd5aTBpxInU1QWE_TCydamtan-vfaHarTMMYQVOMDWDQOiHCqW3JgN2dGGMgZ1SedNzlOY1Yx4mf1vBC_yootwU0hFzEtBwlERJsXOUbFSSuOzTOPoyJaFQ-g7IPT4ySXv4ZYUADqAhpLytfYxCZORxMAPQ8T_H0oH3272IV-JHMgaRj_ymrjUrqhfrF2X4b9ZwHYyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
این ترفندهای ساده، نتیجه آشپزی رو از این رو به اون رو کردن!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/674112" target="_blank">📅 15:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674110">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2309525546.mp4?token=aFi5OO_aNq1EadgBfyQLSJ3fszjxos1IC12c-JMU7B5tf_JNtyu6fcsUGGnxN010g3sH3sIcqsXaJl3EBEreAXT5zYYBQkY8VfOinH7Dvpen-S-yd8kacBGlM3Qy5dVdK8zQlLbYFAlOfXkGfaZI1ec9O0QdhZkLhX41H16BAfriVuSnyw-nUojkNfpibj4vAJ-Pij367vW3iXrz2bd0IBQ4IOtTMugkC9FVqhqfhWyajp7E3aRa8zsiLi8nhIgfhRk9cqcy3FOTlUhr3wOU4bU0b22UsUdU-6AhRt99BPTpPpxkm8tczTsDQCDLcZTewCHHeKkzRWngzdkZQSRBxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2309525546.mp4?token=aFi5OO_aNq1EadgBfyQLSJ3fszjxos1IC12c-JMU7B5tf_JNtyu6fcsUGGnxN010g3sH3sIcqsXaJl3EBEreAXT5zYYBQkY8VfOinH7Dvpen-S-yd8kacBGlM3Qy5dVdK8zQlLbYFAlOfXkGfaZI1ec9O0QdhZkLhX41H16BAfriVuSnyw-nUojkNfpibj4vAJ-Pij367vW3iXrz2bd0IBQ4IOtTMugkC9FVqhqfhWyajp7E3aRa8zsiLi8nhIgfhRk9cqcy3FOTlUhr3wOU4bU0b22UsUdU-6AhRt99BPTpPpxkm8tczTsDQCDLcZTewCHHeKkzRWngzdkZQSRBxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیروز حناچی، شهردار اسبق تهران: ۳ میلیون نفر در تهران در تاکسی‌های اینترنتی کار می‌کنند
#فوکوس
@TV_Fori</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/674110" target="_blank">📅 15:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674108">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from| نَبض تهران |</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/208a49956e.mp4?token=MJqM0hi1BprCqRYszBDECTkC3nwgU9RAI6gO2cyb5xQmyKJiVyz-68lLQDRwj6b6cxft-MM6Hjnoi-8DtvonbTnpV4NT_LiE70ZKaA5Lw4Jg1CsQoPqaBr5CnsWLubFUZiaqHDi3rYKuLmzmRdPOklKLl3c-kTZnoXc97BH5dcj16ILXj0aejygmC_pE_9MfmK71AJbSp3gstjOwr98eNIyQY-LXBNrKbwv3S2ng2Y7d2V_Np45r73iL1CcR2Dpp1fJi_LDew1qoMgVqInTMzijmgGt_F4QOjqTu_-1z3FiJrsYxa1ja5wvt2cWa0pngrEd1CS1Q_JAImSfITjuIXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/208a49956e.mp4?token=MJqM0hi1BprCqRYszBDECTkC3nwgU9RAI6gO2cyb5xQmyKJiVyz-68lLQDRwj6b6cxft-MM6Hjnoi-8DtvonbTnpV4NT_LiE70ZKaA5Lw4Jg1CsQoPqaBr5CnsWLubFUZiaqHDi3rYKuLmzmRdPOklKLl3c-kTZnoXc97BH5dcj16ILXj0aejygmC_pE_9MfmK71AJbSp3gstjOwr98eNIyQY-LXBNrKbwv3S2ng2Y7d2V_Np45r73iL1CcR2Dpp1fJi_LDew1qoMgVqInTMzijmgGt_F4QOjqTu_-1z3FiJrsYxa1ja5wvt2cWa0pngrEd1CS1Q_JAImSfITjuIXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عذرخواهی از مردم بابت خاموشی‌های مقطعی/ خاموشی برق منازل برای جلوگیری از بیکاری کارگران صنعت است
⚡️
محمدجعفر قائم‌پناه، معاون اجرایی رئیس‌جمهور: از مردم عزیز عذرخواهی می‌کنم اگر مجبوریم و در تابستان برق شما در برخی ساعات قطع می‌شود چراکه می‌خواهیم کارگری بیکار نشود و کارخانه‌ای تعطیل نشود.
#مدیریت_مصرف
|
#معاون_اجرایی_رئیس‌جمهور
#پویش_۲۵درجه_قرار_همدلی
روابط عمومی شرکت توزیع نیروی برق استان تهران</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/674108" target="_blank">📅 15:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674106">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/736cf4867e.mp4?token=InAKJ9r03GYzDxqdTUr4Ptb6INqBQBUyE9iUcW2f-FEczI6knxfRVqOoDXkR9Qqq-rXeqz9oXzvLAR_m88LAKKHKgUMYVFSuJP11ZQ7tNGs4nuLdHIxioAfDOCtyikkvF42XeayVZIqk5olTBJC3L19t149Zlsh_R9aiwmxtHMrEQOI25VS7sCZnOcPBESTEE-HSja9Tt2r_TucrKaOBmxbx1jtDXAh95we14y-dL18ug5-FCbFnCBp4KyCbYAa34psYck-AzjJJImlS5lYjfNQvFF-MgLxZnwdqMmDE3zLFIu8DSxVkG37vvdC19ScCaQ95NqgLZFAep9lVmOUOwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736cf4867e.mp4?token=InAKJ9r03GYzDxqdTUr4Ptb6INqBQBUyE9iUcW2f-FEczI6knxfRVqOoDXkR9Qqq-rXeqz9oXzvLAR_m88LAKKHKgUMYVFSuJP11ZQ7tNGs4nuLdHIxioAfDOCtyikkvF42XeayVZIqk5olTBJC3L19t149Zlsh_R9aiwmxtHMrEQOI25VS7sCZnOcPBESTEE-HSja9Tt2r_TucrKaOBmxbx1jtDXAh95we14y-dL18ug5-FCbFnCBp4KyCbYAa34psYck-AzjJJImlS5lYjfNQvFF-MgLxZnwdqMmDE3zLFIu8DSxVkG37vvdC19ScCaQ95NqgLZFAep9lVmOUOwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار مستقر در تنگه‌هرمز: صدای ۳ انفجار در جزیره لارک و سیریک  شنیده شد
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/674106" target="_blank">📅 14:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674105">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
حملهٔ سنگین سپاه به پایگاه‌های آمریکا در اردن
🔹
سپاه: حماسه حضور الهام بخش شما در خیابان می‌رود تا منشأ بیداری بزرگ ملت‌ها گردد و عرصه را بیشتر از همیشه بر مستکبران تنگ کند.
🔹
حملات تجاوزکارانه آمریکا در شب‌های گذشته به بهانه تلافی انفجار کشتی‌های متخلف…</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/674105" target="_blank">📅 14:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674094">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nxb6bu58hGJzDU4-nbjnYIQe9MvCuwrN-9ibjSJZCJ7ZXv8MzobRQi3nq-1z0SZcU3myZkpdGpp5ovfkWLTk3gmjUn0dhGpa0UsXhhZvezCt-WjWnF8iALp7-pacxmhxuTrMuK_j9UPEtvGVHfDgcMH87Yck_1B9HJQkI4MdiLMKzofGho_jA_e6s4NtW5ATX57uOWpJ_rhFu_XBQTAfsRkjkAE6ZPbT5E-IOEyOGF6-EXAPFATm0jbJPH5qqyL-BQQF-EbeoPd9zAI2omy03-_4d9kcfpSXdQc-aZPseOEpC5KP2pExmgeqjmLRkUhPmo2dwswh8HIjdLtJ6jhY-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T3FLgzU6BlUe_iy3L-Jc7l8QTkr9pP92Zs_HKgGZNhJ4TphWv6PuLYOjA6MdqB7VX4OQb-4IOIi0pSBoIRxFj6G73OxJZntzncucWM_BhHcPuNp1KRK1XC4-ZEENKQwk0u2zqNNyI8PrPywLGnDUEP61XPCyXXnyviwHowSkZob-tkvkJJU8yQ3uAMDK26SXsPLOJ4gbbD73TPCzoHouzOJ1ssQEaj7OhMUD371husn2MXOEr2TmWzeM-hk68TQ7_wQ12zfAcCkJKFJkGrBjMlBW2fWoNZao0bWxMcmLvRoT8dQFHfWj_uuhsf6nq09eg6jrbKq5dz0B3UtmEWuY9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/smsTfUikVARD_im_iTzdVkXftqHzyHteazfF-alu_AjjTuCQ6GKnC6WwDcVN3ORxmhtlY83-JoIwlBxXYw-7DisHL8ETvuqxd0giUlbWsJeCEStSa_QsaIWkLqlk_yVSuUXQSuVqVG8iGMUFdN4f5O5X0KFMf3vsN_njgOMZzNB2ZyHXhmzqVlYs63Vxc1F6IIBCQZ-ab-aAwnqG6WuzH4TOSpVG_cIXLcScWhQTs3xN3z9lAgl_eWoKshbMRc2y0OAyRBPynPcLqRPvjknOblXjjHJUb2pwarckqf9zbZlyKlFIISP4yBzH3O80ADVnq2gyeiid5EPYg25A3nU2Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SNgeABFBlU0FHwEYR626O-dllk7HHLA9mzj6_cXGouyscY1IS8ZNGedbgHehjc7LXCX9otjnfjpq-PVyroFlT04hvysJ7_W02osEbYCh1n_jFtq6jXQ_cAs060NsYteX1oe2MLEthflupvj6POKPm3-Ad-trkK5F7lbPFwv0fyuMyUmon9n0m2VsiTbQjSx4zNv1eYeu6CbcWD1OwscbK4jX1evTh4bl2l9AYsI1s1Av2y6_zPoXpisiga3GPJrbb8G8OtqHUCQlTIh3vADCXNwUCzXUENpSeWKXHAihF0qLcbQ_DZtezL9ePFkHHHyZ6r3D6g-08B_BReC2_jtS1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uQ_XBbQwLPWI-bBM0dxwGSA963tCjavrPi3IyzDHBiF27MKXr2XlHahf2afq46w3E3KrJcSaHFJ7babvPATbOcuBC_fBrxGstzODiUtVBIYG-P5l8h2xlPQUDdWYqfEMh0dj4gbxUnVJluFrVbJvTC8_hlU_1ALr0-lBVH-DzniHim19M3IzjQVzi2jSaLLczJp6MRTtXEQMxi1fhwJPMjlBI0KvCi48oNEuD6rAZ6dqI2a8kHJEl-5nyvNRtBxvjZoYI6kdoWCTV2syF1WJybdwFDnpgXWOu3ZlKtB2gyWH8WUi8KKtoO150WBs2aUQVdKDxzlCiQ2wdYNYqVtPGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f3sfsk19Mv07PTg2zwQCsVfUvobF2oPKzV38NXaSxBkG73C5vvX0LXjqhDTl1qUTj3ytehUUWrw6O0FykvWvCOscylzIWPzwF0jlTZLb-5oAAB212CmRFkrRW7U4ZfVyf5HFOO560alUaa8O1h4V38blNVbGrgW0TvEZcPWSsDvbWaMhuRGkb53--XMdpTzK-zOHNIgfuZsdpvEeUC9MNXctu4sFPfe5RLplyTdZ_UOfCkb2dXhoCAUXMIy9XGkPZ6oq42VbuiSRP31G9f9NUuxe5aT4Ss_lrQTnTrRrvYUfmug_9zzK9K1Q3Aj6JnWfbiMwOwdYAinUYrebAUXhWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IsMAF8amO23Tkagd8Nd2P-_IK-Ikpjk7ODvVjC4LDFOGDyyf3DIciXpxwCH3vT1XG05uj-Oxs6H-hkYc5CxcB3aOevXqPIvsE1so4rvUhjnqhOSI8QLHLvfVsu-uevp_I3RpJME2AdYACy1UO4jFb7JSMYSnol2UTmyS9nK93twBRslPnabPxAdU6NpnXxHnnCzxtuI3NF9xI1a_OOBCgMrp6_-3aCeKBxyxJF_ogQf0189I7c_OnxuzI-Oae_Y7saekAUpjtRnA6AxLwUroWJLD-mBQMCXGY55-oMuQL7DIoCa3IAFbAwQManK5GHshsebYrhxwVqYxFYRF8JH3YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IbN6Dj01_SB9m2gEn0qh7kJBz_oZvAJnWy402uyxg9TUEbTRk6gziw_yyM0PoZtB__90WG8qylvuEsp2BB9IWzEDv_g6k4lMQ8LaK4Pv4TQpsiXok-vrQIdRoax4t9pyyRE8Y_gIfZCulE8yF0jB-PxZxSgIOIB5dE3-cWH-4h2ceKI3rSw0uMbbyLqtiqlYOvM7q9lt4QjFSFLiK5kUHOmhc0yPGrUcSE9mGmhjVV-NHwugayWDrkBudeSS__G7l4yym4CVXJMIoK7zBer4wLK_MQwlIlT9EKDDuB5KKGMRIDX6p85SMQHjn8hxAEESH-UoY4PMlnUdP8jfQ-eYmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/snpdqlhgVABGrPOy4v-eFCVtFAHXCjBxYb42SI9Ko46Ux8TssyAgFDaLs7yiiW_J829u1SxFs312HzZY1VuAqtDWdtzFcp4IYVKDtph_V4f8Zbk5lilohiUG9-va49L9dYB_TPSTkfTxT2bBefXNj_tCD8h0oLd-fEGuB3VlvH9KiiVt8Ei47BSi-N1gRSjk8hWLYfygqCyK4d5b1zEHyeezpL3EPi0tTvcRiwzIfLwk-rQanVkS6cGjleZDeaHdEBaWB5Vj16rGIbvOOgwn5CxZ69BqRRdVZobKANaC2pJ9zDmIxbErHlxSXhABSfTYGbyrMg1CxEDhwJ1mf2WCOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qIozInR0g-eqTbCXI7aI2p332vu9shGU3hBlgUDG6QGFZUw0XkeOznkDEyC5spAE9HamSS0PMhNihK8NslJZRk2EJ8DxiCnlHZ26GrBkPQ1Om4I9pxAEU2gRP5Xtyrn8JPmfK1qC3zl2b-aQeQSg1kzwUGVz5jS8lkb8kgKiBuEFoCiNnC5QkkfyUno_IJjbHcBO6EEqBiP1tq9MxHYw8o6tqElCLZ3mtCNU929C786I_JtQkARYr50UZf2dvYsG3qcPcbrNdm7zzx5Y5Mtf_Oau8DKTK6fFhwTmOnTZic5iDEbfITYY3qTjdHjWbEUkgyLBDsdAqf3JM7oJhBfT0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حذف ترامپ و اینفانتینو از عکس قهرمانی اسپانیا با هوش مصنوعی
🔹
فدراسیون فوتبال اسپانیا با استفاده از هوش مصنوعی، تصویر دونالد ترامپ و اینفانتینو را از عکس دسته‌جمعی قهرمانی حذف کرد که با واکنش و افشاگری کاربران فضای مجازی روبرو شد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/674094" target="_blank">📅 14:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674091">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3108cde4ff.mp4?token=AyS_EYEpJQtRL3T2VY75TI2NHVcKyX7BfSP0fTiMmMDr3k3BloGAzY6C652G8apw1BC9w-PYLE6u_aZKccVDIuxCn6fMzyfHqzoA628uDD4ZtKUH9iDjMUkhy_ofJ6-KzzjjSGpSFTC8KY9_aH2VVRuNDxsd59Qk6zR_oaGODMvBeGhV0m4OWmez3mzxXsagQCT8ZEdLiCF1dak1lRZUqSgu1BWOxZ9Gz4tZXXXeSgf-hGrPAEKZChUlzQPJCffR3GET3ThOGyfAlYFexYoxdjv9hiufETEbB-kyWvRM2UeySoG1jfUNX5gC4HQbxlRFOGoZs_NOVQ_nZ5tkRrUQKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3108cde4ff.mp4?token=AyS_EYEpJQtRL3T2VY75TI2NHVcKyX7BfSP0fTiMmMDr3k3BloGAzY6C652G8apw1BC9w-PYLE6u_aZKccVDIuxCn6fMzyfHqzoA628uDD4ZtKUH9iDjMUkhy_ofJ6-KzzjjSGpSFTC8KY9_aH2VVRuNDxsd59Qk6zR_oaGODMvBeGhV0m4OWmez3mzxXsagQCT8ZEdLiCF1dak1lRZUqSgu1BWOxZ9Gz4tZXXXeSgf-hGrPAEKZChUlzQPJCffR3GET3ThOGyfAlYFexYoxdjv9hiufETEbB-kyWvRM2UeySoG1jfUNX5gC4HQbxlRFOGoZs_NOVQ_nZ5tkRrUQKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حملهٔ سنگین سپاه به پایگاه‌های آمریکا در اردن
🔹
سپاه: حماسه حضور الهام بخش شما در خیابان می‌رود تا منشأ بیداری بزرگ ملت‌ها گردد و عرصه را بیشتر از همیشه بر مستکبران تنگ کند.
🔹
حملات تجاوزکارانه آمریکا در شب‌های گذشته به بهانه تلافی انفجار کشتی‌های متخلف انجام می‌شد.
🔹
شب گذشته هم که با وجود وسوسه خدمه کشتی‌ها، هیچ شناوری جرات آزمون عبور از مسیر غیرقانونی جنوب تنگه را نکرد، و طبعاً انفجاری هم رخ نداد، ارتش کودک‌کش آمریکا خوی تجاوزگری را کنار نگذاشت و حمله هوایی و موشکی به تعدادی از مراکز نظامی و غیرنظامی ما را تکرار کرد و اینک در حال دریافت پاسخ‌های کوبنده است.
🔹
با توکل به خدای متعال، رزمندگان شجاع هوافضای سپاه در پاسخ به تجاوزات دشمن در موج ۲۵ عملیات نصر ۲ با رمز مبارک یا حسن ابن علی (ع) و تقدیم به شهدای مدرسه شجره طیبه میناب، پایگاه‌های آمریکایی در اردن را یک بار دیگر در هم کوبیدند.
🔹
در اولین مرحله پاسخ در حمله موشکی و پهپادی به پایگاه‌های ملک فیصل و پرنس حسن یک سوله آماده سازی اف ۱۵ هدف قرار گرفت و همچنین در حمله به یک سوله آماده‌سازی پهپادها، هشت پهپاد MQ 9 نو و آکبند در بسته‌های خود قبل از آماده‌سازی به طور کامل منهدم گردید و به دو فروند از آنها که در محوطه بودند خسارت سنگین وارد آمد.
🔹
در حمله بعدی به سوله نگهداری بالگردها خسارت اساسی به دو فروند بالگرد سنگین آمریکایی وارد آمد.
🔹
در حمله به یک مرکز اسکان نیروهای متجاوز، تعدادی از آنها کشته و زخمی شدند.
عملیات تنبیه متجاوز ادامه دارد، چرا که اگر متجاوز تنبیه نشود و هزینه سنگینی بابت عهد شکنی و زیر پا گذاشتن توافقات نپردازد، تصور خواهد کرد که هر وقت اراده کند می‌تواند جنگ را از سر گیرد و هر وقت تحت فشار قرار گیرد به آن خاتمه دهد و چرخه جنگ، مذاکره و باز هم جنگ را تکرار کند و سایه جنگ را دائماً روی سر ما نگه دارد.
🔹
تنها راه احیای بازدارندگی و برقراری امنیت پایدار، اجرای فرمان قرآن است که می‌فرماید "و قاتلوهم حتی لا تکونوا فتنه".
🔹
برای دور کردن دائمی سایه جنگ از کشور جز ایستادگی و تحمیل هزینه سنگین به متجاوز راهی نیست اگر این پاسخ‌ها اکتفا نکند و تجاوزات ادامه یابد، آماده عملیات پشیمان‌کننده‌ای می‌شویم که اعلام عزای عمومی در آمریکا را به دنبال خواهد داشت.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/674091" target="_blank">📅 14:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674090">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
آشپزی با چشم بسته روی آنتن زنده شبکه سه!/ مهارت عجیب یک سرآشپز همه را شوکه کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/674090" target="_blank">📅 14:17 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674088">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43629cc089.mp4?token=uPJ6RCxTnvN1d4aNAWJwIAA8yycQnQO1XPPEnsCT1GJzYY_GHVALlqKAyX5wCn9txewApHLmdLS0L-PPnr2sQZrDE8noXlF2M_hGN697Ex4wgazAVFTNhEbxYNfcyX9a-EXe47zMfFYP1vaVaPqmAIoc1zyM2QyIgp1F3LsYKP2IBxLgXR9lyQVkWe1_0YLKfTtR08mxiZNScWvQqRrKQZrs-1Fqdtm-Skr9F4N9CLQc4KGoX4KweN-OKFuG2Ea2vvsW_YVkuGwHv9azjtEkT86OfZ3-6pfiAi6wzbIkjedcFCqjyLAS_bq3eQO53gaE3ueip47ASSiOohIxvnE8Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43629cc089.mp4?token=uPJ6RCxTnvN1d4aNAWJwIAA8yycQnQO1XPPEnsCT1GJzYY_GHVALlqKAyX5wCn9txewApHLmdLS0L-PPnr2sQZrDE8noXlF2M_hGN697Ex4wgazAVFTNhEbxYNfcyX9a-EXe47zMfFYP1vaVaPqmAIoc1zyM2QyIgp1F3LsYKP2IBxLgXR9lyQVkWe1_0YLKfTtR08mxiZNScWvQqRrKQZrs-1Fqdtm-Skr9F4N9CLQc4KGoX4KweN-OKFuG2Ea2vvsW_YVkuGwHv9azjtEkT86OfZ3-6pfiAi6wzbIkjedcFCqjyLAS_bq3eQO53gaE3ueip47ASSiOohIxvnE8Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیروز حناچی، شهردار اسبق تهران: اگر هاشمی نبود، قطعنامه ۵۹۸ پذیرفته نمی‌شد/ هاشمی رفسنجانی از معدود روحانیونی بودند که پیش از انقلاب، با هزینه شخصی
جهانگردی کرده بودند و به همین دلیل طرح‌هایی مانند مترو را وارد ایران کردند
پیروز حناچی، شهردار اسبق تهران، در
#گفتگو
با خبرفوری:
🔹
در باب جریان‌هایی مانند جبهه پایداری، حدیثی از امام جعفر صادق (ع) داریم؛ ایشان از حضرت امیر (ع) نقل می‌کند که دو طیف کمر مرا شکستند؛ عابدانِ متهتک و جاهلانِ متنسک؛ عابدانی که هتک حرمت می‌کردند و جاهلانی که به قول معروف جانماز آب می‌کشیدند، ولی ریشه می‌زدند.
#فوکوس
@TV_Fori</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/674088" target="_blank">📅 14:08 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674087">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/324cb6ed71.mp4?token=kSb4PpoaP2YyocGmLS4KGRIWxAdDXQ_2jK2FOCCppHmHT2MazZoOM7apri-1ATnIlDGAxUxyVM9UC6cSfyEuABcnGAf2YE2t72xsWP_DAM4_3hvDCDj0wDyzoZ0X29VSCk3hBjt5qxkf_XmBsfDULvMii8A0dT4x0qiIHSU0KKKVtTdwi9FZaW30lWs7cdhsMOrvkHfiFbgxHG9AgQp-0O_SAEBqQLimkXS_QVtLkmx2x9GdA_xqXWn7N_qWiB5P840uLrLil2cQ6KfQvldFoHK6LBuTpPB2FxIl9xcIzgfIuxyfAFfaQto404QUJgsQO1SnC-2gDqU1eZ2oFR7lrWG30lESzTmZucsrYpZ0HdH9WQ90uRpjXDBpKY9jffk-YeE7djT2ijsyYrdK8f2dXBGhUPtoYVRyrEXEnOx1LU5BVzTLVgFod-DBcaX9XXhQnUf65wpnFrzoRAi9H9TkPMzida9t0u_ymBU0I6oglqWjmKC6VfGL10KEj4pMNf-xLwuK5EwDOXmnEMTBXlrXfJvN0jVlx9zlG1Wpp3S7B0_M9sZMDuXweyBgQAJRK_Qi5hE6oFGecsGoAnzk-ATNE41MH24lo4OM1taSt1lXEIV4rNT3_KJo7yeh46nf9lsSxzhlw_p2AxnvT_geuHaKZzB9dOA8bfICx0_UGey5Z1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/324cb6ed71.mp4?token=kSb4PpoaP2YyocGmLS4KGRIWxAdDXQ_2jK2FOCCppHmHT2MazZoOM7apri-1ATnIlDGAxUxyVM9UC6cSfyEuABcnGAf2YE2t72xsWP_DAM4_3hvDCDj0wDyzoZ0X29VSCk3hBjt5qxkf_XmBsfDULvMii8A0dT4x0qiIHSU0KKKVtTdwi9FZaW30lWs7cdhsMOrvkHfiFbgxHG9AgQp-0O_SAEBqQLimkXS_QVtLkmx2x9GdA_xqXWn7N_qWiB5P840uLrLil2cQ6KfQvldFoHK6LBuTpPB2FxIl9xcIzgfIuxyfAFfaQto404QUJgsQO1SnC-2gDqU1eZ2oFR7lrWG30lESzTmZucsrYpZ0HdH9WQ90uRpjXDBpKY9jffk-YeE7djT2ijsyYrdK8f2dXBGhUPtoYVRyrEXEnOx1LU5BVzTLVgFod-DBcaX9XXhQnUf65wpnFrzoRAi9H9TkPMzida9t0u_ymBU0I6oglqWjmKC6VfGL10KEj4pMNf-xLwuK5EwDOXmnEMTBXlrXfJvN0jVlx9zlG1Wpp3S7B0_M9sZMDuXweyBgQAJRK_Qi5hE6oFGecsGoAnzk-ATNE41MH24lo4OM1taSt1lXEIV4rNT3_KJo7yeh46nf9lsSxzhlw_p2AxnvT_geuHaKZzB9dOA8bfICx0_UGey5Z1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تیزر قسمت نهم از فصل پنجم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ خانم حدیث ایران‌منش که به دلیل داشتن ۲ فرزند، قصد سقط کردن سومین فرزند ناخواسته خود را داشته اما با اصرار اطرافیان او را نگه می‌دارد ولی بلافاصله بعد از زایمان به بیماری کرونا مبتلا و روح از جسم جدا شده و مدت زیادی را در کما به سر می‌برد و مسائل زیادی را در دنیای برزخی درک می‌کند و در نهایت بخاطر انصراف از سقط و جان بخشی به فرزندش، خداوند جان دوباره به ایشان می‌بخشد را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: حدیث ایرانمنش
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/674087" target="_blank">📅 14:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674078">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MwbFBLTjSJR_oZ42Zl8TglIq1hvHvGfGjqhCkMU2eNwIVg12Y6H09EpfBmzz8xxKtnKAr2FAqVVyn9IdkAeTuvgDhb0kLZ8CuXwzW_XLKu6klMlAMQW4iRyPWwoJrrEx7gvBQnnyPbOhxriKCtUF43XtSQUKUgYf6TVnA5uTURScGLVK0ZT8kRWXM4WpADgy5W0Rv7E19x_xcvPUeHNxjZcM1nCr1E4JXZtGjy7L_hJix3EC_xeXV6Pn4Ao6-io-4eLzC898vT3a_SQk735ygLQFwdSmjPQ7Dq__XdrouVn5Tx4bDgrgT3csgfw1LufdfIrlu3RDy_Fn9UeUcS-kXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dLvtLyr4tC-obhO-_48KljUdRkFF0UJD5XyBW6nQiH45ppIiJMbd5gGboBwKUMHOGDjLrowr8sMPQJhPweuDdXh1MiL4oJz_LtRRzDYlddt_Fo1zzxBOdkaGY31tNaMcauUF_Gviv836fWb6UAOUUgxhrNGWHSMnk2aBEZIzoDdnHNGlbdIR6I25m2L3UXyb7v747aCQcnUoubq9pZeesw-YBjpVUpE7KTXqOilfZ9w_pukM3r_2cGZJd2N-0lqJECw5BqDFz6SNoRvDLG0iihLRv9sbK73OFHN_dgr4RgJOMJiANAjbmGsW_DEabl8jny12MJl2oZOxNW5AkiHDjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CKBskwL_xXCw1bqgy4BPkZhXS77dQXu6GOsk56dJBOQYNwmjXNn3z6Ql1Gbl1iYxwV-PPI0nDB168JFS_qw_jocSNpdoe-gJ2g9h23YGc_EKKDkPY4J5BF556ejxCHkpQUh6tUAXY0w8XuVQ55KxF3oVDaVedS7WUxsOEKcoZzztl8GL-mK4H87TYvm4XdeKcUgBDCs1N0n04f9D8UUhrX7R8MS9LQ-Ut14uk1sYRQ1B_QJBWlrjcPSuXDMZsj_V1FbnQGpSRsNYgaxnXmgA3w7TWgM0eXn3sd5Orf2ouNXu0Uvv-UrFD43ejtuY6eTpqAuEV3IX70dPg6nbrNQC0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kIFTnn77iMIayr3Eu5meegQ3jdDDjJv3r40FAVLDvfz_1hOqsUjn2S57cvgkTw8GNrO4cmB7tSzY37VwNhnl0ee04QyCgEUTtjQvBn2frlKLq--FdCWhk_R9PQdt-rxK5viCorGfkhJOiJjrwUd2Ej6fizh84s52-qmZZTNxIoMkZiEpaLIDbUWclQ-daI3zBnerTqWL3BWaQG7vOmsYYRoZtT2rP4DRI2EbHKMpv0ANCBy_f9RUqxQfxz5gyS6UBpW_gEucopu9mnIq8XqfIzgBdAKwpNXVmByGtZHoIurVwxRYeW9Mv4SYTWqi2YUKeZh1qUk-8AqAJ9msLLMLCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nx9BjE3qAVajS0EPEVsRC-J_5xuPQWkcamnBdA4YX-8jsAz8_T18CTrPyxEba01ozvIUr60pCzJScCjZIEyGeJ316DWfUuNwJ3f3wu4cLqY4t1JKNCPIvzgyNeI9zlQytLzwda8UmppH7E0jg8wbapk24CTsR-usWndND3IwLSY-r1WijTM7UQUyA20-zNp3yEA0rDOxYdoaQZutXhJvx3vfbs0yVkJb5ScFjN13xQI3Nj03RTHDLqpcNgKphZdbjWQ69z5CtI9K_k835GKSfKY0ST_g2XO4Z-nJI0cFJ31vrZ5MKupO2iw2QHCYmR80RYA7B70hjvOPPm5ZmHi5Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dO1Vrd8XfVllAKx95iTPtoR7qPZ7Z7M3qWP_pDMEo0gMA95LudfBxt1YSjIHDLF22eVfJBKmUmp8s5OGcrOmf9USCJInakDZ3EUejBOByJFS65K6_TN2hpmqP3RenmTGHtfRW6nZ4axHHb2FJJSBVCyJsz88fTZOknIjO_vwFYyeDYQMHUlLDb5mxL6iapP3weqgHYX7ge8bl9cvzMqY2zWVO1s2NyvHB2M7RR4RF-l0f500XhwfxYvsHTYtL_7_bGCnyoSaVhL5z8_1UU9TLD88RIrlEiv2hVouIIkiJ5CFjuJRBwtw_s2JmY_kDKArqHIQakojm8PId0YoQXsXcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EG3SBGzDFyc-lvIEzc847jqR8f1NS9BAbp0TpsI7YmpMZ-vB3N4niSD1J6Up8aTNTnCJKrOsUEdEVs_e7dR1NSDrwIE7N6V6-JzZi5N1AfATnIOrbRcHB8rO2RGAJYbhzlGeOGAIRy2RIF4YubxS-FEZk7WjWuNRphXNAppSHYrD05dHYr8yqTZJ1i6J4GlF-9BD_1-T8GESH27RUJPMlmpFO0y1YGtXoEWmp7KcTOgsSUMuATIIXfUc2tJJM4oTUAvra1GmLSkXg9VTAA_Wwg8lV_1-Sl9G3NLNrQBi9H533_6KQDuPMcVjqPjmnIBR3eZVPpP19KtsDJSl88iH-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NBHPiaMqL8QWkCp89NtVM8V5e_FoutRCM38iWZF8y86IVSr2BogH8-oe1GzVxyC1xX9LS8QaOM9c1_-HhvowxQoGAwV2FXjjHi44ffg0U-olhhbeSAoHVMSIWdpL52PNJgUxVXDwHrSCZhFmdRTkUiRxTNSBq4yfHnobSB7nFhLyvR4IJQ8iYOFLSNEKTb_Bxgai4kVH7rsiQhAaKuGTlogFOU0H7Kl0G4zLALgax85lAsfvA1HfSdPH9ovMkCOf6rtkGXo332Wf70OusR1EMFHBBc3H1HA_KMBukYdNa3w71i2FAq9vkA9RpSOS3AyOCw1Qs_KppOKf_3suqXELvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fsvvf9mwsV1rsGCq3Il46S_XNTBo-YY679Vcr0Z182ZWkEhIsv3E8RosRharz8L2iqGFswj5RMscNXgqRVpnezf-ni6iOv_NCclqCfIzll5yG3UIshbUX062h-ZbOr9ytfbER7ER5vl8Ju4ehtMI4F-ZuMFsVY_yGUo5B8-61OvN-ssrPeZ7OBIWP1WJRK_Mz8dKJeWH3ie0xcUGf6iUY9mww1QARBQeyG81ntxg_qzID7ZwZnDFqG2QNzjlAA3wVUu1vRzuTngxRhdC20MchBJVtk46du03Gw3G6fW2Xi21xLrwSBWV72-2X0Tws16tcESJEgJboRKSqZPcvdk22A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
جدیدترین مدل‌های آستین که استایل شما را متحول می‌کنند
😍
#فوری_استایل
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/674078" target="_blank">📅 14:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674077">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from| تهران روشن |</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7e77e148b.mp4?token=VYaOWHQHZIUkyOwB467ua84jGHRZSaL6N0rVsK4ytx0iBZVQxv8X2PSmYnNJkxeEi9bX_xXO-SF65aPGsj4atp5p92X6GU-sTNNNfXAnNK2uo3llViF6GMQyzDKihBvvhCdH2zP5rA3GgTsJAJKQyDi9VJzfLFmyfvcDl61f2279avp8c3cR6VvmxwteDrYEnFhHCJue622N4ZDH3CHnX6yo0ndUcg4M51ccHEm6Bd7V5N9LaCF7Aw_cHxbG6yRD75uWaftcLV2khKGpgpaSSDcHDmHz6ayskuwYQVt6hicsPzOFEhIlIU04MNCnuUa7IVu42zj7LV13S_ZZHKC3PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7e77e148b.mp4?token=VYaOWHQHZIUkyOwB467ua84jGHRZSaL6N0rVsK4ytx0iBZVQxv8X2PSmYnNJkxeEi9bX_xXO-SF65aPGsj4atp5p92X6GU-sTNNNfXAnNK2uo3llViF6GMQyzDKihBvvhCdH2zP5rA3GgTsJAJKQyDi9VJzfLFmyfvcDl61f2279avp8c3cR6VvmxwteDrYEnFhHCJue622N4ZDH3CHnX6yo0ndUcg4M51ccHEm6Bd7V5N9LaCF7Aw_cHxbG6yRD75uWaftcLV2khKGpgpaSSDcHDmHz6ayskuwYQVt6hicsPzOFEhIlIU04MNCnuUa7IVu42zj7LV13S_ZZHKC3PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتحاد مردم در پویش «قرار همدلی» برای پایداری برق نتیجه داد
اکبر حسن‌بکلو، معاون هماهنگی توزیع توانیر، اعلام کرد:
✨
مردم به پویش «قرار همدلی» پیوستند و با کاهش مصرف، بیش از هزار مگاوات کاهش مصرف برق را در روزهای گذشته شاهد بودیم.
این کاهش موجب رفع محدودیت تأمین برق در استان‌های جنوبی شد.
✨
ادامه همراهی مردم می‌تواند به تأمین برق پایدار برای استان‌های جنوبی کمک کند.
#پویش_۲۵درجه_قرار_همدلی
🆔
@tehran_roshan</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/674077" target="_blank">📅 14:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674075">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uey9SFbLHV8PMqzU7H_dfDgw71yDOK66k7wIzmzy3eu1cYhuaNFiSKRC4tebsBpdxixAYPhOb5yJ0NQFbOzMdz_BBwCdXz-nPjNGSwu6i4-PCiN3lsXUbq-OztK73-XuYXV_bnZA6Zh3nYkY6rS1W2L0iXeMsytfKv9cdoVbBoDLAAmDlIXPidvmerk81B15DeSuMjV8kLZYDhGGqKsq_7kE2AGNv3-_ydlngeg9TtshiZb8keJO3yg2DkNysIF0mdtTJJF1b6UP8KHWim8J7WY1VQtdNqGR28JRYCXk4UxvAnYvvGcpjouOrdMTETmj5Cj-HVzX3qy_vaFFlDNWHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه مخاطبان برای ساخت آینده شغلی نسل جوان
🔸
در این نظرسنجی بیش از ۶۹ هزار نفر شرکت کردند که سهم روبیکا ۷۹ درصد، بله حدود ۱۵ درصد و تلگرام ۶ درصد بوده است.
🔸
توصیه حدود ۴۴ درصد شرکت‌کنندگان برای جوانانی که در ابتدای مسیر شغلی هستند، یادگیری یک مهارت تخصصی است؛ حدود ۳۳ درصد هم یادگیری فناوری‌های جدید را پیشنهاد می‌کنند.
🔸
مشاغل آینده بیش از هر زمان دیگری به مهارت‌های تخصصی و تسلط بر فناوری‌های نوین وابسته‌اند و موفقیت شغلی نسل جوان در گرو یادگیری مستمر است.
@amarfact</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/674075" target="_blank">📅 13:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674074">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfa26ad2eb.mp4?token=h436BIrPfhz2ThTdu0RvViedOwyQsC0bH7c53rQCDk6WRXyFbqo3Cj101FqA-GfrpJ63msZACowkkGgHQ5amAKkQylxGiRM2bdiygm0V7tGcEO91h4KBXAH89ej1NfE714ZDCvm744vN1AZMRZAng5bQyCCcnuP8ihuK9kJgxWpboqskeELZD7dafHEI_8OeWc6zU0-kOiLmdVKC8Q91E6Hbcx7KF5oEazg_vrVPiHetTRdeJhzO91XFp9YdaIMCWkTJT3ZzDw3oHIlTKvN26VM6OjCbCOcmiUpKQi9HYi8ehaGSXyrRS3L-9UVTiXUZICKusLzWTxfeb3-T4rPMjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfa26ad2eb.mp4?token=h436BIrPfhz2ThTdu0RvViedOwyQsC0bH7c53rQCDk6WRXyFbqo3Cj101FqA-GfrpJ63msZACowkkGgHQ5amAKkQylxGiRM2bdiygm0V7tGcEO91h4KBXAH89ej1NfE714ZDCvm744vN1AZMRZAng5bQyCCcnuP8ihuK9kJgxWpboqskeELZD7dafHEI_8OeWc6zU0-kOiLmdVKC8Q91E6Hbcx7KF5oEazg_vrVPiHetTRdeJhzO91XFp9YdaIMCWkTJT3ZzDw3oHIlTKvN26VM6OjCbCOcmiUpKQi9HYi8ehaGSXyrRS3L-9UVTiXUZICKusLzWTxfeb3-T4rPMjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر نزدیک از مکانی که در کوه ازمر، در استان سلیمانیه در شمال عراق، مورد هدف یک پهپاد قرار گرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/674074" target="_blank">📅 13:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674072">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
ادعای روبیو: ما برای مذاکره با ایران آماده‌ایم
🔹
وزیر امور خارجه آمریکا مدعی شد که خواهان دست‌یابی به یک راهکار و توافق دیپلماتیک با ایران هستیم.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/674072" target="_blank">📅 13:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674071">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
روایت برای اولین بار/ ماجرای نامه اعتراضی پیروز حناچی، شهردار پیشین تهران به رهبر شهید انقلاب
پیروز حناچی، شهردار پیشین تهران در
#گفتگو
با خبرفوری:
🔹
کسانی که دنبال رانت بودند با تصدی من به عنوان شهردار مشکل داشتند. نامه اعتراضی به رهبری نوشتم، عکس‌العملی را که منجر به تایید حکم من به عنوان شهردار شد، نتیجه پیگیری ایشان (رهبر شهید) تلقی میکنم.
🔹
آقای علوی گفت که آقای روحانی به وزیر کشور و وزیر اطلاعات دستور داد که چرا بیخود چیز می‌کنید (سنگ اندازی می‌کنید).
#فوکوس
@TV_Fori</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/674071" target="_blank">📅 13:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674067">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gJ_EPmE2qnIs4QbXi-U6lqK3AkqtYKY343rQy82FxOlHCwoVy_8Fi9zk__KNzPiPysCzhgABG3KSCCUikQae3K4AY8Y6nT_3C94JETJmr9dQ9bmGhia7NKqbr7K9RjH65kLhTO0rPptbDa5uO0e8xOiYn9_1L7YXu4-P-zxpw7hoa-dmNFy1EeQzeLsVIgsmJIt8qc4LcNMhrnrLE8RruUYGqp2ayz0L6MWzFDyGn73NvYtCtpoR8WMCX8PQG4L3-9gymO6FhyKauoItKEUGbq6p86F3RBNXvOjlSMkql3oWM4CKWLuN-gwgYjOfYcKtfN6bh4mE7evF5ZaqV-6SRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KWq4v9RVevWWkiuQuQkBpjlauTR89FMLfiAuDpjozlrgS2NRvAhJ3Z_bF99gNIo5csaHmC2kJ50fXwmgscMenWE3Va9ZjMJ4Dmotphcb1nIvYky_d0FUbxLAWWCx4ZwhaNF-5jY8TOvZywh-LD0yFp1CXfwBrdvoAB5LXURhgN2AJggYL_V7J4gno6YAKmIIPgHI3zY9kr6nYvIQlyIFeiEh0gERepslTE0KEFaIwKTD2kr9Vl57YIT6wexnCVrSyVqvVNa36kXx-O0JNxiEjiMx2Ac3yTiWDq2wQS72Q2E3CGAVbNJhWEhcOXBq726A2WLkgKNpfAbzVWTogL9C9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qDwXRQs_Y4QFtxEbxJPRBd1b87zgcYuNCpeu34cGbZJ_Jve_lsL10jBeHGjP57AgymfvzjHqA42QI5EhnzktV6PTqobnJSC2tvNE9VFFj_Vm9tdzB61H0TjG84GagPOpahqLl0y-pL7PfI6HDLTtYRZVRJ_WhR6nlyX98ZrMXQu6BvIHvGFvvyk0qRUlRWZB4e2XKJ3cMblJQ9ev5aXtgIp0UtZ_zYS4NDl4XTj7ZJMmFFUbeg2QvphiUiMGqDcfqunoriUPhxeFDjUCCNj0SjktHuk1XZI02D9pwe3uX9bOV14SgsYzKVoOf0CdJAPO3ICVvt-rE6MyxFzUxeylYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/khqKQmMuIcUoHsph_xWXh1vCA7GDGkcDkTbSzyt8fQ5VLFAN6OMT7m8GNZ-_v1J-N6XknKgVltuHIeg6lK1iSGCb-SWXBxs1lwhpfgNZRKo7yE7d5nR_xEmGh93XUQ47FTNW4y9IYym9Gb4HnfDhs5ZwfvP8NhkWJZ0wZqUO-wz2YKec19TfKyGBErgctLG4RoSwP67J-g8zN99_SLm-Mtl956HpBKvGY8dW4jweVLYAmUS2Pf-NEhTa07BE6pp8O79KfAYn1C4n1VTmM9HVaRS_NDC-MYvr5mn2uxIrnSg5gtGeMK_mOE6pZ38KtnCksDrj96KI-lOuwKWWVCTv4A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چگونه در تابستان خوش‌بو باشیم؟
/ خبرفردا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/674067" target="_blank">📅 13:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674066">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GhIDzB-2RxGA7uSC6XzFjQmwHnvaLQEdnMEU9DvZmsDeoZezWbP4a7naX9tWmlyFRrJOAGTob06qS_Icl_x5du_OD0uSdfRjtB96CLjqrPvXhhh7V_hWgKeoVevR5pZ7oNxTkcmdsQN9KONWz0AbnTtWs3mxcP-Bc2NGMg7H08ASGwOONw93hKkyTkK6rFR4HDbSO5iACzf0Xj4Wv9RuUfC4lWB-i98YIqXT7chOWyvvdg4SVh7SbQbT6sIQzD7yZX4npzJ1LbmzkbWc5DP0lNX9JrVFNNR5pRAPjeRcngzWIHI0ms9LEIclDcn4DOSISuO1x47os9ykc9WrLpGHHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وال استریت ژورنال: توانمندی موشکی ایران همچنان پابرجاست
🔹
در حالی که مقامات آمریکایی می‌گویند قابلیت‌های موشکی ایران به شدت تضعیف شده است، حملات ۲ هفته اخیر ایران، نشان می‌دهد که تهدید همچنان قابل توجه است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/674066" target="_blank">📅 13:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674065">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/911c88bf87.mp4?token=EHOHhmvtOn1rK05PBTXZ3drsz6zQq0I8RZM_Gb4i60yi8_Dr-F-g4RhcLLj8F7MEQ6zq2-S9YmoKNESPjJBLpYqqvV2UsW58T980ymg1zSA1gbhRq5Itdrv-z7_haSSJ_dmXFcC_BePTOIpbvIxYuxaRz2i-vl927AWOeh03G7F18v_un2171J4VXibKr31LOVJd9QiBukotBhsaCHe4s8Z6ngRAHv5jjYf8JHrrBIgsvuAZInD15HOpmJF9zff-lydBBwJ2miGBPeeVYszqwLUn9YA08mlX2lEJnLBYoY7AsCc27etNbxPOgtrCC4Ga7JNHulwZFMEUL74ZS_y8Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/911c88bf87.mp4?token=EHOHhmvtOn1rK05PBTXZ3drsz6zQq0I8RZM_Gb4i60yi8_Dr-F-g4RhcLLj8F7MEQ6zq2-S9YmoKNESPjJBLpYqqvV2UsW58T980ymg1zSA1gbhRq5Itdrv-z7_haSSJ_dmXFcC_BePTOIpbvIxYuxaRz2i-vl927AWOeh03G7F18v_un2171J4VXibKr31LOVJd9QiBukotBhsaCHe4s8Z6ngRAHv5jjYf8JHrrBIgsvuAZInD15HOpmJF9zff-lydBBwJ2miGBPeeVYszqwLUn9YA08mlX2lEJnLBYoY7AsCc27etNbxPOgtrCC4Ga7JNHulwZFMEUL74ZS_y8Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماساژ آسان و مؤثر برای جوانسازی صورت
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/674065" target="_blank">📅 13:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674063">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
تردد ریلی ایران به چین ۳ برابر شد
حبیب قاسمی، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
تردد ریلی ایران به چین سه برابر شده و محدودیت‌های مرزی با ترکیه نیز برطرف شده است که هرچند هزینه حمل در مسیرهای جایگزین بالاتر از مسیر جنوب است.
🔹
دستگاه‌های اقتصادی با محوریت وزارت راه برنامه افزایش سهم کریدورهای جایگزین از ۲۰ به ۶۰ درصد را با هدف کاهش وابستگی به مسیر جنوب دنبال کردند.
@TV_Fori</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/674063" target="_blank">📅 13:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674062">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CB4D3dvCcEPmeC2o_wijl9lGY67nQQTr5N3JR-v-1eY1d-VQXc2ICH80cGWmJJDsoAFgGXkJvzuo84P0k8l-pjqulT10DjCU63qtohAHl8BCSGxilnoa4Xyc97xQdz6wPoNbIzjuyjtZbYplmp-XkBTshd8nRXjl7h8GpszaEXaAW2lBgDGwNUES9XXR51WjsgcrNDdiY5iEWkFFXGEzcZBOy8H5x_g1NgSJUBtKIfb3t1d4WUkkeJJM71xlpc7QumNHO6R3RCgzKyCs-ovJ4ITBC9xX-OmIo0To11Xi6Cm61KfNwLdzGQmp6dNlr0wBgZL9HCggIloAvLo7drTNng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مهر تایید سهامداران بر عملكرد سال ۱۴۰۴ بانك ملت
🔹
با برپایی مجمع عمومی عادی سالیانه بانک ملت برای سال مالی منتهی به پایان اسفندماه ۱۴۰۴، عملکرد این بانک بورسی مورد تایید سهامداران قرار گرفت.
🔹
مجمع عمومی عادی سالیانه بانک ملت با حضور بیش از ۶۳.۴۱ درصد از سهامداران و به ریاست مسعود نصر اصفهانی رییس هیأت مدیره و نظارت علیرضا خاتون زاده ابیانه مدیرکل امور بانکی وزارت امور اقتصادی و دارایی و اسماعیل چمنی نماینده شرکت سرمایه گذاری سهام عدالت، منشی گری احمد خیرخواه مدیرکل حقوقی بانک ملت و با حضور نماینده سازمان بورس و اوراق بهادار برپا شد و پس از قرائت گزارش عملکرد هیات مدیره از سوی فرشید فرخ نژاد مدیرعامل بانک ملت و قرائت گزارش حسابرس و بازرس قانونی، سهامداران با رای قاطع صورت های مالی این بانک را تصویب کردند.
🔹
همچنین در این مجمع حسابرس و بازرس قانونی، صورت های مالی بانک ملت را از تمامی جنبه های با اهمیت، منطبق با استانداردهای حسابرسی و مطلوب ارزیابی کرد.
🔹
در این مجمع، تقسیم ۴۶ ریال سود (از محل سود جاری و انباشته) به ازای هر سهم بانک ملت به تصویب سهامداران رسید.</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/674062" target="_blank">📅 13:08 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674060">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kTS4Fr4QVul5fmRlZ0XyLkSfo-8YNo3Qm7dPQSTPJ_eaVQ8N7ZEqKYS3NHuLxSsvR6fKRpFglNSzcmoQ-HkWtAiJSlSlyZRplf2KP4oaV3pbFOzWo-4x2EyDGzG-ZbP1IRzYgXyRokRi-4koejfiJU6H9DxRLoIfS49d2vb-_Z9zNhV9oGQf5MNnYtpQG5xRTAWBhU3yF_81JcHoSblpYwYxnWyl6-_A1FeAWRS-X0dS8aaAbScVLUnyxeOYL9yG9QkDr5gfLIRu3XlHmgV02oRhAn1T2HUf2mGC2TgmOjtLbJlNnsRrY77OyLl8Qw9qInpfsN9aypZTS1UoN8IBKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۳۱ تیر ۱۴۰۵؛ ساعت ۱۲:۴۰
🔹
دلار امروز ۳۱ تیر با وجود نوسان محدود، همچنان در کانال ۱۹۰ هزار تومان معامله می‌شود و بهای آن در بازار آزاد ۱۹۱ هزار و ۵۰۰ تومان ثبت شده است.
🔹
در همین حال، رشد طلای ۱۸ عیار، این فلز گرانبها را به آستانه ۱۹ میلیون تومان رساند و قیمت سکه بهار آزادی، حدود ۱۸۵ میلیون تومان ثبت شد./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/674060" target="_blank">📅 13:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674057">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
تکلیف امتحانات نهایی روشن شد
🔹
یک منبع آگاه به خبرفوری گفت که طبق جلسه‌ای که با وزیر آموزش و پرورش برگزار شد، تصمیم‌ بر این شد امتحان‌های نهایی به جز در استان‌های درگیر جنگ به تعویق نیفتد.
🔹
در خصوص کنکور هم هنوز تصمیمی گرفته نشده و طبق برنامه قبلی، به قوت خود باقیست‌./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/674057" target="_blank">📅 13:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674056">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h97_HtdEiL2DG8SuSB4Aw9Rcxr49j5E3iCQ67ZvVIwpA8EfRzf0KcQUs3zY2VEZ8R5k9HGPD1F9BB2cHSVOG_zibcM_iBuhGFvWvdnik304EqQF2MgY4T-aqoNFdoYaIAVpioh37H1C-27GhxTBuH80kHckU4TJPSAumX1X99xfQoNJMhL3ZldqyC1TWTgquMnXonprbXDa539hKy1lAE8DCdyF6gwKDW6oFdFZXW0TMqPaj9gwjysRP3q8jX0bcpXhyYyy8H72EZl-lZfMa7xP9lYxpw2WpjhIxzGHKN-j0E_JCtIK6vtfKDj5ZyZWASRHfTGSPTWPvyMCjiJu5Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
♦️
جادوی دمای رنگ: کلید آرامش در خانه
🔹
رعایت استاندارد کلوین(دمای رنگ) در نورپردازی، تأثیر مستقیمی بر سلامت روان دارد. اگر این اصل را نادیده بگیرید، فضای خانه به جای حس آرامش، شبیه به روشنایی سرد و بی‌روحِ مراکز خرید یا نمایشگاه‌ها می‌شود و خواب راحت را از شما می‌گیرد!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/674056" target="_blank">📅 12:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674055">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a109d2696.mp4?token=XictSQ6nr4x4HvG3Ka6OvKZTTPKcVlEKQV-lPWa2Kkf6UVVsIbX8oeUVVA_fR11-oBgDo6ZUjLa6jnAmz06MOVHUJbKh-tmDUl7Apy99RdDHGWIcEBlVmDBCJfKEPkraIVnzlhbFEb6vEMsgikozaZnRVW6APHK1xfdICDKa1fDNVOAeql1cwQeUTjTTCwBC7I2707W9jffpWTHgZ25AFSgbc1An_D3v_iAyCnLue_7v-XeszzMOveJIdutnbC3xgUcXLYx4UANvRYJZB1J2nyWSfSHG3vObPJkqOxnSfgGkTYjkkoWnbHF5mWxjyph4fVodAu24i-0JogiHBVZhoFpd4ABWfz4OtZiysBJW2nLkB_EQ4yAGoDqAo-YUJ9BJyVMryt91PRJzToG6UddT14W_xpwYezPoC28oNta9Z8RifVI8-OhqXJwVAFz1NoGwnHAlx8Co19yOOkZqtR-eJZXQPVWqtI4CquuURwRN3LDvcPsJEAZNPOxRO8VeSFRuKC0i1nzT9UzoXmyfpcl9v360CoVzoJJU6Op8RQZ11C_jsp1jO4rp1UKBbe-8AJynjVZ1Amq4ni-Cq0d04x02nXuhWhvdYkYzzNag3T4hAfKuD0c33N93abShUSRQsb7pox63knl6Pp8GuP0b8QZpuwRqGUrQ0AzjjNYrz5ficao" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a109d2696.mp4?token=XictSQ6nr4x4HvG3Ka6OvKZTTPKcVlEKQV-lPWa2Kkf6UVVsIbX8oeUVVA_fR11-oBgDo6ZUjLa6jnAmz06MOVHUJbKh-tmDUl7Apy99RdDHGWIcEBlVmDBCJfKEPkraIVnzlhbFEb6vEMsgikozaZnRVW6APHK1xfdICDKa1fDNVOAeql1cwQeUTjTTCwBC7I2707W9jffpWTHgZ25AFSgbc1An_D3v_iAyCnLue_7v-XeszzMOveJIdutnbC3xgUcXLYx4UANvRYJZB1J2nyWSfSHG3vObPJkqOxnSfgGkTYjkkoWnbHF5mWxjyph4fVodAu24i-0JogiHBVZhoFpd4ABWfz4OtZiysBJW2nLkB_EQ4yAGoDqAo-YUJ9BJyVMryt91PRJzToG6UddT14W_xpwYezPoC28oNta9Z8RifVI8-OhqXJwVAFz1NoGwnHAlx8Co19yOOkZqtR-eJZXQPVWqtI4CquuURwRN3LDvcPsJEAZNPOxRO8VeSFRuKC0i1nzT9UzoXmyfpcl9v360CoVzoJJU6Op8RQZ11C_jsp1jO4rp1UKBbe-8AJynjVZ1Amq4ni-Cq0d04x02nXuhWhvdYkYzzNag3T4hAfKuD0c33N93abShUSRQsb7pox63knl6Pp8GuP0b8QZpuwRqGUrQ0AzjjNYrz5ficao" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خالق ملودی «پلنگ صورتی» درگذشت
🔹
پلاس جانسون، نوازنده برجسته ساکسوفون جاز آمریکایی که با ملودی ماندگار خود در فیلم کلاسیک «پلنگ صورتی» (۱۹۶۳) جاودانه شد، در ۹۴ سالگی در لس آنجلس درگذشت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/674055" target="_blank">📅 12:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674054">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4042d84114.mp4?token=H1DeGYrxhDr6ovaX4uBdKSzdndH86YQBkaocjlVRqoeQF6c3hosvVXJTrCuraZ7M5Zjywcp5lY8wJQEQuKHww8ik17r7GviNuhbGPRtDrtfridK0NZhbFWmPrdIlNxR44Xo1uYuy5qtsnjSN3nk_9Dc2dqUv7Ij4YD9uI4dLXxwYO87BNpMKAnTUxRFXExBYwbVZWVAvdVtob3VIoJId5XCbtxdueU-5xOnEHIdGTMCPxJtzvEVSrG2rL9Kk56hdLv2GQxlanuNXGaVJtft96dbNNunmqg2FqahK6MN16uaVTueDUNENGro36zUyJxvxRkpAKsAarZeQr0oPCqBwsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4042d84114.mp4?token=H1DeGYrxhDr6ovaX4uBdKSzdndH86YQBkaocjlVRqoeQF6c3hosvVXJTrCuraZ7M5Zjywcp5lY8wJQEQuKHww8ik17r7GviNuhbGPRtDrtfridK0NZhbFWmPrdIlNxR44Xo1uYuy5qtsnjSN3nk_9Dc2dqUv7Ij4YD9uI4dLXxwYO87BNpMKAnTUxRFXExBYwbVZWVAvdVtob3VIoJId5XCbtxdueU-5xOnEHIdGTMCPxJtzvEVSrG2rL9Kk56hdLv2GQxlanuNXGaVJtft96dbNNunmqg2FqahK6MN16uaVTueDUNENGro36zUyJxvxRkpAKsAarZeQr0oPCqBwsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیروز حناچی، شهردار پیشین تهران: ای کاش احمدی‌نژاد هیچ کاری نمی‌کرد چون نتیجه‌اش فقط تخریب بود/ احمدی‌نژاد سازمان میراث را به شیراز برد و بسیاری از اسناد این سازمان گم شدند و این سازمان نابود شد/ تخریب باغات در تهران را احمدی‌نژاد آغاز کرد
پیروز حناچی، شهردار پیشین تهران در
#گفتگو
با خبرفوری:
🔹
احمدی‌نژاد خودش را جزو نخبگان امر در حوزه‌های تخصصی می‌دانست، اما به نظرم تخصصی‌ترین موضوعات را به وجه بدی به اجرا درمی‌آورد که دیگر کسی نمی‌توانست به آن دست بزند.
🔹
در نتیجه سیاست عدم تمرکز در زمان احمدی‌نژاد، سازمان میراث را به شیراز بردند و این سازمان منهدم شد طوری که اسناد گم شد؛ اسنادی که برخی از آن نقشه‌هایی با قدمت صدساله بود.
#فوکوس
@TV_Fori</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/674054" target="_blank">📅 12:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674052">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00f0137ab5.mp4?token=CP2f3zfIkCw_aUFhgsULsubLCxGgN2qkWJYtiwBN61y7U2Ykd9v6Z6jcm0YqJzgCrNfBAaCrFwk5q2N52nezC4-3WxPso7mWeJgxI_jikVHDWLj7AfCZBk_RLZw1Etyddrc1R2_c3O9o3IsmDIdftlSpiLgWIwY6rJttul4pZn1NXYjZuB77Uk5IaqRXiqXPqSgm630w8D6zWpqWSCnK3Sk48zF-8JXBkplnH2X9tRANMhke1mAjPxFe8Fxl01ObNQAsJNswGKTwfF5OmgyaSYxYHiyAbP3yYFdD27u8yhLWd3zy72tSSdwEciUAPvKRBxNTIvYg_AY8QFYQwhuHGqicyqhv7UoqicGgyqE3wKksqq6F1XVKJrFzspHWSaZOnelvZSaaJQGOkYb76lenw-XvMCZ4YYQw91H3CopLwIl6nvZ-_nJeJTkR2_mu0tevaztw_YdYG0XdIkSvp7zFQpPGApWlNzvkGi3S526DIKaBwYKAheT8Tr8v6iqjaIKHw61PdI_HjxpaqyyNx0z1tnbNCjRCp9hnbub4H3oWUKgaDqTf6gcbKDH_qylWeY7VZ1qWueOkZFjxGXTWXaj9_GEy8shWEZRYapp2j_AhHidIgBEubWdBYM0b7kuAXBs8G2PLddgsb0RXpwAqeFTe2j_sPB4_ru7SnxSuXN8B4lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00f0137ab5.mp4?token=CP2f3zfIkCw_aUFhgsULsubLCxGgN2qkWJYtiwBN61y7U2Ykd9v6Z6jcm0YqJzgCrNfBAaCrFwk5q2N52nezC4-3WxPso7mWeJgxI_jikVHDWLj7AfCZBk_RLZw1Etyddrc1R2_c3O9o3IsmDIdftlSpiLgWIwY6rJttul4pZn1NXYjZuB77Uk5IaqRXiqXPqSgm630w8D6zWpqWSCnK3Sk48zF-8JXBkplnH2X9tRANMhke1mAjPxFe8Fxl01ObNQAsJNswGKTwfF5OmgyaSYxYHiyAbP3yYFdD27u8yhLWd3zy72tSSdwEciUAPvKRBxNTIvYg_AY8QFYQwhuHGqicyqhv7UoqicGgyqE3wKksqq6F1XVKJrFzspHWSaZOnelvZSaaJQGOkYb76lenw-XvMCZ4YYQw91H3CopLwIl6nvZ-_nJeJTkR2_mu0tevaztw_YdYG0XdIkSvp7zFQpPGApWlNzvkGi3S526DIKaBwYKAheT8Tr8v6iqjaIKHw61PdI_HjxpaqyyNx0z1tnbNCjRCp9hnbub4H3oWUKgaDqTf6gcbKDH_qylWeY7VZ1qWueOkZFjxGXTWXaj9_GEy8shWEZRYapp2j_AhHidIgBEubWdBYM0b7kuAXBs8G2PLddgsb0RXpwAqeFTe2j_sPB4_ru7SnxSuXN8B4lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئوی یک نظامی آمریکایی در پایگاه آمریکا در اردن هنگام به صدا درآمدن آژیر هشدار حمله موشکی ایران
🔹
سربازان آمریکایی پنج دقیقه وقت دارند در محفظه‌هایی که برای آنها طراحی شده است پناه بگیرند، این پناهگاه‌ها با فاصله از هم طراحی شده تا تعداد تلفات به حداقل برسد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/674052" target="_blank">📅 12:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674050">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e810dcc5f0.mp4?token=GRC0mL8uEo1PPkL0qS_i-99nlZzLiSPuxihbN4bIADhMYPNwAOwcUMqJ6yLN4m13Rn3kNx2pYc89dtTOoMIVgR_9tvl0ng6yu3bI4cly-2qhvl_80f2Z_PGBF-i5a3Dmo2NOzH6W35zUYWUxl0c1zJZpFUrz-2-hoJPvoJ1ZrsVxxon4_dGjwcbrB_CVpCeQPXGffEps75tlsi7469kvZHmBCo0LyyIqTC6XU2i7l5BezbSMWFukV43nv3JwQUoW8aefgk0MdrNO4hTXbVlXOCQfHJw7KbAOaIh1C2kFO9uDrkjmotNCJuzx8x67Rw2vHI6FvwX3hZ9YYIWnPT7ac39Q-RPZQCf5X2UwkgVh_3xR1nUhFFpEn_Vi5a8PX21Dy7tLlHBelSXKEtq2We3x_S_f7DR99ltOKgnV5QXpttFNpL6_eNqzdoU_1jLR25kvFKqFbEM4xxswI2GWu4EpthUyhzu8VwLMFhnS5ezNM9KYPt4NOyxRsNwbjUdVaHGmewheLYJuuh2GcwXQWtGCTJ-15USFmIHjlRCrejYMqDqrAWC56IFPhEBgLshgqIDCjuWTjM4Z4wRA5Iw9FlMh7p7n6QKbVo2p95XIQhOjmwFbxJQH5eZTtWBs9S2aXfxv5QqFijW9LndnCh-klcpZ9BGJs08yrSeBVmTrK0URBR0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e810dcc5f0.mp4?token=GRC0mL8uEo1PPkL0qS_i-99nlZzLiSPuxihbN4bIADhMYPNwAOwcUMqJ6yLN4m13Rn3kNx2pYc89dtTOoMIVgR_9tvl0ng6yu3bI4cly-2qhvl_80f2Z_PGBF-i5a3Dmo2NOzH6W35zUYWUxl0c1zJZpFUrz-2-hoJPvoJ1ZrsVxxon4_dGjwcbrB_CVpCeQPXGffEps75tlsi7469kvZHmBCo0LyyIqTC6XU2i7l5BezbSMWFukV43nv3JwQUoW8aefgk0MdrNO4hTXbVlXOCQfHJw7KbAOaIh1C2kFO9uDrkjmotNCJuzx8x67Rw2vHI6FvwX3hZ9YYIWnPT7ac39Q-RPZQCf5X2UwkgVh_3xR1nUhFFpEn_Vi5a8PX21Dy7tLlHBelSXKEtq2We3x_S_f7DR99ltOKgnV5QXpttFNpL6_eNqzdoU_1jLR25kvFKqFbEM4xxswI2GWu4EpthUyhzu8VwLMFhnS5ezNM9KYPt4NOyxRsNwbjUdVaHGmewheLYJuuh2GcwXQWtGCTJ-15USFmIHjlRCrejYMqDqrAWC56IFPhEBgLshgqIDCjuWTjM4Z4wRA5Iw9FlMh7p7n6QKbVo2p95XIQhOjmwFbxJQH5eZTtWBs9S2aXfxv5QqFijW9LndnCh-klcpZ9BGJs08yrSeBVmTrK0URBR0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این داروها رو با این مواد غذایی نخورید
‼️
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/674050" target="_blank">📅 12:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674049">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kfxz0AfojKdLdZ1b_X1KMnaQpEWyvo3J6Gkd7LWVVBkIHeW3Ce74SCAek1BOVDfTKblLnA_b6lb_0WLb7mmjT97iyo_M1Qf9yuDH8HEChNIjrzR5Y5XGddzJ_n2Jln1bBejBpL6VZg-P0oVA9NVJmJE4KQasoYISmP8I1ORhI3RVioD8gUQptEBOdy6BtBOmPKHizXlg1mKR5XPS3sU97kXk3gE3wXFSuW9EbuRANv3C5ExszAXGXNotMWAtb2C5s75jX_dDmHGRQ1Rice7tMUGuobQfYgp-KunbYvESGfH-jVod8umDSMMsdabtv3sGr0FEA_WRflBkHcq0Q-JAgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی کمیسیون امنیت ملی مجلس: ‏ادعای ترامپ درباره درخواست ایران برای مذاکره درست نیست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/674049" target="_blank">📅 12:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674048">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
سرنگونی یک فروند پهپاد متخاصم در آسمان تهران
🔹
شب گذشته یک فروند پهپاد متخاصم توسط شبکه یکپارچه پدافند هوایی خاتم‌الانبیا در آسمان تهران رهگیری و سرنگون شده است.
🔹
این اقدام در شرایطی صورت گرفت که بامداد امروز، مردم تهران از شنیده‌شدن صدای فعالیت پدافند هوایی در برخی نقاط پایتخت خبر داده بودند./ فارس
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/674048" target="_blank">📅 12:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674046">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07db88e44.mp4?token=D_MfZnd0Mpb1Vq0L7b783Y31VSlSvAVHQyo_HRVQKRcFigGrFZpDUA0LRgHjo-u3qce0ezDD2OuLS7Poeu7G0T_8bBSe0AIDRniWf8LDhJZaQCv21rCsRj9queebAQ5qgw7C-B6Snp50rGX4L0UOEs_c2cm1qFNgvNxNeo8qZWP6pw3F3__d-Md9FRqJieY-okW5xtKjLVzwyUbHD5i3Yi6pvHAWgsLjI-xxxnAEde_6scBOhA3BsLqY0Ird5NUVq7SDCKlwCyi2muViupwHu5Upfbka4kd4KmgocZTJgeIjESQDDTHmbDcrJWKaNLQZ5n1uCZl2aWJl1HspOf44lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07db88e44.mp4?token=D_MfZnd0Mpb1Vq0L7b783Y31VSlSvAVHQyo_HRVQKRcFigGrFZpDUA0LRgHjo-u3qce0ezDD2OuLS7Poeu7G0T_8bBSe0AIDRniWf8LDhJZaQCv21rCsRj9queebAQ5qgw7C-B6Snp50rGX4L0UOEs_c2cm1qFNgvNxNeo8qZWP6pw3F3__d-Md9FRqJieY-okW5xtKjLVzwyUbHD5i3Yi6pvHAWgsLjI-xxxnAEde_6scBOhA3BsLqY0Ird5NUVq7SDCKlwCyi2muViupwHu5Upfbka4kd4KmgocZTJgeIjESQDDTHmbDcrJWKaNLQZ5n1uCZl2aWJl1HspOf44lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
قطعی برق؟ تاریکی دیگه دردسر نیست!
🔦
چراغ شارژی خورشیدی تاشو با طراحی کاربردی، مناسب برای خانه، سفر، کمپینگ و مواقع اضطراری.
✨
ویژگی‌ها:
✅
شارژ با نور خورشید و USB
✅
طراحی تاشو و کم‌جا
✅
نوردهی قوی
✅
مناسب برای قطعی برق، خودرو، ویلا و طبیعت‌گردی
🔥
قیمت قبلی: 1,598,000 تومان
❌
💰
قیمت ویژه: 1,098,000 تومان
✅
⏳
این تخفیف برای مدت محدود فعال است.
🛒
برای مشاهده مشخصات و ثبت سفارش، روی لینک زیر کلیک کنید:
👇
👇
👇
https://memarket24.ir/product/brief/47540/180124/</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/674046" target="_blank">📅 12:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674045">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cv2kTOw8oxRl-pK_g5IIUhBH5Dlfhi_UKJMCNi4b-PdX7z4sCAZ3J7d2MwogRbEiHfVlq9PeR1PcuKLkRqLiR0yqMe0NUr69ZkzRizOmJSDV2ADoE43lWtC6e5NOQZytCSAYnCmWON9NuknScvh2__W7nL5sWm12mtdyQCxAhBY0L9CHN-4keD54atVkAYBif0usECnjXEmo7Tcf-MFM1TIZcKEAPZLkpJkmvWNJeS7npdSb2KL6n36egUoM_RHc_B-R9zp_BJl2cxXxJwyCpoxOq4N4uS0yNYhZjOtwjuRNh4yqR83cJRCIEHaiD57irCr7FJykzWFQqTXehn7BQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جایزه‌ عجیب برای قهرمانان اسپانیا؛ از جام قهرمانی تا کارتن گوجه!
🍅
🔹
گاوی و فابین روییز پس از قهرمانی در جام جهانی، در زادگاهشان سویل طبق سنتی قدیمی، به اندازه وزن بدنشان کارتن گوجه‌فرنگی هدیه گرفتند!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/674045" target="_blank">📅 12:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674043">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/348d732189.mp4?token=m5qrpbCcvzjlPJmOejeTZh8hv8XUQkHjrb3wZOvP7B9pF5J6Up6t_YUVJeKCGGCUBwHupEuV_grGaqmjvDXh2wqLC4YUX2D6a9ApK_W3OIiq1rISIoYpO9Hv8TlieFZExEkNHb0il5VyIy1qxjP6BOTgsOLJYArwqT-EYI1AnyKUfEycstX9lF2XYvUGtW8xZ1xh69IMpKnPbzeB_FytknYTODqOTZ238TZT7jwG9jlNr4gqyHHuBCdRXhWAdOTaicFrj1y9CsmUdDWfQgkgg3FsEK3vh0-AjXXyPyF2dmSs_UmZDF7lLxktSG6iFiNbIT2nbWwfMUGfVh5OJO8iwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/348d732189.mp4?token=m5qrpbCcvzjlPJmOejeTZh8hv8XUQkHjrb3wZOvP7B9pF5J6Up6t_YUVJeKCGGCUBwHupEuV_grGaqmjvDXh2wqLC4YUX2D6a9ApK_W3OIiq1rISIoYpO9Hv8TlieFZExEkNHb0il5VyIy1qxjP6BOTgsOLJYArwqT-EYI1AnyKUfEycstX9lF2XYvUGtW8xZ1xh69IMpKnPbzeB_FytknYTODqOTZ238TZT7jwG9jlNr4gqyHHuBCdRXhWAdOTaicFrj1y9CsmUdDWfQgkgg3FsEK3vh0-AjXXyPyF2dmSs_UmZDF7lLxktSG6iFiNbIT2nbWwfMUGfVh5OJO8iwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت کشور: سقوط مشهد در اغتشاشات دی‌ماه پارسال را کاملا تکذیب می‌کنم
🔹
آن شب آقای مومنی، پورجمشیدیان و بنده در وزارت کشور بودیم و مرتب با استاندار خراسان‌رضوی که در استانداری بودند صحبت می‌کردیم.
🔹
بعید می‌دانم آقای عراقچی چنین چیزی را گفته باشد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/674043" target="_blank">📅 12:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674041">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pAMuVT5lM5kvjgPcdSpJyu7qhek4RRbi7eNsiv1YDXzr2tiMMUElJk-yBnyHeaA4Tg9ERbSbcoz6n_CZth-uALA6sfjgkULrq1jByySzS91i2ppFtYr76AC9BBinBvkjR_4fESqUaQGARDWoBRPS6_Tr0QA1y3qB2RQF2JKaGVGnHViWN2DQCL3nnCod5oTWwKeeZYAtHqxS_Xza45W_FyQqvLImDk7RQFa_n-dT28bOinMEtve_a-7tZUx7yw_GNIgS-CAfS6TNm-XA9nzcGzCSbObLOMbpkEd-rKIVGJ8vn6zaffo4xbPjNAZUK1S-gAjwNyfsvM89W-TxpvNICQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mlg80-_Pwf_5eXIsvnSlZ8G5p9G_0oAf1xZZ98VlWacAua77RwQBKg_I25pTaauj3QTR6aoVT0ybKY27XfFWwGSP7FS2qVqsturyGYowQHJYUA7uaYbY8Jv6POXbyDgx5SeSNjWpsOsF1d30o3Hpd2yvOTzZ2ph8Yg4uHnCHYmlFA07KPVoXNcAwHoQf_jpAifjIT-mw9UuUB0MRnykl1G6HJNhga8H95jZhSHMVebChCg5o9ucTnlV9m_LIuUUx5yilztQC82GGoyRe-HylofA72VAJLfnHQ28FeJYHK2i2bPFj-pYssTeS6RbkabmKyf_NeyPB5_7UsvhSMpZcyQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصویر ماهواره‌ای از انهدام رادار هشدار اولیه آمریکا در پایگاه احمدالجابر کویت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/674041" target="_blank">📅 12:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674040">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gd68LO1_6AnNWWidRO1lm39XFNo46GiQF3c_nCy3MUiz5g1XRH-gv5MFbqzBBKdT2VAkLor_4uwDxXqMzYR77VOmKo64hjV-whpoWwnOSFfq0Bc8Z_KrsRnI2JAv6kT4ufU-QIidQgWfB0mEszUB8PHJm_x-ogIyVXFkK5BZQd9PJg-aIprjCCse3sYJ9MMQdSsYdgM-6GulGToRK_BymOa51lTDM0y0oROJ1ROnyApHpVH0anXstDnkBNDVjyktU8-CkBs-MmfCpiao4BU1PCU5T0l_3WLzDxLQ208HvX_Q1ivcFnlVUhHBXiCUXre98t3oxlJUbvR6zQtNCZOO-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اینستاگرام قابلیت تعویض یا تغییر آهنگ پست‌های قدیمی را فراهم کرد
🔹
اینستاگرام قابلیت جدیدی به نام Replace Audio معرفی کرده که به کاربران اجازه می‌دهد موزیک پست‌های فید و کاروسل‌های منتشرشده را تغییر دهند. با این ویژگی، برای تعویض آهنگ دیگر نیازی به حذف و بارگذاری مجدد پست نیست و تمامی لایک‌ها، کامنت‌ها و آمار تعامل حفظ می‌شوند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/674040" target="_blank">📅 12:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674039">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a25e7a443.mp4?token=i6dCZXmQLX90bgnN5lPg_7R38XxO0df5qjX4tS9bV2FNyJGZRKqWilqrJHQtHBWmwRUpqX-TeEixUPrC7gBCdupAekIcrW6p0NHyHB0bYugKAXOX1J9ank-NHRbO0l_vOarsJXSS_8Nj8YKZn3YIewg0InZe13YxUjBknffrlocq_5fCxrHV2heybxHhaGGFa44qjgxMdQV1ELThN_pVptdJpXYiTuQuxt6NPrpigBXDQmuVPS5EfF0J73_Wk6rjMuf6jxMdyuRnP1ttBLa31nKu6zhETrvGl2WKn8e8EIUpH1SiOXil64talAoGOzy7Nk3jJjVH61WsFwLn1-0LxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a25e7a443.mp4?token=i6dCZXmQLX90bgnN5lPg_7R38XxO0df5qjX4tS9bV2FNyJGZRKqWilqrJHQtHBWmwRUpqX-TeEixUPrC7gBCdupAekIcrW6p0NHyHB0bYugKAXOX1J9ank-NHRbO0l_vOarsJXSS_8Nj8YKZn3YIewg0InZe13YxUjBknffrlocq_5fCxrHV2heybxHhaGGFa44qjgxMdQV1ELThN_pVptdJpXYiTuQuxt6NPrpigBXDQmuVPS5EfF0J73_Wk6rjMuf6jxMdyuRnP1ttBLa31nKu6zhETrvGl2WKn8e8EIUpH1SiOXil64talAoGOzy7Nk3jJjVH61WsFwLn1-0LxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اولین تصاویر از کارگاه بمب‌سازی و دستگیری مهدی خانکی
🔹
«مهدی خانکی» عنصر عملیاتی و فعال یکی از گروهک‌های تروریستی؛ صبح امروز به دار مجازات آویخته شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/674039" target="_blank">📅 12:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674038">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d91b263bf7.mp4?token=IWoUSBppBWIoU5auMwyp_MdqDsiw7SsAExrWM7ZvnGIJSx1fLnNdSlPKZMRTyXMWYptU7yGLN2zGVlEmgmeZ7FQ0a3SRmLAQOIgdEycZPVk4TBUg73KoVdkfoMyLgOrphfeR35caS8DdR3HtbyYhmbpQrS6FyLfiX8UoxATZjpOjOGma0DBCDf5yp9TPVyFB4eYJL7rKiLifSFGc-2CMG6HFAPbaZdFMJRDwAhg98OUQxvafwwwDD3aQpNoVEV_APjvDqVWNBdrh_RZahmFXmM2Q7B6PihVMe0NIRKW8wyyob9VQhIQtyKvJHeCNGo0iYWkwQdp-FgfNNxr2RtYZMIJoi0tjHkY-6ltFWJmfGlY65FIdcTsyqkEgYj4tlHs15XcHp9kMVdLi2CqdIqgiaJgTt8QAfCQ5ZosbLeS-V2qL2BvZ-Qs4Ci5lu0BDk0ZUVQ3Z3YMZdq4YMyUAo5SpfIrJXwe0gnbRp2tV9rOnwqtZbV3Us3BMSQLLuvlF5UVLa9R-zpZuGvu7QbFzYXY7Vm1TNCBraQxncWUWpqrusX8jXY4Ep107tqVu6iap-2m12PXGQQ6ng1DAmZVV5BPcNcTDHu5FjmvNmmkKGSUNIf5Q3gKmaQvRbzp8KfmcviU9fsBcIOMDboJtKjM3ElHamXb64jg7MNjMEQES-CvCCyk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d91b263bf7.mp4?token=IWoUSBppBWIoU5auMwyp_MdqDsiw7SsAExrWM7ZvnGIJSx1fLnNdSlPKZMRTyXMWYptU7yGLN2zGVlEmgmeZ7FQ0a3SRmLAQOIgdEycZPVk4TBUg73KoVdkfoMyLgOrphfeR35caS8DdR3HtbyYhmbpQrS6FyLfiX8UoxATZjpOjOGma0DBCDf5yp9TPVyFB4eYJL7rKiLifSFGc-2CMG6HFAPbaZdFMJRDwAhg98OUQxvafwwwDD3aQpNoVEV_APjvDqVWNBdrh_RZahmFXmM2Q7B6PihVMe0NIRKW8wyyob9VQhIQtyKvJHeCNGo0iYWkwQdp-FgfNNxr2RtYZMIJoi0tjHkY-6ltFWJmfGlY65FIdcTsyqkEgYj4tlHs15XcHp9kMVdLi2CqdIqgiaJgTt8QAfCQ5ZosbLeS-V2qL2BvZ-Qs4Ci5lu0BDk0ZUVQ3Z3YMZdq4YMyUAo5SpfIrJXwe0gnbRp2tV9rOnwqtZbV3Us3BMSQLLuvlF5UVLa9R-zpZuGvu7QbFzYXY7Vm1TNCBraQxncWUWpqrusX8jXY4Ep107tqVu6iap-2m12PXGQQ6ng1DAmZVV5BPcNcTDHu5FjmvNmmkKGSUNIf5Q3gKmaQvRbzp8KfmcviU9fsBcIOMDboJtKjM3ElHamXb64jg7MNjMEQES-CvCCyk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیروز حناچی: مردم انتخاب کردند در جنگ کنار نظام بمانند و مقابل دشمن ایستادگی کنند
پیروز حناچی، شهردار پیشین تهران در
#گفتگو
با خبرفوری:
🔹
دنیا ایران را به واسطه تاب‌آوری و مقاومتی که از خود نشان داد، تحسین می‌کند.
🔹
قدیم که جوان‌تر بودیم در خاطرم است آمریکا سر ناو خود را به سمت کشوری کج می‌کرد، حکومت ساقط می‌شد.
#فوکوس
@TV_Fori</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/674038" target="_blank">📅 12:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674036">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0ffb7964c.mp4?token=Guv8nuXNDrVWnOC2XgzYPYmN6f5xhzjfGjQkcNC6MqUBkc7qyOAqQWjGxGLgNhw1Hb6SZUWD6mEfHsZHg0CSAX-hRuoDUsTiCztrAX32OktiwSfU7w-50RVJh_ugIr4yT7luAK9EHFHS0k0hMbZE6_xvX4_QD4c2hyMlX3fhg3WJRD25k5MmvG-b14CL7JXK8zI-N9g1IrgNBUljxT0UqX-Y9s1RPHGv1JQHbSxgeK_K4tyD8ey5XFn8aMYtv_sLjy2iuh4KAD-0xpETx5_hipuadR67c1GNATMEHL6oUnvPiiJKulIW5BAhgfKp6VNAGGg6-ts9rVT1J0RyvlF-jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0ffb7964c.mp4?token=Guv8nuXNDrVWnOC2XgzYPYmN6f5xhzjfGjQkcNC6MqUBkc7qyOAqQWjGxGLgNhw1Hb6SZUWD6mEfHsZHg0CSAX-hRuoDUsTiCztrAX32OktiwSfU7w-50RVJh_ugIr4yT7luAK9EHFHS0k0hMbZE6_xvX4_QD4c2hyMlX3fhg3WJRD25k5MmvG-b14CL7JXK8zI-N9g1IrgNBUljxT0UqX-Y9s1RPHGv1JQHbSxgeK_K4tyD8ey5XFn8aMYtv_sLjy2iuh4KAD-0xpETx5_hipuadR67c1GNATMEHL6oUnvPiiJKulIW5BAhgfKp6VNAGGg6-ts9rVT1J0RyvlF-jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چطور می‌تونیم هورمون‌های شادی رو فعال کنیم؟ #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/674036" target="_blank">📅 12:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674035">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from| تهران روشن |</strong></div>
<div class="tg-text">مدیرعامل شرکت توزیع نیروی برق تهران بزرگ در برنامه زنده تلویزیونی تهران ۲۰:
همکاری شهروندان تهرانی در مدیریت مصرف برق کمکی ارزنده در راستای کاهش محدودیت های انرژی هموطنان ما در جنوب کشور در شرایط حساس کنونی است
┄┄┅┅❅❁❅┅┅┄┄
💻
وبسایت اینترنتی توزیع برق پایتخت
www.tbtb.ir
┄┄┅┅❅❁❅┅┅┄┄
🆔️
@tehran_roshan</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/674035" target="_blank">📅 12:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674034">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k8d6SjuLqSk1_Viq7RRxvoMDxr3WCUemCIkipVQFzVX4P3Hsj9Uox9lyk29EWyINJz6DW7_G2UhK_mNJrSCbJt4V_sHDCPqodUgMxblwB6UPCGE1K9iurfIT3_UwNvabvJP7N1WVMsI_1uFQ_0vgjgYEQZwdMP3b_WU94vsL8mMPIcUclFeulKJpaIA1e3PByKOVvhPII1Jsh1OyqWuMUUm5jFRta1IeHpHNfGvM0NFnHmWja9BTOXiy3IGPMe-7o9Pt-DfTepNbUOeVQ1th0oNEsJPu3HhRbU6ese2pq4wFSxHOawGsbuzP3V6P1IfvinDsWpGowZhywwIfXYMq_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ارلینگ هالند روزانه ۶ وعده غذا و حدود ۶۰۰۰ کالری مصرف می‌کند؛ معادل تقریباً ۲۴ چیزبرگر
🔹
رژیم غذایی او شامل مرغ، پاستا، استیک، ماهی، سبزیجات و عسل است و تا حد امکان از خوراکی‌های شکردار دوری می‌کند.
🔹
جاشوا کینگ، هم‌تیمی سابق هالند: «او مثل یک خرس غذا می‌خورد.»…</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/674034" target="_blank">📅 12:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674030">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
فرار هواپیمای صهیونیستی در حمله ایران به بندر عقبه اردن!
🔹
رسانه‌های صهیونیستی گزارش دادند که در پی انفجارهای متوالی لحظاتی پیش در بندر عقبه اردن، یک هواپیمای غیرنظامی رژیم صهیونیستی در پی انجام این حمله از پرواز خود منصرف شده و به فرودگاه بازگشته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/674030" target="_blank">📅 11:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674027">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6N4jLLs4E3Ej28cPs5zvLvXwrhnibw_e50ADpFk-dqhpHhB01EV0zPOdxpB-eEtEFkr7co7kvNuGh_SrFbsvtOojzcMtT3RyqbU_7UZX5xYl6GUwfV9EcwjYRaYGW2u2igTr2-WS71gft3yBQctRAyazM0alhSOpPhddqaJ7dQ-VF7mM9Bb40gR65UC3FyxWyyawPmZHAnLxKbRzKU2_w_tIiKNRxr0GrurYqWiFgNRL8950TtFUBc7eKp9TkUl7xA6fmjGw7oDyo-NVSbj_fb1qwuRGUExcCm67qbKbMXCEb7ZD3r1PzMi7fiwhXelabqoFkLIf0gLTGQOwO967g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نخستین حلقه ازدواج جهان، که مربوط به ۳۲۶٠ سال پیش است، متعلق به ملكه "ناپیرآسو" همسر "اونتاش ناپریشا" پادشاه ایلام می‌باشد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/674027" target="_blank">📅 11:46 · 31 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
