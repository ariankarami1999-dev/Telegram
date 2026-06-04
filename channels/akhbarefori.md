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
<img src="https://cdn4.telesco.pe/file/DGShUanv8_LWDxyF8PR0FrPs1WjMxZyO4rPM1U5RMu0Zv7SL6Y73mjygwN7OfSNE69SMQ6NSEXslUJBgNdFjRjAEepWsdCUijUfUBpKrmLWAfsJNZk8WYywg_VfU7hqcP_FP1UEdb6fyEEz9ZWLEb9oiyY5NVJx8NJzPdtJYKTilhTv3skObCLNSSpxDVNmouCEKNmIIxOJjYXbofnan4D5swVqAOQIO1cUCdpJTUxoaDvU5k5RBo9rdkChHNbHy_bUsmR3A4JjaxJkVHngBWN38_LlzvLbu-uvvkiTux1bC2W6rLKZcXt_a_D4Nap2Gt2YBnazfEgwHk2fOHQ7zSw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.15M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-14 22:44:21</div>
<hr>

<div class="tg-post" id="msg-656217">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/148dbf71a8.mp4?token=R5L3jBeaSxGLoB3gHRyOfHttm5CcOUk1PIS7GzWfNaXDnB7CTn20WDZdRddR7D1QHLN8UDzt7nhonZql9CY3BaVmK5nkEc9keQk_45T-w80IoABT9bv5ozFerVRVYH6rXgd5nQmNHaLvH9Tv77Jj1cuxtcTMfXxMCUrirTP8p3Fz7WqWIbvtbkNnLP54oJkSDxK-vnIvMx8axagKSMobsyN8JVc_P0zCiEb1YwQzmm9t-Tz6vhRlsoDIEVPn5ZX8NuCtyivii5Cx3u-9bUpTr1IYMaSw_vhqnUjc6GH3COsW6VDe80ZU04EHMUGjDqwNWRuoD-xQJ_VCwPhuwxcohQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/148dbf71a8.mp4?token=R5L3jBeaSxGLoB3gHRyOfHttm5CcOUk1PIS7GzWfNaXDnB7CTn20WDZdRddR7D1QHLN8UDzt7nhonZql9CY3BaVmK5nkEc9keQk_45T-w80IoABT9bv5ozFerVRVYH6rXgd5nQmNHaLvH9Tv77Jj1cuxtcTMfXxMCUrirTP8p3Fz7WqWIbvtbkNnLP54oJkSDxK-vnIvMx8axagKSMobsyN8JVc_P0zCiEb1YwQzmm9t-Tz6vhRlsoDIEVPn5ZX8NuCtyivii5Cx3u-9bUpTr1IYMaSw_vhqnUjc6GH3COsW6VDe80ZU04EHMUGjDqwNWRuoD-xQJ_VCwPhuwxcohQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وضعیت آب سد کرج، امروز
#اخبار_البرز
در فضای مجازی
👇
@akhbare_alborz</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/656217" target="_blank">📅 22:44 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656216">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l_um_4aA0pMvK0plUChVDobxsTSMMC9nF0Czrn2CvotZUkB9M27xu7DCVJWoDYcwUujLWnuBI42iB53PVDLiUTYmERXUbEI3UrcIvRvepwHjH5j9vE35nl40mwvWMHYuk3-9-Q_XMR-LUHKm0aln9bnDi8h-wvGi3G2JNv0sGAbsYwU8kITiaf2aJG3F6_aHv7Gv4-GCq88EAYJqjo3Bip4HyL2O71MUb579ehy6bg24FzlArmfax6NP257VWJvV1XVPnups09wiuAvZrR263kmVvPziQdU-P1eEp218tN2eM4IvylF3BSRfiQV-ap6J7cx9Fs0hU3d8tjT-SKyqrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کشف گروه خونی عجیب؛ فقط یک نفر در جهان آن را دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/akhbarefori/656216" target="_blank">📅 22:36 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656215">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">نماهنگ حیدر حیدر</div>
  <div class="tg-doc-extra">سجاد محمدی قرار مداحی /  @gharar_madahi</div>
