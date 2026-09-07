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
<img src="https://cdn4.telesco.pe/file/qv0zHbFY8WTyRl5HgTZnlUKwbG-AfVRELkqLCWAB3zXRVAUCgw81BUV1NhqjpcKdxfK7g3RFj3IGQm9CLEe4io5rvN9KI3kRF0IEonhUtDiN1V63P6PxnBCVvDoyvnWe_3Q8hKkdP06mTszOxfa84PBN5FgIk7B9cRq3JgCj3cLNI-cK0MKqQPoe-Qrd5capcZBMHutNnIgFK3Bop36PLZdls-Mte7CUhzuEbA0dU7qE5Y2hRXe5LhgR1kz6S3LFASkrpJAndUobZzZ6rKraxKKLrWjMeyxwpcGx2KG_XYyz_b9cQBfowkT50Umxp6kI-j5_ayVTAe4FqnokEWrEfQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 112K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-16 08:58:46</div>
<hr>

<div class="tg-post" id="msg-71220">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71220" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/news_hut/71220" target="_blank">📅 00:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71219">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_dX66uuWYUSmLfbvOrsPm-bsW1QvFAfKGCqu7_nBdLDK9aMJrYauLiiioCCD80mvD4WNG5uJ0NYSyw2WdWwgd8cTP4TWmh2q7rca66QXoptbLRgWcybuhAQi1gh6OvQzzWZrg67tGFfqZmjE6Cg2bGgSEKKoMYg28YB8xGddViDO-wM9H8jBKP8qvH5bKrwPxnJmrDemh1oeQD-Nm_GShvdSd8BuhgxvDNsgrjqEEbFi0cNLv6fuDEo1dhRd62U0q7Lt-ll97_lYk5SJuJlmMm3SdvtuyduK0kwDl2tAr_9ixw_abOJmu1WBR_vWJO4HqSxBAz-a_OU5D2eD2fw6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
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
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/news_hut/71219" target="_blank">📅 00:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71214">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eKnuvqtAN5pl67Li7FFAmn6_xoNmotiwmxg-DIno9MZSVQ1tBa5At9p52LFlAmCbQTiD6rTD3TYudWBJfMHLVfnsKwoAZBVw_g_8okQahVcePrO8C9fh-ZkeKlA09Ui7SLVvvk8AF9j0zWnu9x4BTF0Pd4D2hDGgwiYiqpKV6m0cXyZb0qn8F5GTtQvH4tZ24NOh38fTh1wsS-qvoK8Bt-b8H1qCYnD53EyYsHAFHpJf1rKoWzszbCfNzuBDxDT3UM3m3aIfkVNwkOf-Y-LJolHQ3_ZoVxQYZYxrtIi8pyUmu7nndiZ2SEAFZMO9mzsqfEl4xnhVroLCp69v2t_jzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ohUa1UStQbOEl4Ro8-q6FAPo0g5Wbm6N9kDYCRB9QGmnCg7SzSYM-JZgxuR9UuLorRa62HRWZEhni_N7SglgaZlYX3VaVwISqJaAKfi8HysFhtCgJps6oVR9WrH8fCZfCTrJXve5XjR_bwVyW-DtltD1z5LxYJBwmQ8KKLsN_F9EaZAH8PVGhkFYe7PucabOUAYH07HKTptEMAt5yxsy-_lqr1yonXPd2gjnJ_IwCTe2LdK-3m-V5YuyfnWncUfxjHfN8D7FNaGn92gLRwGabRYMmDqkx-lNiP597iotuig3G7xVcxXftULNZc541n5NAjtYKV9KbNDoZimEkiqkFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a2TtLjdllkED_i0NlqGAp1v_t2kwZp8hahZ727HGxrTXEqcKyTPCr_XMRqYGCpN1WfdonjyY3FhcrJ3OmViq5Nv2nI1iH4TURL02IqGdFPtC3F3acriBFcrjOqyPl5XjftNL5rBBXbg_y1f3uGq5c7y4E2vU9mnc2CandtR2ipXdcCPjNUC7OZyAKOpi2At8_l4C01UbZJDNeDtHN4SpNmv7k5hwvPqbE0VuFAA5wjHdkoI168efqynYa4Uik-naEFXD5YCKievtc7aPEQOsHZzpk8z2CgP6Mdq1UB7V8JIvlIYwnNtnQHWpEPm430qEsi42IjfYJs-43tce8OuBJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WGWS3Y67BrLnbh_WFijd1p23o2o1TF6oAD-PMEeXzZYBbpb1G23zu4Lel-bCxm5XRk6JuS8gdBosNxUsPJRJtcqtXVzC5dWh6VWuq32Neowb-Ah20NiE87V5WkRx2T9LlNkGC2SDQW34zQsZn3lBmSZBKlyEEkYN3ojxiaaiohlsxrIAlSoGF5pHEpTaq7A3Vvl33ERaATCUPx93u4HxcOANpjFMkXnr7-1a6QgOU298rnwWMz77CBBhlZ4qSiH2DBapJCC7OayOg8ImsF6Lbv8ms0ZMs64hugzfyCSGwDkg4IPUGWLom7eCQb5A9xHOhYLocxhvyWj_E6kMauNmSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sPCKOJTdLND3wPmtZHWpEzQiPqJ8JPsGX16uhURstXoE2qVPzGYtAikdhnofXE0dGyza0LaDsb9AOsgcsbOWW2-SvF0UhrorsnXXKFZZTdDXKptKmGeHm6dmGBfVpnYCiDRRUGGaso48qVcLyUiarlQ7_JO9p6oShx2m8SSwLxbPVs1vUB30a0rRtcrdYjVYu8T6fwxIMoy8XSTVR2z-2tZBSx-X1lhSp5-noBZIszr6tkcpVWJIzjRxGsWbnPnIns21dLCwap4BP9toNMZkZLn5rQnckih5-_S7cfp8jcRjU9V7IKHw1NKtaQqpIgClNdAi0L9-PgCMCr0I6nkbMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
ترامپ:
۱_ایران کشوری در حال فروپاشی‌ست.
۲_خداحافظ جزیره خارک.
۳_ارزش پول ایران از بین رفته است.
۴_صادرات نفت ایران به شدت در حال سقوط است.
۵_ حجم‌های نفت هرمز به سطح قبلی بازگشته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/news_hut/71214" target="_blank">📅 00:28 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71210">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eWXjQ6Bl6OFQmGv1lt67WzMgjKiscDkHLfw2U_Tt76xwYisPHztLsgPL5eExf_LfWs1XuOT-N4NT4w33kMR79w7jpKq-7myqFfT5S2gN3PwfKKKcggiNCSWwfzMNGpU13aLbDxUUnZBPY-atUlQ2dYA6qZINt8dBASrepIHE9fDh3qQc-SOevvmtuNWN8qEK5BHnUdS4XWM51Pc3ToHosbJKvNqPkDuuSOkz2DxoZKhvpPci3pvb7sckmU_fEkRFbAg59gosfJk86A9rt4Eb97HPsYy1KLd5hSlJV_yXhFf-pBBgEw_95N24qbTbaHZjBpAhLEwBA1FxdR0ihpFWPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eK-WUBAL-agDyyVeKy22WIlfaQzDbY2AJuhS_Uhs8f4VPdGTEKSI-q01_eOyCdD3olXUusebXvbj_4KxzK11JhVmvoGyGhKbakwigRXSpKo4l58NN0Xv_B1k9np58NR8xDhL8saNItwGzWeXv81y0m_55KLv9NiqE0VarsQdc76UQ9JZr5szECQ-b3kZhyTYxfZl8H397Q53Dzrnxw73W9VLhVMYkAdh8as0Bnj6GVPnZGThYhK-93pV_aLVLk-hIjjAitniwmWURB3IvOMMViGjg_G3O7TyERMv1om-7CCtGg27HLg4ado5vvuWCfW1Rn-xn02PhchnHmMsZyahKw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری که ترامپ در تروث سوشال منتشر کرده
😟
@News_Hut</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/71210" target="_blank">📅 00:09 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71209">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bca8942d62.mp4?token=EHFUEtfZduXDWPSMApuL0aBEPEHrX4pZ8i2dnSY9FpoH5kBiJ4pkEjxPmJJfS9t9IIS5gdWpjJnkYjjocXO9DHtgPMgiNplQlJ8EKgmxCKRJ7TByXUHni5Tszj7b6YXi7DRgaD1pitCpMpgLGtXZjo_kyJrahEIesQYw2bXF77pzmhUyWGkGwh3FmXNrVfU55rb6r1mU26vQQtNU1Xe5Y0xobbioci1L1ACo9ukurhz71BjIW1WR7BFOPW2C-_HtX0Pp9A_qBtCxCdHkUhM42w20hLksXcHcoxsqwFzJ33V8VQ5ZYZa6BbtamLveEt3dXtbl8TpAM3QnaYTDeQ1eQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bca8942d62.mp4?token=EHFUEtfZduXDWPSMApuL0aBEPEHrX4pZ8i2dnSY9FpoH5kBiJ4pkEjxPmJJfS9t9IIS5gdWpjJnkYjjocXO9DHtgPMgiNplQlJ8EKgmxCKRJ7TByXUHni5Tszj7b6YXi7DRgaD1pitCpMpgLGtXZjo_kyJrahEIesQYw2bXF77pzmhUyWGkGwh3FmXNrVfU55rb6r1mU26vQQtNU1Xe5Y0xobbioci1L1ACo9ukurhz71BjIW1WR7BFOPW2C-_HtX0Pp9A_qBtCxCdHkUhM42w20hLksXcHcoxsqwFzJ33V8VQ5ZYZa6BbtamLveEt3dXtbl8TpAM3QnaYTDeQ1eQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
دو عدد سیب زمینی 100 هزار تومان؛ اینکه قیمت یه دونه سیب زمینی بزرگ‌ به ۵۰ هزار تومن رسیده‌؛ یعنی فاجعه اقتصادی.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/71209" target="_blank">📅 23:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71208">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a65cbcd011.mp4?token=pHzcDFK7vb6XBTWYxnWoZBHr-7h8ncBZsjSaPHeoTa9N2b5lz53MTesj6TE3L9PxiOj15YbGjsmwun2DMOsIhCA-U9-cl9mR1GhHGWrUnWcqD_rURjMGfIHKbXKParYIN332S1ZRrSOSgUy2u62x1AZfAgRbBiz2WdE88MlYWOLHAfVM65nQ7ACFl7aEC5qtz7GLTFEzAV41Whq942pZhP4fCdMwPsmpBxBN0GhCo-XTK_VQ6-XxdJpDRaol2iCJf55p4jnlVsiVH8Aor7sz95Qvs3AbjDjClpuZIyMnyfBogAi0XFY9w0uLodnGJBSYXiZ-KNNCz9UvJ7-R0qD2aA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a65cbcd011.mp4?token=pHzcDFK7vb6XBTWYxnWoZBHr-7h8ncBZsjSaPHeoTa9N2b5lz53MTesj6TE3L9PxiOj15YbGjsmwun2DMOsIhCA-U9-cl9mR1GhHGWrUnWcqD_rURjMGfIHKbXKParYIN332S1ZRrSOSgUy2u62x1AZfAgRbBiz2WdE88MlYWOLHAfVM65nQ7ACFl7aEC5qtz7GLTFEzAV41Whq942pZhP4fCdMwPsmpBxBN0GhCo-XTK_VQ6-XxdJpDRaol2iCJf55p4jnlVsiVH8Aor7sz95Qvs3AbjDjClpuZIyMnyfBogAi0XFY9w0uLodnGJBSYXiZ-KNNCz9UvJ7-R0qD2aA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سعید لیلاز، اقتصاددان و کارشناس اقتصادی:
«کشور با تذبذب و دودلی، مس‌مس کردن و فس‌فس کردن  اداره نمی‌شود و حکومت باید تصمیم‌های قاطع بگیرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/71208" target="_blank">📅 22:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71207">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qEBXEUvRmlw86s5Vw-GxC14JmXlPtzkCHFmQv4kAMfVkCFo-s-krO6H0a15uRCxeZ6R_DE1-D9lxNF68UDO2MFdcN4ZtG3hmQExhngqF9Dm-R5OQyIJwE4urk6UoW443aeU5PAQE22eX2pI1mHeZ4zBqKkVlKkoty33WAP75JcmbqYOVe7K5ZGAngglLoG2W4cb1Odhe5brYj7JvwFEqZ_FONMez4lEYQpleeCYGZz_6OEpOd2g8lixdAeFl9N3Vg1ABl0AUPkaJH6Wbi34Rd0lSZWMwFgjKM5f_r2LsfZ8iLyaTY7OMGdKAr5WmGumXkwWV0qE27YdmSsP1F4Izaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ در تروث که اومده کلشو جای نقشه ایران گذاشته
😟
😟
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/71207" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71206">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6400639d7.mp4?token=DGVfqA9P-2l6Ft0TS6-hx9ZUs1MvB2KfAQuCuNF81DfssG-ycGa9J84tGHuxH0Qd1FjdVPUANdOYzP_eGipHjTyAh-2SpooYUkFzHwflvY9JAQiUzMP0Wkshqtw3pggX7IBXd_JhSkvtDKb9oS9aQ18GwTin5FwhImVXowCIMbiFdj3vJf_UaQRpTsxGhB0vC1k2CWEgpqbcvU-ucYmuYLXlEwUsP_-67BJs9BaKhZfgE3IBEgvBcKkdJQBD3MveW4zgjOlGMnPSdO_ztiZyvYLLRzblOqg7LPZ3-ZDv6yQAlYN8stKOCQZbTb1kHTtz7fxsuOudmR9TMbXLNxSXGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6400639d7.mp4?token=DGVfqA9P-2l6Ft0TS6-hx9ZUs1MvB2KfAQuCuNF81DfssG-ycGa9J84tGHuxH0Qd1FjdVPUANdOYzP_eGipHjTyAh-2SpooYUkFzHwflvY9JAQiUzMP0Wkshqtw3pggX7IBXd_JhSkvtDKb9oS9aQ18GwTin5FwhImVXowCIMbiFdj3vJf_UaQRpTsxGhB0vC1k2CWEgpqbcvU-ucYmuYLXlEwUsP_-67BJs9BaKhZfgE3IBEgvBcKkdJQBD3MveW4zgjOlGMnPSdO_ztiZyvYLLRzblOqg7LPZ3-ZDv6yQAlYN8stKOCQZbTb1kHTtz7fxsuOudmR9TMbXLNxSXGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
مجری لبنانی:
مجتبی خامنه‌ای، رهبر عالی و ولی‌فقیه، اگر به بیروت بیاید باید بداند که هویت ما عربی است، نه فارسی.
بگذارید این را به روشنی دریابد: اینجا بیروت است، نه تهران؛
اینجا پایتختی عربی و آزاد است و هرگز به پایتختی فارسی بدل نخواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71206" target="_blank">📅 21:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71205">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
⭕️
#فوری
؛ نرخ سوم بنزین تغییر کرد
سخنگوی دولت: نرخ کارت جایگاه سوخت از بامداد سه‌شنبه به ۱۰ هزار تومان افزایش خواهد یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71205" target="_blank">📅 21:13 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71201">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O2YseL0kAXk99M1o8Q1fEwWA2Xc8nwLzVsnBqsveJoqjbcXdo1N_FtzepdsYiGfumcrho2R1WvLyVdx_fL9K0vC_ljznLnTV1ANDvMFao7TcUM3J04Hwo1uaaHPJcfXJP27RwY2VZK5ztRz38VmUNL2ICUgGTd-cqmvDkInBR-WqOn8gQnj9oJDprGRy80nRgLKNA-Ec8ROoU9_x62LTfHFLhFbQ0rL5s8Oo1DvbcRMyvw7YieRz2KOvJGiR7Ak8W4TxslQZW9v4QOHD3rkit6vozZwW__TTA2p5uQCV30WQJO-RjLnlJ9_CPrMlg9MHnKOJqPLByy2Njjayuq3NJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BzjJAxlueh9m-oIY44YGDioqrRjhtco0Tfb8qSJKIiafryf_RbwLGVBvYx_M_CJ3CotMJSP_iCPXzjQzerrY7mJl82RfFn7J7sYnQlsXo8F5sj0hBy5vxHjcPFk9MPErGOwjQF6aD7vlAQ6dnc0SsFW5BKIcPU5MBI10pE95UVoalZm2SVPYl3uUzBGwXZX5H6GCx0iCE22L0o6je-vRQzIQM8VsLXserz8sBQ-G4Z55mDEjCYj4Y4TECrDqymqcw-eTfKfVLfGBv6QJ2SbsLjlrVLUHIKEZlG8b-2GhxOQ3EkqXhtLfoBZtJ5Ek0dkGtVumW0cFTn9hhNd1KcG8GQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98460c35d8.mp4?token=cY36qWDIkcS3UIl-PyA-j91I7H_HKAE8u_TOz3iQL1mUs0lhCdC1GQlL84QmKCMIr1rJvHPgayKtt4mB9nkhSmK6vOF-UBXWPscxLus9uiwV2EGejicoSZrauEuQr_k8LXYKa4fG4u-GElw7kwaL77eyoy_AV0boJ3GDt9jQWTNg6FpnXNdpLkSrJBvWjnOMENjoUDte_rPm84L27aLtW-I6IOt-5VTPKywgPn6qXDjvQBN1BasmQ_pG1Wz3HLVOSN3b_yq2QVe41nHP-y-JHrvrdMU0XfntanvqcfOvstm0QnortDpHekDb-TfjHq7p-_d6YwJMGxWRTTgFLo1qTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98460c35d8.mp4?token=cY36qWDIkcS3UIl-PyA-j91I7H_HKAE8u_TOz3iQL1mUs0lhCdC1GQlL84QmKCMIr1rJvHPgayKtt4mB9nkhSmK6vOF-UBXWPscxLus9uiwV2EGejicoSZrauEuQr_k8LXYKa4fG4u-GElw7kwaL77eyoy_AV0boJ3GDt9jQWTNg6FpnXNdpLkSrJBvWjnOMENjoUDte_rPm84L27aLtW-I6IOt-5VTPKywgPn6qXDjvQBN1BasmQ_pG1Wz3HLVOSN3b_yq2QVe41nHP-y-JHrvrdMU0XfntanvqcfOvstm0QnortDpHekDb-TfjHq7p-_d6YwJMGxWRTTgFLo1qTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
🇱🇧
حملات شبانه جنگنده های اسرائیلی به ارتفاعات علی الطاهر و نبطیه الفوقا در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71201" target="_blank">📅 20:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71200">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a237cee509.mp4?token=VvhekB5CYjsJHaIzsInK7WoTiGtIRTnNlNoH3f9L-A2WTAzlq8bblpodTd2iq4tb_UZssGoaH0WxYNYcVY29uBQKIz3wvlfmVBRc1RIepXBagrq_xsFOjRn-bmokZdmkX9-ZuWTpGcL-46bODnvWJI4BNz2jT6vY8bbzMOzUT6r8msaqc-bL62ahcX-Aswf6Y9hEB55IjOpECXDmAB4_5opSTll0RDmCY5nzmaRPxtJ0ljamw-SW8M4hBz2LzfKrfi9sCTxaW31xp-ciRW_bk91U1z6-lr8f3vftT5LNGRJZeUE7DstS8NfF2yUlnVotw4ZoaAWNpy0JwTscNQuakg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a237cee509.mp4?token=VvhekB5CYjsJHaIzsInK7WoTiGtIRTnNlNoH3f9L-A2WTAzlq8bblpodTd2iq4tb_UZssGoaH0WxYNYcVY29uBQKIz3wvlfmVBRc1RIepXBagrq_xsFOjRn-bmokZdmkX9-ZuWTpGcL-46bODnvWJI4BNz2jT6vY8bbzMOzUT6r8msaqc-bL62ahcX-Aswf6Y9hEB55IjOpECXDmAB4_5opSTll0RDmCY5nzmaRPxtJ0ljamw-SW8M4hBz2LzfKrfi9sCTxaW31xp-ciRW_bk91U1z6-lr8f3vftT5LNGRJZeUE7DstS8NfF2yUlnVotw4ZoaAWNpy0JwTscNQuakg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
زاکانی:از وصیت‌نامه علی خامنه‌ای خبری نیست، احتمالا در بمباران از بین رفته.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71200" target="_blank">📅 20:15 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71199">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90305378ee.mp4?token=FUzlLnKc86Yn730gVui_s_g3clg_jiW_35ML7UH7nqvgYDQ--ta-uKIFUvHV1dB8UJplGrak82iOEpCFZRsLib7mvLm6IBI6gy6b_s6eX0M39EawizpUZPKEYiXpBwfroie9tIbkdBayqKuGHkrZbHbJeiL0OzzsE-i2ELiotAwrganey2qokIyvbPE3CRM5Zrat55kqAvEqSt0Xh3jyHrkdrc_UJa9XNNubMyMBNirVKkjBQFJBeKTpf3Oi2WQxqoNLA1Sa5SLyjfWWEhxZ2oMdGrWYumJ4T5NZNX50sxl3cMQdOj1OgS6r7MeP6o6LAKTqPNKuMaL6YdoYVdomtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90305378ee.mp4?token=FUzlLnKc86Yn730gVui_s_g3clg_jiW_35ML7UH7nqvgYDQ--ta-uKIFUvHV1dB8UJplGrak82iOEpCFZRsLib7mvLm6IBI6gy6b_s6eX0M39EawizpUZPKEYiXpBwfroie9tIbkdBayqKuGHkrZbHbJeiL0OzzsE-i2ELiotAwrganey2qokIyvbPE3CRM5Zrat55kqAvEqSt0Xh3jyHrkdrc_UJa9XNNubMyMBNirVKkjBQFJBeKTpf3Oi2WQxqoNLA1Sa5SLyjfWWEhxZ2oMdGrWYumJ4T5NZNX50sxl3cMQdOj1OgS6r7MeP6o6LAKTqPNKuMaL6YdoYVdomtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇵🇰
بلاتکلیفی بیش از یک‌هفته‌ای صدها راننده ترانزیت ایرانی در نقطه صفر مرزی پاکستان
این سنگین‌سواران ١۴ شهریور در ویدیویی گفتند که بی آب، غذا و امکانات بهداشتی به حال خود رها شده‌اند. با اتمام سوخت یخچال‌ها، بارهای فاسدشدنی در آستانه نابودی است و گمرک هیچ‌یک از دو کشور پاسخگو نیست
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71199" target="_blank">📅 19:32 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71198">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">بیناموسا مگه نگفتین از امروز برق نمی‌ره؟ رفت که
#hjAly‌</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71198" target="_blank">📅 19:06 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71197">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd3aa09393.mp4?token=R32tAAZRpyoBYDUbqMVi7gNTcD245QLMIo4edxsH48cNcWbAlKoDOg-6G69L_EQxbJ85PoHjut7YjdAbUtU6pWBqx8VBjj9XKyRQCTqnILXoH34a2G4mu9oq6BT9LwFHu9Xp5pz3b1T3MBBXBy_HX3sJJcfAL2ZooTKpH9COmF63yD1E8b4103mID3HfqcOiQQ7Nqlfp_0DyVdTI9aRB9PP8XzqNDK6RFnSdoiQRxS2KeQlePVX0QCPE2tYnCfX_GCqds0FUjrROZXsePlQer2WwxmIah6sXgq26jom4p6uOPzBsPHSQjwxF6IzdPo8OJtmfbDXQm1wjMgaZjBuk9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd3aa09393.mp4?token=R32tAAZRpyoBYDUbqMVi7gNTcD245QLMIo4edxsH48cNcWbAlKoDOg-6G69L_EQxbJ85PoHjut7YjdAbUtU6pWBqx8VBjj9XKyRQCTqnILXoH34a2G4mu9oq6BT9LwFHu9Xp5pz3b1T3MBBXBy_HX3sJJcfAL2ZooTKpH9COmF63yD1E8b4103mID3HfqcOiQQ7Nqlfp_0DyVdTI9aRB9PP8XzqNDK6RFnSdoiQRxS2KeQlePVX0QCPE2tYnCfX_GCqds0FUjrROZXsePlQer2WwxmIah6sXgq26jom4p6uOPzBsPHSQjwxF6IzdPo8OJtmfbDXQm1wjMgaZjBuk9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نخست‌وزیر نتانیاهو درباره ایران:
پایان این رژیم در ایران نزدیک است.
این رژیم ضعیف است، برای بقای خود می‌جنگد، متزلزل شده است و هنوز مأموریتی ناتمام باقی مانده که ما مصمم به انجام آن هستیم.
این امر در نهایت چهره خاورمیانه و مسیر تاریخ را تغییر خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71197" target="_blank">📅 19:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71196">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djTvA5MEvOW-qWoGwfTs9MZHjV4Fch2b9wnA1X3kRPUaxUvLkBiFqF-95hUpBrqsWPg_LO4onSbZ7RWi6xNLHvMNPJBE3ia63DzWYn7-xR-dxTolLRysrLFbaHmrv8b4d_4POlqtbLDURexDrxTa-HNMuwWh3zbnqJ5LIpjGFDZsMsvdWTCSL3Wfjm7xCnRzdh3FGpB2s4xpDRN5ZJydpHDYqABAyQTMCetWHhKhZ-VYpgqq9TRQGHqPkVs3RO2jAGZGt9CpRdMUGjEMwKUclL3FLX3egzo566mlQSgPJ1VJOcTkEmkJWXQPQY3ZxPYRGIX3PWCK9P1KV1FuiSE04Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
دیس قالیباف به بسنت:
چرخ‌ها آماده. گرم کردن قبل از پرتاب:
دیزل ATH: فروش فوری
بزرگترین طلبکار شما: موفق باشید با Yentervention++
80میلیارد دلار کاهش می‌دهد: نام نروژ را به Americaway تغییر دهید
استخدام کم: بدهی به خدمات با DO[Israel's]W، طبق گفته عروسک‌گردان‌های شما
اوه. طرح نقطه‌ای فدرال رزرو قرمز چشمک می‌زند
😁
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71196" target="_blank">📅 18:55 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71195">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hensaTYEqShBYACGNK9bo5CVRgCUIwQBY5dOcwoMvh3WIQat91XJh9xH_-POnkM95R-CyuJMs8sdQDFQLRt54dHvSbkxmgQb9K9Rzwl8kvOlMc3UR3o0SBc1reGTSHd9Hh4v0uitpwm0fk6KDrhZe-weS86vV24zhusbU23OJq-Ab8CbqXwq-Jf7LIcQf80Y2MY06gZ4pP3E_VEcczcry40QH8nohVYigQ-1hCOyZiBeDT3WpN2VKaXZ23BFLcZ2gSLxpdAbt1S6ChRv_2wAvNfYj0EzMYeuWCyrYp0_FG_QGnesy7uiWTuwjFuyiPkCr4DdGJSkqcu5OJkLgXRCJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
گویا املاکی موهاشو رنگ کرده
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71195" target="_blank">📅 18:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71193">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NbDx5bgKnUZ3ub3MqzE7Py9q2pRAKpkJu5usPjHdqz8jrcsylTfB_zMvuOnZ6pxeuExtz9ZyZ9CdNluW8Z4YeCZ_MlUXYXKET7vs_M-JJ_MGV8YHQXZ2TN2XjUKSpxdjbi_dVkPLbu7bB-LMlv5yHsGVZSCsNAzdHHlXnbrNRVIwH5tzCtdwwUs9pxcBIQKZvWGvuTGa0jtOp4oQJsM118cOlPI_UtKYwuf_6r81GCwzzi5L_1qSM7xgvSISERiOdoMwPgva4VnoD2zHutw-1f1THtNuc4Q7kuklh8Hn8bfih2sF_QNc9FgpQX6HbaAiCYvtrR_uWxlPRmK_PguG3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/385d0bbd1a.mp4?token=KJSkWwcJX-dLigCvCeCSsnKMtOrjPlNp-aN_jJrh8hFffBtF5D4mHYugxcoPmS8k6q2HAzLKrX28rYNPGum4u2swq9C2nhSKW1UqEzDyyBGFpV1I5HyxCStevlqaedaCUwuYEyRQK8Uh1aUQGj3OQ1pKldNDdlHQLA_xn-Ws5DWQ5bFnhK42fn_za2_h45VVz95V9Pzf1m37xbDNo3oI6zfR-hyx9nFj5y6Uth6_7DTRg2vaUjN2_HDHND89xoyUlUtjajDJKrABRZGd1SC1Wt0sEHJdssXqLaPzpSdhiHl-oRmAkURNUIoOEEEAemEApuZKbOHnRkddyUUFQ9kqHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/385d0bbd1a.mp4?token=KJSkWwcJX-dLigCvCeCSsnKMtOrjPlNp-aN_jJrh8hFffBtF5D4mHYugxcoPmS8k6q2HAzLKrX28rYNPGum4u2swq9C2nhSKW1UqEzDyyBGFpV1I5HyxCStevlqaedaCUwuYEyRQK8Uh1aUQGj3OQ1pKldNDdlHQLA_xn-Ws5DWQ5bFnhK42fn_za2_h45VVz95V9Pzf1m37xbDNo3oI6zfR-hyx9nFj5y6Uth6_7DTRg2vaUjN2_HDHND89xoyUlUtjajDJKrABRZGd1SC1Wt0sEHJdssXqLaPzpSdhiHl-oRmAkURNUIoOEEEAemEApuZKbOHnRkddyUUFQ9kqHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
تو همه جای جهان هوش مصنوعی داره جای آدما رو میگیره ولی تو ایران برعکسه
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71193" target="_blank">📅 18:13 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71192">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa47cd6f21.mp4?token=Z2u-76JdrCUDSpBAXxFuU1f5DYpY47JxNNGcWWeuGaWGXNqP62rEA6jBBRx8V2U959pHYcyIzIFPk2Ea3etdaKe_3GtZXHSXzmcBSMc_WW6lGKWrVbDuHsibRtOgv2NWUXLYOEXebtLer7xLpnM241MonXnVP4KewdAPBbAgmzTqXlA0F-tJiktjVT4d6L0bMHZISlpX4n-a1fAtjrhbalq2ieOTWWYaVKL21TzXIZyUvxZVIqTxcEMKK_mpgBxKsKWxCoLZvm7T8eJYuRb5JKn8VgjsYuq8WWLyVcdwqyHjsVa24pVJzEscUtsUSStzZtQ1ZG5ABW9sy9fSfmOQkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa47cd6f21.mp4?token=Z2u-76JdrCUDSpBAXxFuU1f5DYpY47JxNNGcWWeuGaWGXNqP62rEA6jBBRx8V2U959pHYcyIzIFPk2Ea3etdaKe_3GtZXHSXzmcBSMc_WW6lGKWrVbDuHsibRtOgv2NWUXLYOEXebtLer7xLpnM241MonXnVP4KewdAPBbAgmzTqXlA0F-tJiktjVT4d6L0bMHZISlpX4n-a1fAtjrhbalq2ieOTWWYaVKL21TzXIZyUvxZVIqTxcEMKK_mpgBxKsKWxCoLZvm7T8eJYuRb5JKn8VgjsYuq8WWLyVcdwqyHjsVa24pVJzEscUtsUSStzZtQ1ZG5ABW9sy9fSfmOQkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دعوای دو تا ترنس تو پارک لاله تهران!
فقط آخرش
😐
😐
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71192" target="_blank">📅 17:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71191">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb7600cfd5.mp4?token=OyW40qeJseGlmc8KGz8kuwUjtrK9sMZ-H1vX9CcRTt_RKVMozqhlhnokdRG2vI_7skmVDLpHlgYEfcjIm_CjjC-2supoEQxJfu5-ejAgqVoEWFoEW0TgZEANs7niMRDi--MGQNWdSbQJ27_BDLeAw7OIYpZnZjnv40IDilb4OtSGfB7dGufcZXPiNQV8kXw42_O5oOILDsxHaOAgUOxWIuVMXsw0XXBLxWXAE_I-4mBdvyWRZU299G9o30u3eIIUxLLTKzVlXVt-hnzeLrHt0IzZBkwP4x8jmqUB9vIGaxAK0Cop9RWnX9wOK0Ta5YHRma2SKc1DLt5UUfQcA1glDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb7600cfd5.mp4?token=OyW40qeJseGlmc8KGz8kuwUjtrK9sMZ-H1vX9CcRTt_RKVMozqhlhnokdRG2vI_7skmVDLpHlgYEfcjIm_CjjC-2supoEQxJfu5-ejAgqVoEWFoEW0TgZEANs7niMRDi--MGQNWdSbQJ27_BDLeAw7OIYpZnZjnv40IDilb4OtSGfB7dGufcZXPiNQV8kXw42_O5oOILDsxHaOAgUOxWIuVMXsw0XXBLxWXAE_I-4mBdvyWRZU299G9o30u3eIIUxLLTKzVlXVt-hnzeLrHt0IzZBkwP4x8jmqUB9vIGaxAK0Cop9RWnX9wOK0Ta5YHRma2SKc1DLt5UUfQcA1glDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇭
🇺🇸
وضعیت دخترای حشری تایلندی بعد دیدن پرسنل ناو هواپیمابر آبراهام لینکلن در پاتایا برای تعطیلات!
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71191" target="_blank">📅 17:02 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71190">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/45226525f2.mp4?token=VbyOKZkCccXj8XbZfctwryXesKEecflc07isw7ggjd01BBmCw_rDL7STwu8Da1Bhip6xkDvDgxnp3mgqO3apNZeF9VVtNvARv0HcpndBJJsMWuDXAkwExQwoZN3n2j_wLljSDv30xXNecsqGq8X0_vU_QaWU32InynRH1uqbSOXCsVu4_Gay3AUMhK6B1nKlcjaubobLCZgmji6xqv3zKSeePoq8kc_hwU2D2B_0nIJM9r_GGB_HAaPP5XrYrtcZkwEotQvGbZ2ObrOh6AGuJJbjWU0CafNw-iB-1A3zbYcuGFZTZtflQstUgpZz0RoLqCdQ0k1Ih_EKugRlGETHsA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/45226525f2.mp4?token=VbyOKZkCccXj8XbZfctwryXesKEecflc07isw7ggjd01BBmCw_rDL7STwu8Da1Bhip6xkDvDgxnp3mgqO3apNZeF9VVtNvARv0HcpndBJJsMWuDXAkwExQwoZN3n2j_wLljSDv30xXNecsqGq8X0_vU_QaWU32InynRH1uqbSOXCsVu4_Gay3AUMhK6B1nKlcjaubobLCZgmji6xqv3zKSeePoq8kc_hwU2D2B_0nIJM9r_GGB_HAaPP5XrYrtcZkwEotQvGbZ2ObrOh6AGuJJbjWU0CafNw-iB-1A3zbYcuGFZTZtflQstUgpZz0RoLqCdQ0k1Ih_EKugRlGETHsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
راننده ای که چند شب پیش در مشهد طرفداران حکومت رو زیر گرفت:
عمدی نبود تعادل نداشتم به یکی برخورد کردم تشنج کردم جای ترمز گاز دادم و یهویی زیر گرفتم
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71190" target="_blank">📅 16:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71189">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71189" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/71189" target="_blank">📅 16:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71188">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DPpaHh-lGkKx_zEWCUxr_Ieyl5hdSICpZbmw0Ok5VGSClkGo5FZVfnV5wOWLot09gkn1cX2jkN2lgZcW7w59nx89DyYawunnrTvhx17mw1mHNQQRmj134Ngg2itG_TI6vqMfM6fwrz6PWFWWfn2tWyDv8NY2KDtATuPvqrwqTg-6ARccp32U7-XXcaWnkj-KhRI-06i1P7HA4_Tgz0Ec_FdoSkdnscOIUSOiiDBokSA-3Ogh0ueIy3pIP3zFeESKvZgwVzO8Gc9pYXcLZJylzUxCWkyCT3QZgvXR7Z0hlVW2R3dYmAEnPjC6kqDMTeIo2oJupQ0V0flzjuzSle-ivg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بازی جذاب
⚽️
چلسی
🆚
آرسنال
⚽️
را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید.
📊
نگاهی به آمار ۲ تیم:
چلسی: ۲ بازی ۲ برد و ۷ گل زده
آرسنال: ۲ بازی ۲ برد و ۴ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71188" target="_blank">📅 16:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71187">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cU27KpZqhBXcA3sYj5wOJR7M2d39C5vA-lQfPmUc3zOiTuOC9huC9uLx5Pujnb68aTMiuyCDkMBbWbgigtm6j9KQ0S592UiY8gkf1M_3V8JQLGn21to4rSfTNneUovGz_8vs4D7hJgEFevAikO4aDDCVp0pBqSoX_g9YecqxRXhZOmeah4nYvpP1bQKbtyUax2jLRDdW9KapSTMGYS15PUhyGZjZUF_q4fiYUTIw1yHKwWzGUCeQWGCYfiEtWP60HbDDzLnVemxGjnTnN62PfQBkxQ_NT7sFhY9KBJdC9uEpG4uloCTlpMnIe7Azo2hJ71wWhKjhZiHG95PzkAcMmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇰
🇵🇰
پارلمان پاکستان برای نخستین بار در تاریخ این کشور، فرماندهی قانونی هر سه شاخه نیروهای مسلح — شامل نیروی زمینی، نیروی دریایی و نیروی هوایی — را به «عاصم منیر»، فرمانده ارتش، واگذار کرده است.
او می‌تواند بدون نیاز به تصویب کابینه، کارکنان این نیروها را بازنشسته یا اخراج کند و یا در خدمت نگه دارد.
دوره پنج‌ساله مسئولیت او دست‌کم تا سال ۲۰۳۰ ادامه خواهد داشت.
او با دریافت درجه «فیلد مارشال»، این درجه و مصونیت قانونی را مادام‌العمر حفظ خواهد کرد و برکناری‌اش مستلزم کسب رأی دو‌سوم نمایندگان پارلمان است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71187" target="_blank">📅 16:30 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71186">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22246726de.mp4?token=pl96_1ClUtH0GVZDLdPNKbUfEhYFqhy1d5toMKMxlEhqMXZtibzMloN12qAgwp61tZyWjmbyTpH5ibzUOiTJkXSPqkHf25BZCU38izfmTGKFqHqNOMoI6gcF_K7FzQDD27f3QTdqrqcjT21rxnom0YXRhCI3REvG74HZbxwC4uf1G-Yj2LEvm366FwzGwRBjX0pImQlb34JNLHZdwAQvwrc1_IAQTl3-OU2xqgfdYKsVT3nld4PyIt9SVOEhk8dlnD3ppJQgBSmnyp0wUAHvUfMVmgUNNdADJMvLhy9lkoRyeWCNo-w-WAocyAVRxkj6-FkgHUq538RnQt8U2R1rBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22246726de.mp4?token=pl96_1ClUtH0GVZDLdPNKbUfEhYFqhy1d5toMKMxlEhqMXZtibzMloN12qAgwp61tZyWjmbyTpH5ibzUOiTJkXSPqkHf25BZCU38izfmTGKFqHqNOMoI6gcF_K7FzQDD27f3QTdqrqcjT21rxnom0YXRhCI3REvG74HZbxwC4uf1G-Yj2LEvm366FwzGwRBjX0pImQlb34JNLHZdwAQvwrc1_IAQTl3-OU2xqgfdYKsVT3nld4PyIt9SVOEhk8dlnD3ppJQgBSmnyp0wUAHvUfMVmgUNNdADJMvLhy9lkoRyeWCNo-w-WAocyAVRxkj6-FkgHUq538RnQt8U2R1rBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیلم وایرال شده از ی دختر ایرانی که با یه پسر مکزیکی با هم وارد رابطه میشن و بعد از ۴ سال بالاخره به هم میرسن و باهم ازدواج میکنن.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71186" target="_blank">📅 16:01 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71185">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KWt1__7W_WkU62DTYn28DTMFhp6qCrU4_HG_aS4YpI87FriX7_VQq3UAF4OtjsngdbuRcIYusvsSViPuQ-wPSjC43KBCbel2pqyyzUFpp61lruQ2MX1vlfikpONkvvF2K4rVI10ApXnXwcdZgrrUlthNCZCxD9sAW6WP790uDXcErUi-Djco6hDlywkMeuRk2WltyBqSawdc-sVGlDrerl2FHrVRyXqQ6JqBv21Q5p_PgnWBYGJsmxrZHj0Cbdj0mBauusxJxVULVIRTUoqD_Azh_I202Wrd4GkLhy-15dsVRbrJa1vo-NKHgmKW0WnvfnhiXQ7IfvNxuyxzRqisSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
دیده شده در تجمعات شبانه:
قالیباف
:
علی الاصول یادت رفت
علی الطاهر هوا رفت
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71185" target="_blank">📅 15:30 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71184">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/64baa312ad.mp4?token=tPG1rWT3OEY1Zq_kN7pIjt7FNY4w98i0Ih0UQPCDUhw7q1OrxUq3NyUjxyJPFAvCbvFKtMIal8TSfaFb_2vKGXHqM4tyzsAkOe8O4FEeUBIKaPGKfvOsMcdzuINyhcVOW_EvxpuiI71v7846ETuoc65vOQp27XOqz67iJ2x17qbHgDbAGxA7PJZ0HT3wHr4xlLFzFAlJC4nVgkcQaybiWjD80PqECxzm5OnJmpLejHC63R_lRVO-sE9NxFfjYrJ6HSni9YfUtXyc8EuFYOYmafaoLTlswf2l0i3k5cUgB4HJuRIjaiiNMYG0dnqGPdwWfdIUqqaXnh8qWjDV8Ex4bA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/64baa312ad.mp4?token=tPG1rWT3OEY1Zq_kN7pIjt7FNY4w98i0Ih0UQPCDUhw7q1OrxUq3NyUjxyJPFAvCbvFKtMIal8TSfaFb_2vKGXHqM4tyzsAkOe8O4FEeUBIKaPGKfvOsMcdzuINyhcVOW_EvxpuiI71v7846ETuoc65vOQp27XOqz67iJ2x17qbHgDbAGxA7PJZ0HT3wHr4xlLFzFAlJC4nVgkcQaybiWjD80PqECxzm5OnJmpLejHC63R_lRVO-sE9NxFfjYrJ6HSni9YfUtXyc8EuFYOYmafaoLTlswf2l0i3k5cUgB4HJuRIjaiiNMYG0dnqGPdwWfdIUqqaXnh8qWjDV8Ex4bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدیو درباره یکی از جنبه‌های سختی مرد بودن در حال وایرال شدنه:
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71184" target="_blank">📅 15:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71183">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c325a7591.mp4?token=HGAUK3LKt60jgRqwW199bt0bN4n8GiGqAX0XBCbn1rzpSY-XhZRfHhXyzGhwScgJYcuaz9vVvbd3KPjONMtsx2yUvKENaFq9WunoVih7JkpmtLFGMk9zhCg5R_plIWKXL2sPTqxxNiqbwTdaXr_xsp5LMRarf1T4Yu60peTR6uxebTUsGPygn7qJOm0vfKIC-2fnh5kJvX27TA3OyYnLey4E2u0WlkY3Hw_S2xsd_nGs8R5J4iRLk67jq6FRaeYFW93lkpkdaEEDx-pEQCTNyXhmHBuIbt030MiMdJpKn12OUnRe9b_R-4kzZdJo-iSH1Z9AG4Z4-SXpj8T9N9z1PIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c325a7591.mp4?token=HGAUK3LKt60jgRqwW199bt0bN4n8GiGqAX0XBCbn1rzpSY-XhZRfHhXyzGhwScgJYcuaz9vVvbd3KPjONMtsx2yUvKENaFq9WunoVih7JkpmtLFGMk9zhCg5R_plIWKXL2sPTqxxNiqbwTdaXr_xsp5LMRarf1T4Yu60peTR6uxebTUsGPygn7qJOm0vfKIC-2fnh5kJvX27TA3OyYnLey4E2u0WlkY3Hw_S2xsd_nGs8R5J4iRLk67jq6FRaeYFW93lkpkdaEEDx-pEQCTNyXhmHBuIbt030MiMdJpKn12OUnRe9b_R-4kzZdJo-iSH1Z9AG4Z4-SXpj8T9N9z1PIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مراد ویسی درباره مسعود پزشکیان:
حساب اینو نکنید این متخصص قلبه. از نظر سواد اجتماعی یه آدم به شدت پرتیه پزشکیان.
گفته کارمند‌های دولتو داریم صحبت می‌کنیم در سراسر شهرها، نیان تو شهرها. مثلاً اگر کارمند بانک‌اند اولین بانکی که اونجا هستن برن تو بانک بشینن کار کنن. اگر کارمند تامین اجتماعی‌اند اولین شعبه تامین اجتماعی که هست برن اونجا کار کنن
😟
گفته دو میلیون خودرو میاد کارمند ما اگر یه میلیون از این کارمندها رو بگیم روزانه نیان سر کار تعطیل کنیم اداره رو یا بگیم اولین اداره‌ای که می‌بینن برن اونجا بشینن کار کنن.
گفته یه میلیون خودرو هرکدوم روزی بیست لیتر مصرف می‌کنن یه میلیون ضربدر بیست لیتر می‌شه بیست میلیون لیتر مسئله بنزین حل می‌شه
🧠
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71183" target="_blank">📅 14:32 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71181">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c318eb355.mp4?token=A85KxOo6R-xC4QJZJxkWQgIMBtFpCy7Bhd9VdBLlaERcBcDCzUpwIdO05_K20LxJmR42Po9juNKMkS4A6EYf5wu_AbnhLLXCq7wUgiPopi4rfnINl6QMQtRJvu3Xocimiq-NJhnBxOKVgBMP4x74aUM37r0C9bA8Za1gjOFVU9sOXg9U8kxwZE2t14UzhhaPkJudzTnXrKzdl-FBx4IlOgKhBUA8XAoZnPBKeqE2Jl4oKpUwGFrEj4-Xoff-BiIbRcQw9NuvwQlDw0hClT9CvgPJbgcC11w3vUOJpk8CqdN-Lbp04AePM_4km-hnyGuyN5fXUjblgiovO67htug8pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c318eb355.mp4?token=A85KxOo6R-xC4QJZJxkWQgIMBtFpCy7Bhd9VdBLlaERcBcDCzUpwIdO05_K20LxJmR42Po9juNKMkS4A6EYf5wu_AbnhLLXCq7wUgiPopi4rfnINl6QMQtRJvu3Xocimiq-NJhnBxOKVgBMP4x74aUM37r0C9bA8Za1gjOFVU9sOXg9U8kxwZE2t14UzhhaPkJudzTnXrKzdl-FBx4IlOgKhBUA8XAoZnPBKeqE2Jl4oKpUwGFrEj4-Xoff-BiIbRcQw9NuvwQlDw0hClT9CvgPJbgcC11w3vUOJpk8CqdN-Lbp04AePM_4km-hnyGuyN5fXUjblgiovO67htug8pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇭
〰️
ناو هواپیمابر «یو‌اس‌اس آبراهام لینکلن» (CVN-72) اسکله C-0 در بندر «لائم چابانگ» واقع در استان چونبوری تایلند را ترک کرد و مسیر خود را در عرض اقیانوس آرام به سوی پایگاه اصلی‌اش در سن‌دیگو در پیش گرفت.
خروج این ناو در صبح روز ۶ سپتامبر، به توقفِ حدوداً چهارروزه‌ای که از ۲ سپتامبر آغاز شده بود پایان داد و مرحله بعدیِ مسیر بازگشت آن به ایالات متحده را رقم زد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71181" target="_blank">📅 13:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71180">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/003437fd92.mp4?token=ooCAVwne7Qd5Km6TmeSO7BF8cD0Kp3f_hNAvFmAXSi4pou-xPHkPK7k2sj2HzhX3iiXdNlsfRgvLWAyDc0-qPlDbz5Wy_9WIkzKhrvargjLjJWO2htjV4sjKn8LdMm6SSBeyOidEFjAvRdaNzLn4v4lhBF-_SHms966rV5SyijpQhDG4cvusqy3Dv2jszbUjvMNz_t_8HSS6evcUUPyOayKWe7un8_ESTQTNqeH27VgBlTLXfeAi3PEzDUHXZJ-RbHMRAvtjMz98W3ibcCKbG_Q2g2GyBJbDvIg0K1rrpFicFtWu1WsL4-8bKchr4rDBIXYy5AGkF8TyRXWX1ak24Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/003437fd92.mp4?token=ooCAVwne7Qd5Km6TmeSO7BF8cD0Kp3f_hNAvFmAXSi4pou-xPHkPK7k2sj2HzhX3iiXdNlsfRgvLWAyDc0-qPlDbz5Wy_9WIkzKhrvargjLjJWO2htjV4sjKn8LdMm6SSBeyOidEFjAvRdaNzLn4v4lhBF-_SHms966rV5SyijpQhDG4cvusqy3Dv2jszbUjvMNz_t_8HSS6evcUUPyOayKWe7un8_ESTQTNqeH27VgBlTLXfeAi3PEzDUHXZJ-RbHMRAvtjMz98W3ibcCKbG_Q2g2GyBJbDvIg0K1rrpFicFtWu1WsL4-8bKchr4rDBIXYy5AGkF8TyRXWX1ak24Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
توی ایتا و روبیکا، ناو جرالد فورد رو بمبارون و غرق کردن
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71180" target="_blank">📅 13:53 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71179">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71179" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71179" target="_blank">📅 13:52 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71178">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LAqV7O73hxiwA6uETAiAHSEdTZ74FNtKjaJIWVYNbh-H-fWc7yAKbT1m2WnTS4IRw83F4h-GVbYnnkzSm_u7z_qzrpuOwQlKqGFsbtCnuokSVWA2c4IysNyRPE91VXKMxZvdIywd4gpfgofQYp7dnWlRgmxb15NJ_croS2TwpOabKgr6ouXLWtbWiu66cLsfYVAvqmq6Mxdte-Me3IyDwpqryGXWQ4KaWYSFK8aGIYbSxch4KxHQ8CETrxeKfAjKnOgde6Mn5pS0Nif4i4TRb8pJ03Ou2HhlSUGxxOAjmaUR0ZXzGjKGGjdSN6GxFkvmpRK3p_bwJix4XIbGpun86g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
پیش‌بینی کنید
.
اورتون
🆚
منچستریونایتد
آرسنال
🆚
چلسی
آلومینیوم
🆚
استقلال
والنسیا
🆚
بارسلونا
یوونتوس
🆚
میلان
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز و برداشت آسان و امن
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71178" target="_blank">📅 13:52 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71177">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3c6743716.mp4?token=sXyiLkwBqBmvsW6rJgjkC0gKLcz4k1TDprXoUEyTeh3O5TubNyU-11kmjoy4ITvTsLMwoBDlrfSRAZCezADYYSqjuYGrgRgAePdQJpfUvX8J8CXEHau2aMtrNKoWB4jIJAULfpRcpRhoJv9w4By50BBd_KEO3yTkwAa3AtLl9kMcdSC8AtPkUOoZOLiQvPNv9q2_ygwzbRyAZvRWs0s6SiupXsxi7fJG3TpTIvk4sEw25lAVfsFsD9-BkgyMBCtF7oDQu6hhKoOkM589VgnIeu7_Ty9nJIvdLbZ6pW8waqtB93gMbv_dXP40o3OmaWFwtQ-hDVofWB_pv5LWXQBy5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3c6743716.mp4?token=sXyiLkwBqBmvsW6rJgjkC0gKLcz4k1TDprXoUEyTeh3O5TubNyU-11kmjoy4ITvTsLMwoBDlrfSRAZCezADYYSqjuYGrgRgAePdQJpfUvX8J8CXEHau2aMtrNKoWB4jIJAULfpRcpRhoJv9w4By50BBd_KEO3yTkwAa3AtLl9kMcdSC8AtPkUOoZOLiQvPNv9q2_ygwzbRyAZvRWs0s6SiupXsxi7fJG3TpTIvk4sEw25lAVfsFsD9-BkgyMBCtF7oDQu6hhKoOkM589VgnIeu7_Ty9nJIvdLbZ6pW8waqtB93gMbv_dXP40o3OmaWFwtQ-hDVofWB_pv5LWXQBy5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">〰️
سنتکام ویدئو غرق شدن نفتکش ایرانی در دریای عمان را منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71177" target="_blank">📅 13:12 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71176">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">⏺
🇮🇷
قالیباف:
آمریکایی‌ها باید دریافته باشند که دوران «پاسخ‌های متناسب» به سر آمده است.
حملات ما به پایگاه‌های متجاوزان تنها یک آغاز بود.
قواعد بازی تغییر کرده است.
از این پس، هرگونه تجاوز به منافع ایران، پاسخی سریع‌تر، سنگین‌تر و دردناک‌تر در پی خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71176" target="_blank">📅 12:44 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71175">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20d5a31326.mp4?token=eT6yE4cJ5VlK7nZ2EykSbgum-cplWZzQ_74IrD52rNAxVp2EYfOy9X-GcLh83k1rz0Eiktg7OAQ7PixXBL_SbjM7F0MfZnM_qZ1xqK_LluFDDhlMXnV6N0tlZrI2qwJh91KBG5y2JIHCJz7VxW8THI5zVTkts5NjYkHvYIMpbQ8Re5Fe5iNg4AKVpctKiFptxreOuv4VpzZUT5k-zPZx9FC2-qYEUT52cHNkckz7SPIUJE48Fo7i2Da4YRdAIXdazH2jXa-skbSxGAcm4wpp_VUGN2ykvhzX-fsu3ctPtoA-0FfM3jPxq4cYhULeHBPHkALjgVGda2e5FBJn7kvkog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20d5a31326.mp4?token=eT6yE4cJ5VlK7nZ2EykSbgum-cplWZzQ_74IrD52rNAxVp2EYfOy9X-GcLh83k1rz0Eiktg7OAQ7PixXBL_SbjM7F0MfZnM_qZ1xqK_LluFDDhlMXnV6N0tlZrI2qwJh91KBG5y2JIHCJz7VxW8THI5zVTkts5NjYkHvYIMpbQ8Re5Fe5iNg4AKVpctKiFptxreOuv4VpzZUT5k-zPZx9FC2-qYEUT52cHNkckz7SPIUJE48Fo7i2Da4YRdAIXdazH2jXa-skbSxGAcm4wpp_VUGN2ykvhzX-fsu3ctPtoA-0FfM3jPxq4cYhULeHBPHkALjgVGda2e5FBJn7kvkog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
قالیباف:بستن تنگه هرمز به ضرر ایران شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71175" target="_blank">📅 12:01 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71174">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8313313bb.mp4?token=D2stdFqt5EY9jjv2pdf6YSpCG5cQntnKkz894o1Q3A6wGyzRf1zsOVxDwvkGAAxo8mrpDxmJLOnE94Qe2-TQkdS-iq30IBAKsWWTQZk3JKbhH7p_YKzLTCR49gQaWSLFQfYcpFGRzx6t3KiMAr1NbzMuwGfftpCHBd26wv8GBD2wqc84jm_xwVmhmMkxYFZx6AJLnpMeq02EugVBT4bAV3KwX1tml79AQzPv6oYktGvbu6V4sgwEgslxacs1WQGj0FV6yOHnb9tm_B-RewIR4cYz-Qd7TkDiSXihmZk0jFdvoMd_w9yFNSPVDfmeshIazHDc779JsXTjT3mw5URJIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8313313bb.mp4?token=D2stdFqt5EY9jjv2pdf6YSpCG5cQntnKkz894o1Q3A6wGyzRf1zsOVxDwvkGAAxo8mrpDxmJLOnE94Qe2-TQkdS-iq30IBAKsWWTQZk3JKbhH7p_YKzLTCR49gQaWSLFQfYcpFGRzx6t3KiMAr1NbzMuwGfftpCHBd26wv8GBD2wqc84jm_xwVmhmMkxYFZx6AJLnpMeq02EugVBT4bAV3KwX1tml79AQzPv6oYktGvbu6V4sgwEgslxacs1WQGj0FV6yOHnb9tm_B-RewIR4cYz-Qd7TkDiSXihmZk0jFdvoMd_w9yFNSPVDfmeshIazHDc779JsXTjT3mw5URJIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">〰️
ویدیویی که در توییتر فارسی به شدت در حال وایرال شدنه
😃
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71174" target="_blank">📅 11:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71173">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f8295abc0.mp4?token=RhTIA-A14TnlaCzcRSmSXrxY52Zfut7uVz7Q3cjDheU_G6x7EpOp2H23wk0bvyvtRiipmHnOp__NFd_HVBTjue7nkZRxc5Rvco1TPEp5Avgk1Mia9JcdQnsp6TGrPPXU0zOKRqyR3vfnB7TcWgp8ykv17NTkl5XFqfZYLkRDy6pYhpvvEca-zBLxeUtQz1oxgRI6sPlgy3QhXIyxM8Fw1M4wBHDqGF7-pQFLfBzF0tBdoolinPESbTRoM6nZY8gXIDaloNC_dVWoKxiVqxZwdt35VY2PkgoHe0zkUvJGjnlgTZ7TOOhdRf2VMoCb1SBumwys-swvPWHYA11iG9MA5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f8295abc0.mp4?token=RhTIA-A14TnlaCzcRSmSXrxY52Zfut7uVz7Q3cjDheU_G6x7EpOp2H23wk0bvyvtRiipmHnOp__NFd_HVBTjue7nkZRxc5Rvco1TPEp5Avgk1Mia9JcdQnsp6TGrPPXU0zOKRqyR3vfnB7TcWgp8ykv17NTkl5XFqfZYLkRDy6pYhpvvEca-zBLxeUtQz1oxgRI6sPlgy3QhXIyxM8Fw1M4wBHDqGF7-pQFLfBzF0tBdoolinPESbTRoM6nZY8gXIDaloNC_dVWoKxiVqxZwdt35VY2PkgoHe0zkUvJGjnlgTZ7TOOhdRf2VMoCb1SBumwys-swvPWHYA11iG9MA5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
به گفته آقای دکتر اگه می‌خوای سرطان پروستات نگیری، باید ماهی ۲۱ بار سکس کنی...!
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71173" target="_blank">📅 11:02 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71172">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b321711db4.mp4?token=lYL7NmekmMv3egqBvxMNmjNkXQueyHGnk-YhVMgCneT7DDeVWiC6CELP5BavZXXMepOWEwKlOGvkjyc8R_-yfnn_kXHTcWjZs942cP3B-DcU6h8-LPkTTOPS0CkrFhQMsMuAnEbHuuWaVETo9n6qPsTAdoudUWcmfafj4zllfYpBb7cUlQ0u-dOl0cNfy5Hq84lfb0dpLQd3iWJY_IsTdw2Cy9M42VQIm8LWjhuNip7YSIy73f5CD3fNWxHEw8MLF9So61ipXG9wiwP71EMEOeHCQ3MAGexloFOY82w5yTSnQCD6cNlU_3hwI7AxZW4QypnGOhMEjUW4hfRAr3__dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b321711db4.mp4?token=lYL7NmekmMv3egqBvxMNmjNkXQueyHGnk-YhVMgCneT7DDeVWiC6CELP5BavZXXMepOWEwKlOGvkjyc8R_-yfnn_kXHTcWjZs942cP3B-DcU6h8-LPkTTOPS0CkrFhQMsMuAnEbHuuWaVETo9n6qPsTAdoudUWcmfafj4zllfYpBb7cUlQ0u-dOl0cNfy5Hq84lfb0dpLQd3iWJY_IsTdw2Cy9M42VQIm8LWjhuNip7YSIy73f5CD3fNWxHEw8MLF9So61ipXG9wiwP71EMEOeHCQ3MAGexloFOY82w5yTSnQCD6cNlU_3hwI7AxZW4QypnGOhMEjUW4hfRAr3__dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇹🇷
این پسر بچه ارومیه ای که چند وقت پیش با ویدیوش که در حال آهنگ خوندن بود توی اینستاگرام به شدت وایرال شد حالا یه کمپانی بزرگ از ترکیه اومده و باهاش قرارداد همکاری بسته؛
فعلا این قرارداد واسه اجرای کنسرت های مختلف تو ترکیه‌ست
رئیس کمپانی میگه که این تازه اول راهه و قراره بزودی تو سراسر جهان کنسرت برگزار کنیم...
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71172" target="_blank">📅 10:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71171">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99e529d142.mp4?token=W7XMBJaLaTZJEKZKAYD6LZNPNVYBbbZT80-19KM6_ZHN-Gsh6z7Ij7brd5JORFFr_vr8WNuZ3kvmgxs9T-yNeRjOXHavyxi0qPSTncsNCAHiiYNqIThNUyInAkPcStQSzXk7SVTbKg5Rl6G5lFa3xdKsQVxOxaR6Ru-ZqbJLDdgZz2kjryi7ECwdCKGgB6ke8DjDM_p4yFPLkl5BfwLYftvh5FNYGsOk5ho40ItbfjqdYXjqxTIBb_HQhrirUcQPo3m99kf-UV_qsBV7wvDX8EEaQFctR4EUX9vu_BN6D1eXwgI8XqSgAH3fpSIvR35_pE43qwtpeVQuXBX9jUuLOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99e529d142.mp4?token=W7XMBJaLaTZJEKZKAYD6LZNPNVYBbbZT80-19KM6_ZHN-Gsh6z7Ij7brd5JORFFr_vr8WNuZ3kvmgxs9T-yNeRjOXHavyxi0qPSTncsNCAHiiYNqIThNUyInAkPcStQSzXk7SVTbKg5Rl6G5lFa3xdKsQVxOxaR6Ru-ZqbJLDdgZz2kjryi7ECwdCKGgB6ke8DjDM_p4yFPLkl5BfwLYftvh5FNYGsOk5ho40ItbfjqdYXjqxTIBb_HQhrirUcQPo3m99kf-UV_qsBV7wvDX8EEaQFctR4EUX9vu_BN6D1eXwgI8XqSgAH3fpSIvR35_pE43qwtpeVQuXBX9jUuLOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
🇱🇧
خبرنگار جمهوری اسلامی در لبنان:
اعضای سپاه پاسداران در تپه‌های علی‌الطاهر، به دلیل محاصره اسرائیل، در شرایط عاشورایی قرار دارن.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71171" target="_blank">📅 10:04 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71170">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a662811c73.mp4?token=u_SEuAqj2bv_p1PnKNGtfhfTQEkViy0Qdzf-rX_HaMNEwdpfsH58c6bCkijab7ZNn8wFRLsu3-iIcx3Ji7S_R7PLyDkSpuJ4EfDN3qs1qF-QgmCQFiRmhK8mkzBawHyDfqpMqB-4tVMDZMtrI6keXGdz-yrJhAnNbL8p7WUyANBCpwXAKAJb9Qx9_vIh9OCCWoSjBjrxQdXFpsdIZESKaimJCbV0xT8maSgdmwltaNT3gEtLWxHpGuugIjBWjR21YNe4JoO1MoOVzmbnh1jP-yLcvhqQQ1cBA0ckd9CQz1IUo9MZAgTYsYbVjvb8jPEGNdfmtfkDD7uAWLLAG2lBWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a662811c73.mp4?token=u_SEuAqj2bv_p1PnKNGtfhfTQEkViy0Qdzf-rX_HaMNEwdpfsH58c6bCkijab7ZNn8wFRLsu3-iIcx3Ji7S_R7PLyDkSpuJ4EfDN3qs1qF-QgmCQFiRmhK8mkzBawHyDfqpMqB-4tVMDZMtrI6keXGdz-yrJhAnNbL8p7WUyANBCpwXAKAJb9Qx9_vIh9OCCWoSjBjrxQdXFpsdIZESKaimJCbV0xT8maSgdmwltaNT3gEtLWxHpGuugIjBWjR21YNe4JoO1MoOVzmbnh1jP-yLcvhqQQ1cBA0ckd9CQz1IUo9MZAgTYsYbVjvb8jPEGNdfmtfkDD7uAWLLAG2lBWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
شاهین نجفی:
هرکسی رضا پهلوی رو مورد انتقادهای عجیب غریب قرار میده و میزنتش یه سرش وصل میشه به جمهوری اسلامی
اینا جوگیر شدن چهارتا شعار دادن و حرف زدن بعد دیدن اینجا خبری از سهم دهی به کسی نیست مسیرشون رو عوض کردن
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71170" target="_blank">📅 09:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71169">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2d150aea8.mp4?token=fxVr0Hbvj-8kV7NBzmnnNc3TnFi0-bM91kVbMf6UX3GfxSMg53zRTV9OBW4EUcSOSq_QQ4UBXuPeYUzY9Uip8kDiJaT6glMCSREcg8PGTQfWFSeyDqEQYD_Vb5iWsoeS9RI-UHwrW9uj5KVKQJmtI4b92VT_yky4KkYPjRzZxHes7uQ_bLZj8jBsuDAPRJwmlh7WB9JPI-u_NYYksOpZiAYRIZoI3mdcnoRVF58DMWDybqqFd94OFTh8flDSfA78Zg-vBwn_7Koa-543kmSb_dY2syiRmH4lknQTQiTwUGCGIYv_wMnM3ZUG4ICcCYmr_dr6D2sbYXWz52wmVFBRTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2d150aea8.mp4?token=fxVr0Hbvj-8kV7NBzmnnNc3TnFi0-bM91kVbMf6UX3GfxSMg53zRTV9OBW4EUcSOSq_QQ4UBXuPeYUzY9Uip8kDiJaT6glMCSREcg8PGTQfWFSeyDqEQYD_Vb5iWsoeS9RI-UHwrW9uj5KVKQJmtI4b92VT_yky4KkYPjRzZxHes7uQ_bLZj8jBsuDAPRJwmlh7WB9JPI-u_NYYksOpZiAYRIZoI3mdcnoRVF58DMWDybqqFd94OFTh8flDSfA78Zg-vBwn_7Koa-543kmSb_dY2syiRmH4lknQTQiTwUGCGIYv_wMnM3ZUG4ICcCYmr_dr6D2sbYXWz52wmVFBRTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
صداوسیما آمار رسمی کشته شدگان اسرائیل تو سه روز اول جنگ رو منتشر کرد:
۶عدد ژنرال ارشد اسرائیلی
۳۲ نفر مامور موساد و ۷۸ نفر مامور شین بت
یازده دانشمند هسته‌ای
۱۹۸ نفر افسر نیروی هوایی
۴۶۲ سرباز و ۴۲۳ نیروی ذخیره ارتش اسرائیل کشته شدند
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/71169" target="_blank">📅 09:01 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71168">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🇺🇸
🇮🇷
سپاه پاسداران انقلاب اسلامی ساعاتی قبل در بیانیه ای مدعی حمله به یک ناو هواپیمابر و یک ناوشکن آمریکایی شد و اعلام کرد که پس از این حمله اونا خسارت دیدن، ترسیدن و از منطقه فرار کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/71168" target="_blank">📅 08:02 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71167">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71167" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/71167" target="_blank">📅 01:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71166">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yqdaeb1_MW9lYrk1GsrbmNznUOJSGlSMqGL1Skmwa8p7uFPfl_haG3pcC-a_wd6IE4L3TVPC5NItADk8OYgFQkPs_NaIoM1bPsnT-njziQYBq1TWgDBV73ZOCEKg2kEuuYZFiVEXrdMETmbKY02WkjQ1FWES40nx9spfOUmXkTII3of8EnWrHOsSoCaW120eeD4BRZT1MJ5rgVat4qXE03iQbAutxT-lHraEsFQUWsWS_rKCclx4HWrE9CQ0q94qs_i0PZZYt8iJPutygGIN96tfESZ-cTjYrGGC1hJrph1Zxje9Zz7h-oeK02Pas_zC63DP7Vp9RNwiHuSeBqzqBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
تنیس US Open داغ‌تر از همیشه دنبال میشه!
🦖
مسابقات جذاب
US Open
رو در
TrexBet
پیش‌بینی کنید، هیجان رقابت‌ها رو بیشتر کنید و برای جوایز جذاب وارد رقابت بشید!
🦖
فرصت هیجان
US Open
رو از دست ندید!
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/71166" target="_blank">📅 01:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71165">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ویس فحاشی خداداد</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/news_hut/71165" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚨
🚫
فوتبال مملکت هم اوضاع جالبی داره.  خداداد عزیزی امشب کلش فوق‌العاده کیری شده و اینجوری خواهر و مادر امید عالیشاه رو به فوش کشیده
😳
😳
😳
😳
😳
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/71165" target="_blank">📅 01:04 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71163">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c0f365bbb.mp4?token=aREqeagqCg2y8lRZsNSLFtOOOFiQMJWNJffro1s28fTG4hZUZlC47wWV4jlXFp-gX5SRUBpl6VWEvbWZf4RVbEPmI47fCX2Ra_Gs83btr_RSYtAm0M4i8fVHP9cegzSwGjGd4oa-nWcjYYhU6NrYEmieeRWzLTuxjgfo_Vls6nX3cneBGvarroFwlu3iO8kxhI5blVWjgFSgGXUlBKdUmXRDIKz8PpTsVjEZnrIFoBVgFfs24E58xy8kp_mkEr-JyS7XKyuUcEF6H6FhOYlUOuuxHcQZEfCb0FWvZ3k0QZw90uyaaUjiW12yWp5LVOd03JRgvDycpEuXcEWo__500Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c0f365bbb.mp4?token=aREqeagqCg2y8lRZsNSLFtOOOFiQMJWNJffro1s28fTG4hZUZlC47wWV4jlXFp-gX5SRUBpl6VWEvbWZf4RVbEPmI47fCX2Ra_Gs83btr_RSYtAm0M4i8fVHP9cegzSwGjGd4oa-nWcjYYhU6NrYEmieeRWzLTuxjgfo_Vls6nX3cneBGvarroFwlu3iO8kxhI5blVWjgFSgGXUlBKdUmXRDIKz8PpTsVjEZnrIFoBVgFfs24E58xy8kp_mkEr-JyS7XKyuUcEF6H6FhOYlUOuuxHcQZEfCb0FWvZ3k0QZw90uyaaUjiW12yWp5LVOd03JRgvDycpEuXcEWo__500Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سپاه پاسداران تصاویری از «رصد و رهگیری شناورهای متخلف» در تنگه هرمز منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/71163" target="_blank">📅 00:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71162">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e9440ae83.mp4?token=uzDQmsYqcoSXzE-jqGoYEEuF_RMoIgxQked9VDCvOSsV-6fteA3UYX17VZuoir__gGz09BbeXS5YqIAQK9Dv1HM_q5U0qpMKFZ7QQv8a8sR2MJgH1dpkLpbLqpmQrHX0sr3n5XkJIcZ6TsujZjoj4Y96PUnqZrBZ8fZshodgEyxxotPlgMudwH0aozPlBdhmc4Gp7GcKjQskFXXCPCSmKVIQPoZGg-Jn4qTbP-txk2D0j0KelnRy1XVjKS6U8_AvSeXfCpzoIaFghIOdJqsGlq_YtuvgvRQJxInnjwGtk2vQAPgOjUIXXMCV0u6HHRskGZw0JNejVn5YQvY8VNbqyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e9440ae83.mp4?token=uzDQmsYqcoSXzE-jqGoYEEuF_RMoIgxQked9VDCvOSsV-6fteA3UYX17VZuoir__gGz09BbeXS5YqIAQK9Dv1HM_q5U0qpMKFZ7QQv8a8sR2MJgH1dpkLpbLqpmQrHX0sr3n5XkJIcZ6TsujZjoj4Y96PUnqZrBZ8fZshodgEyxxotPlgMudwH0aozPlBdhmc4Gp7GcKjQskFXXCPCSmKVIQPoZGg-Jn4qTbP-txk2D0j0KelnRy1XVjKS6U8_AvSeXfCpzoIaFghIOdJqsGlq_YtuvgvRQJxInnjwGtk2vQAPgOjUIXXMCV0u6HHRskGZw0JNejVn5YQvY8VNbqyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇬🇷
یک فروند جنگنده F-4 فانتوم نیروی هوایی یونان در جریان رویداد «هفته پرواز آتن» در پایگاه هوایی تاناگرا سقوط کرد و دو خلبان این جنگنده کشته شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/71162" target="_blank">📅 00:14 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71161">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a02f1d06a.mp4?token=rzySHiLVFOzhBOVotvagucwYDyJJEF_fVyYDLM9DFW-pxGoUapf69JOWF4vqRXLOVYksp9HZWimOyB7zdqBrcbi1v4Y31iUOIuR642a3qxG2r5tDtAWhJSudqBMBPPKUEW-Zh3RCLTJnrjjMkmXy-Tm0FOo19anqfLnYvEMYLUYkTa7aSJ4v7tBYGg9pQTJWo__ncpa2QSxgGDc7DwC5LFf8DRr9G5hdiN-0uyE24l0WdFeFTEf0XWatI8UNulzMw3YXmZVySIh4XiTHQi2MmBx47aQL3e15wfgE2KgIqLatPdX6zEYuj0zTvkAN7UzHy6EPIhWTO4-ZGS2skcClOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a02f1d06a.mp4?token=rzySHiLVFOzhBOVotvagucwYDyJJEF_fVyYDLM9DFW-pxGoUapf69JOWF4vqRXLOVYksp9HZWimOyB7zdqBrcbi1v4Y31iUOIuR642a3qxG2r5tDtAWhJSudqBMBPPKUEW-Zh3RCLTJnrjjMkmXy-Tm0FOo19anqfLnYvEMYLUYkTa7aSJ4v7tBYGg9pQTJWo__ncpa2QSxgGDc7DwC5LFf8DRr9G5hdiN-0uyE24l0WdFeFTEf0XWatI8UNulzMw3YXmZVySIh4XiTHQi2MmBx47aQL3e15wfgE2KgIqLatPdX6zEYuj0zTvkAN7UzHy6EPIhWTO4-ZGS2skcClOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
یه خانم درباره اقتصاد:
چرا مردم هر چی گرون میشه از زاویه ی آدمای متوسط بهش نگاه می‌کنن؟
خونه از ۵ میلیارد شده ۵۰ میلیارد.
گوشت از ۵۰۰ تومن شده ۴ میلیون.
سود شما چند برابر شده.
مردم از گرونیا دارن سود میکنن، مردم باید دیدگاهشون از آدمای متوسط جامعه تغییر بدن و بگن هر چی گرون میشه خب ما هم سودمونو داریم میبریم
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/71161" target="_blank">📅 23:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71160">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2d7d2ec60.mp4?token=NbvBgr-RfoDm_sGBxYTCCmzkJ-AY9YDP936lxTopI-6UuRJmW6Pn48qRogrpys_wDtkS2YKuVt-cWkKwKBEvKJAr-wrrxCmNepU5Lm_4WwM28z_NgCb5Nn-p8HcNf8Rb3KXH_MQZKeFawu9XUIfEISV-x-4odKvmu2bx0oEs0Dzddp4sfvKzC2VihehlNeBdKoIUb7AAXbPqXIqs3hQApjJvJwWxSdstlBzf8vJ-8HFraaInK5QBpX7oStAJW2hsCVxgMmQwzvvJ-ta_gDZOEykhieQvsfrEPt_u_tv585ffp9l-JP0bavklKGJH0T4jmb6qdkkPlOADe2hGcVer0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2d7d2ec60.mp4?token=NbvBgr-RfoDm_sGBxYTCCmzkJ-AY9YDP936lxTopI-6UuRJmW6Pn48qRogrpys_wDtkS2YKuVt-cWkKwKBEvKJAr-wrrxCmNepU5Lm_4WwM28z_NgCb5Nn-p8HcNf8Rb3KXH_MQZKeFawu9XUIfEISV-x-4odKvmu2bx0oEs0Dzddp4sfvKzC2VihehlNeBdKoIUb7AAXbPqXIqs3hQApjJvJwWxSdstlBzf8vJ-8HFraaInK5QBpX7oStAJW2hsCVxgMmQwzvvJ-ta_gDZOEykhieQvsfrEPt_u_tv585ffp9l-JP0bavklKGJH0T4jmb6qdkkPlOADe2hGcVer0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه جانفدای رندوم و حرکات جالبش
😃
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/71160" target="_blank">📅 22:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71159">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66b1ca1096.mp4?token=sAManY8abpIidBQyMDTtaV7fOxdFKXn3lYFhKTQgrIwEbdIMUWdeKAXix0XpN6T7vMGXKxIcbYKIB8y1_rrY5p7P5sLcQsVZNc4M00pNtoMQmSlg6gTE4inr9OJvQbq8GVo8OitY-S_Adjo0iBERWMoiHqngZrCAW_qxKPsJqJU3Tp9UicDNL85jjKGXkEyGn5xWBxDOvqznrJYsxqLK_QHddrD0N0CNiEKeAGG-YfziRt0cuiqkaWdpXWf79T-SomSQMGNAubTVvqhrouQa5WWK5aczhDqRUCT14PRNZqIjsqD1YIoUvoS26i6cbSGLbIRfeTIoFUCkEfVd7_WBoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66b1ca1096.mp4?token=sAManY8abpIidBQyMDTtaV7fOxdFKXn3lYFhKTQgrIwEbdIMUWdeKAXix0XpN6T7vMGXKxIcbYKIB8y1_rrY5p7P5sLcQsVZNc4M00pNtoMQmSlg6gTE4inr9OJvQbq8GVo8OitY-S_Adjo0iBERWMoiHqngZrCAW_qxKPsJqJU3Tp9UicDNL85jjKGXkEyGn5xWBxDOvqznrJYsxqLK_QHddrD0N0CNiEKeAGG-YfziRt0cuiqkaWdpXWf79T-SomSQMGNAubTVvqhrouQa5WWK5aczhDqRUCT14PRNZqIjsqD1YIoUvoS26i6cbSGLbIRfeTIoFUCkEfVd7_WBoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساعاتی پیش تو مسیر پلیس‌راه همدان ـ سنندج، یه ماشین سنگین گویا ترمز می‌بره و مستقیم با یه دستگاه تانکر حامل سوخت برخورد می‌کنه و یه انفجار وحشتناک رخ میده!
متاسفانه تا الان 7  جونشون رو از دست دادن...
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/71159" target="_blank">📅 22:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71158">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3aea156fe3.mp4?token=m5YqA6g14CrPObNJUXWwrnS9mU1CxfvTb_V9StTcVHO4RPnPCByCXsZI8_Wm1OkQaiTR29a8tA8jo8XlRI-XlQ36gz3MefOwG3X7HmiMdv6aO2HUTPqNhofOwbz4kxIcXUfJj29hAm1uba93Bu3OqmySQmvLkhkFvD6afWK3jSHZxiUZrShYg8G0stwcn13Mutsqk9E_MVNOS9hIu33JWMvuDyx7jnn6vD5Id6Ie0x0IrU3tWMvUjSW6P6qJeZpWsyjMJaMlcTKCv0leOfLaUXInRC00OlL8xDcJd-yJV71QY_XgXyxZ0AXcxP3axIQIvZNVIMHfsxiIU5r-vfmc_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3aea156fe3.mp4?token=m5YqA6g14CrPObNJUXWwrnS9mU1CxfvTb_V9StTcVHO4RPnPCByCXsZI8_Wm1OkQaiTR29a8tA8jo8XlRI-XlQ36gz3MefOwG3X7HmiMdv6aO2HUTPqNhofOwbz4kxIcXUfJj29hAm1uba93Bu3OqmySQmvLkhkFvD6afWK3jSHZxiUZrShYg8G0stwcn13Mutsqk9E_MVNOS9hIu33JWMvuDyx7jnn6vD5Id6Ie0x0IrU3tWMvUjSW6P6qJeZpWsyjMJaMlcTKCv0leOfLaUXInRC00OlL8xDcJd-yJV71QY_XgXyxZ0AXcxP3axIQIvZNVIMHfsxiIU5r-vfmc_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
وزیر نیرو:
دیگر قطعی برق برنامه‌ریزی‌شده نداریم
اگر مردم جایی دیدند به سامانهٔ ۱۲۱ اطلاع دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/71158" target="_blank">📅 21:42 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71157">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31160c5df1.mp4?token=ntvQanvYgHLKRhi6O0wNMzVinstxknZC4lXNj-8Ezoyhr1Dy2sYU8bvXIO_-FBTLoDzu51Virm14IbGayQMqM5qv26R_vNEsiDDZRn3WGDwcqxxFxF9XnZMMLaleHcOGzOexZjCw03ZhCq4C-vpfB6UR8b8jCJF1MrcxoHZYXWr3EnNojqisLeTjrBtYNhm1paz6xJhayn22pdPQfvuWsRnvdNjRHZkM8mYB4qgoyn4-EEFm7KtnXlvThrk4zj_bPAcXwWmBJCJD6C-jit4NtZaDJ_-jVoFmXBcMygmrPcDvUFzzgUeitd-WzR7gGPXM-1C1pvinngYANzDYOr5kDTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31160c5df1.mp4?token=ntvQanvYgHLKRhi6O0wNMzVinstxknZC4lXNj-8Ezoyhr1Dy2sYU8bvXIO_-FBTLoDzu51Virm14IbGayQMqM5qv26R_vNEsiDDZRn3WGDwcqxxFxF9XnZMMLaleHcOGzOexZjCw03ZhCq4C-vpfB6UR8b8jCJF1MrcxoHZYXWr3EnNojqisLeTjrBtYNhm1paz6xJhayn22pdPQfvuWsRnvdNjRHZkM8mYB4qgoyn4-EEFm7KtnXlvThrk4zj_bPAcXwWmBJCJD6C-jit4NtZaDJ_-jVoFmXBcMygmrPcDvUFzzgUeitd-WzR7gGPXM-1C1pvinngYANzDYOr5kDTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
جان بولتون دیپلمات آمریکایی درباره ایران:
من معتقدم — و دهه‌هاست که چنین نظری دارم — که تنها راه دستیابی به صلح و امنیت واقعی و پایدار در خاورمیانه، خلاص شدن از شر رژیم تهران است.
به گمانم حملات آمریکا و اسرائیل آسیب قابل‌توجهی به این رژیم وارد کرد.
بی‌شک ما اشتباهات زیادی مرتکب شدیم.
اما اگر اراده کنیم که درباره چگونگی انجام آن به‌درستی بیندیشیم، این هدف همچنان قابل‌تحقق است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/71157" target="_blank">📅 21:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71156">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
صداوسیما:
صدای انفجار هایی که در جزیره قشم شنیده شده مربوط به شلیک موشک ها به سمت شناور های متخلف در تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/71156" target="_blank">📅 21:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71155">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed43299c5.mp4?token=kPQLxqOzzuiM4tCVeC4eiiWuiegvj8yNAjlOb_7Ro2pPf7NzJyCh__z8EZPU1fuk9oW-Yf2iWa45NBqtH4DG8lbNdgDOczRk1iZmLhI_aOEwokOVxISkWvlvpXfMvczPNyGHj5MVAUAHBikOe2u09O-R22tTTAaYhImiEH70GgTBCbkxc4n2OZW3V1h7X4Qfhrkjs5TdE2fhTgdKa9t1eKHFSfYuX9VSPjSHHIrMDi_BRP1qW3eS1bn5DZKs63P4R5WWM6qd4soLxbOHt24G9ADXYghDOeg-UPtNCpfAvHEydNwbFXoc7VOiHkdf0WG0slrh4boCRL4pnEB-DaTCAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed43299c5.mp4?token=kPQLxqOzzuiM4tCVeC4eiiWuiegvj8yNAjlOb_7Ro2pPf7NzJyCh__z8EZPU1fuk9oW-Yf2iWa45NBqtH4DG8lbNdgDOczRk1iZmLhI_aOEwokOVxISkWvlvpXfMvczPNyGHj5MVAUAHBikOe2u09O-R22tTTAaYhImiEH70GgTBCbkxc4n2OZW3V1h7X4Qfhrkjs5TdE2fhTgdKa9t1eKHFSfYuX9VSPjSHHIrMDi_BRP1qW3eS1bn5DZKs63P4R5WWM6qd4soLxbOHt24G9ADXYghDOeg-UPtNCpfAvHEydNwbFXoc7VOiHkdf0WG0slrh4boCRL4pnEB-DaTCAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
تصاویر منتشرشده نشان می‌دهد یک کشتی کانتینربر در اسکله بوشهر تقریبا به‌طور کامل نابود شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/71155" target="_blank">📅 20:33 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71154">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
سازمان تجارت دریایی بریتانیا UKMTO:
گزارش‌ هایی مبنی بر وقوع حوادث برای چندین کشتی تجاری در شمال خلیج فارس و دریای عمان دریافت کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/71154" target="_blank">📅 19:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71153">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5717843ac.mp4?token=klLms4N-i6NXyhVT3T0oxPE26jMJBhL330MYH6uIinkzEeKYEc5N7_dJqhGGcIBGhQtMdHmlKs2FcuPv8HRIRb0KFAjtRxMimYxZFeSKjLtFYXyJpaTMKHvGcF7VYXW0iMk5yADvsfyORBfg9oQi3RVHENxdrFx7yVqLy0ws44w9doB76xyVQqOSrv2gGMJ-e6s0aVLIEabuv2l4nx0IVxQorXxh3U1zHT18o0m0U7MxB2vDA3UH0v8ysrwcW5QeD_bRyGpp4v-MocYri_DlfPD020ANoSlXvHICIg-6GpgDkJ7gbeEtUMJjSikoRhR2LAAMhfsyCTQoZS1VgUb6rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5717843ac.mp4?token=klLms4N-i6NXyhVT3T0oxPE26jMJBhL330MYH6uIinkzEeKYEc5N7_dJqhGGcIBGhQtMdHmlKs2FcuPv8HRIRb0KFAjtRxMimYxZFeSKjLtFYXyJpaTMKHvGcF7VYXW0iMk5yADvsfyORBfg9oQi3RVHENxdrFx7yVqLy0ws44w9doB76xyVQqOSrv2gGMJ-e6s0aVLIEabuv2l4nx0IVxQorXxh3U1zHT18o0m0U7MxB2vDA3UH0v8ysrwcW5QeD_bRyGpp4v-MocYri_DlfPD020ANoSlXvHICIg-6GpgDkJ7gbeEtUMJjSikoRhR2LAAMhfsyCTQoZS1VgUb6rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
✈️
ویدیویی تایید نشده از پرواز تانکر سوخت‌رسان آمریکایی به همراه دو جنگنده در آسمان جزیره کیش استان هرمزگان
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/71153" target="_blank">📅 19:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71152">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71152" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/71152" target="_blank">📅 19:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71151">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UIgqRNjwpvI53xTGI7brlyy_xzl1fq--HV7C8bMybWPUvMfNpIZqJ-vH7lPGiJDa4hHPrMNT81zHPePXHvx5RIxFdED3yqDYmQMm2YUO9ZZmkYmb-JHUkDpqtfKVg1sypmiHVPBzEAq4HjQ5Dbv2rwVfvoQA-aKoq5DQ6YXo6cbm_Owb7sDsTGuncycr42qsyUscspV89iLeTeBklYs4PGMsUc7KnLoNWR1Zh88J7t6xqh0KB-SB-btUTyWHChAFgmr-PAOMAoevHoBp9rPCadoF9T-cOuklCLiYLRQPmjmnXp5kaLYAd84zu_RQBDGV-84YNPHoPibHQOA2IbJrVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بازی جذاب اینتر
🆚
ناپولی را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید.
📊
نگاهی به آمار دو تیم:
اینتر: ۲ بازی ۲ برد و کسب و ۵ گل زده
ناپولی: ۲ بازی ۱ برد و ۱ شکست و ۳ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/71151" target="_blank">📅 19:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71150">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf5e996b2c.mp4?token=ruUvKS-e6vN0LEFQDdw1cvBQLZPMUnJULzByZORkMVtpkkY3-oQoHdWDeukpmbda1n0ZCc6E2ScZDANIGKF58MqPaXwNgiT9JAC4lEH-BQjyRW8mzarBqM5N5VkwwULw9-OdMgRy_j9Lq64Jb8WN-ClpzqDFPz0MSw2G0tHuAAhIaflexyb20WWA9QUauLOFFibZQ7GbinonertnKDXwlE0WIXNUbR1ssNq8fjs81vPZ-MwwxOm8ig_sGzxNOLOXJUsoHSManh0_LinCi1py4c3Qyoz0JAWRcmbvfma47b9J217yp1SxeVUsAUt8TlqFpB62xlfR8QlZyyLJwC2HjAxECLOaxtwmEH4UYdUN8d2qvrZfkBOfvXvcf-K56Yu_hP0waRN-nMbOrdgHucS37DLb6MS75uZ0IMyt7-6IOALt2O0Rp8Go0ccJDqw2pz4YmO4H9UOUzq_ntcTWntYo_cR3CW5JFY58M-2FzYFIoyq8FTaAQNPxYaclZMWcM0-aZPTZO1lcBmq5mlhbAedkyKl_p_K-cuSfyD0FkZJATFmH4-rSTb75vjy3hzaecYKRW9O4Gta1yXBlPi_Cvm7o1tVOw2qv5TvvbpR1MWAC6LNE146FEeZgZxkcAB9_ZbNCPyQlAlzkANwFRtOiHoOnDEhfBTByl15uLaysCVts2_I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf5e996b2c.mp4?token=ruUvKS-e6vN0LEFQDdw1cvBQLZPMUnJULzByZORkMVtpkkY3-oQoHdWDeukpmbda1n0ZCc6E2ScZDANIGKF58MqPaXwNgiT9JAC4lEH-BQjyRW8mzarBqM5N5VkwwULw9-OdMgRy_j9Lq64Jb8WN-ClpzqDFPz0MSw2G0tHuAAhIaflexyb20WWA9QUauLOFFibZQ7GbinonertnKDXwlE0WIXNUbR1ssNq8fjs81vPZ-MwwxOm8ig_sGzxNOLOXJUsoHSManh0_LinCi1py4c3Qyoz0JAWRcmbvfma47b9J217yp1SxeVUsAUt8TlqFpB62xlfR8QlZyyLJwC2HjAxECLOaxtwmEH4UYdUN8d2qvrZfkBOfvXvcf-K56Yu_hP0waRN-nMbOrdgHucS37DLb6MS75uZ0IMyt7-6IOALt2O0Rp8Go0ccJDqw2pz4YmO4H9UOUzq_ntcTWntYo_cR3CW5JFY58M-2FzYFIoyq8FTaAQNPxYaclZMWcM0-aZPTZO1lcBmq5mlhbAedkyKl_p_K-cuSfyD0FkZJATFmH4-rSTb75vjy3hzaecYKRW9O4Gta1yXBlPi_Cvm7o1tVOw2qv5TvvbpR1MWAC6LNE146FEeZgZxkcAB9_ZbNCPyQlAlzkANwFRtOiHoOnDEhfBTByl15uLaysCVts2_I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
🇮🇷
لحظه تهدید تخلیه خدمه نفتکش های جمهوری اسلامی توسط خلبان جنگنده ارتش آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/71150" target="_blank">📅 18:59 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71149">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
〰️
⭕️
سنتکام مسئولیت حمله به نفتکش های ایرانی را گردن گرفت؛  پس از شلیک موشک‌های بالستیک سپاه به سمت دو ناو جنگی آمریکا، نیروهای آمریکایی ۳ نفتکش حامل نفت خام ایران را هدف قرار داده و از کار انداختند. دو نفتکش نزدیک خارک و جاسک هدف قرار گرفتند و یک نفتکش دیگر…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71149" target="_blank">📅 18:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71148">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AGWGK5l8cH_LrVAQZ6gpNGAVIDkIsnuxKaPXB0eFg-lqPizJ_3euz2Ebs2j0IG-6e0CZ8yPOjoezoITrI4PsVf6OjrGva560a16M_ta-xU_c0nFqu9joOKXOM8bysXnuWkI7-7e-ZL4QJTcSiV_MYkmIOIheTmxmkQinu3WMtNE4d45QbPa2rnOV_9cXoOCV1nSnSiwNDG1SIGV704Z-ZKOLiHjsUUloOi-FC4T0K41krc3hstcp6HGwjRlp2QDIyrcGYOROJuGNa59O0kx4lnrRTsRkR6hT0S86SocfzaOxxZjJ8RdfUEUNVSDeZ3WreCq85XbjdHDWaayxHZFsTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
🇧🇭
سفارت ایالات متحده در بحرین:
با توجه به تنش‌ها در خاورمیانه، وضعیت امنیتی همچنان پیچیده است و احتمال تشدید غیرمنتظره اوضاع وجود دارد.
سفارت ایالات متحده به شهروندان آمریکایی یادآوری می‌کند که ایران پیش‌تر زیرساخت‌های غیرنظامی در بحرین، از جمله هتل‌های منامه، را هدف قرار داده است.
آمریکایی‌هایی که در حال حاضر در خاورمیانه حضور دارند، باید هوشیاری خود را افزایش دهند و نسبت به احتمال لغو پروازها، بسته شدن حریم هوایی و اختلال در سفرها آگاه باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71148" target="_blank">📅 18:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71147">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1d8dfb05eb.mp4?token=qH61pJDZSNOC6FDruTqwZpSMplJQGDs0oT9l0TzvvdXX8zyNrK1NjT_3sxFYbH0cGBtcGl0yc8Rb8s38g6iCOHUZbQZy0YOcucNju2zJ6cmDRAbehlcuz3tE0F_q80EggzkvnT31OOs9kZA0eMVii9IOdpMdYv-OtlDmKXGETqsBdiQ886WI005P3QMywKtI8xyLCkFgdplPBagPYJT9lC9kW8bTpFj5shqozjYD0l1Np6h0G4QZ7IqIF08U2BbVFkz4TSrJIQ5zFjFpLvyRgZn4sx97hDw-oarS03EIcYyHPks4ErFvCU8uVyfjCbpgfby55byvn422QNalNvKrBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1d8dfb05eb.mp4?token=qH61pJDZSNOC6FDruTqwZpSMplJQGDs0oT9l0TzvvdXX8zyNrK1NjT_3sxFYbH0cGBtcGl0yc8Rb8s38g6iCOHUZbQZy0YOcucNju2zJ6cmDRAbehlcuz3tE0F_q80EggzkvnT31OOs9kZA0eMVii9IOdpMdYv-OtlDmKXGETqsBdiQ886WI005P3QMywKtI8xyLCkFgdplPBagPYJT9lC9kW8bTpFj5shqozjYD0l1Np6h0G4QZ7IqIF08U2BbVFkz4TSrJIQ5zFjFpLvyRgZn4sx97hDw-oarS03EIcYyHPks4ErFvCU8uVyfjCbpgfby55byvn422QNalNvKrBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
〰️
⭕️
سنتکام مسئولیت حمله به نفتکش های ایرانی را گردن گرفت؛
پس از شلیک موشک‌های بالستیک سپاه به سمت دو ناو جنگی آمریکا، نیروهای آمریکایی ۳ نفتکش حامل نفت خام ایران را هدف قرار داده و از کار انداختند.
دو نفتکش نزدیک خارک و جاسک هدف قرار گرفتند و یک نفتکش دیگر در دریای عمان منهدم شد.
سنتکام اعلام کرد این نفتکش‌ها بخشی از شبکه تأمین مالی سپاه و نیروهای نیابتی آن بوده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71147" target="_blank">📅 17:55 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71146">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c865776e9.mp4?token=khM5ugt0EHniK1DeCrDWwWHF6yUdovfDnxngbKg2OYXQfwbOMpWMwnbUwNO-RYtX3ZdZzrGqBhRVpG7vvGx4e5_lgn4BvvEztHp3VkJ0I2u3LgHebjmHfJzC64lAGR3PoDyQGIx3SrLDSCnM4ixtpEHdRmXiifyU6vTrduJxH9Uq0jDnzfledEgIzrOt8QkZrYuzQcf6QV9o4sp8Ti8GL3OuUi1h2L8tWrtm1DrXTL_xt_EXDk-FWvBGWKqSCQekiS6wlUwFLd0vhHoCrhw3GARZBQyKf1KFlhLq4YOn5MV5YdfmgfagqKaRIR4WZ1Ooa2uovZg3ugkzmAGO7sXkzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c865776e9.mp4?token=khM5ugt0EHniK1DeCrDWwWHF6yUdovfDnxngbKg2OYXQfwbOMpWMwnbUwNO-RYtX3ZdZzrGqBhRVpG7vvGx4e5_lgn4BvvEztHp3VkJ0I2u3LgHebjmHfJzC64lAGR3PoDyQGIx3SrLDSCnM4ixtpEHdRmXiifyU6vTrduJxH9Uq0jDnzfledEgIzrOt8QkZrYuzQcf6QV9o4sp8Ti8GL3OuUi1h2L8tWrtm1DrXTL_xt_EXDk-FWvBGWKqSCQekiS6wlUwFLd0vhHoCrhw3GARZBQyKf1KFlhLq4YOn5MV5YdfmgfagqKaRIR4WZ1Ooa2uovZg3ugkzmAGO7sXkzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
حسن روحانی:
به مردم بگیم قرار ما اینه که با قدرت‌های بزرگ تا بیست سال دیگه بجنگیم.
اگه مردم قبول کردن عالیه بریم ادامه بدیم.
ولی اگه مردم نپذیرفتن و راه دیگه‌ای نشون دادن حق نداریم نادیده‌شون بگیریم.
حتی پیغمبر هم با مردم خودش مشورت می‌کرد.
تو این کشور هیچکی از جانب خدا حاکم نیست‌؛ همه به لطف رای مردم اومدن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/71146" target="_blank">📅 17:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71145">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/100451e13a.mp4?token=Kzdd35zWJFGfUyXs1HauxIBS7IlbPkY-6Z3vlt7llMxR-Jm4nvv1-DK0_UemqJLeDW-eUOUOCPR5VJcIbSwJND8WelEb9FV-nlf_mKD6w9E6sN_0rCjcRg7vwTQUN8VVzvP4fuLPZZnfGc_r7UBoIoNpFlvhUNLOUOIPqJ_ulT7c2WxzQSCXNrla7kf7PKeWWdRPni-U6CdDDYFc7rML_Kw77ZJLBlwntE3TOQ1IdHXz4OZDAjHE9x1kTUhrvk8QadnaneTJi-MuyuflvWTfrZ_v_tZxEEBbjhJPbp0Gei39-5Kp-8zKX26TH7KfmPcdV5oT2PNU6Z-z9mixeo2kxYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/100451e13a.mp4?token=Kzdd35zWJFGfUyXs1HauxIBS7IlbPkY-6Z3vlt7llMxR-Jm4nvv1-DK0_UemqJLeDW-eUOUOCPR5VJcIbSwJND8WelEb9FV-nlf_mKD6w9E6sN_0rCjcRg7vwTQUN8VVzvP4fuLPZZnfGc_r7UBoIoNpFlvhUNLOUOIPqJ_ulT7c2WxzQSCXNrla7kf7PKeWWdRPni-U6CdDDYFc7rML_Kw77ZJLBlwntE3TOQ1IdHXz4OZDAjHE9x1kTUhrvk8QadnaneTJi-MuyuflvWTfrZ_v_tZxEEBbjhJPbp0Gei39-5Kp-8zKX26TH7KfmPcdV5oT2PNU6Z-z9mixeo2kxYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
بابک زنجانی: سایپا را ۱ میلیارد دلار می‌فروختند، ۲ میلیارد پیشنهاد دادم، نفروختند
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71145" target="_blank">📅 17:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71144">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b09e3df411.mp4?token=MRwSz-7At5KoFtGYhoWMK99yYNsprDkjse16TAVJ6HgLlOq4DX1YvzevxKnhDzUWocr3wd1Mw45dN22phyQmEfgNvf68bE6FFck-X1zYVLasaEFm-h1HTZtcUBeVbYQGf_RyLpFkz9SIbEcN9CIWH66p--0COne4XmF7qTVX5-bLADBmmvc4vz4QR5iUUD_we98anlMf35A-fBXDNUmczPtr9H_gm7EyBysSoEyHoCcIhXr1CyJHNaS3CbSdfdLV4VyRWyeptc7wrmHfHxlZLqWO1uHodjWPzCYctGuzwgLGIM0V98UeP-GijQmje6Oi9l_UcBFACcVo8UjtuGykpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b09e3df411.mp4?token=MRwSz-7At5KoFtGYhoWMK99yYNsprDkjse16TAVJ6HgLlOq4DX1YvzevxKnhDzUWocr3wd1Mw45dN22phyQmEfgNvf68bE6FFck-X1zYVLasaEFm-h1HTZtcUBeVbYQGf_RyLpFkz9SIbEcN9CIWH66p--0COne4XmF7qTVX5-bLADBmmvc4vz4QR5iUUD_we98anlMf35A-fBXDNUmczPtr9H_gm7EyBysSoEyHoCcIhXr1CyJHNaS3CbSdfdLV4VyRWyeptc7wrmHfHxlZLqWO1uHodjWPzCYctGuzwgLGIM0V98UeP-GijQmje6Oi9l_UcBFACcVo8UjtuGykpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه سری ایرانیا هم انگار توی یه ایران دیگن و رفتن توی جنگلای شمال پستونک پارتی گرفتن
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71144" target="_blank">📅 16:31 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71143">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc463ce6f9.mp4?token=kKqlcvmtbTP37cYP1DB68W05MjtbeV-PvV3HGEawCu7JzmprTDA-39tvnKBSrlw5IaMqPwmCccqQPPliQBRIb1fGhLM3H_bIV4O7g0u32oGIn3ccvfov8MEyJfZh44GFeJ5Y_ARj1Ko8Xl8hX0Zltt9HJqPkMhSvZRrlvlqj3W4HDFwbHxZ4o7Zfual29mjdueBYMgnZgKHEp3Hdyf05l22F9O-PzQJkqhJJL9SwdB9smI_-QGhjj3MUz8fxcwNjZicBFVRYNtRSc3az8elH8o_MKMdGMyVG6EJ02CIih-II1WCNfKMrrcAn43w6GAZzfz7uvTPaCCqQ4fxbUSlg2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc463ce6f9.mp4?token=kKqlcvmtbTP37cYP1DB68W05MjtbeV-PvV3HGEawCu7JzmprTDA-39tvnKBSrlw5IaMqPwmCccqQPPliQBRIb1fGhLM3H_bIV4O7g0u32oGIn3ccvfov8MEyJfZh44GFeJ5Y_ARj1Ko8Xl8hX0Zltt9HJqPkMhSvZRrlvlqj3W4HDFwbHxZ4o7Zfual29mjdueBYMgnZgKHEp3Hdyf05l22F9O-PzQJkqhJJL9SwdB9smI_-QGhjj3MUz8fxcwNjZicBFVRYNtRSc3az8elH8o_MKMdGMyVG6EJ02CIih-II1WCNfKMrrcAn43w6GAZzfz7uvTPaCCqQ4fxbUSlg2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇳
تو چین یه نفر بعد ورود به مغازه‌ش که به علت نشتی پر از گاز بوده، کلید برق رو میزنه و کل مغازه میترکه ولی خوشبختانه زنده میمونه و بعد از اینکه به بیرون پرت میشه کون لختی فرار میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71143" target="_blank">📅 16:03 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71142">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9c6b59588.mp4?token=WtQJUfD4TqenWn_nAXABIPhBFCIRF06xjXFkTybTq2s6aJgMBihjVKxs8gfEbnLLsnfCKxqFvh9ZEtBhVZEdsp5h2V3X9FHm8PcKIks7g6XDKup4-Z2oSqwAM_L3vPIjdBsKmZRlERjx2RfCMu5BGOiiXoqJjAXXOy2FiAewpiLSamiod9cKjtbq9PAAYU_uTsg1_uvrN2SZ0ykb-7hObAJcmhBaRp9Ij8k95zmVpL9VEk_vhwIenmQZ5g87trArR4fyWY6uKXbFvTGyqII6Bg-opTxKQfsF2E_Bpxhn1tAKvh8eKtiXuA2yMiPPfNjHyovAZGir2I3XV3B-iK6fpzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9c6b59588.mp4?token=WtQJUfD4TqenWn_nAXABIPhBFCIRF06xjXFkTybTq2s6aJgMBihjVKxs8gfEbnLLsnfCKxqFvh9ZEtBhVZEdsp5h2V3X9FHm8PcKIks7g6XDKup4-Z2oSqwAM_L3vPIjdBsKmZRlERjx2RfCMu5BGOiiXoqJjAXXOy2FiAewpiLSamiod9cKjtbq9PAAYU_uTsg1_uvrN2SZ0ykb-7hObAJcmhBaRp9Ij8k95zmVpL9VEk_vhwIenmQZ5g87trArR4fyWY6uKXbFvTGyqII6Bg-opTxKQfsF2E_Bpxhn1tAKvh8eKtiXuA2yMiPPfNjHyovAZGir2I3XV3B-iK6fpzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
🇺🇦
🇷🇺
یک مزدور برزیلی که در درگیری‌های روسیه و اوکراین می‌جنگید، لحظه حیرت‌انگیز عبور یک تانک از روی خود را — در حالی که میان علف‌ها پنهان شده بود — ضبط و در حساب اینستاگرامش منتشر کرد
😟
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71142" target="_blank">📅 15:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71141">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f07a24e005.mp4?token=ZL_5DakOHlj6eYtnVyvjEgQMlVK9IM8sPoAlhRBdEA1c5fpYN4JClzzbOJ3W7yRZCwH_0WWizcvZJYjLnykz35eT-Ae-skM142CG7BDiHrvIaLgw_eCURbKDZjmEJJiq4RT7aZp1qW0w7TF1hMjqYYl3wVFKPQAXBeBNVt3p4kJraTwF_SLW1lZcA1ZIzRqr61jWCFg6o28QwWWswvjKhGnwn5aoKtZUQ3gRp08GGNcEF3AsuEJTqeUlnO9K4uHrpQpMoKDKnjPVVcILVtTL3QY6pQMvK9WV2MwkXkwkP947P0f8hYFVT9m8pvHPpGXX7NvOf_JxuxlV6sB9xFuUkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f07a24e005.mp4?token=ZL_5DakOHlj6eYtnVyvjEgQMlVK9IM8sPoAlhRBdEA1c5fpYN4JClzzbOJ3W7yRZCwH_0WWizcvZJYjLnykz35eT-Ae-skM142CG7BDiHrvIaLgw_eCURbKDZjmEJJiq4RT7aZp1qW0w7TF1hMjqYYl3wVFKPQAXBeBNVt3p4kJraTwF_SLW1lZcA1ZIzRqr61jWCFg6o28QwWWswvjKhGnwn5aoKtZUQ3gRp08GGNcEF3AsuEJTqeUlnO9K4uHrpQpMoKDKnjPVVcILVtTL3QY6pQMvK9WV2MwkXkwkP947P0f8hYFVT9m8pvHPpGXX7NvOf_JxuxlV6sB9xFuUkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
یه آخوند درباره شعار«تا آخوند کفن نشود این وطن وطن نشود»
؛
همونطور که رهبرمون رو شهید کردن یه آخوند دیگه جاشو گرفت
به ترامپ و نتانیاهو و منافقین داخلی میگم این حرفمو
تا آخوند شماهارو کفن نکنه ول نخواهیم کرد
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71141" target="_blank">📅 15:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71140">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">⛔️
این قبیله ای که میبینید اسمشون موکو موکو هست
؛
این قبلیه در افریقا که مثل سرخپوست ها هستن برای اینکه زنان قبیله خودشون دعوت کنن به سبک رقص های به خصوص خودشون انجام میدن
هر زنی در قبیله شون مجذوب رقص مردی بشه میره بهش میده و اصلا اینطوری نیست که کسی حتما باید زن شخص خاصی بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71140" target="_blank">📅 14:33 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71137">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca83f4e683.mp4?token=kI5HNjbGtUeF_vRazf5AAoWJzMbNiZ2GYvKmD5MjBl3nMnNx-izIZ8AP-dEUUsUim-fvdC1THyH-eFzQNFzvQaVK5QMi38ZVxqQ500QBgbigTIicWHZxscX2Zf0-fS2y86oEmLZftljE6wwQ9GpRsbuPoLGI03Djn7VmwetT1Zh6158FdBvwhx9CO3H2gd2wE2AOuvWGHPKGQBOZXCIcMZW2kPOaoBI7c86NjSP1LcwUNRlHVu2cZ4AEprhtq1me6UiMu7SusfjAdlXkNkDbCyvIMM_WpLOGaaREQSq8qI7-Ml9huy0fUA7ilZp-o33ijHzWYHGkUEvMGI9bOI40ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca83f4e683.mp4?token=kI5HNjbGtUeF_vRazf5AAoWJzMbNiZ2GYvKmD5MjBl3nMnNx-izIZ8AP-dEUUsUim-fvdC1THyH-eFzQNFzvQaVK5QMi38ZVxqQ500QBgbigTIicWHZxscX2Zf0-fS2y86oEmLZftljE6wwQ9GpRsbuPoLGI03Djn7VmwetT1Zh6158FdBvwhx9CO3H2gd2wE2AOuvWGHPKGQBOZXCIcMZW2kPOaoBI7c86NjSP1LcwUNRlHVu2cZ4AEprhtq1me6UiMu7SusfjAdlXkNkDbCyvIMM_WpLOGaaREQSq8qI7-Ml9huy0fUA7ilZp-o33ijHzWYHGkUEvMGI9bOI40ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇦
تصاویری از تورنتو کانادا بعد از بارش باران و طوفان
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71137" target="_blank">📅 13:51 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71136">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fec01afbd.mp4?token=ha9OEbZMjuiWjTOR7VOqCPV1Wb5BgrfxSJOj5AvmmNfgrRospIQaiRJVkNqCvxg2n5X2u5d-CSWHSKm2UapMYEbVZJk2CYb7x8z0MTDJdwg5FZA0JIuACwOrOPIIVCDcFIp12ZYih1h_R3lEFV3FKjE5b8tcn7fp5dVV2CJb8zBzuqzJrii48ViGTYPkezl--O_5AJq1AQK1f3KEKGhesf3EyCKbyJFC1CtTS8sytj29GZknGQqamCY-LlzHBo3Hkid8QA_EP-PQoz5rXwlf7RtvnTi39dzoqatY_N0QDqnl93nN1C0A5a6FBcDiZgYy8xY_owEEewJZ3mJeqol9xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fec01afbd.mp4?token=ha9OEbZMjuiWjTOR7VOqCPV1Wb5BgrfxSJOj5AvmmNfgrRospIQaiRJVkNqCvxg2n5X2u5d-CSWHSKm2UapMYEbVZJk2CYb7x8z0MTDJdwg5FZA0JIuACwOrOPIIVCDcFIp12ZYih1h_R3lEFV3FKjE5b8tcn7fp5dVV2CJb8zBzuqzJrii48ViGTYPkezl--O_5AJq1AQK1f3KEKGhesf3EyCKbyJFC1CtTS8sytj29GZknGQqamCY-LlzHBo3Hkid8QA_EP-PQoz5rXwlf7RtvnTi39dzoqatY_N0QDqnl93nN1C0A5a6FBcDiZgYy8xY_owEEewJZ3mJeqol9xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پیرزن طرفدار حکومت که میگه:
نه پول میخایم نه چیزی دیگه گرونی هم تحمل میکنیم مسئله حجاب رو حل بکنید خیلی مسئله مهم تر و واجبی هستش
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/71136" target="_blank">📅 13:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71135">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5af49e9554.mp4?token=qHVt6AV_ovd5Aqa52WZkWDDgVVa9QUVRUlc7_PD7TVOoB42KUQ16jNw5wSkFkCGtPfNzLpHgJE5L513jbGefUR8Ef00u_QEuiYWglzt-4M1TQ-c3dXeSIKms8FhFu88Q_G-krDZUvocTPnpid57Sn-OXBhyGl-xTmI8hAcfZIX5gs34ZQrT6L6gFtn9URueT-7oKADTK5fZ9idkuBifD8ELNkQYp0amZi3nsDzW99Z1Sl_yhd0Zy6I3hH5WgOEKQ8Qyt5S73GZR-YOfD7sR7J1hx0g0qxbRb-2eehY01hjvDbCUh9SSjUQxz2YnluGnbKhQKVm4qmELDesc37BLb6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5af49e9554.mp4?token=qHVt6AV_ovd5Aqa52WZkWDDgVVa9QUVRUlc7_PD7TVOoB42KUQ16jNw5wSkFkCGtPfNzLpHgJE5L513jbGefUR8Ef00u_QEuiYWglzt-4M1TQ-c3dXeSIKms8FhFu88Q_G-krDZUvocTPnpid57Sn-OXBhyGl-xTmI8hAcfZIX5gs34ZQrT6L6gFtn9URueT-7oKADTK5fZ9idkuBifD8ELNkQYp0amZi3nsDzW99Z1Sl_yhd0Zy6I3hH5WgOEKQ8Qyt5S73GZR-YOfD7sR7J1hx0g0qxbRb-2eehY01hjvDbCUh9SSjUQxz2YnluGnbKhQKVm4qmELDesc37BLb6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
🇮🇷
تصاویری از نفتکش ایرانی که چند ساعت قبل هدف حمله آمریکا قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/71135" target="_blank">📅 12:41 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71131">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bb2e861ad.mp4?token=rnArM3Fp5zETvLf1D73NJ2GNuPXvm3GAz_gT1lrDDTt0W558sv0Q9DhKWf80XiAoiwV-wXSTIW84SDy7CvtYBQ3xGpJ0XF6h18I2kOsTja4ORcRxcnRrBHjEO0mamNoYw-72KcGXsCTSZYk00aFEQwQLjjx3J_5zNGOAH_x3RyELQoDkp2jeWQxvIMY2QXnnCRPKsNELURcvFZAByP2k4VvLTms2Sx4-9AaPUN8uIyU4lHC50VGS5MXv69_25Kld_N5rALqKcHBPRzj-miDG9YB6AHVBAKwDqYWOdF21SPzY9zzVVh-jwobHpaILzKpvojimQVOxWf_D9gWRoAi1PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bb2e861ad.mp4?token=rnArM3Fp5zETvLf1D73NJ2GNuPXvm3GAz_gT1lrDDTt0W558sv0Q9DhKWf80XiAoiwV-wXSTIW84SDy7CvtYBQ3xGpJ0XF6h18I2kOsTja4ORcRxcnRrBHjEO0mamNoYw-72KcGXsCTSZYk00aFEQwQLjjx3J_5zNGOAH_x3RyELQoDkp2jeWQxvIMY2QXnnCRPKsNELURcvFZAByP2k4VvLTms2Sx4-9AaPUN8uIyU4lHC50VGS5MXv69_25Kld_N5rALqKcHBPRzj-miDG9YB6AHVBAKwDqYWOdF21SPzY9zzVVh-jwobHpaILzKpvojimQVOxWf_D9gWRoAi1PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇱🇧
خبرنگار اعزامی صداوسیما به لبنان سقوط تپه علی الطاهر در جنوب لبنان رو تایید کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/71131" target="_blank">📅 12:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71130">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
خبرگزاری فارس:ساعتی پیش، صدای چند انفجار از خلیج فارس در محدوده جزیره خارگ شنیده شد  خبرنگار فارس در جزیره خارگ می‌گوید صدای انفجار از محدودهٔ خلیج فارس به گوش رسیده است اما نشانه‌ای از دود و آتش در خلیج فارس مشاهده نمی‌شود. تاکنون اطلاعات رسمی و دقیقی درباره…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71130" target="_blank">📅 11:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71128">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UAoSPqZDOnTrZg4xUHJjXNob7zJlG3lJscMflSGZGx3Ki9j_u6NbEoAmN73SbO_0nqpaAvDpW-eHo3FrVd7Fa1fFQTfCzeu-uZCCdohssN0Jbg9tLej00LHQC1tTq4WrvyYxt2RzhiuEZhIv4rncOfv3Ko53agfIF9SzXi_OEG4gbQiLsXR9N8VrHHfT8K8fGJT_nga2DB1y6wwfgtHlEVvyrMyIi0tYisiHvdH85fs7oXE2gwjba7cT-6NsL63XsDtZ8Hc1lby6OtZmpIVye_bEh66Yqm_zjYx94Weg0UDiGfVSNbqnQmh2yxZzXlh9dAIkUZIWpYiGfhLh_3vz_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/924e97ac3c.mp4?token=e72-PWyHzw3yaSchIBLrvGblfPg1p28psqsQI3dyfpxXEAIn8RjOxC4ypFM3UVtSKzemNPK9Sf3-fAWHhXEYia-DlhLS2emYT0dXp2GZcmb_rk0qH5IlYZm4r81BNdVkCPHdDc6VqalwL5m4BAtmJmBTcGYahELBQz6HusZFQN6h7LqlWhgcDIFMDwM63LfB5GUmhs-ZzPA33phlANueivjXYlThyPV2n336Q2bLiMKAphf2Je0RvPJAoWAwSPJa8tYhIa9hSDLh2H7Tt9CXbMge6BLgwUvjLTtOJQgDObOADU1fNj8xyDCjt7-C9HwztU6ln0UTXs6dgFlWw7DoLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/924e97ac3c.mp4?token=e72-PWyHzw3yaSchIBLrvGblfPg1p28psqsQI3dyfpxXEAIn8RjOxC4ypFM3UVtSKzemNPK9Sf3-fAWHhXEYia-DlhLS2emYT0dXp2GZcmb_rk0qH5IlYZm4r81BNdVkCPHdDc6VqalwL5m4BAtmJmBTcGYahELBQz6HusZFQN6h7LqlWhgcDIFMDwM63LfB5GUmhs-ZzPA33phlANueivjXYlThyPV2n336Q2bLiMKAphf2Je0RvPJAoWAwSPJa8tYhIa9hSDLh2H7Tt9CXbMge6BLgwUvjLTtOJQgDObOADU1fNj8xyDCjt7-C9HwztU6ln0UTXs6dgFlWw7DoLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یه پسر بدبخت پست گذاشته که اگه این پست ۵ هزار تا لایک بخوره، صاحبکارم منو میکنه! تورو خدا لایکش نکنین.
و حالا واکنش مردم دلسوز ایران:
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/71128" target="_blank">📅 11:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71127">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
خبرگزاری فارس:ساعتی پیش، صدای چند انفجار از خلیج فارس در محدوده جزیره خارگ شنیده شد
خبرنگار فارس در جزیره خارگ می‌گوید صدای انفجار از محدودهٔ خلیج فارس به گوش رسیده است اما نشانه‌ای از دود و آتش در خلیج فارس مشاهده نمی‌شود.
تاکنون اطلاعات رسمی و دقیقی درباره علت و منشأ این صداها منتشر نشده و جزئیات تکمیلی متعاقباً اعلام خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71127" target="_blank">📅 11:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71126">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71126" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71126" target="_blank">📅 11:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71125">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxZRpLoSPDdl5uZzK7hP9ZgmvwULYSe9pXNIGTHWwJkmVpU7a5uldNAyzv7KTdil3VOOcSxdnFlQGTfTbs08Ivx9uH3xDHfwR7v3iMtMYpX7tdhqbsyjSgRnJrMcrryRGfAgxn_KDUREMaTFfujcBFmznuwkwGCdyElusAQ0-J9UzNxYI-uqnt9F9ulkPSXg9-HpgmxZTfa7k42ka_UO1XV761wTOmOfzvpqM4BLRp5Q1ZHEsXmB0tKJjZGL2zyxgmcYrYmk_K5HPVpJ0_Ua0NLwSvC1iFQOgWreWcWnaE7BhjXA2iTDZXdxpcne2krd4gKwYXH_tni19WavSbJJ8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
پیش‌بینی کنید.
بورنموث
🆚
نیوکاسل
کاونتری
🆚
منچستر سیتی
تاتنهام
🆚
ناتینگهام فارست
اتلتیکو مادرید
🆚
اتلتیکو بیلبائو
ناپولی
🆚
اینتر
آتالانتا
🆚
رم
دورتموند
🆚
هوفنهایم
بایرن مونیخ
🆚
شالکه
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
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71125" target="_blank">📅 11:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71124">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0380bdceab.mp4?token=uLiWHRuOrWjCN4PJev2OLbUObJeV9WTMGN7CciDduGCIHc-nGnTIzeQuZv3dfg57PV4ZtCpcqj6Ld0xgThr4gCCgmNei4uZ8tRfWk5MqKXgMMJZRgzv_sGX4LmzIJIM_pN0kzBCFhIiDkRFb86m4zJcrsRUQDfwN4id2N_DcMrJJa21b0_YjUL7LtRtO9q5Tvd4xELJVG1MlkHOAT1wQqXiaohxTky5CE1hbfx4fhl_xx5prIpwWvW1UPYX5GPzEUuEMoLW4524YtSKF3CKD9e-oqQwVh6JEVLh6b3S3bCoWC96_womG9FdGubMDB5kka-b7ysJsYbB0AcYfQRs7fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0380bdceab.mp4?token=uLiWHRuOrWjCN4PJev2OLbUObJeV9WTMGN7CciDduGCIHc-nGnTIzeQuZv3dfg57PV4ZtCpcqj6Ld0xgThr4gCCgmNei4uZ8tRfWk5MqKXgMMJZRgzv_sGX4LmzIJIM_pN0kzBCFhIiDkRFb86m4zJcrsRUQDfwN4id2N_DcMrJJa21b0_YjUL7LtRtO9q5Tvd4xELJVG1MlkHOAT1wQqXiaohxTky5CE1hbfx4fhl_xx5prIpwWvW1UPYX5GPzEUuEMoLW4524YtSKF3CKD9e-oqQwVh6JEVLh6b3S3bCoWC96_womG9FdGubMDB5kka-b7ysJsYbB0AcYfQRs7fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📚
معرفی لاکچری‌ترین مدارس ایران !
برای اینکه به علم برسی هم باید اول ثروت داشته باشی!
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71124" target="_blank">📅 11:03 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71123">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a478b3c9a9.mp4?token=gWrZy7vIoAYE-QZGR2jm1gKTiIoFIn4avvK_BzwZVq5PVfGFCTU4o0NejytaF5_keX-VHMrmnJjsa6lPqQHwkXXwZywecCguSNoHTxzhAhpZpGPOvT_VNra1IrGoO4U-nljOuZvJwm85Z7bVXMxLTASBIYatu4kLQSJzBJmTWOakKPeHGnFtxsIE_uWxIiIWiE0IeGmaFhytvBoRcT5MBWdA71cLirwTrUA98ACILDRuXe_l-OA3E8hvWyZAw6Gl3NcXAU29btniztuu3OA8NtlWGVevDzhWDKiewFG-4KIY7kYRGTfw_93Jl4gJamk5cAa-1aEELIdKWkaVxvvLng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a478b3c9a9.mp4?token=gWrZy7vIoAYE-QZGR2jm1gKTiIoFIn4avvK_BzwZVq5PVfGFCTU4o0NejytaF5_keX-VHMrmnJjsa6lPqQHwkXXwZywecCguSNoHTxzhAhpZpGPOvT_VNra1IrGoO4U-nljOuZvJwm85Z7bVXMxLTASBIYatu4kLQSJzBJmTWOakKPeHGnFtxsIE_uWxIiIWiE0IeGmaFhytvBoRcT5MBWdA71cLirwTrUA98ACILDRuXe_l-OA3E8hvWyZAw6Gl3NcXAU29btniztuu3OA8NtlWGVevDzhWDKiewFG-4KIY7kYRGTfw_93Jl4gJamk5cAa-1aEELIdKWkaVxvvLng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تسلا، سفر با تاکسی‌های خودران Cybercab رو تو تگزاس آغاز کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71123" target="_blank">📅 10:34 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71122">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a09a3f19ee.mp4?token=t6W66ooTwumAFDXsuutg_KCg2SJQa6D2FUMdX1Z5kd0KRe_-1kdOMQ2BN0UxgDf6Mu8h3k2EoyVzEDuXUyajSye2M75K-sMLPMBWNgjgte8qnCejB17m3Q8JRqJKCOa04DBa8I5v3jjG0ZTE0JSdQCea4NjKuqJ5gFWveEi74MSnl9UJaf7q8VRkbyLWtjtByZvpVKP9kLLnIZrjVfyv3BglF5mFy-ctZ9R2_GxFLGdimXGev4BwH0IUsS-1MrId_sEPaXMVvuUKxTf0NPucUPN-dNpKS1lhE6iDY_u8nWsrZbybRm7sTX1ARPFYBdwC4N9jvWmpELYzb2Jze3JR4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a09a3f19ee.mp4?token=t6W66ooTwumAFDXsuutg_KCg2SJQa6D2FUMdX1Z5kd0KRe_-1kdOMQ2BN0UxgDf6Mu8h3k2EoyVzEDuXUyajSye2M75K-sMLPMBWNgjgte8qnCejB17m3Q8JRqJKCOa04DBa8I5v3jjG0ZTE0JSdQCea4NjKuqJ5gFWveEi74MSnl9UJaf7q8VRkbyLWtjtByZvpVKP9kLLnIZrjVfyv3BglF5mFy-ctZ9R2_GxFLGdimXGev4BwH0IUsS-1MrId_sEPaXMVvuUKxTf0NPucUPN-dNpKS1lhE6iDY_u8nWsrZbybRm7sTX1ARPFYBdwC4N9jvWmpELYzb2Jze3JR4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
〰️
🇹🇭
کامیون‌های سوخت‌رسان مشغول انتقال سوخت هواپیما به ناو هواپیمابری «یو‌اس‌اس آبراهام لینکلن» (CVN-72) در بندر «لائم چابانگ» تایلند هستند؛ به‌طوری که از زمان پهلو گرفتن این ناو، روزانه ورود و خروج ۲۰ تا ۳۰ دستگاه کامیون مشاهده شده است.
این سوخت برای تأمین نیازهای «بال هوایی نهم ناو» (CVW-9) در داخل ناو ذخیره می‌شود؛
یگانی شامل جنگنده‌های رادارگریز F-35C Lightning II، جنگنده‌های تهاجمی F/A-18E/F Super Hornet، جت‌های جنگ الکترونیک EA-18G Growler، هواپیماهای هشدار زودهنگام E-2D Advanced Hawkeye و بالگردهای MH-60 Seahawk.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71122" target="_blank">📅 10:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71121">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/deba41468f.mp4?token=ZXS5KnOQ_i6-dKs1MzzqWs2F-rG51zRhNhWRbTRE0Dj68PXiqso-CuEXra-39N7csqFyy7QdYGEIr8SenxIOFmKR4zuHTNe0A89RVd5DQNxXgnnjaAFK082LZQMa7UbnugHSrys76_vEHZGhaTCc1Ln-TxnHM2zopHCIqgxq1j7sF0PSoTzEXj6cpCwd4QWicPmNzYzQ4vYultRJ07nyLKNOmULXzt495xSpQxiOauDTHsnd10Cz6J59wW3PtvI6C7yg_vqRxj0HsDD8FMYUYOmfb-dwYvV_t5rllrwvnlqt_YMXIZLzVbDmYkp5hG0juS77SwMrHK1EXLJsEArfFxXAd6KOQRzOZVOzVUffp5pei2uUX6qdXHxgMhCnlIPLXwPglvenlIYroohqo8cG17N5UKnxryy5YyhH3fmWylrln7Ufn99vIIHuxhFSJcq8NbmHk5OT42-ZMXGLMekpX2GZBcKvBtt81n_xgr43_daFKi4N1zx3onj48azr2wsD7DkCvyDvlZTSNTyfzDyOliG8esnpw7hmR9e5sTDkRaE2UWWsLQueVqniyXFRfduJ6bvRt2N3CT0gMDHd4fQYoe6U98pDThSFjBbNDqjV8yk0M-o9R7gZvrhloADgatW1LYuYv14zj33oqJr2GSsimK4qfguBh5ikNmZK0ZUrYjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/deba41468f.mp4?token=ZXS5KnOQ_i6-dKs1MzzqWs2F-rG51zRhNhWRbTRE0Dj68PXiqso-CuEXra-39N7csqFyy7QdYGEIr8SenxIOFmKR4zuHTNe0A89RVd5DQNxXgnnjaAFK082LZQMa7UbnugHSrys76_vEHZGhaTCc1Ln-TxnHM2zopHCIqgxq1j7sF0PSoTzEXj6cpCwd4QWicPmNzYzQ4vYultRJ07nyLKNOmULXzt495xSpQxiOauDTHsnd10Cz6J59wW3PtvI6C7yg_vqRxj0HsDD8FMYUYOmfb-dwYvV_t5rllrwvnlqt_YMXIZLzVbDmYkp5hG0juS77SwMrHK1EXLJsEArfFxXAd6KOQRzOZVOzVUffp5pei2uUX6qdXHxgMhCnlIPLXwPglvenlIYroohqo8cG17N5UKnxryy5YyhH3fmWylrln7Ufn99vIIHuxhFSJcq8NbmHk5OT42-ZMXGLMekpX2GZBcKvBtt81n_xgr43_daFKi4N1zx3onj48azr2wsD7DkCvyDvlZTSNTyfzDyOliG8esnpw7hmR9e5sTDkRaE2UWWsLQueVqniyXFRfduJ6bvRt2N3CT0gMDHd4fQYoe6U98pDThSFjBbNDqjV8yk0M-o9R7gZvrhloADgatW1LYuYv14zj33oqJr2GSsimK4qfguBh5ikNmZK0ZUrYjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
بابک زنجانی:
الان کافه‌های مردم را می‌بندید بعد شب آدم می‌فرستید که بیاید تعامل کند.
می‌خواهم فیلم و مستند درباره این موضوع تهیه کنم... آن شخص هم فکر می‌کند که با ۱۰، ۲۰ سکه زندگی‌اش را گذرانده
بیکار کردن ۸۰ نفر در منِ بابک زنجانی چه اثری دارد؟! اصلاً فردا بیایید آتشَش بزنید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71121" target="_blank">📅 09:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71120">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f4goW3lUp_B6eNx-Mg0ovrae2Oh4IAFCY2Jfx3xXUn77wJrB_b-QC82C8y6e3rt63EdHZO0WSQSPd6ssdrIW_61IK6brzhQe3Eg1lbr1SIlBB1tltm0KK-z9ncmlYDTHRDv5D9rlPSt-0OGjUuQ-DPPUJEKwvTx4iROiZq1F-4GzsCFVKtlmMnWT6T404hnrI1RaU-bjBAHAMXCjr1DmsYxiGidFsA52kCCVua02KwdhlvmVhDwepiy8g6o_8OaHcfq-Q3B5iNxDsXXKIOmq_noh8apAeq-ZLblzL92uDYIANarWmlx9SuAFwYQfqdQAfDXXvt-JeXJUJv_3IW3mxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇷
🇴🇲
نیویورک پست:عمان بی‌سروصدا پیشنهاد ایران برای دریافت مشترک عوارض از کشتی‌های عبوری از تنگه هرمز — حتی به‌صورت داوطلبانه — را رد کرده است.
این اقدام، ادعای هفته گذشته سپاه پاسداران مبنی بر توافق دو کشور بر سر تقسیم درآمدهای این آبراه را تضعیف می‌کند.
عمان معتقد است که دریافت عوارض از کشتی‌های عبوری ناقض قوانین بین‌المللی است و تحت فشار آمریکا و کشورهای حوزه خلیج فارس، از این طرح عقب‌نشینی کرده است.
ترامپ دو بار تهدید کرده است که در صورت موافقت عمان با دریافت عوارض، این کشور را بمباران خواهد کرد.
ایران در دوران جنگ، نهادی برای مدیریت تنگه ایجاد کرده بود و از هر نفتکش مبلغی بین ۱ تا ۲ میلیون دلار عوارض می‌گرفت؛ اما بدون همکاری عمان، هرگونه سازوکار دریافت عوارض در دوران پس از جنگ، فاقد وجاهت قانونی خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71120" target="_blank">📅 09:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71119">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71119" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71119" target="_blank">📅 01:13 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71118">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0DHPj6X8pjqony1KWeUVTdMsUBb7AXgb6NkA3RV1EB1EhyHQ30HioX3g5F0sU8Xs25gA2iY3KRD_Y20cc9A4zXzquFjpIfpag2ZzOh2DWGmM-ab6nu_nDOxsWjeX2kmIxG3MBr3ovX430dL5h6Mj2gbFPruZhUBBetqWJ9Zf3wdLh1Z21EYolKl5GK30uT1uqj5xhUUqkNNX3c60tavaZqeDZjRppye7vAziZTRGmSPaDMHoUriIyhBwns1BNsWM4YWIMtP4LOLrezDEGE3ndEL6J8GWfD_ehh902ro1pGLZUfNb8JAEGWLsY6JSbqEENnRN2tFXaUcwG63c19hVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
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
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/71118" target="_blank">📅 01:13 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71117">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59487b6d80.mp4?token=FZbSX-YoJroXb2J7hi_y4DGClTS2029quel6RUcNzKqbH5oTUPxbhCUZTjVXfPuywmjsiedX3dAaLCu98U3RF8ruW6iIvbptRV8WjyeyilApVsGzEgL5p71xTX2xjkxoyjNb3VxS2VuKEKOiwCDi6U57LvuoaaJH4BqhTrOyP6WRhh6uvx7q_h6xgC8Xny_YE2NSdfmV8y93ef0ltUYHz2aH0vtcGxIhf3iVlQXuiIXC2dKLoOqhKMLSmQjMQ1pJS5Z3IMrqKl3yAB3Pads0ol0BQzzBfz6VJqCPpXUn5UVeVLXHmDQzhuRzToA7TNd1IS_HoWil8Irbh4YUMJUUaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59487b6d80.mp4?token=FZbSX-YoJroXb2J7hi_y4DGClTS2029quel6RUcNzKqbH5oTUPxbhCUZTjVXfPuywmjsiedX3dAaLCu98U3RF8ruW6iIvbptRV8WjyeyilApVsGzEgL5p71xTX2xjkxoyjNb3VxS2VuKEKOiwCDi6U57LvuoaaJH4BqhTrOyP6WRhh6uvx7q_h6xgC8Xny_YE2NSdfmV8y93ef0ltUYHz2aH0vtcGxIhf3iVlQXuiIXC2dKLoOqhKMLSmQjMQ1pJS5Z3IMrqKl3yAB3Pads0ol0BQzzBfz6VJqCPpXUn5UVeVLXHmDQzhuRzToA7TNd1IS_HoWil8Irbh4YUMJUUaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
مردم آمریکا چه زمانی باید انتظار تعیین تکلیف (resolution) در مورد ایران را داشته باشند؟
🇺🇸
ترامپ:
انقلاب(Revolution)؟
🎙
خبرنگار:
تعیین تکلیف(Resolution).
🇺🇸
ترامپ:
تفاوت بزرگی است. فکر کردم انقلاب(Revolution) جالب‌تر بود.
⭕️
🗒️
به دلیل تلفظ نزدیک دو کلمه راه حل/تعیین‌وتکلیف(Resolution) و انقلاب(Revolution) ممکنه ترامپ اینجا به عمد کلمه انقلاب رو انتخاب کرده باشه!
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/71117" target="_blank">📅 01:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71116">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76ef0c44cf.mp4?token=L-1PLZepMYSJ3rxob8YhJoIyw9mGzgewgM8jDO9A_tmCHMFJSFDXN1roCFT9OlvUn48oC1HyORtvcGYY469OP2ztq4Fe1inLopDrhIqDlflT5cPLGNkc6qiIr4OgHakbuvJ4YiCy6X-uc9lEgbMMbg_0VUu5QFLHTy1EQwRYwGwWmxgi9Ob2zRhaYSXoGOZrT7wy65jKrUZFc23_Aurvmbpfq6MaJ27kWq7H2A6ocLEk8k_fR44LrRM1vcLhCrbvhV3WQ3koauWXZ6qgI_jwwY16ajMTC45BXfAusyMd_ptNz7CsMUzY9i4uKFGfmO_ToaQPTC5pubNHJB0vlc-G5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76ef0c44cf.mp4?token=L-1PLZepMYSJ3rxob8YhJoIyw9mGzgewgM8jDO9A_tmCHMFJSFDXN1roCFT9OlvUn48oC1HyORtvcGYY469OP2ztq4Fe1inLopDrhIqDlflT5cPLGNkc6qiIr4OgHakbuvJ4YiCy6X-uc9lEgbMMbg_0VUu5QFLHTy1EQwRYwGwWmxgi9Ob2zRhaYSXoGOZrT7wy65jKrUZFc23_Aurvmbpfq6MaJ27kWq7H2A6ocLEk8k_fR44LrRM1vcLhCrbvhV3WQ3koauWXZ6qgI_jwwY16ajMTC45BXfAusyMd_ptNz7CsMUzY9i4uKFGfmO_ToaQPTC5pubNHJB0vlc-G5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو ایتا و روبیکا از یچیزی رونمایی کردن که حتی خودشون هم نمیدونن چیه
😳
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/71116" target="_blank">📅 23:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71115">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c1e4d7b78.mp4?token=uzw6FU4-yjL9m9y-gWSDL-3GBRnos4IWLGwAw9j6KsP7R9g7MllyQXxaUcQGWZCvdGUTu0bhcKsXKS44EVnIiAwpMfrc5p6bCf_41oKl0s9nPspuHM2pmqmqZeKFtk1oNSa82hu11e8TY3M5LK_pRWF0ZPU0jjHGroZemhVVk2pxIIkkOkkvOvY9caYnYPLYFNtXU_QMELbjeMN9aeK49QuijiKSJY7OporXkQhEr_caHQFj05aXOFGeXTZVlF57eNteM8lIrsK1cNhggV_CvAo88vq0syt-q0-oeLGbpxbVgkbYgkIS7lBxsNIXU-qSA0PIc-SL9M4_uYFsl0bEEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c1e4d7b78.mp4?token=uzw6FU4-yjL9m9y-gWSDL-3GBRnos4IWLGwAw9j6KsP7R9g7MllyQXxaUcQGWZCvdGUTu0bhcKsXKS44EVnIiAwpMfrc5p6bCf_41oKl0s9nPspuHM2pmqmqZeKFtk1oNSa82hu11e8TY3M5LK_pRWF0ZPU0jjHGroZemhVVk2pxIIkkOkkvOvY9caYnYPLYFNtXU_QMELbjeMN9aeK49QuijiKSJY7OporXkQhEr_caHQFj05aXOFGeXTZVlF57eNteM8lIrsK1cNhggV_CvAo88vq0syt-q0-oeLGbpxbVgkbYgkIS7lBxsNIXU-qSA0PIc-SL9M4_uYFsl0bEEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
طرف اندازه یه گاری پول جمع کرده و الان آورده تبدیل به دلارش کنه، کل این همه پول نقد شد فقط ۳۰۰ دلار
!
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/71115" target="_blank">📅 22:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71114">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/05f93dafa7.mp4?token=t65LVQho4JNUj5VqkgN-vWn0iJltmTZDAi-7bgD1ElO0h8ujiVUabrn-wNozUB2pYpQnfKMiggir6Of-g0REXz5RqZXtHuKDw3QoHj0RWOldCMZouYTXWFVP8OTF1ilkNgfInATK7JiQezRMcLV77hmXxVaqodteKkvfkiHU9m7oAHeGKJsuPCvyCyKmn5wOmrCSDXpq1kJtTeVYkPKSHaNphhfkeWhhzvoHwnRTiBwU6Lb59eltaLW3l8VoG0hwwW9FLRSoC8OlUUOtXY7c_ZnVKqnDkRcPTFXb8ZggUOfHMqYDZwQquA8n92ocNcfFdrwsObIZhzmP7OhoU9V2BoRwhE0--Up8aFtifk1ZGCoLvUb5VrCM17jPuqCz9PMBptYX47anGt-4h_eopFxp1IUjZFTct1l3DXHMXZrfzNlPKpxrxabTwL8MlrKxiPNndtzvr_5htsvoYYSgsAIvhPMWZ3Bs0Fz2uNEpeTToTQckjvBfIMpG5lB8mHjNAn_vzMBiFgRQP4Vj0EY7_8tiDlKXUBiDQXGSqKnfrOXURyr9IQYUR4g1MsDKkX2wZkdWYXjzc3iFVEb_uU6gCxPvX7_ZHEKfozEf8o52xzUNvSic1t1sWWI7sXkYFDMvisGsJrukxA88sxR4VgDDGUeYkjpEYH0r3X_4EJimzpOBlxY" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/05f93dafa7.mp4?token=t65LVQho4JNUj5VqkgN-vWn0iJltmTZDAi-7bgD1ElO0h8ujiVUabrn-wNozUB2pYpQnfKMiggir6Of-g0REXz5RqZXtHuKDw3QoHj0RWOldCMZouYTXWFVP8OTF1ilkNgfInATK7JiQezRMcLV77hmXxVaqodteKkvfkiHU9m7oAHeGKJsuPCvyCyKmn5wOmrCSDXpq1kJtTeVYkPKSHaNphhfkeWhhzvoHwnRTiBwU6Lb59eltaLW3l8VoG0hwwW9FLRSoC8OlUUOtXY7c_ZnVKqnDkRcPTFXb8ZggUOfHMqYDZwQquA8n92ocNcfFdrwsObIZhzmP7OhoU9V2BoRwhE0--Up8aFtifk1ZGCoLvUb5VrCM17jPuqCz9PMBptYX47anGt-4h_eopFxp1IUjZFTct1l3DXHMXZrfzNlPKpxrxabTwL8MlrKxiPNndtzvr_5htsvoYYSgsAIvhPMWZ3Bs0Fz2uNEpeTToTQckjvBfIMpG5lB8mHjNAn_vzMBiFgRQP4Vj0EY7_8tiDlKXUBiDQXGSqKnfrOXURyr9IQYUR4g1MsDKkX2wZkdWYXjzc3iFVEb_uU6gCxPvX7_ZHEKfozEf8o52xzUNvSic1t1sWWI7sXkYFDMvisGsJrukxA88sxR4VgDDGUeYkjpEYH0r3X_4EJimzpOBlxY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇳
یه بلاگر ایرانی رفته چین و ربات انسان نمای چینی رو به مبارزه طلبیده؛
حرکات ربات به قدری تمیزه که انسان واقعا از آینده جهان خایه میکنه!
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/71114" target="_blank">📅 22:16 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71113">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a66a864cef.mp4?token=bcUB_6pqMUbPi4ytTOoSrt5jb_gE7dbAApnMmevFdvpharLwZIZVWWaneGdbAHKiLg9jSHgKiTKtqnfBsVZGie8PfyOhbEXZXIN3Lf8WMzKomNazih3o9BElVhwuKFdMSoMnz-Boj9fziSOCc5yiVvLKFMxERLyoLcNKnUxqKBYr_qJc_1YPq_9cFl4-Q1f0t3Mer1zZm0CQDfeFMme8YutPs7EqR0MHNckTy4SscNLPLApn4vINRu2aeqQebrNKP42wHY-wUfXW1quOnDenK4B72Y0LxRTrDX8GP3WWdRQLD8bELzMgmmA4mC1SX1WVThCXW8J6qd1jWHOq9SdEfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a66a864cef.mp4?token=bcUB_6pqMUbPi4ytTOoSrt5jb_gE7dbAApnMmevFdvpharLwZIZVWWaneGdbAHKiLg9jSHgKiTKtqnfBsVZGie8PfyOhbEXZXIN3Lf8WMzKomNazih3o9BElVhwuKFdMSoMnz-Boj9fziSOCc5yiVvLKFMxERLyoLcNKnUxqKBYr_qJc_1YPq_9cFl4-Q1f0t3Mer1zZm0CQDfeFMme8YutPs7EqR0MHNckTy4SscNLPLApn4vINRu2aeqQebrNKP42wHY-wUfXW1quOnDenK4B72Y0LxRTrDX8GP3WWdRQLD8bELzMgmmA4mC1SX1WVThCXW8J6qd1jWHOq9SdEfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اخیرا بعضی دخترا طی یه حرکت فوق‌العاده و زیبا، دارن هرچی ژل و بوتاکس تو صورتشون بوده رو خارج میکنن تا نچرال به نظر بیان
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/71113" target="_blank">📅 21:29 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71112">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FTvIo8mQd848MIQK4bJFkCkfsxIibFuKsfPr_aZ30hHsCn3j6NFrUqM9IV8PFdVUQtI2AOWWX6G2pVd-Q5Sgn6Z1Jd5RWutD8pbSr9OOEteM8bAk5kAvjwm7v5aFgyFOWM9jyfmM6aXOU-h3ZLGsB2J0x2ipPAGyW1oNBfReVvDf0En45YoG0TizHNHOgKM1KRqk-6avQZZR3uMp4pbrbhBkiYqlwY6_zhDYFUbLYUYLdCdmCAJxS2wYCUEClsRirKbRbMmtWt7xAT4P8eeaITKa5V80QvIs9kfFS5poRpFiF4vQ1ueZYII3_T_GzNEUmQu328ew_Ds5j0IgvToApg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👎
قرارگاه خاتم الانبیا: حملات پیش دستانه علیه پایگاه آمریکا در اردن که در حال آماده سازی برای حملاتی علیه کشور بودند را انجام دادیم!
❌
خبر بالا که بطور گسترده در حال انتشار در رسانه هاست فیک و نادرسته، همونطور که می‌بینید سپاه پاسداران و قرارگاه خاتم‌الانبیا هیچ اطلاعیه‌ای مبنی بر حملات پیش‌دستانه منتشر نکرده
@HutNewsPlus</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71112" target="_blank">📅 21:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71111">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTMeVaZUeiYrRZOAW0OCkd8ZxRgbz6eoKHGduchib76AsMzYCMVeoGI5IdtB7VisH0xY-HKKcxzLxDdqF1r6KkkUXNbK7Gk7cE4H0mB9hmVyouqQjSm741OKTZXmsIUfoj73dSuL5KCawndp8iHYHLaLQoz4AtVmg5Ip6XB08l4M68l_sFaVmuMgluuKUF4w8GV5AR_iFrFXY3D6FZhCR3cRYK0UAnS2tf3JO_bsfz-G46Wv_D-u1k3PQZ5Y7ueOd54jlR0ULosWuqY3KVAWitH_GbG-OslB7MQ11SfNKCPihqm7ADwkX6C_ExcobY_7dlJdBDsn2sofz_cWPwmamw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقام ارشد آمریکایی به کانال 12: در حال حاضر هیچ اطلاعی از وقوع آتش‌سوزی در پایگاه‌های آمریکا در اردن وجود ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/71111" target="_blank">📅 21:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71110">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c74f1d2d4f.mp4?token=Ri58pbIDbznI0k9vW_z0CptJaSm-o7PVo-DBEc6R3YjfI84bjAtqObHfw9Oc-puykTvOzPoCM06-Yo0jXN7HPmckivgFSjp1neRCKdJ5W9P7S_GluebB_o4yHJo-c6T0qp8uzYF6raouMrbSw1Vxkm0-i7POX7RnTADnuW52pKruYASkueOSjrDetHE0Ik9iDrxeZywNjvorblSDPHAEzpnVW2Nv7uwkVOboCMCO-lq-vtJUpljJQ6TNj2nrNnKEMiGXw-gy5VGGRYUv5eA61LJol7rlU0vLkfnDCE7puUiLFaCzBHIJP7yFNLKwGH5lLWA9J4cK36W75GtOLzG48A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c74f1d2d4f.mp4?token=Ri58pbIDbznI0k9vW_z0CptJaSm-o7PVo-DBEc6R3YjfI84bjAtqObHfw9Oc-puykTvOzPoCM06-Yo0jXN7HPmckivgFSjp1neRCKdJ5W9P7S_GluebB_o4yHJo-c6T0qp8uzYF6raouMrbSw1Vxkm0-i7POX7RnTADnuW52pKruYASkueOSjrDetHE0Ik9iDrxeZywNjvorblSDPHAEzpnVW2Nv7uwkVOboCMCO-lq-vtJUpljJQ6TNj2nrNnKEMiGXw-gy5VGGRYUv5eA61LJol7rlU0vLkfnDCE7puUiLFaCzBHIJP7yFNLKwGH5lLWA9J4cK36W75GtOLzG48A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
شلیک موشک ها از ایران به سمت اردن
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/71110" target="_blank">📅 20:29 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71109">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
منابع عربی:چندین انفجار در اردن رخ داد
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/71109" target="_blank">📅 20:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71108">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbf8f1e1a9.mp4?token=TX8Dl6KODCWe7C898z7Wou5TUznRc6iM_BKCQUXSRuLWivWdoYu3A71ssglF1Dvj21DE-gzVKiiVIIjwH7EOgxyffDu9wVqLdPh4Xnsam-FJZG-AVcpNMrBBKh7xgl2VFLXjFnWFt58-wHcWvoiflTqNntYoNs121zNVFhAA2EXYUZakWfpNHhbRqJQrEshTQ-klhcGW3AC3HA3MeP2jOYGrv22q4GDCUnI8drbWvixPXsE5Tyi4s5b0jsHEjRe993FS5a5OWBFWs1UWLI46IaHVYcWqY78Tsxh01UR4XSxMtQoU7M3KNA0K6-oHWWu-I9Kmst2g3URKdsaFOnuY2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbf8f1e1a9.mp4?token=TX8Dl6KODCWe7C898z7Wou5TUznRc6iM_BKCQUXSRuLWivWdoYu3A71ssglF1Dvj21DE-gzVKiiVIIjwH7EOgxyffDu9wVqLdPh4Xnsam-FJZG-AVcpNMrBBKh7xgl2VFLXjFnWFt58-wHcWvoiflTqNntYoNs121zNVFhAA2EXYUZakWfpNHhbRqJQrEshTQ-klhcGW3AC3HA3MeP2jOYGrv22q4GDCUnI8drbWvixPXsE5Tyi4s5b0jsHEjRe993FS5a5OWBFWs1UWLI46IaHVYcWqY78Tsxh01UR4XSxMtQoU7M3KNA0K6-oHWWu-I9Kmst2g3URKdsaFOnuY2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🇮🇷
🇨🇳
بِسِنت درباره ایران:
آن‌ها محموله‌های نفت را به سمت چین روانه کردند. منتظر اقدامات مربوط به این موضوع در روز سه‌شنبه باشید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/71108" target="_blank">📅 20:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71105">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64aa07a7bb.mp4?token=LLHY4kLAOPxXkhhHdP1yh-cw0KDXyuRBsLmCPvnVCCQm3yd_b02Jnobq5XVflK_v6Nze_9sm-Nb6R9mu_eqrgvZLMLEUXXVg6BebKeTRz8VYPVzEI9KWEdOSlovIG16TIg-8DtapoIMbBDWdpZOcWQr__VATW58bvzYXYWpyQYrWgXkpGidq2hO2TwrEUmmjpSCO12S3LxJUgSM6prHA25V2Ju3M6L6icu219dL67U5QvELIpL8ePCQXicG4RcwFo27ipc2ANta7eRPVh89Ouu3ThPombzWL5rQXGXTJDE_nQZym6KoZErQKLnq2kMt-Rah-LTLcCNFiGFW3DOYDxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64aa07a7bb.mp4?token=LLHY4kLAOPxXkhhHdP1yh-cw0KDXyuRBsLmCPvnVCCQm3yd_b02Jnobq5XVflK_v6Nze_9sm-Nb6R9mu_eqrgvZLMLEUXXVg6BebKeTRz8VYPVzEI9KWEdOSlovIG16TIg-8DtapoIMbBDWdpZOcWQr__VATW58bvzYXYWpyQYrWgXkpGidq2hO2TwrEUmmjpSCO12S3LxJUgSM6prHA25V2Ju3M6L6icu219dL67U5QvELIpL8ePCQXicG4RcwFo27ipc2ANta7eRPVh89Ouu3ThPombzWL5rQXGXTJDE_nQZym6KoZErQKLnq2kMt-Rah-LTLcCNFiGFW3DOYDxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
بابک زنجانی: دلار رو بدید دست من تا یک سال رو همین قیمت نگهش میدارم وگرنه با همین فرمون کشور تا یک سال دیگه نابود میشه.
من رو ۷ سال بدون بدهی انداختن زندان و همشم تو انفرادی بودم. همه اموالمم ازم گرفتن. وقتی آزاد شدم حتی ۱ دلار نداشتم.
با چند تا تلفن ۱ میلیارد دلار پول جور کردم و چندتا شرکت تاسیس کردم.
من میخواستم سایپا رو به قیمت ۲ میلیارد دلار بخرم که نشد ولی خودم میخوام کارخونه تولید خودرو تاسیس کنم
من توی خارج کشور بانک داشتم پولای وزارت نفت تو اون حساب بود. اونا تحریم شدن پولاشون اونجا گیر کرد گفتن تقصیر توعه و حکم اعـدام بهم دادن
تمام بانکای ایران بیان جلوی من بشینن ببینیم من بیشتر میتونم سرمایه جذب کنم یا اونا. فقط با چندتا تلفن. تا معلوم بشه کی اعتبار داره
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/71105" target="_blank">📅 19:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71104">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf31ca2a30.mp4?token=v82ky4hpNsv8YcjWEHyIKlMXgYP2yRc36b6fvqPaZNPFn_GOiKUckx7HmFKY5nANDopQVo0WHZlxg9d-oRW0wyR-LtGoEgjBeWuIxc60M6T7lqBh4UxCGO52kH3sUH_GGdbjoBncLdIs2TRVAtEJy5s1uf6wP5vRxunSg8pr2eDuEZ3BZnzRgYDsVimCn_xJlGlpoIRQhPINYIexjgKTUdV2Lo0SzbF6DJTGNm98HrNK3bGUe7yVcgOjMJZ9EIGPxZHSLAxFh9u8jfn4yB42G6LNWN5CiLtiIp3J2lAduFTj67jOwZonWJMVTAP-Bd9eS0gyI7r8nCKAUuO3dsIh3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf31ca2a30.mp4?token=v82ky4hpNsv8YcjWEHyIKlMXgYP2yRc36b6fvqPaZNPFn_GOiKUckx7HmFKY5nANDopQVo0WHZlxg9d-oRW0wyR-LtGoEgjBeWuIxc60M6T7lqBh4UxCGO52kH3sUH_GGdbjoBncLdIs2TRVAtEJy5s1uf6wP5vRxunSg8pr2eDuEZ3BZnzRgYDsVimCn_xJlGlpoIRQhPINYIexjgKTUdV2Lo0SzbF6DJTGNm98HrNK3bGUe7yVcgOjMJZ9EIGPxZHSLAxFh9u8jfn4yB42G6LNWN5CiLtiIp3J2lAduFTj67jOwZonWJMVTAP-Bd9eS0gyI7r8nCKAUuO3dsIh3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
بسنت درباره ایران:
متحدان ما در امارات متحده عربی در خصوص این بانک مستقر در دبی همکاری بسیار مؤثری داشتند. اکنون ما برای متوقف کردن تمامی این جریان‌های مالی غیرقانونی، با آن‌ها وارد همکاری شده‌ایم.
ما برای رفع این مشکل با آن‌ها همکاری خواهیم کرد، چرا که بانک‌های متعددی در سیستم مالی آن‌ها فعالیت می‌کنند.
ما نمی‌خواهیم این بانک‌ها را نابود کنیم — هرچند اگر لازم باشد چنین خواهیم کرد — اما اکنون همه کشورها در این مسیر با ما همراه شده‌اند.
این پایان کار برای این رژیم است؛ آن‌ها یا باید [رفتار خود را] عادی‌سازی کنند و یا با عواقب آن روبرو شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71104" target="_blank">📅 18:41 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71103">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38e7eb93ff.mp4?token=EYNkVcC_rOhfBibpVqOGGql92wJyWYOQbgaajHRaRzRib9e3jLDocODvp1jIQLcCaEJ8zbvLSc04tWikgMGtrRpTnfokPiKr8b_GvpI6S3N_VyXUTXbJgU8sqRJsFvo5-7YSCN_xcFm6Ma2MRvH8lU9TiCYs_Lk-X5zdQVNmCTLC5DC_lzlTyE5_98QPWZmYrMvTPR8zpbZmAS3wXk3B2eOUU0cMf7bTQAsMkNOBr1sj0k0D5bH975Hz3w4r0Ae6ujkuPoXz1wNSGgNQJjGWfpwT0VFs-KdMVZAQdTYB6f_ebkKmF6Lfas6YbwZFZqo2k6jgInUU7r-gCZ_3sY_BXz3zqTCABwVdhcMh-UowZUymlAIjjdUEo0EKFpSqQj8d_k3TxpkIsoiuEzZVqCt_Z2cX0M_YLqT3TSZVBSv8VbYt6n6joWrfiMAFyZ-ZQ0OP7q0vpfWSWEMGhupK8bUc58KeVMezFBEsRbG4eQS_6Jj0A7wIptqva6-WoD6Kwnl8dMxRVOm_hNDS0WXf1NALMYeyGZO93yOK-thXXT2d8wm2LEwRhXocaz8YNpF6vvEHeTdywl1MKJAqy0xYx-9Qt3zXCw65FlUAOJq7soBPImiwV2VTDIA4Rt_Jw6mQE3SxyFHxJ5qRvjP-ff6nhAxOkm981HdoRi-gfa6KsoWiM_I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38e7eb93ff.mp4?token=EYNkVcC_rOhfBibpVqOGGql92wJyWYOQbgaajHRaRzRib9e3jLDocODvp1jIQLcCaEJ8zbvLSc04tWikgMGtrRpTnfokPiKr8b_GvpI6S3N_VyXUTXbJgU8sqRJsFvo5-7YSCN_xcFm6Ma2MRvH8lU9TiCYs_Lk-X5zdQVNmCTLC5DC_lzlTyE5_98QPWZmYrMvTPR8zpbZmAS3wXk3B2eOUU0cMf7bTQAsMkNOBr1sj0k0D5bH975Hz3w4r0Ae6ujkuPoXz1wNSGgNQJjGWfpwT0VFs-KdMVZAQdTYB6f_ebkKmF6Lfas6YbwZFZqo2k6jgInUU7r-gCZ_3sY_BXz3zqTCABwVdhcMh-UowZUymlAIjjdUEo0EKFpSqQj8d_k3TxpkIsoiuEzZVqCt_Z2cX0M_YLqT3TSZVBSv8VbYt6n6joWrfiMAFyZ-ZQ0OP7q0vpfWSWEMGhupK8bUc58KeVMezFBEsRbG4eQS_6Jj0A7wIptqva6-WoD6Kwnl8dMxRVOm_hNDS0WXf1NALMYeyGZO93yOK-thXXT2d8wm2LEwRhXocaz8YNpF6vvEHeTdywl1MKJAqy0xYx-9Qt3zXCw65FlUAOJq7soBPImiwV2VTDIA4Rt_Jw6mQE3SxyFHxJ5qRvjP-ff6nhAxOkm981HdoRi-gfa6KsoWiM_I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🇺🇸
بسنت، وزیر خزانه‌داری آمریکا، درباره ایران:
همه خواهان پایان یافتن این وضعیت هستند. ۴۷ سال از عمر این رژیم شرور می‌گذرد و دنیا دیگر از دست آن‌ها به ستوه آمده است.
مردم ایران مردمی عالی هستند؛ اما رژیمی سرکوبگر بر آن‌ها حاکم است.
یا رژیم از درون تغییر خواهد کرد، یا مردم قیام خواهند کرد، و یا باید دید چه پیش می‌آید.
ما آن‌ها را از نظر اقتصادی خفه خواهیم کرد. آن‌ها در وضعیتی قرار دارند که من آن را «آرواره‌های مرگ اقتصادی» می‌نامم.
ارزش پول ملی‌شان در حال فروپاشی است و صادرات نفت آن‌ها به صفر رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71103" target="_blank">📅 18:30 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71102">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13cf8fb01d.mp4?token=vhsRO-P8qkfou7J80DbfX5sjJ-dTLkvYEwLE_rYSTkH3M8tiheIrbfZav0uCy1AB3qAGXDSusARIERZlFu5Dvo_GQPiRf4FymGoLRTMdqdL2MhlaMD_M-4WK9RuTMMOUSWm1x2sDJiKuztz0frAmzb_IrT0Ym_7EZ6GgjMaMbYFjhHdm1SHuzdKc5eTZrJNoFtDOHoCymXOrH963uvn-3BJp5L5SMnOZw63uShQHAuytnyBD4fCB1jfVZA86CO9y-guviocc76cfje2HZb4evxbDuwuSMU1ryEvRXivomYuemrTX5eTGPYTjvFroUz5O9H41Ts7wZSAihTDM7qM_OoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13cf8fb01d.mp4?token=vhsRO-P8qkfou7J80DbfX5sjJ-dTLkvYEwLE_rYSTkH3M8tiheIrbfZav0uCy1AB3qAGXDSusARIERZlFu5Dvo_GQPiRf4FymGoLRTMdqdL2MhlaMD_M-4WK9RuTMMOUSWm1x2sDJiKuztz0frAmzb_IrT0Ym_7EZ6GgjMaMbYFjhHdm1SHuzdKc5eTZrJNoFtDOHoCymXOrH963uvn-3BJp5L5SMnOZw63uShQHAuytnyBD4fCB1jfVZA86CO9y-guviocc76cfje2HZb4evxbDuwuSMU1ryEvRXivomYuemrTX5eTGPYTjvFroUz5O9H41Ts7wZSAihTDM7qM_OoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
بسنت، وزیر خزانه‌داری آمریکا، درباره ایران:
ما بانک دیگری را که با ایران مرتبط است، تحریم کردیم. هفته گذشته، یک بانک مصری را که پنج شعبه در دبی داشت و ۱.۸ میلیارد دلار در اختیار این رژیم قرار داده بود، تحریم کردیم.
امروز بانک دیگری را تحریم خواهیم کرد و احتمالاً هفته آینده نیز بانک دیگری را تحریم می‌کنیم.
ما به سیستم مالی می‌گوییم:
ای عوامل مخرب، ما می‌دانیم شما چه کسانی هستید. خودتان هم می‌دانید چه کسانی هستید. کارتان تمام است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71102" target="_blank">📅 18:27 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71101">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
⭕️
🇹🇷
🇮🇷
وزارت خزانه‌داری آمریکا سه نهاد مستقر در ترکیه را به‌دلیل ارتباطات مالی و فعالیت‌های مرتبط با ایران تحریم کرده است:  Golden Global Portföy Yönetimi Golden Global Varlık Kiralama Golden Global Yatırım Bankası
⏺
هم‌زمان یک مجوز عمومی برای دوره جمع‌کردن…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71101" target="_blank">📅 18:23 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71100">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
⭕️
🇹🇷
🇮🇷
وزارت خزانه‌داری آمریکا سه نهاد مستقر در ترکیه را به‌دلیل ارتباطات مالی و فعالیت‌های مرتبط با ایران تحریم کرده است:
Golden Global Portföy Yönetimi
Golden Global Varlık Kiralama
Golden Global Yatırım Bankası
⏺
هم‌زمان یک مجوز عمومی برای دوره جمع‌کردن معاملات (wind-down) با این نهادها صادر شده است
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/71100" target="_blank">📅 18:14 · 13 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
