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
<img src="https://cdn4.telesco.pe/file/IywVzZmRifxaktD1_TnuGi0ZQaRajNUgPaDOiLAtpMXvZmdJlw0xEurOFDerKRSdlq1rLmM6dlmJz9NpSY3Mq9r4JZ2txvQVfVT48jdVcV2QLfxm_C_zUAOFUfOX72rMXcNBfWOhhYcx-OkrkO4sfjiMIA4BdVrOK2JT5CdwrMfO5aa9QpIyn7d5MN9FO3rJd0wG6VwFKVaPP0Xuxxo7uwUrYuY_NnL_rw-_R5D9klMzCJYibIYztAdd2mSRO7TRFyYwi4uCOsr9WoW5soKwGjrr8iyzhEuCunk-yU-cbw_BXp5NV6ypAW8whXmKBdP_UGDlGF3AnkwQrxC_nM_J-w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.03M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-16 11:37:30</div>
<hr>

<div class="tg-post" id="msg-679129">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/akhbarefori/679129" target="_blank">📅 11:35 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679128">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46cd3dfb68.mp4?token=ncWyk2Y0rpY9MWPMpiIyTr_jR30FAoOuRbra8EOYsd5n1O9fgy2-tHQVVhysPqk8vtMeLgRFdjg8TJfqROZCdXZ8Wy56al7E0lhifkKS9KjRE-PAPLKP0pBEcLgQEpak2Ib0m7YYuT27ran_OCItV7S-n_XUVsg3RP79xJB6NKr3VQ8bCn0ruY5vFZLI7iUK4kxRtDWGz1FoAREEUzwuhnv5nC7G_bkCFKIsyc1W-B8erYJbh_8nuXhg1hLUlowyP00bJHe8fE57x1xdopQHpuQrksv8D_-K3XTmG2dMv8RFGARV9poso7aB80AJxEamnbzIuzS_uXBEciPp-Vb_Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46cd3dfb68.mp4?token=ncWyk2Y0rpY9MWPMpiIyTr_jR30FAoOuRbra8EOYsd5n1O9fgy2-tHQVVhysPqk8vtMeLgRFdjg8TJfqROZCdXZ8Wy56al7E0lhifkKS9KjRE-PAPLKP0pBEcLgQEpak2Ib0m7YYuT27ran_OCItV7S-n_XUVsg3RP79xJB6NKr3VQ8bCn0ruY5vFZLI7iUK4kxRtDWGz1FoAREEUzwuhnv5nC7G_bkCFKIsyc1W-B8erYJbh_8nuXhg1hLUlowyP00bJHe8fE57x1xdopQHpuQrksv8D_-K3XTmG2dMv8RFGARV9poso7aB80AJxEamnbzIuzS_uXBEciPp-Vb_Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روزنامه‌نگار انگلیسی: تنگه هرمز به نماد یک تحقیر تاریخی و ماندگار برای آمریکا تبدیل شد
جاش گلنسی، روزنامه‌نگار و نویسنده انگلیسی:
🔹
تنگه هرمز به نماد یک تحقیر تاریخی برای آمریکا تبدیل شد. تحقیرى که ممکن است برای یک نسل در حافظه‌ها بماند؛ اگر نتیجه به‌کارگیری تمام توان زرادخانه و قدرت هوایی آمریکا علیه ایران این باشد که اکنون جهان برای عبور از تنگه هرمز مجبور به پرداخت عوارض شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/akhbarefori/679128" target="_blank">📅 11:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679127">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/346dcb5023.mp4?token=NkXagdSMQXL8ARusRdbuoSqCM8mltlMwpffDo2WHQraFqCDDm0EVptxZLmOBSUU8tme8lKaqbqW0elDMmF7KoF0sg1b2PAO7odq-azAe_ziYGIFGfpdMNJ7qA_BAfWWNXYH4_j2qKbQRgSoYKfJ2OAd0LaGBo3FwuC3vuX2qzPZpFd2Zh5VPYL8voQzkiFuYTy7ZJWc7UUk8pVoOKlQLTwb_P3ikniv4Tq0G8zXOa0I5qBMWUjmud8sofWQFYTp-fnHmLObuBgbpQA4m4PnnbVRHwXgw_2p2pGii3DSDO4OxCWFOoODTjHR3DDwJJ35nf-yyN0YZrcgRmlEt2wZX4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/346dcb5023.mp4?token=NkXagdSMQXL8ARusRdbuoSqCM8mltlMwpffDo2WHQraFqCDDm0EVptxZLmOBSUU8tme8lKaqbqW0elDMmF7KoF0sg1b2PAO7odq-azAe_ziYGIFGfpdMNJ7qA_BAfWWNXYH4_j2qKbQRgSoYKfJ2OAd0LaGBo3FwuC3vuX2qzPZpFd2Zh5VPYL8voQzkiFuYTy7ZJWc7UUk8pVoOKlQLTwb_P3ikniv4Tq0G8zXOa0I5qBMWUjmud8sofWQFYTp-fnHmLObuBgbpQA4m4PnnbVRHwXgw_2p2pGii3DSDO4OxCWFOoODTjHR3DDwJJ35nf-yyN0YZrcgRmlEt2wZX4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خودکشی ضارب ۱۴ سالۀ مدرسۀ تایلند
🔹
دانش‌آموز مدرسه حومه بانکوک، عامل تیراندازی بوده که جان حداقل هشت نفر (سه معلم و سه دانش‌آموز) را گرفت.
🔹
او پیش از یورش به مدرسه، پدربزرگ و مادربزرگ خود را کشته بود و در نهایت، در مدرسه خودکشی کرد.
🔹
مظنون دانش‌‌آموز کلاس نهم (حدود ۱۴ ساله)، ۲۶ گلوله شلیک کرده و ۳۴ گلوله دیگر در محل تیراندازی پیدا شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/akhbarefori/679127" target="_blank">📅 11:23 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679126">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
ثبت تاریخی‌ترین کاهش تردد در تنگه هرمز
🔹
باوجود این‌که ترامپ از تسلط بر تنگه هرمز می‌گوید، داده‌ها حاکی از سقوط آزاد تردد در این منطقه به میانگین ۳ فروند کشتی در روز است.
🔹
براساس داده‌های کپلر، میانگین تردد روزانه کشتی‌ها از تنگه هرمز در دوران پیش از جنگ حدود ۱۲۰ تا ۱۴۰ فروند بوده  و این رقم در دوران اوج درگیری به میانگین روزانه به حدود ۱۰ تا ۱۳ فروند رسیده بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/akhbarefori/679126" target="_blank">📅 11:21 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679123">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EX2nBnNNOuxZoptok_3JtB3XDuudYvoP1I7QrrPw232c8TogkmB0i7o8jczGEYgu471a42D4P64kmOHZ2DVieGRIcxDvFtMi5XZ7KtdrRSZt-Nk2-i0ueuVugxeHdOzAEMDz-BfBznKTqO13LVELnhtQxQs5VFt1wa_SagLi0VQ5lHCD1zrGf0TPdBwJL8-ugItiiyD9waDHb1FpR9yK7cHpI7Ne1MtsaAYe-3cIcUvCYLjew9S7uvR3Figs40cpaETA3S_5v-xJMiP_5Oe9FuA8X4HFtp2C-yjjlO2V5icbuY4qr7gLprk2lnLLo-A7rNuUQNVqUFA-T7jEzahbMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F4vueUm6HjOY5ZPWL2r5zD_6skVmjOdTXhL-TQ42tbDSFmdxVt9pcsz6Y2kE7foT_s1BYyXbBwQTl41fFZf6a-DwPMECYozf-tDP2c_PfnoChej0QIZkfNEV19CEmY9ONnPTQp09pvcYrec2PnfndoK3GvF9n38AnFjpJ1kUUIQSg0KcnyUm7XuFkjbhbJSYWTHKyVJOK_lOJgpZ3a65DJ8W1pLRUPcWXFzs7c2xsbRvMDbeD686gK1boWpcYV2LyLZFiVzQoYfS-ryE9yKcCaBWY-sdXf3AP1DGFqhaJMHogvcSS4h4Bf_5dfaL4E8ioW6U-LadltzfcWU2sib5kw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
این گربه‌ای که می‌بینید پیرترین گربه‌ی دنیاست که جدیدا ۳۱ ساله شده
🔹
غذای این گربه فقط آب معدنی با ماهی سالمون، میگو، مرغ و تن‌ماهی هست! اکثر گربه‌ها متوسط طول عمرشون بین۳ تا ۱۲ ساله.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/akhbarefori/679123" target="_blank">📅 11:09 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679122">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
منابع عربی از برخاستن ستون دود از مواضع مزدوران عربستان سعودی در مأرب یمن بر اثر حملات مجدد یمنی‌ها خبر می‌دهند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/679122" target="_blank">📅 11:04 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679121">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
هشدار اطلاعاتی آمریکا: روسیه شاید به ناتو حمله کند
وال‌استریت‌ژورنال:
🔹
ارزیابی‌های جدید اطلاعاتی آمریکا نشان می‌دهد که روسیه ممکن است به یک کشور عضو ناتو، حملۀ محدود کند.
🔹
طبق این ارزیابی‌های اطلاعاتی آمریکا، حمله روسیه به ناتو در فاصلۀ پاییز امسال تا سال ۲۰۲۹ انجام می‌شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/679121" target="_blank">📅 11:02 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679120">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7af38b512f.mp4?token=O77fElw8zUIY9v5GTLc-Y3rvhQtx2IU7Svt9mEPItuD574emLJTsBCC6TZTewhiOuIyE41OVgc4Dc9r0vSxgLntUubYDBsECwj5cnmTNvl4dch1XD4dEcvBrmyqahNW970J5-83rKsr2qEJiy7hTRWC9o95JmOEnMOzKmRaAPyPaR-x9-FURQLlqt6m6icTzLwXDERPO5RdROFGNkGdWcfhs2hdC3ERBWIdpvNs7WaFtnb53J79U4tW8chVJ_zJiiKyChKw38wQ3A2VYgcZTug0D0s7Kyd5SahSCZ2a8WZ7Q8sgqLN3cXAR00G6DoIZOAZxgTbliXmkhNk_w5uTE0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7af38b512f.mp4?token=O77fElw8zUIY9v5GTLc-Y3rvhQtx2IU7Svt9mEPItuD574emLJTsBCC6TZTewhiOuIyE41OVgc4Dc9r0vSxgLntUubYDBsECwj5cnmTNvl4dch1XD4dEcvBrmyqahNW970J5-83rKsr2qEJiy7hTRWC9o95JmOEnMOzKmRaAPyPaR-x9-FURQLlqt6m6icTzLwXDERPO5RdROFGNkGdWcfhs2hdC3ERBWIdpvNs7WaFtnb53J79U4tW8chVJ_zJiiKyChKw38wQ3A2VYgcZTug0D0s7Kyd5SahSCZ2a8WZ7Q8sgqLN3cXAR00G6DoIZOAZxgTbliXmkhNk_w5uTE0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آینده‌ گوشی‌های هوشمند
🔹
این گوشی رول‌شونده به نام MOTOROLA RIZR فرم کوچکی داره که توی جیب جا می‌شه، اما وقتی به صفحه‌نمایش بزرگ‌تر نیاز دارین باز می‌شه!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/679120" target="_blank">📅 10:52 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679119">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28871f432c.mp4?token=UXGvgcpCEZg4Vrd0BBlbzEYj1afOjy1a4kQcVI55z_E4L_noaaTAOx6moEFBZ_OXro6xyHLnfDPL-WS2jG8wB3H49KXVv10ezGR2stfCNZvNutM5zIjm0pg74xBZ65IFsc-0Y1kEnk5ux8SJWLpIuT7_JZWy5b3-mfTEoP-6hRuYZLlS4vV6bfWgFTmUgR74DH5PjQTb3SxCSAAzAvW2Kla0LCV9JYY2q709f7XgKQNnRr4V7h-linMy0A5JVpZcVbJsiQz7ibX4waErLKkfUgSgTd_2vuEPmSCvkFQTGv-9wNvZ6u_0-8dkrhS9bOUNwGzZPfzfahO_qLKJ-ykRhq8RZ__eciMXYUvICTYG0jhYM9NSKtAQbnoO9BAYyDBv8dKSXwk2cBJhb8Q9TtqjNA4jmebywXljqfzsXTndkD-krA8V0a3JGwELtzeMJlc2Z1KsWlANQDARdzwrkD88Yvpt1881mvmSrxxPaTf0Vz5emnVYZvo8A1MkygqyD_NCQqLxQD7tmeZ7fC0_L-Yfcnoy4xRZuh5An3VxKg8ioca2lTPonxuD0wEv0A4FMtqn7SHAajbIn7GiZo-krtNlGfCVNHhR3YzOI1MpLCp6dcy_c8Mr-6Rvq4z4EDWDL278-Jo1suYSuGCq0fCTD86UcGbKePVbA9-fhT7r2ZJr5Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28871f432c.mp4?token=UXGvgcpCEZg4Vrd0BBlbzEYj1afOjy1a4kQcVI55z_E4L_noaaTAOx6moEFBZ_OXro6xyHLnfDPL-WS2jG8wB3H49KXVv10ezGR2stfCNZvNutM5zIjm0pg74xBZ65IFsc-0Y1kEnk5ux8SJWLpIuT7_JZWy5b3-mfTEoP-6hRuYZLlS4vV6bfWgFTmUgR74DH5PjQTb3SxCSAAzAvW2Kla0LCV9JYY2q709f7XgKQNnRr4V7h-linMy0A5JVpZcVbJsiQz7ibX4waErLKkfUgSgTd_2vuEPmSCvkFQTGv-9wNvZ6u_0-8dkrhS9bOUNwGzZPfzfahO_qLKJ-ykRhq8RZ__eciMXYUvICTYG0jhYM9NSKtAQbnoO9BAYyDBv8dKSXwk2cBJhb8Q9TtqjNA4jmebywXljqfzsXTndkD-krA8V0a3JGwELtzeMJlc2Z1KsWlANQDARdzwrkD88Yvpt1881mvmSrxxPaTf0Vz5emnVYZvo8A1MkygqyD_NCQqLxQD7tmeZ7fC0_L-Yfcnoy4xRZuh5An3VxKg8ioca2lTPonxuD0wEv0A4FMtqn7SHAajbIn7GiZo-krtNlGfCVNHhR3YzOI1MpLCp6dcy_c8Mr-6Rvq4z4EDWDL278-Jo1suYSuGCq0fCTD86UcGbKePVbA9-fhT7r2ZJr5Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یزد؛ دومین شهر تاریخی جهان
😍
#اخبار_یزد
در فضای مجازی
👇
@akhbar_yazd</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/679119" target="_blank">📅 10:41 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679118">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZ7gvfu6n75MY06IJMkWjfQBAeSDvieWAYqcWsb21oloQI4FmmCDk07rphFIvwiBwddXIlOYpln4HivBi8n8tpfGdWXayshSCUE2CELVHVJWBbLDrPLEsvx4SM9gqRSiHW2TpkKB48sKxkAe21iTAUaLGS2qQBZNuihL1RsXCKNtfT7nFQoDjcFlCYiUBZfnTNfNMFrKAM-Z96Qh8BhskJTS_RNCXM-Ia9SZtBln113K8Zla0n03RY3fGR4I8mTVWjXFb16XW1gxEu3OqEbwHQOBFANB7jQxWlw9bmeSJS2yJMvbodm6FoAv1T7ShvYkAfCXwxgpsyESWFYFuyCJuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
احتمال وجود حیات در اقیانوس مدفون «اروپا»
🔹
دانشمندان می‌گویند قمر یخی «اروپا» با وجود اقیانوس عظیم زیرسطحی، همچنان یکی از امیدوارکننده‌ترین مکان‌ها برای جستجوی حیات است، اما پژوهشی جدید نشان می‌دهد پوسته ضخیم یخی آن مانع از رسیدن مستقیم آب اقیانوس به سطح می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/679118" target="_blank">📅 10:35 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679112">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FBnfxrwUHa2GmT6HiBHQVGrXWV0BtSOcw7Y2Er0q7JZwBC4-tLVUeOyRHmj3iCA4v1IDRoC4nskBSFlENLiVhjrqcbREnEwioSC-4ZksChYgdnngcHKpa-1u0CIqSF9xHKFKNe6QsJG7HvW3rS13unYaAcN3RnUtEfinX2E-qRnmSyshBMeNYLGe4g0GbVqxZy9ZR1_PBetXTMNs0g8585i_mDwvbanjcjTDuV-gs0dPI5_O7BjwtvTQjF2ZnQkM7nJhMfjBzyfnucrmIFw8upx5VcIqoYP-CV213V_f3JYt24Q_vK_XIWQi_7OFLvvKSo2ZY2NrfoHPYZxGoYt2rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i4rIhk2hdXtEbYVKiDTa2PTRS_P5HBuJpdf2j_g6kBHZML8AcWp7hFqVUwzvY4XEPUhtCkf5EymochEHM0lZ3hpkgkxqkSWm6h2A4gw-bTAl8vTJWRGJXRhDMpFX_FMxZNeBJyRB9nGFF3pn3ksqsK5bjL47q1XukOgq9c-ZiBvO_zmhkWbrKLkIo_Vdc8UuiKue1OFRnOoNh11RmL132lR4WkYGnYmY4TmGnVb6J2coaIBYix-deJCA3gROSAgcvo--7Xnki5yrCJk5fDErG8D1r44YofVQo6QkSjh-Xe4Do67B_HvuBBF4-MPiFi4VDoBQReZahexrBFNl5mA50g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fmujQg2XDTPeKjOqweJ3lKOWHhfYJAQAQw2I08LLS2WKbA3rB-XuTNXq2eJNCl7vJn6908O325kSHStRFXzWMXFg4KZhHiRMlU7eWAUGkymJvSNzthyMnJvsRGTnPetm3Jj1-m19Dg5RRGe8i7W8i38eq-z7t1RpTF5fgfQvbS2F8I2mHx6QHOrKcPU8To-FgpnRUpEVYiq4_D6XWlOUyMTvNDfEy2W8HzDs2IAcb5YAvS4KC22eXHY-L0hQIN12Un8w0r6jBK4QTJuEHn2Cr2cwVqH74p-FNmBfCluczjbeMqzgub6-XzlXJV6egqfc1M-V3A9ncOhYq-ba_ujC8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qsJt7Mkszrksfj5ysf25KqWGCEZZgV_i0PwPE6QElWWSxdLI9r7D96q2ulw_QeRec5ZvXVGlXVdpFezzyBWJKRdSa0EjsHGLhuqLelyxD5pLFu0Yr3DtmtZaEV3XWwf5DzIACfrZdhgmBq9UTBtle9M69VRV49nmXzxYzQy2L89h7MIHw0nc2fomqw4Y5T3Jb1Xk13joWWI3n5smxE-zydhyqxC36tXK_JQGCZBepMT27ftqfjZutsKjVyZ0wumNGuw6enfRbFjSuI3lhNeaxwQwOUWQv_7iZ9s369rdHuzUfdT0HhvtQ7P8Y9KWEsDDVl1lYHxuyVIlpqfr8nroew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qi_mtSzPNm9XETVRbQIkGi3YPObQzveW-M8Zrv-8Lz-e_ahtq8AUqLMYP4uZF7B68dPCagJgqb3mYFaA19jxtAzOiBE2GdMCyyehq7vb1XtqW7TBVROz4kB06QLEWtr7LUQDsKAT_JBOcI8DyRmqAN4s6nL7J7YaB-OyguHAT5k_GkjUtAT6CUuS05W6fnhhNEWyXYRrKaJ2ro4IllpjmiaA9g8rrDq1I2q8UlE-gZgUDnfJ1jH927rKqsgLIEr2enR4X06tlL1H_OV4-XB0XklyCQny1p5s3TiOgMB4IQGZgVBm55giGR7rBqUDEZQm1ynNnvCcaykS6l416QT9hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IFtwK7FeSi69RMhAcdmkptOjMZT7VKjAt_1hLw_JCu10NmS4OoaNJJsVL6QMdb4L6AGLcMjNdFLU8D2j761jkJ7JLjl0IcO3gt3UqlrfVxNtBZt2tsYm5vz_tGQjNFQCKeXmnKNmh4MPnLKE2JoiSlimTi5X2KmJQyvMWZM_tNESHtO4660dR-io2XW6aHyQvOcFEL7tXtKecNIB3XVPiwaOgZLjpwrKC-XwE_BWgz9S1ky2GjQsd-V-AMLzrkt_sYVBV3qg24pBQANFkQC_nfg355bXBjhKzPLIrA2bBX_0QTs-HwYm7sdULtmX5ZlPXnDClqQw462Z0La8ZoWz1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ترش، تند، وسوسه‌انگیز؛ آموزش تهیه انواع ترشی‌های خانگی
😍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/679112" target="_blank">📅 10:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679111">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
قیمت نفت در سایه نگرانی درباره هرمز افزایش یافت
🔹
قیمت نفت برنت با ۰.۹۷ درصد افزایش به ۸۳ دلار و ۲۹ سنت در هر بشکه رسید.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/679111" target="_blank">📅 10:28 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679110">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
تجرد قطعی در ایران؛ از وضعیت فردی تا سبک زندگی
🔹
به گفته یک جامعه‌شناس تجرد قطعی در حال تبدیل شدن به نوعی سبک زندگی است و بخشی از جامعه تمایل بیشتری به مجرد ماندن دارد؛ آمارهای رسمی از بیش از ۱۸ میلیون مجرد قطعی بالای ۴۵ سال و بیش از ۲۴ میلیون نفر مجرد بر اثر طلاق یا فوت همسر حکایت دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/679110" target="_blank">📅 10:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679109">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔹
خبرهای متفاوت هر روز را در وبسایت خبرفوری کلیک کنید
🔹
🔹
همه چیز درباره توافق مهم ایران و عمان بر سر تنگه هرمز/ این تفاهم جنگ را برای همیشه پایان می دهد؟
👇
khabarfoori.com/fa/tiny/news-3235999
🔹
افشاگری رویترز از علت تعلیق حمله به ایران
👇
khabarfoori.com/fa/tiny/news-3235850
🔹
اینفلوئنسر مشهور در پخش زنده کشته شد
👇
khabarfoori.com/fa/tiny/news-3235919
🔹
اعلام آمادگی یک نماینده مجلس برای شلاق زدن باقر خرازی
👇
khabarfoori.com/fa/tiny/news-3235825
🔹
عذرخواهی سحر دولتشاهی درباره استوری خود؛ قصدی برای بی‌احترامی به اذان نداشتم
👇
khabarfoori.com/fa/tiny/news-3235984
🔹
اخبار لحظه به لحظه جنگ ایران و آمریکا
🔹
https://share.google/8EImhrm9fBFYjsyZr</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/679109" target="_blank">📅 10:25 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679108">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7026900c0e.mp4?token=byNbkkwjIlDxC6kbG4eSQ770lrxG-J4v6Br33Ku9lxH9B8cwAmvScc5dGb4PEIxtL3YtdhBUWMZagqnJGkXwoI1IoQQG70miuEjv0JHF2xKY_D4ksR0KjWGxomUDkPZqsFA44J3KoYQ3NyDZOL8v7VBokiQMsSZX8_QMSc41hzhKabQwj7-V5iOVjG40ycppcIRUI_Ztk8Tj03oqBQ8AYI3fYBfFpEofBJU2lZ9rALL8YeA5urbB33rOdoP-Gr9FLQb5Jr_hhW4pOjr0EFydWTd6ML7FnjsB6a5sYlDY4lghHOhbUg5l3MdjksnIgw7lOgJ0I0dfYyAeNd__YYwkNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7026900c0e.mp4?token=byNbkkwjIlDxC6kbG4eSQ770lrxG-J4v6Br33Ku9lxH9B8cwAmvScc5dGb4PEIxtL3YtdhBUWMZagqnJGkXwoI1IoQQG70miuEjv0JHF2xKY_D4ksR0KjWGxomUDkPZqsFA44J3KoYQ3NyDZOL8v7VBokiQMsSZX8_QMSc41hzhKabQwj7-V5iOVjG40ycppcIRUI_Ztk8Tj03oqBQ8AYI3fYBfFpEofBJU2lZ9rALL8YeA5urbB33rOdoP-Gr9FLQb5Jr_hhW4pOjr0EFydWTd6ML7FnjsB6a5sYlDY4lghHOhbUg5l3MdjksnIgw7lOgJ0I0dfYyAeNd__YYwkNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله جدید یمن به مزدوران سعودی در مأرب
🔹
برخی منابع یمنی از حمله ارتش یمن به نیروهای وابسته به عربستان در پادگان صحن‌الجن مأرب خبر دادند.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/679108" target="_blank">📅 10:21 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679107">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromورزش فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ghr246KRyiqskIyhyq0OyL2JRcuovM7xrp2Hi-FEKxabWEjAgGb-JcArKiHYXLXrKnmCDyqC6q78Lvem9hvKu23HgLnJxPggdzwrg2c4qOXrqHQ_EP7TsYiANSsOPuiXC2JfJyokQmTo62mIsyqb3KePRV5TVNUDlhSa5w5Ss0DG_TdbLlCN9cbhZX8fOxXQ-jbqzr8YKSD0RHeCprGCpgCZLBRgZeNQLk7QZmZiaJvxIp5AO06Igpk_wQDqAFZISsGL_Z3Rcbzt9GO6pYnCWyHoT6ytZODNr_QEPM4VqAicfqMitZXDyQaaLFchC9WiUw9TD1F2PmGta4BrsdvvJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایجاد تاخیر برای جلوگیری از تماشای مسابقه شناگران پیش چشم مادران مشهدی!
🔹
مسابقات شنای کودکان شناگر مشهدی در حالیکه قرار بود امروز در استخر شهید هاشمی‌نژاد سعدآباد این شهر برگزار شود با اتفاقی عجیب روبه رو شد. این مسابقات قرار بود از ساعت ۸ صبح آغاز شود و در شرایطی که مسابقات آغاز هم شده بود، ناگهان با تصمیم یکی از مسئولین هیات شنا متوقف شد. این مسئول ناگهان با ایجاد اختلال در روند مسابقات، اعلام کرد تا وقتی مادران در سالن حضور داشته باشند مسابقات برگزار نخواهدشد!
🔹
این تصمیم عجیب در شرایطی که مادران بی صبرانه منتظر تماشای رقابت کودکانشان بودند، با واکنش خانواده‌ها مواجه شد. تاخیر در ادامه برگزاری مسابقات و لجبازی مسئول مربوطه در نهایت با ورود مسئولین ورزش استان ختم به خیر شد و با استقرار مادران در بخشی از محل برگزاری مسابقه، مسابقات ادامه یافت.
🔹
گفتنی است عموم کودکان شناگر حاضر در این مسابقه زیر ۱۰ سال سن دارند!/ورزش‌فوری
@fori_sport</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/679107" target="_blank">📅 10:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679106">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
رویترز: هکرها شرکت‌های مالی بزرگ آمریکا را هدف گرفتند
🔹
هکرها طی هفته‌های اخیر ده‌ها شرکت مالی و سرمایه‌گذاری آمریکایی را هدف قرار داده و دست‌کم ۷۲ وب‌سایت مخرب برای حمله به کارکنان این شرکت‌ها ایجاد کرده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/679106" target="_blank">📅 10:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679105">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ad7d62d37.mp4?token=WMoAJqJpLRSdlirio0RPfGxwhfbXUKoWBJnTLyUiSkQaqsJPvS10BzXxSJGiinO07Z2W9CqJm3k614I19MtviaZW3TTR9owcKkvp1xU7c-D4VZIpZQrWqP74Gq_ds48DvO6sl158ZNFjm91n71j2m0psKnFK7YIcaHfPNOINm9zkctRS3dAARIXLeVUuC0vSX-M_Zvr4nt2b6FPvWWooMpmby2WUKCjU07H45KEqjNkVWyADGMFRxbbPJleDIkJYlLAhgUpL4o8vbPAo0RlB7TF4tcNAo-aKEQ7zkMvgO5AOk6KmD9ohRd6XPXqo3YdF1r99W39UgMsvZgOKEZ80kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ad7d62d37.mp4?token=WMoAJqJpLRSdlirio0RPfGxwhfbXUKoWBJnTLyUiSkQaqsJPvS10BzXxSJGiinO07Z2W9CqJm3k614I19MtviaZW3TTR9owcKkvp1xU7c-D4VZIpZQrWqP74Gq_ds48DvO6sl158ZNFjm91n71j2m0psKnFK7YIcaHfPNOINm9zkctRS3dAARIXLeVUuC0vSX-M_Zvr4nt2b6FPvWWooMpmby2WUKCjU07H45KEqjNkVWyADGMFRxbbPJleDIkJYlLAhgUpL4o8vbPAo0RlB7TF4tcNAo-aKEQ7zkMvgO5AOk6KmD9ohRd6XPXqo3YdF1r99W39UgMsvZgOKEZ80kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ضرب‌الاجل مقاومت عراق به دولت و تهدید به پاسخ نظامی علیه آمریکا و عربستان
🔹
مقاومت اسلامی عراق با محکوم‌کردن حمله آمریکا به حشدالشعبی در کربلا، به دولت عراق تا ۲۳ صفر مهلت داد تا توانایی خود را در دفاع از کشور نشان دهد.
🔹
برای حفظ امنیت زائران اربعین، پاسخ…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/679105" target="_blank">📅 10:13 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679104">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e445bf036.mp4?token=iEz8NNmDVH4haCISLec5gpJCOsULMULfFRG0PSXHIWSdYsI0y1cQGznV96ZB5uJPNOrSzrNccwG2NpdZVgqxxTLuZ_8vEVloZiBwwe-6l7vVMVW8u3KUqPU2TMEyN7Q-3CXnla4AIY7Ee2z-OuLJ7Q1k_h2fDLZN7ONF7sDQ61jodZuMKRxie281MZgysiYKv8h0-vo7b5dgcHm_epP1jvUpGMIghGJDTDJ27VEBI592SP_v1Ls-QwajXNiyNncmY72lQAfXRh7sGFvdNEoIBCkW2liQoCW5KTd4WnS2xqzvPi8haOVecrISD-IuDg7e7fppefglKzx7xZ7c4qPH0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e445bf036.mp4?token=iEz8NNmDVH4haCISLec5gpJCOsULMULfFRG0PSXHIWSdYsI0y1cQGznV96ZB5uJPNOrSzrNccwG2NpdZVgqxxTLuZ_8vEVloZiBwwe-6l7vVMVW8u3KUqPU2TMEyN7Q-3CXnla4AIY7Ee2z-OuLJ7Q1k_h2fDLZN7ONF7sDQ61jodZuMKRxie281MZgysiYKv8h0-vo7b5dgcHm_epP1jvUpGMIghGJDTDJ27VEBI592SP_v1Ls-QwajXNiyNncmY72lQAfXRh7sGFvdNEoIBCkW2liQoCW5KTd4WnS2xqzvPi8haOVecrISD-IuDg7e7fppefglKzx7xZ7c4qPH0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خودکفایی در صنعت پالایش؛ ویدئو وایرال شده از یک برج تقطیر با ظرفیت ۱۲۰ هزار بشکه در روز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/679104" target="_blank">📅 10:11 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679103">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f65c3ad0d.mp4?token=IFrvMYtIoHe_xQ3MfCItlj1N__EP-JE1-ztjV0nUDF293DLNO2FDzpVZCX3AmMJCEKCTr5V5dKEB_2f7p411963HSR2iEzgaKorL0qwnw_MovpSmZccPvAYIijIBF06kjuvVjG2ra_hSUinBROxRjOgl0BsHP7x6LE3kXJRd46p5KPXr1HnBFIgW3S_Zr5GzovBlQafeExqFAkW-1ix3wllAHY63sG7QStj8KDjyxDm0S2NtN5LSM2r0MlC21vY1_52UQ_0cSA0NAnRyaT3RUun4OjgmbQ69X9T95ior1RXYparhWLLJ0aa3_wkF9gqSoKtbEpIKatkOrlI7WOLrpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f65c3ad0d.mp4?token=IFrvMYtIoHe_xQ3MfCItlj1N__EP-JE1-ztjV0nUDF293DLNO2FDzpVZCX3AmMJCEKCTr5V5dKEB_2f7p411963HSR2iEzgaKorL0qwnw_MovpSmZccPvAYIijIBF06kjuvVjG2ra_hSUinBROxRjOgl0BsHP7x6LE3kXJRd46p5KPXr1HnBFIgW3S_Zr5GzovBlQafeExqFAkW-1ix3wllAHY63sG7QStj8KDjyxDm0S2NtN5LSM2r0MlC21vY1_52UQ_0cSA0NAnRyaT3RUun4OjgmbQ69X9T95ior1RXYparhWLLJ0aa3_wkF9gqSoKtbEpIKatkOrlI7WOLrpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برنی سندرز، سناتور کهنه‌کار آمریکایی: ترامپ فاسد و زورگو است؛ جنگ ترامپ با ایران یک فاجعه برای آمریکا بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/679103" target="_blank">📅 09:48 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679102">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
شرکت ردیابی کشتی کپلر: ۶ نفت‌کش از تنگه هرمز خارج شدند و ۲۱ کشتی این هفته وارد تنگه شدند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/679102" target="_blank">📅 09:41 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679101">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
نمایی
متفاوت از تشییع با شکوه پیکر مطهر رهبر شهید انقلاب اسلامی بر دستان مردم عزادار عراق در کربلای معلی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/679101" target="_blank">📅 09:38 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679100">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
حمله جدید یمن به مزدوران سعودی در مأرب
🔹
برخی منابع یمنی از حمله ارتش یمن به نیروهای وابسته به عربستان در پادگان صحن‌الجن مأرب خبر دادند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/679100" target="_blank">📅 09:30 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679099">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
کشف بقایای انسانی در ارتفاعات شمیرانات
کمیته جستجو و نجات هیأت کوهنوردی استان تهران:
🔹
بقایای یک فرد مجهول‌الهویه به همراه وسایل شخصی در شکاف میان دو تخته‌سنگ در منطقه بندیخچال کشف شد.
🔹
هلال‌احمر و عوامل تشخیص هویت در محل حاضر شدند و بقایا با دستور قضایی برای تعیین هویت، علت و زمان مرگ به پزشکی قانونی منتقل شد.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/679099" target="_blank">📅 09:21 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679097">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e205c1352.mp4?token=uiepUS2lrzJ10E4Iwpd0y9ghGvGiVxh2AsHZ46QvXtSec3_4-OYlq8M2rVfBGSxzEao2t2GEebePlf8FWvF23aR3508AiWekAZ7DQrlifTc_iuNLAlx24EoeXQ_7wIyghmrTVINO1e_aS0JQJt_yL6GZJVKejr3kCFau79vz_BBcH4w9EPhy3Btd-5V0Fy6ibdMURC9f5eddxPaDrLgh_lajYf2R3Vbx-25ICp8HsK5v4EDXzEal4qs9XXs6HNTsm2uFqhgvP5JhxaGqbN1NbK9pa1cauZnvyqpTfx1GDNuCmlFbF1ltVAtHvTbvpajUpEXXyAj5XLjbDUpshauc2AcEMdXzbGgPzr6JWsqdVhWjrdC8oXirpL1HqvXYbhkCqCKw7_LT9CLM7hxLO2lrOwQMz0sJAapHy-FBW7HtbvnMXjQ3SHpelvMt4Gw3X76nQ2P319s-i4OYQ8fuwkovT1bi1tJzX0rt8w-JYtXE9EDTW6UQGxcSwNsm5U4BmPqet1m51di3VTFWZUjD1iRWNZrPH58H9Grr-MhHHM55Uy8-wThsusPQaxhduK-XYJrur7I5Fwu_3BPYI2AmxkqB3QXvsI94CCAemaweua5cK_MGLhmMal8tGGP1RTFj8_BCiV6LxOaY0mdshrk7-YmWm7W_609LzzUyaR69GdT0L5Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e205c1352.mp4?token=uiepUS2lrzJ10E4Iwpd0y9ghGvGiVxh2AsHZ46QvXtSec3_4-OYlq8M2rVfBGSxzEao2t2GEebePlf8FWvF23aR3508AiWekAZ7DQrlifTc_iuNLAlx24EoeXQ_7wIyghmrTVINO1e_aS0JQJt_yL6GZJVKejr3kCFau79vz_BBcH4w9EPhy3Btd-5V0Fy6ibdMURC9f5eddxPaDrLgh_lajYf2R3Vbx-25ICp8HsK5v4EDXzEal4qs9XXs6HNTsm2uFqhgvP5JhxaGqbN1NbK9pa1cauZnvyqpTfx1GDNuCmlFbF1ltVAtHvTbvpajUpEXXyAj5XLjbDUpshauc2AcEMdXzbGgPzr6JWsqdVhWjrdC8oXirpL1HqvXYbhkCqCKw7_LT9CLM7hxLO2lrOwQMz0sJAapHy-FBW7HtbvnMXjQ3SHpelvMt4Gw3X76nQ2P319s-i4OYQ8fuwkovT1bi1tJzX0rt8w-JYtXE9EDTW6UQGxcSwNsm5U4BmPqet1m51di3VTFWZUjD1iRWNZrPH58H9Grr-MhHHM55Uy8-wThsusPQaxhduK-XYJrur7I5Fwu_3BPYI2AmxkqB3QXvsI94CCAemaweua5cK_MGLhmMal8tGGP1RTFj8_BCiV6LxOaY0mdshrk7-YmWm7W_609LzzUyaR69GdT0L5Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مدرسۀ تایلندی هدف تیراتدازی مرگبار
🔹
طبق آمار وبگاه تایلندی «خوسود» در این تیراندازی حداقل ۷ نفر کشته و ۳۰ نفر زخمی شده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/679097" target="_blank">📅 09:17 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679091">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a2ff432da.mp4?token=BlwVD6f0qSkkZIVlxOVzKWSa2UY_UHEniHb-0B2OLyUlae0Y0theZ_GhDlF6RxCKcx-tGVNsls2mFClnEccswQcPIclKl2nuMqla8Ycx86KHHt0bLN_5vyC9jfO9p_t0xf9ig-kbfm5Yz8DKqt1qB8YdBQoFGHzwOE5q0kFZWOgdH7kzwlhRcXyhBnveXKG9Xg6cseOUU3lE0mqC2aiI-fr0nMtSkP4N5USwGAqxOrTUws9Tj-lD5tw0NE_1cApikyZUF5vgxlo_19iDCLbnl3VALi3mII5e4rFF5Xnb4p4khbDs7vHunKCI6haDD1knu_HlW28wY1iNaMlafV-JzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a2ff432da.mp4?token=BlwVD6f0qSkkZIVlxOVzKWSa2UY_UHEniHb-0B2OLyUlae0Y0theZ_GhDlF6RxCKcx-tGVNsls2mFClnEccswQcPIclKl2nuMqla8Ycx86KHHt0bLN_5vyC9jfO9p_t0xf9ig-kbfm5Yz8DKqt1qB8YdBQoFGHzwOE5q0kFZWOgdH7kzwlhRcXyhBnveXKG9Xg6cseOUU3lE0mqC2aiI-fr0nMtSkP4N5USwGAqxOrTUws9Tj-lD5tw0NE_1cApikyZUF5vgxlo_19iDCLbnl3VALi3mII5e4rFF5Xnb4p4khbDs7vHunKCI6haDD1knu_HlW28wY1iNaMlafV-JzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حجم تخریب پادگان مزدوران ائتلاف سعودی در حمله روز گذشته ارتش یمن
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/679091" target="_blank">📅 07:34 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679090">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDzDhMJiRPQsQ_u3Dm3f2Fy8_rsKv0qgUp40hC000p7IFqMZ-LFvU75RWdJyiOxcC4SOi0JhX2EjjXHsXQ-lGE3nxH4WFWwKKTn1Nu8Z2r6p23kL2NmtoPbb6AJXoePCxmAM7-uK9Dz-XUaKNJfGo11Qb47jMKoabn3xu-RRL-zTkLv2yYrXWjsUzQu4He65evoa7TFuXrREAwXWP3RvgUKjAHHGSxj0yBUQENJP-uaouyG46vMeL2CyAMhY9EmGSuCwVbJwIFKODRr2ssInEBjecJ6aKtvS1B8RKNj2wW_ym_ATUhUMJubYRPV64wm-K1VMaYZTTtbwr4Iy4CL9YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز جمعه
۱۶ مرداد ماه
۲۳ صفر ۱۴۴۸
۷ آگوست ۲۰۲۶
جمعه‌ها
#دعای_ندبه
بخوانیم
⬅️
متن و صوت دعای ندبه
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/679090" target="_blank">📅 07:30 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679089">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eD90GhWUNbic7nz36Dn8Y0yqgA_yMRrrj_oiliN1zkMoOHu9brQa2Po4dFSbDoRJ48Rt8KzwUyDk9Dy3y_lOZs27MrUXwpC3MhQga6xO0Vc5nD8XlBY8VngSwJ1M0Z17ix86uONwGPsppFZalqAD4mWv2zSNCtetqs0DyA1CyvqPcSnu5CPrTePZayrlxA8_0t-1zzhJiE2BWk1ZhCLdr81MxdFfqG3al-MpfSzW49JbZoLwrAWlDW0Y0SSqMs_L_2Ti7Iyxi53--S_u3Hs9IOcUtaUiUqh0Bn0pZH2ZQTNJaiOl4ymG2ZoeTkTfOGT58PEZHxM6Z0hoPcy1E_q6lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفت ۳۶۰
مرجع تخصصی اخبار نفت، گاز، پتروشیمی و انرژی
✅
اخبار فوری
✅
تحلیل اختصاصی
✅
استخدام صنعت نفت
✅
پروژه‌ها و مناقصات
✅
بازار جهانی انرژی
@naft360</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/679089" target="_blank">📅 07:07 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679086">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
رد پای موساد در بحران مهاجرتی اخیر اسپانیا
🔹
محافل اطلاعاتی و دانشگاهی چین گمانه‌زنی می‌کنند که اسرائیل بحران اخیر مهاجرت دسته‌جمعی در منطقهٔ خودمختار سئوتای اسپانیا را طراحی کرده است.
🔹
به گزارش روزنامهٔ ال موندو، در پکن گزارش‌هایی در دست است که بر اساس آن‌ها، هجوم مرزی یک عملیات حساب‌شدهٔ جنگ ترکیبی به رهبری موساد بوده که با همکاری مراکش برای بی‌ثبات‌سازی دولت اسپانیا اجرا شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/akhbarefori/679086" target="_blank">📅 02:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679083">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
رویترز از دو منبع منطقه‌ای گزارش داد: ترکیه، عربستان سعودی و پاکستان امروز در عربستان قرارداد دفاعی مشترک امضا می‌کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/akhbarefori/679083" target="_blank">📅 01:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679080">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8da4c49a2.mp4?token=sHOxKlw5YOnfv6sePq5Krt-CHt8XTCQmIBDDxQ_xVSToDM-hc28K8PGhGKDF0k1oPvb8xuVk59iawOsn-zHud9HSmUIlm1QZqbV5G6n-77d11LL1bXWZ89PrYRDzY21XZK7c6fg41rNVhz11bZbprYAUQFyGVmhCVLh3gDL9RbkvM-LE8RM60tnY_RSW6_Z9arCkzsIsZPX6a0HEqt8DIclcCrAIJ7o5XXQlvCShIUp6aA8yool9ZO-sgQDyQm7qkokOJSYM0hMGaiOw_f5laGvPOjN9UTW_sbMlJxmFQgfXpAd1CNt8xHBm9aqcM-EaLuFIgwIrRxm1FFWl44Agl4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8da4c49a2.mp4?token=sHOxKlw5YOnfv6sePq5Krt-CHt8XTCQmIBDDxQ_xVSToDM-hc28K8PGhGKDF0k1oPvb8xuVk59iawOsn-zHud9HSmUIlm1QZqbV5G6n-77d11LL1bXWZ89PrYRDzY21XZK7c6fg41rNVhz11bZbprYAUQFyGVmhCVLh3gDL9RbkvM-LE8RM60tnY_RSW6_Z9arCkzsIsZPX6a0HEqt8DIclcCrAIJ7o5XXQlvCShIUp6aA8yool9ZO-sgQDyQm7qkokOJSYM0hMGaiOw_f5laGvPOjN9UTW_sbMlJxmFQgfXpAd1CNt8xHBm9aqcM-EaLuFIgwIrRxm1FFWl44Agl4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مغز خودش رو بر اساس چیزهایی که بیشتر بهش گفته میشود شکل می‌دهد
🔹
هر بار که به خودت می‌گی ضعیفم، شکست خوردم، فقط حرف نمی‌زنی بلکه داری به مغزت یاد می‌دی که این‌ها رو باور کنه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/akhbarefori/679080" target="_blank">📅 01:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679079">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/254b28154f.mp4?token=HLtxkthO5ppuvMIBNa7HRdCUExBm3pMCFIJtMwAo4BE1mhNGhEaHDFCZUN_FqmzSkQcL5x_rymU1Qq-xckxg93m_f08c8OIW4w5iIeRDWuk3_WqgnNMFlFvpwrvM0KdOMPTNCsG2aHASJgA_nlEBiVkSqmgRwjVhswqJNo_2xxFi6ctO6fLgH_lDWFUvp_uo9NUs0CIEbdlszUZDud5RNJtRwaRgB-vxVZHstg1YZTuQoGlLsVEtheojSnEA7L74oFihIPWG6dQE8UTq74QXy2hSZdy7UGRZ_Uk6hClJPFU4D9msHl3cXjN5e_9cH9QRQaKrljxjZqC7rjFD3AFauw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/254b28154f.mp4?token=HLtxkthO5ppuvMIBNa7HRdCUExBm3pMCFIJtMwAo4BE1mhNGhEaHDFCZUN_FqmzSkQcL5x_rymU1Qq-xckxg93m_f08c8OIW4w5iIeRDWuk3_WqgnNMFlFvpwrvM0KdOMPTNCsG2aHASJgA_nlEBiVkSqmgRwjVhswqJNo_2xxFi6ctO6fLgH_lDWFUvp_uo9NUs0CIEbdlszUZDud5RNJtRwaRgB-vxVZHstg1YZTuQoGlLsVEtheojSnEA7L74oFihIPWG6dQE8UTq74QXy2hSZdy7UGRZ_Uk6hClJPFU4D9msHl3cXjN5e_9cH9QRQaKrljxjZqC7rjFD3AFauw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شهید حاج قاسم سلیمانی: ما در زندگی خودمان باید به الگوهای بزرگ نگاه کنیم؛ عمر ما می‌گذرد، تمام می‌شود، همه می‌میریم؛ اما انتخاب راه درست خیلی مهم است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/akhbarefori/679079" target="_blank">📅 01:24 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679075">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6460030eb.mp4?token=RDjr1ZzWkqW7BAvAFE9Nof8Lq3xPclAN-Nyu00TOsWKzZZXZtFYwQx0mAL4UxqwsCibnPp18Lsuuw4dwB8oKHmCCgGoPJT6UtGfkJt_qPUa7mXjTELR7kqI2H_V7z8jcOOZKFLZrubBgJcfSOzac_h_B7ejB3O8cNCxjbYlhIBzMBRfb1vDxuLKJAJ3vYA7qOAffaa7fVSEiC1NuDNIZEr0UjbeIuydoNO0fcKiMjCfS5_gOZ5fxNWVTacEvP5Vw_jYEyJLaSsjzYHsWT10yb2ErTbs9gxTjEwTS8SuCdL2cU0zCLA71sFR_782RcFKelo9-C8NW4bqCmp1W_fm38A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6460030eb.mp4?token=RDjr1ZzWkqW7BAvAFE9Nof8Lq3xPclAN-Nyu00TOsWKzZZXZtFYwQx0mAL4UxqwsCibnPp18Lsuuw4dwB8oKHmCCgGoPJT6UtGfkJt_qPUa7mXjTELR7kqI2H_V7z8jcOOZKFLZrubBgJcfSOzac_h_B7ejB3O8cNCxjbYlhIBzMBRfb1vDxuLKJAJ3vYA7qOAffaa7fVSEiC1NuDNIZEr0UjbeIuydoNO0fcKiMjCfS5_gOZ5fxNWVTacEvP5Vw_jYEyJLaSsjzYHsWT10yb2ErTbs9gxTjEwTS8SuCdL2cU0zCLA71sFR_782RcFKelo9-C8NW4bqCmp1W_fm38A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مراحل آماده سازی موکب هیئت "قرار" در محل "تپه سلام" مسیر منتهی به مشهد مقدس برای استقبال از زائران پیاده امام رضا(ع)
@Heyate_gharar</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/akhbarefori/679075" target="_blank">📅 01:04 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679074">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
در ۳ دقیقه ماجرای شایعات این روزهای دریای خزر را بشنوید!
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/akhbarefori/679074" target="_blank">📅 00:54 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679073">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc78f30d4e.mp4?token=nnrG10_f7SX5L5-cio0ThjnwXSbE4oHEfmiQGvTnPpmDaN7kbXfVShj7deSYnlUXBESdD0bYRydU3M10TcGKAwFjpFK_IAP-AzSzuJIO4t1Lglz9eXJMuTURumIVm4mPgSQOZjSQ-MsCtcIJgF70Z6b6TOlwyOV6mpjf04oytdpcu7ebnxlrU4-RhJOet5_SS4mVWolpaMGXzex_c5rMt12jBLIEl2w56UH1MSPTcYktq9ulN5uYvBwD0pMCN6u9kIqAbjb85XvZFMKz84yxc4_atCJi6XecpykfmCmpBMScR7GRmZWeVfN8B8tTtkuz4qSszIjru0V8IVMneTKWmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc78f30d4e.mp4?token=nnrG10_f7SX5L5-cio0ThjnwXSbE4oHEfmiQGvTnPpmDaN7kbXfVShj7deSYnlUXBESdD0bYRydU3M10TcGKAwFjpFK_IAP-AzSzuJIO4t1Lglz9eXJMuTURumIVm4mPgSQOZjSQ-MsCtcIJgF70Z6b6TOlwyOV6mpjf04oytdpcu7ebnxlrU4-RhJOet5_SS4mVWolpaMGXzex_c5rMt12jBLIEl2w56UH1MSPTcYktq9ulN5uYvBwD0pMCN6u9kIqAbjb85XvZFMKz84yxc4_atCJi6XecpykfmCmpBMScR7GRmZWeVfN8B8tTtkuz4qSszIjru0V8IVMneTKWmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روزی به موشک‌ های ایران می‌گفتند آبگرمکن، اما امروز خودشان و اربابانشان از آبگرمکن ایرانی ترسیده‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/akhbarefori/679073" target="_blank">📅 00:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679072">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4deefa9dfc.mp4?token=PIK4nSY7dt0Czcoh4WUu2uQsjcqJpH2T0LQyoNmjquBCaY3iBgp_l0MdFGPIaNrnjqlw7Gx2xyZrtJKdl9MJyoNZie48mg_T38Bb-R_acRwtI1BivFoen4mF9pDYafM1tERr3IqLQ2z6KtxoQrU0J69TQ8sHpOlIs4aH3wC20mXAmL9EIIne31mPu1dbvdR3phaF7hhsCntLdZVMV-v2F2l4xfTk8yffpCTRehzWhNNpm19nHaWhySaSHC73ogq1I8w14tv8aLFMeLptdtCass7mrRjBV6Q8mpod48vIpUtkhl1PeUBjVklgDR4WOLIi8EdmyOS22YbRbKzndJmE5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4deefa9dfc.mp4?token=PIK4nSY7dt0Czcoh4WUu2uQsjcqJpH2T0LQyoNmjquBCaY3iBgp_l0MdFGPIaNrnjqlw7Gx2xyZrtJKdl9MJyoNZie48mg_T38Bb-R_acRwtI1BivFoen4mF9pDYafM1tERr3IqLQ2z6KtxoQrU0J69TQ8sHpOlIs4aH3wC20mXAmL9EIIne31mPu1dbvdR3phaF7hhsCntLdZVMV-v2F2l4xfTk8yffpCTRehzWhNNpm19nHaWhySaSHC73ogq1I8w14tv8aLFMeLptdtCass7mrRjBV6Q8mpod48vIpUtkhl1PeUBjVklgDR4WOLIi8EdmyOS22YbRbKzndJmE5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تماشای فیلم اودیسه در سینما 4DX قطر؛ تجربه‌ای که مرز فیلم و واقعیت را شکست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/akhbarefori/679072" target="_blank">📅 00:47 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679071">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7982f7e7c0.mp4?token=Yt22mk09FFgzHPf56IrJoEkDG3kqQ3TG2bzXjq62AcTet2BHzb91Y0mOuziQlayYh9u2bAXyOk4rr3Re8eGbrc9lkdeU9Hc0tQ_1_ygLMlMuaF6Bb2N3ShyCuo6P3v9EFfTgroHfqWBsXJDfijUT3-6f6sBUCLWugw69j2wmFbzNU4U0E6BgpJcDeAcrGsS9ZYdWY40qveiD8OITiVTIumljhj29g5qrD0KcN-66esXzAIsqFi-Ghp0iilFlhyC98tJzeBBT5Vu3E9oxil9KRU3tjKCUHe_X_ta9FQLwOXBZVwzSVyZsDUaYMZgXimLv1nP8z3yhzLXY-M4LQf6yJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7982f7e7c0.mp4?token=Yt22mk09FFgzHPf56IrJoEkDG3kqQ3TG2bzXjq62AcTet2BHzb91Y0mOuziQlayYh9u2bAXyOk4rr3Re8eGbrc9lkdeU9Hc0tQ_1_ygLMlMuaF6Bb2N3ShyCuo6P3v9EFfTgroHfqWBsXJDfijUT3-6f6sBUCLWugw69j2wmFbzNU4U0E6BgpJcDeAcrGsS9ZYdWY40qveiD8OITiVTIumljhj29g5qrD0KcN-66esXzAIsqFi-Ghp0iilFlhyC98tJzeBBT5Vu3E9oxil9KRU3tjKCUHe_X_ta9FQLwOXBZVwzSVyZsDUaYMZgXimLv1nP8z3yhzLXY-M4LQf6yJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آهنگ "گل یاس" که در وصف حضرت زهرا(س) خوانده شده بود توسط شادمهر عقیلی بعد از ۲۷سال بازخوانی شد
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/akhbarefori/679071" target="_blank">📅 00:44 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679070">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔹
خبرهای متفاوت هر روز را در وبسایت خبرفوری کلیک کنید
🔹
🔹
همه چیز درباره توافق مهم ایران و عمان بر سر تنگه هرمز/ این تفاهم جنگ را برای همیشه پایان می دهد؟
👇
khabarfoori.com/fa/tiny/news-3235999
🔹
افشاگری رویترز از علت تعلیق حمله به ایران
👇
khabarfoori.com/fa/tiny/news-3235850
🔹
اینفلوئنسر مشهور در پخش زنده کشته شد
👇
khabarfoori.com/fa/tiny/news-3235919
🔹
اعلام آمادگی یک نماینده مجلس برای شلاق زدن باقر خرازی
👇
khabarfoori.com/fa/tiny/news-3235825
🔹
عذرخواهی سحر دولتشاهی درباره استوری خود؛ قصدی برای بی‌احترامی به اذان نداشتم
👇
khabarfoori.com/fa/tiny/news-3235984
🔹
اخبار لحظه به لحظه جنگ ایران و آمریکا
🔹
https://share.google/8EImhrm9fBFYjsyZr</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/akhbarefori/679070" target="_blank">📅 00:39 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679068">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
رسانه آمریکایی MS NOW: عمان با چارچوب یک توافق موقت با ایران برای بازگشایی تنگه هرمز موافقت کرده است
🔹
هدف از این توافق، فراهم کردن زمینه برای برقراری آتش‌بس جدید و ازسرگیری مذاکرات هسته‌ای میان آمریکا و ایران عنوان شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/akhbarefori/679068" target="_blank">📅 00:37 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679067">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
وقتی کلمات هزینه می‌شوند؛ ایثار، واژه‌ای که نباید ارزان خرج کنیم
🔹
امیر قلعه‌نویی می‌گوید پاداش صعود به جام جهانی را به‌جای دلار، ریالی گرفته و «ایثار» کرده است. اما آیا هر گذشت مالی را می‌توان ایثار نامید؟
🔹
در روزگاری که هزاران نفر بی‌هیاهو از حق و آسایش خود می‌گذرند، شاید بد نباشد واژه‌های مقدس را با دقت بیشتری به زبان بیاوریم.
🔹
گزارش امروز، نه درباره میزان پاداش تیم ملی، بلکه درباره مسئولیت ما در استفاده از واژه‌هایی است که نباید بی‌محابا مصرف شوند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/akhbarefori/679067" target="_blank">📅 00:30 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679066">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OaxoYJHw9orPcl9UsLZldQccejYVSdGx0A4-MUgWAftmovH02TLn-CayOwfeDdKEdteKto8FInSWV6HxyNNh-cW8WQhpayd9_335iSGuZ783FdIC5nMzzPJaa0JxlIyzWrtlqIH3a70VGjZOdlxHkazdsyaCtfqZ1aHg_AjGhCWQS2fXlRRYJ_EKbT0f3q90xXMWuFfMUE4SScCE-yvoybtj4PXZpV9KxbfkH87wS-bBzLBgmZ2zfnpOOqkZph0ocmuLlgooMgKPwlQFx7gWV9STC8XlWv0_0sSb6gEtcQ5HG3hqxPvwRWYSh7e5rIP5fdoJgjGdSkm_WXcoXrHC3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محسن رضایی: اجازه باز شدن مسیر دوم در تنگه هرمز را نخواهیم داد
🔹
اگر محاصره ادامه یابد، کشتی‌ها و نیروهای آمریکایی با خطرات و تلفات جدی روبرو خواهند شد.
🔹
ایالات متحده باید رفتار خود را تغییر دهد در غیر این صورت ما این وضعیت را تحمل نخواهیم کرد.
🔹
ما هرگز اجازه باز شدن یک کریدور دوم در تنگه هرمز را نخواهیم داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/akhbarefori/679066" target="_blank">📅 00:29 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679065">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
خبرنگار: زلنسکی می‌گوید که کشورش نیاز فوری به باتری‌های موشکی پاتریوت دارد  ترامپ قمارباز:
🔹
ما هم موشک می‌خواهیم #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/679065" target="_blank">📅 00:23 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679064">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c926eb53cb.mp4?token=NrI4_YtOn_6Q0x5B56eNcpaNzb6ePytR4EaOdvand2fMd9PZxmKh4MEvWL4wNzItHBEdU3by9XBcLln-5lXJsWqpBvr8qNtCKSgnfHk6nBkCrwid3UvnIbLUlNkb1AMl8_VUntIP_-0OHu-YGNgQawyzfs9NtPuifKZ2z5jgMIaruLaG2zEFOu474XfK6TFTNUydS3VFwzQvMoZ3dDxYbvnADJOZBTA_lAp6RrIfMCh8akGSVuQwbRtuUvPE7qQEB9NxKk8lF5qdKdAv_Z6wQNvFhpZThRKCMN1fx_CC-Mc499fPuizsgVzNi1s26WScOkQobfMTORCRst4jx-RsiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c926eb53cb.mp4?token=NrI4_YtOn_6Q0x5B56eNcpaNzb6ePytR4EaOdvand2fMd9PZxmKh4MEvWL4wNzItHBEdU3by9XBcLln-5lXJsWqpBvr8qNtCKSgnfHk6nBkCrwid3UvnIbLUlNkb1AMl8_VUntIP_-0OHu-YGNgQawyzfs9NtPuifKZ2z5jgMIaruLaG2zEFOu474XfK6TFTNUydS3VFwzQvMoZ3dDxYbvnADJOZBTA_lAp6RrIfMCh8akGSVuQwbRtuUvPE7qQEB9NxKk8lF5qdKdAv_Z6wQNvFhpZThRKCMN1fx_CC-Mc499fPuizsgVzNi1s26WScOkQobfMTORCRst4jx-RsiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار: زلنسکی می‌گوید که کشورش نیاز فوری به باتری‌های موشکی پاتریوت دارد
ترامپ قمارباز:
🔹
ما هم موشک می‌خواهیم
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/akhbarefori/679064" target="_blank">📅 00:20 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679056">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nwuUxToA2f7TJZtz8GSH2ROvQtXxoAjzGlsiSYpAOF5sGVVrEOlC_aKMnFxjGkkLmZtkdR7_ZU3IByl64_o8c26UE8n3e2eLxKJOaXDXqsqj4wbgjbdtQeLH0aqh7ecJLAJ6qtkUZMWJ5gkYlybtxBefgFbVqhkeszxeMpqc4ZYZJ9Rqs849-lt06qAwUdhXK-QkHZ0Gz9qe9O6cLlbZRemGbPRxL3ygmhLlbR9BEqW1LBFKh9ffVstMMGMQOtLBlvkhmTbuaiYKq2UJJDT9jlI1HtyPxJPMQsVLw-UUL3C8ve02imZmMGjMOCsRbYPGnwmkgsESPgVLwVjtu06b5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BurOt3BNXTvCd_kruvXJQa2vBjWDHlmlOSMolPzmhp1C70Ogf5uJbhHBBS8ViLG-gQBqyoZHOur00hVqrOqDWSvpjh0HXlDxNJ3HUAq1T0sPu5_-Pr7w1mRxJ4jKCNfqOmjaz2fP6aXQvExOKb9Psg-qThHoP2zn2WqybnzQj4swvTQsL43g2ZCpsqss7Dh6cquLOrFLMwwa-l_-wFafeWL30FZoTWGF2t5wcRPNtVLpEn5i91Gn7syePw2OidimDfVgr0kWkP0ulJcUm_xCGFW-pvQ5hUM0GWskj5NFomIOD3A6oO3Du9OXVF3pnr5-NFNemUqW-BzaaXqw9_FM_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iyYIVGO52IDmfDqoexaXB1uVRI75XPg7yxscYJUfjh6LiFqL7lu-8OCsiFVqLUbzLzFoP3apAQ0Eyiz3mcYjMOnb0dXOPYqGOGkSNSfFtySBngjeMWxSMCmsyoDhTI1XRde66picHjF98Dci2hIu7GI7Wz5RkNczrsmDEmPiZFe34ceWA39YXR5pryr5yGK0TjfHsp55M-SqR0bBCwTE1gSC37ixsQNTAi0tKQYOV0HQIFJ36FWsUWcP9V06UWO_D7r1LwknDlDU8Y0NINa65aelKPXpfWywx_NMmvpPWTtChZvmW9USWfgC-nrpuaUkigmK_adrUxY4iQTZ8HYjMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X_xtXiengKtsrnhryD7hklwkUELgBADO3LHI8p85_U0hv96sY_aweKPr6UPQpJN13ZjcMa4XSdARzz4tUjMBnKAbOo6oQC3DTFNLY1D913uOJtITkzyDpy7s0HBvUQPTFQoAjAx1ZICddze9-HD5kAljJAJldWnomLyRC2lC-sLWZhUvj29Qwec0BeIUVyvk75r3DjzHIdGVWnf-s3tWQV8TDNCErPeFRj4JqB7NFy_cXyGHwm9XetNoyYKXMRVC2N10OPCGLn8PE7hlRBCV_rIjsutw-DK2NcK36AWU2u0-E8C4-RAO8XSXkM708-bnCC0AQ-3Hcad1fieThcbk3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NtoSOaqRD837HZUEDc5d6793Sqlkl54IYhm81pxH8jn4dt-kEV9GDMhNqgotKKRN5sk5nWx7dbEFhCsi8uQW2h-sWElYuRWtP8LbKoEJoGaBAU7ghKVk2Xqh72pOCBcXxWv7IPze7zlMlKMn3n9BYK88EhBrWp8vmQugQUYBxKiIKfXgu_xr3eWCmIoea5PmHPsvtlp4bfS92shf3G9LvKhKj0fBKNDBV3LOA385ja0HEF1Jtk9VaqXArcQDnZ107vdppzwVuGAa0WP2rxrojpDJpLjkgCkqKTmGLwl_MEfZrnqPfOsTzsBHcZhK15z964CnKFru6dobbEnHwNwSVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">واکنش کاربران به قطع اینترنت در دوران جنگ
🔸
بر اساس نظرسنجی ایسپا، ۴۶ درصد کاربران اعلام کرده‌اند که در زمان جنگ از قطع اینترنت بین‌الملل به‌شدت عصبانی بوده‌اند و ۴۷درصد آنها گفته‌اند از این تصمیم عصبانیت کم یا اصلا نداشته‌اند.
🔸
در این دوره، صداوسیما با ۳۹ درصد، اصلی‌ترین مرجع کاربران برای پیگیری اخبار بود. پس از آن، شبکه‌های اجتماعی داخلی با ۲۱ و شبکه‌های ماهواره‌ای با ۱۴ درصد، در رتبه‌های بعدی قرار داشتند.
🔸
اختلال در ارتباط با دوستان و خانواده با ۳۸ درصد، مهم‌ترین مشکل ناشی از قطع اینترنت برای کاربران بود. پس از آن، سرگرمی  با ۳۳ و کار و درآمدزایی با ۲۹ درصد در رتبه‌های بعدی قرار داشتند.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/679056" target="_blank">📅 00:11 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679052">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3f5ae7020.mp4?token=bMBnFnOT6VoJ0tTDYkcLus5p61TalfaRAaLVbl39PZRIpCt702fALav9yZYuKIanFFsNSMXW43Hh9uRGXtge17Yj7et9kdomNTTt8qFiLgOrABOY1zSHXcbQ84SbghtGCjp6BWarvugPayd1iTPU8UCO2VYu69en-j5d2wq1IXbcaXe2QfQACMg81fJNvT6Do3yZ8tDr5U_BU1faNBxRO89i-3sR3HGxN1AmkBa_RGeKqQcxlOZa4kV6nJdo6gxb3y7Q9tiCE8nyvh8yX-ZAfX9EWqaUlOulgFBczVSqOnp8SqDAtvsq3cr2m9BiCWDf7xkc0TEifgdBMQwPlGDALQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3f5ae7020.mp4?token=bMBnFnOT6VoJ0tTDYkcLus5p61TalfaRAaLVbl39PZRIpCt702fALav9yZYuKIanFFsNSMXW43Hh9uRGXtge17Yj7et9kdomNTTt8qFiLgOrABOY1zSHXcbQ84SbghtGCjp6BWarvugPayd1iTPU8UCO2VYu69en-j5d2wq1IXbcaXe2QfQACMg81fJNvT6Do3yZ8tDr5U_BU1faNBxRO89i-3sR3HGxN1AmkBa_RGeKqQcxlOZa4kV6nJdo6gxb3y7Q9tiCE8nyvh8yX-ZAfX9EWqaUlOulgFBczVSqOnp8SqDAtvsq3cr2m9BiCWDf7xkc0TEifgdBMQwPlGDALQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار: آیا توافقی برای بازگشایی تنگه هرمز حاصل شده است؟  ترامپ متوهم:
🔹
نمی‌خواهم بگویم تمام شده است، اما به نظر می‌رسد در حال حاضر باز است. ما تنگه را کنترل می کنیم. #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/akhbarefori/679052" target="_blank">📅 00:06 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679051">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f10f13cb18.mp4?token=kyAmF5FoTsUNQJoCUkqPewwWRX0hiBWegKu3blxkBvccD6gJ5G5zfKJbgdp9vP3h2Cu0yr37_OgYE8eRD0av4C1j7y0QsArGvmBZEjpWcCCDeDfT69CzLRKzkp3AL34mTxm5OwV8dNCDQgLAjCvJRFPqZvQ_SYCdDAimR20l6zYk1xdHvABUMw75vARXx_NpzEYGAQNSKalE2fMITErrdQlXkaMEvEjW4IqgqbRMXFTg_1Jsve1W0R3opOIv696VHhPv2ZOjP6Sxq8nD5tn5s9H_1TRVKZnPf94s18HTkBJTs-hLrENo68SG83t7NDyKVZ0xw9_oOUU4AUFUOlB3Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f10f13cb18.mp4?token=kyAmF5FoTsUNQJoCUkqPewwWRX0hiBWegKu3blxkBvccD6gJ5G5zfKJbgdp9vP3h2Cu0yr37_OgYE8eRD0av4C1j7y0QsArGvmBZEjpWcCCDeDfT69CzLRKzkp3AL34mTxm5OwV8dNCDQgLAjCvJRFPqZvQ_SYCdDAimR20l6zYk1xdHvABUMw75vARXx_NpzEYGAQNSKalE2fMITErrdQlXkaMEvEjW4IqgqbRMXFTg_1Jsve1W0R3opOIv696VHhPv2ZOjP6Sxq8nD5tn5s9H_1TRVKZnPf94s18HTkBJTs-hLrENo68SG83t7NDyKVZ0xw9_oOUU4AUFUOlB3Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ جنایتکار: فکر می‌کنم جنگ به‌زودی پایان می‌یابد/ تصور نمی‌کنم آنها بتوانند بیش از این ادامه دهند #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/akhbarefori/679051" target="_blank">📅 00:03 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679049">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9f68b3d99.mp4?token=HI9UTsp-vc65KJqOyX1tBlRTBv5rhcchjyFDyNmvfghZPX9Nfkf3c_bzW9mGddWk3XNgpAUdI1gL9j7h4poGO8ZDpdio7pnqkL--l0e4Bue3cSF1jb9zVN9XR3oEDd3OaAxIpC1WWUJvuJpFHStyz8DLE3XtgaB6O5l5bzoMtTLBFncobZSOeeRfxsmQBoO_ScbhREO36yJG6BHoMK3iSMoeJd416PF86lDr0Iucz1gSm_IxsHhaqboA50YX9gsf8j9PTMwuaenPpwBdBmZAcs3ri8Q0cvPwbB2Su73d9nV3saa_0bmB9KvJilnXDWSmewBzCzfbLo_Y5urtIYMsgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9f68b3d99.mp4?token=HI9UTsp-vc65KJqOyX1tBlRTBv5rhcchjyFDyNmvfghZPX9Nfkf3c_bzW9mGddWk3XNgpAUdI1gL9j7h4poGO8ZDpdio7pnqkL--l0e4Bue3cSF1jb9zVN9XR3oEDd3OaAxIpC1WWUJvuJpFHStyz8DLE3XtgaB6O5l5bzoMtTLBFncobZSOeeRfxsmQBoO_ScbhREO36yJG6BHoMK3iSMoeJd416PF86lDr0Iucz1gSm_IxsHhaqboA50YX9gsf8j9PTMwuaenPpwBdBmZAcs3ri8Q0cvPwbB2Su73d9nV3saa_0bmB9KvJilnXDWSmewBzCzfbLo_Y5urtIYMsgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ جنایتکار: فکر می‌کنم جنگ به‌زودی پایان می‌یابد/ تصور نمی‌کنم آنها بتوانند بیش از این ادامه دهند
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/679049" target="_blank">📅 00:00 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679048">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v6pXcsm9fhnw0IGs8nF5DKGzmSkdthYv5UTnZq7PNCYhzoQTCGZAKfGpn6WS_lNDHHPOy2zoLguB8gbY07tg3SkykPRvPazdpV49dh6VU87-Moa5rniIhj_tR900nsy2OC3UGgV6J2b0U29ZoODOapCnTdyVH1fMBAAewRrMju0KtJfnVcN_Oul_P_ms3s65ZZmerTf0jYHBm2ms0JvSHKXFk_zfsJsR2kZ3weCITacJZ-jQ0_7GP-w-pmmEvOOtRtdRd4wCK381BTi6kxgM82tnCehiIAc94-Y10NyCAswGF48azNcq9lzKMXStvl4Bt3j5ecMwZFlxfCKvoRYIyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/679048" target="_blank">📅 00:00 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679046">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pOF9JFKDZSuZ4JMRE7vM_P9lVPMzoGgAB5RBIc5Whe2znRGhjr_5Lt_drhdNFwVnpxG-tdcIdL_3CcphF2zUgv2sthMxsXVoIjmfQJgcw2A1HvWnNEWhGi6cIpvazU4zgHs72RR18odKvPFAM32ov9Lb4L3gngZms-Eg97uCc5kFr6BrxXnA7sWUIseFBSnYelsadhHFUJGFI7Rax2eXA1jk0eB8oYIlhK4fcNk7ROrI7J_sJR_Q6llvi2aLz7CJjTm2jPdAuLUEYzF1nk3OnSW16JG6VogdJwc7_m9v831_lUXRJcODwgNXp9rUDSqLJihiYXR2rod-iq5OXnpXow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ته دیگ
🔹
رسانه‌های غربی خبر دادند که وزارت جنگ آمریکا پس از تماس تلفنی خشمگین دونالد ترامپ با پیت هگست، قرار است یک جلسه اضطراری مختص به کمبود تسلیحات برگزار کند. سی ان ان هم بنا به گفته دو منبع آگاه اعلام کرد که ارتش آمریکا در جریان جنگ با ایران بخش قابل‌توجهی از مهم‌ترین موشک‌های رهگیر خود را مصرف کرده است؛ به‌گونه‌ای که حدود ۸۰ درصد از موجودی موشک‌های سامانه دفاع موشکی تاد و نزدیک به نیمی از موشک‌های رهگیر پاتریوت از زمان آغاز درگیری‌ها مورد استفاده قرار گرفته‌اند. این گزارش نگرانی‌ها درباره کاهش توان دفاع موشکی آمریکا را افزایش داده است.
🔹
هشتصدوبیست‌ونهمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/679046" target="_blank">📅 23:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679045">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
آیت‌الله جوادی آملی: با ناقضان وحدت مبارزه کنید
🔹
حضرت امیر یک بیان نورانی دارد که بالاخره ما جامعه را متحد کردیم، و تمام کوشش دشمن این است که این جامعه را ارباً اربا بکند. شما مواظب باشید این جامعه متحد، مختلف نشود، پراکنده نشود.
🔹
اگر کسی خدای ناکرده عالماً عامداً دارد این وحدت اسلامی را به هم می‌زند، با او مبارزه کنید، ولو عمامه من بر سر او باشد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/akhbarefori/679045" target="_blank">📅 23:32 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679044">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6898fed19.mp4?token=mGt0xp2mN4ZlqZ8LfyDPcy1IhtnRV84n8Voc1XYB8RpB4kPuuzlv3PHD9QJtfAz-XvPkVne0wl-Wz4TWpWG7IRFOMUT1dVHGGxaq1NmfCsKKGPfOWzaVwVKIEtlKzB_D8MgNI_GZ-El4UU-HIHiTg6OHVwxhxDApIU50o7df5LBfkpJv08ZHzGm2YqnT1Yny6u-BuIIGHPYLt4blQZ4IPjiyVhl_OS9i3yvnIcI5FV5UrO46iMY93ciduNOYUy_H7lKWWafEQsvFkSM2JBbd3ntf0e69DTSWFYseRWMWTY92mtTpkaqeLdkSyqUX_LWwNDG5mMbqGEtwr-4wVtLFuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6898fed19.mp4?token=mGt0xp2mN4ZlqZ8LfyDPcy1IhtnRV84n8Voc1XYB8RpB4kPuuzlv3PHD9QJtfAz-XvPkVne0wl-Wz4TWpWG7IRFOMUT1dVHGGxaq1NmfCsKKGPfOWzaVwVKIEtlKzB_D8MgNI_GZ-El4UU-HIHiTg6OHVwxhxDApIU50o7df5LBfkpJv08ZHzGm2YqnT1Yny6u-BuIIGHPYLt4blQZ4IPjiyVhl_OS9i3yvnIcI5FV5UrO46iMY93ciduNOYUy_H7lKWWafEQsvFkSM2JBbd3ntf0e69DTSWFYseRWMWTY92mtTpkaqeLdkSyqUX_LWwNDG5mMbqGEtwr-4wVtLFuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آنچه داوطلبان ورود به دانشگاه فرهنگیان باید بدانند
/ تلویزیون اینترنتی مدار
این برنامه را کامل ببینید
👇
https://aparat.com/v/xffqtvr
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/akhbarefori/679044" target="_blank">📅 23:29 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679043">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
فعلا خبری از کاهش مدت تحصیل کارشناسی ارشد و دکتری نیست
رمضان رحیمی، دبیر کمیسیون آموزش مجلس در
#گفتگو
با خبرفوری:
🔹
طرح کاهش مدت تحصیل کارشناسی ارشد به یک سال و دکتری به سه سال، که آذرماه ۱۴۰۴ مطرح شده بود، صرفاً یک پیشنهاد مقدماتی از سوی وزارت علوم بود و به دلیل شرایط جنگ و مسائل دانشگاهی فعلاً مسکوت مانده است که با عادی شدن اوضاع مجدداً در کمیسیون بررسی خواهد شد.
🔹
امید می‌رود این طرح‌ها سال آینده به صحن علنی مجلس ارائه شوند و اجرای طرح کاهش مدت تحصیل مقاطع کارشناسی ارشد و دکتری به امسال نمی‌رسد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/akhbarefori/679043" target="_blank">📅 23:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679042">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7238929701.mp4?token=p4cCJOIXY6DpmgFiMQq5HoMq4A0Jsf4z8neuQKvLnyZa9sUF7IGOTG09LhIRNbtgmPeHyOMYxyJZQQ9fh3Y9OWoSSel30FkDvYoeGgq-rpM0kflNbQxQF1m4PNE4O-WIJT7FqTDSQPCeqMWH-31EGJgBCGbvj9bM6uOmgTzslhVn91HklQsJu9ZFJZxV7PDt98ZmDYr-q4P1GVRFc6qijMYvgrH_5BfD7hI-My08v5_1o5jB7zsp2M4CcUDwj4IbP9lgZ80uxQ4Zv2QBsQZw7SfvPjQB6oTuRJxGpMJ_PpRSCkzovitH-zYQHh3evoLWutcElEfZPCEYShwW_vRByA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7238929701.mp4?token=p4cCJOIXY6DpmgFiMQq5HoMq4A0Jsf4z8neuQKvLnyZa9sUF7IGOTG09LhIRNbtgmPeHyOMYxyJZQQ9fh3Y9OWoSSel30FkDvYoeGgq-rpM0kflNbQxQF1m4PNE4O-WIJT7FqTDSQPCeqMWH-31EGJgBCGbvj9bM6uOmgTzslhVn91HklQsJu9ZFJZxV7PDt98ZmDYr-q4P1GVRFc6qijMYvgrH_5BfD7hI-My08v5_1o5jB7zsp2M4CcUDwj4IbP9lgZ80uxQ4Zv2QBsQZw7SfvPjQB6oTuRJxGpMJ_PpRSCkzovitH-zYQHh3evoLWutcElEfZPCEYShwW_vRByA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تیم اندرسون، نویسنده و پژوهشگر: تفاوت فرهنگ عربستان و عراق را می‌توان از نحوه برخورد نیروهای امنیتی آن‌ها با زائران دید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/akhbarefori/679042" target="_blank">📅 23:19 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679041">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nL7WAZZCT-1oHrvNFePTlWCJhpORDKavNya4UCeFmFfcBFIu56BGqtlBw7Y1dTaZ0ylcoBriK2vUpqKZBw1Xg8J0Xq-GsVkMzlh9qmR6cCZiKKl8A1L-N58e3izMutj0gez5SMXVePwmdknIDPzNt-G3xRnF7aacgIDgUAO7ql583SXI9oWWkHk3hf4rvXG7wFd_91A81BcPCB_bKOMUoZqBijyCBb7ayjWjR6DkoSAgalJ_DTq9KCOaPOv07qCoKKplxjom1Ql-PNDMifqAdM2ULf-Lg-vB0Ht34y8367Pa0EsL0JHGpdUyAI0xj7KRzdFSq5qjgf7qat7nAmPxHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پایان ۴ دهه واردات نفت از عربستان؛ آمریکا به سراغ ونزوئلا رفت
🔹
برای نخستین‌بار از سال ۱۹۸۵، واردات نفت خام آمریکا از عربستان سعودی در ماه جولای به صفر رسید؛ تغییری بزرگ در نقشه انرژی جهان که پیامد مستقیم تنش‌های نظامی در خلیج‌فارس است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/akhbarefori/679041" target="_blank">📅 23:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679040">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/039b2e86ac.mp4?token=Uadk14OT4LMSq31SBAABJYA39TLB5vnUUpNvTzWyZyDCdGzIVzar1MhoO8UXsQpMydcguNKvSkFgoSiTRHOhkx_u5dFhKSUQBlfQKxxjImXSwLvHJsuPmTjubT3EUmJvesiPG1o5q2168EHchnMryf17MRe_uSeGg9FgxoYQO8Eaq-6Sm8wmW5JcE4GcTEu1sgo6CEHFTcjLi3wGZvrgQayKNabSfXRJo9x-T_bTC7jZBmWHlRrlZy65xVleT_dSpwMCz2LeE59RwK-FB5h4GiI1w69cHR4f_kwpyffwBal3vG4oQGzVi5OagYQUOcmt_M3_UzYv4v-ZHhQRbgxYNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/039b2e86ac.mp4?token=Uadk14OT4LMSq31SBAABJYA39TLB5vnUUpNvTzWyZyDCdGzIVzar1MhoO8UXsQpMydcguNKvSkFgoSiTRHOhkx_u5dFhKSUQBlfQKxxjImXSwLvHJsuPmTjubT3EUmJvesiPG1o5q2168EHchnMryf17MRe_uSeGg9FgxoYQO8Eaq-6Sm8wmW5JcE4GcTEu1sgo6CEHFTcjLi3wGZvrgQayKNabSfXRJo9x-T_bTC7jZBmWHlRrlZy65xVleT_dSpwMCz2LeE59RwK-FB5h4GiI1w69cHR4f_kwpyffwBal3vG4oQGzVi5OagYQUOcmt_M3_UzYv4v-ZHhQRbgxYNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش پزشکیان به اقدام مادر کردستانی که پول دیه دخترش را خرج مدرسه‌سازی کرد
🔹
این که شما پول و سرمایه داشته باشی و ببخشی، یک موضوع معمولی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/akhbarefori/679040" target="_blank">📅 23:14 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679038">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCAYgEn1oVORAbMb9ViOY5c4rXiT9ZPar8hM1jaIfmpHaseb81QTtvHU_MKEa1hNs--Gpqn1qtjfHTESCqsNhxa-Oy8wqXKRdsyOW66oHMAiKLniz4Tw0p9EYeM-KTrHeI7DDyEn8VaV-_NVv55Oc5HldCNAO24B_12Tu0Olx9fdoS4MKwB47BBkwTsf_6fg_V_z_ikKvFI8A5EgGV2KuPcGv-iGwMe8_naXFV-Q8W2tR__9QmNx1crwm5249PJ1CoMdUE49BVlBTraS0Watov7pWpYauGLCvUhO45Qk0usuB9kjD7ncCCyGiN1oLxztiH6pzaYIHf-l10-bVYQfcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«نوستراداموس چین»؛ پیش‌بینی جنجالی درباره جنگ علیه ایران | دو پیشگویی قبلی او که محقق شد چه بود؟
🔹
در دنیای پرشتاب رسانه‌ها، جایی که پیش‌بینی آینده ژئوپلیتیک جهان اغلب به گمانه‌زنی‌های دیپلماتیک محدود می‌شود، ظهور چهره‌هایی که با رویکردی متفاوت به تحلیل رویدادها می‌پردازند، همواره توجهات را به خود جلب می‌کند.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3235477</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/akhbarefori/679038" target="_blank">📅 23:09 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679036">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qGpZJDKu5d-0ziPVuIzlt2w1TyioRH6YEAL1ffYOai7bVBCMnoL8otX08VBq7GmvKbTHe3J_hcEde9f6MQjAtgPConsX9ol3BPDYayU4S71Dnk9JsGM7WCdqyNniOTsjZBoJRfrLRQGDKRcoC2kcY16z7D2RPStJSIuiosxvEumQZK9VCsqK0uILPnKUjREE8Do_oIIK-HL5ixMv0C-IGfYsR6Hq2VSuxZUFvOSHMS1sEtSoC1617QgEUPTJoPF5ez0EGdRPAp9CqWWW15p3cbOUPTsE5im5JZXPAmgHnGOj9nVmZwBePOhkeLaAr1H9Tr6AMB25hjEr3-UIoDGYTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آدمی پشت واژه‌هایش شناخته می‌شود
🔹
امام علی(ع) در نهج‌البلاغه یادآوری می‌کند که حقیقت شخصیت انسان، پیش از سخن گفتن پنهان است. واژه‌ها می‌توانند میزان خرد، شخصیت و نگاه ما را آشکار کنند؛ پس گاهی یک لحظه سکوت و اندیشیدن، بهتر از سخنی است که نتوان آن را جبران…</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/akhbarefori/679036" target="_blank">📅 23:01 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679035">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک تجارت | Tejarat Bank</strong></div>
<div class="tg-text">🎬
#تماشا_کنید
✅
حضور فعال بانک تجارت در قلب عسلویه
💫
پروژه بازسازی فازهای ۴ و ۵ پارس جنوبی با بازدید میدانی دکتر اخلاقی مدیرعامل بانک تجارت کلید خورد.
📌
گامی بلند برای تأمین مالی، بازسازی و بازگشت سریع‌تر این پروژه ملی به مدار تولید.
⬅️
دکتر اخلاقی: ما در بانک تجارت، نه فقط یک تأمین‌کننده، بلکه همراهِ عملیاتیِ صنعت نفت، گاز و پتروشیمی برای حفظ اقتدار انرژی کشور هستیم.
مشروح خبر
👉
📱
tejaratbankofficial
📱
TejaratBank
📱
TejaratBank.ir
🟢
TejaratBank
🟢
TejaratBank
📲
TejaratBank</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/679035" target="_blank">📅 23:00 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679034">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9740cd9b11.mp4?token=Ckh9zdEUcb4_J2-2vjUboVsbqCMRWgLfd6kH0ccuVjISNCT9DMz7c2AHDl1ZA7GlxhlOmz6AaSw7fqbAcWpgPpV2p25UgJpZzBPXw6gDiG1clD9ooQz83wqUa7mKtemxoQLj0Vy_EK5YE9Q8QFuoqGA3BCabvAZYP76Y7xKqJIwMpRBK6tVsaQahhZmnd6F-s152UFQ_2lfMorU0ROJ5YL6kQRZCql2itxVmCra6rBfD57wfpjU3mRK_ThYm6wYOJ5koMH-VKyhJN9TrfNb3NlKdwVn0x_y1-imPM5G3HQqeNXqJwWnx-Jmcr08CU17fyxoJeFwp2BY_4_LFpYxYmTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9740cd9b11.mp4?token=Ckh9zdEUcb4_J2-2vjUboVsbqCMRWgLfd6kH0ccuVjISNCT9DMz7c2AHDl1ZA7GlxhlOmz6AaSw7fqbAcWpgPpV2p25UgJpZzBPXw6gDiG1clD9ooQz83wqUa7mKtemxoQLj0Vy_EK5YE9Q8QFuoqGA3BCabvAZYP76Y7xKqJIwMpRBK6tVsaQahhZmnd6F-s152UFQ_2lfMorU0ROJ5YL6kQRZCql2itxVmCra6rBfD57wfpjU3mRK_ThYm6wYOJ5koMH-VKyhJN9TrfNb3NlKdwVn0x_y1-imPM5G3HQqeNXqJwWnx-Jmcr08CU17fyxoJeFwp2BY_4_LFpYxYmTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: بهترین روش آموزشی دنیا را باید مستقر کنیم
🔹
باید بهترین روش آموزشی موجود در دنیا را در کشورمان پیاده‌سازی کنیم.
🔹
باید هر روزمان بهتر از دیروزمان باشد، اگر این نگاه را در فرزندان خود ایجاد کنیم، قطعاً پیشرفت خواهیم کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/akhbarefori/679034" target="_blank">📅 22:55 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679033">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64880a95c9.mp4?token=qgkpCED9ZsN_tDZU4T75SDS8nz7pJOFOIh1yGxQobQNWmXWGqLS8jYcDiPOmXPuEWK6u2CsWWkoaQhsfoQKacXFR_RTBMpuvB7p-uoZulhBwk7B4CWIlYbtDW3BWyE8TGjWgPXHbBOCDBX_gbYXiSLLayA7Ap2t6xOA0ZtayMrSXbUpX1C6dVjODOmpj5E5DcU4pIw20v4_JsET0gcbUnlRX4kVR1XnhvMhjmTN4XtnRJVE3apPlcfxqFBGMVmSdXijUXmEt14jbRciJT-0gZOhzBZhtb-cecKHYZNAOr43-80SOWix3D4yzK5_yTcMRNowlLRcE5UjWKaCJ73k6ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64880a95c9.mp4?token=qgkpCED9ZsN_tDZU4T75SDS8nz7pJOFOIh1yGxQobQNWmXWGqLS8jYcDiPOmXPuEWK6u2CsWWkoaQhsfoQKacXFR_RTBMpuvB7p-uoZulhBwk7B4CWIlYbtDW3BWyE8TGjWgPXHbBOCDBX_gbYXiSLLayA7Ap2t6xOA0ZtayMrSXbUpX1C6dVjODOmpj5E5DcU4pIw20v4_JsET0gcbUnlRX4kVR1XnhvMhjmTN4XtnRJVE3apPlcfxqFBGMVmSdXijUXmEt14jbRciJT-0gZOhzBZhtb-cecKHYZNAOr43-80SOWix3D4yzK5_yTcMRNowlLRcE5UjWKaCJ73k6ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: بهترین روش آموزشی دنیا را باید مستقر کنیم
🔹
باید بهترین روش آموزشی موجود در دنیا را در کشورمان پیاده‌سازی کنیم.
🔹
باید هر روزمان بهتر از دیروزمان باشد، اگر این نگاه را در فرزندان خود ایجاد کنیم، قطعاً پیشرفت خواهیم کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/akhbarefori/679033" target="_blank">📅 22:51 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679032">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
منشأ صدای انفجار در قشم، هدف قرار دادن اهداف متخاصم بود
منابع آگاه:
🔹
علت شنیده شدن صدای ۲ انفجار در قشم حوالی ساعت ۲۱ و ۴۰ دقیقه پانزدهم مرداد، مقابله با اهداف دشمن متخاصم در ورودی تنگه هرمز بوده. دستاوردهای این مقابله دریا‌دلان نیز در ساعات آینده به اطلاع همگان خواهد رسید.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/akhbarefori/679032" target="_blank">📅 22:50 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679030">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef8d84e289.mp4?token=MjByVNCyXS3PNtBWC6-nFnJ8oMYujyHg1If77bGnZm-x5Lc9OHlCYMejo-6YdRyWCgu2jqplh4fW-I_H4C-rCllUKaIrebV7mqdj_BucLIKeo5D6khEzrGcKT4VNzsJj6ofRRSqc4c3gk0LMDUN95CAAotmITVy-UuSAVFFGx4aUWGxiGtK5t1kWB5MLxVR_ckq_xkWFmerw-NetYYdfodn_BXZm3rGkIJJXQKb8LI-qY68TFt5wYqhgVbDu3638bZfqZdSdNH0j2FY1KOEWnEzcM9oBXKb0b9rPrZooC7i_WxUz0AQBruVDRa8_e3HWZghlui65Sa0QxpZX2K4gcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef8d84e289.mp4?token=MjByVNCyXS3PNtBWC6-nFnJ8oMYujyHg1If77bGnZm-x5Lc9OHlCYMejo-6YdRyWCgu2jqplh4fW-I_H4C-rCllUKaIrebV7mqdj_BucLIKeo5D6khEzrGcKT4VNzsJj6ofRRSqc4c3gk0LMDUN95CAAotmITVy-UuSAVFFGx4aUWGxiGtK5t1kWB5MLxVR_ckq_xkWFmerw-NetYYdfodn_BXZm3rGkIJJXQKb8LI-qY68TFt5wYqhgVbDu3638bZfqZdSdNH0j2FY1KOEWnEzcM9oBXKb0b9rPrZooC7i_WxUz0AQBruVDRa8_e3HWZghlui65Sa0QxpZX2K4gcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت زائر استرالیایی که به کمپین نظافت مسیر اربعین پیوست در برنامۀ پرچمدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/679030" target="_blank">📅 22:48 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679027">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac440038d6.mp4?token=gFqyc0yj0Sg8BakSb2IiVvu-63YIz_u79qc5ucSVLADpElgqkw8OfE-uwQGyEc4WeMZDY9h9TYlLlsj5-Ax2hK2HGZaSDhZVZV3A5yceu6D2p_O0VzX8_fVKqNRmGoaaHJrCZBKOzoLBHbrMp2KXU6SgIcpMesQkSQk1OMTqx10cXUmJtvq_g6n9CH2YDFCaaCSRpZUnHaLt1AEWxz79wVvtnrrZ4-O2VOrAnzXLQ6f6-tn82WOG9yMQ6znY4DlCaTqd2Pv00kAQ5ACpAruIM6Ty0DM4jdnaHm0ahfBoK_i_XxEXqSbfRaLWKuXVossOWBIwfGR84utyWpVKx7Cdzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac440038d6.mp4?token=gFqyc0yj0Sg8BakSb2IiVvu-63YIz_u79qc5ucSVLADpElgqkw8OfE-uwQGyEc4WeMZDY9h9TYlLlsj5-Ax2hK2HGZaSDhZVZV3A5yceu6D2p_O0VzX8_fVKqNRmGoaaHJrCZBKOzoLBHbrMp2KXU6SgIcpMesQkSQk1OMTqx10cXUmJtvq_g6n9CH2YDFCaaCSRpZUnHaLt1AEWxz79wVvtnrrZ4-O2VOrAnzXLQ6f6-tn82WOG9yMQ6znY4DlCaTqd2Pv00kAQ5ACpAruIM6Ty0DM4jdnaHm0ahfBoK_i_XxEXqSbfRaLWKuXVossOWBIwfGR84utyWpVKx7Cdzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: آموزش حق همۀ مردم است؛ نه فقط پولدارها
🔹
حاکمیت باید بستر آموزش مناسب برای همه مردم را فراهم کند.
🔹
اگر امروز جوان ما مشکل دارد؛ مقصر ماییم، نه جوان مملکت. ما نتوانسته‌ایم درست آموزش بدهیم و آن‌‌ها را توانمند کنیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/679027" target="_blank">📅 22:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679025">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f645eb026d.mp4?token=IrTOMMaT1NaQI0Uyo7xu7opBVhY8u1n0sUR1GP5l1cqA0JPlXa7GBdNmh3lwYZ7njqLQ6M8BsLdGZ1dJPw2fg1vOj5iO9IidvOFaFuVKQ--1nulsnL1CA-XrpxFP1OqnmNsNotSKj7-_jJlrFFWhplxGP6sT20UH0U68N9nlkEb4UBIGjs5hrwV9mxZdk2oVUGfLHz_YxLNCP768JUu9KNx-m03KBe0y3doYNogJk-bx4K085IH3i_17NnOnBR69SyrkPH6VBYXTih53DIvS0AZ7Tu8aGSMBHe2QwSq8gncHU76HNSfxHTC_GQaW3mp9FbGHrSlyRVivPbVqy8JeoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f645eb026d.mp4?token=IrTOMMaT1NaQI0Uyo7xu7opBVhY8u1n0sUR1GP5l1cqA0JPlXa7GBdNmh3lwYZ7njqLQ6M8BsLdGZ1dJPw2fg1vOj5iO9IidvOFaFuVKQ--1nulsnL1CA-XrpxFP1OqnmNsNotSKj7-_jJlrFFWhplxGP6sT20UH0U68N9nlkEb4UBIGjs5hrwV9mxZdk2oVUGfLHz_YxLNCP768JUu9KNx-m03KBe0y3doYNogJk-bx4K085IH3i_17NnOnBR69SyrkPH6VBYXTih53DIvS0AZ7Tu8aGSMBHe2QwSq8gncHU76HNSfxHTC_GQaW3mp9FbGHrSlyRVivPbVqy8JeoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس‌جمهور: ما باید بتوانیم در کنار ایجاد بزرگراه و آزادراه؛ کریدورهای ریلی کشور را هم تقویت کنیم چون هم سوخت کمتری مصرف می‌شود و هم سرعت تخریب جاده پایین می‌آید؛ در همین راستا قطار چابهار به زاهدان در هفته دولت به بهره‌برداری می‌رسد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/akhbarefori/679025" target="_blank">📅 22:37 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679024">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b11217e8c.mp4?token=l10Fw9zaADCzji9qXBYMBC8_MNrwKWdwwAqOYKW1ZB0IVYCwMWvRLO5nTQBY_4-K9Hy0GyNfiLbD8ZfhZOoSAG3g8Dla_dnqAzs5VhQXVWn8TnIRVgRrPFYP-LMqtaIV_RxfFgEYoarKxmH3Kkaj2yajtkFcK4dqAP9JeSUJHvA-dmHPEBzT_2s75rnVF11b0FmittaRrVubMLX3mCCtUSjD30NGfqAj7gKOAsJUwXy_B6WK-2DsciKbmQA3eeNrK_lzsq3Vst604qBT8MEWQwFoluSdJSdbtbTWtRqrFBJaT5Ay3JmKY4wytMQulGmci-1DDEUN9BIQT13YkP4f_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b11217e8c.mp4?token=l10Fw9zaADCzji9qXBYMBC8_MNrwKWdwwAqOYKW1ZB0IVYCwMWvRLO5nTQBY_4-K9Hy0GyNfiLbD8ZfhZOoSAG3g8Dla_dnqAzs5VhQXVWn8TnIRVgRrPFYP-LMqtaIV_RxfFgEYoarKxmH3Kkaj2yajtkFcK4dqAP9JeSUJHvA-dmHPEBzT_2s75rnVF11b0FmittaRrVubMLX3mCCtUSjD30NGfqAj7gKOAsJUwXy_B6WK-2DsciKbmQA3eeNrK_lzsq3Vst604qBT8MEWQwFoluSdJSdbtbTWtRqrFBJaT5Ay3JmKY4wytMQulGmci-1DDEUN9BIQT13YkP4f_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: چرا به مدیران شرکت‌های زیان‌ده، فوق‌العادهِ مدیریت می‌دهیم؟!
🔹
مدیریت کردن با وجود صداهای تفرقه‌انگیز کار خداست
🔹
کارخانه‌ها و شرکت‌های ما باید توسط بخش خصوصی هدایت شوند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/679024" target="_blank">📅 22:36 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679022">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e551e21f3b.mp4?token=Qr5mV9q_zc5FMrjN4ECGfGVlhV8UBddlsg_ci2BUp-Wn_fCnS8VkbwFe_B3dQZfkhCwQGpCWBx3W4z1lzPOFChnDcuBdVsXms8kJ5W6zjF_9LUBWxsNgKxvpaJGqWZlIgRaKgXScEelmjw4ar-GHbOcE948f_Yurqj57BY1nDV2Y-z4SpHRfBj4sU60rE6MkOLKjOiTsDX7ysLrYWkCxdi2xAzg6iNZGp8R0VTqebc4e_RwrnRMKyrePvl4SJeRlGSeiMpn6UybJn5_qxLaSqgqNzNyPPYwAUu6hKO2P_XF9Ao6DdTYtSyE6coR0UwD-6aZT_R9AC-KT_Cat-dr4Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e551e21f3b.mp4?token=Qr5mV9q_zc5FMrjN4ECGfGVlhV8UBddlsg_ci2BUp-Wn_fCnS8VkbwFe_B3dQZfkhCwQGpCWBx3W4z1lzPOFChnDcuBdVsXms8kJ5W6zjF_9LUBWxsNgKxvpaJGqWZlIgRaKgXScEelmjw4ar-GHbOcE948f_Yurqj57BY1nDV2Y-z4SpHRfBj4sU60rE6MkOLKjOiTsDX7ysLrYWkCxdi2xAzg6iNZGp8R0VTqebc4e_RwrnRMKyrePvl4SJeRlGSeiMpn6UybJn5_qxLaSqgqNzNyPPYwAUu6hKO2P_XF9Ao6DdTYtSyE6coR0UwD-6aZT_R9AC-KT_Cat-dr4Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس جمهور: سایپا و چند شرکت دیگر هم مثل ایران‌خودرو واگذار خواهند شد
🔹
واگذاری واقعی با خصولتی کردن فرق دارد
🔹
کارخانه ایران‌خودرو را که واگذار کردیم، وزیر اقتصاد دولت استیضاح شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/akhbarefori/679022" target="_blank">📅 22:29 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679021">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e405a0f0bf.mp4?token=bBrgA-D1UuqZy9bDwzbPWU24T9jDw-UzasnwybDuwiqnWNxxjpLUpVe7XEQ17vUnGiY_giFAROGkgcOIXZENwwmpkwzdVkMcjlkJWr0fP8JhzU5zwR41m69TipOL_kvPj7XM8Pnh1V7nq8BFD6i0fZ2b6O1tRWViEf783eNxFlO1eT0UpatXgPk23IY9V153JQ6aPWGrVylSYGY0lcRkWxo_ZaGCZhu52QraHAg_knr-9O6LBlokzZWoh_udiowGdyARPB-3MTeOgKcL7wDVDC4A1yTp7JU6NVCs8-SVopeKtVkaGXbFh56ipPsBZ9lFb-rIcbtz4Lk8-b9FRTLFxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e405a0f0bf.mp4?token=bBrgA-D1UuqZy9bDwzbPWU24T9jDw-UzasnwybDuwiqnWNxxjpLUpVe7XEQ17vUnGiY_giFAROGkgcOIXZENwwmpkwzdVkMcjlkJWr0fP8JhzU5zwR41m69TipOL_kvPj7XM8Pnh1V7nq8BFD6i0fZ2b6O1tRWViEf783eNxFlO1eT0UpatXgPk23IY9V153JQ6aPWGrVylSYGY0lcRkWxo_ZaGCZhu52QraHAg_knr-9O6LBlokzZWoh_udiowGdyARPB-3MTeOgKcL7wDVDC4A1yTp7JU6NVCs8-SVopeKtVkaGXbFh56ipPsBZ9lFb-rIcbtz4Lk8-b9FRTLFxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: باید به سمتی برویم که یارانه‌های دهک‌های بالا کمتر و به دهک‌های پایین پرداخت شود
🔹
در مورد یارانه‌ها اگر بتوانیم از کسانی که به کمک دولت نیاز ندارند، بگیریم و به کسانی که نیازمند مساعدت هستند، اضافه کنیم، عدالت بیشتری برقرار خواهد شد.
🔹
عادلانه این…</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/akhbarefori/679021" target="_blank">📅 22:27 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679020">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5e2b25a4c.mp4?token=KCvpELQz31CQn9XxzJYPx-cDadScfvJ3oIEaKnDtiFgF1q0QDnDPwzjrIiPH3W7HHbcChdXMBwFzDtlNcYnouMYIdhSkNRbVbMMwXP0FTtW9aPR_XSOX2o6Hf74NxfGlOz3UBaTY1HsWPxxRrxeEdEGuHQwGoZFF-aRkEbGJGtihn1t43sme3nEfyy0wAN9T_sPCmLoAZT9gR2WxFXhjGD8G83QTvQtsd5YfxY-udBo7GPFWa9HquEm6vAhVKaKMzx2DvDRsc7XmOQx0WsvhfPNUTasuXPKMYghfYv2DEVJMu2tTqLsB3FHyr_juF1fbP0QpwjdK6XD1JVGwYDWlSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5e2b25a4c.mp4?token=KCvpELQz31CQn9XxzJYPx-cDadScfvJ3oIEaKnDtiFgF1q0QDnDPwzjrIiPH3W7HHbcChdXMBwFzDtlNcYnouMYIdhSkNRbVbMMwXP0FTtW9aPR_XSOX2o6Hf74NxfGlOz3UBaTY1HsWPxxRrxeEdEGuHQwGoZFF-aRkEbGJGtihn1t43sme3nEfyy0wAN9T_sPCmLoAZT9gR2WxFXhjGD8G83QTvQtsd5YfxY-udBo7GPFWa9HquEm6vAhVKaKMzx2DvDRsc7XmOQx0WsvhfPNUTasuXPKMYghfYv2DEVJMu2tTqLsB3FHyr_juF1fbP0QpwjdK6XD1JVGwYDWlSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: اگر ارز ترجیحی را حذف نمی‌کردیم، قطعاً در زمان جنگ قحطی پیش می‌آمد
🔹
با اجرای این طرح زمینه فساد را از بین بردیم
🔹
امروز برنامه داریم تا زمینه‌های فساد را از بین ببریم، این فساد می‌تواند رانت، رشوه یا قاچاق باشد.
🔹
تا زمانی که زمینه فساد وجود دارد؛…</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/akhbarefori/679020" target="_blank">📅 22:25 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679019">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0674cb13c.mp4?token=JZCpB5e1UCsRLy_e54CqJFNha_cONZIZ4qWeeVUwAK-gyTNtSANo5b0Bvv9NFsg67IRlpf9-da9sqQAeISonvanBbL63oqKy75c9m02v2Hlu-YfsIr7b6FPR4ECQ9vcYuZz5FePDwwgutsE1Ruz_2da80hpZlEUXtcu_ECxdbSmFef98IRNQlDaaiGw1DLp_lCz3KxiDqB3MqLZkdcrI2OEVfI7eEI1AZRYSJIi1mgk1TcWGpcmBJnq_SeRmdhxigFYfgDTXvum1awzgYVeMKGPmxfkFt2QVk-6T2k4srblfU106zEFJS51KDkM0He_nvWaAj1SZ4YV2dvqbezLU3i7N2sK5ULS1XPlCqP801xeJnoImLBjkuwaRg8Gra08I1YJurLE3rzmUEc4TIcIVjOrwMZAoHRT__4fQp28UEvqfldQM1z6God0-kT24q8JkE1mNwxXmJa3pjp0JSeWEdYUDNaQWi1ym4LJX9NFAccK6or5GNSwuubsi6MkvnV5K3FTHA7oSbrJ3YC6irIuNlEDmC2K8McC42rBbcHYNMISU1j0kS2HYg59Om6Rwy8L83w24FJNwzggzC3CILvNv53THWyS8nIsaTizzC1miOEfKcURL524tsyAmsdazsuyGoJf84xsccFBCaAAm6mh5oT1Jgpat1ByKRfA5YwVpKws" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0674cb13c.mp4?token=JZCpB5e1UCsRLy_e54CqJFNha_cONZIZ4qWeeVUwAK-gyTNtSANo5b0Bvv9NFsg67IRlpf9-da9sqQAeISonvanBbL63oqKy75c9m02v2Hlu-YfsIr7b6FPR4ECQ9vcYuZz5FePDwwgutsE1Ruz_2da80hpZlEUXtcu_ECxdbSmFef98IRNQlDaaiGw1DLp_lCz3KxiDqB3MqLZkdcrI2OEVfI7eEI1AZRYSJIi1mgk1TcWGpcmBJnq_SeRmdhxigFYfgDTXvum1awzgYVeMKGPmxfkFt2QVk-6T2k4srblfU106zEFJS51KDkM0He_nvWaAj1SZ4YV2dvqbezLU3i7N2sK5ULS1XPlCqP801xeJnoImLBjkuwaRg8Gra08I1YJurLE3rzmUEc4TIcIVjOrwMZAoHRT__4fQp28UEvqfldQM1z6God0-kT24q8JkE1mNwxXmJa3pjp0JSeWEdYUDNaQWi1ym4LJX9NFAccK6or5GNSwuubsi6MkvnV5K3FTHA7oSbrJ3YC6irIuNlEDmC2K8McC42rBbcHYNMISU1j0kS2HYg59Om6Rwy8L83w24FJNwzggzC3CILvNv53THWyS8nIsaTizzC1miOEfKcURL524tsyAmsdazsuyGoJf84xsccFBCaAAm6mh5oT1Jgpat1ByKRfA5YwVpKws" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توضیح رئیس جمهور درباره چرایی حذف ارز ترجیحی/ مبلغ کالابرگ افزایش می‌یابد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/679019" target="_blank">📅 22:23 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679018">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/721068f983.mp4?token=Th67q4S_ZtkZVRuwGeRqAoOvnhR_WCJJvc31L-AgfotbOpHJMB_WU35pVGwC-eqAx7lfESces6Osze9fUBqV4Ta_wuRv91FF_mCJ6ecLHSGnGm673t-hKvAKzdQoqTmojBFJ8KIKeSIYGWZxavwIyDS9Sa_MgHGf5fRjFRHe8SWUEvuq8_oIEcHaKyLlApX35BYieNvYw6EfH4_ldXBMmyncgVitYQZhz2htB6ACUylKrGm6nd8gVQ9rUUqFeNoUna0guKhtxIYhHl5ODrnO7vTBlzzcMpmoY7pmFRhDBiVhHiPLts4ZJ1ZVh6yAW-7tvinX_4PQC55imz77XAxNYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/721068f983.mp4?token=Th67q4S_ZtkZVRuwGeRqAoOvnhR_WCJJvc31L-AgfotbOpHJMB_WU35pVGwC-eqAx7lfESces6Osze9fUBqV4Ta_wuRv91FF_mCJ6ecLHSGnGm673t-hKvAKzdQoqTmojBFJ8KIKeSIYGWZxavwIyDS9Sa_MgHGf5fRjFRHe8SWUEvuq8_oIEcHaKyLlApX35BYieNvYw6EfH4_ldXBMmyncgVitYQZhz2htB6ACUylKrGm6nd8gVQ9rUUqFeNoUna0guKhtxIYhHl5ODrnO7vTBlzzcMpmoY7pmFRhDBiVhHiPLts4ZJ1ZVh6yAW-7tvinX_4PQC55imz77XAxNYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت پزشکیان از انحلال بانک آینده/ اصلاح نظام بانکی ادامه خواهد داشت
🔹
یکی از اصلی‌ترین روش‌های کنترل تورم؛ اصلاح نظام بانکی است.
🔹
امروز با کمک وزارت اقتصاد و بانک‌ها برنامه‌هایی برای کنترل تورم وجود دارد و روند اصلاح ادامه خواهد داشت
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/akhbarefori/679018" target="_blank">📅 22:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679016">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b26ea9f032.mp4?token=cFzEEUprJHUWoFlibzf5Y_K0Dz9P-kCIojfopne_PTe-iJIR8wnnEW5RdYDlfdetyXiP8mbjCHts5nEK7mCUxHjtH3q58Rf3zG-E7U7AYWNQ818Ub3Gb-MmBe1_KX7rgDYexFPp-ZDxWJJxyGIu2xnI5eJ7ysBkzbGcD-F1AMlHPuym1YSZOtbXmLbMMZH32F45zeiBD8ZvlBjq2wQ8GO11TASLtuW5VF4TPlLsEUaEaJ1V_P_isQ4c5oMOUnLxPpCJtiQEPLYvtOp_EqsKp7hJK4LHMh2uBhoVRHEHX7z8PlUplpX3xhKBzsJOs1lFoHnHMSgT4ckZA2WfjWEZSrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b26ea9f032.mp4?token=cFzEEUprJHUWoFlibzf5Y_K0Dz9P-kCIojfopne_PTe-iJIR8wnnEW5RdYDlfdetyXiP8mbjCHts5nEK7mCUxHjtH3q58Rf3zG-E7U7AYWNQ818Ub3Gb-MmBe1_KX7rgDYexFPp-ZDxWJJxyGIu2xnI5eJ7ysBkzbGcD-F1AMlHPuym1YSZOtbXmLbMMZH32F45zeiBD8ZvlBjq2wQ8GO11TASLtuW5VF4TPlLsEUaEaJ1V_P_isQ4c5oMOUnLxPpCJtiQEPLYvtOp_EqsKp7hJK4LHMh2uBhoVRHEHX7z8PlUplpX3xhKBzsJOs1lFoHnHMSgT4ckZA2WfjWEZSrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت پزشکیان از انحلال بانک آینده/ اصلاح نظام بانکی ادامه خواهد داشت
🔹
یکی از اصلی‌ترین روش‌های کنترل تورم؛ اصلاح نظام بانکی است.
🔹
امروز با کمک وزارت اقتصاد و بانک‌ها برنامه‌هایی برای کنترل تورم وجود دارد و روند اصلاح ادامه خواهد داشت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/akhbarefori/679016" target="_blank">📅 22:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679014">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49280562db.mp4?token=v5nW8CEPRTGs8SsT4kAtZWt96fvNqHUEEaXJS2iHCD-LCBTL_EmxbY3Yg4NvUboj1xrlaLS2_yUS4ZyJW4sOOqU96U1B6ileZhu-4BUcurYOjoBBFv3H3L9Fvh9rd6GzYtUXp1w8ArdqtKcsZ-Bj2EkFkL53d3dc16QRO5k3YpsdVY7rZBKjJdKelAlbha_xcUqWATTaYccq_ZasQbMhN4CM0FaLLOHZvt1aNf75hgu26ttunA554P3ptQkqVOwfKO_K1DD3d5uoKfUE8DejFQ-JGUGZgK_q2XRLU2-7N94TQeYqiVW7RDMT4tBluMnUfbQKP0_wjI3hPKf5cDPGVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49280562db.mp4?token=v5nW8CEPRTGs8SsT4kAtZWt96fvNqHUEEaXJS2iHCD-LCBTL_EmxbY3Yg4NvUboj1xrlaLS2_yUS4ZyJW4sOOqU96U1B6ileZhu-4BUcurYOjoBBFv3H3L9Fvh9rd6GzYtUXp1w8ArdqtKcsZ-Bj2EkFkL53d3dc16QRO5k3YpsdVY7rZBKjJdKelAlbha_xcUqWATTaYccq_ZasQbMhN4CM0FaLLOHZvt1aNf75hgu26ttunA554P3ptQkqVOwfKO_K1DD3d5uoKfUE8DejFQ-JGUGZgK_q2XRLU2-7N94TQeYqiVW7RDMT4tBluMnUfbQKP0_wjI3hPKf5cDPGVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس‌جمهور در گفت‌وگو با مردم در دومین سالروز تحلیف ریاست جمهوری: امروز حدود ۷ هزار مگاوات از پنل‌های خورشیدی وارد مدار شده است و این یعنی هفت میلیارد دلار صرفه‌جویی پول
🔹
سوخت کشور را ارزان هدر می‌دهیم و با همین هدررفت هوا را هم آلوده می‌کنیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/akhbarefori/679014" target="_blank">📅 22:13 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679013">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55f1b62d43.mp4?token=CsJOor3mT2E7WmHZuOaRJ2f9u9K0gkGBO0fANz_4-JpbKdU_ub5AuL4DCcsAIKBp4aUvJQe0uFa0mWXLM8n1IJnlniSSheYtAcQGOkpStrBzMusGG8tK0ayxgL0jH2Kurqau_EVPJFOXY2Z0ClN1-SMxuwFDzfB0OmlOJt2kvjw7yvAhjxl4VosfX8wUz5nppooEbOc5MPEC-ryQRWD4ISqx0SN6vX2Zw13ExBcdcqXeK4FJEYz82sBmIQOzmC4O5i4uC3jlX4yL6gNmB4gf7TTYCbRH5Ra0JIb_F1RPkizRuN7fRKYbIjTzWtGNFE5lUsv8R-8t_8vjQs8Q_xEHzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55f1b62d43.mp4?token=CsJOor3mT2E7WmHZuOaRJ2f9u9K0gkGBO0fANz_4-JpbKdU_ub5AuL4DCcsAIKBp4aUvJQe0uFa0mWXLM8n1IJnlniSSheYtAcQGOkpStrBzMusGG8tK0ayxgL0jH2Kurqau_EVPJFOXY2Z0ClN1-SMxuwFDzfB0OmlOJt2kvjw7yvAhjxl4VosfX8wUz5nppooEbOc5MPEC-ryQRWD4ISqx0SN6vX2Zw13ExBcdcqXeK4FJEYz82sBmIQOzmC4O5i4uC3jlX4yL6gNmB4gf7TTYCbRH5Ra0JIb_F1RPkizRuN7fRKYbIjTzWtGNFE5lUsv8R-8t_8vjQs8Q_xEHzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: در ابتدای دولت با قطعی برق، آب و گاز مواجه بودیم
🔹
اعلام شده بود که ذخایر انرژی کشور فقط تا آبان کفاف می‌دهد و از این تاریخ به بعد سوخت برای چرخاندن نیروگاه‌ها نخواهیم داشت؛ اما با همیاری و مدیریت این مشکل برطرف شد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/akhbarefori/679013" target="_blank">📅 22:10 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679012">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d501b4c3d.mp4?token=Oe5DG1y2Jd5CfGeIGY-3I2D7177eCM-E6wS8Kv_C-HfETZGqpl7KGYwDOg1NwieFb5SJDP15dLO7dkzIsrEnGCCrgoLuJpY85GvxLaf18n2-z9wwGJPAkVwqN-CwI4RfbT-52aD490FxDnB-clkPMH1QPOZMhFoQNUu3mknRHWMmfMk8_IKLxz439WuvfduspKbT5sWEleegNJ1DbYm_GTi09DeyTCeSk0N4t6KF4X4afiUC8F_tannN6aYnG-7Ag-0PRjxdfXjM32m_pVFLzmJW7GclukT6e1UmCEiTLDCHyTaxvnvBQq0WFYOGPsx_OgxPxFA53-aIc6KyC57lvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d501b4c3d.mp4?token=Oe5DG1y2Jd5CfGeIGY-3I2D7177eCM-E6wS8Kv_C-HfETZGqpl7KGYwDOg1NwieFb5SJDP15dLO7dkzIsrEnGCCrgoLuJpY85GvxLaf18n2-z9wwGJPAkVwqN-CwI4RfbT-52aD490FxDnB-clkPMH1QPOZMhFoQNUu3mknRHWMmfMk8_IKLxz439WuvfduspKbT5sWEleegNJ1DbYm_GTi09DeyTCeSk0N4t6KF4X4afiUC8F_tannN6aYnG-7Ag-0PRjxdfXjM32m_pVFLzmJW7GclukT6e1UmCEiTLDCHyTaxvnvBQq0WFYOGPsx_OgxPxFA53-aIc6KyC57lvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بخش دوم گفت و گوی صریح و تفصیلی رئیس جمهور با مردم
🔹
مسیر اصلاحات آغاز شده و متوقف نخواهد شد
🔹
توسعه انرژی پاک، عدالت یارانه‌ای و اصلاح مدیریت، سه محور تحول اقتصادی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/akhbarefori/679012" target="_blank">📅 22:08 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679011">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nTD9jZkiWnk58RXPl66HIqkWHlJeSypssdAz-9XQDoj7lC8c8UvbAS0dxkDc7oygEu_GSYE3RqVNQzYo71y_P0lwaE1LLCHMf1vMpEJ47mF8rs8dAD3mTV_Uex1gfnhjLJVQbiQY71WRABnFZNq9ulOeQddhmWOs76P2mxiF2XQHX0BvSBD2yoVNnu1JVR3gwkvr6whxCCRqgsZzJASvWHLddwKkIG3DAc2hm0TNZIs7f7QcgZ6X1h8mcamJ_n-jDlpu1rIZ2Z6Vmamw5I3TB2PxUYsleRqCwSE-yV-9nm5VZ58b5Kmrigm8_rhcdvsy0n_ncaCy_udn1yD8Y5FcjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پاسخ قالیباف به ترامپ: این دیپلماسی نمایشی، شکست خورده است
🔹
حملهٔ بزرگی تو راهه… صبر کنید، بی‌خیال، اونها می‌خوان مذاکره کنن، این حرف‌ها چیزی جز یک دیپلماسی نمایشی تکراری نیست.
🔹
استفاده از قلدری همراه با وعده‌های عمل‌نشده و اخبار جعلی به‌عنوان اهرم فشار برای مذاکره، یک استراتژی شکست‌خورده است.
🔹
واقعیت‌ها را بپذیرید و به تعهدات‌تان عمل کنید. ما به نمایش‌های بیشتر نیازی نداریم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/679011" target="_blank">📅 22:06 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679010">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
بخش دوم گفت و گوی صریح و تفصیلی رئیس جمهور با مردم
🔹
مسیر اصلاحات آغاز شده و متوقف نخواهد شد
🔹
توسعه انرژی پاک، عدالت یارانه‌ای و اصلاح مدیریت، سه محور تحول اقتصادی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/akhbarefori/679010" target="_blank">📅 22:05 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679009">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYYSHGQFdKE4ovHDU1moe1JWqnv-aNfRdRpyLygtJ7g1UmOncc3GCmU5g1q3LYYlAmDi_uisaDOvWmz0SbgYrhkydxkS78-Ju1oEY2etc1EhnYXBFsrL1h0mm0WGv8V3nU9LTwyD4xZJVo0UDZBchM_yX0MBjX_hlznVH-3mTRvQqWiiAjxkv0rI8cRhaxcpia0d-ZXvE908mi4B_SeUOhIFoLPCNT6YI3cybzV3ZYnCaximzkV3fJD1ONEgsefE9Hz3Y7VGundGbJenHw94OrmVKVgA54VuV9pymvJ7y-jD8FQx6ph8HhliqYWX3pSI8AB7H4GBZzY8zhwjoLodrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
مام اسپری سورملینا
💥
✅
۱۰۰٪ حذف بوی بد عرق
✅
بدون حساسیت، بدون لک
✅
مناسب برای خانم‌ها و آقایان
✅
ماندگاری بالا با یک‌بار استفاده بعد از حمام
🔵
🟡
بسته ۲ عددی با رایحه اسپرت و دلپذیر
🔥
سفارش با تخفیف ویژه از لینک زیر
👇🏻
https://yeklinks.ir/mamtele?utm_source=foritel
https://yeklinks.ir/mamtele?utm_source=foritel
پرداخت درب منزل +ارسال رایگان</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/akhbarefori/679009" target="_blank">📅 22:03 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679008">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
گزارش شنیده شدن صدای انفجار در بندرعباس و قشم/ هم‌میهن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/akhbarefori/679008" target="_blank">📅 21:59 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679007">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68a748f282.mp4?token=AqiXIDB89VmtvClU2aXz2AUdry3qkuXbQDs3YRKqR7ByL8v89Qviyq7qPISpF1FugiTR7SVXBJkgwAlk0HgmbYXPScdymwivmNA04ws-l43a0tTa4_y4wh6RqUmLrIMUad4cg5txP3rIGwVM75oNxBa3dTzmWpCz72bSc280-UtklPYlp0dEd0f6mdJGbFRKk811SRZf2JXo--DWyQV1fphvc-4VfWGQPSCaA9FIv05F72k8banS9hD60wLPbqeiWKKY3T1OfrveDNfVEllcidEhMY92DmNSvYCvEAfXrmpnxnrsPR5VQ4UaBjpXONmHg7-ZLwGenFETL5eYpHC89g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68a748f282.mp4?token=AqiXIDB89VmtvClU2aXz2AUdry3qkuXbQDs3YRKqR7ByL8v89Qviyq7qPISpF1FugiTR7SVXBJkgwAlk0HgmbYXPScdymwivmNA04ws-l43a0tTa4_y4wh6RqUmLrIMUad4cg5txP3rIGwVM75oNxBa3dTzmWpCz72bSc280-UtklPYlp0dEd0f6mdJGbFRKk811SRZf2JXo--DWyQV1fphvc-4VfWGQPSCaA9FIv05F72k8banS9hD60wLPbqeiWKKY3T1OfrveDNfVEllcidEhMY92DmNSvYCvEAfXrmpnxnrsPR5VQ4UaBjpXONmHg7-ZLwGenFETL5eYpHC89g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تارانداز اسپایدرمن؛ اسباب بازی برای کودکان بالای ۳۰ سال
😄
🕸
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/akhbarefori/679007" target="_blank">📅 21:57 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679005">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kRkTUrm5cfFMUmuR_B_dVHEYJRvzdpzdU82gmGgZzScepDPtlm_zcaVXOXhdH6EQyyhYXecelQtJ42QfGV76IMiDDspPqMlmU6DrixErN99UzguWIYj5eOvGdxUDl6cylGsJ-IattdTObb7-cWOPDgkZU2fKX__sK_C8cfGg2ZFdx_Ez4HFL8P_n0zmxZPXYMw06BN0-zzJzwXlayMWhIbyJVjVCNsXF_pGMx-gCDYXMm44vJ2w4lNCoCDDMcOf3Tffe2htWiIOamFtePEQixH9nOjiRXtw71FjzAkPMry03Z5Ql0zyCf-x84g2OI0wh5GTnQJDdDYn8GuRKdtmBCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای رویترز: طرح ایران برای دریافت عوارض از کشتی‌های عبوری هرمز با موانع جدی روبه‌روست
🔹
منابع صنعت حمل‌ونقل می‌گویند طرح پیشنهادی ایران برای دریافت ۵ تا ۷ درصد ارزش محموله از کشتی‌های عبوری، عملاً قابل اجرا نیست؛ زیرا پرداخت این هزینه می‌تواند ناقض تحریم‌های آمریکا باشد و پوشش بیمه خطرات جنگ را نیز از بین ببرد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/akhbarefori/679005" target="_blank">📅 21:55 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679001">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VUKDjOgJQzQSAKrDEcAHtYMNoe6PySscYkmoIUZHNMo943FGo-QRvYWLMV_Q98v3jWv0bEb8pqemMgfLoIuQf3Ds7X3bFQljUEH9LUG3wAleLgND24K20PEwJR-FX5dHUhPi5xaKWnq5i230hE-IGlxApl4u50w-rL9W2BiiioZZfwJv2xsYPEFs93EM-6ecOWwMgm7ssbmpu8v28sMYeYPfhKTEpak8MmSUAN32DJGtN5xHODASNjVoxUjU2sCimTRe3B2svMgUYVdtwCCA_LJ5mEpqOB7lr77PgB7aZtaNscral2H-zvFws6F2HhyaMbFvJirsfneWrfoPo-cE-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دل‌شکسته
🔹
کارگردان: علی روئین‌تن
🔹
ژانر: عاشقانه، اجتماعی، درام
🔹
بازیگران: شهاب حسینی، بیتا بادران، خسرو شکیبایی و...
🔹
خلاصه داستان: امیرعلی و نفس، دو دانشجو با سبک زندگی، باورها و نگاه‌هایی کاملاً متفاوت‌اند که برای انجام یک پروژه دانشگاهی مجبور می‌شوند…</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/akhbarefori/679001" target="_blank">📅 21:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678999">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
کارگزاری‌ها ۷۷ هزار میلیارد تومان سود خالص به جیب زدند
🔹
بررسی عملکرد سال قبل ۱۰۳ کارگزاری نشان می‌دهد که صنعت کارگزاری ۷۷ همت سود خالص داشته است. حاشیه سود ۳۳ درصدی، همچنان یکی از سودسازترین بخش‌های بازار سرمایه است.
🔹
درآمدهای کارمزدی این صنعت به ۱۶۸ همت و سود حاصل از سرمایه‌گذاری‌ها به ۶۰۴ همت رسیده است. همچنین مجموع دارایی‌های شرکت‌های کارگزاری ۳۷۶ همت برآورد می‌شود./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/akhbarefori/678999" target="_blank">📅 21:13 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678998">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
روایت جدید و تکان‌دهنده دانش‌آموز مینابی از لحظات حمله موشکی به مدرسه شجره طیبه در محفل ستاره‌ها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/akhbarefori/678998" target="_blank">📅 21:10 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678997">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWqY3wSOk4wNyuSbxdCFcizTye8YD6TnDjIXVoKDHQiOI2cP4oYt5DoCrxBpJNZdBJXQ8LJEHwZKLrCGeydzzkHCXPlynAkznxr96NfifCDXOgWRfYEQXWrpq6bBBV9Ox2aLYcuIEkxMw4L8fp-SiZWShoJy9g0ksJ3nzdw_9COdZbwKp9RLiz8tsO9KTBz_CykHqbkEA_RF0qLHdzIjR1NdEXXlnltTEszyqOQQ-QqvGn3u9wu_Eopxs5fS1Lf6xE4TFzgWgFLvC78n49_SsgQ4Bb6atCpDFyqdEmBjnkN2lpM1SqC01mtHZL8v2nyZzGNSpFG0GWISGsieamhy-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
همه چیز درباره توافق مهم ایران و عمان بر سر تنگه هرمز/ این تفاهم جنگ را برای همیشه پایان می دهد؟
🔹
به نظر می رسد اگر ایران بخواهد مساله تنگه هرمز را به نفع خود حل کند ابتدا باید اختلافات خود با عمان را حل کند و سپس سراغ گام بعدی یعنی آمریکا برود.
گزارش خبرفوری را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3235999</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/akhbarefori/678997" target="_blank">📅 21:01 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678996">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
لحظاتی منتشر نشده از دیدارهای صمیمانه خانواده‌های معظم شهدا با رهبر شهید انقلاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/akhbarefori/678996" target="_blank">📅 21:01 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678994">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
۷ تا ۸ درصد تولدها در ایران متعلق به اتباع خارجی است
رضا سعیدی، رئیس مرکز جوانی جمعیت، سلامت خانواده و مدارس وزارت بهداشت و فوق‌تخصص نوزادان، در
#گفتگو
با خبرفوری:
🔹
در سال ۱۴۰۴ سامانه‌های ما حدود ۹۵۴ هزار ولادت را ثبت کردند که از این تعداد حدود ۸۹۲ هزار ولادت در ثبت‌احوال، کد ملی ایران را دریافت کردند.
🔹
به عبارتی سهم ولادت‌های اتباع خارجی در ایران ۷ الی ۸ درصد است و سال گذشته ۷۰ هزار ولادت غیرایرانی در کشور داشته‌ایم.
@Tv_Fori</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/akhbarefori/678994" target="_blank">📅 20:43 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678992">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dwPAidfP_TL9uH31hlmPSEF2fb2jPi7kJ_ZIFoLx7ljhs_75EHcucemZywJe5DYVCvHifzx3AgaVpp1tZ7xmfjat9yuWsasBYeCfIRNbQBiBFr3DJklwTrYBf4aGnMkC-O4e-G5FF4Xjo1EW6H4JCMhGWBxqW2mI6XrlXLpPKNCSKSgoEBXqOCiuXQJ6ISLoZLdwNk92iDET_agACbSlPb9KDxY_4z5CB7bWN0MYhWioBCd9Nr26VWyB3E4_OKwSkjsq8ALtN6GdSRju6j038jFwl5MAjFB4ZAPQjBl0EbKJlmaCV889GC9rG8WfFGy410tNUUklTQzx0Ymshhujwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک میلیارد تومان طلا را کجا نگهداری کنیم؟!
🔹
در این مقایسه، مزایا و محدودیت‌های هر روش را ببینید و انتخاب آگاهانه‌تری داشته باشید.
🔸
کانال رسمی داریک در تلگرام:
https://t.me/daric_market
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/akhbarefori/678992" target="_blank">📅 20:40 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678989">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvU5mOtcxkBu6O8Qe69izQj8NATQXQ70Sl1Af7RFZV5mQAsFa7yNgpi9NoCq6IO83oaCBKmjUH6w1Qpdkzq7LGpOWA6RsH-Qz07yMUrOY4Jg9HwouDDj76uiZLPA1EvGxOcKEcHLJk2rP0T35czhYi-mXQW592m2U777NejO3184r5zMKD4wsYBaJoXql0NpdSRg5OcJCKS0jr6Nj8ElikpD6rQVEi3W9JxCmP1eG5AyRIjBdzXmSsK2qf2GjMdl_A7io8XnrdFv__-i7WVZb5PYDu-d0QdQBXdc0iACvtQ38L29_3r7UL3CsUYQphAloGV8DDXUsc5RHnyhgrxwLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بومرنگ، چه تحول مثبتی
سفارت ایران در اسپانیا:
🔹
محور متجاوز اپستینی جنگی تجاوزکارانه به راه انداخت که تهدیدی وجودی برای ایران به شمار می‌رفت.
🔹
اکنون همان جنگ در حال تبدیل شدن به تهدیدی وجودی برای هژمونی ایالات متحده در جهان است! چه تحول مثبتی!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/akhbarefori/678989" target="_blank">📅 20:33 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678988">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
وقتی بدرفتاری با پدر و خانواده، عذاب برزخ را رقم زد
🔹
00:06:00 تندی و بدخلقی کردن با پدر
🔹
00:28:20 ماندن در کنار خانواده برای اثبات سلامتی‌ام
🔹
00:42:25 هدایت شدن به تونل مذاب در انتهای اتاق بیمارستان
🔹
00:47:20 گرز آتشین در قبال حق‌الناس نسبت به خواهر و همسرم
🔹
00:59:50 تقسیم‌بندی دریایی از مذاب برای انسان‌هایی با ۵ گناه
🔹
01:06:40 اجازه بازگشت به دنیا بخاطر جلوگیری از خودکشی مادرم بعد از مرگ من
🔹
01:12:30 شرایط امواتی که بازماندگان آنها بر مزارشان حاضر نمی‌شوند
🔹
قسمت بیست‌ودوم (جان مادر)، فصل پنجم
🔹
#تجربه‌گر
: حمید جعفری
🔹
قسمت قبلی
#زندگی_پس_از_زندگی
#فصل_پنجم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/akhbarefori/678988" target="_blank">📅 20:31 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678984">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b2201b7fe.mp4?token=tatGc6zLJFGGXaFPHuVabhouOjW57Ieu2x9N1CPsH3cW-XM6VtS5hWzlpICX8Jj-VmX9A3QfPhmteGsnxmC1Buw8IM0UUIxU5cuDITNIfgTXQMlYIgttxk5z_WDsRvi0ihcibalnT4jo8JYZsoBr8dh1BnJNmirMgmwGIUItaO6tffTfeTrodNFWPdEJyP3A7G4mEA4LOi8C5Q3CcOE999Oq6axaZpbyWmvP3K-g0yFZrNjiK5jbN-DOYiEnLoL0NwA3-KC_ByyBv25dJRBj82HqSUmZevGpqtnIUZtmPbDcXQstQ3PryhfG2BfxdjNtAOtlUAIUaJQLH1w2KfWK5U_Fq5DY0Jgh_FAECv0TasnOe7fjWER7az9erRibKVZ1cMFwspbUY-_-926cNtCtK1g39dC4UyhNQAVqx2iLT8uiRZFcBdggY8KF6nHP6zn2YjNSu9ivvYueR9pApe-Guh0hsUjoEuJJTbZvo3h-pODEse2aN53HaTCFqr9bGd0LIj4HKqiUbGNaa5rfYfhq6XZBZ4j67e4c6WXLtO7JSlN1EvH8lBJMrK1aI4lm69XYtpWcCqI47B-q-IV6LRI3tRMU5gidvyIiprWczFZ3tDVIf6TgXnlSBmTvPtDemCoBMZRN1DCj6m_HXWUvfIXIH-_xDTophmYWeYA2Q0Vs6Ko" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b2201b7fe.mp4?token=tatGc6zLJFGGXaFPHuVabhouOjW57Ieu2x9N1CPsH3cW-XM6VtS5hWzlpICX8Jj-VmX9A3QfPhmteGsnxmC1Buw8IM0UUIxU5cuDITNIfgTXQMlYIgttxk5z_WDsRvi0ihcibalnT4jo8JYZsoBr8dh1BnJNmirMgmwGIUItaO6tffTfeTrodNFWPdEJyP3A7G4mEA4LOi8C5Q3CcOE999Oq6axaZpbyWmvP3K-g0yFZrNjiK5jbN-DOYiEnLoL0NwA3-KC_ByyBv25dJRBj82HqSUmZevGpqtnIUZtmPbDcXQstQ3PryhfG2BfxdjNtAOtlUAIUaJQLH1w2KfWK5U_Fq5DY0Jgh_FAECv0TasnOe7fjWER7az9erRibKVZ1cMFwspbUY-_-926cNtCtK1g39dC4UyhNQAVqx2iLT8uiRZFcBdggY8KF6nHP6zn2YjNSu9ivvYueR9pApe-Guh0hsUjoEuJJTbZvo3h-pODEse2aN53HaTCFqr9bGd0LIj4HKqiUbGNaa5rfYfhq6XZBZ4j67e4c6WXLtO7JSlN1EvH8lBJMrK1aI4lm69XYtpWcCqI47B-q-IV6LRI3tRMU5gidvyIiprWczFZ3tDVIf6TgXnlSBmTvPtDemCoBMZRN1DCj6m_HXWUvfIXIH-_xDTophmYWeYA2Q0Vs6Ko" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ چگونه با موازنه تهدید در برابر ایران وقت‌کشی می‌کند؟/
تلویزیون اینترنتی مدار
دومین قسمت "نامه‌ها" را ببینید
👇
https://youtu.be/48Ci2wDj1HI?si=xahSwBa6bMJX_vG5
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/akhbarefori/678984" target="_blank">📅 20:25 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678981">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jvmZfy-_3fGwTH-PJotUBuPp7Qwj_V6Im11h0G4et7H0wo_3-TWhbwxx4Ru-pDL5oaNLVOnmfDWHXOEsP5GdDXmN4agEA2MpIeXGj_GPmzfF5v3jyd9g6fBj3gJBFAYrLeuy7eRLnJVeM0VZ3bcZYFbJI1kIohplEOl72gNQRNa1BnyweTH1-_YIOl1czNkjN6HD3L-9HTDzniycdfZZlrYM1GxuwZuZ2ylLfl8wLP3S7yB0fQy2dfgGFB1-Ime9mqvLm1xrXeijqWFA8M7ZJByrhOXzKvYz-ItDmZdZue05lUtyplbjxuEZwiMOdMx56I-VjnU1XXDoSzMELPIKlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای رویترز: ایران به کشورهای خلیج فارس هشدار داد که به ترامپ بگویید دست بردارد وگرنه به شدت با شما برخورد می‌کنیم
🔹
ایران از کشورهای خلیج فارس خواسته ترامپ را به توقف حملات متقاعد کنند و هشدار داده در غیر این صورت، تأسیسات نفتی، پالایشگاه‌ها، نیروگاه‌ها، زیرساخت‌های آب، برق و حمل‌ونقل آنها ممکن است هدف قرار گیرد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/akhbarefori/678981" target="_blank">📅 20:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678979">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2f3c50bb2a.mp4?token=EZfK7_kW_YBX9T7cRISwZWHWb1X9NNVpaQZmtpcCCZxA8tt94MX3W6FPsamwavBdnhUKx_86oV71FdbOiS3Ci3c10-f2--9AnqQBvV7NMANBKZe3vtwimLGi6cE4pd7KcYcsckmp1kwcR-A0xmcfuTktIhV1YTTGBpevatuHrJr6xMx37_aeK48ubhQ6wkSq2BcUF1v9oNZEqertKkT4tZ_3SHOzW8mLhqIe_zQTzMMtMt1cYVKd27fKgf3qh28BIIBw7aZHqQvvbWmUJaFyGsz2qrI5YeSgkD265usfrYJaJSdM_b-MEO0C4bmNFQGcCLquUsCYepC3N4bXmT0nXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2f3c50bb2a.mp4?token=EZfK7_kW_YBX9T7cRISwZWHWb1X9NNVpaQZmtpcCCZxA8tt94MX3W6FPsamwavBdnhUKx_86oV71FdbOiS3Ci3c10-f2--9AnqQBvV7NMANBKZe3vtwimLGi6cE4pd7KcYcsckmp1kwcR-A0xmcfuTktIhV1YTTGBpevatuHrJr6xMx37_aeK48ubhQ6wkSq2BcUF1v9oNZEqertKkT4tZ_3SHOzW8mLhqIe_zQTzMMtMt1cYVKd27fKgf3qh28BIIBw7aZHqQvvbWmUJaFyGsz2qrI5YeSgkD265usfrYJaJSdM_b-MEO0C4bmNFQGcCLquUsCYepC3N4bXmT0nXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همه کشورهای دنیا برای عبور از تنگه‌ها عوارض پرداخت می‌کنند اما وقتی نوبت ایران می‌رسد، صدای اعتراض برخی بلند می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/akhbarefori/678979" target="_blank">📅 20:14 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678977">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار رهبر شهید انقلاب🇮🇷</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n3hfPtG7QAS5JkTri7v7UZHL6K8ySl_StUuA4urErnYkk9FYV8uNeZNCyD6hMu80uUKjqTVBcxKmASGE3H-Rqw4WYcMiYAcqF4vvPNl-ZiUWR-fB8oHS0F1HvGlrkcdthwbxVsvI48xOwwj7PYWKkfxTN0ajhq1uQi1LvrCm8gJ6lInySVkcaH6DIqDNfAeqEqh34t487nE6w5RN7CIKwfNO1WmvHGYhfx9JpfkoglJweI2axb7fm4vpWD1tB1cHC7dWyofcI56wb_HYP9ZQzHPjJXsldUGv8JyZcvgoNNTBhfuHI0FK7YNLmRogt4rSC8V_LUyzh9foldqKBDXWuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
توصیه‌ حضرت آیت‌الله العظمی خامنه‌ای رضوان‌الله‌علیه به قرائت قرآن و دعا برای پیروزی جبهه مقاومت
🔹️
رهبر شهید انقلاب اسلامی در پاسخ به سوالی، قرائت
سوره فتح
،
دعای ۱۴ صحیفه سجادیه
و
دعای توسل
را برای پیروزی جبهه مقاومت توصیه کرده بودند.
💻
Farsi.khamenei.ir</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/678977" target="_blank">📅 20:08 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678975">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/akizPvF2sU1zxve1Dr5eG5rf8C4rn8YvtCfHfpiylJM8EX79ZZ_dYhb-g5qLwAJc5JAX_UBBv7t_zMJbTkSL5OpWJylWgNz3llRWj8X8WasC0F981YlVJvpIGHRugSA4oBKDyQtEGj8eaCpnnDFqAxm5wnM20xNZFeWRi9v21XvepvlZlT3EOtN45t9seCeD1V4ZXVSW2z_eqL6LkEDCS3vAr1bxCr76gvJ8404cBZwqrzLLwfZAQFMDF8hHbHKq1IcWOq1BwCxJHvP2IiHRwhYAeVt4eEhzNk6xmtFwPmw6REJlaVI9Cp_Zl2YETcGSyGjs0sKu9uteiKRXTzTw0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شارژت زود تموم میشه؟
🔋
این تنظیم‌ها رو فعال کن تا باتریت بیشتر دوام بیاره
⚡️
#ترفند_فوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/678975" target="_blank">📅 20:01 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678974">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dP8vp_9FyWA3AV1Z6pPvREtqBCrmCyyH272z6bcn9okyIk38E2lZi1Hf0FucJh10c2k0xRC4bVR6mU8g5mAt0pvznIcc0wcyKCy1DJgY01Dy5HlZEEKOaB__zULOciy9ph_48yxmG1QtvEb8x8Dr2SoqQVWqSmIejG-DY_TIo6UKm_8ex_AsQZ5d0GEtXKz03cx-AExB2aowFsVDKmccmoGTX8pc7U-I1zG55KMCX44z-FlYeeEbAGpB5CZ6JH6_w_l_Uk0hd_xI255qmHesLOnfPigrhfkA47Aho1C56Z-iedcBAkreW7ZgDSNBKDXI6JmvgEpSoenv3u-o8IrsaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
هرچی برای مراقبت و زیبایی می‌خوای، توی ارکیده شاپ پیدا میشه!
🌸
از محصولات مراقبت پوست و مو تا بهداشت و زیبایی، با برندهای محبوب و کیفیت مطمئن
🛍️
برای یه روتین کامل و دوست‌داشتنی، انتخابت رو به ارکیده شاپ بسپار
💕
📦
تنوع بالا |
🛒
خرید راحت |
🌷
انتخاب‌های جذاب
https://t.me/Orkide2025
https://t.me/Orkide2025</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/akhbarefori/678974" target="_blank">📅 20:00 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678973">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qc-Bd3OrQgp5vGsMablcJAdsYEuKWPlvAllpFTeOzkxV0mf5Kb2qX0B-T96YzAxP-7YukKnWRdnCGAn6jY-BULaQ4aiuqJVselqbM4FH1fyscu4YKmzujvCB0zkMaKkTYOb5RDrOkL-KtVGJSBEFhcXkSL65Yt_EMzOWpt-MEC37l_MRDEbNxhAM3a_z90OmYCscTSrwWMociPLZoDDXMRhGCDhXPYYPMj7-pcwTVJy-vzH3ccrrcnx2ikY9m1nF7PAzjPAmGhcy549-pxcW-_HoVypByinMS-NOnJeN8WcMixxYwX00V04aJyPz1zJNXE_A6W7QGJPs7HI6rplfwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ در حال سوختن در آتشی خودساخته
سفارت جمهوری اسلامی ایران در سیرالئون در وصف وضعیت ترامپ:
🔹
محصور در میان جنگی که نمی‌تواند پیروزش باشد و شکستی که نمی‌تواند بپذیرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/akhbarefori/678973" target="_blank">📅 19:55 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678969">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/729a70a35c.mp4?token=FYtRyZj5nsIhmIcG6LTzWyFqlE4kQOVyeV3488rHGoN3EDVlY5DghxiubV1u9PJa-uMKHdIMupEuVwGhBl2rEj1hmJi46EJHXC44huRXOsAfnWF7Who-XmDYVQ2hvWi68P6r820157tEGukYFCgnBwT8Wpz442DF4cl5U4BYLPh3LNhrY5tO0PmQG0owgOngIFg8t22OrGVjnwRQInRDaYPyQGyJKTKea5RdctMYOnaIegvQr5sLcTOSHhLX8DTt9sqEOi78To6ue82pGa0HTWTqpCvKW7XlArKaW-nast8RH2R1Y4yK66tEPgCbsSwdLfSWrjr0g3EHXm_v3GD2Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/729a70a35c.mp4?token=FYtRyZj5nsIhmIcG6LTzWyFqlE4kQOVyeV3488rHGoN3EDVlY5DghxiubV1u9PJa-uMKHdIMupEuVwGhBl2rEj1hmJi46EJHXC44huRXOsAfnWF7Who-XmDYVQ2hvWi68P6r820157tEGukYFCgnBwT8Wpz442DF4cl5U4BYLPh3LNhrY5tO0PmQG0owgOngIFg8t22OrGVjnwRQInRDaYPyQGyJKTKea5RdctMYOnaIegvQr5sLcTOSHhLX8DTt9sqEOi78To6ue82pGa0HTWTqpCvKW7XlArKaW-nast8RH2R1Y4yK66tEPgCbsSwdLfSWrjr0g3EHXm_v3GD2Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دیدار باورنکردنی: شیر بزرگ‌شده در لندن صاحبانش را شناخت
🔹
کریستین، شیر نر (۱۹۶۹–۱۹۷۳)، توله‌شیری بود که دو استرالیایی به نام‌های جان رندال و آنتونی «اِیس» بورک او را از فروشگاه هارودز لندن خریدند. آن‌ها کریستین را در آپارتمان خود در محله چلسی لندن بزرگ کردند، اما وقتی او بیش از حد بزرگ شد و دیگر امکان نگهداری‌اش وجود نداشت، با همکاری جورج آدامسون، فعال برجسته حفاظت از حیات وحش، او را برای بازگشت به طبیعت در کنیا آماده و رها کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/akhbarefori/678969" target="_blank">📅 19:28 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678967">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
جزئیات متن اولیۀ طرح راهبردی مدیریت تنگه هرمز
سلیمی، عضو هیئت‌رئیسه مجلس:
🔹
متن اولیۀ طرح «اقدام راهبردی تأمین امنیت و پیشرفت پایدار تنگۀ هرمز و خلیج‌فارس» در کمیسیون امنیت ملی در دست بررسی است.
براساس این طرح:
🔹
عبور شناورهای متعلق به آمریکا، رژیم صهیونیستی و سایر کشورهای متخاصم از تنگه هرمز ممنوع می‌شود.
🔹
محموله‌های مرتبط با رژیم صهیونیستی، اعم از نظامی و غیرنظامی، حق تردد از این منطقه را نخواهند داشت.
🔹
شناورها یا محموله‌هایی که در اقدامات علیه جبهه مقاومت نقش داشته باشند نیز مشمول ممنوعیت خواهند بود.
🔹
کشورها و اشخاصی که به ایران خسارت وارد کرده‌اند، تا زمان جبران خسارت، مجوز عبور از تنگه هرمز و خلیج فارس را دریافت نخواهند کرد.
🔹
برای قانون‌شکنان، جریمه‌های سنگین از جمله تا ۲۰ درصد ارزش محموله، پیش‌بینی شده است.
🔹
دولت موظف خواهد شد با همکاری نیروهای مسلح، مسئولیت‌هایی مانند هدایت ناوبری، نظارت بر تردد شناورها و حفاظت از امنیت و محیط زیست خلیج فارس را برعهده بگیرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/akhbarefori/678967" target="_blank">📅 19:21 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678965">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e849a8859.mp4?token=cSxOCryWYmMFq3ahzfOyyAoFEvWHy1OnP5uSe97A4dsNEcLjzFKCRAiEF35PEqosHeZ88B5FE8CR4jSQCxzt9S_F7KlhVuaXf7Vjtd5reruXTo3DxI0qx3C-xpXzc4-NgEnLjre44wB_2DmmqY28H_w6IAX_D3bYKAvGGZHyBciuW76L1w6WEv1CWP94qWs3ICzTI8vYoHWnXu7zyK1_bDBQmpSpZp9iibEsO5yGbxY8zOVwe21Mvf9GX4Wjm5bZ8Z0CJHRvrDU88MFagZqsYY9QEupwhzErA2AhhMbVS9_maYbjTfjEwApvwce0k5eTxb0hD7UiRfiyIBL3DQ7Zbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e849a8859.mp4?token=cSxOCryWYmMFq3ahzfOyyAoFEvWHy1OnP5uSe97A4dsNEcLjzFKCRAiEF35PEqosHeZ88B5FE8CR4jSQCxzt9S_F7KlhVuaXf7Vjtd5reruXTo3DxI0qx3C-xpXzc4-NgEnLjre44wB_2DmmqY28H_w6IAX_D3bYKAvGGZHyBciuW76L1w6WEv1CWP94qWs3ICzTI8vYoHWnXu7zyK1_bDBQmpSpZp9iibEsO5yGbxY8zOVwe21Mvf9GX4Wjm5bZ8Z0CJHRvrDU88MFagZqsYY9QEupwhzErA2AhhMbVS9_maYbjTfjEwApvwce0k5eTxb0hD7UiRfiyIBL3DQ7Zbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فوران شدید آتشفشان فوئگو در گواتمالا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/akhbarefori/678965" target="_blank">📅 19:09 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678964">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8i8HlG8OxmJyJYcEZv359D-tKkgLuaa7WDaVt9aF2590_5A4c169dHq0rzzRKYqj9OavhUwoM17xpquOgYIbYCUw2g7gzHEiWcnVJXyA7IaarQ0nOCQm4aiCt5HgYpnTdOBvoQBVIRvWKHlywgHTjJBZ_7U4sZCium3f7QdfPIO-B6tPsQLuKKVsv4UUrH0jg73UAersSLYfiZgkN0Gk1p4s2RMVsChG6VP71g_zdrmsVJEr035iVrQDkD3JcP-cowWF4-ctFd4H_6mZHrykMtoTBXM7ZNf7uF5DSs24qInpeuoVr7Ihsy6a88xv1jcnorGAcI6KWNqliSPgF8Hew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کره زمین با مردمانی پیر؛ پیش‌بینی کاهش رشد جمعیت جهان
بررسی آمارهای سازمان ملل نشان می‌دهد که نرخ رشد سالانه جمعیت جهان پس از گذر از اوج خود، روندی کاملاً نزولی به خود گرفته و در ۱۵ نوامبر ۲۰۲۲ به کمتر از ۰.۸۸ درصد رسیده است.
بر اساس برآوردهای جمعیتی، نرخ رشد جهان تا سال ۲۱۰۰ رسیدن به صفر یا حتی اعداد منفی را تجربه خواهد کرد که نشان‌دهنده آغاز عصر پیری و کاهش جمعیت کره زمین است.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/akhbarefori/678964" target="_blank">📅 19:07 · 15 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
