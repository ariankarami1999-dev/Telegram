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
<img src="https://cdn4.telesco.pe/file/FloiBnAlff_ltE4z97atjFzytzVqwArVVCGCNmy7ewBXzpfF1bmYR_mT9YOK2qy435b4GwvFlrNUzXsfFh-Q43Nmfrg12GVJfAWawQvWByqJtxT-CKUaR9PdlqovcQAJErEWcz05ZgyZ8mqkK2mKXADBOG6zKKqzpIlXImbdCab3eo-wS_ytqC1t-G3Ns5U6vCgIDO6vkzctoP7mRSe0_jaH8DAlKkaJnXTjOWXPGHw40jgq8tBaBmxcvopNmJOBFElDkuLRF77DojB2TagV-SKlSX3kDi-8St3phBQr0hN_aikQXxMfp3VAP16e4eP-nu0rXczt_LyYmJu3HhxSEA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 105K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-11 21:34:41</div>
<hr>

<div class="tg-post" id="msg-72694">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7af7d5f80.mp4?token=isycbWZWYXVuDVOvPuYVhqhgeh8kmYArSixG8k8ULNQbFk8HLg601mX-ioJ7eD8JaO72xTkqGGrV7LFrEz0Yks1xz8HQnRLybColpFaYP-bCB1_xNMUUCptjRydJfxvyJyrXhd2fHY4Q1BUYyKvm8S2Q3ICC9dvPXkw8qWibGCsNHK5ejXZUIQU2Kxk_NrZLFHDvzAK5XdFuZwvi3o5suUS8wwRFY9sm-1HvoYrExFl2ER-sEFFJvBv-N-ihA2PfYf78EUTXLimKpvNNAwfxqTIdFXaMEE19piANPHIETd6ZD4bu8QCG3aC0wUFQ9qSgkLQIPwmWUHx-jiUSW-gsbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7af7d5f80.mp4?token=isycbWZWYXVuDVOvPuYVhqhgeh8kmYArSixG8k8ULNQbFk8HLg601mX-ioJ7eD8JaO72xTkqGGrV7LFrEz0Yks1xz8HQnRLybColpFaYP-bCB1_xNMUUCptjRydJfxvyJyrXhd2fHY4Q1BUYyKvm8S2Q3ICC9dvPXkw8qWibGCsNHK5ejXZUIQU2Kxk_NrZLFHDvzAK5XdFuZwvi3o5suUS8wwRFY9sm-1HvoYrExFl2ER-sEFFJvBv-N-ihA2PfYf78EUTXLimKpvNNAwfxqTIdFXaMEE19piANPHIETd6ZD4bu8QCG3aC0wUFQ9qSgkLQIPwmWUHx-jiUSW-gsbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو بمب‌افکن راهبردی رادارگریز B-2 Spirit نیروی هوایی ایالات متحده بر فراز محل برگزاری مسابقه تیم‌های نیروی دریایی و نیروی هوایی در «کلرادو اسپرینگز» پرواز کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/news_hut/72694" target="_blank">📅 21:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72693">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/24bef6628d.mp4?token=NXUufTkOyrjrLz7OFnMgNgz0p-OY-1Y4hwn9IZkBdXz8naGyFhCB7rwmqmGzl_YqaBHuZn2MIY9xP5zLS7xNm-5oBic2B-tLFI_2rEqxvubt077OZnVCUM1fi6QUPIqcb-TQDAAe6G3Yq5saRVwsQoNLOYRiLKrg-OtmesLgzHBGtwQvvPoRnnnF2ifUGYpeuAejp-2nzM5Oq_a6ieQV37dYC_eSTYEgWFaN3-FG6W5XOieceQO2ZCFHSOer77-G2_w5Vp11xKGL1TI40H9yCAC__kYAOb_fxs98jSBxJs4N52VbNZPk8JtNeeEdzHQiHIXfGfvZpRIfXgo4EnNffw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/24bef6628d.mp4?token=NXUufTkOyrjrLz7OFnMgNgz0p-OY-1Y4hwn9IZkBdXz8naGyFhCB7rwmqmGzl_YqaBHuZn2MIY9xP5zLS7xNm-5oBic2B-tLFI_2rEqxvubt077OZnVCUM1fi6QUPIqcb-TQDAAe6G3Yq5saRVwsQoNLOYRiLKrg-OtmesLgzHBGtwQvvPoRnnnF2ifUGYpeuAejp-2nzM5Oq_a6ieQV37dYC_eSTYEgWFaN3-FG6W5XOieceQO2ZCFHSOer77-G2_w5Vp11xKGL1TI40H9yCAC__kYAOb_fxs98jSBxJs4N52VbNZPk8JtNeeEdzHQiHIXfGfvZpRIfXgo4EnNffw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از سیلاب شدید امروز عظیمیه کرج:
@News_Hut</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/news_hut/72693" target="_blank">📅 21:06 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72692">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">به گزارش نیویورک‌تایمز، مقامات بریتانیایی و آمریکایی معتقدند افرادی که در نزدیکی پایگاه نیروی هوایی سلطنتی «فیرفورد» (RAF Fairford) دستگیر شده‌اند، با عملیاتی تحت حمایت ایران — که یا به سپاه پاسداران و یا به یک مرکز فرماندهی نظامی دیگر در تهران مرتبط بوده…</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/news_hut/72692" target="_blank">📅 20:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72691">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b1UluoE1fIeU3E_Z8BaSNzkxCQFPtAShm8_FnGCUbt8wlv32Hjkz8KLbFhF0b-hgSVdfrGNVY0R_O4G6wSeqVMQi-G8EvOn9erXh4rnXfpJ1S_m6JYwcLv_V9V3UuvCwXrqXJ49_ClQEVm18s_FeK8U5XEL7zBPKU-dhcQmLHsJQDLlFMP6kPjFLTIqsgzPeCPviWOeInIK796cCGoidqG1T1muXRl2RTV7UhzsV6CZDuMOlKn0-RKkMQMpmnThCpLe0dsVA4uZ55RUZuBHW9JC-nisU9aiZswW0sdlSBmqEKLrhHQLpzXfriQeWBngael-VNOxG37GbJh4SA_iLZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش نیویورک‌تایمز، مقامات بریتانیایی و آمریکایی معتقدند افرادی که در نزدیکی پایگاه نیروی هوایی سلطنتی «فیرفورد» (RAF Fairford) دستگیر شده‌اند، با عملیاتی تحت حمایت ایران — که یا به سپاه پاسداران و یا به یک مرکز فرماندهی نظامی دیگر در تهران مرتبط بوده — در ارتباط بوده‌اند.
بازرسان در تلاش‌اند تا هویت فردی را که این افراد را به خدمت گرفته، شناسایی کنند؛ کسانی که یکی از مقامات آن‌ها را «افراد ساده‌لوح و بی‌خبر» توصیف کرده است.
با این حال، مقامات اذعان کرده‌اند که جزئیات مهمی از این توطئه ادعایی همچنان نامشخص است.
@News_Hut</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/news_hut/72691" target="_blank">📅 20:18 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72690">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">دونالد ترامپ به تمام شهروندان بزرگسال ایالات متحده وعده داد در صورتی که جمهوری‌خواهان در انتخابات مجلس‌نمایندگان و سنا پیروز شوند به آنها ۵۰۰۰دلار خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/news_hut/72690" target="_blank">📅 19:56 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72689">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a49047dbc.mp4?token=H13V44NoUsl2gehIE6YjTum7zNZX6erH4BE9XkmKMfyaHyNmphbuNOMyqA09jMNV3hLd9jap0Ar35DJDNnsmu605JQA8JVcZc0pwmtQyi15bEo7Trhf7Hm8fmcnNVGnWAzE4hrX73TWmY1zoCvmIAIY5dXWIYM1N3l_WsPtua1leipeb4GoHnAH8q2bv0BhMa1PdFf6W-l_Qc-qSsqWrtm4hbQwIWvEra5hmZelSRoEE07JB-RkYVRb5rdHMlDRG0IWPAWx3xvsSg-lvRBVvz2zdkSDMtxVrWJIoj4B_D9bVvBDXpRtuh-LU81c0zSXVJ5vMxwR01YCY4LowCoLcx75gObLxRAJ53hwe1kJR9pSwWovj9nfS5ay0foUR3LcUy8affv8TnDcEcG0CWwQM4Eql29lmL5msxyVHvGHxsfzOHeY2VbKOLL5J-3oR-by8Z1dnuwqsbMKAYawR7CS9JVYofwRQf9UVQH_0rDWJopTG_kt3fc_bHY4Ly3P644cydhPb6SxKkRRqO0wBtvAa2kyzqzaAo8l1WChpnAVhSEd2ruC889XD4Ci1jhu5XIlaa57wiQhblN8B2PiEPC_Cw6hx3q5Mw5iD1C4wwhmjXEmJ8PvxWv35JVXFOljY3-w_BaIPco5uSKzVhi4mAEODyBa7OOmqczjCXGKbc73Gf7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a49047dbc.mp4?token=H13V44NoUsl2gehIE6YjTum7zNZX6erH4BE9XkmKMfyaHyNmphbuNOMyqA09jMNV3hLd9jap0Ar35DJDNnsmu605JQA8JVcZc0pwmtQyi15bEo7Trhf7Hm8fmcnNVGnWAzE4hrX73TWmY1zoCvmIAIY5dXWIYM1N3l_WsPtua1leipeb4GoHnAH8q2bv0BhMa1PdFf6W-l_Qc-qSsqWrtm4hbQwIWvEra5hmZelSRoEE07JB-RkYVRb5rdHMlDRG0IWPAWx3xvsSg-lvRBVvz2zdkSDMtxVrWJIoj4B_D9bVvBDXpRtuh-LU81c0zSXVJ5vMxwR01YCY4LowCoLcx75gObLxRAJ53hwe1kJR9pSwWovj9nfS5ay0foUR3LcUy8affv8TnDcEcG0CWwQM4Eql29lmL5msxyVHvGHxsfzOHeY2VbKOLL5J-3oR-by8Z1dnuwqsbMKAYawR7CS9JVYofwRQf9UVQH_0rDWJopTG_kt3fc_bHY4Ly3P644cydhPb6SxKkRRqO0wBtvAa2kyzqzaAo8l1WChpnAVhSEd2ruC889XD4Ci1jhu5XIlaa57wiQhblN8B2PiEPC_Cw6hx3q5Mw5iD1C4wwhmjXEmJ8PvxWv35JVXFOljY3-w_BaIPco5uSKzVhi4mAEODyBa7OOmqczjCXGKbc73Gf7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست، وزیر جنگ:
مرا بفرستید تا با «کت‌قرمزها» (نیروهای بریتانیا) بجنگم.
مرا بفرستید تا با کمونیست‌ها بجنگم.
مرا بفرستید تا با نازی‌ها بجنگم.
مرا بفرستید تا با اسلام‌گرایان بجنگم.
@News_Hut</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/72689" target="_blank">📅 19:30 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72688">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bc7b08156.mp4?token=YfVEQCNM6FBPsKivWEihhvqNX6DSf0CmKgzXcVE5yCZoLIsDQT1dT3NPBNRqDinjfyNC3Phx69peiO4kWjb3Tu6E8hOwTbRKwjmlegz19b3qVNRVboqnL80XdTniAtijpPSf07Acqe2pC_Fbeh417f7BE55C0p7szdcEnvGfoiPJd6LE85KR-1xae1TWdBQdZ55zakyTD7mtpHBGl4mQg6TM3g4LslLJxqDfwqK1LZ6up-t8y1YGY2FWcP7WdxN5ntlWsweo3_3Qztogqbqy4VFuI4K25Zx4dSWmW9zSYui4xXuAcqdwDA6XjufzEkLvIOOAnnm7RVb3uzFhbTvzeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bc7b08156.mp4?token=YfVEQCNM6FBPsKivWEihhvqNX6DSf0CmKgzXcVE5yCZoLIsDQT1dT3NPBNRqDinjfyNC3Phx69peiO4kWjb3Tu6E8hOwTbRKwjmlegz19b3qVNRVboqnL80XdTniAtijpPSf07Acqe2pC_Fbeh417f7BE55C0p7szdcEnvGfoiPJd6LE85KR-1xae1TWdBQdZ55zakyTD7mtpHBGl4mQg6TM3g4LslLJxqDfwqK1LZ6up-t8y1YGY2FWcP7WdxN5ntlWsweo3_3Qztogqbqy4VFuI4K25Zx4dSWmW9zSYui4xXuAcqdwDA6XjufzEkLvIOOAnnm7RVb3uzFhbTvzeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست، وزیر جنگ:
اطلاعات نادرست، اطلاعات گمراه‌کننده و تبلیغات عامدانه‌ی بسیاری پیرامون ناو «یو‌اس‌اس آبراهام لینکلن» وجود داشت، اما ۸۰ درصد از کارکنان آن گروه ضربتِ ناو هواپیمابر، برای تمدید خدمت خود اعلام آمادگی کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/72688" target="_blank">📅 19:22 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72687">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cee4b7ed20.mp4?token=QxL_eBx2Zz46z8_YtOiU9V3yjURNbTJXqOocetKl5RUQQOtUukelbmpZ9HZ9OScXfgwNHqSa1MQ8YNHRAHIAKXOWJ6QFMqXQyMrYII2LWWWMHbPYwYHDdyIQf0d6ZOtrdUmql04ybqM3Jlgf_6HPPcvDEB6CUAMQSoqc2735kPua5PpiZPp_qCjlj9FxONe5vwLiM56WChMdRNtISSvVq4BJnH3ZDIzdRxrUIhFJLWqmuXPSwRTnA1N0emd6w2KTgVljB8WNDC3zQj8D4wAJPnOrGrp5fVsPepfWuY5M64TseKRwkMS9k_gda_S7LNfwVlTGEgxAAUpVczK9eVYTGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cee4b7ed20.mp4?token=QxL_eBx2Zz46z8_YtOiU9V3yjURNbTJXqOocetKl5RUQQOtUukelbmpZ9HZ9OScXfgwNHqSa1MQ8YNHRAHIAKXOWJ6QFMqXQyMrYII2LWWWMHbPYwYHDdyIQf0d6ZOtrdUmql04ybqM3Jlgf_6HPPcvDEB6CUAMQSoqc2735kPua5PpiZPp_qCjlj9FxONe5vwLiM56WChMdRNtISSvVq4BJnH3ZDIzdRxrUIhFJLWqmuXPSwRTnA1N0emd6w2KTgVljB8WNDC3zQj8D4wAJPnOrGrp5fVsPepfWuY5M64TseKRwkMS9k_gda_S7LNfwVlTGEgxAAUpVczK9eVYTGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگست لحن و رفتار ترامپ رو تقلید کرد و چیزی رو که ترامپ هنگام پیشنهاد این سمت به او گفته بود بازگو کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/news_hut/72687" target="_blank">📅 18:36 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72685">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdd7350ab9.mp4?token=mnfAWjUCwsBltOs4t4_1t61NCKTfW-qa8z6wpVMzQpU24-PGBnZ-g4sK7gJMd6CNVv_AH3mBFpgUiS3hcIS5eAsAijoTOhYDUXvJdFX9WI60KyP64JpddY9kyYelxs0p7KAEO4a03MbZPysnEtp4pV1sd7rSWSTkl3JhLJOn6HbnIV2KByPiYFhm0glOQlNrdfzNGvGUpekPqeoJOsIxNIG-0C5ToWwfpkBmV7mC7EQ8miHbW3cqdrHmormEoKZ-kQufUGYyzvwzaARDohdPeaRXonHV-oiYj_l645fSCguXBMQoUH7Gmz9MzWHElKTdnQVTW_tiVQIWs4KztjE-NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdd7350ab9.mp4?token=mnfAWjUCwsBltOs4t4_1t61NCKTfW-qa8z6wpVMzQpU24-PGBnZ-g4sK7gJMd6CNVv_AH3mBFpgUiS3hcIS5eAsAijoTOhYDUXvJdFX9WI60KyP64JpddY9kyYelxs0p7KAEO4a03MbZPysnEtp4pV1sd7rSWSTkl3JhLJOn6HbnIV2KByPiYFhm0glOQlNrdfzNGvGUpekPqeoJOsIxNIG-0C5ToWwfpkBmV7mC7EQ8miHbW3cqdrHmormEoKZ-kQufUGYyzvwzaARDohdPeaRXonHV-oiYj_l645fSCguXBMQoUH7Gmz9MzWHElKTdnQVTW_tiVQIWs4KztjE-NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت آب‌و‌هوای قم رو ببینید
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/72685" target="_blank">📅 18:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72682">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/po2b2gf0qMuyYpObaeOByn_gzPlDu9at-8n4a7hFPBBhwgGpZ1rW-st7n6zyLJ030qCrrNQVkWbAj4HRdIBjq42ebZ6oASRAqezakZ-oT5B6NE8Op3IemTbnUii5-z91QBu2hh0K9pUqAY8UpEi4z2c84fMOk7ClCIDtkZmBcpX3jVyoSToF7tnCoNhAMSPBcw6K12fEJfLYdIhdQDizpahOXADNl5Mw8VgUZNO76KY7dr2d3FgrFY1pfkLfWBZInDPjseuuuQXtixOVBj-L114nQ8fcuUfT1gZsDpm5cKrQa2PK04TrehscsHHh6iIUl5inL_t_gaTWN-BG8MLVRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/C4GFBCOvTAfQfvN1oGux-0QDOCkrO8E0EkP9xDjqAzF9vEPAtNhspvzAoxyoarzBCbkPaeyB75bwWUda_U_O1DG7EKHM6w__iIC_2xSELmBsQKGeDKySuqTyuFNWFWEN0Sl1rJwxqJb4y9oh94WQWL054EMwQ0y9P00k81E1fAN-NNdvDOLU0wTDRbu0QhYeCLXnazOZLczPE24xAUgh1sZo99gzH81-8gc9tlhaiskvNW11ccaAWTIXi1UaqDJrsBO354SsLF0_wasUmY7zULZsafVnyptg0boN7uRGfpUSuwV3MTMU8d7sGfLKXTNRaZRXecZ_xMyijOvZItIsrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZTKDKWWDsHesVkiZ-k9gzQtzJpk7OLUT0NS16qj5TwCf7O1Pc_XhmSj131eSmCZ6yjUkr6VyI8KQvbKB14FjvOm5hTP5yOkusNyzOYT4zMMdZp1ltP-lK-EuV6xulE6w50aeBfBYDQ6cxMclUs4Ldxzq82k_Za1l3c-q22GqYDSWrDEzHzZfZzkMFsqYWwc04CWA1sHh0gwhskW-erHBnSH5V-7C5-PEp93k90Ob4h_RSmFHsoHaEJV_JjDW5NjDwmxSW2SgFAKuRgnuD7fCNXgpp8v8v9_NHasujjYnsvZtl9WghA5hfVA0onpa1zd88t3jZ_asazT9xfU9yDHu-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ایلیا هاشمی:
ساعت ۱۶:۳۵ شنبه؛ ابتدا صدای جنگنده در قشم شنیده شد و سپس یک جسم مشابه با بدنه موشک، داخل شهرک بوستان قشم
سقوط کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/72682" target="_blank">📅 17:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72681">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72681" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/news_hut/72681" target="_blank">📅 17:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72680">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I_FyrzLWP8sN1EZLXn0tRgFbMXPByNL-u_Tm17RZWj0x2vTAxO4OYnkQAWeRFKosnWOrg0-OgLyAS5Xbzjs5sjN3lMMnRuXyiM01tqQQCX2bBzYHpL89jbOtSdqRqyjp7tLcD3oi3UudyOSWd5CzhvTgydVTL9HWibrhsjx4whg5wnyRoEj0cLTFDOPqGv9_S1NMD2o-yYeJ-mn992yG9aliuEUKyFZVlOvFeXqYBxWEAfx7Je4uO7lorNr4YZuGad-MSGeBBuKZEci7gSygLNdgxWvYW3TzOMdGHo8BgTpLZMIsCWGQ0wl-FwM7meVYGABDVT-aE64PutWA5bIs4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز انگلیس
🆚
کرواسی را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
انگلیس: ۳ برد، ۲ شکست و ۱۳ گل زده
کرواسی: ۳ برد، ۲ شکست و ۷ کل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/news_hut/72680" target="_blank">📅 17:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72679">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4323337b42.mp4?token=Mt2I6NRUexHkIdBFHCHhN3HJzTaC0hsX_5_Kmv2EjBxs58MQMsZKAbul4OHbXPRhz46sLuTuHuEntNrMjyPrLFcZPT3kP4jPnfnJIyxxKnhnynCcRrR7FgGHeeCQLVR3Nqfh-OOqkK8vD7AyQpx9_FE8PMaQfhXm1XYEeFvZOynGKkj571ZqtuvhsHrPPqpBpTLS3yR3JtGU4L-xn0vaDhPurOlRGl6uSwMJv0SXRapbIVZj_2YY_WtMx-EP9-Kpa8VP9tuw2fe_26sQCq1nF5X0Arxl9xgEuGnlsBzHuv-4IBHyqT79FNtqE04rh588crafHj5I9iRaZ4mvfEg_qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4323337b42.mp4?token=Mt2I6NRUexHkIdBFHCHhN3HJzTaC0hsX_5_Kmv2EjBxs58MQMsZKAbul4OHbXPRhz46sLuTuHuEntNrMjyPrLFcZPT3kP4jPnfnJIyxxKnhnynCcRrR7FgGHeeCQLVR3Nqfh-OOqkK8vD7AyQpx9_FE8PMaQfhXm1XYEeFvZOynGKkj571ZqtuvhsHrPPqpBpTLS3yR3JtGU4L-xn0vaDhPurOlRGl6uSwMJv0SXRapbIVZj_2YY_WtMx-EP9-Kpa8VP9tuw2fe_26sQCq1nF5X0Arxl9xgEuGnlsBzHuv-4IBHyqT79FNtqE04rh588crafHj5I9iRaZ4mvfEg_qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن مرجانی، رئیس انجمن صنفی تولیدکنندگان شیرآلات ایران:
اگر این وضعیت اقتصادی دو ماه دیگ ادامه پیدا کنه
کل کارخانه‌های شیرآلات کاملا تعطیل میشن
@News_Hut</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/72679" target="_blank">📅 17:32 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72678">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ناو هواپیمابر USS George Washington  در حال انجام عملیات پرواز در آب‌های منطقه در خاورمیانه است.
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/72678" target="_blank">📅 17:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72677">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c0fbd5c19.mp4?token=AsWpsfs9GwRn9dc_AkWzTsikuIk0uGLZI8WCWe7XUjK7j_TUTxCX6W96PJ_ZO3qp4h1aYJbUCNY3sFFyXaJdJ2jMgwuxd0985fhYjI7lV8DGVFC37B-6ybmUjJAwXOWUVVrHSUjK2kK2al6DReofp7e0FGFaIW-zFVoP5Ke3wpaJVPWSZCSAjkfQaDGXFxPm_M5lyIJN0J1ZmbomCWiwKd6LO_H2jKZ_Xnt82VmqdX0usObbIe0imZ-gbEpR4CCg0FRwRHePrHQ3iNoMmj7hNRN2HpVqx0i_lQgw4ivBgpdsbCMhnMiaK5ZB4fsumKcdKTR42c8UY5cdNfU9bTkLKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c0fbd5c19.mp4?token=AsWpsfs9GwRn9dc_AkWzTsikuIk0uGLZI8WCWe7XUjK7j_TUTxCX6W96PJ_ZO3qp4h1aYJbUCNY3sFFyXaJdJ2jMgwuxd0985fhYjI7lV8DGVFC37B-6ybmUjJAwXOWUVVrHSUjK2kK2al6DReofp7e0FGFaIW-zFVoP5Ke3wpaJVPWSZCSAjkfQaDGXFxPm_M5lyIJN0J1ZmbomCWiwKd6LO_H2jKZ_Xnt82VmqdX0usObbIe0imZ-gbEpR4CCg0FRwRHePrHQ3iNoMmj7hNRN2HpVqx0i_lQgw4ivBgpdsbCMhnMiaK5ZB4fsumKcdKTR42c8UY5cdNfU9bTkLKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛اسکات بسنت وزیر خزانه‌داری آمریکا:
برای نخستین بار در تاریخ — از زمان آغاز استخراج و صدور نفت(ایران) — آن‌ها در هفته جاری هیچ نفتی روی آب (در حال حمل‌ونقل دریایی) نخواهند داشت.
آن‌ها هیچ درآمدی نخواهند داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/72677" target="_blank">📅 16:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72676">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">صدای انفجاری از سمت دریا در قشم شنیده شد.  @News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/72676" target="_blank">📅 16:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72674">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kWo3MLBoJlLaqk657NyWrma6CHqFeWuHr4OuQa_1qquQLqPHW-Q4P_GDMVRJnz5-oWJSUlGxpyaQvAiQ-AS05YUtRWqIER2pYavd9spyflrOeJM2ndWlnilLn8WH1rLRsw7seuXntOqFs3ztZqXc_x5EFO_7OrHTjac5UJPWEMEdgQ4bVrG1KNcdvAc3xq-Smoz094EQUoLXXMbYlDi69HuP97lMS3XmLWgLDSivE1_eD9c-dwi98N92GjcQlEos4Ag5PgvNG-an1SX-5qMQaV0erxfUPrGRWqlzhCLc4ZblLpApElTwhgT9nuVJtNdFsnWqdEpCPwqbils5-YErjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MaoFcsOpEMS_ghTwfZI-8CNbUQjL2QtRV304VMwH5IKgwAfPJLySOeVciHLshzscsDoWNN6yJXvgEJ4yj5l1Ykcy_xvA2GT94d0fd4hyCQ54t7i6_nPmIr5DcGmHUSVOzroMKqFqDdvbecDhO8L16upCa87CqKJDNp74SEd6OCp1j3SQCNruHddTYPMPue5oG0PyF1ewtPxSQ7ey8b_1qaSjfDZXixwootGVuabC2r4IYAFwqPTShbWutwKkexCIVGa0_S0LnBNT8WGrFV4sIOr1m7NVfMBmQnpkRDNchjhoBNpljTDUtLxoGsZRV7MOzzEFB-uzGUjHd-ImcS2RbA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نمونه کار:)
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/72674" target="_blank">📅 16:04 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72673">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nqSPpzwDdqKNWHN7TTmwnoV9HKjAP2xw7-WfZ9Jipg2rXo17J2dj7AkSWloQ-3VOEyDqDwKHIqauyrpKXLIxJQQGsvNUvr541sAi-hyCu1CQGjGi1I4G4uxTlhUDsPrvxbfwdOsvhP8J1I3sTazB4_URyednQJkeS-a3Gi4pZZFBpc1M3yUPUoJ9DUYfM7pyNTPJRJk-sj9hmQzXoOJFHaDcwuQZLuaq3NTtkWslM2YuIliJx6JnzVdoUA0XjUHk8oOF5I5KoecossoXzYT-jCG6hWXOunF7UjZzxwB8mbtvU1z6jryMi3x05NUv3Q9u-hvhDS7CfHxSQhWpmYb3Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام به دانشکده 05 کرمان
✌️
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/72673" target="_blank">📅 16:02 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72672">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">#فوری
؛نتایج اولیه کنکور ۱۴۰۵ اعلام شد!
با ورود به پنل شخصی خود در سایت سنجش میتونید کارنامتون رو مشاهده کنید.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/72672" target="_blank">📅 15:37 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72671">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c967ea5781.mp4?token=uDs_hMw5MvYVAi6oFUlFNIvBJy63HoFNIWek2438XhOK2iC2bsEV6IvS54wxXfOaFVkvVkmgN-Kx8_Jk2HxoxHsWQT94YC6PkhF2JBHpwMPn9-Mr9c38C7_nfFlsSjnSzybS0k6o6XykNB1y_ZfjZuuU1HiqgrJxXJXmNSgtZPWvgmZx8rsIByWdt3mSii_xvcx3J1_8MLuW6wLj-8sWwJErBx_tvXeY0wQ9LMd9bpY1j8uTsO_6gJS1IPKRUQI74wcSwb5-EgHgPA7XkIzvcIb0ZNBmsN2Wdo9h61sYrqoqYfOb8u5sLB0SoszXSrFwnOkC5BHKAOaaqIJe_8ViLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c967ea5781.mp4?token=uDs_hMw5MvYVAi6oFUlFNIvBJy63HoFNIWek2438XhOK2iC2bsEV6IvS54wxXfOaFVkvVkmgN-Kx8_Jk2HxoxHsWQT94YC6PkhF2JBHpwMPn9-Mr9c38C7_nfFlsSjnSzybS0k6o6XykNB1y_ZfjZuuU1HiqgrJxXJXmNSgtZPWvgmZx8rsIByWdt3mSii_xvcx3J1_8MLuW6wLj-8sWwJErBx_tvXeY0wQ9LMd9bpY1j8uTsO_6gJS1IPKRUQI74wcSwb5-EgHgPA7XkIzvcIb0ZNBmsN2Wdo9h61sYrqoqYfOb8u5sLB0SoszXSrFwnOkC5BHKAOaaqIJe_8ViLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بسنت، وزیر خزانه‌داری آمریکا:
ما از این مناقشه با ایران عبور خواهیم کرد. به گمانم عرضه نفت بهبود خواهد یافت و قیمت‌ها به‌مراتب پایین‌تر خواهند آمد.
روند افزایش دستمزدها ادامه خواهد داشت، چرا که شاهد رنسانس (احیای) بخش تولید هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/72671" target="_blank">📅 15:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72670">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">صدای انفجاری از سمت دریا در قشم شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/72670" target="_blank">📅 15:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72669">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2fafdeb0b.mp4?token=Dy6HyaZeFOgJ7xoi2cPdwU2wqH29jEwUerY4SFIpcl-vMKL2f2WBIVfxQ0_dlvN1rPIYKBRJuRJaqSyyuQeHmenCL69kUHek717T_Die2m6tpr8dR4vlGjKna0LIaCTeynqIRQq6y3z0VtMQPUcnyDoDAZa0U2n7FGuZPCZRc4fU-82yAjyaZh-UwB6Mw_WYkLNDrQZVOSgME5gpKCQ46B3b1EXUkMNUpJ70gpX0V_xSkO-IcLqI0ExH6Ce-o2GZv2BnWS3e51RvY9efgDtpxpzQuf3BoTQ7Y9gaZsWIqN0Xp6UPEUiW_koroZJy_JO2ce9mElkpvaQJWf_WPvYZKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2fafdeb0b.mp4?token=Dy6HyaZeFOgJ7xoi2cPdwU2wqH29jEwUerY4SFIpcl-vMKL2f2WBIVfxQ0_dlvN1rPIYKBRJuRJaqSyyuQeHmenCL69kUHek717T_Die2m6tpr8dR4vlGjKna0LIaCTeynqIRQq6y3z0VtMQPUcnyDoDAZa0U2n7FGuZPCZRc4fU-82yAjyaZh-UwB6Mw_WYkLNDrQZVOSgME5gpKCQ46B3b1EXUkMNUpJ70gpX0V_xSkO-IcLqI0ExH6Ce-o2GZv2BnWS3e51RvY9efgDtpxpzQuf3BoTQ7Y9gaZsWIqN0Xp6UPEUiW_koroZJy_JO2ce9mElkpvaQJWf_WPvYZKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واژگونی ترسناک کمپرسی بر اثر ترمز بریدن در کازرون
💔
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/72669" target="_blank">📅 14:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72668">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">پشماتون بریزه!
ایران‌اینترنشنال در گزارشی درباره مهدی نادری جهرمی، رئیس هیئت‌مدیره شرکت تهران‌اینترنت و مؤسس و مالک اپلیکیشن هف‌هشتاد، ادعاهایی جنجالی درباره ارتباط او با شبکه‌ای مرتبط با موساد مطرح کرده است.
نادری جهرمی با نمایش چهره‌ای کاملاً همسو با جمهوری اسلامی و حضور در ساختارهای اقتصادی و تجاری، به تدریج به موقعیت‌های حساس دسترسی پیدا کرده است.
ارتباطات و فعالیت‌های او در حوزه‌های بانکی و مخابراتی، در اختیار شبکه‌ای قرار گرفته که با عملیات موساد در ایران مرتبط بوده است؛ از جمله انتقال اطلاعات، شنود و نقش در برخی عملیات اسرائیل در ایران.
این گزارش بر پایه اسناد تجاری و قضایی، مکاتبات بانکی، قراردادهای شرکتی و روایت فردی با نام «کیا» تهیه شده که ایران‌اینترنشنال او را مأمور سابق موساد معرفی می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72668" target="_blank">📅 14:14 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72665">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1jXhcYJ4FY-62Y1EDt47Uwfe0M0KpKsAFEmyBZRbcLgPRK0GiAHPlJ67A6EhruGxIgOpPAmHlRZX4nEZuLRcblCjucjHnMMmIl7ZhcwfQSOXY_7mfBAE0EjwC7GOaHEGpP9SI7RBEd3jdUjNp1kIGi2fPXBBCs3Wz8pD5PMiueZgznBw7TxgtNjLHkrce5xho6wXnwr9Own_Fb7v0ZNepnvwLaLf7AbZWJPQzEeqgZcETSbz4nsjGHKrAP1SGv1QeVZOCE23S47kxBW7gNL_BVaTPJY56xvwIAPtG89LG6eR3cD3FEp-aeV7ApIjapguQwK4e21lkq8GhSU0MB5sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1908d250d4.mp4?token=AodPMVCX0R5w0ldoYkrWVw9576f1gYMNQJiOl0VJQ3S3QM-fya5bdOCKLHjbOA3G6-ZbZnXrSyxcB_9kU7ADNUGAb17XKLn8ChXG3cv6l_NB-YEr64tZMjCo4NVwagHQXxtErhPLx2eQcAzjVx_xo8pQ7-ijpASRgLkEikby5c1LPI-PlLiBKJi5UgwdREs8npXSkF2FRFyKoYJU3miuNzcQ8UC7eTI3K0T6v-lhMIgxGOfEoUiPKXmyQiaYdKHSCJ8EGe5IIuIXAvitEUbL3maBhnPNjiSFw9KsxVibNtN5h46PkZp-s3AihNo3nGgLhNMiyW0xkurr5zrNJSWlAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1908d250d4.mp4?token=AodPMVCX0R5w0ldoYkrWVw9576f1gYMNQJiOl0VJQ3S3QM-fya5bdOCKLHjbOA3G6-ZbZnXrSyxcB_9kU7ADNUGAb17XKLn8ChXG3cv6l_NB-YEr64tZMjCo4NVwagHQXxtErhPLx2eQcAzjVx_xo8pQ7-ijpASRgLkEikby5c1LPI-PlLiBKJi5UgwdREs8npXSkF2FRFyKoYJU3miuNzcQ8UC7eTI3K0T6v-lhMIgxGOfEoUiPKXmyQiaYdKHSCJ8EGe5IIuIXAvitEUbL3maBhnPNjiSFw9KsxVibNtN5h46PkZp-s3AihNo3nGgLhNMiyW0xkurr5zrNJSWlAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هزاران دانش‌آموز دبیرستانی فرانسوی به دلیل کمبود معلم، ازدحام بیش از حد و ساختمان‌های در حال فروریختن، مدارس سراسر کشور را محاصره کردند.
@News_Hut
| Clash Report</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/72665" target="_blank">📅 13:42 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72661">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b9ce8d805.mp4?token=M6RNUzYQJSqzpEXK2EIq5TvtimRDD8oPUQZmJVnqLOf_-GGOqnsmz5d5QkYEqh9E1gL3T7WzXHxYzoRNBcnVc3T1U0wG35F8uY1XeBShWZcHGk1ta-WNYHVWWYy9X50pTn0MY3pBWWx03hoaOr4gMEeanzc1MXavKia_HZ_J914GncIMAdSiFLMVsdQnAKGMQ1VjhY38kl7U5Y-50cWzPwgroHvDHxmEiNod1GGvAwr5iVc5jkXDSICugpgyBIvXo7YC9IHmCDgFVC8FFOCnlGoLkaDc9mPM8kxoHSeIVua9Bf0L3CZjzRduk0DQP1AxskI4g9aG1HrMZrId4esQLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b9ce8d805.mp4?token=M6RNUzYQJSqzpEXK2EIq5TvtimRDD8oPUQZmJVnqLOf_-GGOqnsmz5d5QkYEqh9E1gL3T7WzXHxYzoRNBcnVc3T1U0wG35F8uY1XeBShWZcHGk1ta-WNYHVWWYy9X50pTn0MY3pBWWx03hoaOr4gMEeanzc1MXavKia_HZ_J914GncIMAdSiFLMVsdQnAKGMQ1VjhY38kl7U5Y-50cWzPwgroHvDHxmEiNod1GGvAwr5iVc5jkXDSICugpgyBIvXo7YC9IHmCDgFVC8FFOCnlGoLkaDc9mPM8kxoHSeIVua9Bf0L3CZjzRduk0DQP1AxskI4g9aG1HrMZrId4esQLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از انبارهای نفتی آرامکو در ریاض که هدف حملات موشکی حوثی های یمن قرار گرفته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72661" target="_blank">📅 12:51 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72659">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g-dAd8Cuz8bciEa56j1mj-E3Aa7qaphQTtH9ABUPwLavZFZNfmUaDczcU1yEsmuScrIPhSkcVEhMGuBbKXoMJIqes-4az0UQOPaMb-DEtcDaff3z4ysaJXtob_uGJVjRXYMZNs4XZZka9CdxkAGeXQvgipjIqIin80X1AkhsVAq5A5WjTo7-KyakhYBoeLNmrX3FJ9Grrr2nwLK8n3AinGXAkQDYVaVVf45YpuP615Ph6e0NWKU6cw6GTzrB0hdpIXDW67eJMF37Tslhf7uCEyhmhT1F5a_Wmcp0Jom5G0R9M94aR0AJXPSDUxR9D1IZuZZGQ7nksTU-zMLYeBOR0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cc83c2d7b4.mp4?token=ofLQutWYocIOGQ1HcsJgl1v0xb0QIuqHghtKJx8x4vcWXfL86tUzpdYlF9d_SppVxj7wwZatawP_6Tk7GAqTm7-cDjrvsZx2BtKV9kpyl44p-KXvSi8qXWBah1kVOqwkn9Ja7nfU0gI5NC0rHjktkSdd1MxJ2M5WHR4XrJtsEnHEwMEs-a74Oc6kstQJZzfzAkhqQCr44RpSf93B0MqfqJZ12IeJdH3bzZj8ww2HO6tChxXZbErnqXl2sbr3BoSNyr34Glc14hdGyL33tt-xw6Hmkcs5lw-Cnn-lav-L_0wIVvQ4tGmvOnzlCHX8zBb9Fo_5sKJpCIMoUrsg3FOvvw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cc83c2d7b4.mp4?token=ofLQutWYocIOGQ1HcsJgl1v0xb0QIuqHghtKJx8x4vcWXfL86tUzpdYlF9d_SppVxj7wwZatawP_6Tk7GAqTm7-cDjrvsZx2BtKV9kpyl44p-KXvSi8qXWBah1kVOqwkn9Ja7nfU0gI5NC0rHjktkSdd1MxJ2M5WHR4XrJtsEnHEwMEs-a74Oc6kstQJZzfzAkhqQCr44RpSf93B0MqfqJZ12IeJdH3bzZj8ww2HO6tChxXZbErnqXl2sbr3BoSNyr34Glc14hdGyL33tt-xw6Hmkcs5lw-Cnn-lav-L_0wIVvQ4tGmvOnzlCHX8zBb9Fo_5sKJpCIMoUrsg3FOvvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرماندهی جنوبی ایالات متحده فیلمی از عملیات شناورهای جنگی آمریکایی Saronic Corsair نیروی دریایی ایالات متحده در پایگاه دریایی گوانتانامو بی، کوبا منتشر کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72659" target="_blank">📅 12:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72658">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ترامپ:
باید با چه کسی طرف شوم.
کسی نیست که بتونم باهاش درباره ایران تعامل کنم. هیچ‌کس نمیخواد رئیس‌جمهور بشه.
من می‌پرسم: «در ایران با چه کسی صحبت کنم؟» تق‌تق(در میزنم)...اما کسی خونه نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72658" target="_blank">📅 11:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72657">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72657" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/72657" target="_blank">📅 11:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72656">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q6-hk9kqnac494h7rZ_igKR6EMxlgh1Exv5dJljPOX4aqp0NsmywfmqGVLVCnYPDrlzzceQ5nSqCoF0aQLqn4wHWCWAtTsienQjl0uU417UPUO7PV3rkRaL7KXDCqBaWwaPi3lraqVyzswkESBZUtkCI1IsphYAsL1mPMFxgibnLaiB6AJlAazKHdUFaBd6tNtofJnAeAgJPkQwuN6l-jMsqxiYLXXsOQDmOTcidvXyOSFIL98TyC4LJ9yIFCWQGnv9DyAOEGLiXMhrd3UtgevTqjykXnJ48mtPQa4BI3TsgOQzDEl1ID74qsHInfRtMSU-vTukwOXsS7v8PNRu28A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
انگلیس
🆚
کرواسی
چک
🆚
اسپانیا
اسلوونی
🆚
سوئیس
لومتزانه
🆚
اینتر
یووه استابیا
🆚
لاتزیو
برزیل
🆚
هند
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72656" target="_blank">📅 11:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72655">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c533100ff9.mp4?token=WjRnHUgH4K4P0yukQvQXTb0_N91yQvdrAjJ5vnH21Yds3ADJgcfxUv46i76D8wcWFRtg-ghzswH7iqDk6JgJ4b6i2wuG0-LPxnve9bJw_J07tPDWNdrT2iIp2KSljiSFai1rNcc_RkZ4JJ-j_G7uRUEfUVu5-mZwoKhQFyL8XJ1SAojnM1OKbVAwKluLN9CW_apf8yEJsnojS-BPIbRfVvpH7_DxvCUCwjWMIfKrdptRVsO7Qa7B_oAV1uMPdk996EZK5ynYXtf0qso79aS8jCF6u7xCVurUSS62bLhNPFuQ-JjTxfJ1zfVctUGsllAUGzuxBTdyF7ZMOc2ZMUK9zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c533100ff9.mp4?token=WjRnHUgH4K4P0yukQvQXTb0_N91yQvdrAjJ5vnH21Yds3ADJgcfxUv46i76D8wcWFRtg-ghzswH7iqDk6JgJ4b6i2wuG0-LPxnve9bJw_J07tPDWNdrT2iIp2KSljiSFai1rNcc_RkZ4JJ-j_G7uRUEfUVu5-mZwoKhQFyL8XJ1SAojnM1OKbVAwKluLN9CW_apf8yEJsnojS-BPIbRfVvpH7_DxvCUCwjWMIfKrdptRVsO7Qa7B_oAV1uMPdk996EZK5ynYXtf0qso79aS8jCF6u7xCVurUSS62bLhNPFuQ-JjTxfJ1zfVctUGsllAUGzuxBTdyF7ZMOc2ZMUK9zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
گروهی از افراد را دیدم با عنوان «هم‌جنس‌گرایان حامی فلسطین». بیایید یک روز آن‌ها را برای مذاکره به آنجا بفرستیم.
دیگر هرگز آن‌ها را نخواهید دید. آنجا کارهایی با آنها می‌کنند که باورتان نمی‌شود
😂
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/72655" target="_blank">📅 11:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72654">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">اسامی نفرات برتر آزمون سراسری ۱۴۰۵  @News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/72654" target="_blank">📅 10:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72653">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jtdLP9V2HXiIXDWxZIPUvESptOPWkFGDkaay5TcMmVjt8GvoSYPhbHDQ2oFXoGV1pDQIQ4iPMB5LB_qGWXOL9g9CAfnNwNMP_0LptgZiypaIeaK4UDV6EQRHO97DXfJClvrJziLezCJ-AksWXOBhQPXEFqLGN9IbXecfhIFeQ4AGqZrRarlocsinGpEj9xjcRN40S42t_OBwClKp8gDPLU2YaajbBzuH8hFb6k_KTgILBSauTvHAuWRGiYmUB738vc9TLPTkESPxPN2tlMQuoKr-Ss-wrSPjcTGuADrmXB1AqBgLsau41HjBqmwKEi2oVJed2fJeaEb4LvoWu7XCXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسامی نفرات برتر آزمون سراسری ۱۴۰۵
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72653" target="_blank">📅 10:53 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72652">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">نتایج کنکور سراسری برای عموم کنکوری ها فردا میاد!!
انتخاب رشته از دوشنبه ۱۳ مهر ماه تا ۱۶ مهر ماه ادامه خواهد داشت!
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/72652" target="_blank">📅 10:39 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72651">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMB0fH3cFZM_G_LqieOKc8CyL7A3MKR0XB2CDj9zmDJ1GOezva0TFkawL_RBHpnFcvGg1BMv0smw0UIDavGQvL41fzhQe5b4jzY_t6LiquFz08nloSRe7bxMV3dQKa1TZAwZxE_2e3gqnJjBMVXAab16z0VKxvKnMl9cN9vo33YxXzfxeF4KD9BT997V--70Wg-PC-oxPaBk8gHgopGOle5Ae0BccdvGewuECFwg1KJ7UqKnro-3hP68R6i3FIUxRGO9RR6545Mp530gdN-5Icf5lw4dEHYsInG8419s_7bsicCJzIwsFULXa9swXSKQEwGtDcBb3-uxy_4vcQF10g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشست خبری سنجش تا دقایقی دیگر!
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72651" target="_blank">📅 10:28 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72650">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l52JGgqcO9vMjtHLSdws7PoBCi3IWA_VIqs0AOfM2ZYiBrOBPPoj5Kh7BdWOuD7IOTv7wkuXIX0-m6_uk_zxHFitwY8cX_HMtazljKmFH0CGcsh4SCc5zmHkV12N0oQSbf4dyj7LIdofJbuorlvuKBUhdD4HQhSja7CfUpupVh7nr-gXOAwPJjblpzG7YDWX0SvUkKVqNxFTt3Gg4Qis0g-7Qt_7v8qVOYsVQe_KUnAUr0hrZSsWFoaCNc59xcnHhE6YxW2lwAiKBwxTkCGZe6PWhz0WFzQ5PiH6bTqhoba0aoHBQXzI7r_K3Ckmtjvt8n9jPwUq1zEhHHAYLf2nyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#مهم
؛ اکسیوس به نقل از سه مقام آمریکایی:
مقامات ارشد کابینه ایالات متحده در «کمپ دیوید» مریلند گرد هم آمدند تا درباره گام‌های بعدی در قبال ایران و انصارالله گفتگو کنند.
یک مقام آمریکایی اظهار داشت که در این جلسه تصمیماتی اتخاذ شد یا دست‌کم بحث‌های عمیقی پیرامون این موضوعات صورت گرفت.
ریاست این نشست بر عهده «جی. دی. ونس»، معاون رئیس‌جمهور بود.
«مارکو روبیو» (وزیر امور خارجه)، «پیت هگسث» (وزیر جنگ)، ژنرال «دن کین» (رئیس ستاد مشترک ارتش)، «جان رتکلیف» (رئیس سیا) و «استیو ویتکاف» (نماینده ویژه در امور خاورمیانه) نیز در این جلسه حضور داشتند.
آخرین باری که نشستی مشابه برگزار شد، به ژوئن ۲۰۲۵ و پیش از آغاز «جنگ دوازده‌روزه» توسط اسرائیل بازمی‌گردد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72650" target="_blank">📅 10:07 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72649">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f04d52dbe.mp4?token=bNf0jGXF8WQhK7IXbb8tqYKtNy5PBICv8ZDP9gadFn4x853W5iiZHC1XFn8zC_1MDJg-suDMpG58Aq2UzrQ58c90JrhPPZejuVU10F4ShOH35t0Z3tp_TToWy3z0iwv9yckMATXdhmu_DmPiIbHO3iGFzxxohwv2be2cPhcbN4ra1Irhze0FGDIlGF_aRRwh965xO3yfSa9Um1r0qX92vJpJ8fz_SFZqOyRwmGd_qEtXrLcAShpOmdZ0gcqYFFlrtnUVpkVY-64ElNgTLj0mEmmFHXGC8myCer0BPKLjjpvFyGrno3INwnEkaeydWwVF4FTGIvsheOF6PJZEHB8lrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f04d52dbe.mp4?token=bNf0jGXF8WQhK7IXbb8tqYKtNy5PBICv8ZDP9gadFn4x853W5iiZHC1XFn8zC_1MDJg-suDMpG58Aq2UzrQ58c90JrhPPZejuVU10F4ShOH35t0Z3tp_TToWy3z0iwv9yckMATXdhmu_DmPiIbHO3iGFzxxohwv2be2cPhcbN4ra1Irhze0FGDIlGF_aRRwh965xO3yfSa9Um1r0qX92vJpJ8fz_SFZqOyRwmGd_qEtXrLcAShpOmdZ0gcqYFFlrtnUVpkVY-64ElNgTLj0mEmmFHXGC8myCer0BPKLjjpvFyGrno3INwnEkaeydWwVF4FTGIvsheOF6PJZEHB8lrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ربات‌های چینی با لباس‌های سنتی عربستان، برای شهردار ریاض و سفیر چین رقص محلی اجرا می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72649" target="_blank">📅 09:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72648">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LKuLmUmo-UaY5g-hILQ07g1RicI6nQWlYm-bw4WAatmqC_Bfq37CR80eGdhjEyxBVhtD810X4D5PtqyKzwu0mPmddQM1oIhz7L3P8gGWzPeAh3pF9AaeBjiGLiJdxhtGixdXRSBBFwN9tY3Z1OU5lY-1BO9Rau1rFgt6gQ7ZyrxE1U2u8L-A3dxJ7lOHcJaAIzmYAaOdmIEHCORjNQqo6ucllouFPGWTfur6EzM_fnbhPUGeBExYzC8EZ_RNRYRTXpS8YmZlK5A-I6dxfV35R9DWEIbJdaE5zHxlIc5MmQ4sCSUWJijnoaVab7PvQqeXbBvFkmo5FGyLn851Oyvfvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش «ای‌بی‌سی نیوز»، کمک‌خلبان شرکت «فلای‌دبی» که به خلبان حمله کرد و قصد داشت پرواز شماره ۱۰۷۳ این شرکت به مقصد اسرائیل را ساقط کند، «همام الحمامی»، تبعه ۲۹ ساله اهل عمان شناسایی شده است؛ او اذعان کرده که قصد داشته هواپیما را در اسرائیل سرنگون کند.
الحمامی در سال ۲۰۲۴، در دوران آموزش در شرکت «عمان‌ایر»، پس از کشف مطالب افراط‌گرایانه نزد وی، از پرواز تعلیق شده بود اما همچنان در سمتی اداری به همکاری با این شرکت هواپیمایی ادامه داد.
بازرسان در حال بررسی چگونگی صدور مجوز پرواز برای او در شرکت «فلای‌دبی» و تعیین وی برای مسیر پروازی اسرائیل هستند.
الحمامی با بازرسان در امارات متحده عربی همکاری می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72648" target="_blank">📅 07:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72647">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tC6vw3mRqzpC4V5hhosXKEeGjLSRfZYDmQsT5tQkdwvA6-Ia8CgqB2CStGkUvgyxY1aBCDxDR2OMf4CWw-h71FG_LXN5vL48di6bN5GmrHnLFAbEjGx6FWp6vQkMtdkjOALCMsTsb3JsDTEhMhy6TtiVRkskcyxE3OPFQ7zcRIAx_yksGBWGKFfmd5bbIw5vO6h1yAaelVOFnss5RwUr71JEjFY45yYgAzkiS05qDm-zRQa5CRquxLA0RWb4jrE2RvopQFPvD1THfjY1cMnFAMjckEwZRc9sxVCqYCkYpvKEfabXeVKIY7bbp4_CIBKdMMoVNziMCEwv6i6JGWKXQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار: گام بعدی شما در قبال ایران چیست؟  ترامپ: خب، اگر به شما بگویم، خبر بزرگی برایتان می‌شود، مگر نه؟ اما خواهید دید؛ اوضاع دارد خیلی خوب پیش می‌رود. وضعیت ایران خوب نیست.  @News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/72647" target="_blank">📅 06:04 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72646">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72646" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72646" target="_blank">📅 01:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72645">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BvMfrXc7HIJy84Tik6EuotH_x9DJRYqj_kxN2CC0AjJDG-JJj7YwTFAEzCW2DC7-aWI4oUQkwHfdFNevnE2_V2O-Lwsa_1aWDwB1bNtC_Z65G7ACUieeDUGHNx1lAuYt2pcCrno1RR-YnPIe_DWHq66XKV-3gA4FZLliWaKkM0YHlIKursW0pGpx8xgf3Eudhn0laR5kjdXH-ig9HwHCzA_BOJwuaBSiURR6B_B-4t4qSzVz1kDRHTl2y6Wd_8sz4y5Y_WU8jJAVh6gLvL-OrpnflGRC066Fm91hgCFvN3PtbowtaaHRdzLJTsAefX1jBK29V0IYoAivbekXY4IgrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
شماره معکوس تا رویارویی بزرگ
​
🦖
دیوسون فیگاردو در مقابل پیتون تالبوت
🦖
تجربه اسطوره یا طوفان پدیده جوان؟
​هیجان واقعی و پیش‌بینی بالاترین ضریب‌ها در
TrexBet
!
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/72645" target="_blank">📅 01:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72644">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b49a7f3128.mp4?token=CckSS90Z6iua1XHuRwKA1XExdxZOqUSMFedz1GwaOmPralgsrQYs13fPe1Z5eo_P8PWl-Bko4rBthP8PhloqJ9DcWFfegcn3JDVLQK1C4PKaByL02buiys17_WA7Go_iB5O74bQs3_gm4ATnEha6fqyHDzcNYAL8dYc-yAzwLQKqBBb46iak9kSoVmavejkg6-7QYfkdh2gxxpvPyTNqzWbKfqGeWa_OXLvSFo8sQ-JqSzuVIyWHUKxbPF0HDbhbQHoMTRWXlrui9TquHM0RY-84HWEbyFMzfSuSfYJwNIlWMe42QMkZMhXlCpz4IbsJLhvKn8r2e3HFTbcU6Soedw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b49a7f3128.mp4?token=CckSS90Z6iua1XHuRwKA1XExdxZOqUSMFedz1GwaOmPralgsrQYs13fPe1Z5eo_P8PWl-Bko4rBthP8PhloqJ9DcWFfegcn3JDVLQK1C4PKaByL02buiys17_WA7Go_iB5O74bQs3_gm4ATnEha6fqyHDzcNYAL8dYc-yAzwLQKqBBb46iak9kSoVmavejkg6-7QYfkdh2gxxpvPyTNqzWbKfqGeWa_OXLvSFo8sQ-JqSzuVIyWHUKxbPF0HDbhbQHoMTRWXlrui9TquHM0RY-84HWEbyFMzfSuSfYJwNIlWMe42QMkZMhXlCpz4IbsJLhvKn8r2e3HFTbcU6Soedw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: گام بعدی شما در قبال ایران چیست؟
ترامپ: خب، اگر به شما بگویم، خبر بزرگی برایتان می‌شود، مگر نه؟ اما خواهید دید؛
اوضاع دارد خیلی خوب پیش می‌رود. وضعیت ایران خوب نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/72644" target="_blank">📅 00:02 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72643">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ساعاتی پس از معرفی رتبه‌های برتر، کارنامه داوطلبین برروی پنل شخصی هر داوطلب در سایت سنجش قرار خواهد گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/72643" target="_blank">📅 23:27 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72642">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">طبق گفته حسن‌پور خبرنگار خبرگزاری فارس، فردا در نشست خبری رئیس سازمان سنجش رتبه‌های برتر کنکور ۱۴۰۵ معرفی خواهند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/72642" target="_blank">📅 23:21 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72641">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d476b5a95.mp4?token=PXgZcnyxiQSRgSrMRYkcsA3jI6Lvr2iFpqFaeKtANIsvXLW0WfLLR7Jto8LMqGK9a_5Je3JgTnhNrWBhG-2Oz0I7iVjkbA93lf5rfDDhmtlhpulsfHOC7v4Z0on9bRdx3WW9RU_-2nPQ2nzVGcYIxbvM3r5Oo2U2d0UfWaxt9Vxc4ieXZ-vQkP6NJ2gX0LZyJSkeC-UgU_jXPXGryIHlNaPHieusMSwn2bvpLAGdJU7VctiI4f9hPYBblkaLkZDi_0oGoN5iuzF-HnprCYWIXPwg8SoZ2a28Zz6SMyLtZFo1PiLJJr5zv6kqhDNCei2KkwtU7C8VLtL71c2jaes23Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d476b5a95.mp4?token=PXgZcnyxiQSRgSrMRYkcsA3jI6Lvr2iFpqFaeKtANIsvXLW0WfLLR7Jto8LMqGK9a_5Je3JgTnhNrWBhG-2Oz0I7iVjkbA93lf5rfDDhmtlhpulsfHOC7v4Z0on9bRdx3WW9RU_-2nPQ2nzVGcYIxbvM3r5Oo2U2d0UfWaxt9Vxc4ieXZ-vQkP6NJ2gX0LZyJSkeC-UgU_jXPXGryIHlNaPHieusMSwn2bvpLAGdJU7VctiI4f9hPYBblkaLkZDi_0oGoN5iuzF-HnprCYWIXPwg8SoZ2a28Zz6SMyLtZFo1PiLJJr5zv6kqhDNCei2KkwtU7C8VLtL71c2jaes23Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر گوگل‌ارث با مقایسه وضعیت در ماه‌های مه ۲۰۲۲ و ۲۰۲۶، ابعاد ویرانی در اطراف مدرسه «القادسیه» در رفح (واقع در نوار غزه) را نشان می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/72641" target="_blank">📅 23:00 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72640">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06f0ca8354.mp4?token=hlaALtw-KPR9IDoDgFQchu9kHvEFnnFvK5lYBR6E6JT4Fhb6efvr7tN0F9awgu2UwRz7Fv3Br0RvDhcbHsdFldHcAzw8wEAcU0EJLIImXwHJZxjwOPN74Ly_CdykzB_tGIY5GAYPp6aS_r6hFGFw_1W_EWkvgMuk45jps6vyV5uD9H7Vgm4T0nquFRI6_4xLMIlQBVS-nSxOsAjgxvJr4xhXxBXD4J1D3LIGXk9TRqwr57ulacQ8_p4LG8sgtldUKunuSQmYjIdN88pAIAXwsNDGNvNo-36uFLUBW6MtdSWjzPywl3vSHRaljeHQcOEcefdWDtx0a5Yaz0T9Et3vvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f0ca8354.mp4?token=hlaALtw-KPR9IDoDgFQchu9kHvEFnnFvK5lYBR6E6JT4Fhb6efvr7tN0F9awgu2UwRz7Fv3Br0RvDhcbHsdFldHcAzw8wEAcU0EJLIImXwHJZxjwOPN74Ly_CdykzB_tGIY5GAYPp6aS_r6hFGFw_1W_EWkvgMuk45jps6vyV5uD9H7Vgm4T0nquFRI6_4xLMIlQBVS-nSxOsAjgxvJr4xhXxBXD4J1D3LIGXk9TRqwr57ulacQ8_p4LG8sgtldUKunuSQmYjIdN88pAIAXwsNDGNvNo-36uFLUBW6MtdSWjzPywl3vSHRaljeHQcOEcefdWDtx0a5Yaz0T9Et3vvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این خانم میخواسته بره مهمونی و لباس درست درمون نداشت؛
اومد تصمیم گرفت یکی گرون ترین لباس‌های آنلاین شاپ که بالای
۱۰ میلیون
بود رو سفارش داد.
حالا چیزی که به دستش رسیده :
میگه این چیه لامصب؛ من با این برم مهمونی میگن خرم سلطان اومده
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/72640" target="_blank">📅 22:15 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72639">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62412d8d06.mp4?token=XGKqvbGUyZKOh9kiKXN9bCmChAoyBb8T49uHCReiHZlIe3aNB-fD-SKrmWngF5Flij8_YhsM3XPwvlJ9plb4wTQ14DH2V1GCCxQQPTjogZCA7cBLjn1pwVoaAqLq-U2rEjUXDU2-cOsEGQXL1Pmh8vcjR7QiZQDfRtxcxqRc8N2v0_B-s1ggiUCSYek6L96q3IAk5hvgqpOwCgZQxyO0FXh1CEOyGw8pKTBfv159N2XtxDpQfRKsucHjnNFOJFQNtRJe1CMlgq1tX6uj2aQFuWw3SRETAegBbBX3qBzA6gHHDjwegsI17WOOvroTP-YxmhsWa8D1aMGgpwT1V7gzzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62412d8d06.mp4?token=XGKqvbGUyZKOh9kiKXN9bCmChAoyBb8T49uHCReiHZlIe3aNB-fD-SKrmWngF5Flij8_YhsM3XPwvlJ9plb4wTQ14DH2V1GCCxQQPTjogZCA7cBLjn1pwVoaAqLq-U2rEjUXDU2-cOsEGQXL1Pmh8vcjR7QiZQDfRtxcxqRc8N2v0_B-s1ggiUCSYek6L96q3IAk5hvgqpOwCgZQxyO0FXh1CEOyGw8pKTBfv159N2XtxDpQfRKsucHjnNFOJFQNtRJe1CMlgq1tX6uj2aQFuWw3SRETAegBbBX3qBzA6gHHDjwegsI17WOOvroTP-YxmhsWa8D1aMGgpwT1V7gzzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پسره سر صبح رفته گوشی داداش ۱۱ سالشو چک کنه که میره تو پیامکا و با همچین شاهکاری روبرو میشه:
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/72639" target="_blank">📅 21:33 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72638">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uNJMUVyhBJuzH6wDOiz9amLH2uwxg-FzrhNXv0FC_JBI9vEPixRpXJ85PTI0ARtCt3KGMChO2NCdgfGWKx3xpUwR0BgmReLsS2Nnr4BhjZGMPkEjFHujFpg8YPoudGLhWIFgM_xZwckwr5QAh0SUxdZYWRT7jiee9fYX8T1P7STK-4kN33pm0S0jmz2227Jj6_5t1kllf6XEWpTraOGvd7ZOoHHzkX2YhBEE_j95W08DBOCZ8jt-9jaKh6kYV0r0iztjcjuf-uQA4kC7bDBW4xdxAh6M7VdejwqRRdJSfpY3zubY0b39n_T522BFQzvoEEC6PsyAm5JghtGRujW9pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) اعلام کرد که ناخدای یک نفت‌کش گزارش داده است این شناور هنگام عبور از تنگه هرمز مورد اصابت یک پرتابه قرار گرفته است.
در پی این حادثه، آتش‌سوزی مختصری رخ داد و برق کشتی برای مدت کوتاهی قطع شد؛ با این حال، آتش خاموش شده و شناور به مسیر خود ادامه می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/72638" target="_blank">📅 20:58 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72637">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">دلار 265
😑
#hjAly</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/72637" target="_blank">📅 20:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72636">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">دلار 265
😑
#hjAly</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/72636" target="_blank">📅 20:48 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72635">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd07c4e807.mp4?token=hHCvQgyQXLZGF54G4wiIs46QBPLTuCKW4FIhB8L9VGjm-UxFZwDm5EzxqZGQ7AwQuaAq8fUw_1XGXbcxj5WPbvBDtVsOavBaefJeUYvrJNZRIfne8qa7uI5ECutFO4oWVYl85hw0VHmUyRnRdBzwzF9SWq4BUHUDnpgQjcH7qhlD2QSdMkpZyCHjWG6X5LbKL-Tv3oZKW-Vs8z1XFe1xuY0GfL4onLR1mwBPyB-y3qhOb75cTLR9I5puF5bVjTPKb6-b7b-4bn1pihNHUyUyUR8mEUqvFbhwsteColoUHk9-loye6FCJKfLIwDyIL__rm4FusrpmtARXv_JmIkMw2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd07c4e807.mp4?token=hHCvQgyQXLZGF54G4wiIs46QBPLTuCKW4FIhB8L9VGjm-UxFZwDm5EzxqZGQ7AwQuaAq8fUw_1XGXbcxj5WPbvBDtVsOavBaefJeUYvrJNZRIfne8qa7uI5ECutFO4oWVYl85hw0VHmUyRnRdBzwzF9SWq4BUHUDnpgQjcH7qhlD2QSdMkpZyCHjWG6X5LbKL-Tv3oZKW-Vs8z1XFe1xuY0GfL4onLR1mwBPyB-y3qhOb75cTLR9I5puF5bVjTPKb6-b7b-4bn1pihNHUyUyUR8mEUqvFbhwsteColoUHk9-loye6FCJKfLIwDyIL__rm4FusrpmtARXv_JmIkMw2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داداش تاییده خیالت جمع برو بگیرش.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/72635" target="_blank">📅 20:32 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72634">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">شبکه سه اومد بازی جودکار ایرانو تو مسابقات آسیایی رو پخش کنه که جودکار ایرانی تو ثانیه اول بازیو باخت و حذف شد و گزارشگر اومد سلام کنه خداحافظی کرد
😂
😂
😂
@HutNewsPlus</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/72634" target="_blank">📅 20:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72633">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">عراق اعلام کرد که مجوز معافیتی برای انجام روزانه ۴۰ پرواز توسط شرکت‌های هواپیمایی ایرانی (به‌جز هواپیمایی ماهان) به مقصد فرودگاه نجف و بالعکس دریافت کرده است.
هدف از این معافیت، تسهیل سفر مسافران و تأمین نیازهای بشردوستانه و پزشکی است.
نخست‌وزیر عراق از دولت آمریکا بابت موافقت با این معافیتِ درخواستی تشکر کرد.
@News_Hut
| Clash Report</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/72633" target="_blank">📅 19:43 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72632">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b2fb6f9cd.mp4?token=YzOzkfulcjS4uPykKB4SSDcD7wWspXSw-kD0QEicQBa1sEOPvKxoQW3HnFeH6QyHiHVwgszAG813izeTn1Gpln5wvz2HtezGH1yR5dhH2c1RCAz1gcFdck0Qtxy0TBZcWhlD-SKzBY0eirK65O9Yyq8OAeu2aQZpN7dfwoVJoehWJwNjePmBAEIZhukhz0dFGbvZvMuHbuaettbt76fJOlFpRcehVgihBg08ajSQUyTT0s3KTgdyEbMuQpiXuIeIrooO4MvN71jghH5ckuwOxqe5zsCy10AWEpK5r-nXHr5q2Up-4WT_i4w-ET-T0uw6FQSohPSnqDYZCgMk6s0h7KRjKC5bTEIK0D8PJB-W5XxUNvtRqWIaS_QAj4oaeXx_tcZDVs58D30py79uEtOKQqtsczSdVMO7FBuTmkMUx8QVup9HU1C0_oXV1I3e8qNfEpmUPR8WROt5mjnsWj7rFQjY8qBBXnykMoi7wzJxw3jVNOTNDHRHr7PV9Ys_oTolG8KPqkc2i-80FMJw2SB2U7x2CuYjqK8m0IezmrgB5djSkcHdkfytDfkPLk68mgo4ZkW0ebxbwX6hESjkOgbWSXNGfszfwbM2NmCrTT371YIAhQ02uxpUToFH975h_91J4n-O39-HB5fWrWPrV0gAeT2Y_DKk4oxNBoCvePpuWPk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b2fb6f9cd.mp4?token=YzOzkfulcjS4uPykKB4SSDcD7wWspXSw-kD0QEicQBa1sEOPvKxoQW3HnFeH6QyHiHVwgszAG813izeTn1Gpln5wvz2HtezGH1yR5dhH2c1RCAz1gcFdck0Qtxy0TBZcWhlD-SKzBY0eirK65O9Yyq8OAeu2aQZpN7dfwoVJoehWJwNjePmBAEIZhukhz0dFGbvZvMuHbuaettbt76fJOlFpRcehVgihBg08ajSQUyTT0s3KTgdyEbMuQpiXuIeIrooO4MvN71jghH5ckuwOxqe5zsCy10AWEpK5r-nXHr5q2Up-4WT_i4w-ET-T0uw6FQSohPSnqDYZCgMk6s0h7KRjKC5bTEIK0D8PJB-W5XxUNvtRqWIaS_QAj4oaeXx_tcZDVs58D30py79uEtOKQqtsczSdVMO7FBuTmkMUx8QVup9HU1C0_oXV1I3e8qNfEpmUPR8WROt5mjnsWj7rFQjY8qBBXnykMoi7wzJxw3jVNOTNDHRHr7PV9Ys_oTolG8KPqkc2i-80FMJw2SB2U7x2CuYjqK8m0IezmrgB5djSkcHdkfytDfkPLk68mgo4ZkW0ebxbwX6hESjkOgbWSXNGfszfwbM2NmCrTT371YIAhQ02uxpUToFH975h_91J4n-O39-HB5fWrWPrV0gAeT2Y_DKk4oxNBoCvePpuWPk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تایوان نخستین محموله شامل دو فروند از ۶۶ فروند جنگنده جدید F-16V Block 70 را که در سال ۲۰۱۹ به ایالات متحده سفارش داده بود، تحویل گرفت؛ تحویلی که پس از ماه‌ها تأخیر — که تا حدی ناشی از مشکلات نرم‌افزاری بود — صورت گرفت.
این قرارداد ۸ میلیارد دلاری، شمار ناوگان جنگنده‌های F-16 تایوان را به بیش از ۲۰۰ فروند می‌رساند.
وزیر دفاع تایوان اعلام کرد که انتظار می‌رود پیش از پایان سال ۲۰۲۶، تعداد بیشتری از این جنگنده‌های F-16V تحویل داده شوند.
@News_Hut
| Reuters</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/72632" target="_blank">📅 19:11 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72631">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EEP7RrkXdvcGYDqmAxPslQi4KmETDCYQMUXLF_k7uQe1aJYZAp7qbt99WXE9FPgkhNN39CbONcaN-WQXNAX10Ms9LIPiQZ_PwdKFpG3XTZIEdeRgXsSdzZSVTz-iZfLEoY-3d1R-29_XQJO2itEbhVRS1B8aSYSwiRnKt2djVr8fYJoBC7gumKbmAFTFpbbKzPLYj4Hnur0IfilRS_viKHJqXDmAgnd7BV66crZM7D4S7l0AMRH_n6XuRE8kElL--nLrVOTiYNhpYUeIJje5tnrxHnKSRbSdJUUXVVWImhQRFEPeuN8M4eKv6rbLIW0tp1HrpnP--7Zv3HfKxxANtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش «اکسیوس»، با وجود اینکه هم دولت ترامپ و هم تهران علناً اعلام کرده‌اند که خواهان پایان دیپلماتیک مناقشه هستند، دیپلماسی میان ایالات متحده و ایران همچنان در بن‌بست قرار دارد.
رویکرد دو طرف نسبت به مذاکرات، تفاوت‌های بنیادینی با یکدیگر دارد.
ترامپ خواهان دستیابی به توافقی سریع، پرسر و صدا و احتمالاً فراگیر است؛ در حالی که ایران مذاکرات طولانی‌مدت و غیرمستقیم با تمرکز بر ترتیبات محدودتر را ترجیح می‌دهد.
بی‌اعتمادی عمیق نیز بر پیچیدگی‌های این روند دیپلماتیک افزوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/72631" target="_blank">📅 18:26 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72630">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ترامپ در تروث:
اروپا به‌تازگی موافقت کرده است که حجم عظیمی از ذخایر کلان گازوئیل خود را آزاد کند.
این فرایند بلافاصله آغاز خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/72630" target="_blank">📅 17:39 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72629">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd453b2fe8.mp4?token=rmCFnxq2l6giWX25Vt7xj3gJFi81xJMQZf0iEr-76CmWMI40QCUnxBMwcWRQj4dKyjMQePsTv-4UVIdEM1Ds3hKkUgfZBFw5v2lasgqmHqKoFDt817kFpMxAjqkCNDCJwwMbDKjdrWA7tjFbn0zfVDn4H7IRRCOGIW5F8ucdCb8mNm9OEOEsAGOguLFPY96wg2Y_pt7reJdEJogkhSuh4eOiBi6s9D_prptfoA6EzIcFZ3pud4U6A2UxiPmIBRA9ZyqtBrUaeBgw4bB4Seb8AQ27XFU22FhUd4EBzZaUp24gb5Qp-RLegjYvJAZ9rEH9nNIXaQ9rkAPeDf7H72zVrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd453b2fe8.mp4?token=rmCFnxq2l6giWX25Vt7xj3gJFi81xJMQZf0iEr-76CmWMI40QCUnxBMwcWRQj4dKyjMQePsTv-4UVIdEM1Ds3hKkUgfZBFw5v2lasgqmHqKoFDt817kFpMxAjqkCNDCJwwMbDKjdrWA7tjFbn0zfVDn4H7IRRCOGIW5F8ucdCb8mNm9OEOEsAGOguLFPY96wg2Y_pt7reJdEJogkhSuh4eOiBi6s9D_prptfoA6EzIcFZ3pud4U6A2UxiPmIBRA9ZyqtBrUaeBgw4bB4Seb8AQ27XFU22FhUd4EBzZaUp24gb5Qp-RLegjYvJAZ9rEH9nNIXaQ9rkAPeDf7H72zVrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه دختر لینک کلاس مجازیشو میده به دوس پسرش و پسره هم با دارودسته رفیقاش میپرن توی کلاس و همچین صحنه ای رو رقم میزنن؛
این وسط یه کاربر با نام عباس عراقچی هم دیده میشه:))
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/72629" target="_blank">📅 17:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72628">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72628" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72628" target="_blank">📅 17:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72627">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rVsY9inBV2DmLYrQewvXNQvToZ3iVa1XKs86Awy2hbfBzpD5xWbv1o1pvEyIXFH3DeO5jVzbs5_101AZ4zvEw-wkkYtv5SFl_hchhpdH3Fj6cTZ-6snbyZFGziqS14iML_Ploh1n54GK_12LG0HOad-ixq8IliecOfXk5rPmdELaETEAKqDNHXpelacRmZDNB1W5-1_w1Ps3zzzWauzqRthvKJfi9Llmt8vZa1YQEt9Vk0LkJyOla8uZcA3FEM9SjKKtwfnFZp40UOiAjgkYNCV8t7hvsMFpe0cVOyXDspkLgpig16ez6Kn24bR84NB1rc0Z2cyYbz5bdq6anaovIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز ایتالیا
🆚
فرانسه
را در
TrexBet
پیش‌بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
ایتالیا: ۳ برد، ۱ تساوی، ۱ شکست و ۷ گل زده
فرانسه: ۳ برد، ۲ شکست و ۸ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72627" target="_blank">📅 17:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72626">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11e067ea31.mp4?token=rL0Q-ZVEHmiJdbIwFv-sjTrA0aMJko0mn5UAH4XSzaRtVSvWbNH2cNjXIQC_c08rF7d4qg7MpYl68gVn_UQpRmRpDHjcohjQ-_cg5goX_z8bJK7V_bzL6ciUK7M8iGGnUfQfp9YW_KiWnEJ13HEzEMvbQ_QjxV9FZ0mER1er-KluZD3ytleFbWdug-YxxwWmyV6ZbHKLA97MvqiAVD7lSYhxB_gpuvKtpXzsTq83AN9__wvvibwjZPC4ztjHZeiuTTve9yYHd_J-usM0inX5zvv_6jZX5sCsUEhZ_0u1ERKJLwwX9XuFVGto3jX-ClnoAiWb38sK2rFw6olJrnQ0iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11e067ea31.mp4?token=rL0Q-ZVEHmiJdbIwFv-sjTrA0aMJko0mn5UAH4XSzaRtVSvWbNH2cNjXIQC_c08rF7d4qg7MpYl68gVn_UQpRmRpDHjcohjQ-_cg5goX_z8bJK7V_bzL6ciUK7M8iGGnUfQfp9YW_KiWnEJ13HEzEMvbQ_QjxV9FZ0mER1er-KluZD3ytleFbWdug-YxxwWmyV6ZbHKLA97MvqiAVD7lSYhxB_gpuvKtpXzsTq83AN9__wvvibwjZPC4ztjHZeiuTTve9yYHd_J-usM0inX5zvv_6jZX5sCsUEhZ_0u1ERKJLwwX9XuFVGto3jX-ClnoAiWb38sK2rFw6olJrnQ0iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">احمد مجدزاده: آقای پزشکیان این اخطار آخره، اگه استعفا ندی، استعفات میدیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72626" target="_blank">📅 17:03 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72625">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad77de0b54.mp4?token=kJ9mEKnswQs45BR2hMLVvcDp-Bf7ndWlmKmAtKT8kEHOUdwbwi2TptJGdgxtuNWy-uf2wl2bKb9ogPgsFXnTEZho3LxnF2OPboLaB2wEri7xWil0REmi-FLBgPekrMtARA0WS-oRlnjxxp7zllk_d1rGmc-qG60PUh081OUXrF131_vTWTypKYGqccQ3Sf5oPHWWsDH7hr9mJ1ON-ZZS-OGXHlQXzT7kd_BTLDX3n__c1O9wATobvNI0nvT2LVN9R98TcMCdkcLaTy4dWWbs63BSRv-EZXEwm3TaMirBTB5J2R_jB2pYZsv7a6DjdcIp42AttSblDYiA2LEXXHlpuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad77de0b54.mp4?token=kJ9mEKnswQs45BR2hMLVvcDp-Bf7ndWlmKmAtKT8kEHOUdwbwi2TptJGdgxtuNWy-uf2wl2bKb9ogPgsFXnTEZho3LxnF2OPboLaB2wEri7xWil0REmi-FLBgPekrMtARA0WS-oRlnjxxp7zllk_d1rGmc-qG60PUh081OUXrF131_vTWTypKYGqccQ3Sf5oPHWWsDH7hr9mJ1ON-ZZS-OGXHlQXzT7kd_BTLDX3n__c1O9wATobvNI0nvT2LVN9R98TcMCdkcLaTy4dWWbs63BSRv-EZXEwm3TaMirBTB5J2R_jB2pYZsv7a6DjdcIp42AttSblDYiA2LEXXHlpuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده از بانوان پولدار تهرانی که میرن توی یه سری کلاس ها شرکت میکنن پول میدن تا برن اونجا گریه کنن و تخلیه بشن.
یسری انقدر پولدارن که نمیدونن پولاشونو چیکار کنن.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72625" target="_blank">📅 16:30 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72624">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa3ebce38d.mp4?token=dY8ncCXMZOuE0hHwCWr4Rn5QUlv1IHbZ68gT146aGwRpboyMjTnGWobDNffir8xQyUlIAkyjoyfvp_cTNJXbHzmguat3GchHRm9sZqEhVf0VUxHuOlk63c50zK6zm5s-3GEQ8oHM60fq-VmrGy8hjYh0OyTMLtb_tIozmyL1wZkP-9ImMz9ezmk_VAkfJ74K--_zgNH0isdcsiRj3HeSfItZUwYZEFBCXDnHcqoXpmVa2X65E6fIxVVZGjdMSMUFBmHlO0YC0GPr6sTG5ToBDQ2BXy55CLVj7y6WWQ59dJe7P7IWii1cjIUcsZ4TCvPKZ1krOY7AMGyEf6Hr7yrobw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa3ebce38d.mp4?token=dY8ncCXMZOuE0hHwCWr4Rn5QUlv1IHbZ68gT146aGwRpboyMjTnGWobDNffir8xQyUlIAkyjoyfvp_cTNJXbHzmguat3GchHRm9sZqEhVf0VUxHuOlk63c50zK6zm5s-3GEQ8oHM60fq-VmrGy8hjYh0OyTMLtb_tIozmyL1wZkP-9ImMz9ezmk_VAkfJ74K--_zgNH0isdcsiRj3HeSfItZUwYZEFBCXDnHcqoXpmVa2X65E6fIxVVZGjdMSMUFBmHlO0YC0GPr6sTG5ToBDQ2BXy55CLVj7y6WWQ59dJe7P7IWii1cjIUcsZ4TCvPKZ1krOY7AMGyEf6Hr7yrobw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دانش‌آموزان دبستانی در قزوین، در مقابل مدیر و ناظم مدرسه که آنها را با شلنگ تهدید می‌کند شعار می‌دهند؛
«این آخرین نبرده، پهلوی برمی‌گرده».
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72624" target="_blank">📅 16:03 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72623">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d885465ad.mp4?token=PyLTr9Rcqj89SzAqiGgrkWTB54sPGX8h4qFkyAX2__wXvg6devHSoe1WCc2Aav5M9YtFfqRsEIi91ux323L1s4lMjo3wK7H4q4H171YSVl0CTwzAe-QvCyXzlptK1rH9nUOEVr19gFa94wAFhFUbnlxOoQDJYSqmK8jk7B-oNxe-paQ2-QlZFnidEBhDUbBGHguuMGycf5_7BPe3bakFxNgGVNPaHRTXEy9jil6VQnQinZZ7CQK5eXwTJL40LkOTXy1Uim7wCw9CQRVEcEeUJFzPzjsTZ2OyNENZV0sNveX8BLhsiePiP4Bzjjih6k2kEPHqlpl8lQzTYMizH_8rYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d885465ad.mp4?token=PyLTr9Rcqj89SzAqiGgrkWTB54sPGX8h4qFkyAX2__wXvg6devHSoe1WCc2Aav5M9YtFfqRsEIi91ux323L1s4lMjo3wK7H4q4H171YSVl0CTwzAe-QvCyXzlptK1rH9nUOEVr19gFa94wAFhFUbnlxOoQDJYSqmK8jk7B-oNxe-paQ2-QlZFnidEBhDUbBGHguuMGycf5_7BPe3bakFxNgGVNPaHRTXEy9jil6VQnQinZZ7CQK5eXwTJL40LkOTXy1Uim7wCw9CQRVEcEeUJFzPzjsTZ2OyNENZV0sNveX8BLhsiePiP4Bzjjih6k2kEPHqlpl8lQzTYMizH_8rYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه دختر ۲۲ ساله تو تعویض روغنی با دوست پسرش در حال سکس بوده ژل روان کننده نداشتن بجاش از روغن ترمز استفاده کردن، روغن ترمز باعث خوردگی شدید پوست گوشت آلت تناسلی دوست پسرش شده و‌ بر اثر سوختگی درجه ۳ پسره فوت کرده، دختره ام بعد ۲۰ روز تو ICU بودن اومده پیش دکتر!
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/72623" target="_blank">📅 15:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72622">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNqzc9goUekA2JjDeAQtQaVxgKdCGjFymlkd0dJXs9JKiUCDzdYO5qNBXs7YqgB-Qb_dpuY4jMVQFROabVZAk8SZ6cfC0FvSOenllVAOIAU3dje6YBqrKOlYpAMRWXZtk7TQzzUAM9Q4xUDhl9FnPo12oqIuhz0zzk6n6PCCa7oDqPlu8mlwKR3r8lIDoBXkxl0_w-OV5_rGl24dog2bKxBrgbu8z1SkIiInwms2ufPyl8wmPpB9-zsOfhLPHJjhK6g2elYWhS03VmPS90vu5NzYoUCcMJ_S4RwKUDcO7MsGEPVX5cZgStJ7LdIYiYBcMgLhZudaNw1qstn3HI-wRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کارشناس رژیم، علی قلهکی:
ماجرای «پروازِ فلای دبی» هم چاشنیِ اتفاقات آینده است!
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/72622" target="_blank">📅 14:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72621">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d8bb7d42b5.mp4?token=sUwKAi_d1gyqRPXflWOqkSHvipCD4gD1B-1YofatRjNxqwnKr8Dxmd9o_jZlX110MR9zByZ7UFxb6tXeNGN6XEIFff_WA4TA9Yx_UhJz8NrWquAQuvC_r_s_Owgn3Yfo8FwW5UDYdHscRopCHGvqNUr61Ir4tBLgCgxvL_9cLgZjKSw4-qSH5a-iMPujh-3y5kJAeYWfrWxh6kshtRY75W0-mVI3VYij5l2gJqeca-jhm1sQSGlRmwcim3LgLZVjTs3XiqfmK3sIOQgX0Mez5DQ7nvZcBpsTIGoVdBlry-ZND6f8Fr_MgaoXPlIQprK8qmjUQD5z3sl7yXbrMPNIdA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d8bb7d42b5.mp4?token=sUwKAi_d1gyqRPXflWOqkSHvipCD4gD1B-1YofatRjNxqwnKr8Dxmd9o_jZlX110MR9zByZ7UFxb6tXeNGN6XEIFff_WA4TA9Yx_UhJz8NrWquAQuvC_r_s_Owgn3Yfo8FwW5UDYdHscRopCHGvqNUr61Ir4tBLgCgxvL_9cLgZjKSw4-qSH5a-iMPujh-3y5kJAeYWfrWxh6kshtRY75W0-mVI3VYij5l2gJqeca-jhm1sQSGlRmwcim3LgLZVjTs3XiqfmK3sIOQgX0Mez5DQ7nvZcBpsTIGoVdBlry-ZND6f8Fr_MgaoXPlIQprK8qmjUQD5z3sl7yXbrMPNIdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این دو خانم محترم، آبروی ایران رو خریدن و باید سر تعظیم جلوشون فرود آورد!
یه توریست و بلاگر خارجی اومده بود ایران و با دوچرخه میخواست بره یه شهر دیگه.
دو تا خانم دیدن شبه و خطرناک و تاریکه، برای همین تا مقصد، دو ساعت تمام اسکورتش کردن!
حالا این بلاگر پستشو گذاشته اینستا و تمام دنیا به مردم ایران افتخار میکنن!
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/72621" target="_blank">📅 14:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72620">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6c59bf1bb.mp4?token=AlRLRPySOtj4WeVZ4qp44Ps8h7hQuQZhKxeas2i3a7FioxzO2b7owFnhF1EWSshItp6O6mJLvFN6oEr1p2SQ-OQq1lbttKhxUy939OC6LgmHF0J99srvq4v0ybUy5nOad88IKUnMeVoaNWZ7arW1fL_qjJhPFCgqI8sQrpZJWpvL2E0LXWWcdvS0KYZ0cRXCIE1eUc5FefdIesq3pjCnSP1n-f6LPScuzeHGAQQsDjZhtAEONCC9X8mmCtytSynU1kXdDShi1ZbNr9tYZ5sEFHPW8swCI3IEn4NftDAzEfQhxqaznhFD_qygT1PK5jAX8FkwxgAijV3fdrY7GQhfsSavxoN9aZBO2nj9vdOh3L73g7LqxwNwknQ-zfsPN-JTd5KYgy3Fsis3Snz2GqPTV57r8MKT58nKgy9r9yn1Ho4enNwt-bUWCvPw7blOrN-oJyr0pm2DoireghHkqPzBUgwFeKYDtRQTTjO_8irfr9QxHt3saJezb5YExlI5MMK3VKuG0uDzz9djTUnLgW3z7euo4CAvpLQKYBJw_LkmqAdD7QuG2eAhSxozGzJ9Jmyrt2qpx82R_Ibk_XnBGpr1ElzL1ZEPkpSiAY7W2edeudaBLxNu_iFjj6q5CZGpd7b_rqTgGBNYoi_mAlNnH8mGwv_jdPIF71aTsS4fWr7GCsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6c59bf1bb.mp4?token=AlRLRPySOtj4WeVZ4qp44Ps8h7hQuQZhKxeas2i3a7FioxzO2b7owFnhF1EWSshItp6O6mJLvFN6oEr1p2SQ-OQq1lbttKhxUy939OC6LgmHF0J99srvq4v0ybUy5nOad88IKUnMeVoaNWZ7arW1fL_qjJhPFCgqI8sQrpZJWpvL2E0LXWWcdvS0KYZ0cRXCIE1eUc5FefdIesq3pjCnSP1n-f6LPScuzeHGAQQsDjZhtAEONCC9X8mmCtytSynU1kXdDShi1ZbNr9tYZ5sEFHPW8swCI3IEn4NftDAzEfQhxqaznhFD_qygT1PK5jAX8FkwxgAijV3fdrY7GQhfsSavxoN9aZBO2nj9vdOh3L73g7LqxwNwknQ-zfsPN-JTd5KYgy3Fsis3Snz2GqPTV57r8MKT58nKgy9r9yn1Ho4enNwt-bUWCvPw7blOrN-oJyr0pm2DoireghHkqPzBUgwFeKYDtRQTTjO_8irfr9QxHt3saJezb5YExlI5MMK3VKuG0uDzz9djTUnLgW3z7euo4CAvpLQKYBJw_LkmqAdD7QuG2eAhSxozGzJ9Jmyrt2qpx82R_Ibk_XnBGpr1ElzL1ZEPkpSiAY7W2edeudaBLxNu_iFjj6q5CZGpd7b_rqTgGBNYoi_mAlNnH8mGwv_jdPIF71aTsS4fWr7GCsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ناو تهاجمی آبی‌ـخاکی USS Makin Island (LHD-8) یک یگان دریایی آبی‌ـخاکی آمریکاست که هسته اصلی آن ناو تهاجمی آبی‌ـخاکی USS Makin Island (LHD-8) است و در مأموریت فعلی، سیزدهمین واحد اعزامی تفنگداران دریایی (13th MEU) را نیز با خود حمل می‌کند.
این گروه از سه شناور تشکیل می‌شود:
USS Makin Island (LHD-8) — ناو تهاجمی آبی‌ـخاکی از کلاس Wasp
USS Anchorage (LPD-23) — کشتی انتقال و پهلوگیری آبی‌ـخاکی
USS John P. Murtha (LPD-26) — کشتی انتقال و پهلوگیری آبی‌ـخاکی
چیست(13th MEU)؟
13th Marine Expeditionary Unit
یا سیزدهمین واحد اعزامی تفنگداران دریایی آمریکا یک نیروی اعزامی تفنگداران دریایی است که برای عملیات و واکنش سریع در مأموریت‌های خارج از خاک آمریکا سازمان‌دهی شده است.
در کنار ناوهای ARG فعالیت می‌کند.
ترکیبی از نیروهای رزمی، پشتیبانی و عناصر هوایی
تجهیزات و هواگردهای همراه:
همراه با 13th MEU، هواگردهایی از جمله F-35B Lightning II، MV-22B Osprey و AH-1Z Viper را در اختیار دارد. F-35Bها متعلق به اسکادران VMFA-211 هستند و از ناو USS Makin Island عملیات می‌کنند.
این گروه تا پایان نوامبر به منطقه می‌رسد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/72620" target="_blank">📅 13:55 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72619">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2a1a8f77f.mp4?token=plgr3y4kC4YspfhM7zsr6AF2-dr0YSHiU20V0rVnfpCRqJ0EH4i6ZaJS7q3RKOtQa-d62eFoCEAoY9_WwR-aHqo2TVPBB1gbWo0XPdI7sMPE5OTfRHNola9NNEi6OPNMhqs5sq6uDVfm1IQNUS2bK_jm-DnoA-KoPxf7PXDtKOXLUjLd2N2hGgkFzgamZXRXLCz9RC-1G9PCZYnQl16ptyTz-W_4amlsEbFeMt8R9cNjQN79ANkmzvBXVaAe0dY1ZM2KdvhdF5I4SeSc0sTQrLFYCk790Lw5omIScBc6ZVMn2w3KjKyPIzJvmDtXrf_z_bj-iqYrlyBX35H4oPF6HV9Xm_jwgFbOAtHcuJFjc2XEPqi-yuJhuhqJxpXqXyU-CvBjemOABM04sGMRohMpv-MYHEfAVYaFjija1H3-lP-UQ5HLB9D9_JX8Nlvd0w7xCx_Viv7P-aLq3kGrw6R2cic5wFHzeQ78AsDE7Ryq41aFKeROsPE8rkvsqfrLbvn9eg0UPeKE34Zpqw5ucNdGIKbxrgTUQy37qlqGvKCCdltgZt8Wguf1qR_vOellyEyEZKFEkyOz9hY11Ge254uqM5RPwWpATPCJaIpqqS6NOCUaaQJbwDW1x91ot31ylO3EYHgUIEfpxiNwvuFYAVCECBbIccR5RHoQOsGQqeIyTJY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2a1a8f77f.mp4?token=plgr3y4kC4YspfhM7zsr6AF2-dr0YSHiU20V0rVnfpCRqJ0EH4i6ZaJS7q3RKOtQa-d62eFoCEAoY9_WwR-aHqo2TVPBB1gbWo0XPdI7sMPE5OTfRHNola9NNEi6OPNMhqs5sq6uDVfm1IQNUS2bK_jm-DnoA-KoPxf7PXDtKOXLUjLd2N2hGgkFzgamZXRXLCz9RC-1G9PCZYnQl16ptyTz-W_4amlsEbFeMt8R9cNjQN79ANkmzvBXVaAe0dY1ZM2KdvhdF5I4SeSc0sTQrLFYCk790Lw5omIScBc6ZVMn2w3KjKyPIzJvmDtXrf_z_bj-iqYrlyBX35H4oPF6HV9Xm_jwgFbOAtHcuJFjc2XEPqi-yuJhuhqJxpXqXyU-CvBjemOABM04sGMRohMpv-MYHEfAVYaFjija1H3-lP-UQ5HLB9D9_JX8Nlvd0w7xCx_Viv7P-aLq3kGrw6R2cic5wFHzeQ78AsDE7Ryq41aFKeROsPE8rkvsqfrLbvn9eg0UPeKE34Zpqw5ucNdGIKbxrgTUQy37qlqGvKCCdltgZt8Wguf1qR_vOellyEyEZKFEkyOz9hY11Ge254uqM5RPwWpATPCJaIpqqS6NOCUaaQJbwDW1x91ot31ylO3EYHgUIEfpxiNwvuFYAVCECBbIccR5RHoQOsGQqeIyTJY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور ترامپ درباره عملیات «چکش نیمه‌شب» (Midnight Hammer):
آن‌ها تمام بمب‌ها را فرو ریختند؛ بمب‌ها مستقیماً از طریق مجراهای هوایی به داخل این... خب، کارخانه‌های مواد مخدر فرستاده شدند؛ واقعاً کارشان همین بود.
هم بحث هسته‌ای در میان بود و هم مواد مخدر.
آن‌ها مشغول تولید مواد مخدر بودند.
به این کارخانه‌های مواد مخدر و تأسیسات هسته‌ای، ضربات بسیار سنگینی وارد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/72619" target="_blank">📅 12:43 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72618">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q1VLuK8fyKLNtOH5GlsI5UcPYEIL_-ENjpOv671Z_YMXZRt2tGyK1KjKEEJqJZ35kfL9WO6qPjyu14hMJcmzlmMzw40wrxd4CehyPXYFpa7Q-tgWAjdVtOWEYzYdX5ARK_aD9Ng1xYbQI1GIN60ubgvP4H12lkVl-U2LK3jWN3uAC1keUbqe506RoD-4e1pW7EyNCe-5H-IM0KKZiK_sWJwoMcSy2FhSuBePeHu2KrXyxW8caKHVGk4e8EaB7K-1fiTpnh8DM3myW_BqBE9UnuU3X2_-24T3pxhc6DtDJ1Aqf7wms6hH0vsx8BfpEDN59yKeyv0clblPvOzTmNSkbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوووووری
؛ آکسیوس به نقل از یک مقام آمریکایی گزارش داد که گروه آماده آبی‌ـخاکی «مکین آیلند» (Makin Island ARG) و سیزدهمین واحد اعزامی تفنگداران دریایی آمریکا (13th MEU)، پایگاه نیروی دریایی سن‌دیگو در کالیفرنیا را برای استقرار در غرب آسیا ترک کرده‌اند.
انتظار می‌رود این نیروها تا پایان نوامبر به منطقه برسند.
این گروه شامل سه ناو است:
ناو تهاجمی آبی‌_خاکیUSS Makin Islandاز کلاسWasp
ناو ترابری آبی‌_خاکیUSS Anchorageاز کلاسSan Antonio
ناو ترابری آبی‌_خاکیUSS John P. Murtha از کلاسSan Antonio
این گروه همچنین ۱۰ فروند جنگنده F-35B Lightning II و حدود ۲۲۰۰ تفنگدار دریایی آمریکا را به همراه خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/72618" target="_blank">📅 11:53 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72617">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72617" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72617" target="_blank">📅 11:52 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72616">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nsvWdTRl123cJT5tnONmhhuIEXFalEnUoaRua4XZykUCDcjAfpQjUTVmuh_qR82pi26ng9e-PCiSTwpw30DrMMNjCGOpzvOiTyApAXUAExrhi1BcKdXhgxSD2vQ-wnSYZ-epnmd90BOUsWVV7NK4EVYud6b2vFqAbfiYhHX9krWVaD49MRS7Cl_BD_45m4pvyyySFALbmALaW9aZao3FoCyIRWOHq_toxgxd3wo_PXITj2OBLq_2gAA4z6u-qw6wRHGfXOZLLxG7nte7IoczdVbWqGZqe5BA3vldqS9BKXSMcyaoySrSfXTIHHLc4mhfAU9KKK6BcJU8TW8uI8v1_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین المللی
TrexBet
ترکیه
🆚
بلژیک
ایتالیا
🆚
فرانسه
سوئد
🆚
بوسنی
نروژ
🆚
ولز
ونزوئلا
🆚
کره‌ی جنوبی
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72616" target="_blank">📅 11:52 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72615">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1127789805.mp4?token=LO0d4_7Jw9M82ZPwPAEYAYFqeVydrFr1Nx_ZY2CVt_QOgiV0i9VNOWJOJcVXKiuwadxPeGakHXNEEUO46tiPNis3hipAPXh5rV3R24mcHJjkQcqhzo0yY_AuwP5PfEUfEdAfwDOe0BfQRyn6XB82Sw4Qe7FJxCAlbfp8IH4pLFsDwi1kJO1dPa58eY4f69vHqfs1ofpi2aYCsrWBdE6j-xFKowGfLLkk-l2O75EhAE3u1AvwvJ8eBoMuDfB5pd1XyLVPiaH3H2wUcuVjZh9tY7SLShnrSESCnKwGpK9siJnpe28yrF1aWPWz5aiJCrOCBN3twrFFFNQaz_VODgbYFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1127789805.mp4?token=LO0d4_7Jw9M82ZPwPAEYAYFqeVydrFr1Nx_ZY2CVt_QOgiV0i9VNOWJOJcVXKiuwadxPeGakHXNEEUO46tiPNis3hipAPXh5rV3R24mcHJjkQcqhzo0yY_AuwP5PfEUfEdAfwDOe0BfQRyn6XB82Sw4Qe7FJxCAlbfp8IH4pLFsDwi1kJO1dPa58eY4f69vHqfs1ofpi2aYCsrWBdE6j-xFKowGfLLkk-l2O75EhAE3u1AvwvJ8eBoMuDfB5pd1XyLVPiaH3H2wUcuVjZh9tY7SLShnrSESCnKwGpK9siJnpe28yrF1aWPWz5aiJCrOCBN3twrFFFNQaz_VODgbYFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی هند یه میمون یهویی وارد مشروب فروشی شده و انقدر مشروب خورده که به این روز افتاده :
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72615" target="_blank">📅 11:00 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72614">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hKlyNxO2c1nyR1a5ynChidF5X8VcS8K-6x-2yLfdpzqbw0gyer_c2tIDBvBilUp1x9zWNUo6_k234trN8njsWVedDimwkd2W9X-waXuLpIOjsAOimSbL351YZD2Sl5WDE0pVjpPyn_XM5BVgq0wnch5Z1GZihIl3reyA-oVAsDgWOCEauLvjeyvCRKka_od-kFaHbpFNa-gvRnFjfKnNcsoAwCOYVbkkOARyxbK8GHbf5Oh8tEEGaZGmF2szHgSv2gba3e7PDFPVzh30iqhTUz_oS8Xrmw4IcFqiwJmTj2J-75AKVZ_a1LFScCCy58CQ6GKXtjrGKHiBq3JnImKNaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسنت، وزیر خزانه‌داری آمریکا:
ایران در ماه سپتامبر حتی یک بشکه نفت خام هم روی نفتکش‌ها بارگیری نکرده.
دولت ترامپ در حال قطع کردن مهم‌ترین منبع درآمد حکومت ایرانه.
عملیات «طرد اقتصادی» در حال قطع کردن شریان‌های اقتصادی‌ایه که به تهران اجازه داده برنامه‌های تروریستی خودش رو تأمین مالی کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/72614" target="_blank">📅 10:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72613">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c00080542.mp4?token=qroakKq7KKh6U2nqBr4z-i1lomRe_3aD2qkr0HRncLPObHrjgeVfQfo-sbeJPCsxmb7RT3X217BQH3ulLB7ukhkCq2OqW0SeuOxUJIT8k1Saxm38dPaANF4G079S4h229DrfW_O2WXyUNIdyHZ1lwZTvEOr7dRfOvsJXnAAdZSy8NaW5MLaTNS4w_qhZsWl51jIqZK40TA2C2soqiGF6fxf_UCvVoq4Y9nqsujV1pWVE1XZ8tT__mJe5EkQbnbDnrh_Fof_2lLAiumwY1AbfjD30KxewVoN1lDwY8Y3gfcVwcXfoZTuOYM13erRxyX8XPH2y-EjX3zg92cEwMIEzvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c00080542.mp4?token=qroakKq7KKh6U2nqBr4z-i1lomRe_3aD2qkr0HRncLPObHrjgeVfQfo-sbeJPCsxmb7RT3X217BQH3ulLB7ukhkCq2OqW0SeuOxUJIT8k1Saxm38dPaANF4G079S4h229DrfW_O2WXyUNIdyHZ1lwZTvEOr7dRfOvsJXnAAdZSy8NaW5MLaTNS4w_qhZsWl51jIqZK40TA2C2soqiGF6fxf_UCvVoq4Y9nqsujV1pWVE1XZ8tT__mJe5EkQbnbDnrh_Fof_2lLAiumwY1AbfjD30KxewVoN1lDwY8Y3gfcVwcXfoZTuOYM13erRxyX8XPH2y-EjX3zg92cEwMIEzvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک اخوند در تجمعات شبانه: دو شب پیش رهبری نیم ساعت در تجمع شبانه حضور داشتند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72613" target="_blank">📅 09:58 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72611">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a16936d012.mp4?token=G-5z3DVvKDCJM17zT8ptEMec9j0hszExWZpRdATTprnBpp7B8nBoHrVrMgm6Crard-9BtB8DA4HyeiSKxaqUoXYEbGwwnnlalfr1Fejz61FltOsdaJDcdnDjgf5nVt2Oc7sLr6fnNoq9xSsVxtqZUwMf7ZCJOb1pE7p7WK8swbD7RCJgIZSQq5YFjDr2lFnuRzs19Ws62vNsZXpyfGwJ6cYxL5UQYLXpPfY-gwWmYvY893kuWfPbjzgYgAGAThMazeKd5-IGHb5cysKSLKH_snzy5j3PCYinL41qh0EkqV6-qM_etqFKSEE7kJX5MjssvkiIqK9b4VWvw3z7XoVV-g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a16936d012.mp4?token=G-5z3DVvKDCJM17zT8ptEMec9j0hszExWZpRdATTprnBpp7B8nBoHrVrMgm6Crard-9BtB8DA4HyeiSKxaqUoXYEbGwwnnlalfr1Fejz61FltOsdaJDcdnDjgf5nVt2Oc7sLr6fnNoq9xSsVxtqZUwMf7ZCJOb1pE7p7WK8swbD7RCJgIZSQq5YFjDr2lFnuRzs19Ws62vNsZXpyfGwJ6cYxL5UQYLXpPfY-gwWmYvY893kuWfPbjzgYgAGAThMazeKd5-IGHb5cysKSLKH_snzy5j3PCYinL41qh0EkqV6-qM_etqFKSEE7kJX5MjssvkiIqK9b4VWvw3z7XoVV-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به تازگی توی مملکت یه سری مهمونی میگیرن که توش با تم و استایل دهه هشتادی شرکت میکنن :))
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72611" target="_blank">📅 09:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72610">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OS76hOXgT4HYx4Ihn_fRRILMZJCZrXlLbVUQ-CtTwx7Ak2t5dZB6P_4DWJJ1xq1fGEtLbjH5sC7uD4ncCEXun6Acx-pHZuP0TGut3Zpbydh-GQSFFLSg_p6e6iG2hKBYFQjRe8zO6YkULpzaTu3xBMjr0DW6mRH3_v-3uP5LuIGeSYGwEQwB5Eptqh76xAdwFfZkuGRedNkQqh2KzAniqhOWLA0RyHlsKJp8pi5pfiYEwYI22c4Zmka-6GZHM3j5YTcNyLhHLgDktE248zRxZCNCTwactzbA9pzeiVNpF0OclZre3N4rlCRs3hruJvCXKNqSArjW1RjbEXueBujOBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خزانه‌داری ایالات متحده با اعمال تحریم‌های جدید علیه بخش‌های خودروسازی، ریلی، تولیدی و فولاد ایران، دامنه «عملیات طرد اقتصادی» (Operation Economic Outcast) را گسترش داد؛ بخش‌هایی که به گفته واشنگتن، با کاهش درآمدهای نفتی ایران در پی محاصره دریایی آمریکا، اهمیت فزاینده‌ای یافته‌اند.
وزارت خزانه‌داری مجوزهای جدیدی برای اعمال تحریم‌های بخشی علیه صنایع خودروسازی و ریلی ایران صادر کرد و شرکت‌های بزرگ خودروسازی از جمله «ایران‌خودرو»، «سایپا»، «ایران‌خودرو دیزل»، «پارس‌خودرو»، «زامیاد» و دو شرکت «نیرو موتور» را در فهرست تحریم‌ها قرار داد.
همچنین تأمین‌کنندگان خارجی در اندونزی، امارات متحده عربی، ترکیه و هنگ‌کنگ به اتهام تأمین قطعات خودرو برای تولیدکنندگان ایرانی و کمک به حفظ شبکه‌های تدارکاتی بین‌المللی آن‌ها، تحریم شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72610" target="_blank">📅 09:03 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72609">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72609" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72609" target="_blank">📅 01:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72608">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XC5qqd-MnE3jMx4Wr58juJFt9JeI-lNf1BEzdAyBR3vUupmztOeQAFti-ZJaLsSZ-hpHUZgcftCv6_M0B8syq7ceGRPNDTTg7AQTKfC2a2gmz2j7ruPHKDVROGeuETUArGdwlK-nj2iOIFdPPz-0_vpN6eidWs37R_SFy_sSEQezjo_9AZjTf_qidRieGA4pN9qTjvdIY4D1XXVOX7Q2G6YEisNdHqiIQIijPyOhfPtioXRp-MadtuQBigGKfVFuu4liPnY5DWGV7BqYd4wIBFceRV9HFDqKCMbOjn_bgS75P69tSK3UaWilmMnsLXCQneWGWru7n27_mC3lEV_fFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
🦖
قوانین رو در سایت مطالعه کنید
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/72608" target="_blank">📅 01:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72607">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5821a90294.mp4?token=a7j9-zATxfBrSufdZ0JGcAxTfc6tvdufBsIHOPzFv24Mfm_yYVxR-_ISX95CtCGrakRAh5NpgHPQItmCSBINl8Ma5x6ViPKBkqPa1Pfq_pAx14TaqS86-9L3W8Hzal9EAsAnqcaz4lFq4_jJrBRwf3dpVRhx93ZxJmscPtnZ8Gdw14gPkapFcZYcY0ghFMLOQbbfBR1xpVnXvjBjJmSpWSbm05eYKtIuPPmfYg5shNn5u5DOHr8Fa8hw5kT-IE7-4XUpMRMY8CVqLnr5TBYq4aAuBNl-gXW6xasd_Wf9v4RhiwUo0K4hQlgOlnWJ_iPJxqbcgv6jayR8N3C2KgpN8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5821a90294.mp4?token=a7j9-zATxfBrSufdZ0JGcAxTfc6tvdufBsIHOPzFv24Mfm_yYVxR-_ISX95CtCGrakRAh5NpgHPQItmCSBINl8Ma5x6ViPKBkqPa1Pfq_pAx14TaqS86-9L3W8Hzal9EAsAnqcaz4lFq4_jJrBRwf3dpVRhx93ZxJmscPtnZ8Gdw14gPkapFcZYcY0ghFMLOQbbfBR1xpVnXvjBjJmSpWSbm05eYKtIuPPmfYg5shNn5u5DOHr8Fa8hw5kT-IE7-4XUpMRMY8CVqLnr5TBYq4aAuBNl-gXW6xasd_Wf9v4RhiwUo0K4hQlgOlnWJ_iPJxqbcgv6jayR8N3C2KgpN8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛ترامپ درباره ایران:
یا کار بسیار درست و هوشمندانه‌ای انجام می‌دهند، یا عمرشان چندان طولانی نخواهد بود.
وقتی با آن‌ها توافق می‌کنید، بسیار محتمل است که به آن پایبند نمانند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72607" target="_blank">📅 01:47 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72606">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd837a9d25.mp4?token=EW69dzMF50rkSiyNQvvDk9wbbWh1xO_wJfZ62KvvMaSk0nEhktl9R0PMgtpDwH3-DD7_imFWL92y8VwS7YQr-bcVRiERW5prHI9IeA6KVyipVH4hNr8RfqYNsG_Tx_12bvNO41pKzkQezXhxjqcPH75RAcQezPrPgPpFfRSmMFQevODS7QnZJT61OZ6MaIRpVUmLO4OfhIRb8TPVCmcrXgYyJPQp6jmqOCMpFDR8sp8-UOTJAJn5bmAHEsqnO_LPuLmnp0A0onjE-SZ0fZDvXP7eNw2kcN1k1flG-6BULthe-7K_pQUeBUsDmBfSO_F5zneG82lq0s4RJHgTGgFlNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd837a9d25.mp4?token=EW69dzMF50rkSiyNQvvDk9wbbWh1xO_wJfZ62KvvMaSk0nEhktl9R0PMgtpDwH3-DD7_imFWL92y8VwS7YQr-bcVRiERW5prHI9IeA6KVyipVH4hNr8RfqYNsG_Tx_12bvNO41pKzkQezXhxjqcPH75RAcQezPrPgPpFfRSmMFQevODS7QnZJT61OZ6MaIRpVUmLO4OfhIRb8TPVCmcrXgYyJPQp6jmqOCMpFDR8sp8-UOTJAJn5bmAHEsqnO_LPuLmnp0A0onjE-SZ0fZDvXP7eNw2kcN1k1flG-6BULthe-7K_pQUeBUsDmBfSO_F5zneG82lq0s4RJHgTGgFlNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
ایران در فوریه ۲۰۲۶، تنها سه تا چهار هفته با دستیابی به سلاح هسته‌ای فاصله داشت؛ شاید هم زودتر.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72606" target="_blank">📅 01:43 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72605">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69424629e7.mp4?token=k8B48GJsBw3_Iu7fMCJHtHfzP9unU6MBsTYBumlP36whEycIrarTl2Qg9DOBpRBOB_9dNn_KFlEYc0KoEKqKRWgItI9L6NrFxPzoKB6os5c494ZFCDVm6C6UvkdR48plH3kclmoEJLK3vVzJkHDsjDz_hc23xCiXzLne-777Cu5_0LDhzqD0T4UhO6tferBd8C6nJcgHHl4pAXNao4pqL3jZq63td4HGIZxvMCYVVWFopknbchTsZsArMU1vsULLf7DWnEELA9ha6Gy5qtgdQPMwyEzHMiNQ7lZXYCtEb7XPJHNNnsor90PAGXUS-R98Spzlbax0hgSRM9UTpmGNrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69424629e7.mp4?token=k8B48GJsBw3_Iu7fMCJHtHfzP9unU6MBsTYBumlP36whEycIrarTl2Qg9DOBpRBOB_9dNn_KFlEYc0KoEKqKRWgItI9L6NrFxPzoKB6os5c494ZFCDVm6C6UvkdR48plH3kclmoEJLK3vVzJkHDsjDz_hc23xCiXzLne-777Cu5_0LDhzqD0T4UhO6tferBd8C6nJcgHHl4pAXNao4pqL3jZq63td4HGIZxvMCYVVWFopknbchTsZsArMU1vsULLf7DWnEELA9ha6Gy5qtgdQPMwyEzHMiNQ7lZXYCtEb7XPJHNNnsor90PAGXUS-R98Spzlbax0hgSRM9UTpmGNrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ونزوئلا:
ونزوئلا تماماً تجهیزات روسی و چینی داشت. ما همه آن مزخرفات را از کار انداختیم؛ آن‌ها کار نمی‌کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72605" target="_blank">📅 01:42 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72604">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d2bdd7600.mp4?token=TSzua2HUS5LeNqhzg6GjaAuRO5TSOjL7z3SLr_kWqf3IoLd7zwEMwXI-ocd73nHp4nmHCbRxL2jrbX9JJ13f2t-Vou28z7UepG00sli0JOcAG3hvwAj3MG7YVqaLNZxthVBoSAc-JKoiEbUxw-66XsJcA_1FobDFj_PTa8qRTj9rHG1jGA8mFctGg_VCF0mp-CKk8OG61riipitXCdYdzA9DIX-psgrm4oNUzS8EsDQtTilWw8h5kLRcRboy9KhJ-bHFNXDrrRqv99bAUXc_bBB1LQuOW7YpXn4r_qdHWf6wxbNDsxySffPb51WCGMXahG6klxXNsxtGlBPYxi92Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d2bdd7600.mp4?token=TSzua2HUS5LeNqhzg6GjaAuRO5TSOjL7z3SLr_kWqf3IoLd7zwEMwXI-ocd73nHp4nmHCbRxL2jrbX9JJ13f2t-Vou28z7UepG00sli0JOcAG3hvwAj3MG7YVqaLNZxthVBoSAc-JKoiEbUxw-66XsJcA_1FobDFj_PTa8qRTj9rHG1jGA8mFctGg_VCF0mp-CKk8OG61riipitXCdYdzA9DIX-psgrm4oNUzS8EsDQtTilWw8h5kLRcRboy9KhJ-bHFNXDrrRqv99bAUXc_bBB1LQuOW7YpXn4r_qdHWf6wxbNDsxySffPb51WCGMXahG6klxXNsxtGlBPYxi92Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
رؤسای جمهور [پیشین] ایران دیگر با ما نیستند، اما سعی داریم با فرد فعلی خوش‌رفتار باشیم.
بالاخره باید با کسی کنار بیاییم، مگر نه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/72604" target="_blank">📅 01:39 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72603">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ترامپ درباره ایران: ایران آماده تسلیم شدن است. ما همین حالا خیلی راحت پیروز خواهیم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/72603" target="_blank">📅 01:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72601">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9371c09764.mp4?token=Chv_5N-rtBRkvsaHFsmDXLvcoP-OLNXKnGARgPZ1wQ2StYK_ZPo31kU0QgCopz8R8hq4wBSgjxJfKOjCU9WBORFnhAS5vtkbA5ob8IaNgzqSfGnQViLCflNHT942pYJ4-yEB-AyhhmT0p6-jAOOvHFbUxu_H9ghu6aeVaTjBD4MgrIM_HZ-qyTgx2i-pnZjtLNaR1VCO-Wo3WECsZ3cmvFowQIzOXQ9v4PxUjM5Obav_2HJI0Vy3_k3L3aIlnuU06Ukr06UyrPfrBPmWFTER7pAPL9TfE4-Djm1sscMke_6TuEE5E3OfxR5zVQPL59N254iRpBMYeHgUEAaErKDxYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9371c09764.mp4?token=Chv_5N-rtBRkvsaHFsmDXLvcoP-OLNXKnGARgPZ1wQ2StYK_ZPo31kU0QgCopz8R8hq4wBSgjxJfKOjCU9WBORFnhAS5vtkbA5ob8IaNgzqSfGnQViLCflNHT942pYJ4-yEB-AyhhmT0p6-jAOOvHFbUxu_H9ghu6aeVaTjBD4MgrIM_HZ-qyTgx2i-pnZjtLNaR1VCO-Wo3WECsZ3cmvFowQIzOXQ9v4PxUjM5Obav_2HJI0Vy3_k3L3aIlnuU06Ukr06UyrPfrBPmWFTER7pAPL9TfE4-Djm1sscMke_6TuEE5E3OfxR5zVQPL59N254iRpBMYeHgUEAaErKDxYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛مامور های عربستان یه شخصی رو که قصد انجام عملیات انتحاری داشت در مسجدالحرام (خانه خدا)دستگیر کردن:
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/72601" target="_blank">📅 00:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72600">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c38d02b25b.mp4?token=vH9fMWGA6P5NfHzQRLr0RtDIj_vg5FGm3YsQAVCvaoVlH5jlC2WwAb64J0nt-4IBE3xQhp89YBpNgcZuSm64iU2RtuX2XUrOBUGbR-yIOmPjfky97NNM-nkE6zdcvPRZJrcSW_WqT0z28qvnS7mckt_RbkqDepEEfJgD7fHkK7PRkkRyYMGLCvuiZwZP2j5eLAWT1g4DShr4TOlE5aoLEiqtmqxTbyWCGra8hHiz0JsK8JtAcARyButrmoP9BArzMF09eDVRRdw-qHXI2jgp1Xo0_rb9AQmLFHSS_uD68gXP86x5HkGAbJCPNoOjoCs4wRJLD7bgabsqzwKw0i93Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c38d02b25b.mp4?token=vH9fMWGA6P5NfHzQRLr0RtDIj_vg5FGm3YsQAVCvaoVlH5jlC2WwAb64J0nt-4IBE3xQhp89YBpNgcZuSm64iU2RtuX2XUrOBUGbR-yIOmPjfky97NNM-nkE6zdcvPRZJrcSW_WqT0z28qvnS7mckt_RbkqDepEEfJgD7fHkK7PRkkRyYMGLCvuiZwZP2j5eLAWT1g4DShr4TOlE5aoLEiqtmqxTbyWCGra8hHiz0JsK8JtAcARyButrmoP9BArzMF09eDVRRdw-qHXI2jgp1Xo0_rb9AQmLFHSS_uD68gXP86x5HkGAbJCPNoOjoCs4wRJLD7bgabsqzwKw0i93Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سؤال: آیا ایران در حادثه «آر.ای.اف فیرفورد» (RAF Fairford) نقش داشت؟
ترامپ: بله، ظاهراً همین‌طور است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72600" target="_blank">📅 00:15 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72599">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E24Vxbz1MoprIxcvfpU3voRsDCQjgxY8L0vjY0LZWrY2Ag64vFBQarnway9vhc-5JoJCDZCSlunYUxnYd_LT2qbjxeLbm41uiDNyMXNlDigKC5jnfixFEqqygF308_-Xe50Yi96MAAMans2uDjN2wrh8Rtql5rUiXBQwCweOtKlEMBAa6ABn7OikQDmSAHl3M_ctem_8IUH3m3f5kRS_L8ehG47NeJsrTSfoWgmBXYxVzlO5oyH7Fh3jNbDR3It6pzbkr8PtOFNc-mhz3X7QAKW1IClbLREpWKLICxykyz3n-c3l7oGQ_xAVDL5-meGj-bPlV9f44EPRjkcaZX7cTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش وال استریت ژورنال، ده‌ها نفتکش ایرانی و مرتبط با ایران در آب‌های آسیا سرگردان مانده‌اند، زیرا ایالات متحده فشار بر کشورها و شرکت‌هایی را که به کشتی‌های درگیر در تجارت نفت تحریم‌شده ایران خدمات می‌دهند، تشدید کرده است.
حدود ۲۰ نفتکش خالی ایرانی تنها در سریلانکا سرگردان هستند و برخی از خدمه با کمبود غذا، سوخت و آب شیرین مواجه هستند.
از زمان اعمال مجدد محاصره تنگه هرمز توسط ایالات متحده در ماه ژوئیه، کشتی‌های دیگری در نزدیکی مالزی، هند و چین سرگردان شده‌اند و از بازگشت بسیاری از کشتی‌ها به ایران جلوگیری کرده‌اند.
واشنگتن همچنین به سریلانکا فشار آورده است تا از تأمین کشتی‌های تحریم‌شده توسط شرکت‌های محلی جلوگیری کند و به آنها در مورد تحریم‌های ثانویه هشدار داده است. فشارهای مشابه و افزایش اقدامات تنبیهی در سایر نقاط آسیا، بنادر و شرکت‌های دریایی را به طور فزاینده‌ای نسبت به خدمات‌رسانی به کشتی‌های ایرانی بی‌میل کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/72599" target="_blank">📅 23:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72598">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bce71f4cf.mp4?token=v-sBBndJ7liL32vJrOG11biNf_WEXJ_l4Z1SrrmVmGj93dklYfUefnbS9ThBLJVynbW8b5u5UuERWrUB6NLhKNAYrF7uVJ_smt0Jak4sPDSlBKDOB9aF2WNToyf4XM1jOdwgcxl2nExEOtNgZRB64g4jXsqaAyBq-aqnhmPpHnAg9N5mNzz0Hb-uZG7Y-S_D6YYc6bmUJB-2HtQVlQnKGv5SjFCOdMB_DT6rvnD7yrS0YQB9rpWrUqzFKF4__VRJCGlIMP4_fDA5Z_uj06ExBlv3LSFr7bbhb-0VDlb0AAyhN4uWobNe3ujNLazh2IoaTR3CUQY_Np9qRFYdQ64B1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bce71f4cf.mp4?token=v-sBBndJ7liL32vJrOG11biNf_WEXJ_l4Z1SrrmVmGj93dklYfUefnbS9ThBLJVynbW8b5u5UuERWrUB6NLhKNAYrF7uVJ_smt0Jak4sPDSlBKDOB9aF2WNToyf4XM1jOdwgcxl2nExEOtNgZRB64g4jXsqaAyBq-aqnhmPpHnAg9N5mNzz0Hb-uZG7Y-S_D6YYc6bmUJB-2HtQVlQnKGv5SjFCOdMB_DT6rvnD7yrS0YQB9rpWrUqzFKF4__VRJCGlIMP4_fDA5Z_uj06ExBlv3LSFr7bbhb-0VDlb0AAyhN4uWobNe3ujNLazh2IoaTR3CUQY_Np9qRFYdQ64B1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با پیشرفت هوش‌مصنوعی، حضور و غیاب تو مدارس هم شکلش عوض شده و به این صورت با تشخیص چهره انجام میشه :
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/72598" target="_blank">📅 23:14 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72597">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Abnc_bkBPxjUobjj8s_Vo_zt5A5rpUYPsE0_asfsEAlkU1_EhyPQlNw94EKtBmxDRVyjLVJ0wyJ2vU9PONDPjW1IZES84lttu-ypaK0jV_c565iJilaqVhgJXx4s9aj6-WUMei768gKhsYIHW7oH-jF1g_B3P2dev9mJpwXFtCBp6FHqeqmXnjw8MW2QyaNx-E_fI2T_URXJQ5zSKLeGaOn-RcaXgK1T8JifN-znCa-JLYI7HK7XDDEjuV5HpE_v-aUjQMzDbFifX2GcCEMerJtPdC7sB67o3VKnvamdFVuJgGV_SuyXGtTAb-xMSRKONSp40M83Ui1KcV1tzGU5xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛پلیس بریتانیا اعلام کرد که یک تبعه ۲۷ ساله با تابعیت دوگانه بریتانیایی-ایرانی را در مرکز لندن به ظن «تدارک اقدامات تروریستی» بازداشت کرده است؛ اقدامی که با حادثه روز یکشنبه در نزدیکی یک پایگاه هوایی در انگلستان (که مورد استفاده ارتش ایالات متحده است) مرتبط دانسته می‌شود.
دو ملک در این منطقه مورد بازرسی قرار گرفتند.
مأموران مبارزه با تروریسم همچنین از مرد دیگری که تبعه ۲۶ ساله بریتانیاست، بازجویی کردند.
ویکی ایوانز، هماهنگ‌کننده ارشد ملی در بخش پلیس مبارزه با تروریسم، تحقیقات مربوط به پرونده «گلاسترشر» را «بسیار پیچیده» توصیف کرد و اظهار داشت که تیم‌های تخصصی در حال پیگیری «چندین خط تحقیقاتی» هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/72597" target="_blank">📅 22:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72595">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KYEiewNQSQsKpAzNIXiFjCZNNrBWn9uy5hTLNfaPC9fupmezwxG-PIsXYkl2T3_pbEuDhrPCz1CufnZ3YfpBYNuHKxGJL9QiUDTg73ZsM_5hDpvurzVGaMFie8amfaPYDaxqZvn-DX82_Gsk485X60QX9F0dKgDgzNsKEPqdiEu6sh9672LXCCXtT7p-sH8A1CB4d3yhOIYef_k_G0kK-vRIFzFh_GnoKmD29JrU1dil4XHjBxdY4KfXiF6kK-u2yNCsIo9RKHlWazHKcP6Crx3Vw-BFdL1XxQdlqydbCcYMRJqwh0WnxFQo4ssirhLSnorwfIztW-lj9PWuT8WOJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b5d4066c.mp4?token=Kd55IVsHsCitnDtcyF5n8BiSWRubqAD2Bx13USDBEbPbrPjxP6qGsmE1wJAsDf5vLo6NHnfG5Vsv4kGU_sxomq3MidGenOjvHnNYsEyLYjk69Y-Fv4Q0TfmIs_eFrlOHKAJG1C2BHvEakKMwmGKjvvcT6zvYnVnbAm2waLrMHV-DReHtDWZK4SArARK7-TxCmiXHQ9H2Oh-fqV2XlrjPrtoPbJZ3ceWyFxuJby9vmREheq8da5GkaG8mKh4oxGbFhhSEtGYIUBgdhqBY5R96ODau9zbhMhqPqD-dEqySgT-4EuGoUSakv4-Zhm6yL_4h8oLwvJmM47SHtP40acyAtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b5d4066c.mp4?token=Kd55IVsHsCitnDtcyF5n8BiSWRubqAD2Bx13USDBEbPbrPjxP6qGsmE1wJAsDf5vLo6NHnfG5Vsv4kGU_sxomq3MidGenOjvHnNYsEyLYjk69Y-Fv4Q0TfmIs_eFrlOHKAJG1C2BHvEakKMwmGKjvvcT6zvYnVnbAm2waLrMHV-DReHtDWZK4SArARK7-TxCmiXHQ9H2Oh-fqV2XlrjPrtoPbJZ3ceWyFxuJby9vmREheq8da5GkaG8mKh4oxGbFhhSEtGYIUBgdhqBY5R96ODau9zbhMhqPqD-dEqySgT-4EuGoUSakv4-Zhm6yL_4h8oLwvJmM47SHtP40acyAtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوووری
؛ترامپ در‌تروث پستی از اعتراضات دی‌ماه ایران منتشر کرد که مردم در آن شعار میدهند «امسال سال خونه سید علی سرنگونه»
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/72595" target="_blank">📅 21:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72594">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BEnCBM1fHtRazf-QOY3geUSjmJPe86AHmokZO7DFsqeMcrOHHnDUJ-QACIQDRbHM5zLPKgZL2S8T1nKcq9E2jsh_bGoeMPHr22uEe73wuFADGIGPW5GxC4gYNFWB_lO1uXZq_e1dtG3hzkQFg_-ybO8q_sZQ4YxF-9B9yA4d1SSQvK4KRr_4l88m7WugpNzMBx2GGQKzrfzkQ0uBAAW2bsvyzm80WceZDFAohfza5Qm9DMzwkTZbwMNMmh3DgLhJMAailb5Tc5i6ARnrFhIAY7C4bhSKzo3su4e9vgxfi4NlXG1S-YC3Om2GFvqJcwsDT_jp5fnnLM9faQk-FTqoJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرزیدنت ترامپ:
«گفتم برای از بین بردن تهدید هسته‌ای ایران ۴ تا ۶ هفته زمان لازم است، اما این کار را در یک شب انجام دادم. زمان باقی‌مانده برای اطمینان از این بود که این تهدید دوباره بازنگردد.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/72594" target="_blank">📅 21:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72593">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/210cf276f7.mp4?token=XD_pJ8Hx_sP52exPeYCZomWFZyXxzhM1IFBTVob_jUwNPIqFHrsmHGRF2Ewpe6Xot_UT1Zd4vTftfequBhdP5wXXnEN07LQja7zfbr4emTbsbMeSShi0waFJcHZDiJO5AhncwguFm7UZ2ZYBmtGLtrgKwqpBV1MDGJJCdFdWV9_Kcpn9pP-3kLIdTKSP3o0pP6Ms7J7XrtPouT9MUF2Q6qH8Iq7iB2K0B_ZMCDi4zTBG02BLOxEfYz7s6P2S_hXJtl3IFlWmhSa6B5Lb2mTkeo0adqaXbALfGmCVecXSJ4soq4PMfeVCTBGoke26XUDCS0_CFpFS33yYaCBa8K3PFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/210cf276f7.mp4?token=XD_pJ8Hx_sP52exPeYCZomWFZyXxzhM1IFBTVob_jUwNPIqFHrsmHGRF2Ewpe6Xot_UT1Zd4vTftfequBhdP5wXXnEN07LQja7zfbr4emTbsbMeSShi0waFJcHZDiJO5AhncwguFm7UZ2ZYBmtGLtrgKwqpBV1MDGJJCdFdWV9_Kcpn9pP-3kLIdTKSP3o0pP6Ms7J7XrtPouT9MUF2Q6qH8Iq7iB2K0B_ZMCDi4zTBG02BLOxEfYz7s6P2S_hXJtl3IFlWmhSa6B5Lb2mTkeo0adqaXbALfGmCVecXSJ4soq4PMfeVCTBGoke26XUDCS0_CFpFS33yYaCBa8K3PFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیتر دوسی (از شبکه فاکس): آیا ممکن است این خلبان [در پرواز فلای‌دبی] توسط سپاه پاسداران در آنجا منصوب شده باشد، یا به طریقی دیگر افراطی شده و سپس تلاش کرده باشد هواپیما را سرنگون کند؟
ترامپ: بله، ممکن است همین‌طور بوده باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/72593" target="_blank">📅 20:54 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72592">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31205a46fc.mp4?token=Qv0r-gmPmRXi_uJPzSNvBgSUnX9p8IjRZSUW2zzdpmDRXJJGk3KBOo6dLybnTFVn2NMJ4UEpBlnTw0JvxptYkn0-gQNpyBSmoa1MKR1Fz2vV5reLJNpVidLVbmB0_GJ6c45ZXwn7n5zfH6fgIYxIPf83tWvk-9z0hbETmyFb9EfIbqlg2hWNjG8ZV0xRt_uCI34ihg-7OaBok0PGIAroNo1_jVNSlGWrC0a0FXOKsIqV4oBqMzBZPlc3uv3t9RpVu1-UBuW6f0etEKZS6X7gu10DsbqDgpMKnDsKC7q9SRtYf6CI17TSoF-UyKM_WCPNFkfD94Ug8qxtGIPzwa4FJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31205a46fc.mp4?token=Qv0r-gmPmRXi_uJPzSNvBgSUnX9p8IjRZSUW2zzdpmDRXJJGk3KBOo6dLybnTFVn2NMJ4UEpBlnTw0JvxptYkn0-gQNpyBSmoa1MKR1Fz2vV5reLJNpVidLVbmB0_GJ6c45ZXwn7n5zfH6fgIYxIPf83tWvk-9z0hbETmyFb9EfIbqlg2hWNjG8ZV0xRt_uCI34ihg-7OaBok0PGIAroNo1_jVNSlGWrC0a0FXOKsIqV4oBqMzBZPlc3uv3t9RpVu1-UBuW6f0etEKZS6X7gu10DsbqDgpMKnDsKC7q9SRtYf6CI17TSoF-UyKM_WCPNFkfD94Ug8qxtGIPzwa4FJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اظهارات ترامپ درباره احتمال دخالت ایران در حادثه هواپیمای فلای‌دبی:
بر اساس آنچه می‌شنوم، پاسخ را «بله» می‌دانم، اما در حال حاضر مشغول بررسی آن هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72592" target="_blank">📅 20:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72591">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b0dca1ef0.mp4?token=u4313c02RVtBiqEThZ-qny-AGehxoGd5v6O6G4qcXh33kbAlw0pwJRtza84k6-dUdmc6SxGUvrHW5fqxLP9wKScxstbIbJ5bkSKznTERylZf-3pEvpsv5bfthR2xpJUXnyOfQZBWBJlbsYa1D8_emCC_q6ILFCt_CnG5i_9OPHdnm76kCEsCU6CYTBADh7MT2iRykQ6QSEGKDBDUdRFtug879yL5l2oYcCR-yOCkg9OhKCikC__G1dykHSlgH1S5fWPjRD3l-Gl3Hbo0BWtFT-Yd3GOfcFHpu1zq92_lVZExMs3coIE-HvQk0WiXdp1glKSrmjFcChOzqnp6FzBOdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b0dca1ef0.mp4?token=u4313c02RVtBiqEThZ-qny-AGehxoGd5v6O6G4qcXh33kbAlw0pwJRtza84k6-dUdmc6SxGUvrHW5fqxLP9wKScxstbIbJ5bkSKznTERylZf-3pEvpsv5bfthR2xpJUXnyOfQZBWBJlbsYa1D8_emCC_q6ILFCt_CnG5i_9OPHdnm76kCEsCU6CYTBADh7MT2iRykQ6QSEGKDBDUdRFtug879yL5l2oYcCR-yOCkg9OhKCikC__G1dykHSlgH1S5fWPjRD3l-Gl3Hbo0BWtFT-Yd3GOfcFHpu1zq92_lVZExMs3coIE-HvQk0WiXdp1glKSrmjFcChOzqnp6FzBOdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#مهم
:سؤال: در مورد نیروهای نیابتی ایران، مثل حزب‌الله، چطور؟
ترامپ: سرنوشت آن‌ها به سرنوشت ایران گره خورده است؛ هر مسیری که ایران طی کند، آن‌ها نیز همان مسیر را طی می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72591" target="_blank">📅 20:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72590">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ترامپ درباره ایران:
به جرئت می‌گویم که صددرصد مردم — از جمله در سراسر جهان — با دستیابی ایران به سلاح هسته‌ای مخالف‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72590" target="_blank">📅 20:44 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72589">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">سؤال: اگر ایران پشت آن حمله به هواپیما باشد، آیا دست به تلافی خواهید زد؟ آیا آمریکا تلافی خواهد کرد؟
ترامپ: ضربه بسیار سختی به آن‌ها وارد خواهد شد؛ نگران نباشید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72589" target="_blank">📅 20:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72588">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8061e95725.mp4?token=KktFr7i1PtyL2xN8JT7U91mGJLjoXaM8n35dezms9eW7EF3MaL9lmiDGeyG2k0UGptuesTsIUQPY6GUiFIA64aE5pyreFYFFdQoxHoCvXkVfkxelvXMxGNcROKiXncx1RZUyrluqnh2_qhhztyv7MS-vLl8uCYe_7rkU_TI7PgDJ3KxhXtGhMM_XnZPd-yeVqqY4TCIBpcZpAsQ0249RUuWARMAgie1Fv4H9LFJdt8XEqCUzyQTd_ijo6fsDxvQ4RrxGb_P3B6aw8j03CfLe_6A-G8AH0odeZ55rFSArQP_kFMwie1vQlJ5X9iVjlmDNiV-TWn3iMFnpOCCJ9Qg-GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8061e95725.mp4?token=KktFr7i1PtyL2xN8JT7U91mGJLjoXaM8n35dezms9eW7EF3MaL9lmiDGeyG2k0UGptuesTsIUQPY6GUiFIA64aE5pyreFYFFdQoxHoCvXkVfkxelvXMxGNcROKiXncx1RZUyrluqnh2_qhhztyv7MS-vLl8uCYe_7rkU_TI7PgDJ3KxhXtGhMM_XnZPd-yeVqqY4TCIBpcZpAsQ0249RUuWARMAgie1Fv4H9LFJdt8XEqCUzyQTd_ijo6fsDxvQ4RrxGb_P3B6aw8j03CfLe_6A-G8AH0odeZ55rFSArQP_kFMwie1vQlJ5X9iVjlmDNiV-TWn3iMFnpOCCJ9Qg-GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوووری
؛رئیس‌جمهور ترامپ درباره ایران:
اکنون باید تصمیمی بگیرم: یا ایران توافق را امضا می‌کند، یا دیگر وجود نخواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/72588" target="_blank">📅 20:28 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72587">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ترامپ درباره ایران: «آن‌ها نمی‌توانند سلاح هسته‌ای داشته باشند — و نخواهند داشت.»
انها توافق کرده اند که سلاح هسته‌ای نداشته باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72587" target="_blank">📅 20:24 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72586">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">خبرنگار: لارا ترامپ گفته است که جنگ با ایران ممکن است انتخابات میان‌دوره‌ای را برای شما به خطر بیندازد. آیا موافقید؟
ترامپ: ممکن است. [اما] باید کمک‌کننده باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72586" target="_blank">📅 20:23 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72585">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72ce76f49c.mp4?token=FItjtuQ8YJvQi3i2u89vcCrfxPO3Kvsg449I6Vu0yBezpnBFWRBSXYyXsv0owtKP0JAYQu0RaK1Lj7Qcr5SqDb7uTRLyyedeC3A-JuKGg1oBjSVXIG12CFGQggsyZhlNN6kf1sMkH8t9uBgLBvbB7U0NhPx1bcika6-p3JC1peQpNjqEAntPHz5B3um3_Qo6krG9lTwhnCHr-omOVhFpwxTj5JD7-noUouDvyWArOrTKZWe40yDdgrt5VU6rS7D7ZkgMZap-lrF7arrxPDu3_QnB6vDQ2Bj0uxH_RaYK22RLyeSkTigr_XFGglyf1IBPHkW_bUGZ10ZrYuCtKGPkmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72ce76f49c.mp4?token=FItjtuQ8YJvQi3i2u89vcCrfxPO3Kvsg449I6Vu0yBezpnBFWRBSXYyXsv0owtKP0JAYQu0RaK1Lj7Qcr5SqDb7uTRLyyedeC3A-JuKGg1oBjSVXIG12CFGQggsyZhlNN6kf1sMkH8t9uBgLBvbB7U0NhPx1bcika6-p3JC1peQpNjqEAntPHz5B3um3_Qo6krG9lTwhnCHr-omOVhFpwxTj5JD7-noUouDvyWArOrTKZWe40yDdgrt5VU6rS7D7ZkgMZap-lrF7arrxPDu3_QnB6vDQ2Bj0uxH_RaYK22RLyeSkTigr_XFGglyf1IBPHkW_bUGZ10ZrYuCtKGPkmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛ایالات متحده در حال اعزام گروه ضربت ناو هواپیمابار «یو‌اس‌اس تئودور روزولت» به خاورمیانه است.
تا پایان ماه نوامبر، سه ناو هواپیمابر و دو کشتی تهاجمی دوزیست در اطراف ایران مستقر خواهند شد.
@News_Hut
| NBC</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/72585" target="_blank">📅 20:09 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72584">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a42198336a.mp4?token=u16m8HernbHYTNLeJFxuyvVAsruDGzg9jkl7TpqWgrJz8-KHU8G9r4bw0znF09qfq6ILsL_JN5SFMLh6fmaUaVs5jMh3OVZrt2DCVkBA-8X5ZGuGEL7irAcL1btv1WDFU0KNuYmNEfNZ90T3a4ROUqLJ6aftETtqVsJIvLOWWLoGrXzTQLSo1Y_R5oAYLusxGmFUQt4jGCp9nVL2lItc6IxTfa7fHlJ1WW4WFrDjdaVzqAgZlJMI07aLVwke4tE7QsTpx0fl15mq-eWaB8rPQFcDhy_dDGdLMhWqSQY3j1ekOKtkJzMOUx3utRmoF_IoVvFLW0kxQJ0YEtSH8LwrOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a42198336a.mp4?token=u16m8HernbHYTNLeJFxuyvVAsruDGzg9jkl7TpqWgrJz8-KHU8G9r4bw0znF09qfq6ILsL_JN5SFMLh6fmaUaVs5jMh3OVZrt2DCVkBA-8X5ZGuGEL7irAcL1btv1WDFU0KNuYmNEfNZ90T3a4ROUqLJ6aftETtqVsJIvLOWWLoGrXzTQLSo1Y_R5oAYLusxGmFUQt4jGCp9nVL2lItc6IxTfa7fHlJ1WW4WFrDjdaVzqAgZlJMI07aLVwke4tE7QsTpx0fl15mq-eWaB8rPQFcDhy_dDGdLMhWqSQY3j1ekOKtkJzMOUx3utRmoF_IoVvFLW0kxQJ0YEtSH8LwrOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درگیری ثبت نامی های خودروی لاماری با شرکت وارد کننده، که ادعا می‌کند به دلیل محاصره دریایی چیزی وارد نکرده.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72584" target="_blank">📅 19:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72583">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5610e80a6.mp4?token=M2HR1ChM4FaLozFuRzzxeVtl8JRHqT14Ose2m-sqKWGKo6dWM74oq3Ily25hQ2qKDVGHOXpV_M5q71a6JW7uu5K7KfKa3ge1vXphaYNCpwWtj7kR-Z_FjORY3h1FoslRcunEZD2JMw6ua2ZnZWp61Wmu-L7jRp2sGIJAS7H9O_DAj5i1OuVyaAOwRkgB-GNGau50UrqDqLvybEF2B_c79KAAzxsMZSUsfVuIJq3kDRTNNi9vjahyE6xYBj5eKxzLE897K7yDVt3lyfAJ0tZqjEAzcRyUaj6Nq6WhaKRjoGsAOQybqgGgGL9fYicv_tzG0Wj8iSr7GD7iknEGzGEC0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5610e80a6.mp4?token=M2HR1ChM4FaLozFuRzzxeVtl8JRHqT14Ose2m-sqKWGKo6dWM74oq3Ily25hQ2qKDVGHOXpV_M5q71a6JW7uu5K7KfKa3ge1vXphaYNCpwWtj7kR-Z_FjORY3h1FoslRcunEZD2JMw6ua2ZnZWp61Wmu-L7jRp2sGIJAS7H9O_DAj5i1OuVyaAOwRkgB-GNGau50UrqDqLvybEF2B_c79KAAzxsMZSUsfVuIJq3kDRTNNi9vjahyE6xYBj5eKxzLE897K7yDVt3lyfAJ0tZqjEAzcRyUaj6Nq6WhaKRjoGsAOQybqgGgGL9fYicv_tzG0Wj8iSr7GD7iknEGzGEC0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهنشاه آریامهر:
«کلمه‌ی شاه در این‌کشور (ایران) معنای ویژه‌ای دارد و همه آن را می‌پذیرند. ممکن است اهالی روستایی دور‌افتاده در کشور درباره‌ی اتفاقات جهان چیزی ندانند، اما آنها معنی شاه را می‌دانند!»
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72583" target="_blank">📅 19:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72582">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72582" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72582" target="_blank">📅 18:59 · 09 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