</div>
<a href="https://t.me/akhbarefori/656215" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✨
بر دشمن مرتضی علی لعنت حیدر حیدر
یا ضیغم المهمهم و ای نور منجلی حیدر حیدر
یا مظهر العجائب و یا مرتضی علی حیدر حیدر
🎙
#سجاد_محمدی
#عید_غدیر
💚
مرجع رسمی مداحی
👇🏻
👇🏻
@gharar_madahi</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/akhbarefori/656215" target="_blank">📅 22:30 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656213">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a5e53b53a.mp4?token=u5vVk3l-4H0NzroQ6u797yRV6S1p0LGoONYMYEy_9O3NQwtQhQ_ypDlSrW8yiVbd3zs_2ktLzFjxYBNfu-g966c_EJCwJCazmFKO_mdLVazB-9ZKdvVA2Qc6ZFTeUrMqn7OziqMKm4Mnv7NPtQ4jWZcTNNR8QOz-LHqBrVD37P5V4rRdrmzNmf8Dbu_mDzyIo7y70N-3uEU-pdH8jgH4kaI537nv0k6oOUkuTb5aj2mG9DRG4znJZ3EyKRx6D79T045BmmHypce27RIT_VwIAmPWsbVH36f48-JVdGulXDLXxznmYhe9sdGJOldWHiwrOyFNAwWxOEirj3rF8q_4Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a5e53b53a.mp4?token=u5vVk3l-4H0NzroQ6u797yRV6S1p0LGoONYMYEy_9O3NQwtQhQ_ypDlSrW8yiVbd3zs_2ktLzFjxYBNfu-g966c_EJCwJCazmFKO_mdLVazB-9ZKdvVA2Qc6ZFTeUrMqn7OziqMKm4Mnv7NPtQ4jWZcTNNR8QOz-LHqBrVD37P5V4rRdrmzNmf8Dbu_mDzyIo7y70N-3uEU-pdH8jgH4kaI537nv0k6oOUkuTb5aj2mG9DRG4znJZ3EyKRx6D79T045BmmHypce27RIT_VwIAmPWsbVH36f48-JVdGulXDLXxznmYhe9sdGJOldWHiwrOyFNAwWxOEirj3rF8q_4Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قرائت زیارت مطلقه امیرالمؤمنین(ع) توسط مردم در میدان انقلاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/akhbarefori/656213" target="_blank">📅 22:23 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656206">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uWSCSBF0NY5LQ0TtHa6KhvjyVxlQ7Q30BXflVShRYx1m_yQHZgVNhMVUtFY6b20uRl06MOa_r0vT4RIBNrVUEAHInZKa3NajPLSBVlYBlPdrPvELoJR2UAbQQMl3fNypBvrGUv9rz9N9pG0rlotAXLEo7WtSS_EDW2Okp3cBceAoF6psoo9Rl0QpQPg4g1lu7pjK3rvgpSG1bHJ_86JEhZN5FDhCmX0YGUKLy50SgPmi3YRPH15yXyibEg44SE7-IbRURmNL2CF1AgX2I-Mp4dr2I_q8UUGDXOA7UFF5Ad3ArkUGldNQG_fmiXWm_HkMvLUzr27LyOfplsFcyiWWzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LEsmWA3eoKol9J-357QyjAsIBZFpid2ZD5-lG9zbLqxWmwkBlHJUdjml8ff8TKKrye554c8TdWzj1GEIwgzTJmyM_ckAsF5uc2YDqnHvCvwdr-eD77FsPxD3oo6aBf4mP7YNIgE5NlhJaOF1HpjSeslW5tY87tBpaus5Z6L16edrEXEy95hxZjQPT5yK2wgnlm7JJmEIYFucLeiVR8xtZkGzWgnjt3ZSrUGkj3i1zOZD2AEihSkr6eCVpIxyYtdR0C0GN4hHie9iZxvnz67SrOmez-4P_kio_pw6Nt19MCQranvwwTCfx_IlAC9KS6nOGU7jUD1iV_FNZYMAzT-yHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mtT2O4Wrpd2xeAyHJq_Z0xTCnU55EkyfByzZAD9E_U8ET_tgMzsrOlc2k2vSh1DRZd6jVWlZs-rBwXXxQpteOOAp4u6On2SO3IZ5JNNefanZ9yRM0ufWbFGpqKGAi125GuxWqiq1-nmZqAj0h2FSEDdFl2qODsOGrt18z7OAhlnF1lRom3fBkG8pqdFGyMaWojhNeARvDrC2-IyY7omakD3bZZy0NnzuLwOcBCK1mQ4djm2aS9gy6DOTUQlllTB5XIhaiTDCRPCqSrna-CijszpECHTQvJiZq_KfjcnGb5h1XIkiabk09ZrbZ5kz5yQK6_tlXyPNtlpd9ma3N1BPzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lGYGR1agnR8i4YN_9gXRW_aLMbPQwKv3Y3JlMxXejyJJtUIfygtpEey5mrfMqU9y01aIsdKEOqQ5oceVIyPozhcPYVKn9JIJkINLRd4TQxCXSeFTcyc6Mcu1ppaTbjDkrOoF-EOpgHuw__Jo_-cDEFRmguRlpFcRePaSAFaxUG0rGw8fwsEDMF1VJCdN3zwVBJmscH3tmiwz5OWz_kLFMagxLqQE-roU52yolUj1JUxdxCyIqogwIqT2A1EkX5mdt5yu3kb1kFaf8yJu6QBNVZcrAil2PAycDwtvce7jwSkf6fgjNieuoIx7kbcO4jv5LRz6ut7aLTN8txd8WJCNtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MWzvcwI-8vUGzBdqML_z06u-dTHg5ZEd8b77cPP7bTYssyeihFwg_cvV6vb3g1goec8KOhfviBfYyl9xgxSTWTtd00kELe1QEmbCrSjUcepFHZ5I15MaWoPMnQMXOMaPCrpl0AB8DahFf_VjEXvHTn-oGxGDztY_AQlVakto56HzdChxVqiApeVWzXfvYU303fw0p2K48dW2-3nsIIqUGeKnXrmlyAC3ZZDj9lZx5szSptdkHl1CEO54Y4hMPRN7_w51Ly7FzEuElhpDts2iiO2fMCHnqNB1PGvkBiTZJylQsHvfyRDa_Y4XFdWECGRCj_zjTKY-EkWyz4yivyZgJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YAS7W1qFma4gRsyrMdcoD2WPQQoJAV8xyr14_HgQezyP6AJIX5PRPUb3DOx0MHtQ0TTdNhLJw_9Dy_RS9ckcVSMqb4aui12vbHvpBdqCA8zhtJW-w5V2zxZ_oHHSzjj4c7m2cX2ryKALuhfTi7yhak2UUI1aTt5N_66vN3DrO_fVXqVdMyjPg6k9lxb7HpYlIbTI-a1wF279-xDi0BASBcLI6PoatEQH2NlzsY9OHQotMhi5lIfJXpsRarhjLanomvJXRSbDUrjck9av6McO3whcMV3HfnTC7JAEEPQc188Zli3aa2QcAfJyrdoBhjPfwRWA6cqC7NqJLG-PRlrX7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yu8Bx2Gf0ej-wc1SlTQ63uD6RopqxBFRo4NqrtAZCr1Zk-WEkj68MTZMc1mfGNUeXLw3Ff7rQUK1kyY-QGnQvemOQS8kE28UXdjTQpZ0P_1oZ_ehHZP-Ti04T81AayHI9DSoCaAkNGM_p1BR2zVvk51dZDfuXBlQA0fO78HPOt2G8ELeNhYRCWS0hLW0YBVWHM2Yg3USFkxtrrfrL7bV6DCTEDDWs51knpO6Xj4barR4iS-n9pJ530XbzO8gdpUX68L3a6qaqEkDJ4DSO8YM9EILuQB7egWCl3ItEz8TuvnsIu2Nh3IpD5u_F5dCOO4WBJ-F7O8HMzEGoQVZUxVPIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💚
دنیا محو اقتدار ماست
اسم حیدر ذوالفقار ماست
▫️
این برنامه به همت هیئت قرار و مجتمع فرهنگی امیرالمومنین در حال برگزاری است
@Heyate_gharar</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/akhbarefori/656206" target="_blank">📅 22:21 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656205">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
عراقچی: ما در طول جنگ اخیر شواهد بسیاری داشتیم مبنی بر اینکه آمریکا و «اسرائیل» از آسمان و خاک امارات علیه ما استفاده کردند
🔹
‌اسناد و مدارکی وجود دارد که نشان می‌دهد خود امارات نیز در برخی مواقع در عملیات‌های نظامی علیه ما مشارکت داشته است.
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/akhbarefori/656205" target="_blank">📅 22:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656204">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08a09ff6e8.mp4?token=csg6B_GzmjFUJF08nH4OGHA4z3jG9C7rT6_AatX9HbJ5GbJdC20njAM-s4fYo26mRRxRP75ANpDOWS6UMTQro0LUD1JudNCflHVTGQgAQoK7Gv53zftgR-NWcRH3DmWTOdtZxl__tgXL_JjTTtf0Z__bErgeR6UCy_wCWex9BrCMflWKP_PUMWmABU1J-2OqiWHYzYdt-6AFFuVHM3i31TCle0vtAF2iUzYsaA1ShJHPlA3DYDJwwGIi2O2z5S8qn010JIMf9BJfYparHiAkunSfnMWqPeCsmESPDY9_WCLzB957EhPvHrHPitWS4q_al7MNsWdU_vdaFBZB-rjkDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08a09ff6e8.mp4?token=csg6B_GzmjFUJF08nH4OGHA4z3jG9C7rT6_AatX9HbJ5GbJdC20njAM-s4fYo26mRRxRP75ANpDOWS6UMTQro0LUD1JudNCflHVTGQgAQoK7Gv53zftgR-NWcRH3DmWTOdtZxl__tgXL_JjTTtf0Z__bErgeR6UCy_wCWex9BrCMflWKP_PUMWmABU1J-2OqiWHYzYdt-6AFFuVHM3i31TCle0vtAF2iUzYsaA1ShJHPlA3DYDJwwGIi2O2z5S8qn010JIMf9BJfYparHiAkunSfnMWqPeCsmESPDY9_WCLzB957EhPvHrHPitWS4q_al7MNsWdU_vdaFBZB-rjkDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نذر باحال مغازه جیگرکی در مهمونی ده کیلومتری غدیر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/akhbarefori/656204" target="_blank">📅 22:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656203">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1992f9d726.mp4?token=L5iVU-m5un0lZoW66-NFl84wcX1wl08e4Fy-R32ELJiY9q419JFRNuQCwtY2IdzUqI0Q18ZTgLy9j-AfRLQ2Jqc_xhZyDOR0nzbM3oQiW1Cuphzut-1Me0AFAL5xHutUZHJTpcRvt3kPBelhBb-5scLSj8srsZ3qr3gFXWjbtGqOfN5Vo5DdMdxSCL61yuBfMmM_1dIHJ04p-RxeGD84WFNuNVxDYlPok0QdFmTg0jNTvQe9qLQfBmpdQ5BueJJmlQVqm-cOczCMf6gg8-tff7ugHPCkPRinkMpPdwMSLeRsPVz7aBJKQiWI0jBDv-3IdLuKCQ1c9BY6GxKH9j930g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1992f9d726.mp4?token=L5iVU-m5un0lZoW66-NFl84wcX1wl08e4Fy-R32ELJiY9q419JFRNuQCwtY2IdzUqI0Q18ZTgLy9j-AfRLQ2Jqc_xhZyDOR0nzbM3oQiW1Cuphzut-1Me0AFAL5xHutUZHJTpcRvt3kPBelhBb-5scLSj8srsZ3qr3gFXWjbtGqOfN5Vo5DdMdxSCL61yuBfMmM_1dIHJ04p-RxeGD84WFNuNVxDYlPok0QdFmTg0jNTvQe9qLQfBmpdQ5BueJJmlQVqm-cOczCMf6gg8-tff7ugHPCkPRinkMpPdwMSLeRsPVz7aBJKQiWI0jBDv-3IdLuKCQ1c9BY6GxKH9j930g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کار هنری و احساسی مردم در همبستگی با شهدای حزب‌الله
با شعار با هم مقاومت کردیم....
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/akhbarefori/656203" target="_blank">📅 22:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656201">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a1caea1f3.mp4?token=phPyUZNQBjAQRFcBTJlyIjYN1aCoSA5uDC75GWyML16KCZaCO2zjiWUlrRunbOIXiEBd5Y6tQw9kS6H4_D_9LcGLutVjV5QdueGnVNqvu25XtUgp--MXEH97y-0X_yPrzxmdmHhBgFk6v262fR9S8DtG7lsppRwjXmGsN-wC5i6KBuC3LLxmoDOpBaT9a56dGWPdbhgMg06nb9H82TLaWku47EZ7MXK-mi4DVwq4F5Apdoe358vNSQo0fb5i-nsQM0eWs3iDRHUETj844ZtDttuyQsxrOdxzu0bDcINzI_lbRKuQbCdA5EDptrkqKOSt3sndpOFYPfESByu0trsAKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a1caea1f3.mp4?token=phPyUZNQBjAQRFcBTJlyIjYN1aCoSA5uDC75GWyML16KCZaCO2zjiWUlrRunbOIXiEBd5Y6tQw9kS6H4_D_9LcGLutVjV5QdueGnVNqvu25XtUgp--MXEH97y-0X_yPrzxmdmHhBgFk6v262fR9S8DtG7lsppRwjXmGsN-wC5i6KBuC3LLxmoDOpBaT9a56dGWPdbhgMg06nb9H82TLaWku47EZ7MXK-mi4DVwq4F5Apdoe358vNSQo0fb5i-nsQM0eWs3iDRHUETj844ZtDttuyQsxrOdxzu0bDcINzI_lbRKuQbCdA5EDptrkqKOSt3sndpOFYPfESByu0trsAKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برافراشته شدن ابر پرچم ۵۰۰ متری حزب‌الله لبنان بر فراز برج آزادی تهران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/akhbarefori/656201" target="_blank">📅 22:16 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656200">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/827e4e7f2f.mp4?token=cyS5gJ0EHR3GIRBl4ir77Jgm47zJkEB7IkG6z28xdSzby3zzFU92KHZfy3LLUkaP7T9TrbJYw8OZ8zQ2sCyxjKPiGsfgkp2ui43sjwjd4jMJd6TQzgVJcW-2rZsB6aKWdxaATqsic1Z2u8Ia9rd3qLn4W_W3kCdE5nAfj9mU6QkEEMVBG4fCGWzsbJawVXjwDvFdwwc5JU22F2mb5wKiCyNcD0cqYMESkZ-LNPoJibIH8DpjsvIp8PF5z-iTCcv-JvOH1KGQQVFk4pReAbkUrhC5PGerdJBXrYFqs0Kqm0Al84teKb_VfLMLj_YcqfdIs5OL0DIDT4MOWd6k5b0RXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/827e4e7f2f.mp4?token=cyS5gJ0EHR3GIRBl4ir77Jgm47zJkEB7IkG6z28xdSzby3zzFU92KHZfy3LLUkaP7T9TrbJYw8OZ8zQ2sCyxjKPiGsfgkp2ui43sjwjd4jMJd6TQzgVJcW-2rZsB6aKWdxaATqsic1Z2u8Ia9rd3qLn4W_W3kCdE5nAfj9mU6QkEEMVBG4fCGWzsbJawVXjwDvFdwwc5JU22F2mb5wKiCyNcD0cqYMESkZ-LNPoJibIH8DpjsvIp8PF5z-iTCcv-JvOH1KGQQVFk4pReAbkUrhC5PGerdJBXrYFqs0Kqm0Al84teKb_VfLMLj_YcqfdIs5OL0DIDT4MOWd6k5b0RXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اجرای متفاوت عبدالرضا هلالی/ خواندن به زبان چینی در میدان انقلاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/akhbarefori/656200" target="_blank">📅 22:15 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656199">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-text">✨
«مست نجف» این بار با صدای عاشقان امیرالمؤمنین (ع)
▫️
اجرای قطعه مست نجف توسط کربلایی علی‌اکبر حائری در اجتماع در پناه غدیر مردم مشهد
@Heyate_gharar</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/akhbarefori/656199" target="_blank">📅 22:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656198">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
عراقچی: پیش‌تر به کشورهای منطقه درباره استفاده آمریکا از پایگاه‌هایشان هشدار داده بودیم  وزیر امور خارجه کشورمان:
🔹
به کشورهای منطقه هشدار داده بودیم که پایگاه‌های آمریکا در صورت مشارکت در تجاوز به ایران هدف مشروع ما خواهند بود.
🔹
پاسخ ما متوجه پایگاه‌های…</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/akhbarefori/656198" target="_blank">📅 22:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656197">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
رویت زندگی ۲۰ سال آینده در حالتی وحشتناک
🔹
06:10 نیمه تاریکی که از کودکی همراه من بود
🔹
14:00 ارزش قائل نبودن و آسیب رسانی به دیگران
🔹
28:20 رویت زندگی ۲۰ سال آینده ام در حالتی وحشتناک
🔹
33:00 درک کامل احساس افراد در زمان خوبی یا بدی کردنم به آنها
🔹
37:50 کسب آگاهی در تجربه نزدیک به مرگ، باعث نجات من شد
🔹
39:45 پرسش بانوی پهلو شکسته
🔹
44:45 درک لذتی عجیب در اولین تجربه نماز خواندن
🔹
50:50 تفاوت مهم پدیده توهم با تجربه نزدیک به مرگ از نظر علم پزشکی
🔹
قسمت اول، (منفی هفت)، فصل چهارم
🔹
#تجربه‌گر
: دانیال قاسمعلی
#زندگی_پس_از_زندگی
#فصل_چهارم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/akhbarefori/656197" target="_blank">📅 22:12 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656196">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
عراقچی: پیش‌تر به کشورهای منطقه درباره استفاده آمریکا از پایگاه‌هایشان هشدار داده بودیم
وزیر امور خارجه کشورمان:
🔹
به کشورهای منطقه هشدار داده بودیم که پایگاه‌های آمریکا در صورت مشارکت در تجاوز به ایران هدف مشروع ما خواهند بود.
🔹
پاسخ ما متوجه پایگاه‌های آمریکاست و نه خاک کشورهای منطقه و در همین راستا ارتباط مستمر با وزیر خارجه عربستان داشتیم.
🔹
بسیاری از کشورهای منطقه مخالف استفاده از حریم هوایی و خاکشان علیه ایران بودند اما متأسفانه آمریکا از این امکانات علیه ما استفاده کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/akhbarefori/656196" target="_blank">📅 22:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656195">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DqrexIXbNK0-JJ14pFD5WoiM2zVYLN3E4XEiJmd8IiOlJwzlWHKopy82C4gwHP6hKHggtmmMXOlSTx0vPYLSEQi_UDaytUpulWrjDiEM0IMKjCQD2vXD2tr3dkm0iX8-_r4peT4a_Z7dIUjQHzvC04mWQKQxHbMHE_rIEhLjP5URagXoDtAnhfY1qrtPIvjzadq2ZApqKVrCXx7m58QD6lypwH0ZXb2BVbhsnM49Px8Lq6oGUj0sh3eCh9Az6O1YEyFaQYeNa721cKHLuNBr6czaMsjGQxrxNb6XEJRJBAqaBc0CFS70-D_QUXfKYSej3W2a7wasTlL-fSA7dJaS9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افشاگری یک منبع امنیتی درباره مشاور ویژه رئیس امارات
‌
🔹
یک منبع امنیتی ارشد در حوزه مقاومت، اطلاعات جدیدی را درباره انور قرقاش، مشاور رئیس دولت امارات در امور دیپلماسی، در میان گذاشته است.
‌
🔹
این منبع امنیتی فاش کرد که اگرچه انور قرقاش از حدود ۲۰۰۷ به دلیل نوع مواضع خود تحت رصد نیروهای امنیتی اسرائیل قرار داشت، اما از سال ۲۰۱۵ این مسئله وضعیت جدیدی به خود گرفت.
🔹
کشف اصلی قرقاش، در بخش امنیتی ساختار وزارت خارجه اسرائیل صورت گرفت؛ امّا نهادی که این مهم را انجام داد، ماماد המרכז למחקר מדיני (Mamad) بود که در واقع سرویس اطلاعاتی وزارت خارجه اسرائیل و عضو جامعه اطلاعاتی این رژیم محسوب می‌شود.
🔹
ماماد، یکی از سه نهاد اصلی ارزیابی اطلاعاتی اسرائیل (در کنار موساد و آمان(اطلاعات ارتش اسرائیل) است که در بیرون با نام پوششی و غیرواقعی «مرکز پژوهش‌‌های سیاسی» معرفی می‌شود، درحالیکه در واقع رکن امنیتی و اطلاعاتی وزارت خارجه اسرائیل است./ تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/akhbarefori/656195" target="_blank">📅 22:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656194">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1d4399aa8.mp4?token=RwTzVVo-um-ATAtgrP1QC8Niab_wDr2Z5Imh1m2F1H5tlkW06rLNHCe3bLyQ8XCQcTZo4DzsG2k6355FKjbjHlGFGyTlsy7n3zQBXHMYApb1ZxnCHTvrirBHJ52S77lYHE3j3js6iTkkEsYgFnKdd7kVUjCqjM5GU_x58rC2GXPA7C3DVikiEKb52EwAoHtxLcwRyvbQt42_AzRxPP6WISUD2dMTuXjD8Y4IuLP_UHnAsDQC9nEA06vJZsoCT1kV22jzhrCTB7GoYj3lcg7gtIIKTu_0hZpTekGzKWRdnIh-uk5cP5-_YB3Rh8ZWN0cD83gcbG16SOTasxCfAXdlig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1d4399aa8.mp4?token=RwTzVVo-um-ATAtgrP1QC8Niab_wDr2Z5Imh1m2F1H5tlkW06rLNHCe3bLyQ8XCQcTZo4DzsG2k6355FKjbjHlGFGyTlsy7n3zQBXHMYApb1ZxnCHTvrirBHJ52S77lYHE3j3js6iTkkEsYgFnKdd7kVUjCqjM5GU_x58rC2GXPA7C3DVikiEKb52EwAoHtxLcwRyvbQt42_AzRxPP6WISUD2dMTuXjD8Y4IuLP_UHnAsDQC9nEA06vJZsoCT1kV22jzhrCTB7GoYj3lcg7gtIIKTu_0hZpTekGzKWRdnIh-uk5cP5-_YB3Rh8ZWN0cD83gcbG16SOTasxCfAXdlig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محسن رضایی: به نفع آمریکا است زودتر حقوق ملت ایران را بدهد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/akhbarefori/656194" target="_blank">📅 22:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656193">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c7c682f9c.mp4?token=ozm_1f5dg7evUyVqrXU6UuFBpjSYSik2LGy_molduD5KkEvtp30fK2NM3eQ1ZHyUr1QXi-TAjYIViFebo5CqhmbMFHvlJ0cUKTumIT4xS40oS2XVU6nO_NrUti1kQ2NwcTR48Rb0T59UyRJDE6QR8lXvsl-ef-YI751huFx3c4KPhZbWkSq7a3HvB_mw7sBDYUpkULS4V1OPsrvnKobdugacNg_ytA8C3XAx5c6YiRoj05fJvhgsnlloUFxalO6L76-nSj0X9BEN1TKYurDnuhNRB2ACeXLkf4RBJL--8N2h1JxAZdQ8waczZdeQTk8sCniOsPm9rD89PPcB3WOWGzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c7c682f9c.mp4?token=ozm_1f5dg7evUyVqrXU6UuFBpjSYSik2LGy_molduD5KkEvtp30fK2NM3eQ1ZHyUr1QXi-TAjYIViFebo5CqhmbMFHvlJ0cUKTumIT4xS40oS2XVU6nO_NrUti1kQ2NwcTR48Rb0T59UyRJDE6QR8lXvsl-ef-YI751huFx3c4KPhZbWkSq7a3HvB_mw7sBDYUpkULS4V1OPsrvnKobdugacNg_ytA8C3XAx5c6YiRoj05fJvhgsnlloUFxalO6L76-nSj0X9BEN1TKYurDnuhNRB2ACeXLkf4RBJL--8N2h1JxAZdQ8waczZdeQTk8sCniOsPm9rD89PPcB3WOWGzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اجرای قطعه مست نجف توسط کربلایی علی‌اکبر حائری در اجتماع در پناه غدیر مردم مشهد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/akhbarefori/656193" target="_blank">📅 21:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656192">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j3dU3twq8YT3l531ttzjNr5hqibzpaSWJaVykwRdwxJV7j68ZRftklbNYj_9gm2hhCUG3BAc4CKmvCBauqsUV9bMcKLi9t7-dwVb-sXp11P6fd8cbxQObMAL_Wcx7-ROuGtPq0Svw_EAhAoSBJyZRuHLh2F6Z7prrTsnYW7oZkivUxUQCt_aB9MArTW3A-Ll1FdBVXQvmNy8n7t5h8NX79JHheAS19WRRGy4JkNpJEh2Q8YvcisKFjvoyaZP1gS6qk7uAdgmHPf2ootK7zfvT0nT_5ZkcZaWaHr-fLiyLNZZPlGy1Bc5JRgkwMm-bRhgx9l8Td-k01DqJVTIdamfqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آخرین تصویر از سردار شهید امیرعلی حاجی‌زاده در شب عید غدیر ۱۴۰۴
🔹
ساعاتی قبل از شهادت به همراه شهید سینا سهامی از محافظین ایشان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/akhbarefori/656192" target="_blank">📅 21:56 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656191">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">نماهنگ بارون نجف</div>
  <div class="tg-doc-extra">حاج محمدرضا طاهری قرار مداحی /  @gharar_madahi</div>
</div>
<a href="https://t.me/akhbarefori/656191" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✨
دل بیتاب دل بیچاره
سر زلف تو اسیره
شب عشق و شب مستی شد
دلم آروم نمیگیره
شب عقد اخوته بازم عید غدیره
🎙
#حاج_محمدرضا_طاهری
#عید_غدیر
💚
مرجع رسمی مداحی
👇🏻
👇🏻
@gharar_madahi</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/akhbarefori/656191" target="_blank">📅 21:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656190">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
گل دوم برای ایران توسط رامین رضاییان در دقیقه ۵۵
🔹
ایران ۲ - مالی صفر
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/akhbarefori/656190" target="_blank">📅 21:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656189">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
پوتین: روسیه آماده نقش‌آفرینی برای حل مسئله ایران است
رئیس‌جمهور روسیه:
🔹
مسکو به دلیل روابط نزدیک با تهران قادر است در مسیر حل بحران نقش‌آفرینی کند.
🔹
بحران اوکراین مسئله‌ای محلی است اما وضعیت ایران ابعادی جهانی دارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/akhbarefori/656189" target="_blank">📅 21:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656188">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
ادعای یک مقام آمریکایی در گفتگو با الجزیره: آتش‌بس با ایران برقرار است، اما ما به حفاظت از نیروهای خود و اعمال محاصره بر بنادر آن ادامه خواهیم داد
🔹
یک مسیر کشتیرانی آزاد از طریق تنگه هرمز وجود دارد، اما این به کشتی‌ها بستگی دارد که تصمیم بگیرند آیا عبور کنند یا خیر.
🔹
از زمان اجرای آتش‌بس با ایران در ۸ آوریل، تقریباً ۱۰۰۰ کشتی از تنگه هرمز عبور کرده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/akhbarefori/656188" target="_blank">📅 21:48 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656187">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ca617cbb1.mp4?token=gj0eRvssAf_mDgf3iTzdNvnj07H1MmYsnPPw7fS_xKVJW6ETaadBVnLdf_F29bkEMKwMsgO3FXX32zVGxNBMi7237cpHyoSdiF--9T3CxhnQWrY-w-0aQhfRIUXZk-j-_FeBazFWmd17glXdm1NZ62xFVH47Nod87iqsHl8tnCnZ2cFKW78eoccbKzQYCCMLITHC_t4ALlLNafQNxf9UIC3u9FqrrljYAXnDF4BzTQHUuUKku8qBLakda9gYg2ZKd_9qvCbcvn4kwxVlLPkiFotdlNnwLvX8jSvl9MbHlC5kygnCYTUCsjl-EkJrzplvHrXyJtjnjeGEYdSV309-ElBOg7HzGSARZ7GgSrOEUQu9zuzmT51OvQ_818JxFuPbKYociv7sUU7PyyaDyvq9485cRNzCHp_JH5Pps5DmWJiW6-CWeuAnP1HXh0NO-R2yRujcgCWhf5p_dZ092CNN9hUCUx2ECCrvHnCeBvvK9uUD6fI1Pi_EYLGMKRtIUsmmSF-cIEg13kmlLLLLY5rzqmJMvOSlyOCMVFWrUuOJWXfnu2XSo83YcLHFWWed6gCs_mYXsa06nwg5cUcyzzhxMQTn1FSM0EMlX1-mfGVvhvg6CXzDlTtKi9z4SB9EN6uiUtonoy4C9l9c2KnhbdFDIdIdRXpBEy8Ji_8aKfzKfXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ca617cbb1.mp4?token=gj0eRvssAf_mDgf3iTzdNvnj07H1MmYsnPPw7fS_xKVJW6ETaadBVnLdf_F29bkEMKwMsgO3FXX32zVGxNBMi7237cpHyoSdiF--9T3CxhnQWrY-w-0aQhfRIUXZk-j-_FeBazFWmd17glXdm1NZ62xFVH47Nod87iqsHl8tnCnZ2cFKW78eoccbKzQYCCMLITHC_t4ALlLNafQNxf9UIC3u9FqrrljYAXnDF4BzTQHUuUKku8qBLakda9gYg2ZKd_9qvCbcvn4kwxVlLPkiFotdlNnwLvX8jSvl9MbHlC5kygnCYTUCsjl-EkJrzplvHrXyJtjnjeGEYdSV309-ElBOg7HzGSARZ7GgSrOEUQu9zuzmT51OvQ_818JxFuPbKYociv7sUU7PyyaDyvq9485cRNzCHp_JH5Pps5DmWJiW6-CWeuAnP1HXh0NO-R2yRujcgCWhf5p_dZ092CNN9hUCUx2ECCrvHnCeBvvK9uUD6fI1Pi_EYLGMKRtIUsmmSF-cIEg13kmlLLLLY5rzqmJMvOSlyOCMVFWrUuOJWXfnu2XSo83YcLHFWWed6gCs_mYXsa06nwg5cUcyzzhxMQTn1FSM0EMlX1-mfGVvhvg6CXzDlTtKi9z4SB9EN6uiUtonoy4C9l9c2KnhbdFDIdIdRXpBEy8Ji_8aKfzKfXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
حضور پرشور مشهدی‌ها در جشن عید غدیر
▫️
این برنامه به همت هیئت قرار و مجتمع فرهنگی امیرالمومنین در مشهد در حال برگزاری است
@Heyate_gharar</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/656187" target="_blank">📅 21:38 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656186">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58c9c8c965.mp4?token=RFMYAb7RJp8EAIrSuvHPjJuJF9X59gLOGTOvifvJAV4bIU37h-qcFkXKOigCqQXmtJf5CyyQUFfzR_Tty6K-ar330D7ORylLaVb06knnbbG6DJP4KoenhesDxgQ6ccgL4TEfJiIOs-v0503ht8LoVMYIdN8tayCTio24qlv6S30mSTkhrDby21S5Fa9b3VzaKvYmnZLH7XOw0GWnN0k-Mke9eaPt1bJGzQnQeSSiJQwjBJFNEpKg4btleDPhpLCrxw-0QMS8v6PkHzd8jSmOwmjGhOjhny7SC7ngMeeczYjWNuWczHJYeN3LqK1tJ5VZaioz5GkuYwOuKduT1Rz0irCt3Uqhou4NvBTSMmMeptbUY4cbuqaJBQmC2Hz1dkKkgnHyvNMOu4VBNX7a18JDeqD_XrxVu7tE8XA_Dgp1ru2Y5UyCtShsCyYoYfwLYakKE-qzcICzH20Uf1litySHeQgR9GYWjY3oaLLoT-Jol2F4MwbH5cLwriQ8w_mYhJ9HseQoKhFztfsi_WGLDdDBfo-SzCk9GGHbhHGzW6apTBIrt0EwHf5gYeq08D-EnrHozVD__ZFJjuoCkXfIfFdoL2ftqeXvcrVhEIV15UwnPreU7xRilPnYH_Fk_GZDmz4HKSt7dPvGxkofEuAejhLd5ibO84du5Lw8eoYZXs02i64" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58c9c8c965.mp4?token=RFMYAb7RJp8EAIrSuvHPjJuJF9X59gLOGTOvifvJAV4bIU37h-qcFkXKOigCqQXmtJf5CyyQUFfzR_Tty6K-ar330D7ORylLaVb06knnbbG6DJP4KoenhesDxgQ6ccgL4TEfJiIOs-v0503ht8LoVMYIdN8tayCTio24qlv6S30mSTkhrDby21S5Fa9b3VzaKvYmnZLH7XOw0GWnN0k-Mke9eaPt1bJGzQnQeSSiJQwjBJFNEpKg4btleDPhpLCrxw-0QMS8v6PkHzd8jSmOwmjGhOjhny7SC7ngMeeczYjWNuWczHJYeN3LqK1tJ5VZaioz5GkuYwOuKduT1Rz0irCt3Uqhou4NvBTSMmMeptbUY4cbuqaJBQmC2Hz1dkKkgnHyvNMOu4VBNX7a18JDeqD_XrxVu7tE8XA_Dgp1ru2Y5UyCtShsCyYoYfwLYakKE-qzcICzH20Uf1litySHeQgR9GYWjY3oaLLoT-Jol2F4MwbH5cLwriQ8w_mYhJ9HseQoKhFztfsi_WGLDdDBfo-SzCk9GGHbhHGzW6apTBIrt0EwHf5gYeq08D-EnrHozVD__ZFJjuoCkXfIfFdoL2ftqeXvcrVhEIV15UwnPreU7xRilPnYH_Fk_GZDmz4HKSt7dPvGxkofEuAejhLd5ibO84du5Lw8eoYZXs02i64" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حجت الاسلام محمد برمایی در برنامه در پناه غدیر با حضور جمعی از مردم مشهد: حتی یک نفر هم در شهر میناب نمی‌خندد چون از هر خانواده یک نفر شهید شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/656186" target="_blank">📅 21:35 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656185">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fec7f8a30a.mp4?token=hr4mLDwuoYg5XTbGpQCGcj07jojOtno-sBjcRBEatDT1AY8w-1g8u8tBhn0DSVmLDGQWonp92LtYl7r1nsy7s4WHBVelO4QfSMg7OSCxXreAxXfhGJIhFhP4RBBc01a4-L5hAKJr47FxJ_ixB4pqaPTuP_NyN1Zu-yJ-bLFNnManHSc6JCNzEI1UIsUv22kbgE25PEA8RLb9txfhTncXND8Hh75JxGhdgY5HCnqhF438AUc_u8ah-HtJJmivocRQVsfrPnPK5EeqiJ1PaIAKNcN6B8sFZTO5ruhUYUJaqZe4rAY_RyjfVGVwn0UEyMzIKOfO2esPuJapwL1Kt1QjNTUoB-Us9HPVAvP1rCfxIpd8Il2M4bWeZvVxDgQTqRsRBfaNxdqEVvOAR2cew9OZgsYvlfvBGfctWA5UJYlGCtcW93n5dWtBf9dqrPtj9-4HS8Ter1VaEyyRliLaxalhQmB4Kqpu5TPmsv0hhIe4kwgAFZyH8HsipeUWOYLWYnmSqwAPZXB7ZxThnWe9D3zjHovaX7xIEHcwYWe9Mcty-7nz6GYCl3MnnLrLEb0VVjkan82pIKLCBfu93g0gPLVlwzr2TmjnW3nVQLf0Eiinih3nfkvjpHvlPrD0pbtb83rF3kpbvwr216hRbBRmC6d7J98mh4HPtONU22JcGXqW5OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fec7f8a30a.mp4?token=hr4mLDwuoYg5XTbGpQCGcj07jojOtno-sBjcRBEatDT1AY8w-1g8u8tBhn0DSVmLDGQWonp92LtYl7r1nsy7s4WHBVelO4QfSMg7OSCxXreAxXfhGJIhFhP4RBBc01a4-L5hAKJr47FxJ_ixB4pqaPTuP_NyN1Zu-yJ-bLFNnManHSc6JCNzEI1UIsUv22kbgE25PEA8RLb9txfhTncXND8Hh75JxGhdgY5HCnqhF438AUc_u8ah-HtJJmivocRQVsfrPnPK5EeqiJ1PaIAKNcN6B8sFZTO5ruhUYUJaqZe4rAY_RyjfVGVwn0UEyMzIKOfO2esPuJapwL1Kt1QjNTUoB-Us9HPVAvP1rCfxIpd8Il2M4bWeZvVxDgQTqRsRBfaNxdqEVvOAR2cew9OZgsYvlfvBGfctWA5UJYlGCtcW93n5dWtBf9dqrPtj9-4HS8Ter1VaEyyRliLaxalhQmB4Kqpu5TPmsv0hhIe4kwgAFZyH8HsipeUWOYLWYnmSqwAPZXB7ZxThnWe9D3zjHovaX7xIEHcwYWe9Mcty-7nz6GYCl3MnnLrLEb0VVjkan82pIKLCBfu93g0gPLVlwzr2TmjnW3nVQLf0Eiinih3nfkvjpHvlPrD0pbtb83rF3kpbvwr216hRbBRmC6d7J98mh4HPtONU22JcGXqW5OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حجت الاسلام محمد برمایی در برنامه در پناه غدیر با حضور جمعی از مردم مشهد: مادرم می‌گفت تو برای آخوند شدن خیلی قرتی هستی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/656185" target="_blank">📅 21:35 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656184">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qCvNG9fwxc8Z3Ha3zqDQJ51H4zyxq3ht1MoznjinzdbGOlf9PEGBV1sN1nJMRMMxU77wg4yDYEYXqGk0hhin9IZB95ojY5VzgPaN1mc2iXVOVtdSt5C802ovYwkqtdTeb_SSYUBupsvF9bVUlFTYN6KvOc7iQKnLIjjHpOM0MuoUK3WErFpSOj0tcp5wblswJxSB5xmc6N3rBagD8jtOfhx-Q_mVXNCxkEjcxJwTkTHtaek8yChwsCzo3RGQWhNVkHJX0vuetpNd48o82Q-erSb8FxP5JiibIrqWMvx_QZ4QNMf4aR2fWq6kEMCc_XJGCAyhHggC1P1MOgOJl4LJFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قرآن به ما می‌گوید؛ راه خدا همان محبت اهل‌بیت (ع) است
🔹
قرآن با دو تعبیر آنچه ما بای به عنوان مزد پیامبری رسول خدا (ص ) انجام دهیم را بیان می‌کند: یک‌بار «پیمودن راه خدا» و بار دیگر «مودّت اهل‌بیت(ع)». از آنجا که هر دو به‌عنوان تنها پاداش پیامبر معرفی شده‌اند،…</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/656184" target="_blank">📅 21:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656183">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GMe6xgXfkhJsOvBWL8uO0YY62YaQi1WT93RAIVcX7ZKoiBgPueazVXE0kDB5E_Ob2yxCBpboKboIeK7FcehURc4S149oYqCUhNXFceXDxzCeuPightWJrs5tTZrzOj6jKytJ--KUozvtJY_LpYDk0o95ZExr83oKjDu526SgD3_S5tN3KRNEv_o9jf22SWYPA_3fWg23PFkDon1YACWN045Pdq4cNbiLwspc5G7TTrj8azWL9r-i42k_LDggk_pJ4cr9SOfw-7UGlHG4xm_xXDZ4gzzWKxMXixKipeMDlP3z-W9mn2Dh57eJNVGv9PtPOw0F7rG25Nrpbk_rN1KMEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استایل جدید محمدرضا گلزار سوژه شبکه‌های اجتماعی شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/656183" target="_blank">📅 21:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656182">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cf15e7412.mp4?token=Lfiv185N8UDQh0nJJQQWDmNS6214TwqT3F3NtZtj3bzSXViDM3yQLXMSHR0pbx9hHAfi5DwJXwSEmoHoEiBL0lp12vGG3D_67hnuliTAzuZYAYc0IxpoJhN4wyhMhF-jksdzVJ2D1bcOwONpm0UJh23dgO8KNdfDIANhmIsM0Hc0wjzVunvizu5QEhM3Ihvm556sV5etqSMUt644Xl9plkwfVgTJQsEckeWr1LjJej7cKAFFcvLIoYlwVX4mHF5rjfgR9c9Ye5ktMgtdDoSIk5B60cA4-wFpXoBJKi3qsqSdMzi0xS_nBNRy_hFih9z-5AWd18TKp_afA3JDk8Pn7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cf15e7412.mp4?token=Lfiv185N8UDQh0nJJQQWDmNS6214TwqT3F3NtZtj3bzSXViDM3yQLXMSHR0pbx9hHAfi5DwJXwSEmoHoEiBL0lp12vGG3D_67hnuliTAzuZYAYc0IxpoJhN4wyhMhF-jksdzVJ2D1bcOwONpm0UJh23dgO8KNdfDIANhmIsM0Hc0wjzVunvizu5QEhM3Ihvm556sV5etqSMUt644Xl9plkwfVgTJQsEckeWr1LjJej7cKAFFcvLIoYlwVX4mHF5rjfgR9c9Ye5ktMgtdDoSIk5B60cA4-wFpXoBJKi3qsqSdMzi0xS_nBNRy_hFih9z-5AWd18TKp_afA3JDk8Pn7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حضور ارسلان قاسمی بازیگر معروف سینما در مهمونی ده کیلومتری غدیر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/656182" target="_blank">📅 21:22 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656181">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4d60a9878.mp4?token=elRtoSQZ6v6dwwBttWXHD65W67tD1GSL0qmCnmqeerIv0tQvHoPhFwEOy4LXJRB2jy9OgKwnpv98jWBRLAu1AWmuMv0k1oRnq_5WKet1CewczVer4iq9jG3MW_WFYQDKDYuubCpzQ2xeJdFTyV6Og4HHZSWljQn-I5Jbzv5kSRUm_iRwkGjS3Bguj3-PbkAxm8qo1a0rYskupTCVmT9hr9HW7_okwSVQttNQ_mTcXsGZSWQGx-L8RJXBSNBzwk__T4me1FBEoDCJ35jOhADCOjUSpJtAGA9y8lN-pHabNggPO4UEoVlZQCTR512sFFwtNjCCgVSCr2ewXRLqi3DIJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4d60a9878.mp4?token=elRtoSQZ6v6dwwBttWXHD65W67tD1GSL0qmCnmqeerIv0tQvHoPhFwEOy4LXJRB2jy9OgKwnpv98jWBRLAu1AWmuMv0k1oRnq_5WKet1CewczVer4iq9jG3MW_WFYQDKDYuubCpzQ2xeJdFTyV6Og4HHZSWljQn-I5Jbzv5kSRUm_iRwkGjS3Bguj3-PbkAxm8qo1a0rYskupTCVmT9hr9HW7_okwSVQttNQ_mTcXsGZSWQGx-L8RJXBSNBzwk__T4me1FBEoDCJ35jOhADCOjUSpJtAGA9y8lN-pHabNggPO4UEoVlZQCTR512sFFwtNjCCgVSCr2ewXRLqi3DIJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک هفته حقوقمو جمع کردم امروز بیارم نذر امام علی (ع) کنم
نذری یک پاکبان در مهمونی ده کیلومتری غدیر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/656181" target="_blank">📅 21:22 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656180">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dbf214dc5.mp4?token=WtCm31XkitCyucfA_4FpJIyJMLMX3kvSOiagWF39sbaww3UbCbGVlP6lsIHjanlovIoUcE5z5pNmGpE9jOGXbC3BBNLD9cxi3RSbGHZ3lYjCcWqRh_fKpOLju9LQljXqKhXIGlgjxknEitt4vA6oSXtsW7LkTUtnoQ1pQALmf5YOgB4n5VKE5_91d_kSIWgmcBhbpgVr3TcULhw6y4krvw2xZUgbtMJ9Lirxmt2ICQEIz4N3Z7RoKnr21FB2_brXmQ04QMU6AbN9cNLm7NJGF_asDCs5R5oqei_ozJL3yYMUKOfEODRzfRc1kmoGYU8Gw_dJ2mqg6VZDh4xexMWWYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dbf214dc5.mp4?token=WtCm31XkitCyucfA_4FpJIyJMLMX3kvSOiagWF39sbaww3UbCbGVlP6lsIHjanlovIoUcE5z5pNmGpE9jOGXbC3BBNLD9cxi3RSbGHZ3lYjCcWqRh_fKpOLju9LQljXqKhXIGlgjxknEitt4vA6oSXtsW7LkTUtnoQ1pQALmf5YOgB4n5VKE5_91d_kSIWgmcBhbpgVr3TcULhw6y4krvw2xZUgbtMJ9Lirxmt2ICQEIz4N3Z7RoKnr21FB2_brXmQ04QMU6AbN9cNLm7NJGF_asDCs5R5oqei_ozJL3yYMUKOfEODRzfRc1kmoGYU8Gw_dJ2mqg6VZDh4xexMWWYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نذر بستنی قیفی ایتالیایی در مهمونی ده کیلومتری غدیر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/656180" target="_blank">📅 21:21 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656178">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b46290c09c.mp4?token=HZG4Cp8Q8MPryrnbIO4fdvJg6mlbQYYqxzqb6xl1iBpFs9RMv7ZJWMzRhzTGkgSas7ijL8xp1Z-j0Ahws8sKk6c27fDBbQPu00yXNZSRhpxb2kKH0O2n9LKtFVM9ZppN6TS6k7w6HfO83TI9kWNegfS3iciJcje3ZAW4SW9DWLgWFW6DkPDtSXZOIhnXxN71kgd4y7Mb8HiiPOZDNqfF94KD3DiKMD560C-NNQVoY-10b2708imI3SqvuUK4c4yTYedXrmt3XPEShECpsHYfmeIOY4h5uMbhv8NEIBc6OSVo3yzC18_t4VrutL4C9fiR1ZZc8IVKsvhf-_H7BBVJlkQnvIsgQ-ocGGLlsefh8SNoRB7rY7rZGKp7vUs2aOkWGodf3_LFUBrgFIT9pPEbskBYLPr2AydOJH2T_9hVGrJ-c_q9Z_j-_5usf1Uk5bkvUfCJGhaNAz1fHYVenYPR88O_d4esvvWr9CPt-kG69VQ3TD7RJymO7_aIj9whXq-jZt6dfAqAB8bN5ZhtE9jUcZXuDViTeaMJpxKsCbAGwC1O-WlDxXEgtLwM1LGJK0XmcFI7-T5rdJeqY4nrYUyfVzIgbYYXnnqEwLyvaQSl5gHoAgV_326sFDyyFitiFWQpgyBl1sNG-ekokZgw2UWlLHTJbUTojzfuhWin_HyZxTU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b46290c09c.mp4?token=HZG4Cp8Q8MPryrnbIO4fdvJg6mlbQYYqxzqb6xl1iBpFs9RMv7ZJWMzRhzTGkgSas7ijL8xp1Z-j0Ahws8sKk6c27fDBbQPu00yXNZSRhpxb2kKH0O2n9LKtFVM9ZppN6TS6k7w6HfO83TI9kWNegfS3iciJcje3ZAW4SW9DWLgWFW6DkPDtSXZOIhnXxN71kgd4y7Mb8HiiPOZDNqfF94KD3DiKMD560C-NNQVoY-10b2708imI3SqvuUK4c4yTYedXrmt3XPEShECpsHYfmeIOY4h5uMbhv8NEIBc6OSVo3yzC18_t4VrutL4C9fiR1ZZc8IVKsvhf-_H7BBVJlkQnvIsgQ-ocGGLlsefh8SNoRB7rY7rZGKp7vUs2aOkWGodf3_LFUBrgFIT9pPEbskBYLPr2AydOJH2T_9hVGrJ-c_q9Z_j-_5usf1Uk5bkvUfCJGhaNAz1fHYVenYPR88O_d4esvvWr9CPt-kG69VQ3TD7RJymO7_aIj9whXq-jZt6dfAqAB8bN5ZhtE9jUcZXuDViTeaMJpxKsCbAGwC1O-WlDxXEgtLwM1LGJK0XmcFI7-T5rdJeqY4nrYUyfVzIgbYYXnnqEwLyvaQSl5gHoAgV_326sFDyyFitiFWQpgyBl1sNG-ekokZgw2UWlLHTJbUTojzfuhWin_HyZxTU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حجت الاسلام محمد برمایی در برنامه در پناه غدیر با حضور جمعی از مردم مشهد: جوانانی که در دی‌ماه کف خیابان بودند نامه می‌نویسند و می‌گویند رهبر شهید ما را حلال کن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/656178" target="_blank">📅 21:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656177">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
گل در دقیقه ١٢ برای ایران توسط سعید عزت‌اللهی
🔹
ایران یک - مالی صفر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/656177" target="_blank">📅 21:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656176">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
شبکه ۱۴ اسرائیل از آغاز نشست مهم کابینه امنیتی این رژیم با هدف بررسی سناریوهای مختلف جهت دستیابی به توافق آتش‌بس در جبهه لبنان خبر داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/656176" target="_blank">📅 21:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656175">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
رایزنی قطر و ترکیه برای میانجی‌گری میان تهران و واشنگتن
🔹
محمد بن عبدالرحمان آل ثانی، نخست‌وزیر و وزیر امور خارجه قطر در تماس تلفنی با‌هاکان فیدان، همتای ترکیه‌ای خود، آخرین تحولات مربوط به تلاش‌های میانجی‌گرانه برای کاهش تنش میان ایران و آمریکا را بررسی کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/656175" target="_blank">📅 21:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656174">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1JYIvvRyO41EA_AoDYuGqOYhZRiWJbFSmGD0qNdgfXGfIdPnq-0kp-DhJK7nla_SMh50jSHDOv7_duLpZJUBp5RunAdjs0OGtBfDHZBkNxmIcVTZbmaW1rBJSesvoWxrNvIkuR_nq4D266HC_qSysaqDayp4aQCIZblrBxfisj8fMufGbAteiaXkSb_ngYi30kUq73-6TohA5HpaSpPe7F_M5Uyj2CrQWhzGuSDBdb--aE9ebl1QRT9V_XhMMh3JgphqlNY7Tqx8RkEAKMko6rb3cdtarHX4VOWXbzgcgdXFvtqgVGFTauttauTW5YKzVgsoYyakzg8YtHz09mGYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
غدیر را روایت کنیم
🔹
امسال شما راوی عید غدیر باشید؛ عکس، ویدئو یا حتی یه متن کوتاه ارسال کنید
💚
🔹
همین کارای ساده، حال‌وهوای عید رو قشنگ‌تر می‌کنه.
#فقط_به_عشق_علی
#LiveLikeAli
شما هم به این پویش بپیوندید
👇
@Ertebat_baforii</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/656174" target="_blank">📅 21:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656173">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
ادعای کانال ۱۲ رژیم صهیونیستی: واشنگتن از تهران خواسته است پاسخ خود را قبل از پایان هفته ارائه کند
🔹
واشنگتن به تهران گفته مراسم امضای توافق با آنها در سوئیس برگزار خواهد شد/ انتخاب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/656173" target="_blank">📅 21:01 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656172">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pSabA1bfhm04Sr_p6NT8KLX5B3aT_fN2hD8A_l19hgZuW-bhhZ1NkhsTzmBQL81wktrlmPhH-i7KgzhHCnu4yxr9i5TXvbB4QxvUKwYcqjDpRXPhHMxWgWgja-X7Wr71LXMuZkSzPJmp5kcxmu4uqx0lscyFHwugu09LDoH5kx3-j7VNDi3FalPErZU1t1DuCHnoXr3IQ2CU2THldazrosfRbKhi8Xu4aao8ltGDDGI6Is_o2vaNHTJ8h1F09XF_fN0hUPduLd1crcBMawW900YTjzYHdYXO3-pqkW80OV12QN2KERS4UVDfJxW1GL3BpBP5j9Kq0ycChFOqSslEaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آرژانتین؛ در جست‌وجوی ستاره چهارم | رویا ادامه دارد | مأموریت دفاع از تاج جهان
🔹
تیم ملی آرژانتین در آستانه جام جهانی ۲۰۲۶، بار دیگر در مرکز توجه فوتبال جهان قرار گرفته است. قهرمان جهان در قطر حالا با ترکیبی از ستاره‌های باتجربه و نسل تازه‌ای از بازیکنان جوان، سودای تکرار افتخاری را دارد که آخرین‌بار بیش از شصت سال پیش توسط برزیل رقم خورد؛ قهرمانی در دو جام جهانی پیاپی.
اینجا بخوانید و ببینید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3218711</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/656172" target="_blank">📅 20:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656171">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeb5aec45d.mp4?token=tuLbJBG4jcWntL1t6mff1AIfeNGLWG5A4EgeYOJ7JnWDfhwI6GOCabXU9glcfFn1jKtilK6kXsWKpjt2CeoPvHW65HAWNJsZLKMax8SW2fW7wi5yaWlB49pTLME5E50rZZuFyKMfN4R8IiAQHX95uLuepISQfGJbhxFReC-n22fAX2hH87zw-3sPtkkAHL1tGgMNeRl3B5c_LlwVjuXMBw9DDookhu-l5sWIkzxKk9SI_Mfm8INkyu8rkysiDT4SLCaX1PAxXl6Xlu-djuYLNhrjZS-Wl9_0NyASfpznVH-2eZHCEY5lurwI0Mn1heY3MRMRGC73uh70Wi46W0JmvRSZRjEvyudQ3bd0lmh8Br4MKUhtXY98CnI5d25UqtD1nwxqFggN-QW2CruTBIfEi1aMCHcuZzEVhCmgocXKVqk_SS_r_l_FGaNN83R12l8SYh-BifH9pahfD8KvaEtTJ7fi5W3FbSvVN5AiIb-VIdU5NiHKn7HsnMOBRRILPRg4kbxhZX80wjD--hfNAYBHKCJcB-IQkWvInmDsKkyvy7dKW7VOGf7EDdR-uyMHOUPeLtZ1wstdBcF1lCvWN5avjG7Je0d0d3iWH74o7lADh-tpyU790_MLTpAAbX4iACGNO9yd2Q65I9b5thNQBFYz7HECBR5csHUD_BU242_JXl4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeb5aec45d.mp4?token=tuLbJBG4jcWntL1t6mff1AIfeNGLWG5A4EgeYOJ7JnWDfhwI6GOCabXU9glcfFn1jKtilK6kXsWKpjt2CeoPvHW65HAWNJsZLKMax8SW2fW7wi5yaWlB49pTLME5E50rZZuFyKMfN4R8IiAQHX95uLuepISQfGJbhxFReC-n22fAX2hH87zw-3sPtkkAHL1tGgMNeRl3B5c_LlwVjuXMBw9DDookhu-l5sWIkzxKk9SI_Mfm8INkyu8rkysiDT4SLCaX1PAxXl6Xlu-djuYLNhrjZS-Wl9_0NyASfpznVH-2eZHCEY5lurwI0Mn1heY3MRMRGC73uh70Wi46W0JmvRSZRjEvyudQ3bd0lmh8Br4MKUhtXY98CnI5d25UqtD1nwxqFggN-QW2CruTBIfEi1aMCHcuZzEVhCmgocXKVqk_SS_r_l_FGaNN83R12l8SYh-BifH9pahfD8KvaEtTJ7fi5W3FbSvVN5AiIb-VIdU5NiHKn7HsnMOBRRILPRg4kbxhZX80wjD--hfNAYBHKCJcB-IQkWvInmDsKkyvy7dKW7VOGf7EDdR-uyMHOUPeLtZ1wstdBcF1lCvWN5avjG7Je0d0d3iWH74o7lADh-tpyU790_MLTpAAbX4iACGNO9yd2Q65I9b5thNQBFYz7HECBR5csHUD_BU242_JXl4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیل جمعیت در خیابان‌ فدائیان اسلام مشهد
این برنامه به همت هیئت قرار و مجتمع امیرالمومنین (ع)برگزار شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/656171" target="_blank">📅 20:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656170">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
وب‌سایت کپلر: چهار نفتکش دیگر از محاصره آمریکا در تنگه هرمز عبور کردند
🔹
به گفته شرکت ردیابی دریایی کپلر، چهار نفتکش با پرچم ایران که در مجموع حامل هفت میلیون بشکه نفت بودند، روز دوشنبه از تنگه هرمز عبور کردند که این اولین مورد از ۱۷ آوریل در جریان محاصره بنادر ایران توسط آمریکا به شمار می‌رود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/656170" target="_blank">📅 20:51 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656169">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">نماهنگ شرف المکان بالمکین</div>
  <div class="tg-doc-extra">وحید شکری قرار مداحی /  @gharar_madahi</div>
</div>
<a href="https://t.me/akhbarefori/656169" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✨
شرف المکان باالمکین
ندیدم مثلش روی زمین
همه عالمو بگرد و بعد
نجفو ببین نجفو ببین
🎙
#وحید_شکری
#عید_غدیر
💚
مرجع رسمی مداحی
👇🏻
👇🏻
@gharar_madahi</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/656169" target="_blank">📅 20:49 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656168">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1de75e5851.mp4?token=SJNpMJmuEunXwV3FyB2EOt5rcE8agc8wbgo_lHOn4ooUdH7a03M4sjrw_0HtMyYPhRiMCqQiyhoKQhR3PU35P71rjbs9cAmw7tmrI3q99yuCrYHVUC97Xm6iaal23ZhpRN3iSF0AbApG17EFeaUpR8CPeaQhmbmgJ8tF1i4usRIVOTSrBiK_gBZTL54zsD2JIfxmnQdLX5Kh3k3YEBDsXGduYs-m3xZPqgd-keCrY_fVtiR38C4StAzyf6KtMAdJF4cipokiWxJIfTZhQq7nRmAtNvNqOgQ--Zna3koPaAkgCpwTl4DAHx6ffN6v-TjTnywD2coI9AOHCBxkgeODaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1de75e5851.mp4?token=SJNpMJmuEunXwV3FyB2EOt5rcE8agc8wbgo_lHOn4ooUdH7a03M4sjrw_0HtMyYPhRiMCqQiyhoKQhR3PU35P71rjbs9cAmw7tmrI3q99yuCrYHVUC97Xm6iaal23ZhpRN3iSF0AbApG17EFeaUpR8CPeaQhmbmgJ8tF1i4usRIVOTSrBiK_gBZTL54zsD2JIfxmnQdLX5Kh3k3YEBDsXGduYs-m3xZPqgd-keCrY_fVtiR38C4StAzyf6KtMAdJF4cipokiWxJIfTZhQq7nRmAtNvNqOgQ--Zna3koPaAkgCpwTl4DAHx6ffN6v-TjTnywD2coI9AOHCBxkgeODaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اجرای زیبای گروه دختران زینبی در شور عظیم مشهدی‌ها در مهمانی غدیر؛ هم‌اکنون در حد فاصل چهارراه نخریسی _ چهارراه چمن
این برنامه به همت هیئت قرار و مجتمع امیرالمومنین (ع)برگزار شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/656168" target="_blank">📅 20:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656162">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sEh1ea_NxBIFpKeAdo42aEvWG_w-g0Up-w8VakzCYsuCWt0NO6r9PFW61QEG5o883tbRtzSlxlxln-FHNFZyfPn0l5x5TKHIPRG_wEYlkxtqrNA8M8Iv3ugU3jTZ0iHe3oNJmb8IEugU_htc6FZ9oJd3YrNna6homLc-TT_gknaqMcOjBVXxj5wzvN88b_Hh_-KfIYnJBuUPOMplLsmgh79u4u3U4gyvWY8Rjh4hT-QKsHUAj1VBk89nZG84w67L9eQCcnMs0KOVnzmnRKyZjIYnb9LeqkQau4oEvZ8OOvoIuOZKy0dF797_JY5gjnA5tZptWQZIrHN65WS7Qd6Ovg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YnLEHVlnipz8rWB4zTPv-HBeAwWot4Gz5Ld8OBnLVgyBS1CudsMq8bN3kkB795g-09jVpC5dcGgqM2TUJ8GpVmup7uFypLC0wzVawXEFQHeIaAmALcVnpc9ioUXOPsGvpOK4YKRK7fh7J0zDoVcsXyU742bnTxo1sJwZnAke-NVLjrxnSqM039th_gV4S5uIs7G7GFBUUD1Vj3UPD9wI_EPd-RVMa06t4Be7SyVYrKM6DZRgZgItlqbF7WoCZoM3uJtMWhrrFnd2DcO-xRS6E0vRX2ApZ4aghD6AIxLceHx9gcFWOEBfhM73fVpsebiDjiDQbwsTpMAMTvcFEXancw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wtp9zvk8g9Z9Tur9ZFmSwlikci7vEy4Bf4Z5CBPiN374rzu6zzCq4iO1M4r_oWPPJynQK_aBW61kxqD9iNZ4SkP7QRjQfih-A3LX7cGzkfEiqYQSs82fdcLRO5XoLy_s3MMNngG8jT0fzDpLS8ROceTkiJXSNzIr5DUKNH4cOP9di1xeIuJgM_p8FcFMN7zEi46oK9rwjcElqSNLFwYXvYWdJsGG2BxYtHCI-n_beOKoPSp6Yrx0NYg1jWpEOr_KjW1XuFrbetEGWYmx9HFbGwThTKyDX_T1W4FTw9uNjB060jap32loLfznlKou3KdgULo7G6M1_3tu9_js02SlGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mgI1y-sHk_IoeKQnvPa7TnAtIRanHS2aDtxIMlyJCiejGMED66iYUEyhC519K6obW7FM3Xw5bsIU1pI1vjCssOpCK7OMcG8nRxeLN5KSLr-w4Tj7kN-G43PUFYL6kKJ_1VyQoQQ2izjgrQTg3Ms9RQPRA4XT3fpnkT4wjE6Fri_oaOfI6mje3Ecyw_Bus3ac-8jJ6IkEIbNQSZYazEufS8HAXsKX7Rq69th-U9xCmDbHtVSNSw9eG2n71gb38ecLq3ameDUGCg3k6C53OxlQu0r3RsbVL2DwZ2Ygr7xGcltCApvON_4UOGJfoslbCT5uTcKokYIpUS6p8d2m_yQ8hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VE768oeU4Iz_kGyuHQdIfYfInHKNV5w90Wa5c1S31RcWWZ-sWqTHENUZsEVt-YlqkkU1V7Rfc85H2rdYkXl8cFg10i0JF4N_eWGLrmtxcw3gs9Y5eTQfCH5B7s_ifloLcurb7RqZqydXHwbccpnwTdVYRZ8oPyMk1bl8Fu8-SwKy5tPumid2Fc7zWGe5liFXi5X7A4SGLAQhY1-chMyghYeyrN2GzkqFaRk7UmrybPuYCZOyKPdgFzEIIW_m1om3iSYD7mBAOrsoYmJu-Q7ph0NqVp4ARm-rKiugujRlKsV9fTZL9SJNxpDZ-f291-hTMdkPVZEt1W5lV6LJRnLJaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c8tWLL1UjVvEp2vzooDGlW5mSDrupCl4r0PNS260KdxD0F60z6WmvU3dCOztowJMYDeJDGAI50-i0WcBifKtiPZgYuRXHjDfQqha04T93Zi91MEAV0Mg16nZ33uJ743zRWbJ7VARbycMWnLUD572N1TTps76ZHYcgkoLSuPX12fO7uKh0QZzUCMjOvGzNA2XfMhXOg2bWdSVT47mNOv36kAw2jB_6t35FPtmO-23cm9RvGTQ5GBlijgqduGOBQrykuTIF3Sj54s2xpXSty8Pg-xQmZbbbUb0KGlZijEnQd1-rjmlDd0pFoXy3HCr7u7dgcr0PxFzPLgBLWNNRcJIEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قاب هایی از مهمونی کیلومتری غدیر تهران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/akhbarefori/656162" target="_blank">📅 20:42 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656161">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c195313f80.mp4?token=EbaGn49JxJfBtIbTbxfq1Ksz7dVJIugoIIawSpdXDHDzM_XrnbYKG5YGOBqEXc8uN_WwcaT6RPXwu3OscuByx--6ijHzotFwlvwnCTHlwcP1qe7JfBWt7AHAM_AAlUqQrfoMJ_9leHuGBAyZfVDt_pL9cHuE2mywVIQi0njYySBbSIWQRt9uu7pudU_YfvCEUYWOUzjbnbcEAw4KTiHj5-UX2FeZ4tzxdfpXjr1gwf1qKH_iv6c6lIGQzlszJgk2IS7N9DBB2Ci9ANXE0jCa-5TThGu-O4zfTyg4riOGDxCaNJiGFUd_D4ROV8S6ELd8wxm6PPCGmhBr9r4_yYLH7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c195313f80.mp4?token=EbaGn49JxJfBtIbTbxfq1Ksz7dVJIugoIIawSpdXDHDzM_XrnbYKG5YGOBqEXc8uN_WwcaT6RPXwu3OscuByx--6ijHzotFwlvwnCTHlwcP1qe7JfBWt7AHAM_AAlUqQrfoMJ_9leHuGBAyZfVDt_pL9cHuE2mywVIQi0njYySBbSIWQRt9uu7pudU_YfvCEUYWOUzjbnbcEAw4KTiHj5-UX2FeZ4tzxdfpXjr1gwf1qKH_iv6c6lIGQzlszJgk2IS7N9DBB2Ci9ANXE0jCa-5TThGu-O4zfTyg4riOGDxCaNJiGFUd_D4ROV8S6ELd8wxm6PPCGmhBr9r4_yYLH7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حضور قیصر خواننده لس آنجلسی در مهمونی کیلومتری غدیر تهران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/656161" target="_blank">📅 20:42 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656160">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">«چالش بیعت» در‌ مهمونی کیلومتری غدیر  تهران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/656160" target="_blank">📅 20:42 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656159">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">کودکان تهرانی جیپ سپاه رو صورتی کردن!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/656159" target="_blank">📅 20:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656158">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0aa5cab1da.mp4?token=G9ZQxOpv0t_ezErY5tkDkaMvLudiAprIhuuFXFH8ov7ZD_PJLqgCoqa8ridyKwHqMWRYz7GJ3tuT0UUmK8rRRqTskAerCxmgKgepdLq56B7nI7V39LzTA1QSsRKjEop3zd19L-BbjXoFWG7NzHdLrfO_m3tmHvG0nniUth3QuihbkdcnRrqhRA83hozugP1HRl6nVi4Y6S8tmj_pgeEld4mSBN_3-nede4Ebd_FZv81Ik2umuLI9u_2CdQJW2l1N9eaYxON48Thd29rGP_0ve9CRqAna4cVZMgyC1t3kgr_RjUy99K1_jNCbZ03hllSmcr4GPRSkyDaiVAeT3ttDxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0aa5cab1da.mp4?token=G9ZQxOpv0t_ezErY5tkDkaMvLudiAprIhuuFXFH8ov7ZD_PJLqgCoqa8ridyKwHqMWRYz7GJ3tuT0UUmK8rRRqTskAerCxmgKgepdLq56B7nI7V39LzTA1QSsRKjEop3zd19L-BbjXoFWG7NzHdLrfO_m3tmHvG0nniUth3QuihbkdcnRrqhRA83hozugP1HRl6nVi4Y6S8tmj_pgeEld4mSBN_3-nede4Ebd_FZv81Ik2umuLI9u_2CdQJW2l1N9eaYxON48Thd29rGP_0ve9CRqAna4cVZMgyC1t3kgr_RjUy99K1_jNCbZ03hllSmcr4GPRSkyDaiVAeT3ttDxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حضور باشکوه تهرانی ها در جشن عید سعید غدیر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/656158" target="_blank">📅 20:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656157">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b718e8b54.mp4?token=sz0oeO4DrR1mwsk1jejRkju-KGdwAqiui0C3SatEN4i8e0vZeRllBuufeI5UG2Rp4cA3DfYbsYeG7mmgLj5bRFRYFBBrJTiA2cWmDWEDSq4zwN0BgJ8GeTz2ZuHzL1zXdLZf5dL-vupGfs4aLuTTBoHVeVZlBopmmMRcjdgvAJERnr11y9KFvZKFn8LoaH4hdKYP7uYF2dqTBOiXmGXXKH4E5TIhs1IYv-6Fi9z9LhIpytyj_D9KOQGPQh4iypwTluKQFivBnv1tPbp35M1_12h1RULmde8mtovU8jLo-lx0sdquWmLipVbYkH6IJ09TAMq3sOlQzvEmbKcW0oy46KHX9yBSbEI6Yh1at_4KgTdPanhEdV4xgE1CZISOgB8fTXnl2j49Rekrpk0lEzUTpWE7eSm_YonqIIOoNaajNUybPozqRonL-pZVt7IWZyh-Hv2HeuwOam5JwrlcqqoClY4_6_vXYbU6uA9Ht42p_b5-ahqrC_tBtcy7SnvVa9cZeuoXuehkdXgM95H3kvq3v1D6mQgiP1OFGL_glZtT29P6PWEgHVoUgJhDB_DQNo8Kmcfxj2pvm3U2-xXY67dcNgFvLgOnPZ7UoviwN1SUNTPSqP6rUbE9IM7JDhk3KHIMxWyPF1snmI6fRy6kRPRlzVdNDh62Ijee1qmbGZNATUU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b718e8b54.mp4?token=sz0oeO4DrR1mwsk1jejRkju-KGdwAqiui0C3SatEN4i8e0vZeRllBuufeI5UG2Rp4cA3DfYbsYeG7mmgLj5bRFRYFBBrJTiA2cWmDWEDSq4zwN0BgJ8GeTz2ZuHzL1zXdLZf5dL-vupGfs4aLuTTBoHVeVZlBopmmMRcjdgvAJERnr11y9KFvZKFn8LoaH4hdKYP7uYF2dqTBOiXmGXXKH4E5TIhs1IYv-6Fi9z9LhIpytyj_D9KOQGPQh4iypwTluKQFivBnv1tPbp35M1_12h1RULmde8mtovU8jLo-lx0sdquWmLipVbYkH6IJ09TAMq3sOlQzvEmbKcW0oy46KHX9yBSbEI6Yh1at_4KgTdPanhEdV4xgE1CZISOgB8fTXnl2j49Rekrpk0lEzUTpWE7eSm_YonqIIOoNaajNUybPozqRonL-pZVt7IWZyh-Hv2HeuwOam5JwrlcqqoClY4_6_vXYbU6uA9Ht42p_b5-ahqrC_tBtcy7SnvVa9cZeuoXuehkdXgM95H3kvq3v1D6mQgiP1OFGL_glZtT29P6PWEgHVoUgJhDB_DQNo8Kmcfxj2pvm3U2-xXY67dcNgFvLgOnPZ7UoviwN1SUNTPSqP6rUbE9IM7JDhk3KHIMxWyPF1snmI6fRy6kRPRlzVdNDh62Ijee1qmbGZNATUU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیعت با حضرت آیت الله سید مجتبی خامنه ای در مهمونی کیلومتری غدیر تهران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/656157" target="_blank">📅 20:39 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656156">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6be575cff4.mp4?token=iO3ElxfSyJZluIDgiaM7pcSoPE90IOxst8Z2jBu_E2eYTpxABFF_T6Ea3tYNJe0Fg6IqVjyHgcqda5WQEnnIGpqNgrLrsiT5AFv9DghScisEScZltXnwIds8gAC_qgysbhPaiyoXhCNpdaSV_ZWD6aQYxjFumbSWzm3BKOzPFbS3TFaktNCvcIj3bg_qRerVOjS1MJ6D0fTCet4fR6EXR6UiZC_Z2LPk1A2nVZlK9DApTLjeCDSChOyUlCcKOUVgx4eHR0MM0QneGNEZIzVDG04yVfwz6StDxD6KflJQr0QoUjvq_ej0hDz2Sg3RqzShmtZuJNLOixlP9-YDTRFTgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6be575cff4.mp4?token=iO3ElxfSyJZluIDgiaM7pcSoPE90IOxst8Z2jBu_E2eYTpxABFF_T6Ea3tYNJe0Fg6IqVjyHgcqda5WQEnnIGpqNgrLrsiT5AFv9DghScisEScZltXnwIds8gAC_qgysbhPaiyoXhCNpdaSV_ZWD6aQYxjFumbSWzm3BKOzPFbS3TFaktNCvcIj3bg_qRerVOjS1MJ6D0fTCet4fR6EXR6UiZC_Z2LPk1A2nVZlK9DApTLjeCDSChOyUlCcKOUVgx4eHR0MM0QneGNEZIzVDG04yVfwz6StDxD6KflJQr0QoUjvq_ej0hDz2Sg3RqzShmtZuJNLOixlP9-YDTRFTgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش
‌
زدن پرچم ایران در تلویزیون آمریکا در دوران پهلوی
🔹
درحالی‌که برخی مدام از «اعتبار پاسپورت»، «ژاندارم منطقه بودن» و «جایگاه جهانی» ایران در دوران پهلوی سخن می‌گویند، تصاویر تاریخی سال ۱۳۵۷ روایت دیگری را نشان می‌دهد؛ جایی که پرچم ایران در یک برنامه تلویزیونی آمریکا به آتش کشیده می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/akhbarefori/656156" target="_blank">📅 20:38 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656150">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NCg52yzFM3rFTdH-qTOxP8d-YaPBKftE4LqeaMy64ruOKvjmdTG8XRa4daFStyUtvBbuXkZXupFmeKfc-hr6cY3nKWygmik3hQIcctH248ZMLb37Sxx8MGjYICWG6OOs0km-3er1ZOirOH_jaJFcXVqddyyk37YuM-wEyk9IpZ-iRCWqTGkCbiZsFrn-1405pL5i1iqTIU-n5EsV4TihHdiA98TYNvOYSPAfruSVw8lb2FVh_xkgP8z4qTwGIuL6lzygKXw3YVj73xROwuhA6EdQx_tnJCmrkmvsuskg__bC89rqZebLCN2CotU0ii2TfXssXDffG1kJqaEG1vvxlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SW1HOGkn9hAiOHzy6fxuuNqOB9xK9fmqetbZnAZo3IWeqc0xdYm-wGnJrl18MSn_l83dweshvnDIx0nv8vnVCbGyXXMJFLRqo6pTLizyMImtm6MHwsxndb5MVBK8pL4CSUWrY0xpqJhGf8WX08FE_-xo37X2uxWUnxM8J3itsthaL3P2lKE4NMtsrKeKigzUYiWk7xOxZqsaeHn7MCa4eBg5Exg42C71qE48Czb--CJu9LVTaMJL29mHvOJHgVZwFEEtviEG__4OPrn3B93gN8juz6EBlCeBy3J_9NmWvT2dq_FexuquI6__LxgtOuy5MQMWyASwsPCXjzdQThivtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GywOEcBONRTMxByy4YLnyq9yBj1-vZHI2wtdLcJvZj0ZCIs9nn473loo3yWFIumsgQPgT_MCvrTN2t-EAT9gimdrsOiqGxfzaP_WQblVnv2L3AiDVB0NWKWGHKUS_6DxN725FCEzp-Fwr6fI1SgoA80Ay67zczief4f6k8Qq7eJxM0fMd4tVAD5eTbcHLOLyq29CgwC3A5ZEikeX1yVs5KpZ782VZCrgqroEn0oYAsjQ-0rEIOaTd5cz6WyaGse_uhYVOdee7Qgn3imJ0r5_4qvsoFseiUy5j6rRbd3Xmtu9-7RYmU_AHdsrwe8GtyXyeRwMg5YKH8tE5GoKWvp6KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ukq5ArIQEYXe-kdM1iL28ogazJ4FYK7lzjXhnWrc7GCm9OxT4scLPZYq0jQfDh2aVMy5E5cqWpEhqR78LQV8Yi-MjH1RcecxCwtbRbxWBDMIU3IWdmALSoBuOkMHTIuLv3j13ZbfRZZeiaAAtAkWgei5zwdIMcapdaLERqPBhUEOFA3eDsjnLn95DgwogmhBH4aF-bl6qPJenT5aAh7MfVrls0BjZUJFhRpQdu3kq_8cpBZrgpv4Id_MggCnIUJKP8yKWaruTw6H2i7JpgYYB6S60CyHb2mu1tUApK5-udtUxRfg5JezIqboycg7JCmmejkDXYSpFC2Er0ng2yrm1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CsFfE-6WfUJAM5W8tnaUbsImYGqmRH7pjr5pOg44lR9e1kxnTH8KfY2HSy5JbwylwLnkF1xXQvFRwfLWG4g2s5swmjmwZXdTMPOEE99h1G1DAHwYrBXboLOBApwbahCQZvag0i0nf4Cw6eASMQaVFMVP5n4LOTxWRtZYwR5jRliYtTD62AO_3PY00R-uT4TbW7KiiAaefNnAplZh0hPurQZiqzBpdZRWmdE__zVm9xrrzT_8KKfQ9eMSk5dEdQnE9XYck7dQHqj7ruHtQyQ3tVjjrEeqCKHuGYCbdCFiZTJd5jq-VZpYmJDmzfT3aVtlPOiM0pBo14rBXE1-iDkAYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EaoX6D0J_yXlyML9eyFDPxuZ5nFD3Crk1t7pBn3mcgyulqYygyZHFTYc2g2vQroZsjvr5kpvDLSaw_3Nmyww-9HEmCvmIGaSUhlg27NAEg2p4TRNwdtxBDZlmg-OJ8nZsuJGQsPab0gxlW62KouRoWOmVCCrJhoZc-AyIN9LtbaZEudthUvHjGEZJ7PTjG5JZsekPwpYHGlAfb2Ctc_B0naIYUFEkuKHOprPZG4tUaZPKpSKkA7tElRVbxts3EVu9ICvzpH92xYZj5z848du6BvArNPuWfx85Q3CrXI0Z8caJHq-ySE9pkwPanJ5crEmZcZC1w1I91VTj8dDBP8MSA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری عجیب از ابرهای آسمان بلغارستان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/656150" target="_blank">📅 20:36 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656149">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e86e44310d.mp4?token=iXb6wUHXxpG6W3MHjVcFm8B0oTW_BJj-4yoMhzSzf0dd1ttzsqiWswn77YVsY98J_3dyrAJl_BrFxNeqXIV04ULj0tozUvL2uSY2ug03LUW43KSiz7g9wFyE1iaaZcSLW9viFsLO_yl3bUI3H6XZVZQ5u1Raqwa9u9ou54V5TnQkEuSBLJtq7kao9rrBGupYrO7EXKUoggOfMOZzNtJG6kXTThyXFcGtuj-7kB5G6xDDIdgZc2PKkcYmKPhoocQdhd9yWOoH89o1YTcVQePN8N2Iv00eSRAAkrAlMArH5X5CMtTcNDYcr7kzx5pdBaGDbSJuYykO96RouFX4ENhMzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e86e44310d.mp4?token=iXb6wUHXxpG6W3MHjVcFm8B0oTW_BJj-4yoMhzSzf0dd1ttzsqiWswn77YVsY98J_3dyrAJl_BrFxNeqXIV04ULj0tozUvL2uSY2ug03LUW43KSiz7g9wFyE1iaaZcSLW9viFsLO_yl3bUI3H6XZVZQ5u1Raqwa9u9ou54V5TnQkEuSBLJtq7kao9rrBGupYrO7EXKUoggOfMOZzNtJG6kXTThyXFcGtuj-7kB5G6xDDIdgZc2PKkcYmKPhoocQdhd9yWOoH89o1YTcVQePN8N2Iv00eSRAAkrAlMArH5X5CMtTcNDYcr7kzx5pdBaGDbSJuYykO96RouFX4ENhMzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جمعیت عظیم مشهدی‌ها در مهمونی غدیر/هم‌اکنون در حد فاصل چهارراه نخریسی _ چهارراه چمن
این برنامه به همت هیئت قرار و مجتمع امیرالمومنین (ع)برگزار شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/akhbarefori/656149" target="_blank">📅 20:34 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656148">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81d6e65b18.mp4?token=l3sM7IUKuOnjtJ58ABkHILPnk06_uIcPNi7y6lO2YEGOwl27HnDr2NEBGU6GLD52M2LqLeUFLAxYr_87HqjMxxnKqDe--o-aPU5CTjESaris5MYcREFSw8OM9-YfJK8kCTEO-0dvB0TaSAgWOcci8MI-LQtGUqtJK0Mkn8tJQ9V5INLnX0D7Oes_hv5iaD7KIJOdn1BFtKLgceYiJimE8BpMIZgdH43IvGIC9lbj1vJ10Pt2czA6tlhpomOYVtxRfzSK39ktsqr9VFaSq08ju64RfeWR5VNCAT4SBrcUOjikfhm5hF3nNmRGYRiVNAfu1mNFkJvhIECZACvYPgtkpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81d6e65b18.mp4?token=l3sM7IUKuOnjtJ58ABkHILPnk06_uIcPNi7y6lO2YEGOwl27HnDr2NEBGU6GLD52M2LqLeUFLAxYr_87HqjMxxnKqDe--o-aPU5CTjESaris5MYcREFSw8OM9-YfJK8kCTEO-0dvB0TaSAgWOcci8MI-LQtGUqtJK0Mkn8tJQ9V5INLnX0D7Oes_hv5iaD7KIJOdn1BFtKLgceYiJimE8BpMIZgdH43IvGIC9lbj1vJ10Pt2czA6tlhpomOYVtxRfzSK39ktsqr9VFaSq08ju64RfeWR5VNCAT4SBrcUOjikfhm5hF3nNmRGYRiVNAfu1mNFkJvhIECZACvYPgtkpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بدشانسی عروس و داماد سنندجی و تصادف شدید با یک پراید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/akhbarefori/656148" target="_blank">📅 20:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656147">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8f9f8cdee.mp4?token=XWjsXNBbOInacHhWJ5sMz6nkfs61oxtXnDpIMXMhHu7eI9yfhn8tGr3ZwO3acdz-KFpa31XMJUq6yJZVrpS8SpJ_VPFheDq3GOYG-I5xOeGSlPPteK-wHvOKsBjt6DiXi7jqSwnPtFlZJu8WH4pIorUGSytxf-ADGGCj1kM-k5UYiij5xughWMfs0qV4HZx1VfhOhfhiIWGNTRX4zc_NTfXCZvbNAXdar2fE6zQwLPPMzzjtY0drNDAMHEXcLDO8Lqjj_HS7R2c2ow993n7EZi78cNF8buBoiasvULFNG40Swb6gVALzrI_LCmowF1cnPDrNaFOKqlXrGiOtNbR_qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8f9f8cdee.mp4?token=XWjsXNBbOInacHhWJ5sMz6nkfs61oxtXnDpIMXMhHu7eI9yfhn8tGr3ZwO3acdz-KFpa31XMJUq6yJZVrpS8SpJ_VPFheDq3GOYG-I5xOeGSlPPteK-wHvOKsBjt6DiXi7jqSwnPtFlZJu8WH4pIorUGSytxf-ADGGCj1kM-k5UYiij5xughWMfs0qV4HZx1VfhOhfhiIWGNTRX4zc_NTfXCZvbNAXdar2fE6zQwLPPMzzjtY0drNDAMHEXcLDO8Lqjj_HS7R2c2ow993n7EZi78cNF8buBoiasvULFNG40Swb6gVALzrI_LCmowF1cnPDrNaFOKqlXrGiOtNbR_qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کلیپ جالب از دلتنگی و علاقه شهید آیت‌الله خامنه‌ای به امام خمینی و ماجرای عکس امام در بیمارستان
🔹
در دوران بستری شدن حضرت آیت‌الله خامنه‌ای، رهبر معظم انقلاب اسلامی، پس از حادثه ترور ناموفق سال ۱۳۶۰، تصویری از امام خمینی(ره) در اتاق بیمارستان توجه ایشان را جلب کرد.
🔹
شهید آیت‌الله خامنه‌ای در نقل این خاطره فرمودند: «در بیمارستان دیدم عکس امام زده شده بود و خیلی خوشحال شدم. به دوستان گفتم تخت را جایی قرار بدهید که رو به عکس امام باشد.»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/akhbarefori/656147" target="_blank">📅 20:29 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656146">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tMi6HkHbg0HA1AObQ1WqCHw_Ed9aLF9sMOV-U3NJI9sezsPBIhnTMbJIEU7oxH9moquw6KOZyK7Rmo3qMEWZMhH1O8FbbXTKzNW0Izc-1p2JZnmlQZh3FlW9n7eGnQ8jHfac6C0lvlBOzGwHG4zbwtiRKtTB1PH6aRN_wlu0HqiXeH7ABgpqtNitb-9tp3ZGsEdNLuTMNsn82DcvpeVzq4Z0vnKAPys5QMhjxLbg9AN85XnCY3erfnmUI9gZPEVVSg_V6w4HSFKP4M2-2i6mYMUJ4raLSNkizKk3Xpu3S0sr9O-tCnt4jBemH3pqD6k_2n1Y0309C6bK8P2aKdKKLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا خود را برای جنگ هسته‌ای آماده می‌کند؟ | هواپیماهای تهاجمی در کشورهای بالتیک مستقر می‌شوند
🔹
روزنامه فایننشال تایمز به نقل از سه منبع آگاه گزارش داده که دولت واشنگتن گزینه توسعه برنامه «اشتراک هسته‌ای ناتو» را به کشورهای بیشتری در اروپا مورد بررسی قرار داده است.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3220311</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/akhbarefori/656146" target="_blank">📅 20:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656145">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f8643a124.mp4?token=F6THzI7sBMRyvvlZmQnhWAvjs3tf9Oz7k_ZScVwzPSU7gwWaFkIvGZ4aJpqyJJ1j4pxusWNDXuXwIwcvoAlOeKSGPTPyQMfNa8Od4NVBT3560WhW3H0CHgKXdtLkE-rT6j-R3HAj_Ve2LSqVuGeOAl33sjjGu3f_afmS8CTGhqn-CqYtaPR5uaJVkoJoFEFcnOWKCVwAjRSf_xVE4J9zheMChfyVJgEJfrRp_q2X8tgaHXhpOCGPmd3EDZXYxgS5qfJ_bsD3C2ZlWNSjEKOhsvV5kzFBXJKJyhFunqrCVsImgFa5xhFNQIxNjaUDLt9JICI_vDL4yUBPo5R4Z3xk4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f8643a124.mp4?token=F6THzI7sBMRyvvlZmQnhWAvjs3tf9Oz7k_ZScVwzPSU7gwWaFkIvGZ4aJpqyJJ1j4pxusWNDXuXwIwcvoAlOeKSGPTPyQMfNa8Od4NVBT3560WhW3H0CHgKXdtLkE-rT6j-R3HAj_Ve2LSqVuGeOAl33sjjGu3f_afmS8CTGhqn-CqYtaPR5uaJVkoJoFEFcnOWKCVwAjRSf_xVE4J9zheMChfyVJgEJfrRp_q2X8tgaHXhpOCGPmd3EDZXYxgS5qfJ_bsD3C2ZlWNSjEKOhsvV5kzFBXJKJyhFunqrCVsImgFa5xhFNQIxNjaUDLt9JICI_vDL4yUBPo5R4Z3xk4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بمباران شهر بزرگ صور در جنوب لبنان ادامه دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/akhbarefori/656145" target="_blank">📅 20:21 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656144">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
گل در دقیقه ١٢ برای ایران توسط سعید عزت‌اللهی
🔹
ایران یک - مالی صفر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/656144" target="_blank">📅 20:16 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656141">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c441d35b4.mp4?token=jdFIRbKwWlIgKSmVXocTdjD7UnueKSvYtpU-HnHGIJtVVFNJ9pash5dvHzG7F990Ovjetj6SoRMKfCIE0Ciy4lt5FcNNRuDS1B7wBoqZpZfHRcO7JEXyrsq7XE-wwYOSET6kwu23hHenvRRBvRLGdwYsUx-GVQV-2ybMWwAsQZT6A_K1zRcq5JlMTANgmWBlKsBD1lZVBwoADvVJlyXhgtA1ZoYRMII1Me8nCfW-Kz5aI8qD2BBxg7vdFcMFrj9sgdSnypMV5qEw9D0L6UteQKPkWIARHu0eLOVyR_hHCQPuHmLzr5bisKDJwav62WUkTfRcD967-O-goZcsG1lunA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c441d35b4.mp4?token=jdFIRbKwWlIgKSmVXocTdjD7UnueKSvYtpU-HnHGIJtVVFNJ9pash5dvHzG7F990Ovjetj6SoRMKfCIE0Ciy4lt5FcNNRuDS1B7wBoqZpZfHRcO7JEXyrsq7XE-wwYOSET6kwu23hHenvRRBvRLGdwYsUx-GVQV-2ybMWwAsQZT6A_K1zRcq5JlMTANgmWBlKsBD1lZVBwoADvVJlyXhgtA1ZoYRMII1Me8nCfW-Kz5aI8qD2BBxg7vdFcMFrj9sgdSnypMV5qEw9D0L6UteQKPkWIARHu0eLOVyR_hHCQPuHmLzr5bisKDJwav62WUkTfRcD967-O-goZcsG1lunA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جمعیت عظیم مشهدی‌ها در مهمونی غدیر/هم‌اکنون در حد فاصل چهارراه نخریسی _ چهارراه چمن
این برنامه به همت هیئت قرار و مجتمع امیرالمومنین (ع)برگزار شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/656141" target="_blank">📅 20:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656140">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b62330897.mp4?token=j7IYKMwbKQHbWxGbfes3VLO-iHZX1KOkLU9XHo0jZTh4dtD-pf5b84z04Ohq7YYWSE550FbDxPRP1m0tDPJk4QqNQSjxulKYPKNjqFyOko61HQHHUVO1_kxmlV4a56HdAcMHQ8VMote7VVoDUEaEqgWFxF7EBrF3aJNZuoCXNjSjdNCwOI2b40BHzz0-Bg6tA-iVFx7mFdBHI_Qziy_g2yTF4xc0thR16hsXHO2j9DoYEXTHFwAyz9FPyujqBljtM7de7gHS4T7PHM9qcQAqOxjdQUBKABcTTy2XfG_jLDhe8wfgmRkdj4r1NvMCQx1XnidHi758JWUSXb3sKOAScg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b62330897.mp4?token=j7IYKMwbKQHbWxGbfes3VLO-iHZX1KOkLU9XHo0jZTh4dtD-pf5b84z04Ohq7YYWSE550FbDxPRP1m0tDPJk4QqNQSjxulKYPKNjqFyOko61HQHHUVO1_kxmlV4a56HdAcMHQ8VMote7VVoDUEaEqgWFxF7EBrF3aJNZuoCXNjSjdNCwOI2b40BHzz0-Bg6tA-iVFx7mFdBHI_Qziy_g2yTF4xc0thR16hsXHO2j9DoYEXTHFwAyz9FPyujqBljtM7de7gHS4T7PHM9qcQAqOxjdQUBKABcTTy2XfG_jLDhe8wfgmRkdj4r1NvMCQx1XnidHi758JWUSXb3sKOAScg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طعنه خبرنگار اسرائیلی به وضعیت آتش‌بس در شمال فلسطین اشغالی
🔹
پس از حملات موشکی حزب‌الله به شمال فلسطین اشغالی و فعال شدن سامانه‌های پدافندی در کریات‌شمونه، عمیت سیگال روزنامه‌نگار مشهور صهیونیستی با انتشار پستی کنایه‌آمیز، وضعیت آتش‌بس را به سخره گرفت.
🔹
سیگال در واکنش به رهگیری موشک‌ها در آسمان کریات‌شمونه نوشت زیباترین آتش‌بس جهان همین است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/656140" target="_blank">📅 20:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656139">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9ea5df58.mp4?token=A3rqqei-2OgiXjmWRu9XVIyZFkedVKOYbIcb93ndumdq-M0F4nb8HJFqGRjUbCbfvMge2UTXZ5KJFDh2XyID2Xq8vG6HmAtXJs74SksYHJd9edomGxPyG89VRsXt7f2wmdix1XaLHcnPlyLCxH5jtrETAZm9ueZUCy8reHHMv-HHuaPy6aIgF8n2qATem8SQ57Zxqi75W-63EpwMASxEdM_e6qCxVq3712l-rPfujRC5l8j181BVBMET9itBrah2cmjyecgEiM5wxcWwVvdRVO_wEnJan5dbQ3jY18bdMAOBoBuswjuoBJLxZWtfBOkRbxERLkRACNZraPGij7qgGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9ea5df58.mp4?token=A3rqqei-2OgiXjmWRu9XVIyZFkedVKOYbIcb93ndumdq-M0F4nb8HJFqGRjUbCbfvMge2UTXZ5KJFDh2XyID2Xq8vG6HmAtXJs74SksYHJd9edomGxPyG89VRsXt7f2wmdix1XaLHcnPlyLCxH5jtrETAZm9ueZUCy8reHHMv-HHuaPy6aIgF8n2qATem8SQ57Zxqi75W-63EpwMASxEdM_e6qCxVq3712l-rPfujRC5l8j181BVBMET9itBrah2cmjyecgEiM5wxcWwVvdRVO_wEnJan5dbQ3jY18bdMAOBoBuswjuoBJLxZWtfBOkRbxERLkRACNZraPGij7qgGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری تماشایی از رعد و برق در آسمان چین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/656139" target="_blank">📅 20:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656138">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/793266281b.mp4?token=vsIhPRF9FNqiMIfGK_-vN19RWS6-LxaGHrGowRcJEpf9LvoIZkQrQXuKBL0UMsbLRI1NRfNMOh9sraUTft6YGCYGnzH8uAQZtubdhcdTFlKJUqlxKvJ4oA7AE3iWDssfQCT27PlUtbbHNzAYb2W5jDpLScxbGCEHMeR_8uOpvCBYwlxN4yKFRKibe0w2P1CL70sMR9RlBJSdGpgd0NixEgvHFvjJY5o3jnkcnLdAhKVYWObv9r7bXmfjdXZYagHQZs-jJ077jUubias75PUUIfuVrFg3Y4pyxVu18QMAsH90T1DmSMdp9Srx3MNeJAHKMMpHJuAR7jkRJdRNEe7e_4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/793266281b.mp4?token=vsIhPRF9FNqiMIfGK_-vN19RWS6-LxaGHrGowRcJEpf9LvoIZkQrQXuKBL0UMsbLRI1NRfNMOh9sraUTft6YGCYGnzH8uAQZtubdhcdTFlKJUqlxKvJ4oA7AE3iWDssfQCT27PlUtbbHNzAYb2W5jDpLScxbGCEHMeR_8uOpvCBYwlxN4yKFRKibe0w2P1CL70sMR9RlBJSdGpgd0NixEgvHFvjJY5o3jnkcnLdAhKVYWObv9r7bXmfjdXZYagHQZs-jJ077jUubias75PUUIfuVrFg3Y4pyxVu18QMAsH90T1DmSMdp9Srx3MNeJAHKMMpHJuAR7jkRJdRNEe7e_4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم‌اکنون مهمانی بزرگ غدیر در مشهد حد فاصل چهارراه نخریسی _ چهارراه چمن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/656138" target="_blank">📅 20:01 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656137">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KE6s0nm-9mkcmUouLmJNUNCa84vx-l6U5g7c0W4PN1eCIG0H9yhAuYvkNKS_hIBvl79T3xqY9_q1ipRBcBKaPJodHPHFQ0LLN2e9_--pSblK-3VHzsBWn1apaeUT90TLlXgBKTobTXaFzkEIWqQmW4Nj0b2x4AZR4B7rY_Hhz12G5aybweMzWIU6txzHcdZVi3R2RoaTCf-PZetd9-S5ryR-TOYn3h01E8uIgvfdTgPc8AubLW7OWeoFMVSIaci2hGSBuzSBv1cveEoRUHooz-Oui2850x3qElWeZfuZbLu2hlaUX0eWItfPHd_ICF9DUo_U29Xs20lQDO-6oxzEuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
داستانی از عدالت، تواضع و نور ایمان…
🔹
در روزگاری که عدالت، جلوه‌ای از ایمان بود، امام علی(ع) زره گمشده‌ی خود را در دست مردی مسیحی دید.
🔹
ایشان برای اثبات حق خود، نزد قاضی رفتند و چون شاهدی نداشتند، حکم به نفع مرد صادر شد.
🔹
اما همین عدالت و انصاف، دلِ مرد…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/656137" target="_blank">📅 19:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656136">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
کشف جدید در پرونده سلاح‌های شیمیایی سوریه و واکنش روسیه و آمریکا
🔹
معاون دبیرکل سازمان ملل متحد در نشست شورای امنیت درباره اجرای قطعنامه ۲۱۱۸ (مصوب ۲۰۱۳) پیرامون نابودی برنامه تسلیحات شیمیایی سوریه گزارش داد و اعلام کرد: حجم قابل توجهی از تسلیحات شیمیایی اعلام نشده کشف شده است. در اوایل ماه مه، تیمی از سازمان منع سلاح‌های شیمیایی (OPCW) به سوریه سفر کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/656136" target="_blank">📅 19:56 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656135">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/727aca4cc1.mp4?token=q4f_g4u163LOr8rmh8M450ZG-A2CzuDvKkdIyRvegQd4lrqckr0SDb2cQAxAmrSNht7GqLD2sC5BJOD6oRgy4N0xh6A_T1aFhyQxCwB6zjvyfIxNBKSrCpUrrOhZQDW4TXA0zLi9R-lQSisuYOgCaZELD7C27wHslAtgzqle8GXo-Tw5tmrHbwzNR0qKSkivWmQBtAiojPYVqugaqy4KnErYNDcb7cw2GrktsmADAgGLwLdXV8wf6owjfGlSotrZh-M5ZwgBKmyxXu3OtbfH2cwCWUVBEoJqXxg2ELw-MpvbT3lIXsTSrm1rzAiPheddyMElQlaiPdeqrOTkrGCafA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/727aca4cc1.mp4?token=q4f_g4u163LOr8rmh8M450ZG-A2CzuDvKkdIyRvegQd4lrqckr0SDb2cQAxAmrSNht7GqLD2sC5BJOD6oRgy4N0xh6A_T1aFhyQxCwB6zjvyfIxNBKSrCpUrrOhZQDW4TXA0zLi9R-lQSisuYOgCaZELD7C27wHslAtgzqle8GXo-Tw5tmrHbwzNR0qKSkivWmQBtAiojPYVqugaqy4KnErYNDcb7cw2GrktsmADAgGLwLdXV8wf6owjfGlSotrZh-M5ZwgBKmyxXu3OtbfH2cwCWUVBEoJqXxg2ELw-MpvbT3lIXsTSrm1rzAiPheddyMElQlaiPdeqrOTkrGCafA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سریع‌ترین راه گرم کردن غذا بدون تغییر طعم و بدون کثیف کردن ظرف
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/656135" target="_blank">📅 19:52 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656133">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SuY91s5p9FYw0vWWRnmeQ9PE_Eo6AAdL1EWnbdiU7tQRd4Cn-z-z0vMQ8bxxALUFHF8C1ISHNJXHJ1OMKhmdH-_ZEbSUe045ufoju-XDtWVLv8vasqfZghPDFNX8S2o6sZgHEwWqGAcqoHp7rB06OA_AiPu7axZImIdg4QelVPSgYmKRQ6qQpyjkBN_r-4l8VUtg1glOk8mWGSUFeOtJJMnVUuVrkRaxAb_vTwvzQD5b1IJQ3YnkIMWNXnsD9v7boIOQZyci1A0NYoa7ykVMUEB5FbexIEolZ6bQA_NxvtxXBT8gcUZVqmsXt0behjD4jSSY5wcr-liTLjlScyPAEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/940b725639.mp4?token=IH1ezDMcNr6BbZ4nmHe-nHu0okWoWf40LxvzrMf5Xa4mPRtNbw1W3G6KlMKhs4_Q9nLwRfDbHCVFHdyml2tew-f9cKcmV7NOHMfmxTDpMLf908AuqFNZ2Ph_IEX0VZjJ6Qr25FhcyFmtmTuBk8Zef_FeoLvOrfS-5Ap3UdxzYU_R4F6MhBJ4agTFKtA-l_nlZjtB49L3g4SZ8Ev_SsCNGnir40qKuYiduNBUs1be60RkuKv3iI1rEpL1OU5qNn1zuoA8aZnHM2iP08k01hACg-IwvDW1zgijW_IXEYDDsuRmT8GDz0e4uVtJLJ5bLS4WK1acBpRF32HEeSeFbOoolA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/940b725639.mp4?token=IH1ezDMcNr6BbZ4nmHe-nHu0okWoWf40LxvzrMf5Xa4mPRtNbw1W3G6KlMKhs4_Q9nLwRfDbHCVFHdyml2tew-f9cKcmV7NOHMfmxTDpMLf908AuqFNZ2Ph_IEX0VZjJ6Qr25FhcyFmtmTuBk8Zef_FeoLvOrfS-5Ap3UdxzYU_R4F6MhBJ4agTFKtA-l_nlZjtB49L3g4SZ8Ev_SsCNGnir40qKuYiduNBUs1be60RkuKv3iI1rEpL1OU5qNn1zuoA8aZnHM2iP08k01hACg-IwvDW1zgijW_IXEYDDsuRmT8GDz0e4uVtJLJ5bLS4WK1acBpRF32HEeSeFbOoolA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نذری عجیب و جالب گلس رایگان در خیابان انقلاب در مهمونی ده کیلومتری غدیر به عشق امیرالمومنین (ع)
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/656133" target="_blank">📅 19:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656132">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/676736e9f8.mp4?token=as_owYtPJLVzWtIrwa_Vys8pSz1ubfmMnmseWOcgSQlhTy9ggKoFCUH7VABAc5ZTIPI5DYInXpQRfHvasxXciyJnw_CfsT0_p1sMwRq5cLYNwgwKIPhkenC1gG7guibkBtaR3Dz5HJJPlt3e0LvyxO88X3RhgCOowthugj_GelH3I59m-mtTAiatUKuZGc5aw15D03_2bdJmBCyKhbwIR7arsCLXdYw4LjDXu_dRUCcsCa1cNCwEaUaIaiHlUQcFq6Bo9vWVDYmUENgs3KoL2IEh6rH79-XfYrgVrixqdd97LEvTLzDfk0huIRBMuln8srC-ytB_8iljUxgd6ycn8Rzll7HhnXOJWzYkZC6hkrTbbVC5KnTrPQepq6M4t01fKTwy7pVNGMygnw7ZeE1CDnY5xKy3GP1ffhsPEmAQ-iKnN9-7leyBVFm59vwhAw-wf64-zfFBJfXDvV4jRG05i3lziQGov3LTpDi7HYIjRwMxxZ7EPpsxYPQba5J1yPc4lZgBDXzFKs2kKEdYPrQnsrM8czyPI5QNROBNL0XRx03D9ZP7KL7RtgmBOGqisNFkoEMudFufQNL1C-DbA_ARGqCitb6ZANFTHQwvdvsNiJt_aKa-iXYe8uTSz5KLq_sL_7e1F0nh28_034eBsvRzWsurx_W_ulHN4gzA08sUiyU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/676736e9f8.mp4?token=as_owYtPJLVzWtIrwa_Vys8pSz1ubfmMnmseWOcgSQlhTy9ggKoFCUH7VABAc5ZTIPI5DYInXpQRfHvasxXciyJnw_CfsT0_p1sMwRq5cLYNwgwKIPhkenC1gG7guibkBtaR3Dz5HJJPlt3e0LvyxO88X3RhgCOowthugj_GelH3I59m-mtTAiatUKuZGc5aw15D03_2bdJmBCyKhbwIR7arsCLXdYw4LjDXu_dRUCcsCa1cNCwEaUaIaiHlUQcFq6Bo9vWVDYmUENgs3KoL2IEh6rH79-XfYrgVrixqdd97LEvTLzDfk0huIRBMuln8srC-ytB_8iljUxgd6ycn8Rzll7HhnXOJWzYkZC6hkrTbbVC5KnTrPQepq6M4t01fKTwy7pVNGMygnw7ZeE1CDnY5xKy3GP1ffhsPEmAQ-iKnN9-7leyBVFm59vwhAw-wf64-zfFBJfXDvV4jRG05i3lziQGov3LTpDi7HYIjRwMxxZ7EPpsxYPQba5J1yPc4lZgBDXzFKs2kKEdYPrQnsrM8czyPI5QNROBNL0XRx03D9ZP7KL7RtgmBOGqisNFkoEMudFufQNL1C-DbA_ARGqCitb6ZANFTHQwvdvsNiJt_aKa-iXYe8uTSz5KLq_sL_7e1F0nh28_034eBsvRzWsurx_W_ulHN4gzA08sUiyU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نذری پیراشکی فروش معروف میدان انقلاب در مهمونی ده کیلومتری عید غدیر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/656132" target="_blank">📅 19:49 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656131">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
آمریکا برای تبعه خود در کویت هشدار امنیتی صادر کرد
🔹
سفارت ایالات متحده در کویت از شهروندان خود خواست که احتیاط کرده و دستورالعمل‌های مقامات محلی را دنبال کنند. علاوه بر این، سفارت ایالات متحده در کویت سیتی تمام خدمات کنسولی را به حالت تعلیق درآورده است. واشنگتن همچنین از تبعه خود خواست که از اعتراضات و تظاهرات در این کشور دوری کنند./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/656131" target="_blank">📅 19:46 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656130">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FU7FeeuwCMZBe6S4Uc-nVkqw9UK1Qagd_Re1zFg9TTcxE-oPlevay4eAlJhLczKje0OggILQeNiyG0jQge2U2LB9ekACSXqRPdwd43o1-zBRGdUhq86dIlEdh03Pe8sPY7QuoO7zjbbRyDvgO7CKH_ROey_pAP99SpKedWUIy315gBGe1Qps9eoSAZWgnqysQ9ig8bNX0mdIbKaN3PsoxnFndNeWZ0nO6jzmkXm1mm7USr0ZZAUvJthP-QScMU-GoT_IYbAN9F_HqSPDBHuhnfojdUfJHR9_b_oeX8goVV3gtQNkzrTaPglrU3nXpNzQKWkCJzBv-wRCe22slXFB0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پدرها بین دخترانشان فرق نمی‌گذارند...
حتی برای به دوش کشیدن پیکر نحیفشان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/656130" target="_blank">📅 19:42 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656129">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
گزارش یکجانبه گروسی به شورای حکام درباره ایران
ادعای مدیرکل آژانس بین‌المللی انرژی اتمی:
🔹
آژانس نه اطلاعاتی از ایران درباره وضعیت مواد هسته‌ای اعلام‌شده، تاسیسات و مکان‌های خارج از تاسیسات برای اهداف پادمانی دریافت کرده و نه به هیچ‌یک از این تاسیسات و مکان‌ها، به‌استثنای نیروگاه بوشهر، برای انجام فعالیت‌های راستی‌آزمایی میدانی دسترسی داشته است.
🔹
آژانس قادر به راستی‌آزمایی وضعیت این تاسیسات و مواد هسته‌ای مرتبط با آن‌ها نیست. این مسائل باید از طریق یک توافق دیپلماتیک پایدار و قابل راستی‌آزمایی حل شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/656129" target="_blank">📅 19:37 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656128">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d35080d7e7.mp4?token=rvwjxe3F1W50NXVac6Xw0ozjPWEu5J5fwTSs8thcK9KQMrjth9wI61ZNiHehady_Krw2lBOQIjbi2NMh8jQ_RJBYncXsVmlf_UHFAXTJU1qNG5vlbvBOuBlOJ5Tvu8tVvO_wiFu7nKoafN95J_1JwBBn89qLXfRvEig1Zwkxz2uWmHeNXXl0elgOBK5xiXoclWF7SUsa2D8hVZfjAAU5VoRJsq4HK4Q7m_o-6kCt8Pm9nWlpA46mgCunI56jsoRXfIWOPJRdNbWIk0sjwHwFIKNxC6OegoWhgXRzB7J39dJX2ZNlz6yarSsK5ojZe6AuQ7mArWoQxr2TcDIkWzxoAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d35080d7e7.mp4?token=rvwjxe3F1W50NXVac6Xw0ozjPWEu5J5fwTSs8thcK9KQMrjth9wI61ZNiHehady_Krw2lBOQIjbi2NMh8jQ_RJBYncXsVmlf_UHFAXTJU1qNG5vlbvBOuBlOJ5Tvu8tVvO_wiFu7nKoafN95J_1JwBBn89qLXfRvEig1Zwkxz2uWmHeNXXl0elgOBK5xiXoclWF7SUsa2D8hVZfjAAU5VoRJsq4HK4Q7m_o-6kCt8Pm9nWlpA46mgCunI56jsoRXfIWOPJRdNbWIk0sjwHwFIKNxC6OegoWhgXRzB7J39dJX2ZNlz6yarSsK5ojZe6AuQ7mArWoQxr2TcDIkWzxoAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آخرین حضور سردار حاج قاسم سلیمانی در مراسم رحلت امام خمینی، خرداد سال ٩٨
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/656128" target="_blank">📅 19:36 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656127">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
ارتش اسرائیل از افزایش تلفات خود در نبرد با حزب‌الله خبر داد
سخنگوی ارتش رژیم صهیونیستی:
🔹
مجموع مجروحان ارتش متجاوز صهیونیستی از آغاز تجاوز به جنوب لبنان به ۱۲۴۳ نفر رسیده است. از این تعداد، ۷۲ نظامی در وضعیت وخیم قرار دارند. همچنین حال ۱۴۰ نفر از مجروحان «متوسط» اعلام شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/656127" target="_blank">📅 19:30 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656126">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50daff1723.mp4?token=Gz4IXRqCpKOaMg3Ovn6FV9N307PjjCrRPn7kVe3bEQ5O5M1nIhXE8AEF5V5EbFlEACUiW7ZvuzQGZvnSL6b6uvyfUc-OSMg9XIzl5IcErqjq1tsWNm5Nj210sy5NJ4iny_RQYRL6cWBnIkBQIHKer3Bb8T5zMjB5OTip-bERQthw-uumfyHHSG9-_60MlgqQ7FJUAW4SbFNhpH6lr48r6Ou4tgB7WpIJgnGcGLJcfVXzBUIbNybX5FuvxhwQhuu9WGYuwInuM_MUHq_QvJjoKqPyKLOc6KapNXjzvU6eyxMTkHyYr2ncnvcLCID-F0asGTadk60Nn4x4FZV_2-OGbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50daff1723.mp4?token=Gz4IXRqCpKOaMg3Ovn6FV9N307PjjCrRPn7kVe3bEQ5O5M1nIhXE8AEF5V5EbFlEACUiW7ZvuzQGZvnSL6b6uvyfUc-OSMg9XIzl5IcErqjq1tsWNm5Nj210sy5NJ4iny_RQYRL6cWBnIkBQIHKer3Bb8T5zMjB5OTip-bERQthw-uumfyHHSG9-_60MlgqQ7FJUAW4SbFNhpH6lr48r6Ou4tgB7WpIJgnGcGLJcfVXzBUIbNybX5FuvxhwQhuu9WGYuwInuM_MUHq_QvJjoKqPyKLOc6KapNXjzvU6eyxMTkHyYr2ncnvcLCID-F0asGTadk60Nn4x4FZV_2-OGbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بیعت مردم مبعوث شده با حضرت آیت‌الله سید مجتبی خامنه‌ای در میدان آزادی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/akhbarefori/656126" target="_blank">📅 19:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656125">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2a6ae89b5.mp4?token=Ih_3yR4pOxOMEjxbQ9nfLQiHtTsBpUrlRiuTkeiyh9NQydBW_-u9cnVaiG8DnofqSe0GLWhhHnW0gl07Tn_0sX3EnXn75ET62F1ib9JaOYbxybkI8lI6u_y3miDsCgcP3lMyxX0c-Z_OkwCX5k3kdeXnDN6QnbSOBecc3HGH6SzPweQ2nFKkguyGtNpfnx5iS9Jx7RO1WKsrW9lgMI8c1IOE7k5fUg3vPf8lzAS1WTiBXIaCFT0Dcs8zUohL8NeCnsIF30UbJhz8GnfRnhT06LRMfkK8l9h34L0s2QLR4RKHOo_LgPCAwiMiIPb8bXFoCeqnnMD_wYGqmdCazEqBcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2a6ae89b5.mp4?token=Ih_3yR4pOxOMEjxbQ9nfLQiHtTsBpUrlRiuTkeiyh9NQydBW_-u9cnVaiG8DnofqSe0GLWhhHnW0gl07Tn_0sX3EnXn75ET62F1ib9JaOYbxybkI8lI6u_y3miDsCgcP3lMyxX0c-Z_OkwCX5k3kdeXnDN6QnbSOBecc3HGH6SzPweQ2nFKkguyGtNpfnx5iS9Jx7RO1WKsrW9lgMI8c1IOE7k5fUg3vPf8lzAS1WTiBXIaCFT0Dcs8zUohL8NeCnsIF30UbJhz8GnfRnhT06LRMfkK8l9h34L0s2QLR4RKHOo_LgPCAwiMiIPb8bXFoCeqnnMD_wYGqmdCazEqBcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عضو مجلس نمایندگان آمریکا: جنگ با ایران به هر خانواده آمریکایی ۷۵۰ دلار ضرر زده است
ریچارد نیل:
🔹
به‌خاطر جنگ با ایران، آمریکایی‌ها برای هر باک بنزین ۵۰ درصد هزینه بیشتری می‌دهند. گویا آن ۱۷۰۰ دلار هزینه‌ای که تعرفه‌ها روی دست مردم گذاشتند کافی نبود، چراکه برآوردهای جدید نشان می‌دهد جنگ با ایران هم‌اکنون ۷۵۰ دلار دیگر به خانواده‌ها ضرر زده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/akhbarefori/656125" target="_blank">📅 19:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656120">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromگرافیک قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cq1wWfYq__VQwCAE3ed3HFUQR97rTXft-bLTEB5foA9o1Iy9srrjB-nXL6qjmr9Al3YG0eY5Dtn9UcMGT2RvXh8H8NsxufJYMS5qILHm1tLKTQvC0E3tZusnUjWO2tPHKQUwDo0qd2nri5A5iij8KO2sXkfffWPo30xuaGkfzL_nsGMpA9kFcVYSCg7AaNCbuVQ9ZS1-jOV64_oEwBj9UYIbMGwsH_CWO1Pu_dTv_Rr4xu2vwegKyRO1N_JM2KEW9YKq2DrxgeC1jUlDVgUJEF_cvWgHMYO_ucQXt4StMpdpwe6dK83qs4Bs5CJxP6xBNnCGMf1gtvAymovJzz1nlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JEldP3RkdNEoQzlqp1mnH8noRE8RUjRcZFX0a04kmrTIWDZQg6HaLjiaxZZcGhHk0lxwvsbyxcIBJrnarYwxi9NIQi0Hl8AsoreLNcC0FCY_iIRXMCsgi2EdKE5hXLfvFz_QgvPT_WBmosDTIxJ8wjaH35o-ybpJVkg75yMTR-lJd9Q68NwGs-2rF3iL7AVfadMJsQLAK8ZOZytzSnAyfNFuocKdYdu_oZzrvdQI8_03T418HGxIkuZ-OuiREXuUQbmW01TElLtBYA252bsUXfferUIo7xsinTT85ZA7spdM6vaSlQmeYTHzHExy-J0r3Bw2tTm3qmcZTaY8EjsZKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cHm2oOUBIjQ-mY1Cv6hMsJ-mqYSyQrn8YuVsRuHb1gZsWUzJvRR-PfzdANjpVaMZR3Gs9elnv5VSK_JxHhWEw0jnQk8BQ2zqNacnSpi4svhNT9dAIF-rBblS7bCVWVPJHLydAWLUocNcfotMmr2GnQXG9qmUOEyjPIIqupZwnp_hULhmnSAuJd6kXBUCmPd8QtlV7sJIV6cNDyGNcbimOJorpTzxy2vGldVQIQYGyrkxAbvxaIAbcJYMSA7omcmdGJk56ZqO3TovQB4fBkV8lIt95BhjndE_Jdexa0crLvMIieuJP7i5q6KX-jz83JEtmL4bhFcoQxbzM_RusU3wLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t1h77nxUd1nj4EtLt8MSRPmZj3HUBReL-8KV79CmQg2kMBNbLsASPQnWPHzbCToD6FkomZLA7nm7t3PeccO8f0fzv7lfSvhKfoautZwWlDem1YBq9AIG9CQ1wN2YlGN7Ub4jIR2-FSAej24iF7jHNqTAh5nNxVbEspzIGWuO9s3Cm3ontiF2WscVYi77up_Z1QIbVSTl3Z3xcVqg5ksxV7qa-LzKtQu_1lxnfkCMuhcJ3GP-OELW-9gHXcaATAQ2TL7Odg8evPTjtJB87lAPyOEn_W8z-x4TO2YKxZ8-GqhbXWeEe5-BamaYS_e94HJvclI7MQ2mTrJfnayhu1D_gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nwb9N4zjlOofPewtni2TEc6k2AdqFPhlM5jqqp_p2irIOY2uiNuhaahzArP6_xohzMBtQ3oObIjG4ctF7g7KaZA_kpIm6V9z7ehGY-wN-uLYElLe5ooTMfeA4YvgYLm7237dtG9ol0K7nteVp5e7hc_IOmwQdyCnsDBsYeaERqipHEYVI7PSPg_Np4jQFc_VnzOWOpInq4VjdnQ-EYLjM13zTb8XWC1Zyj1_vOjbdmcCC_8TXD-7ZWmUd0e2qb24EFOePBPshjvZx8kvnpX-zRoDM6hQbw8vYUKzLrBvhw8UTjrHvemQgcur5bFtHrsR90oi3FDqXWHqj4mYvAfKww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✨
چه افتخاری بالاتر از این
که دل‌مان به عشق تو می‌تپد
و سایه‌ات بر سر زندگی‌مان هست...
#عید_غدیر
💚
#بک_گراند
#پس_زمینه
#پروفایل
#والپیپر
#امام_علی
(ع)
گرافیک های خاص مذهبی را اینجا ببینید
👇🏻
👇🏻
@gerafic_gharar</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/akhbarefori/656120" target="_blank">📅 19:24 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656119">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y_ABjVw8RetJYhmlqcE6S7_qR_cUY8XKXx84jtOrfQ7WRjhIRqk0VEw7KO70gy0gtuFpuCQIQclPgs5mlPbu6MjkB6bnBH3gTidD6QshDdownrp5TT8__0NUlFC5gM8xZhJIbHwAi2oGlpLfXm1DOoS9banieshZDTOODiArmbJRBzcQXpx1zhrMnujh_N40bAkYBPp1qpZOsVE1gSbzOzYK99DClrNZhcfd8t9fiPrcQrIqVSLcDRIQlgzO1aBrwGNKHYJYsjWDe_zXcs9hvTwp8g_PW46lP31hGtUZnYLNPoVdwcKHKcJFRjrQ0qomptQMxGZYKx5SYeOhOthq9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تمامی استادیوم‌های جام جهانی ۲۰۲۶
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/656119" target="_blank">📅 19:15 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656118">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kdnVVz9-35ksaeqp2M6iADlJtSpKCe6t3gIXUnu33lUx7uik7BtNhDLs-lBcYt5OdYcEY_FXoG-39aGoYxaJg0ds4T0wB0lVPI9-seyMCXSAzKiWKqZ7pT1uuFYXSuE6VYW85NSlSyhjR10tQj5aFI5OOPh_3JZPapMeItiGE9wkACFoRqh9-FHzSW0vblYxQco6nkfmhY9X61dRFWxkxTc8Dq37Mf5hsyH77wVpWipXe3ofL1dbXYzrvQRnwm6e6VO1W7DQeX4ZhOhYv3Z3LjLEc8gcuxeKSg0-hpQptZo8DG6WDB8kYA4CAmZhmjcbt-kodxdf6Lwxe4eSktj9tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سردرگمی عجیب در اعلام روز کنکور و امتحان نهایی/ کنکور رسما بحران شد!
🔹
مساله کنکور در شرایط سیاسی – اقتصادی کنونی سبب ناراحتی و یاس بسیاری از داوطلبان و والدین آنها شده است. نگرانی از جنگ و تداوم آن همزمان شده با تعویق پیاپی کنکور و مشخص نبودن زمان برگزاری آن. این مساله سبب شده بسیاری از داوطلبان از بلاتکلیفی خود ناراحت شده و نگران آینده شوند.
گزارش خبرفوری را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3219943</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/akhbarefori/656118" target="_blank">📅 19:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656117">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
توضیحات دختر شهید لبنانی در خصوص کلیپ جنجالی پخش شده از او: وقتی گفتم مردم لبنان منتظر کمک ایران هستند، ایرانیان خارج از کشور به من فحاشی کردند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/656117" target="_blank">📅 19:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656116">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3502ccbb01.mp4?token=UPRir0z1RGOr6tTP5TdvUQEc1kpBsj8iCyMrKnQR4iD29e5RrgK2faP7o2x2wQJNFGnBxEP7x6RUDPPWQl-MhXbIPaZTLo6g3JuO6hOxD27rzU6bFYOVmCxG4DUZABRHX-Yft4-siZlnHrGX3GIhFVYgSNiRdyrdgppgN2CqXT200tJm4bG4Z8vHdXnBRDwyzJQpvj5DOXDQ6wOFKD_jwzzIB6cYytOsFm8wi9oDROph3coOBnsxZvlC_BS8-Qny65Nyz2rgyWkT3ogfwo7fT3oMUbLdzLkpIk0rtgSRmGA1Vit7pIFmxfZyxvY-wfo2ktD9ECnk0BcVKIyASm_xdrLw7V95f3W-Y4FEyPdXgVAQkufig36DELArJJ3Gh0pTo6ONZhvvfw2KEKTjt9TejTK3AuVUB4-qkHK10uFH7VZsMN7x6GCLbv83_DD2qQGBwNWdeSm1lseWP13I1Lz7b6kBQ4lkOMBi-aiWCJXjW4tU8NyCEwrk_Hyb_ZRbV6iR_U2qJFQMMN1NLbCO4MkoglYkBuU2VR3f55dPIa5V70Uc76O5RPF5yAbVru_KmfQKLIq23FTrjlVn2AjfpS9jb026CZl5qiE0WPFvbYjBNHLYnPYgjc5rNscKADYtD9c0wgxMWFINQPbZ-GVsNpIE15bb3C7pBdqtAgmOVMyihJY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3502ccbb01.mp4?token=UPRir0z1RGOr6tTP5TdvUQEc1kpBsj8iCyMrKnQR4iD29e5RrgK2faP7o2x2wQJNFGnBxEP7x6RUDPPWQl-MhXbIPaZTLo6g3JuO6hOxD27rzU6bFYOVmCxG4DUZABRHX-Yft4-siZlnHrGX3GIhFVYgSNiRdyrdgppgN2CqXT200tJm4bG4Z8vHdXnBRDwyzJQpvj5DOXDQ6wOFKD_jwzzIB6cYytOsFm8wi9oDROph3coOBnsxZvlC_BS8-Qny65Nyz2rgyWkT3ogfwo7fT3oMUbLdzLkpIk0rtgSRmGA1Vit7pIFmxfZyxvY-wfo2ktD9ECnk0BcVKIyASm_xdrLw7V95f3W-Y4FEyPdXgVAQkufig36DELArJJ3Gh0pTo6ONZhvvfw2KEKTjt9TejTK3AuVUB4-qkHK10uFH7VZsMN7x6GCLbv83_DD2qQGBwNWdeSm1lseWP13I1Lz7b6kBQ4lkOMBi-aiWCJXjW4tU8NyCEwrk_Hyb_ZRbV6iR_U2qJFQMMN1NLbCO4MkoglYkBuU2VR3f55dPIa5V70Uc76O5RPF5yAbVru_KmfQKLIq23FTrjlVn2AjfpS9jb026CZl5qiE0WPFvbYjBNHLYnPYgjc5rNscKADYtD9c0wgxMWFINQPbZ-GVsNpIE15bb3C7pBdqtAgmOVMyihJY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
موزیک رپ دیدنی برای حضرت علی علیه‌السلام
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/656116" target="_blank">📅 19:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656115">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bkp10qL59Sed2UeLlh2ayO0ONsYXFXKYEkYR-LVwr9kORavEMf54cQPnym4LzHACvPBaqOlVkLnB02Plv1x29BmmH24YnPNiTgVNNbyDY7SgkB1aVA7M0OpCur6InuxLIgI75RJoXwYI5rZ4BlXGtrCpBnTievWAzJnJ4C1pbZQ10diZLeY3BIjw7sWuv--w-hzYieAsSZzi7T3Ijkm0-UMin3yBm9oJVjKRzfixDtXPCtq0dI1UIE_pat4JH1UwC_SaoIxI9rAiw54p4SKOu6VK3mSGqBJiEINZvxMqHYXAVQpJrrl45MVmEYCebDxBWY7Q6RubO_4GHfHp-gWHRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
فرصت ویژه خرید از چرم مَنطِ
تا %70 تخفیف
➕
%10 بیشتر
و هدیه 1,000,000 تومانی اسنپ‌پی
برای خرید «حضوری و آنلاین»
کد: PAYSS9R
حداقل خرید ۴ میلیون تومان
مشاهده محصولات
👉
manteofficial.com
📍
سیتی سنتر، طبقه همکف</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/656115" target="_blank">📅 19:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656114">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lp_PA2kD_4AvZYu13b9MQkeeJMgDRs9XSz1UoijI6U43QGoPnVq3HEADiJmYX9ktuxXiyFyuY3ghU0iCdHZp8IxIt5QRNwkWNgkYrJjV6OvQugfmj-z5YpwGQ0lxiLkZOKJB2VCcfjjRfo_yXXIb540jPDqE10WsUwVwyVJXjpV4flrKCOjefSWX57I5IGk-qwOX0ANZMraaQpdd2E4rWXr5TABOYk-egeeiVlgqRvzveB88JLvh9DNL34SVZxR74Tbc1r_-sWnHxySYQvAo6-8wxw5TRUJXiZvI3US94ylvlHFtqFFAIGTT1cwTsmlZYMLU5FYmlFCjY8Za89sU8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۰ کشور برتر تولیدکننده نفت در سال ۲۰۲۶؛ ایران و آمریکا در رده چندم هستند؟
🔹
بر اساس آمار سال ۲۰۲۶، آمریکا با تولید روزانه ۱۳.۲۵ میلیون بشکه نفت، بزرگترین تولیدکننده نفت جهان است. این رقم بیشتر از مجموع تولید عربستان (۱۰.۱۱) و روسیه (۱۰.۰۳ میلیون بشکه) می‌باشد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/656114" target="_blank">📅 18:56 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656113">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uyrYvjxpHB5d8IKhDwxaa7V2SZMYrSQp_HX79A9rVuJjJY2dgxJer9N9TEj_vV4V4XcIfRNfZuyr3PiauY0dn_MTuzLmUjEq9Tzo9AnnCuNCG4FuO62XSP9JaRf1WrTDk4rnclztaTn6nAsdEXVoBbPaT1S4g4YxsQohFO96c5CY6n7rsf8RGmxASZcRLT1sfaZl3SG65wiurnIzj9klPShegt8XHoMEeQ8NMkjp-mmz1sBQOkQyqYGttjK0iTxbeZ281GMNblGNYXy8oJGCepW27GsM8wD2aRCpWsvMte5cZ5Htm9B2HVZcA6gILsPa0isfcZKws5eN2ATozO-hFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
دعای مردم برای سلامتی فرمانده هوافضا سپاه
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/656113" target="_blank">📅 18:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656112">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iw2IouDTYPlu2wI8vFJzK-s5YGNmQl3M6uQ41ne0QLSydZxNpdLegkoHLhH1eOumCUCcziMTWItlLCexLrHGUe9Qlvl0jTH4on6Ii-FUOYAy3lmGvsUS7WhcP6h_P7_ZHCLFxVmzkPciBNI8Dq65PkIPQ4ZKNetw1U8Vnv6AkPSgAC0KG5cRmowy-5CxzOWNl-chF6bFNJe-1tqCmh-BcQ8zbLTsfXu_fwY79v4GSGY13jsoD6qLF34rwdRUKDyoFFn98_sRjSVPfTiUs77LwTaq2n3E3unH_9STnzbkzip-Wgqq0q4wl_V1IkeRhUzaR8j-gcCTKM1wlW-KulIRHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/656112" target="_blank">📅 18:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656111">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0BNomBIHUVHfOc1ggHKdG7PrNt-upHTsDmilKm_Jc9d9Iv28eCYtIxSb8cfY0cAqaMFNji5tR9uc3IVl0RDw9uZapYy83t4oB9RdXubjwiQnryjia_mMcndFBjgNo_MLe51MH4B8IeZUK6vOkWo272cPnFAxFULyjUzEjX1LvY9Yeoent0vgm65J8jjL8P6pbWeZ_my6yA46LuNIlkft170SlwytcIbeZQXQryy82QrtAt9isEpmlUHJ-otrK9kLuJF997u-D0rGc2-f4lI0UAGgVgMFoWWAAxvoOvieiWZbDUlo8T6LpGh9M62tvjVFBTgz6pQVpxmXAvn9MKH7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پشت‌پرده اظهارنظر ترامپ درباره رهبر انقلاب/ نقشه جدید رئیس‌جمهور آمریکا چیست؟
🔹
ترامپ تلاش دارد مسیر خود را تغییر داده و به نحوی دیگر با ایران برخورد کند. شیفت سیاسی ترامپ را می‌توان شیفت "چماق به هویج" خواند. او تلاش دارد از طریق تغییر لحن، سیاست مقاومتی ایران را بشکند.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3220287</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/akhbarefori/656111" target="_blank">📅 18:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656104">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8f00fcfa3.mp4?token=D06VdG_cMECGGGZciLlcI3HSAhl_lkcXe5R_z7UP1-u2d2avKowd-GA3C0CB005aNvqUB0QpJnzQ9DC0Q8CgrhM2wCTkofQf5nCRS03m83SYdWvhV8tKrk1S5m4Bgd4mG6p6mZuGS1wYe9vBz20tvwQXfCvdL0zvHPoHoWNYrrYPZaEx0yAlOB16RX0DgJyFPaY0BsU30fc4Obn_b9-5yhdg7BfawRUBb4qstqOl50Z3HvuZ337bYLQUHWK20K5QEZojoCSFdyTb_gj5d4fQ3lnk1wwVk3xnWCGaLOHfuQzQnNqzgfHbVEpueFTPB3RSo9Edem6SCFCOfcCweJBN2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8f00fcfa3.mp4?token=D06VdG_cMECGGGZciLlcI3HSAhl_lkcXe5R_z7UP1-u2d2avKowd-GA3C0CB005aNvqUB0QpJnzQ9DC0Q8CgrhM2wCTkofQf5nCRS03m83SYdWvhV8tKrk1S5m4Bgd4mG6p6mZuGS1wYe9vBz20tvwQXfCvdL0zvHPoHoWNYrrYPZaEx0yAlOB16RX0DgJyFPaY0BsU30fc4Obn_b9-5yhdg7BfawRUBb4qstqOl50Z3HvuZ337bYLQUHWK20K5QEZojoCSFdyTb_gj5d4fQ3lnk1wwVk3xnWCGaLOHfuQzQnNqzgfHbVEpueFTPB3RSo9Edem6SCFCOfcCweJBN2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💚
پک استوری ویژه عید غدیر
💚
✨
غدیر روزی است که دین خدا به ولایت علی (ع) کمال می‌یابد...
#عید_غدیر
#استوری
#امام_علی
(ع)
@Heyate_gharar</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/656104" target="_blank">📅 18:27 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656102">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nj343Yz7CXzcHLj_hOlK6LUmlNqFPf_RR5_8JalSniwmndkP_QzLfSe2-5OerAt3FbNbB2GmWf9kr4gY9YyQwiIvZLPJzn4xDuCkZu-_TNh_y64QIoAx0N7PMvlHQ_r5MPK4ETxzgQ263nqk4anSy_xkesWWCL5UMZCZdpJngiqTFPJIScrLjdBv2hIK12IA_hNSZosonl2kB7ucFakpE0bdPA_WZ6hNDcMNPBwXFiApbKwluN3-EpeyIiNgQMaKJJI-v2E5KGWW3i9vRuxY2Z5MPkFTF21riFCPEb1xscuIzAWgSue2Aq0cYqPiXWqcNsC6zk5C4yA1n_EGCd0JXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
امام حسن (ع)؛ اولین سفره‌دار غدیر
🔹
اهمیت اطعام در غدیر چنان بالاست که در روایات ثواب آن را به‌اندازه اطعام تمام پیامبران و صدیقین دانسته‌اند. شاید جالب باشد بدانیم که نخستین کسی که در روز غدیر سفره‌ای به وسعت یک شهر پهن کرد، امام حسن (ع) بود. #جرعه‌ای_از_خم…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/656102" target="_blank">📅 18:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656100">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MzVBnc9Zv2cVVaiPsfaU1l6gu3-8nIY1bRYBe0Kj7uKliGbuFRyFEmE8tR4RVc-aUbHNOm69p907dLV5VAuZ97XpzleT3ogNJAiOiRWqzy-NVQUXNqCT_fwBiDhoCmWppqQOUj2rdGFj892pIS0e0ePobVXogq3FCe90YGU0ukzuh_4TV8ha8pv1-vqfm2O3MJX_LEwy8vrjyOT0KBbbud_2BwMLv2_G4Udg54A8F_hA6fqovdmp4oeQxLIATzSTyUiO_xbEdbhFT4LQ8LS7yP2XqCyiVSEEpag2cMSniGQ-4hLMWSKxYjHxIHishIqvzacd8I3iCRlIkui2Bsj4Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای خرید این ویلا و مشاهده قیمت و عکسهای بیشتر به سایت زیر مراجعه کنید
👇🏼
:
https://melksell.ir/
نور
📍
۳۵۰ متر زمین
۳۵۰ متر بنا
تعداد خواب ۴
نما مدرن شخصی ساز
دسترسی عالی
سند تکبرگ و مجوز ساخت
دسترسی عالی تا جنگل و دریا
🔻
برای خرید این ویلا و مشاهده قیمت و عکسهای بیشتر به سایت زیر مراجعه کنید
👇🏼
:
https://melksell.ir/</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/656100" target="_blank">📅 18:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656099">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9300b4e3eb.mp4?token=AgaNS3pwLf33jl1C5cjFaH4wxMdctVAc35gGGtf0gKPzNrm1egG04Q-TkfRI0E88tfsNlHKsuForNUVXx4LeuwQsVbUotJOnVuVJnuN2WoiQTTrJMZ9ywkaXWwJ8zizJatO6qmy9lA0pcW5uHAhT4vJHsnraEnMhhkJhspXvY6UXCjA6TCjd2lNkPGo28VyhhuG4p1Pi3vdoKxjd-Y66svnfBBEVo2d2gdaUjlmElFDIbZO8M4nFxqUehsOUbqFtdkT8GZXnVpVFcIebQqKMnn9wa7IiiGP906JQzO_jT6WjBjYlWIqDisMhDkUi3Xf-aCnFkBay6IoplN_dT-jquw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9300b4e3eb.mp4?token=AgaNS3pwLf33jl1C5cjFaH4wxMdctVAc35gGGtf0gKPzNrm1egG04Q-TkfRI0E88tfsNlHKsuForNUVXx4LeuwQsVbUotJOnVuVJnuN2WoiQTTrJMZ9ywkaXWwJ8zizJatO6qmy9lA0pcW5uHAhT4vJHsnraEnMhhkJhspXvY6UXCjA6TCjd2lNkPGo28VyhhuG4p1Pi3vdoKxjd-Y66svnfBBEVo2d2gdaUjlmElFDIbZO8M4nFxqUehsOUbqFtdkT8GZXnVpVFcIebQqKMnn9wa7IiiGP906JQzO_jT6WjBjYlWIqDisMhDkUi3Xf-aCnFkBay6IoplN_dT-jquw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عروس و داماد موتوری در مهمانی غدیر تهران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/656099" target="_blank">📅 18:16 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656098">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">بازی و تفریح کودکان در مهمانی کیلومتری غدیر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/656098" target="_blank">📅 18:15 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656097">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dz1bSPS7wVtfSMZefUNDsSwW7ZZNXxdHuEgNNFaFk8z-5AQ6ViSwqPGG3H4VZDkhnwppOOkb-H3tXPUSl8OG8PJYMRwCxq7Erzaj4CP095WYM4YGzJ-FiXXgk5a-6TaZyXf7cerR9F8FuyL3exYx2VDU5GCmEBB0E4xRrLv2KO8IvfKZWtIUndTaNlEfIQuUKqpSDIywJFcUbEssQLnvl4NPqUuNikeGXxMWxfGOrFEKoDJQhvdUDtXZNiIOkAJi5RsSsS47lLARW_VLRLSdJW_nrOhptVhSugMQCU4TPGj-bivDC_JxCur-z73FpfuSmyWQmGbwkiYuG99WudyhbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استقبال عجیب مردم از مهمونی کیلومتری غدیر
🔹
تصویر شبکه خبر از حضور میلیونی مردم در مهمونی های کیلومتری غدیر در سرتاسر کشور
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/akhbarefori/656097" target="_blank">📅 18:15 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656094">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dgK18iXpqSkWA604nPTmDvYao4NnNRsIXUlDfwFo2W5dFDqSuBOSYmWhrQkhtRgtoxmTldmK6mPxiw9NOuwmJKnBEYO8_NY82aEZBWdGdkIlI6zF3JPRQHpfAdRr3v12rtl7GaX0VM73Cm8OZT2TuEI5hRPPc6OIG1_laMURgtPJlaj9Fhml5mV_vJhXsxf4RTF5UGeBT8xHu9Puaj9AYjPJN4_3JpV-6z2Ae8cypBTMSPT5MZFCio7V5-NSJGQGTH8WfI1iYwY7udptAlK-zBIJnGgl3zOb66bf5I9M7W0mUD2PS7cj_NbVfdB09xp3PEy8BKPC3XdHqLmTg0XRtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اخبار مرتبط با برداشت ۴۵ همت از حساب سازمان تامین اجتماعی صحت ندارد
🔹
روابط عمومی سازمان تامین اجتماعی در خصوص اخبار منتشر شده مبنی بر برداشت ۴۵ هزار میلیارد تومان توسط بانک مرکزی از حساب تامین اجتماعی، را صحیح ندانست و تکذیب کرد.
سازمان تأمین اجتماعی در واکنش به این خبر اعلام کرد این منابع در قالب خط اعتباری بانک مرکزی و با عاملیت بانک رفاه کارگران برای جبران کسری‌های ناشی از شرایط جنگی و کاهش وصول حق بیمه تأمین شده است.
🔹
در جریان جنگ ۱۲ روزه، با کسری ۳۰ همتی برای پرداخت حقوق بازنشستگان مواجه شد که با تخصیص خط اعتباری بانک مرکزی جبران شد و مجموع استفاده از این ظرفیت به ۴۵ همت رسید.
🔹
همچنین در جنگ رمضان، منابع سازمان برای پرداخت حدود ۴۳ همت عیدی بازنشستگان کافی نبود. در پی توافق وزیر تعاون، کار و رفاه اجتماعی و مدیرعامل تأمین اجتماعی با رئیس کل بانک مرکزی، ۳۰ همت خط اعتباری جدید اختصاص یافت و عیدی بیش از ۵ میلیون بازنشسته، ازکارافتاده و بازمانده پرداخت شد.
🔹
تأمین اجتماعی تأکید کرد همکاری بانک مرکزی و بانک رفاه در تأمین منابع مورد نیاز بازنشستگان و ارائه خدمات به آنان ادامه داشته است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/656094" target="_blank">📅 18:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656093">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">khotbeghadirpdf.pdf</div>
  <div class="tg-doc-extra">665.8 KB</div>
</div>
<a href="https://t.me/akhbarefori/656093" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✨
متن عربی و ترجمۀ فارسیِ خطبۀ غدیر
▫️
در خطبه پیامبر اکرم صلی الله علیه وآله است که درمحل معروف غدیر خم و دراجتماع بیش ازیک صدو بیست هزار نفر ایراد شده است ، بخشی از اسرار ولايت بيان شده است
#امام_علی
( ع)
#عید_غدیر
💚
@Heyate_gharar</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/656093" target="_blank">📅 17:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656092">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59ed301c9b.mp4?token=nYvaCLfrN5MtlVM8mqjuJobNhTWOoCQbaLGh8UV15GdTc5sfS8tJF4WXDXbtA9dFIRwkvidBj9JXWQ46t7pc13ErM5jlvHE5d9ciQBzhs0hNUeDTxVNN6u90-Wy1eIuhhZIhVdqioBx86nXta2aSgidY4jLYycHeXY3gNwSc7QWoOUgV_3qfN_JwwXs8cGiPalZ9nXUfaQKAnFvEv9TSpHVAJyPhIfSFrvUDx54fWnLx6rQWrMpH0-8i1T3B0VBMWNwj4OI0metNxSuK17gxBRbcR7UJJ-RRmR9C0gMZEyKYFXs0YSnldngxqdYeOExBLc4j5EyI5C4IrX7KzO1FBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59ed301c9b.mp4?token=nYvaCLfrN5MtlVM8mqjuJobNhTWOoCQbaLGh8UV15GdTc5sfS8tJF4WXDXbtA9dFIRwkvidBj9JXWQ46t7pc13ErM5jlvHE5d9ciQBzhs0hNUeDTxVNN6u90-Wy1eIuhhZIhVdqioBx86nXta2aSgidY4jLYycHeXY3gNwSc7QWoOUgV_3qfN_JwwXs8cGiPalZ9nXUfaQKAnFvEv9TSpHVAJyPhIfSFrvUDx54fWnLx6rQWrMpH0-8i1T3B0VBMWNwj4OI0metNxSuK17gxBRbcR7UJJ-RRmR9C0gMZEyKYFXs0YSnldngxqdYeOExBLc4j5EyI5C4IrX7KzO1FBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تلاش نافرجام جوان برای نجات توله‌سگ گرفتار در سیلاب؛ ویدیویی که کاربران را متاثر کرد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/656092" target="_blank">📅 17:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656091">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/deac8104a4.mp4?token=KDXsqhoyCKT6Y5wLt3Tj3kjfywoHMOGX7DT-YXCV8zlJ08N-UpG0vFgztgvr93XtX5M1IWyBzLY7at39dUcNRmBovSw7oGFc54iYZX90hBgj_3WLgdvYgEwf9zUVWXAOfBbO_mHE7fN8OPKWvcTtfaqtWOl79D809wqEDUigyKp-abrYUSlt1LjOtVc8FYxkLe6vJ6IgyWTEgf7CgMl7rflHa73U4Pme9kroWqxMotstdq00V77akzVMZN186zDUHLPbRObqYNHkxhCuA7LexMh_SW_ifQf77wpwVLZo0_PVlorjpdA4xsHAM-yYgr5O8pBYKosLa7DVTUU2rgZZ4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/deac8104a4.mp4?token=KDXsqhoyCKT6Y5wLt3Tj3kjfywoHMOGX7DT-YXCV8zlJ08N-UpG0vFgztgvr93XtX5M1IWyBzLY7at39dUcNRmBovSw7oGFc54iYZX90hBgj_3WLgdvYgEwf9zUVWXAOfBbO_mHE7fN8OPKWvcTtfaqtWOl79D809wqEDUigyKp-abrYUSlt1LjOtVc8FYxkLe6vJ6IgyWTEgf7CgMl7rflHa73U4Pme9kroWqxMotstdq00V77akzVMZN186zDUHLPbRObqYNHkxhCuA7LexMh_SW_ifQf77wpwVLZo0_PVlorjpdA4xsHAM-yYgr5O8pBYKosLa7DVTUU2rgZZ4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فوران بی سابقه چشمه کوهرنگ/سرچشمه زاینده رود
#اخبار_چهارمحال_و_بختیاری
در فضای مجازی
👇
@akhbarchaharmahalvabakhtiari</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/akhbarefori/656091" target="_blank">📅 17:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656090">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a8c2303b7.mp4?token=TLyqeKE-XL9vW80vcyyAwDVRJlyOgYgW7jyUZ1tg45ElQoQ96c-JQckaHqQMTiQo2JEVLx7wc5izg8qumhcRGQeK8NP4D8j7mU-ULOkprX9FvBNlAP3lGkCnU7JMr5NOT0nhFSZ4F9r03KuwIkqipFUZUMiOAZzQuDXy1bTC60IM9_uuy2dO5aQFLpjx5joBc0u17oae3llN6FMn9wQWgoZKc549a7JC_mN2jRQ_Ifk4-6mJxFDK6oQ1BERQAKI8zPaa_WWlS04hU0Haf5p6jZLu8NK595HyfyOeRa1JsMLb6xxk-y8nry6JT1FRjByEIyMFNMpLKA1bYJaBiqgUOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a8c2303b7.mp4?token=TLyqeKE-XL9vW80vcyyAwDVRJlyOgYgW7jyUZ1tg45ElQoQ96c-JQckaHqQMTiQo2JEVLx7wc5izg8qumhcRGQeK8NP4D8j7mU-ULOkprX9FvBNlAP3lGkCnU7JMr5NOT0nhFSZ4F9r03KuwIkqipFUZUMiOAZzQuDXy1bTC60IM9_uuy2dO5aQFLpjx5joBc0u17oae3llN6FMn9wQWgoZKc549a7JC_mN2jRQ_Ifk4-6mJxFDK6oQ1BERQAKI8zPaa_WWlS04hU0Haf5p6jZLu8NK595HyfyOeRa1JsMLb6xxk-y8nry6JT1FRjByEIyMFNMpLKA1bYJaBiqgUOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تنش در آلبانی پس از خبر ساخت جزیره منتسب به دختر ترامپ
🔹
پس از انتشار خبر ساخت یک جزیره در آلبانی توسط دختر ترامپ، فضای این کشور متشنج شده و اعتراضاتی شکل گرفته است.
🔹
معترضان شعارهایی علیه «فروش کشور به اسرائیل» سر داده‌اند.
🔹
برخی تحلیل‌ها نیز از افزایش حساسیت افکار عمومی اروپا نسبت به داماد ترامپ خبر می‌دهند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/656090" target="_blank">📅 17:36 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656089">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
سپاه: هیچ آرامشی در منطقه بدون عقب‌نشینی صهیونیست‌ها از مناطق اشغالی لبنان برقرار نخواهد
شد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/656089" target="_blank">📅 17:28 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656087">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
افزایش مبلغ کالابرگ در چه صورتی خطر ندارد؟
کامران ندری، کارشناس مسائل اقتصادی در
#گفتگو
با خبرفوری:
🔹
باید دید مبلغی را که بخواهند به کالابرگ اضافه کنند، از کجا تامین می‌کنند. اگر از بانک مرکزی یا شبکه بانکی بگیرند خیلی فرقی نمی‌کند.
🔹
اگر از طریق خلق یا چاپ پول این مبالغ مربوط به کالابرگ را دولت تامین کند، آثار و تبعات تورمی دارد که فوری نیست و در اقتصاد ما نزدیک به یک‌سال طول می‌کشد تا تورم ناشی از خلق پول اتفاق بیوفتد. اگر از محل درآمد مالیاتی، ارزی یا فروش اوراق این وجوه تامین شود، آثار تورمی ندارد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/656087" target="_blank">📅 17:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656086">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJnZDd3IKDkOH4uduM-C9CbR4kMiAhIhJXBs_zTHb-xEJ9BwYdl6n5qzVa0oB84dSGcf1Fp70OfwoUs-3zIdIEEkMPtPGeAVrisEL-Hu-1MaK5f9Fz5VbLc9hStbYEj2NTq5WBURtqPuNUNEuE8XviC7iwdV_F_8hyfGz7KC2rZIwIU1s5p4n6Et-ARfR2sGZGASypmtrzPAztvsBwH8uZW7DpK5CzWiHWge50aG5XuZGhSpQ0GW5q_RqVm7Q_fvkzdqdn6rWa4P0aHR8JLG6COH6wc_GpGCPgCRUGBHLg37b2ph5bVAf7vhzhUUuyMy5iMvUwi7h19BYJs-LXtp5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
نقشه‌ای از جهانِ غدیر؛ از نجف تا پنج قاره، یک پیام و میلیون‌ها دل #جهان_بر_مدار_غدیر #فقط_به_عشق_علی #LiveLikeAli #VoiceOfAli
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/656086" target="_blank">📅 17:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656085">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tV_yUNbUKsIn6dwLg9UBLhtmR6O1jDuA1Xa0tYK8ci1pI1trl1IncmwKln_YPM4SCS-iSAzE7qF_TAqQI_x0-JRS_zSUWnpJDmS38x5iUSKtMnhcfszDkf3njZfrAJPVlYVpvaZ9tTPiujpi6lIW8VCKgC7gEltkKAWHS6iODd8A_qwst8kgHhPY06qemYliYpvxNv-Ex92Sk1B2NOb_T1ClpGyJ6jDPARwVXCy2Qe8zcXzkbV8QZsQnzZ0uTuDqLrQHthTr9ZS5Ujy5hU-GhSOn2n8trZyu815cH9KNNK2JCLFcisIlrKsuKxqblkJsKg5IylYMPfOgAaGqgZ0wyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مذاکره استقلال با اسکوچیچ/ چند مربی دیگر در فهرست آبی‌ها
🔹
باشگاه استقلال برای فصل آینده به دنبال تعیین سرمربی است. در صورت «فریز» شدن لیگ، قرارداد سهراب بختیاری‌زاده به پایان می‌رسد و آبی‌ها سراغ گزینه‌های داخلی و خارجی می‌روند. در بین گزینه‌ها نام اسکوچیچ هم مطرح است؛ مربی‌ای که قبلاً هم مورد بررسی استقلال بوده اما توافقی حاصل نشده بود.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/656085" target="_blank">📅 16:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656084">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78d7f591a3.mp4?token=d4-LjfstopLymRneAJ4t3boR-qqIZTL-0sjiOktocBL02CAZtQu8wQfR8HvLyyemT2aC4cbWJKtQJ0g7ssxQY9Ks_A91ll4qvcRxO5ktCkF_MNVMhENmuDK9GsWnTonxTRymgqYvhwvClNFVyOkT0GC64Q_7Ime-sUc_-s0yfnnPGT1Rn3oW6yIN3lhMsEoAwvd_dDXjJv8EvfdiGCIOKgIjXgucUvO4nK0zj44NUQlAYE15OTYoZ-btPxOHpED1l4FXzucrP-Tdxv2aB2EXU28onsg0nIiFKQFOtYrmvtuG1GpMrIMqGp3jXR0vQ0bMw6RT2G5ylGdI3nOyIEPqAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78d7f591a3.mp4?token=d4-LjfstopLymRneAJ4t3boR-qqIZTL-0sjiOktocBL02CAZtQu8wQfR8HvLyyemT2aC4cbWJKtQJ0g7ssxQY9Ks_A91ll4qvcRxO5ktCkF_MNVMhENmuDK9GsWnTonxTRymgqYvhwvClNFVyOkT0GC64Q_7Ime-sUc_-s0yfnnPGT1Rn3oW6yIN3lhMsEoAwvd_dDXjJv8EvfdiGCIOKgIjXgucUvO4nK0zj44NUQlAYE15OTYoZ-btPxOHpED1l4FXzucrP-Tdxv2aB2EXU28onsg0nIiFKQFOtYrmvtuG1GpMrIMqGp3jXR0vQ0bMw6RT2G5ylGdI3nOyIEPqAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بحران بنزین در عراق
🔹
منابع خبری از وجود صف‌های گسترده و طویل در پمپ بنزین‌های چندین استان عراق از جمله صلاح الدین و بغداد گزارش می‌دهند.
🔹
مسئولان عراقی اعلام کردند که این بحران موقتی است و به زودی مشکل کمبود بنزین رفع خواهد شد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/656084" target="_blank">📅 16:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656082">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
زمان صدور احکام جدید حقوق بازنشستگان اعلام شد
‌
رئیس کانون عالی بازنشستگان کشور:
🔹
احکام جدید حقوق بازنشستگان تأمین اجتماعی برای سال ۱۴۰۵ حداکثر تا ابتدای هفته آینده قابل دریافت است. مرحله سوم طرح متناسب‌سازی با هدف تحقق ۹۰ درصد همسان‌سازی حقوق‌ها، همزمان با تعیین حقوق سال جدید اجرا می‌شود. این احکام برای بیش از ۵ میلیون و ۲۰۰ هزار نفر صادر می‌شود.. / فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/656082" target="_blank">📅 16:28 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656081">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Sejjeel</div>
  <div class="tg-doc-extra">Meshki X RaaSaa X Mofleh</div>
</div>
<a href="https://t.me/akhbarefori/656081" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
سجیل
موضوع ایران باشه همه قشرها متحدن
تو رو چه به شیرهای ایرانی آخه سگ زرد
#آهنگ
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/656081" target="_blank">📅 16:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656080">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/136b67ba91.mp4?token=U6VIaRS5tanwmdkTSf49SFLsmKn4JnCBaZn_Ueke4cFtWzLdK6NhkzQ4a6BdwpgspMogHNM1KU4EYMko79uNGj29K2AAqRhsB6l2ePn5ONWLCtESpHvGP1T4x2WQA1Uw-sxCZvZjWRkAAH3SbGVTWQSoOKvWotdq-7wKfJtTW96KIPCnKwIq_3KrnYutZASwN-zN16tE4PyF6BbVvwSffrukR5Tl5lZz4dhPzXhF5a0JP6MqlyKzifoBsvXpMIJD1GMlJ6u9Lr6TjMxjfZGLC_wQgZ19o3Ap2wjz3tfzRPiB8HpJDKjo_Fy1XimfQMw4-OiJWskrjNRE7KNY52Iwtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/136b67ba91.mp4?token=U6VIaRS5tanwmdkTSf49SFLsmKn4JnCBaZn_Ueke4cFtWzLdK6NhkzQ4a6BdwpgspMogHNM1KU4EYMko79uNGj29K2AAqRhsB6l2ePn5ONWLCtESpHvGP1T4x2WQA1Uw-sxCZvZjWRkAAH3SbGVTWQSoOKvWotdq-7wKfJtTW96KIPCnKwIq_3KrnYutZASwN-zN16tE4PyF6BbVvwSffrukR5Tl5lZz4dhPzXhF5a0JP6MqlyKzifoBsvXpMIJD1GMlJ6u9Lr6TjMxjfZGLC_wQgZ19o3Ap2wjz3tfzRPiB8HpJDKjo_Fy1XimfQMw4-OiJWskrjNRE7KNY52Iwtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عصبانیت شدید تحلیلگر اسرائیل‌نشنال از ناکامی آمریکا در براندازی حکومت!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/656080" target="_blank">📅 16:24 · 14 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
