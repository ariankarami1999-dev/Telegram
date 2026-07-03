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
<img src="https://cdn4.telesco.pe/file/TOn3M6IjdpmkKHQ0QjtKns5ZMTMuCx2PponC68cHUk_vsqGpCYCiHB5BMvpH7pWxysMaHCbybOfYYK5yFBUSogP8-LoeUIuH_nxYdUvZfW3yg7x_IMowagBGDHqP2FnQ2Od5RE5wxObDOSdalcyCarG-xsh7J1iCBmhYoH5lMqXLJdGTKNGTZm8D68YUAHTrKoNC-RyyURgXIoRB-YiCpWYRhktO4DWRqOWujyYuwK1QF_Z3ZxUcCXeoOp5LLBuZoJkpccDcL8XOS89XsendHetu3OftIeeBigA20WfhgvHz-DyHs7MqfXDvFjaT_F3r61Vea7QPiCFVlcZbkDUYLQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.1M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-12 09:52:45</div>
<hr>

<div class="tg-post" id="msg-665817">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f860cc7e0.mp4?token=F-yxY6Vq4xvityomyf0FumJU2q-oELjVHgfLv6y0rgbjyhdw4gNmSZUhsZNo3kLDAbSd-jiKiRIenuBmon6NG003vupV3YdkfAncPvzVZgxnoloXwXVJXjhvn7xN1De76IymM_7c_jZrmbNPtLG5h4g3tG_WZ1rPf4v9bOJPC8AKjgApHoPVjcl2sTNHeDjX61rstHU0JP8wfjQLOS2j8cuYDOq0yAVijyO8cUetW0ThMIm1Z4jMRpNEycbwaky9A6qoOiqhsJti4bodkG_CoUpY3eE1ytcBO2ibmUrTfnx_O5wETEk44XyOcyyrnmVTjDBJW97QhCOEbNgDONmTIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f860cc7e0.mp4?token=F-yxY6Vq4xvityomyf0FumJU2q-oELjVHgfLv6y0rgbjyhdw4gNmSZUhsZNo3kLDAbSd-jiKiRIenuBmon6NG003vupV3YdkfAncPvzVZgxnoloXwXVJXjhvn7xN1De76IymM_7c_jZrmbNPtLG5h4g3tG_WZ1rPf4v9bOJPC8AKjgApHoPVjcl2sTNHeDjX61rstHU0JP8wfjQLOS2j8cuYDOq0yAVijyO8cUetW0ThMIm1Z4jMRpNEycbwaky9A6qoOiqhsJti4bodkG_CoUpY3eE1ytcBO2ibmUrTfnx_O5wETEk44XyOcyyrnmVTjDBJW97QhCOEbNgDONmTIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برخورد خشن پلیس آمریکا با هوادار تیم ملی مصر که در حال گرفتن سلفی با یکی از بازیکنان این تیم بود
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/akhbarefori/665817" target="_blank">📅 09:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665816">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vXD72h4laj8ENZU7uoMVWzVtosfRi2kT5COoOvWc3TFrFZvIPJRDYoTqLZGHFCXpNPQueyZ1Nn5ZrvVMgE2PHqGE1QWantaivErZ8VEzSM9oBC_jswv_EDIzDVy6DtFFGHoXcAqMkwYRfgsYePHLkEh9v8gzR8oZ5kNgAvYdi0Jxdzgc9laemqoskp5ClWKDHcWqdHCNvYPzUpzD0UqXyZHOIoZEkg-1rAecqrRRCw56g3xOslNuWCen3rmjD3qGAXftUSDH6mjGx0txHbseJ89WGZFgPQzICxNGYALBCGhVnhveD_UdbA9zmHYwgU92NLL8hfO7qzSqNGZHlYdN6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
ادای احترام احمد مسعود فرمانده مقاومت افغانستان بر پیکر مطهر رهبر شهید انقلاب
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/akhbarefori/665816" target="_blank">📅 09:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665815">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYzqb8VwBhFQY765sUqkrYsJm_OxBysyhKzYZPpVKg_sbLtRvpL0_azKoCr1BqncoeffWA1z7No8dMgnaFEjzqhl6S5yBiWIHg9Lp8lZ-IG5YgBdZgCLXFHgCRx0aFinXTg9cazZj-sdodsEQQEcb_3q_HkV_CzaJk5UptjeEAPMOWy1ZBDmQ6nXGusPJKHE7A2h2fA6T64KPRDaqPjldjGpwJ3GDImfgm1H6QcF8wGaPcyB3GCBG6DwKHreuFeF7Cu6GIYN_Viz0FzRhJDV0wvycmoJOe0_BQeuVcY4DX2yV3Dpn4uW-cwry8-WAiMjErpXqLt69NJPxIi5ms761Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نوشیدن منظم قهوه تا ۶ سال مغز را جوانتر می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/akhbarefori/665815" target="_blank">📅 09:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665814">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d463bb3a6.mp4?token=ERPlp5eREWG2iC9q1cybPTE3BXDDT_X1qb-p-AeP9t6BZDQGCezPIghetUTbrP43sAzcxGNiQW6MXiqA4_B0g6HXtWVXeyNH8ByYF0MuBIrjr3jnmHR2y0zx72jRB_BYcdHSmSz7ZglyPzRwwRy_LD9nDsEqLqs5vKSjiYgGaSnKGkVBK7LZVxy_eFiZ_3TEXpU960smXMs4kO-6WylKZA7tS8ipRLS4pqXmzA_oT2ADftO3X8yHw8cyBwVhk5gskUhNIkXf_I1vZCoELx8aSF_DWXWxPB89Au4_JJcPEJ9YQKvEapt5AB4xVvgvFkDSIC_BleozDdXV3HuNA22vdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d463bb3a6.mp4?token=ERPlp5eREWG2iC9q1cybPTE3BXDDT_X1qb-p-AeP9t6BZDQGCezPIghetUTbrP43sAzcxGNiQW6MXiqA4_B0g6HXtWVXeyNH8ByYF0MuBIrjr3jnmHR2y0zx72jRB_BYcdHSmSz7ZglyPzRwwRy_LD9nDsEqLqs5vKSjiYgGaSnKGkVBK7LZVxy_eFiZ_3TEXpU960smXMs4kO-6WylKZA7tS8ipRLS4pqXmzA_oT2ADftO3X8yHw8cyBwVhk5gskUhNIkXf_I1vZCoELx8aSF_DWXWxPB89Au4_JJcPEJ9YQKvEapt5AB4xVvgvFkDSIC_BleozDdXV3HuNA22vdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام اعضای جنبش امل لبنان به رهبر شهید
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/akhbarefori/665814" target="_blank">📅 09:37 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665813">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCSRPvfr_IuzPrFdvy0IEu49EDDkjUtMvM3RhozO-WU6ScB063D0BZoZ_GpqACnsFyV3aHv7P7HQbmTOoaOyzL5bKAx3fY4cca3F6cIsGo6Hz8JyShEJtXE7YGBVWPqVGJ6mMmMolY0IzSb56ygTWA04DlWZXuwNNIDx-5qafAOzSN22SIPx2Znjog_bsuiFWZhIA098SbZKn7gksLIIjZVBlpB-c4DuJ1TXiz6i3oSkZhD4y5E0erQ-rvUcWi8Ne8EagaPrNT5-BUo9AO6naZB1z6sfDJngDILQjPHjG6DwXlx-PvhVPkyqcnMZJ2W-nA5haMSCOVGkzLu2gY-pKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ورود پیکر مطهر شهیده «زهرا محمدی گلپایگانی» نوه ۳ ساله رهبر شهید انقلاب به مصلی تهران #بدرقه_یار
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/akhbarefori/665813" target="_blank">📅 09:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665812">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52f5f27434.mp4?token=oPljT9eykgWA17H7WzWZyY1C373zwzU5FKnl8s_b1QHcHCH00i0egiD7aHVoaS0XXVjwZK9Id4Rd2t2iaeogLaf4n5B8Iv3BKrMGi8yoKiY2ey_XsiXcNgJUhVoRNjKiZvwtSVJlSccgLBsRPmYHbl3R8sxFDZ-3TyWOzi0-TodQQSGvL8IxQnOTw3bjx5h3SATazdD7IMLQ5EeQiC9u1WzSbYwQmAjtpqewfcnUNz6ZLfWqMlt8_qFMyXrd-ee4QOLf9VipxnCIrtbDXUOFor_QDxkPAWiKzMtlXl7ZBMvI-toEGCpIRkFly8sGFSC4h0603k5dndwdG67L0UL1q0dBIIzmJwpqWH4TEJ3vwlkXl_b6fLcJ1Y12wiLqPQC_TL2W3AwST4kfh63lDcODnhZmCGaIn5N0Ed4kKWAPmHW4ISXfhC6y77mPTTsUygGulHQOZ4C0s74rdAzpXGNbWVWDbnrrGU8VWvcO4ZJ5kyGzoc-_Pi8nkJ8joXuHL8xHCd3lfqv7dLunZYBlSs9ySbd8p7aRr8GkG-kOG_2eBych6jetK2tmLTZRFpk1YYMpFAyPzJ99gN4lSVELRgVH0hnlYV7RWaE2FJIUCawRJaVF5W5zBicSMN7CVeQnqNJdBrmL9Ca4_Y3wfxl2Mh-RjkaFRcEMTkF2rV5ASU7O2OY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52f5f27434.mp4?token=oPljT9eykgWA17H7WzWZyY1C373zwzU5FKnl8s_b1QHcHCH00i0egiD7aHVoaS0XXVjwZK9Id4Rd2t2iaeogLaf4n5B8Iv3BKrMGi8yoKiY2ey_XsiXcNgJUhVoRNjKiZvwtSVJlSccgLBsRPmYHbl3R8sxFDZ-3TyWOzi0-TodQQSGvL8IxQnOTw3bjx5h3SATazdD7IMLQ5EeQiC9u1WzSbYwQmAjtpqewfcnUNz6ZLfWqMlt8_qFMyXrd-ee4QOLf9VipxnCIrtbDXUOFor_QDxkPAWiKzMtlXl7ZBMvI-toEGCpIRkFly8sGFSC4h0603k5dndwdG67L0UL1q0dBIIzmJwpqWH4TEJ3vwlkXl_b6fLcJ1Y12wiLqPQC_TL2W3AwST4kfh63lDcODnhZmCGaIn5N0Ed4kKWAPmHW4ISXfhC6y77mPTTsUygGulHQOZ4C0s74rdAzpXGNbWVWDbnrrGU8VWvcO4ZJ5kyGzoc-_Pi8nkJ8joXuHL8xHCd3lfqv7dLunZYBlSs9ySbd8p7aRr8GkG-kOG_2eBych6jetK2tmLTZRFpk1YYMpFAyPzJ99gN4lSVELRgVH0hnlYV7RWaE2FJIUCawRJaVF5W5zBicSMN7CVeQnqNJdBrmL9Ca4_Y3wfxl2Mh-RjkaFRcEMTkF2rV5ASU7O2OY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام مقامات یمن به پیکر رهبر شهید انقلاب
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/akhbarefori/665812" target="_blank">📅 09:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665811">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1fc62f1ca.mp4?token=hLc8TpQDZFhs2h1bMQTHcXdL2LgKOLwCt9pvqzaf8ixJgxk1KTXfO2vJB5e3oguhHS_w-YUa6y2QWg-TAZjs3RK37ub3S2E1I92KP2NU_LLVVNgGRKrmfmQMKADmWx0Kso9h1E9BlQSTKG-uk5uCFfo3I_DceiZlqRTuoT9Cjfh0k8soLGKtk8V5Vp3bQrsiPM5v4spXG_zS7HYI9gPkDklfw5LRRZ5IU0JCD1pGIKX1U1WXvSvFAUEromHKmmA0r1kqcKq_PhRFy8l-9VG0WMYaBJOHA8FI2O2Bqe8b5uyrBqkvf1N5mfj9GbWNKBVeky8RsgtKIaK1XEWyd8TzuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1fc62f1ca.mp4?token=hLc8TpQDZFhs2h1bMQTHcXdL2LgKOLwCt9pvqzaf8ixJgxk1KTXfO2vJB5e3oguhHS_w-YUa6y2QWg-TAZjs3RK37ub3S2E1I92KP2NU_LLVVNgGRKrmfmQMKADmWx0Kso9h1E9BlQSTKG-uk5uCFfo3I_DceiZlqRTuoT9Cjfh0k8soLGKtk8V5Vp3bQrsiPM5v4spXG_zS7HYI9gPkDklfw5LRRZ5IU0JCD1pGIKX1U1WXvSvFAUEromHKmmA0r1kqcKq_PhRFy8l-9VG0WMYaBJOHA8FI2O2Bqe8b5uyrBqkvf1N5mfj9GbWNKBVeky8RsgtKIaK1XEWyd8TzuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سال‌ها آرزوی شهادت؛ سرانجام اجابت شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/akhbarefori/665811" target="_blank">📅 09:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665810">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9688fa726.mp4?token=ZnjS5hhC6HXQaaF2uLqTj-rD5nx28Jhn69AevMgRmd4gOw4eATp5BQ8l2horA8mbTCvRnbvN407KxBVlR_4EUqVhV9q7XJMlzgz3qYWxg8_iaTn5qdKCF9YDY2Bct3K4ybrS8vomr3yBVYJCEVcTwyVNlnCQygcZ9ecLSx2yrIVn3a2aoYdCo7VShyF6Ja8vlN28JL-t-HVeRSx1j5t1rn6-XxJpWp6jBXNQAq0_jXT_OGQ-lBohKJ6Rh00JVf2B3qJaqSIPiWMJtFCm6MbzGCwASBAEYHppaPbx63CeGm8n1_AbiioyTNZ6iFTS6qg71JCLeS3ZhXt4HyY92zd4aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9688fa726.mp4?token=ZnjS5hhC6HXQaaF2uLqTj-rD5nx28Jhn69AevMgRmd4gOw4eATp5BQ8l2horA8mbTCvRnbvN407KxBVlR_4EUqVhV9q7XJMlzgz3qYWxg8_iaTn5qdKCF9YDY2Bct3K4ybrS8vomr3yBVYJCEVcTwyVNlnCQygcZ9ecLSx2yrIVn3a2aoYdCo7VShyF6Ja8vlN28JL-t-HVeRSx1j5t1rn6-XxJpWp6jBXNQAq0_jXT_OGQ-lBohKJ6Rh00JVf2B3qJaqSIPiWMJtFCm6MbzGCwASBAEYHppaPbx63CeGm8n1_AbiioyTNZ6iFTS6qg71JCLeS3ZhXt4HyY92zd4aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام شخصیت‌های مجاهد حشدالشعبی عراق به پیکر قائد شهید امت
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/akhbarefori/665810" target="_blank">📅 09:12 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665807">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GnqbF_aDhtkHrAA4dINB4nTKCP-16p7xf6DeabwhHF0lmt6cO0SaBYqYadCHFrPnkL9oDY5yROSxjn5DTyL1hU7sRL_APdKgu6TVYm59709EbeXRnRWP2GWgKTsDlMqrPIUoe7uqvqBJ12sBise3AqzokT-0esQly4BbK-68CuLThiOk_t5_eAqE5tTcfMrIVp5umtP8EHjyLo1_hVc5IIZdxUYcEyz-ujzpTrVYCrLMKCEV2H0Wzpw_CRcHD975jMQ4qG8OVS4W4SRiQtuNVigHr2xNCPTVGsn83Eax4dxY38Kamix0IdZ_mMh332uAkiL2LI0E4z8GnrluCwFG4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tc9OmoV3QoQ5O85uRnHLrR7KJEePSYP9s8fSN32eKDNb6MWMDUZfSrUoFVZliUj4LHsoU4J5p-Pyo64ogNvvzcAbCPQbKz1JGt6pc2le0F61go50Wcv6Nylfo8iHLezBgLuLgQSa4q8eR9mOuRx1UoLtSSuc8QASbMOziJTcTxC1optPWoZQmmEnfSd9U7cHpRJkbD7Kl_j_Az7tXSSyYUZ5vGVVFJVM5GE-mlLfGvwDpoKTVMwXFfY8wwZgwM_ibYzU66N0gOE7VSxrdzDMlrBz14QTcVqII0RQ9FKsWUymQy2YIU_LHDQzU6AIYa6sPt688tn9NMH2obgItz9A8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NcUerNrD-1npkYLoD0KtikvqZyi2zzRn6M9uDc-BISFxAZcWyNb-z09CTuQjXD1jPjisR083RC6jxXRsNRSjqsdQW92BEL5ow4XXW3UOUtSwZ7smsDZWm07ph3gsSFlyFI9gmdf0gxfpYZ-NdBKG3soDQWMnmVsinVywSnr-3fBpkjFp4K1YMnGYEL2aJtnhQVhcZLOTzPDjZvfOSf-CzNheMXjtE6B8AkTx0eRjUrsMdOoHc4Lm90b6Jwz8WacWJIZEFgaE0P2_ZVOru2ss0AegI9a17yeBJ2LyK-6libcwegHbeEEcwLKO4eFbt1Sky1lZ1El7HMyAzLaJ-Qksvw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
دیدار معاون کنگره خلق چین  با قالیباف
🔹
«هه وی» معاون کنگره خلق چین که برای حضور در مراسم تشییع پیکر رهبر شهید انقلاب، به ایران سفر کرده‌ است، امروز (جمعه) با محمدباقر قالیباف دیدار کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/akhbarefori/665807" target="_blank">📅 09:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665806">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7188c59e7c.mp4?token=WfDE7FV7_dyxPZxnx3ZnV0vCXN3n_gAKa2wyL1VfJsXcbPoWu94E7WwKBMJwpxDYHUkeohbBSeZ6B0c6pQawbjJ_CHIksg92F0GXXBAU6cJSTIGUI0swIMJkPkdkkgirniIbwOm4NYSINQRiPzy3i2JEOv135WKG21MZdR0ViMTk1cQjC7RL_8x_kpOKDMFIVxxy290aLUW2Sh96kUZEoXRpCrNTmyPhcT7p5QdBCEipzjCfYscE8HAgec3dQhtIwhK2SQedBH7EOaSD7LZbCRVqZlnTsVrvxBXMLrbkboOWc9m6EhubdYuOh39Qyt0zIRm6eUI6wKqm4XW6KN738w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7188c59e7c.mp4?token=WfDE7FV7_dyxPZxnx3ZnV0vCXN3n_gAKa2wyL1VfJsXcbPoWu94E7WwKBMJwpxDYHUkeohbBSeZ6B0c6pQawbjJ_CHIksg92F0GXXBAU6cJSTIGUI0swIMJkPkdkkgirniIbwOm4NYSINQRiPzy3i2JEOv135WKG21MZdR0ViMTk1cQjC7RL_8x_kpOKDMFIVxxy290aLUW2Sh96kUZEoXRpCrNTmyPhcT7p5QdBCEipzjCfYscE8HAgec3dQhtIwhK2SQedBH7EOaSD7LZbCRVqZlnTsVrvxBXMLrbkboOWc9m6EhubdYuOh39Qyt0zIRm6eUI6wKqm4XW6KN738w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام هیئتی از مجاهدان و شخصیت‌های کتائب حزب‌الله عراق به رهبر شهید
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/665806" target="_blank">📅 08:59 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665805">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
رئیس مجلس عراق و مقامات ترکمنستانی، ارمنستانی و اقلیم کردستان برای وداع با رهبر شهید انقلاب وارد تهران شدند.
🔹
شمار قربانیان زلزله در ونزوئلا به ۲۵۹۵ نفر رسید.
🔹
تداوم محدودیت تردد در جاده چالوس و آزادراه تهران–شمال تا ساعت ۱۲ امروز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/665805" target="_blank">📅 08:51 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665804">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
قالیباف: بند مربوط به لبنان با اصرار ایران در تفاهم‌نامه با آمریکا گنجانده شد
محمدباقر قالیباف، در دیدار با خلیل حمدان، عضو ارشد جنبش امل لبنان، با اشاره به تفاهم‌نامه ایران و آمریکا گفت:
🔹
یکی از مهم‌ترین دغدغه‌های جمهوری اسلامی در این توافق، جبهه مقاومت به‌ویژه لبنان بوده و با اصرار ایران، بندی مربوط به لبنان در متن تفاهم‌نامه گنجانده شده است.
🔹
اجرای این بند می‌تواند به تقویت لبنان و جلوگیری از فتنه‌انگیزی در این کشور کمک کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/665804" target="_blank">📅 08:49 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665803">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
حضور ۸ رئیس دولت و ۱۲ رئیس مجلس در مراسم وداع با رهبر شهید
/
حضور هیات‌های رسمی از اروپای شرقی در مراسم
سخنگوی وزارت امور خارجه:
🔹
نزدیک به ۱۰۰ کشور با هیئت‌های رسمی یا شخصیت‌های مردمی در مراسم وداع با رهبر شهید حضور دارند.
🔹
تاکنون حضور ۸ رئیس دولت، ۱۲ رئیس مجلس و ده‌ها وزیر و مقام ارشد از کشورهای مختلف، از جمله کشورهای همسایه و اروپای شرقی، قطعی شده است. کشورهای اروپایی حامی تجاوز علیه ایران به این مراسم دعوت نشده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/665803" target="_blank">📅 08:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665802">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tsKgTaqwTo1wTqpvBd_XGETgcJpSdM-FkETWfX7dBKV8YmNQsFxqu8Q7qCDuoi_sYVpJl3682vEJYxxHkeZlzzbDoxO_TPZ_XPAF3J7fvkBGF9cKdu8Lv4aKnklLsWMm-U5p7n4rwoC-4H0VTHOu8aSOBfznHMeiAtklG0-1vYfu0Sxp8YuXCgVyQQ2JpVVXG6YT_T1K9QkhyU2cJrs5dRxlHLojrRnuNjGf2okSPt-DM_cfyohogQ1Q_fwcLrZmyr7M8p8nfqQiyqLxN82oS03_tB-eH2X3tOyYrmesBa6J_BJDal97snldiLMFZ8nPJnMcyCqq4SASK0_oN1zJTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نمودار جام جهانی بعد از پایان بازی‌های دیشب و بامداد امروز
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/665802" target="_blank">📅 08:38 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665797">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JNZWiLR3BtFDBiKU6LRIzHGjN7WWksDtXBbLy5cMZz3qV4CxgaT0GLW2bdRpKkCDeRiAjbK1VCRHgUTO0faD_XpciXTd7aONfIWANh4GshIUuJ8Te0qetG8qYknfOz-bIwa8AA1BiletqWDkdyBtYyeLd7CHKxpMbf9CVux2Yh9h6C35gzJMeiZaGEittcv96tM2ntJGJrH5CgHYhmBujcNE5HA2qnG-7014UD1PZXuSCKVLSfJHfYWsCIJUfnA5VXuImZ9XHVOhlxHnJbfOu4DBTZdXe1t-oz2yDiTeTZnDnkJYdI0cLRTuJJtehXCGJbFs91xg9QZJhpknlDCR6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/epX9HGenDRM_y_K8b29g9AQRtqwsXqwGCl3gFZ8HADbS0660hO8w7IcCJ3VdFH4m3KRTGGRVoCpZ0CJwVqA_NQqCqsQouf2dvjsq8boXNfjKLgHf-dW0O3tFrVsIN-X_6lroysTdkiLB9fYVaJULI994uGV99wUduCFhtn6U8PdN57CUbKC-VG3sAFaBqcOAddZveY3z7ltQxzCPU2sRJpwJiCGxZU9X3iFolLOWCVkKDm4tRvxShk3Hc8IPLxoAvwdc_KPnMZm-Ha4PU1z6Wh_-WGUnc7ShtZ6N0E1P4hUkxSAHwcHCu2PFEOMiAcagNogktt-rXYHsiZ1bXHiB5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GFhArc6_cXXl4vr77KR1g_P7nukpEzoNGbWuo8GVZgwABXyQI9a6OBTIWu7YSPK9Q5L5YNPMtQoIUUlFA66-tuTlH9vtNq8gAVwZQqHulYYsGKvTHgTdL6aw-7PZsFMQSDPbi_Dn6X7FZREo4U2RcUEOVwA72Hr19GpnvRbsrizmujPfQWPKq9z-U0B4lpZNrsDQtlWWa2ZgDKBgAXRhgXjm8PB4kvX_C7ZuUfzK3LuL1QXjH7z2narIxipfG8Pvf5ZtfGV8Uy6W72PQ6FpN8HskUx_tcmIlnJ9picAB6rd4URaZF6FPGB4CVOYLuOEd9r6fdWjkF0MQKUFsKiG2rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VVIWWNBilQdDSmhi6Ymo2JfHk6H9iLPR24J1WMKEI7QlzO4UYwsoA695uQWduBWbNtw_wGkr01I9FSyNjc9T3qgAwQhHAPu-JXhCkkHrRl2rLr3QnBH2_lN9hKGTZwnPGTEGPzdB45xX4tYWzTjgmitUh5mZZKM0lMwtYKk8flvINyiZFD-vkAxihmSdz0kA8a-DozVkGRrBclcoiLiH5MdbAuY80zwpNIVo95O3H69Bc8RTyAX6ThziL1V45K7uTIDT0vLLrJE_YlmJwXyd580Eul1Pfdgh3VZOpiCs5ILG8amoMWsaqtnUASotyJz38LoZVa1ThNTYLCu85HHe6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Co2DkgYASiF1lBOiay2HHN6sDOLKU2wuseLC53b5X7Rsm8WE_chjmD0mrgBHQVMl_p2RpRt58Q_gdbwZxAvq013wDOam7P5FRTxAbtrVgL19YSHXMFhmrGXcbco6_HbsABjL72XMPyFUcU_VnpuDJfMaznyGS1Vv2g-4IAJV_7yPHVmXFtm-R7IL1hApfZj2fkStMNuP3cregEL06Sbwi9crsQXzi4b5Hiiseouw6IsDTjF-kiqzRwmwgsh_9EyRa5Zpc_PSH-8nkHgRb5ws07IcPKIl3JuItCXVJcD-gGJMid6Jcyt3QB-IH3B-n2l1C6JNKRyZHXahWBbw5WLHGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حلقه‌های اعمال محدودیت ترافیکی برای مراسم وداع با رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/665797" target="_blank">📅 08:27 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665796">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ddf75733e.mp4?token=DU_Kg9qOEzLmSfNgmM8imjbjLhh7sVAa4vWHwWEqL1B1sVzRzR9XJsCUfa-YfTpx-goHqFklLmJkmMbAeCx0CamxDtTz44zIcSdwlXWcL9PBF1ZhdTEm67orkLlMlCN8U4mjLRPezLJZ-5ZVBoeh7xqKHcMMETRTeenNiWceFT0Jm6EO_dJZ-xzG7dg6wZ4s2i46X35b6fmsFkHf84L1itzgF8NCvuVoxrweNmNiGJ-KYQKS1Fm50DcyK1MDeefdYhjx_OvllZFmdbriN5_QOO4yTriUR9cTxJIocOdG5Vq0pYNR1rMX0ZLOgnonApFc7fO4DAy7_oSEUz8X6qd5QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ddf75733e.mp4?token=DU_Kg9qOEzLmSfNgmM8imjbjLhh7sVAa4vWHwWEqL1B1sVzRzR9XJsCUfa-YfTpx-goHqFklLmJkmMbAeCx0CamxDtTz44zIcSdwlXWcL9PBF1ZhdTEm67orkLlMlCN8U4mjLRPezLJZ-5ZVBoeh7xqKHcMMETRTeenNiWceFT0Jm6EO_dJZ-xzG7dg6wZ4s2i46X35b6fmsFkHf84L1itzgF8NCvuVoxrweNmNiGJ-KYQKS1Fm50DcyK1MDeefdYhjx_OvllZFmdbriN5_QOO4yTriUR9cTxJIocOdG5Vq0pYNR1rMX0ZLOgnonApFc7fO4DAy7_oSEUz8X6qd5QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام هیئت‌هایی از روسیه و چین به قائد شهید امت
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/665796" target="_blank">📅 08:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665795">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/702696af3d.mp4?token=rPjTw8ctNAuB0NdZc0Yh5klj46bohr-ERGc1O41uldstEETgbcOaiEvWkUz_Wjx566LBULix6g8Cj3rqQ0zEh2jNns13YAUC_ddWjcAnDLXSidsp84Bqy8mKSpOBj9P3Sf8II72j4o1SNfEAVaNB993sy3KoMFuseJ4JYqm_D8F8_km1LcLhrZDOCuNMbWZfqVohBarhf9kzXs2CNFz6ROaaryRZHpO46m28fmuM2e8pbDWif9pHrgCHGn0P5wywkf2Z8fWyNBuoQVLja8TmC1waz-pHPrKGULyNGrjjK7RJIYgUdP-sVLggyDGVoSpGZa4V1YPX2zyFI0dwAZWmTg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/702696af3d.mp4?token=rPjTw8ctNAuB0NdZc0Yh5klj46bohr-ERGc1O41uldstEETgbcOaiEvWkUz_Wjx566LBULix6g8Cj3rqQ0zEh2jNns13YAUC_ddWjcAnDLXSidsp84Bqy8mKSpOBj9P3Sf8II72j4o1SNfEAVaNB993sy3KoMFuseJ4JYqm_D8F8_km1LcLhrZDOCuNMbWZfqVohBarhf9kzXs2CNFz6ROaaryRZHpO46m28fmuM2e8pbDWif9pHrgCHGn0P5wywkf2Z8fWyNBuoQVLja8TmC1waz-pHPrKGULyNGrjjK7RJIYgUdP-sVLggyDGVoSpGZa4V1YPX2zyFI0dwAZWmTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایی از پیکر مطهر رهبر شهید انقلاب در مصلی تهران
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/665795" target="_blank">📅 08:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665794">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCUIjaDZHHRlG1sjIr_9-guCee_pzCqnqTSiB1JFy8PhlSmw6YPFhEOQExLJGO2yyfE--fOi0N2dSWQcSjtm19XLscURCk7qvMRuFWTrTRsqKFG4l0meskI7f4YbVuo4tbyppBtBe-OKrQbNGW-ib5lTsA7wIVW863I7JU5y-E1GTId8l_M6oJFvQXNN63HgZAZEyIPV-mhMGv2crtRhNHy0L7zYSYBc7dum_zAwL_MZCzT5rdhWqnd_GKMt_s2sL_wKMP5TInYIYwqXlE56RfWqHWEen8jfuxAuJcEcyNnvz8EP2Dp8_Y0pmokT3qkUIgAwlozXdO9B8SHYXog6Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انتقاد دوباره ترامپ از کمک ناکافی کشورهای ناتو
🔹
ترامپ کودکش بامداد امروز بار دیگر از عدم مشارکت کشورهای عضو سازمان پیمان آتلانتیک شمالی (ناتو) در جنگ تحمیلی علیه جمهوری اسلامی ایران انتقاد کرد.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/665794" target="_blank">📅 08:07 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665793">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ul5RVfKAR9bP_VTSSFjxTAPBzB-RcdCHXjKQlwgsSNDPinYvlCCygE1PjyyoL-hXi-TJFa5piJOVo98vpI80VIgTes1nCAHcrV2EP30SYxQixZ9e47lUGryXyvte1bg5XHTC0XJCkV5ImF7Bmk0FApDTdA4nhCzWdMuxdr0ayx2PxHSRmsRm8ZtOyusi0EPfxBBj-E-GlDRGDpw1TJ42Iu_TEB3BablXZyIgLaNhqs6TisJrwz_y_9twk3mB_MlW-9U1IFuWG7CmyueGdmo2YppLnf59YO2V9nSZxHlIjeurstKmQRoti_TxorPnBB10-FapI6aoSzm4AVUZsQHr7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
قاب ماندگار از پرچم مقدس حرم حضرت اباعبدالله الحسین علیه‌السلام بر روی پیکر مطهر حضرت آیت‌الله العظمی سیدعلی حسینی خامنه‌ای رهبر شهید انقلاب اسلام
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/665793" target="_blank">📅 07:58 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665792">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e2b0644df1.mp4?token=hDwVWaIbAZqMl11WoFklkKW5Ox02ScBEV3vHZtBBRW_86Dp3QNl9DLTZpz9s5x7tF-NxrZ73ghveDvSPHOkSKbiAurxVFjxGOd5ry2T9Zb0Cm-7nUounb9dnrOCWGDqgLwPFcjhllqfkEgjaOxQusPyc9Kw6bobp1YsSkPvdJMWS6F5Nif-G6oULKoanc6cDPp25l7AXJVFZgz_11G5N90kUAxJ0t2krqMpAgIemsrVnjWF_2NrddZwPeSJLo7fh_rEzyIU_8n8vd1cRietBauwTVCnnzrfy6uQ_aTKuSCbcNcI_yFrrxoc3jYyHkUC5fS_kau-ezRFrbuT9tLiBwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e2b0644df1.mp4?token=hDwVWaIbAZqMl11WoFklkKW5Ox02ScBEV3vHZtBBRW_86Dp3QNl9DLTZpz9s5x7tF-NxrZ73ghveDvSPHOkSKbiAurxVFjxGOd5ry2T9Zb0Cm-7nUounb9dnrOCWGDqgLwPFcjhllqfkEgjaOxQusPyc9Kw6bobp1YsSkPvdJMWS6F5Nif-G6oULKoanc6cDPp25l7AXJVFZgz_11G5N90kUAxJ0t2krqMpAgIemsrVnjWF_2NrddZwPeSJLo7fh_rEzyIU_8n8vd1cRietBauwTVCnnzrfy6uQ_aTKuSCbcNcI_yFrrxoc3jYyHkUC5fS_kau-ezRFrbuT9tLiBwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام هیئت فرهیختگان و فعالان فرهنگی رسانه‌ای از کشورهای اسپانیا، برزیل، آرژانتین، کلمبیا، اکوادور، بولیوی، نیکاراگوئه و افغانستان به پیکر رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/665792" target="_blank">📅 07:46 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665791">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67ad31c42c.mp4?token=bGSOWqydlBor8N70xu2orNIoYd6PDWc91ObMBOtAsVkN8SYyINxS5PGYcy3giUHerDirvjYNVB1SYln4x2Nj-vdkZk4lp9kN1JrSJBTJx-7hyWt20Hc_T_7bR7OWJz3QCQ2XGYtmRqOIfGfyC2dNQ4uxb-VJpCZ626r3JybY6YoLH0NeyGeStaRDIk1tCSLnkhvkbUYPD7l_beGot2XxceIR0vA7HYOqNzOktTs6uOc12thaPz_Y4qal3l3byXioEtitkbYsggFqe3oIehuP0Gd5RDgmU79E4RXUwll0n3efBg5izbYUm_Q7lfAJeJ6IvkU-xlETgSiQvUmCma3RZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67ad31c42c.mp4?token=bGSOWqydlBor8N70xu2orNIoYd6PDWc91ObMBOtAsVkN8SYyINxS5PGYcy3giUHerDirvjYNVB1SYln4x2Nj-vdkZk4lp9kN1JrSJBTJx-7hyWt20Hc_T_7bR7OWJz3QCQ2XGYtmRqOIfGfyC2dNQ4uxb-VJpCZ626r3JybY6YoLH0NeyGeStaRDIk1tCSLnkhvkbUYPD7l_beGot2XxceIR0vA7HYOqNzOktTs6uOc12thaPz_Y4qal3l3byXioEtitkbYsggFqe3oIehuP0Gd5RDgmU79E4RXUwll0n3efBg5izbYUm_Q7lfAJeJ6IvkU-xlETgSiQvUmCma3RZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ورود پیکر مطهر شهیده «زهرا محمدی گلپایگانی» نوه ۳ ساله رهبر شهید انقلاب به مصلی تهران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/665791" target="_blank">📅 07:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665790">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b127043fb0.mp4?token=GcMVSFN1B_A-n5naNPUSOvPVqUKqgJ7SgiIwA5k08W-BwRd-3G6BNLpAIaZi9U3yZFMqoqHm9g_S1FYGZ1Ac9PVShR6_gY4BRyAl7WQ7tQjVvZRoER3Rl_l5q6sHsEiIquwRonvifh_40rddrevlXr5ntRouOL9pSixE4PcAKR1UdThUj6qr9qqxr2ZGmK6zd6RCePXFbGZcWI0yA4ookJTFlpsFnWk8Z7sDw9Tgcbbxqm751GOakzH91TAU_5v6x6l42WtI1P1eRNjwqj8i0zT0bAKdeoxqRuIuZV33Ziywt0j57VaK39DvcIE5Aet7gM6tU3o9GxtlBqGfiWufIhoRzL1oR2_lyCLdjklRpXiqUnfW_Z--Touepx92saz5Kx12PIj7QhdG_3u1vY91SGDKGdqZbRdPTmmo7BmdIH99slXa25nPnevyQi48-jf3KTEmFsS3MyO2EU1NJj2mXpLSN4xi3D7xX1nSiNWXGF6WN63B7uzbr3k-Ijrk8nAK2z1hsVfyJYgP3vMxA1CUz2oWP1yCMfMrOyHXlgBiYHatH19nODyPd9pu5ef8hILRdvog6esPmZJAkkteegz7JN1i_opjX10dxwElN4AkH1Fp2BN9r_GZmZBHjFSUURsIboP8jG8WUchJdDzzuh-QqbOQn13qJJvvnnug7WJpIhc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b127043fb0.mp4?token=GcMVSFN1B_A-n5naNPUSOvPVqUKqgJ7SgiIwA5k08W-BwRd-3G6BNLpAIaZi9U3yZFMqoqHm9g_S1FYGZ1Ac9PVShR6_gY4BRyAl7WQ7tQjVvZRoER3Rl_l5q6sHsEiIquwRonvifh_40rddrevlXr5ntRouOL9pSixE4PcAKR1UdThUj6qr9qqxr2ZGmK6zd6RCePXFbGZcWI0yA4ookJTFlpsFnWk8Z7sDw9Tgcbbxqm751GOakzH91TAU_5v6x6l42WtI1P1eRNjwqj8i0zT0bAKdeoxqRuIuZV33Ziywt0j57VaK39DvcIE5Aet7gM6tU3o9GxtlBqGfiWufIhoRzL1oR2_lyCLdjklRpXiqUnfW_Z--Touepx92saz5Kx12PIj7QhdG_3u1vY91SGDKGdqZbRdPTmmo7BmdIH99slXa25nPnevyQi48-jf3KTEmFsS3MyO2EU1NJj2mXpLSN4xi3D7xX1nSiNWXGF6WN63B7uzbr3k-Ijrk8nAK2z1hsVfyJYgP3vMxA1CUz2oWP1yCMfMrOyHXlgBiYHatH19nODyPd9pu5ef8hILRdvog6esPmZJAkkteegz7JN1i_opjX10dxwElN4AkH1Fp2BN9r_GZmZBHjFSUURsIboP8jG8WUchJdDzzuh-QqbOQn13qJJvvnnug7WJpIhc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آغاز مراسم ادای احترام شخصیت‌های خارجی به آقای شهید ایران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/665790" target="_blank">📅 07:43 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665789">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s1K-a4r2eaAfQiF-zg9Qbt4FX5eSVC8pY_-ctwlR0P71U8TjSJOT7iK8GyKMjRunsmaktIZ5MT6149UNxxsZNEnNZoiPlR02nc-FV3O6P3KG4OYi7yXUrd_LQ6tQEmHFN1m2eYZySobrdVek5DtMM7qYPNFMpwPAI6Og6gwlpXy2_mdUO85R8quaHKrJBbkk8-XacojkyMykVRq8-727gwfamaWQEhTNXOLRakY0_js2F0ZJGUeggKs1otOxGWSu5gye0_tj51VlctvamjbNqnHC4Ngw4uGDWVUEofhxb7eH48FcOGgdVpvKpTI4qPZARXV804JK_pOtyirtC7D23A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز جمعه
۱۲ تیر ماه
۱۸ محرم ۱۴۴۸
۳ جولای ۲۰۲۶
جمعه‌ها
#دعای_ندبه
بخوانیم
⬅️
متن و صوت دعای ندبه
@AkhbareFori</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/665789" target="_blank">📅 07:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665788">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FvheAHAc30ZSndG-jwv2to63jcucdC46pQQjLirxzZlNBkMHebqGuNsHOSkb7ngTIURBaxWFQ_FQ_5rDCUvwYtetMcjiJDBVkA1mt-DVGN2cAi16E4ie1RzX_yiKYW9idLu3D2MedgAq8tvTyai9NiovoDI4atJAwhbsRKAmj45Ie_io9KKllMXk-yOv6qqXOzkXsvja2LWwvm27A3k1-vYJjlSaCBMb2oljAIBAH0bsbpvpzVTdYwtOBeqNnfzuWwOLx1bOVpGpWpRpA9jODmeHMhTmav-enYlIJeWWfRrdE_QSRaCodjhCmU_szySdYuj_2fiGpRJZd33D4ebDUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
سرمایه‌های کوچک، پروژه‌های بزرگ
هر پروژه بزرگ، از کنار هم قرار گرفتن قدم‌های کوچک آغاز می‌شود؛ کرادفاندینگ فرصتی برای مشارکت در طرح‌های سرمایه‌گذاری منتخب است.
🔰
شروع با سرمایه‌های خرد
🔰
مشارکت در فرصت‌های سرمایه‌گذاری
🔰
انتخاب آگاهانه با کارینکس
👈
برای دریافت اطلاعات بیشتر کلیک کنید
📄
#کرادفاندینگ
#سرمایه_گذاری
#کارینکس
💎
با ما همراه باشید
کانال فرصت‌ها
|
لینکدین
|
تلگرام
|
وبسایت</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/665788" target="_blank">📅 02:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665787">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LCAkCwB-uaJZ__BlqhhF-xxyB5d-UtBvKUht-VuhDTMOolfvOWKNTuTowxKTqMA0xfLzkB_Jg6uwj8ig1iBEBGtDvfL4_NJqCawUwXCf-3GFevdlR7H2BxAZMvROmpBoXlKsFMsbHQO2TJkMVjLL8ou1T9hkU1ZP7iJHH24HvgKhkRLnq2yuwqFyUfhWmdjiNEqElsQmJpnh6CZQPuBU2gkTqO3peS3wNkglg7HFZm8m3IMFrHihhkLomPN_nqZzNVmPga_eDYdRraT_CV884WUOa-VhtoNPNS2rD56OveiNZF60QdYPuw7o2_1mNqS1HLKwRjB1b2FH5Dp2Oy4llg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
انقلابی در صنعت هوش مصنوعی
🔥
🔥
🔥
🔴
میدونی هوش مصنوعی ترند دنیاست و اینده ی اقتصاده ولی بلد نیستی ازش استفاده کنی؟
🔴
تریدری ولی همش استرس اینو داری ضرر کنی؟
🔴
یا کلا ترید بلد نیستی ولی میخوای سود دلاری داشته باشی؟
هوش مصنوعی TimeTrade این مشکلاتو حل کرده
✅
هرکسی با هرمقدار علمو دانشی میتونه ازین هوش مصنوعی استفاده کنه و به صورت live و روزانه درامد دلاری داشته باشه
🔥
👇
https://t.me/+hcwmoHXpF6k5Y2Q0</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/665787" target="_blank">📅 02:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665786">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U4VNXjqivyRyijTDumWMyzHTWD7S4bWHij8y1R7vgWA28BVTRz9kJ6ByTQtNPIl24cME9us66-ebC5YIBFwqxgNEMOpVBIKssWmiaC_jDMm6NcfOwc7ZZ6_zRmxDWug50OGlb0gDnG7yYUAY60G1UQ0WysQAKaGb9t-qOLJKUtJUhBDgM46bVAGPkY6A49WVCkhY3bzBAM4VuG2gQhL4o8EjfAl7qxMTy97wVN-QNAvOIBQMjq5ykSY_bPYk6Eqsn2UTfWINbT9oMIRSj1JAwqKqO7bwg42FMiEXYavgxA1lX-mO09KPP8NZn_Jf_qB_2eYT4kj9E5l1PWk9t6BtGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙️
بسیاری از کسب‌وکارها مشکل محصول ندارند.
مشکل این است که صدایشان به افرادی که باید بشنوند، نمی‌رسد.
بهترین خدمات، زمانی ارزش واقعی پیدا می‌کنند که دیده شوند.
محتوا شروع مسیر است،
اما دیده شدن، مقصد آن است.
دست رسی به گسترده ترین شبکه انتشار کشوری(کلیک کنید)
#DigitalCast
#MediaAgency
مشاوره و تحلیل رایگان
👇
@marketing_mn</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/665786" target="_blank">📅 02:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665785">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec6ffec7cf.mp4?token=eijocKIwnfCjvnPCzMzdOLTp0hHeHdmD3tAOnKwKcSpH5n-_0duu3gVQfqLgcP7pDcRwdqVtyoZfU86VMafovLOb3flqHHOK6DVrAHuT95la27NSZ6TF0nfQqvmG044vgm_p-OmJuzcCxz1nGQ8uU7586fAITkxF99trrgwRXwZn6FRmSt0o9MqvOtXGqB-BP7kkg313CT5_Qqm5LXxoYhH_CsXZw6MpGhlOTH28DQxTjEuuMf8GCfORKF5E2YEOlmaXAPupYs_G7yce0X7e67Qrng7iYmAi18ZE0_oqCxCEtDeOd4BQf-AGemKQL0kK6Ppvahm_PNa_Ru0JkQSdTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec6ffec7cf.mp4?token=eijocKIwnfCjvnPCzMzdOLTp0hHeHdmD3tAOnKwKcSpH5n-_0duu3gVQfqLgcP7pDcRwdqVtyoZfU86VMafovLOb3flqHHOK6DVrAHuT95la27NSZ6TF0nfQqvmG044vgm_p-OmJuzcCxz1nGQ8uU7586fAITkxF99trrgwRXwZn6FRmSt0o9MqvOtXGqB-BP7kkg313CT5_Qqm5LXxoYhH_CsXZw6MpGhlOTH28DQxTjEuuMf8GCfORKF5E2YEOlmaXAPupYs_G7yce0X7e67Qrng7iYmAi18ZE0_oqCxCEtDeOd4BQf-AGemKQL0kK6Ppvahm_PNa_Ru0JkQSdTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترک اعتیاد (مواد و سیگار) در ۵ روز
🏆
🟢
بدون بازگشت
🟢
بدون بستری شدن
🟢
بدون درد و خماری
🟢
بدون عوارض و وابستگی
یک بار اقدام کن تو پاکی بمون
✅
جهت مشاوره رایگان، پیام بدید
👇
☎️
09388403141
☎️
09388403141
لینک دریافت اطلاعات شما برای مشاوره
👇
https://survey.porsline.ir/s/uic3tg60
https://survey.porsline.ir/s/uic3tg60
لینک کانال ما در ایتا
👇
https://eitaa.com/joinchat/3149399356C76d980ac27</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/665785" target="_blank">📅 02:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665784">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16002524fe.mp4?token=PSLJj9SGj0kRxf4AB95c2f-FwzY2ThdoKns6mxSJWZR38E9X5w6ChsRJkCVHSAzrAfvDbNqeqsRddnd6PVJDuhzujxISiOFGSrvP5iMevl8fjPod2dbLyABw82lHMSy7em3s1_lgZZDbTE0Y0eGGvDKBg9SAnhAE-U3sQh3ozySUBujPEY59Swj-kBEtsFFpfZia2f5NLluztycp1WxP_VDim__JAmeXCr5C9WVKaT8BOQ5f1EbzRu349KPgiNtoshUQbMLSjuz0kHNuZ1vsWGOQ66CuFIOGtUGDz8vMGZLgFSnzjlsVt61mUt63d-xJOBd4HRDbtVfeYnA507hw4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16002524fe.mp4?token=PSLJj9SGj0kRxf4AB95c2f-FwzY2ThdoKns6mxSJWZR38E9X5w6ChsRJkCVHSAzrAfvDbNqeqsRddnd6PVJDuhzujxISiOFGSrvP5iMevl8fjPod2dbLyABw82lHMSy7em3s1_lgZZDbTE0Y0eGGvDKBg9SAnhAE-U3sQh3ozySUBujPEY59Swj-kBEtsFFpfZia2f5NLluztycp1WxP_VDim__JAmeXCr5C9WVKaT8BOQ5f1EbzRu349KPgiNtoshUQbMLSjuz0kHNuZ1vsWGOQ66CuFIOGtUGDz8vMGZLgFSnzjlsVt61mUt63d-xJOBd4HRDbtVfeYnA507hw4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله هوایی جنگنده‌های صهیونیستی به جنوب لبنان
🔹
منابع خبری از حمله هوایی جنگنده‌های صهیونیستی به شهرک صدیقین در جنوب لبنان گزارش دادند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/665784" target="_blank">📅 01:58 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665783">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
لحظاتی از وداع مردم با پیکر امام شهید انقلاب در جوار حسینیه امام خمینی(ره)
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/665783" target="_blank">📅 01:58 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665782">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
ادعای ترامپ: ما موفق شدیم ۲۲ نفتکش غول‌پیکر را در یک شب، تحت محافظت شدید و با سکوت رادیویی کامل، خارج کنیم  رئیس‌جمهور آمریکا: امریکا هفتۀ گذشته سیستم راداری جدید ایران را از کار انداخته و تهران در حال حاضر فاقد شبکۀ راداری است./ خبرفوری #Devil
📲
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/665782" target="_blank">📅 01:49 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665781">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
ادعای ترامپ: به دنبال تغییر رژیم در ایران نیستم، بلکه هدفم جلوگیری از دستیابی این کشور به سلاح هسته‌ای است/ خبرفوری  #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/665781" target="_blank">📅 01:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665780">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
باید تقاص پس بدهند آن حرامیان
ننگ بر ما اگر از خونت گذر کنیم
🔹
مراسم وداع با پیکر امام شهید انقلاب در جوار حسینیۀ امام خمینی(ره)
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/665780" target="_blank">📅 01:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665779">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mw8XQrvSwRz1kocCZK1u-im6EsZmX5ts8lmHJoeVtkDXBmTP23y5KC3Sr4Lsa-xC_d__Qic2_bBWAq6UXtmwPdvKOfj_x6P8EVZ12Z3Z5ReXZGC9kf9t5kAPUe6WZcmg6p7dBTjlC4udp4TpG-60R9gvUz7ZmRPZWvPjnIOmAQ2LKi9LuEnJGnLxYuufO97757tyf0fyVwtdGFpoyzVjGmC1zE6F2Jpvr9Ld1_YZ802YKGSkn4fG_CRfJznfcsMKkyMD5j1lby3pFfQq6dQvM-V5Avyue8_mnAXtERpBNx0gA93YJb-k2MS4UjD1jA4v6kNMCV8v_hM3POm0W-aXDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس‌جمهور: شهادت رهبر عظیم‌الشأن ایران، اندوهی عمیق بر دل آحاد ملت ما، امت اسلامی و همه آزادگان جهان نشاند
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/665779" target="_blank">📅 01:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665778">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
ادعای ترامپ: به دنبال تغییر رژیم در ایران نیستم، بلکه هدفم جلوگیری از دستیابی این کشور به سلاح هسته‌ای است/ خبرفوری
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/665778" target="_blank">📅 01:27 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665777">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e79ff51089.mp4?token=JXVryjrhzRQbnmbc2cqDJ_l0OdbONzq6M1Y7slmJK5bfYF9pNWzSobykM3O6tRM4PlDWBojYxNG1y2hkvRypEzdZwEGzP-o_d91RsVKFjLhu8V0ob1etIZieG6ycudi3OW4cZVUoB5GuhqCs1jlGX4iXaybHDOkTYMhpyY_o64pn9-H0NE962HwIG6tp4T4UYGzv1yxLLxI32vS3CTfgGkbBipbVQzh8pERdJRDLeKTbCpzvlSD8Vr9CSgg-Y1ddG1w1DnqwI1Xk_jZpUjvOdjOlN_kilrgDujvrOLIYTqqpMrH-lBdBKw39hiQKXJvEtE8qTw0_nsNrqtcPklrYsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e79ff51089.mp4?token=JXVryjrhzRQbnmbc2cqDJ_l0OdbONzq6M1Y7slmJK5bfYF9pNWzSobykM3O6tRM4PlDWBojYxNG1y2hkvRypEzdZwEGzP-o_d91RsVKFjLhu8V0ob1etIZieG6ycudi3OW4cZVUoB5GuhqCs1jlGX4iXaybHDOkTYMhpyY_o64pn9-H0NE962HwIG6tp4T4UYGzv1yxLLxI32vS3CTfgGkbBipbVQzh8pERdJRDLeKTbCpzvlSD8Vr9CSgg-Y1ddG1w1DnqwI1Xk_jZpUjvOdjOlN_kilrgDujvrOLIYTqqpMrH-lBdBKw39hiQKXJvEtE8qTw0_nsNrqtcPklrYsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای مضحک ترامپ متوهم: ایران را نظامی شکست دادیم/ خبرفوری
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/665777" target="_blank">📅 01:22 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665776">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
ترامپ متوهم: تقابل با ایران، عملیات خلع سلاح است نه جنگ
دونالد ترامپ در گفتگو با شبکه CNBC:
🔹
تقابل با ایران را نه جنگ، بلکه عملیاتی برای خلع سلاح هسته‌ای توصیف کرد؛ وی با تأکید بر اینکه دستیابی ایران به سلاح هسته‌ای غیرممکن است، گفت ۴ ماه است که هدایت تلاش‌ها برای خلع سلاح این کشور را بر عهده دارد./ خبرفوری
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/665776" target="_blank">📅 01:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665775">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcbe1af175.mp4?token=ZcLNJCaqsmpAwPNZjzBdINqkkaRmw8l2MtlEGexACiQ26m3OdVy8umPwC3Iasw1kZgWa1Y0thXVWHmvCBg2AB_HxqXBgh5hZz2BgztDtlvC18ywKUQdW2KlBvHJ-jMWI78XvbIPU2UeTflH8iBTGXA9W8kPRICpOSqhCypwS3TFiO2owdHndRx2kCmKTf4f9D5fRFVCBd-zI6J9diPnupQPp7YjF0KK2FaHu_EUZMtVy4ktIqEKW_TLvHgoFsIiRwJV09EQZkx1Q_t2fmOOYypRpvlGVm-RFeRZdCTO2tNDowD5A_U7r4OHR-XMbdz42TTwfR3fDvh713uZ4TnKkOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcbe1af175.mp4?token=ZcLNJCaqsmpAwPNZjzBdINqkkaRmw8l2MtlEGexACiQ26m3OdVy8umPwC3Iasw1kZgWa1Y0thXVWHmvCBg2AB_HxqXBgh5hZz2BgztDtlvC18ywKUQdW2KlBvHJ-jMWI78XvbIPU2UeTflH8iBTGXA9W8kPRICpOSqhCypwS3TFiO2owdHndRx2kCmKTf4f9D5fRFVCBd-zI6J9diPnupQPp7YjF0KK2FaHu_EUZMtVy4ktIqEKW_TLvHgoFsIiRwJV09EQZkx1Q_t2fmOOYypRpvlGVm-RFeRZdCTO2tNDowD5A_U7r4OHR-XMbdz42TTwfR3fDvh713uZ4TnKkOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ قمارباز: برای جلوگیری از سلطه چین و دیگر رقبا، آمریکا باید در بازار رمزارزها پیشتاز باشد
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/665775" target="_blank">📅 01:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665774">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ox51ZfYaA2NuSNnIpax09cqdQxfkv1t6Y-1fatR7h7jt-sYlmo5ZmNzhfAjJCzrTezbtpmMcjE5Cw2hhHcI-RNcAWO0a7OWggGTaMVlJ7eLsQ5RzyJkDm4bpRKn4SmtC-2M8dQ7B-mJ1t3NbWz2gX2hnTEh3QQ9xKt1ZiM8cN9M36tx59v6ZDuyh17EZmQK6m8z-L1xQjntx3vjTPHkoPFKpgdZeTYCI69WJbyC09lMuLwsb8lL2Uovcadya3cxY5-XqxBil4srz3dTk9rTw4IM_WjCFKks78JJaMhVQ3UmgHeUf3X9wq-KxDb4avb622hYmR2SenFILqzqfGzBNsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یحیی ابوزکریا: آیت‌الله خامنه‌ای میراث‌دار عزت و مقاومت مسلمانان بود
🔹
این متفکر الجزایری، آیت‌الله خامنه‌ای را رهبری کم‌نظیر در تاریخ معاصر خواند که با وقف عمر خود برای اسلام، راه عزت و مقابله با ظلم جهانی را به عنوان میراثی جاودان برای مسلمانان به یادگار گذاشت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/665774" target="_blank">📅 01:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665773">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
هتل‌های تهران هفته آینده نیم‌بها می‌شوند  جامعه هتل‌داران تهران:
🔹
تمامی هتل‌ها و مراکز اقامتی استان از جمعه تا پایان سه‌شنبه با تخفیف ۵۰ درصدی، برای اسکان زائران و شرکت‌کنندگان در مراسم تشییع آماده خدمات‌رسانی هستند. #بدرقه_یار   #اخبار_تهران در فضای مجازی
👇
…</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/665773" target="_blank">📅 01:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665772">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngedKiNnm-fLLzDGuiovh1gLii6BEmCAU8xNARPGLnW78Ih7sadDt0L6vD14EvhGkKIAUf78O5CpgMFgXH8nMtKENPSNiJUNEfRWXEnNtKfnborQY0gpUeLXokz756dOgfRPMjpJAWNMXpsmcaRHAy7fNS0TRQrQ5RSc8nQm_8OLr-Fn0GTfZcHE5ACzK04aC3agkX_0sdM2d2FTiKksoPdMhzbeUUa2rc_sxWP5W9dHfOryNv796nulmOTEABPhLx-fuw39woPzgNGoi7GdiRaxRatKVPN3VlbE27vMVFLPp-2rsdD2QPG3aOIZQC67EQdyBHVYT85aHmYlGV2j8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمله قایق‌های جنگی اسرائیل به سواحل غزه
🔹
منابع فلسطینی از آغاز موج جدیدی از حملات دریایی و گلوله‌باران گسترده سواحل شهر غزه توسط قایق‌های جنگی اسرائیل خبر دادند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/665772" target="_blank">📅 00:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665771">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
انفجار در یک کافه در دمشق
🔹
رسانه‌ها از وقوع انفجار در یک کافه در دمشق پایتخت سوریه خبر دادند. بنابر اعلام رسانه‌های عربی بر اثر این انفجار ۴ نفر کشته و ۱۰ نفر زخمی شدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/665771" target="_blank">📅 00:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665770">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/397157b218.mp4?token=PvyZ_U5UQGGHuEPg4o4eIGbHpV_Owi6tcioWH91KS418MxDUO6O8gWZm2O7rvm3tj-8DRp4QnF1I-Y8AUfC_ze5YHVB7bOAUUzdimY1SeyllphvAPwwgrcAAzTmJWPttXEMPxU63VYcl0jHxAAHCNywI7f7UYVSpjqLuuNeXlm3T8AH94MVHi1ZcbLWUphjlR_m24rE1RzW8Nx810zBedWR7kPF6aMOrK8IhetLHdhVV7S__0um0Fk9Cx7zuTDxdP_0tc1rexKgpHGCaOgx24uAuP_Qcc-7bEKtTMUQMXZSJaxgX1rDaAvXG2qU2pdRTaL7oVyZF6UdoZmzeKNdw9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/397157b218.mp4?token=PvyZ_U5UQGGHuEPg4o4eIGbHpV_Owi6tcioWH91KS418MxDUO6O8gWZm2O7rvm3tj-8DRp4QnF1I-Y8AUfC_ze5YHVB7bOAUUzdimY1SeyllphvAPwwgrcAAzTmJWPttXEMPxU63VYcl0jHxAAHCNywI7f7UYVSpjqLuuNeXlm3T8AH94MVHi1ZcbLWUphjlR_m24rE1RzW8Nx810zBedWR7kPF6aMOrK8IhetLHdhVV7S__0um0Fk9Cx7zuTDxdP_0tc1rexKgpHGCaOgx24uAuP_Qcc-7bEKtTMUQMXZSJaxgX1rDaAvXG2qU2pdRTaL7oVyZF6UdoZmzeKNdw9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
درگیری‌ مسلحانه در السویداء سوریه
🔹
منابع خبری از وقوع درگیری‌های سنگین میان شبه‌نظامیان دروز و نیروهای امنیتی حکومت جولانی در شهر السویداء در جنوب سوریه خبر دادند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/665770" target="_blank">📅 00:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665769">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQsnzImZFJ8u2fqWDLKZPstzOiFsNijRjoJu276sUjc0gq-nvWtRlOC2rnkUrQbmsxluV0fuiQx9qK4xVf4WfO8uqt1k1UA8kV7y19hQ6P5601AKND0otLtg15s_9cM6Ry7NWWxKF30kX1u6EJ_QLnzXNYERNvNlR440u78UNSJ8d1z8kBUuyopfDE__HrcKZTbAtksFCNRWL2x3UBhIgkLa5ZMji6qJFjthg0r-a0Hcpf2wBVRO2De-De_g0xEp79jsOnQSAJTfU9w4hElp0A10qXn_Jw0q8TcrKUlUbasOb94mcYsKxRWegF4rTygrw4v0N57qjfIotIndpUbaJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
غریب‌آبادی: شهادت رهبر انقلاب، نماد تداوم دشمنی آمریکا و ایستادگی ملت ایران است
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/665769" target="_blank">📅 00:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665768">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kdbTqIektWvdOlDdppdspVsFAmDto0HjLJhnJj58th7WwA3-Iu5hmiB9NmRv7CWkGd5wP85pRZPnCpNSsehWtq-C7YzUea0GKQodT_l1nS-ItBBIqPydsSP6z1IKdzdTKqdMZrwrb6NUml13kXmjEY_DUKSoLAMAblA6sPZHAFK40tPi6gcpl3As7CLu9p4nxYaT5Fyd1C4-NaQfdaO1poS4EPYmYwGWfVyfHAWlHi9qPleRljwGx2tzzV95VVZcYUpHXOXo-8TbCQ7OFitTmqDeiLwTsaQjIdFcrXXQ_UW6sMcjYCqSmrKfPwbxR5rJA9nJmrM51JDNWbAMFl2NUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مسدودسازی حساب افشاگر معاملات مالی ترامپ در ایکس
🔹
ایکس حساب افشاگر سبد سرمایه‌گذاری ترامپ را تنها ۲۴ ساعت پس از فعالیت و جذب ۸۰ هزار دنبال‌کننده، بدون توضیح مسدود کرد.
🔹
این صفحه جزئیات گزارش مالی ۲۰۲۵ ترامپ، شامل درآمد ۲.۲ میلیارد دلاری (از جمله کسب ۱ میلیارد دلار از رمزارزها) را منتشر کرده بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/665768" target="_blank">📅 00:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665767">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f53a3d8358.mp4?token=ZTUW0zzrFHy2mHLog7S49kBAljgrrseP6orLTKc4s0wCjo8egbrjvs3DsQnWXfT83sl_b_06GOd4bSFOAraizJz2DJotrUkvj1B4DaC-mOaDINWAGcJ53N6CAvh-DbzTEH_WFI6rEgoRxwfP0X-_pYN5pCmY8aHor0jEOqphVYWViAM8bZJS_MAIH1A__t9ApocKpXSh7CXSCfnIQLm0rqzfnzHueZ5rBfmh7el1ooUmwbKiNxkWr5kv_rVJKuGxwV7_hRnHQlljYPX3qziPFm_HfDNX3RLVvHKqvSaP6nslH-d4_Q1ov45QoMm0j1-D4kXIJGfbyY9o0B1ARlvPkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f53a3d8358.mp4?token=ZTUW0zzrFHy2mHLog7S49kBAljgrrseP6orLTKc4s0wCjo8egbrjvs3DsQnWXfT83sl_b_06GOd4bSFOAraizJz2DJotrUkvj1B4DaC-mOaDINWAGcJ53N6CAvh-DbzTEH_WFI6rEgoRxwfP0X-_pYN5pCmY8aHor0jEOqphVYWViAM8bZJS_MAIH1A__t9ApocKpXSh7CXSCfnIQLm0rqzfnzHueZ5rBfmh7el1ooUmwbKiNxkWr5kv_rVJKuGxwV7_hRnHQlljYPX3qziPFm_HfDNX3RLVvHKqvSaP6nslH-d4_Q1ov45QoMm0j1-D4kXIJGfbyY9o0B1ARlvPkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل سوم اسپانیا به اتریش؛دبل اویارزابال در دقیقه ۸۹
🇪🇸
3️⃣
🏆
0️⃣
🇦🇹
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/665767" target="_blank">📅 00:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665765">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qnzVTBGYDEgdDhp5S2CXwJmxuwVU3AtAF8tY_xFg3a1QIE4thoClrqp4PHFVYCT51GtjsTo26rHUji4B40JFXGVGXz5l1WB7L4K53jkP7dKzC7-FcXfQ-CTbbgi8vSp3mJX80D3YG7NSx7POzPVkAxVWNMIQ8Z1SHqr7tSAr8RSdMoIbsYT4Y-UyLfUDFtpTyM699i4TIY09rmB_V7y1qzjEQj-OvxE7TnO3qGILW8vTmpQhJ8SIiDtWJFjtion4GWsLnA8vR_TWbjYNeTIUoBWnvSsedCdpW6uWO0ZKzjG0xn7qbEzklossRL7ZAaTbwR7momAmfT69HdMu7hsn6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tYyq1s5qOgVI2MzPm0xfGyI9YiLaLy8vPYNUOVf5AQ5wnLAI2maXjGRKkTToGlCChFeovN1QLEEtid0K12GU1yKp_6Q4kqSa8p1kYP9NvusxOP6tC1VsGC6k4czjSWl0VVicKU9wP_0DFP19NhjEpMNPEJK7qo8uM-xV7-Cagw4el_SjSj1ZONWElxvEXs9FDuY5sj5zXznFi2CjCugJrPyzaGpbHjhvkKkfH20dido7RnIUUBwGQ5Fnkw3c4piNyj2PejwfR2WVkW9LJnzEyl_WkSHndChvRkbQpqAY7kqmZKcjZYS8AS_R0YWXWyKTMKkqCuXoARE4M0DdRotJBA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حضور سردار وحیدی در مراسم وداع با پیکر مطهر قائد شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/665765" target="_blank">📅 00:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665764">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8435478b2d.mp4?token=j4G1y4C1UNQ4xLM6In7f--LNCnGBT03o-1-QGhy87awHV3V4HxRXH8vU7aCgI1XjaAqkchPeM1lyoYEnu8krq6qTk-iGxIvYdfIosfpmOoqxiLVI3oUhbQi-i7n9xWej3NGEl3m_TOp2rnkchrygVqmDs7kLntPoCGDR8NJsLWXjpv3I01O4qdTSSmCWcQFAgowW3tAFa0xhNIvdBPC6NSzHQNOyywYIAlWkO_h67dsFvnPG2yhljhaOIBKaUn8kbXhrT8p17CSUx_EVcqtIV8AI06IszX7TX5diQHIIQaDrDgoys4VM_Zx2ZBq8qSPZewL-iNLApSVElbamOuMFdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8435478b2d.mp4?token=j4G1y4C1UNQ4xLM6In7f--LNCnGBT03o-1-QGhy87awHV3V4HxRXH8vU7aCgI1XjaAqkchPeM1lyoYEnu8krq6qTk-iGxIvYdfIosfpmOoqxiLVI3oUhbQi-i7n9xWej3NGEl3m_TOp2rnkchrygVqmDs7kLntPoCGDR8NJsLWXjpv3I01O4qdTSSmCWcQFAgowW3tAFa0xhNIvdBPC6NSzHQNOyywYIAlWkO_h67dsFvnPG2yhljhaOIBKaUn8kbXhrT8p17CSUx_EVcqtIV8AI06IszX7TX5diQHIIQaDrDgoys4VM_Zx2ZBq8qSPZewL-iNLApSVElbamOuMFdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یورش نظامیان صهیونیست به شهرک «بیت‌ریما»
🔹
منابع محلی از یورش گسترده نیروهای ارتش رژیم صهیونیستی به شهرک «بیت‌ریما» در شمال غربی رام‌الله واقع در کرانه باختری خبر دادند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/665764" target="_blank">📅 00:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665763">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بخش سوم - روضه (نمیشه باورم که وقت رفتنه)</div>
  <div class="tg-doc-extra">حاج محمود کریمی</div>
