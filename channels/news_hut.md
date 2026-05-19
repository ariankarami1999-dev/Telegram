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
<img src="https://cdn4.telesco.pe/file/vc1geowBBvFRuk8szsd1Yl6W_hWUUDmwdm6-XPibxRacoeKClnHVbmOsrKx1U6Jl-kCIdEVx3VZoTySnqm5HRccBhUz414zFOfYRx89NIILyFSiMmpJ7rsfOUFR0Y2Yw_RlhmfUB4Gs_ND7ZKgP_DrA0CpxzMNDtvffrLoN9bklKGbC8_MV1lVB1k5oNxo1EG93xWrFJbqZxcAn6XS_JYwkhHmxVaMrYdcCA3XG7KkCZGZRRYQ8-lrPmzRVRL-KB-42PPD-MRrchOc5L36Nco-rNsH82-ejZwFM0A2mJOsCfwzhZguxmg-wucEe3bidTtWSDwrxexBo68nNJm5V6oQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 144K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-29 14:16:55</div>
<hr>

<div class="tg-post" id="msg-64963">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lc1MQqGJ08MCePeYpvSASVmEfJ-WoTNbreiXhrDA7gHhvV-rqCdpx0p0b8Mlh7yFu1FJYnYNrrNiFXkwFjKt0NimfPgCmYFMDtuvcbrgObLT-twGvkFPCaCuYZ_i0KGbeYY-Q9Y_IpJ4wAFy3574uPlPu13xr2B4lNe4skXPuAVrznMiLjop2ttjINoF4fU0HApECblnweg_PyILpiW94IL08cEwbINgqyW8Aw9Nncow3VO6Ow5IbdW1HYIyZM_e_9x9r6WDSMHGV1P8L77J205s5j46hRiLnV6qHr6QDHDrESET1VH9k7oVaoHzC2hhdeGgGSw72mdr3HM_QFD-dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:   من از طرف امیر قطر، ولیعهد عربستان و رئیس امارات خواسته شدم که حمله‌ای که برای فردا علیه ایران برنامه‌ریزی شده بود رو فعلاً متوقف کنم، چون مذاکرات جدی در جریانه و احتمال یه توافق وجود داره. این توافق به نظرشون می‌تونه شامل این باشه که ایران به…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/64963" target="_blank">📅 01:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64962">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cYjERLEY64-U4uYhPgkfPG4BFiFB9JfqImhyFZyDPHUV2T5eJyAEYq_wOWmT2UtUNjWESA9tAKR2kxskrN90jJBNgDQhAmFQ75NCuBHNXBYny5iRSZWnGsxPISf4EmAHZlOK7Z5hqwKpjMrk0PHjWFtUMOUq6d_sWWGDnUQAvkhHsdd4c9uOSv5Pmf7RTUb2MOq7xG0rjJUD_Zgn05POEcqKkDhlg8b5NNzCU-3uDGgng3a7GDMgB15pOY9Ogui5hrj48qSYXhNfkTFMu8ttlUiYh86NKMTFYtIanPJd26tp9tv7s2bnI0yIS4AxxYTiIDbpd-qJsvVkjLwMZReRrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:
من از طرف امیر قطر، ولیعهد عربستان و رئیس امارات خواسته شدم که حمله‌ای که برای فردا علیه ایران برنامه‌ریزی شده بود رو فعلاً متوقف کنم، چون مذاکرات جدی در جریانه و احتمال یه توافق وجود داره. این توافق به نظرشون می‌تونه شامل این باشه که ایران به سلاح هسته‌ای دست پیدا نکنه.
با توجه به احترامم به این رهبران، به ارتش آمریکا دستور دادم فعلاً حمله انجام نشه، اما همزمان آماده‌باش کامل هستیم که اگه توافقی به نتیجه نرسه، در هر لحظه یه حمله گسترده رو شروع کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/64962" target="_blank">📅 22:39 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64961">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sgmrUZ1Yre1M4d9ZPIctvlD2Z83yu-FUYYEiE5PitQ3cP9nowFzhYr5WACOaDOaFkJZw6rgA1NHnceskOXQAz7Q066Dxc-CeaVcad38w72wENVkTGmIkMYcULrcTeSUxVumd89RmJrFT0a6evpqbxpJqs4rhbhsDP7VlQmHsc1Otaah8DIPAhr8EODApPEoNAGXnNGFLd4bMzIfHW86c8mdlMT0fPPQ116T60bLec5qnAVgfuhnF7mDewx4e-Ij7vqatxC2HWNbtpjDWL691VBPgIRuabhzEgHlDqv35CRxLUN8p_2TprxjHGoQwqxw48T0TfU2-aKg_4t6Y1faEdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ:
«اگر ایران تسلیم شود، اعتراف کند که نیروی دریایی‌اش از بین رفته و در ته دریا است، و نیروی هوایی‌اش دیگر با ما نیست، و اگر کل ارتش‌شان از تهران خارج شود، سلاح‌ها را رها کرده و دست‌ها را بالا ببرند، هر کدام فریاد بزنند «من تسلیم می‌شوم، من تسلیم می‌شوم» در حالی که پرچم سفید نماینده را به شدت تکان می‌دهند، و اگر تمام رهبران باقی‌مانده‌شان همه «اسناد تسلیم» لازم را امضا کنند و شکست خود را در برابر قدرت و نیروی بزرگ و باشکوه ایالات متحده آمریکا بپذیرند، روزنامه‌های در حال سقوط نیویورک تایمز، وال استریت ژورنال چین (WSJ!)، سی‌ان‌ان فاسد و اکنون بی‌اهمیت، و همه اعضای دیگر رسانه‌های خبری جعلی، تیتر خواهند زد که ایران پیروزی استادانه و درخشانی بر ایالات متحده آمریکا داشته است، حتی نزدیک هم نبود. دموکرات‌ها و رسانه‌ها کاملاً راه خود را گم کرده‌اند. آنها کاملاً دیوانه شده‌اند!!!»
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/64961" target="_blank">📅 18:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64959">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gPBLePufAL-uLBfwCt2dSCHyrdue-5VoGQ2rooCcJuQ6u9nM2ABKWW12HF1o4BTZrYpkzsE_I759a_KqKV7CkcSQ4ZenAiFJcBw6ah0VSefEmqdF86lSxn0pYbKxWAvEssy5nfDwS6DZqpB5x9CFAT8qjZf_sldXpD-q6UsqNBjnBnGHfmZLG2NdKIDUjlGqTdKYfbgfgzMKvDdK7JCIdf2gtRJiY7eaz4yPp66yd6CzWr7uuNNe-6Hl-kp_9BM52BC524WnpmRaSSolvTL5lmm2dfligjqsWtKcnl5u36uL0w0G0LyLWVKdhmjUfPyaNA3y892DfGgYqhAfu9_0GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X0e7TY39qUxSg1bpkG39JX-ELps6sXz0sKCD4rMqDwVnGaGU6AwH88TLFr9WJS7lUlJYueEVk3c9Yn_g_9NaiL2gsIf99XVLD9GfVH2akTpcARtbxjYX91S7fPE6wc9mVPRNo8eV9LoxJ6jc6FEvMS7rLfiNMJWFhelJKid906YmMheCU46lXBmSR1ysKekqwAQ9wwac7wZWa3Wz8de7BCwA4dDR0a7WT68vWR0JdTnP1nqj7x0EircPLAiGdR0Hkf-aloj4PK3JnAWd7xAfEbh-xSKVg5C9pNLBkKv7DEP--e0dt1RTTLw3v20oDf4MvYS7inlE03KsRAE2KUW4ag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قیمت خودرو ، ۲۸ اردیبهشت‌ماه ۱۴۰۵
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/64959" target="_blank">📅 14:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64952">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Myc1lrt2HCJFrJkQYMCjmwYU1743jm8GjIV_PA9zvqvVVMsmH9a7FuKgCP-kimlLe5Q9fC1weHo5jkA42azEIKlnQTSuovolprJweVT9GGG_boHX5Y5C9i2MQeqTwBsngiln-KrIlrLmncE_nLiP_n0ehzdnAo8Te_7wKuBzExM_CZsH047vt4lP4VhLq34vFKZo66ywq08ow20YAHr9Zbvu-aa8cWjdbp4t0lcZU-Gr3WLmmZKB74w80b6GvWOk-g500x51No00OFlujymPnrDQxCKY4xfLhW6TMRoTcpwOP0znK3CjOaxufqz65GXfXCcf-_SjYQ7uNDHSFbaVGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VCZgNx13n0CfWy8sipw5OpF54hKPNGDWMGNGz1a5DdAD9N80qTCZUvV03xaxNfjCvM7mnz2FOM0_UygGc7CB1EK7sko_nPotmC-e4kvVZzK8V7fk9_uEqAD8DdnN5ZqRyIsTRFF-RJE2efcs3I-YdiU4UkY0MtoGzXsZr7TDvac7VtAkOsOga2mTufP-x3WkIKW6k2NVgZKIARlbTBr2DozrOuWfEY9HLyvBUHxnBPoP78_oBBUOUUx1h6CUBYrGI8m76hSRh7rCFRfMZrNg19Nn3nDSKvewswtHforYGqGW1ZCOLq5I-8Ph4whx2FiLaf5pOuN1YEM8QLQ10YLC2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Gij3n4lqIqVXYRk69sPRAgpM4xKD69P242dWTQnoAEtEC4-4gQ0DKOjbJtb57r7PeWO1N1gTkL4a6CQISDtdwEFNR1BzeKFOFF9NZE8MyFAbIAWgmndHGoZLrWWaqV9QGYZw0CZJIyhCZq6bTNYxqffFzaQst8V9PBXTuXEQsEaVdleZq4tDiQ5YQR4SXGpOGCVD9P_wLKjghJ-IqvZ-5z2ypCTllKtY9uKel2GzTD6BCVqoCQJ-B8WKaugafj_8iOwh1Zr4C5zvJiRJKMN0AsSk9nDPXoCIRCrAe_v6JG6MtpLNemNl_t6J50nK86fTsWgvBOOCeVxX4pVqBnGD3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rpwvmIufOClkSVZbiGp3BLPBukcyyaQUyc5jFk2ccvljvyWH0YVyPyh3qIGHcW7-nfAd0zrb-mn2QtaXgjwXnl1Em_iMd7V2fDEo2Coo7A4UOqtUDMZfeVXpx6JisgwGj-G0YWf3GcA0dCDxFd9TjLrn767Lu1XZiOQwKtvMjaU9FFz8agQPUFHvioGH88AHZ4ipoOVn3G3Rb-6pAFwC7S-Iaz0Kt34PavMw7OCBh8U-VHNbBa8S3rSm3CqH5et1s-Vwgf1qjXbWzJvVqJdJVhO_jhDDwubsv_81Aagqz6QgEBO9PY9q0YJOuioskJUJ3ldtgGoHNm9_PUkRBZaaDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vZ1YIX-bok-1of3kCVSR-V3FdO3-Fsgo1e5FvUdIlkPFvCm_KxyCN6W8obopn-mfCooWYyJHNNEPA2txo8s_XcOYIJYtYkdhwJXYTrpRm1uawkkcKARM2sapBxREkAXp-JRjgD3UPB3wZD-La-IQ2eO37OBMjFfAt9AJnL3IfaAHKIzlYsrdtbo1sQ3Wz3f9GnmVm3SCzeBcW2snGLAZu0HO6uag6wsuVbalGCZmSGUJc4YjaMMyiDOgoan0w_or5sWlaiNf7kQvxBvcJVg1Vb2mstRVj-5twW0uMXhf94QBUHLMf9ak2RtoSG1mm9rMpeZ1HGjZ6tis_cLvZGzP9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ml7d4t1P5WctohlyzU2Yzxv3_U-64ZbHwlKfs_j1XGt1MSeEpDWPtZ4jTt175pAiluW9mTRCOEC7RSu32LoCfnuQwRCg5mK-m2sXgPn3-KoEnyLAIgc0-T9c6W9epNyxxezvFGiBq3l9VS_qccOsmLpBRH7b_6JJVnM0qXbG5MJ0cKLRaykKrkoIMMEQXEou5zFaoeKswhWUjPL8ShPVCrKMPf46kpWhz1ZO-2f24N9uEocnY8pcDbvTit2o-ATFjNBmPtVS65pQTvtwxA3r5MS9wro12uVfRTKb5Poq0ZHwOs-6hj5M-LMjA53Gfp4DX24h4aT8lUuTNESMIeqLpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FL3f-gvT31aMWZu-WBGIttY70wlqWcNb5dlbAU69JKSjpwpyi1IMvLfN1c7bkcIAl1_Zw5I0YrCtaHOMSaSjEcAdPCh0zYfoyalzsj2HGyuTq3tE7ABF6f9EAnG28Tvh5UHNhHxKTLyZCQhqqGEQWa-f0iij_L1W673GffqZohpZDcurpgDm1Z5mzUpj3WYWSHk3omYsmbK0yw1-bxmT_DakvcCeL-g4mdF_DeOwq28E1n6NbDsNSWttLvxxstfRaA1ZdqUi9_sSRnC8gBYdJLFES7xyeN_kDGMCO3kd8-5xmhqyAi_c8twK5bbhq2m8gyhlssLJs7cojE9wm2KC1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
پست های دیشب ترامپ دلقک که با هوش مصنوعی ساخته.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/64952" target="_blank">📅 10:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64951">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mqgyBGY1D0dkRpg5D7t3p6JcJF7Mdku2gmBJ9ki1dI1uwDIQV_m4ZlGcICYgDydAhVx5DGV6IjUSvVGPIxiy9UFLoMh-Gj-PUgONKGrYkX19t3lBIBrxXOFWyIUYJcCY_fUMD_Vxw_gIh701XynvCMZ0jZgz9NqE94XQKR1jvqwdvXS_Bbd4tnZcohu72Naq0ydm0Ks5w4AqThsKlXiiRA3ax_dsT-zlL905Qs4Iu-lDwEchOeZ0attLIUxReG3ZyNxBldt0ubbB26c48kgeu_QPgfwGNlgT2aLXjBc2SziD4VUju1sC1KXCcOFNOLklswQ39P7vzWiLC6hlNzvC7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پست عجیب حسین دهباشی سازنده ویدئو تبلیغاتی حسن روحانی تو انتخابات ۱۳۹۶:
حملات و ترورهای دشمن تا رهبری حسن روحانی ادامه خواهد داشت
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/64951" target="_blank">📅 10:03 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64950">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/VbmlOV6y7DVyNi2Tbfid02Zi4A38jQIoMtfqxKnangRQusGW690jbGA7_jExgJ3LWvxUFVkDInBY_Ue6FOIb9XmNflnlIiqn8enHfbHZLvOPUa6LcrFDhFo7cUyDjuAqgy8ijgwJalV5IdmiZXe5gkKDNdQJRhshO4ScH6Q_V7OCvRFY1x2jipr1miThYVKGrndZHHrnD9k2yZZLFt9uH8k4F2u_d896VFWlkuSUCVEtoQO9eNraE3W0DYxntFH5dZaTdekbCYvVxp1KTEjj4tGottbPgo6cM2eECfnLJwV2cWS-NfP6DZ5zaA74Hvh_0ox4eCeFPqopVh_UreQ6rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان در شبکه اجتماعی که فیلتر شده
روز ارتباطاتی که قطع شده رو تبریک گفت
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/64950" target="_blank">📅 21:45 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64949">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tAtaJutOjt4YEtFis2-H8u7RJYZi0eYaubygoiSKORN5J0JJZjxzUAa4ML6iNnqiCXkvZGVx3PCrZ2St4tHQ5N7R2YKrDMOjUNBdD5zvtPboC-AEgEcQX4JKFjASwAlzeING4f_jRhru2CsTZLLEp__72vV8JxnuZUojCiI-GCIZu1Bq8iTY_uogdcbBfdEfc6zSz0N44j-AiB2fxZETfZd4aYRmkhnMIhgQnYkki6tJN51vuP2yKzRXK98yS7uxnc5L4n5hPeSTSV9GrYR8BPEbN7EEWi_NS1_ffjwSPC1BCvv-RT0pJg4KXn0dGktknObb9mtSXVAf3pd1z-yhtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🆓
رفقا
توجه توجه
✅
درآمد تضمینی روزانه 35 میلیون در منزل
🌟
تمامی ضرر هایی که این چند وقت بخاطر جنگ دادی  رو جبران کن
✔️
🚨
⚡
⚡
⚡
⚡
⚡
⚡
https://t.me/+ArmBt6ZWMF84ZDlk
https://t.me/+ArmBt6ZWMF84ZDlk</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/64949" target="_blank">📅 21:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64948">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/632a1eba8a.mp4?token=rW3C1ejYoh0yF1I2vKTXCNHE-Q13tnjTqbCIn2pUY70WKsuLvm6eUceBJSlbuG3bzS-J_Vp7T7bdLvepJISL7g3RpztWzq2W8Po0yqucfalaUSZ3cbbMMxL2rtkOp9hKXWTqNQ8xTGylv-vYaGGLd01NbSPtY3F1-3i-DpEO7ZEidkHwlx57I2MYrx1l2p18EEyrRxSH7MuXM7YKWwuDqjTp8oO5lA6IzfP4ov1RNVLb9faGn-ichtzwQagVo1JKMH-_gieS1mdClpBy9qlBHmL4fXKDaoscB6jEi-jsdLGp72ueMzO4f-svvi4ug800pbIBzE44Fjs6nXtpLWW2Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/632a1eba8a.mp4?token=rW3C1ejYoh0yF1I2vKTXCNHE-Q13tnjTqbCIn2pUY70WKsuLvm6eUceBJSlbuG3bzS-J_Vp7T7bdLvepJISL7g3RpztWzq2W8Po0yqucfalaUSZ3cbbMMxL2rtkOp9hKXWTqNQ8xTGylv-vYaGGLd01NbSPtY3F1-3i-DpEO7ZEidkHwlx57I2MYrx1l2p18EEyrRxSH7MuXM7YKWwuDqjTp8oO5lA6IzfP4ov1RNVLb9faGn-ichtzwQagVo1JKMH-_gieS1mdClpBy9qlBHmL4fXKDaoscB6jEi-jsdLGp72ueMzO4f-svvi4ug800pbIBzE44Fjs6nXtpLWW2Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
سناتور لیندسی گراهام:
بر اساس تحلیل من، هیچ چیزی نشان نمی‌دهد که افرادی که اکنون در قدرت هستند با قبل متفاوت باشند
آنها هنوز هم می‌خواهند جهان را ترور کنند، اسرائیل را نابود کنند و به ما حمله کنند.
هر قیمتی که لازم باشد بپردازیم، خواهیم پرداخت.
چرچیل چه گفت؟ «هر قیمتی که لازم باشد برای شکست هیتلر بپردازیم، خواهیم پرداخت.»
همین موضوع درباره ایران هم صدق می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/64948" target="_blank">📅 20:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64947">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">یک سری کانفیگ فروش طی یک حرکت بی‌شرفانه برا سرور هاشون ضریب گذاشتن، یعنی شما ۱۰۰ مگابیت مصرف می‌کنید ولی حجم مصرفی ضربدر یک عدد می‌شه، حالا ۲ یا ۳ یا هر عدد دیگه‌ای  اگه این حرکت کصشرتونو جمع نکنید تک تک اسم می‌برم تا نه آبرویی بمونه نه مشتری‌ای @News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/64947" target="_blank">📅 19:56 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64946">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">تسنیم: ممباقر گذاشتیم نماینده ویژه جمهوری اسلامی تو امور چین
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/64946" target="_blank">📅 12:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64945">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/fee67a1237.mp4?token=ROcBhdfRXg8Adt15yZqYh0tBzOCCjr_ZK9g8N7VEyBTh_UFJWQ9XqFISykBoeu5s4Z3C4ApDUNbRc1xLWq_H60vW0dlJeZYCQ47-MEe284sw-Ufbg81ewI4XxsqAcfbXRCgvpRJaocxRJ2UM88FbaHeTtCd7bS0mV74uCaai30FFVcRTwewtm7CMIt9xGuLRp4CdmQD5FBHFrGQA685TFjnr3g75z7Bl8jfIG8QKlJ3ma36_F2PwYRlEna3pqzga1wEo4sBc-BcmRn8JcdauLl_Fi-A_0jF72bazqT6v8DcPfB_dzfj6cqFq1s0kmgd43BP9TrbkcqusSYds2k_syg" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/fee67a1237.mp4?token=ROcBhdfRXg8Adt15yZqYh0tBzOCCjr_ZK9g8N7VEyBTh_UFJWQ9XqFISykBoeu5s4Z3C4ApDUNbRc1xLWq_H60vW0dlJeZYCQ47-MEe284sw-Ufbg81ewI4XxsqAcfbXRCgvpRJaocxRJ2UM88FbaHeTtCd7bS0mV74uCaai30FFVcRTwewtm7CMIt9xGuLRp4CdmQD5FBHFrGQA685TFjnr3g75z7Bl8jfIG8QKlJ3ma36_F2PwYRlEna3pqzga1wEo4sBc-BcmRn8JcdauLl_Fi-A_0jF72bazqT6v8DcPfB_dzfj6cqFq1s0kmgd43BP9TrbkcqusSYds2k_syg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏مجری صدا وسیما : خواهش می‌کنم سلام من رو به مجتبی خامنه‌ای برسونید.
‏
حدادعادل: والا من خودم به دامادم دسترسی ندارم، از همین‌جا بهش سلام می‌رسونم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/64945" target="_blank">📅 10:23 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64944">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Bo0zm58VSWAAuJeOsl9yFLdWCjOp_lrMdgrxth-yC_TW0xt2-niJ2EU2I1jJZVEWySybKn_HOJf-UBxOA0lnc0fRWwkNMwL6XSn4nv7biljy-byKoaGRsfcE6lKB1fNL4flE1OKpxWG2xdkDxv_EcUSa0AzNLW0diH6VDni7FkOhpCKF1xTNUJnwR7iQ8EiADdD4Cpqg9YyySlc6E0XGka8K3VZS-uRJBSwTkuWY36zLn5H7XLxjAAemRcHpNbh6iq2rMcgKVQTXSqCHpqD1vswHfBMbTuUvBEzahHBCFTrL6d-Voadki6sGhSJKkU8-M2zYxHA9P9kvqXudsOxtWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیلی‌میل: کیر میخواد از نخست‌وزیری انگلیس استعفا بده
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/64944" target="_blank">📅 07:55 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64943">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TijvJO-khck6tH2qCtq8PDaQ3BMps-CMpbKcF6QyPKiUVEAz97LQhXBZfPSgwZitVaGhhdF6MoFRSiZDyPece-RhpwuSwhnuPB4FQGgRxR_QTYPhMmbtbVNwoq4NKV4PYzQGZbM2sO-axL9NoNZ0zW4eAClad0CYrv3cnW2LPNYj85bk1yuyOtVyZpiQ-LdtIMC3klSnmS1f9xHstUWAEehUtooAGF977KLtqZLaULjDF118DDZCAJU3VIluzLhGejc99gdg32BTHZgHMcmA9-axgQZklqAeakXMGElg-W6sobpNgVLTkpK-HMUnDVtpVMSxV5EiOlJx76Wm8_wGVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ در سوشال تروث: «این آرامشِ پیش از طوفان بود»
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/64943" target="_blank">📅 00:08 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64942">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">مثل اینکه شمال کشور زلزله‌ی نسبتاً شدیدی اومده، مراقب پس‌لرزه هاش باشید
❤️
‌
#hjAly</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/64942" target="_blank">📅 20:31 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64940">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VjNPVwmIFpmEGL3vjOciXOHRaK_r-POPtEVbOcpr98c9rkOaIfzAAeVCsKE-wwIc73w7jAY3Oj7TFHDOPLcNK5_OYcv8CR4Dw4-AMO7ntCgSBRd89IkDVvG3ClepG41WWZtg0hR203rXzoZJZ2FwjvprxFx2pd2TjdHGsPyPe6LinmuqvyceIR6ttDxfmtbIF02GTBVktDlT8Z0EFkkQfyjM2_LUZpsmB2ihaErK04AsdXwibhzZ7LG81nagtLMvJCpnYHUmCdksdyquzLuMtgPOwKOIa_q8MjyFaKX-7JZ3wwlW57HmQ27kPU4iuCi-Ozaqb4OY2KtugZ25xBRS0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f0ac308ebe.mp4?token=jma-NmpQABFOzMCodIz3S-Z-AlM4SajKwwdxzg8kVV3wqCjALD7R_N4fzd2QueKrQ7XgdWyyLQJScqbTfgDkqzwE4V06xT-7Gc0806tzjDlTxljnKbO9jyYsR5Mw4ujiDvHoQW0Vrugd5ZST1FohChpY-ROr9GWph4OMPuiCMT9XG2Kq-y7tdMWVHGc_gAGPYPRK5S_PJlhfFoNg0zUYEfIJwzzFGUYmLGrg61687KVMgf280s2LYA55q5-0su26hS2J6TrOo_EJuhD6ScisVY8qnyQ7H5nqZCle4xJoLU6TJ5Itg3bhukTcLYJ6lKfJo0x4M35XapOZMVK9LJjfuA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f0ac308ebe.mp4?token=jma-NmpQABFOzMCodIz3S-Z-AlM4SajKwwdxzg8kVV3wqCjALD7R_N4fzd2QueKrQ7XgdWyyLQJScqbTfgDkqzwE4V06xT-7Gc0806tzjDlTxljnKbO9jyYsR5Mw4ujiDvHoQW0Vrugd5ZST1FohChpY-ROr9GWph4OMPuiCMT9XG2Kq-y7tdMWVHGc_gAGPYPRK5S_PJlhfFoNg0zUYEfIJwzzFGUYmLGrg61687KVMgf280s2LYA55q5-0su26hS2J6TrOo_EJuhD6ScisVY8qnyQ7H5nqZCle4xJoLU6TJ5Itg3bhukTcLYJ6lKfJo0x4M35XapOZMVK9LJjfuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چند طرفدار فلسطین از برج ایفل بالا رفتند و پرچم فلسطین را از طبقه اول آن آویزان کردند
شش نفر از این افراد توسط پلیس دستگیر شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/64940" target="_blank">📅 19:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64939">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQ0hR2RD_Km-mHtZJBbHubV_EyAll02Or71Dy_MzfyDWGrtrjNdxv4lBlDWrEq43m4iRsYcsd0EnEtBoVEo8EZgkHPevMhkEVbfLHKNJM-VGR2pv0lw7la3M4oZacQK6BMEJZmJPmEBqtToOycXhAxMe5cont1N0VxvI33hahxOwhjfcUxvfnCcBYUfvuA5_TBBAgOYhefGU3-nLRMnM6vjGmVJZzza7p9Z7hMlqqrP7Xu7z5VN01uvUUF4a8jHnmc_HfxFpABZJA6H5bJ0poyFXsan4gkP4qJCABE2P_rTLqR1kN8dMDjTZEQ8XpSHlQ1rpEQ6B69yAJbmzbAkbMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پست ترامپ در تروث‌سوشال:
بازی نداریم! تماشا کن قراره بعدش تو موضع مورد علاقت چه اتفاقی رخ میده!
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/64939" target="_blank">📅 18:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64938">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔥
🔥
آفر انفجاری امن‌نت
🔥
🔥
💥
گیگی ۱۷۵ تومن
🎁
۳۰٪ تخفیف خرید اول
کد:
AmnNet30
⏳
فقط تا پایان امشب
❗️
ظرفیت محدود
⚡️
اتصال پایدار | تحویل فوری
👇
برای خرید سریع کلیک کن
🤖
@Amnnet_admin_bot</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/64938" target="_blank">📅 18:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64936">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HhOzXM7eFKzMx0hWDeJ6nFj4s_R-aBQIOjYqeCj6POO9zmLP9W9If-8GYX5D1883YwuBYHdb9nPIjXViN5ZUp-p5-7WjYq_eiycz8N3s0XapSeRMhO9zW0ajsMg7e7pDoi31eOTISruyBEmo4Nr9VJ_YMGhCjddAam0Qv3bgELEnkvQ1D_r7KRrryhc6BpV597LZdsc0qnbayOZXTBs6BVWHbG_lyFnSPfBcdpvxtsHiF4akfF_gQLl6-Y19etfQyewP9zLL6wOlVWiADnOMlejszAYbLA6ltljArqObd3rMCUWWtZxGF0VAz2190R6QCzmkFUf2cTzwt1dzKvtlFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PLj1IjTUrfx39Z08CHnhw45Jn0NN0FydAFVWl7XghZOMBv8qd1Voks2ka5VovD9UgZ04wNQb1JjJRLEm_Yb9wJx2f7V7rFo07p3-1bCkcDHOKbSvKWtl_f2GbSrMmxkzMhGN2cJ4o17hANuM05jdesokaKOYWpEwde6yx_YhUGZ1xispWnku543WJruCr3T_0MuReRIUO0kgItAcpFCfgWqAxsCWOwTeBcX1UXaPAoM4rhbO1t_nHos2znbBES3eFb_uM8apZXnPrOUcEUl9TkvGl4iQoatQJ44JxRl2ji1oOqFIDw1Ai-MpE9y0U1Dc2rW9yt3THD6k5d3fHhMFEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیکتاتور‌ها مثل هم رفتار می‌کنند
دیکتاتور ها مثل هم سقوط می‌کند
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/64936" target="_blank">📅 10:41 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64935">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🇮🇱
کانال۱۲ اسرائیل گزارش داد که در اسرائیل برآورد می‌شود دونالد ترامپ در ۲۴ ساعت آینده درباره اقدام نظامی علیه جمهوری اسلامی تصمیم بگیرد
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/64935" target="_blank">📅 10:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64934">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">عه امروز واقعاً روز پسره؟ روزمون مبارک
🕺
#hjAly
‌</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/64934" target="_blank">📅 10:33 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64933">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RKcdVd3pEDilt3FWjotwdhlKsAQJBCw1NtFStHN8IabxW3E5BetPAuCV0OrgfUVIxxMQUO9eW27f-Be1B-TwDV5YXeB3seA82JK0fOJ1JHBzMaq1wxrm_7KVLK-3-kF_AmNCkkW7Q9Jk0Zl2U8d3QfCFzlfrl-Ee1IJa5QjM7pHcQeSDqFMGXgo8q_jYjPRsflyW2UkvhhFMYL_zb_qNamlag-j9R9amoQ72crFwRNQHk5aXqyMhe-EWPTjEc0_eqEljOgr1nuV_HFgjkoIOq3C897LI2G-OMt3sUIpTcyqZWdH9JlzdB-sd6feCMyr8MCpQhfNMl3RXZp56lP-LHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عزالدین حداد، رئیس شاخه نظامی حماس کشته شد
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/64933" target="_blank">📅 22:28 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64932">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39ff7f49a4.mp4?token=JOIQC-ScE4O5UeRZgMkOaX_lc2-In0GwFCL-_mZwuVv50oXgpBODtnMvI9z9oBcHZS1f8jdPEp-_nOaF2WSwcFc9in6OX-lbZ7eRRE-sDOiCFuBOaoC2Z2Kwzhzc2TKn1irSMyH2BFUQLGQZlsl6k1jEgjB5MQCgDFCmtLrUwLHbPZy-4r_NzVZg7KnhVH-p22BDPj16BDwZoZ2_u34vWGm-jzBZ4nPpOD7p_4iX7tHfkeQQIQ69SOfr9DLkIuysUGtugSCTgXZODjvPN4DtNY-7J28BdxUQ8xmpl9K3JYFRAEOiwl8_XcIdS5wTwGN7oYtchldkTGITbphuuxUZEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39ff7f49a4.mp4?token=JOIQC-ScE4O5UeRZgMkOaX_lc2-In0GwFCL-_mZwuVv50oXgpBODtnMvI9z9oBcHZS1f8jdPEp-_nOaF2WSwcFc9in6OX-lbZ7eRRE-sDOiCFuBOaoC2Z2Kwzhzc2TKn1irSMyH2BFUQLGQZlsl6k1jEgjB5MQCgDFCmtLrUwLHbPZy-4r_NzVZg7KnhVH-p22BDPj16BDwZoZ2_u34vWGm-jzBZ4nPpOD7p_4iX7tHfkeQQIQ69SOfr9DLkIuysUGtugSCTgXZODjvPN4DtNY-7J28BdxUQ8xmpl9K3JYFRAEOiwl8_XcIdS5wTwGN7oYtchldkTGITbphuuxUZEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار
: آیا آخرین پیشنهاد ایران را رد کرده‌اید؟
🇺🇸
ترامپ:
نگاهش کردم، و اگر جمله اولش را دوست نداشته باشم، کلش را دور می‌اندازم.
🎙
خبرنگار
: جمله اول چه بود؟
🇺🇸
ترامپ:
یک جمله غیرقابل‌قبول. اگر آن‌ها بخواهند هر نوع برنامه هسته‌ای، به هر شکلی، داشته باشند، بقیه‌اش را اصلاً نمی‌خوانم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/64932" target="_blank">📅 20:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64931">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
📱
👑
آی‌پی های جدید برای فیلترشکن شیر و خورشید
🛜
‌ ‌ ‌ همراه اول
2.22.250.149
23.58.193.140</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/64931" target="_blank">📅 19:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64929">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">همه‌ی اعضاء هیأت آمریکایی قبل از اینکه سوار «ایر فورس وان» بشن و پکن رو ترک کنن، هر چی که از میزبان‌های چینی گرفته بودن [هدیه و یادگاری]، همش رو همون‌جا انداختن تو سطل زباله.
دلیل این کار احتمال جاسوسی بوده
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/64929" target="_blank">📅 17:50 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64928">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0_SOn7l4GdRWPxitnjati9JoPybl2LT6jw8IJkhmJnwxZP7zN4qxV4ZANdmF4XrqRBQQ_oKNJzc5o_v_hnxHpL5JFSpZkNXXSlY0iVIKqGF1VNFhBuhX0zFVuCL99M-0oN5OWr9mJG6y1S1WlCTS-xNsY7VSWb5B2UN-07L2fzTeWksvNUILXrjpNyWKyjC0fglory0ybDlBNEuT9acter42CXCxOxeDieXGzhaEKtd2Ehw5t6UJSfTwnhuiSHJBvNehE24Qn1zRuEtBcSNkODQTyRhk6AicHbazWZJQKSieYDXWZzVadYDL8W6rlybZ0f3t3uMcMxA-YR6Hoybiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنظر می‌رسه تکلیف خیلی از مسائلِ کشور در دیدار آخر هفته بین ترامپ و شی مشخص می‌شه</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/64928" target="_blank">📅 14:47 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64927">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری؛ ترامپ: تعلیق ۲۰ ساله‌ی غنی‌سازی باید یک تعهد واقعی باشد  @News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/64927" target="_blank">📅 14:39 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64926">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#مهم؛ ترامپ: با تعلیق ۲۰ ساله‌ی برنامه هسته‌ای ایران موافقم  @News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/64926" target="_blank">📅 14:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64925">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#مهم
؛ ترامپ: با تعلیق ۲۰ ساله‌ی برنامه هسته‌ای ایران موافقم
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/64925" target="_blank">📅 14:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64924">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">تنها هدف حاکمیت فعلی، رسیدن به اولین شرط هست و بقیه شرط بیشتر نمایشی هستند برای بستن دهان طرفداران، چون به خوبی ‌می‌دونند که ترامپ، اوباما نیست و تا زمان انجام توافق، قرار نیست تحریمی لغو شه یا اموال بلوک شده آزاد شه!  منتها ترامپ به خوبی برنامه‌ی جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/64924" target="_blank">📅 14:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64923">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
ایران از چند روز پیش منتظر پاسخ آمریکا به این پیشنهاد پنج‌بندی بوده، طراحان این پنج‌بند فرماندهان سپاه از جمله جعفر عزیزی با مدیریت احمد وحیدی و تایید مجتبی خامنه‌ای بودند، طبق گزارش خبرنگار ارشد الجزیره، تمامی این پنج بند توسط آمریکا رد شده!  جزئیات پیشنهاد…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/64923" target="_blank">📅 13:40 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64921">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eHtvZIhJmeRn6-J5X8cKmRjMHoLbxezDdOwyLs5GqNK6PWc_Z6llluw2AlsQpfsxDRSVFrsBpdgcTAkSzle7kMs_nwroi7BEP0ER73uZY0hupWQsHZgU0AoB3SvcnXKpYIWvHIT2rAb0Eo4CRKJlZpY3vcXlzIlh2OGllWFDGQEwQH8vArkE4YjkhehSJ7bN588rViCeJQ7MU2p1QBqSzjDQq306YgJQ3_NIzryFr-HFjEgwdUtk2q0IUfxKqPrbXplUSO5AyjRtepI293K570RQUnp85Hj1TCIGUhI2gvZGWD1mUhNyBTagkFgKFEX136uOZZuA46syTBlUeKiEMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i1I-WcsOl9LbzXVCtcIvmQajXhi5ABb8GempqCIgHw6u1MCDQbxp6KjKQeg4LPWc2NWspPPWWrqVNvw2wiXyjyA3audgT1AhHT-EJNyFlq306Kldjfb9G9l_6NDSMo7synhDFKwVBKUumGIRX0pcjEahNH1SEgSlC-EwpW3WvSlA_tj0X-GQDJ4gFE5TE12y8m8X5XWcde5Qc35b1_5Y_Ux5XHJvj99OjpEEbFUz3pN9qJT87oCQXGLRRfmLoK0VvoKSbfVvmxX5odQ-H6BB9dmEhKXRqYoV8eYXd9t26QGxmooiTTv6eUJH6JuJlytCqqMOIRanR_YZy30vVo8imQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
#مهم؛ الجزیره: پنج بند ایرانی ها توسط ترامپ بطور کامل رد شده‌اند، مجتبی خامنه‌ای دستور داده بود در صورت رد این پنج بند، دیگر وارد مذاکرات نشوند  @News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/64921" target="_blank">📅 13:26 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64920">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s8JUbAvdhR0pbFibvWV-p1hbS5B0soB9GkuQsdFPxVUIKeU8iDF4tiB_93w2MW3ALFuzyyPiE7Uj6wgKq3v_KNWuDY9b7yZK9X48LslS7J12OnHwWxtvjU0PaFIlfoEjkkHMeKMKbqRqwUL-hxNkqiWi3PWW7UPAZwFzh63WfdF50J2JJB8yXnTPhO1bh7xyf4GdOBpJMToeXCmJZvQkF67aygZ9pwD6pPoUvhbp_7Ng0ZqThrhEoC1_MB9PeiJj2sAwsyOm8QzkXsvmoJ-ax8FvhLc8ubvRSi1xZWEAtGYfGxuwArOUhkNcY_acsmNQdAroUfAkfgSggI4bUI-9UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
#فوری؛ علی‌هاشم خبرنگار ارشد الجزیره: یک منبع آگاه ایرانی به من گفت که تهران رسماً پاسخ آمریکا به پیشنهاد ایران را دریافت کرده است و واشنگتن شرایط ایران را به طور کامل رد کرده است  تیم مذاکره‌کننده ایران پنج شرط را که باید قبل از ورود به مذاکرات در مورد…</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/64920" target="_blank">📅 13:22 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64919">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇺🇸
ترامپ:  امیدوارم ایران در حال تماشا باشد. ما دقیقاً می‌دانیم چه چیزی را به نمایش گذاشته‌اند. می‌دانید، آنها کمی استراحت داشتند، بنابراین سعی می‌کنند چند چیز را جمع کنند. آنها چند موشک را از زیر زمین برداشته‌اند. همه آن‌ها در یک روز از بین خواهد رفت. هر کاری…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/64919" target="_blank">📅 12:46 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64918">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🇮🇷
عراقچی: پیام‌های متناقض آمریکایی‌ها مهم‌ترین مشکل است، هیچ راه‌حل نظامی‌ای وجود ندارد و فکر می‌کنم ایالات متحده باید این واقعیت را درک کند. آن‌ها دست‌کم دو بار ما را آزموده‌اند و اکنون به این نتیجه رسیده‌اند که راه‌حل نظامی وجود ندارد!
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/64918" target="_blank">📅 12:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64917">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭 𝐕𝐏𝐍 ]</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ShirOKhorshid-2026.05.14@HotVpnPlus.apk</div>
  <div class="tg-doc-extra">23.9 MB</div>
