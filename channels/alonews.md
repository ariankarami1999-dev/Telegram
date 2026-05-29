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
<img src="https://cdn4.telesco.pe/file/AaR_R3pyhxNfD3ghknxpT2U8LFFWby_SQ1f2GX3_xxWjldS57E8pUpaGSzg8aGnihA1B1PWm890nvrThqB2ZFZnCpib3KJuqRuYqWsiFU4D-fCCl2qUdp2f-dEBMBUBsaoCWxoEP_R38Cq6YI4rN-ewFx0g01ShEgOCMSiZ2x8PG8EUIhngLt0bsyugPkaSJx6LtYEE-RdPtowJDKZrdWsbf_JeGsdzGbBEUQB2_2QuMCiY4Xc4duyQgbRZfBqvlj3HtUA1wAJKpPZD9cfhBIbUY3Gh8HxfAn_P-VmyIPHjZ5fp-H4wId6AFlydG_yfwmxJnJLbdza2m971LSESZCQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 919K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-08 05:59:39</div>
<hr>

<div class="tg-post" id="msg-123413">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">بهترین سرعت با بهترین قیمت با God Vpn
🔵
تخفیف ویژه برای امشب فقط
✅
😍
10 گیگ فقط 280,000 تومن
😍
متصل حتی در شرایط جنگی به خاطر اختصاصی بودن
✅
❤️
😍
کانفیگ اقتصادی در ربات دوم 20 گیگ 290,000 تومن
😍
برای نمایندگان پنل نمایندگی فعال میشه
👍
❤️
✅
تضمین بدون قطعی
🌐
اتصال…</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/alonews/123413" target="_blank">📅 01:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123412">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vWRieMGMmjBLLyMrGK-zncqmmNNQ90UCRZoRKyg0cAM6HFOf34KM4No-KyykxmHQ-mL6yLWI9hAqt-l1ljPDeQELSfK_cwaUKVD8699fzwSg7Ucmx5B7njCiATM8rBMIv04wAMl5guaJCMhFZx6m28OKL2PE19wh0afLMkOSIAz4AqORDkU3xzCizuoFdFLdG_1iGB2r64sV5smlFc94_FT2FKeSBnWV_45hONNWQPOY0pIrp8PH0xPnGLwQb1f28IH5aS-Out1Sr3yQ2gazWAb695_a3Q4_6-gecIkfwE7oRaIXsy2MgDHgTWgUP83hfmu388VLlUTyBkd6J9r_5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین سرعت با بهترین قیمت با God Vpn
🔵
تخفیف ویژه برای امشب فقط
✅
😍
10 گیگ فقط 280,000 تومن
😍
متصل حتی در شرایط جنگی به خاطر اختصاصی بودن
✅
❤️
😍
کانفیگ اقتصادی در ربات دوم 20 گیگ 290,000 تومن
😍
برای نمایندگان پنل نمایندگی فعال میشه
👍
❤️
✅
تضمین بدون قطعی
🌐
اتصال با تمامی دستگاه
🔻
🏪
پشتیبانی ۲۴ ساعته
✔️
دور زدن نت ملی
🔘
بالاترین سرعت با تمام اپراتورها
⭐
با کیفیت عالی و ضمانت بازگشت وجه
🌐
🌐
🌐
🌐
🌐
🌐
⭐️
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
جهت خرید کانفیگ اختصاصی در این ربات:
@GodVpnV2_Bot
خرید کانفیگ اقتصادی در این ربات:
@v2raypc1bot
ایدی کانال:
t.me/God_of_Vpn
پشتیبانی و خرید عمده:
@Mmkhh00
@Pc_V2ray</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/alonews/123412" target="_blank">📅 01:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123408">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T5egpM65rwjk9YUR0sVDpws1YPWpRyCoJiwk0Cqs0QJb3eNGITav5QzFx5omG10frLzoTgaQ2Nth35MPYuikDYXEcTCH1RNditXqrC30Bj7JmbC1MIRZHi0jf4g4D5tpfX5ZEy10FTZ5aoaWllIwAJSOaGx1InxF9Rk_2_rCG9ajhIInDUK43AGjRhHnoaBPKIN69KKCnXDropA99v5Cw-ZgTUs_msbXuh6xzFHqEiJQMD8vt6yVTZLZF6pvXobDZ7U4tNvAyPLm55TUPrAMBDjBNnlQc0oQ4b1Sup2s3YPuAyqmpWq0ygUPwCPvek_yHPIGQ6QDUiYXJEGcSbT3cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cnnYnzzfrF0BE7zdem2QW_L4f0oRcsm1YDr7CUPhdit2--p3r0kkZPxeS9RLqls9YAyTiEtqyhgjarMO-qPanryg_zwKrj-HJ11funqagGCIaUNEbO1FVWxB8ep_PtwiFuh-AlTnqA7495pv_SuAVNDD0dZHaMYuGK4N539fWKeKGY3YnisJo5UjKvK5k3psYzrSRQUU6q7gIRXOMm-laFWfAaACaKDRohlw2IObfbJerEPjDHhBLJOoE-naL53YkCEEVr3mRIlFX8nkpvufpcNrzLQ9Va-tOSDykFnmVJpUj57cIifQYuehvCs86Hr07CrUbHDLiEz4PzEeMQcwwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pfwxwXrCr-BGLTd4yVxbXhLIzdoVXE590kpjoYuQjVHUYpJ37kQZUvt6Pwohppa2P-u3GTGtm9nJ2PCoKoFrKwNkgoIbodS1CJ_vZH8KO7hB5QFi0j8Vfa5ceSnKkeV9GEGDlo0aNXlO9NS6GQRMO2E2I3JzY8AyGMmMd3AwXt5CyosH9deCwUwiVnBU-CxzcMLoLIvJ9Jm0ow3qSZ_6C6IAVwRzbauqTFGjBzOntO41E-SQYDFjGlAzxlF3ljAhEe77POOGn7r6m_XiPnArp8yUooaUH6cSKm0QJIUdisxruVGAhfvmsQdj-1rVqttRFFDtA8rTRXsrbHPxqba0fg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fb8eceea1.mp4?token=ofZziQZ9aLRljoO95VvWF8Bmov6EwkPCdQGWi-xoTrlH9RmbPA9x501YLdvdtUpBWy-RxnznUG147U9xiUCse_xWad7vt_LZ8Y9jw5sabOi2fJuTQTTJmb6D6Ur39PHQy8D_Ijcwdl2c-_2zbN5uLOc339otoDa0XGhLdstWt_X5fF8el2Q3JqYyoEdKzR8ybSBSMgE9swRPuFUJyC0Tvzjwd1HIf5B_OainwmJDp4N1lBxrlc5gQODw6H_nmIGbbhJOpnmzklDk0pfnXbQJjjto9EWCevUkgerFmbm-FPtjAYgOF3MVhQXr4cMeVqbbqETI_zBdrh4i9QIjuULYVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fb8eceea1.mp4?token=ofZziQZ9aLRljoO95VvWF8Bmov6EwkPCdQGWi-xoTrlH9RmbPA9x501YLdvdtUpBWy-RxnznUG147U9xiUCse_xWad7vt_LZ8Y9jw5sabOi2fJuTQTTJmb6D6Ur39PHQy8D_Ijcwdl2c-_2zbN5uLOc339otoDa0XGhLdstWt_X5fF8el2Q3JqYyoEdKzR8ybSBSMgE9swRPuFUJyC0Tvzjwd1HIf5B_OainwmJDp4N1lBxrlc5gQODw6H_nmIGbbhJOpnmzklDk0pfnXbQJjjto9EWCevUkgerFmbm-FPtjAYgOF3MVhQXr4cMeVqbbqETI_zBdrh4i9QIjuULYVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله‌های امشب ارتش اسرائیل به جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/alonews/123408" target="_blank">📅 01:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123407">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/D9GnA3_tpOrJbY0RAJmthCawNVImSoQtQwMhYJAPZ6z2YOuHPArOXVJYKtX1U1pm7IngZ3r46hA3ywva3Q3Rh9LYJFbumHeKE2l0K4GfQ1CvttJjQyNonWVblAJ5MZrJxZHaVhetxJm_3us7DAVbCNyI3sc9GcOXfitKaE_1rj-6rQjCKLa6q9Mu4rjierhcvRhFKnDR6mJsEwJQ9_n-v_7OYQIro8imvJZGI7QxyyCvrRGZVs_UQoRyGp8w0aEsgPK0qnnMr_gAe6qptLFxWGe7SFFhDuAbAY-rUk4CF2QGlVw6OGgTm5WVw6WS9AGvSZ59s3UrOAWncIPl-caE0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بعد از سال‌ها پُرشدگی سد کرج به 70 درصد رسید!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/alonews/123407" target="_blank">📅 01:13 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123406">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nlliuvlPH3cm77OURU_rTvq3EBD2kodEkcl0IzUh99aACf9LXbhV7rOkHrb2R2AqNus5dfGLqC-dIlXwVDlyYzBqZe1kyVTqEfb9RjSqAP6a3tHFy6xkP6qAGKeAJ6UhRg-zOSk1ILfpVh1O5OrDy2LmLpv-HJOIzjcjgFCPK6IC89X82gqFCPfCIsZRYCpxxiiOuXaNxpjdacYmNtCIsW45ls9PN9PRdwONJGga9W3I309hx6nd0CbebPhhIRnnKaRZKQ31IRAeZsWW2i5P-f6mnqve00kieaKughR_YW1599uI5xi-U_37GXK0G_t3HjRuED4TSMFyDvhfro9seg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست عجیب کاخ سفید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/alonews/123406" target="_blank">📅 01:06 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123405">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a48cd5832a.mp4?token=spKwqOBVTIRLUnZ52Y32rHET8WedWZQs6JqDTONJUcp4KfrtwNMqHfjbM4sMo3acFPYVSLOh-57rrsSXxgF_j_8i5LQZGK1jYixSnxfc0AvVF-HU_IwCQkK-q3BytfeuP8-5obPzARJRkHoHUuY0NlY0Y6qm_SEOYzqg_5DIAD5Zd6R3BFJHz2sGvS3KYrxTS1LwRXA-4M3w5AkPTYcgcIC4bjOc-UvkWqjSdCHzPKP7HVYa7euGt59Phhq2oJXGeBGrFoly8mAV1Lg9c-5DdAiv0kUhNFMrRovY_uOXDIlCLEC_GdzgztAZjsSs8VieB2GPFNvMCrD-pTgr2Bds_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a48cd5832a.mp4?token=spKwqOBVTIRLUnZ52Y32rHET8WedWZQs6JqDTONJUcp4KfrtwNMqHfjbM4sMo3acFPYVSLOh-57rrsSXxgF_j_8i5LQZGK1jYixSnxfc0AvVF-HU_IwCQkK-q3BytfeuP8-5obPzARJRkHoHUuY0NlY0Y6qm_SEOYzqg_5DIAD5Zd6R3BFJHz2sGvS3KYrxTS1LwRXA-4M3w5AkPTYcgcIC4bjOc-UvkWqjSdCHzPKP7HVYa7euGt59Phhq2oJXGeBGrFoly8mAV1Lg9c-5DdAiv0kUhNFMrRovY_uOXDIlCLEC_GdzgztAZjsSs8VieB2GPFNvMCrD-pTgr2Bds_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصویری که الجزیره از شدت خسارت حملات آمریکا به تاسیسات فولاد اصفهان منتشر کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/alonews/123405" target="_blank">📅 01:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123404">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
نورالدین الدغیر خبرنگار الجزیره در تهران:
یادداشت تفاهم، حاصل جمعبندی مذاکرات در سطح دیپلماتیک است.
🔴
برای اجرایی شدن، نیاز به امضای مقامات عالی در تهران و واشنگتن دارد.
🔴
نیت توافق وجود دارد و انتظار می‌رود که از مرحله نیت به مرحله عمل منتقل شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/123404" target="_blank">📅 00:58 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123403">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
ستاد فرماندهی مرکزی آمریکا «سنتکام» شامگاه پنج‌شنبه هفتم خرداد ویدیویی از عملیات پروازی انجام شده از عرشه ناو هواپیمابر ابراهام لینکولن[USS Abraham Lincoln (CVN 72)] در جریان حرکت آن در دریای عرب و پشتیبانی از محاصره دریایی اعمال شده بر بنادر ایران، منتشر کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/alonews/123403" target="_blank">📅 00:56 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123402">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C7CqwJ7dBOQAk1bedyx0WrFj_gE6luQxIcoWIcnPWLYPKorQa-Lbvy5fPr3rmVzybt9kH9Ycag5i82A7PqVWgfeEslA4uBXc5tkcpLc9HTk0ZdnwiYGYl83OlYnQDuPqPf0mHeE060Q4XxN4Nkw1MWXVlxrJ2KzTIeXugKQH38Bzn4JCQjjH6zq8FBQI6syLEVPvYE9u4BUK9YmKTV326iFbVoiUuXg-5iqlbwCsxBi0i-YiQqllpYC6IZJM24DDUTE8WxaQ7T5MkoerwUznU0RkdPX006qgEyMeo53-eJ4wlMPFZzZfSdDEoSZCKKla8O7Fz2lg2eZ2VHPno_nynw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان:
به جلیلی گفتم توام بیا یه گوشه کارو بگیر کمک کن کشورو درست کنیم. گفت نه من فقط پیشنهاد میدم. گفتم پیشنهاد به چه دردم میخوره اخه. عمل میخوام. نخواستیم اصلا.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/alonews/123402" target="_blank">📅 00:44 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123401">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T36CFdmvbQap0A_YqY4PP6xQWKwotYFKp4VCUEfvMT98krhVEwAPkh8g-cSDfKkHSo7-NWUiPtiokJKlUpqh2lqcD8WQS3b_XaP7a0bjKUY6sEl019dzvKo8849-O_xEYFmbegPYeT75pb1E-ckBCTjWM8XujLLCYAFx-dBsSEpH_4quzHl5jKl2Iu0lkYCqYKXomooCtvqTS2opFY0pDQnBmNZxMiyccXn4Hm-RWbf5HIdhoY8C8bETr86ak86BuusKJCmmjkbVEl7x8RAvqOipV-iE0J_kX7UI_DXmj3-InzBi0jJe8fDMaUR0vAZYTJdq0t-RJmzpRu5TRCj6XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سوخت رسان KC3 بریتانیا برفراز عراق
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/alonews/123401" target="_blank">📅 00:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123400">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚀
مصرف بالا؟ حجم‌خوری زیاد؟ اینو ببین
👇
💎
همراه با ساب یعنی مصرف بهینه‌تر و تجربه بهتر
⚡️
🚀
سرعت عالی پایدار برای استفاده روزانه و بلند مدت
😍
😍
@NetAazaadBot @NetAazaadBot
😍
آف فقط برای امشب
😍
❌
گیگی 50T
❌
✅
فقط گیگی 25T
✅
@NetAazaadBot  @NetAazaadBot
🔥
یه…</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/alonews/123400" target="_blank">📅 00:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123399">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/exZ7pdm81wXZAzSD1ib78pZSEqZEAUnn5fZqpg2oAbFYPY7NycT-G0Ykjcf9s3wlwD1ojIkEibgvYsmdxL2A6Ej0GvV6LybXE84YiCx9ui2p7yS0xo5RqD8y12X3enDaB5_vWb_q8lrGL03Z8f9HAMPpXD-CL0RXsUux5bz4XjfbXYRMMFV2xNfVmlrTJI-LMqbXSS9RjNmaBN6qRskq1WRJa102J1_66uD0PWK8qbj05qBJx_JmXwWvF8DLTNU7DK5bX-KOY9yg5qOn8mnQ41KY9T7aJoh9XhzK10ip4981DWnCHcad1TV6iRZ7_qI6Mqhf28hnKWRUYKOLw1SsCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
مصرف بالا؟ حجم‌خوری زیاد؟ اینو ببین
👇
💎
همراه با ساب
یعنی مصرف بهینه‌تر و تجربه بهتر
⚡️
🚀
سرعت عالی پایدار برای استفاده روزانه و بلند مدت
😍
😍
@NetAazaadBot
@NetAazaadBot
😍
آف فقط برای امشب
😍
❌
گیگی 50T
❌
✅
فقط
گیگی 25T
✅
@NetAazaadBot
@NetAazaadBot
🔥
یه بار امتحان کن، خودت تفاوتشو حس می‌کنی
✅</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/alonews/123399" target="_blank">📅 00:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123396">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EEp1u0R36OyR6SNTvbZlzaQnTpXX68P9xCekDld9Dc3wksVvZMra401tFvGnITvsDkVIZ-GA7UzWY1_jcu05ZsOZOzrfZj6PWsn1ATsSbfcFFxT-0E6ysNK1mV7h5Nv-tfFb2S0WG763pCPOPOVkUo0LsDlsXj-7SEsR3mdG_hSnMWutkpE797rFylcdWIrzD-Klx0CWPftywK_Em52IAZnW8RTmk7m8bUff_4HpPiPCtFzBNXmbzmaXUurykIlsidtVhYilpZ5aj6rIgntJGiu6HwnAOCpS-x-0AF7yMqiS8By3bksa0NPst3MZR6cks4mT2Y4LVvfB0p63RPQ8MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یواش یواش برخی از اکانتهای امنیتی حذف جانشین سردار تنگسیری را دارن تایید میکنند در حمله دیشب آمریکا به بندرعباس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/123396" target="_blank">📅 00:28 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123395">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SaULWOYHLU_IzG-myjgeS2GjS4JyPLkSxmxQ75AnsRv_LYNiRUchUvxOYvTcQbdMBzo2ZkRrWooyItYed8Ni_fIKsAATtKd43p8Efxtq4bkb89-Mx811KgDWrCAYinlEAsxefFtvoV7OYdwFNUmI55bL5Ex3EBfDPfT79MUJVvkFIi9jiGyzr2cxqr_LJJZb8Im5ip-IpccIZDVp6c0OwIe0DBr5oI70fvaUC6iegIJ793LQFwDgv7sBPGOWG3TSY3SKO2nqdZdbbjBJQQUvyOKVNFx-48atNik3dCAcWKhBJznDMh12Rz0ddeqNTwNowcG7_S-NupMsBuPUz9Eyfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
90 روز از ترور علی خامنه‌ای رهبر پیشین جمهوری اسلامی گذشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/alonews/123395" target="_blank">📅 00:14 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123394">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/695242755a.mp4?token=a02YECsEilmHelM-KmQnz24DRzc5KujPmUQyZAFWhkEjo2lbxc-6E0jKcg_mzCcQsImANxt7HeuEX1teoX61Xx0o6WHV6zxBMwR9dTXwsSKJxSSeUIzHMrNAVhB6TwVhlfd3gat-Kq015ZfE8zGbgW6-3NIADisDDkqdmcpEJDc6Z8taEhSs-tXl0cyWVk11Xrnm0Ndns6i5vuPu4DujtC2dtrbo5xx5FIjP19sWjUiY_M3gd9dM1uHCcad9YGyC9ZPnD_KyRkWY3mqZo5dPiRa0_rcNAGezGcYygfMKtHFkHCC-pWUJYmBEuij-JmE0Q91ElVpaw_MxS7UqLotzhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/695242755a.mp4?token=a02YECsEilmHelM-KmQnz24DRzc5KujPmUQyZAFWhkEjo2lbxc-6E0jKcg_mzCcQsImANxt7HeuEX1teoX61Xx0o6WHV6zxBMwR9dTXwsSKJxSSeUIzHMrNAVhB6TwVhlfd3gat-Kq015ZfE8zGbgW6-3NIADisDDkqdmcpEJDc6Z8taEhSs-tXl0cyWVk11Xrnm0Ndns6i5vuPu4DujtC2dtrbo5xx5FIjP19sWjUiY_M3gd9dM1uHCcad9YGyC9ZPnD_KyRkWY3mqZo5dPiRa0_rcNAGezGcYygfMKtHFkHCC-pWUJYmBEuij-JmE0Q91ElVpaw_MxS7UqLotzhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه حمله به شرکت آسا پنجره کاشان، تصاویر از دوربین‌های مداربسته گرفته شده است
🔴
در حمله دوم که با شدت بیشتری انجام گرفت هیچ تصاویری موجود نیست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/alonews/123394" target="_blank">📅 00:06 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123390">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j6qFNNtSYh79U4u7YvJHtGB4q0lbPXIw0J2NkRswinlSLIEjzscjQSPlsVQMIZzh7wHSD7yeDOd6QqwM_hZ39cO36kW8X2we1S-DFXXJ1SWcVI9NZAQIwtfQegWpOsmZx_u3v8uSGKsUf3rRt0bHM2nvCHD0FaBbEHRZ8StiOfnIeXJOkik87kAjJAem44c8bzNsX6H-4v3RKKZLgv5d3YXF_iNLDgbKck4K5g8_E1jevQgJMPCkeoHe6phOMOQn0heTTlQQeyOGVLPP1NbNCBYPcyR5P_OfLxNfRNw3owtgkGk7JWqlGJed8xjvvEVe3Wfrlh3zDgqpQxIZo14enw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/se42T3PPrpb_J-mIyJlxB9DG_URW31-yM6YLQtAS7IYV17_9f3-9i8sI8yWq0mqfvlNOiq6TfWRaMJYUf-5ZUYG4vQOb5FVH6TD51dQa56iFihRlNrr1ftVtH0YzgJ4Lut7t-Oly8VCO2kd5d_5PEuPsr2wzTbSSwOWAC7IJMKK_5mjT0-I_EY63Af-yEUnTdouB2WIpsN3BcwQoRl5x6yF_Me3BdNy5OZZc9rsZd3rSYkLjcvdrS4Icrxwf22IjHTKs46fxGoMRbSBSykSGFoFotMDB4VRxUcDuVeWciTc9juKST6L7d4BQNEivMfKgoiiYSl7HVx9VCbJ1LQ3FCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cDrVFylalz8KwN8o-J5IxkdP6fxKhcOHa8VEpgOaoKul3ZNYMLx0b3g9kOJMM0o_k2ndsC_UKK-8SDacYXT8dhB16rMBD4w2btFQIG9Fei5BOyQIvE8lermSjbMflGM4_QgLGwNsWG6nusOE58uKOQP5wbbqhcufV-5KkX7WE5YWgfrxT-vpjzqv-1ONtCR_e-5v7BtFN3hSyWXO11Z7DoTTjALDNR79J24HeCEg_yHB4t5nsAT7RK1jMSV1PuGFc9_mPpkAwXkfU2a-w1xTESvVRKr5dR2RvB6kAasaWuEfivEfPFPg9f1I7SW1pTm99FOFeL23xGdynMA29ht3PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EqAynM5omnJ4Iyio5OUq0Y4_DUXclrUMcsmApG8zhho3jaNiZ5qKCxQI8houlR6AbfCLFCneUeAQKe6yqfZegxNbWkFwz1Q6eEjjSlcbdhSuntfqWVHxgHw6Yaccu8s-zBFjaZS2axdhwyLG-yi2PUwR1lCwT_9gIdBCRKbPMo4P98wKT6JcE9QMrdGeOAgG-j_i6yMJs_oUVRifwVbwqUa35NOZmH4Rc7uFgWh-y9_NSuYY548uWLqrFKKbyFn1AzGq_Vnz_5idlPGiy-TVZgfRFrcVrxcq38BnjYPbkxkjdicKJJaHOLXp94FsH41jJnWA35ZeWnidmHD5vGMwQw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این وسط «صابر ابر» برند خودش رو با شعار زیست پنهان راه اندازی کرده.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/123390" target="_blank">📅 00:01 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123389">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
مهر: نیروهای مسلح ایران در نزدیکی تنگه هرمز به چهار شناور خاطی شلیک اخطار انجام دادند، این شناورها قصد عبور بدون هماهنگی از تنگه هرمز را داشتند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/alonews/123389" target="_blank">📅 23:54 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123388">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">⭕️
⭕️
این روزها بعضی از سلبریتی‌ها، چه از روی فشار نهادهای امنیتی و چه از روی منفعت‌طلبی و ترس، شروع کرده‌اند به تخریب انقلاب شیر و خورشید.
🔴
بعضی‌ها هم تازه رنگ عوض کرده‌اند و می‌خواهند با حاشیه‌سازی، مسیر اصلی را کمرنگ کنند.
🔴
بهترین پاسخ، درگیر شدن با حاشیه‌هایشان…</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/alonews/123388" target="_blank">📅 23:54 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123387">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1800a0dd05.mp4?token=BTrANfoUHm4EXRyPe1iyeOpyCg17wVYQvqgycOPwhV28ZOpaSxpwvrDXxYjk-eg5iwBwZ2kR8NsR99zGYJhRDDzzwNk11dFCDuoSNdUw1D4k7QO82CctUuDDhn9j0FrBh9NgqWO7T2xwHS1_M2BAJTYJB5jVv6d97xoMS2NRy3AfJRZfStLIBeMVU74Z77rF54ZWNs2TzZCRimgic7HFNXOEhGNrpCMtN2eQYiJ71UjD5tsJpmf31oW_9kth7LAIaqp1FQ1NMbTO_uwbg_e6e9917oKCZ-JAlz-733qmHMs9VM7lcqRQhbdohJ07o-BfbV0tf60qU8B2Ac_DhZTj_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1800a0dd05.mp4?token=BTrANfoUHm4EXRyPe1iyeOpyCg17wVYQvqgycOPwhV28ZOpaSxpwvrDXxYjk-eg5iwBwZ2kR8NsR99zGYJhRDDzzwNk11dFCDuoSNdUw1D4k7QO82CctUuDDhn9j0FrBh9NgqWO7T2xwHS1_M2BAJTYJB5jVv6d97xoMS2NRy3AfJRZfStLIBeMVU74Z77rF54ZWNs2TzZCRimgic7HFNXOEhGNrpCMtN2eQYiJ71UjD5tsJpmf31oW_9kth7LAIaqp1FQ1NMbTO_uwbg_e6e9917oKCZ-JAlz-733qmHMs9VM7lcqRQhbdohJ07o-BfbV0tf60qU8B2Ac_DhZTj_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: آنها مذاکره‌کنندگان بسیار خوبی هستند — آنها زیرک‌اند — اما ما همه کارت‌ها را در دست داریم، چون آنها را از نظر نظامی شکست داده‌ایم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/alonews/123387" target="_blank">📅 23:49 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123386">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a4e1909ff.mp4?token=YK1LLfjiC04hifrbGl_83MaITDpDvfCeoRN7S68JD_b23oMuqI_5jPFIpOdC8mWpLOq5EGEq-qzFXX2ZGXKwCZAwMyJzZ4F5TY4UWrSDnm6cWkvCVeoP_JCLnZmZF_UEQuxNkTo7m_BpqErJQWDbjJevDaxq2VJVxltR-LTcHJz5TmA7f86mmRliEh1EMjE1kJr1O7jhYdz58Gj3wiP9Em-EACGHnR1t8jjf6m-pKZukGnz_r9KZJ5aYWLGMFn7qhq3qbGdMFHLiKpOJkgz1wnthDUUfN1YmwIbfW3Na3o0OR1XHwKkOzLSIoGXNeMjSNoav7Vr0XM_vWGCx7kZ6IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a4e1909ff.mp4?token=YK1LLfjiC04hifrbGl_83MaITDpDvfCeoRN7S68JD_b23oMuqI_5jPFIpOdC8mWpLOq5EGEq-qzFXX2ZGXKwCZAwMyJzZ4F5TY4UWrSDnm6cWkvCVeoP_JCLnZmZF_UEQuxNkTo7m_BpqErJQWDbjJevDaxq2VJVxltR-LTcHJz5TmA7f86mmRliEh1EMjE1kJr1O7jhYdz58Gj3wiP9Em-EACGHnR1t8jjf6m-pKZukGnz_r9KZJ5aYWLGMFn7qhq3qbGdMFHLiKpOJkgz1wnthDUUfN1YmwIbfW3Na3o0OR1XHwKkOzLSIoGXNeMjSNoav7Vr0XM_vWGCx7kZ6IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم اکنون حملات سنگین هوایی اسرائیل به غزه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/123386" target="_blank">📅 23:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123385">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
تسنیم: گزارش منابع محلی حاکیست که منشا صداهایی که شنیده شده به درگیری‌های نظامی در دریا برمی‌گردد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/123385" target="_blank">📅 23:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123384">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QDZNmO3GQJX5KjfZqA4L3Q3NnceOdXQda3voAfGFmgs0A4uuBP505hBVeS9LtUcizKltwsEBJbqtUDJePPhijbggDTk05EkcrFYwfgxTBprObHsDCcOOH5Itk3PuslWgJYPWUA6Lzeq1Gk-iTMYd0wfhfF5cU2K3ALUCVE2C9lf7IkfKGo1McKpmwud13mYHQwzm5mmejvUm596c6eAsUMBgPCaVoqyKzVlYCtwy1WcSGoOW9hYsMMVbhqaZMnxhKgfVNLlHIEqB7GiWAPijrHDzC4j3QV0NjHwdZzxeIy8ylsAx9SkDBG20avdSxXIm4HKUYCCo19XnfrBHydciTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🏆
به دنیای هیجان‌انگیز فوتبال خوش اومدی!
⭐️
اینجا قراره باهم لحظه‌به‌لحظه‌ی جام جهانی رو زندگی کنیم؛
از بازی‌های حساس و نتایج داغ گرفته تا حاشیه‌ها، کری‌خونی‌ها و اتفاقاتی که همه درباره‌ش حرف میزنن!
🔥
🔥
✅
پوشش کامل مسابقات
💀
ترول تیم‌ها و بازیکن‌ها
🎥
ویدیوها و لحظه‌های فان فوتبالی
📊
آمار، ترکیب‌ها و اخبار فوری
🌍
حواشی جذاب از سراسر جام جهانی
📢
اینجا فقط یک کانال خبری نیست؛
یک جمع فوتبالیه برای کسایی که فوتبال رو با هیجان، شوخی و احساس واقعی دنبال میکنن
📛
💟
🆘
🔞
آماده باش چون قراره جام جهانی رو متفاوت تجربه کنیم!
⚡
@Vaarzesh_Plus
⚡
@Vaarzesh_Plus</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/alonews/123384" target="_blank">📅 23:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123383">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
تسنیم: گزارش منابع محلی حاکیست که منشا صداهایی که شنیده شده به درگیری‌های نظامی در دریا برمی‌گردد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/alonews/123383" target="_blank">📅 23:38 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123382">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
خبرگزاری فارس : دقایقی پیش ایران از جنوب کشور چند موشک به سمت اهداف مشخص شلیک کرد
🔴
هنوز مقصد دقیقشون معلوم نیست ولی احتمال درگیری تو خلیج فارس مطرح شده
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/123382" target="_blank">📅 23:30 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123381">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
خبرگزاری فارس : دقایقی پیش ایران از جنوب کشور چند موشک به سمت اهداف مشخص شلیک کرد
🔴
هنوز مقصد دقیقشون معلوم نیست ولی احتمال درگیری تو خلیج فارس مطرح شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/123381" target="_blank">📅 23:30 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123380">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IpiaWW-ysj__2qj20Txe81AcXBbz42qlVVtxeE9UUlQs2fvnYzXJ9vGWoLLYPfFJ2d_Hq8L1T_wr_2_ieK5oCpn7WzMYuvuEnUmStxbm7oG9Py_AFkAzUyOKLoRlGA66sUaaU05XHEgv_wtBpHT_72nxc02O7sxMpMT2mhzJaj3ixWV3VMpT8kHi2No49_d92VjS9HkWhBWUxu5aiJyOhSPLyPavA5_Tg243zf7TezBurpiHIZirXtmUyv3GunebAEH4RuxuJoB07XySdJUgyh0M3Yx2kHY0PqUmk1_AFUj6IKMoZ2ADt9VbnTNSl94YPL4QNfvtObRfmWpgC6zMgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از اسکناس ۲۵۰ دلاری با تصویر دونالد ترامپ که در صورت تصویب کنگره چاپ خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/123380" target="_blank">📅 23:08 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123379">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
فوری / هرمزگان و بوشهر صدای چند انفجار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/123379" target="_blank">📅 23:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123378">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
جوان ۲۰ ساله دزفولی، به دلیل اختلافات خانوادگی با سلاح سرد پدر، مادر و برادر خود را به قتل رساند و سپس خود را از کوه به پایین پرتاب کرد و به زندگی خود پایان داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/alonews/123378" target="_blank">📅 22:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123377">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
وزارت بهداشت لبنان گزارش می‌دهد که از آغاز دور فعلی درگیری‌ها، ۳۲۴۳ نفر کشته و ۱۰۲۷ نفر زخمی شده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/alonews/123377" target="_blank">📅 22:51 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123376">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b58cf68a4.mp4?token=uwk9WXjZUGgr-h52vqPFNNRPyfvybRWwC6_ht6PRTUaAo1VD4ZBFdxUAeLIGjHZoXRefQNNOrEF-9ruo7BqjRaEwJT8Jx8v9dM9JhTErvgSG0l7_q5BGpi3fMA2jcHfhVExOx6wq7pN7FyLkrlYUtL9WQNdC1z0L53pV0V5OYnnNUtAc2v-dje7Qa7Qkw7u6qNe0VQKO1ecSsG23w0ndKvJUOLGEp9Yeim3NPG-BcJLgvDvjlOZChpQzm5Imw-Oy6BKyJbSr57mESkzzo1_ladmHCRU8_F26pZjj5SjZVCMS6MA74JtvsYq9l11FWrGNmOtwEvuaAQIg-l4WUrdDnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b58cf68a4.mp4?token=uwk9WXjZUGgr-h52vqPFNNRPyfvybRWwC6_ht6PRTUaAo1VD4ZBFdxUAeLIGjHZoXRefQNNOrEF-9ruo7BqjRaEwJT8Jx8v9dM9JhTErvgSG0l7_q5BGpi3fMA2jcHfhVExOx6wq7pN7FyLkrlYUtL9WQNdC1z0L53pV0V5OYnnNUtAc2v-dje7Qa7Qkw7u6qNe0VQKO1ecSsG23w0ndKvJUOLGEp9Yeim3NPG-BcJLgvDvjlOZChpQzm5Imw-Oy6BKyJbSr57mESkzzo1_ladmHCRU8_F26pZjj5SjZVCMS6MA74JtvsYq9l11FWrGNmOtwEvuaAQIg-l4WUrdDnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حاجی بابایی، نایب‌رئیس مجلس : ایران ابرقدرت شده و همین کار مجلس رو سخت‌تر کرده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/alonews/123376" target="_blank">📅 22:47 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123375">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
هگستث: به لطف سرمایه‌گذاری نظامی تاریخی ۱.۵ تریلیون دلاری رئیس‌جمهور ترامپ، سربازان ما بزرگ‌ترین افزایش حقوق در تاریخ مدرن را دریافت خواهند کرد.
🔴
ما همچنین سرمایه‌گذاری نسلی در خوابگاه‌ها، زیرساخت‌های نظامی و سیستم‌های پشتیبانی سربازان انجام می‌دهیم.
🔴
آمریکا اول = سربازان اول
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/alonews/123375" target="_blank">📅 22:37 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123374">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V0q5wfALpgEyIXRcUoszd2YJB2TKroi57GQXIE0dix5guyC2B7hFIYygeroYUtw7c7j6OMyNC_u9FfSt269Yp8QfqkcBZ5dKhTJfOy7x8XiFG5VPXnSIr7dTZ0A9qdjVqPGX5VLd5mflFdo5FVG3wrpnepq6E90pfDe31XSPUxQIf_3SXmg7UqcrKhOiYX13b29t2cFzfs8HbiSJAylDTjOw9yRv_FfvqhZUInBrT6DbcrDVSvjlO5pjhG5nMCpWfxp1KPk-QbVGmRJ5oTS3KWVBeydU3vra0h7vAIB-WOee-gYMK4qIBA0X90U6uaaGPNm6QGhS2QjFaFxIJMxwrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آتلانتیک
:
«قیمت نفت پایین است زیرا سرمایه‌ گذاران انتظار دارند ترامپ قبل از اینکه قیمت‌ها خیلی بالا بروند، به جنگ پایان دهد.»
🔴
اما از آنجا که قیمت‌ها پایین است، ترامپ با فشار کمتری برای پایان دادن به جنگ مواجه است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/123374" target="_blank">📅 22:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123373">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b25dad216.mp4?token=N0VT0XMyGG1SKTAGGox-gmR-3Vd5VqtoU1oEYihUKgXG_zAL6pk_3v2MUsVPc6PKwxNPEADXvq_fS0WQQeATKOT3chQTl_hDdrlEzSKHLVAmpTiGe1t67sARelfpVDN53jul9senw-vhzmjDo0IX97mK39hkZdWrAYx4-fKtICHWnNVLINr9BHN7RHzCvwV-f5XP9m1VXaahaHgFcrNPurOTIraUPD7fKRYJcWwLkFtfm3Kt-fL8KCISfJKoKuzybD1DCGxPDFY2R4p-CZ9RCnXrMQeiAA2KAUXalhOdbfiyaD2K0rJYv0Wgqm9Nyt3CUXKXgAKYL9Ma9x-79xPyvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b25dad216.mp4?token=N0VT0XMyGG1SKTAGGox-gmR-3Vd5VqtoU1oEYihUKgXG_zAL6pk_3v2MUsVPc6PKwxNPEADXvq_fS0WQQeATKOT3chQTl_hDdrlEzSKHLVAmpTiGe1t67sARelfpVDN53jul9senw-vhzmjDo0IX97mK39hkZdWrAYx4-fKtICHWnNVLINr9BHN7RHzCvwV-f5XP9m1VXaahaHgFcrNPurOTIraUPD7fKRYJcWwLkFtfm3Kt-fL8KCISfJKoKuzybD1DCGxPDFY2R4p-CZ9RCnXrMQeiAA2KAUXalhOdbfiyaD2K0rJYv0Wgqm9Nyt3CUXKXgAKYL9Ma9x-79xPyvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر خزانه داری اسکات بسنت: هیچ‌کس به اندازه دولت ترامپ تحریم‌های بیشتری علیه نفت روسیه اعمال نکرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/123373" target="_blank">📅 22:23 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123372">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b334f5701.mp4?token=vUAN-_XL-AByx8ijUJS_vAD6YWD2XfkcQqnvHFjg_3msra5SyH-8jVLKfU1EYlKTtXjYBi6a6sKKarussMr-pyAzggtCNat3Ra8iS5j-c6EsNrVNFI9sk6XUWCA-_5KzVrdne52UCCdz7SCI93f2M9z947gKiTwzkmIQn3Jkov8Y_rl5oWtHJ8K4wIU5YD90hAes7yhZj1Rq5wdn0452si5cz9Ngv5RGQDpSWjpxGnTgHI4JJIS_xZCJYADIBo6nj-yAtyjDlNnumTRFb7n0SXr-TVI-YE_TuM1fucAZBzN59EdTHLo-oIrsX4jGifQHSLQFAZcViW0kn3MbuVmYew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b334f5701.mp4?token=vUAN-_XL-AByx8ijUJS_vAD6YWD2XfkcQqnvHFjg_3msra5SyH-8jVLKfU1EYlKTtXjYBi6a6sKKarussMr-pyAzggtCNat3Ra8iS5j-c6EsNrVNFI9sk6XUWCA-_5KzVrdne52UCCdz7SCI93f2M9z947gKiTwzkmIQn3Jkov8Y_rl5oWtHJ8K4wIU5YD90hAes7yhZj1Rq5wdn0452si5cz9Ngv5RGQDpSWjpxGnTgHI4JJIS_xZCJYADIBo6nj-yAtyjDlNnumTRFb7n0SXr-TVI-YE_TuM1fucAZBzN59EdTHLo-oIrsX4jGifQHSLQFAZcViW0kn3MbuVmYew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر خزانه داری اسکات بسنت: اقتصاد در حال حاضر چالش برانگیز است، اما بیکاری هنوز کم است، بازپرداخت مالیات بالا بود، و هزینه های مصرف کننده هنوز بسیار بالاست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/123372" target="_blank">📅 22:23 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123371">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86a941d630.mp4?token=MgPGrdXx3kbtNQXXlh5sm4l2jyAlVBdAFTBY2G_zcL1CumGCY_nSAqMvahICR85ytGf7SeTq9z6z3ijmsg0QP0NX7gme9P8ILh0vMIfQq31VTOyL29oVYOhkykWgAFQGAfPKKCm7348CjZ5KXEm090n3qOqFumh0t5QHwMpKsfX4SCPR370XiHVqnLEhZzZx14lUCrFTJWC76GFLPGKmaO4k6DxaGwhsMiFE8FtSIlBaG-KGDrZq69ndiNWUSERP0-EDCkzW65AJMnovYme1blqzUfKklAdzSW8rd87VnSSEusvaphDlvauAKCms_uwVg71J7XGlv73aVGMj19e-NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86a941d630.mp4?token=MgPGrdXx3kbtNQXXlh5sm4l2jyAlVBdAFTBY2G_zcL1CumGCY_nSAqMvahICR85ytGf7SeTq9z6z3ijmsg0QP0NX7gme9P8ILh0vMIfQq31VTOyL29oVYOhkykWgAFQGAfPKKCm7348CjZ5KXEm090n3qOqFumh0t5QHwMpKsfX4SCPR370XiHVqnLEhZzZx14lUCrFTJWC76GFLPGKmaO4k6DxaGwhsMiFE8FtSIlBaG-KGDrZq69ndiNWUSERP0-EDCkzW65AJMnovYme1blqzUfKklAdzSW8rd87VnSSEusvaphDlvauAKCms_uwVg71J7XGlv73aVGMj19e-NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار : آمریکا به پهپادهای ایران حمله کرده و سنتکام هم گفته ایران آتش‌بس رو نقض کرده، پس چطور هنوز می‌گن آتش‌بس هست؟
🔴
بِسِنت : ما داریم فعلاً صبر می‌کنیم، ولی اگه رئیس‌جمهور ببینه توافق صلح درنمیاد، دوباره گزینه نظامی میاد وسط
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/alonews/123371" target="_blank">📅 22:22 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123370">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43a0f72629.mp4?token=EujmSb2Xe1odE6wMv_GX6UBN2lT3-5NovX5w61CZJ21G0HWa_js-tC8t_4yaXUQ6msxjFpT2N2JdieRifeWQ3uarNlOaxZT_ZLKj3VhNHScjfHwoJEFi6c7hoVoEKMoo694T4wvyYxyDD-Q6B05Tfbmi1Jb7iP_5FnxJKNYjw33RCOLSyYMCS4MKxhWB3u69qyHI0FFKxnsHEldSK2IGqV3BfAHm7XwrdzG8eHEo0pDoCkCTSvaeyU4Qa8wuRoTRQ5TSgPvj0JHrXqCWrmn2MNn5uPx2CdoLVNB5I8hhduOl5axCZ54woD3x3nWabojAPoZ3vwU7gb3bFezZx1aAEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43a0f72629.mp4?token=EujmSb2Xe1odE6wMv_GX6UBN2lT3-5NovX5w61CZJ21G0HWa_js-tC8t_4yaXUQ6msxjFpT2N2JdieRifeWQ3uarNlOaxZT_ZLKj3VhNHScjfHwoJEFi6c7hoVoEKMoo694T4wvyYxyDD-Q6B05Tfbmi1Jb7iP_5FnxJKNYjw33RCOLSyYMCS4MKxhWB3u69qyHI0FFKxnsHEldSK2IGqV3BfAHm7XwrdzG8eHEo0pDoCkCTSvaeyU4Qa8wuRoTRQ5TSgPvj0JHrXqCWrmn2MNn5uPx2CdoLVNB5I8hhduOl5axCZ54woD3x3nWabojAPoZ3vwU7gb3bFezZx1aAEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: آیا لغو تحریم‌ها برای ایران در دستور کار است؟
🔴
وزیر خزانه‌داری آمریکا: هیچ چیزی روی میز نخواهد بود تا زمانی که تنگه هرمز باز شود و ایرانی‌ها موافقت کنند که اورانیوم بسیار غنی‌شده را تحویل دهند و نتوانند برنامه هسته‌ای داشته باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/alonews/123370" target="_blank">📅 22:18 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123369">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a2e821515.mp4?token=NIIye7CX4_iVT6i09DsMU52EaDJur_GQxFPolBg6IJMbNsEkXquJviAL9L0wCVJ81KHzjqF3auhlk4vHM6LJZP41o9dgA3DRl1HzZ6pdW_Jv7wYo0QVNIlq9UWeuZDtERQqBgHJ_PV_D183IfPhYSwx5yW4H7oSf57j6amFVzknPVABYv9SHuYodptiJ1PpBJhEoZdpnogiHLrKrBnx_JyP0TJNLatTQomlPoL1FD0suY_9ZYTtVPubBrdbFq7KNOI3-L81mrLbTaxMOZV40sSTSo03v4WC9Z6E19te1bR8oyDUfJGarvx05p-frIxKO_8LXHNyegGT00jtrYrC1Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a2e821515.mp4?token=NIIye7CX4_iVT6i09DsMU52EaDJur_GQxFPolBg6IJMbNsEkXquJviAL9L0wCVJ81KHzjqF3auhlk4vHM6LJZP41o9dgA3DRl1HzZ6pdW_Jv7wYo0QVNIlq9UWeuZDtERQqBgHJ_PV_D183IfPhYSwx5yW4H7oSf57j6amFVzknPVABYv9SHuYodptiJ1PpBJhEoZdpnogiHLrKrBnx_JyP0TJNLatTQomlPoL1FD0suY_9ZYTtVPubBrdbFq7KNOI3-L81mrLbTaxMOZV40sSTSo03v4WC9Z6E19te1bR8oyDUfJGarvx05p-frIxKO_8LXHNyegGT00jtrYrC1Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر خزانه داری آمریکا اسکات بسنت درباره رژيم جمهوري اسلامي ایران:
ما تغییر رژیم نداشتیم، اما رژیم را تغییر دادیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/123369" target="_blank">📅 22:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123368">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe01c7dc63.mp4?token=J6lJ7vR3C1Cy3ZOSeH3MpvE9H90CiOhYFhEE6JqH4adWqXl4M57MXxTcMA9dwbhEdnhOGDbd1FBGmMQ4MHHSkXN7O1qoLSEJmDCKvZ_U-vdUg_iNXCCCq1_2Ux31rZf-ePZNB0f66gO8XA4fblfxf46tu-MsI13JBWtgaA29GQ2h5aDoVC81LQZSz2k0n982eFffiMsVQcryT1XxN9OrdBnH0kej-dTlIrPJhGkB6MRjZQ-y8Se_P8Zqbk5UUY-GywEyfaLYiD83No7JERpl7YpCIHHjbeof1O4bILq_UIZlYYQemlExNSlYRBxdP4ftsCJmLUFiz22mYnWmXRwuYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe01c7dc63.mp4?token=J6lJ7vR3C1Cy3ZOSeH3MpvE9H90CiOhYFhEE6JqH4adWqXl4M57MXxTcMA9dwbhEdnhOGDbd1FBGmMQ4MHHSkXN7O1qoLSEJmDCKvZ_U-vdUg_iNXCCCq1_2Ux31rZf-ePZNB0f66gO8XA4fblfxf46tu-MsI13JBWtgaA29GQ2h5aDoVC81LQZSz2k0n982eFffiMsVQcryT1XxN9OrdBnH0kej-dTlIrPJhGkB6MRjZQ-y8Se_P8Zqbk5UUY-GywEyfaLYiD83No7JERpl7YpCIHHjbeof1O4bILq_UIZlYYQemlExNSlYRBxdP4ftsCJmLUFiz22mYnWmXRwuYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار : آیا تمدید موقت ۶۰ روزه آتش‌بس و ادامه مذاکرات هسته‌ای درحال حال بررسیه؟
🔴
بِسِنت : رئیس‌جمهور خیلی واضح گفته،تنگه هرمز باید باز شه
- اورانیوم بسیار غنی‌شده باید تحویل داده شه، و برنامه هسته‌ای نباید وجود داشته باشه
🔴
خبرنگار : آیا این سه مورد داخل توافق هست؟
🔴
بِسِنت :
- اگه بدون این موارد اصلاً توافقی وجود نداره، پس چرا باید توافقی بدون آن‌ها باشه؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/alonews/123368" target="_blank">📅 22:13 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123367">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3ec88d54d.mp4?token=nACLzz-89yU0lRjp9_m20Zwpjg8mjHZ8qC9LdvtjA43W_ozdr6KmnsrIG8T2FCHwmTyc8fspHV6gpZRjURciwWbhyXf7WpbYjRrt4TjN3CZdC9hhM-zDk4AmjatfB-lq7lBBZSPIbPitvhS4GfsbnveH_Tt_XQioqe_H7C41OOCF-7s1K3x5W40VE_vQAoOTF0y36ktkv-cy38xV7fiIXo0PCEGqqkUk0muwGipc_L05YOBptvTakXZ2dBzbhVYtyM5rjVrKipZXj8IsANk34QQcJhWFX4ahUmxq5GbmMa9g9LHLkQIIuJYnfORIQzf9QlsmM1aTVtL7Ec2sH2q-rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3ec88d54d.mp4?token=nACLzz-89yU0lRjp9_m20Zwpjg8mjHZ8qC9LdvtjA43W_ozdr6KmnsrIG8T2FCHwmTyc8fspHV6gpZRjURciwWbhyXf7WpbYjRrt4TjN3CZdC9hhM-zDk4AmjatfB-lq7lBBZSPIbPitvhS4GfsbnveH_Tt_XQioqe_H7C41OOCF-7s1K3x5W40VE_vQAoOTF0y36ktkv-cy38xV7fiIXo0PCEGqqkUk0muwGipc_L05YOBptvTakXZ2dBzbhVYtyM5rjVrKipZXj8IsANk34QQcJhWFX4ahUmxq5GbmMa9g9LHLkQIIuJYnfORIQzf9QlsmM1aTVtL7Ec2sH2q-rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار : ترامپ تهدید کرده عمان رو «بمباران» کنه. شما دارید برای جنگ جدید با عمان برنامه‌ریزی می‌کنید؟
🔴
بِسِنت : فکر می‌کنم رئیس‌جمهور می‌خواست بر اهمیت آزادی کشتیرانی تو تنگه تأکید کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/alonews/123367" target="_blank">📅 22:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123366">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/symzkqXVElWGMj6z3j5JaRCjxwPA62AjQmMzZQUnhSv8mHKXHvMMf-KnpdzN2q9vufB4hSr8kC1Up6Fxq4POdhTalqqps8ioRwt6mWz1lpjIgslicpmd7fF75Vn4o9Fyi-mfar4ZhgX8D4lLBXymX9uS1sODwPLLk8ngbnCapfw8TYOuQB_REAOK8L_6zEOc5IrdBZqxMAd_4AS5Gw8h-ZVJ3USeCMZjnxy3y9BvtFjJC00foTV_qam2Hh78fQv4E3Svv4wGoCP4M3H9WDtgE3BAaLC_lR3IcRnj8e8PCqIzKV6BCZiwDWz0K4oSlGX8NeJnNIBiqiA5Qs6babJ-qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیریت حرفه‌ای سرمایه بدون نیاز به دانش معامله‌گری
سرمایه شما در حساب شخصی خودتان باقی می‌ماند؛
ما فقط با دسترسی محدود معاملاتی (Trading Permission) مدیریت معاملات را انجام می‌دهیم.
بدون نیاز به دانش تخصصی، تحلیل بازار یا تجربه معامله‌گری
می‌توانید از خدمات مدیریت سرمایه و کپی‌تریدینگ حرفه‌ای بهره‌مند شوید.
✔
مدیریت ریسک حرفه‌ای
✔
شفافیت کامل عملکرد
✔
تمرکز بر رشد پایدار و کنترل سرمایه
✔
بدون واریز مستقیم سرمایه به ما
❎
ضمنا میتوانید در کانال تلگرام از سیگنال های روزانه رایگان فارکس و همچنین آموزش تخصصی استفاده کنید
❎
👇
👇
👇
https://t.me/+gm6piMRKtzE5Mjk0
Investment Pulse Capital
📍
Muscat, Oman
📞
+968 93606848
📱
اینستاگرام
✈
️
کانال تلگرام
📞
واتساپ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/123366" target="_blank">📅 22:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123365">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
خبرنگار: ترامپ گفت که می‌تواند عمان را «بترکاند». آیا شما برنامه‌ای برای جنگ جدید با عمان دارید؟
🔴
بسنت، وزیر خزانه‌داری آمریکا: فکر می‌کنم ترامپ می‌خواست بر آزادی ناوبری در تنگه تأکید کند. سفیر عمان به من اطمینان داد که برنامه‌ای برای دریافت عوارض از تنگه وجود ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/alonews/123365" target="_blank">📅 22:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123364">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
یک مقام آمریکایی به الجزیره: ما تأیید می‌کنیم که ایالات متحده و ایران به یک یادداشت تفاهم در مورد تنگه هرمز و مذاکرات هسته‌ای دست یافته‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/123364" target="_blank">📅 22:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123363">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
رئیس کمیسیون امنیت ملی مجلس: تبادل پیام با آمریکا در جریان است
🔴
اگر ترامپ می‌خواهد از بن‌بست خارج شود راهی جز تن دادن به اراده ملت ایران ندارد
🔴
آمریکایی‌ها اول باید شروط پنج‌گانه ایران را بپذیرند. در این مرحله پذیرفتند اما تا الان اقدامی انجام نداده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/alonews/123363" target="_blank">📅 22:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123362">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">⭕️
⭕️
این روزها بعضی از سلبریتی‌ها، چه از روی فشار نهادهای امنیتی و چه از روی منفعت‌طلبی و ترس، شروع کرده‌اند به تخریب انقلاب شیر و خورشید.
🔴
بعضی‌ها هم تازه رنگ عوض کرده‌اند و می‌خواهند با حاشیه‌سازی، مسیر اصلی را کمرنگ کنند.
🔴
بهترین پاسخ، درگیر شدن با حاشیه‌هایشان نیست؛ آنفالو کنید، محتوایشان را نشر ندهید و برایشان تریبون نسازید.
👑
مسیر درست روشن است: ادامه دادن، متحد ماندن و نپرداختن به بازی‌های فرسایشی.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/123362" target="_blank">📅 22:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123361">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👑</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/alonews/123361" target="_blank">📅 22:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123360">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H9uZmJmxRSONIRFeRiyaMk6WZNENkxMX6lld9J_EspVnGONb_g64CMwnePjYXMbWqm5XLjz0bcg6vl-AoK4M5wcAMO0t4_IX1i-YDCtkn4hK_5tN0iqimcrqgZMvUbThb6JQdWBpluJ_Fsv1J9aozXPnlavHFUL-2yPs46fJUZhmQkOWJykYy3hz8MMrtOVR0KYaJalHyYINTZRzcY1insMJSWzVwQaW9h3VN6YUGFa1AEshnofXtoL27Gsk1YZUtyV0KzYxczJCqfdIR0LS81Apz3UjA9CnfzLbkSaT7CoRG48Q0NFiJhnfHl2LkaLfnZDq08_yjCD3luPI1QeuyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خاویر بلاس، ستون‌نویس بلومبرگ:
با قضاوت بر اساس هشدارها و تهدیدهای مستقیم کاخ سفید و وزارت خزانه‌داری آمریکا، به نظر می‌رسد
عمان واقعاً در حال بررسی پیوستن به ایران برای اجرای نوعی سیستم «عوارض» یا «هزینه عبور» در تنگه هرمز است
. این تنها توضیح برای ۲۴ ساعت حمله از سوی واشنگتن است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/alonews/123360" target="_blank">📅 22:00 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123359">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f49bb5b725.mp4?token=D19-9g9ZBzMUQDbAd10J7ZlCL0quQZuO-ht7sD3THcClNwPt9_QpXdCMQ5MQvkhqLBrE5vLfY-pKdmoZwiQq33-fdPYMbwv_znPc_m87hDm3lfcb4bO3IuXjPj5gkd7wCiUw-b-_Fd-BT9ikEwYWWRqDxjdB5M42Aj-ZsPxEly-47Lws3rY3b601cxsycLE4r8ezT_DM7iDgnOpG_RP1_kh6Dxd-ci0suV70p1S5P2WPLtXrWxg1O-kPCm3KVWNvC3pY2cF4rQ1uxSeJpcpB_iuYvd8raS7cYqJs2YW9Mjg4xainRHgugNHBmepOgs6mQRst7UGunLh1TTDLRjATbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f49bb5b725.mp4?token=D19-9g9ZBzMUQDbAd10J7ZlCL0quQZuO-ht7sD3THcClNwPt9_QpXdCMQ5MQvkhqLBrE5vLfY-pKdmoZwiQq33-fdPYMbwv_znPc_m87hDm3lfcb4bO3IuXjPj5gkd7wCiUw-b-_Fd-BT9ikEwYWWRqDxjdB5M42Aj-ZsPxEly-47Lws3rY3b601cxsycLE4r8ezT_DM7iDgnOpG_RP1_kh6Dxd-ci0suV70p1S5P2WPLtXrWxg1O-kPCm3KVWNvC3pY2cF4rQ1uxSeJpcpB_iuYvd8raS7cYqJs2YW9Mjg4xainRHgugNHBmepOgs6mQRst7UGunLh1TTDLRjATbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دولت ترامپ تولد مارکو روبیو را با یک کیک بزرگ جشن می‌گیرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/123359" target="_blank">📅 21:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123358">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
خبرگزاری CNN: ترامپ قبل از امضای تفاهم‌نامه با بنیامین نتانیاهو مشورت خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/alonews/123358" target="_blank">📅 21:51 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123357">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
مهدی کاظمیان سخنگوی منطقه آزاد انزلی گفت: در ساعت ۱۸ و ۳۰ دقیقه امروز آتش سوزی در فندرهای (ضربه گیر) لاستیکی اسکله رخ داد که با تلاش آتش نشانان این منطقه مهار شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/alonews/123357" target="_blank">📅 21:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123356">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
تسنیم: برخلاف ادعای منابع غربی، متن تفاهم‌نامه احتمالی تا این لحظه نهایی و قطعی نشده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/alonews/123356" target="_blank">📅 21:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123355">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TzX_rRNFLJmbKlsIeHJelENCUjOlR5IWeYQZnGftKGZ0IkJcZoFgkuGmdtmL8-drUcFo_2qsMSD8EIqInpNEAiqdCqS24mZgCD9rsxgm7UzIyLXVBvYK_FsJr_qDUwAwMKiB1GY2vkgiKNPe2nWPs3jEhag0fw6zg5vY3fG6M0ofZL-y4EtcOeJFbmmpibLR_FogzU1S0qBBo9s_vFRK2--TtBWUsbW6Z3Yoc9eIQVmNAA4aWcHCDPCC-DSjsMOxonOrH2KvaY03Wqb33q9S_OcC5E2SR4hms4JtO7GHgJknkEDxXteXopGdcMaw-JhitAVtmfCVaOoH_p6tHLsM1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ می‌گوید توافقی برای پایان جنگ با ایران نزدیک است، اما در مسائل کلیدی همه چیز به نقطه صفر یا حتی بدتر بازگشته است — پس از یک «فاجعه حماسی» که حداقل ۲۸ میلیارد دلار هزینه داشته، باعث ایجاد محاصره فلج‌کننده هرمز شده، عرضه جهانی انرژی را مختل کرده و احتمالاً به اعتبار ایالات متحده آسیب جبران‌ناپذیری وارد کرده است، طبق گزارش نیویورکر.
🔴
گزارش اشاره می‌کند که نکته اصلی طنزآمیز این است که این جنگ پرهزینه تنها یک سند یک صفحه‌ای بدون هیچ جزئیات فنی به بار آورده است.
🔴
بسیاری از نکات نوشته شده بی‌معنی هستند — مانند تعهد به «عدم تجاوز» که قابل تأیید یا اجرا نیست — که باعث شده درد تحمل شده برای رسیدن به این نقطه واقعاً تأسف‌بار باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/123355" target="_blank">📅 21:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123354">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IKTy31QFv-GO8FTr1_wCAdvGuzk2zm29-_0fVINhSOZlnIzL_rz9wbbc3HY650SxoaAfSTGUu1o9qPFgLt0zXXrgMNsP7W2He_Focwx4UunV4LwUziSzcpSOpQZrCdUjOs-aScRBJvteKekGDOFNkXHWdURswY-CmIZct5Bo_giMu0ldGm8YfaMBGbVAQlz_EqmPH5kpr3UArtDMlxJ5npfJ34lMcLPK03e5p5iBT1vSciS13e39SlWIBLblE8EaoyBgs7qFdKs4xzK8ZNTjFI8fbPNmF0aCBUlgqclJiDyRSC86jiNkXpaxbPkxMnT5YJUwGo0aplj-FQ1iWKG9DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زهران ممدانی شهردار نیویورک دیروز با لباس آرسنال رفته بود نماز جماعت عید قربان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/123354" target="_blank">📅 21:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123353">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
شبکه الحدث به نقل از سفیر عربستان در واشنگتن ادعا کرد: پیت هگست، وزیر جنگ آمریکا، نخست‌وزیر قطر را در تماس تلفنی به دلیل حمایت از حماس و انعطاف‌ناپذیری در قبال ایران، تهدید به ترور کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/alonews/123353" target="_blank">📅 21:36 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123352">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/acef1f161f.mp4?token=ESDkrtoRu1lHXy44H3Sa3fqJLV9vKSL4KLWjR3e2IRXcBjji_H2r1ATSPCQixd8Zlo6lSyXuADPe9ymk5QBapfM87-oeYicUa3iOXrWqp0J0xIfWmv1etjQnHqMFgkw-2ak9xoZdkAheNU9ybherWGYVfw70pEsUoGa8VcJsUpa7Z2LTfCnoDkno1T8eu6ksw0CiT005yXVdY-JmrzNUkBEbxcr3-cx8BMyuqJcfETQaV_Xt1apOh1nn6FFHmoMYsoqrsuCiQ-prCs9oYE8O1tvSPLX_zApTVHWPHAscIc9G2coDpJ1W2UmoCxZYxkMYuiUGDGEdwkRRbRpat38Obw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/acef1f161f.mp4?token=ESDkrtoRu1lHXy44H3Sa3fqJLV9vKSL4KLWjR3e2IRXcBjji_H2r1ATSPCQixd8Zlo6lSyXuADPe9ymk5QBapfM87-oeYicUa3iOXrWqp0J0xIfWmv1etjQnHqMFgkw-2ak9xoZdkAheNU9ybherWGYVfw70pEsUoGa8VcJsUpa7Z2LTfCnoDkno1T8eu6ksw0CiT005yXVdY-JmrzNUkBEbxcr3-cx8BMyuqJcfETQaV_Xt1apOh1nn6FFHmoMYsoqrsuCiQ-prCs9oYE8O1tvSPLX_zApTVHWPHAscIc9G2coDpJ1W2UmoCxZYxkMYuiUGDGEdwkRRbRpat38Obw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه نابودی پایگاه هوایی بندرعباس توسط بمب‌های فوق سنگین 2.2 تنی GBU-72 که توسط بمب افکن استراتژیک سنگین B-1B نیروی هوایی آمریکا در این حمله استفاده شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/123352" target="_blank">📅 21:31 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123351">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
سازمان ملل: در مورد تبادل آتش بین ایران و آمریکا در روزهای اخیر به شدت نگرانیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/123351" target="_blank">📅 21:30 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123350">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
شبکه ان‌بی‌سی ادعا کرد: مذاکره‌کنندگان آمریکایی و ایرانی سه روز پیش در دوحه بر سر شرایط توافق آتش‌بس به توافق رسیدند، اما هر دو طرف در اعلام نهایی آن تأخیر می‌کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/alonews/123350" target="_blank">📅 21:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123349">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y8l2KI_Grdolb0xPw9faBohPIUjLcTEyTn9PZqtCP687AE9r0FlcgZg0f_cS8Wh9TrcaH5wMbmFXuGTwemhK2hoDS9KPYOZ7a5D3QXudWrFlRFWhI3vxJziXiShaPtftbNKGEAWa-PBkVYdrJgpFd5CzV39lmK6YKugjiZmj7qUe-jshkYIMi5293M2w0zRAhXO9ReXcAMnTV7oGco8qyNvQFoQsc7lEi5korGkwi1u5sUUGD7VOfXzqY7bGyCHgTL1baswljJTGAqOWC3OqjnXc0SlxHKYBoYmNLVVZKYWlsnl79tsF8pZC-WGbZC-_RS0Xc18Zh06nLw_DqX6EOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شبکه CNN به نقل از تصاویر ماهواره‌ای: ایران با استفاده از بلدوزر و کامیون، در حال بازگشایی تأسیسات زیرزمینی موشکی و بیرون کشیدن زرادخانه عظیم خود است که ادعاهای ترامپ مبنی بر نابودی آن را زیر سؤال می‌برد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/123349" target="_blank">📅 21:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123348">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
فوری/سی‌ان‌ان: منابع آمریکایی هشدار می‌دهند که هرگونه پیشرفت در مذاکرات با ایران می‌تواند به سرعت لغو شود اگر ترامپ تصمیم بگیرد تأیید خود را بر یادداشت تفاهم پیشنهادی صادر نکند.
🔴
ترامپ به دنبال تضمین‌هایی است که هر توافقی قوی‌تر از توافق هسته‌ای دوران اوباما در سال ۲۰۱۵ که او از آن خارج شد به نظر برسد، در حالی که همچنین تحت فشار متحدان جمهوری‌خواه و نتانیاهو، برای عدم کاهش فشار بر ایران قرار دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/123348" target="_blank">📅 21:18 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123347">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
سی‌ان‌ان : ترامپ تو تلاشه قبل از تایید توافق با ایران، مشورت بگیره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/alonews/123347" target="_blank">📅 21:13 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123346">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
نخبگان عمانی در واکنش به تهدید ترامپ: عمان باج نخواهد داد، این تهدیدات نشانه قلدرمآبی و شکست ترامپ در منطقه است و ما در موضع ثابت خود در قبال جنگ علیه ایران باقی می‌مانیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/123346" target="_blank">📅 20:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123345">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
مدیرعامل شرکت ارتباطات زیرساخت:
بازگشت ترافیک بین‌الملل به دلیل طولانی شدن قطعی‌ها، چند روزی زمان می‌برد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/alonews/123345" target="_blank">📅 20:47 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123344">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
پزشکیان، رئیس‌جمهور: به دنبال سلاح هسته‌ای نیستیم و با ذلت دیپلماسی نمی‌کنیم؛ ناآرامی منطقه به خاطر اسرائیل است و حضور ۸۰ روزه مردم در صحنه، دنیا را متعجب کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/123344" target="_blank">📅 20:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123343">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fMeB1eX1lx4grzaIglNUzPvkruCVRq4kok-tgpFr3NSAhBAtUynDpoYOyipUp-PrNWVgE-GkSTJq4GTjafrNliwze-cmjljKJ7f_yFzXfIg8BNKMNRF7mVUaciHhIo-LtdoRJTIhPJ6BEFRNbvV1rh5RrzZMvWt_NIFR-izTF0yQdntbKs5QQJMEX0u1hcSXPKwuihyJaYIHq_jVekA853LYTfG3TjBv2iC8fiWcXkDeTMggu3hHIHRemPqiBO8djaJMH9n6vpnXnaYQrfwmSrwNwRqOweOsIwg3t_QRCg_UZkgSe8N9-5M39K0jwOc3-jXNCBr4GdjiamXV1PoAYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کشور های دارای سریع ترین اینترنت موبایل در جهان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/123343" target="_blank">📅 20:37 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123342">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
معاون وزیر خارجه: به هرگونه نقض آتش‌بس، پاسخ قاطعانه می‌دهیم، تا زمانی که تفاهمی در راستای منافع ملی نباشد، ایران آن را امضا نخواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/123342" target="_blank">📅 20:34 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123341">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jmwi2AFAJhfEkQkhgplwrr0DgdAAWt6ezQNCfEvuLs7o4v-8FiYQAxORH9Lv3lxDi6nlGxDPl9uNrl225Xxmns2rKtk65v5TtlpOtApXGjSfdHHu3YVnTPYBVnQd8uqvfXtLUwaQgOoiRJMWe3LrJ_urmDhq2hEC1dhMYcNwxU008GllCCG6UiTof8EWNGOISDLqfnKJO-bf3Mp1hGl4DXNKZGO9YWHSGPw2XLXCNh7w0r4ryM6kLjGIlfdguCuZeMC9biVumV74q7nuJgsAcxpW44xY3BXc24hoB6GJLwjSMCTGc88D9JjscUO-yIzVuXzU8BHfuECFcJzeJy1nYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ادعای العربیه به نقل از یک منبع دیپلماتیک : توافق بین واشنگتن و تهران در دو مرحله خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/123341" target="_blank">📅 20:31 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123340">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
کاخ سفید اعلام کرد تفاهم‌نامه‌ای وجود دارد که ترامپ هنوز آن را امضا نکرده است.
🔴
به نقل از الجزیره، ادعا شده این یک آتش‌بس ۶۰ روزه است، تنگه هرمز بازگشایی خواهد شد، ایران قول می‌دهد ظرف ۳۰ روز تمام مین‌ها را پاکسازی کند و متعهد می‌شود که سلاح هسته‌ای نسازد.
🔴
ایالات متحده در مورد کاهش تحریم‌ها و آزاد شدن دارایی‌های ایران بحث خواهد کرد.
🔴
به طور موازی، محاصره دریایی ایالات متحده لغو خواهد شد و سپس آنها در مورد اورانیوم غنی‌شده مذاکره خواهند کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/alonews/123340" target="_blank">📅 20:28 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123339">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
شبکه ۱۲ اسرائیل : آمریکا از اسرائیل خواسته درباره هر نوع عملیات ترور در لبنان، از جمله جنوب لبنان، مرتب گزارش و به‌روزرسانی بده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/alonews/123339" target="_blank">📅 20:28 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123338">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cVdxxt4Mgm4xuS_Lr32Lr82lmdBPiGz86We-V-mNV6Xb8a4U1LA6lXmWuIaQSx-X_6pQr8dkAJt0_0hMpgmB78tgC4MUREzkfVREjpvXAfxFho2OswuRdYBxMdKdyTVtZaCWBiyP_fPry7h1Vrjhz7S5QsW9stwg0llsyy2Z7Y0q8ZeymrXNFC4CrOwc6H3bswL2ZprFQpa15kvf-z1X9SAhKXZtgGNL3sbzRDxPqPoyOSUiz2WdMnpx5TqjRbZmwSaMzItiZ4ZR_uchflilswxj8EwfFFd13ycs-gGK9OHmVCaXp_IE_fivQopMt0I8KgwozGe1e-IooXiv8O_4Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
رتبه‌بندی تیم‌های جام‌جهانی در رنکینگ فیفا
@AloSport</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/123338" target="_blank">📅 20:22 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123337">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/alonews/123337" target="_blank">📅 20:21 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123336">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚀
مصرف بالا؟ حجم‌خوری زیاد؟ اینو ببین
👇
💎
همراه با ساب یعنی مصرف بهینه‌تر و تجربه بهتر
⚡️
🚀
سرعت عالی پایدار برای استفاده روزانه و بلند مدت
😍
😍
@NetAazaadBot @NetAazaadBot
😍
آف فقط برای امشب
😍
❌
گیگی 50T
❌
✅
فقط گیگی 25T
✅
@NetAazaadBot  @NetAazaadBot
🔥
یه…</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/123336" target="_blank">📅 20:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123335">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PDebvyT-Gw6NEhxN4vF9AQ3J_os69P21cG2FxHwWtZu3JpUMHHeLtmBScPwVjou6G-FMu7o-31KDrkUKhPKKaecNZuTrpAqfHlHAyDVkzygTp0mHCvs-sasW-3UyMBZSfR1037Ha3CTaOmLGfHbB3qiy0wmWkZ9rBr04XLV2DZI_P5VjgMt9TAyNLIQ8F23QNHjLTre6a8FMofrWUbQ7VI37tAjkclblnuzj5ThOGvrdtJDZGOKuKL9u8e7aRo9yw_Q9BjHQZITZg-y5zvi4q1DWLwtFvWaILJ-myjPr7-W4KAXMgihU88qSzNHo2p_ImFkgwKUtzCosFSXIPVgwyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
مصرف بالا؟ حجم‌خوری زیاد؟ اینو ببین
👇
💎
همراه با ساب
یعنی مصرف بهینه‌تر و تجربه بهتر
⚡️
🚀
سرعت عالی پایدار برای استفاده روزانه و بلند مدت
😍
😍
@NetAazaadBot
@NetAazaadBot
😍
آف فقط برای امشب
😍
❌
گیگی 50T
❌
✅
فقط
گیگی 25T
✅
@NetAazaadBot
@NetAazaadBot
🔥
یه بار امتحان کن، خودت تفاوتشو حس می‌کنی
✅</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/123335" target="_blank">📅 20:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123334">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
امانوئل مکرون، رئیس‌جمهور فرانسه:
هیچ چیز حملاتی را که امروز در جنوب لبنان انجام می‌شود توجیه نمی‌کند.
🔴
ما بار دیگر خواستار پایان این حملات، بازگشت به صلح و گفتگو، و ایجاد یک راه حل پایدار هستیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/alonews/123334" target="_blank">📅 20:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123333">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gbe8jVzgt-NiekUpItVCCuY16d5IvKhQEjUBDeu2BP4KsSDatNvfJw1CV03kgfCdHY-Ckq71QiQg5I7HGY-dp77WtOlsly2LEVframltidSkXdYthQEvE0ABAtut0zgGfzWwAOW1vTbJvfDi0SM5Zx8YVdlnfFpZLqw8d42xahjTwHQXZSvtV8nTILozyxRQyhxFsftdrmzBbiBhkDcK7tZgE4IHRbk1PQNpA0uw7-7-0OwwyiRaUOPpgZUJzU3VtoZmahcZv0yhorCTXFtWXQmS6UUMpmZ3tEMNVFhbCrTNvXOqqdCU1z5mcS9OY7G-qhzz6_BHSnkWp8UfEcp7qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اتحادیه اروپا: اگر اوضاع تنگه هرمز بهبود نیابد، بازار سوخت جت با مشکل مواجه خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/alonews/123333" target="_blank">📅 20:06 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123332">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rxhZzuyhv15qhK8-zIYd_Cw9BlAzAx_n49O7qx0OGKu3QR4Dh03soYKmRaVICK6ZEV6kYsajQ5OqIXIsY9_joevOWwTkRJ8owbTcjoIxOD9ayYt3Rx26s7q5ZWGr1I_piXitfNABNV11S5s7GZv7eL2dKTDd9_fjoDjnktCwhQUyqkg8o_HDCIE-FFGpT3hSTXcl4DpedMpeUop3smN96GfE4NGURzZ6Lbq5wa4zdNmwWRAoFvQWQmrEtp0xWu7q0VUsdqlvWt4Dg8NwKSSOv9cD0T8f0dB6-IarqlZ7Oyy-O7Ci97wbx1evj78sKMimUMmsLaBZrJ-XfmykZzD81A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اکبری، معاون وزیر ارتباطات: بهبود کیفیت اینترنت چند روزی زمان میبره پس صبور باشید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/123332" target="_blank">📅 20:02 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123331">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/su85yh-pjDSbZ8ZPxTdms0SrWLbpp7Que_Rl-g1YgLqXwMDp08Bu5AJyTSzA-RhDAvEXR68UeA94QRnqXcuu6_hECnoBbuZLPQys7alQHvn2L13BvdB9tNcKvbwcFDsf1s0eBPhM8bek_YA41tT_TDHIuS5omrBlpU3QQE802jFtOwSJUNpP2JZtG9-eehIQGPvobYEPzAhPRuT_RKarRpc-CGfUD9SlF196-WdDAJ_e12urTlbNewxyZUP7HfDLDcdR0O_TfOHZa6SN17ZzJk4EdQEjjmTW39bhPJMfrhvcoU8LB_cyq0V1eMzytUzpCmifvgxb-JAa5VBT6CJgMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسکات بسنت، وزیر خزانه‌داری آمریکا خطاب به عمان: می‌دانیم با ایران دارید چیکار می‌کنید، مجازات خواهید شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/123331" target="_blank">📅 19:57 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123330">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
رادیو ارتش اسرائیل به نقل از یک منبع نظامی عالی رتبه: بعید نمی‌دانیم که لبنان بخشی از توافق آینده آمریکا با ایران باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/123330" target="_blank">📅 19:54 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123329">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
ادعای یک منبع دیپلماتیک به «الحدث»:
پاکستان به عنوان «شاهد» در مراسم امضای توافق آمریکا و ایران حضور خواهد داشت!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/123329" target="_blank">📅 19:51 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123328">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
عضو کمیسیون امنیت ملی مجلس: مذاکرات با پیشرفت قابل‌توجهی همراه بوده، بخش عمده پیشنهادات ایران پذیرفته شده!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/123328" target="_blank">📅 19:51 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123327">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
عزیزی، رئیس کمیسیون امنیت ملی مجلس: ایران پیشنهاد‌های خودش را در قالب متن ۱۴ بندی ارسال کرده
🔴
تنها مشکل سردرگمی آمریکا است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/alonews/123327" target="_blank">📅 19:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123326">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
دن کین، رئیس ستاد مشترک آمرکا وارد کاخ سفید شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/alonews/123326" target="_blank">📅 19:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123325">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbd4b148b0.mp4?token=TNlBLvZglFnrUuc4CEDvWk5Qzx1a2tpd5InZX3b67WUH4R1z2eLi2Ralv8LP3AOwLd6hwpGHGumHXjpoZ0jjcoCmRxU2QQJF6CrnxyppU3FVpP0eQQ-FHxqjL0pyoK4KtuWbY9kYeuiP8PtZA6miN19v7N72RMffklGTxKZYcaCoT6kOXxnaw6RA2LhYtfgpV3DqS5__aYvotSpQjpyjY4zhZODXu4kHbvIimOFXI-4Ubc3PWTrP76vzC4iWhFPMafrDNIEj-Ia0TqRjFdFPFH2ohGkfeA8XuvOnbiKX6uyMPOxG_P3JSX2SFH0z3K_t42dbx5g8cFc2-uq9ePpJxU2TIl78hHmZGRrS1E-5nVXUtVNKtBV3OLXtozYrYxf-WhD2M16SjvEwhPSuBZPrmZt89xRcTNsJ4ZrLfZLo2jAXT0km1zZSuNmQ0Oa-oDEfmw7tZTbKtNYzN42Jp53M-HdS1OATSvehwrXEVgicOW77kJpjmSMfihu9jsMVlIUHYBf4d49IENaUTnZPoJdtpz9tCtNHBKOznbvevzMmZlN6QaZuUiCtWEnXGDL4343e_izPEUgqjxLzt9EeI4FxJOYOobZoY5ClngDvHHPlpo_V6DvfBO1ZOepmX6S3ykayYKm9q8Ms_rZ3LS-0EOEiXvr6B5ErSlMCZB6DKYVpdrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbd4b148b0.mp4?token=TNlBLvZglFnrUuc4CEDvWk5Qzx1a2tpd5InZX3b67WUH4R1z2eLi2Ralv8LP3AOwLd6hwpGHGumHXjpoZ0jjcoCmRxU2QQJF6CrnxyppU3FVpP0eQQ-FHxqjL0pyoK4KtuWbY9kYeuiP8PtZA6miN19v7N72RMffklGTxKZYcaCoT6kOXxnaw6RA2LhYtfgpV3DqS5__aYvotSpQjpyjY4zhZODXu4kHbvIimOFXI-4Ubc3PWTrP76vzC4iWhFPMafrDNIEj-Ia0TqRjFdFPFH2ohGkfeA8XuvOnbiKX6uyMPOxG_P3JSX2SFH0z3K_t42dbx5g8cFc2-uq9ePpJxU2TIl78hHmZGRrS1E-5nVXUtVNKtBV3OLXtozYrYxf-WhD2M16SjvEwhPSuBZPrmZt89xRcTNsJ4ZrLfZLo2jAXT0km1zZSuNmQ0Oa-oDEfmw7tZTbKtNYzN42Jp53M-HdS1OATSvehwrXEVgicOW77kJpjmSMfihu9jsMVlIUHYBf4d49IENaUTnZPoJdtpz9tCtNHBKOznbvevzMmZlN6QaZuUiCtWEnXGDL4343e_izPEUgqjxLzt9EeI4FxJOYOobZoY5ClngDvHHPlpo_V6DvfBO1ZOepmX6S3ykayYKm9q8Ms_rZ3LS-0EOEiXvr6B5ErSlMCZB6DKYVpdrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: اسرائیل دیگر صرفاً یک قدرت منطقه‌ای نیست — بلکه اکنون یک قدرت جهانی است.
🔴
و چرا یک قدرت جهانی؟ چون ما فناوری‌های سطح جهانی داریم.
🔴
امروز، آنها این را می‌بینند — در خلیج فارس و جاهای دیگر.
🔴
ما اکنون در موقعیتی هستیم که می‌توانیم قدرت خود را در جهات مختلف به کار بگیریم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/alonews/123325" target="_blank">📅 19:47 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123324">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a1ee2f450.mp4?token=SjKc9gHUmPLEVvZjgsTvbr5UBxX58Qg4qLfmJE-BxWi6PitZWeGe5By5sTBRgbCq7YDlPxBMsKhqxElfz7TF033JddXw65d39NBRsMQ0DVFT7p7BtLdNsgFnrMXFbKCWzhktMlY5LXYW3Wkl-Vn6Ku9mY8DscS4Xmd8Of6_X8hxp0SAdZXWOx8bDPi7zVnr7smkiT58XdFuXjcXWYmgv6jnev-tLU1tShs5VdW-phrbfyLjiGsCoO_Wc_irDrt21lJpIjb69tdG9Bc9GNREy_RxBtaZvZ2hY7WgbQJB1I7dcXeZ_o1q4H_G_CZPy7iZ4K2gFMblcSGQpLqyHsCM1pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a1ee2f450.mp4?token=SjKc9gHUmPLEVvZjgsTvbr5UBxX58Qg4qLfmJE-BxWi6PitZWeGe5By5sTBRgbCq7YDlPxBMsKhqxElfz7TF033JddXw65d39NBRsMQ0DVFT7p7BtLdNsgFnrMXFbKCWzhktMlY5LXYW3Wkl-Vn6Ku9mY8DscS4Xmd8Of6_X8hxp0SAdZXWOx8bDPi7zVnr7smkiT58XdFuXjcXWYmgv6jnev-tLU1tShs5VdW-phrbfyLjiGsCoO_Wc_irDrt21lJpIjb69tdG9Bc9GNREy_RxBtaZvZ2hY7WgbQJB1I7dcXeZ_o1q4H_G_CZPy7iZ4K2gFMblcSGQpLqyHsCM1pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو:
در نتیجه بحران نفت، جهان منابع انرژی خود را متنوع کرد. آنها نفت را در مکان‌های جدید پیدا کردند و مسیرهای تأمین جدیدی ایجاد کردند.
همین اتفاق اینجا هم خواهد افتاد. من همین حالا به شما می‌گویم: آنها شروع به جستجوی خطوط لوله انرژی خواهند کرد که به جای عبور از خلیج، به سمت غرب حرکت می‌کنند.
و ما فرصتی داریم که در آن مسیر به سمت مدیترانه باشیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/123324" target="_blank">📅 19:43 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123323">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98c381825c.mp4?token=URsGtHvbQBN4IZRBa4Aq9HMwWpEXvbAx-eZb0kXtpReLy2zf6A9D8BVIWG1KG3i54gcOdt_83SbhyUScAVZUPgnnijB8StsBqNiFVjppY5YbffWxkicuI8j5q9l1FTI06YKgaUbNzEomU8eF_ZifTu4rqBMEwbKZ9yWNI6xUH_FJABUtjjiDjJbhuTQByYsvutkT1ho1oQxR9FKJ6wYEYB40TFz_v-Hojl_zB2LljinKhZeRi7rI82LeGOCIH1CyHKMzYMFbO3mwVYH6mIgOAsrFO0lM9cIns8S_QwxGcqYdeF5FqTob6C3qlIzVpAdK3b3Begj5BnIJe6BRGmI3JYrYBpOOaGXibHzsGADD2_chg9adxfckqeQCCgtvSbY7mUtVZwUhAFYoOUftLG7HUSDBOtTwDbhB2-sgmZQ2sA4yw5pKu5ftUXXUPaEQ0nn69ZXSAfe6bamRWLoC83N1A5DlMz5i2m2RWjXDFSx0sgSespPIVcJx-KqSuGWV1ao598NMbT-xPBQbipsYmbKvKYaKz3ew7fHccxvcY38stGwZlrZ0Q0-qBOhcnB5sM_2bFcYhS6OrF5tJlpYgKOliYrpbuiyLh642dncfq6TmKKC0gGikNwRz_G3Ewb1MaHht4fHyfXk-9hs34QLlCWE-fKBSXtZq3bbUa2IHYocYclM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98c381825c.mp4?token=URsGtHvbQBN4IZRBa4Aq9HMwWpEXvbAx-eZb0kXtpReLy2zf6A9D8BVIWG1KG3i54gcOdt_83SbhyUScAVZUPgnnijB8StsBqNiFVjppY5YbffWxkicuI8j5q9l1FTI06YKgaUbNzEomU8eF_ZifTu4rqBMEwbKZ9yWNI6xUH_FJABUtjjiDjJbhuTQByYsvutkT1ho1oQxR9FKJ6wYEYB40TFz_v-Hojl_zB2LljinKhZeRi7rI82LeGOCIH1CyHKMzYMFbO3mwVYH6mIgOAsrFO0lM9cIns8S_QwxGcqYdeF5FqTob6C3qlIzVpAdK3b3Begj5BnIJe6BRGmI3JYrYBpOOaGXibHzsGADD2_chg9adxfckqeQCCgtvSbY7mUtVZwUhAFYoOUftLG7HUSDBOtTwDbhB2-sgmZQ2sA4yw5pKu5ftUXXUPaEQ0nn69ZXSAfe6bamRWLoC83N1A5DlMz5i2m2RWjXDFSx0sgSespPIVcJx-KqSuGWV1ao598NMbT-xPBQbipsYmbKvKYaKz3ew7fHccxvcY38stGwZlrZ0Q0-qBOhcnB5sM_2bFcYhS6OrF5tJlpYgKOliYrpbuiyLh642dncfq6TmKKC0gGikNwRz_G3Ewb1MaHht4fHyfXk-9hs34QLlCWE-fKBSXtZq3bbUa2IHYocYclM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو پهپادهای FPV فیبر نوری را «طاعون جهانی» و «تهدید استراتژیک» خواند و گفت اسرائیل اولین کشوری در جهان خواهد بود که راه‌حلی برای آن‌ها توسعه می‌دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/123323" target="_blank">📅 19:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123322">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
سخنگوی ارتش اسرائیل: در هیچ جبهه‌ای عقب‌نشینی نخواهیم کرد و در صورت لزوم آماده‌ایم برای جنگ با ایران بازگردیم
🔴
تصمیم گرفته‌ایم روابط خود را با دفتر دبیرکل سازمان ملل متحد قطع کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/alonews/123322" target="_blank">📅 19:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123321">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: «شاید نوعی توافق بین عراقچی، ویتکوف، قالیباف، کوشنر و دیگران وجود داشته باشد — اما رهبر ایران و رئیس جمهور آمریکا هیچ تأییدی نداده اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/alonews/123321" target="_blank">📅 19:00 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123320">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
آمریکا ۲ شرکت هواپیمایی ایران را تحریم کرد
🔴
وزیر خزانه‌داری آمریکا نوشت: دسترسی ۲ شرکت هواپیمایی ایران به نقاط فرود، سوخت‌گیری و فروش بلیت مسدود خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/123320" target="_blank">📅 18:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123319">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
ادعای شبکه ۱۲ اسرائیل : رهبر ایران با توافق موافقت نکرده، و این یکی از دلایلی هست که باعث شد ترامپ به نفاهم‌نامه «بله» نگه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/123319" target="_blank">📅 18:44 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123318">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
کالاس ،مسئول سیاست خارجی اتحادیه اروپا: ایران و ایالات متحده در حال حاضر در مرحله‌ای بسیار خطرناک میان جنگ و صلح قرار دارند.
🔴
ادامه این جنگ به نفع هیچ‌کس نیست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/alonews/123318" target="_blank">📅 18:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123317">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
اسکات بسنت، وزیر خزانه‌داری آمریکا: هرگونه تلاش برای اعمال سیستم عوارض در تنگه هرمز را تحمل نمی‌کنیم و هر بازیگری که مستقیم یا غیرمستقیم در تسهیل آن نقش داشته باشد، هدف قرار خواهد داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/alonews/123317" target="_blank">📅 18:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123316">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
الجزیره به نقل ازیک مقام آمریکایی : حوادث اخیر هرمز تهدیدی برای مذاکرات نیست
🔴
حوادث اخیر در تنگه هرمز، مذاکرات با ایران را تهدید نمی‌کند و این گفتگوها با هدف دستیابی به توافق، همچنان ادامه دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/alonews/123316" target="_blank">📅 18:31 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123315">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا: محدودیت‌های شدیدی علیه خطوط هوایی ایران از جمله محرومیت از حق نشست و برخاست، خدمات سوخت‌رسانی و سیستم‌های فروش بلیت وضع می‌کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/123315" target="_blank">📅 18:24 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123314">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O85ieZ4KVUSX0bldpe2YVCmofpBTNtxBVAq-B74i5fllIx6IbFBNDmfgnLT9dbh6_jNtSrC9BBHK4grFHRes8gZRCInJuAQnZ2zUNAngbQhh8ORYgMIYiKzCmF3o4vm98MTmZT3rS87K3sWAUXWKNtYBtcboU1Mzu5NGJmHbnVwYICOPxjJ2pbUThn7HalOzMHJ1vTdSA_sWCZAxOAVMGGO5z_5sQbunkxaeV4k95gfRu_e41XzGtlpxrj5q6TeVEBUw9cd14Srl-4nTyhIJtB_5ecach12ua5VQTYlZogjAz6C35Rth3CaYa86wiTDv1X8r-RDaLfcOtP6LtyGsTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آکسیوس:
اکثر شرایط تا سه‌شنبه نهایی شده بود و مذاکره‌کنندگان ایرانی بعداً اعلام کردند که تأییدیه‌های لازم برای امضا را دریافت کرده‌اند. ترامپ در جریان توافق قرار گرفت اما به میانجی‌ها گفت که «چند روز» برای بررسی آن می‌خواهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/123314" target="_blank">📅 18:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123313">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
ادعای اکسیوس: به گفته مقامات، آمریکا و ایران به توافق رسیده‌اند اما تأیید نهایی ترامپ باقی مانده
🔴
مقامات آمریکایی گفتند که مفاد توافق تا روز سه‌شنبه تقریباً توافق شده بود، اما هر دو طرف نیازمند دریافت تأییدیه از مقامات عالیه خود خود بودند
🔴
مذاکره‌کنندگان…</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/alonews/123313" target="_blank">📅 18:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123312">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
ادعای اکسیوس: به گفته مقامات، آمریکا و ایران به توافق رسیده‌اند اما تأیید نهایی ترامپ باقی مانده
🔴
مقامات آمریکایی گفتند که مفاد توافق تا روز سه‌شنبه تقریباً توافق شده بود، اما هر دو طرف نیازمند دریافت تأییدیه از مقامات عالیه خود خود بودند
🔴
مذاکره‌کنندگان آمریکایی جزییات توافق نهایی را به ترامپ گزارش دادند، اما او فوراً آن را تأیید نکرد.
🔴
«رئیس‌جمهور به میانجی‌گران اعلام کرد که چند روز برای فکر کردن در این مورد فرصت می‌خواهد.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/123312" target="_blank">📅 17:59 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123311">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10b0b9d0c8.mp4?token=j-w9uZEaiuWMO2RvwHoB6s6m_QNFtRiBhDC8QMyHz8kQNUrmiueYzheWKxntthVaagMWZEMKKula24surpBUBPdLpmszDnFnvh0ojeqRhBSc1lYpc-32HcD7n4i-WHe2kbJdOT1vkADEOehbZt02bu8sZnnhyg68ecvrt71EJbKmQJNEIXeFocx9IFXWaRZJaN_E8z_1V31H3S1vQzRHWfM88s6nc2f3CorqfzydptCT0YkdC4gn4_PA08tIsRpFYb3HZssB8KBCrbkGtWNbb8nrHHIBsVrRgMboWM8vRubE0LbzGrenq6Kz3AUEGbfXbZStHDVEW7tMpDPGl1DC2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10b0b9d0c8.mp4?token=j-w9uZEaiuWMO2RvwHoB6s6m_QNFtRiBhDC8QMyHz8kQNUrmiueYzheWKxntthVaagMWZEMKKula24surpBUBPdLpmszDnFnvh0ojeqRhBSc1lYpc-32HcD7n4i-WHe2kbJdOT1vkADEOehbZt02bu8sZnnhyg68ecvrt71EJbKmQJNEIXeFocx9IFXWaRZJaN_E8z_1V31H3S1vQzRHWfM88s6nc2f3CorqfzydptCT0YkdC4gn4_PA08tIsRpFYb3HZssB8KBCrbkGtWNbb8nrHHIBsVrRgMboWM8vRubE0LbzGrenq6Kz3AUEGbfXbZStHDVEW7tMpDPGl1DC2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نخست‌وزیر اسرائیل، بنیامین نتانیاهو:
اسرائیل کنترل ۶۰٪ از نوار غزه را در دست دارد، دستور من حرکت به سمت ۷۰٪ است. با این شروع خواهیم کرد.
ما در فرایندی هستیم که می‌توانیم قدرت خود را در جهات مختلف به کار بگیریم.
ما همچنان باید بر حزب‌الله فشار وارد کنیم؛ در حال حاضر با حماس درگیر هستیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/alonews/123311" target="_blank">📅 17:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123310">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UgiDqfdNRJduZota8llWLig0v-OmZfHM1ZaBzdPpEm4IJI5RJYkTDHnc7uDEEtvhMZcJsBR5uTkHfWg03h-C7plNdcd0Zh_ZmambP8dqpljbVn9AHWhtEiiBYn8R9rLyJJtxJdCd1isLUGYUGoZbUT6DCdmHy3a720yTaKIzA7OJojG19zC8COEnTw-sMqy2ymUVMmmTQtr_1oOU6AFTDovOr1Y7hES8yn21zqOlHqlLs2nzavEJly23mTBrARMtALZ6h5fPZonU_AP_pf3u9EIst1SEZB5MPrZWyTS0c8_WMI_lvWL0GnDlw7swPigFlXlHGMyLMk8jD5YWpbaBtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
ماجرای نماز خواندن کریستیانو رونالدو
سعد السبیعی، مدیر پیشین اداره حقوقی باشگاه النصر:
🔴
پیش از آخرین بازی مقابل ضمک، دون (رونالدو) با بازیکنان نماز خواند و سعی کرد در رکوع و سجود از آن‌ها تقلید کند.
@AloSport</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/alonews/123310" target="_blank">📅 17:30 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123309">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
روسیه:
ترامپ با انتقال اورانیوم غنی‌شده ایران به مسکو موافقت نکرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/123309" target="_blank">📅 17:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123305">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac373359e1.mp4?token=ax2kKjLBG8JMFfPdf90jzXUXqLW2yHRciO1uIt8QAoqeMFFt5fgh9ZR-d527RPYTxxAdmorfk8m2eTfqlVL_y40Xly-ef8ZIE7oLRk0jVBFj7VryMbjaXxnyyJwirOaeT8U6dUtpLJ9cYSmsPc18eVB2u6M1FKZWQyLZKYV9amwjxfNWqWJzYQxZNPHRUQ9RgYuoet3zADicOLwR6nUA7-vzE_0DMdL9s9ztQ4P3PKAoLY6UbFTRYUe0rv-lSVmGQtgTDhSJE1ZkFbtP6A17oV1z1om0K4xYS9xVVU-J11sN3RZeYVxC17zVqV8enrX-z_29suXBFI9XUjhEz7KoOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac373359e1.mp4?token=ax2kKjLBG8JMFfPdf90jzXUXqLW2yHRciO1uIt8QAoqeMFFt5fgh9ZR-d527RPYTxxAdmorfk8m2eTfqlVL_y40Xly-ef8ZIE7oLRk0jVBFj7VryMbjaXxnyyJwirOaeT8U6dUtpLJ9cYSmsPc18eVB2u6M1FKZWQyLZKYV9amwjxfNWqWJzYQxZNPHRUQ9RgYuoet3zADicOLwR6nUA7-vzE_0DMdL9s9ztQ4P3PKAoLY6UbFTRYUe0rv-lSVmGQtgTDhSJE1ZkFbtP6A17oV1z1om0K4xYS9xVVU-J11sN3RZeYVxC17zVqV8enrX-z_29suXBFI9XUjhEz7KoOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت وخیم لبنان بعد بمباران امروز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/alonews/123305" target="_blank">📅 17:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123304">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده درباره محاصره:
نیروهای آمریکایی اکنون ۱۱۱ کشتی تجاری را برای اطمینان از رعایت قوانین هدایت کرده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/alonews/123304" target="_blank">📅 17:11 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123303">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74fef6c239.mp4?token=l4f8v_UAAV_8ST1jyXwHUjdfNQyeg9qmc6fBcN8VaVixwrK3FLGqp0BthY2oL4KfqtCXehN2y8J8UG0r50CIZ4s0rQqgglsxuP5h4WViLrEusX-rNTybqqrpBat5pfOcAkSY1grXkfKcgsMsKLU4ngjnwwt6969XHM4CQiwS4wHfLYZOl7azNkIH2LPCvL9LqsTw8mfI_KVj06dMfdSpYGQppCj-IfxMu1v239dzGCjbLTnpOnbzqEc1ky9zKrjcTTE3xUoNkw9sdzX0WjMiDFbI40FH2hAIV2MF2PXDTjnGFHFQa8Hs50oqH3ogY3aSYkypWNbBT2i9GYETmJtg5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74fef6c239.mp4?token=l4f8v_UAAV_8ST1jyXwHUjdfNQyeg9qmc6fBcN8VaVixwrK3FLGqp0BthY2oL4KfqtCXehN2y8J8UG0r50CIZ4s0rQqgglsxuP5h4WViLrEusX-rNTybqqrpBat5pfOcAkSY1grXkfKcgsMsKLU4ngjnwwt6969XHM4CQiwS4wHfLYZOl7azNkIH2LPCvL9LqsTw8mfI_KVj06dMfdSpYGQppCj-IfxMu1v239dzGCjbLTnpOnbzqEc1ky9zKrjcTTE3xUoNkw9sdzX0WjMiDFbI40FH2hAIV2MF2PXDTjnGFHFQa8Hs50oqH3ogY3aSYkypWNbBT2i9GYETmJtg5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: الان ما تو بیروت حمله کردیم، دیروز در صور هم حمله کردیم
- نیروهای ما از رود لیتانی عبور کردن،ما اونا رو می‌زنیم و خیلی شدیدتر هم خواهیم زد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/123303" target="_blank">📅 16:57 · 07 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