</div>
<a href="https://t.me/akhbarefori/665763" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نمیشه باورم...
🖤
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/665763" target="_blank">📅 00:08 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665758">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nNnmCjvr39WaoEkVPT0eHXkzsj-REi_l_SHFAAA-dbp4VpVhPmwRIAm8JCs6SghlQ73nOiizgOf9CCBYVfOoru-BvY6FmzCkrTzHIzoiTQ0e57PleYSslF2WFJk1fB2sr7rKuJdabPoA2bqKT4inHuyy-BoO-IpViAa_giLG0CzzllPb725mm6GxzUpIF1t2bBYDeysBVhvBNcLEznXv8jYJwjTy9nb6okFhDitLHAixsCsNUH43hRrO1nMl3XetOHkcfABCXu1JUw29A_xo628_IRHQ6YSIPu_Sa8ZFul3sn2IygsJ7sYrmqAXILUB8Gr3RpTS5h6SGE_iFGkylNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R2oVPo-xkRIzqZH0VGg12sTrB4Jxv4LUAAoUN0v7-HOloOdtq0Z9CWS3jgoAQ44BbJFsDtpxlz5HMBRwbiFMGGzGVbHUYT3OwlFKpv6sXyfTJ97qQZgpO6UntzAd2F3vr8ZPiUKJtQBeiqxsA-6H3YpPOgbZbozmOZU_85DGmKCHMbQVj2pftuzjWwCifuLbzcnM2zpnyIh9oKTmTiLCSvTfrRnYJvqgPV3b_tJq85Q2mwFx43If067kUbCNuA805ZKVymLqO8p0PSMV65QsnnKG8UmlPs-l4NAW-Fmqdu_OHipx4UNdNZwAO8fGisRSP0dmBMr3-IhmpNpN343QCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pdrkVxuj-WHh1u9bSFzKKkRXEiWcknVfXhrM0YEzqbyP6PelzWcJ7LgAmjl21jp7F7Dc-HTr2zV0dvsy7GfPZKq_yl_jTRkmmHbRnQQ5M1qbWUu3S_r6GNdsEseWAJCh6pqF_7YfnFyo8cXal5HekWty95mtgtj110Z58ddHx4lVBNYGqRGQm1jZi9BESgSTI2iZzl1eYFFLuxpgurSI5654c3UgcvnWkhU0hoPHmY-p2uv5rxX4Tqw9JrLdxvl7C2S-lSkOsxKOHYcAAZYpsL62wFHFf4aSQm_TdhIKO4sSy0Ag-lhZoRs9MmdnZbF9m_HhnY00_AVIDauwnVjpXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MVQopyXOlPTo4qSMnzCCCXhstoSC2JF7e0dU8Sv0y4ilMsqboAlRGqjJgHUk4oo_aceL1z4-0Ku3l-pWiQHJQAYHSyfCHiReb37kQt2iDK1iAzC91U056og27m94GIqnmbSJp5McmPqUWEBMUwJPsKe-p_nQF6uVasHoMYpmtLLeRfiTpx6LOuP5v4P3BNAFjsLtQRrVnbC7URT21RsrVR7ddHRGVfll7fbhtGLpyVap3yUBUPFWElvvHGR4QsRnQl5e8bAsw9SJGrAtWVpDJcARGHvQeC2s6JFcJmNj65bS57MlkmpwnHiiUQb3xVSxNFC_HueHZBtMVRnNsuQ5gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uinePd-g_Ie2Zl_ys5SIRKvYsC1M-JWJkAZ8VgjDgoxGomeHfccY6SAi-peo-v4pyYGaawyJKEK2q-VUfr9NFOUDYCKU_J05thyvuTexxMq04xQybTuEEwtGWuIDa76syy3pFO7aMwzExnRgUQw9OOVndvQHatUymAbkx8A7HTL1m6ktF2ibdbXX2BlnEvuVu8jnN8nqZ0ZHaeugiovHYQuviR5UY6TpdzPZmoL_Qxfbavr599YXw8XhmNPfPXNDpXMSHIw7ZAUpUogtGLziWAfFpYJNsOG4P3bUe90kE6YXyMAA2Nsb9IYrdllzt7KLTArQiUY6ZaH1931viXe9Jw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۵ توصیه راهبردی رهبر شهید انقلاب به دانشجویان
#بدرقه_یار
@TV_Fori</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/665758" target="_blank">📅 00:07 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665757">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba79e01e9a.mp4?token=CcGf4JccHV-qs6wEztsykK1ONbBStA846ny7l9QkHgY7vQAaPYXTRqz0cFrpM8VP_NbvBv-daVWVnJFX_eVVp4s6npBMAvZ4FhGhDbinPOxMHqvyB3V75r7XdGw_y4HmqFT4FA6b8hSwRL4G88lACpOZ9MdZGAZicd1t4aTxal3ZdLXMnzbOfblPkvpbSNHDph1g0sDkDvJIMzANCrG0gX54cxXDzgGUX3rTYr9_edsm6hpCW4PTyknCJGgduYtJ2fec8WV1pajGWaMaH0Mw2gj1Y7rHHMLBDvjcSDiR55ndNme9mstMl1msT3RYNNitVgqKoxfynDuKN9z4pBrv7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba79e01e9a.mp4?token=CcGf4JccHV-qs6wEztsykK1ONbBStA846ny7l9QkHgY7vQAaPYXTRqz0cFrpM8VP_NbvBv-daVWVnJFX_eVVp4s6npBMAvZ4FhGhDbinPOxMHqvyB3V75r7XdGw_y4HmqFT4FA6b8hSwRL4G88lACpOZ9MdZGAZicd1t4aTxal3ZdLXMnzbOfblPkvpbSNHDph1g0sDkDvJIMzANCrG0gX54cxXDzgGUX3rTYr9_edsm6hpCW4PTyknCJGgduYtJ2fec8WV1pajGWaMaH0Mw2gj1Y7rHHMLBDvjcSDiR55ndNme9mstMl1msT3RYNNitVgqKoxfynDuKN9z4pBrv7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم اسپانیا به اتریش توسط پدرو پورو
🇪🇸
2️⃣
🏆
0️⃣
🇦🇹
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/665757" target="_blank">📅 00:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665756">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
کشته‌های گرمایی در اروپا از ۲۱۲۹ نفر گذشت
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/665756" target="_blank">📅 00:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665755">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lAjRN5VUITe2rZ5fjDsVz9PnYaTJfm2fCpwdSvyX9mxskWIJlWgJzuE_q9nykNlPPUzxV4i2dFUZGAh86b5zxl69zxxaoQJnESaLpx-CrUWni5s2-T9aI3t1PBlbMck0zKCqTOzJhjjslsJdbQpUKNIxlJBcMMYj2gqzyP_u-4xtil2EKAhDVRbAm4bBJ1omIwkE30Wr5LYa8rkkTpaR2u_UgHwJFwnA17N5ND3u1TllkCIErn6S1oGmHvkP8MEq6FdjIAmwFhNRN6SRKSltp6H8Q0jqZ6X03xdOLkuS41v0SQbML0K5mzGp_okeMNbZU1ZMiJ6KeL33t1Oo3_fZlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/665755" target="_blank">📅 00:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665754">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">زیارت-عاشورا-pdf.pdf</div>
  <div class="tg-doc-extra">115.8 KB</div>
