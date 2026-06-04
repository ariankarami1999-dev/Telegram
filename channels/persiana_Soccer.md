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
<img src="https://cdn4.telesco.pe/file/nzACfbbfWWuyfUW4wktyxUZfm78Pu0BAtQnk6gccbfvKiWAVG85Eh0sJolt7qcdkfMJv2iARB8jX8xLN9wbjgri89-X9pzMcDub6u2T_tbN7gaA6KxJlDUFw7MXQMvbnmbY-hfJBUx7pR5GB8kSAUrtfpBl-MsXmNtk9tBkXAkWZSz0H3KUM1q2XkFD5r-xfYkSP0yUUc_3N-KWzQxO8-2OoVuKfQ_FErAVcJLvjk9GDVo6PzO740p9t3mKXbmyjFNZplS_iHiSOvK1SX8-YZLeFmyl5Tx_vb0kxdgn2_G7lWXadQu8ndDBn8PRyPZln-0ShpflkeSK902EHNAwEVw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 174K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-14 22:44:21</div>
<hr>

<div class="tg-post" id="msg-22791">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qAalfEhbCeZ6i9ow-fkBBew_WLd_f5iZuAzAOkbsXESrDqUua7QJaYIUfavLyCmT858iaL55ZXG7ceeG5jIhoCUDuqFAYGwA913isF0OY4PQMuoGmapX0niz8V81PsPOPY8sJIPn0883VZB7pwm87LdI4QukPDRDhP_sQRApA7IdP9aQVxL0BRABVQIbYqy3L1m8jUF9q5Xeh1uNr0hmJrdnzQpFRY7w1ukGW737G8OBJCFmu-9OorVhRVBZwDEnaU33-AULKjdnjn0Lky1YdAPOfCfX5Mr5KkPA-ot4o2gh3ano4yIlwXudMn93zsv5wBIn2fk-0rfZVPhWOo_94A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین تیم‌ های تاریخ رقابت‌های جام جهانی؛
برزیل با اختلاف در صدر جدول تاریخ این رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/persiana_Soccer/22791" target="_blank">📅 22:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22789">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hV_xgvh28yPofX3yn8KECmBMd0R7i5_FUEhBKual_6jzpIxBDBBRts5OQ_uOsGZz4KMse4YtNbUS7r7vhxS_nz1-m6zEsKzP36p3nxrLcj1aYppp4Kgevi6f1j-AvtRqR4i2QkCZ8OdkKXWKLK4fw71Ypy27L15_wmF8YJiX4Mh8anKpKm7uKCI_fMetXLapd3lkXZI2FVl7CK1x6nU5vhnqyszIknI2zk-u_5ibUsjg4wJrTag9LcvZlQVLmvaUwdAWU1YZKN2z37Q_yQHmlbn47CJsAPZFt__zdw1BPUT3GhFg0P1ZaZAqOIUQM_8hOvjj3hDj28UbWXSCJY9ofQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/psAJW9UY_zIOVe75PNnVDHD0dM8yBterz2emVX3awoO94GlrYW65dRpZ1C9NnS__FX6HYuZir52UZLGvsgtFvNiZtyS7-74aMfZoRUQmRi4JhC7El-wG7nNYM-FWjVN4c4s9J5ipC7bWQn-hiXEYpZjXpRVm-0ZdRhbV6Ekat0sGsW9UfAo8h4rf3QmLoc1wa31T7lcrbN8Fq1RoMt0mfSgOfg54-W6KFTkWZAIwKEswdeR-yqqWiGAaFxwZtGnTCE_-RMm8fI0Y8Aq9rI9GSu0Ta2z3pwONpfHCYp0lq3-qiEy4YA5DBm7twE6ShfOjuRvbKde4Ry0MY7yoxIw0cQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بااعلام رومانو: آندونی ایرائولا سرمربی 43 ساله اسپانیایی با عقد قراردادی 3 ساله رسما بعنوان سرمربی جدید باشگاه لیورپول انگلیس انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/persiana_Soccer/22789" target="_blank">📅 22:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22786">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31e7361d2f.mp4?token=RyR-qQjJ0AmS0k5i4KubuOEbd-R6B7HUjXeazwl2MmTeOYv8a0nvlxBUtKfcorHlnsQqN5C9ZfBwXsssOd_3BMI-IHTMgHC855grjrZU7LmjS3jcN-mjNayWo2_FT40-6DfrRtPac9ouT0SAT6FqhCz3IIoGyMCJQg2LkpME5JjjFFzG0zQCbFn_RZUHHZWqBjmeXNxKjeYWAkGJkLT0l5kBJkasfol_d4Or8WH905KLPpycyQQelDfMvZrDm62LOX-ibK3RQ995WUTle7iCIvJ-MCe7GrJzOEMMzVkIBPYzPEJ5MpMD4VGg2Q42iuLqTqkFfptozD-pISVRzcNRcK6M_DLWexg4rakRLAiTqoNu1KKGuaKitGc-THj3lEkNAhgPv5Z6sveTNF_vOu9q5WQb6txuK5-1qlMy16pWCIFtFyaxk0Ep7X7x19qLpFyYQU-AmbW-FSbfimW7pEkJ9EQ42vPdZeegQCeLyDoonDIAsZoEDzgLPIYr7izJ645hYDHLEdq9J5z8TCt65Qtb_PzWcFbcIxadm1Cz2vkR1V3tZ8XEGyzty2Svh4qGx6UtY2PcnYfF-n16WLM7pWMJe1ZddOgw8SQtoC2NCzwjDk842G9-Kz6mRXcIUjmkaJj7VOktkJuaP-ALtXTHd5sSPYNlM-0JuuTzyov5EW103bI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31e7361d2f.mp4?token=RyR-qQjJ0AmS0k5i4KubuOEbd-R6B7HUjXeazwl2MmTeOYv8a0nvlxBUtKfcorHlnsQqN5C9ZfBwXsssOd_3BMI-IHTMgHC855grjrZU7LmjS3jcN-mjNayWo2_FT40-6DfrRtPac9ouT0SAT6FqhCz3IIoGyMCJQg2LkpME5JjjFFzG0zQCbFn_RZUHHZWqBjmeXNxKjeYWAkGJkLT0l5kBJkasfol_d4Or8WH905KLPpycyQQelDfMvZrDm62LOX-ibK3RQ995WUTle7iCIvJ-MCe7GrJzOEMMzVkIBPYzPEJ5MpMD4VGg2Q42iuLqTqkFfptozD-pISVRzcNRcK6M_DLWexg4rakRLAiTqoNu1KKGuaKitGc-THj3lEkNAhgPv5Z6sveTNF_vOu9q5WQb6txuK5-1qlMy16pWCIFtFyaxk0Ep7X7x19qLpFyYQU-AmbW-FSbfimW7pEkJ9EQ42vPdZeegQCeLyDoonDIAsZoEDzgLPIYr7izJ645hYDHLEdq9J5z8TCt65Qtb_PzWcFbcIxadm1Cz2vkR1V3tZ8XEGyzty2Svh4qGx6UtY2PcnYfF-n16WLM7pWMJe1ZddOgw8SQtoC2NCzwjDk842G9-Kz6mRXcIUjmkaJj7VOktkJuaP-ALtXTHd5sSPYNlM-0JuuTzyov5EW103bI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
بمناسبت شروع رقابت های جام جهانی؛
بخشی از صحبت‌های شکیرا خواننده مطرح این مسابقات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22786" target="_blank">📅 21:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22785">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d39ef7da3.mp4?token=uUpkaqHsKnEz6ybvuMpuMK4DgUesJX2TMa6pRzxjYYsvpE72LwzL58_yxuKzTswZD96nziCoxeYPW8PvIDjm-MSQIki64rtzu7muVRBoTeU7Z_dSaa1MEjIddmRgX36yJ9TRH9dyWCTshF6v5nd-m65obrlwvxofrHtvI6IB0IqqrTlcPt7o6iUXjyrNlXmloTLu3uzI0Yy2TrVYOkR6REXN_AFYZUJPVH6EkvFB8fXne5aGE9rBjx7F-tIL47onVdStRG41vVw_urCEgiZBp9MCdYVCeSriNrtJcm1awlN5dsX2iI6FmxGq2ORoRN-rRa-U4WcEqX6lBUPZonVc_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d39ef7da3.mp4?token=uUpkaqHsKnEz6ybvuMpuMK4DgUesJX2TMa6pRzxjYYsvpE72LwzL58_yxuKzTswZD96nziCoxeYPW8PvIDjm-MSQIki64rtzu7muVRBoTeU7Z_dSaa1MEjIddmRgX36yJ9TRH9dyWCTshF6v5nd-m65obrlwvxofrHtvI6IB0IqqrTlcPt7o6iUXjyrNlXmloTLu3uzI0Yy2TrVYOkR6REXN_AFYZUJPVH6EkvFB8fXne5aGE9rBjx7F-tIL47onVdStRG41vVw_urCEgiZBp9MCdYVCeSriNrtJcm1awlN5dsX2iI6FmxGq2ORoRN-rRa-U4WcEqX6lBUPZonVc_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
جمله‌ای که تمام راه‌های فرار رو بست؛
فکر کنم‌مهدی‌طارمی هم‌این‌ویدیو رو دیده بود که جوگیر شد و به میلاد محمدی گفت بره مقابل تیم ازبکستان پنالتی بزنه، که البته اون پنالتی‌اش رو خراب کرد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22785" target="_blank">📅 21:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22784">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twFbsX-Y5X7TwrYtV1qyNLJ3ve9cn7fBh_kRb7bvjy-AtUqrke_XG0y4SuelruO40CVzeVA80naXUO9HQWFUVB8vn5oPqQTpZA9j9XNfTDlE3p0Af7kxRgKX8iFlBqIzf9irqeYECYSh2VipctJZkUpASMoUg50gjdPDMwxOKpX19Hz22e0IhvUpLE3LfNKmexob2jaRoXPg81duAs_ypCgcPiYSfXRmrtVFlhHpSSQlaDll3JPrdqIETW_6T2OE5eCuJ9xsl1pZiNn4GS3GNtThoy70HxknQIhhIYy5iDQ2oYyfw94bQRWD36QMr2ROp6y6g7jNR2UQiEXvVWPGhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه کامل مسابقات هفته اول و دوم رقابت های جام جهانی 2026؛ بازی‌ها از 21 خرداد ماه در آمریکا رسما استارت خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/persiana_Soccer/22784" target="_blank">📅 21:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22782">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hdQRm3WVc4YdJ14I6t-KfvFfX0w_vYhUi2SDLGJHHd5He0pgq4obzhNcJQaPkbRaNc2Hn2v8o63KDdEduOkH4XRlOgrHcRm_-fRGe_5vlpJ9dg5XvS3dGknJk8aS2w_uhzZAS4slFIwVfkwZhnXvK47WDMIWH7LYBrb5EG_YeXQa6qwwhSWP0DSdF7W6lFHa4qYYGZKHSfDmPwnwlxUW-b3tIa9CXrV8ZiR5DbllB9Mk8Tt76QyS7no2jESbq6yuCHWlaYnGUuXyZrJCa5OVuWvUw3fDdRNYcsRwPrbbuualtS0SgDz06EB7ZWAgHNp23iaKCjflDi8Ou_XhGHGgJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J0agdOBIACggOh1nwVXtjoljW7TckiXApYzHLEZ_RFKHckYgklWt7upiHKmaGgyIRvK89C94B8OT9D1zxeTg2lhXKYsb-77c_B1QAUKaqZqESwe6xnGg5x4qTE5ZXqpJtvcfha1sD5NREwwEuk1WLPgqJ8PG4CCZLkFl-pBYh_gUaMOv7fe2I-xRheZJaJhaK3_W9Xtou9HCf5Lk5eF-GtBk5sR63Sg32VtsIRGCP6PaW9z_4f_MEcaSeCfsrUjYUwBzJflnrIIN2YXZCuWlx4w6hEITs7WyhC-wmwbTYs_n6JBUiZAAt3nePVrE3QVdNpBat_4eoHvWbibX6ooUZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
برنامه کامل مسابقات هفته اول و دوم رقابت های جام جهانی 2026؛ بازی‌ها از 21 خرداد ماه در آمریکا رسما استارت خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/persiana_Soccer/22782" target="_blank">📅 21:23 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22781">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZyIzlqugKbMCXbNZE4v8VAXPZHzAmhHMw1KCeD0CY1I1YZ8lxDoZXrpYfELSQt6r-ddhDZto8Dt3XAgF3XUjMNdKJPPFUm8-8vsDIBA_1aHg6i2j--It96P6TR9soHTe4kR8JFJ9qsNIT5S07SUcwxauxH1Qv7xk8-ndnp_iRMK-bGZNjspOorOCYkTKHRBGVXDUXY0syIjjZgeE9BCZRU20vHiQR-69VgF0qu19ZCMS5m2AD6t9pwccNKYPZnZnVnSmSDuRoLp6RGh8a6x5UV7B5CLU36z8WE0vhfCvHzy4epkrCmhk_Pq1JGF2owk0kbGgev5aDeMnEAZUJwkWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇪🇸
تیم ملی اسپانیا امشب با این ترکیب پر ستاره در بازی دوستانه بمصاف عراق خواهند رفت؛ فدراسیون لاروخا ابتدا قصدداشت باایران بازی کنه اما بعد از قتل عام مردم در دی ماه پیشمون شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/persiana_Soccer/22781" target="_blank">📅 21:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22780">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J5xIOES4Dl6x47GMbgJsXpJ-7tlnBXNjoaOambanPARKfYWd-5k6WmsoRSe6GN7Bp8KfR2PWbkuSxt9z99xa81hihujBliV1Bt0OTYUnDi59bWnlfN6INyNHy0ITrpJMsN87UryIKBVJGke70cKtKvg1u24ObsSMXNDNhYaTjiKhyamKUWTEOS6EBP9wkzH8z-2bPENOiXq585kb7ts2s1Kie8Y33h9Xr9GnfpNyUhrR_g-dmoaWP5ApmmjjBb_td5F1tGdxwCAekyJ3bxXkpg7L6g3GxuPdRceZuY7WNhvn-gjEyy1I2O02ERuhygwQavsn0X4Kk0fZWp9_-eKC7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ ادرسون سیلوا هافبک برزیلی 26 ساله آتالانتا با عقد قراردادی چهار ساله رسما به منچستر یونایتد پیوست و جانشین کاسمیرو شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/persiana_Soccer/22780" target="_blank">📅 20:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22779">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">⚽️
اسپید با انتشار آهنگ جدیدش برای جام جهانی، هیجان بزرگ‌ترین رویداد فوتبالی را با انرژی همیشگی خودش ترکیب کرده. اسپید که سال‌هاست عشق خود به فوتبال را به نمایش گذاشته، حالا با این ترک تلاش کرده بخشی از فضای جام جهانی را برای میلیون‌ ها طرفدارش زنده‌کند. پیج‌رسمی جام جهانی هم اعلام کرده که این اهنگ در آلبوم جام‌جهانی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/persiana_Soccer/22779" target="_blank">📅 20:24 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22778">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gdQhK1aFOrI1_aZYpaiur8-hN3icgTP8G99c7SufynRcegIkmWRg8askP1Muhp8GAGnB8LTZIWbxiDpb26bnVsHzgpw_m5GIQnA9S5g_UamlUgaJtXU8pH0THTdMtgm4KhHW2PUSe-EG4oI4oEatB8fFlHek8bW7-PV_WOj7ipT-DQyW5CnncTaSxA-D6dmv3FXKzImlAAXCb_KS7PI9tDLI4lzB7zm4lbJhdK1WzSijBQwX6cCSp0F8jcVjGrKSUQQCpy1E3SFJFtD5dHyWPV4Vr1uPlA22cNjniVCrte8TS2_o-RUOxaEYbdDY47sHYLwz5gqevnO0fqU4_u_f-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شوخی‌جالب‌روبرتو پیاتزا ایتالیایی با عرشیا به‌ نژاد: من 58 ساله‌هستم‌اما چربی‌خیلی‌کمتری از تو دارم!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/persiana_Soccer/22778" target="_blank">📅 20:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22777">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPmbuE9xgkmQ9SmhDPYzctmTO86Tn-DGvWLlXm2qFuVroATyWk2MjTMOM9h0FVuMm5ASfrZm7VYRavso0MQrUo3Uq9mPlqA8tUnUltuss3KxEgD6p6hcc4P02mTEJBL0mhvWrTGGV8vy6HOMMRLZp8qN7GRjUnVDvb4q2KYbGaPLToYJnN9bqDRcJy7I9mheMF8tEkzHPK48NZdnl4mfyy1CNRDCreMgERDj5c1f8n_xyrozOaJqNbTxJbbCh8_yJdj-nlhbx-DO_o3xc2aVy3I8rlLWmWufqaF23QNFVS3QIUEUn8pN0QtKYNaurefy6EnXDOPZM9uXhw9OxLImkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ 2+1 رونمایی رسمی باشگاه رئال مادرید درصورت‌پیروزی پرز درانتخابات روز یکشنبه هفته آینده. بجز این سه نفر پرز به آقای خاص قول داده بزودی چهار ستاره دیگر جذب خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/persiana_Soccer/22777" target="_blank">📅 19:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22776">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nXWta7Eb7QPokg6GKVPHy0jFojaaEViiDpG3mNZuRHa-nKmA35rFAjOaq4nUIpR141db5DHDEbrqi_gqet0jaPlPesWUHDNv31TdPESYSJ828a98-0Eb4P4OTn0NhrcqUYkssGfcaLjFSOs17UweE1YxAksTKkZ9rnBlBlSRdHBqRrWYpnvE39t4_z3HjqWuXwBO_slNFYCxobPwvvcL8rpARoWYPqtuX7i-V9I0FIDsVjfUdn8tNGntufK1QjlLRzd4OEJhCZ3by7KizDm0BJe3QRZz0DlU5TMJiaN6_NMT-scdVzZYBWGmJk_1vZxepHFdTMKrWb4RYJBuIsvEYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛طبق‌آخرین‌اخبار دریافتی پرشیانا؛ فیفا تا 15 روز آینده در مورد باز یا بسته بودن پنجره نقل‌وانتقالات‌تابستانی‌باشگاه استقلال جواب استعلام آبی ها رو خواهد داد. وکیل‌جدید و ایتالیایی که علی تاجرنیا استخدام‌کرده به او قول داده به هر شکلی که شده رضایت‌شاکیان‌وفیفا…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/persiana_Soccer/22776" target="_blank">📅 18:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22775">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vrvMj5UeRheQaXP1yU03qA5Yy4_T8NY1H8Q046UuwFjG-wyaoIRKBLh9ZgSV5lWRc6WWzAQjAApS__FSEaE7fn1danME-IaQSgo0ssA_adY-9DPVUCYczVuloJHx63LNFKI9T4g1GiWUOI7cUBp0S6qy3bTHT_VY7eRONPaNF0vC4bpl8i77I83V8Zkrw37FhqNJ2qzjX5bsd-7zUEyIlTFauIfYOs7GHKMWAIbl1qsZGbl07haHP_JMapNku-p7lIl48cAUptj2x-a2efVWCHfxIsPEWX8qr073wmlubPawfZFAxAFxE150bTnEFavto6WWBM4omZp3Jo4Ia8AMbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ اسکای اسپورت: ریکاردو کالافیوری درلیست خرید مورینیو و فلورنتینو پرز قرار داره و حتی مستقیما با او حرف زده و به زودی پروژه عقد قرارداد باستاره‌ایتالیایی آرسنال کلید خواهد خورد. کالافیوری خودش برای پیوستن به رئال اوکی داده.
‼️
پس تا حالا لیست بازیکنان…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/persiana_Soccer/22775" target="_blank">📅 18:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22774">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q2zXmYv4UNtVEVlNhs7y2epldHE7SvdkJ-RzVXBtb6UnYpSciEwg4jPaGRiQ7ldKeXDe7Fa7IaAH8Y0lDGYhd2XVa5o5om087yzOU-loOtdo4XVfVjtHKDguBa0jpSd_Uifcv4ADwF94P46K815bnXL34AKCjJn8hEkTa2hkzLge9ug3Pt874L23y3sw2JXC2Vw98B_Eabf-4Iy8Sfa3hwyd6SPyEKWCarhx-j6iBKXl74Tff5V7OagExX8fVpi0ubsDQhnE1dSOPy7js-fgomlAms5wmn9taifH-VIAQRFb5eEBpEqHa0PgaEv-ulOOzdW1WUSAU4rEYHi92iSXBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ انریکه ریکلمه: درقرارداد ارلینگ هالند با منچستر سیتی بند فسخی وجود داره که بلافاصله بعداز انتخاب‌شدنم‌بعنوان رئیس باشگاه اون رو فعال میکنم. به تموم‌رئالی‌ها قول میدم رئیس بشم هالند و رودری دوستاره سیتی روبلافاصله رئالی خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/persiana_Soccer/22774" target="_blank">📅 18:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22773">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rcZR0u8nTo_tmX9BxagFy2VNmiBjC9RuBxOhyPKDYjHq29SRPzw8ek3n_vJWi52HFtWoD3D37rRvJzOwKvuuAZLxxSWvYNBrJVzRhSqSObdzp7g6zepGw6KD595V_BQqHbptD7D0260Z7ukq9GlqUYo5pxIUggHA0U2q9ucxfu_iBR02rbtose9c2ANiz3EptvFn4IWUF4ZHhIgAdGQZsOt3jDBrEO3Ezt6GVa6sHhuT3rIGVUGssgUKt2JxJgJ2go7tF7Oj23xDxK75N5IYYz7h5pWlt7GiHOVjnwn9RBWsqDO3lcXbxFcnPtIa7YvRXueP_rZnygprJ6fCxU_vKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💳
در
#رومابت
میتوانید با کارت بانکی ایران انواع ووچر و همچین‌انواع ارزهای رایج حسابتون را شارژ و برداشت کنید
✅
🎁
10% بونوس برای شارژ با رمز ارز
💰
10% کش بک روی تیم محبوبت
💰
100% بونوس خوشامدگویی
🎁
20% کش بک بازی های کازینویی و انفجار
🔥
پلن وفاداری همراه با کش بک بی نظیر
#RomaBet
📣
‌
#بدون_احراز_هویت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⛔
در صورت فیلتر بودن از طریق VPN غیر از سرور انگلیس ( سرور
🇺🇸
🇩🇪
🇨🇦
🇫🇮
🇹🇷
👇
👇
)
🇪🇺
https://trentivo6402.bar
✅
کانال تلگرامی
#رومابت
14
👇
🔵
@Romabet_official</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/persiana_Soccer/22773" target="_blank">📅 18:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22772">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c00997812.mp4?token=M1lfS6KbeL0vbcKz5HAR1YCW6PMKGvchMeTBm6ancwsf-_q58-WirQeiR3ixXmkF4pxZo-LTNLmDoAsfsYLBFnOBnhCM_lBn0drsATMpBjkCNqluI29xNL0DDf7oJdLRFBT8Pv0yb7Syly0IUIS_NdbNE1KK7mkmau00YCXlgBX6j_T6unpYJto6KN-hROYGr8s8XQPxgZBgPJWZmAzZxfsenogkUVEWlXiG9-BxilbysrpVN39_oEP7xo8CcrXw113INJPdQzfK3hyfwHRvdV7RXhJ6qCcWMlWJvzTozUwrO-SRhEyyV7NXR5WbBnf7x9XgsYZ19o7A6u5sAN64mC8VqF2jV-ocrTsYPUWrB6ysHhoV0Ta3bYtPccbyysI9oh6VblsTGGa9Vzui-PkBtC1Jq2zCGJkE73dqzoIKM6ngRJ8_fD6J2fi1fDx2ypxn7wGKWvDYNMfTfHtQ_X1n2h_JLo_nE41RBLZE4h6U4C-3IEkeCMwoqCDDYPzOZqmBD4PNBXo9CNsLDgxUlqAxDDpRD_dvM3ZxHXyoVhNu-0OpQyMUmrXD0f_-6Q1eaIbYPaehBpx4Z5rvCokSseahykf572qwKbN4v3FmOSQeURRBPpYe1-E8fKWhP3jXbETVeYNG7F44VAjh68NVySJ_NSik_P-UG3nrjvLa7iOa2zk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c00997812.mp4?token=M1lfS6KbeL0vbcKz5HAR1YCW6PMKGvchMeTBm6ancwsf-_q58-WirQeiR3ixXmkF4pxZo-LTNLmDoAsfsYLBFnOBnhCM_lBn0drsATMpBjkCNqluI29xNL0DDf7oJdLRFBT8Pv0yb7Syly0IUIS_NdbNE1KK7mkmau00YCXlgBX6j_T6unpYJto6KN-hROYGr8s8XQPxgZBgPJWZmAzZxfsenogkUVEWlXiG9-BxilbysrpVN39_oEP7xo8CcrXw113INJPdQzfK3hyfwHRvdV7RXhJ6qCcWMlWJvzTozUwrO-SRhEyyV7NXR5WbBnf7x9XgsYZ19o7A6u5sAN64mC8VqF2jV-ocrTsYPUWrB6ysHhoV0Ta3bYtPccbyysI9oh6VblsTGGa9Vzui-PkBtC1Jq2zCGJkE73dqzoIKM6ngRJ8_fD6J2fi1fDx2ypxn7wGKWvDYNMfTfHtQ_X1n2h_JLo_nE41RBLZE4h6U4C-3IEkeCMwoqCDDYPzOZqmBD4PNBXo9CNsLDgxUlqAxDDpRD_dvM3ZxHXyoVhNu-0OpQyMUmrXD0f_-6Q1eaIbYPaehBpx4Z5rvCokSseahykf572qwKbN4v3FmOSQeURRBPpYe1-E8fKWhP3jXbETVeYNG7F44VAjh68NVySJ_NSik_P-UG3nrjvLa7iOa2zk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
ترکیه پس از ۲۴ سال بار دیگر به جام جهانی باز می‌گردد؛ تیمی‌که با تکیه بر نسل جدیدی از بازیکنان مستعد، از جمله نان ییلدیز یووه و آردا گولر، هافبک رئال مادرید و با خاطره شیرین صعود به نیمه‌نهایی جام جهانی ۲۰۰۲، وارد این رقابت‌ها می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/persiana_Soccer/22772" target="_blank">📅 17:36 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22771">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CwGUspRx7xEsO2AjvO_frLWkiKG0m0tul-Au72gagZ0Md-uY1rcahjISIbhQ4i_8r9kR_CK6oBHAMr0SYd_vDMjNJYadOUF3wNgOiJ3uk3zH1ZtUGvA5ra8YfLbK67_pCGbrxXebPsl9Lh27gOYDfxtFPCdEdQmTT47Xl_Avwnp11PTJHkZXsbMuaLOPv-c3swkyNMotaL6i5HJz5WgEi8OeugaAZzwQiPHcgrsH4vzrxtoZMwHLnHlvUmfmxy7ZMo3Cee4YGpG8OjpfEP8WKt0lvES8fD8xilGdxv6jRCpZRrwY30Fh1Pj0GYUB37Z5_HM_pMwCw-bAAoENDmc3PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات|با اعلام رومانو؛ دوشان ولاهوویچ از باشگاه یوونتوس جدا شد و قراردادش تمدید نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/22771" target="_blank">📅 17:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22770">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10d92766a1.mp4?token=cPVjOy_BvUU2Bzeo2zPMZBVw-yWE3UeLMOXvslRu3XmZMX6_smFrtybMH984rzUzasahvsttP7zdY0oudewMiNz46Jeg16geuKg23wEEbdGwhA1G4P6RO49NIGxYC--a4tgTWKptZHggINyenV3ARtIQbTyRbxEWEKDOThArFK4cfX2bpOQU3bl1EyuIBjijGNLNrt2nHBUyaIu_-DiwOwltM5N9aRWAWdjCy0AfDUAslQsz5GlAiPxoBQQz6QKgkV7Z6inf-bxgA01QyR4TYOQgw1l3yW8QCu0-ZQl_M7Z8T15V3qxbzqxam8cICblLXZUAKLGpQkEI6IeQ7x2Id2_1q4fkvrxmi8yn0zlc20IzjTOHcdJZe2beE7Pdj84YBX4sjB0cNyoDR38NyBc1rLEzMYCOCLECnUG0vpq5Zs06QpeebkV_4rmWi8OoAg8EyW1F8RnoplPGu9jJDs9JI5dR0_8gMHC2TltTNWmFoTak5J19AHeG-VrEFJBFwZm1-veCr0KBFG-Wf8tVsDsa95dDVrq7U_hQgiaqDuJn5oO72drjPZpBKTUpwuh2v8huiFObkUQ5Mlyv6o2-qntxqkZMoYC_Z7z-8bH2LgR7EatJu6HvSuVqMpW1QoDXPMbnF8vC6OSR1L0HbGVuQRaEKfLQBba6sr3NEx_Pj9DP9YE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10d92766a1.mp4?token=cPVjOy_BvUU2Bzeo2zPMZBVw-yWE3UeLMOXvslRu3XmZMX6_smFrtybMH984rzUzasahvsttP7zdY0oudewMiNz46Jeg16geuKg23wEEbdGwhA1G4P6RO49NIGxYC--a4tgTWKptZHggINyenV3ARtIQbTyRbxEWEKDOThArFK4cfX2bpOQU3bl1EyuIBjijGNLNrt2nHBUyaIu_-DiwOwltM5N9aRWAWdjCy0AfDUAslQsz5GlAiPxoBQQz6QKgkV7Z6inf-bxgA01QyR4TYOQgw1l3yW8QCu0-ZQl_M7Z8T15V3qxbzqxam8cICblLXZUAKLGpQkEI6IeQ7x2Id2_1q4fkvrxmi8yn0zlc20IzjTOHcdJZe2beE7Pdj84YBX4sjB0cNyoDR38NyBc1rLEzMYCOCLECnUG0vpq5Zs06QpeebkV_4rmWi8OoAg8EyW1F8RnoplPGu9jJDs9JI5dR0_8gMHC2TltTNWmFoTak5J19AHeG-VrEFJBFwZm1-veCr0KBFG-Wf8tVsDsa95dDVrq7U_hQgiaqDuJn5oO72drjPZpBKTUpwuh2v8huiFObkUQ5Mlyv6o2-qntxqkZMoYC_Z7z-8bH2LgR7EatJu6HvSuVqMpW1QoDXPMbnF8vC6OSR1L0HbGVuQRaEKfLQBba6sr3NEx_Pj9DP9YE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
مهدی تاتار سرمربی گل‌گهرسیرجان از طریق دوستان نزدیک‌خود درباشگاه پرسپولیس اعلام کرده درصورتی‌که اوسمار ویرا از این تیم جدا شود حاضر است از گل‌گهرجداشود و راهی تیم محبوبش شود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/persiana_Soccer/22770" target="_blank">📅 17:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22769">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQmt-KCO99QsYt_WmYdsrBwjF0-j-bD7h1X9xav2-dWOnVkTmIN-91HW0Jet9k5DH-4gV7tOKKFLCOUQjRqxKtIZA3t01hSmZehjl_nV8fIOlcGni8kQqFh2Gl4PJtEpnjon2WHlhj9wNqE-Nf7R4-ckYn6rTuhaJHWhDi8U5sQCmNqX_AfLbIEPS6OS4Pc47KX4timMLCxczETCZgo2zkqxacVgiS7vodBMHPbNlE1c5HS3u7F_RxOpp1TdUFAZF11LXYD9rsPS0BBa4BEf4RF-MEhXZ3SQcgOP19DtFq-K5xedweyQDm46L_Q3eHzCl8xKKJU9tKovM-EZ8xGXZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/persiana_Soccer/22769" target="_blank">📅 16:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22768">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Brajad58XsQu_voyhH4E0enBj8jp34PbnLK_fB1qV6U5aHOeHZ5x9sL7tHVPxNk5JYdTn6aIF9JEAb6KBWruy2RErIyEQSrvMK9pYH28UqHjwh2ezo0Tg5qNlQ_p1uZgpVeK9r-tHKtZUS7Yff5fRq3O32mTsoqyLX7vT81G20A7X0EIvh02bboOgHcTVTqZKJKf9XWnth4ZLUd8HQlggUMwRlEcdeMA9mRe_ccVeXIAIay8Ryxb8obVHHxU5pUHxOPQU4nfxc-ue5cdewj-zioP9QWp1DrlRnrj_Lzj6RUSxij9-ChNRjB-mWNEgcsdsjq6xmilKBlJ3QuRSHs-0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
یاسر آسانی ستاره‌آلبانیایی 30 ساله استقلال شب گذشته بدلیل‌عدم‌پرداخت‌حدود 3 ماه مطالباتش به‌باشگاه خود نویس ارسال کرد. هلدینگ قول داده تا 72 ساعت آینده 250  هزار دلار به او پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/persiana_Soccer/22768" target="_blank">📅 16:37 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22767">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q3QuBfFAldHVQbNf-cNoQEqhmeD1PyhX4cBMUgmqzF5vM4cUpgK4vQtr0XqsH5FBwefbEPWWM7dUpjkFb5fGZ3vOihQ-8RHKdvBmJJ6zoYTgtb-dwGgjeWNUhOMLwcG9BN1fSd5WHVzmMV7uxYGmEXNNX2xMxTZFu0RthBtt6QpgKr-0x-_L7sRFvDQMo2YwyCx3G1cnRwBXRmnhJ32pDx8ykFseFxgsO38at67VueOfLY8Er71ZJba_eq47EMg-6t-vxDQhxIIGZarPqo_OFVykMH7dvtAYU8aWygHFaXSsM9qfbqGapxAUwmZDxyHcsrzXzTX7fq2jTwgPDhn-Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/22767" target="_blank">📅 15:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22766">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vCcO3RAWfbm7nd2K6_1nzAyJiT__4qQWedLxb3MUXkVoqP8RFnoRCip8kpXpxk62B12uQwm8p5qZO_FdTu-ARPnY88UeMgr7UW-IN6flcXoMHH85RYN84o4aYMroXBpqt8NgSPNsnHEYkrKOn71zDOhaZd4QwAH7Q7BlmK4MwGWm_Smmsi0z9BTkHuHTENFQuChbcIMVWcX5VncTat_QRl72isBjejxBr3vMRTpFA2zCQcUyLNpATNBf7NiJCwMMt_h8jqF3cO04N0Rhk7OjAYFeROft54mAzzoWVftyZ-KbxjBQlqBKTuQ0b6uGmttsCJGAv0GSTyyuKPnwRwfqkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
علاوه‌برجذب‌قطعی‌کوناته و دامفریس؛ ژائو نوس ستاره پاریسن ژرمن و یوشکو گواردیول ستاره خط دفاعی منچستر سیتی دو بازیکن دیگری هستند که هفته آینده فلورنتینو پرز بعدانتخاب‌شدن بعنوان ریاست باشگاه به تیم رئال مادرید خواهد آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/persiana_Soccer/22766" target="_blank">📅 15:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22765">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔵
مسابقه جالب بین کیلیان امباپه و نیمار جونیور زمانی که هردو در پاری سن ژرمن حضور داشتند‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/22765" target="_blank">📅 15:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22764">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qshhBdHY3mFxrS-O2739Y_OhYUiuLZY3FRpCqklgSXIybw5xz8K_e7FhUZ0_i3ucA16bpyKcrjZg4oGLCDp_YIcAB4F57dtBV2PBsv2umuoyo6YYOZinQ-mjMMhENhKeDfmBh0fQNmXXTKlHvGEyEWRLfmDF1uHjCeczpacvStLfpccUQmRLfAxpZ_l_mf_QFMW_DPBh4BCGILLlxeLBw7AUNVLOPbqTor0PgGNRqdcbg3jrK4MZFSVmIzHYLFLZl4Cu4_3bTEcW-B07h7HnF5JmHw0_R2r_0wC1MEIgnku8LP3NHDAfeFVAvk3mep6Z8OSyLMhw6fUDr3bNNANkPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛فابریزیو رومانو درلایو اینستاگرامی خود: مایکل اولیسه ستاره فرانسوی بایرن دیگر هدف اصلی پرز برای تقویت خط حمله رئال مادرید است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/persiana_Soccer/22764" target="_blank">📅 15:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22763">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nsElsNA9V7CFN2_D7p9Rx0q3xo2ibCxGzG_Gv3axFj2_bkd8rMRNg0q_5iJntNqOdb5WyVzyzWyNSKB3efJN_DuFDgyXagrb2TbUQaieq2Zx-oKJcp4z2JWGZ2GX-Oc59Nc-rblOye9RsfpX2XOeue0znSoJ2L-1XGNbhQe5HzTeei8TU-wXBcUiRjs0uHWsmKd6TRyvIf8xl3gPlkCc27M3Be6xHeX-d_7spde4A3VrWcGa4Tsa4tP66ulSGM6qAfw1iXhPt9_AcKHuf9hdFsZg2NfLYZsq5GmU63j3UtsOpdJKWQtzFUnlUkUC8YSg_eUajZOayVFShyM3VJalaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این چهره که زندگیِ سرشار از خوشبختی‌اش رو درکنار زن و بچه‌ش مشاهده می‌کنید، همین چند روز پیش برای دومین فصل متوالی تیمش قهرمان اروپا شد و خودشم یکی از بهترین فوتبالیست‌های جهانه. عامل موفقیتش هم نه مربیش بوده و نه همسرش، بلکه فتحعلی‌شاه بود با تصویب عهدنامه گلستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/22763" target="_blank">📅 14:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22762">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qXJY7nXhfLduGfduPaTBgxVjLVqoaC8LG_o5Q3eYLUxNL47dyBntYGpDAmIzN8V8WQL3hnW6UDY5_ERppSYqs0_1c3HAkrFToOQ7EVpgMzDEjh92kR2SlVouUx5bFDjh0mUXcNeZvG7m7MqQhuiQ5gVWrsUjvwQacsRIEjmpgWZCkqYg8hhO--EmaEg4I6m6Bb-TyDkw4OMYD8OJ3NyZ5l3vDj2bCs9-cnHfKejd9pD0bQeuuSkILb4mC8gPzA_waWPyUaIjRBMRRRs_HXNpboCqatqgH1xNHfo4kyn4NSreorTZOesMANOBXsaHT23jhGbn01vLAGmdQEeSRW6cGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
رسانه‌ معتبر اسپورت 4TV کرواسی: دراگان اسکوچیچ سرمربی سابق تراکتور از باشگاه استقلال تهران آفر رسمی دریافت کرده و احتمال بازگشت دوباره او به فوتبال ایران وجود دارد.
‼️
پ.ن: اکثر رسانه‌های‌کرواسی خبراز مذاکرات ابی ها با اسکوچیچ‌ میدهند امارسانه‌های حکومتی…</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/persiana_Soccer/22762" target="_blank">📅 14:47 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22761">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u5zh5S6T40BoQ6_xAA-uyy6bskTf8u3wdihExntiV4wMQBichMc7uMzIib4o6TnmtxpsRztVLpPEVyissX2CMLaVQreeNiOmxpsDJKnrvT40L8MCiam20GSjfEJruRFA-_9RYDVs56EU5LjX1E8lJcVJxYMz4bwpRAxkKkLdCfpCXuoYhRMoX32gu_9BoTqy_XtDNAuh3FjxUdijMQJ7t-wWxHTK8IEFZ5NXqMZaoTlNfj7lklIkUmOkvGJk97dhcuZpRlnodsRAU-AXoLPSbAFtHoz2svw3-OA_A-7C5gT59Kx9gY0QmQzKcZxOfG2bcVw5lBvt3a89rYzcF0mF3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#اختصاصی_پرشیانا #فوری؛ دراگان اسکوچیچ سرمربی‌کروات، موفق‌وسابق‌تراکتور از طریق ایجنت ایرانی نزدیک‌به‌خودگفته درصورتیکه تکلیف مذاکرات جمهوری اسلامی با آمریکامشخص‌شود و دیگر جنگی رخ ندهد به قطعا لیگ برتر باز خواهد گشت و به آفر مدیران باشگاه استقلال پاسخ مثبت…</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/22761" target="_blank">📅 13:36 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22760">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VKBVoUBmAUHj-mw6KeQBSjp4axi5xEOwYt-EZNBDa_I-fqBIhZ7eB0oThC0D6iiGKAyIbyoouW_aZKaZXTZAF8dx7DB21QJ3Qp_8rxxattI2YY5EHWxpoaliRQcEOor4LZeVGtLoa827VqJV35TsTvRcBfHQUgof0CI96zp9WMRGAYQcbpQ8R6ikYCABamM31OpOU2i2r0byZMPnskv9GMXoBQByQz5Mn26_4WPY2Tr7XYpE6Obj31x3lasQIEWKp9oxkRkgo-HKFQbOdteFygPkmzkI3eiXsjLkWRbr7Q0RzKCYNwvFve2A8Q_H74-Ti4enebarXZUcWAHP1PgLaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ اسکای اسپورت: ریکاردو کالافیوری درلیست خرید مورینیو و فلورنتینو پرز قرار داره و حتی مستقیما با او حرف زده و به زودی پروژه عقد قرارداد باستاره‌ایتالیایی آرسنال کلید خواهد خورد. کالافیوری خودش برای پیوستن به رئال اوکی داده.
‼️
پس تا حالا لیست بازیکنان…</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/22760" target="_blank">📅 12:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22759">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OyQNvHAGn7EtDGTvCexcHvbXmOy7D-p-cTiPEyZ6c4qqAwuKmsODZ1jPOlfaTchiKrqIWZNU4zTripJz6euLf_Ny4eQ8L5hsRvzLyNQe-MtrdLu4VfuJNByBPrU8_dTbtmODnzEUHi4jSRt2EqQuV491NCzAdno3HQz7jHnmhwaJhXYPGXJ9wgHh-o6gyHAKwjbTYigVYLi_PH9a0tZ-j3cIpR0wPMi99-9pqhNEJhbReWBkkmIujKqWtnshxXPWiUXV_i1GsBM2ct_Twyy5zsMTw3JOAko16oSeb_31uk1zlXDSoyWmSR-cdG36-8AcM1YdFTwK1SJG8JfCdxRhLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
باشگاه‌های رکورددار بیشترین بازیکن در رقابت های جام جهانی؛ منچسترسیتی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/22759" target="_blank">📅 12:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22758">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee451d1e8a.mp4?token=Oo9lrWavcUpljtup8Dn9kLA-gHMXNxYJPmr3HvAyO9CtNLofvZoURgm1ezF_1mkjJ0_SkXSf6Veyh8C01OBGT4NkQyKKCtXP7tO7LwFcxR5v9VOWer7hpZM5vQBrKuheuHJfyfC1LPd4EA4JiTQWjhUll0bCVdA6Ld0wU1d-jztzYNExd5ba6HWoNb2oYAXYUcXW1RpWmh4ptCGSCx7wF6p7vLQqyzpxuWN7DtKlEg9pts1YWPMcoIQcYD2MipbfpZbDtojRLhGlh2ZqaVBSWAWxEm5fWzwZQBYEw39EWbf9FIgQODau-0f7zjVqEXQOy5DZ8bBHFwTPIxJ9g2vnSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee451d1e8a.mp4?token=Oo9lrWavcUpljtup8Dn9kLA-gHMXNxYJPmr3HvAyO9CtNLofvZoURgm1ezF_1mkjJ0_SkXSf6Veyh8C01OBGT4NkQyKKCtXP7tO7LwFcxR5v9VOWer7hpZM5vQBrKuheuHJfyfC1LPd4EA4JiTQWjhUll0bCVdA6Ld0wU1d-jztzYNExd5ba6HWoNb2oYAXYUcXW1RpWmh4ptCGSCx7wF6p7vLQqyzpxuWN7DtKlEg9pts1YWPMcoIQcYD2MipbfpZbDtojRLhGlh2ZqaVBSWAWxEm5fWzwZQBYEw39EWbf9FIgQODau-0f7zjVqEXQOy5DZ8bBHFwTPIxJ9g2vnSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
تعدادی‌ازسوپرگل‌های این فصل آردا گولر در رئال مادرید؛ شلیک۶۸متری آردا گولر مقابل الچه، به عنوان بهترین‌گل‌فصل رقابت‌های لالیگا انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/22758" target="_blank">📅 11:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22757">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j9TX1LHEZyjhPgVWJxTZQFdE95nuijtCOhHPKbsU9DdCUd6RKuQFbEN3baogCC26FDuSLDU3puLHzas9Z_pVlwNUDLVzTZH2bFkiR7xncpdb5GRkwZgkMyqyFE7AwiIE23bf3Z43E_QIEdtUyn-UItl6JU0E-qOY-blXR81xi2O5o4WHvigjkyp2_Iaxr-k8miKfjn0egs1qQ377HWWwyQa37jR3HNm2pxYPzeBF9YU9XNQwGEZJq6NXk-iYr-NpkhdBOrrsZDzXnTR1Vkl-xpYVoP3HAqXohAtliJMiHf74W9Xz3cKy2oW1wUG7wgw-4rNEqL_hs3jH_Iag6tcZUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/22757" target="_blank">📅 11:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22756">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CrtF9nQNuU4HSqnZltANiyKGD8hysm0E6SK13uf2mRxbXd2nE84hcwzPd9lnYXviGcnyCNt6FiNWfBYaxQKq9ct9mjEdF7kiNEddARZcMasmZhjWhUBsOVuu2_mguaXsm5m87LiVqotOkIctDSSGAJ8hV4U5oDyUPb6ZVwewkZ4S0QHxUwoTHskUbm61wvmrktrKrM4KmNvu9H77u14ZFvLnhWxJNCKR4oqsvmSZqdjAmTE0guXeqAadO6OTzMJPi6_08LMBQmTBd6rajB8eCwAKWh9hWyvqC14Deap694yG8Vbx0QAf5FDKcedDITROHsOLsLIVYL-xUNEwmmYmJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یادآوری
؛شبکه‌های رایگان پخش جذاب مسابقات جام جهانی 2026 که از 21 خرداد استارت میخوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/22756" target="_blank">📅 10:37 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22755">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QuoioPIeykGZ1hY0jBvs6pwbPjWR3SKXvus1CnMZVKdS7lxUe1uWla8xidf9vFJd_yvE0xmYi-OyP-ongYgoRa-rlYXyBOUkaWwdrUBJlbNuyNGItfouathxSKnZOvQuoIa6TX11mWDxt2_t5jk4ATKIST0wlYWJWun6HAdY2IB_7ryKrZK6tw0lk2NoERcT7iLMHY52XHQGLhISi2lEN2zDW1FGIKBE-RB7k48OOUhcZBlXCLhFURTpNQ0_L35knT_MAEcF6vkBl_bn_dO2yrqFbeVXs_VFmHENy-4ZYhJNp4oxCGylQdfzjx-IQww5YCZFQNXU1JfZTgo1Q6pKJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
دانیال ایری مدافع‌میانی‌ذوب‌آهن‌که دو فصل گذشته بعنوان سرباز در ملوان بازی میکرد قراردادش با گاندو ها به پایان‌رسیده و بعداز جام جهانی بعنوان بازیکن آزاد میتواند راهی باشگاه جدیدش شود. ایری هم از استقلال و پرسپولیس پیشنهاد داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/22755" target="_blank">📅 10:32 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22754">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ede7c22d43.mp4?token=Y_N-WFbDz5rMhy05zygG0rq5Bwe1gv15BE_vxhQdRvTc89_9Y6sEDEFICK1Cuds4_TbmgMAnRhZuf0OpfIKb3Ns2EBGVOuK48h5AXzwOnP1PiFgIZk-1hnx6gWCmtCcaeD4r7GhRpBIImOzNhUe-5EnIwHiGi24j-GkFYA70A2yx9HcUazGQLJoHT2hcpjVq6AGYmxij2CxlcdQt4HczpahEtPAYsXzgLbdxqxjNO0NOiknjBH5XUbpG9q-OrJdPF5d3z2ICeneiEF5B294p9WnGBWZCr82vda2Iz8WvDPCptNrHrQuOaAHBcPohxiZdvwHs22P94GyxYfgEF6FT1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ede7c22d43.mp4?token=Y_N-WFbDz5rMhy05zygG0rq5Bwe1gv15BE_vxhQdRvTc89_9Y6sEDEFICK1Cuds4_TbmgMAnRhZuf0OpfIKb3Ns2EBGVOuK48h5AXzwOnP1PiFgIZk-1hnx6gWCmtCcaeD4r7GhRpBIImOzNhUe-5EnIwHiGi24j-GkFYA70A2yx9HcUazGQLJoHT2hcpjVq6AGYmxij2CxlcdQt4HczpahEtPAYsXzgLbdxqxjNO0NOiknjBH5XUbpG9q-OrJdPF5d3z2ICeneiEF5B294p9WnGBWZCr82vda2Iz8WvDPCptNrHrQuOaAHBcPohxiZdvwHs22P94GyxYfgEF6FT1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
تکل‌فوق‌العاده‌مارکینیوش در فینال چمپونزلیگ ونجات PSG؛
ولی‌واقعا برام باورش سخته که فقط 32 سالشه، فکر میکردم نزدیک 15 20 ساله داریم بازیشو میبینیم حداقل‌تو ذهنم 38 39 سالش بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/22754" target="_blank">📅 10:32 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22753">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔺
بانس‌های فوق خفن مل‌بت
🔺
🫴
100 درصد پاداش اولین واریز
😀
100 درصد بانس یکشنبه ها
🎁
100 درصد بانس چهارشنبه ها
🔹
هر روز 1 چرخش گردونه 1 یورویی
😀
3 درصد باز پرداخت نقدی
😀
بانس شرط رایگان 30 دلاری
🎩
10 درصد باز پرداخت نقدی کازینو
🎆
بانس هدیه روز تولد
💵
و چندین بانس دیگر از جمله بانس خوش‌آمد گویی، بانس شرطبندی طولانی مدت، بانس 1750 یورویی کازینو و...
💰
هنگام ثبت‌نام با وارد کردن کد هدیه Sport100 بانس 100 دلاری رایگان دریافت کنید!
✅
معرفی سایت و اپلیکیشن مل‌بت
💛
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/22753" target="_blank">📅 10:32 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22752">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qUQFJ-9uuCqlLYfPEcp-7EH7zxFYj_7-IXB-5p-RDq9QiI-XBndH0FKOV0OsbLRkVakqKY5NTfFFS5lu8e80XnfSlzwzX2drNg0owNJwICfBtA2UCFvI_b5ccS-i0RhAg5XlRBGzXVtBxIqEGqMl46AnNkaIHkSxb9ZLowuzwfjlJRvCYwTVGMG0XrLA-wA2uR3sgG5CR7198KPLxcfLZ4jnnrMBAxnw7cWl-zu2X96BtYC3GEf9bKxjEjxe67uiouhYScB5l8pWA6gaU9Gs9tFSo6s0ZQX7RArbDhYchOLb37MSYca56aifk382QJ-EDzq1vpBIXDMAE06clzThLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
درسته برزیل از سال ۲۰۰۲ جام جهانی رو نبرده، اما همچنان پادشاهان بی‌چون‌وچرای این مسابقاته و با بیش از ۲۰ امتیاز در صدر جدول کلی قرار داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/22752" target="_blank">📅 09:42 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22751">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gq9drA3_-JPZEsYSdwxL3qTL8kea2eLphzWhfZ23s2hE1BUOEyJrjENNYI2CM4vzICECvEtmdonso37fmcGXZkZf4fxFPfkhi_ksvpw9okdT-gBl7eg5jjChMuIxs7azpo62uem2EJmD83yw_kp1-TPoIt1wwhPFSoLg8dAwDrpY8E55iI3P1cH9YbGEwr5zNnakMWIm7TgUSPazcb3Mgrgs3h5soqOLxURrP2twchX-V3cWh0d-m83WemBgzSQ1uLrjKNu8jjYasaPpHAIII3bUd5-pU86LXHN7CkRqDmUvYL3Q2CJYU4J34aeO21T0ulssNsEbn9fNjmcYcArmsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جوان‌ترین سرمربیان جام جهانی 2026
؛ یولین ناگلزمن آلمانی‌ها با 38 سال سن جوان‌ترین سرمربی حاضر در رقابت‌های جام جهانی 2026 خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/22751" target="_blank">📅 09:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22750">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SwkdIxg0f59jxZg6YPKDgIqo8mil-eEBImWHFiiJzAW1ULQZy5wmZIv-2GuDRRplRA-kKnS52519uvvGv1Ymcpai-c2mQLhoqmAL-e-ZWLGdbRJSSjy74Ud8CL87iuCd0drrM82jmqkvCc3Hpeuv1vbyn-McSBQ5_65wfhGz-f9tmdi37dmM4lIsjWGdp-2sUemd0_HW7mAeLtxODcv23GK0Y3o-MAcnU67qrYdPG2W-495GSMLixpgWjAqpenI4QuQqg0qAitn9j-dYhf2vPgYeExtBn7sdSa86CjcbOF6vOytLKEjZjSxfsupxmgj_hoC6CEYrZ5a2MRGONRnYQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درخصوص نحو سرچ فرکانس شبکه‌های رایگان ماهواره یاهست‌سوال‌زیاد پرسیدین. روپست ریپلای شده کامل ویدیونحو سرچ فرکانس شبکه مدنظر رو توضیح‌دادیم. الان‌این ماهواره‌خودمه شبکه‌ها سرچ‌ کردم مرتب پشت سر هم قرار دادم که هرکدوم رو خواستم سریع پیدا بشه. تموم این شبکه‌ها…</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/22750" target="_blank">📅 09:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22749">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CilKIa6gBOfOsn4eT6AcsU6o2U_tuMnnBRjF0SzEEgsLjFryLOYi7_rZvzl1597fwBWFTtsjgOqC0aX9z0Yz6a4bSD-N78Wrhp0SsXYntV2T2AO-BN770oC-JLpmMYCIoEqOjS2wrkkD1g8DLzkDNSOGr092V0ISJe31AoH3jFfIiBHNnKHWQQRJvb4wKNWOcFD4grruAXlFWbCA03_21y38bmMl8CHwhZ0IGfnpQ1mszxAcLn1wLw5VWZsO_6PacMIEs2MfxKsGhTQhQjQtgcs4tpTeCQC2uCtl9A4Qw1J_6-jp9cmB5ZZZ7ITXKEeGoNz9EfbOmVmaDtR3gxw67A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
فابریزیو رومانو: رئال‌مادرید مستقیما به ریکارو کالافیوری مدافع‌چپ خوش‌اتیه آرسنال تماس گرفته و میخواد این‌بازیکن‌ رو بدرخواست ژوزه مورینیو به خدمت بگیره. احتمال این انتقال‌جذاب‌بسیار بالاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/22749" target="_blank">📅 02:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22748">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qGjRw3DBH7H2HC9DG2o1HWkndOBnT4cZW8ubC9JcfIY8laIykOddyuOggYgtRZ7vNHfmP2h67nEaibM-avl9sxH4X3wIPAVA1pOAsQrRn2AhOi5Yc7DgEDNKdi48p3CspTpb32s6H9M6BYng2eczy6pa45r40jjkwmG_moRwfavuHFaD3vKWAA_Fq4Ae9vIyQTC4C46xRbhCHPnNLzgLProN2RnaRCCKMCEgkjITPbxKUjkay1LrgZoHbLopbehOX1NEDaWP0547_YrOEwum7K2_LlYP8cP426t6uZhXTsDxd0nmCup6tJPtAXLy3dK-JjkXrIVjXSdtjwh6kds0kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رومانو: ابراهیم کوناته و دنزل دامفریس با عقد قرار دادی 4 ساله رسما به رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/22748" target="_blank">📅 01:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22747">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RkddRTOFfKZJpRVUaifUBJNZ1T0wH_wRhnh98fvtwMei960rJG4Jl3IZgBxY3Yu7NAMlGRTeuMNHbx-LxnfCLaLNz-_OS8VYuLJOUHtG2vKAfV_-H1eXbiv9mzZb6gdx8P6YPp_5Oziewgxu3eG1e03Zyr0hJHxVHBq5tWEr47dI48lyeu60cyJmSzjSPvx984OHjSjGWxR-TuK9DaI406U3y2B_UahXd8msyHZdmROyHj0zU208Q4_pyWZTuZ9Zn2u309kwxzQXsuoGybSXD9B83HVE6C7YJ0mNt380anrpKGItx-z20QEvqxeQqu3vK_KpuAMPxz62-z4ApVlF4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ مدافع‌فرانسویی بالاخره به آرزویش رسید؛ ابراهیم کوناته مدافع‌میانی تیم ملی فرانسه با عقد قرار دادی چهار ساله به رئال مادرید پیوست.
‼️
کوناته در ژانویه خیلی تلاش کرد که با لیورپول توافق کنه و راهی رئال‌مادرید بشه که سران باشگاه انگلیسی اجازه ندادند…</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22747" target="_blank">📅 01:27 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22745">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GBGd0x5aMmH-jR78LreyNrA22oYXtBRUVGlTP5su6q6D3Lou20uwxiOKF00S5DgNWjtKsleS26nzW5plc9Vm2SpFC8yFKN0ZHk7ykX6MWnuprHoOy9Ua_vffnCiwV5NaNC58xXR3OuJST-f7Zo3Gg_aFsdFm22Btwe5eHCV4TJmJDOcVLWeQlD89O2n6C7Liy39UPLnl1C38n5CxT2PACeNdemJA2py3BYE7arxr0ULMY0aa5TJExMRjd-wPs3fCLx4aQZkBL0IVLmUPCFRzf1BL_VHpI4oXyE3jiHUk4opTcVtxwmO15F7wFx3VojUz19olej3SJ9-TwPzKKEnegA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a98b9e9ac.mp4?token=NUMh1VysSAv36fy9AvxTbsPebgkXQyBv4J5crUz1VSTNXzeeO6Jl1XgcKE8To8mxA4GNhMYaQSdJcQXLlRKDparAu5JDg3eC5avkgLY7wEmY60lbNUiESukpjgFowX87LNefNQ5LjdOf4TLYs1TzBu_9YuzxVMXcXXwEhX-_w8239zXuXN5usTgBKDFvshUryaZGlMpY_prUgej3fwOrJ1RpwsCb8tJPrfF9QLzrY4N75wBTs_ND9eE1n-U8LFjTUmbtkCvOQNdcW-_iR3kQwHJ8lgkAd-lvqoHopxxiTE4V79NnR-Pc4bAYz-9YqIQOoMnif7JnUSjiU2lPicuysw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a98b9e9ac.mp4?token=NUMh1VysSAv36fy9AvxTbsPebgkXQyBv4J5crUz1VSTNXzeeO6Jl1XgcKE8To8mxA4GNhMYaQSdJcQXLlRKDparAu5JDg3eC5avkgLY7wEmY60lbNUiESukpjgFowX87LNefNQ5LjdOf4TLYs1TzBu_9YuzxVMXcXXwEhX-_w8239zXuXN5usTgBKDFvshUryaZGlMpY_prUgej3fwOrJ1RpwsCb8tJPrfF9QLzrY4N75wBTs_ND9eE1n-U8LFjTUmbtkCvOQNdcW-_iR3kQwHJ8lgkAd-lvqoHopxxiTE4V79NnR-Pc4bAYz-9YqIQOoMnif7JnUSjiU2lPicuysw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
#تکمیلی؛ انریکه ریکلمه: درقرارداد ارلینگ هالند با منچستر سیتی بند فسخی وجود داره که بلافاصله بعداز انتخاب‌شدنم‌بعنوان رئیس باشگاه اون رو فعال میکنم. به تموم‌رئالی‌ها قول میدم رئیس بشم هالند و رودری دوستاره سیتی روبلافاصله رئالی خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/22745" target="_blank">📅 01:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22744">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BKGRhkB_0rt6M3WgGKlA6RbNVo1DnuMqTPaXxkUCdb8xpN1kiMG0E9FmQKfXSZr2WXa85ITemCDchIbEOUYAkDbmOmxLi8i8lkCT78g9hqHSVkPB0DgSgBeu-bZGMeO7ptlc55smxH2Vxny7bk8W2vt6vCTQ3S6RdP5tfHXTqmeOyHzS-3_wfPyTUgNWb8eGFl_3XnbV2sQIXJsBgm76o882DSj7rJZg0j_a-GAopI1cb5GO_uzU_Azgx4QFY1oI9lEm8j9AJl12zol7SRgP8hKSmYQyol_owiYCPCVT9_vALM-JmQvfOZ9x14VTKEsivJEpSLx99LO5cSwfYXE6Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ انریکه ریکلمه: درقرارداد ارلینگ هالند با منچستر سیتی بند فسخی وجود داره که بلافاصله بعداز انتخاب‌شدنم‌بعنوان رئیس باشگاه اون رو فعال میکنم. به تموم‌رئالی‌ها قول میدم رئیس بشم هالند و رودری دوستاره سیتی روبلافاصله رئالی خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/22744" target="_blank">📅 01:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22742">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sf_sWyElhR1pRQP0iPu0gz6ELGklkAM1rpzP1zQ4Dp4td9pn5zvao1Jv1jtwXguC6rYGd_ECiduCLMC1_d3VUpVzsm1wJitTfzo-kdNgMs3vjzsoXsNjr9pkGH1ovFtS3EHw1f6B1yTvv5991pOm62fkI7tHBRwzlx6JUKFogFeonSD2VQg6N2WygiD3FgP0DID-XSZoeqBiReM13LEVMa1-QT0M4nfAEX9sa6sn_Ub2f7w9IcKUf6LGx2zjjhHyrBCiEdjpEU2_RdxliJMPjWTSCSEda7KXNiW6mO07uPI4OKDpdJU_ojfYDP6JSrAjdtZxuK4qZOASOnMt7m3aHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارهای‌‌امروز؛
از بازی تیم امیر قلعه‌نویی با مالی تا مصاف عراقی‌ها با تیم دوم رنکینگ فیفا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/22742" target="_blank">📅 01:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22741">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mnQtnFkA7q0KtUDDKbtbKodgZXINTRNit833hvRTmwQ7vuQ3S9Rt6d4HWnIM1goOf2_0Lt75_RLsQT-VMZ8OmGb9MmImmFFRUDRP7zgvgsLgSMZcwwujE1fLPoBy2UhTwX-PiMmPIDj9RxPXMr7YrbFOkr06TEUJUDOiTVxkJn_QwB3FxCpVTShlfIsKDbznkpfno_76Cio2ni1FuYbH069CeKvF5uF4XPjRYUyz1k6keKTROMgCBWMeGMr1D5ZkpCXCy2mvRTSI7FNaWm2JfUp3AMUIo-vzJDzLK11h0KNICH-jL-0eGzyLURRljiJ4OG7IVA38lzqtDdJHw7jCHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نتایج‌‌دیدارهای‌دیروز؛
شکست سنگین نیوزیلند پیش از آغاز جام جهانی 2026 و باخت غیرمنتظره شاگردان کومان در دیداری دوستانه برابر الجزایر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/22741" target="_blank">📅 01:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22740">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nDf0AtJg674_ZlpLvFAZ8zP2tGXdHVaSaMwUYTEcY4ktB3_EQWxjrwVc8LOEeKwSgfo92RIbfoQkvOakdlGqKpDoCrS62Tw1o6C0bJjM1MJTAf9d8ouI6qDZa0RbrKBmCnjOC2D9qW-WvelzDErtt2oYWD108nqvW-4z6b8wZN-5nwVarwHVArDlBZNz1IaCnvRo-iOElTairIfAurzaP_NIkPVwflQ1ZcCOLAS9wvUNHSoMTGoeZ87HGQyDlWNvsVLkQ7ZqcjACgiR_9cxkA1FLi2HN0_RK8uQKSLDVMiXfxWJ_v9xCLVRsEtM-37gdHIx047qsM7nRvaaN38DulQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛انریکه ریکلمه رقیب انتخاباتی پرز: اگه در انتخابات باشگاه پیروز شوم قول میدهم 72 ساعت بعدش با ارلینگ هالند قراردادی 5 ساله امضا خواهم کرد و فوق ستاره رو به برنابئو خواهم اورد.
‼️
همچنین‌سرمربی‌مدنظر من مورینیو نخواهد بود‌. همان مربی خواهد بود که همه…</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/22740" target="_blank">📅 01:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22739">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVTE_Theq1QOzNmBPBdVI5IXVcDexaBrrVdD4gUjjr05U_1rPXNqpG4wtWwLSmA77gy24h7_nXtGtpMFS68maEZM1_Z1FmMOasxqjH47NWEra_kwKHPFYiSqJjHzw8SmyvZrgLeSPwX9-9Ig9Y5VXLIx9PAdHiZqPYUkRz67Yrxv2FMuWdOeKrqZHt8floyDs6N1c4fpy95Wntzz98TCa_Y9an3HczvG5H7n49I0qyEqprB6yrO6UAy70LRC9bDsBrG4gwdGA4YR56XtmQ9RqGSmT6cLS0YnYCQHcUzDzkv46ntKlfGsEVT66za3Dt3O9daaxiDSmYhnaOLcZ6E-AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛انریکه ریکلمه رقیب انتخاباتی پرز: اگه در انتخابات باشگاه پیروز شوم قول میدهم 72 ساعت بعدش با ارلینگ هالند قراردادی 5 ساله امضا خواهم کرد و فوق ستاره رو به برنابئو خواهم اورد.
‼️
همچنین‌سرمربی‌مدنظر من مورینیو نخواهد بود‌. همان مربی خواهد بود که همه…</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/22739" target="_blank">📅 01:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22737">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSajpBL8zvO53DSsc-2UWIiIx2gJ5wCwzhlnrvHvJhKofOW3tw85Iv0adTQDTc4hOceHTzPNTPT57lrvTNX2I75Mr4a9kNxbh-m51_PMYJEpWVouwVLpmLUK7V6VSx5F_lfV8jZmi_62yf3Y-0zLJuZy9B1MaqgPbnB2-fAsrCZyZ7Lx6MJ7Xnmi3oxNMYX65_6sbaMl07K92Cyp_vssLIMlMqVh33KZ5Qti70IES-diGgco50isufyUJS-UsnbLCEQkRNs7jOcN-na6-6ShOl4d-JkrsC3crC8tewj2u8ny5i4RRp3bvLHMMUtICHKtU3tIt8zYysRE5kjIo75mFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ 2+1 رونمایی رسمی باشگاه رئال مادرید درصورت‌پیروزی پرز درانتخابات روز یکشنبه هفته آینده. بجز این سه نفر پرز به آقای خاص قول داده بزودی چهار ستاره دیگر جذب خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/22737" target="_blank">📅 00:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22736">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1314be179f.mp4?token=CoUjP7TugGMsDo8Eg5I9TWSqOai400VXyscivUPlfI-ytZNtxqchRU7AlJRAcjvgW-l8gIx5Z2C6OhJoP0AsfUL8UGc6M47LJI4xHRPXSp45lFhh4kxQjpUITTQGrdNf04b0GI-LeRHUrJqNryQMF7I1fas5W1sh8uEud88Jxml006XrDthSVXDNQYYvmnW3yvsOBVYhFjDVDmsB2vNrhoV8B4-b7TjyzMrPP4JZhEEjOl9Yi5rNzkzk3CrDri60zs5gnbL2ngO4Sb4iowevghv4tIH5Mbt5dviCnD9KLZA-ty44fBtl97P3NMRXUDu6LmjQmFGjOL1rKWGet5ThRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1314be179f.mp4?token=CoUjP7TugGMsDo8Eg5I9TWSqOai400VXyscivUPlfI-ytZNtxqchRU7AlJRAcjvgW-l8gIx5Z2C6OhJoP0AsfUL8UGc6M47LJI4xHRPXSp45lFhh4kxQjpUITTQGrdNf04b0GI-LeRHUrJqNryQMF7I1fas5W1sh8uEud88Jxml006XrDthSVXDNQYYvmnW3yvsOBVYhFjDVDmsB2vNrhoV8B4-b7TjyzMrPP4JZhEEjOl9Yi5rNzkzk3CrDri60zs5gnbL2ngO4Sb4iowevghv4tIH5Mbt5dviCnD9KLZA-ty44fBtl97P3NMRXUDu6LmjQmFGjOL1rKWGet5ThRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
اسطوره‌آبی‌ها50ساله‌شد
؛فرهادمجیدی ستاره و سرمربی سابق‌استقلال وارد دهه 50 زندگی‌اش شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/22736" target="_blank">📅 00:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22735">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d55442a50f.mp4?token=SpWdmE_e6-8KOwPSpKcpHNNRu8It3jwdw8FxjGcuQkK0IqNi-Ct0kiDiaUY2UZREO8yYb_ZDAQYk8ZDXsNeYujzjXID3atAIPwWoW5NaRDi6rH13WdFABJoNsCZRQ8SJts8XEIUGGGlb4x_SMj3ddWD7Gt-8cJtT_FYpCp2jV7iZndiiF7fUoQSASuVqhve-JfYH5i0KkoNgVQix7cl-vn1mA-lIppfmQU5xjZ71r2SwXv6lv7BLzERKTI0nLuokcWFZFRKYMm1GaF7xUFMYdhaosXasts9loHd9Q1YEqWeyde7aNTGfqxihJPCptjcn0hbK-YvzrMJ321euGIyotzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d55442a50f.mp4?token=SpWdmE_e6-8KOwPSpKcpHNNRu8It3jwdw8FxjGcuQkK0IqNi-Ct0kiDiaUY2UZREO8yYb_ZDAQYk8ZDXsNeYujzjXID3atAIPwWoW5NaRDi6rH13WdFABJoNsCZRQ8SJts8XEIUGGGlb4x_SMj3ddWD7Gt-8cJtT_FYpCp2jV7iZndiiF7fUoQSASuVqhve-JfYH5i0KkoNgVQix7cl-vn1mA-lIppfmQU5xjZ71r2SwXv6lv7BLzERKTI0nLuokcWFZFRKYMm1GaF7xUFMYdhaosXasts9loHd9Q1YEqWeyde7aNTGfqxihJPCptjcn0hbK-YvzrMJ321euGIyotzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
پیروزقربانی سرمربی‌فجرسپاسی:
امیر تتلو یک اهنگ داره اول تااخرش فحشه ولی خیلی خوبه. قبل هر بازی مهمی اونو چند بار برای خودم پخش میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/22735" target="_blank">📅 00:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22734">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xci6uHptbsE3Po2XkI99AwNB_zNQNh6Ho2CyooeIMFD7FpE3i_E92zdZN_BKtNiGLMOfYch8gz7ernrqdQIDlzyUU1uxqEmGfrr3t89XhF2yzw9kbRlZjzYgDClLQRv0tP7iRgyVX7LbE2bQhu5cci1Zo4VSLb6WqxcY9qjlEbkdSyfkKWUQee6Fbi5qBRz28H1CTBZeZ7ZpOCV3-rug_jNZ8QO47NZskcMw44vH9exyqvTrQw_mMWZDOknSxet5yvJ7QhI7lrcEZsxe4dG3zijcD9MkTSq2WCjOfbQRSOptyJQvmpMhfE9DRSHgRl8Qrj7FmDKK2MSIX5pPw4PiNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فکت‌های جالب از جام جهانی 2026:
1️⃣
۲۲ قهرمان جام‌ دراین دوره حضور دارند. حضور ۴۴۹ تیم‌مختلف‌از ۷۱ کشور جهان. ۳۵۷ بازیکن حداقل در یک دوره از جام جهانی‌های گذشته بازی کرده‌اند.
2️⃣
۸۹۱ بازیکن برای اولین بار حضور در جام جهانی را تجربه می‌کنند.»جوان‌ترین‌بازیکن: خیلبرتو مورا از مکزیک با ۱۷سال و ۲۴۰ روز سن.»«مسن‌ترین بازیکن: کریگ گوردون از اسکاتلند با ۴۳ سال و ۱۶۲ روز سن.
3️⃣
کشورهای کیپ‌ورد، جمهوری دموکراتیک کنگو، ساحل‌عاج،کوراسائو،سنگال و اروگوئه هیچ بازیکنی ازلیگ داخلی‌شان دعوت نشده است.» «۷ بازیکن با سن ۴۰ سال یا بالاتر.» «۲۲ بازیکن زیر ۲۰ سال.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/22734" target="_blank">📅 23:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22733">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dqOwZMFsbcqSPaEFYPRme8KZZguG45mRI5NI4Q7qP2XVlerYt9BWFGSrDoeEektynG5LKWfoy3uEvveoKOqjT_VmRfgas_t5RL9fZyQgeIrgR7BZw26xDzoQxM0-e1McUz8o3MhmUFjQ_G3hFoXw2Hxi9ClbzIMfIwsx9K-BtA621qSo6BClDFf-BR9pwULD7NvLrDzoE-NhNPrar-vNHv3YVIAb2TJBug0tHWYSqgISVxxu5cQOQojUHI-3uT-lCsD5ZmE0ZD4U_DYIpRSGDoI5thuhzQlOg-dT86CM5t_ZSgj-6S3YiKi3X78U3OY67Qw2xaoiEpOhKMiyQK18dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
قرارداد دنزل دامفریس با باشگاه رئال مادرید تا سال 2030 خواهد بود. او ساعاتی قبل تست های پزشکی باشگاه رئال مادرید رو با موفقیت گذرونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/22733" target="_blank">📅 23:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22732">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZ1UMoA7WWzJoclb20TJe59oWbgUwgqXu_rrJ27n_3TTBG_sJ5U0fFaUvmLTLQg-ljrxjkhq6kOJt305dN66XDdDDjN2Lb0EIHkFlI9seTBR9lZpdoKHV8KK56wAH8Zj2BzKZ5z8vxKhdtXP5M2jAUZJRp8KDMHtwpc7ukxMz5_hf8n_uW2RlXEnN2Xip4avQi46xE0X8U03zI9VQVWoFEW5x5rMoznOE-EidPO9NW-EowxFqmbQW8k1bQOK9GwgRaf2JqK-reTHoQPrQA5XOkCAw6zyPow9j9d3dZzntwQhS1RyrgdgJyF2ybfwowEgl9MNuQRdExNCdOeniVjHVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ دنزل دامفریس مدافع راست جدید رئال مادرید بزودی در تست‌های پزشکی کهکشانی‌ ها شرکت خواهد کرد و سپس باشگاه به شکل رسمی از او رونمایی خواهد کرد. رئال هم همچون بارسا خرید های پر تعدادی خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/22732" target="_blank">📅 23:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22731">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dddc4505bc.mp4?token=LejH2S7DxU21YzoO7T_wXvkLCkdUcD9agdw9CXbfMhM8JQ7A8CZc9PAeIlJlXVBeKGpbpeEWVHg1taDno0e05IcIn9w8ovhYivzgl4v4TPxQogwnUKtlrggaFjiqWge7tEIuR9IoXPk377k0jpRmjdFh7u5VqswaT39WMvkRyFz14nGZkzJxwRZ-sTBETKuOIRgb76TWiIsWYa8wwME1qOo3am71m6vmYl-Fx72EFoeB4d3xy33bCtad3GtjWE4tdEVygwP4AsDr0u0VBtgzcGpduWFxAAnyO5Dj01vejo2kORaIa-a9A7YhAqpVLRlHyvHNO53bhKki9WHCQsxW6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dddc4505bc.mp4?token=LejH2S7DxU21YzoO7T_wXvkLCkdUcD9agdw9CXbfMhM8JQ7A8CZc9PAeIlJlXVBeKGpbpeEWVHg1taDno0e05IcIn9w8ovhYivzgl4v4TPxQogwnUKtlrggaFjiqWge7tEIuR9IoXPk377k0jpRmjdFh7u5VqswaT39WMvkRyFz14nGZkzJxwRZ-sTBETKuOIRgb76TWiIsWYa8wwME1qOo3am71m6vmYl-Fx72EFoeB4d3xy33bCtad3GtjWE4tdEVygwP4AsDr0u0VBtgzcGpduWFxAAnyO5Dj01vejo2kORaIa-a9A7YhAqpVLRlHyvHNO53bhKki9WHCQsxW6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ژائو نوس ستاره‌تیم‌ملی‌پرتغال و باشگاه PSG که در 21 سالگی‌فوتبالیست‌حرفه‌ایه، 2 بار قهرمان UCL شده، میلیونره و با دختری که عاشقشه زندگی میکنه؛ برادر در داخل و بیرون زمین زندگی رو کاملا برده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/22731" target="_blank">📅 23:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22730">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cw0GaQCfnCWbSXSQlDRGHUbtKG4qbaIQ16kUx83ZMXbUkPy5w3AfVRWvN5iDeJ85Stp0qfyK9KLesnhpUtbCkGDOCAgjOLqiC8xBXw8LCTLt08tzI7BsnlWRhSVnnbjZFphtOpKH_lqwh-B85_O-FvoYJ6pJMOt72Xj5K7cy51Fyon5Unjramy9G-10eqz3m-_7w7cOTMJEgR4zauhgqlJB386Il2oSPYF7KJ6Wn_PLBMCSY7v-zUv9Kk56YnnDbX2w2FogXY6DkvHPkissjYltI49V3wzqFef37JR3rvBHmyYHc6062-retV4tXhnCnpxLgDNEkLFB0X1sdZz1iXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تغییرات‌جدید در‌قوانین‌فوتبال برای جام‌جهانی:
برای اوت و ضربه دروازه، شمارش معکوس 5 ثانیه‌ ای در نظر گرفته می‌شه. بازیکنانی که موقع درگیری دهانشون رو بپوشونن با کارت قرمز جریمه میشن.
تیم‌هایی که در اعتراض زمین‌مسابقه رو ترک کنن، با مجازات روبه‌رو میشن. بازیکنان مصدوم باید حداقل یک دقیقه بیرون از زمین تحت درمان قرار بگیرن.
وار اجازه داره که خطاهای رخ داده قبل از شروع مجدد بازی روی ضربات ایستگاهی رو بررسی کنه. VAR همچنین اجازه داره کارت زرد دوم اشتباه و تصمیمات نادرست مربوط به کرنرها رو اصلاح کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/22730" target="_blank">📅 22:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22729">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1UXpNL5ETVGWLK-khP4LIgMj50JgfJSsP-Yo_OySheQMpihjwTNIHPCxAr1LFfEbBNnrxbrokh722Kh70x3T-6v9en0uL3zA0uYN3-SohBRjHXR9lEWzQIv9QYs18EroY7QEBYR2dUVDBppsw3qxKwbhWiSPnr4ueFpraRRKmrVgirMhW7yr8VKGgclLEjWBfrd-HfyH9Sh4pE_fN7j5s1Q52lj1vdnF0EF_XXxF54A_DOexRnI6Mi6-9O1WF6hTaAve7UPStlLLuzLIEnh8xwn1i08oUTq93qusWa2258DJ4hQKMvUcDT8en0FcFIC6x6x3je57gyxhSaw-HZLdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برسی دوپیشنهاد برناردو سیلوا ستاره پرتغالی:
🇪🇸
اتلتیکومادرید: تا سال 2029؛ سالانه 18M€
🇪🇸
بارسلونا: تا سال 2028؛ سالانه 8M€
‼️
ستاره تیم‌ملی پرتغال آفر بارسلونا رو قبول کرده و بزودی این انتقال به شکل رسمی انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/22729" target="_blank">📅 22:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22727">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SsvVXh2hmd_S-ptchd1SiX2MOfCf4HqwSu8e0NzZLV0ZnoNgGpRG72hnTmfjJXB_2ubxE2l_N1Q_YBSNba9gZv4vH_VvVthhX0uMH6ZIPVbUvWAQVOEzXlh-BVgA6ACE3n7j9V1I68O1jpaTecn6rZ8FDPBvsUOzlqZjRcK_vjks_jPMPlcab7nFROdr_MCQJBvCPSIx9pp1XxcfXZDZNwRQC7Mlhqmpdg8YscB-5RcG53m1yoOcylGQUP8Gsjv1vyqaHiu6r0QQ7ZNqK5vzjqGlLq5nc3QPZXzVC4knUOa7aOIPYwt06y-DCqQ1t0cxjTOKmN2Lp4PhfAxpVn9T5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ دنزل دامفریس مدافع راست جدید رئال مادرید بزودی در تست‌های پزشکی کهکشانی‌ ها شرکت خواهد کرد و سپس باشگاه به شکل رسمی از او رونمایی خواهد کرد. رئال هم همچون بارسا خرید های پر تعدادی خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/22727" target="_blank">📅 21:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22726">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZSrQl6qdg8HO2-Fbp28Vuh8y8TVql6Pb7fcCmpRs8MyZgeIkUHyFEtQSZZrocaah_65yg02bovPw3sg0RGL4gDAfxLCvJVpRtNEDELEL-Tb_7wT-ZG9ZPtsa1b37S6TwnpfBLTtnhiDwFwW38CEn5AlFTZm8SpKGfriaD3KyNpYPV4p-BEfenCWUMGz3J8YIHsTBuHXjTBaKFhiV9_omIR0GJa6hP0nqWoRbAu9uqE8quLqH1VJVvMlo3Z7OtKJ1RHdq_NX7xV3FOGyZCLQiYbqSpRYxPYf86ZTk9qhtryDz1yxeyH2D3DuWvvLAZnBAfUwj8Cw8F5yz1jcjqAWITw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
طبق داده‌های سوفا‌اسکور، دیگو مارادونا در مجموع ادوارجام‌جهانی باکسب نمره ۹ در سال ۱۹۸۶ رکورددار تاریخ‌شده و‌ تاامروز هیچ بازیکنی نتونسته دریک‌دوره‌ازمسابقات چنین نمره‌ای رو بدست بیاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/22726" target="_blank">📅 21:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22725">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQj_38aKx3H8VeSuqcehl55YdfyRC9j7KtKuNugXk1Gdg2p4sQgk-o5Ak9D0V0MmapW1B96vMK0td6lohluYEZ60sEnRXePid9_Gc7StoAd1kQc-kSubqHhRfLn2C35065jViBMEjloQMCmxu2OeMLbHQfw_N-dp7AYtO686zfRo0YDy0nL18OfQMmT7ivQHMPp2SuNsVUO-ixf3i05L67b4Jo3Pvihal5BUKzhEz1AWtfjV-tBVIMa0ZSIaUNoAj7GY3v1QdKRMgfWgjYtibg7gOLcZd7ElD2pnAlFvM3ecHe1Mx0vRyslUMR9eKnh8WD-XgEjj1CIUN6HTTfjLXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دیوید اورنشتاین خبرنگار معتبر انگلیسی: دنزل دامفریس به احتمال‌بسیارزیاد بعداز انتخابات ریاست باشگاه رئال‌مادرید باسران این باشگاه مذاکرات نهایی رو انجام خواهد داد و راهی این تیم خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/22725" target="_blank">📅 21:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22724">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">توپ ترایوندا آدیداس یکی از پیشرفته‌ترین توپ‌های دنیاست که فیفا برای جام جهانی ۲۰۲۶ انتخاب کرده. این توپ میتواند در هر ثانیه ۵۰۰ بار سرعت، جهت و چرخش توپ رامحاسبه‌کند و داده‌های خود را با اتاق VAR به اشتراک بگذارد.آدیداس‌معتقداست این توپ می‌تواند بادقت میلی‌متری و زودتراز داوران آفساید را تشخیص دهد و به سیستم تشخیص آفساید نیمه خودکار کمک شایانی کند. این توپ بدون سنسور در فروشگاه آدیداس با قیمت ۱۵۰ دلار بفروش میرسد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/22724" target="_blank">📅 21:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22722">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FbnztysLE0eqz1R6T0XXVK9u4tTzYPZB-iLww-R8m1cg9b02ZwULSRwz9ReJKnXeTJuCvQysZQwKF0or1_fKSDVDtbMWnmkGX3vHHPwPXuicCwjcPrrSxKAiPNVNt6Z82ppsBwGsCrpj18eGJOxPrx5YKNNV0UDc65LNDXzctpTt9-ok_8gmPS8sD_CHi5WVLzEw3P4Cq7iBhrzsdINCn5d3_NF2JVXBbDGeT8ZahpHSOfcEujGF76SVjQBvkM6cdDKWE3qBNb5P4k8rbAp4S-xHV926khT4vQmqXAvIyMAVB-PZJ9Yu8J3-8GyVOczt-g149HJTf-REfoQM2GLi2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
لوئیز فیگو اسطوره‌پرتغال:به‌جرات‌میتونم بگم که اسکواد این دوره تیم‌ملی‌پرتغال خوشبختانه‌ یکی از بهترین اسکواد های تاریخه که امیدوارم با کریس رونالدو بتونند به قهرمانی جام جهانی برسند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/22722" target="_blank">📅 20:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22721">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eQZRpF2pVKaBVcj0Y98BTKd6G9IArZanHxxHpbvbTdGhHDZ-C9suB6hHPmNnxpRnUfvGYOeC0QNWJ4KVxn3Xa-EDaPl-QTdqZSY0oIj18WvMyjFsT-qvrbPY5knK5jLhAb1JY1HqHH2AlV97beESrWCIdIk1KIGMd-NcZu2GO_ayKxK4QCOzBLmzchZ3Mh9TOv0H_4RLEwiGJa9WBGk8zaXHfb88fSRKb3_awGgpay7RV9YLrnNKw9A7EFXpM2tsI0evF3V9jUyGysEZtS6rdqRHUpMonrDtycMW_k6j8T9od8Cu1uT_QZXkveT-4RdY6HeIsxqJlux7BIKyfWf09w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
#تکمیلی؛اتلتیک:انزو فرناندز ستاره چلسی به سران این باشگاه خبر داده که قطعی میخواهد در این تابستون از این تیم جدا شه و راهی رئال مادرید بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/22721" target="_blank">📅 19:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22720">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lkWHClLvK8atJeGXIepnsWRa0QbiFXWNvrLriGC9Rirq9ZZs8Na8YDZdSj93Hn7EPly7uzvA9n32n4kAxCjKO90Q1t3HsLXBsmVe52znOxjcV7Ldhu1bmWiYKlUhCeuZj6HV5DTtbBZ6eLkTKWpLeN7R-G31iY0t3DW0afQfhEVoz4XBlqdSC6_xEnWJOKSjEPqXvqDFPuUCPgyvEucLt_4SqgHGeOjpLRsmUphb-RfzUwQX0FYA56kzy5QYiJJ_Zq3ghQT7m3mOBxhX6lWiXZKb-7f8LhzCcGOtb27SedbY9NTOiOQii6TlAfcSFta_BUcyO_3i0hQNZ3WgfwfiiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌آمارمثلث‌هجومی PSG فصل 2025/26 و آمار لیونل مسی به تنهایی در فصل 2014/15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/22720" target="_blank">📅 19:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22719">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YfAi7o3uU0NmFelfShZCPVmoKcttIN1QN171_neG7YIHx1DBzy9MXwkwy18eqweRuKb33BaO0CJjzfDnb5qqmsdpu3Liq6PDLW0WlmYz6A5spbzEgLuvkNQz6IpCo2SoplF7mJnKNkH-Sov70iL9h2KNEDcsMg8kiVMSSG5Os4-yEdcrkcL0EGAyJzwKhlHAi_lOj7pbYU1caochGrkv7RRYekx-Xw4GtvxPJigjF_YJULKGro_EGye5rEJsd5FTsqbr83Md1PBmMvkk2D2izVVEYSlZUB7pj7tLFYJa7IO0CFryGazBqpZLBZY5xuY1H-A8gjpM2g5lE-JcbIASjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
#تکمیلی؛ بافعال کردن‌ بند تمدید قرارداد اوسمار برای فصل‌بعد؛ باشگاه پرسپولیس به بازیکنان این تیم پیغام رساند که هر بازیکنی که قصد کم کاری داشته باشد قطعا در پایان فصل از جمع سرخ‌ها جدا خواهد شد. ضمن اینکه تا این لحظه جدایی عالیشاه، رفیعی و پور علی گنجی…</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22719" target="_blank">📅 18:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22718">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BoHHpFOvYANK0i6S4OB9C5xYiAhIFULLOF1C5SfW0KZp7RvE5iX0wGPBRfOGHTQa6Vtqx0_L59W5CFOfH4yJkAJU3hr-eVkxDEtdqA9dqIwvMBshr0QXGmnOW-wfqajID1zAMBbMexqVwAnOmtGr_pix_InNZykqpOPNYHvM8HkYUJaMfo97r0ONabha3dJfm0c0tmfaZ1ndoH7Awjo-iJLvrPZ95fI9dbl8SmkA4aeuurLfbdPP3VdaMOgETjp5ZozD6TS_hsJ5R_-tsZ5lmq8yRTBy6lLc3TZFZeA_4iH0LPtc0gU4XTHr6XP9VjUvNAQ-CUvnInmtX48Mcw86_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات
|با اعلام رومانو؛ دوشان ولاهوویچ از باشگاه یوونتوس جدا شد و قراردادش تمدید نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/22718" target="_blank">📅 18:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22717">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PhprZP4D9wUbFTX4Po5RLKmGZCa0cnmLe1QEJrGY_LhNO79UKK3s7DFGBHXxQaRdegeUh7DYYfCIsl_n9PTszch8eMDZQ7AUnURnXS8tvFkvUxRg_cOxrBZf6kTaOZA1ut2dx3BBVnnupAXuzJTj663W-vfsUcly1SEG1438BoPTo5gTwg0NqYwrrzaIav0B6iyH5HbD1yzcAyhClX3t4Abwl3lqCuzwdeZVH8YWlNoGiFK1JtIK0zRBcTjXhLCFjfG1TfdZWRqTpqyJCsnkaFoprVngU0ZGKRtXL2cOzrv1r2wDRCKpdjL_kf7F0EgYU2dmtorCWstFVTVC-CndbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اسپورت عراق با انتشار این پوستر؛ خبر از عقد قرارداد دو ساله یحیی گلمحمدی با دهوک عراق طی ساعات آینده داد. هنوز قرارداد رسمی امضا نشده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/22717" target="_blank">📅 17:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22715">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WXbVZrIMyW5HcTq3RKaIyUzItDlvIR1j2nTCzGk6NRyI7uY_aiddRzmwOI8MQ1nk3YGzvdquCvdXTldgcFMiwS0ge7LtdMinPxRldZjb1FEZc9I37gXmEkbyb5lOSCO36SFqtiK9pEc51c4G4kHtgd_SUbtyF_o3LfGRVR_JFrPD7ZJC2nn27WYx330u1egK3wUeIEO7PloL0u9icjsCb9-BAETE4O96Q1byv38sX8GKIEVFEBBP0RLNerwAn3aghptiiHFdN6LUSH2ewRwvPmIAi2WaQmf302K5xp7xc3j0m85U_FLZHnZwLVvbIckQ_8GU5SbTsS9d6aYtacXS_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y7Azr9W4Zb7MPkRXoUG7CBVy8HPq00i79OTNJ7Ea17JEfEcr-B1PyuMohSU4HKk4wsVlw5ci3Z6JX_ixHCHCUU5YXGoBo-hZC40BNVfsGvNCKm-Dpty6Fp2T4wJXRB-knkRM8J-VGTSF8V5NuU8rjGKo0mAbmPA6OFSkZUuSy_zULSvSl_F0KusZLNNi0kLA2lWxffq4X514v8wE28aYFRlzCDMfMX2Djo-Q9xFNJXXyCsgNrXmT99RKLadU385lmZ472W_8YDVUaivS2WkZHQuYp57eCHgSqu4YLgSllIDjKL1hKGOXXmIYgTjKQYzK-sVhcQEHZNXx3UVSgSRqiQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇿
🇮🇷
ترکیب احتمالی تیم ملی ازبکستان و تیم جمهوری اسلامی برای رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22715" target="_blank">📅 17:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22714">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e93182b0f.mp4?token=HrVr07VxbTOTnGOeQFygHMKFpcrza4Ue_q6DKwWnV4iyzSb4kDjHEUTNHcLvK1W9WrPR99sxROz2RTnI2ddJXja8uJQXE4aSKXRsym_edBcV4MgGgkYqixdH68qQTdVUfubWExQ2Q8X4CVnt3rt_-lgtViUWxTZejJJ7aLjjBXzcRc7Ai014OxDLXsk4cqdg_LLj-gSolQAxFMhq1PFEvIGD9hVbnhJ88Es-sfOMuCO9HanxbRMnl8ypaddkPhXr7kiY9WiyF7gbe-zQ5Q07SNfVdwCmwfVhtS1duJAozmQRZOe_xdwNcFFw3Y_HBEw4p0tJXWEZrlTthA18_rwyKYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e93182b0f.mp4?token=HrVr07VxbTOTnGOeQFygHMKFpcrza4Ue_q6DKwWnV4iyzSb4kDjHEUTNHcLvK1W9WrPR99sxROz2RTnI2ddJXja8uJQXE4aSKXRsym_edBcV4MgGgkYqixdH68qQTdVUfubWExQ2Q8X4CVnt3rt_-lgtViUWxTZejJJ7aLjjBXzcRc7Ai014OxDLXsk4cqdg_LLj-gSolQAxFMhq1PFEvIGD9hVbnhJ88Es-sfOMuCO9HanxbRMnl8ypaddkPhXr7kiY9WiyF7gbe-zQ5Q07SNfVdwCmwfVhtS1duJAozmQRZOe_xdwNcFFw3Y_HBEw4p0tJXWEZrlTthA18_rwyKYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌ازشوت‌های فوق تماشایی گرت بیل فوق ستاره سابق رئال مادرید در دوران حضور در تاتنهام
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/22714" target="_blank">📅 17:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22713">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJ7dMH4VpOkFM2uoZ2kecSx6O2TWGDVr8xD8bkDs4CFPBMMpbPIBBAh3SqV6Ib1xzPKkV4L0Cpd-wzZ996fT3_aH-qnfeO4t6eOTFbSX3mTKWWcrQsEPknyRPPM-BYTDu9Sb6WN4q6t7McBQ-M69rYw0asMTagehNQ9Tzb19__wpBN6S_5KypZVopCm27e-gACCchruz-j9LUPhEh9xaKiJH3vnLmv8CgTAmYFV6KPTECY0MJs3HUSE__H_5f3rImggDI5ZqpSzCa8VoSqXjuANL8wRFkDpcI2GXw_xFxoOPnyCRq27LDzGK-aZ7Fzs0X7H5dcP2UmEwE6GvnbFt3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق شنیده های رسانه پرشیانا؛ یحیی گلمحمدی در روز های گذشته مذاکرات مثبتی رو با باشگاه عراقی خواهانش‌ داشته و حتی توافقات لازم بین طرفین انجام شده اما منتظره تا تکلیف نیمکت پرسپولیس برای فصل بعد رقابت ها رسما مشخص شودتا درصورتیکی بنا به‌هردلیلی‌اوسمار از…</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/22713" target="_blank">📅 16:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22712">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_KGCopv312Wmlijg7EcrYTkq4gXbNHeIyLkd1FKv3RMfgeH_7vztP8Eqq39jGxEY2ICYtkbq3bdkbc07qmBSL_qfH0VbzpzoJGBEzbnGRd1xAx5sKH5xaQScd1bXHmURlP8vDdcfN5p4NH916dr036TvK2P0q619J7WbBiYxaSHcbkupLnb2Lh4mhW5XIVmDeXKglK4r5Dj-q_SMwJacSukEZ0VRhkTG6LlxG8OtLCmbTV2i4xxVirCpva4SxhcNGhfUHYEJS9BeUJp3sjwZrk8Dyd8seqCppl8wxkAY45Kg8cIZxS7kSKQzup8J4YqGXyzaxZJ3F1QMARJD_Zrpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
#فوری؛ بعداز توافق‌ نهایی با ابراهیم کوناته؛ هدف بعدی باشگاه رئال‌مادرید برای تقویت خط دفاعی این تیم، یوشکو گواردیول مدافع جوان منچستر سیتی است. پرز به مورینیو قول داده بعد انتخاب حداقل پنج خرید تاپ خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/22712" target="_blank">📅 16:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22711">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6cb529dda.mp4?token=gpfLIMnqqK0-U7ezMDX5392eOsmGK3Xh2EqtrOR7wQS5fNFJkT61DE350JJAcbRM7ANea0XwXJK7YKXP_1R_R2qSPZVD_c8lMosE_EQ-i7pxQobWLqUNYa9fQCnXmbQZsJYmdYYJSyj2O7EQtLLqyIjS_j-CKAyCNVMfuTL7c8Z7JVRoIIPKdx7_vcA5IMzpLDFDmtT2mB-kwa2zF41rdft8_MKjIbkQIyJU6MGLvg9JsiopdvL6Ny0bkEow8B35cwkT5FzBORhFfeH56LKh84Z1SC5Y8OVkZPH6yBO5t9DugHnrpMs9OME0U7EBiERZwc_aT35v-SS-HaI2FtSRyoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6cb529dda.mp4?token=gpfLIMnqqK0-U7ezMDX5392eOsmGK3Xh2EqtrOR7wQS5fNFJkT61DE350JJAcbRM7ANea0XwXJK7YKXP_1R_R2qSPZVD_c8lMosE_EQ-i7pxQobWLqUNYa9fQCnXmbQZsJYmdYYJSyj2O7EQtLLqyIjS_j-CKAyCNVMfuTL7c8Z7JVRoIIPKdx7_vcA5IMzpLDFDmtT2mB-kwa2zF41rdft8_MKjIbkQIyJU6MGLvg9JsiopdvL6Ny0bkEow8B35cwkT5FzBORhFfeH56LKh84Z1SC5Y8OVkZPH6yBO5t9DugHnrpMs9OME0U7EBiERZwc_aT35v-SS-HaI2FtSRyoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
توپ فوتبالی مجهز به هوش مصنوعی که به تشخیص آفساید کمک میکند در جام جهانی استفاده خواهد شد. توپ رسمی مسابقه می‌تواند داده‌ها را با سرعت 500 بار در ثانیه ثبت کند، به این معنا که هر ضربه به توپ تحت نظارت قرار دارد.⁩
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22711" target="_blank">📅 16:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22710">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FSIFkPz96PgT7stgyFbbWFRzm9IIB8wnxkBpYPW3TrJB99gc7rgb6aU880Ju97razXdfxSrDUVbRUVsHaNGif_c-yEfoHHSDvYy0TGnqVWDlXwzEvyXh6eJsHMOtoW9DOemUouEdtCQecuRFWQbRKs5zGwbIW2Cbg1ZrMsDl4SU0ROdhn5MNQ1TNsTh8qqCPrmGyfqSwzp3y0NGz29BMRs-nDePVSR_a8P-MDKCY7LTSTC7bnxBVxNegccrCsnPaZ5LAaZ-mp0pwIG398IjU0CbVAaRnpwJLMpD18Ycd9eCXBgO6tLDbAVf77ZuTE6r87Q7wRTh76R2PW7DGUMQ_cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
#فوری؛ بعداز توافق‌ نهایی با ابراهیم کوناته؛ هدف بعدی باشگاه رئال‌مادرید برای تقویت خط دفاعی این تیم، یوشکو گواردیول مدافع جوان منچستر سیتی است. پرز به مورینیو قول داده بعد انتخاب حداقل پنج خرید تاپ خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22710" target="_blank">📅 15:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22709">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cNs6FZ2rGuZ0p2E85QDEXp23yzFNArFHnCMACMDNonSqWeHBF6HZ9OuGvhS6sZHIrTsDeVZTqYsPieDWk8F-Pnyw8PvMH4YvjAXq2Lo_-7KVEyAsueN3GUpqo9fTgJVtzNBktc_a-h_O2OkC1XZRusL9mbQw_eEpfGrt2SkayWKy3Ys5oKb0vffwXkl59aojO36k50VpGRZTI6ZoNDs4xG9QpXz_PnZSTZjglpwEpOEf7DwJBPtLkQ3wNFT5Hez2ykufqYN0Ftuj2Jw-961QYBfcpEAKWKInf8USvUSjadxy7T5cqZnbFV8qX0I3DIPParhpC8J02e8TkOSo7rJM4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باحضور دنیس‌وسامان‌از تیم جمهوری اسلامی؛
لیست کامل ۲۸۹ بازیکن در جام جهانی ۲۰۲۶ حاضرند وبرای کشوری بازی می‌کنند که در آن متولد نشده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/22709" target="_blank">📅 15:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22708">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vlIz0BA-IHQY_fcZj5w6tjIGR9MagsTrFaf9rvgfBx_ghGZrq183N9L2b7f_qDhVNKkaIG5h5cCc7EUYdpU9oWHLUNKXEtRl8Ks47OcbOEDSrrkapFxapA7YIxl5eV7M3cDem_tAVm1IagUjwfpGsLMAENwOii3JxRfyHjjvphu_aa_z_9QnqFrJYWbt15TpgsahFtCLo7m0nE3ORoWtYMelOr6BI4_Ok07eWyrSF2-FeN9hrWDPeueVj8kwidrZIbXMoYpt2RAgAIuvQTZVZgadieE-nQplvzxrHQj5xZgvoexip4TuMpAKVRDfZ6v1Ye6yBySUY6OHX3tFsZaYYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار هری‌کین‌مهاجم بایرن‌ و عثمان دمبله مهاجم PSG در این فصل؛ کدومشون لایق توپ‌طلاعه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22708" target="_blank">📅 15:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22707">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GhP42e-ZbgcCRzR10aUPuTQbs9yYegK9LCK-IQRPkhw6htPwLvTopArYuBTMj7J1yM9MyFdILHZyARSdtSbwJN-UDprV-hrPOuuNjvmcTlsCT-4j6eC-FLwCnDLjb_u23P6BlJuDs1GdB8Q30G6fy7Ip0BDK8b27wSXKc4WdHitbm0cq6UL6nBAJB3gGw0BWazYYLW9Lri3rmG5y2cVVHZ85ginARxvzVeUsh5LGbdG7r7_O7TvuKGloKcf1mc_tDSvS7Ehc06-GKIKNzEI36l0593mkNPgvjs6yCPcsE3m9xxMeQXYz_PJB1DDqdqCOGTTjgG9p8Zuuer8UQ5c9Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🔵
راسمون هویلند: امیدوارم‌که باشگاه ناپولی در پایان فصل بندخریدقطعی من رو فعال کنه چون حقیقتا دیگه‌علاقه‌ای‌به‌بازگشت به اولترافورد ندارم. برای من بهترین بازیکن تاریخ کریس رونالدوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22707" target="_blank">📅 14:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22706">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JwlrKvrkmepxcd89eTz9mhOcQxAPHJ1HctWeXQ8bAcvoi-IrYhsvqJ-oAOMh4jlLA7JdGY2rZ_qAWAasrze9G54iD2hqXDW39P9Vc-7Nq24-J4KGxU5qAVWZXIlMGzM71G2yLy9dQuQcylArv0Cdpj2vbhQK1Eci9MTswvV6Sy6QMbJaDrtd_e4dWQDNUHiePG9t56eIbl8Pjj-MK72ONrSZYOStEVoPyuXfnuFbdiQqIjFQXy-r9StBh1b9R0I4vBsOuF8ewl1AgHaQXyrcIyljzJx6jzNIeLcRTNSeM3fr_Cb2m5_k9pa-V8-By6aTGyBqfL1C17NwOPtCPoWW4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💣
#تکمیلی #فوری #اختصاصی_پرشیانا؛ یحیی گلمحمدی علاوه بر دوباشگاه‌عراقی؛ از باشگاه تراکتور تبریز آفر مالی بسیارسنگینی رو برای سه فصل حضور در تبریز دریافت‌کرده. مالک پرشورها قصد داره یحیی رو جانشین محمد ربیعی سرمربی فعلی این تیم کنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/22706" target="_blank">📅 13:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22705">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85e0818cf5.mp4?token=qVx96tRJt4rLRHMrRGVMzP0Ak3BLGu2O0FMerpH52Od6gFseE_BtODqcLqCBQvY-mcHq_LtbyCKIbycfFeHPUHsQe4M8f12-TNya3xpvv89DPW4ARECVEWXJ9chwE4ho-elYAzIaSq2ln7_MG9pcBRSbfvvyWjljFtaC1XFpRq4hYy4K2wPeIrypioO2wmZ2hB8b1wjnciYtYN6EptAHyyN2NahSj3fAONyknViqbSmrhmrmGf9Hpj38-p3YE_swX7OH59FAxKTHFNDmWP6o8ORFittrKNOcFZMRCOzc_UF2glPF9SpQIGZ9poYdzKLYJuZ_CIJLuWZ-lAnz1xvI3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85e0818cf5.mp4?token=qVx96tRJt4rLRHMrRGVMzP0Ak3BLGu2O0FMerpH52Od6gFseE_BtODqcLqCBQvY-mcHq_LtbyCKIbycfFeHPUHsQe4M8f12-TNya3xpvv89DPW4ARECVEWXJ9chwE4ho-elYAzIaSq2ln7_MG9pcBRSbfvvyWjljFtaC1XFpRq4hYy4K2wPeIrypioO2wmZ2hB8b1wjnciYtYN6EptAHyyN2NahSj3fAONyknViqbSmrhmrmGf9Hpj38-p3YE_swX7OH59FAxKTHFNDmWP6o8ORFittrKNOcFZMRCOzc_UF2glPF9SpQIGZ9poYdzKLYJuZ_CIJLuWZ-lAnz1xvI3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
تکل جسورانه تیاگو پسر بزرگ لیونل مسی؛ این چند ماه که اینترنت نبود احساس میکنم از همه چی عقب افتادیم تیاگو کی اینقدر بزرگ شد، آخرین باری که ازش ویدیو دیدمش دقیقا نصف الانش بود
😍
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/22705" target="_blank">📅 13:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22704">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m1knb00Gr44lhJCHsiN3NNWXPVnSSAkiw3n_DVciMXnMMgxl_GUGFqDfTWTi3DjsXb4qJ0hpqWgDPdL7Skgx5v2cqRff1mdrGDtMmMGJeOGe8CaXW-nse_ur1dQWcfd5zbbMY1okA6EjrvDRZhnVr0688yMbGq5OrW8B2swMRdngg78fkpsfGyakUxt62fBN8-f5YLN6v0tbQyguMVC7P5CaXNtLQVb_wGW1jmN1Z7DQatI1HrbxFy7LeYBneJOc4dz9bt089rgwMSLRGUQ_VG77ROuHQbLJ3nBWywcsSYtxCsdQQ3Pa1fll7K1SU-KQx_ud803FvrmHT_OqVHznzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌انتقالات|رسانه اسکای اسپورت: ژائو نوس، انزوفرناندز، یوشکو گواردیول، ابراهیم کوناته و باستونی‌فوق‌ستاره‌هایی هستندکه‌علاقمند به عقد قرارداد و پیوستن به باشگاه رئال‌ مادرید هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/22704" target="_blank">📅 12:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22703">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ev3k8tmeFw7SZOmtAxr36g1JGAyxVz5OcIkSwIgvK2aJweN4J8N_KSEMkWwhUv_OxOFzGKkBM3giJreji3H4Yj3jRKL4kPOv1Tn-7ZIll71X1hBnANRNgJKDtRkjCJMQSR-nNqvNCvMPF1IAb8bWKztFKM2JPuL11V-XKeyb64ANJNTNucNnXpLBpHdp6VwlZ4O0c-pNDa5rzIJRltG4e7HMwbf3BTYNXQQa7fBxu1tQLHDQiq-6T5nitxgcGIHeTq4UJTy80Sdys8VhOZFVwFRaXCYhveyIR_EJMVReEcUA9TQdpaMSCR0uYBZvOi4YdPtIo7j37Q5XVDkNdIwobQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ طبق آخرین اخباردریافتی‌پرشیانا؛علی‌تاجرنیا رئیس هیات مدیره استقلال تماس های اولیه خود را با دراگان اسکوچیچ و نماینده رسمی او برای عقد قرار داد سه ساله با آبی پوشان پایتخت بعد از جام جهانی 2026 آغاز کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/22703" target="_blank">📅 12:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22702">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6YVS7O5RlOEoEYSZPx80uLb8ly6SibvQ5Shqrlp17hPK9LZyw2QwwAl4ZBIEKeZezUAIOLUR6b40fIrlAuz4M4U01rzEEU2ymOu7XZ8INlJZuhQ1UMN2XyW4NBmX3nAC5rrzfuNaxgkwO5HKL0sDhAiGTheCqyeqIx8PVtDVZwzZUrXnYj7RDaUomf0M692S4JUz9AP4KRTAw9pW4WiPhvEP4EvWyCEKqSYhcfcpozk2r5M5r7n0gb8J8gWI6QGQmggW14T-vnlYeYkaGDAMoAxqod2JR6Ps9qKPhMNJPlj-GOvq9oHtrPAYFSw-zBRmyZVCBSkDiWwGzT2GhZTRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
هری‌کین‌درباره‌تصاحب دوباره کفش‌طلا: ‏«این یک افتخار است، به ویژه که فکر می‌کنم فقط رونالدو و مسی بیش از دو بار این جایزه را برده‌اند.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/22702" target="_blank">📅 12:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22701">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gIdskJrTnNqubKCWYYA8ZKaRkfV51bTTakMNa_Osq3A41rWTSsAQv-msHnb9BBa7mdSMWZJJ6kOH7v670pOekIb0Q2iAEAB4cARojz_z0JC-0ahY-43Gp6DOXbGZkska1dKhkbOiSvW_w9DpnNHEjiu1I-O6kvQJsJvK-8mAuJ4XR_Yp7mm0s7h1KLCJ3cLvcD8rhoiFDD4vq5j22bATZzqVhRS98PKtRqmRVa7_mVWTKxrIo7oh7mxNjoD_85lbMpkXDO2Kj2Tb937i8NIQxpjzkct_-prdoLWk8_zKpd69-m6DGDrcsoVnBNAQ6RorVeJqX1bAeIKXy8A0KV6Nog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
۳۲ باشگاه با بیشترین بازیکن دعوت‌شده به جام جهانی؛ بایرن‌مونیخ با ۱۶ بازیکن‌درصدر این فهرست قرار دارد. تیم های پاریسن‌ژرمن، آرسنال و منچستر سیتی نیز با پانزده نماینده در تعقیب صدر هستند.
‼️
نکته‌جالب‌این فهرست، حضور دو باشگاه ایرانیه:
🔵
استقلال با 8 بازیکن
🔴
پرسپولیس با 6 بازیکن
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/22701" target="_blank">📅 11:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22700">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c4ff2b5a8.mp4?token=R2jHSQL09eO27Jp-T_AunPPZR80E01JejE8Ee3vbENjcqICqjVGwCM8TdntSfCuq08dba1X4GRzys07EgpsD2j6jOC9fsNSk6tKeP6wDwX9zBl-cORvf9tZ5MSVC2p1tyd2J6ZtD01s3BSSaZ6SpFMUapc52CeezBJPZHqs2xP7o5WWW2R5S173tZAehMaRo2mS_PNeyrbU_4JB_0dU5laAiYO2lxdF_-2HIPIto9ZUS8tqHX6ntVkBJ4z2zAsyi1NwuUXPuoblAre1DM6nlwkxDgzM1prsyr1fGLnMovNYG_AjtCThLfPVsb-zYrwgtA66jZY7zRtNmS1RJxVM-Q2puIHPcm8UbL3hoNIvwR-ZW3_Nsu_6XoGiKaCiek4_JhfnxCg6RLrLQr58wCQiACu6MzSv3ddiuDn4u7HuxQHl48ElA4CaIOmgbX-Jgq6NaS4xmBxCbxW-V_FEuCrVZ-XqeyCrZeOKrN7KUgaiHj372B6rGESDfKEHLvs4tQscd2UnwymScUZIgZR5WG1yVhZqssJlXnVTDxx8iTV8qPOogzYTaIe7i1WA1m_E9-AlWxzz3cyJ41QoG2J0h0RpXocVMPMcdbkqNWaDPSzEmEWiktqyl-W02Ir3eLeAscBsrEMZzZvyb0fo2NnX_h-K0EQZTDdFPW-6NrLr1BQ9lM-k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c4ff2b5a8.mp4?token=R2jHSQL09eO27Jp-T_AunPPZR80E01JejE8Ee3vbENjcqICqjVGwCM8TdntSfCuq08dba1X4GRzys07EgpsD2j6jOC9fsNSk6tKeP6wDwX9zBl-cORvf9tZ5MSVC2p1tyd2J6ZtD01s3BSSaZ6SpFMUapc52CeezBJPZHqs2xP7o5WWW2R5S173tZAehMaRo2mS_PNeyrbU_4JB_0dU5laAiYO2lxdF_-2HIPIto9ZUS8tqHX6ntVkBJ4z2zAsyi1NwuUXPuoblAre1DM6nlwkxDgzM1prsyr1fGLnMovNYG_AjtCThLfPVsb-zYrwgtA66jZY7zRtNmS1RJxVM-Q2puIHPcm8UbL3hoNIvwR-ZW3_Nsu_6XoGiKaCiek4_JhfnxCg6RLrLQr58wCQiACu6MzSv3ddiuDn4u7HuxQHl48ElA4CaIOmgbX-Jgq6NaS4xmBxCbxW-V_FEuCrVZ-XqeyCrZeOKrN7KUgaiHj372B6rGESDfKEHLvs4tQscd2UnwymScUZIgZR5WG1yVhZqssJlXnVTDxx8iTV8qPOogzYTaIe7i1WA1m_E9-AlWxzz3cyJ41QoG2J0h0RpXocVMPMcdbkqNWaDPSzEmEWiktqyl-W02Ir3eLeAscBsrEMZzZvyb0fo2NnX_h-K0EQZTDdFPW-6NrLr1BQ9lM-k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
استفاده عجیب از گاز اشک‌آور توسط ماموران در بازی این هفته دو تیم بندرعامری و شهرآرکا البرز!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22700" target="_blank">📅 11:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22698">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tNx5Lk4_mHy1IqcFbWYMw2mgqZcLtNRWbiDDbvlngyD38-f4Lk3CL-2aqQ2VCAhwGA0KhG39bIXJ_IqTbsc8KsdZerQeNKS55D3Gw-m7Xe4YowMhLd_dgEgYmxCAWCH7VAfV5KvTQ4SrS14kmdmdyeEeiKs-V3WeQPc606NerHtuoONitkOPLxrvtFyrW79yAHndtjbVJC_YnxTKZvgDpha7rj6LA4WuZqthXVCtyn8y-mS-NPQ4yII9vk_Spx_v-QES1XYP1lN4mSKm8f4ipo8xtlAantWq-D8339e4jatjWXLsLmppexQHxG0-KDnHys9WM21XowifZRCySw0w7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌شنیده‌های‌رسانه پرشیانا؛ دانیال ایری مدافع 22 ساله ملوان اصلی‌ترین گزینه اوسمار ویرا سرمربی پرسپولیس برای جانشینی مرتضی پورعلی گنجی مدافع 34 ساله سرخپوشان در تابستونه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/22698" target="_blank">📅 11:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22697">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">خلاصه بازی سوئد VS انگلیس؛ بازی‌‌ای که زلاتان یه سوپر پوکر کرد و اون گل مشهورش هم پوشکاش برد
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/22697" target="_blank">📅 10:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22696">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UdNYhdKKW1aptVed8q1IuuUdGvvxxnR_k-fmqBCz-N6gs7s4vd8PCVV9HfsYfXoVybTfTT7CyrkGQKPBGqudhj-EnkfVY9koPrNOSlIHJLkow5QAIdBHMvXQTNTLaKpK0T21OzI7_XP4mq3vYuB1I3XAqaRGOkVxgJQqEXLMO4eMmqFTGcm8jwfqODay84KNkRcIZ-1dLb2v71Omwpfmy3yZiUctH2lyCXmEv9fjb0Y-XzdsoSG1yQyqEec_D0y4VFS2eXmAb2RKIulVDJwAh8_uDsm2qt7T7DnNPDKkb66-bPVqoTVa-PqGPRCSRU0xLqPMHE9gY4O8cteQzn_y3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اسکالونی سرمربی آرژانتین:
مدعی اصلی جام؟ بنظرم تیم ملی اسپانیا قهرمان رقابت‌ها میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/22696" target="_blank">📅 09:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22694">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B24ozusOr1TH2x65ih9PNXBh7Tw0_bWmb7HYXTUw-bodDRq2r5NSJivTv3jOChaFfGyk7rHagfNH1IRWBEAVMJxWrIaV9GoFt1zV8o7n3003R2fZO81yRatEMhHtIIIwBLAsVuEznhhwXjHRuD-G4Bg3wKzPTkX9AUSgBVzThVZp8BfhD69iV3DVPSIFNOhb6DXNgdsopdjfGQ-vIe5XxWB1YQTRbXu_mgQXSmmfu1hRiYBTG-rRi3FcY2nBB2xZHgmteOveQQzbZenFRV2o4hN6zUuZvqB_-0d3FtwXF9P37v2mPAFN85kenQaYftIJr-QLkTjzIAg09NbPP6C2qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اینفلوئنسر برزیلی کارولای شاوس لباسی رو که قراره درجام‌جهانی ۲۰۲۶ بپوشه به نمایش گذاشت؛ اون با پوشاندن بدن‌خود باصدها برچسب از بازیکنان فوتبال این لباس رو طراحی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/22694" target="_blank">📅 01:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22693">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rjaV0-a7B2-lTQRhEyE5fzst7vRdHJyUkWC5AHZ1pzPvc45lv-luSLQXWi_8D8h22Wk8CRciktJbVxA0-Z7NkT-G8W5BKmI5Wl2BdBlHurGMPhFLrQ6eyPrVZM4qGmsBtnvbkXbc9vq-w1eC9NAe5hafTRuLy89_LwmXM1RvClU17JnzcMvixAqvysHGVcmxAva9EQGL7sl3YtC3iKSmcww4S4G2Pl2PPOmslXyMPeZaf3VwuI5LQKNtXXDPQuCCwJLCe2tDEwgTGhF3QEU-11WYOmbjCbKLyIrRqTp2P6xNLSyEoHgvj9DRojd0z3PMCr4nDfH1RfydBsMf9LuQKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدار های‌ امروز؛
از تقابل یاران نازون و کریس وود تاجدال دوستانه هلندی‌ها مقابل الجزایر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/22693" target="_blank">📅 01:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22692">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cv9oMGZNClGWfo_T3NpJ8qt_aIzhptgWWIxMgmRl1uAO__ivnILoFa-AkPxNfBtSmel4zU07-MFc68-HhoS-L3kkkB-VCDN0TJVnClSjMgMM5nFunuPXxAUnUSIW7y7NbmEQA6ZMvYLc1vmUwBuhBR7rOl3wc0N_XlER5GP5I5wyalBBHwP1uaevT0VuUEKmnBijVeQwHqMuB4gmdQwI64V_dIjcQFoFLjQ772QYIyNabS6qZcleI6SABAQSC9asDZOzYpidL4cNh6FYyV7ZXh-ez64V2IJHSGjHAp5kOUgvtwjywwF6N2ELrc8ySyRlradabi_bXOXlCHPYV4nrvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نتایج‌‌دیدارهای‌دیروز؛
شکست‌شاگردان کاناوارو برابر کانادا و برتری بلژیکی‌ها در جدال با کرواسی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/22692" target="_blank">📅 01:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22691">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JnAn-LJFVGxbE2S4LpoyjZE633VmIkRHO3iiDLsUIYUV1ngRquJsp2LLz90T1EaIL-wOLCByop1U7gpSr7hB-sWZbwSGvalkbOmQOQf9Mqk-uYobZKhZglf5CCOt47J8s7-p8MInj5oKq7W2zBXdhxJmxqv-cf9osfGGRIkbXrS4iP92FC4kj8K7WITTnWut5TCZfNVbmzCNd_LWWCwyHVePEDTiBHHWKC3Dk-BW70J5hsM5dU46LXoVD3h9KCt8ijKyGOHrEaD9Mnmdd6C8UnJKz1ciIzKXt5jvx8gd27PShpxzCsvBLE8i-Hkq1F6Kl_e8jOPLNAercUPmjl5S_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#نقل‌وانتقالات|ادرسون‌سیلوا هافبک 26 ساله برزیلی آتالانتا در آستانه عقد قرار داد چهار ساله با منچستر یونایتد برای جانشینی کاسمیرو قرار دارد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/22691" target="_blank">📅 00:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22690">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sm3ycyKn1u_9YKBwdogcTZNfIXzoyVaAtRAcCUsS7kGVT5g-HyWJY78boGMR0jy1mNps0REKrRjWGEwV1IKN9S8LBFF9ix6JwOMAR935-OuFuLAQCG3wHbN8duvYUQCIOwMlMFA0jsHQrtV1tBZNjU4OQQXLSwdLD6omEEI0tERdx-6Q1XIoG7TLutSSVDkpMCfo6-4e5pbDzWQEH10xtcO-STsxo2oQ9KPzw7lSqV_gxpriUXMg2B5wJ770rXjKTXppFlEwmAtkz6VRwoNcKsEjr-BkwZ95xANMTC_Ry39a145O-RPhSSnFpil9R3xM4iwnv0sTvNjglAFbDUohvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باتوجه به تعداد سوالات زیادی که پرسیدین؛ لازم‌بودبه‌احترام هواداران پرسپولیس بگم که‌اوسمار ویرا لیست بازیکنان مدنظرش رو داده و از بین اسامی 9 بازیکن که به مدیرعامل باشگاه داده 5 تاش رو قطعی میخواد حالا اگه مدیریت علاقه‌ای به همکاری با اوسمار نداشته…</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/22690" target="_blank">📅 00:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22689">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a506ed7ce.mp4?token=q29wzRa_TOHLpatpC5YunAR0dKiD5RFnU32tmx-4XiW2Rz_R5SSaoHlCCVYcSS_9Q_PAP2OI48CFimWh1ibgmjBY-7vd4UFm8iEckIZksGObVUZKRcThmDuqeMfgBH12hvUtSnyMAqhC-uguVA6AKCCEJT10uh0cDYABO68bhWvqebn39bZApNZmHNNuBj-FyhAIGSX53NhVRcJ52HH3NXUQH4CyrgScp023O8OoHnjpS47sbtUXgbSMtbtHI8mzMS_LV2tLO6ak9aCchKGBHkUh-a32pSxZtbZD-tU39-rSuG0zTl8YLJBmBG3LpwXyw83Z891d9bSEdf-RPqOT3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a506ed7ce.mp4?token=q29wzRa_TOHLpatpC5YunAR0dKiD5RFnU32tmx-4XiW2Rz_R5SSaoHlCCVYcSS_9Q_PAP2OI48CFimWh1ibgmjBY-7vd4UFm8iEckIZksGObVUZKRcThmDuqeMfgBH12hvUtSnyMAqhC-uguVA6AKCCEJT10uh0cDYABO68bhWvqebn39bZApNZmHNNuBj-FyhAIGSX53NhVRcJ52HH3NXUQH4CyrgScp023O8OoHnjpS47sbtUXgbSMtbtHI8mzMS_LV2tLO6ak9aCchKGBHkUh-a32pSxZtbZD-tU39-rSuG0zTl8YLJBmBG3LpwXyw83Z891d9bSEdf-RPqOT3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحنه عجیب از خوش و بش آنجلوتی و اعضای برزیل؛ آخه چه‌وقت دست زدن به اونجا بود.
😒
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/22689" target="_blank">📅 23:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22688">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RrQ5oDLT9fcsAP7DyFEpvur4yJ77UBdv9rLDwIr4OB0pZYTLMDkmC8qgaL3g3DlfptKGW4dO36oISlpQjgqVqHOEAMkqGyyIp-384hxqmbfmWEXtAzKVk9V1aEz_S8_e6D2ZAAEGzCVHJPIoQQfAnibRtA0xSeZVwnSRoyNlLcTfBuq4gnM6eASewPu0phnxeKqxckQxkuC1ROai4tX3l9o6LUsN9ORZhpjyyI4_ziflyc2B_oSkMNYPf-qDRTC1s6yK_zYa0L9AqIvGHkzJAvFvSzBaZl8fUbaa0JmuD38GYZJTtvq5zdeBpgIj0SUqNNiEI4LdcyI_3KBd7PbfKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
رسانه‌های عربستانی:
باشگاه النصر بدرخواست کریس رونالدو پیشنهادی سالانه 85 میلیون یورو به برونو فرناندز کاپیتان منچستر یونایتد داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/22688" target="_blank">📅 23:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22687">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cBP8mNLYvxwE6cdLaZVRoCu4HglcqIcsth-3k-RYVXjzeqFKoj3b-OW04mpjbHu4v100rcHvX3Noag-ub6vGB6lLh3OdflcSVLoEB9klPsGWw2COWh2EcxL5qNDJvDyoVrd2lpcarumc7-WPwngYHCLEPwktr_1kbvVgcJuxgoVQ2AIWqz8zRkd3r5gDvvKgXqIbFjlE6NdoL19ENx6LCb0iB4EXdPRolEn0qRUu_8PY3OP5rMXpXyPsMLHUnj2Igx8dqCwVpKcBLg4ytatIpGgX0r52tupQaW17qp7ahqweSQzx47DfK-iE2Hievks-JmQxddMGn3W5h4r93VKweQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم‌ملی‌بلژیک‌درفاصله 19 روز تابازی با شاگردان قلعه نویی، با نتیجه 2-0 کرواسی رو شکست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/22687" target="_blank">📅 22:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22686">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yuzmy4zLzjnQcUKlFh4hQyeBCSEDp24B21p5sINq2tB51z-43S_HADOJ_zPkLmI48N5dJQM-8eDCxqPpIKAScOGg-VC8nnQRAijHhsUnIGJy3Rwtrmj9I-ryNCCMR8P1T2EcJ6wtmG0IC1QJAvnBjNk0l1I6Ysj4HuZcPcgonAV1JchTZvFIvYVztvYiXYdFetN6QsFLth2GJyir-bqOzJGPHnPD997HQ5mIFV4RHhYDSIBC8h18YX-p0cc5Kyezz4MyGHsXqsNFYT8wXtN1CD75s45a8J31frhdJGUI-3ZhLIAePj4TGVR4c39cRCt1SC4k9ouvTgvze_4_Do8mjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#فوری؛ بااعلام‌رومانو؛ باشگاه PSG بزودی قرار داد لوئیز انریکه رو بلند مدت همون دائم العمر تمدید خواهدکرد. حالاخداروشکرکریک با یونایتد جا افتاده ولی بنظرم تنهامربی که میتونست یونایتد رو بدوران خوب خودش برگردونده همین آقای انریکه بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/22686" target="_blank">📅 21:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22684">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5291786993.mp4?token=A6htvWnP2zWcRzrhUDD19rE8jLvAXuewr8pJ1op1YWR5T6lS_WaWLJ99_tT-3bFmjt4dtIz8HS9xfFe9zNH6aBh3y-KQbXdzq1giesNa_81mHLNIc-_Jv8s6Z3HbIuw8nwfLdWzO1w6Axqv9Gv0peb-37gg5brnjnI6Z9tSx5XHdT2BuIRhA_i1VhsRejw0XP8LgLOsnQNLsImbCLSbbudGPbRfuoEwTLxUCFSknwTu9cD8lS6VtmUJH2IK4TnXvpHpi47CMwJX07nMjFnvT0LCFB71r9JeBEdfq1ZaXEKScpP2O0DcoeM_PZ80RzKxSpZUDBA1CStTyG8y3zcaM_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5291786993.mp4?token=A6htvWnP2zWcRzrhUDD19rE8jLvAXuewr8pJ1op1YWR5T6lS_WaWLJ99_tT-3bFmjt4dtIz8HS9xfFe9zNH6aBh3y-KQbXdzq1giesNa_81mHLNIc-_Jv8s6Z3HbIuw8nwfLdWzO1w6Axqv9Gv0peb-37gg5brnjnI6Z9tSx5XHdT2BuIRhA_i1VhsRejw0XP8LgLOsnQNLsImbCLSbbudGPbRfuoEwTLxUCFSknwTu9cD8lS6VtmUJH2IK4TnXvpHpi47CMwJX07nMjFnvT0LCFB71r9JeBEdfq1ZaXEKScpP2O0DcoeM_PZ80RzKxSpZUDBA1CStTyG8y3zcaM_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بدل‌های ایرانی لئو مسی و رونالدو پیش‌از WC
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/22684" target="_blank">📅 21:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22683">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nXYLVfGt2M8bgw0P730LsE2k0eG_VJlBDEr5sdKvv3KedfJNbb_jMlrIXp1GdO0_HpWDy8jKNndin8aAoDpaUsaJC4YN8aPm1TW8quzhKaey7FvZsvgCJfVHYpAA0ayR183ht0B1hcgL2WNnc5UyZweL8g1F0oKUzWwVDhzsUqcWBki2oNyiOWIB_NjQwHubZww0-NjmDMg1Safcj-Cv0-g7P5FvvtCB63_-KdRWDn17vWKFX9JpVf5-ES9W4d1X0knkaIC-XQMchcvNGktbsLnVtuZKq3xHRjoU-_HquCQ6FbHlPH0D8hbJ0nmTEqIz4-_YhY5oMn_3dBF6cWBMCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
فلش بک بزنیم به سال ۲۰۲۰ و شاهکار پدری درسن ۱۸ سالگی که تونست طی یک فصل ۷۳ بازی رسمی رو بازی کنه و قیافش به این شکل دربیاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/22683" target="_blank">📅 20:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22682">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/739be8e1c9.mp4?token=Yyb94IV770kyMAVbeaW1itO-XHfUn-x6ZNqwPa63b5foKW47lQ75PdpGNcaNNnkQii1IWja-o1yfLi0KE6xm0FcESxOzuVYQw8NegxWu4hqPb0Q7n_CHJ4XwHRzXxLqprjYlSnpUVy4_DmTqWk50Y5i7LhpH-byRYGA9HKtQbC8sD9BQOsYCcdypiC2EwE3sq11e3EA6iGRVWCMrVEx0KOmnVaZu-3CnHtTHLBa9x8nZ15YWNr9CNAryE8qJXqN9tFdmng3gaeUihdlgfdG6yoMl2ivJXEgte7HGUiZIi6Zf6YEPf1rWh0kAADwEWL-voPUiDtw_WCogkjlZJixqpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/739be8e1c9.mp4?token=Yyb94IV770kyMAVbeaW1itO-XHfUn-x6ZNqwPa63b5foKW47lQ75PdpGNcaNNnkQii1IWja-o1yfLi0KE6xm0FcESxOzuVYQw8NegxWu4hqPb0Q7n_CHJ4XwHRzXxLqprjYlSnpUVy4_DmTqWk50Y5i7LhpH-byRYGA9HKtQbC8sD9BQOsYCcdypiC2EwE3sq11e3EA6iGRVWCMrVEx0KOmnVaZu-3CnHtTHLBa9x8nZ15YWNr9CNAryE8qJXqN9tFdmng3gaeUihdlgfdG6yoMl2ivJXEgte7HGUiZIi6Zf6YEPf1rWh0kAADwEWL-voPUiDtw_WCogkjlZJixqpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شادی‌جنجالی درلیگ آزادگان؛ سلمان بحرانی پس از گلزنی مقابل تیم نود ارومیه، در شادی جنجالی و بچگونه گل خود حرکت گلر حریف را تقلید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/22682" target="_blank">📅 20:16 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22681">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JeM8xAVYV6PqAbgyaBR7fyNn1i0ZEU545hgGTLDtCpmWsJ4WE7KGScpNC_foweA0zcrdWymqSmZtgkLcZbN5TKLl9e-zTIEhVwaiZj_ZND3ceRetsQW40sSIdlxCN0srKWxIpB56OVhWyjw6L2J-nfO7R1SiKQU9v9fZVT2LYy_oOvP1FRVMOIRbXILR7tCRmUiEdk97HSyHC4zIIZRGItkMH0k2SB39RXXuehS6b5elzdAWoemAwMh5FBUvOpnW2b5py8Uly9khcQJ8VhM9K2JwOMwFlAPrJUOtdILw5T1JD7nr50RQJNy4qB-7fep986BSCcrew6RzbUJ5pcUNzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
کریستیانو رونالدو 25 درصداز سهام باشگاه آلمریااسپانیا رو رسماخریداری‌کرد؛ 7 فوق ستاره‌ ای که سهام باشگاه‌های اروپایی رو خریده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/22681" target="_blank">📅 19:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22680">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5549cd5855.mp4?token=e_QsnOoGZoOOF_lfaIFExl4wSDevG5DcvDT03k73-WUYc2JwQ8KeaWrZVC0Z01Gt7jdO2gmT3L0B2Q9fkbBitWUEyoVSrhZBXces8N7XOGWgq5dNRh9PW5jslHLM8leqk33bMAAXOlSx2A9a8nSCEzxJvcoY3FuPWb6YxQJ3f5Lahd4Dj_8oe1UCTSL-SF1Nv5dooOj6tbkk5VGIIswLvrFGP8YeEpM-A5nlbTc7DOl28FKJgEI4GQB15pFFdufEd4S018TpCz7v2ccRBke5ljeVsYumOhfmpYfyQg9AJEuNOSrOGuyRAfW1mrLsxCaiwCnOipCp9ddnwi5VxIq2NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5549cd5855.mp4?token=e_QsnOoGZoOOF_lfaIFExl4wSDevG5DcvDT03k73-WUYc2JwQ8KeaWrZVC0Z01Gt7jdO2gmT3L0B2Q9fkbBitWUEyoVSrhZBXces8N7XOGWgq5dNRh9PW5jslHLM8leqk33bMAAXOlSx2A9a8nSCEzxJvcoY3FuPWb6YxQJ3f5Lahd4Dj_8oe1UCTSL-SF1Nv5dooOj6tbkk5VGIIswLvrFGP8YeEpM-A5nlbTc7DOl28FKJgEI4GQB15pFFdufEd4S018TpCz7v2ccRBke5ljeVsYumOhfmpYfyQg9AJEuNOSrOGuyRAfW1mrLsxCaiwCnOipCp9ddnwi5VxIq2NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این پست برای رفقایی که تمرین بدنسازی انجام میدهند. بهترین‌میان وعده‌های‌قبل و بعد تمرین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/22680" target="_blank">📅 19:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22679">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZ3_sW5_GwPV2ogFs5a84em2a8TI_jrhc8jmIjBWH02cAIrzbM3g753cKAjZu7fKeSealP5KjzzFpDTMvsExejjfXmNd2b7WyMckG-MJ1nCoHQog6vcJO33NRNBAfwKoZO7bkRk5KQKWwDd9zlaJqEnzJBanl0V6P41eD8d_hAS4uu6v4RsSPtgV9rY44q7TESr44HmhntxicR8V1cIrXq09SwL2CUW2X8GGc0p96tNzhrBYrywWzfzRKZHMzaZ_svjw1gtEpSUR5CggAWC7uEWDzspKmox-RirQQ9BZutBsAnzo0gJvA3Ktfbm5KlFolDqI--aCHxTzuUnZipMO3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ تمام‌رسانه‌های‌معتبر بجز رومانو میگن که بعد از ابراهیم‌کوناته؛ خریدبعدی کهکشانی‌ها برای پست دفاع دنزل دامفریس مدافع راست اینترمیلانه. ممکنه بزودی خود رومانو هم هیر وی گو کار کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/22679" target="_blank">📅 19:22 · 12 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