</div>
<a href="https://t.me/news_hut/64917" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📱
👑
یکی از فیلترشکن هایی که گزارش اتصال خیلی بالایی از اون میاد، فیلترشکن غیررسمی سایفون بنام شیر و خورشید هست، دقت کنید این یک ورژن غیررسمی هست که تعداد زیادی از کاربران تونستند با این روش به اینترنت بین‌الملل درستی پیدا کنند! در آخر پست لینک دانلود این اپلیکیشن قرار می‌گیره</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/64917" target="_blank">📅 12:44 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64916">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭 𝐕𝐏𝐍 ]</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qGl4jUK2mYBRfYIYsWDuTUakNJgk3uE-Nm_UiOZV8l8TyDKbIDVNflJOpi-CkPHy1ZCDzGyVTaOEVw6bhM0Thq6lhf5EBZrs78v1KKeOv5j6mTJD7r69SktzFfUt-N-AzdowqCiMK69s91-ELBKMZF4hgC6IEfD3cyXG_OjZhR-GB7_uXJlJn6OuYjfLo2Rn8EESmqvlmscCXMBJYYlLOg-Hm8T5m05zNDmMWkancB41xHF1QXTqbhxAI7U_1zZO_CGQPpcmSMysa7-WDsnucOlnSigKHb1Hn1zAMKLKy_meA_PFvCKygNzXs4AgD6dK33LvXP3Jsr0RbNGf8GUbKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
👑
یکی از فیلترشکن هایی که گزارش اتصال خیلی بالایی از اون میاد، فیلترشکن غیررسمی سایفون بنام شیر و خورشید هست، دقت کنید این یک ورژن غیررسمی هست که تعداد زیادی از کاربران تونستند با این روش به اینترنت بین‌الملل درستی پیدا کنند! در آخر پست لینک دانلود این اپلیکیشن قرار می‌گیره
👑
‌ ‌ ‌ وارد فیلترشکن شیر و خورشید شوید
[دانلود فایل در پایین همین پست]
1️⃣
‌ ‌ ‌ بعد از اینکه نصبش کردین و وارد شدین، از نوار بالا برید تو قسمت OPTIONS
2️⃣
‌ ‌ ‌ تو مرحله دوم وارد قسمت آخر یعنی More Options بشین
3️⃣
‌ ‌ ‌ تو این مرحله برید پایین تا گزیه Connection Protocol رو پیدا کنید یبار بزنید روش تا با صفحه جدید روبرو شید
4️⃣
‌ ‌ ‌ تو منوی باز شده گزینه CDN Fronting رو بزنید و برگردین عقب، دقت کنید برا بعضیا تا همینجای کار رو انجام دادن و برگشتن به صفحه یک استارت رو زدن وصل شده و برا عده باید باید آی‌پی هم وارد کنه که در ادامه می‌گیم
5️⃣
‌ ‌ ‌ تو مرحله بعد باید یه قسمت برگردین عقب و وارد بخش CDN edge IPs بشید
6️⃣
‌ ‌ ‌ تو صفحه‌ی باز شده باید آی‌پی های زیر رو وارد کنید، دقت کنید آی‌پی ها مدام آپدیت می‌شن و آپدیت های جدید در داخل کانال قرار داده می‌شه، تو این بخش کافیه یه آی‌پی وارد کنید و OK رو بزنید، حالا برگردین به قسمت تصویر شماره
1️⃣
‌ ‌ ‌  و روی استارت کلیک کنید تا وصل شین، دقت کنید بعضی از آی‌پی‌ها hostname دارن که بدون هیچ مشکلی تو شکل شماره پنجم، host رو تو قسمت دوم (پایین فلش) وارد می‌کنید
🌟
آی‌پی هایی که فعلا موجود هستند
:
CDN SNI Hostname:
python.org
151.101.64.223
151.101.0.223
151.101.128.223
151.101.192.223
92.122.123.128
2.16.186.20
2.16.186.31
2.16.186.44
2.16.186.58
2.16.186.69
2.16.186.81
2.19.204.19
2.19.204.87
2.19.204.137
2.19.204.144
2.19.204.145
2.19.204.170
2.19.204.184
2.19.204.185
2.19.204.202
2.19.204.210
2.19.204.211
2.19.204.217
2.19.204.218
2.19.204.225
2.19.204.232
2.19.204.234
2.19.204.240
2.19.204.249
2.19.204.250
2.19.204.251
2.19.205.8
2.19.205.9
2.19.205.11
2.19.205.27
2.19.205.33
2.19.205.34
2.19.205.40
2.19.205.41
2.19.205.42
2.19.205.49
2.19.205.50
2.19.205.58
2.19.205.59
2.19.205.64
2.19.205.65
2.19.205.82
2.19.205.83
2.19.205.88
2.19.205.97
2.19.205.98
2.19.205.105
2.22.151.4
2.22.151.9
2.22.151.12
2.22.151.13
2.22.151.15
2.22.151.17
2.22.151.20
2.22.151.22
2.22.151.23
2.22.151.32
2.22.151.36
2.22.151.37
2.22.151.39
2.22.151.47
2.22.151.51
2.22.151.53
2.22.151.54
2.22.151.58
2.22.151.60
2.22.151.62
2.22.151.135
2.22.151.138
2.22.151.139
2.22.151.141
2.22.151.142
2.22.151.143
2.22.151.144
2.22.151.146
2.22.151.149
2.22.151.150
2.22.151.151
2.22.151.152
2.22.151.153
2.22.151.154
2.22.151.155
2.22.151.156
2.22.151.157
2.22.151.158
2.22.151.159
2.22.151.161
2.22.151.162
2.22.151.163
2.22.151.164
2.22.151.168
2.22.151.169
2.22.151.170
2.22.151.171
2.22.151.173
2.22.151.175
2.22.151.179
2.22.151.181
2.22.151.182
2.22.151.183
2.22.151.184
2.22.151.185
2.22.151.186
2.22.151.188
2.22.151.189
2.22.151.190
2.22.151.191
2.22.151.193
2.22.151.194
2.22.151.195
23.32.5.18
23.32.5.44
23.32.5.71
23.32.5.96
23.32.5.118
23.32.5.141
23.32.5.167
23.32.5.193
23.32.5.214
23.32.5.236
23.53.35.146
23.53.35.158
23.53.35.171
23.53.35.182
23.53.35.194
23.53.35.207
23.67.253.24
23.67.253.55
23.67.253.77
23.67.253.101
23.67.253.120
23.195.81.72
23.195.81.84
23.195.81.96
23.195.81.108
50.7.5.83
63.141.252.203
65.109.34.234
92.122.123.128
94.130.13.19
94.130.33.41
94.130.50.12
94.130.70.160
95.216.69.37
96.16.97.82
96.16.97.104
96.16.97.126
96.16.97.148
96.16.97.169
96.16.97.191
104.124.148.191
104.124.148.203
138.201.54.122
142.54.178.211
144.76.1.88
184.26.163.12
184.26.163.24
185.200.232.49
185.200.232.50
185.200.232.42
185.200.232.41
184.24.77.42
184.24.77.32
184.24.77.5
184.24.77.7
184.24.77.16
184.24.77.36
184.24.77.21
184.24.77.11
23.48.23.186
23.48.23.133
23.48.23.195
23.48.23.178
184.24.77.29
184.24.77.42
184.24.77.32
184.24.77.5
184.24.77.7
184.24.77.16
184.24.77.36
184.24.77.21
184.24.77.11
185.200.232.49
185.200.232.50
185.200.232.42
185.200.232.41
23.48.23.186
⚠️
‌ ‌‌ ‌ دقت کنید با یکبار لمس همه کپی می‌شن فقط اول ip هارو رو از حالت خلاصه به حالت گسترده تبدیل کنید تا همه قابل نمایش باشن، و داخل فیلترشکن باید تک‌تک بزنید
👑
‌ ‌ ‌
لینک دانلود جدیدترین فایل فیلترشکن شیر و خورشید
https://t.me/hotVPNplus/9
@HotVpnPlus
|
@HutNewsPlus</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/news_hut/64916" target="_blank">📅 12:44 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64915">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61dd932f8a.mp4?token=hX9eXycSNsKQ1TKTknSXqnQDClU5-MAigrOcbtNCwrfA5ZVbJvWEo7Cgd4JBmCzwVeUjA1wBexM9scDy8-Svi-eMyTN9HqcGsTRb1vrrEnkpBGOFag9X1PqBS41XVWkEQpg50L1e5n_U1Nn7ittWAlhWLFZnJy3_g8VzFe8m4fwPljibduZxX46UAnEfprXlNB2QBvc0LrkmBVwjjcyhQ99HYfZD54KYAcj43FGz5WhARRDoUcjoTcGoSk1NNhxyHGLF9aSZlNSlruM_fgtLXg4zAM6jpOMmZdvxnO8U1bCZSdpo08ijI7kmfH2UgWXghqyUXItJR2RvPOERnwznpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61dd932f8a.mp4?token=hX9eXycSNsKQ1TKTknSXqnQDClU5-MAigrOcbtNCwrfA5ZVbJvWEo7Cgd4JBmCzwVeUjA1wBexM9scDy8-Svi-eMyTN9HqcGsTRb1vrrEnkpBGOFag9X1PqBS41XVWkEQpg50L1e5n_U1Nn7ittWAlhWLFZnJy3_g8VzFe8m4fwPljibduZxX46UAnEfprXlNB2QBvc0LrkmBVwjjcyhQ99HYfZD54KYAcj43FGz5WhARRDoUcjoTcGoSk1NNhxyHGLF9aSZlNSlruM_fgtLXg4zAM6jpOMmZdvxnO8U1bCZSdpo08ijI7kmfH2UgWXghqyUXItJR2RvPOERnwznpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
امیدوارم ایران در حال تماشا باشد. ما دقیقاً می‌دانیم چه چیزی را به نمایش گذاشته‌اند.
می‌دانید، آنها کمی استراحت داشتند، بنابراین سعی می‌کنند چند چیز را جمع کنند. آنها چند موشک را از زیر زمین برداشته‌اند. همه آن‌ها در یک روز از بین خواهد رفت.
هر کاری که در چهار هفته گذشته انجام داده‌اند، در یک روز از بین خواهد رفت.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/64915" target="_blank">📅 10:26 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64914">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
📰
کان نیوز:اسرائیل معتقد است که ترامپ پس از بازگشت از سفر چین برای از سرگیری عملیات نظامی علیه ایران تصمیم خواهد گرفت.  مقامات ارشد ارتش اسرائیل و فرماندهی مرکزی آمریکا (CENTCOM) در هفته گذشته درباره احتمال از سرگیری عملیات علیه ایران گفتگو کرده‌اند. بحث‌ها…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/64914" target="_blank">📅 10:23 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64913">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/kH66bJS5lwyFm1JzkVtxhWw1VPLsqZeT9YXy8lPXCAnROzPZ77L6mD72gH20uGFRFMaZsG8r5L0IuSZjwAO6Mgszo-7J_A4SxKnbp58a4tX-EWqSRWbTdz2xkI1UJI8SehlgVvKj077ppRF82y8_PrqoV6BREfpoguIJw1mM4PBXm2Z3VCuhIodtLV0lb39a6kPj0WkCBWGX03DYCuIDsWQGtXDBSS5LgYqWg6TuNd9Ari4GuJN14GEsgyPsTXw9J6gBz50Cfw-tO5_i6IUf1slY4qTSZLjFV5j9sjlx7ABhtQvqK9Ov_6djEYLlQr2xR1S7f-KHHpyAo4UlOvB84w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تخفیف فوق‌العاده - ظرفیت محدود
سرویس اقتصادی با کیفیت موجود شد
💥
10 گیگ فقط =>> 1,700,000 ت
20 گیگ  فقط =>> 3,100,000 ت
40 گیگ فقط =>> 5,600,000 ت
سرور ها  v2ray هستن کاملا با کیفیت بدون قعطی
خرید
@amoadmins_bot
@amoadmins_bot</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/news_hut/64913" target="_blank">📅 03:09 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64912">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JPtSaSNAZsKCQ-fwvF2GVoFAxRZKyOpyo2rxg58-0aWmi03kD5YAQacxq-gp8N8gRuTOWSi3Wb7JSUPEdQvnOpzr4Mp72LGQmwK2tePNFBZpwdjLZBVx0HfUp_EknODMI00ba3FkRrKdGREraxBGQylIxeh2C_vqVW2MqmUg0yAOc2MVzh7ERcQfC6CGbS58mjqjv-moKo1mqUyQulyai9bbBW5ybq5C3mp2JnlBPtQYhrkN1DAwO-JLKCwGpdZcj3fK2qpdIsFTKtXGiYRwggZ3XLESAK1AJypbYs8WmQHgl0GtyTBoeSwJcLvHO4lp8ebOKDI-3XGm3ZjL5geiXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسایی؛ نماینده‌ی مجلس:
دولت قصد داره میزان سهمیه ماهانه بنزین ۱۵۰۰ تومنی و ۳۰۰۰ تومنی رو کاهش بده و قیمت بنزین ۵۰۰۰ تومنی رو هم به ۲۰۰۰۰ تومن برسونه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/64912" target="_blank">📅 19:59 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64911">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09aa0f1cc3.mp4?token=TsMmEMOQSG4ZKvitgU90OIH1sB5cni8_6TAhfJTwBgbnvogMbIVRaY-FnBU0CJKC7Yp0cCtV--ere_ZsC5xPsV3K_AzM9yItj5DVsez1RbO0w5DIzJRQ81nD-LRznpbop1C0J5u5H7bE0pC8L1wny5LsoWIsXyNxFeTtQIWd1h73dWVJjrS-ZPLbSNwPitTdSWFEVUXM5xBXAbnICv2zaWV9ul-UetEobc9pcp2PCB4bepGdEJb_s7QHbR_pYCEuTf5AE9Xnw4HwP0HcfiSyZBgfeW-NKbRqZCIv8mlwBh5_zrMQBIOyJ7AMP7nZZY7fkkGM8sdQJAoo-yvT3j43rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09aa0f1cc3.mp4?token=TsMmEMOQSG4ZKvitgU90OIH1sB5cni8_6TAhfJTwBgbnvogMbIVRaY-FnBU0CJKC7Yp0cCtV--ere_ZsC5xPsV3K_AzM9yItj5DVsez1RbO0w5DIzJRQ81nD-LRznpbop1C0J5u5H7bE0pC8L1wny5LsoWIsXyNxFeTtQIWd1h73dWVJjrS-ZPLbSNwPitTdSWFEVUXM5xBXAbnICv2zaWV9ul-UetEobc9pcp2PCB4bepGdEJb_s7QHbR_pYCEuTf5AE9Xnw4HwP0HcfiSyZBgfeW-NKbRqZCIv8mlwBh5_zrMQBIOyJ7AMP7nZZY7fkkGM8sdQJAoo-yvT3j43rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ی دست دادن ترامپ و شی
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/64911" target="_blank">📅 13:36 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64910">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KRJMGDehRexrA36F9l2xxkQlN2BQirDs5krMjC-kOYr2cZTmKoyjcGoWWl0s4TyT3_nR3NlTj_GCssS9Ty9mDWxT_LvswdxP4-RowAmbppWbfORzq_r1ZCJk247IILUFa919f2lTeOe5ub_UJrXGKTSG2qM3VukgEx06C2pyVNpjCYLjksDsv7FqddCb5kZPaH04pZysF2Ii3AuYE-FU4UKu-KhDS7YJc7kLsl2D1BIO5LBlrteQ6iiJ_WcMquFySdypyBoqKzisvvytQOdvRWEZNdhclwMicAceS-TDJiPI0Xxp5bnMFeCr70Ye11DgKCNZ0I3C7H4BwSBhekKUwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خسته‌ایم و کم‌رمق
😂
#hjAly</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/64910" target="_blank">📅 02:36 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64909">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">خسته‌ایم و کم‌رمق
😂
#hjAly</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/64909" target="_blank">📅 02:33 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64908">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🇺🇸
#مهم
؛ برای اولین بار،  اینجا در کنگره امریکا، سه نفر از جمهوری خواهان از صف حامیان جنگ ایران خارج شدند و به قطع نامه پایان جنگ با ایران رای موافق دادند.
با اینحال این قطع نامه رای نیاورد و تنها با اختلاف “یک رای” رد شد.
در‌صورت تصویب این قطع نامه ترامپ به عنوان فرمانده کل قوا حق قانونی حملات مجدد به ایران را نخواهد داشت.
اگرچه در نهایت ترامپ حق وتوی این قطع نامه را خواهد داشت
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/64908" target="_blank">📅 23:04 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64904">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o_QCpkYZukrW_qsoVFVf6J7qq4dTtcx8ggNJ0t6BeYuo5IOijlqVyKADbjA4_PFYsGoQpFgh6Ra9u-zzL5MYbyEc3pMjAIWpgO4G2UNqI2XbNOkPWKPJN00-lcGi6RLjvmNrILbD4GuexOSYF2LewxVF5M8Can95vwYhbyvF69S7FaZFnuNk_KeydNE8F--bB60Dv2VzuzBeEMmNkR6UdsafWlRvg4dIVBZ4sugSus0mWxWow2db9b-nojb_-fi9DQ2nEdGG7KHDBdR_T6Fv2uwFQSfs0qNUlOuhiEBcrj9avWN7yJ0hrTAhn8G7_hhyeAoyoKe2Ff5sXPPWHQ8QrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DCtxLV8eD4xMJeA-CMEtQCd9jaFP9uX9hgaYViet5MRe59PSdNP_QDS7xoZH5L_yGK-pak9iCM6jg_z3nS3kydGgO-HaK_xKnpq4lPFgW4Fx1QWaqrX7kHYMSAidbq2GKRTLhIaw7E-7H9CbgBuhksR57N0KOmEb2xF7XnOyAKQXiGkwJr5ytsKQtPDK3d4ziyxNvruTC_vzWvwLh5jTPtlaNEFuFoZxKM1G4o9M3NMjaptpsEb1PxJD8DTm8MeSSFP7TaooWi10SFNf5QqxQ-wN3KAe1wl6LA1918U-IVDQEodG50T83hMmhtWVIWL-mhN-BV7Ah3f7CLj5hWQxkg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8253c8a3d.mp4?token=MMC2uqIUMgD6LgG2NbyLxQ6QWtEA-p6PQGHHu7G7kQtBs46nmWsvqtbzrkEVPCOoEPwM6z2VnLZQS-AXgpjKcVWYbnzb4CRrUxHyRKLqRKtVq1IgbBaZX3laPhn0vepJDfDD88cxpwb_6bSYZkH6yq7aJ3NOCa02ppTm-gpqTfp9_Dn6waLUjn2Ymy7ZFhV8ULnF666BKqNk7jiN6zNx3PIRCV8HUIZmy-TdVUHfgbYpRERdpj6mNcTYpyuVNpPQjSR3yjkLtNAnduevE5rrCnVzDMyd3TvoecyXknhWR74cirwxk9JU4_fU_bdRVJBgQn98lD_fycr3KUUVwsXWYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8253c8a3d.mp4?token=MMC2uqIUMgD6LgG2NbyLxQ6QWtEA-p6PQGHHu7G7kQtBs46nmWsvqtbzrkEVPCOoEPwM6z2VnLZQS-AXgpjKcVWYbnzb4CRrUxHyRKLqRKtVq1IgbBaZX3laPhn0vepJDfDD88cxpwb_6bSYZkH6yq7aJ3NOCa02ppTm-gpqTfp9_Dn6waLUjn2Ymy7ZFhV8ULnF666BKqNk7jiN6zNx3PIRCV8HUIZmy-TdVUHfgbYpRERdpj6mNcTYpyuVNpPQjSR3yjkLtNAnduevE5rrCnVzDMyd3TvoecyXknhWR74cirwxk9JU4_fU_bdRVJBgQn98lD_fycr3KUUVwsXWYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت مردم تو خیابو‌نا و پارک‌های اطراف پردیس بعد از زلزله و پس‌لرزه‌های دیشب تهران
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/64904" target="_blank">📅 10:14 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64902">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gCT2--HEK549_VwKc3JSGtj6a6ykdBo5Bl_7npIGO7W8WB3NMHpMb7dvLelcn_8XEuk3EoAfOJvjfl6ulfhMnKzGjXkBVQV62jVsZUq-a2qwi4pRX4fvvMzeToTuQsIP-CdNTzCfxuT0p8J9C-W8CihskwyJE4s8AX-zRihu0kxx8yxt_LZ3nOHUpC0pF4S9-45RU8ILqrwZmVOkiB00wU9LmKBMHA4GwvUpIN3PNYjak_3cGMQ5yGE6oInwj2DspIc_0qlgHquAXybq06A8yov9WFZCrg3dRDE6cJjsFxa9iB4i__3hrZS-disFt9Q0D-EwnwOM_FJNfAbvQcbU3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nKnzb9D-qF3yapSyetCLpwv1g8z8EkTZehDiJtXp8upyNpMkWeH6EwsWRohJd8SiG2f4zX6HO-Cp_88l6u66915KD5OsATglG9LIT6QxNQOw2bNQDn35Zhs4TnZEAXQ0CpXFFn0p14qguQol-pbEDUO_bUQOGBmEXvLGvQB8UGvYVhfyRz85FnP7cQWRU_370LUNZq4EKmEkhURJIYttFkTm0D4aDBdmyxsmvTaGMLrGAz5hGZUBhIhKGBQUdO6DUPwszXWpr-2nLp2kigD-VKQJMUtolc-_rE3LKFbbDKGW-mZ4B_-VL1PW4h_jPo3URtdvgGX1nvdE3cAktZ-n7Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">با اعلام خبرگزاری قوه اعدامیه با اذان صبح امروز حکم اعدام «احسان افراشته» به اتهام جاسوسی اجرا شد!!
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/64902" target="_blank">📅 09:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64901">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
📰
خبرگزاری NBCNEWS: پنتاگون در حال بررسی تغییر نام جنگ ایران به «sledgehammer» به معنی«چکش سنگین» در صورت شکست آتش‌بس است.  یک مقام کاخ سفید به شبکه خبری ان‌بی‌سی گفت هرگونه عملیات نظامی جدید علیه ایران تحت نام و عملیات جدیدی رخ خواهد داد. بحث‌ها در مورد جایگزینی…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/64901" target="_blank">📅 09:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64899">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uYq9BVNFhw7XIusI0AhoKsZ9hsl-6gXtOjYkA91mNfxCyJeJK2wVQ83ZhMPcoz-psgKLBAuafrgDt9G7AqEVoPcwKkyMNRt3eTO8tv4XqpghTf8bXVogA1bvlJaBGSQGQXHcha-spPqjJQWCcKFlN_NjHvp41WH_FERvgrmIPm12TW8apwjEbDUnK5ScqR4rWLvFoRSW6CvHDu7ze9vw-4M0sZd2vnvXnoOaBw84T1oEBrm6eaDhB4B1nFmDkduqzGzPy4B8k40XfAToznm9quogwxf76Uvkb8vG_MzMvgl2252KScOo_mexgvF3uSmQnwYtwnL2x_7ooj5zqoIkzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/succPn7xd5r7zhJBV26GaMRTf7IEcV0AAEHtvmrUjaoAssWHzj5Z986dLjhxiujnUUrJNULbu8CBxm_aWv10K6lDr7ySHorUOSa-sOjuHP-uLKphSTLUZBAwTQBjkvmUB2ZXwQTrE_uNrBCcpZ4r7RzUMj5dHCFPA6EtNyhGpmz_X4jiX6L5uHauR-upL7qCi9eQiXocSmFJl33z9CsXw1llzq_-SVYf8TyyQCqJL2EwOzyylEGst58dWbgbeW7ALsWyVuZIGC9no7vbEKnelyhwi3N0WbyDxsP_5jt5JjGd3Uz2wEZepJwVHUKfYmsGj0I8-UFzGAgh9ym6Wn94ZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مارکوروبیو داخل «ایر فورس وان» دقیقا لباسی رو پوشیده که مادورو پوشیده بود
هنوز نرسیده ترول رو شروع کردن :)
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/64899" target="_blank">📅 04:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64898">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VMObmyY9jw5nocqna1rufGB9lmPUG8FmUoFRQhktUII32shKFD76uCpMqaSIxUQFF4bTv4o1vQlphO0taz-FjHOW2Upda2F6Tf9YFSU2pO66yLmthNkwUaSbjJFz1gGLEL6aIY6i6V6HT3I94r98sEH-vtXq-tJNUFONePTXimdLgmZdIzYlOszJQIPQcJlbbP6gnq7CvSMzMAuetKqs5TgWYlqzTCXlGG7OF76wdTsq-2IwnV-wC1TXf4NZf-dpKksyY5TSGCB9v-6CDSm5VOWW2RNjK_9w3I7Wq4Ol8p0mOppdYcntIYLULRlCdKv_n-THM8BkOfSBkAf9UDJblw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باز تهران یه چص‌زلزله اومد، منتظر باشید طهلیلگرا ربطش بدن به آزمایش هسته‌ای
🤯
#hjAly</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/64898" target="_blank">📅 03:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64897">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">باز تهران یه چص‌زلزله اومد، منتظر باشید طهلیلگرا ربطش بدن به آزمایش هسته‌ای
🤯
#hjAly</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/64897" target="_blank">📅 00:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64896">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g5RetagSkL3K_hI1OhogNf3gaJ8gxyqgJk5TZbn3KA-a9w4RaJjqTA9LVLkGnFff0E0_LNdNFIQq_cQpNFOjz4ni-9tvAdGIqkd5f6YEbNUc2mkMVNxMnDLq9oDHW2NccAXYLlW3rGi_nl-yvTnHCSwtg0zOmZ03n43rha-PamwhwZEXWTkbmPkPiYHUwr-mHssvntnELuj4KDgvvQ1g7-S1Qv876zWLSjIqE6GdADnODtZrov5Mc-v9kh5IBDqhxRn66jLwBQ0WkFAsJ-MBDAwX6RiJ9mcWs74TGI2gg8AJDrdMQqbONY05R-vESvlbvrXrCxiC3gbXJTKTrJkFXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ قراره یه اکیپ کلفت از رئیس شرکت‌های بزرگ امریکایی رو با خودش به چین ببره  رئیس شرکت بلک راک رئیس شرکت گلدمن رئیس شرکت مسترکارت رئیس شرکت سیسکو رئیس شرکت متا رئیس شرکت ویزا رئیس شرکت اپل رئیس شرکت تسلا (ایلان ماسک)  @News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/64896" target="_blank">📅 20:28 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64895">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83afc3e388.mp4?token=uxrgWmNeO_gv1No8jrfa2jnYl_KvBw4yEuSunvBHgC3aqzcCuseVLjNO0La2VJPrvFv7j1mzKQ6FK1BLDHYwif5oJnZDPdiZ0LCn4EuSI7pt7sX5dX-ZujflJUNH-gquXO0QVGhVc2jKI2LewsMW0k9qbflfdv-anSsBsLTETnjReYA4Yv5N-RK7JtrzdeiDzUkosA9IEqO6lKc1ZS-3Wf2KcDXBVvNGX8GF05z33nSrRsoC3sEoz1LXYlALWszH5fUxCE12XtbV6iUu1Ptdi_xs2tez5FthICmSnBLrDke_D3JHQclhWLtWKhfksVUhYUhgx--RVKZLf3sEyKOO2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83afc3e388.mp4?token=uxrgWmNeO_gv1No8jrfa2jnYl_KvBw4yEuSunvBHgC3aqzcCuseVLjNO0La2VJPrvFv7j1mzKQ6FK1BLDHYwif5oJnZDPdiZ0LCn4EuSI7pt7sX5dX-ZujflJUNH-gquXO0QVGhVc2jKI2LewsMW0k9qbflfdv-anSsBsLTETnjReYA4Yv5N-RK7JtrzdeiDzUkosA9IEqO6lKc1ZS-3Wf2KcDXBVvNGX8GF05z33nSrRsoC3sEoz1LXYlALWszH5fUxCE12XtbV6iUu1Ptdi_xs2tez5FthICmSnBLrDke_D3JHQclhWLtWKhfksVUhYUhgx--RVKZLf3sEyKOO2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
پیت هگست درباره ایران:
ما در صورت لزوم  برنامه ای برای تشدید درگیری داریم. ما برنامه ای داریم که در صورت لزوم به عقب برگردیم.
مطمئناً در این شرایط، با توجه به سنگینی مأموریتی که پرزیدنت ترامپ برای اطمینان از اینکه ایران هرگز بمب هسته‌ای نخواهد داشت، گام بعدی رو فاش نمی‌کنیم.
ما داریم یه ارتش رو دوباره می‌سازیم که مردم آمریکا بهش افتخار کنن
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/64895" target="_blank">📅 19:13 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64893">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nxSl6o3gAphUm5UU57iATc1lrXHxysPt3Szry722fT8BMdWTpHl5nH1GoBRlM47EPX1smsIism75AnPB3xXFq4vrQsstTuBellZu5hnyMds8Z8-mQLgAUKS0ltNSAA3Fo89nxSb9u6VYsyF1s45ZvzJJrwHRx8KmViq7wH6sF-JNd7lxptmiVjGNSXUj48QcnOjX7CM6Ti-XkY5KAFZPqOwQiOyATmmlk26mYmnQqXAiFlkSGSL2nSfsUKS5RoJSghdYbHjS4cP3zyMaq2FYXusHHm0KSmycua2fgQzqmpcxCQsvvx6eQGVNDrITUa3nts-nYW7BnyY5tV6hTEWSng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qb1pdyybwTXml2DQtAa96NgzoOOE_U4xVAWpHynAXPu87U0Jrs3nfkZNLLqLfOPfHU89ufjw5wZH6EFahAXmIuy90TofjZ7GFCM8SwIxq-JiIhIC_Spy14WLUaq0ye26YTALr4MiXT1sZjcyE74H8oY0ACUGRjm4g6fWdkv9IUs-B9LHYCCz8gkKGVTWIQdqFzIlL9wv88ghQvLINVDu4qbomu9q2G1hZiIwOeCYYxkyO1P6CFJsC418vG5MBuAVXMmVVAT74FZ4inrsiml_f6ZfIHTGb896RsmB7Re7oC0vwhsZjFivJtbFoR4Ai_jqHSoggaJazyxysOxOlO9W7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من هیچ جانوری رو ندیده بودم که آرزوی مرگ یک نوزاد رو بکنه...  جمهوری اسلامی حکومت بی‌ناموسا و حرومزاده‌هاست، اگه حتی جایی یک درصد با اینا همنظر بودی، به انسان بودنت شک کن #hjAly</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/64893" target="_blank">📅 17:50 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64892">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/awc8EUYc-yqlmChsN07mCPQ5inLL58p8M4imPInvNMJl1T81_6vReruDpHg8KcrSt0RraivrGAaAC7HX4U6LSj7BrLhvi-bdoLde79hxaeOjFmrg4XSetvNk4-OIdP3amJEpXhM1VhBE29--iSLWKBGyR8iTnt9LnivIT2lT2st1CL8oAzJfOMxV2bGjnTXg7riQC323cjg_MMyg5EUBHLzEwVqw8XJ67kjEdILXJFuIwPZ7NZYFQnngGLX84Aes3XLm5Y1XFbAt9bV8jABiUEILD_5NHZDeu29fkNBIMKZQBLt1j5P637elMzFYnnMnKkYbnOPzYjFOcvn2UbHLgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من هیچ جانوری رو ندیده بودم که آرزوی مرگ یک نوزاد رو بکنه...
جمهوری اسلامی حکومت بی‌ناموسا و حرومزاده‌هاست، اگه حتی جایی یک درصد با اینا همنظر بودی، به انسان بودنت شک کن
#hjAly</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/64892" target="_blank">📅 14:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64891">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbb21e178c.mp4?token=fkdwR_3ERFthxooFVd9lUL9AeDiEHMlFrRKNx5tU4WjPD24uvE4mQW2AVNcjj3bFGg68iJIz90oQ2508XqHhxrfAddd0zGvx8Hb7a___FXKjxWem18Fwv7qrXKtDo-SkTM_fZLeDrKIVzUwSjfF4RI7gdbHPTf3OPCT1IVDkVuwMEhYIj-39MUwdlxFmswjpJYbB7YBbjy5dyLbn2cmNC-yJOHr6HvOs9SieHnS9tWSXtroWJNBNdYPV79Wl6CrUZyBLowFFFUFSS5-lfwms_z-YZw5OoicxbPdAih_yAMPeygPv3-lLEsxkuXfHNLRpY_eFqaYsRYlQ99G1Dfpsdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbb21e178c.mp4?token=fkdwR_3ERFthxooFVd9lUL9AeDiEHMlFrRKNx5tU4WjPD24uvE4mQW2AVNcjj3bFGg68iJIz90oQ2508XqHhxrfAddd0zGvx8Hb7a___FXKjxWem18Fwv7qrXKtDo-SkTM_fZLeDrKIVzUwSjfF4RI7gdbHPTf3OPCT1IVDkVuwMEhYIj-39MUwdlxFmswjpJYbB7YBbjy5dyLbn2cmNC-yJOHr6HvOs9SieHnS9tWSXtroWJNBNdYPV79Wl6CrUZyBLowFFFUFSS5-lfwms_z-YZw5OoicxbPdAih_yAMPeygPv3-lLEsxkuXfHNLRpY_eFqaYsRYlQ99G1Dfpsdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
ملانیا بهم  گفته باید رفتارت رو درست کنی تو دیگه رئیس جمهوری پس از کلمات رکیک و فوش استفاده نکن. من هم همین کار رو می‌کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/64891" target="_blank">📅 09:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64890">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba55a8b78a.mp4?token=LDSYfFRgfo8d0Lasi8Qpon84YR33o4IosKLMuViLtBwVCpNrgNIUpxV53qaS2zrwWCsg9tSoU9SlMnzagMDTxtRySA8A9gQvxlNlXvzrw_ZzNxQP6vtD_oIy1zGM8chwymfkMJf0LbCOfIG8zhmY5hZhiaft3I6FlSer-fYvCKVEr8_IBR71wsFg7htZt8mm87fzKBAEBh3XSMEUwzps5CLTe4g4WqcTmFdNNVskBwPrcBD96nmqG5ZaqXarzEhbDGEDY7fEKn6lohqpg_WiSQa7bfK-Te1taAn_LAcqetl8w0JhwNohiocOysxCrNmiz9nq2ANtq5Ha5dW4Aoq8PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba55a8b78a.mp4?token=LDSYfFRgfo8d0Lasi8Qpon84YR33o4IosKLMuViLtBwVCpNrgNIUpxV53qaS2zrwWCsg9tSoU9SlMnzagMDTxtRySA8A9gQvxlNlXvzrw_ZzNxQP6vtD_oIy1zGM8chwymfkMJf0LbCOfIG8zhmY5hZhiaft3I6FlSer-fYvCKVEr8_IBR71wsFg7htZt8mm87fzKBAEBh3XSMEUwzps5CLTe4g4WqcTmFdNNVskBwPrcBD96nmqG5ZaqXarzEhbDGEDY7fEKn6lohqpg_WiSQa7bfK-Te1taAn_LAcqetl8w0JhwNohiocOysxCrNmiz9nq2ANtq5Ha5dW4Aoq8PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ درباره نماینده حزب جمهوری خواهان تو انتخابات ریاست جمهوری آینده امریکا:
کیا جی‌دی ونس رو دوست دارن؟ کیا مارکو روبیو رو؟
به نظر ترکیب خوبی میان، من معتقدم که این یه تیم رویاییه. فکر می‌کنم کاندیدای ریاست جمهوری و کاندیدای معاونت ریاست جمهوری آینده باشند
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/64890" target="_blank">📅 09:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64889">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
📰
خبرگزاری والا اسرائیل: هفته پیش ایالات متحده نزدیک بود حملات به ایران را از سر بگیرد؛  اما پس از آنکه مشاوران نزدیک ترامپ به او توصیه کردند که قبل از تشدید نظامی، یک تلاش نهایی برای مذاکرات را مجاز کند، تصمیم به تعویق افتاد. ﻿ @HutNewsPlus</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/64889" target="_blank">📅 09:21 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64888">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u26beEvXSg9gHnuqPTuMcxEVRe5fa9dOeshSuDG5J6f3H6H2vtWGxHsTDuNgppLcy30wyUkXIWIayMCIrNHKZWdLBleLhGRFGNQlxVdXvmzHvflHieIf9EAKQWIH6THctoyA_flU6JF0I6P4Cf5FkP7AnsE-c-W2PxHYJAkIEQRy895RshHnlLKCQblfEBda6lw8c88nmqu-uzZQiUR0KUV-EM3c7MUHT_f-WQDWZ9fF8OgKBDXPulX8Oa2N0kjB64xXXxgyxuB-B5h3dKNi7RSwQJGJRgnlKYiCSpUtebiiH_60FUTJkiFqF6Pkih1O96HLpCTeUQSW3lKXzA7ihQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: من بسیار مشتاق سفرم به چین هستم، کشوری شگفت‌انگیز، با رهبری، رئیس‌جمهور شی، که مورد احترام همه است. اتفاقات بزرگی برای هر دو کشور خواهد افتاد!
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/64888" target="_blank">📅 03:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64886">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇨🇳
🇺🇸
سخنگوی وزارت خارجه چین: ترامپ از چارشنبه ۱۳می تا جمعه ۱۵می (۲۳ تا ۲۵ اردیبهشت) میاد چین.  @News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/64886" target="_blank">📅 22:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64885">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/WHtamBhHJb-PEEv-xUBLM0nrxPoh72a_M7BkybybVAlMzPSG0xOKNBGVXX7LLUojRlvsL3E2npgYMgbqKGzRXWEFNAKRrnMpzssNLJparZ0EWPR4BccTGCNtcxn1hkXn4UVJ-zQJ3NKQAlcPwq7jTXGAJbfgYg48J0SzEImusVyu13N8__KLHlalYNPrGtqeyhX4-TlxFcEIuAbpFb63tl1OK4-eF8Nbu3T2JP8QEdJ42B97Rlz61ykGKvXCdthNZZvlsPqsJEYD4cryoKyjkJZblPzGAfcqdaPWmzVIJM_vYkt6YckCD4vaSCHJeRn0ky4KnQbYMZ-FlH_p-OsRrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تخفیف فوق‌العاده - ظرفیت محدود
سرویس اقتصادی با کیفیت موجود شد
💥
10 گیگ فقط =>> 1,700,000 ت
20 گیگ  فقط =>> 3,100,000 ت
40 گیگ فقط =>> 5,600,000 ت
سرور ها  v2ray هستن کاملا با کیفیت بدون قعطی
خرید
@amoadmins_bot
@amoadmins_bot</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/news_hut/64885" target="_blank">📅 22:21 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64884">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
📰
آکسیوس: ترامپ به انجام عملیات نظامی فکر میکند اما ازسرگیری حملات آمریکا به ایران پیش از سفر ترامپ به چین بعید به‌نظر می‌رسد
+باراک جان
اینو که ما خیلی‌وقت پیش گفتیم
😎
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/64884" target="_blank">📅 20:56 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64883">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری؛ ترامپ: آتش‌بس داره می‌میره، بهش اکسیژن وصل کردیم تا زنده بمونه، یک درصد ممکنه زنده بمونه!!!!  @News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/64883" target="_blank">📅 19:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64882">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری
؛ ترامپ: آتش‌بس داره می‌میره، بهش اکسیژن وصل کردیم تا زنده بمونه، یک درصد ممکنه زنده بمونه!!!!
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/64882" target="_blank">📅 19:16 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64881">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇺🇸
ترامپ: کُرد ها سلاح‌ها رو برداشتند، مردم ایران بی‌سلاح هستند
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/64881" target="_blank">📅 19:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64880">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇺🇸
ترامپ: ایرانیا گفتن بیاین اورانیوم رو بیرون بیارید چون ما نمی‌تونیم، فقط شما و چین می‌تونید!
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/64880" target="_blank">📅 19:11 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64879">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">تا مرز رسیدن به تفکر اوباما</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/64879" target="_blank">📅 19:10 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64878">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">حالا ترامپ با یک نیروی معجزه‌آسای تاریخی بنام #محاصره‌_دریایی به دنبال حداکثرِحداکثرِحداکثرهاست!</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/64878" target="_blank">📅 19:09 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64877">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇺🇸
ترامپ: آخرش رهبرای تندرو ایران رو تسلیم می‌کنیم  @News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/64877" target="_blank">📅 18:49 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64876">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇺🇸
ترامپ: ایرانیا بهمون گفتن بیاین اورانیوم های مدفون شده رو خودتون بردارین، چون ما فناوریش استخراجش رو نداریم  @News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/64876" target="_blank">📅 18:48 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64875">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇺🇸
ترامپ: ایرانیا بهمون گفتن بیاین اورانیوم های مدفون شده رو خودتون بردارین، چون ما فناوریش استخراجش رو نداریم
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/64875" target="_blank">📅 18:47 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64874">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sYX8vrMZ9TDag_U6FVBrRJbaJIxhRqNhD28cNMT8kqurfxSfPqsVYZy7x_lmEXUy27kbBIHipI6VeQjGJFYtjB3xjHxTEEvVVvNXFOgJidrgVs6npFJQuNnxl7Ac62nF2Zu5uNk5VRDOQSblDBezjCRRRrVG1xDRY62t2ig6uY1nFhJbafSklrikVCOFXVcLFzQ7pAVfQDVvI5D-vakp6o-rZYcRjGxJ1RQO3RA6HdVv66vuJb5ZK8HFEPaBrI3qjP2Ge1RBoVuuOl3oWryV85eJR1Mv-nZJTcGTzDAg-0lTvt7NHhaj1IPErycBfpSn_gy4UEBAmwnjlTrBKF7s_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی بعد از اذان صبح امروز، عرفان شکورزاده، نخبه‌ی هوافضای کشور را اعدام کرد
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/64874" target="_blank">📅 11:03 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64873">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s69FEftLdmolyR3E9YXBPwchndU0C6Sn4bAPEWm8Ca-9YryEdxLFSOLyKZeZt99e72t_pZBzqOUwrDgkfO8fJShBBFw6H0fPgVMfjS1mr0GZzduHpiUl4xDOvaDKgfkzOzATcJsitCEnt2hAAEedBE5L02S7YBSixy7j6zz0OWtsxcR1EMbUKWMZoAdNV9v7KZ3hAXJA2-XlzthVdS9s29ydx4-wtGLMVRQ0MMIMlYOpZ8TGmuAFBpqChm6JpFgfZ8aQjXmnO8rlSqFIjNjoJiFyp_a1WUAM33gSkoT4TNUUAvdgC19aEK82rGGPz51m6c9jGiBUpXKmxpyzi3afcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
لیندسی گراهام:
من از تلاش‌های جدی دونالد ترامپ برای پیدا کردن یک راه‌حل دیپلماتیک جهت تغییر رفتار رژیم ایران قدردانی می‌کنم.
ولی با توجه به حمله‌های مداوم آنها به کشتی‌رانی بین‌المللی، حمله‌های ادامه‌دار به متحدان آمریکا در خاورمیانه و حالا هم این پاسخ کاملا غیرقابل‌قبول به پیشنهاد دیپلماتیک آمریکا، به‌نظر من وقتشه مسیر عوض بشه.
در این زمان “پروژه ازادی پلاس” خیلی ایده خوبی به‌نظر میاد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/64873" target="_blank">📅 09:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64872">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
📰
المیادین: منابع المیادین جزئیات پاسخ ایران به پیشنهاد آمریکا را فاش کردند:  لغو تحریم‌های آمریکا علیه ایران آزادسازی دارایی‌های مسدود شده ایران آزادی صادرات نفت و لغومحدودیت‌ هایOFAC مدیریت تنگه هرمز توسط ایران  گنجاندن بندی مربوط به آتش‌بس در لبنان با تاکید…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/64872" target="_blank">📅 09:12 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64871">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iS72WBjzxNHVttKZmVISzOmONTfBKSnS0ZlGhWaHN9zSO4wbWNfihv07JmA8gt2ufPKHIUc77cPFXJw656pJXlpP_pS2_XRDQKexw1LuBkqGIl0ckQcF12bnjHzXC9f2tIdtuTBC4fUucdZxsP-NJvY4r2JHdTO2Y8PZRh6ACpDT9emR2T1IzqG28JLHW9SXPdMm8Cak3JnfsZeA0RRSyaWTxBe_Cxm-2rs6AG1z8H84dagfN0HReuiyMmQh7qcuo7VgQCn5LOy34dt7kXhJ3iq2PUvxLvARgMG5rwkp55WjA4z1L0vKMDzkmP9zGX7yHB_ge0OW6l1uDREm_v_sBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇳
🇺🇸
سخنگوی وزارت خارجه چین: ترامپ از چارشنبه ۱۳می تا جمعه ۱۵می (۲۳ تا ۲۵ اردیبهشت) میاد چین.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/64871" target="_blank">📅 08:04 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64870">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ca5d9dd02.mp4?token=ZXoB897mK3DLh6w_xjvAaHWc52bT5h_kxZrTTZ7ZACXR_riARakwkYjuuECMNbNNds82yTnLsQ_Nib__BgnznX-UeX8GueSr982_0vmROpDMGraMSNcf-DOtAGOLudSmlE0PzlUKkPkGj1jfH0J2K1wZF5ycsxdm1tBY_c31U6Zs-TQWCC9ZDYv1a4LPkgBKl4qBmLinot4kULGYStX2muvR91bH5kDN5Yw2tfU8wjVCfydfLFPLGFP1zTnAwDwi6VNitREsIKmSo3CQtLUAcn3pU_qMg7Bq5FFSj9I0O2rS1HoLoHS5qTIWgGus7coo6ak-WiyOGz_Yun2XDJg1Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ca5d9dd02.mp4?token=ZXoB897mK3DLh6w_xjvAaHWc52bT5h_kxZrTTZ7ZACXR_riARakwkYjuuECMNbNNds82yTnLsQ_Nib__BgnznX-UeX8GueSr982_0vmROpDMGraMSNcf-DOtAGOLudSmlE0PzlUKkPkGj1jfH0J2K1wZF5ycsxdm1tBY_c31U6Zs-TQWCC9ZDYv1a4LPkgBKl4qBmLinot4kULGYStX2muvR91bH5kDN5Yw2tfU8wjVCfydfLFPLGFP1zTnAwDwi6VNitREsIKmSo3CQtLUAcn3pU_qMg7Bq5FFSj9I0O2rS1HoLoHS5qTIWgGus7coo6ak-WiyOGz_Yun2XDJg1Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
نتانیاهو درباره احتمال سقوط رژیم جمهوری اسلامی:
فکر می‌کنم که نمی‌توان پیش‌بینی کرد که چه زمانی این اتفاق می‌افتد. آیا ممکن است؟ بله. آیا تضمین شده است؟ خیر.
شبیه ورشکستگی است — به تدریج پیش می‌رود و سپس سقوط می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/64870" target="_blank">📅 05:55 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64869">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d34c8a4b81.mp4?token=avtTvGWO3ia5B_5u2qEnpWAErYPZSbM05jE4ja8tfsmFArHkwpPaJBqDYSO0H0r9I2p5WPw7RVllJztDaJXSCID9h17Cj3tdOonREWYfzK7MiRsoNApy-p52ZGgsUcPS84jDeQmiGCb8YKDFWlPrGPSipFd11TAyh3o0kH9ICAooIjEVrBdRfLlXQGpiG8PMa5ZB16c_Zd5L8vzR2mLp8zu2gYrj85xrLsu-08dmLNRZnyQ-uTpXhXbUDrlGFw1Y8ao7Z28zM3cf9BHnrdB2sP-dvAMiVOG99Qvr8SpH0l5uTJMWih_k5k2cPOT_3MiWYMfE_B9fwLwUwTFQqWjR0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d34c8a4b81.mp4?token=avtTvGWO3ia5B_5u2qEnpWAErYPZSbM05jE4ja8tfsmFArHkwpPaJBqDYSO0H0r9I2p5WPw7RVllJztDaJXSCID9h17Cj3tdOonREWYfzK7MiRsoNApy-p52ZGgsUcPS84jDeQmiGCb8YKDFWlPrGPSipFd11TAyh3o0kH9ICAooIjEVrBdRfLlXQGpiG8PMa5ZB16c_Zd5L8vzR2mLp8zu2gYrj85xrLsu-08dmLNRZnyQ-uTpXhXbUDrlGFw1Y8ao7Z28zM3cf9BHnrdB2sP-dvAMiVOG99Qvr8SpH0l5uTJMWih_k5k2cPOT_3MiWYMfE_B9fwLwUwTFQqWjR0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
نتانیاهو:
در ایران، به نام من خیابان نام‌گذاری کرده‌اند. می‌دانید؟ البته بعد از رئیس‌جمهور ترامپ هم همین‌طور، چون او رهبری این نبرد را بر عهده دارد.
اما یک چیزی هست  من فارسی بلد نیستم ولی آن‌ها به من می‌گویند “بی‌بی جون”، یعنی بی‌بیِ عزیز.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/64869" target="_blank">📅 05:53 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64868">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">یک ماه و سه روز از ورودمون به چرخه‌ی سیرک‌وارِ مذاکراتی گذشت، و این چرخه مطمئنا تا روز دیدار ترامپ و شی ادامه داره [اولین رویداد مشخص شده در تصویر]، و بعد از این دیدار بهترین زمان برای آمریکا جهت آغاز مجدد درگیری ها به حساب میاد   #hjAly</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/64868" target="_blank">📅 02:38 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64867">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vn-asDI3J2X3Mdf6QvGcyQp9Ig2t8fglfs-_GQ-ypsVbTwOu4plSEtdzVucAPC2nzd8qG8ZBTGI6sJhCFDSeF3xkr-PKU1jSdww5mLTFNspxVuqudmyxUoS5WpxbpIgD2oADhH46XmUfygx5o6raV2UE-AEYGaZnfHM7oiJmd2RbrBAYczQRNHQvRJfJ-kIet8Yucx-qkSGCzwl9glcHvBsn2NcPsF6IxqK-i3BCNe-X7PPBbxw6l6s5IuQJICqFwevgda7ArLon74pMQ97snBvmGMZ-wdBt6WCWRky-E65WUPb53b2-i0eWjPQ0DSrU-s4P6hpz56pIwb-4PJk-Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنظر می‌رسه تکلیف خیلی از مسائلِ کشور در دیدار آخر هفته بین ترامپ و شی مشخص می‌شه  البته که در همین حالِ‌حاضر، احتمال از سرگیری جنگ خیلی از بیشتر از موفقیتِ مذاکراته، آمریکا بعد از خارج کردن اورانیوم های ونزوئلا، هدفش دقیقا انجام همین فرایند در ایرانه و با…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/64867" target="_blank">📅 02:18 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64866">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/s2539ElSGsAS5Hc7AulDaCRl7WJ3FD_i8p4OW_GdwHp93YAaR9QcK7bVneCaYAhIlj-OBpcENoAvK-ZlhQlk5tMD-qvgConn18oqtYo-yMz40Nsa_VTWYf_4QQjHMRocC-WXUlRzFPjx5StRXrKdOuWSqQ7ddJp-zVnzMhyhMHCDyt2NaK5GdtO__cNP-J8xOdfAb1nvIV9iKZM6r7JSFHuBn7fqKqk3b2VE1faWbXe46uP9wB58IKNncLhCsK6XTi6W49DgABJEKhk4_zvN8luOHbPZFb4AjjVm-Jc7ClcIE3BEypmi7UUGHPb1l4wEqbs_nbkhPbZTG5lwGTJo6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تخفیف فوق‌العاده - ظرفیت محدود
سرویس اقتصادی با کیفیت موجود شد
💥
10 گیگ فقط =>> 1,700,000 ت
20 گیگ  فقط =>> 3,100,000 ت
40 گیگ فقط =>> 5,600,000 ت
سرور ها  v2ray هستن کاملا با کیفیت بدون قعطی
خرید
@amoadmins_bot
@amoadmins_bot</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/news_hut/64866" target="_blank">📅 02:12 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64865">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQaCmeAZkl7MuVZxFxa2gZ7mzkKryYWb2uWAXKtyRcV5NtQyIMLwU8tF1cRG5mNvcwVsoAebilnfo9QNXbDhCaK_I-jwOOQ0-hGZMTK3H62dtyXgCgLCLUI8S-zYmW4oWdFbGAEuXEDFN6X_ss0KsQuVg2beAGeBLi7-IxhoX1cgmpglgf9dHBnRBUxDjiQ8sQnCUsVDfd8XjXXYBkL2DVgQZ7p2UjHSwUsB00tqKmv_50muHvcYvbt9V3Y2OBwU4hGlXYOUATXyeFdr26utgxS_2KTsSoUCaqLZuITWQ35vx0WHCXY-eeJegVvPldPqcyXa3QmsdnMSy6llIJDK1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داریم به دو رویداد مهم نزدیک می‌شیم  ۱.اولین‌دیدار ترامپ در دوره‌ی جدید ریاست جمهوری خود با رئیس جمهور چین ۲‌.آغاز جام جهانی ۲۰۲۶  می‌شه گفت عملیات آزادی که ترامپ استارتش رو زد بخاطر دیدارش با رئیس جمهور چینه و می‌خواد حداقل وضعیت تنگه رو از این آشفتگی در…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/64865" target="_blank">📅 02:08 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64864">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🇺🇸
؛ ترامپ: از پاسخ ایران راضی نیستم   @News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/64864" target="_blank">📅 23:57 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64863">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">خبرگزاری فارس: مولوی عبدالحمید همکارِ نتانیاهو و ترامپه!
@News_hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/64863" target="_blank">📅 23:54 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64862">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBCu9Z6Z-8yUdsK2ybcUr-546dhpI8ZTAgl5IxLFWLNVndn7N-JFcycWyBiaFvTAMK4XOyxRsgzwE196WfNfmVWZILPb4z6jGH7on_rTLfW406Onj4tZ1M-_r2ys09uEA6qmZUMEAQGYVShXUqPJsc3g5Vu06UB5GKbKBHqWdOgmep7IIt4CXFyvniGO3kUXCz1WpGUB8d-2hcvzsItUz5Ex_6uz97k0eVXzp_cHIXoVgdDrv7pD8YLKhA1g_jbMlY_k4_vQ_DgUAV0OLec42eXQHs5f_ljJbKVW8izF1OwubvHY7vs296c6JIykgmr4R6TDm0FMAsyyg4jjr6TZLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
؛ ترامپ: از پاسخ ایران راضی نیستم
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/64862" target="_blank">📅 23:47 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64861">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">بعد مدت‌ها دارم ال‌کلاسیکو می‌بینم این چه کصشریه کاپیتان دو تیم وینسیسوس و پدری شدن یه زمانی کاسیاس و پویول بودن ابهتی داشت بازوبند
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/64861" target="_blank">📅 22:35 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64860">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d27dd7e9a1.mp4?token=kQx86dOnB4Pul-JldByUS3AiuXVvnvcFmI38aAuqiyE3Ru2pkIs2A0pH17ZZRR2Zvbsi2uCXREZz0r_I-ixz9PZ6wVKwZVstfGibVPrKentafGJ-pgz6cr95HyRNdS9zz1sWkeaVXbpQW4Dsy8XpFFxY9RaN-9achNjWnF0n5UKP6G81q6Cm5v_eUcIHNpwWK8fYAq3RUbcGX6VFQVAvjwZb-DExWJD-qUjgMdCv4ZYZdSDQq9h_kD1vrRzESh8FF8d7yqVU35MpIFlFiQOytbUNgbfhmK8WsWV-krMCcs1_-QnjJbeGa3JE7thJ2bh8wBOhM1E4nXAGJOVhMH3lRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d27dd7e9a1.mp4?token=kQx86dOnB4Pul-JldByUS3AiuXVvnvcFmI38aAuqiyE3Ru2pkIs2A0pH17ZZRR2Zvbsi2uCXREZz0r_I-ixz9PZ6wVKwZVstfGibVPrKentafGJ-pgz6cr95HyRNdS9zz1sWkeaVXbpQW4Dsy8XpFFxY9RaN-9achNjWnF0n5UKP6G81q6Cm5v_eUcIHNpwWK8fYAq3RUbcGX6VFQVAvjwZb-DExWJD-qUjgMdCv4ZYZdSDQq9h_kD1vrRzESh8FF8d7yqVU35MpIFlFiQOytbUNgbfhmK8WsWV-krMCcs1_-QnjJbeGa3JE7thJ2bh8wBOhM1E4nXAGJOVhMH3lRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: اونا دیگه نمی‌خندن
.
مجتبی و فرماندهای سپاه:
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/64860" target="_blank">📅 22:27 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64859">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: ایران به مدت ۴۷ سال با ایالات متحده و بقیه جهان بازی کرده است (تأخیر، تأخیر، تأخیر!)، و سپس بالاخره وقتی باراک حسین اوباما رئیس‌جمهور شد، به «گنج» رسید. او نه تنها با آنها خوب بود، بلکه عالی بود، در واقع به طرف آنها رفت، اسرائیل و همه متحدان دیگر…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/64859" target="_blank">📅 21:42 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64858">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2VkIdzeIIYGDVxo7Lb2EhpMHS5j1Grib4sAsmdeT53eWeNUoqlqfMAk9bVPMye69YcR8pckooYsGDj5rsdqL3Mz2qDulVKhCPcyez8awpw62LOGpmcSxd7k6_51iY8NHiQblZtquwhzyghbnwYcLOQA6J-mFnaG0xdQb-qg4_by2Q7Prb1OrZCO2kAV786ORHeMWqiR_Ib_7u3Ae4kz0xArGM4oWB5LAOJRelnxk3aLY29r_LFV9qBF2avP-EauJtYMhpyjWGegjfE9xAHXRy5Ez3ojo4j4LURG2SmtjqyPPOypj72hc0qYr-0j2p5yuhNuJ7QNUi_3BtINNY4uUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ:
ایران به مدت ۴۷ سال با ایالات متحده و بقیه جهان بازی کرده است (تأخیر، تأخیر، تأخیر!)، و سپس بالاخره وقتی باراک حسین اوباما رئیس‌جمهور شد، به «گنج» رسید.
او نه تنها با آنها خوب بود، بلکه عالی بود، در واقع به طرف آنها رفت، اسرائیل و همه متحدان دیگر را رها کرد و به ایران یک فرصت جدید و بسیار قدرتمند زندگی داد.
صدها میلیارد دلار و ۱.۷ میلیارد دلار پول نقد سبز به تهران منتقل شد و روی یک سینی نقره‌ای به آنها داده شد. هر بانکی در واشنگتن دی سی، ویرجینیا و مریلند خالی شد — اینقدر پول زیاد بود که وقتی رسید، اوباش ایرانی نمی‌دانستند با آن چه کنند.
آنها هرگز چنین پولی ندیده بودند و دیگر هم نخواهند دید. پول‌ها در چمدان‌ها و کیف‌ها از هواپیما خارج شدند و ایرانی‌ها نمی‌توانستند خوش‌شانسی خود را باور کنند.
آنها بالاخره بزرگ‌ترین ساده‌لوح را پیدا کردند، به شکل یک رئیس‌جمهور ضعیف و احمق آمریکایی. او به عنوان «رهبر» ما فاجعه بود، اما نه به بدی جو بایدن خواب‌آلود!
برای ۴۷ سال ایرانی‌ها ما را «آزمایش» کرده‌اند، ما را منتظر نگه داشته‌اند، مردم ما را با بمب‌های کنار جاده‌ای کشته‌اند، اعتراضات را سرکوب کرده‌اند و اخیراً ۴۲ هزار معترض بی‌گناه و بی‌سلاح را از بین برده‌اند و به کشور ما که حالا دوباره بزرگ شده است، می‌خندند. آنها دیگر نخواهند خندید!
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/64858" target="_blank">📅 21:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64857">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/777e4c1402.mp4?token=hBZzEi0mlPT9Q6SxnKWdOAU6bmSrUFPS4GApR5NeRKWRNAFwhgQi2Yifs1A-AL8uAdZ5lAU6b8P3R7vPorMDFQSbH-m90plrlihMLD_nCQURCJdwqdmY7xqQ61N6b8nbi-55yuHwidXyddM8ZkuWhTegiqRvvtctzLdOX1oDIfsyY9jIuStP1iJPc9b8T2vIY0FhkgFLno6y-Xw0MVCYg1j_kyv9YAM0_QExylH7Hoi08gVXgHBbXqqWzdRbJTV37cpAqn1Ub9iUTFGQFXi4v23LiWMjO-njp7wel4afgbFytV8Ui_5nhr_yPvn2C9VX1H0XBmaa2DpI5krG15DMSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/777e4c1402.mp4?token=hBZzEi0mlPT9Q6SxnKWdOAU6bmSrUFPS4GApR5NeRKWRNAFwhgQi2Yifs1A-AL8uAdZ5lAU6b8P3R7vPorMDFQSbH-m90plrlihMLD_nCQURCJdwqdmY7xqQ61N6b8nbi-55yuHwidXyddM8ZkuWhTegiqRvvtctzLdOX1oDIfsyY9jIuStP1iJPc9b8T2vIY0FhkgFLno6y-Xw0MVCYg1j_kyv9YAM0_QExylH7Hoi08gVXgHBbXqqWzdRbJTV37cpAqn1Ub9iUTFGQFXi4v23LiWMjO-njp7wel4afgbFytV8Ui_5nhr_yPvn2C9VX1H0XBmaa2DpI5krG15DMSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری: چگونه تصور می‌کنید اورانیوم بسیار غنی‌شده از ایران خارج شود؟
🇮🇱
نتانیاهو: شما وارد می‌شوید و آن را خارج می‌کنید. رئیس‌جمهور ترامپ به من گفته است، «می‌خواهم وارد آنجا شوم.»
من جدول زمانی برای آن نمی‌دهم، اما می‌گویم این یک مأموریت فوق‌العاده مهم است.
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/64857" target="_blank">📅 21:27 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64856">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bf0dbe0a2.mp4?token=awsYVF7b7MydlfPoKcvjNyOK2yvE1HPrpuJXFjruGQW_k-N68ulhELFAXQIupsnc1zGC9DiOat9Nu2-8v-6Lgs7SfYxKUCT477_701a-MDO_zOBn0r6u7EBQhgrWo2mGhUMlpvVagY1qxv3s-uSkVMmyvwRJavZkSk8QXRjNzNrtaPeB0gJrSKZkXiGocey5CV8rA09X5dwQXhyxBYiKZpmXiIqrtfaplxuQwFHt8hEy-Xe7WAa0Xa3_v01rJ0wGVoB10PBCc3Ri6Jfhq5_O6dqrtwiPsFGnCgIV3rAS_6VPTV12pkkpAgvxdVksy4XMBmbdbDQOs1SSB53H894A7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bf0dbe0a2.mp4?token=awsYVF7b7MydlfPoKcvjNyOK2yvE1HPrpuJXFjruGQW_k-N68ulhELFAXQIupsnc1zGC9DiOat9Nu2-8v-6Lgs7SfYxKUCT477_701a-MDO_zOBn0r6u7EBQhgrWo2mGhUMlpvVagY1qxv3s-uSkVMmyvwRJavZkSk8QXRjNzNrtaPeB0gJrSKZkXiGocey5CV8rA09X5dwQXhyxBYiKZpmXiIqrtfaplxuQwFHt8hEy-Xe7WAa0Xa3_v01rJ0wGVoB10PBCc3Ri6Jfhq5_O6dqrtwiPsFGnCgIV3rAS_6VPTV12pkkpAgvxdVksy4XMBmbdbDQOs1SSB53H894A7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: جنگ با ایران هنوز تموم نشده، چون هنوز یه مقدار اورانیوم غنی‌شده تو ایران مونده که باید از ایران خارج بشه
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/64856" target="_blank">📅 20:35 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64855">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAriya</strong></div>
<div class="tg-text">احتمال حقیقت پیدا کردن پست آخرت از تو رابطه رفتن من بیشتره</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/64855" target="_blank">📅 20:19 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64854">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZCGAL6wbA4EVx8mUU0EFTHgfEc9GAC_xEUQg4xEDzh5t5pVKJNeqWJN7d3XCNCq2iaGfd9l_dP9P-bWtVHsBdcQt7iTRMjE2VxICpt7kep9PrtadlP_cR4QadU7OGMzVXDDAtU-36iubvGOA3ZCOBX-cPbeaAOJfiIWnlyBvZcPHYdN8JtNPMRhdAhiB5Sp9OqN00G5tOYkBN6s6Ri2xuN2oavJp-sjIxVY0vkjEDUc6Ti5gy503lWnFWAQ-iKScNpt5tgIhpwrvBAwDF_mXgTpTriUXLTcdyoCMXZdIOeB1xgnYpVvPyjFu_QuXD5S8AFRuaMyff7Cas6Ah89rMfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا سیدمجتبی
🔥
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/64854" target="_blank">📅 19:53 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64853">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">این وسط کره‌شمالی(آینده بقای جمهوری اسلامی) قانونی رو وضع کرد که اگر رهبر این کشور ینی کیم‌جونگ اون ترور بشه به اون کشور حمله کننده بمب اتمی بزنن
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/64853" target="_blank">📅 16:34 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64852">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Dq3h6PmLlCLkGcr152oGDd3bGhUvEaoWCRzYejak-ZLqIf3R3LanuKFfo3hJMqGjHEe9QYGIOHLwPy34P5MdqpB77A5sM1UDiRnhYaixPIvj3AeCXCHTtvNw84M8OIfNtqrONv7vXs73yoxbCgrVhqtukun36HZn9bSqAqdjn1oAgI-XCorktJzYMnTtlDnRDUhoj_q-VBSYU20-3YrXotlto-YQ4MX-KZmlpxnPt8uKH-3nJ9LiqKmVglHH-fSNDf1D8PTRNWrVSCydlNO_qQLWavCkCvJxvtnF0imHlfzjmeqi8nqeLvrO2Bcrnp2b3QmiZQurb8Zvyh0btlbuEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📰
خبرگزاری جمهوری اسلامی، ایرنا: ایران پاسخ پیشنهاد متنی امریکا رو به واسطه پاکستانی ارسال کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/64852" target="_blank">📅 16:23 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64851">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81439301a6.mp4?token=FpeAAJDf_gN9Z5B0tYtD3pQzexlx8XJXpVkTs8E5b39SOay2o43VpZ9m3gjo3pilXJKWzoq1MPPekPjILrbU3DVOMRMrrYYQ_XuDOjSqXsDI0Fd6jJzNgaUE2SrX-VllLkJoxmtyQZ3Mf8IZQRdfevSfn0hdMyD_gnjEnn2JsxnK6U6YEfeU8ZrE_F9YdQgbwzUJhPymczpfY0HFisdDvvwI6NPbraLSWcK0xIKOvWmg1YnhnK-qcw8ipm8dQP3hSACYhsgmb80FvrpUG_a1yAyk1OR_517Nm3lxsEi1pTbECtNx3F6eDV98QMTKFgfohCEj8M0T7_IHsApgCYMW3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81439301a6.mp4?token=FpeAAJDf_gN9Z5B0tYtD3pQzexlx8XJXpVkTs8E5b39SOay2o43VpZ9m3gjo3pilXJKWzoq1MPPekPjILrbU3DVOMRMrrYYQ_XuDOjSqXsDI0Fd6jJzNgaUE2SrX-VllLkJoxmtyQZ3Mf8IZQRdfevSfn0hdMyD_gnjEnn2JsxnK6U6YEfeU8ZrE_F9YdQgbwzUJhPymczpfY0HFisdDvvwI6NPbraLSWcK0xIKOvWmg1YnhnK-qcw8ipm8dQP3hSACYhsgmb80FvrpUG_a1yAyk1OR_517Nm3lxsEi1pTbECtNx3F6eDV98QMTKFgfohCEj8M0T7_IHsApgCYMW3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در همین حین که ما تو ایران هی داریم به عقب برمی‌گردیم، برقمون بیشتر قطع میشه و اینترنت نداریم؛ بعد از ۱۵ سال تو سوریه دوباره «ویزا» و «مسترکارد» برگشت و مردم‌ش دوباره دارن به بدیهی ترین حقوق شهروندیشون میرسن.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/64851" target="_blank">📅 16:19 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64850">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01d351c3a4.mp4?token=keT6svS6XfjfQxpudx4x1l4RsA65P0vkFkrdq9rgT9jonbV5N8uH4S5qs_eHEQAQj1d9nHv_ItTZEO4f0e6skJp5jXzBwC-Pj1cQKNNT4crnJsvAOySbeoUBlaq3jHKk59ur0xXu0b_U_0nLUbzPHIjk1KCfrWWEhvY27GejqNhV6ook-5F6e9ITU8h5THu7ZDSpsqPfCGna_VfekNSwSOtPCX38_P4SMHGCF3WjAIR2S6Una5geN5kmPV9dGOG-q5AzFN-SBoufeqHXt51NU5l7BW0q50O0zap4rYLsBgFlkIUZpVEQzqvL6_OIul4moaOKAqLS2bOya-Di3XmAhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01d351c3a4.mp4?token=keT6svS6XfjfQxpudx4x1l4RsA65P0vkFkrdq9rgT9jonbV5N8uH4S5qs_eHEQAQj1d9nHv_ItTZEO4f0e6skJp5jXzBwC-Pj1cQKNNT4crnJsvAOySbeoUBlaq3jHKk59ur0xXu0b_U_0nLUbzPHIjk1KCfrWWEhvY27GejqNhV6ook-5F6e9ITU8h5THu7ZDSpsqPfCGna_VfekNSwSOtPCX38_P4SMHGCF3WjAIR2S6Una5geN5kmPV9dGOG-q5AzFN-SBoufeqHXt51NU5l7BW0q50O0zap4rYLsBgFlkIUZpVEQzqvL6_OIul4moaOKAqLS2bOya-Di3XmAhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز 10می روز جهانی مادره
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/64850" target="_blank">📅 12:44 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64847">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u1efO8n-iWgatGlvIquWrGKLRsYY51kwZbgJCb2mWBThJj7HVN39QEywuY77iPSNf3VMp0erHRSiNKJU8hz-QTARHNIRu80d4GrUFmnBBo-p47aYv1honX1YBHiV_KYM5TWE2e6TD_xGzyKTX8JprcmqpfX3_aEb4laxHnFMUNLUTSUxsaebZmCz6Kkl1rdPXzEOQJRwAvKp5eTLMFjSTgvlV5ni_vxIIFksVMxBA-Ych9KsWw-B2nwJLkuGoRu0bUnfkzWe78Rcgq516W4pGMdBgpFR_m0_Ir26w0P2tOCiutpPGsg__kvqrWx7XGiIe9nh8AQ028-a8RkGjc-gqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZRGexGRZdnqSwBI06DFQ1H24NeIdf2MuknPDwX-S09vTVyBtYFN4o9MYD1VwXNQPe5-HLjRREtzcBXqOzl352uXjclJ4K7luojVhaYIe48eEQroon4BppkRgXU1tyWMvyq8gYMtRfTGxzzhRTzpt1QcsuQAZX5-vYRyRPO-EMzTIecdF-wtbpeLvSTfAIwQaRLUtmVayZbiZolGUapdHEOUc1qtFHyQp3d4KuUckx7tLJpKRbpSIrOu4pnShQHyPjwEOIK93AKM_stHSvM3mPwdK-gT0kF1-fJE3QKv3K0vSDdh9cbt8ePqqbVD6HpAQKyHNDW3g1D8JpkPJ7H0z4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L0zfZD5TeYCbEnap3rBnUjZgu6M5ZySHkxUI87LuJjs3x4d_DHK8W2q5HWZocQUpcM7pMKOc6nk2f2aDubgMYC11ttAuegaU-exCJGiwrMIFcNMc3914rV9rqklTM44SJk8G94UagnCvhH3vQ4_nW3qWfmCg8d9vovh5NwpEMJi08GBjpfN1A_q68nGN9zhs5KxH-NJQ904H4SeQKUUyfDvHWkcc9KL84ZnYEovqiRCMvF6cr1Ow5Q3r6PyJvBtWifVNdmoGLvei0zpHM9OlkqKHfVhH7Hnm8_KQXfck0e84x5Uz_T3voUD76sdLpit_vwHKKxEn5SQR7zZ7aIHVFw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست های دیشب ترامپِ بیکار تو تر‌وث‌سوشال
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/64847" target="_blank">📅 09:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64846">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">❤️
تلگرام از هوش‌مصنوعی و دستیار جدیدش با نام «@mira» رو نمایی کرد  امکانات رایگانش شامل چت متنی نامحدود، تبدیل ویس به متن، تبدیل متن به صدا، جستجو داخل اینترنت، تحلیل تصاویر، ساخت ریمایندر، لینک سوال ناشناس و حتی مدیریت والت شبکه TON روی تست‌نته. بخش پولی…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/64846" target="_blank">📅 09:26 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64845">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
📰
وال استریت ژورنال: اسرائیل یک پایگاه مخفی در عراق ساخته بود که برای نیروهای ویژه، تیم‌های جست‌و‌جو و نجات به کار می‌رفت.  اسرائیل با اطلاع آمریکا، یک پایگاه نظامی مخفی در بیابان غربی عراق پیش از جنگ با ایران تأسیس کرد. این پایگاه توسط نیروهای ویژه اسرائیل…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/64845" target="_blank">📅 09:22 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64844">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/syZJKYBArsOrkb6Pmo22YmOxxSwJv1vcjLeidTFNN5B_7mXdVZGUKI_0i0qk1ngTmeoz3NPj303zcOPd-FnirDP7sFt9Lr5uBdvGYRQMMd0_SkP_APtYiYinSxz204LbzPl3m_sJpjZO9Vlwt_5WqwIQp-Z3R4XhfghOFTLVGTYmV4n6bBzzVfA4HZLSJ07eZzbFpG96328eEr4VE-_ik9tntJ4XIK-IjUby8CA_OB9pfwbogocjY6IwPMxMnnDVrc_1D60XgKJ8Fmh-XEX3vku4KbXkAQuRg0oZ7yUpIB-ofQKrts70da9UH5L3nYE_tk2vkzJUlwl8htUGOOPauw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه: از این به بعد اگه امریکا به نفتکش‌های ما حمله کنه در عوض ما به یکی از پایگاه‌ها یا کشتی‌های امریکا تو منطقه تهاجم سنگنین می‌کنیم
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/64844" target="_blank">📅 08:36 · 20 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
