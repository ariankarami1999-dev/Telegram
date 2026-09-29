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
<img src="https://cdn4.telesco.pe/file/B2g8qpBPbOZbGgIEA7yodNbMZg4prkUUAeC9QXOkjivxfkCHT9Nc6eK5CwE0ybva8XB4N3agcRYRzlaAe9t0IQkgxkS9nTmT5HhF25D6EjgnbT91HyGuQNCCYf7Y1AcFLAHPEwm0qsRGQm6pDatlTdMZ5V3jhSAuClSczCbUMZtIhVfNwAepEA2ePUtKBrVEBPwmc6YOn_fVxgJO_IrFrz7ltvW48n-6N_bdTl53Ml0AX9KosOfKAhqJ3TnFZmGLwEpnQ0de9f28XXu0NOmkQ5aNz7S0gnU_k2C6wwke5K9_4C4E2xyDAtjCGyBqxeD-LMYG19JPPMAdhIveLtjLzA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 252K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-07 12:18:18</div>
<hr>

<div class="tg-post" id="msg-84164">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">سخنگوی قوه قضاییه:پرونده حقوقی ترور سردار سلیمانی در دادگستری تهران تشکیل شد که سه هزار و ۳۱۷ نفر شاکی داشت
رأی این پرونده دو سال و نیم پیش صادر شد و بر اساس آن، سردمداران دولت آمریکا به پرداخت ۴۸ میلیارد دلار محکوم شدند.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/funhiphop/84164" target="_blank">📅 12:01 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84163">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ما میگیم اعدام فوری بیرانوند دور میدون آزادی شما میگید بره سربازی؟</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/funhiphop/84163" target="_blank">📅 11:02 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84162">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/398fe520da.mp4?token=rxxQyj7JwOyk7fX1ihdlr4PY57f919_lzLZFL1m7ZINmjBknf7eio9jtfM95_b74ZNcAtLbULPMQS7uxUYkIQQVowr5peVWO0ABzawOMMfluKUefxbxI-0scN884PsN30gWg9H8blIrEWN6Xs25a_qQfG_aGDTt9o0U2VgqE1GV74ttXR75Fk9HOipLIrouNKUxM4bI94ST4Yse8LDMVB6tfVHEbaAntHM6ti33YZIDgF2xIW_ruzXHkBDzW9K94cknk_peJPJAOzTu-3P1bIVGic5KZq6zEDiXi83JK9O0_1Matq8BYY-7QumCQGnRJCnUFP5_wW7bnCaWYJe7RrrUFHcK_zX6XFIAUjeVmqbhlaSuZ2VshiWgnXdFTgf0WnLT-Ls1-PioHmg4lH7bcMF1YPfK2tc8VmjZLTC4_3aMafhzBJfr7HowaXQrECVTgw0L1SDf1XgS6TStwKGv2w4J4NmqDPmq4OEt7K8Bt3rl5pulQFHxdImb__mktLuz0NsUvXZLNixdanev6OC8BqM3hnoKOeeh_2jKO8zDz_SLCKjd6JwsrlXkAFpsfpxoBgQczQI87WfgMighnoNKO-MrzmdFnet6qhCTgCR7UAfOdhXoVBsvKINWAGD5jMsmkvzXIc0hPH9lmnpCMtZsT7t5mS9Wcy4hafo4PmH6mpbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/398fe520da.mp4?token=rxxQyj7JwOyk7fX1ihdlr4PY57f919_lzLZFL1m7ZINmjBknf7eio9jtfM95_b74ZNcAtLbULPMQS7uxUYkIQQVowr5peVWO0ABzawOMMfluKUefxbxI-0scN884PsN30gWg9H8blIrEWN6Xs25a_qQfG_aGDTt9o0U2VgqE1GV74ttXR75Fk9HOipLIrouNKUxM4bI94ST4Yse8LDMVB6tfVHEbaAntHM6ti33YZIDgF2xIW_ruzXHkBDzW9K94cknk_peJPJAOzTu-3P1bIVGic5KZq6zEDiXi83JK9O0_1Matq8BYY-7QumCQGnRJCnUFP5_wW7bnCaWYJe7RrrUFHcK_zX6XFIAUjeVmqbhlaSuZ2VshiWgnXdFTgf0WnLT-Ls1-PioHmg4lH7bcMF1YPfK2tc8VmjZLTC4_3aMafhzBJfr7HowaXQrECVTgw0L1SDf1XgS6TStwKGv2w4J4NmqDPmq4OEt7K8Bt3rl5pulQFHxdImb__mktLuz0NsUvXZLNixdanev6OC8BqM3hnoKOeeh_2jKO8zDz_SLCKjd6JwsrlXkAFpsfpxoBgQczQI87WfgMighnoNKO-MrzmdFnet6qhCTgCR7UAfOdhXoVBsvKINWAGD5jMsmkvzXIc0hPH9lmnpCMtZsT7t5mS9Wcy4hafo4PmH6mpbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با یه پست رپی ناب روزمون رو شروع کنیم
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/funhiphop/84162" target="_blank">📅 09:35 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84161">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">صبح دلار ۲۵۰ تومنیتون بخیر
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/funhiphop/84161" target="_blank">📅 09:08 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84160">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">یسری رسانه میگن عراقچی قبول کرده تسلیم بشن و اورانیوم هارو بدن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/84160" target="_blank">📅 00:36 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84159">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">مادر ترکیه گاییده شد که</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/84159" target="_blank">📅 22:44 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84158">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">قوه قضاییه: حمید رسایی به بند ویژه روحانیت زندان اوین منتقل و رسما زندانی شد.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/84158" target="_blank">📅 21:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84157">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qDx4FvteXwj9e4OF20fpm-7umRycAPYN5LqWpB58d7HV5l2sUwP5g9J_hiMnfT5R6xs-nAiciWFjwoG9tC9Id77metNc9PL-qKv8A3bJUxlCKRT9piah5R3mJR-vhLhJr0lOsbawPFqurq6tMg7jtFhOSEGHlQxCP-EGP_qN2c6agpdWC5uTwX3NzmrBmrW1PTez1E3rAH6wAQCTMdhothVqkJS_dD1N6N7H1VObbnYt6xQWivGTQvvrOZnNFDCYzuty4avsr4RwsoZm8ymGk5hR3f50HtidoydIcfmGGEPwycb3yHhPfNSUl3tzy5Lzf1D0MsvF2SnZmGbJsmz4_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضاییه:
حمید رسایی به بند ویژه روحانیت زندان اوین منتقل و رسما زندانی شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/84157" target="_blank">📅 21:33 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84156">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_c6DVzRJt-Viev7AGwHNN5l4JYEKGjXa53xOg04Z6JIGALUEZksPmvIOkOzL5oXt5sFVaHVoE_DMpag5lB5lTkPp200SQsNEfFzgzEjismH1ShVQejIxxz9MI6yXKl6FENbAXHCkvvAO75AHOKzdTLQI7qPKl1wCIMIx7gxyQcjq2ExsdQLk0HTClLqBTcOo9a4_eL--nrGuLru5Dg6MnggasxGRxfNKEfNMnJO2fVquz-xagkMqosTr45fGgZ9Jc-Bo5pVhzI9Y7w1y8Pjhm8U6L5YNsb-7H03AZibqb08vf6Z3bJF8EBAmlcEp6Gsc-RTGy1XInFr7wp5RVJGNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من وقتی یبار تصمیم میگیرن رو فرانسه بزنم بعد عمری
واکنش زیدان:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/84156" target="_blank">📅 21:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84155">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fwS_gLwSmBv6Ph5Bbu6K1FHgy2fYhw1PNHZAOmD3P-8jeWDbLeaig7FFJBh8-iyc4zAjUASvvQMzcSJUyODWwmaB0MQocegyqY39m4V2jA_yGWyyl2-ZbPvOmK0wuos1a371TRFK4uZTSVOwD4llfPayNEqr4gzU5Nr6q8fKzqfBgABRQz0ShtYnfBKwafuoIqZqFPwOU__8JQsZf6iyqoEetnkiTvmu5EiyWN2igmggKKosxyh-lzocW1fGUksH_wBDm_3llqAiTrklkiLqU8rHknQkHx8wzaJpI3r7h8M2mIfi2rMGldaQoIxbMx05TjPa_lhec7dWNkj_Z199Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تسلیت به دخترا
ایسم عکسش با زیدشو استوری کرده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/84155" target="_blank">📅 21:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84154">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">بهترین کیفیت کانفیگ V2RaY با تخفیف و قیمت استثنایی
☑️
فروش ویژه کانفیگ های تانل با کمترین قیمت تلگرام همراه با ارائه  نمایندگی ویژه جهت فروش
❤️‍🔥
🟢
گیگی 2200 تومان
⭕
با تست رایگان + زیر مجموعه گیری با هر دعوت شما 10هزار تومان هدیه هم به شما و هم به طرف مقابل…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/84154" target="_blank">📅 21:08 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84153">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LEyBYjlr2icLExFF12j--ZWBFOi1T9KK22yCoAu8vHaHCmJXYe6vvQGH7deJxvEmXTbowqz57uMBtR_QpCxHFfb1Jd5z4WWKS7Ku9ndvCn8ggCNSqW45WqH_OLi7EiOhtuk25meGqySsbUxYdJxD3hcGoo88reMi0dEuGTqw2Y9gsHWLNDaBq-I4rEjpSp9cL7LOSmaIJwDULZ9O0TO5A6O1vJ544oufzGwvfPtYr77k5rB9keDyEFJGtE5HSxTaT2M1044Ip_yq74-HOvHvl6TQE6pdz2uw5c_SjlT2EcI3Ci_ek69ejy7YLIT7RpuZuW7MkXTbBT0lHK1viFdOQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین کیفیت کانفیگ V2RaY با تخفیف و قیمت استثنایی
☑️
فروش ویژه کانفیگ های تانل با کمترین قیمت تلگرام همراه با ارائه  نمایندگی ویژه جهت فروش
❤️‍🔥
🟢
گیگی 2200 تومان
⭕
با تست رایگان + زیر مجموعه گیری با هر دعوت شما 10هزار تومان هدیه هم به شما و هم به طرف مقابل تعلق میگیره
🤩
🔖
جهت خرید و مشاهده محصولات:
@HyperPing_VPNBOT</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/84153" target="_blank">📅 20:57 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84152">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aff9d6bc22.mp4?token=HbDmMvDH-qPowresK81ErXd0fGBm1_0tntAvRROrFy0TWmdPGOVrHQjP5YQ1VE7uqmUItA-RqylMGHp3VCfq4NS28eQs_JPStuxiY9d0qyL8UftclNssrKSRsnsZKKl84NAGb54P7U5mfl6MMzDGlZzI1SY5TYI_scIGuwtpcfHv4Zn9OZh5LSMB3LEpf5RYaGad_5HnMRig5COKuZFqyz_UChJ-8BKWl3krJA9ER1_G5u42mVgkN3N0rjJ7_qgGPQPA6voa7bJhMOvZ4LlJ_Kwm97TQhVpOwPjnxBYJrxMV2dQl8YYVJX598n3nln7dyNZgFaV5DiUkqf2iPWyPcjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aff9d6bc22.mp4?token=HbDmMvDH-qPowresK81ErXd0fGBm1_0tntAvRROrFy0TWmdPGOVrHQjP5YQ1VE7uqmUItA-RqylMGHp3VCfq4NS28eQs_JPStuxiY9d0qyL8UftclNssrKSRsnsZKKl84NAGb54P7U5mfl6MMzDGlZzI1SY5TYI_scIGuwtpcfHv4Zn9OZh5LSMB3LEpf5RYaGad_5HnMRig5COKuZFqyz_UChJ-8BKWl3krJA9ER1_G5u42mVgkN3N0rjJ7_qgGPQPA6voa7bJhMOvZ4LlJ_Kwm97TQhVpOwPjnxBYJrxMV2dQl8YYVJX598n3nln7dyNZgFaV5DiUkqf2iPWyPcjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حلال ترین استفاده از هوش مصنوعی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/84152" target="_blank">📅 20:09 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84151">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اسنپ پی روح و روان سالم چهار قسطه نمیفروشه؟</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/84151" target="_blank">📅 19:38 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84150">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">آلبوم جدید ناجی به نام "استار بوی" ریلیز شد.  Youtube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/84150" target="_blank">📅 19:22 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84149">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HwaQwsjtfE7PpnH3G8_FKXfiYNbofEeW5RO2qJhHfonX7kJPl0Q0L5fto64gG-w-3F-rp6AdXGz0O1MWvjIH70Im-63nckzZPQeOlPzhfr9Sch7v1F21p_hVJ_WYn4Uwaq6hvm-62dYEBnmkrTc3N9rCtBCR_6Mxe338cF7rsHYgNJT0hfVrKVfKsp91jbuzx9mU1eHQffIgFvA3-cqyU-G1tlxtfh9O2H21wfebwJGEDyWJMZDLT6Cqol_k6a5YjCT_COzZ6XfqLyybSowIjZB5-a9JbS2QYMe_dFeqouzL5wrtksIXIQ94zGo8EihNubRRXggXvtNlvEy87-RcDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلبوم جدید ناجی به نام "استار بوی" ریلیز شد.
Youtube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/84149" target="_blank">📅 19:21 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84147">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZoIW6bk0KWajzBXtqeGN_k6454a_CAxiQ1Y2FXpAVRNHa6wJ1N40pgli9XHquHKAZhqry3BBFM7IFcPl-blu8oswEhbBJjC1_bgRD-q9TM3MO4UqwmfQ5-Ti8CjZPvZpYGM8v3fAhoj9e4fUH6BtCQfkxzAuSDSQ24Kxm_st--C_pQZlIkqum47FqjtVMk_yOLVr6I3X5e7WmQD1lIzJWGUkH4HgqjuPfEath5AyRPnuTDvYHuiO9KGa9AdZbj4kOB0__w9Oyl1A36d4ckzFonPbH4dq35oaQFionHtXA1-_0JS9X9cQQfdU6n6R1m4SjD0LlW_0-y7NQNH48BTSoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/213569f829.mp4?token=LNNyq8cd7iHqNav9HPJrADMgHTxDZl4FQPUny3AMaMBYgDxxl0RKne69QnowtpPczNQVrC0z5SnQH1VLnwD0CO-CQXCz9Gu919zoXpkduznz4tnBBC54XjnQBt6JeadRJoqSPRqynH7MTdvr7V1c4fD_DyGOywYhVwCQbwJQSBnizWfcpezOlNSHiC7Wdq13Ur_8zpVfxqexiikkF0mrRia7SPDDHH7lXoBDuLoOfw5MbYLTsWRyqP_65-nCQRWN6vkRqMQM6AYKN2ufF0vGjOvFC2ddVIVbQRQHme6ztHbtFFU0rQoyRB9rEqu2CzZJxSPASQEBQMG8g1KqTUYprA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/213569f829.mp4?token=LNNyq8cd7iHqNav9HPJrADMgHTxDZl4FQPUny3AMaMBYgDxxl0RKne69QnowtpPczNQVrC0z5SnQH1VLnwD0CO-CQXCz9Gu919zoXpkduznz4tnBBC54XjnQBt6JeadRJoqSPRqynH7MTdvr7V1c4fD_DyGOywYhVwCQbwJQSBnizWfcpezOlNSHiC7Wdq13Ur_8zpVfxqexiikkF0mrRia7SPDDHH7lXoBDuLoOfw5MbYLTsWRyqP_65-nCQRWN6vkRqMQM6AYKN2ufF0vGjOvFC2ddVIVbQRQHme6ztHbtFFU0rQoyRB9rEqu2CzZJxSPASQEBQMG8g1KqTUYprA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به این داداشمون دابمسش های دخترا با موزیکا علی گرامی و سجاد شاهی رو نشون ندید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/84147" target="_blank">📅 18:43 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84146">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ritzobet.apk</div>
  <div class="tg-doc-extra">45.3 MB</div>