</div>
<a href="https://t.me/akhbarefori/665754" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">▫️
فایل pdf
#متن_زیارت_عاشورا
همراه با ترجمه
@Heyate_gharar</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/665754" target="_blank">📅 23:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665753">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">-زیــارت‌عاشـــورا</div>
  <div class="tg-doc-extra">علی فانی</div>
</div>
<a href="https://t.me/akhbarefori/665753" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">▫️
صوت
#زیارت_عاشورا
🎙
#علی_فانی
@Heyate_gharar</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/665753" target="_blank">📅 23:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665747">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EEJ6w_tjcHOHxgyqdyk1pqzLVG9Tn_kMyXjLG64fh_FPESDGdrsJt-LesRZEAnnWwlLcfRmxKGqNfaPdlBSTZqX1hTIpuODzyexcN_7YQ8WFIlNN6juvo-oXpkrgof5VtsYkAIoxk2MnB3--kc4qP0H0oyW1e0CI9p8Keq8Or32B1qdrcUHaWVW8dF_WGKB775Q8BK_bmFBGF9wCIxSTCsV0USGyBa2IbCSARvDH8ZUiHsZJgbjIOuZBrdjAOvBF5dRYf6ow1tAkkajcaHGcenyVKJSi3DOEKK3e50nKiZ7rvfdY4_DX57ZgKeCT2Ku17Q82t-qLDzyYgsAjg7hTgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tnZnuMxeMg3r6b9rADjAMdXM5ZXm1HVTQw7rCaqNvMKSC1U3V-Vnm1VSMgMGEyf377jf6bVxb2Yd117Z34nR2qcPd2_fyFJUqkN8fS8bNhtiMPHp2qXvlbxbMC6WYKrCl0cDg93XakDk2NfUFkibe8JUuYnhT92qVcOiaX00AwUPVScVZYBbFeTQAOFvFuMQE7szksLaYLvpwpCcm5YDGy5RxFokZi7L-4tM8FstdTezdqubtm0rGYDCRSKGEhS-speKNF3U9sp6UP_AE35moyx6QUmPVm6Sx3qvbi00fzDG8H-AMZZq06LJLs5pAL1f691PSP08KTyd7hM8682LRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UZcMbBZID3RTI8OAdFvtkS4xTCMlGFufzto4P9aoKLavb6IW6bcLpV2fgg93NFCrdwQwZbzvA-sWLk5TIgiOSKRqcP-MV5I368kXTdTEHnEAhj8RmcM-mFY_ReBQkpTOXoFnJXDSVK2XgyigWNxHHIsIbo1lfJPqhqUDIOURUSGj_Vx8uqf87gzIvzH_Q27YrBGMZ1rs_MeKQrDA855rKaM71DnvYGw8sjJ3cnZCdzuPOKpT5dd2_qNISyx-e3Bjjqvyhi6BQ0t5s03SWPtSYy-Cx5r5lgTh3WFXZxKYOZNpzy8tzhDZrRa9F_8shzuY_SEI36em4QnZXXZWVsApGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/snhcaTsjZxtY8DKko0h3v3kUbSexYclzv9vg8O82_81sqHCAq-yTxIoLQ13BbXSDaDNNew2LF1nNCgjvhaicWVUGenoU1A9IW4aBm3SMFdbQhWlnetCussxLVuLalIiCkifyjQWGsKBmvOGXLnRK6lb5660c8X59S6TnVt-GrXTODsaQYt7pua9K0LIe9k-GRf5wO5ECs3rWxBUiLe8INbqigIEzh_ETFgT_riV8THbHh-jjZOmG7z-OS20rGqj9t27coHVq_fA9osrx4JvWDwcSmyLJNyAYjnrhLUx4qFMdy6GBL_s3iLq65zK78G1GjoOkSvM8uISsZDMeTMLKvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q2chD4-TO09x5ftyLARVbZ-QH5c3IB8OFXbVw4EaTztynOxem1g3UiOFr301qg33_C7cXcWeiVWmlGGKxa9_eTAY-lUQq-AqqjQPKrY3wrt1GpedpTR_9RASPLLeqlUIkXwGbcYdbNm_Ggpb5tiIJadyaD2e2Yg2NMQvfTLJIavVFXtPtu2jvJj_sz1ygyT69d19yIYNWuWDUjmR5WRtTE_oOm8S_XmLu0UFV0CO9sWuDnhG7Iej4WiYCEAdhlcxGLopSo8ZNqJpAEQFBQ2XKXti0n0YOuA78NODFYjwJRzaniyPnhXJxFDBFPQElwNUuIL0SdO2noQLL9uvKcjAAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mfQcxbRHePOQnRX2AJF6zp_uiAY-awyS8_2gup_j8H8yQseeBKKnEH1Mv1OoNegKyw_7ZsTZws5QggrlHH9LVn-jOmFbssQKktPNNHSClXSDDAqTnb4_e9D7SM74s6ptNEuEHDEmxUhdlv056ndODypzzhnCYQDbY1CVZaCLHJV_gQF-hnerqSN-YIQxWfMq9VjmLK3vzwy2bcdtgZbkFVBAb05kF3pbQeSI0XUfTMd4QLgbNmmOohf0gfrZkuRMkPgVZBbexBW23yeY8yKCHbI9tokxDNp2rRAPEIaKq2aSa3dOZ97xiKUSmMk68Z65VTv0t-FszqFM4thsxAX93w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
آخرین دیدار رهبر شهید با خانواده شهدا
🔹
امشب، هزاران نفر از خانواده‌های معظم شهدا با حضور در جوار حسینیه امام خمینی(ره) و محل شهادت آیت‌الله سیدعلی خامنه‌ای، در مراسمی مملو از حزن و اندوه، با پیکر رهبر شهید انقلاب وداع کردند. #بدرقه_یار
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/665747" target="_blank">📅 23:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665746">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/skzw1deXGNmbxGN-2tAr6TBpQKRVF3sAUfLOb5SPlA4Y9fO9wb0h8qmYwv5k_4e-I4M2smO0txD5vnId8Bzp5NubhYf9ZuOa9EGwm8sM9N9OKtFuu0gqASD8W4YfEU0Rv3pvPn-OogcCAIk0lChWNZ1I34I2vHuDIHW9yBljZTD0FDNNzKOnj39qbC24DZ06tRF0rivMCqcqDnwd-dccV-4PJlXpvEwIkNqBFDckl5wcStXFyaXchlilIBGhMhi3wENBI_Owd0Iz_RWSuFxSKqyaldO7Bnez7G--pRntNGSGALYunM0ildErObLHrZOVBGaFVvAT5Wa5_KR_a2DFgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تجربه تاریخی نشان می‌دهد سکوت در برابر ترور رهبران می‌تواند به عادی‌سازی خشونت منتهی شود
🔹
از این رو، خونخواهی صرفاً یک حق نیست، بلکه ضرورتی حقوقی برای پاسداری از امنیت بین‌المللی به شمار می‌آید.
#هزینه_خواهید_داد
#WillPayThePrice
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/665746" target="_blank">📅 23:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665745">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔹
خبرهای داغ امروز را از دست ندهید
🔹
🔹
شکایت یک میلیارد دلاری از فیفا به دلیل حذف ایران؛ تصمیم VAR عمدی بود
👇
khabarfoori.com/fa/tiny/news-3227322
🔹
همه چیز درباره عملیات بزرگ بغداد/ مطالبی عجیب از بزرگترین اختلاس خاورمیانه
👇
khabarfoori.com/fa/tiny/news-3227390
🔹
پیام احمدی نژاد در آستانه مراسم تشییع پیکر رهبر شهید انقلاب
👇
khabarfoori.com/fa/tiny/news-3227344
🔹
راز علاقه عجیب دستیار بلوند ترامپ به او فاش شد!
👇
khabarfoori.com/fa/tiny/news-3227379
🔹
تشییع پیکر همسر شهید رهبر انقلاب/ گریه های حدادعادل در وداع با دخترش/ تصاویر
👇
khabarfoori.com/fa/tiny/news-3227329
🔹
ویدئوهای جذاب ما را در وبسایت خبرفوری کلیک کنید
🔹
http://aparat.com/akhbar.fori/videos
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/665745" target="_blank">📅 23:50 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665744">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EY9qimJPQspRaOrHsMT2OEcBuTsG_KBs0O6lorc_9HSWdrvWkWxXt-2xq9xYEUZYXaVy246O8ozeITOXxUI7_hXIxp_0GHcpJZrxYRqyHpzxlfdMlMcnN1M4yspNf96wanyEzm3UiXSpCvGfA7Ceob5OAxcmFPyvJwkhdExF1gTDodxLmA3Qq2T13iKZ9VMaQDRgZqoS_lATM73sTXORB0V0EeVZkExIdYrs5Exrk9YOd_d_NQsOUopS7AfmICyVI2w1EIaRsaM1QXkl7K77aRlYOHTCWYSEc8466LQeOHZGcsgr6VVz2Tr_BWC6XEuCpUrUVXswL5dIPD4C91QaJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لحظه ورود پیکر رهبر شهید انقلاب به مراسم وداع در جوار حسینیه امام خمینی #بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/665744" target="_blank">📅 23:46 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665743">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
لحظه ورود پیکر رهبر شهید انقلاب به مراسم وداع
در جوار حسینیه امام خمینی
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/665743" target="_blank">📅 23:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665742">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">▪️
آخرین دیدار با رهبر شهید
▪️
پدر امت برای همیشه از تهران میره …
وداع با پیکر مطهر قائد امت شهید امام سید علی خامنه ای
۱۳-۱۴ تیر ماه
تهران ،مصلی امام خمینی(ره)
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/665742" target="_blank">📅 23:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665741">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0aa7753da0.mp4?token=gXDuIGp5tr0M5S3FjVt3fx2XjmQhHm_Fx5br3nxpC3zkPeyAim2EtKbC1JRGlwryH6yO8sJR_9YDcTeAIbrqc1vm8RmVjWIWccTDDf005_wqrvvnkIuXwb0ZdhgcwTKtFroa1UC6K4vdE-_q8ZC9TAUMKq8Q-NPKcx_ebljzIylIAp-B45iZJOC2-pK5A4Ej1lOrVw06IEXqH1sRH1YkDB22n4U-TDMMvYNKpIojh1GOM1EcplxVBfW1-AxXjvuofU1XIXsSWPZKuLtDL4maunZPnqeh8FA9ZTSihrOf7v8HX9_Zjpzs7_bqmk6hms9ZYMc3Vks87UMqSLINwVfd4oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0aa7753da0.mp4?token=gXDuIGp5tr0M5S3FjVt3fx2XjmQhHm_Fx5br3nxpC3zkPeyAim2EtKbC1JRGlwryH6yO8sJR_9YDcTeAIbrqc1vm8RmVjWIWccTDDf005_wqrvvnkIuXwb0ZdhgcwTKtFroa1UC6K4vdE-_q8ZC9TAUMKq8Q-NPKcx_ebljzIylIAp-B45iZJOC2-pK5A4Ej1lOrVw06IEXqH1sRH1YkDB22n4U-TDMMvYNKpIojh1GOM1EcplxVBfW1-AxXjvuofU1XIXsSWPZKuLtDL4maunZPnqeh8FA9ZTSihrOf7v8HX9_Zjpzs7_bqmk6hms9ZYMc3Vks87UMqSLINwVfd4oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خطر امام‌کُشی را جدی بگیریم ای امت حزب‌الله!
اونی که نشسته اونور، میگه خون سیدعلی خامنه‌ای چند؟ بعد امضا می‌کنی!
اونوقت میگه خون امام بعدی چند؟ یکم بیشتر پول میده و تمام..</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/665741" target="_blank">📅 23:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665740">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
ادعای نیویورک‌تایمز: تلاش آمریکا برای ممانعت از ترور عراقچی و قالیباف توسط اسرائیل
روزنامه نیویورک‌تایمز:
🔹
واشنگتن با اطلاع از نقشه اسرائیل برای ترور عراقچی و قالیباف، به‌شدت نگران بود که این اقدامات مذاکرات حساس صلح را به شکست کشانده و شعله‌های جنگ را دوباره برافروزد؛ بر همین اساس، آمریکا از طریق برخی کشورهای منطقه به ایران درباره این تهدید هشدار داد و دولت ترامپ نیز مستقیماً از اسرائیل خواست از هدف قرار دادن قالیباف خودداری کند.
🔹
این گزارش بر شکاف ایجاد شده میان اهداف جنگی آمریکا و اسرائیل تأکید دارد و به واقعه‌ای در جریان سفر قالیباف به اسلام‌آباد اشاره می‌کند که طی آن، به دلیل تهدید اسرائیل برای هدف قرار دادن هواپیمای او، پرواز ناچار به فرود اضطراری در مشهد شد و تیم مذاکره‌کننده مسیر باقی‌مانده تا تهران را زمینی طی کردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/665740" target="_blank">📅 23:30 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665739">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aCE3BIt2PadXc4W2FEsb1HQmcp7ffJIvax6hSTJR2NiIGv85Jk_ldn12stHPbBDuYUbwivZ9Sfj_CvbbZKAZhNJdTV1JwtOixvFgdlXU9D0Q611tjMpAFaJLRo_bxy913qaRuICsZSlg0IdZ_UGBIgB5GCWo6-f55UfaVMoP5SwRgDSqHpOEtqdQT8BTvRjLCF-ztN8oTQHyiCUhonGOLzwrMR7xi2lfb7_zKRTiL9kq-dRAvxLa0ZoW2lw-1pvlh0bHPrlgfif0lt1hQgLBxldhFndTTj6EM79qYOXnao4Os1YUb_GDxgpuIosDFfrN932O9X8pla6IhhzVhlExcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تأکید توییتری پزشکیان بر نمایش همبستگی ملی در آستانه تشییع
رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/665739" target="_blank">📅 23:24 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665738">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6fe6debe7.mp4?token=UCcSAUvuBCwry_e1JVvrmiisSF92nAuh0b23-gEa76k-TFoj8Ri8eFeJeSIh7vD75V3DyWd4SWuMOoKha-VGWdI6Kn9iZxhQXQC7xARv_CmXRFZOJnt_O8MXAv_ZydDYfeis99eSQHNPdGO1X-9GWi-tWgg-thdRHLjNVS1d-AMYVclBHBK8yH8qedQBsonlSindcbyxMRzZqx7UBTf1VGyisqp7bPBATbfHsyD0G3JtPiEDWf5J5btA-4kKkXDzGtuHL39JTbs_cX7qdgEmsXpjdl1-3cpOzmmZRvkFQmNZ-aFhOefcA71mOigEJMg9om81c_KuY8TGnu2hRj-q4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6fe6debe7.mp4?token=UCcSAUvuBCwry_e1JVvrmiisSF92nAuh0b23-gEa76k-TFoj8Ri8eFeJeSIh7vD75V3DyWd4SWuMOoKha-VGWdI6Kn9iZxhQXQC7xARv_CmXRFZOJnt_O8MXAv_ZydDYfeis99eSQHNPdGO1X-9GWi-tWgg-thdRHLjNVS1d-AMYVclBHBK8yH8qedQBsonlSindcbyxMRzZqx7UBTf1VGyisqp7bPBATbfHsyD0G3JtPiEDWf5J5btA-4kKkXDzGtuHL39JTbs_cX7qdgEmsXpjdl1-3cpOzmmZRvkFQmNZ-aFhOefcA71mOigEJMg9om81c_KuY8TGnu2hRj-q4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی مسی ناخواسته وارد ماجرای علی شد
🔹
بازنشر ویدیوی قدیمی لیونل مسی که در آن همسایه ایرانی‌اش در بارسلون از او درخواست می‌کند پیامی برای فردی به نام «علی» ارسال کند، بار دیگر در شبکه‌های اجتماعی پربازدید شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/665738" target="_blank">📅 23:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665737">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G_NSuXTiZtqKtCYmXBYMgu2ZNtKb5GLRJ3GJe4XAbiTogS_mperBf4bz8WcG_pp54BqplQTWUgscLiZh5WOkY58XnR8Q8O9RJ3k9fKnB5CbpkzNKCOPMZvNM26scRXJbP6BEJfd85oya6KVchinWgOaEWv_hR3FIq14fa40re7cI7zWUa1xeM48imWiPmKPDSK3Xappff61bVKojoere-rTE0nov98RBBWmaLV_K_9xeQbjCiUfcyU298LxopSBxVtnwZyTiSYGtwzhsGguFpXQnFnusVSW_5Pl036Dwz9nlPrnWMsyZwmcUDLYMg_hlMtTUf7Rmxf5_s2FcyVW2kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
به تو از دور سلام
چله زیارت عاشورا تا اربعین حسینی
#روز_هشتم
▫️
امروز با خواندن زیارت عاشورا به نیت شهیده  زهرا محمدی گلپایگانی  ، دل‌هایمان را به سوی امام حسین (ع) میبریم. امیدواریم که ایشان ما را پیش اربابمان شفاعت کنند
@Heyate_gharar</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/665737" target="_blank">📅 23:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665735">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcac573db5.mp4?token=J9a9RHyEwwbjoGUpe-OtKAIEeTArpjZ1q5oJwyxT-l2l-dYVo9iVXJhGWK_v4DlvX1RT4UCLAuUeKfN3nmyFEQOmcRFoktTYIy9ExfnoFeew5EDVtcODAlPFK61AQGU8kcqaBeCpPvdvY2aTbMsMf6ZBsosAUn6DnmN4KQZEszi1UjIDvEajTOyZjAt1djGAMYibvSkvEf2EIqKRPyN59e_u5DnocZUsZFzT-ZGBzpHnWadDitM56V0-lBzkZEAahTvtg51mnfyX6vudv0kxXZ8l8W0GrNjh-3cNQh3NzNbBNaNm_-WerZ9Ofu2Yf69iErzS7xIS3kllOCyJRXToBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcac573db5.mp4?token=J9a9RHyEwwbjoGUpe-OtKAIEeTArpjZ1q5oJwyxT-l2l-dYVo9iVXJhGWK_v4DlvX1RT4UCLAuUeKfN3nmyFEQOmcRFoktTYIy9ExfnoFeew5EDVtcODAlPFK61AQGU8kcqaBeCpPvdvY2aTbMsMf6ZBsosAUn6DnmN4KQZEszi1UjIDvEajTOyZjAt1djGAMYibvSkvEf2EIqKRPyN59e_u5DnocZUsZFzT-ZGBzpHnWadDitM56V0-lBzkZEAahTvtg51mnfyX6vudv0kxXZ8l8W0GrNjh-3cNQh3NzNbBNaNm_-WerZ9Ofu2Yf69iErzS7xIS3kllOCyJRXToBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول اسپانیا به اتریش توسط اویارزابال
🇪🇸
1️⃣
🏆
0️⃣
🇦🇹
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/665735" target="_blank">📅 23:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665734">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aBTxeLUYQL1mu0hup-ohVBMjv27fs8h76tfqk3nT_LhJaOkQ7HNXdP_b8gTJcLF1MZUT8cK5rInrVgxaHc3EYZrPpe2fbEe17xcjKknas78gn26RbhZHzvmOcGz2GVb4WCrP-4NFWeCRgT1DQcWgkVfv29WOy13IV9Hmu0mHPMSAGrIJJmOsiGLczhBZ-9g0lCfEqUjBg64o6aGYI-LRe5ZzTe9RQqFjSmlh4trFE5o5ZO95XiNt8iVtejBoWxyEjQkm6fAS3XlqgovURd85u3q0D24-hUSWdxt9GdTdOZxjyD9wIqaG0ALnUSjO55hlRa_Oifdc-2RtuuTo4faN2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رستاخیز خونخواهی
🔹
۱۲۴ روز از شهادت رهبر انقلاب اسلامی می گذرد، اما اندوه فقدان آن بزرگوار همچون روز نخست بر دل و جان مردم ایران سنگینی میکند. اکنون که کشور در آستانه تشییع پیکر مطهر ولی امر مسلمین قرار گرفته است شعله های خون خواهی این امام شهید بیش از پیش برافروخته شده و دودمان قاتلان آن بزرگوار را در آتش خشم و عدالت خواهد سوزاند.
🔹
هفتصدوهشتادونهمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/665734" target="_blank">📅 23:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665731">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال رسمی فیلیمو</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b603dc349e.mp4?token=hybbE2AGZcahn_o-cUF2T33F_gCn944avgPruRRYqX3_xO8DhjP8FBJZjhxjhZL8y5Y51QgbFQd5702PRbi2UlmAknI9Jr4Ucr91LZB6XPCbYfyOlCweqLzUgicBRMoC83eXxStRi8rQ9nBEYpgQ4eXBOWSXUoh564OBP2DwKhq6pwiQwZdmgeAE8DHrOOSjHvbixhK5Liw7SQH5VcvI3JEcwgcMqSsqTaST9__lF2oKJBkNFXk7mOtB4OBZquEmo4jFvUZd44jr4P7Ak9JQDW_8Le3Cun5k3iSf189Q5vpIHbAxj38r4f4iJN-3AzSKOVl_HMmsT1i0fRlPF2qK0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b603dc349e.mp4?token=hybbE2AGZcahn_o-cUF2T33F_gCn944avgPruRRYqX3_xO8DhjP8FBJZjhxjhZL8y5Y51QgbFQd5702PRbi2UlmAknI9Jr4Ucr91LZB6XPCbYfyOlCweqLzUgicBRMoC83eXxStRi8rQ9nBEYpgQ4eXBOWSXUoh564OBP2DwKhq6pwiQwZdmgeAE8DHrOOSjHvbixhK5Liw7SQH5VcvI3JEcwgcMqSsqTaST9__lF2oKJBkNFXk7mOtB4OBZquEmo4jFvUZd44jr4P7Ak9JQDW_8Le3Cun5k3iSf189Q5vpIHbAxj38r4f4iJN-3AzSKOVl_HMmsT1i0fRlPF2qK0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه راست میگی الان سرشو ببر و منو بشون پای سفره‌ی عقد!
#
بدنام
، قسمت ۱۳، “داستان دو شب”
فردا ساعت ۸ صبح، به‌صورت اختصاصی در
#فیلیمو
با حضور حسن پورشیرازی، امیر آقایی، سینا مهراد، ستایش رجایی نیا، سولماز غنی، سید مهرداد ضیایی، به‌آفرید غفاریان و لعیا زنگنه
کارگردان: احسان سجادی حسینی
@filimo</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/665731" target="_blank">📅 23:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665727">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QSkUNRFrvU4ys3XrDEhOs1Mk2pF-PKdjTmtRpV6pKFv8ZqFt-qAUHTikhC8A9i0iu04wAXfs8TulReYxVGWReXLDy3kKhyRNrZN5nigsFVqab85KNAnAtPsDFEFVwiUvxj3wdvTaPsEORg9117lIXtHj84PsK6u8PaaFRxSO9wQzCKbTy7DnmDMoanbxick0Z7cgQof_FoQNgnu5YezIkBZebcyAJkkvI2tkVBou91O00cdcXCenwV1ODpUtf8Yvc1QTl0iJpnsQO6ffMXfeu-oc83NXr5J4xGKrIu_H3ekshEIq7ZNOBj1KAv6bYuOdKJnXncWZ-1usqpxfGV43Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خاموشی فقط چراغ‌ها را خاموش نمی‌کند؛ سفره مردم را هم کوچک‌تر می‌کند #برق_مردم_کجاست
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/665727" target="_blank">📅 22:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665726">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27f7a4b6ef.mp4?token=m5GLslT149q1qZuycfZNat3_gkQV3w4rrQj6o6YPwgci_OZNf61ncOKCNfxCcI8IBecWvpmiZ7EZAtqXaWWLhakaxPR7Fz0nU7HCiTilcacaziEAnwd2RTa69rH1oZDO2JxsHw1EXUdzPZJ9fysKAzoPCYN81uo_dVgsyHa6qpFHeJWol-UkdNklEMmbNGDUQxcLO4BJe9VosAWAK00efghqKfmIlDeOKHpzQk6HlADd_LYxTM2biRwcr3jjsxlve8rsZD9ASDp5GXHGAC_2Z1YJXoW-VN4hw1anc2wnY36ZK8pQcVthzwgJVFHPJLXe3yWZdERvmnFQSY9lIVAidA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27f7a4b6ef.mp4?token=m5GLslT149q1qZuycfZNat3_gkQV3w4rrQj6o6YPwgci_OZNf61ncOKCNfxCcI8IBecWvpmiZ7EZAtqXaWWLhakaxPR7Fz0nU7HCiTilcacaziEAnwd2RTa69rH1oZDO2JxsHw1EXUdzPZJ9fysKAzoPCYN81uo_dVgsyHa6qpFHeJWol-UkdNklEMmbNGDUQxcLO4BJe9VosAWAK00efghqKfmIlDeOKHpzQk6HlADd_LYxTM2biRwcr3jjsxlve8rsZD9ASDp5GXHGAC_2Z1YJXoW-VN4hw1anc2wnY36ZK8pQcVthzwgJVFHPJLXe3yWZdERvmnFQSY9lIVAidA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وضعیت بحرانی بنزین در روسیه
🔹
تاثیرات جنگ به پشت فرمون روس‌ها رسید. قرار بود سوخت اهرم فشار روسیه علیه اوکراین و اروپا باشه
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/665726" target="_blank">📅 22:43 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665725">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c454c5ac8.mp4?token=fu3u8T2g-2iiLO0MoV_meOFk95zLksj8H5PMBrfpyKcABv8aiGrNpvKRRn7KmGEc0vyZoQamLNQQUFVfHuoT0K99nWQVDglwvwuYTkjhS2L4iwiAS0FF_o9kyj8krKkfZ1_PUvaiPBiYICKXtdTg_CkMbvlVT7cDapoTymLWk0J3sKoh46HayVgSK11zoAeDAVINTwaPJ_3cjjTjjp2-7CBY_45_0X5D8YSZ3fUALFsrxDr5SiOmHO6vOLBapj42ypjBCqcghTThf_8QzHLDeOO7iFdHvagfFGoiSPoHXm7N4E4l2yIH3Fz8v7Z7j4wvAY0BRXk_mGevhfEk_7Jj7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c454c5ac8.mp4?token=fu3u8T2g-2iiLO0MoV_meOFk95zLksj8H5PMBrfpyKcABv8aiGrNpvKRRn7KmGEc0vyZoQamLNQQUFVfHuoT0K99nWQVDglwvwuYTkjhS2L4iwiAS0FF_o9kyj8krKkfZ1_PUvaiPBiYICKXtdTg_CkMbvlVT7cDapoTymLWk0J3sKoh46HayVgSK11zoAeDAVINTwaPJ_3cjjTjjp2-7CBY_45_0X5D8YSZ3fUALFsrxDr5SiOmHO6vOLBapj42ypjBCqcghTThf_8QzHLDeOO7iFdHvagfFGoiSPoHXm7N4E4l2yIH3Fz8v7Z7j4wvAY0BRXk_mGevhfEk_7Jj7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نوین ایر در آستانه آغاز پرواز؛ ورود رسمی جدیدترین ایرلاین کشور
🔹
بر اساس اطلاعات بدست امده  « نوین ایر »،  به‌عنوان جدیدترین ایرلاین کشور، در آینده‌ای نزدیک فعالیت عملیاتی خود را آغاز خواهد کرد.
♦️
بر اساس اطلاعات موجود، هواپیمایی نوین ایر با پشتوانه‌ای توانمند و برنامه‌ریزی منسجم، در حال ورود به صنعت هوانوردی کشور است و از حضور جمعی از مدیران باسابقه، متخصص و شناخته‌شده این حوزه در ترکیب مدیریتی خود بهره می‌برد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/665725" target="_blank">📅 22:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665722">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e65499983.mp4?token=SblVSInpA0QUkFAwTk1gpRNlFWOCwDaL_4qhggL9YlTmMpZh6ax4uoQrcPDCPPdATwRO2c5aJCVgNVflWwJbg_JLtNMPXPUicH-W8vQkPlkR9mkaVAUp0xhiEoHWEdbfea1Zfqf2ovkv_Z8jyaV2MJzztp3Dypo8g5SrRWCxFJa4VhQM76l-tc4FXywK3CPn2NZuB5T77BctZMr1F0lLVwEcTSHv6mEzxTA2zy9cev-YmriePYgdISugRwuK4Qu0dw5KueDqXFXXcwWQfBOUGy_r5uJcK0PbTmJi4xWrYH_wg3Rup__KjSIbmab5FilU1UcNg2HS1k-fdk1udklaaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e65499983.mp4?token=SblVSInpA0QUkFAwTk1gpRNlFWOCwDaL_4qhggL9YlTmMpZh6ax4uoQrcPDCPPdATwRO2c5aJCVgNVflWwJbg_JLtNMPXPUicH-W8vQkPlkR9mkaVAUp0xhiEoHWEdbfea1Zfqf2ovkv_Z8jyaV2MJzztp3Dypo8g5SrRWCxFJa4VhQM76l-tc4FXywK3CPn2NZuB5T77BctZMr1F0lLVwEcTSHv6mEzxTA2zy9cev-YmriePYgdISugRwuK4Qu0dw5KueDqXFXXcwWQfBOUGy_r5uJcK0PbTmJi4xWrYH_wg3Rup__KjSIbmab5FilU1UcNg2HS1k-fdk1udklaaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازتاب شعارهای جدید در تجمعات شبانه پیرامون تنگه هرمز
🔹
گندم و جو ارزونیتون؛ تنگه نمیدیم بهتون
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/665722" target="_blank">📅 22:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665721">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
نماینده مجلس: کنار رفتن وزیر نیرو به وزارتخانه کمک جدی می‌کند
بهروز محبی نجم‌آبادی، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
در صورت بازگشایی مجلس حتما این موضوع مطرح می‌شود که استان‌هایی که تولید آن‌ها از مصرف‌شان بیشتر یا مساوی است شامل خاموشی نشوند، اما امروز شاهد خاموشی برخی استان‌هایی هستیم که تولید آن‌ها از مصرف‌شان بیشتر است.
🔹
هزاران خاموشی‌ بدون اطلاع اخیر به کشاورزی، صنعت و مصارف خانگی جای گله‌مندی دارد.
🔹
شخص وزیرنیرو عامل جدی مشکلات وزارت‌خانه است و نقص مدیریتی او کاملا مسجل است و کنار رفتن او می‌تواند به وزارت خانه کمک جدی کند.
@TV_Fori</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/665721" target="_blank">📅 22:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665720">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a71c35768.mp4?token=hKAKGdChX9WLO-PpWGVYiYpjrIK-4XId3SmI-tQ5vK05uhFvTk0AmuWz-vIUe4Q9xfr_Hw7BGL3M5uu21dQIoUqYAcDsfuDkWqrDY7y4Q4A9fbvZ2SIgKZB_fXjUXjtD6CIHC-KXwPidod-uWZDqsu5xWQxkHRPU1tZ3I8PydxxJqQm0etDnA87zSPuuTXcPidEXEaEsgyn_SiT1sjzVL_mVYYQWhQIDuoumdAGXMtSF4uxeru4SRryFHu_czCqxlLSE59Gnh6noZwZ2PYwVqXnYCitwvOTJ0drYOlXwpClOaKZ1KTeqPyppjHw402klP2Qan2GdoK58W4BkZH5HDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a71c35768.mp4?token=hKAKGdChX9WLO-PpWGVYiYpjrIK-4XId3SmI-tQ5vK05uhFvTk0AmuWz-vIUe4Q9xfr_Hw7BGL3M5uu21dQIoUqYAcDsfuDkWqrDY7y4Q4A9fbvZ2SIgKZB_fXjUXjtD6CIHC-KXwPidod-uWZDqsu5xWQxkHRPU1tZ3I8PydxxJqQm0etDnA87zSPuuTXcPidEXEaEsgyn_SiT1sjzVL_mVYYQWhQIDuoumdAGXMtSF4uxeru4SRryFHu_czCqxlLSE59Gnh6noZwZ2PYwVqXnYCitwvOTJ0drYOlXwpClOaKZ1KTeqPyppjHw402klP2Qan2GdoK58W4BkZH5HDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تفاوت آشکار قیمت خودرو در بازار عمان و ایران
🔹
مقایسه قیمت‌ها در عمان با بازار داخلی، گویای فاصله معنادار هزینه‌ها و دسترسی به مدل‌های روز جهانی در این دو کشور است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/665720" target="_blank">📅 22:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665719">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kBMbeeVHZNzidB-47-h8OQGHJhZSGj1QaiCEPxxOvJ5cJNI_42tsXTI7bAMiz_RUlpg8fyMANDhNZjidXjWxgMSacrKkWVGzDf8qVwXffzmWr1lb4kyim_hty6SAfCgA1N3CuPyy7hi8mVTDedVhCS9Hk1c7fyi7cJfTHDc0uipOmbYu3gBa2U7apjhDTq3WD9oNCoX_rbNpB68O-oY3f7y_5pKPS88W6LDno15k4Ki53o7WvvBIuF9qzaIna-XIXBwGlLRbp7olqhMUUth48dLASQS4UvzlyYUUkSlBBJJFP_byo-p2p1QqCHwPPfJ6MaOsATJRWc0Lmm16lMf0xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش عراقچی به سنتکام: صلح منطقه بدون مداخله خارجی پایدار است
عباس عراقچی در واکنش به پیام سنتکام، ضمن زیر سوال بردن نقش این فرماندهی در تأمین امنیت منطقه، تأکید کرد:
🔹
صلح پایدار تنها در سایه همکاری فراگیر و بدون مداخله نیروهای خارجی محقق می‌شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/665719" target="_blank">📅 22:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665718">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
کوهکن: خونخواهی رهبر شهید اگر انجام نشود دشمن جسورتر می‌شود
محسن کوهکن، کارشناس سیاسی:
🔹
در ابعاد داخلی مطالبه خونخواهی رهبر شهید یک مطالبه صد درصدی و اجماعی در میان مردم است و حتی کسانی که مذهبی نیستند، ایشان را ایران دوست‌ترین رهبر تاریخ می‌دانند.
🔹
اگر خونخواهی رهبر شهید پیگیری نشود دشمن جسورتر می‌شود و مطالبه مردم از مسئولان این است که این موضوع را جدی بگیرند و آن را رها نکنند.
🔹
اگر خونخواهی انجام نشود، هیچ نقطه‌ای در دنیا برای صهیونیست‌ها و آمریکایی‌ها امن نخواهد بود و این پیام باید به دنیا برسد که با شهادت رهبر ایران موضوع تمام شدنی نیست و مطالبه خونخواهی ادامه خواهد داشت.
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/665718" target="_blank">📅 22:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665717">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f4VygJfgIceZmC16DlUpAOAV9XR6vH8onLT24jhhQaYDBWqi20B6isDCEwrLp3msCWcH2CnxlCDgggOL6tErPK7T951iMo6_7tLni_a4lx_585F7pvY9nZ8x17vxV7U-odC58VPHR1aAvoj46E7mI80TGNBDZEEhsGyqCfWFRmwwtBDf_LVurJBC9aXd84zpB4lIbC3a0Mv1rkwcNcncucF_QhqZA3qTHTAZNCyHR-zU0NKhlIZVwhVBngtcdH-BvikZrHsS51rxE9oW9D3XFjqUuu1iw7KlrhJ-B2bqsv2kEQVuroCcMeKgTmrdBG4g8NcD09I_ovavNsoZRDaBjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آیینهٔ روزگار؛ عبرت‌های فراوان و چشمان بسته
🔹
امام می‌فرماید: عبرت‌ها فراوان‌اند؛ اما عبرت‌گیرندگان اندک. نه‌تنها تمام تاریخ بشر بلکه طبیعتِ پیرامون، سرشار از نشانه‌های بیدارکننده‌اند. خداوند نیز در قرآن می‌فرماید چه بسيار نشانه‌‌هایی از خدا در آسمان‌ها…</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/665717" target="_blank">📅 22:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665715">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d5af43285.mp4?token=kOQyJ_VZV-DSwlZb0j6W7oOK9YN51Hf5V-kgKRlkHoqbZHGqWhfJOPL-sMnsl3CG36L13db5DNnX6VoZqyRkwAW5khrQT-WlfMlpc9aEA5Qb4naZe3DJyg6Xc6sGo2_2f7OLlXDv_WGLbHqLJcNDRWkSlJ45VxvM5SVKOGtmH0FT_z6wCmBz3N4l05fmkdVQNiWZd6eE26cH4-bPuWtsCGU7vex9ddTx-HvltK4Wm96Dq1hnWM1DTzvliG-kIR_Z9LDEKB__6-gMMloT_XoUDQb0Vw6HsJ41sqmLBdxz0Wc4ccTvKxMP2NdL181tCYG2n1i7Nkh1kY95NosWKSfgow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d5af43285.mp4?token=kOQyJ_VZV-DSwlZb0j6W7oOK9YN51Hf5V-kgKRlkHoqbZHGqWhfJOPL-sMnsl3CG36L13db5DNnX6VoZqyRkwAW5khrQT-WlfMlpc9aEA5Qb4naZe3DJyg6Xc6sGo2_2f7OLlXDv_WGLbHqLJcNDRWkSlJ45VxvM5SVKOGtmH0FT_z6wCmBz3N4l05fmkdVQNiWZd6eE26cH4-bPuWtsCGU7vex9ddTx-HvltK4Wm96Dq1hnWM1DTzvliG-kIR_Z9LDEKB__6-gMMloT_XoUDQb0Vw6HsJ41sqmLBdxz0Wc4ccTvKxMP2NdL181tCYG2n1i7Nkh1kY95NosWKSfgow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دعوا و جدال فرانسوی‌ها در فروشگاه‌ها بر سر خرید کولر و پنکه
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/665715" target="_blank">📅 21:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665710">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cMdoY2vDz7ZA9N5tpekQB76AwFBTaCBVO3H1k5qPqp64ZCdHSqq3UCz8-p3vfM3tKMl4_DjMrui7oOCLrcYvW0QdPKKW7H_TizZS_SatrCOV-fsBZ5x0AGtqXNKPqFXib4BSVmofcrix4tyPvWhbnHb7fUH_XZfS0dKGz1ICFTj_vorb33ZpZ34OtPHC2CTFlNeNm_nycXQUy7CxoT0hFagdXuHZ04PivGBivzS6kP7XQWJAP1gTSUmqNHYT3qdyTZwW95g0LXsj90RjDOCL4FBURVWYaQQHN-XXCYwZQHUgejVhm__RHf5y5JR-Tppi3ukXFYd2U8u8mx0aE15eCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Og5PgWIqIo5tYxwHCsqd3gDf__US_8ylLjkB0F9-Zf6y2wsRZgl270D8_dNLn2AWMO_iY78j5FAns8IQFtl0elBW81vGFMW7fpJQVSn26McsBRbS9gBey5uZcZ2-rNj0nwqbXh33NVyYS5n9xoEGgzguigAdXblADgHODBOS-88QSqVcWlqSgumbqxGFQXd05Z0oED-bhbMYoXnp1pmUorabVzmwA5URsAfRvremnFrBaS6EvARj6ANvcCLRQ55tCsMRqBgYpvumPYM_kIyF8TOg62cZlJVpJ13yHRavrj1lMjvrUFdP84kPK2rfEWSwJ2wtStIXTe2qliMu9Xtq1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iW_PtapFfzSTcVwNdBTOTA6zhITqlyNQ4ZAz6hSMhQFZUdAgO6WG_9QmI96ZYUSNVa0exI8o1B0IqJgrrSwfjdN7Ax0LBUOz79yjO1mSXJVh4mjYwXeOd_dM2ZaXMQdjU9a7rU8RJT9tU0VWo6wbcTL4K6HX8pvr24JNqOSusl7DHVPuK-DDtu-mKeX4Ak3Hv6n_yKF4_XY4Yu9fuvMCNV1EHKLZAJgpGPixwLoM11lJOki46gCaExAzHNf_seycFUwtnYZmxCIxyWLwLyId-tOMEF3RIB6sOvGGL0C9fdTOopdgNFaMgWtyvOlLK3DRA03u8aCauUehvcwsSYdAyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FvmBPm6tPYYSEqhQdOxDDV5Br7XRi55d_WXlSoaSmHsvtYcIrwwdCYv4YErZF6sjVbhR4fZtcJjlPiVhOuhxXaVrTyRMOP2osCm-lzCMLSYkXw0hq0L2m9pvs3ImiLYqK2wBtrv_2ldsNjQoiVI0F-Z1uoq5bv-EJKyxSx_jJUpuVUrF7A_sWDVWk3QeswS8qDsX6WZaAnQeyo9odlMcAGfxBQBT5K2m7HEj50aWCJzQaQSB_liRaD5oD0p9QXieN6EmQRp_f-8f-sxXCGWfNNZKiRXvVC9abbplC4mhh0FtUTnhVdUHXGAy1Pw22yFU-8ySrr5FtdDoRo4BCDp2Fw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
دیدار عضو ارشد جنبش امل لبنان با قالیباف
🔹
خلیل حمدان و هیئت همراه، ضمن سفر به تهران برای شرکت در مراسم تشییع رهبر شهید، با رئیس مجلس درباره تحولات منطقه دیدار و گفت‌وگو کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/665710" target="_blank">📅 21:53 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665709">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55a5b7b725.mp4?token=DjZBM0Nmiim3vmxZ2dSkcEL0YAPBsKLSfm2NMtbLtiDI7CuPKD89EE9HLcNQc4hRiKBZu9WbLbGFx1Xxn6pr7vJEsAVxprkn9r7QMubmTaIY1eD-4p2yi5AERFgXbK4N-EaDXhWjft3G9srSGuLgz2fnLr0CxbRISXLCH35L3vSyiiHWdXiUHLs_5Co4DcgE9AlKvKapMqMSDGZeJFXVNqNRnsErCg_8XsW5p_xIF9U05CM4AFrEYajbl14sGKOjteF04WDdZ8gWZCCodEUoaDpdUw5HAhn6TGV_TUif_v-1KIV-Ihgdg9V2GOOctAnOVHzRbBikLQm25fHLowAd6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55a5b7b725.mp4?token=DjZBM0Nmiim3vmxZ2dSkcEL0YAPBsKLSfm2NMtbLtiDI7CuPKD89EE9HLcNQc4hRiKBZu9WbLbGFx1Xxn6pr7vJEsAVxprkn9r7QMubmTaIY1eD-4p2yi5AERFgXbK4N-EaDXhWjft3G9srSGuLgz2fnLr0CxbRISXLCH35L3vSyiiHWdXiUHLs_5Co4DcgE9AlKvKapMqMSDGZeJFXVNqNRnsErCg_8XsW5p_xIF9U05CM4AFrEYajbl14sGKOjteF04WDdZ8gWZCCodEUoaDpdUw5HAhn6TGV_TUif_v-1KIV-Ihgdg9V2GOOctAnOVHzRbBikLQm25fHLowAd6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به نظرت مرکز دنیا کجاست‌؟!
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/665709" target="_blank">📅 21:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665708">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nh4UvZARN0RdXZj9Eb2J3POfZVNkJHP7Ss1uMBOmoXuoInrtdmx4yRU_6yBoKVT3iNcW9EjhpOzqE224Ls21k6anW_FuqzP7mdy8HEVQw9NccMXpUul7pgIQsr__y37s83COErKTEmJ2BZZl5DrVlIbeNADcikCuT0aTVJj8ZSOsvB-wWgozzE12QmXf_I1Ggv5VjUubaNtpd--kWUyTcfF__NGk6UQBwtWZcX3o8cN28ulK-TGzdFKbqvfKsJ8oWJAC9PBN8CT7Dowi8fxPw_kCD_UhzAMqksb7oDVtd9hYV0n0X2-GPRU8wNvlf4eiCtt0oPPAby9uTLI6dJz7TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مجله تایم: ایران شاید بدشانس‌ترین تیم ورزشی تاریخ
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/665708" target="_blank">📅 21:46 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665706">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cCJWGeouaNkvXR7O6RrFnVO7A6n17h72nBPRKOLMKphojxukRMEZ9qBK5HwzbfRtc1Q_UZ5GvxhRFdoVVcZCNlrEKBBqRRfEKGHYUCbs_KM3VdsRWvWWcyxHdbWsbuCj6VoSKgWMZsmrlLZTD5fPg47sCC4jlQEPkJu35iAw90iWMY7mPFj7kysfFjco28Uzy3gTf25dCwA4jq-6hJ5tewTnalZ_ymZh48bkIx5X4fh6LktuT-iIkgLzv0JVSVuzFCgxLaQH68VkoCHZn5YNwLOSsOrNRmLqlE1gD7pNNuMRIwH5Hpm2VliGO3lDrBSK3HHkLjFREqm4x1VXohVB6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راز علاقه عجیب دستیار بلوند ترامپ به او فاش شد!
🔹
برادر «ناتالی هارپ»، از نزدیک‌ترین دستیاران «دونالد ترامپ»، مدعی شده است که وابستگی و وفاداری کم‌سابقه خواهرش به رئیس‌جمهور آمریکا ریشه در دوران کودکی، نوع تربیت خانوادگی و باورهای مذهبی او دارد؛ ادعایی که بار دیگر توجه رسانه‌های آمریکایی را به رابطه ویژه این دستیار با ترامپ جلب کرده است.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3227379</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/665706" target="_blank">📅 21:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665702">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcf88d31ae.mp4?token=h0xVB067vavt1qR_uHDGAFQDf-Vzr9IK54vBpwVhUt2N57jAGciwCQS7lyz0ag6DX-6gaB6j5p4FwO3WFNsys6OmKpSDswX2hLpt5IW0p-fJ85yirjVzED1Ih-Lt4LI3KblRIDJywRdEpKdTMi8v2tEpqKLA-jcm-j63VU3O7gMiE6Om3RjLqhgqQ7Z71FWS0joFByjcjTfCORiC-B47pVh-dJCehUE-W9FSuCcgZ9zQaoNoSUCKhjHz0byCfEbRVZjauAlgDeq_ZPe9rEl8Iv3sYj_xdc8ykFvbCvgACH1DFa7w2AHQWQLLfqDChy1NcZYNe2yvmXqNEMEKu-IoR1aGo-a6HCeBWnNtnYT9674FCpr0rV9kQK3qLzJ6sh4RRJGGGoFsMNqPcf-kLhAtgBpWOZT8UW3COIWO_leuvbzhs5zfA-HlB9Auv6gwNRRTXBC1t4hBId2cECpOgsZTnkoee_fGD3RoMQ_P4EifbvHC3txlxqqFpaHcl_SE1IO045i9T1jnK_NL7KWSpYiTLYnwOJFN8UJwcCKkpjhF2zDLe04e3xOu8Jfag55NAkxlOd2HYomeGRNSizx2YDElmAPAvmOAK5aLsXVvYUj4a2po7Lqrg6Igfd38Qk42maZbfFFP8QUxtmUZ-7iJc1BSeH55YnbMMG2ZJVo_URGzVb0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcf88d31ae.mp4?token=h0xVB067vavt1qR_uHDGAFQDf-Vzr9IK54vBpwVhUt2N57jAGciwCQS7lyz0ag6DX-6gaB6j5p4FwO3WFNsys6OmKpSDswX2hLpt5IW0p-fJ85yirjVzED1Ih-Lt4LI3KblRIDJywRdEpKdTMi8v2tEpqKLA-jcm-j63VU3O7gMiE6Om3RjLqhgqQ7Z71FWS0joFByjcjTfCORiC-B47pVh-dJCehUE-W9FSuCcgZ9zQaoNoSUCKhjHz0byCfEbRVZjauAlgDeq_ZPe9rEl8Iv3sYj_xdc8ykFvbCvgACH1DFa7w2AHQWQLLfqDChy1NcZYNe2yvmXqNEMEKu-IoR1aGo-a6HCeBWnNtnYT9674FCpr0rV9kQK3qLzJ6sh4RRJGGGoFsMNqPcf-kLhAtgBpWOZT8UW3COIWO_leuvbzhs5zfA-HlB9Auv6gwNRRTXBC1t4hBId2cECpOgsZTnkoee_fGD3RoMQ_P4EifbvHC3txlxqqFpaHcl_SE1IO045i9T1jnK_NL7KWSpYiTLYnwOJFN8UJwcCKkpjhF2zDLe04e3xOu8Jfag55NAkxlOd2HYomeGRNSizx2YDElmAPAvmOAK5aLsXVvYUj4a2po7Lqrg6Igfd38Qk42maZbfFFP8QUxtmUZ-7iJc1BSeH55YnbMMG2ZJVo_URGzVb0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گنجینه‌هایی که رهبر شهید انقلاب هیچ‌گاه فراموششان نمی‌کردند
#بدرقه_یار
@TV_Fori</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/665702" target="_blank">📅 21:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665700">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nso9kD1wzhOBVKgmbbbIifv8Hbg3qXNFGIUGZQUOmp-JdXyFAjZXz3geZK28R7cn1kIcgYoa206OU39PSF0r7yRCdiQL15HIFeZ4XDCTsXH2WOOQmEjfEiAzcQRnic4bkjuhfTee8ufmYi9dQFDPQ75VLp2W4VUb9KTPcQ7QigDrK1whw_264rb0ApEVMZzN0-wnUNy3B0on8pInIr_bRh6kCBExLN3cyo7t4Ctk95YvINasUtix3qLsRM-KMR1CBg50FGd_KOlByywK-Vsz540_zXmd8_yP5HG-BKtkZhD-09LEmvtjzqsz7Bi9g7O589wqQBRlmi0C6yGL4_kFjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معرفی فیلم: داستان ازدواج | (Marriage Story - 2019)
🔹
ژانر: درام
🔹
امتیاز (IMDb): ۷.۹
🔹
خلاصه:  «داستان ازدواج» روایت فروپاشی آرام زندگی زوجی است که هنوز همدیگر را دوست دارند؛ اما دیگر نمی‌توانند کنار هم بمانند. فیلم با بازی خیره‌کننده آدام درایور و اسکارلت…</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/665700" target="_blank">📅 21:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665699">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k9big_G9LtPX34i3G4Fxu5gCUakbs35r0jXmU1hHBcPNIabkAHajffJ6J63DAGObJxicLkeU-0onIAJu3jPV_uBjDQ3DpZwYjEqQeci_YYfCDw1dipYQoclkJ5YJIxfLQT03ZG_VGGUEFQszkfKYYIHedk4SH402dtMfFHCCFci8cEFCroTTnaAATHH6KKR-EoIn3t7SkvODkJ2z7YoSf352n6pKWwmPqVfbjfb8V06j59N4DiBFqW3_38AmAzEfZ3eP5dAIscTZog_6xJ4KzEjyJWWT_swTQvKj7E_V7FYX1xKrKYmAnft0VxXgwXW3fqPX8X-OeF-EAdvTqWx76w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رؤیت شیء ناشناس پرنده در رادارهای هوانوردی آمریکا
🔹
ادعای فلایت‌رادار از شناسایی یک شیء ناشناس در حریم هوایی آمریکا خبر داد که ماهیت آن هنوز تأیید نشده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/665699" target="_blank">📅 21:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665698">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GT8jK3vfpgz5sIk9JAFYD51_4KCn3m5eLUvAeKSjSF1bRYUp2zv2qbOM-sJgOBs9XP_NA10m0w3RKMYwRh-bimjZGhYxLQIV0rMhCEpi319IQMlTRQf3C0GGAs8RjYK5sWwDK6TGvRWzR9uYS9spFU9xUl2NQZblfIN2hHRoeAGlnSCU9Q2o9JpxJargozom-JBm8VDNZ4TFhWvll6NKKrWaVGFFgmEXrTxlFWKJ6OX7Rigp2-nol0uL3zCuTYj97MF9U4-rVRVTK69YTLPwmlAOFQI9gawzQTT00Hb_RYAsG55l9nqdgLmud5NtOxSpkrap7wN062djcWKYKCpHgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دستیار رهبر انقلاب:امروز، عزتِ یک امت، بر دوشِ دلدادگانِ راهِ اوست
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/665698" target="_blank">📅 21:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665696">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
آماده‌باش گسترده اورژانس برای مراسم تشییع رهبر شهید
شروین تبریزی، سخنگو اورژانس استان تهران در
#گفتگو
با خبرفوری:
🔹
در مراسم وداع با پیکر مطهر رهبر شهید، کمیته امداد و فوریت‌های پزشکی ستاد برگزاری مراسم، تمهیدات گسترده‌ای انجام داده از جمله ۱۵۰۰ نیروی عملیاتی اورژانس که در تمام این چند روز برگزاری مراسم به صورت پیاده و یا با ناوگان حضور دارند.
🔹
همچنین ۴۴۳ دستگاه آمبولانس، ۳۰۰ دستگاه موتورلانس، ۳۸ دستگاه اتوبوس آمبولانس،۷ فروند بالگرد نیز در نظر گرفته شده است.
🔹
برای نخستین بار قرار است انتقال ریلی برای مصدومین داشته باشیم و در ایستگاه‌های میرزای شیرازی و شهید بهشتی ظرفیت پذیرش داریم و از آن‌جا مصدومان انتقال پیدا می‌کنند و خروج نیز در ایستگاه جوانمرد قصاب و ایستگاه مترو سمت شهرری به عنوان ایستگاه پایانی می‌باشد.
🔹
قطار به صورت اختصاصی برای اورژانس درنظر گرفته شده و ۱۴ اتاق سرد و ۱۲ ایستگاه درمانی نیز برای شهروندان احداث می‌شود.
#بدرقه_یار
@TV_Fori</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/665696" target="_blank">📅 20:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665695">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87d68fa36a.mp4?token=rQLqHoyR9zCAcqUdcDckccMsvkx81KY3AcOnCtAbI6m-KTLCBUH3lDJGteMxBsZSJa-49WAvL64q3CVSBm_cI9seNhxSPo9mDiGp-q5S6LdW3Es_TIGU0bkZlzKVTMPPfT3-_ujWvjTtYfzN2CQYrXkLVUUHob4B6qqkuYfIzoQOPlfql4jfqmBy3Z9xhamBspzatK79n5ypZJ1bnjfUy1gU9J2c3lJLJZu7FnlMdYwAhdgbjJEJJAFVSb-zlg9t7Fm64727MYCAukQT_jJgwRcCsURvuuInoacxP-uxa1Q8k2p7IksG7HzXpxtkcMnHWIY7AFCC92TBw09yEGhxbIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87d68fa36a.mp4?token=rQLqHoyR9zCAcqUdcDckccMsvkx81KY3AcOnCtAbI6m-KTLCBUH3lDJGteMxBsZSJa-49WAvL64q3CVSBm_cI9seNhxSPo9mDiGp-q5S6LdW3Es_TIGU0bkZlzKVTMPPfT3-_ujWvjTtYfzN2CQYrXkLVUUHob4B6qqkuYfIzoQOPlfql4jfqmBy3Z9xhamBspzatK79n5ypZJ1bnjfUy1gU9J2c3lJLJZu7FnlMdYwAhdgbjJEJJAFVSb-zlg9t7Fm64727MYCAukQT_jJgwRcCsURvuuInoacxP-uxa1Q8k2p7IksG7HzXpxtkcMnHWIY7AFCC92TBw09yEGhxbIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خانه آنشرلی در دنیای واقعی
✨
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/665695" target="_blank">📅 20:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665694">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3f1f62805.mp4?token=TGKdsWLTQ53l5NjQbnMNh7FI_k5PqE7WmjmvZq3ArLPn96ddsPvOKvHsLNXrCNJUVM_ei60UCxAY9_OUVjb8SSOetnn48e8VadmfTq1TZbUpx0agdBc7XHCFjLgIwPmh9rPYUAESCAxUTkaphlzgOrgn1LcHlhTixxFxtaRd0KdQa6I9MCJsDfEr4LZJgjvRHO0K-uLrniSpkBNeocidaQ9goMC0mLzdGSQXq709592CrwqJHUdMOXbfsW1ECBHIpR357Lvn86tGqWehv8PhGSJ50fd1gkf83YhfEB7HYsZGahK6DC8JkhHOVVNlr4SY6AgO-bmG09IxXvIfuahUQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3f1f62805.mp4?token=TGKdsWLTQ53l5NjQbnMNh7FI_k5PqE7WmjmvZq3ArLPn96ddsPvOKvHsLNXrCNJUVM_ei60UCxAY9_OUVjb8SSOetnn48e8VadmfTq1TZbUpx0agdBc7XHCFjLgIwPmh9rPYUAESCAxUTkaphlzgOrgn1LcHlhTixxFxtaRd0KdQa6I9MCJsDfEr4LZJgjvRHO0K-uLrniSpkBNeocidaQ9goMC0mLzdGSQXq709592CrwqJHUdMOXbfsW1ECBHIpR357Lvn86tGqWehv8PhGSJ50fd1gkf83YhfEB7HYsZGahK6DC8JkhHOVVNlr4SY6AgO-bmG09IxXvIfuahUQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: در شورای‌عای امنیت ملی از ۱۳ نفر ۱۲ نفر نه‌تنها به تفاهم رأی دادند، بلکه از آن دفاع هم کردند
رئیس‌جمهور:
🔹
هیچ گناهی بالاتر از اختلاف و تفرقه نیست؛ من خیلی حرف دارم که می‌توانم بزنم ولی وحدت مهم‌تر از این حرف‌هاست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/665694" target="_blank">📅 20:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665692">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
چرا او از بازگشت به دنیا پشیمان شد؟
🔹
00:07:10 عدم اجازه ورود به هاله‌ای از نور
🔹
00:13:50 سوختن دردناک چشم و دهان با گرمای سوزان
🔹
00:26:00 درک شرایط فرزند سقط شده در برزخ
🔹
00:33:10 امر و ابلاغ به ملک‌الموت برای بازگرداندن من به دنیا
🔹
00:45:50 هم نوایی تمام ذرات هستی با بیان مفاهیم قرآنی
🔹
00:49:20 زنجیره‌ای از عشق میان اجرام آسمانی
🔹
00:53:10 درک عمیقی از تاریکی و موجودات اعماق دریا
🔹
01:14:10 مطلع بودن من از محرمانه‌های نظامی همسرم را برانگیخته کرد
🔹
قسمت بیست‌وهفتم (مرز نور)، فصل چهارم
🔹
#تجربه‌گر
: زهره ابراهیمی
#زندگی_پس_از_زندگی
#فصل_چهارم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/665692" target="_blank">📅 20:31 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665690">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KRBXiGgdHGR_o5UWiEPhvOjcc_ysxbgUiu8N8TY7yMMNtCavPKbl3KvUquUMeaoOZrYmFGR7N4fcSMYLOcS6YTPOrGzTIjH9nrMlfaq5hf1MSg61VuKO9oqTdWC9USr6lhvQnEdItGznvkKba2vIVE3KyIdvAi2Wv4DOI5EzjS2qziRnnhNt0nLXHC2vlJJUSahX5MP2jJCCUbJL8XHb_jWq45vTFRP0Bkwl2d93JkBFirHZH7eD7Xc-y1a3ATvrIx3m4olKeetoaYOSpfUuF0ria9Eq1x-BUI8doVkJSFni1EHXC5xiS8NhtHjs6MvQkXMgAze48emI_K_HNa1Oqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری | کمپین «جامانده»
🔹
اگر به هر دلیل امکان حضور در مراسم تشییع را ندارید و میخواهید در این مراسم حضور داشته باشید، یک فایل صوتی حداکثر ۱۵ ثانیه‌ای برای خبرفوری ارسال کنید تا یک همراهِ قلبی به نیابت از شما در مراسم شرکت کند.
🔹
در پیام صوتی، فقط نام خود، نام شهر محل سکونت و جمله‌ای کوتاه درباره همراهی و ادای احترام خود را بیان کنید.
🔹
منتخبی از پیام‌های صوتی ارسالی با عنوان «جامانده» در خبرفوری منتشر خواهد شد.
#بدرقه_یار
🔸
ویس خود را برای ما ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/665690" target="_blank">📅 20:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665689">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e6305f707.mp4?token=vRPhI25xG74dHEPBZP3sYCvesqCQGRidTdCwyS1ZbmzCDDTzPSDO_3I3K55-zTjQNPLzEvw0CNPfdfZcTfTDkNrQd8PPmudBlA3KZPBvaTzop3Z6_WxlqehBnblQI0XesvZV56CiQMnTkm8rp7lUZB1FlQRGrqYN3wT47rcHkPEnPOsW7QEhVJN64Su2RUC41J4oGGvV1izs2VMuqDASGm1BUoZSVsZHLIRuSVjRCWWOGnjDaZH8DBnPmQ9VoCLoP2YksEGFE8OwSU6bMLqL6oY5Lc7YUy3UpMMdobwfBdaDNkjyoNBQUWiLXUhxll2yWlfTXaL7SvUYWmI6XyOT9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e6305f707.mp4?token=vRPhI25xG74dHEPBZP3sYCvesqCQGRidTdCwyS1ZbmzCDDTzPSDO_3I3K55-zTjQNPLzEvw0CNPfdfZcTfTDkNrQd8PPmudBlA3KZPBvaTzop3Z6_WxlqehBnblQI0XesvZV56CiQMnTkm8rp7lUZB1FlQRGrqYN3wT47rcHkPEnPOsW7QEhVJN64Su2RUC41J4oGGvV1izs2VMuqDASGm1BUoZSVsZHLIRuSVjRCWWOGnjDaZH8DBnPmQ9VoCLoP2YksEGFE8OwSU6bMLqL6oY5Lc7YUy3UpMMdobwfBdaDNkjyoNBQUWiLXUhxll2yWlfTXaL7SvUYWmI6XyOT9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: من به عنوان مسئول دولت نمی‌توانم ببینم مردم مشکل دارند و بگویم همه چیز خوب است
🔹
در مقابل دشمن کوتاه نخواهیم آمد، تا پای جان می‌ایستیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/665689" target="_blank">📅 20:23 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665688">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GKS_XuxM-NkXNRH8TR3tVU-rgmowr7NTMOZegOIgWlKf0wQi0WWTZZ9dyIz5dwtiuR9uRZ3UH8KTfzsq9wPngLmYj3zL696jVlF204_UWBsx6jZxjULISOuZzzd-OfWZUW7Qp2fHJHThSL69G9p6T8sA04sG0UDOW3IGvQG8aMR24D9E_Hk_l5gZ4COTZQLlfqS_870Ti6xzFOuydgXxmA34mf5QdxErmXBUirbdnlSCqNrzTSDcjow6OA2un_iwtmZeJzugDd59ldW0uk6RaxlFn-46EycbVDe1xemdl223UyhkkCvDUCfcLvbmsyJdKMXGhq28-mkl4t3K1L3OGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
همه چیز درباره عملیات بزرگ بغداد/ چگونه تریلیون‌ها دلار دزدیده شد؟/ مطالبی عجیب از بزرگترین اختلاس خاورمیانه
🔹
در میان متهمان، فردی بازداشت شده که همسرش به‌تنهایی یک ملک ۵ میلیون دلاری در حومه دبی خریداری کرده بود، و دیگری بیش از ۵۰ قطعه زمین و آپارتمان به نام خود و فرزندانش ثبت کرده است.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3227390</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/665688" target="_blank">📅 20:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665687">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
همه با هم با افتخار میزبان مهمانان رهبر شهید که مهمانان ایران هستند باشیم
🔹
گپ و گفتی با مردم مبعوث شده؛ حاضری برای میزبانی میهمانان مراسم تشییع آقای شهید ایران چیکار کنی؟
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/665687" target="_blank">📅 20:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665685">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81adfe9f60.mp4?token=SCRog0JFZ44JaMeyENWhD6X8J5rmJOpQccR8QqWfctZlfTBumlfXRHieHlfzSRqp9rGMPZq6nQTco78T7wpdkoT7wrMIhcKhpmPDvaOwCVWnS2_K_egJ7NaJm-Xr1yHS7jpH4eU6ntjEmDLWaziDJSgYH9IoA8Cw5xNWFGAV6K-YWQ1ruQ_xlMGyPAoIC87pidIRqj_HqnfKfXV-a92Bs-bhT2uCGdveC5ZrGQ_Zm3y2VhaqL_alJmnkpMQuqMETohysnJgPaWTQ4BPa3FwztHk2C_z09OVFvhVbox5ehbEV6y28MY66hCpTmMTYhe7Gc2fhNX47CVDVYQ4-xbBiwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81adfe9f60.mp4?token=SCRog0JFZ44JaMeyENWhD6X8J5rmJOpQccR8QqWfctZlfTBumlfXRHieHlfzSRqp9rGMPZq6nQTco78T7wpdkoT7wrMIhcKhpmPDvaOwCVWnS2_K_egJ7NaJm-Xr1yHS7jpH4eU6ntjEmDLWaziDJSgYH9IoA8Cw5xNWFGAV6K-YWQ1ruQ_xlMGyPAoIC87pidIRqj_HqnfKfXV-a92Bs-bhT2uCGdveC5ZrGQ_Zm3y2VhaqL_alJmnkpMQuqMETohysnJgPaWTQ4BPa3FwztHk2C_z09OVFvhVbox5ehbEV6y28MY66hCpTmMTYhe7Gc2fhNX47CVDVYQ4-xbBiwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وضعیت عجیب آشپز سابق صداوسیما؛
وقتی کودک بودم لباس‌های دخترانه می‌پوشیدم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/665685" target="_blank">📅 20:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665684">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0539c154ff.mp4?token=rwlfdRo-UQe_yByaZ6ZV55Tt1siD34BxI7huMQYA5h36X2ju8rvN0g7-Z8KKZcE0oatAK239edEDSR6t44tO9OLBxxfk4IuMNug4FjjfHAEK-Nj4fcNR7cIglkaqG2Bs0iRQXMWSUCmGxAXt1iaUu0lfZ0a0B2T-qNZUbMY6tSrGB6wc9ql2qU7gSEngVjzA2YyhRe2gCQz7iWhfFJ_zW3nW7DVeXmzUUWpgGKGwqTgdv8VsmVcNb5GP_9naUIjv5QoZuOrRuVerR5PkWNNfwFKqvP0XIXmH0aTRklMVMyIjMW2bAUueutXWeLWnWG7Ua8KPEgFCD1MfSaW6hW0LV0loklyf9acaMR9FctkpP4XWw_1fgzPq5WFGCwbd874QhNPQw75EzIPcTHr4s7HhPPVtlIFa7MFwkKilmHUoL-Je1ajPH3iv7PND-O96BaB3OnUQfdzGvkczVp3ExFY03Q7XxVyDsAfNEvefeKURUPCqpnxmJh7g-AEVrQZVUQpJc3EoqaRoiLU8fCRYzHtFgzd1Xv9WWwe_kBFp3Si8I_E-Ks6i8JlnOWV5XV-TkmUrI3qdJbEtt6bOmwTc8U-yRCrVuxG66927Uj58H9DC80oVBFSyZ3kwyceBhvTr0cHh-U0hP-PQwjmwZqLhF_78F1T60uUyixFsPp5sdvv5hCk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0539c154ff.mp4?token=rwlfdRo-UQe_yByaZ6ZV55Tt1siD34BxI7huMQYA5h36X2ju8rvN0g7-Z8KKZcE0oatAK239edEDSR6t44tO9OLBxxfk4IuMNug4FjjfHAEK-Nj4fcNR7cIglkaqG2Bs0iRQXMWSUCmGxAXt1iaUu0lfZ0a0B2T-qNZUbMY6tSrGB6wc9ql2qU7gSEngVjzA2YyhRe2gCQz7iWhfFJ_zW3nW7DVeXmzUUWpgGKGwqTgdv8VsmVcNb5GP_9naUIjv5QoZuOrRuVerR5PkWNNfwFKqvP0XIXmH0aTRklMVMyIjMW2bAUueutXWeLWnWG7Ua8KPEgFCD1MfSaW6hW0LV0loklyf9acaMR9FctkpP4XWw_1fgzPq5WFGCwbd874QhNPQw75EzIPcTHr4s7HhPPVtlIFa7MFwkKilmHUoL-Je1ajPH3iv7PND-O96BaB3OnUQfdzGvkczVp3ExFY03Q7XxVyDsAfNEvefeKURUPCqpnxmJh7g-AEVrQZVUQpJc3EoqaRoiLU8fCRYzHtFgzd1Xv9WWwe_kBFp3Si8I_E-Ks6i8JlnOWV5XV-TkmUrI3qdJbEtt6bOmwTc8U-yRCrVuxG66927Uj58H9DC80oVBFSyZ3kwyceBhvTr0cHh-U0hP-PQwjmwZqLhF_78F1T60uUyixFsPp5sdvv5hCk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرگ تدریجی امپراتوری آمریکا از زبان تحلیلگر امنیت ملی آمریکا!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/665684" target="_blank">📅 20:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665683">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">محکم در آغوشم بگیر.pdf</div>
  <div class="tg-doc-extra">39 MB</div>
