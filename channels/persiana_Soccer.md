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
<img src="https://cdn4.telesco.pe/file/t__wUD5960hfXh1yJzC1VboECe33bVVc130ScU6CzuLMnVPSJ1z8_IElWBps-Ya-jwkz3N-gF55iFyySrQSHJFl4XnWK8TUP-4TV9B1FXWUozqNLN0UW1BiXlXh5PvDY5i5FzPrCUgGUkInFiGcjmwSpJAMMfu5mkyOl3ixhfmbnYSOQxh77fdbFeexTdvgRUGl-n94PUl_BwykOCNRB1jqTfl7Po8aY7OU6oXwjej0mMqQdliB4KoojOuPbKyuq9gSEQM0kJd76mINUPOWVbehrU3VzpVl3nqFsi43_t1IPketbQsb3eea_J0a-UjZT_avp9lx1MddaDI4GNRWb-A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 469K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 22:26:50</div>
<hr>

<div class="tg-post" id="msg-25796">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mx2MTsnyryxDtBHHMBRTM_DAOTwiUTDL92YSPvXoQxb61rQFArBD43j6BB6aoPyZF1SyScSREXCzMTQw_fo_hzd1OYYUriwG-KMCACyUm90wkXZLAsvZp2p0BQXhy5taNbTxyU2DMJ4IpXnmUE1lOiGxg3xo4ku6zLDWlqEXjV7mVnNC1hWHiEVdlZcowFmksA3IqRbrgrNgv0oRkE6qkfLya91RTd76rr5VD3Zf2ZXT1Nf2ALPVY86Bk9zq5XF4jXKN04m3lKeZR-eNv-Zc9s6Go_QOsgKXwrJtuLVxGArKgESgRw_6h0ysXKsPD_E_6xWqkH1s5gT9_N3jqjsf2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
هفته اینده هلدینگ خلیج فارس؛ تغییراتی مدیریتی گسترده‌ای درباشگاه استقلال ایجاد میکنه و بچه بالاخره از هیات مدیره رفتنی میشه. شخصی که تاثیر زیادی در جدایی ستاره‌های این تیم داشت.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/persiana_Soccer/25796" target="_blank">📅 22:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25794">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/113eaa3d5a.mp4?token=IPxthAn9epxc_wXkbgSZMBKA48LXyS9fat0I9j7bFYE0pcc20o1VceKaEpFaNdRsT3xkvnhjx6Yt1khg32cVqMT4hXs7fKbNYonamAK1TNjvISd9HygOJOF39MuOatXOcVxOsYoNhxPdNlnNC_D8Wkn-lb6Bm6qUw1qcQ_616ay3FvpGAKZigaVdmr1V5dMEPbdRtwCFlz_AcSYpD1dGE5MZ-DuPNORjR2YE_bcqdvAGoF96ZITGbXcUrcc814ybijHhnTXmxpzARQcq4elHD4KjdHDr4Y4t6YbkB907syMPpMMn3lx4g8A9fGiLu4uQ4RCOR82sanm6GSuMQI-CdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/113eaa3d5a.mp4?token=IPxthAn9epxc_wXkbgSZMBKA48LXyS9fat0I9j7bFYE0pcc20o1VceKaEpFaNdRsT3xkvnhjx6Yt1khg32cVqMT4hXs7fKbNYonamAK1TNjvISd9HygOJOF39MuOatXOcVxOsYoNhxPdNlnNC_D8Wkn-lb6Bm6qUw1qcQ_616ay3FvpGAKZigaVdmr1V5dMEPbdRtwCFlz_AcSYpD1dGE5MZ-DuPNORjR2YE_bcqdvAGoF96ZITGbXcUrcc814ybijHhnTXmxpzARQcq4elHD4KjdHDr4Y4t6YbkB907syMPpMMn3lx4g8A9fGiLu4uQ4RCOR82sanm6GSuMQI-CdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
قابی بسیار زیبا از سه مرد شریف و عزیز ایران در آستانه دیدار امشب دو تیم آرژانتین
🆚
انگلیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/persiana_Soccer/25794" target="_blank">📅 21:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25793">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/558fc696a6.mp4?token=ISyZOCKv0RWZr0VNa2Dayxus6rEyDz4eVwTW3YzCMyMwLuMckOoXPNEYbC8SAzEwv9hYr1ypWGLOyly28G6s3StH-UuXVNk4e9BXT75WoU4dxjmogYKXp6CbAnr1pRhLASLJZjjYB6Fnzvk03TDplkicn-_SGlnu3U2-F3VJP5o_tHSKQOKZHUPZlk6vPAbAmeNzyseQrjqqZARfxZ0C4T37PNOehVEJ3hqEiGpVYAyebINljnuu4VqQm3rEBz0iDeQwIGk7aF6UnRfa8IQyZNGK7piBj0KD70sPG-qnga68orjheE95sEPt19ldeBeYFoPfRG2zCmRwpV48hfAGmoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/558fc696a6.mp4?token=ISyZOCKv0RWZr0VNa2Dayxus6rEyDz4eVwTW3YzCMyMwLuMckOoXPNEYbC8SAzEwv9hYr1ypWGLOyly28G6s3StH-UuXVNk4e9BXT75WoU4dxjmogYKXp6CbAnr1pRhLASLJZjjYB6Fnzvk03TDplkicn-_SGlnu3U2-F3VJP5o_tHSKQOKZHUPZlk6vPAbAmeNzyseQrjqqZARfxZ0C4T37PNOehVEJ3hqEiGpVYAyebINljnuu4VqQm3rEBz0iDeQwIGk7aF6UnRfa8IQyZNGK7piBj0KD70sPG-qnga68orjheE95sEPt19ldeBeYFoPfRG2zCmRwpV48hfAGmoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
#فکت؛ ‏بیژن مرتضوی تو فینال‌جام‌جهانی حضور داره، اولیسه و امباپه نه؛ تعز من تشا و تذل من تشا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/persiana_Soccer/25793" target="_blank">📅 21:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25792">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MNFO3j7cliQT8lVASY8LkjeLi6isZRsakB_ogDe5NvqD46zhwteD3mzvp7WL8lY_HNmmlHCmDaHWXzyhxlGJUB3fuKcREnl5Woi8o_lQ7siU4_gpfgsMz18ZynDmIciqi--AB2b1Orhb8KpREQm0KC4wGrEbuoKKdj0QXunVQolRNmHyxrQ50ElanFloN3gD-qNZnmpL3tllOlvL9ufZe0heiMNNKL9yAuu_bLzaaoEEQt-KV4BCohn02yJsoXArbKHDoKt69lJxSsClu-MUVrWe8abeE1ajZtokEhQWADWEhbzWLWm9mVlfu_3NIxtXo9QnuvKAR8a4xTRXoCoG9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇫🇷
🇬🇦
#فکت؛ با دبل‌دربازی‌امشب مارسی؛ پیر امریک‌ اوبامیانگ برکورد 400 گل‌زده در دوران حرفه ای خود رسید. امار فوق‌العاده اوبامیانگ در این فصل درمارسی: 18 مسابقه، 10 گل زده و 8 پاس گل.  گرینوود هم که در منچستر سرنخواستنش دعوا بود آمار خیره‌کننده داشته: 15 بازی،…</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/persiana_Soccer/25792" target="_blank">📅 21:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25790">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GX99Y_HuA4cO-xdaIKvjb9H26NnT54BJtfCd5AMwNrPTp1SlEqNlFUDU77UNJNd14hj5wC6-roCA-UZUONlr9lh4UmRuqxHR2vHtUek3EtT4UXefOk7iex-egi-dNU4o3SEu07WSE1UGXzHdw3M6c-Oy_XyKMgNfNAIfKaZ-riuUu9R0B_DeAzS58Gq-lpzjp15doMb2QguBHbqZq70c2FduWKBPP9reWV6wLDsWMTelVpfepYGBtlsg_ledm-HKG1uiOLusVL3SOgS3Ps3NdbiBM7_nVvUvvpH7wdc0Zl7inK5d9P3eZPEMpYCUwexV6pnla1r5Be-LOoVUjBfBhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UciGm-K7cCiVReEYyecFcTGG3G0neNxpOihPJUw8bnfMULB9aN5H5Uf7OYWwNYiRtZtdst0SFhiRqfJO4HZGllzInUhetO23iizYW7xQhZNH-Lvn2_wOjxNlqER4lcgZ3dT5pt2yOG8hzgMhfNcudBFihfRq03lHNSQqpkcgU-_nx1Srb_locf3ZjgQm77VHyeTpAqTAw_ejSMZ-B9k1oLk-r0xxav_G3oslgKybmnJn3O0qFepo4ZgBUdNKs1Hj5sDuzM5HAsrBKVlIe6iCWtwPN2uZaA9h6_nibYlk6YjLc0kqrCmiAVtRrHW74G3AibSWPyBNo_H1t550Irb8lA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نیمه نهایی جام‌ جهانی
؛ شماتیک ترکیب دو تیم ملی انگلیس
🆚
آرژانتین؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/persiana_Soccer/25790" target="_blank">📅 21:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25789">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BB-F3OfstbJwU9bsLg5qqqGRXX5FDUxj8zOci0e2wPtT35yTFv3NWev5jxIGxxfJyYM1A_d8QJUyrowp0ZCKQ4b5Buta7qhzPNWMAmef8bie2KaEjClD47h1-eqfzi4nEIBHe5Vhg2WI0UqSFX7jKbKoTtVxeLBnIDujEIYqGRy64jvqSA5tICw4kFxAgxc5wZeqo_14oI4EAm1ml7AzubcS8zZfXdK-d8dYaBIcKAjs2yJu8Lg0pIJkx21U_r1UWJNrxgS9ACvhNGUQAfnfAqfUvkmeTqfen09uj7n9ispQ2jo9BtEUZNXBX93tv_LXx96UU3MRi-vdWmVnPfs1KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#فکت؛ تیم ملی اسپانیا با رکورد تیم ملی ایتالیا برای‌طولانی‌‌ترین نوارشکست‌ناپذیری در تاریخ فوتبال ملی مردان برابری کرد. 37 بازی بدون شکست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/persiana_Soccer/25789" target="_blank">📅 20:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25788">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kSJVe8IUBdBNdawenDOcRf0Heh9krbxA2Kacs0jtV9VSZ0iOFMgUmKZHXG5I0gnNvAB7WgAcDo0tckKFDE2nUp1-2_t3SfJZ3VY-3QWb3VA8fRt67EaST1ZFsoFc9ii431D6lwk1WjaV75elybDlwnZpSE_Wn1XghQ63i4W5rOWN29sUWTJUn-7xguQCGNd9nAtFVEovCNAJMQJRxp83mXKXJHkH9PUTWPK5yDfScEE4HyTemRQaXtxlAMnXYnDT_z9lw_sy5ZHQBuRe4eQqzXnbRzfLWnQ5slTlBluRy5hpPaq-yOMpb6J061mFozMYPOSCGZ9qIAsGyodJh7HdsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لئو مسی در نیمه‌نهایی‌های جام جهانی:
دو بازی، یک‌گل،یک‌پاس‌گل،یک‌برد، یک تساوی؛ هر بار که‌ مسی به‌نیمه‌نهایی‌جام‌جهانی رسیده موفق‌شده راهی فینال شود؛ این اتفاق تاکنون دو بار براش رخ داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/25788" target="_blank">📅 20:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25787">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b4c95cb5f.mp4?token=gRFpzwIzZM4RxPRl4UdhMG-Y5SnPPgd5zJJguyx7cIFG8duIemGdPoVsxpbutHw7UATqag4He-gOvRDsNt5XyqTabaJUKnc4FHUOO0rtQkHPE_kTTpYJYpTg8a_fEu0TWueujmx4D6AnH7B8nhJv3d1Al4n8s0_g7yKmpFYwB9G5GhPHA9_ZhfXHLeANufZj-T1WAazWjp--vwJWJHG-3X0rXjrt1azhC5QU7R8xOME-R5UG1HRBvUfitumdPIrTgDP9Z9tfKutOK2aIGhdKR2KIDsN4-Gk2AvNy0QsabcP_OQrck-x8MLdjUm1nGZAtYf47ipZOJiNnYapvzTo2xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b4c95cb5f.mp4?token=gRFpzwIzZM4RxPRl4UdhMG-Y5SnPPgd5zJJguyx7cIFG8duIemGdPoVsxpbutHw7UATqag4He-gOvRDsNt5XyqTabaJUKnc4FHUOO0rtQkHPE_kTTpYJYpTg8a_fEu0TWueujmx4D6AnH7B8nhJv3d1Al4n8s0_g7yKmpFYwB9G5GhPHA9_ZhfXHLeANufZj-T1WAazWjp--vwJWJHG-3X0rXjrt1azhC5QU7R8xOME-R5UG1HRBvUfitumdPIrTgDP9Z9tfKutOK2aIGhdKR2KIDsN4-Gk2AvNy0QsabcP_OQrck-x8MLdjUm1nGZAtYf47ipZOJiNnYapvzTo2xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇭🇷
چالش ترند این روز های اینستاگرام این بار با آنا ماریا مارکوویچ ستاره تیم‌ملی‌کرواسی با خواهرش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/persiana_Soccer/25787" target="_blank">📅 20:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25786">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sUNo-ttyVjLvGfVYFn1e0camMucDES_qLgOndyUqAfMCKJgl4aQEM2F68YjT0GAUoBqcqWRAj3ntkwK4lrV4UfUiDVn9wgWn9KR02DSydRXrujdgLmIIepC7Mqqgu4Zrh2AG4QPxSFQlL3OA94Si8feEHXXKYhCWaCni4NI4jktYxTDl2Jdqmn32tMLCmCp6UvRX1NKx0iYaXgzBMMJtX_pgJ6WT5sl6zAGd3zwiXb-mJxcYYYelE-XGd03gEF8RyfDNL2dXos0EkbcoCAA4TyBfB3lq_v8g_-inUymMCwEimyAd5lq_UjCCVZVpARDnxxlwoJ6tj_b2d6gQ-oOX5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
— آرژانتین
🇦🇷
🚨
۵۰۰ دلار جایزه + ۱ گیگ اینترنت یک‌ماهه برای همه پیش‌بینی‌های صحیح
نتیجه بازی را تا قبل از شروع مسابقه ثبت کن.
🏆
مبلغ ۵۰۰ دلار بین برندگان تقسیم می‌شود.
📶
هر برنده یک گیگ اینترنت یک‌ماهه هم دریافت می‌کند.
🎁
جوایز به‌صورت
FreeBet
پرداخت می‌شود.
👇
ثبت پیش‌بینی:
https://t.me/betegram_bot?start=p8_r4EF37DCE</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/persiana_Soccer/25786" target="_blank">📅 20:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25785">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jgzhJJ8U6P0klz_QtszAjNu_IF_p2I4q4UeZBj57u4gHRAGkSpywXgGKDBFmAOVpDVLO2zo5UpTC7SOzQksp4uJTj3WfQueAvStDSnXm_O7PmXcjrxE5mvlLEEhWixO9JLgFl50DNtx8bXRPKRTLPfn_qDTKq445r4uL4SfW1zeteJNVDsL0ErqS3Lc8DI-boxPQL6wkGPKk0dMYSjdw84vh5gbTXgH-xJzCRguaJY-IjeosPRaUn8FGU3h0sd-AnQ6Mop0tZaq7cKzCwDURjjfQyYJw7yy2zODrsN-_fFj0elWzA-Ln1QgU-rboWab-KQ8hEmFc7X5VAfLj4csTsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
علی‌دایی‌ و کریم‌ باقری دوتااز اسطوره‌های بزرگ فوتبال ایران مهمون ویژه‌برنامه امشب عادل هستند. ویدیو کامل برنامه رو در پایان این گفتگو میزاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/persiana_Soccer/25785" target="_blank">📅 20:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25784">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sz1VgjnzTYZlBd9ZVrWgWVShn7_w4gkTlXrpdCO-jYOhlvcGwRXLS9iIwLB2zP11jyihWbPINdATn7SX2PZ3cVRlMm7Cxmi2ABrTRUHmwAwi6yH0uCa2NAXkLgWQ9vVB7GJ_wkFd0SR0sfZox6R2AK4zW5V_WTizSV-5lt6mmyZm4QHCJXv4m30zOaKMPq2v0nFLRK9TRGpTsQT2tnZHBPfqxN4zpPHeg06og7QxGE7q9_hpdQt71yj7LXe-smMnTUNe50z85LhfLQ78IfANTXc3eN7LUpUZcPC6Vm7cHzBrIjvRnaYyExpxu2uU54ZyY5ldPOdDHFl9Czf4_tbBhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سرویس برگ‌ریزون بازیکن جوان تیم ملی والیبال در بازی امروز مقابل تیم ملی اوکراین؛ خودشم فهمید خرابکاری کرده زد زیرخنده؛ اشکال نداره این همشون 17 18 سالشونه جوونن. اونیکه تو 33 سالگی و اوج فوتبالش مفت پنالتی خراب میکنه اون درد داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/persiana_Soccer/25784" target="_blank">📅 20:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25783">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_YEOQW4R6G8zz00w1FNI_ErnKY38hTodgz-Yji5g-ep3eIa6oerSlUSS4MYpa0PydOPrrlRTnrmoK8iqhVHo-P8aCStnf5d4kRXzzIFU_nLu3kryWFBRF97-URaGBcXUSR2bCaa6UgkU_wQ7Kso9m-L4Xp6BOWLKBxaCnt45o-BoMPEp4kyiasChPTJ2-DSaLM6b3GnEM5rSz-pT8k50VCKLhApt-tZIMamgzcMNjMhU8dZyeL7yrAHy7mG4PhEHGXiLweKyvSjD2akyrLSed0fHqYwKyMGy_Ys46uoupEmFwypyxhuxM0sv0xoWL33TnH8mOxBVVstHU3KHAKN8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
واکنش جالب ابوطالب به انتخاب بیژن مرتضوی بعنوان خواننده بین دو نیمه بازی فینال جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/25783" target="_blank">📅 20:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25782">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87ed733fb0.mp4?token=rZ8c5QieMUm0HBt-DK0VwPDh_WhDkuxP_VaQjHD3U0PF7L7GIFnJfkXUTr_bS4zcSWqkQS3K0A8X3BBQJrL9p6jiAAeXn_ua5MJwNu96BKqH4Pdnr6nDnqzfJ6aMV6WpFNMPfIM11Zne61dhlebPfS-45_W_SX52nQAdIU1M9DNNKxnChInLGZWGz83RiIvzg_TjfgqB6PutziWUOl94IU-CSegj-Pha6k-0Imx-IcxIiSW8I8UcMvHBpXhNYWu94Ee8z8K6ymVv9javgtg9Dn12FQRq5lC2NMGjtmqT4j2QGOoI0CsjnVTN7D4uwABTDqLRlQIpCvRwGZ--yMIV_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87ed733fb0.mp4?token=rZ8c5QieMUm0HBt-DK0VwPDh_WhDkuxP_VaQjHD3U0PF7L7GIFnJfkXUTr_bS4zcSWqkQS3K0A8X3BBQJrL9p6jiAAeXn_ua5MJwNu96BKqH4Pdnr6nDnqzfJ6aMV6WpFNMPfIM11Zne61dhlebPfS-45_W_SX52nQAdIU1M9DNNKxnChInLGZWGz83RiIvzg_TjfgqB6PutziWUOl94IU-CSegj-Pha6k-0Imx-IcxIiSW8I8UcMvHBpXhNYWu94Ee8z8K6ymVv9javgtg9Dn12FQRq5lC2NMGjtmqT4j2QGOoI0CsjnVTN7D4uwABTDqLRlQIpCvRwGZ--yMIV_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه بازی‌های تیم‌ملی‌والیبال+جدول رده بندی لیگ ملت‌های والیبال قبل از شروع هفته سوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/25782" target="_blank">📅 19:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25781">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a5e427ee9.mp4?token=nxePHNwwlJQXYsVuU8HWp3klrMFIhQh18b1cZtu8eYAYkEjbfipHhBp--bSz0eA2GjQPw-wdeBDTGfFu5HXJcvj1FjR6PA46m-JehS9dFKq0iArYZvWqxiSZOKYKGOh9d-XJG0k1WrNL2ab7AFglATbOPBRtAvH6YDZhfCY07JPkOlVPxTvmZdSRWoIgoV94UMyZF7jR3LSKypzch9tg5Hh2C5s5lTFGAvwEpCVIbl53aHRTnfvB1ZqD6Ca4RVr5mQG6GgLMdnqWWhw54kxBkX31cnfQ2h1HJ0ki67CpqFKyWKaXolOEoJVifd6t7Jg6AeJKilUba8BwjuwsfwfCnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a5e427ee9.mp4?token=nxePHNwwlJQXYsVuU8HWp3klrMFIhQh18b1cZtu8eYAYkEjbfipHhBp--bSz0eA2GjQPw-wdeBDTGfFu5HXJcvj1FjR6PA46m-JehS9dFKq0iArYZvWqxiSZOKYKGOh9d-XJG0k1WrNL2ab7AFglATbOPBRtAvH6YDZhfCY07JPkOlVPxTvmZdSRWoIgoV94UMyZF7jR3LSKypzch9tg5Hh2C5s5lTFGAvwEpCVIbl53aHRTnfvB1ZqD6Ca4RVr5mQG6GgLMdnqWWhw54kxBkX31cnfQ2h1HJ0ki67CpqFKyWKaXolOEoJVifd6t7Jg6AeJKilUba8BwjuwsfwfCnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویدیوزیبا از حضوراسطوره‌های تاریخ اسپانیا در حاشیه دیدار شب گذشته دوتیم اسپانیا
🆚
فرانسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/25781" target="_blank">📅 19:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25780">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f78ae3e4c.mp4?token=cLlk2bKYJdQs8jbw8q-LHWviHmxe_n-D1m2uO6c2klyGBUk1bpPP9tyyNqMfDlmihFmd4UFYa9GVNxo6ra7Qhckl9SmQYsZvAP9J4lCbajfA5snn8PWYcIAtXh-HjK-y_5KSG9oa4ChzYE49HTT0GLzMXHsrbs9pIcWMUQEhBDoK6aEEi3UZxzxseJTUYs9wnc1LuXor9xZTFU5mWYE-9iSafy4C-ogVX-I2HIb9FVeRb2M3ojynmLPwYehhWzjsEISIrq0qrRJvUgWg5w4Nd-82yP_HowVld1ZgYt_89WM66lLB-nG2vdS5fWmGQjaGSNDyYWPioFN7TU-xHMMQ9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f78ae3e4c.mp4?token=cLlk2bKYJdQs8jbw8q-LHWviHmxe_n-D1m2uO6c2klyGBUk1bpPP9tyyNqMfDlmihFmd4UFYa9GVNxo6ra7Qhckl9SmQYsZvAP9J4lCbajfA5snn8PWYcIAtXh-HjK-y_5KSG9oa4ChzYE49HTT0GLzMXHsrbs9pIcWMUQEhBDoK6aEEi3UZxzxseJTUYs9wnc1LuXor9xZTFU5mWYE-9iSafy4C-ogVX-I2HIb9FVeRb2M3ojynmLPwYehhWzjsEISIrq0qrRJvUgWg5w4Nd-82yP_HowVld1ZgYt_89WM66lLB-nG2vdS5fWmGQjaGSNDyYWPioFN7TU-xHMMQ9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
#نوستالژی
؛ یک زمانی میلان تیم نبود مجموعه از سوپر استارهایی بود که همه جام ها رو میبردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/25780" target="_blank">📅 19:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25778">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RoX4Jh0IkGo6VKuVOI3FHFMtPLR-gjH7MvU5o-Ts9ekHY0uDEH1GBWwP-ctxCxDUu8bJ2_MCSj2xqEe5lCLmgp9zw9dbNLBrYNn661sl-JzPzYgHN9Ufr-NxxB6jVTkaplvVOeLzOd2Q-T7OZnytri1g4zdIa6ptr7HAB1s8t-RayMlA4UlwOMvRoHWsWRkxZ-fqJVb6F0aTLrsRKstwyEZldRz0mINQTCxkdy9l_u__P17752-xazBGJsa94QHZaPXgGHM_sieAtyMbtIrBAFHxQUYtWkt7LGVI3CvP56aYp400HcA1tQCokzZIWe407u4j9MvRoKeq53Dvwyt78g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r-f8BESUnPFVEorN_FGGR_JzEtM9jIrVF75IQ8ewrlxnT5en8zo4Y_Xl0WSWxapDVNy_fNQ_kQdkUgPnk54fjygMCor9Q6ExDlC-sGuuLV84km7-EkVGDBdcokbCk-UES9Xe6oycdO3UHPVxNJ6yWGU53a0vEl3n7_S_3trsaBx7-HOVKmPkCtlB-aXsxrfymH6H2DAn9ODQ2srBl25topB0PHw4PjRNtdnYYWJpwdi3O3GJ-AtrYXSbf4nCBAJ9_U_J6jxC8_Cwgl3g1xljDFmiFAzKdcbwYcWXF9XDMAuiSy_Lj0wlDrJ9YdwOl-HLqpRz4IKy3OYLfLDagQ3c-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
👤
مدل موهای جدید مهدی قایدی ستاره ملی پوش النصر امارات؛ اماراتی‌ها رقم فروش ستاره ایرانی‌اش را 3 میلیون‌دلار اعلام کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/25778" target="_blank">📅 19:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25777">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cS5-wcs8Lib8dOEBIp4ggO4swlfMcWtMqQe8-pZA0xtTxFb-6-T7ykJQFoulY-_i9s9ARXy3xY728aNqfCAFDzOps8NQrs-3UvALDq9zaXCLL7K2hg6WdXZv_KSmPapDhWLJv7acXHEtYjsr73RNFEMyN7U1GsDe93MDzP7xdOYq5JmmV_Ph77Oit_a1gJ3xWJ4P1T4cb8GdHcqbNwvKIv7RoBIt4bRAD9LPl0dLQXyg2-DLUCCq42wajmILawZypvWvwJ4dEicIQwkPmA4ChhpnTKcC5g9fypDr7u-mJYKp6EwqLQFZdxKRUruJ4jCm62shr43jr8Vd54bTxCznSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها دیدار مهم امروز؛ جدال تماشایی انگلیسی‌ها برابر یاران لئو مسی درنیمه‌نهایی جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/25777" target="_blank">📅 19:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25776">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tsRkYQjdCm0RQsQjDb5vBBAYixARnoeQSfThGdseyDddwwWoyRPsd6bumQpRXb0aU4ZR-ldTClOI3qI8Ba68Ni_xU5oSayEpHfFhS2h6IvHYRvOllOL0sXJYC6fedhR8-OfFXhfzgwoFZ1PRiej65G8kkxJLIuqXYL6cfYT9VeaiA6PDKqPaz3A_CRlatA6DT_TqQ7i3JAfYP1iaK2f7mdoUNiEcG2xj6Fk7SVQLppXI1nM1960OD13S5OAAwZE4LlTPDMNQ_-EYR0ZdfZ2uScJ2mNmk-UjPzlttXzWmcZ5tl5wjcsmh6wBBRYP576nfqFqCH-kjud-3gEUe8N4G9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ سانتی‌آئونا: باشگاه رئال مادرید اماده است هزینه بسیار هنگفتی برای جذب مایکل اولیسه بکنه. بایرنی‌ها به‌احتمال‌فراوان با 220 میلیون یورو موافقت خود را با فروس اولیسه خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/25776" target="_blank">📅 18:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25775">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/isACpuYeNbFIh0kK1qIA9gvDWehlCkP-WZjE0XgRZEzDyDW4s_WtVjHgoAm9hq-a_5v347hIbnKSIjbkLsJhgCp20UTORSpWfMQU9b-N_rUeuKgTxvZY74SOrMStg2Z48OGlAO_pMH5taMLguN-Qb4ZaKqvPwarSoYaFTwxjvWY2I8v_xmK2IbJOJqrqBYfE2jxYU1KzPnJmCM44I5blTnjjIdAU507WTLdyGBxo-LxTvwl0ydcZQ2vNQmTyhxkw5WkABHf2HKgVlx480EzG74IaibfEXJgdSCK_2D8lBVAvLQx-ovO2kJYoKY4Blxok97kc6yvUOHd6vDjem7oo4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
👤
طبق‌‌اخبار دریافتی‌‌پرشیانا؛ احسان حاج‌ صفی قراردادش‌روبه‌مدت 1+1 فصل دیگر با سپاهان تمدید کرد و تا 38 سالگی در این تیم خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/25775" target="_blank">📅 18:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25774">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/urlZd5TZMgYSGIGTUmd_VCqwha8rxEf58HMVc0PXcMp0DlRLQMTCk2hB2E-sAoFVt9WdAn1-Io07Q-qyiQ23hW_gOWeCHWljft-Dn4ArVvt2rxYRqnLATHbZFYRjvFEh7LjmyiMwKO6_w2ZRT9k-yj7zOvOczoxsQ_15wgSKfIcjptI-bdZgYr0ZbfL4qWvaAHf8zDiLllmGqCsSR7tnmnp_xZyv6aLwxpNycEAh4LMxLxpaHFb8KLQGc4Pm-GmqofWG5_XMNAKWoF1RwVfaZnauwg7OkiCOa3WIrU60abYCjY59rF5RC4RyVnCs-cXDpXYTaXPAIDnGKt27r9wzGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
#فوری؛ سانتی آئونا: مایکل اولیسه می‌خواد درهمین تابستان به رئال مادرید بره و این موضوع رو نماینده او به مدیران‌باشگاه بایرن مونیخ اطلاع داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/25774" target="_blank">📅 18:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25773">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lvIlWO5eB03H3KzkqBZCS5fEaZLaJPcSYSguABjoz_gMPPsWSpmgbA0T-U0oHFPzOR2RRRBfm6r6C5vplxHIyWUhMa5xCSO4g5rlNYluEix84oefenBk0rhxXkQjWWQzWFUtcv_RT6AoBf5ipDF1Ex-4taWrRMqaiBMV1yx7AWSDrgTf0YazFOdb0Z8uA-qunfK2twYqPJYbBtZnzotfSUDRz90gbR0__4hDgXIlJHXX_21VpOzTjtNwd3g9KHQ49JvKTfdwX9cV6Xre6H0Jb6Dmr4sdCQ3SbHl8p0AIsYQfPYxmRWuy5C-zcCTlCYp_nYx-Rk_qssg5v0cKTXDqmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
بازی فوووق جذاااااب
انگلیس
و
آرژانتین
رو با آپشن های تخصصی در
MelBe
t پیشبینی کنید!
💵
امکان شارژ
کارت بکارت
و
هات ووچر
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
🌐
دانلود مستقیم اپلیکیشن اندروید
🤝
اسپانسر رسمی جام جهانی
🇮🇷
پشتیبانی از زبان فارسی
✍️
حرفه‌ای، مطمئن و درکلاس‌جهانی پیشبینی کنید!
برای ورود بسایت‌فیلترشکن خود را خاموش کنید!
‌
🌐
Link
🔜
MelBet1.net
🌐
‌
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/25773" target="_blank">📅 18:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25772">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KvZsLVeSkpxrnPe4168BmNhxlIFksHreVTxvTWdRTWXOI_nEehNYZu07GDKGlTQIYOeY01NRMLCE70A3Kd6LWN8qeG8x91-OHkViM9k31VL7b_jxnvlebGbnq52v_AZNxfmOQvNzZUv0qNygbpRcB6gdfED-2P2E0P-miUtTeaygUMlLNSU7w_3oP1Ga7rZTiODJDWpHXBjTM-FytBjL2EbCQ8z-5DFui1W0iIA1XvtcMCRNrSc-vArZiwdYHJTUihrKCdoafq6uSZvlrIXYyUok94XcimmZsdngzVzdRDzUgHSUlVMy5KrupVu3BJwprJttF4pVgS1Vxx1jOpgHKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
فابریس هاوکینز: مایکل اولیسه پس از جام جهانی دربارهٔ آینده‌اش بابایرن‌مونیخ گفت‌وگو خواهد کرد. اگر آفری‌بالای ۲۰۰ میلیون یورو برای اولیسه ارائه شود ردکردن آن برای بایرنی‌ها سخت خواهد بود. پرز رویای حضور اولیسه در رئال مادرید را در سر دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/25772" target="_blank">📅 18:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25771">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ayabq7mACFTNWoXuw-ia_Rv7QgIA_bbOBf3iRRy3n65EvnDC2OPdt46LBpqwu_gLjjVbdW9jv9qHN9gvuQ3HBb_Xh2gXKtEm1vVfJ4OkqwUYLUCx5re3b2wdabV696-nKyPSg4wYvtpOj8S8d5HlieJbPkbT6F84PSLYo4agX-IDyfafSgHw8SYhqAExe0GlZXCkaQSMwuG47iFL4qRbZbpNOT0UfXto5t-8n_WXNgRLn69tuaSKVnSk-c9ph55HniKggQtzSL976IiWU7GsAzNbzJgEhsjzF2RhdhKzkawOMAZLc_QryJEKfdZ9_r8BOW-5PtwhbbUiWSPfmWDDHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درحالی استقلال پنجره‌اش بسته و دوفوق ستاره فصل قبل‌خود یعنی یاسرآسانی و منیر الحدادی رو از دست داد که فصل آینده نماینده ایران در لیگ نخبگان آسیا خواهد بود. کار بختیاری زاده سخت بود سخت تر هم شد. ممکنه حتی بختیاری زاده استعفا بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/25771" target="_blank">📅 18:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25770">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qM9YqYLXkaElqMTmpsqVh_cka2oGjO9Snwew6Pl8y5HVpyfYcR7L82J01YryHVKQvBmffjYacXgXpA_VJXb3UZH8Nn6O9Zc5V3rUQ4_SVRN-Uxzn6uSnIrd1dcy76cJQOhNL3jlFrP7FYlgDiQDNK7cjpkFUEBUOE52TDloNNKSkjV2_B01P343ffOFsLdNLN4rZzKnXm_xkiCcWmAAw9R5KwiQDE7kqiFhuFCirbKoToZBzEXirX02d6Yu6US9UrrKxMtvLCZXkn8GmKMfMUemEFlf_u3usdzHD_4PsLE1-ThqMch53zvDxGPSgbYFEBnhFFxgHHNJxzwqipa4TKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیشب‌بعداز بازی فرانسه و اسپانیا درنیمه نهایی جام جهانی؛ خونه یامال تو بارسلون مورد حمله قرار گرفته. دزدهاداشتن‌از دیوار بالا میرفتن که نیروهای امنیتی بارسلون متوجه‌شدن‌وجلو دزدی‌رو گرفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/25770" target="_blank">📅 17:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25769">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UtVxvLonZIV1GrpWAetpdY59LI8F_hV7Zg3NQl_ALolPTggS2R-S_kQSOmJFi_6VuN2Gi2Z_jmx6zM4hWyksR3BFfF72L7qitRl1y5lysj-fFXL77autWfiavHlqk2oLTs4Vk2byeK_P_CYiQucVnYRwoY29WI0lWXFMyYucO8YHt14MAYmU2MiQfyxjp3kVvZmPqTm8jHqQAp7RsHnnMZSi9jWtlfYt8uKdgPmL71y3WSmxe-9aiizWB7KXB3WGHnnKGDCM3p8TCXQJoILmf3vCxlIxnksHiPRKRv-UGYYH2XQa7d2aIfHGT3E8XexZPmmYXCFfPc77MV36B2F28Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ بعد از باشگاه‌‌تراکتورتبریز؛مدیریت‌باشگاه‌ پرسپولیس نیز با ایجنت ایرانی یاسر آسانی ستاره سابق تیم استقلال تماس گرفته و از او خواسته که یاسر آسانی رو برای پیوستن به پرسپولیس راضی کند. حدادی به ایجنت آسانی اعلام کرده حاضره اون رقمی…</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25769" target="_blank">📅 17:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25768">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NEK6Zkbd32dcADu4f2S3R0POHpIcgTu2aHiv0O02Sc9jFtFfG8kSRKNMy7OxxHeRBQJ4uT3-qmf_I9eVZ6oreESiWJB5ahmYeE-uoQ4QY04QbWwxPM2vVuFYVk1cDsSuydvUA2U485XFWqanXGdvER83G4cq8jzTOvzN4XB_JX-EbRyhlQs-5Dfyn9M3RrbH1vMiS4wgnqkj29Bb1QA3Cp7hWLLpgTEvPNsFrjrOQsGGvSs2X9gmQ6BZiV2_IM9ECkGwdCcjI9khGm1bp7q8-vRRVdWZ11v3B1KWYfuEbTgociaUXKbP-4-H2rrLYhIQiE3njl7f5rIdLph59QpfZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های بلژیکی مدعی شدند که جرمی دوکو ستاره تیم ملی این کشور دیدار فرداشب مقابل تیم ایران در هفته دوم جام جهانی رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/25768" target="_blank">📅 16:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25767">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dq_Ta0GdY-X7eXcci6-kFo7h88w_eAXREQnjODnp9P-3POIcCHQj1yd3qRme5y9oOy9h48GgQb3MSnrtkBf6LMHRuO5vjuuyBjs9yS9-lYMUCXLRQOzGtg-nvRI7jiH3PbeO2_EB5kheppA1dLc_fHmQxTbvI9LVQtlOdy47Li_UwGVywn_Avwj4anyHeUS2Cy23FjGWEmrjWuAAz0mKKIsgH-c3VbfSws80RbZ2VqbrFgaN5djvnk_HrC_ACYiWYr_pXK-1Eq5sdxE6dS7PCFEXTgrC2yfrQUUCNnlmpyyfTNzCiCfIhU0YUYC5SrxudccgCUz4zeCHBvbaw_xyqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌ های قطری:
باشگاه الغرافه قطر به دنبال جذب منیز الحدادی ستاره سابق بارسلونا و استقلاله و مذاکرات رو با نماینده او آغاز کرده است. علاوه بر الغرافه یک باشگاه مراکشی دیگر دنبال جذب منیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25767" target="_blank">📅 16:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25765">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb986dc0f7.mp4?token=U87LHwnNizeuU5hNCWaP9GyTi5Qme0xVb3mmeDMVei2YtGSfRY1HUaMbFwtSOcveBJEzqHBPBCcMg8RL_hGcE37tYAiTy2uDCUeNXBmqHCLEcfKZ-IKsL9L6xl9m3CGO7E7llDMJMLhR5p5RupsaLMa6-DnJsuwcLxma3y295B-FHBNIEP9a5TbtTZNR4MT2v1I5ecao-mxdzdr1JQCk67MZXc6MM9DwzUrwSlkGek6_Y3lShQFpqO8vaxOckCRqmiSvO9llRKyH76M-ssmFVBK6Ujg-vynwYUCmOAqTFaIdcGERddUKEJIV_KqBkGMnpXhNqSIXUxG3sxhAbvEFAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb986dc0f7.mp4?token=U87LHwnNizeuU5hNCWaP9GyTi5Qme0xVb3mmeDMVei2YtGSfRY1HUaMbFwtSOcveBJEzqHBPBCcMg8RL_hGcE37tYAiTy2uDCUeNXBmqHCLEcfKZ-IKsL9L6xl9m3CGO7E7llDMJMLhR5p5RupsaLMa6-DnJsuwcLxma3y295B-FHBNIEP9a5TbtTZNR4MT2v1I5ecao-mxdzdr1JQCk67MZXc6MM9DwzUrwSlkGek6_Y3lShQFpqO8vaxOckCRqmiSvO9llRKyH76M-ssmFVBK6Ujg-vynwYUCmOAqTFaIdcGERddUKEJIV_KqBkGMnpXhNqSIXUxG3sxhAbvEFAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخرین‌آرزویی‌که مادر عمو پورنگ داشت. فقط اونجا که میگه بالاخره‌آوردمت. عمو شما بلیت بهشت رو با همین نوکری کردن مادرت گرفتی خدا بهت صبر بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25765" target="_blank">📅 16:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25764">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K51F02mwc8Z_xeej-_UgelMRlRZqDQSDGjsNE_lrYoLEW_wa1asZ_INk_HgGtUE7ucN78hvWyTpgugfZrOOkNF4artP338Eaveiu-fqbTkp9YR81T8a6njjN1RjrjEQkQcVDxJE1-Rvz-bh0Lc0uAzhudD7UPKOuJTJf9h07RRGy88vwBsKFWiB-YXOd5NSRh_vGJ2Bsu_F9Ik-X_7K9PYsht8KSVSDkmCgYqmympGV6SsSfJsuk9HCe8JArU2soAXAiIobPvA_o-u2e6QipiiT4KhFc2cU4xKdnqKVG-UbQFARB2jcA5tNK-ChXZirw9E7yFzf-K7iruq1NuRYIOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
بااعلام باشگاه فجر سپاسی؛ فیروز قربانی سرمربی جوان‌ونسبتاموفق‌ شیرازی‌ها از این باشگاه جدا شد. بر سر مسائل مالی به توافق نرسیده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/25764" target="_blank">📅 16:08 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25763">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QU57pACMKpoGNoBP6pAufRqCeSiI1b3s9Pj9YNJ-apaVhzUb5uTyU6M8PnL7OkFWcCIrrqB676-RsVB-cEYiLzs60V1ZGSgpEvoJlGNYKtPxIvE8mNkrxoCJULl412_aYhJu_neS2hLr8zEwnbdVFyw2fPMRQulqw8qgRZuQG5NPV5aq2C8ys9gPyocUCI0vtD_e7F8F_H2jv87V7xrmyfmVyNd-q0aq5AF9RH8UHQgn2WmH3QcPVAZbaN01tQ2PWFEu7dpEgnCRJaBbTJG5yvlPKY_8aMuyUs93f0eIgkHWD1_4Dbfk9hbSQLWDbCdZ12_fhs3eV3dpXjFtCpNV9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی #اختصاصی‌پرشیانا؛باشگاه تراکتور از شب گذشته با مدیربرنامه یاسر آسانی تماس گرفته و آفر دوساله‌خود را به ستاره 31 ساله سابق استقلال داده است اما برخلاف‌رسانه‌ها توافقی صورت نگرفته است و تراکتوری‌ها منتظر پاسخ نهایی آسانی هستند. ولی پیشنهاد مالی خیلی…</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/persiana_Soccer/25763" target="_blank">📅 15:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25762">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dgnsgfoWcxU1x7QITyTLl20T4rRAF9Hp-PRlWIt9Bw3-tgJpyf77drBQvoTod_9tT-ohTJZKbmbM5KRoZwMPEetJCzIonslXO4rYHhmkS2jvJIgm7RpX0UXhkilQsHkYFcimv39c3sBXJtvHp92iAE-k9XTl8BPv74bXdwuZtTAd8JRVMW8SBItvUMn8x1ZoT6zPiYe888OWIgAdbfLQEn-2dOm2PwX-UQhA2lc91AYx53a9CbZRR2096gTtNwbZhl991Kc3soZj1D52wAPZprnSKe4SrGJP7IDx5uT29QyKu2rC5WtDha7UdY732PVKxbSSa6VHRu9NkYqq7-xGiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی #اختصاصی‌پرشیانا؛باشگاه تراکتور از شب گذشته با مدیربرنامه یاسر آسانی تماس گرفته و آفر دوساله‌خود را به ستاره 31 ساله سابق استقلال داده است اما برخلاف‌رسانه‌ها توافقی صورت نگرفته است و تراکتوری‌ها منتظر پاسخ نهایی آسانی هستند. ولی پیشنهاد مالی خیلی…</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/persiana_Soccer/25762" target="_blank">📅 15:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25761">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33fde3599e.mp4?token=qC6M1S5EXV98JNhuK878Rx9t1OBkY0kp4Tovfm4fCkDkNs4bB4LHYa0rPzmaP26anEyFt-fMYcIvJsCmSNKZCMUAvbTMWj4ELeS6OnTQdp02SB-och_5XVYK2-6ZkEHPiDyJy8LBD8z-cj-fPb7ZiSaGKFCvarTmLNHyr1ZW89jgCJlpnQMhgtOL8d1oDGZLT_e-_VT59Ded2Yxbc49FofPzEc_XCtPtM93CJkDWTRWA-0-wS0-dNknRspjs19JDp8j8JyQcW2clBwzVjiu5gkOIyrsPZMLrHJp58BQsJ4sbyaByabXiT4YQ2c1iNSVqgHtPNFwRfS86Y0UlmkzxLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33fde3599e.mp4?token=qC6M1S5EXV98JNhuK878Rx9t1OBkY0kp4Tovfm4fCkDkNs4bB4LHYa0rPzmaP26anEyFt-fMYcIvJsCmSNKZCMUAvbTMWj4ELeS6OnTQdp02SB-och_5XVYK2-6ZkEHPiDyJy8LBD8z-cj-fPb7ZiSaGKFCvarTmLNHyr1ZW89jgCJlpnQMhgtOL8d1oDGZLT_e-_VT59Ded2Yxbc49FofPzEc_XCtPtM93CJkDWTRWA-0-wS0-dNknRspjs19JDp8j8JyQcW2clBwzVjiu5gkOIyrsPZMLrHJp58BQsJ4sbyaByabXiT4YQ2c1iNSVqgHtPNFwRfS86Y0UlmkzxLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
حماسه‌ای دیگر از جواد خیابانی در ویژه برنامه دیشب جام‌جهانی؛ از خداداد سوال میپرسه نمیزاره حرفش تموم بشه دوباره یه سوال دیگه میپرسه:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/persiana_Soccer/25761" target="_blank">📅 15:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25760">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GMmek5x1ahWyLjnmHYz6zYDGlz_h1eCw8Sh59NWBqeXqXxf1O1ouYY8IkroLHHqMNbraJ4aDhaBNSQ2ObscDiGdtTsW7xP4i9I4Ge7Qrcp0SwM1J0SrMg_rMhSg3aXcfcVKDRfpLmIO7C4lz1UVm2XgH5vgHMCZJEJHk-yViZdm4Mml2Y3gAKyhhzZUZnKFWiXCWtWTDkfraLXjFhW0g_RzYm77CZmS8kvr-izY37EQceSrqz3Mes8V3Lz-a7HhhrSAGlPyS0HRdJRS8Y4PI0VsmFsZZH1Qpk-huKhFj0f-NzSd8GP_UGQIlsLPhSP8YWStaS1Aue8f2a5JO7-xyNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🤩
#نقل‌انتقالات
|اسپورت:
سران اتلتیکو بدنبال جذب رونالد آرائوخو مدافع 27 ساله بارسلونا هستند. مذاکرات باشگاه با نماینده آرائوخو آغاز شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25760" target="_blank">📅 15:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25759">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bSISFbQpxyYkarBuhJ9k_gK0Y9xA-trOgdhAQMROS3x5_lzxiAWPPHuzGgbv_aAvookmmDUvlWhchdpIzTl8OKPaLi-zNf670EhjfqNwuNUWJr-A9HWogu76Zfm2G98UzWj7X7D3_2tLhNPW7TTkYgAS_WFInsXUmFF1qL6J5e7i8sH5cb97FcQrzmTa1Q4YIxn_6AyRMevaePR7Fs9AD_HS-IBKy0G4fKjc5BhiFYve7Fwt_rhIj6sI56uzENEDHNzC0uJPuPVNyJ3l8UEMcK7Uejo8Fk-0pLGSlGnu9w0QtfwyqqCHtMu6370Dv6fTT6G9Xcgg9BijF32d0u0KPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/25759" target="_blank">📅 15:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25757">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LfRuLGO0JeZnLBQxkHU2DBhHn7U4HM5CjctDenbT-HQJ_4t3NaUle7OHYoYY14QEGsHPg8lKKTzbje9g9RtaK1TnhJLIyWwnn4WktU3uVLo49hUoy_8Bf5eKv873uqPQQ3Xdu8sHLhJvDIJY_xT3aOR9wUMyH5MxrKu6qZCRUQvjdSbIxvMDi5HQfRCbmdp7ytQCiKvhwciap1qXhPeCrlDtiZfq4fR3uUeuQg36cPz7zo3gjIxZRo7lTvsa8wMBpYuA_9WGPYqMZwiLI24kN9wqKqt9v5iMZoO7UzFaEDIx-dAb0FFVtRrKV17j9oHJVKSgEzSUT0PSj_XQmqUn1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق‌ پیگیری‌ های‌ ما از ایجنت ستاره‌ سابق استقلال؛ قرارداد فصل‌ آینده یاسر آسانی 1.2 میلیون‌‌دلاربوده که فوق‌ستاره آبی‌پوشان برای تمدید قراردادش1.5میلیون‌دلار درخواست‌کرده که مدیران استقلال با این درخواست مخالفت کردند و به مدیر برنامه‌ های او اعلام…</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/25757" target="_blank">📅 15:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25756">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYCCDeCYFyYFSdXBIuZJJq6iNjHNI6c_SPU0uBITIVIJmAv4wyngsrHsP_bJcJAlwI5DomkqYORiOc2W6SawKeCJvvOdcoqO_wTsR--bKfYOiSJf1_pEgggzBqeR_SnpGUu9KeI9RiG21bXt2ljw3dPDJ6I1t9O78c3N6ZxrmuPxydUxQfUXd1X2v3y7KCF-X2U7TWvtq9PPfAL0sixy4FMfIRQRwW1p4MlI2z90AytTXhWHQykdvTPwP12EWqrq0vZW_sWn4ZpSlMlfG20OogO5MJMMt9lX_m8tfn6e5n3AvJnyOXE8Q_WsU_alXTbi-7jtS2HOXIrD2vzFOs-xvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نیمکت‌های جام‌جهانی 2026
؛ چه کسی ماند و چه کسی‌رفت؟ از 48تیم‌حاضر درجام جهانی 2026 برخی سرمربیان همچنان هدایت تیم‌های خود را بر عهده دارند و برخی هم از سمت خود کنار رفته اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/25756" target="_blank">📅 14:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25755">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QebI9MWA_hCAdH2KuJaSm-HNGwafsSM_gjnAxN3nsE19jR67XlJItMi1skvQQ7wLAzDNgtB7enxSqq8OxMB1_Qb72Oj4Tg-Z4yHf8fK5Dsmwd-bff21XxFQayfYPDkZa-OyKvpI4kXoNAy409AdbcxugsjjTB7vrF13FP9oB_gw5_NSgk2gcqZDcqpsglbiCU1Pg6TBQzehRrLP3gEKC64a0Cyx1IhHFY-ablNsiMKxXF3UQik2evl5p5htgzHhu_wW5Z8WhUCrKGR4419S79Vh7FHz8aolJKpKfpK1yjkKGA-II2TRbSxAgPCw8nnN-J7tennRo91GzF8-l4wrBaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
همانطور که دیشبم گفتیم؛ سهراب بختیاری زاده قصد داره درصورتیکه تا یک‌هفته اینده وضعیت استقلال سر و سامان نکند از هدایت این تیم استعفا بدهد و این موضوع رو به علی تاجرنیا اعلام کرده. سهراب بختیاری زاده به تاجرنیا گفته با این وضعیت اسفناک آبی‌ها از آسیا استعفا…</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/25755" target="_blank">📅 14:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25754">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FOqFy1edCgLykBW3voRn9QXrLSqr2Ul7HhS7zaBZIb2k8QRdgmd6m8sYcJVtpIWu99uXEhI3Ccjawvl7dBt4JKSJD19oiaFxX-Bev7JqTgsYi8cA3SXf97M1klxoQF2_kXNxvhXHGFpSWRH2nEZxMW7BIdm1_XRj1QhVLsmhv9VKh_HQoyyne7a33DPuTm-bQF7a7VKeTTmIF4Vv5zkUut-B7BoTfmde5lzpvAohYxcpZH9k6dOmV3ytu_bFF2X1GuvHZKpWb4wgMIOKZsJwXrAtPv3sypty4ZLLCat-fssOu8IklE2tL7CY1G0kkrzp7cSgsdDY0N5ZMv_DZ6wXIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
خبرنگارمطرح‌باشگاه شاختار دونتسک پیش بینی کرده آرژانتین میره فینال و اسپانیا قهرمان میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25754" target="_blank">📅 13:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25753">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FbC2EY7pVTRtUjj0ahBNSkXHjPRSIcgTDc20cHBmSNN-EMxVKDFfYIIdb-eSDVFnaxlbXYGlDxzU5mZZXK5ujy7O0R8bPRrg6VEs7dXBdMO4zOhiQNM4h1cK8WaK-gpegCz8-vIx2cl_t7xDMQysG-8GpDs5bAxfJknkp6x0xkEut9jl-C5F8F_W3y2aSlb24YJAjl6WlrMNY30z3ze7u2_DxdySsvG7UwaI2ecn1pih8Hbcq-bkfE6gJ6N5NEX2XVH2ic5jhbIFxKOau8-a7nD2BChYdKaBZsza1jdh2fOr9NdWsaXpdtxlQs5YnpqzJpTIAqbPAYfmGwC9BP7ozA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ممکنه حتی بختیاری زاده استعفا بدهد.</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/25753" target="_blank">📅 13:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25751">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kgfEoj_R7JpJ9_3s-kVmZI2ewJRZ4u6t2rj-pG6CScoUXVzpGtb08Ii1WqOrPvj7D44EcmtUwSwifl71Ei8PRNS_XgRvzRYae3k1qm-JmOnzZHpJlbM_rOKtVLBMwNB90Tc2VSMQMwo5zaYwVpIy7JVubqpF3TfqTaPYuLLlyhnUFI9raovmc7OVKwDVQ0TMJjmkMKfwrWvCgoufb26IfUmJstgorPhK00aNQTMvD2b7qNRfSzn9YgmBVBgXu-_a3DvqAo9zoROA_M5nhHBiVIoEHpcB0U4jrTet0RbcoKeSPG2-sLV8egTVjmtEjRXAh6nKwlHHTNPXc2t9zL5W6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
کمیته استیناف حکم خود را درباره پرونده باشگاه پرسپولیس و علیرضا بیرانوند اعلام کرده که باشگاه‌پرسپولیس موظف‌شد که مبلغ یک میلیارد و دویست میلیون به گلر سابق خود پرداخت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/25751" target="_blank">📅 13:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25750">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K064-hpG3XgZ1IUNnfcfh-t6U4UGpHfOOf9Llpm003OalciA8tWkxaw1MyhAQ9U_zJrsrPAl3b_7F-BfcFSYS32GCr_jP2EqRMVOv8ahk7a6jdVKSh_A5vf7hd8TEuH5vueIG3HgLpuMAeuynvDZVuj_CBBmywWHQ1tFiVoxF0sJXVmI0Dr3Gd8Mr3ay4eYoULCUCYHl6fgfBCs_-otrB4h3D0a7swhhhknI3bjq-Je41XVxmOm2vNd2RYH6NkyLx4heBrKxtUap0q27ta4WsXkD5aH_D1Z_10OfSCRB1pzv5pQoLfJeu9JBQD568Ps3vmW2Q8Hs_7FlWjMBvlB0fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فکت؛ امسال سال‌ خوبی برای دیکتاتورا نبود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25750" target="_blank">📅 12:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25749">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dba39423e.mp4?token=MDO19MFwpmEWE0oa4LcEF6-p8O8hJm3qWlbZq6CQsYI-ouc4Gspi61uUyjk58QKAwEsSaNYX5jqTlh-OI2T5meZuPXDt-HHMoX8hRpnxEpxYVIBam1Abz8bBsOjTUq0Le5m0EPAaG4eYl8Zmx4FhHA79emg0ZzbghzBhFAhZ3IJtzUA3V68U-miJ8cM9RO2f62zwT4Kbx5sHGnW1bwsnadnQesdOlC2320WSu1yV1ZJgb0tg8J3CFtmeadsw4kj-nyq5nyXVSbisPqDj3IQ0pe48-cGnXbnI5y0sK9HoZUnZXWceY8QW0dpnf7gegWcl7vqKeYRXhaBBLEouHmacpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dba39423e.mp4?token=MDO19MFwpmEWE0oa4LcEF6-p8O8hJm3qWlbZq6CQsYI-ouc4Gspi61uUyjk58QKAwEsSaNYX5jqTlh-OI2T5meZuPXDt-HHMoX8hRpnxEpxYVIBam1Abz8bBsOjTUq0Le5m0EPAaG4eYl8Zmx4FhHA79emg0ZzbghzBhFAhZ3IJtzUA3V68U-miJ8cM9RO2f62zwT4Kbx5sHGnW1bwsnadnQesdOlC2320WSu1yV1ZJgb0tg8J3CFtmeadsw4kj-nyq5nyXVSbisPqDj3IQ0pe48-cGnXbnI5y0sK9HoZUnZXWceY8QW0dpnf7gegWcl7vqKeYRXhaBBLEouHmacpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابواطالب حسینی در برنامه دیشب خود خواننده آهنگ‌معروف "جناب‌سروان ولم‌کن" دعوت کرده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/25749" target="_blank">📅 12:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25748">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XlwqncwfG1UJrky0_WFoJN96cGTTCWbedZMoii9XNpsXUwLqymwItGvnMf4kUInBTWiC767FufJBTEdnDv8cV6vchS1qjpcNajtyb_XrkTbcIWrU0AOzLRqIiEcwW4Dpsb74k-jggZtNu6k8maKUTxhS9DXbaGKKFDBS2N9S-ZEu9PpeykXsIp3tteYhS2qLFhVLaw4X7TzefKFNMIPOstXsFqQXO0wNkcoLf_y3IDCLPHVnYkr-Vu9kYTAdSVdFYK1U4LBKCVLZn7A42f1K7WAhYygfS5HH2fmSPdiK-THz_NfQ0ONvwfY3dBVRfS-JsXAB8CxKm3Ngre_FLL5Yzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیران استقلال: آسانی برای ماندن مبلغ جدیدی میخواست که مابااین‌موضوع مخالفت کردیم و رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25748" target="_blank">📅 12:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25747">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/funk4VwP_hP7b53Yodu9s7kLpPQgZano6BBRbO4N0AedgtQUBLehpBB2ug9j1T0uokXNGrMNJxSY5L63UIkZehaJB-th6mq1kMNmYIRS5AsC0a3dHwHZSdCbcFIzoFuvaGN0_1SVxH3zKS6VwvQb5-pZEkIyi69pVGA5n-nldhLI8BE_TniPxiOrWVa_4KrxHSRAIaVi0UUNREg3X4R9PvuqGHJesEkNDkOstMqKguc_N5PWmETty4wcsPIGF-yqwHDeKIuNFNw2F45Hic-nrapFbaRcL9hB7m7TJxIR-YN1w68EkQWFCa_5zHIYjgiupfotOZoD5iCghRY1ZwR_HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آندرس‌اینیستا اسطوره‌بارسلونا درگفتگو با عادل فردوسی‌پور: لیونل مسی بهترین‌بازیکن تاریخه. از او همیشه انتظارات بالاس. لیونل مسی فراتر از کلماته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/25747" target="_blank">📅 11:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25746">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mtMuiqbPndku9qTspn71lBv3KYFuLBDwCc72XCg0t-njDFL7Wksgne74hsgVrhmNOboL8876NbUF9OeyOhmH49WKdrgBuRorBjX1pr6nuds9xjf7WTJcuh3Lppsug7WlExt_jErBDFWV-2zWl3Fz69Ed9O0tTf6z7eWNOh2Q88gFPek_cpCiAGLS5YBQCqNuv0nbf_5x9tZLfESykb7rzDj2qWd09dlz4H8HEwprJWCm9BlM28RcNqb0fJvMFBv8flL0cpQz3AtreyocMLUNKTNzr2sHeLKnhUcqO-293tAF7jFY1MjIIstdYnb5aqFu9m6Ct3Ryjp16bSnc9zTyMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هایلایتی از دیدار جذاب و تماشایی شب گذشته دوتیم فرانسه
🆚
اسپانیا در رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25746" target="_blank">📅 11:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25745">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R3HwIHiBM6_4BhtbpSRxrmuc3_XiCQJHo9c1XeXEhjiJsrK44-HD0ILqOu6UksXrJpX2kEEIQYeEFBKk0wrA-vru1YjMPwMeUiYsFwsh5Gxb3LHU_ekSZxU_tDzMGd6twDE-Xj5nlwRPDfdYEqRIccIEsxlywJjajFGFUn-pG9TB84UBdhdG84QvhsRUHrXLn85Xdf4tbKaL6LMbhI4BC81xZvvqASwzrU2x3GKbPb0ObmfdZ6Bme78ZJksyaDLxgFadOIPJY46wPtZylNM3-rIaVJ2V69WwXesti3aUTs8tyx5UwzH5BVmLoAdvRraniY9N-DmUBLpr6omoINFZLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛دیشب‌مدیربرنامه‌های آسانی به ما گفت که‌باشگاه استقلال ریالی به آسانی نداده و به او گفته که‌میتونه بره قراردادش روفسخ کنه ولی اگه بعنوان اولین‌رسانه این‌خبر رومیزدیم قطعا هجمه‌های زیادی به‌ما وارد میشد پس صبر کردیم همه بزنند بعد ما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/25745" target="_blank">📅 11:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25744">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tEmMch2U0Dy_8V6BYYbCVFSBu7M3V3IIjbKncSxkEeSYeEb7_Qq0mEFgdE5h-XI5piuDBlUTMPGQwG5YfxhNX4EY8Xt_8-DfWci1znis20Sr97xOTQKX5rlzHy5j_wJoqUqNoBldtgFl1i1odagcZf2RCApa1uMzrGWZ07zf_w0rdQ1rvI-WNPwiOjdN9c_csskhZgQpr9BuFT4Bl_SY7mWa-uj4Mjd9BBuAGsGe82jmXPpBVyBcQDP3kOwQWa7TwPbWLKRak-RH7qm-pkBhINlYaUycic4RknxszR5UjwCI1iE7xC2VqPp4rcwi3cWSCBpeSXHMkEb1MaGfnr690w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
#تکمیلی؛ پیشنهادباشگاه‌سپاهان به امید عالیشاه دو ساله به ارزش95میلیاردتومان است که به احتمال زیاد به آن پاسخ مثبت خواهد داد و بزودی با حضور در باشگاه سپاهان قراردادش رو امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/25744" target="_blank">📅 11:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25743">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1866f42adb.mp4?token=rR4aSzWwls031XVUyRZCtMzW-Y5j5wuoIUDkKqNyAy9BsSOcUJruP8G8uSz24ini55Ilho2D-_Z8uI4fu5MHDDfCNJlKgJACyVcwRhJThiy2LBTs3FCegeRNcI64oOKH_giTUQpPjhK5xAXDK3Y5qnQwYorLhC2CX2kYDIV2L6tFyNeJL-WQJIQ9HcUO_dLLf3Coi46lfHI7t1rgyhwoMUTyEo_Lm19_DaCaoSvGfXEM1IFvvuXY5_Ve2bKsic91karI4LpGYprDnEoVYmGuqwMrHTHaGXWk3ugOfG8xBLvnjnLDeVqcAxl0YWeCUZnudSO5ZuMwBqFl8wA79JUcRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1866f42adb.mp4?token=rR4aSzWwls031XVUyRZCtMzW-Y5j5wuoIUDkKqNyAy9BsSOcUJruP8G8uSz24ini55Ilho2D-_Z8uI4fu5MHDDfCNJlKgJACyVcwRhJThiy2LBTs3FCegeRNcI64oOKH_giTUQpPjhK5xAXDK3Y5qnQwYorLhC2CX2kYDIV2L6tFyNeJL-WQJIQ9HcUO_dLLf3Coi46lfHI7t1rgyhwoMUTyEo_Lm19_DaCaoSvGfXEM1IFvvuXY5_Ve2bKsic91karI4LpGYprDnEoVYmGuqwMrHTHaGXWk3ugOfG8xBLvnjnLDeVqcAxl0YWeCUZnudSO5ZuMwBqFl8wA79JUcRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
آندرس‌اینیستا اسطوره‌بارسلونا درگفتگو با عادل فردوسی‌پور: لیونل مسی بهترین‌بازیکن تاریخه. از او همیشه انتظارات بالاس. لیونل مسی فراتر از کلماته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/25743" target="_blank">📅 10:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25742">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ پیروزی قاطع و ارزش مند لاروخا مقابل‌یاران‌کیلیان‌امباپه با طعم صعود به فینال جام؛ دیدیه دشان حرفی برای گفتن نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/25742" target="_blank">📅 10:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25741">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cOVFkgSDIv3iYhZfsNp96Fe9_D1VRKekBN3J_ukMCeOKqZfF4q3dZJr0Q1Ig-Gc33yTra01-aliSSEWN2B-ztiE_-kUhoGt4KJ5F5EOiVw4o2ObHim1JdSLtxar70IwCISuCqA54hZ9vA0Zns_aaF4wbkqDhEQ9QQa7CRv3SJKPTpGftbZk3hCDX2wANyBGvrKibFlxUvaG8e2lUtiUwsSYECyJUCEAyYgtMfxQCjtyu6FutPBHhaGb855uvEzaoxawkveVxkQL67Bpl_Grmx2qX9ndBNC7zfhJAg63QUQySo3itBkycF3XCT8rEOQelePrGydYspMMaRm61LDpFVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
محمد عمری وینگر 26 ساله پرسپولیس دو پیشنهاد از امارات و قطر دریافت کرده و به احتمال فراوان فصل آینده لژیونر خواهد شد. از این انتقال 600 هزار دلار به باشگاه پرسپولیس خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/25741" target="_blank">📅 10:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25739">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vQEhscP1gzjjCJyC1eV3PaM2KgmnoEUdKHuBGgV5cBv_PmAvpYQegnFOIc8xpAyJRGOmFGE_9-35mbO6ooB5F5sXVEWjwL9SkllrZ5Be-zVMRl5Pj3dG6WOv8ZlxK4SK3abbyE9t5OKVKD7pmDVqGyx_j4d-5QAIabiDbe2ZYoVCMHHmx4ZFApiC_2i-6J49dvJ6a1U_piHalE8W9hxPRRJMXM6gqq1VVqaUZirJyztsIlijrmftRSltKqZDd54xUYdYS0RvogbQySCj_B-RoAzzouTGK1ZadRn1JvM1OUu1YJHd0O4iytZt-A9q4iSKEGClwEhQT6leSDuQd0altA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تقویم؛ سال 2016 دقیقا در چنین روزی؛ باشگاه منچستر یونایتد با عقد قراردادی آزاد زلاتان ابراهیموویچ رو به‌خدمت‌ گرفت. زلاتان در مصاحبه بعد از عقدقرارداد گفت به‌جرات میتونم بگم که من بهترین‌خرید باشگاه منچستریونایتد خواهم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/25739" target="_blank">📅 10:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25738">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89f9fe6011.mp4?token=a1ZnAooe0hJURS_NmS9375AUfXBtuOLWmBYoP4kIAAgEXAiGJHfwc6jw1_l-A3mnxvqGcikEunLRXTU2F3cgSmKmjgTgj6ryhumiW0qfKpFCEtCOY4hJCKHaZ3rQNKex9SN7rM1wBzr6VouZRYAnv3lMSGrwLqMITnD6W5T5Z5YUiHNdkAdUlB3SO9KXYti1HK0poFVG1bt3ZBzOld-RBB8-VXwzlVghHdgmjV74A7rXDap80GXCpEb_mO9SKklGmYX4f_obwAa7QkXsPUH5KaMselE73QdaDJOEvtQAir5wboOXYxYj2HwAi2Ie37md4INQGxlVD3-USS-HEBAVVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89f9fe6011.mp4?token=a1ZnAooe0hJURS_NmS9375AUfXBtuOLWmBYoP4kIAAgEXAiGJHfwc6jw1_l-A3mnxvqGcikEunLRXTU2F3cgSmKmjgTgj6ryhumiW0qfKpFCEtCOY4hJCKHaZ3rQNKex9SN7rM1wBzr6VouZRYAnv3lMSGrwLqMITnD6W5T5Z5YUiHNdkAdUlB3SO9KXYti1HK0poFVG1bt3ZBzOld-RBB8-VXwzlVghHdgmjV74A7rXDap80GXCpEb_mO9SKklGmYX4f_obwAa7QkXsPUH5KaMselE73QdaDJOEvtQAir5wboOXYxYj2HwAi2Ie37md4INQGxlVD3-USS-HEBAVVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو لو رفته‌از اعصبانیت‌شدیددیکتاتور کیلیان امباپه در رختکن فرانسه بعد از دیدار برابر اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/25738" target="_blank">📅 10:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25737">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vd8_uP7hc65AEkZye3XFmxdi79U2DiN4Ka8FYsPMY7L4n1e81u3-JkjkCx6I19S4Qerp05wGLb8vx0WvHv0YNn5JjtY_I-Z8-Tl_Nx2HyDDc1TZ-alyj23mls1H0OLkYfLdSL6GKJj8ucqXpg4TsHh0_E6uBlVcp0B3sQ2ndasAs7dJ01At4dvlt81Yf0MBgT6rjE1tgC1-ggCXEcR5kHSOaJ_I9C0w1-TZUKB4UkcgvvYO6JHb1VZURDy3nBFX1hu4BbCJW2Qcd5sDhvWrzKLu4d5hS_AEnBXfPyrlDtD8zPup3QK9ihGtonm-duOXoMJkUmWpJh2MBENPY07c3gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک‌کنم‌اگه‌هرشب‌با ۱۰۰ هزار تومن میومدین چنل بت ماشبی بالای ۲ میلیون‌سودکرده بودین مثل دیشب:)
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/25737" target="_blank">📅 10:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25736">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8e4998f7f.mp4?token=J8Wa4VuhQterLAQOcaYMeRxsu5rnd4IbOimZCI4VreUmPOSEf-38mGdQilPlku6vwSh2GXcHtmgs_B5l2Vjlyu21zLvpNxt7pjZqnCYAyqtgb-wHu6omM99r7jIY0SScYzGFPq3BMKe2UGRFW9aWrXhblGexRwwd58LX1q7VB8KmCdfrgONNEA_uB_Vp93fju9zfVOcx-JYqDPVIa2GXOv2WMdwcE-InqW66D7u-9w6FX9WnPVgX94v-rWRqp9rN-xXolOGOZ8VysZ5_UCiF2fLhx6GkO5xS9PJtdB2C0LHGJQ3ga7dsAH6ZJBJ0ywfQ7R4DWumgesIjJGqLxq5NEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8e4998f7f.mp4?token=J8Wa4VuhQterLAQOcaYMeRxsu5rnd4IbOimZCI4VreUmPOSEf-38mGdQilPlku6vwSh2GXcHtmgs_B5l2Vjlyu21zLvpNxt7pjZqnCYAyqtgb-wHu6omM99r7jIY0SScYzGFPq3BMKe2UGRFW9aWrXhblGexRwwd58LX1q7VB8KmCdfrgONNEA_uB_Vp93fju9zfVOcx-JYqDPVIa2GXOv2WMdwcE-InqW66D7u-9w6FX9WnPVgX94v-rWRqp9rN-xXolOGOZ8VysZ5_UCiF2fLhx6GkO5xS9PJtdB2C0LHGJQ3ga7dsAH6ZJBJ0ywfQ7R4DWumgesIjJGqLxq5NEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آقا یکم جمع و جور تر بشینید امباپه هم اومد:) فرداشب یه ستاره دیگه به این قاب اضافه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/25736" target="_blank">📅 09:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25735">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tqHF2Lk35aLrEDIciy-5jvlgFglZkXQGxdZye23WSSkXM8CLIo7UxkWQO4PANdyWT1Pzw1_NLH-weE6HegnUmJD7WD3XAzkNYk9a1usyt1jqpbB89DRWFZRDQQixgr8O3UA7_OhCgIHspUhM0LzchP2x8GHc_Cy0CigHmq9OKwSSnJGIfauui-R0K60e34RUxOCmb0X1J3e8Gz2qAIIRrCWYMssL8FNayFDEo1KLv8VoXr4Go7YoYrmxoeZU-2qjnyg3KjdLS4Tu80cLyZoJ5ekP2JEZzM0M_744JBruf1Q4ovp-ZIc3icLlsSJfJMHhPYWeCH0eku-XSl9mbq8hrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضعیت‌بین دو‌نیمه فینال: بیژن ویالون بزنه شکیرا شیک، کی میخواد جلو این ترکیبو بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/25735" target="_blank">📅 09:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25734">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PH2hEmNnkHgO_ncL30tOxwkQW47Qa0elMNjNJC7rGjL0acavGUIOuDE_UsmkMUM7uTkjbM5VXxLt6w456xZ5vJEsKCqEu1rLjDRI1aohYeq9IW7v9NC1otG_cMwtyYTxM3NYqllNjNIN5MNfxdEzLSOgVdUFrDEuhLgxW6F5Yio0cQLrQPb5VFPUG2dS1IqQJLZcrC2g_kBiPPDcp0UazH99QCPFuVW2sVQ-Bun83a5yxYFrV5AIf1zJf-16PAgJtg_hDSRyBY2bLVFAjnAz4ysOm_n16v15QPSfrMicyDMwHeYBcutRrAf9vTquVPcceBjIIg4JKIIJE82S4EVBRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گویا فوق‌ستاره‌انگلیسی‌ها شارژشده؛ دوس دختر جود بلینگهام: فردا یک‌ورژن‌جدید و فوق العاده ازبلینگهام مقابل آرژانتین خواهید دید. مطمئن هستم جود میتونه انگلیس رو به فینال جام جهانی ببره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25734" target="_blank">📅 09:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25733">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0f3f3f6d3.mp4?token=TwAu-9O_5DT0LbYspZRl8aScmmx5LbkjFAoVyckqWV4jJJlrllRNW0e8WTJF6fSXQzdeGLdgL_X2CSPYxH2H68rsmLfijvn2GXwGeTvPNyjW-bvDKni_dXumTrisbR0R9PPSQGbaQaRLb_PE_l2WPvdKlNDhiEIfrHFIl5leOhVOwYSd7lJddXlqgUkBjxKb17we5-GDtoXESr9ChtbfevUr7mrPF5qfi43INdglF8VM1NUha777eACMHLM-TD04_J6Glc3EyKifKcWN4h-i9rdcVtRkNElXXPKZzn5Js2o3ikYGtiUfPHOy3Lz8LGn43hbF5bnTER5RfR7pbQ-2GIv-UQZ3OobVX3A7vaED5OUOCzlLStnc46GSr5QbG1IC85O03ZpY0pk7k1jV8KyNqc9tDdCxrZDllmBVGIgA8jpRst9MjzAsY-C4iBpkytQYEAugAKmGNIhDfyNld_Q2JH0cELhvB1FcYwvxUC9Zda-gA6DRqm-mqNPA4Si2IDQS1PcQFYdG9NGAc7nVzgwNAtw92YVPtbw1FdK-tMyDb2lFFSgZ48BZgAlVZBIzq7M2sUc5KSfHFM4N2V-llLnKtwHRlBK2bdrm-rAkwapYBkbnrbiFjHodAsgXVd4vAW2IcDrPngFXff6OlBD56LUft8qBt0K9uptAI6nMBkv7N1s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0f3f3f6d3.mp4?token=TwAu-9O_5DT0LbYspZRl8aScmmx5LbkjFAoVyckqWV4jJJlrllRNW0e8WTJF6fSXQzdeGLdgL_X2CSPYxH2H68rsmLfijvn2GXwGeTvPNyjW-bvDKni_dXumTrisbR0R9PPSQGbaQaRLb_PE_l2WPvdKlNDhiEIfrHFIl5leOhVOwYSd7lJddXlqgUkBjxKb17we5-GDtoXESr9ChtbfevUr7mrPF5qfi43INdglF8VM1NUha777eACMHLM-TD04_J6Glc3EyKifKcWN4h-i9rdcVtRkNElXXPKZzn5Js2o3ikYGtiUfPHOy3Lz8LGn43hbF5bnTER5RfR7pbQ-2GIv-UQZ3OobVX3A7vaED5OUOCzlLStnc46GSr5QbG1IC85O03ZpY0pk7k1jV8KyNqc9tDdCxrZDllmBVGIgA8jpRst9MjzAsY-C4iBpkytQYEAugAKmGNIhDfyNld_Q2JH0cELhvB1FcYwvxUC9Zda-gA6DRqm-mqNPA4Si2IDQS1PcQFYdG9NGAc7nVzgwNAtw92YVPtbw1FdK-tMyDb2lFFSgZ48BZgAlVZBIzq7M2sUc5KSfHFM4N2V-llLnKtwHRlBK2bdrm-rAkwapYBkbnrbiFjHodAsgXVd4vAW2IcDrPngFXff6OlBD56LUft8qBt0K9uptAI6nMBkv7N1s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابواطالب حسینی در برنامه دیشب خود خواننده آهنگ‌معروف "جناب‌سروان ولم‌کن" دعوت کرده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25733" target="_blank">📅 09:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25731">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pUy8TU1Ld1nuHfP2ZfscEtwRWKF668_dRBNKLzuxfBIG3wuK3hiAAPNBVREbHR5h7mTq-2BN72MJanRAxs7npltsfgkJgz3i1LcyBjWnShZPyXDdpCEYvs0zYvfDvODTkhblYEzUpczsaG8eXmOdemI3JbN53nCrGbA6JnH_QDVKhhgkiHWMm90pfDz-h-dQN3sBSnYdk6ykdhchQobfqJjJOP86by5acBWCGQC85VXTgQuMQZ_jrcW2FktJU4tCyup1I_KgRDC7GITHp9CEEt2YnZMOYp6yCFyGhgFrw-O8fG_xTpfoOhZ5FESyyT4bwr-xuJaYLbAYPwApD0iPZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#فکت؛ تیم ملی اسپانیا با رکورد تیم ملی ایتالیا برای‌طولانی‌‌ترین نوارشکست‌ناپذیری در تاریخ فوتبال ملی مردان برابری کرد. 37 بازی بدون شکست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25731" target="_blank">📅 02:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25730">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dDjo8aeWklBZWaQ4v7ZL4Y00WsDV9JWTuOROdv9vTXfWdkbN0gumX9jmjeUSxbAgzE4LUIGB9KUal_voFWmkonFNZbTOSb3IwTRXguY01w02qQnYDGUjv7nwEk92QteIqVMVmz424XsNc3_3z7MophdcsG7kMyD1Ch_jD16i_UcBHmPad1Mk0W30ZFXumxUGtHOhpRgUkGRzTMXuwWOIRYPboXQxLBqxIAmk88ayFtYPE1l1qoR3I8SS0rvZPsH3tyfcyd7d3V6kqce-1RhJJNPXtKM9BCNQJgxG11BC7kagNIyagSfr3-UWhWKNmj_OIu41djePW2iQ61bSVCWe_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درسته که کیلیان امباپه امشب تو زمین نتونست گل بزنه؛ دقایقی دیگه گل رو توی تخت خواب میزنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25730" target="_blank">📅 02:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25729">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fhZqhMQHkgtP9oQ84SCxP88lY7XyAPV1j7f46yO1vBUCf3TFfbQY1URcVuTD1PoCI4hPTfuxa7e78iz31s8cvAL6wXUYL44d4Mgvj7UUwSAazAuKfuKfOBL1E0HE38f30-NW4ioqjU_5zka__m2yXinazJ90zS8cIX35ctWZgoxFuWprgu1amIRypXiLxzsKKdJkMHE2rnadXvzBCBQBlvVLt1YwnICDc9nxngcN2IPHrzTcTG0g0CY8DEuB9c-C9KSLHAM5ajHhJaWUyDELBCYBXvYWKsEs9RYh8Gil5b4g7AFhzSJkOtXye2Mm7dwr9kGYa-kU2oy_fagCurokjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
جود بلینگهام ستاره‌انگلیسی‌هاگل‌هایش در جام جهانی رو به دوست دخترش که قبل هر بازی به او روحیه میدهد و او رو شاداب میکنه تقدیم میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25729" target="_blank">📅 01:51 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25728">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZWJh2E2R7Cgb-rPCHzhal_avv8XvkQEhPHeC7bgaToCXDNXsYgOj-BFlR0g6lgmQMDBDHXvnagGlWo1yltoYE38ajjpR2cqhj3RN3A1ls59Nwa0DazgBzwCEH1Dlpb1BMZs-ycd0dw6o-_uKrFv9OHWOrugWERPBrMPgK2AN-IGPOe8ANLiX5_Hc2VKZ82oA2KJPI6uJ80TArrHdL1anAcSKjUeaY-Q0lduj_QcVXYoxc8oVTwpJYQxPRsgdaGmkzNpIC8vKK5kpFNbn7ZAeC93mMf27VlmSgBYblxaZzWbYkypPNw1caKE3XzPCZe5xcn_hfjuT-R4YQh_be3rGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام وکیل اسپانیایی منیر الحدادی؛ این ستاره اسپانیایی به خاطر مسائل خانوادگی "بارداری همسرش" و آرام‌نبودن وضعیت‌منطقه برای جدایی و فسخ قرار دادش با باشگاه استقلال به توافق رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25728" target="_blank">📅 01:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25727">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50f8c52913.mp4?token=c3yHAYgEXnuh8m8Vt2UUVL0_p45OgjIbnZz5u48O1FQWHjjT5Z5X1MTcoMiB4IG00k9sR9kWU_1VflVIcts-o81t3feDhyPJnD-T2-IIEgu1qfMvxxcSdhkKAr1gb5Simoo7kCLF8CpwIgAj8W3-9444I4x_kVRb-iXCSqBWK5tZoO6v9gfwiX2CgWSo8frBNMooPCX2dIhAIpviX4FAKrmR04DDBdpEcWuuYNxTgB4ASqhtUwTIdo1WmJU5iuOuCsckasndH4Y1XOr7WXBpxy7kWw83qLovTz8sIs-EIxMtkMj62HekmmpiFnHjTFvBPtSFDVJ9IBZbnRc2eQ0B9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50f8c52913.mp4?token=c3yHAYgEXnuh8m8Vt2UUVL0_p45OgjIbnZz5u48O1FQWHjjT5Z5X1MTcoMiB4IG00k9sR9kWU_1VflVIcts-o81t3feDhyPJnD-T2-IIEgu1qfMvxxcSdhkKAr1gb5Simoo7kCLF8CpwIgAj8W3-9444I4x_kVRb-iXCSqBWK5tZoO6v9gfwiX2CgWSo8frBNMooPCX2dIhAIpviX4FAKrmR04DDBdpEcWuuYNxTgB4ASqhtUwTIdo1WmJU5iuOuCsckasndH4Y1XOr7WXBpxy7kWw83qLovTz8sIs-EIxMtkMj62HekmmpiFnHjTFvBPtSFDVJ9IBZbnRc2eQ0B9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آقا یکم جمع و جور تر بشینید امباپه هم اومد:) فرداشب یه ستاره دیگه به این قاب اضافه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/25727" target="_blank">📅 01:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25726">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LqsawqwX36STP4bMEwcgBQxRv38lWmgPZu-tIQ4GrK9cbnKZqQ22KWq2PTg2GAkt0Pzeoc37Y8iRTvD5XRelXPoNlAqs43TvxjY0FkeU5pzN_RgiCxGoSprHH2hckj1PRN3h_5YpNXETYHRcehLvKDGizIKTnVWEk1h0bUILOjGdIGNzWFmDlBYuqiQuCuT2c53nwfVPu9qVNgDxgXuy1sY8lkowOhi3UCh5Nw8UCofUBy7mGFYvLpPskRqNaClVNhIPjeNEf4LRiGGo9p4C-yOUMeriyfbzDeQn1LnyoXnilV1KBa_3_PiTuNjJvsSXI0MwAPs0sRajNa0RL0XIPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇫🇷
استر اکسپوزیتو دوست دختر اسپانیایی کیلیان امباپه امشب تو تخت: آخه من چکاره‌ام؟
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25726" target="_blank">📅 01:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25725">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bDn0_8HO2Ud8n86gQhKEkUb-iyDyY-slQ7WsK_u-vLbZRs2yUA5nIYYn6m_ieN1_PsCxoqTmkLxAG7nsOfsBNZF5qpXxX6rZ5QSWPGTTU2NGQIrFoUKHBFvDKEP3rFq0FJNf9_OvZUMTaYJBcoKWHzoD7jd1dUJ8pBcxyszcQ3sKexRCHTZtyDOLxG3TL-pZM5kmMhDZIU-0w3u8XE8YWhiy6cc6wu1asYTCapBnMtGiNrJGP_s347_blZfsJIq47zy8QVhCtzE-SdzT_MMxGK53miFC0Lm5dUvn9hXF2ODj46M8OQMoU3OKSBvTfGxhlzNTXA5kmsmIhnD58xVNkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فکت؛ امسال سال‌ خوبی برای دیکتاتورا نبود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25725" target="_blank">📅 01:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25723">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fQ-4uiRoFQ170IoFrJS_Go_4CtvJQsheDIklshKvPempD5ZUVXCZp-bmKO7gPUVD22cPNTDM7NHzgZllaEWFGOrHsriIAPXiuJmK0KBTLAscV8FalNdumsuSVF0Fl0V5fJu-VhUAGYJD76gI0MV6CUr_MMfzb_0YoXg7eZDkBpbxthW2LDiUA4HU0KlPszl_FW8FqdlilM729QW1c9nXDSQKg_Lmig6Pv7mW1029M_WtcRlTlV8uNBMSlv1-YaFM_hdd7CK5UJAmcIV3n3TMIpjKj8bgu0WUGjAFHfmffdV8Be31vgw9Rj1NrQN1lfrYAJBVtBjtsZxzK4EJwb3vqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VDOjyh4BVEK0h5tXU70eHVZrBxIBN0Ep4km8jhSfQ6wfRcEEW0hLaUFIDgWiexOBJ3pYWRSufz3rn28wsHHxLah1qX5Pe-1cuKUuxB9mgyCQX-e26tqfoKckX7IvFha90bblxRMNueuMWFTB6AY9fEKpac2Mhk0TA2ymy72NqJe-0msJnvXSpR78NyA25IqMM3xnPFcdErML5sqIraUoyjZRihFEUuy4u8Z5euBDUcfSzuvAOrn2jexSU4qPm6TuhRbeTEvvUpOIw7MuxgCVozzd0kLWysE7io3DUZTADiR54mWAScsTZIq6WamHo2oabNZgV5dBLw3Hi_ylD5mmtw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25723" target="_blank">📅 01:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25722">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/avwnxNCTu2M0DOGEdz7cyZ7ToVtoggR4MWosIz_zElcicitVjXO70uGRogM6MR704q45qUw5n5Xp3izcttxX6-oWRlarObA6Vjhe9tvHXl-5idGIydMczmDMp-k8GUPXDZeWZObxm1Is62LXQFBLzjm_XIugg6bCd8djitdF-zFR6YEVKpN9UXrO5Ye5aBfPjp8TbTFV1-BF4uxk-Q6oUDoTxsRvrRV0xhW9Te1zO0nBMHFcP1BxLAe8rivs8eYhzN9oecQ7-8ObvJ91FbSZYaj3s_TfCweOmy8Zce6VoGZkbTBAodlud3wcJZ6YStWD-A7Q9y7vtdH_n-8P8F5iXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها دیدار مهم امروز؛
جدال تماشایی انگلیسی‌ها برابر یاران لئو مسی درنیمه‌نهایی جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25722" target="_blank">📅 00:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25721">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQyo4ogIU2OIs5dRD8EdFWx7g6nIGoLZ9iijwEd5BSgPSIc8RTyWLK4zYI8nWyHjAVQ4DZ3bBRfdicGLpldlc8sH1m0g2RVL7JCaq4_u2cu5wLcMseraB1AVvV5t9WjdydO6FZ1PUcPU4umk54ENF1MSRwgBq01Ag_OO1mEo4ipRlIFaO5HlBu5KtBdZjIzZv5lIFjpA-ynvUkdEStdXwhM33y3yJ_7dQdRRrPmQgGEvh4GdYv4KKtGccNNo7SsB_lGcZRG_BYntDFxp0c8lQnPFiRxuaCvfnQQvhK3F-najnM7-0KnPnRnFXDbp8YUqZyq2hJRZStWOlGdDsKm84g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌تنها دیدار‌ دیروز؛
راهیابی اسپانیا به فینال جام‌جهانی با نمایشی منظم مقابل شاگردان دشان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/25721" target="_blank">📅 00:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25720">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mgXn4Y1roL-3nPpHHgkEo7VMe9jJTyyK4BIYx3Qx2GXe9eIlba5RIVpM1IJNfR8ZzGpRuBHcPOhzUvEea81BunPZo5VSegCQY-G87Mmd7ADf3yp236iPJMJiDVVrgbhc_drviIQIfJlFezbsEDhzg7yqLtzHjxqrTUPfBQ8OKfEgLzHtvhuz8vCwTxErvt0aet0MBYzhuhP44WFiNIbnlgDj53DfP2pnSOJ6GS_5_Tgt45LYWucIF5c8XSIXQs27o72Lav7yFIQp5K2J9F_6NyyWsw-_sWDzFGJLuI5glDn4q7t6ufwtOIs75kSf2-8enDiEMQlsll2JuoqgsWRd7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#تکمیلی؛ زین الدین زیدان برای قرار داد 4 ساله بافدراسیون‌فوتبال‌فرانسه به توافق کامل رسید و در پایان جام جهانی 2026 جانشین دشان خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/25720" target="_blank">📅 00:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25718">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QVCvaSj8SJWEORc7CowHDE1eafcyIlQT11p0UCrN0XnEp_K6tsI5QcanBLW6WWMiyAY0gfA8jThsfRnymO_nIYcjbsIQECTqBgwFiFsxvAZT3l67DPi-qClSnDMkwhyIXL0gMRGwYTUjVpaNRX47xGa4UsFVC4_OvXRqNEdqR-UydGr9rWUp8SuS8hc4VkUm15n5l3NefoQeTt2hCxR2sVHC8Ae3SKsb6gl-NcXPsTF2MXVBQSAShCVvV-8xft0qiKB1hTh7YcAu14OK4l6s-zs2DT4oYTavlFid9TeLIkPtnRs8mtV6dD0wVohoh10INC860fkEKoMN2eqUumC1Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ERERlFLI_clqZCPQo3n9ZUTWK0-GqlTaWxIUI_rWK1b1Nb76JNCRapLlN0d-WxJ9Pfgdn94Bpj3qrYxyjlcfC5zl-D56TD6-zRIkwSOVxICiucMQaPIc7TFCQ7n6-04C7tzG7x67zvfHQYG4a57xuEPC9886IIKS90V8dT13aXUPod52fyIJ2rDz4cRFgLvMUiRna4n-4LUr59YOaruj4FS5QLkCau0eg0ZUERRaBl4O463t3lwGXf6y45lERdtn1DuOGSwZQrjPZtKRP53VSZHKDy5gKpiukDu_I7Skp51IYWn5n_OIMB0ZZxKInSiLckKC4TzirPqZjboe0YY6gA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ پیروزی قاطع و ارزش مند لاروخا مقابل‌یاران‌کیلیان‌امباپه با طعم صعود به فینال جام؛ دیدیه دشان حرفی برای گفتن نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25718" target="_blank">📅 00:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25717">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YIR_QCz_F4WLi9xdU91I0cW9EuU5XvwEhKwO8JhXZxvmRl0W0cIXnXDNCMYZ5vuiYETsik09zV2nWfb9m-SqZafGYKK1wsJEH6q8ZcSyCxod7eCr8olK9VWJ6A2CMQkZdrzIwdVrVPfELLHuTD-n3N7nl9So9CMStKLlCQNvWI7K1_lJ4ABWNHPfxYq4b7Ip8AjPphDUyDDaWgPmuOZh1O-InwILbfRiaXxf1QRppiFA8SaHM0mlwN3qNsSk0oXRNqDR87YvTslyzMDOcE0b7xz1pvHaFuexpG_s08Lo6m_7TN_0vrL5y4nUzR2BF4hJd_LzYNJvXEB6cfZ0JUlsFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ پیروزی قاطع و ارزش مند لاروخا مقابل‌یاران‌کیلیان‌امباپه با طعم صعود به فینال جام؛ دیدیه دشان حرفی برای گفتن نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25717" target="_blank">📅 00:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25716">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YpmcBqKEK54hAgCt7QXICIrZM6khuN1vv9YcTY39EOm-OLt91BIc_mtALyo31pSwCjPY50KobS1fLZ6D7pK9adYs0vawCAz0ARmIPE1Jn-SWVnHDJhU-2cIiF-KXr27ov_MNYU-SPTXB5OnJy-tIdG5H6hBCbWrXpgWUuT6Y6GBnHzj73mfj1bkNoyw4X0gg2Iaq8VlN7ouQaf8tMPtF8dhTyEjiW8P_bMnKTRtPwAiR6_u5mSDxAKvHOm83i1VtGf-bukItrnvHCOGxsv9hwialjHcWOK0xUSog0tFF82t9DPivFk9Im7zzM7VcoA1RhkdI2y-FIOgTTMirRkRK8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار نیمه اول دیدار اسپانیا
🆚
فرانسه در نیمه نهایی؛ برتری نسبتی ماتادورها در نیمه اول؛ رودری با نمره 7.2 بهترین بازیکن نیمه اول این بازی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/25716" target="_blank">📅 00:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25715">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XCuae7-kCRop0yt-8-fCPMSqr4AXmuUWWISjNY4YRFIRNuyPyL4X3rd8BZdMD6D88K538FXsCNs6iVBTuKx2ZG908pwP2-WENTiiMMyamFkJO39RC0LD2rw2XXnW3q5ua3abMfi3wAZw1lAGCeXRj91I25FJ2f37NNvsiVBSzSlf_1bxQWIeHRglFL_YYw0LDHkBKrPQKG900Z1ObPx3VZHPAP_E2oDG-mK2anQZmH4YfqsYlSZj5Ml7Rsstod5LCcQOBBTqK1JJ9Avzb_H1wOaF4dpltovOnGJk5b147WRG25JbBLV33aYW5w6qVvSDtAFwxdO-xpQpqwGQDbBRjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باشگاه گلگهر به‌‌درخواست‌ مهدی رحمتی خواستار جذب امیر رضا رفیعی دروازه‌بان جوان پرسپولیس شد. این احتمال وجود دارد که درصورت موافقت خودِ رفیعی، این بازیکن با پوریا لطیفی فر معاوضه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25715" target="_blank">📅 00:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25714">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4Xy2ZCgxVgGjSC8zGT1uunQ0QK08T9gOfIxycx-UZHlU3zTNoUoU4wfjZl45EeQiry1O9dVlQvU62qKDuZIBPAXbe4qBVPRy9WdpK6dojIZJOp6TNAsI0S-VABQpZ86vLELF_DZ8vzh3d8yiQ81NbSmhthOF149eS3PnyzMqQ1q36gfgHvt5BhFEc_CtWxmsLW6BMEvQJNxi-Wvtvm83eKbe7xVcl_yBsTPOj8emh41wbJENjQyAH9tNywnufefEYMAPhHj2bq9ggiOHwiIsNA1TLEQILpKAqkVAUZvRxiSRZfQ-8c2eCN2jX3lNQPHqyi31gSPWIU3XloWvTtyJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
وریا غفوری کاپیتان‌سابق‌استقلال درگفتگو با عادل اعلام‌ کرد دیگر نمیخواد بعنوان دستیار فعالیت کنه و به همین خاطر پیشنهاد کادر فنی آبی‌ها رو رد کرده. وریا میخواهد سرمربی تیم لیگ برتری شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25714" target="_blank">📅 23:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25713">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/km3iKxIfMADiADf9rBQ2xC0seTzu3HKhN-yTwvMuUTS8oA1ht86zf2g-wFN9__cIX49CxVoKqOlg0agHPTx3XpKfG0VMkPFe8lkWTufry_OuTtIIWDa3ELVp1ZVHToVcgsUe_NYZE1-ZsTgyp3-4X0rMhFgOzY5hb6uhImwWNEUuP8gJcyei-ioUEfT9UcTXUFvZLQ2PFfjWOM3Xlkx4SGWhsqc7hamcnj6z_mTBS81UQ-mg8ST74WS55-F1UzBmhWEgSGEktJoXw4L26Dn6Cp_4z-ML_HlS08Ajn-RbtbP3__vGZNYRBbjuSIY2x2P_4onW8zodMvU3nGIuSArL8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار نیمه اول دیدار اسپانیا
🆚
فرانسه در نیمه نهایی؛ برتری نسبتی ماتادورها در نیمه اول؛ رودری با نمره 7.2 بهترین بازیکن نیمه اول این بازی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25713" target="_blank">📅 23:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25712">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-LUL31nyridPYpuY8BCHd_qJ2klj2-tcQ4XRVPPpv0P_Grh7M4Fq8YWrXieR42a4Jk-ugguTnc0H2qSCn5ehaIJ-9EAagifL2qtlFd4n4EUmLs1tnVF7X1OPLQhnwPUAr7dMg65YXmaQAcnFImFEGG5nEcGgh_F9rE1fRxaePhkVlDfZIbYf_EezWQA6_ojtMMwDMOVI03BqjrLH-Orf8F3VQ7VzU6Q-7pyOPd4lRpNlk-KqglY3VrpJplpu9ABoo7YNHqw1UbXif8PeX-zGHDNhGYirdJeQ8sZcwgTo8YD1zT2faZoH4GzPKi9i6Myfe9c4sXdODqkMFEDZoXYPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ شماتیک ترکیب دو تیم ملی اسپانیا
🆚
فرانسه؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25712" target="_blank">📅 23:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25711">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d4h6UNb1urb_Y6vEf87hFrYazGWSf2feKAu7i1XzH7zZ4hfVivegDlOKWmpwJLepLTlrZq3Btn59bITeW6CnUiUKEYCe3DOcngsAANyWs5h_oPPKQMxa3-s3DKDhyCncD99U6OKYefioNQLZuVWPxKkLdROUP01jQeq1DsjFi5UOhJ703_LTaSO0Wr15-5Epnr7V2XUY0111ZALRPeU7HLgtDNBuqQ-BNqbOAseO_YAGrOgp1yq1jAi6VVvwrZkiNz2gvwwDn0JUeN3uxjLOROoWvLh0wy3pdEZuNsz2rEtic_nyE3KTMAbtmgMqpIWJ-VkoaPMghuSkL_pt4s_Skg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
بااعلام باشگاه فجر سپاسی؛
فیروز قربانی سرمربی جوان‌ونسبتاموفق‌ شیرازی‌ها از این باشگاه جدا شد. بر سر مسائل مالی به توافق نرسیده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25711" target="_blank">📅 23:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25710">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fb85979f5.mp4?token=M3vrlandLTnbBZ2g6iAFAXFyAHKPY1BNvC3bqcH3WOi6CnhvPs9O_yQjHPJTUcP1_kVxWfjNq4LOBQks0MrUl_qeZskU0J0xlWEfjmnu4dU273a-TqWdckZ7Px04Ixvzze3uPxn6f40sKfXCLuNlMU56HG8SNtFq4UrlYswC9GoKWOzCfDKBQ7200IcmiOtDKK0VHsli-hFNxrTcVxTvZm0tuWGEj52xTql0apzW6KVRMa9uXVIVwgoFxphc6D5f9_WgUtOUjKf436fY5nt_70q9SQQBUantJeoximv1Pt6T6irdgogyL_FrsJgEHwrC6rRj15b_sHTYsGQNEO25AB4nvj9ohbVECJTKDAuRCzeYlCwwxO8f_9cfxsWzYEMDyxxD8Dj5JpS98t1wY7DElG5iuHCYJ5x44VKiyo8WmNQiyXPFjmO3kxkJH2Kh8ElEZHRUHCi8fFG1uVheN3F_uXmxXl2HHhp2j59ZoiqqH9tRICeHDJegBYYozEgBx0a_kzrVeNbv_rjrHPMnXyETIi1JVEQH8IAIeCoWFlczFs_J2QPGnwGC1DMFn_Zxp7w0jO-mnxlSvLbL5OqAvyJwtMehMdVL8mCyjmh2gHHuRTwRJ6lKpi6kwvAh4s92_JqDbfJK5xnstwbwIxbSF7qvpCF51Wch6X-An2iRj-8Z2ZM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fb85979f5.mp4?token=M3vrlandLTnbBZ2g6iAFAXFyAHKPY1BNvC3bqcH3WOi6CnhvPs9O_yQjHPJTUcP1_kVxWfjNq4LOBQks0MrUl_qeZskU0J0xlWEfjmnu4dU273a-TqWdckZ7Px04Ixvzze3uPxn6f40sKfXCLuNlMU56HG8SNtFq4UrlYswC9GoKWOzCfDKBQ7200IcmiOtDKK0VHsli-hFNxrTcVxTvZm0tuWGEj52xTql0apzW6KVRMa9uXVIVwgoFxphc6D5f9_WgUtOUjKf436fY5nt_70q9SQQBUantJeoximv1Pt6T6irdgogyL_FrsJgEHwrC6rRj15b_sHTYsGQNEO25AB4nvj9ohbVECJTKDAuRCzeYlCwwxO8f_9cfxsWzYEMDyxxD8Dj5JpS98t1wY7DElG5iuHCYJ5x44VKiyo8WmNQiyXPFjmO3kxkJH2Kh8ElEZHRUHCi8fFG1uVheN3F_uXmxXl2HHhp2j59ZoiqqH9tRICeHDJegBYYozEgBx0a_kzrVeNbv_rjrHPMnXyETIi1JVEQH8IAIeCoWFlczFs_J2QPGnwGC1DMFn_Zxp7w0jO-mnxlSvLbL5OqAvyJwtMehMdVL8mCyjmh2gHHuRTwRJ6lKpi6kwvAh4s92_JqDbfJK5xnstwbwIxbSF7qvpCF51Wch6X-An2iRj-8Z2ZM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خاطره‌جذاب‌وشنیدنی‌فیروزکریمی‌کارشناس‌بازی اسپانیا
🆚
فرانسه از تسلطش روی زبان انگلیسی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25710" target="_blank">📅 23:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25709">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e6f94a364.mp4?token=DFQHS8oJCRQ274168frsx7Si_LlLlwVczRUlUjkG3lNvvY-9xzg8aLD0jB_P83nxBlxVdL68gcCwv3OCDKX5TVtoBn6RsMQPjdG-u06vgkTv1qZhoIgp_JXAef1CvavTKb83uwbtRmILBWAp8ZOy6rJfozvZxiUa-Vjmmkzb5C7y2x-gGqL4DVAxy82fX1yJqrJGsthUitlwR_xYRv7aGEHpQt34PJDMjUP1jHI0xPZ0iBjhuBAYDOvayjCBaU6pPoVqd1NcNZe2bf4xo4Mj2fOSFHvut5_stTk8PHWCHheT7-Moxz1hie7WPLuFM552CSHszdSvm-tSEwZ_sXLRAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6f94a364.mp4?token=DFQHS8oJCRQ274168frsx7Si_LlLlwVczRUlUjkG3lNvvY-9xzg8aLD0jB_P83nxBlxVdL68gcCwv3OCDKX5TVtoBn6RsMQPjdG-u06vgkTv1qZhoIgp_JXAef1CvavTKb83uwbtRmILBWAp8ZOy6rJfozvZxiUa-Vjmmkzb5C7y2x-gGqL4DVAxy82fX1yJqrJGsthUitlwR_xYRv7aGEHpQt34PJDMjUP1jHI0xPZ0iBjhuBAYDOvayjCBaU6pPoVqd1NcNZe2bf4xo4Mj2fOSFHvut5_stTk8PHWCHheT7-Moxz1hie7WPLuFM552CSHszdSvm-tSEwZ_sXLRAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
آندرس اینیستا اسطوره اسپانیا خطاب به عادل فردوسی‌پور: باعث‌افتخارمه‌که باشما حرف میزنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25709" target="_blank">📅 22:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25708">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V-KShijv6l35L2b_6F9RTn7Gsy1bMDnJoRbJxrmBOZvf0Zgx_SwPIzvrKzqLEi-ZixsQaNF2FTTzNU2C1_XRooNRooAwZf_ARB8WQvnGDTHE0Q_4MRCgJEF4pvgoKPuVnOYqlVyrPwEGwYf_55dgYBdGRXTwpGHYXG17zAgw4-PJzZm9PFvI0UjJGT_rXO4PdkBq0v-dHZgkH-yxGrnhNHsyTkpkZsmZoeeeSMd6GJFWxaHBHOfGRDFm8Cwyu7javRWs3i0JclRiuQCviF8_nYBG5yonf5TD39t8qgNye1jbNfeHMcAUoFFCBiv6Rf0RSZflzzB8P2xZPqJZnt6KOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام وکیل اسپانیایی منیر الحدادی؛ این ستاره اسپانیایی به خاطر مسائل خانوادگی "بارداری همسرش" و آرام‌نبودن وضعیت‌منطقه برای جدایی و فسخ قرار دادش با باشگاه استقلال به توافق رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/25708" target="_blank">📅 22:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25707">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cHbCPO0EmtQEoUW8nAjq053Wh7vDiu1HmyCPIxIV5rjn0LJlpplgAptcwNzW3StfqbZ25sLGs7qpT64KAqxiC_ze4wJvoN8JgmDN7xkON6Yr_UAjI4Z28tAeiGBobkrSR1IEbuJVwaSkdpc407wFky8BotR9_nl8bqIQWB1hNlRRBy__iHLPLJLuSpdLZtv64gyOtM1xSeQHHWuFApF854XEus-E9uP65sqJdC1HbTqKAvF-b419hc6ROYWeBQe8WqEY93ZPwZkRFaSx5hODOCPhwL9MKexWLC9rk_HDFufOkALQ7Cymh25-NyH6Ya12dviiqjBP4U3Lu5bUsuD7gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ شماتیک ترکیب دو تیم ملی اسپانیا
🆚
فرانسه؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25707" target="_blank">📅 22:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25705">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V5IG1AFR7dhXBhCgPVFMx4_-TIdkHCz8yt4fhBaTBcqEvCQgAxFHTihgJhLgL1h_BMh3zMLk5aKpP1_69wxpFCSKMtVWxoVSwQ-F43XU0Xq8CsZjshV4ndqyoOWXetF3s6xKbMvZ33Qr96eEJJPx9huQoBy4zZbCeS7eOS6nS_BWJXWLryi7_m_RM6B62eKnlTv1lDY0AwPfnGDvSxSF7p238E3yxcLqsoJKNGoyUDo69fT8EMGNkptafr2AMm319Qwxq_gUTq2VjP3so3j8xa9yubNs6fKaJ7jszzH5oFX2m9cq-UjY2vBe-nJT4wi6TIrseOz3XABb3WoOYYdV5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iXCR_fY-wFNOct3eh6Rec-JB0UOpHrgkkWOdlFYktN4ufECn7zuGQ83K9O9xRJxEpoxTBGMV2jfWHxugWcF2ezCDMu-vHHoE01n52dzjw2kCiY82BwS11NchSe5eELdga4knB9ZSbdp5dRiTWo1idLlDAvqhgg4Z1bYUL7b4QxB8AnzArivmVitkrptY09Vdr-jh2-VkDKEtoPqydRyNXPZE7MumuHXWR8dXJq95STrpw0A10LsvWKIz2TjCOvFmKQjC150PC0SQj5zH4b63kHE7oOPSOKEwgcEdCy7YpOi7rjvlXLwSMZ15pVyWiGn1jI0dF2xFvBFpYOBYeaREWA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
خبرنگار معروف‌ شبکه ایتالیایی DAZN که معتقده تیم‌ انگلیس قهرمان جام‌ جهانی میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25705" target="_blank">📅 22:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25704">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jqoa8SzeiFxNvc3XQ17A0lfiW849d9H_WQH2b3U-p4ByvvnIDBbwx75_lJDN2DjnQnB7cCbTWALexMmHG1zWLlfHvGd5N5iPT2IaIBtyMnKsY2b2UqjLUqpv-NrH95XllhjrfjBNyjh7RRu4iBzKgJieeM_6pimm1mcjVQI8o526NXQSIKDDAEgLCNqqqdIQz2eh0MnsMJWRUcUiq0W2-EkUnAdti84XSuoYvf97Ler8kFfv2l3k6pRab7CkCiCOLJ6AUKnIxbbdsZZnBLjjmE3k0W5fg-mhd4s8iM_hew1sTCzmyH8HIYPdFbd5Jz6IMpUEkOym36-fUFDhSo4hjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شهاب‌زندی‌‌مدیرعامل‌‌تیم‌نساجی: برای خرید یک بازیکن‌دیگر از روسیه باباشگاهش‌به‌توافق رسیدیم که روی 1.8 میلیون‌دلار این‌بازیکن تهاجمی روبخریم اما خودِ بازیکن حاضر به امضای قرارداد نشد. پدر کسری طاهری به نماینده از خودِ او امضازد و به تیم‌ما اومد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25704" target="_blank">📅 21:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25703">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mj0V_nO4xdZ9xGS3GuY5XoMdh2HNce-yp5ehm4jzwfZ6Z-A3ifPkPJ4Pi08b-9h5R3gLFqvJ08PeqD4EcTMBigHO8r22uJ0P6iqaJgQVxM8Yy5pp1nZxHGkLc6gyxbqUFQYmR1qR6Pacg1aBjiz5mSKrdDPtteRVzh6ABM1WUX4YNC0pDeV-V9oJwoRf5U27GU85hi87BgvB2rFeUM4rbILAQz3tQOlQofnl5Odfzv2fsBohmScwAtVu748oB6e8t5ro0Oevh9F7M5bCQas-xP1V6P-t0Mnd1qvskJpqtNIz-6FL686eikEWMudzFP9pNUxJZmcBghpBMQfuQ70Clw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
طبق‌نتایج‌یک‌نظرسنجی‌درکشور پرتغال، اکثر مردان حذف‌شدن رونالدو ازجام‌جهانی را سخت‌تر از جدایی‌خودشان‌ازپارتنر و کاپلشون توصیف کرده‌اند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25703" target="_blank">📅 21:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25702">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E13_q7qhhLv9A1M9SiMPq10V2G7WdXrOhcTF9nn-357BC4G14OktVq67lmI7NQFyHvUSjPsU16P__SGGbdGUq1p2Q_vXEoR8mpV3nclK6vA7hDQAYwQOTY8lkRqanFvYeuzPS5bPwyMIKHQoIpYMxNRjOPDaRNwdyHYpRjXR03ep60q74mQTkL1H4CLtBgzjfNBQ4v0ilwVLbOvl53_JDFZFgIZ3l9cmMa2TOs9u6zXxTCq-h_bw1CYMQQKgo7gtFyk19y_ZANIjc_BKsptlBBiGwMWEM-pgmHaglEKOXVQh5HRF5wG52UiMAn-Htzvv-SkpwEeWyAcsIYbHBUq4Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
۵۰۰ دلار جایزه نقدی + ۱ گیگ اینترنت رایگان!
🎁
🇫🇷
فرانسه
🆚
اسپانیا
🇪🇸
🔥
نیمه‌نهایی جام جهانی ۲۰۲۶
فقط کافیه نتیجه بازی رو
قبل از شروع مسابقه
درست پیش‌بینی کنی.
🏆
۵۰۰ دلار بین تمام پیش‌بینی‌های صحیح بصورت FreeBet تقسیم میشه.
🎁
علاوه بر اون، همه برنده‌ها
۱ گیگ اینترنت یک‌ماهه رایگان
دریافت می‌کنن.
⏳
فرصت ثبت پیش‌بینی محدوده؛ بعد از شروع بازی دیگه امکان شرکت وجود نداره.
👇
همین حالا وارد شو:
https://t.me/betegram_bot?start=p7_r4EF37DCE</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/25702" target="_blank">📅 21:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25701">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DvD6RLLA03LhZxzV1kxV9H3hRWYVTugmnx89Gj3wFtvJVlQAftaZhrcNb0L4MyZCSw_YC0UktDocn45xxulHZom19OFTJk7ee-ouwZHMWPG2kUSC93KVXLjy0CdISn9LpbiWD-F8CQzpkGp5ghlWt1eOIQK8gmzSqOn61npzbyQh_5JT2QF7L3JwVIm2hyz1c1hJN4mYAuuEZibaOEbpzMeppqGyZ3PYq4gI4i1OGTq9Py8S2ksvwbkKVnfxszuEOLMh1wrvLxraiVycAAzQiexEt_F8KXosgvkah-zZ1NtUKrhWUmA4ipKdyJWT_t4VUvqhlQnPb4gM4P23p7Glog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام وکیل اسپانیایی منیر الحدادی؛ این ستاره اسپانیایی به خاطر مسائل خانوادگی "بارداری همسرش" و آرام‌نبودن وضعیت‌منطقه برای جدایی و فسخ قرار دادش با باشگاه استقلال به توافق رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/25701" target="_blank">📅 21:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25700">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AstSP-0QMcer6ZOBai9aYmiP9eVN8rIJWQpkdo4P7SRuSw9FgaCpkQ0K4s2S8aY3AMAH-cP6HGqFxcUSq5T1vFMXqeSIRib9y-3mMJwMLitQYg58Ptw9pcpzn_SNS7JNb_sxNnf777mJV7cj6iPK9wVOx3-nA_cWt5aWCiPVEsVLwpWpM9uCPeHD-oS6s5F1cZ6XU2ZJvmRngOztTj8FeLyt3SI1MH9njT4E_kerkDhhN0I-Sk4AqRQx-EjojzYlgvfM8OCZj8kAl0sFfFZfVkYUESiwnMfYbLc4AFeiKM8Bk55HqsavwmJujzzUOtdPWVjBPfY3k_Q18q52_G8nAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
طبق شنیده‌های رسانه پرشیانا؛ هفته آینده جلسه‌‌ای بین ایگور سرگیف و مدیریت باشگاه پرسپولیس برگزار خواهد شد تا مدیریت‌سرخ‌ها این بازیکن رو برای‌موندن دراین باشگاه برای فصل آینده متقاعد کنند. سرگیف بخاطر مسائل خانوادگی قصد داره فصل جدید رو در لیگ برتر ازبکستان…</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25700" target="_blank">📅 21:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25699">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BNgmfCH4GH3ICo1tReQChJ_RbyOXs4cfjCWVdnoGxRIoxaVVSNrWgIm4p2wMn2PlcPT--Y7oNSd2ATYmTBvVDIeQjLYjuRqVBMvF-PROsycs2t1GmoUpgPqOY2i5sndRW1eNp5NSa04v3jffwDR7sIgF4AWl9JUk2krYqz2HPimXP9hKg6SKRFAVfiudM8-NGp3v_n9nSs518dnEjBj-m-PDUE72hanKCTfiTDPHz6cX_39SRp5cmbGes9R1rSFo3yCagxd3C80_QjFdmKwxzuKg2xgZrTko9KNUO4Hzl5_q-pza7MJqB85NbkE7A_MqVpooChddEljlM_0vx-OO0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛ آخرین پیغام منیر الحدادی به مدیران باشگاه استقلال: وضعیت منطقه آرام باشد این هفته به ایران باز خواهم گشت امادرغیر اینصورت باتوجه به شرایط خاص همسر و به‌دنیا اومدن فرزندم نمیتونم باهاتون کار کنم و ازای فسخ قراردادم مبلغی برای شما واریز…</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25699" target="_blank">📅 21:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25698">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b34e61019.mp4?token=Pt7BrfevTVKTn7r8t4dyaOULVyzvXREOGQCLqPmDUbNHpXNZcSh_GxncfHSt0ILWxzqLxVV7xqWFsFiNPMrrIQ-foOflgpWZW7X0wAmKH1IQAIt2DvMJYZfuvleINmMSOBA1jTSHzXSUFVQWR9K6vvvgG_bqCs0mlqEZ5yBg7g6IpX2pkEFQ2sGbdSVWvE1Ik4IavV_o3g2eouCgQGRpH0AlNlMxmKSTIrg9UxwnvBA_v6Cif7GCsmJk85izRKatN2h8n11CRuTrooaPjlm5PoJs4MwSY5DqWVPdAzmaXUSqOpeJI5g6gJ-juEnhqoeNGSCk7svrAyCdMJRBjgoUvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b34e61019.mp4?token=Pt7BrfevTVKTn7r8t4dyaOULVyzvXREOGQCLqPmDUbNHpXNZcSh_GxncfHSt0ILWxzqLxVV7xqWFsFiNPMrrIQ-foOflgpWZW7X0wAmKH1IQAIt2DvMJYZfuvleINmMSOBA1jTSHzXSUFVQWR9K6vvvgG_bqCs0mlqEZ5yBg7g6IpX2pkEFQ2sGbdSVWvE1Ik4IavV_o3g2eouCgQGRpH0AlNlMxmKSTIrg9UxwnvBA_v6Cif7GCsmJk85izRKatN2h8n11CRuTrooaPjlm5PoJs4MwSY5DqWVPdAzmaXUSqOpeJI5g6gJ-juEnhqoeNGSCk7svrAyCdMJRBjgoUvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇧🇪
خرید خوب‌کریک‌برای‌شیاطین‌سرخ؛ یوری تیلمانس ستاره 29 ساله تیم ملی بلژیک با عقد قرار دادی چهار ساله رسما به منچستریونایتد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/25698" target="_blank">📅 21:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25697">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LofEjhKUMbB5py0q089eJHIXzC55clgCKzXgKRqzlFGORKbtCEu7WPpmErj8uDDlT1uUbP3C0Ck2fYmofQunN7kGdkoJXAyq35AjhhcqLrc5f9fevSbNR47HHYIUAnGIHYeoqZ6ZM0Vn8GRDqLCnxKGdmcsmMpQVXaj3_IVYnfOFHV9XtTL5V3FnaCupiHWaYv2danlImTOJB_uSk2XK1dg5A7FULYHI_9-90byjAIkg6xhYVNC9AmVBwwo6riO2QrFw8TUjJZjkGG0usFDUpd1RvOjfxe2ESf6yraqD5_7wuRSTxkqs6a5syhwLhvWXDgfJKQpyhDtD1IFXq1bS7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛پوریا لطیفی‌فر ستاره‌جوان گل گهر امروز از سیدمهدی‌رحمتی‌بابت موافقتش باجدایی از این‌تیم‌ و پیوستن به پرسپولیس تشکر کرده‌. همانطور که‌درروزهای اخیر نیزخبردادیم تمام توافقات بین سه طرف انجام شده و به احتمال زیاد این انتقال بزودی انجام خواهد شد و لطیفی‌فر…</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/25697" target="_blank">📅 20:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25695">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Amcd4RVJKuclttc4PN8o0WTqc8wFdP0R5Co3vpCDKwgzdOFpDAt8r5wdUo50Jvnb77Ti3lCfzwMUKGMOcZejMLUgnE5wjsQcnYIWwQL__oFKX1hJM6tn0HSgJkqBvyrZR6E69Apk0XSRTUQlL1FxegShHmZtW2RoK9kCDQT9uj9NRqljAjtDKvbQemlxqvI5YgKWd0B6y_3E4ZvUaN-EKLU1_y3S2END_1xe6bw77uYa5AeWnPeo6czb44gPVQfPqiONIMvy0gdlCvYYmxCs-mrP-FDYEpcTCk5cqZqZ8t3abzlQArOw7oeLaYObPKVWiWLWN-gQ1ROBftC6FiCeLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RghC2bIzJtTfLw023dm3N5XlKB64hRqv3fPB0-9nDhJX33asv8OlzY__spx9IhrxXHA4qulBCTZpFWPueoVe4meKIvqQ6P3MX21S07hugWQXR6qjWk5_DYb_GBy3TUN8yOQ8fSiKq4fE74HBeiaB7Dw6foxP2Y_GFnDlgu2eXgYAABNhDjObJ8w7hbzTj6rX_t5LXh_dGvIXzJ4Cvx8Z0wrBiXx1yWW-8YQSwmXr3qiZHvZ9fpUle4H-7Lia3oo237GFYCcebouppq_pjYvaG0JsX7IFawP1vZJIBqibwh1gv2BvM1dnxqv0Rps1PMCwjNGbOcKB5AIqBR9Dlc4qrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛
شماتیک ترکیب دو تیم ملی اسپانیا
🆚
فرانسه؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25695" target="_blank">📅 20:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25694">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szxSJWywUB5mK5ZYwHWLQkWVJs1FA5BAbOUSwTSP0H6NOXpgWx8N20BronIKs3uYg6f-qK1Xs3pz4SbyGlXyOoavJtzjj8olv9abpuTjZkEjeeiI5u3vsZrfKklRNUzJ9Y_Gx1us3TA_-CETt4chDTq-JkcYjYZ-Bo-xDJRRCxNzRcl-VgMUn55sh4OOAlXjB1RQT6Hr26iF1sg9DMvYoPYvOhLBz6msjtaD-R0PuGpXQEeefRWgCa8Dc0obsfF5Z6TTnP_1r0X_zaGwVxs8NNxGmVX-xy8Ew9mWbO64dUdmCLi13_Se-YcUD0jX9YVhzgjDdOWExQ610WXZGaaVBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
کمیته‌داوران‌فیفا پس فردا عملکرد نامزدهای قضاوت فینال‌جام‌جهانی رو برسی میکنه و به گزینه نهایی دست‌پیدامیکنند. علی آقای فغانی در این جام جهانی سه‌بازی‌قضاوت کرد که به بهترین شکل ممکن هرسه بازی رو در آورد. یه کوچولو شانس باهاش یار باشه قطعا فینالم بهش میرسه.…</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25694" target="_blank">📅 20:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25693">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hgq1DlaimMJj9Ymq9wts78zNpxQ0sZw-PONwTovp3xF-4O2tbKH2DdGErNeCCIImGG55cKQIeNO6O6rSdrNzkm2XvTp9nSQSepcnN2ZG9ySTRFpYwZfSQoxQWAGh6n7LJbRG4DhSxAtTcSTqMAacbe9WM7Qzh2IaB2fwvYKjdSxLCyCm1P_SW39futykt6riaw6S2b6Bi2RKqBrs9pYxKuex6k08nXeJmym6pnGCKb3qGxV966-1uFs9ggQS680Uo57bTZBE-TLb40hcRa-iTetKmOdLnuhBMFlN-1UrcOyTaxOZoz0Ki-ZRvLEBQJqdm2Kte-lNXl-gnGcoouPzBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق پیگیری‌های پرشیانا؛ یاسر آسانی به باشگاه استقلال قول‌داده که از شنبه هفته آینده به تمرینات آبی‌ها اضافه‌شود. خانواده او علی الخصوص همسرش از وقوع جنگ احتمالی بین ایران و آمریکا بشدت نگرانه و مدیریت باشگاه با او صحبت کرده که خطری آسانی روتهدیدنمیکنه.…</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/25693" target="_blank">📅 20:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25692">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YX2n_0aYj_pqRxxZJWZXdwNklgzdRKmoGJ3brpPj56Zn9TMTv_FIYTdkzF2YxxN49xpI4cqTwX00it6ugG_m-thIjua-c6v3W-qWhQrOfHkzhPV_6hewaMUhuw8LLeKCSDgFzfVzPaINxlf5-8HfvFMXQS_r-96jAX0DmiXoPEUrMmcXlFADITw_YL0ctlzN3QeNiGO6-bMRpq6D-YUIvso4p5hw-Dy4BLiP69MOAsJ9IX5HMISVF8Lr3LJc2cBcD1wKHRD43QYs5-yXji5f-dj35bzbRQKa69xgE11N6FSET_mEE-4KrFED6eGnb93sEA6WFvZxHpHpq1ojS4Oiiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
👤
یاسر آسانی ستاره استقلال ساعتی قبل با ارسال نامه ای به مدیریت آبی‌ها خبر از فسخ قرار دادش با این‌تیم بدلیل عدم پرداخت مطالباتش داد.
❌
مدیربرنامه‌آسانی: باشگاه هیچ‌علاقه‌ای به ادامه همکاری دو طرفه نداشت و از قصد مطالبات آسانی رو پرداخت نکرده تا او قراردادس…</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/25692" target="_blank">📅 20:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25691">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GsLXzXk5tc303RlswzS1v7SCv_xD3uIcLOuW2FKdZfcR8bvQIC4zOGbmUelDPw3-PBeLA4y9z1YIm7Zbjf6HKTjSpOH0xOWCGy2zf-DuDL0lcZBcRBiRnLd0bYlTH_nJ0vFGavV5r6GwVUTl0b4tTDZiifHDWmHHI0tEfgCRfGFFdZr-MxKuPJRyAdjUCMLEzNHLmvVbF2zNivOoat-u5OFWueTpSDj5FXA6tvGZWYGTP9xt31D00CVu35AGr3u7q2wUcv4eTxhR2LCTFYba4jFdzQX7UTMW-kClOJxbQsvtSPFCzOsCX-dgGQv83EzKf43QOC2ZHXXv2yb4Nj-b2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رئیس‌هیات‌مدیره‌باشگاه استقلال: یاسر آسانی و منیر الحدادی با باشگاه استقلال قرارداد دارند و به ما قول دادند هفته اینده به ایران برگردند. امیدواریم به قراردادشون پایبند باشند و آن‌ها رو داشته باشیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/25691" target="_blank">📅 20:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25690">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">آخرین‌آرزویی‌که مادر عمو پورنگ داشت. فقط اونجا که میگه بالاخره‌آوردمت. عمو شما بلیت بهشت رو با همین نوکری کردن مادرت گرفتی خدا بهت صبر بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/25690" target="_blank">📅 19:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25689">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qrk7PaJFgAVM-pfSzkzogTzchkc2AZhD1Luh-iXbIDXZDjTm8NFNIr9n8gEWi6r3FYWu8Jw4fkHSz2ztDXUCg6x3ibQUS2vx_pcl0xdJ87cz7o5VMOEUENyYB1ShmHr1VDHAgSm-MOez_Xseew5aYr2Pihs_7FRNgMuLqfRHIam3jnLVzzUU9Qe8TBDhJyDgZ9yZxJvRCq35TcklWDNnAsViS_SGOQNa_u-nOACpCJqxLPUZnFvOfo2LL4b9rG3cgq9mM_j57SGTVWh0t23Us24VU2jSF5oeZrUOxZOu7d3OgjbPdi2Xoe6iX7az2fMlTEGesYLOipxDGhoNHGcy-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
عزیزم این نیمه‌نهایی جام‌جهانیه خیلی مهم تر از چیزیه که فکرش رو میکنی؛ نمیتونم جلو اسپانیا از عمد بد بازی کنم چون کشور توعه:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/25689" target="_blank">📅 19:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25687">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W7udql3SOqnUYQm6PHXCgZGHdmwI5dmpAxJqou-yiUspfYESaEEFz-4mwmH9gc8AORnKgIoAgADyPegNON43n_bATr5pFwYySntc_QHZnNn2sRLFRWUZC4kR8vt9r8tSKZKRAIJbfp37KvCNr5GxZALToB0T-BBiEOG44QqW2EXtCWN-eID4gdGs15cTG65JRnYY-WuN42hEV0nwMeRCEAnQy-V3u3ssT-JRrTBwgzVA_S-NlqstDkWl28X2ulwIdUsvEu0Rh7b70gD5Agnmdrz9Ksabxf6ltiFBZxBVByRZPo6xKuXXdcTbwvIhR4UE-YMawaVFyrTs2QUcCzmHrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XC4-mZFvrJlxH-_ldc92baaXNOAveaLlzovwrHFbPIK2PU4NbMGo4_pqyYagDOgu3GUmgWwMn89MZoCWT0ZXAQeqguDcajWRXSIykKCsSTb6hdLzoe7PE2zsXMqMEfT_iy_uRTsxZRR1Nwht3e_Z-Y56adfx7KCZy0b65OukbqfWV0PlqwujeN9B6zCifKJYA07HCoBAM5d4zVpn1RZ70WlcyJnzxRnonyZJcXXU8EeICCWfXyAtHDB3-zKE68-NZa7RpIr485giAxa8dNfU4_9jzYbCQs2jiue_kNqaGHpTNQoYxcwdVud9Ju2l2B1sQbLaTc3G3F0f8FWJmaqYkQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏐
برنامه‌دیدارهای روز 24 تیر لیگ ملت‌های والیبال؛ هفته سوم لیگ ملت‌ها از فردا شروع خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/25687" target="_blank">📅 19:35 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25686">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-31eE_QIye2F99vGwryvvdqc3e_4UQnrasRlu2I5wDE624obKkR4RwUDaeUJzJQJ0eXiKy05GdvLOc0FMCi97ucG-NjWoCl0cS6vBxZGG86lC94BJnPbeYRvZkmqRR2uWhqqfrkf5O4EZgBA1gLGDeKy1NiJsxC5Rvla7wM0vtBXRPl-Rq4XqW_fGUXlw-AHj-sg0ZJ66lZh1heW8B14r6tV53GxQr-aHvLlgK61erZGSNsqkRKVfHhPEMkmWvk1Me5miFmxeVxqxCjvG7jci5zgEiz1pCQeVPJlWZrlCHyr4VZkcQ7Cw3We0ezn6H5mey0FXMIC3sN0neCsPloTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛ با جذب مجتبی فخریان سیدمهدی رحمتی موافقت خود را با فروش پوریا لطیفی فر به پرسپولیس با رقم 600 هزار دلار به‌مدیران تیم گل گهر سیرجان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/25686" target="_blank">📅 19:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25685">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZyZpi1YxC9ejazxKmAFSvB2hYjCfGwbm9dnZQIfgj3u0vcf-1BjRkcro5e5eIQ2i3FJa-Pt_7Igb_Cwk3d6gzt-cmpRcqFhmmPTr2A5GHaYORLJzRiNrHkLuwaLu4IHp5lzUPiJA-My6i2OizXVB1cth7Vd2t4i6j7VAR591ag9xf8MfhvgLnPhp-l3_8dDLFk82wL_UrDfAUolk5oXSIeGwSkoZGPSNgBV69srVfZEgl-LFRZ-FAj2vvyD7omfU7jq89b_wdgz4XvXWo11d7ugKPg5VYWYx2Up88XTEH2qTkoppmTLme6hjHmb75ZWfYltd3WFDP9ffe84hf1RTWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی‌پرشیانا؛باشگاه‌استقلال علاوه‌ بر پین؛ با یک‌مربی اسپانیایی که بالاترین مدرک مربیگری اروپا رو داره در حال انجام مذاکرات نهایی است و به احتمال بسیار زیاد با او قرارداد امضا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/persiana_Soccer/25685" target="_blank">📅 19:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25683">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pgXRPxsAv2dH_Tb1bIZn8KyB0bhNSzlubwhW6jl0BOoofI3j-rkXvZuw6fs6eOWZBRoTQJ1Dl-5rPpLv8LJEoNsXS9zGkHhsP9K6HKKH6oMIQ5ZS0Y8lw44dr3Rt7tcA3Nvc3MotxfaraUuPyMx1O2d2HG9KG7yMQSv89znclLuoIIfc4Y5GosgOMuuRs3MQm33pWWo3cr4JmzBlJPENys6fvSWrIzP7vL8inBR6UHOy9-Lc0nWoAz2eoBN_ls8nS76h0RuINu2XQbFgkq0Yi7ExxmJ21YRtVjJXHQ_HAUiDT9I6v02xChVkdqNagKbkot7EOBIJiQn8HOaAz7btNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EWwOTnvfcgW-R29cqbwvBMySqVTV0lxWtrWeykp4IEFf7_NdXqgOCVNtKmma91rClJG82xriLbYEveAiq0AN87xuyM-QJK4gIewD4WTPF5EZQ9eKxcbxEVTOVHuKFbdWEp9m-bv2AwlocBk73UCS9sIgMwhV2upVLLLuR4YnuUgLKITyLNWczJTPVPr5mh8GCgnYMdie0_rsMmiuVwQMZEOjPnFxC4CscLYg9s2Yh_4LGnst9JSf9UAYeyXaCZk9NvaAsm6q22R8JbRlq1gtg9Uz3PqMjCdUXewY3rBiYHcumCHaR83B_mZI1awp4UtVg_l3h66pZdV1LMla8YEs-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇫🇷
عزیزم این نیمه‌نهایی جام‌جهانیه خیلی مهم تر از چیزیه که فکرش رو میکنی؛ نمیتونم جلو اسپانیا از عمد بد بازی کنم چون کشور توعه:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/persiana_Soccer/25683" target="_blank">📅 18:46 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