</div>
<a href="https://t.me/funhiphop/84146" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکیشن اندروید سایت ریتزوبت
🔥
🚀
وقتی شرط ‌هاتون رو توی ریتزوبت ثبت کنین ، علاوه بر ضرایب بالا ، هفتگی با کد های هدیه کسب درآمد میکنید
🤑
♦️
آموزش شارژ حساب با کریپتو
♦️
آموزش شارژ حساب  ریالی در ریتزوبت</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/84146" target="_blank">📅 18:43 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84145">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qgIhMSZHPYJKIah7ptYGxHDjKUObjiensp6aB9M2WQ2_i1w7exFL-fuL2qjk1Q1SnHo_-rolm2YEDFyqP0ozte0n7ttIx65dBtZiMX6Y7nqChyR2voWagsuklOtY1F5Q-vaMsOfBgUjdBOIykHQPCLJUSGj9Jmeq5nj74b323g1tfkbDHaFvwN_4nYw121_qW2wjLL_34Jwv25ENlgKEUIok_Uqs_R1mi-rpsNCFaEJpv2qE-LsrOUJ_2RFQeAlZKJQysChl3jzSl1N2ENfx2M6dSY89lbCe1h_nHpio1TjIuTshAqlIOlLoltJFIpPHYcmVydmvjMhWQyvVV-spUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
برتری با کیست
⁉️
شاگردان زیدان کبیر در فرانسه یا کوین و رفقا در بلژیک
❓
🇧🇪
بلژیک
🆚
🇫🇷
فرانسه
🕔
ساعت 22:15 به وقت ایران
⚡️
واریز آنی با کریپتو
⚡️
تسویه‌حساب سریع و مطمئن
⚡️
دسترسی آسان و بدون دردسر
⚡️
محیط حرفه‌ای برای شرط‌بندی و کازینو
🚀
همین حالا ثبت‌نام کن و تجربه‌ای متفاوت از شرط‌بندی آنلاین رو شروع کن.
📲
اپلیکیشن موبایل برای اندروید
🌐
https://RitzoBet.com
پشتیبان فارسی سایت ریتزوبت
👇
🅰
g6
⚡️
@RitzoBetsupports</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/84145" target="_blank">📅 18:43 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84144">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">باز قیمت دلار رند شد ملت یادشون افتاد دلار گرونه</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/84144" target="_blank">📅 18:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84142">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">نمیشه به دلیل تقلب های سیتی یدونه قهرمانی آسیا هم به پرسپولیس بدن؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/84142" target="_blank">📅 18:24 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84141">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ولی این انصاف نیست کانیه وست کیر خورد پسر عموش کیرش خورده شد کاسه کوزه ها سر من شکست</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/84141" target="_blank">📅 18:17 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84140">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNo happy</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNTjfiaQh23myLgj8DZRxnnh2PyzgsQtvn03KRRzPEsuLx_FUqijJL2Y8heMf49J-hfZ2dCp18LPp1_xAr7kbLdJjlBPH0D2HHZpL1cLLkkxUrpSNdy2rRFf9c6VI8BYSUvJwCYr2ZTyrrZk1FTa7TwqJsOQlgCB2fREw8azMci4BGIdmkAh2nZrAJ-p1rbK4N3ZLDcGB10UNihdpLHgtTsDCTxmpiF0UWR4ZSweo0Gh8fJARlo5acTnRiueYH9FERZ-3WyFliNjVvhbObMdNyoGClUkG1KgwxjHhB4aDur_NbuXj-HNddyyaX7GY_OWJwFyxMkdpo4VtJOAHQx1cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلم مهدی رسیدددددد</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/84140" target="_blank">📅 18:10 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84139">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">مجتبی خامنه ای: امروزه، برخی ما را به عنوان چهارمین ابرقدرت جهان معرفی می‌کنند. البته، آن‌ها این را بر اساس محاسبات دنیوی می‌گویند.  اما از نظر محاسبات الهی، ما به عنوان قدرتمندترین کشور جهان شناخته می‌شویم   @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/84139" target="_blank">📅 18:07 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84137">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">مجتبی خامنه ای:
امروزه، برخی ما را به عنوان چهارمین ابرقدرت جهان معرفی می‌کنند. البته، آن‌ها این را بر اساس محاسبات دنیوی می‌گویند.
اما از نظر محاسبات الهی، ما به عنوان قدرتمندترین کشور جهان شناخته می‌شویم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/84137" target="_blank">📅 17:23 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84136">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f73abc8dd.mp4?token=W0wNg54Kwp-37diEoW74esv8sJG8bKJntvXpYGUE0NuKOtrKW1cS8LNaBrQsnLofFi0ZraliPR1i--NmWqak3DiGMVGFSzxcJnMnwQYzaTThYzPsBLn3XzmTfuLWwHXro-t8gcaAFEZg22aF8STJN00qJnXpf-wYXXHZxMPmatCJZ99w6G7xgbYMLBjH3pOra5xG8FwWV2-6OxUxVu_B0Uuz08ymbRhF2BaxHLtvsht7vgWpQgk8Xhy3Y-Dha4IIQDHEzEDqcZS760ej4SOVhxU0fGz8g1P1FDtbnUak1wbaTMTeO8u_luSixlm8h3KW2KmUmaipziB4QdjvGd4XmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f73abc8dd.mp4?token=W0wNg54Kwp-37diEoW74esv8sJG8bKJntvXpYGUE0NuKOtrKW1cS8LNaBrQsnLofFi0ZraliPR1i--NmWqak3DiGMVGFSzxcJnMnwQYzaTThYzPsBLn3XzmTfuLWwHXro-t8gcaAFEZg22aF8STJN00qJnXpf-wYXXHZxMPmatCJZ99w6G7xgbYMLBjH3pOra5xG8FwWV2-6OxUxVu_B0Uuz08ymbRhF2BaxHLtvsht7vgWpQgk8Xhy3Y-Dha4IIQDHEzEDqcZS760ej4SOVhxU0fGz8g1P1FDtbnUak1wbaTMTeO8u_luSixlm8h3KW2KmUmaipziB4QdjvGd4XmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پول دونیته ها
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/84136" target="_blank">📅 17:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84135">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">۶ تا F35 دیگه جهت استحکام سازی پایه های مذاکرات از آمریکا به خاورمیانه اعزام شدن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/84135" target="_blank">📅 17:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84134">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">دلار ۲۴۵
ترکوندی مذاکره، عالی بودی مذاکره
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/84134" target="_blank">📅 16:23 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84133">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">استاد بیژن مرتضوی اعلام کرد که نه بابا ایران کجا بود و نمی‌خوام حتی یک نت از موسیقی من... و از این حرفا.
ولی خبرنگاری که امروز صبح خبر برگشت استاد رو منتشر کرده بود خیلی اصرار داره که استاد همون‌جوری که تو اجرای جام‌جهانی تونست خیلی خفن بین جمعیت پنهان بشه، الان هم داره خیلی خوب پنهان کاری می‌کنه و همین خبرنگاره قراره ساعت ۹ شب یه سری عکس و سند از استاد پخش کنه که ثابت می‌کنن استاد ایرانه.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/84133" target="_blank">📅 16:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84132">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Op5olc97VkyXkyRgv6IBxQP4aacufCIk0vfO89Ghel6kDijHgTdzosCtSU7m8kIBEm4NchW6y5TpzaRUGNOJq0bZ0wN8g3kWCJnUItAUhnYP6hv__Q3O6u_XbNXaDh2bM_ciPTG081sdo16xEiihJzwmUorRwleBfSCelU24H-9dAy5fvw4J2EP7OFmYqyuC7PohTKWILfdNlAckZddvGHou9y5MLi9A5INAu88getDSiUY609-0AnS_AOvpR75f5C_8vVWHMcKVCuerApQ5hNelJ9rHUMupDMoQZesJVcSXFTltJ60EpLoVZmQIhXfkkvvO63I5_BBDPdh5PJLbuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مردم کشوری که ای کیو چهارم جهان هست
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/84132" target="_blank">📅 15:47 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84130">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">به نمایندگی خبرنگاری فان هیپ هاپ سه نفر اول به این بازیکن ها رای دادم
1 بلینگهام
2 مسی
3 کواراتسخلیا</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/84130" target="_blank">📅 15:18 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84129">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee4b03712b.mp4?token=Lnc3fYiSk-d9DJ_tRuinNbObhEal-2sklKA6GncPNwTgtPfoh2JtsfyOCJpa3DlVeKWTYcQ7V3Oo7zXOu04oM6m5-nXAtWP1rj0LQdWsBPNQjzpENaLXWK1cqvpBOe8SaVuTFMsOgrgmsCRpQLZnl11agYwBD8CrTS661j8PIB_d2Sn6Knauy2aAkXOLKVU6UscI2KoOBtNV8FQwDnvwJu_FwQ7MMojHI4dKPplsv5xTi6OM9ndZeJYO-bnTRrmwpaJ3IQF26CRVdkl0CvywrguOxh2f3P1wv0M9DGc7jhy8U5EHzXRLvKJKRpW_Boq0A7ZaS8Hx9ErQOkR6Ljn79kkSxiZQFO6JVzF2WVm--guq-PgB1rGhRbm3PNOw_NBJMT_8shBzvtwJqN8BbWZtumy0DeJjFHWFmLtUT3wZmouSJ8s-cdmBlHEpMGRspvekOJdna3ZVN5HU7Bjef3W-wPr5sJ84Wy3n4_93p7Hy4M6sKdOw-BvJ4LJgevwKKVZ0DogoJQdIWRiqDe8jqpD8vUA8wSK6VLZjPD49LNRw6G_pVhjj5A1oAE_pCDuwzCkqyDQwmkTobkch4SsxQzZ5dudv-1B9QM4dwFv0vkUEEgn9w_cpwSpmDGhUIM38dzJCJ1sud4BtZ7PIZvBPSU-EYsZ7FxNJAH59-2a25Mrbop4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee4b03712b.mp4?token=Lnc3fYiSk-d9DJ_tRuinNbObhEal-2sklKA6GncPNwTgtPfoh2JtsfyOCJpa3DlVeKWTYcQ7V3Oo7zXOu04oM6m5-nXAtWP1rj0LQdWsBPNQjzpENaLXWK1cqvpBOe8SaVuTFMsOgrgmsCRpQLZnl11agYwBD8CrTS661j8PIB_d2Sn6Knauy2aAkXOLKVU6UscI2KoOBtNV8FQwDnvwJu_FwQ7MMojHI4dKPplsv5xTi6OM9ndZeJYO-bnTRrmwpaJ3IQF26CRVdkl0CvywrguOxh2f3P1wv0M9DGc7jhy8U5EHzXRLvKJKRpW_Boq0A7ZaS8Hx9ErQOkR6Ljn79kkSxiZQFO6JVzF2WVm--guq-PgB1rGhRbm3PNOw_NBJMT_8shBzvtwJqN8BbWZtumy0DeJjFHWFmLtUT3wZmouSJ8s-cdmBlHEpMGRspvekOJdna3ZVN5HU7Bjef3W-wPr5sJ84Wy3n4_93p7Hy4M6sKdOw-BvJ4LJgevwKKVZ0DogoJQdIWRiqDe8jqpD8vUA8wSK6VLZjPD49LNRw6G_pVhjj5A1oAE_pCDuwzCkqyDQwmkTobkch4SsxQzZ5dudv-1B9QM4dwFv0vkUEEgn9w_cpwSpmDGhUIM38dzJCJ1sud4BtZ7PIZvBPSU-EYsZ7FxNJAH59-2a25Mrbop4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رای گیری توپ طلا هم تموم شده ۴ ابان برنده رو اعلام میکنن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/84129" target="_blank">📅 15:08 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84128">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2NQK5YL2kZLrJ2jkl7ee24MGpjxHxkhpqQfwSAghZ1RkDakHfBOT0YFv-8sQosv6Xw0xVtSDSZxNTdbmI790Ip1KUQfvsZV1Z1UH5NbIhA_m2bda_hYqT0-0RMgHS5-_JiDIQrOtr-My4MbLEPRzhpaKVzXrbCLpDqd9rDmZk1cyZM4daLZkpa8kenUjEJEMy1ddRz1KbtUyBtdVRm62WWigbEDC2Vno3zGVe3qBAELTrPVZMRyrsYjhVMaCqH0sV-OLPzXNl-8fJNbXf8Owxgi--jz8D9-4xWka0d6KNCmDWALq03J972ZpxVXrzrHi5AWSmktBkbnj_3lq40mgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ما که راضی هستیم
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/84128" target="_blank">📅 14:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84127">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e988dd3baa.mp4?token=neYEa56GwuHMqtLCFjo9lu2IWKPqmhxX3TcJTai3IIzuKSqblDtVJu6Jkt4Fh_MtvjRN_Xpqww9Ieupe_0M9rOjiMPIK4RsILDLBlvq799Ajfa9jGK-8KSFSIzTzBxBoyhmliNU0MEEEfaHMvPZYtCvxcwb9CysXDwb4Cc9IC_ihMFvnZgDC6Gws4gg_lYJ9ZHC2R8X755IP3nBvx1sqAwPc-LeBQCWQJ5vOpQACCTXqvK4eJp9rN8o9ohkLZRJt8lOMzBvb845n30AWrJW5G7LXqiRyPH94lJisSg-9jSaU7bWgcX-D2AY_V5ymYYBAG8VQI6BCMWePpoPGUxP52A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e988dd3baa.mp4?token=neYEa56GwuHMqtLCFjo9lu2IWKPqmhxX3TcJTai3IIzuKSqblDtVJu6Jkt4Fh_MtvjRN_Xpqww9Ieupe_0M9rOjiMPIK4RsILDLBlvq799Ajfa9jGK-8KSFSIzTzBxBoyhmliNU0MEEEfaHMvPZYtCvxcwb9CysXDwb4Cc9IC_ihMFvnZgDC6Gws4gg_lYJ9ZHC2R8X755IP3nBvx1sqAwPc-LeBQCWQJ5vOpQACCTXqvK4eJp9rN8o9ohkLZRJt8lOMzBvb845n30AWrJW5G7LXqiRyPH94lJisSg-9jSaU7bWgcX-D2AY_V5ymYYBAG8VQI6BCMWePpoPGUxP52A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش امین تیجی به گل کاشته‌ی دیشب مسی و فحاشی ناموسی وی به کیرستانو رونالدو
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/84127" target="_blank">📅 13:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84126">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tSdLcI9JZJIGhSLmqMN_NOXdCA2dVqtT9widb8li4zal37hOwFnQvYpoMustXU45nqX6fmGrFSzKuMyflLtnChEGYeGCS8jYL3cONioqABNkWmY6ECeg2JgWZtKmVVcERnbOCsO-S4ArOZORW3n3VkzLavRVc2fPYgicn9XZ5FnUC28LIyuFSd4-b6nkElhbZ0bAovVhcW1I3_4twViTq_nz1k5ZJRo-IXDJnO5p2aUvYRUUt-JY4UZ-qKsDihZFIGGs59z4wZR7i04n4ivEyTAsNc_L_mMytJAkCkbl1KaztGW6o7kxA-eotUYHd4kfHNbZcT2iTjW3OPDhiyIfAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخجون.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/84126" target="_blank">📅 13:45 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84124">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e46577007d.mp4?token=Crh6nh-BvYAP3o_hMguud1OBUjQYxgiiDHmo5SMVdHCbcbJVyY6K4cDy2UExFdA58S0tZsEpYnnS9ZtoIfzSeDiclikEj5xP2IRqkOU7MqH4ib--Ez-3QYtLo_s4rtWHC8_VkgtUlEaJbubWosRMafqJ6p6KnVCfrH-sUDMmHyG_rMjrep4laVOpMus_TR-Ac378eKDf4f8VVOusjjbtsx8S-79KJdsJ4uYLsH5xEs13WKyKTswwugp9wq0rLC-3bzw5baZG2NoMUlyhu8sNRTuHn9yTagl7zqYuw6aCRbcgvVo6-DVBvGt7qv4o4mE_fehyNu4pOiens_TTpCBF1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e46577007d.mp4?token=Crh6nh-BvYAP3o_hMguud1OBUjQYxgiiDHmo5SMVdHCbcbJVyY6K4cDy2UExFdA58S0tZsEpYnnS9ZtoIfzSeDiclikEj5xP2IRqkOU7MqH4ib--Ez-3QYtLo_s4rtWHC8_VkgtUlEaJbubWosRMafqJ6p6KnVCfrH-sUDMmHyG_rMjrep4laVOpMus_TR-Ac378eKDf4f8VVOusjjbtsx8S-79KJdsJ4uYLsH5xEs13WKyKTswwugp9wq0rLC-3bzw5baZG2NoMUlyhu8sNRTuHn9yTagl7zqYuw6aCRbcgvVo6-DVBvGt7qv4o4mE_fehyNu4pOiens_TTpCBF1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوس دخترای چرسی و تیجی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/84124" target="_blank">📅 13:35 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84123">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00bebdd4e5.mp4?token=dlMa8W9vTu8VVO6V6zGgPS7D_duEK7rknIq002CRdiI0eKKLDDCstH2YOE-d3aPQrRy84APPjMay6Cgtw2N9KpRZqejfRt73gRuCaXL10FHzTUx_O-BGLs6L9qk7DXpDSxJGiPDLlxF9MCUcOD6xNHKS70RM91WFyDYdFwMsneDf7N4Tg8qnwO4AOX1vhRmm-nZfBfQHuAxIBs6WaXDaR0pOe1IEcjOFFW1d7RJaCWHwxQGMgbCDmdvlwOSrscTg4ngvEpKSPDq3RWpeA-PakDqp0MBAKsxy25OpMu161qD443ZFUpAszVddi-X0lgq4HBt2ZMmyEmSsEyA1cVNwhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00bebdd4e5.mp4?token=dlMa8W9vTu8VVO6V6zGgPS7D_duEK7rknIq002CRdiI0eKKLDDCstH2YOE-d3aPQrRy84APPjMay6Cgtw2N9KpRZqejfRt73gRuCaXL10FHzTUx_O-BGLs6L9qk7DXpDSxJGiPDLlxF9MCUcOD6xNHKS70RM91WFyDYdFwMsneDf7N4Tg8qnwO4AOX1vhRmm-nZfBfQHuAxIBs6WaXDaR0pOe1IEcjOFFW1d7RJaCWHwxQGMgbCDmdvlwOSrscTg4ngvEpKSPDq3RWpeA-PakDqp0MBAKsxy25OpMu161qD443ZFUpAszVddi-X0lgq4HBt2ZMmyEmSsEyA1cVNwhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیش از ۵۰۰ بیلبورد دیجیتال در خیابان های منهتن نیویورک خطرات ایران هسته ای رو نشون میدن،
احتمالا این اقدام برای آماده سازی افکار عمومی و برای شروع یه جنگ بزرگ صورت گرفته
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/84123" target="_blank">📅 13:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84122">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ناو هواپیمابر یو اس اس تئودور روزولت CVN-71 راهی خاورمیانه شد
تئودور روزولت قرار است جایگزین ناو هواپیمابر یواس‌اس جورج واشنگتن شود. مدت این استقرار بیش از ۷ ماه پیش‌بینی شده و خدمه برای مأموریتی طولانی‌تر از حد معمول آماده شده‌اند.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/84122" target="_blank">📅 13:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84121">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2R6BBri1bpPvdeHVypLti-dEJvYzKXx_yjk1a46I7z_JjJlD7Jsrz7VTe-y1G9O0Hb8z7Ekq56dKR9ooe96vxuJGm0QmE9k_SgOw3QM7ktP-vEB95go_KxojE8sLKULSnBEaf29hFmy0ykx1WaruMoqTRH4paEGP1SsDeqxigUSPgdeGLMG0cwzeeMyfiBsBmnIKb8KbrkyGp6iZQEVjFImJcMhlOdJ8mWWXPQsZnQLhSMrG9w1CjumS-Tyio3xRTiUnSHsvo5iF1BPlbNvBl0Jpa-fO115AUGc0q_9bb4pt1hOKRQqmrwdf1vGfVlIj9fh9BpjCxE_tod3LBY17g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بوی جنگ میاد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/84121" target="_blank">📅 12:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84120">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ritzobet.apk</div>
  <div class="tg-doc-extra">45.3 MB</div>
