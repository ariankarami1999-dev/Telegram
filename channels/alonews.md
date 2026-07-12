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
<img src="https://cdn4.telesco.pe/file/gXs83xBQpDXPTAqlZDYhWUt60pjHZsJ3-lP-AfDUV1sLWUUTvi5S4xI3MSzmiWmhQx-QDjROtaqChyKSYV55Q37UjIPUfneFozFeX2dYBT26v8cu03LTgnz-8GVCsOmh4x1sKrbAkaiodE9QFDiJGvYYzu8_-z-Dtsngohpf4rAWyM432soQhKaie7WoWGmHxJnJ7cM8kJV2WTyX7DcT7PsPGbZWWjPEqWacLjQwJsH9AF5A_ETaqDDKDAUFZ4eU_6rDNAVhga1E3vmRyQ3Uw2dLqBsgXAgTAdbKn8MZmqG00PuSxKozVhlZT0tlkasbU-hu2pNwimt6meE948vQ8A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 919K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-22 00:41:58</div>
<hr>

<div class="tg-post" id="msg-133571">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
فوری/انفجار در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/alonews/133571" target="_blank">📅 00:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133570">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
فوری/انفجار در سیریک و قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/alonews/133570" target="_blank">📅 00:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133569">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CyATDsouAxGKEMBOFfE288sebzxK--WPROrewIJp9pyssrJ5T9VgsMg38qaHUv7qs6cvc5KyggK0yinTuzYFyOS28NEWTUtL-lNSNvpKxYOKZN0_HGJXWYiqRPNTtnF1YgWd35oHOJECEYccFryzWd86LR-d2NH4W93TWIVSv1ParbmiyyNUXU9oeHbRay6LeYuuYpH4jkvnz9bDo5oh89mXZu5DZ3NtvBQPwbZ1WreRgbdEuyF_LcAp2GWe6SiWC5q0PODU6ZbtXvHFYNSwgD-W8E5N72Sr94d_Prpk0_d19n0avGn-D41b8Z4otWYrnqoXQxOw0b4IFzYTuCdLVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سه تا سوخت رسان داره از سمت اسراییل میاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/133569" target="_blank">📅 00:24 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133568">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfs8CQ65fYKmJJkyX_2_saCpm49e00WzeMCoSXuiNDvJliqkU8SzV40XOi5i3QHDELeTavJxZFGADp_7qa1JzXJBZlI6zerjgOH95l78EaTxyfsdYLIAW7toxcmivIv7BEqsYkbR6Qy8a3yrU89PfQsLRhSjW4CC18ix-ywMS8Bk23JpidKmaie2M8SvlD45IqQvxp8nzJrtSqPPb7Um0Hf5cyDN-uy0KKZMqsDosSSoWSw3VZ_4I_SDsHbi_hKCmLc1-NJ9DpbGv4NCzCBI-d9vPTLYj_yMqU5Sbngaww8w7wpVK2mImct-6NTwjZGpr0ku6AGHiqAgVpx3EDcHVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنت‌کام
: رسانه‌های تبلیغاتی ایران امروز مدعی شدند که در حملات ایران به کویت، سه نظامی آمریکایی کشته شده‌اند.
نادرست.
🔴
واقعیت
: هیچ گزارشی از کشته یا زخمی شدن نیروهای آمریکایی در منطقه وجود ندارد و تمام نیروهای آمریکایی در سلامت هستند و حضور همه آن‌ها تأیید شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/alonews/133568" target="_blank">📅 00:10 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133566">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iTTdrjNko_ud9bT0ux9wfORz975MH_qaEVgyTyGzhXS3wJ0i0AASplzEmLH9Hy-O9KlTDzKwRUaH9ghv35BkPLiHtVXh00yS_LvutXW4471Y1xy3X5k_3QlrqIZD88cyaUZROWP16Fg8SsCu2-77-l0vO-Wqo4FMgW48YLhWiM5P4b5_32xaMyCQmiWVh1kRfGDnpOQKgmbwmlB3O5tkyiPLLAjQKPCYUEL7LJUHdGPaR8C5jQKm2S1ZVi-TRgJQJBrbtfkUTtdnXn7YQ8NlENQl4n2Eo-0IQaUCN0vh7eHUmZqyH0inPqcQ5zq8a8I1Jkdy-rHu54bmYzYrTvBydA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tOkHpiiVfFlT2ksO1jaEMDvfthhYUzrMoNPfz9qpsR-UjTp5lPfIcAob6V5QNMC6iBBNWq49cD8qzA763f_ZfN-68DQpVd2janDH6FNFS3bG1x3t-w2iyRt4_sRPhJ8b6ZBebNYFVpZqP5XJBpwwAeyfvvN1a-h92Hm5NpQx3nZzH3wuGowCL5Q3deHRk7GspfYHBhQ8vNiQWEt1Fi_M02VvtZfkZ7I53VaOENchc1YhSplQJtDVF6OLDbd7f7GechbaYoYLlsX_cVHpOTQJOkRJrdleC_OtdfIfax_nZLLpX6rZndKhomO7Za4ZVOpcdbn5JGnAeIFVvxv4kuEd9w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
عکسای دیگه ای که ترامپ پست کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/alonews/133566" target="_blank">📅 00:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133564">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fabe17e0f.mp4?token=qmP-jFczG2VTvvTKvB1l09bdGyw4eKLRrNyWRtFb_j2YSzoaBgbDuneHFKyQZSm_-m0bKxdLwD0yo1eGjOk4JHg834i7TTuvnwqCoYhivX3YUmMmPNFhgIkcTXyOcBZTD4aE12gN4XVZ6R5E5rJ6YnYW8WQFzrQ2lH4nRG0Sn8gAMsZa5bebjdIYrZrY9moafwF8H6pV59wRDzsAvjGJjaoEc6bbY8FCiLEq5N0dzTVmsaXJdX-QVTYREzn3aCcJaYncyqoMkFtAF3JZxB5JNi4JuPWbt6pmluvJaOflaQIKHaRBLPQ_7_TjGS2J2V1MzkzH-6CfAS1BCzbPz0tHhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fabe17e0f.mp4?token=qmP-jFczG2VTvvTKvB1l09bdGyw4eKLRrNyWRtFb_j2YSzoaBgbDuneHFKyQZSm_-m0bKxdLwD0yo1eGjOk4JHg834i7TTuvnwqCoYhivX3YUmMmPNFhgIkcTXyOcBZTD4aE12gN4XVZ6R5E5rJ6YnYW8WQFzrQ2lH4nRG0Sn8gAMsZa5bebjdIYrZrY9moafwF8H6pV59wRDzsAvjGJjaoEc6bbY8FCiLEq5N0dzTVmsaXJdX-QVTYREzn3aCcJaYncyqoMkFtAF3JZxB5JNi4JuPWbt6pmluvJaOflaQIKHaRBLPQ_7_TjGS2J2V1MzkzH-6CfAS1BCzbPz0tHhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یه نفر در حال فیلم گرفتن از خرابی‌های غزه بود که همون لحظه چند تا موشک دیگه تو چند متریش فرود اومد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/133564" target="_blank">📅 23:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133562">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNsXqyVedGLSmdpJd9JjGIBzXkyHvlHKX7meevmHcVActDBZ_D71szzK03Z7CBE4ib-2y6JmLA0MQjdKVzV48GsH3DAVUzFcQ67Tdf0mINQx_l17Nb7R-wWS8I0RkedPMrBYdPygxmCBINAbYb1mgkVUsuYjwDn7ghLSoRJK1tZEKmbKORZeEyykeu1GWV9nJ9_vMA8f_q7zQuyODTCJS9tHUzVtXGwuxQlg6Bdu4h0DJ1cgH3GtJE8I4rFg54uqkEu5Ylv9uYQ0JNbf68hyTYdR6DpDGY4D1Ym2Azd9bUlIfhmzNLF3aMRaKffHvQS4iQvEiAK9MBNKb-38Ho97xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
از ساعاتی قبل تصاویری بسیار منشوری از آرام جوینده همسر سپهر حیدری، اسطوره پرسپولیس درحال پخش شدن است
◀️
مشاهده فوری و بدون سانسور</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/alonews/133562" target="_blank">📅 23:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133561">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">قاتل همیشه اونیه که گردن نمیگیره، نه اونی که جار میزنه کار منه
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/alonews/133561" target="_blank">📅 23:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133560">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7dba5acc7a.mp4?token=ICXZ_P6eGudDmGXYyjFp2A6JKiSRsKqgrXO4h-LV0CqBECKpn09SRfRgcOnOxT8sU7_1jXWUp2kpF2-WkC6glCrA2Zp4hOp9Z3RgY4-EPsR6a4Pzp7yEJfKOKpoLD7TkuwWqXt9Beq3uMGsPpvE7FPH_7GehhCqFxQSYAcJheMtmLSrpc5TMzIDDaF4lHt8j97EqPHQiaBXbZoDgpLApOaCdQq5A54hdvhF2S0SBToaIbIc2ywnOsL8zML_oWAKDsvjd1StNrJtSfy5JKNCfhAZxRZYbhDGFE7-brlV5pjLBpRBgBz8Y5U4D0WgbdtPO9XWOkko0XhzIxn0yyk3Z6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7dba5acc7a.mp4?token=ICXZ_P6eGudDmGXYyjFp2A6JKiSRsKqgrXO4h-LV0CqBECKpn09SRfRgcOnOxT8sU7_1jXWUp2kpF2-WkC6glCrA2Zp4hOp9Z3RgY4-EPsR6a4Pzp7yEJfKOKpoLD7TkuwWqXt9Beq3uMGsPpvE7FPH_7GehhCqFxQSYAcJheMtmLSrpc5TMzIDDaF4lHt8j97EqPHQiaBXbZoDgpLApOaCdQq5A54hdvhF2S0SBToaIbIc2ywnOsL8zML_oWAKDsvjd1StNrJtSfy5JKNCfhAZxRZYbhDGFE7-brlV5pjLBpRBgBz8Y5U4D0WgbdtPO9XWOkko0XhzIxn0yyk3Z6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رسانه های قطر از تشییع پیکر امیر سابق این کشور در دوحه و دفن آن در مقبره شهر لوسیل خبر دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/alonews/133560" target="_blank">📅 23:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133559">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vrIiv2O2LtZo4Ut9Mi7TlTxzdUvkNZ6OmCPEHGQUUR6uwzTb-Y6-B_XhL4YeF0JufYgZIvjbdDQSfIo6lkzHpma__67y27Po362lFQ5SYJ-QPGzkH9CYOmeRgW7gYhTagCoyjbastPl_ucuJYYreOOdZ6cM9kagnFsrrDlLzktMhe28RL-S2R0og0Je25DbYkXJhDDf_l5Qp2UrWZxU4NQwYzHMW-o6Up8-fEDjbnCrDGp2MEnK9bTWYa0rz1ss65S0K49f2P-LqRWJfQkvSUlfj3CAqYGYbz6djRm2pejqHHXMCW4lHN2k21amSUe7G4ejQzN_oaQRWm0G-gCTUXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مجری : آیا ممکنه لیندسی گراهام رو روس ها کشته باشند؟!
🔴
حسین پاک: نه،باتوجه به بیانیه رهبری درخصوص انتقام،گزینه روسیه منتفیه،این راهیه که حاج قاسم وعمادمغنیه بنیان گذاشتند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/133559" target="_blank">📅 23:35 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133558">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LHO5G641bDvoQ7KVkPI-jrTzYAG-oreDQ2g8KRmVj-iEKCIHt8F2JLx6kfwDknkJXQ74QWbGBY-MqqmEJxNq1MMgVDlYnkK0Rd25pttho6VwXAWz4vrj4xTb6LhVt8NdlPAzG2w0eJletxIImQmkhkCEqaEKGzG8YUjceJucZ6ICElu9a1wo0CPfDgStd26xIdOBXy0AvaZ6RKF-Ju9uR-AgxcB-ejkyZoAx1GT1Nu0GtNqloLBnu39GiBJccvCnTkMqAyYTEb3KLq6wAk-wt13_6j1JXCdwP0RhvpWonBy9FAjc9i5f_R2V6bPgWtRkgKE7TCWpy0W4lehFThJp3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توییت ترامپ
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/133558" target="_blank">📅 23:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133557">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XBIolWdVM5e6cs_3dNbSW1cJcO8D91JBKfeCjCRWGIfZCc9pyV9bRy6KY_vb5TLFZmbnEHiWT-b2zLmFzT7KZ0OiEY1DgYv07F3RfbxRRywF23KFcUPCIydw9Z4XjIuvW8PEMVWC3jbI7yKl18UK0rdMCNPFljUZtVwB5o2kQRESuPZaFAtw-SlwxRHKbq3XEGF6mO6tkCcvwT_S7hOyd1Y3EHPgAAXn4LmAMW24Tg4c7Raw7A6qJNm2iX3QgMCKEIMjryFiRPugFoqUX-VuKC0jqIwenTDPqBB7UyHHlvX_Dds5d2LcxHbt7xpFDMsSUrEyL9wJ8EJxfl9g0E0wgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توییت ترامپ
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/133557" target="_blank">📅 23:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133556">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
وزیر جنگ اسرائیل: «الگوی رفح را در جنوب لبنان اجرایی کردیم/منازل و زیرساخت‌های ۲۴ روستای مرزی لبنان را ویران ساختیم»
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/alonews/133556" target="_blank">📅 23:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133555">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/723cbb9eb0.mp4?token=O0FCy7k-5mtfqR7pfzP0RanEgp2O1gDuatsr7t6vk0xS4hCtyTK3kjywATLAexGL4hUhRHnRh7i2RmW0ECpudDBQqOL9ZsDrZiPaCoAvAouvyppeUFN7J4cpU5gdJaFnSEiczGyS0FyCxRzXZNZKz4dAI5yCwQj4-NCxQQxdrMtufZYqwSmVWHzwjw4ggpdB8Ryom1vQ99_GYdsvLuPZ6pn-ZIZwnZK-uRuUFR9ZIX6TcSvnin_Darh1Z8Rdh9PZdBmnt9a7GW1ZWAgPB3pn_KyedUbKu78GtTCMs8rXVrs2eX02BAuznYtOHk-LwqA2dDQYt7ByiXcxXICgJuxcugkcNE8TNE__tguh0FnZz_3wHgMAS6ZagfBhN33DV1lB8w_imWD2Izw54QOpVi61QgePu168NWjRvrSUzGYyCkfjsvLv39BiwWnrtFC0BsdY_GsQWXVe_S8sHb1KhCUO-LA3mX5wsGG68L5fxrjkasb2uV8Xt9IhN0zgRdE-jik7ITtI1hTJKlokesoDZTqXfGC9mEEtnXCLEuXckiMn9A-oebiGsNgPGVv5IrdvwkqNvxlOBfu7MfT-Bp6PYsjg2qUfmouyRWYkPtjjUGMJpuqrQkdMH6oqjaId3TQ3tSbLZTolThqjP0wtRi2G3m4s1lraxOyMGIQ2LixQRgTn5q4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/723cbb9eb0.mp4?token=O0FCy7k-5mtfqR7pfzP0RanEgp2O1gDuatsr7t6vk0xS4hCtyTK3kjywATLAexGL4hUhRHnRh7i2RmW0ECpudDBQqOL9ZsDrZiPaCoAvAouvyppeUFN7J4cpU5gdJaFnSEiczGyS0FyCxRzXZNZKz4dAI5yCwQj4-NCxQQxdrMtufZYqwSmVWHzwjw4ggpdB8Ryom1vQ99_GYdsvLuPZ6pn-ZIZwnZK-uRuUFR9ZIX6TcSvnin_Darh1Z8Rdh9PZdBmnt9a7GW1ZWAgPB3pn_KyedUbKu78GtTCMs8rXVrs2eX02BAuznYtOHk-LwqA2dDQYt7ByiXcxXICgJuxcugkcNE8TNE__tguh0FnZz_3wHgMAS6ZagfBhN33DV1lB8w_imWD2Izw54QOpVi61QgePu168NWjRvrSUzGYyCkfjsvLv39BiwWnrtFC0BsdY_GsQWXVe_S8sHb1KhCUO-LA3mX5wsGG68L5fxrjkasb2uV8Xt9IhN0zgRdE-jik7ITtI1hTJKlokesoDZTqXfGC9mEEtnXCLEuXckiMn9A-oebiGsNgPGVv5IrdvwkqNvxlOBfu7MfT-Bp6PYsjg2qUfmouyRWYkPtjjUGMJpuqrQkdMH6oqjaId3TQ3tSbLZTolThqjP0wtRi2G3m4s1lraxOyMGIQ2LixQRgTn5q4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سعید جلیلی در واکنش به پرسش مردم که «دولت گفته همه رأی مثبت دادند»، پاسخ داد: «اشتباه کردند؛ من بارها رأی منفی خود را اعلام کردم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/alonews/133555" target="_blank">📅 23:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133554">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9054413b86.mp4?token=bqS9YW9cNv8pGTTqqbfTys6i1a62XjhTnTMgB_DGxMgq7pxoNY7Vg_bCn9nQ2I77Dz_rtue8F4pZ9h8MZUp8GrGr4JKtxygApTSAGLFuTA6nzwF9FMcu8PTktpkZTTLWwGOw1yK3GtwZbzMuqVJhzSPL4uPvYmhP-M63juQL2kcjdhSex2-793lr5YWWq4ffYjHpUKAC-UnlCEG69DXM7mteBIiq-T9P-74TiF9EQpbNxbqaFo4E3rVFSexwimW5B-a82ppygLMigXO8rdXPhuAzpvxVMIHTj0poDJGJfAjQeRjVPP_wcr7mpJYirOBJOmPSH--mjlRGOu1jlfdZvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9054413b86.mp4?token=bqS9YW9cNv8pGTTqqbfTys6i1a62XjhTnTMgB_DGxMgq7pxoNY7Vg_bCn9nQ2I77Dz_rtue8F4pZ9h8MZUp8GrGr4JKtxygApTSAGLFuTA6nzwF9FMcu8PTktpkZTTLWwGOw1yK3GtwZbzMuqVJhzSPL4uPvYmhP-M63juQL2kcjdhSex2-793lr5YWWq4ffYjHpUKAC-UnlCEG69DXM7mteBIiq-T9P-74TiF9EQpbNxbqaFo4E3rVFSexwimW5B-a82ppygLMigXO8rdXPhuAzpvxVMIHTj0poDJGJfAjQeRjVPP_wcr7mpJYirOBJOmPSH--mjlRGOu1jlfdZvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فرمانده جدید نیروی دریایی سپاه:
هیچ کشتی خارجی بدون شناسایی ایران از تنگه هرمز نمی‌گذرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/alonews/133554" target="_blank">📅 23:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133553">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
نیروهای نظامی ایران با هشداری از شهروندان کشورهای امارات، بحرین و کویت خواستند از مراکز نظامی دوری کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/alonews/133553" target="_blank">📅 23:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133552">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/065c481a53.mp4?token=SD1MfNKTJi1wXsYjGzvzqIKMb-V7IFXP6C8T5CFb9ReklPcxP0si0_Xo2RC7nEVOVb8bqkyQTikpKQh20PPCowvss6HR85EiAvMDr2ho5WVmXSVqyWi58BzVD4yaD_S0c_OwlU_mdtXorqReH9mH_HFyzSWgU_gE7UWKRHYNLlEjhY7w3a0GLM-k2XtBjXxaUSoyDpgLi4cHusdVWmqiOkBNUcBO8HLtfVS1GOicQ2eTKqiIEPvYQ-bD9U-kY4ZNLaLQIypKByPAOJPUcwseFPhbii2thFJ4zFDUXr7zqQmjEZuzt05dEM3452xTUej3iun09XRu22bK0-oQkVwPAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/065c481a53.mp4?token=SD1MfNKTJi1wXsYjGzvzqIKMb-V7IFXP6C8T5CFb9ReklPcxP0si0_Xo2RC7nEVOVb8bqkyQTikpKQh20PPCowvss6HR85EiAvMDr2ho5WVmXSVqyWi58BzVD4yaD_S0c_OwlU_mdtXorqReH9mH_HFyzSWgU_gE7UWKRHYNLlEjhY7w3a0GLM-k2XtBjXxaUSoyDpgLi4cHusdVWmqiOkBNUcBO8HLtfVS1GOicQ2eTKqiIEPvYQ-bD9U-kY4ZNLaLQIypKByPAOJPUcwseFPhbii2thFJ4zFDUXr7zqQmjEZuzt05dEM3452xTUej3iun09XRu22bK0-oQkVwPAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو، درباره فوت لیندسی گراهام:
در اسرائیل، ما ناراحت هستیم در ایران، جشن گرفته می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.4K · <a href="https://t.me/alonews/133552" target="_blank">📅 22:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133551">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r6y67aks9c3ewZLjODzdGH4B-8aLQKt2FlRD1Ojitv1LAQc-oEakib3p1WuOM6nqSDdlyP8d6hATWQW3oooiAktQAXLZBZqUE57jRBtvBpAF5fZsZhT1oregjj2WA7jxqB1RYiYKyvuxdMztLSJzhuU-2Y4JX23RHYwGnISwXqAb2Zeu8lXYHMGzc5asMPDhOVwPqce2ZS44Gg_Cl0Eq1SEWuI2kaY5NAgSzhptEEIdjQBB9M3BqTh5VRFPVjsA2IUsN54Gn41NrBDYdl0s6CXcl0Q5UUJOh5dkKnnVr-o4qu90-Li2_B31d2BLwSIENSFuB6yBOYLgHibLcCt5zbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی کمیسیون آموزش: استرس، ترک آزمون، برگه‌های سفید، ناامنی در مناطق جنوبی و احتمال تقلب و لو رفتن سوالات؛ ماحصل روز اول امتحانات نهایی بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/alonews/133551" target="_blank">📅 22:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133550">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Fce8q8uPf_MdWOMWdAsvMhhCCUDCrdjJJNhc5pfVBncXt2-b3u4ycQ1lk3JV0LhG5HP_S5di0t2rzCJ67ufH0EC8VQUxzhaoikHdHDIMZILRQJdW2l-gE7ErWK9SctpNDqiW9-bhATgnmjInAfaPweH9XbfhYS_f5V9jSAB0FtHW5tpkIK3_Gs7OXzYwdk0iAwAsYTau66MsNxHzJqgev32QbAeQSIQEY86fqkfOS2vhwqcbNCcXKSjbvYAOK-epVoXUASSWrU_IhrSxIDfjSrQhWccxNAZILy8Kcn9as72fBOH0SCQIcdDku_TK8rrRuDdItUfMVzVG2Mffi-iPnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دومین هواپیمای معراج مخصوص گروه مذاکره کننده ایرانی از مشهد به سمت بغداد درحال پرواز است
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/alonews/133550" target="_blank">📅 22:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133549">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخرید و پشتیبانی</strong></div>
<div class="tg-text">💫
یکی از با کیفیت ترین و پایدار ترین اشتراک های بازار با قیمت خیلی مناسب حتما یک بار تست کنید.
📣
با توجه به سابقه عملکرد سرویس‌های SafeVPN در زمان
📣
اختلالات و‌قطعی کامل اینترنت بین الملل سرویس های
📣
خریداری شما فعال خاهد بود.
خرید فوری از ربات زیر :
🤖
@SafeVPNXBot
✅</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/alonews/133549" target="_blank">📅 22:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133548">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخرید و پشتیبانی</strong></div>
<div class="tg-text">🚀
تعرفه سرویس تک‌لوکیشن های مختلف Safe VPN
✔️
اتصال پایدار و پرسرعت
✔️
دارای ساب برای اطلاع لحظه ای از باقیمانده
✔️
متصل در تمامی دستگاه ها و اینترنت ها
✔️
مناسب استریم، بازی و استفاده روزمره
✔️
پشتیبانی تا پایان سرویس
💬
تعرفه‌ها
🔸
پلن‌های یک‌ماهه
▫️
۲۰ گیگابایت — 30,000 تومان
▫️
۴۰ گیگابایت — 60,000 تومان
▫️
۶۰ گیگابایت — 90,000 تومان
▫️
۸۰ گیگابایت — 120,000 تومان
▫️
۱۰۰ گیگابایت — 150,000 تومان
▫️
۱۵۰ گیگابایت — 210,000 تومان
▫️
۲۰۰ گیگابایت — 300,000 تومان
▫️
نامحدود (مصرف منصفانه ۳۰۰ گیگ) — 450,000 تومان
🔹
پلن‌های دوماهه
♦️
۳۰ گیگابایت — 50,000 تومان
♦️
۵۰ گیگابایت — 80,000 تومان
♦️
۷۰ گیگابایت — 105,000 تومان
♦️
۱۰۰ گیگابایت — 155,000 تومان
♦️
۱۵۰ گیگابایت — 230,000 تومان
♦️
۲۰۰ گیگابایت — 305,000 تومان
♦️
نامحدود (مصرف منصفانه ۴۰۰ گیگ) — 585,000 تومان
🔸
پلن‌های سه‌ماهه
▫️
۸۰ گیگابایت — 160,000 تومان
▫️
۱۰۰ گیگابایت — 200,000 تومان
▫️
۱۵۰ گیگابایت — 300,000 تومان
▫️
۲۰۰ گیگابایت — 400,000 تومان
▫️
۳۰۰ گیگابایت — 600,000 تومان
▫️
نامحدود (مصرف منصفانه ۵۰۰ گیگ) — 680,000 تومان
⭐️
تعرفه سرویس‌های مولتی لوکیشن SafeVPN
▫️
10 گیگ ➜ 50,000 تومان
▫️
20 گیگ ➜ 100,000 تومان
▫️
30 گیگ➜ 150,000 تومان
▫️
50 گیگ ➜ 250,000 تومان
━━━━━━━━━━━━━━
🤖
ربات خرید
@SafeVPNXBot
✅
📞
پشتیبانی
@safevpn_secureSupport
✅
😍
رضایت مشتریان
@safevpn_feedback
✅</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/alonews/133548" target="_blank">📅 22:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133547">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
رویترز از حمله پهپادی به اردوگاه کردهای مخالف ایران در سلیمانیه عراق خبر داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/alonews/133547" target="_blank">📅 22:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133546">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
خبرگزاری فارس: قطر و عربستان بازوهای حملات هوایی آمریکا به ایران هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/alonews/133546" target="_blank">📅 22:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133545">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
فوری/پرواز چندین سوخت رسان آمریکایی بر فراز خلیج فارس
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/alonews/133545" target="_blank">📅 22:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133544">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
نتانیاهو: سناتور گراهام به من توصیه کرده بود به تأسیسات هسته‌ای ایران حمله کنیم
🔴
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در واکنش به مرگ سناتور لیندسی گراهام که امروز درگذشت، اظهار داشت:
🔴
«او به من گفته بود: باید به تأسیسات هسته‌ای ایران حمله کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/alonews/133544" target="_blank">📅 22:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133541">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
یک هواپیمای دولتی عمان درحال فرود در فرودگاه بغداد است
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/alonews/133541" target="_blank">📅 22:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133539">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bJM1LjbECUjdo6pGlWj66l7qV13b-6deVeRdiwXcUx6z_HV_mePBTQlyjPe3dedwqja9WuDsqGmU2Ix1-eSjr91gBmg9emjpB5myw6pYNFGGN-2Vt1WsDCCJVELDEgaSaBdkgF_52FVHmhf88lGiGHhi2V5F6_xYTGG6AYFwIekqkBElaOJd6njhO9xfqFX9YhJ2xNmJoW3JslosDVYYJEKHbxUqW8-orRK_8YKoK6hwzF9uuGxF59Yf8AZt_KZgpgLs7YT6Ldh0u6NUfmrCTJ9ytI5SQCovCBNli8otl4Xr3XN5h5bsirZJMVa8XkW1i_b_aUzLu6ySoDky-wGi1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیمای میناب ۱۶۸ متعلق به تیم مذاکره کننده ایرانی (عراقچی و قالیباف) بدون مشخص کردن مبدا و مقصد و همچنین روشن کردن رادارش در نزدیکی مرز ، رو آسمون عراق درحال ورود به بغداد است
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/alonews/133539" target="_blank">📅 21:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133538">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
معاون سیاسی امنیتی و اجتماعی استاندار بوشهر خبر منتشر شده در فضای مجازی، مبنی بر حمله به محدوده تیروگاه اتمی بوشهر را تکذیب کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/alonews/133538" target="_blank">📅 21:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133537">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
واکنش دبیرکل سازمان ملل به درگیری‌ها و حملات سپاه و سنتکام: بسه دیگه خیلی نگرانیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/alonews/133537" target="_blank">📅 21:47 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133536">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_eL9x0YHdWYktdcOUGFRNbqwc7ps9Q5haOjt7iimZqt6RM37IMFFVgoCjKl3O5yIKUO16EXhd3dXGh01eyIvFLOXQCtGrrLozvDqdmHDapB64-HD4kIiV5sBu1eBB0Cfi8aBAwVKMYRkxRcstTQfaBbJ2hYK-u4ZRSB2vVeNDtjZuzjCgyQwi_DoDRpaFuHkiVcDCbqE919y_4uE-BG9E2shspTbvisclaVwXxEDOQ4ES8J2lM9YuTu-U7Ye-4H8lk-g59Spaw7KfTmHyhKjCAfPo1urnSR4wVfpVGLnTxnzyJNE3pwOn2iLlCXK1K-kXC3n22Fr5kX5PNYjQ_S6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روزنامه فرهیختگان خطاب به رضا پهلوی
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/alonews/133536" target="_blank">📅 21:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133535">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HUVAf76RRJvXCbfC45-aOlSwL1Hw7aEUumGRxHqJ9nLp6RUzv4GIJ4-RwXi7QO6eICYn1kV55hgn_Mb9VV9_JL9uVjDi2FT_SvjjPIdoiyfy0-mfsNYLilcT4yBaR2Cc3xwix-2hDdpbs-gPHjG49qjVKCOyhtJVMz521w7U2NblmKAqplAiIAd744jUFae7oJmngLIdxDFzILzXZDcazXk-Jd7KyiFHzqByuYZwcY2bgns2dlvkIm5Km8fdj-yn3k2rY9Pwj157OsBAC0w7xs9oOoDT26ubhnXzM36TGu-HGR1S_Br9izMI__1mvl_9zqPa-HeJpmMZrwcbCE-TAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون /وضعیت آسمان پروازی ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/alonews/133535" target="_blank">📅 21:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133534">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
انفجار در سلیمانیه عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/alonews/133534" target="_blank">📅 21:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133533">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
فیصل بن فرحان، وزیر امور خارجه عربستان سعودی، در تماس‌های تلفنی متعدد با همتایان خود در کشورهای قطر، عمان، بحرین و اردن، تحولات اخیر منطقه را بررسی کرد.
🔴
وزرای خارجه این کشورها بر ضرورت تلاش‌های دیپلماتیک برای بازیابی امنیت و کاهش تنش‌های منطقه‌ای تأکید کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/alonews/133533" target="_blank">📅 21:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133532">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uC2BfCelgJwJPS-dndkIx9IhGokb3IZozqJ9xpAfe8pzkw6uBmkfA7CjqoTo6vklaSt_2TWB_SQa3vGQSjJlg-4tEKKO4XFmox8e1zjaqkqKiAsrrZUZGwI2caMQgr6jrud0wRGf2yg0_rqT3JPi5ncgjIGJeXAPkNkS6wNA-k8bumVUawNUUQ4cg8U9tPIIGA-u0dF7ZrnU0lr2Ast_XAYwkPP38AI-lB8nvJykfwH0Ba4FUpGSQHS3KtXTkpEv-F3C9Dk_Zvm1FJBtgBKr1insIv_R_-EFq_zCbGA_EA9c_-sv-jCg0j4w6ZTMAGsuWdeCHRG-jv3qgJM2qutJ4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون فعالیت گسترده نیروهای امریکایی در جنوب کشور
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/alonews/133532" target="_blank">📅 21:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133531">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
هم اکنون هواپیماهای هشدار اولیه و سوخت‌رسانی هوایی ارتش ایالات متحده از پایگاه‌های مستقر در اسرائیل، عربستان سعودی، امارات متحده عربی و قطر به پرواز درآمده اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/alonews/133531" target="_blank">📅 21:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133530">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
انفجار در سلیمانیه عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/alonews/133530" target="_blank">📅 21:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133529">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
گزارش هایی از صدای انفجار در لارک
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/alonews/133529" target="_blank">📅 21:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133528">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
کانال 12 اسرائیل: ایران قصد داشت ترامپ را در جریان سفرش به ترکیه از بین ببرد. اطلاعات خارجی این توطئه را کشف و به مقامات آمریکایی هشدار داد، که منجر به تعویض هواپیمای ترامپ با پرواز برگشت او به واشنگتن شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/alonews/133528" target="_blank">📅 21:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133527">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ByWRMoCC0D_hKWRjefkvCqW7m449ZCDY5DfuXHgYiyqSuFO0mxUasYOVzVM7dWlFdner62O-yH80qb5jWO8r3rYlN58QYn7-qwtURF31-sLUbpAvjvXJ8LiNZu1tjfNre-WeHkCgVfKrswbmEBhDoWhYuNoodArQIHMGH0NH8dzBuAp702_vD7KIuFvMi8AjnLoGPO6Nfxbee26Ko1Lx5xLBdjWFLmSFx0dejkj-qZzjK_Nl2aULga6yP8kWfTdHOYhccXsfolwGFwAs06fMd5_jaDVyi_-NR9WUIBEOjlZuSqL2bymfblBzBXejNoU5fcSP3uXpjFMUG7fvHqkOzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک ناو هواپیمابر نیروی دریایی ایالات متحده که توسط دو ناوشکن کلاس ارلی برک همراهی می‌شود، یک‌بار دیگر در ورودی جنوبی خلیج عمان، در ۳۰۰ کیلومتری جنوب سواحل ایران مشاهده شده است.
🔴
نیروی دریایی ایالات متحده دو ناو هواپیمابر در منطقه دارد و به نظر می‌رسد آن‌ها را نزدیک‌تر به ایران نسبت به (مرحله اول) جنگ مستقر کرده است.
🔴
مکان ناو: ۲۲.۵۱۴۶ شمالی ۶۰.۵۸۷۰ شرقی
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/alonews/133527" target="_blank">📅 21:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133526">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
اکسیوس: لیندسی گراهام ساعتی قبل از مرگ گفت «الان نمی‌توانم بمیرم، هنوز باید ماجرای ایران را حل کنم و تحریم‌های روسیه را پیش ببرم»
🔴
او چند ساعت قبل از مرگ، احساس ناخوشی کرده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/alonews/133526" target="_blank">📅 21:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133525">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l54YR81z9k5iFgOnBAi9xFwnYGSyj3TZ5HOkUGJxzBmwyvsBTW-Wg_eAAk67q8MaJCk7OOFxdJ013uCFMCBS1rOupk71fxWqKAbeaI5qfj9R7XjCFj4sybxKIFJiYB-V8ujJwxjPLNjtmuCD_6mAhbRVYjb_fM5O0wDUrrEKa6U-RKhv_YcIZm5UOiSRDrkDwtGjEC69boGQ0NJa4PAE-d03c8FC7MwWDWNQeQ-lwsMnIZYPxybpKv1ZJXFgYS7bAFKRNBODFVHmelVdp0qkqqVlMTklneR5urerrVoemy_8xwB7JweWp-c6-4B8zJXu6o-Kt4PVZbxoIjgGsNxthg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منو غذا در سال ۱۲۷۰ شمسی (۱۳۵ سال پیش)
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/133525" target="_blank">📅 21:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133523">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
فوری / وب‌سایت واللا: ارتش اسرائیل همراه با ارتش آمریکا سناریوی پیوستن به حملات علیه ایران را بررسی کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/alonews/133523" target="_blank">📅 20:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133522">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
انفجار مجدد در قشم و بندر عباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/alonews/133522" target="_blank">📅 20:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133521">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aOEUpHLmTzpJEI_8Womu1LVnvYO74AcSydkS1E6Dy7BJVcNkZ1Q0dr4kIRQ58omMdw6XjuOYLVe1VEmQXh8YeRhtvLsKdiQyCBpP3HCA_dXnpDx55gc9pLzjHk0K2SfLJa4f_On4UexXYEMmIbMX3nqgKIw807x8E79zW9paINszkNlHxyOK5HqWeUH0dqs5OdxWd5ESCrBH4uG2ZbXnI8IgjPbN5Oqns_IAmppVvJiBpOLLXs6NXUxCsg8kh8OQjtvlyad5-gfERgYdgwtceeQSnY58kCo1k9gwtInXXuA-tWjKFsnKaXoPAzMAt-hjGp5AReJBNpdotGbD48DgXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دوگین نزدیک به پوتین ادعا می‌کند که موساد سناتور گراهام را ترور کرده و این کار را برای ارسال هشدار به ترامپ انجام داده تا جنگ در ایران ادامه یابد.
🔴
"مرگ ناگهانی گراهام می‌تواند لکه ننگی باشد که به ترامپ فرستاده شده است.
🔴
من شک دارم که ایرانی‌ها این کار را کرده باشند.
🔴
واقع‌بینانه‌ترین حالت این است که کار موساد بوده تا ترامپ را به تجدید جنگ تمام‌عیار با ایران سوق دهد. این به وضوح به این معنی است که "شما نفر بعدی هستید". لیندسی گراهام سایه ترامپ بود"
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/alonews/133521" target="_blank">📅 20:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133520">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ee15376941.mp4?token=tp1WPlc1CF2jrJqIpf4spZhhHH8m4b0cgPBTTusZQnmE5Fh2HI5otkOb24saK30DUWy0w-2y0Cv6Ni9pQhzEQ0wf2yIahoMDI1POJ4xYj4okxoZI6TU7iL7yH4nqe-siNJh-CqgulfxTxYlGd7hJP0MVSFwE2CvFSZHKp14LWOvZVrxIsB1Dy4klJpZhDMmuJGAVE7Qpm91eKWkPmFs8L_eUTR6gTuTPpQ8TYrN1K9gMXMSJtK-xgvF2GvEYn42s26X9KPtbMKKLbGbQVqIihILUFIuVIrU5Qtq9KqETSs6kfgUDO0Ti40npBKxfz6-HTrtZy42ef4vMUZUULzzipg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ee15376941.mp4?token=tp1WPlc1CF2jrJqIpf4spZhhHH8m4b0cgPBTTusZQnmE5Fh2HI5otkOb24saK30DUWy0w-2y0Cv6Ni9pQhzEQ0wf2yIahoMDI1POJ4xYj4okxoZI6TU7iL7yH4nqe-siNJh-CqgulfxTxYlGd7hJP0MVSFwE2CvFSZHKp14LWOvZVrxIsB1Dy4klJpZhDMmuJGAVE7Qpm91eKWkPmFs8L_eUTR6gTuTPpQ8TYrN1K9gMXMSJtK-xgvF2GvEYn42s26X9KPtbMKKLbGbQVqIihILUFIuVIrU5Qtq9KqETSs6kfgUDO0Ti40npBKxfz6-HTrtZy42ef4vMUZUULzzipg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک حمله دیروز از سوی ایالات متحده، تقریباً به نیروگاه هسته‌ای بوشهر، واقع در سواحل جنوب ایران، آسیب وارد می‌کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/133520" target="_blank">📅 20:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133519">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e63fb7b34c.mp4?token=oODwerBE2F8C2RebeJufPYxFAf8IBTTzf-OOKBast1IRrs2fLrJnbYz5-VmL5JRqpG-HvBBn2M7xA-fZ0kRmTLHL8QRLaQ4iBpbrL5kCphT_hXcBBhLffO1UNlXm3qxNDzsSC4A3k843jmmEfbgl7Q9ojY48reL-5fF3vXYecKULC60KRErQwbF1Fk8draJXMlfDDSmNLyi_0oLWaxTr6PDTKCvruqeM2pnxA6kvSLxQ_IEnIFgDSBWjRTJsc2oAXJMVUos6heRKPTiNxz7_xeaLz8LDDg5JCCkvvrnmXhnORkfbLg4hxnrextd8HQ3gP3DQR85DtSg3YXpfrvHylUMv2Lryf1HkqfdpQjUdO7H8UCpN-n0qI4XHLyYwty3nGlnPHayECsxctYTS44qialUK3_Zp8Q3t6cCHXwQvBl9Bf-VrvErO-Ja0tTS4NRl9vX4n89NE4aXSziIKc-eimsq79SH88xoYdq1VizzGL4ffPKYm-naqy2RoS2f7j1gE2q1s8bUjf8TpUEEi4ILf17Ny6hGq2K2u2J9PSmQcdtO1m-mZIZpzfQ9B_Zofs357R18U6PhrJ3a80RXx_DZm-ebsX2oBUYfgLJFYLAI6fMar3ScvWSkRZZKxqqHKADDnPmicyiGTr8w7YnWIb45aBKj6bJlWH-z42FsSveYlW4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e63fb7b34c.mp4?token=oODwerBE2F8C2RebeJufPYxFAf8IBTTzf-OOKBast1IRrs2fLrJnbYz5-VmL5JRqpG-HvBBn2M7xA-fZ0kRmTLHL8QRLaQ4iBpbrL5kCphT_hXcBBhLffO1UNlXm3qxNDzsSC4A3k843jmmEfbgl7Q9ojY48reL-5fF3vXYecKULC60KRErQwbF1Fk8draJXMlfDDSmNLyi_0oLWaxTr6PDTKCvruqeM2pnxA6kvSLxQ_IEnIFgDSBWjRTJsc2oAXJMVUos6heRKPTiNxz7_xeaLz8LDDg5JCCkvvrnmXhnORkfbLg4hxnrextd8HQ3gP3DQR85DtSg3YXpfrvHylUMv2Lryf1HkqfdpQjUdO7H8UCpN-n0qI4XHLyYwty3nGlnPHayECsxctYTS44qialUK3_Zp8Q3t6cCHXwQvBl9Bf-VrvErO-Ja0tTS4NRl9vX4n89NE4aXSziIKc-eimsq79SH88xoYdq1VizzGL4ffPKYm-naqy2RoS2f7j1gE2q1s8bUjf8TpUEEi4ILf17Ny6hGq2K2u2J9PSmQcdtO1m-mZIZpzfQ9B_Zofs357R18U6PhrJ3a80RXx_DZm-ebsX2oBUYfgLJFYLAI6fMar3ScvWSkRZZKxqqHKADDnPmicyiGTr8w7YnWIb45aBKj6bJlWH-z42FsSveYlW4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
علی خضریان، عضو کمیسیون امنیت ملی مجلس: مسئولان دستگاه دیپلماسی ایران در دنیای موازی زندگی می‌کنند/ آمریکا و ترامپ می‌گویند که ما از توافق‌نامه خارج شده‌ایم و آتش‌بس تمام شده است بعد مذاکره‌‌کنندگان ایرانی می‌گویند فلان اقدام دشمن نقض آتش‌بس است
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/133519" target="_blank">📅 20:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133518">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
تصاویر بیشتر  از جزیره قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/133518" target="_blank">📅 20:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133517">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/COCEvyNrlcyRKdRExGj6dVVFeUdks3-BOSGLRB-XAY-9JKW6Qk2bdNU78PFekyG-ukVjxWT_SNPbrknNEZrtLq-9g2ZsndIJL0EQUZLGXOphXymiw39qKWCjRKSTS56ZI584Lzs0gE84kMRUaxqUVDcQB1FjNWiCA3BNIzdUisLk0bgORb7vsD8HysLx04r7RpMYaPE_qL_PHLiyhID0oWqcW5Hg380zzoKvNGBbk8PmZ8OrP9PTHjVIlIYDPpfIoUnzwyz4hhugTlHigwmk-J1wRke5c_uts0AgYx7MRGMEzBKVFXqBjRtpo1zcMvoCdRa6S7e0tuj1hPuACXdfMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ دستور داد که تمام پرچم‌های ایالات متحده در سراسر کشور به مدت شش روز آینده، به احترام لیندسی گراهام، نیمه برافراشته بمانند: به پاس زندگی و دستاوردهای برجسته سناتور لیندسی گراهام، دوست گرامی من و مردی بزرگ که دستاوردهای فراوانی برای کشورمان و ایالت دوست‌داشتنی کارولینای جنوبی به دست آورد، دستور می‌دهم که تمام پرچم‌های آمریکایی در سراسر ایالات متحده تا روز شنبه، ساعت ۶ بعد از ظهر، به حالت نیمه برافراشته درآیند. خداوند شما را حفظ کند، لیندسی!
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/133517" target="_blank">📅 20:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133516">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
نتانیاهو در حال حاضر در یک جلسه امنیتی با مقامات ارشد دستگاه‌های امنیتی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/133516" target="_blank">📅 20:35 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133515">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
گزارشاتی از شنیده شدن صدای انفجار مجدد در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/133515" target="_blank">📅 20:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133514">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
فوری/گزارشات از آماده باش جنگی تمام یگان‌های سپاه
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/alonews/133514" target="_blank">📅 20:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133513">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
اف بی‌آی پرونده درگذشت لیندسی گراهام را بررسی می‌کند/ تا کنون علت رسمی مرگ گراهام تایید نشده
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/133513" target="_blank">📅 20:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133512">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
۴ صدای انفجار در روستای مسن قشم تایید شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/133512" target="_blank">📅 20:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133509">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
ارتش اسرائیل (IDF): طی دو ماه گذشته ۸۰ نفر از اعضای حزب الله و ۲۰۰ زیرساخت مرتبط با این گروه رو نابود کردیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/alonews/133509" target="_blank">📅 20:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133508">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
فوووری/ترامپ: امشب جهنم بپا خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 93K · <a href="https://t.me/alonews/133508" target="_blank">📅 20:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133507">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
ارتش کویت اعلام کرد سه مرکز مرزی این کشور هدف حمله قرار گرفته‌اند که در نتیجه آن خسارت‌های مادی وارد شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/alonews/133507" target="_blank">📅 20:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133506">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
فرماندار قشم : اصابت ۱۰ تا ۱۱ پرتابه (موشک) از عصر امروز یکشنبه، تو جزیره قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/133506" target="_blank">📅 20:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133505">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
فوووری/ فارس: برخی منابع از کشته شدن ۳ آمریکایی در حملات ایران به کویت خبر دادند
🔴
وال استریت ژورنال یک ماه پیش در خبری مدعی شد: در صورت کشته شدن سربازان آمریکایی ترامپ پایان کامل آتش‌بس با ایران را بررسی خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/133505" target="_blank">📅 20:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133504">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
آکسیوس به نقل از یک مقام آمریکایی مدعی شد: ارتش آمریکا ساعتی پیش حملاتی را علیه سامانه‌های موشکی، پدافند هوایی و قایق‌های کوچک متعلق به سپاه پاسداران در دو نقطه نزدیک تنگه هرمز انجام داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/133504" target="_blank">📅 20:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133503">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
نهاد فرودگاه‌های پاکستان از فرود اضطراری یک فروند هواپیمای امارات در این کشور خبر داد.
🔴
یک فروند هواپیمای باری بوئینگ ۷۷۷ متعلق به شرکت  «امارات اسکای‌کارگو» که از اوساکا به مقصد دبی در حال پرواز بود، امروز پس از آنکه خدمه از بروز یک مشکل فنی در حین پرواز مربوط به یکی از موتورهای هواپیما خبر دادند، مسیر خود را تغییر داد و در کراچی فرود آمد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/133503" target="_blank">📅 20:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133502">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R9iPSW1jdr7SToqO1-wDD1IC1riJB6eSeCLBq3XbaQbhwIdIVKD3wc_VtvafnfIguqCSzDPqiOkuizSMvVbfsV1v9NXz7Yk-hjhgTgJfFUw6niXY68G5F0PWoju_n5enqKlph9EvtFm03nF746aXaIuHFVoJkw-9wMb6ZK55pyegXOQFrZOchRUzSttd-F1R_MDlcIiFJKPwTl-WlymmXUG7bVd-X9bNc0j3cBbsyFz3jHNnybclB5We1u7t187bz02bq4WsIUotprP3DrGPd_QlxDTRwi6UchHZvKbI6Yi6az1xyyzQmR-_2Q0K2TTEyX5HKdqxgnXHnXe7Kx9n2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویر بیشتر  از جزیره قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/133502" target="_blank">📅 20:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133501">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
فوری / منابع امنیتی به نیویورک تایمز.
🔴
ارتش ایالات متحده، مجروحان جدی را در پی حملات اخیر ایران، به بیمارستان پایگاه رامشتاین در اروپا منتقل کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/133501" target="_blank">📅 19:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133500">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKeVhMDwrCBWdLYl11afl6K0T7TFnMGX0JmcNqcw1d6Ng2-74rPt6V1iKxb4FQv1td_TTBQCtHARa4K3hu-7m3GPYExxAzCdhq5RqwBIwIvpT_WdMATKMA7wGOmLMipkzwBt0CS0PxP7PbXnnt9LVRWmlFOAmA96-JjaQJT2dumk3Z7Xd9op1JmulxHY7ND2gV2nnZTBum3-GnRKLty6z88UoKgE3d5916jI02Eu86_Ub44O7h9JAOdhbBk5VW4IvrFZO_X0_hI9EiuslPnrJ6Oh6QglpwX8BbCzGkVGrKOxJFfBD0r6M76aWfVuAQKSaziHNSciE7D5Cf1Uj90eBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از آتش سوزی در جزیره قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/133500" target="_blank">📅 19:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133499">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
ایالات متحده حملات تلافی‌جویانه‌ای را در پاسخ به حملات ایران به کشتی‌ها آغاز کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/133499" target="_blank">📅 19:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133498">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
فوری / گزارش‌هایی در برخی رسانه‌های منطقه‌ای از درگیری در دریا بین نیروی دریایی ایران و کشتی‌های جنگی آمریکا منتشر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/133498" target="_blank">📅 19:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133497">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56ca9785e0.mp4?token=ah7wiDN8ljVcIT198m6ZD0gJJxEPNhcP2HxRT2MwUJEnRxNr2IQ62EsI2QpWzxK8OF8ZbyOln2YNiOPqeBMmDAxYh7JY-H1yVu21XpLWYrtrhCBYvePgN3GATcvDoFz9S056Jr5PLdC45uLAFuWNyUUzlYwDx8NaVBwUvn8wQ6vnRkMQd-pgzeCPqABE69RGnFip57w4hxJlqtU_0ebFMXy83WleCVO9MrDExSLsN7jkQbdrhrEbxrliBnk3BOJlaeQeRVf3yX_uIwaD0fslbwNn-K2xERzrQQImvsa2mu53-nYxWRxNpzM2OLTwwM1Bu5DufTTbvMOBKu-hr-rCew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56ca9785e0.mp4?token=ah7wiDN8ljVcIT198m6ZD0gJJxEPNhcP2HxRT2MwUJEnRxNr2IQ62EsI2QpWzxK8OF8ZbyOln2YNiOPqeBMmDAxYh7JY-H1yVu21XpLWYrtrhCBYvePgN3GATcvDoFz9S056Jr5PLdC45uLAFuWNyUUzlYwDx8NaVBwUvn8wQ6vnRkMQd-pgzeCPqABE69RGnFip57w4hxJlqtU_0ebFMXy83WleCVO9MrDExSLsN7jkQbdrhrEbxrliBnk3BOJlaeQeRVf3yX_uIwaD0fslbwNn-K2xERzrQQImvsa2mu53-nYxWRxNpzM2OLTwwM1Bu5DufTTbvMOBKu-hr-rCew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصویری از مِسن استان هرمزگان
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/133497" target="_blank">📅 19:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133496">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
فوری/صدای انفجارهای مهیبی از تنگه هرمز به گوش می‌رسد.
🔴
گزارشاتی از درگیری بین نیروی دریایی ایران و ناوهای جنگی آمریکایی مخابره میشود
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/133496" target="_blank">📅 19:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133495">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
فوری / صدای دو انفجار در جزیره قشم و بندرعباس، ، شنیده شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/133495" target="_blank">📅 19:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133494">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
فوری / هم اکنون سفیر آمریکا در سازمان ملل: تهران به یادداشت تفاهم نامه با آمریکا پایبند نیست، همه گزینه ها اکنون روی میز قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/alonews/133494" target="_blank">📅 19:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133493">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
عراقچی: ایران از تمامیت ارضی و حاکمیت ملی لبنان قاطعانه حمایت می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/133493" target="_blank">📅 19:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133492">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
فوری / منابع خبری از شلیک ۳ موشک بالستیک به سمت منطقه المینا در کویت و محل شلیک موشک‌های آمریکایی ATCAM خبر می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/alonews/133492" target="_blank">📅 18:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133491">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6a433de38.mp4?token=FJH7ZlMBBDeWhj_Ni5JpAuULPj_oP9nK46qmFgxIIVl8ylEca8pM2YkxdZGleHnT-l0Bcr4OvmlpRRsnsRsSc4HZYCeSo3fI8eqf5s4IUfM3bkdsdbyiJmhgbNrfmfStj-85qz2GMHgof06VpIViKHvRZEuy-jkrvnKeYJncuqkQGNru9-lvig7Cxdg58jcTTyHBvdItcp8CbruitsoXjn3MyZnLtcEPvegNoCj3a-ShPRIwC8Sups_2-nukiZ4Amk0L88lA1az_TApiyNmXWF514GAj2xdmkyzqSHZvDy_9GgyqTBMDSBITcoKKe5TBV3UQOr0DV5IsQrFii8Bnrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6a433de38.mp4?token=FJH7ZlMBBDeWhj_Ni5JpAuULPj_oP9nK46qmFgxIIVl8ylEca8pM2YkxdZGleHnT-l0Bcr4OvmlpRRsnsRsSc4HZYCeSo3fI8eqf5s4IUfM3bkdsdbyiJmhgbNrfmfStj-85qz2GMHgof06VpIViKHvRZEuy-jkrvnKeYJncuqkQGNru9-lvig7Cxdg58jcTTyHBvdItcp8CbruitsoXjn3MyZnLtcEPvegNoCj3a-ShPRIwC8Sups_2-nukiZ4Amk0L88lA1az_TApiyNmXWF514GAj2xdmkyzqSHZvDy_9GgyqTBMDSBITcoKKe5TBV3UQOr0DV5IsQrFii8Bnrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک انبار در مقر فرماندهی ناوگان پنجم نیروی دریایی ایالات متحده در بحرین نیز شب گذشته مستقیماً مورد اصابت قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.7K · <a href="https://t.me/alonews/133491" target="_blank">📅 18:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133490">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
فوری / منابع خبری از شلیک ۳ موشک بالستیک به سمت منطقه المینا در کویت و محل شلیک موشک‌های آمریکایی ATCAM خبر می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/alonews/133490" target="_blank">📅 18:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133489">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
فوری / منابع خبری از شلیک ۳ موشک بالستیک به سمت منطقه المینا در کویت و محل شلیک موشک‌های آمریکایی ATCAM خبر می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/alonews/133489" target="_blank">📅 18:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133487">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c14311630a.mp4?token=vGiuXaWIjM5PBRklaumC2pRQ_P6Vh111-f7WaRl5CNBfKNWN67Yzk3-Afhd7ekeaLWUDF1PjT6CRevD609Pf4TbcjkBd00NiOiqo0nU8bGsD_a4RZzpIe_EnD_crS4LLMGbkUOzllHggcP9fZkDIl6WNDDGvPjjPcY65HCi4Axnjusj1raMDXD8fmzQnIQAc53u-E3M6A-EYS5orFQUYGk6cftOJUg8GtGgzwzTRBpfVmrXfIqtcy23GS15vZyD6nMEKO649WbMd_bbvwGMFQzNRO3EL02HnN4spXbBBr5-l-n_ogQpxyvi5dRM9RQJK8Jg5dUIN14wQAeTBRX1Agg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c14311630a.mp4?token=vGiuXaWIjM5PBRklaumC2pRQ_P6Vh111-f7WaRl5CNBfKNWN67Yzk3-Afhd7ekeaLWUDF1PjT6CRevD609Pf4TbcjkBd00NiOiqo0nU8bGsD_a4RZzpIe_EnD_crS4LLMGbkUOzllHggcP9fZkDIl6WNDDGvPjjPcY65HCi4Axnjusj1raMDXD8fmzQnIQAc53u-E3M6A-EYS5orFQUYGk6cftOJUg8GtGgzwzTRBpfVmrXfIqtcy23GS15vZyD6nMEKO649WbMd_bbvwGMFQzNRO3EL02HnN4spXbBBr5-l-n_ogQpxyvi5dRM9RQJK8Jg5dUIN14wQAeTBRX1Agg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش سوزی گسترده در کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/alonews/133487" target="_blank">📅 18:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133486">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T_ovty3fOkH4_DomdfetN7MRUpJfjYWqurIC-26Xd8SaPoQGLVlj8iiXerPAeSi9HkseVpaRqVCQQ94QZuWFsLaRm2Zxo_TD1IqmkIkr9DpCj2V3DD7QOCIW_O4Djsht6TBppsxRKfPkBDoI7yjRxrtvD8mqMmb7JoM0yjt3LW72WDl-CWrNM-u-YiPjMknF3w9inVTql6YZpvd-mSuWqpztqWXwv3diRtUPAZT8qmiQjUA2pNL7Y3FXg51HDNIBr9EXUl8xbJkQy5e7Uzh0o3orLFisVwXSW7xaXC3q9KU6zVS2xoZEnXl9fHJjJIThAmNux7DfPfE7BOJ_WSuE2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ستون‌های غلیظ دود در مرزهای مشترک عراق و کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/133486" target="_blank">📅 18:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133485">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
المانیتور به نقل از منابع اسرائیلی:
راهبرد محتمل اسرائیل، دور ماندن از درگیری ایران و آمریکا همزمان با فشار به واشنگتن برای تشدید تحریم‌ها و مقاومت در برابر خواسته‌های تهران
🔴
سناریوی مطلوب و کم‌ریسک تل‌آویو، بازگشت محاصره دریایی است که «بسیار بهتر از یک توافق بد با ایران یا یک جنگ کم‌شدت است»
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/133485" target="_blank">📅 18:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133484">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVlRHVkycwYcGoxn9GqiJWXM-YnoakWmLM4E2lu4_JCZCTUxocoMb3z6Mfyns0jLrievsx2rOrbEkEB--d8jXatlOp0KUr4UVYIuXqJomU8lNHvWJoYLYwz-yGikG6UZu5M99KTpq7L11ly4guar9X0DJ4J-iJoes7w653LxPclFp4fFN8ay8QHFleVZflralse0t0hqyxJIS4OroPQ5qSnB98h14pHtxBSxt3MuC1eyBK1qx4mMSSAZn11i-gPALzeWIStz_qLMMxBbRrvCNF1JCNFYQ7nmSwmWJj3Z7FSIFBuZkR7UL1ize6zhox4teFTBdxQhL1UurtC-3EljKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر ماهواره ای از پایگاه هوایی العدید در قطر که دست کم محل اصابت یک پرتابه ایرانی در آن دیده می شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/133484" target="_blank">📅 18:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133483">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
رسانه i24: انتخابات اسرائیل در تاریخ ۲۷ اکتبر [ ۵ آبان ] برگزار خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/133483" target="_blank">📅 18:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133482">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/365f150fdc.mp4?token=D6LXu2bjm5xZrvWiBL9PzDz4Iukmu7x28CHiFW2ZGW1prpzBkmVUZ2g7kQ1jdyKNiugLTcvTNMuZMkPmzfpZ9tBLYvztVuRXZ4ZTJcR3dVmkYii2__cs-LYuzelmsmEmFHZVKiZ6kpeHFr6iZWNc1q4GRWEiWjhjiK_VJ-BjYPIJD2B-gV9b5z2Mv718lSXxD5WgCi_PcOusZ7drwAZIII8HpAe5oisTKqNoicprmmOMs-jGdcit9sLIs0cQQ47lqVq9PFfNQRdvKKlCXnITPmonedh09bC22dxZKLNN6gI9B_epZ5F1M7ezpjAykTD7fkUNND9jl6Iuug7lWSU3Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/365f150fdc.mp4?token=D6LXu2bjm5xZrvWiBL9PzDz4Iukmu7x28CHiFW2ZGW1prpzBkmVUZ2g7kQ1jdyKNiugLTcvTNMuZMkPmzfpZ9tBLYvztVuRXZ4ZTJcR3dVmkYii2__cs-LYuzelmsmEmFHZVKiZ6kpeHFr6iZWNc1q4GRWEiWjhjiK_VJ-BjYPIJD2B-gV9b5z2Mv718lSXxD5WgCi_PcOusZ7drwAZIII8HpAe5oisTKqNoicprmmOMs-jGdcit9sLIs0cQQ47lqVq9PFfNQRdvKKlCXnITPmonedh09bC22dxZKLNN6gI9B_epZ5F1M7ezpjAykTD7fkUNND9jl6Iuug7lWSU3Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: فکر می‌کردم لیندزی قراره تا ابد زنده بمونه! بهش گفتم: "لیندزی، تو که جاودانه‌ای!"
🔴
و قرار بود یه پیروزی بزرگ به دست بیاره؛ همه پیش‌بینی‌ها هم نشون می‌داد با اختلاف زیادی برنده می‌شه
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/133482" target="_blank">📅 18:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133481">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUXJl_N4ZHcJd3ioQyjlKQMSdmWqgcBEEN_-G-7eFMNh1MPZKV_vODHDo1pADpgap-2O_q_hM-2An7zcRhZxV_dhSasGg-YabW4l4zCmXrS61DmBsggHUwBj76-8k90bTHoFPu5tWZsYXyMivfrQfA1nfUSsH0K-VLD_QkmVrW2bsK6yBBxftH9WUeGRNGEVNuP6Uka59kGBeXJX4XSXcAYINrCmH525YrJJKjKqOuHGEHGlO1KoiXymTdFw78WDJqwZ4aAizKgcZQTsXCtOcMqu3XGdnft0Xlb5t6EZDGJ2MLC80FCPgwFFw-bRn3kEQ_Y1aeGPU4ImZHK3CVEgmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون حمله گسترده پهپادی اوکراین به سمت روسیه.
🔴
بیشتر این حملات در حال حرکت به سمت مسکو، دریای آزوف و شبه جزیره کریمه هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/133481" target="_blank">📅 18:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133480">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/664dc8a38e.mp4?token=p8fOrg0_tOufCpvWMTey_RCbWT4cj6qr4jA_2DnRbXNuJlV8Q9sE_LKwHhs3IFYRJg6SggQAd7nX6F1dN9E7q8bBYSSxOliDncbmvlniMpE-raHTyb2tqy_ZOuiiVDGNmwNG7WpK7JezKGix8qeciXsUhlvdynusMJqVCAx-0rWizlwfeUmR75urcaikUvUA5-DLcE5HDaR1A-mfO1g0Jc-YJ1swzKysYdGidFNkwj0RYsq6EnfOaUXA4kmUCmosfQV6j4jBUdBYkSeiwplkiej1fiMHE6j0wsnk4HJYMdn_HkEjBQFDpGoYKDr49VevzMCrnDYJAzIl6p08TaHIIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/664dc8a38e.mp4?token=p8fOrg0_tOufCpvWMTey_RCbWT4cj6qr4jA_2DnRbXNuJlV8Q9sE_LKwHhs3IFYRJg6SggQAd7nX6F1dN9E7q8bBYSSxOliDncbmvlniMpE-raHTyb2tqy_ZOuiiVDGNmwNG7WpK7JezKGix8qeciXsUhlvdynusMJqVCAx-0rWizlwfeUmR75urcaikUvUA5-DLcE5HDaR1A-mfO1g0Jc-YJ1swzKysYdGidFNkwj0RYsq6EnfOaUXA4kmUCmosfQV6j4jBUdBYkSeiwplkiej1fiMHE6j0wsnk4HJYMdn_HkEjBQFDpGoYKDr49VevzMCrnDYJAzIl6p08TaHIIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تجمع امشب تندروها بخاطر مرگ گراهام
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/133480" target="_blank">📅 18:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133479">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
لهستان خواستار دریافت 10 هزار زلوتی در سال از آلمان برای هر قربانی رژیم نازی است.
🔴
در نتیجه تجاوز و اشغال آلمان، حدود 6 میلیون لهستانی جان خود را از دست دادند. بنابراین، درخواست لهستان معادل 13.8 میلیارد یورو در سال است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/133479" target="_blank">📅 18:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133478">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
علی خضریان، عضو کمیسیون امنیت ملی مجلس:
جمهوری اسلامی ایران چه با عمان و چه بدون عمان تنگه هرمز را مدیریت می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/133478" target="_blank">📅 18:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133477">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
وزارت خارجه پاکستان:
پاکستان تحولات اخیر را که
تنش‌های منطقه‌ای را بیش از پیش تشدید می‌کند
، با نگرانی عمیق پیگیری می‌کند.
🔴
پاکستان مجدداً بر حمایت قوی خود از حاکمیت و تمامیت ارضی تمام کشورهای برادر در منطقه تأکید می‌کند و از همه طرف‌ها می‌خواهد که خویشتنداری پیشه کنند،
گام‌های فوری برای کاهش تنش بردارند و تعهدات خود را بر اساس تفاهم‌نامه اسلام‌آباد (mou) حفظ نمایند.
🔴
پاکستان از سوی خود متعهد می‌ماند که از طریق گفت‌وگو و دیپلماسی، همه گونه حمایت را برای دستیابی به صلح و ثبات پایدار در منطقه فراهم آورد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/133477" target="_blank">📅 18:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133476">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
ترامپ: رهبران ایران دیوانه هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/133476" target="_blank">📅 18:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133475">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/491f5ab181.mp4?token=eopLD4EqWjFLGqT64sH9oSQEffYkjhjr2mRjCk4FsPojAZw21a3aAaBGjvohVbWyeO4phGd7d0q_gB1G2NKBYYIZq00u3FGYeRAcdH1Xelp8di72ZwhTcsQf-xNUTh2YTDQviVbkDW3iuQjjkRygmam0VD8nX4on3_dTKph64s4cdNOYSORTPLus1qsOU7Fy1ctZKAEC_DejXTS59CGfWwoATi1PLhoY4yfP2ogeZKQBlQTZTttcg-UJ4bGpIa3On-XaYvU5mQnzvfx_4QuoDpHkvF8BAWYG8ZFpISvurWVtxVR13mbND_RXqQbFbhlBoJh92aV_MMT62HunvJhaqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/491f5ab181.mp4?token=eopLD4EqWjFLGqT64sH9oSQEffYkjhjr2mRjCk4FsPojAZw21a3aAaBGjvohVbWyeO4phGd7d0q_gB1G2NKBYYIZq00u3FGYeRAcdH1Xelp8di72ZwhTcsQf-xNUTh2YTDQviVbkDW3iuQjjkRygmam0VD8nX4on3_dTKph64s4cdNOYSORTPLus1qsOU7Fy1ctZKAEC_DejXTS59CGfWwoATi1PLhoY4yfP2ogeZKQBlQTZTttcg-UJ4bGpIa3On-XaYvU5mQnzvfx_4QuoDpHkvF8BAWYG8ZFpISvurWVtxVR13mbND_RXqQbFbhlBoJh92aV_MMT62HunvJhaqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ :
چند دقیقه قبل اینکه لیندسی گراهام فوت بشه، باهاش تلفنی حرف زدم؛ حالش خوب و فقط یه خرده احساس خستگی می‌کرد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/alonews/133475" target="_blank">📅 17:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133474">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00ad100662.mp4?token=WhdYbaEDG2K45jWjZK1FDVm4ueXPLrQKKHpM1QfojGwI4MRiHgk8rD7E8v1CArRJeWkqeKzVHVNXTYAqUgsbDzfBQcQH13Y3zG5-dna6hQpBZyRCnope_WObuXHIaE9tHwiVk_3Y0dRCC71SNHz2Cj0Yx5pn0ZBddSXPpAtb2CMuc_1JnbV3JIW9Jsn0jgRtusE5KjJjfFCtXy_FYz5iz7vNE27p26KZwF7BaoOnKVsbNjpezpUbPWGGbYMxZtr3afKrePCnC2Zkvw3LlvbWTkSIilO_OwUFS7Obb9lFyhBTFCcMfZYQyeX-0NoE9MVMQhmaK-7lcdDIEgf00lmb5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00ad100662.mp4?token=WhdYbaEDG2K45jWjZK1FDVm4ueXPLrQKKHpM1QfojGwI4MRiHgk8rD7E8v1CArRJeWkqeKzVHVNXTYAqUgsbDzfBQcQH13Y3zG5-dna6hQpBZyRCnope_WObuXHIaE9tHwiVk_3Y0dRCC71SNHz2Cj0Yx5pn0ZBddSXPpAtb2CMuc_1JnbV3JIW9Jsn0jgRtusE5KjJjfFCtXy_FYz5iz7vNE27p26KZwF7BaoOnKVsbNjpezpUbPWGGbYMxZtr3afKrePCnC2Zkvw3LlvbWTkSIilO_OwUFS7Obb9lFyhBTFCcMfZYQyeX-0NoE9MVMQhmaK-7lcdDIEgf00lmb5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ برای ادای احترام به لیندسی گراهام، دستور داد تا پرچم آمریکا در کاخ سفید به حالت نیمه افراشته در بیاد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/alonews/133474" target="_blank">📅 17:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133473">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/321fd5e5da.mp4?token=iKdMxJD-tRkATSU06Ea4QXzidr9FwHEELtuMcxkymeH1Y7r2VM9rJ7pz7_lwZpklljG_r0QuEVykHmJzAmba1rpwpYMUeFu9Tmqqix2WaWNK8mSM9JLZou4Tp7FKyEJZZmHiXF2lkUCj5Du-Zf6FsWTBqD8mYlJDkMjA8sM4061aNER88wogrd5yaPgV58m_XeJl3MGx-WBXa_gtt1b3HzcL8NbY0QqMbhUL0gh7vbLZCWZpb80C4uTGqDdm0v05GAJMT71b9PbCaz1P6JimHaG8lZnSXb_CPx6d2a8aFEHjblSAed1lYpn6Vha4WESRHRVcFXfWJXp9UUDFaeoB0jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/321fd5e5da.mp4?token=iKdMxJD-tRkATSU06Ea4QXzidr9FwHEELtuMcxkymeH1Y7r2VM9rJ7pz7_lwZpklljG_r0QuEVykHmJzAmba1rpwpYMUeFu9Tmqqix2WaWNK8mSM9JLZou4Tp7FKyEJZZmHiXF2lkUCj5Du-Zf6FsWTBqD8mYlJDkMjA8sM4061aNER88wogrd5yaPgV58m_XeJl3MGx-WBXa_gtt1b3HzcL8NbY0QqMbhUL0gh7vbLZCWZpb80C4uTGqDdm0v05GAJMT71b9PbCaz1P6JimHaG8lZnSXb_CPx6d2a8aFEHjblSAed1lYpn6Vha4WESRHRVcFXfWJXp9UUDFaeoB0jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره
جانشینش :
- یه نفر رو تو ذهنم دارم که فکر می‌کنم گزینه خیلی خوبی باشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.7K · <a href="https://t.me/alonews/133473" target="_blank">📅 17:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133472">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
ترامپ: تنگه هرمز باز است. ما حملات شدیدی علیه ایران انجام دادیم.
🔴
ما دیروز با ایرانی‌ها به توافق رسیده بودیم و آن‌ها از همه چیز گذشتند، اما ناگهان دو ساعت بعد، با یک پهپاد به یک کشتی حمله کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/133472" target="_blank">📅 17:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133471">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
ترامپ: تنگه کاملا بازه
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/alonews/133471" target="_blank">📅 16:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133470">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QzYvKqJVRhmNOoqkzOaKToBViXSY79taCYjWrNyN5CRGRySaCWV05uPR8rJ7b8_wAAP-deFLFYHGPwablzfMDRu9UXk32zfwnZMHbwZbE5hlsxCF4Yx7cByWlo-4Zdl-si_6LzG9eZLtPayazw2wtVa1JU_gPRf8aduMtWdO6_AhUscZ7BPq7iiVO8-qwgSgrUJktzlxvYt3_mwEk-Dl5aaoonVmjLXayEkBsreq6oGT5jIG141Z80MW5FBbWbeN7K59DHDnRbo1DVx1i7OG1PoG4-nz9dZ7PvkZuT49CFRS4_cqfWgzpAuEx3Qj4xmyWDEbcT1x52wWnCothjcDIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به هوش مصنوعی گفتم یه تصویر از تندروهای ایرانی بده که اینو داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/alonews/133470" target="_blank">📅 16:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133468">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jIGxWTozZ0lbf8Lfe6w5282Y0ZrTZD7L0kjcbzz1BUSB5a0NTXBHYcQypI2cFvpGUL9AcGA8SbzDrGcz1qcQEZ0kboNP2G6C4upMpnLZMpRE9hdE4xrUZfynZRHbDRG9aOzNLyZ_YJ2Ip0ZdCjzTVK0V0dqxY8iRBZC4QHbvy4vQjvkyXo5FA2VmdmzGbAxrVCjDzpT3eU4wozN89cBqfReAYyUhX0hkuzRAj-CoJIDDgm8o0pYXUHBVZZTAGlAhPPKXSvzRki1h2kzeugSTTKovSKPIS7m_9XyyPHb-vvDapMHuFC6RDrz3elz3upMp2niYRESIsqMPD4Smh4QLfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XiMUbxtYr5frPV4eoZxMOzpMOFazdue4Ni9RiMRxwjhjwMpAh2ibYv-dYehmkTtdHVAqW_KfD_VVqBqVd7BktBLfynl40lcRvJWvSqHdA3bDGam0K0Ecz9BtmUqPmHzjlUt5JzHH8uwcd1rU8aQgG3enW9KpkCkwuGApSiP4pWTlNXhOSRqShbwDcyLSUrkG3lMbMxMYUPKptWCLgXueMOZcrb5-CS1GkZG29aQ2D7zG2tpGXxlom-xIXss1MrOttX-okG1tfhDgue5kNLizJw9Xq4GKIt2PT-IMvWAn5GflR69Ztm3a0Hbfnf3DANnJSK5Dvjii2g7qoErJAPAVfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
فراخوان و لشگرکشی پایداری‌ها(ملت معکوس) برای محاکمه قالیباف و پزشکیان و اعضای شعام
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.8K · <a href="https://t.me/alonews/133468" target="_blank">📅 16:35 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133467">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfylWJArnmtwWnnUx1mmhLKwHLMt1yIpUeEaPKny7g_Bq7wi-L6hZjDxeyznYAVrrJDGf6KZA1ISDsvht1-zWEaWR6kxd-GUxGR2XAf1iK7k7ryL4zpUBp2hWMR4E12n1xfHbyqd96Au10KXJzzK2sUL1H7Hf-pRj3D6l4N0XZ8UTy_xMx-segJaAIQWMTAO24N5_pnYzKZ5Mnkq_x2mUs1u-VpAISOW5xSGFxRkeyeUyYEaEyjJA6RRRUUo98Na05f7pi-S__NsyJEUgxMS59uMzj2gJpgCxMwj3ikHezhjIv6AXhW2s-fmb9WI9UM1kHFP6xqIePW_n5dNQ9olSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سازمان مدیریت مسیر آبی خلیج فارس:
به دلیل تحرکات غیرقانونی اخیر نیروهای نظامی آمریکایی در منطقه، عبور از تنگه هرمز در حال حاضر امکان‌پذیر نیست.
🔴
به محض بازگشت ثبات و آرامش، تمامی درخواست‌ها مطابق با برنامه زمانی بررسی خواهند شد و مجوزهای لازم صادر خواهند شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/alonews/133467" target="_blank">📅 16:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133466">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5608c7ac3c.mp4?token=sLxifyoWwaVxwsb44hOgYTG74Zr5hyv8-XkdxX5QFuPf6KLYxTu0MkVcy-_V-c5Xhf8q-fH3FqVTYCjuxnSuKfkXW2G4mCmnx_RYPyETylLEBN2-NOmNyJ_R2-s0_G1dyFxLRH4ZyVEtsBuNAOhUHzKN7pCfkKW78JDeRELan1AxiK5bfjBfQ3EdGCEQaCyuB_Od6tkBWkR4OkuwdWl8qj4GQE3oDFKneQutHU0Rx1uY4SzKTOdfQvGUFphT5ETJRO437U-rBTRpJYRLOAcVN-G_3mCchtUBuO2GlEKEYqko-SnIRCOZbOSi_UlFi53qq7q5uwvw-TQeIGcPPLX_Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5608c7ac3c.mp4?token=sLxifyoWwaVxwsb44hOgYTG74Zr5hyv8-XkdxX5QFuPf6KLYxTu0MkVcy-_V-c5Xhf8q-fH3FqVTYCjuxnSuKfkXW2G4mCmnx_RYPyETylLEBN2-NOmNyJ_R2-s0_G1dyFxLRH4ZyVEtsBuNAOhUHzKN7pCfkKW78JDeRELan1AxiK5bfjBfQ3EdGCEQaCyuB_Od6tkBWkR4OkuwdWl8qj4GQE3oDFKneQutHU0Rx1uY4SzKTOdfQvGUFphT5ETJRO437U-rBTRpJYRLOAcVN-G_3mCchtUBuO2GlEKEYqko-SnIRCOZbOSi_UlFi53qq7q5uwvw-TQeIGcPPLX_Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عادل فردوسی پور: آقای اژدهایی، خبرنگار صداوسیما وقتی صدتا موشک خوردیم و صدنفر آدم کشته شده می گوید همه چیز عادی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.8K · <a href="https://t.me/alonews/133466" target="_blank">📅 16:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133465">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
سنتکام: تنگه هرمز برای همه کشتی‌هایی که مایل به عبور قانونی از این آبراه بین‌المللی هستند، باز است/ نیروهای ما در موقعیت مناسب قرار دارند و آماده‌اند تا علیرغم حملات بی‌دلیل ایران، آزادی مداوم دریانوردی را تضمین کنند
🔴
ایران تنگه هرمز را کنترل نمی‌کند و ترافیک دریایی ادامه دارد.
🔴
بیش از ۱۴۰ کشتی در هفت روز گذشته از تنگه هرمز عبور کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/alonews/133465" target="_blank">📅 16:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133464">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12b2f989ab.mp4?token=SS6SBgWhtmbfSVhsIXCE5mSu03qW3-mntWXXRdzynjAvNkdi_WHFopDesPdc8sni_Y_mfzkGxlb0XFa0GVYnmqWKjZHdmadVJrTQ2LjtN1THtJWC5298_d5GBKsLU2bXHbVBglMclzWwK7uhPvfga_X1b5wmYOGNUcZR7PK7JVIUN1roBAuJhc2fRElpfgrq7gncAVlbm-OUq1QIffF4MnxpbU005f3yCEvLqh29Lg68iaMU6NinUMGnxI-HTsZOS91F3KaSadH8ScznDylMgCRiUfB_U-niHrXEXurZiwSDz6oC0N8iUitST5iGSnFNAxjHo9rn_LRLjMOL82q-BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12b2f989ab.mp4?token=SS6SBgWhtmbfSVhsIXCE5mSu03qW3-mntWXXRdzynjAvNkdi_WHFopDesPdc8sni_Y_mfzkGxlb0XFa0GVYnmqWKjZHdmadVJrTQ2LjtN1THtJWC5298_d5GBKsLU2bXHbVBglMclzWwK7uhPvfga_X1b5wmYOGNUcZR7PK7JVIUN1roBAuJhc2fRElpfgrq7gncAVlbm-OUq1QIffF4MnxpbU005f3yCEvLqh29Lg68iaMU6NinUMGnxI-HTsZOS91F3KaSadH8ScznDylMgCRiUfB_U-niHrXEXurZiwSDz6oC0N8iUitST5iGSnFNAxjHo9rn_LRLjMOL82q-BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انفجار اشتباهی در تمرین پدافند هوایی روسیه/ پرتاب شدن سرباز
🔴
فیلم منتشرشده نشان می‌دهد که نقص فنی در جریان یک تمرین پدافند هوایی، منجر به انفجار زودهنگام شده و سرباز مسلح به سلاح را به هوا پرتاب کرده است. این حادثه تقریباً به کشته شدن همرزم وی منجر شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/alonews/133464" target="_blank">📅 15:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133463">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUJ2BcydDI0b7xaUs53zz7w4Gyrvklv4JddZX9BCl8TpkVWkfZcV_Ai2of22950Y2UwKkkQpo62RJjtxRGdnjn1gifCY_BrBvpmhzLBIOhdwL_Fyd7ToTpfNLc7fFdRg7j9X4nKiZgo1Q4ZgbQJtnDp6e1DQuKOMyZvaDW2QNCoGkLpvNJ6zF-4-5c1bPpPNsJB-6iFIuI7YLXMlqaqwvRMbayJx3uHK-tkGdZ5YJ3s4CcLE5HZKoRcPefdVDkcH3SElCUJ8q0bNHZRneD8G4P3Q0fB63u7YZxT5bUMSkuIAlZ6Fi2lUP7UBUkLWbtg1vkgkFT4-R01P3cujz-MYxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده:
تنگه هرمز برای تمام کشتی‌هایی که قصد عبور قانونی از این آبراه بین‌المللی را دارند، باز است.
🔴
نیروهای ایالات متحده در موقعیت‌هایی مستقر هستند و آماده‌اند تا اطمینان حاصل کنند که آزادی تردد دریایی همچنان حفظ می‌شود، علی‌رغم اقدامات تهاجمی، آزار و اذیت، تهدیدها و اظهارات غیرمنطقی ایران.
🔴
ایران کنترل این تنگه را در اختیار ندارد. ترددها به روال خود ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/alonews/133463" target="_blank">📅 15:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133462">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل، کاتز : الان وسط غزه هستیم
🔴
نه‌تنها از غزه خارج نشدیم، بلکه حضورمون هر روز بیشتر هم می‌شه؛ الان بیش از ۶۰ درصد غزه رو در اختیار داریم
🔴
همون‌جا هم می‌مونیم و عقب‌نشینی نمی‌کنیم
🔴
این مناطق امنیتی از این به بعد بخشی از سیاست امنیت ملی اسرائیله
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/alonews/133462" target="_blank">📅 15:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133461">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
سی‌ان‌ان به نقل از داده‌های ردیابی: تردد دریایی از طریق تنگه هرمز پس از اعلام بسته شدن این تنگه از سوی ایران، به طور محسوسی کاهش یافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.7K · <a href="https://t.me/alonews/133461" target="_blank">📅 15:42 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