</div>
<a href="https://t.me/akhbarefori/665683" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
فایل کتاب محکم در آغوشم بگیر
#فوری_کتاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/665683" target="_blank">📅 19:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665681">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IiKQROxgQymi4eTRkl_wS-FHZ0TSA1s92GlThO4asVkw0pMc3XW21XnhQ9Q2JlMRmmIIARcprULK3A6nCLuZcr9rSOSU8h1vAAcBpr4TjnMh17-hNjrLTdwwBNIkk0gzjmtkvPHpqEQbnCWepnIMoKwBE1s5TrQTRiVvNpUPJ3OyMwZA57Yw0i2ZstqIpFJ1BnR17UcMmUYdtce3CrFVyxrhnPE7QK-aTwQIhDk8RnjZkMeVUNxmU20arxiaVxrdD51-4w3hi-ezGoQTxMUr2y6ouCYNX6nRqRX6I8mGiDmN__UIP3j-7veqimXCAQxwMW1pID_1SOPEPPu1Koz90g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y892wUHbzrfFxYp6b7sbPA3B0WDIXL5VxotEl3dYKL-DZ7A0gDO0fM5EefQk-n4egCxuYhrNS1juMCo4LKhX0SHxwaveba2Fv_pNWxi1cubNDWFrZ4IEinfaxVJlXSRvU1RcFV2WtsD1BulfbM-61-xWFuF8GR_ZH5juIxuU1aSCLuqudRPaJf_uY0HOZo4aBnI-ljYoSh1iLsFJMpYYJ_0ryZPulB-bZvzGgrZ_wcUap8JGSrBgDFLQBwRvqVc2jPtYl_JIxPHVZ7hpL9eE_fqYEYmgYHQ3tUm0LNyNKCpd5kx-0A_asL3eQx62QMdXtq38sNEYWZRZqqZtDlaknA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اگر رابطه‌ات سرد شده و نمی‌دانی چرا، این کتاب جواب خیلی از سؤال‌هایت را می‌دهد!
🔹
«محکم در آغوشم بگیر» اثر سو جانسون، یکی از تأثیرگذارترین کتاب‌های روان‌شناسی روابط عاطفی است. نویسنده نشان می‌دهد ریشه بیشتر اختلاف‌های زوج‌ها، کمبود دلبستگی و احساس امنیت است نه نداشتن عشق. کتاب با مثال‌های واقعی و راهکارهای عملی، مسیر بازسازی اعتماد، صمیمیت و رابطه‌ای عمیق‌تر را آموزش می‌دهد.
#فوری_کتاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/akhbarefori/665681" target="_blank">📅 19:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665680">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
ایروانی: محاصره دریایی مجازات جمعی است
ایروانی در پاسخ به ادعاهای آمریکا:
🔹
جلوگیری از ورود کشتی‌ها «مجازات جمعی» است و تأکید کرد میزان حمایت مردمی از حاکمیت ایران در مراسم تشییع آیت‌الله خامنه‌ای آشکار خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/665680" target="_blank">📅 19:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665678">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EEqAGXXTZOmYsHu3suroRe4qV-ieaZmN5opPXahCOXkpy51MpHl9028KFNIa955wq6JLuV7UsuWlJleS5OkGLoxwvUOq_H7Zbminj4KlKUnbPnMkTquLtJUuzKWPIU_JEe1RCKkIbu-BNJIIlfj9DgF_iviTeIdzqtRqB9w7-BTvG_9GT3G8z4_a87qQc9GXtEFxvtCOJqIaCUtoROUE26sjbLTBBDa55AW96MdCqjgWDcUWCi--Wfg5Kb8wsfsKJEcsfme3dR4vtrssT69Xa80Wb2vwuvR3hc1QBQ5W6KKzDMq8nJ5atA5W-Rhxvf0fnkk_p26-y6BoiU7wQ1kJfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حضور سردار وحیدی در مصلی تهران
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/665678" target="_blank">📅 19:41 · 11 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