</div>
<a href="https://t.me/funhiphop/84120" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکیشن اندروید سایت ریتزوبت
🔥
🚀
وقتی شرط ‌هاتون رو توی ریتزوبت ثبت کنین ، علاوه بر ضرایب بالا ، هفتگی با کد های هدیه کسب درآمد میکنید
🤑
♦️
آموزش شارژ حساب با کریپتو
♦️
آموزش شارژ حساب  ریالی در ریتزوبت</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/84120" target="_blank">📅 12:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84119">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ChBlYdjxBPjzaXdFBx971-WA_xeqWJpHiaqHcqaXpxziaoa3JtFxzWUQ9IRbilYpB-JtR0sCZgKB8XasNuj0L5yTx6bSxxt_-QwqzH6lA1SMp9xMVFE9RIdRvOFhXEksNKqfs_CkoSIIwj7eDoEnuK_Os8c3CPrt5PfsDbRDw95IudawWT5DJwW3W8OabVM6KMCoGSLXqcQkeAoEutrA4efEfsf8iNC48Bwh1hFMs_y5KpoXa040P-eUbpl7CFeDVO_AHh7HkSypWZqZvrXZIjBd7Xw6N422_f11yE_72D_QoKndq5xXVGBic4c1gILWMGWlYKvN5uVavVAC7GNBAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👏
یک بار شارژ کن ، دوبار شارژشو‌ این طرح اختصاصی ریتزوبت برای کاربرای فارسی زبان خودش رو از دست نده
🔵
اولین پلتفرم جهانی و اسپانسر لیگ هلند محیط امن و حرفه ای برای عاشقان شرط بندی فوتبال
⚡️
واریز آنی با کریپتو
⚡️
تسویه‌حساب سریع و مطمئن
⚡️
دسترسی آسان و بدون دردسر
⚡️
محیط حرفه‌ای برای شرط‌بندی و کازینو
🚀
همین حالا ثبت‌نام کن و تجربه‌ای متفاوت از شرط‌بندی آنلاین رو شروع کن.
📲
اپلیکیشن موبایل برای اندروید
🌐
https://RitzoBet.com
پشتیبان فارسی سایت ریتزوبت
👇
🅰
r6
⚡️
@RitzoBetsupports</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/84119" target="_blank">📅 12:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84118">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">حتی تصور نوازندگی بی‌نظیر و پشت صحنه‌ی استاد بیژن مرتضوی تو کنسرت مشترک استاد نامجو و قیصر با حضور افتخاری مینا نامداری، چشمام رو اکلیلی می‌کنه.
🥹
🫠
همیشه می‌دونستم آقای پزشکیان از خودمونه
❤️
#فرق_می‌کنه_کی_رئیس‌جمهور_باشه
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/84118" target="_blank">📅 12:01 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84117">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AMn1PPuKyBeSE5vFZvGII44fsgzVYELTDHUJzNBqogalJtDWskw-0Dumjkynu5RwVAAhy7FaM9qukG6BW6REQMyTyHg1G9LHybnUtEVqTDLOrGK9xIuNDFJ8OhK7vCp-V3bOUBp1BWn9nd0F_7gPGysXVJlzaDyAYxsCQHAaQzR5EhmbNSsWHJnNIf4tBbLfmphLoXhhA33yTM44pyNKIwOKiR_4M0zp_gR0F3AdWA4pzeKh4pZ1qcvEYaQ_-BEaSkHfavRzQ7LZQ3loWA7w9PXbAcOkNySqnFkEJH1Ib_c4-4j_EVJG2lYQVp0oumwTvNBcfyYwGjN5vwxBquDj_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری و حمایت هیپ‌هاپولوژیست از کنسرت اخیر بیگ‌شگی که خبر از احتمال همکاری این دو نفر در آینده‌ای نزدیک می‌دهد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/84117" target="_blank">📅 11:35 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84116">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f68DosT2dMSGcaKb3GV551O1QGum0rb5zny51HVgIF-hFFjTVb-Vq_itTSuNOjgqIi22r1Ke3RRr1S65R3273xE6KV5dfVi7J_0jR3ZrGHqo10r7PJA3B6PwJiLdNjOX7EiVwNPqgAkDfv0M5sj9_LeBGKK8xg-0uxuJXPP0103Zj6qlCMTT0igYIQpmwTu66E0XXFY5wUrKmW6qumOlxoZK3l2RUzdUMruCsexfi6QSq7kI6BrRXDdASY30_fBr-woEd5m11lRtFLVcgzRhkm7AegCKxp3E3iE7JzX0vYD0UVDdga_P3I_xzZSsQXJ-xxmKNbuQMgpQkJnRmgOCQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که نگران مهاجرتشون هستند ذره‌ای نگران نباشند و گول تبلیغات رسانه‌ای دشمنان رو هم نخورند.
دریای خزر هنوز با پذیرش خطرات کاملا احتمالی تقریبا باز هستش.
در کنار کلاس‌های آیلتس و تافل و خوردن ۸ لیوان آب و قوز نکردن، کلاس شنا رو هم با جدیت پیگیری باشید به زودی تورهای فرار و استتار در اعماق خزر با امکانات و قیمت‌های ویژه موجود میشه می‌تونید بدون محدودیت شرکت کنید.
❤️
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/84116" target="_blank">📅 11:23 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84115">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ناو هواپیمابر تئودور روزولت آمریکا هم پس از نهایی شدن مراحل آماده‌سازی راهی خاورمیانه شد تا نشون بده دکتر عراقچی حتی تو نیویورک هم با تعهد کاری و تکنیکال عمل می‌کنه.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/84115" target="_blank">📅 10:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84114">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DyRxNJSyc4i8c9Fe0iCVY8bJDH21Lx8LT287Nvd9kivJ3-GCaMA1OMm9lH4hTNe1nURK8SRVwuRObBXSPwcDK-mpuDyMwgSYcappcscyVzNgnf4KUjneYe1T_bYMsheE3V2TGf32Bgaw51aHO4xTQkpzecA6rUfFDJbrMdSxgAwO_SiFhCAlTx0y9Qj6mkojU75-yCFN96Xf_lvCGgPwLBD7Luqrw-QrBtUlzHUxhfkaHRnId5elatF9qaFLi_kdLVD88oUkbFoSWOqzf1R73kwGiejhP4AAkSxUFu1hsMkQdFWWa55Nb5XZCJ1clR3T7AUylu6W5xH3N6MO3hqK9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر حیف شد وارد مارکت ترکیه نشدی
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/84114" target="_blank">📅 01:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84112">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">سلام بیایید چنلم
https://t.me/+q5Ml6Hl1Af5lMTI0</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/84112" target="_blank">📅 00:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84110">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aqyLWy_FPwtrjZPshrPqSvAMfiBrvBAqK3GnRXbyO-OYTy8hhEbwiYQhDsS6PKvhSF0e0hwNUyfAVbOTMlLPIlApfejVR71FL12RQi0BIFLLLO352vkO4589FeCFLgDxogjNendkrlPH9xabcVW4aErdIZ5ZYL7cKJXtDoLH738fuTC0HoXCm4Y8qCHD-VpDSXK3jFfDoZ1vCVMFIHp75BFyrR1mrouryflCK0OwUKBoJ5MtH6GOhhWi0Gx2J9bb4ujj5-4xnrU1a4jAG6SqzWWl11NIC7iuaVR7clPzh1SPhUHi942h5BGArt0CKz0M72-OhmfnsTghG8TxXR-oXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vaVAwVKuRXAbrVBtwwEybxCIS8VfYaHki1oKndrR--MuZLSEcAemVRJvQ-cmMXQHEBIt-zh8hQnROVjyFcD-Pv1isCv3Q9wrLtFPpFyYQFA-bswkRe9pC0BH56HRxheN4lgsmhr2vi9RzmF2QrkdOKdxa_buNEILkHtmQnUM7gk7wHqtNuoraCbIzrZhc74TEkoI8mooCdsGGhqghyXmmMAF4It8534eV7zMpMpLWfMoT3HkAgSY4Gw_3OYr1wVnFwMYKmyQNfI7wvXdaXfSskRDzV9-sBVLD-ACHlQderjwANW13SPWb2ix9KhqbD8a1m2MH0FDzPEVXQqLL8CSTg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به مناسبت شاتای جدید سیدنی سوئینی موافقید کیری اورریتده؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/84110" target="_blank">📅 23:19 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84109">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZNsA-yK-PBzIS2VxgXQorUBRnYvknn_3LGOG5hnJU2Z2tU2FIm7PWsE5mlz6joN41S30SjcNnKpXOmZNnl24lFLQQ2BrduuoIIo7dtDRHbpTTCyxe8_O2PiJaiy7eBKoPbq671Pduh7MlfQvaUvkj-y7BY9j4jb5h-TjEffd1iCh0StfgeCFaOwr5sCwydIBYqOBRkGLkbUoZZl9gKYMb4mkuyX-FzNNY82D6CwDx-HajJVnlYZBJCYYCskbycB13pJaBenNAhTzaFBQjOcMU8kHdWfCOhqte945qpyFmGrdQ10KoFGBWpznijRti8fJe2NRBBSNXV7cwuDeTKxUSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشبینی ایلان ماسک از آینده‌ هوش مصنوعی:
2029: ربات های اپتیموس از بهترین جراحان جهان پیشی میگیرند.
2030: هوش مصنوعی از هوش ترکیبی تمام بشریت پیشی میگیرد.
2031: ربات های انسان نما از صد میلیون فراتر میرود.
2032: اقتصاد جهان دوبرابر میشود.
2035: درآمد تضمین شده بدون نیاز به کار کردن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/84109" target="_blank">📅 22:08 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84108">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔹
بدوووووو نامحدود اومد!!!!
🎉
بدوووو حجم نامحدود، سرعت بدون محدودیت!
🪙
بدوووو یک ماه نامحدود فقط 270,000 تومن!
💸
بدوووو 50 درصد تخفیف افتتاحیه، فقط تا آخر سه‌شنبه 7 مهر!
👤
بدوووو یه اشتراک برای تا 5 کاربر همزمان!
⭐
بدوووو هرچی روز بیشتر بخری، ارزون‌تر درمیاد!…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/84108" target="_blank">📅 22:03 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84106">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/urn9KTDG7wI4cJgY1o-c_pSE_Q4OownFc74yf-pCJNdSuRbcdya1SVngBpUyty1WYq8vqfVUYIeKVqSr9S4NozchsV-9bx0oKq-qVCMuQv4UCKSlmfeji53513BUYVuP8YOIFhFrDlIyBQpGRjLu0r69WEqSJ9Ynw70I7_YiMkIgCKkpoJRMw-Z0bGnEls6ni_dDf7El1NN8R8ucBTEEqhmYxSBjephGm4FA0YEkJKgW6HENSbi7ONc52tKFk_9xt7k5v62bclvh-KlADUCB_pdx2vihXSwyscc6PU4R5k0uzLeuqioc3lBHRU2UgjxIPUHmKPuNaqN6eSDU8sWjmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
بدوووووو نامحدود اومد!!!!
🎉
بدوووو حجم نامحدود، سرعت بدون محدودیت!
🪙
بدوووو یک ماه نامحدود فقط 270,000 تومن!
💸
بدوووو 50 درصد تخفیف افتتاحیه، فقط تا آخر سه‌شنبه 7 مهر!
👤
بدوووو یه اشتراک برای تا 5 کاربر همزمان!
⭐
بدوووو هرچی روز بیشتر بخری، ارزون‌تر درمیاد!
🧨
بدوووو 2 گیگ تست رایگان. خوشت اومد، بدو بخر.
🔹
@BodoVPN_Bot
| بدو وی پی ان
🔹</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/84106" target="_blank">📅 21:58 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84105">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">عراقچی:
غنی‌سازی ۶۰٪ غیرقانونی نیست و برای اهداف صلح‌آمیزه.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/84105" target="_blank">📅 21:21 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84104">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">از روزی که وزیر نیرو گفته ناترازی برق نداریم و دیگه قطع نمیشه بجای روزی یبار روزی دوبار برقمون میره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/84104" target="_blank">📅 19:22 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84103">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3ce0419e2.mp4?token=rc8Sq9FBa2ib_zwhnb-ck_sr2gnbgw4axkpsgBwi9UIHMoKsFktdGN6AxRbD1jfiZnTbmiwyebs6mSlweXO1CSxI2dFbyq2DZkZgVbAJ_31rghXV7TI-9TSEIum-2XwiKMmCo8QJ0eYqV5BinPBEf3ndNxOuVUySqN6QMv3yNY_L4z2EmCavSPbdv0O2dDD4YUqba6tnLPcBq1TUU4KdYwItYU6Y1uii42p2EKhJiiJXpyj1-0_gN4PurWrgwgsKDfPdpwkVqpIAWZGsLB7O8i61F20qhGm17iqRGhCyDBYT0tRStuEBda1M5TVLRpbJtb4R_B7YjjpxhW2jhf2s3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3ce0419e2.mp4?token=rc8Sq9FBa2ib_zwhnb-ck_sr2gnbgw4axkpsgBwi9UIHMoKsFktdGN6AxRbD1jfiZnTbmiwyebs6mSlweXO1CSxI2dFbyq2DZkZgVbAJ_31rghXV7TI-9TSEIum-2XwiKMmCo8QJ0eYqV5BinPBEf3ndNxOuVUySqN6QMv3yNY_L4z2EmCavSPbdv0O2dDD4YUqba6tnLPcBq1TUU4KdYwItYU6Y1uii42p2EKhJiiJXpyj1-0_gN4PurWrgwgsKDfPdpwkVqpIAWZGsLB7O8i61F20qhGm17iqRGhCyDBYT0tRStuEBda1M5TVLRpbJtb4R_B7YjjpxhW2jhf2s3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی برنامه دیت ناشناس، یه دختر مدعی شد بلده یه طوری نگاه کنه، که باهاش می‌تونه مخ هر پسری رو بزنه
و در نهایت این شاهکار رو خلق کرد:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/84103" target="_blank">📅 19:12 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84100">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMahdiyar</strong></div>
<div class="tg-text">کاش اسم منو میذاشت</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/84100" target="_blank">📅 17:39 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84099">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HyfR241Rh6x2sCn5XHhG33epocT6izqgYE9zwOIeONqaFd2zEVKYg2Qd1lyilRPbsZqW-FYECutCKKAZ8WiUYH801J_nLXBKVbci4hHCj5jbWUsEVgxW2WF_r8Y0zZMZCtYPrahNKOktLvPukS9HJKCkfXeHqFl_CcwLvFvp29bp1bqMSxY9aKkDdkaO6Ti7IgCixSIUvki09JQBHqKlXtl0QEEIZGaNLfsbVYdElrb6ePX9OhnVEGoli-w9ncNe5pvxDUUlReKnjNxXhfO2HU53IqFViZUNgWVlgLNqBtFxyCk4UvelydjaQ84A8FrtCZgRp7XjKBUpssF4M30Gjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ممد ناراحت نمیشه لنا اسم پتشو گذاشته تونی؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/84099" target="_blank">📅 17:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84096">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kt4fEfoY3h1fo3OUmiOjwGGiapWAcdBlOEUOpW5_x7u_LknuVcrw2pdXnEcnUy9qFBGPuGm35C-vyEWZs2N9-ExuutgdZh5BM7oMU2S3RPuvlKCy_zQa6S2Ssf06TITkLsDBGXDRdIN21pNyOwhL4nKeTljcROxYtPUVewPiWWmISLLmDFJG58ZiiFV3nvWxjxnNptRe6d5IVCY-JxAnjpgL7JaikeIOFYH4NikNq0a27aN-bFGxKfUqC2loIliKD5irsKm9uGw17JGsvk_FXURuGFImjsPIybmssA8EE9uDRsgE2p_MvBu_kBOUy6kq2ZcGdH_MR6n5WoY9xBD0gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GRsftj9ySCGjHSjrNFpP6DL__oSoXZTkrUH7JeMvz3EWITqwRiqUUHnAA5xJ15_3v1uWILQrViC1-HFZBxDwM3EMkBlwkRrTro27m_b2MH8IDi8_DEj0IK06P-GFuIEz_k7NEjbDvJT8ktgokJap6XZMyoPdk0XymzADkS_o6rILRi3usP2-RNgZjAFtdaTpAdhYke0mJFP2kkqJuNZe7KGs0zAqmEwxqVNlmwSuH7RSH0SG3iYZBwX6t5EZftbSNg38WWvvnZtsWRS3ACUDh1OCHryjPXPTye6lgHIoGjACEzbSBlb4t69SWKC7Mv2MvzdrmauXFK_tT8zmRX2Csw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ro_N8uiq1Q-sj0GyanLGNg-EBLx9mLgwo9QyvwI7oqG4hur8OoaRN3AisR9UIMGZtkTlFHVmNRJZ2bTcOcoBybaMV0KQ1YFM7Nx0lmyI7ftFw1fK21CjIp-txJBK9a3_TaQSsPhheJDupDZq_--AolImJwNg1u1BQetIL_kfZ8gqcMp-3KateiVUBVhYLhivpA2JpO2vPX987XktPbSNgWYcqjjfci6ypFuGzlgp-GY7fF3Hu0nL6oobh0AKgnihbDHjCFBrp2f_zE1Ls4lUj_DOoUxwYhxPU51-BdQUDQ5Y8y48FIt9tmuSu25CMyzZ_PW-rnbGVYUVneJhED-Jww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست جدید ریری و کامنت های فرزندان فهیم کوروش زیر پستش:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/84096" target="_blank">📅 16:00 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84095">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">هانی رامبد تو دایرکت هادی چوپان:  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/84095" target="_blank">📅 15:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84094">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t-phrVDdY0RS4SDtLNZMqLxjX8bJ5p9ZxrYDArqd7qkaw1TgeVEr2G1-cU5U3YU2K8CEY0GaAM_7puFLDtXD3Cs8hAzn2tXSIblLRiBYn2OFOAAmFOkxBSuWdeKpN7UTmH62gohhbm6eAd3ijStoGBqS8zTMP2PH9Wx3-lqdG3JZ0vELFE-yaMhsf1RUGZaAkxNWAkCN_cqioqmsCLe2PNKiwoN5PmFavy1oBhxd6-g4DbJotUeU8-qVuDThq0kOZkg1KhKWX8WSgmkt5MAajXPSmmzGLC4SZ_1hc7Dojkava-SwgWjeX_UUSkTLIDSotP4IO15t6pZsujCd_yV5ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هانی رامبد تو دایرکت هادی چوپان:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/84094" target="_blank">📅 15:46 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84093">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b331c3393f.mp4?token=JadLw-hXkpG5iWvlMHDmarE4PfOQnT2KCyG_KL2eS4tnqeKf60_2x5sQSNgjDM-Pi5W13-OyiMjSSYwmxuJvs-MuKzOFRH8DqG_WnJJ7K6tU2IsPOqTMxzQKBihwgploZKnTFJqy-v1B3U1mNOE_25J2h0Di7R6XJ9UZEAe4iYU8hpIoV_gLOCLdb6OCMKdQGDXC5YiFBTlJkTYCz81cR_3E32Itxr4SuMiIXeEY6hD6rzXvUIR8JQaH7Gv_8Dkf8vNS_O2i5pVfXRxCCshPJ6vwSIz0hkczDFATt5S9RUqKmSSGObq1XGIGYp-SYoXFqcJfeX8cEaySWOv7LrrCQ7eFRuTHL7RmsI2Z8ywp5M0ryplRmaPolJqM--4Ok90YB36lspsp4t0ZaEcQUj0-x5IcDtzFZdwH8uEEc4sCIzmn-PQ24Oscs-BCHZ_oUBjdIFoK9sQYcWsbzOcGseCozwUKO-Cjoi19ReV6LWyLgGiwC5NYrHQy2bUoE6gp_XtV0-FnSSdsk5IhR5PEjN8yR_9UwrwiNE-NChjpV6gkR8v0v_H2gAPpekfylJ28yy62XyVTU61YMdPqAGyYO9kZszZtuCQCCSoumuVZ7cMqV-oyuEQbQ9XHzR3Dh8sqGzP05ZAg2k1lpsjXbUnEJlqnsUyPTq2QsbU_LQMAr9dSY3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b331c3393f.mp4?token=JadLw-hXkpG5iWvlMHDmarE4PfOQnT2KCyG_KL2eS4tnqeKf60_2x5sQSNgjDM-Pi5W13-OyiMjSSYwmxuJvs-MuKzOFRH8DqG_WnJJ7K6tU2IsPOqTMxzQKBihwgploZKnTFJqy-v1B3U1mNOE_25J2h0Di7R6XJ9UZEAe4iYU8hpIoV_gLOCLdb6OCMKdQGDXC5YiFBTlJkTYCz81cR_3E32Itxr4SuMiIXeEY6hD6rzXvUIR8JQaH7Gv_8Dkf8vNS_O2i5pVfXRxCCshPJ6vwSIz0hkczDFATt5S9RUqKmSSGObq1XGIGYp-SYoXFqcJfeX8cEaySWOv7LrrCQ7eFRuTHL7RmsI2Z8ywp5M0ryplRmaPolJqM--4Ok90YB36lspsp4t0ZaEcQUj0-x5IcDtzFZdwH8uEEc4sCIzmn-PQ24Oscs-BCHZ_oUBjdIFoK9sQYcWsbzOcGseCozwUKO-Cjoi19ReV6LWyLgGiwC5NYrHQy2bUoE6gp_XtV0-FnSSdsk5IhR5PEjN8yR_9UwrwiNE-NChjpV6gkR8v0v_H2gAPpekfylJ28yy62XyVTU61YMdPqAGyYO9kZszZtuCQCCSoumuVZ7cMqV-oyuEQbQ9XHzR3Dh8sqGzP05ZAg2k1lpsjXbUnEJlqnsUyPTq2QsbU_LQMAr9dSY3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی یه ویدیو از پابندش گذاشته با کپشن"یادگار دی ماه"
و حالا کامنت های مردم:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/84093" target="_blank">📅 15:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84092">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">بانک کارگشایی یک تن طلای مردم که دست میلی گلد بود رو بالا کشیده و میگه دست ما طلایی نیست، حالا میلی اومده به محسن رضایی نامه زده که پیگیری کنه.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/84092" target="_blank">📅 14:23 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84091">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XLvymAem1iEXUn0P64-rKYvkZrTOuKSV02LcZVb8GIIA84wrAuptnKNROuukxZyHRDnQuwNOzROGEu2HWOt00RxI9vkJlneoYQzWwu6nfnUHIInfQvJ-tuWUUJHpALf-OQsKTfDqrtB7G8l2_RtuHvLSlRbH32lfeBdGLJ_VYy5f50oVLmbi3IOhXFm1uUpEx12qnfE8_aCCjinw2pNyqEr2GwAIeeV5cc95cDINacHSOx3zrcOs4wU41uzFKMf167MRuViOrJ5HIbeolvWMJvHuf8oxsB0aBo_yP3QkWM-kuWkN6QnRNJ22p5ZN8owKugF-IG6AXN5644qYcC6MSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانک کارگشایی یک تن طلای مردم که دست میلی گلد بود رو بالا کشیده و میگه دست ما طلایی نیست، حالا میلی اومده به محسن رضایی نامه زده که پیگیری کنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/84091" target="_blank">📅 14:19 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84090">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfgX3CMV6-Yfwr8OkLQ4PrjBIjUk4wf4i1ZayM3Z27-hGAe8b5rNh3iD3WpgHWtafa-Guq4HYA3x8FDmyH1MKtdJIe_1-FjFBK3MG8CAUzKuygjL7UddvvZn4k-Un65uZ-iiZZ6v9ayilHy635vhFc_i4SK0aSm5XzZRcBlBn7qWLaZpJgqGUpE6VT-dPrTR7kmO_yM85pCsENgVzine9fPK0hLxk1u2J1KQgsb28FQanO8HuvjxyrgDz61ctoOEyneGPIf6HjaEq28nohrKbTZKZHmRMwH6ZW-V0nGlKGnDq3SC229sMeqQSminM7LKjf1l_t27VoS2y0eToosm4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد همین نیما و دارو دستش تا یه چیزی به آرتیستاش میگیم میان میگن نه هیت ندید و فلان، وقتی ما میگیم هیته وقتی اینا میگن انتقاد سازندس.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/84090" target="_blank">📅 14:12 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84089">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e6331f6cc.mp4?token=eWm_yXOQrdIFlpfMJImq0WyBtT8NcSEfV6q7QlNgFH1BvgoFrdsYHe8kxlwQwGW5o-IDuEiHxVbNLynp7KVx_w0UrI-pE3O0A-5U5o9d7eYOQAtQ8z8LVtipBCqnJYXfYV-xnCz6W-RRu7sZ5tWtYrazCNVnyWtQzGs10Z0MWOXMNZQp_WL5ZYG-YM672Bi3GOwWczG5ZBRogqT7U7wOpbK1cilLaibd3Im_7rgCR2rPbdADg7U6g7ysR4Rw3EpFHgPwN63eUMTLYmILCzmERBTdT3jgoxeYGpMDM2DybzkktawVDDcoZWVJPR7fxC7jlWaffGwPZz43sKv_hbfazA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e6331f6cc.mp4?token=eWm_yXOQrdIFlpfMJImq0WyBtT8NcSEfV6q7QlNgFH1BvgoFrdsYHe8kxlwQwGW5o-IDuEiHxVbNLynp7KVx_w0UrI-pE3O0A-5U5o9d7eYOQAtQ8z8LVtipBCqnJYXfYV-xnCz6W-RRu7sZ5tWtYrazCNVnyWtQzGs10Z0MWOXMNZQp_WL5ZYG-YM672Bi3GOwWczG5ZBRogqT7U7wOpbK1cilLaibd3Im_7rgCR2rPbdADg7U6g7ysR4Rw3EpFHgPwN63eUMTLYmILCzmERBTdT3jgoxeYGpMDM2DybzkktawVDDcoZWVJPR7fxC7jlWaffGwPZz43sKv_hbfazA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسئولین لیگ برتر به تاجرنیا گفتن خب قهرمانی فصل پیشو میدیم به استقلال ولی به کسی نگو تا موقع اهدای جام که نتونن اعتراض کنن
تاجرنیا چیکار کرده باشه خوبه؟ اومده مصاحبه کرده گفته به من قول دادن جامو بدن به استقلال، حالا کل تیما دارن اعتراض میکنن و احتمالا دوباره کنسل میشه و جامو نمیدن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/84089" target="_blank">📅 13:18 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84086">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mToOB9x9qAardhrYujmwrcoN6RpqpXmAYG3KXtaBVoVRa6yTMA1yyxxknj75odsOWGGJxl8luO8PuQnZfnXah8aH6BAXvg_MPRDo0tVZWcQI58YEXkD3uxeA-fz8DaMhbN4sZ16VLov7KWrO9EKRj1KMOYa7GL0w1Cw5Qo0lTXUqZ7ljuUj95sKyzmK6YgR5EBlJOnjc7UPr2Nz6gyqvOi1jb-jyPy6DCImHnsNsfH5IwAwIKoy5rlzOA9bRZ0jfJYS8Bg75eEEA4l1YfSNZL2AV0o_ORy3-jT-IdVw0rlpmPujlvRR-Orl6c8XkRRoZPJIGE4g1JBDeSy9jFwO5gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسطوره حمید رسایی برای اینکه سال ۱۴۰۲ تو کانال تلگرامش به محمدباقرشاه گفته بود دیکتاتور، الان داره می‌ره زندان.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/84086" target="_blank">📅 12:53 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84085">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6182180c47.mp4?token=GEl-I6N5Az4yMslfGtK2mgeVEBNI-IYO8M-iDamqBzIH51g7XAHgvJi0IGc1M8mLYny_WBVXzH7rMRIAiui4R-aHbgMvKWzCdngZbIMyqJxtiXkUjmL6aaX0txc2i69wwKSUD7ib3fRMDf-NGrD4cwNG4WTMWfw133svYwTl70cFix3oTS8r3w2w0Ios2buDiQY6aWCPc8XfWNxAi0wFXYLu9kgtfIYzqPgGgMRFErhYb-S-uhoR9kFROj8RbjPHnSHkls4-zDze1qfahiNDMIqlyBaMqgIQPu1oqegm2oArHSpWs9F_FKmEVMM3OsshV6jNakRCpttMMvijP0zRXaFe1BoEOsjnOnxgQNgsoRGRDqQ7MZsrwsauNh6CWpuLxeZA8yB72YGXUYRiwNMOwqJ9o4R0QLnYKxazJLc6ORJmO5hYG7sU7iLZd2bzYH7tB-bKH33_vA-EQh5O6nVMZULec3pOWYIrTY0WJ494KERxFD-JCOnROhncpYRzy6l7h1qribXUjzMdnQLksPSheA9ofRwadH8y8CDmtyCE5JL3S0y_zfhcihIDIMtV4hXhcQbHwqTU6gx-fX_EF--QUVmVOto91DVFEPynWaA1-TSpzgAySXr1z_0ZKG2lvH3aooBTNeiXXTLuDJyOW7SUV9U2XGEXvD0TkpEj04bowyc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6182180c47.mp4?token=GEl-I6N5Az4yMslfGtK2mgeVEBNI-IYO8M-iDamqBzIH51g7XAHgvJi0IGc1M8mLYny_WBVXzH7rMRIAiui4R-aHbgMvKWzCdngZbIMyqJxtiXkUjmL6aaX0txc2i69wwKSUD7ib3fRMDf-NGrD4cwNG4WTMWfw133svYwTl70cFix3oTS8r3w2w0Ios2buDiQY6aWCPc8XfWNxAi0wFXYLu9kgtfIYzqPgGgMRFErhYb-S-uhoR9kFROj8RbjPHnSHkls4-zDze1qfahiNDMIqlyBaMqgIQPu1oqegm2oArHSpWs9F_FKmEVMM3OsshV6jNakRCpttMMvijP0zRXaFe1BoEOsjnOnxgQNgsoRGRDqQ7MZsrwsauNh6CWpuLxeZA8yB72YGXUYRiwNMOwqJ9o4R0QLnYKxazJLc6ORJmO5hYG7sU7iLZd2bzYH7tB-bKH33_vA-EQh5O6nVMZULec3pOWYIrTY0WJ494KERxFD-JCOnROhncpYRzy6l7h1qribXUjzMdnQLksPSheA9ofRwadH8y8CDmtyCE5JL3S0y_zfhcihIDIMtV4hXhcQbHwqTU6gx-fX_EF--QUVmVOto91DVFEPynWaA1-TSpzgAySXr1z_0ZKG2lvH3aooBTNeiXXTLuDJyOW7SUV9U2XGEXvD0TkpEj04bowyc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیک واکر با شکست سامسون داودا به مقام اول مستر المپیا رسید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/84085" target="_blank">📅 10:09 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84084">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kfw_ct1EcZ3Hv1S5xhRH0bnSJ_HNgeZJDOwk5gRvEks6WYNn1Yh0OL8_7iHbQ3ffHH_mjynaR_3zWwUNXfNNK8CSypdXiMoan97V_BAsny3hCy8czPgf5-WPyyNt3GL0VM6U2e75wRwtR_ExS_F1KbjgGivH7NeMH_swj8LZBmwt8pY3v4Hbsq2Y568j0xqRtr8AgQtAPy9LthvOdMLvJCNAKGpTB7LghPcKh9t_mSfG5kBxqxjuwQN8Vhxxu5Y8VyGm_Q4sDPLC1-l_L1YU4sLLODjWXc7Knw-23_XFxHdkhmNvosczyrfEOTWIxKh016yaOycATqBqpxdI_tmt7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلخون بد جلوعه حاجی
ناخوناشو تتو کرده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/84084" target="_blank">📅 09:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84083">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">گوگل ایران رو تحریم کرد و دیگه نمیتونید جی‌میل جدید بسازید.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/84083" target="_blank">📅 03:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84082">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">این باز مست کرد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/funhiphop/84082" target="_blank">📅 01:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84081">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FiAPvlzS5Am0vTVuROsBVVFjHC1fW8CraVJMS88Xk6xArb2RSb8gwqXw2snen-jZOF7GxI5zx7CwW9PW3FsemfNDkn0Vu3sL89ndxMxYD3tDIOurDowXQaFlw8CsbKHXDpoWoXTflwAm22wdeEepNjZYaw8n2tVfWWyvQDD-xmQIyvVBzHoQex7CQGa0UNkwtrdjpFTeFNZrrXZf7VgVr1rXIPyqqzJcDcJh-1RVWWXSZ_T_w_0UpudEsPHg3kB6eowfgljb867Z03Gu7ZbnL7j3aNQru4qdA8SR8ubPActOOFtrLqJ9IkxNf_uuLer-c1rPYi1c2Z2z-D8W6gF3MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپانیا رسما هرچی تیم اسم و رسم دار تو دنیا بودو تو سه چهارماه گایید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/funhiphop/84081" target="_blank">📅 00:39 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84080">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">تنگه هرمز بکن بکنه</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/funhiphop/84080" target="_blank">📅 00:28 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84079">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KukFLuohOCBkDSJMtRQjkqen9p_Jllil70YQGjYPbZlZohiTbf-E7FtHs52lV_w2h-hjy0qhXu7K3u7Jl8CMhcQxWzx-ecB0g5YCqKjxgtEKgfGeBz-S5JqP_fSRu_AZiCN8iqZx_n15HbVHnvMZBXTlk1vJGvjJzcm_i4mRwYSpn9si6TbifQ6Wh1qR0FHrMBhLW6dc81fg6j6u2jeTZub-tgS-9onWXOz8AcxdGQltQl95xA_TnrtH-H_EfCXuNOOLK3W37uWhfnWRoHA5qdAItGMIbhaEV8NmT4THrIxqI9i3jPPShAlq9rb16o6QsNz42gGYkWiTqQSIch1bmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مترو مناطق
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/funhiphop/84079" target="_blank">📅 23:30 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84078">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">کوکوریا زنتو گاییدم</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/funhiphop/84078" target="_blank">📅 23:17 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84077">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">آلبوم جدید پیشرو و تهی به نام "رفیق" منتشر شد.  YouTube   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/84077" target="_blank">📅 22:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84076">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">بابا کیرم دهنتون بچه ده ساله هم بلده که همراه با یوتوب از ساندکلاد حداقل بده بالا، شما با ۳۰ سال سابقه بلد نیستید</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/84076" target="_blank">📅 22:42 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84075">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tO2zDJzbfBgPNTdDFe32mQAuEChPYl9Qbm_k_hX-PkpI3ZGbnxuES6C7fdtNlqeiimAGSXJUN-B_CtDYhuPxkPjXlhnqefqAMAxeV3Q-0D_SrwubaGSuuc3tJ1-tPkiWsCy2VyrRnoxEM5YDcfUsSff-Lcm8hVj1Yzv5M8RsstaLjquUjq2mQ-3_lkoUuwrrNKmaxykidJH0LmZ2_bGs6YLut-ylqfHvChhUdhMEaNHpacRTZNtSUNTB1Cam_mnhix77lQWrXXqelz7AMx_0V4jPQlgJ-kb6SFCU7m1uMnGqF-IU3U7f3yBqq-l9ELwnQgiCcU3Yalo72M4K9jW_nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلبوم جدید پیشرو و تهی به نام "رفیق" منتشر شد.
YouTube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/84075" target="_blank">📅 22:41 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84074">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">پزشکیان:
نتانیاهو زورش به غزه نرسید بعد میگه میخوام حکومت ایران رو عوض کنم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/84074" target="_blank">📅 22:31 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84073">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/1a8faead30.mp4?token=XXPGzNpRFa-MAD8TpYO1p8CmRqLAwZQEWkKi5r_-lyI5NKrfPwVCSkZRT0ClM83go41Ipge0QZDL2jk1ylmEwQTCybdaDX1iNSdYLT1hsbJ6cZnMwRIO0k4zSkuqOHwjXWgqzzepMvUfrt-Rdl58oAsSy8NDF1b_zFQS99Xoqsuq20lB-hRRcly1MrtseXDM32NmyFkKEDZB2RPo5dcaY9ziv-gDqZkFecJXkvnYtYTCZDVU4eIqrTURoT9tSE2fhcTg8hSsJI8MqpFulX_P8jmzeMub-Wf4LrXJ1kjeeVPr3jvuhkMyeFNFZVaD_S_7qW92UlcSSWMQF7jnLDuLYw" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/1a8faead30.mp4?token=XXPGzNpRFa-MAD8TpYO1p8CmRqLAwZQEWkKi5r_-lyI5NKrfPwVCSkZRT0ClM83go41Ipge0QZDL2jk1ylmEwQTCybdaDX1iNSdYLT1hsbJ6cZnMwRIO0k4zSkuqOHwjXWgqzzepMvUfrt-Rdl58oAsSy8NDF1b_zFQS99Xoqsuq20lB-hRRcly1MrtseXDM32NmyFkKEDZB2RPo5dcaY9ziv-gDqZkFecJXkvnYtYTCZDVU4eIqrTURoT9tSE2fhcTg8hSsJI8MqpFulX_P8jmzeMub-Wf4LrXJ1kjeeVPr3jvuhkMyeFNFZVaD_S_7qW92UlcSSWMQF7jnLDuLYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو کرمانشاه یه مخزن سوخت خارجی F-16 Sufa اسرائیلو پیدا کردن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/84073" target="_blank">📅 22:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84072">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">گوگل ایران رو تحریم کرد و دیگه نمیتونید جی‌میل جدید بسازید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/funhiphop/84072" target="_blank">📅 21:47 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84071">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e520cf397.mp4?token=nv_ZQ7499t6pRiJhvvBeH4sP9ad8fjFFqFSYiP-XhgjqK25P6YfY00NqerPAD7uWcHlbBElOX9Jx5_ittYnutby3-dZpeOYKvusOdu254V8cbdmrGTS996y7oQ5d8gQ6db0455DRONFjQkFVnEUYtqxUNTgMJEpfa_yLaCqF5FaECb7K3n9mOlcKCQc5SMrlMaGUtJg-fPlR7lONsW2LXE-61JIM8dFxMsVlh6o2G2zPk89NK7GRSnowrpo80MWhtyOaL6D7LGCgQ78UeMNnzH9qFMEf5b8j1SF553gRS4Bhdujn1bkFsYn8zT2pB09tKrZNWnYr1fJ9V68KvpNnRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e520cf397.mp4?token=nv_ZQ7499t6pRiJhvvBeH4sP9ad8fjFFqFSYiP-XhgjqK25P6YfY00NqerPAD7uWcHlbBElOX9Jx5_ittYnutby3-dZpeOYKvusOdu254V8cbdmrGTS996y7oQ5d8gQ6db0455DRONFjQkFVnEUYtqxUNTgMJEpfa_yLaCqF5FaECb7K3n9mOlcKCQc5SMrlMaGUtJg-fPlR7lONsW2LXE-61JIM8dFxMsVlh6o2G2zPk89NK7GRSnowrpo80MWhtyOaL6D7LGCgQ78UeMNnzH9qFMEf5b8j1SF553gRS4Bhdujn1bkFsYn8zT2pB09tKrZNWnYr1fJ9V68KvpNnRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تروخدا نه  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/84071" target="_blank">📅 21:07 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84070">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D71-Yjwm5EPRNrjXVyYcZlN9Jlvup2hBp66o7VY4NCXKGFLjCS5t26IY8yiOP34o_7NgAX1t0bGji0K3VPDASw_1tacLHJOzPOaBj0ZFCF5Omb5V_CpD6VqcyPuCdxXKwcTx-sfiDUNSxuZYnwdwgbWOTNDbFMDaxgBSBI7tBvtH4_mu4uKyHx3EF7RJzQb8fF5fI159xYnOGPEZxZvjjMhihEh98YkqZ8CNV91TDaNiJwmA4emVQZyUvx92YiHW09qBuQ5VbiAuv-7SVRqOX7NlePFuhMulZzfrg9IQlO7aEymZ3XMhhAA3c41XBq5HOjx_gLZOA3371O3bZjSM5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تروخدا نه
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/84070" target="_blank">📅 19:56 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84069">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">یه مردی رفته بالای ضریح امام رضا گفته من ۱۰۰ میلیون واس زن مریضم نذر کردم الان فوت کرده پولمو پس بدید
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/84069" target="_blank">📅 19:42 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84068">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/152539b735.mp4?token=fHvNyoscfyxEwQs6_heAhIqN460vKm3mA91Xq7z8rPV3HsZelw6S1WZAJceWG11INUchThqBomGGSsY2cxwXDlquUB8JEucIV022qlpG_AcbbjHr_dq6cvv4nrYWCIyv7jZvrO0LB6tUT0noepyEyImd5bNRQbPKgZIkMOTNP2OqgPpC9yPBpM5FXAJw_i458v9f9tUl2IGjdW_QkCa5NBoVqlv5peVqYzJUG1yHBD2scFUJ3u8HEKqUZl2dAw8C7s9bgyUH3yXd_YXMEoNxti3X0DioMzQIbAbutAycbBQH7lSOh2T_jKyvMhrE14KHi6kPn1yURVYvP966dlAfErOywx-IsrGCwjjxlcFeR8bKgZaCbJpdQzb8BsmBcvGKWkH6ppQ2t0VEfvuVEELtXfP_MfD5OJ3hdFGiqK361TPPkeQsX-tlTKXHdUCjOuQdeACKhwEaEhO2NOfeVporEffQcQoYpOv3le8X0OlkItKGS3ry92RnmVHD147EuNwSaPOz_TMG-by74TvwwxCvvY2ttYQES7Rhn9hKPdwGap_6o_X5ejHWmHdC_xiBd6SbgajPGv1qTPQ2ogVMXp3FCmX3oYBbX2wGjj8Hevgi4_-Ujcgmti5XiyJRTiUbvv-J6kT3FfFl7f9j_EjGux1YnwaNNrxhpTjPsoj_oni75L8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/152539b735.mp4?token=fHvNyoscfyxEwQs6_heAhIqN460vKm3mA91Xq7z8rPV3HsZelw6S1WZAJceWG11INUchThqBomGGSsY2cxwXDlquUB8JEucIV022qlpG_AcbbjHr_dq6cvv4nrYWCIyv7jZvrO0LB6tUT0noepyEyImd5bNRQbPKgZIkMOTNP2OqgPpC9yPBpM5FXAJw_i458v9f9tUl2IGjdW_QkCa5NBoVqlv5peVqYzJUG1yHBD2scFUJ3u8HEKqUZl2dAw8C7s9bgyUH3yXd_YXMEoNxti3X0DioMzQIbAbutAycbBQH7lSOh2T_jKyvMhrE14KHi6kPn1yURVYvP966dlAfErOywx-IsrGCwjjxlcFeR8bKgZaCbJpdQzb8BsmBcvGKWkH6ppQ2t0VEfvuVEELtXfP_MfD5OJ3hdFGiqK361TPPkeQsX-tlTKXHdUCjOuQdeACKhwEaEhO2NOfeVporEffQcQoYpOv3le8X0OlkItKGS3ry92RnmVHD147EuNwSaPOz_TMG-by74TvwwxCvvY2ttYQES7Rhn9hKPdwGap_6o_X5ejHWmHdC_xiBd6SbgajPGv1qTPQ2ogVMXp3FCmX3oYBbX2wGjj8Hevgi4_-Ujcgmti5XiyJRTiUbvv-J6kT3FfFl7f9j_EjGux1YnwaNNrxhpTjPsoj_oni75L8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ثمره های اون میلان رویایی ۱۹۹۰ تا ۲۰۱۰ دارن میرن دانشگاه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/84068" target="_blank">📅 19:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84065">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">حاجی جیبارو بچسبید پیشرو میخواد پک فیزیکی بفروشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/84065" target="_blank">📅 19:18 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84064">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tF0XA3pxPkofLJr9Aw2KkwCNx9llCeVXbySbqBddl78qpXgmpdizBAn-pKyDXatH7t9Ym7X7o39KnsWU7sJCpyP8YAaQWpR8g0j5Xo1QRvy00cGaoGvwtszxOu5arS56ofHNJC0_oDw83C8dFQQMyNSZBerv-mW4pI7i-hutXAkJcuQ_3SA7R_9P_DdKh84UFGn_3VM35TmNRf3DmDzkzXZvrnfHU4Deb_z23zJioFBXTkkUDUGroYn3-iGAqUqZiDx1ri8z9GARswf_b8SsZB4mhV7wPcKqu-E1Lp9DZ7DMi63MjMGwSk1EaQkDDYqt1zv-GfOfQbzgJlKrpLIe9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تورو خدا یچی جدید بگو پیرمون کردی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/84064" target="_blank">📅 18:31 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84063">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">رضا پیشرو و تهی امشب آلبوم میدن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/84063" target="_blank">📅 17:07 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84062">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uZpNKkgOZ13fiRIw3oAW_vvskrg1iweuma0arwrqdyiILdO99NfcursJCTyBEpqIKGoghVA0tz5XNOPrsAWmgiSGXJRFglrtyWFbHU5jS4auQIRWnUqxP7QGCZwGi_uxWh5x1B8xH1IAak-QNvq9utMP_OAg4b2EL1MCl8WrfCe9dW1oGUyDZ_--O2CUn48vMVtUo851GKkbpONSvt5idS3t_rX9JPMhjv4XRn8RuMsPYiGev1xCoE9epcGyTHfYGLgxjfuByItq6AgpOlqg62xnGTpm6KT-Sxo9XWuCweJe0LuH6z4w5W55ZAhZCteyk2Zmcj0Q_HUdwHlv9-jy8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست بسیار شوکه کننده و بحث برانگیزی که ترامپ دقایقی پیش منتشر کرده است.
طبق بررسی و تحلیل‌های بنده، حتی احتمال تعویق هم ممکن است وجود داشته باشد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/84062" target="_blank">📅 16:28 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84061">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">داریوش تو فری استایل جدیدش تحت تعقیب کمپ اعلام کرد بالاخره ترک کردههههه
🔥
🔥
:
انقدر پاکم می‌گن نشیبولوسعتاااان
🔥
او همچنین در ادامه‌ی بیف قبلی‌اش با هیپ‌هاپولوژیست، به او چند تیکه انداخت:
کونی، دکی فقط داکتر دِرِه
🔥
راستی فکر نکنی لندن پارک‌ها سیفه (احتمالا به دلیل افزایش جمعیت مهاجران غیرقانونی در انگلستان)
🔥
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/84061" target="_blank">📅 16:14 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84060">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">اونایی که فک میکنن سیتی جریمه میشه یا قهرمانی هاش پس گرفته میشه، یا نمیدونن شیخ منصور کیه یا هم ایکیو زیر ۶۰ دارن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/84060" target="_blank">📅 15:54 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84059">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ری اکشن خنده بزنید تا من یه جوک پیدا کنم و ادیت کنم اینو.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/84059" target="_blank">📅 15:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84058">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac6696481c.mp4?token=F9Sd1XCimVAJlXALBRuL0DTML6sxKaDrH9A-V43XFkau27G_5WMGLhz3F_2fm0d3flLUB1kWl92fmmaOy1UhmDhZegVEQ-iCzLOjafOToxi5Z9wqxLwmJgGqWBDQJzbqJ-Fe8xWPnemw3lrbMg5eGmIwAn57yOAnJkFYkkOVB0K4gMOsFS83PctoYatpeZUp_sQtzEq_fA-afuEImdAlCx-UzGbj40sd4W7y98-lOfDSVj0DLHf-tYILxkLl58_2clgdBcC1dPtteFIHvMEpWd5czJSC5uhgSKt3_83K0EAjHULdCFCvlalpb9cnfnMokjI2bTQ4mfaa_54tOCOFAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac6696481c.mp4?token=F9Sd1XCimVAJlXALBRuL0DTML6sxKaDrH9A-V43XFkau27G_5WMGLhz3F_2fm0d3flLUB1kWl92fmmaOy1UhmDhZegVEQ-iCzLOjafOToxi5Z9wqxLwmJgGqWBDQJzbqJ-Fe8xWPnemw3lrbMg5eGmIwAn57yOAnJkFYkkOVB0K4gMOsFS83PctoYatpeZUp_sQtzEq_fA-afuEImdAlCx-UzGbj40sd4W7y98-lOfDSVj0DLHf-tYILxkLl58_2clgdBcC1dPtteFIHvMEpWd5czJSC5uhgSKt3_83K0EAjHULdCFCvlalpb9cnfnMokjI2bTQ4mfaa_54tOCOFAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/84058" target="_blank">📅 15:17 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84057">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cd947a5c3.mp4?token=ck_UAAyxxLBhugnCaeM5Xhl2rFnVaqvRPyGrf-M98w6pc07r3nHm7dveYkaFg2vX9gi9B0xl1cDF5_KIbCZHLt3q2Y576tqJyr8-IzbsmVonLE5_w8Id3lEv8ooNr2DQhzurhA_dwyWQ25gc8p16PZEHq3cB40p_XaEdAb37qNevNPEQykoStJHbN6UGkC8QXVvGJ2MpaBx7fgg_9wEk6-hIp-ve8mN5Rja4-QNplBhu__O1FOGSC5gbgVexAKGUB3rHjhtEXbQMErlgdlDw5dULfiNzzts_aapjAu7fOr3tzR1Kf1EZXIaZDWHEzp-OkUn_ZIvSP4Ar0ZtA9f-x9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cd947a5c3.mp4?token=ck_UAAyxxLBhugnCaeM5Xhl2rFnVaqvRPyGrf-M98w6pc07r3nHm7dveYkaFg2vX9gi9B0xl1cDF5_KIbCZHLt3q2Y576tqJyr8-IzbsmVonLE5_w8Id3lEv8ooNr2DQhzurhA_dwyWQ25gc8p16PZEHq3cB40p_XaEdAb37qNevNPEQykoStJHbN6UGkC8QXVvGJ2MpaBx7fgg_9wEk6-hIp-ve8mN5Rja4-QNplBhu__O1FOGSC5gbgVexAKGUB3rHjhtEXbQMErlgdlDw5dULfiNzzts_aapjAu7fOr3tzR1Kf1EZXIaZDWHEzp-OkUn_ZIvSP4Ar0ZtA9f-x9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخیر.  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/84057" target="_blank">📅 12:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84056">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/534ba3e4c1.mp4?token=mZW4zlVvGFstCTV5HgO6R_QEBoMpbsH4mFDZaQOnk1q5zlO-02T8hQ7MJdBeG4JX7fZdry5qkPIkv3mZJmo3meFA1BJhSHQvgn4RM_hyTF8N1Hh6TT36aQen2RaFBUot6uvLGTJuAWQCCXFEbcH8V2K6tkp-JTAc2Tct9kpMW43t1XSxxpBbkj96iMJ14qw3O0IbroG0x1VMoro6YYp8Eh8vnTqHqMm0Gfnd10vfVrs4cgxhdR8iht8E3bl0VSPHsHxe3NGZN6Gwl5BGaBjUtj_JXOXB2n3NgocTO8yUV4YFKSRTAJAKo7kRzmQ-g1F2pnE8aFBzoY3uV0DMREMK-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/534ba3e4c1.mp4?token=mZW4zlVvGFstCTV5HgO6R_QEBoMpbsH4mFDZaQOnk1q5zlO-02T8hQ7MJdBeG4JX7fZdry5qkPIkv3mZJmo3meFA1BJhSHQvgn4RM_hyTF8N1Hh6TT36aQen2RaFBUot6uvLGTJuAWQCCXFEbcH8V2K6tkp-JTAc2Tct9kpMW43t1XSxxpBbkj96iMJ14qw3O0IbroG0x1VMoro6YYp8Eh8vnTqHqMm0Gfnd10vfVrs4cgxhdR8iht8E3bl0VSPHsHxe3NGZN6Gwl5BGaBjUtj_JXOXB2n3NgocTO8yUV4YFKSRTAJAKo7kRzmQ-g1F2pnE8aFBzoY3uV0DMREMK-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخیر.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/84056" target="_blank">📅 12:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84055">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">نمیدونم این چه مرضیه رپرا دارن، اونایی که تا سگ نمیشناستشون عالین وقتی معروف میشن یه گوهی میشن اون سرش ناپیدا.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/84055" target="_blank">📅 12:19 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84054">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20a8e0532e.mp4?token=rN3c7mvdQNkS-COxgRAOldue7Ri-V1hIbI5hfYwvPVf_NON_f2jlbjD7Dnx2VyB3M_OQ3FLEMrAu84y_MZ0e1VvVvgBeEx7IIEP6243K7TYugFrfB6uuD5YOc6vHzySIxAwzMUR3qWcU6Jen6j2Ro9l_eSJSEHA4RfZSqWh8MoGtsmkXlZHMNFPoyOIBiagFTiJ8zJIC92vm8vwVN-j1feVHOO2YO0xTwsRkMrKy0mS8RLLU3TsT33UCPjQgljoK-3U8xg9bAdE228YHmM8l1BZaq8tohhFsy05_8hZmh_3ikgZ48xlISgKZPzyWZtUtJ1cxluPbD6CQ4y7Ojz_90Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20a8e0532e.mp4?token=rN3c7mvdQNkS-COxgRAOldue7Ri-V1hIbI5hfYwvPVf_NON_f2jlbjD7Dnx2VyB3M_OQ3FLEMrAu84y_MZ0e1VvVvgBeEx7IIEP6243K7TYugFrfB6uuD5YOc6vHzySIxAwzMUR3qWcU6Jen6j2Ro9l_eSJSEHA4RfZSqWh8MoGtsmkXlZHMNFPoyOIBiagFTiJ8zJIC92vm8vwVN-j1feVHOO2YO0xTwsRkMrKy0mS8RLLU3TsT33UCPjQgljoK-3U8xg9bAdE228YHmM8l1BZaq8tohhFsy05_8hZmh_3ikgZ48xlISgKZPzyWZtUtJ1cxluPbD6CQ4y7Ojz_90Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مراد ویسی: بعید میدونم مجتبی خامنه‌ای بیاد بیرون؛ بنظرم مجتبی خامنه‌ای تنها رهبریه که توی تونل رهبر شده، توی تونل رهبریشو طی میکنه و توی تونل رهبریش به پایان میرسه.
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/84054" target="_blank">📅 11:31 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84051">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lw2QLWrMeyASHgvgYU9sEXUsKUz4DQRUxVNqsNjLM9T-vYmdTNRvnMw3A1mjHGOSGODr2_V6l1jkpqMX3HK9Cg25D1aWEPKQGBsj4Y7fQZCpoWw1lSj1rxJvX8O4daRsLj_fOJUeJgQQLBI_rRwPh25w0C10pw95-J3bjlAUJfW0hLYCs0cQ-Nsxf1ULGIZOl57MWExi82E2C1JMX9F1jB3R0VGb7t8fDC0X8hmzckXNoIDNbRc9HAbFg3HEY1DwEDIaAj5v7Shf_M8c1COO1AQEGKr4tQz3glOtuLQSuDXBBLG8bgxWHNVicutZ8rD0YwTK_Mu8-ZHLAO0_j7ZCXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UfVJRWpAq03IFkgZ9fCKKZRozk6FypOIvojRLJBFF4jRMFz_NoxzWkiEPdghaquzgTGLkdeIaD1oyo60mVrEeKTOlCWebOBsx0n89lTWarXP0xmbfm5rjSA9JS5GvropQbzQbWPxgB3mVCS5nXgQwKHkWvdHX4TcWLvPRr0QIse2d3ETzNaeuoy3Iz47KxCGSG1MA9-paGNWyU7vmLRrWCvlrerJ_j02pxKwYOjx_Uoy0snWIjL-Y0M0YaWCnJbldcimkSmxoKk7UtN9n3nK_8msXeTocOUKE27mO7d0iESfvAESkpttu4c161AHd9eOKbGeuj8a6aLYMOoN8nav7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bGecPFQpiIHmyMbwGRLPcEc_OKhcUTxkXvqsvR_Ptpu5F-JnfrH_FXTtf4tz3iA7eTSsCJTAJ_oDDSUJc04YgDWJ8aXes4yknn_gpRWFL_H3fO5EretCHgb0AEBxWBkkgyKFp_E82fWv750FaU-hJeSnHlOnmALqun0kOEhcHoTr5RI6SigBGQrve1wkDfTWjwjHnbag2MsqYfoA8LPcRmg-WCtXkMqUZNzkeRZ7JKsR2z3eZO2PRm-b1bCenAbPQldUpBzAYd9vW_pjkZbQyPQmaKZSfCbhAHEsJlr1t4e1gVrHqLg9hQCoVI5DwlhvsLe3Cd5quD_DnlPG6Te2hg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کیت بازی آخر بهترین بازیکن تاریخ عجب چیزیه
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/84051" target="_blank">📅 11:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84048">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cKP1oVnJazr9KVxeAF0H9PynRja7O70iFwVK6NonMl0NOSso3hdzTj0fTzQnkPbhAb8UlrD7b43EIyMy2_vopiP5-iz2SiWxiojiu5gNw95yXJipEwNhKgYElGau0iva6w4WBpf4IalCl9QsD3xL1LsjDgEiFvgLmVvIEP-0ljwk-8fdAiVoJyXBRJHuu-ZhhH3AX1icVXiV_364QX_Ad-08uDj8psL1CUGvc3-8XlieAa93F8H-vWa9f2ddUpwszbxYz5QIBv6GheNgCLUJxrP6JbVkxV_x91Jpw1601BuOckm_8QC0qLPRv93sMlvPq8nXdX5R4L-Uu2BW2Vb8LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماشالا شیر، ترکوندی شیر
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/84048" target="_blank">📅 11:09 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84047">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/729ba5bf0c.mp4?token=mjy4xpQ4MfEJ5dkZ-61vfDolomYVU3zZYkhFMoYq4-yPsFWtKJMwbm0A0AsV06UXTQm9Ci8ZKFbd9GiSbnwFa9PWALqUSWPFdBhTW29FwFr-wwiUDWGoDstTb9wZPPqqf2QCxOewKO1ao4U1b5m5m8V4Tz4dm7BCjpxVe49V_DuTdSSMVe8AipvHOBl-QLu7q2wsuEYYFEGKciu-ODop4nQVMbnNG7r22LWshpR0d4jZf5dHdT1tGslUpQ95eT20hmCTqgpzv6_XrEcT34E9QajSfRyIod8y8rQ6crtj4DQBatZx85l0vViKTrb6prOrzAX-YF8rNREdOXgmn3-wgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/729ba5bf0c.mp4?token=mjy4xpQ4MfEJ5dkZ-61vfDolomYVU3zZYkhFMoYq4-yPsFWtKJMwbm0A0AsV06UXTQm9Ci8ZKFbd9GiSbnwFa9PWALqUSWPFdBhTW29FwFr-wwiUDWGoDstTb9wZPPqqf2QCxOewKO1ao4U1b5m5m8V4Tz4dm7BCjpxVe49V_DuTdSSMVe8AipvHOBl-QLu7q2wsuEYYFEGKciu-ODop4nQVMbnNG7r22LWshpR0d4jZf5dHdT1tGslUpQ95eT20hmCTqgpzv6_XrEcT34E9QajSfRyIod8y8rQ6crtj4DQBatZx85l0vViKTrb6prOrzAX-YF8rNREdOXgmn3-wgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لطفا همه خفه شید فقط ایشون بخونه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/84047" target="_blank">📅 00:38 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84046">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dgy-X3fzJ2wxgVmLslk2JTDCPZ-CSvvR_a1kx0WmJ0vIDNzeLUJ2cCQnDz1BFJm3usA2ny3YmnPYpukRKRzEBeb8Qv42k4bE7G8cPfzd0IuWobOSLNFHQ0RnzjPqRvGQD9zCWGXhTNJ_a9VnqUOtkJrgI98271ac-ZAM-_E28QbCMd9Xv5qVXiC1ajSAZJAgJe6Fx43aAkO3u2NH3KSr6xEnMptGX9NeaZtPdca3grtvuqwxeyuhE58b0bNnJjKtKVRhPk1Z2KIhSYSLMPEjBcu2-zcaCFyBlYQYPYnScWqefjht_NSztwh_TBCd5FOSbRqNQ_Dxmz9PsIGdoZrXkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خستم کردید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/84046" target="_blank">📅 00:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84044">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LmJ1WT3HZhQqQUjFyw-3SMMEQKI6pIiTjCqg_uaKeqaPmGfd9VOv8qNZxWYL8Zswm9OapDmdDhntM9zRAVlue8PtXVNIqzPR_yGwMPxGBwIIpAm1m_l_DakdYq7nqUh4LaCN5ceFG205V4I1Qur-XGJHhs1Umv6H-lCxva8DEj97mB_L4LqCTEf8YP0Os8Y-w1_Zrk4h2mACwqBqxbMAOCiI1c75Z1Ax7IPKYYzjD1_YnutxB5DitdfcQwV1GA5Jo-Y_V22mOTW63usmDCOyKlN9NoWTBx63mSNRIdwZAHGXMshJi2g6ihQFQ-Gc0vquN57lUjftsegXBaTBZlJgqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/di9urMgCqWOrlRaFbdXBtOzgt0Xk0GVecMP3vOpp8YDHdbTr7zbms1KeY4MA_Rny17mzZI3vxcvXmSEixN8lnWri-LOabQhYYwW1z36XKlGO-iFjjD0XbRou4t4jVTBQq0eMKM_Rx75GIoSMUcyfyDvlDbp82wGHgTnvFwUaLv1CHvQNMOk1eerykWxSwxuCUo5XIbPwsGn3GMEBoSsostP-ivOkGQJoRlrVBX7LUkK2tmbomoQ4MG_s8gx2AUJs4xse6lOsHE64pu-XM6qCMhwVqVPHnMPEqkGsa40w7Lhe6MpJrVhFvWcd_ts3_EgpwC7tNvMGvcbRL4jZDGtcig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فقط نزنیم حرف خالی
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/84044" target="_blank">📅 22:54 · 03 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
